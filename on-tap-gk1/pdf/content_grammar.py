# -*- coding: utf-8 -*-
"""PHAN 3 – Ngu phap: 5 chuyen diem theo bang dac ta."""

BLOCKS = [
    ("h1", "PHẦN 3. NGỮ PHẨM 5 CHUYÊN ĐỀ – HỌC CÔNG THỨC, LẤY TRỌN 2,0 ĐIỂM"),
    ("lead", "Bảng đặc tả gọi tên đúng 5 chủ điểm: <b>① Hiện tại đơn vs Hiện tại tiếp diễn · ② will / be going to · ③ Câu bị động · "
             "④ Câu ghép · ⑤ To-infinitive và bare-infinitive</b>. Mỗi chủ điểm gồm: bảng cấu trúc → khi nào dùng + dấu hiệu nhận biết → "
             "so sánh nhanh → lỗi cấm gặp → mẹo nhớ → Quick Check (làm ngay, đáp án lật xuống)."),

    # ---------------- G1 ----------------
    ("h2", "3.1. PRESENT SIMPLE vs PRESENT CONTINUOUS (Unit 1)"),
    ("table", {"header": ["", "Present Simple", "Present Continuous"],
               "rows": [
                   ["Thể khẳng định", "S + V (s/es)<br/>He <b>does</b> the laundry.", "S + am/is/are + V-ing<br/>He <b>is doing</b> the laundry."],
                   ["Thể phủ định", "S + don't / doesn't + V<br/>She <b>doesn't set</b> the table.", "S + am/is/are + not + V-ing<br/>She <b>isn't setting</b> the table."],
                   ["Câu hỏi", "Do / Does + S + V?", "Am / Is / Are + S + V-ing?"],
                   ["Khi nào dùng", "(a) Thói quen, lịch cố định; (b) Sự thật, chân lý; (c) Trạng thái lâu dài; (d) Thời khóa biểu (The film <b>starts</b> at 7 p.m.)", "(a) Đang xảy ra lúc nói; (b) Tạm thời quanh hiện tại; (c) Xu hướng (More families <b>are sharing</b> housework.); (d) Kế hoạch đã sắp xếp (I'<b>m meeting</b> my cousin tonight.)"],
                   ["Dấu hiệu", "always · usually · often · sometimes · seldom · rarely · never · every day/week · once/twice a week · on Mondays", "now · right now · at the moment · at present · currently · Look! · Listen! · still"],
               ], "widths": [0.16, 0.42, 0.42], "fs": 8.2}),
    ("box", "warn", [
        "<b>Động từ chỉ cảm giác/sở hữu (stative) KHÔNG chia tiếp diễn</b> (đặc tả gọi là “non-lexical verbs”): "
        "like, love, hate, prefer, want, need, know, understand, remember, forget, believe, belong, own, seem, mean.",
        "Sai: <i>I am wanting a new guitar.</i> · Đúng: <b>I want a new guitar.</b>",
        "Nghĩa đổi – cách chia đổi: <b>think</b> (=nghĩ rằng → không V-ing: I <b>think</b> it's great) / <b>think about</b> (=đang suy nghĩ → I'<b>m thinking about</b> joining the club); "
        "<b>have</b> (=có → She <b>has</b> two siblings) / <b>have + hành động</b> (=ăn, có giờ học → She'<b>s having</b> lunch).",
        "Chia -s số ít ngôi 3: go → <b>goes</b>, study → <b>studies</b>, watch → <b>watches</b>, have → <b>has</b>."]),
    ("box", "tip", [
        "<b>Câu có dấu hiệu → chọn thì trong 3 giây:</b> thấy every/always/usually → present simple; thấy now/Look!/at the moment → V-ing. "
        "Chỉ 2 động từ hay bị bẫy: <b>see/hear</b> (=nghe/thấy → không tiếp diễn) và <b>taste/smell</b> (=có vị/mùi → không tiếp diễn)."]),
    ("h3", "Quick Check 1"),
    ("qblock", [
        "1. My sister usually ______ (cook) dinner before I come home.",
        "2. Listen! Someone ______ (play) the drums upstairs.",
        "3. Water ______ (boil) at 100°C.",
        "4. I ______ (think) this song is wonderful — I really ______ (like) it.",
        "5. We ______ (have) a family meeting at the moment.",
    ]),
    ("small", "<b>Đáp án:</b> 1 cooks (usually) · 2 is playing (Listen!) · 3 boils (sự thật) · 4 think / like (stative) · 5 are having (at the moment)."),

    # ---------------- G2 ----------------
    ("h2", "3.2. TƯƠNG LAI: will vs be going to (Unit 2)"),
    ("table", {"header": ["", "will + V", "be going to + V"],
               "rows": [
                   ["Form", "S + will (won't) + V-bare · Will + S + V?", "S + am/is/are (not) + going to + V-bare"],
                   ["Dự đoán", "Không có bằng chứng hiện tại, ý kiến chủ quan: <i>I think cities <b>will be</b> greener in 2050.</i>", "Có BẰNG CHỨNG nhìn thấy ngay: <i>Look at the black clouds! It'<b>s going to rain</b>.</i>"],
                   ["Quyết định / kế hoạch", "Quyết ĐỊNH NGAY lúc nói: <i>The box is heavy. — I'<b>ll carry</b> it!</i>", "Ý ĐỊNH đã chuẩn bị trước: <i>We'<b>re going to visit</b> grandma next Sunday — we've booked tickets.</i>"],
                   ["Chức năng khác", "Lời hứa (I <b>won't tell</b> anyone), lời đề nghị giúp (I'<b>ll open</b> the window!), đe dọa.", "(be + V-ing cũng dùng cho xếp đặt: <i>We'<b>re flying</b> to Da Nang on Friday.</i>)"],
                   ["Dấu hiệu", "tomorrow · next … · in the future · soon · I think · probably · promise", "tomorrow · next … · Look! · evidence; động từ chỉ ý định: plan, intend, decide, arrange"],
               ], "widths": [0.16, 0.42, 0.42], "fs": 8.2}),
    ("box", "warn", [
        "<b>Will + V bare</b> — không <i>will to V</i>, không <i>will V-ing</i>, không <i>will be V-ing</i> (ở mức độ này).",
        "<b>Sau liên từ chỉ thời gian (when, before, after, as soon as, until) KHÔNG dùng will cho mệnh đề đó:</b> "
        "I'll call you when I <b>get</b> home. (Không: ~~when I will get~~)",
        "Viết lại câu “It is my plan to V” → luôn là <b>be going to + V</b> (đã dự định), không phải will."]),
    ("box", "tip", [
        "<b>“TƯƠNG LAI GẦN – CÓ GÌ ĐÓ SẮP XẢY” = BE GOING TO.</b> Bằng chứng trước mặt → going to. Dự đoán trong đầu, quyết định tại chỗ → will.",
        "Nhớ 3 cặp tín hiệu: <i>I think/probably</i> → will · <i>Look! Evidence</i> → going to · <i>plan/intend/booked</i> → going to."]),
    ("h3", "Quick Check 2"),
    ("qblock", [
        "1. A: “Mum, we've run out of milk.” B: “Oh, I ______ (buy) some on my way home now.”",
        "2. Look out! That bike ______ (hit) the bin!",
        "3. They ______ (plant) 500 trees this weekend — the plan was made last week.",
        "4. I hope people ______ (use) less plastic in the future.",
        "5. When she ______ (finish) the washing up, she will go to the music club.",
    ]),
    ("small", "<b>Đáp án:</b> 1 'll buy / will buy (quyết tại chỗ) · 2 is going to hit (bằng chứng) · 3 are going to plant (đã lên kế hoạch) · "
              "4 will use (hope + tương lai xa) · 5 finishes (sau when → hiện tại đơn)."),

    # ---------------- G3 ----------------
    ("h2", "3.3. CÂU BỊ ĐỘNG (PASSIVE VOICE)"),
    ("p", "Công thức gốc: <b>S + BE (chia theo thì) + V3/ED (+ by + O)</b>. BE gánh toàn bộ thì của câu chủ động; động từ chính luôn ở cột 3."),
    ("table", {"header": ["Thì", "Chủ động", "Bị động"],
               "rows": [
                   ["Hiện tại đơn", "People <b>cut down</b> many trees.", "Many trees <b>are cut down</b>."],
                   ["Hiện tại tiếp diễn", "They <b>are building</b> a park.", "A park <b>is being built</b>."],
                   ["Quá khứ đơn", "They <b>held</b> the concert last May.", "The concert <b>was held</b> last May."],
                   ["Tương lai will", "We <b>will organize</b> a show.", "A show <b>will be organized</b>."],
                   ["be going to", "They <b>are going to publish</b> the results.", "The results <b>are going to be published</b>."],
                   ["Modal (can/should/must…)", "We <b>must sort</b> the waste.", "The waste <b>must be sorted</b>."],
               ], "widths": [0.24, 0.4, 0.36], "fs": 8.3}),
    ("h3", "4 bước biến đổi – làm theo thứ tự, không bao giờ sai"),
    ("numbers", [
        "<b>Đổi chỗ:</b> Tân ngữ câu chủ động → chủ ngữ câu bị động (chú ý số ít/nhiều: millions of bottles <b>are</b>…).",
        "<b>Chia BE</b> đúng thì của câu chủ động + hợp chủ ngữ mới.",
        "<b>Đổi động từ chính → V3/ED.</b>",
        "<b>Chủ ngữ cũ → by + O</b> (bỏ if là people, they, everyone…); cụm by đặt SAU V3 và TRƯỚC trạng từ thời gian: <i>The trees are cut down <b>by farmers</b> every year.</i>"]),
    ("box", "warn", [
        "<b>Động từ nội động KHÔNG có dạng bị động:</b> happen, die, arrive, exist, appear, belong. Sai: An accident ~~was happened~~ → <b>happened</b>.",
        "<b>Câu có 2 tân ngữ</b> (give, send, show…): hoặc <i>I <b>was given</b> a book</i>, hoặc <i>A book <b>was given to</b> me</i>.",
        "Quên <b>being / been</b>: tiếp diễn phải có being (is <b>being</b> repaired); hoàn thành phải có been (has <b>been</b> repaired)."]),
    ("box", "tip", ["<b>“BỊ ĐỘNG = BE + V3”</b> — thấy <i>by + người</i> ở cuối, chắc chắn bị động. Số bị động = số của CHỦ NGỮ MỚI, không phải của chủ ngữ cũ!"]),
    ("h3", "Quick Check 3"),
    ("qblock", [
        "1. Our house ______ (clean) every weekend by my family.",
        "2. A new playground ______ (build) in our street at the moment.",
        "3. This guitar ______ (make) in Vietnam in 2015.",
        "4. Plastic bags ______ (should / ban) in our school.",
        "5. Rewrite: “My mother is making a batch of spring rolls.” → A batch of spring rolls ______.",
    ]),
    ("small", "<b>Đáp án:</b> 1 is cleaned · 2 is being built · 3 was made · 4 should be banned · "
              "5 <b>is being made</b> by my mother (giữ thì hiện tại tiếp diễn)."),

    # ---------------- G4 ----------------
    ("h2", "3.4. CÂU GHÉP VỚI LIÊN TỪ KẾT HỢP (COMPOUND SENTENCES)"),
    ("p", "Đặc tả: hai hay nhiều mệnh đề độc lập nối bằng liên từ kết hợp. Bảy liên từ — nhớ tắt <b>FANBOYS</b>: "
          "<b>F</b>or · <b>A</b>nd · <b>N</b>or · <b>B</b>ut · <b>O</b>r · <b>Y</b>et · <b>S</b>o."),
    ("table", {"header": ["Liên từ", "Quan hệ", "Ví dụ chuẩn"],
               "rows": [
                   ["and", "thêm thông tin, hai việc cùng hướng", "I set the table <b>and</b> my brother pours the water."],
                   ["but / yet", "tương phản (yet = “nhưng thế mà”)", "The tap was leaking, <b>but</b> nobody called the plumber. · He is tired, <b>yet</b> he still does the washing up."],
                   ["or", "lựa chọn / cảnh báo (“nếu không thì”)", "Sort the waste, <b>or</b> our teacher will be angry."],
                   ["so", "kết quả", "The tickets were cheap, <b>so</b> we bought four."],
                   ["for", "nguyên do (=because, trang trọng)", "She stayed at home, <b>for</b> she had a lot of homework."],
                   ["nor", "phủ định nối tiếp (đảo trợ động từ)", "He can't sing, <b>nor can</b> he dance."],
               ], "widths": [0.14, 0.28, 0.58], "fs": 8.4}),
    ("box", "warn", [
        "<b>Dấu phẩy trước FANBOYS</b> khi nó nối 2 mệnh đề trọn vẹn: <i>The show was long<b>,</b> but it was exciting.</i> — thiếu dấu phẩy là lỗi phổ biến nhất.",
        "<b>Không dùng cặp Although… / Because… + but/so:</b> Sai: “Because it rained, <b>so</b> we stayed home.” → Đúng: <b>Because it rained, we stayed home.</b> hoặc <b>It rained, so we stayed home.</b> (chọn MỘT).",
        "<b>Cấu trúc song song:</b> vế hai phải cùng dạng với vế một: like reading <b>and</b> listening (không: ~~and to listen~~)."]),
    ("box", "tip", [
        "Chuyển câu đơn ↔ câu ghép trong viết lại câu hay gặp: <i>“A happened. B happened as a result.” → “A happened, <b>so</b> B happened.”</i> "
        "· <i>“I like pop. My friend likes jazz.” → “I like pop, <b>but</b> my friend likes jazz.”</i> — chỉ cần thêm dấu phẩy + FANBOYS, giữ nguyên hai mệnh đề."]),
    ("h3", "Quick Check 4"),
    ("qblock", [
        "1. The music was too loud ______ the neighbours called the police.",
        "2. Wash your hands ______ you will eat dirty apples. (cảnh báo)",
        "3. Find the mistake: “Although the concert was free, but the hall was small.”",
        "4. Rewrite with BUT: “Lan loves folk music. Her brother prefers rap.”",
        "5. Rewrite with SO: “Our class collected 20 kg of plastic. The school gave us a certificate.”",
    ]),
    ("small", "<b>Đáp án:</b> 1 so · 2 or · 3 bỏ <b>but</b> (Although …, Ø) · 4 “Lan loves folk music, <b>but</b> her brother prefers rap.” · "
              "5 “Our class collected 20 kg of plastic, <b>so</b> the school gave us a certificate.”"),

    # ---------------- G5 ----------------
    ("h2", "3.5. TO-INFINITIVE vs BARE-INFINITIVE"),
    ("table", {"header": ["Dùng TO + V", "Dùng V-bare (không TO)"],
               "rows": [
                   ["Sau động từ: <b>want · decide · hope · plan · agree · expect · learn · manage · offer · promise · need · would like/love · ask (sb) · tell (sb)</b>", "Sau <b>modal verbs</b>: can, could, may, might, must, should, will, would + V-bare"],
                   ["Sau <b>tính từ</b>: glad / happy / surprised / easy / difficult / important <b>to V</b> — It's easy <b>to learn</b> folk songs.", "<b>let / make / have + O + V-bare</b>: My parents let me <b>go</b>. The teacher made us <b>repeat</b> the chorus."],
                   ["<b>too + adj (+ for O) + to V</b>: The box is too heavy <b>to lift</b>.", "<b>help + (O) + (to) V</b> — có TO hay bỏ TO đều đúng: She helped me (to) <b>carry</b> the bags."],
                   ["<b>adj/adv + enough + to V</b>: Are you old enough <b>to ride</b> a bike?", "<b>see / hear / watch + O + V-bare</b> (=thấy toàn bộ): I saw him <b>leave</b>. (+V-ing = thấy đang làm: I saw him <b>leaving</b>.)"],
                   ["Mục đích: <b>(in order / so as) (not) to V</b>: We go early <b>in order not to miss</b> the show.", "Noun + to V: something <b>to drink</b> · the way <b>to do</b> it · a chance <b>to meet</b> fans."],
               ], "widths": [0.5, 0.5], "fs": 8.2}),
    ("box", "warn", [
        "<b>Nhóm ONLY + V-ing, không bao giờ + to V</b> (dễ đánh tráo): enjoy, avoid, mind, finish, suggest, practise, admit, keep (on). "
        "Sai: ~~enjoy to listen~~ → enjoy <b>listening</b>. (Đúng theo đặc tả: đây là “liên kết các dạng động từ”.)",
        "<b>let/make KHÔNG chia</b>: ~~make him to do~~ → make him <b>do</b>.",
        "Sau <b>to</b> trong be/get used to, look forward to là V-ing — nhưng đừng nhầm với to-infinitive!"]),
    ("box", "tip", [
        "<b>Cặp chuyển đổi kinh điển của Writing 2:</b> too … to ↔ so … that: "
        "The song is <b>too loud for the baby to</b> sleep = The song is <b>so loud that the baby can't</b> sleep.",
        "not … enough to ↔ too … to: He isn't <b>old enough to</b> drive = He's <b>too young to</b> drive.",
        "allow + O + to V = let + O + V: My parents <b>allow me to go</b> = They <b>let me go</b>."]),
    ("h3", "Quick Check 5"),
    ("qblock", [
        "1. My parents decided ______ (install) solar panels this summer.",
        "2. The band let their fans ______ (choose) the last song.",
        "3. Find the mistake: “My brother enjoys to do the washing up every morning.”",
        "4. Rewrite with TOO: “This music is so loud that nobody can concentrate.”",
        "5. Rewrite with SO…THAT: “The violin was too expensive for me to buy.”",
    ]),
    ("small", "<b>Đáp án:</b> 1 to install · 2 choose · 3 enjoys <b>doing</b> · 4 “This music is <b>too loud for anybody to</b> concentrate.” · "
              "5 “The violin was <b>so expensive that I couldn't</b> buy it.”"),

    ("h2", "3.6. Bảng tổng hợp 1 trang – 5 chủ điểm trước khi làm đề"),
    ("table", {"header": ["Chủ điểm", "Gợi ý nhận diện đề bài", "Bẫy hay gài"],
               "rows": [
                   ["HT đơn / tiếp diễn", "có every day / now / Look! / at the moment", "stative verbs (want, think, know…) không V-ing"],
                   ["will / be going to", "dự đoán hay kế hoạch? bằng chứng ngay trước mắt?", "sau when/while không dùng will; decide→quyết rồi dùng going to nếu có mốc"],
                   ["Bị động", "nhìn thấy <b>by…</b> hoặc chủ ngữ không thể tự làm (trees can't cut themselves)", "chia BE đúng thì; số nhiều → are/were; remember being V3"],
                   ["Câu ghép", "2 mệnh đề có chủ–vị riêng, chỗ trống giữa câu", "dấu phẩy + FANBOYS; không Although…so; song song về dạng từ"],
                   ["To-V / V-bare", "động từ trước ô trống là gì? sau modal? sau let/make?", "enjoy/avoid + V-ing; too…to; enough to"],
               ], "widths": [0.22, 0.4, 0.38], "fs": 8.3}),
]
