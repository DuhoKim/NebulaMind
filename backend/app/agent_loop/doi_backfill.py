"""DOI backfill — resolves missing DOIs on refereed_paper news items via ADS + CrossRef.

One-shot usage:
    python3 -m app.agent_loop.doi_backfill --all-unresolved

Nightly Celery sweep registered in worker.py at 04:00 KST (UTC 19:00).
"""
from __future__ import annotations

import sys

from app.agent_loop.worker import celery_app
from app.database import SessionLocal
from app.models.facility import FacilityNewsItem
from app.models.external import DOIResolutionLog
from app.services.paper_search import (
    ads_lookup_by_title_and_venue,
    crossref_lookup_by_title_and_venue,
    _token_jaccard,
    _venue_prefix_match,
)

AUTO_APPLY_THRESHOLD = 0.85


def _resolve_one(item: FacilityNewsItem) -> dict | None:
    """Try ADS then CrossRef. Return resolution dict or None if unresolved."""
    title = item.title or ""
    venue = item.paper_venue

    best_doi: str | None = None
    best_sim: float = 0.0
    best_venue_match: bool = False
    best_source: str = ""

    # ADS pass
    for rec in ads_lookup_by_title_and_venue(title, venue):
        if not rec.doi:
            continue
        sim = _token_jaccard(title, rec.title)
        vm = _venue_prefix_match(venue or "", rec.venue or "") if venue else False
        # Confidence: title similarity weighted higher, venue as tie-breaker bonus
        conf = sim * (1.05 if vm else 1.0)
        conf = min(conf, 1.0)
        if conf > best_sim:
            best_doi, best_sim, best_venue_match, best_source = rec.doi, conf, vm, "ads"

    # CrossRef fallback (only if ADS didn't hit threshold)
    if best_sim < AUTO_APPLY_THRESHOLD:
        for item_cr in crossref_lookup_by_title_and_venue(title, venue):
            doi = item_cr.get("DOI")
            if not doi:
                continue
            cr_titles = item_cr.get("title") or []
            cr_title = cr_titles[0] if cr_titles else ""
            sim = _token_jaccard(title, cr_title)
            cr_venues = item_cr.get("container-title") or []
            cr_venue = cr_venues[0] if cr_venues else ""
            vm = _venue_prefix_match(venue or "", cr_venue) if venue else False
            conf = sim * (1.05 if vm else 1.0)
            conf = min(conf, 1.0)
            if conf > best_sim:
                best_doi, best_sim, best_venue_match, best_source = doi, conf, vm, "crossref"

    if not best_doi:
        return None

    return {
        "doi": best_doi,
        "confidence": round(best_sim, 4),
        "source_api": best_source,
        "title_similarity": round(best_sim, 4),
        "venue_match": best_venue_match,
    }


def _run_backfill(db, query) -> dict:
    applied = 0
    unresolved = 0
    for item in query:
        result = _resolve_one(item)
        if result and result["confidence"] >= AUTO_APPLY_THRESHOLD:
            item.paper_doi = result["doi"]
            log = DOIResolutionLog(
                news_item_id=item.id,
                resolved_doi=result["doi"],
                confidence=result["confidence"],
                source_api=result["source_api"],
                title_similarity=result["title_similarity"],
                venue_match=result["venue_match"],
                status="auto_applied",
                notes=f"title_sim={result['title_similarity']:.3f}",
            )
            db.add(log)
            applied += 1
        else:
            conf = result["confidence"] if result else 0.0
            log = DOIResolutionLog(
                news_item_id=item.id,
                resolved_doi=result["doi"] if result else None,
                confidence=conf,
                source_api=result["source_api"] if result else "none",
                title_similarity=result["title_similarity"] if result else 0.0,
                venue_match=result["venue_match"] if result else False,
                status="unresolved",
                notes=f"best_conf={conf:.3f} below threshold {AUTO_APPLY_THRESHOLD}",
            )
            db.add(log)
            unresolved += 1
    db.commit()
    return {"auto_applied": applied, "unresolved": unresolved}


@celery_app.task(name="app.agent_loop.doi_backfill.sweep_recent_refereed")
def sweep_recent_refereed() -> dict:
    """Nightly sweep: resolve DOIs for refereed_paper items from the last 7 days."""
    import datetime as dt
    db = SessionLocal()
    try:
        cutoff = dt.datetime.utcnow() - dt.timedelta(days=7)
        candidates = (
            db.query(FacilityNewsItem)
            .filter(
                FacilityNewsItem.kind == "refereed_paper",
                FacilityNewsItem.paper_doi.is_(None),
                FacilityNewsItem.created_at >= cutoff,
            )
            .all()
        )
        if not candidates:
            return {"auto_applied": 0, "unresolved": 0}
        result = _run_backfill(db, candidates)
        print(f"[doi_backfill] sweep: {result}")
        return result
    except Exception as ex:
        db.rollback()
        print(f"[doi_backfill] sweep error: {ex}")
        raise
    finally:
        db.close()


def _backfill_all_unresolved() -> None:
    db = SessionLocal()
    try:
        candidates = (
            db.query(FacilityNewsItem)
            .filter(
                FacilityNewsItem.kind == "refereed_paper",
                FacilityNewsItem.paper_doi.is_(None),
            )
            .outerjoin(
                DOIResolutionLog,
                DOIResolutionLog.news_item_id == FacilityNewsItem.id,
            )
            .filter(DOIResolutionLog.id.is_(None))  # not already attempted
            .all()
        )
        print(f"[doi_backfill] {len(candidates)} candidates found")
        result = _run_backfill(db, candidates)
        print(f"[doi_backfill] done: auto_applied={result['auto_applied']} unresolved={result['unresolved']}")
    finally:
        db.close()


if __name__ == "__main__":
    if "--all-unresolved" in sys.argv:
        _backfill_all_unresolved()
    else:
        print("Usage: python3 -m app.agent_loop.doi_backfill --all-unresolved")
        sys.exit(1)
