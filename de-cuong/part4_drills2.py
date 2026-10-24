# -*- coding: utf-8 -*-
"""Phần II (2/2): Listening, Reading, Writing drills. Transcript & đáp án ở Phần IV."""
from common import *

def passage(txt):
    return box("", [txt], bg=colors.white, border=NAVY)

def build():
    f = []
    # ---------- D. LISTENING ----------
    f.append(P("D. LISTENING — LUYỆN NGHE (2 bài × 5 câu, đúng định dạng đề thật)", "h2"))
    f.append(P("<b>Cách luyện:</b> nhờ thầy cô/bạn học/người thân đọc to <i>Transcript D1, D2</i> ở Phần IV (mục 4.3) đúng 2 lần với tốc độ tự nhiên, "
               "em chỉ nghe – không nhìn transcript. Hoặc dùng tính năng đọc văn bản (text-to-speech) trên điện thoại. Sau khi làm xong mới mở transcript để kiểm tra.", "p"))

    f.append(P("Bài D1. <i>Listen to a conversation between Lan and her brother, Minh, about household chores. "
               "Decide whether the statements are True (T) or False (F).</i>", "h3"))
    qs = [
        "Lan and her family divide the housework equally among four people.",
        "Minh is responsible for cooking dinner every day.",
        "Lan usually does the laundry at the weekend.",
        "Their father does the heavy lifting and fixes broken things.",
        "This evening, Minh is going to do the washing-up because Lan has a lot of homework.",
    ]
    for i, q in enumerate(qs, 1):
        f.append(P(f"<b>{i}.</b> {q} &nbsp;&nbsp; <b>T / F</b>", "q"))

    f.append(P("Bài D2. <i>Listen to a talk about a school music show. Choose the best answer A, B, C or D.</i>", "h3"))
    qs = [
        # KEY B
        ("When will the school music show take place?", ["On Friday morning", "On Friday evening", "On Saturday evening", "On Sunday morning"]),
        # KEY C
        ("Where will the show be held?", ["In the school library", "In the school yard", "In the school hall", "In the music room"]),
        # KEY A
        ("How many performances will there be in the show?", ["Twelve", "Ten", "Twenty", "Fifteen"]),
        # KEY D
        ("What can students do if they want to take part in the show?", ["Send an email to the music teacher", "Talk to their class teacher", "Upload a video to the school website", "Sign up at the school office before Wednesday"]),
        # KEY B
        ("What is the main purpose of the show?", ["To choose singers for the school band only", "To find young talents and raise money for poor students", "To celebrate the teachers' day", "To record an album for the school"]),
    ]
    for i, (q, o) in enumerate(qs, 1): f.append(mcq(i, q, o))

    # ---------- E. CLOZE ----------
    f.append(P("E. READING 1 — CLOZE TEXT: ĐỌC TỜ RƠI/THÔNG BÁO VÀ ĐIỀN TỪ (2 bài × 5 câu)", "h2"))
    f.append(P("Bài E1. <i>Read the leaflet and choose the word that best fits each blank.</i>", "h3"))
    f.append(passage(
        "<b>JOIN OUR GREEN LIVING CLUB!</b><br/>"
        "Do you want to live green and protect our planet? Our Green Living Club is the right place for you! "
        "The club (1) ______ set up two years ago by a group of students who love nature. "
        "Every Sunday morning, members meet at the school gate to (2) ______ the park near our school. "
        "We also collect old paper and plastic bottles (3) ______ them instead of throwing them away. "
        "Joining the club is a great way (4) ______ new friends and learn how to save energy. "
        "If you are interested (5) ______ our activities, sign up at Room 204 before Friday!"))
    qs = [
        # KEY B
        ("(1)", ["is", "was", "has", "were"]),
        # KEY C
        ("(2)", ["clean", "cleaning up", "clean up", "cleans"]),
        # KEY A
        ("(3)", ["to recycle", "recycle", "recycling", "recycles"]),
        # KEY D
        ("(4)", ["make", "making", "for make", "to make"]),
        # KEY B
        ("(5)", ["on", "in", "at", "for"]),
    ]
    for i, (q, o) in enumerate(qs, 1): f.append(mcq(i, q, o))

    f.append(P("Bài E2. <i>Read the announcement and choose the word that best fits each blank.</i>", "h3"))
    f.append(passage(
        "<b>SCHOOL MUSIC FESTIVAL — COME AND JOIN US!</b><br/>"
        "Our school's Music Festival (1) ______ place in the school hall next Saturday evening. "
        "This is a chance for talented students (2) ______ their songs and dances in front of a large audience. "
        "Last year, the festival (3) ______ by hundreds of students and parents, and everyone had a great time. "
        "The best performers will be chosen by a group of music teachers, (4) ______ the winners will receive special prizes. "
        "Don't forget (5) ______ your friends and family to the show. Entrance is free!"))
    qs = [
        # KEY C
        ("(1)", ["makes", "gives", "takes", "does"]),
        # KEY A
        ("(2)", ["to perform", "perform", "performs", "performing"]),
        # KEY B
        ("(3)", ["attends", "was attended", "has attended", "is attend"]),
        # KEY D
        ("(4)", ["but", "or", "because of", "and"]),
        # KEY C
        ("(5)", ["invite", "inviting", "to invite", "invites"]),
    ]
    for i, (q, o) in enumerate(qs, 1): f.append(mcq(i, q, o))

    # ---------- F. READING COMP ----------
    f.append(P("F. READING 2 — READING COMPREHENSION (2 bài × 5 câu)", "h2"))
    f.append(P("Bài F1. <i>Read the passage and choose the best answer.</i>", "h3"))
    f.append(passage(
        "In many modern families, both parents work outside the home, so household chores need to be shared by all family members, "
        "including children. When everyone helps with the housework, no one feels too tired, and parents have more time to rest after a long working day.<br/>"
        "Sharing chores also brings family members closer together. Cooking a meal or cleaning the house together gives parents and children time to talk, "
        "share their stories of the day and understand each other better. In this way, doing housework is not only a duty but also a chance to strengthen the family bond.<br/>"
        "Moreover, children who do chores at home often become more responsible and independent. They learn important life skills such as cooking, cleaning and managing time. "
        "These skills will be very useful when they grow up and live on their own. For example, a teenager who knows how to cook will not depend on fast food when studying far from home.<br/>"
        "Of course, the chores given to children should be suitable for their age. Young children can tidy up their toys or put books on the shelves, "
        "while older ones can help with cooking or do the laundry. When parents give clear tasks and praise children for their work, children will be happy and willing to help."))
    qs = [
        # KEY B
        ("What is the main idea of the passage?", ["Children should not do housework at home.", "Sharing household chores brings many benefits to families.", "Parents should do all the housework themselves.", "Cooking is the most important life skill for children."]),
        # KEY C
        ("According to paragraph 1, why do modern families need to share chores?", ["Because children have a lot of free time.", "Because housework is very easy nowadays.", "Because both parents often go out to work.", "Because parents want children to be tired."]),
        # KEY A
        ("The phrase “<b>strengthen the family bond</b>” in paragraph 2 is closest in meaning to ______.", ["make family relationships closer", "make family members work harder", "spend more money for the family", "build a bigger house"]),
        # KEY D
        ("Which of the following is NOT mentioned as a benefit of doing chores for children?", ["Becoming more responsible", "Learning how to cook", "Managing time better", "Getting high scores at school"]),
        # KEY B
        ("What does the word “<b>ones</b>” in the last paragraph refer to?", ["children (young children)", "children (older children)", "parents", "toys"]),
    ]
    for i, (q, o) in enumerate(qs, 1): f.append(mcq(i, q, o))

    f.append(P("Bài F2. <i>Read the passage and choose the best answer.</i>", "h3"))
    f.append(passage(
        "Nowadays, more and more young people are interested in green living. They understand that the environment is being polluted seriously "
        "and that everyone should take action to protect it. Luckily, living green does not have to be difficult or expensive. "
        "Small changes in our daily habits can make a big difference.<br/>"
        "One simple action is to reduce the use of plastic. Plastic bags and bottles take hundreds of years to break down, and they harm the soil and water. "
        "Instead of using plastic bags, shoppers can bring their own cloth bags when they go to the market. Students can also use refillable water bottles instead of buying new plastic ones every day.<br/>"
        "Another useful habit is saving energy at home and at school. Turning off the lights and electrical appliances when they are not in use is a good example. "
        "Walking or cycling for short distances not only saves energy but also helps us stay healthy and reduces our carbon footprint.<br/>"
        "In short, green living is a choice that everyone can make. If each of us changes just a few small habits, we can protect natural resources "
        "and build a cleaner, healthier planet for future generations."))
    qs = [
        # KEY C
        ("What is the best title for the passage?", ["Why plastic is useful in daily life", "The history of green living", "Small actions for a greener life", "How to produce electricity at home"]),
        # KEY A
        ("According to the passage, why should shoppers use cloth bags?", ["Because plastic bags take a very long time to break down.", "Because cloth bags are more beautiful.", "Because plastic bags are too expensive.", "Because shops no longer sell plastic bags."]),
        # KEY B
        ("The word “<b>they</b>” in paragraph 3 refers to ______.", ["short distances", "the lights and electrical appliances", "students", "small habits"]),
        # KEY D
        ("Which of the following is TRUE according to the passage?", ["Green living is difficult and expensive.", "Only adults can live green.", "Plastic breaks down very quickly in nature.", "Cycling can help reduce our carbon footprint."]),
        # KEY C
        ("It can be inferred from the passage that ______.", ["young people do not care about the environment", "living green is only for rich people", "small daily habits can help protect the planet", "saving energy is not important"]),
    ]
    for i, (q, o) in enumerate(qs, 1): f.append(mcq(i, q, o))

    # ---------- G. REORDERING ----------
    f.append(P("G. WRITING 1 — RE-ORDERING: SẮP XẾP CÂU (6 câu trắc nghiệm)", "h2"))
    f.append(P("<i>Choose the best arrangement of the sentences to make a meaningful dialogue, letter or paragraph.</i>", "p"))
    qs = [
        # KEY B
        ("a. Anna: Then let me do the washing-up for you.\n"
         "b. Anna: Hi, Mum. You look tired. Are you OK?\n"
         "c. Mum: I'm fine, dear. I've just cooked dinner for the whole family.\n"
         "d. Mum: That's very kind of you. Thank you, Anna.",
         ["a – b – c – d", "b – c – a – d", "b – a – c – d", "c – b – a – d"]),
        # KEY C
        ("a. Sharing housework also helps family members understand and love each other more.\n"
         "b. In short, every member should take part in doing household chores.\n"
         "c. Firstly, when everyone helps, no one in the family feels too tired.\n"
         "d. There are several reasons why children should share the housework with their parents.",
         ["d – a – c – b", "c – d – a – b", "d – c – a – b", "a – c – d – b"]),
        # KEY A
        ("a. Nam: I'm going to join the Green Club at school this year.\n"
         "b. Mai: Sounds great! What do members of the club do?\n"
         "c. Mai: Really? When did you decide that?\n"
         "d. Nam: Last week. We collect plastic bottles and plant trees around the school.",
         ["a – c – b – d", "a – b – c – d", "c – a – b – d", "b – a – d – c"]),
        # KEY D
        ("a. I am writing to invite you to our school's Music Festival next Saturday.\n"
         "b. Dear Lan,\n"
         "c. I hope you can come and enjoy the show with us.\n"
         "d. There will be many interesting performances by students from different classes.",
         ["b – d – a – c", "a – b – d – c", "b – c – d – a", "b – a – d – c"]),
        # KEY B
        ("a. Secondly, cycling instead of using motorbikes can reduce air pollution.\n"
         "b. To sum up, small green actions in daily life can make our city cleaner.\n"
         "c. Firstly, we should put litter in the bins and keep public places clean.\n"
         "d. There are many simple things we can do to protect the environment in our city.",
         ["d – a – c – b", "d – c – a – b", "c – d – a – b", "b – d – c – a"]),
        # KEY C
        ("a. Tom: By listening to English songs and singing along with them.\n"
         "b. Tom: Music also helps me relax after studying.\n"
         "c. Lucy: How do you learn English through music, Tom?\n"
         "d. Lucy: That sounds interesting. I think I'll try it.",
         ["c – b – a – d", "a – c – d – b", "c – a – b – d", "d – c – a – b"]),
    ]
    for i, (q, o) in enumerate(qs, 1):
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

    # ---------- H. TRANSFORMATION ----------
    f.append(P("H. WRITING 2 — SENTENCE TRANSFORMATION: VIẾT LẠI CÂU (12 câu tự luận)", "h2"))
    f.append(P("<i>Rewrite each sentence so that its meaning stays the same. Use the word(s) given or the beginning provided.</i>", "p"))
    qs = [
        "People speak English all over the world. → English ______________________________________",
        "The students cleaned up the school yard yesterday. → The school yard ______________________________________",
        "They will hold a music festival at our school next month. → A music festival ______________________________________",
        "We have decided to plant more trees around our school. → We are going ______________________________________",
        "He was very tired. He still finished the performance. → (Join the two sentences into ONE compound sentence using <b>but</b>) ______",
        "It rained heavily, so we cancelled the outdoor concert. → Because ______________________________________",
        "Mum made me do the laundry before going out. → I was ______________________________________",
        "She saves money every month. She wants to buy a new guitar. → She saves money every month to ______________________________________",
        "“I will help you with the housework,” Dad said to Mum. → Dad promised ______________________________________",
        "Don't drop litter, or the park will be dirty. → If you ______________________________________",
        "Turning off the lights is a simple way to save energy. → It is ______________________________________",
        "They should recycle plastic bottles. → Plastic bottles ______________________________________",
    ]
    for i, q in enumerate(qs, 1):
        f.append(openq(i, q))
    f.append(P("Mẹo: trước khi viết, hãy gạch dưới động từ chính của câu gốc để không chia sai thì khi viết lại.", "small"))
    return f
