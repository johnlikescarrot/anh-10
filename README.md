# Đề cương ôn tập Tiếng Anh 10 – Giữa học kì 1 – 2026–2027

Tài liệu ôn thi được biên soạn **dựa trực tiếp trên ma trận và bản đặc tả** trong
[`2026_2027_MA TRẬN 10_GK1.docx`](2026_2027_MA%20TRẬN%2010_GK1.docx), bám sát
sách **Tiếng Anh 10 – Global Success** (Kết nối tri thức với cuộc sống), phạm vi
**Unit 1 – Unit 2 – Unit 3**.

## 📄 Sản phẩm chính

**[`DE_CUONG_ON_TAP_TIENG_ANH_10_GK1_2026-2027.pdf`](DE_CUONG_ON_TAP_TIENG_ANH_10_GK1_2026-2027.pdf)** — 46 trang, có mục lục và bookmark điều hướng.

## Nội dung

| Phần | Nội dung |
|---|---|
| **0** | Giải mã ma trận: cấu trúc đề, số câu – số điểm, đối chiếu số liệu, chiến lược 60 phút, 10 lỗi mất điểm oan, bài tự kiểm tra đầu vào, lộ trình ôn 7 ngày |
| **1** | Từ vựng 3 chủ điểm (Family Life / Humans and the Environment / Music): ~110 từ kèm phiên âm, nghĩa, cụm từ; bảng word family; từ dễ nhầm; 4 dạng bài tập có đáp án |
| **2** | 6 chuyên đề ngữ pháp theo bản đặc tả, mỗi chuyên đề có công thức – dấu hiệu – bẫy – bài tập: thì hiện tại, *will / be going to*, câu bị động, câu ghép, to-V / bare V; kèm bài kiểm tra tổng hợp 24 câu |
| **3** | Kỹ năng Nghe: quy trình 4 bước, 3 audio script (180–200 từ) + câu hỏi + đáp án + giải thích, 6 bẫy nghe |
| **4** | Kỹ năng Đọc: quy trình làm cloze, 2 bài cloze, 2 bài đọc hiểu 220–250 từ, dạng từ tham chiếu, kỹ thuật loại trừ đáp án |
| **5** | Kỹ năng Viết: sắp xếp câu, 5 công thức viết lại câu (20 câu có đáp án), khung viết đoạn 120–150 từ + 3 bài mẫu + thang điểm |
| **6** | **Đề minh họa đúng ma trận**: 28 câu TN + 6 câu TL + 1 bài viết, kèm đáp án, giải thích bẫy và audio script |
| **7** | Bảng tra cứu nhanh (5 nhóm ngữ pháp, 30 cụm từ, khung viết, phân bổ thời gian) |

## Cấu trúc kho

```
.
├── 2026_2027_MA TRẬN 10_GK1.docx   # ma trận gốc của trường (nguồn)
├── content/                         # nội dung nguồn (Markdown)
│   ├── 00_matrix_analysis.md
│   ├── 01_vocabulary.md
│   ├── 02_grammar.md
│   ├── 03_listening.md
│   ├── 04_reading.md
│   ├── 05_writing.md
│   ├── 06_mock_exam.md
│   └── 07_quick_reference.md
├── tools/build_pdf.py               # bộ dựng PDF (ReportLab)
└── DE_CUONG_ON_TAP_TIENG_ANH_10_GK1_2026-2027.pdf
```

## Dựng lại PDF

```bash
python3 -m venv .venv && . .venv/bin/activate
pip install reportlab

python tools/build_pdf.py content/*.md \
  -o "DE_CUONG_ON_TAP_TIENG_ANH_10_GK1_2026-2027.pdf"
```

Yêu cầu: Python 3.9+ và bộ font **DejaVu** (đường dẫn mặc định
`/usr/share/fonts/truetype/dejavu`). Bộ dựng tự tạo mục lục, bookmark PDF và
đánh số trang theo nội dung thực tế.

## Ghi chú về số liệu

Ma trận gốc ghi tỉ lệ phần **Vocabulary** là 15% nhưng chỉ có 4 câu. Tài liệu bám
theo **số câu và cấu trúc 70/30** (28 TN + 6 TL + 1 bài viết) vì bộ số này khớp
đồng thời giữa ma trận và bản đặc tả; phần phân tích chi tiết ở mục **0.3**.
