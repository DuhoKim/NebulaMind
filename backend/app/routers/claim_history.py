"""
GET /api/claims/{claim_id}/history

Returns condensed trust history for a claim.
Filters noise (noop recomputes), groups burst events, humanizes triggers.
"""

from fastapi import APIRouter, Depends, Query
from sqlalchemy.orm import Session
from app.database import get_db
from app.models.claim import TrustAuditLog

router = APIRouter(prefix="/api/claims", tags=["claims"])

TRIGGER_MAP = {
    "evidence_inserted":        ("📄", "evidence_added",    "blue"),
    "arxiv_ingest":             ("📄", "evidence_added",    "blue"),
    "wikipedia_biblio_mine":    ("📄", "evidence_added",    "blue"),
    "stance_jury":              ("⚖️", "jury_voted",        "purple"),
    "settle_evidence":          ("⚖️", "jury_voted",        "purple"),
    "manual":                   ("⭐", "promoted_manually", "gold"),
    "evidence_promoted":        ("⭐", "evidence_promoted", "gold"),
    "human_override":           ("👤", "human_corrected",   "gold"),
    "temporal_decay":           ("⏳", "decayed",           "gray"),
    "initialized":              ("🌱", "initialized",       "green"),
    "recompute":                ("🔄", "recomputed",        "gray"),
    "recalculate":              ("🔄", "recomputed",        "gray"),
}

LEVEL_EMOJI = {
    "consensus":   "🟢",
    "accepted":    "⚪",
    "debated":     "🟠",
    "challenged":  "🔴",
    "unverified":  "❓",
}

def humanize_trigger(trigger: str, old_level: str, new_level: str, detail: dict) -> tuple[str, str, str, str]:
    """Returns (icon, kind, color, summary)"""
    icon, kind, color = TRIGGER_MAP.get(trigger, ("🔄", "recomputed", "gray"))

    if kind == "initialized":
        summary = "Claim added to the wiki"
    elif kind == "evidence_added":
        n = detail.get("n_events", 1)
        summary = f"{n} cited paper{'s' if n != 1 else ''} added"
    elif kind == "jury_voted":
        n = detail.get("n_events", 1)
        summary = f"Jury voted ({n} vote{'s' if n != 1 else ''})"
    elif kind == "human_corrected":
        summary = "Human researcher override"
    elif kind == "decayed":
        summary = "Trust decayed (old citations)"
    elif kind == "promoted_manually":
        summary = "Manually promoted"
    elif kind == "evidence_promoted":
        summary = "Evidence promoted into trust"
    else:
        summary = f"Recomputed (score updated)"

    if old_level != new_level:
        old_e = LEVEL_EMOJI.get(old_level, "❓")
        new_e = LEVEL_EMOJI.get(new_level, "❓")
        summary += f"  {old_e}→{new_e}"

    return icon, kind, color, summary


@router.get("/{claim_id}/history")
def get_claim_history(
    claim_id: int,
    include_noop: bool = Query(False, description="Include recompute events with no level change"),
    limit: int = Query(25, le=100),
    db: Session = Depends(get_db),
):
    """Get condensed trust history for a claim."""

    # Fetch all audit rows for this claim
    rows = db.query(TrustAuditLog).filter(
        TrustAuditLog.claim_id == claim_id
    ).order_by(TrustAuditLog.created_at.asc(), TrustAuditLog.id.asc()).all()

    if not rows:
        return {"claim_id": claim_id, "events": [], "current": None}

    # Filter noops unless requested
    filtered = rows if include_noop else [
        r for r in rows if r.old_level != r.new_level or r.trigger in ("initialized", "manual", "evidence_promoted", "human_override")
    ]

    # Group nearby same-trigger events into bursts (within 1 hour)
    from datetime import timedelta
    bursts = []
    i = 0
    while i < len(filtered):
        row = filtered[i]
        burst = [row]
        j = i + 1
        while j < len(filtered):
            next_row = filtered[j]
            # Same trigger category + within 1 hour of first in burst
            same_cat = TRIGGER_MAP.get(row.trigger, ("","",""))[1] == TRIGGER_MAP.get(next_row.trigger, ("","",""))[1]
            within_hour = (next_row.created_at - burst[0].created_at) <= timedelta(hours=1)
            if same_cat and within_hour:
                burst.append(next_row)
                j += 1
            else:
                break
        bursts.append(burst)
        i = j if j > i + 1 else i + 1

    # Limit
    bursts = bursts[-limit:]

    events = []
    for burst in bursts:
        first = burst[0]
        last = burst[-1]
        icon, kind, color, summary = humanize_trigger(
            first.trigger,
            first.old_level,
            last.new_level,
            {"n_events": len(burst)}
        )
        score_before = float(first.old_score or 0)
        score_after = float(last.new_score or 0)
        score_delta = score_after - score_before
        detail = None
        if abs(score_delta) > 0.001:
            detail = f"Score {score_before:.3f} → {score_after:.3f} ({score_delta:+.3f})"

        events.append({
            "timestamp": first.created_at.isoformat(),
            "icon": icon,
            "kind": kind,
            "color": color,
            "summary": summary,
            "old_level": first.old_level,
            "new_level": last.new_level,
            "old_score": round(score_before, 3),
            "new_score": round(score_after, 3),
            "score_delta": score_delta,
            "detail": detail,
            "event_count": len(burst),
            "trigger": first.trigger,
        })

    # Current state
    last_row = rows[-1]
    current = {
        "level": last_row.new_level,
        "score": round(float(last_row.new_score or 0), 3),
        "emoji": LEVEL_EMOJI.get(last_row.new_level, "❓"),
    }

    return {
        "claim_id": claim_id,
        "events": events,
        "current": current,
        "total_raw_rows": len(rows),
        "total_condensed": len(events),
    }
