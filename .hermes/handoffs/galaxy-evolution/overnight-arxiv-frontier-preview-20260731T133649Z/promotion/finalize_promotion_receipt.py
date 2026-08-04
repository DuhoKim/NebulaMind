#!/usr/bin/env python3
"""Seal the verified frontier-delta promotion receipt and rollback handoff."""

from __future__ import annotations

import datetime as dt
import fcntl
import hashlib
import json
import os
from pathlib import Path
from typing import Any

RUN = Path("/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/overnight-arxiv-frontier-preview-20260731T133649Z")
ENGINE = Path("/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/corpus-ga-co-2009-2026-20260718")
PROMOTION = RUN / "promotion"
RECEIPT = PROMOTION / "PROMOTION_RECEIPT.json"
HANDOFF = PROMOTION / "ROLLBACK_HANDOFF.md"
RESULT = PROMOTION / "FINALIZATION_RESULT.json"
VERIFY_REPORT = PROMOTION / "INDEPENDENT_VERIFICATION.json"
TARGETS = ("new_emb.f32", "new_papers.jsonl", "new_labels.json")
MANIFEST_SHA256 = "aaa9d4fe45da6a8f12b68325c1dd20f1c141f6f24a9929b99e50ce471dc6b0ba"


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


def atomic_bytes(path: Path, body: bytes) -> None:
    temp = path.with_name(f".{path.name}.{os.getpid()}.tmp")
    with temp.open("wb") as handle:
        handle.write(body)
        handle.flush()
        os.fsync(handle.fileno())
    os.replace(temp, path)


def atomic_json(path: Path, payload: dict[str, Any]) -> None:
    body = (json.dumps(payload, indent=2, sort_keys=True) + "\n").encode("utf-8")
    atomic_bytes(path, body)


def fsync_dir(path: Path) -> None:
    fd = os.open(path, os.O_RDONLY)
    try:
        os.fsync(fd)
    finally:
        os.close(fd)


def check_row(report: dict[str, Any], name: str) -> dict[str, Any]:
    for row in report.get("checks", []):
        if row.get("name") == name:
            return row
    raise RuntimeError(f"verification report is missing check: {name}")


def main() -> int:
    if RECEIPT.exists() or HANDOFF.exists() or RESULT.exists():
        raise RuntimeError("final custody artifact already exists; refusing to overwrite")

    lock_path = ENGINE / ".frontier_pipeline.lock"
    with lock_path.open("a+") as pipeline_lock:
        fcntl.flock(pipeline_lock.fileno(), fcntl.LOCK_EX | fcntl.LOCK_NB)

        if (ENGINE / "delta/.ingest_transaction.json").exists():
            raise RuntimeError("active ingest transaction marker exists")

        manifest_actual = sha256(RUN / "MANIFEST.json")
        if manifest_actual != MANIFEST_SHA256:
            raise RuntimeError("sealed manifest checksum drift")

        apply_result = load_json(PROMOTION / "APPLY_RESULT.json")
        pre_execute = load_json(PROMOTION / "PRE_EXECUTE.json")
        verification = load_json(VERIFY_REPORT)
        if verification.get("status") != "INDEPENDENT_VERIFICATION_PASS" or verification.get("all_checks_pass") is not True:
            raise RuntimeError("independent verification has not passed")
        if verification.get("check_count") != 23 or any(row.get("pass") is not True for row in verification.get("checks", [])):
            raise RuntimeError("independent verification check ledger is incomplete")
        verifier_path = Path(verification["verifier"])
        if sha256(verifier_path) != verification["verifier_sha256"]:
            raise RuntimeError("independent verifier script checksum drift")

        target_readback: dict[str, Any] = {}
        for name in TARGETS:
            active = ENGINE / "delta" / name
            snapshot = PROMOTION / "rollback_snapshot" / name
            active_fp = fingerprint(active)
            snapshot_fp = fingerprint(snapshot)
            expected_after = apply_result["targets_after"][name]
            expected_before = apply_result["targets_before"][name]
            if active_fp != {"bytes": expected_after["bytes"], "sha256": expected_after["sha256"]}:
                raise RuntimeError(f"canonical target drift after independent verification: {name}")
            if snapshot_fp != {"bytes": expected_before["bytes"], "sha256": expected_before["sha256"]}:
                raise RuntimeError(f"rollback snapshot drift after independent verification: {name}")
            if verification["targets"][name]["active"] != active_fp:
                raise RuntimeError(f"verification report target mismatch: {name}")
            target_readback[name] = active_fp

        verification_sha = sha256(VERIFY_REPORT)
        finalized_at = dt.datetime.now(dt.timezone.utc).isoformat()
        hwao_relay = PROMOTION / "HWAO_VERIFICATION_RELAY.md"
        receipt = {
            "schema_version": 1,
            "status": "EXECUTED_AND_VERIFIED",
            "run_id": RUN.name,
            "manifest_sha256": MANIFEST_SHA256,
            "applied_at_utc": apply_result["applied_at_utc"],
            "verified_at_utc": verification["verified_at_utc"],
            "finalized_at_utc": finalized_at,
            "apply_result": {
                "path": str(PROMOTION / "APPLY_RESULT.json"),
                "sha256": sha256(PROMOTION / "APPLY_RESULT.json"),
                "original_status": apply_result["status"],
            },
            "pre_execute": {
                "path": str(PROMOTION / "PRE_EXECUTE.json"),
                "sha256": sha256(PROMOTION / "PRE_EXECUTE.json"),
            },
            "independent_verification": {
                "path": str(VERIFY_REPORT),
                "sha256": verification_sha,
                "status": verification["status"],
                "check_count": verification["check_count"],
                "verifier_sha256": verification["verifier_sha256"],
                "post_promotion_tests": check_row(verification, "post_promotion_test_suite")["details"],
            },
            "apply_script": {
                "path": pre_execute["apply_script"],
                "sha256": pre_execute["apply_script_sha256"],
            },
            "rollback_script": {
                "path": pre_execute["rollback_script"],
                "sha256": pre_execute["rollback_script_sha256"],
                "requires_fresh_explicit_approval": True,
            },
            "replace_order": apply_result["replace_order"],
            "target_count": 3,
            "targets_before": apply_result["targets_before"],
            "targets_after": apply_result["targets_after"],
            "target_readback": target_readback,
            "rollback_snapshot": apply_result["rollback_snapshot"],
            "corpus": verification["corpus"],
            "ranking": {
                "constants_frozen": check_row(verification, "ranking_constants_ranks_and_holds")["details"]["constants_frozen"],
                "rank_errors": check_row(verification, "ranking_constants_ranks_and_holds")["details"]["rank_errors"],
                "review_holds": check_row(verification, "ranking_constants_ranks_and_holds")["details"]["recomputed_review_holds"],
            },
            "coordinator_relay": {
                "attempted_before_verification": True,
                "result": "HWAO_PANE_BLOCKED_NOT_LOGGED_IN",
                "relay_path": str(hwao_relay),
                "relay_sha256": sha256(hwao_relay),
            },
            "excluded": [
                "DB/SQL",
                "frontend/live/public/cockpit",
                "wiki/evidence/trust",
                "scheduler/cron/LaunchAgent",
                "deploy/restart",
                "external submission",
                "Git commit/push/merge",
                "second promotion",
            ],
            "safety_ledger": {
                "canonical_target_files_replaced_by_approved_promotion": 3,
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
            "next_gate": "Any product/frontend/live/public application is a separate explicit approval gate.",
        }
        atomic_json(RECEIPT, receipt)
        os.chmod(RECEIPT, 0o444)
        receipt_sha = sha256(RECEIPT)

        rollback_command = (
            f"/Users/duhokim/NebulaMind/NebulaMind/backend/.venv/bin/python "
            f"{pre_execute['rollback_script']} --execute --receipt-sha {receipt_sha}"
        )
        handoff = f"""# Local frontier-delta promotion custody

Status: `EXECUTED_AND_VERIFIED`
Run: `{RUN.name}`
Manifest SHA-256: `{MANIFEST_SHA256}`
Promotion receipt SHA-256: `{receipt_sha}`
Independent verification SHA-256: `{verification_sha}`

## Verified state

- Canonical delta rows: 720 before + 233 appended = 953 after.
- Labels: 953, with exact paper-ID set and matching cluster values.
- Embeddings: 953 × 2560 float32 vectors; all finite; zero zero-norm rows.
- Historical paper and embedding bytes are exact prefixes.
- Appended paper and embedding bytes exactly match staged artifacts.
- New IDs overlap neither the 120,676-row immutable base nor the prior 720-row delta.
- All 15 protected non-target files match their locked hashes.
- All 47 sealed-manifest artifacts and all 47 checksum-ledger entries match.
- Frozen ranking constants, rank arithmetic, and zero review holds independently verified.
- Git status exactly matches the input lock.
- Post-promotion suite: 13 passed.

## Active target hashes

- `new_papers.jsonl`: `{target_readback['new_papers.jsonl']['sha256']}`
- `new_labels.json`: `{target_readback['new_labels.json']['sha256']}`
- `new_emb.f32`: `{target_readback['new_emb.f32']['sha256']}`

## Safety boundary

The approved promotion replaced exactly the three local canonical delta files. Verification made zero canonical writes. No DB/SQL, frontend/live/public/cockpit, wiki/evidence/trust, scheduler/cron/LaunchAgent, deploy/restart, external-submission, or Git write occurred. No second promotion was attempted.

Any product/frontend/live/public application remains a separate explicit approval gate.

## Rollback custody — do not execute without fresh explicit approval

The rollback snapshot and guarded rollback script are sealed by the receipt. If rollback is explicitly approved, the hash-bound command is:

`{rollback_command}`

The rollback script refuses execution unless the active targets still match this verified after-state and the snapshot still matches the exact before-state.
"""
        atomic_bytes(HANDOFF, handoff.encode("utf-8"))
        os.chmod(HANDOFF, 0o444)
        handoff_sha = sha256(HANDOFF)

        finalization_result = {
            "status": "FINAL_CUSTODY_SEALED_AND_READ_BACK",
            "finalized_at_utc": finalized_at,
            "promotion_receipt": {"path": str(RECEIPT), "sha256": receipt_sha, "bytes": RECEIPT.stat().st_size, "mode": "0444"},
            "rollback_handoff": {"path": str(HANDOFF), "sha256": handoff_sha, "bytes": HANDOFF.stat().st_size, "mode": "0444"},
            "independent_verification": {"path": str(VERIFY_REPORT), "sha256": verification_sha},
            "target_readback": target_readback,
            "second_promotion_attempts": 0,
        }
        atomic_json(RESULT, finalization_result)
        os.chmod(RESULT, 0o444)
        fsync_dir(PROMOTION)

        receipt_readback = load_json(RECEIPT)
        result_readback = load_json(RESULT)
        if receipt_readback.get("status") != "EXECUTED_AND_VERIFIED":
            raise RuntimeError("receipt readback failed")
        if result_readback.get("promotion_receipt", {}).get("sha256") != receipt_sha:
            raise RuntimeError("finalization result readback failed")

        fcntl.flock(pipeline_lock.fileno(), fcntl.LOCK_UN)

    print(json.dumps(finalization_result, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
