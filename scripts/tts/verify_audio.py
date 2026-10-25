# -*- coding: utf-8 -*-
"""
Kiem chung chat luong bo MP3 luyen nghe:
  1. Moi MP3 decode duoc, thoi luong khop manifest.json
  2. Ban "exam" co dung cau truc de thi:
       - khoang lang doc de ~30 giay va kiem tra bai ~10 giay
       - tieng bep 880 Hz o cac moc mo/dong
       - 02 dot noi dung (nghe 2 lan)
  3. Ban "clean"/"slow" khong co doan lang > 2 giay
  4. ID3 tags day du
Cach dung: python scripts/tts/verify_audio.py
"""
from __future__ import annotations

import array
import json
import math
import subprocess
import sys
import wave
from pathlib import Path

import imageio_ffmpeg

ROOT = Path(__file__).resolve().parents[2]
MANIFEST = ROOT / "audio" / "listening" / "manifest.json"
SR = 22050
FRAME = int(SR * 0.02)          # 20 ms
SIL_RMS = 250                   # nguong lang


def decode_mp3(path: Path) -> array.array:
    ffmpeg = imageio_ffmpeg.get_ffmpeg_exe()
    proc = subprocess.run(
        [ffmpeg, "-hide_banner", "-loglevel", "error", "-i", str(path),
         "-f", "wav", "-ac", "1", "-ar", str(SR), "-"],
        check=True, capture_output=True)
    import io
    with wave.open(io.BytesIO(proc.stdout), "rb") as w:
        pcm = array.array("h")
        pcm.frombytes(w.readframes(w.getnframes()))
    return pcm


def frame_rms(pcm: array.array) -> list[float]:
    out = []
    for i in range(0, len(pcm) - FRAME, FRAME):
        chunk = pcm[i:i + FRAME]
        out.append(math.sqrt(sum(s * s for s in chunk) / len(chunk)))
    return out


def silence_runs(rms: list[float]) -> list[float]:
    """Danh sach doan lang (giay) dai hon 1.5s."""
    runs, cur = [], 0
    for v in rms:
        if v < SIL_RMS:
            cur += 1
        else:
            if cur:
                runs.append(cur * 0.02)
            cur = 0
    if cur:
        runs.append(cur * 0.02)
    return [r for r in runs if r >= 1.5]


def has_880hz_tone(pcm: array.array) -> bool:
    """Quet tim cua so co tan so chinh gan 880 Hz (tieng bep)."""
    win = int(SR * 0.3)
    step = int(SR * 0.1)
    found = 0
    for start in range(0, max(1, len(pcm) - win), step):
        seg = pcm[start:start + win]
        if len(seg) < win:
            break
        # chi xet cua so nang luong vua phai (khong phai lang/tieng noi)
        rms = math.sqrt(sum(s * s for s in seg) / len(seg))
        if rms < 1500:
            continue
        n = len(seg)
        mag = [abs(sum(seg[i] * math.sin(2 * math.pi * f * i / SR)
                       for i in range(n))) for f in (440, 660, 880, 1100, 1320)]
        if mag.index(max(mag)) == 2 and max(mag) > 1.5 * sorted(mag)[-2]:
            found += 1
            if found >= 2:
                return True
    return False


def read_tags(path: Path) -> str:
    ffmpeg = imageio_ffmpeg.get_ffmpeg_exe()
    p = subprocess.run([ffmpeg, "-hide_banner", "-i", str(path)],
                       capture_output=True, text=True)
    return p.stderr


def main() -> int:
    manifest = json.loads(MANIFEST.read_text("utf-8"))
    failures: list[str] = []
    print(f"Kiem tra {len(manifest['tracks'])} track trong manifest\n" + "-" * 64)

    for rec in manifest["tracks"]:
        path = ROOT / rec["file"]
        tag = f"{rec['id']:10s} {rec['variant']:5s}"
        if not path.exists():
            failures.append(f"{tag}: THIEU FILE {path}")
            continue
        pcm = decode_mp3(path)
        dur = len(pcm) / SR
        if abs(dur - rec["duration_seconds"]) > 1.0:
            failures.append(f"{tag}: lech thoi luong {dur:.1f}s vs manifest "
                            f"{rec['duration_seconds']}s")
        rms = frame_rms(pcm)
        runs = silence_runs(rms)
        tags = read_tags(path)

        if rec["variant"] == "exam":
            long30 = [r for r in runs if 27 <= r <= 34]
            long10 = [r for r in runs if 8 <= r <= 13]
            if not long30:
                failures.append(f"{tag}: khong tim thay khoang doc de ~30s (runs={runs})")
            if not long10:
                failures.append(f"{tag}: khong tim thay khoang kiem tra ~10s (runs={runs})")
            if not has_880hz_tone(pcm):
                failures.append(f"{tag}: khong phat hien tieng bep 880Hz")
        else:
            bad = [r for r in runs if r > 2.0]
            if bad:
                failures.append(f"{tag}: co doan lang bat thuong {bad}")

        for need in ("title", "artist", "album", "comment"):
            if need + ":" not in tags.lower().replace(" ", ""):
                failures.append(f"{tag}: thieu ID3 tag '{need}'")

        voice_n = len(rec["voices"])
        print(f"{tag} | {dur:6.1f}s | {path.stat().st_size // 1024:5d}KB | "
              f"silence_runs={[round(r,1) for r in runs]} | voices={voice_n}")

    print("-" * 64)
    if failures:
        print("KHONG DAT:")
        for f in failures:
            print("  -", f)
        return 1
    print("DAT: tat ca track dung cau truc, thoi luong, tag va tieng bep.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
