import re

FILLER_PATTERNS = [
    r"plays a crucial role",
    r"complex and dynamic field",
    r"in conclusion",
    r"it is important to note",
    r"fascinating field",
    r"has long been",
    r"in recent years",
    r"scientists have discovered",
    r"researchers have found",
    r"is a fascinating",
]


def count_filler_hits(text: str) -> int:
    return sum(1 for p in FILLER_PATTERNS if re.search(p, text, re.IGNORECASE))


def is_generic_content(text: str, threshold: int = 3) -> bool:
    return count_filler_hits(text) >= threshold


# =========================================================================
# Claim-preservation guard (P1)
# =========================================================================
# Each WikiPage has linked Claim rows whose .text is the canonical truth
# layer. A proposal that rewrites the page but drops those claim texts is
# erasing what the system has already verified. We require ≥75% of linked
# claim texts to survive into the proposal.

_TOKEN_SPLIT = re.compile(r"[^\w]+", re.UNICODE)


def _tokenize(text: str) -> set[str]:
    return {t.lower() for t in _TOKEN_SPLIT.split(text or "") if len(t) >= 3}


def _claim_is_preserved(claim_text: str, proposal_text: str) -> bool:
    """A claim is 'preserved' if its text appears in the proposal as a
    case-insensitive substring, OR if ≥60% of its content tokens (length
    ≥3) appear in the proposal. The token-overlap path tolerates light
    paraphrase but not wholesale rewriting."""
    if not claim_text:
        return True
    needle = claim_text.strip()
    if not needle:
        return True
    if needle.lower() in (proposal_text or "").lower():
        return True
    claim_tokens = _tokenize(needle)
    if not claim_tokens:
        return True
    proposal_tokens = _tokenize(proposal_text or "")
    if not proposal_tokens:
        return False
    overlap = len(claim_tokens & proposal_tokens) / len(claim_tokens)
    return overlap >= 0.60


def claim_preservation_ratio(proposal_text: str, claim_texts: list[str]) -> float:
    """Return the fraction of claim texts that survive into the proposal.
    Empty list returns 1.0 (vacuously preserved)."""
    texts = [c for c in claim_texts if c and c.strip()]
    if not texts:
        return 1.0
    preserved = sum(1 for c in texts if _claim_is_preserved(c, proposal_text))
    return preserved / len(texts)


def is_claim_preserving(proposal_text: str, claim_texts: list[str], threshold: float = 0.75) -> bool:
    return claim_preservation_ratio(proposal_text, claim_texts) >= threshold


# =========================================================================
# VOTE_THRESHOLD tiering (P1)
# =========================================================================
# A single +vote should not be able to overwrite a page that's already in
# good shape. Tier the approval threshold by page state:
#   - new / near-empty page          (<500c)            → 2  (current default)
#   - existing populated page                            → 3
#   - high-health page (score ≥ 0.6 OR content ≥ 6000c)  → 4

VOTE_THRESHOLD_NEW = 2
VOTE_THRESHOLD_EXISTING = 3
VOTE_THRESHOLD_HIGH_HEALTH = 4

EXISTING_PAGE_MIN_CHARS = 500
HIGH_HEALTH_SCORE = 0.6
HIGH_HEALTH_MIN_CHARS = 6000


def vote_threshold_for_page(page) -> int:
    """Resolve the vote weight threshold that the proposal must clear to
    be approved. `page` is the WikiPage row being edited."""
    content = page.content or "" if page is not None else ""
    content_len = len(content)
    health = getattr(page, "health_score", None) if page is not None else None
    if (health is not None and health >= HIGH_HEALTH_SCORE) or content_len >= HIGH_HEALTH_MIN_CHARS:
        return VOTE_THRESHOLD_HIGH_HEALTH
    if content_len >= EXISTING_PAGE_MIN_CHARS:
        return VOTE_THRESHOLD_EXISTING
    return VOTE_THRESHOLD_NEW
