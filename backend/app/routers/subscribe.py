"""
Newsletter subscription router.
"""
import json
import uuid

from fastapi import APIRouter, Depends, HTTPException, Query
from pydantic import BaseModel, EmailStr
from sqlalchemy.orm import Session

from app.database import get_db
from app.models.subscriber import Subscriber

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
