"""Stage C: local Ollama claim-to-span alignment.

The marker overlay must not depend on paid alignment providers.  This module
uses only the local Ollama/Buddle lane and fails closed if JSON cannot be
parsed.
"""
from __future__ import annotations

import json
import logging
import os
import re
import time
from pathlib import Path
from typing import Optional

import httpx

from app.config import settings

log = logging.getLogger(__name__)

OLLAMA_BASE = (
    os.getenv("MARKER_ALIGNER_OLLAMA_BASE")
    or settings.BUDDLE_BASE_URL
    or settings.OLLAMA_BASE_URL
    or "http://localhost:11434"
).rstrip("/")
MODEL_LOCAL = os.getenv("MARKER_ALIGNER_MODEL") or settings.BUDDLE_MODEL or "gpt-oss:120b"
LOCAL_CALL_ATTEMPTS = int(os.getenv("MARKER_ALIGNER_LOCAL_CALL_ATTEMPTS", "1"))
LOCAL_CALL_TIMEOUT_SECONDS = float(os.getenv("MARKER_ALIGNER_LOCAL_CALL_TIMEOUT_SECONDS", "45"))
LOCAL_KEEP_ALIVE = os.getenv("MARKER_OLLAMA_KEEP_ALIVE", "12h")
TIMING_LOG = os.getenv("MARKER_TIMING_LOG")
PREFILTER_ENABLED = os.getenv("MARKER_ALIGNER_PREFILTER", "1").strip().lower() not in {"0", "false", "no"}
PREFILTER_FLOOR = float(os.getenv("MARKER_ALIGNER_PREFILTER_FLOOR", "0.45"))
TIER2_ENABLED = os.getenv("MARKER_ALIGNER_TIER2_ENABLED", "0").strip().lower() in {"1", "true", "yes"}
TIER2_NEAR_MISS_FLOOR = float(os.getenv("MARKER_ALIGNER_TIER2_NEAR_MISS_FLOOR", "0.60"))

CONFIDENCE_GATE = 0.50

# Up to 60 candidates: A-Z then AA-BH
_SINGLE = [chr(i) for i in range(ord("A"), ord("Z") + 1)]
_DOUBLE = [f"A{chr(i)}" for i in range(ord("A"), ord("Z") + 1)] + [f"B{chr(i)}" for i in range(ord("A"), ord("I") + 1)]
LETTERS = _SINGLE + _DOUBLE


def _timing_event(event: str, **payload) -> None:
    if not TIMING_LOG:
        return
    try:
        path = Path(TIMING_LOG)
        path.parent.mkdir(parents=True, exist_ok=True)
        with path.open("a", encoding="utf-8") as handle:
            handle.write(json.dumps({"stage": "aligner", "event": event, **payload}, sort_keys=True) + "\n")
    except Exception:
        log.debug("aligner timing log write failed", exc_info=True)

_SYSTEM = (
    "You are aligning a wiki claim to its supporting sentence in a wiki page. "
    "Given a claim and candidate sentences from the same section, decide "
    "which sentence, if any, most directly asserts the claim. Then identify the "
    "smallest contiguous span within that sentence that conveys the claim. "
    "Return strict JSON only."
)

_USER_TMPL = """\
SECTION: {section_title}

CLAIM (id={claim_id}, trust_level={trust_level}):
{claim_text}

CANDIDATES:
{candidates_block}

Return JSON:
{{
  "chosen": "<letter from the list above>" | "none",
  "span_in_chosen": "<exact verbatim substring of the chosen sentence>",
  "confidence": 0.0..1.0,
  "reason": "<one short clause>"
}}

Rules:
- "span_in_chosen" must be a verbatim substring of the chosen candidate.
- Prefer the smallest span that still conveys the claim.
- Choose "none" if no candidate directly asserts the claim.
- Do NOT span across markdown markup ([..](..), **..**, `..`).
"""

_PREC_SYS = (
    "You are matching a claim to a candidate sentence from a wiki page. "
    "Match ONLY if the sentence makes the SAME assertion: same subject and same predicate or conclusion; paraphrase is OK. "
    "Same topic but different predicate, mechanism, or object means none. "
    "Return strict JSON only."
)

_PREC_USER_TMPL = """\
CLAIM (id={claim_id}, trust_level={trust_level}):
{claim_text}

CANDIDATES:
{candidates_block}

Return JSON:
{{
  "chosen": "<letter from the list above>" | "none",
  "confidence": 0.0..1.0,
  "reason": "<one short clause explaining the predicate match or failure>"
}}
"""


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
    raise ValueError("No parseable JSON object in local marker model response")


def _call_local_json(prompt: str, *, system: str, max_tokens: int) -> Optional[dict]:
    payload = {
        "model": MODEL_LOCAL,
        "messages": [
            {"role": "system", "content": system},
            {"role": "user", "content": prompt},
        ],
        "stream": False,
        "format": "json",
        "keep_alive": LOCAL_KEEP_ALIVE,
        "options": {
            "temperature": 0,
            "num_predict": max_tokens,
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
                "local_json_call",
                model=MODEL_LOCAL,
                base=OLLAMA_BASE,
                attempt=attempt,
                ok=True,
                wall_ms=round((time.perf_counter() - started) * 1000, 3),
                prompt_chars=len(prompt),
                max_tokens=max_tokens,
            )
            return parsed
        except Exception as exc:
            _timing_event(
                "local_json_call",
                model=MODEL_LOCAL,
                base=OLLAMA_BASE,
                attempt=attempt,
                ok=False,
                wall_ms=round((time.perf_counter() - started) * 1000, 3),
                prompt_chars=len(prompt),
                max_tokens=max_tokens,
                error=type(exc).__name__,
            )
            log.warning(
                "marker aligner local call failed attempt=%d/%d model=%s err=%s",
                attempt,
                LOCAL_CALL_ATTEMPTS,
                MODEL_LOCAL,
                exc,
            )
            if attempt == LOCAL_CALL_ATTEMPTS:
                return None
    return None


def align_claim(
    claim_id: int,
    claim_text: str,
    trust_level: str,
    section_title: str,
    candidates: list[str],
) -> Optional[dict]:
    started = time.perf_counter()
    if not candidates:
        _timing_event("claim_align", claim_id=claim_id, candidate_count=0, ok=False, wall_ms=0.0, reason="no_candidates")
        return None

    letters = LETTERS[: len(candidates)]
    cand_block = "\n".join(f"[{letter}] {sentence}" for letter, sentence in zip(letters, candidates))
    prompt = _USER_TMPL.format(
        section_title=section_title,
        claim_id=claim_id,
        trust_level=trust_level,
        claim_text=claim_text,
        candidates_block=cand_block,
    )

    result = _call_local_json(prompt, system=_SYSTEM, max_tokens=1024)
    if result is None or result.get("chosen") == "none":
        _timing_event(
            "claim_align",
            claim_id=claim_id,
            candidate_count=len(candidates),
            ok=False,
            wall_ms=round((time.perf_counter() - started) * 1000, 3),
            reason="none",
        )
        return None

    chosen_letter = result.get("chosen", "none")
    if chosen_letter not in letters:
        _timing_event(
            "claim_align",
            claim_id=claim_id,
            candidate_count=len(candidates),
            ok=False,
            wall_ms=round((time.perf_counter() - started) * 1000, 3),
            reason="bad_letter",
        )
        return None

    chosen_idx = letters.index(chosen_letter)
    chosen_sentence = candidates[chosen_idx]
    span = (result.get("span_in_chosen") or "").strip()

    try:
        confidence = float(result.get("confidence", 0.0))
    except (TypeError, ValueError):
        _timing_event(
            "claim_align",
            claim_id=claim_id,
            candidate_count=len(candidates),
            ok=False,
            wall_ms=round((time.perf_counter() - started) * 1000, 3),
            reason="bad_confidence",
        )
        return None
    if confidence < CONFIDENCE_GATE:
        _timing_event(
            "claim_align",
            claim_id=claim_id,
            candidate_count=len(candidates),
            ok=False,
            wall_ms=round((time.perf_counter() - started) * 1000, 3),
            reason="low_confidence",
            confidence=confidence,
        )
        return None

    match_type = "verbatim"
    if not span or span not in chosen_sentence:
        log.warning("aligner: claim_id=%d local span not substring; using whole sentence", claim_id)
        span = chosen_sentence.strip()
        match_type = "sentence"

    payload = {
        "chosen_sentence": chosen_sentence,
        "span": span,
        "confidence": confidence,
        "model_used": MODEL_LOCAL,
        "reason": result.get("reason", ""),
        "match_type": match_type,
    }
    _timing_event(
        "claim_align",
        claim_id=claim_id,
        candidate_count=len(candidates),
        ok=True,
        wall_ms=round((time.perf_counter() - started) * 1000, 3),
        confidence=confidence,
        match_type=match_type,
    )
    return payload


def align_claim_multipass(
    claim_id: int,
    claim_text: str,
    trust_level: str,
    section_title: str,
    section_candidates: list[str],
    all_sentences_with_sections: list[tuple[str, str]],
) -> Optional[dict]:
    """Tier 1 same-section match with cheap prefilter, then optional gated Tier 2.

    The production default is bounded to at most one local LLM call per claim.
    Set MARKER_ALIGNER_PREFILTER=0 and MARKER_ALIGNER_TIER2_ENABLED=1 for the
    full-LLM control path used in diagnostics.
    """
    from app.agent_loop.marker_embed.embed_index import rank_candidates

    started = time.perf_counter()
    section_rank_started = time.perf_counter()
    section_ranked = rank_candidates(
        claim_text,
        section_candidates,
        top_k=min(20, len(section_candidates)),
        cosine_floor=0.0,
    )
    section_top_score = float(section_ranked[0][1]) if section_ranked else 0.0
    _timing_event(
        "tier1_prefilter",
        claim_id=claim_id,
        enabled=PREFILTER_ENABLED,
        floor=PREFILTER_FLOOR,
        top_score=section_top_score,
        candidate_count=len(section_candidates),
        ranked_count=len(section_ranked),
        wall_ms=round((time.perf_counter() - section_rank_started) * 1000, 3),
    )
    if PREFILTER_ENABLED and section_top_score < PREFILTER_FLOOR:
        _timing_event(
            "claim_multipass",
            claim_id=claim_id,
            tier="prefilter",
            ok=False,
            wall_ms=round((time.perf_counter() - started) * 1000, 3),
            reason="below_similarity_floor",
            top_score=section_top_score,
            floor=PREFILTER_FLOOR,
        )
        return None

    tier1 = align_claim(claim_id, claim_text, trust_level, section_title, section_candidates)
    if tier1 is not None:
        tier1["chosen_section"] = section_title
        _timing_event(
            "claim_multipass",
            claim_id=claim_id,
            tier="tier1",
            ok=True,
            wall_ms=round((time.perf_counter() - started) * 1000, 3),
        )
        return tier1

    if not TIER2_ENABLED:
        _timing_event(
            "claim_multipass",
            claim_id=claim_id,
            tier="tier2",
            ok=False,
            wall_ms=round((time.perf_counter() - started) * 1000, 3),
            reason="tier2_disabled",
            top_score=section_top_score,
        )
        return None

    if PREFILTER_ENABLED and section_top_score < TIER2_NEAR_MISS_FLOOR:
        _timing_event(
            "claim_multipass",
            claim_id=claim_id,
            tier="tier2",
            ok=False,
            wall_ms=round((time.perf_counter() - started) * 1000, 3),
            reason="tier2_below_near_miss_floor",
            top_score=section_top_score,
            floor=TIER2_NEAR_MISS_FLOOR,
        )
        return None

    rank_started = time.perf_counter()
    all_sents = [sentence for sentence, _section in all_sentences_with_sections]
    ranked = rank_candidates(claim_text, all_sents, top_k=20, cosine_floor=0.45)
    _timing_event(
        "tier2_rank_candidates",
        claim_id=claim_id,
        sentence_count=len(all_sents),
        returned=len(ranked),
        wall_ms=round((time.perf_counter() - rank_started) * 1000, 3),
    )
    if not ranked:
        _timing_event(
            "claim_multipass",
            claim_id=claim_id,
            tier="tier2",
            ok=False,
            wall_ms=round((time.perf_counter() - started) * 1000, 3),
            reason="no_ranked",
        )
        return None

    top_sents = [sentence for sentence, _score in ranked]
    sent_to_sec = {sentence: section for sentence, section in all_sentences_with_sections}
    letters = LETTERS[: len(top_sents)]
    cand_block = "\n".join(f"[{letter}] {sentence}" for letter, sentence in zip(letters, top_sents))
    prompt = _PREC_USER_TMPL.format(
        claim_id=claim_id,
        trust_level=trust_level,
        claim_text=claim_text,
        candidates_block=cand_block,
    )

    result = _call_local_json(prompt, system=_PREC_SYS, max_tokens=1024)
    if result is None or result.get("chosen") == "none":
        _timing_event(
            "claim_multipass",
            claim_id=claim_id,
            tier="tier2",
            ok=False,
            wall_ms=round((time.perf_counter() - started) * 1000, 3),
            reason="none",
        )
        return None

    chosen_letter = result.get("chosen", "none")
    if chosen_letter not in letters:
        _timing_event(
            "claim_multipass",
            claim_id=claim_id,
            tier="tier2",
            ok=False,
            wall_ms=round((time.perf_counter() - started) * 1000, 3),
            reason="bad_letter",
        )
        return None

    try:
        confidence = float(result.get("confidence", 0.0))
    except (TypeError, ValueError):
        _timing_event(
            "claim_multipass",
            claim_id=claim_id,
            tier="tier2",
            ok=False,
            wall_ms=round((time.perf_counter() - started) * 1000, 3),
            reason="bad_confidence",
        )
        return None
    if confidence < 0.60:
        _timing_event(
            "claim_multipass",
            claim_id=claim_id,
            tier="tier2",
            ok=False,
            wall_ms=round((time.perf_counter() - started) * 1000, 3),
            reason="low_confidence",
            confidence=confidence,
        )
        return None

    chosen_sentence = top_sents[letters.index(chosen_letter)]
    payload = {
        "chosen_sentence": chosen_sentence,
        "span": chosen_sentence.strip(),
        "confidence": confidence,
        "model_used": MODEL_LOCAL,
        "reason": result.get("reason", ""),
        "match_type": "sentence",
        "chosen_section": sent_to_sec[chosen_sentence],
    }
    _timing_event(
        "claim_multipass",
        claim_id=claim_id,
        tier="tier2",
        ok=True,
        wall_ms=round((time.perf_counter() - started) * 1000, 3),
        confidence=confidence,
    )
    return payload
