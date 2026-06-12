from __future__ import annotations

import datetime as dt
import logging
from dataclasses import dataclass
from typing import Any

from sqlalchemy import text
from sqlalchemy.orm import Session

from app.config import settings

log = logging.getLogger(__name__)


PAGE_REGISTRY_LANES = {
    "autowiki",
    "deep_synthesis",
    "judges",
    "section_rewrite",
    "coherence",
    "research_ideas",
    "adversarial",
    "gap_detect",
    "evidence_drain",
    "verbatim_sync",
    "arxiv_feed_l2",
}

WRITE_LANES = {
    "autowiki",
    "deep_synthesis",
    "judges",
    "section_rewrite",
    "coherence",
    "research_ideas",
    "adversarial",
    "gap_detect",
    "evidence_drain",
    "verbatim_sync",
}


@dataclass(frozen=True)
class RegistryPage:
    page_id: int
    slug: str
    title: str
    category: str | None
    budget_caps: dict[str, Any]
    model_assignments: dict[str, Any]
    calibration_config_path: str | None


def _json_dict(value: Any) -> dict[str, Any]:
    return value if isinstance(value, dict) else {}


def active_pages_for(db: Session, lane: str, *, include_onboarding: bool = False) -> list[RegistryPage]:
    if lane not in PAGE_REGISTRY_LANES:
        raise ValueError(f"unknown registry lane: {lane}")

    statuses = ["active"]
    if include_onboarding and lane not in WRITE_LANES:
        statuses.append("onboarding")

    rows = db.execute(
        text(
            """
            SELECT po.page_id,
                   wp.slug,
                   wp.title,
                   wp.category,
                   po.budget_caps,
                   po.model_assignments,
                   po.calibration_config_path
            FROM page_orchestration po
            JOIN wiki_pages wp ON wp.id = po.page_id
            WHERE po.status = ANY(:statuses)
              AND COALESCE((po.enabled_lanes ->> :lane)::boolean, false)
            ORDER BY po.page_id
            """
        ),
        {"lane": lane, "statuses": statuses},
    ).mappings().all()

    return [
        RegistryPage(
            page_id=int(row["page_id"]),
            slug=str(row["slug"]),
            title=str(row["title"]),
            category=row["category"],
            budget_caps=_json_dict(row["budget_caps"]),
            model_assignments=_json_dict(row["model_assignments"]),
            calibration_config_path=row["calibration_config_path"],
        )
        for row in rows
    ]


def registry_slugs_for_feed(db: Session) -> list[str]:
    pages = active_pages_for(db, "arxiv_feed_l2", include_onboarding=True)
    return [page.slug for page in pages]


def budget_exhausted(db: Session, page_id: int, lane: str, budget_caps: dict[str, Any]) -> bool:
    daily_caps = _json_dict(budget_caps.get("daily_llm_calls"))
    cap = daily_caps.get(lane)
    if not cap:
        return False

    since = dt.datetime.utcnow().replace(hour=0, minute=0, second=0, microsecond=0)
    has_scope_columns = db.execute(
        text(
            """
            SELECT count(*)
            FROM information_schema.columns
            WHERE table_name = 'llm_calls'
              AND column_name IN ('page_id', 'lane')
            """
        )
    ).scalar_one()
    if int(has_scope_columns) < 2:
        log.info("[page_registry] budget advisory skipped: llm_calls has no page_id/lane columns yet")
        return False

    count = db.execute(
        text(
            """
            SELECT count(*)
            FROM llm_calls
            WHERE page_id = :page_id
              AND lane = :lane
              AND created_at >= :since
            """
        ),
        {"page_id": page_id, "lane": lane, "since": since},
    ).scalar_one()

    exhausted = int(count) >= int(cap)
    if exhausted or not settings.REGISTRY_ENFORCE_BUDGETS:
        log.info(
            "[page_registry] budget check page=%s lane=%s used=%s cap=%s enforce=%s exhausted=%s",
            page_id,
            lane,
            count,
            cap,
            settings.REGISTRY_ENFORCE_BUDGETS,
            exhausted,
        )
    return exhausted if settings.REGISTRY_ENFORCE_BUDGETS else False


def category_for_slug(db: Session, slug: str) -> str | None:
    return db.execute(
        text("SELECT category FROM wiki_pages WHERE slug = :slug"),
        {"slug": slug},
    ).scalar_one_or_none()
