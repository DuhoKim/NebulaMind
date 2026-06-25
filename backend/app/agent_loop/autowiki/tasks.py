"""
autowiki_tick — 11-step autoresearch-style wiki improvement loop (§4.2).

Kill switch: Redis flag `autowiki:enabled` checked FIRST.
Rakon probe: 1-token ping before any inference; skip (not fallback) on fail.
Concurrency: Redis advisory lock per page + optimistic content-hash check.
Auto-raise: post-COMMIT, bump target_q when Q1 >= target_q - 0.03.
"""
import datetime as dt
import hashlib
import json
import logging
import re
import time
from pathlib import Path

import httpx

logger = logging.getLogger(__name__)
from sqlalchemy import func as sqlfunc
from celery.exceptions import Ignore

from app.agent_loop.worker import celery_app
from app.agent_loop.autowiki.judge import judge_page, PROMPT_VERSION
from app.agent_loop.autowiki.program_loader import load_program
from app.agent_loop.autowiki.proposers import (
    propose_claim_insert,
    propose_evidence_link,
    propose_hero_upgrade,
    propose_section_rewrite,
    ClaimInsertProposal,
    EvidenceLinkProposal,
    HeroUpgradeProposal,
    SectionRewriteProposal,
)
from app.agent_loop.autowiki.scorer import compute_quality
from app.agent_loop.autowiki.citation_context import (
    CITATION_RULES,
    build_evidence_map,
    emit_citation_scrub_required,
)
from app.config import settings
from app.database import SessionLocal
from app.models.autowiki import AutowikiRun, AutowikiTarget
from app.models.claim import Claim, Evidence
from app.models.page import PageVersion, WikiPage
from app.models.agent import Agent
from app.services.llm_utils import strip_think_blocks
from app.services.page_health import compute_health_score
from app.utils.model_guard import guard_batch_model
from app.utils.premium_dispatch import dispatch_premium, log_llm_spend

_ASTROSAGE = settings.ASTRO_SYNTH_MODEL or "astrosage-70b"


@celery_app.task(name="app.agent_loop.autowiki.tasks.align_citations_page")
def align_citations_page(page_id: int) -> dict:
    """Repair author-year citations and hallucinated cite markers for one page."""
    from scripts.align_citations import align_page, bootstrap_page_links

    with SessionLocal() as db:
        page = db.query(WikiPage).filter(WikiPage.id == page_id).first()
        if not page:
            return {"decision": "error", "reason": "page_not_found", "page_id": page_id}
        bootstrap_page_links(db, page_id)
        report = align_page(db, page, dry_run=False, bootstrap=False)
        db.commit()
        return report


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def _get_redis():
    try:
        import redis as redis_lib
        return redis_lib.from_url(settings.REDIS_URL, decode_responses=True)
    except Exception:
        return None


def _is_enabled() -> bool:
    r = _get_redis()
    if r is None:
        return False
    try:
        return r.get("autowiki:enabled") == "1"
    except Exception:
        return False


def _acquire_lock(page_id: int, ttl: int = 330) -> bool:
    r = _get_redis()
    if r is None:
        return True  # no Redis → allow (single-worker mode)
    try:
        return bool(r.set(f"autowiki:page:{page_id}", "1", nx=True, ex=ttl))
    except Exception:
        return True


def _release_lock(page_id: int) -> None:
    r = _get_redis()
    if r:
        try:
            r.delete(f"autowiki:page:{page_id}")
        except Exception:
            pass


def _rakon_probe() -> bool:
    """§4: Ollama liveness check. Returns True if the local Ollama service is
    running and BUDDLE_MODEL is installed/available on the system.

    2026-06-06 v3: switched from /api/ps (loaded-only) to /api/tags (installed).
    Checking /api/ps caused a deadlock when Ollama goes idle and unloads the
    massive 405B model, skipping all ticks and preventing it from ever loading.
    /api/tags verifies Ollama is active and responsive, and the model is
    installed, without requiring it to be resident in memory.

    2026-06-06 upgrade: Refactored to fetch from Redis key 'ollama:health' first
    to avoid conducting network pings on the critical path. Falls back gracefully.
    """
    import json
    r = _get_redis()
    if r:
        try:
            health_str = r.get("ollama:health")
            if health_str:
                health_data = json.loads(health_str)
                local_online = health_data.get("local_online", False)
                local_models = health_data.get("local_models", [])
                probe_model = settings.BUDDLE_MODEL
                
                if local_online:
                    if any(probe_model in name for name in local_models):
                        return True
                    else:
                        logger.warning("[autowiki] _rakon_probe (Redis) model not installed: %s (installed: %s)", probe_model, local_models)
                        return False
                else:
                    logger.warning("[autowiki] _rakon_probe (Redis) local node is offline")
                    return False
        except Exception as redis_err:
            logger.warning("[autowiki] _rakon_probe Redis read/parse error: %s", redis_err)

    # Fallback synchronous check
    base = settings.BUDDLE_BASE_URL.rstrip("/")
    probe_model = settings.BUDDLE_MODEL
    try:
        resp = httpx.get(f"{base}/api/tags", timeout=5)
        if resp.status_code != 200:
            logger.warning("[autowiki] _rakon_probe fallback /api/tags non-200: %s", resp.status_code)
            return False
        installed = {m.get("name", "") for m in resp.json().get("models", [])}
        if not any(probe_model in name for name in installed):
            logger.warning("[autowiki] _rakon_probe fallback model not installed: %s (installed: %s)", probe_model, installed)
            return False
        return True
    except Exception as _probe_exc:
        logger.warning("[autowiki] _rakon_probe fallback exception: %s", _probe_exc)
        return False


def _page_hash(page: WikiPage, claims: list) -> str:
    claims_text = " | ".join(c.text[:80] for c in claims)
    raw = f"{page.content}{page.hero_facts or ''}{claims_text}"
    return hashlib.sha256(raw.encode()).hexdigest()[:32]


def _claims_text(claims: list) -> str:
    return "\n".join(f"[{c.claim_type}] {c.text}" for c in claims[:40])


def _ms(t0: float) -> int:
    return int((time.monotonic() - t0) * 1000)


def _discord_notify(msg: str) -> None:
    try:
        wh = getattr(settings, "NM_DISCORD_WEBHOOK_URL", None) or getattr(settings, "DISCORD_WEBHOOK_URL", None)
        if wh:
            httpx.post(wh, json={"content": msg}, timeout=5)
    except Exception:
        pass


def _autowiki_provenance_gate_mode() -> str:
    mode = (getattr(settings, "AUTOWIKI_PROVENANCE_GATE_MODE", "shadow") or "shadow").strip().lower()
    if mode not in {"off", "shadow", "enforce"}:
        logger.warning("[autowiki_provenance] invalid mode=%s; fail-closed to shadow", mode)
        return "shadow"
    return mode


_PROVENANCE_PAIR_PROPOSAL_TYPES = {
    "claim_insert_subtopic",
    "claim_insert_debate",
    "evidence_link",
}

_PROVENANCE_SUPPRESSED_IN_ENFORCE = {
    "hero_upgrade",
    "section_rewrite",
}


def _autowiki_provenance_requires_pairs(proposal_type: str) -> bool:
    return proposal_type in _PROVENANCE_PAIR_PROPOSAL_TYPES


def _autowiki_provenance_suppressed_in_enforce(proposal_type: str) -> bool:
    return proposal_type in _PROVENANCE_SUPPRESSED_IN_ENFORCE


def _normalize_independent_d1_verdict(raw) -> str | None:
    if isinstance(raw, dict):
        raw = raw.get("verdict") or raw.get("label") or raw.get("support_verdict")
    if raw is None:
        return None
    verdict = str(raw).strip().lower()
    aliases = {
        "direct": "supported",
        "strict_support": "supported",
        "supports": "supported",
        "supported_direct": "supported",
        "unsupported": "unsupported_misattributed",
        "misattributed": "unsupported_misattributed",
        "neutral_or_unclear": "unsupported_misattributed",
        "needs_human": "no_verdict",
    }
    return aliases.get(verdict, verdict)


def _paper_quote_text(paper: dict) -> tuple[str, str]:
    quote = (
        paper.get("quoted_evidence_span")
        or paper.get("source_quote")
        or paper.get("evidence_quote")
        or paper.get("quote")
        or paper.get("quoted_span")
        or ""
    )
    evidence_text = "\n".join(
        str(paper.get(key) or "")
        for key in ("intro_excerpt", "abstract", "summary")
        if paper.get(key)
    )
    return str(quote).strip(), evidence_text


def _evaluate_autowiki_provenance_pair(claim_text: str, paper: dict) -> dict:
    verdict = _normalize_independent_d1_verdict(paper.get("independent_d1_verdict"))
    quote, evidence_text = _paper_quote_text(paper)
    reasons: list[str] = []

    if getattr(settings, "EVIDENCE_REQUIRE_ARXIV", True) and not paper.get("arxiv_id"):
        reasons.append("missing_arxiv_id")

    if getattr(settings, "EVIDENCE_REQUIRE_VERBATIM_QUOTE", True):
        if not quote:
            reasons.append("missing_verbatim_quote")
        elif quote not in evidence_text:
            reasons.append("verbatim_quote_not_substring")

    if verdict is None:
        reasons.append("missing_independent_d1_verdict")
    elif verdict == "supported":
        pass
    elif verdict == "partial" and getattr(settings, "AUTOWIKI_PROVENANCE_ALLOW_PARTIAL", False):
        pass
    else:
        reasons.append(f"independent_d1_{verdict}")

    return {
        "claim_text": claim_text,
        "arxiv_id": paper.get("arxiv_id"),
        "title": paper.get("title", ""),
        "independent_d1_verdict": verdict,
        "quote_present": bool(quote),
        "quote_substring_ok": bool(quote and quote in evidence_text),
        "would_admit": not reasons,
        "reject_reasons": reasons,
    }


def _autowiki_provenance_pairs(db, proposal) -> list[dict]:
    payload = proposal.payload
    pairs: list[dict] = []
    if isinstance(payload, ClaimInsertProposal):
        for paper in payload.papers[:3]:
            pairs.append(_evaluate_autowiki_provenance_pair(payload.claim_text, paper))
    elif isinstance(payload, EvidenceLinkProposal):
        claim = db.query(Claim).filter(Claim.id == payload.claim_id).first()
        claim_text = claim.text if claim else ""
        for paper in payload.papers[:3]:
            pairs.append(_evaluate_autowiki_provenance_pair(claim_text, paper))
    return pairs


def _record_autowiki_provenance_shadow(page_id: int, proposal_type: str, mode: str, pairs: list[dict]) -> dict:
    admitted = sum(1 for pair in pairs if pair["would_admit"])
    rejected = len(pairs) - admitted
    record = {
        "ts": dt.datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%SZ"),
        "page_id": page_id,
        "proposal_type": proposal_type,
        "mode": mode,
        "counts": {
            "pairs": len(pairs),
            "would_admit": admitted,
            "would_reject": rejected,
        },
        "pairs": pairs,
    }
    shadow_dir = Path(getattr(settings, "AUTOWIKI_PROVENANCE_SHADOW_DIR", "reports/autowiki_provenance_shadow"))
    if not shadow_dir.is_absolute():
        shadow_dir = Path.cwd() / shadow_dir
    shadow_dir.mkdir(parents=True, exist_ok=True)
    out_path = shadow_dir / f"autowiki_provenance_shadow_{dt.datetime.utcnow():%Y%m%d}.jsonl"
    with out_path.open("a", encoding="utf-8") as fh:
        fh.write(json.dumps(record, sort_keys=True) + "\n")
    logger.info(
        "[autowiki_provenance] mode=%s page=%s type=%s would_admit=%s would_reject=%s artifact=%s",
        mode,
        page_id,
        proposal_type,
        admitted,
        rejected,
        out_path,
    )
    return {**record["counts"], "artifact": str(out_path)}



def _call_opus_coherence(content: str, claims_text: str = "", citation_context: str = "") -> "str | None":
    """Call Claude claude-opus-4-8 for a full-page coherence rewrite (streaming).

    Reads NM_ANTHROPIC_API_KEY from ~/NebulaMind/NebulaMind/backend/.env.
    Returns full streamed text, or None on failure.
    Logs progress: [opus_coherence] streaming ... got {n} chars
    """
    import os as _os
    try:
        env_path = _os.path.expanduser("~/NebulaMind/NebulaMind/backend/.env")
        api_key = None
        with open(env_path) as _ef:
            for line in _ef:
                line = line.strip()
                if line.startswith("NM_ANTHROPIC_API_KEY="):
                    api_key = line.split("=", 1)[1].strip().strip('"').strip("'")
                    break
        if not api_key:
            logger.error("[opus_coherence] NM_ANTHROPIC_API_KEY not found in .env")
            return None

        import anthropic
        client = anthropic.Anthropic(api_key=api_key)
        
        # Split prompt into stable page block + dynamic instructions
        page_block = _COHERENCE_USER_TEMPLATE.replace("{citation_context}", "").format(full_page_content=content)
        dynamic_block = (
            f"===CLAIMS===\n{claims_text}\n\n"
            f"===CITATIONS===\n{citation_context}\n\n"
            "Now rewrite the page following all system instructions."
        )

        logger.info("[opus_coherence] streaming to claude-opus-4-8 (%d char page, %d char dynamic)...", len(page_block), len(dynamic_block))
        prompt_len = len(page_block) + len(dynamic_block)
        est_tokens = {"input": max(1, (len(_COHERENCE_SYSTEM_PROMPT) + prompt_len) // 4), "output": 32000}
        dispatch_premium("autowiki.opus_coherence", "claude-opus-4-8", est_tokens)

        full_text = ""
        with client.messages.stream(
            model="claude-opus-4-8",
            max_tokens=32000,
            system=_COHERENCE_SYSTEM_PROMPT,
            messages=[
                {
                    "role": "user",
                    "content": [
                        {
                            "type": "text",
                            "text": page_block,
                            "cache_control": {"type": "ephemeral"},  # cache page content
                        },
                        {
                            "type": "text",
                            "text": dynamic_block,                   # dynamic, not cached
                        },
                    ],
                }
            ],
        ) as stream:
            for chunk in stream.text_stream:
                full_text += chunk

        logger.info("[opus_coherence] streaming complete, got %d chars", len(full_text))
        final_msg = stream.get_final_message()
        usage = getattr(final_msg, "usage", None)
        log_llm_spend(
            "autowiki.opus_coherence",
            "claude-opus-4-8",
            prompt_tokens=getattr(usage, "input_tokens", None),
            completion_tokens=getattr(usage, "output_tokens", None),
            cache_creation_tokens=getattr(usage, "cache_creation_input_tokens", None),
            cache_read_tokens=getattr(usage, "cache_read_input_tokens", None),
            estimated_tokens=est_tokens["input"],
        )
        return full_text
    except Exception as exc:
        logger.error("[opus_coherence] failed: %s", exc)
        return None


def _call_gemini_coherence(content: str, claims_text: str = "", citation_context: str = "") -> "str | None":
    """Call Gemini 2.5 Pro for a full-page coherence rewrite (OpenAI-compat endpoint).

    Reads NM_GEMINI_API_KEY from ~/NebulaMind/NebulaMind/backend/.env.
    Returns full response text, or None on failure.
    """
    import os as _os
    try:
        env_path = _os.path.expanduser("~/NebulaMind/NebulaMind/backend/.env")
        api_key = None
        with open(env_path) as _ef:
            for line in _ef:
                line = line.strip()
                if line.startswith("NM_GEMINI_API_KEY="):
                    api_key = line.split("=", 1)[1].strip().strip('"').strip("'")
                    break
        if not api_key:
            logger.error("[gemini_coherence] NM_GEMINI_API_KEY not found in .env")
            return None

        prompt = _COHERENCE_USER_TEMPLATE.format(full_page_content=content, claims_text=claims_text, citation_context=citation_context)
        logger.info("[gemini_coherence] calling gemini-2.5-pro (%d char prompt)...", len(prompt))
        est_tokens = {"input": max(1, (len(_COHERENCE_SYSTEM_PROMPT) + len(prompt)) // 4), "output": 65536}
        dispatch_premium("autowiki.gemini_coherence", "gemini-2.5-pro", est_tokens)

        resp = httpx.post(
            "https://generativelanguage.googleapis.com/v1beta/openai/chat/completions",
            headers={
                "Authorization": f"Bearer {api_key}",
                "Content-Type": "application/json",
            },
            json={
                "model": "gemini-2.5-pro",
                "max_tokens": 65536,
                "messages": [
                    {"role": "system", "content": _COHERENCE_SYSTEM_PROMPT},
                    {"role": "user", "content": prompt},
                ],
            },
            timeout=1800,
        )
        resp.raise_for_status()
        data = resp.json()
        usage = data.get("usage") or {}
        log_llm_spend(
            "autowiki.gemini_coherence",
            "gemini-2.5-pro",
            prompt_tokens=usage.get("prompt_tokens"),
            completion_tokens=usage.get("completion_tokens"),
            estimated_tokens=est_tokens["input"],
        )
        text = (data["choices"][0]["message"].get("content") or "").strip()
        if not text:
            logger.error("[gemini_coherence] empty content in response: %s", str(data)[:300])
            return None
        logger.info("[gemini_coherence] got %d chars", len(text))
        return text
    except Exception as exc:
        logger.error("[gemini_coherence] failed: %s", exc)
        return None


def _score_coherence_output(text: str) -> int:
    """Score a coherence rewrite candidate. Higher = better."""
    if not text:
        return -1
    import re as _re
    h2s = len(_re.findall(r'^## ', text, _re.MULTILINE))
    h3s = len(_re.findall(r'^### ', text, _re.MULTILINE))
    return len(text) + (h2s * 5000) + (h3s * 2000)


COHERENCE_TRIGGER_REWRITES = 50


def _check_coherence_due(db, page_id: int) -> bool:
    """Return True if a coherence pass should be triggered for *page_id*.

    Three conditions (manual trigger or count threshold), guarded by dispatch lock:
    1. If ``autowiki:coherence_dispatched:{page_id}`` is set, a pass is already
       in flight — return False to prevent double-dispatch.
    2. Redis flag ``autowiki:coherence_needed:{page_id}`` is set (manual trigger).
    3. The number of committed ``section_rewrite`` runs since the last committed
       ``rakon_coherence_pass`` exceeds COHERENCE_TRIGGER_REWRITES (default 50).
    """
    try:
        r = _get_redis()
        if r and r.get(f"autowiki:coherence_dispatched:{page_id}"):
            return False
        if r and r.get(f"autowiki:coherence_needed:{page_id}"):
            return True
    except Exception:
        pass

    try:
        from sqlalchemy import text as _sqlt
        row = db.execute(_sqlt("""
            SELECT COUNT(*) FROM autowiki_runs
            WHERE page_id = :pid
              AND proposal_type = 'section_rewrite'
              AND decision = 'commit'
              AND id > COALESCE(
                (SELECT MAX(id) FROM autowiki_runs
                 WHERE page_id = :pid
                   AND proposal_type = 'rakon_coherence_pass'
                   AND decision = 'commit'),
                0
              )
        """), {"pid": page_id}).scalar()
        if (row or 0) >= COHERENCE_TRIGGER_REWRITES:
            return True
    except Exception:
        pass

    return False


def _compute_idea_signals(db, page_id: int) -> tuple[dict[int, float], list[int]]:
    """Step 3.5 — pure SQL, no LLM, p95 < 50ms.

    Returns (claim_boosts, orphan_high_value_idea_ids).
    claim_boosts: {claim_id: boost} where boost = sum of per-idea signals, capped at 1.0.
    Boost components per anchored idea:
      +0.5 saved_by_papa, +0.3 well_posed_score>=0.7, +0.2 status='active',
      plus +0.1×min(count,3) volume signal.
    """
    from sqlalchemy import text

    boost_rows = db.execute(text("""
        SELECT
            regexp_replace(a.ref_id, '[^0-9]', '', 'g')::int AS claim_id,
            LEAST(1.0,
                SUM(
                    CASE WHEN ri.saved_by_papa THEN 0.5 ELSE 0.0 END
                    + CASE WHEN ri.well_posed_score >= 0.7 THEN 0.3 ELSE 0.0 END
                    + CASE WHEN ri.status = 'active' THEN 0.2 ELSE 0.0 END
                )
                + LEAST(COUNT(*)::float, 3.0) * 0.1
            ) AS boost
        FROM research_ideas ri
        JOIN research_idea_anchors a ON a.idea_id = ri.id AND a.kind = 'claim'
        WHERE ri.page_id = :page_id
        GROUP BY a.ref_id
    """), {"page_id": page_id}).fetchall()

    claim_boosts = {row.claim_id: float(row.boost) for row in boost_rows}

    orphan_rows = db.execute(text("""
        SELECT ri.id
        FROM research_ideas ri
        WHERE ri.page_id = :page_id
          AND (ri.saved_by_papa OR ri.well_posed_score >= 0.7)
          AND NOT EXISTS (
              SELECT 1 FROM research_idea_anchors a
              WHERE a.idea_id = ri.id AND a.kind = 'claim'
          )
    """), {"page_id": page_id}).fetchall()

    return claim_boosts, [row.id for row in orphan_rows]


def _takji_methodology_check(proposed_text: str, claims_block: str) -> dict:
    """K2 gate: Nutty checks methodology + dataset realism + systematics.
    Returns {'verdict': 'pass'|'soft_fail'|'hard_fail', 'rationale': str}.
    """
    import re as _re
    prompt = (
        "You are a strict methodology referee for astrophysics research claims.\n"
        "Evaluate the following proposed claim for:\n"
        "1. Methodological soundness (are the methods plausible for the claimed conclusion?)\n"
        "2. Dataset realism (are cited datasets real, accessible, and appropriate?)\n"
        "3. Systematics consistency (does the claim account for known systematic effects?)\n\n"
        f"Existing accepted claims (context):\n{claims_block[:2000]}\n\n"
        f"Proposed claim to evaluate:\n{proposed_text[:500]}\n\n"
        'Respond with ONLY a JSON object:\n'
        '{"verdict": "pass"|"soft_fail"|"hard_fail", "rationale": "<one sentence>"}\n'
        "- pass: methodologically sound\n"
        "- soft_fail: minor issues, not disqualifying\n"
        "- hard_fail: fundamental flaw, fabricated dataset, or systematics violation"
    )
    try:
        model = guard_batch_model(settings.ADVERSARIAL_SKEPTIC_MODEL, "autowiki.takji_methodology_check")
        est_tokens = max(1, len(prompt) // 4)
        dispatch_premium("autowiki.takji_methodology_check", model, est_tokens)
        resp = httpx.post(
            "http://localhost:11434/v1/chat/completions",
            json={
                "model": model,
                "messages": [{"role": "user", "content": prompt}],
                "temperature": 0.1,
                "stream": False,
            },
            timeout=120,
            headers={"Authorization": "Bearer ollama"},
        )
        resp.raise_for_status()
        data = resp.json()
        usage = data.get("usage") or {}
        log_llm_spend(
            "autowiki.takji_methodology_check",
            model,
            prompt_tokens=usage.get("prompt_tokens"),
            completion_tokens=usage.get("completion_tokens"),
            estimated_tokens=est_tokens,
        )
        raw = data["choices"][0]["message"]["content"]
        raw = _re.sub(r"```(?:json)?\s*", "", raw)
        raw = _re.sub(r"```", "", raw)
        raw = strip_think_blocks(raw)
        m = _re.search(r"\{[\s\S]*\}", raw.strip())
        if m:
            result = json.loads(m.group())
            if result.get("verdict") in ("pass", "soft_fail", "hard_fail"):
                return result
    except Exception as exc:
        logger.warning("[autowiki] _takji_methodology_check failed: %s", exc)
    return {"verdict": "pass", "rationale": "takji unavailable — defaulting pass"}


def _atom_score_5_random_accepted_claims(db, page_id: int) -> None:
    """X4: Atom-7b scores 5 random accepted claims for relevance decay.
    Writes claim_decay_candidates rows for claims scoring < 0.4.
    """
    import re as _re
    from sqlalchemy import text as _text
    try:
        rows = db.execute(_text("""
            SELECT id, text FROM claims
            WHERE page_id = :page_id AND trust_level = 'accepted'
            ORDER BY RANDOM() LIMIT 5
        """), {"page_id": page_id}).fetchall()
    except Exception as exc:
        logger.warning("[autowiki] X4 claim fetch page=%d failed: %s", page_id, exc)
        return
    for row in rows:
        prompt = (
            "Rate the relevance of this astrophysics research claim to current "
            "observational surveys on a scale from 0.0 to 1.0.\n"
            f"Claim: {row.text[:400]}\n"
            'Respond with ONLY a JSON: {"score": <float 0-1>, "rationale": "<one sentence>"}'
        )
        try:
            model = guard_batch_model(
                "vanta-research/atom-astronomy-7b:latest",
                "autowiki.atom_score_accepted_claims",
            )
            est_tokens = max(1, len(prompt) // 4)
            dispatch_premium("autowiki.atom_score_accepted_claims", model, est_tokens)
            resp = httpx.post(
                "http://localhost:11434/v1/chat/completions",
                json={
                    "model": model,
                    "messages": [{"role": "user", "content": prompt}],
                    "temperature": 0.1,
                    "stream": False,
                },
                timeout=60,
                headers={"Authorization": "Bearer ollama"},
            )
            resp.raise_for_status()
            data = resp.json()
            usage = data.get("usage") or {}
            log_llm_spend(
                "autowiki.atom_score_accepted_claims",
                model,
                prompt_tokens=usage.get("prompt_tokens"),
                completion_tokens=usage.get("completion_tokens"),
                estimated_tokens=est_tokens,
            )
            raw = data["choices"][0]["message"]["content"]
            raw = _re.sub(r"```(?:json)?\s*", "", raw)
            raw = _re.sub(r"```", "", raw)
            m = _re.search(r"\{[\s\S]*\}", raw.strip())
            if not m:
                continue
            result = json.loads(m.group())
            score = float(result.get("score", 1.0))
            if score < 0.4:
                db.execute(_text("""
                    INSERT INTO claim_decay_candidates
                        (claim_id, decay_score, flagged_at, flagged_by_model, status)
                    VALUES (:cid, :score, NOW(), :model, 'pending')
                    ON CONFLICT DO NOTHING
                """), {
                    "cid": row.id,
                    "score": score,
                    "model": "vanta-research/atom-astronomy-7b:latest",
                })
                db.commit()
        except Exception as exc:
            db.rollback()
            logger.warning("[autowiki] X4 atom score claim=%d failed: %s", row.id, exc)


# ---------------------------------------------------------------------------
# Rollback helpers
# ---------------------------------------------------------------------------

def _rollback_claim_insert(
    db, claim_ids: list[int], evidence_ids: list[int]
) -> None:
    db.query(Evidence).filter(Evidence.id.in_(evidence_ids)).delete(synchronize_session=False)
    db.query(Claim).filter(Claim.id.in_(claim_ids)).delete(synchronize_session=False)


def _rollback_evidence_link(db, evidence_ids: list[int]) -> None:
    db.query(Evidence).filter(Evidence.id.in_(evidence_ids)).delete(synchronize_session=False)


def _rollback_hero_upgrade(page: WikiPage, prior_hero_facts: str | None) -> None:
    page.hero_facts = prior_hero_facts


def _rollback_section_rewrite(db, page: WikiPage, prior_version_id: int) -> None:
    prior = db.query(PageVersion).filter(PageVersion.id == prior_version_id).first()
    if prior:
        page.content = prior.content
    new_version = (
        db.query(PageVersion)
        .filter(PageVersion.page_id == page.id)
        .order_by(PageVersion.id.desc())
        .first()
    )
    if new_version and new_version.id != prior_version_id:
        db.delete(new_version)


# ---------------------------------------------------------------------------
# Pipeline Upgrade Phase 3 (Sequential Canvas Chains in Celery)
# ---------------------------------------------------------------------------

class PipelineSkip(Exception):
    """Exception to cleanly skip or rollback the pipeline chain in Stage 1."""
    pass


def _clear_run_meta(page_id: int) -> None:
    r = _get_redis()
    if r:
        try:
            r.delete(f"autowiki:run_meta:{page_id}")
        except Exception:
            pass


@celery_app.task(
    name="app.agent_loop.autowiki.tasks.autowiki_propose_and_commit",
    bind=True,
    max_retries=0,
)
def autowiki_propose_and_commit(self, page_id: int, pre_image_version_id: int | None = None) -> int:
    latency = {}
    tick_start = time.monotonic()
    
    # Run the tick logic
    result = _run_tick(page_id, tick_start, latency)
    
    decision = result.get("decision")
    if decision != "commit":
        _release_lock(page_id)
        _clear_run_meta(page_id)
        self.update_state(state="IGNORED", meta=result)
        raise Ignore()
        
    # On commit, save run metadata in Redis for rollback capability
    try:
        r = _get_redis()
        if r:
            with SessionLocal() as db:
                run = db.query(AutowikiRun).filter(
                    AutowikiRun.page_id == page_id,
                    AutowikiRun.decision == 'commit'
                ).order_by(AutowikiRun.id.desc()).first()
                
                claim_ids = []
                evidence_ids = []
                prior_hero_facts = None
                
                page = db.query(WikiPage).filter(WikiPage.id == page_id).first()
                if page:
                    prior_hero_facts = page.hero_facts
                
                if run:
                    claims_to_delete = db.query(Claim).filter(
                        Claim.page_id == page_id,
                        Claim.created_at >= run.started_at - dt.timedelta(seconds=10)
                    ).all()
                    claim_ids = [c.id for c in claims_to_delete]
                    
                    if claim_ids:
                        ev_rows = db.query(Evidence).filter(Evidence.claim_id.in_(claim_ids)).all()
                        evidence_ids = [e.id for e in ev_rows]
                    else:
                        evidence_to_delete = db.query(Evidence).join(Claim).filter(
                            Claim.page_id == page_id,
                            Evidence.created_at >= run.started_at - dt.timedelta(seconds=10)
                        ).all()
                        evidence_ids = [e.id for e in evidence_to_delete]
                        
                meta = {
                    "prior_hero_facts": prior_hero_facts,
                    "proposal_type": result.get("proposal_type"),
                    "claim_ids_inserted": claim_ids,
                    "evidence_ids_inserted": evidence_ids,
                    "prior_page_version_id": pre_image_version_id,
                }
                r.set(f"autowiki:run_meta:{page_id}", json.dumps(meta), ex=3600)
    except Exception as meta_exc:
        logger.warning("[autowiki_propose_and_commit] Failed to save metadata in Redis: %s", meta_exc)
        
    return page_id


@celery_app.task(
    name="app.agent_loop.autowiki.tasks.autowiki_post_pipeline_notify",
    bind=True,
    max_retries=0,
)
def autowiki_post_pipeline_notify(self, result_dict, page_id: int) -> dict:
    # Strictly release the Redis advisory lock
    _release_lock(page_id)
    
    # Clean up the run metadata since it completed successfully!
    _clear_run_meta(page_id)
    
    # Update last_tick and decision in Redis
    try:
        r = _get_redis()
        if r:
            now_iso = dt.datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%SZ")
            r.set("autowiki:last_tick", now_iso, ex=86400)
            r.set("autowiki:last_tick_decision", "commit", ex=86400)
    except Exception as redis_exc:
        logger.error("[autowiki_post_pipeline_notify] Failed to write to Redis: %s", redis_exc)
        
    logger.info(
        "[autowiki_post_pipeline_notify] Pipeline successfully completed for page %d. Stats: %s",
        page_id, result_dict
    )
    
    # Trigger process notifications (Discord)
    status_str = result_dict.get("status") if isinstance(result_dict, dict) else "success"
    coverage = result_dict.get("coverage_pct") if isinstance(result_dict, dict) else None
    matched = result_dict.get("matched") if isinstance(result_dict, dict) else None
    total = result_dict.get("total") if isinstance(result_dict, dict) else None
    
    msg = f"✅ **autowiki** page={page_id} pipeline successfully completed! "
    if coverage is not None:
        msg += f"Marker embedding coverage: {coverage:.2f}%. Matched: {matched}/{total}."
        
    _discord_notify(msg)
    
    return {"status": "success", "page_id": page_id, "stats": result_dict}


@celery_app.task(
    name="app.agent_loop.autowiki.tasks.autowiki_pipeline_rollback",
    bind=True,
    max_retries=0,
)
def autowiki_pipeline_rollback(self, request=None, exc=None, traceback=None, page_id: int | None = None, *extra):
    if page_id is None and extra:
        page_id = extra[0]
    if page_id is None and isinstance(request, int):
        page_id = request
        request = None
    if page_id is None:
        logger.error("[autowiki_pipeline_rollback] Missing page_id; request=%s exc=%s", request, exc)
        return {"status": "error", "reason": "missing_page_id"}

    # Ensure Redis page lock is strictly released
    _release_lock(page_id)
    
    # Check if this is a PipelineSkip vs a real error
    exc_class_name = exc.__class__.__name__ if exc else ""
    is_skip = (exc_class_name == "PipelineSkip")
    
    if is_skip:
        logger.info("[autowiki_pipeline_rollback] Pipeline skipped/rolled back cleanly in Stage 1: %s", exc)
        _clear_run_meta(page_id)
        return {"status": "skipped", "reason": str(exc)}
        
    logger.error("[autowiki_pipeline_rollback] Pipeline failed on page %d: %s", page_id, exc)
    
    # Log detailed error trace to logs/autowiki_pipeline_errors.log
    import os
    try:
        os.makedirs("/Users/duhokim/NebulaMind/NebulaMind/backend/logs", exist_ok=True)
        with open("/Users/duhokim/NebulaMind/NebulaMind/backend/logs/autowiki_pipeline_errors.log", "a") as f:
            f.write(f"=== {dt.datetime.utcnow().isoformat()} ===\n")
            f.write(f"Page ID: {page_id}\n")
            f.write(f"Exception: {exc}\n")
            f.write(f"Traceback:\n{traceback}\n")
            f.write("=========================================\n\n")
    except Exception as io_err:
        logger.error("[autowiki_pipeline_rollback] Failed to write to error log: %s", io_err)

    # Perform DB rollback and clean up using Redis metadata if available
    r = _get_redis()
    meta = None
    if r:
        meta_str = r.get(f"autowiki:run_meta:{page_id}")
        if meta_str:
            try:
                meta = json.loads(meta_str)
            except Exception:
                pass
                
    with SessionLocal() as db:
        try:
            prior_version_id = meta.get("prior_page_version_id") if meta else None
            
            page = db.query(WikiPage).filter(WikiPage.id == page_id).first()
            if page:
                if meta and "prior_hero_facts" in meta:
                    page.hero_facts = meta["prior_hero_facts"]
                
                if meta and meta.get("proposal_type") == "section_rewrite" and prior_version_id is not None:
                    prior = db.query(PageVersion).filter(PageVersion.id == prior_version_id).first()
                    if prior:
                        page.content = prior.content
                    
                    db.query(PageVersion).filter(
                        PageVersion.page_id == page_id,
                        PageVersion.id > prior_version_id
                    ).delete(synchronize_session=False)

            if meta:
                claim_ids = meta.get("claim_ids_inserted") or []
                evidence_ids = meta.get("evidence_ids_inserted") or []
                if evidence_ids:
                    db.query(Evidence).filter(Evidence.id.in_(evidence_ids)).delete(synchronize_session=False)
                if claim_ids:
                    db.query(Claim).filter(Claim.id.in_(claim_ids)).delete(synchronize_session=False)
                    
            # Fallback cleanup just in case metadata is missing or incomplete
            if not meta or not meta.get("proposal_type"):
                run = db.query(AutowikiRun).filter(
                    AutowikiRun.page_id == page_id,
                    AutowikiRun.decision == 'commit'
                ).order_by(AutowikiRun.id.desc()).first()
                if run:
                    run.decision = "error"
                    run.error_text = str(exc)[:2000]
                    
                    if run.proposal_type == "section_rewrite" and run.committed_version_id:
                        prior_pv = db.query(PageVersion).filter(
                            PageVersion.page_id == page_id,
                            PageVersion.id < run.committed_version_id
                        ).order_by(PageVersion.id.desc()).first()
                        if prior_pv and page:
                            page.content = prior_pv.content
                        
                        db.query(PageVersion).filter(PageVersion.id == run.committed_version_id).delete(synchronize_session=False)
                    
                    claims_to_delete = db.query(Claim).filter(
                        Claim.page_id == page_id,
                        Claim.created_at >= run.started_at - dt.timedelta(seconds=10)
                    ).all()
                    claim_ids = [c.id for c in claims_to_delete]
                    if claim_ids:
                        db.query(Evidence).filter(Evidence.id.in_(claim_ids)).delete(synchronize_session=False)
                        db.query(Claim).filter(Claim.id.in_(claim_ids)).delete(synchronize_session=False)
                    
                    evidence_to_delete = db.query(Evidence).join(Claim).filter(
                        Claim.page_id == page_id,
                        Evidence.created_at >= run.started_at - dt.timedelta(seconds=10)
                    ).all()
                    ev_ids = [e.id for e in evidence_to_delete]
                    if ev_ids:
                        db.query(Evidence).filter(Evidence.id.in_(ev_ids)).delete(synchronize_session=False)

            db.commit()
        except Exception as db_err:
            db.rollback()
            logger.error("[autowiki_pipeline_rollback] Database rollback failed: %s", db_err)
        finally:
            _clear_run_meta(page_id)


# ---------------------------------------------------------------------------
# Main tick
# ---------------------------------------------------------------------------

@celery_app.task(
    name="app.agent_loop.autowiki.tasks.autowiki_tick",
    task_acks_late=True,
    max_retries=0,
)
def autowiki_tick(page_id: int) -> dict:
    # --- Kill switch (§4.5) ---
    if not _is_enabled():
        return {"decision": "skip", "reject_reason": "flag_off"}

    # --- Rakon probe (§4, warm probe) ---
    if not _rakon_probe():
        logger.warning("[autowiki] tick skipped: rakon_unavailable")
        return {"decision": "skip", "reject_reason": "rakon_unavailable"}

    if not _acquire_lock(page_id):
        logger.warning("[autowiki] tick skipped: concurrent_tick lock held on page %d", page_id)
        return {"decision": "skip", "reject_reason": "concurrent_tick"}

    # Query pre-image PageVersion ID before the pipeline runs
    from app.models.page import PageVersion
    from app.database import SessionLocal
    pre_image_version_id = None
    try:
        with SessionLocal() as db:
            last_ver = (
                db.query(PageVersion)
                .filter(PageVersion.page_id == page_id)
                .order_by(PageVersion.id.desc())
                .first()
            )
            pre_image_version_id = last_ver.id if last_ver else None
    except Exception as db_exc:
        logger.error("[autowiki_tick] Failed to get pre-image page version ID: %s", db_exc)

    from celery import chain
    from app.agent_loop.autowiki.tasks import (
        autowiki_propose_and_commit,
        autowiki_post_pipeline_notify,
        autowiki_pipeline_rollback
    )
    from app.agent_loop.marker_embed.tasks import claim_marker_embed_page, marker_reembed_enabled

    stages = [autowiki_propose_and_commit.s(page_id, pre_image_version_id).set(queue="autowiki")]
    if marker_reembed_enabled():
        stages.append(claim_marker_embed_page.s().set(queue="autowiki"))
    else:
        # Re-enable with Redis marker_embed:enabled=1 or MARKER_REEMBED_ENABLED=1.
        logger.info("[autowiki_tick] Marker overlay stage disabled; skipping marker embed pass")
    stages.append(autowiki_post_pipeline_notify.s(page_id).set(queue="autowiki"))

    pipeline = chain(*stages).on_error(autowiki_pipeline_rollback.s(page_id).set(queue="autowiki"))

    pipeline.delay()
    logger.info("[autowiki_tick] Dispatched sequential canvas chain for page %d", page_id)
    return {"status": "dispatched", "page_id": page_id}


def _run_tick(page_id: int, tick_start: float, latency: dict) -> dict:
    started_at = dt.datetime.utcnow()

    with SessionLocal() as db:
        # ── Step 1: Load page ───────────────────────────────────────────────
        page = db.query(WikiPage).filter(WikiPage.id == page_id).first()
        if not page:
            return {"decision": "error", "reject_reason": f"page {page_id} not found"}

        if getattr(page, "do_not_renovate", False):
            logger.info("[autowiki] tick skipped: do_not_renovate=True page=%d", page_id)
            return {"decision": "skip", "reject_reason": "do_not_renovate"}

        claims = db.query(Claim).filter(Claim.page_id == page_id).order_by(Claim.created_at).all()
        hash_before = _page_hash(page, claims)
        program = load_program(page.slug)
        prior_hero_facts = page.hero_facts

        # ── Step 2: Compute H0_struct ───────────────────────────────────────
        t = time.monotonic()
        h0_result = compute_health_score(page, db)
        latency["h0_struct_ms"] = _ms(t)
        h0_struct = h0_result["score"]
        components_before = h0_result["components"]
        missing_subtopics = h0_result.get("missing_subtopics", [])

        # ── Step 3: Fetch U0 (baseline utility) ────────────────────────────
        t = time.monotonic()
        claims_text_before = _claims_text(claims)
        u0_result = judge_page(
            page_id=page_id,
            content=page.content,
            hero_facts=page.hero_facts,
            claims_text=claims_text_before,
            force=True,  # keep baseline and candidate scoring symmetric
        )
        latency["u0_judge_ms"] = _ms(t)
        u0 = u0_result.utility
        q0 = compute_quality(h0_struct, u0)

        # ── Step 3.5: Idea Signals (§16.3, pure SQL, <50ms) ─────────────────
        claim_boosts: dict[int, float] = {}
        orphan_high_value: list[int] = []
        topic_hint: str | None = None
        idea_signals_json: dict | None = None
        t = time.monotonic()
        try:
            claim_boosts, orphan_high_value = _compute_idea_signals(db, page_id)
            idea_signals_json = {
                "claim_boosts": {str(k): v for k, v in claim_boosts.items()},
                "orphan_count": len(orphan_high_value),
                "topic_hint": None,
            }
            if orphan_high_value:
                logger.info(
                    "[autowiki] step3.5 orphan_high_value=%s page=%d",
                    orphan_high_value, page_id,
                )
                _r2 = _get_redis()
                _cooldown_key = f"autowiki:orphan_ping:{page_id}"
                if _r2 and not _r2.get(_cooldown_key):
                    _discord_notify(
                        f"🔭 **autowiki** page={page_id}: "
                        f"{len(orphan_high_value)} orphan high-value idea(s) "
                        f"(ids: {orphan_high_value[:5]}) — "
                        "saved/well-posed but no claim anchor. "
                        "Consider claim_insert_debate on the next tick."
                    )
                    try:
                        _r2.set(_cooldown_key, "1", ex=86400)
                    except Exception:
                        pass
        except Exception as exc:
            db.rollback()
            logger.warning("[autowiki] step3.5 idea_signals failed: %s", exc)
        latency["idea_signals_ms"] = _ms(t)

        # ── Step 4: Pick proposal type ──────────────────────────────────────
        depth = components_before.get("depth", 1.0)
        freshness = components_before.get("freshness", 1.0)
        hero_richness = components_before.get("hero_richness", 1.0)
        debate_count = sum(1 for c in claims if c.claim_type == "debate")

        proposal_type: str
        if depth < 0.7 and missing_subtopics:
            proposal_type = "claim_insert_subtopic"
        elif debate_count < 4:
            proposal_type = "claim_insert_debate"
        elif orphan_high_value and debate_count < 7:
            # §16.4 rule 2: orphan idea signals missing claim → debate insert with topic hint
            proposal_type = "claim_insert_debate"
            try:
                from sqlalchemy import text as _sqlt
                _row = db.execute(
                    _sqlt("SELECT question FROM research_ideas WHERE id = :id"),
                    {"id": orphan_high_value[0]},
                ).fetchone()
                if _row:
                    topic_hint = _row.question[:300]
                    if idea_signals_json is not None:
                        idea_signals_json = {**idea_signals_json, "topic_hint": topic_hint}
            except Exception:
                pass
        elif freshness < 0.6:
            proposal_type = "evidence_link"
        elif hero_richness < 0.9:
            proposal_type = "hero_upgrade"
        else:
            # SectionRewrite: pick a section not recently touched
            proposal_type = "section_rewrite"

        provenance_mode = _autowiki_provenance_gate_mode()
        if provenance_mode == "enforce" and _autowiki_provenance_suppressed_in_enforce(proposal_type):
            latency["proposer_ms"] = 0
            provenance_note = {
                "mode": provenance_mode,
                "proposal_type": proposal_type,
                "suppressed_before_proposer": True,
                "reason": "empty_provenance_pairs_not_enforceable",
            }
            if idea_signals_json is not None:
                idea_signals_json = {**idea_signals_json, "provenance_enforce": provenance_note}
            else:
                idea_signals_json = {"provenance_enforce": provenance_note}
            logger.info(
                "[autowiki_provenance] enforce suppresses proposal_type=%s before proposer execution",
                proposal_type,
            )
            return _emit_run(
                db, page_id, started_at, proposal_type, h0_struct, None,
                components_before, None, u0_result, None, q0, None,
                "gate_reject",
                "provenance_enforce_suppressed_empty_pairs",
                None, latency, None,
                idea_signals_json=idea_signals_json,
            )


        # surveys-win: if Surveys autowiki holds astrosage:surveys_priority, defer this tick
        _r = _get_redis()
        if _r:
            try:
                _sp = _r.get("astrosage:surveys_priority")
                if _sp:
                    logger.info(
                        "[autowiki] tick deferred: surveys_priority held by %s", _sp
                    )
                    return {"decision": "skip", "reject_reason": "surveys_priority"}
                # per-page AstroSage pause: set autowiki:skip_astrosage:{page_id} to pause
                _skip_key = f"autowiki:skip_astrosage:{page_id}"
                if _r.get(_skip_key):
                    logger.info("[autowiki] tick skipped: astrosage paused for page %d", page_id)
                    return {"decision": "skip", "reject_reason": f"astrosage_paused_page_{page_id}"}
            except Exception:
                pass

        # ── Coherence gate (highest priority) ───────────────────────────────────
        if _check_coherence_due(db, page_id):
            run_rakon_coherence_pass.apply_async(
                kwargs={"page_id": page_id},
                queue="autowiki",
            )
            try:
                _r_lock = _get_redis()
                if _r_lock:
                    _r_lock.set(f"autowiki:coherence_dispatched:{page_id}", "1", ex=7200)
            except Exception:
                pass
            logger.info("[autowiki] coherence_dispatched page=%d", page_id)
            return {"decision": "coherence_dispatched", "page_id": page_id}

        # ── Step 5: Run proposer (AstroSage-70B, 90s budget) ───────────────
        t = time.monotonic()
        claim_ids_inserted: list[int] = []
        evidence_ids_inserted: list[int] = []
        prior_page_version_id: int | None = None

        try:
            if proposal_type in ("claim_insert_subtopic", "claim_insert_debate"):
                ctype = "debate" if proposal_type == "claim_insert_debate" else "established"
                proposal = propose_claim_insert(
                    page.content, page_id, program,
                    claim_type=ctype,
                    missing_subtopics=missing_subtopics,
                    topic_hint=topic_hint,
                )
            elif proposal_type == "evidence_link":
                # §16.4 rule 3: rank by evidence_count - 2.0×claim_boost so Papa-saved
                # idea anchors get prioritized for evidence even with more existing evidence.
                from app.models.claim import Evidence as Ev
                ev_counts = {
                    c.id: db.query(sqlfunc.count(Ev.id))
                    .filter(Ev.claim_id == c.id)
                    .scalar()
                    for c in claims
                }
                sorted_claims = sorted(
                    claims,
                    key=lambda c: ev_counts.get(c.id, 0) - 2.0 * claim_boosts.get(c.id, 0.0),
                )
                proposal = propose_evidence_link(page.content, sorted_claims, program)
            elif proposal_type == "hero_upgrade":
                proposal = propose_hero_upgrade(page.content, page.hero_facts, program)
            else:  # section_rewrite
                # Round-robin across all ## sections: use total run count % num_sections
                import re
                sections = re.findall(r"^## (.+)$", page.content, re.MULTILINE)
                if sections:
                    rewrite_count = (
                        db.query(sqlfunc.count(AutowikiRun.id))
                        .filter(
                            AutowikiRun.page_id == page_id,
                            AutowikiRun.proposal_type == "section_rewrite",
                        )
                        .scalar()
                        or 0
                    )
                    section_header = sections[rewrite_count % len(sections)]
                else:
                    section_header = "Overview"
                from sqlalchemy import text
                sec_key = re.sub(r'[^a-z0-9\s]', '', section_header.replace('##', '').lower()).replace(' ', '_').strip()
                owned_res = db.execute(text("""
                    SELECT c.id, c.trust_level, c.text 
                    FROM claim_section_assignments a
                    JOIN claims c ON c.id = a.claim_id
                    WHERE a.page_id = :pid AND a.owner_section_key = :sec_key AND a.assignment_status = 'active'
                """), {"pid": page_id, "sec_key": sec_key}).fetchall()
                
                must_keep = [r for r in owned_res if r.trust_level in ('accepted', 'consensus')]
                optional = [r for r in owned_res if r.trust_level not in ('accepted', 'consensus')]
                
                owned_claims_text = "Must-Keep Owned Claims:\n" + "\n".join(f"<!--claim:{c.id}--> [{c.trust_level}] {c.text[:200]}" for c in must_keep) + "\n\n"
                owned_claims_text += "Optional Owned Claims:\n" + "\n".join(f"<!--claim:{c.id}--> [{c.trust_level}] {c.text[:200]}" for c in optional)
                
                context_res = db.execute(text("""
                    SELECT c.id, c.trust_level, c.text 
                    FROM claim_section_assignments a
                    JOIN claims c ON c.id = a.claim_id
                    WHERE a.page_id = :pid AND a.owner_section_key != :sec_key AND a.assignment_status = 'active'
                    LIMIT 10
                """), {"pid": page_id, "sec_key": sec_key}).fetchall()
                context_claims_text = "\n".join(f"<!--claim:{c.id}--> [{c.trust_level}] {c.text[:200]}" for c in context_res)

                proposal = propose_section_rewrite(
                    page.content,
                    section_header,
                    program,
                    owned_claims_text,
                    context_claims_text,
                    page_id=page_id,
                )
                
                # Check gate
                raw_text = proposal.payload.new_content if hasattr(proposal.payload, "new_content") else ""
                report_match = re.search(r"<!--marker-report\s*({.*?})\s*-->", raw_text, re.DOTALL) if raw_text else None
                if report_match:
                    try:
                        import json
                        report = json.loads(report_match.group(1))
                        proposal.payload.new_content = re.sub(
                            r"<!--marker-report.*?-->",
                            "",
                            raw_text,
                            flags=re.DOTALL,
                        ).strip()
                        proposal.payload.new_content = re.sub(
                            r"<!--unmatched-citation-->",
                            "",
                            proposal.payload.new_content,
                        ).strip()
                        asserted = set(report.get("asserted_claim_ids", []))
                        must_keep_ids = {r.id for r in must_keep}
                        missing_must_keep = must_keep_ids - asserted
                        omitted = report.get("omitted_owned_claim_ids", [])
                        omitted_with_reason = {o["id"] for o in omitted if "id" in o and o.get("reason")}
                        unaccounted = missing_must_keep - omitted_with_reason
                        if unaccounted:
                            logger.warning(f"[autowiki_tick] Missing must_keep claims unaccounted for in proposer: {unaccounted}")
                            proposal.gate_passed = False
                            proposal.gate_reason = "missing_must_keep_claims"
                    except Exception as e:
                        pass
                else:
                    proposal.gate_passed = False
                    proposal.gate_reason = "missing_marker_report"
                
        except Exception as exc:
            return _emit_run(
                db, page_id, started_at, proposal_type, h0_struct, None,
                components_before, None, u0_result, None, q0, None,
                "error", f"proposer exception: {exc}",
                None, latency, str(exc),
                idea_signals_json=idea_signals_json,
            )
        latency["proposer_ms"] = _ms(t)

        # ── Step 6: Atom-7B alignment gate ──────────────────────────────────
        if not proposal.gate_passed:
            return _emit_run(
                db, page_id, started_at, proposal_type, h0_struct, None,
                components_before, None, u0_result, None, q0, None,
                "gate_reject", proposal.gate_reason,
                None, latency, None,
                idea_signals_json=idea_signals_json,
            )

        # ── Stage 2A: Certified provenance gate, shadow/no-write by default ──
        if provenance_mode != "off":
            provenance_pairs = _autowiki_provenance_pairs(db, proposal)
            provenance_summary = _record_autowiki_provenance_shadow(
                page_id,
                proposal_type,
                provenance_mode,
                provenance_pairs,
            )
            if idea_signals_json is not None:
                idea_signals_json = {**idea_signals_json, "provenance_shadow": provenance_summary}
            else:
                idea_signals_json = {"provenance_shadow": provenance_summary}

            if provenance_mode == "shadow":
                return _emit_run(
                    db, page_id, started_at, proposal_type, h0_struct, None,
                    components_before, None, u0_result, None, q0, None,
                    "gate_reject",
                    "provenance_shadow_no_write",
                    None, latency, None,
                    idea_signals_json=idea_signals_json,
                )

            if _autowiki_provenance_requires_pairs(proposal_type) and not provenance_pairs:
                return _emit_run(
                    db, page_id, started_at, proposal_type, h0_struct, None,
                    components_before, None, u0_result, None, q0, None,
                    "gate_reject",
                    "provenance_gate_empty_pairs",
                    None, latency, None,
                    idea_signals_json=idea_signals_json,
                )

            if any(not pair["would_admit"] for pair in provenance_pairs):
                return _emit_run(
                    db, page_id, started_at, proposal_type, h0_struct, None,
                    components_before, None, u0_result, None, q0, None,
                    "gate_reject",
                    "provenance_gate_reject",
                    None, latency, None,
                    idea_signals_json=idea_signals_json,
                )

        # ── K2: Takji methodology gate (§9.2.7, default ON) ──────────────────
        _proposed_text = ""
        if isinstance(proposal.payload, ClaimInsertProposal):
            _proposed_text = proposal.payload.claim_text
        elif isinstance(proposal.payload, SectionRewriteProposal):
            _proposed_text = proposal.payload.new_content[:500]
        if _proposed_text:
            _r_k2 = _get_redis()
            if (not _r_k2) or (_r_k2.get("idea_judge:takji_enabled") != "0"):
                t_k2 = time.monotonic()
                takji_verdict = _takji_methodology_check(_proposed_text, claims_text_before)
                latency["k2_takji_ms"] = _ms(t_k2)
                if takji_verdict["verdict"] == "hard_fail":
                    return _emit_run(
                        db, page_id, started_at, proposal_type, h0_struct, None,
                        components_before, None, u0_result, None, q0, None,
                        "gate_reject",
                        f"takji_methodology_fail: {takji_verdict['rationale'][:200]}",
                        None, latency, None,
                        idea_signals_json=idea_signals_json,
                    )

        # ── X4: Atom claim relevance probe (§9.2.8, fire-and-log) ────────────
        try:
            _atom_score_5_random_accepted_claims(db, page_id)
        except Exception as _x4_exc:
            logger.warning("[autowiki] X4 atom probe failed: %s", _x4_exc)

        # ── Step 7: Apply candidate as pending state ─────────────────────────
        t = time.monotonic()
        try:
            if isinstance(proposal.payload, ClaimInsertProposal):
                p = proposal.payload
                new_claim = Claim(
                    page_id=page_id,
                    section=p.section,
                    text=p.claim_text,
                    claim_type=p.claim_type,
                    debate_topic=p.debate_topic,
                    created_by_agent_id=None,
                    order_idx=len(claims),
                )
                db.add(new_claim)
                db.flush()
                claim_ids_inserted.append(new_claim.id)
                for paper in p.papers[:3]:
                    ev = Evidence(
                        claim_id=new_claim.id,
                        arxiv_id=paper.get("arxiv_id"),
                        title=paper.get("title", ""),
                        year=paper.get("year"),
                        abstract=paper.get("abstract") or paper.get("summary"),
                        stance=paper.get("stance", "supports"),
                        quality=paper.get("quality_v2") or paper.get("quality") or 0.50,
                        consensus_scorecard_id=paper.get("consensus_scorecard_id"),
                        relevance=paper.get("relevance"),
                        entailment=paper.get("entailment"),
                        rigor=paper.get("rigor"),
                        confidence=paper.get("confidence"),
                        source_channel="autowiki",
                    )
                    db.add(ev)
                    db.flush()
                    evidence_ids_inserted.append(ev.id)

            elif isinstance(proposal.payload, EvidenceLinkProposal):
                p = proposal.payload
                for paper in p.papers[:3]:
                    ev = Evidence(
                        claim_id=p.claim_id,
                        arxiv_id=paper.get("arxiv_id"),
                        title=paper.get("title", ""),
                        year=paper.get("year"),
                        abstract=paper.get("abstract") or paper.get("summary"),
                        stance=paper.get("stance", "supports"),
                        quality=paper.get("quality_v2") or paper.get("quality") or 0.50,
                        consensus_scorecard_id=paper.get("consensus_scorecard_id"),
                        relevance=paper.get("relevance"),
                        entailment=paper.get("entailment"),
                        rigor=paper.get("rigor"),
                        confidence=paper.get("confidence"),
                        source_channel="autowiki",
                    )
                    db.add(ev)
                    db.flush()
                    evidence_ids_inserted.append(ev.id)

            elif isinstance(proposal.payload, HeroUpgradeProposal):
                p = proposal.payload
                try:
                    facts = json.loads(page.hero_facts) if page.hero_facts else []
                except Exception:
                    facts = []
                if p.replace_index is not None and p.replace_index < len(facts):
                    facts[p.replace_index] = p.new_hero_fact
                else:
                    facts.append(p.new_hero_fact)
                page.hero_facts = json.dumps(facts)

            elif isinstance(proposal.payload, SectionRewriteProposal):
                p = proposal.payload
                # Save prior version
                last_ver = (
                    db.query(PageVersion)
                    .filter(PageVersion.page_id == page_id)
                    .order_by(PageVersion.id.desc())
                    .first()
                )
                prior_page_version_id = last_ver.id if last_ver else None
                # Replace section in content
                import re
                pattern = rf"(## {re.escape(p.section_header)}.*?)(?=^## |\Z)"
                # Use a lambda replacement to prevent Python re.sub from parsing backslashes (e.g. \s, \alpha) in the new content
                new_content = re.sub(
                    pattern, lambda m: p.new_content + "\n\n", page.content,
                    count=1, flags=re.MULTILINE | re.DOTALL,
                )
                new_content = re.sub(r"<!--marker-report.*?-->", "", new_content, flags=re.DOTALL)
                new_content = re.sub(r"<!--unmatched-citation-->", "", new_content)
                from app.services.content_canonicalizer import canonicalize
                new_content = canonicalize(new_content, page_id=page_id, db=db).new_content
                page.content = new_content
                # Write new PageVersion
                next_num = (last_ver.version_num + 1) if last_ver else 1
                new_pv = PageVersion(
                    page_id=page_id,
                    version_num=next_num,
                    content=new_content,
                )
                db.add(new_pv)
                db.flush()

        except Exception as exc:
            db.rollback()
            return _emit_run(
                db, page_id, started_at, proposal_type, h0_struct, None,
                components_before, None, u0_result, None, q0, None,
                "error", f"apply exception: {exc}",
                None, latency, str(exc),
                idea_signals_json=idea_signals_json,
            )
        latency["apply_ms"] = _ms(t)

        # ── Step 8: Optimistic concurrency + H1_struct guard ──────────────
        # Reload claims after pending inserts
        db.flush()
        claims_after = db.query(Claim).filter(Claim.page_id == page_id).all()
        hash_after_apply = _page_hash(page, claims_after)
        if hash_after_apply == hash_before and proposal_type not in (
            "evidence_link", "hero_upgrade"
        ):
            # Page unchanged by proposer (content-equality check, rare)
            pass  # proceed — may still affect claims

        t = time.monotonic()
        h1_result = compute_health_score(page, db)
        latency["h1_struct_ms"] = _ms(t)
        h1_struct = h1_result["score"]
        components_after = h1_result["components"]

        # Guard: no structural component may drop by > 0.05
        for dim, v0 in components_before.items():
            v1 = components_after.get(dim, v0)
            if v0 - v1 > 0.05:
                # Hard guard triggered — rollback pending state
                _do_rollback(
                    db, page, proposal_type, claim_ids_inserted,
                    evidence_ids_inserted, prior_hero_facts, prior_page_version_id,
                )
                return _emit_run(
                    db, page_id, started_at, proposal_type, h0_struct, h1_struct,
                    components_before, components_after, u0_result, None, q0, None,
                    "guard_reject", f"component {dim} dropped {v0 - v1:.3f} > 0.05",
                    None, latency, None,
                    idea_signals_json=idea_signals_json,
                )

        if h0_struct - h1_struct > 0.5:
            _do_rollback(
                db, page, proposal_type, claim_ids_inserted,
                evidence_ids_inserted, prior_hero_facts, prior_page_version_id,
            )
            return _emit_run(
                db, page_id, started_at, proposal_type, h0_struct, h1_struct,
                components_before, components_after, u0_result, None, q0, None,
                "guard_reject", f"struct dropped {h0_struct - h1_struct:.1f} > 0.5",
                None, latency, None,
                idea_signals_json=idea_signals_json,
            )

        # ── Step 9: Judge pending state via Rakon × 3, median U1 ──────────
        t = time.monotonic()
        claims_text_after = _claims_text(claims_after)
        u1_result = judge_page(
            page_id=page_id,
            content=page.content,
            hero_facts=page.hero_facts,
            claims_text=claims_text_after,
            force=True,  # never use cache for the candidate state
        )
        latency["u1_judge_ms"] = _ms(t)
        u1 = u1_result.utility
        q1 = compute_quality(h1_struct, u1)
        delta_q = round(q1 - q0, 4)

        # ── Step 10: COMMIT iff Δq ≥ 0.02 ──────────────────────────────────
        if delta_q >= 0.02:
            decision = "commit"
            # Persist pending state
            new_version_id: int | None = None
            if proposal_type == "section_rewrite":
                last_pv = (
                    db.query(PageVersion)
                    .filter(PageVersion.page_id == page_id)
                    .order_by(PageVersion.id.desc())
                    .first()
                )
                new_version_id = last_pv.id if last_pv else None
            page.updated_at = dt.datetime.utcnow()
            db.flush()

            # Auto-raise target (§7 decision 4)
            target_row = db.query(AutowikiTarget).filter(
                AutowikiTarget.page_id == page_id
            ).first()
            if target_row and q1 >= target_row.target_q - 0.03:
                target_row.target_q = min(1.0, target_row.target_q + 0.05)
                target_row.last_raised_at = dt.datetime.utcnow()

            run = _build_run(
                page_id, started_at, proposal_type, h0_struct, h1_struct,
                components_before, components_after, u0_result, u1_result,
                q0, q1, delta_q, decision, None, new_version_id,
                latency, None,
                idea_signals_json=idea_signals_json,
            )
            db.add(run)
            from app.agent_loop.agent_ping import mark_celery_agent_active
            mark_celery_agent_active(db, _ASTROSAGE)
            db.commit()
            print(
                f"[autowiki] COMMIT page={page_id} type={proposal_type} "
                f"Q0={q0:.3f}→Q1={q1:.3f} Δ={delta_q:+.3f}"
            )

            # ── Post-commit: Marker re-embed is now handled asynchronously by the Celery chain (Stage 2) ──
            logger.info("[autowiki] Skipping synchronous claim_marker_embed_page; delegated to Celery chain Stage 2")

            # ── Post-commit: fire research ideas trigger ─────────────────────────────
            from app.agent_loop.research_ideas.auto_improvement import process_lightweight_event
            try:
                import redis as _redis_lib
                from app.config import settings as _s
                _r = _redis_lib.from_url(_s.REDIS_URL, decode_responses=True)
                _phase3_on = _r.get("research_ideas:phase3_enabled") == "1"
            except Exception:
                _phase3_on = False

            if _phase3_on:
                if proposal_type in ("claim_insert", "claim_insert_subtopic", "claim_insert_debate") and claim_ids_inserted:
                    process_lightweight_event.delay(
                        page_id, "claim_inserted", str(claim_ids_inserted[0])
                    )
                elif proposal_type == "evidence_link" and evidence_ids_inserted:
                    process_lightweight_event.delay(
                        page_id, "evidence_linked", str(evidence_ids_inserted[0])
                    )
                elif proposal_type == "section_rewrite":
                    process_lightweight_event.delay(
                        page_id, "section_rewritten", None
                    )
                # §16: fire debated-claim seeder immediately when a claim is marked debated/challenged
                if proposal_type == "claim_insert_debate" and claim_ids_inserted:
                    from app.agent_loop.research_ideas.auto_improvement import seed_debated_claim_ideas
                    seed_debated_claim_ideas.delay(page_id=page_id, target_per_claim=3)
        else:
            decision = "rollback"
            reject_reason = f"Δq={delta_q:+.4f} < 0.02"
            _do_rollback(
                db, page, proposal_type, claim_ids_inserted,
                evidence_ids_inserted, prior_hero_facts, prior_page_version_id,
            )
            run = _build_run(
                page_id, started_at, proposal_type, h0_struct, h1_struct,
                components_before, components_after, u0_result, u1_result,
                q0, q1, delta_q, decision, reject_reason, None,
                latency, None,
                idea_signals_json=idea_signals_json,
            )
            db.add(run)
            db.commit()
            print(
                f"[autowiki] ROLLBACK page={page_id} type={proposal_type} "
                f"Q0={q0:.3f}→Q1={q1:.3f} Δ={delta_q:+.3f}"
            )

        latency["total_ms"] = _ms(tick_start)
        return {
            "decision": decision,
            "page_id": page_id,
            "proposal_type": proposal_type,
            "q0": q0,
            "q1": q1,
            "delta_q": delta_q,
        }


# ---------------------------------------------------------------------------
# Rollback dispatcher
# ---------------------------------------------------------------------------

def _do_rollback(
    db,
    page: WikiPage,
    proposal_type: str,
    claim_ids: list[int],
    evidence_ids: list[int],
    prior_hero_facts: str | None,
    prior_version_id: int | None,
) -> None:
    try:
        if proposal_type in ("claim_insert_subtopic", "claim_insert_debate"):
            _rollback_claim_insert(db, claim_ids, evidence_ids)
        elif proposal_type == "evidence_link":
            _rollback_evidence_link(db, evidence_ids)
        elif proposal_type == "hero_upgrade":
            _rollback_hero_upgrade(page, prior_hero_facts)
        elif proposal_type == "section_rewrite" and prior_version_id is not None:
            _rollback_section_rewrite(db, page, prior_version_id)
        db.flush()
    except Exception as e:
        print(f"[autowiki] rollback error: {e}")


# ---------------------------------------------------------------------------
# Run record helpers
# ---------------------------------------------------------------------------

def _build_run(
    page_id, started_at, proposal_type, h0, h1,
    comp_before, comp_after, u0_result, u1_result,
    q0, q1, delta_q, decision, reject_reason, committed_version_id,
    latency, error_text,
    idea_signals_json=None,
) -> AutowikiRun:
    return AutowikiRun(
        page_id=page_id,
        started_at=started_at,
        finished_at=dt.datetime.utcnow(),
        proposal_type=proposal_type,
        model_proposer=_ASTROSAGE,
        model_judge=u1_result.model_used if u1_result else None,
        h0_struct=h0,
        h1_struct=h1,
        components_before=comp_before,
        components_after=comp_after,
        u0_median=u0_result.utility if u0_result else None,
        u1_median=u1_result.utility if u1_result else None,
        u0_runs=u0_result.raw_scores if u0_result else None,
        u1_runs=u1_result.raw_scores if u1_result else None,
        judge_rationale=(u1_result.rationale if u1_result else None)
        or (u0_result.rationale if u0_result else None),
        judge_prompt_version=PROMPT_VERSION,
        q0=q0,
        q1=q1,
        delta_q=delta_q,
        decision=decision,
        reject_reason=reject_reason,
        committed_version_id=committed_version_id,
        latency_ms_breakdown=latency,
        error_text=error_text,
        idea_signals_json=idea_signals_json,
    )


def _emit_run(
    db, page_id, started_at, proposal_type, h0, h1,
    comp_before, comp_after, u0_result, u1_result,
    q0, q1, decision, reject_reason, committed_version_id,
    latency, error_text,
    idea_signals_json=None,
) -> dict:
    """Write an autowiki_runs row and return a summary dict."""
    delta_q = round(q1 - q0, 4) if q1 is not None and q0 is not None else None
    run = _build_run(
        page_id, started_at, proposal_type, h0, h1,
        comp_before, comp_after, u0_result, u1_result,
        q0, q1, delta_q, decision, reject_reason, committed_version_id,
        latency, error_text,
        idea_signals_json=idea_signals_json,
    )
    db.add(run)
    db.commit()
    return {
        "decision": decision,
        "reject_reason": reject_reason,
        "page_id": page_id,
        "proposal_type": proposal_type,
    }


# ---------------------------------------------------------------------------
# v3: Sonnet active section rewrite proposer (§3.3)
# ---------------------------------------------------------------------------

_SONNET_SECTION_SYSTEM = (
    "You are an expert astronomy wiki editor writing at graduate-textbook depth. "
    "Rewrite the given section with maximum scientific specificity. "
    "Return markdown followed by a JSON marker report. "
    "HARD REQUIREMENTS — violating any disqualifies the response:\n"
    "  1. Minimum 400 words below the ## header.\n"
    "  2. At least 3 quantitative facts: redshifts, masses, luminosities, "
    "percentages, timescales, temperatures, or distances with units.\n"
    "  3. Do not write author-year parenthetical citations. Use only <!--cite:EVIDENCE_ID--> markers from the EVIDENCE MAP.\n"
    "  4. BANNED phrases: 'plays a crucial role', 'complex and dynamic', "
    "'plays an important role', 'is a fascinating', 'remains to be seen', "
    "'future work will', 'this page covers', 'in conclusion'.\n"
    "  5. You MUST weave HTML claim markers (e.g. <!--claim:123-->) inline immediately after asserting any of the provided 'owned' claims.\n"
    "  6. You MUST PRESERVE all trust/consensus HTML comments (e.g. <!--accepted-->, <!--consensus-->).\n"
    "  7. MUST output a valid JSON report at the end wrapped in <!--marker-report ... -->.\n"
    "  8. You MUST include and assert EVERY 'Must-Keep Owned Claim'. DO NOT omit them.\n"
    "  9. Do NOT use raw LaTeX math syntax (e.g. `$...$`, `\\Sigma`, `\\gtrsim`). Use plain text or Unicode for mathematical expressions; avoid dollar signs, backslash commands, and star/sun symbols in prose.\n"
)
_SONNET_MAX_Q_REGRESSION = 0.03


def _normalize_sonnet_plain_math(text: str) -> str:
    """Convert common raw LaTeX fragments from Sonnet into canonicalizer-safe prose."""
    replacements = {
        r"\gtrsim": ">=",
        r"\lesssim": "<=",
        r"\geq": ">=",
        r"\ge": ">=",
        r"\leq": "<=",
        r"\le": "<=",
        r"\approx": "about",
        r"\sim": "~",
        r"\propto": "proportional to",
        r"\times": "x",
        r"\pm": "+/-",
        r"\Sigma": "Sigma",
        r"\sigma": "sigma",
        r"\Delta": "Delta",
        r"\Omega": "Omega",
        r"\Lambda": "Lambda",
        r"\rho": "rho",
        r"\mu": "mu",
        r"\pi": "pi",
        r"\star": "star",
        r"\odot": "sun",
    }
    for raw, plain in replacements.items():
        text = text.replace(raw, plain)
    text = text.replace("\\,", " ")
    text = re.sub(r"\$(.*?)\$", r"\1", text)
    text = re.sub(r"\b([A-Za-z]+)_\{?([A-Za-z]+)\}?", r"\1-\2", text)
    text = text.replace("{", "").replace("}", "")
    text = re.sub(r"\s{2,}", " ", text)
    return text


@celery_app.task(
    name="app.agent_loop.autowiki.tasks.sonnet_section_rewrite",
    bind=True, max_retries=0,
)
def sonnet_section_rewrite(self, page_id: int, target_section: str = None):
    """v3 §3.3: Sonnet (claude-sonnet-4-6) writes section rewrites A/B with AstroSage."""
    import re
    import datetime as _dt
    from app.config import settings
    from app.models.autowiki import AutowikiRun
    from app.services.content_canonicalizer import CanonicalizerError, canonicalize

    if not _is_enabled():
        return {"decision": "skip", "reason": "autowiki_flag_off"}
    if _autowiki_provenance_gate_mode() == "enforce":
        return {
            "decision": "skip",
            "reason": "provenance_enforce_suppressed_direct_section_rewrite",
            "page_id": page_id,
        }

    started_at = _dt.datetime.utcnow()

    db = SessionLocal()

    def _log_error_run(error_text: str) -> None:
        try:
            run = AutowikiRun(
                page_id=page_id,
                started_at=started_at,
                finished_at=_dt.datetime.utcnow(),
                proposal_type="section_rewrite",
                model_proposer="claude-sonnet-4-6",
                decision="error",
                error_text=error_text,
            )
            db.add(run)
            db.commit()
        except Exception as log_exc:
            db.rollback()
            logger.warning("[sonnet_section_rewrite] failed to write error run: %s", log_exc)

    try:
        page = db.query(WikiPage).filter(WikiPage.id == page_id).first()
        if not page:
            return {"decision": "error", "reason": "page_not_found"}

        program = load_program(page.slug)
        # Get claims for context
        from app.models.claim import Claim as ClaimModel


        # Pick section (round-robin)
        sections = re.findall(r"^## (.+)$", page.content, re.MULTILINE)
        if not sections:
            return {"decision": "skip", "reason": "no_sections"}
        from sqlalchemy import func as _func
        rewrite_count = (
            db.query(_func.count(AutowikiRun.id))
            .filter(
                AutowikiRun.page_id == page_id,
                AutowikiRun.proposal_type == "section_rewrite",
                AutowikiRun.model_proposer == "claude-sonnet-4-6",
            )
            .scalar() or 0
        )
        if target_section:
            _matched = [s for s in sections if target_section.lower() in s.lower()]
            section_header = _matched[0] if _matched else sections[rewrite_count % len(sections)]
        else:
            section_header = sections[rewrite_count % len(sections)]

        # §2.1: skip sections that are already near-peak quality (avoids tiny-negative-dq drift)
        recent_q1_row = (
            db.query(AutowikiRun.q1)
            .filter(
                AutowikiRun.page_id == page_id,
                AutowikiRun.proposal_type.in_(["section_rewrite", "sonnet_audit"]),
                AutowikiRun.q1.isnot(None),
                AutowikiRun.judge_rationale.ilike(f"%{section_header}%"),
            )
            .order_by(AutowikiRun.id.desc())
            .first()
        )
        if recent_q1_row and recent_q1_row[0] is not None and recent_q1_row[0] >= 0.90:
            run = AutowikiRun(
                page_id=page_id, started_at=started_at, finished_at=_dt.datetime.utcnow(),
                proposal_type="section_rewrite", model_proposer="claude-sonnet-4-6",
                decision="skip",
                reject_reason=f"section already high quality (q1={recent_q1_row[0]:.3f} ≥ 0.90)",
            )
            db.add(run)
            db.commit()
            return {"decision": "skip", "reason": "section_high_quality", "q1": recent_q1_row[0]}

        # Extract current section
        section_lines: list[str] = []
        in_section = False
        for line in page.content.split("\n"):
            if line.startswith("## ") and section_header in line:
                in_section = True
            elif line.startswith("## ") and in_section:
                break
            if in_section:
                section_lines.append(line)
        current_section = "\n".join(section_lines[:50])
        
        from sqlalchemy import text
        sec_key = re.sub(r'_+', '_', re.sub(r'[^a-z0-9\s]', '', current_section.split('\n')[0].replace('##', '').strip().lower()).replace(' ', '_')).strip('_')
        owned_res = db.execute(text("""
            SELECT c.id, c.trust_level, c.text 
            FROM claim_section_assignments a
            JOIN claims c ON c.id = a.claim_id
            WHERE a.page_id = :pid AND a.owner_section_key = :sec_key AND a.assignment_status = 'active'
        """), {"pid": page_id, "sec_key": sec_key}).fetchall()
        
        must_keep = [r for r in owned_res if r.trust_level in ('accepted', 'consensus')]
        optional = [r for r in owned_res if r.trust_level not in ('accepted', 'consensus')]
        
        claims_text = "Must-Keep Owned Claims:\n" + "\n".join(f"<!--claim:{c.id}--> [{c.trust_level}] {c.text[:200]}" for c in must_keep) + "\n\n"
        claims_text += "Optional Owned Claims:\n" + "\n".join(f"<!--claim:{c.id}--> [{c.trust_level}] {c.text[:200]}" for c in optional)
        evidence_map = build_evidence_map(db, page_id, max_rows=50, section=section_header)


        user_msg = (
            f"Program:\n{program[:400]}\n\n"
            f"{evidence_map}\n\n"
            f"Current section:\n{current_section}\n\n"
            f"Owned claims for this section:\n{claims_text}\n\n"
            "Rewrite this section following the requirements in the system prompt. "
            "Keep the ## header unchanged.\n\n"
            "Citation requirements: do not write (Author et al. Year). Use <!--cite:EVIDENCE_ID--> only from the EVIDENCE MAP. Omit a citation if no evidence ID is available.\n\n"
            "Math notation requirement: do NOT use raw LaTeX math syntax such as `$...$`, `\\Sigma`, or `\\gtrsim`. Use plain text or Unicode instead.\n\n"
            "At the end of your response, you MUST include exactly one marker report in exactly this format. Do not omit it, do not wrap it in a code fence, and do not place any text after it:\n"
            "<!--marker-report\n{\n  \"section\": \"Section Name\",\n  \"asserted_claim_ids\": [123, 124],\n  \"omitted_owned_claim_ids\": [{\"id\": 126, \"reason\": \"not asserted\"}]\n}\n-->"
        )

        try:
            import anthropic
            client = anthropic.Anthropic(api_key=settings.ANTHROPIC_API_KEY)
            est_tokens = {"input": max(1, (len(_SONNET_SECTION_SYSTEM) + len(user_msg)) // 4), "output": 2048}
            dispatch_premium("autowiki.sonnet_section_rewrite", "claude-sonnet-4-6", est_tokens)
            response = client.messages.create(
                model="claude-sonnet-4-6",
                max_tokens=2048,
                system=_SONNET_SECTION_SYSTEM,
                messages=[{"role": "user", "content": user_msg}],
                temperature=0.7,
            )
            usage = getattr(response, "usage", None)
            log_llm_spend(
                "autowiki.sonnet_section_rewrite",
                "claude-sonnet-4-6",
                prompt_tokens=getattr(usage, "input_tokens", None),
                completion_tokens=getattr(usage, "output_tokens", None),
                cache_creation_tokens=getattr(usage, "cache_creation_input_tokens", None),
                cache_read_tokens=getattr(usage, "cache_read_input_tokens", None),
                estimated_tokens=est_tokens["input"],
            )
            new_section_text = response.content[0].text.strip()
        except Exception as exc:
            logger.warning("[sonnet_section_rewrite] API call failed: %s", exc)
            run = AutowikiRun(
                page_id=page_id, started_at=started_at, finished_at=_dt.datetime.utcnow(),
                proposal_type="section_rewrite", model_proposer="claude-sonnet-4-6",
                decision="error", error_text=str(exc),
            )
            db.add(run)
            db.commit()
            return {"decision": "error", "reason": str(exc)}

        logger.info(f"Sonnet response raw text length: {len(new_section_text)}")
        if '<!--marker-report' not in new_section_text:
            logger.info("NO MARKER REPORT FOUND IN TEXT. Prompt might be ignored or model refused.")
            logger.info(new_section_text[-500:])

        if len(new_section_text) < 100:
            run = AutowikiRun(
                page_id=page_id, started_at=started_at, finished_at=_dt.datetime.utcnow(),
                proposal_type="section_rewrite", model_proposer="claude-sonnet-4-6",
                decision="gate_reject", reject_reason="output too short",
            )
            db.add(run)
            db.commit()
            return {"decision": "gate_reject", "reason": "output_too_short"}

        report_match = re.search(r"<!--marker-report\s*({.*?})\s*-->", new_section_text, re.DOTALL)
        if report_match:
            try:
                import json
                report = json.loads(report_match.group(1))
                asserted = set(report.get("asserted_claim_ids", []))
                must_keep_ids = {r.id for r in must_keep}
                missing_must_keep = must_keep_ids - asserted
                if missing_must_keep:
                    logger.warning(f"[sonnet_section_rewrite] Missing must_keep claims: {missing_must_keep}. Rejecting.")
                    return {"decision": "skip", "reject_reason": "missing_must_keep_claims"}
            except Exception as e:
                pass
        else:
            logger.warning("[sonnet_section_rewrite] Missing marker report, but continuing anyway for debug")
            
        new_section_text = re.sub(r"<!--marker-report.*?-->", "", new_section_text, flags=re.DOTALL).strip()
        # Strip any raw claim/topic markers the model leaked from the prompt's owned-claims list.
        # Authoritative markers come from the marker_embed re-embed pipeline; unpaired or duplicate
        # markers here have corrupted the global validator (Page 57 2026-06-02).
        new_section_text = re.sub(r"<!--/?claim:\d+-->", "", new_section_text)
        new_section_text = re.sub(r"<!--topic:\d+-->", "", new_section_text)
        new_section_text = _normalize_sonnet_plain_math(new_section_text)

        if not new_section_text.startswith("## "):
            new_section_text = f"## {section_header}\n\n{new_section_text}"

        # Rebuild page content
        new_parts: list[str] = []
        in_sec = False
        replaced = False
        for line in page.content.split("\n"):
            if line.startswith("## ") and section_header in line and not replaced:
                in_sec = True
                new_parts.append(new_section_text)
                replaced = True
            elif line.startswith("## ") and in_sec:
                in_sec = False
                new_parts.append(line)
            elif not in_sec:
                new_parts.append(line)
        new_content = "\n".join(new_parts)

        if not replaced:
            return {"decision": "error", "reason": "section_not_found"}

        # Commit gates: require minimum length and a lightweight pre-commit
        # quality check. Sonnet writes outside the AstroSage gated lane, so
        # page 57 must not land a section rewrite that regresses q by > 0.03.
        section_body = new_section_text.split("\n", 1)[-1] if "\n" in new_section_text else ""
        if len(section_body.strip()) < 200:
            run = AutowikiRun(
                page_id=page_id, started_at=started_at, finished_at=_dt.datetime.utcnow(),
                proposal_type="section_rewrite", model_proposer="claude-sonnet-4-6",
                decision="gate_reject", reject_reason="section body < 200 chars after header",
            )
            db.add(run)
            db.commit()
            return {"decision": "gate_reject", "reason": "body_too_short"}

        # Snapshot current content into page_versions before writing so that
        # a future autowiki_tick rollback can restore past this commit (not before it).
        canonicalized = canonicalize(new_content, page_id=page_id, db=db)
        if canonicalized.violations:
            raise CanonicalizerError(canonicalized.violations)
        new_content = canonicalized.new_content

        claims_for_gate = (
            db.query(Claim)
            .filter(Claim.page_id == page_id)
            .order_by(Claim.created_at)
            .all()
        )
        claims_text_for_gate = _claims_text(claims_for_gate)
        h0_result = compute_health_score(page, db)
        h0_struct = h0_result["score"]
        components_before = h0_result["components"]
        u0_result = judge_page(
            page_id=page_id,
            content=page.content,
            hero_facts=page.hero_facts,
            claims_text=claims_text_for_gate,
            force=True,
        )
        q0 = compute_quality(h0_struct, u0_result.utility)
        u1_result = judge_page(
            page_id=page_id,
            content=new_content,
            hero_facts=page.hero_facts,
            claims_text=claims_text_for_gate,
            force=True,
        )
        # Section-only rewrites do not alter claim/evidence rows before commit,
        # so structural health is unchanged until marker re-embed follows.
        h1_struct = h0_struct
        components_after = components_before
        q1 = compute_quality(h1_struct, u1_result.utility)
        delta_q = round(q1 - q0, 4)
        if q1 < q0 - _SONNET_MAX_Q_REGRESSION:
            run = AutowikiRun(
                page_id=page_id,
                started_at=started_at,
                finished_at=_dt.datetime.utcnow(),
                proposal_type="section_rewrite",
                model_proposer="claude-sonnet-4-6",
                model_judge=u1_result.model_used,
                h0_struct=h0_struct,
                h1_struct=h1_struct,
                components_before=components_before,
                components_after=components_after,
                u0_median=u0_result.utility,
                u1_median=u1_result.utility,
                u0_runs=u0_result.raw_scores,
                u1_runs=u1_result.raw_scores,
                judge_rationale=u1_result.rationale or u0_result.rationale,
                judge_prompt_version=PROMPT_VERSION,
                q0=q0,
                q1=q1,
                delta_q=delta_q,
                decision="gate_reject",
                reject_reason=(
                    f"sonnet_quality_regression: q1={q1:.4f} < "
                    f"q0-{_SONNET_MAX_Q_REGRESSION:.2f} ({q0 - _SONNET_MAX_Q_REGRESSION:.4f})"
                ),
            )
            db.add(run)
            db.commit()
            return {
                "decision": "gate_reject",
                "reason": "sonnet_quality_regression",
                "q0": q0,
                "q1": q1,
                "delta_q": delta_q,
            }

        last_pv = (
            db.query(PageVersion)
            .filter(PageVersion.page_id == page_id)
            .order_by(PageVersion.id.desc())
            .first()
        )
        next_vnum = (last_pv.version_num + 1) if last_pv else 1
        pv_snapshot = PageVersion(page_id=page_id, version_num=next_vnum, content=new_content)
        db.add(pv_snapshot)
        db.flush()

        page.content = new_content
        page.updated_at = _dt.datetime.utcnow()

        run = AutowikiRun(
            page_id=page_id, started_at=started_at, finished_at=_dt.datetime.utcnow(),
            proposal_type="section_rewrite", model_proposer="claude-sonnet-4-6",
            decision="commit",
            judge_rationale=f"sonnet_section section='{section_header}' body_len={len(section_body)}",
            judge_prompt_version="sonnet_section_v1",
            model_judge=u1_result.model_used,
            h0_struct=h0_struct,
            h1_struct=h1_struct,
            components_before=components_before,
            components_after=components_after,
            u0_median=u0_result.utility,
            u1_median=u1_result.utility,
            u0_runs=u0_result.raw_scores,
            u1_runs=u1_result.raw_scores,
            q0=q0,
            q1=q1,
            delta_q=delta_q,
        )
        # MARKER_REEMBED_REQUIRED: re-derive claim markers against new prose
        try:
            from app.agent_loop.marker_embed.tasks import emit_reembed
            emit_reembed(page_id)
        except Exception:
            pass
        db.add(run)
        db.flush()

        # Dispatch J1 so Nutty generates research ideas from this commit
        try:
            from app.agent_loop.research_ideas.auto_improvement import process_lightweight_event
            _r = _get_redis()
            if _r and _r.get("research_ideas:phase3_enabled") == "1":
                process_lightweight_event.delay(page_id, "section_rewritten", None)
        except Exception as _j1_exc:
            logger.debug("[sonnet_section_rewrite] J1 dispatch failed: %s", _j1_exc)

        from app.agent_loop.agent_ping import mark_celery_agent_active
        mark_celery_agent_active(db, "claude-sonnet-4-6")
        db.commit()
        emit_citation_scrub_required(page_id)
        logger.info(
            "[sonnet_section_rewrite] page=%d section='%s' body_len=%d committed",
            page_id, section_header, len(section_body),
        )
        return {"decision": "commit", "page_id": page_id, "section": section_header}
    except CanonicalizerError as exc:
        db.rollback()
        logger.exception("[sonnet_section_rewrite] canonicalizer failed: %s", exc)
        _log_error_run(str(exc))
        return {"decision": "error", "reason": str(exc)}
    except Exception as exc:
        db.rollback()
        logger.exception("[sonnet_section_rewrite] failed: %s", exc)
        _log_error_run(str(exc))
        raise
    finally:
        db.close()


# ---------------------------------------------------------------------------
# Rakon Coherence Pass — full-page coherence rewrite via deepseek-r1:671b
# ---------------------------------------------------------------------------

_COHERENCE_SYSTEM_PROMPT = 'You are Rakon, a senior astronomy reviewer with deep expertise in galaxy evolution. You are restructuring a Wikipedia-style review article assembled by four different agents over five days. The result is fragmented, duplicative, and inconsistent in voice. Your job: produce a single coherent rewrite with a unified review-article voice, no duplicate content, and clean transitions between sections.\n\nCRITICAL ORGANIZING PRINCIPLE: The structure must be physically and scientifically organized. Observational evidence belongs EMBEDDED WITHIN each physical topic section — not isolated in a standalone observations section. Write like a graduate-level textbook chapter: state the physics, then immediately support it with the relevant observations (SDSS, JWST, ALMA, MaNGA, CANDELS, etc.) inline. There must be NO dedicated "Observational Evidence" H2 section.\n\nYou are NOT adding new scientific claims. You are NOT inventing new citations. You are restructuring existing content with better organization and prose.'

_COHERENCE_USER_TEMPLATE = '''CRITICAL: You MUST use these EXACT H2 header strings, character-for-character. Do not paraphrase or modify them.\n\nTARGET STRUCTURE (9 H2 sections, in this order):\n\n1. ## Overview & Historical Context\n2. ## Galaxy Formation & Dark Matter Halos\n   ### Hierarchical Assembly and Halo Mass Functions\n   ### The Stellar-to-Halo Mass Relation\n   ### Cold Streams vs Hot Accretion\n3. ## Star Formation & Gas Physics\n   ### The Star-Forming Main Sequence\n   ### Molecular Gas Reservoirs and Kennicutt-Schmidt\n   ### Stellar Feedback and Self-Regulation\n4. ## Quenching Mechanisms\n   ### AGN Feedback: Radiative and Kinetic Modes\n   ### Stellar Feedback and Supernova-Driven Winds\n   ### Strangulation, Starvation, and Halo Heating\n   ### The M–σ Relation and AGN Co-evolution\n5. ## Environmental Effects & Galaxy Clusters\n   ### The Morphology-Density Relation\n   ### Ram-Pressure Stripping\n   ### Tidal Interactions, Harassment, and Mergers\n6. ## Structural Evolution\n   ### Morphological Transformation and the Hubble Sequence\n   ### Galaxy Scaling Relations: Tully-Fisher and Faber-Jackson\n   ### Size Growth and the Two-Phase Assembly Picture\n7. ## Chemical Enrichment & Stellar Populations\n   ### The Mass-Metallicity Relation\n   ### α-element Abundances and Star Formation Timescales\n   ### Stellar Population Gradients from IFU Surveys\n8. ## High-Redshift Universe & Cosmic Star Formation History\n   ### Cosmic Star Formation Rate Density\n   ### Early Massive Galaxies and JWST Discoveries\n   ### Color Bimodality Evolution: Red Sequence Growth Since z∼2\n9. ## Open Questions & Future Directions\n   (one concise paragraph per open debate, drawn from the page\'s contested claims)\n\nBelow is the current state of the wiki page. Rewrite it as a coherent review article using the EXACT target structure provided above.\n\nHARD CONSTRAINTS:\n- Preserve all substantive claims (rephrase OK, delete NOT OK).\n- DO NOT write inline citations in (Author et al. Year) format. Evidence is linked via <!--cite:N--> markers.\n- When asserting a claim backed by a specific paper, insert <!--cite:EVIDENCE_ID--> immediately after the assertion using only IDs from the EVIDENCE MAP. If no evidence ID is available, omit the citation.\n- Preserve all quantitative facts (z, M_☉, slopes, fractions, dates). Do not modify.\n- Observational evidence (surveys, instruments, datasets) must be embedded WITHIN the relevant physical section — NEVER grouped into a standalone observations H2.\n- Single unified voice: authoritative astronomy review article. Concrete prose.\n- Transitions: last sentence of each section connects substantively forward.\n- DO NOT invent new claims, datasets, instruments, citations, or evidence IDs.\n- DO NOT add a hero tagline (separate task).\n- PRESERVE ANY EXISTING HTML claim markers (e.g. <!--claim:123-->).\n- Weave HTML claim markers inline where you assert key claims from the list provided below.\n\nOUTPUT FORMAT:\n- Markdown. H1: `# Galaxy Evolution` (keep verbatim). Then H2 sections in order above.\n- H3 sub-sections as listed (adjust names slightly if needed for flow, but keep section count = 9).\n- DO NOT include a `## References` or bibliography section — evidence is surfaced dynamically.\n- Single newline between paragraphs; double newline before headings.\n- Target length: 65,000–80,000 chars.\n\n{citation_context}\n\nCURRENT PAGE CONTENT:\n=====================================\n\n{full_page_content}\n\nNow produce the rewritten page.'''

_COHERENCE_EXPECTED_SECTIONS = ['## Overview & Historical Context', '## Galaxy Formation & Dark Matter Halos', '## Star Formation & Gas Physics', '## Quenching Mechanisms', '## Environmental Effects & Galaxy Clusters', '## Structural Evolution', '## Chemical Enrichment & Stellar Populations', '## High-Redshift Universe & Cosmic Star Formation History', '## Open Questions & Future Directions']


@celery_app.task(
    name="app.agent_loop.autowiki.tasks.run_rakon_coherence_pass",
    bind=True,
    max_retries=0,
    task_acks_late=True,
    queue="autowiki",
    time_limit=32400,    # 9h hard kill
    soft_time_limit=30000,  # ~8.3h soft
)
def run_rakon_coherence_pass(self, page_id: int) -> dict:
    """Full-page coherence rewrite using Claude claude-opus-4-8 via Anthropic API."""
    import json as _json
    import time as _time
    import datetime as _dt

    if _autowiki_provenance_gate_mode() == "enforce":
        return {
            "decision": "skip",
            "reason": "provenance_enforce_suppressed_direct_coherence_rewrite",
            "page_id": page_id,
        }

    logger.info("[coherence] Starting Opus coherence pass page=%d", page_id)

    started_at = _dt.datetime.utcnow()
    t0 = _time.monotonic()

    with SessionLocal() as db:
        # do_not_renovate guard: skip and release lock immediately if set
        _dnr_row = db.execute(
            __import__("sqlalchemy").text(
                "SELECT do_not_renovate FROM wiki_pages WHERE id = :pid"
            ),
            {"pid": page_id},
        ).fetchone()
        if _dnr_row and _dnr_row[0]:
            logger.warning(
                "[coherence] page=%d has do_not_renovate=True — skipping coherence pass",
                page_id,
            )
            try:
                _rc = _get_redis()
                if _rc:
                    _rc.delete(f"autowiki:coherence_dispatched:{page_id}")
                    _rc.delete(f"autowiki:coherence_needed:{page_id}")
            except Exception:
                pass
            return {"decision": "skip", "reject_reason": "do_not_renovate"}

        # Snapshot current page to page_versions before rewrite
        db.execute(
            __import__("sqlalchemy").text("""
                INSERT INTO page_versions (page_id, version_num, content, created_at)
                SELECT :pid,
                       COALESCE((SELECT MAX(version_num) FROM page_versions WHERE page_id=:pid), 0) + 1,
                       content,
                       NOW()
                FROM wiki_pages WHERE id = :pid
            """),
            {"pid": page_id},
        )
        db.commit()

        row = db.execute(
            __import__("sqlalchemy").text(
                "SELECT content FROM wiki_pages WHERE id = :pid"
            ),
            {"pid": page_id},
        ).fetchone()

    if not row:
        msg = f"[coherence] page {page_id} not found"
        logger.error(msg)
        _discord_notify(f"\u26a0\ufe0f Coherence pass FAILED: page {page_id} not found")
        try:
            _rc = _get_redis()
            if _rc:
                _rc.delete(f"autowiki:coherence_dispatched:{page_id}")
        except Exception:
            pass
        return {"decision": "error", "reason": "page_not_found"}

    current_content = row[0]
    with SessionLocal() as db:
        citation_context = build_evidence_map(db, page_id, max_rows=80)

    logger.info(
        "[coherence] Dispatching to Opus 4-7 + Gemini 2.5 Pro in parallel (%d char content)...",
        len(current_content),
    )

    import concurrent.futures as _cf
    with _cf.ThreadPoolExecutor(max_workers=2) as _pool:
        opus_future = _pool.submit(_call_opus_coherence, current_content, "", citation_context)
        gemini_future = _pool.submit(_call_gemini_coherence, current_content, "", citation_context)
        opus_result = opus_future.result()
        gemini_result = gemini_future.result()

    opus_score = _score_coherence_output(opus_result)
    gemini_score = _score_coherence_output(gemini_result)
    winner = opus_result if opus_score >= gemini_score else gemini_result
    winner_label = "opus-4-7" if opus_score >= gemini_score else "gemini-2.5-pro"
    logger.info(
        "[coherence] opus_score=%d gemini_score=%d winner=%s",
        opus_score, gemini_score, winner_label,
    )

    result = winner

    if result is None:
        elapsed_ms = int((_time.monotonic() - t0) * 1000)
        logger.error("[coherence] Both Opus and Gemini calls failed")
        _discord_notify(f"\u26a0\ufe0f Coherence pass FAILED (both models failed) page={page_id}")
        with SessionLocal() as db:
            db.execute(
                __import__("sqlalchemy").text("""
                    INSERT INTO autowiki_runs
                        (page_id, started_at, finished_at, proposal_type,
                         model_proposer, model_judge, decision, judge_rationale,
                         judge_prompt_version, latency_ms_breakdown, error_text)
                    VALUES
                        (:page_id, :started, NOW(), 'rakon_coherence_pass',
                         :model, 'tori_validator', 'error',
                         :rationale, 'coherence_v1', CAST(:lat AS jsonb), :err)
                """),
                {
                    "page_id": page_id,
                    "started": started_at,
                    "model": winner_label,
                    "rationale": "Both Opus and Gemini calls failed",
                    "lat": _json.dumps({"total_ms": elapsed_ms}),
                    "err": "both_models_returned_none",
                },
            )
            db.commit()
        try:
            _rc = _get_redis()
            if _rc:
                _rc.delete(f"autowiki:coherence_dispatched:{page_id}")
        except Exception:
            pass
        return {"decision": "error", "reason": "both_models_failed"}

    elapsed_ms = int((_time.monotonic() - t0) * 1000)
    logger.info(
        "[coherence] %s returned %d chars in %ds",
        winner_label, len(result), elapsed_ms // 1000,
    )

    import re as _re

    def _norm(s: str) -> str:
        return _re.sub(r'[^\w\s]', '', s.lower()).strip()

    # Validate: >= 50k chars + all 10 expected sections present
    failures = []
    if len(result) < 50_000:
        failures.append(f"Too short: {len(result):,} chars (need >= 50,000)")
    for sec in _COHERENCE_EXPECTED_SECTIONS:
        if sec not in result:
            # Normalized fallback: lowercase + strip punctuation
            norm_sec = _norm(sec)
            norm_match = any(_norm(line) == norm_sec for line in result.splitlines())
            if norm_match:
                logger.warning(
                    "[coherence] section header normalized-match (exact mismatch): expected=%r", sec
                )
            else:
                failures.append(f"Missing section: {sec}")

    if failures:
        logger.warning("[coherence] gate_reject: %s", failures)
        _discord_notify(
            f"\u26a0\ufe0f Coherence pass gate_reject page={page_id}: {failures!s:.300}"
        )
        with SessionLocal() as db:
            db.execute(
                __import__("sqlalchemy").text("""
                    INSERT INTO autowiki_runs
                        (page_id, started_at, finished_at, proposal_type,
                         model_proposer, model_judge, decision, judge_rationale,
                         judge_prompt_version, latency_ms_breakdown, error_text)
                    VALUES
                        (:page_id, :started, NOW(), 'rakon_coherence_pass',
                         :model, 'tori_validator', 'gate_reject',
                         :rationale, 'coherence_v1', CAST(:lat AS jsonb), :err)
                """),
                {
                    "page_id": page_id,
                    "started": started_at,
                    "model": winner_label,
                    "rationale": f"Validation failed: {failures}"[:500],
                    "lat": _json.dumps({"total_ms": elapsed_ms}),
                    "err": str(failures)[:500],
                },
            )
            db.commit()
        try:
            _rc = _get_redis()
            if _rc:
                _rc.delete(f"autowiki:coherence_dispatched:{page_id}")
        except Exception:
            pass
        return {"decision": "gate_reject", "failures": failures}

    # Atomic write: UPDATE wiki_pages + INSERT page_versions + log autowiki_run
    with SessionLocal() as db:
        db.execute(
            __import__("sqlalchemy").text(
                "UPDATE wiki_pages SET content = :content WHERE id = :pid"
            ),
            {"content": result, "pid": page_id},
        )

        ver_row = db.execute(
            __import__("sqlalchemy").text("""
                INSERT INTO page_versions (page_id, version_num, content, created_at)
                VALUES (:pid,
                        COALESCE((SELECT MAX(version_num) FROM page_versions WHERE page_id=:pid), 0) + 1,
                        :content, NOW())
                RETURNING id
            """),
            {"pid": page_id, "content": result},
        ).fetchone()
        ver_id = ver_row[0] if ver_row else None

        db.execute(
            __import__("sqlalchemy").text("""
                INSERT INTO autowiki_runs
                    (page_id, started_at, finished_at, proposal_type,
                     model_proposer, model_judge, decision, judge_rationale,
                     judge_prompt_version, latency_ms_breakdown, committed_version_id)
                VALUES
                    (:page_id, :started, NOW(), 'rakon_coherence_pass',
                     :model, 'tori_validator', 'commit',
                     :rationale, 'coherence_v1', CAST(:lat AS jsonb), :ver_id)
            """),
            {
                "page_id": page_id,
                "started": started_at,
                "model": winner_label,
                "rationale": f"Coherence rewrite via {winner_label}: {len(result):,} chars, validation passed.",
                "lat": _json.dumps({"total_ms": elapsed_ms}),
                "ver_id": ver_id,
            },
        )
        from app.agent_loop.agent_ping import mark_celery_agent_active
        mark_celery_agent_active(db, winner_label)
        db.commit()
        emit_citation_scrub_required(page_id)

    # MARKER_REEMBED_REQUIRED: re-derive claim markers against new prose
    try:
        from app.agent_loop.marker_embed.tasks import emit_reembed
        emit_reembed(page_id)
    except Exception:
        pass

    # Clear manual trigger flag and dispatch lock
    try:
        _r = _get_redis()
        if _r:
            _r.delete(f"autowiki:coherence_needed:{page_id}")
            _r.delete(f"autowiki:coherence_dispatched:{page_id}")
    except Exception:
        pass

    _discord_notify(
        f"\u2705 Coherence pass COMMITTED page={page_id}: "
        f"{len(result):,} chars, {elapsed_ms // 1000}s, winner={winner_label}, "
        f"page_versions.id={ver_id}"
    )
    logger.info(
        "[coherence] COMMIT page=%d version=%s chars=%d elapsed_s=%d",
        page_id, ver_id, len(result), elapsed_ms // 1000,
    )
    return {
        "decision": "commit",
        "page_id": page_id,
        "chars": len(result),
        "version_id": ver_id,
        "elapsed_s": elapsed_ms // 1000,
    }
