#!/usr/bin/env python3
"""CI-safe coverage gate (no audio dependencies).

Fails if the inventory stops covering every official listening exercise in the
source PDF, or if the clip/track plan drops a required mode. Cheap enough to run
on every commit; verify_audio.py is the heavy, full-quality gate.
"""

from __future__ import annotations

import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
OUT = ROOT / "listening"

REQUIRED_MODES = {"exam", "clean", "guided", "questions", "answers"}


def main() -> int:
    inventory = json.loads((OUT / "inventory.json").read_text(encoding="utf-8"))
    manifest = json.loads((OUT / "clips_manifest.json").read_text(encoding="utf-8"))
    errors: list[str] = []

    exercises = inventory["exercises"]
    if len(exercises) != 4:
        errors.append(f"expected 4 official exercises, found {len(exercises)}")
    ids = {e["id"] for e in exercises}
    if ids != {f"exam-0{n}-part-0{p}" for n in (1, 2) for p in (1, 2)}:
        errors.append(f"unexpected exercise ids: {sorted(ids)}")
    if sum(len(e["questions"]) for e in exercises) != 20:
        errors.append("expected 20 official questions")
    if sum(len(e["answers"]) for e in exercises) != 20:
        errors.append("expected 20 answer keys")
    for e in exercises:
        if not 180 <= e["computed_words"] <= 200:
            errors.append(f"{e['id']}: word count {e['computed_words']} outside 180-200")
        if not e.get("transcript_text", "").strip():
            errors.append(f"{e['id']}: empty transcript")
        if len(e["questions"]) != 5:
            errors.append(f"{e['id']}: {len(e['questions'])} questions, expected 5")
        if e["pdf_cross_check"]["transcript_segments_matched"] != e[
            "pdf_cross_check"
        ]["transcript_segments_total"]:
            errors.append(f"{e['id']}: transcript/PDF cross-check incomplete")
        if e["pdf_cross_check"]["question_stems_matched"] != e[
            "pdf_cross_check"
        ]["question_stems_total"]:
            errors.append(f"{e['id']}: question/PDF cross-check incomplete")

    tracks = manifest["tracks"]
    for e in exercises:
        kinds = {t["kind"] for t in tracks if e["id"] in t["exercise_ids"]}
        missing = REQUIRED_MODES - kinds
        if missing:
            errors.append(f"{e['id']}: missing audio modes {sorted(missing)}")
    if sum(1 for t in tracks if t["kind"] == "full") != 2:
        errors.append("expected 2 full listening sections")
    if not any(t["kind"] == "strategy" for t in tracks):
        errors.append("missing strategy track")

    clip_ids = {c["id"] for c in manifest["clips"]}
    referenced = {
        s["id"] for t in tracks for s in t["segments"] if s["type"] == "clip"
    }
    if referenced - clip_ids:
        errors.append(f"tracks reference undefined clips: {sorted(referenced - clip_ids)[:5]}")
    if clip_ids - referenced:
        errors.append(f"unused clips: {sorted(clip_ids - referenced)[:5]}")
    for c in manifest["clips"]:
        if len(c["text"]) > 1500:
            errors.append(f"clip {c['id']} exceeds 1500 characters")
        if c["role"] not in manifest["roles"]:
            errors.append(f"clip {c['id']} uses undefined role {c['role']}")

    if errors:
        for err in errors:
            print(f"FAIL: {err}", file=sys.stderr)
        return 1
    print(
        f"PASS: {len(exercises)} official exercises, 20 questions, "
        f"{len(manifest['clips'])} clips, {len(tracks)} planned MP3 tracks."
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
