# -*- coding: utf-8 -*-
"""Phần IV (2/2): Đáp án đề thi thử + bài mẫu + Phụ lục."""
from common import *

def build():
    f = []
    f.append(P("4.5. Đề thi thử số 1 — Đáp án, transcript & bài mẫu", "h2"))

    f.append(box("TRANSCRIPT — Đề thi thử, Listening Part 1 (Hoa & her father)",
                 ["<b>Father:</b> Hoa, remember that our family cleans the house together every Saturday morning. Tomorrow is Saturday, so let's prepare.",
                  "<b>Hoa:</b> Yes, Dad. Are you going to do all the heavy work again?",
                  "<b>Father:</b> No. This time we'll divide the work. I'll clean the garden and do the heavy lifting because those jobs need strength.",
                  "<b>Hoa:</b> What about me, Dad?",
                  "<b>Father:</b> You'll clean the bathroom and the living room. Your mother will do the laundry and prepare lunch for us.",
                  "<b>Hoa:</b> And my little brother? He's only seven.",
                  "<b>Father:</b> He can put his toys away and feed the cat. Small jobs are good for him.",
                  "<b>Hoa:</b> Great. When we share the work, everything will be done quickly and we'll have time to rest together."],
                 bg=LIGHT, border=NAVY))
    f.append(P("<b>Đáp án Listening Part 1:</b> 1. <b>T</b> &nbsp; 2. <b>F</b> (cả nhà chia nhau; bố chỉ làm việc nặng) &nbsp; "
               "3. <b>F</b> (Hoa lau phòng tắm & phòng khách; giặt đồ là việc của mẹ — bẫy “gộp hai việc của hai người”) &nbsp; "
               "4. <b>T</b> &nbsp; 5. <b>F</b> (mẹ nấu bữa trưa).", "p"))

    f.append(box("TRANSCRIPT — Đề thi thử, Listening Part 2 (Green Festival announcement)",
                 ["Attention, please! Our school's Green Festival will be held <b>next Sunday morning</b>. "
                  "All the main activities will take place in the <b>school yard</b>, so remember to bring a hat. "
                  "At the festival, students can bring old paper and plastic bottles to <b>exchange for small green plants</b> to grow at home. "
                  "There will also be games, a fashion show with recycled clothes, and an interesting talk about saving energy. "
                  "Guess who will give the talk? A <b>famous singer</b> who is well known for his green lifestyle will come to share his ideas with us. "
                  "We hope the festival will <b>raise students' awareness of protecting the environment</b> and encourage everyone to live green every day. See you there!"],
                 bg=LIGHT, border=NAVY))
    f.append(P("<b>Đáp án Listening Part 2:</b> 6. <b>B</b> (next Sunday morning) &nbsp; 7. <b>C</b> (school yard) &nbsp; "
               "8. <b>D</b> (old paper and bottles → green plants) &nbsp; 9. <b>A</b> (a famous singer) &nbsp; 10. <b>B</b> (raise awareness of protecting the environment).", "p"))

    f.append(P("<b>Language:</b> 11. <b>A</b> (breadwinner — mức Biết) &nbsp; 12. <b>C</b> (eco-friendly — mức Hiểu: phân biệt tính từ hợp ngữ cảnh) &nbsp; "
               "13. <b>B</b> (<i>does</i> thói quen + <i>is washing</i> hành động hiện tại) &nbsp; 14. <b>C</b> (dấu hiệu mây đen → <i>is going to</i>) &nbsp; "
               "15. <b>D</b> (<i>were planted</i> — bị động quá khứ, chủ ngữ số nhiều) &nbsp; 16. <b>A</b> (<i>decided to organise</i>).<br/>"
               "<b>Câu 17:</b> <i>responsible</i> (sau <i>should be</i> cần tính từ). &nbsp; <b>Câu 18:</b> <i>performance</i> (sau <i>Her beautiful</i> cần danh từ).", "p"))
    f.append(P("<b>Reading:</b> 19. <b>C</b> (musical instrument) &nbsp; 20. <b>B</b> (<i>will be held</i> — bị động tương lai) &nbsp; "
               "21. <b>A</b> (<i>a chance for you to show</i>) &nbsp; 22. <b>D</b> (<i>so</i> — quan hệ kết quả) &nbsp; 23. <b>C</b> (<i>before Wednesday</i>) &nbsp; "
               "24. <b>B</b> (ý chính bao quát cả lợi ích lẫn lưu ý ở đoạn cuối) &nbsp; 25. <b>C</b> (<i>gives us energy when we exercise</i>) &nbsp; "
               "26. <b>A</b> (<i>it</i> = music) &nbsp; 27. <b>D</b> (bài không nói âm nhạc giúp điểm cao mọi môn) &nbsp; 28. <b>B</b> (nghe nhạc quá to lâu ngày hại tai).", "p"))
    f.append(P("<b>Writing 1:</b> 29. <b>A</b> (c – a – d – b: câu chủ đề → Firstly → Secondly → To sum up) &nbsp; "
               "30. <b>B</b> (b – d – a – c: hỏi → trả lời → hỏi tiếp → trả lời).", "p"))
    f.append(P("<b>Writing 2 — đáp án:</b>", "p"))
    for i, a in enumerate([
        "Hundreds of trees <b>were planted around the school (by students) last year</b>.",
        "Minh has decided <b>to take part in the clean-up campaign this Sunday</b>.",
        "Because <b>the show was very interesting, a lot of students stayed until the end</b>.",
        "We <b>were allowed to sing our favourite songs at the party (by our teacher)</b>.",
    ], 31):
        f.append(bullet(f"<b>{i}.</b> {a}"))

    f.append(P("Bài mẫu cho Writing 3 (Câu 35) — chủ đề: bảo vệ môi trường ở trường học (126 từ, đúng khoảng 120–150 từ)", "h3"))
    f.append(box("BÀI MẪU 1 — What students can do to protect the environment at school",
                 ["There are many simple things that students can do to protect the environment at school. "
                  "Firstly, we should follow the 3Rs: reduce, reuse and recycle. For example, we can use refillable water bottles, "
                  "write on both sides of paper, and put plastic bottles in the recycling bins. "
                  "Secondly, saving electricity and water is also very important. Lights and fans should be turned off when classrooms are empty, "
                  "and taps must not be left running. In addition, students can plant trees and flowers to make the school greener and cleaner. "
                  "These small actions should be shared with our friends to raise their awareness of green living. "
                  "In short, if every student changes a few small habits, our school will become a cleaner and healthier place for everyone."],
                 bg=LIGHT3, border=GREEN))
    f.append(P("<i>Phân tích nhanh:</i> đoạn văn có đủ Topic sentence → <i>Firstly</i> → <i>Secondly</i> → <i>In addition</i> → <i>In short</i>; "
               "có câu bị động (<i>should be turned off</i>), câu ghép và từ vựng chủ đề (<i>3Rs, recycling bins, raise awareness</i>) — đúng các yếu tố được cộng điểm.", "p"))

    f.append(P("Hai bài mẫu bổ trợ (học thuộc khung để dùng cho mọi đề Writing 3 thuộc 3 chủ đề)", "h3"))
    f.append(box("BÀI MẪU 2 — Benefits of sharing household chores (Family life)",
                 ["Sharing household chores brings many benefits to my family. "
                  "Firstly, when everyone helps with the housework, no one feels too tired. My father works all day, so my brother and I do the washing-up and clean the house to help him rest. "
                  "Secondly, doing chores together strengthens our family bond. While cooking dinner, we often talk about our day and understand each other better. "
                  "Moreover, sharing chores teaches children responsibility and useful life skills such as cooking and doing the laundry. "
                  "These skills will help us a lot when we grow up and live independently. In my family, housework is divided equally among all members, so everyone feels respected, cared for and loved. "
                  "In short, sharing housework not only keeps our home clean and tidy but also makes our family happier and closer together."],
                 bg=LIGHT3, border=GREEN))
    f.append(box("BÀI MẪU 3 — Benefits of music in our life (Music)",
                 ["Music plays an important part in our daily life. "
                  "Firstly, music helps us relax and reduce stress. After a long day at school, listening to my favourite songs makes me feel calm and happy again. "
                  "Secondly, music connects people together. At concerts, thousands of fans can sing along and share the same feelings, even when they do not know each other. "
                  "Playing a musical instrument also builds young people's confidence and patience, because performers have to practise hard before going on stage. "
                  "In addition, music is a good way to learn about other cultures through their traditional songs. "
                  "For me, music is not only a relaxing hobby but also a close friend that stays with me in my daily life. In short, music makes our life richer, happier and more colourful, so we should all spend time enjoying it every day."],
                 bg=LIGHT3, border=GREEN))
    f.append(P("<b>Cách dùng bài mẫu:</b> gạch chân các câu khung (câu mở, từ nối, câu kết) và học thuộc chúng; khi vào thi, giữ nguyên khung, chỉ thay ví dụ và từ vựng cho khớp đề bài. "
               "Tuyệt đối không sao chép nguyên văn một cách máy móc nếu đề hỏi khác chủ đề.", "p"))

    # ---------------- PHỤ LỤC ----------------
    f.append(band("PHỤ LỤC", NAVY))
    f.append(spacer(6))
    f.append(P("Phụ lục 1. Bảng động từ bất quy tắc hay dùng ở dạng V3 (cho câu bị động)", "h2"))
    f.append(table([
        ["V1", "V2", "V3", "Nghĩa", "V1", "V2", "V3", "Nghĩa"],
        ["write", "wrote", "written", "viết", "take", "took", "taken", "lấy, mang"],
        ["speak", "spoke", "spoken", "nói", "hold", "held", "held", "tổ chức"],
        ["build", "built", "built", "xây dựng", "make", "made", "made", "làm, chế tạo"],
        ["plant", "planted", "planted", "trồng", "clean", "cleaned", "cleaned", "dọn dẹp"],
        ["throw", "threw", "thrown", "ném, vứt", "give", "gave", "given", "đưa, tặng"],
        ["choose", "chose", "chosen", "chọn", "sing", "sang", "sung", "hát"],
        ["bring", "brought", "brought", "mang đến", "teach", "taught", "taught", "dạy"],
        ["grow", "grew", "grown", "trồng, lớn lên", "use", "used", "used", "sử dụng"],
    ], [20*mm, 20*mm, 20*mm, 28*mm, 20*mm, 20*mm, 20*mm, W-148*mm]))
    f.append(P("Phụ lục 2. Checklist 15 phút trước khi vào phòng thi", "h2"))
    for t in [
        "Tôi thuộc 60 từ vựng cốt lõi của Units 1–3 và các cụm <i>collocation</i> đi kèm.",
        "Tôi phân biệt được: HT đơn/HT tiếp diễn; <i>will/be going to</i>; chủ động/bị động; <i>to V/V trần</i>; 4 liên từ câu ghép.",
        "Tôi nhớ công thức bị động: <i>be</i> (theo thì) + V3, và bảng V3 bất quy tắc ở trên.",
        "Tôi đã thuộc khung đoạn văn (Firstly – Secondly – In addition – In short) và 10 câu khung của 3 bài mẫu.",
        "Nghe: đọc câu hỏi trước, gạch từ khóa, không dừng lại ở câu khó. Đọc: tìm ý chính trước, chi tiết sau.",
        "Không bỏ trống bất kỳ câu nào; luôn chừa 2 phút cuối để rà soát -s/es, be + V3 và chính tả.",
    ]:
        f.append(bullet("☐ " + t))
    f.append(P("Phụ lục 3. Nhật ký lỗi sai (ghi lại sau mỗi bài luyện — đây là trang “đắt giá” nhất của tài liệu)", "h2"))
    rows = [["Ngày", "Bài/Câu", "Lỗi của tôi", "Dạng kiến thức", "Cách sửa đúng"]]
    for _ in range(8):
        rows.append(["", "", "", "", ""])
    t = table(rows, [20*mm, 22*mm, 44*mm, 34*mm, W-120*mm])
    f.append(t)
    f.append(P("Phụ lục 4. Bảng theo dõi tiến bộ", "h2"))
    f.append(table([
        ["Lần làm", "Listening /2,5", "Language /2,5", "Reading /2,5", "Writing /2,5", "Tổng /10", "Điểm cần cải thiện nhất"],
        ["Bài luyện Phần II", "", "", "", "", "", ""],
        ["Đề thi thử số 1", "", "", "", "", "", ""],
        ["Làm lại đề thử (sau 3 ngày)", "", "", "", "", "", ""],
    ], [34*mm, 24*mm, 24*mm, 24*mm, 24*mm, 20*mm, W-150*mm]))
    f.append(spacer(6))
    f.append(box("LỜI KẾT",
                 ["Đề thi giữa kỳ 1 Tiếng Anh 10 năm học 2026–2027 không đánh đố: 70% là trắc nghiệm nhận biết – hiểu thuộc đúng Units 1–3, "
                  "30% vận dụng nằm ở phần viết có khung sẵn. Nếu em ôn đúng theo ma trận này — thuộc từ theo cụm, nắm chắc 5 chủ điểm ngữ pháp, "
                  "luyện đủ các dạng bài và không bao giờ bỏ trống phần tự luận — thì mục tiêu điểm số hoàn toàn nằm trong tầm tay. <b>Chúc em thi tốt!</b>"],
                 bg=LIGHT2, border=ORANGE))
    return f
