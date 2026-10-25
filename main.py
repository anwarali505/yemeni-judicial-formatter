"""Utilities for cleaning and formatting Yemeni judicial texts."""

from __future__ import annotations

import re
from typing import Optional

ARABIC_DIGITS = {
    "٠": "0",
    "١": "1",
    "٢": "2",
    "٣": "3",
    "٤": "4",
    "٥": "5",
    "٦": "6",
    "٧": "7",
    "٨": "8",
    "٩": "9",
}


def _normalize_arabic_digits(value: str) -> str:
    for source, target in ARABIC_DIGITS.items():
        value = value.replace(source, target)
    return value


def _normalize_whitespace(value: str) -> str:
    value = value.replace("\r\n", "\n").replace("\r", "\n")
    value = re.sub(r"\n\s*\n+", "\n\n", value)
    value = re.sub(r"[ \t]+", " ", value)
    value = re.sub(r"\s*\n\s*", "\n", value)
    return value.strip()


def _normalize_legal_punctuation(value: str) -> str:
    replacements = {
        "،": ",",
        "؛": ";",
        "؟": "?",
        "ـ": "",
    }
    for source, target in replacements.items():
        value = value.replace(source, target)
    return value


def format_judicial_text(text: str) -> str:
    """Normalize and lightly format a Yemeni judicial or legal text."""
    if text is None:
        raise ValueError("text must not be None")

    text = _normalize_arabic_digits(text)
    text = _normalize_legal_punctuation(text)
    text = _normalize_whitespace(text)

    # Keep common legal formatting patterns readable.
    text = re.sub(r"\s+([,;?.])", r"\1", text)
    text = re.sub(r"([,;?.])(?=\S)", r"\1 ", text)
    text = re.sub(r"\s+", " ", text)
    return text.strip()


def format_case_heading(
    title: str,
    court: Optional[str] = None,
    case_number: Optional[str] = None,
    date: Optional[str] = None,
) -> str:
    """Render a concise heading for a Yemeni judicial case."""
    parts = [title.strip()]
    if court:
        parts.append(f"{court}")
    if case_number:
        parts.append(f"رقم الدعوى: {case_number}")
    if date:
        parts.append(f"بتاريخ: {date}")
    return "\n".join(parts)


def format_ruling(text: str) -> str:
    """Produce a cleaned ruling text with paragraph-level normalization."""
    normalized = format_judicial_text(text)
    paragraphs = [part.strip() for part in normalized.split("\n") if part.strip()]
    return "\n\n".join(paragraphs)
