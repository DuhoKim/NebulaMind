import importlib
import json
import re
import sys
import time
from contextlib import suppress
from datetime import timedelta
from pathlib import Path
from typing import Any
from urllib.parse import urlparse

from playwright.sync_api import TimeoutError as PlaywrightTimeoutError

sys.path.insert(0, "scratch")
a: Any = importlib.import_module("run_wiki_area3_gas_dr")
q = a.q
r = a.r
ramp = a.ramp
base = a.base

AREA_DIR = Path("/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/wiki-expansion-20260715")
QUEUE_PATH = AREA_DIR / "REVIEW_BASE_QUEUE.md"
MANIFEST_PATH = AREA_DIR / "REVIEW_BASE_DR_MANIFEST.json"
PROMPT_PATH = AREA_DIR / "area_review_11_wechsler_tinker_2018_DR_PROMPT.md"
RAW_PACKET_PATH = AREA_DIR / "area_review_11_wechsler_tinker_2018_DR_RAW_PACKET.md"
RAW_METADATA_PATH = AREA_DIR / "area_review_11_wechsler_tinker_2018_DR_PACKET.raw.metadata.json"
CANONICAL_PACKET_PATH = AREA_DIR / "area_review_11_wechsler_tinker_2018_DR_PACKET.md"
STATE_PATH = AREA_DIR / "area_review_11_wechsler_tinker_2018_DR_STATE.json"
FAILURE_PATH = AREA_DIR / "area_review_11_wechsler_tinker_2018_DR_FAILURE.json"
RUN_ID = "REVIEW_BASE_11_WECHSLER_TINKER_2018"
MARKER = "REVIEW_BASE_11_DR_COMPLETE_REFERENCE_ONLY"
FIRST_NOT_BEFORE = "2026-07-16T02:38:44.566432Z"
SPACING_MINUTES = 28

for name, value in {
    "AREA_DIR": AREA_DIR,
    "BRIEF_PATH": QUEUE_PATH,
    "PROMPT_PATH": PROMPT_PATH,
    "PACKET_PATH": RAW_PACKET_PATH,
    "METADATA_PATH": RAW_METADATA_PATH,
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


def update_manifest(status, **fields):
    manifest = json.loads(MANIFEST_PATH.read_text())
    manifest["status"] = status
    manifest["updated_utc"] = r.utcnow()
    item = next(row for row in manifest["queue"] if row["id"] == 11)
    item.update(fields)
    item["status"] = status.lower()
    r.atomic_json(MANIFEST_PATH, manifest)


def spec():
    prompt = PROMPT_PATH.read_text().rstrip("\n")
    return {
        # The inherited one-item batch state is indexed from one; queue identity
        # remains item 11 in queue_item/paper_id and artifact names.
        "paper": 1,
        "paper_id": "review_base_11",
        "shortname": "wechsler_tinker_2018_review_source_base",
        "prompt_path": str(PROMPT_PATH),
        "prompt_file_sha256": r.sha_file(PROMPT_PATH),
        "prompt_sha256": r.sha_bytes(prompt.encode()),
        "prompt_chars": len(prompt),
        "prompt_lines": len(prompt.splitlines()),
        "packet_path": str(RAW_PACKET_PATH),
        "metadata_path": str(RAW_METADATA_PATH),
        "canonical_packet_path": str(CANONICAL_PACKET_PATH),
        "failure_path": str(FAILURE_PATH),
    }


def initial_state(current_spec):
    prior = r.target_record()
    return {
        "run_id": RUN_ID,
        "created_utc": r.utcnow(),
        "updated_utc": r.utcnow(),
        "status": "WAITING_STANDARD_GAP",
        "mission_id": "GALAXY_REVIEW_BASE_DR_20260715",
        "queue_item": 11,
        "review": "Wechsler & Tinker 2018 — The Connection Between Galaxies and Their Dark Matter Halos",
        "review_identity": {
            "doi": "10.1146/annurev-astro-081817-051756",
            "arxiv": "1804.03097",
            "ads_bibcode": "2018ARA&A..56..435W",
            "preflight_status": "PASS_ADS_CROSSREF_ARXIV",
        },
        "advisory_only": True,
        "wiki_write_performed": False,
        "canonical_packet_released": False,
        "canonical_packet_path": str(CANONICAL_PACKET_PATH),
        "raw_packet_path": str(RAW_PACKET_PATH),
        "queue_path": str(QUEUE_PATH),
        "queue_sha256": r.sha_file(QUEUE_PATH),
        "manifest_path": str(MANIFEST_PATH),
        "prompt_path": str(PROMPT_PATH),
        "prompt_sha256": current_spec["prompt_sha256"],
        "prior_route": prior.get("path") if prior else None,
        "first_not_before_utc": FIRST_NOT_BEFORE,
        "assigned_gap_minutes": SPACING_MINUTES,
        "first_unaccepted_policy": "STOP_QUEUE_HOLD_NO_RETRY",
        "hard_challenge_policy": "FREEZE_STOP_QUEUE_HOLD_NEVER_INTERACT",
        "paper": {**current_spec, "status": "pending"},
    }


def wait_for_safe_gap(state):
    first_gate = base.parse_utc(FIRST_NOT_BEFORE)
    while True:
        broker, live = ramp.broker_snapshot()
        if broker.get("frozen"):
            raise r.GlobalChallengeStop("broker frozen before Review Base item 11 dispatch")
        message, count, latest = q.latest_account_grant()
        if message != f"OK ({count} entries)":
            raise RuntimeError(f"ledger verification mismatch: {message} entries={count}")
        live_account = [row for row in live if row.get("kind") == "account-submission"]
        account_gate = base.parse_utc(latest["utc"]) + timedelta(minutes=SPACING_MINUTES) if latest else base.now_utc()
        not_before = max(first_gate, account_gate)
        remaining = max(0.0, (not_before - base.now_utc()).total_seconds())
        q.save_state(
            state,
            status="WAITING_STANDARD_GAP" if remaining > 0 or live_account else "ACCOUNT_GATE_READY",
            latest_prior_account_grant=latest,
            account_gate_not_before=not_before.isoformat().replace("+00:00", "Z"),
            ledger_verify=message,
            live_account_leases=live_account,
        )
        update_manifest("WAITING_ITEM_11_STANDARD_GAP" if remaining > 0 or live_account else "ITEM_11_ACCOUNT_GATE_READY", account_gate_not_before=state["account_gate_not_before"])
        if remaining <= 0 and not live_account:
            return
        print(json.dumps({"status": state["status"], "not_before": state["account_gate_not_before"], "remaining_seconds": round(remaining, 1), "latest_holder": latest.get("holder") if latest else None}, sort_keys=True), flush=True)
        time.sleep(min(30.0, max(5.0, remaining)))


def prepare_new_chat(browser, state):
    record = r.target_record()
    if not record:
        raise r.TargetDrift("dedicated Gemini CDP target missing")
    if record["path"] == "/app":
        q.save_state(state, status="NEW_CHAT_READY", prior_route=record["path"])
        return
    holder = "goru-review-base-11-new-chat"
    client = r.UDSClient(r.SOCK)
    lease = None
    try:
        lease = r.acquire_target(client, holder, "write", ttl=300)
        page = r.exact_page(browser, record["path"])
        if r.page_challenge(page):
            r.freeze_for_challenge(client, holder, "review_base_10", "pre-dispatch current-route classification")
        r.check_action(client, lease, "review_base_10 navigate to new chat", record["path"], page)
        page.goto("https://gemini.google.com/app", wait_until="domcontentloaded", timeout=30000)
        page.wait_for_timeout(1200)
        if r.page_challenge(page):
            r.freeze_for_challenge(client, holder, "review_base_10", "post-navigation new-chat classification")
        if not r.target_matches("/app", page):
            raise r.TargetDrift("Review Base item 11 new-chat route failed exact verification")
        q.save_state(state, prior_route=record["path"], status="NEW_CHAT_READY")
    finally:
        if lease:
            with suppress(Exception):
                r.release_lease(client, lease)
        client.close()


def classify_after_start_timeout(identity, prompt, browser):
    path = identity["conversation_path"]
    holder = "goru-review-base-03-start-settlement"
    client = r.UDSClient(r.SOCK)
    lease = None
    try:
        lease = r.acquire_target(client, holder, "read", ttl=300)
        page = r.exact_page(browser, path)
        if r.page_challenge(page):
            r.freeze_for_challenge(client, holder, "review_base_10", "post-Start timeout settlement")
        snapshot = r.page_snapshot(page)
        all_text = " ".join(item["text"] for item in snapshot.get("messages", []))
        active = snapshot["research"] or (snapshot["stop"] and any(token in all_text for token in ("While I'm researching", "Researching ", "Creating visuals for the report", "Writing your report")))
        if active:
            return "accepted_delayed"
        terminal = len(snapshot.get("messages", [])) >= 3 and len(snapshot["messages"][-1]["text"]) >= 4000 and not snapshot["stop"] and not snapshot["research"]
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
    counts = {prefix: len(set(re.findall(rf"\[REV10-{prefix}\d{{2}}\]", result))) for prefix in ("E", "D", "N", "U")}
    primary_count = len(set(re.findall(r"\[REV10-P\d{3}\]", result)))
    required = ["1. review identity and scope map", "2. established findings", "3. open debates and tensions", "4. key measurements and calibrations", "5. what remained unknown", "6. primary-citation harvest", "7. do_not_use_unverified", "8. review and source identity ledger"]
    checks = {
        "headings_present": all(value in lower for value in required),
        "established_count": counts["E"],
        "debate_count": counts["D"],
        "measurement_count": counts["N"],
        "unknown_count": counts["U"],
        "primary_harvest_count": primary_count,
        "review_doi_present": "10.1146/annurev-astro-082812-140951" in result,
        "review_arxiv_present": "1412.2712" in result,
        "review_ads_present": "2015ARA&A..53...51S" in result,
        "do_not_use_present": "uncited_not_usable" in lower,
        "terminal_marker_present": MARKER in result,
    }
    checks["pass"] = bool(checks["headings_present"] and counts["E"] >= 12 and counts["D"] >= 8 and counts["N"] >= 8 and counts["U"] >= 6 and 40 <= primary_count <= 80 and checks["review_doi_present"] and checks["review_arxiv_present"] and checks["review_ads_present"] and checks["do_not_use_present"] and checks["terminal_marker_present"])
    return checks


def save_packet(snapshot, result_sha, identity, current_spec, state):
    result = snapshot["messages"][-1]["text"]
    links, seen = [], set()
    for item in snapshot.get("links", []):
        if r.keep_source(item) and item["href"] not in seen:
            seen.add(item["href"])
            links.append(item)
    quality = output_quality(result)
    captured_utc = r.utcnow()
    lines = [
        "# Review Base 10 raw Deep Research packet — Conroy 2013",
        "",
        "advisory_only: true",
        "canonical_packet_released: false",
        "wiki_write_performed_by_tori: false",
        "identifier_verification_required_before_canonical_release: true",
        "",
        f"Queue: `{QUEUE_PATH}`",
        f"Queue SHA-256: `{r.sha_file(QUEUE_PATH)}`",
        f"Prompt: `{PROMPT_PATH}`",
        f"Prompt SHA-256: `{current_spec['prompt_sha256']}`",
        f"Conversation ID: `{identity['conversation_id']}`",
        f"Submit UTC: `{identity['submit_utc']}`",
        f"Research Start UTC: `{state['paper'].get('research_start_utc', '')}`",
        f"Result captured UTC: `{captured_utc}`",
        f"Raw result SHA-256: `{result_sha}`",
        "",
        "## Deep Research review-base result",
        "",
        result,
        "",
        "## Captured external source anchors",
        "",
    ]
    lines.extend([f"- {item['label'] or '(unlabeled)'} — {item['href']}" for item in links] or ["- No external anchors exposed."])
    lines.extend(["", "## Custody", "", "- Raw audit custody only; do not integrate. Canonical release requires composite identifier and claim-boundary verification.", "- No wiki, DB, trust, deploy, publish, git, credential, billing, account-setting, or conversation-deletion mutation was performed.", ""])
    r.atomic_write(RAW_PACKET_PATH, "\n".join(lines))
    metadata = {
        "run_id": RUN_ID,
        "queue_item": 11,
        "captured_utc": captured_utc,
        "identity": identity,
        "result_chars": len(result),
        "result_text_sha256": result_sha,
        # Compatibility alias expected by the inherited terminal receipt only.
        # This still names the raw-custody artifact, never the canonical packet.
        "packet_sha256": r.sha_file(RAW_PACKET_PATH),
        "raw_packet_sha256": r.sha_file(RAW_PACKET_PATH),
        "source_anchor_count": len(links),
        "source_anchors": links,
        "output_quality": quality,
        "canonical_packet_released": False,
        "independent_identifier_verification_status": "PENDING",
        "conversation_deleted": False,
    }
    r.atomic_json(RAW_METADATA_PATH, metadata)
    raw = RAW_PACKET_PATH.read_text().split("## Deep Research review-base result\n\n", 1)[1].split("\n\n## Captured external source anchors", 1)[0]
    if r.sha_bytes(raw.encode()) != result_sha:
        raise r.PaperFailure("Review Base item 11 raw-result custody mismatch")
    entry = r.journal_entry(
        "review_base_10_raw_packet_saved",
        f"Review Base 10 Conroy 2013 raw packet saved; conversation={identity['conversation_id']}; raw_sha={r.sha_file(RAW_PACKET_PATH)}; output_shape_pass={quality['pass']}; canonical_released=false; no wiki/DB write; no deletion.",
        [QUEUE_PATH, MANIFEST_PATH, PROMPT_PATH, RAW_PACKET_PATH, RAW_METADATA_PATH],
    )
    q.save_state(
        state,
        status="RAW_PACKET_LANDED_LOCAL_VERIFICATION_PENDING",
        paper={**state["paper"], "status": "raw_packet_saved", "raw_packet_sha256": r.sha_file(RAW_PACKET_PATH), "raw_metadata_sha256": r.sha_file(RAW_METADATA_PATH), "result_chars": len(result), "result_text_sha256": result_sha, "output_quality": quality, "save_ledger": entry},
        raw_packet_sha256=r.sha_file(RAW_PACKET_PATH),
        raw_metadata_sha256=r.sha_file(RAW_METADATA_PATH),
        canonical_packet_released=False,
        next_action="Local composite identifier and claim-boundary verification; no account retry; Hwao ping only after canonical release",
    )
    update_manifest("ITEM_11_RAW_LANDED_LOCAL_VERIFICATION_PENDING", conversation_id=identity["conversation_id"], submit_utc=identity["submit_utc"], research_start_utc=state["paper"].get("research_start_utc"), raw_packet_path=str(RAW_PACKET_PATH), raw_packet_sha256=r.sha_file(RAW_PACKET_PATH), output_shape_pass=quality["pass"])
    return metadata


def write_failure(state, exc, identity=None):
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
        "queue_stopped": True,
    }
    r.atomic_json(FAILURE_PATH, failure)
    q.save_state(state, status="HARD_CHALLENGE_STOP_FROZEN" if failure["global_challenge_stop"] else "FIRST_UNACCEPTED_QUEUE_HOLD" if failure["first_unaccepted_hold"] else "TECHNICAL_OR_CUSTODY_HOLD", failure_path=str(FAILURE_PATH), failure_sha256=r.sha_file(FAILURE_PATH), next_action="STOP queue; no retry; Duho/Hwao review")
    update_manifest("QUEUE_HOLD_ITEM_10", failure_path=str(FAILURE_PATH), error=f"{type(exc).__name__}: {exc}")
    with suppress(Exception):
        r.journal_entry("review_base_10_queue_hold", f"Review Base queue HOLD on item 10: {type(exc).__name__}: {exc}; retry=false; challenge={failure['global_challenge_stop']}", [QUEUE_PATH, MANIFEST_PATH, PROMPT_PATH, FAILURE_PATH])
    r.report_hwao(f"REVIEW-BASE HARD HOLD item 10: {type(exc).__name__}: {exc}; no retry; queue stopped; challenge={failure['global_challenge_stop']}.")


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


# Gemini may accept the prompt and create the exact conversation while the
# navigation never reaches Playwright's final "load" state. Classify that
# durable route in place and continue; never resend the prompt.
_original_stage_and_submit = r.stage_and_submit


def stage_and_submit_with_route_recovery(current_spec, state, browser):
    try:
        return _original_stage_and_submit(current_spec, state, browser)
    except Exception as exc:
        # The public sync API class and the implementation TimeoutError class
        # can differ across the mixed Python 3.9 Playwright installation.
        if type(exc).__name__ != "TimeoutError":
            raise
        record = r.target_record()
        if not record or record["path"] not in {"/app"} and not record["path"].startswith("/app/"):
            raise r.TargetDrift(f"Review Base 10 navigation timeout on unexpected route: {record}") from exc
        page = r.exact_page(browser, record["path"])
        if r.page_challenge(page):
            raise r.GlobalChallengeStop("Review Base 10 challenge after prompt submit")
        prompt = PROMPT_PATH.read_text().rstrip("\n")
        recovered_from_history = False
        if record["path"] == "/app":
            holder = "goru-dr-reresearch-r2-review_base_10-route-recovery"
            client = r.UDSClient(r.SOCK)
            lease = None
            try:
                lease = r.acquire_target(client, holder, "write", ttl=300)
                r.check_action(client, lease, "review_base_10 inspect exact accepted history route without resend", "/app", page)
                opener = page.get_by_role("button", name="Open sidebar", exact=True)
                if opener.count() == 1 and opener.is_visible():
                    opener.click()
                    page.wait_for_timeout(1200)
                links = page.locator('a[href*="/app/"]')
                matches = []
                needle = "Queue item 10 of 20 Core review: Conroy"
                for i in range(min(links.count(), 150)):
                    link = links.nth(i)
                    if link.is_visible() and needle in (link.inner_text() or ""):
                        matches.append(link)
                if len(matches) != 1:
                    raise r.TargetDrift(f"Review Base 10 accepted history route count {len(matches)} after submit timeout")
                href = matches[0].get_attribute("href")
                path = urlparse(href).path if href else ""
                if not path.startswith("/app/"):
                    raise r.TargetDrift(f"Review Base 10 invalid accepted history href: {href}")
                page.goto(f"https://gemini.google.com{path}", wait_until="domcontentloaded", timeout=30000)
                page.wait_for_timeout(1500)
                if not r.target_matches(path, page):
                    raise r.TargetDrift(f"Review Base 10 exact accepted history navigation failed: {page.url}")
                recovered_from_history = True
            finally:
                if lease:
                    r.release_lease(client, lease)
            record = r.target_record()
            if not record or not record["path"].startswith("/app/"):
                raise r.TargetDrift(f"Review Base 10 route absent after history recovery: {record}")
        evidence = r.current_prompt_identity(page, prompt)
        if not evidence:
            raise r.TargetDrift("Review Base 10 navigation timeout without exact visible prompt identity")
        message, count, latest = q.latest_account_grant()
        if message != f"OK ({count} entries)" or not latest or latest.get("holder") != "goru-dr-reresearch-r2-review_base_10-submit":
            raise r.TargetDrift(f"Review Base 10 submit custody mismatch after navigation timeout: {latest}")
        return {
            "conversation_id": record["path"].split("/app/", 1)[1],
            "conversation_path": record["path"],
            "target_id": record["id"],
            "captured_title": record["title"],
            "submit_utc": latest["utc"],
            "submit_account_lease_id": latest["lease_id"],
            "prompt_sha256": current_spec["prompt_sha256"],
            "prompt_file_sha256": current_spec["prompt_file_sha256"],
            "identity_evidence": evidence,
            "page_challenge_after_submit": False,
            "recovered_after_navigation_settlement_timeout": True,
            "recovered_from_exact_history_route": recovered_from_history,
            "prompt_resent": False,
        }


r.stage_and_submit = stage_and_submit_with_route_recovery

if __name__ == "__main__":
    raise SystemExit(q.main())
