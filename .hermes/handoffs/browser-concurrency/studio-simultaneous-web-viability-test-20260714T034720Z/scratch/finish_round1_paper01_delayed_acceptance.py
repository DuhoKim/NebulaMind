import json
import sys
import time
from datetime import datetime, timezone
from pathlib import Path

sys.path.insert(0, "scratch")
import dr_manuscript_round1_review_runner as r
from playwright.sync_api import sync_playwright

PAPER01_PATH = "/app/85cfb351f701a241"
PAPER02_PATH = "/app/14b9d19dbeb7b3ac"
START_ACCOUNT_LEASE_ID = "L00348"
ACCEPTANCE_RECEIPT = r.PACKET_DIR / "paper_01_delayed_start_acceptance.json"
RESTORE_RECEIPT = r.PACKET_DIR / "paper_01_completed_paper_02_route_restored.json"


def navigate_under_lease(client, lease, page, current_path, destination_path, action):
    r.check_action(client, lease, f"authorize {action} from {current_path} to {destination_path}", current_path, page)
    page.goto("https://gemini.google.com" + destination_path, wait_until="domcontentloaded", timeout=60000)
    page.wait_for_timeout(1800)
    r.check_action(client, lease, f"verify {action} at {destination_path}", destination_path, page)


def main():
    ok, message = r.ledger.verify(r.LEDGER_PATH)
    if not ok:
        raise r.GlobalChallengeStop(f"ledger invalid before paper_01 delayed-acceptance recovery: {message}")
    live = json.loads(Path("broker/live_state.json").read_text())
    if live.get("frozen"):
        raise r.GlobalChallengeStop("broker frozen before paper_01 delayed-acceptance recovery")
    start_lease = live.get("leases", {}).get(START_ACCOUNT_LEASE_ID)
    if not start_lease or start_lease.get("holder") != "goru-dr-review-r1-paper_01-start" or start_lease.get("kind") != "account-submission" or start_lease.get("state") != "released":
        raise r.GlobalChallengeStop("paper_01 Start-research lease is not positively released")

    state = json.loads(r.STATE_PATH.read_text())
    specs = r.discover_prompts()
    spec1, spec2 = specs[0], specs[1]
    paper1, paper2 = state["papers"][0], state["papers"][1]
    if paper1.get("status") != "failed" or paper2.get("status") != "submitted":
        raise r.GlobalChallengeStop("paper_01/paper_02 durable states do not match the bounded recovery precondition")
    identity1, identity2 = paper1.get("identity"), paper2.get("identity")
    if not identity1 or identity1.get("conversation_path") != PAPER01_PATH or not identity2 or identity2.get("conversation_path") != PAPER02_PATH:
        raise r.GlobalChallengeStop("conversation identity mismatch before bounded recovery")
    prompt1 = Path(spec1["prompt_path"]).read_text().rstrip("\n")
    prompt2 = Path(spec2["prompt_path"]).read_text().rstrip("\n")
    if r.sha_bytes(prompt1.encode()) != spec1["prompt_sha256"] or r.sha_bytes(prompt2.encode()) != spec2["prompt_sha256"]:
        raise r.GlobalChallengeStop("prompt hash drift before bounded recovery")

    with sync_playwright() as playwright:
        browser = playwright.chromium.connect_over_cdp(r.BASE)
        client = r.UDSClient(r.SOCK)
        lease = None
        try:
            lease = r.acquire_target(client, "tori-paper01-delayed-acceptance-verify", "write", ttl=300, max_wait=120)
            current = r.target_record()
            if not current or current["path"] not in {PAPER01_PATH, PAPER02_PATH}:
                raise r.TargetDrift("expected paper_01 or paper_02 exact-owned route before delayed-acceptance verification")
            page = r.exact_page(browser, current["path"])
            if current["path"] == PAPER02_PATH:
                navigate_under_lease(client, lease, page, PAPER02_PATH, PAPER01_PATH, "paper_01 delayed-acceptance verification")
            else:
                r.check_action(client, lease, "verify current paper_01 delayed-acceptance route", PAPER01_PATH, page)
            prompt_identity = None
            active_research = False
            terminal_candidate = False
            expected_title_sha = identity1.get("identity_evidence", {}).get("document_title_normalized_sha256")
            if not expected_title_sha:
                raise r.GlobalChallengeStop("paper_01 recorded identity lacks its verified document-title hash")
            for _ in range(24):
                if r.page_challenge(page):
                    r.freeze_for_challenge(client, "tori-paper01-delayed-acceptance-verify", "paper_01", "delayed Start-research acceptance verification")
                document_title = r.normalized(page.title())
                current_title_sha = r.sha_bytes(document_title.encode())
                prompt_identity = {
                    "evidence": "exact_route_plus_previously_verified_submit_identity_plus_matching_document_title",
                    "document_title_normalized_sha256": current_title_sha,
                    "expected_document_title_normalized_sha256": expected_title_sha,
                    "conversation_id": identity1["conversation_id"],
                } if current_title_sha == expected_title_sha else None
                snapshot = r.page_snapshot(page)
                in_progress_text = " ".join(item["text"] for item in snapshot["messages"])
                in_progress_signal = snapshot.get("research") or "While I'm researching" in in_progress_text or "Researching " in in_progress_text or "Creating visuals for the report" in in_progress_text or "Writing your report" in in_progress_text
                active_research = bool(in_progress_signal)
                last_message = snapshot["messages"][-1]["text"] if snapshot["messages"] else ""
                terminal_candidate = bool(len(snapshot["messages"]) >= 3 and len(last_message) >= 2000 and not snapshot.get("stop") and not snapshot.get("research"))
                if prompt_identity and (active_research or terminal_candidate) and not snapshot.get("challenge"):
                    break
                page.wait_for_timeout(2500)
            else:
                raise r.GlobalChallengeStop("paper_01 exact-owned route did not settle to a positive active or terminal-result identity within 60 seconds")
        finally:
            r.release_lease(client, lease)
            client.close()

        start_utc = datetime.fromtimestamp(start_lease["granted_at"], timezone.utc).isoformat().replace("+00:00", "Z")
        acceptance = {
            "paper_id": "paper_01",
            "classification": "benign delayed Start-research UI acceptance; no broker freeze and no account challenge",
            "conversation_id": identity1["conversation_id"],
            "conversation_path": PAPER01_PATH,
            "prompt_sha256": spec1["prompt_sha256"],
            "research_start_account_lease_id": START_ACCOUNT_LEASE_ID,
            "research_start_account_lease_state": start_lease["state"],
            "research_start_utc": start_utc,
            "active_research_verified": active_research,
            "terminal_result_candidate_verified": terminal_candidate,
            "page_challenge": False,
            "second_Start_research_click": False,
            "second_prompt_submit": False,
            "prompt_identity_evidence": prompt_identity,
            "verified_utc": r.utcnow(),
            "reference_only": True,
            "advisory_only": True,
        }
        r.atomic_json(ACCEPTANCE_RECEIPT, acceptance)
        acceptance_sha = r.sha_file(ACCEPTANCE_RECEIPT)
        r.set_paper_state(
            state,
            1,
            status="researching",
            research_start_utc=start_utc,
            research_start_mode="confirmed_delayed_ui_settlement",
            research_start_account_lease_id=START_ACCOUNT_LEASE_ID,
            delayed_start_acceptance_receipt=str(ACCEPTANCE_RECEIPT),
            delayed_start_acceptance_receipt_sha256=acceptance_sha,
        )

        snapshot, result_sha = r.poll_terminal(identity1, spec1, state, browser)
        r.save_packet(snapshot, result_sha, identity1, spec1, state)
        r.delete_exact_own(identity1, spec1, state, browser)

        client = r.UDSClient(r.SOCK)
        lease = None
        try:
            lease = r.acquire_target(client, "tori-paper01-finish-restore-paper02", "write", ttl=300, max_wait=120)
            current = r.target_record()
            if not current:
                raise r.TargetDrift("target absent after paper_01 exact-own deletion")
            current_path = current["path"]
            page = r.exact_page(browser, current_path)
            navigate_under_lease(client, lease, page, current_path, PAPER02_PATH, "restore submitted paper_02 exact route")
            if r.page_challenge(page):
                r.freeze_for_challenge(client, "tori-paper01-finish-restore-paper02", "paper_02", "route restoration")
            prompt_identity2 = r.current_prompt_identity(page, prompt2)
            snapshot2 = r.page_snapshot(page)
            start = page.get_by_role("button", name="Start research", exact=True)
            enabled_start = [start.nth(i) for i in range(start.count()) if start.nth(i).is_visible() and not start.nth(i).is_disabled()]
            if not prompt_identity2 or snapshot2.get("challenge") or not (len(enabled_start) == 1 or (snapshot2.get("research") and snapshot2.get("stop"))):
                raise r.GlobalChallengeStop("paper_02 exact submitted route was not positively restored")
        finally:
            r.release_lease(client, lease)
            client.close()

    restore = {
        "paper_01_status": state["papers"][0]["status"],
        "paper_01_conversation_id": identity1["conversation_id"],
        "paper_01_packet_sha256": state["papers"][0].get("packet_sha256"),
        "paper_01_deletion_sha256": state["papers"][0].get("deletion_sha256"),
        "paper_02_status": state["papers"][1]["status"],
        "paper_02_conversation_id": identity2["conversation_id"],
        "paper_02_conversation_path": PAPER02_PATH,
        "paper_02_prompt_sha256": spec2["prompt_sha256"],
        "paper_02_prompt_identity_evidence": prompt_identity2,
        "paper_02_enabled_start_research_count": len(enabled_start),
        "paper_02_already_researching": bool(snapshot2.get("research") and snapshot2.get("stop")),
        "page_challenge": False,
        "restored_utc": r.utcnow(),
        "reference_only": True,
        "advisory_only": True,
    }
    r.atomic_json(RESTORE_RECEIPT, restore)
    restore_sha = r.sha_file(RESTORE_RECEIPT)
    restore_ledger = r.journal_entry(
        "dr_review_r1_paper_01_completed_paper_02_route_restored",
        f"REFERENCE-ONLY paper_01 delayed Start acceptance recovered without a second click; packet saved and exact-own conversation deleted; paper_02 exact submitted route restored; receipt_sha256={restore_sha}; no protected mutation.",
        [RESTORE_RECEIPT, ACCEPTANCE_RECEIPT, spec1["packet_path"], spec1["metadata_path"], spec1["deletion_path"], spec2["prompt_path"]],
    )
    r.set_paper_state(
        state,
        1,
        delayed_start_acceptance_receipt=str(ACCEPTANCE_RECEIPT),
        delayed_start_acceptance_receipt_sha256=acceptance_sha,
        paper02_route_restore_receipt=str(RESTORE_RECEIPT),
        paper02_route_restore_receipt_sha256=restore_sha,
        paper02_route_restore_ledger=restore_ledger,
    )
    r.save_state(state)
    print(json.dumps({
        "status": "PAPER_01_COMPLETED_PAPER_02_ROUTE_RESTORED",
        "paper_01_packet": spec1["packet_path"],
        "paper_01_packet_sha256": state["papers"][0].get("packet_sha256"),
        "paper_01_deletion_sha256": state["papers"][0].get("deletion_sha256"),
        "paper_02_status": state["papers"][1]["status"],
        "paper_02_path": PAPER02_PATH,
        "restore_receipt": str(RESTORE_RECEIPT),
        "restore_receipt_sha256": restore_sha,
        "ledger": restore_ledger,
    }, sort_keys=True))


if __name__ == "__main__":
    main()
