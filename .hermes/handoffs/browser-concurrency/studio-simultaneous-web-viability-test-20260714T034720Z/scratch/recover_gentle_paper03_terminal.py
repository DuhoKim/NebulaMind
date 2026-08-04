import hashlib
import json
import sys
from datetime import datetime, timedelta, timezone
from pathlib import Path
from typing import NoReturn

sys.path.insert(0, "scratch")
import dr_manuscript_round1_review_runner as r
from playwright.sync_api import sync_playwright

AUTH_PATH = Path("receipts/DUHO_RESUME_GENTLE_20260715.md").resolve()
AUTH_SHA256 = "900ac317bf3b9d93e6c1c648edd5a8d77ea7162a9340cd4fcf642d95e802920e"
RESET_ENTRY_SHA256 = "b6b97ee5ab31634867fa4e7bdf892104e418341528a43a7e965695f3f6ecf902"
RESET_EPOCH = 2566
PAPER_NUMBER = 3
RECOVERY_PATH = r.PACKET_DIR / "paper_03_round1_review_dr_packet.gentle_resume_delayed_acceptance.json"


def fail(message: str) -> NoReturn:
    raise RuntimeError(message)


def verify_gate_and_start_lease(state, spec):
    if hashlib.sha256(AUTH_PATH.read_bytes()).hexdigest() != AUTH_SHA256:
        fail("Duho gentle authorization hash mismatch")
    ok, message = r.ledger.verify(r.LEDGER_PATH)
    if not ok:
        fail(f"ledger invalid before paper_03 recovery: {message}")
    entries = r.ledger.read_entries(r.LEDGER_PATH)
    reset = next((row for row in entries if row.get("epoch") == RESET_EPOCH), None)
    if not reset or reset.get("type") != "frozen_reset" or reset.get("entry_sha256") != RESET_ENTRY_SHA256:
        fail("verified broker-authored gentle reset entry absent")
    if entries[-1]["epoch"] < RESET_EPOCH:
        fail("ledger does not include gentle reset")
    broker_state = json.loads(Path("broker/live_state.json").read_text())
    if broker_state.get("frozen"):
        fail("broker remains frozen")
    live = [row for row in broker_state.get("leases", {}).values() if row.get("state") == "live"]
    if live:
        fail(f"unexpected live leases before paper_03 recovery: {[row['lease_id'] for row in live]}")

    paper = state["papers"][PAPER_NUMBER - 1]
    if paper.get("status") != "failed":
        fail(f"paper_03 expected failed state, got {paper.get('status')}")
    identity = paper.get("identity") or {}
    if identity.get("conversation_id") != "bd0b18ee06967bbe" or identity.get("conversation_path") != "/app/bd0b18ee06967bbe":
        fail("paper_03 exact conversation identity mismatch")
    if identity.get("prompt_sha256") != spec["prompt_sha256"]:
        fail("paper_03 prompt identity mismatch")
    failure = Path(paper["failure_path"])
    if not failure.is_file() or r.sha_file(failure) != paper.get("failure_sha256"):
        fail("paper_03 immutable first failure receipt mismatch")
    if Path(spec["packet_path"]).exists() or Path(spec["metadata_path"]).exists() or Path(spec["deletion_path"]).exists() or RECOVERY_PATH.exists():
        fail("paper_03 recovery output already exists")

    start_grant = next((row for row in entries if row.get("type") == "lease_granted" and row.get("payload", {}).get("lease_id") == "L00384"), None)
    start_action = next((row for row in entries if row.get("type") == "action_allowed" and row.get("payload", {}).get("lease_id") == "L00384"), None)
    start_release = next((row for row in entries if row.get("type") == "lease_released" and row.get("payload", {}).get("lease_id") == "L00384"), None)
    if not start_grant or not start_action or not start_release:
        fail("paper_03 original Start lease/action/release custody incomplete")
    return identity, paper, entries, start_action, start_release, message


def main():
    specs = r.discover_prompts()
    state = r.load_or_create_state(specs)
    spec = specs[PAPER_NUMBER - 1]
    identity, paper, entries, start_action, start_release, preverify = verify_gate_and_start_lease(state, spec)
    path = identity["conversation_path"]
    record = r.target_record()
    if not record or record["path"] != path:
        fail(f"paper_03 exact route is not current: {None if not record else record['path']}")

    with sync_playwright() as pw:
        browser = pw.chromium.connect_over_cdp(r.BASE)
        page = r.exact_page(browser, path)
        client = r.UDSClient(r.SOCK)
        lease = r.acquire_target(client, "goru-dr-review-r1-paper_03-gentle-reconcile", "read", ttl=240, max_wait=20)
        try:
            if r.page_challenge(page):
                r.freeze_for_challenge(client, "goru-dr-review-r1-paper_03-gentle-reconcile", "paper_03", "Duho-cleared gentle reconciliation")
            r.check_action(client, lease, "paper_03 gentle exact-terminal reconciliation", path, page)
            snapshot = r.page_snapshot(page)
            starts = [control for control in snapshot["controls"] if control["label"] == "Start research"]
            last = snapshot["messages"][-1]["text"] if snapshot["messages"] else ""
            terminal = (
                len(snapshot["messages"]) >= 3
                and len(last) >= 2000
                and not snapshot["challenge"]
                and not snapshot["research"]
                and not snapshot["stop"]
                and not snapshot["failure"]
                and len(starts) == 1
                and starts[0]["disabled"]
            )
            if not terminal:
                fail(
                    "paper_03 is not positively terminal after clearance; "
                    f"messages={len(snapshot['messages'])} last_chars={len(last)} starts={starts} "
                    f"research={snapshot['research']} stop={snapshot['stop']} failure={snapshot['failure']}"
                )
            recovery = {
                "status": "DELAYED_START_ACCEPTANCE_TERMINAL",
                "paper_id": "paper_03",
                "authorization_path": str(AUTH_PATH),
                "authorization_sha256": AUTH_SHA256,
                "broker_reset_epoch": RESET_EPOCH,
                "broker_reset_entry_sha256": RESET_ENTRY_SHA256,
                "conversation_id": identity["conversation_id"],
                "conversation_path": path,
                "target_id": r.TARGET_ID,
                "prompt_sha256": spec["prompt_sha256"],
                "initial_identity_evidence": identity["identity_evidence"],
                "original_start_account_lease_id": "L00384",
                "original_start_action_epoch": start_action["epoch"],
                "original_start_action_utc": start_action["utc"],
                "original_start_release_epoch": start_release["epoch"],
                "original_start_release_utc": start_release["utc"],
                "first_failure_receipt": paper["failure_path"],
                "first_failure_receipt_sha256": paper["failure_sha256"],
                "current_evidence": {
                    "challenge": snapshot["challenge"],
                    "message_count": len(snapshot["messages"]),
                    "terminal_result_chars": len(last),
                    "terminal_result_sha256": r.sha_bytes(last.encode()),
                    "research": snapshot["research"],
                    "stop": snapshot["stop"],
                    "failure": snapshot["failure"],
                    "start_research_controls": starts,
                    "current_document_title_normalized_sha256": r.sha_bytes(r.normalized(page.title()).encode()),
                },
                "new_prompt_resubmit": False,
                "start_retry_performed": False,
                "account_submission_performed_after_resume": False,
                "classification": "The original broker-recorded Start action was accepted despite the prior detector timeout; the exact-owned route is now terminal. Never click Start again.",
                "ledger_verify_before": preverify,
            }
            r.atomic_json(RECOVERY_PATH, recovery)
            recovery_sha = r.sha_file(RECOVERY_PATH)
            r.set_paper_state(
                state,
                PAPER_NUMBER,
                status="researching",
                research_start_utc=start_action["utc"],
                research_start_mode="delayed_acceptance_recovered_after_Duho_clearance",
                research_start_account_lease_id="L00384",
                gentle_resume_authorization_sha256=AUTH_SHA256,
                gentle_resume_recovery_receipt=str(RECOVERY_PATH),
                gentle_resume_recovery_receipt_sha256=recovery_sha,
                gentle_resume_new_submit_performed=False,
            )
        finally:
            r.release_lease(client, lease)
            client.close()

        stable, result_sha = r.poll_terminal(identity, spec, state, browser)
        metadata, save_entry = r.save_packet(stable, result_sha, identity, spec, state)
        deletion, delete_entry = r.delete_exact_own(identity, spec, state, browser)
        browser.close()

    ok, final_verify = r.ledger.verify(r.LEDGER_PATH)
    if not ok:
        fail(f"ledger invalid after paper_03 custody: {final_verify}")
    final_state = json.loads(r.STATE_PATH.read_text())["papers"][PAPER_NUMBER - 1]
    if final_state.get("status") != "completed":
        fail("paper_03 did not reach completed state")
    next_submit_not_before = (datetime.now(timezone.utc) + timedelta(minutes=25)).isoformat().replace("+00:00", "Z")
    print(json.dumps({
        "status": "GORU_GENTLE_PAPER03_RECOVERED_COMPLETE",
        "paper_id": "paper_03",
        "new_submit_performed": False,
        "result_chars": metadata["result_chars"],
        "result_sha256": metadata["result_text_sha256"],
        "packet_path": spec["packet_path"],
        "packet_sha256": final_state["packet_sha256"],
        "deletion_path": spec["deletion_path"],
        "deletion_sha256": final_state["deletion_sha256"],
        "save_epoch": save_entry["epoch"],
        "delete_epoch": delete_entry["epoch"],
        "ledger_verify": final_verify,
        "next_submit_not_before": next_submit_not_before,
        "next_action": "WAIT; do not submit paper_04 until a fresh gentle-spacing dispatch and at least 20-30 minutes after this custody completion",
    }, sort_keys=True))


if __name__ == "__main__":
    main()
