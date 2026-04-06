"""
Researcher Spotlight router — submit your paper for AI summary + wiki linking.
"""
import datetime as dt
import json

import httpx
from fastapi import APIRouter, Depends, HTTPException, Query
from pydantic import BaseModel, EmailStr
from sqlalchemy import desc
from sqlalchemy.orm import Session

from app.config import settings
from app.database import get_db
from app.models.spotlight import Spotlight
from app.models.page import WikiPage

router = APIRouter(prefix="/api/spotlight", tags=["spotlight"])

# Launch period: no level requirement (SPOTLIGHT_LEVEL_REQUIRED = 0)
SPOTLIGHT_LEVEL_REQUIRED = 0
MAX_PER_MONTH = 1  # per email during launch


class SpotlightRequest(BaseModel):
    email: EmailStr
    arxiv_id: str  # e.g. "2604.01234"


def _fetch_arxiv_metadata(arxiv_id: str) -> dict:
    """Fetch paper metadata from arXiv API."""
    clean_id = arxiv_id.replace("arXiv:", "").strip()
    url = f"http://export.arxiv.org/api/query?id_list={clean_id}"
    try:
        resp = httpx.get(url, timeout=15)
        resp.raise_for_status()
        text = resp.text
        # Quick XML parsing for title and authors
        import re
        title_match = re.search(r"<title>(.*?)</title>", text, re.DOTALL)
        title = title_match.group(1).strip() if title_match else ""
        # Skip first <title> which is feed title
        titles = re.findall(r"<title>(.*?)</title>", text, re.DOTALL)
        if len(titles) >= 2:
            title = titles[1].strip()
        
        authors = re.findall(r"<name>(.*?)</name>", text)
        abstract_match = re.search(r"<summary>(.*?)</summary>", text, re.DOTALL)
        abstract = abstract_match.group(1).strip() if abstract_match else ""
        
        return {
            "title": title,
            "authors": authors,
            "abstract": abstract,
            "url": f"https://arxiv.org/abs/{clean_id}",
        }
    except Exception as e:
        raise HTTPException(400, f"Could not fetch arXiv paper: {e}")


def _match_wiki_pages(title: str, abstract: str, db: Session) -> list[str]:
    """Simple keyword matching to find related wiki pages."""
    pages = db.query(WikiPage).all()
    related = []
    text = (title + " " + abstract).lower()
    for page in pages:
        keywords = page.title.lower().split()
        if any(kw in text for kw in keywords if len(kw) > 3):
            related.append(page.slug)
    return related[:5]


@router.post("")
def submit_spotlight(req: SpotlightRequest, db: Session = Depends(get_db)):
    """Submit a paper for Researcher Spotlight."""
    # Check monthly limit per email
    month_start = dt.date.today().replace(day=1).isoformat()
    this_month = (
        db.query(Spotlight)
        .filter(Spotlight.email == req.email, Spotlight.created_at >= month_start)
        .count()
    )
    if this_month >= MAX_PER_MONTH:
        raise HTTPException(429, f"Monthly limit reached ({MAX_PER_MONTH}/month)")

    # Check duplicate
    existing = db.query(Spotlight).filter(Spotlight.arxiv_id == req.arxiv_id).first()
    if existing:
        raise HTTPException(409, "This paper has already been submitted")

    # Fetch metadata from arXiv
    meta = _fetch_arxiv_metadata(req.arxiv_id)

    # Generate AI summary
    try:
        from app.agent_loop.tasks import _chat
        summary = _chat(
            "llama3.1-8b",
            "You are a concise astronomy writer. Summarize this paper in 2-3 sentences for a general astronomy audience.",
            f"Title: {meta['title']}\nAbstract: {meta['abstract']}"
        )
    except Exception:
        summary = meta["abstract"][:300]

    # Match wiki pages
    related = _match_wiki_pages(meta["title"], meta["abstract"], db)

    spot = Spotlight(
        email=req.email,
        arxiv_id=req.arxiv_id,
        title=meta["title"],
        authors=json.dumps(meta["authors"]),
        summary=summary.strip()[:500],
        related_pages=json.dumps(related) if related else None,
        expires_at=dt.datetime.now(dt.UTC) + dt.timedelta(days=30),
    )
    db.add(spot)
    db.commit()

    return {
        "status": "submitted",
        "id": spot.id,
        "title": meta["title"],
        "summary": spot.summary,
        "related_pages": related,
    }


@router.get("")
def list_spotlights(
    limit: int = Query(default=10, ge=1, le=50),
    db: Session = Depends(get_db),
):
    """List recent active spotlights."""
    spots = (
        db.query(Spotlight)
        .filter(Spotlight.status == "active")
        .order_by(desc(Spotlight.created_at))
        .limit(limit)
        .all()
    )
    return [
        {
            "id": s.id,
            "arxiv_id": s.arxiv_id,
            "title": s.title,
            "authors": json.loads(s.authors) if s.authors else [],
            "summary": s.summary,
            "related_pages": json.loads(s.related_pages) if s.related_pages else [],
            "featured": s.featured,
            "created_at": s.created_at.isoformat() if s.created_at else None,
        }
        for s in spots
    ]


@router.get("/featured")
def featured_spotlights(db: Session = Depends(get_db)):
    """Get featured spotlights (for newsletter)."""
    spots = (
        db.query(Spotlight)
        .filter(Spotlight.featured.is_(True), Spotlight.status == "active")
        .order_by(desc(Spotlight.created_at))
        .limit(5)
        .all()
    )
    return [
        {
            "id": s.id,
            "arxiv_id": s.arxiv_id,
            "title": s.title,
            "summary": s.summary,
        }
        for s in spots
    ]
