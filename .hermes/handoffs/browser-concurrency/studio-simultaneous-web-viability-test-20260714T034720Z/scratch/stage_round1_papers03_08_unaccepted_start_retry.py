import json
import sys
from pathlib import Path

sys.path.insert(0, "scratch")
import dr_manuscript_round1_review_runner as r
from playwright.sync_api import sync_playwright

RETRY_PAPERS = tuple(range(3, 9))
RECEIPT = r.PACKET_DIR / "ROUND1_PAPERS_03_08_UNACCEPTED_START_RETRY.json"


def main():
    ok, message = r.ledger.verify(r.LEDGER_PATH)
    if not ok:
        raise r.GlobalChallengeStop(f"ledger invalid before bounded retry staging: {message}")
    live = json.loads(Path("broker/live_state.json").read_text())
    if live.get("frozen"):
        raise r.GlobalChallengeStop("broker frozen before bounded retry staging")
    if any(value.get("state") == "live" and value.get("kind") == "account-submission" for value in live.get("leases", {}).values()):
        raise r.GlobalChallengeStop("account-submission lease active before bounded retry staging")

    state = json.loads(r.STATE_PATH.read_text())
    specs = r.discover_prompts()
    diagnostics = []
    client = r.UDSClient(r.SOCK)
    lease = None
    try:
        lease = r.acquire_target(client, "tori-r1-papers03-08-unaccepted-start-retry-preflight", "write", ttl=1200, max_wait=120)
        with sync_playwright() as playwright:
            browser = playwright.chromium.connect_over_cdp(r.BASE)
            current = r.target_record()
            if not current or current["path"] != "/app":
                raise r.TargetDrift("bounded retry preflight requires current /app")
            page = r.exact_page(browser, "/app")
            current_path = "/app"
            for paper_number in RETRY_PAPERS:
                row = state["papers"][paper_number - 1]
                spec = specs[paper_number - 1]
                if row.get("status") != "failed":
                    raise r.GlobalChallengeStop(f"{row['paper_id']} is not in failed state")
                records = row.get("failure_records", [])
                if not records:
                    raise r.GlobalChallengeStop(f"{row['paper_id']} lacks a failure receipt")
                failure_path = Path(records[-1]["path"])
                failure = json.loads(failure_path.read_text())
                if failure.get("error") != "Start research acceptance not positively confirmed" or failure.get("global_challenge_stop"):
                    raise r.GlobalChallengeStop(f"{row['paper_id']} failure is not the bounded unaccepted-Start case")
                identity = row.get("identity")
                if not identity:
                    raise r.GlobalChallengeStop(f"{row['paper_id']} lacks durable submitted identity")
                destination = identity["conversation_path"]
                r.check_action(client, lease, f"authorize {row['paper_id']} unaccepted-Start retry preflight navigation", current_path, page)
                page.goto("https://gemini.google.com" + destination, wait_until="domcontentloaded", timeout=60000)
                page.wait_for_timeout(2500)
                r.check_action(client, lease, f"verify {row['paper_id']} exact-owned retry preflight route", destination, page)
                if r.page_challenge(page):
                    r.freeze_for_challenge(client, "tori-r1-papers03-08-unaccepted-start-retry-preflight", row["paper_id"], "bounded retry preflight")
                prompt = Path(spec["prompt_path"]).read_text().rstrip("\n")
                prompt_identity = r.current_prompt_identity(page, prompt)
                snapshot = r.page_snapshot(page)
                start = page.get_by_role("button", name="Start research", exact=True)
                enabled_start = [start.nth(i) for i in range(start.count()) if start.nth(i).is_visible() and not start.nth(i).is_disabled()]
                if not prompt_identity or len(enabled_start) != 1 or snapshot.get("challenge") or snapshot.get("research") or snapshot.get("stop") or snapshot.get("failure"):
                    raise r.GlobalChallengeStop(f"{row['paper_id']} is not positively an exact-owned plan with one unaccepted Start control")
                holder = f"goru-dr-review-r1-{row['paper_id']}-start"
                account_leases = [value for value in live.get("leases", {}).values() if value.get("holder") == holder and value.get("kind") == "account-submission"]
                if len(account_leases) != 1 or account_leases[0].get("state") != "released":
                    raise r.GlobalChallengeStop(f"{row['paper_id']} first Start account lease is not uniquely released")
                diagnostics.append({
                    "paper_id": row["paper_id"],
                    "conversation_id": identity["conversation_id"],
                    "conversation_path": destination,
                    "prompt_sha256": spec["prompt_sha256"],
                    "prompt_identity_evidence": prompt_identity,
                    "plan_message_count": len(snapshot["messages"]),
                    "enabled_Start_research_count": len(enabled_start),
                    "research_visible": snapshot.get("research"),
                    "stop_visible": snapshot.get("stop"),
                    "failure_visible": snapshot.get("failure"),
                    "page_challenge": snapshot.get("challenge"),
                    "first_Start_account_lease_id": account_leases[0]["lease_id"],
                    "first_Start_account_lease_state": account_leases[0]["state"],
                    "first_attempt_failure_path": str(failure_path),
                    "first_attempt_failure_sha256": r.sha_file(failure_path),
                    "retry_requires_new_prompt_submit": False,
                    "retry_requires_second_Start_click": True,
                })
                current_path = destination
            r.check_action(client, lease, "authorize bounded retry preflight return to /app", current_path, page)
            page.goto("https://gemini.google.com/app", wait_until="domcontentloaded", timeout=60000)
            page.wait_for_timeout(1500)
            r.check_action(client, lease, "verify bounded retry preflight return to /app", "/app", page)
    finally:
        r.release_lease(client, lease)
        client.close()

    receipt = {
        "batch_id": state["batch_id"],
        "classification": "six exact-owned research plans where the first Start click was not accepted",
        "retry_scope": [item["paper_id"] for item in diagnostics],
        "diagnostics": diagnostics,
        "broker_frozen": False,
        "account_challenge": False,
        "new_prompt_submits_authorized": False,
        "one_broker_serialized_Start_retry_per_paper_authorized": True,
        "bulk_history_action": False,
        "unrelated_conversation_action": False,
        "reference_only": True,
        "advisory_only": True,
        "created_utc": r.utcnow(),
    }
    r.atomic_json(RECEIPT, receipt)
    receipt_sha = r.sha_file(RECEIPT)
    files = [RECEIPT]
    files.extend(Path(item["first_attempt_failure_path"]) for item in diagnostics)
    files.extend(Path(specs[number - 1]["prompt_path"]) for number in RETRY_PAPERS)
    retry_ledger = r.journal_entry(
        "dr_review_r1_papers_03_08_unaccepted_start_retry_staged",
        f"REFERENCE-ONLY papers_03-08 each positively remain at one exact-owned research plan with one enabled Start control after the first broker-serialized Start click was not accepted; retry receipt_sha256={receipt_sha}; no new prompt submit; one serialized Start retry per paper; no challenge/freeze/protected mutation.",
        files,
    )
    for diagnostic in diagnostics:
        number = int(diagnostic["paper_id"].split("_")[1])
        r.set_paper_state(
            state,
            number,
            status="submitted",
            unaccepted_start_retry_receipt=str(RECEIPT),
            unaccepted_start_retry_receipt_sha256=receipt_sha,
            unaccepted_start_retry_ledger=retry_ledger,
            unaccepted_start_retry_staged_utc=r.utcnow(),
            first_Start_account_lease_id=diagnostic["first_Start_account_lease_id"],
            Start_retry_count_authorized=1,
            new_prompt_resubmit_authorized=False,
        )
    state["first_terminal_summary_superseded_by_unaccepted_start_retry"] = {
        "summary_path": state.get("summary_path"),
        "summary_sha256": state.get("summary_sha256"),
        "retry_receipt": str(RECEIPT),
        "retry_receipt_sha256": receipt_sha,
        "retry_ledger": retry_ledger,
    }
    r.save_state(state)
    print(json.dumps({
        "status": "PAPERS_03_08_UNACCEPTED_START_RETRY_STAGED",
        "receipt": str(RECEIPT),
        "receipt_sha256": receipt_sha,
        "ledger": retry_ledger,
        "paper_statuses": [(row["paper_id"], row["status"]) for row in state["papers"]],
    }, sort_keys=True))


if __name__ == "__main__":
    main()
