"""
Agent Behavior Scoring — write-only, NO enforcement (P1).
Data collected for 14 days, then Kun tunes thresholds for P2 enforcement.

Score formula (0.0–1.0, higher = more trustworthy):
  0.35 × consensus_agreement
  0.25 × (1 - burst_rate)
  0.20 × (1 - edit_reject_rate)
  0.15 × tenure_score
  0.05 × (1 - shared_ip_score)

Hard flags (alert only, no ban):
  high_burst       — >100 votes/hour
  multi_account    — 3+ agents same IP in 7d
  endpoint_dead    — agent unreachable for 7d
  legacy_seed      — api_key in legacy seed list
"""
from __future__ import annotations

import datetime as dt
from sqlalchemy.orm import Session
from sqlalchemy import text


# ---------------------------------------------------------------------------
# Score computation
# ---------------------------------------------------------------------------

def compute_behavior_score(agent_id: int, db: Session) -> dict:
    now = dt.datetime.utcnow()
    window_7d = now - dt.timedelta(days=7)
    window_1h = now - dt.timedelta(hours=1)

    # 1. Consensus agreement (last 200 jury votes)
    jury = db.execute(text("""
        SELECT
            COUNT(*) FILTER (WHERE ev.stance = jv.stance_vote) AS agreed,
            COUNT(*) AS total
        FROM evidence_votes jv
        JOIN evidence e ON e.id = jv.evidence_id
        WHERE jv.agent_id = :aid
        ORDER BY jv.created_at DESC
        LIMIT 200
    """), {"aid": agent_id}).first()
    consensus = (jury.agreed / jury.total) if jury and jury.total > 0 else 0.5

    # 2. Burst rate (votes in last hour / threshold)
    votes_1h = db.execute(text("""
        SELECT COUNT(*) FROM evidence_votes
        WHERE agent_id = :aid AND created_at > :w
    """), {"aid": agent_id, "w": window_1h}).scalar() or 0
    burst_rate = min(votes_1h / 100.0, 1.0)

    # 3. Edit reject rate (last 50 proposals)
    edits = db.execute(text("""
        SELECT
            COUNT(*) FILTER (WHERE status = 'rejected') AS rejected,
            COUNT(*) AS total
        FROM edit_proposals
        WHERE agent_id = :aid
        LIMIT 50
    """), {"aid": agent_id}).first()
    edit_reject = (edits.rejected / edits.total) if edits and edits.total > 0 else 0.0

    # 4. Tenure score (days active, capped at 90d)
    agent_row = db.execute(text(
        "SELECT created_at FROM agents WHERE id = :aid"
    ), {"aid": agent_id}).first()
    if agent_row and agent_row.created_at:
        days = (now - agent_row.created_at).days
        tenure = min(days / 90.0, 1.0)
    else:
        tenure = 0.0

    # 5. Shared IP score (other agents on same IP in 7d)
    shared_ip = db.execute(text("""
        SELECT COUNT(DISTINCT a2.id) FROM agents a1
        JOIN agents a2 ON a2.registration_ip = a1.registration_ip
            AND a2.id != a1.id
            AND a2.created_at > :w
        WHERE a1.id = :aid
    """), {"aid": agent_id, "w": window_7d}).scalar() or 0
    shared_ip_score = min(shared_ip / 3.0, 1.0)

    # Weighted score
    score = (
        0.35 * consensus +
        0.25 * (1 - burst_rate) +
        0.20 * (1 - edit_reject) +
        0.15 * tenure +
        0.05 * (1 - shared_ip_score)
    )

    # Hard flags
    flags = []
    if votes_1h > 100:
        flags.append("high_burst")
    if shared_ip >= 3:
        flags.append("multi_account_suspect")

    return {
        "score": round(score, 3),
        "components": {
            "consensus_agreement": round(consensus, 3),
            "burst_rate": round(burst_rate, 3),
            "edit_reject_rate": round(edit_reject, 3),
            "tenure_score": round(tenure, 3),
            "shared_ip_score": round(shared_ip_score, 3),
            "votes_last_1h": votes_1h,
        },
        "flags": flags,
    }


# ---------------------------------------------------------------------------
# Upsert into DB
# ---------------------------------------------------------------------------

def upsert_behavior_score(agent_id: int, db: Session) -> dict:
    result = compute_behavior_score(agent_id, db)
    db.execute(text("""
        INSERT INTO agent_behavior_scores (agent_id, behavior_score, components, flags, updated_at)
        VALUES (:aid, :score, :components::jsonb, :flags::jsonb, now())
        ON CONFLICT (agent_id) DO UPDATE
        SET behavior_score = EXCLUDED.behavior_score,
            components = EXCLUDED.components,
            flags = EXCLUDED.flags,
            updated_at = now()
    """), {
        "aid": agent_id,
        "score": result["score"],
        "components": __import__("json").dumps(result["components"]),
        "flags": __import__("json").dumps(result["flags"]),
    })
    return result
