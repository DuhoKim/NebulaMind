"""Calendar API — Survey Data Release Calendar."""
from fastapi import APIRouter, Depends, Query
from sqlalchemy.orm import Session
from sqlalchemy import text
from app.database import get_db
from datetime import datetime, timedelta
import json, secrets

router = APIRouter(prefix="/api/calendar", tags=["calendar"])


@router.get("/")
def list_calendar_events(
    kind: str | None = None,
    track: str | None = None,
    facility_slug: str | None = None,
    upcoming_days: int = Query(365, le=730),
    past_days: int = Query(30, le=180),
    limit: int = Query(50, le=200),
    db: Session = Depends(get_db),
):
    """List facility news items / calendar events."""
    since = datetime.utcnow() - timedelta(days=past_days)
    until = datetime.utcnow() + timedelta(days=upcoming_days)

    filters = ["fni.occurs_at BETWEEN :since AND :until OR fni.occurs_at IS NULL"]
    params = {"since": since, "until": until}

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
    rows = db.execute(text(f"""
        SELECT fni.id, fni.slug, fni.title, fni.kind, fni.track, fni.summary,
               fni.occurs_at, fni.occurs_at_confidence, fni.occurrence_status,
               fni.source_url, fni.data_portal_urls, fni.featured, fni.credibility_score,
               fp.slug AS facility_slug, fp.short_name AS facility_name,
               fp.operator AS facility_operator, fp.homepage_url AS facility_url
        FROM facility_news_items fni
        LEFT JOIN facility_profiles fp ON fp.id = fni.facility_id
        WHERE {where}
        ORDER BY fni.featured DESC, fni.occurs_at ASC NULLS LAST
        LIMIT :limit
    """), {**params, "limit": limit}).fetchall()

    return [dict(r._mapping) for r in rows]


@router.get("/stats")
def calendar_stats(db: Session = Depends(get_db)):
    """Basic stats for the calendar."""
    total = db.execute(text("SELECT COUNT(*) FROM facility_news_items")).scalar()
    upcoming = db.execute(text("SELECT COUNT(*) FROM facility_news_items WHERE occurs_at > NOW()")).scalar()
    facilities = db.execute(text("SELECT COUNT(*) FROM facility_profiles")).scalar()
    return {"total_events": total, "upcoming_events": upcoming, "facilities": facilities}


@router.get("/facilities")
def list_facilities(db: Session = Depends(get_db)):
    """List all tracked facilities."""
    rows = db.execute(text("""
        SELECT fp.slug, fp.full_name, fp.short_name, fp.operator, fp.facility_kind,
               fp.operating_status, fp.homepage_url, fp.data_portals,
               COUNT(fni.id) AS event_count
        FROM facility_profiles fp
        LEFT JOIN facility_news_items fni ON fni.facility_id = fp.id
        GROUP BY fp.id ORDER BY fp.short_name
    """)).fetchall()
    return [dict(r._mapping) for r in rows]


@router.get("/{slug}")
def get_calendar_event(slug: str, db: Session = Depends(get_db)):
    """Get a specific calendar event."""
    row = db.execute(text("""
        SELECT fni.*, fp.slug AS facility_slug, fp.full_name AS facility_full_name,
               fp.short_name AS facility_name, fp.homepage_url AS facility_url,
               fp.data_portals AS facility_portals
        FROM facility_news_items fni
        LEFT JOIN facility_profiles fp ON fp.id = fni.facility_id
        WHERE fni.slug = :slug
    """), {"slug": slug}).fetchone()

    if not row:
        from fastapi import HTTPException
        raise HTTPException(404, "Event not found")

    d = dict(row._mapping)
    # Parse JSON fields
    for field in ["data_portal_urls", "related_page_slugs", "related_arxiv_ids", "facility_portals"]:
        if d.get(field):
            try:
                d[field] = json.loads(d[field])
            except Exception:
                pass
    return d


@router.post("/{slug}/subscribe")
def subscribe_to_event(
    slug: str,
    body: dict,
    db: Session = Depends(get_db),
):
    """Subscribe to notifications for a calendar event ('Notify me')."""
    email = body.get("email", "").strip().lower()
    if not email or "@" not in email:
        from fastapi import HTTPException
        raise HTTPException(400, "Valid email required")

    event = db.execute(text("SELECT id FROM facility_news_items WHERE slug=:s"), {"s": slug}).fetchone()
    if not event:
        from fastapi import HTTPException
        raise HTTPException(404, "Event not found")

    # Check existing
    existing = db.execute(text("""
        SELECT id FROM calendar_subscriptions 
        WHERE facility_news_item_id=:eid AND email=:email
    """), {"eid": event[0], "email": email}).fetchone()

    if existing:
        return {"status": "already_subscribed"}

    token = secrets.token_urlsafe(32)
    db.execute(text("""
        INSERT INTO calendar_subscriptions (facility_news_item_id, email, unsubscribe_token, notify_when)
        VALUES (:eid, :email, :token, 'completed')
    """), {"eid": event[0], "email": email, "token": token})
    db.commit()

    return {"status": "subscribed", "message": f"You'll be notified at {email} when this event occurs."}


@router.post("/subscribe")
def subscribe_general(
    body: dict,
    db: Session = Depends(get_db),
):
    """General newsletter/digest subscription (no specific event required)."""
    email = body.get("email", "").strip().lower()
    if not email or "@" not in email:
        from fastapi import HTTPException
        raise HTTPException(400, "Valid email required")

    # Use first upcoming/featured event as anchor, or first event in table
    event = db.execute(text(
        "SELECT id FROM facility_news_items WHERE featured=true ORDER BY occurs_at ASC NULLS LAST LIMIT 1"
    )).fetchone()
    if not event:
        event = db.execute(text("SELECT id FROM facility_news_items ORDER BY id LIMIT 1")).fetchone()
    if not event:
        from fastapi import HTTPException
        raise HTTPException(503, "No events available yet; try again after seeding.")

    existing = db.execute(text("""
        SELECT id FROM calendar_subscriptions
        WHERE facility_news_item_id=:eid AND email=:email
    """), {"eid": event[0], "email": email}).fetchone()
    if existing:
        return {"status": "already_subscribed"}

    token = secrets.token_urlsafe(32)
    db.execute(text("""
        INSERT INTO calendar_subscriptions (facility_news_item_id, email, unsubscribe_token, notify_when)
        VALUES (:eid, :email, :token, 'completed')
    """), {"eid": event[0], "email": email, "token": token})
    db.commit()

    return {"status": "subscribed", "message": f"Subscribed {email} to NebulaMind calendar digest."}
