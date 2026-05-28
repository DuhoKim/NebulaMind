from celery import Celery
from celery.schedules import crontab

from app.config import settings

celery_app = Celery("nebulamind", broker=settings.REDIS_URL, backend=settings.REDIS_URL, include=["app.agent_loop.tasks", "app.agent_loop.arxiv_fetch", "app.agent_loop.newsletter", "app.agent_loop.facility_curation", "app.agent_loop.news_curator", "app.agent_loop.doi_backfill", "app.agent_loop.autowiki.tasks", "app.agent_loop.autowiki.deep_synthesis", "app.agent_loop.autowiki.judge_panel", "app.agent_loop.research_ideas.auto_improvement", "app.agent_loop.research_ideas.dataset_verify", "app.agent_loop.autowiki_surveys.tasks", "app.agent_loop.autowiki_surveys.daily_url_health", "app.agent_loop.autowiki_surveys.weekly_audit", "app.agent_loop.marker_embed.tasks"])

celery_app.conf.update(
    task_serializer="json",
    accept_content=["json"],
    result_serializer="json",
    timezone="UTC",
    enable_utc=True,
    beat_schedule={
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
        "retry-unprocessed-arxiv-daily": {
            "task": "app.agent_loop.tasks.retry_unprocessed_arxiv_papers",
            "schedule": crontab(hour=2, minute=15),  # UTC 02:15 = KST 11:15 (daily sweep)
        },
        "process-pending-verify-retries": {
            "task": "app.agent_loop.tasks.process_pending_verify_retries",
            "schedule": crontab(hour=8, minute=0),  # UTC 08:00 = KST 17:00 (48h ADS-lag retry)
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
        "drain-stance-jury-hourly": {
            "task": "app.agent_loop.tasks.drain_stance_jury_backlog",
            "schedule": crontab(minute=0),  # every hour at :00
        },
        "adversarial-pass-daily": {
            "task": "app.agent_loop.tasks.run_adversarial_pass",
            "schedule": crontab(hour=4, minute=0),  # UTC 04:00 = KST 13:00
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
        # Pilot page is hardcoded in tasks.py (PILOT_PAGE_ID=57)
        "autowiki-tick": {
            "task": "app.agent_loop.autowiki.tasks.autowiki_tick",
            "schedule": 600.0,  # v3: 15 min → 10 min (144 ticks/day)
        },
        # rakon-deep-pass: tightened from 6h to 2h (§9.5.2 v2)
        "rakon-deep-pass-2h": {
            "task": "app.agent_loop.autowiki.deep_synthesis.rakon_deep_pass",
            "schedule": crontab(minute=0, hour="*/2"),
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
            "schedule": crontab(minute=30),
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
            "schedule": crontab(minute=0, hour=15),          # 15 UTC = 00 KST daily
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
    },
)

# Route autowiki long-running tasks to a dedicated queue so they don't get
# buried behind stance-jury bursts. A separate worker pinned to -Q autowiki
# drains this queue (see com.nebulamind.celery_autowiki.plist).
celery_app.conf.task_routes = {
    "app.agent_loop.autowiki.tasks.autowiki_tick":                              {"queue": "autowiki"},
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
}

from celery.signals import worker_ready
import httpx as _httpx_boot
from app.config import settings as _settings_boot

@worker_ready.connect
def _evict_non_resident_on_boot(sender, **_kwargs):
    keep = {
        "astrosage-70b:latest",
        _settings_boot.OLLAMA_STUDIO_FAST_MODEL,
        _settings_boot.OLLAMA_STUDIO_HEAVY_MODEL,
        "gemma3:27b",                                # Tera
        "phi4:14b",                                  # Takji
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
