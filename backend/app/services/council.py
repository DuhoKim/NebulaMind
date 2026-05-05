"""Tiered Council — eligibility functions and escalation helpers."""
from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from app.models.agent import Agent


def is_stage1_eligible(agent) -> bool:
    return (
        getattr(agent, "status", "active") == "active"
        and getattr(agent, "reputation", 0.5) >= 0.05
    )


def is_stage2_eligible(agent, bootstrap: bool = True) -> bool:
    from app.config import settings

    min_rep = settings.COUNCIL_STAGE2_MIN_REPUTATION_BOOTSTRAP if bootstrap else 1.0
    min_votes = settings.COUNCIL_STAGE2_MIN_VOTES_BOOTSTRAP if bootstrap else 30
    rep = getattr(agent, "reputation", 0)
    total_votes = getattr(agent, "total_jury_votes", 0)
    agreed_votes = getattr(agent, "agreed_jury_votes", 0)
    accuracy = agreed_votes / max(1, total_votes)
    return (
        getattr(agent, "status", "active") == "active"
        and rep >= min_rep
        and total_votes >= min_votes
        and accuracy >= 0.55
    )


def is_stage3_eligible(agent, db) -> bool:
    if not is_stage2_eligible(agent, bootstrap=False):
        return False
    if getattr(agent, "reputation", 0) < 1.5:
        return False
    if getattr(agent, "total_jury_votes", 0) < 100:
        return False
    from app.models.council import Stage3Roll

    return (
        db.query(Stage3Roll)
        .filter(
            Stage3Roll.agent_id == agent.id,
            Stage3Roll.removed_at.is_(None),
        )
        .first()
        is not None
    )


def is_verified_human(agent) -> bool:
    return (
        getattr(agent, "contributor_type", "agent") == "human"
        and getattr(agent, "is_verified", False)
        and getattr(agent, "status", "active") == "active"
    )


def check_institutional_email(email: str) -> bool:
    """Auto-verify if institutional domain."""
    from app.config import settings

    domains = [d.strip() for d in settings.COUNCIL_INSTITUTIONAL_EMAIL_DOMAINS.split(",")]
    return any(email.lower().endswith(d) for d in domains if d)


def open_escalation(
    db,
    source_kind: str,
    source_id: int,
    trigger_code: str,
    trigger_detail: str | None = None,
    opened_by: int | None = None,
    stage: int = 2,
):
    """Create an escalation record. Returns the new Escalation."""
    import datetime as _dt
    from app.models.council import Escalation
    from app.config import settings

    days = settings.COUNCIL_ESCALATION_STAGE2_DAYS if stage == 2 else settings.COUNCIL_ESCALATION_STAGE3_DAYS
    quorum = settings.COUNCIL_STAGE2_QUORUM if stage == 2 else settings.COUNCIL_STAGE3_QUORUM
    esc = Escalation(
        source_kind=source_kind,
        source_id=source_id,
        current_stage=stage,
        trigger_code=trigger_code,
        trigger_detail=trigger_detail,
        votes_target=quorum,
        expires_at=_dt.datetime.utcnow() + _dt.timedelta(days=days),
        opened_by_agent_id=opened_by,
    )
    db.add(esc)
    db.flush()
    try:
        from app.agent_loop.tasks import _notify as _n
        _n(f"🔵 New escalation #{esc.id} opened: {source_kind} #{source_id} (trigger: {trigger_code}, Stage {stage})")
    except Exception:
        pass
    return esc


def evaluate_escalation_triggers(db, evidence_id: int, votes: list) -> str | None:
    """After Stage 1 settles, check if escalation is warranted. Returns trigger code or None."""
    from app.config import settings

    if len(votes) < 4:
        return None  # Not settled yet

    n_pos = sum(v.weight for v in votes if v.value > 0)
    n_neg = sum(v.weight for v in votes if v.value < 0)
    n_total = n_pos + n_neg
    if n_total == 0:
        return None

    agreement = n_pos / n_total
    margin = abs(agreement - 0.5) * 2  # 0=tie, 1=unanimous
    if margin < settings.COUNCIL_STAGE1_ESCALATION_MARGIN:
        return "E1"  # Contested jury

    # E2: check if any voter is now muted/banned
    from app.models.agent import Agent

    for v in votes:
        if v.agent_id:
            a = db.query(Agent).filter(Agent.id == v.agent_id).first()
            if a and getattr(a, "status", "active") in ("muted", "banned"):
                return "E2"

    return None
