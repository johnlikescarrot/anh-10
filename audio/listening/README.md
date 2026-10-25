# Bộ File Luyện Nghe MP3 — Tiếng Anh 10 *Global Success* · GK1 2026–2027

Bộ audio được dựng **hoàn toàn ngoại tuyến (offline)** từ chính 04 tapescripts
(180–200 từ/bài) trong
[`DE_CUONG_ON_TAP_TIENG_ANH_10_GK1_2026_2027_GLOBAL_SUCCESS.pdf`](../../DE_CUONG_ON_TAP_TIENG_ANH_10_GK1_2026_2027_GLOBAL_SUCCESS.pdf)
(Phần V), bám sát cấu trúc đề thi thật: **Part 1 True/False + Part 2 MCQs, mỗi
bài nghe 2 lần, có thời gian đọc đề và kiểm tra bài**.

> **Phạm vi: phủ 100% bài nghe trong PDF** — 04 tapescripts của 02 đề thi thử
> (Đề 01: Part 1 hội thoại chia sẻ việc nhà + Part 2 radio talk về Minh Khoa;
> Đề 02: Part 1 thông báo hội chợ Eco-Campus + Part 2 phỏng vấn bữa cơm gia đình).

## 1. Dàn giọng đọc neural (5 giọng, đa dạng giới tính & giọng vùng)

Mô hình TTS neural **Piper VITS, chất lượng medium, 22,05 kHz**, mã hóa MP3
96 kbps mono 44,1 kHz; chuẩn hóa đỉnh −0,7 dBFS để mọi file cùng âm lượng.

| Khóa giọng | Model Piper | Giống | Giọng vùng | Vai trò trong các bài nghe |
|---|---|---|---|---|
| `announcer` | `en_GB-alan-medium` | Nam | Anh-Anh | Lời dẫn đề thi, hướng dẫn, hiệu lệnh |
| `f_lessac` | `en_US-lessac-medium` | Nữ | Anh-Mỹ | Mrs. Lan (Đề 01-P1) |
| `f_hfc` | `en_US-hfc_female-medium` | Nữ (trẻ) | Anh-Mỹ | An (Đề 01-P1), Mai (Đề 02-P1) |
| `f_jenny` | `en_GB-jenny_dioco-medium` | Nữ | Anh-Anh | Người dẫn chương trình *Family Matters* (Đề 02-P2) |
| `m_ryan` | `en_US-ryan-medium` | Nam | Anh-Mỹ | Dẫn *Youth Spotlight* (Đề 01-P2), Dr. Hoang Minh (Đề 02-P2) |

Bốn bài nghe bao phủ đủ ba dạng ngữ liệu theo ma trận: **hội thoại hai nữ**
(Đề 01-P1), **độc thoại radio nam** (Đề 01-P2), **độc thoại thông báo nữ**
(Đề 02-P1) và **phỏng vấn nam – nữ khác giọng vùng** (Đề 02-P2, Anh-Anh đối
thoại Anh-Mỹ).

## 2. Quy ước tên file & 03 phiên bản mỗi bài

Mỗi bài nghe có mã `<Đề>-<Part>-<slug>` và 04 phiên bản:

| Hậu tố | Nội dung | Mục đích sử dụng |
|---|---|---|
| `_clean.mp3` | Đọc **một lần**, tốc độ tự nhiên (~160–170 từ/phút), nghỉ tự nhiên giữa lượt lời/đoạn văn | Nghe nắm ý, nghe lặp nhiều lần, shadowing |
| `_slow.mp3` | Đọc **chậm 30%** (length scale 1,30), khoảng nghỉ dài hơn | Nghe chi tiết, bắt từ còn yếu |
| `_dictation.mp3` | **Chép chính tả từng câu**: mỗi câu đọc một lần (chậm nhẹ 1,15×) rồi nghỉ 5,5 giây để viết; hết bài đọc lại trọn vẹn một lượt để đối chiếu | Luyện dictation, chính tả và ngữ pháp nghe |
| `_exam.mp3` | **Bản chuẩn phòng thi**: tiếng bíp → lời dẫn → 30 giây đọc câu hỏi → nghe lần 1 → 10 giây kiểm tra → nghe lần 2 → tiếng bíp kết thúc | Luyện thi mô phỏng thật, bấm giờ như đề chính thức |

Ngoài ra mỗi đề có file góp `DE0x-listening-full_exam.mp3` (Part 1 + Part 2
liền mạch, có lời chuyển phần) để thi thử trọn vẹn kỹ năng Listening. Thư mục
[`playlists/`](./playlists) chứa 03 playlist M3U đường dẫn tương đối: mô phỏng
đề thi, luyện tốc độ tự nhiên, và nghe chậm + chép chính tả.

## 3. Danh mục track

Chi tiết thời lượng, dung lượng, mã băm SHA-256 và giọng đọc của từng file được
lưu tự động trong [`manifest.json`](./manifest.json). Dưới đây là tóm tắt:

### Đề thi thử số 01 — `de01/`

| File | Nội dung | Thời lượng |
|---|---|---|
| `DE01-P1-housework-conversation_clean.mp3` | Hội thoại An & Mrs. Lan — việc nhà (182 từ) | ~62 giây |
| `DE01-P1-housework-conversation_slow.mp3` | Bản chậm 30% | ~73 giây |
| `DE01-P1-housework-conversation_dictation.mp3` | Chép chính tả từng câu (17 câu) | ~3 phút 56 |
| `DE01-P1-housework-conversation_exam.mp3` | Bản chuẩn phòng thi (nghe 2 lần) | ~3 phút 16 |
| `DE01-P2-minh-khoa-radio-talk_clean.mp3` | Radio talk về thí sinh Minh Khoa (181 từ) | ~62 giây |
| `DE01-P2-minh-khoa-radio-talk_slow.mp3` | Bản chậm 30% | ~71 giây |
| `DE01-P2-minh-khoa-radio-talk_dictation.mp3` | Chép chính tả từng câu (10 câu) | ~3 phút 22 |
| `DE01-P2-minh-khoa-radio-talk_exam.mp3` | Bản chuẩn phòng thi (nghe 2 lần) | ~3 phút 14 |
| `DE01-listening-full_exam.mp3` | Góp trọn Part 1 + Part 2 mô phỏng đề thi | ~6 phút 38 |

### Đề thi thử số 02 — `de02/`

| File | Nội dung | Thời lượng |
|---|---|---|
| `DE02-P1-eco-campus-fair-announcement_clean.mp3` | Mai thông báo hội chợ Eco-Campus (186 từ) | ~66 giây |
| `DE02-P1-eco-campus-fair-announcement_slow.mp3` | Bản chậm 30% | ~76 giây |
| `DE02-P1-eco-campus-fair-announcement_dictation.mp3` | Chép chính tả từng câu (08 câu) | ~3 phút 18 |
| `DE02-P1-eco-campus-fair-announcement_exam.mp3` | Bản chuẩn phòng thi (nghe 2 lần) | ~3 phút 25 |
| `DE02-P2-family-mealtime-interview_clean.mp3` | Phỏng vấn Dr. Hoang Minh — bữa cơm gia đình (187 từ) | ~68 giây |
| `DE02-P2-family-mealtime-interview_slow.mp3` | Bản chậm 30% | ~81 giây |
| `DE02-P2-family-mealtime-interview_dictation.mp3` | Chép chính tả từng câu (15 câu) | ~4 phút 01 |
| `DE02-P2-family-mealtime-interview_exam.mp3` | Bản chuẩn phòng thi (nghe 2 lần) | ~3 phút 28 |
| `DE02-listening-full_exam.mp3` | Góp trọn Part 1 + Part 2 mô phỏng đề thi | ~7 phút 00 |

> Tổng cộng **18 file MP3** cho cả 02 đề (04 bài nghe × 04 phiên bản + 02 file
> góp), khớp 100% 04 tapescripts trong PDF; mọi thông số kỹ thuật lưu trong
> [`manifest.json`](./manifest.json) và được đối chiếu tự động bằng
> `scripts/tts/check_coverage.py`.

## 4. Tái tạo hoàn toàn offline

Môi trường thực thi chỉ có quyền truy cập GitHub/PyPI; toàn bộ mô hình nằm trong
các Git repository công khai (không dùng Git LFS) và runtime cài từ PyPI.

```bash
# 1. Môi trường Python 3.11
python3 -m venv .venv-tts
.venv-tts/bin/pip install "piper-tts==1.2.0" "onnxruntime<2" lameenc imageio-ffmpeg

# 2. Tải 05 model giọng đọc (sparse clone, ~316 MB vào .tts-models/, đã gitignore)
bash scripts/tts/download_models.sh

# 3. Dựng toàn bộ MP3 (hoặc: --exam 1 --variants clean,slow,exam)
.venv-tts/bin/python scripts/tts/build_listening_audio.py --exam all

# 4. Kiểm chứng chất lượng: cấu trúc phòng thi, khoảng lặng 30s/10s,
#    tiếng bíp 880 Hz, ID3 tags, thời lượng khớp manifest
.venv-tts/bin/python scripts/tts/verify_audio.py

# 5. Đối chiếu độ phủ 100%: mọi tapescript trong PDF đều có đủ 04 phiên bản MP3
.venv-tts/bin/python scripts/tts/check_coverage.py
```

| Script | Vai trò |
|---|---|
| [`scripts/tts/tapescripts.py`](../../scripts/tts/tapescripts.py) | Nguyên văn 04 tapescripts, phân vai giọng & lời dẫn đề thi |
| [`scripts/tts/build_listening_audio.py`](../../scripts/tts/build_listening_audio.py) | Engine tổng hợp PCM, ghép khoảng lặng/tiếng bíp, chuẩn hóa âm lượng, mã hóa MP3 + ID3, xuất playlist M3U |
| [`scripts/tts/download_models.sh`](../../scripts/tts/download_models.sh) | Tải & sắp xếp model Piper từ các repository nguồn |
| [`scripts/tts/verify_audio.py`](../../scripts/tts/verify_audio.py) | Tự động kiểm chứng cấu trúc/thời lượng/tag của toàn bộ track |
| [`scripts/tts/check_coverage.py`](../../scripts/tts/check_coverage.py) | Chứng minh phủ 100% tapescript PDF: đối chiếu nguyên văn từng câu + sự đủ mặt các biến thể |

## 5. Bản quyền & nguồn gốc model

- Văn bản tapescript thuộc tài liệu học tập trong repository này.
- Giọng đọc Piper là các mô hình nguồn mở do cộng đồng huấn luyện; giấy phép
  theo từng model (phổ biến là CC BY-NC-SA 4.0). Bộ audio này phục vụ **mục đích
  giáo dục phi thương mại**. Nguồn tải model được ghi rõ trong
  `scripts/tts/download_models.sh`.
- Mọi file MP3 gắn ID3 tag ghi rõ tên bài, danh sách giọng đọc và trích dẫn PDF
  nguồn để dễ truy vết.
