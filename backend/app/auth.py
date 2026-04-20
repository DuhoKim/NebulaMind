"""API key authentication dependency for NebulaMind."""

from fastapi import Depends, Header, HTTPException
from sqlalchemy.orm import Session

from app.database import get_db
from app.models.agent import Agent


def require_api_key(
    x_api_key: str = Header(..., description="Agent API key"),
    db: Session = Depends(get_db),
) -> Agent:
    """Validate X-API-Key header and return the corresponding Agent."""
    agent = db.query(Agent).filter(Agent.api_key == x_api_key).first()
    if not agent:
        raise HTTPException(status_code=401, detail="Invalid API key")
    return agent
