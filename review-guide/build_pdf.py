# -*- coding: utf-8 -*-
"""
Build: Đề cương ôn tập Tiếng Anh 10 - Kiểm tra giữa kỳ 1 (2026-2027)
Nội dung phân tích từ file: 2026_2027_MA TRẬN 10_GK1.docx
(Mã 기술: ma trận & bảng đặc tả kỹ thuật đề kiểm tra giữa kỳ 1, môn Tiếng Anh 10, Global Success)
"""
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import mm
from reportlab.lib import colors
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.enums import TA_CENTER, TA_LEFT, TA_JUSTIFY
from reportlab.platypus import (
    BaseDocTemplate, Frame, PageTemplate, Paragraph, Spacer, Table,
    TableStyle, KeepTogether, HRFlowable, ListFlowable, ListItem
)
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
import os

# ----------------------------------------------------------------------------
# Fonts (Vietnamese-capable: DejaVu Sans)
# ----------------------------------------------------------------------------
FONT_DIR = "/usr/share/fonts/truetype/dejavu"
def reg(name, fname):
    path = os.path.join(FONT_DIR, fname)
    if os.path.exists(path):
        pdfmetrics.registerFont(TTFont(name, path))
        return True
    return False

reg("DVS", "DejaVuSans.ttf")
reg("DVS-B", "DejaVuSans-Bold.ttf")
# No oblique/bold-oblique on this system; fall back to regular/bold.
reg("DVS-I", "DejaVuSans.ttf")
reg("DVS-BI", "DejaVuSans-Bold.ttf")

# ----------------------------------------------------------------------------
# Palette
# ----------------------------------------------------------------------------
NAVY   = colors.HexColor("#1F3A5F")
BLUE   = colors.HexColor("#2E6DA4")
LIGHT  = colors.HexColor("#EAF1F8")
LIGHT2 = colors.HexColor("#F5F8FB")
ACCENT = colors.HexColor("#C0392B")
GREEN  = colors.HexColor("#1E8449")
GREY   = colors.HexColor("#556B7F")
LINE   = colors.HexColor("#B9C9D8")

# ----------------------------------------------------------------------------
# Styles
# ----------------------------------------------------------------------------
def st(name, **kw):
    base = dict(fontName="DVS", fontSize=9.5, leading=13.5, textColor=colors.black,
                alignment=TA_JUSTIFY, spaceAfter=4)
    base.update(kw)
    return ParagraphStyle(name, **base)

S_TITLE   = st("title",  fontName="DVS-B", fontSize=21, leading=26, textColor=NAVY,
               alignment=TA_CENTER, spaceAfter=2)
S_SUB     = st("sub",    fontName="DVS-B", fontSize=12.5, leading=17, textColor=BLUE,
               alignment=TA_CENTER, spaceAfter=2)
S_SUB2    = st("sub2",   fontName="DVS-I", fontSize=9.5, leading=13, textColor=GREY,
               alignment=TA_CENTER, spaceAfter=8)
S_H1      = st("h1",     fontName="DVS-B", fontSize=13, leading=16, textColor=NAVY,
               spaceBefore=12, spaceAfter=5, alignment=TA_LEFT)
S_H2      = st("h2",     fontName="DVS-B", fontSize=10.5, leading=14, textColor=BLUE,
               spaceBefore=9, spaceAfter=3, alignment=TA_LEFT)
S_H3      = st("h3",     fontName="DVS-B", fontSize=9.5, leading=13, textColor=GREY,
               spaceBefore=6, spaceAfter=2, alignment=TA_LEFT)
S_BODY    = st("body")
S_BODY_L  = st("bodyL",  alignment=TA_LEFT)
S_BULL    = st("bull",   leftIndent=14, bulletIndent=4, spaceAfter=2, alignment=TA_LEFT)
S_Q       = st("q",      fontName="DVS-B", fontSize=9.5, leading=13, textColor=colors.black,
               alignment=TA_LEFT, spaceBefore=6, spaceAfter=2)
S_OPT     = st("opt",    leftIndent=22, spaceAfter=1.5, alignment=TA_LEFT)
S_ANS     = st("ans",    fontName="DVS-B", fontSize=9.5, leading=13, textColor=GREEN,
               alignment=TA_LEFT, spaceBefore=3, spaceAfter=5)
S_ANS_TXT = st("anstxt", fontName="DVS-I", fontSize=9, leading=12.5, textColor=GREY,
               leftIndent=22, spaceAfter=4, alignment=TA_LEFT)
S_NOTE    = st("note",   fontName="DVS-I", fontSize=8.5, leading=11.5, textColor=GREY,
               alignment=TA_JUSTIFY, spaceAfter=4)
S_TABLE   = st("table",  fontName="DVS", fontSize=8.2, leading=10.5, alignment=TA_LEFT)
S_TABLEB  = st("tableB", fontName="DVS-B", fontSize=8.2, leading=10.5, alignment=TA_LEFT,
               textColor=colors.white)
S_TABLEH  = st("tableH", fontName="DVS-B", fontSize=8.4, leading=11, alignment=TA_CENTER,
               textColor=colors.white)

def P(text, style=S_BODY):
    return Paragraph(text, style)

def bullet(text):
    return ListFlowable(
        [ListItem(P(text, S_BULL), leftIndent=14, value="•")],
        bulletType="bullet", start="•", leftIndent=14, bulletFontName="DVS-B",
        bulletFontSize=8, spaceBefore=1, spaceAfter=2)

def section(num, title):
    return [HRFlowable(width="100%", thickness=1, color=NAVY, spaceBefore=2, spaceAfter=6),
            Paragraph(f"{num}.  {title}", S_H1)]

# ----------------------------------------------------------------------------
# Document
# ----------------------------------------------------------------------------
doc = BaseDocTemplate(
    "/home/user/anh-10/review-guide/De_cuong_on_tap_Tieng_Anh_10_GK1_2026-2027.pdf",
    pagesize=A4,
    leftMargin=16*mm, rightMargin=16*mm, topMargin=14*mm, bottomMargin=14*mm,
    title="De cuong on tap Tieng Anh 10 - Giua ky 1 - 2026-2027",
    author="Superpowers review guide (from 2026_2027_MA TRAN 10_GK1.docx)",
)
frame = Frame(doc.leftMargin, doc.bottomMargin, doc.width, doc.height, id="main")
doc.addPageTemplates([PageTemplate(id="page", frames=[frame])])

story = []

# ============================ COVER ============================
story.append(Spacer(1, 6))
story.append(P("ĐỀ CƯƠNG ÔN TẬP TIẾNG ANH 10", S_TITLE))
story.append(P("KIỂM TRA GIỮA KỲ 1 – NĂM HỌC 2026–2027", S_SUB))
story.append(P("Dựa trên bộ sách giáo khoa <b>Global Success</b> (Units 1–3)", S_SUB2))
story.append(P("Nội dung phân tích từ tệp: <i>2026_2027_MA TRẬN 10_GK1.docx</i> "
               "— Mã kỹ thuật & Bảng đặc tả đề kiểm tra giữa kỳ 1", S_SUB2))
story.append(Spacer(1, 4))
story.append(HRFlowable(width="100%", thickness=1.4, color=ACCENT, spaceBefore=4, spaceAfter=8))

story.append(P("Môn: <b>Tiếng Anh 10</b>   |   "
               "Chương trình: <b>Giáo dục phổ thông 2018</b>   |   "
               "Bộ sách: <b>Global Success</b> (Units 1–3)", st("cover", fontSize=10, leading=14, alignment=TA_CENTER, spaceAfter=10)))

# Summary info box
info = Table([
    [P("Tổng số câu", S_TABLEB), P("28 câu trắc nghiệm (TN) + 3 tự luận (TL)", S_TABLE),
     P("Tỷ lệ", S_TABLEB), P("70% TN / 30% TL", S_TABLE)],
    [P("Tổng điểm", S_TABLEB), P("10 điểm", S_TABLE),
     P("Thời gian làm bài", S_TABLEB), P("Theo quy định của trường", S_TABLE)],
    [P("Các chủ điểm", S_TABLEB), P("Unit 1: Family life  |  Unit 2: Humans and the environment  |  Unit 3: Music", S_TABLE),
     P("Mức độ đánh giá", S_TABLEB), P("Biết – Hiểu – Vận dụng", S_TABLE)],
], colWidths=[26*mm, 62*mm, 26*mm, 42*mm])
info.setStyle(TableStyle([
    ("BACKGROUND", (0,0), (0,-1), LIGHT),
    ("BACKGROUND", (2,0), (2,-1), LIGHT),
    ("GRID", (0,0), (-1,-1), 0.5, LINE),
    ("VALIGN", (0,0), (-1,-1), "MIDDLE"),
    ("TOPPADDING", (0,0), (-1,-1), 4),
    ("BOTTOMPADDING", (0,0), (-1,-1), 4),
    ("LEFTPADDING", (0,0), (-1,-1), 5),
    ("RIGHTPADDING", (0,0), (-1,-1), 5),
]))
story.append(info)
story.append(Spacer(1, 10))

story.append(P("<b>Lưu ý quan trọng:</b> Đề cương này được biên soạn chặt chẽ theo <b>Ma trận</b> và "
               "<b>Bảng đặc tả kỹ thuật</b> đã được trích từ tệp gốc. Tất cả kiến thức, dạng bài, chủ điểm và "
               "mức độ đánh giá sau đây đều nằm trong phạm vi kiểm tra. Học sinh nên ôn tập đồng bộ cả知识 học tế và "
               "thực hành từng dạng bài có đáp án chi tiết ở phần V.", S_NOTE))

# ============================ 1. THÔNG TIN CHUNG ============================
story += section("1", "THÔNG TIN CHUNG VỀ KỲ THI")
story.append(P("Kiểm tra giữa kỳ 1 môn Tiếng Anh 10 (năm học 2026–2027) kiểm tra khả năng sử dụng ngôn ngữ "
               "qua bốn kỹ năng: <b>Nghe (Listening)</b>, <b>Ngữ âm – Từ vựng – Ngữ pháp (Language)</b>, "
               "<b>Đọc (Reading)</b> và <b>Viết (Writing)</b>.", S_BODY))
for b in [
    "<b>Hình thức câu hỏi:</b> trắc nghiệm nhiều lựa chọn (MCQs), đúng/sai (True/False), điền từ vào chỗ trống, viết lại câu, sắp xếp từ/cụm và viết đoạn văn.",
    "<b>Chủ điểm kiến thức:</b> Unit 1 – Family life; Unit 2 – Humans and the environment; Unit 3 – Music.",
    "<b>Tỷ lệ điểm:</b> Trắc nghiệm ocupa khoảng 70%, Tự luận khoảng 30% của tổng điểm.",
    "<b>Mức độ đánh giá:</b> <b>Biết</b> (nhận ra/nhớ lại), <b>Hiểu</b> (phân biệt/giải thích), <b>Vận dụng</b> (sử dụng trong văn cảnh).",
]:
    story.append(bullet(b))

# ============================ 2. CHI TIẾT TỪNG PHẦN ============================
story += section("2", "CHI TIẾT TỪNG PHẦN THI VÀ YÊU CẦU CẦN ĐẠT")

# --- 2.1 Listening ---
story.append(P("2.1  PHẦN NGHE HIỂU (LISTENING)", S_H2))
story.append(P("Số bài nghe: <b>2 bài</b> (Listening 1 & Listening 2). Mỗi bài khoảng <b>1.5 phút (180–200 từ)</b>, "
               "xoay quanh các chủ điểm Unit 1–3.", S_BODY))
story.append(Table([
    [P("Bài nghe", S_TABLEH), P("Dạng bài", S_TABLEH), P("Yêu cầu cần đạt", S_TABLEH), P("Mức độ / trọng số", S_TABLEH)],
    [P("Listening 1", S_TABLEB), P("True/False hoặc dạng bài tương tự", S_TABLE),
     P("Nghe một đoạn hội thoại/độc thoại để trả lời các dạng câu hỏi liên quan đến chủ điểm đã học.", S_TABLE),
     P("Biết: nghe lấy thông tin chi tiết (30)  Hiểu: hiểu nội dung chính để tìm câu trả lời đúng (20)", S_TABLE)],
    [P("Listening 2", S_TABLEB), P("Trắc nghiệm nhiều lựa chọn (MCQs) hoặc dạng tương tự", S_TABLE),
     P("Nghe một đoạn hội thoại/độc thoại khoảng 1.5 phút (180–200 từ) liên quan đến chủ điểm đã học.", S_TABLE),
     P("Biết: nghe lấy thông tin chi tiết (30)  Hiểu: hiểu nội dung chính để tìm câu trả lời đúng (20)", S_TABLE)],
], colWidths=[24*mm, 40*mm, 56*mm, 36*mm]))
story.append(Spacer(1, 3))
story.append(P("<b>Chủ điểm nghe:</b> Family life · Humans and the environment · Music.", S_NOTE))

# --- 2.2 Language ---
story.append(P("2.2  PHẦN NGỪ ÂM – TỪ VỰNG – NGỮ PHÁP (LANGUAGE)", S_H2))
story.append(P("Dạng bài chủ yếu là <b>trắc nghiệm nhiều lựa chọn (MCQs)</b> hoặc dạng tương tự, dựa trên Unit 1–3.", S_BODY))

story.append(P("2.2.1  Từ vựng (Vocabulary)", S_H3))
story.append(P("Nội dung: từ vựng đã học theo Unit 1–3 (Family life; Humans and the environment; Music).", S_BODY))
for b in [
    "<b>Biết:</b> nhận ra, nhớ lại, liệt kê được các từ vựng theo chủ điểm đã học.",
    "<b>Hiểu:</b> hiểu và phân biệt được các từ vựng theo chủ điểm; nắm được các mối liên kết và kết hợp của từ trong bối cảnh và ngữ cảnh tương ứng.",
    "<b>Vận dụng:</b> hiểu và vận dụng được từ vựng đã học trong văn cảnh (danh từ, động từ, tính từ và trạng từ…).",
]:
    story.append(bullet(b))

story.append(P("2.2.2  Ngữ pháp (Grammar)", S_H3))
story.append(P("Các chủ điểm ngữ pháp đã học (Unit 1–3): <b>Present simple and present continuous</b>; "
               "<b>Future and be going to</b>; <b>Passive Voice</b>; <b>Compound sentences</b>; <b>To-infinitive and bare-infinitive</b>.", S_BODY))
for b in [
    "<b>Biết:</b> nhận ra được các kiến thức ngữ pháp đã học.",
    "<b>Hiểu:</b> hiểu và phân biệt các chủ điểm ngữ pháp đã học.",
    "<b>Hiểu (vận dụng mức cao):</b> phân biệt được các đặc trưng, đặc điểm các thành tố ngôn ngữ và liên kết về mặt văn bản như các dạng khác nhau của động từ (V-ing, to-infinitive, bare-infinitive…).",
]:
    story.append(bullet(b))

story.append(P("2.2.3  Điền từ vào chỗ trống (Close-text)", S_H3))
story.append(P("Đọc tờ rơi/quảng cáo và điền từ vào chỗ trống. Chủ điểm: Family life; Humans and the environment; Music.", S_BODY))
for b in [
    "<b>Biết:</b> nhận ra các thành tố ngôn ngữ và liên kết về mặt văn bản.",
    "<b>Hiểu:</b> phân biệt được các đặc điểm, đặc trưng của các thành tố ngôn ngữ và liên kết về mặt văn bản.",
]:
    story.append(bullet(b))

# --- 2.3 Reading ---
story.append(P("2.3  PHẦN ĐỌC HIỂU (READING)", S_H2))
story.append(P("Có <b>2 bài đọc</b> (Reading 1, Reading 2) dạng trắc nghiệm và một bài đọc hiểu chi tiết.", S_BODY))
for b in [
    "<b>Reading 1 & Reading 2:</b> đoạn văn liên quan đến chủ điểm Unit 1–3, dạng trắc nghiệm nhiều lựa chọn (MCQs) hoặc dạng tương tự.",
    "<b>Đọc hiểu:</b> hiểu được nội dung chính và nội dung chi tiết của đoạn văn bản khoảng <b>220–250 từ</b>, xoay quanh các chủ điểm trong chương trình (Family life; Humans and the environment; Music).",
    "<b>Yêu cầu mức Hiểu:</b> phân biệt đặc điểm/đặc trưng các thành tố ngôn ngữ và liên kết văn bản; hiểu ý chính và chọn câu trả lời phù hợp; hiểu nghĩa tham chiếu; loại trừ các chi tiết sai để đưa ra câu trả lời chính xác.",
]:
    story.append(bullet(b))

# --- 2.4 Writing ---
story.append(P("2.4  PHẦN VIẾT (WRITING)", S_H2))
story.append(P("Có <b>3 bài viết</b>: Writing 1 (sắp xếp lại), Writing 2 (viết lại câu), Writing 3 (viết đoạn văn).", S_BODY))
writing_rows = [
    [P("Bài viết", S_TABLEH), P("Dạng bài / yêu cầu", S_TABLEH), P("Mức độ", S_TABLEH)],
    [P("Writing 1", S_TABLEB),
     P("Sắp xếp lại (Re-ordering): nhận diện dùng từ, cấu trúc, cú pháp trong câu đơn lẻ và sắp xếp thành một hội thoại/lá thư/đoạn văn theo đúng trật tự, cấu trúc.", S_TABLE),
     P("Biết: nhận diện từ, cấu trúc, cú pháp", S_TABLE)],
    [P("Writing 2", S_TABLEB),
     P("Viết lại câu (Sentence transformation): sử dụng kiến thức về các cấu trúc câu để viết lại câu cùng nghĩa với câu đã cho.", S_TABLE),
     P("Vận dụng: viết lại câu cùng nghĩa", S_TABLE)],
    [P("Writing 3", S_TABLEB),
     P("Viết đoạn văn/lá thư/bài báo liền mạch, đơn giản khoảng 120–150 từ về các chủ điểm, bày tỏ quan điểm, ý kiến cá nhân. Chủ điểm: Family life; Humans and the environment; Music.", S_TABLE),
     P("Vận dụng: viết đoạn văn 120–150 từ", S_TABLE)],
]
wt = Table(writing_rows, colWidths=[22*mm, 98*mm, 36*mm], repeatRows=1)
wt.setStyle(TableStyle([
    ("BACKGROUND", (0,0), (-1,0), NAVY),
    ("GRID", (0,0), (-1,-1), 0.5, LINE),
    ("ROWBACKGROUNDS", (0,1), (-1,-1), [colors.white, LIGHT2]),
    ("VALIGN", (0,0), (-1,-1), "MIDDLE"),
    ("TOPPADDING", (0,0), (-1,-1), 4),
    ("BOTTOMPADDING", (0,0), (-1,-1), 4),
    ("LEFTPADDING", (0,0), (-1,-1), 5),
]))
story.append(wt)

# ============================ 3. TÓM TẢT KIẾN THỨC ============================
story += section("3", "TÓM TẢT KIẾN THỨC CẦN NẠM (UNIT 1–3)")

story.append(P("3.1  Unit 1 – Family life", S_H3))
story.append(P("<b>Từ vựng và chủ đề:</b> thành viên gia đình (extended family, nuclear family, breadwinner, close-knit family), "
               "khoảng cách thế hệ (generation gap), việc nhà (household chores), quan hệ gia đình (get along with, take care of, support, respect), "
               "vai trò cha mẹ và con cái.", S_BODY_L))
story.append(P("<b>Ngữ pháp liên quan:</b> thì hiện tại đơn và hiện tại tiếp diễn; từ vợng biểu thị thói quen và hành động đang xảy ra.", S_NOTE))

story.append(P("3.2  Unit 2 – Humans and the environment", S_H3))
story.append(P("<b>Từ vựng và chủ đề:</b> môi trường (environment), ô nhiễm (pollution), phá rừng (deforestation), loài nguy cấp (endangered species), "
               "nóng lên toàn cầu (global warming), tái chế (recycle), bảo vệ môi trường (protect the environment), thải khí thải (emissions), năng lượng tái tạo.", S_BODY_L))
story.append(P("<b>Ngữ pháp liên quan:</b> thì tương lai (will và be going to); câu bị động đơn giản.", S_NOTE))

story.append(P("3.3  Unit 3 – Music", S_H3))
story.append(P("<b>Từ vựng và chủ đề:</b> thể loại âm nhạc (genre), giai điệu (melody), nhịp điệu (rhythm), lời bài hát (lyrics), dàn nhạc (orchestra), "
               "đ franske trình (perform), khán giả (audience), nhạc cụ (instrument), ca sĩ (singer), nhạc sĩ (composer).", S_BODY_L))
story.append(P("<b>Ngữ pháp liên quan:</b> câu ghép (compound sentences); to-infinitive và bare-infinitive sau các động từ/đặc tính tính từ.", S_NOTE))

# ============================ 4. LƯỢT LÀM BÀI ============================
story += section("4", "LƯỢT LÀM BÀI VÀ MẸO ÔN TẬP")
for b in [
    "<b>Trước khi làm:</b> đọc kỹ hướng dẫn của từng phần; phân tích rõ từ khóa trong câu hỏi trước khi chọn đáp án.",
    "<b>Nghe:</b> tập trung từ câu đầu, ghi chú từ khóa (tên, thời gian, nơi, số lượng, ý chính); không bỏ qua bất kỳ từ ngữ nào trong hướng dẫn bài nghe.",
    "<b>Từ vựng/Ngữ pháp:</b> ôn lại bảng từ vựng theo chủ điểm và công thức các thì ngữ pháp; khi làm MCQs, loại chọn sai trước khi chọn đúng.",
    "<b>Đọc:</b> quét đoạn văn để nắm ý chính trước; đọc kỹ câu hỏi rồi quay lại tìm vị trí thông tin trong bài; chú ý từ thay thế (referencing).",
    "<b>Viết:</b> Writing 1 – chú ý liên kết từ và trình tự_logic; Writing 2 – giữ nguyên nghĩa, chỉ thay đổi cấu trúc; Writing 3 – viết khoảng 120–150 từ, có chủ đề câu rõ ràng, dùng các connective (however, therefore, in addition, for example) và kiểm tra ngữ pháp trước khi nộp.",
    "<b>Quản lý thời gian:</b> dành phần lớn thời gian cho trắc nghiệm (70% điểm),留 enough thời gian cho phần tự luận, nhất là bài viết 120–150 từ.",
]:
    story.append(bullet(b))

# ============================ 5. HỆ THỐNG CÂU HỎI THỰC HÀNH ============================
story += section("5", "HỆ THỐNG CÂU HỎI THỰC HÀNH KÈM ĐÁP ÁN")

story.append(P("5.1  Nghe hiểu (Listening)", S_H3))
story.append(P("<b>Bài nghe 1 (True/False):</b> “My family is a close-knit family. My father is the breadwinner and works in a company. "
               "My mother is a teacher. She takes care of the family and helps me with my homework. My elder brother studies music at university. "
               "At the weekend, we often do housework together and have dinner as a family. I love my family very much.”", S_Q))
for q,a,exp in [
    ("1. The writer’s father is a teacher.", "Sai", "Cha là breadwinner làm việc ở công ty; mẹ mới là giáo viên."),
    ("2. The mother helps the writer with homework.", "Đúng", "Mẹ gi´m viết bài cho con."),
    ("3. The elder brother studies medicine at university.", "Sai", "Anh trai học âm nhạc (music), không phải y khoa."),
]:
    story.append(P(q, S_OPT)); story.append(P(f"Đáp án: <b>{a}</b> — {exp}", S_ANS_TXT))

story.append(P("<b>Bài nghe 2 (Trắc nghiệm):</b> “We must protect the environment. Deforestation and pollution are causing global warming. "
               "Many animals are now endangered. We should recycle waste and plant more trees to save the Earth.”", S_Q))
for q,opts,a,exp in [
    ("What is causing global warming?", ["A. Recycling waste", "B. Deforestation and pollution", "C. Planting trees", "D. Saving endangered animals"],
     "B", "Đoạn văn n´c rõ deforestation and pollution là g&acircy ra global warming."),
    ("What should we do to save the Earth?", ["A. Cut down more trees", "B. Throw waste everywhere", "C. Recycle waste and plant more trees", "D. Ignore endangered animals"],
     "C", "Tàc giæ khuyến khích recycle waste and plant more trees."),
]:
    story.append(P(q, S_OPT))
    for o in opts:
        story.append(P(o, S_OPT))
    story.append(P(f"Đáp án: <b>{a}</b> — {exp}", S_ANS_TXT))

# --- 5.2 Language ---
story.append(P("5.2  Ngữ âm – Từ vựng – Ngữ pháp (Language)", S_H3))
story.append(P("5.2.1  Từ vựng (Vocabulary)", S_H3))
for q,opts,a,exp in [
    ("My ______ works hard to earn money for our family.", ["A. breadwinner", "B. generation gap", "C. household chores", "D. close-knit"], "A",
     "Breadwinner = người n chịu Haupt chi trả cho gia đình."),
    ("We should ______ plastic bottles to protect the environment.", ["A. burn", "B. recycle", "C. cut down", "D. waste"], "B",
     "Recycle = tái chế, phù hŝp vào câu bài vê bào v managed s经 sinh thâi."),
    ("I really like the ______ of this song; it’s very pleasant.", ["A. lyrics", "B. melody", "C. orchestra", "D. audience"], "B",
     "Melody = giai điệu (nhiều ính ính, pleasant)."),
]:
    story.append(P(q, S_OPT))
    for o in opts:
        story.append(P(o, S_OPT))
    story.append(P(f"Đáp án: <b>{a}</b> — {exp}", S_ANS_TXT))

story.append(P("5.2.2  Ngữ pháp (Grammar)", S_H3))
for q,opts,a,exp in [
    ("Look! The children ______ in the park now.", ["A. play", "B. are playing", "C. played", "D. will play"], "B",
     "Từ khóa “now” thî hiện tại tiếp diễn: are playing."),
    ("We ______ visit our grandparents next weekend.", ["A. are", "B. is going to", "C. are going to", "D. goes to"], "C",
     "We (nhù số nhiều) + be going to = are going to."),
    ("This song ______ by a famous singer last year.", ["A. sings", "B. is sung", "C. was sung", "D. has sung"], "C",
     "Câu bị động quá khứ đơn: was sung (by a famous singer, last year)."),
    ("I enjoy ______ to music in my free time.", ["A. listen", "B. to listen", "C. listening", "D. listened"], "C",
     "Sau enjoy, dùng V-ing: listening."),
    ("She wants ______ a new guitar.", ["A. buy", "B. to buy", "C. buying", "D. bought"], "B",
     "Sau want, dùng to-infinitive: to buy."),
]:
    story.append(P(q, S_OPT))
    for o in opts:
        story.append(P(o, S_OPT))
    story.append(P(f"Đáp án: <b>{a}</b> — {exp}", S_ANS_TXT))

story.append(P("5.2.3  Điền từ vào chỗ trống (Close-text)", S_H3))
story.append(P("Đoạn văn (tờ rơi/quảng cáo): “SAVE OUR PLANET! The Earth is in danger because of (1) ______. We must stop cutting down trees and (2) ______ waste. "
               "Everyone should (3) ______ used paper, plastic and glass. Together we can (4) ______ the environment for future generations.”", S_Q))
for n,a,exp in [
    ("(1)", "pollution", "Ô nhiễm là ngyên nhân làm Trói Mặt Đất nguy hiểm."),
    ("(2)", "recycling", "Dừng việc rác rách rác rác; c&acircu bài kêu g烤i recycling waste (tài bài sau waste là động danh/nghe>). Để an toàn, đáp án phù hŝp là 'reducing' hoàc 'recycling'; theo ngữ cảnh bài vào vài vài môi tr­­­ờng là 'recycling'/'reducing'. Chấp nhận: recycling/reducing."),
    ("(3)", "recycle", "Mọi người nên tái chế giấy nhựa kích; recycle used paper..."),
    ("(4)", "protect", "Bảo vệ môi trường cho các thé hệ sau…: protect the environment."),
]:
    story.append(P(f"{n}. Đáp án gợi ý: <b>{a}</b> — {exp}", S_ANS_TXT))

# --- 5.3 Reading ---
story.append(P("5.3  Đọc hiểu (Reading)", S_H3))
story.append(P("Đoạn văn: “Music plays an important role in our life. It helps us relax after a hard-working day. There are many kinds of music such as pop, rock, jazz and classical. "
               "Teenagers often like pop music because it is lively and modern. Classical music is suitable for old people or when we need to study. "
               "Listening to music can also improve our mood and reduce stress.”", S_Q))
for q,opts,a,exp in [
    ("What is the main idea of the passage?", ["A. Music is only for teenagers", "B. Music has an important role in our life", "C. Classical music is the best", "D. Pop music reduces stress"],
     "B", "Đoạn n´c role quan trọng của âm nhạc trong cu?c s?ng."),
    ("Who often likes pop music?", ["A. Old people", "B. Teenagers", "C. Singers", "D. Teachers"], "B",
     "Teenagers often like pop music."),
    ("When is classical music suitable?", ["A. When we exercise", "B. When we study or for old people", "C. At parties", "D. In the morning"], "B",
     "Classical music is suitable for old people or when we need to study."),
]:
    story.append(P(q, S_OPT))
    for o in opts:
        story.append(P(o, S_OPT))
    story.append(P(f"Đáp án: <b>{a}</b> — {exp}", S_ANS_TXT))

# --- 5.4 Writing ---
story.append(P("5.4  Viết (Writing)", S_H3))
story.append(P("5.4.1  Writing 1 – Sắp xếp lại (Re-ordering)", S_H3))
story.append(P("Sắp xếp các câu sau thành đoạn văn liền mạch:", S_Q))
story.append(P("a. My mother is a teacher.  b. She helps me with my homework every evening.  c. I love my family very much.  d. My father is a doctor.", S_Q))
story.append(P("Đáp án gợi ý: d → a → b → c (“My father is a doctor. My mother is a teacher. She helps me with my homework every evening. I love my family very much.”)", S_ANS_TXT))

story.append(P("5.4.2  Writing 2 – Viết lại câu (Sentence transformation)", S_H3))
for q,a,exp in [
    ("Gốc: People speak English all over the world. → Viết lại thành câu bị động.", "English is spoken all over the world.", "Câu bị động thì hiện tại đơn: be + V3/V-ed."),
    ("Gốc: I will visit my grandparents tomorrow. → Viết lại với be going to.", "I am going to visit my grandparents tomorrow.", "will → am/is/are going to."),
    ("Gốc: She likes listening to music. → Viết lại với to-infinitive.", "She likes to listen to music.", "Sau like, cùng cù thì to-infinitive hoặc V-ing."),
]:
    story.append(P(q, S_OPT))
    story.append(P(f"Đáp án: <b>{a}</b> — {exp}", S_ANS_TXT))

story.append(P("5.4.3  Writing 3 – Viết đoạn văn (120–150 từ)", S_H3))
story.append(P("Đề bài: Viết một đoạn văn khoảng 120–150 từ về chủ điểm <b>Family life</b>, bày tỏ quan điểm và ý kiến cá nhân của bạn.", S_Q))
story.append(P("Bài mẫu gợi ý (dưới 150 từ):", S_H3))
story.append(P("My family is a close-knit family of four: my father, my mother, my elder brother and me. "
               "My father is the breadwinner; he works hard in a company. My mother is a teacher and she takes care of the family. "
               "My brother studies music at university. At the weekend, we often do housework together and have dinner as a family. "
               "I love my family because they always support me. In my opinion, a happy family is very important in everyone’s life.", S_ANS))

# ============================ 6. ĐÁP ÁN TỔNG HỢP ============================
story += section("6", "ĐÁP ÁN TỔNG HỢP")
ans_rows = [
    [P("STT", S_TABLEH), P("Phần", S_TABLEH), P("Câu", S_TABLEH), P("Đáp án", S_TABLEH)],
    [P("1", S_TABLEB), P("Listening 1", S_TABLE), P("1-3", S_TABLE), P("Sai, Đúng, Sai", S_TABLE)],
    [P("2", S_TABLEB), P("Listening 2", S_TABLE), P("1-2", S_TABLE), P("B, C", S_TABLE)],
    [P("3", S_TABLEB), P("Từ vựng", S_TABLE), P("1-3", S_TABLE), P("A, B, B", S_TABLE)],
    [P("4", S_TABLEB), P("Ngữ pháp", S_TABLE), P("1-5", S_TABLE), P("B, C, C, C, B", S_TABLE)],
    [P("5", S_TABLEB), P("Close-text", S_TABLE), P("1-4", S_TABLE), P("pollution, recycling/reducing, recycle, protect", S_TABLE)],
    [P("6", S_TABLEB), P("Reading", S_TABLE), P("1-3", S_TABLE), P("B, B, B", S_TABLE)],
    [P("7", S_TABLEB), P("Writing 1", S_TABLE), P("sắp xếp", S_TABLE), P("d-a-b-c", S_TABLE)],
    [P("8", S_TABLEB), P("Writing 2", S_TABLE), P("1-3", S_TABLE), P("Xem chi tiết phần 5.4.2", S_TABLE)],
]
at = Table(ans_rows, colWidths=[12*mm, 34*mm, 24*mm, 86*mm], repeatRows=1)
at.setStyle(TableStyle([
    ("BACKGROUND", (0,0), (-1,0), NAVY),
    ("GRID", (0,0), (-1,-1), 0.5, LINE),
    ("ROWBACKGROUNDS", (0,1), (-1,-1), [colors.white, LIGHT2]),
    ("VALIGN", (0,0), (-1,-1), "MIDDLE"),
    ("TOPPADDING", (0,0), (-1,-1), 3.5),
    ("BOTTOMPADDING", (0,0), (-1,-1), 3.5),
]))
story.append(at)
story.append(Spacer(1, 6))

# ============================ 7. CHECKLIST ============================
story += section("7", "CHECKLIST TỰ KIỂM TRA TRƯỚC KHI THI")
story.append(P("Đánh dấu (☐) khi đã hoàn thành từng mục:", S_BODY))
for b in [
    "☐ Đã ôn lại từ vựng cả 3 chủ điểm: Family life, Humans and the environment, Music.",
    "☐ Đã nắm công thức và dụng pháp: thì hiện tại đơn & tiếp diễn, tương lai (will/be going to), câu bị động, câu ghép, to-infinitive & bare-infinitive.",
    "☐ Đã làm theo dõi ít nhất 2 bài nghe và nắm được cách chọn True/False và MCQs.",
    "☐ Đã làm ít nhất 1 bài đọc hiểu đoạn 220–250 từ và tìm ý chính, nghĩa tham chiếu.",
    "☐ Đã viết lại ít nhất 3 câu sang câu bị động/câu ghép/to-infinitive.",
    "☐ Đã viết 1 đoạn văn 120–150 từ về một trong 3 chủ điểm và kiểm tra ngữ pháp.",
    "☐ Đã kiểm tra lại đáp án và hiểu tại sao sai (nếu có).",
]:
    story.append(bullet(b))

story.append(Spacer(1, 10))
story.append(HRFlowable(width="100%", thickness=0.8, color=LINE, spaceBefore=4, spaceAfter=4))
story.append(P("Đề cương biên soạn từ <i>2026_2027_MA TRẬN 10_GK1.docx</i> (Mã kỹ thuật & Bảng đặc tả kiểm tra giữa kỳ 1, Tiếng Anh 10, "
               "năm học 2026–2027, Global Success). Chúc bạn học tập hiệu quả và đạt kết quả cao!", S_NOTE))

doc.build(story)
print("PDF built successfully.")