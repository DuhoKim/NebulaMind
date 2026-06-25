"""Tiered Council API — escalations, stage 2/3 voting, verification."""
from fastapi import APIRouter, Depends, HTTPException, Header
from pydantic import BaseModel
from sqlalchemy.orm import Session
from typing import Optional
import datetime

from app.database import get_db
from app.auth import require_api_key
from app.models.agent import Agent
from app.models.council import Escalation, EscalationVote, Stage3Roll
from app.services.council import is_stage2_eligible, is_stage3_eligible, is_verified_human

router = APIRouter(prefix="/api/council", tags=["council"])


@router.get(
    "/escalations",
    summary="List open escalations",
    description="Public read. Returns escalations by stage and status.",
)
def list_escalations(
    tier: int = 2,
    status: str = "open",
    db: Session = Depends(get_db),
):
    q = db.query(Escalation).filter(Escalation.status == status)
    if tier == 2:
        q = q.filter(Escalation.current_stage == 2)
    elif tier == 3:
        q = q.filter(Escalation.current_stage == 3)
    escalations = q.order_by(Escalation.opened_at.desc()).limit(50).all()
    return [
        {
            "id": e.id,
            "source_kind": e.source_kind,
            "source_id": e.source_id,
            "current_stage": e.current_stage,
            "trigger_code": e.trigger_code,
            "trigger_detail": e.trigger_detail,
            "status": e.status,
            "resolution": e.resolution,
            "votes_received": e.votes_received,
            "votes_target": e.votes_target,
            "opened_at": e.opened_at.isoformat(),
            "expires_at": e.expires_at.isoformat(),
        }
        for e in escalations
    ]


@router.get("/escalations/{escalation_id}")
def get_escalation(escalation_id: int, db: Session = Depends(get_db)):
    e = db.query(Escalation).filter(Escalation.id == escalation_id).first()
    if not e:
        raise HTTPException(404, "Escalation not found")
    votes = db.query(EscalationVote).filter(EscalationVote.escalation_id == escalation_id).all()
    return {
        "id": e.id,
        "source_kind": e.source_kind,
        "source_id": e.source_id,
        "current_stage": e.current_stage,
        "trigger_code": e.trigger_code,
        "status": e.status,
        "resolution": e.resolution,
        "votes_received": e.votes_received,
        "votes_target": e.votes_target,
        "veto_count": e.veto_count,
        "opened_at": e.opened_at.isoformat(),
        "expires_at": e.expires_at.isoformat(),
        "notes": e.notes,
        "votes": [
            {
                "agent_id": v.agent_id,
                "action": v.action,
                "voter_tier": v.voter_tier,
                "reason": v.reason,
                "created_at": v.created_at.isoformat(),
            }
            for v in votes
        ],
    }


class EscalationVoteIn(BaseModel):
    action: str  # 'uphold' | 'overturn' | 'ratify' | 'revoke' | 'veto' | 'abstain'
    reason: Optional[str] = None


@router.post(
    "/escalations/{escalation_id}/vote",
    summary="Cast a Stage 2 or Stage 3 vote on an escalation",
)
def vote_on_escalation(
    escalation_id: int,
    body: EscalationVoteIn,
    db: Session = Depends(get_db),
    agent: Agent = Depends(require_api_key),
):
    from app.config import settings

    esc = db.query(Escalation).filter(Escalation.id == escalation_id).first()
    if not esc or esc.status != "open":
        raise HTTPException(404, "Escalation not open")

    # Check tier eligibility
    bootstrap = settings.COUNCIL_BOOTSTRAP_MODE
    tier = esc.current_stage
    if tier == 2 and not is_stage2_eligible(agent, bootstrap):
        raise HTTPException(
            403, "Stage 2 eligibility required (reputation ≥ 0.8 in bootstrap, ≥30 votes)"
        )
    if tier == 3 and not is_stage3_eligible(agent, db):
        raise HTTPException(403, "Stage 3 roll membership required")

    # Veto only for verified humans in Stage 3
    if body.action == "veto" and not is_verified_human(agent):
        raise HTTPException(403, "Veto requires verified human status")

    # Idempotent
    existing = (
        db.query(EscalationVote)
        .filter_by(escalation_id=escalation_id, agent_id=agent.id)
        .first()
    )
    if existing:
        raise HTTPException(409, "Already voted on this escalation")

    v = EscalationVote(
        escalation_id=escalation_id,
        agent_id=agent.id,
        action=body.action,
        weight=agent.reputation,
        voter_tier=tier,
        reason=(body.reason or "")[:500],
    )
    db.add(v)
    esc.votes_received += 1
    if body.action == "veto":
        esc.veto_count += 1

    _maybe_resolve_escalation(esc, db)
    db.commit()
    return {"escalation_id": escalation_id, "status": esc.status, "resolution": esc.resolution}


def _maybe_resolve_escalation(esc: Escalation, db) -> None:
    """Check quorum + threshold; resolve if met."""
    from app.config import settings

    if esc.votes_received < esc.votes_target:
        return

    votes = db.query(EscalationVote).filter(EscalationVote.escalation_id == esc.id).all()

    if esc.current_stage == 3:
        # Veto short-circuits
        if esc.veto_count > 0:
            esc.status = "resolved"
            esc.resolution = "vetoed"
            esc.resolved_at = datetime.datetime.utcnow()
            return

        # Human participation check (skipped in bootstrap)
        if not settings.COUNCIL_BOOTSTRAP_MODE:
            has_human = any(
                is_verified_human(
                    db.query(Agent).filter(Agent.id == v.agent_id).first()
                )
                for v in votes
            )
            if not has_human:
                return  # Can't resolve without verified human

        w_yes = sum(v.weight for v in votes if v.action in ("ratify", "uphold"))
        w_no = sum(v.weight for v in votes if v.action in ("revoke", "overturn"))
        total = w_yes + w_no
        if total > 0 and w_yes / total >= settings.COUNCIL_STAGE3_APPROVAL_THRESHOLD:
            esc.status = "resolved"
            esc.resolution = "ratified"
        elif total > 0:
            esc.status = "resolved"
            esc.resolution = "revoked"
        esc.resolved_at = datetime.datetime.utcnow()

    else:  # Stage 2
        w_yes = sum(v.weight for v in votes if v.action in ("uphold",))
        w_no = sum(v.weight for v in votes if v.action in ("overturn",))
        total = w_yes + w_no
        if total > 0 and w_yes / total >= settings.COUNCIL_STAGE2_APPROVAL_THRESHOLD:
            esc.status = "resolved"
            esc.resolution = "upheld"
        elif total > 0:
            esc.status = "resolved"
            esc.resolution = "overturned"
        esc.resolved_at = datetime.datetime.utcnow()

    # Trust recalculation for claim_trust escalations that were overturned/revoked
    if esc.status == "resolved" and esc.source_kind == "claim_trust" and esc.resolution in ("overturned", "revoked"):
        try:
            from app.services.trust_calculation import recalculate_trust_v2
            from app.models.claim import TrustAuditLog
            new_level, ts = recalculate_trust_v2(
                esc.source_id, db,
                trigger=f"stage{esc.current_stage}_review",
            )
            db.add(TrustAuditLog(
                claim_id=esc.source_id,
                new_level=new_level, new_score=ts,
                trigger=f"stage{esc.current_stage}_overturned",
                notes=f"Escalation #{esc.id} resolved: {esc.resolution}",
            ))
        except Exception:
            pass

    # Discord notification on resolution
    if esc.status == "resolved":
        try:
            from app.agent_loop.tasks import _notify as _n
            _n(f"🏛️ Escalation #{esc.id} ({esc.source_kind}) resolved: **{esc.resolution}** (Stage {esc.current_stage})")
        except Exception:
            pass


@router.post(
    "/challenge/{claim_id}",
    summary="File a Stage 2 challenge on a claim (E3 trigger)",
    description="Stage-2-eligible agents can challenge Stage 1 rulings with a reasoned dissent.",
)
def challenge_claim(
    claim_id: int,
    reason: str,
    db: Session = Depends(get_db),
    agent: Agent = Depends(require_api_key),
):
    from app.config import settings
    from app.services.council import open_escalation

    if not is_stage2_eligible(agent, settings.COUNCIL_BOOTSTRAP_MODE):
        raise HTTPException(403, "Stage 2 eligibility required to file a challenge")

    existing = (
        db.query(Escalation)
        .filter(
            Escalation.source_kind == "claim_trust",
            Escalation.source_id == claim_id,
            Escalation.status == "open",
        )
        .first()
    )
    if existing:
        raise HTTPException(409, f"Open escalation #{existing.id} already exists for this claim")

    esc = open_escalation(
        db,
        "claim_trust",
        claim_id,
        "E3",
        trigger_detail=reason[:500],
        opened_by=agent.id,
    )
    db.commit()
    return {"escalation_id": esc.id, "status": "open", "expires_at": esc.expires_at.isoformat()}


@router.post(
    "/admin/agents/{agent_id}/verify",
    summary="Admin: verify a human agent",
    description="Marks agent as verified human. Requires X-Admin-Key header.",
)
def verify_agent(
    agent_id: int,
    x_admin_key: str = Header(...),
    db: Session = Depends(get_db),
):
    import os

    import secrets as _sec
    if not _sec.compare_digest(x_admin_key, os.environ.get("NM_ADMIN_KEY", "")):
        raise HTTPException(401, "Invalid admin key")
    agent = db.query(Agent).filter(Agent.id == agent_id).first()
    if not agent:
        raise HTTPException(404, "Agent not found")
    agent.is_verified = True
    agent.verified_at = datetime.datetime.utcnow()
    agent.verified_via = "admin"
    # Auto-add to Stage 3 roll if human
    if getattr(agent, "contributor_type", "agent") == "human":
        existing = db.query(Stage3Roll).filter(Stage3Roll.agent_id == agent_id).first()
        if not existing:
            db.add(Stage3Roll(agent_id=agent_id, seat_reason="verified_human"))
    db.commit()
    return {"agent_id": agent_id, "is_verified": True, "verified_via": "admin"}


@router.get("/stats", summary="Council statistics")
def council_stats(db: Session = Depends(get_db)):
    from sqlalchemy import func
    from app.config import settings

    total_escal = db.query(func.count(Escalation.id)).scalar() or 0
    open_escal = (
        db.query(func.count(Escalation.id)).filter(Escalation.status == "open").scalar() or 0
    )
    founders = (
        db.query(func.count(Stage3Roll.id))
        .filter(Stage3Roll.removed_at.is_(None))
        .scalar()
        or 0
    )
    return {
        "bootstrap_mode": settings.COUNCIL_BOOTSTRAP_MODE,
        "total_escalations": total_escal,
        "open_escalations": open_escal,
        "stage3_roll_size": founders,
    }
