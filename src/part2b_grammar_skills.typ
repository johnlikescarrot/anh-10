#import "style.typ": *

// ============================================================================
// PART II-B & II-C: 05 CORE GRAMMAR TOPICS & SKILL STRATEGIES + MODEL WRITINGS
// ============================================================================

= B. 05 Chuyên đề Ngữ pháp Trọng tâm (Bám sát 100% Bảng Đặc tả Units 1–2–3)

== Chuyên đề 1 (Unit 1): Present Simple vs. Present Continuous (HTĐ & HTTD)

#table(
  columns: (1.1fr, 1.9fr, 1.9fr),
  inset: (x: 6pt, y: 5pt),
  stroke: 0.45pt + c-border,
  fill: (_, row) => if row == 0 { c-navy } else if calc.odd(row) { white } else { c-zebra },
  text(fill: white, weight: "bold", size: 8.8pt)[Tiêu chí],
  text(fill: white, weight: "bold", size: 8.8pt)[Present Simple (Hiện tại đơn)],
  text(fill: white, weight: "bold", size: 8.8pt)[Present Continuous (Hiện tại tiếp diễn)],

  [*Công thức*], [• (+) S + *V(s/es)* | (–) S + *don't/doesn't + V0*\ • (?) *Do/Does* + S + V0? *(be: am/is/are)*], [• (+) S + *am/is/are + V-ing*\ • (–) S + *am/is/are + not + V-ing*],
  [*Cách dùng cốt lõi*], [1. Thói quen, sinh hoạt lặp lại (*daily routines*).\ 2. Sự thật hiển nhiên, chân lý.\ 3. Lịch trình cố định (tàu xe, giờ mở cửa).], [1. Hành động đang diễn ra ngay lúc nói.\ 2. Hành động tạm thời quanh thời điểm nói (*today, this week*).\ 3. Phàn nàn với *always* (*He is always leaving dirty dishes!*).],
  [*Dấu hiệu nhận biết*], [*always, usually, often, sometimes, rarely, never, every day/week, once/twice a week, on Sundays*.], [*now, right now, at the moment, at present, today, this week*, hoặc sau câu mệnh lệnh: *Look!, Listen!, Keep silent!, Watch out!*],
)

#callout(title: "Động từ chỉ trạng thái (Stative Verbs) KHÔNG chia tiếp diễn (-ing)!", kind: "trap")[
  - *Nhóm nhận thức – tình cảm – sở hữu:* *know, believe, understand, remember, forget, want, need, like, love, hate, prefer, seem, appear, belong (to), own*. → Luôn chia #strong[Hiện tại đơn] dù trong câu có *now / at the moment*!
  - *4 Động từ "Hai Mặt" cực hay ra câu phân loại:*
    1. #strong[have]: *có/sở hữu* → HTĐ (*She has two brothers*) ≠ *ăn/tắm/trải nghiệm* → HTTD (*We are having dinner right now*).
    2. #strong[think]: *cho rằng, nghĩ rằng* → HTĐ (*I think housework is useful*) ≠ *đang suy tính/cân nhắc* → HTTD (*I am thinking about joining the Go Green Club*).
    3. #strong[see]: *nhìn thấy / hiểu* → HTĐ ≠ *gặp gỡ/hẹn gặp* → HTTD (*I am seeing the dentist this afternoon*).
    4. #strong[look / smell / taste]: *trông có vẻ / có mùi / có vị* → HTĐ (*The soup tastes great*) ≠ *nhìn / ngửi / nếm (hành động chủ ý)* → HTTD (*Mom is tasting the soup*).
]

== Chuyên đề 2 (Unit 2): Tương lai với WILL vs. BE GOING TO

#callout(title: "Quy tắc đối xứng 3 cặp 'QĐ – DĐ – MĐ' giúp phân biệt trong 3 giây", kind: "mnemonic")[
  #table(
    columns: (1.15fr, 1.9fr, 1.9fr),
    inset: (x: 6pt, y: 4.8pt),
    stroke: 0.45pt + c-border,
    fill: (_, row) => if row == 0 { c-teal } else if calc.odd(row) { white } else { c-zebra },
    text(fill: white, weight: "bold", size: 8.6pt)[Tình huống],
    text(fill: white, weight: "bold", size: 8.6pt)[WILL + V0 (Tương lai đơn)],
    text(fill: white, weight: "bold", size: 8.6pt)[AM/IS/ARE + GOING TO + V0],

    [*1. Quyết định (QĐ)*], [*Quyết định tức thời ngay lúc nói* (chưa tính trước).\ VD: *"The phone is ringing." – "I'll answer it!"*], [*Kế hoạch, dự định đã có từ trước lúc nói*.\ VD: *We have bought the saplings. We are going to plant them tomorrow.*],
    [*2. Dự đoán (DĐ)*], [*Dự đoán chủ quan* (dựa vào quan điểm cá nhân), thường đi kèm: *I think, I believe, I'm sure, probably, perhaps, maybe, hope, expect*.], [*Dự đoán có căn cứ/dấu hiệu rõ ràng trước mắt*.\ VD: *Look at those black clouds! It is going to rain heavily.*],
    [*3. Mục đích khác*], [Lời hứa (*promise*), lời đề nghị giúp đỡ (*offer*), yêu cầu lịch sự (*Will you...?*), sự thật tương lai.], [Ý định cá nhân rõ ràng cho tương lai gần.],
  )
]

== Chuyên đề 3 (Unit 2): Passive Voice (Câu bị động – Cực trọng tâm cả MCQs & Viết lại câu!)

- *Công thức vàng chung cho mọi thì:* Chủ động `S + V + O` ⇒ Bị động: #strong[`S(mới = O) + BE (chia theo thì của V) + V3/ed + (Nơi chốn) + (by O) + (Thời gian)`].

#set text(size: 8.6pt)
#table(
  columns: (1.25fr, 1.55fr, 1.75fr, 1.9fr),
  inset: (x: 5pt, y: 4.5pt),
  stroke: 0.45pt + c-border,
  fill: (_, row) => if row == 0 { c-navy } else if calc.odd(row) { white } else { c-zebra },
  text(fill: white, weight: "bold")[Thì / Cấu trúc],
  text(fill: white, weight: "bold")[Chủ động (Active)],
  text(fill: white, weight: "bold")[Bị động (Passive)],
  text(fill: white, weight: "bold")[Ví dụ chuẩn Global Success],

  [*Hiện tại đơn*], [S + V(s/es) + O], [S + *am/is/are + V3/ed*], [*Rubbish is collected every morning.*],
  [*Hiện tại tiếp diễn*], [S + am/is/are + V-ing + O], [S + *am/is/are + being + V3/ed*], [*More trees are being planted in our school.*],
  [*Quá khứ đơn*], [S + V2/ed + O], [S + *was/were + V3/ed*], [*The Youth Club was set up in 2022.*],
  [*Hiện tại hoàn thành*], [S + have/has + V3/ed + O], [S + *have/has + been + V3/ed*], [*Plastic bags have been banned here.*],
  [*Tương lai (will)*], [S + will + V0 + O], [S + *will + be + V3/ed*], [*Clean energy will be used more widely.*],
  [*Dự định (going to)*], [S + am/is/are going to + V0 + O], [S + *am/is/are going to + be + V3/ed*], [*A music show is going to be held next Sunday.*],
  [*Modal verbs*], [S + can/should/must + V0 + O], [S + *can/should/must + be + V3/ed*], [*Appliances should be turned off when not in use.*],
)
#set text(size: 9.8pt)

#callout(title: "3 Quy tắc sống còn khi viết lại câu Bị động (Writing 2 – Tự luận)", kind: "trap")[
  1. *Thứ tự trạng ngữ cuối câu:* Luôn đặt #strong[`[Nơi chốn] + [by + Tân ngữ] + [Thời gian]`]! *(VD: The stage was decorated #strong[in the schoolyard by the students yesterday]).*
  2. *Lược bỏ `by + O`:* Bắt buộc bỏ *by people, by someone, by somebody, by them, by us, by anyone* (chủ ngữ mơ hồ). Nếu chủ ngữ là *nobody / no one*, phải đổi động từ bị động sang thể #strong[phủ định]! (*Nobody cleaned the room → The room #strong[wasn't cleaned].*)
  3. *Nội động từ KHÔNG có bị động:* *happen, take place, occur, arrive, die, appear, disappear* tuyệt đối không chia `be + V3/ed`!
]

== Chuyên đề 4 (Unit 3): Compound Sentences (Câu ghép với bộ liên từ FANBOYS)

- *Cấu trúc chuẩn:* #strong[`Mệnh đề độc lập 1 (S1 + V1), + Liên từ FANBOYS + Mệnh đề độc lập 2 (S2 + V2).`] *(Luôn có #strong[dấu phẩy] trước liên từ kết hợp khi nối 2 mệnh đề độc lập đủ S–V!)*

#set text(size: 8.6pt)
#table(
  columns: (auto, auto, 1.35fr, 2.5fr),
  inset: (x: 5.5pt, y: 4.2pt),
  align: (center + horizon, center + horizon, left + horizon, left + horizon),
  stroke: 0.45pt + c-border,
  fill: (_, row) => if row == 0 { c-teal } else if calc.odd(row) { white } else { c-zebra },
  text(fill: white, weight: "bold")[Chữ cái],
  text(fill: white, weight: "bold")[Liên từ],
  text(fill: white, weight: "bold")[Ý nghĩa quan hệ],
  text(fill: white, weight: "bold")[Ví dụ & Lưu ý bẫy đề thi],

  [*F*], [*for*], [vì, bởi vì *(chỉ nguyên nhân – trang trọng)*], [*He practiced every night, #strong[for] he wanted to win the contest.* (Đứng giữa câu, sau dấu phẩy)],
  [*A*], [*and*], [và *(bổ sung thông tin cùng chiều)*], [*She writes her own songs, #strong[and] she plays the guitar brilliantly.*],
  [*N*], [*nor*], [cũng không *(nối 2 vế phủ định → ĐẢO NGỮ!)*], [*He cannot sing well, #strong[nor can he] play the piano.* (#strong[Chú ý:] `nor + trợ ĐT + S + V`)],
  [*B*], [*but*], [nhưng *(đối lập thông thường)*], [*The concert tickets were expensive, #strong[but] they sold out within minutes.*],
  [*O*], [*or*], [hoặc là / nếu không thì *(lựa chọn / cảnh báo)*], [*You should book early, #strong[or] you won't get a front-row seat.*],
  [*Y*], [*yet*], [thế nhưng *(đối lập gây bất ngờ = but)*], [*She was only fifteen, #strong[yet] her voice moved all the judges to tears.*],
  [*S*], [*so*], [vì vậy, cho nên *(chỉ kết quả)*], [*It rained heavily, #strong[so] the outdoor music festival was postponed.* (#strong[Cấm] dùng *Although/Because* cùng với *but/so* trong 1 câu!)],
)
#set text(size: 9.8pt)

== Chuyên đề 5 (Unit 3): To-infinitive (To V) vs. Bare Infinitive (V0)

#grid(
  columns: (1fr, 1fr),
  column-gutter: 10pt,
  block(fill: c-navy-soft, stroke: 0.6pt + c-border, radius: 5pt, inset: 9pt, width: 100%)[
    #badge("NHÓM 1: TO-INFINITIVE (TO + V0)", bg: c-navy)
    #v(4pt)
    #set text(size: 8.6pt)
    1. *Sau các động từ chỉ ý định / mong muốn / cam kết:*\
       *decide, plan, intend, want, would like, hope, expect, promise, agree, refuse, offer, manage, afford, learn, tend, fail, seem, pretend, arrange + to V*.
    2. *Sau cấu trúc `V + Tân ngữ + to V`:*\
       *allow, permit, advise, encourage, ask, tell, want, expect, remind, invite, persuade, force, teach + O + to V*.
    3. *Sau tính từ & từ để hỏi:*\
       *It is + adj + (for sb) + to V*; *happy/glad/lucky/ready + to V*; *know/decide + how/what/where + to V*.
    4. *Chỉ mục đích:* *in order to V / so as to V / to V* (để làm gì).
  ],
  block(fill: c-gold-soft, stroke: 0.6pt + rgb("#FCD34D"), radius: 5pt, inset: 9pt, width: 100%)[
    #badge("NHÓM 2: BARE INFINITIVE (V0 KHÔNG TO)", bg: c-gold)
    #v(4pt)
    #set text(size: 8.6pt)
    *Mẹo nhớ 4 chữ vàng: "KHUYẾT – KHIẾN – ĐỂ – GIÁC"*
    1. *Động từ KHUYẾT thiếu & cụm tương đương:*\
       *can, could, will, would, shall, should, may, might, must + V0*; *had better + V0* (nên); *would rather + V0 (than V0)* (thích... hơn).
    2. *Động từ sai KHIẾN & ĐỂ cho:*\
       #strong[make + O + V0] (bắt/làm ai đó làm gì)\
       #strong[let + O + V0] (để/cho phép ai làm gì)\
       #strong[help + O + V0 / to V] (cả hai đều đúng!).
    3. *Động từ tri GIÁC (chứng kiến toàn bộ hành động):*\
       *see, hear, watch, notice, feel + O + #strong[V0]* *(chứng kiến từ đầu đến cuối)* ≠ #strong[V-ing] *(chứng kiến một phần đang diễn ra)*.
  ]
)

#callout(title: "Bẫy kinh điển số 1 của Unit 3: Chủ động MAKE + O + V0 nhưng Bị động BE MADE + TO V!", kind: "trap")[
  - Chủ động: *My parents #strong[make] me #strong[do] the washing-up.* ⇒ Bị động: *I #strong[am made TO DO] the washing-up by my parents.*
  - Chủ động: *Her parents #strong[don't let] her #strong[stay] out late.* ⇒ Bị động: *She #strong[is not allowed TO STAY] out late.* *(Không bao giờ viết `be let V0` trong văn viết chuẩn phổ thông; hãy đổi sang `be allowed to V`!)*
]

= C. Chiến thuật Làm các Dạng bài Đặc thù trong Ma trận 2026–2027

== 1. Chiến thuật Nghe (Listening: 5 câu True/False + 5 câu MCQs = 2,50 điểm)
- *Quy tắc Paraphrase:* Đáp án đúng hiếm khi lặp nguyên văn từ trong băng mà dùng từ đồng nghĩa: *split chores equally* ↔ *share housework fairly*; *cut down on* ↔ *reduce*; *debut album* ↔ *first album*.
- *Bẫy True/False kinh điển:* Cảnh giác cao độ với các từ tuyệt đối (#strong[all, every, never, only, nobody, completely]) và bẫy sửa thông tin ở câu sau (*"At first we planned to meet at 7 p.m., #strong[but actually] we moved it to 7:30 p.m."*).

== 2. Chiến thuật Đọc điền Tờ rơi / Quảng cáo (Reading 1: 5 câu = 1,25 điểm)
5 chỗ trống của một tờ rơi/quảng cáo gần như luôn xoay quanh #strong[5 mảnh ghép cố định]: (1) *Từ loại (Word form)* đứng trước/sau danh từ; (2) *Giới từ* (*take part #strong[in], aware #strong[of], on Sunday, at 7 p.m.*); (3) *Dạng động từ (To-V / V0 / V-ing / Rút gọn mệnh đề)*; (4) *Cụm động từ / Collocation chủ đề*; (5) *Lượng từ / Mạo từ / Liên từ* (*many, much, another, other, a/an/the, and/but/so*).

== 3. Mẹo Giải nhanh 20 Giây Bài Sắp xếp Câu – Re-ordering (Writing 1: 2 câu = 0,50 điểm)
- *Dạng 1 – Hội thoại (3–5 lượt lời):* Tìm câu chào/mở lời hoặc câu đặt vấn đề trước (thường có tên người nghe hoặc câu hỏi mở: *"Hi Nam,...", "Excuse me,..."*), sau đó ghép cặp #strong[Hỏi → Đáp] dựa trên đại từ và từ khóa lặp lại.
- *Dạng 2 – Bức thư (Letter/Email):* Ngay sau *Dear...,* câu đầu tiên luôn là lý do viết thư / hỏi thăm (*"How are you? I'm writing to tell you about..."*); ở giữa là chuỗi sự kiện/gợi ý; câu cuối luôn là lời chúc/mong hồi âm (*"Write back soon", "Let me know what you think"*).
- *Dạng 3 – Đoạn văn (Paragraph):* Câu mở đoạn luôn mang tính khái quát (không bắt đầu bằng *First, Second, Also, However, Finally, They, This*). Sau đó nối theo chuỗi: #strong[Topic sentence → First / Firstly → Second / Moreover / In addition → Finally / In conclusion].

== 4. 06 Công thức Viết lại Câu Đồng nghĩa Bắt buộc Thuộc lòng (Writing 2: 4 câu = 1,00 điểm)

#set text(size: 8.8pt)
#table(
  columns: (auto, 1.9fr, 2.2fr),
  inset: (x: 6pt, y: 4.8pt),
  stroke: 0.45pt + c-border,
  fill: (_, row) => if row == 0 { c-navy } else if calc.odd(row) { white } else { c-zebra },
  text(fill: white, weight: "bold")[Dạng],
  text(fill: white, weight: "bold")[Câu gốc đề bài cho],
  text(fill: white, weight: "bold")[Công thức viết lại đồng nghĩa ăn trọn điểm],

  [*1*], [*Chủ động → Bị động* (6 thì + Modal verbs)], [`O + be (chia thì) + V3/ed + (nơi chốn) + (by S) + (thời gian).`],
  [*2*], [*Ghép 2 câu đơn / Câu có Because, Although*], [`S1 + V1, + so / for / but / yet / and / or + S2 + V2.` *(Nhớ dấu phẩy + bỏ Because/Although!)*],
  [*3*], [*allow / permit + O + to V* ↔ *let + O + V0*], [`My parents let me go...` ↔ `My parents allow me to go...` ↔ `I am allowed to go...`],
  [*4*], [*force + O + to V* ↔ *make + O + V0*], [`Mom made him clean...` ↔ `He was made to clean...` ↔ `Mom forced him to clean...`],
  [*5*], [*plan / intend / decide + to V* ↔ *be going to V*], [`We plan to organize a clean-up.` ↔ `We are going to organize a clean-up.`],
  [*6*], [*spend + time + V-ing* ↔ *It takes + (O) + time + to V*], [`She spends 30 minutes cooking.` ↔ `It takes her 30 minutes to cook.`],
)
#set text(size: 9.8pt)

== 5. Dàn ý Chuẩn & 03 Bài viết Mẫu Đạt Điểm Tuyệt đối 120–150 từ (Writing 3: 1,00 điểm)

- *Khung Dàn ý Vạn năng 4 phần (120–150 từ ≈ 9–11 câu):*
  1. #strong[Mở đoạn (1–2 câu):] Giới thiệu trực tiếp chủ đề & nêu rõ quan điểm cá nhân (*In my opinion, [Chủ đề] plays a vital role in... for several convincing reasons.*).
  2. #strong[Luận điểm 1 + Ví dụ (2–3 câu):] *First and foremost, ... For example, ...*
  3. #strong[Luận điểm 2 + Luận điểm 3 (3–4 câu):] *Second, ... Moreover / Finally, ...*
  4. #strong[Kết đoạn (1–2 câu):] Khẳng định lại thông điệp (*In conclusion, ... Therefore, everyone should...*).

#passage-box(title: "BÀI MẪU SỐ 1 (UNIT 1 – FAMILY LIFE): Should children share household chores? (131 words)")[
  In my opinion, sharing household chores brings many valuable benefits to children and prepares them well for adulthood. First and foremost, doing housework helps young people develop essential life skills. When teenagers learn to cook simple meals, do the laundry, and clean their rooms, they can take care of themselves independently in the future. Second, dividing chores equally teaches children to take responsibility. They realize that every family member must contribute to keeping a warm home, even when they do not enjoy certain tasks. Finally, working together strengthens family bonds and builds gratitude. Sharing daily duties gives parents more time to relax, and children appreciate their parents' hard work much more. In conclusion, doing household chores builds strong character, so parents should encourage their children to help at home every day.
]

#passage-box(title: "BÀI MẪU SỐ 2 (UNIT 2 – HUMANS & THE ENVIRONMENT): Ways to live a greener lifestyle (132 words)")[
  Adopting a green lifestyle is one of the most practical ways for students to protect the environment and reduce their carbon footprint. First, we should save electricity and water both at home and at school. Simple habits such as turning off lights, fans, and electrical appliances when they are not in use can cut down on energy waste significantly. Second, we ought to limit single-use plastic products because plastic takes hundreds of years to break down. Instead of using plastic bags and disposable bottles, students can bring reusable cloth bags and refillable water bottles every day. Finally, planting more trees and walking or cycling to school will reduce greenhouse gas emissions and keep the air cleaner. In short, small daily actions can create a huge positive impact on our planet's sustainable future.
]

#passage-box(title: "BÀI MẪU SỐ 3 (UNIT 3 – MUSIC): Sharing an unforgettable music event experience (134 words)")[
  Last Saturday evening, I attended the Autumn Youth Music Show at our city cultural center with my best friends, and it was an unforgettable experience. The charity concert was organized by local high school clubs to raise funds for disadvantaged children. More than five hundred enthusiastic spectators filled the hall, so the atmosphere was lively and exciting from the beginning. Twelve talented student bands performed both modern pop hits and traditional folk melodies using bamboo clappers and guitars. My favorite moment was the final live performance, where the lead singer invited the whole audience to sing along and wave flashlights together. The music made everyone feel deeply connected and relaxed after a stressful week of studying. Overall, the concert inspired me to learn the guitar, and I truly hope to join next year's show.
]
