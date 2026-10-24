#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Build the Vietnamese revision guide PDF from a tiny markup language.

Usage:
    python tools/build_pdf.py [--out OUTPUT.pdf] [content/*.md ...]

Markup (line based)
-------------------
[[PART 1|Title|subtitle]]        part opener page + TOC level 0
[[TOC]]                          table of contents
[[PAGEBREAK]]
[[W 20 30 50]]                   column widths (%) for the next table
[[ANS]]                          small "dap an" style heading
## Title                         section  (TOC level 1)
### Title                        subsection (TOC level 2)
#### Title                       run-in heading
> text                           note box   (blue)
>! text                          warning box (red)
>+ text                          tip box    (green)
># text                          formula box (amber)
| a | b |                        table row (first row = header)
1. text / - text / * text        list items
"Q." style lines                questions, with A./B./C./D. option lines
blank line                       paragraph break
Inline: **bold**, ==highlight==, ~~small caps?~~ (not supported)
"""
from __future__ import annotations

import argparse
import glob
import os
import re
import sys

from reportlab.lib import colors
from reportlab.lib.enums import TA_CENTER, TA_JUSTIFY, TA_LEFT
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.units import mm
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import (
    BaseDocTemplate, Flowable, Frame, HRFlowable, KeepTogether, NextPageTemplate,
    PageBreak, PageTemplate, Paragraph, Spacer, Table, TableStyle,
)

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)

# ---------------------------------------------------------------- palette ---
INK = colors.HexColor("#1B2A32")
MUTED = colors.HexColor("#5C6B73")
PRIMARY = colors.HexColor("#0E4D64")
PRIMARY_DARK = colors.HexColor("#08313F")
PRIMARY_LIGHT = colors.HexColor("#E8F1F5")
ACCENT = colors.HexColor("#D98324")
ACCENT_LIGHT = colors.HexColor("#FDF3E3")
GREEN = colors.HexColor("#1E7A4A")
GREEN_LIGHT = colors.HexColor("#EAF6EF")
RED = colors.HexColor("#B03A2E")
RED_LIGHT = colors.HexColor("#FBEAE8")
BLUE = colors.HexColor("#1F5FA8")
BLUE_LIGHT = colors.HexColor("#EAF1FA")
RULE = colors.HexColor("#C9D6DD")
ZEBRA = colors.HexColor("#F6F9FA")

PAGE_W, PAGE_H = A4
M_LEFT = 17 * mm
M_RIGHT = 15 * mm
M_TOP = 22 * mm
M_BOTTOM = 17 * mm
AVAIL_W = PAGE_W - M_LEFT - M_RIGHT

DOC_TITLE = "ĐỀ CƯƠNG ÔN TẬP TIẾNG ANH 10 – GIỮA HỌC KỲ 1"
DOC_RUNNING = "Tiếng Anh 10 · Global Success · GK1 2026–2027"


# ------------------------------------------------------------------ fonts ---
def _find_font(name):
    bundled = os.path.join(HERE, "fonts", name)
    if os.path.exists(bundled):
        return bundled
    for base in ("/usr/share/fonts/truetype/dejavu", "/usr/share/fonts"):
        p = os.path.join(base, name)
        if os.path.exists(p):
            return p
    for root, _dirs, files in os.walk("/usr/share/fonts"):
        if name in files:
            return os.path.join(root, name)
    raise FileNotFoundError(name)


def register_fonts():
    files = {
        "Body": "DejaVuSans.ttf",
        "Body-Bold": "DejaVuSans-Bold.ttf",
        "Body-Italic": "DejaVuSans-Oblique.ttf",
        "Body-BoldItalic": "DejaVuSans-BoldOblique.ttf",
        "Serif-Bold": "DejaVuSerif-Bold.ttf",
        "Serif-Italic": "DejaVuSerif-Italic.ttf",
        "Mono": "DejaVuSansMono.ttf",
    }
    for name, fname in files.items():
        try:
            pdfmetrics.registerFont(TTFont(name, _find_font(fname)))
        except FileNotFoundError:
            fallback = "DejaVuSerif-Bold.ttf" if "Serif" in name else "DejaVuSans.ttf"
            pdfmetrics.registerFont(TTFont(name, _find_font(fallback)))
    pdfmetrics.registerFontFamily("Body", normal="Body", bold="Body-Bold",
                                  italic="Body-Italic", boldItalic="Body-BoldItalic")
    pdfmetrics.registerFontFamily("Serif", normal="Serif-Bold", bold="Serif-Bold",
                                  italic="Serif-Italic", boldItalic="Serif-Bold")
    pdfmetrics.registerFontFamily("Mono", normal="Mono", bold="Mono",
                                  italic="Mono", boldItalic="Mono")


# ----------------------------------------------------------------- styles ---
def build_styles():
    S = {}
    S["body"] = ParagraphStyle(
        "body", fontName="Body", fontSize=9.6, leading=14.2, textColor=INK,
        alignment=TA_JUSTIFY, spaceAfter=4.2, spaceBefore=0)
    S["body_left"] = ParagraphStyle("body_left", parent=S["body"], alignment=TA_LEFT)
    S["lead"] = ParagraphStyle(
        "lead", parent=S["body"], fontSize=10.4, leading=15.5, textColor=PRIMARY_DARK,
        spaceAfter=6)
    S["h2"] = ParagraphStyle(
        "h2", fontName="Body-Bold", fontSize=15, leading=19, textColor=PRIMARY_DARK,
        spaceBefore=11, spaceAfter=6, alignment=TA_LEFT, keepWithNext=1)
    S["h3"] = ParagraphStyle(
        "h3", fontName="Body-Bold", fontSize=11.4, leading=15, textColor=PRIMARY,
        spaceBefore=9, spaceAfter=3.5, keepWithNext=0)
    S["h4"] = ParagraphStyle(
        "h4", fontName="Body-Bold", fontSize=9.9, leading=13.5, textColor=ACCENT,
        spaceBefore=7, spaceAfter=2.5, keepWithNext=1)
    S["bullet"] = ParagraphStyle(
        "bullet", parent=S["body"], leftIndent=13, bulletIndent=1, spaceAfter=2.6,
        alignment=TA_LEFT)
    S["bullet2"] = ParagraphStyle(
        "bullet2", parent=S["body"], leftIndent=26, bulletIndent=14, spaceAfter=2.2,
        fontSize=9.3, leading=13.6, alignment=TA_LEFT)
    S["num"] = ParagraphStyle(
        "num", parent=S["body"], leftIndent=17, firstLineIndent=-17, spaceAfter=2.6,
        alignment=TA_LEFT)
    S["box"] = ParagraphStyle(
        "box", parent=S["body"], fontSize=9.3, leading=13.6, spaceAfter=2,
        alignment=TA_LEFT)
    S["box_h"] = ParagraphStyle(
        "box_h", parent=S["box"], fontName="Body-Bold", spaceAfter=2.5,
        fontSize=9.5)
    S["mono"] = ParagraphStyle(
        "mono", fontName="Mono", fontSize=8.9, leading=13.2, textColor=PRIMARY_DARK,
        alignment=TA_LEFT, spaceAfter=2)
    S["tcell"] = ParagraphStyle(
        "tcell", fontName="Body", fontSize=8.5, leading=11.6, textColor=INK,
        alignment=TA_LEFT)
    S["tcell_c"] = ParagraphStyle("tcell_c", parent=S["tcell"], alignment=TA_CENTER)
    S["thead"] = ParagraphStyle(
        "thead", fontName="Body-Bold", fontSize=8.6, leading=11.6,
        textColor=colors.white, alignment=TA_LEFT)
    S["thead_c"] = ParagraphStyle("thead_c", parent=S["thead"], alignment=TA_CENTER)
    S["opt"] = ParagraphStyle(
        "opt", fontName="Body", fontSize=9.4, leading=13.4, textColor=INK,
        alignment=TA_LEFT)
    S["q"] = ParagraphStyle(
        "q", parent=S["body"], spaceBefore=3.4, spaceAfter=1.4, alignment=TA_LEFT)
    S["qnum"] = ParagraphStyle(
        "qnum", parent=S["body"], leftIndent=15, firstLineIndent=-15, spaceBefore=3.4,
        spaceAfter=1.4, alignment=TA_LEFT)
    S["optline"] = ParagraphStyle(
        "optline", fontName="Body", fontSize=9.4, leading=13.4, textColor=INK,
        leftIndent=12, firstLineIndent=-12, alignment=TA_LEFT, spaceAfter=1.6)
    S["caption"] = ParagraphStyle(
        "caption", fontName="Body", fontSize=8.2, leading=11, textColor=MUTED,
        alignment=TA_LEFT, spaceBefore=2, spaceAfter=6)
    S["toc0"] = ParagraphStyle(
        "toc0", fontName="Body-Bold", fontSize=10.6, leading=19, textColor=PRIMARY_DARK,
        spaceBefore=5)
    S["toc1"] = ParagraphStyle(
        "toc1", fontName="Body", fontSize=9.4, leading=15.5, textColor=INK,
        leftIndent=13)
    S["toc2"] = ParagraphStyle(
        "toc2", fontName="Body", fontSize=8.7, leading=13.4, textColor=MUTED,
        leftIndent=27)
    return S


S = build_styles()


# ------------------------------------------------------------- inline text ---
INLINE_OPEN = {
    "***": "<b><i>{}" + "</i></b>",
    "**": "<b>{}" + "</b>",
    "==": '<font backColor="#FFF0B8">{}</font>',
    "~~": '<font color="#5C6B73">{}</font>',
    "`": '<font name="Mono" size="8.4" color="#0E4D64">{}</font>',
    "*": "<i>{}" + "</i>",
}
_MARKERS = ("***", "**", "==", "~~", "`", "*")


def _render(s: str) -> str:
    best = None
    for mk in _MARKERS:
        i = s.find(mk)
        if i == -1:
            continue
        if best is None or i < best[0] or (i == best[0] and len(mk) > len(best[1])):
            best = (i, mk)
    if best is None:
        return s
    i, mk = best
    j = s.find(mk, i + len(mk))
    if j == -1:
        return s[:i] + mk.replace("*", "*") + _render(s[i + len(mk):])
    inner = _render(s[i + len(mk):j])
    out = INLINE_OPEN[mk].format(inner)
    return s[:i] + out + _render(s[j + len(mk):])


def inline(text: str) -> str:
    """Escape XML then convert the mini-markup into reportlab tags (nesting-safe)."""
    text = (text.replace("&amp;", "\x00AMP\x00").replace("&", "&amp;")
                .replace("\x00AMP\x00", "&amp;")
                .replace("<br/>", "\x00BR\x00").replace("<", "&lt;")
                .replace(">", "&gt;").replace("\x00BR\x00", "<br/>"))
    return _render(text)


def P(text, style="body"):
    """Paragraph from RAW markup text (inline() applied here)."""
    return Paragraph(inline(text), S[style])


# ------------------------------------------------------------------ flow ---
class TocMark(Flowable):
    """Zero-height marker that feeds an entry into the table of contents."""

    def __init__(self, level, text, key=None):
        Flowable.__init__(self)
        self.level, self.text, self.key = level, text, key
        self.width = 0
        self.height = 0

    def draw(self):
        pass


class PartOpener(Flowable):
    """Full-page part divider."""

    def __init__(self, number, title, subtitle, bullets=None):
        Flowable.__init__(self)
        self.toc_level = 0
        self.toc_text = f"PHẦN {number}. {title}"
        self.number = number
        self.title = title
        self.subtitle = subtitle
        self.bullets = bullets or []
        self.width = AVAIL_W
        self.height = PAGE_H - M_TOP - M_BOTTOM - 14

    def draw(self):
        c = self.canv
        w, h = self.width, self.height
        c.saveState()
        # left colour band
        c.setFillColor(PRIMARY_DARK)
        c.rect(-M_LEFT, -M_BOTTOM, 9 * mm, h + M_TOP + M_BOTTOM, stroke=0, fill=1)
        c.setFillColor(ACCENT)
        c.rect(-M_LEFT + 9 * mm, -M_BOTTOM, 1.8 * mm, h + M_TOP + M_BOTTOM, stroke=0, fill=1)
        # ghost number (bottom-right, bled off the trim edge)
        c.setFillColor(colors.HexColor("#E3EDF2"))
        c.setFont("Serif-Bold", 230)
        c.drawRightString(w + 16 * mm, -18 * mm, self.number)
        # label
        c.setFillColor(ACCENT)
        c.setFont("Body-Bold", 11)
        c.drawString(6 * mm, h - 42 * mm, "PHẦN " + self.number)
        # title
        c.setFillColor(PRIMARY_DARK)
        c.setFont("Serif-Bold", 25)
        y = h - 56 * mm
        for line in self._wrap(self.title, 25, w - 14 * mm):
            c.drawString(6 * mm, y, line)
            y -= 11.5 * mm
        c.setStrokeColor(ACCENT)
        c.setLineWidth(2.2)
        c.line(6 * mm, y + 4 * mm, 6 * mm + 34 * mm, y + 4 * mm)
        # subtitle
        c.setFillColor(INK)
        c.setFont("Body", 10.5)
        y -= 4 * mm
        for line in self._wrap(self.subtitle, 10.5, w - 22 * mm):
            c.drawString(6 * mm, y, line)
            y -= 5.6 * mm
        # bullets
        y -= 3 * mm
        c.setFont("Body", 9.2)
        for b in self.bullets:
            c.setFillColor(PRIMARY)
            c.circle(7 * mm, y + 1.2 * mm, 1.1 * mm, stroke=0, fill=1)
            c.setFillColor(MUTED)
            for i, line in enumerate(self._wrap(b, 9.2, w - 30 * mm)):
                c.drawString(10.5 * mm, y, line)
                y -= 5.0 * mm
            y -= 1.2 * mm
        c.restoreState()

    @staticmethod
    def _wrap(text, size, width):
        words = text.split()
        lines, cur = [], ""
        maxw = width
        for word in words:
            trial = (cur + " " + word).strip()
            if pdfmetrics.stringWidth(trial, "Body", size) > maxw and cur:
                lines.append(cur)
                cur = word
            else:
                cur = trial
        if cur:
            lines.append(cur)
        return lines or [""]


PAGE_MAP = {}   # filled after the measuring pass
ENTRIES = []    # pre-scanned (level, text, page) for the TOC


class TOCFlow(Flowable):
    """Custom table of contents: dot leaders + right-aligned page numbers."""

    def __init__(self, pagemap, entries=None):
        Flowable.__init__(self)
        self.pagemap = pagemap or {}
        self.entries = entries if entries is not None else []
        self.width = AVAIL_W
        self._built = None

    def wrap(self, aw, ah):
        self.width = aw
        if self._built is None:
            self._built = self._table()
        w, h = self._built.wrap(aw, ah)
        self.height = h
        return w, h

    def draw(self):
        self._built.drawOn(self.canv, 0, 0)

    def split(self, aw, ah):
        if self._built is None:
            self._built = self._table()
        w, h = self._built.wrap(aw, ah)
        if h <= ah:
            return []
        n = len(self.entries)
        half = max(1, n // 2)
        a = TOCFlow(self.pagemap, self.entries[:half])
        b = TOCFlow(self.pagemap, self.entries[half:])
        return [a, b]

    def _table(self):
        rows = []
        for lvl, text, pg in self.entries:
            pg = self.pagemap.get(text, pg)
            if lvl == 0:
                txt = f'<font name="Body-Bold" size="10.8" color="#08313F">' \
                      f'{text.upper()}</font>'
                st = ParagraphStyle("t0", fontName="Body-Bold", fontSize=10.6,
                                    leading=14, alignment=TA_LEFT,
                                    spaceBefore=4, spaceAfter=1)
                rows.append([Paragraph(txt, st),
                             Paragraph(f'<font name="Body-Bold" size="10.8" '
                                       f'color="#08313F">{pg}</font>',
                                       ParagraphStyle("p0", fontName="Body-Bold", alignment=2, leading=14)),
                             "part"])
            else:
                if lvl == 1:
                    st = ParagraphStyle("t1", fontName="Body", fontSize=9.4, leading=13,
                                        leftIndent=12, firstLineIndent=-12,
                                        textColor=INK, alignment=TA_LEFT)
                    pst = ParagraphStyle("p1", fontName="Body", fontSize=9,
                                         alignment=2, leading=13, textColor=INK)
                else:
                    st = ParagraphStyle("t2", fontName="Body", fontSize=8.8, leading=13,
                                        leftIndent=26, firstLineIndent=-8,
                                        textColor=MUTED, alignment=TA_LEFT)
                    pst = ParagraphStyle("p2", fontName="Body", fontSize=8.4,
                                         alignment=2, leading=13, textColor=MUTED)
                rows.append([Paragraph(text, st), Paragraph(str(pg), pst), "sect"])
        data, styles = [], [("VALIGN", (0, 0), (-1, -1), "BOTTOM"),
                            ("LEFTPADDING", (0, 0), (-1, -1), 0),
                            ("RIGHTPADDING", (0, 0), (-1, -1), 0),
                            ("TOPPADDING", (0, 0), (-1, -1), 0),
                            ("BOTTOMPADDING", (0, 0), (-1, -1), 1.0)]
        for r, (c1, c2, kind) in enumerate(rows):
            data.append([c1, c2])
            if kind == "part" and r > 0:
                styles.append(("LINEABOVE", (0, r), (-1, r), 0.6, PRIMARY_LIGHT))
        t = Table(data, colWidths=[AVAIL_W - 16, 16])
        t.setStyle(TableStyle(styles))
        return t


def scan_entries(files):
    """Pre-scan sources for headings so the TOC height is stable across passes."""
    out = []
    for f in files:
        with open(f, encoding="utf-8") as fh:
            for line in fh:
                s = line.strip()
                if s.startswith("[[PART"):
                    m = re.match(r"\[\[PART\s+(\S+?)\|([^|\]]*)\|", s)
                    if m:
                        out.append((0, f"PHẦN {m.group(1)}. {m.group(2).strip()}", 0))
                elif s.startswith("## "):
                    out.append((1, s[3:].strip(), 0))
                elif s.startswith("### "):
                    out.append((2, s[4:].strip(), 0))
    return [e for e in out if not e[1].lower().startswith("hướng dẫn")] \
        if False else out


def hrule(color=RULE, thickness=0.7, space_before=2, space_after=6):
    return HRFlowable(width="100%", thickness=thickness, color=color,
                      spaceBefore=space_before, spaceAfter=space_after)


BOX_STYLES = {
    ">.": (colors.HexColor("#FAFBFC"), MUTED, colors.HexColor("#DCE3E8")),
    ">": (BLUE_LIGHT, BLUE, colors.HexColor("#D6E4F5")),
    ">!": (RED_LIGHT, RED, colors.HexColor("#F3D6D2")),
    ">+": (GREEN_LIGHT, GREEN, colors.HexColor("#D3ECDC")),
    ">#": (ACCENT_LIGHT, ACCENT, colors.HexColor("#F5E2C4")),
    ">=": (PRIMARY_LIGHT, PRIMARY, colors.HexColor("#D2E2E9")),
}


def _box_kind(s):
    """Return the box prefix (longest first) that this line starts with."""
    for k in (">.", ">!", ">+", ">#", ">=", ">"):
        if s.startswith(k) and (len(s) == len(k) or s[len(k)] in " \t"):
            return k
    return None


def make_box(lines, kind=">"):
    bg, border, _ = BOX_STYLES.get(kind, BOX_STYLES[">"])
    flow = []
    for idx, line in enumerate(lines):
        stripped = line.lstrip()
        if stripped.startswith("- "):
            flow.append(Paragraph(inline(stripped[2:]), S["bullet"]))
        elif re.match(r"^\d+\.\s", stripped):
            flow.append(Paragraph(inline(stripped), S["num"]))
        else:
            text = inline(stripped)
            whole_bold = (stripped.startswith("**") and stripped.endswith("**")
                          and stripped.count("**") == 2 and len(stripped) < 95)
            if idx == 0 and whole_bold:
                flow.append(Paragraph(text, S["box_h"]))
            elif not stripped:
                flow.append(Spacer(1, 3))
            else:
                flow.append(Paragraph(text, S["box"]))
    t = Table([[flow]], colWidths=[AVAIL_W])
    t.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, -1), bg),
        ("LINEBEFORE", (0, 0), (0, -1), 3, border),
        ("BOX", (0, 0), (-1, -1), 0.4, colors.HexColor("#E3E9EC")),
        ("LEFTPADDING", (0, 0), (-1, -1), 9),
        ("RIGHTPADDING", (0, 0), (-1, -1), 9),
        ("TOPPADDING", (0, 0), (-1, -1), 6.5),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 6.5),
        ("VALIGN", (0, 0), (-1, -1), "TOP"),
    ]))
    return t


def make_key_strip(tokens, per_row=8):
    """Small grid of '1C' / '2B' style answer tokens."""
    per_row = max(1, min(per_row, len(tokens)))
    cells, row = [], []
    for tok in tokens:
        m = re.match(r"^(\d+)([A-Za-z]{1,3}|T|F|Đ|S)$", tok)
        num, ans = (m.group(1), m.group(2).upper()) if m else ("", tok)
        inner = Paragraph(
            f'<font size="7" color="#5C6B73">{num}</font>'
            f'<br/><font name="Body-Bold" size="9.5" color="#13924F">{ans}</font>',
            ParagraphStyle("k", fontName="Body", alignment=TA_CENTER, leading=10.5))
        row.append(inner)
        if len(row) == per_row:
            cells.append(row)
            row = []
    cellw = AVAIL_W / 8.0
    if row:
        row += [Paragraph("", S["tcell"])] * (per_row - len(row))
        cells.append(row)
    t = Table(cells, colWidths=[cellw] * per_row, hAlign="CENTER")
    st = [("GRID", (0, 0), (-1, -1), 0.4, RULE),
          ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
          ("TOPPADDING", (0, 0), (-1, -1), 2.5),
          ("BOTTOMPADDING", (0, 0), (-1, -1), 2.5),
          ("BACKGROUND", (0, 0), (-1, -1), colors.HexColor("#F3FAF5")),
          ("LEFTPADDING", (0, 0), (-1, -1), 1),
          ("RIGHTPADDING", (0, 0), (-1, -1), 1)]
    t.setStyle(TableStyle(st))
    return t


def split_row(line):
    line = line.strip()
    if line.startswith("|"):
        line = line[1:]
    if line.endswith("|"):
        line = line[:-1]
    return [c.strip() for c in line.split("|")]


def make_table(rows, widths=None):
    header, body = rows[0], rows[1:]
    ncol = len(header)
    body = [r + [""] * (ncol - len(r)) for r in body]

    if widths is None:
        weights = []
        for i in range(ncol):
            lens = [len(re.sub(r"[*=\[\]]", "", r[i])) if i < len(r) else 0 for r in rows]
            lens.sort()
            w = lens[int(len(lens) * 0.85)] if lens else 6
            weights.append(max(5.0, min(46.0, float(w))))
        total = sum(weights)
        widths = [max(15 * mm, AVAIL_W * w / total) for w in weights]
        # rescale to fit exactly
        scale = AVAIL_W / sum(widths)
        widths = [w * scale for w in widths]
    else:
        total = float(sum(widths))
        widths = [AVAIL_W * w / total for w in widths]

    data = []
    data.append([Paragraph(inline(c), S["thead"]) for c in header])
    for r in body:
        data.append([Paragraph(inline(c), S["tcell"]) for c in r])

    t = Table(data, colWidths=widths, repeatRows=1)
    style = [
        ("BACKGROUND", (0, 0), (-1, 0), PRIMARY),
        ("TEXTCOLOR", (0, 0), (-1, 0), colors.white),
        ("GRID", (0, 0), (-1, -1), 0.4, RULE),
        ("VALIGN", (0, 0), (-1, -1), "TOP"),
        ("LEFTPADDING", (0, 0), (-1, -1), 5),
        ("RIGHTPADDING", (0, 0), (-1, -1), 5),
        ("TOPPADDING", (0, 0), (-1, -1), 4),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 4),
        ("TOPPADDING", (0, 0), (-1, 0), 5),
        ("BOTTOMPADDING", (0, 0), (-1, 0), 5),
    ]
    for i in range(1, len(data)):
        if i % 2 == 0:
            style.append(("BACKGROUND", (0, i), (-1, i), ZEBRA))
    t.setStyle(TableStyle(style))
    return t


# ---------------------------------------------------------------- parsing ---
OPT_RE = re.compile(r"^([A-D])[.)]\s+(.*)$")
LIST_RE = re.compile(r"^(\d+)[.)]\s+(.*)$")
BULLET_RE = re.compile(r"^[-*•]\s+(.*)$")
SUBBULLET_RE = re.compile(r"^\s{2,}[-*•]\s+(.*)$")


def parse_file(path, story):
    with open(path, encoding="utf-8") as fh:
        raw = fh.read()
    lines = []
    for line in raw.split("\n"):
        if "[[" in line and not line.strip().startswith("[["):
            before, _, rest = line.partition("[[")
            lines.append(before.rstrip())
            lines.append("[[" + rest)
        else:
            lines.append(line)
    i = 0
    pending_widths = None
    while i < len(lines):
        line = lines[i].rstrip()
        s = line.strip()

        if not s:
            i += 1
            continue

        # ---- directives
        if s.startswith("[[PART"):
            m = re.match(r"\[\[PART\s+(\S+?)\|([^|\]]*)\|([^|\]]*)\|?([^\]]*)\]\]", s)
            num, title, sub = m.group(1), m.group(2), m.group(3)
            bullets = [b.strip() for b in m.group(4).split(";") if b.strip()]
            story.append(PageBreak())
            story.append(PartOpener(num, title.strip(), sub.strip(), bullets))
            story.append(PageBreak())
            i += 1
            continue

        if s == "[[TOC]]":
            story.append(Paragraph(
                '<font name="Serif-Bold" size="20" color="#08313F">MỤC LỤC</font>',
                ParagraphStyle("toch", fontName="Serif-Bold", leading=24, spaceAfter=2)))
            story.append(HRFlowable(width="100%", thickness=1.6, color=ACCENT,
                                    spaceBefore=1, spaceAfter=4))
            toc_entries = [e for e in ENTRIES if e[0] <= 1]
            chunk = 200
            for k in range(0, len(toc_entries), chunk):
                story.append(TOCFlow(PAGE_MAP, toc_entries[k:k + chunk]))
            i += 1
            continue

        if s == "[[PAGEBREAK]]":
            story.append(PageBreak())
            i += 1
            continue

        if s.startswith("[[KEY "):
            toks = s[6:].rstrip("]").split()
            key = make_key_strip(toks)
            key.spaceBefore = 2
            key.spaceAfter = 6
            story.append(key)
            i += 1
            continue

        if s.startswith("[[W "):
            nums = s[4:].rstrip("]").split()
            pending_widths = [float(x) for x in nums]
            i += 1
            continue

        if s.startswith("[[LINES"):
            n = int(s[7:].rstrip("]").split()[0])
            rows = [[Paragraph(f'<font size="7" color="#B9C6CC">{i+1}</font>',
                               ParagraphStyle("ln", fontName="Body", fontSize=7,
                                              leading=10))]
                    for i in range(n)]
            t = Table(rows, colWidths=[AVAIL_W], rowHeights=[7.2 * mm] * n)
            t.setStyle(TableStyle([
                ("LINEBELOW", (0, 0), (-1, -1), 0.5, RULE),
                ("LEFTPADDING", (0, 0), (-1, -1), 2),
                ("TOPPADDING", (0, 0), (-1, -1), 0),
                ("BOTTOMPADDING", (0, 0), (-1, -1), 0),
                ("VALIGN", (0, 0), (-1, -1), "TOP"),
            ]))
            story.append(Spacer(1, 3))
            story.append(t)
            story.append(Spacer(1, 6))
            i += 1
            continue

        if s.startswith("[[SPACER"):
            mm_val = float(s[9:].rstrip("]").split()[-1])
            story.append(Spacer(1, mm_val * mm))
            i += 1
            continue

        # ---- headings
        if s.startswith("## "):
            title = s[3:].strip()
            story.append(TocMark(1, title))
            story.append(Paragraph(inline(title), S["h2"]))
            story.append(HRFlowable(width="100%", thickness=1.1, color=PRIMARY_LIGHT,
                                    spaceBefore=0, spaceAfter=7))
            i += 1
            continue
        if s.startswith("### "):
            title = s[4:].strip()
            story.append(TocMark(2, title))
            story.append(Paragraph(inline(title), S["h3"]))
            i += 1
            continue
        if s.startswith("#### "):
            story.append(Paragraph(inline(s[5:].strip()), S["h4"]))
            i += 1
            continue

        # ---- section banner  >> TEXT
        if s.startswith(">> "):
            story.append(Spacer(1, 3))
            band = Table([[Paragraph(inline(s[3:].strip()),
                          ParagraphStyle("banner", fontName="Body-Bold", fontSize=9.6,
                                         leading=13, textColor=colors.white,
                                         alignment=TA_LEFT))]], colWidths=[AVAIL_W])
            band.setStyle(TableStyle([
                ("BACKGROUND", (0, 0), (-1, -1), PRIMARY),
                ("LEFTPADDING", (0, 0), (-1, -1), 9),
                ("RIGHTPADDING", (0, 0), (-1, -1), 9),
                ("TOPPADDING", (0, 0), (-1, -1), 5.5),
                ("BOTTOMPADDING", (0, 0), (-1, -1), 5.5),
            ]))
            story.append(KeepTogether([band, Spacer(1, 5)]))
            i += 1
            continue

        # ---- boxes
        if _box_kind(s):
            kind = _box_kind(s)
            block, pending_blank = [], 0
            while i < len(lines):
                cur = lines[i].strip()
                nk = _box_kind(cur)
                if nk == ">" and kind != ">":
                    nk = kind        # plain continuation line of a styled box
                if nk == kind:
                    block.extend([""] * pending_blank)
                    pending_blank = 0
                    block.append(cur[len(kind):].strip())
                    i += 1
                elif not cur:
                    break          # a real blank line always closes the box
                else:
                    break
            box = make_box(block, kind)
            box.spaceBefore = 1.5
            box.spaceAfter = 5
            story.append(box)
            continue

        # ---- tables
        if s.startswith("|"):
            rows = []
            while i < len(lines) and lines[i].strip().startswith("|"):
                cells = split_row(lines[i])
                if not all(re.fullmatch(r":?-{2,}:?", c) for c in cells if c):
                    rows.append(cells)
                i += 1
            if rows:
                tbl = make_table(rows, pending_widths)
                tbl.spaceBefore = 2
                tbl.spaceAfter = 6
                story.append(tbl)
                pending_widths = None
            continue

        # ---- question with options
        if OPT_RE.match(s):
            opts, qtext = [], None
            while i < len(lines) and OPT_RE.match(lines[i].strip()):
                m = OPT_RE.match(lines[i].strip())
                opts.append(m.group(1) + ". " + m.group(2))
                i += 1
            # single column if long options
            if any(len(o) > 46 for o in opts) or len(opts) < 3:
                cells = [[Paragraph(inline(o), S["opt"])] for o in opts]
                t = Table(cells, colWidths=[AVAIL_W - 18])
            else:
                cells, row = [], []
                for o in opts:
                    row.append(Paragraph(inline(o), S["opt"]))
                    if len(row) == 2:
                        cells.append(row)
                        row = []
                if row:
                    cells.append(row + [Paragraph("", S["opt"])])
                half = (AVAIL_W - 18) / 2.0
                t = Table(cells, colWidths=[half, half])
            t.setStyle(TableStyle([
                ("LEFTPADDING", (0, 0), (-1, -1), 0),
                ("RIGHTPADDING", (0, 0), (-1, -1), 2),
                ("TOPPADDING", (0, 0), (-1, -1), 1.2),
                ("BOTTOMPADDING", (0, 0), (-1, -1), 1.2),
                ("VALIGN", (0, 0), (-1, -1), "TOP"),
            ]))
            story.append(t)
            story.append(Spacer(1, 3))
            continue

        # ---- list items
        if SUBBULLET_RE.match(line):
            story.append(Paragraph(inline(SUBBULLET_RE.match(line).group(1)),
                                   S["bullet2"], bulletText="–"))
            i += 1
            continue
        if BULLET_RE.match(s):
            story.append(Paragraph(inline(BULLET_RE.match(s).group(1)),
                                   S["bullet"], bulletText="•"))
            i += 1
            continue
        if re.match(r"^\([a-e]\)\s", s):
            story.append(Paragraph(inline(s), S["optline"]))
            i += 1
            continue

        m = LIST_RE.match(s)
        if m:
            story.append(Paragraph(inline(s), S["num"]))
            i += 1
            continue

        # ---- paragraph: collect consecutive plain lines
        chunk = [s]
        i += 1
        while i < len(lines):
            nxt = lines[i].strip()
            if (not nxt or nxt.startswith(("|", ">", "#", "[[", "- ", "* "))
                    or OPT_RE.match(nxt) or LIST_RE.match(nxt)):
                break
            chunk.append(nxt)
            i += 1
        story.append(P(" ".join(chunk)))


# ---------------------------------------------------------------- document ---
class GuideDoc(BaseDocTemplate):
    def __init__(self, filename, **kw):
        BaseDocTemplate.__init__(self, filename, pagesize=A4,
                                 leftMargin=M_LEFT, rightMargin=M_RIGHT,
                                 topMargin=M_TOP, bottomMargin=M_BOTTOM,
                                 title=DOC_TITLE,
                                 author="Ôn tập Tiếng Anh 10",
                                 subject="Đề cương ôn tập Giữa học kỳ 1 – Global Success",
                                 creator="markup2pdf", **kw)
        frame = Frame(M_LEFT, M_BOTTOM, AVAIL_W, PAGE_H - M_TOP - M_BOTTOM,
                      id="normal", leftPadding=0, rightPadding=0,
                      topPadding=0, bottomPadding=0)
        cover_frame = Frame(M_LEFT - 8 * mm, M_BOTTOM, AVAIL_W + 8 * mm,
                            PAGE_H - M_BOTTOM, id="cover",
                            leftPadding=0, rightPadding=0, topPadding=0, bottomPadding=0)
        self.addPageTemplates([
            PageTemplate(id="cover", frames=[cover_frame], onPage=self._cover_bg),
            PageTemplate(id="body", frames=[frame], onPage=self._decorate),
        ])
        self.section = ""
        self.show_header = True
        self.collected = {}

    # page furniture
    def _cover_bg(self, canv, doc):
        self.show_header = False

    def _decorate(self, canv, doc):
        canv.saveState()
        # top rule
        canv.setStrokeColor(PRIMARY_LIGHT)
        canv.setLineWidth(1)
        canv.line(M_LEFT, PAGE_H - M_TOP + 9, PAGE_W - M_RIGHT, PAGE_H - M_TOP + 9)
        canv.setFont("Body", 7.2)
        canv.setFillColor(MUTED)
        canv.drawString(M_LEFT, PAGE_H - M_TOP + 12.5, DOC_RUNNING)
        self._hdr_canv = canv
        self._hdr_done = False
        # footer
        canv.setStrokeColor(PRIMARY_LIGHT)
        canv.line(M_LEFT, M_BOTTOM - 7, PAGE_W - M_RIGHT, M_BOTTOM - 7)
        canv.setFont("Body", 7.6)
        canv.setFillColor(MUTED)
        canv.drawString(M_LEFT, M_BOTTOM - 17, "Ôn tập hiệu quả = Hiểu bản chất + Luyện đúng dạng")
        canv.restoreState()

    def afterFlowable(self, flowable):
        if isinstance(flowable, PartOpener):
            self.notify("TOCEntry", (0, flowable.toc_text, self.page))
            self.collected.setdefault(flowable.toc_text, self.page)
            self.section = flowable.toc_text
            canv = getattr(self, "_hdr_canv", None)
            if canv is not None and not getattr(self, "_hdr_done", False):
                canv.saveState()
                canv.setFont("Body-Bold", 7.2)
                canv.setFillColor(PRIMARY)
                canv.drawRightString(PAGE_W - M_RIGHT, PAGE_H - M_TOP + 12.5,
                                     self.section[:78])
                canv.restoreState()
                self._hdr_done = True
            return
        if isinstance(flowable, TocMark):
            self.notify("TOCEntry", (flowable.level, flowable.text, self.page))
            self.collected.setdefault(flowable.text, self.page)
            if flowable.level <= 1:
                self.section = re.sub(r"<[^>]+>", "", flowable.text)
                canv = getattr(self, "_hdr_canv", None)
                if canv is not None and not getattr(self, "_hdr_done", False):
                    canv.saveState()
                    canv.setFont("Body-Bold", 7.2)
                    canv.setFillColor(PRIMARY)
                    canv.drawRightString(PAGE_W - M_RIGHT, PAGE_H - M_TOP + 12.5,
                                         self.section[:78])
                    canv.restoreState()
                    self._hdr_done = True


class NumberedCanvas:
    """Draws 'Trang x / y' once the total page count is known."""

    def __init__(self, canvas, doc):
        self._canvas = canvas

    def __getattr__(self, name):
        return getattr(self._canvas, name)


def make_numbered_canvas_class():
    from reportlab.pdfgen import canvas as _canvas

    class _NumCanvas(_canvas.Canvas):
        def __init__(self, *args, **kw):
            _canvas.Canvas.__init__(self, *args, **kw)
            self._saved = []

        def showPage(self):
            self._saved.append(dict(self.__dict__))
            self._startPage()

        def save(self):
            total = len(self._saved)
            for state in self._saved:
                self.__dict__.update(state)
                if self._pageNumber > 1:
                    self.setFont("Body", 7.6)
                    self.setFillColor(MUTED)
                    self.drawRightString(PAGE_W - M_RIGHT, M_BOTTOM - 17,
                                         f"Trang {self._pageNumber} / {total}")
                _canvas.Canvas.showPage(self)
            _canvas.Canvas.save(self)

    return _NumCanvas


# ------------------------------------------------------------------- cover ---
def cover_story():
    story = [Spacer(1, 6 * mm)]
    # eyebrow
    eye = Table([[Paragraph(
        '<font color="#FFFFFF" size="7.6"><b>GLOBAL SUCCESS  ·  UNITS 1 – 2 – 3</b></font>',
        S["body_left"])]], colWidths=[62 * mm])
    eye.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, -1), PRIMARY),
        ("LEFTPADDING", (0, 0), (-1, -1), 8), ("RIGHTPADDING", (0, 0), (-1, -1), 8),
        ("TOPPADDING", (0, 0), (-1, -1), 5), ("BOTTOMPADDING", (0, 0), (-1, -1), 5),
    ]))
    story.append(eye)
    story.append(Spacer(1, 9 * mm))

    story.append(Paragraph(
        '<font name="Serif-Bold" size="27" color="#08313F">ĐỀ CƯƠNG</font>',
        ParagraphStyle("cv1", fontName="Serif-Bold", alignment=TA_LEFT, leading=31)))
    story.append(Paragraph(
        '<font name="Serif-Bold" size="27" color="#08313F">ÔN TẬP GIỮA HỌC KỲ 1</font>',
        ParagraphStyle("cv2", fontName="Serif-Bold", alignment=TA_LEFT, leading=31)))
    story.append(Spacer(1, 3 * mm))
    story.append(Paragraph(
        '<font name="Body-Bold" size="14.5" color="#D98324">MÔN TIẾNG ANH – LỚP 10</font>',
        ParagraphStyle("cv3", fontName="Body-Bold", alignment=TA_LEFT, leading=19)))
    story.append(Spacer(1, 2 * mm))
    story.append(HRFlowable(width="42%", thickness=2.4, color=ACCENT,
                            hAlign="LEFT", spaceBefore=2, spaceAfter=8))
    story.append(Paragraph(
        '<font size="11" color="#1B2A32">Năm học 2026 – 2027</font>',
        ParagraphStyle("cv4", fontName="Body", alignment=TA_LEFT, leading=15)))

    story.append(Spacer(1, 12 * mm))

    # feature grid
    feats = [
        ("Bám sát ma trận", "Phân rã 100% chỉ tiêu ma trận &amp; bảng đặc tả\n"
                            "thành lộ trình ôn tập cụ thể"),
        ("Hệ thống kiến thức", "Từ vựng – Ngữ pháp – Kỹ năng của Unit 1, 2, 3\n"
                               "trình bày dạng bảng, sơ đồ, mẹo nhớ"),
        ("Luyện đúng dạng", "Trọn bộ 8 dạng bài thi + 2 đề thi thử\n"
                            "đúng cấu trúc 28 TN · 6 TL · 1 bài viết"),
        ("Đáp án chi tiết", "Toàn bộ đáp án, giải thích, bài viết mẫu\n"
                            "và thang điểm chấm"),
    ]
    cells = []
    for idx, (t, d) in enumerate(feats):
        inner = [
            Paragraph(f'<font name="Body-Bold" size="9.6" color="#0E4D64">{idx+1:02d}. '
                      f'{t}</font>', S["body_left"]),
            Paragraph(d.replace("\n", "<br/>"),
                      ParagraphStyle("f", fontName="Body", fontSize=8.1, leading=11.6,
                                     textColor=INK)),
        ]
        cells.append(inner)
    grid = Table([cells[:2], cells[2:]], colWidths=[AVAIL_W / 2 - 3 * mm] * 2)
    grid.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, -1), colors.HexColor("#F6F9FA")),
        ("BOX", (0, 0), (-1, -1), 0.5, RULE),
        ("INNERGRID", (0, 0), (-1, -1), 0.5, RULE),
        ("LEFTPADDING", (0, 0), (-1, -1), 8), ("RIGHTPADDING", (0, 0), (-1, -1), 8),
        ("TOPPADDING", (0, 0), (-1, -1), 7), ("BOTTOMPADDING", (0, 0), (-1, -1), 7),
        ("VALIGN", (0, 0), (-1, -1), "TOP"),
    ]))
    story.append(grid)

    story.append(Spacer(1, 14 * mm))
    # stat strip
    stats = [("10", "điểm"), ("28", "câu trắc nghiệm"), ("6", "câu tự luận"),
             ("60", "phút")]
    row = [[Paragraph(f'<font name="Serif-Bold" size="17" color="#0E4D64">{n}</font>'
                      f'<br/><font size="7" color="#5C6B73">{l}</font>',
                      ParagraphStyle("st", fontName="Body", alignment=TA_CENTER, leading=19))
            for n, l in stats]]
    st = Table(row, colWidths=[AVAIL_W / 4.0] * 4)
    st.setStyle(TableStyle([
        ("LINEBEFORE", (1, 0), (-1, -1), 0.6, RULE),
        ("TOPPADDING", (0, 0), (-1, -1), 6), ("BOTTOMPADDING", (0, 0), (-1, -1), 6),
        ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
    ]))
    story.append(st)
    story.append(Spacer(1, 11 * mm))

    # --- what's inside ---------------------------------------------------
    story.append(Paragraph(
        '<font name="Body-Bold" size="8.4" color="#D98324">NỘI DUNG CHÍNH</font>',
        ParagraphStyle("cx", fontName="Body-Bold", alignment=TA_LEFT, leading=11,
                       spaceAfter=4)))
    parts = [
        ("1", "Giải mã đề thi", "Ma trận · bản đồ 28 câu · chiến lược 60 phút"),
        ("2", "Hệ thống kiến thức", "Từ vựng · phát âm · 5 chủ điểm ngữ pháp"),
        ("3", "Kỹ năng &amp; chiến thuật", "Tám dạng bài · 20 mẫu biến đổi câu · viết đoạn"),
        ("4", "Luyện tập theo dạng", "9 khối bài tập · đáp án và giải thích"),
        ("5", "Hai đề thi thử", "Đúng cấu trúc 2026–2027 · bài viết mẫu"),
        ("6", "Tổng ôn &amp; tự đánh giá", "120 từ vựng · lịch ôn 10 ngày · bảng tự chấm"),
    ]
    rows = []
    for num, title, desc in parts:
        left = Paragraph(
            f'<font name="Serif-Bold" size="11" color="#0E4D64">{num}</font>',
            ParagraphStyle("pn", fontName="Serif-Bold", alignment=TA_CENTER, leading=13))
        mid = [
            Paragraph(f'<font name="Body-Bold" size="8.8" color="#08313F">{title}</font>',
                      ParagraphStyle("pt", fontName="Body-Bold", fontSize=8.8,
                                     leading=11.4, alignment=TA_LEFT)),
            Paragraph(f'<font size="7.6" color="#5C6B73">{desc}</font>',
                      ParagraphStyle("pd", fontName="Body", fontSize=7.6,
                                     leading=10, alignment=TA_LEFT)),
        ]
        rows.append([left, mid])
    grid2 = Table(rows, colWidths=[9 * mm, AVAIL_W - 9 * mm])
    gs = [("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
          ("LEFTPADDING", (0, 0), (-1, -1), 0), ("RIGHTPADDING", (0, 0), (-1, -1), 4),
          ("TOPPADDING", (0, 0), (-1, -1), 3.2), ("BOTTOMPADDING", (0, 0), (-1, -1), 3.2)]
    grid2.setStyle(TableStyle(gs))
    story.append(grid2)

    story.append(Spacer(1, 9 * mm))
    band = Table([[Paragraph(
        '<font name="Body-Bold" size="8.6" color="#FFFFFF">“Ôn đúng cách quan trọng hơn ôn '
        'nhiều.”</font><br/><font size="7.4" color="#C9D6DD">6 phần – 8 dạng bài – 2 đề thi thử – lịch ôn '
        '10 ngày.</font>',
        ParagraphStyle("bd", fontName="Body-Bold", alignment=TA_LEFT, leading=12))]],
        colWidths=[AVAIL_W])
    band.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, -1), PRIMARY_DARK),
        ("LEFTPADDING", (0, 0), (-1, -1), 10), ("RIGHTPADDING", (0, 0), (-1, -1), 10),
        ("TOPPADDING", (0, 0), (-1, -1), 8), ("BOTTOMPADDING", (0, 0), (-1, -1), 8),
    ]))
    story.append(band)
    story.append(Spacer(1, 4 * mm))
    story.append(Paragraph(
        '<font size="7.4" color="#8A99A1">Tài liệu lưu hành nội bộ – dùng cho học sinh ôn thi '
        'giữa học kỳ 1. Nội dung biên soạn dựa trên Ma trận &amp; Bảng đặc tả kỹ thuật '
        'đề kiểm tra môn Tiếng Anh 10, năm học 2026–2027.</font>',
        ParagraphStyle("cvf", fontName="Body", alignment=TA_LEFT, leading=10)))
    story.append(NextPageTemplate("body"))
    story.append(PageBreak())
    return story


# --------------------------------------------------------------- build ------
def collect_sources(args):
    if args:
        files = []
        for a in args:
            files.extend(sorted(glob.glob(a)))
        return files
    return sorted(glob.glob(os.path.join(ROOT, "content", "*.md")))


def main(argv=None):
    ap = argparse.ArgumentParser()
    ap.add_argument("--out", default=os.path.join(
        ROOT, "DE_CUONG_ON_TAP_TIENG_ANH_10_GK1_2026-2027.pdf"))
    ap.add_argument("sources", nargs="*")
    args = ap.parse_args(argv)

    register_fonts()
    files = collect_sources(args.sources)
    if not files:
        sys.exit("No content files found.")

    global ENTRIES
    entries = scan_entries(files)
    ENTRIES = entries

    # pass 1 – measure page numbers (throwaway)
    global PAGE_MAP
    PAGE_MAP = {e[1]: 0 for e in entries}
    story = cover_story()
    for f in files:
        parse_file(f, story)
    tmp = args.out + ".pass1.pdf"
    doc = GuideDoc(tmp)
    doc.multiBuild(story, canvasmaker=make_numbered_canvas_class())
    PAGE_MAP = dict(doc.collected)
    if os.path.exists(tmp):
        os.remove(tmp)

    # pass 2 – final build with real page numbers
    story = cover_story()
    for f in files:
        parse_file(f, story)
    doc = GuideDoc(args.out)
    doc.multiBuild(story, canvasmaker=make_numbered_canvas_class())
    print(f"Wrote {args.out}")
    try:
        from pypdf import PdfReader
        print("pages:", len(PdfReader(args.out).pages))
    except Exception:
        pass


if __name__ == "__main__":
    main()
