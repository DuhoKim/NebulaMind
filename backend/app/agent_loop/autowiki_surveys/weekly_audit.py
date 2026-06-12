"""
weekly_audit — Sunday 03:00 KST (18:00 UTC Saturday) full survey audit.

Picks the 3 surveys with the lowest quality_score (NULL scores treated as 0).
For each, recomputes structural quality, then dispatches proseenrich ticks
targeting the weakest field.

Also performs a DR-recency check: surveys with no current_data_release and
status='active' get a drrefresh tick enqueued.
"""

from __future__ import annotations

import logging
from datetime import datetime, timezone

from celery import shared_task
from sqlalchemy import text

log = logging.getLogger(__name__)

_AUDIT_COUNT = 3
_DR_MISSING_STATUS = ("active",)


@shared_task(name="autowiki_surveys.weekly_audit")
def run_weekly_audit():
    """
    Celery beat task — runs at 18:00 UTC Saturday (03:00 KST Sunday).
    """
    from app.database import SessionLocal
    from app.services.survey_health import compute_survey_health, compute_quality
    from app.agent_loop.autowiki_surveys.tasks import autowiki_surveys_tick

    db = SessionLocal()
    try:
        now = datetime.now(timezone.utc)

        # ----------------------------------------------------------------
        # 1. Pick lowest-quality surveys
        # ----------------------------------------------------------------
        rows = db.execute(
            text("""
                SELECT * FROM surveys
                 ORDER BY COALESCE(quality_score, 0) ASC
                 LIMIT :n
            """),
            {"n": _AUDIT_COUNT},
        ).fetchall()
        surveys = [dict(r._mapping) for r in rows]

        enqueued = 0
        for sv in surveys:
            sid = sv["id"]

            # Recompute structural health
            try:
                health = compute_survey_health(
                    sv,
                    url_archive_ok=sv.get("url_archive_ok", True),
                    url_mission_ok=sv.get("url_mission_ok", True),
                )
                new_quality = compute_quality(
                    sv,
                    utility_score=None,
                    url_archive_ok=sv.get("url_archive_ok", True),
                    url_mission_ok=sv.get("url_mission_ok", True),
                )
                db.execute(
                    text("""
                        UPDATE surveys
                           SET quality_score = :q,
                               quality_updated_at = :now
                         WHERE id = :sid
                    """),
                    {"q": new_quality, "now": now, "sid": sid},
                )

                # Pick weakest structural field for prose enrichment
                weak_field = _pick_weakest_field(health)
            except Exception as exc:
                log.warning("weekly_audit: health compute failed for #%d: %s", sid, exc)
                weak_field = "description"

            autowiki_surveys_tick.delay(
                sid,
                "weekly_audit",
                "proseenrich",
                "",
            )
            enqueued += 1
            log.info("weekly_audit: enqueued proseenrich tick for survey #%d (%s)", sid, sv.get("slug"))

        # ----------------------------------------------------------------
        # 2. DR-missing check for active surveys
        # ----------------------------------------------------------------
        dr_missing = db.execute(
            text("""
                SELECT id, slug FROM surveys
                 WHERE (current_data_release IS NULL OR current_data_release = '')
                   AND status = ANY(:statuses)
                 LIMIT 10
            """),
            {"statuses": list(_DR_MISSING_STATUS)},
        ).fetchall()

        for row in dr_missing:
            autowiki_surveys_tick.delay(
                row.id,
                "weekly_audit",
                "drrefresh",
                "",
            )
            enqueued += 1
            log.info("weekly_audit: drrefresh tick for DR-missing survey #%d (%s)", row.id, row.slug)

        db.commit()
        log.info(
            "weekly_audit: audited %d low-quality surveys, enqueued %d total ticks",
            len(surveys), enqueued,
        )
        return {"audited": len(surveys), "enqueued": enqueued}

    finally:
        db.close()


def _pick_weakest_field(health) -> str:
    """Pick the prose field with the lowest component score."""
    c = health.components
    candidates = [
        ("description",    getattr(c, "description_richness", 0.5)),
        ("science_goals",  getattr(c, "science_goals_specificity", 0.5)),
    ]
    return min(candidates, key=lambda x: x[1])[0]
