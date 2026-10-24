// ============================================================================
// STYLE & DESIGN SYSTEM — TIẾNG ANH 10 GLOBAL SUCCESS (GK1 2026–2027)
// ============================================================================

#let c-navy        = rgb("#0F2B46")
#let c-navy-soft   = rgb("#EBF1F6")
#let c-teal        = rgb("#0D7377")
#let c-teal-soft   = rgb("#E6F4F4")
#let c-gold        = rgb("#B45309")
#let c-gold-soft   = rgb("#FEF3C7")
#let c-red         = rgb("#B91C1C")
#let c-red-soft    = rgb("#FEE2E2")
#let c-green       = rgb("#15803D")
#let c-green-soft  = rgb("#DCFCE7")
#let c-ink         = rgb("#1E293B")
#let c-muted       = rgb("#64748B")
#let c-border      = rgb("#CBD5E1")
#let c-zebra       = rgb("#F8FAFC")

// Crisp exam fill-in-the-blank rules
#let blank = box(width: 34pt, height: 8pt, stroke: (bottom: 0.75pt + c-ink))
#let wblank = box(width: 72pt, height: 8pt, stroke: (bottom: 0.8pt + c-navy))
#let cblank(n) = [#strong[(#n)]#box(width: 30pt, height: 8pt, stroke: (bottom: 0.75pt + c-navy))]
#let tline = box(width: 1fr, height: 8pt, stroke: (bottom: 0.6pt + c-muted))

// Reusable inline pill badge
#let badge(label, bg: c-navy, fg: white) = box(
  fill: bg,
  inset: (x: 6pt, y: 2.5pt),
  outset: (y: 1pt),
  radius: 3pt,
  text(fill: fg, weight: "bold", size: 8pt, tracking: 0.2pt)[#label]
)

// Major Part Banner (also registers a top-level bookmark/outline entry)
#let part-banner(num, title, subtitle) = {
  pagebreak(weak: true)
  block(
    width: 100%,
    fill: c-navy,
    radius: 6pt,
    inset: (x: 16pt, y: 13pt),
    breakable: false,
    above: 0pt,
    below: 12pt,
  )[
    // Hidden outline anchor for PDF bookmarks & TOC
    #place(hide(heading(level: 1, outlined: true, bookmarked: true)[#num: #title]))
    #grid(
      columns: (auto, 1fr),
      column-gutter: 12pt,
      align: (left + horizon, left + horizon),
      box(
        fill: c-teal,
        radius: 4pt,
        inset: (x: 10pt, y: 6pt),
        text(fill: white, weight: "extrabold", size: 11pt)[#num]
      ),
      stack(
        spacing: 5pt,
        text(fill: white, weight: "extrabold", size: 14pt)[#title],
        text(fill: rgb("#CBD5E1"), size: 9pt, style: "italic")[#subtitle],
      )
    )
  ]
}

// Section Sub-banner (Unit / Topic Header)
#let unit-header(tag, title, summary) = block(
  width: 100%,
  fill: c-teal-soft,
  stroke: (left: 4pt + c-teal, top: 0.5pt + rgb("#99D5D7"), right: 0.5pt + rgb("#99D5D7"), bottom: 0.5pt + rgb("#99D5D7")),
  radius: (right: 5pt),
  inset: (x: 12pt, y: 8.5pt),
  breakable: false,
  above: 12pt,
  below: 9pt,
)[
  #stack(
    spacing: 4pt,
    [#badge(tag, bg: c-teal) #h(6pt) #text(fill: c-navy, weight: "bold", size: 11.5pt)[#title]],
    text(fill: c-ink, size: 8.9pt)[#summary]
  )
]

// Callout box (General / Formula / Tip / Trap)
#let callout(title: none, kind: "info", breakable-box: true, body) = {
  let (accent, bg, icon) = if kind == "mnemonic" {
    (c-gold, c-gold-soft, "MẸO NHỚ SIÊU TỐC")
  } else if kind == "trap" {
    (c-red, c-red-soft, "BẪY ĐỀ THI CẦN TRÁNH")
  } else if kind == "formula" {
    (c-teal, c-teal-soft, "CÔNG THỨC TRỌNG TÂM")
  } else if kind == "answer" {
    (c-green, c-green-soft, "CHECKLIST VỀ ĐÍCH")
  } else {
    (c-navy, c-navy-soft, "GHI NHỚ")
  }
  block(
    width: 100%,
    fill: bg,
    stroke: (left: 3.5pt + accent, top: 0.4pt + accent.lighten(55%), right: 0.4pt + accent.lighten(55%), bottom: 0.4pt + accent.lighten(55%)),
    radius: (right: 4pt),
    inset: (x: 11pt, y: 8pt),
    breakable: breakable-box,
    above: 7.5pt,
    below: 8pt,
  )[
    #if title != none [
      #block(breakable: false, below: 4.5pt)[
        #badge(icon, bg: accent) #h(5pt) #text(weight: "bold", fill: accent.darken(15%), size: 9.6pt)[#title]
      ]
    ]
    #set text(size: 9.2pt, fill: c-ink)
    #body
  ]
}

// True / False item helper
#let tf-item(num, stem) = block(breakable: false, width: 100%, above: 4.8pt, below: 4.8pt)[
  #grid(
    columns: (1fr, auto),
    column-gutter: 12pt,
    align: (left + top, right + top),
    [#text(weight: "bold", fill: c-navy)[Question #num.] #stem],
    [#box(inset: (x: 6pt, y: 2pt), radius: 3pt, stroke: 0.45pt + c-border, fill: c-zebra)[*A.* True #h(8pt) *B.* False]]
  )
]

// Multiple-choice helpers (non-breaking question + neatly aligned options)
#let mcq4(num, stem, a, b, c, d) = block(breakable: false, width: 100%, above: 5.5pt, below: 5.5pt)[
  #set par(justify: false)
  #if stem != [] [
    #text(weight: "bold", fill: c-navy)[Question #num.] #stem
    #v(2pt)
    #grid(
      columns: (1fr, 1fr, 1fr, 1fr),
      column-gutter: 8pt,
      [*A.* #a], [*B.* #b], [*C.* #c], [*D.* #d]
    )
  ] else [
    #grid(
      columns: (auto, 1fr, 1fr, 1fr, 1fr),
      column-gutter: 8pt,
      [#text(weight: "bold", fill: c-navy)[Question #num.]],
      [*A.* #a], [*B.* #b], [*C.* #c], [*D.* #d]
    )
  ]
]

#let mcq2(num, stem, a, b, c, d) = block(breakable: false, width: 100%, above: 5.5pt, below: 5.5pt)[
  #set par(justify: false)
  #text(weight: "bold", fill: c-navy)[Question #num.] #stem
  #v(2pt)
  #grid(
    columns: (1fr, 1fr),
    column-gutter: 12pt,
    row-gutter: 3.5pt,
    [*A.* #a], [*B.* #b],
    [*C.* #c], [*D.* #d]
  )
]

#let mcq1(num, stem, a, b, c, d) = block(breakable: false, width: 100%, above: 5.5pt, below: 5.5pt)[
  #set par(justify: false)
  #text(weight: "bold", fill: c-navy)[Question #num.] #stem
  #v(2pt)
  #stack(
    spacing: 3pt,
    [*A.* #a],
    [*B.* #b],
    [*C.* #c],
    [*D.* #d],
  )
]

// Reading / Cloze / Model passage box (breakable: false keeps short passages intact!)
#let passage-box(title: none, keep-together: true, body) = block(
  width: 100%,
  fill: rgb("#F8FAFC"),
  stroke: 0.7pt + c-border,
  radius: 5pt,
  inset: (x: 12pt, y: 9pt),
  breakable: not keep-together,
  above: 7pt,
  below: 7pt,
)[
  #if title != none [
    #align(center)[#text(weight: "bold", size: 10pt, fill: c-navy)[#title]]
    #v(3.5pt)
  ]
  #set par(justify: true, leading: 0.58em)
  #body
]
