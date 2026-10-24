# -*- coding: utf-8 -*-
"""Common styles & helpers for the revision guide PDF (ReportLab)."""
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import mm
from reportlab.lib import colors
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.enums import TA_CENTER, TA_JUSTIFY, TA_LEFT
from reportlab.platypus import (Paragraph, Spacer, Table, TableStyle,
                                KeepTogether, HRFlowable)

PAGE_W, PAGE_H = A4

# ---------- palette ----------
NAVY   = colors.HexColor("#1F3864")
TEAL   = colors.HexColor("#0E7C7B")
ORANGE = colors.HexColor("#E07B2A")
GREEN  = colors.HexColor("#2E7D32")
PURPLE = colors.HexColor("#5B4B9E")
LIGHT  = colors.HexColor("#EEF3FA")
LIGHT2 = colors.HexColor("#FFF4E6")
LIGHT3 = colors.HexColor("#EAF6EC")
GREY   = colors.HexColor("#5A5A5A")
LGREY  = colors.HexColor("#F4F4F4")

def _st(name, **kw):
    base = dict(fontName="DV", fontSize=10, leading=14.5,
                alignment=TA_JUSTIFY, textColor=colors.HexColor("#1a1a1a"),
                spaceAfter=4)
    base.update(kw)
    return ParagraphStyle(name, **base)

S = {
    "h1": _st("h1", fontName="DVB", fontSize=17, leading=22, textColor=NAVY,
              spaceBefore=10, spaceAfter=8, alignment=TA_LEFT),
    "h2": _st("h2", fontName="DVB", fontSize=13, leading=17, textColor=TEAL,
              spaceBefore=12, spaceAfter=5, alignment=TA_LEFT),
    "h3": _st("h3", fontName="DVB", fontSize=11, leading=15, textColor=NAVY,
              spaceBefore=9, spaceAfter=4, alignment=TA_LEFT),
    "p":  _st("p"),
    "c":  _st("c", alignment=TA_CENTER),
    "small": _st("small", fontSize=8.5, leading=12, textColor=GREY),
    "li": _st("li", leftIndent=12, bulletIndent=2, spaceAfter=2.5),
    "q":  _st("q", fontName="DVB", fontSize=10, leading=14, spaceBefore=6,
              spaceAfter=2, alignment=TA_LEFT),
    "opt": _st("opt", fontSize=9.5, leading=13.5, alignment=TA_LEFT, spaceAfter=1),
    "tbl": _st("tbl", fontSize=9, leading=12.5, alignment=TA_LEFT, spaceAfter=0),
    "tblc": _st("tblc", fontSize=9, leading=12.5, alignment=TA_CENTER, spaceAfter=0),
    "tblh": _st("tblh", fontName="DVB", fontSize=9, leading=12.5,
                textColor=colors.white, alignment=TA_CENTER, spaceAfter=0),
    "key": _st("key", fontSize=9.5, leading=13.5, alignment=TA_LEFT, spaceAfter=2),
    "vi": _st("vi", fontSize=9.5, leading=13.5, textColor=colors.HexColor("#333333")),
}

def P(txt, style="p"):
    return Paragraph(txt, S[style])

def bullet(txt):
    return Paragraph(txt, S["li"], bulletText="•")

def num(n, txt):
    return Paragraph(txt, S["li"], bulletText=f"{n}.")

def spacer(h=4):
    return Spacer(1, h)

def hr():
    return HRFlowable(width="100%", thickness=0.6, color=colors.HexColor("#C9D4E4"),
                      spaceBefore=3, spaceAfter=6)

def band(title, color=NAVY):
    """Full-width coloured section band."""
    t = Table([[Paragraph(f'<font color="white"><b>{title}</b></font>',
                          ParagraphStyle("band", fontName="DVB", fontSize=14,
                                         leading=18, textColor=colors.white))]],
              colWidths=[PAGE_W - 34*mm])
    t.setStyle(TableStyle([
        ("BACKGROUND", (0,0), (-1,-1), color),
        ("LEFTPADDING", (0,0), (-1,-1), 10), ("RIGHTPADDING", (0,0), (-1,-1), 10),
        ("TOPPADDING", (0,0), (-1,-1), 7), ("BOTTOMPADDING", (0,0), (-1,-1), 7),
        ("ROUNDEDCORNERS", [4,4,4,4]),
    ]))
    return t

def box(title, body_paras, bg=LIGHT2, border=ORANGE, title_color=None):
    """Callout box: title + list of Paragraph flowables (strings auto-wrapped)."""
    inner = []
    if title:
        inner.append(Paragraph(f"<b>{title}</b>", ParagraphStyle(
            "bt", fontName="DVB", fontSize=10, leading=14,
            textColor=title_color or border, spaceAfter=3)))
    for b in body_paras:
        inner.append(Paragraph(b, S["vi"]) if isinstance(b, str) else b)
    t = Table([[inner]], colWidths=[PAGE_W - 34*mm])
    t.setStyle(TableStyle([
        ("BACKGROUND", (0,0), (-1,-1), bg),
        ("BOX", (0,0), (-1,-1), 0.9, border),
        ("LEFTPADDING", (0,0), (-1,-1), 9), ("RIGHTPADDING", (0,0), (-1,-1), 9),
        ("TOPPADDING", (0,0), (-1,-1), 7), ("BOTTOMPADDING", (0,0), (-1,-1), 7),
        ("ROUNDEDCORNERS", [4,4,4,4]),
    ]))
    return t

def table(data, col_widths, header=True, align_center_cols=None, fontsize=9):
    """data: list of rows of strings -> styled table."""
    rows = []
    for r, row in enumerate(data):
        cells = []
        for c, cell in enumerate(row):
            if r == 0 and header:
                cells.append(Paragraph(str(cell), S["tblh"]))
            elif align_center_cols and c in align_center_cols:
                cells.append(Paragraph(str(cell), S["tblc"]))
            else:
                cells.append(Paragraph(str(cell), S["tbl"]))
        rows.append(cells)
    t = Table(rows, colWidths=col_widths, repeatRows=1 if header else 0)
    style = [
        ("GRID", (0,0), (-1,-1), 0.4, colors.HexColor("#B9C6DA")),
        ("VALIGN", (0,0), (-1,-1), "MIDDLE"),
        ("LEFTPADDING", (0,0), (-1,-1), 5), ("RIGHTPADDING", (0,0), (-1,-1), 5),
        ("TOPPADDING", (0,0), (-1,-1), 3.5), ("BOTTOMPADDING", (0,0), (-1,-1), 3.5),
    ]
    if header:
        style.append(("BACKGROUND", (0,0), (-1,0), NAVY))
        for r in range(1, len(rows)):
            if r % 2 == 0:
                style.append(("BACKGROUND", (0,r), (-1,r), LGREY))
    t.setStyle(TableStyle(style))
    return t

def mcq(n, question, options, note=None):
    """One multiple-choice question: options = list of 4 strings."""
    items = [P(f"<b>{n}. {question}</b>", "q")]
    if note:
        items.append(P(note, "small"))
    labels = ["A", "B", "C", "D"]
    cells = []
    for i, o in enumerate(options):
        cells.append(Paragraph(f"<b>{labels[i]}.</b> {o}", S["opt"]))
    while len(cells) < 4:
        cells.append(Paragraph("", S["opt"]))
    t = Table([[cells[0], cells[1]], [cells[2], cells[3]]],
              colWidths=[(PAGE_W-34*mm)/2]*2)
    t.setStyle(TableStyle([
        ("LEFTPADDING", (0,0), (-1,-1), 6), ("RIGHTPADDING", (0,0), (-1,-1), 4),
        ("TOPPADDING", (0,0), (-1,-1), 1), ("BOTTOMPADDING", (0,0), (-1,-1), 1),
        ("VALIGN", (0,0), (-1,-1), "TOP"),
    ]))
    items.append(t)
    return KeepTogether(items)

def openq(n, question, lines=1):
    items = [P(f"<b>{n}. {question}</b>", "q")]
    for _ in range(lines):
        items.append(P("______________________________________________________________", "opt"))
    return KeepTogether(items)

W = PAGE_W - 34*mm  # usable width
