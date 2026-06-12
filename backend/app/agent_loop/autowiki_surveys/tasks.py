"""
autowiki_surveys_tick — main Celery task for the Surveys autoresearch loop.

Dispatched by:
  - daily_url_health.py  (trigger='url_health', edit_type='urlhealth')
  - weekly_audit.py      (trigger='weekly_audit', edit_type varies)
  - news_curator.py      (trigger='event_dr', edit_type='drrefresh')
  - Manual / API calls   (trigger='manual')

DB schema (autowiki_surveys_v1 migration):
  autowiki_surveys_runs: trigger, edit_type (NOT NULL), model_proposer (NOT NULL),
    decision (NOT NULL), field_path, source_url, error_text, ...
  survey_update_proposals: field, source_kind, source_url, source_excerpt,
    current_value, proposed_value, confidence, status
  survey_autoapply_log: field, old_value, new_value, source_kind,
    source_url, source_excerpt, confidence, applied_at
"""

from __future__ import annotations

import json
import logging
import time
from datetime import datetime, timezone
from typing import Optional

import httpx
from celery import shared_task

log = logging.getLogger(__name__)

_REDIS_URL = "redis://localhost:6379/0"
_LOCK_TTL = 600  # 10 min AstroSage lock TTL

_ASTROSAGE_LOCK_KEY = "astrosage:in_use"
_SURVEYS_PRIORITY_KEY = "astrosage:surveys_priority"
_SURVEYS_ENABLED_KEY = "autowiki:surveys:enabled"

# edit_type → source_kind mapping for proposal/log rows
_SOURCE_KIND: dict[str, str] = {
    "urlhealth":   "url_probe",
    "drrefresh":   "dr_news",
    "fieldpatch":  "field_patch",
    "proseenrich": "prose_enrich",
}

# edit_type → proposer model name
_MODEL_PROPOSER: dict[str, str] = {
    "urlhealth":   "blanc",
    "drrefresh":   "blanc",
    "fieldpatch":  "blanc",
    "proseenrich": "blanc",
}


# ---------------------------------------------------------------------------
# Redis helpers
# ---------------------------------------------------------------------------

def _redis():
    import redis as _redis_lib
    return _redis_lib.from_url(_REDIS_URL, decode_responses=True)


def _check_surveys_enabled() -> bool:
    try:
        r = _redis()
        val = r.get(_SURVEYS_ENABLED_KEY)
        return val not in ("0", "false", "off", "disabled")
    except Exception:
        return True


def _claim_astrosage(survey_slug: str) -> bool:
    try:
        r = _redis()
        r.set(_SURVEYS_PRIORITY_KEY, survey_slug, ex=_LOCK_TTL)
        acquired = r.set(_ASTROSAGE_LOCK_KEY, f"surveys:{survey_slug}", nx=True, ex=_LOCK_TTL)
        return bool(acquired)
    except Exception:
        return True  # proceed on Redis error


def _release_astrosage():
    try:
        r = _redis()
        r.delete(_ASTROSAGE_LOCK_KEY)
        r.delete(_SURVEYS_PRIORITY_KEY)
    except Exception as exc:
        log.warning("_release_astrosage error: %s", exc)


# ---------------------------------------------------------------------------
# DB helpers
# ---------------------------------------------------------------------------

def _load_survey(db, survey_id: int) -> Optional[object]:
    from sqlalchemy import text
    return db.execute(
        text("SELECT * FROM surveys WHERE id = :id"), {"id": survey_id}
    ).fetchone()


def _survey_to_dict(row) -> dict:
    return dict(row._mapping) if row is not None else {}


def _discord(msg: str):
    try:
        from app.config import settings
        url = getattr(settings, "NM_DISCORD_WEBHOOK_URL", None) or getattr(
            settings, "DISCORD_WEBHOOK_URL", None
        )
        if url:
            httpx.post(url, json={"content": msg}, timeout=10)
    except Exception:
        pass


# ---------------------------------------------------------------------------
# Two-tier apply
# ---------------------------------------------------------------------------

_LOW_CONFIDENCE_FLOOR = 0.70
_HIGH_FIELDS = {"current_data_release", "status"}


def _is_low_stake(proposal: dict) -> bool:
    if proposal.get("stake") == "high":
        return False
    if proposal.get("field") in _HIGH_FIELDS:
        return False
    return proposal.get("confidence", 0.0) >= _LOW_CONFIDENCE_FLOOR


def _auto_apply(db, survey_id: int, proposal: dict):
    from sqlalchemy import text
    field = proposal["field"]
    value = proposal["proposed_value"]
    now = datetime.now(timezone.utc)
    source_kind = _SOURCE_KIND.get(proposal.get("edit_type", ""), "prose_enrich")

    db.execute(
        text(f"UPDATE surveys SET {field} = :val, updated_at = :now WHERE id = :sid"),
        {"val": value, "now": now, "sid": survey_id},
    )
    db.execute(
        text("""
            INSERT INTO survey_autoapply_log
              (survey_id, field, old_value, new_value, source_kind,
               source_url, source_excerpt, confidence, applied_at)
            VALUES
              (:sid, :field, :old, :new, :skind, :src, :excerpt, :conf, :now)
        """),
        {
            "sid":     survey_id,
            "field":   field,
            "old":     "",
            "new":     value,
            "skind":   source_kind,
            "src":     proposal.get("source_url", ""),
            "excerpt": proposal.get("headline", "")[:500] if proposal.get("headline") else "",
            "conf":    proposal.get("confidence", 0.0),
            "now":     now,
        },
    )
    db.commit()
    _discord(
        f"[autowiki-surveys] auto-applied `{field}` for survey #{survey_id} "
        f"(confidence {proposal.get('confidence', 0):.2f})"
    )


def _queue_proposal(db, survey_id: int, proposal: dict):
    from sqlalchemy import text
    now = datetime.now(timezone.utc)
    source_kind = _SOURCE_KIND.get(proposal.get("edit_type", ""), "prose_enrich")

    # Supersede old pending proposals for this survey+field
    db.execute(
        text("""
            UPDATE survey_update_proposals
               SET status = 'superseded'
             WHERE survey_id = :sid AND field = :field AND status = 'pending'
        """),
        {"sid": survey_id, "field": proposal["field"]},
    )
    db.execute(
        text("""
            INSERT INTO survey_update_proposals
              (survey_id, field, current_value, proposed_value,
               source_kind, source_url, source_excerpt, confidence, status, created_at)
            VALUES
              (:sid, :field, :cval, :pval, :skind, :src, :excerpt, :conf, 'pending', :now)
        """),
        {
            "sid":     survey_id,
            "field":   proposal["field"],
            "cval":    "",
            "pval":    proposal["proposed_value"],
            "skind":   source_kind,
            "src":     proposal.get("source_url", ""),
            "excerpt": proposal.get("headline", "")[:500] if proposal.get("headline") else "",
            "conf":    proposal.get("confidence", 0.0),
            "now":     now,
        },
    )
    db.commit()
    _discord(
        f"[autowiki-surveys] queued HIGH-stake proposal for survey #{survey_id} "
        f"field `{proposal['field']}` (confidence {proposal.get('confidence', 0):.2f}) — "
        f"awaiting Papa review."
    )


# ---------------------------------------------------------------------------
# Main tick task
# ---------------------------------------------------------------------------

@shared_task(name="autowiki_surveys.tick", bind=True, max_retries=2, default_retry_delay=120)
def autowiki_surveys_tick(
    self,
    survey_id: int,
    trigger: str,
    edit_type: str = "",
    source_url: str = "",
    headline: str = "",
):
    """
    Main entry point for all survey autoresearch ticks.

    trigger:   "url_health" | "weekly_audit" | "event_dr" | "manual"
    edit_type: "urlhealth" | "proseenrich" | "drrefresh" | "fieldpatch" | ""
    """
    if not _check_surveys_enabled():
        log.info("autowiki:surveys disabled — skipping survey #%d", survey_id)
        return {"skipped": True, "reason": "disabled"}

    from app.database import SessionLocal
    from app.agent_loop.autowiki_surveys.proposers import (
        propose_urlhealth,
        propose_fieldpatch,
        propose_drrefresh,
        propose_proseenrich,
    )
    from app.agent_loop.autowiki_surveys.judge import judge_survey_prose
    from sqlalchemy import text

    db = SessionLocal()
    run_id = None
    astrosage_held = False
    model_proposer = _MODEL_PROPOSER.get(edit_type, "blanc")

    try:
        now = datetime.now(timezone.utc)
        row = _load_survey(db, survey_id)
        if row is None:
            log.warning("autowiki_surveys_tick: survey #%d not found", survey_id)
            return {"error": "not_found"}

        survey = _survey_to_dict(row)
        slug = survey.get("slug", str(survey_id))

        # Insert run row (decision='running' placeholder; updated at end)
        result = db.execute(
            text("""
                INSERT INTO autowiki_surveys_runs
                  (survey_id, trigger, edit_type, model_proposer,
                   decision, source_url, started_at)
                VALUES (:sid, :trigger, :etype, :mproposer,
                        'running', :src, :now)
                RETURNING id
            """),
            {
                "sid":       survey_id,
                "trigger":   trigger,
                "etype":     edit_type or "unknown",
                "mproposer": model_proposer,
                "src":       source_url,
                "now":       now,
            },
        )
        run_id = result.fetchone()[0]
        db.commit()

        # Dispatch to appropriate proposer
        proposal = None

        if edit_type == "urlhealth":
            check_result = {
                "archive_ok": survey.get("url_archive_ok", True),
                "mission_ok": survey.get("url_mission_ok", True),
                "tested_url": source_url,
            }
            proposal = propose_urlhealth(survey, check_result)

        elif edit_type == "drrefresh":
            if headline:
                proposal = propose_drrefresh(survey, headline, source_url)
            elif source_url:
                proposal = propose_fieldpatch(
                    survey,
                    f"Possible DR update for {survey.get('name', slug)}",
                    source_url,
                )

        elif edit_type == "fieldpatch":
            if headline:
                proposal = propose_fieldpatch(survey, headline, source_url)

        elif edit_type == "proseenrich":
            if not _claim_astrosage(slug):
                log.info("AstroSage busy; retrying survey #%d in 2 min", survey_id)
                raise self.retry(countdown=120)
            astrosage_held = True

            field = "description"
            proposal = propose_proseenrich(survey, field)

            if proposal:
                judgment = judge_survey_prose(
                    survey,
                    field=proposal["field"],
                    current=survey.get(proposal["field"], ""),
                    proposed=proposal["proposed_value"],
                )
                if judgment["verdict"] != "accept":
                    log.info(
                        "ProseEnrich rejected for survey #%d field %s (composite %.2f)",
                        survey_id, field, judgment["composite"],
                    )
                    # Record the rejection
                    db.execute(
                        text("""
                            UPDATE autowiki_surveys_runs
                               SET decision = 'rejected',
                                   reject_reason = :rr,
                                   judge_rationale = :jr,
                                   judge_prompt_version = 'v1',
                                   model_judge = :mj,
                                   finished_at = :now
                             WHERE id = :rid
                        """),
                        {
                            "rr":  judgment.get("verdict_reason", "composite below threshold"),
                            "jr":  judgment.get("verdict_reason", ""),
                            "mj":  judgment.get("model_used", "astrosage-70b"),
                            "now": datetime.now(timezone.utc),
                            "rid": run_id,
                        },
                    )
                    db.commit()
                    return {"decision": "rejected", "survey_id": survey_id, "run_id": run_id}

                proposal["proposed_value"] = judgment["preferred_text"]
                proposal["confidence"] = min(0.95, judgment["composite"] / 10.0)

                # Update run with judge info
                db.execute(
                    text("""
                        UPDATE autowiki_surveys_runs
                           SET model_judge = :mj,
                               judge_rationale = :jr,
                               judge_prompt_version = 'v1'
                         WHERE id = :rid
                    """),
                    {
                        "mj":  judgment.get("model_used", "astrosage-70b"),
                        "jr":  judgment.get("verdict_reason", ""),
                        "rid": run_id,
                    },
                )

        # Apply or queue
        decision = "no_proposal"
        if proposal:
            if _is_low_stake(proposal):
                _auto_apply(db, survey_id, proposal)
                decision = "auto_applied"
            else:
                _queue_proposal(db, survey_id, proposal)
                decision = "queued"

        # Finalise run row
        db.execute(
            text("""
                UPDATE autowiki_surveys_runs
                   SET decision = :decision,
                       field_path = :fp,
                       finished_at = :now
                 WHERE id = :rid
            """),
            {
                "decision": decision,
                "fp":       proposal.get("field") if proposal else None,
                "now":      datetime.now(timezone.utc),
                "rid":      run_id,
            },
        )
        db.commit()
        return {"decision": decision, "survey_id": survey_id, "run_id": run_id}

    except self.MaxRetriesExceededError:
        _discord(f"[autowiki-surveys] max retries exceeded for survey #{survey_id} trigger={trigger}")
        return {"error": "max_retries"}

    except Exception as exc:
        log.exception("autowiki_surveys_tick failed for survey #%d: %s", survey_id, exc)
        if run_id:
            try:
                db.execute(
                    text("""
                        UPDATE autowiki_surveys_runs
                           SET decision = 'error', error_text = :e, finished_at = :now
                         WHERE id = :rid
                    """),
                    {"e": str(exc)[:2000], "now": datetime.now(timezone.utc), "rid": run_id},
                )
                db.commit()
            except Exception:
                pass
        raise

    finally:
        if astrosage_held:
            _release_astrosage()
        db.close()
