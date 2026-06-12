"""
Q3 gap_type backfill for galaxy-evolution (page_id=57).
Idempotent: skips ideas that already have gap_type set.

For each unclassified idea:
  - Call Atom-7B to classify gap_type (§6.5 prompt with anchor_claim_text)
  - confidence >= 0.6 → set gap_type + gap_type_source='atom_backfill'
  - confidence <  0.6 → set status='idea_review_queue'

Usage:
    python3 scripts/backfill_gap_type_q3.py [--dry-run]
"""

from __future__ import annotations

import argparse
import json
import logging
import re
import sys
import time
from typing import Optional

import httpx
import psycopg2
import psycopg2.extras

logging.basicConfig(level=logging.INFO, format="%(asctime)s %(levelname)s %(message)s")
log = logging.getLogger("gap_type_backfill")

DATABASE_URL = "postgresql://nebula:nebula@localhost:5432/nebulamind"
OLLAMA_BASE  = "http://localhost:11434"
MODEL_ATOM   = "vanta-research/atom-astronomy-7b:latest"
PAGE_ID      = 57
CONFIDENCE_THRESHOLD = 0.6
VALID_GAP_TYPES = {"gap", "tension", "bridge", "frontier", "synergy"}

# §6.5 prompt — matches design doc exactly
GAP_TYPE_PROMPT = """\
Classify this astrophysics research idea into exactly one gap_type bucket:
  - gap       : addresses a topic mentioned shallowly or not at all
  - tension   : addresses contradiction between two existing claims
  - bridge    : connects two sections never linked explicitly
  - frontier  : tackles an open / known-unknown problem
  - synergy   : combines specific survey datasets to test an existing claim

Return JSON: {{"gap_type": "<one of the five>", "confidence": float 0-1, "reason": "<≤20 words>"}}.

IDEA:
  question:     {question}
  why_now:      {why_now}
  approach:     {approach}
  survey_combo: {survey_combo}
  anchor_claim: {anchor_claim_text}"""


def _ollama_chat(prompt: str) -> str:
    url = f"{OLLAMA_BASE}/api/chat"
    payload = {
        "model": MODEL_ATOM,
        "messages": [{"role": "user", "content": prompt}],
        "stream": False,
    }
    try:
        r = httpx.post(url, json=payload, timeout=120)
        r.raise_for_status()
        return r.json()["message"]["content"]
    except Exception as exc:
        log.warning("Atom call failed: %s", exc)
        return ""


def _parse_json_block(text: str) -> Optional[dict]:
    m = re.search(r"```(?:json)?\s*(\{.*?\})\s*```", text, re.DOTALL)
    raw = m.group(1) if m else None
    if not raw:
        m2 = re.search(r"\{.*\}", text, re.DOTALL)
        raw = m2.group(0) if m2 else None
    if not raw:
        return None
    try:
        return json.loads(raw)
    except json.JSONDecodeError:
        return None


def classify_idea(idea: dict) -> tuple[Optional[str], float, str]:
    """Returns (gap_type | None, confidence, reasoning)."""
    prompt = GAP_TYPE_PROMPT.format(
        question=idea["question"][:300],
        why_now=(idea["why_now"] or "")[:200],
        approach=(idea["approach"] or "")[:200],
        survey_combo=(idea["survey_combo"] or ""),
        anchor_claim_text=(idea["anchor_claim_text"] or "(none)"),
    )
    raw = _ollama_chat(prompt)
    if not raw:
        return None, 0.0, "atom_call_failed"

    parsed = _parse_json_block(raw)
    if not parsed:
        return None, 0.0, "parse_failed"

    gap_type = parsed.get("gap_type", "").lower().strip()
    if gap_type not in VALID_GAP_TYPES:
        return None, 0.0, f"invalid_gap_type:{gap_type}"

    confidence = float(parsed.get("confidence", 0.0))
    reasoning  = str(parsed.get("reason", ""))
    return gap_type, confidence, reasoning


def run_backfill(dry_run: bool = False):
    conn = psycopg2.connect(DATABASE_URL)
    conn.autocommit = False

    with conn.cursor(cursor_factory=psycopg2.extras.RealDictCursor) as cur:
        cur.execute("""
            SELECT ri.id, ri.question, ri.why_now, ri.approach, ri.survey_combo,
                   ri.status, COALESCE(c.text, '') AS anchor_claim_text
            FROM research_ideas ri
            LEFT JOIN claims c ON c.id = ri.claim_id
            WHERE ri.page_id = %s
              AND ri.gap_type IS NULL
              AND ri.status NOT IN ('superseded', 'rejected', 'stale')
            ORDER BY ri.id
        """, (PAGE_ID,))
        ideas = cur.fetchall()
    # Commit after the read so we don't hold an open transaction while calling Atom.
    conn.commit()

    log.info("Found %d unclassified ideas to process for page_id=%d", len(ideas), PAGE_ID)

    typed_count  = 0
    queued_count = 0
    failed_count = 0

    for idea in ideas:
        idea_id = idea["id"]
        log.info("Classifying idea #%d: %s...", idea_id, idea["question"][:80])

        gap_type, confidence, reasoning = classify_idea(idea)

        log.info("  → gap_type=%s  confidence=%.2f  reason=%s", gap_type, confidence, reasoning[:80])

        if dry_run:
            if gap_type and confidence >= CONFIDENCE_THRESHOLD:
                typed_count += 1
            elif gap_type:
                queued_count += 1
            else:
                failed_count += 1
            time.sleep(0.1)
            continue

        with conn.cursor() as cur:
            if gap_type and confidence >= CONFIDENCE_THRESHOLD:
                cur.execute("""
                    UPDATE research_ideas
                       SET gap_type        = %s,
                           gap_type_source = 'atom_backfill',
                           updated_at      = NOW()
                     WHERE id = %s
                """, (gap_type, idea_id))
                typed_count += 1
            elif gap_type:
                # Low confidence: write gap_type (per §6.5) AND flag for review
                cur.execute("""
                    UPDATE research_ideas
                       SET gap_type        = %s,
                           gap_type_source = 'atom_backfill',
                           status          = 'idea_review_queue',
                           updated_at      = NOW()
                     WHERE id = %s
                """, (gap_type, idea_id))
                queued_count += 1
            else:
                failed_count += 1
                log.warning("  → no classification for idea #%d, leaving NULL", idea_id)

        conn.commit()
        time.sleep(0.3)

    conn.close()

    summary = {
        "total":   len(ideas),
        "typed":   typed_count,
        "queued_for_review": queued_count,
        "failed":  failed_count,
        "dry_run": dry_run,
    }
    log.info("Backfill complete: %s", summary)
    return summary


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--dry-run", action="store_true")
    args = parser.parse_args()
    result = run_backfill(dry_run=args.dry_run)
    print(json.dumps(result, indent=2))
