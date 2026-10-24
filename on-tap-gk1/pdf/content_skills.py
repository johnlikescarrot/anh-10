# -*- coding: utf-8 -*-
"""PHAN 4 – Ky nang: Listening, Reading (cloze + comprehension), Writing (reorder,
transformation, paragraph). Includes model paragraphs imported from texts.py."""

from texts import (MP_FAMILY, MP_FAMILY_TITLE, MP_ENV, MP_ENV_TITLE,
                    MP_MUSIC, MP_MUSIC_TITLE)

BLOCKS = [
    ("h1", "PHẦN 4. KỸ NĂNG LÀM TỪNG PHẦN – QUY TRÌNH 4 BƯỚC CHO MỖI DẠNG BÀI"),

    # ---------------- LISTENING ----------------
    ("h2", "4.1. LISTENING (10 câu – 2,5đ): 2 đoạn ~1,5 phút, 180–200 từ"),
    ("p", "Định dạng theo đặc tả: <b>Đoạn 1</b> — độc thoại/hội thoại + 5 nhận định chọn <b>True/False</b> (TNKQ); "
          "<b>Đoạn 2</b> — hội thoại/độc thoại + 5 câu hỏi <b>MCQ</b> 3 lựa chọn. Mỗi đoạn 3 câu Nhận biết (thông tin chi tiết: "
          "ai – gì – mấy giờ – ở đâu) và 2 câu Thông hiểu (ý chính, suy luận)."),
    ("numbers", [
        "<b>Trước khi nghe (30–40 giây):</b> đọc lướt toàn bộ nhận định/câu hỏi, gạch chân từ khóa: tên riêng, con số, "
        "động từ chính, từ phủ định (NEVER, NOT, only). Dự đoán từ sẽ nghe.",
        "<b>Lượt nghe 1:</b> tập trung khớp thông tin cho câu Nhận biết; nếu lỡ một câu, bỏ ngay — đừng “đứng hình” theo câu đó.",
        "<b>Lượt nghe 2:</b> trả lời nốt câu còn thiếu và ưu tiên 2 câu Thông hiểu: câu hỏi “mainly about / best summary / "
        "why” thường nằm ở 1–2 câu ĐẦU hoặc CUỐI đoạn.",
        "<b>Chuyển đáp án:</b> True/False — nhớ: chỉ SAI khi nhận định trái hoặc lệch thông tin (đảo vai người–việc, đổi số, "
        "đổi địa điểm); MCQ — đáp án đúng thường là CÂU DIỄN ĐẠT LẠI (paraphrase), đáp án sai hay lặp nguyên văn từ nhưng "
        "đổi bản chất."]),
    ("box", "warn", [
        "<b>3 bẫy kinh điển của phần nghe:</b> ① “Not mentioned”: thông tin có thật trong bài nhưng gắn với người/vật khác "
        "(Mẹ nấu ăn + TƯỚI CÂY → sai, vì bố tưới cây). ② Số liệu đi kèm phép tính nhỏ (meeting 8:00 + 15 phút → kết thúc 8:15). "
        "③ Từ phủ định đảo nghĩa (volunteers get ONE FREE ticket → bạn không cần MUA một vé)."]),
    ("box", "tip", [
        "Ôn nghe trong 30 giây/ngày: bật 1 đoạn 60 giây bất kỳ (podcast/YouTube) về 3 chủ đề → nhẩm trả lời 3 câu: "
        "Ai? Làm gì? Khi nào? — đúng 3 câu Nhận biết ma trận yêu cầu. Đoạn văn 180–200 từ ≈ 6–7 phút đọc chậm, nhưng khi nghe chỉ ~1,5 phút "
        "→ LUYỆN TỐC ĐỘ là bắt buộc."]),

    # ---------------- READING CLOZE ----------------
    ("h2", "4.2. READING 1 – CLOZE-TEXT trên TỜ RƠI/QUẢNG CÁO (5 câu – 1,25đ)"),
    ("p", "Đặc tả: “Đọc tờ rơi/quảng cáo và điền từ vào chỗ trống” — văn bản ngắn, nhiều thông tin thực (ngày giờ, giá, điều kiện). "
          "5 chỗ trống trộn lẫn: <b>từ vựng chủ đề + ngữ pháp (thì/bị động/infinitive) + liên từ + collocation</b>."),
    ("numbers", [
        "Đọc 1 lượt lấy “bản đồ”: sự kiện gì – cho ai – khi nào – ở đâu – lợi ích/lưu ý.",
        "Với từng ô: nhìn từ LIỀN TRƯỚC và LIỀN SAU để biết cần loại từ gì (sau will → V-bare; “by + người” → V3; "
        "trước N → adj; shouldn't → V-bare…).",
        "Loại trừ: phương án phá vỡ collocation hoặc sai nghĩa cả câu bị loại trước; chỉ cân nhắc giữa 2 phương án cuối.",
        "Điền xong đọc lại CẢ câu: nếu thấy “lấn cấn” giữa 2 vế, thường là thiếu/sai liên từ — kiểm tra ngay dấu phẩy + but/so/and."]),
    ("box", "tip", [
        "Cloze trên tờ rơi hay hỏi đúng các “móc” ngữ pháp ma trận: (1) động từ sau <b>will/should/be going to</b> → bare-V; "
        "(2) “will be ______ <b>by</b>” → <b>V3</b> (bị động); (3) hai mệnh đề có dấu phẩy → <b>FANBOYS</b>; "
        "(4) danh từ đếm được số nhiều đi với “folk ___ / plastic ___” → chọn từ đúng chủ đề."]),

    # ---------------- READING COMPREHENSION ----------------
    ("h2", "4.3. READING 2 – ĐOẠN VĂN 220–250 TỪ (5 câu – 1,25đ)"),
    ("p", "3 câu Nhận biết (chi tiết) + 2 câu Thông hiểu (ý chính / từ tham chiếu). Quy trình “đọc câu hỏi trước – scan sau”."),
    ("numbers", [
        "Đọc lướt 5 câu hỏi (che đáp án), gạch chân từ khóa riêng: tên, số, in hoa, từ hiếm.",
        "Skim đoạn 60–80 giây: đọc câu đầu + câu cuối mỗi đoạn để nắm mạch; đoạn văn một khối → đọc 2 câu đầu & 2 câu cuối.",
        "Về từng câu hỏi: định vị DÀN Ý (đoạn nào chứa từ khóa) → đọc kỹ 1–2 câu quanh đó → chọn đáp án khớp nhất; "
        "chi tiết gây nhiễu chỉ dùng NGUYÊN VĂN nhưng sai bản chất → loại.",
        "Câu “refers to / it / this + N”: thay phương án vào vị trí từ đó rồi đọc lại — chọn phương án giữ nghĩa mạch lạc. "
        "Thường chỉ về cụm DANH TỪ ngay liền trước.",
        "Câu ý chính (mainly about / best title / main idea): chọn phương án bao TRỌN đoạn; phương án chỉ đúng 1 chi tiết là bẫy."]),
    ("box", "warn", [
        "Đừng dịch từng từ — hết giờ. Đoạn 220–250 từ đọc hiểu được thiết kế để làm trong ≤ 8 phút cả 5 câu. "
        "Gặp từ mới: đoán qua ngữ cảnh (thường từ khó nằm ở câu KHÔNG bị hỏi)."]),

    # ---------------- WRITING REORDER ----------------
    ("h2", "4.4. WRITING 1 – SẮP XẾP (2 câu TNKQ – 0,5đ) & các mẹo 30 giây"),
    ("numbers", [
        "Tìm câu MỞ: chào hỏi (Hi/Dear), tuyên bố mục đích (I'm writing to… / Let me tell you about…).",
        "Tìm câu KẾT: lời hẹn/đề nghị/hi vọng (See you then! / I hope you can join us! / Yours sincerely…).",
        "Xâu chuỗi bằng 3 loại móc: liên từ thời gian (First… After that… Finally), đại từ (it, they, this plan — phải có “nguồn” đứng trước), "
        "lặp từ vựng (clean-up → volunteers → rubbish).",
        "Thử ngay 3 phương án của đề: phương án mở/kết vô lý → loại; so sánh 2 phương án còn lại bằng 1 cặp câu dính nhau nhất."]),

    # ---------------- WRITING TRANSFORMATION ----------------
    ("h2", "4.5. WRITING 2 – VIẾT LẠI CÂU (4 câu TL – 1,0đ): bảng chuyển đổi thuộc lòng"),
    ("p", "Đặc tả: “viết lại được câu cùng nghĩa với câu đã cho” — chỉ xoay quanh 5 chủ điểm ngữ pháp. Học thuộc 8 khuôn dưới đây là đủ phủ toàn bộ đề."),
    ("table", {"header": ["Khuôn", "Câu gốc → Câu viết lại"],
               "rows": [
                   ["Chủ động → bị động (theo thì)",
                    "People throw away millions of bottles every day. → Millions of bottles <b>are thrown away</b> every day."],
                   ["Chủ động → bị động (đang làm)",
                    "My father <b>is repairing</b> the bike. → The bike <b>is being repaired</b> by my father."],
                   ["will ↔ be going to (kế hoạch)",
                    "It is our plan to visit grandma next Sunday. → We <b>are going to visit</b> grandma next Sunday."],
                   ["too…to ↔ so…that",
                    "The music is <b>too loud for</b> the neighbours <b>to sleep</b>. → The music is <b>so loud that</b> the neighbours <b>can't sleep</b>."],
                   ["(not) enough to ↔ too + trái nghĩa",
                    "He isn't <b>old enough to ride</b> a motorbike. → He is <b>too young to ride</b> a motorbike."],
                   ["2 câu đơn → câu ghép (so / but)",
                    "The film was boring. We still watched it. → The film was boring<b>, but</b> we still watched it."],
                   ["allow + O + to V ↔ let + O + V",
                    "My parents <b>allow me to go out</b> at weekends. → My parents <b>let me go out</b> at weekends."],
                   ["want/hope/decide + to V (giữ nguyên to V)",
                    "My parents decided <b>to install</b> solar panels. (khi viết lại chỉ đổi sang: It was my parents' decision <b>to install</b>…)"],
               ], "widths": [0.3, 0.7], "fs": 8.3}),
    ("box", "warn", [
        "<b>Giữ nguyên thì</b> trừ khi khuôn đổi thì yêu cầu (bị động = cùng thì + BE chia lại). 3 lỗi trừ điểm phổ biến nhất: "
        "quên “to” sau want/decide; quên đổi số của chủ ngữ mới (<i>Millions of bottles ARE…</i>); nhét thêm từ “cho đủ” làm nghĩa vênh 1%.",
        "Đếm số từ nếu đề giới hạn; không thay đổi từ khóa in hoa; sau khi viết, ĐỌC LẠI CẢ 2 CÂU cạnh nhau: nghĩa vênh nhau 1% cũng là sai."]),
    ("box", "tip", [
        "Chiến thuật “2 phút/câu”: đọc câu gốc → tự hỏi “dấu hiệu gì?” (too? by? 2 mệnh đề? plan?) → chọn khuôn → viết → soát chia động từ. "
        "Câu khó nhất cũng chỉ xoay 8 khuôn trên — không có khuôn ngoài đề."]),

    # ---------------- WRITING PARAGRAPH ----------------
    ("h2", "4.6. WRITING 3 – ĐOẠN VĂN 120–150 TỪ (1,0đ) – “công thức 5 viên gạch”"),
    ("table", {"header": ["Viên gạch", "Nhiệm vụ", "Câu mở đầu mẫu"],
               "rows": [
                   ["① Topic sentence", "Nêu chủ đề + quan điểm cá nhân (2 câu đặc tả: “bày tỏ quan điểm”)",
                    "<i>In my family, sharing the housework is the secret of a happy home. · Music plays an important part in my daily life. · Single-use plastic is a big problem at school.</i>"],
                   ["② Fact / Example", "Việc có thật ở nhà/trường em (dùng thì hiện tại + trạng từ tần suất)",
                    "<i>My mother…, while my father… · Every lunchtime, I see…</i>"],
                   ["③ Reason / Effect", "Giải thích tại sao / kết quả (dùng so, because, when…)",
                    "<i>When everyone shares the tasks, the work finishes quickly, so…</i>"],
                   ["④ Counter / Tip", "Nhượng bộ nhỏ hoặc lời khuyên (thăng hoa cho điểm Vận dụng)",
                    "<i>Some people say…, but… · My tip for busy students is simple: …</i>"],
                   ["⑤ Closing", "Khẳng định lại + mong muốn/hành động",
                    "<i>In short,… · If every member contributes a little,… · Let's act this week!</i>"],
               ], "widths": [0.18, 0.37, 0.45], "fs": 8.2}),
    ("h3", "Chấm đoạn văn theo đúng 4 tiêu chí giáo viên hay dùng (thang 1,0đ)"),
    ("table", {"header": ["Tiêu chí", "Điểm", "Yêu cầu đạt"],
               "rows": [
                   ["Nội dung & quan điểm (Content)", "0,35", "Đủ 2–3 ý đúng chủ đề, CÓ quan điểm cá nhân rõ (I believe / In my opinion)"],
                   ["Tổ chức & mạch lạc (Organization)", "0,25", "Đúng 1 đoạn (không xuống dòng lộn xộn), có liên từ nối (while, When, Besides, To sum up)"],
                   ["Dùng từ & cấu trúc (Language)", "0,25", "≥ 6 từ chủ đề trong bảng từ; dùng đúng 1–2 điểm ngữ pháp đã học (bị động, too…to, FANBOYS)"],
                   ["Độ chính xác & định dạng (Accuracy)", "0,15", "Đủ 120–150 từ; chính tả; viết hoa – dấu câu; không dịch từng chữ"],
               ], "widths": [0.34, 0.1, 0.56], "center": [1], "fs": 8.3}),
    ("box", "warn", [
        "<b>Lỗi trừ điểm nặng:</b> ① quá dài/quá ngắn (dưới 110 hoặc vượt 160 từ); ② lan man 2–3 chủ đề trong 1 đoạn; ③ không có câu kết; "
        "④ “Vietnamese-English”: <i>do housework very much → do a lot of housework</i>; <i>my mother is the best cooker → best cook</i>; "
        "⑤ lạm dụng từ vựng ngoài 3 chủ điểm — sai collocation còn mất điểm hơn từ đơn giản đúng."]),
    ("p", "<b>Đề bài gợi ý cho mỗi chủ đề (khớp đặc tả “chủ đề cá nhân quan tâm”):</b> ① How housework should be shared in a family "
          "· ② How students can reduce plastic at school · ③ The role of music in your life / your favourite musician or song. "
          "Học kỹ 1 trong 3 bài mẫu dưới đây rồi tự biến đổi — cả 3 đều dùng đúng ngữ pháp 5 chủ điểm."),

    ("h3", "BÀI MẪU – tham khảo cách lắp “5 viên gạch” (gạch in đậm là ngữ pháp chủ điểm)"),
    ("passage", [MP_FAMILY], MP_FAMILY_TITLE),
    ("p", "Ngữ pháp được sử dụng: hiện tại đơn + trạng từ tần suất (usually implicitly), <b>while/and</b> câu ghép, <b>should not be</b> + bị động "
          "<i>is finished</i>, <b>to + V</b> (wait for your parents <b>to ask</b>)."),
    ("passage", [MP_ENV], MP_ENV_TITLE),
    ("p", "Ngữ pháp: <b>are sorted</b> (bị động hiện tại đơn), <b>can bring / can set up</b> (modal + bare-V), "
          "<b>although/but</b> (câu ghép/nhượng bộ), <b>need over 400 years TO DECOMPOSE</b> (to-infinitive)."),
    ("passage", [MP_MUSIC], MP_MUSIC_TITLE),
    ("p", "Ngữ pháp: <b>because</b> (lý do), <b>however</b>, <b>showed that songs CAN DIVIDE</b>, <b>can harm</b> — tất cả nằm trong 5 chủ điểm."),

    ("box", "task", [
        "<b>Bài tập tự luyện (nộp cho nhóm học tập):</b> chọn 1 trong 3 đề ①②③, viết đoạn 120–150 từ theo 5 viên gạch; "
        "gạch chân mọi động từ và ghi nhanh (HTĐ / HTTD / bị động / to-V / FANBOYS) bên cạnh. Sau đó đổi chéo soát lỗi theo bảng tiêu chí 4.6."]),
]
