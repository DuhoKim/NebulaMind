"""
New-page proposal queue triage (state audit 2026-06-12, decision D1).

Policy (approved by Papa 2026-06-13):
  1. Auto-expire: pending > PROPOSAL_EXPIRE_DAYS old AND centroid_similarity
     below the pending-set median -> status 'expired' (recoverable, not deleted).
  2. Queue cap: pending count above PROPOSAL_QUEUE_CAP evicts the
     lowest-scoring rows (score = paper_count * centroid_similarity) to 'expired'.
  3. Insert dedupe: new proposals whose slug exactly matches an existing
     proposal, or exactly/fuzzy-matches a wiki_pages slug, are rejected before
     entering the queue.
  4. Weekly review surface: top-N pending by score via top_pending().
"""

from __future__ import annotations

import datetime as dt
import difflib
import json
import logging
import statistics

from sqlalchemy.orm import Session

from app.config import settings
from app.models.external import NewPageProposal
from app.models.page import WikiPage  # noqa: F401 — registers wiki_pages for FK resolution

log = logging.getLogger(__name__)


def _score(p: NewPageProposal) -> float:
    try:
        paper_count = len(json.loads(p.cluster_papers or "[]"))
    except Exception:
        paper_count = 0
    return paper_count * (p.centroid_similarity or 0.0)


def is_duplicate_slug(db: Session, suggested_slug: str) -> str | None:
    """Insert-time dedupe gate. Returns a reason string if duplicate, else None."""
    slug = (suggested_slug or "").strip().lower()
    if not slug:
        return "empty_slug"

    existing_prop = db.query(NewPageProposal).filter(
        NewPageProposal.suggested_slug == slug
    ).first()
    if existing_prop:
        return f"proposal_slug_exists id={existing_prop.id} status={existing_prop.status}"

    page_slugs = [row[0] for row in db.query(WikiPage.slug).all()]
    if slug in page_slugs:
        return "wiki_page_slug_exact"
    ratio_floor = settings.PROPOSAL_DEDUPE_FUZZY_RATIO
    for page_slug in page_slugs:
        ratio = difflib.SequenceMatcher(None, slug, page_slug).ratio()
        if ratio >= ratio_floor:
            return f"wiki_page_slug_fuzzy match={page_slug} ratio={ratio:.2f}"
    return None


def expire_stale(db: Session) -> int:
    """Expire pending proposals older than PROPOSAL_EXPIRE_DAYS with
    below-median centroid_similarity. Returns number expired."""
    pending = db.query(NewPageProposal).filter(
        NewPageProposal.status == "pending"
    ).all()
    if not pending:
        return 0

    median_sim = statistics.median(p.centroid_similarity or 0.0 for p in pending)
    cutoff = dt.datetime.utcnow() - dt.timedelta(days=settings.PROPOSAL_EXPIRE_DAYS)

    expired = 0
    for p in pending:
        if p.created_at and p.created_at < cutoff and (p.centroid_similarity or 0.0) < median_sim:
            p.status = "expired"
            expired += 1
    if expired:
        log.info("[proposal_triage] expired %d stale pending proposals (cutoff=%s, median_sim=%.3f)",
                 expired, cutoff.date(), median_sim)
    return expired


def enforce_queue_cap(db: Session) -> int:
    """Evict lowest-scoring pending proposals above PROPOSAL_QUEUE_CAP."""
    pending = db.query(NewPageProposal).filter(
        NewPageProposal.status == "pending"
    ).all()
    cap = settings.PROPOSAL_QUEUE_CAP
    overflow = len(pending) - cap
    if overflow <= 0:
        return 0

    pending.sort(key=_score)
    for p in pending[:overflow]:
        p.status = "expired"
    log.info("[proposal_triage] queue cap %d: evicted %d lowest-score proposals", cap, overflow)
    return overflow


def top_pending(db: Session, limit: int = 10) -> list[dict]:
    """Top-N pending proposals by (paper_count * centroid_similarity) for weekly review."""
    pending = db.query(NewPageProposal).filter(
        NewPageProposal.status == "pending"
    ).all()
    pending.sort(key=_score, reverse=True)
    out = []
    for p in pending[:limit]:
        try:
            paper_count = len(json.loads(p.cluster_papers or "[]"))
        except Exception:
            paper_count = 0
        out.append({
            "id": p.id,
            "suggested_slug": p.suggested_slug,
            "suggested_title": p.suggested_title,
            "centroid_similarity": p.centroid_similarity,
            "paper_count": paper_count,
            "score": round(_score(p), 4),
            "created_at": p.created_at.isoformat() if p.created_at else None,
        })
    return out


def run_triage(db: Session) -> dict:
    """Full triage pass: expire stale, then enforce cap. Commits."""
    expired = expire_stale(db)
    evicted = enforce_queue_cap(db)
    remaining = db.query(NewPageProposal).filter(
        NewPageProposal.status == "pending"
    ).count()
    db.commit()
    return {"expired": expired, "evicted": evicted, "pending_remaining": remaining}
