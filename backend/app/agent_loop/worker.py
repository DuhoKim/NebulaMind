from celery import Celery
from celery.schedules import crontab

from app.config import settings

celery_app = Celery("nebulamind", broker=settings.REDIS_URL, backend=settings.REDIS_URL, include=["app.agent_loop.tasks", "app.agent_loop.newsletter"])

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
            "schedule": crontab(hour=1, minute=0),  # UTC 08:00 = KST 17:00
        },
        "send-daily-newsletter": {
            "task": "app.agent_loop.newsletter.send_daily_digest",
            "schedule": crontab(hour=1, minute=30),  # UTC 08:30 = KST 17:30 (30min after arxiv fetch)
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
    },
)
