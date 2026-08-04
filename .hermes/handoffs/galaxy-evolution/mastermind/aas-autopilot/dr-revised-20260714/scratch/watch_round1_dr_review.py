import json
import sys
import time
from datetime import datetime
from pathlib import Path
from zoneinfo import ZoneInfo

STATE = Path("/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/dr-revised-20260714/round1/dr-review-packets/ROUND1_DR_REVIEW_STATE.json")
HARD_STOP = datetime(2026, 7, 15, 10, 0, 0, tzinfo=ZoneInfo("Asia/Seoul"))
TERMINAL = {"completed", "failed", "stopped_challenge", "not_run_global_freeze", "not_run_target_blocked"}
last = None
while True:
    now = datetime.now(ZoneInfo("Asia/Seoul"))
    if now >= HARD_STOP:
        print(json.dumps({"status": "HARD_STOP_REACHED", "kst": now.isoformat(), "state_exists": STATE.exists()}, sort_keys=True), flush=True)
        raise SystemExit(3)
    if STATE.exists():
        state = json.loads(STATE.read_text())
        statuses = [(row["paper_id"], row.get("status", "unknown")) for row in state["papers"]]
        if statuses != last:
            print(json.dumps({"kst": now.isoformat(), "statuses": statuses}, sort_keys=True), flush=True)
            last = statuses
        if all(status in TERMINAL for _, status in statuses):
            completed = sum(status == "completed" for _, status in statuses)
            print(json.dumps({"status": "ROUND1_DR_REVIEW_TERMINAL", "completed": completed, "statuses": statuses, "state": str(STATE)}, sort_keys=True), flush=True)
            raise SystemExit(0 if completed == 9 else 2)
    time.sleep(30)
