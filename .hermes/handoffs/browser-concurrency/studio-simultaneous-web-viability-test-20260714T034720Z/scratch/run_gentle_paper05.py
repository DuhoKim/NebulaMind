import hashlib
import json
import subprocess
import sys
import time
from datetime import datetime, timedelta, timezone
from pathlib import Path
from urllib.parse import urlparse

sys.path.insert(0, "scratch")
import dr_manuscript_round1_review_runner as r
from playwright.sync_api import sync_playwright

PAPER_NUMBER = 5
GATE_PATH = Path("receipts/TORI_RELAY_DUHO_FRESH_GENTLE_PAPER05_20260715T022800Z.md").resolve()
GATE_SHA256 = "70e49b1dc5767baae65899649c05af8ee80e71b40b7cea21f334bfe6f644b316"
NOT_BEFORE = datetime.fromisoformat("2026-07-15T02:45:12+00:00")
PRECHECK_PATH = r.PACKET_DIR / "paper_05_round1_review_dr_packet.gentle_precheck.json"
PAPER03_HOLD = r.PACKET_DIR / "PAPER03_GENTLE_RESUME_HOLD_20260715T015326Z.json"
PAPER04_DELETION = r.PACKET_DIR / "paper_04_round1_review_dr_packet.deletion.json"
PAPER04_DELETION_SHA256 = "49e055b1b838ce245712dba2c1950b7f20c4f0bd46c0a1d0c2cd6cebc9ce87be"
PAPER04_ACCOUNT_LEASE = "L00457"
PAPER04_ACCOUNT_GRANT_EPOCH = 2660
HWAO_TARGET = "ge-mastermind:0.0"


def now_utc():
    return datetime.now(timezone.utc)


def report_hwao(text):
    tmux = "/opt/homebrew/bin/tmux"
    env = {k: v for k, v in __import__("os").environ.items() if k != "TMUX"}
    subprocess.run([tmux, "set-buffer", "--", r.normalized(text)], check=True, timeout=10, env=env)
    subprocess.run([tmux, "paste-buffer", "-t", HWAO_TARGET, "-d"], check=True, timeout=10, env=env)
    subprocess.run([tmux, "send-keys", "-t", HWAO_TARGET, "Enter"], check=True, timeout=10, env=env)


def freeze_for_redirect(client, holder, phase, actual_url):
    parsed = urlparse(actual_url)
    if (parsed.netloc == "www.google.com" and parsed.path.startswith("/sorry")) or parsed.netloc == "accounts.google.com":
        r.freeze_for_challenge(client, holder, "paper_05", phase)


def verify_static_gate(state, spec):
    if hashlib.sha256(GATE_PATH.read_bytes()).hexdigest() != GATE_SHA256:
        raise RuntimeError("fresh paper_05 gate hash mismatch")
    if not PAPER03_HOLD.is_file():
        raise RuntimeError("paper_03 held-deletion receipt absent")
    hold = json.loads(PAPER03_HOLD.read_text())
    if hold.get("paper_03", {}).get("exact_owned_deletion_completed") is not False:
        raise RuntimeError("paper_03 held-deletion boundary mismatch")
    if not PAPER04_DELETION.is_file() or r.sha_file(PAPER04_DELETION) != PAPER04_DELETION_SHA256:
        raise RuntimeError("paper_04 verified cleanup receipt mismatch")
    paper04 = state["papers"][3]
    if paper04.get("status") != "completed" or paper04.get("deletion_sha256") != PAPER04_DELETION_SHA256:
        raise RuntimeError("paper_04 completion state mismatch")

    paper = state["papers"][PAPER_NUMBER - 1]
    if paper.get("status") != "failed":
        raise RuntimeError(f"paper_05 expected failed state, got {paper.get('status')}")
    identity = paper.get("identity") or {}
    if identity.get("conversation_id") != "7c2cd635cd4b590d" or identity.get("conversation_path") != "/app/7c2cd635cd4b590d":
        raise RuntimeError("paper_05 exact-owned identity mismatch")
    if identity.get("prompt_sha256") != spec["prompt_sha256"]:
        raise RuntimeError("paper_05 prompt identity mismatch")
    failure = Path(paper["failure_path"])
    if not failure.is_file() or r.sha_file(failure) != paper.get("failure_sha256"):
        raise RuntimeError("paper_05 first immutable failure receipt mismatch")
    for output in (spec["packet_path"], spec["metadata_path"], spec["deletion_path"], PRECHECK_PATH):
        if Path(output).exists():
            raise RuntimeError(f"paper_05 fresh output already exists: {output}")
    return paper, identity


def wait_for_gate():
    while True:
        remaining = (NOT_BEFORE - now_utc()).total_seconds()
        if remaining <= 0:
            return
        print(json.dumps({"status": "WAITING_FOR_PAPER05_GATE", "not_before": NOT_BEFORE.isoformat().replace("+00:00", "Z"), "remaining_seconds": round(remaining, 1)}, sort_keys=True), flush=True)
        time.sleep(min(30, max(1, remaining)))


def verify_runtime_gate():
    broker_state = json.loads(Path("broker/live_state.json").read_text())
    live = [
        {"lease_id": row["lease_id"], "holder": row["holder"], "kind": row["kind"]}
        for row in broker_state.get("leases", {}).values()
        if row.get("state") == "live"
    ]
    if broker_state.get("frozen") or live:
        raise RuntimeError(f"broker not ready at paper_05 gate frozen={broker_state.get('frozen')} live={live}")
    ok, message = r.ledger.verify(r.LEDGER_PATH)
    if not ok:
        raise RuntimeError(f"ledger invalid before paper_05: {message}")
    entries = r.ledger.read_entries(r.LEDGER_PATH)
    account_grants = [row for row in entries if row.get("type") == "lease_granted" and row.get("payload", {}).get("kind") == "account-submission"]
    if not account_grants:
        raise RuntimeError("no prior account-submission custody available")
    last = account_grants[-1]
    if last["epoch"] != PAPER04_ACCOUNT_GRANT_EPOCH or last.get("payload", {}).get("lease_id") != PAPER04_ACCOUNT_LEASE:
        raise RuntimeError(f"account action occurred after paper_04; hold paper_05: last={last}")
    last_time = datetime.fromisoformat(last["utc"].replace("Z", "+00:00"))
    spacing_seconds = (now_utc() - last_time).total_seconds()
    if now_utc() < NOT_BEFORE or spacing_seconds < 20 * 60:
        raise RuntimeError(f"gentle spacing not met at paper_05 gate: {spacing_seconds:.1f} seconds")
    return message, last, spacing_seconds


def restore_exact_paper05(browser, identity):
    desired = identity["conversation_path"]
    record = r.target_record()
    if not record:
        raise RuntimeError("exact target record absent before paper_05 restore")
    if record["path"] == desired:
        return
    if record["path"] != "/app":
        raise RuntimeError(f"unexpected current route before paper_05 restore: {record['path']}")
    holder = "goru-paper05-gentle-restore"
    client = r.UDSClient(r.SOCK)
    lease = r.acquire_target(client, holder, "write", ttl=300, max_wait=20)
    try:
        page = r.exact_page(browser, record["path"])
        freeze_for_redirect(client, holder, "pre-restore redirect classification", page.url)
        if r.page_challenge(page):
            r.freeze_for_challenge(client, holder, "paper_05", "before exact-owned restore")
        r.check_action(client, lease, "paper_05 navigate from clean new-chat route to exact-owned route", record["path"], page)
        page.goto("https://gemini.google.com" + desired, wait_until="domcontentloaded", timeout=60000)
        page.wait_for_timeout(1800)
        freeze_for_redirect(client, holder, "post-restore redirect classification", page.url)
        if r.page_challenge(page):
            r.freeze_for_challenge(client, holder, "paper_05", "after exact-owned restore")
        parsed = urlparse(page.url)
        if parsed.scheme != "https" or parsed.netloc != "gemini.google.com" or parsed.path != desired:
            r.check_action(client, lease, "paper_05 fail closed unexpected restored destination", desired, page)
            raise r.TargetDrift(f"paper_05 restored destination mismatch: {parsed.netloc}{parsed.path}")
        r.check_action(client, lease, "paper_05 verify restored exact-owned route", desired, page)
    finally:
        r.release_lease(client, lease)
        client.close()


def classify_current(page, spec, identity):
    path = identity["conversation_path"]
    prompt = Path(spec["prompt_path"]).read_text().rstrip("\n")
    holder = "goru-paper05-gentle-classify"
    client = r.UDSClient(r.SOCK)
    lease = r.acquire_target(client, holder, "read", ttl=240, max_wait=20)
    try:
        freeze_for_redirect(client, holder, "classification redirect", page.url)
        if r.page_challenge(page):
            r.freeze_for_challenge(client, holder, "paper_05", "classification")
        r.check_action(client, lease, "paper_05 read-only exact-owned classification", path, page)
        snapshot = r.page_snapshot(page)
        starts = [control for control in snapshot["controls"] if control["label"] == "Start research"]
        lengths = [len(item["text"]) for item in snapshot["messages"]]
        last = snapshot["messages"][-1]["text"] if snapshot["messages"] else ""
        terminal = len(lengths) >= 3 and len(last) >= 2000 and not snapshot["stop"] and not snapshot["research"] and not snapshot["failure"]
        active_text = " ".join(item["text"] for item in snapshot["messages"])
        active = snapshot["stop"] or snapshot["research"] or "While I'm researching" in active_text or "Researching " in active_text or "Creating visuals for the report" in active_text or "Writing your report" in active_text
        prompt_identity = r.current_prompt_identity(page, prompt)
        plan = len(lengths) in (1, 2) and prompt_identity is not None and len(starts) == 1 and not starts[0]["disabled"] and not active and not terminal and not snapshot["failure"]
        if terminal:
            classification = "terminal_delayed_acceptance"
        elif active:
            classification = "research_active_delayed_acceptance"
        elif plan:
            classification = "unchanged_plan_one_fresh_start_allowed"
        else:
            classification = "unaccepted_or_ambiguous_hold"
        return classification, snapshot, starts, lengths, prompt_identity
    finally:
        r.release_lease(client, lease)
        client.close()


def main():
    specs = r.discover_prompts()
    state = r.load_or_create_state(specs)
    spec = specs[PAPER_NUMBER - 1]
    paper, identity = verify_static_gate(state, spec)
    wait_for_gate()
    ledger_before, last_account, spacing_seconds = verify_runtime_gate()

    try:
        with sync_playwright() as pw:
            browser = pw.chromium.connect_over_cdp(r.BASE)
            restore_exact_paper05(browser, identity)
            page = r.exact_page(browser, identity["conversation_path"])
            classification, snapshot, starts, lengths, prompt_identity = classify_current(page, spec, identity)
            precheck = {
                "status": "PAPER05_GENTLE_PRECHECK",
                "paper_id": "paper_05",
                "gate_path": str(GATE_PATH),
                "gate_sha256": GATE_SHA256,
                "not_before": NOT_BEFORE.isoformat().replace("+00:00", "Z"),
                "gate_time_requirement_met": now_utc() >= NOT_BEFORE,
                "yui_settled_before_paper05": True,
                "yui_account_submission_performed": False,
                "paper03_delete_retry_performed": False,
                "conversation_id": identity["conversation_id"],
                "conversation_path": identity["conversation_path"],
                "prompt_sha256": spec["prompt_sha256"],
                "first_failure_path": paper["failure_path"],
                "first_failure_sha256": paper["failure_sha256"],
                "classification_rule": "One or two assistant message-content nodes are plan-compatible only with exact route, exact prompt identity, exactly one enabled Start, and zero active/terminal/failure/challenge signals.",
                "classification": classification,
                "challenge": snapshot["challenge"],
                "message_count": len(lengths),
                "message_lengths": lengths,
                "start_controls": starts,
                "research": snapshot["research"],
                "stop": snapshot["stop"],
                "failure": snapshot["failure"],
                "prompt_identity": prompt_identity,
                "last_account_submission_grant_epoch": last_account["epoch"],
                "last_account_submission_grant_utc": last_account["utc"],
                "last_account_submission_lease_id": last_account["payload"]["lease_id"],
                "spacing_seconds_at_precheck": spacing_seconds,
                "spacing_requirement_met": True,
                "ledger_verify_before": ledger_before,
                "new_prompt_send_allowed": False,
                "fresh_start_actions_allowed": 1 if classification == "unchanged_plan_one_fresh_start_allowed" else 0,
            }
            r.atomic_json(PRECHECK_PATH, precheck)
            precheck_sha = r.sha_file(PRECHECK_PATH)

            if classification == "unaccepted_or_ambiguous_hold":
                r.set_paper_state(state, PAPER_NUMBER, status="failed", gentle_precheck_path=str(PRECHECK_PATH), gentle_precheck_sha256=precheck_sha, gentle_classification=classification)
                report_hwao(f"PAPER_05 GENTLE BACKOFF before submit: exact route was ambiguous; no prompt Send and no Start action performed. Hold receipt {PRECHECK_PATH} sha {precheck_sha}. No paper_06.")
                print(json.dumps({"status": "PAPER05_GENTLE_BACKOFF_NO_SUBMIT", "precheck": str(PRECHECK_PATH), "precheck_sha256": precheck_sha, "ledger_verify": ledger_before}, sort_keys=True))
                browser.close()
                return 2

            fresh_start = False
            if classification == "unchanged_plan_one_fresh_start_allowed":
                r.set_paper_state(state, PAPER_NUMBER, status="submitted", gentle_precheck_path=str(PRECHECK_PATH), gentle_precheck_sha256=precheck_sha, gentle_classification=classification, gentle_gate_sha256=GATE_SHA256)
                r.start_research(identity, spec, state, browser)
                fresh_start = True
                current = state["papers"][PAPER_NUMBER - 1]
                report_hwao(f"PAPER_05 GENTLE SUBMIT SETTLED: one broker-serialized Start accepted; account lease {current.get('research_start_account_lease_id')}; UTC {current.get('research_start_utc')}. No prompt resend. No paper_06 is authorized.")
            else:
                recovered_mode = "terminal" if classification.startswith("terminal") else "active"
                r.set_paper_state(state, PAPER_NUMBER, status="researching", research_start_mode=f"delayed_acceptance_recovered_{recovered_mode}", gentle_precheck_path=str(PRECHECK_PATH), gentle_precheck_sha256=precheck_sha, gentle_classification=classification, gentle_gate_sha256=GATE_SHA256, gentle_new_submit_performed=False)
                report_hwao(f"PAPER_05 GENTLE SUBMIT ALREADY SETTLED: pre-gate Start was delayed-accepted ({classification}); no new prompt or Start action. Goru continues read-only result custody. No paper_06.")

            stable, result_sha = r.poll_terminal(identity, spec, state, browser)
            metadata, save_entry = r.save_packet(stable, result_sha, identity, spec, state)
            try:
                _, delete_entry = r.delete_exact_own(identity, spec, state, browser)
                cleanup_status = "exact_owned_deleted"
                deletion_sha = state["papers"][PAPER_NUMBER - 1].get("deletion_sha256")
                delete_epoch = delete_entry["epoch"]
            except Exception as cleanup_exc:
                cleanup_status = "saved_verified_cleanup_hold"
                deletion_sha = None
                delete_epoch = None
                r.set_paper_state(state, PAPER_NUMBER, status="saved_verified", cleanup_hold_error=f"{type(cleanup_exc).__name__}: {cleanup_exc}", cleanup_hold_utc=r.utcnow())
                report_hwao(f"PAPER_05 saved/verified but exact-own cleanup held: {type(cleanup_exc).__name__}: {str(cleanup_exc)[:400]}. No retry and no paper_06.")
            browser.close()

        ok, ledger_after = r.ledger.verify(r.LEDGER_PATH)
        if not ok:
            raise RuntimeError(f"ledger invalid after paper_05: {ledger_after}")
        final = json.loads(r.STATE_PATH.read_text())["papers"][PAPER_NUMBER - 1]
        next_not_before = (now_utc() + timedelta(minutes=25)).isoformat().replace("+00:00", "Z")
        result = {
            "status": "GORU_GENTLE_PAPER05_COMPLETE" if cleanup_status == "exact_owned_deleted" else "GORU_GENTLE_PAPER05_SAVED_VERIFIED_CLEANUP_HOLD",
            "paper_id": "paper_05",
            "fresh_start_performed": fresh_start,
            "new_prompt_send_performed": False,
            "classification": classification,
            "packet_path": spec["packet_path"],
            "packet_sha256": final["packet_sha256"],
            "result_chars": metadata["result_chars"],
            "result_sha256": metadata["result_text_sha256"],
            "save_epoch": save_entry["epoch"],
            "cleanup_status": cleanup_status,
            "deletion_sha256": deletion_sha,
            "delete_epoch": delete_epoch,
            "ledger_verify": ledger_after,
            "next_submit_not_before": next_not_before,
            "next_action": "HOLD; no paper_06 action is authorized",
        }
        print(json.dumps(result, sort_keys=True))
        return 0
    except r.GlobalChallengeStop as exc:
        with __import__("contextlib").suppress(Exception):
            r.write_failure(spec, state, exc, identity)
        report_hwao(f"PAPER_05 CHALLENGE STOP/FROZEN: {exc}. Never interact. Wake Duho. No retry and no paper_06.")
        raise
    except r.PaperFailure as exc:
        with __import__("contextlib").suppress(Exception):
            r.write_failure(spec, state, exc, identity)
        report_hwao(f"PAPER_05 GENTLE FIRST UNACCEPTED/SOFT-THROTTLE BACKOFF: {exc}. No retry and no paper_06.")
        print(json.dumps({"status": "PAPER05_GENTLE_BACKOFF_NO_RETRY", "error": str(exc), "precheck": str(PRECHECK_PATH)}, sort_keys=True))
        return 2
    except Exception as exc:
        with __import__("contextlib").suppress(Exception):
            report_hwao(f"PAPER_05 TECHNICAL HOLD before/after account action: {type(exc).__name__}: {str(exc)[:500]}. No paper_06. Inspect ledger before any fresh disposition.")
        raise


if __name__ == "__main__":
    raise SystemExit(main())
