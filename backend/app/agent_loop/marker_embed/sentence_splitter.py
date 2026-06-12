"""Astronomy-aware sentence splitter for Stage B.

Uses a custom regex approach calibrated for NebulaMind wiki prose:
- Preserves Greek letters, equations, ± notation
- Glues citations (Author et al. YYYY) to their sentences
- Skips code fences, inline code, headings, math blocks, list markers
- Astronomy abbreviations: et al., e.g., i.e., cf., Fig., Eq., etc.
"""
import re

_ABBREV_RE = re.compile(
    r"\b(?:et\s+al|e\.g|i\.e|cf|vs|Fig|Figs|Eq|Eqs|Sect|Ref|Refs|No|"
    r"approx|est|incl|excl|vol|pp|ed|eds|ca|[A-Z])(?=\.)",
    re.IGNORECASE,
)

# Markers for protected regions
_PLACEHOLDER_DOT = "\x00"
_PLACEHOLDER_DEC = "\x01"

# Patterns to detect forbidden injection sites (line-level)
_HEADING_RE = re.compile(r"^\s*#{1,6}\s")
_CODE_FENCE_RE = re.compile(r"^\s*```")
_LIST_MARKER_RE = re.compile(r"^\s*(?:[-*+]|\d+\.)\s")
_BLOCKQUOTE_RE = re.compile(r"^\s*>")


def split_sentences(text: str) -> list[str]:
    """
    Split markdown body text into injectable sentences.
    Skips headings, code fences, list markers, math blocks, inline code lines.
    """
    if not text.strip():
        return []

    sentences: list[str] = []
    in_code_fence = False
    in_math_block = False
    paragraphs: list[list[str]] = []
    current_para: list[str] = []

    for line in text.splitlines():
        stripped = line.strip()

        if stripped.startswith("```"):
            in_code_fence = not in_code_fence
            if current_para:
                paragraphs.append(current_para)
                current_para = []
            continue

        if stripped.startswith("$$"):
            in_math_block = not in_math_block
            if current_para:
                paragraphs.append(current_para)
                current_para = []
            continue

        if in_code_fence or in_math_block:
            continue

        if not stripped:
            if current_para:
                paragraphs.append(current_para)
                current_para = []
            continue

        # Skip headings, list markers, blockquotes
        if (
            _HEADING_RE.match(line)
            or _LIST_MARKER_RE.match(line)
            or _BLOCKQUOTE_RE.match(line)
        ):
            if current_para:
                paragraphs.append(current_para)
                current_para = []
            continue

        current_para.append(line)

    if current_para:
        paragraphs.append(current_para)

    for para_lines in paragraphs:
        para_text = " ".join(para_lines)
        for sent in _split_paragraph(para_text):
            stripped = sent.strip()
            if stripped:
                sentences.append(stripped)

    return sentences


def _split_paragraph(para: str) -> list[str]:
    """Split a single prose paragraph into sentences."""
    # Protect abbreviation dots
    protected = _ABBREV_RE.sub(lambda m: m.group(0)[:-1] + _PLACEHOLDER_DOT, para)

    # Protect decimal numbers (e.g., 0.9649, 1.5 ± 0.3)
    protected = re.sub(r"(\d)\.(\d)", r"\1" + _PLACEHOLDER_DEC + r"\2", protected)

    # Protect inline citations like (White & Rees 1978) at sentence end
    # — just don't split inside parens
    protected = _protect_parens(protected)

    # Split on . ! ? followed by whitespace + uppercase or open paren
    parts = re.split(r"(?<=[.!?])\s+(?=[A-Z\(\"'])", protected)

    result = []
    for part in parts:
        restored = (
            part.replace(_PLACEHOLDER_DOT, ".")
            .replace(_PLACEHOLDER_DEC, ".")
            .replace("\x02", "(")
            .replace("\x03", ")")
        )
        restored = restored.strip()
        if restored:
            result.append(restored)

    return result if result else [para.strip()]


def _protect_parens(text: str) -> str:
    """Replace parens inside citations with placeholders to prevent mid-citation splits."""
    # Simple: replace ( and ) inside balanced inline parens that contain a year
    result = list(text)
    depth = 0
    start = -1
    for i, ch in enumerate(result):
        if ch == "(":
            if depth == 0:
                start = i
            depth += 1
        elif ch == ")":
            depth -= 1
            if depth == 0 and start >= 0:
                inner = "".join(result[start + 1 : i])
                if re.search(r"\d{4}", inner):
                    result[start] = "\x02"
                    result[i] = "\x03"
                start = -1
    return "".join(result)
