import hashlib
import json
import sys
from pathlib import Path

sys.path.insert(0, "scratch")
import dr_batch_9_reference_runner as r
from playwright.sync_api import sync_playwright

AUTH = Path("receipts/DUHO_RESET_RESUME_BATCH9.md")
RELEASE_RECEIPT = r.PACKET_DIR / "DR_RESEARCH_BATCH_9_ACCOUNT_RAIL_RELEASE.json"
EXPECTED_AUTH_MARKER = "DUHO_RESET_RESUME_BATCH9_20260714"
EXPECTED_RESET_EPOCH = 1574
EXPECTED_RESET_SHA256 = "d2250577ad0c120396b468698eca3d11f633ca4946e54e0eebfcae89b22abe8c"
EXPECTED_CONVERSATION_ID = "c41e8761b6e1ad6e"


def sha_file(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def verify_reset_gate(state):
    if EXPECTED_AUTH_MARKER not in AUTH.read_text():
        raise r.GlobalChallengeStop("direct reset authorization marker missing")
    ok, message = r.ledger.verify(r.LEDGER_PATH)
    if not ok:
        raise r.GlobalChallengeStop(f"ledger invalid at resume: {message}")
    entries = r.ledger.read_entries(r.LEDGER_PATH)
    reset = next((entry for entry in entries if entry["epoch"] == EXPECTED_RESET_EPOCH), None)
    if not reset or reset["actor"] != "broker" or reset["type"] != "frozen_reset" or reset["entry_sha256"] != EXPECTED_RESET_SHA256:
        raise r.GlobalChallengeStop("broker-authored reset receipt mismatch")
    if any(entry["type"] == "emergency_stop" for entry in entries[EXPECTED_RESET_EPOCH + 1:]):
        raise r.GlobalChallengeStop("later emergency stop supersedes reset")
    live = json.loads(Path("broker/live_state.json").read_text())
    if live.get("frozen"):
        raise r.GlobalChallengeStop("runtime broker remains frozen")
    live_leases = [lease for lease in live["leases"].values() if lease["state"] == "live"]
    conflicting = [
        lease for lease in live_leases
        if lease["kind"] == "account-submission"
        or (
            lease["kind"] == "target"
            and lease.get("scope", {}).get("host_id") == r.SCOPE["host_id"]
            and lease.get("scope", {}).get("target_id") == r.SCOPE["target_id"]
        )
    ]
    if conflicting:
        raise r.GlobalChallengeStop(f"conflicting live leases before paper_09 resume: {conflicting}")
    paper = state["papers"][8]
    if paper.get("status") not in {"submitted", "researching"} or paper.get("identity", {}).get("conversation_id") != EXPECTED_CONVERSATION_ID:
        raise r.GlobalChallengeStop("paper_09 durable resume identity/status mismatch")
    return reset, message


def verify_all(state):
    entries = r.ledger.read_entries(r.LEDGER_PATH)
    by_epoch = {entry["epoch"]: entry for entry in entries}
    rows = []
    for paper in state["papers"]:
        packet = Path(paper["packet_path"])
        metadata = Path(paper["metadata_path"])
        deletion = Path(paper["deletion_path"])
        row = {
            "paper_id": paper["paper_id"],
            "status": paper["status"],
            "source_anchor_count": paper["result"]["source_anchor_count"],
            "packet_sha256": sha_file(packet),
            "metadata_sha256": sha_file(metadata),
            "deletion_sha256": sha_file(deletion),
            "save_epoch": paper["save_ledger"]["epoch"],
            "delete_epoch": paper["delete_ledger"]["epoch"],
        }
        row["verified"] = (
            row["status"] == "completed"
            and row["packet_sha256"] == paper["packet_sha256"]
            and row["metadata_sha256"] == paper["metadata_sha256"]
            and row["deletion_sha256"] == paper["deletion_sha256"]
            and by_epoch.get(row["save_epoch"], {}).get("entry_sha256") == paper["save_ledger"]["entry_sha256"]
            and by_epoch.get(row["delete_epoch"], {}).get("entry_sha256") == paper["delete_ledger"]["entry_sha256"]
        )
        rows.append(row)
    ok, message = r.ledger.verify(r.LEDGER_PATH)
    return rows, ok, message


def main():
    state = json.loads(r.STATE_PATH.read_text())
    reset, reset_verify = verify_reset_gate(state)
    if r.SUMMARY_PATH.exists() or RELEASE_RECEIPT.exists():
        raise r.GlobalChallengeStop("verified final/release receipt path already exists")
    buffered_reports = []
    r.report_hwao = buffered_reports.append
    state["safety_hold"] = {
        "active": False,
        "cleared_by": "broker-authored frozen_reset",
        "authorization_path": str(AUTH.resolve()),
        "authorization_sha256": sha_file(AUTH),
        "reset_epoch": reset["epoch"],
        "reset_entry_sha256": reset["entry_sha256"],
        "ledger_verify_at_resume": reset_verify,
        "paper_09_resume_point": "accepted exact plan; resume at Start research without prompt resubmit",
        "cleared_utc": r.utcnow(),
    }
    r.save_state(state)
    with sync_playwright() as playwright:
        browser = playwright.chromium.connect_over_cdp(r.BASE)
        outcome = r.run_one(r.discover_prompts()[8], state, browser)
    if outcome != "completed" or state["papers"][8]["status"] != "completed":
        raise r.GlobalChallengeStop(f"paper_09 did not complete: {outcome}")

    live = json.loads(Path("broker/live_state.json").read_text())
    paper9 = state["papers"][8]
    start_lease_id = paper9["research_start_account_lease_id"]
    start_lease = live["leases"].get(start_lease_id)
    live_account = [
        {"lease_id": lease["lease_id"], "holder": lease["holder"]}
        for lease in live["leases"].values()
        if lease["kind"] == "account-submission" and lease["state"] == "live"
    ]
    if not start_lease or start_lease["kind"] != "account-submission" or start_lease["state"] != "released":
        raise r.GlobalChallengeStop("paper_09 Start-research account lease not released")
    release = {
        "batch_id": state["batch_id"],
        "paper_id": "paper_09",
        "reference_only": True,
        "advisory_only": True,
        "released_utc": r.utcnow(),
        "paper_09_prompt_submit_lease_id": paper9["identity"]["submit_account_lease_id"],
        "paper_09_research_start_lease_id": start_lease_id,
        "paper_09_research_start_lease_state": start_lease["state"],
        "live_account_submission_leases_at_release_snapshot": live_account,
        "rail_released_for_next_authorized_lane": True,
        "next_named_lanes": ["Yui narration batch", "read-only Gemini usage check"],
        "broker_frozen": live["frozen"],
        "ledger_verify_before_release_receipt": r.ledger.verify(r.LEDGER_PATH)[1],
    }
    r.atomic_json(RELEASE_RECEIPT, release)
    release_sha = sha_file(RELEASE_RECEIPT)
    release_entry = r.journal_entry(
        "dr9_account_submission_rail_released",
        f"DR9 paper_09 completed; Start-research account lease {start_lease_id} is released; live account-submission leases at snapshot={len(live_account)}; release_receipt_sha256={release_sha}; Yui narration and read-only Gemini usage check may acquire normally under unchanged rails.",
        [RELEASE_RECEIPT],
    )
    state["account_submission_release"] = {
        "receipt_path": str(RELEASE_RECEIPT),
        "receipt_sha256": release_sha,
        "ledger": release_entry,
    }
    r.save_state(state)

    statuses, total_sources, summary_sha, summary_entry, summary_path = r.write_summary(state, final=True)
    rows, verified, ledger_message = verify_all(state)
    if not verified or not all(row["verified"] for row in rows) or statuses != {"completed": 9}:
        raise r.GlobalChallengeStop("final 9/9 custody verification failed")
    result = {
        "status": "DR9_9_OF_9_VERIFIED_COMPLETE",
        "paper_09_outcome": outcome,
        "paper_09_conversation_id": paper9["identity"]["conversation_id"],
        "paper_09_packet_sha256": paper9["packet_sha256"],
        "paper_09_deletion_sha256": paper9["deletion_sha256"],
        "paper_09_source_anchor_count": paper9["result"]["source_anchor_count"],
        "status_counts": statuses,
        "total_source_anchors": total_sources,
        "summary_path": str(summary_path),
        "summary_sha256": summary_sha,
        "summary_ledger": summary_entry,
        "release_receipt_path": str(RELEASE_RECEIPT),
        "release_receipt_sha256": release_sha,
        "release_ledger": release_entry,
        "ledger_verify": ledger_message,
        "papers": rows,
        "buffered_hwao_reports": buffered_reports,
    }
    print(json.dumps(result, sort_keys=True), flush=True)


if __name__ == "__main__":
    main()
