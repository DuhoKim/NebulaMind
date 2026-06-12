from __future__ import annotations

import logging
from typing import Any

from celery import shared_task

from app.agent_loop.worker import celery_app
from app.config import settings
from app.database import SessionLocal
from app.services.page_registry import active_pages_for, budget_exhausted

log = logging.getLogger(__name__)


LANE_TASKS: dict[str, tuple[str, str | None]] = {
    "autowiki_tick": ("app.agent_loop.autowiki.tasks.autowiki_tick", "page_id"),
    "rakon_deep_pass": ("app.agent_loop.autowiki.deep_synthesis.rakon_deep_pass", "page_id"),
    "judges.sonnet": ("app.agent_loop.autowiki.judge_panel.sonnet_judge_tick", "page_id"),
    "judges.opus": ("app.agent_loop.autowiki.judge_panel.opus_judge_tick", "page_id"),
    "buddle_claim_propose": ("app.agent_loop.research_ideas.auto_improvement.buddle_claim_propose", "page_id"),
    "rakon_draft_async": ("app.agent_loop.research_ideas.auto_improvement.rakon_draft_async", "page_id"),
    "rakon_synthesis_pass": ("app.agent_loop.research_ideas.auto_improvement.rakon_synthesis_pass", "page_id"),
    "rakon_adversarial_probe": ("app.agent_loop.research_ideas.auto_improvement.rakon_adversarial_probe", "page_id"),
    "sonnet_section_rewrite": ("app.agent_loop.autowiki.tasks.sonnet_section_rewrite", "page_id"),
    "seed_debated_claim_ideas": ("app.agent_loop.research_ideas.auto_improvement.seed_debated_claim_ideas", "page_id"),
    "generate_research_ideas_v2": ("app.agent_loop.research_ideas.auto_improvement.generate_research_ideas_v2", "page_slug"),
    "run_rakon_coherence_pass": ("app.agent_loop.autowiki.tasks.run_rakon_coherence_pass", "page_id"),
    "drain_evidence_for_page": ("app.agent_loop.tasks.drain_evidence_for_page", "page_id"),
    "backfill_intro_excerpts": ("app.agent_loop.tasks.backfill_intro_excerpts", None),
    "sync_verbatim_markers_nightly": ("app.agent_loop.tasks.sync_verbatim_markers_nightly", "page_id"),
}


@shared_task(name="app.agent_loop.registry.dispatch_lane", max_retries=0)
def dispatch_lane(
    lane: str,
    task_key: str,
    extra_kwargs: dict[str, Any] | None = None,
    *,
    include_onboarding: bool = False,
    shadow: bool = False,
) -> dict[str, Any]:
    task_name, page_param = LANE_TASKS[task_key]
    extra_kwargs = dict(extra_kwargs or {})

    with SessionLocal() as db:
        pages = active_pages_for(db, lane, include_onboarding=include_onboarding)
        selected = [page.page_id for page in pages]
        if shadow:
            expected = [] if lane == "coherence" else [57]
            if selected != expected:
                raise RuntimeError(
                    f"page registry shadow mismatch lane={lane} selected={selected} expected={expected}"
                )
            log.info("[page_registry] shadow lane=%s task=%s selected=%s", lane, task_key, selected)
            return {"status": "shadow_ok", "lane": lane, "task_key": task_key, "selected": selected}

        if page_param is None:
            celery_app.send_task(task_name, kwargs=extra_kwargs)
            return {
                "status": "dispatched",
                "lane": lane,
                "task_key": task_key,
                "selected": selected,
                "count": 1,
            }

        dispatched: list[dict[str, Any]] = []
        for index, page in enumerate(pages):
            if budget_exhausted(db, page.page_id, lane, page.budget_caps):
                continue
            kwargs = dict(extra_kwargs)
            kwargs[page_param] = page.slug if page_param == "page_slug" else page.page_id
            celery_app.send_task(
                task_name,
                kwargs=kwargs,
                countdown=index * settings.REGISTRY_DISPATCH_STAGGER_SECONDS,
            )
            dispatched.append({"page_id": page.page_id, "slug": page.slug, "task": task_name})

    return {"status": "dispatched", "lane": lane, "task_key": task_key, "pages": dispatched}
