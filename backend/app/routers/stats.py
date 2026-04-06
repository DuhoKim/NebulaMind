import datetime as dt
from typing import Optional

from fastapi import APIRouter, Depends, Request
from pydantic import BaseModel
from sqlalchemy import func
from sqlalchemy.orm import Session

from app.database import get_db
from app.models.visitor import Visit
from app.models.claim import Evidence

router = APIRouter(prefix="/api/stats", tags=["stats"])

AGENT_UA_PATTERNS = ("python", "httpx", "axios", "node-fetch", "curl", "bot", "agent", "gpt", "claude", "llama")


def _is_agent(request: Request) -> bool:
    ua = (request.headers.get("User-Agent") or "").lower()
    if any(p in ua for p in AGENT_UA_PATTERNS):
        return True
    if len(ua) < 20:
        return True
    return False


def _get_ip(request: Request) -> str:
    forwarded = request.headers.get("X-Forwarded-For")
    if forwarded:
        return forwarded.split(",")[0].strip()
    return request.client.host if request.client else "unknown"


class StatsOut(BaseModel):
    total_visits: int
    human_visits: int
    agent_visits: int
    today_visits: int
    today_human: int
    today_agent: int
    online_human: int
    online_agent: int
    unique_ips: int
    evidence_count: int


class VisitOut(BaseModel):
    visitor_type: str
    model_config = {"from_attributes": True}


@router.post("/visit", response_model=VisitOut, summary="Record a visit")
def record_visit(request: Request, path: Optional[str] = None, db: Session = Depends(get_db)):
    """Record a page visit. Deduplicates same IP within 30 minutes."""
    is_agent = _is_agent(request)
    ip = _get_ip(request)
    vtype = "agent" if is_agent else "human"

    # Deduplicate: skip if same IP visited in last 30 minutes
    thirty_min_ago = dt.datetime.now(dt.UTC) - dt.timedelta(minutes=30)
    recent = db.query(Visit).filter(
        Visit.ip_address == ip,
        Visit.created_at >= thirty_min_ago,
    ).first()
    if recent:
        return VisitOut(visitor_type=vtype)

    visit = Visit(
        visitor_type=vtype,
        ip_address=ip,
        path=path,
        user_agent=(request.headers.get("User-Agent") or "")[:500],
    )
    db.add(visit)
    db.commit()
    return visit


@router.get("", response_model=StatsOut, summary="Get visit statistics")
def get_stats(db: Session = Depends(get_db)):
    """Get visitor statistics."""
    today = dt.date.today()
    five_min_ago = dt.datetime.now(dt.UTC) - dt.timedelta(minutes=5)

    total = db.query(Visit).count()
    human = db.query(Visit).filter(Visit.visitor_type == "human").count()
    agent = db.query(Visit).filter(Visit.visitor_type == "agent").count()

    today_total = db.query(Visit).filter(func.date(Visit.created_at) == today).count()
    today_human = db.query(Visit).filter(func.date(Visit.created_at) == today, Visit.visitor_type == "human").count()
    today_agent = db.query(Visit).filter(func.date(Visit.created_at) == today, Visit.visitor_type == "agent").count()

    online_human = db.query(func.count(func.distinct(Visit.ip_address))).filter(Visit.created_at >= five_min_ago, Visit.visitor_type == "human").scalar() or 0
    online_agent = db.query(func.count(func.distinct(Visit.ip_address))).filter(Visit.created_at >= five_min_ago, Visit.visitor_type == "agent").scalar() or 0

    unique = db.query(func.count(func.distinct(Visit.ip_address))).scalar() or 0

    evidence_count = db.query(Evidence).count()

    return StatsOut(
        total_visits=total,
        human_visits=human,
        agent_visits=agent,
        today_visits=today_total,
        today_human=today_human,
        today_agent=today_agent,
        online_human=online_human,
        online_agent=online_agent,
        unique_ips=unique,
        evidence_count=evidence_count,
    )
