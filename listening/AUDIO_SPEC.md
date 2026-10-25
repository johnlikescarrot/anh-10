# Đặc tả kỹ thuật bộ audio luyện nghe

## 1. Nguyên tắc biên tập

- **Không đổi một chữ nào** trong 4 tapescript của PDF. Mọi clip TTS được sinh từ `clips_manifest.json`, vốn được trích từ `src/part5_answer_keys.typ` và đối chiếu ngược với PDF trang 32–34.
- Hội thoại dùng **giọng riêng cho từng nhân vật**; độc thoại dùng giọng phát thanh/thông báo phù hợp; hướng dẫn & giải thích đáp án dùng tiếng Việt.
- Mỗi clip TTS có ≤ 1500 ký tự; clip dài nhất hiện tại: **1430 ký tự**.
- Tên tệp MP3 theo mẫu `exam-XX-part-YY-<mode>.mp3`; thư mục con thể hiện chế độ luyện tập.

## 2. Thông số file MP3 (chuẩn xuất bản)

| Thông số | Giá trị |
|---|---|
| Codec | MPEG-1 Layer III (`libmp3lame`) |
| Bitrate | 128 kbps CBR (speech-transparent, tối ưu dung lượng) |
| Sample rate | 44 100 Hz |
| Channels | Stereo (dual-mono từ nguồn TTS) |
| Loudness | `loudnorm I=-16 LUFS, TP=-1.5 dBTP, LRA=11` + `alimiter limit=0.95` |
| High-pass | 75 Hz để loại rumble |
| ID3 | ID3v2.3 UTF-8: title, album, artist, track, genre, year, comment, source pages, transcript `USLT` |
| Tín hiệu báo | Tone 880 Hz ở đầu, giữa 2 lượt nghe và cuối bản exam |
| Khoảng lặng | 0,38 s giữa lượt hội thoại; 0,85 s giữa đoạn độc thoại; 12 s + 10 s làm bài ở bản exam |

## 3. Các chế độ âm thanh

| Chế độ | Số file | Nội dung |
|---|---:|---|
| `exam/` | 4 | Chỉ dẫn + 2 lượt băng + thời gian làm bài, đúng tinh thần phòng thi. |
| `clean/` | 4 | Một lượt băng sạch, không chỉ dẫn: nghe chép chính tả & shadowing. |
| `guided/` | 4 | Câu hỏi → băng → giải thích đáp án tiếng Việt → băng lần 2. |
| `questions/` | 4 | Chỉ đọc 5 câu hỏi + phương án + từ khóa; luyện đọc đề trước khi nghe. |
| `answers/` | 4 | Chỉ giải thích đáp án tiếng Việt; dùng để chấm và sửa lỗi. |
| `full/` | 2 | Ghép Part 1 + Part 2 thành đúng một section Listening của mỗi đề. |
| `strategy/` | 1 | Hướng dẫn sử dụng + toàn bộ chiến thuật nghe trang 13. |
| **Tổng** | **23** | — |

## 4. Vai trò giọng nói

| Role | Ngôn ngữ | Vai |
|---|---|---|
| `adult_female` | en | Mrs. Lan; phát thanh viên Youth Spotlight |
| `teen_female` | en | An; Mai |
| `host_male` | en | Dẫn chương trình, đọc chỉ dẫn và câu hỏi |
| `guest_male` | en | Dr. Hoang Minh |
| `vi_guide` | vi | Chiến thuật & giải thích đáp án |

## 5. Kiểm định bắt buộc

`scripts/verify_audio.py` kiểm tra: đủ 23 MP3; đúng codec/bitrate/sample rate; không clipping; loudness nằm vùng chuẩn; ID3 có transcript; SHA-256 PDF không đổi; 4 transcript vẫn 180–200 từ; 20/20 câu hỏi có đáp án; mỗi bài có đủ 5 chế độ. Báo cáo được ghi ra `AUDIO_QA_REPORT.md`.
