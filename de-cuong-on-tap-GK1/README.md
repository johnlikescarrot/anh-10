# Đề cương ôn tập GK1 - Tiếng Anh 10 (Global Success), 2026-2027

**Tài liệu chính:** [De_cuong_on_tap_GK1_TiengAnh10_2026-2027.pdf](De_cuong_on_tap_GK1_TiengAnh10_2026-2027.pdf)

## Nguồn và phương pháp

Đã đọc toàn bộ `2026_2027_MA TRẬN 10_GK1.docx`: 2 bảng gồm ma trận phân bố câu/điểm và bảng đặc tả yêu cầu cần đạt. Tài liệu bám sát phạm vi Unit 1-3 (Family life, Humans and the environment, Music), gồm:

- 2 bài nghe (mỗi bài 5 câu; transcript và đáp án ở cuối PDF);
- 2 câu từ vựng trắc nghiệm, 2 câu word form tự luận, 4 câu ngữ pháp trắc nghiệm;
- 5 câu cloze test, 5 câu đọc hiểu, 2 câu sắp xếp;
- 4 câu viết lại câu và 1 bài viết đoạn văn 120-150 từ.

Tổng cộng **28 câu trắc nghiệm = 7,0 điểm**, **6 câu tự luận + 1 đoạn văn = 3,0 điểm**. Nội dung đề thực hành là **tự biên soạn để luyện tập**, không phải đề thi chính thức hay trích từ sách giáo khoa.

### Các điểm cần lưu ý trong ma trận gốc

- Bảng ma trận ghi Listening 2 có 3 câu Biết + 2 câu Hiểu = **5 câu**. Bảng đặc tả lại có thêm một dòng tách rời ghi "1" TN cho Listening 2 nhưng không gắn yêu cầu cần đạt; tổng cuối bảng đặc tả vẫn là 28 câu TN. Tài liệu lấy tổng **5 câu** cho Listening 2 để nhất quán với cả tổng ma trận và tổng điểm (10 câu nghe = 2,5 điểm).
- Hàng Writing 1 ở bảng ma trận ghi 2 câu TN, 5% = 0,5 điểm; cột Tổng của hàng này lại có "3" dưới cột Hiểu dù hàng chi tiết ghi 0 câu Hiểu. Tài liệu theo hàng chi tiết và tỉ lệ 5%: **2 câu TN mức Biết**.
- Bảng đặc tả dùng "Close-text"; tài liệu dùng tên thông dụng **Cloze test** (đọc tờ rơi/quảng cáo điền từ).
- Listening 1 ghi "True/False hoặc dạng bài tương tự", Listening 2 ghi "MCQs hoặc dạng bài tương tự"; tài liệu chọn True/False và MCQ để đại diện mỗi dạng.
- Bảng gốc không quy định thời gian làm bài hay rubric chấm đoạn văn chi tiết. Mốc **45 phút** và rubric trong PDF là **gợi ý luyện tập**, không phải quy định của đơn vị ra đề.

## Tái tạo PDF

Yêu cầu: Python 3, `reportlab`, font DejaVu Sans tại `/usr/share/fonts/truetype/dejavu` (Linux). Tạo PDF:

```bash
python3 -m venv .venv
.venv/bin/pip install reportlab
.venv/bin/python build_pdf.py
```

Các tệp `content_review.py`, `content_exam.py`, `content_keys.py` là nguồn nội dung; `engine.py` lo dàn trang. PDF được lưu cùng thư mục.
