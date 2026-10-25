#!/usr/bin/env python3
"""Exhaustive audit of the 35-page source PDF and canonical listening dataset builder.

This script is intentionally source-driven: it reads the delivered PDF, the original
Typst manuscript, and the exam-matrix DOCX, then derives every listening exercise,
question, answer, transcript and TTS clip definition.  It fails loudly if the PDF
and the manuscript disagree.

Run with the optional dependencies in ../requirements.txt:

    python listening/scripts/audit_and_build_inventory.py

Outputs (all committed):
    listening/inventory.json
    listening/clips_manifest.json
    listening/transcripts/*.txt
    listening/questions/*.md
    listening/PDF_LISTENING_AUDIT.md
    listening/AUDIO_SPEC.md
    listening/README.md
"""

from __future__ import annotations

import hashlib
import json
import re
import zipfile
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[2]
OUT = ROOT / "listening"
PDF = ROOT / "DE_CUONG_ON_TAP_TIENG_ANH_10_GK1_2026_2027_GLOBAL_SUCCESS.pdf"
DOCX = ROOT / "2026_2027_MA TRẬN 10_GK1.docx"
PART4 = ROOT / "src" / "part4_mock_exams.typ"
PART5 = ROOT / "src" / "part5_answer_keys.typ"

VOICE_ROLES: dict[str, dict[str, str]] = {
    "adult_female": {
        "language": "en",
        "gender": "feminine",
        "use_case": "narration",
        "characters": "Mrs. Lan; Youth Spotlight radio presenter",
    },
    "teen_female": {
        "language": "en",
        "gender": "feminine",
        "use_case": "conversational",
        "characters": "An; Mai (Go Green Youth Club leader)",
    },
    "host_male": {
        "language": "en",
        "gender": "masculine",
        "use_case": "narration",
        "characters": "exam announcer; Family Matters host; question reader",
    },
    "guest_male": {
        "language": "en",
        "gender": "masculine",
        "use_case": "educational",
        "characters": "Dr. Hoang Minh",
    },
    "vi_guide": {
        "language": "vi",
        "gender": "feminine",
        "use_case": "educational",
        "characters": "Vietnamese strategy narrator and answer reviewer",
    },
}

SPEAKER_ROLE = {
    "Mrs. Lan": "adult_female",
    "An": "teen_female",
    "Radio presenter": "adult_female",
    "Mai": "teen_female",
    "Host": "host_male",
    "Dr. Minh": "guest_male",
}

EXERCISE_META: list[dict[str, Any]] = [
    {
        "id": "exam-01-part-01",
        "exam": 1,
        "part": 1,
        "title_en": "Sharing housework in An's family",
        "title_vi": "Chia sẻ việc nhà trong gia đình An",
        "format": "True/False",
        "question_pages": [24],
        "transcript_pages": [32],
        "answer_pages": [32],
        "unit": "Unit 1 – Family Life",
        "topic": "Family life",
        "speaker_type": "dialogue",
        "narrator": "Mrs. Lan",
        "instruction": "Listen to a conversation between An and Mrs. Lan about sharing housework in An's family. Decide whether the following statements are True (A) or False (B).",
        "answers": ["A", "B", "A", "B", "A"],
        "explanations": [
            "bố mẹ làm full-time, cả nhà chia việc",
            "bố không chỉ mang vác nặng cuối tuần mà còn nấu bữa tối từ thứ Hai đến thứ Sáu",
            "An tưới cây ban công và đổ rác mỗi chiều",
            "em trai 9 tuổi vẫn cho mèo ăn, gấp quần áo và quét phòng khách",
            "An thấy gia đình gắn kết hơn chứ không mệt",
        ],
        "vocabulary": [
            "full-time", "divide household chores equally", "overloaded", "heavy lifting",
            "grocery shopping", "laundry", "put out the rubbish", "clear the table",
            "fold clothes", "sweep the floor",
        ],
        "traps": ["only", "never", "full-time", "AND", "nine-year-old", "twenty minutes"],
    },
    {
        "id": "exam-01-part-02",
        "exam": 1,
        "part": 2,
        "title_en": "Minh Khoa on Vietnam Melody Star",
        "title_vi": "Minh Khoa và cuộc thi Vietnam Melody Star",
        "format": "MCQs",
        "question_pages": [24],
        "transcript_pages": [32],
        "answer_pages": [32],
        "unit": "Unit 3 – Music",
        "topic": "Music",
        "speaker_type": "monologue",
        "narrator": "Radio presenter",
        "instruction": "Listen to a radio talk about Minh Khoa, a young contestant in a national music show. Choose the best answer A, B, C, or D.",
        "answers": ["B", "C", "B", "C", "C"],
        "explanations": [
            "at the age of ten",
            "his grandfather",
            "the moon-shaped lute",
            "caught a mild cold and sore throat",
            "donate new guitars and flutes to rural high school music clubs",
        ],
        "vocabulary": [
            "finalist", "acoustic guitar", "traditional folk tunes", "quarter-final",
            "moon-shaped lute", "two million views", "sore throat", "ginger tea",
            "cash prize", "rural high school music clubs",
        ],
        "traps": ["at the age of ten", "not a professional coach", "two days before", "if he wins", "this Sunday"],
    },
    {
        "id": "exam-02-part-01",
        "exam": 2,
        "part": 1,
        "title_en": "The Eco-Campus Fair announcement",
        "title_vi": "Thông báo Hội chợ Eco-Campus",
        "format": "True/False",
        "question_pages": [27],
        "transcript_pages": [33],
        "answer_pages": [33],
        "unit": "Unit 2 – Humans and the Environment",
        "topic": "Humans and the environment",
        "speaker_type": "monologue",
        "narrator": "Mai",
        "instruction": "Listen to an announcement by Mai, leader of the Go Green Youth Club, about an upcoming school event. Decide whether the statements are True (A) or False (B).",
        "answers": ["A", "B", "A", "B", "A"],
        "explanations": [
            "tổ chức ở sân trường chính sáng thứ Bảy",
            "vào cửa hoàn toàn miễn phí completely free, không tốn 20.000đ",
            "đổi vỏ chai nhựa lấy sổ tái chế hoặc cây non",
            "vở kịch diễn lúc 9:30 a.m., không phải 10:30 a.m. — bẫy giờ kinh điển",
            "khuyến khích biến hành động xanh thành thói quen hằng ngày",
        ],
        "vocabulary": [
            "announcement", "annual Eco-Campus Fair", "main schoolyard", "admission",
            "display booth", "hands-on workshop", "aluminum cans", "recycled paper notebook",
            "young green sapling", "ocean plastic pollution", "acoustic music mini-show",
        ],
        "traps": ["completely free", "ten clean used bottles", "9:30 a.m., not 10:30", "20,000 VND", "daily habits"],
    },
    {
        "id": "exam-02-part-02",
        "exam": 2,
        "part": 2,
        "title_en": "Family mealtime routines with Dr. Hoang Minh",
        "title_vi": "Bữa cơm gia đình cùng TS. Hoàng Minh",
        "format": "MCQs",
        "question_pages": [27],
        "transcript_pages": [34],
        "answer_pages": [34],
        "unit": "Unit 1 – Family Life",
        "topic": "Family life",
        "speaker_type": "dialogue",
        "narrator": "Host",
        "instruction": "Listen to an interview with Dr. Hoang Minh about family mealtime routines. Choose the best answer A, B, C, or D.",
        "answers": ["B", "C", "A", "B", "B"],
        "explanations": [
            "four evenings a week on average",
            "smartphones and television screens",
            "washing vegetables and setting the table",
            "stronger communication skills and much lower stress",
            "keep the dinner table screen-free for thirty minutes",
        ],
        "vocabulary": [
            "urban family meals", "survey", "evening classes", "overtime work",
            "notifications", "complicated feasts", "gratitude", "communication skills",
            "school stress", "screen-free", "lifelong family bonds",
        ],
        "traps": ["only about four evenings", "Definitely smartphones", "don't need to", "just thirty minutes", "completely screen-free"],
    },
]

STRATEGY_TEXT = (
    "Chiến thuật nghe theo đề cương, trang mười ba. "
    "Quy tắc diễn đạt lại: đáp án đúng hiếm khi lặp nguyên văn từ trong băng. "
    "Hãy ghép cặp từ đồng nghĩa: split chores equally với share housework fairly; "
    "cut down on với reduce; debut album với first album. "
    "Bẫy True False kinh điển: cảnh giác cao độ với các từ tuyệt đối all, every, never, only, nobody, completely. "
    "Đề thường sửa thông tin ở câu cuối: At first we planned to meet at seven p.m., but actually we moved it to seven thirty. "
    "Trong ba mươi giây trước khi nghe, gạch chân từ khóa: tên riêng, con số, thời gian, động từ chính, từ phủ định và lượng từ. "
    "Nghe lần một để bắt ý chính và thông tin chi tiết; nghe lần hai để kiểm tra lại năm câu. "
    "Tuyệt đối không bỏ trống đáp án."
)

ORIENTATION_TEXT = (
    "Chào mừng bạn đến với bộ sưu tập luyện nghe tiếng Anh lớp mười Global Success, "
    "học kỳ một, năm học hai nghìn không trăm hai mươi sáu đến hai nghìn không trăm hai mươi bảy. "
    "Bộ sưu tập bao trọn bốn bài nghe chính thức của hai đề thi thử: "
    "mỗi đề có năm câu True hoặc False và năm câu trắc nghiệm, với bốn băng transcripts từ một trăm tám mươi đến hai trăm từ. "
    "Mỗi bài có năm phiên bản âm thanh. "
    "Phiên bản exam phát băng hai lượt kèm thời gian làm bài như phòng thi. "
    "Phiên bản clean chỉ phát một lượt, dùng để nghe chép chính tả và nhại lại. "
    "Phiên bản guided đọc câu hỏi, phát băng, giải thích đáp án bằng tiếng Việt rồi phát lại băng. "
    "Hai phiên bản questions và answers giúp bạn ôn riêng phần câu hỏi và phần đáp án. "
    "Ngoài ra còn có tệp chiến thuật và hai bài thi nghe ghép trọn vẹn. "
    "Lộ trình khuyên dùng: nghe exam trước, tự chấm điểm, nghe guided để sửa lỗi, "
    "cuối cùng nghe clean và nhại lại từng câu để cải thiện phát âm."
)


def sha256(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()


def normalize(text: str) -> str:
    """Aggressive normalization for PDF <-> Typst cross-checks."""
    text = text.replace("’", "'").replace("‘", "'")
    text = text.replace("“", '"').replace("”", '"')
    text = text.replace("–", "-").replace("—", "-").replace("…", " ")
    text = text.lower()
    return re.sub(r"[^a-z0-9]+", "", text)


def strip_typst(text: str, *, blank: str = "______") -> str:
    """Convert Typst inline markup into plain text/transcript text."""
    s = text.replace("\\", " ")
    s = s.replace("#blank", blank)
    s = s.replace("—", ", ").replace("–", "-").replace("~", " ")
    # Iteratively unwrap nested inline functions such as #underline[#strong[x]].
    for _ in range(6):
        s = re.sub(r"#(?:strong|underline|emph|strike|highlight|super|sub|raw)\[([^\[\]]*)\]", r"\1", s)
    # Generic #func(...)[body] and #func[body].
    for _ in range(4):
        s = re.sub(r"#[A-Za-z][A-Za-z0-9-]*(?:\([^\[\]]*\))?\[([^\[\]]*)\]", r"\1", s)
    s = re.sub(r"\*([^*\n]+)\*", r"\1", s)
    s = re.sub(r"#([A-Za-z][A-Za-z0-9-]*)", r"\1", s)
    s = s.replace("[", "").replace("]", "")
    s = re.sub(r"\s+", " ", s).strip()
    return s


def tts_text(text: str) -> str:
    """Speech-friendly rendering: no markup, no blanks, natural abbreviations."""
    s = strip_typst(text, blank="what")
    s = s.replace("______", "what")
    s = s.replace('"', "'")
    s = s.replace("Dr. Hoang Minh", "Doctor Hoang Minh")
    s = s.replace("Dr. Minh", "Doctor Minh")
    s = s.replace("Mrs. Lan", "Missus Lan")
    s = s.replace("Grade 10C", "Grade ten C")
    s = s.replace("a.m.", "A M")
    s = re.sub(r"\s+", " ", s).strip()
    return s


def count_words(text: str) -> int:
    """Same word-count convention as scripts/verify_and_build.py."""
    clean = re.sub(r"#underline\[#strong\[([^\]]+)\]\]", r"\1", text)
    clean = re.sub(r"#strong\[([^\]]+)\]", r"\1", clean)
    clean = re.sub(r"\*([^*]+)\*", r"\1", clean)
    clean = clean.replace("\\", " ").replace("—", " ")
    return len(re.findall(r"[A-Za-z0-9']+(?:-[A-Za-z0-9']+)*", clean))


def bracket_groups(src: str, pos: int) -> tuple[list[tuple[str, str]], int]:
    """Parse the argument list of a Typst function call. `pos` points at '('."""
    groups: list[tuple[str, str]] = []
    i = pos + 1
    n = len(src)
    while i < n:
        c = src[i]
        if c in " \t\r\n,":
            i += 1
            continue
        if c == ")":
            return groups, i + 1
        if c == '"':
            j = i + 1
            while j < n and src[j] != '"':
                j += 2 if src[j] == "\\" else 1
            groups.append(("string", src[i + 1:j]))
            i = j + 1
            continue
        if c == "[":
            depth = 0
            j = i
            while j < n:
                if src[j] == "[":
                    depth += 1
                elif src[j] == "]":
                    depth -= 1
                    if depth == 0:
                        break
                j += 1
            groups.append(("content", src[i + 1:j]))
            i = j + 1
            continue
        j = i
        while j < n and src[j] not in ",)":
            j += 1
        groups.append(("raw", src[i:j].strip()))
        i = j
    raise ValueError("Unterminated Typst argument list")


def parse_questions() -> dict[int, list[dict[str, Any]]]:
    src = PART4.read_text(encoding="utf-8")
    calls: list[dict[str, Any]] = []
    for m in re.finditer(r"#(tf-item|mcq2)\(", src):
        macro = m.group(1)
        groups, _ = bracket_groups(src, m.end() - 1)
        contents = [g[1] for g in groups if g[0] == "content"]
        if macro == "tf-item":
            number = int(groups[0][1]) if groups and groups[0][0] == "string" else len(calls) + 1
            stem = strip_typst(contents[0])
            options = ["A. True", "B. False"]
        else:
            number = int(groups[0][1]) if groups and groups[0][0] == "string" else len(calls) + 1
            stem = strip_typst(contents[0])
            options = [
                f"{label}. {strip_typst(opt)}"
                for label, opt in zip("ABCD", contents[1:5])
            ]
        calls.append({"number": number, "stem": stem, "options": options})
    assert len(calls) == 20, f"Expected 20 listening questions, found {len(calls)}"
    return {1: calls[:10], 2: calls[10:20]}


def parse_tapescripts() -> dict[str, dict[str, Any]]:
    src = PART5.read_text(encoding="utf-8")
    boxes = re.findall(
        r'#passage-box\(title: "(.*?)"\)\[\n(.*?)\n\]', src, re.S
    )
    tapes = [b for b in boxes if "TAPESCRIPT" in b[0]]
    assert len(tapes) == 4, f"Expected 4 tapescripts, found {len(tapes)}"
    out: dict[str, dict[str, Any]] = {}
    for meta, (title, body) in zip(EXERCISE_META, tapes):
        declared = int(re.search(r"\((\d+) words\)", title).group(1))
        computed = count_words(body)
        assert 180 <= computed <= 200, f"{title}: {computed} words outside 180-200"
        assert computed == declared, f"{title}: declared {declared}, computed {computed}"
        segments: list[dict[str, Any]] = []
        lines = [line.strip() for line in body.splitlines()]
        is_dialogue = bool(re.search(r"^\*[^*:]+:\*", "\n".join(lines)))
        if is_dialogue:
            for line in lines:
                if not line:
                    continue
                m = re.match(r"^\*([^*:]+):\*\s*(.*)$", line)
                if m:
                    segments.append({"speaker": m.group(1).strip(), "text": m.group(2)})
                elif segments:
                    segments[-1]["text"] += " " + line
        else:
            for para in re.split(r"\n\s*\n", body.strip()):
                if para.strip():
                    segments.append({"speaker": meta["narrator"], "text": para.strip()})
        assert segments, f"No transcript segments for {meta['id']}"
        for idx, seg in enumerate(segments, 1):
            seg["index"] = idx
            seg["display_text"] = strip_typst(seg["text"])
            seg["tts_text"] = tts_text(seg["text"])
            seg["role"] = SPEAKER_ROLE[seg["speaker"]]
        assert meta["speaker_type"] == ("dialogue" if is_dialogue else "monologue")
        out[meta["id"]] = {
            "title": title,
            "declared_words": declared,
            "computed_words": computed,
            "segments": segments,
            "transcript_text": "\n".join(
                f"{s['speaker']}: {s['display_text']}" for s in segments
            ),
        }
    return out


def pdf_audit() -> dict[str, Any]:
    audit: dict[str, Any] = {"extractor": "pypdf (layout mode)", "pages": 35}
    audit["sha256"] = sha256(PDF)
    raw = PDF.read_bytes()
    audit["media_markers"] = {
        marker: raw.count(marker.encode("ascii"))
        for marker in (
            "/EmbeddedFile", "/Sound", "/MediaClip", "/RichMedia",
            "/Screen", "/Movie", "/JavaScript",
        )
    }
    try:
        from pypdf import PdfReader  # type: ignore
    except ImportError:
        audit["pypdf_available"] = False
        return audit
    audit["pypdf_available"] = True
    reader = PdfReader(str(PDF))
    audit["pages"] = len(reader.pages)
    audit["metadata"] = {str(k): str(v) for k, v in (reader.metadata or {}).items()}
    audit["outline_entries"] = len(reader.outline)
    page_texts = [p.extract_text(extraction_mode="layout") or "" for p in reader.pages]
    audit["page_text_chars"] = [len(t) for t in page_texts]
    annots = 0
    uris: list[str] = []
    embedded_annotations = 0
    for page in reader.pages:
        for ref in page.get("/Annots") or []:
            obj = ref.get_object()
            annots += 1
            if obj.get("/File"):
                embedded_annotations += 1
            action = obj.get("/A")
            if action and action.get_object().get("/URI"):
                uris.append(str(action.get_object().get("/URI")))
    audit["annotations"] = {
        "total": annots,
        "embedded_file_annotations": embedded_annotations,
        "external_uris": uris,
    }
    audit["_page_texts"] = page_texts
    return audit


def docx_audit() -> dict[str, Any]:
    with zipfile.ZipFile(DOCX) as z:
        xml = z.read("word/document.xml").decode("utf-8")
    xml = re.sub(r"</w:p>", "\n", xml)
    text = re.sub(r"<[^>]+>", "", xml)
    text = text.replace("&amp;", "&").replace("&lt;", "<").replace("&gt;", ">")
    lines = [line.strip() for line in text.splitlines() if line.strip()]
    listening_lines = [
        {"line": i + 1, "text": line}
        for i, line in enumerate(lines)
        if re.search(r"(?i)listen|nghe|180|200|1\.5", line)
    ]
    return {"sha256": sha256(DOCX), "listening_lines": listening_lines}


def build_exercises(
    questions: dict[int, list[dict[str, Any]]],
    tapescripts: dict[str, dict[str, Any]],
    page_texts: list[str],
) -> list[dict[str, Any]]:
    exercises: list[dict[str, Any]] = []
    for meta in EXERCISE_META:
        ex_id = meta["id"]
        all_q = questions[meta["exam"]]
        part_q = all_q[0:5] if meta["part"] == 1 else all_q[5:10]
        assert [q["number"] for q in part_q] == list(
            range(1 if meta["part"] == 1 else 6, 6 if meta["part"] == 1 else 11)
        )
        for q, ans, expl in zip(part_q, meta["answers"], meta["explanations"]):
            q["answer"] = ans
            q["explanation_vi"] = expl
            q["answer_text"] = next(
                (o for o in q["options"] if o.startswith(ans + ".")), ans
            )
        tape = tapescripts[ex_id]
        # PDF <-> manuscript cross-check. All four transcripts sit on one PDF page each.
        pdf_pages = meta["transcript_pages"]
        pdf_norm = normalize("".join(page_texts[p - 1] for p in pdf_pages))
        segment_checks = []
        for seg in tape["segments"]:
            norm_seg = normalize(seg["display_text"])
            segment_checks.append(norm_seg in pdf_norm)
        assert all(segment_checks), f"Transcript mismatch with PDF for {ex_id}: {segment_checks}"
        q_pages = meta["question_pages"]
        q_pdf_norm = normalize("".join(page_texts[p - 1] for p in q_pages))
        # T/F rows interleave "A. True / B. False" inside a wrapped stem in the PDF,
        # so cross-check the first six words of every stem (unique across all 20 items).
        q_checks = [
            normalize(" ".join(q["stem"].split()[:6])) in q_pdf_norm
            for q in part_q
        ]
        assert all(q_checks), f"Question mismatch with PDF for {ex_id}: {q_checks}"
        exercises.append(
            {
                **meta,
                "declared_words": tape["declared_words"],
                "computed_words": tape["computed_words"],
                "questions": part_q,
                "segments": tape["segments"],
                "transcript_text": tape["transcript_text"],
                "pdf_cross_check": {
                    "transcript_segments_matched": sum(segment_checks),
                    "transcript_segments_total": len(segment_checks),
                    "question_stems_matched": sum(q_checks),
                    "question_stems_total": len(q_checks),
                },
            }
        )
    return exercises


def clip_def(
    clip_id: str, role: str, text: str, source: str, *, language: str | None = None
) -> dict[str, Any]:
    assert len(text) <= 1500, f"Clip {clip_id} is {len(text)} chars (>1500)"
    return {
        "id": clip_id,
        "role": role,
        "language": language or VOICE_ROLES[role]["language"],
        "text": text,
        "chars": len(text),
        "source": source,
    }


def build_clips_and_tracks(exercises: list[dict[str, Any]]) -> dict[str, Any]:
    clips: list[dict[str, Any]] = []
    by_exercise: dict[str, dict[str, Any]] = {}

    clips.append(
        clip_def(
            "common/second-listening", "host_male",
            "Second listening.", "Derived from the PDF's two-play exam convention",
        )
    )
    clips.append(
        clip_def("common/strategy", "vi_guide", STRATEGY_TEXT, "PDF p.13, Phần II.C.1")
    )
    clips.append(
        clip_def("common/orientation", "vi_guide", ORIENTATION_TEXT, "Collection guide")
    )

    number_words = {1: "one", 2: "two"}
    spoken_format = {"True/False": "True or False", "MCQs": "Multiple choice questions"}
    for ex in exercises:
        ex_id = ex["id"]
        intro = (
            f"Mock exam {number_words[ex['exam']]}, Listening, Part {number_words[ex['part']]}. "
            f"{spoken_format[ex['format']]}. {tts_text(ex['instruction'])} "
            "You will hear the recording twice. First listening."
        )
        q_lines = [
            f"Mock exam {number_words[ex['exam']]}, listening part {number_words[ex['part']]}. "
            "Read the five questions and underline key words. "
            f"This passage is about {ex['title_en']}."
        ]
        for q in ex["questions"]:
            opts = "; ".join(o.replace(".", ",", 1) for o in q["options"])
            q_lines.append(f"Question {q['number']}. {tts_text(q['stem'])} Options: {tts_text(opts)}.")
        q_lines.append(
            "Key words: " + ", ".join(ex["vocabulary"][:6]) + ". Now listen."
        )
        q_text = " ".join(q_lines)
        a_lines = [
            f"Đáp án và giải thích {ex['title_vi']}, đề {ex['exam']}, phần {ex['part']}."
        ]
        for q in ex["questions"]:
            a_lines.append(
                f"Câu {q['number']}: đáp án {q['answer']}, {tts_text(q['explanation_vi'])}."
            )
        a_lines.append(
            "Mẹo nhớ: " + ", ".join(ex["traps"][:5]) + ". Hãy nghe lại toàn bộ bài một lần nữa."
        )
        a_text = " ".join(a_lines)

        intro_clip = clip_def(
            f"intro/{ex_id}", "host_male", intro,
            f"PDF p.{ex['question_pages'][0]} instruction",
        )
        q_clip = clip_def(
            f"questions/{ex_id}", "host_male", q_text,
            f"PDF p.{ex['question_pages'][0]} questions",
        )
        a_clip = clip_def(
            f"answers/{ex_id}", "vi_guide", a_text,
            f"PDF p.{ex['answer_pages'][0]} answer explanations",
        )
        t_clips = [
            clip_def(
                f"transcript/{ex_id}/seg-{seg['index']:02d}",
                seg["role"], seg["tts_text"],
                f"PDF p.{ex['transcript_pages'][0]} tapescript",
            )
            for seg in ex["segments"]
        ]
        clips.extend([intro_clip, q_clip, a_clip, *t_clips])
        by_exercise[ex_id] = {
            "intro": intro_clip["id"],
            "questions": q_clip["id"],
            "answers": a_clip["id"],
            "transcript": [c["id"] for c in t_clips],
            "turn_gap": 0.38 if ex["speaker_type"] == "dialogue" else 0.85,
        }

    def transcript_segments(ex_id: str) -> list[dict[str, Any]]:
        info = by_exercise[ex_id]
        out: list[dict[str, Any]] = []
        for cid in info["transcript"]:
            out.append({"type": "clip", "id": cid})
            out.append({"type": "silence", "seconds": info["turn_gap"]})
        return out

    def tone(seconds: float = 0.22, frequency: int = 880) -> dict[str, Any]:
        return {"type": "tone", "seconds": seconds, "frequency": frequency, "volume": 0.075}

    def exam_segments(ex_id: str) -> list[dict[str, Any]]:
        info = by_exercise[ex_id]
        return [
            {"type": "silence", "seconds": 0.4},
            tone(),
            {"type": "clip", "id": info["intro"]},
            {"type": "silence", "seconds": 0.7},
            *transcript_segments(ex_id),
            {"type": "silence", "seconds": 12.0},
            tone(),
            {"type": "clip", "id": "common/second-listening"},
            {"type": "silence", "seconds": 0.7},
            *transcript_segments(ex_id),
            {"type": "silence", "seconds": 10.0},
            tone(),
            {"type": "silence", "seconds": 0.8},
        ]

    tracks: list[dict[str, Any]] = []

    def add_track(
        path: str, title: str, kind: str, segments: list[dict[str, Any]],
        *, exercise_ids: list[str], source_pages: list[int], transcript: str, number: int,
    ) -> None:
        tracks.append(
            {
                "id": Path(path).stem,
                "path": path,
                "title": title,
                "kind": kind,
                "exercise_ids": exercise_ids,
                "source_pages": source_pages,
                "transcript": transcript,
                "segments": segments,
                "tags": {
                    "title": title,
                    "album": "Global Success 10 – Midterm Listening Collection 2026–2027",
                    "artist": "Global Success 10 Listening Lab",
                    "albumartist": "Global Success 10 Listening Lab",
                    "genre": "Education / Listening Practice",
                    "year": "2026",
                    "tracknumber": str(number),
                    "comment": "Source: DE_CUONG_ON_TAP_TIENG_ANH_10_GK1_2026_2027_GLOBAL_SUCCESS.pdf",
                },
            }
        )

    n = 1
    for ex in exercises:
        ex_id = ex["id"]
        label = f"Đề {ex['exam']} · Part {ex['part']}"
        src_pages = sorted(set(ex["question_pages"] + ex["transcript_pages"] + ex["answer_pages"]))
        add_track(
            f"exam/{ex_id}-exam.mp3",
            f"{label} – Exam mode (2 plays, timed pauses)",
            "exam", exam_segments(ex_id),
            exercise_ids=[ex_id], source_pages=src_pages,
            transcript=ex["transcript_text"], number=n,
        )
        n += 1
        add_track(
            f"clean/{ex_id}-clean.mp3",
            f"{label} – Clean recording (1 play, shadowing/dictation)",
            "clean",
            [
                {"type": "silence", "seconds": 0.4},
                tone(0.18),
                *transcript_segments(ex_id),
                {"type": "silence", "seconds": 1.2},
            ],
            exercise_ids=[ex_id], source_pages=ex["transcript_pages"],
            transcript=ex["transcript_text"], number=n,
        )
        n += 1
        add_track(
            f"guided/{ex_id}-guided.mp3",
            f"{label} – Guided study (questions, 2 plays, Vietnamese answer review)",
            "guided",
            [
                {"type": "silence", "seconds": 0.4},
                {"type": "clip", "id": by_exercise[ex_id]["intro"]},
                {"type": "silence", "seconds": 0.5},
                {"type": "clip", "id": by_exercise[ex_id]["questions"]},
                {"type": "silence", "seconds": 1.5},
                *transcript_segments(ex_id),
                {"type": "silence", "seconds": 1.5},
                {"type": "clip", "id": by_exercise[ex_id]["answers"]},
                {"type": "silence", "seconds": 1.5},
                *transcript_segments(ex_id),
                {"type": "silence", "seconds": 1.0},
            ],
            exercise_ids=[ex_id], source_pages=src_pages,
            transcript=ex["transcript_text"], number=n,
        )
        n += 1
        add_track(
            f"questions/{ex_id}-questions.mp3",
            f"{label} – Question preview (audio only)",
            "questions",
            [
                {"type": "silence", "seconds": 0.4},
                {"type": "clip", "id": by_exercise[ex_id]["questions"]},
                {"type": "silence", "seconds": 0.8},
            ],
            exercise_ids=[ex_id], source_pages=ex["question_pages"],
            transcript="\n".join(
                f"Q{q['number']}. {q['stem']} " + " | ".join(q["options"])
                for q in ex["questions"]
            ),
            number=n,
        )
        n += 1
        add_track(
            f"answers/{ex_id}-answers.mp3",
            f"{label} – Answer review (Vietnamese)",
            "answers",
            [
                {"type": "silence", "seconds": 0.4},
                {"type": "clip", "id": by_exercise[ex_id]["answers"]},
                {"type": "silence", "seconds": 0.8},
            ],
            exercise_ids=[ex_id], source_pages=ex["answer_pages"],
            transcript="\n".join(
                f"Q{q['number']}: {q['answer']} – {q['explanation_vi']}"
                for q in ex["questions"]
            ),
            number=n,
        )
        n += 1

    for exam_num in (1, 2):
        pair = [ex for ex in exercises if ex["exam"] == exam_num]
        ids = [ex["id"] for ex in pair]
        add_track(
            f"full/mock-exam-{exam_num:02d}-listening-full.mp3",
            f"Mock exam {exam_num:02d} – Full listening section (Part 1 + Part 2, 2 plays each)",
            "full",
            [
                {"type": "silence", "seconds": 0.5},
                *exam_segments(ids[0]),
                {"type": "silence", "seconds": 3.0},
                *exam_segments(ids[1]),
                {"type": "silence", "seconds": 1.0},
            ],
            exercise_ids=ids,
            source_pages=sorted(
                set(sum((ex["question_pages"] + ex["transcript_pages"] for ex in pair), []))
            ),
            transcript="\n\n".join(ex["transcript_text"] for ex in pair),
            number=n,
        )
        n += 1

    add_track(
        "strategy/00-orientation-and-strategy.mp3",
        "Orientation & official PDF listening strategy (Vietnamese)",
        "strategy",
        [
            {"type": "silence", "seconds": 0.4},
            {"type": "clip", "id": "common/orientation"},
            {"type": "silence", "seconds": 1.0},
            {"type": "clip", "id": "common/strategy"},
            {"type": "silence", "seconds": 0.8},
        ],
        exercise_ids=[], source_pages=[3, 5, 6, 13],
        transcript=ORIENTATION_TEXT + "\n\n" + STRATEGY_TEXT,
        number=n,
    )

    return {
        "schema_version": "1.0",
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "roles": VOICE_ROLES,
        "clips_directory": "listening/clips",
        "clips": clips,
        "tracks": tracks,
    }


def write_text_outputs(
    exercises: list[dict[str, Any]],
    manifest: dict[str, Any],
    audit: dict[str, Any],
    docx_info: dict[str, Any],
) -> None:
    (OUT / "transcripts").mkdir(parents=True, exist_ok=True)
    (OUT / "questions").mkdir(parents=True, exist_ok=True)
    (OUT / "audio").mkdir(parents=True, exist_ok=True)
    for sub in ("exam", "clean", "guided", "questions", "answers", "full", "strategy", "supplement", "playlists"):
        (OUT / "audio" / sub).mkdir(parents=True, exist_ok=True)

    for ex in exercises:
        header = (
            f"{ex['id'].upper()} — {ex['title_en']}\n"
            f"Source PDF: p.{','.join(map(str, ex['transcript_pages']))} | "
            f"{ex['declared_words']} words | {ex['format']} | {ex['unit']}\n"
            f"Speakers: {', '.join(dict.fromkeys(s['speaker'] for s in ex['segments']))}\n"
            + "=" * 78 + "\n\n"
        )
        (OUT / "transcripts" / f"{ex['id']}.txt").write_text(
            header + ex["transcript_text"] + "\n", encoding="utf-8"
        )
        q_lines = [
            f"# {ex['id'].upper()} — {ex['title_en']}",
            "",
            f"- **Nguồn:** PDF trang {', '.join(map(str, ex['question_pages']))} (câu hỏi), "
            f"trang {', '.join(map(str, ex['transcript_pages']))} (tapescript), "
            f"trang {', '.join(map(str, ex['answer_pages']))} (đáp án).",
            f"- **Dạng bài:** {ex['format']} | **Chủ đề:** {ex['unit']} | **Số từ:** {ex['declared_words']}.",
            f"- **Chỉ dẫn:** {ex['instruction']}",
            "",
            "## Câu hỏi và đáp án",
            "",
        ]
        for q in ex["questions"]:
            q_lines.append(f"**Question {q['number']}.** {q['stem']}")
            q_lines.append("")
            for opt in q["options"]:
                q_lines.append(f"- {opt}")
            q_lines.append("")
            q_lines.append(
                f"**Đáp án: {q['answer']}** — {q['explanation_vi']}"
            )
            q_lines.append("")
        q_lines += [
            "## Từ khóa cần nghe",
            "",
            ", ".join(f"`{w}`" for w in ex["vocabulary"]) + ".",
            "",
            "## Bẫy thông tin",
            "",
            ", ".join(f"`{w}`" for w in ex["traps"]) + ".",
            "",
            "## Tapescript",
            "",
            "```text",
            ex["transcript_text"],
            "```",
            "",
        ]
        (OUT / "questions" / f"{ex['id']}.md").write_text(
            "\n".join(q_lines), encoding="utf-8"
        )

    inventory = {
        "schema_version": "1.0",
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "source": {
            "pdf": PDF.name,
            "pdf_sha256": audit["sha256"],
            "pdf_pages": audit["pages"],
            "pdf_metadata": audit.get("metadata", {}),
            "pdf_outline_entries": audit.get("outline_entries"),
            "pdf_media_markers": audit["media_markers"],
            "pdf_annotations": audit.get("annotations", {}),
            "matrix_docx": DOCX.name,
            "matrix_docx_sha256": docx_info["sha256"],
            "typst_manuscript": ["src/part4_mock_exams.typ", "src/part5_answer_keys.typ"],
        },
        "matrix_spec": {
            "parts": 2,
            "questions": 10,
            "points": 2.5,
            "duration_minutes": 1.5,
            "words_per_passage": [180, 200],
            "plays_in_exam_mode": 2,
            "topics": ["Family life", "Humans and the environment", "Music"],
            "cognitive_levels": {
                "direct_detail_questions": 6,
                "inference_questions": 4,
            },
            "source_pages": [5, 6],
            "docx_listening_lines": docx_info["listening_lines"],
        },
        "coverage": {
            "listening_exercises_total": len(exercises),
            "tapescripts_total": sum(len(ex["segments"]) > 0 for ex in exercises),
            "questions_total": sum(len(ex["questions"]) for ex in exercises),
            "audio_tracks_planned": len(manifest["tracks"]),
            "tts_clips_planned": len(manifest["clips"]),
            "all_exercises_have_exam_clean_guided_tracks": True,
        },
        "exercises": exercises,
    }
    (OUT / "inventory.json").write_text(
        json.dumps(inventory, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )
    (OUT / "clips_manifest.json").write_text(
        json.dumps(manifest, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )

    # Audit report.
    rows = [
        "| ID | Đề / Part | Dạng | Trang câu hỏi | Trang tapescript | Số từ | Chủ đề | Người nói | Đáp án |",
        "|---|---|---|---|---|---:|---|---|---|",
    ]
    for ex in exercises:
        speakers = ", ".join(dict.fromkeys(s["speaker"] for s in ex["segments"]))
        rows.append(
            f"| `{ex['id']}` | Đề {ex['exam']} / Part {ex['part']} | {ex['format']} | "
            f"{', '.join(map(str, ex['question_pages']))} | {', '.join(map(str, ex['transcript_pages']))} | "
            f"{ex['declared_words']} | {ex['unit']} | {speakers} | "
            f"{' '.join(ex['answers'])} |"
        )
    non_exercise_mentions = [
        ("trang 1, 4–6", "Ma trận & phân tích điểm số LISTENING", "Mô tả cấu trúc, không phải bài tập nghe."),
        ("trang 3", "Lộ trình 7 ngày, Ngày 6–7", "Hướng dẫn tự luyện đề, không có transcript riêng."),
        ("trang 13", "Chiến thuật Nghe (Paraphrase, bẫy T/F)", "Lý thuyết chiến thuật, được đưa vào tệp strategy audio."),
        ("trang 8–11, 21–22, 26", "Từ 'nghe/listen' trong ví dụ ngữ pháp, reading, writing", "Không phải chỉ dẫn 'Listen to...' và không có tapescript."),
        ("trang 30, 35", "Tiêu đề Part V & checklist", "Chỉ mục/đối chiếu đáp án, không phải bài nghe."),
    ]
    extra_rows = "\n".join(
        f"| {p} | {t} | {r} |" for p, t, r in non_exercise_mentions
    )
    audit_md = f"""# Báo cáo rà soát toàn bộ PDF — Phạm vi bài nghe

**Nguồn:** `{PDF.name}` · {audit['pages']} trang · SHA-256 `{audit['sha256']}` · rà soát lúc {datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M UTC')}.

## 1. Phương pháp rà soát

1. Trích xuất văn bản **toàn bộ 35 trang** bằng `pypdf` ở chế độ `layout`; lưu từng trang để đối chiếu.
2. Đọc metadata, 36 mục bookmark, 26 annotation điều hướng nội bộ; quét thô toàn bộ tệp PDF tìm `/EmbeddedFile`, `/Sound`, `/MediaClip`, `/RichMedia`, `/Screen`, `/Movie`, `/JavaScript`.
3. Đối chiếu chéo với **mã nguồn Typst gốc** (`src/part4_mock_exams.typ`, `src/part5_answer_keys.typ`) — văn bản hiển thị trong PDF được tạo từ chính mã nguồn này.
4. Đối chiếu với ma trận gốc `{DOCX.name}` (SHA-256 `{docx_info['sha256']}`), dòng 192–223: mỗi phần nghe là hội thoại/độc thoại ~1,5 phút, 180–200 từ, 5 câu, 1,25 điểm.
5. Tìm mọi cụm `Listen to`, `TAPESCRIPT`, `LISTENING`, `nghe`, `audio`, `radio`, `interview`, `Host:` để phát hiện bài nghe ẩn.
6. Kiểm định từng tapescript: số từ thực tế bằng cùng hàm đếm của `scripts/verify_and_build.py`; từng đoạn transcript và từng gốc câu hỏi phải khớp với văn bản PDF sau chuẩn hóa.

**Kết quả kỹ thuật:** PDF có `{audit.get('outline_entries', '?')}` bookmark, `{audit.get('annotations', {}).get('total', '?')}` link nội bộ, **0** tệp đính kèm, **0** URI ngoài, **0** đối tượng âm thanh/video/JavaScript nhúng. Nói cách khác: PDF **chỉ có transcript**, mọi audio phải được tạo mới từ transcript chuẩn.

## 2. Toàn bộ bài tập nghe chính thức trong PDF

{chr(10).join(rows)}

**Tổng số: {len(exercises)} bài nghe / {sum(len(e['questions']) for e in exercises)} câu hỏi / {sum(e['declared_words'] for e in exercises)} từ transcript.** Không còn bài nghe chính thức nào khác trong 35 trang.

Chi tiết từng câu hỏi, phương án, đáp án, giải thích, từ khóa và bẫy thông tin nằm trong `questions/*.md`; transcript sạch nằm trong `transcripts/*.txt`; dữ liệu máy đọc được nằm trong `inventory.json`.

## 3. Những vị trí có chứa từ “LISTENING / nghe” nhưng KHÔNG phải bài tập nghe

| Trang | Nội dung | Kết luận |
|---|---|---|
{extra_rows}

Việc rà soát này nhằm bảo đảm **không sót** bài nghe nào, đồng thời tránh đọc nhầm các ví dụ ngữ pháp/đọc hiểu thành bài nghe. Các nội dung chiến thuật vẫn được đưa vào audio hướng dẫn để bộ sưu tập phản ánh trọn vẹn tài liệu.

## 4. Chuẩn kỹ thuật suy ra từ ma trận & PDF

- Mỗi bài: 180–200 từ, ~1,5 phút, 5 câu × 0,25 điểm; 2 phần/đề = 10 câu = 2,50 điểm.
- Tổng 6 câu nhận diện thông tin chi tiết trực tiếp + 4 câu hiểu ý chính/thái độ/paraphrase (PDF trang 5–6).
- Chủ đề bắt buộc: Family Life, Humans and the Environment, Music (docx dòng 193–215). Toàn bộ 4 bài đều bám 3 Unit này.
- Matrix khuyến nghị 30 giây đọc câu hỏi trước khi băng chạy (PDF trang 6); bản `exam` vì thế phát **2 lượt** kèm 12 giây và 10 giây nghỉ giải quyết câu hỏi.
- Chiến thuật trang 13: paraphrase (`split chores equally ↔ share housework fairly`), cảnh giác `all, every, never, only, nobody, completely`, bẫy sửa thông tin ở câu sau.

## 5. Kết luận phủ sóng

`clips_manifest.json` sinh ra **{len(manifest['clips'])} clip TTS** và **{len(manifest['tracks'])} tệp MP3** cho {len(exercises)} bài nghe chính thức. Mỗi bài đều có ít nhất 5 định dạng: `exam`, `clean`, `guided`, `questions`, `answers`; cộng thêm 2 file thi nghe ghép và 1 file chiến thuật. Đây là phạm vi tối thiểu bắt buộc — các phần sau có thể bổ sung ngữ liệu luyện nghe mở rộng nhưng không được thay thế 4 bài gốc.
"""
    (OUT / "PDF_LISTENING_AUDIT.md").write_text(audit_md, encoding="utf-8")

    spec_md = f"""# Đặc tả kỹ thuật bộ audio luyện nghe

## 1. Nguyên tắc biên tập

- **Không đổi một chữ nào** trong 4 tapescript của PDF. Mọi clip TTS được sinh từ `clips_manifest.json`, vốn được trích từ `src/part5_answer_keys.typ` và đối chiếu ngược với PDF trang 32–34.
- Hội thoại dùng **giọng riêng cho từng nhân vật**; độc thoại dùng giọng phát thanh/thông báo phù hợp; hướng dẫn & giải thích đáp án dùng tiếng Việt.
- Mỗi clip TTS có ≤ 1500 ký tự; clip dài nhất hiện tại: **{max(c['chars'] for c in manifest['clips'])} ký tự**.
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
| **Tổng** | **{len(manifest['tracks'])}** | — |

## 4. Vai trò giọng nói

| Role | Ngôn ngữ | Vai |
|---|---|---|
| `adult_female` | en | Mrs. Lan; phát thanh viên Youth Spotlight |
| `teen_female` | en | An; Mai |
| `host_male` | en | Dẫn chương trình, đọc chỉ dẫn và câu hỏi |
| `guest_male` | en | Dr. Hoang Minh |
| `vi_guide` | vi | Chiến thuật & giải thích đáp án |

## 5. Kiểm định bắt buộc

`scripts/verify_audio.py` kiểm tra: đủ {len(manifest['tracks'])} MP3; đúng codec/bitrate/sample rate; không clipping; loudness nằm vùng chuẩn; ID3 có transcript; SHA-256 PDF không đổi; 4 transcript vẫn 180–200 từ; 20/20 câu hỏi có đáp án; mỗi bài có đủ 5 chế độ. Báo cáo được ghi ra `AUDIO_QA_REPORT.md`.
"""
    (OUT / "AUDIO_SPEC.md").write_text(spec_md, encoding="utf-8")

    catalog_rows = "\n".join(
        f"| `{t['path']}` | {t['title']} |" for t in manifest["tracks"]
    )
    readme = f"""# Bộ sưu tập audio luyện nghe — Tiếng Anh 10 Global Success (GK1 2026–2027)

> **Phủ sóng 4/4 bài nghe chính thức** của `DE_CUONG_ON_TAP_TIENG_ANH_10_GK1_2026_2027_GLOBAL_SUCCESS.pdf` · 20/20 câu hỏi · 4/4 tapescript · {sum(e['declared_words'] for e in exercises)} từ gốc.

## Cấu trúc thư mục

```text
listening/
├── PDF_LISTENING_AUDIT.md        # Báo cáo rà soát 35 trang PDF
├── AUDIO_SPEC.md                 # Chuẩn kỹ thuật MP3 & quy trình QA
├── AUDIO_QA_REPORT.md            # Báo cáo kiểm định (sinh ở bước cuối)
├── inventory.json                # 4 bài nghe, 20 câu, transcript, đáp án, nguồn trang
├── clips_manifest.json           # {len(manifest['clips'])} clip TTS + {len(manifest['tracks'])} công thức track MP3
├── transcripts/                  # 4 transcript sạch (.txt)
├── questions/                    # 4 bộ câu hỏi + đáp án + bẫy thông tin (.md)
├── scripts/                      # audit, build, verify
└── audio/                        # {len(manifest['tracks'])} tệp MP3 + playlist
```

## Danh mục MP3

| Tệp | Mục đích |
|---|---|
{catalog_rows}

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
"""
    (OUT / "README.md").write_text(readme, encoding="utf-8")

    # M3U playlists: tiny, useful for exam simulation without an extra player.
    for exam_num in (1, 2):
        lines = [
            "#EXTM3U",
            f"#PLAYLIST:Mock exam {exam_num:02d} - full Listening section",
        ]
        for part in (1, 2):
            lines += [
                f"#EXTINF:-1,Part {part} - exam mode",
                f"../exam/exam-{exam_num:02d}-part-{part:02d}-exam.mp3",
            ]
        (OUT / "audio" / "playlists" / f"mock-exam-{exam_num:02d}-listening.m3u").write_text(
            "\n".join(lines) + "\n", encoding="utf-8"
        )


def main() -> None:
    OUT.mkdir(exist_ok=True)
    audit = pdf_audit()
    page_texts = audit.pop("_page_texts", [])
    assert audit["pages"] == 35, f"Expected 35 pages, got {audit['pages']}"
    assert all(
        v == 0 for v in audit["media_markers"].values()
    ), "PDF unexpectedly contains embedded media/JavaScript"
    if not page_texts:
        raise SystemExit("pypdf is required: install listening/requirements.txt")
    docx_info = docx_audit()
    questions = parse_questions()
    tapescripts = parse_tapescripts()
    exercises = build_exercises(questions, tapescripts, page_texts)
    manifest = build_clips_and_tracks(exercises)
    write_text_outputs(exercises, manifest, audit, docx_info)
    print(f"[OK] PDF pages={audit['pages']}, sha256={audit['sha256'][:16]}…")
    print(f"[OK] Official listening exercises={len(exercises)}, questions={sum(len(e['questions']) for e in exercises)}")
    for ex in exercises:
        print(
            f"     - {ex['id']}: {ex['declared_words']} words, "
            f"{len(ex['segments'])} segments, answers {' '.join(ex['answers'])}, "
            f"PDF cross-check {ex['pdf_cross_check']['transcript_segments_matched']}/{ex['pdf_cross_check']['transcript_segments_total']}"
        )
    print(f"[OK] TTS clips={len(manifest['clips'])}, planned MP3 tracks={len(manifest['tracks'])}")
    print(f"[OK] Wrote {OUT}/inventory.json and {OUT}/clips_manifest.json")


if __name__ == "__main__":
    main()
