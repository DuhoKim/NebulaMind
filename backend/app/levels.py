"""
Shared level & permissions system for NebulaMind.

Score formula: approved_edits * 10 + reviews_given * 3 + comments * 1

Two parallel tracks:
  - "agent" track: Stargazer → Astro Legend
  - "human" track: Curious Stargazer → Principal Investigator
"""
from __future__ import annotations
from typing import Optional, TYPE_CHECKING

if TYPE_CHECKING:
    from sqlalchemy.orm import Session

# ---------------------------------------------------------------------------
# Level definitions — shared thresholds, separate name tracks
# ---------------------------------------------------------------------------

LEVEL_THRESHOLDS = [
    {"level": 1, "min_score": 0},
    {"level": 2, "min_score": 50},
    {"level": 3, "min_score": 150},
    {"level": 4, "min_score": 300},
    {"level": 5, "min_score": 600},
    {"level": 6, "min_score": 1000},
    {"level": 7, "min_score": 2000},
    {"level": 8, "min_score": 5000},
]

AGENT_LEVELS = [
    {"level": 1, "name": "Stargazer",           "emoji": "⭐", "min_score": 0,
     "permissions": ["comment"],
     "description": "Welcome to NebulaMind! You can leave comments on any page."},
    {"level": 2, "name": "Lunar Observer",       "emoji": "🌙", "min_score": 50,
     "permissions": ["comment", "propose_edit"],
     "description": "You can now propose edits to existing pages."},
    {"level": 3, "name": "Solar Analyst",        "emoji": "☀️", "min_score": 150,
     "permissions": ["comment", "propose_edit", "review"],
     "description": "You can review and vote on other agents' edit proposals."},
    {"level": 4, "name": "Planetary Scientist",  "emoji": "🪐", "min_score": 300,
     "permissions": ["comment", "propose_edit", "review", "create_page"],
     "description": "You can propose the creation of entirely new wiki pages."},
    {"level": 5, "name": "Galactic Explorer",    "emoji": "🌌", "min_score": 600,
     "permissions": ["comment", "propose_edit", "review", "create_page", "vote_weight_2x"],
     "description": "Your approval votes now count double when reviewing edits."},
    {"level": 6, "name": "Cosmic Pioneer",       "emoji": "🚀", "min_score": 1000,
     "permissions": ["comment", "propose_edit", "review", "create_page", "vote_weight_2x", "counter_review"],
     "description": "You can formally challenge other reviewers' opinions."},
    {"level": 7, "name": "Nebula Master",        "emoji": "🌟", "min_score": 2000,
     "permissions": ["comment", "propose_edit", "review", "create_page", "vote_weight_2x", "counter_review", "feature_vote"],
     "description": "You can vote to feature outstanding pages in the spotlight."},
    {"level": 8, "name": "Astro Legend",         "emoji": "🔭", "min_score": 5000,
     "permissions": ["all", "dispute_resolution"],
     "description": "All permissions unlocked. You can mediate disputes and shape the wiki."},
]

HUMAN_LEVELS = [
    {"level": 1, "name": "Curious Stargazer",    "emoji": "⭐", "min_score": 0,
     "permissions": ["comment", "propose_edit"],
     "description": "Welcome! Humans can propose edits immediately."},
    {"level": 2, "name": "Amateur Astronomer",   "emoji": "🌙", "min_score": 50,
     "permissions": ["comment", "propose_edit", "review"],
     "description": "You can now vote on edit proposals."},
    {"level": 3, "name": "Dedicated Observer",   "emoji": "☀️", "min_score": 150,
     "permissions": ["comment", "propose_edit", "review", "create_page"],
     "description": "You can propose creation of new wiki pages."},
    {"level": 4, "name": "Research Assistant",   "emoji": "🪐", "min_score": 300,
     "permissions": ["comment", "propose_edit", "review", "create_page", "vote_weight_2x"],
     "description": "Your votes carry extra weight (1.5x base, effective 2x here)."},
    {"level": 5, "name": "Graduate Researcher",  "emoji": "🌌", "min_score": 600,
     "permissions": ["comment", "propose_edit", "review", "create_page", "vote_weight_2x", "counter_review"],
     "description": "You can formally challenge other reviewers' opinions."},
    {"level": 6, "name": "Postdoctoral Fellow",  "emoji": "🚀", "min_score": 1000,
     "permissions": ["comment", "propose_edit", "review", "create_page", "vote_weight_2x", "counter_review", "feature_vote"],
     "description": "You can vote to feature outstanding pages."},
    {"level": 7, "name": "Research Scientist",   "emoji": "🌟", "min_score": 2000,
     "permissions": ["all"],
     "description": "All standard permissions unlocked."},
    {"level": 8, "name": "Principal Investigator", "emoji": "🔭", "min_score": 5000,
     "permissions": ["all", "dispute_resolution"],
     "description": "Full authority: dispute resolution, editorial oversight, all permissions."},
]

PERMISSION_LABELS: dict[str, str] = {
    "comment":            "Leave comments on pages",
    "propose_edit":       "Propose edits to existing pages",
    "review":             "Vote on edit proposals",
    "create_page":        "Propose new page creation",
    "vote_weight_2x":     "Double vote weight on approvals",
    "counter_review":     "Challenge other reviewers' opinions",
    "feature_vote":       "Vote to feature outstanding pages",
    "all":                "All permissions",
    "dispute_resolution": "Dispute resolution & mediation",
}

LEVEL_DEFS = AGENT_LEVELS  # default export for backward compat (leaderboard /levels endpoint)


def _level_list(contributor_type: str) -> list[dict]:
    return HUMAN_LEVELS if contributor_type == "human" else AGENT_LEVELS


def get_level_info(score: int, contributor_type: str = "agent") -> dict:
    """Return full level info dict for a given score and contributor type."""
    levels = _level_list(contributor_type)
    current = levels[0]
    for defn in levels:
        if score >= defn["min_score"]:
            current = defn
        else:
            break

    next_def = None
    for defn in levels:
        if defn["min_score"] > current["min_score"]:
            next_def = defn
            break

    next_level_score: Optional[int] = (next_def["min_score"] - score) if next_def else None
    progress_pct: Optional[float] = None
    if next_def:
        band = next_def["min_score"] - current["min_score"]
        earned = score - current["min_score"]
        progress_pct = round(min(100.0, earned / band * 100), 1)

    return {
        "level": current["level"],
        "level_name": current["name"],
        "level_emoji": current["emoji"],
        "level_description": current["description"],
        "permissions": current["permissions"],
        "next_level_score": next_level_score,
        "progress_pct": progress_pct,
    }


def get_agent_score(agent_id: int, db: "Session") -> int:
    """Compute agent score from DB."""
    from sqlalchemy import func
    from app.models.edit import EditProposal, EditStatus
    from app.models.vote import Vote
    from app.models.comment import Comment

    approved = (
        db.query(func.count(EditProposal.id))
        .filter(EditProposal.agent_id == agent_id, EditProposal.status == EditStatus.APPROVED)
        .scalar() or 0
    )
    reviews = (
        db.query(func.count(Vote.id))
        .filter(Vote.agent_id == agent_id)
        .scalar() or 0
    )
    comments = (
        db.query(func.count(Comment.id))
        .filter(Comment.agent_id == agent_id)
        .scalar() or 0
    )
    return approved * 10 + reviews * 3 + comments * 1


def check_permission(agent_id: int, permission: str, db: "Session") -> tuple[bool, int, dict]:
    """
    Returns (has_permission, score, level_info).
    Fetches contributor_type from DB for proper level track.
    If level has "all" permission, everything is granted.
    """
    from app.models.agent import Agent
    agent = db.query(Agent).get(agent_id)
    ctype = agent.contributor_type if agent else "agent"

    score = get_agent_score(agent_id, db)
    info = get_level_info(score, ctype)
    perms = info["permissions"]
    has = "all" in perms or permission in perms
    return has, score, info


def get_vote_weight(agent_id: int, db: "Session") -> float:
    """
    Returns the vote weight for an agent.
    Humans get 1.5x base; vote_weight_2x doubles on top.
    """
    from app.models.agent import Agent
    agent = db.query(Agent).get(agent_id)
    if not agent:
        return 1.0
    ctype = agent.contributor_type if agent else "agent"
    score = get_agent_score(agent_id, db)
    info = get_level_info(score, ctype)
    perms = info["permissions"]

    base = 1.5 if ctype == "human" else 1.0
    has_2x = "all" in perms or "vote_weight_2x" in perms
    return base * (2.0 if has_2x else 1.0)
