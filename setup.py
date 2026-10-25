from yemeni_judicial_formatter import format_case_heading, format_judicial_text, format_ruling


def test_format_judicial_text_normalizes_whitespace_and_punctuation():
    text = "  بناءً على الطلب المقدم من المدعي،   وبعد المداولة، حكمت المحكمة  في الدعوى رقم ٢٠٢٤/١٧   "
    cleaned = format_judicial_text(text)
    assert "بناءً على الطلب المقدم من المدعي, وبعد المداولة, حكمت المحكمة في الدعوى رقم 2024/17" in cleaned


def test_format_case_heading_includes_metadata():
    heading = format_case_heading(
        title="حكم في دعوى مدنية",
        court="محكمة عدن الابتدائية",
        case_number="2024/17",
        date="2024-01-15",
    )
    assert "حكم في دعوى مدنية" in heading
    assert "محكمة عدن الابتدائية" in heading
    assert "رقم الدعوى: 2024/17" in heading
    assert "بتاريخ: 2024-01-15" in heading


def test_format_ruling_preserves_paragraphs():
    text = "أولاً: تبين من الأوراق أن الطلب مستوفٍ.\nثانياً: تقرر الحكم لصالح المدعي."
    result = format_ruling(text)
    assert "أولاً: تبين من الأوراق أن الطلب مستوفٍ." in result
    assert "ثانياً: تقرر الحكم لصالح المدعي." in result
