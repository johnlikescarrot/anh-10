# -*- coding: utf-8 -*-
"""Phần I - Chương 2: 5 chủ điểm ngữ pháp."""
from common import *

def build():
    f = []
    f.append(P("CHƯƠNG 2: NĂM CHỦ ĐIỂM NGỮ PHÁP TRỌNG TÂM", "h1"))
    f.append(P("Cả 5 chủ điểm dưới đây đều nằm trong Bảng đặc tả. Với mỗi chủ điểm, hãy học theo trình tự: "
               "<b>công thức → cách dùng → dấu hiệu nhận biết → bẫy</b>. Cuối chương có bảng tổng hợp “một trang” để ôn nhanh trước khi thi."))
    f.append(table([
        ["#", "Chủ điểm", "Thuộc Unit", "Câu cửa miệng để nhớ"],
        ["1", "Present simple & Present continuous", "Unit 1", "“Thói quen dùng <i>simple</i>, đang diễn ra dùng <i>continuous</i>”"],
        ["2", "<i>will</i> & <i>be going to</i> (tương lai)", "Unit 2", "“<i>will</i> = quyết tại chỗ, <i>going to</i> = đã có kế hoạch/căn cứ”"],
        ["3", "Passive voice (câu bị động)", "Unit 2", "“<i>be + V3</i>, tân ngữ lên làm chủ”"],
        ["4", "Compound sentences (câu ghép)", "Unit 3", "“Hai câu đơn, một liên từ: <i>and–but–or–so</i>”"],
        ["5", "To-infinitive & Bare infinitive", "Unit 3", "“<i>make/let + V</i> trần, <i>want/decide + to V</i>”"],
    ], [10*mm, 62*mm, 24*mm, W-96*mm], align_center_cols={0,2}))

    # ---- G1 ----
    f.append(P("2.1. Present simple & Present continuous (Thì hiện tại đơn & hiện tại tiếp diễn) — Unit 1", "h2"))
    f.append(table([
        ["", "Present simple", "Present continuous"],
        ["<b>Công thức</b>", "S + V(s/es)<br/>(-) S + don't/doesn't + V<br/>(?) Do/Does + S + V?", "S + am/is/are + V-ing<br/>(-) S + am/is/are + not + V-ing<br/>(?) Am/Is/Are + S + V-ing?"],
        ["<b>Cách dùng chính</b>", "• Thói quen, việc lặp đi lặp lại<br/>• Sự thật hiển nhiên, chân lý<br/>• Lịch trình cố định (tàu, phim…)<br/>• Trạng thái lâu dài (nghề nghiệp, nơi ở)", "• Hành động đang xảy ra lúc nói<br/>• Hành động quanh thời điểm hiện tại (dự án đang làm)<br/>• Tình huống tạm thời<br/>• Kế hoạch tương lai đã sắp xếp (có thời gian/nơi chốn cụ thể)"],
        ["<b>Dấu hiệu</b>", "always, usually, often, sometimes, rarely, seldom, never, every day/week…, on Mondays", "now, right now, at the moment, at present, today, this week; Look!, Listen!, Be careful!"],
        ["<b>Ví dụ</b>", "My mother <b>wakes up</b> at 5 a.m. every day.<br/>The sun <b>rises</b> in the east.", "Look! Dad <b>is doing</b> the heavy lifting.<br/>I <b>am studying</b> English this semester."],
    ], [26*mm, 62*mm, W-88*mm]))
    f.append(box("BẪY THƯỜNG GẶP — G1",
                 ["<b>Động từ trạng thái (state verbs)</b> — <i>know, believe, like, love, hate, want, need, understand, remember, belong, seem</i> — "
                  "hầu như <b>không</b> dùng ở thì tiếp diễn: <i>I <b>want</b> some water</i> (không phải <i>am wanting</i>).",
                  "Chủ ngữ số ít (he/she/it) ở hiện tại đơn phải thêm <b>-s/-es</b>: <i>She wash<b>es</b> the dishes</i>; phủ định dùng <i>doesn't + V nguyên thể</i> (bỏ -s ở động từ chính): <i>She doesn't wash…</i>",
                  "Cách viết V-ing: bỏ <i>e</i> câm (<i>make → making</i>), gấp đôi phụ âm cuối (<i>run → running, shop → shopping</i>), <i>ie → y</i> (<i>lie → lying</i>)."],
                 bg=LIGHT2, border=ORANGE))
    f.append(P("<b>Mẹo nhớ:</b> Thấy <i>every…, always, usually</i> → nghĩ “đồng hồ lặp lại” → <b>simple</b>. Thấy <i>now, Look!, Listen!</i> → nghĩ “máy quay đang quay” → <b>continuous</b>. "
               "Khi hai thì cùng xuất hiện trong một đoạn, thói quen nền dùng simple, hành động đang xen vào dùng continuous.", "p"))

    # ---- G2 ----
    f.append(P("2.2. Future with <i>will</i> & <i>be going to</i> (Tương lai với will và be going to) — Unit 2", "h2"))
    f.append(table([
        ["", "<i>will</i> + V", "<i>be going to</i> + V"],
        ["<b>Khi nào dùng</b>", "• Quyết định <b>ngay lúc nói</b> (không suy nghĩ trước)<br/>• Lời hứa, đề nghị giúp đỡ, yêu cầu<br/>• Dự đoán dựa trên ý kiến (<i>I think, I'm sure, probably, hope</i>)<br/>• Sự thật về tương lai, cảnh báo", "• Kế hoạch/dự định <b>đã quyết định từ trước</b><br/>• Dự đoán dựa trên <b>dấu hiệu nhìn thấy ngay lúc nói</b><br/>• Việc sắp xảy ra trong tương lai gần"],
        ["<b>Ví dụ</b>", "— The bag is heavy. — I<b>'ll carry</b> it for you. (quyết tại chỗ)<br/>I think our team <b>will win</b>. (ý kiến)", "We<b>'re going to clean up</b> the beach this Sunday. (kế hoạch)<br/>Look at the clouds! It<b>'s going to rain</b>. (dấu hiệu)"],
        ["<b>Phủ định / Câu hỏi</b>", "won't + V; Will you …?", "am/is/are + not going to + V"],
    ], [26*mm, 62*mm, W-88*mm]))
    f.append(box("BẪY THƯỜNG GẶP — G2",
                 ["Có <i>I think / I'm sure / probably / I hope</i> → ưu tiên <b>will</b>. Có bằng chứng trước mắt (<i>Look! Watch out!</i>) → <b>be going to</b>.",
                  "Câu đề nghị giúp đỡ tự phát luôn dùng <b>will</b>: <i>I'll help you with the cleaning.</i>",
                  "Đừng viết <i>will to V</i> hay <i>going to will V</i>. Sau <i>will</i> và sau <i>be going to</i> đều là <b>V nguyên thể</b>.",
                  "Hiện tại tiếp diễn cũng nói về kế hoạch tương lai đã sắp xếp cụ thể (có giờ giấc): <i>We are having a music show tonight.</i> — gặp dạng này, đừng vội cho là sai."],
                 bg=LIGHT2, border=ORANGE))
    f.append(P("<b>Mẹo nhớ:</b> “<i>will</i> — quyết trong 1 giây; <i>going to</i> — đã ghi vào lịch”. Nghe câu “<i>Watch out! You ___ drop the vase!</i>” — có dấu hiệu sắp xảy ra → <i>are going to</i>.", "p"))

    # ---- G3 ----
    f.append(P("2.3. Passive voice (Câu bị động) — Unit 2", "h2"))
    f.append(P("Dùng câu bị động khi <b>hành động quan trọng hơn người thực hiện</b>, không biết/không cần nêu người thực hiện, hoặc trong văn bản khoa học, thông báo, tin tức (rất hợp chủ đề môi trường). "
               "Công thức “xương sống” duy nhất: <b><i>be</i> + V3 (past participle)</b> — thì của câu nằm ở động từ <i>be</i>.", "p"))
    f.append(table([
        ["Thì", "Chủ động", "Bị động: be + V3", "Ví dụ"],
        ["Hiện tại đơn", "S + V(s/es) + O", "am/is/are + V3", "Plastic bags <b>are used</b> everywhere."],
        ["Quá khứ đơn", "S + V2/ed + O", "was/were + V3", "The park <b>was cleaned up</b> yesterday."],
        ["Tương lai đơn", "S + will + V + O", "will be + V3", "A green festival <b>will be held</b> next week."],
        ["Động từ khuyết thiếu", "S + can/must/should + V + O", "can/must/should be + V3", "Electricity <b>should be saved</b>."],
    ], [28*mm, 42*mm, 42*mm, W-112*mm]))
    f.append(P("<b>4 bước chuyển đổi chủ động → bị động:</b> (1) Tân ngữ (O) lên làm chủ ngữ; (2) xác định thì của động từ gốc, chia <i>be</i> theo thì đó và theo chủ ngữ mới; "
               "(3) động từ chính chuyển thành V3; (4) chủ ngữ cũ (nếu cần nêu) đặt sau <i>by</i>: <i>by me/him/her/us/them</i>, danh từ riêng giữ nguyên. "
               "Bỏ <i>by…</i> khi chủ ngữ là <i>people, someone, they</i> chung chung.", "p"))
    f.append(box("BẪY THƯỜNG GẶP — G3",
                 ["Quên chia <i>be</i> theo <b>chủ ngữ mới</b>: <i>The trees <b>were</b> planted</i> (số nhiều → were).",
                  "Nhầm V2 với V3: <i>write – wrote – <b>written</b>; take – took – <b>taken</b>; hold – held – <b>held</b>; build – built – <b>built</b></i>. Hãy học thuộc bảng V3 ở Phụ lục.",
                  "Nội động từ (<i>happen, arrive, sleep</i>…) không có câu bị động vì không có tân ngữ.",
                  "Trong Writing 2, câu gốc cho thì nào thì câu bị động giữ nguyên thì đó."],
                 bg=LIGHT2, border=ORANGE))

    # ---- G4 ----
    f.append(P("2.4. Compound sentences (Câu ghép) — Unit 3", "h2"))
    f.append(P("Câu ghép gồm <b>hai mệnh đề độc lập</b> (mỗi mệnh đề tự đứng được thành câu) nối bằng liên từ đẳng lập. "
               "SGK <i>Global Success 10</i> tập trung vào 4 liên từ: <b>and, but, or, so</b> (và thường có <b>dấu phẩy trước liên từ</b>).", "p"))
    f.append(table([
        ["Liên từ", "Quan hệ nghĩa", "Ví dụ", "Mẹo nhớ"],
        ["<b>and</b>", "bổ sung, thêm ý (và)", "She sings well, <b>and</b> she plays the piano.", "AND = cộng thêm (+)"],
        ["<b>but</b>", "đối lập, trái ngược (nhưng)", "He practised a lot, <b>but</b> he didn't win.", "BUT = rẽ ngược (−)"],
        ["<b>or</b>", "lựa chọn (hoặc; nếu không thì…)", "Hurry up, <b>or</b> you will miss the concert.", "OR = chọn 1 trong 2"],
        ["<b>so</b>", "kết quả (vì vậy, nên)", "The tickets were cheap, <b>so</b> we bought four.", "SO = mũi tên kết quả (→)"],
    ], [22*mm, 44*mm, 62*mm, W-128*mm]))
    f.append(box("BẪY THƯỜNG GẶP — G4",
                 ["Phân biệt <b>so</b> (kết quả: nguyên nhân → kết quả) với <b>because</b> (nguyên nhân, mệnh đề phụ thuộc — không phải câu ghép): <i>It rained, <b>so</b> we stayed home = We stayed home <b>because</b> it rained.</i> Viết lại câu rất hay đổi qua lại hai cấu trúc này.",
                  "Sau <i>or</i> trong câu ghép mang nghĩa cảnh báo: <i>Do it now, or…</i> = <i>If you don't do it now, …</i>",
                  "Không nối hai mệnh đề độc lập chỉ bằng dấu phẩy mà thiếu liên từ (lỗi <i>comma splice</i> trong bài viết)."],
                 bg=LIGHT2, border=ORANGE))

    # ---- G5 ----
    f.append(P("2.5. To-infinitive & Bare infinitive (Động từ nguyên mẫu có to và không to) — Unit 3", "h2"))
    f.append(table([
        ["Dạng", "Dùng sau các động từ / cấu trúc", "Ví dụ"],
        ["<b>to-infinitive</b> (to V)", "<b>decide, plan, want, hope, promise, agree, learn, afford, manage, tend, offer, prepare, expect</b> + to V<br/><i>It + be + adj + to V</i> (It is important to…)<br/><b>to V chỉ mục đích</b> (= in order to): làm gì <i>để…</i><br/>S + V + <b>O + to V</b>: <i>allow, encourage, invite, remind, advise, teach, want</i> + O + to V", "She <b>decided to join</b> the music club.<br/>We learn English <b>to get</b> better jobs.<br/>Our teacher <b>encouraged us to perform</b> on stage."],
        ["<b>bare infinitive</b> (V trần)", "<b>make / let</b> + O + V (khiến/để cho ai làm gì)<br/><b>help</b> + O + V (hoặc to V đều được)<br/>Động từ khuyết thiếu: <i>can, must, should, will…</i> + V<br/><i>would rather / had better</i> + V<br/>Cấu trúc cảm giác: <i>see/hear/watch + O + V</i>", "Mum <b>made me do</b> the washing-up.<br/>Please <b>let me help</b> you.<br/>Music <b>can help</b> people relax.<br/>I saw him <b>play</b> the trumpet."],
    ], [34*mm, 68*mm, W-102*mm]))
    f.append(box("BẪY THƯỜNG GẶP — G5",
                 ["<b>make/let + O + V trần</b>, nhưng khi chuyển sang bị động của <i>make</i> phải có <i>to</i>: <i>He was <b>made to</b> clean the room.</i>",
                  "<i>help</i> là động từ “dễ tính”: <i>help me (to) carry</i> — cả hai đều đúng.",
                  "Sau giới từ dùng <b>V-ing</b>, không dùng to V: <i>be good at <b>playing</b>, interested in <b>learning</b>, without <b>saying</b></i>.",
                  "Phân biệt <i>stop to V</i> (dừng lại để làm việc khác) với <i>stop V-ing</i> (ngừng hẳn việc đang làm) — mức Hiểu hay hỏi."],
                 bg=LIGHT2, border=ORANGE))
    f.append(P("<b>Mẹo nhớ:</b> Nhóm “<i>to V</i>” là các động từ hướng về tương lai/dự định (muốn, hứa, quyết định, hy vọng… việc chưa xảy ra nên “vươn tới” bằng <i>to</i>). "
               "Nhóm “V trần” đứng sau <i>make/let</i> và động từ khuyết thiếu — cứ nhớ khẩu quyết: <b>“Make–let–modal: động từ trần; want–decide–promise: phải có to.”</b>", "p"))

    # ---- One-page summary ----
    f.append(P("2.6. BẢNG TỔNG HỢP NGỮ PHÁP — 1 TRANG (in ra dán bàn học)", "h2"))
    f.append(table([
        ["Chủ điểm", "Công thức cốt lõi", "Dấu hiệu / Từ khóa", "1 ví dụ “đinh”"],
        ["HT đơn / HT tiếp diễn", "V(s/es) ↔ am/is/are + V-ing", "every, usually ↔ now, Look!, Listen!", "She <b>cooks</b> daily. Look! She <b>is cooking</b>."],
        ["will / be going to", "will + V ↔ am/is/are going to + V", "I think, I'll (tại chỗ) ↔ plan, Look at…!", "I<b>'ll help</b> you. It<b>'s going to rain</b>."],
        ["Câu bị động", "be (chia theo thì) + V3 (+ by…)", "by, are used, was built, will be held", "The beach <b>was cleaned up</b> yesterday."],
        ["Câu ghép", "Mệnh đề, + and/but/or/so + mệnh đề", "cộng / ngược / chọn / kết quả", "It was late, <b>so</b> we went home."],
        ["to-inf / bare inf", "want/decide… + to V; make/let/can… + V", "mục đích: to = để", "Let me <b>help</b>; I want <b>to help</b>."],
    ], [34*mm, 46*mm, 46*mm, W-126*mm]))
    return f
