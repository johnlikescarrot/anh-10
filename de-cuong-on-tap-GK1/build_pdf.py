# -*- coding: utf-8 -*-
"""Build the Grade 10 English mid-term 1 review outline PDF.

Run:  python3 build_pdf.py
Output: De_cuong_on_tap_GK1_TiengAnh10_2026-2027.pdf (in this folder)

The content is written to match the official test matrix
(2026_2027_MA TRẬN 10_GK1.docx): Units 1-3 Global Success, 28 MCQ (7 pts)
+ 6 written questions + 1 paragraph (3 pts).
"""
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)

from reportlab.platypus import Spacer, Table, TableStyle, Paragraph, PageBreak
from reportlab.lib.units import mm
from reportlab.lib import colors
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.enums import TA_CENTER
from reportlab.platypus.tableofcontents import TableOfContents

import engine
from engine import Doc, md, PRIMARY, ACCENT, PRIMARY_L, ACCENT_L, LINE, GREY
import content_review
import content_exam
import content_keys

OUT = os.path.join(HERE, "De_cuong_on_tap_GK1_TiengAnh10_2026-2027.pdf")


def cover(D):
    D.gap(18)
    D.story.append(Paragraph(md("ĐỀ CƯƠNG ÔN TẬP"), D.styles["subtitle"]))
    D.story.append(Spacer(1, 4))
    D.story.append(Paragraph(
        md("KIỂM TRA GIỮA HỌC KỲ 1 - NĂM HỌC 2026-2027"),
        ParagraphStyle("c1", fontName="DejaVu-Bold", fontSize=17, leading=23,
                       alignment=TA_CENTER, textColor=colors.black)))
    D.gap(10)
    D.story.append(Paragraph(md("MÔN: TIẾNG ANH 10"), D.styles["title"]))
    D.story.append(Paragraph(
        md("(Bộ sách Global Success - Unit 1, 2, 3)"),
        ParagraphStyle("c2", fontName="DejaVu-Bold", fontSize=13, leading=18,
                       alignment=TA_CENTER, textColor=ACCENT)))
    D.gap(14)
    tbl = Table([[Paragraph(
        md("Biên soạn bám sát **Ma trận - Bảng đặc tả kỹ thuật đề kiểm tra giữa kỳ 1**<br/>"
           "Phạm vi: Unit 1 - Family life | Unit 2 - Humans and the environment | Unit 3 - Music<br/>"
           "Cấu trúc: 28 câu trắc nghiệm (7,0đ) + 6 câu tự luận + 1 bài viết đoạn văn (3,0đ)<br/>"
           "Nội dung: Phân tích ma trận - Đề cương kiến thức - Đề luyện tập hoàn chỉnh - Đáp án chi tiết").replace("&lt;br/&gt;", "<br/>"),
        ParagraphStyle("c3", fontName="DejaVu", fontSize=10, leading=16,
                       alignment=TA_CENTER, textColor=colors.black))]],
        colWidths=[160 * mm])
    tbl.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, -1), PRIMARY_L),
        ("BOX", (0, 0), (-1, -1), 1, PRIMARY),
        ("TOPPADDING", (0, 0), (-1, -1), 12),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 12),
        ("LEFTPADDING", (0, 0), (-1, -1), 14),
        ("RIGHTPADDING", (0, 0), (-1, -1), 14),
    ]))
    D.story.append(tbl)
    D.gap(16)

    # Table of contents
    toc = TableOfContents()
    toc.levelStyles = [
        ParagraphStyle("t0", fontName="DejaVu-Bold", fontSize=11, leading=17,
                       textColor=PRIMARY, spaceBefore=6),
        ParagraphStyle("t1", fontName="DejaVu", fontSize=9.5, leading=14,
                       leftIndent=16, textColor=colors.black),
    ]
    toc.dotsMinLevel = 0
    D.story.append(Paragraph(md("MỤC LỤC"), ParagraphStyle(
        "tl", fontName="DejaVu-Bold", fontSize=13, leading=17,
        alignment=TA_CENTER, textColor=colors.black)))
    D.story.append(Spacer(1, 6))
    D.story.append(toc)
    D.story.append(PageBreak())


def main():
    D = Doc(OUT)
    cover(D)
    content_review.build(D)
    content_exam.build(D)
    content_keys.build(D)
    D.save()
    print("Wrote", OUT, os.path.getsize(OUT), "bytes")


if __name__ == "__main__":
    main()
