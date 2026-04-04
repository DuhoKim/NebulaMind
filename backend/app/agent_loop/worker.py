from celery import Celery

from app.config import settings

celery_app = Celery("nebulamind", broker=settings.REDIS_URL, backend=settings.REDIS_URL, include=["app.agent_loop.tasks"])

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
    },
)
