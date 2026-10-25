# Bộ sưu tập audio luyện nghe — Tiếng Anh 10 Global Success (GK1 2026–2027)

> **Phủ sóng 4/4 bài nghe chính thức** của `DE_CUONG_ON_TAP_TIENG_ANH_10_GK1_2026_2027_GLOBAL_SUCCESS.pdf` · 20/20 câu hỏi · 4/4 tapescript · 736 từ gốc.

## Cấu trúc thư mục

```text
listening/
├── PDF_LISTENING_AUDIT.md        # Báo cáo rà soát 35 trang PDF
├── AUDIO_SPEC.md                 # Chuẩn kỹ thuật MP3 & quy trình QA
├── AUDIO_QA_REPORT.md            # Báo cáo kiểm định (sinh ở bước cuối)
├── inventory.json                # 4 bài nghe, 20 câu, transcript, đáp án, nguồn trang
├── clips_manifest.json           # 37 clip TTS + 23 công thức track MP3
├── transcripts/                  # 4 transcript sạch (.txt)
├── questions/                    # 4 bộ câu hỏi + đáp án + bẫy thông tin (.md)
├── scripts/                      # audit, build, verify
└── audio/                        # 23 tệp MP3 + playlist
```

## Danh mục MP3

| Tệp | Mục đích |
|---|---|
| `exam/exam-01-part-01-exam.mp3` | Đề 1 · Part 1 – Exam mode (2 plays, timed pauses) |
| `clean/exam-01-part-01-clean.mp3` | Đề 1 · Part 1 – Clean recording (1 play, shadowing/dictation) |
| `guided/exam-01-part-01-guided.mp3` | Đề 1 · Part 1 – Guided study (questions, 2 plays, Vietnamese answer review) |
| `questions/exam-01-part-01-questions.mp3` | Đề 1 · Part 1 – Question preview (audio only) |
| `answers/exam-01-part-01-answers.mp3` | Đề 1 · Part 1 – Answer review (Vietnamese) |
| `exam/exam-01-part-02-exam.mp3` | Đề 1 · Part 2 – Exam mode (2 plays, timed pauses) |
| `clean/exam-01-part-02-clean.mp3` | Đề 1 · Part 2 – Clean recording (1 play, shadowing/dictation) |
| `guided/exam-01-part-02-guided.mp3` | Đề 1 · Part 2 – Guided study (questions, 2 plays, Vietnamese answer review) |
| `questions/exam-01-part-02-questions.mp3` | Đề 1 · Part 2 – Question preview (audio only) |
| `answers/exam-01-part-02-answers.mp3` | Đề 1 · Part 2 – Answer review (Vietnamese) |
| `exam/exam-02-part-01-exam.mp3` | Đề 2 · Part 1 – Exam mode (2 plays, timed pauses) |
| `clean/exam-02-part-01-clean.mp3` | Đề 2 · Part 1 – Clean recording (1 play, shadowing/dictation) |
| `guided/exam-02-part-01-guided.mp3` | Đề 2 · Part 1 – Guided study (questions, 2 plays, Vietnamese answer review) |
| `questions/exam-02-part-01-questions.mp3` | Đề 2 · Part 1 – Question preview (audio only) |
| `answers/exam-02-part-01-answers.mp3` | Đề 2 · Part 1 – Answer review (Vietnamese) |
| `exam/exam-02-part-02-exam.mp3` | Đề 2 · Part 2 – Exam mode (2 plays, timed pauses) |
| `clean/exam-02-part-02-clean.mp3` | Đề 2 · Part 2 – Clean recording (1 play, shadowing/dictation) |
| `guided/exam-02-part-02-guided.mp3` | Đề 2 · Part 2 – Guided study (questions, 2 plays, Vietnamese answer review) |
| `questions/exam-02-part-02-questions.mp3` | Đề 2 · Part 2 – Question preview (audio only) |
| `answers/exam-02-part-02-answers.mp3` | Đề 2 · Part 2 – Answer review (Vietnamese) |
| `full/mock-exam-01-listening-full.mp3` | Mock exam 01 – Full listening section (Part 1 + Part 2, 2 plays each) |
| `full/mock-exam-02-listening-full.mp3` | Mock exam 02 – Full listening section (Part 1 + Part 2, 2 plays each) |
| `strategy/00-orientation-and-strategy.mp3` | Orientation & official PDF listening strategy (Vietnamese) |

## Lộ trình luyện nghe khuyến nghị

1. `strategy/00-orientation-and-strategy.mp3` — nắm chiến thuật paraphrase và bẫy T/F.
2. `questions/...-questions.mp3` — đọc đề, gạch chân từ khóa trong 30 giây.
3. `exam/...-exam.mp3` — bấm giờ, nghe 2 lượt, tự làm 5 câu.
4. `answers/...-answers.mp3` — đối chiếu đáp án và giải thích tiếng Việt.
5. `guided/...-guided.mp3` — nghe lại có hướng dẫn, sửa lỗi sai.
6. `clean/...-clean.mp3` — nghe chép chính tả, nhại lại từng câu (shadowing).
7. `full/mock-exam-XX-listening-full.mp3` — thi thử trọn vẹn 10 câu/đề.

## Tái tạo

```bash
python -m pip install -r listening/requirements.txt
python listening/scripts/audit_and_build_inventory.py
# Sau khi có listening/clips/**.mp3 (TTS theo clips_manifest.json):
python listening/scripts/build_audio.py
python listening/scripts/verify_audio.py
```

`listening/clips/` là thư mục trung gian bị Git bỏ qua; các MP3 trong `listening/audio/` là sản phẩm cuối cùng được commit.
