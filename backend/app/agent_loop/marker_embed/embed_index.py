"""Stage B: embed sentences and claims via Ollama.

Embeddings are cached in-process by content hash. Cache is per-process and
reset on Celery worker restart — acceptable since the embedding call is cheap
(~5 ms/sentence) and the cache only needs to save repeated calls within a
single pipeline run.
"""
import hashlib
import os
import logging
import math
import json
import time
import threading
from typing import Optional

import httpx

from app.config import settings

log = logging.getLogger(__name__)

OLLAMA_BASE = (
    os.getenv("EMBED_OLLAMA_BASE")
    or settings.EMBED_OLLAMA_BASE_URL
    or "http://127.0.0.1:11435"
)  # SSH tunnel to Mac Pro :11434 — not saturated by Celery
EMBED_MODEL = settings.EMBED_OLLAMA_MODEL
COSINE_FLOOR = 0.25  # lowered from 0.45 — Claude aligner picks best match, just needs candidates
TOP_K = 5            # increased from 3 — more candidates for Claude to choose from

_cache: dict[str, Optional[list[float]]] = {}
_stats = {"calls": 0, "hits": 0, "misses": 0, "errors": 0}

# Circuit Breaker state
_local_failures = 0
_local_offline_until = 0.0


def _fast_local_check() -> bool:
    try:
        resp = httpx.get("http://localhost:11434/api/tags", timeout=2.0)
        return resp.status_code == 200
    except Exception:
        return False


def _probe_local_async():
    global _local_failures, _local_offline_until
    log.info("Circuit breaker: Spawning background probe to local Mac Studio...")
    try:
        resp = httpx.get("http://localhost:11434/api/tags", timeout=5.0)
        if resp.status_code == 200:
            _local_failures = 0
            _local_offline_until = 0.0
            log.info("Circuit breaker: Local Mac Studio probe succeeded. Circuit closed (local restored).")
        else:
            log.warning("Circuit breaker: Local Mac Studio probe returned non-200: %s", resp.status_code)
    except Exception as e:
        log.warning("Circuit breaker: Local Mac Studio probe failed: %s", e)



def get_cache_stats() -> dict:
    return dict(_stats) | {"unique_keys": len(_cache)}


def reset_cache_stats() -> None:
    _stats["calls"] = 0
    _stats["hits"] = 0
    _stats["misses"] = 0
    _stats["errors"] = 0


def _cache_key(text: str) -> str:
    return hashlib.sha256(text.encode()).hexdigest()[:20]


def _embed(text: str) -> Optional[list[float]]:
    global _local_failures, _local_offline_until

    _stats["calls"] += 1
    key = _cache_key(text)
    if key in _cache:
        _stats["hits"] += 1
        return _cache[key]
    _stats["misses"] += 1

    local_base = "http://localhost:11434"
    remote_base = OLLAMA_BASE

    now = time.monotonic()
    
    # 1. Determine if local is flagged offline in-process
    local_is_flagged_offline = False
    if _local_failures >= 2:
        if now < _local_offline_until:
            local_is_flagged_offline = True
        else:
            # 5 minutes elapsed since flagging offline, trigger a single background probe call
            _local_offline_until = now + 300.0  # extend offline window during probe execution
            t = threading.Thread(target=_probe_local_async, daemon=True)
            t.start()
            local_is_flagged_offline = True

    # 2. If NOT flagged offline in-process, check Redis health/fast local check
    local_is_healthy_cache = False
    if not local_is_flagged_offline:
        try:
            from app.services.liveness_monitor import _get_redis
            r = _get_redis()
            if r:
                health_str = r.get("ollama:health")
                if health_str:
                    health_data = json.loads(health_str)
                    local_is_healthy_cache = health_data.get("local_online", False)
                else:
                    local_is_healthy_cache = _fast_local_check()
            else:
                local_is_healthy_cache = _fast_local_check()
        except Exception as e:
            log.warning("embed_index: redis health read failed, falling back to fast local check: %s", e)
            local_is_healthy_cache = _fast_local_check()

    # 3. Route request
    # Try local Mac Studio if NOT flagged offline and healthy
    if not local_is_flagged_offline and local_is_healthy_cache:
        try:
            resp = httpx.post(
                f"{local_base}/api/embeddings",
                json={"model": EMBED_MODEL, "prompt": text, "keep_alive": "30m"},
                timeout=6.0,  # >5s timeout to trigger circuit breaker if slow
            )
            resp.raise_for_status()
            vec = resp.json().get("embedding")
            _local_failures = 0  # Reset on successful embedding call
            _cache[key] = vec
            return vec
        except Exception as exc:
            _local_failures += 1
            log.warning("embed_index: local embedding failed (consecutive failures: %d): %s. Routing to remote...", _local_failures, exc)
            if _local_failures >= 2:
                _local_offline_until = time.monotonic() + 300.0
                log.warning("embed_index: local Mac Studio failed twice in a row. Circuit breaker OPEN (flagged offline for 300 seconds).")
            
            # Fallback to remote base immediately
            if remote_base:
                try:
                    resp = httpx.post(
                        f"{remote_base}/api/embeddings",
                        json={"model": EMBED_MODEL, "prompt": text, "keep_alive": "30m"},
                        timeout=10,
                    )
                    resp.raise_for_status()
                    vec = resp.json().get("embedding")
                    _cache[key] = vec
                    return vec
                except Exception as fallback_exc:
                    log.warning("embed_index: remote fallback embedding failed: %s", fallback_exc)
    else:
        # Route directly to remote base/fallback
        if remote_base:
            try:
                resp = httpx.post(
                    f"{remote_base}/api/embeddings",
                    json={"model": EMBED_MODEL, "prompt": text, "keep_alive": "30m"},
                    timeout=10,
                )
                resp.raise_for_status()
                vec = resp.json().get("embedding")
                _cache[key] = vec
                return vec
            except Exception as fallback_exc:
                log.warning("embed_index: direct remote fallback embedding failed: %s", fallback_exc)

    _stats["errors"] += 1
    _cache[key] = None
    return None


def _cosine(a: list[float], b: list[float]) -> float:
    dot = sum(x * y for x, y in zip(a, b))
    na = math.sqrt(sum(x * x for x in a))
    nb = math.sqrt(sum(x * x for x in b))
    if na == 0.0 or nb == 0.0:
        return 0.0
    return dot / (na * nb)


def rank_candidates(claim_text: str, sentences: list[str], top_k: int = TOP_K, cosine_floor: float = COSINE_FLOOR) -> list[tuple[str, float]]:
    """
    Return up to top_k sentences scored ≥ cosine_floor, sorted by cosine desc.
    Returns [] if the claim embedding fails.
    """
    claim_vec = _embed(claim_text)
    if claim_vec is None:
        return []

    scored: list[tuple[str, float]] = []
    for sent in sentences:
        vec = _embed(sent)
        if vec is None:
            continue
        score = _cosine(claim_vec, vec)
        if score >= cosine_floor:
            scored.append((sent, score))

    scored.sort(key=lambda x: x[1], reverse=True)
    return scored[:top_k]
