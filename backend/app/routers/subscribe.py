"""
Newsletter subscription router.
"""
import json
import uuid
import datetime as dt

from fastapi import APIRouter, Depends, HTTPException, Query
from pydantic import BaseModel, EmailStr
from sqlalchemy import func
from sqlalchemy.orm import Session

from app.database import get_db
from app.models.subscriber import Subscriber
from app.models.arxiv import ArxivPaper

router = APIRouter(prefix="/api", tags=["newsletter"])


class SubscribeRequest(BaseModel):
    email: EmailStr
    name: str | None = None
    categories: list[str] = ["astro-ph.GA"]
    frequency: str = "daily"  # daily | weekly
    specialty: str = "general"  # cosmology | stellar | exoplanets | high-energy | other | general


@router.post("/subscribe")
def subscribe(req: SubscribeRequest, db: Session = Depends(get_db)):
    """Subscribe to the NebulaMind research newsletter."""
    existing = db.query(Subscriber).filter(Subscriber.email == req.email).first()
    if existing:
        # Reactivate if previously unsubscribed
        existing.is_active = True
        existing.categories = json.dumps(req.categories)
        existing.frequency = req.frequency
        if req.name:
            existing.name = req.name
        existing.specialty = req.specialty
        db.commit()
        return {"status": "resubscribed", "email": req.email}

    if req.frequency not in ("daily", "weekly"):
        raise HTTPException(400, "frequency must be 'daily' or 'weekly'")

    sub = Subscriber(
        email=req.email,
        name=req.name,
        categories=json.dumps(req.categories),
        frequency=req.frequency,
        specialty=req.specialty,
        unsubscribe_token=uuid.uuid4().hex,
    )
    db.add(sub)
    db.commit()
    return {"status": "subscribed", "email": req.email}


@router.get("/unsubscribe")
def unsubscribe(token: str = Query(...), db: Session = Depends(get_db)):
    """One-click unsubscribe via token."""
    sub = db.query(Subscriber).filter(Subscriber.unsubscribe_token == token).first()
    if not sub:
        raise HTTPException(404, "Invalid unsubscribe token")
    sub.is_active = False
    db.commit()
    return {"status": "unsubscribed", "email": sub.email}


@router.get("/subscribers/count")
def subscriber_count(db: Session = Depends(get_db)):
    """Public subscriber count (for social proof)."""
    count = db.query(Subscriber).filter(Subscriber.is_active.is_(True)).count()
    return {"count": count}


@router.get("/newsletter/archive")
def newsletter_archive(
    days: int = Query(default=14, ge=1, le=90),
    category: str | None = Query(default=None),
    db: Session = Depends(get_db),
):
    """Return arxiv papers grouped by date for newsletter archive (last N days)."""
    since = (dt.date.today() - dt.timedelta(days=days)).isoformat()

    q = db.query(ArxivPaper).filter(ArxivPaper.submitted >= since)
    if category:
        q = q.filter(ArxivPaper.category == category)
    papers = q.order_by(ArxivPaper.submitted.desc(), ArxivPaper.created_at.desc()).all()

    # Group by date
    grouped: dict[str, list[dict]] = {}
    for p in papers:
        date = p.submitted
        if date not in grouped:
            grouped[date] = []
        authors = json.loads(p.authors) if p.authors else []
        related = json.loads(p.related_pages) if p.related_pages else []
        grouped[date].append({
            "arxiv_id": p.arxiv_id,
            "title": p.title,
            "authors": authors[:3],  # first 3 authors
            "abstract_summary": p.abstract_summary or "",
            "category": p.category,
            "url": p.url,
            "related_pages": related[:3],
        })

    # Build sorted list of issues
    issues = [
        {"date": date, "papers": group_papers, "count": len(group_papers)}
        for date, group_papers in sorted(grouped.items(), reverse=True)
    ]

    sub_count = db.query(Subscriber).filter(Subscriber.is_active.is_(True)).count()
    return {"issues": issues, "subscriber_count": sub_count, "days": days}


@router.get("/newsletter/preview")
def newsletter_preview(
    date: str | None = Query(default=None),
    db: Session = Depends(get_db),
):
    """Preview the newsletter for a given date (defaults to today)."""
    target = date or dt.date.today().isoformat()
    # Accept yesterday too in case papers haven't arrived yet
    yesterday = (dt.datetime.strptime(target, "%Y-%m-%d").date() - dt.timedelta(days=1)).isoformat()

    papers = (
        db.query(ArxivPaper)
        .filter(ArxivPaper.submitted.in_([target, yesterday]))
        .order_by(ArxivPaper.category, ArxivPaper.created_at.desc())
        .all()
    )

    cat_labels = {
        "astro-ph.GA": "🌀 Galaxies",
        "astro-ph.CO": "🔵 Cosmology",
        "astro-ph.HE": "⚡ High Energy",
        "astro-ph.SR": "☀️ Solar & Stellar",
        "astro-ph.EP": "🪐 Planetary",
        "astro-ph.IM": "🔧 Instrumentation",
    }
    by_cat: dict[str, list] = {}
    for p in papers:
        authors = json.loads(p.authors) if p.authors else []
        related = json.loads(p.related_pages) if p.related_pages else []
        by_cat.setdefault(p.category, []).append({
            "arxiv_id": p.arxiv_id,
            "title": p.title,
            "authors": authors[:3],
            "abstract_summary": p.abstract_summary or "",
            "url": p.url,
            "related_pages": related[:3],
        })

    sections = [
        {"category": cat, "label": cat_labels.get(cat, cat), "papers": ps[:5]}
        for cat, ps in by_cat.items()
    ]
    return {"date": target, "sections": sections, "total": len(papers)}
