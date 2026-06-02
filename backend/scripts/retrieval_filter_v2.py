#!/usr/bin/env python3
"""Shared retrieval-filter v2 routing primitives.

The module is intentionally page-agnostic: section names, thresholds, marker
strings, tag names, and protected row keys are config data. The
``boundary_review_keep`` decision records retrieval audit provenance and never
grants promotion authority.
"""

from __future__ import annotations

import json
import os
import time
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Iterable, Literal, Mapping

import requests
import yaml


Decision = Literal["keep", "drop", "downrank", "boundary_review_keep", "element_unsupported", "semantic_unsupported"]

ReasonCode = Literal[
    "score_band",
    "protected_marker",
    "protected_row_key",
    "tag_protection",
    "suppression_demoted",
    "hard_drop",
]

KEEP: Decision = "keep"
DROP: Decision = "drop"
DOWNRANK: Decision = "downrank"
BOUNDARY_REVIEW_KEEP: Decision = "boundary_review_keep"
ELEMENT_UNSUPPORTED: Decision = "element_unsupported"
SEMANTIC_UNSUPPORTED: Decision = "semantic_unsupported"
ENTAILMENT_OLLAMA_MODEL = "llama3.1:8b"
ENTAILMENT_OLLAMA_BASE = "http://localhost:11434"
ENTAILMENT_GEMINI_BASE = "https://generativelanguage.googleapis.com/v1beta/openai"
ENTAILMENT_GEMINI_MODEL = "google/gemini-2.5-flash"
ENTAILMENT_MODEL = ENTAILMENT_GEMINI_MODEL
ENTAILMENT_TIMEOUT_SECONDS = 45
ENTAILMENT_PROMPT_TEMPLATE = """You are a strict logic evaluator determining if a source document supports a specific claim element. Do not invent support.
Answer yes if the source directly supports the element in equivalent words. A source can support an element by naming the same measurable factor, relationship, or mechanism without repeating the exact wording.

Claim Context: {claim_text_snapshot}
Specific Element to Verify: {element_text}
Source Abstract: {paper_abstract_snapshot}

Task: Does the Source Abstract provide evidence that directly supports the Specific Element?
Respond with JSON only, using exactly this schema:
{{
  "entailment": "yes|no|abstain",
  "reason": "Brief 1-sentence justification"
}}
"""

SCORE_BAND: ReasonCode = "score_band"
PROTECTED_MARKER: ReasonCode = "protected_marker"
PROTECTED_ROW_KEY: ReasonCode = "protected_row_key"
TAG_PROTECTION: ReasonCode = "tag_protection"
SUPPRESSION_DEMOTED: ReasonCode = "suppression_demoted"
HARD_DROP: ReasonCode = "hard_drop"

_VALID_TAG_ACTIONS = {
    "boundary_review",
    "boundary_review_when_protected_marker_present",
    "downrank",
    "downrank_or_boundary_review",
    "downrank_only_unless_stellar_leakage",
    "hard_negative_unless_protected_marker",
    "hard_negative_unless_environment_marker_present",
}

_ACTION_NORMALIZATION = {
    "boundary_review": "boundary_review",
    "boundary_review_when_protected_marker_present": "boundary_review_when_protected_marker_present",
    "downrank": "downrank",
    "downrank_or_boundary_review": "boundary_review",
    "downrank_only_unless_stellar_leakage": "downrank",
    "hard_negative_unless_protected_marker": "hard_negative_unless_protected_marker",
    "hard_negative_unless_environment_marker_present": "hard_negative_unless_protected_marker",
}

_DEFAULT_MARKER_FIELDS = (
    "target_section_title",
    "claim_text_snapshot",
    "element_text",
    "paper_title_snapshot",
    "paper_abstract_snapshot",
    "normalized_subject",
    "normalized_mechanism",
    "section",
    "target_section",
    "astrosage_reason",
)


@dataclass(frozen=True)
class RetrievalCandidate:
    page_slug: str | None
    section: str
    element_id: str
    paper_id: str
    final_score: float
    combined_score: float | None
    dropped: bool
    drop_reasons: tuple[str, ...]
    tags: tuple[str, ...]
    text: Mapping[str, str | None]
    raw: Mapping[str, Any]


@dataclass(frozen=True)
class BoundaryReviewRule:
    policy_id: str
    hard_drop_below: float
    old_v1_floor: float
    protected_markers: tuple[str, ...]
    marker_match_fields: tuple[str, ...]
    tag_protection: Mapping[str, str]
    hard_drop_reasons: tuple[str, ...]
    boundary_review_reasons: tuple[str, ...]
    protected_row_keys: tuple[str | Mapping[str, Any], ...]
    legacy_protected_marker_fallback: bool = False


@dataclass(frozen=True)
class ValidatorEnqueuePolicy:
    keep_decisions: tuple[Decision, ...] = (KEEP,)
    boundary_review_keep: str = "audit_only"
    boundary_review_usage: str = "retrieval_audit_only"


@dataclass(frozen=True)
class RoutingDecision:
    decision: Decision
    reason_code: ReasonCode | None
    reason_detail: str | None
    policy_id: str | None
    enters_validator: bool
    validator_enqueue_policy: str
    validator_enqueue_reason: str | None
    brk_usage: str | None
    promotion_authority: Literal[False]
    features: dict[str, Any]

    @property
    def boundary_review_reason(self) -> str | None:
        return self.reason_detail if self.reason_code == SCORE_BAND else self.reason_code


@dataclass(frozen=True)
class EntailmentGateResult:
    entailment: Literal["yes", "no", "abstain", "error"]
    reason: str | None = None
    error: str | None = None
    raw_response: str | None = None
    latency_seconds: float | None = None
    prompt_tokens: int | None = None
    completion_tokens: int | None = None
    total_tokens: int | None = None

    @property
    def admits_coverage(self) -> bool:
        return self.entailment == "yes"

    @property
    def exclusion_reason(self) -> Literal["entailment_rejected", "entailment_error"] | None:
        if self.entailment == "yes":
            return None
        if self.entailment == "error":
            return "entailment_error"
        return "entailment_rejected"


def load_retrieval_calibration(path: Path) -> dict[str, Any]:
    with path.open(encoding="utf-8") as handle:
        loaded = yaml.safe_load(handle)
    if not isinstance(loaded, dict):
        raise ValueError(f"Invalid retrieval calibration config: {path}")
    return loaded


def _v2_block(calibration: Mapping[str, Any]) -> Mapping[str, Any]:
    block = calibration.get("retrieval_filter_v2_boundary_review")
    if not isinstance(block, Mapping):
        raise KeyError("retrieval_filter_v2_boundary_review missing from calibration")
    return block


def _string_list(value: Any, field_name: str, *, required: bool = False) -> tuple[str, ...]:
    if value is None:
        if required:
            raise ValueError(f"{field_name} must be a list of strings")
        return ()
    if not isinstance(value, list) or not all(isinstance(item, str) for item in value):
        raise ValueError(f"{field_name} must be a list of strings")
    return tuple(value)


def _numeric(value: Any, field_name: str) -> float:
    try:
        return float(value)
    except (TypeError, ValueError) as exc:
        raise ValueError(f"{field_name} must be numeric") from exc


def _validator_enqueue_policy(block: Mapping[str, Any]) -> ValidatorEnqueuePolicy:
    raw = block.get("validator_enqueue_policy", {})
    if raw is None:
        raw = {}
    if not isinstance(raw, Mapping):
        raise ValueError("retrieval_filter_v2_boundary_review.validator_enqueue_policy must be a mapping")

    keep_decisions = _string_list(raw.get("keep_decisions", [KEEP]), "validator_enqueue_policy.keep_decisions")
    invalid_keep = [decision for decision in keep_decisions if decision not in {KEEP, DOWNRANK}]
    if invalid_keep:
        raise ValueError(f"validator_enqueue_policy.keep_decisions contains unsupported decisions: {invalid_keep}")

    brk_raw = raw.get("boundary_review_keep", {})
    if brk_raw is None:
        brk_raw = {}
    if not isinstance(brk_raw, Mapping):
        raise ValueError("validator_enqueue_policy.boundary_review_keep must be a mapping")
    enqueue = bool(brk_raw.get("enqueue", False))
    usage = str(brk_raw.get("usage") or "retrieval_audit_only")
    if enqueue:
        brk_policy = "enqueue"
        if usage == "retrieval_audit_only":
            usage = "validator_candidate"
    else:
        brk_policy = "audit_only"
    return ValidatorEnqueuePolicy(
        keep_decisions=tuple(keep_decisions),
        boundary_review_keep=brk_policy,
        boundary_review_usage=usage,
    )


def validate_retrieval_filter_v2_config(calibration: Mapping[str, Any]) -> None:
    block = _v2_block(calibration)
    scope = block.get("scope")
    if not isinstance(scope, Mapping):
        raise ValueError("retrieval_filter_v2_boundary_review.scope must be a mapping")

    enabled = _string_list(scope.get("enabled_sections"), "scope.enabled_sections", required=True)
    excluded = _string_list(scope.get("excluded_sections", []), "scope.excluded_sections")
    overlap = set(enabled) & set(excluded)
    if overlap:
        raise ValueError(f"enabled_sections and excluded_sections must be disjoint: {sorted(overlap)}")

    section_rules = block.get("section_rules")
    if not isinstance(section_rules, Mapping):
        raise ValueError("retrieval_filter_v2_boundary_review.section_rules must be a mapping")

    _validator_enqueue_policy(block)

    defaults = block.get("defaults") if isinstance(block.get("defaults"), Mapping) else {}
    if defaults:
        _string_list(defaults.get("hard_drop_reasons", []), "defaults.hard_drop_reasons")
        _string_list(defaults.get("marker_match_fields", []), "defaults.marker_match_fields")
        if "legacy_protected_marker_fallback" in defaults and not isinstance(
            defaults.get("legacy_protected_marker_fallback"), bool
        ):
            raise ValueError("defaults.legacy_protected_marker_fallback must be boolean")

    for section in enabled:
        rule = section_rules.get(section)
        if not isinstance(rule, Mapping):
            raise ValueError(f"enabled section {section!r} is missing a section rule")
        hard_drop_below = _numeric(rule.get("hard_drop_below"), f"{section}.hard_drop_below")
        old_v1_floor = _numeric(rule.get("old_v1_floor"), f"{section}.old_v1_floor")
        if hard_drop_below >= old_v1_floor:
            raise ValueError(f"{section}.hard_drop_below must be lower than old_v1_floor")

        _string_list(rule.get("protected_markers", []), f"{section}.protected_markers")
        _string_list(rule.get("marker_match_fields", []), f"{section}.marker_match_fields")
        _string_list(rule.get("boundary_review_reasons", []), f"{section}.boundary_review_reasons")

        protected_row_keys = rule.get("protected_row_keys", [])
        if not isinstance(protected_row_keys, list) or not all(
            isinstance(item, str) or isinstance(item, Mapping) for item in protected_row_keys
        ):
            raise ValueError(f"{section}.protected_row_keys must be a list of strings or mappings")
        if "legacy_protected_marker_fallback" in rule and not isinstance(
            rule.get("legacy_protected_marker_fallback"), bool
        ):
            raise ValueError(f"{section}.legacy_protected_marker_fallback must be boolean")

        tag_policy = rule.get("tag_protection", {})
        if tag_policy is None:
            tag_policy = {}
        if not isinstance(tag_policy, Mapping):
            raise ValueError(f"{section}.tag_protection must be a mapping of string tag to string action")
        for tag, action in tag_policy.items():
            if not isinstance(tag, str) or not isinstance(action, str):
                raise ValueError(f"{section}.tag_protection must be a mapping of string tag to string action")
            if action not in _VALID_TAG_ACTIONS and _normalize_tag_action(action) is None:
                raise ValueError(f"{section}.tag_protection action {action!r} is not supported")

    status = str(block.get("status") or "")
    apply_mode = str(block.get("apply_mode") or "")
    if status == "production_enabled":
        if "production" not in apply_mode:
            raise ValueError("production_enabled requires a production-compatible apply_mode")


def select_v2_rule(calibration: Mapping[str, Any], section: str) -> BoundaryReviewRule | None:
    block = _v2_block(calibration)
    scope = block.get("scope")
    if not isinstance(scope, Mapping):
        return None
    enabled = set(scope.get("enabled_sections") or [])
    excluded = set(scope.get("excluded_sections") or [])
    if section in excluded or section not in enabled:
        return None

    section_rules = block.get("section_rules")
    if not isinstance(section_rules, Mapping):
        return None
    raw_rule = section_rules.get(section)
    if not isinstance(raw_rule, Mapping):
        return None

    defaults = block.get("defaults") if isinstance(block.get("defaults"), Mapping) else {}
    marker_fields = tuple(raw_rule.get("marker_match_fields") or defaults.get("marker_match_fields") or _DEFAULT_MARKER_FIELDS)
    hard_drop_reasons = tuple(defaults.get("hard_drop_reasons") or ("off_domain_enriched_tag_gate", "page_local_paper_suppression"))
    return BoundaryReviewRule(
        policy_id=str(raw_rule.get("policy_id") or ""),
        hard_drop_below=float(raw_rule.get("hard_drop_below")),
        old_v1_floor=float(raw_rule.get("old_v1_floor")),
        protected_markers=tuple(str(item) for item in (raw_rule.get("protected_markers") or [])),
        marker_match_fields=tuple(str(item) for item in marker_fields),
        tag_protection={str(tag): str(action) for tag, action in (raw_rule.get("tag_protection") or {}).items()},
        hard_drop_reasons=tuple(str(item) for item in hard_drop_reasons),
        boundary_review_reasons=tuple(str(item) for item in (raw_rule.get("boundary_review_reasons") or [])),
        protected_row_keys=tuple(raw_rule.get("protected_row_keys") or ()),
        legacy_protected_marker_fallback=bool(
            raw_rule.get(
                "legacy_protected_marker_fallback",
                defaults.get("legacy_protected_marker_fallback", False),
            )
        ),
    )


def select_validator_enqueue_policy(calibration: Mapping[str, Any]) -> ValidatorEnqueuePolicy:
    return _validator_enqueue_policy(_v2_block(calibration))


def _as_tuple(value: Any) -> tuple[str, ...]:
    if value is None:
        return ()
    if isinstance(value, str):
        return (value,)
    if isinstance(value, Iterable) and not isinstance(value, Mapping):
        return tuple(str(item) for item in value)
    return (str(value),)


def _score(row: Mapping[str, Any]) -> float:
    value = row.get("final_score")
    if value is None:
        value = row.get("combined_score")
    try:
        return float(value or 0.0)
    except (TypeError, ValueError):
        return 0.0


def _optional_score(row: Mapping[str, Any], key: str) -> float | None:
    value = row.get(key)
    if value is None:
        return None
    try:
        return float(value)
    except (TypeError, ValueError):
        return None


def _normalize_tag_action(action: str) -> str | None:
    if action in _ACTION_NORMALIZATION:
        return _ACTION_NORMALIZATION[action]
    if action.startswith("boundary_review_when_") and action.endswith("_marker_present"):
        return "boundary_review_when_protected_marker_present"
    return None


def retrieval_candidate_from_row(row: Mapping[str, Any]) -> RetrievalCandidate:
    section = str(row.get("section") or row.get("target_section") or "")
    paper_id = str(row.get("paper_id") or row.get("arxiv_id") or "")
    text: dict[str, str | None] = {}
    for key in _DEFAULT_MARKER_FIELDS:
        value = row.get(key)
        text[key] = None if value is None else str(value)
    return RetrievalCandidate(
        page_slug=None if row.get("page_slug") is None else str(row.get("page_slug")),
        section=section,
        element_id=str(row.get("element_id") or ""),
        paper_id=paper_id,
        final_score=_score(row),
        combined_score=_optional_score(row, "combined_score"),
        dropped=bool(row.get("dropped")),
        drop_reasons=_as_tuple(row.get("drop_reasons")),
        tags=_as_tuple(row.get("tags")),
        text=text,
        raw=row,
    )


def _normal_text(value: Any) -> str:
    return " ".join(str(value or "").lower().replace("_", " ").replace("-", " ").split())


def entailment_gate_prompt(row: Mapping[str, Any]) -> str:
    return ENTAILMENT_PROMPT_TEMPLATE.format(
        claim_text_snapshot=str(row.get("claim_text_snapshot") or ""),
        element_text=str(row.get("element_text") or ""),
        paper_abstract_snapshot=str(row.get("paper_abstract_snapshot") or row.get("paper_abstract") or ""),
    )


def _parse_entailment_payload(raw_content: str) -> EntailmentGateResult:
    content = raw_content.strip()
    if content.startswith("<think>") and "</think>" in content:
        content = content.split("</think>", 1)[1].strip()
    try:
        parsed = json.loads(content)
    except json.JSONDecodeError:
        start = content.find("{")
        end = content.rfind("}")
        if start < 0 or end <= start:
            raise
        parsed = json.loads(content[start : end + 1])
    if not isinstance(parsed, Mapping):
        raise ValueError("entailment response is not a JSON object")
    entailment = str(parsed.get("entailment") or "").strip().lower()
    if entailment not in {"yes", "no", "abstain"}:
        raise ValueError(f"unsupported entailment value: {entailment!r}")
    reason = parsed.get("reason")
    return EntailmentGateResult(
        entailment=entailment,  # type: ignore[arg-type]
        reason=None if reason is None else str(reason),
        raw_response=raw_content,
    )


def evaluate_entailment_gate(
    row: Mapping[str, Any],
    *,
    model: str = ENTAILMENT_OLLAMA_MODEL,
    ollama_base: str = ENTAILMENT_OLLAMA_BASE,
    timeout: int = ENTAILMENT_TIMEOUT_SECONDS,
) -> EntailmentGateResult:
    payload = {
        "model": model,
        "messages": [{"role": "user", "content": entailment_gate_prompt(row)}],
        "stream": False,
        "format": "json",
        "options": {"temperature": 0.0, "num_ctx": 4096, "num_predict": 160},
    }
    started = time.monotonic()
    try:
        response = requests.post(f"{ollama_base.rstrip('/')}/api/chat", json=payload, timeout=timeout)
        response.raise_for_status()
        body = response.json()
        content = ((body.get("message") or {}).get("content") or "").strip()
        parsed = _parse_entailment_payload(content)
        return EntailmentGateResult(
            entailment=parsed.entailment,
            reason=parsed.reason,
            raw_response=parsed.raw_response,
            latency_seconds=round(time.monotonic() - started, 3),
        )
    except Exception as exc:
        return EntailmentGateResult(
            entailment="error",
            error=f"{type(exc).__name__}: {exc}"[:240],
            latency_seconds=round(time.monotonic() - started, 3),
        )


def evaluate_entailment_gate_openai_compatible(
    row: Mapping[str, Any],
    *,
    model: str,
    base_url: str,
    api_key: str,
    timeout: int = ENTAILMENT_TIMEOUT_SECONDS,
) -> EntailmentGateResult:
    request_model = model
    if base_url.rstrip("/").endswith("/v1beta/openai") and request_model.startswith("google/"):
        request_model = request_model.split("/", 1)[1]
    payload = {
        "model": request_model,
        "messages": [{"role": "user", "content": entailment_gate_prompt(row)}],
        "temperature": 0.0,
        "response_format": {"type": "json_object"},
    }
    started = time.monotonic()
    try:
        response = requests.post(
            f"{base_url.rstrip('/')}/chat/completions",
            headers={"Authorization": f"Bearer {api_key}", "Content-Type": "application/json"},
            json=payload,
            timeout=timeout,
        )
        response.raise_for_status()
        body = response.json()
        choices = body.get("choices") or []
        content = (((choices[0] or {}).get("message") or {}).get("content") or "").strip() if choices else ""
        parsed = _parse_entailment_payload(content)
        return EntailmentGateResult(
            entailment=parsed.entailment,
            reason=parsed.reason,
            raw_response=parsed.raw_response,
            latency_seconds=round(time.monotonic() - started, 3),
            prompt_tokens=_usage_int(body, "prompt_tokens"),
            completion_tokens=_usage_int(body, "completion_tokens"),
            total_tokens=_usage_int(body, "total_tokens"),
        )
    except Exception as exc:
        return EntailmentGateResult(
            entailment="error",
            error=f"{type(exc).__name__}: {exc}"[:240],
            latency_seconds=round(time.monotonic() - started, 3),
        )


def _usage_int(body: Mapping[str, Any], key: str) -> int | None:
    usage = body.get("usage")
    if not isinstance(usage, Mapping):
        return None
    value = usage.get(key)
    return value if isinstance(value, int) else None


def evaluate_entailment_gate_gemini(
    row: Mapping[str, Any],
    *,
    model: str = ENTAILMENT_GEMINI_MODEL,
    api_key: str,
    base_url: str = ENTAILMENT_GEMINI_BASE,
    timeout: int = ENTAILMENT_TIMEOUT_SECONDS,
) -> EntailmentGateResult:
    # batch guard — prevents accidentally routing expensive preview/pro models into high-volume loops
    from app.utils.model_guard import guard_batch_model
    model = guard_batch_model(model, "retrieval_filter_v2.evaluate_entailment_gate_gemini")
    return evaluate_entailment_gate_openai_compatible(
        row,
        model=model,
        base_url=base_url,
        api_key=api_key,
        timeout=timeout,
    )


def row_with_entailment_gate(row: Mapping[str, Any], result: EntailmentGateResult, model: str = ENTAILMENT_MODEL) -> dict[str, Any]:
    out = dict(row)
    out.update(
        {
            "entailment_gate_model": model,
            "entailment_gate_decision": result.entailment,
            "entailment_gate_reason": result.reason,
            "entailment_gate_error": result.error,
            "entailment_gate_latency_seconds": result.latency_seconds,
            "entailment_gate_prompt_tokens": result.prompt_tokens,
            "entailment_gate_completion_tokens": result.completion_tokens,
            "entailment_gate_total_tokens": result.total_tokens,
        }
    )
    return out


def split_rows_by_entailment_gate(
    rows: Iterable[Mapping[str, Any]],
    *,
    model: str = ENTAILMENT_MODEL,
    base_url: str = ENTAILMENT_GEMINI_BASE,
    api_key: str | None = None,
    timeout: int = ENTAILMENT_TIMEOUT_SECONDS,
) -> tuple[list[dict[str, Any]], list[dict[str, Any]]]:
    admitted: list[dict[str, Any]] = []
    excluded: list[dict[str, Any]] = []
    resolved_api_key = api_key or os.getenv("NM_GEMINI_API_KEY") or os.getenv("GEMINI_API_KEY")
    for row in rows:
        if resolved_api_key:
            result = evaluate_entailment_gate_gemini(row, model=model, base_url=base_url, api_key=resolved_api_key, timeout=timeout)
        else:
            result = EntailmentGateResult(
                entailment="error",
                error="ValueError: Gemini API key missing; set NM_GEMINI_API_KEY or GEMINI_API_KEY",
                latency_seconds=0.0,
            )
        gated = row_with_entailment_gate(row, result, model)
        if result.admits_coverage:
            admitted.append(gated)
        else:
            excluded.append({**gated, "coverage_queue_exclusion_reason": result.exclusion_reason})
    return admitted, excluded


def _matched_protected_markers(candidate: RetrievalCandidate, rule: BoundaryReviewRule | None) -> list[str]:
    if not rule or not rule.protected_markers:
        return []
    haystack = _normal_text(" ".join(str(candidate.text.get(field) or candidate.raw.get(field) or "") for field in rule.marker_match_fields))
    matched: list[str] = []
    for marker in rule.protected_markers:
        normalized = _normal_text(marker)
        if normalized and normalized in haystack:
            matched.append(marker)
    if not matched and rule.legacy_protected_marker_fallback and not candidate.tags:
        return ["__legacy_protected_marker_fallback__"]
    return matched


def _matched_protected_row_keys(candidate: RetrievalCandidate, rule: BoundaryReviewRule | None) -> list[str]:
    if not rule or not rule.protected_row_keys:
        return []
    section = candidate.section
    claim_id = str(candidate.raw.get("claim_id") or "").strip()
    element_id = candidate.element_id
    paper_id = candidate.paper_id
    candidates = {
        f"{element_id}::{paper_id}",
        f"{section}::{element_id}::{paper_id}",
        f"{claim_id}::{element_id}::{paper_id}",
        f"{section}::{claim_id}::{element_id}::{paper_id}",
    }
    matched: list[str] = []
    for item in rule.protected_row_keys:
        if isinstance(item, str):
            value = item.strip()
            if value in candidates:
                matched.append(value)
        elif isinstance(item, Mapping):
            expected_section = str(item.get("section") or section)
            expected_claim = str(item.get("claim_id") or claim_id)
            expected_element = str(item.get("element_id") or element_id)
            expected_paper = str(item.get("paper_id") or item.get("arxiv_id") or paper_id)
            if (
                expected_section == section
                and expected_claim == claim_id
                and expected_element == element_id
                and expected_paper == paper_id
            ):
                matched.append(f"{expected_section}::{expected_claim}::{expected_element}::{expected_paper}")
    return matched


def _support_exists(candidate: RetrievalCandidate, support_by_section_paper: Mapping[tuple[str, str], int] | None) -> bool:
    if not support_by_section_paper:
        return False
    return support_by_section_paper.get((candidate.section, candidate.paper_id), 0) > 0


def _tag_action(candidate: RetrievalCandidate, rule: BoundaryReviewRule) -> str | None:
    tags = set(candidate.tags)
    for tag, action in rule.tag_protection.items():
        if tag in tags:
            return _normalize_tag_action(action)
    return None


def _score_band_detail(rule: BoundaryReviewRule) -> str:
    return f"{SCORE_BAND}:{rule.hard_drop_below:g}-{rule.old_v1_floor:g}"


def _features(
    candidate: RetrievalCandidate,
    rule: BoundaryReviewRule | None,
    matched_markers: list[str],
    matched_row_keys: list[str],
) -> dict[str, Any]:
    features: dict[str, Any] = {
        "section": candidate.section,
        "paper_id": candidate.paper_id,
        "final_score": candidate.final_score,
        "tags": sorted(candidate.tags),
        "original_drop_reasons": sorted(candidate.drop_reasons),
        "matched_protected_markers": matched_markers,
        "matched_protected_row_keys": matched_row_keys,
    }
    if rule:
        features.update(
            {
                "hard_drop_below": rule.hard_drop_below,
                "old_v1_floor": rule.old_v1_floor,
            }
        )
    return features


def _make_decision(
    decision: Decision,
    reason_code: ReasonCode | None,
    reason_detail: str | None,
    policy_id: str | None,
    features: dict[str, Any],
    enqueue_policy: ValidatorEnqueuePolicy | None = None,
) -> RoutingDecision:
    enqueue_policy = enqueue_policy or ValidatorEnqueuePolicy()
    enters_validator = decision in enqueue_policy.keep_decisions
    validator_policy = "enqueue" if enters_validator else "not_enqueued"
    validator_reason: str | None = decision if enters_validator else None
    brk_usage: str | None = None
    if decision == BOUNDARY_REVIEW_KEEP:
        validator_policy = enqueue_policy.boundary_review_keep
        enters_validator = validator_policy == "enqueue"
        validator_reason = BOUNDARY_REVIEW_KEEP if enters_validator else None
        brk_usage = enqueue_policy.boundary_review_usage
    return RoutingDecision(
        decision=decision,
        reason_code=reason_code,
        reason_detail=reason_detail,
        policy_id=policy_id,
        enters_validator=enters_validator,
        validator_enqueue_policy=validator_policy,
        validator_enqueue_reason=validator_reason,
        brk_usage=brk_usage,
        promotion_authority=False,
        features=features,
    )


def route_candidate_v2(
    candidate: RetrievalCandidate,
    rule: BoundaryReviewRule | None,
    *,
    support_by_section_paper: Mapping[tuple[str, str], int] | None = None,
    validator_enqueue_policy: ValidatorEnqueuePolicy | None = None,
) -> RoutingDecision:
    matched_markers = _matched_protected_markers(candidate, rule)
    matched_row_keys = _matched_protected_row_keys(candidate, rule)
    features = _features(candidate, rule, matched_markers, matched_row_keys)

    if rule is None:
        return _make_decision(
            DROP if candidate.dropped else KEEP,
            None,
            None,
            None,
            features,
            validator_enqueue_policy,
        )

    policy_id = rule.policy_id or None
    if candidate.raw.get("coverage_candidate") is False:
        return _make_decision(SEMANTIC_UNSUPPORTED, None, "semantic_similarity_gate_failed", policy_id, features, validator_enqueue_policy)
    if candidate.raw.get("element_support_gate") is False:
        return _make_decision(ELEMENT_UNSUPPORTED, None, "element_support_gate_failed", policy_id, features, validator_enqueue_policy)
    if not candidate.dropped:
        return _make_decision(KEEP, None, None, policy_id, features, validator_enqueue_policy)

    reasons = set(candidate.drop_reasons)
    if "off_domain_enriched_tag_gate" in reasons:
        return _make_decision(DROP, HARD_DROP, HARD_DROP, policy_id, features, validator_enqueue_policy)

    if "page_local_paper_suppression" in reasons:
        if _support_exists(candidate, support_by_section_paper):
            return _make_decision(
                BOUNDARY_REVIEW_KEEP,
                SUPPRESSION_DEMOTED,
                SUPPRESSION_DEMOTED,
                policy_id,
                features,
                validator_enqueue_policy,
            )
        return _make_decision(DROP, HARD_DROP, HARD_DROP, policy_id, features, validator_enqueue_policy)

    if rule.hard_drop_below <= candidate.final_score < rule.old_v1_floor:
        return _make_decision(
            BOUNDARY_REVIEW_KEEP,
            SCORE_BAND,
            _score_band_detail(rule),
            policy_id,
            features,
            validator_enqueue_policy,
        )

    if matched_row_keys:
        return _make_decision(
            BOUNDARY_REVIEW_KEEP,
            PROTECTED_ROW_KEY,
            PROTECTED_ROW_KEY,
            policy_id,
            features,
            validator_enqueue_policy,
        )

    if "neighboring_domain_tag_downweight" in reasons:
        action = _tag_action(candidate, rule)
        if action == "boundary_review":
            return _make_decision(
                BOUNDARY_REVIEW_KEEP,
                TAG_PROTECTION,
                TAG_PROTECTION,
                policy_id,
                features,
                validator_enqueue_policy,
            )
        if action == "boundary_review_when_protected_marker_present":
            if matched_markers:
                return _make_decision(
                    BOUNDARY_REVIEW_KEEP,
                    TAG_PROTECTION,
                    TAG_PROTECTION,
                    policy_id,
                    features,
                    validator_enqueue_policy,
                )
            return _make_decision(DROP, HARD_DROP, HARD_DROP, policy_id, features, validator_enqueue_policy)
        if action == "downrank":
            return _make_decision(DOWNRANK, TAG_PROTECTION, TAG_PROTECTION, policy_id, features, validator_enqueue_policy)
        if action == "hard_negative_unless_protected_marker":
            if matched_markers:
                return _make_decision(
                    BOUNDARY_REVIEW_KEEP,
                    TAG_PROTECTION,
                    TAG_PROTECTION,
                    policy_id,
                    features,
                    validator_enqueue_policy,
                )
            return _make_decision(DROP, HARD_DROP, HARD_DROP, policy_id, features, validator_enqueue_policy)

    if matched_markers:
        return _make_decision(
            BOUNDARY_REVIEW_KEEP,
            PROTECTED_MARKER,
            PROTECTED_MARKER,
            policy_id,
            features,
            validator_enqueue_policy,
        )

    return _make_decision(DROP, HARD_DROP, HARD_DROP, policy_id, features, validator_enqueue_policy)


def _row_with_decision(row: Mapping[str, Any], routing: RoutingDecision) -> dict[str, Any]:
    out = dict(row)
    out.update(
        {
            "retrieval_filter_version": "v2",
            "retrieval_filter_decision": routing.decision,
            "retrieval_routes_to_validator": routing.enters_validator,
            "validator_enqueue_policy": routing.validator_enqueue_policy,
            "validator_enqueue_reason": routing.validator_enqueue_reason,
            "brk_usage": routing.brk_usage,
            "boundary_review_reason": routing.boundary_review_reason,
            "boundary_review_reason_detail": routing.reason_detail,
            "boundary_review_policy": routing.policy_id,
            "boundary_review_features": routing.features,
            "would_be_promotion_authority": False,
            "would_enter_validator": routing.enters_validator,
        }
    )
    return out


def apply_retrieval_filter(
    rows: Iterable[Mapping[str, Any]],
    calibration: Mapping[str, Any],
    *,
    support_by_section_paper: Mapping[tuple[str, str], int] | None = None,
) -> list[dict[str, Any]]:
    routed: list[dict[str, Any]] = []
    validator_enqueue_policy = select_validator_enqueue_policy(calibration)
    for row in rows:
        candidate = retrieval_candidate_from_row(row)
        rule = select_v2_rule(calibration, candidate.section)
        if rule is None:
            routed.append(dict(row))
            continue
        routing = route_candidate_v2(
            candidate,
            rule,
            support_by_section_paper=support_by_section_paper,
            validator_enqueue_policy=validator_enqueue_policy,
        )
        routed.append(_row_with_decision(row, routing))
    return routed


def apply_retrieval_filter_v2(
    rows: Iterable[Mapping[str, Any]],
    calibration: Mapping[str, Any],
    *,
    support_by_section_paper: Mapping[tuple[str, str], int] | None = None,
) -> list[dict[str, Any]]:
    return apply_retrieval_filter(rows, calibration, support_by_section_paper=support_by_section_paper)


def load_calibration(path: Path) -> dict[str, Any]:
    return load_retrieval_calibration(path)


def validate_v2_config(calibration: Mapping[str, Any]) -> None:
    validate_retrieval_filter_v2_config(calibration)


def section_rule(calibration: Mapping[str, Any], section: str) -> BoundaryReviewRule | None:
    return select_v2_rule(calibration, section)


def _rule_from_mapping(rule: Mapping[str, Any]) -> BoundaryReviewRule:
    return BoundaryReviewRule(
        policy_id=str(rule.get("policy_id") or ""),
        hard_drop_below=float(rule.get("hard_drop_below")),
        old_v1_floor=float(rule.get("old_v1_floor")),
        protected_markers=tuple(str(item) for item in (rule.get("protected_markers") or [])),
        marker_match_fields=tuple(str(item) for item in (rule.get("marker_match_fields") or _DEFAULT_MARKER_FIELDS)),
        tag_protection={str(tag): str(action) for tag, action in (rule.get("tag_protection") or {}).items()},
        hard_drop_reasons=("off_domain_enriched_tag_gate", "page_local_paper_suppression"),
        boundary_review_reasons=tuple(str(item) for item in (rule.get("boundary_review_reasons") or [])),
        protected_row_keys=tuple(rule.get("protected_row_keys") or ()),
        legacy_protected_marker_fallback=bool(rule.get("legacy_protected_marker_fallback", False)),
    )


def route_row_v2(
    row: Mapping[str, Any],
    rule: BoundaryReviewRule | Mapping[str, Any] | None,
    support_by_section_paper: Mapping[tuple[str, str], int] | None = None,
) -> RoutingDecision:
    if isinstance(rule, Mapping):
        rule = _rule_from_mapping(rule)
    return route_candidate_v2(
        retrieval_candidate_from_row(row),
        rule,
        support_by_section_paper=support_by_section_paper,
    )


def apply_v2_routing(
    rows: Iterable[Mapping[str, Any]],
    calibration: Mapping[str, Any],
    support_by_section_paper: Mapping[tuple[str, str], int] | None = None,
) -> list[dict[str, Any]]:
    return apply_retrieval_filter(rows, calibration, support_by_section_paper=support_by_section_paper)


def has_protected_marker(row: Mapping[str, Any], rule: BoundaryReviewRule | Mapping[str, Any] | None) -> bool:
    if isinstance(rule, Mapping):
        rule = _rule_from_mapping(rule)
    return bool(_matched_protected_markers(retrieval_candidate_from_row(row), rule))
