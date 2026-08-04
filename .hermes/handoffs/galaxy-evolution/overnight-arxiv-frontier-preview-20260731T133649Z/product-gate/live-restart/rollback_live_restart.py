#!/usr/bin/env python3
"""Rollback the approved live Next.js build swap; requires a fresh receipt-pinned gate."""

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
RUN = ROOT / ".hermes/handoffs/galaxy-evolution/overnight-arxiv-frontier-preview-20260731T133649Z"
RESTART_ROOT = RUN / "product-gate/live-restart"
LIVE_FRONTEND = Path("/Users/duhokim/NebulaMind/NebulaMind-origin-main-live/frontend")
ACTIVE = LIVE_FRONTEND / ".next"
ROLLBACK = RESTART_ROOT / "rollback-live-next"
ROLLED_BACK_NEW = RESTART_ROOT / "rolled-back-new-build"
RESTART_RESULT = RESTART_ROOT / "RESTART_RESULT.json"
LIVE_RECEIPT = RESTART_ROOT / "LIVE_RESTART_RECEIPT.json"
ROLLBACK_RESULT = RESTART_ROOT / "ROLLBACK_RESULT.json"
LOCK = RESTART_ROOT / ".swap.lock"
LABEL = "com.nebulamind.frontend"
SERVICE = "gui/501/com.nebulamind.frontend"
NEW_BUILD = "lFt_UDNPmeNh2DCabbYZX"
OLD_BUILD = "t-iRxR98ZKuZzWRYYpD8z"
NEW_TREE = "9769977e67874e6580be528e73efe552117c6ba36e2c0ab708fed96cf70dae27"
OLD_TREE = "56793412501c772ebba48c8e5536aca2742db2e9ee2f379471967b209d984333"


def sha(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()


def tree(root: Path) -> str:
    h = hashlib.sha256()
    for path in sorted(root.rglob("*"), key=lambda p: str(p.relative_to(root))):
        rel = str(path.relative_to(root))
        if rel == "cache" or rel.startswith("cache/"):
            continue
        if path.is_symlink():
            payload = os.readlink(path).encode()
            kind = b"L"
        elif path.is_file():
            payload = sha(path).encode()
            kind = b"F"
        else:
            continue
        h.update(kind + b"\0" + rel.encode() + b"\0" + payload + b"\0")
    return h.hexdigest()


def pid() -> int | None:
    result = subprocess.run(["launchctl", "list", LABEL], text=True, capture_output=True, check=False)
    match = re.search(r'"PID"\s*=\s*(\d+)', result.stdout)
    return int(match.group(1)) if match else None


def kickstart() -> None:
    result = subprocess.run(["launchctl", "kickstart", "-k", SERVICE], text=True, capture_output=True, check=False)
    if result.returncode:
        raise RuntimeError(f"kickstart failed rc={result.returncode}: {result.stderr.strip()}")


def probe() -> int:
    req = Request("http://127.0.0.1:3000/lab", headers={"User-Agent": "NebulaMind-rollback-verifier/1.0"})
    with urlopen(req, timeout=3) as response:
        response.read()
        return response.status


def port_open() -> bool:
    s = socket.socket(); s.settimeout(0.5)
    try:
        return s.connect_ex(("127.0.0.1", 3000)) == 0
    finally:
        s.close()


def wait_build(expected: str, prior_pid: int | None, timeout: float = 75.0) -> dict[str, object]:
    deadline = time.monotonic() + timeout
    last = "not started"
    while time.monotonic() < deadline:
        try:
            current_pid = pid()
            if current_pid is None or current_pid == prior_pid:
                raise RuntimeError(f"PID not replaced: {current_pid}")
            if not port_open() or probe() != 200:
                raise RuntimeError("HTTP/port health failed")
            build = (ACTIVE / "BUILD_ID").read_text().strip()
            if build != expected:
                raise RuntimeError(f"build mismatch: {build}")
            return {"pid": current_pid, "build_id": build, "http_status": 200}
        except Exception as exc:
            last = str(exc); time.sleep(0.5)
    raise RuntimeError(f"service did not settle: {last}")


def atomic_json(path: Path, data: dict[str, object]) -> None:
    fd, name = tempfile.mkstemp(prefix=f".{path.name}.", dir=path.parent)
    tmp = Path(name)
    try:
        with os.fdopen(fd, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=2, sort_keys=True); f.write("\n"); f.flush(); os.fsync(f.fileno())
        os.replace(tmp, path)
    finally:
        if tmp.exists(): tmp.unlink()


def now() -> str:
    return subprocess.run(["date", "-u", "+%Y-%m-%dT%H:%M:%SZ"], text=True, capture_output=True, check=True).stdout.strip()


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--execute", action="store_true")
    parser.add_argument("--live-receipt-sha", required=True)
    args = parser.parse_args()
    if not args.execute:
        raise SystemExit("Refusing runtime rollback without --execute")
    if not LIVE_RECEIPT.is_file() or sha(LIVE_RECEIPT) != args.live_receipt_sha:
        raise SystemExit("Live restart receipt SHA mismatch")
    receipt = json.loads(LIVE_RECEIPT.read_text())
    if receipt.get("status") != "LIVE_BUILD_SWAP_RESTART_PUBLICLY_VERIFIED":
        raise SystemExit("Live restart receipt status invalid")
    restart = json.loads(RESTART_RESULT.read_text())
    if receipt.get("restart_result_sha256") != sha(RESTART_RESULT):
        raise SystemExit("Restart-result custody mismatch")
    if ROLLBACK_RESULT.exists() or ROLLED_BACK_NEW.exists():
        raise SystemExit("Rollback already attempted or destination occupied")
    if not ACTIVE.is_dir() or not ROLLBACK.is_dir():
        raise SystemExit("Active or rollback build missing")
    if (ACTIVE / "BUILD_ID").read_text().strip() != NEW_BUILD or tree(ACTIVE) != NEW_TREE:
        raise SystemExit("Active new build drift")
    if (ROLLBACK / "BUILD_ID").read_text().strip() != OLD_BUILD or tree(ROLLBACK) != OLD_TREE:
        raise SystemExit("Rollback old build drift")
    if probe() != 200:
        raise SystemExit("Live service unhealthy before rollback")
    lock = LOCK.open("a+")
    prior = pid()
    try:
        fcntl.flock(lock.fileno(), fcntl.LOCK_EX | fcntl.LOCK_NB)
        os.rename(ACTIVE, ROLLED_BACK_NEW)
        try:
            os.rename(ROLLBACK, ACTIVE)
        except Exception:
            os.rename(ROLLED_BACK_NEW, ACTIVE)
            raise
        try:
            kickstart()
            health = wait_build(OLD_BUILD, prior)
        except Exception as exc:
            restore_error = None
            try:
                os.rename(ACTIVE, ROLLBACK)
                os.rename(ROLLED_BACK_NEW, ACTIVE)
                restore_prior_pid = pid()
                kickstart()
                restore_health = wait_build(NEW_BUILD, restore_prior_pid)
            except Exception as recovery:
                restore_error = str(recovery); restore_health = None
            raise SystemExit(json.dumps({"status": "ROLLBACK_FAILED_NEW_BUILD_RESTORE_ATTEMPTED", "error": str(exc), "restore_error": restore_error, "restore_health": restore_health}, sort_keys=True)) from exc
        result = {"schema_version": 1, "status": "LIVE_RUNTIME_ROLLED_BACK_TO_PRIOR_BUILD", "completed_at_utc": now(), "live_restart_receipt_sha256": args.live_receipt_sha, "old_active_build_id": NEW_BUILD, "restored_build_id": OLD_BUILD, "health": health, "safety_ledger": {"runtime_build_swaps": 1, "existing_frontend_service_restarts": 1, "source_writes": 0, "git_writes": 0, "db_writes": 0, "scheduler_definition_writes": 0}}
        atomic_json(ROLLBACK_RESULT, result)
        print(json.dumps(result, indent=2, sort_keys=True))
        return 0
    finally:
        try: fcntl.flock(lock.fileno(), fcntl.LOCK_UN)
        finally: lock.close()


if __name__ == "__main__":
    raise SystemExit(main())
