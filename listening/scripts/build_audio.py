#!/usr/bin/env python3
"""Render the final MP3 collection from the TTS clips described by clips_manifest.json.

The TTS clips themselves are generated outside this script (one file per manifest
clip id, under listening/clips/).  This script:

  * decodes every clip to a uniform 44.1 kHz / stereo / 16-bit PCM WAV;
  * inserts exam-standard silences and 880 Hz cue tones;
  * concatenates each track exactly as specified in the manifest;
  * normalizes loudness, limits true peak, high-pass filters rumble;
  * encodes 128 kbps MP3 and writes rich UTF-8 ID3v2.3 tags including the full
    transcript in a USLT frame.

Usage:
    python listening/scripts/build_audio.py [--force]
"""

from __future__ import annotations

import argparse
import json
import math
import shutil
import struct
import subprocess
import tempfile
import wave
from pathlib import Path
from typing import Any

from mutagen.id3 import (
    COMM,
    ID3,
    TALB,
    TCON,
    TDRC,
    TIT2,
    TPE1,
    TPE2,
    TRCK,
    TXXX,
    USLT,
)

ROOT = Path(__file__).resolve().parents[2]
OUT = ROOT / "listening"
CLIPS_DIR = OUT / "clips"
AUDIO_DIR = OUT / "audio"
MANIFEST_PATH = OUT / "clips_manifest.json"
INVENTORY_PATH = OUT / "inventory.json"
SAMPLE_RATE = 44_100
CHANNELS = 2
SAMPLE_WIDTH = 2

PDF_NAME = "DE_CUONG_ON_TAP_TIENG_ANH_10_GK1_2026_2027_GLOBAL_SUCCESS.pdf"


def find_ffmpeg() -> str:
    exe = shutil.which("ffmpeg")
    if exe:
        return exe
    try:
        import imageio_ffmpeg  # type: ignore

        return imageio_ffmpeg.get_ffmpeg_exe()
    except Exception as exc:  # pragma: no cover - environment dependent
        raise SystemExit(
            "ffmpeg not found. Install system ffmpeg or `pip install imageio-ffmpeg`."
        ) from exc


def run(cmd: list[str]) -> None:
    subprocess.run(cmd, check=True)


def clip_to_wav(ffmpeg: str, clip: Path, wav: Path) -> None:
    run(
        [
            ffmpeg, "-y", "-v", "error",
            "-i", str(clip),
            "-vn",
            "-ac", str(CHANNELS),
            "-ar", str(SAMPLE_RATE),
            "-c:a", "pcm_s16le",
            str(wav),
        ]
    )


def write_wav(path: Path, frames: bytes) -> None:
    with wave.open(str(path), "wb") as w:
        w.setnchannels(CHANNELS)
        w.setsampwidth(SAMPLE_WIDTH)
        w.setframerate(SAMPLE_RATE)
        w.writeframes(frames)


def silence_wav(path: Path, seconds: float) -> None:
    n = max(1, int(round(seconds * SAMPLE_RATE)))
    frame = struct.pack("<hh", 0, 0)
    write_wav(path, frame * n)


def tone_wav(path: Path, seconds: float, frequency: int, volume: float) -> None:
    n = max(1, int(round(seconds * SAMPLE_RATE)))
    fade = int(0.008 * SAMPLE_RATE)
    chunks: list[bytes] = []
    for i in range(n):
        env = 1.0
        if i < fade:
            env = i / fade
        elif i > n - fade:
            env = max(0.0, (n - i) / fade)
        sample = int(32767 * volume * env * math.sin(2 * math.pi * frequency * i / SAMPLE_RATE))
        chunks.append(struct.pack("<hh", sample, sample))
    write_wav(path, b"".join(chunks))


def concat_wav(paths: list[Path], out: Path) -> None:
    assert paths, "Cannot concatenate an empty WAV list"
    with wave.open(str(paths[0]), "rb") as first:
        params = first.getparams()
        assert params.nchannels == CHANNELS
        assert params.sampwidth == SAMPLE_WIDTH
        assert params.framerate == SAMPLE_RATE
    with wave.open(str(out), "wb") as wo:
        wo.setnchannels(CHANNELS)
        wo.setsampwidth(SAMPLE_WIDTH)
        wo.setframerate(SAMPLE_RATE)
        for p in paths:
            with wave.open(str(p), "rb") as wi:
                if wi.getparams()[:4] != params[:4]:
                    raise ValueError(f"Incompatible WAV params in {p}")
                while True:
                    chunk = wi.readframes(SAMPLE_RATE * 5)
                    if not chunk:
                        break
                    wo.writeframes(chunk)


def encode_mp3(ffmpeg: str, wav: Path, mp3: Path, tags: dict[str, str]) -> None:
    af = (
        "highpass=f=75,"
        "loudnorm=I=-16:TP=-1.5:LRA=11,"
        "alimiter=limit=0.95"
    )
    cmd = [
        ffmpeg, "-y", "-v", "error",
        "-i", str(wav),
        "-map_metadata", "-1",
        "-af", af,
        "-c:a", "libmp3lame",
        "-b:a", "128k",
        "-ar", str(SAMPLE_RATE),
        "-ac", str(CHANNELS),
        "-id3v2_version", "3",
    ]
    for key, value in tags.items():
        cmd += ["-metadata", f"{key}={value}"]
    cmd.append(str(mp3))
    run(cmd)


def tag_mp3(
    mp3: Path,
    tags: dict[str, str],
    transcript: str,
    source_pages: list[int],
    exercise_ids: list[str],
) -> None:
    try:
        id3 = ID3(str(mp3))
    except Exception:
        id3 = ID3()
    id3.add(TIT2(encoding=3, text=tags.get("title", mp3.stem)))
    id3.add(TALB(encoding=3, text=tags.get("album", "")))
    id3.add(TPE1(encoding=3, text=tags.get("artist", "")))
    id3.add(TPE2(encoding=3, text=tags.get("albumartist", "")))
    id3.add(TCON(encoding=3, text=tags.get("genre", "")))
    id3.add(TRCK(encoding=3, text=tags.get("tracknumber", "")))
    id3.add(TDRC(encoding=3, text=tags.get("year", "")))
    id3.add(COMM(encoding=3, lang="eng", desc="Source", text=tags.get("comment", "")))
    id3.add(TXXX(encoding=3, desc="SourcePDF", text=PDF_NAME))
    id3.add(TXXX(encoding=3, desc="SourcePages", text=",".join(map(str, source_pages))))
    id3.add(TXXX(encoding=3, desc="ExerciseIDs", text=",".join(exercise_ids)))
    if transcript:
        id3.add(USLT(encoding=3, lang="eng", desc="Transcript", text=transcript))
    id3.save(str(mp3), v2_version=3)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--force", action="store_true", help="rebuild existing MP3 files")
    args = parser.parse_args()
    force: bool = args.force

    manifest = json.loads(MANIFEST_PATH.read_text(encoding="utf-8"))
    inventory = json.loads(INVENTORY_PATH.read_text(encoding="utf-8"))
    clips: list[dict[str, Any]] = manifest["clips"]
    tracks: list[dict[str, Any]] = manifest["tracks"]
    ffmpeg = find_ffmpeg()

    missing = [c["id"] for c in clips if not (CLIPS_DIR / f"{c['id']}.mp3").is_file()]
    if missing:
        raise SystemExit(
            f"Missing {len(missing)} TTS clips. First few: {missing[:8]}\n"
            "Generate every clip in clips_manifest.json before running build_audio.py."
        )

    AUDIO_DIR.mkdir(parents=True, exist_ok=True)
    with tempfile.TemporaryDirectory(prefix="anh10-audio-") as tmp:
        tmpdir = Path(tmp)
        wavdir = tmpdir / "wav"
        wavdir.mkdir()
        clip_wavs: dict[str, Path] = {}
        print(f"[INFO] Decoding {len(clips)} TTS clips with {Path(ffmpeg).name} …")
        for i, clip in enumerate(clips, 1):
            src = CLIPS_DIR / f"{clip['id']}.mp3"
            dst = wavdir / (clip["id"].replace("/", "__") + ".wav")
            dst.parent.mkdir(parents=True, exist_ok=True)
            clip_to_wav(ffmpeg, src, dst)
            clip_wavs[clip["id"]] = dst
            if i % 10 == 0 or i == len(clips):
                print(f"       decoded {i}/{len(clips)}")

        for n, track in enumerate(tracks, 1):
            mp3 = AUDIO_DIR / track["path"]
            mp3.parent.mkdir(parents=True, exist_ok=True)
            if mp3.exists() and not force:
                print(f"[SKIP] {n:02d}/{len(tracks)} {track['path']}")
                continue
            segment_wavs: list[Path] = []
            for j, seg in enumerate(track["segments"]):
                kind = seg["type"]
                if kind == "clip":
                    cid = seg["id"]
                    if cid not in clip_wavs:
                        raise KeyError(f"Track {track['id']} references unknown clip {cid}")
                    segment_wavs.append(clip_wavs[cid])
                elif kind == "silence":
                    p = wavdir / f"silence-{n:02d}-{j:03d}.wav"
                    silence_wav(p, float(seg["seconds"]))
                    segment_wavs.append(p)
                elif kind == "tone":
                    p = wavdir / f"tone-{n:02d}-{j:03d}.wav"
                    tone_wav(
                        p,
                        float(seg.get("seconds", 0.22)),
                        int(seg.get("frequency", 880)),
                        float(seg.get("volume", 0.075)),
                    )
                    segment_wavs.append(p)
                else:
                    raise ValueError(f"Unknown segment type {kind}")
            combined = wavdir / f"track-{n:02d}.wav"
            concat_wav(segment_wavs, combined)
            encode_mp3(ffmpeg, combined, mp3, track["tags"])
            tag_mp3(
                mp3,
                track["tags"],
                track.get("transcript", ""),
                track.get("source_pages", []),
                track.get("exercise_ids", []),
            )
            print(
                f"[OK] {n:02d}/{len(tracks)} {track['path']} "
                f"({mp3.stat().st_size / 1024:.0f} KiB)"
            )
            combined.unlink(missing_ok=True)

    # Persist a small build receipt for the QA script and for reviewers.
    receipt = {
        "inventory_sha256_prefix": inventory["source"]["pdf_sha256"][:16],
        "official_exercises": inventory["coverage"]["listening_exercises_total"],
        "tts_clips": len(clips),
        "tracks": len(tracks),
        "output_directory": "listening/audio",
        "encoder": "libmp3lame 128 kbps CBR / 44.1 kHz / stereo",
    }
    (OUT / "AUDIO_BUILD_RECEIPT.json").write_text(
        json.dumps(receipt, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )
    print(f"[DONE] Built {len(tracks)} MP3 tracks from {len(clips)} TTS clips.")


if __name__ == "__main__":
    main()
