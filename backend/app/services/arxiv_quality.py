"""Quality guards for arXiv feed rows."""

from __future__ import annotations

import datetime as dt
import re


NEW_STYLE_ARXIV_RE = re.compile(r"^(\d{2})(\d{2})\.\d{4,6}(?:v\d+)?$")

REFUSAL_PATTERNS = (
    "i appreciate you sharing",
    "i cannot",
    "i can't",
    "i am unable",
    "i'm unable",
    "as an ai",
    "i should note that this is actually",
    "i should note that this paper",
)


def submitted_from_arxiv_id(arxiv_id: str | None) -> str | None:
    """Return first day of the arXiv YYMM month for new-style arXiv IDs."""
    match = NEW_STYLE_ARXIV_RE.match((arxiv_id or "").strip())
    if not match:
        return None
    year = 2000 + int(match.group(1))
    month = int(match.group(2))
    if not 1 <= month <= 12:
        return None
    return f"{year:04d}-{month:02d}-01"


def normalize_submitted_date(
    submitted: str | None,
    arxiv_id: str | None,
    *,
    today: dt.date | None = None,
) -> str | None:
    """Normalize an ingest date and reject future dates after arXiv-ID repair."""
    today = today or dt.date.today()
    candidate = (submitted or "").strip()
    if len(candidate) == 7:
        candidate = f"{candidate}-01"
    candidate = candidate.replace("-00", "-01")

    try:
        parsed = dt.date.fromisoformat(candidate)
    except ValueError:
        parsed = None

    if parsed is not None and parsed <= today:
        return parsed.isoformat()

    derived = submitted_from_arxiv_id(arxiv_id)
    if not derived:
        return None
    try:
        derived_date = dt.date.fromisoformat(derived)
    except ValueError:
        return None
    if derived_date > today:
        return None
    return derived


def looks_like_llm_refusal(text: str | None) -> bool:
    normalized = " ".join((text or "").lower().split())
    return any(pattern in normalized for pattern in REFUSAL_PATTERNS)
