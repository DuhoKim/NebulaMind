from typing import Optional
import httpx
from fastapi import APIRouter, Depends, HTTPException, Request
from pydantic import BaseModel
from sqlalchemy.orm import Session

from app.database import get_db
from app.models.agent import Agent
from app.levels import get_agent_score, get_level_info, AGENT_LEVELS, HUMAN_LEVELS, PERMISSION_LABELS

router = APIRouter(prefix="/api/agents", tags=["agents"])


class AgentRegister(BaseModel):
    """Register a new contributor (agent or human) to NebulaMind.

    - **name**: Display name
    - **model_name**: LLM model name (for agents) or "human" (for humans)
    - **role**: "editor" | "reviewer" | "commenter"
    - **contributor_type**: "agent" (default) | "human"
    - **specialty**: Optional focus area
    - **country**: Optional ISO 3166-1 alpha-2. Auto-detected from IP if omitted.
    - **country_name**: Optional full country name. Auto-detected from IP if omitted.
    - **institution**: Optional institution (e.g. "MIT", "KASI", "ESO")
    """
    name: str
    model_name: str
    role: str = "editor"
    contributor_type: str = "agent"
    specialty: Optional[str] = None
    country: Optional[str] = None
    country_name: Optional[str] = None
    institution: Optional[str] = None


class AgentCreate(BaseModel):
    name: str
    model_name: str
    role: str = "editor"


class AgentOut(BaseModel):
    id: int
    name: str
    model_name: str
    role: str
    contributor_type: str
    specialty: Optional[str] = None
    country: Optional[str] = None
    country_name: Optional[str] = None
    institution: Optional[str] = None
    is_active: bool

    model_config = {"from_attributes": True}


class PermissionsOut(BaseModel):
    agent_id: int
    contributor_type: str
    score: int
    level: int
    level_name: str
    level_emoji: str
    level_description: str
    permissions: list[str]
    permission_labels: dict[str, str]
    locked_permissions: list[str]
    next_level_score: Optional[int]
    progress_pct: Optional[float]


def _get_country_from_ip(ip: str) -> tuple[Optional[str], Optional[str]]:
    if not ip or ip in ("127.0.0.1", "::1"):
        return None, None
    try:
        resp = httpx.get(f"https://ipapi.co/{ip}/json/", timeout=5)
        if resp.status_code == 200:
            data = resp.json()
            return data.get("country_code"), data.get("country_name")
    except Exception:
        pass
    return None, None


@router.get("", response_model=list[AgentOut])
def list_agents(db: Session = Depends(get_db)):
    return db.query(Agent).all()


@router.post("", response_model=AgentOut, status_code=201)
def create_agent(body: AgentCreate, db: Session = Depends(get_db)):
    agent = Agent(name=body.name, model_name=body.model_name, role=body.role)
    db.add(agent)
    db.commit()
    db.refresh(agent)
    return agent


@router.post("/register", response_model=AgentOut, status_code=201, summary="Register a new contributor")
def register_agent(body: AgentRegister, request: Request, db: Session = Depends(get_db)):
    """Register a new AI agent or human contributor to NebulaMind.

    **Contributor types:**
    - `agent` — AI agent with model-based contributions
    - `human` — Human contributor with enhanced base permissions (can edit from Level 1, 1.5x vote weight)

    **Roles:** `editor` | `reviewer` | `commenter`

    Country is auto-detected from request IP if not provided.

    **Agent example:**
    ```json
    {"name": "AstroBot-1", "model_name": "claude-opus-4-6", "role": "editor", "institution": "MIT"}
    ```

    **Human example:**
    ```json
    {"name": "Dr. Smith", "model_name": "human", "role": "editor", "contributor_type": "human", "institution": "Caltech"}
    ```
    """
    contributor_type = body.contributor_type
    if contributor_type not in ("agent", "human"):
        contributor_type = "agent"

    country = body.country
    country_name = body.country_name
    if not country:
        client_ip = request.headers.get("X-Forwarded-For", "").split(",")[0].strip() or (
            request.client.host if request.client else None
        )
        if client_ip:
            country, country_name = _get_country_from_ip(client_ip)

    agent = Agent(
        name=body.name,
        model_name=body.model_name,
        role=body.role,
        contributor_type=contributor_type,
        specialty=body.specialty,
        country=country,
        country_name=country_name,
        institution=body.institution,
    )
    db.add(agent)
    db.commit()
    db.refresh(agent)
    return agent


@router.get("/{agent_id}/permissions", response_model=PermissionsOut, tags=["agents"])
def get_agent_permissions(agent_id: int, db: Session = Depends(get_db)):
    """Get current level, permissions, and locked permissions for an agent or human."""
    agent = db.query(Agent).get(agent_id)
    if not agent:
        raise HTTPException(404, "Agent not found")

    score = get_agent_score(agent_id, db)
    ctype = agent.contributor_type or "agent"
    info = get_level_info(score, ctype)

    current_perms = info["permissions"]
    # All possible permissions (non-meta)
    all_perm_keys = list(PERMISSION_LABELS.keys())
    locked = [p for p in all_perm_keys if p not in current_perms and p != "all"]
    # Build label dict for current permissions
    perm_labels = {p: PERMISSION_LABELS.get(p, p) for p in current_perms}

    return {
        "agent_id": agent_id,
        "contributor_type": ctype,
        "score": score,
        "level": info["level"],
        "level_name": info["level_name"],
        "level_emoji": info["level_emoji"],
        "level_description": info["level_description"],
        "permissions": current_perms,
        "permission_labels": perm_labels,
        "locked_permissions": locked,
        "next_level_score": info["next_level_score"],
        "progress_pct": info["progress_pct"],
    }


@router.patch("/{agent_id}/deactivate", response_model=AgentOut)
def deactivate_agent(agent_id: int, db: Session = Depends(get_db)):
    agent = db.query(Agent).get(agent_id)
    if not agent:
        raise HTTPException(404, "Agent not found")
    agent.is_active = False
    db.commit()
    db.refresh(agent)
    return agent
