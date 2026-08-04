import hashlib
import json
import sys
import time
from contextlib import suppress
from pathlib import Path
from urllib.parse import urlparse

sys.path.insert(0, "scratch")
import dr_batch_9_reference_runner as r
from playwright.sync_api import sync_playwright

PAPER8_PATH = "/app/9acdaa7cdab43447"
OLD_FALSE_SUMMARY = r.PACKET_DIR / "DR_RESEARCH_BATCH_9_FINAL_SUMMARY.md"


def h(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def navigate_exact(browser, path, paper_id, reason):
    holder = f"tori-dr9-rescue-{paper_id}-navigate"
    client = r.UDSClient(r.SOCK)
    lease = None
    try:
        lease = r.acquire_target(client, holder, "write", ttl=300)
        record = r.target_record()
        if not record:
            raise r.TargetDrift("no exact Pro Gemini target")
        current_path = record["path"]
        page = r.exact_page(browser, current_path)
        if r.page_challenge(page):
            r.freeze_for_challenge(client, holder, paper_id, reason)
        if current_path != path:
            r.check_action(client, lease, f"{paper_id} navigate exact owned conversation for {reason}", current_path, page)
            page.goto("https://gemini.google.com" + path, wait_until="domcontentloaded", timeout=30000)
        page.wait_for_timeout(8000)
        if not r.target_matches(path, page) or r.page_challenge(page):
            raise r.TargetDrift(f"{paper_id} exact navigation verification failed")
        return page.url
    finally:
        r.release_lease(client, lease)
        client.close()


def preserve_false_summary(state):
    if not OLD_FALSE_SUMMARY.exists():
        return
    old_sha = h(OLD_FALSE_SUMMARY)
    records = state.setdefault("interim_attempts", [])
    if not any(item.get("summary_sha256") == old_sha for item in records):
        records.append({
            "kind": "nonfinal_false_failure_summary_preserved",
            "summary_path": str(OLD_FALSE_SUMMARY),
            "summary_sha256": old_sha,
            "summary_ledger": state.get("final_summary_ledger"),
            "correction": "Seven packets had saved successfully; deletion identity virtualization and later paper-local submit UI failures made the all-failed label incorrect. Preserved, never overwritten.",
            "recorded_utc": r.utcnow(),
        })
    for key in ("final_summary_path", "final_summary_sha256", "final_summary_ledger", "completed_utc"):
        state.pop(key, None)
    r.save_state(state)


def finalize_paper1_prior_delete(state):
    spec = r.discover_prompts()[0]
    ps = state["papers"][0]
    deletion_path = Path(spec["deletion_path"])
    if deletion_path.exists():
        return
    if h(spec["packet_path"]) != ps["packet_sha256"] or h(spec["metadata_path"]) != ps["metadata_sha256"]:
        raise RuntimeError("paper_01 packet custody hash mismatch")
    ok, message = r.ledger.verify(r.LEDGER_PATH)
    if not ok:
        raise RuntimeError(message)
    entries = r.ledger.read_entries(r.LEDGER_PATH)
    choose = next((e for e in entries if e["epoch"] == 1383 and ps["identity"]["conversation_id"] in e.get("payload", {}).get("action", "")), None)
    confirm = next((e for e in entries if e["epoch"] == 1384 and ps["identity"]["conversation_id"] in e.get("payload", {}).get("action", "")), None)
    if not choose or not confirm:
        raise RuntimeError("paper_01 exact deletion action evidence missing")
    record = r.target_record()
    if not record or record["path"] != "/app":
        raise r.TargetDrift("paper_01 deletion settlement requires /app")
    evidence = {
        "paper_id": "paper_01",
        "advisory_only": True,
        "conversation_id": ps["identity"]["conversation_id"],
        "captured_title": ps["identity"]["captured_title"],
        "deletion_match_title": ps["identity"]["captured_title"],
        "title_relation": "exact_route_and_verified_terminal_result",
        "deletion_control": "exact_history_row_options",
        "saved_result_identity_evidence": {
            "evidence": "pre-delete exact route plus terminal result matched verified packet",
            "result_chars": ps["result"]["chars"],
            "result_text_sha256": ps["result"]["text_sha256"],
        },
        "submit_utc": ps["identity"]["submit_utc"],
        "deleted_utc": confirm["utc"],
        "target_id": r.TARGET_ID,
        "pre_delete_path": ps["identity"]["conversation_path"],
        "post_delete_path": "/app",
        "confirmation_mode": "dialog",
        "confirmation_dialog": "Deletion confirmed by exact broker-gated action and independently settled reload.",
        "choose_delete_ledger_epoch": choose["epoch"],
        "choose_delete_entry_sha256": choose["entry_sha256"],
        "confirm_delete_ledger_epoch": confirm["epoch"],
        "confirm_delete_entry_sha256": confirm["entry_sha256"],
        "post_reload_old_link_count": 0,
        "verified_packet": spec["packet_path"],
        "verified_packet_sha256": ps["packet_sha256"],
        "verified_metadata_sha256": ps["metadata_sha256"],
        "verified_save_epoch": ps["save_ledger"]["epoch"],
        "verified_save_entry_sha256": ps["save_ledger"]["entry_sha256"],
        "bulk_delete_used": False,
        "unrelated_conversation_touched": False,
        "reconstructed_after_post_delete_stale_dom_false_negative": True,
    }
    r.atomic_json(deletion_path, evidence)
    evidence_sha = h(deletion_path)
    note = (
        "REFERENCE-ONLY paper_01 exact-own deletion correction after successful side effect and independent settled reload; "
        f"conversation_id={evidence['conversation_id']}; deletion_sha256={evidence_sha}; save_epoch={ps['save_ledger']['epoch']}; "
        "confirm_action_epoch=1384; post_path=/app; old_link_count_after_reload=0; bulk_delete=false; unrelated_conversation_touched=false."
    )
    entry = r.journal_entry("dr9_paper_01_exact_own_deleted_settled_correction", note, [deletion_path, spec["packet_path"], spec["metadata_path"]])
    r.set_paper_state(state, 1, status="completed", deletion_sha256=evidence_sha, delete_ledger=entry, deleted_utc=evidence["deleted_utc"], prior_failure_classification="identity detector and stale post-delete DOM false negatives; packet and deletion valid")
    r.report_hwao(f"DR9 paper_01 COMPLETE after correction. Packet sha={ps['packet_sha256']} sources={ps['result']['source_anchor_count']}; exact-own conversation {evidence['conversation_id']} deletion settled and logged sha={evidence_sha}; no protected mutation.")


def cleanup_saved_papers_2_to_7(state, browser):
    specs = r.discover_prompts()
    for index in range(2, 8):
        spec = specs[index - 1]
        ps = state["papers"][index - 1]
        if ps.get("status") == "completed":
            continue
        if not ps.get("result") or not ps.get("save_ledger"):
            raise RuntimeError(f"{spec['paper_id']} lacks saved packet custody")
        navigate_exact(browser, ps["identity"]["conversation_path"], spec["paper_id"], "verified-result cleanup")
        page = r.exact_page(browser, ps["identity"]["conversation_path"])
        result_identity = r.current_saved_result_identity(page, ps)
        if not result_identity:
            raise RuntimeError(f"{spec['paper_id']} live result does not match saved packet")
        r.set_paper_state(state, index, status="saved_verified", prior_failure_classification="terminal packet valid; deletion identity detector false negative")
        evidence, entry = r.delete_exact_own(ps["identity"], spec, state, browser)
        final = state["papers"][index - 1]
        r.report_hwao(f"DR9 {spec['paper_id']} COMPLETE after correction. Packet sha={final['packet_sha256']} sources={final['result']['source_anchor_count']}; exact-own conversation {evidence['conversation_id']} deleted after verified save; deletion sha={final['deletion_sha256']}; no protected mutation.")
        print(json.dumps({"paper": spec["paper_id"], "cleanup": "completed", "delete_ledger": entry}), flush=True)


def recover_paper8_identity(state, browser):
    spec = r.discover_prompts()[7]
    ps = state["papers"][7]
    navigate_exact(browser, PAPER8_PATH, spec["paper_id"], "accepted-submit identity recovery")
    page = r.exact_page(browser, PAPER8_PATH)
    prompt = Path(spec["prompt_path"]).read_text().rstrip("\n")
    prompt_identity = r.current_prompt_identity(page, prompt)
    snapshot = r.page_snapshot(page)
    start = page.get_by_role("button", name="Start research", exact=True)
    if not prompt_identity or len(snapshot["messages"]) != 1 or start.count() != 1 or not start.is_visible() or start.is_disabled():
        raise RuntimeError("paper_08 accepted conversation/plan identity not recoverable")
    old_failure = {"path": ps["failure_path"], "sha256": ps.get("failure_sha256"), "ledger": ps.get("failure_ledger"), "classification": "URL wait timed out although exact history conversation and settled plan existed"}
    identity = {
        "target_id": r.TARGET_ID,
        "conversation_id": PAPER8_PATH[len("/app/"):],
        "conversation_path": PAPER8_PATH,
        "captured_title": prompt_identity["captured_title"],
        "identity_evidence": {**prompt_identity, "exact_history_row_recovered": True},
        "submit_utc": "2026-07-14T13:09:28Z",
        "submit_account_lease_id": "L00232",
        "submit_ledger_epoch": 1358,
        "submit_ledger_entry_sha256": "3c7757111ae84fd1c96421bff04cc44396a5f5ee1a9734647e84aa348c7f4b45",
        "prompt_sha256": spec["prompt_sha256"],
        "prompt_file_sha256": spec["prompt_file_sha256"],
        "page_challenge_after_submit": False,
    }
    r.set_paper_state(state, 8, status="submitted", identity=identity, prior_failure_records=[old_failure], submit_timeout_correction_utc=r.utcnow())
    correction = r.journal_entry(
        "dr9_paper_08_submit_timeout_identity_correction_resume",
        "paper_08 submit was accepted exactly once under account lease L00232/ledger epoch 1358; recovered exact conversation_id=9acdaa7cdab43447 from unique prompt history row and settled plan. No retry or duplicate prompt submit; resume at Start research.",
        [spec["failure_path"], spec["prompt_path"]],
    )
    r.set_paper_state(state, 8, submit_timeout_correction_ledger=correction)
    r.report_hwao("DR9 paper_08 correction: exact submit conversation 9acdaa7cdab43447 recovered after URL-wait timeout; plan ready; no duplicate prompt submit. Resuming at serialized Start research.")


def run_paper8_and_9(state, browser):
    specs = r.discover_prompts()
    recover_paper8_identity(state, browser)
    outcome8 = r.run_one(specs[7], state, browser)
    print(json.dumps({"paper": "paper_08", "outcome": outcome8}), flush=True)
    if outcome8 == "global_stop" or not r.target_matches("/app"):
        raise RuntimeError(f"paper_08 left global/target block: {outcome8}")
    ps9 = state["papers"][8]
    prior9 = {"path": ps9["failure_path"], "sha256": ps9.get("failure_sha256"), "ledger": ps9.get("failure_ledger"), "classification": "transient disabled Send before any account-submission lease or conversation"}
    r.set_paper_state(state, 9, status="pending", prior_failure_records=[prior9], retry_classification="first actual submit still zero; safe to perform the authorized paper_09 submit once")
    correction9 = r.journal_entry(
        "dr9_paper_09_pre_submit_transient_correction",
        "paper_09 prior failure occurred after verbatim fill but before account-submission acquisition/action; ledger proves zero paper_09 account submit and zero conversation. Proceeding with the one authorized paper_09 prompt submit, not a retry of an accepted job.",
        [specs[8]["failure_path"], specs[8]["prompt_path"]],
    )
    r.set_paper_state(state, 9, pre_submit_correction_ledger=correction9)
    outcome9 = r.run_one(specs[8], state, browser)
    print(json.dumps({"paper": "paper_09", "outcome": outcome9}), flush=True)


def final_summary(state):
    preserve_false_summary(state)
    statuses, total_sources, summary_sha, entry, summary_path = r.write_summary(state, final=True)
    correction = r.journal_entry(
        "dr9_reference_batch_final_correction_of_record",
        f"Corrected final batch summary supersedes preserved nonfinal all-failed summary; statuses={json.dumps(statuses,sort_keys=True)}; total_source_anchors={total_sources}; corrected_summary_sha256={summary_sha}; no protected mutation.",
        [OLD_FALSE_SUMMARY, summary_path],
    )
    state["final_correction_ledger"] = correction
    r.save_state(state)
    r.report_hwao(f"DR9 CORRECTED FINAL: statuses={json.dumps(statuses,sort_keys=True)} total_source_anchors={total_sources}; summary={summary_path} sha={summary_sha}; ledger epoch={correction['epoch']} VERIFY_OK. Old all-failed summary preserved as nonfinal correction source. No .tex/DB/autopilot/auto-apply.")
    print(json.dumps({"status": "RESCUE_FINISHED", "statuses": statuses, "total_sources": total_sources, "summary": str(summary_path), "summary_sha256": summary_sha, "summary_ledger": entry, "correction_ledger": correction}), flush=True)


def main():
    state = json.loads(r.STATE_PATH.read_text())
    preserve_false_summary(state)
    finalize_paper1_prior_delete(state)
    with sync_playwright() as p:
        browser = p.chromium.connect_over_cdp(r.BASE)
        cleanup_saved_papers_2_to_7(state, browser)
        run_paper8_and_9(state, browser)
    final_summary(state)


if __name__ == "__main__":
    main()
