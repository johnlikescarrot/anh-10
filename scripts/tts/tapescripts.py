# -*- coding: utf-8 -*-
"""
Du lieu 04 bai nghe (Tapescripts) trich nguyen van tu PDF:
  DE_CUONG_ON_TAP_TIENG_ANH_10_GK1_2026_2027_GLOBAL_SUCCESS.pdf
  -> src/part5_answer_keys.typ (muc "Tapescripts Chuan (180-200 tu)")

Cau truc moi bai nghe:
  id        : ma bai (DE01-P1 ...)
  exam      : so de thi thu (1 hoac 2)
  part      : phan nghe (1 = True/False, 2 = MCQ)
  slug      : ten file an toan (khong dau, khong khoang trang)
  title     : mo ta ngan
  task      : "tf" (True/False) hoac "mcq" (chon dap an A/B/C/D)
  kind      : "dialogue" (hoi thoai nhieu nguoi) hoac "monologue" (doc thoai)
  intro     : loi dan chuan de thi, doc boi giong "announcer"
  blocks    : cac khoi loi noi; moi block co giong gan cu the (voice key)

Cac khoa giong (voice key) -> model ONNX, dinh nghia trong build_listening_audio.py:
  announcer : en_GB-alan-medium       (nam Anh-Anh, loi dan de thi)
  f_lessac  : en_US-lessac-medium     (nu Anh-My, giong truong thanh)
  f_hfc     : en_US-hfc_female-medium (nu Anh-My, giong tre)
  f_jenny   : en_GB-jenny_dioco-medium(nu Anh-Anh)
  m_ryan    : en_US-ryan-medium       (nam Anh-My)
"""

# ---------------------------------------------------------------------------
# DE THI THU SO 01
# ---------------------------------------------------------------------------

DE01_P1 = {
    "id": "DE01-P1",
    "exam": 1,
    "part": 1,
    "slug": "housework-conversation",
    "title": "Conversation between An and Mrs. Lan about sharing housework",
    "task": "tf",
    "kind": "dialogue",
    "intro": (
        "Part One. Listen to a conversation between An and Mrs. Lan about "
        "sharing housework in An's family. Decide whether the following "
        "statements are True or False. You will hear the recording twice. "
        "You now have thirty seconds to read the questions."
    ),
    "blocks": [
        {"speaker": "Mrs. Lan", "voice": "f_lessac", "text":
            "Good afternoon, An! Both your parents work full-time at the "
            "hospital and an engineering firm. How does your family manage "
            "all the housework every day?"},
        {"speaker": "An", "voice": "f_hfc", "text":
            "Good afternoon, Mrs. Lan! In my home, we divide household chores "
            "equally so nobody feels overloaded. My dad is a great cook, so he "
            "prepares dinner from Monday to Friday and does the heavy lifting "
            "at weekends."},
        {"speaker": "Mrs. Lan", "voice": "f_lessac", "text":
            "That sounds wonderful! What about your mother and you?"},
        {"speaker": "An", "voice": "f_hfc", "text":
            "My mother does the grocery shopping in the morning and handles "
            "the laundry. Every afternoon after school, I water the plants on "
            "our balcony and put out the rubbish. After dinner, I also help "
            "clear the table."},
        {"speaker": "Mrs. Lan", "voice": "f_lessac", "text":
            "Does your nine-year-old brother help out too, or is he too young?"},
        {"speaker": "An", "voice": "f_hfc", "text":
            "Oh, he definitely helps! He feeds our cat, folds his own clothes, "
            "and sweeps the living room floor every evening."},
        {"speaker": "Mrs. Lan", "voice": "f_lessac", "text":
            "Aren't you tired after studying all day?"},
        {"speaker": "An", "voice": "f_hfc", "text":
            "Not at all. Spending twenty minutes doing chores together gives us "
            "time to chat and laugh, so it really brings our family closer."},
    ],
}

DE01_P2 = {
    "id": "DE01-P2",
    "exam": 1,
    "part": 2,
    "slug": "minh-khoa-radio-talk",
    "title": "Radio talk about Minh Khoa, a young contestant in a national music show",
    "task": "mcq",
    "kind": "monologue",
    "intro": (
        "Part Two. Listen to a radio talk about Minh Khoa, a young contestant "
        "in a national music show. Choose the best answer, A, B, C, or D. "
        "You will hear the recording twice. You now have thirty seconds to "
        "read the questions."
    ),
    "blocks": [
        {"speaker": "Radio host", "voice": "m_ryan", "text":
            "Welcome back to Youth Spotlight! Tonight, we are talking about "
            "Minh Khoa, the sixteen-year-old finalist who has captured "
            "millions of hearts on Vietnam Melody Star. Born in a peaceful "
            "town in Nghe An, Khoa first picked up an acoustic guitar at the "
            "age of ten. Interestingly, his first music teacher was not a "
            "professional coach, but his grandfather, who taught him "
            "traditional folk tunes every summer evening."},
        {"speaker": "Radio host", "voice": "m_ryan", "text":
            "During last month's quarter-final, Khoa surprised all three "
            "judges by blending a modern pop ballad with the sound of the "
            "moon-shaped lute. Video clips of that live performance quickly "
            "reached two million views online. However, his journey has not "
            "been easy. Just two days before the semi-final night, Khoa "
            "caught a mild cold and suffered from a sore throat. Thanks to "
            "warm ginger tea and careful rest, he recovered in time to sing "
            "brilliantly."},
        {"speaker": "Radio host", "voice": "m_ryan", "text":
            "In a recent interview, Khoa shared a heartwarming plan: if he "
            "wins the top cash prize this Sunday, he will donate new guitars "
            "and flutes to rural high school music clubs so country teenagers "
            "can pursue their musical dreams too."},
    ],
}

# ---------------------------------------------------------------------------
# DE THI THU SO 02
# ---------------------------------------------------------------------------

DE02_P1 = {
    "id": "DE02-P1",
    "exam": 2,
    "part": 1,
    "slug": "eco-campus-fair-announcement",
    "title": "Announcement by Mai (Go Green Youth Club) about the Eco-Campus Fair",
    "task": "tf",
    "kind": "monologue",
    "intro": (
        "Part One. Listen to an announcement by Mai, leader of the Go Green "
        "Youth Club, about an upcoming school event. Decide whether the "
        "statements are True or False. You will hear the recording twice. "
        "You now have thirty seconds to read the questions."
    ),
    "blocks": [
        {"speaker": "Mai", "voice": "f_hfc", "text":
            "Good morning, everyone! I'm Mai, leader of our school's Go Green "
            "Youth Club, and I have an exciting announcement for this weekend. "
            "This Saturday morning, from 7:30 a.m. to 11:30 a.m., our annual "
            "Eco-Campus Fair is going to take place right in the main "
            "schoolyard."},
        {"speaker": "Mai", "voice": "f_hfc", "text":
            "Best of all, admission to every display booth and hands-on "
            "workshop is completely free for all students, parents, and "
            "teachers — you don't need to buy any entrance tickets at all! "
            "Remember to check your home carefully before coming: if you "
            "bring ten clean used plastic bottles or aluminum cans to our "
            "Green Booth, you can exchange them for a recycled paper notebook "
            "or a young green sapling."},
        {"speaker": "Mai", "voice": "f_hfc", "text":
            "At 9:30 a.m., not 10:30, talented students from Grade 10C will "
            "perform a funny fifteen-minute play about protecting sea turtles "
            "from ocean plastic pollution, followed by an acoustic music "
            "mini-show. Through this meaningful fair, our club hopes to "
            "inspire everyone to turn small green actions into daily habits "
            "both at school and at home. Bring your close friends and reusable "
            "water bottles — see you all this Saturday!"},
    ],
}

DE02_P2 = {
    "id": "DE02-P2",
    "exam": 2,
    "part": 2,
    "slug": "family-mealtime-interview",
    "title": "Interview with Dr. Hoang Minh about family mealtime routines",
    "task": "mcq",
    "kind": "dialogue",
    "intro": (
        "Part Two. Listen to an interview with Dr. Hoang Minh about family "
        "mealtime routines. Choose the best answer, A, B, C, or D. You will "
        "hear the recording twice. You now have thirty seconds to read the "
        "questions."
    ),
    "blocks": [
        {"speaker": "Host", "voice": "f_jenny", "text":
            "Welcome to Family Matters! Today Dr. Hoang Minh is sharing "
            "findings from his recent survey on urban family meals. Dr. Minh, "
            "how often do city families eat dinner together nowadays?"},
        {"speaker": "Dr. Minh", "voice": "m_ryan", "text":
            "Thank you! Because of evening classes and overtime work, busy "
            "city families in our survey share dinner only about four evenings "
            "a week on average."},
        {"speaker": "Host", "voice": "f_jenny", "text":
            "And when they do sit down together, what gets in the way of "
            "conversation?"},
        {"speaker": "Dr. Minh", "voice": "m_ryan", "text":
            "Definitely smartphones and television screens. When everyone "
            "stares at notifications or video clips, family members sit at the "
            "same table yet barely talk to one another."},
        {"speaker": "Host", "voice": "f_jenny", "text":
            "How can tenth-grade teenagers help make family meals warmer?"},
        {"speaker": "Dr. Minh", "voice": "m_ryan", "text":
            "Teenagers don't need to cook complicated feasts. Simply washing "
            "vegetables and setting the table before dinner shows care and "
            "gratitude. Our study also found that teenagers who chat regularly "
            "with their parents over dinner develop stronger communication "
            "skills and experience much lower school stress."},
        {"speaker": "Host", "voice": "f_jenny", "text":
            "What is one golden rule every household can start tonight?"},
        {"speaker": "Dr. Minh", "voice": "m_ryan", "text":
            'Keep the dinner table completely "screen-free" for just thirty '
            "minutes. That half hour builds lifelong family bonds!"},
    ],
}

EXERCISES = [DE01_P1, DE01_P2, DE02_P1, DE02_P2]
EXAMS = {
    1: {"title": "Mock Exam One", "parts": [DE01_P1, DE01_P2]},
    2: {"title": "Mock Exam Two", "parts": [DE02_P1, DE02_P2]},
}
