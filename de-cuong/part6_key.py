# -*- coding: utf-8 -*-
"""Phần IV (1/2): Đáp án & giải thích bài luyện Phần II + transcripts."""
from common import *

def keytable(rows, widths=None):
    return table([["Câu", "Đáp án", "Giải thích ngắn"]] + rows,
                 widths or [14*mm, 28*mm, W-42*mm], align_center_cols={0})

def build():
    f = []
    f.append(band("PHẦN IV — ĐÁP ÁN, GIẢI THÍCH, TRANSCRIPT & BÀI MẪU", GREEN))
    f.append(spacer(6))
    f.append(P("4.1. Đáp án Bài A — Vocabulary", "h2"))
    f.append(P("A1. Unit 1 — Family life", "h3"))
    f.append(keytable([
        ["1", "<b>B</b> breadwinner", "<i>breadwinner</i> = người kiếm tiền chính nuôi gia đình; <i>homemaker</i> là người nội trợ."],
        ["2", "<b>C</b> chores", "Cụm cố định: <i>household chores</i> = việc nhà."],
        ["3", "<b>A</b> laundry", "<i>do the laundry</i> = giặt ủi (washed and ironed clothes)."],
        ["4", "<b>D</b> responsible for", "<i>be responsible for + V-ing</i> = chịu trách nhiệm làm gì."],
        ["5", "<b>B</b> bond", "<i>strengthen the family bond</i> = thắt chặt sự gắn kết gia đình."],
        ["6", "<b>C</b> groceries", "<i>groceries</i> = đồ ăn/thực phẩm mua về (luôn số nhiều)."],
        ["7", "<b>A</b> heavy lifting", "<i>heavy lifting</i> = công việc nặng nhọc, khuân vác."],
        ["8", "<b>D</b> responsibility", "Sau <i>the value of</i> cần danh từ: <i>responsibility</i>."],
        ["9", "<b>B</b> grateful", "<i>be grateful (to sb) for sth</i> = biết ơn."],
        ["10", "<b>C</b> washing-up", "<i>do the washing-up</i> = rửa bát đĩa sau bữa ăn."],
    ]))
    f.append(P("A2. Unit 2 — Humans and the environment", "h3"))
    f.append(keytable([
        ["1", "<b>C</b> eco-friendly", "Tính từ bổ nghĩa cho <i>way</i>: <i>eco-friendly</i> = thân thiện với môi trường."],
        ["2", "<b>A</b> footprint", "Cụm cố định: <i>carbon footprint</i>."],
        ["3", "<b>D</b> pollution", "<i>Air pollution</i> = ô nhiễm không khí (sau tính từ <i>Air</i> cần danh từ ghép)."],
        ["4", "<b>B</b> set up", "<i>set up</i> = tổ chức/thiết lập (một sự kiện, câu lạc bộ)."],
        ["5", "<b>C</b> appliances", "<i>electrical appliances</i> = thiết bị điện."],
        ["6", "<b>A</b> awareness", "<i>raise someone's awareness of…</i> = nâng cao nhận thức."],
        ["7", "<b>B</b> pollute", "Cần động từ song song với <i>take</i>: <i>pollute the soil</i>."],
        ["8", "<b>D</b> recycle", "3Rs: <i>reduce – reuse – recycle</i>."],
        ["9", "<b>C</b> natural", "<i>natural resources</i> = tài nguyên thiên nhiên (tính từ + danh từ)."],
        ["10", "<b>A</b> waste", "<i>waste water</i> = lãng phí nước (hợp nghĩa cảnh báo thiếu nước)."],
    ]))
    f.append(P("A3. Unit 3 — Music", "h3"))
    f.append(keytable([
        ["1", "<b>B</b> single", "<i>a single</i> = đĩa đơn (chỉ có một bài hát); album gồm nhiều bài."],
        ["2", "<b>D</b> concert", "<i>a live concert</i> = buổi hòa nhạc trực tiếp."],
        ["3", "<b>A</b> judges", "Người cho điểm thí sinh là <i>judges</i> (giám khảo)."],
        ["4", "<b>C</b> songwriter", "<i>songwriter</i> = người sáng tác ca khúc."],
        ["5", "<b>B</b> views", "<i>get millions of views</i> = đạt hàng triệu lượt xem."],
        ["6", "<b>D</b> instruments", "<i>musical instruments</i> = nhạc cụ."],
        ["7", "<b>A</b> performance", "Sau tính từ sở hữu <i>Her</i> cần danh từ: <i>performance</i>."],
        ["8", "<b>C</b> talents", "<i>young talents</i> = những tài năng trẻ."],
        ["9", "<b>B</b> record", "<i>record a song</i> = thu âm bài hát."],
        ["10", "<b>D</b> audience", "<i>The audience</i> = khán giả (người nghe/xem biểu diễn)."],
    ]))

    f.append(P("4.2. Đáp án Bài B — Grammar & Bài C — Word form", "h2"))
    f.append(P("B1. Present simple & present continuous: <b>1C – 2A – 3D – 4B – 5C – 6A – 7B – 8D</b>", "p"))
    for t in [
        "Câu 3 là câu “2 trong 1” kinh điển: vế thói quen (<i>usually</i>) → <i>divide</i>; vế việc đang/ tạm thời hôm nay (<i>today</i>) → <i>is doing</i>.",
        "Câu 7: <i>understand</i> là động từ trạng thái → không dùng tiếp diễn dù có <i>now</i>: <i>I don't understand</i>.",
        "Câu 4: phủ định HT đơn với <i>he</i> → <i>doesn't eat</i> (động từ về nguyên thể).",
    ]: f.append(bullet(t))
    f.append(P("B2. <i>will</i> & <i>be going to</i>: <b>1B – 2C – 3A – 4D – 5B – 6C – 7A – 8D</b>", "p"))
    for t in [
        "Câu 1: người nói <i>đã quyết định</i> (I've decided) → hỏi về kế hoạch → <i>be going to</i>.",
        "Câu 2: có dấu hiệu sắp xảy ra (<i>Watch out!</i>) → <i>be going to</i>.",
        "Câu 3 & 7: quyết định/đề nghị ngay tại lúc nói → <i>will</i> (I'll clean… / I'll have…).",
        "Câu 4: dự đoán qua <i>I think</i> → <i>will</i>. Câu 5–6: kế hoạch đã chuẩn bị/đã dành đủ tiền → <i>be going to</i>.",
    ]: f.append(bullet(t))
    f.append(P("B3. Passive voice: <b>1C – 2A – 3B – 4D – 5C – 6A – 7B – 8D</b>", "p"))
    for t in [
        "Công thức duy nhất: <i>be</i> (chia theo thì + chủ ngữ mới) + V3. Câu 1 chủ ngữ số nhiều, HT đơn → <i>are thrown</i>; câu 5 quá khứ, số nhiều → <i>were planted</i>; câu 7 → <i>was written</i> (V3 của write là written).",
        "Câu 6: sau động từ khuyết thiếu <i>should</i> → <i>should be saved</i>.",
    ]: f.append(bullet(t))
    f.append(P("B4. Compound sentences: <b>1C – 2A – 3B – 4D – 5C – 6A</b> &nbsp;(so – but – or – and – so – or)", "p"))
    f.append(P("B5. To-infinitive & bare infinitive: <b>1B – 2C – 3A – 4D – 5B – 6C – 7A – 8D</b>", "p"))
    for t in [
        "<i>decide/encourage sb/promise + to V</i> (câu 1, 5, 7); <i>make/let/can + V trần</i> (câu 2, 3, 6); <i>to V</i> chỉ mục đích (câu 4); <i>It is important + to V</i> (câu 8).",
    ]: f.append(bullet(t))
    f.append(P("Bài C — Word form (đáp án):", "h3"))
    f.append(table([
        ["Câu", "Đáp án", "Vì sao?"],
        ["1", "responsibility", "Sau động từ <i>teaches</i> cần tân ngữ là danh từ (song song với <i>independence</i>)."],
        ["2", "environmental", "Bổ nghĩa cho danh từ <i>action</i> → tính từ <i>environmental</i>."],
        ["3", "pollution", "Cụm <i>Air pollution</i>; vị trí chủ ngữ cần danh từ."],
        ["4", "performance", "Sau <i>Her</i> cần danh từ: <i>performance</i> (màn biểu diễn)."],
        ["5", "musical", "Bổ nghĩa cho <i>voice</i>… chính xác hơn là tính từ chỉ tính chất âm nhạc: <i>musical</i>."],
        ["6", "grateful", "Sau <i>am very</i> cần tính từ: <i>grateful</i> (từ gốc <i>grate</i> → grateful)."],
        ["7", "awareness", "<i>raise students' awareness of…</i> — sau sở hữu cách cần danh từ."],
        ["8", "talented", "Sau mạo từ <i>a</i> + trước danh từ <i>singer</i>: cần cụm tính từ <i>talented young</i>."],
        ["9", "composition", "<i>The composition of the song</i> = việc sáng tác/tác phẩm, cần danh từ."],
        ["10", "beneficial", "Sau <i>is really</i> cần tính từ: <i>beneficial</i> (có lợi). <i>benefit</i> (n/v) không đứng ở vị trí này."],
    ], [14*mm, 32*mm, W-46*mm], align_center_cols={0}))

    # ---------- Listening ----------
    f.append(P("4.3. Listening — Đáp án & Transcript", "h2"))
    f.append(box("TRANSCRIPT D1 — Conversation: Lan & Minh (household chores)",
                 ["<b>Minh:</b> Lan, Mum says we're going to divide the housework equally between the four of us from this week.",
                  "<b>Lan:</b> Good idea. Sharing chores will make everyone less tired. So what's my part?",
                  "<b>Minh:</b> Mum will still cook because she's the best cook in the family, and Dad will do the heavy lifting and fix broken things around the house.",
                  "<b>Lan:</b> And us?",
                  "<b>Minh:</b> I'll do the washing-up after meals, and you can do the laundry at the weekend. Is that OK?",
                  "<b>Lan:</b> Sure. But tonight I have a lot of homework for the English test tomorrow.",
                  "<b>Minh:</b> Don't worry. I'll do the washing-up tonight as well, so you can study. You can help me next time.",
                  "<b>Lan:</b> Thanks, Minh. Doing things together really makes our family closer."],
                 bg=LIGHT, border=NAVY))
    f.append(P("<b>Đáp án D1:</b> 1. <b>T</b> (divide equally among four) &nbsp; 2. <b>F</b> (Mum cooks; Minh does the washing-up) &nbsp; "
               "3. <b>T</b> (do the laundry at the weekend) &nbsp; 4. <b>T</b> (heavy lifting and fixes broken things) &nbsp; "
               "5. <b>T</b> (Minh does the washing-up tonight because Lan has homework).", "p"))
    f.append(box("TRANSCRIPT D2 — Announcement: School Music Show",
                 ["Good morning, everyone. Here is an announcement about our annual School Music Show. "
                  "This year, the show will take place on <b>Friday evening</b> in the <b>school hall</b>. "
                  "There will be <b>twelve performances</b> by students from different classes, including singing, dancing and playing musical instruments. "
                  "If you want to take part in the show, please <b>sign up at the school office before Wednesday</b>. Don't be late, because only twelve students can perform. "
                  "The show has two purposes: it helps us <b>find young music talents</b>, and all the money from ticket sales will be used to <b>help poor students</b> in our school. "
                  "So don't miss it — come and enjoy the music with us on Friday evening!"],
                 bg=LIGHT, border=NAVY))
    f.append(P("<b>Đáp án D2:</b> 1. <b>B</b> (Friday evening) &nbsp; 2. <b>C</b> (school hall) &nbsp; 3. <b>A</b> (twelve) &nbsp; "
               "4. <b>D</b> (sign up at the school office before Wednesday) &nbsp; 5. <b>B</b> (tìm tài năng trẻ + gây quỹ giúp học sinh nghèo — "
               "cả hai mục đích đều được nêu rõ trong bài thông báo).", "p"))

    # ---------- Reading / Writing drills key ----------
    f.append(P("4.4. Reading & Writing (bài luyện) — Đáp án", "h2"))
    f.append(P("<b>E1 (Green Living Club leaflet): 1B – 2C – 3A – 4D – 5B.</b>", "p"))
    for t in [
        "(1) <i>was set up</i>: bị động quá khứ (“được thành lập hai năm trước”). (2) <i>clean up</i> sau <i>to</i> chỉ mục đích. "
        "(3) <i>to recycle</i>: thu gom chai/ giấy <i>để</i> tái chế. (4) <i>a great way to make friends</i>: cấu trúc <i>way + to V</i>. (5) <i>be interested in</i>.",
    ]: f.append(bullet(t))
    f.append(P("<b>E2 (Music Festival announcement): 1C – 2A – 3B – 4D – 5C.</b>", "p"))
    for t in [
        "(1) <i>take place</i> = diễn ra. (2) <i>a chance for students to perform</i>. (3) <i>was attended by…</i>: bị động quá khứ. "
        "(4) <i>and</i> nối hai thông tin bổ sung. (5) <i>Don't forget to invite…</i>: <i>forget + to V</i> = quên (chưa làm).",
    ]: f.append(bullet(t))
    f.append(P("<b>F1 (Sharing household chores): 1B – 2C – 3A – 4D – 5B.</b>", "p"))
    for t in [
        "Câu 5: <i>older ones</i> thay cho <i>older children</i> (so với <i>young children</i> ở vế trước). Câu 4: bài không hề nói việc nhà giúp điểm cao ở trường → chọn D ở câu NOT.",
    ]: f.append(bullet(t))
    f.append(P("<b>F2 (Small actions for a greener life): 1C – 2A – 3B – 4D – 5C.</b>", "p"))
    for t in [
        "Câu 3: <i>they</i> trong “when they are not in use” thay cho <i>the lights and electrical appliances</i>. Câu 4: phương án D đúng nguyên văn đoạn 3 (<i>reduces our carbon footprint</i>).",
    ]: f.append(bullet(t))
    f.append(P("<b>G. Re-ordering: 1B – 2C – 3A – 4D – 5B – 6C.</b>", "p"))
    for t in [
        "Câu 2 & 5 (đoạn văn): luôn bắt đầu bằng câu chủ đề (d), sau đó <i>Firstly (c) → Secondly (a) → In short/To sum up (b)</i>.",
        "Câu 4 (lá thư): <i>Dear… (b)</i> mở đầu → lí do viết (a) → nội dung (d) → hy vọng/kết (c).",
    ]: f.append(bullet(t))
    f.append(P("<b>H. Sentence transformation — đáp án gợi ý:</b>", "p"))
    ans = [
        "English <b>is spoken all over the world</b>.",
        "The school yard <b>was cleaned up by the students yesterday</b>.",
        "A music festival <b>will be held at our school next month</b>.",
        "We are going <b>to plant more trees around our school</b>.",
        "He was very tired, <b>but he still finished the performance</b>.",
        "Because <b>it rained heavily, we cancelled the outdoor concert</b>.",
        "I was <b>made to do the laundry before going out (by Mum)</b>. (Lưu ý: bị động của <i>make</i> phải có <i>to</i>.)",
        "She saves money every month to <b>buy a new guitar</b>.",
        "Dad promised <b>to help Mum with the housework</b>.",
        "If you <b>drop litter, the park will be dirty</b>.",
        "It is <b>a simple way to save energy to turn off the lights</b> / tự nhiên hơn: <i>It is simple to turn off the lights to save energy</i> — chấp nhận cả hai nếu đúng cấu trúc <i>It is + adj + to V</i>.",
        "Plastic bottles <b>should be recycled</b>.",
    ]
    for i, a in enumerate(ans, 1):
        f.append(bullet(f"<b>{i}.</b> {a}"))
    return f
