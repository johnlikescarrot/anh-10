# Báo cáo rà soát toàn bộ PDF — Phạm vi bài nghe

**Nguồn:** `DE_CUONG_ON_TAP_TIENG_ANH_10_GK1_2026_2027_GLOBAL_SUCCESS.pdf` · 35 trang · SHA-256 `c1f9a0fd777157f724beeaa88875d0c1e6d9a9126c6994afeac0a3873d8471f7` · rà soát lúc 2026-10-25 07:56 UTC.

## 1. Phương pháp rà soát

1. Trích xuất văn bản **toàn bộ 35 trang** bằng `pypdf` ở chế độ `layout`; lưu từng trang để đối chiếu.
2. Đọc metadata, 36 mục bookmark, 26 annotation điều hướng nội bộ; quét thô toàn bộ tệp PDF tìm `/EmbeddedFile`, `/Sound`, `/MediaClip`, `/RichMedia`, `/Screen`, `/Movie`, `/JavaScript`.
3. Đối chiếu chéo với **mã nguồn Typst gốc** (`src/part4_mock_exams.typ`, `src/part5_answer_keys.typ`) — văn bản hiển thị trong PDF được tạo từ chính mã nguồn này.
4. Đối chiếu với ma trận gốc `2026_2027_MA TRẬN 10_GK1.docx` (SHA-256 `4012ac5e5108a360721359e6c72276362382072662f55d1173abc8ec00ab11e3`), dòng 192–223: mỗi phần nghe là hội thoại/độc thoại ~1,5 phút, 180–200 từ, 5 câu, 1,25 điểm.
5. Tìm mọi cụm `Listen to`, `TAPESCRIPT`, `LISTENING`, `nghe`, `audio`, `radio`, `interview`, `Host:` để phát hiện bài nghe ẩn.
6. Kiểm định từng tapescript: số từ thực tế bằng cùng hàm đếm của `scripts/verify_and_build.py`; từng đoạn transcript và từng gốc câu hỏi phải khớp với văn bản PDF sau chuẩn hóa.

**Kết quả kỹ thuật:** PDF có `36` bookmark, `26` link nội bộ, **0** tệp đính kèm, **0** URI ngoài, **0** đối tượng âm thanh/video/JavaScript nhúng. Nói cách khác: PDF **chỉ có transcript**, mọi audio phải được tạo mới từ transcript chuẩn.

## 2. Toàn bộ bài tập nghe chính thức trong PDF

| ID | Đề / Part | Dạng | Trang câu hỏi | Trang tapescript | Số từ | Chủ đề | Người nói | Đáp án |
|---|---|---|---|---|---:|---|---|---|
| `exam-01-part-01` | Đề 1 / Part 1 | True/False | 24 | 32 | 182 | Unit 1 – Family Life | Mrs. Lan, An | A B A B A |
| `exam-01-part-02` | Đề 1 / Part 2 | MCQs | 24 | 32 | 181 | Unit 3 – Music | Radio presenter | B C B C C |
| `exam-02-part-01` | Đề 2 / Part 1 | True/False | 27 | 33 | 186 | Unit 2 – Humans and the Environment | Mai | A B A B A |
| `exam-02-part-02` | Đề 2 / Part 2 | MCQs | 27 | 34 | 187 | Unit 1 – Family Life | Host, Dr. Minh | B C A B B |

**Tổng số: 4 bài nghe / 20 câu hỏi / 736 từ transcript.** Không còn bài nghe chính thức nào khác trong 35 trang.

Chi tiết từng câu hỏi, phương án, đáp án, giải thích, từ khóa và bẫy thông tin nằm trong `questions/*.md`; transcript sạch nằm trong `transcripts/*.txt`; dữ liệu máy đọc được nằm trong `inventory.json`.

## 3. Những vị trí có chứa từ “LISTENING / nghe” nhưng KHÔNG phải bài tập nghe

| Trang | Nội dung | Kết luận |
|---|---|---|
| trang 1, 4–6 | Ma trận & phân tích điểm số LISTENING | Mô tả cấu trúc, không phải bài tập nghe. |
| trang 3 | Lộ trình 7 ngày, Ngày 6–7 | Hướng dẫn tự luyện đề, không có transcript riêng. |
| trang 13 | Chiến thuật Nghe (Paraphrase, bẫy T/F) | Lý thuyết chiến thuật, được đưa vào tệp strategy audio. |
| trang 8–11, 21–22, 26 | Từ 'nghe/listen' trong ví dụ ngữ pháp, reading, writing | Không phải chỉ dẫn 'Listen to...' và không có tapescript. |
| trang 30, 35 | Tiêu đề Part V & checklist | Chỉ mục/đối chiếu đáp án, không phải bài nghe. |

Việc rà soát này nhằm bảo đảm **không sót** bài nghe nào, đồng thời tránh đọc nhầm các ví dụ ngữ pháp/đọc hiểu thành bài nghe. Các nội dung chiến thuật vẫn được đưa vào audio hướng dẫn để bộ sưu tập phản ánh trọn vẹn tài liệu.

## 4. Chuẩn kỹ thuật suy ra từ ma trận & PDF

- Mỗi bài: 180–200 từ, ~1,5 phút, 5 câu × 0,25 điểm; 2 phần/đề = 10 câu = 2,50 điểm.
- Tổng 6 câu nhận diện thông tin chi tiết trực tiếp + 4 câu hiểu ý chính/thái độ/paraphrase (PDF trang 5–6).
- Chủ đề bắt buộc: Family Life, Humans and the Environment, Music (docx dòng 193–215). Toàn bộ 4 bài đều bám 3 Unit này.
- Matrix khuyến nghị 30 giây đọc câu hỏi trước khi băng chạy (PDF trang 6); bản `exam` vì thế phát **2 lượt** kèm 12 giây và 10 giây nghỉ giải quyết câu hỏi.
- Chiến thuật trang 13: paraphrase (`split chores equally ↔ share housework fairly`), cảnh giác `all, every, never, only, nobody, completely`, bẫy sửa thông tin ở câu sau.

## 5. Kết luận phủ sóng

`clips_manifest.json` sinh ra **37 clip TTS** và **23 tệp MP3** cho 4 bài nghe chính thức. Mỗi bài đều có ít nhất 5 định dạng: `exam`, `clean`, `guided`, `questions`, `answers`; cộng thêm 2 file thi nghe ghép và 1 file chiến thuật. Đây là phạm vi tối thiểu bắt buộc — các phần sau có thể bổ sung ngữ liệu luyện nghe mở rộng nhưng không được thay thế 4 bài gốc.
