"""
Three-tier judge panel — independent Sonnet/Opus audit judges (§5.6 extension).

Both judges are audit-only: decision='audit', no commit/rollback authority.
- Sonnet (HwaO): claude-sonnet-4-6, every 20 min
- Opus   (Kun):  claude-opus-4-7,   every 60 min

v4 (2026-05-12): updated to the 10-dim hybrid scoring. Sonnet/Opus return
the 5 judge dims; Python computes the 5 objective dims; compute_utility()
combines them with tier gates. See docs/autowiki_loop_v1.md §13.
"""
import datetime as dt
import logging
import time

logger = logging.getLogger(__name__)

from app.agent_loop.worker import celery_app
from app.agent_loop.autowiki.judge import (
    JUDGE_DIM_KEYS,
    JudgeResult,
    _get_redis,
    _load_prompt,
    _parse_rubric,
    compute_python_dims,
    compute_utility,
)
from app.agent_loop.autowiki.scorer import compute_quality
from app.config import settings
from app.database import SessionLocal
from app.models.autowiki import AutowikiRun
from app.models.claim import Claim
from app.models.page import WikiPage
from app.services.page_health import compute_health_score
from app.utils.premium_dispatch import dispatch_premium, log_llm_spend

SONNET_MODEL = "claude-sonnet-4-6"
OPUS_MODEL = "claude-opus-4-7"
PANEL_PROMPT_VERSION_SONNET = "judge_v4-sonnet"
PANEL_PROMPT_VERSION_OPUS = "judge_v4-opus"


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def _is_enabled() -> bool:
    r = _get_redis()
    if r is None:
        return False
    try:
        return r.get("autowiki:enabled") == "1"
    except Exception:
        return False


def _ms(t0: float) -> int:
    return int((time.monotonic() - t0) * 1000)


def _claims_text(claims: list) -> str:
    return "\n".join(f"[{c.claim_type}] {c.text}" for c in claims[:40])


def _call_claude(model: str, system: str, user_msg: str) -> dict | None:
    try:
        import anthropic
        client = anthropic.Anthropic(api_key=settings.ANTHROPIC_API_KEY)
        job_name = "opus-judge-tick" if "opus" in model else "sonnet-judge-tick"
        est_tokens = {"input": max(1, (len(system) + len(user_msg)) // 4), "output": 512}
        dispatch_premium(job_name, model, est_tokens)
        response = client.messages.create(
            model=model,
            max_tokens=512,
            system=[{"type": "text", "text": system, "cache_control": {"type": "ephemeral"}}],
            messages=[{"role": "user", "content": user_msg}],
        )
        usage = getattr(response, "usage", None)
        log_llm_spend(
            job_name,
            model,
            prompt_tokens=getattr(usage, "input_tokens", None),
            completion_tokens=getattr(usage, "output_tokens", None),
            cache_creation_tokens=getattr(usage, "cache_creation_input_tokens", None),
            cache_read_tokens=getattr(usage, "cache_read_input_tokens", None),
            estimated_tokens=est_tokens["input"],
        )
        text = response.content[0].text
        return _parse_rubric(text)
    except Exception as e:
        logger.exception("Claude judge call failed for model %s: %s", model, e)
        return None


def _make_zero_result(prompt_version: str, reason: str) -> JudgeResult:
    judge_dims = {k: 0.0 for k in JUDGE_DIM_KEYS}
    python_dims = {k: 0.0 for k in (
        "citation_density", "recency_density_2020", "recency_density_2023",
        "instrument_breadth", "voice_purity",
    )}
    merged = {**python_dims, **judge_dims, "rationale": reason}
    return JudgeResult(
        utility=0.0,
        raw_scores=[],
        rubric_median=merged,
        rationale=reason,
        prompt_version=prompt_version,
        model_used="none",
    )


def _judge_via_claude(model: str, content: str, claims_text: str, prompt_version: str) -> JudgeResult:
    system = _load_prompt()
    user_msg = (
        f"===PAGE===\n{content[:4000]}\n\n"
        f"===CLAIMS===\n{claims_text[:1500]}"
    )
    judge_dims = _call_claude(model, system, user_msg)
    if judge_dims is None:
        return _make_zero_result(prompt_version, f"{model} judge call failed.")

    python_dims = compute_python_dims(content)
    rationale = judge_dims.pop("rationale", "")
    utility = compute_utility(judge_dims, python_dims)
    merged = {**python_dims, **judge_dims, "rationale": rationale}

    return JudgeResult(
        utility=utility,
        raw_scores=[judge_dims],
        rubric_median=merged,
        rationale=rationale,
        prompt_version=prompt_version,
        model_used=model,
    )


# ---------------------------------------------------------------------------
# Public judge functions
# ---------------------------------------------------------------------------

def judge_sonnet(
    page_id: int,
    content: str,
    hero_facts: str | None,
    claims_text: str,
) -> JudgeResult:
    return _judge_via_claude(SONNET_MODEL, content, claims_text, PANEL_PROMPT_VERSION_SONNET)


def judge_opus(
    page_id: int,
    content: str,
    hero_facts: str | None,
    claims_text: str,
) -> JudgeResult:
    return _judge_via_claude(OPUS_MODEL, content, claims_text, PANEL_PROMPT_VERSION_OPUS)


# ---------------------------------------------------------------------------
# Shared audit tick logic
# ---------------------------------------------------------------------------

def _audit_tick(page_id: int, judge_fn, proposal_type: str, judge_model: str) -> dict:
    if not _is_enabled():
        return {"decision": "skip", "reject_reason": "flag_off"}

    started_at = dt.datetime.utcnow()
    t0 = time.monotonic()

    with SessionLocal() as db:
        page = db.query(WikiPage).filter(WikiPage.id == page_id).first()
        if not page:
            return {"decision": "error", "reject_reason": f"page {page_id} not found"}

        claims = (
            db.query(Claim)
            .filter(Claim.page_id == page_id)
            .order_by(Claim.created_at)
            .all()
        )
        claims_t = _claims_text(claims)

        h_result = compute_health_score(page, db)
        h_struct = h_result["score"]

        jr = judge_fn(page_id, page.content or "", page.hero_facts, claims_t)
        q1 = compute_quality(h_struct, jr.utility)
        finished_at = dt.datetime.utcnow()

        run = AutowikiRun(
            page_id=page_id,
            started_at=started_at,
            finished_at=finished_at,
            proposal_type=proposal_type,
            model_judge=judge_model,
            judge_model=judge_model,
            h1_struct=h_struct,
            u1_median=jr.utility,
            u1_runs=jr.raw_scores,
            q1=q1,
            judge_rationale=jr.rationale,
            judge_prompt_version=jr.prompt_version,
            decision="audit",
            latency_ms_breakdown={"total_ms": _ms(t0)},
        )
        db.add(run)
        db.commit()

    return {"decision": "audit", "q1": q1, "utility": jr.utility, "model": judge_model}


# ---------------------------------------------------------------------------
# Celery tasks
# ---------------------------------------------------------------------------

@celery_app.task(
    name="app.agent_loop.autowiki.judge_panel.sonnet_judge_tick",
    task_acks_late=True,
    max_retries=0,
)
def sonnet_judge_tick(page_id: int) -> dict:
    return _audit_tick(page_id, judge_sonnet, "sonnet_audit", SONNET_MODEL)


@celery_app.task(
    name="app.agent_loop.autowiki.judge_panel.opus_judge_tick",
    task_acks_late=True,
    max_retries=0,
)
def opus_judge_tick(page_id: int) -> dict:
    return _audit_tick(page_id, judge_opus, "opus_audit", OPUS_MODEL)
