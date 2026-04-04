from slowapi import Limiter
from slowapi.util import get_remote_address

limiter = Limiter(key_func=get_remote_address)

import re
import datetime as dt
from typing import Optional

import httpx
from fastapi import APIRouter, Depends, Request
from pydantic import BaseModel, Field
from sqlalchemy.orm import Session

from app.database import get_db
from app.models.feedback import Feedback
from app.config import settings

router = APIRouter(prefix="/api/feedback", tags=["feedback"])

AI_NAME_PATTERNS = re.compile(
    r"(gpt|claude|gemini|llama|mistral|copilot|chatgpt|bard|\bai\b|bot|agent)",
    re.IGNORECASE,
)


class FeedbackCreate(BaseModel):
    name: Optional[str] = Field(None, max_length=100)
    message: str = Field(..., min_length=1, max_length=2000)
    source: Optional[str] = Field(None, description="web or api")


class FeedbackOut(BaseModel):
    id: int
    name: Optional[str]
    message: str
    is_ai: bool
    ip_address: Optional[str]
    country: Optional[str]
    country_code: Optional[str]
    created_at: dt.datetime
    model_config = {"from_attributes": True}


def _detect_ai(name: Optional[str], explicit: Optional[bool]) -> bool:
    if explicit is not None:
        return explicit
    if name and AI_NAME_PATTERNS.search(name):
        return True
    return False


def _get_client_ip(request: Request) -> str:
    forwarded = request.headers.get("X-Forwarded-For")
    if forwarded:
        return forwarded.split(",")[0].strip()
    return request.client.host if request.client else "unknown"


def _geolocate(ip: str) -> dict:
    if ip in ("127.0.0.1", "localhost", "unknown") or ip.startswith("192.168.") or ip.startswith("10."):
        return {"country": "Local", "country_code": "LO"}
    try:
        r = httpx.get(f"https://ipapi.co/{ip}/json/", timeout=5, headers={"User-Agent": "NebulaMind/1.0"})
        if r.status_code == 200:
            data = r.json()
            return {"country": data.get("country_name"), "country_code": data.get("country_code")}
    except Exception as e:
        print(f"[geolocate] failed for {ip}: {e}")
    return {"country": None, "country_code": None}


def _notify_discord(feedback: Feedback) -> None:
    webhook = settings.DISCORD_WEBHOOK_URL
    if not webhook:
        return
    display = feedback.name or "익명"
    tag = "🤖 AI" if feedback.is_ai else "👤 사람"
    location = f" ({feedback.country})" if feedback.country and feedback.country != "Local" else ""
    content = f"📬 **새 피드백!** [{tag}] **{display}**{location}\n💬 {feedback.message}"
    try:
        httpx.post(webhook, json={"content": content}, timeout=10)
    except Exception as e:
        print(f"[feedback] Discord notify failed: {e}")


@router.get("", response_model=list[FeedbackOut], summary="List all feedback")
def list_feedback(db: Session = Depends(get_db)):
    return db.query(Feedback).order_by(Feedback.created_at.desc()).all()


@limiter.limit("10/minute")
@router.post("", response_model=FeedbackOut, status_code=201, summary="Submit feedback")
def submit_feedback(body: FeedbackCreate, request: Request, db: Session = Depends(get_db)):
    is_ai = body.source != "web" if body.source else _detect_ai(body.name, None)
    ip = _get_client_ip(request)
    geo = _geolocate(ip)
    fb = Feedback(
        name=body.name or None, message=body.message, is_ai=is_ai,
        ip_address=ip, country=geo.get("country"), country_code=geo.get("country_code"),
    )
    db.add(fb)
    db.commit()
    db.refresh(fb)
    _notify_discord(fb)
    return fb
