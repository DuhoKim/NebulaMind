"""
Wikipedia cross-check signal for trust scoring.

wikipedia_cross_check_score(claim, page) → float [0.0, 0.05]

The bonus is a tiebreaker, not a verdict. Maximum effect on TS:
  bonus_max=0.05 × w_v=0.35 → ΔTS=0.0175 (moves borderline claims only)
"""
from __future__ import annotations
import re
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from app.models.claim import Claim
    from app.models.page import WikiPage

# Common English + astronomy stopwords for rare-keyword extraction
_CROSSCHECK_STOPWORDS = frozenset("""
a about above after against all also am an and any are as at be because
been before being below between both but by can cannot could did do does
doing down during each few for from further get had has have having he her
here him his how i if in into is it its itself let me more most my no nor
not of off on once only or other our out over own same she should so some
such than that the their them then there these they this those through to
too under until up very was we were what when where which while who with
would you your also using via well may very its can been
""".split())


def rare_keywords(text: str, min_len: int = 5) -> set[str]:
    """Extract rare (longer) lowercase alpha tokens, excluding stopwords."""
    tokens = re.findall(r"[a-z]{%d,}" % min_len, text.lower())
    return {t for t in tokens if t not in _CROSSCHECK_STOPWORDS}


def wikipedia_cross_check_score(claim, page) -> float:
    """
    Returns 0.00–0.05 (capped). Used as a tiebreaker in recalculate_trust_v2.

    Logic:
    - Extract rare keywords (len≥5) from both claim.text and page.wiki_summary
    - If claim has < 2 rare keywords → 0.0 (not enough signal)
    - Overlap ratio = |intersection| / max(2, |claim_kw|)
    - If overlap < 0.30 → 0.0
    - Score = min(0.05, 0.025 + overlap × 0.025)
    """
    if not page or not page.wiki_summary:
        return 0.0
    claim_kw = rare_keywords(claim.text, min_len=5)
    if len(claim_kw) < 2:
        return 0.0
    summary_kw = rare_keywords(page.wiki_summary, min_len=5)
    if not summary_kw:
        return 0.0
    overlap = len(claim_kw & summary_kw) / max(2, len(claim_kw))
    if overlap < 0.30:
        return 0.0
    return min(0.05, 0.025 + overlap * 0.025)
