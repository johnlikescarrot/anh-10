"""Cover page flowables for the GK1 review PDF."""
from reportlab.lib import colors
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.units import mm
from reportlab.platypus import Paragraph, Spacer, Table, TableStyle

from build_pdf import CW, NAVY, BLUE, LIGHT, GREY, GREEN_B, GREEN_D, AMBER_B, AMBER_D, esc


def cover_flowables():
    st_t = ParagraphStyle('ct', fontName='DVS-B', fontSize=24, leading=31,
                          alignment=1, textColor=NAVY)
    st_s = ParagraphStyle('cs', fontName='DVS-B', fontSize=14, leading=20,
                          alignment=1, textColor=BLUE)
    st_x = ParagraphStyle('cx', fontName='DVS', fontSize=10.2, leading=15.4,
                          alignment=1, textColor=GREY)
    st_b = ParagraphStyle('cb', fontName='DVS-B', fontSize=11.5, leading=16,
                          alignment=1, textColor=colors.white)

    out = []
    out.append(Spacer(1, 14 * mm))
    band = Table([[Paragraph('ĐỀ CƯƠNG ÔN TẬP GIỮA KÌ 1 – NĂM HỌC 2026–2027', st_b)]],
                 colWidths=[CW])
    band.setStyle(TableStyle([('BACKGROUND', (0, 0), (-1, -1), NAVY),
                              ('TOPPADDING', (0, 0), (-1, -1), 9),
                              ('BOTTOMPADDING', (0, 0), (-1, -1), 9)]))
    out.append(band)
    out.append(Spacer(1, 8 * mm))
    out.append(Paragraph('MÔN TIẾNG ANH 10', st_t))
    out.append(Spacer(1, 2 * mm))
    out.append(Paragraph('Chương trình GLOBAL SUCCESS – Units 1 · 2 · 3', st_s))
    out.append(Spacer(1, 1.5 * mm))
    out.append(Paragraph('Family life · Humans and the Environment · Music', st_x))
    out.append(Spacer(1, 7 * mm))

    sub = [
        ['Biên soạn bám sát <b>MA TRẬN &amp; BẢNG ĐẶC TẢ KỸ THUẬT ĐỀ KIỂM TRA GIỮA KÌ 1</b>'],
        ['Nguồn: <b>2026_2027_MA TRẬN 10_GK1.docx</b> (ma trận do nhà trường công bố)'],
        ['Cấu trúc đề: <b>28 câu trắc nghiệm (7,0 điểm)</b> + <b>Phần tự luận (3,0 điểm)</b>: 6 câu + 1 bài viết đoạn văn 120–150 từ'],
    ]
    t = Table([[Paragraph(esc(r[0]), ParagraphStyle('su', fontName='DVS', fontSize=10,
                                                     leading=14.5, alignment=1))] for r in sub],
              colWidths=[CW * 0.96])
    t.setStyle(TableStyle([('BACKGROUND', (0, 0), (-1, -1), LIGHT),
                           ('BOX', (0, 0), (-1, -1), 0.6, NAVY),
                           ('TOPPADDING', (0, 0), (-1, -1), 4),
                           ('BOTTOMPADDING', (0, 0), (-1, -1), 4)]))
    out.append(t)
    out.append(Spacer(1, 8 * mm))

    inc = [
        ['PHẦN 1', 'Phân tích chi tiết cấu trúc đề thi – chiến thuật làm bài &amp; phân bổ thời gian'],
        ['PHẦN 2', 'Từ vựng 3 chủ đề theo bảng từ SGK – 36 cụm hay thi – 35 từ nền cho đoạn văn'],
        ['PHẦN 3', 'Ngữ pháp: 5 chuyên đề – công thức, ví dụ, lỗi sai, mẹo nhớ, Quick check'],
        ['PHẦN 4', 'Kỹ năng: Listening · cloze-text · đọc hiểu · viết lại câu · đoạn văn 120–150 từ'],
        ['PHẦN 5', 'ĐỀ ÔN LUYỆN SỐ 1 – sát định dạng ma trận (28 TN + 6 TL + 1 bài viết)'],
        ['PHẦN 6', 'ĐỀ ÔN LUYỆN SỐ 2 – sát định dạng ma trận (28 TN + 6 TL + 1 bài viết)'],
        ['PHẦN 7', 'ĐÁP ÁN – GIẢI THÍCH – FULL TAPESCRIPT – PHIẾU CHẤM ĐOẠN VĂN'],
        ['PHẦN 8', 'BẢNG TRA NHANH “Trước khi thi – đọc 10 phút”'],
    ]
    cells = []
    for a, b in inc:
        cells.append([Paragraph(esc(a), ParagraphStyle('ia', fontName='DVS-B', fontSize=9.4,
                                                       textColor=NAVY)),
                      Paragraph(esc(b), ParagraphStyle('ib', fontName='DVS', fontSize=9.4,
                                                        leading=12.8))])
    t = Table(cells, colWidths=[CW * 0.13, CW * 0.87])
    t.setStyle(TableStyle([
        ('BOX', (0, 0), (-1, -1), 0.6, NAVY),
        ('LINEBELOW', (0, 0), (-1, -2), 0.35, colors.HexColor('#C9D4E6')),
        ('ROWBACKGROUNDS', (0, 0), (-1, -1), [colors.white, colors.HexColor('#F4F7FC')]),
        ('TOPPADDING', (0, 0), (-1, -1), 5.5),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 5.5),
        ('LEFTPADDING', (0, 0), (-1, -1), 8),
        ('RIGHTPADDING', (0, 0), (-1, -1), 8),
        ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
    ]))
    out.append(t)
    out.append(Spacer(1, 8 * mm))

    note = ('Cách dùng tài liệu: (1) Đọc Phần 1 để biết đề thi gồm những gì; '
            '(2) Học từ vựng – ngữ pháp theo từng chuyên đề, làm Quick Check ngay sau mỗi bài; '
            '(3) Đọc kỹ kỹ năng từng phần; (4) Bấm giờ làm lần lượt Đề số 1, Đề số 2 như thi thật; '
            '(5) Chấm bằng đáp án, đọc phần giải thích, chép lại những câu sai vào “sổ tay lỗi”; '
            '(6) Trước khi thi xem lại Bảng tra nhanh (Phần 8).')
    t = Table([[Paragraph(esc(note), ParagraphStyle('nb', fontName='DVS', fontSize=9.2,
                                                     leading=13.4, alignment=0))]],
              colWidths=[CW])
    t.setStyle(TableStyle([('BACKGROUND', (0, 0), (-1, -1), GREEN_B),
                           ('LINEBEFORE', (0, 0), (0, -1), 3, GREEN_D),
                           ('BOX', (0, 0), (-1, -1), 0.4, GREEN_D),
                           ('TOPPADDING', (0, 0), (-1, -1), 7),
                           ('BOTTOMPADDING', (0, 0), (-1, -1), 7),
                           ('LEFTPADDING', (0, 0), (-1, -1), 9),
                           ('RIGHTPADDING', (0, 0), (-1, -1), 9)]))
    out.append(t)
    out.append(Spacer(1, 6 * mm))
    out.append(Paragraph('Tài liệu ôn tập nội bộ – biên soạn tự động từ ma trận đề thi của nhà trường, '
                         'giáo viên và học sinh có thể chỉnh sửa, bổ sung.', st_x))
    out.append(Spacer(1, 4 * mm))
    return out
