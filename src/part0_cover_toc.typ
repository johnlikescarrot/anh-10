#import "style.typ": *

// ============================================================================
// COVER PAGE & TABLE OF CONTENTS + 7-DAY SMART STUDY PLAN
// ============================================================================

#page(
  margin: (top: 15mm, bottom: 14mm, left: 16mm, right: 16mm),
  header: none,
  footer: none,
)[
  #set par(justify: false, leading: 0.56em)
  // Top hero card
  #block(
    width: 100%,
    fill: c-navy,
    radius: 9pt,
    inset: (x: 22pt, y: 20pt),
  )[
    #grid(
      columns: (1fr, auto),
      align: (left + horizon, right + horizon),
      [#badge("CHƯƠNG TRÌNH GDPT 2018 • SGK GLOBAL SUCCESS", bg: c-teal)],
      [#badge("NĂM HỌC 2026 – 2027", bg: rgb("#D97706"))]
    )
    #v(12pt)
    #text(fill: rgb("#93C5FD"), weight: "bold", size: 11pt, tracking: 1pt)[TÀI LIỆU PHÂN TÍCH MA TRẬN & ĐỀ CƯƠNG ÔN TẬP TRỌNG TÂM]
    #v(6pt)
    #text(fill: white, weight: "extrabold", size: 24pt)[TIẾNG ANH LỚP 10]
    #v(3pt)
    #text(fill: rgb("#FDE68A"), weight: "bold", size: 15.5pt)[KỲ THI GIỮA HỌC KỲ 1 (MID-TERM 1 TEST PREP)]
    #v(10pt)
    #line(length: 100%, stroke: 0.8pt + rgb("#335C81"))
    #v(8pt)
    #set par(justify: true)
    #text(fill: rgb("#E2E8F0"), size: 9.6pt)[
      Biên soạn chuyên biệt theo #strong[Ma trận & Bảng đặc tả kỹ thuật Đề kiểm tra Giữa kỳ 1 năm học 2026–2027]. Tích hợp phân tích chuyên sâu cấu trúc đề, hệ thống sơ đồ – mẹo ghi nhớ nhanh Units 1–3, kho bài tập thực hành phân hóa theo từng dạng câu hỏi và 02 đề thi thử chuẩn 100% ma trận kèm đáp án – giải thích chi tiết.
    ]
  ]

  #v(10pt)

  // 4-Pillar Score Architecture Cards
  #text(fill: c-navy, weight: "bold", size: 10pt)[CẤU TRÚC ĐIỂM SỐ CHUẨN MA TRẬN GIỮA KỲ 1 (2026 – 2027)]
  #v(5pt)
  #grid(
    columns: (1fr, 1fr, 1fr, 1fr),
    column-gutter: 8pt,
    block(fill: c-navy-soft, stroke: 0.8pt + c-border, radius: 6pt, inset: 9pt, width: 100%)[
      #text(fill: c-teal, weight: "extrabold", size: 14.5pt)[25%] #h(3pt) #text(fill: c-muted, size: 8.2pt)[(2,5 điểm)]
      #v(2.5pt)
      #text(fill: c-navy, weight: "bold", size: 9.4pt)[I. LISTENING]
      #v(2pt)
      #text(size: 8.1pt, fill: c-ink)[• Part 1: 5 câu T/F (1,25đ)\ • Part 2: 5 câu MCQs (1,25đ)]
    ],
    block(fill: c-navy-soft, stroke: 0.8pt + c-border, radius: 6pt, inset: 9pt, width: 100%)[
      #text(fill: c-teal, weight: "extrabold", size: 14.5pt)[25%] #h(3pt) #text(fill: c-muted, size: 8.2pt)[(2,5 điểm)]
      #v(2.5pt)
      #text(fill: c-navy, weight: "bold", size: 9.4pt)[II. LANGUAGE]
      #v(2pt)
      #text(size: 8.1pt, fill: c-ink)[• Vocab: 2 TN + 2 TL (1,5đ)\ • Grammar: 4 MCQs (1,0đ)]
    ],
    block(fill: c-navy-soft, stroke: 0.8pt + c-border, radius: 6pt, inset: 9pt, width: 100%)[
      #text(fill: c-teal, weight: "extrabold", size: 14.5pt)[25%] #h(3pt) #text(fill: c-muted, size: 8.2pt)[(2,5 điểm)]
      #v(2.5pt)
      #text(fill: c-navy, weight: "bold", size: 9.4pt)[III. READING]
      #v(2pt)
      #text(size: 8.1pt, fill: c-ink)[• Tờ rơi/QC: 5 câu (1,25đ)\ • Đọc hiểu: 5 câu (1,25đ)]
    ],
    block(fill: c-navy-soft, stroke: 0.8pt + c-border, radius: 6pt, inset: 9pt, width: 100%)[
      #text(fill: c-teal, weight: "extrabold", size: 14.5pt)[25%] #h(3pt) #text(fill: c-muted, size: 8.2pt)[(2,5 điểm)]
      #v(2.5pt)
      #text(fill: c-navy, weight: "bold", size: 9.4pt)[IV. WRITING]
      #v(2pt)
      #text(size: 8.1pt, fill: c-ink)[• Sắp xếp: 2 TN (0,5đ)\ • Viết câu (1đ) + Đoạn (1đ)]
    ],
  )

  #v(10pt)

  // 3 Core Units Scope
  #text(fill: c-navy, weight: "bold", size: 10pt)[PHẠM VI KIẾN THỨC TRỌNG TÂM — GLOBAL SUCCESS 10]
  #v(5pt)
  #grid(
    columns: (1fr, 1fr, 1fr),
    column-gutter: 9pt,
    block(fill: c-teal-soft, stroke: (top: 3pt + c-teal, bottom: 0.6pt + c-border, left: 0.6pt + c-border, right: 0.6pt + c-border), radius: 5pt, inset: 9pt, width: 100%)[
      #badge("UNIT 1", bg: c-teal) #h(4pt) #text(weight: "bold", fill: c-navy, size: 9.3pt)[FAMILY LIFE]
      #v(4pt)
      #text(size: 8.2pt, fill: c-ink)[
        • #strong[Chủ điểm:] Chia sẻ việc nhà (#emph[household chores]), vai trò trụ cột & gắn kết gia đình.\
        • #strong[Ngữ pháp:] Hiện tại đơn vs. Hiện tại tiếp diễn & Động từ trạng thái (#emph[Stative verbs]).\
        • #strong[Viết:] Lợi ích làm việc nhà / Sinh hoạt gia đình.
      ]
    ],
    block(fill: c-teal-soft, stroke: (top: 3pt + c-teal, bottom: 0.6pt + c-border, left: 0.6pt + c-border, right: 0.6pt + c-border), radius: 5pt, inset: 9pt, width: 100%)[
      #badge("UNIT 2", bg: c-teal) #h(4pt) #text(weight: "bold", fill: c-navy, size: 9.3pt)[HUMANS & ENV.]
      #v(4pt)
      #text(size: 8.2pt, fill: c-ink)[
        • #strong[Chủ điểm:] Lối sống xanh (#emph[green lifestyle]), giảm dấu chân carbon, bảo vệ môi trường.\
        • #strong[Ngữ pháp:] Tương lai với #emph[will] vs. #emph[be going to]; Câu bị động (#emph[Passive Voice]).\
        • #strong[Viết:] Giải pháp cải thiện môi trường & sống xanh.
      ]
    ],
    block(fill: c-teal-soft, stroke: (top: 3pt + c-teal, bottom: 0.6pt + c-border, left: 0.6pt + c-border, right: 0.6pt + c-border), radius: 5pt, inset: 9pt, width: 100%)[
      #badge("UNIT 3", bg: c-teal) #h(4pt) #text(weight: "bold", fill: c-navy, size: 9.3pt)[MUSIC]
      #v(4pt)
      #text(size: 8.2pt, fill: c-ink)[
        • #strong[Chủ điểm:] Chương trình âm nhạc thực tế, biểu diễn trực tiếp, nhạc truyền thống.\
        • #strong[Ngữ pháp:] Câu ghép (#emph[Compound sentences] – FANBOYS); #emph[To-V] vs. #emph[Bare-V].\
        • #strong[Viết:] Trải nghiệm sự kiện âm nhạc yêu thích.
      ]
    ],
  )

  #v(10pt)

  // Key Highlights Box
  #block(
    width: 100%,
    fill: c-gold-soft,
    stroke: (left: 4pt + c-gold, top: 0.5pt + rgb("#FCD34D"), right: 0.5pt + rgb("#FCD34D"), bottom: 0.5pt + rgb("#FCD34D")),
    radius: 5pt,
    inset: (x: 13pt, y: 9.5pt),
  )[
    #text(weight: "bold", fill: c-gold.darken(15%), size: 9.6pt)[ĐIỂM NỔI BẬT CỦA BỘ ĐỀ CƯƠNG NÀY]
    #v(4pt)
    #grid(
      columns: (1fr, 1fr),
      column-gutter: 12pt,
      row-gutter: 4.5pt,
      text(size: 8.4pt)[#strong[1. Giải mã chi tiết Ma trận 2026–2027:] Chỉ rõ tỉ trọng thật (28 câu TN = 7,0đ; 6 câu + 1 đoạn văn TL = 3,0đ) và đối chiếu 6 điểm kỹ thuật trong tệp gốc.],
      text(size: 8.4pt)[#strong[2. Công thức "Siêu Trí Nhớ":] Hệ thống hóa bằng bảng so sánh đối xứng, từ khóa viết tắt (FANBOYS, QĐ–DĐ–MĐ, KHUYẾT–KHIẾN–ĐỂ–GIÁC) và cảnh báo bẫy hay sai.],
      text(size: 8.4pt)[#strong[3. Trọng tâm định dạng mới:] Hướng dẫn giải nhanh Đọc điền Tờ rơi/Quảng cáo (Reading 1), Sắp xếp hội thoại/lá thư (Writing 1) và Tự luận Từ loại (0,5đ/câu!).],
      text(size: 8.4pt)[#strong[4. Kho 174 câu hỏi & 02 Đề chuẩn 100%:] Gồm 104 câu luyện chuyên đề + 02 đề thi thử đầy đủ Tapescript (180–200 từ), bài viết mẫu (120–150 từ) & giải thích chi tiết.]
    )
  ]

  #v(1fr)
  #line(length: 100%, stroke: 0.6pt + c-border)
  #v(3pt)
  #grid(
    columns: (1fr, auto),
    text(size: 8.2pt, fill: c-muted)[Tài liệu học thuật & ôn luyện Kỳ thi Giữa Học kỳ 1 — Tiếng Anh 10 (#emph[Global Success])],
    text(size: 8.2pt, fill: c-navy, weight: "bold")[Năm học 2026 – 2027]
  )
]

// ============================================================================
// PAGE 2: TABLE OF CONTENTS & 7-DAY STUDY ROADMAP
// ============================================================================
#block(
  width: 100%,
  fill: c-navy,
  radius: 5pt,
  inset: (x: 14pt, y: 9pt),
  below: 8pt,
)[
  #text(fill: white, weight: "extrabold", size: 12.2pt)[MỤC LỤC TRA CỨU NHANH & LỘ TRÌNH ÔN TẬP 7 NGÀY]
]

#block(
  width: 100%,
  stroke: 0.6pt + c-border,
  radius: 5pt,
  inset: (x: 12pt, y: 8pt),
  fill: white,
)[
  #set par(leading: 0.42em)
  #show outline.entry.where(level: 1): it => {
    let body-txt = repr(it.element.body)
    if body-txt.contains("PHẦN ") {
      v(4.5pt, weak: true)
      strong(text(fill: c-teal.darken(15%), size: 9.2pt)[#it])
    } else {
      text(fill: c-ink, size: 8.5pt)[#h(8pt)#it]
    }
  }
  #outline(
    title: none,
    indent: 10pt,
    depth: 1,
  )
]

#v(7pt)

#callout(title: "Lộ trình ôn tập thông minh 7 ngày trước kỳ thi (Spaced Repetition)", kind: "mnemonic", breakable-box: false)[
  #table(
    columns: (auto, 1.35fr, 1.75fr, auto),
    inset: (x: 6pt, y: 4.5pt),
    align: (center + horizon, left + horizon, left + horizon, center + horizon),
    stroke: 0.45pt + c-border,
    fill: (_, row) => if row == 0 { c-navy } else if calc.odd(row) { white } else { c-zebra },
    text(fill: white, weight: "bold", size: 8.2pt)[Ngày],
    text(fill: white, weight: "bold", size: 8.2pt)[Trọng tâm kiến thức],
    text(fill: white, weight: "bold", size: 8.2pt)[Bài tập thực hành tương ứng],
    text(fill: white, weight: "bold", size: 8.2pt)[Mục tiêu điểm],

    [*Ngày 1*], [Đọc kỹ *Phần I* + Từ vựng/Word Form *Unit 1* + *Present Simple vs. Continuous*], [Làm câu 1–5 (Drill 1, 2, 3) + ghi nhớ bảng Stative Verbs], [Nắm cấu trúc & +1,5đ],
    [*Ngày 2*], [Từ vựng/Word Form *Unit 2* + *Will vs. Be going to* + *Passive Voice*], [Làm câu 6–10 (Drill 1, 2) & câu 6–15 (Drill 3)], [Làm chủ Bị động (+1,5đ)],
    [*Ngày 3*], [Từ vựng/Word Form *Unit 3* + *Compound Sentences* + *To-V / Bare-V*], [Làm câu 11–15 (Drill 1, 2) & câu 16–25 (Drill 3)], [Trọn vẹn 2,5đ Language],
    [*Ngày 4*], [Chiến thuật giải *Cloze-text Tờ rơi/Quảng cáo* & *Reading 220–250 từ*], [Hoàn thành *Drill 4* (15 câu) & *Drill 5* (10 câu)], [Trọn vẹn 2,5đ Reading],
    [*Ngày 5*], [Mẹo giải 20s *Re-ordering* + 6 công thức *Viết lại câu* + Dàn ý *Đoạn văn*], [Hoàn thành *Drill 6* (8 câu) & *Drill 7* (16 câu) + lập dàn ý], [Trọn vẹn 2,5đ Writing],
    [*Ngày 6*], [Luyện *Đề thi thử số 01* bấm giờ 60 phút (kèm tự luyện Tapescript)], [Đối chiếu đáp án Phần V, ghi sổ tay các câu sai], [Đạt mốc 8,0 – 9,0 điểm],
    [*Ngày 7*], [Luyện *Đề thi thử số 02* bấm giờ 60 phút + Ôn nhanh các hộp *Bẫy đề thi*], [Rà lại bảng Word Form 3 Unit & 5 bài viết mẫu], [Chinh phục 9,0 – 10,0đ!],
  )
]
