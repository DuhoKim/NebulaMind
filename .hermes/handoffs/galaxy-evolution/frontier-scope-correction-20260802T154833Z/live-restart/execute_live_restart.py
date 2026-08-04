#!/usr/bin/env python3
"""Receipt-pinned atomic Galaxy-scope Next.js build swap with verified failback."""

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

RUN = Path("/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/frontier-scope-correction-20260802T154833Z")
RESTART_ROOT = RUN / "live-restart"
LIVE_GIT_ROOT = Path("/Users/duhokim/NebulaMind/NebulaMind-origin-main-live")
LIVE_FRONTEND = LIVE_GIT_ROOT / "frontend"
ACTIVE_NEXT = LIVE_FRONTEND / ".next"
CANDIDATE_NEXT = RUN / "build-stage/frontend/.next"
ROLLBACK_NEXT = RESTART_ROOT / "rollback-live-next"
FAILED_NEW_NEXT = RESTART_ROOT / "failed-new-build"
RECEIPT = RUN / "RECEIPT.json"
PRE_RESTART = RESTART_ROOT / "PRE_RESTART.json"
RELOCATION_CANARY = RESTART_ROOT / "RELOCATION_CANARY.json"
PATCH = RUN / "REVIEW_PATCH_V5.patch"
RESULT = RESTART_ROOT / "RESTART_RESULT.json"
FAILURE = RESTART_ROOT / "RESTART_FAILURE.json"
LOCK = RESTART_ROOT / ".swap.lock"

LABEL = "com.nebulamind.frontend"
SERVICE = "gui/501/com.nebulamind.frontend"
EXPECTED_RECEIPT_SHA = "d160a85f4445f39cc05ec273d5f22d3d495d1803ee750520e864f7f36f7d014c"
EXPECTED_PRE_RESTART_SHA = "751ec350ccc95860b05b64b4d8e699c47dc6b63c3e6fed9daf59533e746414d9"
EXPECTED_RELOCATION_SHA = "b5a878d7f77c14646b72986d8c7b5f3faa78d1142eaced79bfd6a4a525c57eb7"
EXPECTED_PATCH_SHA = "889e0cf06b0e0a768706cdb14c791a363486f0884ef4a60a5ea1bd17d4624cac"
OLD_BUILD = "lFt_UDNPmeNh2DCabbYZX"
NEW_BUILD = "aNNAOJzzSRMQDzgANAtuv"
OLD_STABLE_TREE = "47f47df17986c3a4bbe582b513113787376c5b29f2c7a21bbfed1a7c410cbbd1"
NEW_RECEIPT_TREE = "c70106d85e7c41a6422e43f27596c0643c6e479035bed56595fe461b3e44b556"
NEW_STABLE_TREE = "7158c6b37af06a2d280421697cd2bd59eb068509421dac90bb44743067c176e0"
NEW_MARKERS = (
    "The most-contested core Galaxy Evolution clusters",
    "ranks only the hand-reviewed",
)
OLD_MARKER = "The top galaxy-evolution frontiers become the studies"


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def receipt_tree(root: Path) -> dict[str, object]:
    digest = hashlib.sha256()
    files = 0
    size = 0
    for path in sorted((item for item in root.rglob("*") if item.is_file()), key=lambda item: item.relative_to(root).as_posix()):
        rel = path.relative_to(root).as_posix()
        file_digest = sha256_file(path)
        digest.update(rel.encode() + b"\0" + file_digest.encode() + b"\0")
        files += 1
        size += path.stat().st_size
    return {"sha256": digest.hexdigest(), "files": files, "bytes": size}


def stable_tree(root: Path) -> dict[str, object]:
    digest = hashlib.sha256()
    files = 0
    size = 0
    for path in sorted((item for item in root.rglob("*") if item.is_file() or item.is_symlink()), key=lambda item: item.relative_to(root).as_posix()):
        rel = path.relative_to(root).as_posix()
        if rel == "cache" or rel.startswith("cache/") or rel == "trace":
            continue
        if path.is_symlink():
            kind = b"L"
            payload = os.readlink(path).encode()
        else:
            kind = b"F"
            payload = sha256_file(path).encode()
            files += 1
            size += path.stat().st_size
        digest.update(kind + b"\0" + rel.encode() + b"\0" + payload + b"\0")
    return {
        "sha256": digest.hexdigest(),
        "files": files,
        "bytes": size,
        "excluded_dynamic_paths": ["cache", "trace"],
    }


def marker_counts(root: Path) -> dict[str, int]:
    markers = NEW_MARKERS + (OLD_MARKER, "ranked study queue")
    counts = {marker: 0 for marker in markers}
    for path in root.rglob("*"):
        if not path.is_file() or path.suffix not in {".js", ".html", ".json"}:
            continue
        try:
            text = path.read_text(errors="ignore")
        except OSError:
            continue
        for marker in markers:
            counts[marker] += text.count(marker)
    return counts


def new_marker_gate(counts: dict[str, int]) -> bool:
    return all(counts[marker] > 0 for marker in NEW_MARKERS) and counts[OLD_MARKER] == 0 and counts["ranked study queue"] == 0


def old_marker_gate(counts: dict[str, int]) -> bool:
    return all(counts[marker] == 0 for marker in NEW_MARKERS) and counts[OLD_MARKER] > 0


def launchctl_pid() -> int | None:
    result = subprocess.run(["launchctl", "list", LABEL], text=True, capture_output=True, check=False)
    match = re.search(r'"PID"\s*=\s*(\d+)', result.stdout)
    return int(match.group(1)) if match else None


def listener_pid() -> int | None:
    result = subprocess.run(["lsof", "-nP", "-iTCP:3000", "-sTCP:LISTEN"], text=True, capture_output=True, check=False)
    match = re.search(r"^node\s+(\d+)\s", result.stdout, re.MULTILINE)
    return int(match.group(1)) if match else None


def process_parent(pid: int) -> int | None:
    result = subprocess.run(
        ["ps", "-o", "ppid=", "-p", str(pid)],
        text=True,
        capture_output=True,
        check=False,
    )
    value = result.stdout.strip()
    return int(value) if result.returncode == 0 and value.isdigit() else None


def port_open() -> bool:
    sock = socket.socket()
    sock.settimeout(0.5)
    try:
        return sock.connect_ex(("127.0.0.1", 3000)) == 0
    finally:
        sock.close()


def http_probe() -> dict[str, object]:
    request = Request(
        "http://127.0.0.1:3000/lab?sub=ranking",
        headers={"User-Agent": "NebulaMind-galaxy-scope-restart-verifier/1.0"},
    )
    with urlopen(request, timeout=3) as response:
        body = response.read()
        return {"status": response.status, "bytes": len(body)}


def kickstart() -> None:
    result = subprocess.run(
        ["launchctl", "kickstart", "-k", SERVICE],
        text=True,
        capture_output=True,
        check=False,
    )
    if result.returncode != 0:
        raise RuntimeError(f"launchctl kickstart failed rc={result.returncode}: {result.stderr.strip()}")


def source_guard() -> None:
    result = subprocess.run(
        ["git", "apply", "--reverse", "--check", str(PATCH)],
        cwd=LIVE_GIT_ROOT,
        text=True,
        capture_output=True,
        check=False,
    )
    if result.returncode != 0:
        raise RuntimeError(f"live V5 source reverse-check failed: {result.stderr.strip()}")


def wait_healthy(
    old_pid: int | None,
    old_listener: int | None,
    expected_build: str,
    expected_tree: str,
    *,
    new: bool,
    timeout: float = 75.0,
) -> dict[str, object]:
    deadline = time.monotonic() + timeout
    last_error = "not started"
    while time.monotonic() < deadline:
        try:
            pid = launchctl_pid()
            if pid is None or pid == old_pid:
                raise RuntimeError(f"LaunchAgent PID not replaced yet: {pid}")
            if not port_open():
                raise RuntimeError("port 3000 not listening")
            current_listener = listener_pid()
            if current_listener is None or current_listener == old_listener:
                raise RuntimeError(f"listener PID not replaced yet: {current_listener}")
            parent = process_parent(current_listener)
            if parent != pid:
                raise RuntimeError(
                    f"listener {current_listener} is not a child of LaunchAgent PID {pid}: parent={parent}"
                )
            probe = http_probe()
            if probe["status"] != 200:
                raise RuntimeError(f"HTTP status {probe['status']}")
            build = (ACTIVE_NEXT / "BUILD_ID").read_text().strip()
            if build != expected_build:
                raise RuntimeError(f"build ID {build} != {expected_build}")
            tree = stable_tree(ACTIVE_NEXT)
            if tree["sha256"] != expected_tree:
                raise RuntimeError(f"stable payload drift: {tree['sha256']} != {expected_tree}")
            counts = marker_counts(ACTIVE_NEXT)
            if new and not new_marker_gate(counts):
                raise RuntimeError(f"new marker gate failed: {counts}")
            if not new and not old_marker_gate(counts):
                raise RuntimeError(f"old marker gate failed: {counts}")
            return {
                "launchctl_pid": pid,
                "listener_pid": current_listener,
                "listener_parent_pid": parent,
                "build_id": build,
                "http": probe,
                "stable_tree": tree,
                "markers": counts,
            }
        except Exception as exc:
            last_error = str(exc)
            time.sleep(0.5)
    raise RuntimeError(f"service did not settle: {last_error}")


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
        raise SystemExit("Receipt SHA mismatch")
    if sha256_file(PRE_RESTART) != EXPECTED_PRE_RESTART_SHA:
        raise SystemExit("Pre-restart custody drift")
    if sha256_file(RELOCATION_CANARY) != EXPECTED_RELOCATION_SHA:
        raise SystemExit("Relocation-canary custody drift")
    if sha256_file(PATCH) != EXPECTED_PATCH_SHA:
        raise SystemExit("V5 patch custody drift")
    if RESULT.exists() or FAILURE.exists() or ROLLBACK_NEXT.exists() or FAILED_NEW_NEXT.exists():
        raise SystemExit("Restart/result/rollback destination already exists; refusing repeat execution")

    receipt = json.loads(RECEIPT.read_text())
    pre = json.loads(PRE_RESTART.read_text())
    relocation = json.loads(RELOCATION_CANARY.read_text())
    if receipt.get("status") != "SOURCE_APPLIED_BUILT_CANARY_VERIFIED_RESTART_REQUIRED":
        raise SystemExit("Receipt status invalid")
    if pre.get("status") != "APPROVED_RECEIPT_PINNED_RESTART_PREFLIGHT_PASS":
        raise SystemExit("Pre-restart status invalid")
    if relocation.get("status") != "RELOCATED_CANDIDATE_CANARY_VERIFIED":
        raise SystemExit("Relocation-canary status invalid")
    source_guard()
    if not ACTIVE_NEXT.is_dir() or not CANDIDATE_NEXT.is_dir():
        raise SystemExit("Active or candidate build missing")
    if (ACTIVE_NEXT / "BUILD_ID").read_text().strip() != OLD_BUILD:
        raise SystemExit("Active old build ID drift")
    if (CANDIDATE_NEXT / "BUILD_ID").read_text().strip() != NEW_BUILD:
        raise SystemExit("Candidate build ID drift")
    if receipt_tree(CANDIDATE_NEXT)["sha256"] != NEW_RECEIPT_TREE:
        raise SystemExit("Candidate receipt-tree drift")
    if stable_tree(CANDIDATE_NEXT)["sha256"] != NEW_STABLE_TREE:
        raise SystemExit("Candidate stable-tree drift")
    if stable_tree(ACTIVE_NEXT)["sha256"] != OLD_STABLE_TREE:
        raise SystemExit("Active old stable-tree drift")
    if not new_marker_gate(marker_counts(CANDIDATE_NEXT)):
        raise SystemExit("Candidate marker preflight failed")
    if not old_marker_gate(marker_counts(ACTIVE_NEXT)):
        raise SystemExit("Active old marker preflight failed")
    if not port_open() or http_probe()["status"] != 200:
        raise SystemExit("Pre-swap live service unhealthy")
    old_pid = launchctl_pid()
    old_listener = listener_pid()
    if old_pid is None or old_listener is None:
        raise SystemExit("Existing LaunchAgent/listener PID missing")
    if CANDIDATE_NEXT.stat().st_dev != ACTIVE_NEXT.stat().st_dev:
        raise SystemExit("Candidate and active builds are not on the same filesystem")

    pre_swap_active_tree = receipt_tree(ACTIVE_NEXT)
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
                os.rename(CANDIDATE_NEXT, ACTIVE_NEXT)
                swapped = True
            except Exception:
                os.rename(ROLLBACK_NEXT, ACTIVE_NEXT)
                raise
            fsync_dir(LIVE_FRONTEND)
            fsync_dir(RESTART_ROOT)
            if receipt_tree(ACTIVE_NEXT)["sha256"] != NEW_RECEIPT_TREE:
                raise RuntimeError("Post-swap candidate receipt-tree readback failed")
            if stable_tree(ACTIVE_NEXT)["sha256"] != NEW_STABLE_TREE:
                raise RuntimeError("Post-swap candidate stable-tree readback failed")
            if stable_tree(ROLLBACK_NEXT)["sha256"] != OLD_STABLE_TREE:
                raise RuntimeError("Post-swap rollback stable-tree readback failed")
            kickstart()
            health = wait_healthy(
                old_pid,
                old_listener,
                NEW_BUILD,
                NEW_STABLE_TREE,
                new=True,
            )
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
                    if (ACTIVE_NEXT / "BUILD_ID").read_text().strip() != OLD_BUILD:
                        raise RuntimeError("Failback restored the wrong build ID")
                    if stable_tree(ACTIVE_NEXT)["sha256"] != OLD_STABLE_TREE:
                        raise RuntimeError("Failback restored the wrong stable tree")
                    if not old_marker_gate(marker_counts(ACTIVE_NEXT)):
                        raise RuntimeError("Failback restored an invalid old marker set")
                    failback_prior_pid = launchctl_pid()
                    failback_prior_listener = listener_pid()
                    kickstart()
                    failback_health = wait_healthy(
                        failback_prior_pid,
                        failback_prior_listener,
                        OLD_BUILD,
                        OLD_STABLE_TREE,
                        new=False,
                    )
                except Exception as recovery_exc:
                    failback_error = str(recovery_exc)
            failure = {
                "schema_version": 1,
                "status": "SWAP_OR_RESTART_FAILED_FAILBACK_ATTEMPTED",
                "failed_at_utc": current_utc(),
                "receipt_sha256": EXPECTED_RECEIPT_SHA,
                "error": str(exc),
                "failback_error": failback_error,
                "failback_health": failback_health,
                "safety_ledger": {
                    "runtime_build_swaps_attempted": 1,
                    "frontend_service_restarts_attempted": 1,
                    "source_writes": 0,
                    "git_writes": 0,
                    "db_writes": 0,
                    "scheduler_writes": 0,
                    "cockpit_writes": 0,
                },
            }
            atomic_json(FAILURE, failure)
            raise SystemExit(json.dumps(failure, sort_keys=True)) from exc

        result = {
            "schema_version": 1,
            "status": "LIVE_BUILD_SWAPPED_RESTARTED_AND_LOCALLY_VERIFIED",
            "completed_at_utc": current_utc(),
            "approval": "APPROVE GALAXY SCOPE LIVE BUILD-SWAP RESTART",
            "receipt_sha256": EXPECTED_RECEIPT_SHA,
            "pre_restart_sha256": EXPECTED_PRE_RESTART_SHA,
            "relocation_canary_sha256": EXPECTED_RELOCATION_SHA,
            "execute_script_sha256": sha256_file(Path(__file__)),
            "service": {
                "label": LABEL,
                "domain": SERVICE,
                "old_launchctl_pid": old_pid,
                "new_launchctl_pid": health["launchctl_pid"],
                "old_listener_pid": old_listener,
                "new_listener_pid": health["listener_pid"],
                "port": 3000,
                "restart_elapsed_seconds": elapsed,
            },
            "build": {
                "old_build_id": OLD_BUILD,
                "new_build_id": NEW_BUILD,
                "pre_swap_active_receipt_tree": pre_swap_active_tree,
                "active_stable_tree": stable_tree(ACTIVE_NEXT),
                "rollback_stable_tree": stable_tree(ROLLBACK_NEXT),
                "active_receipt_tree_after_health": receipt_tree(ACTIVE_NEXT),
                "rollback_receipt_tree_after_health": receipt_tree(ROLLBACK_NEXT),
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
                "source_writes": 0,
                "db_writes": 0,
                "git_writes": 0,
                "cockpit_writes": 0,
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
