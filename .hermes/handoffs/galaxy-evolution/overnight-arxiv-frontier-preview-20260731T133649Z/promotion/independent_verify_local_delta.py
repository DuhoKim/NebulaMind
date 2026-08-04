#!/usr/bin/env python3
"""Independent, read-only verification for an already-applied frontier delta."""

from __future__ import annotations

import datetime as dt
import fcntl
import hashlib
import json
import os
import re
import subprocess
import sys
from collections import Counter
from pathlib import Path
from typing import Any

import numpy as np

RUN = Path("/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/overnight-arxiv-frontier-preview-20260731T133649Z")
ENGINE = Path("/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/corpus-ga-co-2009-2026-20260718")
REPO = Path("/Users/duhokim/NebulaMind/NebulaMind")
PROMOTION = RUN / "promotion"
REPORT = PROMOTION / "INDEPENDENT_VERIFICATION.json"
APPROVED_MANIFEST_SHA256 = "aaa9d4fe45da6a8f12b68325c1dd20f1c141f6f24a9929b99e50ce471dc6b0ba"
TARGETS = ("new_emb.f32", "new_papers.jsonl", "new_labels.json")
DIM = 2560
PYTHON = REPO / "backend/.venv/bin/python"


class VerificationFailure(RuntimeError):
    pass


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def fingerprint(path: Path) -> dict[str, Any]:
    return {"bytes": path.stat().st_size, "sha256": sha256(path)}


def load_json(path: Path) -> Any:
    return json.loads(path.read_text(encoding="utf-8"))


def load_jsonl(path: Path) -> list[dict[str, Any]]:
    rows = []
    with path.open("r", encoding="utf-8") as handle:
        for line_number, line in enumerate(handle, 1):
            if line.strip():
                row = json.loads(line)
                if not isinstance(row, dict):
                    raise VerificationFailure(f"non-object JSONL row in {path}:{line_number}")
                rows.append(row)
    return rows


def atomic_json(path: Path, payload: dict[str, Any]) -> None:
    temp = path.with_name(f".{path.name}.{os.getpid()}.tmp")
    with temp.open("w", encoding="utf-8") as handle:
        json.dump(payload, handle, indent=2, sort_keys=True)
        handle.write("\n")
        handle.flush()
        os.fsync(handle.fileno())
    os.replace(temp, path)


def check(results: list[dict[str, Any]], name: str, passed: bool, details: Any) -> None:
    row = {"name": name, "pass": bool(passed), "details": details}
    results.append(row)
    if not passed:
        raise VerificationFailure(f"{name}: {details}")


def canonical_arxiv_id(raw: Any) -> str | None:
    value = str(raw or "").strip()
    if not value:
        return None
    value = re.sub(r"^https?://(?:export\.)?arxiv\.org/(?:abs|pdf)/", "", value, flags=re.I)
    value = re.sub(r"^oai:arxiv\.org:", "", value, flags=re.I)
    value = re.sub(r"^arxiv:", "", value, flags=re.I)
    value = value.removesuffix(".pdf")
    match = re.fullmatch(r"((?:\d{4}\.\d{4,5})|(?:[A-Za-z0-9.-]+/[0-9]{7}))(?:v\d+)?", value)
    return match.group(1) if match else None


def scan_base(path: Path) -> dict[str, Any]:
    digest = hashlib.sha256()
    identifiers: set[str] = set()
    rows = 0
    byte_count = 0
    with path.open("rb") as handle:
        for line_number, raw_line in enumerate(handle, 1):
            digest.update(raw_line)
            byte_count += len(raw_line)
            if not raw_line.strip():
                continue
            row = json.loads(raw_line)
            rows += 1
            values = row.get("identifier") or []
            if isinstance(values, str):
                values = [values]
            for value in values:
                normalized = canonical_arxiv_id(value)
                if normalized:
                    identifiers.add(normalized)
            normalized = canonical_arxiv_id(row.get("arxiv_id"))
            if normalized:
                identifiers.add(normalized)
    return {
        "rows": rows,
        "bytes": byte_count,
        "sha256": digest.hexdigest(),
        "arxiv_ids": identifiers,
    }


def tractable_ranks(document: dict[str, Any]) -> dict[int, int]:
    rows = sorted(
        (row for row in document.get("clusters", []) if int(row.get("tractable", 0)) == 1),
        key=lambda row: (-float(row.get("score_v1", 0.0)), int(row["cluster"])),
    )
    return {int(row["cluster"]): index + 1 for index, row in enumerate(rows)}


def main() -> int:
    checks: list[dict[str, Any]] = []
    report: dict[str, Any] = {
        "schema_version": 1,
        "run_id": RUN.name,
        "status": "INDEPENDENT_VERIFICATION_FAILED",
        "verified_at_utc": dt.datetime.now(dt.timezone.utc).isoformat(),
        "verifier": str(Path(__file__).resolve()),
        "verifier_sha256": sha256(Path(__file__).resolve()),
        "checks": checks,
        "safety_ledger": {
            "verification_phase_canonical_writes": 0,
            "db_sql_writes": 0,
            "frontend_live_public_cockpit_writes": 0,
            "wiki_evidence_trust_writes": 0,
            "scheduler_cron_launchagent_writes": 0,
            "deploy_restart_actions": 0,
            "git_writes": 0,
            "external_submissions": 0,
            "second_promotion_attempts": 0,
        },
    }

    lock_path = ENGINE / ".frontier_pipeline.lock"
    try:
        with lock_path.open("a+") as pipeline_lock:
            fcntl.flock(pipeline_lock.fileno(), fcntl.LOCK_EX | fcntl.LOCK_NB)

            apply_result = load_json(PROMOTION / "APPLY_RESULT.json")
            pre_execute = load_json(PROMOTION / "PRE_EXECUTE.json")
            manifest = load_json(RUN / "MANIFEST.json")
            input_lock = load_json(RUN / "INPUT_LOCK.json")
            state = load_json(RUN / "STATE.json")
            assignment = load_json(RUN / "staged/assignment_report.json")
            validation = load_json(RUN / "validation/validation_report.json")

            manifest_actual = sha256(RUN / "MANIFEST.json")
            check(checks, "sealed_manifest_sha256", manifest_actual == APPROVED_MANIFEST_SHA256, {
                "actual": manifest_actual,
                "approved": APPROVED_MANIFEST_SHA256,
            })
            check(checks, "apply_state", apply_result.get("status") == "APPLIED_PENDING_INDEPENDENT_VERIFICATION", apply_result.get("status"))
            check(checks, "promotion_contract_consistency", (
                apply_result.get("manifest_sha256") == APPROVED_MANIFEST_SHA256
                and pre_execute.get("manifest_sha256") == APPROVED_MANIFEST_SHA256
                and pre_execute.get("target_count") == 3
                and set(apply_result.get("targets_after", {})) == set(TARGETS)
                and set(pre_execute.get("targets_after", {})) == set(TARGETS)
            ), {
                "apply_manifest": apply_result.get("manifest_sha256"),
                "pre_execute_manifest": pre_execute.get("manifest_sha256"),
                "target_count": pre_execute.get("target_count"),
            })

            apply_script = Path(pre_execute["apply_script"])
            rollback_script = Path(pre_execute["rollback_script"])
            script_checks = {
                "apply_actual": sha256(apply_script),
                "apply_expected": pre_execute["apply_script_sha256"],
                "rollback_actual": sha256(rollback_script),
                "rollback_expected": pre_execute["rollback_script_sha256"],
            }
            check(checks, "promotion_and_rollback_script_hashes", (
                script_checks["apply_actual"] == script_checks["apply_expected"] == apply_result["apply_script_sha256"]
                and script_checks["rollback_actual"] == script_checks["rollback_expected"]
            ), script_checks)

            transaction_marker = ENGINE / "delta/.ingest_transaction.json"
            check(checks, "pipeline_lock_and_transaction_state", not transaction_marker.exists(), {
                "exclusive_lock_acquired": True,
                "transaction_marker_exists": transaction_marker.exists(),
            })

            target_state: dict[str, Any] = {}
            for name in TARGETS:
                active = ENGINE / "delta" / name
                shadow = RUN / "shadow_engine/delta" / name
                snapshot = PROMOTION / "rollback_snapshot" / name
                active_fp = fingerprint(active)
                shadow_fp = fingerprint(shadow)
                snapshot_fp = fingerprint(snapshot)
                expected_after = apply_result["targets_after"][name]
                expected_before = apply_result["targets_before"][name]
                target_state[name] = {
                    "active": active_fp,
                    "shadow": shadow_fp,
                    "rollback_snapshot": snapshot_fp,
                    "expected_after": {"bytes": expected_after["bytes"], "sha256": expected_after["sha256"]},
                    "expected_before": {"bytes": expected_before["bytes"], "sha256": expected_before["sha256"]},
                }
                check(checks, f"target_after_{name}", (
                    active_fp == {"bytes": expected_after["bytes"], "sha256": expected_after["sha256"]}
                    and shadow_fp == active_fp
                    and pre_execute["targets_after"][name]["sha256"] == active_fp["sha256"]
                    and pre_execute["targets_after"][name]["bytes"] == active_fp["bytes"]
                ), target_state[name])
                check(checks, f"rollback_snapshot_{name}", snapshot_fp == {
                    "bytes": expected_before["bytes"], "sha256": expected_before["sha256"]
                }, target_state[name])
            report["targets"] = target_state

            snapshot_papers = (PROMOTION / "rollback_snapshot/new_papers.jsonl").read_bytes()
            active_papers = (ENGINE / "delta/new_papers.jsonl").read_bytes()
            staged_papers = (RUN / "staged/assigned_new_papers.jsonl").read_bytes()
            snapshot_vectors = (PROMOTION / "rollback_snapshot/new_emb.f32").read_bytes()
            active_vectors = (ENGINE / "delta/new_emb.f32").read_bytes()
            staged_vectors = (RUN / "staged/new_emb.f32").read_bytes()
            check(checks, "historical_and_append_byte_prefixes", (
                active_papers == snapshot_papers + staged_papers
                and active_vectors == snapshot_vectors + staged_vectors
            ), {
                "paper_prefix_bytes": len(snapshot_papers),
                "paper_append_bytes": len(staged_papers),
                "vector_prefix_bytes": len(snapshot_vectors),
                "vector_append_bytes": len(staged_vectors),
            })

            old_rows = load_jsonl(PROMOTION / "rollback_snapshot/new_papers.jsonl")
            active_rows = load_jsonl(ENGINE / "delta/new_papers.jsonl")
            appended_rows = load_jsonl(RUN / "staged/assigned_new_papers.jsonl")
            old_ids = [str(row["arxiv_id"]) for row in old_rows]
            active_ids = [str(row["arxiv_id"]) for row in active_rows]
            appended_ids = [str(row["arxiv_id"]) for row in appended_rows]
            duplicate_active_ids = sorted(key for key, count in Counter(active_ids).items() if count != 1)
            check(checks, "paper_counts_order_and_uniqueness", (
                len(old_rows) == input_lock["baseline"]["delta_papers"] == 720
                and len(appended_rows) == assignment["papers"] == 233
                and len(active_rows) == 953
                and active_ids == old_ids + appended_ids
                and not duplicate_active_ids
            ), {
                "before": len(old_rows),
                "appended": len(appended_rows),
                "after": len(active_rows),
                "duplicate_active_ids": duplicate_active_ids,
            })

            state_ids = [str(value) for value in state["details"]["corpus_gate_complete"]["accepted_ids"]]
            check(checks, "accepted_id_custody", appended_ids == state_ids, {
                "state_accepted": len(state_ids),
                "appended": len(appended_ids),
                "same_order": appended_ids == state_ids,
            })

            old_labels = load_json(PROMOTION / "rollback_snapshot/new_labels.json")
            active_labels = load_json(ENGINE / "delta/new_labels.json")
            labels_preserved = all(active_labels.get(key) == value for key, value in old_labels.items())
            paper_label_clusters_match = all(active_labels.get(str(row["arxiv_id"])) == int(row["cluster"]) for row in active_rows)
            check(checks, "paper_label_alignment", (
                len(old_labels) == len(old_rows)
                and len(active_labels) == len(active_rows)
                and set(active_labels) == set(active_ids)
                and labels_preserved
                and paper_label_clusters_match
            ), {
                "before_labels": len(old_labels),
                "after_labels": len(active_labels),
                "key_sets_equal": set(active_labels) == set(active_ids),
                "historical_labels_preserved": labels_preserved,
                "paper_clusters_match_labels": paper_label_clusters_match,
            })

            vector_width = DIM * 4
            vectors = np.fromfile(ENGINE / "delta/new_emb.f32", dtype=np.float32)
            vector_rows = vectors.size // DIM if vectors.size % DIM == 0 else -1
            matrix = vectors.reshape(vector_rows, DIM) if vector_rows >= 0 else np.empty((0, DIM), dtype=np.float32)
            finite = bool(np.isfinite(matrix).all())
            zero_norm_rows = int(np.count_nonzero(np.linalg.norm(matrix, axis=1) == 0)) if vector_rows >= 0 else -1
            check(checks, "paper_label_vector_alignment_and_values", (
                len(active_vectors) == len(active_rows) * vector_width
                and vector_rows == len(active_rows)
                and finite
                and zero_norm_rows == 0
            ), {
                "dimension": DIM,
                "paper_rows": len(active_rows),
                "vector_rows": vector_rows,
                "embedding_bytes": len(active_vectors),
                "expected_embedding_bytes": len(active_rows) * vector_width,
                "all_finite": finite,
                "zero_norm_rows": zero_norm_rows,
            })

            base_path = Path(input_lock["engine_root"]) / "corpus_ga_co_2009_2026.jsonl"
            base = scan_base(base_path)
            base_overlap = sorted(set(appended_ids) & base["arxiv_ids"])
            old_overlap = sorted(set(appended_ids) & set(old_ids))
            check(checks, "base_and_prior_delta_deduplication", (
                base["rows"] == input_lock["baseline"]["base_rows"]
                and base["sha256"] == input_lock["protected_files"][str(base_path)]["sha256"]
                and base["bytes"] == input_lock["protected_files"][str(base_path)]["bytes"]
                and not base_overlap
                and not old_overlap
            ), {
                "base_rows": base["rows"],
                "base_arxiv_ids": len(base["arxiv_ids"]),
                "base_overlap": base_overlap,
                "prior_delta_overlap": old_overlap,
            })

            protected_mismatches = []
            protected_checked = 0
            for raw_path, expected in input_lock["protected_files"].items():
                path = Path(raw_path)
                if path.parent == ENGINE / "delta" and path.name in TARGETS:
                    continue
                protected_checked += 1
                if path == base_path:
                    actual = {"bytes": base["bytes"], "sha256": base["sha256"]}
                elif path.is_file():
                    actual = fingerprint(path)
                else:
                    actual = {"bytes": None, "sha256": None}
                wanted = {"bytes": expected["bytes"], "sha256": expected["sha256"]}
                if actual != wanted:
                    protected_mismatches.append({"path": str(path), "expected": wanted, "actual": actual})
            check(checks, "protected_non_target_files", not protected_mismatches, {
                "checked": protected_checked,
                "mismatches": protected_mismatches,
            })

            manifest_mismatches = []
            for artifact in manifest["artifacts"]:
                path = RUN / artifact["path"]
                actual = fingerprint(path) if path.is_file() else {"bytes": None, "sha256": None}
                wanted = {"bytes": artifact["bytes"], "sha256": artifact["sha256"]}
                if actual != wanted:
                    manifest_mismatches.append({"path": artifact["path"], "expected": wanted, "actual": actual})
            check(checks, "sealed_manifest_artifacts", not manifest_mismatches, {
                "checked": len(manifest["artifacts"]),
                "mismatches": manifest_mismatches,
            })

            checksum_mismatches = []
            checksum_entries = 0
            for line in (RUN / "validation/SHA256SUMS.txt").read_text(encoding="utf-8").splitlines():
                if not line.strip():
                    continue
                expected_hash, relative = line.split("  ", 1)
                checksum_entries += 1
                path = RUN / relative
                actual_hash = sha256(path) if path.is_file() else None
                if actual_hash != expected_hash:
                    checksum_mismatches.append({"path": relative, "expected": expected_hash, "actual": actual_hash})
            check(checks, "validation_checksum_ledger", not checksum_mismatches, {
                "checked": checksum_entries,
                "mismatches": checksum_mismatches,
            })

            # Rank movement is defined against the canonical prior rerank, not
            # the immutable base map. The runner copied this file before
            # overwriting the shadow copy with the new preview.
            previous = load_json(ENGINE / "frontier_map_v3_reranked.json")
            current = load_json(RUN / "shadow_engine/frontier_map_v3_reranked.preview.json")
            movements = load_json(RUN / "ranking/rank_movements.json")
            previous_rows = {int(row["cluster"]): row for row in previous["clusters"]}
            current_rows = {int(row["cluster"]): row for row in current["clusters"]}
            previous_ranks = tractable_ranks(previous)
            current_ranks = tractable_ranks(current)
            assigned_by_cluster = Counter(int(row["cluster"]) for row in appended_rows if int(row["cluster"]) != -1)
            rank_errors = []
            review_holds = []
            for cluster, current_rank in current_ranks.items():
                previous_rank = previous_ranks.get(cluster, current_rank)
                delta = previous_rank - current_rank
                movement = movements.get(str(cluster))
                expected_movement = {
                    "cluster": cluster,
                    "currentRank": current_rank,
                    "delta": delta,
                    "deltaPapers": assigned_by_cluster.get(cluster, 0),
                    "previousRank": previous_rank,
                }
                if movement != expected_movement:
                    rank_errors.append({"cluster": cluster, "expected": expected_movement, "actual": movement})
                if abs(delta) >= 3:
                    review_holds.append({"type": "rank_move_ge_3", "cluster": cluster, "delta": delta})
                if cluster in previous_rows and previous_rows[cluster].get("tractable") != current_rows[cluster].get("tractable"):
                    review_holds.append({"type": "tractability_flip", "cluster": cluster})
            extra_movement_keys = sorted(set(movements) - {str(key) for key in current_ranks})
            check(checks, "ranking_constants_ranks_and_holds", (
                current.get("constants_frozen") is True
                and current.get("v1_constants") == previous.get("v1_constants")
                and sorted(current_ranks.values()) == list(range(1, len(current_ranks) + 1))
                and not rank_errors
                and not extra_movement_keys
                and not review_holds
                and validation.get("review_holds") == []
            ), {
                "constants_frozen": current.get("constants_frozen"),
                "constants_equal": current.get("v1_constants") == previous.get("v1_constants"),
                "tractable_ranks": len(current_ranks),
                "rank_errors": rank_errors,
                "extra_movement_keys": extra_movement_keys,
                "recomputed_review_holds": review_holds,
            })

            git_status = subprocess.run(
                ["git", "status", "--short"], cwd=REPO, text=True, capture_output=True, check=False
            )
            current_git_lines = git_status.stdout.splitlines()
            check(checks, "git_status_unchanged", (
                git_status.returncode == 0 and current_git_lines == input_lock["git_status_lines"]
            ), {
                "returncode": git_status.returncode,
                "baseline_line_count": len(input_lock["git_status_lines"]),
                "current_line_count": len(current_git_lines),
                "lines_equal": current_git_lines == input_lock["git_status_lines"],
                "stderr": git_status.stderr,
            })

            test_env = os.environ.copy()
            test_env["PYTHONDONTWRITEBYTECODE"] = "1"
            test_command = [
                str(PYTHON), "-m", "pytest", "-q", "-p", "no:cacheprovider",
                "tests/test_overnight_frontier_preview.py",
            ]
            tests = subprocess.run(
                test_command, cwd=RUN, env=test_env, text=True, capture_output=True, check=False
            )
            check(checks, "post_promotion_test_suite", tests.returncode == 0, {
                "command": test_command,
                "returncode": tests.returncode,
                "stdout": tests.stdout[-4000:],
                "stderr": tests.stderr[-4000:],
            })

            report["corpus"] = {
                "base_rows": base["rows"],
                "delta_rows_before": len(old_rows),
                "delta_rows_added": len(appended_rows),
                "delta_rows_after": len(active_rows),
                "labels_after": len(active_labels),
                "vector_rows_after": vector_rows,
                "embedding_dimension": DIM,
                "assigned_added": assignment["assigned"],
                "novel_or_noise_added": assignment["novel_or_noise"],
                "drift_far_added": assignment["drift_far"],
            }
            report["status"] = "INDEPENDENT_VERIFICATION_PASS"
            report["all_checks_pass"] = True
            report["check_count"] = len(checks)
            report["verification_phase_canonical_mutation"] = False
            atomic_json(REPORT, report)
            fcntl.flock(pipeline_lock.fileno(), fcntl.LOCK_UN)
    except BaseException as exc:
        report["all_checks_pass"] = False
        report["error"] = repr(exc)
        report["check_count"] = len(checks)
        atomic_json(REPORT, report)
        print(json.dumps(report, indent=2, sort_keys=True))
        return 1

    print(json.dumps(report, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
