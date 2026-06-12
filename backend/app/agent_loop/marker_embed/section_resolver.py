"""Stage A: resolve claims.section → H2 section body in page content."""
import re
from dataclasses import dataclass
from typing import Optional

from rapidfuzz import fuzz

EXCLUDED_SECTIONS = {"Open Questions & Future Directions"}


@dataclass
class SectionBlock:
    title: str
    body: str
    char_start: int  # offset of the ## heading in full content


def parse_sections(content: str) -> list[SectionBlock]:
    """Return all H2 sections as (title, body, char_start) tuples."""
    sections: list[SectionBlock] = []
    heading_re = re.compile(r"^## (.+?)$", re.MULTILINE)
    matches = list(heading_re.finditer(content))

    for i, m in enumerate(matches):
        title = m.group(1).strip()
        body_start = m.end()
        body_end = matches[i + 1].start() if i + 1 < len(matches) else len(content)
        body = content[body_start:body_end].strip()
        sections.append(SectionBlock(title=title, body=body, char_start=m.start()))

    return sections


def resolve_section(claim_section: str, sections: list[SectionBlock]) -> Optional[SectionBlock]:
    """
    Find the SectionBlock matching a claim's section field.
    Returns None for excluded sections or if no match found.
    """
    if claim_section in EXCLUDED_SECTIONS:
        return None

    for s in sections:
        if s.title == claim_section:
            return s

    # Jaccard token similarity fallback
    best_score = 0.0
    best_section: Optional[SectionBlock] = None
    for s in sections:
        score = fuzz.token_sort_ratio(claim_section, s.title) / 100.0
        if score > best_score:
            best_score = score
            best_section = s

    return best_section if best_score >= 0.6 else None
