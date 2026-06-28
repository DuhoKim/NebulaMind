"""Daily smoke calls for the active NebulaMind model platoon."""

from __future__ import annotations

import logging
import time
from dataclasses import dataclass

import httpx
from celery import shared_task

from app.config import settings
from app.utils.premium_dispatch import log_llm_call

log = logging.getLogger(__name__)


@dataclass(frozen=True)
class CanarySeat:
    label: str
    base_url: str
    model: str


def _chat_url(base_url: str) -> str:
    base = base_url.rstrip("/")
    if base.endswith("/v1"):
        return f"{base}/chat/completions"
    return f"{base}/v1/chat/completions"


def platoon_canary_seats() -> list[CanarySeat]:
    return [
        CanarySeat("Buddle", settings.BUDDLE_BASE_URL, settings.BUDDLE_MODEL),
        CanarySeat("Nutty", settings.OLLAMA_BASE_URL, settings.OLLAMA_STUDIO_FAST_MODEL),
        CanarySeat("Mima", settings.OLLAMA_BASE_URL, settings.OLLAMA_STUDIO_HEAVY_MODEL),
        CanarySeat("Tera", settings.OLLAMA_BASE_URL, settings.ADVERSARIAL_QUERY_MODEL),
        CanarySeat("Pico", settings.OLLAMA_BASE_URL, settings.ASTRO_SCORER_MODEL),
        CanarySeat("Vera", settings.OLLAMA_BASE_URL, settings.ASTRO_SYNTH_MODEL),
        CanarySeat("Blanc", settings.OLLAMA_BASE_URL, "llama3.3:70b"),
        CanarySeat("Rakon-proxy", settings.RAKON_BASE_URL, settings.RAKON_MODEL),
    ]


def _discord_critical(message: str) -> None:
    webhook = getattr(settings, "DISCORD_WEBHOOK_URL", "") or getattr(settings, "NM_DISCORD_WEBHOOK_URL", "")
    if not webhook:
        return
    try:
        httpx.post(webhook, json={"content": message}, timeout=10)
    except Exception as exc:
        log.warning("model canary Discord alert failed: %s", exc)


def _check_seat(seat: CanarySeat, *, notify: bool = True) -> dict:
    started = time.monotonic()
    status = "pass"
    error = None
    content = ""
    status_code = None
    try:
        resp = httpx.post(
            _chat_url(seat.base_url),
            headers={"Authorization": "Bearer ollama"},
            json={
                "model": seat.model,
                "messages": [
                    {
                        "role": "system",
                        "content": "You are a healthcheck canary. Reply with exactly: ok",
                    },
                    {"role": "user", "content": "/no_think\nping"},
                ],
                "stream": False,
                "temperature": 0,
                # GPT-OSS via Ollama's OpenAI-compatible chat endpoint may spend
                # the first few tokens in hidden reasoning even when thinking is
                # disabled. Keep enough budget for the visible healthcheck token.
                "max_tokens": 64,
                "thinking": False,
                "reasoning_effort": "none",
                "options": {"num_ctx": 1024},
            },
            timeout=120,
        )
        status_code = resp.status_code
        if resp.status_code >= 400:
            raise RuntimeError(f"HTTP {resp.status_code}: {resp.text[:500]}")
        data = resp.json()
        content = (((data.get("choices") or [{}])[0].get("message") or {}).get("content") or "").strip()
        if not content:
            raise RuntimeError("empty content")
    except Exception as exc:
        status = "fail"
        error = str(exc)

    latency_ms = int((time.monotonic() - started) * 1000)
    log_llm_call(
        "model_canary",
        seat.label,
        model_name=seat.model,
        success=status == "pass",
        latency_ms=latency_ms,
        error=error,
    )
    result = {
        "label": seat.label,
        "model": seat.model,
        "status": status,
        "latency_ms": latency_ms,
        "status_code": status_code,
        "content_preview": content[:80],
        "error": error,
    }
    if status != "pass":
        message = f"CRITICAL model canary failed: {seat.label} {seat.model} - {error}"
        log.critical(message)
        if notify:
            _discord_critical(message)
    return result


@shared_task(name="app.services.model_canary.run_model_call_canary")
def run_model_call_canary() -> dict:
    results = [_check_seat(seat) for seat in platoon_canary_seats()]
    failures = [r for r in results if r["status"] != "pass"]
    return {
        "status": "fail" if failures else "pass",
        "failures": len(failures),
        "results": results,
    }
