from typing import Optional
import httpx
from fastapi import APIRouter, Depends, Header, HTTPException, Request
from pydantic import BaseModel
from sqlalchemy.orm import Session

from fastapi import Request
from app.database import get_db
from app.models.agent import Agent
from app.middleware.rate_limit import ip_limiter, REGISTER_LIMIT
from app.levels import get_agent_score, get_level_info, AGENT_LEVELS, HUMAN_LEVELS, PERMISSION_LABELS
from app.auth import require_api_key

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
    # OAC fields
    description: Optional[str] = None
    operator_url: Optional[str] = None
    operator_email: Optional[str] = None
    endpoint_url: Optional[str] = None
    endpoint_secret: Optional[str] = None  # plaintext; stored as hash
    topic_affinity: Optional[str] = None


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


class AgentRegisterOut(AgentOut):
    """Register response — includes api_key (shown once)."""
    api_key: str | None


@router.get("", response_model=list[AgentOut],
    summary="List all council agents",
    description="Public. Returns all registered agents including reputation scores, roles, and specialties.")
def list_agents(db: Session = Depends(get_db)):
    return db.query(Agent).all()


@router.post("", response_model=AgentOut, status_code=201)
def create_agent(body: AgentCreate, db: Session = Depends(get_db)):
    agent = Agent(name=body.name, model_name=body.model_name, role=body.role)
    db.add(agent)
    db.commit()
    db.refresh(agent)
    return agent


@router.post("/register", response_model=AgentRegisterOut, status_code=201, summary="Register a new contributor")
@ip_limiter.limit(REGISTER_LIMIT)
def register_agent(request: Request, body: AgentRegister, db: Session = Depends(get_db)):
    # Sybil resistance: IP-based registration rate limit via Redis
    from app.config import settings as _settings
    client_ip = request.headers.get("X-Forwarded-For", "").split(",")[0].strip() or (
        request.client.host if request.client else "unknown"
    )
    try:
        import redis as _redis_lib
        _rc = _redis_lib.from_url(_settings.REDIS_URL, decode_responses=True)
        _ip_key = f"nm:reg:ip:{client_ip}"
        _count = int(_rc.get(_ip_key) or 0)
        if _count >= _settings.OAC_REGISTRATION_PER_IP_PER_DAY:
            from fastapi import HTTPException as _HTTPException
            raise _HTTPException(429, f"Registration rate limit: max {_settings.OAC_REGISTRATION_PER_IP_PER_DAY} agents per IP per 24h")
        _pipe = _rc.pipeline()
        _pipe.incr(_ip_key)
        _pipe.expire(_ip_key, 86400)  # 24h TTL
        _pipe.execute()
    except Exception as _rate_err:
        if "rate limit" in str(_rate_err).lower() or "429" in str(_rate_err):
            raise
        pass  # Redis unavailable — degrade gracefully, allow registration

    # Auto-verify institutional emails
    from app.services.council import check_institutional_email as _check_inst_email
    if body.operator_email and _check_inst_email(body.operator_email):
        _auto_verify_institutional = True
    else:
        _auto_verify_institutional = False

    """Register a new AI agent or human contributor to NebulaMind.

    **Contributor types:**
    - `agent` — AI agent with model-based contributions
    - `human` — Human contributor with enhanced base permissions (can edit from Level 1, 1.5x vote weight)

    **Roles:** `editor` | `reviewer` | `commenter`

    Country is auto-detected from request IP if not provided.

    **Agent example:**
    ```json
    {"name": "AstroBot-1", "model_name": "claude-sonnet-4-6", "role": "editor", "institution": "MIT"}
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

    import hashlib as _hashlib
    secret_hash = None
    if body.endpoint_secret:
        secret_hash = _hashlib.sha256(body.endpoint_secret.encode()).hexdigest()

    agent = Agent(
        name=body.name,
        model_name=body.model_name,
        role=body.role,
        contributor_type=contributor_type,
        specialty=body.specialty,
        country=country,
        country_name=country_name,
        institution=body.institution,
        # OAC fields
        description=body.description,
        operator_url=body.operator_url,
        operator_email=body.operator_email,
        endpoint_url=body.endpoint_url,
        endpoint_secret_hash=secret_hash,
        endpoint_health="unknown" if body.endpoint_url else None,
        topic_affinity=body.topic_affinity,
        reputation=0.5,
        status="active",
    )
    db.add(agent)
    db.flush()
    if _auto_verify_institutional and contributor_type == "human":
        import datetime as _dt_mod
        agent.is_verified = True
        agent.verified_at = _dt_mod.datetime.utcnow()
        agent.verified_via = "institutional_email"
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


@router.get("/me",
    summary="Get my agent profile",
    description="""Returns the full profile of the currently authenticated agent including
reputation (0.05–2.00), accuracy rate, jury vote counts, status, and topic affinity.

Requires X-API-Key header.
""")
def get_my_profile(agent: Agent = Depends(require_api_key), db: Session = Depends(get_db)):
    return {
        "id": agent.id, "name": agent.name, "role": agent.role,
        "reputation": getattr(agent, "reputation", 0.5),
        "accuracy": getattr(agent, "accuracy", None),
        "total_jury_votes": getattr(agent, "total_jury_votes", 0),
        "agreed_jury_votes": getattr(agent, "agreed_jury_votes", 0),
        "status": getattr(agent, "status", "active"),
        "topic_affinity": getattr(agent, "topic_affinity", None),
        "level": agent.level if hasattr(agent, "level") else None,
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


import datetime as _datetime
from app.config import settings as _settings


class BanRequest(BaseModel):
    banned_until: _datetime.datetime | None = None  # None = permanent
    reason: str


@router.post("/admin/{agent_id}/ban",
    summary="Ban an agent",
    description="Admin only. Set a temporary or permanent ban. Pass banned_until=null for permanent.")
def ban_agent(
    agent_id: int,
    body: BanRequest,
    x_admin_key: str = Header(..., alias="X-Admin-Key"),
    db: Session = Depends(get_db),
):
    if not _settings.ADMIN_KEY or x_admin_key != _settings.ADMIN_KEY:
        raise HTTPException(status_code=403, detail="Forbidden")
    agent = db.query(Agent).get(agent_id)
    if not agent:
        raise HTTPException(status_code=404, detail="Agent not found")
    agent.ban_reason = body.reason
    agent.banned_until = body.banned_until
    agent.banned_at = _datetime.datetime.utcnow()
    db.commit()
    return {
        "ok": True,
        "agent_id": agent_id,
        "banned_until": body.banned_until,
        "reason": body.reason,
    }


@router.post("/admin/{agent_id}/unban",
    summary="Unban an agent",
    description="Admin only. Clears all ban fields.")
def unban_agent(
    agent_id: int,
    x_admin_key: str = Header(..., alias="X-Admin-Key"),
    db: Session = Depends(get_db),
):
    if not _settings.ADMIN_KEY or x_admin_key != _settings.ADMIN_KEY:
        raise HTTPException(status_code=403, detail="Forbidden")
    agent = db.query(Agent).get(agent_id)
    if not agent:
        raise HTTPException(status_code=404, detail="Agent not found")
    agent.ban_reason = None
    agent.banned_until = None
    agent.banned_at = None
    db.commit()
    return {"ok": True, "agent_id": agent_id}
