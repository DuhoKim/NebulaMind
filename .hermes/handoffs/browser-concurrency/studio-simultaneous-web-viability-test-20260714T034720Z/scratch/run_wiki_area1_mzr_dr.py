import json
import re
import sys
import time
from contextlib import suppress
from datetime import datetime, timedelta, timezone
from pathlib import Path
from urllib.parse import urlparse

sys.path.insert(0, "scratch")
import dr_manuscript_round2_reresearch_runner as r
import run_round2_dr_reresearch_ramp as ramp
from playwright.sync_api import sync_playwright

AREA_DIR = Path("/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/wiki-expansion-20260715")
BRIEF_PATH = AREA_DIR / "area1_mass_metallicity_DR_BRIEF.md"
PROMPT_PATH = AREA_DIR / "area1_mass_metallicity_DR_PROMPT.md"
PACKET_PATH = AREA_DIR / "area1_mass_metallicity_DR_PACKET.md"
METADATA_PATH = AREA_DIR / "area1_mass_metallicity_DR_PACKET.metadata.json"
STATE_PATH = AREA_DIR / "area1_mass_metallicity_DR_STATE.json"
FAILURE_PATH = AREA_DIR / "area1_mass_metallicity_DR_FAILURE.json"
PREFLIGHT_RECOVERY_PATH = AREA_DIR / "area1_mass_metallicity_DR_PREFLIGHT_RECOVERY.json"
GATE_SPACING_MINUTES = 20
RUN_ID = "WIKI_AREA1_MZR_DR_20260715"
MARKER = "MZR_DR_PACKET_COMPLETE_REFERENCE_ONLY"

# Reuse the proven exact-target/broker/CDP machinery, but confine all local
# artifacts for this run to the user-authorized wiki-expansion handoff.
r.PACKET_DIR = AREA_DIR
r.STATE_PATH = STATE_PATH
r.HWAO_TARGET = "ge-mastermind:0.0"


class FirstUnacceptedHold(RuntimeError):
    pass


def now_utc():
    return datetime.now(timezone.utc)


def parse_utc(value):
    return datetime.fromisoformat(value.replace("Z", "+00:00"))


def save_state(state, **updates):
    state.update(updates)
    state["updated_utc"] = r.utcnow()
    r.atomic_json(STATE_PATH, state)


def initial_state(spec):
    return {
        "run_id": RUN_ID,
        "created_utc": r.utcnow(),
        "updated_utc": r.utcnow(),
        "status": "PREFLIGHT",
        "topic": "stellar mass-metallicity relation",
        "broad_non_agn": True,
        "advisory_only": True,
        "wiki_write_performed": False,
        "live_direct_write_authorized_for_hwao": True,
        "tori_output_boundary": str(PACKET_PATH),
        "brief_path": str(BRIEF_PATH),
        "brief_sha256": r.sha_file(BRIEF_PATH),
        "prompt_path": str(PROMPT_PATH),
        "prompt_file_sha256": spec["prompt_file_sha256"],
        "prompt_sha256": spec["prompt_sha256"],
        "minimum_pre_run_account_spacing_minutes": GATE_SPACING_MINUTES,
        "first_unaccepted_policy": "BACK_OFF_AND_HOLD_NO_RETRY",
        "hard_challenge_policy": "STOP_FREEZE_HOLD_NEVER_INTERACT",
        "paper": {**spec, "status": "pending"},
    }


def spec():
    prompt = PROMPT_PATH.read_text().rstrip("\n")
    return {
        "paper": 1,
        "paper_id": "area1_mzr",
        "shortname": "mass_metallicity_relation_wiki_evidence_map",
        "prompt_path": str(PROMPT_PATH),
        "prompt_file_sha256": r.sha_file(PROMPT_PATH),
        "prompt_sha256": r.sha_bytes(prompt.encode()),
        "prompt_chars": len(prompt),
        "prompt_lines": len(prompt.splitlines()),
        "packet_path": str(PACKET_PATH),
        "metadata_path": str(METADATA_PATH),
        "deletion_path": str(AREA_DIR / "area1_mass_metallicity_DR_PACKET.deletion.json"),
        "failure_path": str(FAILURE_PATH),
    }


def base_state(state):
    """Adapt the one-item state to the proven runner's list-shaped contract."""
    return {
        "batch_id": RUN_ID,
        "updated_utc": state["updated_utc"],
        "advisory_only": True,
        "reference_only": True,
        "papers": [state["paper"]],
    }


def sync_from_base(state, adapted):
    state["paper"] = adapted["papers"][0]
    save_state(state)


def account_grants():
    message, entries, grants = ramp.ledger_snapshot()
    account = [entry for entry in grants if entry.get("payload", {}).get("kind") == "account-submission"]
    return message, entries, account


def latest_account_grant():
    message, entries, account = account_grants()
    if not account:
        return message, len(entries), None
    row = account[-1]
    return message, len(entries), {
        "utc": row["utc"],
        "ledger_epoch": row["epoch"],
        **row["payload"],
    }


def wait_for_safe_gap(state):
    while True:
        broker, live = ramp.broker_snapshot()
        if broker.get("frozen"):
            raise r.GlobalChallengeStop("broker frozen before MZR Deep Research dispatch")
        message, count, latest = latest_account_grant()
        if message != f"OK ({count} entries)":
            raise RuntimeError(f"ledger verification mismatch: {message} entries={count}")
        live_account = [row for row in live if row.get("kind") == "account-submission"]
        if latest:
            not_before = parse_utc(latest["utc"]) + timedelta(minutes=GATE_SPACING_MINUTES)
        else:
            not_before = now_utc()
        remaining = max(0.0, (not_before - now_utc()).total_seconds())
        save_state(
            state,
            status="WAITING_GENTLE_ACCOUNT_GATE" if remaining > 0 or live_account else "ACCOUNT_GATE_READY",
            latest_prior_account_grant=latest,
            account_gate_not_before=not_before.isoformat().replace("+00:00", "Z"),
            ledger_verify=message,
            live_account_leases=live_account,
        )
        if remaining <= 0 and not live_account:
            return
        print(json.dumps({
            "status": state["status"],
            "not_before": state["account_gate_not_before"],
            "remaining_seconds": round(remaining, 1),
            "latest_holder": latest.get("holder") if latest else None,
            "live_account_leases": live_account,
        }, sort_keys=True), flush=True)
        time.sleep(min(30.0, max(5.0, remaining)))


def prepare_new_chat(browser, state):
    record = r.target_record()
    if not record:
        raise r.TargetDrift("dedicated Gemini CDP target missing")
    if record["path"] == "/app":
        return
    holder = "goru-wiki-area1-mzr-new-chat"
    client = r.UDSClient(r.SOCK)
    lease = None
    try:
        lease = r.acquire_target(client, holder, "write", ttl=300)
        page = r.exact_page(browser, record["path"])
        if r.page_challenge(page):
            r.freeze_for_challenge(client, holder, "area1_mzr", "pre-dispatch current-route classification")
        r.check_action(client, lease, "area1_mzr navigate to new chat after pivot", record["path"], page)
        page.goto("https://gemini.google.com/app", wait_until="domcontentloaded", timeout=30000)
        page.wait_for_timeout(1200)
        if r.page_challenge(page):
            r.freeze_for_challenge(client, holder, "area1_mzr", "post-navigation new-chat classification")
        if not r.target_matches("/app", page):
            raise r.TargetDrift("new-chat route failed exact verification")
        save_state(state, pivoted_from_prior_route=record["path"], status="NEW_CHAT_READY")
    finally:
        r.release_lease(client, lease)
        client.close()


def classify_after_start_timeout(identity, prompt, browser):
    path = identity["conversation_path"]
    holder = "goru-wiki-area1-mzr-start-settlement"
    client = r.UDSClient(r.SOCK)
    lease = None
    try:
        lease = r.acquire_target(client, holder, "read", ttl=300)
        page = r.exact_page(browser, path)
        if r.page_challenge(page):
            r.freeze_for_challenge(client, holder, "area1_mzr", "post-Start timeout settlement")
        if not r.target_matches(path, page):
            r.check_action(client, lease, "area1_mzr fail closed Start-timeout settlement", path, page)
        snapshot = r.page_snapshot(page)
        all_text = " ".join(item["text"] for item in snapshot.get("messages", []))
        active = snapshot["research"] or (snapshot["stop"] and any(token in all_text for token in (
            "While I'm researching", "Researching ", "Creating visuals for the report", "Writing your report"
        )))
        if active:
            return "accepted_delayed"
        terminal = (
            len(snapshot.get("messages", [])) >= 3
            and len(snapshot["messages"][-1]["text"]) >= 2000
            and not snapshot["stop"]
            and not snapshot["research"]
        )
        if terminal:
            return "terminal_delayed"
        start = page.get_by_role("button", name="Start research", exact=True)
        enabled = [start.nth(index) for index in range(start.count()) if start.nth(index).is_visible() and not start.nth(index).is_disabled()]
        prompt_identity = r.current_prompt_identity(page, prompt)
        if len(enabled) == 1 and prompt_identity and not snapshot["failure"]:
            return "positively_unaccepted"
        return "ambiguous_hold"
    finally:
        r.release_lease(client, lease)
        client.close()


def output_quality(result):
    exact_headings = [
        "## 1. Established findings",
        "## 2. Open debates and tensions",
        "## 3. Key measurements and numbers",
        "## 4. What remains unknown",
        "## 5. DO_NOT_USE_UNVERIFIED",
        "## 6. Source identity ledger",
    ]
    source_lines = re.findall(
        r"(?im)^.*\(\d{4}[a-z]?\s*,\s*[^)]+\)\s*\|\s*(?:DOI|arXiv|ADS):.*\|\s*role=(?:established|debate|caveat|future)\s*\|",
        result,
    )
    checks = {
        "exact_headings_present": all(heading in result for heading in exact_headings),
        "terminal_marker_present": result.rstrip().endswith(MARKER),
        "established_ids": len(set(re.findall(r"\bMZR-E\d{2}\b", result))),
        "debate_ids": len(set(re.findall(r"\bMZR-D\d{2}\b", result))),
        "measurement_ids": len(set(re.findall(r"\bMZR-N\d{2}\b", result))),
        "unknown_ids": len(set(re.findall(r"\bMZR-U\d{2}\b", result))),
        "required_format_source_line_count": len(source_lines),
        "doi_count": len(set(re.findall(r"(?i)\b10\.\d{4,9}/[-._;()/:A-Z0-9]+", result))),
        "arxiv_count": len(set(re.findall(r"(?i)\barXiv\s*:\s*(\d{4}\.\d{4,5})(?:v\d+)?\b", result))),
        "ads_count": len(set(re.findall(r"(?i)\bADS\s*:\s*([12]\d{3}[A-Za-z0-9.&]{8,})", result))),
        "do_not_use_section_present": "## 5. DO_NOT_USE_UNVERIFIED" in result,
        "uncited_not_usable_protocol_present": "UNCITED_NOT_USABLE" in result or "NONE — all cited items above were identity-resolved" in result,
        "broad_non_agn_scope_present": bool(re.search(r"(?i)gas-phase|stellar metallicity|stellar MZR", result)),
    }
    checks["pass"] = (
        checks["exact_headings_present"]
        and checks["terminal_marker_present"]
        and checks["established_ids"] >= 6
        and checks["debate_ids"] >= 4
        and checks["measurement_ids"] >= 5
        and checks["unknown_ids"] >= 4
        and checks["required_format_source_line_count"] >= 15
        and checks["doi_count"] + checks["arxiv_count"] + checks["ads_count"] >= 15
        and checks["uncited_not_usable_protocol_present"]
        and checks["broad_non_agn_scope_present"]
    )
    return checks


def save_packet(snapshot, result_sha, identity, spec, state):
    result = snapshot["messages"][-1]["text"]
    links = []
    seen = set()
    for item in snapshot.get("links", []):
        if r.keep_source(item) and item["href"] not in seen:
            seen.add(item["href"])
            links.append(item)
    quality = output_quality(result)
    captured_utc = r.utcnow()
    prompt = PROMPT_PATH.read_text().rstrip("\n")
    lines = [
        "# Area 1 Deep Research packet — stellar mass–metallicity relation",
        "",
        "advisory_only: true",
        "broad_non_agn: true",
        "wiki_write_performed_by_tori: false",
        "identifier_verification_required_before_live_wiki_use: true",
        "",
        f"Brief: `{BRIEF_PATH}`",
        f"Brief SHA-256: `{r.sha_file(BRIEF_PATH)}`",
        f"Prompt: `{PROMPT_PATH}`",
        f"Prompt file SHA-256: `{spec['prompt_file_sha256']}`",
        f"Submitted prompt text SHA-256: `{spec['prompt_sha256']}`",
        f"Conversation ID: `{identity['conversation_id']}`",
        f"Submit UTC: `{identity['submit_utc']}`",
        f"Research Start UTC: `{state['paper'].get('research_start_utc', '')}`",
        f"Result captured UTC: `{captured_utc}`",
        f"Raw result SHA-256: `{result_sha}`",
        "",
        "## Deep Research evidence map",
        "",
        result,
        "",
        "## Captured external source anchors",
        "",
    ]
    lines.extend([f"- {item['label'] or '(unlabeled)'} — {item['href']}" for item in links] or ["- No external anchors exposed in the result DOM; use only resolved identifiers in the source identity ledger."])
    lines.extend([
        "",
        "## Custody and safety receipt",
        "",
        "- Deep Research source discovery only; independent identifier/claim-boundary verification remains required before live wiki mutation.",
        "- No DB, wiki, trust-score, claim/evidence, code, manuscript, deploy, git, publish, cron, billing, credential, account-setting, or unrelated-conversation mutation was performed by this run.",
        "- No conversation deletion was authorized or performed.",
        "",
    ])
    r.atomic_write(PACKET_PATH, "\n".join(lines))
    metadata = {
        "run_id": RUN_ID,
        "topic": "stellar mass-metallicity relation",
        "broad_non_agn": True,
        "advisory_only": True,
        "wiki_write_performed": False,
        "identity": identity,
        "captured_utc": captured_utc,
        "result_chars": len(result),
        "result_text_sha256": result_sha,
        "packet_sha256": r.sha_file(PACKET_PATH),
        "source_anchors": links,
        "source_anchor_count": len(links),
        "output_quality": quality,
        "independent_identifier_verification_status": "PENDING_TORI_LOCAL_RECONCILIATION",
        "conversation_cleanup_authorized": False,
        "conversation_deleted": False,
    }
    r.atomic_json(METADATA_PATH, metadata)
    packet_text = PACKET_PATH.read_text()
    raw_start = "## Deep Research evidence map\n\n"
    raw_end = "\n\n## Captured external source anchors\n"
    if raw_start not in packet_text or raw_end not in packet_text:
        raise r.PaperFailure("saved MZR packet wrapper markers absent")
    saved_result = packet_text.rsplit(raw_start, 1)[1].rsplit(raw_end, 1)[0]
    if len(saved_result) != len(result) or r.sha_bytes(saved_result.encode()) != result_sha:
        raise r.PaperFailure("saved MZR raw result custody mismatch")
    metadata_read = json.loads(METADATA_PATH.read_text())
    if metadata_read["packet_sha256"] != r.sha_file(PACKET_PATH) or metadata_read["result_text_sha256"] != result_sha:
        raise r.PaperFailure("saved MZR metadata custody mismatch")
    entry = r.journal_entry(
        "wiki_area1_mzr_dr_packet_saved_verified",
        (
            f"Area1 broad non-AGN MZR Deep Research packet saved; conversation_id={identity['conversation_id']}; "
            f"result_sha256={result_sha}; packet_sha256={metadata['packet_sha256']}; metadata_sha256={r.sha_file(METADATA_PATH)}; "
            f"output_shape_pass={quality['pass']}; wiki_write=false; conversation_delete=false; independent identifier verification pending."
        ),
        [PACKET_PATH, METADATA_PATH, PROMPT_PATH, BRIEF_PATH],
    )
    save_state(
        state,
        status="PACKET_LANDED_PENDING_INDEPENDENT_IDENTIFIER_VERIFICATION" if quality["pass"] else "PACKET_LANDED_OUTPUT_SHAPE_HOLD",
        paper={
            **state["paper"],
            "status": "packet_saved",
            "packet_sha256": metadata["packet_sha256"],
            "metadata_sha256": r.sha_file(METADATA_PATH),
            "result_chars": len(result),
            "result_text_sha256": result_sha,
            "output_quality": quality,
            "save_ledger": entry,
        },
        packet_path=str(PACKET_PATH),
        packet_sha256=metadata["packet_sha256"],
        metadata_sha256=r.sha_file(METADATA_PATH),
        ledger_verify=entry["verify"],
        next_action="Tori independently resolves identifier/title/author/year and claim boundaries; Hwao must not write live claims before VERIFIED status",
    )
    r.report_hwao(
        f"MZR-DR packet landed at {PACKET_PATH}; packet sha {metadata['packet_sha256']}; output-shape pass={quality['pass']}; "
        "HOLD live wiring until Tori's independent identifier reconciliation flips the packet to VERIFIED. No wiki write or conversation deletion performed."
    )
    return metadata


def write_failure(state, exc, identity=None):
    failure_path = FAILURE_PATH
    attempt = 2
    while failure_path.exists():
        failure_path = AREA_DIR / f"area1_mass_metallicity_DR_FAILURE_{attempt}.json"
        attempt += 1
    failure = {
        "run_id": RUN_ID,
        "failed_utc": r.utcnow(),
        "status": state.get("status"),
        "error_class": type(exc).__name__,
        "error": str(exc),
        "identity": identity,
        "global_challenge_stop": isinstance(exc, r.GlobalChallengeStop),
        "first_unaccepted_hold": isinstance(exc, FirstUnacceptedHold),
        "retry_performed": False,
        "actions_not_taken": [
            "no retry", "no wiki/DB/trust write", "no deployment", "no git action", "no conversation deletion"
        ],
    }
    r.atomic_json(failure_path, failure)
    with suppress(Exception):
        entry = r.journal_entry(
            "wiki_area1_mzr_dr_hold",
            f"Area1 MZR DR hold: {type(exc).__name__}: {exc}; retry=false; wiki_write=false; challenge={failure['global_challenge_stop']}",
            [failure_path, PROMPT_PATH, BRIEF_PATH],
        )
        failure["ledger"] = entry
        r.atomic_json(failure_path, failure)
    save_state(
        state,
        status=(
            "HARD_CHALLENGE_STOP_FROZEN" if isinstance(exc, r.GlobalChallengeStop)
            else "FIRST_UNACCEPTED_HOLD_NO_RETRY" if isinstance(exc, FirstUnacceptedHold)
            else "TECHNICAL_OR_CUSTODY_HOLD"
        ),
        failure_path=str(failure_path),
        failure_sha256=r.sha_file(failure_path),
        error=f"{type(exc).__name__}: {exc}",
        next_action="HOLD; no retry; Hwao/Duho review required",
    )
    r.report_hwao(
        f"MZR-DR HOLD: {type(exc).__name__}: {exc}; retry=false; challenge={failure['global_challenge_stop']}; "
        f"failure {failure_path} sha {r.sha_file(failure_path)}."
    )


def main():
    current_spec = spec()
    resume_pre_submit = "--resume-pre-submit" in sys.argv[1:]
    if resume_pre_submit:
        if not STATE_PATH.is_file() or not FAILURE_PATH.is_file() or PACKET_PATH.exists() or METADATA_PATH.exists() or PREFLIGHT_RECOVERY_PATH.exists():
            raise RuntimeError("MZR pre-submit recovery boundary mismatch")
        state = json.loads(STATE_PATH.read_text())
        failure = json.loads(FAILURE_PATH.read_text())
        if (
            state.get("status") != "TECHNICAL_OR_CUSTODY_HOLD"
            or state.get("error") != "PaperFailure: Deep research visible count 0"
            or state.get("failure_sha256") != r.sha_file(FAILURE_PATH)
            or failure.get("identity") is not None
            or failure.get("first_unaccepted_hold") is not False
            or failure.get("global_challenge_stop") is not False
            or failure.get("retry_performed") is not False
            or state.get("paper", {}).get("status") != "pending"
            or state.get("prompt_file_sha256") != current_spec["prompt_file_sha256"]
            or state.get("prompt_sha256") != current_spec["prompt_sha256"]
        ):
            raise RuntimeError("MZR pre-submit recovery immutable-state mismatch")
        _, _, grants = account_grants()
        own_grants = [row for row in grants if "area1_mzr" in str(row.get("payload", {}).get("holder", ""))]
        if own_grants:
            raise RuntimeError(f"MZR pre-submit recovery refused after account action: {own_grants}")
        recovery = {
            "status": "PREFLIGHT_CLASSIFIER_RECOVERED_WITH_ZERO_ACCOUNT_ACTION",
            "recovered_utc": r.utcnow(),
            "immutable_failure_path": str(FAILURE_PATH),
            "immutable_failure_sha256": r.sha_file(FAILURE_PATH),
            "failure_ledger_epoch": failure.get("ledger", {}).get("epoch"),
            "failure_ledger_entry_sha256": failure.get("ledger", {}).get("entry_sha256"),
            "root_cause": "semantic Deep research menuitemcheckbox was visible after the 500 ms transient but the old exact-text locator observed zero controls",
            "repair": "use exact semantic role menuitemcheckbox and a bounded 5-second visibility settlement; preserve the already-open menu",
            "account_submission_grants_for_run": 0,
            "prompt_send_performed": False,
            "start_research_performed": False,
            "retry_performed": False,
            "classification": "preflight-only tool-selector repair; original authorization remains unconsumed",
        }
        r.atomic_json(PREFLIGHT_RECOVERY_PATH, recovery)
        save_state(
            state,
            status="PREFLIGHT_CLASSIFIER_RECOVERED_ZERO_ACCOUNT_ACTION",
            preflight_recovery_path=str(PREFLIGHT_RECOVERY_PATH),
            preflight_recovery_sha256=r.sha_file(PREFLIGHT_RECOVERY_PATH),
            prior_failure_preserved=True,
            original_authorization_consumed=False,
        )
    else:
        for path in (PACKET_PATH, METADATA_PATH, STATE_PATH, FAILURE_PATH, PREFLIGHT_RECOVERY_PATH):
            if path.exists():
                raise RuntimeError(f"refusing nonempty MZR run boundary; output already exists: {path}")
        state = initial_state(current_spec)
        r.atomic_json(STATE_PATH, state)
    identity = None
    adapted = base_state(state)

    # Enforce the gentle account gap again inside the first account-acquire
    # boundary, so any intervening shared-account grant shifts this run rather
    # than racing the Send action.
    original_acquire_account = r.acquire_account
    first_account_action_pending = {"value": True}

    def guarded_acquire_account(client, holder, target_lease, expected_path, page):
        if first_account_action_pending["value"]:
            while True:
                message, count, latest = latest_account_grant()
                not_before = parse_utc(latest["utc"]) + timedelta(minutes=GATE_SPACING_MINUTES) if latest else now_utc()
                remaining = max(0.0, (not_before - now_utc()).total_seconds())
                if remaining <= 0:
                    break
                r.check_action(client, target_lease, "area1_mzr wait for shifted gentle account gate", expected_path, page)
                r.broker_need(client.op({"op": "heartbeat", "lease_id": target_lease["lease_id"]}), "MZR gate target heartbeat")
                save_state(state, status="WAITING_SHIFTED_GENTLE_ACCOUNT_GATE", latest_prior_account_grant=latest, account_gate_not_before=not_before.isoformat().replace("+00:00", "Z"), ledger_verify=message)
                print(json.dumps({"status": state["status"], "remaining_seconds": round(remaining, 1), "latest_holder": latest.get("holder") if latest else None}, sort_keys=True), flush=True)
                time.sleep(min(20.0, max(2.0, remaining)))
            lease = original_acquire_account(client, holder, target_lease, expected_path, page)
            first_account_action_pending["value"] = False
            return lease
        return original_acquire_account(client, holder, target_lease, expected_path, page)

    r.acquire_account = guarded_acquire_account

    try:
        wait_for_safe_gap(state)
        with sync_playwright() as playwright:
            browser = playwright.chromium.connect_over_cdp(r.BASE)
            prepare_new_chat(browser, state)
            identity = r.stage_and_submit(current_spec, adapted, browser)
            sync_from_base(state, adapted)
            plan = r.wait_for_plan(identity, current_spec, adapted, browser)
            sync_from_base(state, adapted)
            if plan == "start_required":
                prompt = PROMPT_PATH.read_text().rstrip("\n")
                try:
                    r.start_research(identity, current_spec, adapted, browser)
                    sync_from_base(state, adapted)
                except r.PaperFailure as exc:
                    if "acceptance not positively confirmed" not in str(exc):
                        raise
                    classification = classify_after_start_timeout(identity, prompt, browser)
                    if classification in {"accepted_delayed", "terminal_delayed"}:
                        adapted["papers"][0].update(
                            status="researching" if classification == "accepted_delayed" else "terminal_ready",
                            research_start_utc=r.utcnow(),
                            research_start_mode=classification,
                        )
                        sync_from_base(state, adapted)
                    elif classification == "positively_unaccepted":
                        raise FirstUnacceptedHold("MZR Deep Research Start positively unaccepted; no retry")
                    else:
                        raise FirstUnacceptedHold("MZR Deep Research Start acceptance ambiguous; no retry")
            snapshot, result_sha = r.poll_terminal(identity, current_spec, adapted, browser)
            sync_from_base(state, adapted)
            metadata = save_packet(snapshot, result_sha, identity, current_spec, state)
            browser.close()
        print(json.dumps({
            "status": state["status"],
            "packet": str(PACKET_PATH),
            "packet_sha256": metadata["packet_sha256"],
            "output_shape_pass": metadata["output_quality"]["pass"],
            "independent_identifier_verification": "PENDING",
        }, sort_keys=True), flush=True)
        return 0 if metadata["output_quality"]["pass"] else 2
    except (r.GlobalChallengeStop, FirstUnacceptedHold, r.TargetDrift, r.PaperFailure, RuntimeError) as exc:
        write_failure(state, exc, identity)
        print(json.dumps({"status": state["status"], "error": str(exc)}, sort_keys=True), flush=True)
        return 3 if isinstance(exc, r.GlobalChallengeStop) else 2


if __name__ == "__main__":
    raise SystemExit(main())
