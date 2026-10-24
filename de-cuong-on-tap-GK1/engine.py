# -*- coding: utf-8 -*-
"""Mini PDF engine (reportlab) for the review-outline document.

DejaVu fonts are used so that Vietnamese diacritics render correctly.
"""
import re

from reportlab.lib.pagesizes import A4
from reportlab.lib.units import mm
from reportlab.lib import colors
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.enums import TA_LEFT, TA_CENTER, TA_JUSTIFY
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfbase.pdfmetrics import registerFontFamily
from reportlab.platypus import (BaseDocTemplate, Frame, PageTemplate, Paragraph,
                                Spacer, Table, TableStyle, PageBreak,
                                HRFlowable, KeepTogether, NextPageTemplate)

FONT_DIR = "/usr/share/fonts/truetype/dejavu"
pdfmetrics.registerFont(TTFont("DejaVu", FONT_DIR + "/DejaVuSans.ttf"))
pdfmetrics.registerFont(TTFont("DejaVu-Bold", FONT_DIR + "/DejaVuSans-Bold.ttf"))
pdfmetrics.registerFont(TTFont("DejaVuMono", FONT_DIR + "/DejaVuSansMono.ttf"))
pdfmetrics.registerFont(TTFont("DejaVuMono-Bold", FONT_DIR + "/DejaVuSansMono-Bold.ttf"))
# DejaVu oblique is not installed -> map <i> to the normal face; the md()
# helper renders *emphasis* as underline instead of italics.
registerFontFamily("DejaVu", normal="DejaVu", bold="DejaVu-Bold",
                   italic="DejaVu", boldItalic="DejaVu-Bold")

PRIMARY = colors.HexColor("#1B5E20")   # deep green
PRIMARY_L = colors.HexColor("#E8F5E9") # pale green
ACCENT = colors.HexColor("#0D47A1")    # blue
ACCENT_L = colors.HexColor("#E3F2FD")  # pale blue
ORANGE = colors.HexColor("#E65100")
ORANGE_L = colors.HexColor("#FFF3E0")
GREY = colors.HexColor("#5F6368")
LINE = colors.HexColor("#BDBDBD")
ROW_ALT = colors.HexColor("#F5F5F5")


def md(text):
    """Escape XML and apply a tiny inline markup:  **bold**, *underline*."""
    t = text.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")
    t = re.sub(r"\*\*(.+?)\*\*", r"<b>\1</b>", t)
    t = re.sub(r"\*(.+?)\*", r"<u>\1</u>", t)
    return t


class Doc(object):
    def __init__(self, path):
        self.path = path
        self.story = []
        self.styles = {}
        self._make_styles()

    # ---------------------------------------------------------------- styles
    def _make_styles(self):
        S = self.styles
        S["body"] = ParagraphStyle("body", fontName="DejaVu", fontSize=10,
                                   leading=14.5, alignment=TA_JUSTIFY,
                                   spaceAfter=4)
        S["bodyL"] = ParagraphStyle("bodyL", parent=S["body"], alignment=TA_LEFT)
        S["h2"] = ParagraphStyle("h2", fontName="DejaVu-Bold", fontSize=12.5,
                                 leading=16, textColor=PRIMARY,
                                 spaceBefore=12, spaceAfter=5)
        S["h3"] = ParagraphStyle("h3", fontName="DejaVu-Bold", fontSize=11,
                                 leading=14.5, textColor=ACCENT,
                                 spaceBefore=9, spaceAfter=4)
        S["h4"] = ParagraphStyle("h4", fontName="DejaVu-Bold", fontSize=10,
                                 leading=13.5, textColor=colors.black,
                                 spaceBefore=6, spaceAfter=3)
        S["bullet"] = ParagraphStyle("bullet", parent=S["bodyL"],
                                     leftIndent=14, bulletIndent=4,
                                     spaceAfter=2.5)
        S["cell"] = ParagraphStyle("cell", fontName="DejaVu", fontSize=8.8,
                                   leading=12, alignment=TA_LEFT)
        S["cellc"] = ParagraphStyle("cellc", parent=S["cell"], alignment=TA_CENTER)
        S["cellh"] = ParagraphStyle("cellh", parent=S["cell"],
                                    fontName="DejaVu-Bold",
                                    textColor=colors.white)
        S["cellhc"] = ParagraphStyle("cellhc", parent=S["cellh"], alignment=TA_CENTER)
        S["small"] = ParagraphStyle("small", fontName="DejaVu", fontSize=8.5,
                                    leading=11.5, textColor=GREY)
        S["center"] = ParagraphStyle("center", parent=S["bodyL"], alignment=TA_CENTER)
        S["title"] = ParagraphStyle("title", fontName="DejaVu-Bold", fontSize=20,
                                    leading=26, alignment=TA_CENTER,
                                    textColor=PRIMARY)
        S["subtitle"] = ParagraphStyle("subtitle", fontName="DejaVu-Bold",
                                       fontSize=13, leading=18,
                                       alignment=TA_CENTER, textColor=ACCENT)
        S["boxbody"] = ParagraphStyle("boxbody", fontName="DejaVu", fontSize=9.4,
                                      leading=13.5, alignment=TA_LEFT)

    # -------------------------------------------------------------- flowables
    def h1(self, text, part=False):
        """Section banner (level used by the TOC)."""
        tbl = Table([[Paragraph(md(text), ParagraphStyle(
            "h1", fontName="DejaVu-Bold", fontSize=13.5, leading=17,
            textColor=colors.white))]],
            colWidths=[170 * mm], rowHeights=None)
        tbl.setStyle(TableStyle([
            ("BACKGROUND", (0, 0), (-1, -1), PRIMARY if part else ACCENT),
            ("LEFTPADDING", (0, 0), (-1, -1), 8),
            ("TOPPADDING", (0, 0), (-1, -1), 5),
            ("BOTTOMPADDING", (0, 0), (-1, -1), 5),
        ]))
        # mark for TOC
        tbl._toc_level = 0
        tbl._toc_text = text
        self.story.append(Spacer(1, 8))
        self.story.append(tbl)
        self.story.append(Spacer(1, 6))

    def h2(self, text):
        p = Paragraph(md(text), self.styles["h2"])
        p._toc_level = 1
        p._toc_text = text
        self.story.append(p)

    def h3(self, text):
        self.story.append(Paragraph(md(text), self.styles["h3"]))

    def h4(self, text):
        self.story.append(Paragraph(md(text), self.styles["h4"]))

    def p(self, text, style="body"):
        self.story.append(Paragraph(md(text), self.styles[style]))

    def psmall(self, text):
        self.story.append(Paragraph(md(text), self.styles["small"]))

    def bullets(self, items, bullet="\u2022"):
        for it in items:
            self.story.append(Paragraph(md(it), self.styles["bullet"],
                                        bulletText=bullet))

    def numbered(self, items):
        for i, it in enumerate(items, 1):
            self.story.append(Paragraph(md(it), self.styles["bullet"],
                                        bulletText="%d." % i))

    def gap(self, h=6):
        self.story.append(Spacer(1, h))

    def rule(self):
        self.story.append(HRFlowable(width="100%", thickness=0.7,
                                     color=LINE, spaceBefore=4, spaceAfter=4))

    def pagebreak(self):
        self.story.append(PageBreak())

    def box(self, text, kind="tip", title=None):
        """Coloured callout box. kind: tip | note | warn | formula"""
        scheme = {
            "tip": (PRIMARY_L, PRIMARY),
            "note": (ACCENT_L, ACCENT),
            "warn": (ORANGE_L, ORANGE),
            "formula": (colors.HexColor("#F3E5F5"), colors.HexColor("#4A148C")),
        }[kind]
        flows = []
        if title:
            flows.append(Paragraph("<b>%s</b>" % md(title), ParagraphStyle(
                "boxt", fontName="DejaVu-Bold", fontSize=9.6, leading=13,
                textColor=scheme[1])))
        for line in text.split("\n"):
            if line.strip() == "":
                flows.append(Spacer(1, 3))
            else:
                flows.append(Paragraph(md(line), self.styles["boxbody"]))
        tbl = Table([[flows]], colWidths=[166 * mm])
        tbl.setStyle(TableStyle([
            ("BACKGROUND", (0, 0), (-1, -1), scheme[0]),
            ("LINEBEFORE", (0, 0), (0, -1), 2.5, scheme[1]),
            ("BOX", (0, 0), (-1, -1), 0.4, LINE),
            ("LEFTPADDING", (0, 0), (-1, -1), 8),
            ("RIGHTPADDING", (0, 0), (-1, -1), 8),
            ("TOPPADDING", (0, 0), (-1, -1), 5),
            ("BOTTOMPADDING", (0, 0), (-1, -1), 5),
        ]))
        self.story.append(Spacer(1, 3))
        self.story.append(KeepTogether([tbl, Spacer(1, 6)]))

    def table(self, header, rows, widths, align_center_cols=(), font=8.8):
        """header: list[str] or None. rows: list[list[str]]."""
        data = []
        if header:
            data.append([Paragraph("<b>%s</b>" % md(h), self.styles["cellhc"]
                                   if i in align_center_cols else self.styles["cellh"])
                         for i, h in enumerate(header)])
        for r in rows:
            line = []
            for i, c in enumerate(r):
                stl = self.styles["cellc"] if i in align_center_cols else self.styles["cell"]
                line.append(Paragraph(md(str(c)), stl))
            data.append(line)
        tbl = Table(data, colWidths=[w * mm for w in widths], repeatRows=1 if header else 0)
        style = [
            ("GRID", (0, 0), (-1, -1), 0.4, LINE),
            ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
            ("LEFTPADDING", (0, 0), (-1, -1), 4),
            ("RIGHTPADDING", (0, 0), (-1, -1), 4),
            ("TOPPADDING", (0, 0), (-1, -1), 3),
            ("BOTTOMPADDING", (0, 0), (-1, -1), 3),
        ]
        if header:
            style.append(("BACKGROUND", (0, 0), (-1, 0), PRIMARY))
        for ri in range(1, len(data)):
            if ri % 2 == 0:
                style.append(("BACKGROUND", (0, ri), (-1, ri), ROW_ALT))
        tbl.setStyle(TableStyle(style))
        self.story.append(tbl)
        self.story.append(Spacer(1, 6))

    def q(self, num, text):
        """Exam question line."""
        self.story.append(Paragraph(
            "<b>%s.</b>&nbsp; %s" % (num, md(text)),
            ParagraphStyle("q", fontName="DejaVu", fontSize=10, leading=14,
                           alignment=TA_LEFT, spaceBefore=4, spaceAfter=2)))

    def opts(self, options, per_row=2):
        """options: list of (letter, text)."""
        items = ["<b>%s.</b> %s" % (ltr, md(txt)) for ltr, txt in options]
        lines = []
        for i in range(0, len(items), per_row):
            chunk = items[i:i + per_row]
            joined = "&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;".join(chunk) if per_row > 1 else chunk[0]
            lines.append(joined)
        self.story.append(Paragraph(
            "<br/>".join(lines),
            ParagraphStyle("opt", fontName="DejaVu", fontSize=9.6, leading=14,
                           leftIndent=16, alignment=TA_LEFT, spaceAfter=2)))

    def answer_line(self, text):
        self.story.append(Paragraph(md(text), ParagraphStyle(
            "ans", fontName="DejaVu", fontSize=9.6, leading=13.5,
            textColor=colors.HexColor("#1B5E20"), spaceAfter=2)))

    # ------------------------------------------------------------------- save
    def save(self):
        doc = _DocTemplate(self.path, pagesize=A4,
                           leftMargin=20 * mm, rightMargin=20 * mm,
                           topMargin=18 * mm, bottomMargin=18 * mm,
                           title="Đề cương ôn tập GK1 - Tiếng Anh 10 (Global Success) 2026-2027",
                           author="Biên soạn theo Ma trận - Bảng đặc tả đề kiểm tra GK1")
        frame = Frame(doc.leftMargin, doc.bottomMargin, doc.width, doc.height,
                      id="normal")
        doc.addPageTemplates([
            PageTemplate(id="first", frames=[frame]),
            PageTemplate(id="later", frames=[frame], onPage=_footer),
        ])
        self.story.insert(0, NextPageTemplate("later"))
        doc.multiBuild(self.story)


class _DocTemplate(BaseDocTemplate):
    def afterFlowable(self, flowable):
        """Feed the (optional) table of contents."""
        lvl = getattr(flowable, "_toc_level", None)
        if lvl is not None:
            text = getattr(flowable, "_toc_text", "")
            self.notify("TOCEntry", (lvl, text, self.page))


def _footer(canv, doc):
    canv.saveState()
    canv.setFont("DejaVu", 7.5)
    canv.setFillColor(GREY)
    canv.drawString(20 * mm, 11 * mm,
                    "Đề cương ôn tập GK1 - Tiếng Anh 10 (Global Success) | Năm học 2026-2027")
    canv.drawRightString(190 * mm, 11 * mm, "Trang %d" % doc.page)
    canv.setStrokeColor(LINE)
    canv.setLineWidth(0.4)
    canv.line(20 * mm, 14 * mm, 190 * mm, 14 * mm)
    canv.restoreState()
