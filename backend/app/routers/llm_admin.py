"""LLM Routing admin API — public endpoints for /admin/llm dashboard."""
from fastapi import APIRouter, Depends, Query
from sqlalchemy.orm import Session
from sqlalchemy import text

from app.database import get_db

router = APIRouter(prefix="/api/admin/llm", tags=["llm-admin"])


@router.get("/routing", summary="Get current model routing table")
def get_routing():
    from app.services.llm_routing.routing import ROUTING
    return [
        {"role": role, "models": [m["label"] for m in models]}
        for role, models in ROUTING.items()
    ]


@router.get("/calls", summary="Recent LLM calls telemetry")
def get_calls(limit: int = Query(default=100, le=500), db: Session = Depends(get_db)):
    rows = db.execute(text(
        "SELECT task_role, model_label, success, latency_ms, created_at "
        "FROM llm_calls ORDER BY created_at DESC LIMIT :limit"
    ), {"limit": limit}).all()
    return [
        {
            "task_role": r.task_role,
            "model_label": r.model_label,
            "success": r.success,
            "latency_ms": r.latency_ms,
            "created_at": r.created_at.isoformat(),
        }
        for r in rows
    ]


@router.get("/stats", summary="Model performance stats (last 24h)")
def get_stats(db: Session = Depends(get_db)):
    rows = db.execute(text("""
        SELECT model_label,
               COUNT(*) as cnt,
               AVG(latency_ms) as avg_ms,
               AVG(CASE WHEN success THEN 1.0 ELSE 0.0 END) as success_rate
        FROM llm_calls
        WHERE created_at > NOW() - INTERVAL '24 hours'
        GROUP BY model_label
        ORDER BY cnt DESC
    """)).all()
    return {
        r.model_label: {
            "count": r.cnt,
            "avg_ms": round(r.avg_ms) if r.avg_ms else None,
            "success_rate": round(float(r.success_rate), 3),
        }
        for r in rows
    }
