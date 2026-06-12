"""surveys_freshness.py — J6 Mima daily DR-classifier (rides news-curator, §3.2)

Called from news_curator.curate_daily_news after the main pass.
Two-tier apply policy per §3.5b (Papa Q4):
  HIGH-tier fields → queue to survey_update_proposals + Discord
  LOW-tier fields  → auto-apply + log to survey_autoapply_log + Discord
"""
import re
import json
import logging
import datetime

import httpx

from sqlalchemy import text
from app.config import settings
from app.services.llm_utils import strip_think_blocks

log = logging.getLogger(__name__)

OLLAMA_LOCAL = settings.OLLAMA_STUDIO_BASE_URL
MODEL_MIMA   = settings.OLLAMA_STUDIO_HEAVY_MODEL

MIMA_DR_CONFIDENCE_FLOOR = 0.6  # Papa Q3

DR_CLASSIFIER_PROMPT = """\
You are classifying a news headline for whether it announces a new astronomical survey data release.

Headline: {title}
URL: {url}
Survey: {survey_name} ({survey_acronym})
Current DR in our records: {current_dr}

QUESTION: Does this headline announce one of the following?
1. A new data release (e.g. "DR2", "Data Release 3", "Q1 release")
2. A status change (first light, commissioning end, retirement)
3. A new flagship program / observing cycle

Answer JSON ONLY:
{{
  "is_announcement": "yes" | "no",
  "kind": "dr" | "status" | "program" | "other",
  "extracted_dr_string": "<new DR string if kind=dr, else empty>",
  "extracted_status": "<new status if kind=status, else empty>",
  "confidence": <0-1>
}}

ONLY classify as 'yes' if the announcement is the canonical event (not a recap, anniversary,
or paper that merely references the DR). Be conservative.
"""

# Field tier classification per §3.5b
_HIGH_TIER_FIELDS = {
    "current_data_release", "status", "sky_coverage_deg2", "flagship_programs_json",
    "instruments_json", "wavelength_range", "wavelength_band", "redshift_range",
}
_LOW_TIER_FIELDS = {"archive_url", "mission_url", "data_volume"}


def _is_low_tier(field: str) -> bool:
    return field in _LOW_TIER_FIELDS


def _ollama_chat(model: str, prompt: str, timeout: int = 60) -> str | None:
    try:
        resp = httpx.post(
            f"{OLLAMA_LOCAL}/chat/completions",
            json={
                "model": model,
                "messages": [{"role": "user", "content": prompt}],
                "temperature": 0.1,
                "stream": False,
            },
            timeout=timeout,
            headers={"Authorization": "Bearer ollama"},
        )
        resp.raise_for_status()
        return resp.json()["choices"][0]["message"]["content"]
    except Exception as exc:
        log.warning("_ollama_chat %s failed: %s", model, exc)
        return None


def _parse_json(text_: str) -> dict | None:
    if not text_:
        return None
    text_ = re.sub(r"```(?:json)?\s*", "", text_)
    text_ = re.sub(r"```", "", text_)
    text_ = strip_think_blocks(text_)
    try:
        return json.loads(text_.strip())
    except Exception:
        m = re.search(r"\{[\s\S]*\}", text_)
        if m:
            try:
                return json.loads(m.group())
            except Exception:
                pass
    return None


def _discord(msg: str) -> None:
    try:
        from app.config import settings
        url = getattr(settings, "NM_DISCORD_WEBHOOK_URL", None) or settings.DISCORD_WEBHOOK_URL
        if not url:
            return
        httpx.post(url, json={"content": msg[:2000]}, timeout=8)
    except Exception as exc:
        log.debug("Discord notify failed: %s", exc)


def _url_alive(url: str) -> bool:
    try:
        r = httpx.head(url, timeout=10, follow_redirects=True)
        return r.status_code < 400
    except Exception:
        return False


def run_survey_dr_classifier_pass(db, news_items: list) -> dict:
    """
    Called after the daily news pass with the list of news items just processed.
    Each item is expected to have at least: title, url.
    Returns a summary dict.
    """
    surveys = db.execute(text(
        "SELECT id, slug, name, full_name, current_data_release FROM surveys ORDER BY name"
    )).fetchall()

    proposals_queued = 0
    auto_applied     = 0

    for item in news_items:
        title = item.get("title") or item.get("headline") or ""
        url   = item.get("url") or item.get("link") or ""
        if not title:
            continue

        for survey in surveys:
            if survey.name.lower() not in title.lower() and survey.full_name.lower() not in title.lower():
                continue
            # look for DR-class language
            if not re.search(
                r"(DR\d+|Data Release|first[- ]?light|public release|retired|decommission)",
                title, re.I
            ):
                continue

            prompt = DR_CLASSIFIER_PROMPT.format(
                title=title[:300],
                url=url[:200],
                survey_name=survey.full_name,
                survey_acronym=survey.name,
                current_dr=survey.current_data_release or "unknown",
            )
            raw = _ollama_chat(MODEL_MIMA, prompt)
            result = _parse_json(raw) if raw else None
            if not isinstance(result, dict):
                continue

            if result.get("is_announcement") != "yes":
                continue
            confidence = float(result.get("confidence", 0))
            if confidence < MIMA_DR_CONFIDENCE_FLOOR:
                continue

            kind = result.get("kind", "dr")
            if kind == "dr":
                field = "current_data_release"
                proposed = result.get("extracted_dr_string") or ""
                if not proposed:
                    continue
            elif kind == "status":
                field = "status"
                proposed = result.get("extracted_status") or ""
                if not proposed:
                    continue
            else:
                continue

            current_val = getattr(survey, field, None) or ""

            r = _queue_or_apply(db, survey, field, current_val, proposed, confidence,
                                source_kind="mima_news", source_url=url,
                                source_excerpt=title[:300])
            if r == "applied":
                auto_applied += 1
            elif r == "queued":
                proposals_queued += 1

    return {"proposals_queued": proposals_queued, "auto_applied": auto_applied}


def _queue_or_apply(db, survey, field: str, current_value: str, proposed_value: str,
                    confidence: float, source_kind: str, source_url: str, source_excerpt: str) -> str:
    """Apply two-tier policy. Returns 'applied' | 'queued' | 'skipped'."""
    if not proposed_value or proposed_value == current_value:
        return "skipped"

    if _is_low_tier(field):
        meets_floor = _low_stakes_floor_met(field, current_value, proposed_value, confidence, source_kind)
        if meets_floor:
            _do_auto_apply(db, survey, field, current_value, proposed_value,
                           confidence, source_kind, source_url, source_excerpt)
            return "applied"

    # HIGH tier (or low tier that didn't meet floor) → proposal queue
    _do_queue_proposal(db, survey, field, current_value, proposed_value,
                       confidence, source_kind, source_url, source_excerpt)
    return "queued"


def _low_stakes_floor_met(field: str, current_value: str, proposed_value: str,
                           confidence: float, source_kind: str) -> bool:
    if field in ("archive_url", "mission_url"):
        if not proposed_value.startswith(("http://", "https://")):
            return False
        current_broken = not current_value or not _url_alive(current_value)
        proposed_ok = _url_alive(proposed_value)
        return current_broken and proposed_ok
    if field == "data_volume":
        nums_cur = re.findall(r"\d+", current_value or "")
        nums_pro = re.findall(r"\d+", proposed_value or "")
        same_numbers = sorted(nums_cur) == sorted(nums_pro)
        return same_numbers and confidence >= 0.85
    return False


def _do_auto_apply(db, survey, field: str, old_value: str, new_value: str,
                   confidence: float, source_kind: str, source_url: str, source_excerpt: str):
    try:
        db.execute(text(f"UPDATE surveys SET {field} = :val, updated_at = NOW() WHERE id = :sid"),
                   {"val": new_value, "sid": survey.id})
        db.execute(text("""
            INSERT INTO survey_autoapply_log
              (survey_id, field, old_value, new_value, source_kind, source_url, source_excerpt, confidence)
            VALUES (:sid, :field, :old, :new, :sk, :su, :se, :conf)
        """), {
            "sid":  survey.id,
            "field": field,
            "old":  old_value,
            "new":  new_value,
            "sk":   source_kind,
            "su":   source_url,
            "se":   source_excerpt,
            "conf": confidence,
        })
        db.commit()
        _discord(f"🔧 Auto-applied survey fix: `{survey.name}` `{field}` `{old_value}` → `{new_value}` (confidence={confidence:.2f}, source={source_kind})")
        log.info("[J6] auto-applied %s.%s: %r → %r", survey.slug, field, old_value, new_value)
    except Exception as exc:
        db.rollback()
        log.warning("[J6] auto-apply failed %s.%s: %s", survey.slug, field, exc)


def _do_queue_proposal(db, survey, field: str, current_value: str, proposed_value: str,
                       confidence: float, source_kind: str, source_url: str, source_excerpt: str):
    try:
        # supersede stale pending proposals for the same survey+field
        db.execute(text("""
            UPDATE survey_update_proposals
            SET status = 'superseded', reviewed_at = NOW(), reviewed_by = 'auto_supersede'
            WHERE survey_id = :sid AND field = :field AND status = 'pending'
        """), {"sid": survey.id, "field": field})

        db.execute(text("""
            INSERT INTO survey_update_proposals
              (survey_id, field, current_value, proposed_value, source_kind, source_url, source_excerpt, confidence)
            VALUES (:sid, :field, :cur, :prop, :sk, :su, :se, :conf)
        """), {
            "sid":  survey.id,
            "field": field,
            "cur":  current_value,
            "prop": proposed_value,
            "sk":   source_kind,
            "su":   source_url,
            "se":   source_excerpt,
            "conf": confidence,
        })
        db.commit()
        _discord(
            f"📋 Survey update proposal pending review:\n"
            f"  Survey: **{survey.name}** | Field: `{field}`\n"
            f"  Current: `{(current_value or 'none')[:80]}`\n"
            f"  Proposed: `{proposed_value[:80]}`\n"
            f"  Confidence: {confidence:.2f} | Source: {source_kind}\n"
            f"  Approve: `POST /api/admin/surveys/proposals/<id>/approve`"
        )
        log.info("[J6] queued proposal %s.%s: %r → %r", survey.slug, field, current_value, proposed_value)
    except Exception as exc:
        db.rollback()
        log.warning("[J6] queue proposal failed %s.%s: %s", survey.slug, field, exc)
