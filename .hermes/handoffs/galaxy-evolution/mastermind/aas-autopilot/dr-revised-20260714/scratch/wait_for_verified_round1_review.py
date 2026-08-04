import argparse
import hashlib
import json
import time
from datetime import datetime, timedelta, timezone
from pathlib import Path

BASE = Path("/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/dr-revised-20260714")
STATE = BASE / "round1" / "dr-review-packets" / "ROUND1_DR_REVIEW_STATE.json"


def sha256(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


parser = argparse.ArgumentParser()
parser.add_argument("--paper", type=int, required=True, choices=(6, 7, 8))
parser.add_argument("--timeout-minutes", type=int, default=150)
args = parser.parse_args()
deadline = datetime.now(timezone.utc) + timedelta(minutes=args.timeout_minutes)

while datetime.now(timezone.utc) < deadline:
    payload = json.loads(STATE.read_text())
    paper = payload["papers"][args.paper - 1]
    if paper.get("status") == "completed":
        expected = {
            "packet": (Path(paper["packet_path"]), paper["packet_sha256"]),
            "metadata": (Path(paper["metadata_path"]), paper["metadata_sha256"]),
            "deletion": (Path(paper["deletion_path"]), paper["deletion_sha256"]),
        }
        checks = {
            name: {
                "path": str(path),
                "exists": path.is_file(),
                "expected_sha256": expected_hash,
                "actual_sha256": sha256(path) if path.is_file() else None,
            }
            for name, (path, expected_hash) in expected.items()
        }
        if all(row["exists"] and row["actual_sha256"] == row["expected_sha256"] for row in checks.values()):
            print(json.dumps({
                "status": "VERIFIED_COMPLETED_REVIEW_PACKET",
                "paper_id": f"paper_{args.paper:02d}",
                "checks": checks,
            }, sort_keys=True))
            raise SystemExit(0)
        raise SystemExit("Completed state has missing or mismatched packet custody")
    time.sleep(20)

print(json.dumps({"status": "WAIT_TIMEOUT", "paper_id": f"paper_{args.paper:02d}"}, sort_keys=True))
raise SystemExit(2)
