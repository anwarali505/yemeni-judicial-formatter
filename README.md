# yemeni-judicial-formatter

A small utility for normalizing and formatting Yemeni judicial decisions and legal text in Arabic.

## What it does

- Removes duplicate whitespace and normalizes line breaks.
- Standardizes Arabic punctuation and digits.
- Formats headings for judicial decisions.
- Produces a clean, readable ruling body.

## Installation

```bash
python -m pip install .
```

## Quick usage

```python
from yemeni_judicial_formatter import format_case_heading, format_judicial_text

heading = format_case_heading(
    title="حكم في دعوى مدنية",
    court="محكمة عدن الابتدائية",
    case_number="2024/17",
    date="2024-01-15",
)

text = format_judicial_text(
    "بناءً على الطلب المقدم من المدعي، وبعد المداولة، حكمت المحكمة بما يلي:   إن الواقع يثبت ..."
)

print(heading)
print(text)
```

## CLI

```bash
python main.py "بناءً على الطلب المقدم من المدعي، وبعد المداولة، حكمت المحكمة في الدعوى رقم 2024/17."
```
