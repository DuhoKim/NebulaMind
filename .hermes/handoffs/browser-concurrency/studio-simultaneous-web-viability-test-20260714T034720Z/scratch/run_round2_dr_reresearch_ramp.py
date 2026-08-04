import hashlib
import json
import os
import subprocess
import sys
import time
from contextlib import suppress
from datetime import datetime, timedelta, timezone
from pathlib import Path

sys.path.insert(0, "scratch")
import dr_manuscript_round2_reresearch_runner as r
from playwright.sync_api import sync_playwright

PAPERS = tuple(range(1, 10))
GAP_LADDER_MINUTES = (30, 20, 15, 10, 8)
GATE_PATH = Path("receipts/DUHO_MAX_CONSUMPTION_20260715.md").resolve()
GATE_SHA256 = "a0cf2c39c219a1e2df531dbb1667a0e106e43362f6684c9791272bb5bf90604c"
PROMPT_MANIFEST = r.PROMPT_DIR / "ROUND2_DR_RERESEARCH_PROMPTS.json"
PROMPT_MANIFEST_SHA256 = "8442b235c12f1b1e3da4ccfb2ebf68c7c41d27e2455c1b060c2c1ded343865b7"
RAMP_STATE_PATH = r.PACKET_DIR / "ROUND2_DR_RERESEARCH_RAMP_STATE.json"
ROUND1_SEQUENCE_FINAL = Path("/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/dr-revised-20260714/round1/dr-review-packets/ROUND1_GENTLE_AUTO_06_08_STATE.json")
ROUND1_SEQUENCE_FINAL_SHA256 = "768a107f2ec1e500b85d1716779a70d034c7357da20948694adc1ba9470d9b9d"
HWAO_TARGET = "ge-mastermind:0.0"


class RampHold(RuntimeError):
    pass


class SoftThrottleHold(RuntimeError):
    pass


def now_utc():
    return datetime.now(timezone.utc)


def iso(value):
    return value.isoformat().replace("+00:00", "Z")


def parse_utc(value):
    return datetime.fromisoformat(value.replace("Z", "+00:00"))


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def report_hwao(text):
    tmux = "/opt/homebrew/bin/tmux"
    env = {key: value for key, value in os.environ.items() if key != "TMUX"}
    subprocess.run([tmux, "set-buffer", "--", r.normalized(text)], check=True, timeout=10, env=env)
    subprocess.run([tmux, "paste-buffer", "-t", HWAO_TARGET, "-d"], check=True, timeout=10, env=env)
    subprocess.run([tmux, "send-keys", "-t", HWAO_TARGET, "Enter"], check=True, timeout=10, env=env)


def ledger_snapshot():
    ok, message = r.ledger.verify(r.LEDGER_PATH)
    if not ok:
        raise RampHold(f"ledger invalid: {message}")
    entries = r.ledger.read_entries(r.LEDGER_PATH)
    account_grants = [
        row
        for row in entries
        if row.get("type") == "lease_granted"
        and row.get("payload", {}).get("kind") == "account-submission"
    ]
    return message, entries, account_grants


def broker_snapshot():
    state = json.loads(Path("broker/live_state.json").read_text())
    live = [
        {
            "lease_id": row.get("lease_id"),
            "holder": row.get("holder"),
            "kind": row.get("kind"),
            "scope": row.get("scope"),
        }
        for row in state.get("leases", {}).values()
        if row.get("state") == "live"
    ]
    return state, live


def goru_start_grants(account_grants):
    return [
        row
        for row in account_grants
        if row.get("payload", {}).get("holder", "").lower().startswith("goru-")
        and "-start" in row.get("payload", {}).get("holder", "").lower()
    ]


def find_account_grant(lease_id):
    _, _, grants = ledger_snapshot()
    matches = [row for row in grants if row.get("payload", {}).get("lease_id") == lease_id]
    if len(matches) != 1:
        raise RampHold(f"expected one account grant for {lease_id}, found {len(matches)}")
    return matches[0]


def base_ramp_state(first_prior_grant, first_gate):
    return {
        "batch_id": "DR_RERESEARCH_ROUND2_RAMP_20260715",
        "status": "AUTHORIZED_WAIT",
        "created_utc": iso(now_utc()),
        "updated_utc": iso(now_utc()),
        "authorization_path": str(GATE_PATH),
        "authorization_sha256": GATE_SHA256,
        "prompt_manifest_path": str(PROMPT_MANIFEST),
        "prompt_manifest_sha256": PROMPT_MANIFEST_SHA256,
        "ordered_papers": list(PAPERS),
        "reference_only": True,
        "advisory_only": True,
        "publish_commit_push_authorized": False,
        "flow_parallel_on_studio_authorized": True,
        "broker_serializes_submit_instants_only": True,
        "gap_ladder_minutes": list(GAP_LADDER_MINUTES),
        "current_gap_minutes": GAP_LADDER_MINUTES[0],
        "first_not_before": iso(first_gate),
        "prior_goru_start": {
            "epoch": first_prior_grant["epoch"],
            "utc": first_prior_grant["utc"],
            "holder": first_prior_grant["payload"]["holder"],
            "lease_id": first_prior_grant["payload"]["lease_id"],
        },
        "papers": {str(number): {"status": "pending"} for number in PAPERS},
        "first_unaccepted_or_soft_throttle": None,
        "challenge_stop": None,
        "next_action": "wait for first 30-minute Pro Start gate, then run paper_01",
    }


def save_ramp(state, **updates):
    state.update(updates)
    state["updated_utc"] = iso(now_utc())
    r.atomic_json(RAMP_STATE_PATH, state)
    return state


def update_paper(state, number, **updates):
    row = dict(state["papers"][str(number)])
    row.update(updates)
    state["papers"][str(number)] = row
    save_ramp(state)


def verify_static(specs):
    if sha(GATE_PATH) != GATE_SHA256:
        raise RampHold("Duho max-consumption gate hash mismatch")
    if sha(PROMPT_MANIFEST) != PROMPT_MANIFEST_SHA256:
        raise RampHold("round-2 re-research prompt manifest hash mismatch")
    if sha(ROUND1_SEQUENCE_FINAL) != ROUND1_SEQUENCE_FINAL_SHA256:
        raise RampHold("round-1 final sequence receipt hash mismatch")
    manifest = json.loads(PROMPT_MANIFEST.read_text())
    if manifest.get("ordered_papers") != list(PAPERS) or manifest.get("reference_only") is not True:
        raise RampHold("prompt manifest boundary mismatch")
    if len(specs) != 9:
        raise RampHold(f"expected nine prompt specs, found {len(specs)}")
    for spec in specs:
        if sha(spec["prompt_path"]) != spec["prompt_file_sha256"]:
            raise RampHold(f"prompt file hash drift: {spec['paper_id']}")
        for output in (spec["packet_path"], spec["metadata_path"], spec["deletion_path"], spec["failure_path"]):
            if Path(output).exists():
                raise RampHold(f"fresh re-research output already exists: {output}")
    broker, _ = broker_snapshot()
    if broker.get("frozen"):
        raise r.GlobalChallengeStop("broker already frozen before round-2 ramp")
    ledger_message, _, account_grants = ledger_snapshot()
    starts = goru_start_grants(account_grants)
    if not starts:
        raise RampHold("no prior Goru Start grant found for first-gap anchor")
    prior = starts[-1]
    prior_receipt = json.loads(ROUND1_SEQUENCE_FINAL.read_text())
    paper8 = prior_receipt.get("papers", {}).get("8", {})
    if prior_receipt.get("status") != "COMPLETE_HOLD_AFTER_PAPER08" or paper8.get("status") != "completed":
        raise RampHold("round-1 paper_08 completion receipt boundary mismatch")
    if (
        prior.get("epoch") != paper8.get("account_grant_epoch")
        or prior.get("utc") != paper8.get("account_grant_utc")
        or prior.get("payload", {}).get("lease_id") != paper8.get("account_lease_id")
        or prior.get("payload", {}).get("holder") != "goru-dr-review-r1-paper_08-start"
    ):
        raise RampHold(f"unexpected prior Goru Start anchor: {prior.get('payload', {}).get('holder')}")
    record = r.target_record()
    if not record or record.get("path") != "/app":
        raise RampHold(f"Pro exact target not clean /app before ramp: {record}")
    return prior, ledger_message


def wait_for_gate(state, number, not_before, expected_prior_start_lease):
    while True:
        broker, live = broker_snapshot()
        if broker.get("frozen"):
            raise r.GlobalChallengeStop(f"broker frozen while waiting for paper_{number:02d}")
        ledger_message, _, account_grants = ledger_snapshot()
        starts = goru_start_grants(account_grants)
        if not starts or starts[-1]["payload"]["lease_id"] != expected_prior_start_lease:
            raise RampHold(f"unexpected intervening Goru Start before paper_{number:02d}")
        remaining = (not_before - now_utc()).total_seconds()
        save_ramp(
            state,
            status=f"WAITING_PAPER{number:02d}_GATE",
            next_paper=number,
            next_not_before=iso(not_before),
            remaining_seconds=round(max(0.0, remaining), 1),
            live_leases_snapshot=live,
            ledger_verify=ledger_message,
        )
        if remaining <= 0:
            return
        print(json.dumps({
            "status": f"WAITING_PAPER{number:02d}_GATE",
            "not_before": iso(not_before),
            "remaining_seconds": round(remaining, 1),
            "live_leases": live,
        }, sort_keys=True), flush=True)
        time.sleep(min(30, max(1, remaining)))


def classify_after_start_timeout(identity, spec, browser):
    path = identity["conversation_path"]
    holder = f"goru-r2-{spec['paper_id']}-start-timeout-classify"
    client = r.UDSClient(r.SOCK)
    lease = None
    try:
        lease = r.acquire_target(client, holder, "read", ttl=240, max_wait=60)
        page = r.exact_page(browser, path)
        if r.page_challenge(page):
            r.freeze_for_challenge(client, holder, spec["paper_id"], "delayed Start classification")
        r.check_action(client, lease, f"{spec['paper_id']} classify inconclusive Start without retry", path, page)
        snapshot = r.page_snapshot(page)
        text = " ".join(item["text"] for item in snapshot["messages"])
        active = (
            snapshot["stop"]
            or snapshot["research"]
            or "While I'm researching" in text
            or "Researching " in text
            or "Creating visuals for the report" in text
            or "Writing your report" in text
        )
        last = snapshot["messages"][-1]["text"] if snapshot["messages"] else ""
        terminal = len(snapshot["messages"]) >= 3 and len(last) >= 2000 and not active and not snapshot["failure"]
        starts = [control for control in snapshot["controls"] if control["label"] == "Start research" and not control["disabled"]]
        prompt_identity = r.current_prompt_identity(page, Path(spec["prompt_path"]).read_text().rstrip("\n"))
        if active:
            return "delayed_accepted_active", snapshot
        if terminal:
            return "delayed_accepted_terminal", snapshot
        if snapshot["failure"]:
            return "soft_throttle_or_terminal_failure", snapshot
        if len(starts) == 1 and prompt_identity is not None:
            return "positively_unaccepted", snapshot
        return "ambiguous_technical_hold", snapshot
    finally:
        r.release_lease(client, lease)
        client.close()


def latest_paper_start_grant(spec, identity):
    _, _, grants = ledger_snapshot()
    submit_time = parse_utc(identity["submit_utc"])
    candidates = [
        row
        for row in goru_start_grants(grants)
        if spec["paper_id"] in row.get("payload", {}).get("holder", "")
        and parse_utc(row["utc"]) >= submit_time
    ]
    if len(candidates) != 1:
        raise RampHold(f"expected one Start grant for {spec['paper_id']}, found {len(candidates)}")
    return candidates[0]


def process_paper(state, specs, manuscript_state, number, current_gap, browser):
    spec = specs[number - 1]
    paper_id = spec["paper_id"]
    update_paper(state, number, status="starting", gap_minutes=current_gap, started_utc=iso(now_utc()))
    if not r.target_matches("/app"):
        raise RampHold(f"{paper_id} requires clean exact /app target before prompt staging")
    identity = None
    try:
        r.set_paper_state(manuscript_state, number, status="starting", started_utc=r.utcnow())
        identity = r.stage_and_submit(spec, manuscript_state, browser)
        plan = r.wait_for_plan(identity, spec, manuscript_state, browser)
        if plan == "start_required":
            try:
                r.start_research(identity, spec, manuscript_state, browser)
            except r.PaperFailure as exc:
                if "acceptance not positively confirmed" not in str(exc):
                    raise
                classification, snapshot = classify_after_start_timeout(identity, spec, browser)
                update_paper(state, number, start_timeout_classification=classification)
                if classification.startswith("delayed_accepted"):
                    grant = latest_paper_start_grant(spec, identity)
                    r.set_paper_state(
                        manuscript_state,
                        number,
                        status="researching",
                        research_start_utc=grant["utc"],
                        research_start_mode=classification,
                        research_start_account_lease_id=grant["payload"]["lease_id"],
                    )
                elif classification in {"positively_unaccepted", "soft_throttle_or_terminal_failure"}:
                    raise SoftThrottleHold(f"{paper_id} {classification}; no retry")
                else:
                    raise RampHold(f"{paper_id} Start result ambiguous after read-only classification; no retry")
        elif plan == "already_researching":
            grant = find_account_grant(identity["submit_account_lease_id"])
            r.set_paper_state(
                manuscript_state,
                number,
                status="researching",
                research_start_utc=grant["utc"],
                research_start_mode="automatic_after_prompt_send",
                research_start_account_lease_id=grant["payload"]["lease_id"],
            )
        else:
            raise RampHold(f"{paper_id} unexpected plan classification {plan}")

        current = manuscript_state["papers"][number - 1]
        start_grant = find_account_grant(current["research_start_account_lease_id"])
        start_utc = parse_utc(start_grant["utc"])
        update_paper(
            state,
            number,
            status="researching",
            accepted_start_utc=start_grant["utc"],
            accepted_start_epoch=start_grant["epoch"],
            accepted_start_lease_id=start_grant["payload"]["lease_id"],
            accepted_start_holder=start_grant["payload"]["holder"],
            new_prompt_send_performed=True,
            start_retry_performed=False,
        )
        report_hwao(
            f"GORU ROUND2 DR RAMP {paper_id.upper()} START ACCEPTED at {start_grant['utc']} "
            f"under {start_grant['payload']['lease_id']}; gap step {current_gap} min; no retry. "
            "Reference-only custody continues on Pro while Flow remains parallel on Studio."
        )

        try:
            stable, result_sha = r.poll_terminal(identity, spec, manuscript_state, browser)
        except r.PaperFailure as exc:
            if "stable terminal failure" in str(exc):
                raise SoftThrottleHold(f"{paper_id} terminal research failure after accepted Start; no retry")
            raise
        metadata, save_entry = r.save_packet(stable, result_sha, identity, spec, manuscript_state)
        scan = metadata.get("output_scan", {})
        quality_pass = all(scan.get(f"section_{index}_present") for index in range(1, 6))
        quality_pass = quality_pass and "REFERENCE_ONLY_NO_AUTO_APPLY" in Path(spec["packet_path"]).read_text()
        _, delete_entry = r.delete_exact_own(identity, spec, manuscript_state, browser)
        final = json.loads(r.STATE_PATH.read_text())["papers"][number - 1]
        update_paper(
            state,
            number,
            status="completed",
            packet_path=spec["packet_path"],
            packet_sha256=final["packet_sha256"],
            metadata_sha256=final["metadata_sha256"],
            result_chars=metadata["result_chars"],
            result_sha256=metadata["result_text_sha256"],
            source_anchor_count=metadata["source_anchor_count"],
            required_output_shape_pass=quality_pass,
            save_epoch=save_entry["epoch"],
            deletion_sha256=final["deletion_sha256"],
            delete_epoch=delete_entry["epoch"],
            completed_utc=iso(now_utc()),
        )
        report_hwao(
            f"GORU ROUND2 DR RAMP {paper_id.upper()} COMPLETE: packet {final['packet_sha256']}; "
            f"exact-own deletion {final['deletion_sha256']}; output-shape-pass={quality_pass}; ledger VERIFY_OK."
        )
        return start_grant, start_utc
    except r.GlobalChallengeStop as exc:
        with suppress(Exception):
            r.write_failure(spec, manuscript_state, exc, identity)
        raise
    except SoftThrottleHold as exc:
        with suppress(Exception):
            r.write_failure(spec, manuscript_state, exc, identity)
        raise
    except RampHold:
        raise
    except Exception as exc:
        with suppress(Exception):
            r.write_failure(spec, manuscript_state, exc, identity)
        raise RampHold(f"{paper_id} technical/custody failure: {type(exc).__name__}: {exc}") from exc


def stepped_up_gap(current_gap):
    index = GAP_LADDER_MINUTES.index(current_gap)
    return GAP_LADDER_MINUTES[max(0, index - 1)]


def next_success_gap(current_gap):
    index = GAP_LADDER_MINUTES.index(current_gap)
    return GAP_LADDER_MINUTES[min(len(GAP_LADDER_MINUTES) - 1, index + 1)]


def main():
    specs = r.discover_prompts()
    prior, ledger_message = verify_static(specs)
    first_gate = parse_utc(prior["utc"]) + timedelta(minutes=GAP_LADDER_MINUTES[0])
    if RAMP_STATE_PATH.exists():
        raise RampHold(f"duplicate ramp invocation refused; state already exists: {RAMP_STATE_PATH}")
    state = base_ramp_state(prior, first_gate)
    save_ramp(state, ledger_verify=ledger_message)
    manuscript_state = r.load_or_create_state(specs)
    current_gap = GAP_LADDER_MINUTES[0]
    expected_prior_lease = prior["payload"]["lease_id"]
    next_gate = first_gate

    report_hwao(
        "GORU ROUND2 DR RAMP ACTIVE: papers01..09 reference-only on Pro; Start gap ladder "
        "30→20→15→10→8 minutes after accepted Starts. First unaccepted/soft throttle steps up one notch "
        "and HOLDS with no retry. Hard challenge freezes and wakes Hwao→Duho. Flow may run in parallel on Studio."
    )

    try:
        with sync_playwright() as playwright:
            browser = playwright.chromium.connect_over_cdp(r.BASE)
            for number in PAPERS:
                wait_for_gate(state, number, next_gate, expected_prior_lease)
                manuscript_state = json.loads(r.STATE_PATH.read_text())
                start_grant, start_utc = process_paper(state, specs, manuscript_state, number, current_gap, browser)
                expected_prior_lease = start_grant["payload"]["lease_id"]
                current_gap = next_success_gap(current_gap)
                next_gate = start_utc + timedelta(minutes=current_gap)
                save_ramp(
                    state,
                    status=f"WAITING_PAPER{number + 1:02d}_GATE" if number < 9 else "VERIFYING_FINAL",
                    current_gap_minutes=current_gap,
                    next_paper=number + 1 if number < 9 else None,
                    next_not_before=iso(next_gate) if number < 9 else None,
                )
            browser.close()

        manuscript_state = json.loads(r.STATE_PATH.read_text())
        statuses, source_count, summary_sha, entry, summary_path = r.write_summary(manuscript_state, final=True)
        ledger_final, entries, _ = ledger_snapshot()
        broker, live = broker_snapshot()
        if broker.get("frozen") or live:
            raise RampHold(f"final broker state not clean: frozen={broker.get('frozen')} live={live}")
        if statuses != {"completed": 9}:
            raise RampHold(f"final manuscript state not all completed: {statuses}")
        save_ramp(
            state,
            status="COMPLETE_HOLD_AFTER_PAPER09",
            completed_papers=list(PAPERS),
            current_gap_minutes=current_gap,
            final_summary_path=str(summary_path),
            final_summary_sha256=summary_sha,
            final_summary_ledger_epoch=entry["epoch"],
            total_source_anchors=source_count,
            ledger_verify=ledger_final,
            ledger_entries=len(entries),
            next_action="HOLD for fresh Duho gate; reference packets only; no auto-apply or publication",
        )
        report_hwao(
            f"GORU ROUND2 DR RAMP COMPLETE papers01..09; summary {summary_path} sha {summary_sha}; "
            f"ledger {ledger_final}; no live leases. HOLD: no auto-apply, publish, commit, or next research queue without fresh gate."
        )
        print(json.dumps({"status": state["status"], "summary": str(summary_path), "summary_sha256": summary_sha}, sort_keys=True))
        return 0
    except r.GlobalChallengeStop as exc:
        save_ramp(
            state,
            status="HARD_CHALLENGE_STOP_FROZEN",
            challenge_stop={"utc": iso(now_utc()), "error": str(exc), "interaction_attempted": False},
            next_action="HOLD; never interact; Hwao wakes Duho",
        )
        with suppress(Exception):
            report_hwao(f"GORU ROUND2 DR RAMP HARD CHALLENGE STOP/FROZEN: {exc}. Never interact. Wake Duho now.")
        raise
    except SoftThrottleHold as exc:
        sustainable_gap = stepped_up_gap(current_gap)
        save_ramp(
            state,
            status="FIRST_UNACCEPTED_OR_SOFT_THROTTLE_HOLD_NO_RETRY",
            first_unaccepted_or_soft_throttle={
                "utc": iso(now_utc()),
                "attempted_gap_minutes": current_gap,
                "stepped_up_sustainable_gap_minutes": sustainable_gap,
                "error": str(exc),
                "retry_performed": False,
            },
            current_gap_minutes=sustainable_gap,
            next_action="HOLD at stepped-up maximum sustainable gap; no retry and no later paper",
        )
        with suppress(Exception):
            report_hwao(
                f"GORU ROUND2 DR RAMP FIRST UNACCEPTED/SOFT THROTTLE: {exc}. "
                f"Gap stepped up {current_gap}→{sustainable_gap} min and HOLD. No retry or later paper."
            )
        print(json.dumps({"status": state["status"], "sustainable_gap_minutes": sustainable_gap, "error": str(exc)}, sort_keys=True))
        return 2
    except RampHold as exc:
        save_ramp(
            state,
            status="TECHNICAL_OR_CUSTODY_HOLD",
            error=f"{type(exc).__name__}: {exc}",
            next_action="HOLD; inspect exact target, custody, state, and ledger; no retry or later paper",
        )
        with suppress(Exception):
            report_hwao(f"GORU ROUND2 DR RAMP TECHNICAL/CUSTODY HOLD: {exc}. No retry or later paper; inspect receipts and ledger.")
        print(json.dumps({"status": state["status"], "error": str(exc)}, sort_keys=True))
        return 2
    except Exception as exc:
        save_ramp(
            state,
            status="UNEXPECTED_HOLD",
            error=f"{type(exc).__name__}: {exc}",
            next_action="HOLD; no retry or later paper",
        )
        with suppress(Exception):
            report_hwao(f"GORU ROUND2 DR RAMP UNEXPECTED HOLD: {type(exc).__name__}: {str(exc)[:500]}. No retry.")
        raise


if __name__ == "__main__":
    raise SystemExit(main())
