#!/usr/bin/env python3
"""Candidate-grounded atom coverage backfill.

This artifact stage bridges retrieval-filter rows and the strict element
validator by extracting row-specific, paper-grounded atoms. It is page-agnostic:
callers provide retrieval/validator pair artifacts and the script emits coverage
artifacts without mutating retrieval-filter or validator DB state.
"""

from __future__ import annotations

import argparse
import datetime as dt
import hashlib
import json
import math
import os
import re
import sys
import time
import urllib.request
from collections import Counter, defaultdict
from pathlib import Path
from typing import Any

import requests

BACKEND_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(BACKEND_ROOT))

from scripts.retrieval_filter_v2 import (
    DEFAULT_COVERAGE_REQUIRED_STAGES,
    ENTAILMENT_GEMINI_BASE,
    ENTAILMENT_GEMINI_MODEL,
    ENTAILMENT_OLLAMA_MODEL,
    ENTAILMENT_TIMEOUT_SECONDS,
    evaluate_entailment_gate,
    evaluate_entailment_gate_gemini,
    evaluate_entailment_gate_openai_compatible,
    row_with_entailment_gate,
)


ARTIFACT_ROOT = Path("/Users/duhokim/.openclaw/workspace/arxiv_wiki_feed_v2")
ATOM_MODEL = os.getenv("ARXIV_WIKI_ATOM_MODEL", "vanta-research/atom-astronomy-7b:latest")
ASTROSAGE_MODEL = os.getenv("ARXIV_WIKI_ASTROSAGE_MODEL", "astrosage-70b:latest")
OLLAMA_BASE = os.getenv("ARXIV_WIKI_OLLAMA_BASE", "http://localhost:11434")
ENTAILMENT_GATE_MODEL = os.getenv("ARXIV_WIKI_ENTAILMENT_MODEL", ENTAILMENT_GEMINI_MODEL)
ENTAILMENT_GATE_TIMEOUT = int(os.getenv("ARXIV_WIKI_ENTAILMENT_TIMEOUT", str(ENTAILMENT_TIMEOUT_SECONDS)))
ENTAILMENT_GATE_PROVIDER = os.getenv("ARXIV_WIKI_ENTAILMENT_PROVIDER", "gemini")
ENTAILMENT_GEMINI_API_KEY_ENV = os.getenv("ARXIV_WIKI_ENTAILMENT_GEMINI_API_KEY_ENV", "NM_GEMINI_API_KEY")
EMBED_MODEL = "nomic-embed-text:v1.5"
PROMPT_VERSION = "candidate_grounded_atom_backfill_v1_20260528"

TERMINAL_STATUSES = {"ready", "missing", "needs_human", "error_terminal"}
STOPWORDS = {
    "the", "and", "or", "of", "in", "to", "a", "an", "for", "with", "by", "at", "as",
    "is", "are", "was", "were", "that", "this", "these", "those", "from", "on", "into",
    "stellar", "star", "stars", "formation", "evolution", "redshift",
}
NUMBER_RE = re.compile(r"(?<![a-z0-9])(?:[<>~=]*\s*)?\d+(?:\.\d+)?(?:\s*[x×]\s*10\^?-?\d+)?", re.I)


def read_jsonl(path: Path) -> list[dict[str, Any]]:
    rows: list[dict[str, Any]] = []
    with path.open("r", encoding="utf-8") as handle:
        for line in handle:
            if line.strip():
                rows.append(json.loads(line))
    return rows


def write_jsonl(path: Path, rows: list[dict[str, Any]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8") as handle:
        for row in rows:
            handle.write(json.dumps(row, ensure_ascii=False, sort_keys=True) + "\n")


def write_json(path: Path, payload: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, indent=2, ensure_ascii=False, sort_keys=True), encoding="utf-8")


def sha_text(value: Any) -> str:
    if value is None:
        value = ""
    if not isinstance(value, str):
        value = json.dumps(value, ensure_ascii=False, sort_keys=True)
    return hashlib.sha256(value.encode("utf-8")).hexdigest()


def env_or_dotenv(name: str | None) -> str | None:
    if not name:
        return None
    value = os.getenv(name)
    if value:
        return value
    env_path = BACKEND_ROOT / ".env"
    if not env_path.exists():
        return None
    for line in env_path.read_text(encoding="utf-8").splitlines():
        stripped = line.strip()
        if not stripped or stripped.startswith("#") or "=" not in stripped:
            continue
        key, raw_value = stripped.split("=", 1)
        if key.strip() != name:
            continue
        return raw_value.strip().strip('"').strip("'") or None
    return None


def hydration_abort(row: dict[str, Any], missing: list[str], source: str | Path | None = None) -> ValueError:
    return ValueError(
        "HYDRATION_ARTIFACT_MISSING_TEXT: regenerate coverage artifact first; "
        f"missing={missing}; "
        f"tuple=({row.get('claim_id')}, {row.get('element_id')}, {row.get('arxiv_id')}); "
        f"source={source or row.get('source_candidate_artifact') or 'unknown'}"
    )


def missing_required_artifact_fields(row: dict[str, Any]) -> list[str]:
    missing = [
        field
        for field in ["claim_text_snapshot", "element_text", "paper_title_snapshot", "paper_abstract_snapshot"]
        if not str(row.get(field) or "").strip()
    ]
    if not isinstance(row.get("required"), bool):
        missing.append("required")
    return missing


def coverage_key(row: dict[str, Any], prompt_version: str, model_version: str) -> str:
    parts = [
        row.get("retrieval_filter_run_id"),
        row.get("claim_id"),
        row.get("element_id"),
        row.get("arxiv_id") or row.get("paper_id"),
        prompt_version,
        model_version,
        sha_text(row.get("claim_text_snapshot")),
        sha_text(row.get("element_text")),
        sha_text(row.get("paper_title_snapshot")),
        sha_text(row.get("paper_abstract_snapshot")),
    ]
    return hashlib.sha256("||".join(str(p or "") for p in parts).encode("utf-8")).hexdigest()


def tokenize(text: Any) -> set[str]:
    if not isinstance(text, str):
        text = json.dumps(text, ensure_ascii=False) if text is not None else ""
    tokens = re.findall(r"[a-z][a-z0-9\-]{2,}", (text or "").lower())
    return {token for token in tokens if token not in STOPWORDS and not token.isdigit()}


def extract_numbers(text: Any) -> set[str]:
    if not isinstance(text, str):
        text = json.dumps(text, ensure_ascii=False) if text is not None else ""
    return {re.sub(r"\s+", "", value.lower()) for value in NUMBER_RE.findall(text.lower())}


def element_support_features(row: dict[str, Any]) -> dict[str, Any]:
    element_blob = " ".join(
        [
            str(row.get("element_text") or ""),
            json.dumps(row.get("normalized_subject"), ensure_ascii=False) if row.get("normalized_subject") is not None else "",
            json.dumps(row.get("normalized_mechanism"), ensure_ascii=False) if row.get("normalized_mechanism") is not None else "",
            json.dumps(row.get("quantity_or_range"), ensure_ascii=False) if row.get("quantity_or_range") is not None else "",
            json.dumps(row.get("redshift_or_environment"), ensure_ascii=False) if row.get("redshift_or_environment") is not None else "",
        ]
    )
    paper_blob = " ".join([str(row.get("paper_title_snapshot") or ""), str(row.get("paper_abstract_snapshot") or "")])
    element_terms = tokenize(element_blob)
    paper_terms = tokenize(paper_blob)
    element_numbers = extract_numbers(element_blob)
    paper_numbers = extract_numbers(paper_blob)
    terms = sorted(element_terms & paper_terms)
    numbers = sorted(element_numbers & paper_numbers)
    return {
        "element_support_terms": terms,
        "element_support_numbers": numbers,
        "element_support_proxy": round(len(terms) / max(1, len(element_terms)), 4),
        "element_support_gate": bool(terms or numbers),
        "element_support_threshold": ">=1_content_token_or_>=1_numeric_literal",
    }


def get_embedding(text: str, model: str = EMBED_MODEL, host: str = OLLAMA_BASE, cache: dict[str, list[float]] | None = None) -> list[float]:
    key = f"{host.rstrip('/')}::{model}::{text or ''}"
    if cache is not None and key in cache:
        return cache[key]
    response = requests.post(
        f"{host.rstrip('/')}/api/embeddings",
        json={"model": model, "prompt": text or ""},
        timeout=30,
    )
    response.raise_for_status()
    embedding = response.json().get("embedding")
    if not isinstance(embedding, list):
        raise ValueError("embedding response missing list")
    values = [float(value) for value in embedding]
    if cache is not None:
        cache[key] = values
    return values


def cosine_similarity(left: list[float], right: list[float]) -> float:
    dot = sum(a * b for a, b in zip(left, right))
    left_mag = math.sqrt(sum(a * a for a in left))
    right_mag = math.sqrt(sum(b * b for b in right))
    if not left_mag or not right_mag:
        return 0.0
    return dot / (left_mag * right_mag)


def semantic_support_features(
    row: dict[str, Any],
    min_semantic_similarity: float,
    ollama_host: str,
    cache: dict[str, list[float]] | None = None,
) -> dict[str, Any]:
    try:
        similarity = cosine_similarity(
            get_embedding(str(row.get("element_text") or ""), host=ollama_host, cache=cache),
            get_embedding(str(row.get("paper_abstract_snapshot") or ""), host=ollama_host, cache=cache),
        )
    except Exception as exc:
        return {
            "coverage_candidate": False,
            "semantic_similarity": None,
            "semantic_similarity_threshold": min_semantic_similarity,
            "semantic_support_status": "embedding_failed",
            "semantic_support_error": str(exc)[:220],
        }
    return {
        "coverage_candidate": similarity >= min_semantic_similarity,
        "semantic_similarity": round(similarity, 6),
        "semantic_similarity_threshold": min_semantic_similarity,
        "semantic_support_status": "semantic_supported" if similarity >= min_semantic_similarity else "semantic_unsupported",
        "semantic_support_error": None,
    }


def deterministic_anchors(row: dict[str, Any]) -> dict[str, Any]:
    """Reuse the existing validator precheck, with numeric anchors added."""
    element_blob = " ".join(
        [
            str(row.get("element_text") or ""),
            json.dumps(row.get("normalized_subject"), ensure_ascii=False) if row.get("normalized_subject") is not None else "",
            json.dumps(row.get("normalized_mechanism"), ensure_ascii=False) if row.get("normalized_mechanism") is not None else "",
            json.dumps(row.get("quantity_or_range"), ensure_ascii=False) if row.get("quantity_or_range") is not None else "",
            json.dumps(row.get("redshift_or_environment"), ensure_ascii=False) if row.get("redshift_or_environment") is not None else "",
        ]
    )
    paper_blob = " ".join([str(row.get("paper_title_snapshot") or ""), str(row.get("paper_abstract_snapshot") or "")])
    element_terms = tokenize(element_blob)
    paper_terms = tokenize(paper_blob)
    element_numbers = extract_numbers(element_blob)
    paper_numbers = extract_numbers(paper_blob)
    term_overlap = sorted(element_terms & paper_terms)
    number_overlap = sorted(element_numbers & paper_numbers)
    return {
        "term_overlap": term_overlap,
        "number_overlap": number_overlap,
        "has_anchor_overlap": bool(term_overlap or number_overlap),
        "element_token_count": len(element_terms),
        "paper_token_count": len(paper_terms),
    }


def normalize_support_relation(value: Any) -> str:
    relation = str(value or "absent").strip().lower()
    if relation not in {"direct", "partial", "absent"}:
        return "absent"
    return relation


def normalize_coverage_payload(payload: dict[str, Any]) -> dict[str, Any]:
    status = str(payload.get("candidate_atom_coverage_status") or payload.get("status") or "needs_human").strip().lower()
    if status not in {"ready", "missing", "needs_human", "error_retryable", "error_terminal"}:
        status = "needs_human"
    atoms: list[dict[str, Any]] = []
    for atom in payload.get("candidate_atoms") or []:
        if not isinstance(atom, dict):
            continue
        relation = normalize_support_relation(atom.get("support_relation"))
        confidence = atom.get("confidence", 0.0)
        try:
            confidence = max(0.0, min(1.0, float(confidence)))
        except Exception:
            confidence = 0.0
        text = str(atom.get("atom_text") or "").strip()
        if not text:
            continue
        atoms.append(
            {
                "atom_text": text[:800],
                "atom_type": str(atom.get("atom_type") or "candidate_grounded").strip()[:80],
                "evidence_anchor_terms": sorted({str(v).strip().lower() for v in atom.get("evidence_anchor_terms") or [] if str(v).strip()})[:20],
                "evidence_anchor_numbers": sorted({str(v).strip() for v in atom.get("evidence_anchor_numbers") or [] if str(v).strip()})[:20],
                "quoted_span_or_null": atom.get("quoted_span_or_null"),
                "support_relation": relation,
                "confidence": round(confidence, 4),
            }
        )
    if status == "ready" and not any(atom["support_relation"] in {"direct", "partial"} for atom in atoms):
        status = "missing"
    if status == "missing":
        atoms = [atom for atom in atoms if atom["support_relation"] != "absent"]
    return {
        "candidate_atom_coverage_status": status,
        "candidate_atoms": atoms,
        "rationale": str(payload.get("rationale") or "")[:1200],
        "failure_mode": payload.get("failure_mode"),
    }


def coverage_contract_fields(row: dict[str, Any], coverage_status: str, coverage_key_value: str, reason: str | None = None) -> dict[str, Any]:
    stages = list(DEFAULT_COVERAGE_REQUIRED_STAGES)
    if coverage_status == "coverage_ready":
        statuses = {stage: "ready" for stage in stages}
    elif coverage_status == "coverage_blocked_retryable":
        statuses = {stage: "ready" for stage in stages}
        statuses["atom_decomposition"] = "blocked_retryable"
    else:
        statuses = {stage: "ready" for stage in stages}
        statuses["atom_decomposition"] = "blocked_terminal"
    missing = [stage for stage in stages if statuses[stage] != "ready"]
    refs = {
        stage: {
            "stage": stage,
            "status": statuses[stage],
            "cache_key": coverage_key_value if stage == "atom_decomposition" else sha_text(
                {
                    "stage": stage,
                    "claim_id": row.get("claim_id"),
                    "element_id": row.get("element_id"),
                    "arxiv_id": row.get("arxiv_id"),
                    "element_text_hash": sha_text(row.get("element_text")),
                    "paper_abstract_hash": sha_text(row.get("paper_abstract_snapshot")),
                    "prompt_version": PROMPT_VERSION,
                    "model_version": ATOM_MODEL if stage == "atom_decomposition" else "deterministic_v1",
                }
            ),
            "reason": reason,
        }
        for stage in stages
    }
    return {
        "coverage_status": coverage_status,
        "coverage_required_stages": stages,
        "coverage_missing_stages": missing,
        "coverage_stage_statuses": statuses,
        "coverage_artifact_refs": refs,
    }


def extract_json_object(text_value: str) -> dict[str, Any]:
    text_value = (text_value or "").strip()
    if not text_value:
        raise ValueError("empty model response")
    decoder = json.JSONDecoder()
    try:
        parsed, _end = decoder.raw_decode(text_value)
        if isinstance(parsed, dict):
            return parsed
    except json.JSONDecodeError:
        start = text_value.find("{")
        end = text_value.rfind("}")
        if start < 0 or end <= start:
            raise
        return json.loads(text_value[start : end + 1])
    raise ValueError("model response did not start with a JSON object")


def ollama_chat(model: str, prompt: str, timeout: int) -> tuple[str, float]:
    payload = {
        "model": model,
        "messages": [{"role": "user", "content": prompt}],
        "stream": False,
        "options": {"temperature": 0.0, "num_ctx": 4096, "num_predict": 420},
    }
    request = urllib.request.Request(
        f"{OLLAMA_BASE}/api/chat",
        data=json.dumps(payload).encode("utf-8"),
        headers={"Content-Type": "application/json"},
        method="POST",
    )
    started = time.time()
    with urllib.request.urlopen(request, timeout=timeout) as response:
        raw = response.read().decode("utf-8", errors="replace")
    parsed = json.loads(raw)
    return ((parsed.get("message") or {}).get("content") or "").strip(), round(time.time() - started, 3)


def backfill_prompt(row: dict[str, Any], anchors: dict[str, Any]) -> str:
    return f"""You are Atom-7B extracting candidate-grounded astronomy evidence atoms.

Use only the paper title and abstract. Do not invent support. If the paper does
not support this claim element, return missing with no validator-ready atom.

Respond with JSON only:
{{
  "candidate_atom_coverage_status": "ready|missing|needs_human|error_retryable|error_terminal",
  "candidate_atoms": [
    {{
      "atom_text": "single citation-checkable atom grounded in this paper",
      "atom_type": "subject|mechanism|quantity_or_threshold|relationship|redshift_or_environment|candidate_grounded",
      "evidence_anchor_terms": ["term"],
      "evidence_anchor_numbers": ["number"],
      "quoted_span_or_null": "exact short abstract span or null",
      "support_relation": "direct|partial|absent",
      "confidence": 0.0
    }}
  ],
  "rationale": "brief reason",
  "failure_mode": null
}}

Rules:
- ready: at least one atom is directly or partially supported by the paper.
- missing: title/abstract do not support the element.
- needs_human: ambiguous, malformed, or requires full text.
- Prefer direct atoms that preserve the element's subject, mechanism, quantity, and regime.
- Keep atom_text short and citation-checkable.

Claim:
{row.get("claim_text_snapshot")}

Element:
- id: {row.get("element_id")}
- type: {row.get("element_type")}
- text: {row.get("element_text")}
- normalized_subject: {row.get("normalized_subject")}
- normalized_mechanism: {row.get("normalized_mechanism")}
- quantity_or_range: {json.dumps(row.get("quantity_or_range"), ensure_ascii=False)}
- redshift_or_environment: {json.dumps(row.get("redshift_or_environment"), ensure_ascii=False)}

Deterministic anchors:
- terms: {anchors.get("term_overlap")}
- numbers: {anchors.get("number_overlap")}

Paper:
- arXiv: {row.get("arxiv_id")}
- title: {row.get("paper_title_snapshot")}
- abstract: {row.get("paper_abstract_snapshot")}
"""


def coverage_row(
    row: dict[str, Any],
    coverage_run_id: str,
    model: str = ATOM_MODEL,
    timeout: int = 180,
    use_model: bool = True,
) -> dict[str, Any]:
    anchors = deterministic_anchors(row)

    missing = missing_required_artifact_fields(row)
    if missing:
        raise hydration_abort(row, missing)

    base_coverage_key = coverage_key(row, PROMPT_VERSION, model)
    base = {
        "coverage_run_id": coverage_run_id,
        "retrieval_filter_run_id": row.get("retrieval_filter_run_id"),
        "claim_id": row.get("claim_id"),
        "element_id": row.get("element_id"),
        "arxiv_id": row.get("arxiv_id"),
        "section": row.get("section"),
        "retrieval_filter_decision": row.get("retrieval_filter_decision"),
        "source_label": row.get("label"),
        "candidate_source": row.get("candidate_source"),
        "candidate_key": row.get("candidate_key"),
        "entailment_gate_model": row.get("entailment_gate_model"),
        "entailment_gate_decision": row.get("entailment_gate_decision"),
        "entailment_gate_reason": row.get("entailment_gate_reason"),
        "entailment_gate_error": row.get("entailment_gate_error"),
        "entailment_gate_latency_seconds": row.get("entailment_gate_latency_seconds"),
        "entailment_gate_prompt_tokens": row.get("entailment_gate_prompt_tokens"),
        "entailment_gate_completion_tokens": row.get("entailment_gate_completion_tokens"),
        "entailment_gate_total_tokens": row.get("entailment_gate_total_tokens"),
        "coverage_key": base_coverage_key,
        "backfill_model": model,
        "audit_model_reserved": ASTROSAGE_MODEL,
        "backfill_prompt_version": PROMPT_VERSION,
        "deterministic_anchors": anchors,
        
        "claim_text_snapshot": row.get("claim_text_snapshot"),
        "element_text": row.get("element_text"),
        "element_type": row.get("element_type"),
        "required": row.get("required"),
        "paper_title_snapshot": row.get("paper_title_snapshot"),
        "paper_abstract_snapshot": row.get("paper_abstract_snapshot"),
        "matched_terms": row.get("matched_terms"),
        "element_matched_terms": row.get("element_matched_terms"),
        
        "source_hashes": {
            "claim_text_hash": sha_text(row.get("claim_text_snapshot")),
            "element_text_hash": sha_text(row.get("element_text")),
            "paper_title_hash": sha_text(row.get("paper_title_snapshot")),
            "paper_abstract_hash": sha_text(row.get("paper_abstract_snapshot")),
        },
        "hydration_sources": {
            "claim_text": "artifact",
            "element_text": "artifact",
            "paper_title": "artifact",
            "paper_abstract": "artifact"
        },
        "hydration_db_reads_used": False,
        "hydration_policy": "artifact_only_fail_closed",
        
        "created_at": dt.datetime.now(dt.timezone.utc).isoformat(),
    }

    if not anchors["has_anchor_overlap"]:
        return {
            **base,
            **coverage_contract_fields(row, "coverage_blocked_terminal", base_coverage_key, "anchor_overlap_missing"),
            "candidate_atom_coverage_status": "missing",
            "candidate_atoms": [],
            "rationale": "No lexical or numeric anchor overlap between element and title/abstract.",
            "failure_mode": None,
            "latency_seconds": 0.0,
        }
    if not use_model:
        return {
            **base,
            **coverage_contract_fields(row, "coverage_blocked_retryable", base_coverage_key, "model_disabled"),
            "candidate_atom_coverage_status": "needs_human",
            "candidate_atoms": [],
            "rationale": "Model execution disabled for dry-run plumbing.",
            "failure_mode": "model_disabled",
            "latency_seconds": 0.0,
        }
    started = time.time()
    raw = ""
    try:
        raw, latency = ollama_chat(model, backfill_prompt(row, anchors), timeout)
        normalized = normalize_coverage_payload(extract_json_object(raw))
        status = normalized.get("candidate_atom_coverage_status")
        coverage_status = "coverage_ready" if status == "ready" else "coverage_blocked_terminal"
        if status in {"needs_human", "error_retryable"}:
            coverage_status = "coverage_blocked_retryable"
        return {
            **base,
            **coverage_contract_fields(row, coverage_status, base_coverage_key, status),
            **normalized,
            "raw_response": raw,
            "latency_seconds": latency,
        }
    except Exception as exc:
        return {
            **base,
            **coverage_contract_fields(row, "coverage_blocked_retryable", base_coverage_key, "model_call_or_parse_failed"),
            "candidate_atom_coverage_status": "error_retryable",
            "candidate_atoms": [],
            "rationale": "Model call or parse failed.",
            "failure_mode": str(exc)[:300],
            "raw_response": raw,
            "latency_seconds": round(time.time() - started, 3),
        }


def collect_rows_from_validator_artifacts(
    source_dir: Path,
    retrieval_run_id: int = 6,
    min_semantic_similarity: float = 0.50,
    ollama_host: str = OLLAMA_BASE,
    enable_entailment_gate: bool = True,
    entailment_model: str = ENTAILMENT_GATE_MODEL,
    entailment_timeout: int = ENTAILMENT_GATE_TIMEOUT,
    entailment_ollama_host: str | None = None,
    entailment_provider: str = ENTAILMENT_GATE_PROVIDER,
    entailment_base_url: str | None = None,
    entailment_api_key: str | None = None,
    section: str | None = None,
    limit: int = 0,
) -> dict[str, list[dict[str, Any]]]:
    rows: list[dict[str, Any]] = []
    audit_rows: list[dict[str, Any]] = []
    excluded_rows: list[dict[str, Any]] = []
    seen: set[tuple[Any, ...]] = set()
    retrieval_index = load_retrieval_index(source_dir)
    embedding_cache: dict[str, list[float]] = {}
    main_candidates_seen = 0
    # batch guard — prevents accidentally routing expensive preview/pro models into high-volume loops.
    # Fails fast at the top of the row-iteration loop before any API spend.
    if enable_entailment_gate and entailment_provider in ("gemini", "openai_compatible"):
        from app.utils.model_guard import guard_batch_model
        entailment_model = guard_batch_model(
            entailment_model,
            "candidate_grounded_atom_backfill.collect_rows_from_validator_artifacts",
        )
    for subdir in ["validator_brk_run", "validator_firm_keep_run"]:
        pair_path = source_dir / subdir / "element_candidate_pairs.jsonl"
        if not pair_path.exists():
            continue
        retrieval_decision = "boundary_review_keep" if subdir == "validator_brk_run" else "keep"
        for row in read_jsonl(pair_path):
            key = (row.get("candidate_key"), row.get("claim_id"), row.get("element_id"), row.get("arxiv_id"))
            if key in seen:
                continue
            seen.add(key)
            retrieval_meta = retrieval_index.get((int(row.get("claim_id")), row.get("element_id"), row.get("arxiv_id"))) or {}
            hydrated = {
                **row,
                "retrieval_filter_run_id": retrieval_run_id,
                "retrieval_filter_decision": retrieval_meta.get("retrieval_filter_decision") or retrieval_decision,
                "section": retrieval_meta.get("section") or (row.get("boundary_review_features") or {}).get("section") or row.get("section"),
                "label": retrieval_meta.get("label") or row.get("label"),
                "final_score": retrieval_meta.get("final_score"),
                "source_validator_subdir": subdir,
            }
            support = element_support_features(hydrated)
            hydrated.update({key: hydrated.get(key, value) for key, value in support.items()})
            semantic_support = semantic_support_features(hydrated, min_semantic_similarity, ollama_host, embedding_cache)
            hydrated.update(semantic_support)
            if section and hydrated.get("section") != section:
                continue
            if hydrated.get("label") == "off_domain":
                excluded_rows.append({**hydrated, "coverage_queue_exclusion_reason": "off_domain"})
                continue
            if subdir == "validator_brk_run" or hydrated.get("retrieval_filter_decision") == "boundary_review_keep":
                audit_rows.append({**hydrated, "coverage_surface": "audit_only"})
                continue
            if hydrated.get("coverage_candidate") is False:
                excluded_rows.append(
                    {
                        **hydrated,
                        "retrieval_filter_decision": "semantic_unsupported",
                        "coverage_queue_exclusion_reason": "semantic_unsupported",
                    }
                )
                continue
            main_candidates_seen += 1
            if limit and main_candidates_seen > limit:
                continue
            if enable_entailment_gate:
                if entailment_provider == "gemini":
                    api_key = entailment_api_key or env_or_dotenv(ENTAILMENT_GEMINI_API_KEY_ENV) or env_or_dotenv("GEMINI_API_KEY")
                    if not api_key:
                        from scripts.retrieval_filter_v2 import EntailmentGateResult

                        gate = EntailmentGateResult(
                            entailment="error",
                            error=f"ValueError: Gemini API key missing; set {ENTAILMENT_GEMINI_API_KEY_ENV} or GEMINI_API_KEY",
                            latency_seconds=0.0,
                        )
                    else:
                        gate = evaluate_entailment_gate_gemini(
                            hydrated,
                            model=entailment_model,
                            base_url=entailment_base_url or ENTAILMENT_GEMINI_BASE,
                            api_key=api_key,
                            timeout=entailment_timeout,
                        )
                elif entailment_provider == "openai_compatible":
                    if not entailment_base_url or not entailment_api_key:
                        from scripts.retrieval_filter_v2 import EntailmentGateResult

                        gate = EntailmentGateResult(
                            entailment="error",
                            error="ValueError: entailment openai-compatible base URL or API key missing",
                            latency_seconds=0.0,
                        )
                    else:
                        gate = evaluate_entailment_gate_openai_compatible(
                            hydrated,
                            model=entailment_model,
                            base_url=entailment_base_url,
                            api_key=entailment_api_key,
                            timeout=entailment_timeout,
                        )
                else:
                    gate = evaluate_entailment_gate(
                        hydrated,
                        model=entailment_model,
                        ollama_base=entailment_ollama_host or ollama_host,
                        timeout=entailment_timeout,
                    )
                gated = row_with_entailment_gate(hydrated, gate, entailment_model)
                if not gate.admits_coverage:
                    excluded_rows.append(
                        {
                            **gated,
                            "coverage_queue_exclusion_reason": gate.exclusion_reason,
                        }
                    )
                    continue
                hydrated = gated
            rows.append({**hydrated, "coverage_surface": "main"})
    for bucket in (rows, audit_rows, excluded_rows):
        bucket.sort(key=lambda r: (str(r.get("section")), int(r.get("claim_id") or 0), str(r.get("element_id")), str(r.get("arxiv_id"))))
    return {"main": rows, "audit_only": audit_rows, "excluded": excluded_rows}


def load_rows_from_validator_artifacts(source_dir: Path, retrieval_run_id: int = 6) -> list[dict[str, Any]]:
    return collect_rows_from_validator_artifacts(source_dir, retrieval_run_id)["main"]


def hydration_manifest(
    source_dir: Path,
    out_dir: Path,
    coverage_rows: list[dict[str, Any]],
    ready_rows: list[dict[str, Any]],
    args: argparse.Namespace,
    audit_rows: list[dict[str, Any]] | None = None,
    excluded_rows: list[dict[str, Any]] | None = None,
    audit_missing_input_rows: list[dict[str, Any]] | None = None,
) -> dict[str, Any]:
    source_paths = [
        source_dir / "validator_brk_run" / "element_candidate_pairs.jsonl",
        source_dir / "validator_firm_keep_run" / "element_candidate_pairs.jsonl",
        source_dir / "retrieval_filter_v2_ship_routed_rows.jsonl",
    ]
    sources = []
    for path in source_paths:
        if path.exists():
            sources.append(
                {
                    "path": str(path),
                    "row_count": len(read_jsonl(path)),
                    "sha256": sha_text(path.read_text(encoding="utf-8")),
                }
            )
        else:
            sources.append({"path": str(path), "row_count": 0, "missing": True})
    manifest = {
        "coverage_run_id": out_dir.name,
        "created_at": dt.datetime.now(dt.timezone.utc).isoformat(),
        "source_dir": str(source_dir),
        "source_artifacts": sources,
        "coverage_rows": len(coverage_rows),
        "validator_ready_rows": len(ready_rows),
        "audit_only_coverage_rows": len(audit_rows or []),
        "audit_only_missing_input_rows": len(audit_missing_input_rows or []),
        "excluded_rows": len(excluded_rows or []),
        "excluded_reason_counts": dict(Counter(row.get("coverage_queue_exclusion_reason") for row in (excluded_rows or []))),
        "hydration_policy": "artifact_only_fail_closed",
        "hydration_db_reads_used": False,
        "db_reads_used": False,
        "db_writes_used": False,
        "no_db_write": True,
        "model": args.model,
        "min_semantic_similarity": getattr(args, "min_semantic_similarity", 0.50),
        "ollama_host": getattr(args, "ollama_host", OLLAMA_BASE),
        "entailment_gate_enabled": not getattr(args, "no_entailment_gate", True),
        "entailment_gate_provider": getattr(args, "entailment_provider", ENTAILMENT_GATE_PROVIDER),
        "entailment_gate_model": getattr(args, "entailment_model", ENTAILMENT_GATE_MODEL),
        "entailment_gate_timeout": getattr(args, "entailment_timeout", ENTAILMENT_GATE_TIMEOUT),
        "entailment_ollama_host": getattr(args, "entailment_ollama_host", None) or getattr(args, "ollama_host", OLLAMA_BASE),
        "entailment_base_url": getattr(args, "entailment_base_url", None),
        "prompt_version": PROMPT_VERSION,
    }
    write_json(out_dir / "hydration_manifest.json", manifest)
    return manifest


def load_retrieval_index(source_dir: Path) -> dict[tuple[int, str, str], dict[str, Any]]:
    index: dict[tuple[int, str, str], dict[str, Any]] = {}
    path = source_dir / "retrieval_filter_v2_ship_routed_rows.jsonl"
    if not path.exists():
        return index
    for row in read_jsonl(path):
        arxiv_id = row.get("arxiv_id") or row.get("paper_id")
        if not arxiv_id:
            continue
        meta = {
            "section": row.get("section"),
            "label": row.get("label"),
            "retrieval_filter_decision": row.get("retrieval_filter_decision"),
            "final_score": row.get("final_score"),
        }
        key = (int(row.get("claim_id")), row.get("element_id"), arxiv_id)
        index[key] = meta
        if "v" in arxiv_id:
            index[(int(row.get("claim_id")), row.get("element_id"), arxiv_id.split("v")[0])] = meta
    return index


def summarize_coverage(rows: list[dict[str, Any]]) -> dict[str, Any]:
    total = len(rows)
    statuses = Counter(row.get("candidate_atom_coverage_status") for row in rows)
    by_section: dict[str, dict[str, Any]] = {}
    for section, section_rows in group_by(rows, "section").items():
        section_statuses = Counter(row.get("candidate_atom_coverage_status") for row in section_rows)
        ready = section_statuses.get("ready", 0)
        by_section[section] = {
            "rows": len(section_rows),
            "ready": ready,
            "missing": section_statuses.get("missing", 0),
            "needs_human": section_statuses.get("needs_human", 0),
            "error_retryable": section_statuses.get("error_retryable", 0),
            "error_terminal": section_statuses.get("error_terminal", 0),
            "ready_rate": round(ready / len(section_rows), 4) if section_rows else 0.0,
        }
    non_off = [row for row in rows if row.get("source_label") != "off_domain"]
    terminal = sum(statuses.get(status, 0) for status in TERMINAL_STATUSES)
    retryable = statuses.get("error_retryable", 0)
    ready_non_off = sum(1 for row in non_off if row.get("candidate_atom_coverage_status") == "ready")
    return {
        "row_count": total,
        "status_counts": dict(statuses),
        "terminal_or_ready_coverage": round(terminal / total, 4) if total else 0.0,
        "retryable_error_rate": round(retryable / total, 4) if total else 0.0,
        "non_off_domain_rows": len(non_off),
        "non_off_domain_ready": ready_non_off,
        "non_off_domain_ready_rate": round(ready_non_off / len(non_off), 4) if non_off else 0.0,
        "acceptance": {
            "terminal_or_ready_ge_95pct": (terminal / total) >= 0.95 if total else False,
            "retryable_errors_le_2pct": (retryable / total) <= 0.02 if total else False,
            "non_off_domain_ready_ge_80pct": (ready_non_off / len(non_off)) >= 0.80 if non_off else False,
        },
        "by_section": by_section,
    }


def group_by(rows: list[dict[str, Any]], key: str) -> dict[str, list[dict[str, Any]]]:
    grouped: dict[str, list[dict[str, Any]]] = defaultdict(list)
    for row in rows:
        grouped[str(row.get(key) or "unknown")].append(row)
    return dict(grouped)


def write_report(out_dir: Path, coverage_rows: list[dict[str, Any]], args: argparse.Namespace) -> dict[str, Any]:
    summary = summarize_coverage(coverage_rows)
    audit_rows = read_jsonl(out_dir / "audit_only_coverage_rows.jsonl") if (out_dir / "audit_only_coverage_rows.jsonl").exists() else []
    audit_missing_rows = read_jsonl(out_dir / "audit_only_missing_input_rows.jsonl") if (out_dir / "audit_only_missing_input_rows.jsonl").exists() else []
    excluded_rows = read_jsonl(out_dir / "excluded_coverage_rows.jsonl") if (out_dir / "excluded_coverage_rows.jsonl").exists() else []
    excluded_counts = Counter(row.get("coverage_queue_exclusion_reason") for row in excluded_rows)
    payload = {
        "coverage_run_id": out_dir.name,
        "created_at": dt.datetime.now(dt.timezone.utc).isoformat(),
        "source_dir": str(args.source_dir),
        "retrieval_filter_run_id": args.retrieval_run_id,
        "model": args.model,
        "prompt_version": PROMPT_VERSION,
        "entailment_gate_enabled": not getattr(args, "no_entailment_gate", True),
        "entailment_gate_provider": getattr(args, "entailment_provider", ENTAILMENT_GATE_PROVIDER),
        "entailment_gate_model": getattr(args, "entailment_model", ENTAILMENT_GATE_MODEL),
        "entailment_ollama_host": getattr(args, "entailment_ollama_host", None) or getattr(args, "ollama_host", OLLAMA_BASE),
        "entailment_base_url": getattr(args, "entailment_base_url", None),
        "no_db_writes": True,
        "summary": summary,
        "audit_only": {
            "coverage_rows": len(audit_rows),
            "missing_input_rows": len(audit_missing_rows),
            "status_counts": dict(Counter(row.get("candidate_atom_coverage_status") for row in audit_rows)),
            "ready_rows": sum(1 for row in audit_rows if row.get("candidate_atom_coverage_status") == "ready"),
            "counted_in_ready_rate": False,
        },
        "excluded": {
            "rows": len(excluded_rows),
            "reason_counts": dict(excluded_counts),
            "counted_in_ready_rate": False,
        },
    }
    write_json(out_dir / "coverage_summary.json", payload)
    lines = [
        "# Candidate-Grounded Atom Backfill",
        "",
        f"- Coverage run id: `{out_dir.name}`",
        f"- Source dir: `{args.source_dir}`",
        f"- Retrieval-filter run id: `{args.retrieval_run_id}`",
        f"- Model: `{args.model}`",
        f"- Prompt version: `{PROMPT_VERSION}`",
        "- DB writes: `false`",
        "",
        "## Coverage Gate",
        "",
        f"- Rows: `{summary['row_count']}`",
        f"- Terminal/ready coverage: `{summary['terminal_or_ready_coverage']}`",
        f"- Retryable error rate: `{summary['retryable_error_rate']}`",
        f"- Non-off-domain ready rate: `{summary['non_off_domain_ready_rate']}`",
        f"- Gate terminal >=95%: `{summary['acceptance']['terminal_or_ready_ge_95pct']}`",
        f"- Gate retryable <=2%: `{summary['acceptance']['retryable_errors_le_2pct']}`",
        f"- Gate non-off-domain ready >=80%: `{summary['acceptance']['non_off_domain_ready_ge_80pct']}`",
        f"- Audit-only coverage rows: `{len(audit_rows)}` (not counted in readiness gate)",
        f"- Audit-only missing-input rows: `{len(audit_missing_rows)}` (not counted in readiness gate)",
        f"- Excluded rows: `{len(excluded_rows)}` (not counted in readiness gate)",
        "",
        "## Status Counts",
        "",
        "| status | rows |",
        "|---|---:|",
    ]
    for status, count in sorted(summary["status_counts"].items()):
        lines.append(f"| `{status}` | {count} |")
    lines.extend(["", "## Excluded Queue Rows", "", "| reason | rows |", "|---|---:|"])
    for reason, count in sorted(excluded_counts.items()):
        lines.append(f"| `{reason}` | {count} |")
    lines.extend(["", "## Audit-Only Coverage", "", "These rows are retained for observability only. They do not feed validator-ready rows, readiness-rate gates, or promotion.", "", "| status | rows |", "|---|---:|"])
    for status, count in sorted(Counter(row.get("candidate_atom_coverage_status") for row in audit_rows).items()):
        lines.append(f"| `{status}` | {count} |")
    lines.extend(["", "## Per Section", "", "| section | rows | ready | missing | needs_human | retryable | terminal_error | ready_rate |", "|---|---:|---:|---:|---:|---:|---:|---:|"])
    for section, row in sorted(summary["by_section"].items()):
        lines.append(
            f"| `{section}` | {row['rows']} | {row['ready']} | {row['missing']} | {row['needs_human']} | "
            f"{row['error_retryable']} | {row['error_terminal']} | {row['ready_rate']} |"
        )
    (out_dir / "REPORT.md").write_text("\n".join(lines) + "\n", encoding="utf-8")
    return payload


def run_backfill(args: argparse.Namespace) -> dict[str, Any]:
    out_dir = args.out_dir or ARTIFACT_ROOT / f"candidate_grounded_atom_backfill_{dt.datetime.now(dt.timezone.utc).strftime('%Y%m%dT%H%M%SZ')}"
    out_dir.mkdir(parents=True, exist_ok=True)
    min_semantic_similarity = getattr(args, "min_semantic_similarity", 0.50)
    ollama_host = getattr(args, "ollama_host", OLLAMA_BASE)
    enable_entailment_gate = not getattr(args, "no_entailment_gate", True)
    entailment_model = getattr(args, "entailment_model", ENTAILMENT_GATE_MODEL)
    entailment_timeout = getattr(args, "entailment_timeout", ENTAILMENT_GATE_TIMEOUT)
    entailment_ollama_host = getattr(args, "entailment_ollama_host", None) or ollama_host
    entailment_provider = getattr(args, "entailment_provider", ENTAILMENT_GATE_PROVIDER)
    if entailment_provider == "gemini" and entailment_model == ENTAILMENT_OLLAMA_MODEL:
        entailment_model = ENTAILMENT_GEMINI_MODEL
        args.entailment_model = entailment_model
    entailment_base_url = getattr(args, "entailment_base_url", None)
    entailment_api_key = env_or_dotenv(getattr(args, "entailment_api_key_env", None))
    collected = collect_rows_from_validator_artifacts(
        args.source_dir,
        args.retrieval_run_id,
        min_semantic_similarity,
        ollama_host,
        enable_entailment_gate,
        entailment_model,
        entailment_timeout,
        entailment_ollama_host,
        entailment_provider,
        entailment_base_url,
        entailment_api_key,
        args.section,
        args.limit,
    )
    rows = collected["main"]
    audit_input_rows = collected["audit_only"]
    excluded_rows = collected["excluded"]
    coverage_rows: list[dict[str, Any]] = []
    for index, row in enumerate(rows, 1):
        if args.progress_every and index > 1 and (index - 1) % args.progress_every == 0:
            print(json.dumps({"processed": index - 1, "total": len(rows), "out_dir": str(out_dir)}, sort_keys=True), flush=True)
        coverage_rows.append(coverage_row(row, out_dir.name, args.model, args.timeout, not args.no_model))
    write_jsonl(out_dir / "coverage_rows.jsonl", coverage_rows)
    audit_missing_input_rows = []
    audit_hydratable_rows = []
    for row in audit_input_rows:
        missing = missing_required_artifact_fields(row)
        if missing:
            audit_missing_input_rows.append({**row, "audit_only_missing_fields": missing})
        else:
            audit_hydratable_rows.append(row)
    audit_rows = [coverage_row(row, out_dir.name, args.model, args.timeout, not args.no_model) for row in audit_hydratable_rows]
    write_jsonl(out_dir / "audit_only_coverage_rows.jsonl", audit_rows)
    write_jsonl(out_dir / "audit_only_missing_input_rows.jsonl", audit_missing_input_rows)
    write_jsonl(out_dir / "excluded_coverage_rows.jsonl", excluded_rows)
    ready_rows = []
    for r in coverage_rows:
        if r.get("candidate_atom_coverage_status") == "ready":
            # Must have at least one valid atom
            valid_atoms = [a for a in r.get("candidate_atoms", []) if a.get("support_relation") in {"direct", "partial"} and (a.get("evidence_anchor_terms") or a.get("evidence_anchor_numbers") or a.get("quoted_span_or_null"))]
            sh = r.get("source_hashes", {})
            if valid_atoms and all(sh.values()) and r.get("coverage_key"):
                ready_rows.append(r)
    write_jsonl(out_dir / "validator_ready_rows.jsonl", ready_rows)
    hydration_manifest(args.source_dir, out_dir, coverage_rows, ready_rows, args, audit_rows, excluded_rows, audit_missing_input_rows)
    return write_report(out_dir, coverage_rows, argparse.Namespace(**{**vars(args), "out_dir": out_dir}))


def main() -> None:
    parser = argparse.ArgumentParser(description="Candidate-grounded atom coverage backfill.")
    parser.add_argument("--source-dir", type=Path, required=True)
    parser.add_argument("--out-dir", type=Path)
    parser.add_argument("--retrieval-run-id", type=int, default=6)
    parser.add_argument("--section")
    parser.add_argument("--limit", type=int, default=0)
    parser.add_argument("--model", default=ATOM_MODEL)
    parser.add_argument("--timeout", type=int, default=180)
    parser.add_argument("--no-model", action="store_true", help="Run deterministic anchors only; model rows become needs_human.")
    parser.add_argument("--progress-every", type=int, default=25)
    parser.add_argument("--min-semantic-similarity", type=float, default=0.50)
    parser.add_argument("--ollama-host", default=OLLAMA_BASE)
    parser.add_argument("--no-entailment-gate", action="store_true", help="Disable the post-semantic entailment gate.")
    parser.add_argument("--entailment-model", default=ENTAILMENT_GATE_MODEL)
    parser.add_argument("--entailment-timeout", type=int, default=ENTAILMENT_GATE_TIMEOUT)
    parser.add_argument("--entailment-ollama-host", default=None)
    parser.add_argument("--entailment-provider", choices=["ollama", "openai_compatible", "gemini"], default=ENTAILMENT_GATE_PROVIDER)
    parser.add_argument("--entailment-base-url", default=None)
    parser.add_argument("--entailment-api-key-env", default=None)
    args = parser.parse_args()
    payload = run_backfill(args)
    print(json.dumps(payload, indent=2, ensure_ascii=False, sort_keys=True))


if __name__ == "__main__":
    main()
