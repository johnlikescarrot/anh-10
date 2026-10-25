# -*- coding: utf-8 -*-
"""
Kiem chung DO PHU: moi tapescript ton tai trong PDF (file nguon Typst) phai co
du bo MP3 tuong ung. Chong sot bai nghe.

  - Dem so #passage-box TAPESCRIPT trong src/part5_answer_keys.typ
  - Voi moi tapescript: xac nhan van ban trong tapescripts.py la tap con cua
    nguon (trung tuyet doi tung cau), va du 04 bien ban MP3 + manifest
  - Xac nhan 02 file gop de thi ton tai
Cach dung: python scripts/tts/check_coverage.py
"""
from __future__ import annotations

import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(Path(__file__).resolve().parent))

from tapescripts import EXERCISES  # noqa: E402

TYP = ROOT / "src" / "part5_answer_keys.typ"
MANIFEST = ROOT / "audio" / "listening" / "manifest.json"
VARIANTS = ("clean", "slow", "exam", "dictation")


def normalize(s: str) -> str:
    s = s.replace("—", ", ").replace("–", "-")
    s = s.replace("“", "").replace("”", "").replace("’", "'").replace("‘", "'")
    s = re.sub(r"\*([^*]+)\*", r"\1", s)
    s = re.sub(r"\s+([,.;:!?])", r"\1", s)
    return re.sub(r"\s+", " ", s).strip().lower()


def split_safe(text: str) -> list[str]:
    for abbr in ("Mrs.", "Mr.", "Dr.", "Ms.", "a.m.", "p.m."):
        text = text.replace(abbr, abbr.replace(".", "·"))
    sents = re.split(r"(?<=[.!?])\s+", text)
    return [s.replace("·", ".") for s in sents if s.strip()]


def main() -> int:
    typ_src = TYP.read_text(encoding="utf-8")
    boxes = re.findall(r'#passage-box\(title: "(TAPESCRIPT[^"]+)"\)\[(.*?)\n\]',
                       typ_src, re.S)
    print(f"So TAPESCRIPT trong nguon Typst/PDF: {len(boxes)}")
    if len(boxes) != len(EXERCISES):
        print(f"LOI: nguon co {len(boxes)} tapescript nhung tapescripts.py co "
              f"{len(EXERCISES)} bai")
        return 1

    source_norm = [normalize(body) for _title, body in boxes]
    manifest = json.loads(MANIFEST.read_text("utf-8"))
    indexed = {(t["id"], t["variant"]): t for t in manifest["tracks"]}
    failures: list[str] = []

    for ex, src in zip(EXERCISES, source_norm):
        print(f"\n{ex['id']} — {ex['title'][:60]}...")
        # 1) Trung tuyet doi tung cau (du lieu noi la tap con cua nguon)
        for block in ex["blocks"]:
            for sent in split_safe(normalize(block["text"])):
                if sent not in src:
                    failures.append(f"{ex['id']}: cau khong co trong nguon: {sent[:70]}")
        # 2) Du 04 bien ban MP3 + manifest + file that
        for variant in VARIANTS:
            rec = indexed.get((ex["id"], variant))
            if rec is None:
                failures.append(f"{ex['id']}: thieu ban ghi manifest '{variant}'")
                continue
            if not (ROOT / rec["file"]).exists():
                failures.append(f"{ex['id']}: thieu file {rec['file']}")
            print(f"  [OK] {variant:9s} -> {rec['file']} ({rec['duration_seconds']}s)")

    # 3) Hai file gop de thi
    for exam_no in (1, 2):
        rec = indexed.get((f"DE{exam_no:02d}-FULL", "exam"))
        if rec is None or not (ROOT / rec["file"]).exists():
            failures.append(f"Thieu file gop DE{exam_no:02d}-listening-full_exam.mp3")
        else:
            print(f"\n[OK] full exam {exam_no}: {rec['file']} ({rec['duration_seconds']}s)")

    # 4) Playlist
    for pl in ("01-exam-simulation.m3u", "02-natural-speed-practice.m3u",
               "03-slow-and-dictation.m3u"):
        if not (ROOT / "audio" / "listening" / "playlists" / pl).exists():
            failures.append(f"Thieu playlist {pl}")

    print("\n" + "=" * 60)
    if failures:
        print("KHONG DAT:")
        for f in failures:
            print("  -", f)
        return 1
    print(f"DAT: 4/4 tapescripts duoc phu 100% — {len(manifest['tracks'])} track "
          f"trong manifest, 03 playlist, khong sot bai nghe nao.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
