#!/usr/bin/env python3
"""Mode-1 page 57 atomization + element-scoped coverage recovery.

This script writes artifacts under the OpenClaw workspace and never writes
Evidence, page content, trust, marker, renovation, cron, or routing state.
Coverage-table writes are opt-in and mirror the existing coverage materializer.
"""

from __future__ import annotations

import argparse
import collections
import datetime as dt
import json
import sys
import time
from pathlib import Path
from typing import Any

from sqlalchemy import text

BACKEND_ROOT = Path(__file__).resolve().parents[1]
SCRIPTS_DIR = BACKEND_ROOT / "scripts"
sys.path.insert(0, str(SCRIPTS_DIR))
sys.path.insert(0, str(BACKEND_ROOT))

from app.database import SessionLocal
from scripts import arxiv_wiki_feed_v2_atomize as atomize
from scripts.candidate_grounded_atom_backfill import (
    ATOM_MODEL,
    PROMPT_VERSION as COVERAGE_PROMPT_VERSION,
    coverage_key,
    coverage_row,
    deterministic_anchors,
    get_embedding,
    semantic_support_features,
    sha_text,
)


ARTIFACT_ROOT = Path("/Users/duhokim/.openclaw/workspace/arxiv_wiki_feed_v2")
DEFAULT_EXISTING_ELEMENT_PATHS = [
    ARTIFACT_ROOT / "atomize_galaxy_evolution_20260524T174549Z" / "elements.jsonl",
    ARTIFACT_ROOT / "atomize_galaxy_evolution_20260524T174549Z_phase15_retry_20260524T235035Z" / "elements.jsonl",
    ARTIFACT_ROOT / "atomize_galaxy_evolution_20260524T174549Z_phase15_retry_20260525T071909Z" / "elements.jsonl",
]
PAGE_ID = 57


def utc_stamp() -> str:
    return dt.datetime.now(dt.UTC).strftime("%Y%m%dT%H%M%SZ")


def read_jsonl(path: Path) -> list[dict[str, Any]]:
    if not path.exists():
        return []
    return [json.loads(line) for line in path.read_text(encoding="utf-8").splitlines() if line.strip()]


def write_jsonl(path: Path, rows: list[dict[str, Any]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8") as handle:
        for row in rows:
            handle.write(json.dumps(row, ensure_ascii=False, sort_keys=True) + "\n")


def append_jsonl(path: Path, row: dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("a", encoding="utf-8") as handle:
        handle.write(json.dumps(row, ensure_ascii=False, sort_keys=True) + "\n")


def write_json(path: Path, payload: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, ensure_ascii=False, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def load_live_claims(page_id: int = PAGE_ID) -> list[dict[str, Any]]:
    with SessionLocal() as db:
        rows = db.execute(
            text(
                """
                SELECT id, page_id, section, order_idx, text
                FROM claims
                WHERE page_id = :page_id
                ORDER BY order_idx NULLS LAST, id
                """
            ),
            {"page_id": page_id},
        ).mappings().all()
    return [dict(row) for row in rows]


def load_candidates(page_id: int = PAGE_ID) -> list[dict[str, Any]]:
    with SessionLocal() as db:
        rows = db.execute(
            text(
                """
                SELECT *
                FROM arxiv_wiki_evidence_candidates
                WHERE page_id = :page_id
                ORDER BY run_id, id
                """
            ),
            {"page_id": page_id},
        ).mappings().all()
    return [dict(row) for row in rows]


def element_id_for(claim_id: int, element_index: int) -> str:
    return f"claim-{claim_id}-e{element_index:02d}"


def normalize_element(row: dict[str, Any], *, source_artifact: Path, page_claim: dict[str, Any] | None = None) -> dict[str, Any]:
    claim_id = int(row["claim_id"])
    element_index = int(row.get("element_index") or 0)
    if element_index <= 0:
        element_index = 1
    text_value = str(row.get("text") or row.get("element_text") or "").strip()
    return {
        **row,
        "claim_id": claim_id,
        "element_index": element_index,
        "element_id": row.get("element_id") or element_id_for(claim_id, element_index),
        "element_type": row.get("element_type") or "relationship",
        "required": bool(row.get("required", True)),
        "text": text_value,
        "parent_claim_text": row.get("parent_claim_text") or (page_claim or {}).get("text"),
        "section": row.get("section") or (page_claim or {}).get("section"),
        "order_idx": row.get("order_idx") or (page_claim or {}).get("order_idx"),
        "source_artifact": str(source_artifact),
        "atomization_source": "existing_artifact",
    }


def deterministic_fallback_elements(claim: dict[str, Any], reason: str) -> list[dict[str, Any]]:
    hints = atomize.deterministic_preparse({"id": claim["id"], "text": claim["text"], "section": claim.get("section")})
    raw_items: list[tuple[str, str, Any | None]] = []
    subject = (hints.get("subject") or [{}])[0].get("text") or claim["text"]
    raw_items.append(("subject", subject, None))
    for kind in ("mechanism", "quantity_or_threshold", "redshift_or_environment"):
        for item in hints.get(kind) or []:
            raw_items.append((kind, item.get("text") or item.get("source_span") or "", item.get("normalized")))
    if len(raw_items) == 1:
        raw_items.append(("relationship", claim["text"], None))

    seen: set[tuple[str, str]] = set()
    elements: list[dict[str, Any]] = []
    for kind, value, normalized in raw_items:
        text_value = " ".join(str(value or "").split()).strip(" .,;")
        if not text_value:
            continue
        key = (kind, text_value.lower())
        if key in seen:
            continue
        seen.add(key)
        element_index = len(elements) + 1
        row = {
            "claim_id": int(claim["id"]),
            "element_index": element_index,
            "element_id": element_id_for(int(claim["id"]), element_index),
            "element_type": kind,
            "required": True,
            "text": text_value[:500],
            "parent_claim_text": claim["text"],
            "source_span": text_value[:500],
            "normalized_subject": normalized if kind == "subject" else None,
            "normalized_mechanism": normalized if kind == "mechanism" else None,
            "quantity_or_range": normalized if kind == "quantity_or_threshold" else None,
            "redshift_or_environment": normalized if kind == "redshift_or_environment" else None,
            "citation_hint": None,
            "atomizer_model": atomize.ASTROSAGE_MODEL,
            "atomizer_prompt_version": atomize.PROMPT_VERSION,
            "atomizer_confidence": 0.45,
            "notes": f"deterministic fallback after {reason}",
            "section": claim.get("section"),
            "order_idx": claim.get("order_idx"),
            "atomizer_attempts": 0,
            "atomizer_duration_seconds": 0.0,
            "atomization_source": "deterministic_fallback",
            "source_artifact": "generated_by_page57_selection_atomization_recovery",
        }
        elements.append(row)
    return elements


def build_atomization_manifest(
    out_dir: Path,
    *,
    atomize_missing_with_model: bool,
    timeout: int,
    retries: int,
) -> dict[str, Any]:
    manifest_dir = out_dir / "atomization_manifest"
    live_claims = load_live_claims()
    live_by_id = {int(row["id"]): row for row in live_claims}
    by_claim: dict[int, list[dict[str, Any]]] = {}
    source_counts: dict[str, int] = {}

    for path in DEFAULT_EXISTING_ELEMENT_PATHS:
        rows = read_jsonl(path)
        source_counts[str(path)] = len(rows)
        grouped: dict[int, list[dict[str, Any]]] = collections.defaultdict(list)
        for row in rows:
            claim_id = int(row["claim_id"])
            if claim_id not in live_by_id:
                continue
            grouped[claim_id].append(normalize_element(row, source_artifact=path, page_claim=live_by_id[claim_id]))
        for claim_id, claim_elements in grouped.items():
            claim_elements.sort(key=lambda item: int(item.get("element_index") or 0))
            for index, item in enumerate(claim_elements, 1):
                item["element_index"] = index
                item["element_id"] = item.get("element_id") or element_id_for(claim_id, index)
            by_claim[claim_id] = claim_elements

    old_merged_claims = set(by_claim)
    candidate_claim_ids = {int(row["claim_id"]) for row in load_candidates()}
    absent_claim_ids = sorted(set(live_by_id) - old_merged_claims)
    absent_candidate_claim_ids = sorted(candidate_claim_ids - old_merged_claims)
    raw_failures: list[dict[str, Any]] = []
    generated_elements: list[dict[str, Any]] = []

    for index, claim_id in enumerate(absent_claim_ids, 1):
        claim = live_by_id[claim_id]
        claim_payload = {
            "id": claim["id"],
            "text": claim["text"],
            "section": claim.get("section"),
            "order_idx": claim.get("order_idx"),
        }
        elements: list[dict[str, Any]] = []
        failure_mode: str | None = None
        if atomize_missing_with_model:
            hints = atomize.deterministic_preparse(claim_payload)
            parsed, atomizer_meta = atomize.ollama_atomize(
                atomize.atomizer_prompt(claim_payload, hints),
                timeout=timeout,
                retries=retries,
            )
            parseable, normalized, failure_mode = atomize.normalize_elements(claim_payload, parsed, atomizer_meta)
            if parseable:
                elements = [
                    {
                        **row,
                        "element_id": row.get("element_id") or element_id_for(int(claim_id), int(row["element_index"])),
                        "atomization_source": "model_generated",
                        "source_artifact": "generated_by_page57_selection_atomization_recovery",
                    }
                    for row in normalized
                ]
            else:
                raw_failures.append(
                    {
                        "claim_id": claim_id,
                        "failure_mode": failure_mode,
                        "atomizer_errors": atomizer_meta.get("errors") or [],
                        "raw_response": atomizer_meta.get("raw_response"),
                    }
                )
        if not elements:
            elements = deterministic_fallback_elements(claim, failure_mode or "model_disabled")
        by_claim[claim_id] = elements
        generated_elements.extend(elements)
        if index % 25 == 0 or index == len(absent_claim_ids):
            print(json.dumps({"atomized_absent": index, "total_absent": len(absent_claim_ids)}, sort_keys=True), flush=True)

    merged_elements: list[dict[str, Any]] = []
    status_rows: list[dict[str, Any]] = []
    permanent_failures = 0
    for claim in live_claims:
        claim_id = int(claim["id"])
        elements = by_claim.get(claim_id, [])
        if elements:
            status = "atomized"
            source = elements[0].get("atomization_source")
        else:
            status = "fail_closed_no_elements"
            source = None
            permanent_failures += 1
        for index, element in enumerate(elements, 1):
            merged_elements.append(
                {
                    **element,
                    "element_index": index,
                    "element_id": element.get("element_id") or element_id_for(claim_id, index),
                }
            )
        status_rows.append(
            {
                "claim_id": claim_id,
                "page_id": PAGE_ID,
                "section": claim.get("section"),
                "order_idx": claim.get("order_idx"),
                "status": status,
                "element_count": len(elements),
                "atomization_source": source,
                "has_candidate_rows": claim_id in candidate_claim_ids,
            }
        )

    write_jsonl(manifest_dir / "elements_merged.jsonl", merged_elements)
    write_jsonl(manifest_dir / "claim_atomization_status.jsonl", status_rows)
    write_json(manifest_dir / "raw_failure_artifacts.json", raw_failures)
    summary = {
        "page_id": PAGE_ID,
        "live_claims": len(live_claims),
        "old_merged_claims": len(old_merged_claims),
        "absent_live_claims_before_expansion": len(absent_claim_ids),
        "absent_candidate_claims_before_expansion": len(absent_candidate_claim_ids),
        "atomized_claims": sum(1 for row in status_rows if row["status"] == "atomized"),
        "permanent_atomization_failures": permanent_failures,
        "element_count": len(merged_elements),
        "generated_element_count": len(generated_elements),
        "raw_failure_artifact_count": len(raw_failures),
        "existing_source_counts": source_counts,
        "outputs": {
            "elements_merged": str(manifest_dir / "elements_merged.jsonl"),
            "claim_atomization_status": str(manifest_dir / "claim_atomization_status.jsonl"),
            "raw_failure_artifacts": str(manifest_dir / "raw_failure_artifacts.json"),
        },
    }
    write_json(manifest_dir / "summary.json", summary)
    return summary


def candidate_pairs(elements_path: Path, out_dir: Path) -> tuple[list[dict[str, Any]], list[dict[str, Any]]]:
    elements = read_jsonl(elements_path)
    by_claim: dict[int, list[dict[str, Any]]] = collections.defaultdict(list)
    for row in elements:
        by_claim[int(row["claim_id"])].append(row)
    candidates = load_candidates()
    pairs: list[dict[str, Any]] = []
    missing: list[dict[str, Any]] = []
    for candidate in candidates:
        claim_id = int(candidate["claim_id"])
        claim_elements = by_claim.get(claim_id, [])
        if not claim_elements:
            missing.append(
                {
                    "candidate_id": candidate["id"],
                    "run_id": candidate["run_id"],
                    "claim_id": claim_id,
                    "arxiv_id": candidate["arxiv_id"],
                    "reason": "claim_not_present_in_atomization_manifest",
                }
            )
            continue
        for element in claim_elements:
            candidate_key = sha_text(
                {
                    "candidate_id": candidate["id"],
                    "run_id": candidate["run_id"],
                    "claim_id": claim_id,
                    "element_id": element["element_id"],
                    "arxiv_id": candidate["arxiv_id"],
                }
            )
            pairs.append(
                {
                    "candidate_db_id": candidate["id"],
                    "candidate_key": candidate_key,
                    "retrieval_filter_run_id": candidate["run_id"],
                    "claim_id": claim_id,
                    "element_id": element["element_id"],
                    "element_index": element["element_index"],
                    "element_type": element.get("element_type"),
                    "element_text": element.get("text"),
                    "required": bool(element.get("required")),
                    "normalized_subject": element.get("normalized_subject"),
                    "normalized_mechanism": element.get("normalized_mechanism"),
                    "quantity_or_range": element.get("quantity_or_range"),
                    "redshift_or_environment": element.get("redshift_or_environment"),
                    "section": element.get("section") or candidate.get("claim_section_snapshot"),
                    "source_element_artifact": element.get("source_artifact"),
                    "arxiv_id": candidate["arxiv_id"],
                    "claim_text_snapshot": candidate["claim_text_snapshot"],
                    "paper_title_snapshot": candidate["paper_title_snapshot"],
                    "paper_abstract_snapshot": candidate["paper_abstract_snapshot"],
                    "paper_year": candidate.get("paper_year"),
                    "candidate_source": candidate.get("candidate_source"),
                    "candidate_status": candidate.get("status"),
                    "matched_terms": candidate.get("matched_terms"),
                    "claim_key_overlap": candidate.get("claim_key_overlap"),
                    "duplicate_evidence_id": candidate.get("duplicate_evidence_id"),
                    "hydration_db_reads_used": False,
                    "hydration_policy": "artifact_only_fail_closed",
                }
            )
    write_jsonl(out_dir / "candidate_pairs_all.jsonl", pairs)
    write_jsonl(out_dir / "missing_atomization_candidates.jsonl", missing)
    return pairs, missing


def row_score(row: dict[str, Any]) -> float:
    anchors = row.get("deterministic_anchors") or {}
    terms = len(anchors.get("term_overlap") or [])
    numbers = len(anchors.get("number_overlap") or [])
    token_count = max(1, int(anchors.get("element_token_count") or 1))
    try:
        claim_key_overlap = float(row.get("claim_key_overlap") or 0.0)
    except (TypeError, ValueError):
        claim_key_overlap = 0.0
    matched_count = len(row.get("matched_terms") or [])
    return round(
        (terms / token_count)
        + 0.15 * min(1.0, terms / 4)
        + 0.10 * min(1.0, numbers)
        + 0.20 * max(0.0, min(1.0, claim_key_overlap))
        + 0.02 * min(10, matched_count),
        6,
    )


def split_selection_queue(
    pairs: list[dict[str, Any]],
    *,
    semantic_threshold: float,
    ollama_host: str,
    compute_semantic: bool,
    ordering: str,
    claim_seed_count: int,
) -> tuple[list[dict[str, Any]], list[dict[str, Any]]]:
    selected: list[dict[str, Any]] = []
    excluded: list[dict[str, Any]] = []
    embedding_cache: dict[str, list[float]] = {}
    for index, pair in enumerate(pairs, 1):
        row = dict(pair)
        anchors = deterministic_anchors(row)
        row["deterministic_anchors"] = anchors
        row["selection_rank_score"] = row_score(row)
        row["selection_status"] = None
        if str(row.get("candidate_status") or "").lower() == "off_domain" or str(row.get("source_label") or "").lower() == "off_domain":
            row["selection_status"] = "excluded_off_domain"
            excluded.append(row)
            continue
        if str(row.get("retrieval_filter_decision") or "").lower() == "boundary_review_keep":
            row["selection_status"] = "audit_only_boundary_review_keep"
            excluded.append(row)
            continue
        if not anchors.get("has_anchor_overlap"):
            row["selection_status"] = "excluded_anchor_overlap_missing"
            excluded.append(row)
            continue
        if compute_semantic:
            row.update(semantic_support_features(row, semantic_threshold, ollama_host, embedding_cache))
            if row.get("coverage_candidate") is False:
                row["selection_status"] = "excluded_semantic_unsupported"
                excluded.append(row)
                continue
        else:
            row.update(
                {
                    "coverage_candidate": None,
                    "semantic_similarity": None,
                    "semantic_similarity_threshold": semantic_threshold,
                    "semantic_support_status": "not_computed",
                    "semantic_support_error": None,
                }
            )
        entailment_decision = str(row.get("entailment_gate_decision") or "").lower()
        if entailment_decision == "no":
            row["selection_status"] = "excluded_entailment_rejected"
            excluded.append(row)
            continue
        if entailment_decision == "error":
            row["selection_status"] = "excluded_entailment_error"
            excluded.append(row)
            continue
        row["selection_status"] = "selected_for_atom_coverage"
        selected.append(row)
        if index % 1000 == 0:
            print(json.dumps({"split_rows": index, "total_pairs": len(pairs)}, sort_keys=True), flush=True)

    selected = order_selected_rows(selected, ordering, claim_seed_count=claim_seed_count)
    return selected, excluded


def order_selected_rows(rows: list[dict[str, Any]], ordering: str, claim_seed_count: int = 0) -> list[dict[str, Any]]:
    def row_sort_key(item: dict[str, Any]) -> tuple[float, float, int, str]:
        try:
            score = float(item.get("selection_rank_score") or 0.0)
        except (TypeError, ValueError):
            score = 0.0
        try:
            semantic = float(item.get("semantic_similarity") or 0.0)
        except (TypeError, ValueError):
            semantic = 0.0
        return (-score, -semantic, int(item.get("candidate_db_id") or 0), str(item.get("element_id") or ""))

    score_ordered = sorted(rows, key=row_sort_key)
    if ordering == "score":
        return score_ordered
    if ordering not in {"claim_round_robin", "claim_seed_then_score"}:
        raise ValueError(f"unsupported selection ordering: {ordering}")

    by_claim: dict[int, list[dict[str, Any]]] = collections.defaultdict(list)
    for row in score_ordered:
        by_claim[int(row["claim_id"])].append(row)
    for claim_rows in by_claim.values():
        claim_rows.sort(key=row_sort_key)
    claim_order = sorted(
        by_claim,
        key=lambda claim_id: (
            row_sort_key(by_claim[claim_id][0]),
            int(claim_id),
        ),
    )
    if ordering == "claim_seed_then_score":
        seeded: list[dict[str, Any]] = []
        used_keys: set[tuple[Any, Any, Any]] = set()
        for claim_id in claim_order[: max(0, claim_seed_count)]:
            row = {**by_claim[claim_id][0], "selection_order_depth": 1, "selection_seeded_claim": True}
            seeded.append(row)
            used_keys.add((row.get("candidate_key"), row.get("element_id"), row.get("arxiv_id")))
        for row in score_ordered:
            key = (row.get("candidate_key"), row.get("element_id"), row.get("arxiv_id"))
            if key in used_keys:
                continue
            seeded.append({**row, "selection_seeded_claim": False})
        return seeded

    ordered: list[dict[str, Any]] = []
    depth = 0
    while True:
        added = False
        for claim_id in claim_order:
            claim_rows = by_claim[claim_id]
            if depth >= len(claim_rows):
                continue
            ordered.append({**claim_rows[depth], "selection_order_depth": depth + 1})
            added = True
        if not added:
            break
        depth += 1
    return ordered


def db_coverage_by_key(keys: set[str]) -> dict[str, dict[str, Any]]:
    if not keys:
        return {}
    with SessionLocal() as db:
        rows = db.execute(
            text(
                """
                SELECT *
                FROM arxiv_wiki_candidate_atom_coverage
                WHERE coverage_key = ANY(:keys)
                """
            ),
            {"keys": list(keys)},
        ).mappings().all()
    return {str(row["coverage_key"]): dict(row) for row in rows}


def coverage_from_db(pair: dict[str, Any], cached: dict[str, Any], coverage_run_id: str) -> dict[str, Any]:
    atoms = cached.get("candidate_atoms") or []
    status = cached.get("candidate_atom_coverage_status")
    if status == "ready":
        coverage_status = "coverage_ready"
    elif status in {"needs_human", "error_retryable"}:
        coverage_status = "coverage_blocked_retryable"
    else:
        coverage_status = "coverage_blocked_terminal"
    return {
        **pair,
        **coverage_row(pair, coverage_run_id, ATOM_MODEL, 1, use_model=False),
        "coverage_run_id": coverage_run_id,
        "coverage_key": cached["coverage_key"],
        "candidate_atom_coverage_status": status,
        "candidate_atoms": atoms,
        "deterministic_anchors": cached.get("deterministic_anchors") or pair.get("deterministic_anchors"),
        "source_hashes": cached.get("source_hashes") or {},
        "backfill_model": cached.get("backfill_model") or ATOM_MODEL,
        "backfill_prompt_version": cached.get("backfill_prompt_version") or COVERAGE_PROMPT_VERSION,
        "rationale": cached.get("rationale"),
        "failure_mode": cached.get("failure_mode"),
        "raw_response": cached.get("raw_response"),
        "latency_seconds": 0.0,
        "coverage_status": coverage_status,
        "coverage_missing_stages": [] if coverage_status == "coverage_ready" else ["atom_decomposition"],
        "coverage_from_cache": True,
        "hydration_db_reads_used": False,
        "hydration_policy": "artifact_only_fail_closed",
    }


def valid_ready(row: dict[str, Any]) -> bool:
    atoms = row.get("candidate_atoms") or []
    valid_atoms = [
        atom
        for atom in atoms
        if atom.get("support_relation") in {"direct", "partial"}
        and (atom.get("evidence_anchor_terms") or atom.get("evidence_anchor_numbers") or atom.get("quoted_span_or_null"))
    ]
    source_hashes = row.get("source_hashes") or {}
    return row.get("candidate_atom_coverage_status") == "ready" and bool(valid_atoms) and bool(row.get("coverage_key")) and all(source_hashes.values())


def insert_or_update_coverage(row: dict[str, Any]) -> int:
    raw_response = row.get("raw_response")
    if isinstance(raw_response, str):
        raw_response = {"text": raw_response}
    with SessionLocal() as db:
        result = db.execute(
            text(
                """
                INSERT INTO arxiv_wiki_candidate_atom_coverage
                    (coverage_key, retrieval_filter_run_id, claim_id, element_id, arxiv_id,
                     candidate_atom_coverage_status, candidate_atoms, deterministic_anchors,
                     source_hashes, backfill_model, backfill_prompt_version, rationale,
                     failure_mode, raw_response, updated_at)
                VALUES
                    (:coverage_key, :retrieval_filter_run_id, :claim_id, :element_id, :arxiv_id,
                     :candidate_atom_coverage_status, CAST(:candidate_atoms AS jsonb),
                     CAST(:deterministic_anchors AS jsonb), CAST(:source_hashes AS jsonb),
                     :backfill_model, :backfill_prompt_version, :rationale, :failure_mode,
                     CAST(:raw_response AS jsonb), NOW())
                ON CONFLICT (coverage_key) DO UPDATE SET
                    candidate_atom_coverage_status = EXCLUDED.candidate_atom_coverage_status,
                    candidate_atoms = EXCLUDED.candidate_atoms,
                    deterministic_anchors = EXCLUDED.deterministic_anchors,
                    source_hashes = EXCLUDED.source_hashes,
                    backfill_model = EXCLUDED.backfill_model,
                    backfill_prompt_version = EXCLUDED.backfill_prompt_version,
                    rationale = EXCLUDED.rationale,
                    failure_mode = EXCLUDED.failure_mode,
                    raw_response = EXCLUDED.raw_response,
                    updated_at = NOW()
                """
            ),
            {
                "coverage_key": row["coverage_key"],
                "retrieval_filter_run_id": int(row["retrieval_filter_run_id"]),
                "claim_id": int(row["claim_id"]),
                "element_id": row["element_id"],
                "arxiv_id": row["arxiv_id"],
                "candidate_atom_coverage_status": row["candidate_atom_coverage_status"],
                "candidate_atoms": json.dumps(row.get("candidate_atoms") or [], ensure_ascii=False),
                "deterministic_anchors": json.dumps(row.get("deterministic_anchors") or {}, ensure_ascii=False),
                "source_hashes": json.dumps(row.get("source_hashes") or {}, ensure_ascii=False),
                "backfill_model": row.get("backfill_model") or ATOM_MODEL,
                "backfill_prompt_version": row.get("backfill_prompt_version") or COVERAGE_PROMPT_VERSION,
                "rationale": row.get("rationale"),
                "failure_mode": row.get("failure_mode"),
                "raw_response": json.dumps(raw_response, ensure_ascii=False) if raw_response is not None else None,
            },
        )
        db.commit()
        return int(result.rowcount or 0)


def run_coverage(
    selected: list[dict[str, Any]],
    out_dir: Path,
    *,
    limit: int,
    timeout: int,
    no_model: bool,
    reuse_db_coverage: bool,
    write_coverage_db: bool,
) -> tuple[list[dict[str, Any]], int]:
    rows_to_run = selected[:limit] if limit else selected
    keys = {coverage_key(row, COVERAGE_PROMPT_VERSION, ATOM_MODEL) for row in rows_to_run}
    cached_by_key = db_coverage_by_key(keys) if reuse_db_coverage else {}
    coverage_rows: list[dict[str, Any]] = []
    db_writes = 0
    started = time.time()
    for index, row in enumerate(rows_to_run, 1):
        key = coverage_key(row, COVERAGE_PROMPT_VERSION, ATOM_MODEL)
        if key in cached_by_key:
            coverage = coverage_from_db(row, cached_by_key[key], out_dir.name)
        else:
            coverage = coverage_row(row, out_dir.name, ATOM_MODEL, timeout, not no_model)
            coverage["coverage_from_cache"] = False
            if write_coverage_db:
                db_writes += insert_or_update_coverage(coverage)
        coverage_rows.append(coverage)
        append_jsonl(out_dir / "coverage_rows.jsonl", coverage)
        if index % 25 == 0 or index == len(rows_to_run):
            counts = collections.Counter(item.get("candidate_atom_coverage_status") for item in coverage_rows)
            print(
                json.dumps(
                    {
                        "coverage_rows": index,
                        "target": len(rows_to_run),
                        "status_counts": dict(counts),
                        "elapsed_seconds": round(time.time() - started, 1),
                    },
                    sort_keys=True,
                ),
                flush=True,
            )
    return coverage_rows, db_writes


def summarize_coverage(coverage_rows: list[dict[str, Any]], excluded_rows: list[dict[str, Any]], selected_rows: list[dict[str, Any]], db_writes: int) -> dict[str, Any]:
    ready_rows = [row for row in coverage_rows if valid_ready(row)]
    seen: set[tuple[Any, ...]] = set()
    deduped_ready: list[dict[str, Any]] = []
    for row in ready_rows:
        key = (row.get("claim_id"), row.get("element_id"), row.get("arxiv_id"))
        if key in seen:
            continue
        seen.add(key)
        deduped_ready.append(row)
    status_counts = collections.Counter(row.get("candidate_atom_coverage_status") for row in coverage_rows)
    excluded_counts = collections.Counter(row.get("selection_status") for row in excluded_rows)
    model_run_rows = [row for row in coverage_rows if not row.get("coverage_from_cache")]
    anchor_missing_model_rows = [
        row
        for row in model_run_rows
        if ((row.get("coverage_artifact_refs") or {}).get("atom_decomposition") or {}).get("reason") == "anchor_overlap_missing"
    ]
    return {
        "raw_rows": len(coverage_rows),
        "ready_rows": len(ready_rows),
        "ready_rate": round(len(ready_rows) / max(1, len(coverage_rows)), 6),
        "unique_ready_tuples": len(deduped_ready),
        "distinct_ready_claims": len({row.get("claim_id") for row in ready_rows}),
        "retryable_rows": status_counts.get("error_retryable", 0),
        "retryable_error_rate": round(status_counts.get("error_retryable", 0) / max(1, len(coverage_rows)), 6),
        "status_counts": dict(status_counts),
        "selected_rows": len(selected_rows),
        "excluded_counts": dict(excluded_counts),
        "excluded_anchor_overlap_missing": excluded_counts.get("excluded_anchor_overlap_missing", 0),
        "excluded_semantic_unsupported": excluded_counts.get("excluded_semantic_unsupported", 0),
        "excluded_entailment_rejected": excluded_counts.get("excluded_entailment_rejected", 0),
        "audit_only_boundary_review_keep": excluded_counts.get("audit_only_boundary_review_keep", 0),
        "excluded_off_domain": excluded_counts.get("excluded_off_domain", 0),
        "model_run_rows": len(model_run_rows),
        "anchor_overlap_missing_model_rows": len(anchor_missing_model_rows),
        "anchor_overlap_missing_model_rate": round(len(anchor_missing_model_rows) / max(1, len(model_run_rows)), 6),
        "db_writes_used": db_writes > 0,
        "db_write_count": db_writes,
        "hydration_db_reads_used": False,
        "db_reads_used_for_validator_hydration": False,
        "evidence_rows_written": 0,
        "promoter_run": False,
    }


def write_report(out_dir: Path, summary: dict[str, Any], atom_summary: dict[str, Any], commands: list[str]) -> None:
    lines = [
        "# Page57 Selection/Atomization Recovery",
        "",
        f"- Artifact root: `{out_dir}`",
        f"- Live claims: `{atom_summary['live_claims']}`",
        f"- Atomized claims: `{atom_summary['atomized_claims']}`",
        f"- Missing atomization candidate rows: `{summary['missing_atomization_candidate_rows']}`",
        f"- Coverage rows: `{summary['coverage']['raw_rows']}`",
        f"- Ready rows: `{summary['coverage']['ready_rows']}`",
        f"- Ready rate: `{summary['coverage']['ready_rate']}`",
        f"- Unique ready tuples: `{summary['coverage']['unique_ready_tuples']}`",
        f"- Distinct ready claims: `{summary['coverage']['distinct_ready_claims']}`",
        f"- Retryable rows: `{summary['coverage']['retryable_rows']}`",
        "",
        "## Safety",
        "",
        "- Mode 1 only.",
        "- Evidence rows written: `0`.",
        "- Promoter run: `false`.",
        "- Validator hydration DB reads: `false`.",
    ]
    (out_dir / "REPORT.md").write_text("\n".join(lines) + "\n", encoding="utf-8")
    (out_dir / "RUN_COMMANDS.md").write_text("\n".join(f"- `{command}`" for command in commands) + "\n", encoding="utf-8")


def run(args: argparse.Namespace) -> dict[str, Any]:
    out_dir = args.out_dir or ARTIFACT_ROOT / f"page57_selection_atomization_recovery_{utc_stamp()}"
    out_dir.mkdir(parents=True, exist_ok=True)
    commands = [" ".join(sys.argv)]
    atom_summary = build_atomization_manifest(
        out_dir,
        atomize_missing_with_model=not args.no_atomizer_model,
        timeout=args.atomizer_timeout,
        retries=args.atomizer_retries,
    )
    pairs, missing_atomization = candidate_pairs(out_dir / "atomization_manifest" / "elements_merged.jsonl", out_dir)
    selected, excluded = split_selection_queue(
        pairs,
        semantic_threshold=args.semantic_threshold,
        ollama_host=args.ollama_host,
        compute_semantic=not args.no_semantic,
        ordering=args.selection_ordering,
        claim_seed_count=args.claim_seed_count,
    )
    write_jsonl(out_dir / "coverage_selection_queue.jsonl", selected)
    write_jsonl(out_dir / "coverage_excluded_rows.jsonl", excluded)
    if (out_dir / "coverage_rows.jsonl").exists():
        (out_dir / "coverage_rows.jsonl").unlink()
    coverage_rows, db_writes = run_coverage(
        selected,
        out_dir,
        limit=args.coverage_limit,
        timeout=args.coverage_timeout,
        no_model=args.no_coverage_model,
        reuse_db_coverage=not args.no_reuse_db_coverage,
        write_coverage_db=args.write_coverage_db,
    )
    ready_rows = [row for row in coverage_rows if valid_ready(row)]
    seen: set[tuple[Any, ...]] = set()
    deduped_ready: list[dict[str, Any]] = []
    for row in ready_rows:
        key = (row.get("claim_id"), row.get("element_id"), row.get("arxiv_id"))
        if key in seen:
            continue
        seen.add(key)
        deduped_ready.append(row)
    write_jsonl(out_dir / "validator_ready_rows.jsonl", ready_rows)
    write_jsonl(out_dir / "validator_ready_rows_deduped.jsonl", deduped_ready)
    coverage_summary = summarize_coverage(coverage_rows, excluded, selected, db_writes)
    summary = {
        "artifact_root": str(out_dir),
        "mode": "mode1_selection_atomization_recovery",
        "created_at": dt.datetime.now(dt.UTC).isoformat(),
        "atomization": atom_summary,
        "candidate_pairs_total": len(pairs),
        "missing_atomization_candidate_rows": len(missing_atomization),
        "selection": {
            "selected_for_atom_coverage": len(selected),
            "excluded_rows": len(excluded),
            "selection_status_counts": dict(collections.Counter(row.get("selection_status") for row in selected + excluded)),
            "semantic_threshold": args.semantic_threshold,
            "semantic_computed": not args.no_semantic,
            "selection_ordering": args.selection_ordering,
            "claim_seed_count": args.claim_seed_count,
            "selection_limit": args.coverage_limit,
        },
        "coverage": coverage_summary,
        "mode1_safety": {
            "evidence_rows_written": 0,
            "promoter_run": False,
            "db_reads_used_for_validator_hydration": False,
            "hydration_db_reads_used": False,
            "db_writes_used": db_writes > 0,
            "db_write_count": db_writes,
        },
        "outputs": {
            "atomization_manifest_summary": str(out_dir / "atomization_manifest" / "summary.json"),
            "coverage_selection_queue": str(out_dir / "coverage_selection_queue.jsonl"),
            "coverage_excluded_rows": str(out_dir / "coverage_excluded_rows.jsonl"),
            "coverage_rows": str(out_dir / "coverage_rows.jsonl"),
            "validator_ready_rows": str(out_dir / "validator_ready_rows.jsonl"),
            "validator_ready_rows_deduped": str(out_dir / "validator_ready_rows_deduped.jsonl"),
            "coverage_summary": str(out_dir / "coverage_summary.json"),
            "report": str(out_dir / "REPORT.md"),
            "run_commands": str(out_dir / "RUN_COMMANDS.md"),
        },
    }
    write_json(out_dir / "coverage_summary.json", summary)
    write_report(out_dir, summary, atom_summary, commands)
    print(json.dumps(summary, ensure_ascii=False, indent=2, sort_keys=True), flush=True)
    return summary


def main() -> None:
    parser = argparse.ArgumentParser(description="Page57 Mode-1 selection/atomization recovery")
    parser.add_argument("--out-dir", type=Path)
    parser.add_argument("--no-atomizer-model", action="store_true")
    parser.add_argument("--atomizer-timeout", type=int, default=360)
    parser.add_argument("--atomizer-retries", type=int, default=2)
    parser.add_argument("--semantic-threshold", type=float, default=0.50)
    parser.add_argument("--ollama-host", default="http://localhost:11434")
    parser.add_argument("--no-semantic", action="store_true")
    parser.add_argument("--coverage-limit", type=int, default=300)
    parser.add_argument("--coverage-timeout", type=int, default=180)
    parser.add_argument("--no-coverage-model", action="store_true")
    parser.add_argument("--no-reuse-db-coverage", action="store_true")
    parser.add_argument("--write-coverage-db", action="store_true")
    parser.add_argument("--selection-ordering", choices=["score", "claim_round_robin", "claim_seed_then_score"], default="claim_seed_then_score")
    parser.add_argument("--claim-seed-count", type=int, default=200)
    args = parser.parse_args()
    run(args)


if __name__ == "__main__":
    main()
