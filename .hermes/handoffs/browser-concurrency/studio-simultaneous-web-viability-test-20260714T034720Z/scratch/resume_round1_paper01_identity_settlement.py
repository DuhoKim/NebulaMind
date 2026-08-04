import hashlib
import json
import sys
from datetime import datetime, timezone
from pathlib import Path

sys.path.insert(0, "scratch")
import dr_manuscript_round1_review_runner as r
from playwright.sync_api import sync_playwright

EXPECTED_CONVERSATION_ID = "85cfb351f701a241"
EXPECTED_PATH = f"/app/{EXPECTED_CONVERSATION_ID}"
EXPECTED_ACCOUNT_LEASE_ID = "L00342"
RESUME_RECEIPT = r.PACKET_DIR / "paper_01_identity_settlement_resume.json"


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def main():
    ok, message = r.ledger.verify(r.LEDGER_PATH)
    if not ok:
        raise r.GlobalChallengeStop(f"ledger invalid before identity settlement: {message}")
    live_path = Path("broker/live_state.json")
    live = json.loads(live_path.read_text())
    if live.get("frozen"):
        raise r.GlobalChallengeStop("broker is frozen; identity settlement may not proceed")
    account_lease = live.get("leases", {}).get(EXPECTED_ACCOUNT_LEASE_ID)
    if not account_lease or account_lease.get("holder") != "goru-dr-review-r1-paper_01-submit" or account_lease.get("kind") != "account-submission" or account_lease.get("state") != "released":
        raise r.GlobalChallengeStop("paper_01 prompt-submit account lease is not positively released")
    state = json.loads(r.STATE_PATH.read_text())
    paper = state["papers"][0]
    if paper.get("status") != "failed" or paper.get("staged_text_sha256") != paper.get("prompt_sha256"):
        raise r.GlobalChallengeStop("paper_01 failed/staged durable state mismatch")
    failure_path = Path(paper["failure_path"])
    if not failure_path.exists() or sha(failure_path) != paper.get("failure_sha256"):
        raise r.GlobalChallengeStop("paper_01 failure receipt hash mismatch")
    prompt_path = Path(paper["prompt_path"])
    prompt = prompt_path.read_text().rstrip("\n")
    if r.sha_bytes(prompt.encode()) != paper["prompt_sha256"] or sha(prompt_path) != paper["prompt_file_sha256"]:
        raise r.GlobalChallengeStop("paper_01 prompt hash drift")

    client = r.UDSClient(r.SOCK)
    target_lease = None
    try:
        target_lease = r.acquire_target(client, "tori-paper01-settled-identity-resume", "read", ttl=240, max_wait=90)
        with sync_playwright() as playwright:
            browser = playwright.chromium.connect_over_cdp(r.BASE)
            page = r.exact_page(browser, EXPECTED_PATH)
            if r.page_challenge(page):
                r.freeze_for_challenge(client, "tori-paper01-settled-identity-resume", "paper_01", "settled identity verification")
            r.check_action(client, target_lease, "paper_01 read-only settled identity verification", EXPECTED_PATH, page)
            identity_evidence = r.current_prompt_identity(page, prompt)
            snapshot = r.page_snapshot(page)
            start = page.get_by_role("button", name="Start research", exact=True)
            visible_start = [start.nth(i) for i in range(start.count()) if start.nth(i).is_visible() and not start.nth(i).is_disabled()]
            if not identity_evidence or len(visible_start) != 1 or snapshot.get("challenge") or snapshot.get("research") or snapshot.get("stop"):
                raise r.GlobalChallengeStop("settled exact route does not positively match the submitted prompt plus one enabled Start research control")
    finally:
        r.release_lease(client, target_lease)
        client.close()

    submit_utc = datetime.fromtimestamp(account_lease["granted_at"], timezone.utc).isoformat().replace("+00:00", "Z")
    identity = {
        "target_id": r.TARGET_ID,
        "conversation_id": EXPECTED_CONVERSATION_ID,
        "conversation_path": EXPECTED_PATH,
        "captured_title": identity_evidence["captured_title"],
        "identity_evidence": {
            **identity_evidence,
            "settled_after_initial_transient_history_row_absence": True,
            "enabled_start_research_count": 1,
        },
        "submit_utc": submit_utc,
        "submit_account_lease_id": EXPECTED_ACCOUNT_LEASE_ID,
        "prompt_sha256": paper["prompt_sha256"],
        "prompt_file_sha256": paper["prompt_file_sha256"],
        "page_challenge_after_submit": False,
    }
    receipt = {
        "paper_id": "paper_01",
        "batch_id": state["batch_id"],
        "classification": "benign post-submit identity-settlement lag; not a broker freeze and not an account challenge",
        "original_failure_path": str(failure_path),
        "original_failure_sha256": sha(failure_path),
        "conversation_id": EXPECTED_CONVERSATION_ID,
        "conversation_path": EXPECTED_PATH,
        "prompt_sha256": paper["prompt_sha256"],
        "prompt_file_sha256": paper["prompt_file_sha256"],
        "submit_account_lease_id": EXPECTED_ACCOUNT_LEASE_ID,
        "submit_account_lease_state": account_lease["state"],
        "settled_identity_evidence": identity["identity_evidence"],
        "page_challenge": False,
        "broker_frozen": False,
        "start_research_clicked_by_settlement": False,
        "resumed_status": "submitted",
        "reference_only": True,
        "advisory_only": True,
        "generated_utc": r.utcnow(),
    }
    r.atomic_json(RESUME_RECEIPT, receipt)
    receipt_sha = sha(RESUME_RECEIPT)
    resume_entry = r.journal_entry(
        "dr_review_r1_paper_01_identity_settlement_resume",
        f"REFERENCE-ONLY paper_01 exact prompt route settled after transient identity lag; conversation_id={EXPECTED_CONVERSATION_ID}; submit account lease {EXPECTED_ACCOUNT_LEASE_ID} released; receipt_sha256={receipt_sha}; broker_frozen=false; no challenge; no second prompt submit or Start-research click performed by settlement.",
        [RESUME_RECEIPT, failure_path, prompt_path],
    )
    paper.update({
        "status": "submitted",
        "identity": identity,
        "identity_settlement_receipt": str(RESUME_RECEIPT),
        "identity_settlement_receipt_sha256": receipt_sha,
        "identity_settlement_ledger": resume_entry,
    })
    for later in state["papers"][1:]:
        if later.get("status") == "not_run_target_blocked":
            later["status"] = "pending"
            later["reset_from_first_attempt_hold_utc"] = r.utcnow()
    state["first_attempt_hold_superseded_by_identity_settlement"] = {
        "hold_summary_path": state.get("hold_summary_path"),
        "hold_summary_sha256": state.get("hold_summary_sha256"),
        "resume_receipt": str(RESUME_RECEIPT),
        "resume_receipt_sha256": receipt_sha,
        "resume_ledger": resume_entry,
    }
    r.save_state(state)
    print(json.dumps({"status": "PAPER_01_SETTLED_IDENTITY_RESUMED", "conversation_id": EXPECTED_CONVERSATION_ID, "receipt": str(RESUME_RECEIPT), "receipt_sha256": receipt_sha, "ledger": resume_entry, "paper_statuses": [(row["paper_id"], row["status"]) for row in state["papers"]]}, sort_keys=True))


if __name__ == "__main__":
    main()
