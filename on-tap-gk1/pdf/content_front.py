# -*- coding: utf-8 -*-
"""PHAN 1 – Phân tích cấu trúc đề GK1 (theo docx ma trận) + PHAN 2 – Từ vựng."""

BLOCKS = [
    # ============================ PART 1 ============================
    ("h1", "PHẦN 1. PHÂN TÍCH CẤU TRÚC ĐỀ KIỂM TRA GK1 – MÔN TIẾNG ANH 10, NĂM HỌC 2026–2027"),
    ("lead", "Toàn bộ phần này được phân tích trực tiếp từ tệp <b>“2026_2027_MA TRẬN 10_GK1.docx”</b> của nhà trường, "
             "gồm hai thành phần: (I) <b>Ma trận đề</b> (bảng 4 mức độ × 4 kỹ năng) và (II) <b>Bảng đặc tả kỹ thuật</b> "
             "(yêu cầu cần đạt cho từng mức độ Nhận biết – Thông hiểu – Vận dụng). Đề cương, dạng bài và mức độ khó của "
             "tài liệu này được xây dựng khớp 100% với hai bảng đó."),

    ("h2", "1.1. Thông tin chung về đề thi"),
    ("table", {"header": ["Hạng mục", "Nội dung trích từ ma trận/đặc tả"],
               "rows": [
                   ["Kì thi", "Kiểm tra Giữa kì 1 (GK1), năm học 2026–2027"],
                   ["Môn", "Tiếng Anh 10 – sách Global Success"],
                   ["Phạm vi ôn tập", "Units 1–3: <b>Family life</b> (Unit 1) · <b>Humans and the Environment</b> (Unit 2) · <b>Music</b> (Unit 3)"],
                   ["Hình thức", "Trắc nghiệm nhiều lựa chọn (TNKQ) + Tự luận; tỉ lệ <b>70% TNKQ – 30% tự luận</b>"],
                   ["Số lượng", "<b>28 câu TN</b> (7,0 điểm; 0,25đ/câu) + tự luận: <b>6 câu</b> (từ vựng vận dụng 2, viết lại câu 4) và <b>1 bài viết đoạn văn</b>"],
                   ["Thời gian", "Ma trận không nêu – theo thông lệ trường THPT: 45 phút (làm theo quy định của trường)"],
                   ["Nghe", "2 đoạn (mỗi đoạn ~1,5 phút, 180–200 từ): dạng True/False và MCQ"],
                   ["Đọc", "2 phần: cloze-text trên tờ rơi/quảng cáo + đoạn văn đọc hiểu 220–250 từ"],
                   ["Viết", "Re-ordering (TNKQ) · Sentence transformation · Viết đoạn/bài 120–150 từ nêu quan điểm cá nhân"],
               ], "widths": [0.22, 0.78], "center": []}),

    ("h2", "1.2. Bảng cơ cấu điểm – khôi phục đầy đủ từ ma trận"),
    ("small", "Mỗi câu TNKQ = 0,25 điểm. Điểm phần tự luận được suy ra từ cột “Tỉ lệ % điểm” của ma trận (15% ≈ 1,5đ; 10% ≈ 1,0đ; 5% ≈ 0,5đ) — con số khớp tuyệt đối, tổng đúng 10,0."),
    ("table", {"header": ["Phần", "Đơn vị kiến thức", "Dạng bài", "Mức độ (NB–TH–VD)", "Số câu", "Điểm", "%"],
               "rows": [
                   ["A · LISTENING", "Listening 1", "Đoạn độc thoại/hội thoại + nhận định <b>True/False</b>", "3 – 2 – 0", "5", "1,25", "12,5"],
                   ["", "Listening 2", "Đoạn hội thoại dạng <b>MCQ</b> (3 lựa chọn)", "3 – 2 – 0", "5", "1,25", "12,5"],
                   ["B · LANGUAGE", "Vocabulary", "TNKQ từ vựng theo chủ đề + <b>tự luận</b> cho từ (dạng từ trong ngoặc)", "1 – 1 – <b>2 (TL)</b>", "2 TN + 2 TL", "1,5", "15"],
                   ["", "Grammar", "TNKQ ngữ pháp: 5 chủ điểm", "2 – 2 – 0", "4", "1,0", "10"],
                   ["C · READING", "Reading 1 (cloze-text)", "Đọc <b>tờ rơi/quảng cáo</b>, điền 5 chỗ trống", "3 – 2 – 0", "5", "1,25", "12,5"],
                   ["", "Reading 2 (comprehension)", "Đoạn văn 220–250 từ + câu hỏi MCQ", "3 – 2 – 0", "5", "1,25", "12,5"],
                   ["D · WRITING", "Writing 1", "<b>Sắp xếp</b> câu thành hội thoại/lá thư/đoạn văn (chọn thứ tự)", "2 – 0 – 0", "2", "0,5", "5"],
                   ["", "Writing 2", "<b>Viết lại câu</b> giữ nguyên nghĩa", "0 – 0 – 4", "4 TL", "1,0", "10"],
                   ["", "Writing 3", "<b>Viết đoạn văn</b> 120–150 từ nêu quan điểm", "0 – 0 – 1 bài", "1 bài", "1,0", "10"],
                   ["TỔNG", "", "28 TN (7,0đ) + 6 câu TL + 1 bài viết (3,0đ)", "20 NB · 15 TH · 8 câu/bài V-Dụng", "28 + 7", "10,0", "100"],
               ], "widths": [0.13, 0.16, 0.27, 0.17, 0.1, 0.085, 0.075],
               "center": [0, 3, 4, 5, 6], "fs": 7.9,
               "rowcolors": [[9, "#E4F3EC"]]}),

    ("h2", "1.3. Nhận định quan trọng từ ma trận (cần nhớ khi ôn)"),
    ("bullets", [
        "<b>Phần lớn câu hỏi là NHẬN BIẾT – THÔNG HIỂU (35/43 lượt hỏi).</b> Không có câu Vận dụng cao trong trắc nghiệm → "
        "chỉ cần học chắc từ vựng trong bảng từ SGK + 5 chủ điểm ngữ pháp là đã nắm trong tay 7–8 điểm. Tuyệt đối không lan man ngữ pháp ngoài chương trình.",
        "<b>Toàn bộ điểm Vận dụng nằm ở 3 phần tự luận</b> (2 câu dạng từ, 4 câu viết lại câu, 1 đoạn văn = 3,0đ). Đây là phần tách học sinh khá – giỏi; "
        "trong đó 4 câu viết lại câu chỉ xoay quanh chính 5 chủ điểm ngữ pháp → học công thức chuyển đổi là lấy trọn 1,0đ.",
        "<b>Ngữ pháp gói gọn trong 5 chủ điểm:</b> (1) Hiện tại đơn – hiện tại tiếp diễn; (2) Tương lai: will / be going to; (3) Bị động; "
        "(4) Câu ghép với liên từ kết hợp; (5) To-infinitive &amp; bare-infinitive. Mọi câu TN và viết lại câu đều nằm trong phạm vi này.",
        "<b>Nghe có 10 câu (2,5đ) nhưng KHÔNG khó</b> — 6/10 câu là lấy thông tin chi tiết (tên, thời gian, việc ai làm…). Chiến thuật: đọc trước nhận định, "
        "gạch chân từ khóa, nghe khớp thông tin; câu “ý chính” chỉ cần nắm câu chủ đề đầu/cuối.",
        "<b>Đọc phần 1 là văn bản thực tế (tờ rơi – quảng cáo)</b> — khác bài đọc thông thường: chỗ trống trộn lẫn từ vựng + ngữ pháp + liên từ, "
        "và các “thông tin sự kiện” (giờ, giá, điều kiện) thường được hỏi thẳng.",
        "<b>Đoạn văn viết chỉ 120–150 từ và được quyền chọn chủ đề cá nhân quan tâm</b> (một trong 3 chủ điểm) → chuẩn bị sẵn “xương” bài + từ vựng "
        "cho cả 3 chủ đề thì vào phòng thi chỉ việc lắp.",
        "Trong docx gốc có vài chỗ lệch số liệu nhỏ (ví dụ cột “Tổng” dòng Writing 1 ghi 2 || 3) — đã đối chiếu lại toàn bộ theo tỉ lệ % và bảng đặc tả: "
        "cơ cấu ở mục 1.2 là phương án nhất quán duy nhất (tổng đúng 28 TN + 7 bài TL, đúng 10 điểm).",
    ]),

    ("h2", "1.4. Chiến thuật phòng thi – phân bổ thời gian gợi ý (45 phút)"),
    ("table", {"header": ["Thứ tự", "Phần", "Thời lượng", "Kỹ thuật thực chiến"],
               "rows": [
                   ["①", "Listening (10 câu)", "10′", "Lợi dụng 30–40 giây trước mỗi đoạn: đọc hết 5 nhận định, gạch chân từ khóa (người, số, địa điểm, động từ chính). Nghe câu nào đánh luôn câu đó; lỡ 1 câu → bỏ qua ngay, nghe tiếp. True/False: bẫy ở chi tiết đảo ngược (ai làm gì), đừng suy đoán.”"],
                   ["②", "Language (6 TN)", "6′", "Làm nhanh, ưu tiên câu ngữ pháp: xác định tín hiệu (every day/now/Look!) → chọn thì; có tân ngữ + by → bị động; FANBOYS có dấu phẩy → câu ghép. Câu từ vựng: dịch nhanh 4 đáp án vào chỗ trống, loại 1–2 đáp án vô nghĩa trước.”"],
                   ["③", "Re-ordering (2 TN)", "3′", "Chỉ cần xác định câu MỞ (chào hỏi/mục đích) và câu KẾT (mong chờ/lời hứa) là loại được 2 đáp án, chọn đáp án còn lại.”"],
                   ["④", "Reading (10 câu)", "12′", "Cloze-text: đọc 1 lượt lấy mạch, điền dần từng ô, luôn nhìn từ đứng liền trước/sau ô trống. Đọc hiểu: đọc CÂU HỎI trước, sau đó scan đoạn văn tìm vùng chứa từ khóa; câu ý chính chọn phương án KHÁI QUÁT nhất, câu từ in đậm “refers to” soi 1–2 câu liền trước.”"],
                   ["⑤", "Tự luận (2 từ + 4 viết lại)", "6′", "Câu dạng từ: xác định từ loại cần điền theo vị trí (trước N → adj; sau a/an/my → N; sau be → adj; bổ nghĩa động từ → adv), thêm tiền tố/phụ tố. Viết lại câu: giữ thì – đổi cấu trúc, đếm từ an toàn, viết nháp ngắn rồi chép.”"],
                   ["⑥", "Đoạn văn 120–150 từ", "7′", "Nghĩ dàn ý 3 gạch đầu dòng trong 30 giây → viết theo “công thức 5 viên gạch” (Phần 4.4). Đếm xấp xỉ số từ (mỗi dòng ~11–12 từ × 12 dòng). Chừa 2 phút soát: -s số nhiều, V3 bị động, mạo từ.”"],
                   ["⑦", "Soát toàn đề", "1′", "Kiểm tra tô đáp án, không bỏ trắng: câu chắc chắn dưới 50% vẫn phải chọn theo cảm giác ngôn ngữ — TNKQ không trừ điểm.”"],
               ], "widths": [0.07, 0.2, 0.1, 0.63], "center": [0, 2], "fs": 8.1}),
    ("box", "note", [
        "<b>Qui ước tài liệu:</b> tất cả các đề ôn luyện, số câu, mức độ, thang điểm đều tái hiện đúng ma trận. "
        "Trong đề thi thử, đánh số liên tục: Câu 1–10 Listening · Câu 11–16 Language TN (từ vựng 11–12, ngữ pháp 13–16) · "
        "Câu 17–18 tự luận từ vựng (0,5đ/câu) · Câu 19–28 Reading TN · Câu 29–30 Re-ordering TN · Câu 31–34 viết lại câu (0,25đ/câu) · "
        "Câu 35 đoạn văn (1,0đ). Tổng: 28 câu TN × 0,25đ = 7,0đ + tự luận 3,0đ."]),

    # ============================ PART 2 ============================
    ("h1", "PHẦN 2. TỪ VỰNG THEO CHỦ ĐỀ (UNITS 1–3) – HỌC ĐỂ KHÔNG SAI MỘT CÂU NÀO"),
    ("p", "Đây là phần <b>năng suất nhất</b>: 2 câu TNKQ + 2 câu tự luận từ vựng (1,5đ), đồng thời là nguyên liệu cho cloze-text, "
          "đọc hiểu và đoạn văn. Học theo 3 lớp dưới đây: <b>① bảng từ nòng cốt</b> (gặp là phải nhận ra), "
          "<b>② cụm từ cố định</b> (thi hay kiểm tra khả năng chọn từ trong ngữ cảnh), <b>③ bảng từ họ nhà từ</b> (chuyên dụng cho 2 câu tự luận)."),

    ("h2", "2.1. Unit 1 – FAMILY LIFE (Cuộc sống gia đình)"),
    ("h3", "a) Bảng từ nòng cốt"),
    ("table", {"header": ["Từ / cụm", "Loại", "Nghĩa", "Ví dụ ngắn"],
               "rows": [
                   ["nuclear family", "n", "gia đình hạt nhân (2 thế hệ)", "A <b>nuclear family</b> has parents and children."],
                   ["extended family", "n", "gia đình lớn (nhiều thế hệ)", "I live in an <b>extended family</b> with my grandparents."],
                   ["sibling / offspring", "n", "anh/chị/em ruột / con cái", "Do you have any <b>siblings</b>?"],
                   ["only child · twin", "n", "con một · sinh đôi", "As an <b>only child</b>, she has no brothers or sisters."],
                   ["relative · neighbour", "n", "họ hàng · hàng xóm", "We often visit our <b>relatives</b> at Tết."],
                   ["housework · chore", "n", "việc nhà · việc lặt vặt", "<b>Housework</b> should be shared by all members."],
                   ["do the washing up", "v", "rửa bát", "It's your turn to <b>do the washing up</b>."],
                   ["do the laundry", "v", "giặt giũ", "My dad <b>does the laundry</b> at the weekend."],
                   ["mop / vacuum the floor", "v", "lau nhà / hút bụi", "I <b>vacuum the floor</b> and my brother mops it."],
                   ["take out the rubbish", "v", "đổ rác", "<b>Take out the rubbish</b> before you go to school."],
                   ["set / clear the table", "v", "bày / dọn bát đũa", "She <b>sets the table</b> before every meal."],
                   ["tidy up", "v", "dọn gọn gàng", "<b>Tidy up</b> your bedroom, please."],
                   ["look after", "v", "chăm sóc", "I <b>look after</b> my baby sister after school."],
                   ["do the grocery shopping", "v", "đi chợ/mua thực phẩm", "We <b>do the grocery shopping</b> on Saturday."],
                   ["appreciate", "v", "trân trọng, biết ơn", "We <b>appreciate</b> all the things you do."],
                   ["share", "v", "chia sẻ, san việc", "Everyone <b>shares</b> the housework in my family."],
                   ["hardworking", "adj", "chăm chỉ", "My mother is the most <b>hardworking</b> person I know."],
                   ["caring · supportive", "adj", "giàu tình thương · luôn ủng hộ", "A <b>supportive</b> family makes you confident."],
                   ["reliable · honest", "adj", "đáng tin · trung thực", "You can be <b>reliable</b> — she never breaks a promise."],
                   ["generous · selfish", "adj", "hào phóng · ích kỷ", "He is <b>generous</b> with his time and money."],
                   ["lazy · stubborn", "adj", "lười · bướng bỉnh", "My cat is <b>lazy</b> and a bit <b>stubborn</b>."],
                   ["argument · get on well", "n / v", "cuộc cãi vã · hòa thuận", "We never have <b>arguments</b>; we <b>get on really well</b>."],
               ], "widths": [0.22, 0.08, 0.26, 0.44], "center": [1], "fs": 8.0}),

    ("h3", "b) Unit 2 – HUMANS AND THE ENVIRONMENT (Con người và môi trường)"),
    ("table", {"header": ["Từ / cụm", "Loại", "Nghĩa", "Ví dụ ngắn"],
               "rows": [
                   ["pollution (air/water/noise)", "n", "ô nhiễm không khí/nước/tiếng ồn", "Traffic <b>pollution</b> is the worst in big cities."],
                   ["pollute", "v", "làm ô nhiễm", "Factories <b>pollute</b> the river with waste water."],
                   ["deforestation", "n", "nạn phá rừng", "<b>Deforestation</b> destroys many animals' homes."],
                   ["global warming · greenhouse effect", "n", "nóng lên toàn cầu · hiệu ứng nhà kính", "<b>Global warming</b> makes the weather change quickly."],
                   ["climate change", "n", "biến đổi khí hậu", "<b>Climate change</b> brings stronger storms."],
                   ["drought · flood · erosion", "n", "hạn hán · lũ lụt · xói mòn", "Farmers suffer from <b>drought</b> every summer."],
                   ["endangered species", "n", "loài có nguy cơ tuyệt chủng", "The saola is an <b>endangered species</b>."],
                   ["habitat loss", "n", "mất môi trường sống", "Rice fields cause <b>habitat loss</b> for wild animals."],
                   ["litter / rubbish / waste", "n", "rác", "Don't drop <b>litter</b> in the park."],
                   ["disposable products", "n", "đồ dùng một lần", "We use too many <b>disposable products</b>."],
                   ["plastic bag / packet", "n", "túi/ gói nhựa", "Bring a cloth bag instead of a <b>plastic bag</b>."],
                   ["reuse · reduce · recycle (3R)", "v", "dùng lại · giảm bớt · tái chế", "<b>Reduce</b> your plastic, <b>reuse</b> your bags, <b>recycle</b> your bottles."],
                   ["sort the waste", "v", "phân loại rác", "Our school <b>sorts the waste</b> into three bins."],
                   ["pick up litter", "v", "nhặt rác", "Students <b>picked up litter</b> along the beach."],
                   ["throw away", "v", "vứt đi", "Don't <b>throw away</b> those bottles — we can reuse them."],
                   ["save energy / water / paper", "v", "tiết kiệm điện/nước/giấy", "<b>Save energy</b> by turning off the lights."],
                   ["public transport", "n", "giao thông công cộng", "Go by <b>public transport</b> to cut CO₂."],
                   ["renewable energy", "n", "năng lượng tái tạo", "Solar and wind are <b>renewable energy</b> sources."],
                   ["environmentally friendly", "adj", "thân thiện môi trường", "Paper straws are more <b>environmentally friendly</b>."],
                   ["plant trees · make a difference", "v", "trồng cây · tạo khác biệt tích cực", "Small actions <b>make a difference</b>."],
                   ["raise people's awareness", "v", "nâng cao nhận thức", "Posters help <b>raise awareness</b> of clean water."],
                   ["run out of", "v", "cạn kiệt, dùng hết", "The world may <b>run out of</b> oil this century."],
                   ["cut down", "v", "đốn, hạ (cây)", "People <b>cut down</b> thousands of trees every year."],
                   ["come up with (an idea)", "v", "nghĩ ra (ý tưởng)", "Our class <b>came up with</b> a green plan."],
                   ["use up · waste", "v", "dùng hết · lãng phí", "Don't <b>waste</b> clean water."],
               ], "widths": [0.24, 0.07, 0.27, 0.42], "center": [1], "fs": 8.0}),

    ("h3", "c) Unit 3 – MUSIC (Âm nhạc)"),
    ("table", {"header": ["Từ / cụm", "Loại", "Nghĩa", "Ví dụ ngắn"],
               "rows": [
                   ["pop · rock · jazz · blues", "n", "các thể loại nhạc phổ biến", "<b>Jazz</b> began in the southern USA."],
                   ["classical · folk music", "n", "nhạc thính phòng · dân ca", "My grandma loves <b>folk music</b> of each region."],
                   ["rap / hip-hop · EDM · country", "n", "nhạc rap · nhạc điện tử · nhạc đồng quê", "<b>EDM</b> is energetic but sometimes too loud."],
                   ["musician · singer · vocalist", "n", "nhạc sĩ, nghệ sĩ · ca sĩ", "Son Tung M-TP is a famous Vietnamese <b>singer</b>."],
                   ["composer · songwriter · lyricist", "n", "người viết nhạc · viết lời", "The <b>composer</b> wrote the music; the <b>lyricist</b> wrote the words."],
                   ["guitarist · drummer · violinist", "n", "người chơi ghi-ta · trống · violin", "The <b>drummer</b> keeps the band's beat."],
                   ["conductor · orchestra · band", "n", "nhạc trưởng · dàn nhạc · ban nhạc", "The <b>conductor</b> raised her hands and the <b>orchestra</b> began."],
                   ["instrument: guitar, piano, drums, violin, flute, trumpet, saxophone, cello, harp", "n", "các nhạc cụ", "She learned to play the <b>flute</b> at eight."],
                   ["melody · rhythm · beat · tune", "n", "giai điệu · nhịp · phách", "The <b>melody</b> is simple but beautiful."],
                   ["lyrics", "n", "lời bài hát", "I love the <b>lyrics</b> of this indie song."],
                   ["song · track · album · hit", "n", "bài hát · bản thu · album · bản hit", "Their new <b>album</b> has ten <b>tracks</b>."],
                   ["perform · perform a song", "v", "biểu diễn", "The band will <b>perform</b> three new songs."],
                   ["rehearse · practice", "v", "tập dợt · luyện tập", "They <b>rehearse</b> every Friday evening."],
                   ["concert · show · gig", "n", "buổi hòa nhạc · buổi diễn", "We won tickets to the charity <b>concert</b>."],
                   ["stage · venue · audience · fan", "n", "sân khấu · địa điểm · khán giả · người hâm mộ", "The <b>audience</b> stood up at the end of the show."],
                   ["compete · competition · contest", "v / n", "thi · cuộc thi", "She won first prize in the singing <b>contest</b>."],
                   ["award · win a prize", "n / v", "giải thưởng · đoạt giải", "The song <b>won</b> an international <b>award</b>."],
                   ["catchy", "adj", "dễ bắt tai, dễ nhớ", "The chorus is so <b>catchy</b> that I can't forget it."],
                   ["upbeat · soothing · relaxing", "adj", "sôi động · dịu nhẹ, thư giãn", "I study best with <b>soothing</b> instrumental music."],
                   ["inspiring · powerful · emotional", "adj", "cảm hứng · mạnh mẽ · giàu cảm xúc", "Her voice is <b>powerful</b> and <b>emotional</b>."],
                   ["talented · gifted", "adj", "có tài năng", "He is a <b>talented</b> young guitarist."],
                   ["live · live performance", "adj / adv", "trực tiếp · biểu diễn trực tiếp", "Seeing them <b>live</b> is my dream."],
                   ["loud · noise · noisy", "adj / n", "ồn ào · tiếng ồn", "Turn the music down — it's too <b>loud</b>!"],
                   ["play the guitar (có “the”)", "v", "chơi đàn ghi-ta", "My brother <b>plays the guitar</b> but he never plays volleyball."],
               ], "widths": [0.28, 0.08, 0.26, 0.38], "center": [1], "fs": 8.0}),

    ("box", "tip", [
        "<b>Ba mẹo chọn nhanh cho câu từ vựng (2 câu TNKQ):</b>",
        "① Nhìn từ ngay SAU ô trống: nếu là danh từ → ô trống cần tính từ (a ______ person); nếu sau là <i>to + V</i> / <i>of + N</i> → chỗ trống là danh từ/động từ.",
        "② Đọc CẢ câu để biết thái độ (+ hay –): “always helps the neighbours” → tính từ tốt (generous), không thể là noisy/lazy.",
        "③ Collocation: động từ + giới từ đi kèm phải khớp (share housework WITH sb; look AFTER parents; make a DIFFERENCE) — đáp án nào phá vỡ collocation là đáp án sai."]),

    ("h2", "2.2. Bảng “họ nhà từ” – vũ khí cho 2 câu tự luận từ vựng (1,0đ)"),
    ("p", "Đặc tả yêu cầu <b>Vận dụng: dùng đúng dạng từ trong văn cảnh</b> (danh/động/tính/trạng từ). Bảng dưới liệt kê đúng các từ họ hay ra đề ở ba chủ đề. "
          "Cách làm: xác định từ loại theo vị trí → thêm phụ tố → soát chính tả."),
    ("table", {"header": ["Chủ đề", "N (danh từ)", "V (động từ)", "Adj (tính từ)", "Adv (trạng từ)"],
               "rows": [
                   ["gia đình – quan tâm", "care", "care for", "careful / caring / careless", "carefully / carelessly"],
                   ["gia đình – thành công", "success", "succeed", "successful", "successfully"],
                   ["gia đình – hỗ trợ", "support", "support", "supportive", "supportively"],
                   ["gia đình – cân bằng", "balance", "balance", "balanced", "balancedly (hạn dùng)"],
                   ["môi trường", "environment", "(no verb)", "environmental", "environmentally"],
                   ["ô nhiễm", "pollution", "pollute", "polluted", "—"],
                   ["phá hủy", "destruction", "destroy", "destructive", "destructively"],
                   ["bảo vệ", "protection", "protect", "protective", "—"],
                   ["phát triển", "development", "develop", "developing / developed", "—"],
                   ["sắp xếp", "arrangement", "arrange", "—", "—"],
                   ["sáng tạo", "creativity", "create", "creative", "creatively"],
                   ["dự đoán", "prediction", "predict", "predictable", "—"],
                   ["an toàn", "safety", "(make safe)", "safe", "safely"],
                   ["năng lượng", "energy", "—", "energetic", "energetically"],
                   ["âm nhạc", "music", "—", "musical", "—"],
                   ["nhiệt tình", "enthusiasm", "—", "enthusiastic", "enthusiastically"],
               ], "widths": [0.2, 0.2, 0.2, 0.24, 0.22], "center": [1, 2, 3, 4], "fs": 8.1}),
    ("box", "tip", [
        "<b>Sơ đồ 5 giây chọn từ loại:</b> "
        "Trước N (a/an/my/the ___ + N) → <b>ADJ</b> · Sau to be / become / feel / look → <b>ADJ</b> · Sau a/an/the/tính từ sở hữu, làm chủ ngữ → <b>NOUN</b> · "
        "Đứng sau chủ ngữ, trước tân ngữ → <b>VERB</b> · Đứng sau động từ thường / ở cuối câu bổ nghĩa hành động → <b>ADV</b>.",
        "Phụ tố hay dùng: N: -tion, -ment, -ness, -ity, -ance · Adj: -ful, -less, -al, -ive, -able, -ing/-ed · Adv: -ly."]),

    ("h2", "2.3. 36 “cụm hay thi” – học thuộc lòng theo cặp"),
    ("table", {"header": ["Cụm tiếng Anh", "Nghĩa / chú ý", "Cụm tiếng Anh", "Nghĩa / chú ý"],
               "rows": [
                   ["take part in housework", "tham gia việc nhà", "share the tasks with sb", "san việc với ai"],
                   ["depend on one's parents", "phụ thuộc", "take care of grandparents", "chăm sóc ông bà"],
                   ["a close-knit family", "gia đình gắn bó", "set a good example", "nêu gương"],
                   ["solve a family problem", "giải quyết mâu thuẫn", "express one's feelings", "bày tỏ cảm xúc"],
                   ["protect the environment", "bảo vệ MT", "reduce plastic use", "giảm dùng nhựa"],
                   ["reuse old things", "dùng lại đồ cũ", "sort the rubbish", "phân loại rác"],
                   ["throw rubbish away", "vứt rác", "pick up litter", "nhặt rác"],
                   ["cut down forests", "phá rừng", "grow more trees", "trồng thêm cây"],
                   ["save electricity and water", "tiết kiệm điện nước", "ride a bike instead of a car", "đạp xe thay đi ô tô"],
                   ["run out of clean water", "cạn nước sạch", "make our planet greener", "làm hành tinh xanh hơn"],
                   ["raise awareness of citizens", "nâng cao nhận thức dân", "a cleaner and safer place", "nơi sạch và an toàn hơn"],
                   ["be harmful to health", "gây hại cho sức khỏe", "produce harmful gases", "thải khí độc"],
                   ["listen to music", "nghe nhạc", "play a musical instrument", "chơi nhạc cụ"],
                   ["learn to sing / dance", "học hát/múa", "perform on stage", "biểu diễn trên sân khấu"],
                   ["go to a concert", "đi hòa nhạc", "join a music club", "vào CLB âm nhạc"],
                   ["write one's own songs", "tự viết nhạc", "win the first prize", "đạt giải nhất"],
                   ["relax after school", "thư giãn sau giờ học", "feel less stressed", "bớt căng thẳng"],
                   ["share sth with sb", "chia sẻ cái gì với ai", "be interested in + N/V-ing", "y thích cái gì"],
               ], "widths": [0.28, 0.22, 0.28, 0.22], "fs": 8.0}),

    ("h3", "35 TỪ VÀNG CHO BÀI VIẾT ĐOẠN VĂN (để không bí từ lúc 18 phút cuối)"),
    ("bullets", [
        "<b>Family life:</b> share · housework · responsibility · appreciate · bond · supportive · routine · balance · argument · tidy",
        "<b>Environment:</b> pollution · reduce · reusable · bin · habit · renewable · waste (v/n) · awareness · solution · green · protect · clean up · plastic · save energy · future",
        "<b>Music:</b> instrument · melody · lyric · talented · catchy · stage · audience · relax · genre · performance · folk · modern · compete · band · sing along",
    ]),
    ("box", "note", [
        "Ma trận không có phần Pronunciation riêng. Nếu thầy cô chèn câu phát âm, các điểm hay ra của 3 unit là: "
        "<b>ending -s/-es</b> /s/–/z/–/ɪz/ (cooks, plays, washes), <b>ending -ed</b> /t/–/d/–/ɪd/ (finished, loved, washed) và "
        "<b>trọng âm 2 âm tiết</b> (PUrpose, desSIGN; HOnest, enVIRONMENT). Ôn qua là đủ."]),
]
