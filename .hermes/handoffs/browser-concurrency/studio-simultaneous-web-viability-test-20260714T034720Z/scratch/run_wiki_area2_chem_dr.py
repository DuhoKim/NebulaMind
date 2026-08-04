import importlib
import json
import re
import sys
import time
from contextlib import suppress
from datetime import timedelta
from pathlib import Path

sys.path.insert(0, "scratch")
base = importlib.import_module("run_wiki_area1_mzr_dr")
from playwright.sync_api import sync_playwright

r = base.r
ramp = base.ramp
AREA_DIR = Path("/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/wiki-expansion-20260715")
BRIEF_PATH = AREA_DIR / "area2_chemical_evolution_DR_BRIEF.md"
PROMPT_PATH = AREA_DIR / "area2_chemical_evolution_DR_PROMPT.md"
PACKET_PATH = AREA_DIR / "area2_chemical_evolution_DR_PACKET.md"
METADATA_PATH = AREA_DIR / "area2_chemical_evolution_DR_PACKET.metadata.json"
STATE_PATH = AREA_DIR / "area2_chemical_evolution_DR_STATE.json"
FAILURE_PATH = AREA_DIR / "area2_chemical_evolution_DR_FAILURE.json"
GATE_SPACING_MINUTES = 20
RUN_ID = "WIKI_AREA2_CHEM_DR_20260715"
MARKER = "CHEM_DR_PACKET_COMPLETE_REFERENCE_ONLY"

r.PACKET_DIR = AREA_DIR
r.STATE_PATH = STATE_PATH
r.HWAO_TARGET = "ge-mastermind:0.0"


class FirstUnacceptedHold(RuntimeError):
    pass


def save_state(state, **updates):
    state.update(updates)
    state["updated_utc"] = r.utcnow()
    r.atomic_json(STATE_PATH, state)


def spec():
    prompt = PROMPT_PATH.read_text().rstrip("\n")
    return {
        "paper": 1,
        "paper_id": "area2_chem",
        "shortname": "galaxy_chemical_evolution_wiki_evidence_map",
        "prompt_path": str(PROMPT_PATH),
        "prompt_file_sha256": r.sha_file(PROMPT_PATH),
        "prompt_sha256": r.sha_bytes(prompt.encode()),
        "prompt_chars": len(prompt),
        "prompt_lines": len(prompt.splitlines()),
        "packet_path": str(PACKET_PATH),
        "metadata_path": str(METADATA_PATH),
        "deletion_path": str(AREA_DIR / "area2_chemical_evolution_DR_PACKET.deletion.json"),
        "failure_path": str(FAILURE_PATH),
    }


def initial_state(current_spec):
    return {
        "run_id": RUN_ID,
        "created_utc": r.utcnow(),
        "updated_utc": r.utcnow(),
        "status": "PREFLIGHT",
        "topic": "broad galaxy chemical evolution",
        "distinct_from_area1_mzr": True,
        "broad_non_agn": True,
        "advisory_only": True,
        "wiki_write_performed": False,
        "live_direct_write_authorized_for_hwao": True,
        "tori_output_boundary": str(PACKET_PATH),
        "brief_path": str(BRIEF_PATH),
        "brief_sha256": r.sha_file(BRIEF_PATH),
        "prompt_path": str(PROMPT_PATH),
        "prompt_file_sha256": current_spec["prompt_file_sha256"],
        "prompt_sha256": current_spec["prompt_sha256"],
        "minimum_pre_run_account_spacing_minutes": GATE_SPACING_MINUTES,
        "first_unaccepted_policy": "BACK_OFF_AND_HOLD_NO_RETRY",
        "hard_challenge_policy": "STOP_FREEZE_HOLD_NEVER_INTERACT",
        "paper": {**current_spec, "status": "pending"},
    }


def adapted_state(state):
    return {
        "batch_id": RUN_ID,
        "updated_utc": state["updated_utc"],
        "advisory_only": True,
        "reference_only": True,
        "papers": [state["paper"]],
    }


def sync_state(state, adapted):
    state["paper"] = adapted["papers"][0]
    save_state(state)


def latest_account_grant():
    message, entries, grants = ramp.ledger_snapshot()
    account = [entry for entry in grants if entry.get("payload", {}).get("kind") == "account-submission"]
    if not account:
        return message, len(entries), None
    row = account[-1]
    return message, len(entries), {"utc": row["utc"], "ledger_epoch": row["epoch"], **row["payload"]}


def wait_for_safe_gap(state):
    while True:
        broker, live = ramp.broker_snapshot()
        if broker.get("frozen"):
            raise r.GlobalChallengeStop("broker frozen before Area 2 chemical-evolution dispatch")
        message, count, latest = latest_account_grant()
        if message != f"OK ({count} entries)":
            raise RuntimeError(f"ledger verification mismatch: {message} entries={count}")
        live_account = [row for row in live if row.get("kind") == "account-submission"]
        not_before = base.parse_utc(latest["utc"]) + timedelta(minutes=GATE_SPACING_MINUTES) if latest else base.now_utc()
        remaining = max(0.0, (not_before - base.now_utc()).total_seconds())
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
    holder = "goru-wiki-area2-chem-new-chat"
    client = r.UDSClient(r.SOCK)
    lease = None
    try:
        lease = r.acquire_target(client, holder, "write", ttl=300)
        page = r.exact_page(browser, record["path"])
        if r.page_challenge(page):
            r.freeze_for_challenge(client, holder, "area2_chem", "pre-dispatch current-route classification")
        r.check_action(client, lease, "area2_chem navigate to new chat", record["path"], page)
        page.goto("https://gemini.google.com/app", wait_until="domcontentloaded", timeout=30000)
        page.wait_for_timeout(1200)
        if r.page_challenge(page):
            r.freeze_for_challenge(client, holder, "area2_chem", "post-navigation new-chat classification")
        if not r.target_matches("/app", page):
            raise r.TargetDrift("new-chat route failed exact verification")
        save_state(state, prior_route=record["path"], status="NEW_CHAT_READY")
    finally:
        r.release_lease(client, lease)
        client.close()


def classify_after_start_timeout(identity, prompt, browser):
    path = identity["conversation_path"]
    holder = "goru-wiki-area2-chem-start-settlement"
    client = r.UDSClient(r.SOCK)
    lease = None
    try:
        lease = r.acquire_target(client, holder, "read", ttl=300)
        page = r.exact_page(browser, path)
        if r.page_challenge(page):
            r.freeze_for_challenge(client, holder, "area2_chem", "post-Start timeout settlement")
        if not r.target_matches(path, page):
            r.check_action(client, lease, "area2_chem fail-closed Start-timeout settlement", path, page)
        snapshot = r.page_snapshot(page)
        all_text = " ".join(item["text"] for item in snapshot.get("messages", []))
        active = snapshot["research"] or (snapshot["stop"] and any(token in all_text for token in (
            "While I'm researching", "Researching ", "Creating visuals for the report", "Writing your report"
        )))
        if active:
            return "accepted_delayed"
        terminal = len(snapshot.get("messages", [])) >= 3 and len(snapshot["messages"][-1]["text"]) >= 2000 and not snapshot["stop"] and not snapshot["research"]
        if terminal:
            return "terminal_delayed"
        start = page.get_by_role("button", name="Start research", exact=True)
        enabled = [start.nth(index) for index in range(start.count()) if start.nth(index).is_visible() and not start.nth(index).is_disabled()]
        if len(enabled) == 1 and r.current_prompt_identity(page, prompt) and not snapshot["failure"]:
            return "positively_unaccepted"
        return "ambiguous_hold"
    finally:
        r.release_lease(client, lease)
        client.close()


def output_quality(result):
    heading_patterns = [
        r"(?m)^\s*(?:##\s*)?1\. Established findings\s*$",
        r"(?m)^\s*(?:##\s*)?2\. Open debates and tensions\s*$",
        r"(?m)^\s*(?:##\s*)?3\. Key measurements and numbers\s*$",
        r"(?m)^\s*(?:##\s*)?4\. What remains unknown\s*$",
        r"(?m)^\s*(?:##\s*)?5\. DO_NOT_USE_UNVERIFIED\s*$",
        r"(?m)^\s*(?:##\s*)?6\. Source identity ledger\s*$",
    ]
    source_lines = re.findall(
        r"(?im)^.*\(\d{4}[a-z]?\s*,\s*[^)]+\)\s*\|\s*(?:DOI|arXiv|ADS):.*\|\s*role=(?:established|debate|caveat|future)\s*\|",
        result,
    )
    coverage = {
        "nucleosynthetic_timescales": bool(re.search(r"(?i)core-collapse|Type Ia|AGB", result)),
        "abundance_ratios": bool(re.search(r"(?i)alpha/Fe|\[.?/Fe\]|N/O|C/O", result)),
        "radial_gradients": bool(re.search(r"(?i)radial metallicity gradient|metallicity gradients", result)),
        "flow_models": bool(re.search(r"(?i)closed-box|leaky-box|gas.regulator|inflow|outflow", result)),
        "g_dwarf": bool(re.search(r"(?i)G[- ]dwarf problem", result)),
    }
    checks = {
        "semantic_headings_present": all(re.search(pattern, result) for pattern in heading_patterns),
        "terminal_marker_present": result.rstrip().endswith(MARKER),
        "established_ids": len(set(re.findall(r"\bCHEM-E\d{2}\b", result))),
        "debate_ids": len(set(re.findall(r"\bCHEM-D\d{2}\b", result))),
        "measurement_ids": len(set(re.findall(r"\bCHEM-N\d{2}\b", result))),
        "unknown_ids": len(set(re.findall(r"\bCHEM-U\d{2}\b", result))),
        "required_format_source_line_count": len(source_lines),
        "doi_count": len(set(re.findall(r"(?i)\b10\.\d{4,9}/[-._;()/:A-Z0-9]+", result))),
        "arxiv_count": len(set(re.findall(r"(?i)\barXiv\s*:\s*(?:astro-ph/)?\d{4}\.\d{4,5}(?:v\d+)?\b", result))),
        "ads_count": len(set(re.findall(r"(?i)\bADS\s*:\s*([12]\d{3}[A-Za-z0-9.&]{8,})", result))),
        "do_not_use_section_present": bool(re.search(heading_patterns[4], result)),
        "uncited_not_usable_protocol_present": "UNCITED_NOT_USABLE" in result or "NONE — all cited sources passed" in result,
        "coverage": coverage,
    }
    checks["pass"] = (
        checks["semantic_headings_present"]
        and checks["terminal_marker_present"]
        and checks["established_ids"] >= 8
        and checks["debate_ids"] >= 6
        and checks["measurement_ids"] >= 6
        and checks["unknown_ids"] >= 4
        and checks["required_format_source_line_count"] >= 20
        and checks["doi_count"] + checks["arxiv_count"] + checks["ads_count"] >= 20
        and checks["uncited_not_usable_protocol_present"]
        and all(coverage.values())
    )
    return checks


def save_packet(snapshot, result_sha, identity, current_spec, state):
    result = snapshot["messages"][-1]["text"]
    links = []
    seen = set()
    for item in snapshot.get("links", []):
        if r.keep_source(item) and item["href"] not in seen:
            seen.add(item["href"])
            links.append(item)
    quality = output_quality(result)
    captured_utc = r.utcnow()
    lines = [
        "# Area 2 raw Deep Research packet — galaxy chemical evolution",
        "",
        "advisory_only: true",
        "broad_non_agn: true",
        "distinct_from_area1_mzr: true",
        "wiki_write_performed_by_tori: false",
        "identifier_verification_required_before_live_wiki_use: true",
        "",
        f"Brief: `{BRIEF_PATH}`",
        f"Brief SHA-256: `{r.sha_file(BRIEF_PATH)}`",
        f"Prompt: `{PROMPT_PATH}`",
        f"Prompt file SHA-256: `{current_spec['prompt_file_sha256']}`",
        f"Submitted prompt text SHA-256: `{current_spec['prompt_sha256']}`",
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
    lines.extend([f"- {item['label'] or '(unlabeled)'} — {item['href']}" for item in links] or ["- No external anchors exposed; use only independently reconciled identifiers."])
    lines.extend([
        "",
        "## Custody and safety receipt",
        "",
        "- Raw Deep Research source discovery only; independent composite identifier and claim-boundary verification remains required before live wiki mutation.",
        "- No DB, wiki, trust-score, claim/evidence, code, manuscript, deploy, git, publish, cron, billing, credential, account-setting, or unrelated-conversation mutation was performed.",
        "- No conversation deletion was authorized or performed.",
        "",
    ])
    r.atomic_write(PACKET_PATH, "\n".join(lines))
    metadata = {
        "run_id": RUN_ID,
        "topic": "broad galaxy chemical evolution",
        "distinct_from_area1_mzr": True,
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
        raise r.PaperFailure("saved Area 2 packet wrapper markers absent")
    saved_result = packet_text.rsplit(raw_start, 1)[1].rsplit(raw_end, 1)[0]
    if len(saved_result) != len(result) or r.sha_bytes(saved_result.encode()) != result_sha:
        raise r.PaperFailure("saved Area 2 raw-result custody mismatch")
    metadata_read = json.loads(METADATA_PATH.read_text())
    if metadata_read["packet_sha256"] != r.sha_file(PACKET_PATH) or metadata_read["result_text_sha256"] != result_sha:
        raise r.PaperFailure("saved Area 2 metadata custody mismatch")
    entry = r.journal_entry(
        "wiki_area2_chem_dr_packet_saved_verified",
        f"Area2 broad non-AGN chemical-evolution raw packet saved; conversation_id={identity['conversation_id']}; result_sha256={result_sha}; packet_sha256={metadata['packet_sha256']}; metadata_sha256={r.sha_file(METADATA_PATH)}; output_shape_pass={quality['pass']}; wiki_write=false; conversation_delete=false; independent verification pending.",
        [PACKET_PATH, METADATA_PATH, PROMPT_PATH, BRIEF_PATH],
    )
    save_state(
        state,
        status="PACKET_LANDED_PENDING_INDEPENDENT_IDENTIFIER_VERIFICATION" if quality["pass"] else "PACKET_LANDED_OUTPUT_SHAPE_HOLD",
        paper={**state["paper"], "status": "packet_saved", "packet_sha256": metadata["packet_sha256"], "metadata_sha256": r.sha_file(METADATA_PATH), "result_chars": len(result), "result_text_sha256": result_sha, "output_quality": quality, "save_ledger": entry},
        packet_path=str(PACKET_PATH),
        packet_sha256=metadata["packet_sha256"],
        metadata_sha256=r.sha_file(METADATA_PATH),
        ledger_verify=entry["verify"],
        next_action="Tori independently reconciles composite source identities and claim boundaries; Hwao must hold live wiring until VERIFIED",
    )
    r.report_hwao(
        f"CHEM-DR raw packet landed at {PACKET_PATH}; packet sha {metadata['packet_sha256']}; output-shape pass={quality['pass']}; HOLD live wiring until independent ADS reconciliation. No wiki write or conversation deletion performed."
    )
    return metadata


def write_failure(state, exc, identity=None):
    failure_path = FAILURE_PATH
    attempt = 2
    while failure_path.exists():
        failure_path = AREA_DIR / f"area2_chemical_evolution_DR_FAILURE_{attempt}.json"
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
        "actions_not_taken": ["no retry", "no wiki/DB/trust write", "no deployment", "no git action", "no conversation deletion"],
    }
    r.atomic_json(failure_path, failure)
    with suppress(Exception):
        entry = r.journal_entry(
            "wiki_area2_chem_dr_hold",
            f"Area2 chemical-evolution DR hold: {type(exc).__name__}: {exc}; retry=false; wiki_write=false; challenge={failure['global_challenge_stop']}",
            [failure_path, PROMPT_PATH, BRIEF_PATH],
        )
        failure["ledger"] = entry
        r.atomic_json(failure_path, failure)
    save_state(
        state,
        status="HARD_CHALLENGE_STOP_FROZEN" if isinstance(exc, r.GlobalChallengeStop) else "FIRST_UNACCEPTED_HOLD_NO_RETRY" if isinstance(exc, FirstUnacceptedHold) else "TECHNICAL_OR_CUSTODY_HOLD",
        failure_path=str(failure_path),
        failure_sha256=r.sha_file(failure_path),
        error=f"{type(exc).__name__}: {exc}",
        next_action="HOLD; no retry; Hwao/Duho review required",
    )
    r.report_hwao(f"CHEM-DR HOLD: {type(exc).__name__}: {exc}; retry=false; challenge={failure['global_challenge_stop']}; failure {failure_path} sha {r.sha_file(failure_path)}.")


def main():
    current_spec = spec()
    for path in (PACKET_PATH, METADATA_PATH, STATE_PATH, FAILURE_PATH):
        if path.exists():
            raise RuntimeError(f"refusing nonempty Area 2 run boundary: {path}")
    state = initial_state(current_spec)
    r.atomic_json(STATE_PATH, state)
    identity = None
    adapted = adapted_state(state)
    original_acquire_account = r.acquire_account
    first_account_action_pending = {"value": True}

    def guarded_acquire_account(client, holder, target_lease, expected_path, page):
        if first_account_action_pending["value"]:
            while True:
                message, count, latest = latest_account_grant()
                not_before = base.parse_utc(latest["utc"]) + timedelta(minutes=GATE_SPACING_MINUTES) if latest else base.now_utc()
                remaining = max(0.0, (not_before - base.now_utc()).total_seconds())
                if remaining <= 0:
                    break
                r.check_action(client, target_lease, "area2_chem wait for shifted gentle account gate", expected_path, page)
                r.broker_need(client.op({"op": "heartbeat", "lease_id": target_lease["lease_id"]}), "Area2 gate target heartbeat")
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
            sync_state(state, adapted)
            plan = r.wait_for_plan(identity, current_spec, adapted, browser)
            sync_state(state, adapted)
            if plan == "start_required":
                prompt = PROMPT_PATH.read_text().rstrip("\n")
                try:
                    r.start_research(identity, current_spec, adapted, browser)
                    sync_state(state, adapted)
                except r.PaperFailure as exc:
                    if "acceptance not positively confirmed" not in str(exc):
                        raise
                    classification = classify_after_start_timeout(identity, prompt, browser)
                    if classification in {"accepted_delayed", "terminal_delayed"}:
                        adapted["papers"][0].update(status="researching" if classification == "accepted_delayed" else "terminal_ready", research_start_utc=r.utcnow(), research_start_mode=classification)
                        sync_state(state, adapted)
                    elif classification == "positively_unaccepted":
                        raise FirstUnacceptedHold("Area 2 Deep Research Start positively unaccepted; no retry")
                    else:
                        raise FirstUnacceptedHold("Area 2 Deep Research Start acceptance ambiguous; no retry")
            snapshot, result_sha = r.poll_terminal(identity, current_spec, adapted, browser)
            sync_state(state, adapted)
            metadata = save_packet(snapshot, result_sha, identity, current_spec, state)
            browser.close()
        print(json.dumps({"status": state["status"], "packet": str(PACKET_PATH), "packet_sha256": metadata["packet_sha256"], "output_shape_pass": metadata["output_quality"]["pass"], "independent_identifier_verification": "PENDING"}, sort_keys=True), flush=True)
        return 0 if metadata["output_quality"]["pass"] else 2
    except (r.GlobalChallengeStop, FirstUnacceptedHold, r.TargetDrift, r.PaperFailure, RuntimeError) as exc:
        write_failure(state, exc, identity)
        print(json.dumps({"status": state["status"], "error": str(exc)}, sort_keys=True), flush=True)
        return 3 if isinstance(exc, r.GlobalChallengeStop) else 2


if __name__ == "__main__":
    raise SystemExit(main())
