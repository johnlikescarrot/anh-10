# -*- coding: utf-8 -*-
"""Build the final PDF: Đề cương ôn tập GK1 Tiếng Anh 10 (2026-2027)."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import (BaseDocTemplate, PageTemplate, Frame,
                                PageBreak, NextPageTemplate, Paragraph, Spacer, Table, TableStyle)
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import mm
from reportlab.lib import colors

FONT_DIR = "/usr/share/fonts/truetype/dejavu"
pdfmetrics.registerFont(TTFont("DV", f"{FONT_DIR}/DejaVuSans.ttf"))
pdfmetrics.registerFont(TTFont("DVB", f"{FONT_DIR}/DejaVuSans-Bold.ttf"))
pdfmetrics.registerFontFamily("DV", normal="DV", bold="DVB", italic="DV", boldItalic="DVB")

from common import S, P, band, box, table, spacer, bullet, NAVY, TEAL, ORANGE, LIGHT, W
import part0_analysis, part1_vocab, part2_grammar, part3_skills
import part4_drills1, part4_drills2, part5_mock, part6_key, part7_key_mock

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..",
                   "De-cuong-on-tap-GK1-Tieng-Anh-10-2026-2027.pdf")
OUT = os.path.normpath(OUT)
PAGE_W, PAGE_H = A4

def footer(canvas, doc):
    canvas.saveState()
    if doc.page > 1:
        canvas.setFont("DV", 7.5)
        canvas.setFillColor(colors.HexColor("#6b7a90"))
        canvas.drawString(17*mm, 12*mm, "Đề cương ôn tập giữa học kỳ 1 • Tiếng Anh 10 (Global Success) • Năm học 2026–2027")
        canvas.drawRightString(PAGE_W - 17*mm, 12*mm, f"Trang {doc.page}")
        canvas.setStrokeColor(colors.HexColor("#C9D4E4")); canvas.setLineWidth(0.5)
        canvas.line(17*mm, 14.5*mm, PAGE_W - 17*mm, 14.5*mm)
    canvas.restoreState()

def cover():
    f = []
    f.append(Spacer(1, 26*mm))
    title_style = lambda **kw: kw
    from reportlab.lib.styles import ParagraphStyle
    t1 = ParagraphStyle("ct1", fontName="DVB", fontSize=27, leading=33, textColor=NAVY, alignment=1)
    t2 = ParagraphStyle("ct2", fontName="DVB", fontSize=15, leading=21, textColor=TEAL, alignment=1)
    t3 = ParagraphStyle("ct3", fontName="DV", fontSize=11.5, leading=17, textColor=colors.HexColor("#333333"), alignment=1)
    cover_tbl = Table([
        [Paragraph("ĐỀ CƯƠNG ÔN TẬP", t1)],
        [Paragraph("KIỂM TRA GIỮA HỌC KỲ 1", t1)],
        [Paragraph("MÔN: TIẾNG ANH — LỚP 10", t2)],
        [Spacer(1, 4*mm)],
        [Paragraph("Bám sát Ma trận & Bảng đặc tả đề kiểm tra năm học <b>2026–2027</b><br/>Sách giáo khoa: <b>Global Success 10</b> (Units 1–2–3)", t3)],
    ], colWidths=[W])
    cover_tbl.setStyle(TableStyle([
        ("BACKGROUND", (0,0), (-1,-1), LIGHT),
        ("BOX", (0,0), (-1,-1), 1.2, NAVY),
        ("TOPPADDING", (0,0), (-1,-1), 5), ("BOTTOMPADDING", (0,0), (-1,-1), 5),
        ("LEFTPADDING", (0,0), (-1,-1), 14), ("RIGHTPADDING", (0,0), (-1,-1), 14),
        ("ROUNDEDCORNERS", [6,6,6,6]),
    ]))
    f.append(cover_tbl)
    f.append(Spacer(1, 10*mm))
    f.append(table([
        ["Cấu trúc tài liệu", "Nội dung"],
        ["PHẦN 0", "Phân tích chuyên sâu ma trận: cấu trúc đề, mức độ nhận thức, chiến lược theo mục tiêu điểm"],
        ["PHẦN I", "Kiến thức trọng tâm: 60 từ vựng cốt lõi Units 1–3 • 5 chủ điểm ngữ pháp • kỹ năng từng dạng bài & khung viết đoạn văn"],
        ["PHẦN II", "126 câu luyện tập mọi dạng bài: từ vựng • ngữ pháp • dạng từ • nghe (có transcript) • đọc • sắp xếp câu • viết lại câu"],
        ["PHẦN III", "Đề thi thử số 1 — mô phỏng đúng 100% ma trận (28 câu TN + 6 câu TL + 1 bài viết, 10 điểm)"],
        ["PHẦN IV", "Đáp án & giải thích chi tiết cho mọi câu hỏi, transcript bài nghe, 3 bài văn mẫu"],
        ["PHỤ LỤC", "Bảng V3 bất quy tắc • Checklist trước khi thi • Nhật ký lỗi sai • Bảng theo dõi tiến bộ"],
    ], [32*mm, W-32*mm]))
    f.append(Spacer(1, 10*mm))
    f.append(box("DÀNH CHO AI?",
                 ["Học sinh lớp 10 học theo sách <i>Global Success</i> chuẩn bị cho kỳ kiểm tra giữa học kỳ 1 năm học 2026–2027; "
                  "giáo viên và phụ huynh cũng có thể dùng tài liệu này để đồng hành, kiểm tra và chấm bài cho các em tại nhà."],
                 bg=colors.white, border=TEAL))
    f.append(Spacer(1, 14*mm))
    f.append(P("Biên soạn dựa trên tệp: <i>2026_2027_MA TRẬN 10_GK1.docx</i> — Ma trận & Bảng đặc tả đề kiểm tra giữa kỳ 1, Tiếng Anh 10, năm học 2026–2027.", "c"))
    f.append(P("Chúc các em ôn tập hiệu quả và đạt kết quả cao!", "c"))
    return f

def toc():
    f = [band("MỤC LỤC", TEAL), spacer(6)]
    items = [
        ("Hướng dẫn sử dụng tài liệu & Lộ trình ôn tập 7 ngày", ""),
        ("PHẦN 0 — Phân tích chuyên sâu ma trận đề thi", "0.1 Cấu trúc tổng thể • 0.2 Mức độ nhận thức • 0.3 Phạm vi kiến thức • 0.4 Chiến lược theo mục tiêu điểm"),
        ("PHẦN I — Hệ thống kiến thức trọng tâm", ""),
        ("&nbsp;&nbsp;Chương 1: Từ vựng Units 1–3", "Family life • Humans and the environment • Music • Gia đình từ"),
        ("&nbsp;&nbsp;Chương 2: Năm chủ điểm ngữ pháp", "HT đơn/tiếp diễn • will/be going to • Bị động • Câu ghép • to-inf/bare inf • Bảng tổng hợp 1 trang"),
        ("&nbsp;&nbsp;Chương 3: Kỹ năng làm bài & khung viết", "Listening • Reading cloze/comprehension • Re-ordering • Transformation • Đoạn văn 120–150 từ"),
        ("PHẦN II — Luyện tập theo dạng bài", "A. Vocabulary (30) • B. Grammar (38) • C. Word form (10) • D. Listening (10) • E–F. Reading (20) • G. Re-ordering (6) • H. Transformation (12)"),
        ("PHẦN III — Đề thi thử số 1 (bám sát ma trận)", "Listening 10 • Language 8 • Reading 10 • Writing 7 — tổng 10 điểm"),
        ("PHẦN IV — Đáp án, giải thích, transcript & bài mẫu", "Đáp án Phần II • Transcript bài nghe • Đáp án đề thi thử • 3 bài văn mẫu"),
        ("PHỤ LỤC", "Bảng V3 • Checklist • Nhật ký lỗi sai • Theo dõi tiến bộ"),
    ]
    for title, desc in items:
        f.append(P(f"<b>{title}</b>", "p"))
        if desc:
            f.append(P(desc, "small"))
    f.append(spacer(4))
    f.append(P("<i>Ghi chú: số trang cụ thể xem ở góc dưới mỗi trang của tài liệu. Hãy đánh dấu (bookmark) các trang chứa "
               "“Bảng tổng hợp ngữ pháp 1 trang” (mục 2.6) và “Ngân hàng từ nối” (mục 3.6) — hai trang nên xem lại ngay trước giờ thi.</i>", "small"))
    return f

def main():
    doc = BaseDocTemplate(OUT, pagesize=A4,
                          leftMargin=17*mm, rightMargin=17*mm,
                          topMargin=16*mm, bottomMargin=16*mm,
                          title="Đề cương ôn tập giữa học kỳ 1 Tiếng Anh 10 (Global Success) 2026-2027",
                          author="Biên soạn theo Ma trận GK1 Tiếng Anh 10 năm học 2026-2027")
    frame = Frame(doc.leftMargin, doc.bottomMargin, doc.width, doc.height, id="main")
    doc.addPageTemplates([PageTemplate(id="all", frames=[frame], onPage=footer)])

    story = []
    story += cover()
    story.append(PageBreak())
    story += toc()
    story.append(PageBreak())
    story += part0_analysis.build()
    story.append(PageBreak())
    story += part1_vocab.build()
    story += part2_grammar.build()
    story.append(PageBreak())
    story += part3_skills.build()
    story.append(PageBreak())
    story += part4_drills1.build()
    story += part4_drills2.build()
    story.append(PageBreak())
    story += part5_mock.build()
    story.append(PageBreak())
    story += part6_key.build()
    story += part7_key_mock.build()

    doc.build(story)
    print("BUILT:", OUT, os.path.getsize(OUT), "bytes")

if __name__ == "__main__":
    main()
