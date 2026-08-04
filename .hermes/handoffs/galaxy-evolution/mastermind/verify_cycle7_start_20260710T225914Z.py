#!/usr/bin/env python3
import json
import os
import subprocess
import sys
import time
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parent
STATUS = ROOT / "aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_WEEKEND_48H_20260710T110009Z/SPRINT_STATUS.json"
CANDIDATE = ROOT / "aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_WEEKEND_48H_20260710T110009Z/candidates/cycle_07_package"
RECEIPT = ROOT / "TORI_CYCLE7_START_VERIFICATION_20260710T225914Z.json"
DEADLINE = time.time() + 5400
last_status = {}


def finish(payload: dict, code: int) -> None:
    payload["observed_utc"] = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    RECEIPT.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps(payload, sort_keys=True), flush=True)
    raise SystemExit(code)


while time.time() < DEADLINE:
    try:
        last_status = json.loads(STATUS.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError):
        time.sleep(15)
        continue

    pid = int(last_status.get("pid") or 0)
    alive = pid > 0 and subprocess.run(
        ["kill", "-0", str(pid)], capture_output=True, check=False
    ).returncode == 0
    if not alive:
        finish({"verified": False, "reason": "runner_not_alive", "status": last_status}, 2)

    if (
        int(last_status.get("cycle") or 0) >= 7
        and last_status.get("phase") == "introduction"
        and last_status.get("state") == "running"
        and CANDIDATE.is_dir()
    ):
        finish(
            {
                "verified": True,
                "cycle": last_status.get("cycle"),
                "phase": last_status.get("phase"),
                "state": last_status.get("state"),
                "current_lane": last_status.get("current_lane"),
                "candidate_exists": True,
                "runner_pid": pid,
            },
            0,
        )
    time.sleep(15)

finish({"verified": False, "reason": "timeout", "last_status": last_status}, 3)
