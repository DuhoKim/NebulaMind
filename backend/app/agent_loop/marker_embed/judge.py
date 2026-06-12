"""Stage D: Claude Sonnet independent veto judge.

Claude re-scores each (claim_text, span) pair without seeing the aligner
reasoning. Agreement score < 0.6 drops the injection.
"""
import json
import logging
import os
import re
import signal
import threading
from typing import Optional

import anthropic

log = logging.getLogger(__name__)

from app.config import settings as _nm_settings
_ANTHROPIC_KEY = _nm_settings.ANTHROPIC_API_KEY
_claude = anthropic.Anthropic(api_key=_ANTHROPIC_KEY) if _ANTHROPIC_KEY else None
MODEL_CLAUDE = "claude-sonnet-4-6"
AGREEMENT_FLOOR = 0.50
CLAUDE_CALL_TIMEOUT_SECONDS = 95

_SYSTEM = (
    "You are an astronomy content reviewer. Given a wiki claim and a candidate "
    "span extracted from a wiki page, independently assess how well the span "
    "conveys the claim. Output strict JSON only."
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


def judge_span(claim_text: str, trust_level: str, span: str) -> Optional[dict]:
    prompt = _USER_TMPL.format(
        claim_text=claim_text,
        trust_level=trust_level,
        span=span,
    )
    if _claude is None:
        log.error("judge: Anthropic client not initialized")
        return None
    import time; time.sleep(0.3)
    try:
        msg = _run_with_alarm(
            lambda: _claude.messages.create(
                model=MODEL_CLAUDE,
                max_tokens=80,
                system=_SYSTEM,
                messages=[{"role": "user", "content": prompt}],
                timeout=90.0,
            ),
            CLAUDE_CALL_TIMEOUT_SECONDS,
        )
        raw = msg.content[0].text.strip()

        def robust_extract(text):
            import json, re
            m = re.search(r"```(?:json)?\s*(\{.*?\})\s*```", text, re.DOTALL)
            if m:
                try:
                    return json.loads(m.group(1))
                except:
                    pass
            objs = []
            stack = []
            start = -1
            for i, c in enumerate(text):
                if c == '{':
                    if not stack: start = i
                    stack.append(c)
                elif c == '}':
                    if stack:
                        stack.pop()
                        if not stack:
                            objs.append(text[start:i+1])
            for obj_str in objs:
                try:
                    return json.loads(obj_str)
                except:
                    continue
            return json.loads(text)
        
        return robust_extract(raw)

    except Exception as exc:
        log.warning("judge: Claude call failed err=%s", exc)
        return None


def _run_with_alarm(fn, seconds: int):
    if threading.current_thread() is not threading.main_thread() or not hasattr(signal, "SIGALRM"):
        return fn()

    def _timeout(_signum, _frame):
        raise TimeoutError(f"Claude judge call timed out after {seconds}s")

    previous = signal.getsignal(signal.SIGALRM)
    signal.signal(signal.SIGALRM, _timeout)
    signal.setitimer(signal.ITIMER_REAL, seconds)
    try:
        return fn()
    finally:
        signal.setitimer(signal.ITIMER_REAL, 0)
        signal.signal(signal.SIGALRM, previous)


def passes_judge(claim_text: str, trust_level: str, span: str) -> tuple[bool, float]:
    """Returns (passes, agreement_score). On error returns (False, 0.0)."""
    result = judge_span(claim_text, trust_level, span)
    if result is None:
        return False, 0.0
    score = float(result.get("agreement_score", 0.0))
    return score >= AGREEMENT_FLOOR, score
