import json
import shutil
import sys
from contextlib import suppress
from datetime import timedelta
from pathlib import Path

sys.path.insert(0, "scratch")
import run_round2_dr_reresearch_ramp as x
from playwright.sync_api import sync_playwright

SNAPSHOT_PACKET = x.r.PACKET_DIR / "paper_01_round2_reresearch_dr_packet.failed_save_snapshot_20260715T053400Z.md"
SNAPSHOT_METADATA = x.r.PACKET_DIR / "paper_01_round2_reresearch_dr_packet.failed_save_snapshot_20260715T053400Z.metadata.json"
RECOVERY_RECEIPT = x.r.PACKET_DIR / "PAPER01_PACKET_MARKER_RECOVERY_20260715T053400Z.json"
EXPECTED_FAILURE_SHA256 = "8ed98e6f9d4cdb7f262dc8ac2a874c2df5c6f9ee6bfc2e372265bb74d5a70c2c"
EXPECTED_ACCOUNT_START_LEASE = "L00519"
EXPECTED_ACCOUNT_START_UTC = "2026-07-15T05:23:06Z"


def preflight(specs, ramp_state, manuscript_state):
    if x.sha(x.GATE_PATH) != x.GATE_SHA256 or x.sha(x.PROMPT_MANIFEST) != x.PROMPT_MANIFEST_SHA256:
        raise x.RampHold("authorization or prompt manifest hash mismatch during custody recovery")
    broker, live = x.broker_snapshot()
    if broker.get("frozen"):
        raise x.r.GlobalChallengeStop("broker frozen before paper_01 custody recovery")
    goru_live = [row for row in live if str(row.get("holder", "")).lower().startswith("goru-")]
    if goru_live:
        raise x.RampHold(f"unexpected live Goru leases before custody recovery: {goru_live}")
    ledger_message, _, grants = x.ledger_snapshot()
    starts = x.goru_start_grants(grants)
    if not starts or starts[-1]["payload"]["lease_id"] != EXPECTED_ACCOUNT_START_LEASE:
        raise x.RampHold("paper_01 accepted Start is not the latest Goru Start grant")
    if ramp_state.get("status") != "TECHNICAL_OR_CUSTODY_HOLD":
        raise x.RampHold(f"unexpected ramp state for recovery: {ramp_state.get('status')}")
    paper = manuscript_state["papers"][0]
    if paper.get("status") not in {"failed", "saved_verified"} or paper.get("failure_sha256") != EXPECTED_FAILURE_SHA256:
        raise x.RampHold("paper_01 immutable save-marker failure receipt mismatch")
    failure_path = Path(paper["failure_path"])
    failure = json.loads(failure_path.read_text())
    if x.sha(failure_path) != EXPECTED_FAILURE_SHA256 or "saved packet result markers invalid" not in failure.get("error", ""):
        raise x.RampHold("paper_01 failure is not the narrow local marker-verification defect")
    identity = paper.get("identity") or {}
    if identity.get("conversation_path") != "/app/5cf39108a4ee7ea2":
        raise x.RampHold("paper_01 exact-owned route mismatch")
    if paper.get("research_start_account_lease_id") != EXPECTED_ACCOUNT_START_LEASE:
        raise x.RampHold("paper_01 accepted Start lease mismatch")
    if x.r.target_record().get("path") != identity["conversation_path"]:
        raise x.RampHold("paper_01 exact-owned terminal route is not current")
    for spec in specs[1:]:
        base_row = manuscript_state["papers"][spec["paper"] - 1]
        if base_row.get("status") != "pending":
            raise x.RampHold(f"{spec['paper_id']} is not pending before recovery continuation")
        for output in (spec["packet_path"], spec["metadata_path"], spec["deletion_path"], spec["failure_path"]):
            if Path(output).exists():
                raise x.RampHold(f"unexpected later-paper output before recovery: {output}")
    return ledger_message, identity


def recover_paper01(browser, specs, ramp_state, manuscript_state, identity, ledger_before):
    spec = specs[0]
    packet_path = Path(spec["packet_path"])
    metadata_path = Path(spec["metadata_path"])
    for source, snapshot in ((packet_path, SNAPSHOT_PACKET), (metadata_path, SNAPSHOT_METADATA)):
        if not source.is_file():
            raise x.RampHold(f"failed-save source absent: {source}")
        if not snapshot.exists():
            shutil.copy2(source, snapshot)
    snapshot_packet_sha = x.sha(SNAPSHOT_PACKET)
    snapshot_metadata_sha = x.sha(SNAPSHOT_METADATA)

    current = manuscript_state["papers"][0]
    if current.get("status") == "saved_verified":
        metadata = json.loads(metadata_path.read_text())
        save_entry = current["save_ledger"]
    else:
        stable, result_sha = x.r.poll_terminal(identity, spec, manuscript_state, browser)
        metadata, save_entry = x.r.save_packet(stable, result_sha, identity, spec, manuscript_state)
    scan = metadata.get("output_scan", {})
    quality_pass = all(scan.get(f"section_{index}_present") for index in range(1, 6))
    quality_pass = quality_pass and "REFERENCE_ONLY_NO_AUTO_APPLY" in packet_path.read_text()
    _, delete_entry = x.r.delete_exact_own(identity, spec, manuscript_state, browser)
    final = json.loads(x.r.STATE_PATH.read_text())["papers"][0]
    x.update_paper(
        ramp_state,
        1,
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
        completed_utc=x.iso(x.now_utc()),
        custody_recovery={
            "reason": "verbatim prompt contained a prior Captured-source-anchors heading; final wrapper delimiter is now selected after the new result",
            "new_prompt_or_start_performed": False,
            "failed_packet_snapshot": str(SNAPSHOT_PACKET),
            "failed_packet_snapshot_sha256": snapshot_packet_sha,
            "failed_metadata_snapshot": str(SNAPSHOT_METADATA),
            "failed_metadata_snapshot_sha256": snapshot_metadata_sha,
            "immutable_failure_sha256": EXPECTED_FAILURE_SHA256,
        },
    )
    receipt = {
        "status": "PAPER01_CUSTODY_RECOVERED_WITHOUT_RESUBMISSION",
        "recovered_utc": x.iso(x.now_utc()),
        "conversation_id": identity["conversation_id"],
        "accepted_start_lease_id": EXPECTED_ACCOUNT_START_LEASE,
        "accepted_start_utc": EXPECTED_ACCOUNT_START_UTC,
        "new_prompt_send_performed": False,
        "new_start_performed": False,
        "retry_performed": False,
        "failure_receipt_sha256": EXPECTED_FAILURE_SHA256,
        "failed_packet_snapshot": str(SNAPSHOT_PACKET),
        "failed_packet_snapshot_sha256": snapshot_packet_sha,
        "failed_metadata_snapshot": str(SNAPSHOT_METADATA),
        "failed_metadata_snapshot_sha256": snapshot_metadata_sha,
        "verified_packet_sha256": final["packet_sha256"],
        "verified_metadata_sha256": final["metadata_sha256"],
        "verified_deletion_sha256": final["deletion_sha256"],
        "save_epoch": save_entry["epoch"],
        "delete_epoch": delete_entry["epoch"],
        "required_output_shape_pass": quality_pass,
        "ledger_verify_before": ledger_before,
        "ledger_verify_after": x.ledger_snapshot()[0],
    }
    x.r.atomic_json(RECOVERY_RECEIPT, receipt)
    x.save_ramp(
        ramp_state,
        status="WAITING_PAPER02_GATE",
        current_gap_minutes=20,
        next_paper=2,
        next_not_before=x.iso(x.parse_utc(EXPECTED_ACCOUNT_START_UTC) + timedelta(minutes=20)),
        paper01_custody_recovery_receipt=str(RECOVERY_RECEIPT),
        paper01_custody_recovery_receipt_sha256=x.sha(RECOVERY_RECEIPT),
    )
    x.report_hwao(
        f"GORU ROUND2 DR RAMP PAPER_01 CUSTODY RECOVERED without prompt/Start retry: packet {final['packet_sha256']}; "
        f"exact-own deletion {final['deletion_sha256']}; ledger VERIFY_OK. Continue paper_02 at the 20-minute gate."
    )


def main():
    specs = x.r.discover_prompts()
    ramp_state = json.loads(x.RAMP_STATE_PATH.read_text())
    manuscript_state = json.loads(x.r.STATE_PATH.read_text())
    ledger_before, identity = preflight(specs, ramp_state, manuscript_state)
    current_gap = 20
    expected_prior_lease = EXPECTED_ACCOUNT_START_LEASE
    next_gate = x.parse_utc(EXPECTED_ACCOUNT_START_UTC) + timedelta(minutes=current_gap)

    try:
        with sync_playwright() as playwright:
            browser = playwright.chromium.connect_over_cdp(x.r.BASE)
            recover_paper01(browser, specs, ramp_state, manuscript_state, identity, ledger_before)
            for number in range(2, 10):
                x.wait_for_gate(ramp_state, number, next_gate, expected_prior_lease)
                manuscript_state = json.loads(x.r.STATE_PATH.read_text())
                start_grant, start_utc = x.process_paper(
                    ramp_state, specs, manuscript_state, number, current_gap, browser
                )
                expected_prior_lease = start_grant["payload"]["lease_id"]
                current_gap = x.next_success_gap(current_gap)
                next_gate = start_utc + timedelta(minutes=current_gap)
                x.save_ramp(
                    ramp_state,
                    status=f"WAITING_PAPER{number + 1:02d}_GATE" if number < 9 else "VERIFYING_FINAL",
                    current_gap_minutes=current_gap,
                    next_paper=number + 1 if number < 9 else None,
                    next_not_before=x.iso(next_gate) if number < 9 else None,
                )
            browser.close()

        manuscript_state = json.loads(x.r.STATE_PATH.read_text())
        statuses, source_count, summary_sha, entry, summary_path = x.r.write_summary(manuscript_state, final=True)
        ledger_final, entries, _ = x.ledger_snapshot()
        broker, live = x.broker_snapshot()
        goru_live = [row for row in live if str(row.get("holder", "")).lower().startswith("goru-")]
        if broker.get("frozen") or goru_live:
            raise x.RampHold(f"final Goru broker state not clean: frozen={broker.get('frozen')} live={goru_live}")
        if statuses != {"completed": 9}:
            raise x.RampHold(f"final manuscript state not all completed: {statuses}")
        x.save_ramp(
            ramp_state,
            status="COMPLETE_HOLD_AFTER_PAPER09",
            completed_papers=list(x.PAPERS),
            current_gap_minutes=current_gap,
            final_summary_path=str(summary_path),
            final_summary_sha256=summary_sha,
            final_summary_ledger_epoch=entry["epoch"],
            total_source_anchors=source_count,
            ledger_verify=ledger_final,
            ledger_entries=len(entries),
            live_non_goru_leases_at_final=live,
            next_action="HOLD for fresh Duho gate; reference packets only; no auto-apply or publication",
        )
        x.report_hwao(
            f"GORU ROUND2 DR RAMP COMPLETE papers01..09 after local custody recovery; summary {summary_path} sha {summary_sha}; "
            f"ledger {ledger_final}. HOLD: no auto-apply or publication."
        )
        print(json.dumps({"status": ramp_state["status"], "summary_sha256": summary_sha}, sort_keys=True))
        return 0
    except x.r.GlobalChallengeStop as exc:
        x.save_ramp(
            ramp_state,
            status="HARD_CHALLENGE_STOP_FROZEN",
            challenge_stop={"utc": x.iso(x.now_utc()), "error": str(exc), "interaction_attempted": False},
            next_action="HOLD; never interact; Hwao wakes Duho",
        )
        with suppress(Exception):
            x.report_hwao(f"GORU ROUND2 DR RAMP HARD CHALLENGE STOP/FROZEN: {exc}. Never interact. Wake Duho.")
        raise
    except x.SoftThrottleHold as exc:
        sustainable_gap = x.stepped_up_gap(current_gap)
        x.save_ramp(
            ramp_state,
            status="FIRST_UNACCEPTED_OR_SOFT_THROTTLE_HOLD_NO_RETRY",
            first_unaccepted_or_soft_throttle={
                "utc": x.iso(x.now_utc()),
                "attempted_gap_minutes": current_gap,
                "stepped_up_sustainable_gap_minutes": sustainable_gap,
                "error": str(exc),
                "retry_performed": False,
            },
            current_gap_minutes=sustainable_gap,
            next_action="HOLD at stepped-up maximum sustainable gap; no retry and no later paper",
        )
        with suppress(Exception):
            x.report_hwao(
                f"GORU ROUND2 DR RAMP FIRST UNACCEPTED/SOFT THROTTLE: {exc}; gap {current_gap}→{sustainable_gap}; HOLD, no retry."
            )
        print(json.dumps({"status": ramp_state["status"], "sustainable_gap_minutes": sustainable_gap}, sort_keys=True))
        return 2
    except x.RampHold as exc:
        x.save_ramp(
            ramp_state,
            status="TECHNICAL_OR_CUSTODY_HOLD",
            error=f"{type(exc).__name__}: {exc}",
            next_action="HOLD; no retry or later paper",
        )
        with suppress(Exception):
            x.report_hwao(f"GORU ROUND2 DR RAMP RECOVERY HOLD: {exc}. No retry or later paper.")
        print(json.dumps({"status": ramp_state["status"], "error": str(exc)}, sort_keys=True))
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
