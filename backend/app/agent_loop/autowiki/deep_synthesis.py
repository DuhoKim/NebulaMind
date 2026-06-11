"""
Rakon deep synthesis pass — 6h batch worker.

Rakon (deepseek-r1:671b, Mac Pro) generates reasoning skeletons for missing
debate claims. AstroSage-70B polishes each skeleton into final prose.
Inserts claims as claim_type='debate', logs to autowiki_runs.

Gated behind the same `autowiki:enabled` Redis flag as the tick loop.
"""
import datetime as dt
import json
import time

import httpx

from app.agent_loop.worker import celery_app
from app.agent_loop.autowiki.program_loader import load_program
from app.config import settings
from app.database import SessionLocal
from app.models.autowiki import AutowikiRun
from app.models.claim import Claim
from app.models.page import WikiPage


_RAKON_MODEL = settings.RAKON_MODEL
_ASTROSAGE_MODEL = settings.ASTRO_SYNTH_MODEL or "astrosage-70b"


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


def _get_autowiki_agent_id(db) -> int | None:
    from sqlalchemy import text
    row = db.execute(
        text("SELECT id FROM agents WHERE name = 'autowiki' LIMIT 1")
    ).first()
    return row.id if row else None


def _call_rakon(prompt: str, timeout: int = 3600) -> str:
    base = settings.RAKON_BASE_URL.rstrip("/")
    resp = httpx.post(
        f"{base}/v1/chat/completions",
        json={
            "model": _RAKON_MODEL,
            "messages": [
                {
                    "role": "system",
                    "content": (
                        "You are a deep astronomy reasoner with expertise in the current "
                        "state of observational and theoretical astrophysics. "
                        "Return valid JSON only — no prose outside the JSON structure."
                    ),
                },
                {"role": "user", "content": prompt},
            ],
            "temperature": 0.3,
            "options": {"num_ctx": 8192},
        },
        timeout=timeout,
    )
    resp.raise_for_status()
    return resp.json()["choices"][0]["message"]["content"]


def _call_astrosage(prompt: str, timeout: int = 90) -> str:
    base = settings.OLLAMA_BASE_URL.rstrip("/")
    resp = httpx.post(
        f"{base}/v1/chat/completions",
        json={
            "model": _ASTROSAGE_MODEL,
            "messages": [
                {
                    "role": "system",
                    "content": (
                        "You are an astronomy wiki editor. Polish the given debate claim "
                        "skeleton into a single authoritative, specific, citation-ready "
                        "claim sentence. Return only the polished sentence — no preamble."
                    ),
                },
                {"role": "user", "content": prompt},
            ],
            "temperature": 0.4,
            "options": {"num_ctx": 8192},
        },
        timeout=timeout,
    )
    resp.raise_for_status()
    return resp.json()["choices"][0]["message"]["content"].strip()


def _parse_skeletons(raw: str) -> list[dict]:
    """Extract JSON array of skeletons from Rakon response."""
    start = raw.find("[")
    end = raw.rfind("]") + 1
    if start == -1 or end <= start:
        return []
    try:
        items = json.loads(raw[start:end])
        return [
            s for s in items
            if isinstance(s, dict) and s.get("claim_text") and s.get("supporting_argument")
        ][:3]
    except Exception:
        return []


# ---------------------------------------------------------------------------
# Main task
# ---------------------------------------------------------------------------

@celery_app.task(
    name="app.agent_loop.autowiki.deep_synthesis.rakon_deep_pass",
    task_acks_late=True,
    max_retries=0,
    time_limit=3900,
    soft_time_limit=3600,
)
def rakon_deep_pass(page_id: int) -> dict:
    if not _is_enabled():
        return {"decision": "skip", "reason": "flag_off"}

    started_at = dt.datetime.utcnow()
    t0 = time.monotonic()

    with SessionLocal() as db:
        page = db.query(WikiPage).filter(WikiPage.id == page_id).first()
        if not page:
            return {"decision": "error", "reason": f"page {page_id} not found"}

        agent_id = _get_autowiki_agent_id(db)
        program = load_program(page.slug)

        # Existing debate claims — give Rakon context to avoid duplicates
        existing_debates = (
            db.query(Claim)
            .filter(Claim.page_id == page_id, Claim.claim_type == "debate")
            .all()
        )
        existing_debate_texts = [c.text[:120] for c in existing_debates]

        # ── Step 2: Rakon generates reasoning skeletons ──────────────────────
        rakon_prompt = (
            f"Page: {page.slug}\n\n"
            f"Existing debate claims (do NOT duplicate these):\n"
            + "\n".join(f"- {t}" for t in existing_debate_texts)
            + f"\n\nProgram priorities:\n{program[:800]}\n\n"
            "Generate 2-3 new debate claim REASONING SKELETONS that a professional "
            "astronomer would find genuinely controversial and researchable in the "
            "current literature (2023-2025). For each skeleton provide:\n"
            "- claim_text: the contested claim in one sentence\n"
            "- supporting_argument: 2-3 sentences (who argues for it, with what evidence)\n"
            "- challenging_argument: 2-3 sentences (who argues against it, with what evidence)\n"
            "- key_papers: up to 3 paper titles/arXiv IDs from 2022-2025\n\n"
            "Return a JSON array:\n"
            '[{"claim_text": "...", "supporting_argument": "...", '
            '"challenging_argument": "...", "key_papers": ["..."]}]'
        )

        try:
            raw = _call_rakon(rakon_prompt)
        except Exception as e:
            return _log_and_return(
                db, page_id, started_at, "error",
                f"Rakon call failed: {e}", [], t0,
            )

        skeletons = _parse_skeletons(raw)
        if not skeletons:
            return _log_and_return(
                db, page_id, started_at, "error",
                "Rakon returned no valid skeletons", [], t0,
            )

        # ── Step 3: AstroSage polishes each skeleton ─────────────────────────
        inserted_claims: list[dict] = []
        next_order = db.query(Claim).filter(Claim.page_id == page_id).count()

        for skel in skeletons:
            polish_prompt = (
                f"Polish this debate claim skeleton into a single authoritative claim "
                f"sentence suitable for an astronomy research wiki:\n\n"
                f"Claim: {skel['claim_text']}\n"
                f"Supporting: {skel['supporting_argument']}\n"
                f"Challenging: {skel['challenging_argument']}\n\n"
                "Return only the polished claim sentence."
            )
            try:
                polished = _call_astrosage(polish_prompt)
            except Exception:
                polished = skel["claim_text"]

            # ── Step 4: Insert into DB ────────────────────────────────────────
            claim = Claim(
                page_id=page_id,
                section="Open Questions and Active Debates",
                claim_type="debate",
                trust_level="debated",
                text=polished[:500],
                debate_topic=skel["claim_text"][:200],
                created_by_agent_id=agent_id,
                order_idx=next_order,
            )
            db.add(claim)
            db.flush()
            next_order += 1
            inserted_claims.append({"claim_id": claim.id, "text": polished[:120]})

        # ── Step 5: Log to autowiki_runs ──────────────────────────────────────
        latency_ms = int((time.monotonic() - t0) * 1000)
        run = AutowikiRun(
            page_id=page_id,
            started_at=started_at,
            finished_at=dt.datetime.utcnow(),
            proposal_type="rakon_deep_pass",
            model_proposer=_RAKON_MODEL,
            model_judge=_RAKON_MODEL,
            decision="commit",
            judge_rationale=(
                f"Rakon deep pass inserted {len(inserted_claims)} debate claim(s): "
                + "; ".join(c["text"] for c in inserted_claims[:2])
            )[:500],
            judge_prompt_version="deep_pass_v1",
            latency_ms_breakdown={"total_ms": latency_ms},
        )
        db.add(run)
        db.commit()

        print(
            f"[rakon_deep_pass] page={page_id} inserted={len(inserted_claims)} "
            f"claims in {latency_ms}ms"
        )
        return {
            "decision": "commit",
            "page_id": page_id,
            "inserted_claims": len(inserted_claims),
            "claims": inserted_claims,
        }


def _log_and_return(
    db, page_id: int, started_at: dt.datetime,
    decision: str, reason: str, claims: list, t0: float,
) -> dict:
    latency_ms = int((time.monotonic() - t0) * 1000)
    run = AutowikiRun(
        page_id=page_id,
        started_at=started_at,
        finished_at=dt.datetime.utcnow(),
        proposal_type="rakon_deep_pass",
        model_proposer=_RAKON_MODEL,
        decision=decision,
        reject_reason=reason,
        latency_ms_breakdown={"total_ms": latency_ms},
    )
    db.add(run)
    db.commit()
    return {"decision": decision, "reason": reason, "page_id": page_id}
