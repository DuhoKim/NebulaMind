#!/usr/bin/env python3
"""Atomic live Next.js build swap with verified failback."""

from __future__ import annotations

import argparse
import fcntl
import hashlib
import json
import os
import re
import socket
import subprocess
import tempfile
import time
from pathlib import Path
from urllib.request import Request, urlopen

ROOT = Path("/Users/duhokim/NebulaMind/NebulaMind")
LIVE_FRONTEND = Path("/Users/duhokim/NebulaMind/NebulaMind-origin-main-live/frontend")
RUN = ROOT / ".hermes/handoffs/galaxy-evolution/overnight-arxiv-frontier-preview-20260731T133649Z"
PRODUCT_GATE = RUN / "product-gate"
RESTART_ROOT = PRODUCT_GATE / "live-restart"
RECEIPT = PRODUCT_GATE / "GATE_C_RECEIPT.json"
PRE_RESTART = RESTART_ROOT / "PRE_RESTART.json"
BUILD_RESULT = RESTART_ROOT / "BUILD_RESULT.json"
STAGED_NEXT = RESTART_ROOT / "build-stage/frontend/.next"
ACTIVE_NEXT = LIVE_FRONTEND / ".next"
ROLLBACK_NEXT = RESTART_ROOT / "rollback-live-next"
FAILED_NEW_NEXT = RESTART_ROOT / "failed-new-build"
RESULT = RESTART_ROOT / "RESTART_RESULT.json"
LOCK = RESTART_ROOT / ".swap.lock"
SERVICE = "gui/501/com.nebulamind.frontend"
LABEL = "com.nebulamind.frontend"
EXPECTED_RECEIPT_SHA = "bfd9218df587c2ef7aaa92208c3925ad60c058dbbbd6a9c0a36f24adc66b3b88"
EXPECTED_PRE_RESTART_SHA = "8de841f90ac9aa4a2a13801c7de5c44d331ce59bab0834a0d89a866ea7e222cd"
EXPECTED_SOURCE_SHA = "08ec69b7b059dc9c0ed1bc1311f9253d092c8ec314e684c149a1e13f3882dc36"
NEW_MARKERS = ("1316 papers", "674 papers")
OLD_MARKERS = ("1306 papers", "661 papers")


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def tree_fingerprint(root: Path) -> dict[str, object]:
    digest = hashlib.sha256()
    files = 0
    size = 0
    for path in sorted(root.rglob("*"), key=lambda item: str(item.relative_to(root))):
        rel = str(path.relative_to(root))
        if rel == "cache" or rel.startswith("cache/"):
            continue
        if path.is_symlink():
            payload = os.readlink(path).encode()
            kind = b"L"
        elif path.is_file():
            file_digest = hashlib.sha256()
            count = 0
            with path.open("rb") as handle:
                for chunk in iter(lambda: handle.read(1024 * 1024), b""):
                    file_digest.update(chunk)
                    count += len(chunk)
            payload = file_digest.hexdigest().encode()
            kind = b"F"
            files += 1
            size += count
        else:
            continue
        digest.update(kind + b"\0" + rel.encode() + b"\0" + payload + b"\0")
    return {"sha256": digest.hexdigest(), "files": files, "bytes": size, "cache_excluded": True}


def marker_counts(root: Path) -> dict[str, int]:
    markers = NEW_MARKERS + OLD_MARKERS
    counts = {marker: 0 for marker in markers}
    for path in root.rglob("*.js"):
        try:
            text = path.read_text(errors="ignore")
        except OSError:
            continue
        for marker in markers:
            counts[marker] += text.count(marker)
    return counts


def marker_gate(counts: dict[str, int], *, new: bool) -> bool:
    if new:
        return all(counts[item] > 0 for item in NEW_MARKERS) and all(
            counts[item] == 0 for item in OLD_MARKERS
        )
    return all(counts[item] == 0 for item in NEW_MARKERS) and all(
        counts[item] > 0 for item in OLD_MARKERS
    )


def launchctl_pid() -> int | None:
    result = subprocess.run(
        ["launchctl", "list", LABEL], text=True, capture_output=True, check=False
    )
    match = re.search(r'"PID"\s*=\s*(\d+)', result.stdout)
    return int(match.group(1)) if match else None


def kickstart() -> None:
    result = subprocess.run(
        ["launchctl", "kickstart", "-k", SERVICE],
        text=True,
        capture_output=True,
        check=False,
    )
    if result.returncode != 0:
        raise RuntimeError(
            f"launchctl kickstart failed rc={result.returncode}: {result.stderr.strip()}"
        )


def http_probe() -> dict[str, object]:
    request = Request("http://127.0.0.1:3000/lab", headers={"User-Agent": "NebulaMind-restart-verifier/1.0"})
    with urlopen(request, timeout=3) as response:
        body = response.read()
        return {"status": response.status, "bytes": len(body)}


def port_open() -> bool:
    sock = socket.socket()
    sock.settimeout(0.5)
    try:
        return sock.connect_ex(("127.0.0.1", 3000)) == 0
    finally:
        sock.close()


def wait_healthy(old_pid: int | None, expected_build: str, timeout: float = 75.0) -> dict[str, object]:
    deadline = time.monotonic() + timeout
    last_error = "not started"
    while time.monotonic() < deadline:
        try:
            pid = launchctl_pid()
            if pid is None or pid == old_pid:
                raise RuntimeError(f"PID not replaced yet: {pid}")
            if not port_open():
                raise RuntimeError("port 3000 not listening")
            probe = http_probe()
            if probe["status"] != 200:
                raise RuntimeError(f"HTTP status {probe['status']}")
            build = (ACTIVE_NEXT / "BUILD_ID").read_text().strip()
            if build != expected_build:
                raise RuntimeError(f"build ID {build} != {expected_build}")
            counts = marker_counts(ACTIVE_NEXT)
            if not marker_gate(counts, new=True):
                raise RuntimeError(f"new marker gate failed: {counts}")
            return {"pid": pid, "build_id": build, "http": probe, "markers": counts}
        except Exception as exc:  # bounded settlement loop
            last_error = str(exc)
            time.sleep(0.5)
    raise RuntimeError(f"service did not settle: {last_error}")


def wait_old_healthy(expected_build: str, timeout: float = 75.0) -> dict[str, object]:
    deadline = time.monotonic() + timeout
    last_error = "not started"
    while time.monotonic() < deadline:
        try:
            pid = launchctl_pid()
            if pid is None or not port_open():
                raise RuntimeError("old service not listening")
            probe = http_probe()
            build = (ACTIVE_NEXT / "BUILD_ID").read_text().strip()
            counts = marker_counts(ACTIVE_NEXT)
            if probe["status"] != 200 or build != expected_build or not marker_gate(counts, new=False):
                raise RuntimeError(f"old health mismatch build={build} markers={counts}")
            return {"pid": pid, "build_id": build, "http": probe, "markers": counts}
        except Exception as exc:
            last_error = str(exc)
            time.sleep(0.5)
    raise RuntimeError(f"old build failback did not settle: {last_error}")


def fsync_dir(path: Path) -> None:
    descriptor = os.open(path, os.O_RDONLY)
    try:
        os.fsync(descriptor)
    finally:
        os.close(descriptor)


def atomic_json(path: Path, value: dict[str, object]) -> None:
    descriptor, name = tempfile.mkstemp(prefix=f".{path.name}.", dir=path.parent)
    temp = Path(name)
    try:
        with os.fdopen(descriptor, "w", encoding="utf-8") as handle:
            json.dump(value, handle, indent=2, sort_keys=True)
            handle.write("\n")
            handle.flush()
            os.fsync(handle.fileno())
        os.replace(temp, path)
        fsync_dir(path.parent)
    finally:
        if temp.exists():
            temp.unlink()


def current_utc() -> str:
    return subprocess.run(
        ["date", "-u", "+%Y-%m-%dT%H:%M:%SZ"],
        text=True,
        capture_output=True,
        check=True,
    ).stdout.strip()


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--execute", action="store_true")
    parser.add_argument("--receipt-sha", required=True)
    args = parser.parse_args()
    if not args.execute:
        raise SystemExit("Refusing build swap/restart without --execute")
    if args.receipt_sha != EXPECTED_RECEIPT_SHA or sha256_file(RECEIPT) != EXPECTED_RECEIPT_SHA:
        raise SystemExit("Gate C receipt SHA mismatch")
    if sha256_file(PRE_RESTART) != EXPECTED_PRE_RESTART_SHA:
        raise SystemExit("Pre-restart custody drift")
    if RESULT.exists() or ROLLBACK_NEXT.exists() or FAILED_NEW_NEXT.exists():
        raise SystemExit("Restart/result/rollback path already exists; refusing second execution")
    if sha256_file(LIVE_FRONTEND / "src/app/lab/frontiersData.ts") != EXPECTED_SOURCE_SHA:
        raise SystemExit("Live ranking source drift")
    receipt = json.loads(RECEIPT.read_text())
    build_result = json.loads(BUILD_RESULT.read_text())
    if receipt.get("status") != "SOURCE_APPLIED_BUILD_VERIFIED_AWAITING_RESTART_GATE":
        raise SystemExit("Gate C receipt status invalid")
    if build_result.get("status") != "ISOLATED_LIVE_SOURCE_BUILD_AND_RELOCATION_CANARY_VERIFIED":
        raise SystemExit("Build/canary status invalid")
    if not STAGED_NEXT.is_dir() or not ACTIVE_NEXT.is_dir():
        raise SystemExit("Staged or active build missing")
    new_build = (STAGED_NEXT / "BUILD_ID").read_text().strip()
    old_build = (ACTIVE_NEXT / "BUILD_ID").read_text().strip()
    if new_build != build_result["build"]["build_id"]:
        raise SystemExit("Staged build ID drift")
    if old_build != build_result["active_old_build"]["build_id"]:
        raise SystemExit("Active old build ID drift")
    if tree_fingerprint(STAGED_NEXT) != build_result["build"]["payload_tree"]:
        raise SystemExit("Staged build payload drift")
    if tree_fingerprint(ACTIVE_NEXT) != build_result["active_old_build"]["payload_tree"]:
        raise SystemExit("Active old build payload drift")
    if not marker_gate(marker_counts(STAGED_NEXT), new=True):
        raise SystemExit("Staged marker preflight failed")
    if not marker_gate(marker_counts(ACTIVE_NEXT), new=False):
        raise SystemExit("Active old marker preflight failed")
    if not port_open() or http_probe()["status"] != 200:
        raise SystemExit("Pre-swap live service is unhealthy")
    old_pid = launchctl_pid()
    if old_pid is None:
        raise SystemExit("Existing LaunchAgent PID missing")
    if STAGED_NEXT.stat().st_dev != ACTIVE_NEXT.stat().st_dev:
        raise SystemExit("Staged and active builds are not on the same filesystem")

    LOCK.parent.mkdir(parents=True, exist_ok=True)
    lock_handle = LOCK.open("a+")
    swapped = False
    try:
        try:
            fcntl.flock(lock_handle.fileno(), fcntl.LOCK_EX | fcntl.LOCK_NB)
        except BlockingIOError as exc:
            raise SystemExit("Restart lock is busy") from exc
        if ROLLBACK_NEXT.exists() or FAILED_NEW_NEXT.exists():
            raise SystemExit("Rollback/failure destination appeared after lock acquisition")
        started = time.monotonic()
        try:
            os.rename(ACTIVE_NEXT, ROLLBACK_NEXT)
            try:
                os.rename(STAGED_NEXT, ACTIVE_NEXT)
            except Exception:
                os.rename(ROLLBACK_NEXT, ACTIVE_NEXT)
                raise
            fsync_dir(LIVE_FRONTEND)
            fsync_dir(RESTART_ROOT)
            swapped = True
            if tree_fingerprint(ACTIVE_NEXT) != build_result["build"]["payload_tree"]:
                raise RuntimeError("Post-swap new payload readback failed")
            if tree_fingerprint(ROLLBACK_NEXT) != build_result["active_old_build"]["payload_tree"]:
                raise RuntimeError("Post-swap rollback payload readback failed")
            kickstart()
            health = wait_healthy(old_pid, new_build)
            elapsed = round(time.monotonic() - started, 3)
        except Exception as exc:
            failback_error = None
            failback_health = None
            if swapped:
                try:
                    if FAILED_NEW_NEXT.exists():
                        raise RuntimeError("failed-new destination already exists")
                    os.rename(ACTIVE_NEXT, FAILED_NEW_NEXT)
                    os.rename(ROLLBACK_NEXT, ACTIVE_NEXT)
                    fsync_dir(LIVE_FRONTEND)
                    fsync_dir(RESTART_ROOT)
                    kickstart()
                    failback_health = wait_old_healthy(old_build)
                except Exception as recovery_exc:
                    failback_error = str(recovery_exc)
            raise SystemExit(
                json.dumps(
                    {
                        "status": "SWAP_OR_RESTART_FAILED_FAILBACK_ATTEMPTED",
                        "error": str(exc),
                        "failback_error": failback_error,
                        "failback_health": failback_health,
                    },
                    sort_keys=True,
                )
            ) from exc
        result = {
            "schema_version": 1,
            "status": "LIVE_BUILD_SWAPPED_RESTARTED_AND_LOCALLY_VERIFIED",
            "completed_at_utc": current_utc(),
            "gate_c_receipt_sha256": EXPECTED_RECEIPT_SHA,
            "service": {
                "label": LABEL,
                "domain": SERVICE,
                "old_pid": old_pid,
                "new_pid": health["pid"],
                "port": 3000,
                "restart_elapsed_seconds": elapsed,
            },
            "build": {
                "old_build_id": old_build,
                "new_build_id": new_build,
                "active_payload": tree_fingerprint(ACTIVE_NEXT),
                "rollback_payload": tree_fingerprint(ROLLBACK_NEXT),
            },
            "health": health,
            "paths": {
                "active_next": str(ACTIVE_NEXT),
                "rollback_next": str(ROLLBACK_NEXT),
            },
            "safety_ledger": {
                "live_build_swaps": 1,
                "existing_frontend_service_restarts": 1,
                "launchagent_plist_writes": 0,
                "new_services_or_schedulers": 0,
                "db_sql_api_writes": 0,
                "git_index_history_writes": 0,
                "cockpit_writes": 0,
                "curated_topic_writes": 0,
                "paper_merit_writes": 0,
                "unrelated_service_restarts": 0,
                "external_submissions": 0,
            },
        }
        atomic_json(RESULT, result)
        print(json.dumps(result, indent=2, sort_keys=True))
        return 0
    finally:
        try:
            fcntl.flock(lock_handle.fileno(), fcntl.LOCK_UN)
        finally:
            lock_handle.close()


if __name__ == "__main__":
    raise SystemExit(main())
