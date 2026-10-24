#import "style.typ": *

// ============================================================================
// PART I: IN-DEPTH FORENSIC ANALYSIS OF "2026_2027_MA TRẬN 10_GK1.docx"
// ============================================================================

#part-banner(
  "PHẦN I",
  "PHÂN TÍCH CHUYÊN SÂU MA TRẬN & ĐẶC TẢ ĐỀ THI GK1 (2026–2027)",
  "Giải mã cấu trúc, ma trận điểm số, cấp độ nhận thức và đối chiếu kỹ thuật từ tệp gốc 2026_2027_MA TRẬN 10_GK1.docx"
)

= 1. Tổng quan cấu trúc & Định hướng đổi mới của Đề thi Giữa kỳ 1 (2026–2027)

Qua phân tích toàn diện cấu trúc dữ liệu của tệp *`2026_2027_MA TRẬN 10_GK1.docx`* (gồm Bảng Ma trận 15 dòng × 22 cột lưới và Bảng Đặc tả kỹ thuật 24 dòng × 6 cột), đề kiểm tra Giữa học kỳ 1 môn Tiếng Anh 10 năm học 2026–2027 được thiết kế theo #strong[định hướng đánh giá năng lực ngôn ngữ thực tế] của Chương trình GDPT 2018 (bộ sách *Global Success*), đồng bộ trực tiếp với định dạng đề thi Tốt nghiệp THPT từ năm 2025 trở đi:

- *Phạm vi chủ điểm (3 Units đầu học kỳ 1):* #strong[Unit 1: Family Life] (*Cuộc sống gia đình*), #strong[Unit 2: Humans and the Environment] (*Con người và môi trường*), và #strong[Unit 3: Music] (*Âm nhạc*).
- *Cấu trúc cân bằng "4 Trụ cột × 25%":* Đề thi chia đều 10,0 điểm cho 4 phần: #strong[Listening (2,5đ)] – #strong[Language (2,5đ)] – #strong[Reading (2,5đ)] – #strong[Writing (2,5đ)]. Không có kỹ năng nào bị bỏ ngỏ.
- *Tỉ lệ hình thức thi (70% TNKQ – 30% Tự luận):*
  - #strong[Phần Trắc nghiệm khách quan (TNKQ):] Gồm #strong[28 câu] × #strong[0,25 điểm/câu] = #strong[7,00 điểm (70%)]. Toàn bộ câu hỏi trắc nghiệm tập trung ở mức *Nhận biết* (17 câu) và *Thông hiểu* (11 câu).
  - #strong[Phần Tự luận (TL):] Gồm #strong[6 câu đơn lẻ + 1 bài viết đoạn văn] = #strong[3,00 điểm (30%)]. Toàn bộ phần tự luận nằm trọn ở mức *Vận dụng*, đóng vai trò phân loại học sinh Khá – Giỏi – Xuất sắc.

#callout(title: "4 Thay đổi chiến lược học sinh lớp 10 bắt buộc phải nắm rõ", kind: "trap")[
  1. *KHÔNG có phần Ngữ âm rời rạc (0% Pronunciation / Word Stress):* Khác với các mẫu đề cũ, ma trận 2026–2027 #strong[không] ra câu hỏi trắc nghiệm tìm từ phát âm khác hay trọng âm khác. Học sinh không nên mất hàng giờ cày mẹo phát âm rời rạc mà hãy học phiên âm gắn liền với nghĩa từ vựng.
  2. *Câu Từ vựng Tự luận (Word Form) có trọng số điểm GẤP ĐÔI câu trắc nghiệm:* Phần Vocabulary chiếm #strong[15% (1,50 điểm)] gồm 2 câu TNKQ (0,25đ × 2 = 0,50đ) và #strong[2 câu Tự luận chia dạng từ N/V/Adj/Adv] chiếm tới #strong[1,00 điểm (0,50 điểm/câu!)]. Chỉ sai 2 câu từ loại tự luận là mất ngay 1 điểm toàn bài!
  3. *Xuất hiện dạng Đọc điền Tờ rơi / Quảng cáo (Reading 1 – Cloze-text):* Thay vì đoạn văn học thuật dài, bài đọc điền từ (5 câu = 1,25đ) sử dụng ngữ liệu thực tế là #strong[tờ rơi (leaflet) hoặc quảng cáo (advertisement)] xoay quanh sự kiện gia đình, chiến dịch sống xanh hoặc đêm nhạc.
  4. *Xuất hiện dạng Sắp xếp Hội thoại / Lá thư / Đoạn văn (Writing 1 – Re-ordering):* Có #strong[2 câu trắc nghiệm (0,50đ)] yêu cầu sắp xếp các câu rời thành hội thoại, bức thư hoặc đoạn văn mạch lạc — dạng bài thương hiệu của cấu trúc thi mới.
]

= 2. Bảng Ma trận Chuẩn hóa & Quy đổi Điểm số Chi tiết

Dưới đây là bảng tổng hợp chuẩn hóa toàn bộ thông số từ Ma trận & Bảng đặc tả gốc, bổ sung cột #strong[Đơn giá điểm từng câu] đã được kiểm chứng toán học chính xác 100%:

#block(breakable: false)[
  #set text(size: 8.2pt)
  #table(
    columns: (auto, 1.15fr, 1.65fr, auto, auto, auto, auto, auto, auto),
    inset: (x: 5pt, y: 5pt),
    align: (center + horizon, left + horizon, left + horizon, center + horizon, center + horizon, center + horizon, center + horizon, center + horizon, right + horizon),
    stroke: 0.45pt + c-border,
    fill: (_, row) => if row < 2 { c-navy } else if row >= 11 { c-navy-soft } else if calc.odd(row) { white } else { c-zebra },

    table.cell(rowspan: 2)[#text(fill: white, weight: "bold")[TT]],
    table.cell(rowspan: 2)[#text(fill: white, weight: "bold")[Kỹ năng /\ Phần thi]],
    table.cell(rowspan: 2)[#text(fill: white, weight: "bold")[Đơn vị kiến thức & Dạng bài\ (SGK Global Success: Units 1–2–3)]],
    table.cell(colspan: 2)[#text(fill: white, weight: "bold")[TNKQ (70%)]],
    table.cell(colspan: 1)[#text(fill: white, weight: "bold")[Tự luận]],
    table.cell(rowspan: 2)[#text(fill: white, weight: "bold")[Tổng\ số câu]],
    table.cell(rowspan: 2)[#text(fill: white, weight: "bold")[Tỉ lệ\ %]],
    table.cell(rowspan: 2)[#text(fill: white, weight: "bold")[Điểm số\ (Đơn giá)]],

    [#text(fill: white, weight: "bold")[Biết]],
    [#text(fill: white, weight: "bold")[Hiểu]],
    [#text(fill: white, weight: "bold")[VD]],

    [*1*], [*LISTENING*\ *(2,50đ)*], [*Listening 1:* Hội thoại/độc thoại ≈ 1,5 phút (180–200 từ) – *True/False*], [3], [2], [0], [5 TN], [12,5%], [*1,25đ* (0,25×5)],
    [], [], [*Listening 2:* Hội thoại/độc thoại ≈ 1,5 phút (180–200 từ) – *MCQs*], [3], [2], [0], [5 TN], [12,5%], [*1,25đ* (0,25×5)],

    [*2*], [*LANGUAGE*\ *(2,50đ)*], [*Vocabulary:* Từ vựng, cụm từ (TN) & Từ loại N/V/Adj/Adv trong câu (TL)], [1], [1], [*2*], [2 TN +\ 2 TL], [15,0%], [*1,50đ*\ (0,25×2 + *0,50×2*)],
    [], [], [*Grammar:* HTĐ/HTTD, Will/Be going to, Bị động, Câu ghép, To-V/V0], [2], [2], [0], [4 TN], [10,0%], [*1,00đ* (0,25×4)],

    [*3*], [*READING*\ *(2,50đ)*], [*Reading 1 (Cloze-text):* Đọc điền từ Tờ rơi / Quảng cáo], [3], [2], [0], [5 TN], [12,5%], [*1,25đ* (0,25×5)],
    [], [], [*Reading 2 (Comprehension):* Đọc hiểu đoạn văn 220–250 từ (MCQs)], [3], [2], [0], [5 TN], [12,5%], [*1,25đ* (0,25×5)],

    [*4*], [*WRITING*\ *(2,50đ)*], [*Writing 1 (Re-ordering):* Sắp xếp hội thoại / lá thư / đoạn văn], [2], [0], [0], [2 TN], [5,0%], [*0,50đ* (0,25×2)],
    [], [], [*Writing 2 (Transformation):* Viết lại câu đồng nghĩa theo cấu trúc], [0], [0], [*4*], [4 TL], [10,0%], [*1,00đ* (0,25×4)],
    [], [], [*Writing 3 (Paragraph):* Viết đoạn văn / thư / bài báo 120–150 từ], [0], [0], [*1 bài*], [1 bài TL], [10,0%], [*1,00đ* (1,00×1)],

    table.cell(colspan: 3)[*TỔNG SỐ CÂU THEO HÌNH THỨC & MỨC ĐỘ*], [*17*], [*11*], [*6 + 1 bài*], [*28 TN +\ 6 câu + 1 bài*], [*100%*], [*10,00 điểm*],
    table.cell(colspan: 3)[*TỔNG ĐIỂM THỰC TẾ / TỈ LỆ CHÍNH XÁC*], [*4,25đ*\ *(42,5%)*], [*2,75đ*\ *(27,5%)*], [*3,00đ*\ *(30,0%)*], [*TN: 7,0đ*\ *(70%)*], [*TL: 3,0đ*\ *(30%)*], [*Mốc làm tròn:\ 4,0 – 3,0 – 3,0*],
  )
]

= 3. Phân tích Cấp độ Nhận thức & Yêu cầu Cần đạt theo từng Phần

1. #strong[Mức độ Nhận biết (17 câu TNKQ = 4,25 điểm thực tế ≈ 40% quy ước):]
   - *Listening (6 câu = 1,50đ):* Nghe bắt thông tin chi tiết trực tiếp (số liệu, thời gian, tên hoạt động, sự kiện xuất hiện rõ trong bài nghe).
   - *Language (3 câu = 0,75đ):* 1 câu nhận diện nghĩa từ vựng cơ bản theo chủ đề Unit 1–3; 2 câu nhận diện dấu hiệu ngữ pháp trực tiếp (trạng từ chỉ tần suất, dấu hiệu *now/at the moment*, liên từ cơ bản, công thức bị động cơ bản).
   - *Reading (6 câu = 1,50đ):* 3 câu ở bài Tờ rơi/Quảng cáo (từ loại, giới từ, thành tố liên kết cơ bản) + 3 câu thông tin chi tiết/thành tố ngôn ngữ trong bài Đọc hiểu 220–250 từ.
   - *Writing 1 (2 câu = 0,50đ):* Nhận diện câu mở đầu – câu phản hồi – từ nối trình tự để sắp xếp đúng đoạn hội thoại, lá thư hoặc đoạn văn ngắn.
2. #strong[Mức độ Thông hiểu (11 câu TNKQ = 2,75 điểm thực tế ≈ 30% quy ước):]
   - *Listening (4 câu = 1,00đ):* Hiểu ý chính toàn bài, thái độ người nói hoặc câu đã được diễn đạt lại (*paraphrase*) ở cả bài True/False (2 câu) và MCQs (2 câu).
   - *Language (3 câu = 0,75đ):* 1 câu cụm từ cố định (*collocation*) / phân biệt từ trong ngữ cảnh; 2 câu phân biệt cặp ngữ pháp dễ nhầm (*Present Simple vs. Continuous*, *Will vs. Be going to*, *To-inf vs. Bare-inf*).
   - *Reading (4 câu = 1,00đ):* 2 câu hiểu mạch liên kết/ngữ cảnh trong Tờ rơi/Quảng cáo + 2 câu tìm ý chính (*main idea*), từ quy chiếu (*it/they/them/this*) và suy luận loại trừ (*TRUE / NOT mentioned*) trong bài đọc 220–250 từ.
3. #strong[Mức độ Vận dụng (6 câu + 1 bài viết Tự luận = 3,00 điểm = 30%):]
   - *Vocabulary Tự luận (2 câu = 1,00đ):* Biến đổi đúng từ gốc sang Danh từ, Động từ, Tính từ hoặc Trạng từ phù hợp cấu trúc ngữ pháp và nghĩa của câu.
   - *Writing 2 – Sentence Transformation (4 câu = 1,00đ):* Viết lại câu giữ nguyên nghĩa bằng câu bị động, câu ghép, cấu trúc *to-infinitive / bare infinitive* hoặc tương lai dự định.
   - *Writing 3 – Paragraph Writing (1 bài = 1,00đ):* Viết đoạn văn / bức thư / bài báo ngắn #strong[120–150 từ] trình bày mạch lạc quan điểm cá nhân về *Family Life*, *Humans and the Environment*, hoặc *Music*.

= 4. Lưu ý Kỹ thuật: 06 Điểm Bất nhất Phát hiện khi Đối chiếu Tệp Gốc `.docx`

Khi kiểm định chéo từng ô giữa #strong[Bảng I (Ma trận)] và #strong[Bảng II (Bảng đặc tả kỹ thuật)] trong tệp `2026_2027_MA TRẬN 10_GK1.docx`, có #strong[06 chi tiết sai số biên tập nhỏ] do thao tác ghép bảng trên Word. Đề cương này đã chuẩn hóa hoàn toàn để giáo viên và học sinh áp dụng thống nhất:

#table(
  columns: (auto, 1.3fr, 1.8fr, 1.8fr),
  inset: (x: 6pt, y: 5pt),
  align: (center + horizon, left + horizon, left + horizon, left + horizon),
  stroke: 0.45pt + c-border,
  fill: (_, row) => if row == 0 { c-navy } else if calc.odd(row) { white } else { c-zebra },
  text(fill: white, weight: "bold", size: 8.3pt)[TT],
  text(fill: white, weight: "bold", size: 8.3pt)[Vị trí trong tệp `.docx` gốc],
  text(fill: white, weight: "bold", size: 8.3pt)[Chi tiết bất nhất trong bản gốc],
  text(fill: white, weight: "bold", size: 8.3pt)[Chuẩn hóa chính xác để ôn thi],

  [*1*], [Bảng Đặc tả – cuối mục *Listening* (Dòng 7)], [Có một dòng trống nội dung nhưng cột TNKQ bị gõ sót số `1` (nếu cộng cả số này sẽ thành 29 câu thay vì 28 câu).], [*Listening chuẩn gồm đúng 10 câu TNKQ* (Part 1: 5 câu + Part 2: 5 câu = 2,50 điểm), khớp với dòng Tổng 28 câu TN.],
  [*2*], [Bảng Ma trận – dòng *Writing 1* & cột *Tổng*], [Writing 1 chỉ có `2` câu TN Biết (5%), nhưng cột *Tổng → Hiểu* lại ghi thừa số `3`, làm dòng Tổng cộng lệch thành `20 – 15 – 2`.], [*Writing 1 có đúng 2 câu TN Nhận biết (0,50đ)*. Tổng thực tế toàn đề là `17 Biết + 11 Hiểu = 28 câu TN`.],
  [*3*], [Bảng Ma trận – dòng *Tổng điểm theo mức độ*], [17 câu Biết × 0,25 = 4,25đ (42,5%) và 11 câu Hiểu × 0,25 = 2,75đ (27,5%), nhưng dòng cuối ghi tròn `4đ (40%) – 3đ (30%)`.], [Mỗi câu TN vẫn chấm đều *0,25đ/câu* (tổng TN = 7,00đ); con số 40%–30%–30% là tỉ lệ quy ước làm tròn của ma trận.],
  [*4*], [Bảng Đặc tả – mục *Reading 2* (Dòng 16–17)], [Cả 2 nhóm câu hỏi (3 câu + 2 câu) đều bị dán nhãn *Hiểu*, trong khi Bảng Ma trận chia rõ `3 Biết + 2 Hiểu`.], [*Reading 2 gồm 5 câu:* 3 câu Nhận biết (chi tiết/từ ngữ trong văn bản) + 2 câu Thông hiểu (ý chính, quy chiếu, loại trừ).],
  [*5*], [Bảng Đặc tả – mục *Grammar* (Dòng 13)], [Có dòng phụ mô tả phân biệt *V-ing, to-inf, bare-inf* với số lượng câu `0 | 0`.], [Kiến thức dạng động từ này được tích hợp trực tiếp vào *4 câu Grammar MCQs* và *5 câu Cloze-text Reading 1*.],
  [*6*], [Bảng Đặc tả – cột TT mục *II/III* & *Writing*], [Mục II (Language) và III (Reading) bị gộp ô dọc chung; mục IV (Writing) bị gõ nhầm TT thành `0` và khuyết nhãn *WRITING*.], [Đề thi thực tế tách rõ *4 phần độc lập: I. Listening – II. Language – III. Reading – IV. Writing*.],
)

= 5. Chiến thuật Phân bổ 60 Phút Làm bài Tối ưu Điểm số

- #strong[Phút 01 – 12 (12 phút) | LISTENING (2,50đ):] Tận dụng 30 giây trước mỗi bài nghe để gạch chân *từ khóa (keywords)*: tên riêng, động từ chính, từ phủ định/lượng từ (*not, never, only, all*) và con số. Tuyệt đối không bỏ trống đáp án khi băng chuyển sang bài tiếp theo.
- #strong[Phút 13 – 20 (08 phút) | LANGUAGE TNKQ + WRITING 1 RE-ORDERING (1,50đ):] Giải nhanh 6 câu từ vựng – ngữ pháp và 2 câu sắp xếp hội thoại/lá thư (dùng quy tắc *câu chào mở đầu → cặp hỏi đáp / từ nối First–Second–Finally → câu kết*).
- #strong[Phút 21 – 36 (16 phút) | READING 1 & READING 2 (2,50đ):] Làm bài Tờ rơi/Quảng cáo (5 phút) trước, sau đó dành 11 phút cho bài Đọc hiểu 220–250 từ (làm câu từ vựng/quy chiếu/chi tiết trước, câu *Main idea* làm cuối cùng).
- #strong[Phút 37 – 44 (08 phút) | TỰ LUẬN NGẮN: VOCABULARY TL & WRITING 2 (2,00đ):] Cực kỳ cẩn trọng ở #strong[2 câu Word Form (0,50đ/câu!)] — kiểm tra kỹ danh từ số ít/số nhiều và chính tả; sau đó viết 4 câu biến đổi câu (kiểm tra chia thì của *to be* trong câu bị động và dấu phẩy trước liên từ câu ghép).
- #strong[Phút 45 – 57 (12 phút) | WRITING 3 – ĐOẠN VĂN 120–150 TỪ (1,00đ):] Lập dàn ý 2 phút (*Topic sentence → 2–3 Supporting ideas + Examples → Concluding sentence*), viết 10 phút (khoảng 12–14 câu đơn/ghép rõ ràng, đếm đủ khoảng 120–150 từ).
- #strong[Phút 58 – 60 (03 phút) | RÀ SOÁT CUỐI GIỜ:] Kiểm tra phiếu tô trắc nghiệm (đủ 28 câu), đuôi *-s/-es/-ed*, mạo từ và chính tả phần tự luận.
