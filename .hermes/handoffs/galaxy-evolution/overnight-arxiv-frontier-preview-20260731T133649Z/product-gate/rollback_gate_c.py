#!/usr/bin/env python3
"""Guarded rollback for the approved Gate C frontier-ranking application."""

from __future__ import annotations

import argparse
import fcntl
import hashlib
import json
import os
import shutil
import stat
import tempfile
from pathlib import Path

ROOT = Path("/Users/duhokim/NebulaMind/NebulaMind")
RUN = ROOT / ".hermes/handoffs/galaxy-evolution/overnight-arxiv-frontier-preview-20260731T133649Z"
PRODUCT_GATE = RUN / "product-gate"
ENGINE = ROOT / ".hermes/handoffs/galaxy-evolution/corpus-ga-co-2009-2026-20260718"
RECEIPT = PRODUCT_GATE / "GATE_C_RECEIPT.json"
RESULT = PRODUCT_GATE / "ROLLBACK_RESULT.json"
LOCK = ENGINE / ".frontier_pipeline.lock"
TRANSACTION = ENGINE / "delta/.ingest_transaction.json"


def fingerprint(path: Path) -> dict[str, object]:
    digest = hashlib.sha256()
    size = 0
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
            size += len(chunk)
    return {"sha256": digest.hexdigest(), "bytes": size}


def fsync_dir(path: Path) -> None:
    fd = os.open(path, os.O_RDONLY)
    try:
        os.fsync(fd)
    finally:
        os.close(fd)


def atomic_replace_from(source: Path, target: Path) -> None:
    mode = stat.S_IMODE(target.stat().st_mode)
    fd, tmp_name = tempfile.mkstemp(prefix=f".{target.name}.rollback-", dir=target.parent)
    tmp = Path(tmp_name)
    try:
        with os.fdopen(fd, "wb") as output, source.open("rb") as input_handle:
            shutil.copyfileobj(input_handle, output)
            output.flush()
            os.fsync(output.fileno())
        os.chmod(tmp, mode)
        os.replace(tmp, target)
        fsync_dir(target.parent)
    finally:
        if tmp.exists():
            tmp.unlink()


def exact(path: Path, expected: dict[str, object]) -> bool:
    return path.is_file() and fingerprint(path) == {
        "sha256": expected["sha256"],
        "bytes": expected["bytes"],
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--execute", action="store_true")
    parser.add_argument("--receipt-sha", required=True)
    args = parser.parse_args()
    if not args.execute:
        raise SystemExit("Refusing rollback without --execute")
    if RESULT.exists():
        raise SystemExit("Rollback result already exists; refusing a second rollback")
    if fingerprint(RECEIPT)["sha256"] != args.receipt_sha:
        raise SystemExit("Receipt SHA-256 mismatch")
    receipt = json.loads(RECEIPT.read_text())
    if receipt.get("status") != "SOURCE_APPLIED_BUILD_VERIFIED_AWAITING_RESTART_GATE":
        raise SystemExit("Receipt status does not authorize guarded rollback")
    if TRANSACTION.exists():
        raise SystemExit("Active delta transaction marker")

    order = [
        "live_frontend_source_ts",
        "worktree_frontend_ts",
        "canonical_staging_ts",
        "canonical_rerank",
    ]
    before = receipt["targets_before"]
    after = receipt["targets_after"]
    for name in order:
        target = Path(after[name]["path"])
        backup = Path(before[name]["backup"])
        if not exact(target, after[name]):
            raise SystemExit(f"Active target drift: {name}")
        if not exact(backup, before[name]):
            raise SystemExit(f"Rollback snapshot drift: {name}")

    LOCK.parent.mkdir(parents=True, exist_ok=True)
    lock_handle = LOCK.open("a+")
    restored: list[str] = []
    try:
        try:
            fcntl.flock(lock_handle.fileno(), fcntl.LOCK_EX | fcntl.LOCK_NB)
        except BlockingIOError as exc:
            raise SystemExit("Frontier pipeline lock is busy") from exc
        if TRANSACTION.exists():
            raise SystemExit("Transaction marker appeared after lock acquisition")
        for name in order:
            target = Path(after[name]["path"])
            if not exact(target, after[name]):
                raise SystemExit(f"Target changed after lock acquisition: {name}")
        try:
            for name in order:
                target = Path(after[name]["path"])
                backup = Path(before[name]["backup"])
                atomic_replace_from(backup, target)
                if not exact(target, before[name]):
                    raise RuntimeError(f"Rollback readback failed: {name}")
                restored.append(name)
        except Exception as exc:
            recovery_errors: list[str] = []
            for name in reversed(restored):
                target = Path(after[name]["path"])
                source = Path(after[name]["source"])
                try:
                    atomic_replace_from(source, target)
                    if not exact(target, after[name]):
                        recovery_errors.append(name)
                except Exception:
                    recovery_errors.append(name)
            raise SystemExit(
                f"Rollback failed; after-state recovery attempted; recovery_errors={recovery_errors}: {exc}"
            ) from exc
        result = {
            "schema_version": 1,
            "status": "ROLLED_BACK_AND_VERIFIED",
            "receipt_sha256": args.receipt_sha,
            "restored_order": order,
            "targets": {
                name: fingerprint(Path(after[name]["path"])) for name in order
            },
            "safety_ledger": {
                "restored_target_files": 4,
                "db_sql_api_writes": 0,
                "git_index_history_writes": 0,
                "deploy_restart_actions": 0,
                "external_submissions": 0,
            },
        }
        fd, tmp_name = tempfile.mkstemp(prefix=".ROLLBACK_RESULT.", dir=PRODUCT_GATE)
        tmp = Path(tmp_name)
        try:
            with os.fdopen(fd, "w", encoding="utf-8") as handle:
                json.dump(result, handle, indent=2, sort_keys=True)
                handle.write("\n")
                handle.flush()
                os.fsync(handle.fileno())
            os.replace(tmp, RESULT)
            fsync_dir(PRODUCT_GATE)
        finally:
            if tmp.exists():
                tmp.unlink()
    finally:
        try:
            fcntl.flock(lock_handle.fileno(), fcntl.LOCK_UN)
        finally:
            lock_handle.close()
    print(json.dumps({"status": "ROLLED_BACK_AND_VERIFIED", "targets": 4}))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
