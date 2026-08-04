import json
import sys
from contextlib import suppress
from pathlib import Path

from playwright.sync_api import sync_playwright

sys.path.insert(0, "scratch")
import run_review_base_item05 as m

r = m.r
q = m.q
ROUTE = "/app/c5df8c52cb041e99"
CONVERSATION_ID = "c5df8c52cb041e99"
RECOVERY_HOLD = m.AREA_DIR / "area_review_05_maiolino_mannucci_2019_DR_RECOVERY_HOLD.json"


def relevant_grants():
    message, entries, grants = m.ramp.ledger_snapshot()
    rows = []
    for row in grants:
        holder = row.get("payload", {}).get("holder", "")
        if "review_base_05" in holder:
            rows.append(row)
    return message, entries, rows


def navigate_exact_owned_route(browser):
    holder = "goru-dr-reresearch-r2-review_base_05-route-recovery"
    client = r.UDSClient(r.SOCK)
    lease = None
    try:
        record = r.target_record()
        if not record or record["path"] != "/app":
            raise r.TargetDrift(f"Review Base 05 recovery expected /app before exact-route navigation, got {record}")
        lease = r.acquire_target(client, holder, "write", ttl=300)
        page = r.exact_page(browser, "/app")
        if r.page_challenge(page):
            r.freeze_for_challenge(client, holder, "review_base_05", "pre-recovery exact-route navigation")
        r.check_action(client, lease, "review_base_05 navigate to exact accepted conversation without resend", "/app", page)
        page.goto(f"https://gemini.google.com{ROUTE}", wait_until="domcontentloaded", timeout=30000)
        page.wait_for_timeout(1500)
        if r.page_challenge(page):
            r.freeze_for_challenge(client, holder, "review_base_05", "post-recovery exact-route navigation")
        if not r.target_matches(ROUTE, page):
            raise r.TargetDrift(f"Review Base 05 exact route navigation failed: {page.url}")
        return page
    finally:
        if lease:
            r.release_lease(client, lease)


def main():
    if m.RAW_PACKET_PATH.exists() or m.RAW_METADATA_PATH.exists():
        raise RuntimeError("Review Base 05 raw custody already exists; refusing recovery rerun")
    existing = json.loads(m.STATE_PATH.read_text())
    if existing.get("papers", [{}])[0].get("status") != "staged":
        raise RuntimeError(f"Review Base 05 unexpected pre-recovery state: {existing}")
    current_spec = m.spec()
    custom = m.initial_state(current_spec)
    custom["created_utc"] = existing.get("papers", [{}])[0].get("staged_utc", r.utcnow())
    custom["paper"].update(existing["papers"][0])
    custom["status"] = "SUBMIT_ACCEPTED_ROUTE_RECOVERY_PENDING"
    custom["recovery"] = {"prompt_resent": False, "second_submit": False, "second_start": False, "conversation_id": CONVERSATION_ID, "reason": "accepted prompt appeared in exact Gemini history while dedicated target remained /app after navigation settlement timeout"}
    q.save_state(custom)
    adapted = q.adapted_state(custom)
    message, entries, grants = relevant_grants()
    submit = [row for row in grants if row.get("payload", {}).get("holder") == "goru-dr-reresearch-r2-review_base_05-submit"]
    starts = [row for row in grants if row.get("payload", {}).get("holder") == "goru-dr-reresearch-r2-review_base_05-start"]
    if not message.startswith("OK (") or len(submit) != 1 or starts:
        raise RuntimeError(f"Review Base 05 recovery custody mismatch: message={message} submit={submit} starts={starts}")
    identity = None
    try:
        with sync_playwright() as playwright:
            browser = playwright.chromium.connect_over_cdp(r.BASE)
            page = navigate_exact_owned_route(browser)
            prompt = m.PROMPT_PATH.read_text().rstrip("\n")
            evidence = r.current_prompt_identity(page, prompt)
            snapshot = r.page_snapshot(page)
            start = page.get_by_role("button", name="Start research", exact=True)
            visible_start = [start.nth(i) for i in range(start.count()) if start.nth(i).is_visible() and not start.nth(i).is_disabled()]
            if not evidence or snapshot["challenge"] or snapshot["research"] or snapshot["failure"]:
                raise r.TargetDrift(f"Review Base 05 accepted-route classification failed: evidence={evidence} snapshot={{'challenge':{snapshot['challenge']},'research':{snapshot['research']},'failure':{snapshot['failure']}}}")
            if len(visible_start) != 1 and not snapshot["messages"]:
                # The plan can still be settling; wait_for_plan below owns the terminal/start classification.
                pass
            submit_row = submit[0]
            identity = {
                "conversation_id": CONVERSATION_ID,
                "conversation_path": ROUTE,
                "target_id": r.target_record()["id"],
                "captured_title": "Review Base 05 exact accepted history route",
                "submit_utc": submit_row["utc"],
                "submit_account_lease_id": submit_row["payload"]["lease_id"],
                "prompt_sha256": current_spec["prompt_sha256"],
                "prompt_file_sha256": current_spec["prompt_file_sha256"],
                "identity_evidence": evidence,
                "page_challenge_after_submit": False,
                "recovered_after_navigation_settlement_timeout": True,
                "recovered_from_exact_history_route": True,
                "prompt_resent": False,
            }
            adapted["papers"][0].update(status="submitted", identity=identity)
            q.sync_state(custom, adapted)
            plan = r.wait_for_plan(identity, current_spec, adapted, browser)
            q.sync_state(custom, adapted)
            if plan == "start_required":
                try:
                    r.start_research(identity, current_spec, adapted, browser)
                    q.sync_state(custom, adapted)
                except r.PaperFailure as exc:
                    if "acceptance not positively confirmed" not in str(exc):
                        raise
                    classification = m.classify_after_start_timeout(identity, prompt, browser)
                    if classification in {"accepted_delayed", "terminal_delayed"}:
                        adapted["papers"][0].update(status="researching" if classification == "accepted_delayed" else "terminal_ready", research_start_utc=r.utcnow(), research_start_mode=classification)
                        q.sync_state(custom, adapted)
                    elif classification == "positively_unaccepted":
                        raise q.FirstUnacceptedHold("Review Base 05 Deep Research Start positively unaccepted; no retry")
                    else:
                        raise q.FirstUnacceptedHold("Review Base 05 Deep Research Start acceptance ambiguous; no retry")
            terminal_snapshot, result_sha = r.poll_terminal(identity, current_spec, adapted, browser)
            q.sync_state(custom, adapted)
            metadata = m.save_packet(terminal_snapshot, result_sha, identity, current_spec, custom)
            browser.close()
        print(json.dumps({"status": custom["status"], "packet": str(m.RAW_PACKET_PATH), "packet_sha256": metadata["packet_sha256"], "output_shape_pass": metadata["output_quality"]["pass"], "independent_identifier_verification": "PENDING", "prompt_resent": False, "second_start": False}, sort_keys=True), flush=True)
        return 0 if metadata["output_quality"]["pass"] else 2
    except Exception as exc:
        hold = {"status": "RECOVERY_HOLD_NO_RETRY", "failed_utc": r.utcnow(), "error_class": type(exc).__name__, "error": str(exc), "identity": identity, "prompt_resent": False, "second_submit": False, "retry_performed": False}
        r.atomic_json(RECOVERY_HOLD, hold)
        with suppress(Exception):
            q.save_state(custom, status="RECOVERY_HOLD_NO_RETRY", recovery_hold_path=str(RECOVERY_HOLD), error=f"{type(exc).__name__}: {exc}")
        print(json.dumps(hold, sort_keys=True), flush=True)
        return 3 if isinstance(exc, r.GlobalChallengeStop) else 2


if __name__ == "__main__":
    raise SystemExit(main())
