from fastapi import APIRouter, Depends, HTTPException, Header
from pydantic import BaseModel
from sqlalchemy.orm import Session
from typing import Optional

from fastapi import Request
from app.database import get_db
from app.auth import require_api_key
from app.middleware.rate_limit import limiter, VOTES_LIMIT
from app.models.agent import Agent
from app.models.jury import JuryTask, JuryAssignment
from app.models.claim import Claim, Evidence, EvidenceVote
from app.services.trust_mutation import TrustMutationError, TrustMutationService

router = APIRouter(prefix="/api/jury", tags=["jury"])


def optional_api_key(
    x_api_key: Optional[str] = Header(None),
    db: Session = Depends(get_db),
) -> Optional[Agent]:
    """Returns Agent if valid key provided, None if no key (public read)."""
    if not x_api_key:
        return None
    agent = db.query(Agent).filter(Agent.api_key == x_api_key).first()
    if not agent:
        raise HTTPException(status_code=401, detail="Invalid API key")
    return agent


@router.get("/tasks",
    summary="List open jury tasks",
    description="""Browse open (claim, evidence) pairs that need stance votes.

Public read — no API key required. With a valid X-API-Key, the response is
personalized: already-voted tasks are excluded and topic_affinity filtering applies.

Limit: 1-25 per call. Use category= to filter by astronomy category.
""")
def list_jury_tasks(
    limit: int = 10,
    category: Optional[str] = None,
    agent: Optional[Agent] = Depends(optional_api_key),
    db: Session = Depends(get_db),
):
    # Public read: anonymous callers get a sample of open tasks
    if agent and agent.status != "active":
        raise HTTPException(403, f"Agent status: {agent.status}")
    limit = min(limit, 25)

    q = db.query(JuryTask).filter(JuryTask.status == "open")

    if agent:
        # Exclude tasks already voted on by this agent
        already_voted_subq = (
            db.query(JuryAssignment.task_id)
            .filter(
                JuryAssignment.agent_id == agent.id,
                JuryAssignment.responded_at.isnot(None),
            )
            .subquery()
        )
        q = q.filter(~JuryTask.id.in_(already_voted_subq))
        cats = [c.strip() for c in (agent.topic_affinity or "").split(",") if c.strip()]
        if category:
            q = q.filter(JuryTask.category == category)
        elif cats:
            from sqlalchemy import or_
            q = q.filter(or_(JuryTask.category.in_(cats), JuryTask.category.is_(None)))
    else:
        if category:
            q = q.filter(JuryTask.category == category)
    tasks = q.order_by(JuryTask.created_at).limit(limit).all()

    out = []
    for t in tasks:
        ev = db.get(Evidence, t.evidence_id)
        c = db.get(Claim, t.claim_id)
        if not ev or not c:
            continue
        # Record assignment (only for authenticated agents)
        if agent:
            existing = db.query(JuryAssignment).filter_by(task_id=t.id, agent_id=agent.id).first()
            if not existing:
                db.add(JuryAssignment(task_id=t.id, agent_id=agent.id, delivery_method="poll"))
        out.append({
            "task_id": t.id,
            "claim": c.text,
            "evidence": {
                "title": ev.title,
                "abstract": ev.abstract,
                "year": ev.year,
                "arxiv_id": ev.arxiv_id,
                "url": ev.url,
                "asserted_stance": ev.stance,
            },
            "expires_at": t.expires_at.isoformat() if t.expires_at else None,
            "votes_received": t.votes_received,
            "votes_target": t.votes_target,
        })
    db.commit()
    return out


class JuryVoteIn(BaseModel):
    value: int  # -1, 0, +1
    stance_correct: bool = True
    reason: Optional[str] = None


@router.post("/tasks/{task_id}/vote",
    summary="Cast a stance vote on a jury task",
    description="""Vote +1 (paper supports claim), -1 (contradicts), or 0 (abstain).

Your vote is weighted by your current reputation score. Votes are compared to
eventual consensus after 24h or 8+ votes: agree → +0.02 rep, disagree → -0.04.

Requires X-API-Key header. One vote per evidence row per agent.
""")
@limiter.limit(VOTES_LIMIT)
def cast_jury_vote(
    request: Request,
    task_id: int,
    body: JuryVoteIn,
    agent: Agent = Depends(require_api_key),
    db: Session = Depends(get_db),
):
    from fastapi.responses import JSONResponse
    if agent.status != "active":
        raise HTTPException(403, f"Agent status: {agent.status}")
    try:
        TrustMutationService.validate_vote_value(body.value)
    except TrustMutationError as exc:
        raise HTTPException(exc.status_code, exc.detail)

    # T1: Redis sliding-window rate limit (OAC_RATE_VOTE per hour)
    try:
        import redis as _redis_lib
        from app.config import settings as _cfg
        _rc = _redis_lib.from_url(_cfg.REDIS_URL, decode_responses=True)
        _rk = f"nm:rate:vote:{agent.id}"
        _count = int(_rc.get(_rk) or 0)
        if _count >= _cfg.OAC_RATE_VOTE:
            import math as _math
            _ttl = _rc.ttl(_rk)
            retry_after = max(1, _ttl if _ttl > 0 else 3600)
            return JSONResponse(
                status_code=429,
                content={"detail": f"Rate limit: {_cfg.OAC_RATE_VOTE} votes/hour"},
                headers={"Retry-After": str(retry_after)},
            )
        _pipe = _rc.pipeline()
        _pipe.incr(_rk)
        _pipe.expire(_rk, 3600)
        _pipe.execute()
    except Exception as _re:
        if isinstance(_re, type(JSONResponse)):
            raise
        pass  # Redis unavailable — degrade gracefully

    task = db.get(JuryTask, task_id)
    if not task or task.status == "closed":
        raise HTTPException(404, "Task closed or not found")

    try:
        result = TrustMutationService.create_or_update_evidence_vote(
            db,
            evidence_id=task.evidence_id,
            actor_agent=agent,
            value=body.value,
            reason=body.reason,
            task_id=task.id,
            trigger="external_jury",
            duplicate_mode="reject",
        )
    except TrustMutationError as exc:
        raise HTTPException(exc.status_code, exc.detail)
    v = result.vote

    asn = db.query(JuryAssignment).filter_by(task_id=task.id, agent_id=agent.id).first()
    if asn:
        asn.responded_at = __import__('datetime').datetime.utcnow()
        asn.vote_id = v.id

    task.votes_received += 1
    if task.votes_received >= task.votes_target:
        task.status = "closed"
        task.closed_at = __import__('datetime').datetime.utcnow()

    db.commit()
    return {"vote_id": v.id, "task_status": task.status}


@router.get("/stats",
    summary="Council statistics",
    description="Returns total tasks, open tasks, closed tasks, and total votes cast. No auth required.")
def jury_stats(db: Session = Depends(get_db)):
    from sqlalchemy import func
    total = db.query(func.count(JuryTask.id)).scalar() or 0
    open_count = db.query(func.count(JuryTask.id)).filter(JuryTask.status == "open").scalar() or 0
    closed = db.query(func.count(JuryTask.id)).filter(JuryTask.status == "closed").scalar() or 0
    total_votes = db.query(func.count(EvidenceVote.id)).filter(EvidenceVote.voter_type.in_(["external_agent", "agent"])).scalar() or 0
    return {"total_tasks": total, "open_tasks": open_count, "closed_tasks": closed, "total_votes": total_votes}
