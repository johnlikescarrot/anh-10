# -*- coding: utf-8 -*-
"""PART D - answer keys, explanations, transcripts, model answers."""


def build(D):
    D.pagebreak()
    D.h1("PHẦN D. ĐÁP ÁN VÀ GIẢI THÍCH CHI TIẾT", part=True)

    D.h2("D1. Bảng đáp án nhanh (trắc nghiệm, mỗi câu 0,25 điểm)")
    D.table(
        ["Câu", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14"],
        [["Đáp án", "F", "T", "T", "F", "T", "B", "C", "C", "B", "D", "B", "A", "B", "B"]],
        [16] + [11] * 14, align_center_cols=tuple(range(1, 15)))
    D.table(
        ["Câu", "15", "16", "17", "18", "19", "20", "21", "22", "23", "24", "25", "26", "27", "28"],
        [["Đáp án", "B", "C", "C", "A", "A", "A", "A", "B", "C", "B", "D", "C", "A", "A"]],
        [16] + [11] * 14, align_center_cols=tuple(range(1, 15)))

    D.h2("D2. Giải thích chi tiết từng câu")

    D.h3("Part I - Listening 1 (True/False)")
    D.table(
        ["Câu", "Đáp án", "Giải thích"],
        [
            ["1", "**F**", "Bài nghe nói gia đình Linh có **bốn** người: 'There are four people in my family: my parents, my younger brother and me.'"],
            ["2", "**T**", "'He does the heavy lifting, repairs things around the house, and **cooks dinner at weekends**.'"],
            ["3", "**T**", "'...during the week she only prepares breakfast and **does the shopping online**.'"],
            ["4", "**F**", "Nam đổ rác và cho chó ăn **mỗi buổi tối** (every evening), không phải buổi sáng (every morning)."],
            ["5", "**T**", "Ý chính cuối bài: 'Sharing housework has **brought us closer**.' - chia sẻ việc nhà giúp các thành viên gắn bó hơn."],
        ],
        [10, 16, 144], align_center_cols=(0, 1))

    D.h3("Part II - Listening 2 (A-D)")
    D.table(
        ["Câu", "Đáp án", "Giải thích"],
        [
            ["6", "**B**", "Nam nói: 'My school's music club is giving a **concert** at the Youth Centre. Would you like to come?'"],
            ["7", "**C**", "Concert có pop, dance music và folk songs - **không có rock**."],
            ["8", "**C**", "Nam nói: '**My sister** is playing the piano in two performances.'"],
            ["9", "**B**", "Vé 50.000đ, học sinh được giảm nửa giá (half price) → Mai (học sinh) trả **25.000đ**."],
            ["10", "**D**", "Nam dặn: 'Just bring **your student card** for the discount.'"],
        ],
        [10, 16, 144], align_center_cols=(0, 1))

    D.h3("Part III & IV - Language")
    D.table(
        ["Câu", "Đáp án", "Giải thích"],
        [
            ["11", "**B**", "nuclear family = gia đình hạt nhân (chỉ gồm bố mẹ và con cái); extended family là gia đình đa thế hệ."],
            ["12", "**A**", "be keen on sth = rất yêu thích cái gì; phù hợp ngữ cảnh 'follow their favourite singers everywhere'."],
            ["13", "**B**", "'Look!' → dấu hiệu hiện tại tiếp diễn: are playing."],
            ["14", "**B**", "Câu bị động hiện tại đơn với 'Nowadays': songs (số nhiều) → **are recorded**."],
            ["15", "**B**", "Dự đoán **có bằng chứng trước mắt** ('dark clouds') → dùng **be going to**."],
            ["16", "**C**", "Hai vế tương phản (muốn đi xem nhưng phải ở nhà) → liên từ **but**."],
        ],
        [10, 16, 144], align_center_cols=(0, 1))

    D.h3("Part V - Cloze test")
    D.table(
        ["Câu", "Đáp án", "Giải thích"],
        [
            ["17", "**C**", "Cấu trúc **be interested in** (quan tâm/hứng thú với). 'Interesting' là tính từ chủ động, không đi với 'Are you...' ở đây."],
            ["18", "**A**", "pick up rubbish = nhặt rác (đúng ngữ cảnh dọn vệ sinh); throw away = vứt đi (sai nghĩa)."],
            ["19", "**A**", "**more than** one tonne = hơn một tấn (thành tích của CLB); 'less/fewer' sai nghĩa, 'many' không đi với 'one tonne'."],
            ["20", "**A**", "Từ tham chiếu thay cho **waste** (danh từ không đếm được, số ít) → dùng **it**."],
            ["21", "**A**", "Collocation: **fill in / fill out the form** = điền vào đơn."],
        ],
        [10, 16, 144], align_center_cols=(0, 1))

    D.h3("Part VI - Reading 2")
    D.table(
        ["Câu", "Đáp án", "Giải thích"],
        [
            ["22", "**B**", "Ý chính toàn bài: thói quen nghe nhạc, gu âm nhạc và tác động (tích cực lẫn tiêu cực) của âm nhạc với thanh thiếu niên."],
            ["23", "**C**", "Đoạn 1: 'more than 80% of students between 13 and 18 listen to music for at least one hour every day.'"],
            ["24", "**B**", "'it' thay cho **traditional folk music** ở ngay trước: '...is the least popular choice..., although **it** is part of a nation's culture.'"],
            ["25", "**D**", "Bài đọc nêu lợi ích: bình tĩnh trước kì thi, tính kiên nhẫn - kỉ luật, kết bạn; **không** nói âm nhạc giúp kiếm tiền."],
            ["26", "**C**", "Đoạn cuối: 'Experts suggest that young people should **keep the volume at a safe level and take a break** after every hour of listening.'"],
        ],
        [10, 16, 144], align_center_cols=(0, 1))

    D.h3("Part VII - Re-ordering")
    D.table(
        ["Câu", "Đáp án", "Giải thích"],
        [
            ["27", "**A** (a-b-c-d-e)", "Trật tự hội thoại: hỏi thăm kế hoạch (a) → trả lời (b) → lời mời (c) → đồng ý, hỏi địa điểm (d) → hẹn giờ, địa điểm (e)."],
            ["28", "**A** (c-a-d-e-b)", "Câu chủ đề (c) → First (a) → Second (d) → Finally (e) → In conclusion (b)."],
        ],
        [10, 16, 144], align_center_cols=(0, 1))

    # ---------------- written answers
    D.h2("D3. Đáp án phần tự luận")

    D.h3("Câu 29-30: Word form")
    D.table(
        ["Câu", "Đáp án", "Giải thích"],
        [
            ["29", "**decisions**", "Sau tính từ 'important' cần **danh từ**; 'make decisions' (đưa ra quyết định); dùng số nhiều vì nói chung, không có mạo từ."],
            ["30", "**pollution**", "Cần **danh từ** làm chủ ngữ: air pollution = ô nhiễm không khí (danh từ không đếm được)."],
        ],
        [10, 22, 138], align_center_cols=(0,))

    D.h3("Câu 31-34: Viết lại câu")
    D.table(
        ["Câu", "Đáp án mẫu", "Giải thích"],
        [
            ["31", "A lot of trees **are planted** in the park every spring.",
             "Bị động hiện tại đơn: 'every spring' → is/are + V3/ed; tân ngữ 'a lot of trees' (số nhiều) → **are planted**."],
            ["32", "My sister **is going to learn** how to play the guitar.",
             "'has already decided' = dự định đã quyết định từ trước → dùng **be going to**."],
            ["33", "The box is **too heavy for me to lift**.",
             "Cấu trúc **too + adj + for O + to V**: quá... đến nỗi ai đó không thể làm gì."],
            ["34", "Nam was very tired after the clean-up activity, **but he still helped his mother cook dinner**.",
             "Câu ghép với **but** nối hai ý tương phản; giữ nguyên thì quá khứ đơn; 'help + O + bare infinitive'."],
        ],
        [10, 62, 98], align_center_cols=(0,))
    D.psmall("Lưu ý: học sinh có thể diễn đạt tương đương, miễn đúng cấu trúc ngữ pháp và giữ nguyên nghĩa.")

    D.h3("Câu 35: Bài viết mẫu (139 từ)")
    D.box("Sharing housework brings many benefits to every member of the family. First, it makes the workload "
          "lighter. When all members join hands, chores such as cooking, doing the laundry and tidying up are "
          "finished more quickly, so everybody has more time to rest. Second, sharing housework teaches children "
          "important life skills. By doing chores, they learn how to look after themselves and become more "
          "independent and responsible. Third, it helps family members understand and love one another more. "
          "Working together gives them chances to talk, share and laugh, which brings the family closer. In "
          "addition, when fathers share the housework with mothers, children learn a good lesson about equality. "
          "In short, sharing housework is not only about keeping the house clean, but also about building a warm "
          "and close-knit family.", kind="tip", title="MODEL PARAGRAPH")
    D.table(
        ["Tiêu chí", "Điểm tối đa", "Yêu cầu"],
        [
            ["Nội dung", "0,4", "Đủ 2-3 lợi ích, bám sát đề, có ví dụ cụ thể"],
            ["Ngữ pháp & từ vựng", "0,3", "Dùng đúng thì, từ vựng Unit 1 (chia sẻ việc nhà, life skills, close-knit...)"],
            ["Bố cục & liên kết", "0,2", "Có câu chủ đề - thân - kết; dùng First/Second/In short..."],
            ["Chính tả & trình bày", "0,1", "Sạch đẹp, không quá 3 lỗi chính tả"],
        ],
        [40, 22, 108], align_center_cols=(1,))

    # ---------------- transcripts
    D.h2("D4. Transcript hai bài nghe (dùng để tự luyện)")
    D.h3("Listening 1 - Chia sẻ việc nhà trong gia đình Linh (độc thoại, ~185 từ)")
    D.p("*Hello everyone. I'm Linh, and today I'd like to tell you about how my family shares housework. There are "
        "four people in my family: my parents, my younger brother and me. We all believe that housework should be "
        "divided fairly, so nobody feels tired or unhappy. My father is the breadwinner, but that doesn't mean he "
        "never does any chores. He does the heavy lifting, repairs things around the house, and cooks dinner at "
        "weekends. My mother works eight hours a day in a hospital, so during the week she only prepares breakfast "
        "and does the shopping online. My brother Nam is in Grade 7. He takes out the rubbish and feeds our dog "
        "every evening. As for me, I'm in Grade 10, so I do the laundry twice a week and wash the dishes after "
        "dinner. We also tidy up the living room together on Saturday mornings. Sharing housework has brought us "
        "closer. We talk and laugh while working, and my parents have more time to relax. I think every family "
        "member, even children, should do some chores to help the family.*")
    D.h3("Listening 2 - Nam rủ Mai đi xem hoà nhạc (hội thoại, ~180 từ)")
    D.p("*Nam: Hey, Mai! Have you got any plans for Saturday evening?*\n"
        "*Mai: Not yet. Why?*\n"
        "*Nam: My school's music club is giving a concert at the Youth Centre. Would you like to come?*\n"
        "*Mai: Sounds great! What kind of music will they play?*\n"
        "*Nam: Mostly pop and dance music, but there will also be some traditional folk songs. My sister is "
        "playing the piano in two performances.*\n"
        "*Mai: That's exciting! I really enjoy live music. How much is a ticket?*\n"
        "*Nam: It's 50,000 dong, and students get half price. The concert starts at 7.30 p.m.*\n"
        "*Mai: OK. Where shall we meet?*\n"
        "*Nam: Let's meet at the bus stop near our school at 6.45, and we can take bus number 8.*\n"
        "*Mai: Great. Oh, should I bring anything?*\n"
        "*Nam: Just bring your student card for the discount. And don't be late - the hall is always full before "
        "seven.*\n"
        "*Mai: Don't worry. See you on Saturday!*")

    # ---------------- final tips
    D.h2("D5. 10 mẹo ghi nhớ nhanh trước ngày thi")
    D.numbered([
        "**FANBOYS** - 7 liên từ câu ghép: For, And, Nor, But, Or, Yet, So.",
        "**Dấu hiệu hiện tại tiếp diễn:** now, at the moment, Look!, Listen! → am/is/are + V-ing.",
        "**will**: quyết định tức thì + dự đoán không bằng chứng; **be going to**: kế hoạch có trước + dự đoán có bằng chứng.",
        "**Bị động = be + V3/ed**; 'be' chia theo thì của câu chủ động.",
        "**make/let + O + V** (nguyên thể không to); **allow/advise/tell + O + TO V**.",
        "**too + adj + to V** (quá... không thể) ↔ **not + adj enough + to V**.",
        "**3R** bảo vệ môi trường: Reduce - Reuse - Recycle; collocation: fill **in** the form, be interested **in**, listen **to** music, keen **on**.",
        "**Word form:** sau tính từ + trước danh từ thường là vị trí của danh từ; bổ nghĩa động từ → trạng từ.",
        "**Viết đoạn:** mở - thân (First/Second/Finally) - kết (In short) = 5-7 câu, 120-150 từ.",
        "Làm bài theo thứ tự: trắc nghiệm dễ trước; viết lại câu luôn kiểm tra **thì** và **nghĩa không đổi**.",
    ])
    D.gap(8)
    D.p("- **Chúc các em ôn tập tốt và đạt kết quả cao trong kì kiểm tra giữa học kỳ 1!** -", "center")
