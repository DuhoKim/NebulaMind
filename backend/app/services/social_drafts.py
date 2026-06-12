"""Social post auto-drafting for featured news items."""
import re
import json
import datetime as dt

import httpx
from sqlalchemy.orm import Session

from app.config import settings
from app.models.social import SocialPostDraft
from app.models.facility import FacilityNewsItem
from app.services.llm_utils import strip_think_blocks
from app.utils.model_guard import guard_batch_model
from app.utils.premium_dispatch import dispatch_premium, log_llm_spend

OLLAMA_BASE = "http://localhost:11434"
OLLAMA_MODEL = settings.OLLAMA_STUDIO_HEAVY_MODEL

PLATFORM_CONFIGS = {
    "twitter": {
        "max_chars": 280,
        "tone": "concise, professional, one key insight",
        "hashtag_hint": "2-3 hashtags max",
    },
    "bluesky": {
        "max_chars": 300,
        "tone": "professional, slightly more detail than Twitter",
        "hashtag_hint": "2-3 hashtags",
    },
}

DRAFT_PROMPT = """\
You write social media posts for NebulaMind, an astronomy research platform.
Audience: professional astronomers, astrophysicists, and graduate students.

News item:
  Title: {title}
  Summary: {summary}
  Facility: {facility}
  Source: {source_url}
  Kind: {kind}

Write a {platform} post ({max_chars} chars max).
Tone: {tone}.
Hashtags: {hashtag_hint}. Include relevant ones like #{facility_tag} #Astronomy.
If there is a source URL, end with it.
Reply with ONLY the post text, no commentary."""

FACILITY_HASHTAGS = {
    "desi": "DESI",
    "jwst": "JWST",
    "euclid": "Euclid",
    "lsst-rubin": "RubinObservatory",
    "rubin": "RubinObservatory",
    "alma": "ALMA",
    "vla": "VLA",
}


def _call_ollama(prompt: str) -> str | None:
    try:
        model = guard_batch_model(OLLAMA_MODEL, "services.social_drafts")
        est_tokens = max(1, len(prompt) // 4)
        dispatch_premium("services.social_drafts", model, est_tokens)
        resp = httpx.post(
            f"{OLLAMA_BASE}/v1/chat/completions",
            json={
                "model": model,
                "messages": [{"role": "user", "content": prompt}],
                "temperature": 0.4,
                "stream": False,
            },
            timeout=60,
        )
        resp.raise_for_status()
        data = resp.json()
        usage = data.get("usage") or {}
        log_llm_spend(
            "services.social_drafts",
            model,
            prompt_tokens=usage.get("prompt_tokens"),
            completion_tokens=usage.get("completion_tokens"),
            estimated_tokens=est_tokens,
        )
        text = strip_think_blocks(data["choices"][0]["message"]["content"])
        return text
    except Exception as ex:
        print(f"[social_drafts] ollama error: {ex}")
        return None


def draft_social_post(
    db: Session,
    news_item: FacilityNewsItem,
    platform: str,
) -> SocialPostDraft | None:
    """Generate and store a draft social post for the given news item and platform."""
    cfg = PLATFORM_CONFIGS.get(platform)
    if not cfg:
        raise ValueError(f"Unknown platform: {platform}")

    facility_tag = FACILITY_HASHTAGS.get(
        (news_item.facility.slug if news_item.facility else "") or "", "Astronomy"
    )

    prompt = DRAFT_PROMPT.format(
        title=news_item.title,
        summary=news_item.summary or "",
        facility=news_item.facility.short_name if news_item.facility else "Unknown",
        source_url=news_item.source_url or "",
        kind=news_item.kind,
        platform=platform.capitalize(),
        max_chars=cfg["max_chars"],
        tone=cfg["tone"],
        hashtag_hint=cfg["hashtag_hint"],
        facility_tag=facility_tag,
    )

    draft_text = _call_ollama(prompt)
    if not draft_text:
        return None

    # Trim to platform limit
    if len(draft_text) > cfg["max_chars"]:
        draft_text = draft_text[: cfg["max_chars"] - 1] + "…"

    draft = SocialPostDraft(
        news_item_id=news_item.id,
        platform=platform,
        draft_text=draft_text,
        status="draft",
    )
    db.add(draft)
    db.flush()
    return draft


def draft_posts_for_featured(db: Session) -> int:
    """Auto-draft Twitter + BlueSky posts for today's top-3 featured items."""
    today_start = dt.datetime.utcnow().replace(hour=0, minute=0, second=0, microsecond=0)
    featured = (
        db.query(FacilityNewsItem)
        .filter(FacilityNewsItem.featured.is_(True))
        .filter(FacilityNewsItem.created_at >= today_start)
        .order_by(FacilityNewsItem.credibility_score.desc())
        .limit(3)
        .all()
    )

    drafted = 0
    for item in featured:
        for platform in ("twitter", "bluesky"):
            # Skip if already drafted today for this item+platform
            existing = (
                db.query(SocialPostDraft)
                .filter(SocialPostDraft.news_item_id == item.id)
                .filter(SocialPostDraft.platform == platform)
                .first()
            )
            if existing:
                continue
            draft = draft_social_post(db, item, platform)
            if draft:
                drafted += 1

    db.commit()
    return drafted
