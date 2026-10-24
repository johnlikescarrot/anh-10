# -*- coding: utf-8 -*-
"""PART C - full practice test built to match the matrix exactly:
28 MCQ (7.0 pts) + 6 written questions + 1 paragraph (3.0 pts)."""


def build(D):
    D.pagebreak()
    D.h1("PHẦN C. ĐỀ LUYỆN TẬP MINH HOẠ (BÁM SÁT MA TRẬN)", part=True)
    D.p("**MÔN: TIẾNG ANH 10 (Global Success) - GIỮA HỌC KỲ 1 - NĂM HỌC 2026-2027**")
    D.p("*Thời gian làm bài: 45 phút (không kể thời gian giao đề). Đề gồm 28 câu trắc nghiệm (câu 1-28), "
        "6 câu tự luận (câu 29-34) và 1 bài viết (câu 35). Đáp án và giải thích chi tiết ở Phần D. "
        "Hai bài nghe được in kèm transcript ở Phần D để tự luyện (nhờ người đọc hoặc tự đọc thu âm).*", "small")

    # ---------------- PART I LISTENING 1
    D.h2("Part I. LISTENING 1 - Nghe đoạn độc thoại và chọn True (T) hoặc False (F) (câu 1-5)")
    D.psmall("(Nghe 2 lần - đoạn độc thoại khoảng 190 từ, chủ đề Family life)")
    tf = [
        ("1", "There are five people in Linh's family."),
        ("2", "Linh's father cooks dinner at weekends."),
        ("3", "Linh's mother does the grocery shopping online during the week."),
        ("4", "Nam takes out the rubbish and feeds the dog every morning."),
        ("5", "According to Linh, sharing housework helps family members become closer."),
    ]
    D.table(["Câu", "Nội dung", "T / F"], [[n, t, ""] for n, t in tf], [12, 138, 20],
            align_center_cols=(0, 2))

    # ---------------- PART II LISTENING 2
    D.h2("Part II. LISTENING 2 - Nghe đoạn hội thoại và chọn đáp án đúng A, B, C hoặc D (câu 6-10)")
    D.psmall("(Nghe 2 lần - hội thoại giữa Nam và Mai về một buổi hoà nhạc, chủ đề Music)")
    l2 = [
        ("6", "What is Nam inviting Mai to?",
         [("A", "a birthday party"), ("B", "a music concert"), ("C", "a piano lesson"), ("D", "a bus trip")]),
        ("7", "What kind of music will NOT be played at the concert?",
         [("A", "pop"), ("B", "dance music"), ("C", "rock"), ("D", "folk songs")]),
        ("8", "Who will play the piano at the concert?",
         [("A", "Nam"), ("B", "Mai"), ("C", "Nam's sister"), ("D", "Mai's sister")]),
        ("9", "How much will Mai pay for her ticket?",
         [("A", "50,000 dong"), ("B", "25,000 dong"), ("C", "100,000 dong"), ("D", "Nothing - it is free")]),
        ("10", "What does Nam ask Mai to bring?",
         [("A", "Some food and drinks"), ("B", "A piano"), ("C", "Bus number 8"), ("D", "Her student card")]),
    ]
    for n, t, o in l2:
        D.q(n, t)
        D.opts(o)

    # ---------------- PART III LANGUAGE: VOCABULARY
    D.h2("Part III. LANGUAGE - Vocabulary (câu 11-12: trắc nghiệm; câu 29-30: tự luận ở Part VIII)")
    D.q("11", "A ______ family consists of only parents and their children.")
    D.opts([("A", "extended"), ("B", "nuclear"), ("C", "crowded"), ("D", "traditional")])
    D.q("12", "Many teenagers today are ______ on pop music; they follow their favourite singers everywhere.")
    D.opts([("A", "keen"), ("B", "bored"), ("C", "scared"), ("D", "tired")])

    # ---------------- PART IV LANGUAGE: GRAMMAR
    D.h2("Part IV. LANGUAGE - Grammar: chọn đáp án đúng (câu 13-16)")
    D.q("13", "Look! The children ______ football in the school yard.")
    D.opts([("A", "play"), ("B", "are playing"), ("C", "played"), ("D", "will play")])
    D.q("14", "Nowadays, many old songs ______ again by young singers.")
    D.opts([("A", "record"), ("B", "are recorded"), ("C", "are recording"), ("D", "recorded")])
    D.q("15", "Look at those dark clouds! It ______.")
    D.opts([("A", "rains"), ("B", "is going to rain"), ("C", "will rain"), ("D", "rained")])
    D.q("16", "Mai wanted to go to the concert, ______ she had to stay home and look after her little brother.")
    D.opts([("A", "and"), ("B", "so"), ("C", "but"), ("D", "or")])

    # ---------------- PART V READING 1 - CLOZE
    D.h2("Part V. READING 1 - Đọc tờ rơi và điền từ thích hợp vào chỗ trống (câu 17-21)")
    D.box("**JOIN THE GREEN SUMMER CLUB!**\n"
          "Are you (17)______ in protecting the environment? Join our Green Summer Club today! "
          "Our members meet every Sunday morning to (18)______ rubbish around West Lake and plant trees in the "
          "neighbourhood. Last summer, the club collected (19)______ one tonne of waste and recycled most of "
          "(20)______. You don't need any experience - just a pair of gloves and a willing heart! To become a "
          "member, simply fill (21)______ the form on our website before 30 June. Together, we can make our city "
          "greener and cleaner.", kind="note")
    D.q("17", "______")
    D.opts([("A", "interest"), ("B", "interesting"), ("C", "interested"), ("D", "interestingly")])
    D.q("18", "______")
    D.opts([("A", "pick up"), ("B", "throw away"), ("C", "cut down"), ("D", "turn off")])
    D.q("19", "______")
    D.opts([("A", "more than"), ("B", "less"), ("C", "fewer"), ("D", "many")])
    D.q("20", "______")
    D.opts([("A", "it"), ("B", "them"), ("C", "its"), ("D", "their")])
    D.q("21", "______")
    D.opts([("A", "in"), ("B", "on"), ("C", "at"), ("D", "with")])

    # ---------------- PART VI READING 2
    D.h2("Part VI. READING 2 - Đọc đoạn văn và chọn đáp án đúng (câu 22-26)")
    for para in [
        "Music plays an important part in the lives of teenagers around the world. Thanks to smartphones and music "
        "apps, young people can enjoy their favourite songs anytime and anywhere - on the bus, while doing homework, "
        "or even before going to bed. A recent survey in a large city showed that more than 80% of students between "
        "13 and 18 listen to music for at least one hour every day.",
        "Teenagers have very different tastes in music. While many students love pop and dance music because of "
        "their cheerful melodies and lively rhythms, others prefer rock or hip hop. Traditional folk music, however, "
        "is the least popular choice among young listeners, although it is part of a nation's culture.",
        "Scientists have discovered that music can bring several benefits to teenagers. Listening to soft classical "
        "music before an exam can help students feel calmer and remember information better. Learning to play an "
        "instrument like the guitar or piano teaches young people patience and discipline, because they must "
        "practise regularly to improve. Music also connects people: singing in a school choir or playing in a band "
        "helps teenagers make new friends and work together as a team.",
        "Of course, music can be harmful if it is used in the wrong way. Listening to loud music through headphones "
        "for a long time may damage teenagers' hearing. Experts suggest that young people should keep the volume at "
        "a safe level and take a break after every hour of listening.",
    ]:
        D.p(para)
    D.q("22", "What is the passage mainly about?")
    D.opts([("A", "The most popular musical instruments among students"),
            ("B", "Teenagers and music: their habits, tastes, and the effects of music"),
            ("C", "How to become a professional musician"),
            ("D", "The history of pop and dance music")])
    D.q("23", "According to the survey, how many students between 13 and 18 listen to music for at least one hour a day?")
    D.opts([("A", "About 13%"), ("B", "About 18%"), ("C", "More than 80%"), ("D", "All of them")])
    D.q("24", "The word 'it' in paragraph 2 refers to ______.")
    D.opts([("A", "a nation's culture"), ("B", "traditional folk music"), ("C", "pop and dance music"), ("D", "a lively rhythm")])
    D.q("25", "Which of the following is NOT mentioned as a benefit of music?")
    D.opts([("A", "Helping students feel calmer before exams"),
            ("B", "Teaching young people patience and discipline"),
            ("C", "Helping teenagers make new friends"),
            ("D", "Helping teenagers earn money")])
    D.q("26", "What do experts advise young people to do?")
    D.opts([("A", "Stop listening to music through headphones"),
            ("B", "Listen to loud music only in the morning"),
            ("C", "Keep the volume at a safe level and take breaks"),
            ("D", "Listen to music for more than one hour without a break")])

    # ---------------- PART VII WRITING 1 - REORDERING
    D.h2("Part VII. WRITING 1 - Sắp xếp các câu thành hội thoại/đoạn văn hoàn chỉnh (câu 27-28)")
    D.q("27", "Sắp xếp các câu sau thành một hội thoại hợp lí:")
    D.opts([("a.", "Hi Nam, what are you doing this Sunday?"),
            ("b.", "Nothing special. Why?"),
            ("c.", "Would you like to join our Green Club's clean-up activity?"),
            ("d.", "That sounds interesting! Where shall we meet?"),
            ("e.", "At the school gate at 7.30 a.m. Don't be late!")], per_row=1)
    D.opts([("A", "a - b - c - d - e"), ("B", "a - c - b - d - e"), ("C", "b - a - c - e - d"), ("D", "a - b - d - c - e")])
    D.q("28", "Sắp xếp các câu sau thành một đoạn văn hoàn chỉnh:")
    D.opts([("a.", "First, we should reuse and recycle paper, plastic bottles and glass instead of throwing them away."),
            ("b.", "In conclusion, small daily actions can make our earth a better place to live."),
            ("c.", "There are several simple things that students can do to protect the environment."),
            ("d.", "Second, remember to turn off the lights and fans when leaving the classroom."),
            ("e.", "Finally, say no to single-use plastic bags and bring your own water bottle to school.")], per_row=1)
    D.opts([("A", "c - a - d - e - b"), ("B", "a - c - d - e - b"), ("C", "c - d - a - b - e"), ("D", "a - d - c - e - b")])

    # ---------------- PART VIII WRITING 2 & word form (written)
    D.h2("Part VIII. TỰ LUẬN (câu 29-34)")
    D.h3("Câu 29-30 (0,5 điểm/câu): Cho dạng đúng của từ trong ngoặc")
    D.q("29", "My parents always make important ______ together before buying anything expensive. (DECIDE)")
    D.answer_line("Đáp án: .................................................................")
    D.q("30", "Air ______ is a serious problem in many big cities in Viet Nam. (POLLUTE)")
    D.answer_line("Đáp án: .................................................................")
    D.h3("Câu 31-34 (0,25 điểm/câu): Viết lại câu sao cho nghĩa không thay đổi")
    D.q("31", "People plant a lot of trees in the park every spring.")
    D.answer_line("A lot of trees .......................................................................................")
    D.q("32", "My sister has already decided to learn how to play the guitar.")
    D.answer_line("My sister .......................................................................................")
    D.q("33", "The box is very heavy. I can't lift it.")
    D.answer_line("The box .......................................................................................")
    D.q("34", "Nam was very tired after the clean-up activity. He still helped his mother cook dinner.")
    D.answer_line("Nam was very tired after the clean-up activity, but ...............................................................")

    # ---------------- PART IX WRITING 3
    D.h2("Part IX. WRITING 3 - Viết đoạn văn (câu 35 - 1,0 điểm)")
    D.box("Write a paragraph (**120-150 words**) about **the benefits of sharing housework among family members**.\n"
          "You may use the following suggestions:\n"
          "- makes the workload lighter; everybody has more time to rest\n"
          "- teaches children life skills; makes them independent and responsible\n"
          "- helps family members understand and love one another; builds a happy, equal family\n"
          "- your own feelings or examples", kind="warn", title="ĐỀ BÀI")
