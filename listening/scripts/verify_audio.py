#!/usr/bin/env python3
"""Strict QA gate for the listening MP3 collection.

Checks source integrity, coverage, per-file technical quality, loudness, ID3
metadata and catalog consistency.  Writes AUDIO_QA_REPORT.md and audio_qa.json.

Usage:
    python listening/scripts/verify_audio.py
"""

from __future__ import annotations

import hashlib
import json
import re
import shutil
import subprocess
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

from mutagen.id3 import ID3
from mutagen.mp3 import MP3

ROOT = Path(__file__).resolve().parents[2]
OUT = ROOT / "listening"
AUDIO_DIR = OUT / "audio"
PDF = ROOT / "DE_CUONG_ON_TAP_TIENG_ANH_10_GK1_2026_2027_GLOBAL_SUCCESS.pdf"


def sha256(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()


def find_ffmpeg() -> str:
    exe = shutil.which("ffmpeg")
    if exe:
        return exe
    import imageio_ffmpeg  # type: ignore

    return imageio_ffmpeg.get_ffmpeg_exe()


def volume_stats(ffmpeg: str, mp3: Path) -> tuple[float, float]:
    res = subprocess.run(
        [
            ffmpeg, "-hide_banner", "-nostats", "-v", "info",
            "-i", str(mp3), "-af", "volumedetect", "-f", "null", "-",
        ],
        capture_output=True,
        text=True,
        check=False,
    )
    text = res.stdout + "\n" + res.stderr
    mean = re.search(r"mean_volume:\s*(-?[\d.]+) dB", text)
    peak = re.search(r"max_volume:\s*(-?[\d.]+) dB", text)
    if not mean or not peak:
        raise RuntimeError(f"Could not read volumedetect output for {mp3}:\n{text[-1200:]}")
    return float(mean.group(1)), float(peak.group(1))


def main() -> None:
    inventory = json.loads((OUT / "inventory.json").read_text(encoding="utf-8"))
    manifest = json.loads((OUT / "clips_manifest.json").read_text(encoding="utf-8"))
    tracks: list[dict[str, Any]] = manifest["tracks"]
    clips: list[dict[str, Any]] = manifest["clips"]
    exercises: list[dict[str, Any]] = inventory["exercises"]
    ffmpeg = find_ffmpeg()

    errors: list[str] = []
    warnings: list[str] = []

    # ---- Source integrity -------------------------------------------------
    current_pdf_hash = sha256(PDF)
    if current_pdf_hash != inventory["source"]["pdf_sha256"]:
        errors.append("Source PDF SHA-256 changed since the inventory was built")

    # ---- Coverage ---------------------------------------------------------
    if len(exercises) != 4:
        errors.append(f"Expected 4 official listening exercises, got {len(exercises)}")
    total_questions = sum(len(e["questions"]) for e in exercises)
    if total_questions != 20:
        errors.append(f"Expected 20 official questions, got {total_questions}")
    if len({e["id"] for e in exercises}) != len(exercises):
        errors.append("Duplicate exercise ids")
    for ex in exercises:
        if not 180 <= ex["computed_words"] <= 200:
            errors.append(f"{ex['id']}: {ex['computed_words']} words outside 180-200")
        if ex["computed_words"] != ex["declared_words"]:
            errors.append(f"{ex['id']}: word-count mismatch")
        if len(ex["questions"]) != 5 or len(ex["answers"]) != 5:
            errors.append(f"{ex['id']}: expected 5 questions and 5 answers")
        for q in ex["questions"]:
            if q["answer"] not in "ABCD":
                errors.append(f"{ex['id']} Q{q['number']}: invalid answer")
        modes = {t["kind"] for t in tracks if ex["id"] in t["exercise_ids"]}
        expected_modes = {"exam", "clean", "guided", "questions", "answers"}
        if not expected_modes.issubset(modes):
            errors.append(
                f"{ex['id']}: missing modes {sorted(expected_modes - modes)}"
            )
    if sum(1 for t in tracks if t["kind"] == "full") != 2:
        errors.append("Expected exactly 2 full mock-exam listening tracks")
    if sum(1 for t in tracks if t["kind"] == "strategy") < 1:
        errors.append("Missing strategy track")
    used_clips = {
        s["id"] for t in tracks for s in t["segments"] if s["type"] == "clip"
    }
    all_clips = {c["id"] for c in clips}
    if used_clips != all_clips:
        errors.append(
            f"Clip catalog mismatch: unused={sorted(all_clips - used_clips)[:6]}, "
            f"undefined={sorted(used_clips - all_clips)[:6]}"
        )
    for c in clips:
        if len(c["text"]) > 1500:
            errors.append(f"Clip {c['id']} exceeds 1500 chars")

    # ---- File-level QA ----------------------------------------------------
    expected_paths = {t["path"] for t in tracks}
    actual_paths = {
        p.relative_to(AUDIO_DIR).as_posix() for p in AUDIO_DIR.rglob("*.mp3")
    }
    missing_paths = expected_paths - actual_paths
    extra_paths = actual_paths - expected_paths
    if missing_paths:
        errors.append(f"Missing {len(missing_paths)} MP3 files: {sorted(missing_paths)[:8]}")
    if extra_paths:
        errors.append(f"Uncatalogued MP3 files: {sorted(extra_paths)[:8]}")

    report_rows: list[dict[str, Any]] = []
    for t in sorted(tracks, key=lambda x: x["path"]):
        mp3 = AUDIO_DIR / t["path"]
        if not mp3.is_file():
            continue
        info = MP3(str(mp3)).info
        size = mp3.stat().st_size
        duration = float(info.length)
        bitrate = int(info.bitrate)
        sample_rate = int(info.sample_rate)
        channels = int(getattr(info, "channels", 2))
        mean_db, peak_db = volume_stats(ffmpeg, mp3)

        if mp3.suffix.lower() != ".mp3":
            errors.append(f"{t['path']}: not an MP3")
        if size < 20_000:
            errors.append(f"{t['path']}: suspiciously small ({size} bytes)")
        if duration < 15:
            errors.append(f"{t['path']}: suspiciously short ({duration:.1f}s)")
        if duration > 900:
            errors.append(f"{t['path']}: suspiciously long ({duration:.1f}s)")
        if bitrate < 120_000:
            errors.append(f"{t['path']}: bitrate {bitrate} bps below 120 kbps")
        if sample_rate != 44_100:
            errors.append(f"{t['path']}: sample rate {sample_rate} Hz != 44100")
        if channels != 2:
            errors.append(f"{t['path']}: {channels} channel(s), expected stereo")
        if peak_db > -0.2:
            errors.append(f"{t['path']}: true peak {peak_db:.1f} dB risks clipping")
        if not -30.0 <= mean_db <= -10.0:
            errors.append(f"{t['path']}: mean volume {mean_db:.1f} dB outside [-30, -10]")
        if mean_db < -26:
            warnings.append(f"{t['path']}: quiet track ({mean_db:.1f} dB mean)")

        try:
            id3 = ID3(str(mp3))
        except Exception as exc:
            errors.append(f"{t['path']}: unreadable ID3 tags ({exc})")
            id3 = ID3()
        frames = set(id3.keys())
        has_transcript_tag = any(k.startswith("USLT:") for k in frames)
        if "TIT2" not in frames:
            errors.append(f"{t['path']}: missing ID3 title")
        if not has_transcript_tag:
            errors.append(f"{t['path']}: missing ID3 transcript/lyrics frame")
        source_frames = [k for k in frames if k.startswith("TXXX:SourcePDF")]
        if not source_frames:
            errors.append(f"{t['path']}: missing source-PDF tag")

        report_rows.append(
            {
                "path": t["path"],
                "kind": t["kind"],
                "duration_s": round(duration, 2),
                "size_bytes": size,
                "bitrate_kbps": round(bitrate / 1000, 1),
                "sample_rate_hz": sample_rate,
                "channels": channels,
                "mean_volume_db": round(mean_db, 1),
                "max_volume_db": round(peak_db, 1),
                "id3_title": str(id3.get("TIT2", "")),
                "has_transcript_tag": has_transcript_tag,
            }
        )

    qa = {
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "pdf_sha256": current_pdf_hash,
        "official_exercises": len(exercises),
        "official_questions": total_questions,
        "tracks_expected": len(tracks),
        "tracks_verified": len(report_rows),
        "tts_clips": len(clips),
        "total_duration_s": round(sum(r["duration_s"] for r in report_rows), 1),
        "total_size_bytes": sum(r["size_bytes"] for r in report_rows),
        "errors": errors,
        "warnings": warnings,
        "files": report_rows,
    }
    (OUT / "audio_qa.json").write_text(
        json.dumps(qa, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )

    lines = [
        "# Báo cáo kiểm định chất lượng audio",
        "",
        f"- Thời gian: {qa['generated_at']}",
        f"- SHA-256 PDF nguồn: `{current_pdf_hash}`",
        f"- Bài nghe chính thức: **{len(exercises)}/4**; câu hỏi: **{total_questions}/20**",
        f"- Tệp MP3: **{len(report_rows)}/{len(tracks)}**; clip TTS nguồn: **{len(clips)}**",
        f"- Tổng thời lượng: **{qa['total_duration_s'] / 60:.1f} phút**; tổng dung lượng: **{qa['total_size_bytes'] / 1024 / 1024:.1f} MiB**",
        f"- Lỗi: **{len(errors)}**; cảnh báo: **{len(warnings)}**",
        "",
        "## Thông số từng tệp",
        "",
        "| Tệp | Chế độ | Thời lượng | Dung lượng | Bitrate | Hz | Kênh | Mean / Peak (dB) | Transcript tag |",
        "|---|---|---:|---:|---:|---:|---:|---:|---|",
    ]
    for r in report_rows:
        lines.append(
            f"| `{r['path']}` | {r['kind']} | {r['duration_s']:.1f}s | "
            f"{r['size_bytes'] / 1024:.0f} KiB | {r['bitrate_kbps']:.0f}k | "
            f"{r['sample_rate_hz']} | {r['channels']} | "
            f"{r['mean_volume_db']:.1f} / {r['max_volume_db']:.1f} | "
            f"{'✓' if r['has_transcript_tag'] else '✗'} |"
        )
    if errors:
        lines += ["", "## Lỗi", ""] + [f"- {e}" for e in errors]
    else:
        lines += ["", "## Kết luận", "", "**PASS** — toàn bộ tiêu chuẩn kỹ thuật và phủ sóng đều đạt."]
    if warnings:
        lines += ["", "## Cảnh báo", ""] + [f"- {w}" for w in warnings]
    (OUT / "AUDIO_QA_REPORT.md").write_text("\n".join(lines) + "\n", encoding="utf-8")

    print(f"[QA] tracks={len(report_rows)}/{len(tracks)} errors={len(errors)} warnings={len(warnings)}")
    for e in errors:
        print("  ERROR:", e)
    for w in warnings:
        print("  WARN: ", w)
    if errors:
        raise SystemExit(1)
    print("[QA] PASS — AUDIO_QA_REPORT.md written")


if __name__ == "__main__":
    main()
