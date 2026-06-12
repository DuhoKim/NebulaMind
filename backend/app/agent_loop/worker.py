from celery import Celery
from celery.schedules import crontab
import os

from app.config import settings

celery_app = Celery("nebulamind", broker=settings.REDIS_URL, backend=settings.REDIS_URL, include=["app.agent_loop.tasks", "app.agent_loop.arxiv_fetch", "app.agent_loop.newsletter", "app.agent_loop.facility_curation", "app.agent_loop.news_curator", "app.agent_loop.doi_backfill", "app.agent_loop.autowiki.tasks", "app.agent_loop.autowiki.deep_synthesis", "app.agent_loop.autowiki.judge_panel", "app.agent_loop.research_ideas.auto_improvement", "app.agent_loop.research_ideas.dataset_verify", "app.agent_loop.registry", "app.agent_loop.autowiki_surveys.tasks", "app.agent_loop.autowiki_surveys.daily_url_health", "app.agent_loop.autowiki_surveys.weekly_audit", "app.agent_loop.marker_embed.tasks", "app.services.liveness_monitor", "app.services.model_canary"])

celery_app.conf.update(
    task_serializer="json",
    accept_content=["json"],
    result_serializer="json",
    timezone="UTC",
    enable_utc=True,
    beat_schedule={
        "liveness-check-30s": {
            "task": "app.services.liveness_monitor.run_liveness_check",
            "schedule": 30.0,
        },
        "model-call-canary-daily": {
            "task": "app.services.model_canary.run_model_call_canary",
            "schedule": crontab(hour=0, minute=20),  # UTC 00:20 = KST 09:20
        },
        "fetch-arxiv-daily": {
            "task": "app.agent_loop.tasks.fetch_arxiv_daily",
            "schedule": crontab(hour=1, minute=0),  # UTC 01:00 = KST 10:00
        },
        "send-daily-newsletter": {
            "task": "app.agent_loop.newsletter.send_daily_digest",
            "schedule": crontab(hour=1, minute=30),  # UTC 01:30 = KST 10:30 (30min after arxiv fetch)
        },
        "send-arxiv-daily-summary": {
            "task": "app.agent_loop.tasks.send_arxiv_daily_summary",
            "schedule": crontab(hour=1, minute=30),  # UTC 01:30 = KST 10:30 (30min after fetch)
        },
        "arxiv-wiki-feed-v2-daily-mode1": {
            "task": "app.agent_loop.tasks.arxiv_wiki_feed_daily",
            "schedule": crontab(hour=1, minute=10),  # chained by fetch; beat is a safety net
            "kwargs": {"trigger": "beat_safety_net"},
        },
        "retry-unprocessed-arxiv-daily": {
            "task": "app.agent_loop.tasks.retry_unprocessed_arxiv_papers",
            "schedule": crontab(hour=2, minute=15, day_of_week=0),  # weekly cleanup sweep
        },
        "arxiv-wiki-feed-v2-retry-coverage": {
            "task": "app.agent_loop.tasks.arxiv_wiki_feed_retry_coverage",
            "schedule": crontab(hour=2, minute=15),  # Layer 2 retryable coverage sweep
        },
        "process-pending-verify-retries": {
            "task": "app.agent_loop.tasks.process_pending_verify_retries",
            "schedule": crontab(hour=8, minute=0, day_of_week=0),  # weekly cleanup sweep
        },
        "update-coverage-map-daily": {
            "task": "app.agent_loop.tasks.update_coverage_map",
            "schedule": crontab(hour=2, minute=0),  # UTC 02:00 = KST 11:00 (after arxiv + newsletter)
        },
        "refresh-wikipedia-summaries-daily": {
            "task": "app.agent_loop.tasks.refresh_wikipedia_summaries",
            "schedule": crontab(hour=3, minute=0),  # UTC 03:00 = KST 12:00
        },
        "cluster-new-topic-candidates-daily": {
            "task": "app.agent_loop.tasks.cluster_new_topic_candidates",
            "schedule": crontab(hour=2, minute=0),  # UTC 02:00 = KST 11:00, same slot as coverage-map
        },
        # D1 triage (state audit 2026-06-12): expire >30d low-sim, enforce queue cap
        "triage-new-page-proposals-daily": {
            "task": "app.agent_loop.tasks.triage_new_page_proposals",
            "schedule": crontab(hour=2, minute=40),  # after the daily clustering run
        },
        "drain-stance-jury-hourly": {
            "task": "app.agent_loop.tasks.drain_stance_jury_backlog",
            "schedule": crontab(minute=0),  # every hour at :00
        },
        "adversarial-pass-daily": {
            "task": "app.agent_loop.tasks.run_adversarial_pass",
            "schedule": crontab(hour=4, minute=0, day_of_week=0),  # weekly re-mining lane
        },
        "temporal-decay-daily": {
            "task": "app.agent_loop.tasks.run_temporal_decay",
            "schedule": crontab(hour=5, minute=0),  # UTC 05:00 = KST 14:00
        },
        "sweep-human-overrides-daily": {
            "task": "app.agent_loop.tasks.sweep_human_overrides",
            "schedule": crontab(hour=6, minute=0),  # UTC 06:00 = KST 15:00
        },
        "facility-daily-curation": {
            "task": "facility_curation.run_daily",
            "schedule": crontab(hour=6, minute=30),  # UTC 06:30 = KST 15:30
        },
        "sweep-council-tiers-hourly": {
            "task": "app.agent_loop.tasks.sweep_council_tiers",
            "schedule": crontab(minute=45),  # at :45 each hour
        },
        "sweep-stale-escalations-daily": {
            "task": "app.agent_loop.tasks.sweep_stale_escalations",
            "schedule": crontab(hour=7, minute=0),  # UTC 07:00 = KST 16:00
        },
        "settle-evidence-reputation-hourly": {
            "task": "app.agent_loop.tasks.settle_evidence_and_update_rep",
            "schedule": crontab(minute=15),  # at :15, after stance jury at :00
        },
        "dispatch-jury-webhooks-hourly": {
            "task": "app.agent_loop.tasks.dispatch_jury_webhooks",
            "schedule": crontab(minute=30),  # at :30, after settlement at :15
        },
        "jury-fast-drain-30min": {
            "task": "app.agent_loop.tasks.drain_jury_fast_pass",
            "schedule": 1800.0,  # every 30 minutes
        },
        # DISABLED 2026-05-12: old generic-LLM renovation pipeline replaced by autowiki loop
        # (autowiki loop uses AstroSage-70B + judge-gated quality control — no garbage writes)
        # "queue-renovation-daily": {
        #     "task": "app.agent_loop.tasks.queue_next_renovation",
        #     "schedule": crontab(hour=2, minute=30),
        # },
        # "rescue-stale-renovations-daily": {
        #     "task": "app.agent_loop.tasks.rescue_stale_renovation_plans",
        #     "schedule": crontab(hour=10, minute=0),
        # },
        "warm-models-every-20min": {
            "task": "app.agent_loop.tasks.warm_models",
            "schedule": 1200.0,  # every 20 minutes
        },
        "check-api-key-expiry-daily": {
            "task": "app.agent_loop.tasks.check_api_key_expiry",
            "schedule": crontab(hour=9, minute=30),  # UTC 09:30 = KST 18:30
        },
        "agent-behavior-scores-daily": {
            "task": "app.agent_loop.tasks.update_agent_behavior_scores",
            "schedule": crontab(hour=8, minute=0),  # UTC 08:00 = KST 17:00
        },
        "gdpr-purge-weekly": {
            "task": "app.agent_loop.tasks.gdpr_subscriber_purge",
            "schedule": crontab(hour=9, minute=0, day_of_week=1),  # Monday UTC 09:00
        },
        "curate-news-daily": {
            "task": "app.agent_loop.news_curator.curate_daily_news",
            "schedule": crontab(hour=16, minute=0),  # UTC 16:00 = KST 01:00
        },
        "doi-backfill-nightly": {
            "task": "app.agent_loop.doi_backfill.sweep_recent_refereed",
            "schedule": crontab(hour=19, minute=0),  # UTC 19:00 = KST 04:00 (3h after news curation)
        },
        # autowiki-tick: disabled behind Redis flag `autowiki:enabled`
        # Enable via: redis-cli set autowiki:enabled 1
        # Page selection moves to page_orchestration when BEAT_SCHEDULE_MODE != legacy.
        "autowiki-tick": {
            "task": "app.agent_loop.autowiki.tasks.autowiki_tick",
            "schedule": 600.0,  # v3: 15 min → 10 min (144 ticks/day)
            "kwargs": {"page_id": 57},
        },
        # rakon-deep-pass: tightened from 6h to 2h (§9.5.2 v2)
        "rakon-deep-pass-2h": {
            "task": "app.agent_loop.autowiki.deep_synthesis.rakon_deep_pass",
            "schedule": crontab(minute=0, hour=2, day_of_week=0),  # weekly re-mining lane
            "kwargs": {"page_id": 57},
        },
        # sonnet-judge-tick: HwaO (claude-sonnet-4-6) independent quality audit
        # Scores only — no commit/rollback. Gated behind autowiki:enabled.
        "sonnet-judge-tick": {
            "task": "app.agent_loop.autowiki.judge_panel.sonnet_judge_tick",
            "schedule": 1200.0,  # 20 min
            "kwargs": {"page_id": 57},
        },
        # opus-judge-tick: Kun (claude-opus-4-7) deep authoritative audit
        # Scores only — no commit/rollback. Gated behind autowiki:enabled.
        "opus-judge-tick": {
            "task": "app.agent_loop.autowiki.judge_panel.opus_judge_tick",
            "schedule": 3600.0,  # 60 min
            "kwargs": {"page_id": 57},
        },
        # §9 v3 lanes — retune 2026-05-15 per beat_schedule_v3.md
        "idea-judge-q4h": {                                   # was idea-judge-tri-daily (3×/day → 6×/day)
            "task": "app.agent_loop.research_ideas.auto_improvement.judge_idea_pool",
            "schedule": crontab(minute=0, hour="*/4"),        # 00/04/08/12/16/20 UTC
        },
        "buddle-draft-q6h": {                                 # was buddle-draft-tri-daily (3×/day → 4×/day)
            "task": "app.agent_loop.research_ideas.auto_improvement.buddle_draft_async",
            "schedule": crontab(minute=0, hour="*/6"),        # 00/06/12/18 UTC
        },
        "buddle-claim-propose-q3h": {                         # NEW v3 B4: Buddle proposes claims from orphan ideas
            "task": "app.agent_loop.research_ideas.auto_improvement.buddle_claim_propose",
            "schedule": crontab(minute=15, hour="*/3"),       # :15 offset to avoid collision
            "kwargs": {"page_id": 57},
        },
        "buddle-evidence-pair-hourly": {
            "task": "app.agent_loop.research_ideas.auto_improvement.buddle_evidence_pair",
            "schedule": crontab(hour=6, minute=30, day_of_week=0),  # weekly evidence-pair cleanup
        },
        "opus-hero-refresh-8h": {                             # was astrosage-hero-refresh-8h; now Opus
            "task": "app.agent_loop.research_ideas.auto_improvement.opus_hero_refresh",
            "schedule": crontab(minute=0, hour="20,4,12"),   # 05/13/21 KST
        },
        "rakon-draft-async-q4h": {                           # NEW v3 R2: Rakon idea draft every 4h (6×/day)
            "task": "app.agent_loop.research_ideas.auto_improvement.rakon_draft_async",
            "schedule": crontab(minute=0, hour="*/4"),       # 00/04/08/12/16/20 UTC
            "kwargs": {"page_id": 57},
        },
        "rakon-synthesis-pass-q8h": {                        # NEW v3 R4: Rakon section rewrite proposer
            "task": "app.agent_loop.research_ideas.auto_improvement.rakon_synthesis_pass",
            "schedule": crontab(minute=30, hour="1,9,17"),   # 01:30/09:30/17:30 UTC (offset from rakon-deep-pass)
            "kwargs": {"page_id": 57},
        },
        "rakon-adversarial-probe-daily": {                   # was rakon-adversarial-probe-mwf (3×/wk → daily)
            "task": "app.agent_loop.research_ideas.auto_improvement.rakon_adversarial_probe",
            "schedule": crontab(minute=0, hour=15, day_of_week=0),  # weekly re-mining lane
            "kwargs": {"page_id": 57},
        },
        "sonnet-section-rewrite-q30m": {                     # NEW v3 §3.3: Sonnet active section proposer
            "task": "app.agent_loop.autowiki.tasks.sonnet_section_rewrite",
            "schedule": crontab(minute="15,45"),             # :15 and :45 (offset from autowiki_tick :00)
            "kwargs": {"page_id": 57},
        },
        "mima-cross-page-synthesis-6h": {
            "task": "app.agent_loop.research_ideas.auto_improvement.mima_cross_page_synthesis",
            "schedule": crontab(minute=0, hour="*/6"),
        },
        "tera-evidence-audit-12h": {
            "task": "app.agent_loop.research_ideas.auto_improvement.tera_evidence_audit",
            "schedule": crontab(minute=0, hour="22,10"),     # 07/19 KST
        },
        "takji-schema-validate-4h": {
            "task": "app.agent_loop.research_ideas.auto_improvement.takji_schema_validate",
            "schedule": crontab(minute=0, hour="*/4"),
        },
        "nutty-trust-recompute-hourly": {
            "task": "app.agent_loop.research_ideas.auto_improvement.nutty_trust_recompute",
            "schedule": crontab(minute=20),
        },
        "tera-coverage-audit-mwf": {
            "task": "app.agent_loop.research_ideas.auto_improvement.tera_coverage_audit",
            "schedule": crontab(minute=0, hour=17, day_of_week="1,3,5"),
        },
        # J11: coverage detection — Tuesday 02:00 KST = Monday 17:00 UTC
        "idea-coverage-detection": {
            "task": "app.agent_loop.research_ideas.auto_improvement.coverage_detection_pass",
            "schedule": crontab(hour=17, minute=0, day_of_week=1),  # Mon 17:00 UTC = Tue 02:00 KST
        },
        # debated-claim seeder: every 6h; :15 offset to avoid 00/06/12/18 collisions
        "debated-claim-seeder-6h": {
            "task": "app.agent_loop.research_ideas.auto_improvement.seed_debated_claim_ideas",
            "schedule": crontab(minute=15, hour="*/6"),
            "kwargs": {"page_id": 57, "target_per_claim": 3},
        },
        # Karpathy v2 gap-detection: 04:10 KST daily (UTC 19:10); staggered 10min after doi-backfill
        "karpathy-v2-gap-detect-daily": {
            "task": "app.agent_loop.research_ideas.auto_improvement.generate_research_ideas_v2",
            "schedule": crontab(hour=19, minute=10),  # UTC 19:10 = KST 04:10
            "kwargs": {"page_slug": "galaxy-evolution"},
        },
        # Autowiki-Surveys: daily URL health probe — 04:00 KST = UTC 19:00
        "autowiki-surveys-daily-url-health": {
            "task": "autowiki_surveys.daily_url_health",
            "schedule": crontab(hour=19, minute=0),  # UTC 19:00 = KST 04:00
        },
        # Autowiki-Surveys: weekly audit — Sunday 03:00 KST = Sat 18:00 UTC
        "autowiki-surveys-weekly-audit": {
            "task": "autowiki_surveys.weekly_audit",
            "schedule": crontab(hour=18, minute=0, day_of_week=6),  # Sat 18:00 UTC = Sun 03:00 KST
        },
        # Autowiki coherence: full-page Rakon rewrite — Sunday 02:00 UTC = KST 11:00
        "autowiki-coherence-weekly": {
            "task": "app.agent_loop.autowiki.tasks.run_rakon_coherence_pass",
            "schedule": crontab(hour=2, minute=0, day_of_week=0),  # Every Sunday 02:00 UTC
            "kwargs": {"page_id": 57},
        },
        # P1-A: drain evidence for page 57 (hourly)
        "drain-evidence-p57": {
            "task": "app.agent_loop.tasks.drain_evidence_for_page",
            "schedule": crontab(minute=30),
            "kwargs": {"page_id": 57},
        },
        "backfill-intro-excerpts": {
            "task": "app.agent_loop.tasks.backfill_intro_excerpts",
            "schedule": crontab(minute=10, hour="*/2"),
        },
        # P1-C: nightly verbatim sync + alarm (daily at 03:00 UTC)
        "sync-verbatim-nightly-p57": {
            "task": "app.agent_loop.tasks.sync_verbatim_markers_nightly",
            "schedule": crontab(hour=3, minute=0),
            "kwargs": {"page_id": 57},
        },
    },
)


_REGISTRY_DISPATCH_TASK = "app.agent_loop.registry.dispatch_lane"
_REGISTRY_BEAT_ENTRIES = {
    "autowiki-tick": {"lane": "autowiki", "task_key": "autowiki_tick"},
    "rakon-deep-pass-2h": {"lane": "deep_synthesis", "task_key": "rakon_deep_pass"},
    "sonnet-judge-tick": {"lane": "judges", "task_key": "judges.sonnet"},
    "opus-judge-tick": {"lane": "judges", "task_key": "judges.opus"},
    "buddle-claim-propose-q3h": {"lane": "research_ideas", "task_key": "buddle_claim_propose"},
    "rakon-draft-async-q4h": {"lane": "research_ideas", "task_key": "rakon_draft_async"},
    "rakon-synthesis-pass-q8h": {"lane": "section_rewrite", "task_key": "rakon_synthesis_pass"},
    "rakon-adversarial-probe-daily": {"lane": "adversarial", "task_key": "rakon_adversarial_probe"},
    "sonnet-section-rewrite-q30m": {"lane": "section_rewrite", "task_key": "sonnet_section_rewrite"},
    "debated-claim-seeder-6h": {
        "lane": "research_ideas",
        "task_key": "seed_debated_claim_ideas",
        "extra_kwargs": {"target_per_claim": 3},
    },
    "karpathy-v2-gap-detect-daily": {"lane": "gap_detect", "task_key": "generate_research_ideas_v2"},
    "autowiki-coherence-weekly": {"lane": "coherence", "task_key": "run_rakon_coherence_pass"},
    "sync-verbatim-nightly-p57": {"lane": "verbatim_sync", "task_key": "sync_verbatim_markers_nightly"},
}


def _registry_entry(source_entry: dict, registry_kwargs: dict, *, shadow: bool) -> dict:
    kwargs = {
        "lane": registry_kwargs["lane"],
        "task_key": registry_kwargs["task_key"],
        "extra_kwargs": registry_kwargs.get("extra_kwargs"),
        "shadow": shadow,
    }
    return {
        "task": _REGISTRY_DISPATCH_TASK,
        "schedule": source_entry["schedule"],
        "kwargs": kwargs,
    }


def _apply_page_registry_schedule_mode() -> None:
    mode = (os.getenv("BEAT_SCHEDULE_MODE") or settings.BEAT_SCHEDULE_MODE or "legacy").strip().lower()
    schedule = celery_app.conf.beat_schedule
    if mode not in {"legacy", "registry_shadow", "registry"}:
        raise RuntimeError(f"Unsupported BEAT_SCHEDULE_MODE={settings.BEAT_SCHEDULE_MODE!r}")
    if mode == "legacy":
        return

    for schedule_name, registry_kwargs in _REGISTRY_BEAT_ENTRIES.items():
        source_entry = schedule[schedule_name]
        registry_schedule_name = schedule_name.replace("-p57", "")
        if mode == "registry":
            schedule.pop(schedule_name)
            schedule[registry_schedule_name] = _registry_entry(source_entry, registry_kwargs, shadow=False)
        else:
            schedule[f"registry-shadow-{registry_schedule_name}"] = _registry_entry(
                source_entry,
                registry_kwargs,
                shadow=True,
            )


_apply_page_registry_schedule_mode()

# Route autowiki long-running tasks to a dedicated queue so they don't get
# buried behind stance-jury bursts. A separate worker pinned to -Q autowiki
# drains this queue (see com.nebulamind.celery_autowiki.plist).
celery_app.conf.task_routes = {
    "app.agent_loop.registry.dispatch_lane":                                      {"queue": "autowiki"},
    "app.agent_loop.autowiki.tasks.autowiki_tick":                              {"queue": "autowiki"},
    "app.agent_loop.autowiki.tasks.autowiki_propose_and_commit":                {"queue": "autowiki"},
    "app.agent_loop.autowiki.tasks.autowiki_post_pipeline_notify":              {"queue": "autowiki"},
    "app.agent_loop.autowiki.tasks.autowiki_pipeline_rollback":                 {"queue": "autowiki"},
    "app.agent_loop.autowiki.deep_synthesis.rakon_deep_pass":                   {"queue": "autowiki"},
    "app.agent_loop.research_ideas.auto_improvement.process_lightweight_event": {"queue": "autowiki"},
    "app.agent_loop.research_ideas.auto_improvement.judge_idea_pool":           {"queue": "autowiki"},
    "app.agent_loop.research_ideas.auto_improvement.rakon_draft_async":         {"queue": "autowiki"},
    "app.agent_loop.research_ideas.auto_improvement.mima_draft_async":          {"queue": "autowiki"},
    "app.agent_loop.research_ideas.auto_improvement.tera_draft_async":          {"queue": "autowiki"},
    "app.agent_loop.research_ideas.auto_improvement.buddle_draft_async":        {"queue": "autowiki"},
    "app.agent_loop.research_ideas.auto_improvement.rakon_adversarial_probe":   {"queue": "autowiki"},
    "app.agent_loop.research_ideas.auto_improvement.buddle_evidence_pair":      {"queue": "autowiki"},
    "app.agent_loop.research_ideas.auto_improvement.astrosage_hero_refresh":    {"queue": "autowiki"},
    "app.agent_loop.research_ideas.auto_improvement.opus_hero_refresh":         {"queue": "autowiki"},
    "app.agent_loop.research_ideas.auto_improvement.rakon_synthesis_pass":      {"queue": "autowiki"},
    "app.agent_loop.research_ideas.auto_improvement.buddle_claim_propose":      {"queue": "autowiki"},
    "app.agent_loop.autowiki.tasks.sonnet_section_rewrite":                     {"queue": "autowiki"},
    "app.agent_loop.research_ideas.auto_improvement.mima_cross_page_synthesis": {"queue": "autowiki"},
    "app.agent_loop.research_ideas.auto_improvement.tera_coverage_audit":       {"queue": "autowiki"},
    "app.agent_loop.research_ideas.auto_improvement.tera_evidence_audit":       {"queue": "autowiki"},
    "app.agent_loop.research_ideas.auto_improvement.takji_schema_validate":     {"queue": "autowiki"},
    "app.agent_loop.research_ideas.auto_improvement.seed_debated_claim_ideas":  {"queue": "autowiki"},
    "app.agent_loop.research_ideas.auto_improvement.generate_research_ideas_v2": {"queue": "autowiki"},
    "app.agent_loop.research_ideas.auto_improvement.nutty_trust_recompute":     {"queue": "celery"},
    "autowiki_surveys.tick":                                                    {"queue": "autowiki"},
    "autowiki_surveys.weekly_audit":                                            {"queue": "autowiki"},
    "app.agent_loop.autowiki.tasks.run_rakon_coherence_pass":                   {"queue": "autowiki"},
    "app.agent_loop.marker_embed.tasks.claim_marker_embed_page":                {"queue": "autowiki"},
    "app.services.liveness_monitor.run_liveness_check":                         {"queue": "celery"},
    "app.services.model_canary.run_model_call_canary":                          {"queue": "celery"},
}

from celery.signals import task_failure, task_postrun, task_prerun, worker_ready
import httpx as _httpx_boot
from app.config import settings as _settings_boot

_SCHEDULE_NAMES_BY_TASK: dict[str, str] = {}
for _schedule_name, _entry in celery_app.conf.beat_schedule.items():
    _task_name = _entry.get("task")
    if not _task_name or _schedule_name == "liveness-check-30s":
        continue
    if _task_name in _SCHEDULE_NAMES_BY_TASK:
        _SCHEDULE_NAMES_BY_TASK[_task_name] = f"{_SCHEDULE_NAMES_BY_TASK[_task_name]},{_schedule_name}"
    else:
        _SCHEDULE_NAMES_BY_TASK[_task_name] = _schedule_name

_PIPELINE_RUN_IDS: dict[str, int | None] = {}


@task_prerun.connect
def _pipeline_run_start(task_id=None, task=None, args=None, kwargs=None, **_kwargs):
    task_name = getattr(task, "name", None)
    if not task_name or task_name not in _SCHEDULE_NAMES_BY_TASK:
        return
    try:
        from app.services.pipeline_runs import start_pipeline_run

        _PIPELINE_RUN_IDS[task_id] = start_pipeline_run(
            task_name=task_name,
            task_id=task_id,
            schedule_name=_SCHEDULE_NAMES_BY_TASK.get(task_name),
            args=args,
            kwargs=kwargs,
        )
    except Exception as exc:
        print(f"[pipeline_runs] start skipped for {task_name}: {exc}")


@task_postrun.connect
def _pipeline_run_finish(task_id=None, task=None, retval=None, state=None, **_kwargs):
    task_name = getattr(task, "name", None)
    if not task_name or task_name not in _SCHEDULE_NAMES_BY_TASK:
        return
    run_id = _PIPELINE_RUN_IDS.pop(task_id, None)
    try:
        from app.services.pipeline_runs import finish_pipeline_run

        finish_pipeline_run(
            run_id=run_id,
            task_id=task_id,
            status="failed" if state == "FAILURE" else "finished",
            result=retval,
        )
    except Exception as exc:
        print(f"[pipeline_runs] finish skipped for {task_name}: {exc}")


@task_failure.connect
def _pipeline_run_failure(task_id=None, exception=None, traceback=None, sender=None, **_kwargs):
    task_name = getattr(sender, "name", None)
    if not task_name or task_name not in _SCHEDULE_NAMES_BY_TASK:
        return
    try:
        from app.services.pipeline_runs import finish_pipeline_run

        finish_pipeline_run(
            run_id=_PIPELINE_RUN_IDS.get(task_id),
            task_id=task_id,
            status="failed",
            error=f"{exception}\n{traceback}"[:4000],
        )
    except Exception as exc:
        print(f"[pipeline_runs] failure skipped for {task_name}: {exc}")

@worker_ready.connect
def _evict_non_resident_on_boot(sender, **_kwargs):
    keep = {
        "astrosage-70b:latest",
        _settings_boot.OLLAMA_STUDIO_FAST_MODEL,
        _settings_boot.OLLAMA_STUDIO_HEAVY_MODEL,
        _settings_boot.ADVERSARIAL_QUERY_MODEL,      # Tera
        _settings_boot.BUDDLE_MODEL,                 # Buddle
        "vanta-research/atom-astronomy-7b:latest",
        _settings_boot.EMBED_OLLAMA_MODEL,           # marker-embed Stage B
    }
    try:
        loaded = _httpx_boot.get("http://localhost:11434/api/ps", timeout=5).json().get("models", [])
        for m in loaded:
            name = m.get("name") or m.get("model")
            if name and name not in keep:
                _httpx_boot.post("http://localhost:11434/api/generate",
                                 json={"model": name, "keep_alive": 0}, timeout=5)
                print(f"[boot-evict] requested unload of {name}")
    except Exception as e:
        print(f"[boot-evict] skipped: {e}")
