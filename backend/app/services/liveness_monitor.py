import json
import time
import logging
import httpx
from app.agent_loop.worker import celery_app
from app.config import settings

logger = logging.getLogger(__name__)

def _get_redis():
    try:
        import redis as redis_lib
        return redis_lib.from_url(settings.REDIS_URL, decode_responses=True)
    except Exception:
        return None

def update_liveness_cache() -> dict:
    """Queries local (Mac Studio) and remote (Mac Pro tunnel) Ollama instances,
    measures latencies and available models, and caches the result in Redis.
    """
    results = {
        "local_online": False,
        "local_latency_ms": -1.0,
        "local_models": [],
        "remote_online": False,
        "remote_latency_ms": -1.0,
        "remote_models": []
    }

    # Query local
    try:
        t0 = time.perf_counter()
        resp = httpx.get("http://localhost:11434/api/tags", timeout=5.0)
        latency = (time.perf_counter() - t0) * 1000.0
        if resp.status_code == 200:
            results["local_online"] = True
            results["local_latency_ms"] = float(latency)
            models_data = resp.json().get("models", [])
            results["local_models"] = [m.get("name", "") for m in models_data if m.get("name")]
        else:
            results["local_latency_ms"] = float(latency)
            logger.warning(f"[liveness_monitor] Local Ollama non-200 response: {resp.status_code}")
    except Exception as e:
        logger.warning(f"[liveness_monitor] Failed to query local Ollama: {e}")

    # Query remote
    try:
        t0 = time.perf_counter()
        resp = httpx.get("http://127.0.0.1:11435/api/tags", timeout=5.0)
        latency = (time.perf_counter() - t0) * 1000.0
        if resp.status_code == 200:
            results["remote_online"] = True
            results["remote_latency_ms"] = float(latency)
            models_data = resp.json().get("models", [])
            results["remote_models"] = [m.get("name", "") for m in models_data if m.get("name")]
        else:
            results["remote_latency_ms"] = float(latency)
            logger.warning(f"[liveness_monitor] Remote Ollama non-200 response: {resp.status_code}")
    except Exception as e:
        logger.warning(f"[liveness_monitor] Failed to query remote Ollama: {e}")

    # Save dictionary as JSON string under Redis key ollama:health
    r = _get_redis()
    if r:
        try:
            r.set("ollama:health", json.dumps(results))
            logger.info(f"[liveness_monitor] Successfully updated Redis key 'ollama:health': {results}")
        except Exception as e:
            logger.error(f"[liveness_monitor] Failed to set ollama:health key in Redis: {e}")
    else:
        logger.warning("[liveness_monitor] Redis client is not available to save liveness cache")

    return results

@celery_app.task(name="app.services.liveness_monitor.run_liveness_check")
def run_liveness_check():
    logger.info("[liveness_monitor] Running scheduled run_liveness_check task")
    return update_liveness_cache()
