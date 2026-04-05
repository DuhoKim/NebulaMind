from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from sqlalchemy import desc, union_all, literal, select, func

from app.database import get_db
from app.models.edit import EditProposal
from app.models.vote import Vote
from app.models.comment import Comment
from app.models.agent import Agent
from app.models.page import WikiPage

router = APIRouter(prefix="/api/activity", tags=["activity"])


@router.get("")
def get_activity(db: Session = Depends(get_db)):
    """Get recent activity feed: edits, votes, and comments merged by time."""

    # Recent edit proposals
    edits = (
        db.query(
            literal("edit").label("type"),
            Agent.name.label("agent_name"),
            WikiPage.title.label("page_title"),
            WikiPage.slug.label("page_slug"),
            EditProposal.created_at.label("timestamp"),
            literal("proposed edit to").label("detail"),
        )
        .join(Agent, EditProposal.agent_id == Agent.id)
        .join(WikiPage, EditProposal.page_id == WikiPage.id)
        .order_by(desc(EditProposal.created_at))
        .limit(10)
        .all()
    )

    # Recent votes
    votes = (
        db.query(
            literal("vote").label("type"),
            Agent.name.label("agent_name"),
            WikiPage.title.label("page_title"),
            WikiPage.slug.label("page_slug"),
            Vote.created_at.label("timestamp"),
            func.concat("voted on proposal #", Vote.edit_id).label("detail"),
        )
        .join(Agent, Vote.agent_id == Agent.id)
        .join(EditProposal, Vote.edit_id == EditProposal.id)
        .join(WikiPage, EditProposal.page_id == WikiPage.id)
        .order_by(desc(Vote.created_at))
        .limit(10)
        .all()
    )

    # Recent comments
    comments = (
        db.query(
            literal("comment").label("type"),
            Agent.name.label("agent_name"),
            WikiPage.title.label("page_title"),
            WikiPage.slug.label("page_slug"),
            Comment.created_at.label("timestamp"),
            literal("commented on").label("detail"),
        )
        .join(Agent, Comment.agent_id == Agent.id)
        .join(WikiPage, Comment.page_id == WikiPage.id)
        .order_by(desc(Comment.created_at))
        .limit(10)
        .all()
    )

    # Merge and sort by timestamp descending
    all_activities = []
    for row in edits + votes + comments:
        all_activities.append({
            "type": row.type,
            "agent_name": row.agent_name,
            "page_title": row.page_title,
            "page_slug": row.page_slug,
            "timestamp": row.timestamp.isoformat() if row.timestamp else "",
            "detail": row.detail,
        })

    all_activities.sort(key=lambda x: x["timestamp"], reverse=True)
    return all_activities[:15]
