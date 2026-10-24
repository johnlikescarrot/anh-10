# -*- coding: utf-8 -*-
"""PART A (matrix analysis) + PART B (review outline)."""


def build(D):
    # ================================================== PART A
    D.h1("PHẦN A. PHÂN TÍCH MA TRẬN ĐỀ KIỂM TRA", part=True)
    D.p("Đề kiểm tra giữa học kỳ 1 môn **Tiếng Anh 10** (bộ sách *Global Success*) năm học "
        "2026-2027 được xây dựng theo Ma trận - Bảng đặc tả với phạm vi kiến thức "
        "**Unit 1: Family life - Unit 2: Humans and the environment - Unit 3: Music**. "
        "Tổng điểm toàn bài là **10 điểm**, gồm **28 câu trắc nghiệm (7,0 điểm - 70%)** và "
        "**phần tự luận: 6 câu + 1 bài viết đoạn văn (3,0 điểm - 30%)**.")

    D.h2("A1. Cấu trúc đề thi (tóm tắt từ ma trận)")
    D.table(
        ["Phần", "Dạng bài", "Số câu", "Điểm", "Mức độ (Biết/Hiểu/VD)"],
        [
            ["I. LISTENING", "Bài 1: Nghe hội thoại/độc thoại (~1,5 phút; 180-200 từ), chọn **True/False**", "5", "1,25", "3 biết + 2 hiểu"],
            ["", "Bài 2: Nghe hội thoại/độc thoại, chọn **đáp án A-D**", "5", "1,25", "3 biết + 2 hiểu"],
            ["II. LANGUAGE", "**Từ vựng** Unit 1-2-3 (trắc nghiệm)", "2", "0,5", "1 biết + 1 hiểu"],
            ["", "**Từ vựng** - cho dạng đúng của từ (tự luận)", "2", "1,0", "vận dụng"],
            ["", "**Ngữ pháp** Unit 1-2-3 (trắc nghiệm)", "4", "1,0", "2 biết + 2 hiểu"],
            ["III. READING", "Bài 1: **Cloze test** - đọc tờ rơi/quảng cáo, điền từ", "5", "1,25", "3 biết + 2 hiểu"],
            ["", "Bài 2: **Đọc hiểu** văn bản 220-250 từ, chọn A-D", "5", "1,25", "3 biết + 2 hiểu"],
            ["IV. WRITING", "Bài 1: **Sắp xếp** câu thành hội thoại/đoạn văn (trắc nghiệm)", "2", "0,5", "2 biết"],
            ["", "Bài 2: **Viết lại câu** cùng nghĩa (tự luận)", "4", "1,0", "vận dụng"],
            ["", "Bài 3: **Viết đoạn văn 120-150 từ** theo chủ đề", "1", "1,0", "vận dụng"],
            ["**TỔNG**", "**Trắc nghiệm 28 câu + Tự luận 6 câu + 1 bài viết**", "**35**", "**10**", "70% trắc nghiệm / 30% tự luận"],
        ],
        [24, 78, 12, 12, 40], align_center_cols=(2, 3, 4))

    D.h2("A2. Phạm vi kiến thức trọng tâm")
    D.bullets([
        "**Chủ đề (Topics):** Unit 1 - Family life; Unit 2 - Humans and the environment; Unit 3 - Music.",
        "**Ngữ pháp (Grammar):** (1) Hiện tại đơn & hiện tại tiếp diễn; (2) Tương lai: *will* & *be going to*; "
        "(3) Câu bị động (Passive voice); (4) Câu ghép (Compound sentences); (5) Động từ nguyên mẫu có *to* & không *to* "
        "(to-infinitive & bare infinitive).",
        "**Từ vựng (Vocabulary):** từ vựng 3 chủ điểm, đặc biệt chú ý **collocation** (kết hợp từ) và "
        "**word form** (danh từ - động từ - tính từ - trạng từ) vì phần tự luận từ vựng (1,0 điểm) hỏi dạng đúng của từ.",
    ])

    D.box("Mỗi câu trắc nghiệm đúng được **0,25 điểm**. Muốn đạt 8+ điểm, học sinh cần chắc toàn bộ phần "
          "Biết (17 câu TN) và Hiểu (11 câu TN); muốn đạt 9-10 cần làm tốt phần tự luận vận dụng: "
          "word form, viết lại câu và bài viết đoạn văn.", kind="warn", title="CHIẾN LƯỢC ĐIỂM SỐ")

    # ================================================== PART B
    D.pagebreak()
    D.h1("PHẦN B. ĐỀ CƯƠNG ÔN TẬP KIẾN THỨC", part=True)

    # ------------------------------------------------ B1 VOCAB
    D.h2("B1. TỪ VỰNG THEO CHỦ ĐIỂM")
    D.p("Học theo 3 bảng dưới đây. Với mỗi từ, cần nhớ: **nghĩa tiếng Việt - loại từ - collocation đi kèm**. "
        "Các từ in đậm là từ trọng tâm hay xuất hiện trong đề.")

    D.h3("B1.1. Unit 1 - FAMILY LIFE (Đời sống gia đình)")
    D.table(
        ["Từ / Cụm từ", "Loại từ", "Nghĩa"],
        [
            ["nuclear family / extended family", "n.", "gia đình hạt nhân / gia đình đa thế hệ (mở rộng)"],
            ["breadwinner", "n.", "trụ cột gia đình (người kiếm tiền chính)"],
            ["homemaker", "n.", "người nội trợ"],
            ["housework / household chores", "n.", "việc nhà (không đếm được) / việc vặt trong nhà"],
            ["do the housework / do the laundry / do the washing-up", "v. phr.", "làm việc nhà / giặt quần áo / rửa bát"],
            ["take out the rubbish", "v. phr.", "đổ rác"],
            ["tidy up (the room)", "v. phr.", "dọn dẹp, sắp xếp gọn gàng (phòng)"],
            ["shop for groceries / go grocery shopping", "v. phr.", "đi mua thực phẩm, đồ dùng hằng ngày"],
            ["lay / set the table", "v. phr.", "dọn bàn ăn (trước bữa ăn)"],
            ["be responsible for sth", "v. phr.", "chịu trách nhiệm về việc gì"],
            ["divide / split the housework", "v. phr.", "chia sẻ / phân chia việc nhà"],
            ["join hands (to do sth)", "v. phr.", "chung tay, cùng nhau làm gì"],
            ["heavy lifting", "n.", "việc nặng (khiêng vác)"],
            ["look after = take care of", "v. phr.", "chăm sóc, trông nom"],
            ["bring up (children)", "v. phr.", "nuôi dạy (con cái)"],
            ["generation gap", "n.", "khoảng cách thế hệ"],
            ["family values / family tradition", "n.", "giá trị / truyền thống gia đình"],
            ["close-knit (family)", "adj.", "(gia đình) gắn bó, khăng khít"],
            ["obedient", "adj.", "ngoan ngoãn, vâng lời"],
            ["supportive", "adj.", "ủng hộ, động viên, hỗ trợ"],
            ["willing (to do sth)", "adj.", "sẵn lòng, tự nguyện (làm gì)"],
            ["quality time", "n.", "thời gian chất lượng (dành cho gia đình)"],
            ["sibling / relative", "n.", "anh chị em ruột / họ hàng"],
            ["childcare", "n.", "việc chăm sóc trẻ em"],
        ],
        [62, 18, 90])

    D.h3("B1.2. Unit 2 - HUMANS AND THE ENVIRONMENT (Con người và môi trường)")
    D.table(
        ["Từ / Cụm từ", "Loại từ", "Nghĩa"],
        [
            ["the environment / environmental (adj.)", "n. / adj.", "môi trường / thuộc về môi trường"],
            ["pollution (air / water / soil / noise ~)", "n.", "ô nhiễm (không khí / nước / đất / tiếng ồn)"],
            ["polluted (adj.) / pollutant (n.)", "adj. / n.", "bị ô nhiễm / chất gây ô nhiễm"],
            ["contaminate", "v.", "làm nhiễm bẩn, làm ô nhiễm"],
            ["litter (n./v.) / littering", "n. / v.", "rác vứt bừa bãi / vứt rác bừa bãi"],
            ["rubbish / garbage / waste", "n.", "rác / rác thải / chất thải"],
            ["dump (waste)", "v.", "đổ, thải (rác, chất thải)"],
            ["reduce - reuse - recycle", "v.", "giảm thiểu - tái sử dụng - tái chế (3R)"],
            ["deforestation", "n.", "sự phá rừng"],
            ["climate change / global warming", "n.", "biến đổi khí hậu / sự nóng lên toàn cầu"],
            ["greenhouse gas emissions", "n.", "khí thải nhà kính"],
            ["carbon footprint", "n.", "lượng khí thải carbon (của cá nhân/tổ chức)"],
            ["natural resources", "n.", "tài nguyên thiên nhiên"],
            ["conserve / conservation", "v. / n.", "bảo tồn (tài nguyên) / sự bảo tồn"],
            ["protect / protection", "v. / n.", "bảo vệ / sự bảo vệ"],
            ["preserve / preservation", "v. / n.", "giữ gìn, bảo quản / sự giữ gìn"],
            ["eco-friendly = green", "adj.", "thân thiện với môi trường"],
            ["biodegradable", "adj.", "có thể phân huỷ sinh học"],
            ["single-use / disposable (plastic)", "adj.", "(đồ nhựa) dùng một lần"],
            ["endangered species", "n.", "các loài (động, thực vật) có nguy cơ tuyệt chủng"],
            ["ecosystem", "n.", "hệ sinh thái"],
            ["clean-up campaign / clean-up activity", "n.", "chiến dịch / hoạt động dọn vệ sinh"],
            ["sort (the) rubbish / waste", "v. phr.", "phân loại rác"],
            ["save / waste energy", "v. phr.", "tiết kiệm / lãng phí năng lượng"],
            ["harm (n./v.) / harmful (adj.)", "-", "tác hại / gây hại / có hại"],
        ],
        [62, 18, 90])

    D.h3("B1.3. Unit 3 - MUSIC (Âm nhạc)")
    D.table(
        ["Từ / Cụm từ", "Loại từ", "Nghĩa"],
        [
            ["pop / rock / country / folk / classical / jazz / hip hop", "n.", "nhạc pop / rock / đồng quê / dân ca / cổ điển / jazz / hip hop"],
            ["musical instrument", "n.", "nhạc cụ (piano, guitar, violin, drum, flute, saxophone, trumpet...)"],
            ["play an instrument", "v. phr.", "chơi một loại nhạc cụ"],
            ["musician / composer / singer / songwriter", "n.", "nhạc công / nhạc sĩ sáng tác / ca sĩ / ca sĩ kiêm nhạc sĩ"],
            ["band / orchestra / choir / conductor", "n.", "ban nhạc / dàn nhạc / dàn hợp xướng / nhạc trưởng"],
            ["audience", "n.", "khán giả, thính giả"],
            ["perform (v.) / performance (n.)", "v. / n.", "biểu diễn / buổi biểu diễn, tiết mục"],
            ["concert / live music / stage", "n.", "buổi hoà nhạc / nhạc sống / sân khấu"],
            ["lyrics", "n.", "lời bài hát"],
            ["melody / rhythm / beat", "n.", "giai điệu / nhịp điệu / nhịp, phách"],
            ["album / single / hit (song)", "n.", "an-bum / đĩa đơn / bài hát ăn khách"],
            ["release (v.) / record (v., n.)", "v. / n.", "phát hành / thu âm, bản thu"],
            ["talent show / judge", "n.", "chương trình tìm kiếm tài năng / giám khảo"],
            ["talented / talent", "adj. / n.", "có tài năng / tài năng"],
            ["taste in music", "n.", "gu âm nhạc"],
            ["be into / be keen on / be fond of music", "v. phr.", "yêu thích, mê âm nhạc"],
            ["give a performance", "v. phr.", "trình diễn một tiết mục"],
            ["listen to music", "v. phr.", "nghe nhạc (chú ý giới từ *to*)"],
        ],
        [62, 18, 90])

    D.h3("B1.4. Word form - Dạng thức của từ (trọng tâm phần tự luận 1,0 điểm)")
    D.p("Dạng bài: *Cho dạng đúng của từ trong ngoặc.* Hãy ghi nhớ các 'gia đình từ' sau:")
    D.table(
        ["Danh từ (n.)", "Động từ (v.)", "Tính từ (adj.)", "Trạng từ (adv.)"],
        [
            ["decision", "decide", "decisive", "decisively"],
            ["responsibility", "-", "responsible", "responsibly"],
            ["pollution / pollutant", "pollute", "polluted", "-"],
            ["protection", "protect", "protective", "-"],
            ["conservation", "conserve", "-", "-"],
            ["environment", "-", "environmental", "environmentally"],
            ["performance", "perform", "-", "-"],
            ["musician", "-", "musical", "musically"],
            ["beauty", "-", "beautiful", "beautifully"],
            ["benefit", "benefit", "beneficial", "-"],
            ["independence", "-", "independent", "independently"],
            ["creation", "create", "creative", "creatively"],
            ["appearance", "appear", "-", "-"],
            ["tradition", "-", "traditional", "traditionally"],
            ["energy", "-", "energetic", "energetically"],
        ],
        [45, 40, 45, 40])
    D.box("Mẹo làm bài word form: xác định **chỗ trống cần loại từ nào** (đứng sau mạo từ/tính từ → danh từ; "
          "sau chủ ngữ → động từ; trước danh từ hoặc sau *to be* → tính từ; bổ nghĩa cho cả câu/động từ/tính từ → trạng từ), "
          "rồi chọn đúng 'người anh em' của từ cho sẵn. Chú ý danh từ đếm được số nhiều (-s/-es).", kind="tip", title="MẸO")

    # ------------------------------------------------ B2 GRAMMAR
    D.pagebreak()
    D.h2("B2. NGỮ PHÁP TRỌNG TÂM (5 CHỦ ĐIỂM)")

    # ---- G1
    D.h3("B2.1. Hiện tại đơn & Hiện tại tiếp diễn (Present simple & Present continuous)")
    D.table(
        ["", "Hiện tại đơn (Present simple)", "Hiện tại tiếp diễn (Present continuous)"],
        [
            ["Công thức", "S + V(s/es); phủ định: don't / doesn't + V; hỏi: Do / Does + S + V?",
             "S + am / is / are + V-ing; phủ định: isn't / aren't + V-ing"],
            ["Cách dùng", "Thói quen, sự việc lặp lại; sự thật hiển nhiên; lịch trình tàu xe, giờ mở cửa",
             "Hành động đang xảy ra lúc nói; kế hoạch đã chốt trong tương lai gần; xu hướng hiện nay"],
            ["Dấu hiệu", "always, usually, often, sometimes, never, every day/week, once a week, on Mondays",
             "now, right now, at the moment, at present, currently, these days, Look!, Listen!"],
        ],
        [22, 74, 74])
    D.box("Lưu ý quan trọng:\n"
          "- **Động từ chỉ trạng thái** (state verbs) KHÔNG dùng tiếp diễn: like, love, hate, want, need, "
          "prefer, know, understand, believe, remember, belong, seem...\n"
          "   Ví dụ: She *understands* the problem. (KHÔNG dùng: is understanding)\n"
          "- **always + hiện tại tiếp diễn** diễn tả sự phàn nàn: He is always leaving his dirty clothes on the floor.",
          kind="warn", title="BẪY HAY GẶP")

    # ---- G2
    D.h3("B2.2. Tương lai: will & be going to")
    D.table(
        ["", "will", "be going to"],
        [
            ["Công thức", "S + will + V (nguyên thể); will not = won't", "S + am/is/are + going to + V (nguyên thể)"],
            ["Cách dùng", "Quyết định **ngay lúc nói**; dự đoán **không có bằng chứng** (I think/believe...); lời hứa, đề nghị, yêu cầu",
             "Dự định/kế hoạch **đã quyết định từ trước**; dự đoán **có bằng chứng ngay trước mắt**"],
            ["Ví dụ", "The phone is ringing. - I'll answer it. / I think people will live longer.",
             "We have bought the tickets. We're going to visit Ha Noi. / Look at those dark clouds! It's going to rain."],
        ],
        [22, 74, 74])

    # ---- G3
    D.h3("B2.3. Câu bị động (Passive voice)")
    D.p("Công thức chung: **S + be + V3/ed (+ by O)**. Tân ngữ của câu chủ động trở thành chủ ngữ của câu bị động; "
        "động từ *be* chia theo thì của câu chủ động.")
    D.table(
        ["Thì", "Chủ động", "Bị động", "Ví dụ"],
        [
            ["Hiện tại đơn", "V(s/es)", "am/is/are + V3/ed", "People recycle paper. → Paper is recycled."],
            ["Hiện tại tiếp diễn", "am/is/are + V-ing", "am/is/are + being + V3/ed", "They are painting the wall. → The wall is being painted."],
            ["Quá khứ đơn", "V2/ed", "was/were + V3/ed", "He wrote the song. → The song was written by him."],
            ["Tương lai (will)", "will + V", "will be + V3/ed", "They will release the album. → The album will be released."],
            ["be going to", "am/is/are going to + V", "am/is/are going to be + V3/ed", "We are going to plant trees. → Trees are going to be planted."],
            ["Động từ khuyết thiếu", "can/should/must + V", "can/should/must + be + V3/ed", "You must turn off the lights. → The lights must be turned off."],
        ],
        [30, 34, 44, 62])
    D.box("- Chủ ngữ không xác định (people, they, someone...) có thể **lược bỏ by...**: English is spoken all over the world.\n"
          "- Giữ nguyên phần đuôi câu: He is looking after the baby. → The baby is being looked after (by him).",
          kind="note", title="GHI NHỚ")

    # ---- G4
    D.h3("B2.4. Câu ghép (Compound sentences)")
    D.p("Câu ghép gồm 2 mệnh đề độc lập nối với nhau bằng **liên từ kết hợp (coordinating conjunctions)**. "
        "Mẹo nhớ: **FANBOYS**. Trước liên từ thường có dấu phẩy.")
    D.table(
        ["Liên từ", "Nghĩa / Chức năng", "Ví dụ"],
        [
            ["**F**or", "vì (giải thích lý do)", "She stayed at home, for she was ill."],
            ["**A**nd", "và (bổ sung ý cùng chiều)", "Nam plays the guitar, and his sister sings."],
            ["**N**or", "cũng không (bổ sung ý phủ định)", "He doesn't smoke, nor does he drink."],
            ["**B**ut", "nhưng (ý tương phản)", "The concert was great, but the tickets were expensive."],
            ["**O**r", "hoặc (lựa chọn)", "We can take the bus, or we can walk."],
            ["**Y**et", "vậy mà, tuy thế (tương phản, trang trọng hơn but)", "The task was hard, yet they finished on time."],
            ["**S**o", "vì vậy (kết quả)", "It rained heavily, so the match was cancelled."],
        ],
        [22, 74, 74])

    # ---- G5
    D.h3("B2.5. Động từ nguyên mẫu: to-infinitive & bare infinitive")
    D.table(
        ["Nhóm", "Công thức / Động từ", "Ví dụ"],
        [
            ["V + to-infinitive", "want, hope, decide, promise, offer, refuse, agree, learn, manage, plan, expect, afford, would like/love + to V",
             "She decided to join the music club."],
            ["V + O + to-infinitive", "ask, tell, invite, encourage, remind, advise, allow, persuade, warn, expect + O + to V",
             "My mother told me to take out the rubbish."],
            ["V + bare infinitive", "make, let, help* (+ O + V); động từ khuyết thiếu (can, will, must, should...); would rather, had better",
             "My parents let me choose my favourite instrument. (*help có thể đi với to-inf)"],
            ["Cấu trúc khác", "It is + adj + to V; too + adj + (for O) + to V; adj + enough + (for O) + to V",
             "The box is too heavy for me to lift. / She is old enough to stay at home alone."],
            ["Động từ chỉ giác quan", "see / watch / hear + O + V (hành động trọn vẹn); + O + V-ing (đang diễn ra)",
             "I saw him cross the street. / I heard them singing."],
        ],
        [34, 74, 62])

    # ---- drills
    D.h3("B2.6. Bài tập nhanh (Quick drill) - mỗi chủ điểm 4 câu")
    D.p("*Chọn đáp án đúng (đáp án ở cuối trang):*")
    drills = [
        ("1", "Listen! Someone ______ the piano upstairs.", [("A", "plays"), ("B", "is playing"), ("C", "played"), ("D", "will play")]),
        ("2", "My father usually ______ the housework at weekends.", [("A", "does"), ("B", "is doing"), ("C", "do"), ("D", "did")]),
        ("3", "I ______ my grandparents every Sunday.", [("A", "am visiting"), ("B", "visit"), ("C", "visits"), ("D", "visited")]),
        ("4", "She can't answer the phone now because she ______ a shower.", [("A", "takes"), ("B", "take"), ("C", "is taking"), ("D", "took")]),
        ("5", "Look at the black clouds! It ______ soon.", [("A", "rains"), ("B", "will rain"), ("C", "is going to rain"), ("D", "rained")]),
        ("6", "I'm thirsty. - I ______ you a glass of water.", [("A", "am going to bring"), ("B", "will bring"), ("C", "bring"), ("D", "brought")]),
        ("7", "We have made a plan, so we ______ trees along the river this Saturday.", [("A", "are going to plant"), ("B", "will plant"), ("C", "plant"), ("D", "planted")]),
        ("8", "I think robots ______ most of the housework in the future.", [("A", "are doing"), ("B", "do"), ("C", "will do"), ("D", "did")]),
        ("9", "Choose the correct passive form of: People hold a music festival here every year.", [("A", "A music festival is held here every year."), ("B", "A music festival holds here every year."), ("C", "A music festival is holding here every year."), ("D", "A music festival held here every year.")]),
        ("10", "The rubbish ______ every morning in our school.", [("A", "collects"), ("B", "is collected"), ("C", "is collecting"), ("D", "collected")]),
        ("11", "The song ______ by a famous Vietnamese composer in 1990.", [("A", "wrote"), ("B", "was written"), ("C", "is written"), ("D", "writes")]),
        ("12", "These old bottles must ______ for recycling.", [("A", "sort"), ("B", "be sorted"), ("C", "sorted"), ("D", "be sorting")]),
        ("13", "Mai wanted to go out with friends, ______ she had to finish her homework first.", [("A", "and"), ("B", "so"), ("C", "but"), ("D", "or")]),
        ("14", "Nam is good at maths, ______ his brother prefers literature.", [("A", "so"), ("B", "but"), ("C", "or"), ("D", "for")]),
        ("15", "The weather was bad, ______ the clean-up activity was postponed.", [("A", "so"), ("B", "but"), ("C", "yet"), ("D", "nor")]),
        ("16", "You can join the guitar class, ______ you can join the singing club.", [("A", "or"), ("B", "so"), ("C", "but"), ("D", "for")]),
        ("17", "My parents don't allow me ______ music too loud at night.", [("A", "play"), ("B", "to play"), ("C", "playing"), ("D", "played")]),
        ("18", "The teacher made the students ______ the classroom after school.", [("A", "to clean"), ("B", "cleaning"), ("C", "clean"), ("D", "to cleaning")]),
        ("19", "This exercise is difficult. Nobody can do it. (Nối bằng cấu trúc too...to)", [("A", "This exercise is too difficult for anybody to do."), ("B", "This exercise is enough difficult to do."), ("C", "This exercise is too difficult do."), ("D", "This exercise is so difficult to anybody.")]),
        ("20", "It is important ______ rubbish into the right bins.", [("A", "sort"), ("B", "sorting"), ("C", "to sort"), ("D", "sorted")]),
    ]
    for n, t, o in drills:
        D.q(n, t)
        D.opts(o, per_row=2)
    D.box("1.B  2.A  3.B  4.C  5.C  6.B  7.A  8.C  9.A  10.B  11.B  12.B  13.C  14.B  15.A  16.A  17.B  18.C  19.A  20.C",
          kind="tip", title="ĐÁP ÁN QUICK DRILL (B2.6)")

    # ------------------------------------------------ B3 SKILLS
    D.pagebreak()
    D.h2("B3. KỸ NĂNG LÀM BÀI THEO TỪNG DẠNG")

    D.h3("B3.1. Nghe hiểu (Listening)")
    D.bullets([
        "**Trước khi nghe (45-60 giây vàng):** đọc kỹ câu hỏi/từ khoá; với True/False hãy đoán trước thông tin nào dễ bị 'bẫy'.",
        "**Trong khi nghe:** nghe **từ khoá** và **ý được paraphrase** (ví dụ: 'not cheap' = 'expensive'); chú ý các từ chỉ sự đối lập "
        "(but, however) vì đáp án thường nằm sau chúng.",
        "**Bẫy thường gặp:** số liệu gần giống nhau, thông tin bị phủ định ở vế sau, chủ ngữ bị đổi (đáp án nói về người khác).",
        "Với câu hỏi ý chính: chọn phương án **bao quát cả bài**, tránh phương án chỉ đúng 1 chi tiết nhỏ.",
    ])

    D.h3("B3.2. Cloze test (điền từ vào tờ rơi/quảng cáo)")
    D.bullets([
        "Xác định **loại từ** cần điền (danh từ/động từ/tính từ/trạng từ) dựa vào vị trí trong câu.",
        "Chú ý **collocation** (fill in the form, take part in, be interested in...) và **giới từ** cố định.",
        "Chú ý **từ tham chiếu**: it/they/this/these phải khớp với danh từ đứng trước (số ít/nhiều, đếm được/không đếm được).",
        "Điền xong, **đọc lại cả đoạn** để kiểm tra tính logic.",
    ])

    D.h3("B3.3. Đọc hiểu (Reading comprehension)")
    D.bullets([
        "Câu hỏi **ý chính** (mainly about / best title): đọc câu mở đầu + câu cuối mỗi đoạn.",
        "Câu hỏi **chi tiết** (according to the passage): tìm từ khoá trong bài, đối chiếu từng phương án - đáp án đúng thường được **viết lại bằng từ khác**.",
        "Câu hỏi **tham chiếu** ('it/they' refers to...): thay lần lượt danh từ gần nhất vào chỗ của từ đó, chọn phương án hợp nghĩa.",
        "Câu hỏi **từ vựng** ('...' is closest in meaning to): đoán nghĩa dựa vào ngữ cảnh câu chứa nó.",
        "Câu **NOT/EXCEPT**: đánh dấu 3 thông tin CÓ trong bài → loại trừ.",
    ])

    D.h3("B3.4. Sắp xếp hội thoại / đoạn văn (Re-ordering)")
    D.bullets([
        "Hội thoại: tìm **câu mở đầu** (lời chào/câu hỏi), bắt cặp **hỏi - đáp**, chú ý từ nối (Well..., Sure..., Oh...).",
        "Đoạn văn: tìm **câu chủ đề** (khái quát nhất, không chứa từ nối chi tiết); sắp xếp ý theo tín hiệu "
        "First/Second/Finally; câu có In short/In conclusion luôn đứng cuối.",
    ])

    D.h3("B3.5. Viết lại câu (Sentence transformation) - 5 dạng kinh điển")
    D.table(
        ["Dạng", "Câu gốc", "Viết lại"],
        [
            ["Chủ động → Bị động", "People plant a lot of trees every spring.", "A lot of trees **are planted** every spring."],
            ["will ↔ be going to", "I've decided to learn the guitar. →", "I **am going to learn** the guitar."],
            ["2 câu đơn → câu ghép", "The music was loud. We still enjoyed it.", "The music was loud, **but** we still enjoyed it."],
            ["too...to / enough...to", "The box is very heavy. I can't lift it.", "The box is **too** heavy **for me to** lift."],
            ["to-infinitive khác", "Let's take the bus. → / Why don't we...? ", "**Why don't we** take the bus?"],
        ],
        [40, 65, 65])
    D.box("Nguyên tắc: **KHÔNG đổi nghĩa** của câu; giữ nguyên thì; kiểm tra lại chính tả, mạo từ, giới từ sau khi viết. "
          "Đề GK1 thường rơi vào 4 dạng đầu (bám sát 5 chủ điểm ngữ pháp của ma trận).", kind="warn", title="NGUYÊN TẮC")

    D.h3("B3.6. Viết đoạn văn 120-150 từ (Writing paragraph)")
    D.p("Cấu trúc 3 phần kinh điển (5-7 câu):")
    D.bullets([
        "**Mở đoạn (1 câu):** câu chủ đề nêu thẳng vấn đề. *There are several reasons why... / I am going to write about...*",
        "**Thân đoạn (3-4 câu):** 2-3 ý, mỗi ý bắt đầu bằng *First(ly), ... / Second, ... / Moreover, ... / For example, ...*",
        "**Kết đoạn (1 câu):** tóm tắt hoặc nêu cảm nghĩ. *In short, ... / All in all, ...*",
    ])
    D.box("Thang điểm gợi ý (1,0 điểm): Nội dung đủ ý, bám chủ đề: 0,4 - Ngữ pháp & từ vựng (đúng thì, dùng từ Unit 1-3): 0,3 - "
          "Bố cục & từ nối mạch lạc: 0,2 - Chính tả & trình bày: 0,1. Hãy tuân thủ yêu cầu độ dài 120-150 từ trong đề.",
          kind="note", title="TIÊU CHÍ CHẤM")

    D.h4("Bài mẫu 1 - Benefits of sharing housework (Unit 1) - 139 từ")
    D.p("*Sharing housework brings many benefits to every member of the family. First, it makes the workload lighter. "
        "When all members join hands, chores such as cooking, doing the laundry and tidying up are finished more quickly, "
        "so everybody has more time to rest. Second, sharing housework teaches children important life skills. By doing "
        "chores, they learn how to look after themselves and become more independent and responsible. Third, it helps "
        "family members understand and love one another more. Working together gives them chances to talk, share and "
        "laugh, which brings the family closer. In addition, when fathers share the housework with mothers, children "
        "learn a good lesson about equality. In short, sharing housework is not only about keeping the house clean, "
        "but also about building a warm and close-knit family.*")

    D.h4("Bài mẫu 2 - Simple ways to protect the environment (Unit 2) - 136 từ")
    D.p("*Protecting the environment is the duty of everyone, and there are several simple things that students can do. "
        "First, we should follow the three Rs: reduce, reuse and recycle. For example, we can reuse old paper and "
        "recycle plastic bottles instead of throwing them away. Second, we need to save energy at home and at school "
        "by turning off the lights, fans and computers when we do not use them. Third, we should say no to single-use "
        "plastic bags and bring our own water bottles to school. Finally, taking part in clean-up activities and "
        "planting trees in our neighbourhood can make our living area greener and cleaner. In short, small daily "
        "actions can bring big changes to our environment.*")

    D.h4("Bài mẫu 3 - The benefits of music (Unit 3) - 134 từ")
    D.p("*Music plays an important part in our lives and brings us many benefits. First, music helps us relax and "
        "reduce stress. After hours of studying, listening to my favourite songs makes me feel calm and happy again. "
        "Second, music helps us study better. Some scientists say that soft classical music can improve our "
        "concentration and memory. Third, learning to play an instrument such as the guitar or the piano teaches us "
        "patience and discipline, because we have to practise regularly. Finally, music connects people. When we sing "
        "in a choir or play in a school band, we can make new friends and learn to work as a team. In short, music is "
        "not only entertainment but also a wonderful friend of everyone.*")
