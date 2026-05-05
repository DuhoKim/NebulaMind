"""
arXiv paper → NebulaMind page/claim classifier.

Uses TF-IDF cosine similarity. No LLM, no embeddings (Phase A).
Decision matrix:
  cos(paper, page) >= ARXIV_PAGE_MATCH_THRESHOLD (0.30)       → not unrelated
  cos(paper, page) >= ARXIV_PAGE_EXTENSION_THRESHOLD (0.50)   → page_extension candidate
  cos(paper, claim) >= ARXIV_CLAIM_MATCH_THRESHOLD (0.55)     → claim_evidence
  else                                                         → new_topic_candidate or unrelated

Return: one of {'claim_evidence', 'page_extension', 'new_topic_candidate', 'unrelated'}
"""

from __future__ import annotations

import math
import re
from collections import Counter
from dataclasses import dataclass, field
from typing import TYPE_CHECKING

from sqlalchemy.orm import Session

if TYPE_CHECKING:
    from app.models.arxiv import ArxivPaper
    from app.models.claim import Claim

# --------------------------------------------------------------------------
# Stopwords (astronomy-extended)
# --------------------------------------------------------------------------
_STOPWORDS = frozenset("""
a about above after against all also am an and any are aren't as at be because
been before being below between both but by can't cannot could couldn't did
didn't do does doesn't doing don't down during each few for from further get
got had hadn't has hasn't have haven't having he he'd he'll he's her here
here's hers herself him himself his how how's i i'd i'll i'm i've if in into
is isn't it it's its itself let's me more most mustn't my myself no nor not
of off on once only or other ought our ours ourselves out over own same shan't
she she'd she'll she's should shouldn't so some such than that that's the
their theirs them themselves then there there's these they they'd they'll
they're they've this those through to too under until up very was wasn't we
we'd we'll we're we've were weren't what what's when when's where where's
which while who who's whom why why's will with won't would wouldn't you you'd
you'll you're you've your yours yourself yourselves
also using via using
""".split())


def _tokenize(text: str) -> list[str]:
    """Lowercase, strip non-alpha, remove stopwords, min length 3."""
    tokens = re.findall(r"[a-z]{3,}", text.lower())
    return [t for t in tokens if t not in _STOPWORDS]


def _tfidf_vector(tokens: list[str], idf: dict[str, float]) -> dict[str, float]:
    tf = Counter(tokens)
    n = sum(tf.values()) or 1
    return {t: (tf[t] / n) * idf.get(t, 1.0) for t in tf}


def _cosine(a: dict[str, float], b: dict[str, float]) -> float:
    if not a or not b:
        return 0.0
    dot = sum(a[k] * b[k] for k in a if k in b)
    norm_a = math.sqrt(sum(v * v for v in a.values()))
    norm_b = math.sqrt(sum(v * v for v in b.values()))
    if norm_a == 0 or norm_b == 0:
        return 0.0
    return dot / (norm_a * norm_b)


# --------------------------------------------------------------------------
# Corpus cache (module-level, refreshed via refresh_page_vectors)
# --------------------------------------------------------------------------
@dataclass
class _Corpus:
    idf: dict[str, float] = field(default_factory=dict)
    page_vectors: dict[int, dict[str, float]] = field(default_factory=dict)
    page_content_map: dict[int, str] = field(default_factory=dict)  # page_id → raw text


_corpus: _Corpus = _Corpus()


def _page_text(page) -> str:
    """Extract searchable text from WikiPage. Trim to keep TF-IDF stable."""
    parts = [page.title or ""]
    if page.summary:
        parts.append(page.summary[:500])
    if page.content:
        parts.append(page.content[:1500])
    return " ".join(parts)


def _paper_text(paper) -> str:
    """Extract searchable text from ArxivPaper."""
    parts = [paper.title or ""]
    if paper.abstract:
        parts.append(paper.abstract[:1200])
    return " ".join(parts)


def refresh_page_vectors(db: Session) -> None:
    """Rebuild TF-IDF corpus from all wiki pages. Call at startup or when pages change."""
    from app.models.page import WikiPage
    pages = db.query(WikiPage).all()

    # Build document frequency
    doc_tokens: dict[int, list[str]] = {}
    for page in pages:
        tokens = _tokenize(_page_text(page))
        doc_tokens[page.id] = tokens

    N = len(pages) or 1
    df: Counter = Counter()
    for tokens in doc_tokens.values():
        df.update(set(tokens))

    idf = {term: math.log((N + 1) / (count + 1)) + 1.0 for term, count in df.items()}

    # Build per-page TF-IDF vectors
    page_vectors: dict[int, dict[str, float]] = {}
    for page in pages:
        tokens = doc_tokens[page.id]
        page_vectors[page.id] = _tfidf_vector(tokens, idf)

    _corpus.idf = idf
    _corpus.page_vectors = page_vectors
    _corpus.page_content_map = {page.id: _page_text(page) for page in pages}


def _ensure_corpus(db: Session) -> None:
    if not _corpus.idf:
        refresh_page_vectors(db)


# --------------------------------------------------------------------------
# Public API
# --------------------------------------------------------------------------

def match_pages_semantic(
    paper,
    db: Session,
) -> list[tuple[int, float, list[str]]]:
    """Return list of (page_id, score, matched_keywords) sorted by score desc."""
    _ensure_corpus(db)
    from app.config import settings

    paper_tokens = _tokenize(_paper_text(paper))
    paper_vec = _tfidf_vector(paper_tokens, _corpus.idf)

    results = []
    for page_id, page_vec in _corpus.page_vectors.items():
        score = _cosine(paper_vec, page_vec)
        if score >= settings.ARXIV_PAGE_MATCH_THRESHOLD:
            # Extract top overlapping keywords for meta
            overlap = sorted(
                [(k, paper_vec[k] * page_vec[k]) for k in paper_vec if k in page_vec],
                key=lambda x: x[1], reverse=True
            )
            keywords = [k for k, _ in overlap[:8]]
            results.append((page_id, score, keywords))

    results.sort(key=lambda x: x[1], reverse=True)
    return results


def score_claims(
    paper,
    claims: list,
) -> list[tuple[int, float, dict]]:
    """Score paper against a list of claims. Returns (claim_id, score, meta) sorted desc."""
    paper_tokens = _tokenize(_paper_text(paper))
    paper_vec = _tfidf_vector(paper_tokens, _corpus.idf)

    results = []
    for claim in claims:
        claim_tokens = _tokenize(claim.text)
        claim_vec = _tfidf_vector(claim_tokens, _corpus.idf)
        score = _cosine(paper_vec, claim_vec)
        overlap = [k for k in paper_vec if k in claim_vec]
        results.append((claim.id, score, {"matched_keywords": overlap[:6], "score": score}))

    results.sort(key=lambda x: x[1], reverse=True)
    return results


def classify_match_type(
    paper,
    db: Session,
) -> tuple[str, dict]:
    """
    Classify a paper into one of:
      - 'claim_evidence'      → paper matches a specific claim well
      - 'page_extension'      → paper matches a page but no specific claim
      - 'new_topic_candidate' → weak page match, could be new topic
      - 'unrelated'           → no match

    Returns: (match_type, meta_dict)
    meta_dict keys: page_ids, page_scores, claim_scores, matched_keywords
    """
    from app.config import settings
    from app.models.page import WikiPage
    from app.models.claim import Claim

    _ensure_corpus(db)

    page_matches = match_pages_semantic(paper, db)

    if not page_matches:
        return "unrelated", {"page_ids": [], "page_scores": [], "claim_scores": []}

    best_page_id, best_page_score, page_keywords = page_matches[0]

    # Below page match threshold → unrelated
    if best_page_score < settings.ARXIV_PAGE_MATCH_THRESHOLD:
        return "unrelated", {
            "page_ids": [], "page_scores": [best_page_score],
            "claim_scores": [], "matched_keywords": []
        }

    # Check claim-level match on the best matching page
    claims = db.query(Claim).filter(Claim.page_id == best_page_id).all()
    claim_scores = score_claims(paper, claims) if claims else []

    best_claim_id = None
    best_claim_score = 0.0
    if claim_scores:
        best_claim_id, best_claim_score, claim_meta = claim_scores[0]

    meta = {
        "page_ids": [pm[0] for pm in page_matches[:3]],
        "page_scores": [pm[1] for pm in page_matches[:3]],
        "best_page_id": best_page_id,
        "best_page_score": best_page_score,
        "best_claim_id": best_claim_id,
        "best_claim_score": best_claim_score,
        "claim_scores": claim_scores[:5],
        "matched_keywords": page_keywords,
    }

    # Decision matrix
    if best_claim_score >= settings.ARXIV_CLAIM_MATCH_THRESHOLD:
        return "claim_evidence", meta
    elif best_page_score >= settings.ARXIV_PAGE_EXTENSION_THRESHOLD:
        return "page_extension", meta
    elif best_page_score >= settings.ARXIV_PAGE_MATCH_THRESHOLD:
        return "new_topic_candidate", meta
    else:
        return "unrelated", meta
