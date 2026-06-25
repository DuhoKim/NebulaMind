"""Stage D: independent veto judge for marker overlay.

Default path is local Ollama only.  A bounded Claude plan-CLI fallback can be
enabled for Phase 3 marker rendering with MARKER_JUDGE_CLAUDE_PLAN_FALLBACK=1.
This fallback must not use Anthropic/OpenAI API keys.
"""
from __future__ import annotations

import json
import logging
import os
import re
import subprocess
import time
from pathlib import Path
from typing import Optional

import httpx

from app.config import settings

log = logging.getLogger(__name__)

OLLAMA_BASE = (
    os.getenv("MARKER_JUDGE_OLLAMA_BASE")
    or settings.BUDDLE_BASE_URL
    or settings.OLLAMA_BASE_URL
    or "http://localhost:11434"
).rstrip("/")
MODEL_LOCAL = os.getenv("MARKER_JUDGE_MODEL") or settings.BUDDLE_MODEL or "gpt-oss:120b"
LOCAL_CALL_ATTEMPTS = int(os.getenv("MARKER_JUDGE_LOCAL_CALL_ATTEMPTS", "1"))
LOCAL_CALL_TIMEOUT_SECONDS = float(os.getenv("MARKER_JUDGE_LOCAL_CALL_TIMEOUT_SECONDS", "45"))
LOCAL_KEEP_ALIVE = os.getenv("MARKER_OLLAMA_KEEP_ALIVE", "12h")
TIMING_LOG = os.getenv("MARKER_TIMING_LOG")
AGREEMENT_FLOOR = 0.50
CLAUDE_PLAN_FALLBACK_ENABLED = os.getenv("MARKER_JUDGE_CLAUDE_PLAN_FALLBACK", "").strip().lower() in {"1", "true", "yes"}
CLAUDE_PLAN_MODEL = os.getenv("MARKER_JUDGE_CLAUDE_PLAN_MODEL", "sonnet")
CLAUDE_PLAN_MAX_CALLS = int(os.getenv("MARKER_JUDGE_CLAUDE_PLAN_MAX_CALLS", "250"))
CLAUDE_PLAN_TIMEOUT_SECONDS = int(os.getenv("MARKER_JUDGE_CLAUDE_PLAN_TIMEOUT_SECONDS", "60"))
CLAUDE_PLAN_THROTTLE_SECONDS = float(os.getenv("MARKER_JUDGE_CLAUDE_PLAN_THROTTLE_SECONDS", "1.5"))

_fallback_stats = {
    "local_success": 0,
    "local_fail": 0,
    "claude_plan_success": 0,
    "claude_plan_fail": 0,
    "claude_plan_timeout": 0,
    "claude_plan_calls": 0,
    "claude_plan_cap_hit": False,
}


def _timing_event(event: str, **payload) -> None:
    if not TIMING_LOG:
        return
    try:
        path = Path(TIMING_LOG)
        path.parent.mkdir(parents=True, exist_ok=True)
        with path.open("a", encoding="utf-8") as handle:
            handle.write(json.dumps({"stage": "judge", "event": event, **payload}, sort_keys=True) + "\n")
    except Exception:
        log.debug("judge timing log write failed", exc_info=True)

_SYSTEM = (
    "You are an astronomy content reviewer. Given a wiki claim and a candidate "
    "span extracted from a wiki page, independently assess how well the span "
    "conveys the claim. Output ONLY the JSON object, no prose, no markdown, no code fences."
)

_USER_TMPL = """\
CLAIM (trust_level={trust_level}):
{claim_text}

SPAN:
{span}

Return JSON:
{{
  "agreement_score": 0.0..1.0,
  "trust_alignment": "ok" | "mismatch"
}}
"""


def reset_fallback_stats() -> None:
    for key in _fallback_stats:
        _fallback_stats[key] = False if key == "claude_plan_cap_hit" else 0


def get_fallback_stats() -> dict:
    return dict(_fallback_stats)


def _extract_json(raw: str) -> dict:
    raw = raw.strip()
    try:
        return json.loads(raw)
    except Exception:
        pass
    fenced = re.search(r"```(?:json)?\s*(\{.*?\})\s*```", raw, re.DOTALL)
    if fenced:
        try:
            return json.loads(fenced.group(1))
        except Exception:
            pass
    stack: list[str] = []
    start = -1
    objects: list[str] = []
    for i, char in enumerate(raw):
        if char == "{":
            if not stack:
                start = i
            stack.append(char)
        elif char == "}":
            if stack:
                stack.pop()
                if not stack and start >= 0:
                    objects.append(raw[start : i + 1])
    for obj in objects:
        try:
            return json.loads(obj)
        except Exception:
            continue
    raise ValueError("No parseable JSON object in local marker judge response")


def _build_prompt(claim_text: str, trust_level: str, span: str) -> str:
    return _USER_TMPL.format(
        claim_text=claim_text,
        trust_level=trust_level,
        span=span,
    )


def _call_local(prompt: str) -> Optional[dict]:
    payload = {
        "model": MODEL_LOCAL,
        "messages": [
            {"role": "system", "content": _SYSTEM},
            {"role": "user", "content": prompt},
        ],
        "stream": False,
        "format": "json",
        "keep_alive": LOCAL_KEEP_ALIVE,
        "options": {
            "temperature": 0,
            "num_predict": 256,
        },
    }
    for attempt in range(1, LOCAL_CALL_ATTEMPTS + 1):
        if attempt > 1:
            time.sleep(2 ** (attempt - 1))
        started = time.perf_counter()
        try:
            response = httpx.post(
                f"{OLLAMA_BASE}/api/chat",
                json=payload,
                timeout=LOCAL_CALL_TIMEOUT_SECONDS,
            )
            response.raise_for_status()
            content = (response.json().get("message") or {}).get("content") or ""
            parsed = _extract_json(content)
            _timing_event(
                "local_call",
                model=MODEL_LOCAL,
                base=OLLAMA_BASE,
                attempt=attempt,
                ok=True,
                wall_ms=round((time.perf_counter() - started) * 1000, 3),
                prompt_chars=len(prompt),
            )
            return parsed
        except Exception as exc:
            _timing_event(
                "local_call",
                model=MODEL_LOCAL,
                base=OLLAMA_BASE,
                attempt=attempt,
                ok=False,
                wall_ms=round((time.perf_counter() - started) * 1000, 3),
                prompt_chars=len(prompt),
                error=type(exc).__name__,
            )
            log.warning(
                "marker judge local call failed attempt=%d/%d model=%s err=%s",
                attempt,
                LOCAL_CALL_ATTEMPTS,
                MODEL_LOCAL,
                exc,
            )
            if attempt == LOCAL_CALL_ATTEMPTS:
                return None
    return None


def _call_claude_plan(prompt: str) -> Optional[dict]:
    if not CLAUDE_PLAN_FALLBACK_ENABLED:
        return None
    if int(_fallback_stats["claude_plan_calls"]) >= CLAUDE_PLAN_MAX_CALLS:
        _fallback_stats["claude_plan_cap_hit"] = True
        log.warning("marker judge claude plan fallback cap hit max_calls=%d", CLAUDE_PLAN_MAX_CALLS)
        return None

    time.sleep(CLAUDE_PLAN_THROTTLE_SECONDS)
    full_prompt = (
        f"{_SYSTEM}\n\n"
        f"{prompt}\n\n"
        "Output ONLY the JSON object. Required keys: agreement_score, trust_alignment."
    )
    _fallback_stats["claude_plan_calls"] = int(_fallback_stats["claude_plan_calls"]) + 1
    try:
        proc = subprocess.run(
            ["claude", "-p", "--model", CLAUDE_PLAN_MODEL, full_prompt],
            cwd=str(settings.__class__.__module__ and os.getcwd()),
            text=True,
            capture_output=True,
            timeout=CLAUDE_PLAN_TIMEOUT_SECONDS,
            check=False,
            env={key: value for key, value in os.environ.items() if key not in {"NM_ANTHROPIC_API_KEY", "ANTHROPIC_API_KEY", "OPENAI_API_KEY"}},
        )
    except subprocess.TimeoutExpired:
        _fallback_stats["claude_plan_timeout"] = int(_fallback_stats["claude_plan_timeout"]) + 1
        log.warning("marker judge claude plan fallback timed out after %ss", CLAUDE_PLAN_TIMEOUT_SECONDS)
        return None
    except Exception as exc:
        _fallback_stats["claude_plan_fail"] = int(_fallback_stats["claude_plan_fail"]) + 1
        log.warning("marker judge claude plan fallback failed: %s", exc)
        return None

    if proc.returncode != 0:
        _fallback_stats["claude_plan_fail"] = int(_fallback_stats["claude_plan_fail"]) + 1
        log.warning("marker judge claude plan fallback rc=%s stderr=%s", proc.returncode, proc.stderr[:300])
        return None
    try:
        parsed = _extract_json(proc.stdout)
    except Exception as exc:
        _fallback_stats["claude_plan_fail"] = int(_fallback_stats["claude_plan_fail"]) + 1
        log.warning("marker judge claude plan fallback JSON parse failed: %s", exc)
        return None
    _fallback_stats["claude_plan_success"] = int(_fallback_stats["claude_plan_success"]) + 1
    return parsed


def judge_span(claim_text: str, trust_level: str, span: str) -> Optional[dict]:
    prompt = _build_prompt(claim_text, trust_level, span)
    result = _call_local(prompt)
    if result is not None:
        _fallback_stats["local_success"] = int(_fallback_stats["local_success"]) + 1
        return result

    _fallback_stats["local_fail"] = int(_fallback_stats["local_fail"]) + 1
    return _call_claude_plan(prompt)


def passes_judge(claim_text: str, trust_level: str, span: str) -> tuple[bool, float]:
    """Returns (passes, agreement_score). On error returns (False, 0.0)."""
    started = time.perf_counter()
    result = judge_span(claim_text, trust_level, span)
    if result is None:
        _timing_event("passes_judge", ok=False, wall_ms=round((time.perf_counter() - started) * 1000, 3), reason="no_result")
        return False, 0.0
    try:
        score = float(result.get("agreement_score", 0.0))
    except (TypeError, ValueError):
        _timing_event("passes_judge", ok=False, wall_ms=round((time.perf_counter() - started) * 1000, 3), reason="bad_score")
        return False, 0.0
    passed = score >= AGREEMENT_FLOOR
    _timing_event("passes_judge", ok=passed, wall_ms=round((time.perf_counter() - started) * 1000, 3), score=score)
    return passed, score
