"""Batch-cost safeguard for LLM-in-loop call sites.

Apply guard_batch_model() at the entry of any function that dispatches LLM
calls inside a loop over claims, papers, or other large datasets. The guard
blocks routing of premium / preview models (e.g. gemini-3.1-pro-preview,
gemini-2.5-pro, claude-opus, gpt-5.5) into high-volume loops where total
token spend would otherwise scale into the tens or hundreds of millions of
tokens on a per-batch basis.

History: 2026-06-01 Gemini 3.1 Pro Preview entailment-gate batch burned
~₩777K vs an expected ~₩8K. See the `entailment_gate_v1_gemini_*` artifacts
and the 2026-06-02 Tori spike-investigation memory.
"""

from __future__ import annotations

import logging

from app.config import (
    BATCH_SAFE_DEFAULT_MODEL,
    BATCH_SAFE_MODELS,
    settings,
)

log = logging.getLogger(__name__)


def _normalize(model_id: str) -> str:
    """Strip provider prefix (e.g. "google/", "anthropic/") for allowlist lookup."""
    if "/" in model_id:
        return model_id.split("/", 1)[1]
    return model_id


def guard_batch_model(model_id: str, job_name: str) -> str:
    """Validate that model_id is approved for batch use; return a safe model ID.

    Args:
        model_id: The model the caller intends to use (may include provider prefix).
        job_name: Stable identifier of the calling loop / job, used in errors and logs.

    Returns:
        model_id if it (or its unprefixed form) is in BATCH_SAFE_MODELS.
        BATCH_SAFE_DEFAULT_MODEL if BATCH_STRICT_MODE is False and the input is not allowlisted.

    Raises:
        ValueError: BATCH_STRICT_MODE is True and the input is not allowlisted.
    """
    normalized = _normalize(model_id)
    if model_id in BATCH_SAFE_MODELS or normalized in BATCH_SAFE_MODELS:
        return model_id

    if settings.BATCH_STRICT_MODE:
        raise ValueError(
            f"Model {model_id!r} is not approved for batch job {job_name!r}. "
            f"Use a model from BATCH_SAFE_MODELS (see app/config.py)."
        )

    log.warning(
        "batch_guard: substituting %r -> %r for job %r (NM_BATCH_STRICT_MODE=False)",
        model_id,
        BATCH_SAFE_DEFAULT_MODEL,
        job_name,
    )
    return BATCH_SAFE_DEFAULT_MODEL
