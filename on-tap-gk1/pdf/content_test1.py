# -*- coding: utf-8 -*-
"""PHAN 5 – DE ON LUYEN SO 1.
Đánh số liên tục 1–35: 28 câu TN (0,25đ) xen kẽ hợp lý, tự luận gồm 2 câu từ vựng (0,5đ),
4 câu viết lại (0,25đ) và 1 đoạn văn (1,0đ). Tổng 10đ = đúng ma trận."""
from texts import T1_FLYER, T1_FLYER_TITLE, T1_PASSAGE, T1_PASSAGE_TITLE

REORDER_A = [
    ("a", "Hoa: Hi David, you look tired. What's the matter?"),
    ("b", "Hoa: That sounds hard! But you should keep your promise to the team."),
    ("c", "David: I promised to help the environment club plant trees tomorrow morning, but I have a maths test then."),
    ("d", "Hoa: Why not talk to your teacher? She might let you take the test early."),
    ("e", "David: Good idea. Thank you, Hoa!"),
]
REORDER_B = [
    ("a", "First, we are going to collect rubbish along the beach near our school this Saturday morning."),
    ("b", "We are writing to tell you about our class field trip!"),
    ("c", "After that, we will visit the art museum and listen to a student music show in the afternoon."),
    ("d", "Please bring a hat, and don't forget your camera!"),
    ("e", "We hope you will join us!"),
]

BLOCKS = [
    ("h1", "PHẦN 5. ĐỀ ÔN LUYỆN SỐ 1 – GIỮA KÌ 1 TIẾNG ANH 10 (2026–2027)"),
    ("box", "note", [
        "Bấm giờ <b>45 phút</b>, làm như thi thật, không tuốt từ vựng. Câu 1–10: đọc to TAPESCRIPT 1–2 ở Phần 7 (hai lượt) "
        "hoặc nhờ bạn đọc. Đáp án + giải thích + biểu điểm đoạn văn: <b>PHẦN 7</b> — chỉ mở sau khi nộp bài. "
        "Cơ cấu: A · Listening 1–10 · B · Language 11–18 · C · Reading 19–28 · D · Writing 29–35."]),

    # ---------------- PART A ----------------
    ("h2", "PART A – LISTENING (Câu 1 – 10 · 2,5 điểm)"),
    ("h3", "Câu 1 – 5: Nghe đoạn kể về ngày thứ Bảy của Mai (TAPESCRIPT 1). Chọn A (True) hoặc B (False)."),
    ("qblock", [
        "<b>Câu 1.</b> Mai's family starts doing the housework together on Saturday morning.<br/>A. True&nbsp;&nbsp;&nbsp;&nbsp;B. False",
        "<b>Câu 2.</b> Mai's mother cooks breakfast and waters the plants.<br/>A. True&nbsp;&nbsp;&nbsp;&nbsp;B. False",
        "<b>Câu 3.</b> Nam carries the heavy bags at the market because he is strong.<br/>A. True&nbsp;&nbsp;&nbsp;&nbsp;B. False",
        "<b>Câu 4.</b> Mai's family works all Saturday and never relaxes at the weekend.<br/>A. True&nbsp;&nbsp;&nbsp;&nbsp;B. False",
        "<b>Câu 5.</b> Mai believes sharing housework saves time and brings the family closer.<br/>A. True&nbsp;&nbsp;&nbsp;&nbsp;B. False",
    ]),
    ("h3", "Câu 6 – 10: Nghe hội thoại Lan – Minh về kế hoạch Chủ nhật (TAPESCRIPT 2). Chọn A, B hoặc C."),
    ("qblock", [
        "<b>Câu 6.</b> Where is the clean-up activity this Sunday?<br/>A. at school&nbsp;&nbsp;&nbsp;B. at West Lake&nbsp;&nbsp;&nbsp;C. at the Youth Centre",
        "<b>Câu 7.</b> What does Lan remind Minh to bring?<br/>A. gloves and a reusable bottle&nbsp;&nbsp;&nbsp;B. plastic bags&nbsp;&nbsp;&nbsp;C. two tickets",
        "<b>Câu 8.</b> Who is performing at the music show?<br/>A. Lan's cousin&nbsp;&nbsp;&nbsp;B. Minh's brother&nbsp;&nbsp;&nbsp;C. Minh's cousin",
        "<b>Câu 9.</b> Why does Lan decide to book the tickets immediately?<br/>A. The price will rise.&nbsp;&nbsp;&nbsp;B. The tickets are nearly sold out.&nbsp;&nbsp;&nbsp;C. Minh asks her to.",
        "<b>Câu 10.</b> What do the speakers mainly talk about?<br/>A. comparing two school clubs&nbsp;&nbsp;&nbsp;B. planning a day that combines volunteering and music&nbsp;&nbsp;&nbsp;C. asking Minh to join a club",
    ]),

    # ---------------- PART B ----------------
    ("h2", "PART B – LANGUAGE (Câu 11 – 18 · 2,5 điểm)"),
    ("h3", "I. Vocabulary & Grammar (Câu 11 – 16): chọn A, B hoặc C."),
    ("qblock", [
        "<b>Câu 11.</b> My uncle is very ______; he often gives money to poor children and helps his neighbours.<br/>A. generous&nbsp;&nbsp;&nbsp;B. noisy&nbsp;&nbsp;&nbsp;C. lazy",
        "<b>Câu 12.</b> The city has planted thousands of trees to reduce air ______.<br/>A. pollute&nbsp;&nbsp;&nbsp;B. pollution&nbsp;&nbsp;&nbsp;C. poisonous",
        "<b>Câu 13.</b> My sister usually ______ breakfast for the whole family before school.<br/>A. makes&nbsp;&nbsp;&nbsp;B. is making&nbsp;&nbsp;&nbsp;C. made",
        "<b>Câu 14.</b> They bought the bus tickets yesterday, so they ______ visit their grandparents next Sunday.<br/>A. are going to&nbsp;&nbsp;&nbsp;B. will be going&nbsp;&nbsp;&nbsp;C. go to",
        "<b>Câu 15.</b> Millions of trees ______ in this area every year.<br/>A. cut down&nbsp;&nbsp;&nbsp;B. are cut down&nbsp;&nbsp;&nbsp;C. are cutting down",
        "<b>Câu 16.</b> The music festival had sold out, ______ we couldn't get any tickets.<br/>A. so&nbsp;&nbsp;&nbsp;B. but&nbsp;&nbsp;&nbsp;C. and",
    ]),
    ("h3", "II. Viết vận dụng từ vựng (Câu 17 – 18): cho dạng đúng của từ trong ngoặc – 0,5đ/câu."),
    ("qblock", [
        "<b>Câu 17.</b> After a ______ week of volunteering, the students felt really proud of the team. <b>(SUCCESS)</b>",
        "<b>Câu 18.</b> It was ______ of Peter to leave the tap running after washing his hands. <b>(CARE)</b>",
    ]),

    # ---------------- PART C ----------------
    ("h2", "PART C – READING (Câu 19 – 28 · 2,5 điểm)"),
    ("h3", "III. Cloze-text (Câu 19 – 23): chọn từ/cấu trúc đúng nhất cho mỗi chỗ trống."),
    ("passage", [T1_FLYER], "GREEN LIVING DAY – tờ rơi quảng cáo (đọc và điền vào chỗ trống (1)–(5))"),
    ("qblock", [
        "<b>Câu 19.</b>&nbsp;&nbsp;A. throw away&nbsp;&nbsp;&nbsp;B. give away&nbsp;&nbsp;&nbsp;C. throw up",
        "<b>Câu 20.</b>&nbsp;&nbsp;A. songs&nbsp;&nbsp;&nbsp;B. supermarkets&nbsp;&nbsp;&nbsp;C. factories",
        "<b>Câu 21.</b>&nbsp;&nbsp;A. hosted&nbsp;&nbsp;&nbsp;B. hosting&nbsp;&nbsp;&nbsp;C. host",
        "<b>Câu 22.</b>&nbsp;&nbsp;A. but&nbsp;&nbsp;&nbsp;B. and&nbsp;&nbsp;&nbsp;C. yet",
        "<b>Câu 23.</b>&nbsp;&nbsp;A. to drop&nbsp;&nbsp;&nbsp;B. drop&nbsp;&nbsp;&nbsp;C. dropping",
    ]),
    ("h3", "IV. Đọc hiểu (Câu 24 – 28): chọn A, B hoặc C."),
    ("passage", [T1_PASSAGE], T1_PASSAGE_TITLE),
    ("qblock", [
        "<b>Câu 24.</b> In the study, the students who worked with loud pop music ______.<br/>A. made more mistakes and finished more slowly&nbsp;&nbsp;&nbsp;B. worked faster than the silent group&nbsp;&nbsp;&nbsp;C. could not hear the questions",
        "<b>Câu 25.</b> According to Dr Nguyen, songs with words hurt performance because ______.<br/>A. they are always too quiet&nbsp;&nbsp;&nbsp;B. the brain pays attention to both the song and the task&nbsp;&nbsp;&nbsp;C. students prefer classical music",
        "<b>Câu 26.</b> What kind of music helped students feel less stressed?<br/>A. light music without words&nbsp;&nbsp;&nbsp;B. loud dance music&nbsp;&nbsp;&nbsp;C. songs written by the students",
        "<b>Câu 27.</b> The phrase “this information” refers to ______.<br/>A. the findings about music and studying&nbsp;&nbsp;&nbsp;B. the names of the two groups&nbsp;&nbsp;&nbsp;C. the length of the homework",
        "<b>Câu 28.</b> What is the main idea of the passage?<br/>A. Teenagers should give up pop music.&nbsp;&nbsp;&nbsp;B. Used wisely, music can be a study helper, not a problem.&nbsp;&nbsp;&nbsp;C. Classical music is the only good music for studying.",
    ]),

    # ---------------- PART D ----------------
    ("h2", "PART D – WRITING (Câu 29 – 35 · 2,5 điểm)"),
    ("h3", "V. Re-ordering (Câu 29 – 30): chọn thứ tự sắp xếp đúng."),
    ("passage", [f"<b>{l}.</b>&nbsp;{t}" for l, t in REORDER_A],
     "Sắp xếp (a)–(e) thành đoạn hội thoại hoàn chỉnh:"),
    ("qblock", ["<b>Câu 29.</b>&nbsp;&nbsp;A. a – c – b – d – e&nbsp;&nbsp;&nbsp;B. a – c – d – b – e&nbsp;&nbsp;&nbsp;C. c – a – e – b – d"]),
    ("passage", [f"<b>{l}.</b>&nbsp;{t}" for l, t in REORDER_B],
     "Sắp xếp (a)–(e) thành phần thân bức thư hoàn chỉnh:"),
    ("qblock", ["<b>Câu 30.</b>&nbsp;&nbsp;A. b – a – c – d – e&nbsp;&nbsp;&nbsp;B. b – c – a – d – e&nbsp;&nbsp;&nbsp;C. a – b – c – e – d"]),
    ("h3", "VI. Viết lại câu, nghĩa không đổi (Câu 31 – 34) – 0,25đ/câu"),
    ("qblock", [
        "<b>Câu 31.</b> People throw away millions of plastic bottles every day.<br/>→ Millions of plastic bottles ______________________________________ .",
        "<b>Câu 32.</b> Their team will start the recycling project next month. (USE: BE GOING TO)<br/>→ Their team ______________________________________ next month.",
        "<b>Câu 33.</b> The film was boring. We still watched it until the end. (USE: BUT)<br/>→ The film was boring, ______________________________________ .",
        "<b>Câu 34.</b> The music is too loud for the neighbours to sleep. (USE: SO … THAT)<br/>→ The music is ______________________________________ .",
    ]),
    ("h3", "VII. Viết đoạn văn (Câu 35 – 1,0 điểm)"),
    ("passage", ["Viết đoạn văn (120–150 từ) nêu quan điểm của em về việc chia sẻ công việc nhà trong gia đình. "
                 "Gợi ý: ai làm gì trong gia đình em; vì sao nên san việc; một lời khuyên cho học sinh bận rộn."],
     "ĐỀ BÀI – WRITING 3"),
]
