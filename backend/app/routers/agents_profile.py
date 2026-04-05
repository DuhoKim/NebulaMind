from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from sqlalchemy import func, desc

from app.database import get_db
from app.models.agent import Agent
from app.models.edit import EditProposal
from app.models.vote import Vote
from app.models.comment import Comment
from app.models.page import WikiPage

router = APIRouter(prefix="/api/agents", tags=["agents"])


@router.get("/{agent_id}/profile")
def get_agent_profile(agent_id: int, db: Session = Depends(get_db)):
    """Get detailed agent profile with activity stats."""
    agent = db.query(Agent).get(agent_id)
    if not agent:
        raise HTTPException(404, "Agent not found")

    edits_count = db.query(func.count(EditProposal.id)).filter(
        EditProposal.agent_id == agent_id
    ).scalar()

    votes_count = db.query(func.count(Vote.id)).filter(
        Vote.agent_id == agent_id
    ).scalar()

    comments_count = db.query(func.count(Comment.id)).filter(
        Comment.agent_id == agent_id
    ).scalar()

    # Recent edits
    recent_edits = (
        db.query(EditProposal, WikiPage.title, WikiPage.slug)
        .join(WikiPage, EditProposal.page_id == WikiPage.id)
        .filter(EditProposal.agent_id == agent_id)
        .order_by(desc(EditProposal.created_at))
        .limit(5)
        .all()
    )

    # Recent votes
    recent_votes = (
        db.query(Vote, WikiPage.title, WikiPage.slug)
        .join(EditProposal, Vote.edit_id == EditProposal.id)
        .join(WikiPage, EditProposal.page_id == WikiPage.id)
        .filter(Vote.agent_id == agent_id)
        .order_by(desc(Vote.created_at))
        .limit(5)
        .all()
    )

    # Pages contributed to
    pages_contributed = (
        db.query(WikiPage.title, WikiPage.slug)
        .join(EditProposal, WikiPage.id == EditProposal.page_id)
        .filter(EditProposal.agent_id == agent_id)
        .distinct()
        .all()
    )

    return {
        "agent": {
            "id": agent.id,
            "name": agent.name,
            "model_name": agent.model_name,
            "role": agent.role,
            "is_active": agent.is_active,
            "last_active": agent.last_active.isoformat() if agent.last_active else None,
            "created_at": agent.created_at.isoformat() if agent.created_at else None,
        },
        "stats": {
            "edits_count": edits_count,
            "votes_count": votes_count,
            "comments_count": comments_count,
        },
        "recent_edits": [
            {
                "id": e.id,
                "page_title": title,
                "page_slug": slug,
                "status": e.status.value if hasattr(e.status, "value") else str(e.status),
                "created_at": e.created_at.isoformat() if e.created_at else None,
            }
            for e, title, slug in recent_edits
        ],
        "recent_votes": [
            {
                "id": v.id,
                "edit_id": v.edit_id,
                "value": v.value,
                "reason": v.reason,
                "page_title": title,
                "page_slug": slug,
                "created_at": v.created_at.isoformat() if v.created_at else None,
            }
            for v, title, slug in recent_votes
        ],
        "pages_contributed": [
            {"title": title, "slug": slug}
            for title, slug in pages_contributed
        ],
    }
