# -*- coding: utf-8 -*-
"""Phần I - Chương 3: Kỹ năng làm bài Listening/Reading/Writing + khung viết đoạn."""
from common import *

def build():
    f = []
    f.append(P("CHƯƠNG 3: KỸ NĂNG LÀM TỪNG DẠNG BÀI & KHUNG VIẾT", "h1"))
    f.append(P("Kiến thức (Chương 1–2) chiếm một nửa thành công; nửa còn lại là <b>kỹ thuật làm bài</b>. "
               "Chương này “mổ xẻ” từng dạng bài đúng như Bảng đặc tả mô tả, kèm quy trình từng bước để em áp dụng ngay."))

    # Listening
    f.append(P("3.1. Listening (10 câu — 2,5 điểm): nghe 1,5 phút, 180–200 từ", "h2"))
    f.append(P("Hai bài nghe đều xoay quanh 3 chủ đề Units 1–3. Listening 1 thường là dạng <b>True/False</b> (hoặc tương tự), "
               "Listening 2 là <b>trắc nghiệm MCQ</b>. Mỗi bài: 3 câu mức Biết (nghe chi tiết: con số, tên, hoạt động…) và 2 câu mức Hiểu (ý chính/suy luận gần).", "p"))
    f.append(P("<b>Quy trình 3 giai đoạn:</b>", "p"))
    for t in [
        "<b>TRƯỚC khi nghe (30–60 giây quý giá):</b> đọc lướt toàn bộ câu hỏi, gạch chân <i>từ khóa</i> (who/what/when/where/how many). Dự đoán trước loại thông tin cần nghe (số? tên người? hoạt động?).",
        "<b>TRONG khi nghe lần 1:</b> tập trung bắt ý chính và các từ khóa đã gạch; đừng dừng lại ở một câu chưa nghe rõ — băng không chờ ai. Nghe thấy từ trái nghĩa/phủ định (<i>not, never, but, instead</i>) phải đặc biệt chú ý vì bẫy thường nằm ở đó.",
        "<b>NGHE lần 2 (nếu có) & 15 giây cuối:</b> kiểm chứng từng câu, nhất là các câu True/False có chi tiết “gần đúng”. Câu nào còn trống, hãy đoán theo logic của bài — không để trống.",
    ]:
        f.append(bullet(t))
    f.append(box("BẪY NGHE KINH ĐIỂN",
                 ["<b>“Nhắc tới nhưng không phải đáp án”:</b> băng nhắc cả 3–4 phương án nhưng chỉ một cái đúng với câu hỏi (hỏi <i>ai rửa bát</i> — băng nhắc cả nhà, phải nghe đúng người).",
                  "<b>Đảo thông tin bằng but/however:</b> “I usually do the cooking, <b>but</b> today my sister is doing it.” → đáp án là <i>sister</i>, không phải <i>I</i>.",
                  "<b>Số liệu bị “bẻ”:</b> nghe 15 phút/50 phút, 3 người/13 người — ghi nhanh con số ra nháp ngay khi nghe thấy.",
                  "Câu True/False chứa <i>always/never/every day</i> rất hay là <b>False</b> vì băng thường nói nhẹ hơn (<i>often, sometimes</i>)."],
                 bg=LIGHT2, border=ORANGE))
    f.append(P("<b>Luyện nghe ở nhà khi không có file audio:</b> dùng chính phần <i>Transcript</i> ở Phần IV của tài liệu này — nhờ người thân/điện thoại (đọc văn bản) đọc thành tiếng 2 lần, "
               "em chỉ nghe và trả lời, sau đó mới mở transcript kiểm tra. Mỗi ngày 1 bài 5 phút là đủ để “quen tai” với tốc độ 180–200 từ.", "p"))

    # Reading
    f.append(P("3.2. Reading 1 — Cloze text (điền từ vào tờ rơi/quảng cáo, 5 câu)", "h2"))
    f.append(P("Văn bản thường là tờ rơi CLB Xanh, thông báo buổi hòa nhạc, quảng cáo khóa học… 5 chỗ trống kiểm tra xen kẽ: "
               "từ vựng theo chủ đề, ngữ pháp (thì, bị động, to-inf…), từ nối và đại từ liên kết.", "p"))
    for i, t in enumerate([
        "Đọc <b>toàn bài một lượt</b> (chưa điền) để nắm chủ đề và giọng văn.",
        "Với từng chỗ trống: xác định <b>loại từ cần điền</b> (nhìn từ trước/sau trống) → loại ngay 1–2 phương án sai loại từ.",
        "Kiểm tra <b>cụm cố định & ngữ pháp quanh trống</b>: giới từ đi kèm, thì của câu, chủ–vị hòa hợp, <i>to V / V-ing / V trần</i>.",
        "Điền xong đọc lại cả câu thành tiếng trong đầu — câu đúng phải “trôi” cả về nghĩa lẫn ngữ pháp.",
    ], 1):
        f.append(num(i, t))
    f.append(P("3.3. Reading 2 — Reading comprehension (đoạn văn 220–250 từ, 5 câu MCQ)", "h2"))
    for i, t in enumerate([
        "<b>Đọc câu đầu mỗi đoạn</b> để nắm ý chính toàn bài trước khi đọc câu hỏi.",
        "Câu hỏi <b>ý chính (main idea/title)</b>: đáp án phải bao quát cả bài; loại phương án quá hẹp (chỉ một chi tiết) hoặc quá rộng.",
        "Câu hỏi <b>chi tiết</b>: gạch từ khóa trong câu hỏi, “quét” (scan) đoạn văn tìm đúng vị trí, đọc kỹ 1 câu trước – 1 câu sau vị trí đó.",
        "Câu hỏi <b>tham chiếu</b> (<i>The word “they” refers to… / The pronoun “it” refers to…</i>): thay từng phương án vào vị trí đại từ và đọc lại — phương án đúng là danh từ (thường ở câu liền trước) hợp nghĩa nhất.",
        "Câu <b>NOT true / EXCEPT</b>: kiểm chứng lần lượt từng phương án với bài; 3 phương án có trong bài, 1 phương án sai/không có — đó là đáp án.",
        "Câu <b>suy luận</b> (<i>It can be inferred that…</i>): đáp án phải suy ra được từ bài, không dùng kiến thức ngoài đời để chọn.",
    ], 1):
        f.append(num(i, t))

    # Writing 1
    f.append(P("3.4. Writing 1 — Re-ordering (sắp xếp câu, 2 câu trắc nghiệm)", "h2"))
    f.append(P("Đề cho 4–5 câu rời (a–e) và 4 phương án thứ tự. Bí quyết: <b>tìm câu mở đầu</b> (câu chào/giới thiệu/câu chủ đề — thường chứa danh từ chưa có mạo từ xác định, hoặc lời chào trong hội thoại) "
               "và <b>câu kết</b> (cảm ơn, lời chúc, kết luận). Sau đó ghép các cặp câu “dính” nhau: câu hỏi → câu trả lời; <i>Firstly → Secondly → Finally</i>; đại từ (<i>it/they/this</i>) phải đứng sau danh từ mà nó thay thế.", "p"))
    f.append(table([
        ["Thể loại", "Cấu trúc trật tự điển hình"],
        ["Hội thoại", "Chào hỏi → hỏi/đề nghị → trả lời/phản hồi → nói rõ chi tiết → cảm ơn/tạm biệt"],
        ["Lá thư / email", "Lời chào (Dear…) → lí do viết thư → nội dung chính (2–3 ý) → lời kết (Looking forward to…; Best wishes)"],
        ["Đoạn văn", "Câu chủ đề (topic sentence) → ý 1 + ví dụ → ý 2 + ví dụ (Secondly…) → câu kết luận (In short/To sum up…)"],
    ], [30*mm, W-30*mm]))

    # Writing 2
    f.append(P("3.5. Writing 2 — Sentence transformation (viết lại câu, 4 câu tự luận)", "h2"))
    f.append(P("Đề cho câu gốc và thường gợi ý bằng từ/cụm cho sẵn (in đậm hoặc từ đầu câu viết sẵn). 8 “đường mòn” biến đổi hay gặp nhất, tất cả đều quay về 5 chủ điểm ngữ pháp:", "p"))
    f.append(table([
        ["#", "Dạng biến đổi", "Ví dụ gốc → viết lại"],
        ["1", "Chủ động → Bị động", "People use plastic bags everywhere. → <b>Plastic bags are used everywhere.</b>"],
        ["2", "Bị động → Chủ động (có by)", "The room was cleaned by the students. → <b>The students cleaned the room.</b>"],
        ["3", "will ↔ be going to (theo ngữ cảnh)", "We've decided to plant trees. → <b>We are going to plant trees.</b>"],
        ["4", "Nối 2 câu đơn thành câu ghép", "It rained heavily. We stayed at home. → <b>It rained heavily, so we stayed at home.</b>"],
        ["5", "Tách/chuyển so ↔ because", "Because she was ill, she stayed home. → <b>She was ill, so she stayed home.</b>"],
        ["6", "make/let → bị động / đổi cấu trúc", "Mum made me wash the dishes. → <b>I was made to wash the dishes.</b>"],
        ["7", "want/decide/hope + to V; mục đích", "She saves money. She wants to buy a guitar. → <b>She saves money to buy a guitar.</b>"],
        ["8", "HT đơn ↔ HT tiếp diễn (theo trạng từ)", "He is playing the piano now. → (giữ nguyên ý, đổi theo từ gợi ý cho sẵn)"],
    ], [10*mm, 52*mm, W-62*mm], align_center_cols={0}))
    f.append(box("3 NGUYÊN TẮC “BẤT DI BẤT DỊCH” KHI VIẾT LẠI CÂU",
                 ["<b>Nghĩa không đổi</b> — viết xong đọc lại, so với câu gốc: ai làm gì, khi nào, khẳng định hay phủ định.",
                  "<b>Chia động từ đầy đủ</b> — lỗi bị trừ điểm nhiều nhất là quên -s/es, quên be trong bị động, quên V3.",
                  "<b>Dùng đúng từ gợi ý</b> (nếu đề cho từ in đậm/cho sẵn đầu câu) — không thay bằng từ đồng nghĩa khác."],
                 bg=LIGHT3, border=GREEN))

    # Writing 3
    f.append(P("3.6. Writing 3 — Viết đoạn văn 120–150 từ (1,0 điểm)", "h2"))
    f.append(P("Đề yêu cầu viết đoạn văn/thư/bài báo ngắn bày tỏ quan điểm về một trong ba chủ đề: <b>Family life, Humans and the environment, Music</b>. "
               "Đây là câu “1 điểm tròn” duy nhất của bài thi nên cần đầu tư đúng mức: không cần viết hay như văn mẫu, chỉ cần <b>đúng cấu trúc + đủ ý + ít lỗi</b>.", "p"))
    f.append(P("<b>Cấu trúc đoạn văn 4 phần (công thức T–S–S–C):</b>", "p"))
    f.append(table([
        ["Phần", "Nhiệm vụ", "Câu mở đầu mẫu"],
        ["<b>T</b> — Topic sentence (1 câu)", "Nêu thẳng chủ đề/quan điểm", "Sharing household chores brings many benefits to my family."],
        ["<b>S1</b> — Supporting idea 1 (2–3 câu)", "Ý chính 1 + giải thích/ví dụ", "Firstly, … For example, …"],
        ["<b>S2</b> — Supporting idea 2 (2–3 câu)", "Ý chính 2 + giải thích/ví dụ", "Secondly, … In addition, …"],
        ["<b>C</b> — Concluding sentence (1 câu)", "Kết luận, khẳng định lại quan điểm", "In short, … / To sum up, …"],
    ], [42*mm, 52*mm, W-94*mm]))
    f.append(box("NGÂN HÀNG TỪ NỐI & CÂU “ĂN ĐIỂM” (học thuộc 10 cụm này là đủ dùng)",
                 ["Mở ý: <b>Firstly, … / Secondly, … / Finally, …</b> &nbsp;•&nbsp; Thêm ý: <b>In addition, … / Moreover, … / Besides, …</b>",
                  "Cho ví dụ: <b>For example, … / For instance, …</b> &nbsp;•&nbsp; Đối lập: <b>However, … / On the other hand, …</b>",
                  "Kết quả: <b>As a result, … / Therefore, …</b> &nbsp;•&nbsp; Kết luận: <b>In short, … / To sum up, … / In my opinion, …</b>",
                  "Câu “ghi điểm ngữ pháp” nên cài 1–2 câu vào bài: một câu <b>bị động</b> (<i>Housework is shared equally in my family</i>), "
                  "một câu <b>ghép với so/and</b>, một câu <b>to-infinitive chỉ mục đích</b> (<i>… to strengthen our bond</i>). Giám khảo chấm Writing 3 rất chú ý sự đa dạng cấu trúc này."],
                 bg=LIGHT, border=NAVY))
    f.append(P("<b>Dàn ý nhanh cho 3 chủ đề (học thuộc khung, thay nội dung khi vào thi):</b>", "p"))
    f.append(table([
        ["Chủ đề đề có thể ra", "Ý 1 (Firstly)", "Ý 2 (Secondly)", "Câu kết gợi ý"],
        ["Lợi ích của việc chia sẻ việc nhà (Family life)", "Giảm gánh nặng cho cha mẹ; không ai bị quá mệt", "Gắn kết gia đình, dạy trẻ tính trách nhiệm", "In short, sharing chores makes our home happier and brings us closer."],
        ["Việc học sinh có thể làm để bảo vệ môi trường (Environment)", "Thực hiện 3Rs ở trường/nhà: giảm nhựa, tái sử dụng, phân loại rác", "Tiết kiệm điện nước, trồng cây, tuyên truyền nâng cao nhận thức", "To sum up, small green actions every day can make a big difference."],
        ["Vai trò/lợi ích của âm nhạc trong đời sống (Music)", "Giúp thư giãn, giảm căng thẳng sau giờ học", "Kết nối mọi người, phát triển tài năng và sự tự tin", "In short, music makes our life richer and happier."],
    ], [48*mm, 42*mm, 42*mm, W-132*mm]))
    f.append(P("Ba bài văn mẫu hoàn chỉnh (120–150 từ) cho đúng 3 dàn ý trên được trình bày ở <b>Phần IV – mục 4.5</b>. Hãy học thuộc <i>khung câu</i> của các bài mẫu đó, "
               "đừng học thuộc lòng từng chữ — vào phòng thi em chỉ việc thay chi tiết cho khớp đề. <b>Lưu ý độ dài:</b> đếm sơ khoảng 8–10 câu là đạt 120–150 từ; viết quá ngắn (&lt;100 từ) hoặc quá dài (&gt;180 từ) đều bất lợi.", "p"))
    return f
