#!/usr/bin/env python3
"""Materialize validator coverage artifacts between retrieval-filter and validator.

This stage is artifact-only. It does not mutate historical retrieval-filter
runs, does not write database state, and does not call promoter code.
"""

from __future__ import annotations

import argparse
import datetime as dt
import hashlib
import json
from collections import Counter
from pathlib import Path
from typing import Any, Callable, Iterable, Mapping

from scripts.retrieval_filter_v2 import DEFAULT_COVERAGE_REQUIRED_STAGES, row_with_initial_coverage


StageRunner = Callable[[Mapping[str, Any], str, str], dict[str, Any]]
STAGE_READY = "ready"
STAGE_PENDING = "coverage_pending"
STAGE_RETRYABLE = "blocked_retryable"
STAGE_TERMINAL = "blocked_terminal"
ROW_READY = "coverage_ready"
ROW_PENDING = "coverage_pending"
ROW_RETRYABLE = "blocked_retryable"
ROW_TERMINAL = "blocked_terminal"
PROMPT_VERSION = "validator_coverage_v1_20260531"
MODEL_VERSION = "artifact_only_v1"


def read_jsonl(path: Path) -> list[dict[str, Any]]:
    rows: list[dict[str, Any]] = []
    with path.open(encoding="utf-8") as handle:
        for line in handle:
            if line.strip():
                rows.append(json.loads(line))
    return rows


def write_jsonl(path: Path, rows: Iterable[Mapping[str, Any]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8") as handle:
        for row in rows:
            handle.write(json.dumps(row, ensure_ascii=False, sort_keys=True) + "\n")


def write_json(path: Path, payload: Mapping[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, ensure_ascii=False, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def sha_text(value: Any) -> str:
    if value is None:
        value = ""
    if not isinstance(value, str):
        value = json.dumps(value, ensure_ascii=False, sort_keys=True)
    return hashlib.sha256(value.encode("utf-8")).hexdigest()


def stage_cache_key(row: Mapping[str, Any], stage: str, prompt_version: str, model_version: str) -> str:
    paper_text = " ".join(str(row.get(key) or "") for key in ("paper_title_snapshot", "paper_abstract_snapshot", "paper_title", "paper_abstract"))
    parts = [
        stage,
        row.get("claim_id"),
        row.get("element_id"),
        row.get("arxiv_id") or row.get("paper_id"),
        sha_text(row.get("element_text")),
        sha_text(paper_text),
        prompt_version,
        model_version,
    ]
    return hashlib.sha256("||".join(str(part or "") for part in parts).encode("utf-8")).hexdigest()


def required_input_missing(row: Mapping[str, Any]) -> list[str]:
    missing = [
        field
        for field in ("claim_text_snapshot", "element_text")
        if not str(row.get(field) or "").strip()
    ]
    if not str(row.get("paper_abstract_snapshot") or row.get("paper_abstract") or "").strip():
        missing.append("paper_abstract_snapshot")
    if not isinstance(row.get("required"), bool):
        missing.append("required")
    return missing


def default_stage_runner(row: Mapping[str, Any], stage: str, cache_key: str) -> dict[str, Any]:
    missing = required_input_missing(row)
    if missing:
        return {
            "stage": stage,
            "status": STAGE_TERMINAL,
            "cache_key": cache_key,
            "reason": f"malformed_input:{','.join(missing)}",
        }
    if stage == "precheck":
        return {"stage": stage, "status": STAGE_READY, "cache_key": cache_key, "reason": "deterministic_precheck_ready"}
    if stage == "atom_decomposition":
        atom_status = str(row.get("candidate_atom_coverage_status") or "").strip().lower()
        if atom_status == "ready" or row.get("candidate_atoms"):
            return {"stage": stage, "status": STAGE_READY, "cache_key": cache_key, "reason": "atom_artifact_ready"}
        if atom_status in {"error_retryable", "needs_human"}:
            return {"stage": stage, "status": STAGE_RETRYABLE, "cache_key": cache_key, "reason": atom_status}
        if atom_status in {"missing", "error_terminal"}:
            return {"stage": stage, "status": STAGE_TERMINAL, "cache_key": cache_key, "reason": atom_status}
        return {"stage": stage, "status": STAGE_PENDING, "cache_key": cache_key, "reason": "atom_artifact_missing"}
    if stage == "astrosage_verdict":
        verdict = str(row.get("astrosage_verdict_status") or row.get("entailment_gate_decision") or "").strip().lower()
        if verdict in {"ready", "yes", "supported"}:
            return {"stage": stage, "status": STAGE_READY, "cache_key": cache_key, "reason": "astrosage_artifact_ready"}
        if verdict in {"no", "abstain", "missing", "error_terminal"}:
            return {"stage": stage, "status": STAGE_TERMINAL, "cache_key": cache_key, "reason": verdict}
        return {"stage": stage, "status": STAGE_PENDING, "cache_key": cache_key, "reason": "astrosage_artifact_missing"}
    return {"stage": stage, "status": STAGE_TERMINAL, "cache_key": cache_key, "reason": "unknown_stage"}


def cache_index(rows: Iterable[Mapping[str, Any]]) -> dict[tuple[str, str], dict[str, Any]]:
    index: dict[tuple[str, str], dict[str, Any]] = {}
    for row in rows:
        refs = row.get("coverage_artifact_refs") or {}
        if not isinstance(refs, Mapping):
            continue
        for stage, ref in refs.items():
            if not isinstance(ref, Mapping):
                continue
            cache_key = ref.get("cache_key")
            if isinstance(cache_key, str) and ref.get("status") == STAGE_READY:
                index[(str(stage), cache_key)] = dict(ref)
    return index


def row_identity(row: Mapping[str, Any]) -> dict[str, Any]:
    return {
        "claim_id": row.get("claim_id"),
        "element_id": row.get("element_id"),
        "arxiv_id": row.get("arxiv_id") or row.get("paper_id"),
        "candidate_key": row.get("candidate_key"),
    }


def hydration_fields(row: Mapping[str, Any]) -> dict[str, Any]:
    title = row.get("paper_title_snapshot") or row.get("paper_title")
    abstract = row.get("paper_abstract_snapshot") or row.get("paper_abstract")
    return {
        "source_hashes": {
            "claim_text_hash": sha_text(row.get("claim_text_snapshot")),
            "element_text_hash": sha_text(row.get("element_text")),
            "paper_title_hash": sha_text(title),
            "paper_abstract_hash": sha_text(abstract),
        },
        "hydration_sources": {
            "claim_text": "artifact",
            "element_text": "artifact",
            "paper_title": "artifact",
            "paper_abstract": "artifact",
        },
        "hydration_db_reads_used": False,
        "hydration_policy": "artifact_only_fail_closed",
    }


def materialize_coverage_rows(
    rows: Iterable[Mapping[str, Any]],
    *,
    cached_rows: Iterable[Mapping[str, Any]] = (),
    required_stages: Iterable[str] = DEFAULT_COVERAGE_REQUIRED_STAGES,
    prompt_version: str = PROMPT_VERSION,
    model_version: str = MODEL_VERSION,
    stage_runner: StageRunner = default_stage_runner,
) -> list[dict[str, Any]]:
    cached = cache_index(cached_rows)
    out: list[dict[str, Any]] = []
    stages = [str(stage) for stage in required_stages]
    for source_row in rows:
        row = row_with_initial_coverage(source_row, stages)
        refs: dict[str, dict[str, Any]] = {}
        statuses: dict[str, str] = {}
        for stage in stages:
            key = stage_cache_key(row, stage, prompt_version, model_version)
            cached_ref = cached.get((stage, key))
            if cached_ref:
                result = {**cached_ref, "stage": stage, "status": STAGE_READY, "cache_key": key, "reused": True}
            else:
                result = stage_runner(row, stage, key)
                result.setdefault("stage", stage)
                result.setdefault("cache_key", key)
                result.setdefault("reused", False)
            status = str(result.get("status") or STAGE_RETRYABLE)
            statuses[stage] = status
            refs[stage] = {
                **row_identity(row),
                "stage": stage,
                "status": status,
                "cache_key": key,
                "prompt_version": prompt_version,
                "model_version": model_version,
                "reason": result.get("reason"),
                "reused": bool(result.get("reused")),
            }

        missing = [stage for stage in stages if statuses.get(stage) != STAGE_READY]
        if not missing:
            coverage_status = ROW_READY
        elif any(statuses.get(stage) == STAGE_RETRYABLE for stage in missing):
            coverage_status = ROW_RETRYABLE
        elif any(statuses.get(stage) == STAGE_TERMINAL for stage in missing):
            coverage_status = ROW_TERMINAL
        else:
            coverage_status = ROW_PENDING
        out.append(
            {
                **row,
                **hydration_fields(row),
                "coverage_status": coverage_status,
                "coverage_required_stages": stages,
                "coverage_missing_stages": missing,
                "coverage_stage_statuses": statuses,
                "coverage_artifact_refs": refs,
                "coverage_materialized_at": dt.datetime.now(dt.timezone.utc).isoformat(),
            }
        )
    return out


def run(args: argparse.Namespace) -> dict[str, Any]:
    rows = read_jsonl(args.input)
    cached_rows = read_jsonl(args.cache) if args.cache and args.cache.exists() else []
    coverage_rows = materialize_coverage_rows(rows, cached_rows=cached_rows)
    ready_rows = [row for row in coverage_rows if row.get("coverage_status") == ROW_READY]
    blocked_rows = [row for row in coverage_rows if row.get("coverage_status") != ROW_READY]
    args.out_dir.mkdir(parents=True, exist_ok=True)
    write_jsonl(args.out_dir / "coverage_rows.jsonl", coverage_rows)
    write_jsonl(args.out_dir / "coverage_ready_manifest.jsonl", ready_rows)
    write_jsonl(args.out_dir / "blocked_rows.jsonl", blocked_rows)
    summary = {
        "created_at": dt.datetime.now(dt.timezone.utc).isoformat(),
        "input": str(args.input),
        "row_count": len(coverage_rows),
        "ready_rows": len(ready_rows),
        "blocked_rows": len(blocked_rows),
        "coverage_status_counts": dict(Counter(str(row.get("coverage_status")) for row in coverage_rows)),
        "no_db_writes": True,
        "promoter_calls": False,
    }
    write_json(args.out_dir / "coverage_summary.json", summary)
    return summary


def main() -> None:
    parser = argparse.ArgumentParser(description="Materialize validator coverage artifacts.")
    parser.add_argument("--input", type=Path, required=True, help="Retrieval-filter rows JSONL or candidate artifact.")
    parser.add_argument("--out-dir", type=Path, required=True)
    parser.add_argument("--cache", type=Path, help="Prior coverage_rows.jsonl for idempotent reuse.")
    args = parser.parse_args()
    print(json.dumps(run(args), ensure_ascii=False, sort_keys=True))


if __name__ == "__main__":
    main()
