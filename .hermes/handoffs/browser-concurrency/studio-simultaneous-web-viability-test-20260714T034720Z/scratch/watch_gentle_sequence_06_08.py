import json
import time
from datetime import datetime, timedelta, timezone
from pathlib import Path

STATE = Path("/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/dr-revised-20260714/round1/dr-review-packets/ROUND1_GENTLE_AUTO_06_08_STATE.json")
TERMINAL = {
    "COMPLETE_HOLD_AFTER_PAPER08",
    "CHALLENGE_STOP_FROZEN",
    "FIRST_UNACCEPTED_STOP_NO_RETRY",
    "TECHNICAL_OR_CUSTODY_HOLD",
    "UNEXPECTED_HOLD",
}
DEADLINE = datetime.now(timezone.utc) + timedelta(hours=4)

while datetime.now(timezone.utc) < DEADLINE:
    if STATE.is_file():
        payload = json.loads(STATE.read_text())
        if payload.get("status") in TERMINAL:
            print(json.dumps(payload, sort_keys=True))
            raise SystemExit(0)
    time.sleep(30)

print(json.dumps({"status": "WATCH_TIMEOUT", "state_path": str(STATE)}, sort_keys=True))
raise SystemExit(2)
