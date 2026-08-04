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

PAPERS = (6, 7, 8)
GATE_PATH = Path("receipts/TORI_RELAY_DUHO_GENTLE_AUTO_06_08_20260715T030511Z.md").resolve()
GATE_SHA256 = "7c7981f2d0c35c5205e13a1150d13c575ebd75acdca3452fbd328cf36d7c156b"
SEQUENCE_STATE_PATH = r.PACKET_DIR / "ROUND1_GENTLE_AUTO_06_08_STATE.json"
FIRST_BASE_GATE = datetime.fromisoformat("2026-07-15T03:19:31.772367+00:00")
MIN_START_SPACING = timedelta(minutes=30)
PAPER03_HOLD = r.PACKET_DIR / "PAPER03_GENTLE_RESUME_HOLD_20260715T015326Z.json"
PAPER05_DELETION = r.PACKET_DIR / "paper_05_round1_review_dr_packet.deletion.json"
PAPER05_DELETION_SHA256 = "9115716a5b4084c235e9a0694d51a3df191f984a5f1b2cf77f9cc5a57585a829"
PAPER05_ACCOUNT_LEASE = "L00467"
PAPER05_ACCOUNT_GRANT_EPOCH = 2733
HWAO_TARGET = "ge-mastermind:0.0"
EXPECTED = {
    6: {
        "conversation_id": "61e26df7c80b4126",
        "conversation_path": "/app/61e26df7c80b4126",
        "failure_sha256": "1359ff0b9ed7224af28f91a8e06e9da2aff3313ece48d79658b5985ab807e7a1",
    },
    7: {
        "conversation_id": "de87d3319efdfa0b",
        "conversation_path": "/app/de87d3319efdfa0b",
        "failure_sha256": "e183c0eb285fb0d2a274cff6f6963bf65d315816641346daefcd288052f67ee7",
    },
    8: {
        "conversation_id": "96b6513b7a1380d2",
        "conversation_path": "/app/96b6513b7a1380d2",
        "failure_sha256": "02e8c6c6d219d0cc5bc759ee03e459cdad78e6d376b2621657be735ed0b5ec7d",
    },
}


class SequenceHold(RuntimeError):
    pass


def now_utc():
    return datetime.now(timezone.utc)


def iso(value):
    return value.isoformat().replace("+00:00", "Z")


def report_hwao(text):
    tmux = "/opt/homebrew/bin/tmux"
    env = {k: v for k, v in __import__("os").environ.items() if k != "TMUX"}
    subprocess.run([tmux, "set-buffer", "--", r.normalized(text)], check=True, timeout=10, env=env)
    subprocess.run([tmux, "paste-buffer", "-t", HWAO_TARGET, "-d"], check=True, timeout=10, env=env)
    subprocess.run([tmux, "send-keys", "-t", HWAO_TARGET, "Enter"], check=True, timeout=10, env=env)


def write_sequence_state(**updates):
    if SEQUENCE_STATE_PATH.exists():
        state = json.loads(SEQUENCE_STATE_PATH.read_text())
    else:
        state = {
            "status": "AUTHORIZED_WAIT",
            "gate_path": str(GATE_PATH),
            "gate_sha256": GATE_SHA256,
            "papers": {str(number): {"status": "pending"} for number in PAPERS},
            "paper03_delete_retry_performed": False,
            "re_research_or_round2_authorized": False,
        }
    state.update(updates)
    state["updated_utc"] = iso(now_utc())
    r.atomic_json(SEQUENCE_STATE_PATH, state)
    return state


def update_paper_sequence(number, **updates):
    state = json.loads(SEQUENCE_STATE_PATH.read_text()) if SEQUENCE_STATE_PATH.exists() else write_sequence_state()
    row = dict(state["papers"][str(number)])
    row.update(updates)
    state["papers"][str(number)] = row
    state["updated_utc"] = iso(now_utc())
    r.atomic_json(SEQUENCE_STATE_PATH, state)
    return state


def freeze_for_redirect(client, holder, paper_id, phase, actual_url):
    parsed = urlparse(actual_url)
    if (parsed.netloc == "www.google.com" and parsed.path.startswith("/sorry")) or parsed.netloc == "accounts.google.com":
        r.freeze_for_challenge(client, holder, paper_id, phase)


def live_leases():
    broker_state = json.loads(Path("broker/live_state.json").read_text())
    live = [
        {"lease_id": row["lease_id"], "holder": row["holder"], "kind": row["kind"]}
        for row in broker_state.get("leases", {}).values()
        if row.get("state") == "live"
    ]
    return broker_state, live


def ledger_snapshot():
    ok, message = r.ledger.verify(r.LEDGER_PATH)
    if not ok:
        raise SequenceHold(f"ledger invalid: {message}")
    entries = r.ledger.read_entries(r.LEDGER_PATH)
    account_grants = [
        row
        for row in entries
        if row.get("type") == "lease_granted"
        and row.get("payload", {}).get("kind") == "account-submission"
    ]
    return message, entries, account_grants


def verify_static_gate(state, specs):
    if hashlib.sha256(GATE_PATH.read_bytes()).hexdigest() != GATE_SHA256:
        raise SequenceHold("fresh 06-08 auto-sequence gate hash mismatch")
    if not PAPER03_HOLD.is_file():
        raise SequenceHold("paper_03 held-deletion receipt absent")
    hold = json.loads(PAPER03_HOLD.read_text())
    if hold.get("paper_03", {}).get("exact_owned_deletion_completed") is not False:
        raise SequenceHold("paper_03 held-deletion boundary mismatch")
    if not PAPER05_DELETION.is_file() or r.sha_file(PAPER05_DELETION) != PAPER05_DELETION_SHA256:
        raise SequenceHold("paper_05 verified cleanup receipt mismatch")
    paper05 = state["papers"][4]
    if paper05.get("status") != "completed" or paper05.get("deletion_sha256") != PAPER05_DELETION_SHA256:
        raise SequenceHold("paper_05 completion state mismatch")

    for number in PAPERS:
        spec = specs[number - 1]
        paper = state["papers"][number - 1]
        expected = EXPECTED[number]
        identity = paper.get("identity") or {}
        if paper.get("status") != "failed":
            raise SequenceHold(f"paper_{number:02d} expected failed state, got {paper.get('status')}")
        if identity.get("conversation_id") != expected["conversation_id"] or identity.get("conversation_path") != expected["conversation_path"]:
            raise SequenceHold(f"paper_{number:02d} exact-owned identity mismatch")
        if identity.get("prompt_sha256") != spec["prompt_sha256"]:
            raise SequenceHold(f"paper_{number:02d} prompt identity mismatch")
        failure = Path(paper["failure_path"])
        if not failure.is_file() or r.sha_file(failure) != expected["failure_sha256"] or paper.get("failure_sha256") != expected["failure_sha256"]:
            raise SequenceHold(f"paper_{number:02d} first immutable failure receipt mismatch")
        precheck_path = r.PACKET_DIR / f"paper_{number:02d}_round1_review_dr_packet.gentle_precheck.json"
        for output in (spec["packet_path"], spec["metadata_path"], spec["deletion_path"], precheck_path):
            if Path(output).exists():
                raise SequenceHold(f"paper_{number:02d} fresh output already exists: {output}")
    message, _, account_grants = ledger_snapshot()
    last = account_grants[-1]
    last_is_paper05 = last["epoch"] == PAPER05_ACCOUNT_GRANT_EPOCH and last.get("payload", {}).get("lease_id") == PAPER05_ACCOUNT_LEASE
    last_is_presequence_yui = last["epoch"] > PAPER05_ACCOUNT_GRANT_EPOCH and "yui" in last.get("payload", {}).get("holder", "").lower()
    if not (last_is_paper05 or last_is_presequence_yui):
        raise SequenceHold(f"unexpected account submit before sequence authorization: {last}")
    return message


def wait_for_paper06_gate():
    while True:
        broker_state, live = live_leases()
        if broker_state.get("frozen"):
            raise SequenceHold("broker frozen while waiting for paper_06")
        ledger_message, _, account_grants = ledger_snapshot()
        last = account_grants[-1]
        holder = last.get("payload", {}).get("holder", "")
        if last["epoch"] == PAPER05_ACCOUNT_GRANT_EPOCH and last.get("payload", {}).get("lease_id") == PAPER05_ACCOUNT_LEASE:
            effective_gate = FIRST_BASE_GATE
            account_note = "paper_05 remains the last account submit"
        elif last["epoch"] > PAPER05_ACCOUNT_GRANT_EPOCH and "yui" in holder.lower():
            last_time = datetime.fromisoformat(last["utc"].replace("Z", "+00:00"))
            effective_gate = max(FIRST_BASE_GATE, last_time + MIN_START_SPACING)
            account_note = f"Yui pre-sequence submit {last['payload']['lease_id']} at {last['utc']}"
        else:
            raise SequenceHold(f"unexpected non-Yui account action before paper_06: {last}")

        yui_live = [row for row in live if "yui" in row["holder"].lower()]
        other_live = [row for row in live if "yui" not in row["holder"].lower()]
        if other_live:
            raise SequenceHold(f"unexpected non-Yui live leases before paper_06: {other_live}")
        remaining = (effective_gate - now_utc()).total_seconds()
        write_sequence_state(
            status="WAITING_PAPER06_GATE",
            effective_paper06_not_before=iso(effective_gate),
            pre_sequence_account_note=account_note,
            yui_live_leases=yui_live,
            ledger_verify=ledger_message,
        )
        if not yui_live and remaining <= 0:
            return effective_gate, last
        print(json.dumps({
            "status": "WAITING_PAPER06_GATE",
            "effective_not_before": iso(effective_gate),
            "remaining_seconds": round(max(0, remaining), 1),
            "yui_live": yui_live,
            "account_note": account_note,
        }, sort_keys=True), flush=True)
        time.sleep(30)


def wait_between_papers(not_before, expected_account_lease, expected_account_epoch, next_number):
    while True:
        broker_state, live = live_leases()
        if broker_state.get("frozen"):
            raise SequenceHold(f"broker frozen while waiting for paper_{next_number:02d}")
        if live:
            raise SequenceHold(f"unexpected live lease between sequence papers: {live}")
        ledger_message, _, account_grants = ledger_snapshot()
        last = account_grants[-1]
        if last["epoch"] != expected_account_epoch or last.get("payload", {}).get("lease_id") != expected_account_lease:
            raise SequenceHold(f"intervening account action before paper_{next_number:02d}: {last}")
        remaining = (not_before - now_utc()).total_seconds()
        write_sequence_state(
            status=f"WAITING_PAPER{next_number:02d}_GATE",
            next_paper=next_number,
            next_not_before=iso(not_before),
            ledger_verify=ledger_message,
        )
        if remaining <= 0:
            return
        print(json.dumps({
            "status": f"WAITING_PAPER{next_number:02d}_GATE",
            "not_before": iso(not_before),
            "remaining_seconds": round(remaining, 1),
        }, sort_keys=True), flush=True)
        time.sleep(min(30, max(1, remaining)))


def restore_exact(browser, identity, number):
    desired = identity["conversation_path"]
    record = r.target_record()
    if not record:
        raise SequenceHold(f"exact target record absent before paper_{number:02d} restore")
    if record["path"] == desired:
        return
    if record["path"] != "/app":
        raise SequenceHold(f"unexpected current route before paper_{number:02d} restore: {record['path']}")
    paper_id = f"paper_{number:02d}"
    holder = f"goru-{paper_id}-gentle-restore"
    client = r.UDSClient(r.SOCK)
    lease = r.acquire_target(client, holder, "write", ttl=300, max_wait=20)
    try:
        page = r.exact_page(browser, record["path"])
        freeze_for_redirect(client, holder, paper_id, "pre-restore redirect classification", page.url)
        if r.page_challenge(page):
            r.freeze_for_challenge(client, holder, paper_id, "before exact-owned restore")
        r.check_action(client, lease, f"{paper_id} navigate from clean new-chat route to exact-owned route", record["path"], page)
        page.goto("https://gemini.google.com" + desired, wait_until="domcontentloaded", timeout=60000)
        page.wait_for_timeout(1800)
        freeze_for_redirect(client, holder, paper_id, "post-restore redirect classification", page.url)
        if r.page_challenge(page):
            r.freeze_for_challenge(client, holder, paper_id, "after exact-owned restore")
        parsed = urlparse(page.url)
        if parsed.scheme != "https" or parsed.netloc != "gemini.google.com" or parsed.path != desired:
            r.check_action(client, lease, f"{paper_id} fail closed unexpected restored destination", desired, page)
            raise r.TargetDrift(f"{paper_id} restored destination mismatch: {parsed.netloc}{parsed.path}")
        r.check_action(client, lease, f"{paper_id} verify restored exact-owned route", desired, page)
    finally:
        r.release_lease(client, lease)
        client.close()


def classify_current(page, spec, identity, number):
    paper_id = f"paper_{number:02d}"
    path = identity["conversation_path"]
    prompt = Path(spec["prompt_path"]).read_text().rstrip("\n")
    holder = f"goru-{paper_id}-gentle-classify"
    client = r.UDSClient(r.SOCK)
    lease = r.acquire_target(client, holder, "read", ttl=240, max_wait=20)
    try:
        freeze_for_redirect(client, holder, paper_id, "classification redirect", page.url)
        if r.page_challenge(page):
            r.freeze_for_challenge(client, holder, paper_id, "classification")
        r.check_action(client, lease, f"{paper_id} read-only exact-owned classification", path, page)
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


def find_account_grant(lease_id):
    _, _, account_grants = ledger_snapshot()
    matches = [row for row in account_grants if row.get("payload", {}).get("lease_id") == lease_id]
    if len(matches) != 1:
        raise SequenceHold(f"expected exactly one account grant for {lease_id}, got {len(matches)}")
    return matches[0]


def process_paper(browser, specs, manuscript_state, number, gate_not_before):
    spec = specs[number - 1]
    paper = manuscript_state["papers"][number - 1]
    identity = paper["identity"]
    paper_id = f"paper_{number:02d}"
    precheck_path = r.PACKET_DIR / f"{paper_id}_round1_review_dr_packet.gentle_precheck.json"

    broker_state, live = live_leases()
    if broker_state.get("frozen") or live:
        raise SequenceHold(f"broker not ready before {paper_id}: frozen={broker_state.get('frozen')} live={live}")
    ledger_before, _, account_grants = ledger_snapshot()
    last_account = account_grants[-1]

    restore_exact(browser, identity, number)
    page = r.exact_page(browser, identity["conversation_path"])
    classification, snapshot, starts, lengths, prompt_identity = classify_current(page, spec, identity, number)
    precheck = {
        "status": f"PAPER{number:02d}_GENTLE_AUTO_PRECHECK",
        "paper_id": paper_id,
        "gate_path": str(GATE_PATH),
        "gate_sha256": GATE_SHA256,
        "gate_not_before": iso(gate_not_before),
        "gate_requirement_met": now_utc() >= gate_not_before,
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
        "ledger_verify_before": ledger_before,
        "new_prompt_send_allowed": False,
        "fresh_start_actions_allowed": 1 if classification == "unchanged_plan_one_fresh_start_allowed" else 0,
    }
    r.atomic_json(precheck_path, precheck)
    precheck_sha = r.sha_file(precheck_path)
    update_paper_sequence(number, status="prechecked", precheck_path=str(precheck_path), precheck_sha256=precheck_sha, classification=classification)

    if classification == "unaccepted_or_ambiguous_hold":
        r.set_paper_state(manuscript_state, number, status="failed", gentle_precheck_path=str(precheck_path), gentle_precheck_sha256=precheck_sha, gentle_classification=classification)
        raise SequenceHold(f"{paper_id} exact route ambiguous before submit; no Send and no Start")

    fresh_start = False
    account_grant = last_account
    if classification == "unchanged_plan_one_fresh_start_allowed":
        r.set_paper_state(manuscript_state, number, status="submitted", gentle_precheck_path=str(precheck_path), gentle_precheck_sha256=precheck_sha, gentle_classification=classification, gentle_gate_sha256=GATE_SHA256)
        try:
            r.start_research(identity, spec, manuscript_state, browser)
        except (r.GlobalChallengeStop, r.PaperFailure) as exc:
            with __import__("contextlib").suppress(Exception):
                r.write_failure(spec, manuscript_state, exc, identity)
            raise
        fresh_start = True
        current = manuscript_state["papers"][number - 1]
        account_grant = find_account_grant(current["research_start_account_lease_id"])
        update_paper_sequence(number, status="researching", fresh_start_performed=True, account_lease_id=account_grant["payload"]["lease_id"], account_grant_epoch=account_grant["epoch"], account_grant_utc=account_grant["utc"])
        report_hwao(f"{paper_id.upper()} AUTO-SEQUENCE START SETTLED: exactly one broker-serialized Start accepted at {account_grant['utc']} under {account_grant['payload']['lease_id']}; no prompt resend. Yui remains held. Goru continues read-only custody; no per-paper dispatch needed.")
    else:
        recovered_mode = "terminal" if classification.startswith("terminal") else "active"
        r.set_paper_state(manuscript_state, number, status="researching", research_start_mode=f"delayed_acceptance_recovered_{recovered_mode}", gentle_precheck_path=str(precheck_path), gentle_precheck_sha256=precheck_sha, gentle_classification=classification, gentle_gate_sha256=GATE_SHA256, gentle_new_submit_performed=False)
        update_paper_sequence(number, status="researching_recovered", fresh_start_performed=False)
        report_hwao(f"{paper_id.upper()} AUTO-SEQUENCE ALREADY SETTLED ({classification}); no new prompt or Start. Goru continues read-only custody. Yui remains held.")

    try:
        stable, result_sha = r.poll_terminal(identity, spec, manuscript_state, browser)
    except (r.GlobalChallengeStop, r.PaperFailure) as exc:
        with __import__("contextlib").suppress(Exception):
            r.write_failure(spec, manuscript_state, exc, identity)
        raise
    metadata, save_entry = r.save_packet(stable, result_sha, identity, spec, manuscript_state)
    try:
        _, delete_entry = r.delete_exact_own(identity, spec, manuscript_state, browser)
    except Exception as cleanup_exc:
        r.set_paper_state(manuscript_state, number, status="saved_verified", cleanup_hold_error=f"{type(cleanup_exc).__name__}: {cleanup_exc}", cleanup_hold_utc=r.utcnow())
        raise SequenceHold(f"{paper_id} saved/verified but exact-own cleanup held: {type(cleanup_exc).__name__}: {cleanup_exc}")

    ok, ledger_after = r.ledger.verify(r.LEDGER_PATH)
    if not ok:
        raise SequenceHold(f"ledger invalid after {paper_id}: {ledger_after}")
    final = json.loads(r.STATE_PATH.read_text())["papers"][number - 1]
    completion = {
        "status": "completed",
        "fresh_start_performed": fresh_start,
        "new_prompt_send_performed": False,
        "classification": classification,
        "packet_path": spec["packet_path"],
        "packet_sha256": final["packet_sha256"],
        "metadata_sha256": final["metadata_sha256"],
        "result_chars": metadata["result_chars"],
        "result_sha256": metadata["result_text_sha256"],
        "save_epoch": save_entry["epoch"],
        "deletion_sha256": final["deletion_sha256"],
        "delete_epoch": delete_entry["epoch"],
        "ledger_verify": ledger_after,
    }
    if fresh_start:
        completion.update({
            "account_lease_id": account_grant["payload"]["lease_id"],
            "account_grant_epoch": account_grant["epoch"],
            "account_grant_utc": account_grant["utc"],
        })
    update_paper_sequence(number, **completion)
    report_hwao(f"{paper_id.upper()} AUTO-SEQUENCE COMPLETE: packet {final['packet_sha256']}; exact-own cleanup {final['deletion_sha256']}; ledger {ledger_after}. " + ("Waiting for the next 30-minute Start gate; no fresh dispatch needed." if number < 8 else "ROUND-1 03-08 COMPLETE. HOLD: no re-research or round-2 gate."))
    return completion, account_grant


def main():
    specs = r.discover_prompts()
    manuscript_state = r.load_or_create_state(specs)
    ledger_before = verify_static_gate(manuscript_state, specs)
    write_sequence_state(status="AUTHORIZED_WAIT", ledger_verify=ledger_before, first_base_gate=iso(FIRST_BASE_GATE))

    try:
        first_gate, previous_account = wait_for_paper06_gate()
        current_gate = first_gate
        results = []
        with sync_playwright() as pw:
            browser = pw.chromium.connect_over_cdp(r.BASE)
            for index, number in enumerate(PAPERS):
                if number > 6:
                    wait_between_papers(current_gate, previous_account["payload"]["lease_id"], previous_account["epoch"], number)
                manuscript_state = json.loads(r.STATE_PATH.read_text())
                result, account_grant = process_paper(browser, specs, manuscript_state, number, current_gate)
                results.append(result)
                if result["fresh_start_performed"]:
                    start_time = datetime.fromisoformat(account_grant["utc"].replace("Z", "+00:00"))
                    current_gate = start_time + MIN_START_SPACING
                    previous_account = account_grant
                else:
                    current_gate = now_utc() + MIN_START_SPACING
                if number < 8:
                    write_sequence_state(status=f"WAITING_PAPER{number + 1:02d}_GATE", next_paper=number + 1, next_not_before=iso(current_gate))
            browser.close()

        ledger_final, entries, account_grants = ledger_snapshot()
        account_after_gate = [row for row in account_grants if row["epoch"] > PAPER05_ACCOUNT_GRANT_EPOCH]
        final_state = write_sequence_state(
            status="COMPLETE_HOLD_AFTER_PAPER08",
            completed_papers=list(PAPERS),
            ledger_verify=ledger_final,
            ledger_entries=len(entries),
            account_grants_after_paper05=[{
                "epoch": row["epoch"],
                "utc": row["utc"],
                "holder": row["payload"]["holder"],
                "lease_id": row["payload"]["lease_id"],
            } for row in account_after_gate],
            next_action="HOLD; no re-research or round-2 Deep Research until a fresh Duho gate",
        )
        print(json.dumps({
            "status": final_state["status"],
            "papers": final_state["papers"],
            "ledger_verify": ledger_final,
            "next_action": final_state["next_action"],
        }, sort_keys=True))
        return 0
    except r.GlobalChallengeStop as exc:
        write_sequence_state(status="CHALLENGE_STOP_FROZEN", error=f"{type(exc).__name__}: {exc}", next_action="HOLD; Hwao wakes Duho; never interact")
        report_hwao(f"06-08 AUTO-SEQUENCE CHALLENGE STOP/FROZEN: {exc}. Never interact. Wake Duho. No retry, no later paper, no re-research/round2.")
        raise
    except r.PaperFailure as exc:
        write_sequence_state(status="FIRST_UNACCEPTED_STOP_NO_RETRY", error=f"{type(exc).__name__}: {exc}", next_action="HOLD; no retry and no later paper")
        report_hwao(f"06-08 AUTO-SEQUENCE FIRST UNACCEPTED/SOFT-THROTTLE BACKOFF: {exc}. No retry; no later paper; no re-research/round2.")
        print(json.dumps({"status": "FIRST_UNACCEPTED_STOP_NO_RETRY", "error": str(exc)}, sort_keys=True))
        return 2
    except SequenceHold as exc:
        write_sequence_state(status="TECHNICAL_OR_CUSTODY_HOLD", error=f"{type(exc).__name__}: {exc}", next_action="HOLD; no retry and no later paper")
        report_hwao(f"06-08 AUTO-SEQUENCE HOLD: {exc}. No retry or later paper. Inspect custody/ledger; no re-research/round2.")
        print(json.dumps({"status": "TECHNICAL_OR_CUSTODY_HOLD", "error": str(exc)}, sort_keys=True))
        return 2
    except Exception as exc:
        write_sequence_state(status="UNEXPECTED_HOLD", error=f"{type(exc).__name__}: {exc}", next_action="HOLD; no retry and no later paper")
        with __import__("contextlib").suppress(Exception):
            report_hwao(f"06-08 AUTO-SEQUENCE UNEXPECTED HOLD: {type(exc).__name__}: {str(exc)[:500]}. No retry or later paper; no re-research/round2.")
        raise


if __name__ == "__main__":
    raise SystemExit(main())
