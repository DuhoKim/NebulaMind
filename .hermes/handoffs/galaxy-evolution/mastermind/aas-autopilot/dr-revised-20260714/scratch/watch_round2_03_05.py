import hashlib
import json
import time
from datetime import datetime, timedelta, timezone
from pathlib import Path

BASE = Path("/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/dr-revised-20260714")
DEADLINE = datetime.now(timezone.utc) + timedelta(hours=1)

while datetime.now(timezone.utc) < DEADLINE:
    rows = []
    complete = True
    for number in (3, 4, 5):
        tex = BASE / "round2" / f"paper_{number:02d}_r2.tex"
        source = BASE / "round2" / "receipts" / f"paper_{number:02d}_sources.json"
        revision = BASE / "round2" / "receipts" / f"paper_{number:02d}_revision.md"
        present = tex.is_file() and source.is_file() and revision.is_file()
        complete = complete and present
        rows.append({
            "paper": number,
            "complete_artifacts_present": present,
            "tex_sha256": hashlib.sha256(tex.read_bytes()).hexdigest() if tex.is_file() else None,
        })
    if complete:
        print(json.dumps({"status": "ROUND2_03_05_ARTIFACTS_PRESENT", "papers": rows}, sort_keys=True))
        raise SystemExit(0)
    time.sleep(20)

print(json.dumps({"status": "ROUND2_03_05_WATCH_TIMEOUT"}, sort_keys=True))
raise SystemExit(2)
