"""News API — unified feed of facility news items and curated arXiv papers."""
from fastapi import APIRouter, Depends, Query, HTTPException
from sqlalchemy.orm import Session
from sqlalchemy import text
from app.database import get_db
from datetime import datetime, timedelta

router = APIRouter(prefix="/api/news", tags=["news"])


@router.get("", include_in_schema=False)
@router.get("/")
def list_news(
    kind: str | None = None,
    track: str | None = None,
    facility_slug: str | None = None,
    include_arxiv: bool = Query(True),
    past_days: int = Query(180, le=365),
    upcoming_days: int = Query(730, le=730),
    limit: int = Query(100, le=200),
    db: Session = Depends(get_db),
):
    """Unified news feed: facility news items + curated arXiv papers."""
    since = datetime.utcnow() - timedelta(days=past_days)
    until = datetime.utcnow() + timedelta(days=upcoming_days)

    filters = ["(fni.occurs_at BETWEEN :since AND :until OR fni.occurs_at IS NULL)"]
    params: dict = {"since": since, "until": until}

    if kind:
        filters.append("fni.kind = :kind")
        params["kind"] = kind
    if track:
        filters.append("fni.track = :track")
        params["track"] = track
    if facility_slug:
        filters.append("fp.slug = :facility_slug")
        params["facility_slug"] = facility_slug

    where = " AND ".join(filters)
    facility_rows = db.execute(text(f"""
        SELECT
            fni.id, fni.slug, fni.title, fni.kind, fni.track, fni.summary,
            fni.occurs_at, fni.occurs_at_confidence, fni.occurrence_status,
            fni.source_url, fni.data_portal_urls, fni.featured, fni.credibility_score,
            fni.created_at,
            fp.slug AS facility_slug, fp.short_name AS facility_name,
            fp.operator AS facility_operator, fp.homepage_url AS facility_url,
            'facility' AS source_type
        FROM facility_news_items fni
        LEFT JOIN facility_profiles fp ON fp.id = fni.facility_id
        WHERE {where}
        ORDER BY fni.featured DESC, fni.occurs_at ASC NULLS LAST
        LIMIT :limit
    """), {**params, "limit": limit}).fetchall()

    items = [dict(r._mapping) for r in facility_rows]

    if include_arxiv and not (kind or track or facility_slug):
        arxiv_since = datetime.utcnow() - timedelta(days=min(past_days, 30))
        arxiv_rows = db.execute(text("""
            SELECT
                id, arxiv_id AS slug, title,
                'arxiv' AS kind, 'results' AS track,
                abstract_summary AS summary,
                NULL AS occurs_at, 'hard' AS occurs_at_confidence,
                'completed' AS occurrence_status,
                url AS source_url, NULL AS data_portal_urls,
                false AS featured, NULL AS credibility_score,
                created_at,
                NULL AS facility_slug, NULL AS facility_name,
                NULL AS facility_operator, NULL AS facility_url,
                'arxiv' AS source_type
            FROM arxiv_papers
            WHERE created_at >= :since
              AND match_type IN ('claim_evidence', 'page_extension', 'new_topic_candidate')
            ORDER BY created_at DESC
            LIMIT 50
        """), {"since": arxiv_since}).fetchall()
        items.extend([dict(r._mapping) for r in arxiv_rows])

    return items


@router.get("/featured")
def list_featured_news(db: Session = Depends(get_db)):
    """Return today's featured facility news items."""
    today = datetime.utcnow().replace(hour=0, minute=0, second=0, microsecond=0)
    rows = db.execute(text("""
        SELECT
            fni.id, fni.slug, fni.title, fni.kind, fni.track, fni.summary,
            fni.occurs_at, fni.occurrence_status, fni.source_url,
            fni.credibility_score, fni.created_at,
            fp.slug AS facility_slug, fp.short_name AS facility_name,
            fp.homepage_url AS facility_url
        FROM facility_news_items fni
        LEFT JOIN facility_profiles fp ON fp.id = fni.facility_id
        WHERE fni.featured = true AND fni.created_at >= :today
        ORDER BY fni.credibility_score DESC NULLS LAST
        LIMIT 10
    """), {"today": today}).fetchall()
    return [dict(r._mapping) for r in rows]


@router.get("/stats")
def news_stats(db: Session = Depends(get_db)):
    """Quick stats for the news feed."""
    facility_total = db.execute(text("SELECT COUNT(*) FROM facility_news_items")).scalar()
    featured_today = db.execute(text(
        "SELECT COUNT(*) FROM facility_news_items WHERE featured=true AND created_at >= NOW() - INTERVAL '24 hours'"
    )).scalar()
    arxiv_total = db.execute(text("SELECT COUNT(*) FROM arxiv_papers")).scalar()
    facilities = db.execute(text("SELECT COUNT(*) FROM facility_profiles")).scalar()
    return {
        "facility_news_total": facility_total,
        "featured_today": featured_today,
        "arxiv_papers_total": arxiv_total,
        "tracked_facilities": facilities,
    }


@router.get("/{slug}")
def get_news_item(slug: str, db: Session = Depends(get_db)):
    """Detail view for a single facility news item or arXiv paper by slug."""
    row = db.execute(text("""
        SELECT
            fni.id, fni.slug, fni.title, fni.kind, fni.track, fni.summary,
            fni.occurs_at, fni.occurs_at_confidence, fni.occurrence_status,
            fni.source_url, fni.data_portal_urls, fni.featured, fni.credibility_score,
            fni.created_at,
            fp.slug AS facility_slug, fp.short_name AS facility_name,
            fp.operator AS facility_operator, fp.homepage_url AS facility_url,
            'facility' AS source_type
        FROM facility_news_items fni
        LEFT JOIN facility_profiles fp ON fp.id = fni.facility_id
        WHERE fni.slug = :slug
        LIMIT 1
    """), {"slug": slug}).fetchone()

    if row:
        return dict(row._mapping)

    # Fallback: check arxiv_papers by arxiv_id
    arxiv_row = db.execute(text("""
        SELECT
            id, arxiv_id AS slug, title,
            'arxiv' AS kind, 'results' AS track,
            abstract_summary AS summary,
            NULL AS occurs_at, 'hard' AS occurs_at_confidence,
            'completed' AS occurrence_status,
            url AS source_url, NULL AS data_portal_urls,
            false AS featured, NULL AS credibility_score,
            created_at,
            NULL AS facility_slug, NULL AS facility_name,
            NULL AS facility_operator, NULL AS facility_url,
            'arxiv' AS source_type
        FROM arxiv_papers
        WHERE arxiv_id = :slug
        LIMIT 1
    """), {"slug": slug}).fetchone()

    if arxiv_row:
        return dict(arxiv_row._mapping)

    raise HTTPException(status_code=404, detail=f"News item '{slug}' not found")
