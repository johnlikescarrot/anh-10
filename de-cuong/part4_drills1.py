# -*- coding: utf-8 -*-
"""Phần II (1/2): Luyện tập từ vựng, ngữ pháp, dạng từ. Đáp án ở Phần IV."""
from common import *

def build():
    f = []
    f.append(band("PHẦN II — LUYỆN TẬP THEO DẠNG BÀI", PURPLE))
    f.append(spacer(6))
    f.append(P("Hãy làm bài bằng bút chì, <b>không xem đáp án trước</b>. Làm xong từng bài mới đối chiếu Phần IV, "
               "đọc kỹ giải thích và ghi lỗi sai vào Nhật ký lỗi sai (Phụ lục). Đó là cách duy nhất để điểm số tăng thật.", "p"))

    # ---------- A. VOCABULARY ----------
    f.append(P("A. VOCABULARY — TỪ VỰNG THEO UNIT (30 câu trắc nghiệm)", "h2"))
    f.append(P("Bài A1. Unit 1 — Family life. <i>Choose the best answer.</i>", "h3"))
    qs = [
        # KEY B
        ("My father works very hard because he is the main ______ in our family.", ["homemaker", "breadwinner", "housekeeper", "babysitter"]),
        # KEY C
        ("In my family, we divide the household ______ equally among all members.", ["jobs", "works", "chores", "duties"]),
        # KEY A
        ("Every Sunday, my sister does the ______ — she washes and irons all the clothes.", ["laundry", "washing-up", "cooking", "shopping"]),
        # KEY D
        ("As the eldest child, I am ______ looking after my younger brother when my parents are away.", ["grateful for", "interested in", "famous for", "responsible for"]),
        # KEY B
        ("Doing housework together is a good way to strengthen the family ______.", ["value", "bond", "routine", "character"]),
        # KEY C
        ("Mum usually goes to the market early to buy fresh ______ for the day.", ["laundries", "chores", "groceries", "appliances"]),
        # KEY A
        ("My dad often helps with the ______ because he is the strongest in the family.", ["heavy lifting", "light work", "easy task", "homework"]),
        # KEY D
        ("Children who help at home often learn the value of ______ and hard work.", ["music", "talent", "energy", "responsibility"]),
        # KEY B
        ("I am very ______ to my parents for everything they have done for me.", ["responsible", "grateful", "talented", "aware"]),
        # KEY C
        ("After dinner, it is my turn to do the ______.", ["laundry", "grocery", "washing-up", "breadwinner"]),
    ]
    for i, (q, o) in enumerate(qs, 1): f.append(mcq(i, q, o))

    f.append(P("Bài A2. Unit 2 — Humans and the environment. <i>Choose the best answer.</i>", "h3"))
    qs = [
        # KEY C
        ("Using public transport is an ______ way to travel because it produces less pollution.", ["environment", "environmentally", "eco-friendly", "eco-friend"]),
        # KEY A
        ("Cycling to school helps you reduce your carbon ______.", ["footprint", "footstep", "fingerprint", "footpath"]),
        # KEY D
        ("Air ______ from factory smoke is harmful to people's health.", ["protect", "protection", "pollute", "pollution"]),
        # KEY B
        ("Our school is going to ______ a “Green Sunday” to clean up the park.", ["set off", "set up", "take up", "give up"]),
        # KEY C
        ("We should turn off electrical ______ when we leave the room.", ["resources", "materials", "appliances", "instruments"]),
        # KEY A
        ("The campaign aims to raise students' ______ of the importance of recycling.", ["awareness", "aware", "awares", "awarenesses"]),
        # KEY B
        ("Plastic bags are not eco-friendly because they take hundreds of years to break down and ______ the soil.", ["protect", "pollute", "reduce", "recycle"]),
        # KEY D
        ("Remember the 3Rs: reduce, reuse and ______.", ["repeat", "repair", "return", "recycle"]),
        # KEY C
        ("Forests are precious ______ resources that we must protect.", ["nature", "naturally", "natural", "nation"]),
        # KEY A
        ("If we ______ water now, there may not be enough for future generations.", ["waste", "save", "use", "keep"]),
    ]
    for i, (q, o) in enumerate(qs, 1): f.append(mcq(i, q, o))

    f.append(P("Bài A3. Unit 3 — Music. <i>Choose the best answer.</i>", "h3"))
    qs = [
        # KEY B
        ("The young singer has just released a new ______ with only one song.", ["album", "single", "concert", "record"]),
        # KEY D
        ("Thousands of fans came to the stadium to watch the live ______.", ["instrument", "audience", "composition", "concert"]),
        # KEY A
        ("The ______ gave the last singer the highest score because her voice was wonderful.", ["judges", "audiences", "composers", "viewers"]),
        # KEY C
        ("He is a famous ______ who has written many popular songs.", ["judge", "audience", "songwriter", "viewer"]),
        # KEY B
        ("Her video got more than two million ______ after only one day on the Internet.", ["albums", "views", "stages", "scores"]),
        # KEY D
        ("My brother can play three musical ______: the guitar, the piano and the trumpet.", ["songs", "bands", "shows", "instruments"]),
        # KEY A
        ("The band's ______ on stage last night was so impressive that everyone stood up and clapped.", ["performance", "perform", "performer", "performing"]),
        # KEY C
        ("This talent show is a great chance for young ______ to show what they can do.", ["albums", "singles", "talents", "records"]),
        # KEY B
        ("Before the show, the singers will ______ their songs in a studio.", ["upload", "record", "reach", "watch"]),
        # KEY D
        ("The ______ sat quietly and listened to every song.", ["judges", "artists", "talents", "audience"]),
    ]
    for i, (q, o) in enumerate(qs, 1): f.append(mcq(i, q, o))

    # ---------- B. GRAMMAR ----------
    f.append(P("B. GRAMMAR — NĂM CHỦ ĐIỂM NGỮ PHÁP (38 câu trắc nghiệm)", "h2"))
    f.append(P("Bài B1. Present simple & Present continuous (8 câu)", "h3"))
    qs = [
        # KEY C
        ("My mother ______ up early every day to prepare breakfast for the family.", ["get", "gets", "is getting", "getting"]),
        # KEY A
        ("Listen! Someone ______ the piano upstairs.", ["is playing", "plays", "play", "played"]),
        # KEY D
        ("We usually ______ the housework equally, but today my sister ______ all of it because I am ill.", ["divide / does", "divides / is doing", "are dividing / does", "divide / is doing"]),
        # KEY B
        ("He ______ meat very often; he prefers vegetables.", ["doesn't eat", "isn't eating", "don't eat", "not eats"]),
        # KEY C
        ("— What is Anna doing at the moment? — She ______ for her mid-term test.", ["studies", "study", "is studying", "studying"]),
        # KEY A
        ("The sun ______ in the east and sets in the west.", ["rises", "is rising", "rise", "rising"]),
        # KEY B
        ("I ______ this word now. Can you explain it again?", ["don't understand", "am not understanding", "not understand", "doesn't understand"]),
        # KEY D
        ("Look! The children ______ the dishes after the party.", ["wash", "washes", "is washing", "are washing"]),
    ]
    for i, (q, o) in enumerate(qs, 1): f.append(mcq(i, q, o))

    f.append(P("Bài B2. <i>will</i> & <i>be going to</i> (8 câu)", "h3"))
    qs = [
        # KEY B
        ("— I've decided to live green. — Really? What ______ do?", ["will you", "are you going to", "do you", "did you"]),
        # KEY C
        ("Watch out! You ______ drop that glass vase!", ["will to", "are go to", "are going to", "shall"]),
        # KEY A
        ("— The classroom is so dirty. — Don't worry. I ______ clean it now.", ["will", "will to", "am going", "shall to"]),
        # KEY D
        ("I think our school ______ the music contest this year.", ["wins", "winning", "won", "will win"]),
        # KEY B
        ("We ______ a clean-up campaign next Sunday. Everything has been prepared.", ["will helps", "are going to hold", "holds yesterday", "held"]),
        # KEY C
        ("She has saved enough money. She ______ a new guitar.", ["buys", "bought", "is going to buy", "buy"]),
        # KEY A
        ("— Would you like something to drink? — I ______ a glass of orange juice, please.", ["will have", "am have", "had", "has"]),
        # KEY D
        ("Promise me you ______ off the lights before leaving.", ["turns", "turned", "is turn", "will turn"]),
    ]
    for i, (q, o) in enumerate(qs, 1): f.append(mcq(i, q, o))

    f.append(P("Bài B3. Passive voice (8 câu)", "h3"))
    qs = [
        # KEY C
        ("Millions of plastic bottles ______ every year.", ["throw away", "throws away", "are thrown away", "is thrown away"]),
        # KEY A
        ("The school yard ______ by the students yesterday morning.", ["was cleaned up", "cleaned up", "is cleaned up", "cleans up"]),
        # KEY B
        ("A music show ______ at our school next Friday.", ["will hold", "will be held", "holds", "held"]),
        # KEY D
        ("English ______ in many countries around the world.", ["speaks", "speak", "spoke", "is spoken"]),
        # KEY C
        ("The trees in our garden ______ by my grandfather last spring.", ["plant", "plants", "were planted", "are plant"]),
        # KEY A
        ("Electricity should ______ when it is not needed.", ["be saved", "save", "saves", "saving"]),
        # KEY B
        ("This song ______ by a very famous composer in 1998.", ["wrote", "was written", "is write", "writes"]),
        # KEY D
        ("The classroom ______ every day by the students on duty.", ["cleans", "clean", "cleaned yesterday", "is cleaned"]),
    ]
    for i, (q, o) in enumerate(qs, 1): f.append(mcq(i, q, o))

    f.append(P("Bài B4. Compound sentences — <i>and / but / or / so</i> (6 câu)", "h3"))
    qs = [
        # KEY C
        ("The singer practised every day, ______ she won the first prize.", ["but", "or", "so", "because of"]),
        # KEY A
        ("He wanted to join the band, ______ he couldn't play any instrument.", ["but", "and", "so", "or"]),
        # KEY B
        ("Hurry up, ______ we will be late for the concert.", ["and", "or", "so", "but"]),
        # KEY D
        ("My sister sings beautifully, ______ she plays the piano very well.", ["or", "so that", "but", "and"]),
        # KEY C
        ("It was raining heavily, ______ the outdoor concert was cancelled.", ["but", "or", "so", "and"]),
        # KEY A
        ("You can join the Green Club, ______ you can take part in the music show.", ["or", "so", "because", "but"]),
    ]
    for i, (q, o) in enumerate(qs, 1): f.append(mcq(i, q, o))

    f.append(P("Bài B5. To-infinitive & Bare infinitive (8 câu)", "h3"))
    qs = [
        # KEY B
        ("She decided ______ the school music club this year.", ["join", "to join", "joining", "joins"]),
        # KEY C
        ("My mother made me ______ the washing-up before going out.", ["to do", "doing", "do", "does"]),
        # KEY A
        ("Please let me ______ you with the heavy lifting.", ["help", "to help", "helps", "helping"]),
        # KEY D
        ("Students go to the Green Club ______ about protecting the environment.", ["learn", "learns", "learning", "to learn"]),
        # KEY B
        ("Our teacher encouraged us ______ part in the talent show.", ["take", "to take", "taking", "takes"]),
        # KEY C
        ("Music can ______ people feel relaxed after a hard day.", ["to help", "helps", "help", "helped"]),
        # KEY A
        ("He promised ______ off all the electrical appliances before leaving home.", ["to turn", "turn", "turns", "turning"]),
        # KEY D
        ("It is important for everyone ______ the environment.", ["protect", "protects", "protecting", "to protect"]),
    ]
    for i, (q, o) in enumerate(qs, 1): f.append(mcq(i, q, o))

    # ---------- C. WORD FORM ----------
    f.append(P("C. WORD FORM — DÙNG ĐÚNG DẠNG CỦA TỪ (10 câu tự luận — đúng dạng “Vận dụng” trong ma trận)", "h2"))
    f.append(P("<i>Write the correct form of the word in brackets to complete each sentence.</i>", "p"))
    qs = [
        "Sharing housework teaches children ______ and independence. (responsible)",
        "We must take ______ action to protect our planet before it is too late. (environment)",
        "Air ______ is getting worse in big cities because of traffic fumes. (pollute)",
        "Her ______ on stage last night made the whole audience stand up and clap. (perform)",
        "The judges were impressed by his ______ voice and stage style. (music)",
        "I am very ______ for my parents' love and support. (grate)",
        "We should raise students' ______ of saving energy at school. (aware)",
        "He is a ______ young singer who can also play the trumpet. (talent)",
        "The ______ of the new song took the composer nearly a year. (compose)",
        "Doing chores together is really ______ for the whole family. (benefit)",
    ]
    for i, q in enumerate(qs, 1):
        f.append(openq(i, q))
    return f
