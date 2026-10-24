#import "style.typ": *

#set document(
  title: "Phân tích Ma trận & Đề cương Ôn tập Giữa Học kỳ 1 Tiếng Anh 10 (Global Success) – Năm học 2026–2027",
  author: "Tài liệu Học thuật Tiếng Anh 10 Global Success",
)

#set page(
  paper: "a4",
  margin: (top: 19mm, bottom: 18mm, left: 17mm, right: 17mm),
  header: context {
    if counter(page).get().first() > 1 [
      #set text(size: 8pt, fill: c-muted)
      #grid(
        columns: (1fr, auto),
        [Đề cương Ôn tập Giữa Học kỳ 1 — *Tiếng Anh 10 (Global Success)*],
        [Ma trận & Đặc tả *2026 – 2027*]
      )
      #v(-4pt)
      #line(length: 100%, stroke: 0.45pt + c-border)
    ]
  },
  footer: context {
    if counter(page).get().first() > 1 [
      #line(length: 100%, stroke: 0.45pt + c-border)
      #v(-3pt)
      #set text(size: 8pt, fill: c-muted)
      #grid(
        columns: (1fr, auto),
        [Units 1 – 2 – 3: *Family Life • Humans and the Environment • Music*],
        text(weight: "bold", fill: c-navy)[Trang #counter(page).display("1 / 1", both: true)]
      )
    ]
  }
)

#set text(
  font: ("Be Vietnam Pro", "Noto Sans", "DejaVu Sans"),
  lang: "vi",
  size: 9.5pt,
  fill: c-ink,
)

#set par(
  justify: true,
  leading: 0.58em,
  spacing: 0.80em,
)

// Prevent stretched whitespace inside table cells globally
#show table: set par(justify: false)

#show heading.where(level: 1): it => block(
  breakable: false,
  sticky: true,
  width: 100%,
  above: 12pt,
  below: 6.5pt,
)[
  #set text(fill: c-navy, weight: "extrabold", size: 11.5pt)
  #it
  #v(-4pt)
  #line(length: 100%, stroke: 1.1pt + c-teal)
]

#show heading.where(level: 2): it => block(
  breakable: false,
  sticky: true,
  above: 9.5pt,
  below: 5pt,
)[
  #set text(fill: c-teal.darken(15%), weight: "bold", size: 10.1pt)
  #it
]

#include "part0_cover_toc.typ"
#include "part1_matrix_analysis.typ"
#include "part2a_vocabulary.typ"
#include "part2b_grammar_skills.typ"
#include "part3_practice_drills.typ"
#include "part4_mock_exams.typ"
#include "part5_answer_keys.typ"
