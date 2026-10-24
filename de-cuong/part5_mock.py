# -*- coding: utf-8 -*-
"""Phần III: Đề thi thử bám sát 100% ma trận. Transcript & đáp án ở Phần IV."""
from common import *

def passage(txt):
    return box("", [txt], bg=colors.white, border=NAVY)

def build():
    f = []
    f.append(band("PHẦN III — ĐỀ THI THỬ GIỮA HỌC KỲ 1 (BÁM SÁT MA TRẬN 2026–2027)", NAVY))
    f.append(spacer(6))
    f.append(P("ĐỀ THI THỬ SỐ 1 — MÔN: TIẾNG ANH 10 (Global Success)", "h1"))
    f.append(P("<i>Thời gian làm bài gợi ý: 60 phút (không kể thời gian phát đề/nghe). "
               "Học sinh không được sử dụng tài liệu. Hãy làm bài như thi thật: bấm giờ, làm theo thứ tự, không bỏ trống câu trắc nghiệm.</i>", "p"))
    f.append(table([
        ["Phần", "Câu", "Số câu", "Điểm"],
        ["A. LISTENING", "1 – 10", "10 TN", "2,5 (mỗi câu 0,25)"],
        ["B. LANGUAGE (Vocabulary + Grammar)", "11 – 16 (TN) + 17 – 18 (TL)", "6 TN + 2 TL", "2,5 (TN 0,25/câu; TL 0,5/câu)"],
        ["C. READING", "19 – 28", "10 TN", "2,5 (mỗi câu 0,25)"],
        ["D. WRITING", "29 – 30 (TN) + 31 – 34 (TL) + 35 (bài viết)", "2 TN + 4 TL + 1 bài", "2,5 (TN 0,25/câu; TL 0,25/câu; bài viết 1,0)"],
        ["<b>TỔNG</b>", "", "<b>28 TN + 6 câu TL + 1 bài viết</b>", "<b>10,0</b>"],
    ], [52*mm, 44*mm, 44*mm, W-140*mm], align_center_cols={1,2,3}))

    # ---- Listening ----
    f.append(P("A. LISTENING (2,5 điểm)", "h2"))
    f.append(P("<b>Part 1 (Câu 1–5).</b> <i>Listen to a conversation between Hoa and her father about their family's weekend cleaning. "
               "Decide whether each statement is True (T) or False (F).</i> (Transcript ở Phần IV, mục 4.3)", "p"))
    qs = [
        "Hoa's family clean their house together every Saturday morning.",
        "Hoa's father is going to do all the housework this weekend.",
        "Hoa is responsible for cleaning the bathroom and doing the laundry.",
        "Hoa's little brother puts his toys away and feeds the cat.",
        "This Saturday, Hoa is going to cook lunch because her mother is busy.",
    ]
    for i, q in enumerate(qs, 1):
        f.append(P(f"<b>{i}.</b> {q} &nbsp;&nbsp; <b>T / F</b>", "q"))

    f.append(P("<b>Part 2 (Câu 6–10).</b> <i>Listen to a school announcement about a Green Festival. Choose the best answer A, B, C or D.</i>", "p"))
    qs = [
        # KEY B
        ("When will the Green Festival be held?", ["Next Saturday morning", "Next Sunday morning", "This Sunday afternoon", "Next Monday morning"]),
        # KEY C
        ("Where will the main activities of the festival take place?", ["In the school library", "In the classrooms", "In the school yard", "In the school hall"]),
        # KEY D
        ("What will students exchange at the festival?", ["Old books", "Plastic bottles for cloth bags", "Used clothes", "Old paper and bottles for green plants"]),
        # KEY A
        ("Who will give a talk about saving energy at the festival?", ["A famous singer", "The school principal", "A music teacher", "A student from the Green Club"]),
        # KEY B
        ("What is the main aim of the Green Festival?", ["To find the best singers in the school", "To raise students' awareness of protecting the environment", "To collect money for a new library", "To celebrate the school's birthday"]),
    ]
    for i, (q, o) in enumerate(qs, 6): f.append(mcq(i, q, o))

    # ---- Language ----
    f.append(P("B. LANGUAGE (2,5 điểm)", "h2"))
    f.append(P("<b>Vocabulary — Trắc nghiệm (Câu 11–12).</b> <i>Choose the best answer.</i>", "p"))
    qs = [
        # KEY A (Biết)
        ("The person who earns money to support a family is called a ______.", ["breadwinner", "homemaker", "babysitter", "housekeeper"]),
        # KEY C (Hiểu)
        ("To protect the environment, we should use cloth bags instead of plastic ones because they are ______.", ["polluted", "harmful", "eco-friendly", "expensive"]),
    ]
    for i, (q, o) in enumerate(qs, 11): f.append(mcq(i, q, o))

    f.append(P("<b>Grammar (Câu 13–16).</b> <i>Choose the best answer.</i>", "p"))
    qs = [
        # KEY B
        ("My younger brother ______ his homework every evening, but now he ______ the dishes.", ["does / washes", "does / is washing", "is doing / wash", "do / washing"]),
        # KEY C
        ("Look at those dark clouds! It ______ rain soon.", ["will to", "rains", "is going to", "rain"]),
        # KEY D
        ("A lot of trees ______ around our school last spring.", ["plant", "plants", "is planted", "were planted"]),
        # KEY A
        ("The students decided ______ a “Green Sunday” to clean up the beach.", ["to organise", "organise", "organising", "organises"]),
    ]
    for i, (q, o) in enumerate(qs, 13): f.append(mcq(i, q, o))

    f.append(P("<b>Vocabulary — Tự luận vận dụng (Câu 17–18).</b> <i>Write the correct form of the word in brackets.</i>", "p"))
    f.append(openq(17, "Students should be ______ for keeping their classroom clean. (responsibility)"))
    f.append(openq(18, "Her beautiful ______ at the school concert received a big round of applause. (perform)"))


    # ---- Reading ----
    f.append(P("C. READING (2,5 điểm)", "h2"))
    f.append(P("<b>Part 1 (Câu 19–23) — Cloze text.</b> <i>Read the announcement and choose the word that best fits each blank.</i>", "p"))
    f.append(passage(
        "<b>ANNOUNCEMENT: SCHOOL TALENT SHOW</b><br/>"
        "Are you a fan of music? Do you sing, dance or play a musical (19) ______? Then don't miss our School Talent Show! "
        "The show (20) ______ held in the school hall on Friday evening, October 24. "
        "This is a wonderful chance for you (21) ______ your talent in front of teachers, friends and parents. "
        "Last year, more than 200 people came to the show, (22) ______ this year we expect an even bigger audience. "
        "If you want to take part, please sign up with your music teacher (23) ______ Wednesday. Hurry up — only fifteen performances can join the show!"))
    qs = [
        # KEY C
        ("(19)", ["concert", "audience", "instrument", "album"]),
        # KEY B
        ("(20)", ["holds", "will be held", "held", "is hold"]),
        # KEY A
        ("(21)", ["to show", "show", "shows", "showing"]),
        # KEY D
        ("(22)", ["but", "or", "because of", "so"]),
        # KEY C
        ("(23)", ["in", "on", "before", "since"]),
    ]
    for i, (q, o) in enumerate(qs, 19): f.append(mcq(i, q, o))

    f.append(P("<b>Part 2 (Câu 24–28) — Reading comprehension.</b> <i>Read the passage and choose the best answer.</i>", "p"))
    f.append(passage(
        "Music has been an important part of human life for thousands of years, and today it is more popular than ever, especially among teenagers. "
        "Many young people listen to music every day — on the bus, at home, or even while they are studying.<br/>"
        "One of the greatest benefits of music is that it helps people relax. After a long day at school, listening to a favourite song can reduce stress "
        "and make us feel happier. Slow, gentle music can also help us sleep better at night, while fast, strong music gives us energy when we exercise.<br/>"
        "Music is also a powerful way to connect people. At concerts and music festivals, thousands of fans sing together and share the same feelings, "
        "even if they do not know each other. In addition, playing a musical instrument or singing in a group teaches young people teamwork, patience and confidence. "
        "Many students who perform on stage feel more confident when they speak in front of their class.<br/>"
        "However, people should listen to music in a sensible way. Listening to music too loudly for a long time can harm our ears, and spending too many hours with headphones "
        "may make us less willing to talk with family and friends. Used wisely, music truly makes our life richer and more colourful."))
    qs = [
        # KEY B
        ("What is the main idea of the passage?", ["Teenagers should not listen to music while studying.", "Music brings many benefits, but it should be enjoyed sensibly.", "Playing an instrument is difficult for young people.", "Concerts are the best way to make friends."]),
        # KEY C
        ("According to paragraph 2, fast and strong music ______.", ["helps people sleep better", "makes people feel stressed", "gives people energy when they exercise", "should be listened to at night"]),
        # KEY A
        ("The word “<b>it</b>” in paragraph 1 refers to ______.", ["music", "human life", "a favourite song", "stress"]),
        # KEY D
        ("Which of the following is NOT mentioned as a benefit of music?", ["Reducing stress after school", "Helping people sleep better", "Building confidence when performing", "Helping students get higher marks in all subjects"]),
        # KEY B
        ("It can be inferred from the last paragraph that ______.", ["people should never use headphones", "listening to very loud music for a long time is bad for our ears", "music makes people talk less with their families in all cases", "young people should stop listening to music"]),
    ]
    for i, (q, o) in enumerate(qs, 24): f.append(mcq(i, q, o))

    # ---- Writing ----
    f.append(P("D. WRITING (2,5 điểm)", "h2"))
    f.append(P("<b>Part 1 (Câu 29–30) — Re-ordering.</b> <i>Choose the best arrangement of the sentences.</i>", "p"))
    qs = [
        ("a. Firstly, we should save water by turning off the taps while brushing our teeth.\n"
         "b. To sum up, protecting the environment starts from very small actions at home.\n"
         "c. There are simple things every student can do at home to protect the environment.\n"
         "d. Secondly, we should turn off the lights and fans when leaving a room.",
         ["c – a – d – b", "a – c – d – b", "c – d – a – b", "b – c – a – d"]),
        ("a. Linh: That sounds fun. What are you going to do there?\n"
         "b. Linh: Hi, Tuan. Are you going to the Green Festival this Sunday?\n"
         "c. Tuan: I'm going to exchange old bottles for green plants.\n"
         "d. Tuan: Yes, I am. I've already signed up with my class.",
         ["b – a – d – c", "b – d – a – c", "a – b – d – c", "b – d – c – a"]),
    ]
    for i, (q, o) in enumerate(qs, 29):
        f.append(P(f"<b>{i}.</b>", "q"))
        for line in q.split("\n"):
            f.append(P(line, "opt"))
        labels = ["A", "B", "C", "D"]
        t = Table([[Paragraph(f"<b>{labels[j]}.</b> {o[j]}", S["opt"]) for j in range(2)],
                   [Paragraph(f"<b>{labels[j]}.</b> {o[j]}", S["opt"]) for j in range(2, 4)]],
                  colWidths=[(PAGE_W-34*mm)/2]*2)
        t.setStyle(TableStyle([("LEFTPADDING", (0,0), (-1,-1), 6),
                               ("TOPPADDING", (0,0), (-1,-1), 1), ("BOTTOMPADDING", (0,0), (-1,-1), 1)]))
        f.append(t)

    f.append(P("<b>Part 2 (Câu 31–34) — Sentence transformation.</b> <i>Rewrite each sentence so that its meaning stays the same, beginning as shown.</i>", "p"))
    qs = [
        "Students planted hundreds of trees around the school last year. → Hundreds of trees ______________________________________",
        "“I'll take part in the clean-up campaign this Sunday,” said Minh. (has decided) → Minh has decided ______________________________________",
        "The show was very interesting, so a lot of students stayed until the end. → Because ______________________________________",
        "Our teacher let us sing our favourite songs at the party. (were allowed) → We ______________________________________",
    ]
    for i, q in enumerate(qs, 31):
        f.append(openq(i, q))

    f.append(P("<b>Part 3 (Câu 35) — Writing a paragraph.</b>", "p"))
    f.append(P("<i>Write a paragraph (120–150 words) about what students can do to protect the environment at school. "
               "You may use the suggestions below:</i> — follow the 3Rs (reduce, reuse, recycle); — save electricity and water; "
               "— keep the school clean and green; — raise other students' awareness. Bài viết tối thiểu 120 từ; viết ra giấy thi, "
               "chừa dòng giữa các câu cho dễ đọc.", "p"))
    for _ in range(8):
        f.append(P("________________________________________________________________________", "opt"))
    f.append(spacer(4))
    f.append(box("TỰ NHẮC TRƯỚC KHI NỘP BÀI (dành cho lúc làm đề thử ở nhà)",
                 ["Đã tô/chọn đủ 28 câu TN chưa? Còn câu TL nào bỏ trống không? Đoạn văn đã đủ ~120 từ, có Firstly/Secondly/In short chưa? "
                  "Hãy tự chấm bằng Phần IV và ghi lại điểm của từng phần vào bảng theo dõi tiến bộ (Phụ lục)."],
                 bg=LIGHT, border=NAVY))
    return f
