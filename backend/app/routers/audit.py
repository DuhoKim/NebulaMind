"""Audit log API endpoints."""
import secrets
from fastapi import APIRouter, Depends, Query, Header, HTTPException
from sqlalchemy.orm import Session
from sqlalchemy import text

from app.database import get_db
from app.config import settings

router = APIRouter(prefix="/api/audit", tags=["audit"])

ADMIN_KEY = getattr(settings, "ADMIN_KEY", "")


@router.get("/events", summary="Recent audit events (public fields)")
def get_audit_events(
    limit: int = Query(default=100, le=500),
    db: Session = Depends(get_db),
):
    rows = db.execute(text(
        "SELECT event_type, target_kind, target_id, created_at "
        "FROM audit_events ORDER BY created_at DESC LIMIT :limit"
    ), {"limit": limit}).all()
    return [
        {
            "event_type": r.event_type,
            "target_kind": r.target_kind,
            "target_id": r.target_id,
            "created_at": r.created_at.isoformat() if r.created_at else None,
        }
        for r in rows
    ]


@router.get("/events/admin", summary="Full audit events (admin only)")
def get_audit_events_admin(
    limit: int = Query(default=500, le=2000),
    x_admin_key: str = Header(default=""),
    db: Session = Depends(get_db),
):
    if not ADMIN_KEY or not secrets.compare_digest(x_admin_key, ADMIN_KEY):
        raise HTTPException(status_code=403, detail="Forbidden")

    rows = db.execute(text(
        "SELECT event_type, actor_id, actor_ip_hash, target_kind, target_id, payload, created_at "
        "FROM audit_events ORDER BY created_at DESC LIMIT :limit"
    ), {"limit": limit}).all()
    return [
        {
            "event_type": r.event_type,
            "actor_id": r.actor_id,
            "actor_ip_hash": r.actor_ip_hash,
            "target_kind": r.target_kind,
            "target_id": r.target_id,
            "payload": r.payload,
            "created_at": r.created_at.isoformat() if r.created_at else None,
        }
        for r in rows
    ]
