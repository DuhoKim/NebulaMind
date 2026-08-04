import json
import sys
from contextlib import suppress
from pathlib import Path

sys.path.insert(0, "scratch")
from playwright.sync_api import sync_playwright
import run_review_base_item02 as m

r = m.r
q = m.q
STATE = m.STATE_PATH


def main():
    spec = m.spec()
    adapted_on_disk = json.loads(STATE.read_text())
    if adapted_on_disk.get("batch_id") != m.RUN_ID or len(adapted_on_disk.get("papers", [])) != 1:
        raise RuntimeError("unexpected Review Base 02 pre-recovery state")
    existing = adapted_on_disk["papers"][0]
    if existing.get("status") != "staged":
        raise RuntimeError(f"expected staged state, got {existing.get('status')}")
    prompt = m.PROMPT_PATH.read_text().rstrip("\n")
    message, count, latest = q.latest_account_grant()
    if message != f"OK ({count} entries)" or not latest or latest.get("holder") != "goru-dr-reresearch-r2-review_base_02-submit":
        raise RuntimeError(f"submit grant custody mismatch: ledger={message} latest={latest}")
    broker, live = m.ramp.broker_snapshot()
    if broker.get("frozen") or live:
        raise RuntimeError(f"broker not clean before Review Base 02 recovery: frozen={broker.get('frozen')} live={live}")
    state = m.initial_state(spec)
    identity = None
    with sync_playwright() as playwright:
        browser = playwright.chromium.connect_over_cdp(r.BASE)
        record = r.target_record()
        if not record or not record["path"].startswith("/app/"):
            raise r.TargetDrift("Review Base 02 exact conversation route missing")
        page = r.exact_page(browser, record["path"])
        if r.page_challenge(page):
            client = r.UDSClient(r.SOCK)
            try:
                r.freeze_for_challenge(client, "goru-review-base-02-recovery", "review_base_02", "recovery pre-Start classification")
            finally:
                client.close()
        prompt_evidence = r.current_prompt_identity(page, prompt)
        start = page.get_by_role("button", name="Start research", exact=True)
        enabled = [start.nth(i) for i in range(start.count()) if start.nth(i).is_visible() and not start.nth(i).is_disabled()]
        snapshot = r.page_snapshot(page)
        if not prompt_evidence or len(enabled) != 1 or snapshot["failure"] or snapshot["research"] or snapshot["stop"]:
            raise r.TargetDrift(f"Review Base 02 plan not safely recoverable: prompt={bool(prompt_evidence)} starts={len(enabled)} snapshot={snapshot}")
        identity = {
            "conversation_id": record["path"].split("/app/", 1)[1],
            "conversation_path": record["path"],
            "target_id": record["id"],
            "captured_title": record["title"],
            "submit_utc": latest["utc"],
            "submit_account_lease_id": latest["lease_id"],
            "prompt_sha256": spec["prompt_sha256"],
            "prompt_file_sha256": spec["prompt_file_sha256"],
            "identity_evidence": prompt_evidence,
            "page_challenge_after_submit": False,
            "recovered_after_navigation_settlement_timeout": True,
            "prompt_resent": False,
        }
        adapted = {
            "batch_id": m.RUN_ID,
            "reference_only": True,
            "advisory_only": True,
            "updated_utc": r.utcnow(),
            "papers": [{**existing, "status": "plan_ready", "identity": identity}],
        }
        state["paper"].update(existing)
        state["paper"].update(status="plan_ready", identity=identity)
        q.save_state(state, status="RECOVERED_PLAN_READY_START_ONCE", paper=state["paper"], recovery={"classification": "exact_owned_plan_ready", "prompt_resent": False, "submit_grant": latest})
        m.update_manifest("ITEM_02_RECOVERED_PLAN_READY", conversation_id=identity["conversation_id"], submit_utc=identity["submit_utc"], submit_account_lease_id=identity["submit_account_lease_id"], recovery="exact_owned_plan_no_resend")
        try:
            r.start_research(identity, spec, adapted, browser)
        except r.PaperFailure as exc:
            if "acceptance not positively confirmed" not in str(exc):
                raise
            classification = m.classify_after_start_timeout(identity, prompt, browser)
            if classification not in {"accepted_delayed", "terminal_delayed"}:
                raise q.FirstUnacceptedHold(f"Review Base 02 Start settlement {classification}; no retry")
            adapted["papers"][0].update(status="researching" if classification == "accepted_delayed" else "terminal_ready", research_start_utc=r.utcnow(), research_start_mode=classification)
        state["paper"].update(adapted["papers"][0])
        q.save_state(state, status="RESEARCH_ACTIVE", paper=state["paper"], recovery={"classification": "exact_owned_plan_started_once", "prompt_resent": False})
        m.update_manifest("ITEM_02_RESEARCH_ACTIVE", research_start_utc=state["paper"].get("research_start_utc"), research_start_account_lease_id=state["paper"].get("research_start_account_lease_id"), prompt_resent=False)
        snapshot, result_sha = r.poll_terminal(identity, spec, adapted, browser)
        state["paper"].update(adapted["papers"][0])
        metadata = m.save_packet(snapshot, result_sha, identity, spec, state)
        browser.close()
    print(json.dumps({"status": state["status"], "raw_packet": str(m.RAW_PACKET_PATH), "raw_packet_sha256": metadata["raw_packet_sha256"], "output_shape_pass": metadata["output_quality"]["pass"], "prompt_resent": False}, sort_keys=True), flush=True)
    return 0 if metadata["output_quality"]["pass"] else 2


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except Exception as exc:
        state = m.initial_state(m.spec())
        m.write_failure(state, exc)
        raise
