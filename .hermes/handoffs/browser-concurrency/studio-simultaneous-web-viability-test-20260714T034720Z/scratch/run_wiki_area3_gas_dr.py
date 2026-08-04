import importlib
import json
import re
import sys
import time
from contextlib import suppress
from datetime import timedelta
from pathlib import Path
from typing import Any

sys.path.insert(0, "scratch")
q: Any = importlib.import_module("run_wiki_area2_chem_dr")
r = q.r
ramp = q.ramp
base = q.base

AREA_DIR = Path("/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/wiki-expansion-20260715")
BRIEF_PATH = AREA_DIR / "area3_gas_depletion_DR_BRIEF.md"
PROMPT_PATH = AREA_DIR / "area3_gas_depletion_DR_PROMPT.md"
PACKET_PATH = AREA_DIR / "area3_gas_depletion_DR_PACKET.md"
METADATA_PATH = AREA_DIR / "area3_gas_depletion_DR_PACKET.metadata.json"
STATE_PATH = AREA_DIR / "area3_gas_depletion_DR_STATE.json"
FAILURE_PATH = AREA_DIR / "area3_gas_depletion_DR_FAILURE.json"
RUN_ID = "WIKI_AREA3_GAS_DR_20260715"
MARKER = "GAS_DR_PACKET_COMPLETE_REFERENCE_ONLY"
HUMAN_GAP_NOT_BEFORE = "2026-07-15T11:17:36Z"
SPACING_MINUTES = 20

for name, value in {
    "AREA_DIR": AREA_DIR,
    "BRIEF_PATH": BRIEF_PATH,
    "PROMPT_PATH": PROMPT_PATH,
    "PACKET_PATH": PACKET_PATH,
    "METADATA_PATH": METADATA_PATH,
    "STATE_PATH": STATE_PATH,
    "FAILURE_PATH": FAILURE_PATH,
    "RUN_ID": RUN_ID,
    "MARKER": MARKER,
    "GATE_SPACING_MINUTES": SPACING_MINUTES,
}.items():
    setattr(q, name, value)
r.PACKET_DIR = AREA_DIR
r.STATE_PATH = STATE_PATH
r.HWAO_TARGET = "ge-mastermind:0.0"


def spec():
    prompt = PROMPT_PATH.read_text().rstrip("\n")
    return {
        "paper": 1,
        "paper_id": "area3_gas",
        "shortname": "gas_depletion_star_formation_efficiency_wiki_evidence_map",
        "prompt_path": str(PROMPT_PATH),
        "prompt_file_sha256": r.sha_file(PROMPT_PATH),
        "prompt_sha256": r.sha_bytes(prompt.encode()),
        "prompt_chars": len(prompt),
        "prompt_lines": len(prompt.splitlines()),
        "packet_path": str(PACKET_PATH),
        "metadata_path": str(METADATA_PATH),
        "deletion_path": str(AREA_DIR / "area3_gas_depletion_DR_PACKET.deletion.json"),
        "failure_path": str(FAILURE_PATH),
    }


def initial_state(current_spec):
    prior = r.target_record()
    return {
        "run_id": RUN_ID,
        "created_utc": r.utcnow(),
        "updated_utc": r.utcnow(),
        "status": "WAITING_HUMAN_LIKE_GAP",
        "topic": "gas depletion and star-formation efficiency",
        "broad_non_agn": True,
        "distinct_from_areas1_2": True,
        "advisory_only": True,
        "wiki_write_performed": False,
        "live_direct_write_authorized_for_hwao": True,
        "tori_output_boundary": str(PACKET_PATH),
        "brief_path": str(BRIEF_PATH),
        "brief_sha256": r.sha_file(BRIEF_PATH),
        "prompt_path": str(PROMPT_PATH),
        "prompt_file_sha256": current_spec["prompt_file_sha256"],
        "prompt_sha256": current_spec["prompt_sha256"],
        "prior_route": prior.get("path") if prior else None,
        "human_gap_anchor": "Area 2 verified-final ledger event at 2026-07-15T10:57:36Z",
        "human_gap_not_before": HUMAN_GAP_NOT_BEFORE,
        "minimum_post_area2_gap_minutes": SPACING_MINUTES,
        "minimum_pre_run_account_spacing_minutes": SPACING_MINUTES,
        "first_unaccepted_policy": "BACK_OFF_AND_HOLD_NO_RETRY",
        "hard_challenge_policy": "STOP_FREEZE_HOLD_NEVER_INTERACT",
        "paper": {**current_spec, "status": "pending"},
    }


def wait_for_safe_gap(state):
    human_gate = base.parse_utc(HUMAN_GAP_NOT_BEFORE)
    while True:
        broker, live = ramp.broker_snapshot()
        if broker.get("frozen"):
            raise r.GlobalChallengeStop("broker frozen before Area 3 gas-depletion dispatch")
        message, count, latest = q.latest_account_grant()
        if message != f"OK ({count} entries)":
            raise RuntimeError(f"ledger verification mismatch: {message} entries={count}")
        live_account = [row for row in live if row.get("kind") == "account-submission"]
        account_gate = base.parse_utc(latest["utc"]) + timedelta(minutes=SPACING_MINUTES) if latest else base.now_utc()
        not_before = max(human_gate, account_gate)
        remaining = max(0.0, (not_before - base.now_utc()).total_seconds())
        q.save_state(
            state,
            status="WAITING_HUMAN_LIKE_GAP" if remaining > 0 or live_account else "ACCOUNT_GATE_READY",
            latest_prior_account_grant=latest,
            account_gate_not_before=not_before.isoformat().replace("+00:00", "Z"),
            ledger_verify=message,
            live_account_leases=live_account,
        )
        if remaining <= 0 and not live_account:
            q.save_state(state, human_gap_passed_utc=r.utcnow())
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
        q.save_state(state, status="NEW_CHAT_READY", prior_route=record["path"])
        return
    holder = "goru-wiki-area3-gas-new-chat"
    client = r.UDSClient(r.SOCK)
    lease = None
    try:
        lease = r.acquire_target(client, holder, "write", ttl=300)
        page = r.exact_page(browser, record["path"])
        if r.page_challenge(page):
            r.freeze_for_challenge(client, holder, "area3_gas", "pre-dispatch current-route classification")
        r.check_action(client, lease, "area3_gas navigate to new chat", record["path"], page)
        page.goto("https://gemini.google.com/app", wait_until="domcontentloaded", timeout=30000)
        page.wait_for_timeout(1200)
        if r.page_challenge(page):
            r.freeze_for_challenge(client, holder, "area3_gas", "post-navigation new-chat classification")
        if not r.target_matches("/app", page):
            raise r.TargetDrift("new-chat route failed exact verification")
        q.save_state(state, prior_route=record["path"], status="NEW_CHAT_READY")
        r.journal_entry(
            "wiki_area3_gas_new_chat_prepared",
            "Area 3 exact Pro target navigated to /app after the human-like post-Area-2 gap; no account submission yet.",
            [BRIEF_PATH, PROMPT_PATH],
        )
    finally:
        if lease:
            with suppress(Exception):
                r.release_lease(client, lease)
        client.close()


def classify_after_start_timeout(identity, prompt, browser):
    path = identity["conversation_path"]
    holder = "goru-wiki-area3-gas-start-settlement"
    client = r.UDSClient(r.SOCK)
    lease = None
    try:
        lease = r.acquire_target(client, holder, "read", ttl=300)
        page = r.exact_page(browser, path)
        if r.page_challenge(page):
            r.freeze_for_challenge(client, holder, "area3_gas", "post-Start timeout settlement")
        if not r.target_matches(path, page):
            r.check_action(client, lease, "area3_gas fail-closed Start-timeout settlement", path, page)
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
        enabled = [start.nth(i) for i in range(start.count()) if start.nth(i).is_visible() and not start.nth(i).is_disabled()]
        if len(enabled) == 1 and r.current_prompt_identity(page, prompt) and not snapshot["failure"]:
            return "positively_unaccepted"
        return "ambiguous_hold"
    finally:
        if lease:
            with suppress(Exception):
                r.release_lease(client, lease)
        client.close()


def output_quality(result):
    lower = result.lower()

    def id_count(prefix):
        return len(set(re.findall(rf"\[GAS-{prefix}\d{{2}}\]", result)))

    headings = [
        "1. established findings",
        "2. open debates and tensions",
        "3. key measurements and numbers",
        "4. what remains unknown",
        "5. do_not_use_unverified",
        "6. source identity ledger",
    ]
    source_lines = re.findall(
        r"(?mi)^.+\(\d{4},\s*[^\n)]+\)\s*\|\s*(?:DOI|arXiv|ADS):[^\n]+\|\s*role=(?:orientation|established|measurement|debate|caveat|future|theory)\s*\|\s*.+$",
        result,
    )
    coverage = {
        "hi_h2_distinct": bool(re.search(r"\bHI\b|atomic gas", result, re.I)) and bool(re.search(r"\bH2\b|molecular gas", result, re.I)),
        "depletion_sfe": "depletion" in lower and "efficiency" in lower,
        "star_formation_law": "kennicutt" in lower or "schmidt" in lower,
        "quenching_modes": "starvation" in lower and ("removal" in lower or "stripping" in lower),
        "cosmic_gas": "aspecs" in lower or "phibss" in lower or "cosmic" in lower,
        "conversion_caveats": "alpha_co" in lower or "x_co" in lower or "conversion factor" in lower,
    }
    checks = {
        "semantic_headings_present": all(h in lower for h in headings),
        "established_ids": id_count("E"),
        "debate_ids": id_count("D"),
        "measurement_ids": id_count("N"),
        "unknown_ids": id_count("U"),
        "required_format_source_line_count": len(source_lines),
        "doi_count": len(re.findall(r"DOI:\s*10\.\S+", result, re.I)),
        "arxiv_count": len(re.findall(r"arXiv:\s*(?:\d{4}\.\d{4,5}|[a-z-]+/\d{7})", result, re.I)),
        "ads_count": len(re.findall(r"ADS:\s*\S+", result, re.I)),
        "do_not_use_section_present": "do_not_use_unverified" in lower,
        "uncited_not_usable_protocol_present": "uncited_not_usable" in lower,
        "terminal_marker_present": MARKER in result,
        "coverage": coverage,
    }
    checks["pass"] = bool(
        checks["semantic_headings_present"]
        and checks["established_ids"] >= 10
        and checks["debate_ids"] >= 7
        and checks["measurement_ids"] >= 7
        and checks["unknown_ids"] >= 5
        and checks["required_format_source_line_count"] >= 20
        and checks["do_not_use_section_present"]
        and checks["uncited_not_usable_protocol_present"]
        and checks["terminal_marker_present"]
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
        "# Area 3 raw Deep Research packet — gas depletion and star-formation efficiency",
        "",
        "advisory_only: true",
        "broad_non_agn: true",
        "distinct_from_areas1_2: true",
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
        "- Raw source discovery only; independent composite identifier and claim-boundary verification remains required before live wiki mutation.",
        "- No DB, wiki, trust-score, claim/evidence, code, deploy, git, publish, cron, billing, credential, account-setting, or unrelated-conversation mutation was performed.",
        "- No conversation deletion was authorized or performed.",
        "",
    ])
    r.atomic_write(PACKET_PATH, "\n".join(lines))
    metadata = {
        "run_id": RUN_ID,
        "topic": "gas depletion and star-formation efficiency",
        "broad_non_agn": True,
        "distinct_from_areas1_2": True,
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
        raise r.PaperFailure("saved Area 3 packet wrapper markers absent")
    saved_result = packet_text.rsplit(raw_start, 1)[1].rsplit(raw_end, 1)[0]
    if len(saved_result) != len(result) or r.sha_bytes(saved_result.encode()) != result_sha:
        raise r.PaperFailure("saved Area 3 raw-result custody mismatch")
    metadata_read = json.loads(METADATA_PATH.read_text())
    if metadata_read["packet_sha256"] != r.sha_file(PACKET_PATH) or metadata_read["result_text_sha256"] != result_sha:
        raise r.PaperFailure("saved Area 3 metadata custody mismatch")
    entry = r.journal_entry(
        "wiki_area3_gas_dr_packet_saved_verified",
        f"Area3 broad non-AGN gas-depletion/SFE raw packet saved; conversation_id={identity['conversation_id']}; result_sha256={result_sha}; packet_sha256={metadata['packet_sha256']}; metadata_sha256={r.sha_file(METADATA_PATH)}; output_shape_pass={quality['pass']}; wiki_write=false; conversation_delete=false; independent verification pending.",
        [PACKET_PATH, METADATA_PATH, PROMPT_PATH, BRIEF_PATH],
    )
    q.save_state(
        state,
        status="PACKET_LANDED_PENDING_INDEPENDENT_IDENTIFIER_VERIFICATION" if quality["pass"] else "PACKET_LANDED_OUTPUT_SHAPE_HOLD",
        paper={**state["paper"], "status": "packet_saved", "packet_sha256": metadata["packet_sha256"], "metadata_sha256": r.sha_file(METADATA_PATH), "result_chars": len(result), "result_text_sha256": result_sha, "output_quality": quality, "save_ledger": entry},
        packet_path=str(PACKET_PATH),
        packet_sha256=metadata["packet_sha256"],
        metadata_sha256=r.sha_file(METADATA_PATH),
        ledger_verify=entry["verify"],
        next_action="Tori independently reconciles composite identities and claim boundaries; Hwao holds live wiring until VERIFIED",
    )
    r.report_hwao(
        f"GAS-DR raw packet landed at {PACKET_PATH}; packet sha {metadata['packet_sha256']}; output-shape pass={quality['pass']}; HOLD live wiring until independent composite-ID reconciliation. No wiki write or conversation deletion."
    )
    return metadata


def write_failure(state, exc, identity=None):
    failure_path = FAILURE_PATH
    attempt = 2
    while failure_path.exists():
        failure_path = AREA_DIR / f"area3_gas_depletion_DR_FAILURE_{attempt}.json"
        attempt += 1
    failure = {
        "run_id": RUN_ID,
        "failed_utc": r.utcnow(),
        "status": state.get("status"),
        "error_class": type(exc).__name__,
        "error": str(exc),
        "identity": identity,
        "global_challenge_stop": isinstance(exc, r.GlobalChallengeStop),
        "first_unaccepted_hold": isinstance(exc, q.FirstUnacceptedHold),
        "retry_performed": False,
        "actions_not_taken": ["no retry", "no wiki/DB/trust write", "no deployment", "no git action", "no conversation deletion"],
    }
    r.atomic_json(failure_path, failure)
    with suppress(Exception):
        entry = r.journal_entry(
            "wiki_area3_gas_dr_hold",
            f"Area3 gas-depletion/SFE DR hold: {type(exc).__name__}: {exc}; retry=false; wiki_write=false; challenge={failure['global_challenge_stop']}",
            [failure_path, PROMPT_PATH, BRIEF_PATH],
        )
        failure["ledger"] = entry
        r.atomic_json(failure_path, failure)
    q.save_state(
        state,
        status="HARD_CHALLENGE_STOP_FROZEN" if isinstance(exc, r.GlobalChallengeStop) else "FIRST_UNACCEPTED_HOLD_NO_RETRY" if isinstance(exc, q.FirstUnacceptedHold) else "TECHNICAL_OR_CUSTODY_HOLD",
        failure_path=str(failure_path),
        failure_sha256=r.sha_file(failure_path),
        error=f"{type(exc).__name__}: {exc}",
        next_action="HOLD; no retry; Hwao/Duho review required",
    )
    r.report_hwao(f"GAS-DR HOLD: {type(exc).__name__}: {exc}; retry=false; challenge={failure['global_challenge_stop']}; failure {failure_path} sha {r.sha_file(failure_path)}.")


for name, fn in {
    "spec": spec,
    "initial_state": initial_state,
    "wait_for_safe_gap": wait_for_safe_gap,
    "prepare_new_chat": prepare_new_chat,
    "classify_after_start_timeout": classify_after_start_timeout,
    "output_quality": output_quality,
    "save_packet": save_packet,
    "write_failure": write_failure,
}.items():
    setattr(q, name, fn)

if __name__ == "__main__":
    raise SystemExit(q.main())
