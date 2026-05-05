"""Trust Mechanics Phase 1 — recalculator.

Distinct from the v2 calculator in `app.routers.claims`. This one applies the
Phase 1 *evidence quality gate*: only evidence with `arxiv_verified=True` counts
toward the E component. Unverified evidence is treated as if it doesn't exist
(it stays in the DB for audit, but doesn't move trust).
"""
from __future__ import annotations

import datetime as _dt

from sqlalchemy.orm import Session

from app.models.claim import Claim, Evidence, TrustAuditLog


def recalculate_trust(claim_id: int, db: Session) -> str:
    """Recalculate trust for a claim under the Phase 1 evidence-quality-gate model.

    Returns the new trust level (string). Persists `trust_score`, `trust_level`,
    and a `TrustAuditLog` row when the level changes.
    """
    claim = db.query(Claim).get(claim_id)
    if not claim:
        return "unverified"

    evidence_list = db.query(Evidence).filter(Evidence.claim_id == claim_id).all()

    # ---- E component (arxiv-verified evidence only) ----
    if not evidence_list:
        E = -0.2  # slight penalty for no evidence
    else:
        verified = [e for e in evidence_list if e.arxiv_verified]
        supports = [e for e in verified if e.stance == "supports"]
        challenges = [e for e in verified if e.stance == "challenges"]
        pos_score = sum(e.quality for e in supports)
        neg_score = sum(e.quality for e in challenges)
        total = pos_score + neg_score + 0.001
        E = (pos_score - neg_score) / total

    # ---- V (Phase 1: vote-weighted signal not yet wired in) ----
    V = 0.0
    # ---- T (Phase 1: temporal modifier reserved) ----
    T = 0.0

    TS = 0.45 * E + 0.35 * V + 0.10 * T

    n_supports = sum(
        1 for e in evidence_list if e.stance == "supports" and e.arxiv_verified
    )
    n_challenges = sum(
        1 for e in evidence_list if e.stance == "challenges" and e.arxiv_verified
    )

    if TS >= 0.75 and n_supports >= 3 and n_challenges == 0:
        new_trust = "consensus"
    elif TS >= 0.30:
        new_trust = "accepted"
    elif abs(TS) < 0.30 and n_supports >= 1 and n_challenges >= 1:
        new_trust = "debated"
    elif TS <= -0.30:
        new_trust = "challenged"
    else:
        new_trust = "unverified"

    old_trust = claim.trust_level
    old_score = getattr(claim, "trust_score", 0.0) or 0.0

    claim.trust_score = TS
    claim.trust_level = new_trust
    claim.trust_score_updated_at = _dt.datetime.utcnow()

    if old_trust != new_trust:
        db.add(TrustAuditLog(
            claim_id=claim_id,
            old_level=old_trust,
            new_level=new_trust,
            old_score=old_score,
            new_score=TS,
            e_component=E,
            v_component=V,
            t_component=T,
            h_component=0.0,
            trigger="phase1_recalculation",
            notes="evidence-quality-gate recalc",
        ))

    db.commit()
    return new_trust
