#!/usr/bin/env python3
"""Mirror weekend audit fields into the private dashboard's stable audit schema."""

import json
import os
import tempfile
import time
from pathlib import Path

ROOT = Path(__file__).resolve().parent
STATUS = ROOT / "SPRINT_STATUS.json"
LOG = ROOT / "logs" / "dashboard_audit_sync.log"
END = time.time() + 49 * 3600


def load_json(path):
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError):
        return None


def atomic_write(path, data):
    path.parent.mkdir(parents=True, exist_ok=True)
    fd, tmp_name = tempfile.mkstemp(prefix=path.name + ".", dir=str(path.parent))
    try:
        with os.fdopen(fd, "w", encoding="utf-8") as handle:
            json.dump(data, handle, indent=2, sort_keys=True)
            handle.write("\n")
        os.replace(tmp_name, path)
    finally:
        if os.path.exists(tmp_name):
            os.unlink(tmp_name)


def sync_once():
    status = load_json(STATUS)
    if not status:
        return None, False
    audit_value = status.get("latest_audit")
    if not audit_value:
        return status, False
    audit_path = Path(audit_value)
    if not audit_path.is_file() or ROOT not in audit_path.resolve().parents:
        return status, False
    audit = load_json(audit_path)
    if not audit:
        return status, False
    compile_data = audit.get("compile") or {}
    metrics = audit.get("metrics") or {}
    integrity = audit.get("integrity_blockers") or []
    expected = {
        "marker": "WEEKEND_JOURNAL_QUALITY_AUDIT_V1",
        "fatal_failures": len(integrity),
        "compile_ok": [bool(item.get("build_ok")) for item in compile_data.get("results", [])],
        "compile_results": [{"ok": bool(item.get("build_ok"))} for item in compile_data.get("results", [])],
        "figures": metrics.get("figure_count", 0),
        "figure_count": metrics.get("figure_count", 0),
    }
    changed = any(audit.get(key) != value for key, value in expected.items())
    if changed:
        audit.update(expected)
        atomic_write(audit_path, audit)
        LOG.parent.mkdir(parents=True, exist_ok=True)
        with LOG.open("a", encoding="utf-8") as handle:
            handle.write("{} synced {}\n".format(time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()), audit_path))
    return status, changed


def main():
    while time.time() < END:
        status, _ = sync_once()
        if status and status.get("state") in {"completed", "failed", "stopped"} and not (ROOT / "RUNNING.pid").exists():
            return 0
        time.sleep(15)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
