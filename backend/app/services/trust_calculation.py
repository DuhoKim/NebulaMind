import math
import os
from datetime import datetime, timedelta

from sqlalchemy.orm import Session

from app.config import settings
from app.models.claim import Claim, Evidence, EvidenceVote, TrustAuditLog


def _human_override_score(claim) -> float:
    """Map human_trust_override to a float contribution H."""
    mapping = {
        "consensus": 1.0,
        "accepted": 0.5,
        "debated": 0.0,
        "challenged": -0.5,
    }
    if not claim.human_trust_override:
        return 0.0
    return mapping.get(claim.human_trust_override, 0.0)


def _bucket_debate(claim, evidence: list) -> str:
    """Determine trust level for claim_type='debate' claims."""
    has_supports = any(e.stance == "supports" for e in evidence)
    has_challenges = any(e.stance == "challenges" for e in evidence)
    if has_supports and has_challenges:
        return "debated"
    elif has_supports:
        return "accepted"
    elif has_challenges:
        return "challenged"
    else:
        return "unverified"


def _emit_event(event_name: str, **kwargs) -> None:
    """Emit a trust event. Phase 1: just print. Phase 4 will hook to Discord/Celery."""
    print(f"[trust_event] {event_name}: {kwargs}")


def _notify_trust_demotion(claim_id: int, old_level: str, new_level: str, claim_text: str) -> None:
    """Post hard demotion to #nebulamind-recruitment Discord channel."""
    try:
        import httpx
        msg = (
            f"🔴 **Hard demotion** — Claim #{claim_id} demoted: "
            f"{old_level} → **{new_level}**\n"
            f"*{claim_text}...*\n"
            f"View: https://nebulamind.net"
        )
        recruitment_webhook = os.getenv("DISCORD_NEBULAMIND_RECRUITMENT_WEBHOOK", "")
        if not recruitment_webhook:
            return
        httpx.post(recruitment_webhook, json={"content": msg}, timeout=5)
    except Exception:
        pass  # best-effort


def recalculate_trust_v2(
    claim_id: int,
    db: Session,
    *,
    trigger: str = "manual",
    actor_agent_id: int | None = None,
    actor_human_id: int | None = None,
) -> tuple[str, float]:
    """Compute and persist the v2 trust score for a claim.

    Returns (new_level, trust_score).
    """
    claim = db.query(Claim).filter(Claim.id == claim_id).first()
    if not claim:
        return "unverified", 0.0

    evidence = (
        db.query(Evidence)
        .filter(Evidence.claim_id == claim_id, Evidence.status == "active")
        .all()
    )

    # ---- E component ----
    if not evidence:
        E = 0.0
        n_supports = n_challenges = 0
    else:
        E_sup  = sum(e.quality for e in evidence if e.stance == "supports")
        E_chal = sum(e.quality for e in evidence if e.stance == "challenges")
        # neutral counts as 0 in the numerator (context only)
        E = math.tanh((E_sup - E_chal) / 1.5)
        n_supports   = sum(1 for e in evidence if e.stance == "supports")
        n_challenges = sum(1 for e in evidence if e.stance == "challenges")

    # ---- V component ----
    if evidence:
        ev_ids = [e.id for e in evidence]
        votes = db.query(EvidenceVote).filter(EvidenceVote.evidence_id.in_(ev_ids)).all()
        n_pos = sum(v.weight for v in votes if v.value > 0)
        n_neg = sum(v.weight for v in votes if v.value < 0)
        n_total = n_pos + n_neg
        if n_total > 0:
            raw = (n_pos - n_neg) / n_total
            confidence = 1.0 - math.exp(-n_total / settings.VOTE_CONFIDENCE_HALF_LIFE)
            V = raw * confidence
        else:
            V = 0.0
    else:
        V = 0.0

    # ---- T component ----
    sup_years = [e.year for e in evidence if e.stance == "supports" and e.year]
    if sup_years:
        years_since = datetime.utcnow().year - max(sup_years)
        T = -0.05 * max(0, years_since - settings.DECAY_FREE_YEARS) / 5.0
        T = max(T, -settings.DECAY_MAX_PENALTY)
    else:
        T = 0.0

    # ---- H component ----
    H = _human_override_score(claim)

    # === Phase F: Wikipedia cross-check signal ===
    if settings.WIKIPEDIA_CROSSCHECK_ENABLED:
        from app.models.page import WikiPage
        from app.services.wikipedia_ingest import wikipedia_cross_check_score
        try:
            page = db.get(WikiPage, claim.page_id)
            if page and page.wikipedia_title and page.wiki_summary:
                bonus = wikipedia_cross_check_score(claim, page)
                bonus = min(bonus, settings.WIKIPEDIA_CROSSCHECK_MAX_BONUS)
                if bonus > 0:
                    V = min(1.0, V + bonus)
        except Exception:
            pass  # cross-check is advisory; never fail trust computation

    # ---- Combine ----
    TS = (
        settings.TRUST_W_EVIDENCE * E
        + settings.TRUST_W_VOTES * V
        + settings.TRUST_W_TEMPORAL * T
        + settings.TRUST_W_HUMAN * H
    )

    # ---- Bucket ----
    if claim.human_trust_override and claim.human_override_locked:
        new_level = claim.human_trust_override
    elif claim.claim_type == "debate":
        new_level = _bucket_debate(claim, evidence)
    elif not evidence and TS == 0:
        new_level = "unverified"
    elif (TS >= settings.TRUST_CONSENSUS_MIN
          and n_supports >= settings.TRUST_CONSENSUS_MIN_SUPPORTS
          and n_challenges == 0):
        new_level = "consensus"
    elif TS >= settings.TRUST_ACCEPTED_MIN:
        new_level = "accepted"
    elif TS <= settings.TRUST_CHALLENGED_MAX:
        new_level = "challenged"
    elif n_supports >= 1 and n_challenges >= 1:
        new_level = "debated"
    else:
        new_level = "unverified"

    # ---- Freshness floor ----
    if (new_level == "consensus" and sup_years
            and (datetime.utcnow().year - max(sup_years)) > settings.FRESHNESS_FLOOR_YEARS):
        # Check if any evidence was added recently
        cutoff = datetime.utcnow() - timedelta(days=settings.FRESHNESS_FLOOR_NEW_EVIDENCE_DAYS)
        recent = any(e.created_at >= cutoff for e in evidence)
        if not recent:
            new_level = "accepted"
            _emit_event("claim.stale", claim_id=claim_id)

    # ---- Persist + audit ----
    old_level = claim.trust_level
    old_score = getattr(claim, "trust_score", None)
    claim.trust_level = new_level
    claim.trust_score = TS
    claim.trust_score_updated_at = datetime.utcnow()

    # Hard demotion notification
    if new_level == "challenged" and old_level != "challenged":
        _notify_trust_demotion(claim_id, old_level, new_level, claim.text[:120] if claim.text else "")

    db.add(TrustAuditLog(
        claim_id=claim_id,
        old_level=old_level,
        new_level=new_level,
        old_score=old_score,
        new_score=TS,
        e_component=E,
        v_component=V,
        t_component=T,
        h_component=H,
        trigger=trigger,
        triggered_by_agent_id=actor_agent_id,
        triggered_by_human_id=actor_human_id,
    ))
    return new_level, TS
