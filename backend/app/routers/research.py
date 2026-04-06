"""
arXiv Research Frontier router — DB-backed with Celery fetch.
"""
import datetime as dt
import json

from fastapi import APIRouter, Depends, Query
from sqlalchemy import desc
from sqlalchemy.orm import Session

from app.database import get_db
from app.models.arxiv import ArxivPaper

router = APIRouter(prefix="/api/research", tags=["research"])


@router.get("/arxiv")
def get_arxiv_papers(
    category: str = Query(default="astro-ph.GA", description="arXiv category"),
    limit: int = Query(default=10, ge=1, le=50),
    days: int = Query(default=30, description="papers from last N days"),
    db: Session = Depends(get_db),
):
    """Return arXiv papers stored in DB for the given category."""
    cutoff = (dt.date.today() - dt.timedelta(days=days)).isoformat()
    papers = (
        db.query(ArxivPaper)
        .filter(ArxivPaper.category == category)
        .filter(ArxivPaper.submitted >= cutoff)
        .order_by(desc(ArxivPaper.submitted), desc(ArxivPaper.created_at))
        .limit(limit)
        .all()
    )
    return [
        {
            "arxiv_id": p.arxiv_id,
            "title": p.title,
            "authors": json.loads(p.authors) if p.authors else [],
            "abstract_summary": p.abstract_summary,
            "submitted": p.submitted,
            "related_pages": json.loads(p.related_pages) if p.related_pages else [],
            "url": p.url,
            "category": p.category,
        }
        for p in papers
    ]


@router.post("/arxiv/trigger")
def trigger_arxiv_fetch():
    """Manually trigger arXiv fetch (for testing)."""
    from app.agent_loop.tasks import fetch_arxiv_daily
    fetch_arxiv_daily.delay()
    return {"status": "triggered"}
