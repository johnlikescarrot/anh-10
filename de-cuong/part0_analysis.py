# -*- coding: utf-8 -*-
"""Phần mở đầu: hướng dẫn sử dụng + phân tích chuyên sâu ma trận."""
from common import *

def build():
    f = []
    # ---------------- Cách dùng tài liệu ----------------
    f.append(band("HƯỚNG DẪN SỬ DỤNG TÀI LIỆU", TEAL))
    f.append(spacer(6))
    f.append(P("Tài liệu này được biên soạn <b>trực tiếp từ Ma trận và Bảng đặc tả đề kiểm tra "
               "giữa học kỳ 1 năm học 2026–2027 môn Tiếng Anh 10</b> (sách <i>Global Success</i>). "
               "Mọi nội dung ôn tập, mọi dạng bài luyện tập đều bám đúng: chủ đề, chủ điểm ngữ pháp, "
               "dạng câu hỏi, số câu và mức độ nhận thức mà ma trận quy định — không ôn thừa, không ôn thiếu."))
    f.append(P("<b>Cách học hiệu quả nhất với tài liệu này:</b>", "p"))
    for t in [
        "<b>Bước 1 – Đọc Phần 0</b> để hiểu “luật chơi”: đề thi lấy điểm ở đâu, phần nào dễ mất điểm nhất.",
        "<b>Bước 2 – Học Phần I</b> theo từng Unit và từng chủ điểm ngữ pháp. Sau mỗi mục nhỏ có ô <b>“Mẹo nhớ”</b> và <b>“Bẫy thường gặp”</b> — hãy đọc kỹ hai ô này, đây là nơi phân hóa điểm số.",
        "<b>Bước 3 – Làm Phần II</b> (luyện theo từng dạng bài), tự chấm bằng đáp án ở Phần IV, ghi lại lỗi sai vào “Nhật ký lỗi sai” ở Phụ lục.",
        "<b>Bước 4 – Làm Đề thi thử (Phần III)</b> trong điều kiện như thi thật: bấm giờ, không tra từ điển. Đây là đề mô phỏng đúng 100% cấu trúc ma trận.",
        "<b>Bước 5</b> – Đối chiếu đáp án – giải thích, ôn lại đúng những điểm còn sai, đọc lại bài văn mẫu.",
    ]:
        f.append(bullet(t))
    f.append(spacer(2))
    f.append(box("KÝ HIỆU DÙNG TRONG TÀI LIỆU",
                 ["<b>B</b> = Biết (nhận biết) &nbsp;•&nbsp; <b>H</b> = Hiểu &nbsp;•&nbsp; <b>VD</b> = Vận dụng &nbsp;•&nbsp; "
                  "<b>TN</b> = Trắc nghiệm &nbsp;•&nbsp; <b>TL</b> = Tự luận &nbsp;•&nbsp; <b>(n)</b> = danh từ, <b>(v)</b> = động từ, "
                  "<b>(adj)</b> = tính từ, <b>(adv)</b> = trạng từ. &nbsp; Dấu / … / là phiên âm quốc tế (IPA)."],
                 bg=LIGHT, border=NAVY))
    f.append(spacer(6))
    f.append(P("<b>Lộ trình ôn tập gợi ý trong 7 ngày</b> (mỗi ngày 60–90 phút):", "p"))
    f.append(table([
        ["Ngày", "Nội dung ôn", "Mục tiêu"],
        ["Ngày 1", "Đọc Phần 0 + Từ vựng Unit 1 & Ngữ pháp 1 (Hiện tại đơn / tiếp diễn)", "Nắm cấu trúc đề; thuộc 20 từ Unit 1"],
        ["Ngày 2", "Từ vựng Unit 2 + Ngữ pháp 2–3 (<i>will/be going to</i>, Câu bị động)", "Phân biệt được 2 cách nói tương lai"],
        ["Ngày 3", "Từ vựng Unit 3 + Ngữ pháp 4–5 (Câu ghép; <i>to-inf / bare inf</i>)", "Hoàn tất 5 chủ điểm ngữ pháp"],
        ["Ngày 4", "Làm bài luyện Từ vựng + Ngữ pháp (Phần II, mục A–C)", "Độ chính xác ≥ 80%"],
        ["Ngày 5", "Luyện Listening + Reading (Phần II, mục D–F) + học khung Writing", "Quen tốc độ nghe, kỹ thuật đọc"],
        ["Ngày 6", "Luyện Writing (Phần II, mục G–H) + học thuộc 3 dàn ý đoạn văn", "Viết được đoạn 120–150 từ"],
        ["Ngày 7", "Làm Đề thi thử (Phần III) bấm giờ → chấm → chữa kỹ", "Đạt mục tiêu điểm đã đặt"],
    ], [22*mm, 95*mm, W-117*mm]))
    f.append(spacer(8))

    # ---------------- PHẦN 0 ----------------
    f.append(band("PHẦN 0 — PHÂN TÍCH CHUYÊN SÂU MA TRẬN ĐỀ THI", NAVY))
    f.append(spacer(6))
    f.append(P("0.1. Cấu trúc tổng thể của đề thi", "h2"))
    f.append(P("Đề kiểm tra giữa kỳ 1 môn Tiếng Anh 10 năm học 2026–2027 có tổng điểm <b>10</b>, gồm "
               "<b>28 câu trắc nghiệm (7,0 điểm — mỗi câu 0,25 điểm)</b> và <b>phần tự luận 3,0 điểm</b> "
               "(6 câu nhỏ + 1 bài viết đoạn văn). Bốn kỹ năng/nội dung được phân bổ đều nhau — mỗi phần đúng <b>25%</b>:"))
    f.append(table([
        ["Phần", "Nội dung", "Số câu", "Điểm", "Tỉ lệ", "Hình thức"],
        ["1. LISTENING", "Listening 1: nghe hội thoại/độc thoại ~1,5 phút (180–200 từ), dạng True/False hoặc tương tự", "5", "1,25", "12,5%", "TN"],
        ["", "Listening 2: nghe hội thoại/độc thoại ~1,5 phút (180–200 từ), dạng MCQ hoặc tương tự", "5", "1,25", "12,5%", "TN"],
        ["2. LANGUAGE — Vocabulary", "Từ vựng Units 1–2–3 (Family life; Humans and the environment; Music)", "2 TN + 2 TL", "1,5", "15%", "TN + TL"],
        ["2. LANGUAGE — Grammar", "5 chủ điểm ngữ pháp Units 1–2–3", "4 TN", "1,0", "10%", "TN"],
        ["3. READING", "Reading 1 — Cloze text: đọc tờ rơi/quảng cáo, điền từ vào chỗ trống", "5", "1,25", "12,5%", "TN"],
        ["", "Reading 2 — Reading comprehension: đoạn văn 220–250 từ, trả lời MCQ", "5", "1,25", "12,5%", "TN"],
        ["4. WRITING", "Writing 1 — Re-ordering: sắp xếp câu thành hội thoại/thư/đoạn văn", "2", "0,5", "5%", "TN"],
        ["", "Writing 2 — Sentence transformation: viết lại câu đồng nghĩa", "4", "1,0", "10%", "TL"],
        ["", "Writing 3 — Writing paragraph: viết đoạn văn 120–150 từ", "1 bài", "1,0", "10%", "TL"],
        ["<b>TỔNG</b>", "", "<b>28 TN + 6 câu TL + 1 bài viết</b>", "<b>10,0</b>", "<b>100%</b>", ""],
    ], [30*mm, 62*mm, 26*mm, 14*mm, 15*mm, W-147*mm], align_center_cols={2,3,4,5}))
    f.append(P("<i>Ghi chú: trong văn bản gốc, một vài ô của bảng ma trận có lỗi trình bày nhỏ (ví dụ một ô thừa số “1” "
               "ở phần Listening của Bảng đặc tả, hay dòng tổng tự luận ghi “3 (TL)”). Các số liệu trong tài liệu này đã được "
               "chuẩn hóa theo tổng nhất quán của chính ma trận: 28 câu TN = 7,0 điểm; tự luận = 3,0 điểm; tổng 10 điểm.</i>", "small"))

    f.append(P("0.2. Phân tích theo mức độ nhận thức", "h2"))
    f.append(table([
        ["Mức độ", "Tỉ lệ / Điểm", "Xuất hiện ở đâu trong đề?", "Ý nghĩa khi ôn tập"],
        ["<b>BIẾT</b> (nhận biết, nhớ lại)", "40% — 4,0 điểm", "Listening (6/10 câu lấy chi tiết); Vocabulary TN; Grammar TN; Reading cloze; Writing 1 (re-ordering)", "Đây là “điểm nền” — chỉ cần thuộc từ vựng, nắm công thức ngữ pháp và nghe được thông tin chi tiết là lấy trọn."],
        ["<b>HIỂU</b> (phân biệt, suy luận gần)", "30% — 3,0 điểm", "Listening (4/10 câu hỏi ý chính); Vocabulary TN; Grammar TN; Reading comprehension (ý chính, tham chiếu, loại trừ chi tiết)", "Đòi hỏi hiểu bản chất, phân biệt các phương án gần giống nhau — luyện bằng cách làm bài có giải thích."],
        ["<b>VẬN DỤNG</b> (dùng kiến thức để tạo sản phẩm)", "30% — 3,0 điểm", "<b>Toàn bộ nằm ở tự luận:</b> 2 câu vận dụng từ vựng (1,0đ) + Writing 2 viết lại câu (1,0đ) + Writing 3 viết đoạn văn (1,0đ)", "Muốn đạt điểm cao (8+) bắt buộc phải <b>viết được</b>. Đây là phần phân hóa học sinh giỏi."],
    ], [38*mm, 26*mm, 52*mm, W-116*mm]))
    f.append(box("NHẬN ĐỊNH CHUYÊN SÂU SỐ 1 — “ĐIỂM VẬN DỤNG NẰM HẾT Ở PHẦN VIẾT”",
                 ["Cả 3,0 điểm mức Vận dụng đều thuộc phần tự luận. Hệ quả rất quan trọng: một học sinh làm đúng "
                  "<b>toàn bộ 28 câu trắc nghiệm (7,0đ)</b> nhưng bỏ trắng phần viết lại câu và đoạn văn thì cũng chỉ đạt khoảng <b>7,0–7,5 điểm</b>. "
                  "Ngược lại, chỉ cần viết đúng 2/4 câu transformation và một đoạn văn tạm ổn, học sinh đã “mở khóa” thêm 1,5–2,0 điểm. "
                  "<b>Chiến lược: không bao giờ bỏ trống phần tự luận.</b>"],
                 bg=LIGHT2, border=ORANGE))
    f.append(spacer(4))
    f.append(box("NHẬN ĐỊNH CHUYÊN SÂU SỐ 2 — NGỮ PHÁP “ÍT CÂU NHƯNG LAN TỎA”",
                 ["Phần Grammar trắc nghiệm chỉ có 4 câu (1,0đ) cho 5 chủ điểm, nhưng cùng 5 chủ điểm đó lại là “nguyên liệu” "
                  "của Writing 2 (viết lại câu, 1,0đ) và xuất hiện dày đặc trong Reading cloze. Như vậy ngữ pháp thực chất ảnh hưởng tới "
                  "khoảng <b>3,0–3,5 điểm</b> của cả bài thi. Ôn chắc 5 chủ điểm ở Phần I là khoản đầu tư có lợi nhất."],
                 bg=LIGHT3, border=GREEN))
    f.append(spacer(4))
    f.append(box("NHẬN ĐỊNH CHUYÊN SÂU SỐ 3 — NHỮNG GÌ <b>KHÔNG</b> CÓ TRONG ĐỀ (theo ma trận)",
                 ["Ma trận <b>không</b> có: phần thi Nói (Speaking); mục riêng về phát âm/trọng âm (Pronunciation); "
                  "kiến thức ngoài Units 1–3; thì quá khứ hoàn thành, câu điều kiện… Vì vậy hãy tập trung 100% sức lực vào "
                  "3 Unit và 5 chủ điểm ngữ pháp đã liệt kê — đó là cách ôn “đúng trọng tâm” nhất."],
                 bg=LIGHT, border=NAVY))

    f.append(P("0.3. Phạm vi kiến thức chính thức (theo Bảng đặc tả)", "h2"))
    f.append(table([
        ["Khối", "Nội dung cụ thể", "Dạng bài / Yêu cầu"],
        ["Chủ đề (dùng cho Listening, Reading, Writing 3)", "Unit 1: <b>Family life</b> • Unit 2: <b>Humans and the environment</b> • Unit 3: <b>Music</b>", "Nghe 180–200 từ/1,5 phút; đọc 220–250 từ; viết đoạn 120–150 từ"],
        ["Vocabulary", "Toàn bộ từ vựng theo 3 chủ điểm trên (SGK <i>Global Success 10</i>, Units 1–3)", "TN: nhận ra/phân biệt từ trong ngữ cảnh. TL (VD): dùng đúng dạng của từ trong câu"],
        ["Grammar", "1) Present simple & present continuous &nbsp; 2) <i>will</i> & <i>be going to</i> &nbsp; 3) Passive voice &nbsp; 4) Compound sentences &nbsp; 5) To-infinitive & bare infinitive", "TN: nhận ra và phân biệt. TL: vận dụng khi viết lại câu và viết đoạn"],
        ["Reading 1 (Cloze)", "Tờ rơi / quảng cáo về 3 chủ đề trên, điền từ vào 5 chỗ trống", "Kiểm tra từ vựng, ngữ pháp, liên kết văn bản (từ nối, đại từ…)"],
        ["Reading 2", "Đoạn văn 220–250 từ về 3 chủ đề trên", "Ý chính, chi tiết, nghĩa tham chiếu (reference), loại trừ phương án sai"],
        ["Writing 1", "Sắp xếp các câu đơn lẻ thành hội thoại / lá thư / đoạn văn đúng trật tự", "2 câu TN — nhận diện cấu trúc hội thoại, thư, đoạn văn"],
        ["Writing 2", "Viết lại câu sao cho nghĩa không đổi", "4 câu TL — dùng đúng cấu trúc đã học"],
        ["Writing 3", "Viết đoạn văn/thư/bài báo 120–150 từ bày tỏ quan điểm về 1 trong 3 chủ đề", "1 bài — chấm theo nội dung, tổ chức ý, từ vựng, ngữ pháp"],
    ], [42*mm, 62*mm, W-104*mm]))

    f.append(P("0.4. Chiến lược làm bài theo mục tiêu điểm", "h2"))
    f.append(table([
        ["Mục tiêu", "Cần “khóa chặt” phần nào", "Phần quyết định"],
        ["5,0–6,5 (trung bình – khá)", "Listening lấy chi tiết (Biết) + Vocabulary/Grammar TN + Reading cloze + Re-ordering. Riêng khối “Biết” đã là 4,0đ.", "Không bỏ trống bất kỳ câu tự luận nào — viết được câu nào hay câu đó."],
        ["7,0–8,5 (khá – giỏi)", "Toàn bộ TN đạt ≥ 22/28; thêm 2 câu word-form và ít nhất 3/4 câu transformation.", "Đoạn văn đủ 120 từ, đúng cấu trúc, ít lỗi ngữ pháp cơ bản."],
        ["9,0+ (xuất sắc)", "TN gần như tuyệt đối (26–28/28); tự luận trọn vẹn.", "Đoạn văn có từ vựng theo chủ đề, câu ghép/câu bị động dùng đúng chỗ, liên kết mạch lạc."],
    ], [38*mm, 72*mm, W-110*mm]))
    f.append(P("<b>Phân bổ thời gian gợi ý</b> (nếu đề thi 60 phút; nếu thời gian khác, giữ nguyên tỉ lệ): "
               "Listening ~12 phút (nghe theo tiến trình băng, không quay lại) → Language ~8 phút → Reading ~18 phút → "
               "Writing 1 ~3 phút → Writing 2 ~7 phút → Writing 3 ~10 phút → 2 phút cuối rà soát. "
               "Nguyên tắc vàng: <b>câu nào khó quá 45 giây thì đánh dấu, làm tiếp</b>, tuyệt đối không để trống câu trắc nghiệm — "
               "đoán có căn cứ vẫn có 25% cơ hội đúng.", "p"))
    f.append(P("<b>Ba lỗi “mất điểm oan” phổ biến nhất</b> cần tránh: (1) nghe Listening mà không đọc trước câu hỏi trong lúc chờ băng; "
               "(2) viết lại câu làm thay đổi nghĩa hoặc quên chia động từ/dạng bị động; (3) đoạn văn viết lan man không có câu chủ đề, "
               "hoặc thiếu từ nối khiến ý rời rạc. Cả ba lỗi này đều được luyện kỹ ở Phần I (Chương 3) và Phần II.", "p"))
    return f
