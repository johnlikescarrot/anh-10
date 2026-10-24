#!/usr/bin/env python3
"""
Automated verification & PDF build pipeline for:
DE_CUONG_ON_TAP_TIENG_ANH_10_GK1_2026_2027_GLOBAL_SUCCESS.pdf
"""

import glob
import os
import re
import sys
import zipfile
import xml.etree.ElementTree as ET

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT_PDF = os.path.join(
    ROOT, "DE_CUONG_ON_TAP_TIENG_ANH_10_GK1_2026_2027_GLOBAL_SUCCESS.pdf"
)


def count_words(text: str) -> int:
    clean = re.sub(r"#underline\[#strong\[([^\]]+)\]\]", r"\1", text)
    clean = re.sub(r"#strong\[([^\]]+)\]", r"\1", clean)
    clean = re.sub(r"\*([^*]+)\*", r"\1", clean)
    clean = clean.replace("\\", " ").replace("—", " ")
    return len(re.findall(r"[A-Za-z0-9']+(?:-[A-Za-z0-9']+)*", clean))


def verify_source_docx() -> None:
    docx_path = os.path.join(ROOT, "2026_2027_MA TRẬN 10_GK1.docx")
    assert os.path.exists(docx_path), f"Missing source matrix docx: {docx_path}"
    with zipfile.ZipFile(docx_path, "r") as z:
        doc_xml = z.read("word/document.xml")
    root = ET.fromstring(doc_xml)
    ns = {"w": "http://schemas.openxmlformats.org/wordprocessingml/2006/main"}
    tables = root.findall(".//w:tbl", ns)
    assert len(tables) == 2, f"Expected 2 tables in matrix docx, found {len(tables)}"
    print("[OK] Source matrix DOCX verified (2 tables: Matrix + Specification).")


def verify_typst_sources() -> None:
    for path in sorted(glob.glob(os.path.join(ROOT, "src", "*.typ"))):
        with open(path, "r", encoding="utf-8") as f:
            content = f.read()
        assert "**" not in content, f"Leftover Markdown '**' found in {path}"
        assert "\\rightarrow" not in content, f"Leftover LaTeX macro found in {path}"

    # 1. Verify 3 model writings in part2b (120-150 words)
    with open(os.path.join(ROOT, "src", "part2b_grammar_skills.typ"), encoding="utf-8") as f:
        p2b = f.read()
    p2b_models = re.findall(r'#passage-box\(title: "(.*?)"\)\[\n(.*?)\n\]', p2b, re.S)
    assert len(p2b_models) == 3, f"Expected 3 model essays in part2b, got {len(p2b_models)}"
    for title, body in p2b_models:
        wc = count_words(body)
        assert 120 <= wc <= 150, f"{title}: word count {wc} outside [120, 150]"
        print(f"[OK] {title} -> {wc} words (target 120-150)")

    # 2. Verify 2 reading comprehension passages in part3 (220-250 words)
    with open(os.path.join(ROOT, "src", "part3_practice_drills.typ"), encoding="utf-8") as f:
        p3 = f.read()
    p3_readings = re.findall(r"== Bài 5([AB]).*?#passage-box\[\n(.*?)\n\]", p3, re.S)
    assert len(p3_readings) == 2, f"Expected 2 reading passages in part3, got {len(p3_readings)}"
    for label, body in p3_readings:
        wc = count_words(body)
        assert 220 <= wc <= 250, f"Reading 5{label}: word count {wc} outside [220, 250]"
        print(f"[OK] Drill 5 Reading 5{label} -> {wc} words (target 220-250)")

    # 3. Verify 2 reading comprehension passages in part4 (220-250 words)
    with open(os.path.join(ROOT, "src", "part4_mock_exams.typ"), encoding="utf-8") as f:
        p4 = f.read()
    p4_readings = re.findall(
        r"\*Part 2\. Read the following passage.*?\*.*?#passage-box\[\n(.*?)\n\]",
        p4,
        re.S,
    )
    assert len(p4_readings) == 2, f"Expected 2 reading passages in part4, got {len(p4_readings)}"
    for idx, body in enumerate(p4_readings, 1):
        wc = count_words(body)
        assert 220 <= wc <= 250, f"Mock {idx} Reading 2: word count {wc} outside [220, 250]"
        print(f"[OK] Mock Exam 0{idx} Reading 2 -> {wc} words (target 220-250)")

    # 4. Verify 4 listening tapescripts (180-200 words) & 2 model writings (120-150 words) in part5
    with open(os.path.join(ROOT, "src", "part5_answer_keys.typ"), encoding="utf-8") as f:
        p5 = f.read()
    p5_boxes = re.findall(r'#passage-box\(title: "(.*?)"\)\[\n(.*?)\n\]', p5, re.S)
    assert len(p5_boxes) == 6, f"Expected 6 passage boxes in part5, got {len(p5_boxes)}"
    for title, body in p5_boxes:
        wc = count_words(body)
        if "TAPESCRIPT" in title:
            assert 180 <= wc <= 200, f"{title}: word count {wc} outside [180, 200]"
            print(f"[OK] {title} -> {wc} words (target 180-200)")
        else:
            assert 120 <= wc <= 150, f"{title}: word count {wc} outside [120, 150]"
            print(f"[OK] {title} -> {wc} words (target 120-150)")


def build_and_verify_pdf(font_dirs: list[str]) -> None:
    import typst
    import pymupdf

    main_typ = os.path.join(ROOT, "src", "main.typ")
    pdf_bytes = typst.compile(main_typ, root=ROOT, font_paths=font_dirs)
    with open(OUT_PDF, "wb") as f:
        f.write(pdf_bytes)

    doc = pymupdf.open(OUT_PDF)
    print(f"[OK] Compiled {os.path.basename(OUT_PDF)} ({len(pdf_bytes):,} bytes, {len(doc)} pages)")
    assert len(doc) >= 18, f"Unexpectedly short PDF ({len(doc)} pages)"
    for idx, page in enumerate(doc, 1):
        txt = page.get_text().strip()
        assert len(txt) > 80, f"Page {idx} appears nearly blank ({len(txt)} chars)"
    toc = doc.get_toc()
    print(f"[OK] PDF bookmarks verified ({len(toc)} outline entries, 0 blank pages).")


if __name__ == "__main__":
    font_dirs = [d for d in ["/tmp/fonts", "/usr/share/fonts"] if os.path.isdir(d)]
    verify_source_docx()
    verify_typst_sources()
    build_and_verify_pdf(font_dirs)
    print("=== ALL VERIFICATION CHECKS PASSED ===")
