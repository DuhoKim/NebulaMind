"""
Survey edit proposers — generate candidate edits for each edit type.

Each proposer returns a dict with keys:
  field: str          — database column to update
  proposed_value: str — new value
  source_url: str     — evidence URL (may be empty string)
  confidence: float   — 0..1
  edit_type: str      — matches the constants in tasks.py

Returns None if no credible proposal can be generated.
"""

from __future__ import annotations

import json
import logging
import re
import time
from pathlib import Path
from typing import Optional

import httpx

log = logging.getLogger(__name__)

# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

_OLLAMA_BASE = "http://localhost:11434"

PROGRAMS_DIR = Path(__file__).parent / "programs"


def _band_program(band: Optional[str]) -> str:
    if not band:
        return (PROGRAMS_DIR / "program.default.md").read_text()
    slug = band.lower().replace("-", "_").replace(" ", "_")
    p = PROGRAMS_DIR / f"{slug}.md"
    if p.exists():
        return p.read_text()
    return (PROGRAMS_DIR / "program.default.md").read_text()


def _ollama_chat(model: str, prompt: str, base_url: str = _OLLAMA_BASE) -> str:
    url = f"{base_url}/api/chat"
    payload = {
        "model": model,
        "messages": [{"role": "user", "content": prompt}],
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


# ---------------------------------------------------------------------------
# URL-health proposer
# ---------------------------------------------------------------------------

def propose_urlhealth(survey: dict, check_result: dict) -> Optional[dict]:
    """
    When a URL check finds a bad archive or mission URL, propose a replacement
    by asking Blanc to suggest an updated URL, then return a LOW-stakes proposal.

    check_result keys: archive_ok (bool), mission_ok (bool), tested_url (str)
    """
    field = "archive_url" if not check_result.get("archive_ok") else "mission_url"
    current_url = survey.get(field, "")
    survey_name = survey.get("name", survey.get("slug", "unknown"))

    prompt = f"""You are helping maintain the NebulaMind Surveys Directory.

Survey: {survey_name}
Field: {field}
Current URL (returning 4xx/5xx): {current_url}

Please suggest the single most likely correct replacement URL for this survey's
{field}. Search your knowledge for the official website or data archive of this
survey. Respond with JSON only:

```json
{{"proposed_url": "<full https URL>", "confidence": <0.0-1.0>, "reasoning": "<one sentence>"}}
```"""

    raw = _ollama_chat("llama3.3:70b", prompt)
    parsed = _parse_json_block(raw)
    if not parsed or not parsed.get("proposed_url"):
        return None

    confidence = float(parsed.get("confidence", 0.5))
    if confidence < 0.5:
        return None

    return {
        "field": field,
        "proposed_value": parsed["proposed_url"].strip(),
        "source_url": current_url,
        "confidence": confidence,
        "edit_type": "urlhealth",
        "stake": "low",
    }


# ---------------------------------------------------------------------------
# Field-patch proposer (from news / DR headlines)
# ---------------------------------------------------------------------------

_BLANC_FIELDPATCH_PROMPT = """\
You are an astronomy knowledge editor for the NebulaMind Surveys Directory.

Survey metadata:
{survey_json}

A news headline suggests an update:
Headline: {headline}
Source URL: {source_url}

Identify the single most important field to update based on this headline.
Eligible fields: current_data_release, status, description, science_goals.

Rules:
- Only propose a change if you are highly confident the headline refers to THIS survey.
- For current_data_release: extract the exact DR string (e.g. "DR3", "EDR", "Q1").
- For status: only use values: planning, active, completed, decommissioned.
- Do NOT change description or science_goals unless the headline reveals a major
  mission pivot or name change.

Respond with JSON only:
```json
{{"field": "<field_name>", "proposed_value": "<new value>", "confidence": <0.0-1.0>, "reasoning": "<one sentence>"}}
```

If no confident update is possible, respond:
```json
{{"field": null, "proposed_value": null, "confidence": 0.0, "reasoning": "no confident match"}}
```"""


def propose_fieldpatch(survey: dict, headline: str, source_url: str) -> Optional[dict]:
    prompt = _BLANC_FIELDPATCH_PROMPT.format(
        survey_json=json.dumps(survey, default=str),
        headline=headline,
        source_url=source_url,
    )
    raw = _ollama_chat("llama3.3:70b", prompt)
    parsed = _parse_json_block(raw)
    if not parsed or not parsed.get("field"):
        return None

    confidence = float(parsed.get("confidence", 0.0))
    if confidence < 0.55:
        return None

    field = parsed["field"]
    stake = "high" if field in ("current_data_release", "status") else "low"

    return {
        "field": field,
        "proposed_value": str(parsed["proposed_value"]).strip(),
        "source_url": source_url,
        "confidence": confidence,
        "edit_type": "fieldpatch",
        "stake": stake,
    }


# ---------------------------------------------------------------------------
# DR-refresh proposer
# ---------------------------------------------------------------------------

_BLANC_DRREFRESH_PROMPT = """\
You are an astronomy knowledge editor for the NebulaMind Surveys Directory.

Survey metadata (current):
{survey_json}

A news item suggests a new data release for this survey:
Headline: {headline}
Source URL: {source_url}

Extract the exact data release string referenced in this news item.
Use the format actually used by the survey team (e.g. "DR3", "PDR2", "Q1", "EDR").

Respond with JSON only:
```json
{{"dr_string": "<extracted DR string>", "confidence": <0.0-1.0>, "reasoning": "<one sentence>"}}
```"""


def propose_drrefresh(survey: dict, headline: str, source_url: str) -> Optional[dict]:
    prompt = _BLANC_DRREFRESH_PROMPT.format(
        survey_json=json.dumps(survey, default=str),
        headline=headline,
        source_url=source_url,
    )
    raw = _ollama_chat("llama3.3:70b", prompt)
    parsed = _parse_json_block(raw)
    if not parsed or not parsed.get("dr_string"):
        return None

    confidence = float(parsed.get("confidence", 0.0))
    if confidence < 0.60:
        return None

    return {
        "field": "current_data_release",
        "proposed_value": str(parsed["dr_string"]).strip(),
        "source_url": source_url,
        "confidence": confidence,
        "edit_type": "drrefresh",
        "stake": "high",
    }


# ---------------------------------------------------------------------------
# Prose-enrich proposer (Blanc drafter)
# ---------------------------------------------------------------------------

_BLANC_PROSEENRICH_PROMPT = """\
You are Blanc, an astronomy prose writer for the NebulaMind Surveys Directory.

Your task: rewrite or improve a single field for a survey entry.

Survey metadata:
{survey_json}

Band editorial program:
{band_program}

Field to improve: {field}
Current value:
{current_value}

Write an improved version of this field. Follow the band program guidelines.
Be accurate, specific, and concise. Do not invent facts not present in the metadata.

Respond with the improved text only — no explanation, no preamble.
"""


def propose_proseenrich(survey: dict, field: str) -> Optional[dict]:
    current_value = survey.get(field, "")
    if not current_value or len(str(current_value).strip()) < 10:
        return None

    band = survey.get("band")
    program = _band_program(band)

    prompt = _BLANC_PROSEENRICH_PROMPT.format(
        survey_json=json.dumps(survey, default=str),
        band_program=program,
        field=field,
        current_value=current_value,
    )
    proposed = _ollama_chat("llama3.3:70b", prompt).strip()
    if not proposed or proposed == current_value.strip():
        return None

    return {
        "field": field,
        "proposed_value": proposed,
        "source_url": "",
        "confidence": 0.7,
        "edit_type": "proseenrich",
        "stake": "low",
    }
