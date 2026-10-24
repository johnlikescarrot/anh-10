#!/usr/bin/env python3
"""
Build the PDF revision guide (đề cương ôn tập) from Markdown sources.

Usage:
    python tools/build_pdf.py content/*.md -o DE_CUONG.pdf

Markdown subset supported:
    # H1            -> part title (new page, big band)
    ## H2           -> chapter  (TOC level 1)
    ### H3          -> section  (TOC level 2)
    #### H4         -> sub-section (no TOC)
    - item          -> bullet
    1. item         -> numbered
    | a | b |       -> table (first row = header, "---" separator optional)
    > text          -> callout box (continuation lines starting with "> ")
    ---             -> horizontal rule
    \\newpage        -> page break
Inline: **bold**, *italic*, `code`
"""
import re
import sys
import copy
import argparse
import os

from reportlab.lib import colors
from reportlab.lib.enums import TA_CENTER, TA_JUSTIFY, TA_LEFT, TA_RIGHT
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle, StyleSheet1
from reportlab.lib.units import cm, mm
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import (
    BaseDocTemplate, Frame, PageTemplate, Paragraph, Spacer, Table, TableStyle,
    PageBreak, KeepTogether, Flowable, NextPageTemplate, CondPageBreak,
)
from reportlab.platypus.flowables import HRFlowable

# --------------------------------------------------------------------------- #
# Fonts
# --------------------------------------------------------------------------- #
FONT_DIR = "/usr/share/fonts/truetype/dejavu"
pdfmetrics.registerFont(TTFont("DJ", f"{FONT_DIR}/DejaVuSans.ttf"))
pdfmetrics.registerFont(TTFont("DJ-B", f"{FONT_DIR}/DejaVuSans-Bold.ttf"))
pdfmetrics.registerFont(TTFont("DJ-M", f"{FONT_DIR}/DejaVuSansMono.ttf"))
# no italic face available in this container -> map italic to the roman face
pdfmetrics.registerFontFamily(
    "DJ", normal="DJ", bold="DJ-B", italic="DJ", boldItalic="DJ-B"
)

# --------------------------------------------------------------------------- #
# Palette
# --------------------------------------------------------------------------- #
INK      = colors.HexColor("#1A2B34")
TEAL     = colors.HexColor("#0F4C5C")
TEAL_D   = colors.HexColor("#08323B")
TEAL_L   = colors.HexColor("#E7F1F3")
ACCENT   = colors.HexColor("#D9531E")
ACCENT_L = colors.HexColor("#FBEDE6")
GOLD     = colors.HexColor("#B07D1166")
GREY     = colors.HexColor("#5B6B73")
RULE     = colors.HexColor("#C9D6DB")
GREEN    = colors.HexColor("#1E6B47")
GREEN_L  = colors.HexColor("#E6F3EC")
ZEBRA    = colors.HexColor("#F4F8F9")

PAGE_W, PAGE_H = A4
LM = RM = 1.55 * cm
TM = 1.85 * cm
BM = 1.55 * cm

TITLE_RUNNING = "ĐỀ CƯƠNG ÔN TẬP GIỮA HỌC KÌ 1  •  TIẾNG ANH 10  •  2026–2027"


# --------------------------------------------------------------------------- #
# Styles
# --------------------------------------------------------------------------- #
def build_styles():
    ss = StyleSheet1()
    ss.add(ParagraphStyle(
        "Body", fontName="DJ", fontSize=9.6, leading=14.6, textColor=INK,
        alignment=TA_JUSTIFY, spaceAfter=5.5, spaceBefore=0))
    ss.add(ParagraphStyle(
        "BodyTight", parent=ss["Body"], spaceAfter=2.5))
    ss.add(ParagraphStyle(
        "H1", fontName="DJ-B", fontSize=21, leading=26, textColor=TEAL_D,
        spaceBefore=0, spaceAfter=2, alignment=TA_LEFT))
    ss.add(ParagraphStyle(
        "H1Sub", fontName="DJ", fontSize=10.5, leading=15, textColor=GREY,
        spaceAfter=14, alignment=TA_LEFT))
    ss.add(ParagraphStyle(
        "H2", fontName="DJ-B", fontSize=14.6, leading=19, textColor=TEAL,
        spaceBefore=15, spaceAfter=7, alignment=TA_LEFT,
        keepWithNext=1, backColor=None))
    ss.add(ParagraphStyle(
        "H3", fontName="DJ-B", fontSize=11.4, leading=15.5, textColor=TEAL_D,
        spaceBefore=11, spaceAfter=5, alignment=TA_LEFT, keepWithNext=1))
    ss.add(ParagraphStyle(
        "H4", fontName="DJ-B", fontSize=9.9, leading=14, textColor=ACCENT,
        spaceBefore=8, spaceAfter=3.5, alignment=TA_LEFT, keepWithNext=1))
    ss.add(ParagraphStyle(
        "Bullet", parent=ss["Body"], leftIndent=13, bulletIndent=3,
        spaceAfter=2.8, alignment=TA_LEFT))
    ss.add(ParagraphStyle(
        "Num", parent=ss["Body"], leftIndent=17, bulletIndent=2,
        spaceAfter=2.8, alignment=TA_LEFT))
    ss.add(ParagraphStyle(
        "NumQ", fontName="DJ", fontSize=9.6, leading=14.6, textColor=INK,
        leftIndent=17, alignment=TA_LEFT, spaceAfter=1.5))
    ss.add(ParagraphStyle(
        "Option", fontName="DJ", fontSize=9.0, leading=12.4, textColor=INK,
        leftIndent=14, alignment=TA_LEFT, spaceAfter=0))
    ss.add(ParagraphStyle(
        "LetterItem", fontName="DJ", fontSize=9.6, leading=14.2,
        textColor=INK, leftIndent=26, firstLineIndent=-12,
        alignment=TA_LEFT, spaceAfter=2.2))
    ss.add(ParagraphStyle(
        "FillItem", fontName="DJ", fontSize=9.6, leading=14.6,
        textColor=INK, alignment=TA_LEFT, leftIndent=17, spaceAfter=0))
    ss.add(ParagraphStyle(
        "TableCell", fontName="DJ", fontSize=8.5, leading=11.8, textColor=INK,
        alignment=TA_LEFT))
    ss.add(ParagraphStyle(
        "TableHead", fontName="DJ-B", fontSize=8.5, leading=11.8,
        textColor=colors.white, alignment=TA_LEFT))
    ss.add(ParagraphStyle(
        "Callout", fontName="DJ", fontSize=9.3, leading=13.8, textColor=INK,
        alignment=TA_LEFT, spaceAfter=0))
    ss.add(ParagraphStyle(
        "TOC1", fontName="DJ-B", fontSize=8.9, leading=11.2, textColor=TEAL_D,
        spaceBefore=0))
    ss.add(ParagraphStyle(
        "TOC2", fontName="DJ", fontSize=8.3, leading=10.4, textColor=INK,
        leftIndent=14))
    ss.add(ParagraphStyle(
        "CoverTitle", fontName="DJ-B", fontSize=31, leading=38,
        textColor=colors.white, alignment=TA_LEFT))
    ss.add(ParagraphStyle(
        "CoverSub", fontName="DJ", fontSize=13, leading=19,
        textColor=colors.HexColor("#CDE4E9"), alignment=TA_LEFT))
    ss.add(ParagraphStyle(
        "CoverTag", fontName="DJ-B", fontSize=9.5, leading=13,
        textColor=colors.HexColor("#F6C9A8"), alignment=TA_LEFT))
    ss.add(ParagraphStyle(
        "CoverBox", fontName="DJ", fontSize=9.6, leading=15,
        textColor=colors.white, alignment=TA_LEFT))
    return ss


STY = build_styles()


# --------------------------------------------------------------------------- #
# Inline markdown
# --------------------------------------------------------------------------- #
def inline(text):
    """Convert a small inline-markdown subset into well-formed RML.

    Uses a state machine so that bold/italic can nest without producing
    crossing tags (which reportlab rejects).
    """
    text = text.replace("<br>", "\x01").replace("<br/>", "\x01")
    text = text.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")
    text = text.replace("\x01", "<br/>")
    runs = []          # (text, bold, italic, code)
    buf = []
    bold = italic = False
    i = 0

    def flush(code=False):
        if buf:
            runs.append(("".join(buf), bold, italic, code))
            buf.clear()

    while i < len(text):
        if text.startswith("***", i):
            flush(); bold = not bold; italic = not italic; i += 3
        elif text.startswith("**", i):
            flush(); bold = not bold; i += 2
        elif text[i] == "*":
            flush(); italic = not italic; i += 1
        elif text[i] == "`":
            j = text.find("`", i + 1)
            if j == -1:
                buf.append(text[i]); i += 1
            else:
                flush()
                runs.append((text[i + 1:j], bold, italic, True))
                i = j + 1
        else:
            buf.append(text[i]); i += 1
    flush()

    out = []
    for txt, b, it, code in runs:
        if not txt:
            continue
        if code:
            txt = ('<font name="DJ-M" size="8.4" color="#0F4C5C">%s</font>' % txt)
        if b or it:
            # escape any font tags already inserted -> keep simple: apply
            # formatting outside the code font
            inner = txt
            if it:
                inner = "<i>%s</i>" % inner
            if b:
                inner = "<b>%s</b>" % inner
            txt = inner
        out.append(txt)
    return "".join(out)


def strip_md(text):
    text = text.replace("***", "").replace("**", "")
    return text.replace("`", "").replace("*", "")


# --------------------------------------------------------------------------- #
# Flowables
# --------------------------------------------------------------------------- #
class PartBand(Flowable):
    """Full-width coloured band announcing a Part (H1)."""

    def __init__(self, number, title, subtitle="", toc=None):
        Flowable.__init__(self)
        self.number = number
        self.title = title
        self.subtitle = subtitle
        if toc:
            self._toc_level = 1
            self._toc_text = toc
        self.width = PAGE_W - LM - RM
        self.height = 0

    def wrap(self, aw, ah):
        self.width = aw
        self.height = 68 if self.subtitle else 56
        return self.width, self.height

    def draw(self):
        c = self.canv
        w, h = self.width, self.height
        c.setFillColor(TEAL)
        c.roundRect(0, 0, w, h, 5, stroke=0, fill=1)
        c.setFillColor(ACCENT)
        c.rect(0, 0, 7, h, stroke=0, fill=1)
        c.setFillColor(colors.HexColor("#8FBEC7"))
        c.setFont("DJ-B", 9.5)
        c.drawString(20, h - 20, self.number.upper())
        c.setFillColor(colors.white)
        size = 18.0
        limit = w - 34
        while size > 11 and pdfmetrics.stringWidth(
                self.title, "DJ-B", size) > limit:
            size -= 0.5
        c.setFont("DJ-B", size)
        c.drawString(20, h - 41, self.title)
        if self.subtitle:
            c.setFillColor(colors.HexColor("#BFDCE2"))
            c.setFont("DJ", 8.6)
            c.drawString(20, 11, self.subtitle)


class SectionRule(Flowable):
    """Thin accent rule under an H2 heading."""

    def __init__(self):
        Flowable.__init__(self)
        self.width = PAGE_W - LM - RM
        self.height = 3

    def draw(self):
        c = self.canv
        c.setStrokeColor(RULE)
        c.setLineWidth(0.8)
        c.line(0, 1.5, self.width, 1.5)
        c.setStrokeColor(ACCENT)
        c.setLineWidth(2)
        c.line(0, 1.5, 42, 1.5)


class FillLine(Flowable):
    """A prompt line ("> The plants") followed by a dotted rule to the margin."""

    def __init__(self, markup, plain, style, indent=17):
        Flowable.__init__(self)
        self.plain = plain
        self.indent = indent
        self.p = Paragraph(markup, style)
        self.width = 0
        self.height = 0
        self._tw = pdfmetrics.stringWidth(plain, "DJ", style.fontSize)

    def wrap(self, aw, ah):
        w, h = self.p.wrap(aw, ah)
        self.width, self.height = aw, h + 1.5
        return self.width, self.height

    def draw(self):
        c = self.canv
        self.p.drawOn(c, 0, 3)
        x0 = min(self.indent + self._tw + 6, self.width - 1.0 * cm)
        c.setStrokeColor(colors.HexColor("#9AAFB6"))
        c.setLineWidth(0.55)
        c.setDash(1.4, 2.0)
        c.line(x0, 5.2, self.width - 2, 5.2)
        c.setDash()


class TocHeading(Paragraph):
    """Paragraph that records itself for the table of contents."""

    def __init__(self, text, style, level, toc_text=None):
        Paragraph.__init__(self, text, style)
        self._toc_level = level
        self._toc_text = toc_text or strip_md(text)


class QuestionNo(Flowable):
    """Small numbered chip used to open a question block."""

    def __init__(self, label, colour=TEAL):
        Flowable.__init__(self)
        self.label = label
        self.colour = colour

    def wrap(self, aw, ah):
        self.width = aw
        self.height = 0
        return 0, 0

    def draw(self):
        pass


# --------------------------------------------------------------------------- #
# Markdown block parser
# --------------------------------------------------------------------------- #
def md_table(rows, avail):
    head = rows[0]
    body = rows[1:]
    ncol = max(len(r) for r in rows)
    rows = [r + [""] * (ncol - len(r)) for r in rows]

    def cell_w(txt, f="DJ", size=8.5):
        return pdfmetrics.stringWidth(strip_md(txt), f, size)

    natural, minimum = [], []
    for i in range(ncol):
        longest = max(cell_w(r[i]) for r in rows) + 12
        # longest single word cannot be broken -> hard lower bound
        words = [cell_w(w) for r in rows for w in strip_md(r[i]).split()] or [0]
        hard = max(words) + 12
        natural.append(longest)
        minimum.append(min(longest, max(hard, 1.5 * cm)))

    # Answer-grid detection: many short columns -> equal widths, narrow label
    grid = (ncol >= 6
            and max(len(strip_md(r[0])) for r in rows) <= 8
            and max(len(strip_md(c)) for r in rows for c in r[1:]) <= 12)
    if grid:
        first = 1.85 * cm
        rest = (avail - first) / (ncol - 1)
        widths = [first] + [rest] * (ncol - 1)
        return _table_from_rows(rows, widths)

    total_nat, total_min = sum(natural), sum(minimum)
    if total_nat <= avail:
        # scale every column to its natural width (keeps proportions readable)
        k = avail / total_nat
        widths = [w * k for w in natural]
        # no column may fall below a usable minimum: take the shortfall from
        # the widest column
        floor = 1.55 * cm
        for _ in range(ncol):
            short = [i for i in range(ncol) if widths[i] < floor]
            if not short:
                break
            deficit = sum(floor - widths[i] for i in short)
            widest = max(range(ncol), key=lambda i: widths[i])
            widths[widest] -= deficit
            for i in short:
                widths[i] = floor
    elif total_min >= avail:
        k = avail / total_min
        widths = [w * k for w in minimum]
    else:
        # proportional to natural width, but never below the hard minimum
        widths = [avail * natural[i] / total_nat for i in range(ncol)]
        for _ in range(ncol):
            short = [i for i in range(ncol) if widths[i] < minimum[i] - 0.01]
            if not short:
                break
            need = sum(minimum[i] - widths[i] for i in short)
            roomy = [i for i in range(ncol) if widths[i] > minimum[i] + 0.01]
            avail_room = sum(widths[i] - minimum[i] for i in roomy) or 1
            for i in roomy:
                widths[i] -= need * (widths[i] - minimum[i]) / avail_room
            for i in short:
                widths[i] = minimum[i]

    # Grid-like tables (many columns of short values) look wrong when one
    # label column hogs the width: cap any column at 1.6x the fair share and
    # hand the surplus back to the others.
    if ncol >= 6:
        cap = 1.6 * avail / ncol
        for _ in range(ncol):
            over = [i for i in range(ncol) if widths[i] > cap + 0.5]
            if not over:
                break
            freed = sum(widths[i] - cap for i in over)
            for i in over:
                widths[i] = cap
            room = [i for i in range(ncol) if widths[i] < cap - 0.5]
            tw = sum(widths[i] for i in room) or 1
            for i in room:
                widths[i] += freed * widths[i] / tw

    return _table_from_rows(rows, widths)


def _table_from_rows(rows, widths):
    data = []
    for j, r in enumerate(rows):
        st = STY["TableHead"] if j == 0 else STY["TableCell"]
        cells = []
        for cell in r:
            txt = inline(cell.strip())
            if txt.startswith("^"):
                txt = '<para align="center">%s</para>' % txt[1:].strip()
            cells.append(Paragraph(txt or "&nbsp;", st))
        data.append(cells)

    t = Table(data, colWidths=widths, repeatRows=1, hAlign="LEFT")
    style = [
        ("BACKGROUND", (0, 0), (-1, 0), TEAL),
        ("TEXTCOLOR", (0, 0), (-1, 0), colors.white),
        ("VALIGN", (0, 0), (-1, -1), "TOP"),
        ("GRID", (0, 0), (-1, -1), 0.4, RULE),
        ("LINEBELOW", (0, 0), (-1, 0), 0.4, TEAL),
        ("TOPPADDING", (0, 0), (-1, -1), 3.4),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 3.4),
        ("LEFTPADDING", (0, 0), (-1, -1), 4.5),
        ("RIGHTPADDING", (0, 0), (-1, -1), 4.5),
    ]
    for i in range(1, len(rows)):
        if i % 2 == 0:
            style.append(("BACKGROUND", (0, i), (-1, i), ZEBRA))
    t.setStyle(TableStyle(style))
    return t


LIST_ITEM = re.compile(r"^([a-e]|[0-9]{1,2})\.\s")
LEAD_BOLD = re.compile(r"^\*\*[^*]+\*\*")


def md_callout(lines, avail):
    # A ">" block keeps its internal line structure: list items and lines
    # that open with a bold lead-in start a new paragraph.
    segs, cur = [], []
    for l in lines:
        t = l.strip()
        if not t:
            if cur:
                segs.append(" ".join(cur))
                cur = []
            continue
        starts_new = (LIST_ITEM.match(t) or LEAD_BOLD.match(t)) and cur
        if starts_new:
            segs.append(" ".join(cur))
            cur = [t]
        else:
            cur.append(t)
    if cur:
        segs.append(" ".join(cur))

    listy = sum(1 for sg in segs if LIST_ITEM.match(sg) or LEAD_BOLD.match(sg))
    sep = "<br/>" if listy >= max(1, len(segs) - 1) else "<br/><br/>"
    text = sep.join(segs)

    kind = "note"
    lower = strip_md(text).lower()
    if "đáp án" in lower[:22] or lower.startswith("✅") \
            or "answer key" in lower[:26] or lower.startswith("gợi ý"):
        kind = "answer"
    elif lower.startswith("⚠") or "cảnh báo" in lower[:18] \
            or "lỗi" in lower[:12] or "trap" in lower[:12]:
        kind = "warn"
    elif lower.startswith("💡") or "mẹo" in lower[:10] or "tip" in lower[:8]:
        kind = "tip"

    bg, bar, fg = {
        "note":   (TEAL_L, TEAL, TEAL_D),
        "answer": (GREEN_L, GREEN, GREEN),
        "warn":   (ACCENT_L, ACCENT, colors.HexColor("#8A3212")),
        "tip":    (colors.HexColor("#FFF8E1"), colors.HexColor("#C9A227"),
                   colors.HexColor("#6B5411")),
    }[kind]

    p = Paragraph(inline(text), ParagraphStyle(
        "co", parent=STY["Callout"], textColor=fg))
    t = Table([[p]], colWidths=[avail], hAlign="LEFT")
    t.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, -1), bg),
        ("LINEBEFORE", (0, 0), (0, -1), 3, bar),
        ("BOX", (0, 0), (-1, -1), 0.3, colors.Color(0, 0, 0, 0)),
        ("LEFTPADDING", (0, 0), (-1, -1), 8),
        ("RIGHTPADDING", (0, 0), (-1, -1), 8),
        ("TOPPADDING", (0, 0), (-1, -1), 5.5),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 5.5),
    ]))
    return t


OPT_SPLIT = re.compile(r"(?=(?<![A-Za-z])[A-D]\.\s)")


def split_options(line):
    """Split 'A. foo B. bar C. baz D. qux' (any spacing) into 4 strings."""
    line = line.strip()
    parts = [p.strip() for p in OPT_SPLIT.split(line) if p.strip()]
    return parts


def options_block(opts, avail, label=None):
    """Lay MCQ options out in 4 columns (or 2x2 when long), optional label."""
    texts = [strip_md(o) for o in opts]
    single_row = (len(opts) == 4
                  and max(len(t) for t in texts) <= 26
                  and sum(pdfmetrics.stringWidth(t, "DJ", 9.0)
                          for t in texts) < avail - 26)
    if single_row:
        row = [Paragraph(inline(o), STY["Option"]) for o in opts]
        data = [row]
        widths = [avail / 4.0] * 4
    else:
        rows = [opts[i:i + 2] for i in range(0, len(opts), 2)]
        data = [[Paragraph(inline(o), STY["Option"]) for o in r] for r in rows]
        widths = [avail * 0.47, avail * 0.53]

    if label:
        lab_w = 1.30 * cm
        rest = avail - lab_w
        k = rest / sum(widths)
        widths = [lab_w] + [w * k for w in widths]
        lab = Paragraph(inline(label), ParagraphStyle(
            "lab", parent=STY["Option"], leftIndent=0, fontSize=9.6))
        data = [[lab] + r for r in data]
        try:
            data[0][0].style = ParagraphStyle("lab2", parent=STY["Option"],
                                              leftIndent=0)
        except Exception:
            pass
        data[0][0] = Paragraph(inline(label), ParagraphStyle(
            "lab3", parent=STY["Option"], leftIndent=0))

    t = Table(data, colWidths=widths, hAlign="LEFT")
    t.setStyle(TableStyle([
        ("VALIGN", (0, 0), (-1, -1), "TOP"),
        ("SPAN", (0, 0), (0, -1)) if label else ("TOPPADDING", (0, 0), (0, 0), 1.2),
        ("LEFTPADDING", (0, 0), (-1, -1), 0),
        ("RIGHTPADDING", (0, 0), (-1, -1), 6),
        ("TOPPADDING", (0, 0), (-1, -1), 1.2),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 2.6),
    ]))
    return t


def parse_markdown(text, avail):
    flow = []
    lines = text.split("\n")
    i = 0
    story_meta = []   # (kind, payload) for TOC placeholder insertion
    while i < len(lines):
        raw = lines[i]
        line = raw.rstrip()
        stripped = line.strip()

        if not stripped:
            i += 1
            continue

        if stripped in ("\\newpage", "<newpage>"):
            flow.append(PageBreak())
            i += 1
            continue

        if stripped == "---":
            flow.append(Spacer(1, 4))
            flow.append(HRFlowable(width="100%", thickness=0.6, color=RULE,
                                   spaceBefore=0, spaceAfter=8))
            i += 1
            continue

        # tables
        if stripped.startswith("|"):
            rows = []
            while i < len(lines) and lines[i].strip().startswith("|"):
                row = lines[i].strip().strip("|")
                if not re.fullmatch(r"[\s:\-\|]+", row):
                    cells = [c.strip() for c in row.split("|")]
                    rows.append(cells)
                i += 1
            if rows:
                flow.append(Spacer(1, 2))
                flow.append(md_table(rows, avail))
                flow.append(Spacer(1, 7))
            continue

        # callouts
        if stripped.startswith("> "):
            buf = []
            while i < len(lines) and lines[i].strip().startswith(">"):
                buf.append(lines[i].strip()[1:].strip())
                i += 1
            flow.append(Spacer(1, 2))
            flow.append(md_callout(buf, avail))
            flow.append(Spacer(1, 8))
            continue

        # headings
        m = re.match(r"^(#{1,4})\s+(.*)$", stripped)
        if m:
            level = len(m.group(1))
            title = m.group(2).strip()
            if level == 1:
                if flow:
                    # start the part on a fresh page unless there is a good
                    # amount of room left (avoids near-empty pages)
                    flow.append(CondPageBreak(9.2 * cm))
                flow.append(PartBand("", title, toc=strip_md(title)))
                flow.append(Spacer(1, 13))
            elif level == 2:
                flow.append(CondPageBreak(3.8 * cm))
                flow.append(Spacer(1, 3))
                flow.append(TocHeading(inline(title), STY["H2"], 2, strip_md(title)))
                flow.append(SectionRule())
                flow.append(Spacer(1, 6))
            elif level == 3:
                flow.append(CondPageBreak(2.9 * cm))
                flow.append(Paragraph(inline(title), STY["H3"]))
            else:
                flow.append(Paragraph(inline(title), STY["H4"]))
            i += 1
            continue

        # MCQ option lines:  "A. foo  B. bar  C. baz  D. qux"
        if re.match(r"^[A-D]\.\s", stripped):
            opts = []
            while i < len(lines) and re.match(r"^[A-D]\.\s",
                                              lines[i].strip()):
                opts += split_options(lines[i])
                i += 1
            if len(opts) >= 2:
                block = options_block(opts, avail)
                # keep a question stem glued to its options
                if (flow and isinstance(flow[-1], Paragraph)
                        and getattr(flow[-1].style, "name", "") in
                        ("Num", "NumQ", "Body", "BodyTight", "Option")):
                    stem = flow.pop()
                    flow.append(KeepTogether([stem, block]))
                else:
                    flow.append(KeepTogether([block]))
            continue

        # lettered sub-items:  "a. Second, ..."
        if re.match(r"^[a-e]\.\s", stripped):
            while i < len(lines) and re.match(r"^[a-e]\.\s",
                                              lines[i].strip()):
                item = lines[i].strip()
                if "→" in item:
                    item = item.split("→")[0].strip()
                flow.append(Paragraph(inline(item), STY["LetterItem"]))
                i += 1
            flow.append(Spacer(1, 3))
            continue

        # bullets
        if re.match(r"^[-•]\s+", stripped):
            buf = []
            while i < len(lines) and re.match(r"^[-•]\s+", lines[i].strip()):
                buf.append(re.sub(r"^[-•]\s+", "", lines[i].strip()))
                i += 1
            for b in buf:
                flow.append(Paragraph(inline(b), STY["Bullet"],
                                      bulletText="•"))
            flow.append(Spacer(1, 4))
            continue

        # numbered list
        m = re.match(r"^(\d+)[.)]\s+(.*)$", stripped)
        if m:
            while i < len(lines):
                m2 = re.match(r"^(\d+)[.)]\s+(.*)$", lines[i].strip())
                if not m2:
                    break
                body_txt = m2.group(2)
                parts = split_options(body_txt)
                if (len(parts) >= 3
                        and re.match(r"^[A-D]\.\s", body_txt.strip())):
                    flow.append(options_block(parts, avail,
                                              label=m2.group(1) + "."))
                else:
                    flow.append(Paragraph(inline(body_txt), STY["Num"],
                                          bulletText=f"{m2.group(1)}."))
                i += 1
            flow.append(Spacer(1, 4))
            continue

        # answer-line items ("→ The plants ______")
        if stripped.startswith("→") and "___" in stripped:
            txt = re.sub(r"_{2,}\s*$", "", stripped).rstrip()
            flow.append(FillLine(inline(txt + " "), strip_md(txt) + " ",
                                 STY["FillItem"]))
            i += 1
            continue

        # paragraph
        buf = [stripped]
        i += 1
        while i < len(lines):
            nxt = lines[i].strip()
            if (not nxt or nxt.startswith("#") or nxt.startswith("|")
                    or nxt.startswith(">") or re.match(r"^[-•]\s+", nxt)
                    or re.match(r"^\d+[.)]\s+", nxt) or nxt == "---"):
                break
            buf.append(nxt)
            i += 1
        flow.append(Paragraph(inline(" ".join(buf)), STY["Body"]))
    return flow


# --------------------------------------------------------------------------- #
# Document template
# --------------------------------------------------------------------------- #
class Doc(BaseDocTemplate):
    def __init__(self, filename, **kw):
        BaseDocTemplate.__init__(self, filename, pagesize=A4,
                                 leftMargin=LM, rightMargin=RM,
                                 topMargin=TM, bottomMargin=BM,
                                 title="Đề cương ôn tập Giữa học kì 1 – Tiếng Anh 10 – 2026-2027",
                                 author="Tổ Tiếng Anh", **kw)
        self.toc = []
        self.cover_pages = 0
        frame_cover = Frame(LM, BM, PAGE_W - LM - RM, PAGE_H - BM - TM,
                            id="cover", leftPadding=0, rightPadding=0,
                            topPadding=0, bottomPadding=0)
        frame_body = Frame(LM, BM, PAGE_W - LM - RM, PAGE_H - BM - TM,
                           id="body", leftPadding=0, rightPadding=0,
                           topPadding=0, bottomPadding=0)
        self.addPageTemplates([
            PageTemplate(id="cover", frames=[frame_cover], onPage=self.cover_bg),
            PageTemplate(id="body", frames=[frame_body], onPage=self.body_bg),
        ])

    def cover_bg(self, canv, doc):
        canv.saveState()
        canv.setFillColor(TEAL)
        canv.rect(0, 0, PAGE_W, PAGE_H, stroke=0, fill=1)
        canv.setFillColor(TEAL_D)
        canv.rect(0, PAGE_H - 4.6 * cm, PAGE_W, 4.6 * cm, stroke=0, fill=1)
        canv.setFillColor(colors.HexColor("#14606F"))
        canv.circle(PAGE_W - 1.2 * cm, 1.6 * cm, 3.4 * cm, stroke=0, fill=1)
        canv.setFillColor(colors.HexColor("#1B7183"))
        canv.circle(PAGE_W - 5.6 * cm, 0.6 * cm, 2.0 * cm, stroke=0, fill=1)
        canv.setFillColor(ACCENT)
        canv.rect(LM, PAGE_H - 2.05 * cm, 2.3 * cm, 0.16 * cm, stroke=0, fill=1)
        canv.restoreState()

    def body_bg(self, canv, doc):
        canv.saveState()
        canv.setFont("DJ", 7.4)
        canv.setFillColor(GREY)
        canv.drawString(LM, PAGE_H - 1.16 * cm,
                        "ĐỀ CƯƠNG ÔN TẬP GK1 – TIẾNG ANH 10 – GLOBAL SUCCESS")
        canv.drawRightString(PAGE_W - RM, PAGE_H - 1.16 * cm, "2026 – 2027")
        canv.setStrokeColor(RULE)
        canv.setLineWidth(0.6)
        canv.line(LM, PAGE_H - 1.32 * cm, PAGE_W - RM, PAGE_H - 1.32 * cm)
        canv.line(LM, 1.16 * cm, PAGE_W - RM, 1.16 * cm)
        canv.setFont("DJ", 7.6)
        canv.setFillColor(GREY)
        canv.drawCentredString(PAGE_W / 2, 0.82 * cm, str(canv.getPageNumber()))
        canv.restoreState()

    def afterFlowable(self, flowable):
        lvl = getattr(flowable, "_toc_level", None)
        if lvl:
            self.toc.append((lvl, flowable._toc_text, self.page))
            try:
                key = "toc%d" % len(self.toc)
                self.canv.bookmarkPage(key)
                self.canv.addOutlineEntry(
                    self._plain(flowable._toc_text), key,
                    level=0 if lvl == 1 else 1, closed=(lvl == 1))
            except Exception:
                pass

    @staticmethod
    def _plain(text):
        import re as _re
        return _re.sub(r"<[^>]+>", "", text)


# --------------------------------------------------------------------------- #
# Cover + TOC
# --------------------------------------------------------------------------- #
def cover_story():
    s = []
    s.append(Spacer(1, PAGE_H - TM - BM - 12.4 * cm))
    s.append(Paragraph("TÀI LIỆU ÔN THI  •  LỚP 10", STY["CoverTag"]))
    s.append(Spacer(1, 8))
    s.append(Paragraph("ĐỀ CƯƠNG<br/>ÔN TẬP", STY["CoverTitle"]))
    s.append(Spacer(1, 10))
    s.append(Paragraph("TIẾNG ANH 10 – GIỮA HỌC KÌ 1", STY["CoverSub"]))
    s.append(Spacer(1, 4))
    s.append(Paragraph("Năm học 2026 – 2027", STY["CoverSub"]))
    s.append(Spacer(1, 22))
    box = Table([[
        Paragraph("Bộ sách <b>Global Success</b> (Kết nối tri thức với cuộc sống)<br/>"
                  "Phạm vi: <b>Unit 1 – Unit 2 – Unit 3</b><br/>"
                  "Biên soạn theo <b>Ma trận &amp; Bản đặc tả</b> đề kiểm tra của trường",
                  STY["CoverBox"])]],
        colWidths=[11.6 * cm], hAlign="LEFT")
    box.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, -1), colors.HexColor("#0B4150")),
        ("LINEBEFORE", (0, 0), (0, -1), 3, ACCENT),
        ("LEFTPADDING", (0, 0), (-1, -1), 12),
        ("RIGHTPADDING", (0, 0), (-1, -1), 12),
        ("TOPPADDING", (0, 0), (-1, -1), 11),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 11),
    ]))
    s.append(box)
    s.append(Spacer(1, 26))
    s.append(Paragraph(
        "Gồm: phân tích ma trận đề · từ vựng 3 chủ điểm · 6 chuyên đề ngữ pháp · "
        "kỹ năng Nghe – Đọc – Viết · đề minh họa có đáp án chi tiết",
        ParagraphStyle("cs", parent=STY["CoverSub"], fontSize=8.6, leading=13,
                       textColor=colors.HexColor("#9DC6CE"))))
    return s


def toc_story(toc, pages):
    s = [PartBand("", "MỤC LỤC",
                  "Mỗi mục gắn dấu trang (bookmark) — dùng bảng điều hướng để nhảy nhanh"),
         Spacer(1, 8)]
    rows = [["NỘI DUNG", "TRANG"]]
    for idx, (lvl, text, _pg) in enumerate(toc):
        num = pages[idx] if pages else 0
        label = text if lvl == 2 else text
        prefix = "" if lvl == 2 else ""
        rows.append([f"{prefix}{label}", str(num) if num else ""])
    data = []
    for j, r in enumerate(rows):
        if j == 0:
            data.append([Paragraph(r[0], STY["TableHead"]),
                         Paragraph('<para align="right">TRANG</para>' if False else "TRANG", STY["TableHead"])])
        else:
            lvl = toc[j - 1][0]
            st = STY["TOC1"] if lvl == 2 else STY["TOC2"]
            data.append([Paragraph(inline(r[0]), st),
                         Paragraph(f'<para align="right">{r[1]}</para>',
                                   ParagraphStyle("p", parent=st, fontSize=8.8))])
    t = Table(data, colWidths=[PAGE_W - LM - RM - 2.0 * cm, 2.0 * cm],
              hAlign="LEFT", repeatRows=1)
    st = [
        ("BACKGROUND", (0, 0), (-1, 0), TEAL),
        ("VALIGN", (0, 0), (-1, -1), "TOP"),
        ("LINEBELOW", (0, 0), (-1, -2), 0.35, RULE),
        ("LINEBELOW", (0, 0), (-1, 0), 0.35, TEAL),
        ("TOPPADDING", (0, 0), (-1, -1), 0.8),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 0.8),
        ("LEFTPADDING", (0, 0), (-1, -1), 6),
        ("RIGHTPADDING", (0, 0), (-1, -1), 6),
    ]
    t.setStyle(TableStyle(st))
    s.append(t)
    return s


def make_body(sources):
    """Parse all sources as ONE document so part breaks stay consistent."""
    chunks = []
    for src in sources:
        with open(src, encoding="utf-8") as f:
            chunks.append(f.read().strip())
    return parse_markdown("\n\n".join(chunks), PAGE_W - LM - RM)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("sources", nargs="+")
    ap.add_argument("-o", "--out", required=True)
    args = ap.parse_args()

    sources = sorted(args.sources)
    body = make_body(sources)

    # pass 0 — discover headings and their pages (story built without a TOC)
    probe = Doc("/tmp/_probe.pdf")
    probe.build([NextPageTemplate("body"), PageBreak()] + copy.deepcopy(body))
    headings = list(probe.toc)
    pages = [0] * len(headings)

    # passes 1..n — paginate with real page numbers until the map is stable
    doc = probe
    for _ in range(6):
        doc = Doc(args.out)
        story = cover_story() + [NextPageTemplate("body"), PageBreak()]
        story += toc_story(headings, pages)
        story.append(PageBreak())
        story += copy.deepcopy(body)
        doc.build(story)
        new_pages = [p for _, _, p in doc.toc]
        if len(new_pages) == len(pages) and new_pages == pages:
            break
        pages = new_pages

    print(f"built {args.out}: {len(headings)} toc entries, {doc.page} pages")


if __name__ == "__main__":
    main()
