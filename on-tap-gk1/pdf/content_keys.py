# -*- coding: utf-8 -*-
"""PHAN 7 – Dap an + giai thich + tapescripts. PHAN 8 – Bang tra nhanh."""
from texts import (T1_SC_A, T1_SC_B, T2_SC_A, T2_SC_B,
                    MP_FAMILY, MP_ENV, MP_MUSIC)

BLOCKS = [
    ("h1", "PHẦN 7. ĐÁP ÁN – GIẢI THÍCH CHI TIẾT – FULL TAPESCRIPT"),
    ("small", "Học theo 3 bước: ① So đáp án, tô đỏ câu sai · ② Đọc giải thích để hiểu VÌ SAI · ③ Chép câu sai + nguyên nhân vào sổ tay lỗi. "
              "Sau khi làm xong mới đọc tapescript: mỗi đoạn, hãy tự đọc to 1 lượt với tốc độ ~140 từ/phút để não “khớp” âm thanh với mặt chữ."),

    # ---------------- TEST 1 KEYS ----------------
    ("h2", "7.1. ĐÁP ÁN ĐỀ SỐ 1 (kèm giải thích những câu dễ sai)"),
    ("table", {"header": ["TN", "Đáp án", "TN", "Đáp án", "TN", "Đáp án", "TN", "Đáp án"],
               "rows": [
                   ["1", "A", "8", "C", "15", "B", "22", "B"],
                   ["2", "B", "9", "B", "16", "A", "23", "B"],
                   ["3", "A", "10", "B", "19", "B", "24", "A"],
                   ["4", "B", "11", "A", "20", "A", "25", "B"],
                   ["5", "A", "12", "B", "21", "A", "26", "A"],
                   ["6", "B", "13", "A", "27", "A", "28", "B"],
                   ["7", "A", "14", "A", "29", "A", "", ""],
               ], "widths": [0.09, 0.16, 0.09, 0.16, 0.09, 0.16, 0.09, 0.16],
               "center": [0, 1, 2, 3, 4, 5, 6, 7], "fs": 8.4}),
    ("h3", "Giải thích nhanh – phần trắc nghiệm (câu dễ sai)"),
    ("bullets", [
        "<b>Câu 2 (False):</b> mẹ “nấu + giặt đồ”, còn TƯỚI CÂY là của bố → nhận định đảo người. Đây là bẫy #1 của dạng True/False.",
        "<b>Câu 4 (False):</b> chiều muộn cả nhà thư giãn, nghe nhạc → “never relaxes” sai hoàn toàn.",
        "<b>Câu 8 (C):</b> “My cousin is performing” – Minh nói, nên là ANH EM HỌ CỦA MINH; phương án A/B đánh tráo người nói.",
        "<b>Câu 14 (A):</b> “bought the tickets yesterday” = kế hoạch đã chốt trước → be going to; “will be going” (B) sai ngữ pháp sau will + V-bare.",
        "<b>Câu 15 (B):</b> “Millions of trees” không thể tự cắt → bị động hiện tại đơn số nhiều: are cut down.",
        "<b>Câu 16 (A):</b> sold out là NGUYÊN NHÂN, vế sau là KẾT QUẢ → so.",
        "<b>Câu 19 (B):</b> swap stand (quầy trao đổi) → give away (cho/tặng); throw away = vứt (mâu thuẫn “take home something new”).",
        "<b>Câu 21 (A):</b> “will be ______ by” → bị động: hosted.",
        "<b>Câu 22 (B):</b> “simple ideas ___ useful tips” — liệt kê cùng chiều → and.",
        "<b>Câu 27 (A):</b> “this information” tổng kết lại các phát hiện + lời khuyên ở hai phần trước (nhìn 1–2 câu liền trước).",
        "<b>Câu 29 (A):</b> a mở (chào – hỏi), c giải thích mâu thuẫn, b phản ứng “sounds hard!”, d giải pháp mới, e chốt “Good idea. Thank you!” — chỉ a-c-b-d-e là mạch.  ",
        "<b>Câu 30 (A):</b> b mở thư (chủ đích “We are writing to tell you…”), e kết (hope you will join); a–c–d thân bài theo First → After that → Please bring.",
    ]),
    ("h3", "Đáp án tự luận – Đề 1 (thang: 17–18: 0,5đ; 31–34: 0,25đ; 35: 1,0đ)"),
    ("table", {"header": ["Câu", "Đáp án chuẩn", "Lưu ý chấm"],
               "rows": [
                   ["17", "successful", "sau “a ___ week” → tính từ; sai: success (danh từ)"],
                   ["18", "careless", "ngữ nghĩa mỉa mai “It was ___ of Peter” + để vòi nước chảy → careless; sai: careful (ngược nghĩa)"],
                   ["31", "Millions of plastic bottles are thrown away every day.", "throw → thrown (V3); bỏ “by people” được tính như nhau"],
                   ["32", "Their team is going to start the recycling project next month.", "đủ: is going to + V"],
                   ["33", "The film was boring, but we still watched it until the end.", "phẩy + but; giữ “still watched”"],
                   ["34", "The music is so loud that the neighbours can't sleep.", "so + adj + that + can't"],
                   ["35", "Xem bài mẫu MP1 (bên dưới) – chấm theo rubric 4.6", "đủ 120–150 từ; có ý kiến cá nhân"],
               ], "widths": [0.08, 0.5, 0.42], "center": [0], "fs": 8.3}),
    ("h3", "Bài mẫu chấm 1,0đ – Đề 1 (đúng 147 từ)"),
    ("passage", [MP_FAMILY], "MẪU ĐOẠN VĂN – chia sẻ việc nhà"),

    # ---------------- TEST 2 KEYS ----------------
    ("h2", "7.2. ĐÁP ÁN ĐỀ SỐ 2"),
    ("table", {"header": ["TN", "Đáp án", "TN", "Đáp án", "TN", "Đáp án", "TN", "Đáp án"],
               "rows": [
                   ["1", "B", "8", "C", "15", "B", "22", "B"],
                   ["2", "B", "9", "B", "16", "A", "23", "B"],
                   ["3", "A", "10", "B", "19", "B", "24", "B"],
                   ["4", "A", "11", "B", "20", "B", "25", "A"],
                   ["5", "A", "12", "C", "21", "A", "26", "A"],
                   ["6", "B", "13", "B", "27", "B", "28", "A"],
                   ["7", "A", "14", "A", "29", "A", "", ""],
               ], "widths": [0.09, 0.16, 0.09, 0.16, 0.09, 0.16, 0.09, 0.16],
               "center": [0, 1, 2, 3, 4, 5, 6, 7], "fs": 8.4}),
    ("h3", "Giải thích nhanh – Đề 2"),
    ("bullets", [
        "<b>Câu 1 (False):</b> “moved to Hue”, không phải Đà Nẵng.",
        "<b>Câu 2 (False):</b> BÀ Tran dạy nấu ăn; ông Tran sửa đồ trong nhà.",
        "<b>Câu 4 (True):</b> hợp đồng viết ra sau các trục trặc nhỏ (towel, dishes) → suy luận “to settle small problems” đúng.",
        "<b>Câu 12 (C):</b> “leave + O + V-ing” (leave the tap running) là collocation cố định; let + V-bare → không khớp “running”.",
        "<b>Câu 13 (B):</b> “think” = nhận xét/không gian → không tiếp diễn.",
        "<b>Câu 14 (A):</b> let + O + V-bare.",
        "<b>Câu 19 (B):</b> tương phản “Join us … ___ you don't need to be a star yet” → but.",
        "<b>Câu 21 (A):</b> funny ___ about rhythm: lessons hợp nghĩa; rubbish/singers phá vỡ cấu trúc câu.",
        "<b>Câu 22 (B):</b> a big concert không tự tổ chức → is organized (bị động).",
        "<b>Câu 23 (B):</b> must + V-bare.",
        "<b>Câu 27 (B):</b> “such simple habits” chỉ chính các thói quen của gia đình (họp 15 phút, chia việc, kiểm tra phòng) vừa kể.",
        "<b>Câu 29 (A):</b> b nêu chủ đề → c “To begin with” → a “Second” → d “Finally” → e kết quả.",
    ]),
    ("h3", "Đáp án tự luận – Đề 2"),
    ("table", {"header": ["Câu", "Đáp án chuẩn", "Lưu ý chấm"],
               "rows": [
                   ["17", "arrangement", "sau “an excellent ___” → danh từ; arrange → arrangement"],
                   ["18", "energetic", "sau “stays” (nối tiếp) → tính từ; energy → energetic"],
                   ["31", "His old motorbike is being repaired (by my father) at the moment.", "HT tiếp diễn → is being + V3; nhiều em quên “being”"],
                   ["32", "We are going to open a second-hand uniform stall next term.", "intend → be going to"],
                   ["33", "The homework was too difficult for me to finish.", "so…that + không → too + adj + for O + to V"],
                   ["34", "Lan likes pop music, but her brother prefers folk music.", "tương phản → but, giữ dấu phẩy"],
                   ["35", "Xem bài mẫu MP3 – chấm theo rubric 4.6", "đủ 120–150 từ"],
               ], "widths": [0.08, 0.5, 0.42], "center": [0], "fs": 8.3}),
    ("h3", "Bài mẫu chấm 1,0đ – Đề 2 (đúng 148 từ)"),
    ("passage", [MP_MUSIC], "MẪU ĐOẠN VĂN – âm nhạc trong đời sống học sinh"),

    # ---------------- TAPESCRIPTS ----------------
    ("h2", "7.3. PHỤ LỤC – FULL TAPESCRIPT (đọc 2 lượt, tốc độ ~140 từ/phút)"),
    ("h3", "TAPESCRIPT 1 – Đề 1 (Mai's Saturday – 188 từ)"),
    ("passage", [T1_SC_A]),
    ("small", "Mấu chốt: mẹ = nấu ăn + giặt đồ; bố = tưới cây + đổ rác; Nam = xách túi nặng + chơi guitar; chiều = thư giãn. Ý chính: san việc → nhanh + gắn kết."),
    ("h3", "TAPESCRIPT 2 – Đề 1 (Lan & Minh – 190 từ)"),
    ("passage", [T1_SC_B]),
    ("small", "Chi tiết cần nhớ: gặp 7:30 ở cổng trường; nhặt rác ở West Lake; diễn viên = cousin của Minh; vé gần hết nên Lan chốt mua ngay; tình nguyện viên được 1 vé miễn phí."),
    ("h3", "TAPESCRIPT 3 – Đề 2 (Tom's host family – 189 từ)"),
    ("passage", [T2_SC_A]),
    ("small", "Đảo vai là bẫy chính: bà Tran dạy nấu ăn; ông Tran sửa đồ; Hung chơi guitar. Thông điệp cuối bài: nhà hạnh phúc = nhà mọi người giúp nhau."),
    ("h3", "TAPESCRIPT 4 – Đề 2 (Minh & Lan – 181 từ)"),
    ("passage", [T2_SC_B]),
    ("small", "Chuỗi logic: từ chối (do bận đón cousin) → tò mò về band → nhắn tin đổi kế hoạch → chốt giờ (cổng đóng 7:15 → đi 5:45). Câu ý chính chọn “họ đổi kế hoạch để cùng đi”."),

    # ---------------- PARAGRAPH SCORING ----------------
    ("h2", "7.4. PHIẾU TỰ CHẤM ĐOẠN VĂN (dùng cho bài của em – 4 tiêu chí, 1,0đ)"),
    ("table", {"header": ["① Nội dung 0,35", "② Tổ chức 0,25", "③ Ngôn ngữ 0,25", "④ Chính xác & định dạng 0,15"],
               "rows": [[
                   "0,20 đủ 2–3 ý đúng đề; 0,15 có quan điểm rõ (I believe…)",
                   "0,15 một mạch đoạn văn, câu trước–sau dính nhau; 0,10 có ≥ 3 liên từ (While/Besides/so/To sum up)",
                   "0,15 ≥ 6 từ trong bảng từ chủ đề; 0,10 dùng đúng 1–2 cấu trúc chủ điểm (bị động, too…to, FANBOYS…)",
                   "0,10 đủ 120–150 từ + viết hoa, dấu câu; 0,05 không lỗi động từ (s/es, V3, to-V)",
               ]], "widths": [0.25, 0.25, 0.25, 0.25], "fs": 8.0}),
    ("p", "Tự chấm xong, đối chiếu với 3 bài mẫu Phần 4.6 để thấy khoảng cách; chép 2 câu mình muốn “nâng cấp” và viết lại theo kiểu bài mẫu."),

    # =========================== PART 8 ===========================
    ("h1", "PHẦN 8. BẢNG TRA NHANH – “10 PHÚT TRƯỚC KHI VÀO PHÒNG THI”"),
    ("h2", "8.1. 12 quy tắc vàng (đọc thuộc – không cần hiểu sâu lúc này)"),
    ("numbers", [
        "every day / usually / often → <b>V(s/es)</b> · now / Look! / at the moment → <b>am-is-are + V-ing</b>.",
        "want · think · know · have (=có) → KHÔNG bao giờ thêm -ing.",
        "Có bằng chứng (mây đen, vé mua rồi, kế hoạch) → <b>be going to</b>. Quyết tại chỗ / hứa / tin tưởng → <b>will</b>.",
        "Sau when/before/as soon as: KHÔNG dùng will.",
        "Nhìn thấy <b>by + người</b> hoặc chủ ngữ “tự làm không được” → bị động: <b>BE + V3</b>. BE chia đúng thì, số nhiều là are/were.",
        "Hai mệnh đề độc lập + 1 chỗ trống giữa → chọn <b>FANBOYS</b> (and/but/so/or/yet), nhớ dấu phẩy trước liên từ.",
        "<b>Because</b> đi một mình, <b>so</b> đi một mình — không dùng cả hai.",
        "want/decide/hope/plan/promise/agree → <b>to + V</b>; modal (can/must/should/will) + let/make + O → <b>V-bare</b>.",
        "enjoy/avoid/mind/finish/practise → <b>V-ing</b> (không to).",
        "too + adj + to V = so + adj + that + S + can't V · not + adj + enough to V = too + trái nghĩa + to V.",
        "Chỗ trống trước danh từ → tính từ; sau my/a/the → danh từ; sau be → tính từ; bổ nghĩa V → trạng từ.",
        "Viết lại câu: GIỮ nguyên thì; đoạn văn: đếm nhẩm 12 dòng × 12 từ ≈ 145.",
    ]),
    ("h2", "8.2. Bảng từ “đi thi phải nhớ mặt” – 30 từ hay nhất (đã lọc từ bảng 2.1)"),
    ("table", {"header": ["Family life", "Humans and the Environment", "Music"],
               "rows": [[
                   "housework · do the laundry · wash up · take out the rubbish · tidy up · set the table · share · look after · nuclear family · supportive · reliable",
                   "pollution · deforestation · global warming · endangered species · recycle · reuse · reduce · sort the waste · disposable · save energy · renewable · raise awareness",
                   "folk music · catchy · lyrics · melody · perform · rehearse · composer · conductor · audience · competition · award · soothing · play the guitar",
               ]], "widths": [0.34, 0.36, 0.3], "fs": 8.2}),
    ("h2", "8.3. Checklist 5 ngày cuối (30–45 phút/ngày)"),
    ("table", {"header": ["Ngày", "Việc cần làm", "Xong"],
               "rows": [
                   ["D-5", "Học thuộc bảng từ 2.1 (3 unit) + làm lại toàn bộ Quick Check Phần 3, chỉ chữa câu sai", "☐"],
                   ["D-4", "Đọc Phần 4 + làm trọn Đề số 1 (bấm giờ) — tự chấm, chép lỗi", "☐"],
                   ["D-3", "Học bảng họ nhà từ 2.2 + 8 khuôn viết lại câu 4.5; viết 1 đoạn văn chủ đề còn yếu", "☐"],
                   ["D-2", "Làm trọn Đề số 2 (bấm giờ) — chấm và so với đề 1: lỗi cũ có lặp lại?", "☐"],
                   ["D-1", "Đọc Bảng tra nhanh Phần 8 + sổ tay lỗi; trước khi ngủ nghe lại tapescript 1–2 đọc chậm", "☐"],
               ], "widths": [0.1, 0.78, 0.12], "center": [0, 2], "fs": 8.4}),
    ("box", "tip", [
        "<b>Ngay trong phòng thi:</b> câu 17–18 (dạng từ) luôn kiểm tra thêm chính tả đuôi (-ful/-less/-tion/-ment); "
        "câu viết lại: viết nháp ĐỦ CÂU (có chấm cuối) rồi chép; đoạn văn: viết số từ ước lượng ở góc giấy nháp để canh 120–150."]),
    ("h2", "Ghi chú bản quyền & nguồn dữ liệu"),
    ("small", "Tài liệu do Arena Agent biên soạn tự động ngày 24-10-2026 từ tệp <b>2026_2027_MA TRẬN 10_GK1.docx</b> (ma trận + bảng đặc tả "
              "kỹ thuật đề kiểm tra giữa kì 1 môn Tiếng Anh 10, năm học 2026–2027). Phạm vi kiến thức đối chiếu sách Global Success 10 – Units 1–3. "
              "Ngữ liệu đề, tapescript, bài mẫu là nội dung tự soạn (original) — không sao chép từ đề thi thương mại nào. "
              "Giáo viên được phép sửa, in, phát cho học sinh; khi dùng lại cần ghi nguồn."),
]
