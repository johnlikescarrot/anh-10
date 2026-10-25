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

## 2. Quy ước tên file & 03 phiên bản mỗi bài

Mỗi bài nghe có mã `<Đề>-<Part>-<slug>` và 03 phiên bản:

| Hậu tố | Nội dung | Mục đích sử dụng |
|---|---|---|
| `_clean.mp3` | Đọc **một lần**, tốc độ tự nhiên (~160–170 từ/phút), nghỉ tự nhiên giữa lượt lời/đoạn văn | Nghe nắm ý, nghe lặp nhiều lần, shadowing |
| `_slow.mp3` | Đọc **chậm 30%** (length scale 1,30), khoảng nghỉ dài hơn | Nghe chi tiết, chép chính tả (dictation), bắt từ còn yếu |
| `_exam.mp3` | **Bản chuẩn phòng thi**: tiếng bíp → lời dẫn → 30 giây đọc câu hỏi → nghe lần 1 → 10 giây kiểm tra → nghe lần 2 → tiếng bíp kết thúc | Luyện thi mô phỏng thật, bấm giờ như đề chính thức |

Ngoài ra mỗi đề có file góp `DE0x-listening-full_exam.mp3` (Part 1 + Part 2
liền mạch, có lời chuyển phần) để thi thử trọn vẹn kỹ năng Listening.

## 3. Danh mục track

Chi tiết thời lượng, dung lượng, mã băm SHA-256 và giọng đọc của từng file được
lưu tự động trong [`manifest.json`](./manifest.json). Dưới đây là tóm tắt:

### Đề thi thử số 01 — `de01/`

| File | Nội dung | Thời lượng |
|---|---|---|
| `DE01-P1-housework-conversation_clean.mp3` | Hội thoại An & Mrs. Lan — việc nhà (182 từ) | ~62 giây |
| `DE01-P1-housework-conversation_slow.mp3` | Bản chậm | ~74 giây |
| `DE01-P1-housework-conversation_exam.mp3` | Bản chuẩn phòng thi (nghe 2 lần) | ~3 phút 15 |
| `DE01-P2-minh-khoa-radio-talk_clean.mp3` | Radio talk về thí sinh Minh Khoa (181 từ) | ~61 giây |
| `DE01-P2-minh-khoa-radio-talk_slow.mp3` | Bản chậm | ~72 giây |
| `DE01-P2-minh-khoa-radio-talk_exam.mp3` | Bản chuẩn phòng thi (nghe 2 lần) | ~3 phút 14 |
| `DE01-listening-full_exam.mp3` | Góp trọn Part 1 + Part 2 mô phỏng đề thi | ~6 phút 36 |

### Đề thi thử số 02 — `de02/`

*(Sẽ bổ sung trong phần công việc tiếp theo: 03 phiên bản cho Part 1 thông báo
Eco-Campus Fair và Part 2 phỏng vấn Dr. Hoang Minh, kèm file góp.)*

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
```

| Script | Vai trò |
|---|---|
| [`scripts/tts/tapescripts.py`](../../scripts/tts/tapescripts.py) | Nguyên văn 04 tapescripts, phân vai giọng & lời dẫn đề thi |
| [`scripts/tts/build_listening_audio.py`](../../scripts/tts/build_listening_audio.py) | Engine tổng hợp PCM, ghép khoảng lặng/tiếng bíp, chuẩn hóa âm lượng, mã hóa MP3 + ID3 |
| [`scripts/tts/download_models.sh`](../../scripts/tts/download_models.sh) | Tải & sắp xếp model Piper từ các repository nguồn |
| [`scripts/tts/verify_audio.py`](../../scripts/tts/verify_audio.py) | Tự động kiểm chứng toàn bộ track sau khi dựng |

## 5. Bản quyền & nguồn gốc model

- Văn bản tapescript thuộc tài liệu học tập trong repository này.
- Giọng đọc Piper là các mô hình nguồn mở do cộng đồng huấn luyện; giấy phép
  theo từng model (phổ biến là CC BY-NC-SA 4.0). Bộ audio này phục vụ **mục đích
  giáo dục phi thương mại**. Nguồn tải model được ghi rõ trong
  `scripts/tts/download_models.sh`.
- Mọi file MP3 gắn ID3 tag ghi rõ tên bài, danh sách giọng đọc và trích dẫn PDF
  nguồn để dễ truy vết.
