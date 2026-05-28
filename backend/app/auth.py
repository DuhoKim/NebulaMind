"""API key authentication dependency for NebulaMind."""

import hashlib
import datetime

from fastapi import Depends, Header, HTTPException, Request
from sqlalchemy.orm import Session
from sqlalchemy import text

from app.database import get_db
from app.models.agent import Agent


def _hash_key(key: str) -> str:
    return hashlib.sha256(key.encode()).hexdigest()


def _log_auth_event(db: Session, event_type: str, actor_id: int | None, payload: dict) -> None:
    try:
        import json
        db.execute(text("""
            INSERT INTO audit_events (event_type, actor_id, payload)
            VALUES (:evt, :aid, :payload::jsonb)
        """), {"evt": event_type, "aid": actor_id, "payload": json.dumps(payload)})
    except Exception:
        pass


def optional_api_key(
    x_api_key: str | None = Header(None, description="Agent API key (optional)"),
    db: Session = Depends(get_db),
) -> Agent | None:
    """Return Agent if X-API-Key header is valid, else None (anonymous)."""
    if not x_api_key:
        return None
    key_hash = _hash_key(x_api_key)
    agent = db.query(Agent).filter(Agent.api_key_hash == key_hash).first()
    return agent  # None if key invalid — treated as anonymous


def require_api_key(
    x_api_key: str = Header(..., description="Agent API key"),
    db: Session = Depends(get_db),
) -> Agent:
    """Validate X-API-Key header and return the corresponding Agent."""
    key_hash = _hash_key(x_api_key)
    agent = db.query(Agent).filter(Agent.api_key_hash == key_hash).first()
    if not agent:
        _log_auth_event(db, "agent_auth_fail", None, {"reason": "invalid_key"})
        db.commit()
        raise HTTPException(status_code=401, detail="Invalid API key")
    # Check expiry
    if agent.api_key_expires_at and agent.api_key_expires_at < datetime.datetime.utcnow():
        _log_auth_event(db, "agent_auth_fail", agent.id, {"reason": "key_expired"})
        db.commit()
        raise HTTPException(status_code=401, detail="API key expired — please rotate your key")
    # Check ban status: permanent (banned_until is None) or temporary (banned_until > now)
    if agent.ban_reason is not None:
        if agent.banned_until is None or agent.banned_until > datetime.datetime.utcnow():
            _log_auth_event(db, "agent_auth_fail", agent.id, {"reason": "agent_suspended"})
            db.commit()
            raise HTTPException(status_code=401, detail="Agent suspended")
    return agent
