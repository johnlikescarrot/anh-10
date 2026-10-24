#import "style.typ": *

// ============================================================================
// PART IV: 02 FULL MOCK EXAMS STRICTLY ALIGNED WITH THE 2026–2027 MATRIX
// ============================================================================

#part-banner(
  "PHẦN IV",
  "02 ĐỀ THI THỬ CHUẨN 100% MA TRẬN GIỮA KỲ 1 (NĂM HỌC 2026–2027)",
  "Cấu trúc chuẩn: 28 câu Trắc nghiệm (7,0 điểm) + 6 câu & 1 bài viết Tự luận (3,0 điểm) | Thời gian làm bài: 60 phút"
)

// ============================================================================
// MOCK EXAM 01
// ============================================================================

#block(
  width: 100%,
  fill: c-navy-soft,
  stroke: 1pt + c-navy,
  radius: 6pt,
  inset: (x: 14pt, y: 10pt),
  breakable: false,
  below: 10pt,
)[
  #grid(
    columns: (1fr, 1fr),
    align: (left + horizon, right + horizon),
    stack(
      spacing: 8.5pt,
      text(weight: "bold", size: 9pt, fill: c-navy)[ĐỀ KIỂM TRA GIỮA HỌC KỲ 1 – NĂM HỌC 2026–2027],
      text(weight: "extrabold", size: 12.5pt, fill: c-teal)[ĐỀ THI THỬ CHUẨN MA TRẬN SỐ 01],
    ),
    stack(
      spacing: 8.5pt,
      text(weight: "bold", size: 9pt, fill: c-navy)[MÔN: TIẾNG ANH LỚP 10 (GLOBAL SUCCESS)],
      text(size: 8.8pt, fill: c-ink)[Thời gian: *60 phút* | Tổng điểm: *10,0 điểm*],
    )
  )
]

#place(hide(heading(level: 1, outlined: true)[Đề Thi Thử Chuẩn Ma Trận Số 01]))

== PHẦN I. TRẮC NGHIỆM KHÁCH QUAN (7,00 điểm | Câu 1 – Câu 28; 0,25 điểm/câu)

*I. LISTENING (2,50 điểm)*

*Part 1. Listen to a conversation between An and Mrs. Lan about sharing housework in An's family (Tapescript in Part V). Decide whether the following statements are True (A) or False (B).*

#tf-item("1", [Both of An's parents work full-time, so all family members share the household chores.])
#tf-item("2", [An's father is only responsible for doing the heavy lifting at weekends.])
#tf-item("3", [An puts out the rubbish and waters the balcony plants every afternoon.])
#tf-item("4", [An's younger brother never helps with housework because he is only nine years old.])
#tf-item("5", [An feels that sharing chores brings her family closer together rather than making her tired.])

*Part 2. Listen to a radio talk about Minh Khoa, a young contestant in a national music show (Tapescript in Part V). Choose the best answer A, B, C, or D.*

#mcq2("6", [At what age did Minh Khoa start learning to play the acoustic guitar?],
  [At the age of seven], [At the age of ten], [At the age of twelve], [At the age of fifteen])

#mcq2("7", [Who taught Minh Khoa his first traditional folk melodies?],
  [His school music teacher], [A famous pop judge], [His grandfather], [His older sister])

#mcq2("8", [In the quarter-final round, Minh Khoa impressed the audience by combining modern pop with #blank.],
  [opera singing], [the moon-shaped lute], [electronic drums], [piano solos])

#mcq2("9", [Why was Minh Khoa worried two days before the semi-final night?],
  [He forgot the lyrics of his song.], [His guitar string broke on stage.], [He caught a mild cold and sore throat.], [His parents could not watch the show.])

#mcq2("10", [What does Minh Khoa plan to do with his prize money if he wins the competition?],
  [Buy an expensive electric car], [Record an album in London], [Donate instruments to rural school clubs], [Open a private music café])

*II. LANGUAGE (1,50 điểm TNKQ)*

*Choose the best answer A, B, C, or D to complete each of the following sentences.*

#mcq4("11", [Doing household chores together helps children appreciate the value of hard work and #blank family bonds.],
  [strengthen], [eliminate], [pollute], [interrupt])

#mcq4("12", [Switching to reusable cloth bags is an effective way to #blank plastic waste in daily shopping.],
  [cheer up], [cut down on], [look after], [make up])

#mcq4("13", [Be quiet, please! The judges #blank their comments on the band's live performance right now.],
  [give], [gave], [are giving], [usually give])

#mcq4("14", ["Look at the dark clouds gathering over the stadium!" – "Oh no, it #blank before the concert starts."],
  [will rain], [is going to rain], [rains], [rained])

#mcq4("15", [More than three hundred bamboo trees #blank along the school fence by volunteers last Saturday.],
  [planted], [are planted], [were planted], [have planted])

#mcq4("16", [My parents always encourage me #blank part in community clean-up activities on Sundays.],
  [take], [taking], [to take], [took])

*III. READING (2,50 điểm)*

*Part 1. Read the following leaflet and mark the letter A, B, C, or D to indicate the option that best fits each blank.*

#passage-box(title: "GREEN SUNDAY AT BINH MINH PARK — JOIN HANDS FOR NATURE!")[
  Would you like to make our city cleaner and greener this weekend? Come to *Green Sunday*, an inspiring community event organized #cblank("17") the City Youth Union!
  - *Time:* 7:00 a.m. – 10:30 a.m., Sunday, November 8.
  - *Main activities:*
    - Collect plastic litter around the lake #cblank("18") sort recyclable cans and bottles on the spot.
    - Exchange 5 kg of old paper for a lovely green plant #cblank("19") home for your study desk!
    - Learn practical tips on saving household #cblank("20") and lowering your family's monthly bills.
  Gloves and cloth bags will be provided free of charge. Let's adopt an eco-friendly #cblank("21") today for a brighter tomorrow!
]

#mcq4("17", [], [by], [with], [from], [at])
#mcq4("18", [], [but], [or], [and], [for])
#mcq4("19", [], [bring], [to bring], [bringing], [brought])
#mcq4("20", [], [energy], [audience], [laundry], [character])
#mcq4("21", [], [instrument], [lifestyle], [breadwinner], [spectator])

*Part 2. Read the following passage (228 words) and mark the letter A, B, C, or D to indicate the correct answer to each question.*

#passage-box[
  Television music competitions have transformed how young musical talents build their professional careers over the past two decades. Popular programmes such as *American Idol* and *Vietnam Idol* welcome ordinary citizens who dream of singing on a bright national stage. Instead of needing wealthy sponsors or famous family connections, contestants only need genuine passion, strong vocal skill, and determination to audition in front of experienced judges.

  Participating in a multi-week competition is both exciting and physically demanding. Every single week, finalists rehearse tirelessly with vocal coaches, live band members, and stage choreographers to prepare an unforgettable live performance. Meanwhile, millions of television viewers watch eagerly from home and vote for #underline[#strong[their]] favorite singers via mobile apps or text messages. Because at least one contestant is eliminated after each round, young performers must learn to stay calm under intense pressure and accept constructive feedback gracefully.

  Even for contestants who do not win first prize, these television programmes offer #underline[#strong[valuable]] career opportunities. Many talented runners-up gain loyal fan communities on social media and release successful debut singles shortly after the final night ends. More importantly, music competitions inspire thousands of teenagers watching at home to pick up musical instruments, join school choirs, and discover confidence in their own voices. In this way, televised music contests do far more than entertain families on weekend nights; they actively nurture artistic creativity across generations.
]

#mcq1("22", [What is the passage mainly about?],
  [Why mobile voting apps often fail during live television broadcasts.],
  [How televised music competitions develop young performers and inspire audiences.],
  [The high cost of hiring sponsors for professional pop singers.],
  [Why school choirs are more popular than television reality shows.])

#mcq4("23", [According to paragraph 1, what do contestants need to audition for shows like *Vietnam Idol*?],
  [Wealthy sponsors], [Passion, vocal skill, and determination], [At least three debut albums], [Foreign university degrees])

#mcq4("24", [The word *"their"* in paragraph 2 refers to #blank.],
  [vocal coaches], [experienced judges], [television viewers], [choreographers])

#mcq4("25", [The word *"valuable"* in paragraph 3 is closest in meaning to #blank.],
  [useful and beneficial], [ordinary and boring], [harmful and risky], [spotless and quiet])

#mcq1("26", [Which of the following is NOT TRUE according to the passage?],
  [Finalists practice with vocal coaches and band members every week.],
  [One contestant has to leave the competition after each round.],
  [Only the first-prize winner can release songs after the competition finishes.],
  [Music shows motivate young people at home to learn musical instruments.])

*IV. WRITING — RE-ORDERING (0,50 điểm TNKQ)*

#mcq4("27", [
  a. *Lan:* I'm going to donate my old textbooks to the Green Library corner. Would you like to join me?\
  b. *Nam:* Hi Lan! Where are you carrying that big box of books?\
  c. *Nam:* Definitely! Wait five minutes while I get my comic books from my locker.
], [a – b – c], [b – a – c], [b – c – a], [c – b – a])

#mcq4("28", [
  a. Second, listening to upbeat songs while doing household chores makes cleaning much faster and more enjoyable.\
  b. Music plays a wonderful role in improving our daily mood and productivity.\
  c. First, soft instrumental melodies help students relax their minds after intense exams.\
  d. For these reasons, music truly acts as medicine for every busy student's soul.
], [b – c – a – d], [c – a – b – d], [b – a – c – d], [d – b – c – a])

== PHẦN II. TỰ LUẬN (3,00 điểm | Câu 29 – Câu 35)

*Part A. Vocabulary – Give the correct form of the word in brackets (1,00 điểm | 0,50 điểm/câu).*

*Question 29.* Parents should teach teenagers to use electricity #wblank to protect natural resources. *(RESPONSIBLE)*

*Question 30.* Using chemical sprays too often causes serious #wblank to both soil and underground water. *(POLLUTE)*

*Part B. Sentence Transformation – Rewrite the following sentences without changing their meaning (1,00 điểm | 0,25 điểm/câu).*

*Question 31.* Our school clubs will hold a traditional folk music night next Saturday.\
→ *A traditional folk music night* #tline.

*Question 32.* Because plastic straws harm sea turtles, our canteen stopped using them. *(Use #strong[so])*\
→ *Plastic straws* #tline.

*Question 33.* My father lets me practice the drums in the garage on Sunday afternoons. *(Use #strong[allows])*\
→ *My father* #tline.

*Question 34.* Minh intends to join the school's Go Green volunteer team this semester. *(Use #strong[going to])*\
→ *Minh is* #tline.

*Part C. Paragraph Writing (1,00 điểm).*

*Question 35.* Write a paragraph (#strong[120 – 150 words]) about #strong[three practical ways your family can reduce its carbon footprint at home]. You may use the following suggestions:
- Saving electricity and water in daily routines;
- Reducing single-use plastic when shopping and cooking;
- Using eco-friendly transport and planting green trees/vegetables.

#pagebreak()

// ============================================================================
// MOCK EXAM 02
// ============================================================================

#block(
  width: 100%,
  fill: c-navy-soft,
  stroke: 1pt + c-navy,
  radius: 6pt,
  inset: (x: 14pt, y: 10pt),
  breakable: false,
  below: 10pt,
)[
  #grid(
    columns: (1fr, 1fr),
    align: (left + horizon, right + horizon),
    stack(
      spacing: 8.5pt,
      text(weight: "bold", size: 9pt, fill: c-navy)[ĐỀ KIỂM TRA GIỮA HỌC KỲ 1 – NĂM HỌC 2026–2027],
      text(weight: "extrabold", size: 12.5pt, fill: c-teal)[ĐỀ THI THỬ CHUẨN MA TRẬN SỐ 02],
    ),
    stack(
      spacing: 8.5pt,
      text(weight: "bold", size: 9pt, fill: c-navy)[MÔN: TIẾNG ANH LỚP 10 (GLOBAL SUCCESS)],
      text(size: 8.8pt, fill: c-ink)[Thời gian: *60 phút* | Tổng điểm: *10,0 điểm*],
    )
  )
]

#place(hide(heading(level: 1, outlined: true)[Đề Thi Thử Chuẩn Ma Trận Số 02]))

== PHẦN I. TRẮC NGHIỆM KHÁCH QUAN (7,00 điểm | Câu 1 – Câu 28; 0,25 điểm/câu)

*I. LISTENING (2,50 điểm)*

*Part 1. Listen to an announcement by Mai, leader of the Go Green Youth Club, about an upcoming school event (Tapescript in Part V). Decide whether the statements are True (A) or False (B).*

#tf-item("1", [The Eco-Campus Fair will take place in the main schoolyard this Saturday morning.])
#tf-item("2", [Students need to buy entrance tickets for 20,000 VND to join the workshops.])
#tf-item("3", [Visitors can bring used plastic bottles to exchange for small notebooks or tree saplings.])
#tf-item("4", [Grade 10C is going to perform a short play about ocean pollution at 10:30 a.m.])
#tf-item("5", [The main goal of the fair is to encourage students to practice green habits every day.])

*Part 2. Listen to an interview with Dr. Hoang Minh about family mealtime routines (Tapescript in Part V). Choose the best answer A, B, C, or D.*

#mcq2("6", [According to Dr. Minh's survey, how many evenings a week do busy city families eat dinner together on average?],
  [One evening], [Four evenings], [Six evenings], [Every evening])

#mcq2("7", [What does Dr. Minh identify as the biggest distraction during modern family meals?],
  [Loud street traffic], [Cooking complicated dishes], [Smartphones and television screens], [Unexpected phone calls from teachers])

#mcq2("8", [How can teenagers contribute before dinner starts?],
  [By setting the table and washing vegetables], [By ordering fast food every night], [By repairing kitchen appliances], [By doing all the heavy shopping alone])

#mcq2("9", [According to Dr. Minh, teenagers who regularly eat with their parents tend to have #blank.],
  [more Pocket money], [better communication skills and lower stress], [fewer household duties], [longer summer holidays])

#mcq2("10", [What simple rule does Dr. Minh recommend to every family?],
  [Eat dinner in under ten minutes], [Keep meals "screen-free" for thirty minutes], [Cook only Western dishes on Sundays], [Let parents do all the washing-up])

*II. LANGUAGE (1,50 điểm TNKQ)*

*Choose the best answer A, B, C, or D to complete each of the following sentences.*

#mcq4("11", [When my mother works night shifts at the hospital, my father willingly #blank the cooking and laundry.],
  [makes], [does], [puts], [takes])

#mcq4("12", [Thousands of enthusiastic #blank cheered loudly inside the stadium when the band sang their hit song.],
  [spectators], [appliances], [groceries], [pollutants])

#mcq4("13", [Mr. Nam #blank to work by bus every day to save fuel, although today he #blank his bicycle.],
  [travels / rides], [is travelling / rides], [travels / is riding], [travelled / rides])

#mcq4("14", [The concert hall was completely full, #blank hundreds of fans watched the live stream outside on a big screen.],
  [for], [or], [but], [so])

#mcq4("15", [Single-use plastic cups #blank in our school canteen since the beginning of this school year.],
  [weren't used], [haven't been used], [aren't using], [won't use])

#mcq4("16", [During yesterday's rehearsal, the director made the singers #blank onto the stage without microphones.],
  [step], [to step], [stepping], [stepped])

*III. READING (2,50 điểm)*

*Part 1. Read the following advertisement and mark the letter A, B, C, or D to indicate the option that best fits each blank.*

#passage-box(title: "VIETNAM FOLK & POP NIGHT 2026 — WHERE TRADITION MEETS YOUTH!")[
  Experience a magical evening of music at Vinh City Cultural Palace on Saturday, November 14! *Vietnam Folk & Pop Night 2026* brings together #cblank("17") young singers and master folk musicians on one vibrant stage.
  - Enjoy traditional melodies played #cblank("18") the moon-shaped lute, bamboo flute, and drums.
  - Sing along to chart-topping pop songs arranged in a fresh acoustic style.
  - Meet the winners of *Youth Melody*, who promised #cblank("19") free autographs after the show!
  Tickets #cblank("20") at the student counter from Monday to Friday, #cblank("21") you can book online at `folkpopnight.vn` with a 20% student discount!
]

#mcq4("17", [], [talent], [talented], [talents], [talentedly])
#mcq4("18", [], [on], [in], [at], [to])
#mcq4("19", [], [give], [giving], [to give], [given])
#mcq4("20", [], [sell], [are selling], [are sold], [have sold])
#mcq4("21", [], [or], [nor], [for], [yet])

*Part 2. Read the following passage (221 words) and mark the letter A, B, C, or D to indicate the correct answer to each question.*

#passage-box[
  Along Vietnam's beautiful central coastline, plastic waste has become one of the most urgent environmental challenges in recent years. Every summer holiday, millions of domestic and foreign tourists visit sunny beaches in coastal provinces to swim and enjoy fresh local seafood. Unfortunately, careless littering often leaves behind thousands of disposable plastic bottles, snack wrappers, and foam boxes that wash directly into the sea and threaten marine creatures.

  Recognizing this serious problem, energetic high school students in several coastal towns have launched creative community campaigns to protect #underline[#strong[their]] hometown beaches. Instead of merely picking up rubbish once a year, student volunteer clubs work closely with seaside drink stalls and local fishermen. They politely persuade shop owners to replace single-use plastic straws with reusable bamboo or paper ones and place colourful recycling bins shaped like friendly dolphins along the sand. Because these bins look cheerful and eye-catching, young children and tourists gladly drop empty cans and bottles inside rather than throwing trash on the ground.

  In addition, artistic students turn collected plastic bottle caps into vibrant wall murals depicting clean blue oceans. These public artworks remind every visitor that plastic takes centuries to #underline[#strong[break down]] in nature. Within just one year, several youth-led beaches have become noticeably cleaner, proving that when young citizens take practical action together, sustainable environmental change is entirely achievable.
]

#mcq1("22", [What is the main topic of the passage?],
  [How fishermen build wooden boats in central Vietnam.],
  [Creative youth-led initiatives to reduce coastal plastic pollution in Vietnam.],
  [Why tourists prefer eating seafood indoors during winter.],
  [The history of mural painting in Vietnamese art museums.])

#mcq4("23", [According to paragraph 1, what threatens marine creatures along the coast?],
  [Cold ocean currents], [Bamboo straws], [Plastic bottles, wrappers, and foam boxes], [Dolphin-shaped bins])

#mcq4("24", [The word *"their"* in paragraph 2 refers to #blank.],
  [marine creatures], [high school students], [food wrappers], [art museums])

#mcq4("25", [The phrase *"break down"* in paragraph 3 is closest in meaning to #blank.],
  [decompose naturally], [grow rapidly], [perform live], [increase sharply])

#mcq1("26", [Which of the following is TRUE according to the passage?],
  [Student clubs only clean the beaches once a year during winter.],
  [Shop owners are encouraged to use bamboo or paper straws instead of plastic ones.],
  [Tourists refuse to use the dolphin-shaped recycling bins on the beach.],
  [Collected plastic caps are burned on the sand after every weekend.])

*IV. WRITING — RE-ORDERING (0,50 điểm TNKQ)*

#mcq4("27", [
  a. *Dad:* Don't worry, Minh. I'll help you carry the heavy pots of soil upstairs.\
  b. *Minh:* Dad, I'm going to plant some tomatoes on our balcony, but these soil bags are quite heavy!\
  c. *Minh:* Thank you, Dad! With your help, our green balcony will be ready before lunch.
], [b – a – c], [a – b – c], [b – c – a], [c – a – b])

#mcq4("28", [
  *Dear Tom,*\
  a. After dinner, my sister and I take turns doing the washing-up while Dad puts out the rubbish.\
  b. I hope you and your family in London are doing well!\
  c. Write back soon and tell me which household chores you usually do at home.\
  d. You asked about our evening routine: Mom cooks delicious meals, and I help her wash the vegetables.\
  *Best wishes, Phong*
], [b – a – d – c], [d – b – a – c], [b – d – a – c], [b – d – c – a])

== PHẦN II. TỰ LUẬN (3,00 điểm | Câu 29 – Câu 35)

*Part A. Vocabulary – Give the correct form of the word in brackets (1,00 điểm | 0,50 điểm/câu).*

*Question 29.* All four judges praised Phuong's #wblank in combining folk instruments with modern rap. *(CREATE)*

*Question 30.* Sharing daily chores teaches children to be #wblank for everything their parents do for them. *(GRATEFUL)*

*Part B. Sentence Transformation – Rewrite the following sentences without changing their meaning (1,00 điểm | 0,25 điểm/câu).*

*Question 31.* Volunteers collect over two hundred kilos of recyclable paper at our school every month.\
→ *Over two hundred kilos of recyclable paper* #tline.

*Question 32.* Although Minh practiced the piano for only six months, he played the piece confidently. *(Use #strong[yet])*\
→ *Minh practiced* #tline.

*Question 33.* Mrs. Hoa made her son turn off the air conditioner before going to school. *(Passive voice)*\
→ *Mrs. Hoa's son* #tline.

*Question 34.* My sister spends twenty minutes tidying up her bedroom every morning.\
→ *It takes* #tline.

*Part C. Letter / Email Writing (1,00 điểm).*

*Question 35.* Write an email (#strong[120 – 150 words]) to your English pen pal, #strong[Alex], telling him/her about #strong[how your family divides household chores and why you think sharing housework is important].
