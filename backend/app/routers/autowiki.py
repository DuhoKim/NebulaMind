"""Autowiki admin API — dashboard data + kill-switch."""
import datetime as dt

from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy import func, text
from sqlalchemy.orm import Session

from app.database import get_db
from app.models.autowiki import AutowikiRun, AutowikiTarget

router = APIRouter(prefix="/api/autowiki", tags=["autowiki"])


# ---------------------------------------------------------------------------
# Run history
# ---------------------------------------------------------------------------

@router.get("/runs")
def get_runs(
    page_id: int = Query(...),
    limit: int = Query(default=50, le=200),
    decision: str | None = Query(default=None),
    db: Session = Depends(get_db),
):
    q = db.query(AutowikiRun).filter(AutowikiRun.page_id == page_id)
    if decision:
        q = q.filter(AutowikiRun.decision == decision)
    runs = q.order_by(AutowikiRun.started_at.desc()).limit(limit).all()
    return [_run_dict(r) for r in runs]


def _run_dict(r: AutowikiRun) -> dict:
    return {
        "id": r.id,
        "page_id": r.page_id,
        "started_at": r.started_at.isoformat() if r.started_at else None,
        "finished_at": r.finished_at.isoformat() if r.finished_at else None,
        "proposal_type": r.proposal_type,
        "model_judge": r.model_judge,
        "h0_struct": r.h0_struct,
        "h1_struct": r.h1_struct,
        "components_before": r.components_before,
        "components_after": r.components_after,
        "u0_median": r.u0_median,
        "u1_median": r.u1_median,
        "u0_runs": r.u0_runs,
        "u1_runs": r.u1_runs,
        "q0": r.q0,
        "q1": r.q1,
        "delta_q": r.delta_q,
        "decision": r.decision,
        "reject_reason": r.reject_reason,
        "judge_rationale": r.judge_rationale,
        "judge_prompt_version": r.judge_prompt_version,
        "committed_version_id": r.committed_version_id,
        "latency_ms_breakdown": r.latency_ms_breakdown,
        "error_text": r.error_text,
    }


# ---------------------------------------------------------------------------
# Dashboard summary
# ---------------------------------------------------------------------------

@router.get("/summary")
def get_summary(
    page_id: int = Query(...),
    db: Session = Depends(get_db),
):
    target_row = db.query(AutowikiTarget).filter(
        AutowikiTarget.page_id == page_id
    ).first()
    target_q = target_row.target_q if target_row else 0.78
    last_raised_at = (
        target_row.last_raised_at.isoformat()
        if target_row and target_row.last_raised_at
        else None
    )

    # Most recent tick
    latest = (
        db.query(AutowikiRun)
        .filter(AutowikiRun.page_id == page_id, AutowikiRun.q1.isnot(None))
        .order_by(AutowikiRun.started_at.desc())
        .first()
    )

    # Last commit
    last_commit = (
        db.query(AutowikiRun)
        .filter(AutowikiRun.page_id == page_id, AutowikiRun.decision == "commit")
        .order_by(AutowikiRun.started_at.desc())
        .first()
    )

    # 24h Δq
    since_24h = dt.datetime.utcnow() - dt.timedelta(hours=24)
    oldest_24h = (
        db.query(AutowikiRun)
        .filter(
            AutowikiRun.page_id == page_id,
            AutowikiRun.q0.isnot(None),
            AutowikiRun.started_at >= since_24h,
        )
        .order_by(AutowikiRun.started_at.asc())
        .first()
    )
    delta_24h = None
    if latest and oldest_24h and latest.q1 is not None and oldest_24h.q0 is not None:
        delta_24h = round(latest.q1 - oldest_24h.q0, 4)

    # Buddle fallback rate (last 100)
    last_100 = (
        db.query(AutowikiRun)
        .filter(
            AutowikiRun.page_id == page_id,
            AutowikiRun.model_judge.isnot(None),
        )
        .order_by(AutowikiRun.started_at.desc())
        .limit(100)
        .all()
    )
    buddle_count = sum(1 for r in last_100 if r.model_judge == "buddle")
    buddle_rate = round(buddle_count / len(last_100), 3) if last_100 else 0.0

    return {
        "page_id": page_id,
        "current_q": latest.q1 if latest else None,
        "target_q": target_q,
        "last_raised_at": last_raised_at,
        "delta_24h": delta_24h,
        "last_commit_at": last_commit.started_at.isoformat() if last_commit else None,
        "buddle_fallback_rate": buddle_rate,
    }


# ---------------------------------------------------------------------------
# Q trajectory (for chart)
# ---------------------------------------------------------------------------

@router.get("/trajectory")
def get_trajectory(
    page_id: int = Query(...),
    limit: int = Query(default=200, le=500),
    db: Session = Depends(get_db),
):
    rows = (
        db.query(AutowikiRun)
        .filter(
            AutowikiRun.page_id == page_id,
            AutowikiRun.q1.isnot(None),
        )
        .order_by(AutowikiRun.started_at.asc())
        .limit(limit)
        .all()
    )

    # Also include auto-raise events
    target_events = db.execute(
        text(
            "SELECT last_raised_at, target_q FROM autowiki_targets "
            "WHERE page_id = :pid AND last_raised_at IS NOT NULL"
        ),
        {"pid": page_id},
    ).all()

    return {
        "ticks": [
            {
                "id": r.id,
                "t": r.started_at.isoformat() if r.started_at else None,
                "q0": r.q0,
                "q1": r.q1,
                "delta_q": r.delta_q,
                "decision": r.decision,
                "proposal_type": r.proposal_type,
                "rationale_snippet": (r.judge_rationale or "")[:120],
            }
            for r in rows
        ],
        "target_raises": [
            {
                "raised_at": e.last_raised_at.isoformat() if e.last_raised_at else None,
                "new_target": e.target_q,
            }
            for e in target_events
        ],
    }


# ---------------------------------------------------------------------------
# Judge panel — latest score from each of the 3 judges
# ---------------------------------------------------------------------------

@router.get("/judge-panel")
def get_judge_panel(
    page_id: int = Query(...),
    db: Session = Depends(get_db),
):
    def _latest_audit(proposal_type_filter) -> dict | None:
        row = (
            db.query(AutowikiRun)
            .filter(
                AutowikiRun.page_id == page_id,
                AutowikiRun.proposal_type == proposal_type_filter,
                AutowikiRun.u1_median.isnot(None),
            )
            .order_by(AutowikiRun.started_at.desc())
            .first()
        )
        if not row:
            return None
        return {
            "score": row.u1_median,
            "q1": row.q1,
            "rationale": row.judge_rationale,
            "model": row.judge_model or row.model_judge,
            "at": row.started_at.isoformat() if row.started_at else None,
        }

    def _latest_rakon() -> dict | None:
        row = (
            db.query(AutowikiRun)
            .filter(
                AutowikiRun.page_id == page_id,
                AutowikiRun.proposal_type.notin_(["sonnet_audit", "opus_audit"]),
                AutowikiRun.u1_median.isnot(None),
            )
            .order_by(AutowikiRun.started_at.desc())
            .first()
        )
        if not row:
            return None
        return {
            "score": row.u1_median,
            "q1": row.q1,
            "rationale": row.judge_rationale,
            "model": row.model_judge,
            "at": row.started_at.isoformat() if row.started_at else None,
        }

    rakon = _latest_rakon()
    sonnet = _latest_audit("sonnet_audit")
    opus = _latest_audit("opus_audit")

    scores = [j["score"] for j in [rakon, sonnet, opus] if j and j["score"] is not None]
    max_divergence = round(max(scores) - min(scores), 4) if len(scores) >= 2 else None

    return {
        "rakon": rakon,
        "sonnet": sonnet,
        "opus": opus,
        "max_divergence": max_divergence,
        "divergence_flagged": max_divergence is not None and max_divergence > 1.5,
    }


# ---------------------------------------------------------------------------
# Kill switch
# ---------------------------------------------------------------------------

@router.post("/kill-switch")
def set_kill_switch(enabled: bool, db: Session = Depends(get_db)):
    try:
        import redis as redis_lib
        from app.config import settings
        r = redis_lib.from_url(settings.REDIS_URL, decode_responses=True)
        if enabled:
            r.set("autowiki:enabled", "1")
        else:
            r.delete("autowiki:enabled")
    except Exception as e:
        raise HTTPException(status_code=503, detail=f"Redis unavailable: {e}")
    return {"autowiki_enabled": enabled}


@router.get("/kill-switch")
def get_kill_switch():
    try:
        import redis as redis_lib
        from app.config import settings
        r = redis_lib.from_url(settings.REDIS_URL, decode_responses=True)
        return {"autowiki_enabled": r.get("autowiki:enabled") == "1"}
    except Exception:
        return {"autowiki_enabled": False}
