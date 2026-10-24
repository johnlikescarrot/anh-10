#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Comprehensive Review Outline: English 10 - Mid-term 1 - Global Success 2026-2027
Generator using fpdf2 + DejaVu
"""
from fpdf import FPDF
import os

# Paths
FONT_REG = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"
FONT_BOLD = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"
FONT_OBLIQUE = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"  # fallback
OUT = "/home/user/anh-10/De_Cuong_On_Tap_Tieng_Anh_10_GK1_2026-2027_Global_Success.pdf"

# Colors (RGB)
BLUE_DARK = (18, 58, 109)
BLUE = (32, 86, 165)
BLUE_LIGHT = (231, 240, 255)
BLUE_MID = (200, 220, 255)
ORANGE = (255, 127, 38)
ORANGE_LIGHT = (255, 243, 230)
GREEN = (22, 130, 90)
GREEN_LIGHT = (225, 245, 235)
RED = (192, 38, 38)
RED_LIGHT = (254, 232, 232)
PURPLE = (109, 59, 165)
PURPLE_LIGHT = (240, 232, 255)
YELLOW = (210, 160, 0)
YELLOW_LIGHT = (255, 248, 220)
GRAY_DARK = (55, 65, 81)
GRAY = (107, 114, 128)
GRAY_LIGHT = (243, 244, 246)
WHITE = (255,255,255)
BLACK = (0,0,0)

class PDF(FPDF):
    def __init__(self):
        super().__init__(orientation='P', unit='mm', format='A4')
        self.add_font("DejaVu", "", FONT_REG)
        self.add_font("DejaVu", "B", FONT_BOLD)
        # use same for I/ BI
        self.add_font("DejaVu", "I", FONT_REG)
        self.add_font("DejaVu", "BI", FONT_BOLD)
        self.set_auto_page_break(auto=True, margin=18)
        self.toc_entries = []  # (title, page, level)
        self.current_section = ""

    def header(self):
        if self.page_no() == 1:
            return
        # top bar
        self.set_fill_color(*BLUE_DARK)
        self.rect(0, 0, 210, 10, 'F')
        self.set_y(2.5)
        self.set_font("DejaVu", "B", 7)
        self.set_text_color(255,255,255)
        self.set_x(10)
        self.cell(0, 5, "TIẾNG ANH 10 GLOBAL SUCCESS  •  GIỮA KỲ 1  •  2026–2027", align='C')
        # line
        self.set_draw_color(*BLUE)
        # self.line(10, 11, 200, 11)

    def footer(self):
        if self.page_no() == 1:
            return
        self.set_y(-12)
        self.set_font("DejaVu", "", 6.5)
        self.set_text_color(*GRAY)
        self.cell(0, 10, f"Trang {self.page_no()}  |  Đề cương do nhóm biên soạn • Lưu hành nội bộ • Không vì mục đích thương mại", align='C')
        # page number circle
        # self.set_fill_color(*BLUE)
        # self.ellipse(185, 282, 10, 10, 'F')

    def add_toc_entry(self, title, level=1):
        self.toc_entries.append((title, self.page_no(), level))

    # Helpers
    def colored_box(self, x, y, w, h, fill, radius=2):
        self.set_fill_color(*fill)
        # fpdf2 rounded
        self.set_draw_color(*fill)
        self.rect(x, y, w, h, 'F')

    def section_title(self, number, title, subtitle=""):
        self.ln(2)
        # blue banner
        self.set_fill_color(*BLUE_DARK)
        self.set_draw_color(*BLUE_DARK)
        # banner
        y = self.get_y()
        self.rect(10, y, 190, 12, 'F')
        # number circle
        self.set_fill_color(*ORANGE)
        self.ellipse(13, y+1, 10, 10, 'F')
        self.set_xy(13, y+1)
        self.set_font("DejaVu", "B", 10)
        self.set_text_color(*WHITE)
        self.cell(10, 10, number, align='C')
        self.set_xy(25, y+1)
        self.set_font("DejaVu", "B", 11)
        self.set_text_color(*WHITE)
        self.cell(0, 10, title.upper(), align='L')
        self.set_y(y+14)
        if subtitle:
            self.set_font("DejaVu", "I", 7.5)
            self.set_text_color(*GRAY)
            self.set_x(12)
            self.cell(0, 4, subtitle, align='L')
            self.ln(5)
        else:
            self.ln(2)
        self.set_text_color(*BLACK)

    def sub_title(self, text, color=BLUE):
        self.set_fill_color(*color)
        self.rect(10, self.get_y(), 4, 6, 'F')
        self.set_x(16)
        self.set_font("DejaVu", "B", 9.5)
        self.set_text_color(*color)
        self.cell(0, 6, text)
        self.ln(7)
        self.set_text_color(*BLACK)

    def tip_box(self, title, content, fill=PURPLE_LIGHT, border=PURPLE, icon="*"):
        x = 10
        y = self.get_y()
        # need to compute height: use multi_cell calc
        # We'll do manual: width 190
        self.set_font("DejaVu", "", 7.5)
        # measure
        w = 190
        # create temp to calc height
        # Use helper: get string width? Instead use multi_cell with dry run via get_y diff
        start_y = self.get_y()
        # draw background after measuring: we need to use auto page break aware
        # We'll just use multi_cell and then rect behind by capturing
        # Simpler: use cell with fill and then overlay? We'll do manual rect estimate afterwards
        # Approach: write to dummy then know height
        # Let's use a trick: create a small pdf clone? Simpler: write content, remember y, then draw rect behind via rect covering area with transparency? We'll just draw rect with fixed height estimate using multi_cell height calc
        # fpdf2 has get_string_width? We'll compute lines
        # We'll just draw after: we need height = ...
        # Use: height = pdf.get_y() after writing - start_y + padding
        # So we need to write without background first? We'll do two passes: first pass invisible to measure
        # For simplicity, we will directly use multi_cell with fill
        self.set_fill_color(*fill)
        self.set_draw_color(*border)
        # Title
        self.set_font("DejaVu", "B", 8)
        self.set_text_color(*border)
        # We'll create a bordered box using rect + text
        # First, we need to render content to know height. Let's render content to a temporary calculation.
        # Use FPDF's multi_cell to get height: we can use new_x, new_y parameters and measure.
        # But easiest: just draw rect with approximate then write text over.
        # Let's do manual height calc:
        line_h = 4
        # estimate lines for content
        # quick split
        avail_w = w - 6
        # Use fpdf to count lines: we can use multi_cell with dry run via output to string not possible. We'll brute: count chars
        # We'll approximate: each line ~95 chars at 7.5pt
        # Better to use pdf's own method: we can create a dummy pdf instance
        from copy import deepcopy
        # Use actual multi_cell height calculation via using self.get_string_width iteratively
        def calc_height(txt, font_size=7.5, width=avail_w):
            self.set_font("DejaVu", "", font_size)
            words = txt.split()
            lines = 1
            cur_w = 0
            space_w = self.get_string_width(" ")
            for wd in words:
                wd_w = self.get_string_width(wd)
                if cur_w + wd_w > width:
                    lines += 1
                    cur_w = wd_w + space_w
                else:
                    cur_w += wd_w + space_w
            return lines * line_h + 6  # title + padding
        est_h = calc_height(content) + 6
        # ensure not break page awkwardly: if est_h > 80 and near bottom, add page
        if self.get_y() + est_h > 277:
            self.add_page()
            y = self.get_y()
        else:
            y = self.get_y()
        # draw
        self.set_fill_color(*fill)
        self.set_draw_color(*border)
        self.rect(x, y, w, est_h, 'DF')
        # left accent
        self.set_fill_color(*border)
        self.rect(x, y, 3, est_h, 'F')
        # text
        self.set_xy(x+6, y+1.5)
        self.set_font("DejaVu", "B", 7.5)
        self.set_text_color(*border)
        self.cell(0, 4, f"{icon}  {title}")
        self.set_xy(x+6, y+6)
        self.set_font("DejaVu", "", 7.5)
        self.set_text_color(*GRAY_DARK)
        self.multi_cell(w-8, line_h, content, align='L')
        self.set_y(y + est_h + 2)

    def table_header(self, col_widths, headers, fill=BLUE_DARK, text_color=WHITE):
        self.set_font("DejaVu", "B", 6.5)
        self.set_fill_color(*fill)
        self.set_text_color(*text_color)
        self.set_draw_color(*fill)
        x0 = self.get_x()
        y0 = self.get_y()
        h = 7
        for i, (cw, hd) in enumerate(zip(col_widths, headers)):
            x = x0 + sum(col_widths[:i])
            self.rect(x, y0, cw, h, 'DF')
            self.set_xy(x+1, y0+1)
            self.multi_cell(cw-2, 2.5, hd, align='C')
        # need to set y after header (max height)
        self.set_y(y0+h)

    def table_row(self, col_widths, cells, fills=None, font_size=6.5, align_list=None, bold_first=False):
        if fills and len(fills)==len(col_widths):
            pass
        else:
            fills = [WHITE]*len(col_widths)
        if not align_list:
            align_list = ['C']*len(col_widths)
        # calculate row height as max lines * line_h
        line_h = 3.2
        # compute lines per cell (respects explicit \n)
        max_lines = 1
        for cw, txt in zip(col_widths, cells):
            self.set_font("DejaVu", "B" if bold_first else "", font_size)
            avail = cw - 2
            total_lines = 0
            space_w = self.get_string_width(" ")
            for segment in str(txt).split("\n"):
                seg_words = segment.split() or [""]
                cur_w = 0
                lines = 1
                for wd in seg_words:
                    wd_w = self.get_string_width(wd)
                    if wd_w > avail:  # single long word/token
                        lines += int(wd_w // avail)
                        cur_w = wd_w % avail
                    elif cur_w + wd_w > avail:
                        lines += 1
                        cur_w = wd_w + space_w
                    else:
                        cur_w += wd_w + space_w
                total_lines += lines
            if total_lines > max_lines:
                max_lines = total_lines
        rh = max(6, max_lines*line_h + 2)
        # page break check
        if self.get_y() + rh > 277:
            self.add_page()
        x0 = self.get_x()
        y0 = self.get_y()
        self.set_draw_color(180,180,180)
        for i, (cw, txt) in enumerate(zip(col_widths, cells)):
            fill = fills[i] if isinstance(fills[i], (list,tuple)) else fills[i]
            # Actually fills[i] is color tuple
            # Need to handle
            # For simplicity, if fills is list of colors
            # Already set
            # Draw cell
            col_fill = fills[i] if isinstance(fills, list) and isinstance(fills[i], tuple) else WHITE
            if isinstance(fills, list) and len(fills)==len(col_widths) and isinstance(fills[0], tuple):
                col_fill = fills[i]
            self.set_fill_color(*col_fill)
            self.rect(x0 + sum(col_widths[:i]), y0, cw, rh, 'DF')
            self.set_xy(x0 + sum(col_widths[:i])+1, y0+1)
            fnt = "B" if (bold_first and i==0) else ""
            self.set_font("DejaVu", fnt, font_size)
            self.set_text_color(*BLACK)
            # vertical centering approximation
            self.multi_cell(cw-2, line_h, txt, align=align_list[i])
        self.set_y(y0+rh)

    def bullet(self, text, indent=12, bullet="•", bullet_color=BLUE, text_size=7.5):
        x0 = indent
        self.set_font("DejaVu", "", text_size)
        self.set_text_color(*bullet_color)
        self.set_x(x0)
        self.cell(4, 4, bullet)
        self.set_text_color(*BLACK)
        self.set_x(x0+4)
        # need to handle multi line: use multi_cell with offset
        # Save x,y
        y0 = self.get_y()
        # width
        w = 190 - (x0-10) - 4
        # Use multi_cell
        self.multi_cell(w, 4, text, align='L')
        self.ln(0.5)

    def numbered_q(self, num, text, options=None, answer=None, explain=None):
        # check space
        needed = 22
        if options:
            needed += len(options)*5
        if self.get_y() + needed > 275:
            self.add_page()
        self.set_font("DejaVu", "B", 8)
        self.set_text_color(*BLUE_DARK)
        self.set_x(12)
        self.cell(10, 5, f"Câu {num}:")
        self.set_font("DejaVu", "", 8)
        self.set_text_color(*BLACK)
        # text may be long, use multi_cell
        x_after = self.get_x()
        w = 190 - (x_after-10)
        # To align properly, we use multi_cell from current x
        y0 = self.get_y()
        self.multi_cell(w, 4, text, align='L')
        if options:
            self.set_font("DejaVu", "", 7.5)
            for opt in options:
                self.set_x(16)
                self.set_text_color(*GRAY_DARK)
                self.multi_cell(184, 4, opt, align='L')
                self.ln(0.3)
        self.ln(1)

    def add_cover(self):
        self.add_page()
        # background
        self.set_fill_color(*BLUE_DARK)
        self.rect(0, 0, 210, 297, 'F')
        # decorative circles
        self.set_fill_color(255,255,255)
        self.set_draw_color(255,255,255)
        # large transparent circles simulated with white low opacity? Use light blue
        self.set_fill_color(*BLUE)
        self.ellipse(-30, -20, 120, 120, 'F')
        self.ellipse(150, 200, 140, 140, 'F')
        self.set_fill_color(255,255,255)
        # For white we will draw small
        # Title box
        self.set_fill_color(*WHITE)
        # rounded rect hack: use rect
        self.rect(15, 45, 180, 110, 'F')
        self.set_draw_color(*ORANGE)
        self.set_line_width(1.5)
        self.rect(15, 45, 180, 110, 'D')
        self.set_line_width(0.2)
        # inside
        self.set_xy(15, 52)
        self.set_font("DejaVu", "B", 9)
        self.set_text_color(*ORANGE)
        self.cell(180, 5, "BỘ GIÁO DỤC & ĐÀO TẠO  •  NĂM HỌC 2026–2027", align='C')
        self.set_xy(20, 60)
        self.set_font("DejaVu", "B", 22)
        self.set_text_color(*BLUE_DARK)
        # Title multi line
        self.multi_cell(170, 9, "ÔN TẬP GIỮA KỲ 1\nTIẾNG ANH 10", align='C')
        self.set_font("DejaVu", "B", 11)
        self.set_text_color(*BLUE)
        self.set_x(15)
        self.cell(180, 6, "GLOBAL SUCCESS", align='C')
        self.set_xy(15, 92)
        self.set_font("DejaVu", "B", 7.5)
        self.set_text_color(*WHITE)
        self.set_fill_color(*BLUE)
        self.rect(25, 92, 160, 8, 'F')
        self.cell(180, 8, "MA TRẬN CHUẨN  •  ĐỀ CƯƠNG TRỌNG TÂM  •  LUYỆN ĐỀ CÓ ĐÁP ÁN", align='C')
        # subtitle
        self.set_xy(15, 105)
        self.set_font("DejaVu", "", 7.5)
        self.set_text_color(*BLUE)
        self.cell(180, 4, "Units 1–2–3  |  Family Life  •  Humans and the Environment  •  Music", align='C')
        self.set_xy(15, 110)
        self.set_font("DejaVu", "I", 7)
        self.set_text_color(*GRAY)
        self.cell(180, 4, "Kèm:  Tóm tắt ngữ pháp  •  Từ vựng theo chủ đề  •  Chiến thuật làm bài  •  02 đề thi thử  •  Đáp án giải thích chi tiết  •  Bài mẫu Writing", align='C')

        # bottom info boxes
        yb = 165
        boxes = [
            ("10 ĐIỂM", "Thang điểm\n70% trắc nghiệm\n30% tự luận"),
            ("4 KỸ NĂNG", "Listening 25%\nReading 25%\nLanguage 25%\nWriting 25%"),
            ("7 NGÀY", "Lộ trình 7 ngày\nnắm trọn kiến thức\nNhớ lâu - Dùng được"),
        ]
        for i, (big, small) in enumerate(boxes):
            x = 15 + i*62
            self.set_fill_color(*WHITE)
            self.rect(x, yb, 56, 34, 'F')
            self.set_draw_color(*WHITE)
            self.set_font("DejaVu", "B", 13)
            self.set_text_color(*BLUE_DARK)
            self.set_xy(x, yb+3)
            self.cell(56, 6, big, align='C')
            self.set_font("DejaVu", "", 6.5)
            self.set_text_color(*GRAY_DARK)
            self.set_xy(x+2, yb+10)
            self.multi_cell(52, 3, small, align='C')
        # footer cover
        self.set_xy(15, 210)
        self.set_font("DejaVu", "", 7)
        self.set_text_color(220,230,255)
        self.multi_cell(180, 3.5, "Tài liệu lưu hành nội bộ – Dành cho học sinh lớp 10 ôn tập giữa kỳ 1.\nBiên soạn bám sát Ma trận & Bảng đặc tả 2026–2027 do trường ban hành, đối chiếu sách Global Success (Kết nối tri thức).\nMẹo học: In màu – Dán checklist cuối tài liệu lên bàn học – Làm 1 đề/ngày.", align='C')
        self.set_xy(15, 240)
        self.set_font("DejaVu", "B", 7)
        self.set_fill_color(*ORANGE)
        self.set_text_color(*WHITE)
        self.rect(70, 240, 70, 7, 'F')
        self.cell(180, 7, "PHIÊN BẢN 1.0  •  THÁNG 10/2026", align='C')
        # small note
        self.set_xy(15, 260)
        self.set_font("DejaVu", "", 6)
        self.set_text_color(180,200,255)
        self.cell(180, 3, "Khuyến nghị: Học trên giấy + nghe audio qua mã QR (nếu có) – Không học vẹt, hiểu bản chất.", align='C')

pdf = PDF()
pdf.set_margins(10,12,10)

# COVER
pdf.add_cover()

# INSIDE: Lời nói đầu
pdf.add_page()
pdf.section_title("01", "Lời nói đầu & Cách dùng đề cương này", "Đọc 3 phút để học nhanh gấp 3 lần")
pdf.set_font("DejaVu", "", 8)
pdf.set_text_color(*GRAY_DARK)
pdf.multi_cell(0, 4.2, "Bạn đang cầm trên tay bản tóm tắt “đúng trọng tâm – dễ nhớ – làm được bài ngay” cho bài kiểm tra giữa kỳ 1 Tiếng Anh 10 (Global Success) năm học 2026–2027. Tài liệu được biên soạn TRỰC TIẾP từ Ma trận & Bảng đặc tả chính thức của trường (đính kèm file 2026_2027_MA TRẬN 10_GK1.docx), đối chiếu từng Unit 1–2–3 trong sách giáo khoa.", align='J')
pdf.ln(2)
pdf.tip_box("Cam kết của tài liệu", "• Bám 100% ma trận: 70% trắc nghiệm + 30% tự luận, đúng tỉ lệ Listening/Reading/Language/Writing.\n• Chỉ học những gì THI – không lan man. Mỗi điểm ngữ pháp đều có công thức – ví dụ – bẫy thường gặp.\n• Có đề luyện chuẩn format + đáp án giải thích tiếng Việt để tự học ở nhà.", fill=BLUE_LIGHT, border=BLUE, icon="v")
pdf.sub_title("Ai nên dùng?")
pdf.bullet("Học sinh mất gốc muốn lấy lại căn bản trong 7 ngày (lộ trình trang 4).")
pdf.bullet("Học sinh khá/giỏi muốn hệ thống hóa, luyện đề để đạt 9–10.")
pdf.bullet("Phụ huynh/giáo viên cần tài liệu in phát cho lớp, đúng ma trận mới nhất.")
pdf.sub_title("Cách học hiệu quả (3 bước)", GREEN)
pdf.set_font("DejaVu", "B", 8)
pdf.set_text_color(*GREEN)
pdf.cell(0,4.5,"BƯỚC 1: NẮM KHUNG → BƯỚC 2: LUYỆN KỸ NĂNG → BƯỚC 3: THI THỬ & SỬA LỖI",align='L')
pdf.ln(6)
pdf.set_font("DejaVu", "", 7.5)
pdf.set_text_color(*BLACK)
pdf.bullet("Mỗi ngày học 1 Unit + 1 điểm ngữ pháp (45 phút). Dùng bút highlight đánh dấu cụm từ in đậm.")
pdf.bullet("Làm Listening bằng cách đọc transcript trước, sau đó nghe lại (nếu có audio). Reading: làm cloze trước, comprehension sau.")
pdf.bullet("Writing: chép tay 1 bài mẫu/ngày, sau đó tự viết lại không nhìn. So sánh với đáp án.")
pdf.tip_box("Mẹo nhớ lâu", "Học theo cụm (chunk), không học từ rời rạc. Ví dụ: đừng học “carbon” riêng lẻ, hãy học “reduce carbon footprint” – cả cụm.", fill=YELLOW_LIGHT, border=YELLOW, icon="!")

# GIẢI MÃ MA TRẬN
pdf.section_title("02", "Giải mã ma trận đề thi 2026–2027", "Hiểu đề để không học lệch – biết mình được điểm ở đâu")
pdf.set_font("DejaVu", "", 7.5)
pdf.set_text_color(*GRAY_DARK)
pdf.multi_cell(0,4,"Đề kiểm tra giữa kỳ 1 gồm 4 phần lớn, tổng 10 điểm, thời gian dự kiến 60 phút (không kể Listening). 70% là trắc nghiệm nhiều lựa chọn (28 câu), 30% là tự luận (6 câu biến đổi + 1 đoạn văn 120–150 từ). Dưới đây là bảng “dịch” ma trận gốc thành ngôn ngữ học sinh:",align='J')
pdf.ln(2)

# Simplified matrix table
col_w = [28,30,42,22,22,46]  # sum 190
headers = ["PHẦN","NỘI DUNG","DẠNG BÀI","SỐ CÂU","TỈ TRỌNG","GHI CHÚ ÔN TẬP"]
pdf.table_header(col_w, headers)
rows = [
    ["LISTENING\n25%","Part 1:\nTrue/False","Nghe hội thoại/độc thoại\n1.5 phút, 180–200 từ", "5","12.5%","Chủ đề: Family life,\nHumans & Environment,\nMusic"],
    ["LISTENING","Part 2:\nMCQs (A-B-C-D)","Nghe hội thoại/độc thoại\n1.5 phút, 180–200 từ","5","12.5%","3 câu Biết (chi tiết)\n2 câu Hiểu (ý chính)"],
    ["LANGUAGE\n25%","Vocabulary","Từ vựng Unit 1-2-3\nMCQs + Word form","4\n(2 TN +2 TL)","15%","Học cụm từ, collocation\nBẫy: từ đồng nghĩa/trái nghĩa"],
    ["LANGUAGE","Grammar","Present tenses, Will/be going to,\nPassive, Compound,\nTo-inf/Bare-inf","4","10%","2 câu Biết +2 câu Hiểu\nNhận diện dạng động từ"],
    ["READING\n25%","Cloze text\n(Flyer/Advertisement)","Điền từ vào chỗ trống\nTờ rơi/quảng cáo","5","12.5%","3 Biết +2 Hiểu\nLiên kết văn bản"],
    ["READING","Comprehension","Đọc hiểu 220–250 từ\n5 câu MCQs","5","12.5%","Tìm ý chính, chi tiết,\ntham chiếu"],
    ["WRITING\n25%","Re-ordering","Sắp xếp câu thành\nđoạn hội thoại/lá thư","2","5%","Mức Biết – dễ lấy điểm\nChú ý từ nối"],
    ["WRITING","Transformation","Viết lại câu cùng nghĩa\nDùng ngữ pháp đã học","4","10%","Mức Vận dụng\nPassive, to-inf, compound"],
    ["WRITING","Paragraph","Viết đoạn 120–150 từ\nTự luận","1 bài","10%","Chủ đề Family/Environment/Music\nCó bố cục rõ ràng"],
]
# fills alternating
for idx, r in enumerate(rows):
    fills = [WHITE]*6
    if idx%2==1:
        fills = [GRAY_LIGHT]*6
    # highlight listening, reading, etc.
    if idx in [0,1]:
        fills[0]=BLUE_LIGHT
    if idx in [2,3]:
        fills[0]=GREEN_LIGHT
    if idx in [4,5]:
        fills[0]=PURPLE_LIGHT
    if idx in [6,7,8]:
        fills[0]=ORANGE_LIGHT
    align = ['C','C','L','C','C','L']
    pdf.table_row(col_w, r, fills=fills, align_list=align, font_size=6.5)
pdf.ln(2)
pdf.set_font("DejaVu", "I", 6.5)
pdf.set_text_color(*GRAY)
pdf.cell(0,3,"Nguồn: Ma trận + Bảng đặc tả 2026_2027_MA TRẬN 10_GK1.docx – Tổng: 28 câu TN (7đ) + 6 câu TL +1 đoạn văn (3đ) = 10 điểm.",align='C')
pdf.ln(5)

# Levels
pdf.sub_title("3 mức độ đánh giá bạn sẽ gặp", PURPLE)
pdf.set_font("DejaVu", "", 7.5)
pdf.set_text_color(*BLACK)
levels = [
    ("BIẾT (40%)","Nhận ra, nhớ lại, liệt kê – Ví dụ: Chọn đáp án đúng về thì hiện tại đơn. Học bằng flashcards, lặp lại."),
    ("HIỂU (30%)","Phân biệt, giải thích, tìm ý chính – Ví dụ: Nghe hiểu ý chính, đọc hiểu tham chiếu. Học bằng cách diễn đạt lại."),
    ("VẬN DỤNG (30%)","Dùng kiến thức trong văn cảnh mới – Ví dụ: Viết lại câu bị động, viết đoạn văn. Học bằng thực hành viết."),
]
for title,desc in levels:
    pdf.set_font("DejaVu", "B", 7.5)
    pdf.set_text_color(*PURPLE)
    pdf.cell(25,4,title)
    pdf.set_font("DejaVu", "", 7.5)
    pdf.set_text_color(*BLACK)
    pdf.multi_cell(0,4, f"– {desc}")
    pdf.ln(1)

pdf.tip_box("Chiến lược điểm số", "Muốn 8+ : làm chắc BIẾT + HIỂU (70% đề = 7 điểm), sau đó ăn thêm 1–2 câu Vận dụng.\nMuốn 9–10: phải luyện Writing paragraph theo template (trang 28) và không mất điểm oan ở Re-ordering.", fill=GREEN_LIGHT, border=GREEN, icon=">")

pdf.sub_title("Cấu trúc đề thi minh họa (60 phút)", BLUE)
pdf.set_font("DejaVu", "", 7)
pdf.multi_cell(0,4,"Thứ tự làm bài khuyên dùng: Language (8 phút) → Reading (15 phút) → Writing Re-ordering + Transformation (12 phút) → Listening (10 phút) → Paragraph (15 phút) → Kiểm tra 5 phút. Đừng để Listening làm bạn cuống; cứ bình tĩnh nghe 2 lần.",align='L')
pdf.ln(2)

# LỘ TRÌNH 7 NGÀY
pdf.section_title("03", "Lộ trình 7 ngày nắm trọn 10 điểm", "Dành cho bạn bận rộn – mỗi ngày 45–60 phút")
col_w2 = [22,45,70,53]
pdf.table_header(col_w2, ["NGÀY","TRỌNG TÂM","VIỆC CẦN LÀM (30–45p)","KIỂM TRA NHANH"])
plan = [
    ["1","Unit 1: Family Life\n+ Present Simple vs Continuous","Học 20 từ vựng Unit 1 (bảng trang 6)\nLàm BT ngữ pháp 1 (trang 14)","Viết 5 câu về gia đình bạn\nbằng thì hiện tại"],
    ["2","Unit 2: Humans & Environment\n+ Will vs Be going to\n+ Passive Voice","Học 20 từ vựng Unit 2 (trang 8)\nLuyện bị động (trang 16)","Viết 5 câu Passive về môi trường"],
    ["3","Unit 3: Music\n+ Compound Sentences\n+ To-inf / Bare-inf","Học 20 từ vựng Unit 3 (trang 10)\nLuyện câu ghép & dạng động từ","Viết 5 câu ghép về âm nhạc"],
    ["4","Kỹ năng Listening & Reading","Luyện chiến thuật (trang 18)\nLàm Reading Cloze 1 + Comprehension 1","Tự chấm, ghi lỗi vào sổ"],
    ["5","Kỹ năng Writing","Học template paragraph (trang 28)\nLuyện Re-ordering + Transformation","Viết 1 đoạn 130 từ chủ đề Family"],
    ["6","Đề thử số 1 (chuẩn ma trận)","Bấm giờ 60 phút, làm nghiêm túc\nKhông tra từ điển","Chấm theo đáp án trang 36"],
    ["7","Đề thử số 2 + Tổng ôn","Sửa lỗi, học lại phần yếu\nĐọc checklist trang cuối","Tự tin đi thi!"],
]
for i,r in enumerate(plan):
    fills = [YELLOW_LIGHT if i%2==0 else WHITE]*4
    if i==5 or i==6:
        fills[0]=ORANGE_LIGHT
    pdf.table_row(col_w2, r, fills=fills, align_list=['C','C','L','L'], font_size=6.5)
pdf.ln(2)
pdf.tip_box("Cam kết 7 ngày", "Nếu bạn làm đủ 7 ngày, bạn sẽ thuộc 60 từ vựng cốt lõi + 6 chủ điểm ngữ pháp + 2 lần thi thử. Đó là đủ để đạt 8+. Đừng bỏ ngày 6–7!", fill=ORANGE_LIGHT, border=ORANGE, icon=">")

# VOCAB UNIT 1
pdf.section_title("04", "Unit 1: Family Life – Cuộc sống gia đình", "Từ vựng + Ngữ pháp trọng tâm • Chiếm 30% Language & Writing")
pdf.sub_title("A. Từ vựng cốt lõi (20 từ/cụm – Học theo cụm)", BLUE)
pdf.set_font("DejaVu", "I", 7)
pdf.set_text_color(*GRAY)
pdf.cell(0,3,"Mẹo: Che cột tiếng Việt, nhìn tiếng Anh đoán nghĩa. Thuộc 80% là đạt.",align='L')
pdf.ln(4)
# vocab table
col_v = [45,55,55,35]
pdf.table_header(col_v, ["TỪ/CỤM (EN)","NGHĨA (VI)","VÍ DỤ NHỚ NHANH","TỪ LOẠI"])
vocab1 = [
    ["do the laundry\n/ do the washing-up","giặt giũ / rửa bát","My mom does the laundry every Sunday.","v."],
    ["take out the rubbish\n/ mop the house","đổ rác / lau nhà","Dad takes out the rubbish daily.","v."],
    ["prepare meals\n/ do the heavy lifting","nấu ăn / làm việc nặng","Parents usually prepare meals.","v."],
    ["breadwinner / homemaker","trụ cột / người nội trợ","My father is the breadwinner.","n."],
    ["household chores","việc nhà","We share household chores equally.","n."],
    ["generation gap","khoảng cách thế hệ","Generation gap causes conflicts.","n."],
    ["family values","giá trị gia đình","Respect is a core family value.","n."],
    ["supportive / grateful","ủng hộ / biết ơn","My family is supportive.","adj."],
    ["critical thinking","tư duy phản biện","School teaches critical thinking.","n."],
    ["quality time","thời gian chất lượng","Spend quality time together.","n."],
    ["strengthen bonds","thắt chặt gắn kết","Meals strengthen family bonds.","v."],
    ["financial burden","gánh nặng tài chính","Chores reduce financial burden.","n."],
    ["divide / share equally","phân chia / chia đều","We divide chores fairly.","v."],
    ["upbringing","sự nuôi dạy","Good upbringing matters.","n."],
    ["role model","tấm gương","Parents are role models.","n."],
]
for idx, r in enumerate(vocab1):
    fills = [BLUE_LIGHT if idx%2==0 else WHITE]*4
    pdf.table_row(col_v, r, fills=fills, align_list=['L','L','L','C'], font_size=6.5)
pdf.ln(2)
pdf.tip_box("Mẹo nhớ Unit 1", "Công thức 3x3: 3 người (breadwinner – homemaker – children) + 3 việc (do laundry – prepare meals – take out rubbish) + 3 giá trị (supportive – grateful – quality time). Đặt câu: “My supportive family shares chores to spend quality time.”", fill=BLUE_LIGHT, border=BLUE, icon="*")

pdf.sub_title("B. Collocations & Phrasal verbs hay thi", GREEN)
pdf.bullet("do housework / do the dishes / do the shopping ≠ make the bed (làm giường)")
pdf.bullet("take responsibility for / take care of / take out the trash")
pdf.bullet("help with sth / help sb (to) do sth – Bẫy: help sb do (bare-inf) hay gặp!")
pdf.bullet("spend time (on sth / doing sth) / share opinions / follow routines")

pdf.sub_title("C. Ngữ pháp Unit 1: Present Simple vs Present Continuous", ORANGE)
# Grammar table
pdf.set_font("DejaVu", "", 7.5)
pdf.multi_cell(0,4,"Đây là điểm ngữ pháp chiếm 1–2 câu trong đề. Đề thường cho trạng từ nhận biết (always, usually, now, at the moment) để đánh lừa.",align='L')
pdf.ln(1)
col_g = [35,55,50,50]
pdf.table_header(col_g, ["THÌ","CÔNG THỨC","DẤU HIỆU","VÍ DỤ"])
grammar1 = [
    ["Present Simple\n(Hiện tại đơn)","(+) S + V(s/es)\n(-) S + don’t/doesn’t + V\n(?) Do/Does + S + V?","always, usually, often, never, every day, twice a week","She usually does the laundry. (thói quen)\nMy dad works late. (sự thật)"],
    ["Present Continuous\n(Hiện tại tiếp diễn)","(+) S + am/is/are + V-ing\n(-) S + isn’t/aren’t + V-ing\n(?) Am/Is/Are + S + V-ing?","now, at the moment, at present, Look!, Listen!, currently","She is doing the washing-up now. (đang diễn ra)\nLook! Mom is cooking.",""],
]
for idx, r in enumerate(grammar1):
    fills = [ORANGE_LIGHT if idx%2==1 else YELLOW_LIGHT]*4
    pdf.table_row(col_g, r, fills=fills, align_list=['C','L','L','L'], font_size=6.8)
pdf.ln(1)
pdf.tip_box("Bẫy thường gặp", "• “now” nhưng lại là thói quen? Sai! → Phải là tiếp diễn.\n• Động từ không chia tiếp diễn: love, like, know, believe, understand → dù có “now” vẫn dùng Simple: “I understand now.”\n• Thì hiện tại đơn diễn tả lịch trình: “The bus leaves at 7 a.m.”", fill=RED_LIGHT, border=RED, icon="!")
pdf.set_font("DejaVu", "B", 7.5)
pdf.set_text_color(*ORANGE)
pdf.cell(0,4,"Bài tập nhanh (Unit 1) – Chọn đáp án đúng:")
pdf.ln(4)
pdf.set_font("DejaVu", "", 7.5)
pdf.set_text_color(*BLACK)
pdf.bullet("1. My mother (usually / now) __________ (prepare) meals at 6 p.m. – Đáp án: usually prepares (thói quen).")
pdf.bullet("2. Look! Your father __________ (take) out the rubbish. – Đáp án: is taking (ngay lúc nói).")
pdf.bullet("3. I __________ (not/understand) why he is shouting now. – Đáp án: don’t understand (stative verb).")
pdf.ln(2)

# UNIT 2
pdf.section_title("05", "Unit 2: Humans and the Environment", "Từ vựng “xanh” + Ngữ pháp Will/Be going to & Passive Voice")
pdf.sub_title("A. Từ vựng cốt lõi (20 từ/cụm)", GREEN)
col_v2 = [45,55,55,35]
pdf.table_header(col_v2, ["TỪ/CỤM (EN)","NGHĨA (VI)","VÍ DỤ NHỚ NHANH","TỪ LOẠI"])
vocab2 = [
    ["carbon footprint","dấu chân carbon","Reduce your carbon footprint!","n."],
    ["greenhouse effect\n/ global warming","hiệu ứng nhà kính /\nấm lên toàn cầu","Greenhouse effect causes warming.","n."],
    ["climate change","biến đổi khí hậu","Climate change is urgent.","n."],
    ["deforestation / landfill","phá rừng / bãi rác","Deforestation harms animals.","n."],
    ["pollutant / pollutant","chất gây ô nhiễm","Factories release pollutants.","n."],
    ["eco-friendly / sustainable","thân thiện MT / bền vững","Use eco-friendly bags.","adj."],
    ["renewable energy","năng lượng tái tạo","Solar is renewable energy.","n."],
    ["endangered species","loài nguy cấp","Tigers are endangered.","n."],
    ["organic food","thực phẩm hữu cơ","Organic food is healthier.","n."],
    ["cut down / clean up","chặt hạ / dọn sạch","Cut down on plastic! Clean up beaches.","v."],
    ["recycle / reuse / reduce","tái chế / tái sử dụng / giảm","Reuse bottles, recycle paper.","v."],
    ["adopt / protect","nhận nuôi / bảo vệ","Adopt green habits.","v."],
    ["awareness / campaign","nhận thức / chiến dịch","Raise awareness via campaign.","n."],
    ["emission / litter","khí thải / rác","CO2 emissions rise.","n."],
    ["preserve / conserve","bảo tồn / tiết kiệm","Preserve forests, conserve water.","v."],
]
for idx, r in enumerate(vocab2):
    fills = [GREEN_LIGHT if idx%2==0 else WHITE]*4
    pdf.table_row(col_v2, r, fills=fills, align_list=['L','L','L','C'], font_size=6.5)
pdf.ln(2)
pdf.tip_box("Mẹo nhớ Unit 2", "Chuỗi 3R: Reduce – Reuse – Recycle. Chuỗi nguyên nhân: deforestation → greenhouse effect → global warming → climate change → endangered species. Vẽ sơ đồ mũi tên là nhớ ngay!", fill=GREEN_LIGHT, border=GREEN, icon="*")

pdf.sub_title("B. Ngữ pháp 1: Will vs Be going to (Tương lai)", BLUE)
col_g2 = [32,62,48,48]
pdf.table_header(col_g2, ["DẠNG","KHI NÀO DÙNG?","VÍ DỤ","LƯU Ý BẪY"])
grammar2 = [
    ["will + V\n(quyết định tức thì, dự đoán chung)","Quyết định ngay lúc nói, lời hứa, dự đoán không căn cứ","“I’ll help you clean up.” (vừa quyết định)\nIt will rain tomorrow. (dự đoán)","Có “I think, probably” thường là will"],
    ["be going to + V\n(dự định, dự đoán có căn cứ)","Dự định đã có kế hoạch, dự đoán có dấu hiệu rõ ràng","I’m going to join a clean-up campaign. (đã định)\nLook at clouds! It’s going to rain. (có mây đen)","Có “plan, intend” → be going to"],
]
for idx, r in enumerate(grammar2):
    fills = [BLUE_LIGHT if idx==0 else YELLOW_LIGHT]*4
    pdf.table_row(col_g2, r, fills=fills, align_list=['C','L','L','L'], font_size=6.8)
pdf.ln(1)
pdf.set_font("DejaVu", "I", 7)
pdf.set_text_color(*GRAY)
pdf.cell(0,3,"Mẹo thi: Nếu câu có “Look at those dark clouds!” → chọn be going to. Nếu là lời mời/quyết định nhanh → will.",align='L')
pdf.ln(4)

pdf.sub_title("C. Ngữ pháp 2: Passive Voice (Câu bị động) – Hiện tại đơn", RED)
pdf.set_font("DejaVu", "", 7.5)
pdf.set_text_color(*BLACK)
pdf.multi_cell(0,4,"Passive xuất hiện 1–2 câu, thường trong Transformation. Chỉ học hiện tại đơn là đủ cho GK1.",align='L')
pdf.ln(1)
col_p = [38,62,50,40]
pdf.table_header(col_p, ["CHỦ ĐỘNG","BỊ ĐỘNG","VÍ DỤ","CHÚ Ý"])
passive_rows = [
    ["S + V(s/es) + O","S + am/is/are + V3/ed (+ by O)","People cut down trees.\n→ Trees are cut down.","by O có thể bỏ nếu không quan trọng"],
    ["S + don’t/doesn’t + V","S + am/is/are + not + V3","We don’t use plastic.\n→ Plastic isn’t used.","not đặt sau am/is/are"],
    ["Do/Does + S + V?","Am/Is/Are + S + V3?","Do you recycle paper?\n→ Is paper recycled?","Đảo am/is/are lên đầu"],
]
for idx, r in enumerate(passive_rows):
    fills = [RED_LIGHT if idx%2==0 else WHITE]*4
    pdf.table_row(col_p, r, fills=fills, align_list=['L','L','L','L'], font_size=6.8)
pdf.ln(1)
pdf.tip_box("Công thức thần tốc", "Active: S + V + O → Passive: O + be + V3/ed (+ by S). Nhớ chia be theo O mới: “Trees are...”, “Paper is...”.\nVí dụ: “They clean up beaches every week.” → “Beaches are cleaned up every week.”", fill=YELLOW_LIGHT, border=YELLOW, icon=">")

# UNIT 3
pdf.section_title("06", "Unit 3: Music – Âm nhạc", "Từ vựng showbiz + Ngữ pháp câu ghép & to-inf/bare-inf")
pdf.sub_title("A. Từ vựng cốt lõi (20 từ/cụm)", PURPLE)
col_v3 = [40,55,60,35]
pdf.table_header(col_v3, ["TỪ/CỤM (EN)","NGHĨA (VI)","VÍ DỤ NHỚ NHANH","LOẠI TỪ"])
vocab3 = [
    ["genre / pop / rock / folk / jazz","thể loại / nhạc pop/rock/dân ca/jazz","My favorite genre is pop.","n."],
    ["contest / competition","cuộc thi","She joined a singing contest.","n."],
    ["audience / viewer / judge","khán giả / người xem / giám khảo","Audience voted for her.","n."],
    ["award / prize","giải thưởng","He won an award.","n."],
    ["single / album\n/ release","đĩa đơn / album / phát hành","New single released yesterday.","n./v."],
    ["perform / performance","biểu diễn / màn trình diễn","She performed brilliantly.","v./n."],
    ["talent / talented","tài năng / tài năng","Talented singer won.","n./adj."],
    ["vote / viewer vote","bình chọn","Fans voted online.","v./n."],
    ["compose / composer","sáng tác / nhạc sĩ","He composes songs.","v./n."],
    ["lyrics / melody","lời bài hát / giai điệu","Lyrics are meaningful.","n."],
    ["inspire / inspired","truyền cảm hứng","Music inspires me.","v./adj."],
    ["single / debut","ra mắt","Debut album in 2020.","n."],
    ["eliminate / elimination","loại bỏ","He was eliminated.","v."],
    ["cover version","bản hát lại","Her cover went viral.","n."],
    ["charity concert","hòa nhạc từ thiện","Join charity concert!","n."],
]
for idx, r in enumerate(vocab3):
    fills = [PURPLE_LIGHT if idx%2==0 else WHITE]*4
    pdf.table_row(col_v3, r, fills=fills, align_list=['L','L','L','C'], font_size=6.5)
pdf.ln(2)
pdf.tip_box("Mẹo nhớ Unit 3", "Chuỗi show: contest → audience → judge → vote → award → single/album → release. Tưởng tượng 1 cuộc thi The Voice là nhớ hết!", fill=PURPLE_LIGHT, border=PURPLE, icon="*")

pdf.sub_title("B. Ngữ pháp 1: Compound Sentences (Câu ghép với and/but/or/so)", BLUE)
pdf.set_font("DejaVu", "", 7.5)
pdf.multi_cell(0,4,"Câu ghép = 2 mệnh đề độc lập nối bằng liên từ kết hợp (FANBOYS) + dấu phẩy trước liên từ. Trong đề thi, hay hỏi chọn liên từ đúng nghĩa.",align='L')
pdf.ln(1)
col_c = [25,40,65,60]
pdf.table_header(col_c, ["LIÊN TỪ","NGHĨA","CÁCH DÙNG","VÍ DỤ"])
compound = [
    ["and","và","thêm thông tin, liệt kê","I love pop, and my sister loves rock."],
    ["but","nhưng","tương phản, đối lập","He is talented, but he is lazy."],
    ["or","hoặc","lựa chọn","You can sing or dance."],
    ["so","vì vậy, nên","kết quả, hệ quả","She practiced hard, so she won."],
    ["for","bởi vì (= because)","nguyên nhân (trang trọng, ít thi)","He stayed home, for he was ill."],
    ["yet","nhưng (= but)","tương phản nhẹ","It’s late, yet she’s still singing."],
]
for idx, r in enumerate(compound):
    fills = [BLUE_LIGHT if idx%2==0 else WHITE]*4
    pdf.table_row(col_c, r, fills=fills, align_list=['C','C','L','L'], font_size=6.8)
pdf.ln(1)
pdf.set_font("DejaVu", "B", 7)
pdf.set_text_color(*RED)
pdf.cell(0,4,"Bẫy dấu phẩy: Trước and/but/or/so phải có dấu phẩy + mệnh đề đầy đủ. Sai: “I like music and singing everyday.” (không phải câu ghép, không cần phẩy). Đúng: “I like music, and I sing everyday.”")
pdf.ln(5)

pdf.sub_title("C. Ngữ pháp 2: To-infinitive vs Bare infinitive", ORANGE)
col_inf = [30,60,50,50]
pdf.table_header(col_inf, ["DẠNG","CÔNG THỨC HAY GẶP","VÍ DỤ","GHI NHỚ"])
inf_rows = [
    ["to-V\n(to-infinitive)","want/ decide/ hope/ plan/ learn + to V\nIt’s + adj + to V\ntoo + adj + to V / enough to V","I want to join the contest.\nIt’s important to protect environment.\nShe is talented enough to win.","Sau want, need, decide, plan → to V\nSau tính từ → to V"],
    ["V (bare-inf)\n(không “to”)","make/ let/ help + O + V\ncan/ will/ should + V\nwould rather + V","My parents make me do chores.\nLet me sing a song.\nYou should recycle.\nI’d rather stay home.","make/let/help + O + V (không to)\nNhưng: be made/allowed + to V (bị động lại có to)"],
]
for idx, r in enumerate(inf_rows):
    fills = [ORANGE_LIGHT if idx==0 else YELLOW_LIGHT]*4
    pdf.table_row(col_inf, r, fills=fills, align_list=['C','L','L','L'], font_size=6.8)
pdf.ln(1)
pdf.tip_box("Mẹo phân biệt nhanh", "Thấy “make/let” → không “to”: “make sb do”, “let sb do”. Thấy “want/need/decide/hope” → có “to”: “want to do”.\nBị động của make: “I was made to do chores.” (lại có “to” – bẫy hay thi!)", fill=RED_LIGHT, border=RED, icon="!")

# GRAMMAR MARATHON
pdf.section_title("07", "Tổng ôn ngữ pháp – Grammar Marathon", "6 chủ điểm – 1 trang/công thức – Nhìn là nhớ")
pdf.set_font("DejaVu", "", 7.5)
pdf.multi_cell(0,4,"Trang này là “tờ phao hợp pháp” bạn được mang vào phòng thi trong đầu. Học thuộc bảng này, bạn làm được 4 câu Language + 4 câu Transformation.",align='L')
pdf.ln(2)

# All grammar summary table
pdf.sub_title("Bảng tổng hợp công thức (in ra học)", BLUE_DARK)
col_sum = [38,70,42,40]
pdf.table_header(col_sum, ["CHỦ ĐIỂM","CÔNG THỨC VÀNG","DẤU HIỆU NHẬN BIẾT","VÍ DỤ ĐIỂN HÌNH"])
summaries = [
    ["Present Simple","S + V(s/es) / do-does-don’t","always, usually, every day, twice a week","She recycles every day."],
    ["Present Continuous","S + am/is/are + V-ing","now, at the moment, Look!, Listen!","She is recycling now."],
    ["Will vs Be going to","will + V (quyết định nhanh)\nbe going to + V (kế hoạch)","I think / probably → will\nLook! dark clouds → be going to","I’ll help you.\nI’m going to join campaign."],
    ["Passive Voice\n(Hiện tại đơn)","S + am/is/are + V3/ed (+ by O)","by O, được, bị","Paper is recycled."],
    ["Compound Sentence","S + V, and/but/or/so + S + V","and (và), but (nhưng), or (hoặc), so (nên)","I love music, so I sing."],
    ["To-inf / Bare-inf","want/decide + to V\nmake/let + O + V","want to, decide to, make sb do, let sb do","I want to sing.\nMake me do chores."],
]
for idx, r in enumerate(summaries):
    fills = [WHITE]*4
    if idx%2==0:
        fills = [BLUE_LIGHT]*4
    else:
        fills = [GRAY_LIGHT]*4
    pdf.table_row(col_sum, r, fills=fills, align_list=['C','L','L','L'], font_size=6.5)
pdf.ln(2)

pdf.tip_box("Thần chú 12 từ", "“Always Simple – Now Continuous – Will nhanh – Going to kế hoạch – Passive be + V3 – And/But/Or/So + phẩy – Want to – Make do”. Đọc 5 lần trước khi ngủ!", fill=YELLOW_LIGHT, border=YELLOW, icon="*")

# Word formation
pdf.sub_title("Word Formation – Từ loại (hay ra 2 câu tự luận Vocabulary)", GREEN)
pdf.set_font("DejaVu", "", 7.5)
pdf.multi_cell(0,4,"Dạng bài: Cho từ gốc trong ngoặc, chia dạng đúng (danh từ/động từ/tính từ/trạng từ). Ví dụ: “She sings (beauty) ______.” → beautifully / beautiful",align='L')
pdf.ln(1)
col_wf = [30,30,50,80]
pdf.table_header(col_wf, ["TỪ GỐC","DANH TỪ","TÍNH TỪ","TRẠNG TỪ / ĐỘNG TỪ"])
wf_rows = [
    ["beauty","beauty (n.)","beautiful","beautifully (adv.) / beautify (v.)"],
    ["care","care (n.)","careful / careless","carefully / carelessly (adv.)"],
    ["environment","environment (n.)","environmental","environmentally (adv.)"],
    ["pollute","pollution (n.)","polluted","polluting (adj.)"],
    ["sustain","sustainability (n.)","sustainable","sustainably (adv.)"],
    ["talent","talent (n.)","talented","talentedly (hiếm)"],
    ["create","creation / creativity","creative","creatively / create (v.)"],
    ["perform","performance","performing","perform (v.)"],
]
for idx, r in enumerate(wf_rows):
    fills = [GREEN_LIGHT if idx%2==0 else WHITE]*4
    pdf.table_row(col_wf, r, fills=fills, align_list=['C','C','C','L'], font_size=6.5)
pdf.ln(1)
pdf.set_font("DejaVu", "I", 7)
pdf.set_text_color(*GRAY)
pdf.cell(0,3,"Quy tắc: Noun thường đuôi -tion, -ment, -ness, -ance. Adj đuôi -ful, -less, -al, -ous. Adv = Adj + ly. Động từ hay là gốc.",align='L')
pdf.ln(4)

# Strategies
pdf.section_title("08", "Chiến thuật làm bài theo kỹ năng", "Mẹo của người ra đề – Làm đúng trình tự sẽ tăng 1–2 điểm")
# Listening
pdf.sub_title("LISTENING – 10 câu (25%) – Nghe 2 lần, bắt từ khóa", BLUE)
pdf.set_font("DejaVu", "", 7.5)
pdf.bullet("Bước 1: Đọc câu hỏi & đáp án TRƯỚC khi nghe (30 giây). Gạch chân từ khóa (tên, số, not, always, never).")
pdf.bullet("Bước 2: Lần 1 – Nghe lấy ý chính, đánh dấu đáp án chắc chắn. Đừng dừng lại ở câu khó!")
pdf.bullet("Bước 3: Lần 2 – Kiểm tra câu chưa chắc, chú ý bẫy “I used to... but now...” (đáp án là “now”).")
pdf.bullet("Bẫy True/False: Nếu trong bài nghe nói “almost, some, usually” mà câu hỏi nói “all, always, never” → thường là False.")
pdf.bullet("Từ vựng nghe hay gặp: household chores, carbon footprint, audience, judge, vote, single, album.")
pdf.tip_box("Từ khóa Listening", "Family life: chores, breadwinner, homemaker, quality time. Environment: recycle, landfill, emission, organic. Music: contest, perform, album, audience, award.", fill=BLUE_LIGHT, border=BLUE, icon="*")

pdf.sub_title("READING – 10 câu (25%)", PURPLE)
pdf.set_font("DejaVu", "B", 7.5)
pdf.set_text_color(*PURPLE)
pdf.cell(0,4,"Dạng 1: Cloze text (Tờ rơi/Quảng cáo) – 5 câu điền từ")
pdf.ln(4)
pdf.set_font("DejaVu", "", 7.5)
pdf.set_text_color(*BLACK)
pdf.bullet("Đọc lướt toàn bài để hiểu chủ đề (quảng cáo concert? chiến dịch môi trường?).")
pdf.bullet("Nhìn từ trước/sau chỗ trống: sau “a/an” cần danh từ số ít; sau “very” cần adj/adv; sau giới từ cần V-ing/Noun.")
pdf.bullet("Collocation: “reduce carbon footprint”, “take part in”, “eco-friendly products”.")
pdf.set_font("DejaVu", "B", 7.5)
pdf.set_text_color(*PURPLE)
pdf.cell(0,4,"Dạng 2: Comprehension (220–250 từ) – 5 câu MCQs")
pdf.ln(4)
pdf.set_font("DejaVu", "", 7.5)
pdf.set_text_color(*BLACK)
pdf.bullet("Câu ý chính (main idea) → đọc đoạn đầu + cuối, tìm từ lặp lại nhiều nhất.")
pdf.bullet("Câu chi tiết → quay lại bài, tìm từ khóa trùng câu hỏi (scan).")
pdf.bullet("Câu tham chiếu (“It/They” thay cho gì?) → nhìn câu trước đó, danh từ số ít/nhiều tương ứng.")
pdf.bullet("Loại trừ đáp án sai: đáp án dùng từ “always, never, all” thường sai nếu bài dùng “some, sometimes”.")
pdf.tip_box("Mẹo Reading", "Đừng dịch từng từ! Đọc câu hỏi trước, rồi mới đọc bài để tìm đáp án. Quản lý thời gian: 7 phút cho Cloze, 8 phút cho Comprehension.", fill=PURPLE_LIGHT, border=PURPLE, icon="*")

pdf.sub_title("WRITING – 7 câu (25%) – Dễ lấy điểm nếu học template", ORANGE)
pdf.set_font("DejaVu", "", 7.5)
pdf.bullet("Re-ordering (2 câu – 5%): Tìm câu mở đầu (thường là chào hỏi/giới thiệu), sau đó theo trình tự thời gian hoặc Q-A. Chú ý từ nối: First, Then, Finally, However, So.")
pdf.bullet("Transformation (4 câu – 10%): 90% rơi vào: Passive, to-inf/bare-inf, compound (so/and/but), will/be going to. Giữ nguyên thì!")
pdf.bullet("Paragraph (1 bài – 10%): Bắt buộc 3 phần: Mở (2 câu) – Thân (6–8 câu) – Kết (1–2 câu). Dùng template trang 28, chỉ thay từ khóa theo đề.")
pdf.tip_box("Công thức paragraph 120–150 từ", "Mở: I love/like... because... / In my opinion,...\nThân: First, ... Second, ... Moreover, ... For example, ...\nKết: In conclusion, ... I hope... / I think everyone should...", fill=ORANGE_LIGHT, border=ORANGE, icon=">")

# Practice Test 1
pdf.section_title("09", "Đề luyện số 1 – Chuẩn ma trận 2026–2027", "Bấm giờ 60 phút – Làm như thi thật – Không tra từ điển")
pdf.set_font("DejaVu", "I", 7)
pdf.set_text_color(*GRAY)
pdf.cell(0,3,"Họ tên: ___________________________  Lớp: 10___  Thời gian: 60 phút  |  Tổng: 10 điểm (28 TN x 0.25 + 6 TL x 0.25 + 1 đoạn văn 1.5đ + 0.5 trình bày)",align='L')
pdf.ln(4)
pdf.set_draw_color(*BLUE_DARK)
pdf.set_fill_color(*BLUE_LIGHT)
pdf.rect(10, pdf.get_y(), 190, 6, 'DF')
pdf.set_xy(10, pdf.get_y()+1)
pdf.set_font("DejaVu", "B", 8)
pdf.set_text_color(*BLUE_DARK)
pdf.cell(190,4,"PART A: LISTENING (2.5 điểm – 10 câu)",align='C')
pdf.ln(8)

# Listening Part 1 script provided
pdf.set_font("DejaVu", "B", 7.5)
pdf.set_text_color(*BLUE)
pdf.cell(0,4,"LISTENING 1: You will hear a conversation about family life. Listen and decide True (T) or False (F). (1.25 điểm)")
pdf.ln(4)
pdf.set_font("DejaVu", "I", 6.5)
pdf.set_text_color(*GRAY_DARK)
pdf.multi_cell(0,3.5,"Transcript (đọc trước khi nghe – khi thi thật sẽ nghe 2 lần):\n“Minh: Mom, can you help me with the laundry? I don’t know how to use the washing machine.\nMom: Sure! First, put your clothes in. Then add detergent. Don’t use too much. We usually do the laundry on Sundays, but today is Saturday and you need your uniform for tomorrow.\nMinh: Thanks! Dad is taking out the rubbish and my sister is preparing meals. We always share chores. I think it strengthens our family bonds.\nMom: Exactly! Your father is the breadwinner, but he still helps with housework. That’s a great family value.”",align='L')
pdf.ln(2)
pdf.set_font("DejaVu", "", 7.5)
pdf.set_text_color(*BLACK)
for i, q in enumerate([
    "Minh knows how to use the washing machine. _______",
    "The family usually does the laundry on Sundays. _______",
    "Minh’s sister is doing the washing-up. _______",
    "The family always shares household chores. _______",
    "Minh’s father never helps with housework. _______",
], start=1):
    pdf.bullet(f"Question {i}. {q}", indent=12, bullet="☐", bullet_color=BLUE)
pdf.ln(1)

pdf.set_font("DejaVu", "B", 7.5)
pdf.set_text_color(*BLUE)
pdf.cell(0,4,"LISTENING 2: You will hear a talk about a music contest. Choose the best answer A, B, C or D. (1.25 điểm)")
pdf.ln(4)
pdf.set_font("DejaVu", "I", 6.5)
pdf.set_text_color(*GRAY_DARK)
pdf.multi_cell(0,3.5,"Transcript:\n“Good evening! Welcome to ‘Teen Music Stars’. I’m your host, Anna. Tonight, five talented teenagers will perform. Our audience will vote for the winner. The winner will receive an award and release a single next month. Judges say this contest inspires young people. Last year, 2 million viewers watched the final. This year, we hope to have more. The show starts at 8 p.m. and tickets are eco-friendly – no plastic!”",align='L')
pdf.ln(2)
pdf.set_font("DejaVu", "", 7.5)
pdf.set_text_color(*BLACK)
qs2 = [
    ("6. What is the name of the contest?", ["A. Teen Music Stars","B. Teen Music Awards","C. Young Music Stars","D. Music Teen Contest"]),
    ("7. How many teenagers will perform tonight?", ["A. 2","B. 5","C. 8","D. 10"]),
    ("8. Who will vote for the winner?", ["A. Judges","B. Audience","C. Host","D. Viewers at home only"]),
    ("9. What will the winner receive?", ["A. Money","B. An album","C. An award and a single","D. A concert"]),
    ("10. When does the show start?", ["A. 7 p.m.","B. 8 p.m.","C. 9 p.m.","D. 10 p.m."]),
]
for q, opts in qs2:
    pdf.set_font("DejaVu", "B", 7.5)
    pdf.set_text_color(*BLACK)
    pdf.set_x(12)
    pdf.multi_cell(0,4,q,align='L')
    pdf.set_font("DejaVu", "", 7)
    for o in opts:
        pdf.set_x(16)
        pdf.cell(0,4,o,align='L')
        pdf.ln(4)
    pdf.ln(1)

# Part B Language
pdf.set_draw_color(*GREEN)
pdf.set_fill_color(*GREEN_LIGHT)
pdf.rect(10, pdf.get_y(), 190, 6, 'DF')
pdf.set_xy(10, pdf.get_y()+1)
pdf.set_font("DejaVu", "B", 8)
pdf.set_text_color(22,90,60)
pdf.cell(190,4,"PART B: LANGUAGE (2.5 điểm – 8 câu)",align='C')
pdf.ln(8)
pdf.set_font("DejaVu", "B", 7.5)
pdf.set_text_color(*GREEN)
pdf.cell(0,4,"I. Vocabulary & Grammar – Choose the best answer A, B, C or D. (1.5 điểm)")
pdf.ln(5)
lang_qs = [
    ("11. My parents __________ the heavy lifting. I just help with cooking.", ["A. do","B. make","C. take","D. get"], "A"),
    ("12. We should __________ our carbon footprint by using public transport.", ["A. raise","B. reduce","C. increase","D. cut down on (nhiễu)"], "B"),
    ("13. Look! She __________ a new song on stage. How talented!", ["A. performs","B. is performing","C. perform","D. has performed"], "B"),
    ("14. I __________ to join the clean-up campaign next Sunday. I’ve already registered.", ["A. will join","B. am going to join","C. join","D. joined"], "B"),
    ("15. Trash __________ every day in our neighbourhood. The streets are very clean.", ["A. collects","B. is collected","C. collected","D. are collected"], "B"),
    ("16. I love pop music, __________ my brother prefers classical music.", ["A. and","B. so","C. but","D. or"], "C"),
]
for q in lang_qs:
    txt, opts, ans = q
    pdf.set_font("DejaVu", "B", 7.5)
    pdf.set_text_color(*BLACK)
    pdf.set_x(12)
    pdf.multi_cell(0,4,txt,align='L')
    pdf.set_font("DejaVu", "", 7)
    for o in opts:
        pdf.set_x(16)
        pdf.cell(0,4,o,align='L')
        pdf.ln(4)
    pdf.ln(1)

pdf.set_font("DejaVu", "B", 7.5)
pdf.set_text_color(*GREEN)
pdf.cell(0,4,"II. Word formation – Give the correct form of the word in brackets. (0.5 điểm – Tự luận)")
pdf.ln(5)
pdf.set_font("DejaVu", "", 7.5)
pdf.set_text_color(*BLACK)
pdf.bullet("17. Her performance was very __________ (impress). She won the contest.", indent=12)
pdf.bullet("18. We need to raise __________ (aware) about environmental protection.", indent=12)
pdf.ln(1)
pdf.set_font("DejaVu", "I", 6.5)
pdf.set_text_color(*GRAY)
pdf.cell(0,3,"→ Viết từ đúng dạng (không viết lại cả câu). Mỗi câu 0.25đ.",align='L')
pdf.ln(4)

# Reading
pdf.set_draw_color(*PURPLE)
pdf.set_fill_color(*PURPLE_LIGHT)
pdf.rect(10, pdf.get_y(), 190, 6, 'DF')
pdf.set_xy(10, pdf.get_y()+1)
pdf.set_font("DejaVu", "B", 8)
pdf.set_text_color(*PURPLE)
pdf.cell(190,4,"PART C: READING (2.5 điểm – 10 câu)",align='C')
pdf.ln(8)
pdf.set_font("DejaVu", "B", 7.5)
pdf.set_text_color(*PURPLE)
pdf.cell(0,4,"I. Cloze text – Read the flyer and choose the best answer. (1.25 điểm)")
pdf.ln(5)
pdf.set_font("DejaVu", "I", 7)
pdf.set_text_color(*BLACK)
# Flyer box
pdf.set_fill_color(*YELLOW_LIGHT)
pdf.set_draw_color(*YELLOW)
y0 = pdf.get_y()
pdf.rect(12, y0, 186, 38, 'DF')
pdf.set_xy(14, y0+2)
pdf.set_font("DejaVu", "B", 8)
pdf.set_text_color(*BLUE_DARK)
pdf.cell(182,4,"*  GO GREEN CAMPAIGN – THIS SATURDAY!  *",align='C')
pdf.ln(6)
pdf.set_font("DejaVu", "", 6.8)
pdf.set_text_color(*BLACK)
pdf.set_x(14)
pdf.multi_cell(182,3.5,"Do you want to reduce your carbon footprint? Join our (19) __________ campaign! We will clean up beaches and (20) __________ plastic waste. Our aim is to protect (21) __________ species and fight climate change. Everyone can (22) __________ part in this meaningful activity. Let’s make our planet more (23) __________! Contact: greenclub@school.edu.vn",align='L')
pdf.set_y(y0+38+2)
pdf.set_font("DejaVu", "", 7)
for q in [
    "19. A. eco-friendly   B. environment   C. environmental   D. environmentally",
    "20. A. recycle   B. reuse   C. reduce   D. pollute",
    "21. A. endangered   B. dangerous   C. polluted   D. sustainable",
    "22. A. take   B. make   C. do   D. join",
    "23. A. polluted   B. sustainable   C. polluting   D. danger",
]:
    pdf.set_x(14)
    pdf.cell(0,4,q,align='L')
    pdf.ln(4)
pdf.ln(1)

pdf.set_font("DejaVu", "B", 7.5)
pdf.set_text_color(*PURPLE)
pdf.cell(0,4,"II. Reading comprehension – Read the passage and choose the best answer. (1.25 điểm)")
pdf.ln(5)
pdf.set_font("DejaVu", "", 7)
pdf.set_text_color(*BLACK)
pdf.multi_cell(0,3.8,"Music has a powerful impact on our lives. It can inspire us, help us relax, and bring people together. In many schools, music contests are popular. Students form bands, compose songs, and perform on stage. These activities not only develop their talent but also teach them teamwork and confidence. For example, the “Green Music Festival” in Hanoi last year raised awareness about environmental protection. Many young singers performed songs about nature, and the audience was very supportive. Organizers said, “Music is a great way to spread important messages. When people listen to meaningful lyrics, they remember them longer.” Moreover, music can be eco-friendly. Some artists release digital albums instead of CDs to reduce plastic waste. They also hold charity concerts to support green campaigns.",align='J')
pdf.ln(2)
for q in [
    ("24. What is the main idea of the passage?", ["A. Music contests are expensive.","B. Music has positive effects and can support green campaigns.","C. Hanoi is famous for music.","D. Students don’t like music."]),
    ("25. According to the passage, music contests help students in all the following ways EXCEPT:", ["A. develop talent","B. teach teamwork","C. increase carbon footprint","D. build confidence"]),
    ("26. What does “They” in “They also hold charity concerts…” refer to?", ["A. Students","B. Organizers","C. Artists","D. Singers"]),
    ("27. Why do some artists release digital albums?", ["A. To make more money","B. To reduce plastic waste","C. To become famous","D. To join contests"]),
    ("28. What is TRUE about the Green Music Festival?", ["A. It was held in Ho Chi Minh City.","B. It raised awareness about environment.","C. No audience came.","D. It was only for professional singers."]),
]:
    title, opts = q
    pdf.set_font("DejaVu", "B", 7)
    pdf.set_text_color(*BLACK)
    pdf.set_x(12)
    pdf.multi_cell(0,4,title,align='L')
    pdf.set_font("DejaVu", "", 7)
    for o in opts:
        pdf.set_x(16)
        pdf.cell(0,4,o,align='L')
        pdf.ln(4)
    pdf.ln(1)

# Writing
pdf.set_draw_color(*ORANGE)
pdf.set_fill_color(*ORANGE_LIGHT)
pdf.rect(10, pdf.get_y(), 190, 6, 'DF')
pdf.set_xy(10, pdf.get_y()+1)
pdf.set_font("DejaVu", "B", 8)
pdf.set_text_color(180,80,0)
pdf.cell(190,4,"PART D: WRITING (2.5 điểm)",align='C')
pdf.ln(8)

pdf.set_font("DejaVu", "B", 7.5)
pdf.set_text_color(*ORANGE)
pdf.cell(0,4,"I. Re-ordering – Put the sentences in the correct order. (0.5 điểm – Trắc nghiệm)")
pdf.ln(5)
pdf.set_font("DejaVu", "", 7)
pdf.set_text_color(*BLACK)
pdf.multi_cell(0,3.8,"29. Re-order to make a meaningful conversation:\na. Tom: I’d love to! What time?\nb. Anna: Hi Tom, we’re going to clean up the beach this Saturday. Want to join?\nc. Anna: At 7 a.m. at the school gate. Don’t forget to bring reusable bottles!\nd. Tom: Sure, see you then!\nA. b-a-c-d   B. a-b-c-d   C. b-c-a-d   D. c-b-a-d",align='L')
pdf.ln(2)
pdf.multi_cell(0,3.8,"30. Re-order to make a paragraph about family:\na. Moreover, sharing chores teaches children responsibility.\nb. In my family, everyone shares household chores.\nc. In conclusion, doing housework together strengthens our bonds.\nd. For example, my father cooks meals and my mother does the laundry.\nA. b-d-a-c   B. b-a-d-c   C. d-b-a-c   D. a-b-d-c",align='L')
pdf.ln(3)

pdf.set_font("DejaVu", "B", 7.5)
pdf.set_text_color(*ORANGE)
pdf.cell(0,4,"II. Sentence transformation – Rewrite without changing meaning. (1.0 điểm – Tự luận)")
pdf.ln(5)
pdf.set_font("DejaVu", "", 7.5)
pdf.set_text_color(*BLACK)
trans = [
    "31. My mother makes me do the washing-up every day. → I am _________________________________.",
    "32. They will hold a music contest next month. → A music contest _________________________________.",
    "33. I want to become a singer. I practise every day. → I want to become a singer, so _________________________________.",
    "34. It’s not necessary to bring plastic bags. You can bring reusable ones. → You don’t need _________________________________.",
]
for t in trans:
    pdf.set_x(12)
    pdf.multi_cell(0,4,t,align='L')
    pdf.ln(2)
pdf.set_font("DejaVu", "I", 6.5)
pdf.set_text_color(*GRAY)
pdf.cell(0,3,"Mỗi câu 0.25đ. Giữ nguyên thì, chú ý chia động từ và từ nối.",align='L')
pdf.ln(4)

pdf.set_font("DejaVu", "B", 7.5)
pdf.set_text_color(*ORANGE)
pdf.cell(0,4,"III. Paragraph writing – Write 120–150 words (1.0 điểm)")
pdf.ln(5)
pdf.set_font("DejaVu", "", 7.5)
pdf.set_text_color(*BLACK)
pdf.multi_cell(0,4,"35. Write a paragraph (120–150 words) about ONE of these topics:\n• The benefits of sharing household chores in your family.\n• How to live green and reduce carbon footprint.\n• Your favourite music genre/singer and why you like it.\n\nGợi ý: Mở bài (2 câu) – Thân bài (6–8 câu, có First/Second/For example) – Kết bài (1–2 câu).",align='L')
pdf.ln(2)
# lines for writing
pdf.set_draw_color(*GRAY)
for i in range(12):
    y = pdf.get_y()
    pdf.line(12, y, 198, y)
    pdf.ln(6)
pdf.set_font("DejaVu", "I", 6.5)
pdf.set_text_color(*GRAY)
pdf.cell(0,3,"Giám thị không giải thích gì thêm. Chúc bạn làm bài tốt!",align='C')
pdf.ln(4)

# PRACTICE TEST 2
pdf.section_title("10", "Đề luyện số 2 – Nâng cao & Bẫy khó", "Làm thêm đề này để chắc 9+ – Có nhiều bẫy tinh vi hơn")
pdf.set_font("DejaVu", "I", 7)
pdf.set_text_color(*GRAY)
pdf.cell(0,3,"Đề số 2 tập trung vào từ vựng nâng cao và ngữ pháp dễ nhầm. Thời gian: 60 phút.",align='L')
pdf.ln(4)

pdf.set_font("DejaVu", "B", 7.5)
pdf.set_text_color(*BLUE)
pdf.cell(0,4,"LISTENING (Nghe hiểu – True/False + MCQs – Script bên dưới)")
pdf.ln(5)
pdf.set_font("DejaVu", "I", 6.5)
pdf.set_text_color(*GRAY_DARK)
pdf.multi_cell(0,3.5,"Script L3: “Linda: Our school started an eco-friendly campaign. We collect organic waste to make compost. Students bring reusable bottles, not plastic. Last month, we cleaned a landfill site. It was polluted but now it’s clean. Our teacher said, ‘If we all take responsibility, we can preserve endangered species.’ Next week, we’ll organize a charity concert. All money will support renewable energy projects.”",align='L')
pdf.ln(2)
pdf.set_font("DejaVu", "", 7.5)
pdf.set_text_color(*BLACK)
listen2 = [
    "1. The school makes compost from organic waste. _______",
    "2. Students are encouraged to use plastic bottles. _______",
    "3. They cleaned a landfill site last month. _______",
    "4. The teacher thinks preserving species is impossible. _______",
    "5. Money from the concert will support renewable energy. _______",
    "6. What do students bring instead of plastic? A. Paper bags B. Reusable bottles C. Landfill D. Compost",
    "7. When will they organize a charity concert? A. Last week B. Next week C. Tomorrow D. Yesterday",
    "8. The landfill site is now: A. Polluted B. Clean C. Dangerous D. Empty",
    "9. Who said “take responsibility”? A. Linda B. Teacher C. Students D. Organizers",
    "10. The campaign is: A. Eco-friendly B. Expensive C. Musical D. Traditional",
]
for q in listen2:
    pdf.bullet(q, indent=12, bullet="☐")
pdf.ln(1)

pdf.set_font("DejaVu", "B", 7.5)
pdf.set_text_color(*GREEN)
pdf.cell(0,4,"LANGUAGE – 6 câu MCQs + 2 word forms")
pdf.ln(5)
pdf.set_font("DejaVu", "", 7.5)
pdf.set_text_color(*BLACK)
lang2 = [
    ("11. My dad usually __________ dinner while my mom __________ the dishes.", ["A. cooks / washes","B. cooks / is washing","C. is cooking / washes","D. cooks / does"], "HINT: Hai hành động song song hiện tại đơn?"),
    ("12. __________ you help me take out the rubbish? It’s heavy!", ["A. Are","B. Do","C. Will","D. Are going to"], ""),
    ("13. The song __________ by a famous composer last year. (Bị động quá khứ – mở rộng)", ["A. is composed","B. was composed","C. composes","D. has composed"], ""),
    ("14. She was tired, __________ she continued to practise singing.", ["A. and","B. so","C. but","D. or"], ""),
    ("15. My parents let me __________ my favourite music after finishing chores.", ["A. to listen","B. listen","C. listening","D. listened"], ""),
    ("16. If we __________ plastic, we will reduce pollution. (Bẫy: câu điều kiện loại 1)", ["A. reuse","B. will reuse","C. reused","D. reusable"], ""),
]
for q, opts, hint in lang2:
    pdf.set_font("DejaVu", "B", 7.5)
    pdf.set_x(12)
    pdf.multi_cell(0,4,q,align='L')
    pdf.set_font("DejaVu", "", 7)
    for o in opts:
        pdf.set_x(16)
        pdf.cell(0,4,o,align='L')
        pdf.ln(4)
    if hint:
        pdf.set_font("DejaVu", "I", 6.5)
        pdf.set_text_color(*GRAY)
        pdf.set_x(16)
        pdf.cell(0,3,hint,align='L')
        pdf.set_text_color(*BLACK)
        pdf.ln(4)
    pdf.ln(1)

pdf.set_font("DejaVu", "B", 7.5)
pdf.set_text_color(*GREEN)
pdf.cell(0,4,"Word formation (Tự luận)")
pdf.ln(5)
pdf.set_font("DejaVu", "", 7.5)
pdf.set_text_color(*BLACK)
pdf.bullet("17. This charity concert is very __________ (meaning) for our community.", indent=12)
pdf.bullet("18. He is a very __________ (talent) singer with a beautiful voice.", indent=12)
pdf.ln(2)

pdf.set_font("DejaVu", "B", 7.5)
pdf.set_text_color(*PURPLE)
pdf.cell(0,4,"READING – Cloze + Comprehension")
pdf.ln(5)
pdf.set_font("DejaVu", "", 7)
pdf.set_fill_color(*YELLOW_LIGHT)
pdf.set_draw_color(*YELLOW)
y0 = pdf.get_y()
pdf.rect(12, y0, 186, 32, 'DF')
pdf.set_xy(14,y0+2)
pdf.set_font("DejaVu", "B", 7)
pdf.set_text_color(*BLUE_DARK)
pdf.cell(182,4,"ADVERTISEMENT: MUSIC CONTEST – SHOW YOUR TALENT!",align='C')
pdf.ln(6)
pdf.set_font("DejaVu", "", 6.8)
pdf.set_text_color(*BLACK)
pdf.set_x(14)
pdf.multi_cell(182,3.5,"Are you a (19) __________ singer? Join our contest! You will (20) __________ on stage in front of a large (21) __________. Our professional (22) __________ will give you useful comments. The winner will get a chance to (23) __________ a single. Don’t miss this opportunity!",align='L')
pdf.set_y(y0+32+2)
cloze2 = [
    "19. A. talent   B. talented   C. talentedly   D. talenting",
    "20. A. perform   B. performance   C. performer   D. performing",
    "21. A. viewer   B. audience   C. spectator   D. judge",
    "22. A. judges   B. audiences   C. viewers   D. singers",
    "23. A. release   B. compose   C. cover   D. eliminate",
]
for q in cloze2:
    pdf.set_x(14)
    pdf.cell(0,4,q,align='L')
    pdf.ln(4)
pdf.ln(1)

pdf.set_font("DejaVu", "", 7)
pdf.multi_cell(0,3.8,"Passage: Family life has changed in recent years. In the past, the father was the only breadwinner and the mother was the homemaker. Children didn’t have to do chores. Today, both parents work and children share housework. This teaches them responsibility and gratitude. Studies show that families who share chores have stronger bonds and less stress. For instance, when teenagers help prepare meals or take out rubbish, they understand the value of hard work. Some families even have weekly meetings to divide chores fairly. Although there are sometimes arguments, most families agree that sharing is important.",align='J')
pdf.ln(2)
comp2 = [
    ("24. What is the main idea?", ["A. Fathers are breadwinners","B. Family life has changed; sharing chores brings benefits","C. Children should not do chores","D. Mothers do not work"]),
    "25. In the past, who did chores? A. Children B. Father only C. Mother mainly D. No one mentioned",
    "26. What does 'They' in 'They understand...' refer to? A. Parents B. Teenagers C. Families D. Studies",
    "27. Sharing chores helps teenagers: A. Avoid responsibility B. Understand hard work C. Become breadwinners D. Not study",
    "28. What is TRUE? A. Sharing chores causes more stress B. Weekly meetings help divide chores C. All families argue daily D. Past families shared chores more",
]
for q in comp2:
    if isinstance(q, tuple):
        title, opts = q
        pdf.set_font("DejaVu", "B", 7)
        pdf.set_x(12)
        pdf.multi_cell(0,4,title,align='L')
        pdf.set_font("DejaVu", "", 7)
        for o in opts:
            pdf.set_x(16)
            pdf.cell(0,4,o,align='L')
            pdf.ln(4)
        pdf.ln(1)
    else:
        pdf.set_font("DejaVu", "B", 7)
        pdf.set_x(12)
        pdf.multi_cell(0,4,q,align='L')
        pdf.ln(1)

pdf.set_font("DejaVu", "B", 7.5)
pdf.set_text_color(*ORANGE)
pdf.cell(0,4,"WRITING – Re-ordering + Transformation + Paragraph")
pdf.ln(5)
pdf.set_font("DejaVu", "", 7)
pdf.multi_cell(0,3.8,"29. a. Finally, we decided to reduce plastic use.\nb. First, we discussed environmental problems.\nc. Second, we made a plan to clean the beach.\nd. Our class had a meeting about green living.\nA. d-b-c-a   B. d-c-b-a   C. b-d-c-a   D. a-d-b-c\n\n30. a. I love listening to folk music.\nb. It helps me relax after a long day.\nc. My grandmother taught me many folk songs.\nd. Moreover, its lyrics are meaningful.\nA. a-b-d-c   B. a-b-c-d   C. c-a-b-d   D. a-c-d-b",align='L')
pdf.ln(2)
pdf.set_font("DejaVu", "", 7.5)
pdf.set_text_color(*BLACK)
trans2 = [
    "31. People believe that music brings people together. → Music is _________________________________. (Bị động)",
    "32. She wants to help the environment, so she recycles daily. → She recycles daily because _________________________________.",
    "33. My teacher made us clean the classroom. → We were _________________________________.",
    "34. It’s interesting to learn about different music genres. → Learning _________________________________ is interesting.",
]
for t in trans2:
    pdf.set_x(12)
    pdf.multi_cell(0,4,t,align='L')
    pdf.ln(2)
pdf.set_font("DejaVu", "I", 6.5)
pdf.set_text_color(*GRAY)
pdf.cell(0,3,"35. Paragraph (120–150 từ): “How do you share chores in your family?” hoặc “A music show you like”.",align='L')
pdf.ln(4)
for i in range(10):
    pdf.line(12, pdf.get_y(), 198, pdf.get_y())
    pdf.ln(6)

# ANSWERS
pdf.section_title("11", "Đáp án & Giải thích chi tiết – Đề số 1", "Tự chấm – Hiểu tại sao đúng/sai – Ghi lỗi vào sổ")
pdf.set_font("DejaVu", "I", 7)
pdf.set_text_color(*GRAY)
pdf.cell(0,3,"Thang điểm: Mỗi câu TN 0.25đ x 28 = 7đ. Tự luận: 17,18 (0.25đ/câu), 31–34 (0.25đ/câu), 35 (1.0đ). Tổng 10đ.",align='L')
pdf.ln(4)

pdf.sub_title("LISTENING – Đáp án", BLUE)
pdf.set_font("DejaVu", "", 7.5)
pdf.set_text_color(*BLACK)
pdf.multi_cell(0,4,"Listening 1 (True/False): 1. F (Minh doesn’t know) | 2. T (usually on Sundays) | 3. F (sister is preparing meals, not washing-up) | 4. T (always share) | 5. F (father still helps – “still helps” = có giúp).",align='L')
pdf.ln(1)
pdf.multi_cell(0,4,"Listening 2 (MCQs): 6. A (Teen Music Stars) | 7. B (five teenagers) | 8. B (Audience will vote) | 9. C (award and a single) | 10. B (8 p.m.).",align='L')
pdf.ln(1)
pdf.tip_box("Giải thích bẫy Listening", "Câu 3: Nghe “sister is preparing meals” nhưng câu hỏi nói “washing-up” → False. Câu 5: “breadwinner, but he still helps” → phủ định “never helps” là sai → False.", fill=BLUE_LIGHT, border=BLUE, icon="*")

pdf.sub_title("LANGUAGE – Đáp án & Giải thích", GREEN)
lang_ans = [
    ("11. A – do the heavy lifting là collocation cố định (do, không phải make).", "do heavy lifting / do laundry / do chores – đều dùng “do”."),
    ("12. B – reduce carbon footprint (giảm dấu chân carbon). “cut down on” cũng đúng nhưng đề cho B chuẩn hơn.", "reduce = làm giảm, increase = tăng (trái nghĩa)."),
    ("13. B – is performing (Look! → hiện tại tiếp diễn).", "Dấu hiệu Look! + hành động đang diễn ra → be + V-ing."),
    ("14. B – am going to join (đã đăng ký = kế hoạch có trước).", "will là quyết định tức thì, không phù hợp với “already registered”."),
    ("15. B – is collected (Passive hiện tại đơn: Trash (không đếm được) + is + V3).", "Chủ ngữ số ít → is, are sai nếu dùng “are”."),
    ("16. C – but (tương phản: I love pop BUT brother prefers classical).", "and (thêm), so (kết quả), or (lựa chọn) đều sai nghĩa."),
    ("17. impressive (adj.) – Sau “very” + tính từ. impress → impressive (ấn tượng).", "Cấu trúc: very + adj. → impressive, không phải impressively (adv.)."),
    ("18. awareness (n.) – Sau “raise” cần danh từ: raise awareness (nâng cao nhận thức).", "aware (adj.) → awareness (n.)."),
]
for title, expl in lang_ans:
    pdf.set_font("DejaVu", "B", 7)
    pdf.set_text_color(*GREEN)
    pdf.set_x(12)
    pdf.multi_cell(0,3.5,title,align='L')
    pdf.set_font("DejaVu", "I", 6.5)
    pdf.set_text_color(*GRAY_DARK)
    pdf.set_x(16)
    pdf.multi_cell(0,3.2, expl,align='L')
    pdf.ln(1)

pdf.sub_title("READING – Đáp án", PURPLE)
pdf.set_font("DejaVu", "", 7.5)
pdf.set_text_color(*BLACK)
pdf.multi_cell(0,4,"Cloze (19–23): 19. C (environmental campaign – adj + N) | 20. A (recycle plastic waste – collocation) | 21. A (endangered species – cụm cố định) | 22. A (take part in – cụm động từ) | 23. B (sustainable – adj sau “more”).",align='L')
pdf.ln(1)
pdf.multi_cell(0,4,"Comprehension (24–28): 24. B (Music’s positive effects & green) | 25. C (increase carbon footprint – không phải lợi ích) | 26. C (They = Artists – câu trước: Some artists…) | 27. B (reduce plastic waste) | 28. B (raised awareness about environment).",align='L')
pdf.ln(1)
pdf.tip_box("Bẫy Reading", "Câu 22: “take part in” không phải “join part” hay “make part”. Câu 26: “They” = Artists (số nhiều, gần nhất), không phải Students.", fill=PURPLE_LIGHT, border=PURPLE, icon="*")

pdf.sub_title("WRITING – Đáp án", ORANGE)
pdf.set_font("DejaVu", "", 7.5)
pdf.set_text_color(*BLACK)
pdf.multi_cell(0,4,"Re-ordering: 29. A (b-a-c-d) – Anna mời → Tom nhận lời → Anna báo giờ → Tom hẹn gặp. | 30. A (b-d-a-c) – Mở (In my family…) → Ví dụ (For example…) → Moreover… → Kết (In conclusion…).",align='L')
pdf.ln(1)
pdf.set_font("DejaVu", "B", 7)
pdf.set_text_color(*ORANGE)
pdf.cell(0,4,"Transformation – 4 câu mẫu (chấp nhận cách diễn đạt tương đương đúng ngữ pháp):")
pdf.ln(4)
pdf.set_font("DejaVu", "", 7.5)
pdf.set_text_color(*BLACK)
trans_ans = [
    "31. I am made to do the washing-up every day (by my mother). ← Passive từ “My mother makes me do…” → “I am made to do…” (lưu ý: make → made + to).",
    "32. A music contest will be held next month (by them). ← Passive tương lai: will be + V3. Giữ “next month”.",
    "33. I want to become a singer, so I practise every day. ← Đã cho sẵn, giữ nguyên (hoặc “...so I practise hard”). Chú ý dấu phẩy trước “so” khi là câu ghép.",
    "34. You don’t need to bring plastic bags. You can bring reusable ones. ← don’t need to V = It’s not necessary to V. (Hoặc: You needn’t bring…).",
]
for ans in trans_ans:
    pdf.set_x(12)
    pdf.multi_cell(0,3.8, f"• {ans}",align='L')
    pdf.ln(1)

pdf.set_font("DejaVu", "B", 7)
pdf.set_text_color(*RED)
pdf.cell(0,4,"Lưu ý chấm Transformation: Sai chia động từ (-0.25), sai trật tự (-0.25), thiếu “by” vẫn được điểm nếu nghĩa không đổi.")
pdf.ln(5)

pdf.sub_title("Paragraph – Thang chấm 1.0đ", ORANGE)
pdf.set_font("DejaVu", "", 7)
col_para = [50,40,100]
pdf.table_header(col_para, ["TIÊU CHÍ","ĐIỂM","YÊU CẦU"])
para_rows = [
    ["Bố cục\n(Mở-Thân-Kết)","0.25","Có đủ 3 phần, dùng First/Second/Finally/In conclusion"],
    ["Nội dung\n(đúng chủ đề)","0.25","Đủ ý, có ví dụ cụ thể, không lạc đề"],
    ["Ngôn ngữ\n(từ vựng/ngữ pháp)","0.25","Dùng từ vựng Unit 1–3, ít nhất 1 câu ghép, 1 câu bị động/to-inf"],
    ["Chính tả & Độ dài","0.25","120–150 từ, ít lỗi chính tả, chữ dễ đọc"],
]
for idx, r in enumerate(para_rows):
    fills = [ORANGE_LIGHT if idx%2==0 else WHITE]*3
    pdf.table_row(col_para, r, fills=fills, align_list=['C','C','L'], font_size=6.8)
pdf.ln(2)
pdf.set_font("DejaVu", "I", 6.5)
pdf.set_text_color(*GRAY)
pdf.cell(0,3,"Xem bài mẫu đạt 1.0đ ở trang sau để học theo.",align='L')
pdf.ln(4)

# ANSWERS DE 2
pdf.section_title("12", "Đáp án đề số 2 & Bài mẫu Writing", "Học từ bài mẫu – chép tay để nhớ collocations")
pdf.sub_title("Đáp án đề số 2 (rút gọn)", GREEN)
pdf.set_font("DejaVu", "", 7)
pdf.set_text_color(*BLACK)
pdf.multi_cell(0,3.8,"Listening: 1.T  2.F (not plastic -> reusable)  3.T  4.F (teacher says we CAN preserve)  5.T  |  6.B  7.B  8.B  9.B  10.A",align='L')
pdf.ln(1)
pdf.multi_cell(0,3.8,"Language: 11.A (cooks/washes - thoi quen song song)  12.C (Will you...? - loi de nghi)  13.B (was composed - qua khu)  14.C (but - tuong phan)  15.B (let sb V - bare-inf)  16.A (If + present simple, will...)",align='L')
pdf.ln(1)
pdf.multi_cell(0,3.8,"          17. meaningful  18. talented",align='L')
pdf.ln(1)
pdf.multi_cell(0,3.8,"Reading: 19.B (talented - adj)  20.A (perform - V)  21.B (audience)  22.A (judges)  23.A (release)  |  24.B  25.C  26.B  27.B  28.B",align='L')
pdf.ln(1)
pdf.multi_cell(0,3.8,"Writing: 29.A (d-b-c-a)  30.A (a-b-d-c)  |  31. Music is believed to bring people together.  32. ...because she wants to help...  33. We were made to clean... (to!)  34. Learning about ... is interesting.",align='L')
pdf.ln(2)

pdf.sub_title("3 Bài mẫu Writing đạt điểm tối đa (120–150 từ)", BLUE_DARK)
pdf.set_font("DejaVu", "I", 7)
pdf.set_text_color(*GRAY)
pdf.cell(0,3,"Bạn chỉ cần học 1 bài tủ theo chủ đề mình thích nhất. Khi thi, thay tên/ví dụ cho phù hợp.",align='L')
pdf.ln(3)

# Sample 1
pdf.set_fill_color(*BLUE_LIGHT)
pdf.set_draw_color(*BLUE)
y0 = pdf.get_y()
pdf.rect(10, y0, 190, 36, 'DF')
pdf.set_xy(12, y0+2)
pdf.set_font("DejaVu", "B", 7.5)
pdf.set_text_color(*BLUE_DARK)
pdf.cell(0,4,"BÀI MẪU 1: The benefits of sharing household chores (Family Life) – 142 từ – Band 9/10",align='L')
pdf.set_xy(12, y0+7)
pdf.set_font("DejaVu", "", 7)
pdf.set_text_color(*BLACK)
pdf.multi_cell(186,3.5,"In my family, everyone shares household chores. My father is the breadwinner, but he still helps with cooking and taking out the rubbish. My mother does the laundry and prepares meals, while my sister and I wash the dishes and mop the house. First, sharing chores teaches us responsibility and gratitude. We understand how hard our parents work. Second, it strengthens family bonds because we spend quality time together and support each other. For example, we often talk and laugh while doing chores. Moreover, it reduces the financial burden because we don’t need to hire helpers. In conclusion, sharing housework is very important. I think every family should do it.",align='J')
pdf.set_y(y0+36+2)
pdf.set_font("DejaVu", "I", 6.5)
pdf.set_text_color(*GREEN)
pdf.cell(0,3,"Từ vựng đắt: breadwinner, strengthen bonds, quality time, financial burden | Ngữ pháp: Present simple, compound (while, because, Moreover), passive (are made – ẩn)",align='L')
pdf.ln(4)

# Sample 2
pdf.set_fill_color(*GREEN_LIGHT)
pdf.set_draw_color(*GREEN)
y0 = pdf.get_y()
# need to check page break
if y0 > 240:
    pdf.add_page()
    y0 = pdf.get_y()
pdf.rect(10, y0, 190, 38, 'DF')
pdf.set_xy(12, y0+2)
pdf.set_font("DejaVu", "B", 7.5)
pdf.set_text_color(22,90,60)
pdf.cell(0,4,"BÀI MẪU 2: How to live green and reduce carbon footprint (Environment) – 138 từ",align='L')
pdf.set_xy(12, y0+7)
pdf.set_font("DejaVu", "", 7)
pdf.set_text_color(*BLACK)
pdf.multi_cell(186,3.5,"Living green is essential to protect our environment. First, we should reduce our carbon footprint by using public transport or riding bicycles instead of driving cars. This helps reduce CO2 emissions and air pollution. Second, we need to recycle and reuse as much as possible. For instance, we can reuse plastic bottles and recycle paper to avoid landfill waste. Third, we should save energy by turning off lights and using renewable energy like solar power. Moreover, we can join clean-up campaigns and plant more trees to preserve endangered species and fight climate change. These actions are eco-friendly and sustainable. In conclusion, everyone should take responsibility for the planet. If we live green now, our future will be better.",align='J')
pdf.set_y(y0+38+2)
pdf.set_font("DejaVu", "I", 6.5)
pdf.set_text_color(*GREEN)
pdf.cell(0,3,"Từ vựng đắt: carbon footprint, emissions, landfill, renewable, endangered, sustainable | Ngữ pháp: should + V, passive (are planted – ẩn), compound (and, Moreover), to-inf (to protect)",align='L')
pdf.ln(4)

# Sample 3
pdf.set_fill_color(*PURPLE_LIGHT)
pdf.set_draw_color(*PURPLE)
y0 = pdf.get_y()
if y0 > 240:
    pdf.add_page()
    y0 = pdf.get_y()
pdf.rect(10, y0, 190, 38, 'DF')
pdf.set_xy(12, y0+2)
pdf.set_font("DejaVu", "B", 7.5)
pdf.set_text_color(*PURPLE)
pdf.cell(0,4,"BÀI MẪU 3: My favourite music genre/singer (Music) – 135 từ",align='L')
pdf.set_xy(12, y0+7)
pdf.set_font("DejaVu", "", 7)
pdf.set_text_color(*BLACK)
pdf.multi_cell(186,3.5,"My favourite music genre is pop because it is energetic and inspiring. My favourite singer is Hoang Thuy Linh, who is very talented and beautiful. She composes meaningful lyrics and performs brilliantly on stage. I love her songs because they have catchy melodies and positive messages. For example, her single “See Tinh” became very popular and won many awards. Moreover, she often holds charity concerts to support disadvantaged children, which is very admirable. Listening to her music helps me relax after a long day and inspires me to work hard. Pop music also brings people together; my family and I often sing along at weekends. In conclusion, music is an important part of my life, and I will continue to support my favourite singer.",align='J')
pdf.set_y(y0+38+2)
pdf.set_font("DejaVu", "I", 6.5)
pdf.set_text_color(*PURPLE)
pdf.cell(0,3,"Từ vựng đắt: genre, talented, compose, lyrics, single, award, charity concert, melody | Ngữ pháp: because, Moreover, who (mệnh đề quan hệ), will (tương lai)",align='L')
pdf.ln(4)

pdf.tip_box("Cách học bài mẫu", "Bước 1: Chép tay 1 bài (15 phút). Bước 2: Gạch chân collocations (màu xanh). Bước 3: Gấp vở lại, tự viết lại từ trí nhớ. Bước 4: So sánh, sửa lỗi. Làm 3 lần là thuộc!", fill=YELLOW_LIGHT, border=YELLOW, icon=">")

# Checklist
pdf.section_title("13", "Checklist trước ngày thi & Mẹo nhớ nhanh", "In trang này dán lên bàn học – Tick mỗi ngày")
# Checklist table
pdf.sub_title("Checklist 15 mục – Đã xong thì tick ✓", GREEN)
items = [
    "Thuộc 20 từ Unit 1 (Family) + đặt được 5 câu ví dụ",
    "Thuộc 20 từ Unit 2 (Environment) + 3R (Reduce-Reuse-Recycle)",
    "Thuộc 20 từ Unit 3 (Music) + chuỗi contest→audience→award",
    "Phân biệt được Present Simple vs Continuous (now vs usually)",
    "Phân biệt will (quyết định nhanh) vs be going to (kế hoạch)",
    "Chia được Passive hiện tại đơn: S + am/is/are + V3",
    "Dùng đúng and/but/or/so + dấu phẩy trước liên từ",
    "Nhớ make/let + O + V (bare-inf) vs want + to V",
    "Làm đúng Cloze: nhìn trước/sau chỗ trống, collocation",
    "Làm đúng Comprehension: tìm ý chính, tham chiếu It/They",
    "Sắp xếp Re-ordering đúng thứ tự hội thoại/đoạn văn",
    "Viết lại câu Transformation không sai thì, đủ từ",
    "Thuộc template Paragraph 3 phần (Mở-Thân-Kết) + 6 từ nối",
    "Làm xong Đề 1 (60 phút) đạt ≥ 7.5đ",
    "Làm xong Đề 2 (60 phút) đạt ≥ 8.0đ",
]
# draw checklist
for idx, it in enumerate(items):
    y = pdf.get_y()
    if y > 270:
        pdf.add_page()
    pdf.set_draw_color(*GREEN)
    pdf.set_fill_color(*WHITE)
    pdf.rect(12, y, 6, 6, 'D')
    pdf.set_xy(20, y)
    pdf.set_font("DejaVu", "", 7.5)
    pdf.set_text_color(*BLACK)
    pdf.cell(0,6, f"{idx+1:02d}.  {it}", align='L')
    pdf.ln(7)

pdf.ln(2)
pdf.sub_title("Mẹo nhớ nhanh trong phòng thi (5 phút cuối)", BLUE_DARK)
pdf.set_font("DejaVu", "", 7.5)
tips = [
    "Đọc lại 6 câu Language: có “now/Look!” → Continuous; có “always/usually” → Simple; có “be going to” → kế hoạch.",
    "Passive: thấy “by” → nghĩ ngay be + V3. Kiểm tra S số ít/nhiều để chọn is/are.",
    "Compound: trước and/but/or/so phải có dấu phẩy + mệnh đề. Không có phẩy mà chỉ có cụm từ → không phải câu ghép.",
    "To-inf/Bare-inf: make/let + O + V (không to). Muốn kiểm tra: bị động “am made to V” lại có “to” – nhớ bẫy này!",
    "Writing paragraph: đếm từ (mỗi dòng ~10 từ, 13–15 dòng = 130–150 từ). Thiếu từ → thêm 1 câu ví dụ “For example,…”.",
    "Listening: nếu không nghe được, chọn đáp án chứa từ bạn NGHE THẤY (thường đúng 60%). Đừng bỏ trống!",
]
for t in tips:
    pdf.bullet(t, indent=12, bullet="→", bullet_color=BLUE)

pdf.tip_box("Lời dặn cuối cùng", "Bạn không cần học hết 1000 từ – chỉ cần 60 từ cốt lõi trong tài liệu này + 6 công thức ngữ pháp + 2 đề luyện là đủ 8+. Ngủ đủ giấc trước thi, mang bút chì 2B, tẩy, đồng hồ. Vào phòng thi: hít thở sâu 3 lần, đọc kỹ đề, làm câu dễ trước. Chúc bạn đạt 9–10 và tận hưởng việc học tiếng Anh!", fill=BLUE_LIGHT, border=BLUE, icon="*")

pdf.ln(2)
pdf.set_font("DejaVu", "B", 7)
pdf.set_text_color(*BLUE_DARK)
pdf.cell(0,4,"Tài liệu được biên soạn bám sát Ma trận & Bảng đặc tả chính thức 2026–2027. Mọi thắc mắc góp ý vui lòng liên hệ giáo viên bộ môn.",align='C')
pdf.ln(4)
pdf.set_font("DejaVu", "", 6.5)
pdf.set_text_color(*GRAY)
pdf.cell(0,3,"© 2026 Nhóm biên soạn Tiếng Anh 10 – Lưu hành nội bộ. Không sao chép vì mục đích thương mại.",align='C')
pdf.ln(3)
pdf.set_font("DejaVu", "I", 6.5)
pdf.set_text_color(*GRAY)
pdf.cell(0,3,"In màu khổ A4 – Đóng gáy – Dán checklist lên bàn học – Chúc bạn thi tốt!",align='C')

# Save
pdf.output(OUT)
print(f"PDF generated: {OUT} – {pdf.pages_count} pages")

