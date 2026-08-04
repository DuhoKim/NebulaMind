#!/usr/bin/env python3
"""Rollback an executed local frontier-delta promotion after a fresh exact gate."""

from __future__ import annotations

import argparse
import fcntl
import hashlib
import json
import os
import shutil
from pathlib import Path

RUN = Path("/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/overnight-arxiv-frontier-preview-20260731T133649Z")
ENGINE = Path("/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/corpus-ga-co-2009-2026-20260718")
PROMOTION = RUN / "promotion"
SNAPSHOT = PROMOTION / "rollback_snapshot"
TARGETS = ("new_emb.f32", "new_papers.jsonl", "new_labels.json")


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def atomic_json(path: Path, payload: dict) -> None:
    temp = path.with_name(f".{path.name}.{os.getpid()}.tmp")
    temp.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n")
    os.replace(temp, path)


def staged_copy(source: Path, target: Path) -> Path:
    temp = target.with_name(f".{target.name}.{os.getpid()}.rollback")
    with source.open("rb") as src, temp.open("wb") as dst:
        shutil.copyfileobj(src, dst, length=1024 * 1024)
        dst.flush()
        os.fsync(dst.fileno())
    if sha256(temp) != sha256(source):
        temp.unlink(missing_ok=True)
        raise RuntimeError(f"rollback staging checksum mismatch: {target.name}")
    return temp


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--receipt-sha", required=True)
    parser.add_argument("--execute", action="store_true")
    args = parser.parse_args()
    if not args.execute:
        raise RuntimeError("rollback requires --execute")
    receipt_path = PROMOTION / "PROMOTION_RECEIPT.json"
    if not receipt_path.is_file() or sha256(receipt_path) != args.receipt_sha:
        raise RuntimeError("promotion receipt checksum mismatch")
    receipt = json.loads(receipt_path.read_text())
    if receipt.get("status") != "EXECUTED_AND_VERIFIED":
        raise RuntimeError("promotion receipt is not executable rollback custody")
    lock_path = ENGINE / ".frontier_pipeline.lock"
    with lock_path.open("a+") as lock:
        fcntl.flock(lock.fileno(), fcntl.LOCK_EX | fcntl.LOCK_NB)
        expected_after = receipt["targets_after"]
        expected_before = receipt["targets_before"]
        for name in TARGETS:
            active = ENGINE / "delta" / name
            snap = SNAPSHOT / name
            if sha256(active) != expected_after[name]["sha256"]:
                raise RuntimeError(f"active target drift before rollback: {name}")
            if sha256(snap) != expected_before[name]["sha256"]:
                raise RuntimeError(f"rollback snapshot drift: {name}")
        staged = {name: staged_copy(SNAPSHOT / name, ENGINE / "delta" / name) for name in TARGETS}
        for name in TARGETS:
            os.replace(staged[name], ENGINE / "delta" / name)
        for name in TARGETS:
            if sha256(ENGINE / "delta" / name) != expected_before[name]["sha256"]:
                raise RuntimeError(f"rollback verification failed: {name}")
        fcntl.flock(lock.fileno(), fcntl.LOCK_UN)
    result = {
        "status": "ROLLED_BACK_AND_VERIFIED",
        "promotion_receipt_sha256": args.receipt_sha,
        "restored": {name: {"sha256": sha256(ENGINE / "delta" / name)} for name in TARGETS},
    }
    atomic_json(PROMOTION / "ROLLBACK_RESULT.json", result)
    print(json.dumps(result, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
