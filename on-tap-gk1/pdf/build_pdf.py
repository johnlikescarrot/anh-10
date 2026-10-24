#!/usr/bin/env python3
"""
Build "Đề cương ôn tập GK1 – Tiếng Anh 10 – Năm học 2026-2027" (PDF).

Renders a small tuple-DSL defined in content_*.py modules via ReportLab.
Block types:
  ("h1", text)          section heading (forces a new page)
  ("h1nb", text)        section heading without page break
  ("h2", text) ("h3", text)
  ("p", text)           body paragraph (inline <b>, <font> allowed)
  ("small", text)       small grey paragraph
  ("lead", text)        intro paragraph, justified
  ("bullets", [..])     bullet list   ("numbers", [..]) numbered list
  ("table", {"header":[..], "rows":[[..],..], "widths":[..], "fs":8.5,
             "center":[col idx..], "zebra":True, "rowcolors":[hex..]})
  ("box", kind, [lines])  kind: tip | warn | note | task | pass | script
  ("qblock", [lines])     exam question blocks with hanging indent
  ("pb",)                 page break
  ("spacer", pt)
"""
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
from reportlab.pdfbase.pdfmetrics import registerFontFamily
from reportlab.platypus import (BaseDocTemplate, Frame, KeepTogether, PageBreak,
                                Paragraph, Spacer, Table, TableStyle)

HERE = os.path.dirname(os.path.abspath(__file__))
DEJA = '/usr/share/fonts/truetype/dejavu'
pdfmetrics.registerFont(TTFont('DVS', os.path.join(DEJA, 'DejaVuSans.ttf')))
pdfmetrics.registerFont(TTFont('DVS-B', os.path.join(DEJA, 'DejaVuSans-Bold.ttf')))
registerFontFamily('DVS', normal='DVS', bold='DVS-B', italic='DVS', boldItalic='DVS-B')

# palette
NAVY = colors.HexColor('#1F3864')
BLUE = colors.HexColor('#2E5FA3')
LIGHT = colors.HexColor('#EAF0F8')
GREEN_D = colors.HexColor('#1E6B4F')
GREEN_B = colors.HexColor('#E4F3EC')
RED_D = colors.HexColor('#A63A2E')
RED_B = colors.HexColor('#FBEAE7')
AMBER_D = colors.HexColor('#8A6100')
AMBER_B = colors.HexColor('#FFF6DD')
GREY = colors.HexColor('#5A5A5A')
RULE = colors.HexColor('#C9D4E6')
PAGE_W, PAGE_H = A4
MARGIN = 16 * mm
CW = PAGE_W - 2 * MARGIN  # content width in points

ENT_RE = re.compile(r'&(?!(?:amp|lt|gt|quot|apos|nbsp|#\d+|#x[0-9a-fA-F]+);)')


def esc(s):
    return ENT_RE.sub('&amp;', s)


def styles():
    d = {}
    base = dict(fontName='DVS', fontSize=9.4, leading=13.6, spaceAfter=4,
                textColor=colors.black, alignment=TA_JUSTIFY)
    d['p'] = ParagraphStyle('p', **base)
    d['lead'] = ParagraphStyle('lead', **{**base, 'fontSize': 10, 'leading': 14.6,
                                          'spaceAfter': 6})
    d['small'] = ParagraphStyle('small', **{**base, 'fontSize': 8, 'leading': 11,
                                            'textColor': GREY, 'alignment': TA_LEFT})
    d['h1'] = ParagraphStyle('h1', fontName='DVS-B', fontSize=14.5, leading=19,
                             textColor=colors.white, backColor=NAVY,
                             borderPadding=(5, 6, 5, 6), leftIndent=0,
                             spaceBefore=0, spaceAfter=9)
    d['h2'] = ParagraphStyle('h2', fontName='DVS-B', fontSize=11.6, leading=15.6,
                             textColor=NAVY, spaceBefore=8, spaceAfter=4,
                             borderPadding=(0, 0, 1, 0))
    d['h3'] = ParagraphStyle('h3', fontName='DVS-B', fontSize=9.8, leading=13.4,
                             textColor=BLUE, spaceBefore=5, spaceAfter=3)
    d['li'] = ParagraphStyle('li', **{**base, 'alignment': TA_LEFT, 'leftIndent': 7 * mm,
                                      'bulletIndent': 1 * mm, 'spaceAfter': 2.5,
                                      'firstLineIndent': -3 * mm})
    d['cell'] = ParagraphStyle('cell', fontName='DVS', fontSize=8.4, leading=11.6,
                               spaceAfter=0, alignment=TA_LEFT)
    d['cellc'] = ParagraphStyle('cellc', d['cell'], alignment=TA_CENTER)
    d['cellh'] = ParagraphStyle('cellh', d['cell'], fontName='DVS-B',
                                textColor=colors.white, alignment=TA_CENTER)
    d['q'] = ParagraphStyle('q', **{**base, 'alignment': TA_LEFT, 'fontSize': 9.4,
                                    'leading': 13.8, 'leftIndent': 4 * mm,
                                    'firstLineIndent': -4 * mm, 'spaceAfter': 5})
    d['boxtitle'] = ParagraphStyle('boxtitle', fontName='DVS-B', fontSize=9.6,
                                   leading=13, spaceAfter=2)
    d['boxbody'] = ParagraphStyle('boxbody', fontName='DVS', fontSize=9.2,
                                  leading=13.4, alignment=TA_JUSTIFY, spaceAfter=0)
    d['passage'] = ParagraphStyle('passage', fontName='DVS', fontSize=9.5,
                                  leading=14.5, alignment=TA_JUSTIFY, spaceAfter=0)
    d['cover_t'] = ParagraphStyle('cover_t', fontName='DVS-B', fontSize=25, leading=32,
                                  alignment=TA_CENTER, textColor=NAVY)
    d['cover_s'] = ParagraphStyle('cover_s', fontName='DVS-B', fontSize=14.5,
                                  leading=20, alignment=TA_CENTER, textColor=BLUE)
    d['cover_x'] = ParagraphStyle('cover_x', fontName='DVS', fontSize=10, leading=15,
                                  alignment=TA_CENTER, textColor=GREY)
    return d


S = styles()

BOX_STYLES = {
    'tip': (AMBER_B, AMBER_D),
    'warn': (RED_B, RED_D),
    'note': (LIGHT, NAVY),
    'task': (GREEN_B, GREEN_D),
}
BOX_TITLES = {'tip': 'MẸO GHI NHỚ', 'warn': '⚠ LỖI SAI THƯỜNG GẶP',
              'note': 'GHI CHÚ', 'task': 'BÀI TẬP NHANH'}


def para(text, style='p'):
    return Paragraph(esc(text), S[style])


def render_table(spec):
    header = spec.get('header')
    rows = spec['rows']
    fs = spec.get('fs', 8.4)
    widths = spec.get('widths')
    ncol = len(header) if header else len(rows[0])
    if not widths:
        widths = [1.0] * ncol
    tot = float(sum(widths))
    cwid = [CW * w / tot for w in widths]
    data = []
    if header:
        data.append([Paragraph(esc(str(h)), ParagraphStyle('ch', parent=S['cellh'],
                                                            fontSize=fs)) for h in header])
    center_cols = set(spec.get('center', []))
    for r in rows:
        row = []
        for i, c in enumerate(r):
            st = ParagraphStyle('cc', parent=S['cell'], fontSize=fs, leading=fs + 3.2)
            if i in center_cols:
                st = ParagraphStyle('cc2', parent=S['cellc'], fontSize=fs, leading=fs + 3.2)
            if isinstance(c, str):
                row.append(Paragraph(esc(c), st))
            else:
                row.append(c)
        data.append(row)
    t = Table(data, colWidths=cwid, repeatRows=1 if header else 0)
    style_cmds = [
        ('GRID', (0, 0), (-1, -1), 0.4, RULE),
        ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
        ('TOPPADDING', (0, 0), (-1, -1), 2.6),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 2.6),
        ('LEFTPADDING', (0, 0), (-1, -1), 4),
        ('RIGHTPADDING', (0, 0), (-1, -1), 4),
    ]
    if header:
        style_cmds.append(('BACKGROUND', (0, 0), (-1, 0), NAVY))
    if spec.get('zebra', True) and header:
        for ri in range(1, len(data)):
            if ri % 2 == 0:
                style_cmds.append(('BACKGROUND', (0, ri), (-1, ri),
                                   colors.HexColor('#F4F7FC')))
    for rc in spec.get('rowcolors', []):
        style_cmds.append(('BACKGROUND', (0, rc[0]), (-1, rc[0]),
                           colors.HexColor(rc[1])))
    t.setStyle(TableStyle(style_cmds))
    return t


def render_box(kind, lines, title=None):
    bg, accent = BOX_STYLES[kind]
    inner = []
    head = title or BOX_TITLES.get(kind, '')
    if head:
        inner.append([Paragraph(esc(head), ParagraphStyle('bt', parent=S['boxtitle'],
                                                           textColor=accent))])
    body = '<br/>'.join(esc(l) for l in lines)
    inner.append([Paragraph(body, S['boxbody'])])
    t = Table(inner, colWidths=[CW])
    t.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, -1), bg),
        ('LINEBEFORE', (0, 0), (0, -1), 3, accent),
        ('BOX', (0, 0), (-1, -1), 0.4, accent),
        ('TOPPADDING', (0, 0), (-1, 0), 5),
        ('BOTTOMPADDING', (0, -1), (-1, -1), 5),
        ('LEFTPADDING', (0, 0), (-1, -1), 8),
        ('RIGHTPADDING', (0, 0), (-1, -1), 7),
    ]))
    return t


def render_passage(lines, title=None, tone='passage'):
    bg = colors.HexColor('#F6F4EC')
    bord = colors.HexColor('#C7BFA3')
    inner = []
    if title:
        inner.append([Paragraph(esc(title), ParagraphStyle(
            'pt', parent=S['boxtitle'], textColor=GREY, alignment=TA_CENTER))])
    body = '<br/><br/>'.join(esc(l) for l in lines)
    st = ParagraphStyle(tone, parent=S['passage'],
                        fontSize=9.3, leading=14.2)
    inner.append([Paragraph(body, st)])
    t = Table(inner, colWidths=[CW])
    t.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, -1), bg),
        ('BOX', (0, 0), (-1, -1), 0.8, bord),
        ('TOPPADDING', (0, 0), (-1, 0), 6),
        ('BOTTOMPADDING', (0, -1), (-1, -1), 6),
        ('LEFTPADDING', (0, 0), (-1, -1), 9),
        ('RIGHTPADDING', (0, 0), (-1, -1), 9),
    ]))
    return t


def bullets_block(items, number=False):
    out = []
    for i, it in enumerate(items):
        mark = f'{i + 1}.' if number else '•'
        out.append(Paragraph(esc(it), S['li'], bulletText=mark))
    return out


def qblock(items):
    out = []
    for it in items:
        out.append(Paragraph(esc(it), S['q']))
    return out


def render_blocks(blocks, story):
    for b in blocks:
        kind = b[0]
        if kind == 'h1':
            story.append(PageBreak())
            story.append(Paragraph(esc(b[1]), S['h1']))
        elif kind == 'h1nb':
            story.append(Paragraph(esc(b[1]), S['h1']))
        elif kind == 'h2':
            story.append(Paragraph(esc(b[1]), S['h2']))
        elif kind == 'h3':
            story.append(Paragraph(esc(b[1]), S['h3']))
        elif kind == 'p':
            story.append(para(b[1]))
        elif kind == 'lead':
            story.append(para(b[1], 'lead'))
        elif kind == 'small':
            story.append(para(b[1], 'small'))
        elif kind == 'table':
            story.append(Spacer(1, 2))
            story.append(render_table(b[1]))
            story.append(Spacer(1, 4))
        elif kind == 'box':
            extra = b[3] if len(b) > 3 else None
            story.append(Spacer(1, 2))
            story.append(render_box(b[1], b[2], extra))
            story.append(Spacer(1, 4))
        elif kind == 'passage':
            extra = b[2] if len(b) > 2 else None
            story.append(Spacer(1, 2))
            story.append(render_passage(b[1], extra))
            story.append(Spacer(1, 4))
        elif kind == 'bullets':
            story.extend(bullets_block(b[1]))
            story.append(Spacer(1, 2))
        elif kind == 'numbers':
            story.extend(bullets_block(b[1], number=True))
            story.append(Spacer(1, 2))
        elif kind == 'qblock':
            story.extend(qblock(b[1]))
            story.append(Spacer(1, 2))
        elif kind == 'keep':
            inner = []
            render_blocks(b[1], inner)
            story.append(KeepTogether(inner))
        elif kind == 'pb':
            story.append(PageBreak())
        elif kind == 'spacer':
            story.append(Spacer(1, b[1]))
        else:
            raise ValueError(f'unknown block: {kind}')


def footer(canvas, doc, cover=False):
    canvas.saveState()
    if not cover:
        canvas.setStrokeColor(RULE)
        canvas.setLineWidth(0.5)
        canvas.line(MARGIN, 11 * mm, PAGE_W - MARGIN, 11 * mm)
        canvas.setFont('DVS', 7.2)
        canvas.setFillColor(GREY)
        canvas.drawString(MARGIN, 7.6 * mm,
                          'ĐỀ CƯƠNG ÔN TẬP GK1 • TIẾNG ANH 10 • NĂM HỌC 2026–2027 • Global Success (Units 1–3)')
        canvas.drawRightString(PAGE_W - MARGIN, 7.6 * mm, f'Trang {doc.page}')
    canvas.restoreState()


def build(out_path, all_blocks, cover_blocks):
    doc = BaseDocTemplate(out_path, pagesize=A4,
                          leftMargin=MARGIN, rightMargin=MARGIN,
                          topMargin=14 * mm, bottomMargin=16 * mm,
                          title='Đề cương ôn tập GK1 Tiếng Anh 10 – Năm học 2026-2027',
                          author='Arena Agent', subject='ON TAP GK1 TIENG ANH 10')
    frame = Frame(MARGIN, 16 * mm, PAGE_W - 2 * MARGIN, PAGE_H - 14 * mm - 16 * mm,
                  id='main', showBoundary=0,
                  leftPadding=0, rightPadding=0, topPadding=0, bottomPadding=0)
    from reportlab.platypus import PageTemplate
    page_t = PageTemplate(id='body', frames=[frame], onPage=lambda c, d: footer(c, d))
    doc.addPageTemplates([page_t])
    story = []
    story.extend(cover_blocks)
    render_blocks(all_blocks, story)
    doc.build(story)
    return out_path


def main():
    sys.path.insert(0, HERE)
    import content_front
    import content_grammar
    import content_skills
    import content_test1
    import content_test2
    import content_keys
    from cover import cover_flowables
    all_blocks = (content_front.BLOCKS + content_grammar.BLOCKS + content_skills.BLOCKS
                  + content_test1.BLOCKS + content_test2.BLOCKS + content_keys.BLOCKS)
    out = sys.argv[1] if len(sys.argv) > 1 else \
        os.path.join(HERE, '..', 'DE_CUONG_ON_TAP_GK1_TIENG_ANH_10_2026-2027.pdf')
    build(out, all_blocks, cover_flowables())
    print('PDF written to', os.path.normpath(out))


if __name__ == '__main__':
    main()
