from celery import Celery
from celery.schedules import crontab

from app.config import settings

celery_app = Celery("nebulamind", broker=settings.REDIS_URL, backend=settings.REDIS_URL, include=["app.agent_loop.tasks", "app.agent_loop.newsletter", "app.agent_loop.facility_curation", "app.agent_loop.news_curator"])

celery_app.conf.update(
    task_serializer="json",
    accept_content=["json"],
    result_serializer="json",
    timezone="UTC",
    enable_utc=True,
    beat_schedule={
        "wake-agents-every-5m": {
            "task": "app.agent_loop.tasks.wake_agents",
            "schedule": 300.0,
        },
        "fetch-arxiv-daily": {
            "task": "app.agent_loop.tasks.fetch_arxiv_daily",
            "schedule": crontab(hour=1, minute=0),  # UTC 01:00 = KST 10:00
        },
        "send-daily-newsletter": {
            "task": "app.agent_loop.newsletter.send_daily_digest",
            "schedule": crontab(hour=1, minute=30),  # UTC 08:30 = KST 17:30 (30min after arxiv fetch)
        },
        "send-arxiv-daily-summary": {
            "task": "app.agent_loop.tasks.send_arxiv_daily_summary",
            "schedule": crontab(hour=1, minute=30),  # UTC 01:30 = KST 10:30 (30min after fetch)
        },
        "retry-unprocessed-arxiv-daily": {
            "task": "app.agent_loop.tasks.retry_unprocessed_arxiv_papers",
            "schedule": crontab(hour=2, minute=15),  # UTC 02:15 = KST 11:15 (daily sweep)
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
        "queue-renovation-daily": {
            "task": "app.agent_loop.tasks.queue_next_renovation",
            "schedule": crontab(hour=2, minute=30),  # UTC 02:30 = KST 11:30
        },
        "rescue-stale-renovations-daily": {
            "task": "app.agent_loop.tasks.rescue_stale_renovation_plans",
            "schedule": crontab(hour=10, minute=0),  # UTC 10:00 = KST 19:00
        },
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
    },
)
