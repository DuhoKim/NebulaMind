"""
Survey prose judge — uses AstroSage (astrosage-70b) to evaluate ProseEnrich proposals.

AstroSage is priority-claimed for surveys (astrosage:surveys_priority Redis flag).
On AstroSage error, Tera (qwen3.6:35b-a3b-nvfp4) is used as fallback.

judge_survey_prose() runs N=3 independent judgements and returns the median verdict.
"""

from __future__ import annotations

import json
import logging
import re
import statistics
from pathlib import Path
from typing import Optional

import httpx

log = logging.getLogger(__name__)

_OLLAMA_BASE = "http://localhost:11434"
_ASTROSAGE = "astrosage-70b"
_TERA_FALLBACK = "qwen3.6:35b-a3b-nvfp4"
_JUDGE_RUNS = 3
_ACCEPT_THRESHOLD = 7.0

PROMPTS_DIR = Path(__file__).parent / "prompts"


def _load_judge_prompt() -> str:
    p = PROMPTS_DIR / "surveys_judge_v1.md"
    if p.exists():
        return p.read_text()
    raise FileNotFoundError(f"Judge prompt not found: {p}")


def _ollama_chat(model: str, system: str, user: str, base_url: str = _OLLAMA_BASE) -> str:
    url = f"{base_url}/api/chat"
    payload = {
        "model": model,
        "messages": [
            {"role": "system", "content": system},
            {"role": "user", "content": user},
        ],
        "stream": False,
    }
    try:
        r = httpx.post(url, json=payload, timeout=300)
        r.raise_for_status()
        return r.json()["message"]["content"]
    except Exception as exc:
        log.warning("_ollama_chat(%s) error: %s", model, exc)
        return ""


def _parse_json_block(text: str) -> Optional[dict]:
    m = re.search(r"```(?:json)?\s*(\{.*?\})\s*```", text, re.DOTALL)
    if m:
        raw = m.group(1)
    else:
        m2 = re.search(r"\{.*\}", text, re.DOTALL)
        if not m2:
            return None
        raw = m2.group(0)
    try:
        return json.loads(raw)
    except json.JSONDecodeError:
        return None


def _band_program(band: Optional[str]) -> str:
    programs_dir = Path(__file__).parent / "programs"
    if band:
        slug = band.lower().replace("-", "_").replace(" ", "_")
        p = programs_dir / f"{slug}.md"
        if p.exists():
            return p.read_text()
    return (programs_dir / "program.default.md").read_text()


def _run_single_judge(
    system_prompt: str,
    survey: dict,
    field: str,
    current: str,
    proposed: str,
    model: str,
) -> Optional[dict]:
    band = survey.get("band")
    program = _band_program(band)

    user_content = f"""## CONTEXT
{json.dumps(survey, default=str)}

## BAND PROGRAM
{program}

## Field: {field}

## CURRENT
{current}

## PROPOSED
{proposed}"""

    raw = _ollama_chat(model, system_prompt, user_content)
    if not raw:
        return None
    return _parse_json_block(raw)


def judge_survey_prose(
    survey: dict,
    field: str,
    current: str,
    proposed: str,
) -> dict:
    """
    Run N=3 independent AstroSage judgements.
    Returns median composite verdict.

    Return dict keys:
      verdict: "accept" | "reject"
      composite: float
      preferred_text: str
      runs: int
      model_used: str
    """
    try:
        system_prompt = _load_judge_prompt()
    except FileNotFoundError as exc:
        log.error("judge prompt missing: %s", exc)
        return {
            "verdict": "reject",
            "composite": 0.0,
            "preferred_text": current,
            "runs": 0,
            "model_used": "none",
        }

    # Try AstroSage first; if it errors on the first run, fall back to Tera
    model = _ASTROSAGE
    results = []

    for i in range(_JUDGE_RUNS):
        r = _run_single_judge(system_prompt, survey, field, current, proposed, model)
        if r is None and i == 0:
            log.warning("AstroSage unavailable for judge, falling back to Tera")
            model = _TERA_FALLBACK
            r = _run_single_judge(system_prompt, survey, field, current, proposed, model)
        if r:
            results.append(r)

    if not results:
        return {
            "verdict": "reject",
            "composite": 0.0,
            "preferred_text": current,
            "runs": 0,
            "model_used": model,
        }

    composites = [float(r.get("composite", 0.0)) for r in results]
    median_composite = statistics.median(composites)

    # Pick the result closest to the median composite
    median_result = min(results, key=lambda r: abs(float(r.get("composite", 0.0)) - median_composite))

    verdict = "accept" if median_composite >= _ACCEPT_THRESHOLD else "reject"
    preferred = proposed if verdict == "accept" else current

    return {
        "verdict": verdict,
        "composite": round(median_composite, 2),
        "preferred_text": preferred,
        "runs": len(results),
        "model_used": model,
        "accuracy": median_result.get("accuracy"),
        "utility": median_result.get("utility"),
        "conciseness": median_result.get("conciseness"),
        "band_compliance": median_result.get("band_compliance", "ok"),
        "band_notes": median_result.get("band_notes", "none"),
        "verdict_reason": median_result.get("verdict_reason", ""),
    }
