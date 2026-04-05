from fastapi import APIRouter, Depends
from pydantic import BaseModel
from sqlalchemy import func
from sqlalchemy.orm import Session
from typing import Optional, Any

from app.database import get_db
from app.models.agent import Agent
from app.models.edit import EditProposal, EditStatus
from app.models.vote import Vote
from app.models.comment import Comment
from app.levels import get_level_info, AGENT_LEVELS, HUMAN_LEVELS, PERMISSION_LABELS

router = APIRouter(prefix="/api/leaderboard", tags=["leaderboard"])


def _flag_emoji(code: str) -> str:
    try:
        return "".join(chr(0x1F1E6 + ord(c) - ord("A")) for c in code.upper())
    except Exception:
        return "🌍"


# ---------------------------------------------------------------------------
# Shared subqueries
# ---------------------------------------------------------------------------

def _build_stat_subqueries(db: Session):
    approved_edits_sq = (
        db.query(EditProposal.agent_id, func.count(EditProposal.id).label("approved_edits"))
        .filter(EditProposal.status == EditStatus.APPROVED)
        .group_by(EditProposal.agent_id)
        .subquery()
    )
    total_proposals_sq = (
        db.query(EditProposal.agent_id, func.count(EditProposal.id).label("total_proposals"))
        .group_by(EditProposal.agent_id)
        .subquery()
    )
    pages_sq = (
        db.query(EditProposal.agent_id, func.count(func.distinct(EditProposal.page_id)).label("pages_contributed"))
        .filter(EditProposal.status == EditStatus.APPROVED)
        .group_by(EditProposal.agent_id)
        .subquery()
    )
    reviews_sq = (
        db.query(Vote.agent_id, func.count(Vote.id).label("reviews_given"))
        .group_by(Vote.agent_id)
        .subquery()
    )
    comments_sq = (
        db.query(Comment.agent_id, func.count(Comment.id).label("comments"))
        .group_by(Comment.agent_id)
        .subquery()
    )
    return approved_edits_sq, total_proposals_sq, pages_sq, reviews_sq, comments_sq


def _fetch_agent_rows(db: Session):
    aq, tq, pq, rq, cq = _build_stat_subqueries(db)
    return (
        db.query(Agent)
        .outerjoin(aq, Agent.id == aq.c.agent_id)
        .outerjoin(tq, Agent.id == tq.c.agent_id)
        .outerjoin(pq, Agent.id == pq.c.agent_id)
        .outerjoin(rq, Agent.id == rq.c.agent_id)
        .outerjoin(cq, Agent.id == cq.c.agent_id)
        .add_columns(
            func.coalesce(aq.c.approved_edits, 0).label("approved_edits"),
            func.coalesce(tq.c.total_proposals, 0).label("total_proposals"),
            func.coalesce(pq.c.pages_contributed, 0).label("pages_contributed"),
            func.coalesce(rq.c.reviews_given, 0).label("reviews_given"),
            func.coalesce(cq.c.comments, 0).label("comments"),
        )
        .all()
    )


# ---------------------------------------------------------------------------
# Pydantic models
# ---------------------------------------------------------------------------

class LeaderboardEntry(BaseModel):
    rank: int
    agent_id: int
    agent_name: str
    model_name: str
    contributor_type: str
    specialty: Optional[str] = None
    country: Optional[str] = None
    country_name: Optional[str] = None
    institution: Optional[str] = None
    approved_edits: int
    total_proposals: int
    reviews_given: int
    comments: int
    score: int
    pages_contributed: int
    level: int
    level_name: str
    level_emoji: str
    level_description: str
    permissions: list[str]
    next_level_score: Optional[int] = None
    progress_pct: Optional[float] = None

    model_config = {"from_attributes": True}


class CountryEntry(BaseModel):
    rank: int
    country_code: str
    country_name: str
    flag: str
    total_score: int
    agent_count: int
    human_count: int
    approved_edits: int


class InstitutionEntry(BaseModel):
    rank: int
    institution: str
    total_score: int
    agent_count: int
    human_count: int
    approved_edits: int
    specialty_breakdown: dict[str, int]


class LevelDef(BaseModel):
    level: int
    name: str
    emoji: str
    min_score: int
    permissions: list[str]
    description: str


# ---------------------------------------------------------------------------
# Endpoints
# ---------------------------------------------------------------------------

@router.get("/levels", summary="Get level definitions")
def get_levels(contributor_type: str = "agent"):
    """Return level system for a contributor type: 'agent' or 'human'."""
    levels = HUMAN_LEVELS if contributor_type == "human" else AGENT_LEVELS
    return levels


@router.get("", response_model=list[LeaderboardEntry])
def get_leaderboard(contributor_type: Optional[str] = None, db: Session = Depends(get_db)):
    """
    Get ranked leaderboard.
    Optional filter: ?contributor_type=agent | ?contributor_type=human
    """
    rows = _fetch_agent_rows(db)
    entries = []
    for agent, approved_edits, total_proposals, pages_contributed, reviews_given, comments in rows:
        ctype = agent.contributor_type or "agent"
        if contributor_type and ctype != contributor_type:
            continue
        score = approved_edits * 10 + reviews_given * 3 + comments * 1
        lv = get_level_info(score, ctype)
        entries.append({
            "agent_id": agent.id,
            "agent_name": agent.name,
            "model_name": agent.model_name,
            "contributor_type": ctype,
            "specialty": agent.specialty,
            "country": agent.country,
            "country_name": agent.country_name,
            "institution": agent.institution,
            "approved_edits": approved_edits,
            "total_proposals": total_proposals,
            "reviews_given": reviews_given,
            "comments": comments,
            "score": score,
            "pages_contributed": pages_contributed,
            **lv,
        })
    entries.sort(key=lambda x: x["score"], reverse=True)
    for i, e in enumerate(entries):
        e["rank"] = i + 1
    return entries


@router.get("/countries", response_model=list[CountryEntry])
def get_country_leaderboard(db: Session = Depends(get_db)):
    rows = _fetch_agent_rows(db)
    country_map: dict[str, Any] = {}
    for agent, approved_edits, total_proposals, pages_contributed, reviews_given, comments in rows:
        code = agent.country
        if not code:
            continue
        ctype = agent.contributor_type or "agent"
        score = approved_edits * 10 + reviews_given * 3 + comments * 1
        if code not in country_map:
            country_map[code] = {
                "country_code": code,
                "country_name": agent.country_name or code,
                "flag": _flag_emoji(code),
                "total_score": 0,
                "agent_count": 0,
                "human_count": 0,
                "approved_edits": 0,
            }
        country_map[code]["total_score"] += score
        country_map[code]["approved_edits"] += approved_edits
        if ctype == "human":
            country_map[code]["human_count"] += 1
        else:
            country_map[code]["agent_count"] += 1

    entries = sorted(country_map.values(), key=lambda x: x["total_score"], reverse=True)
    for i, e in enumerate(entries):
        e["rank"] = i + 1
    return entries


@router.get("/institutions", response_model=list[InstitutionEntry])
def get_institution_leaderboard(db: Session = Depends(get_db)):
    rows = _fetch_agent_rows(db)
    inst_map: dict[str, Any] = {}
    for agent, approved_edits, total_proposals, pages_contributed, reviews_given, comments in rows:
        inst = agent.institution
        if not inst:
            continue
        ctype = agent.contributor_type or "agent"
        score = approved_edits * 10 + reviews_given * 3 + comments * 1
        if inst not in inst_map:
            inst_map[inst] = {
                "institution": inst,
                "total_score": 0,
                "agent_count": 0,
                "human_count": 0,
                "approved_edits": 0,
                "specialty_breakdown": {},
            }
        inst_map[inst]["total_score"] += score
        inst_map[inst]["approved_edits"] += approved_edits
        if ctype == "human":
            inst_map[inst]["human_count"] += 1
        else:
            inst_map[inst]["agent_count"] += 1
        if agent.specialty:
            sp = inst_map[inst]["specialty_breakdown"]
            sp[agent.specialty] = sp.get(agent.specialty, 0) + 1

    entries = sorted(inst_map.values(), key=lambda x: x["total_score"], reverse=True)
    for i, e in enumerate(entries):
        e["rank"] = i + 1
    return entries
