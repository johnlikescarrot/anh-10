# -*- coding: utf-8 -*-
"""Phần I - Chương 1: Từ vựng Units 1-3 (Global Success 10)."""
from common import *

CW = [34*mm, 22*mm, 34*mm, W-90*mm]  # word | type/IPA short | meaning | example

def unit_table(rows):
    data = [["Từ vựng", "Loại từ", "Nghĩa", "Ví dụ (ngữ cảnh thi)"]]
    data += rows
    return table(data, CW)

def build():
    f = []
    f.append(band("PHẦN I — HỆ THỐNG KIẾN THỨC TRỌNG TÂM", NAVY))
    f.append(spacer(6))
    f.append(P("CHƯƠNG 1: TỪ VỰNG THEO CHỦ ĐIỂM (UNITS 1–3)", "h1"))
    f.append(P("Ma trận yêu cầu: nhận ra và nhớ từ vựng (Biết), phân biệt từ trong ngữ cảnh (Hiểu) và <b>dùng đúng dạng của từ "
               "trong câu tự luận (Vận dụng)</b>. Vì vậy với mỗi từ, hãy học theo “bộ ba”: <b>từ – nghĩa – một cụm/ví dụ</b>. "
               "Học từ đơn lẻ rất nhanh quên; học theo cụm (collocation) thì vừa nhớ lâu vừa dùng được ngay vào bài viết."))
    f.append(box("CÁCH HỌC TỪ VỰNG “3 LỚP” DỄ NHỚ NHẤT",
                 ["<b>Lớp 1 – Gia đình từ (word family):</b> học 1 từ gốc, suy ra danh/động/tính/trạng từ (vd: <i>responsibility → responsible</i>). "
                  "Đây là chìa khóa của 2 câu tự luận vận dụng từ vựng.",
                  "<b>Lớp 2 – Cụm cố định (collocation):</b> <i>do the laundry, share household chores, reduce carbon footprint, perform on stage…</i>",
                  "<b>Lớp 3 – Câu ví dụ của chính em:</b> đặt 1 câu về gia đình/lớp học của mình cho mỗi từ khó. Tự đặt câu = nhớ gấp đôi."],
                 bg=LIGHT3, border=GREEN))

    # ---------------- UNIT 1 ----------------
    f.append(P("1.1. UNIT 1 — FAMILY LIFE (Cuộc sống gia đình)", "h2"))
    f.append(unit_table([
        ["breadwinner /ˈbredwɪnə(r)/", "n", "người trụ cột (kiếm tiền chính)", "My father is the <b>breadwinner</b> of the family."],
        ["homemaker /ˈhəʊmmeɪkə(r)/", "n", "người nội trợ", "Her mother is a <b>homemaker</b> who looks after the house."],
        ["household chores /ˈhaʊshəʊld tʃɔːz/", "n.phr", "việc nhà", "Children should help with <b>household chores</b>."],
        ["divide /dɪˈvaɪd/ (v) → division (n)", "v", "chia, phân chia", "We <b>divide</b> the housework equally."],
        ["share /ʃeə(r)/", "v", "chia sẻ, cùng làm", "Sharing chores helps family members feel closer."],
        ["groceries /ˈɡrəʊsəriz/", "n (số nhiều)", "hàng tạp hóa, đồ ăn mua về", "My mum buys <b>groceries</b> at the market every morning."],
        ["heavy lifting", "n.phr", "việc nặng nhọc (khuân vác)", "Dad usually does the <b>heavy lifting</b> at home."],
        ["laundry /ˈlɔːndri/", "n", "việc giặt ủi; đồ cần giặt", "I often do the <b>laundry</b> at weekends."],
        ["washing-up", "n", "việc rửa bát đĩa", "After dinner, my brother does the <b>washing-up</b>."],
        ["care for", "phr.v", "chăm sóc", "Grandparents help to <b>care for</b> the children."],
        ["raise /reɪz/", "v", "nuôi nấng, nuôi dạy", "It is not easy to <b>raise</b> three children."],
        ["responsibility /rɪˌspɒnsəˈbɪləti/", "n", "trách nhiệm", "Cooking is my <b>responsibility</b> in the family."],
        ["responsible /rɪˈspɒnsəbl/", "adj", "có trách nhiệm; chịu trách nhiệm", "Be <b>responsible for</b> your own tasks."],
        ["grateful /ˈɡreɪtfl/", "adj", "biết ơn", "I am <b>grateful for</b> my parents' support."],
        ["benefit /ˈbenɪfɪt/", "n / v", "lợi ích; có lợi", "Sharing housework brings many <b>benefits</b>."],
        ["bond /bɒnd/", "n / v", "sự gắn kết; gắn bó", "Doing things together strengthens the family <b>bond</b>."],
        ["routine /ruːˈtiːn/", "n", "thói quen, việc làm thường ngày", "My daily <b>routine</b> starts at 5.30 a.m."],
        ["value /ˈvæljuː/", "n", "giá trị", "Respect is an important family <b>value</b>."],
        ["character /ˈkærəktə(r)/", "n", "tính cách, phẩm chất", "Doing chores builds children's <b>character</b>."],
        ["support /səˈpɔːt/", "v / n", "ủng hộ, hỗ trợ", "Family members should <b>support</b> one another."],
    ]))
    f.append(box("CỤM TỪ VÀNG — UNIT 1 (dùng ngay cho Writing 3)",
                 ["<b>share/divide household chores</b> (chia sẻ việc nhà) • <b>be responsible for + N/V-ing</b> (chịu trách nhiệm làm gì) • "
                  "<b>do the cooking / laundry / washing-up / heavy lifting</b> • <b>look after = care for = take care of</b> (chăm sóc) • "
                  "<b>strengthen the family bond</b> (thắt chặt tình cảm gia đình) • <b>be grateful for sth</b> (biết ơn về điều gì)"],
                 bg=LIGHT2, border=ORANGE))
    f.append(P("<b>Mẹo nhớ Unit 1:</b> Hãy hình dung một ngày của gia đình theo thứ tự: mua đồ (<i>groceries</i>) → nấu ăn → rửa bát "
               "(<i>washing-up</i>) → giặt đồ (<i>laundry</i>) → việc nặng (<i>heavy lifting</i>). Người kiếm tiền là <i>breadwinner</i> "
               "(“người thắng bánh mì” cho cả nhà), người lo việc nhà là <i>homemaker</i> (“người làm nên tổ ấm”). "
               "Cặp dễ nhầm nhất: <b>responsibility</b> (danh từ, <i>trách nhiệm</i>) ↔ <b>responsible</b> (tính từ) — câu tự luận rất hay kiểm tra cặp này.", "p"))

    # ---------------- UNIT 2 ----------------
    f.append(P("1.2. UNIT 2 — HUMANS AND THE ENVIRONMENT (Con người và môi trường)", "h2"))
    f.append(unit_table([
        ["environment /ɪnˈvaɪrənmənt/", "n", "môi trường", "We must protect the <b>environment</b>."],
        ["environmental /ɪnˌvaɪrənˈmentl/", "adj", "thuộc về môi trường", "<b>Environmental</b> protection is everyone's duty."],
        ["pollution /pəˈluːʃn/ → pollute (v)", "n", "sự ô nhiễm", "Air <b>pollution</b> is a serious problem in big cities."],
        ["eco-friendly /ˌiːkəʊ ˈfrendli/", "adj", "thân thiện với môi trường", "We should use <b>eco-friendly</b> products."],
        ["carbon footprint /ˈkɑːbən ˈfʊtprɪnt/", "n", "“dấu chân carbon” (lượng CO₂ thải ra)", "Cycling helps reduce your <b>carbon footprint</b>."],
        ["global warming /ˌɡləʊbl ˈwɔːmɪŋ/", "n", "sự nóng lên toàn cầu", "<b>Global warming</b> causes extreme weather."],
        ["climate change /ˈklaɪmət tʃeɪndʒ/", "n", "biến đổi khí hậu", "<b>Climate change</b> affects farming badly."],
        ["natural resources /ˈnætʃrəl rɪˈsɔːsɪz/", "n", "tài nguyên thiên nhiên", "We should save <b>natural resources</b> like water."],
        ["energy /ˈenədʒi/", "n", "năng lượng", "Turn off the lights to save <b>energy</b>."],
        ["electricity /ɪˌlekˈtrɪsəti/", "n", "điện", "Solar panels produce clean <b>electricity</b>."],
        ["appliance /əˈplaɪəns/", "n", "thiết bị (gia dụng)", "Turn off electrical <b>appliances</b> when not in use."],
        ["reduce /rɪˈdjuːs/", "v", "giảm, cắt giảm", "We should <b>reduce</b> the use of plastic bags."],
        ["reuse /ˌriːˈjuːz/", "v", "tái sử dụng", "<b>Reuse</b> old bottles instead of throwing them away."],
        ["recycle /ˌriːˈsaɪkl/", "v", "tái chế", "Paper and cans can be <b>recycled</b>."],
        ["protect /prəˈtekt/ → protection (n)", "v", "bảo vệ", "Everyone should <b>protect</b> the planet."],
        ["clean up", "phr.v", "dọn dẹp, làm sạch", "Students will <b>clean up</b> the park on Sunday."],
        ["set up", "phr.v", "thành lập, thiết lập", "Our school has <b>set up</b> a Green Club."],
        ["aware /əˈweə(r)/ → awareness (n)", "adj", "nhận thức; sự nhận thức", "We need to raise <b>awareness</b> of recycling."],
        ["waste /weɪst/", "n / v", "rác thải; lãng phí", "Don't <b>waste</b> water. Sort your <b>waste</b>!"],
        ["litter /ˈlɪtə(r)/", "n / v", "rác (vứt bừa bãi); xả rác", "Please don't drop <b>litter</b> in the park."],
    ]))
    f.append(box("CỤM TỪ VÀNG — UNIT 2",
                 ["<b>the 3Rs: Reduce – Reuse – Recycle</b> (giảm – tái sử dụng – tái chế) • <b>protect the environment</b> • "
                  "<b>raise people's awareness of…</b> (nâng cao nhận thức về…) • <b>cut down on</b> (cắt giảm) • "
                  "<b>go green / live green</b> (sống xanh) • <b>be harmful to</b> (có hại cho) • <b>save energy/water</b> (tiết kiệm)"],
                 bg=LIGHT2, border=ORANGE))
    f.append(P("<b>Mẹo nhớ Unit 2:</b> Nhớ “công thức 3R” theo thứ tự giảm dần mức độ tốt cho môi trường: "
               "<i>Reduce</i> (giảm dùng) → <i>Reuse</i> (dùng lại) → <i>Recycle</i> (tái chế). "
               "Phân biệt: <b>pollute</b> (động từ) – <b>pollution</b> (danh từ) – <b>polluted</b> (tính từ: bị ô nhiễm). "
               "<i>Carbon footprint</i> = dấu chân ta “đạp” lên Trái Đất bằng lượng khí thải — đi xe đạp thì dấu chân nhẹ hơn.", "p"))

    # ---------------- UNIT 3 ----------------
    f.append(P("1.3. UNIT 3 — MUSIC (Âm nhạc)", "h2"))
    f.append(unit_table([
        ["music /ˈmjuːzɪk/ → musical (adj), musician (n)", "n", "âm nhạc; thuộc âm nhạc; nhạc sĩ", "<b>Music</b> plays an important part in our life."],
        ["instrument /ˈɪnstrəmənt/", "n", "nhạc cụ; dụng cụ", "The piano is a popular musical <b>instrument</b>."],
        ["artist /ˈɑːtɪst/", "n", "nghệ sĩ", "She is a talented young <b>artist</b>."],
        ["composer /kəmˈpəʊzə(r)/", "n", "nhà soạn nhạc", "The <b>composer</b> wrote this song in 1990."],
        ["composition /ˌkɒmpəˈzɪʃn/", "n", "tác phẩm, bản nhạc", "His latest <b>composition</b> won a prize."],
        ["concert /ˈkɒnsət/", "n", "buổi hòa nhạc", "We went to a live <b>concert</b> last night."],
        ["performance /pəˈfɔːməns/ → perform (v)", "n", "buổi/màn biểu diễn", "Her <b>performance</b> impressed the judges."],
        ["audience /ˈɔːdiəns/", "n", "khán giả", "The <b>audience</b> clapped loudly."],
        ["talent /ˈtælənt/ → talented (adj)", "n", "tài năng; có tài", "The show helps young <b>talents</b> to shine."],
        ["judge /dʒʌdʒ/", "n / v", "giám khảo; chấm, đánh giá", "The <b>judges</b> gave her the highest score."],
        ["single /ˈsɪŋɡl/", "n", "đĩa đơn (một bài hát)", "The singer has just released a new <b>single</b>."],
        ["album /ˈælbəm/", "n", "album (tập hợp bài hát)", "Their first <b>album</b> sold millions of copies."],
        ["songwriter /ˈsɒŋraɪtə(r)/", "n", "người sáng tác ca khúc", "He is a famous singer and <b>songwriter</b>."],
        ["upload /ˌʌpˈləʊd/", "v", "tải lên (mạng)", "Fans <b>upload</b> videos of the show every day."],
        ["view /vjuː/", "n / v", "lượt xem; xem", "The video got millions of <b>views</b>."],
        ["trumpet /ˈtrʌmpɪt/", "n", "kèn trumpet", "He plays the <b>trumpet</b> in the school band."],
        ["piano /piˈænəʊ/ – guitar /ɡɪˈtɑː(r)/ – violin /ˌvaɪəˈlɪn/", "n", "đàn piano – ghi-ta – vĩ cầm", "She has played the <b>piano</b> since she was six."],
        ["record /ˈrekɔːd/ (n) – /rɪˈkɔːd/ (v)", "n / v", "bản thu âm; thu âm", "They will <b>record</b> the song tomorrow."],
        ["decide /dɪˈsaɪd/ → decision (n)", "v", "quyết định", "The judges will <b>decide</b> the winner tonight."],
        ["famous /ˈfeɪməs/ (for)", "adj", "nổi tiếng (về)", "The band is <b>famous for</b> its folk songs."],
    ]))
    f.append(box("CỤM TỪ VÀNG — UNIT 3",
                 ["<b>play the piano/guitar/violin/trumpet</b> (chơi đàn/kèn — nhớ mạo từ <i>the</i>!) • <b>perform on stage / give a performance</b> • "
                  "<b>take part in / participate in</b> a talent show • <b>release a single/album</b> (phát hành) • "
                  "<b>be famous for…</b> • <b>attract a large audience</b> • <b>upload a video clip</b>"],
                 bg=LIGHT2, border=ORANGE))
    f.append(P("<b>Mẹo nhớ Unit 3:</b> Nhóm người: <i>composer</i> (soạn) → <i>songwriter</i> (viết ca khúc) → <i>musician/artist</i> (biểu diễn) → "
               "<i>judge</i> (chấm) → <i>audience</i> (xem). Nhóm sản phẩm: <i>single</i> (1 bài) → <i>album</i> (nhiều bài) → <i>record</i> (bản thu). "
               "Bẫy kinh điển: <b>play the piano</b> nhưng <b>play football</b> (nhạc cụ có <i>the</i>, thể thao thì không).", "p"))

    # ---------------- Word families ----------------
    f.append(P("1.4. Gia đình từ (Word families) — “vũ khí” cho câu tự luận vận dụng từ vựng", "h2"))
    f.append(P("2 câu tự luận của phần từ vựng thường yêu cầu điền <b>dạng đúng của từ cho sẵn</b>. Quy tắc vàng: "
               "<b>nhìn vị trí trống trước, đoán loại từ cần điền, rồi mới biến đổi từ</b>. Bảng dưới đây là các gia đình từ xuất hiện nhiều nhất trong Units 1–3:", "p"))
    f.append(table([
        ["Từ gốc", "Danh từ (n)", "Động từ (v)", "Tính từ (adj)", "Trạng từ (adv)"],
        ["responsibility", "responsibility", "—", "responsible", "responsibly"],
        ["environment", "environment", "—", "environmental", "environmentally"],
        ["pollute", "pollution / pollutant", "pollute", "polluted / polluting", "—"],
        ["protect", "protection / protector", "protect", "protective", "—"],
        ["music", "music / musician", "—", "musical", "musically"],
        ["perform", "performance / performer", "perform", "—", "—"],
        ["compose", "composition / composer", "compose", "—", "—"],
        ["decide", "decision", "decide", "decisive", "—"],
        ["benefit", "benefit", "benefit", "beneficial", "—"],
        ["grateful", "gratitude", "—", "grateful", "gratefully"],
        ["aware", "awareness", "—", "aware", "—"],
        ["talent", "talent", "—", "talented", "—"],
        ["care", "care", "care (for)", "careful / caring", "carefully"],
        ["value", "value", "value", "valuable", "—"],
    ], [32*mm, 38*mm, 32*mm, 38*mm, W-140*mm]))
    f.append(box("QUY TẮC ĐIỀN DẠNG TỪ — NHỚ THEO VỊ TRÍ",
                 ["Sau <b>a/an/the, tính từ, giới từ</b> → cần <b>danh từ</b>: <i>the ___ of the environment → protection</i>.",
                  "Sau <b>to be (am/is/are/was/were), become, seem, feel</b> → cần <b>tính từ</b>: <i>be ___ for → responsible</i>.",
                  "Sau <b>chủ ngữ</b>, cần hành động → <b>động từ</b> (nhớ chia thì và số): <i>Students ___ the park → clean up</i>.",
                  "Bổ nghĩa cho <b>động từ</b> (trả lời “như thế nào?”) → <b>trạng từ</b> (-ly): <i>divide the chores ___ → equally</i>.",
                  "Sau <b>very/so/too, more/most</b> → <b>tính từ</b>: <i>very ___ → talented</i>."],
                 bg=LIGHT, border=NAVY))
    f.append(P("<b>Hậu tố nhận diện nhanh:</b> danh từ thường kết thúc bằng <i>-tion/-sion, -ment, -ness, -ity, -ance/-ence, -er/-or</i> (người); "
               "tính từ: <i>-ful, -less, -able, -ible, -ive, -al, -ous, -ed/-ing</i>; trạng từ: <i>-ly</i>; động từ: <i>-ise/-ize, -en</i>.", "p"))
    return f
