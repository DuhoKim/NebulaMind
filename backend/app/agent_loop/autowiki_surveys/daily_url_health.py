"""
daily_url_health — HEAD-probe all surveys at 04:00 KST (19:00 UTC).

For each survey, checks archive_url and mission_url.
On failure: sets url_archive_ok / url_mission_ok = False + enqueues autowiki_surveys_tick.
On success: sets url_archive_ok / url_mission_ok = True (clears stale failures).

Rate-limits: max 3 concurrent probes (httpx async pool), 10s timeout per URL.
"""

from __future__ import annotations

import asyncio
import logging
from datetime import datetime, timezone
from typing import Optional

import httpx
from celery import shared_task
from sqlalchemy import text

log = logging.getLogger(__name__)

_PROBE_TIMEOUT = 10
_CONCURRENCY = 3


async def _head(client: httpx.AsyncClient, url: str) -> bool:
    if not url or not url.startswith("http"):
        return True  # no URL = not a failure
    try:
        r = await client.head(url, follow_redirects=True, timeout=_PROBE_TIMEOUT)
        return r.status_code < 400
    except Exception:
        return False


async def _probe_survey(client: httpx.AsyncClient, survey: dict) -> dict:
    archive_url = survey.get("archive_url") or ""
    mission_url = survey.get("mission_url") or ""

    archive_ok, mission_ok = await asyncio.gather(
        _head(client, archive_url),
        _head(client, mission_url),
    )
    return {
        "id": survey["id"],
        "slug": survey["slug"],
        "archive_ok": archive_ok,
        "mission_ok": mission_ok,
        "archive_url": archive_url,
        "mission_url": mission_url,
    }


async def _run_all_probes(surveys: list) -> list:
    sem = asyncio.Semaphore(_CONCURRENCY)
    results = []

    async def _guarded(client, sv):
        async with sem:
            return await _probe_survey(client, sv)

    async with httpx.AsyncClient() as client:
        tasks = [_guarded(client, sv) for sv in surveys]
        results = await asyncio.gather(*tasks, return_exceptions=True)

    return [r for r in results if isinstance(r, dict)]


@shared_task(name="autowiki_surveys.daily_url_health")
def run_daily_url_health():
    """
    Celery beat task — runs at 19:00 UTC daily (04:00 KST).
    """
    from app.database import SessionLocal
    from app.agent_loop.autowiki_surveys.tasks import autowiki_surveys_tick

    db = SessionLocal()
    try:
        now = datetime.now(timezone.utc)
        rows = db.execute(text("SELECT id, slug, archive_url, mission_url FROM surveys ORDER BY id")).fetchall()
        surveys = [dict(r._mapping) for r in rows]

        results = asyncio.run(_run_all_probes(surveys))

        enqueued = 0
        for res in results:
            sid = res["id"]
            archive_ok = res["archive_ok"]
            mission_ok = res["mission_ok"]

            db.execute(
                text("""
                    UPDATE surveys
                       SET url_archive_ok = :aok,
                           url_mission_ok = :mok,
                           url_checked_at = :now
                     WHERE id = :sid
                """),
                {"aok": archive_ok, "mok": mission_ok, "now": now, "sid": sid},
            )

            if not archive_ok or not mission_ok:
                failed_url = res["archive_url"] if not archive_ok else res["mission_url"]
                autowiki_surveys_tick.delay(
                    sid,
                    "url_health",
                    "urlhealth",
                    failed_url,
                )
                enqueued += 1
                log.info(
                    "URL health FAIL for survey #%d (%s): archive_ok=%s mission_ok=%s",
                    sid, res["slug"], archive_ok, mission_ok,
                )

        db.commit()
        log.info(
            "daily_url_health: probed %d surveys, enqueued %d ticks",
            len(results), enqueued,
        )
        return {"probed": len(results), "enqueued": enqueued}

    finally:
        db.close()
