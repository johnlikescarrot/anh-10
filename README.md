# Đề cương ôn tập Tiếng Anh 10 – Giữa học kỳ 1 (2026–2027)

Tài liệu ôn thi được biên soạn **trực tiếp từ** `2026_2027_MA TRẬN 10_GK1.docx` (Ma trận & Bảng đặc tả kỹ thuật đề kiểm tra giữa kỳ 1 – môn Tiếng Anh 10, năm học 2026–2027), bám sát sách **Tiếng Anh 10 – Global Success**, Unit 1 – 2 – 3.

## Sản phẩm chính

**`DE_CUONG_ON_TAP_TIENG_ANH_10_GK1_2026-2027.pdf`** – 68 trang, tiếng Việt, gồm 6 phần:

| Phần | Nội dung |
|---|---|
| 1 | Giải mã đề thi: cấu trúc 28 TN + 6 TL + 1 bài viết, trọng số 70/30, bản đồ 28 câu, chiến lược 60 phút, 10 bẫy thường gặp |
| 2 | Hệ thống kiến thức Unit 1 – 2 – 3: từ vựng theo cụm, phát âm, 5 chủ điểm ngữ pháp + cheat sheet |
| 3 | Kỹ năng & chiến thuật cho 8 dạng bài (True/False, MCQ, từ vựng, dạng từ, cloze, đọc hiểu, re-ordering, viết lại câu, viết đoạn) |
| 4 | Luyện tập theo từng dạng: 4 bài nghe (có transcript), 12 + 12 câu từ vựng, 16 câu ngữ pháp, 2 cloze, 2 bài đọc, 3 re-ordering, 12 viết lại câu, 3 đề viết đoạn có bài mẫu |
| 5 | 2 đề thi thử đúng cấu trúc, có dòng kẻ viết bài, đáp án + giải thích + bài viết mẫu + transcript |
| 6 | Đáp án tổng hợp, 40 cấu trúc viết lại câu, 120 từ vựng Anh–Việt, lịch ôn 10 ngày, bảng tự đánh giá |

## Cấu trúc mã nguồn

```
content/            Nội dung tài liệu (định dạng markup rút gọn, tiếng Việt)
  00_front.md       Mục lục, hướng dẫn sử dụng, lịch ôn
  10_part1.md       Phần 1 – Giải mã đề thi
  20..22_part2*.md  Phần 2 – Hệ thống kiến thức
  30_part3.md       Phần 3 – Kỹ năng và chiến thuật
  40..43_part4*.md  Phần 4 – Luyện tập theo từng dạng
  50..51_part5*.md  Phần 5 – Hai đề thi thử
  60_part6.md       Phần 6 – Tổng ôn và tự đánh giá
tools/build_pdf.py  Trình dựng PDF (ReportLab + DejaVu, hỗ trợ tiếng Việt)
tools/fonts/        Font DejaVu (giấy phép tự do) để bản dựng không phụ thuộc hệ thống
```

## Dựng lại PDF

```bash
python3 -m venv .venv
.venv/bin/pip install reportlab
.venv/bin/python tools/build_pdf.py
```

Kết quả ghi ra `DE_CUONG_ON_TAP_TIENG_ANH_10_GK1_2026-2027.pdf`.

### Cú pháp markup (tóm tắt)

`## / ### / ####` tiêu đề · `| a | b |` bảng · `> ` hộp ghi chú, `>!` cảnh báo, `>+` mẹo, `>#` công thức, `>.` ngữ liệu · `>> ` dải tiêu đề · `[[PART n|Tiêu đề|Mô tả|ý;ý]]` trang mở phần · `[[KEY 1C 2B …]]` bảng đáp án · `[[LINES n]]` dòng kẻ viết bài · `**đậm**`, `*nghiêng*`, `==highlight==`.

## Ghi chú về nguồn

- Toàn bộ tỉ lệ, số câu, dạng bài và mức độ nhận thức lấy từ file ma trận gốc; phần diễn giải (quy đổi điểm, bản đồ câu hỏi, chiến lược thời gian) được ghi rõ là suy ra từ văn bản.
- Ba điểm số liệu chưa khớp trong file ma trận gốc được nêu minh bạch ở mục 1.6 kèm cách xử lý khi ôn tập.
- Ngữ liệu nghe/đọc/đề thi thử do tài liệu tự biên soạn theo đúng chủ điểm, độ dài và định dạng mà bảng đặc tả yêu cầu.
