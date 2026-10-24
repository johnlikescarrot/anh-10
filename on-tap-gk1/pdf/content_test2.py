# -*- coding: utf-8 -*-
"""PHAN 6 – DE ON LUYEN SO 2 (cung cau truc ma tran nhu De 1)."""
from texts import T2_FLYER, T2_PASSAGE, T2_PASSAGE_TITLE

REORDER_A = [
    ("a", "Second, they reuse plastic bottles as pencil holders and plant pots."),
    ("b", "Students of Class 10A have found simple ways to live green."),
    ("c", "To begin with, they bring their own lunch boxes, so the canteen produces less rubbish."),
    ("d", "Finally, they turn off all the lights before leaving the classroom."),
    ("e", "These small habits help their school save money and energy."),
]
REORDER_B = [
    ("a", "Mai: May I go to the music festival this weekend, Mum?"),
    ("b", "Mum: You can, but first you have to finish the laundry and tidy the yard."),
    ("c", "Mai: I'll ask my brother to help me, and we'll do it on Saturday morning."),
    ("d", "Mum: That sounds fair — have fun on Sunday!"),
]

BLOCKS = [
    ("h1", "PHẦN 6. ĐỀ ÔN LUYỆN SỐ 2 – GIỮA KÌ 1 TIẾNG ANH 10 (2026–2027)"),
    ("box", "note", [
        "Đề 2 giữ nguyên cơ cấu – thang điểm – độ khó của ma trận, đổi toàn bộ ngữ liệu để tránh “học vẹt đáp án”. "
        "TAPESCRIPT 3–4 và đáp án: Phần 7."]),

    # ---------------- PART A ----------------
    ("h2", "PART A – LISTENING (Câu 1 – 10 · 2,5 điểm)"),
    ("h3", "Câu 1 – 5: Nghe bạn Tom kể về gia đình chủ nhà ở Huế (TAPESCRIPT 3). Chọn A (True) hoặc B (False)."),
    ("qblock", [
        "<b>Câu 1.</b> Tom moved to Da Nang to work as an English teacher.<br/>A. True&nbsp;&nbsp;&nbsp;&nbsp;B. False",
        "<b>Câu 2.</b> Mr Tran is teaching Tom how to cook three Vietnamese dishes.<br/>A. True&nbsp;&nbsp;&nbsp;&nbsp;B. False",
        "<b>Câu 3.</b> The family cleans the whole house together on Sunday mornings.<br/>A. True&nbsp;&nbsp;&nbsp;&nbsp;B. False",
        "<b>Câu 4.</b> The family contract was written to settle small housework problems.<br/>A. True&nbsp;&nbsp;&nbsp;&nbsp;B. False",
        "<b>Câu 5.</b> Tom believes a happy house is a house where people help each other, not a perfect one.<br/>A. True&nbsp;&nbsp;&nbsp;&nbsp;B. False",
    ]),
    ("h3", "Câu 6 – 10: Nghe hội thoại Minh – Lan về buổi hòa nhạc (TAPESCRIPT 4). Chọn A, B hoặc C."),
    ("qblock", [
        "<b>Câu 6.</b> Why does Lan say she can't come at first?<br/>A. She has a maths test.&nbsp;&nbsp;&nbsp;B. Her cousin is arriving and her family is having a welcome dinner.&nbsp;&nbsp;&nbsp;C. She doesn't like the band.",
        "<b>Câu 7.</b> What is TRUE about the band Red Sun?<br/>A. Their song <i>Green Street</i> won the Young Musician Award.&nbsp;&nbsp;&nbsp;B. They are organizing the clean-up.&nbsp;&nbsp;&nbsp;C. Lan's cousin is in the band.",
        "<b>Câu 8.</b> Who will look after Lan's little brother?<br/>A. Minh&nbsp;&nbsp;&nbsp;B. Lan's parents&nbsp;&nbsp;&nbsp;C. Her cousin's mum",
        "<b>Câu 9.</b> Why do they have to get to the hall before 7:15?<br/>A. The contest starts early.&nbsp;&nbsp;&nbsp;B. The gate closes then and latecomers can't enter.&nbsp;&nbsp;&nbsp;C. They want to buy tickets.",
        "<b>Câu 10.</b> What is the result of the conversation?<br/>A. Lan misses the show.&nbsp;&nbsp;&nbsp;B. Lan changes her plan and they go to the show together.&nbsp;&nbsp;&nbsp;C. Minh gives the tickets to Lan's cousin.",
    ]),

    # ---------------- PART B ----------------
    ("h2", "PART B – LANGUAGE (Câu 11 – 18 · 2,5 điểm)"),
    ("h3", "I. Vocabulary & Grammar (Câu 11 – 16): chọn A, B hoặc C."),
    ("qblock", [
        "<b>Câu 11.</b> A ______ is a person who writes music for songs or orchestras.<br/>A. conductor&nbsp;&nbsp;&nbsp;B. composer&nbsp;&nbsp;&nbsp;C. drummer",
        "<b>Câu 12.</b> Don't ______ the tap running while you brush your teeth — you waste litres of water.<br/>A. let&nbsp;&nbsp;&nbsp;B. make&nbsp;&nbsp;&nbsp;C. leave",
        "<b>Câu 13.</b> I ______ this is a wonderful plan — you should really do it.<br/>A. am thinking&nbsp;&nbsp;&nbsp;B. think&nbsp;&nbsp;&nbsp;C. thinks",
        "<b>Câu 14.</b> Our music teacher let the students ______ their own songs for the school concert.<br/>A. perform&nbsp;&nbsp;&nbsp;B. to perform&nbsp;&nbsp;&nbsp;C. performing",
        "<b>Câu 15.</b> Old exercise books and plastic bottles ______ in separate bags so that they can be recycled.<br/>A. should collect&nbsp;&nbsp;&nbsp;B. should be collected&nbsp;&nbsp;&nbsp;C. should be collecting",
        "<b>Câu 16.</b> Look! The workers ______ the water pipes in our street, so we ______ use the tap water at the moment.<br/>A. are repairing / can't&nbsp;&nbsp;&nbsp;B. repair / don't have to&nbsp;&nbsp;&nbsp;C. repaired / couldn't",
    ]),
    ("h3", "II. Viết vận dụng từ vựng (Câu 17 – 18): cho dạng đúng của từ trong ngoặc – 0,5đ/câu."),
    ("qblock", [
        "<b>Câu 17.</b> Our school has made an excellent ______ to reduce plastic: water fountains in every classroom. <b>(ARRANGE)</b>",
        "<b>Câu 18.</b> Even at the age of eighty, my grandmother stays ______ and dances every morning. <b>(ENERGY)</b>",
    ]),

    # ---------------- PART C ----------------
    ("h2", "PART C – READING (Câu 19 – 28 · 2,5 điểm)"),
    ("h3", "III. Cloze-text (Câu 19 – 23): chọn từ/cấu trúc đúng nhất cho mỗi chỗ trống."),
    ("passage", [T2_FLYER], "GREEN VALLEY SUMMER MUSIC CAMP – tờ rơi quảng cáo (điền vào chỗ trống (1)–(5))"),
    ("qblock", [
        "<b>Câu 19.</b>&nbsp;&nbsp;A. and&nbsp;&nbsp;&nbsp;B. but&nbsp;&nbsp;&nbsp;C. so",
        "<b>Câu 20.</b>&nbsp;&nbsp;A. or&nbsp;&nbsp;&nbsp;B. and&nbsp;&nbsp;&nbsp;C. but",
        "<b>Câu 21.</b>&nbsp;&nbsp;A. lessons&nbsp;&nbsp;&nbsp;B. rubbish&nbsp;&nbsp;&nbsp;C. singers",
        "<b>Câu 22.</b>&nbsp;&nbsp;A. organizes&nbsp;&nbsp;&nbsp;B. is organized&nbsp;&nbsp;&nbsp;C. organizing",
        "<b>Câu 23.</b>&nbsp;&nbsp;A. to bring&nbsp;&nbsp;&nbsp;B. bring&nbsp;&nbsp;&nbsp;C. bringing",
    ]),
    ("h3", "IV. Đọc hiểu (Câu 24 – 28): chọn A, B hoặc C."),
    ("passage", [T2_PASSAGE], T2_PASSAGE_TITLE),
    ("qblock", [
        "<b>Câu 24.</b> Why did Mrs Ho start the Sunday meetings?<br/>A. To teach the children to cook.&nbsp;&nbsp;&nbsp;B. To solve small family problems before they became big.&nbsp;&nbsp;&nbsp;C. To save money for school fees.",
        "<b>Câu 25.</b> At each meeting, every member says ______.<br/>A. one thing they thank for and one thing they want to change&nbsp;&nbsp;&nbsp;B. this week's shopping list&nbsp;&nbsp;&nbsp;C. a complaint about the neighbours",
        "<b>Câu 26.</b> How is Chi's housework now?<br/>A. She cooks on two evenings and washes up once a week.&nbsp;&nbsp;&nbsp;B. She washes the dishes every day.&nbsp;&nbsp;&nbsp;C. She does no housework at all.",
        "<b>Câu 27.</b> The phrase “such simple habits” refers to ______.<br/>A. expensive gifts for children&nbsp;&nbsp;&nbsp;B. family practices like the short weekly meeting&nbsp;&nbsp;&nbsp;C. arguments at Sunday dinner",
        "<b>Câu 28.</b> What is the writer's main message?<br/>A. Families benefit from talking and sharing tasks regularly.&nbsp;&nbsp;&nbsp;B. Children must do all the housework.&nbsp;&nbsp;&nbsp;C. Sunday is the best day for family meetings.",
    ]),

    # ---------------- PART D ----------------
    ("h2", "PART D – WRITING (Câu 29 – 35 · 2,5 điểm)"),
    ("h3", "V. Re-ordering (Câu 29 – 30): chọn thứ tự sắp xếp đúng."),
    ("passage", [f"<b>{l}.</b>&nbsp;{t}" for l, t in REORDER_A],
     "Sắp xếp (a)–(e) thành đoạn văn hoàn chỉnh:"),
    ("qblock", ["<b>Câu 29.</b>&nbsp;&nbsp;A. b – c – a – d – e&nbsp;&nbsp;&nbsp;B. b – a – c – d – e&nbsp;&nbsp;&nbsp;C. c – b – a – e – d"]),
    ("passage", [f"<b>{l}.</b>&nbsp;{t}" for l, t in REORDER_B],
     "Sắp xếp (a)–(d) thành đoạn hội thoại hoàn chỉnh:"),
    ("qblock", ["<b>Câu 30.</b>&nbsp;&nbsp;A. a – b – c – d&nbsp;&nbsp;&nbsp;B. b – a – c – d&nbsp;&nbsp;&nbsp;C. a – c – b – d"]),
    ("h3", "VI. Viết lại câu, nghĩa không đổi (Câu 31 – 34) – 0,25đ/câu"),
    ("qblock", [
        "<b>Câu 31.</b> My father is repairing his old motorbike at the moment.<br/>→ His old motorbike ______________________________________ at the moment.",
        "<b>Câu 32.</b> We intend to open a second-hand uniform stall next term. (USE: BE GOING TO)<br/>→ We ______________________________________ next term.",
        "<b>Câu 33.</b> The homework was so difficult that I couldn't finish it. (USE: TOO … TO)<br/>→ The homework was ______________________________________ .",
        "<b>Câu 34.</b> Lan likes pop music. Her brother prefers folk music. (USE: BUT)<br/>→ Lan likes pop music, ______________________________________ .",
    ]),
    ("h3", "VII. Viết đoạn văn (Câu 35 – 1,0 điểm)"),
    ("passage", ["Đài phát thanh của trường đang thu thập ý kiến về “Âm nhạc và việc học”. Viết đoạn văn (120–150 từ) "
                 "nêu quan điểm của em về vai trò của âm nhạc với học sinh: em nghe nhạc khi nào, vì sao thích, "
                 "có nên nghe khi học không, lưu ý gì về âm lượng."],
     "ĐỀ BÀI – WRITING 3"),
]
