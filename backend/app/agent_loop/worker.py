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
            "schedule": crontab(hour=8, minute=0),  # UTC 08:00 = KST 17:00
        },
        "send-daily-newsletter": {
            "task": "app.agent_loop.newsletter.send_daily_digest",
            "schedule": crontab(hour=8, minute=30),  # UTC 08:30 = KST 17:30 (30min after arxiv fetch)
        },
    },
)
