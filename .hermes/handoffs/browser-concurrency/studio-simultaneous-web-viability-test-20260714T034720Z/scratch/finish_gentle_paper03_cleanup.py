import hashlib
import json
import sys
from pathlib import Path

sys.path.insert(0, "scratch")
import dr_manuscript_round1_review_runner as r
from playwright.sync_api import sync_playwright

AUTH_PATH = Path("receipts/DUHO_RESUME_GENTLE_20260715.md").resolve()
AUTH_SHA256 = "900ac317bf3b9d93e6c1c648edd5a8d77ea7162a9340cd4fcf642d95e802920e"
RESET_EPOCH = 2566
RESET_SHA256 = "b6b97ee5ab31634867fa4e7bdf892104e418341528a43a7e965695f3f6ecf902"
PAPER_NUMBER = 3


def main():
    if hashlib.sha256(AUTH_PATH.read_bytes()).hexdigest() != AUTH_SHA256:
        raise RuntimeError("Duho gentle authorization hash mismatch")
    specs = r.discover_prompts()
    state = r.load_or_create_state(specs)
    spec = specs[PAPER_NUMBER - 1]
    paper = state["papers"][PAPER_NUMBER - 1]
    if paper.get("status") != "saved_verified":
        raise RuntimeError(f"paper_03 expected saved_verified, got {paper.get('status')}")
    identity = paper.get("identity") or {}
    if identity.get("conversation_id") != "bd0b18ee06967bbe" or identity.get("conversation_path") != "/app/bd0b18ee06967bbe":
        raise RuntimeError("paper_03 exact-owned identity mismatch")
    if r.sha_file(spec["packet_path"]) != paper.get("packet_sha256") or r.sha_file(spec["metadata_path"]) != paper.get("metadata_sha256"):
        raise RuntimeError("paper_03 verified packet custody hash mismatch")
    if Path(spec["deletion_path"]).exists():
        raise RuntimeError("paper_03 deletion evidence already exists")

    ok, before = r.ledger.verify(r.LEDGER_PATH)
    entries = r.ledger.read_entries(r.LEDGER_PATH) if ok else []
    reset = next((row for row in entries if row.get("epoch") == RESET_EPOCH), None)
    save = next((row for row in entries if row.get("epoch") == paper.get("save_ledger", {}).get("epoch")), None)
    if not ok or not reset or reset.get("type") != "frozen_reset" or reset.get("entry_sha256") != RESET_SHA256:
        raise RuntimeError(f"gentle reset custody invalid: {before}")
    if not save or save.get("type") != "dr_review_r1_paper_03_reference_packet_saved_verified" or save.get("entry_sha256") != paper.get("save_ledger", {}).get("entry_sha256"):
        raise RuntimeError("paper_03 verified-save ledger custody invalid")
    broker_state = json.loads(Path("broker/live_state.json").read_text())
    live = [row["lease_id"] for row in broker_state.get("leases", {}).values() if row.get("state") == "live"]
    if broker_state.get("frozen") or live:
        raise RuntimeError(f"broker not ready frozen={broker_state.get('frozen')} live={live}")
    if not r.target_matches(identity["conversation_path"]):
        raise RuntimeError("paper_03 exact-owned terminal route is not current")

    with sync_playwright() as pw:
        browser = pw.chromium.connect_over_cdp(r.BASE)
        page = r.exact_page(browser, identity["conversation_path"])
        if r.page_challenge(page):
            client = r.UDSClient(r.SOCK)
            try:
                r.freeze_for_challenge(client, "goru-paper03-gentle-cleanup-recovery", "paper_03", "cleanup recovery preflight")
            finally:
                client.close()
        saved_identity = r.current_saved_result_identity(page, paper)
        if not saved_identity:
            # The prior bounded diagnostic closed Gemini's immersive report
            # panel. Reopen only this exact route's report, re-prove the saved
            # result, then let delete_exact_own close the verified panel before
            # exposing the current-chat menu.
            client = r.UDSClient(r.SOCK)
            lease = r.acquire_target(client, "goru-paper03-gentle-reopen-verified-report", "write", ttl=180, max_wait=20)
            try:
                expand = page.locator('[data-test-id="luminous-expand-button"]')
                if expand.count() != 1 or not expand.is_visible():
                    raise RuntimeError(f"paper_03 verified report Expand control unavailable count={expand.count()}")
                r.check_action(client, lease, "paper_03 reopen exact verified terminal report for cleanup identity", identity["conversation_path"], page)
                expand.click()
                page.wait_for_timeout(900)
                if r.page_challenge(page):
                    r.freeze_for_challenge(client, "goru-paper03-gentle-reopen-verified-report", "paper_03", "after verified report reopen")
                r.check_action(client, lease, "paper_03 verify exact route after terminal report reopen", identity["conversation_path"], page)
                saved_identity = r.current_saved_result_identity(page, paper)
            finally:
                r.release_lease(client, lease)
                client.close()
        if not saved_identity:
            raise RuntimeError("paper_03 current exact route does not match the verified terminal result")
        deletion, delete_entry = r.delete_exact_own(identity, spec, state, browser)
        browser.close()

    ok, after = r.ledger.verify(r.LEDGER_PATH)
    final = json.loads(r.STATE_PATH.read_text())["papers"][PAPER_NUMBER - 1]
    if not ok or final.get("status") != "completed":
        raise RuntimeError(f"paper_03 cleanup final verification failed: {after}")
    print(json.dumps({
        "status": "GORU_GENTLE_PAPER03_COMPLETE",
        "paper_id": "paper_03",
        "new_prompt_submit_performed": False,
        "start_retry_performed": False,
        "challenge_seen_after_resume": False,
        "packet_path": spec["packet_path"],
        "packet_sha256": final["packet_sha256"],
        "result_text_sha256": final["result"]["text_sha256"],
        "result_chars": final["result"]["chars"],
        "deletion_path": spec["deletion_path"],
        "deletion_sha256": final["deletion_sha256"],
        "delete_epoch": delete_entry["epoch"],
        "ledger_verify": after,
        "next_action": "WAIT; paper_04 is not authorized in this process",
    }, sort_keys=True))


if __name__ == "__main__":
    main()
