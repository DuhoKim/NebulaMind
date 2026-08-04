#!/usr/bin/env python3
"""Guarded promotion of exactly three local NebulaMind frontier-delta files."""

from __future__ import annotations

import argparse
import datetime as dt
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
MANIFEST_SHA = "aaa9d4fe45da6a8f12b68325c1dd20f1c141f6f24a9929b99e50ce471dc6b0ba"
TARGET_MAP = {
    "new_papers.jsonl": "shadow_engine/delta/new_papers.jsonl",
    "new_labels.json": "shadow_engine/delta/new_labels.json",
    "new_emb.f32": "shadow_engine/delta/new_emb.f32",
}
REPLACE_ORDER = ("new_emb.f32", "new_papers.jsonl", "new_labels.json")


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def atomic_json(path: Path, payload: dict) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    temp = path.with_name(f".{path.name}.{os.getpid()}.tmp")
    with temp.open("w", encoding="utf-8") as handle:
        json.dump(payload, handle, indent=2, sort_keys=True)
        handle.write("\n")
        handle.flush()
        os.fsync(handle.fileno())
    os.replace(temp, path)


def staged_copy(source: Path, target: Path, suffix: str) -> Path:
    temp = target.with_name(f".{target.name}.{os.getpid()}.{suffix}")
    with source.open("rb") as src, temp.open("wb") as dst:
        shutil.copyfileobj(src, dst, length=1024 * 1024)
        dst.flush()
        os.fsync(dst.fileno())
    if sha256(temp) != sha256(source):
        temp.unlink(missing_ok=True)
        raise RuntimeError(f"staged copy checksum mismatch: {target.name}")
    return temp


def fsync_dir(path: Path) -> None:
    fd = os.open(path, os.O_RDONLY)
    try:
        os.fsync(fd)
    finally:
        os.close(fd)


def load_contract() -> tuple[dict, dict, dict, dict]:
    manifest_path = RUN / "MANIFEST.json"
    if sha256(manifest_path) != MANIFEST_SHA:
        raise RuntimeError("sealed manifest checksum mismatch")
    manifest = json.loads(manifest_path.read_text())
    if manifest.get("verdict") != "PREVIEW_READY_FOR_REVIEW":
        raise RuntimeError("preview verdict is not promotable")
    lock = json.loads((RUN / "INPUT_LOCK.json").read_text())
    artifacts = {row["path"]: row for row in manifest["artifacts"]}
    before = {}
    after = {}
    for name, relative in TARGET_MAP.items():
        active = ENGINE / "delta" / name
        shadow = RUN / relative
        before[name] = lock["protected_files"][str(active)]
        after[name] = artifacts[relative]
        if sha256(active) != before[name]["sha256"] or active.stat().st_size != before[name]["bytes"]:
            raise RuntimeError(f"active precondition drift: {name}")
        if sha256(shadow) != after[name]["sha256"] or shadow.stat().st_size != after[name]["bytes"]:
            raise RuntimeError(f"shadow after-state drift: {name}")
    other_mismatches = []
    for raw, expected in lock["protected_files"].items():
        path = Path(raw)
        if path.parent == ENGINE / "delta" and path.name in TARGET_MAP:
            continue
        actual = sha256(path) if path.is_file() else None
        if actual != expected["sha256"]:
            other_mismatches.append(raw)
    if other_mismatches:
        raise RuntimeError(f"non-target protected drift: {other_mismatches}")
    if (ENGINE / "delta/.ingest_transaction.json").exists():
        raise RuntimeError("active ingest transaction marker exists")
    return manifest, lock, before, after


def ensure_snapshot(before: dict) -> None:
    SNAPSHOT.mkdir(parents=True, exist_ok=True)
    for name in TARGET_MAP:
        active = ENGINE / "delta" / name
        snap = SNAPSHOT / name
        if snap.exists():
            if sha256(snap) != before[name]["sha256"]:
                raise RuntimeError(f"existing rollback snapshot drift: {name}")
            continue
        staged = staged_copy(active, snap, "snapshot")
        os.replace(staged, snap)
        if sha256(snap) != before[name]["sha256"]:
            raise RuntimeError(f"rollback snapshot verification failed: {name}")


def prepare_packet(before: dict, after: dict) -> dict:
    rollback_script = PROMOTION / "rollback_local_delta.py"
    packet = {
        "status": "PREPARED_FOR_APPROVED_EXECUTION",
        "approval_phrase": f"PROMOTE LOCAL FRONTIER DELTA {RUN.name} {MANIFEST_SHA}",
        "manifest_sha256": MANIFEST_SHA,
        "apply_script": str(Path(__file__).resolve()),
        "apply_script_sha256": sha256(Path(__file__).resolve()),
        "rollback_script": str(rollback_script),
        "rollback_script_sha256": sha256(rollback_script),
        "target_count": 3,
        "targets_before": before,
        "targets_after": after,
        "rollback_snapshot": str(SNAPSHOT),
        "excluded": ["DB", "frontend", "public", "scheduler", "deploy/restart", "Git"],
        "prepared_at_utc": dt.datetime.now(dt.timezone.utc).isoformat(),
    }
    atomic_json(PROMOTION / "EXACT_DIFF.json", packet)
    atomic_json(PROMOTION / "PRE_EXECUTE.json", packet)
    return packet


def restore_snapshot(before: dict) -> None:
    staged = {
        name: staged_copy(SNAPSHOT / name, ENGINE / "delta" / name, "restore")
        for name in REPLACE_ORDER
    }
    for name in REPLACE_ORDER:
        os.replace(staged[name], ENGINE / "delta" / name)
    fsync_dir(ENGINE / "delta")
    for name in REPLACE_ORDER:
        if sha256(ENGINE / "delta" / name) != before[name]["sha256"]:
            raise RuntimeError(f"automatic rollback failed: {name}")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--prepare-only", action="store_true")
    parser.add_argument("--execute", action="store_true")
    parser.add_argument("--manifest-sha", required=True)
    parser.add_argument("--script-sha")
    args = parser.parse_args()
    if args.manifest_sha != MANIFEST_SHA:
        raise RuntimeError("approved manifest SHA does not match stored contract")
    if args.prepare_only == args.execute:
        raise RuntimeError("choose exactly one of --prepare-only or --execute")
    lock_path = ENGINE / ".frontier_pipeline.lock"
    with lock_path.open("a+") as pipeline_lock:
        fcntl.flock(pipeline_lock.fileno(), fcntl.LOCK_EX | fcntl.LOCK_NB)
        manifest, input_lock, before, after = load_contract()
        ensure_snapshot(before)
        packet = prepare_packet(before, after)
        if args.prepare_only:
            fcntl.flock(pipeline_lock.fileno(), fcntl.LOCK_UN)
            print(json.dumps(packet, indent=2, sort_keys=True))
            return 0
        actual_script_sha = sha256(Path(__file__).resolve())
        if not args.script_sha or args.script_sha != actual_script_sha:
            raise RuntimeError("apply script checksum mismatch")
        staged = {
            name: staged_copy(RUN / TARGET_MAP[name], ENGINE / "delta" / name, "promote")
            for name in REPLACE_ORDER
        }
        replaced = []
        try:
            for name in REPLACE_ORDER:
                os.replace(staged[name], ENGINE / "delta" / name)
                replaced.append(name)
            fsync_dir(ENGINE / "delta")
            for name in REPLACE_ORDER:
                active = ENGINE / "delta" / name
                if sha256(active) != after[name]["sha256"] or active.stat().st_size != after[name]["bytes"]:
                    raise RuntimeError(f"post-write checksum mismatch: {name}")
        except BaseException as exc:
            for path in staged.values():
                path.unlink(missing_ok=True)
            restore_snapshot(before)
            atomic_json(
                PROMOTION / "APPLY_RESULT.json",
                {
                    "status": "FAILED_AND_AUTOMATICALLY_ROLLED_BACK",
                    "error": repr(exc),
                    "replaced_before_failure": replaced,
                    "targets_before": before,
                },
            )
            raise
        fcntl.flock(pipeline_lock.fileno(), fcntl.LOCK_UN)
    result = {
        "status": "APPLIED_PENDING_INDEPENDENT_VERIFICATION",
        "applied_at_utc": dt.datetime.now(dt.timezone.utc).isoformat(),
        "manifest_sha256": MANIFEST_SHA,
        "apply_script_sha256": actual_script_sha,
        "replace_order": list(REPLACE_ORDER),
        "targets_before": before,
        "targets_after": after,
        "rollback_snapshot": str(SNAPSHOT),
        "canonical_other_writes": 0,
    }
    atomic_json(PROMOTION / "APPLY_RESULT.json", result)
    print(json.dumps(result, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
