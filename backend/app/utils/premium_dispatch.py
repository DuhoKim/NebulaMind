"""Premium/standard LLM spend guard and audit logging."""

from __future__ import annotations

import json
import logging
from dataclasses import dataclass
from typing import Any

from sqlalchemy import text

from app.config import BATCH_SAFE_MODELS, settings

log = logging.getLogger(__name__)

KRW_PER_USD = 1_400
N_PREMIUM = 5

# Static price table, KRW per 1M input/output tokens.
MODEL_PRICE_TABLE: dict[str, tuple[int, int]] = {
    "claude-opus-4-7": (15 * KRW_PER_USD, 75 * KRW_PER_USD),
    "claude-sonnet-4-6": (3 * KRW_PER_USD, 15 * KRW_PER_USD),
    "claude-3-5-sonnet": (3 * KRW_PER_USD, 15 * KRW_PER_USD),
    "gemini-2.5-pro": (2 * KRW_PER_USD, 10 * KRW_PER_USD),
    "gemini-2.5-flash": (420, 3_500),
    "gemini-2.0-flash": (140, 560),
    "gemini-3.5-flash": (140, 560),
    "llama-3.3-70b-versatile": (830, 1_100),
    "llama3.1-8b": (0, 0),
    "llama3.3:70b": (0, 0),
    "deepseek-r1:671b": (0, 0),
    "gpt-oss:20b": (0, 0),
    "gpt-oss:120b": (0, 0),
    "qwen3.6:35b-a3b-nvfp4": (0, 0),
    "qwen3.6:27b-nvfp4": (0, 0),
    "astrosage-70b": (0, 0),
    "astrosage-70b:latest": (0, 0),
    "vanta-research/atom-astronomy-7b": (0, 0),
    "vanta-research/atom-astronomy-7b:latest": (0, 0),
    "nomic-embed-text:v1.5": (0, 0),
}

PREMIUM_MODEL_FRAGMENTS = ("opus", "sonnet", "gemini-2.5-pro", "gpt-5")
PREMIUM_JOB_WHITELIST = {
    "opus-judge-tick",
    "sonnet-judge-tick",
    "interactive-agent-session",
    "interactive_agent_session",
    "autowiki.sonnet_section_rewrite",
    "autowiki.opus_coherence",
    "autowiki.gemini_coherence",
    "research_ideas.opus_hero_refresh",
    "tasks.fact_draft",
    "services.social_drafts",
}


class PremiumDispatchBlocked(RuntimeError):
    pass


@dataclass(frozen=True)
class DispatchDecision:
    job_name: str
    model: str
    tier: str
    estimated_tokens: int
    estimated_cost_krw: float
    warnings: tuple[str, ...] = ()


def normalize_model(model: str) -> str:
    model = (model or "").strip()
    if "/" in model and not model.startswith("vanta-research/"):
        return model.split("/", 1)[1]
    return model


def model_tier(model: str) -> str:
    normalized = normalize_model(model)
    if model in BATCH_SAFE_MODELS or normalized in BATCH_SAFE_MODELS:
        return "BATCH_SAFE"
    lower = normalized.lower()
    if any(fragment in lower for fragment in PREMIUM_MODEL_FRAGMENTS):
        return "PREMIUM"
    return "STANDARD"


def estimate_token_count(value: int | dict[str, int] | None) -> tuple[int, int]:
    if isinstance(value, dict):
        return max(0, int(value.get("input", 0))), max(0, int(value.get("output", 0)))
    total = max(0, int(value or 0))
    return total, 0


def estimate_cost_krw(model: str, est_tokens: int | dict[str, int] | None) -> float:
    input_tokens, output_tokens = estimate_token_count(est_tokens)
    in_price, out_price = MODEL_PRICE_TABLE.get(normalize_model(model), (1_400, 5_600))
    return (input_tokens * in_price + output_tokens * out_price) / 1_000_000


def _rolling_cost(db, interval_sql: str) -> float:
    row = db.execute(
        text(
            """
            SELECT COALESCE(SUM(total_cost_krw), 0)
            FROM llm_spend_log
            WHERE created_at >= NOW() - CAST(:interval AS interval)
              AND status = 'executed'
              AND tier IN ('PREMIUM', 'STANDARD')
            """
        ),
        {"interval": interval_sql},
    ).fetchone()
    return float(row[0] or 0)


def _insert_log(
    db,
    *,
    job_name: str,
    model: str,
    tier: str,
    estimated_tokens: int = 0,
    prompt_tokens: int | None = None,
    completion_tokens: int | None = None,
    input_cost_krw: float = 0,
    output_cost_krw: float = 0,
    total_cost_krw: float = 0,
    status: str,
    blocked_reason: str | None = None,
    metadata: dict[str, Any] | None = None,
) -> None:
    db.execute(
        text(
            """
            INSERT INTO llm_spend_log (
                job_name, model_name, tier, estimated_tokens, prompt_tokens,
                completion_tokens, input_cost_krw, output_cost_krw, total_cost_krw,
                status, blocked_reason, metadata_json
            )
            VALUES (
                :job, :model, :tier, :estimated_tokens, :prompt_tokens,
                :completion_tokens, :input_cost, :output_cost, :total_cost,
                :status, :blocked_reason, :metadata
            )
            """
        ),
        {
            "job": job_name,
            "model": model,
            "tier": tier,
            "estimated_tokens": estimated_tokens,
            "prompt_tokens": prompt_tokens,
            "completion_tokens": completion_tokens,
            "input_cost": input_cost_krw,
            "output_cost": output_cost_krw,
            "total_cost": total_cost_krw,
            "status": status,
            "blocked_reason": blocked_reason,
            "metadata": json.dumps(metadata) if metadata is not None else None,
        },
    )


def log_llm_call(
    task_role: str,
    model_label: str,
    *,
    model_name: str | None = None,
    success: bool = True,
    latency_ms: int | None = None,
    prompt_tokens: int | None = None,
    completion_tokens: int | None = None,
    error: str | None = None,
    db=None,
) -> None:
    """Write the lightweight model-call telemetry used by /admin/llm."""
    close_db = False
    if db is None:
        from app.database import SessionLocal

        db = SessionLocal()
        close_db = True
    try:
        db.execute(
            text(
                """
                INSERT INTO llm_calls (
                    task_role, model_label, model_name, success, latency_ms,
                    prompt_tokens, completion_tokens, error
                )
                VALUES (
                    :task_role, :model_label, :model_name, :success, :latency_ms,
                    :prompt_tokens, :completion_tokens, :error
                )
                """
            ),
            {
                "task_role": task_role[:50],
                "model_label": model_label[:80],
                "model_name": (model_name or model_label)[:120],
                "success": success,
                "latency_ms": latency_ms,
                "prompt_tokens": prompt_tokens,
                "completion_tokens": completion_tokens,
                "error": error[:2000] if error else None,
            },
        )
        db.commit()
    except Exception as exc:
        log.warning("failed to log LLM call for %s/%s: %s", task_role, model_label, exc)
        db.rollback()
    finally:
        if close_db:
            db.close()


def dispatch_premium(
    job_name: str,
    model: str,
    est_tokens: int | dict[str, int] | None,
    *,
    items_touched: int = 1,
    db=None,
) -> DispatchDecision:
    """Check whether a premium/standard model dispatch is allowed."""
    tier = model_tier(model)
    input_tokens, output_tokens = estimate_token_count(est_tokens)
    estimated_tokens = input_tokens + output_tokens
    estimated_cost = estimate_cost_krw(model, est_tokens)

    warnings: list[str] = []
    if tier == "BATCH_SAFE":
        return DispatchDecision(job_name, model, tier, estimated_tokens, estimated_cost)

    if tier == "PREMIUM" and job_name not in PREMIUM_JOB_WHITELIST:
        reason = f"premium model {model!r} is not whitelisted for job {job_name!r}"
        _log_block(job_name, model, tier, estimated_tokens, estimated_cost, reason, db)
        raise PremiumDispatchBlocked(reason)

    if tier == "PREMIUM" and items_touched > N_PREMIUM:
        reason = f"premium job {job_name!r} touches {items_touched} items; max is {N_PREMIUM}"
        _log_block(job_name, model, tier, estimated_tokens, estimated_cost, reason, db)
        raise PremiumDispatchBlocked(reason)

    if not settings.PREMIUM_DISPATCH_ENABLED:
        reason = "NM_PREMIUM_DISPATCH_ENABLED=false"
        _log_block(job_name, model, tier, estimated_tokens, estimated_cost, reason, db)
        raise PremiumDispatchBlocked(reason)

    if estimated_cost >= settings.PREMIUM_JOB_HARD_KRW:
        reason = f"estimated job cost {estimated_cost:.0f} KRW exceeds hard cap"
        _log_block(job_name, model, tier, estimated_tokens, estimated_cost, reason, db)
        raise PremiumDispatchBlocked(reason)
    if estimated_cost >= settings.PREMIUM_JOB_SOFT_KRW:
        warnings.append(f"estimated job cost {estimated_cost:.0f} KRW exceeds soft alert")

    close_db = False
    if db is None:
        from app.database import SessionLocal

        db = SessionLocal()
        close_db = True

    try:
        cost_24h = _rolling_cost(db, "24 hours") + estimated_cost
        cost_30d = _rolling_cost(db, "30 days") + estimated_cost
        if cost_24h >= settings.PREMIUM_24H_HARD_KRW:
            reason = f"rolling 24h cost {cost_24h:.0f} KRW exceeds hard cap"
            _insert_log(db, job_name=job_name, model=model, tier=tier,
                        estimated_tokens=estimated_tokens, total_cost_krw=estimated_cost,
                        status="blocked", blocked_reason=reason)
            db.commit()
            raise PremiumDispatchBlocked(reason)
        if cost_30d >= settings.PREMIUM_30D_HARD_KRW:
            reason = f"rolling 30d cost {cost_30d:.0f} KRW exceeds Papa-only hard cap"
            _insert_log(db, job_name=job_name, model=model, tier=tier,
                        estimated_tokens=estimated_tokens, total_cost_krw=estimated_cost,
                        status="blocked", blocked_reason=reason)
            db.commit()
            raise PremiumDispatchBlocked(reason)
        if cost_24h >= settings.PREMIUM_24H_SOFT_KRW:
            warnings.append(f"rolling 24h cost {cost_24h:.0f} KRW exceeds soft alert")
        if cost_30d >= settings.PREMIUM_30D_SOFT_KRW:
            warnings.append(f"rolling 30d cost {cost_30d:.0f} KRW exceeds soft alert")
        db.commit()
    finally:
        if close_db:
            db.close()

    for warning in warnings:
        log.warning("premium_dispatch: %s", warning)
    return DispatchDecision(job_name, model, tier, estimated_tokens, estimated_cost, tuple(warnings))


def _log_block(
    job_name: str,
    model: str,
    tier: str,
    estimated_tokens: int,
    estimated_cost: float,
    reason: str,
    db=None,
) -> None:
    close_db = False
    if db is None:
        from app.database import SessionLocal

        db = SessionLocal()
        close_db = True
    try:
        _insert_log(db, job_name=job_name, model=model, tier=tier,
                    estimated_tokens=estimated_tokens, total_cost_krw=estimated_cost,
                    status="blocked", blocked_reason=reason)
        log_llm_call(
            job_name,
            model,
            model_name=model,
            success=False,
            prompt_tokens=estimated_tokens,
            error=reason,
            db=db,
        )
        db.commit()
    finally:
        if close_db:
            db.close()


def log_llm_spend(
    job_name: str,
    model: str,
    *,
    prompt_tokens: int | None = None,
    completion_tokens: int | None = None,
    cache_creation_tokens: int | None = None,
    cache_read_tokens: int | None = None,
    estimated_tokens: int | None = None,
    status: str = "executed",
    metadata: dict[str, Any] | None = None,
    db=None,
) -> None:
    """Log an executed LLM call using actual tokens when available."""
    prompt = int(prompt_tokens or 0)
    completion = int(completion_tokens or 0)
    if estimated_tokens is None:
        estimated_tokens = prompt + completion

    # Merge cache stats into metadata for log visibility
    cache_stats: dict[str, Any] = {}
    if cache_creation_tokens is not None:
        cache_stats["cache_creation_tokens"] = cache_creation_tokens
    if cache_read_tokens is not None:
        cache_stats["cache_read_tokens"] = cache_read_tokens
    if cache_stats:
        metadata = {**(metadata or {}), **cache_stats}

    in_price, out_price = MODEL_PRICE_TABLE.get(normalize_model(model), (1_400, 5_600))
    input_cost = prompt * in_price / 1_000_000
    output_cost = completion * out_price / 1_000_000
    if prompt == 0 and completion == 0 and estimated_tokens:
        input_cost = estimate_cost_krw(model, estimated_tokens)
    total = input_cost + output_cost
    close_db = False
    if db is None:
        from app.database import SessionLocal

        db = SessionLocal()
        close_db = True
    try:
        _insert_log(
            db,
            job_name=job_name,
            model=model,
            tier=model_tier(model),
            estimated_tokens=int(estimated_tokens or 0),
            prompt_tokens=prompt_tokens,
            completion_tokens=completion_tokens,
            input_cost_krw=input_cost,
            output_cost_krw=output_cost,
            total_cost_krw=total,
            status=status,
            metadata=metadata,
        )
        log_llm_call(
            job_name,
            model,
            model_name=model,
            success=status == "executed",
            latency_ms=(metadata or {}).get("latency_ms"),
            prompt_tokens=prompt_tokens,
            completion_tokens=completion_tokens,
            error=(metadata or {}).get("error"),
            db=db,
        )
        db.commit()
    except Exception as exc:
        log.warning("failed to log LLM spend for %s/%s: %s", job_name, model, exc)
        db.rollback()
    finally:
        if close_db:
            db.close()
