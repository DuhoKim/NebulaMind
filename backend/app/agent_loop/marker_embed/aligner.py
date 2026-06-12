"""Stage C: LLM claim-to-span alignment.

Primary: Claude Sonnet (Anthropic API) — local Ollama too saturated.
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

# Load API key via app.config (.env is read by pydantic-settings with env_prefix=NM_).
from app.config import settings as _nm_settings
_ANTHROPIC_KEY = _nm_settings.ANTHROPIC_API_KEY
_claude = anthropic.Anthropic(api_key=_ANTHROPIC_KEY) if _ANTHROPIC_KEY else None
MODEL_CLAUDE = "claude-sonnet-4-6"
CLAUDE_CALL_TIMEOUT_SECONDS = 95

CONFIDENCE_GATE = 0.50  # lowered from 0.7 — Opus rewrite shifted phrasing; judge stage vetoes bad matches
ASTROSAGE_FALLBACK_THRESHOLD = 0.6

_DOMAIN_TOKEN_RE = re.compile(
    r"\b(?:JWST|ALMA|SDSS|MaNGA|CANDELS|HSC|Euclid|DESI|VLA|Planck|Herschel|"
    r"Chandra|XMM|Spitzer|2dFGRS|GAMA|zCOSMOS|COSMOS|MUSE|SINFONI|"
    r"[A-Z][a-z]+ et al\.\s+\d{4}|[A-Z][a-z]+ & [A-Z][a-z]+ \d{4})\b"
)

# Up to 60 candidates: A-Z then AA-BH
_SINGLE = [chr(i) for i in range(ord('A'), ord('Z') + 1)]
_DOUBLE = [f"A{chr(i)}" for i in range(ord('A'), ord('Z') + 1)] + [f"B{chr(i)}" for i in range(ord('A'), ord('I') + 1)]
LETTERS = _SINGLE + _DOUBLE  # 60 total

_SYSTEM = (
    "You are aligning a wiki claim to its supporting sentence in a wiki page. "
    "Given a claim and candidate sentences from the same section, decide "
    "which sentence (if any) most directly asserts the claim. Then identify the "
    "smallest contiguous span within that sentence that conveys the claim. "
    "Output strict JSON only — no prose, no markdown fences."
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
- Do NOT span across markdown markup ([..](..),  **..**, `..`).
"""


def _call_claude(prompt: str) -> Optional[dict]:
    """Call Claude Sonnet for alignment. Fast, reliable JSON output."""
    import time
    if _claude is None:
        log.error("aligner: Anthropic client not initialized (missing API key)")
        return None
    time.sleep(0.3)  # avoid rate limit with rapid-fire large prompts
    try:
        msg = _run_with_alarm(
            lambda: _claude.messages.create(
                model=MODEL_CLAUDE,
                max_tokens=1024,  # larger prompt with up to 60 sentences
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
        log.warning("aligner: Claude call failed err=%s", exc)
        return None


def _run_with_alarm(fn, seconds: int):
    """Bound blocking SDK reads during manual foreground runs.

    Celery uses worker threads, where SIGALRM cannot be installed; those paths
    still rely on the SDK timeout. Manual repair runs execute on the main
    thread, so this prevents one stalled HTTPS read from blocking the whole pass.
    """
    if threading.current_thread() is not threading.main_thread() or not hasattr(signal, "SIGALRM"):
        return fn()

    def _timeout(_signum, _frame):
        raise TimeoutError(f"Claude call timed out after {seconds}s")

    previous = signal.getsignal(signal.SIGALRM)
    signal.signal(signal.SIGALRM, _timeout)
    signal.setitimer(signal.ITIMER_REAL, seconds)
    try:
        return fn()
    finally:
        signal.setitimer(signal.ITIMER_REAL, 0)
        signal.signal(signal.SIGALRM, previous)


def align_claim(
    claim_id: int,
    claim_text: str,
    trust_level: str,
    section_title: str,
    candidates: list[str],
) -> Optional[dict]:
    """
    Stage C alignment. Returns dict:
      {chosen_sentence, span, confidence, model_used, reason}
    or None if rejected.
    """
    if not candidates:
        return None

    letters = LETTERS[: len(candidates)]
    cand_block = "\n".join(f"[{l}] {s}" for l, s in zip(letters, candidates))
    prompt = _USER_TMPL.format(
        section_title=section_title,
        claim_id=claim_id,
        trust_level=trust_level,
        claim_text=claim_text,
        candidates_block=cand_block,
    )

    result = _call_claude(prompt)
    model_used = MODEL_CLAUDE

    if result is None or result.get("chosen") == "none":
        return None

    chosen_letter = result.get("chosen", "none")
    if chosen_letter not in letters:
        return None

    chosen_idx = letters.index(chosen_letter)
    chosen_sentence = candidates[chosen_idx]
    span = result.get("span_in_chosen", "").strip()

    confidence = float(result.get("confidence", 0.0))
    if confidence < CONFIDENCE_GATE:
        return None

    match_type = "verbatim"
    if not span or span not in chosen_sentence:
        log.warning("aligner: claim_id=%d span not substring, falling back to whole sentence", claim_id)
        span = chosen_sentence.strip()
        match_type = "sentence"

    return {
        "chosen_sentence": chosen_sentence,
        "span": span,
        "confidence": confidence,
        "model_used": model_used,
        "reason": result.get("reason", ""),
        "match_type": match_type,
    }
import json
import logging
import re
from typing import Optional

from app.agent_loop.marker_embed.aligner import _call_claude, MODEL_CLAUDE, CONFIDENCE_GATE, _USER_TMPL, LETTERS

log = logging.getLogger(__name__)

# New Tier 2 Prompt
_PREC_SYS = (
    "You are matching a claim to a candidate sentence from a wiki page. "
    "Match ONLY if the sentence makes the SAME assertion: same subject AND same predicate/conclusion, paraphrase OK. "
    "Same topic but different predicate/mechanism/object -> none. "
    "Output strict JSON only — no prose, no markdown fences."
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

def align_claim_multipass(
    claim_id: int,
    claim_text: str,
    trust_level: str,
    section_title: str,
    section_candidates: list[str],
    all_sentences_with_sections: list[tuple[str, str]], # (sentence, section_title)
) -> Optional[dict]:
    """
    Tier 1: Verbatim/Sentence match in the claim's own section (existing logic).
    Tier 2: Strict cross-section predicate-equivalence across all page sentences.
    Returns: {chosen_sentence, span, confidence, model_used, reason, match_type, chosen_section}
    """
    from app.agent_loop.marker_embed.aligner import align_claim
    from app.agent_loop.marker_embed.embed_index import rank_candidates

    # Tier 1
    t1_res = align_claim(claim_id, claim_text, trust_level, section_title, section_candidates)
    if t1_res is not None:
        t1_res["chosen_section"] = section_title
        # align_claim already sets match_type (verbatim or sentence)
        return t1_res

    # Tier 2
    # Prerank candidates across all sections
    all_sents = [s for s, _ in all_sentences_with_sections]
    ranked = rank_candidates(claim_text, all_sents, top_k=20, cosine_floor=0.45)
    if not ranked:
        return None
    
    top_sents = [sent for sent, score in ranked]
    sent_to_sec = {sent: sec for sent, sec in all_sentences_with_sections}

    letters = LETTERS[: len(top_sents)]
    cand_block = "\n".join(f"[{l}] {s}" for l, s in zip(letters, top_sents))
    prompt = _PREC_USER_TMPL.format(
        claim_id=claim_id,
        trust_level=trust_level,
        claim_text=claim_text,
        candidates_block=cand_block,
    )

    import anthropic
    from app.agent_loop.marker_embed.aligner import _claude
    if _claude is None:
        return None
        
    import time
    time.sleep(0.3)
    try:
        msg = _run_with_alarm(
            lambda: _claude.messages.create(
                model=MODEL_CLAUDE,
                max_tokens=1024,
                system=_PREC_SYS,
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
        
        result = robust_extract(raw)

    except Exception as exc:
        log.warning("aligner: Claude call failed err=%s", exc)
        return None

    if result is None or result.get("chosen") == "none":
        return None

    chosen_letter = result.get("chosen", "none")
    if chosen_letter not in letters:
        return None

    chosen_idx = letters.index(chosen_letter)
    chosen_sentence = top_sents[chosen_idx]
    
    # Tier 2 gate
    confidence = float(result.get("confidence", 0.0))
    if confidence < 0.60:
        return None

    return {
        "chosen_sentence": chosen_sentence,
        "span": chosen_sentence.strip(),
        "confidence": confidence,
        "model_used": MODEL_CLAUDE,
        "reason": result.get("reason", ""),
        "match_type": "sentence",
        "chosen_section": sent_to_sec[chosen_sentence]
    }
