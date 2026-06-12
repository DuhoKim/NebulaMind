"""Lightweight helper: mark a Celery agent as recently active via last_active."""
import logging

logger = logging.getLogger(__name__)


def mark_celery_agent_active(db, model_name: str) -> None:
    """Update last_active = NOW() for the agent row matching model_name.

    Called just before db.commit() at page-write commit points so that
    /api/stats online_agent reflects real Celery activity.
    Non-fatal: any exception is swallowed and logged.
    """
    try:
        from sqlalchemy import text
        db.execute(
            text("UPDATE agents SET last_active = NOW() WHERE model_name = :m"),
            {"m": model_name},
        )
    except Exception as exc:
        logger.debug("[agent_ping] mark_celery_agent_active failed for %s: %s", model_name, exc)
