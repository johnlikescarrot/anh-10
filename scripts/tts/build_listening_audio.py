# -*- coding: utf-8 -*-
"""
Engine dung file MP3 luyen nghe cho bo de cuong Tieng Anh 10 Global Success
(GK1 2026-2027). Hoat dong hoan toan OFFLINE:

  * Giong doc neural Piper (VITS, medium, 22.05 kHz) tai qua scripts/tts/download_models.sh
  * Ghep PCM 16-bit bang thu vien chuan (wave/array), khong can ffmpeg cho buoc ghep
  * Ma hoa MP3 96 kbps / 44.1 kHz qua ban ffmpeg tinh cua goi imageio-ffmpeg (PyPI)

Moi bai nghe (04 tapescripts) tao 03 phien ban:
  - <id>-<slug>_clean.mp3 : doc mot lan, toc do tu nhien (luyen nghe lap/shadowing)
  - <id>-<slug>_slow.mp3  : doc cham hon (length_scale 1.25), nghe chinh ta/chi tiet
  - <id>-<slug>_exam.mp3  : bo de chuan: loi dan, 30 giay doc de, nghe 2 lan,
                            10 giay kiem tra, tieng bep mo/dong bai
Ngoai ra moi de co file gop 2 phan:  DE0x-listening-full_exam.mp3

Cach dung:
  python scripts/tts/build_listening_audio.py --exam all
  python scripts/tts/build_listening_audio.py --exam 1 --variants all
"""
from __future__ import annotations

import argparse
import array
import hashlib
import io
import json
import math
import re
import subprocess
import wave
from dataclasses import dataclass
from pathlib import Path

from piper import PiperVoice
import imageio_ffmpeg

# ---------------------------------------------------------------------------
# Hang so
# ---------------------------------------------------------------------------
ROOT = Path(__file__).resolve().parents[2]
VOICES_DIR = ROOT / ".tts-models" / "voices"
BUILD_DIR = ROOT / ".tts-models" / "build"
OUT_BASE = ROOT / "audio" / "listening"

SAMPLE_RATE = 22050
MAX_AMP = 32767
PEAK_TARGET = 0.92                       # chuan hoa dinh song (-0.7 dBFS)
TONE_FREQ = 880.0                        # tieng bep A5
TONE_DUR = 0.30
TONE_GAIN = 0.22

# khoa giong -> model Piper + mo ta (dung cho ID3 tag va README)
VOICE_MODELS = {
    "announcer": ("en_GB-alan-medium",       "male, British English (exam instructions)"),
    "f_lessac":  ("en_US-lessac-medium",     "female, American English"),
    "f_hfc":     ("en_US-hfc_female-medium", "female, American English, younger timbre"),
    "f_jenny":   ("en_GB-jenny_dioco-medium","female, British English"),
    "m_ryan":    ("en_US-ryan-medium",       "male, American English"),
}


# ---------------------------------------------------------------------------
# Tien xu ly van ban
# ---------------------------------------------------------------------------
def normalize_text(text: str) -> str:
    """Chuan hoa dau cau Typst/Unicode de espeak-ng doc chinh xac."""
    text = text.replace("—", ", ").replace("–", "-")
    text = text.replace("“", "").replace("”", "")
    text = text.replace("‘", "'").replace("’", "'")
    text = text.replace("\\", " ")
    text = re.sub(r"\s+([,.;:!?])", r"\1", text)   # bo khoang trang truoc dau cau
    text = re.sub(r"\s+", " ", text).strip()
    return text


# ---------------------------------------------------------------------------
# Xu ly PCM
# ---------------------------------------------------------------------------
def pcm_silence(seconds: float) -> array.array:
    return array.array("h", [0]) * int(SAMPLE_RATE * seconds)


def pcm_tone(seconds: float = TONE_DUR, freq: float = TONE_FREQ,
             gain: float = TONE_GAIN) -> array.array:
    """Song sine co fade in/out tranh tieng nep."""
    n = int(SAMPLE_RATE * seconds)
    fade = int(SAMPLE_RATE * 0.015)
    out = array.array("h", [0]) * n
    for i in range(n):
        env = 1.0
        if i < fade:
            env = i / fade
        elif i > n - fade:
            env = (n - i) / fade
        out[i] = int(MAX_AMP * gain * env * math.sin(2 * math.pi * freq * i / SAMPLE_RATE))
    return out


def trim_silence(pcm: array.array, pad_ms: int = 40) -> array.array:
    """Cat lang dau/cuoi, nguong thich nghi theo dinh song."""
    if not pcm:
        return pcm
    peak = max(abs(s) for s in pcm)
    threshold = max(250, int(peak * 0.04))
    start, end = 0, len(pcm)
    while start < end and abs(pcm[start]) < threshold:
        start += 1
    while end > start and abs(pcm[end - 1]) < threshold:
        end -= 1
    pad = int(SAMPLE_RATE * pad_ms / 1000)
    start = max(0, start - pad)
    end = min(len(pcm), end + pad)
    return pcm[start:end]


def peak_normalize(pcm: array.array) -> array.array:
    peak = max(abs(s) for s in pcm) or 1
    scale = (MAX_AMP * PEAK_TARGET) / peak
    return array.array("h", (max(-MAX_AMP, min(MAX_AMP, int(s * scale))) for s in pcm))


def write_wav(path: Path, pcm: array.array) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with wave.open(str(path), "wb") as wf:
        wf.setnchannels(1)
        wf.setsampwidth(2)
        wf.setframerate(SAMPLE_RATE)
        wf.writeframes(pcm.tobytes())


def pcm_duration(pcm: array.array) -> float:
    return len(pcm) / SAMPLE_RATE


# ---------------------------------------------------------------------------
# Bo tong hop giong noi
# ---------------------------------------------------------------------------
class VoiceFactory:
    def __init__(self) -> None:
        self._cache: dict[str, PiperVoice] = {}

    def get(self, voice_key: str) -> PiperVoice:
        if voice_key not in self._cache:
            model, _desc = VOICE_MODELS[voice_key]
            model_path = VOICES_DIR / f"{model}.onnx"
            if not model_path.exists():
                raise FileNotFoundError(
                    f"Thieu model {model_path}. Chay: bash scripts/tts/download_models.sh"
                )
            self._cache[voice_key] = PiperVoice.load(str(model_path))
        return self._cache[voice_key]

    def synth(self, text: str, voice_key: str, length_scale: float = 1.0,
              sentence_silence: float = 0.15) -> array.array:
        voice = self.get(voice_key)
        buf = io.BytesIO()
        with wave.open(buf, "wb") as wf:
            wf.setnchannels(1)
            wf.setsampwidth(2)
            wf.setframerate(SAMPLE_RATE)
            voice.synthesize(
                normalize_text(text),
                wf,
                length_scale=length_scale,
                sentence_silence=sentence_silence,
            )
        buf.seek(0)
        with wave.open(buf, "rb") as wf:
            pcm = array.array("h")
            pcm.frombytes(wf.readframes(wf.getnframes()))
        return trim_silence(pcm)


# ---------------------------------------------------------------------------
# Dung cac phien ban
# ---------------------------------------------------------------------------
@dataclass
class RenderConfig:
    length_scale: float
    sentence_silence: float
    turn_gap: float          # khoan nghi giua luot loi thoai
    para_gap: float          # khoan nghi giua doan doc thoai


# Toc do chuan de thi lop 10 (~150-170 tu/phut): Piper mac dinh hoi nhanh,
# nen keo dai nhe 1.10; ban slow 1.30 de luyen chinh ta/nghe chi tiet.
CLEAN = RenderConfig(1.10, 0.18, 0.50, 0.75)
SLOW = RenderConfig(1.30, 0.32, 0.95, 1.25)


def render_content(factory: VoiceFactory, exercise: dict, cfg: RenderConfig) -> array.array:
    """Ghep phan noi dung chinh (khong ke loi dan de thi)."""
    out = array.array("h")
    blocks = exercise["blocks"]
    for i, block in enumerate(blocks):
        out.extend(factory.synth(block["text"], block["voice"],
                                  length_scale=cfg.length_scale,
                                  sentence_silence=cfg.sentence_silence))
        if i < len(blocks) - 1:
            gap = cfg.turn_gap if exercise["kind"] == "dialogue" else cfg.para_gap
            out.extend(pcm_silence(gap))
    return out


def render_clean(factory: VoiceFactory, exercise: dict, slow: bool) -> array.array:
    cfg = SLOW if slow else CLEAN
    out = pcm_silence(0.6)
    out.extend(render_content(factory, exercise, cfg))
    out.extend(pcm_silence(0.8))
    return peak_normalize(out)


def render_exam(factory: VoiceFactory, exercise: dict,
                closing: str | None = None, opening: str | None = None) -> array.array:
    """Phien ban chuan de thi: loi dan -> doc de -> nghe lan 1 -> nghi -> nghe lan 2."""
    part_word = "One" if exercise["part"] == 1 else "Two"
    closing = closing or f"That is the end of Part {part_word}."
    out = array.array("h")

    if opening:
        out.extend(pcm_silence(0.5))
        out.extend(factory.synth(opening, "announcer"))
        out.extend(pcm_silence(1.0))

    # Loi dan + thoi gian doc cau hoi
    out.extend(pcm_tone())
    out.extend(pcm_silence(0.4))
    out.extend(factory.synth(exercise["intro"], "announcer", sentence_silence=0.25))
    out.extend(pcm_silence(1.0))
    out.extend(pcm_tone())
    out.extend(pcm_silence(30.0))                 # 30 giay doc de
    out.extend(pcm_tone())
    out.extend(pcm_silence(0.8))

    # Nghe lan 1
    out.extend(factory.synth("First listening.", "announcer"))
    out.extend(pcm_silence(1.0))
    out.extend(render_content(factory, exercise, CLEAN))
    out.extend(pcm_silence(1.0))

    # Nghi giua hai lan nghe
    out.extend(pcm_tone())
    out.extend(pcm_silence(0.4))
    out.extend(factory.synth("You have ten seconds to check your answers.",
                             "announcer"))
    out.extend(pcm_silence(10.0))
    out.extend(pcm_tone())
    out.extend(pcm_silence(0.8))

    # Nghe lan 2
    out.extend(factory.synth("Now listen again.", "announcer"))
    out.extend(pcm_silence(1.0))
    out.extend(render_content(factory, exercise, CLEAN))
    out.extend(pcm_silence(1.0))

    # Ket thuc
    out.extend(pcm_tone())
    out.extend(pcm_silence(0.4))
    out.extend(factory.synth(closing, "announcer"))
    out.extend(pcm_silence(1.0))
    return peak_normalize(out)


def render_full_exam(factory: VoiceFactory, exam_no: int, parts: list[dict]) -> array.array:
    opening = f"Mock Exam {'One' if exam_no == 1 else 'Two'}. Listening test."
    out = array.array("h")
    out.extend(render_exam(factory, parts[0], closing="That is the end of Part One.",
                           opening=opening))
    out.extend(pcm_silence(1.2))
    out.extend(factory.synth("Now turn to Part Two.", "announcer"))
    out.extend(pcm_silence(1.2))
    out.extend(render_exam(factory, parts[1],
                           closing="That is the end of the listening test."))
    return out


# ---------------------------------------------------------------------------
# Ma hoa MP3 + metadata
# ---------------------------------------------------------------------------
def encode_mp3(wav_path: Path, mp3_path: Path, tags: dict) -> None:
    ffmpeg = imageio_ffmpeg.get_ffmpeg_exe()
    cmd = [
        ffmpeg, "-y", "-hide_banner", "-loglevel", "error",
        "-f", "wav", "-i", str(wav_path),
        "-codec:a", "libmp3lame", "-b:a", "96k", "-ac", "1", "-ar", "44100",
        "-metadata", f"title={tags['title']}",
        "-metadata", f"artist={tags['artist']}",
        "-metadata", f"album={tags['album']}",
        "-metadata", "date=2026",
        "-metadata", f"comment={tags['comment']}",
        "-metadata", f"track={tags['track']}",
        str(mp3_path),
    ]
    subprocess.run(cmd, check=True)


def sha256_file(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------
def main() -> None:
    ap = argparse.ArgumentParser(description="Build MP3 listening tracks (offline Piper TTS).")
    ap.add_argument("--exam", choices=["1", "2", "all"], default="all")
    ap.add_argument("--variants", choices=["clean", "slow", "exam", "all"], default="all")
    args = ap.parse_args()

    from tapescripts import EXERCISES, EXAMS

    BUILD_DIR.mkdir(parents=True, exist_ok=True)
    factory = VoiceFactory()
    manifest = json.loads((OUT_BASE / "manifest.json").read_text("utf-8")) \
        if (OUT_BASE / "manifest.json").exists() else {"tracks": []}
    known_ids = {t["id"] + "|" + t["variant"] for t in manifest["tracks"]}

    wanted = [ex for ex in EXERCISES
              if args.exam == "all" or str(ex["exam"]) == args.exam]
    variants = ["clean", "slow", "exam"] if args.variants == "all" else [args.variants]

    for ex in wanted:
        out_dir = OUT_BASE / f"de{ex['exam']:02d}"
        out_dir.mkdir(parents=True, exist_ok=True)
        base = f"{ex['id']}-{ex['slug']}"
        voices_used = sorted({VOICE_MODELS[b["voice"]][0] for b in ex["blocks"]}
                             | {VOICE_MODELS["announcer"][0]})
        album = "Tieng Anh 10 Global Success - GK1 2026-2027 Listening"
        common_comment = (
            f"Source: DE_CUONG_ON_TAP_TIENG_ANH_10_GK1_2026_2027_GLOBAL_SUCCESS.pdf | "
            f"Tapescript {ex['id']} | Offline neural TTS: Piper VITS medium | "
            f"Voices: {', '.join(voices_used)}"
        )

        renders = {
            "clean": (render_clean(factory, ex, slow=False),
                      f"{ex['id']} {ex['title']} (natural-speed practice)"),
            "slow": (render_clean(factory, ex, slow=True),
                     f"{ex['id']} {ex['title']} (slow dictation practice)"),
            "exam": (render_exam(factory, ex),
                     f"{ex['id']} {ex['title']} (full exam version, two listenings)"),
        }
        for variant in variants:
            pcm, title = renders[variant]
            wav_path = BUILD_DIR / f"{base}_{variant}.wav"
            mp3_path = out_dir / f"{base}_{variant}.mp3"
            write_wav(wav_path, pcm)
            encode_mp3(wav_path, mp3_path, {
                "title": title,
                "artist": "Piper neural voices: " + ", ".join(voices_used),
                "album": album,
                "comment": common_comment,
                "track": str(ex["part"]),
            })
            rec = {
                "id": ex["id"],
                "variant": variant,
                "file": str(mp3_path.relative_to(ROOT)),
                "duration_seconds": round(pcm_duration(pcm), 2),
                "size_bytes": mp3_path.stat().st_size,
                "sha256": sha256_file(mp3_path),
                "voices": voices_used,
            }
            manifest["tracks"] = [t for t in manifest["tracks"]
                                  if not (t["id"] == ex["id"] and t["variant"] == variant)]
            manifest["tracks"].append(rec)
            print(f"[OK] {mp3_path.relative_to(ROOT)}  ({rec['duration_seconds']}s, "
                  f"{rec['size_bytes'] // 1024} KB)")

    # File gop moi de (chi khi dung yeu cau day du)
    if args.variants == "all":
        for exam_no, data in EXAMS.items():
            if args.exam != "all" and str(exam_no) != args.exam:
                continue
            pcm = render_full_exam(factory, exam_no, data["parts"])
            base = f"DE{exam_no:02d}-listening-full"
            wav_path = BUILD_DIR / f"{base}_exam.wav"
            mp3_path = OUT_BASE / f"de{exam_no:02d}" / f"{base}_exam.mp3"
            write_wav(wav_path, pcm)
            encode_mp3(wav_path, mp3_path, {
                "title": f"Mock Exam {exam_no} - complete Listening section (Parts 1-2)",
                "artist": "Piper neural voices (multi-speaker)",
                "album": "Tieng Anh 10 Global Success - GK1 2026-2027 Listening",
                "comment": "Complete exam-style listening: Part 1 True/False + Part 2 MCQs, "
                           "instructions, reading time and two listenings per part.",
                "track": "3",
            })
            rec = {
                "id": f"DE{exam_no:02d}-FULL", "variant": "exam",
                "file": str(mp3_path.relative_to(ROOT)),
                "duration_seconds": round(pcm_duration(pcm), 2),
                "size_bytes": mp3_path.stat().st_size,
                "sha256": sha256_file(mp3_path),
                "voices": sorted({VOICE_MODELS[b["voice"]][0]
                                  for ex in data["parts"] for b in ex["blocks"]}
                                 | {VOICE_MODELS["announcer"][0]}),
            }
            manifest["tracks"] = [t for t in manifest["tracks"]
                                  if not (t["id"] == rec["id"] and t["variant"] == "exam")]
            manifest["tracks"].append(rec)
            print(f"[OK] {mp3_path.relative_to(ROOT)}  ({rec['duration_seconds']}s, "
                  f"{rec['size_bytes'] // 1024} KB)")

    manifest["tracks"].sort(key=lambda t: (t["file"], t["variant"]))
    OUT_BASE.mkdir(parents=True, exist_ok=True)
    (OUT_BASE / "manifest.json").write_text(
        json.dumps(manifest, ensure_ascii=False, indent=2), "utf-8")
    print(f"\nManifest: {(OUT_BASE / 'manifest.json').relative_to(ROOT)} "
          f"({len(manifest['tracks'])} tracks)")


if __name__ == "__main__":
    main()
