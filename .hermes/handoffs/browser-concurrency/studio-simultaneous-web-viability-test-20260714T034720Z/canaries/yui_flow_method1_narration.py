#!/usr/bin/env python3
"""Generate exactly one METHOD-1 Veo native-narration beat per invocation.

This wrapper reuses the verified narration analysis/download machinery while
adding explicit active-tab/AX target alignment, a no-retry policy, and the
independent METHOD-1 Start-to-Start ramp. It never writes the shared ledger.
"""
from __future__ import annotations

import argparse
import hashlib
import importlib.util
import json
import os
import re
import shutil
import subprocess
import time
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

PACKET = Path(__file__).resolve().parents[1]
BASE = PACKET / "canaries" / "yui_flow_narration_batch_02_07.py"
_spec = importlib.util.spec_from_file_location("narration_base", BASE)
assert _spec and _spec.loader
M = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(M)

OUTPUT_DIR = Path("/Users/duhokim/HermesOps/scripts/clips/method1")
BRIEF = OUTPUT_DIR / "M1_NARRATION_BRIEF.md"
MANIFEST = OUTPUT_DIR / "M1_NARRATION_MANIFEST.json"
LANE_STATE = OUTPUT_DIR / "M1_FLOW_LANE_STATE.json"
AXSET_SOURCE = PACKET / "canaries" / "axset_textarea.swift"
AXSET_BINARY = Path("/tmp/yui_axset_textarea")
NARRATOR = "a warm, calm, professional female documentary narrator delivers a clean studio voiceover with no on-screen speaker"
RAMP_MINUTES = [30, 20, 15, 10, 8]

VISUALS = {
    1: "Slow cinematic drift past a dark black hole and a quiet galaxy with restrained cyan-and-gold data traces",
    2: "Two matched galaxies align side by side against a clean deep-space background, one with a subtly active core",
    3: "A field of survey galaxies resolves into a clean B-P-T diagram and matched pairs, with no readable labels",
    4: "Thousands of paired galaxies form two restrained distributions, one visibly lower in star formation",
    5: "A cautious scientific balance and branching uncertainty paths appear over a subtle galaxy survey field",
    6: "A galaxy environment map and repeating black-hole activity cycles resolve into a calm final cosmic vista",
}


def utc_now() -> str:
    return time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime())


def sha256_file(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()


def parse_brief() -> dict[int, str]:
    text = BRIEF.read_text()
    rows: dict[int, str] = {}
    for match in re.finditer(r'^- b([1-6]): "(.+)"$', text, re.MULTILINE):
        rows[int(match.group(1))] = match.group(2)
    if set(rows) != set(range(1, 7)):
        raise RuntimeError(f"brief beat set drift: {sorted(rows)}")
    return rows


def prompt_for(beat: int, line: str) -> str:
    return (
        f"{VISUALS[beat]}; {NARRATOR}: \"{line}\" "
        "Subtle cosmic ambience kept low under the voice. No on-screen speaker, captions, subtitles, logos, or added text."
    )


def chrome_tab_state() -> dict[str, Any]:
    script = '''tell application "Google Chrome"
set w to window 1
set i to active tab index of w
return ((i as text) & "\n" & (URL of tab i of w) & "\n" & (count of tabs of w as text))
end tell'''
    lines = subprocess.run(["osascript", "-e", script], text=True, capture_output=True, check=True).stdout.splitlines()
    return {"index": int(lines[0]), "url": lines[1], "count": int(lines[2])}


def activate_flow(target: dict[str, Any], desktop: dict[str, Any], focus: dict[str, Any]) -> dict[str, Any]:
    prior = chrome_tab_state()
    M.H.probe_exact(target_lease=target)
    M.H.check(target, "activate exact Flow tab 1 for METHOD-1 trusted AX work")
    M.H.check(focus, "focus exact Flow tab 1 for METHOD-1 narration")
    M.H.check(desktop, "activate exact Flow tab 1 before AX writes", uses_desktop=True)
    subprocess.run(["osascript", "-e", 'tell application "Google Chrome" to set active tab index of window 1 to 1'], check=True)
    time.sleep(0.5)
    active = chrome_tab_state()
    if active["index"] != 1 or active["url"] != M.H.PROJECT_ROOT:
        raise RuntimeError(f"active Flow target verification failed: {active}")
    return prior


def restore_prior_tab(prior: dict[str, Any] | None, target: dict[str, Any], desktop: dict[str, Any], focus: dict[str, Any]) -> None:
    if not prior or prior["index"] == 1:
        return
    current = chrome_tab_state()
    if prior["index"] > current["count"]:
        print("TAB_RESTORE_SKIPPED", json.dumps({"reason": "prior index no longer exists", "prior": prior, "current": current}, sort_keys=True), flush=True)
        return
    script = f'''tell application "Google Chrome"
set w to window 1
if URL of tab {prior["index"]} of w is {json.dumps(prior["url"])} then
set active tab index of w to {prior["index"]}
return "RESTORED"
end if
return "SKIPPED_URL_DRIFT"
end tell'''
    M.H.check(target, "restore prior user tab after METHOD-1 AX work")
    M.H.check(focus, "restore prior user tab after METHOD-1 AX work")
    M.H.check(desktop, "restore prior user tab after METHOD-1 AX work", uses_desktop=True)
    result = subprocess.run(["osascript", "-e", script], text=True, capture_output=True, check=True).stdout.strip()
    print("TAB_RESTORE", result, flush=True)


def ensure_axset_helper() -> None:
    if not AXSET_SOURCE.exists():
        raise RuntimeError(f"missing semantic AX text helper source: {AXSET_SOURCE}")
    if AXSET_BINARY.exists() and AXSET_BINARY.stat().st_mtime_ns >= AXSET_SOURCE.stat().st_mtime_ns:
        return
    subprocess.run(["swiftc", str(AXSET_SOURCE), "-o", str(AXSET_BINARY)], check=True)


def paste_prompt_background(
    clip_num: int,
    prompt: str,
    target: dict[str, Any],
    desktop: dict[str, Any],
    focus: dict[str, Any],
) -> None:
    """Set the exact active Flow AXTextArea without clipboard/global keys."""
    ensure_axset_helper()
    last: dict[str, Any] | None = None
    for attempt in range(1, 13):
        M.H.probe_exact(target_lease=target)
        M.H.check(target, f"set METHOD-1 vo_b{clip_num - 100} exact prompt through active Flow AXTextArea")
        M.H.check(focus, f"focus exact METHOD-1 vo_b{clip_num - 100} Flow composer")
        M.H.check(desktop, f"background AXValue METHOD-1 vo_b{clip_num - 100} prompt", uses_desktop=True)
        result = subprocess.run([str(AXSET_BINARY), "68262", prompt], text=True, capture_output=True)
        time.sleep(0.5)
        state_now = M.H.run_js(
            r'''(() => {const vis=e=>{const s=getComputedStyle(e),r=e.getBoundingClientRect();return s.display!='none'&&s.visibility!='hidden'&&r.width>0&&r.height>0};const input=[...document.querySelectorAll('[contenteditable=true]')].find(vis);const buttons=[...document.querySelectorAll('button,[role=button]')].filter(vis);const create=buttons.find(e=>(e.innerText||e.textContent||'').includes('arrow_forward')&&(e.innerText||e.textContent||'').includes('Create'));return JSON.stringify({prompt:(input?(input.innerText||input.textContent||'').trim():null),active:document.activeElement===input,config:buttons.map(e=>(e.innerText||e.textContent||'').trim().replace(/\s+/g,' ')).find(x=>x.includes('Video ·'))||'',videos:document.querySelectorAll('video').length,create_disabled:create?create.disabled:null});})()'''
        )
        last = state_now
        ready = result.returncode == 0 and state_now["prompt"] == prompt and state_now["active"] and state_now["config"] == "Video · 8s crop_16_9 1x" and state_now["create_disabled"] is False
        if ready:
            print(f"vo_b{clip_num - 100} prompt ready", json.dumps(last, sort_keys=True), flush=True)
            return
        print("AXSET_RETRY", json.dumps({"attempt": attempt, "returncode": result.returncode, "stdout": result.stdout.strip(), "state": last}, sort_keys=True), flush=True)
        time.sleep(0.5)
    raise RuntimeError(f"background AX prompt input failed after bounded readiness retries: {last}")


def submit_once_background(
    clip_num: int,
    prompt: str,
    target: dict[str, Any],
    desktop: dict[str, Any],
    focus: dict[str, Any],
) -> tuple[str, int, str]:
    """Dispatch one trusted exact Create AXPress under one account lease."""
    M.H.probe_exact(target_lease=target)
    state = M.H.run_js(
        r'''(() => {const vis=e=>{const s=getComputedStyle(e),r=e.getBoundingClientRect();return s.display!='none'&&s.visibility!='hidden'&&r.width>0&&r.height>0};const input=[...document.querySelectorAll('[contenteditable=true]')].find(vis);const buttons=[...document.querySelectorAll('button,[role=button]')].filter(vis);return JSON.stringify({url:location.href,prompt:(input?(input.innerText||input.textContent||'').trim():null),active:document.activeElement===input,config:buttons.map(e=>(e.innerText||e.textContent||'').trim().replace(/\s+/g,' ')).find(x=>x.includes('Video ·'))||'',videos:document.querySelectorAll('video').length});})()'''
    )
    valid = state["url"] == M.H.PROJECT_ROOT and state["prompt"] == prompt and state["active"] and state["config"] == "Video · 8s crop_16_9 1x"
    if not valid:
        raise RuntimeError(f"METHOD-1 final pre-submit verification failed: {state}")
    baseline_cards = int(state["videos"])
    for lease in (target, desktop, focus):
        M.H.heartbeat(lease)
    account = M.wait_acquire(
        f"yui-flow-method1-vo-b{clip_num - 100}",
        "account-submission",
        "write",
        {"account": "google-ultra-shared"},
        120,
        60,
        keepalive=(target, desktop, focus),
    )
    submit_utc = utc_now()
    try:
        M.H.probe_exact(target_lease=target)
        M.H.check(target, f"submit exactly one METHOD-1 vo_b{clip_num - 100} on exact Flow project")
        M.H.check(focus, f"exact Flow Create AXPress for METHOD-1 vo_b{clip_num - 100}")
        M.H.check(desktop, f"background AXPress METHOD-1 vo_b{clip_num - 100} Veo Quality x1", uses_desktop=True)
        M.H.check(account, f"serialized shared-account submit METHOD-1 vo_b{clip_num - 100} Veo Quality x1")
        M.H.ax_press("AXButton", 'n==="arrow_forward Create"', before_attempt=lambda: M.H.probe_exact(target_lease=target))
        time.sleep(5)
    finally:
        M.safe_release(account)
    M.H.probe_exact(target_lease=target)
    accepted = M.H.run_js(
        r'''(() => {const vis=e=>{const s=getComputedStyle(e),r=e.getBoundingClientRect();return s.display!='none'&&s.visibility!='hidden'&&r.width>0&&r.height>0};const input=[...document.querySelectorAll('[contenteditable=true]')].find(vis);const lines=(document.body.innerText||'').split('\n').map(x=>x.trim()).filter(Boolean);return JSON.stringify({input:(input?(input.innerText||input.textContent||'').trim():null),videos:document.querySelectorAll('video').length,failed:[...document.querySelectorAll('*')].filter(e=>vis(e)&&e.children.length===0&&(e.innerText||e.textContent||'').trim()==='Failed').length,prompt_visible:lines.includes(''' + json.dumps(prompt) + r''')});})()'''
    )
    print(f"vo_b{clip_num - 100} accepted", json.dumps(accepted, sort_keys=True), flush=True)
    if accepted["input"] != "What do you want to create?" or not accepted["prompt_visible"]:
        raise RuntimeError(f"METHOD-1 vo_b{clip_num - 100} first submit unaccepted: {accepted}")
    return submit_utc, baseline_cards, account["lease_id"]


def read_lane_state() -> dict[str, Any]:
    if not LANE_STATE.exists():
        return {"submit_count": 0, "next_gap_minutes": None, "last_start_utc": None, "hold": False}
    return json.loads(LANE_STATE.read_text())


def enforce_lane_gap(state: dict[str, Any]) -> None:
    if state.get("hold"):
        raise RuntimeError(f"METHOD-1 Flow lane is held: {state.get('hold_reason')}")
    last = state.get("last_start_utc")
    gap = state.get("next_gap_minutes")
    if not last or gap is None:
        return
    then = datetime.strptime(last, "%Y-%m-%dT%H:%M:%SZ").replace(tzinfo=timezone.utc)
    elapsed = (datetime.now(timezone.utc) - then).total_seconds()
    required = float(gap) * 60
    if elapsed < required:
        raise RuntimeError(f"METHOD-1 Start-to-Start gap not open: wait {required - elapsed:.1f}s more")


def write_json_atomic(path: Path, data: dict[str, Any]) -> None:
    tmp = path.with_suffix(path.suffix + ".tmp")
    tmp.write_text(json.dumps(data, indent=2, sort_keys=True) + "\n")
    os.replace(tmp, path)


def load_manifest(reference: dict[str, Any]) -> dict[str, Any]:
    if MANIFEST.exists():
        data = json.loads(MANIFEST.read_text())
        if data.get("brief_sha256") != sha256_file(BRIEF):
            raise RuntimeError("METHOD-1 brief hash drift against existing manifest")
        return data
    return {
        "status": "in_progress",
        "started_utc": utc_now(),
        "updated_utc": utc_now(),
        "brief": str(BRIEF),
        "brief_sha256": sha256_file(BRIEF),
        "project_id": M.H.PROJECT_ID,
        "model": "Veo 3.1 - Quality",
        "duration": "8s",
        "aspect_ratio": "16:9",
        "output_count": "1x",
        "displayed_cost_per_submit": 100,
        "narrator_descriptor": NARRATOR,
        "reference": reference["public"],
        "start_to_start_ramp_minutes": RAMP_MINUTES,
        "no_direct_run_ledger_appends": True,
        "clips": [],
    }


def generate_one(beat: int, prompt: str, spoken_line: str, reference: dict[str, Any], work_dir: Path) -> dict[str, Any]:
    clip_num = 100 + beat
    target = desktop = focus = None
    prior: dict[str, Any] | None = None
    submit_utc = ""
    baseline_cards = 0
    account_lease_id = ""
    try:
        target, desktop, focus = M.acquire_write_set(clip_num, 1)
        prior = activate_flow(target, desktop, focus)
        M.H.ensure_root(target)
        M.verify_full_config(clip_num, 1, target, desktop, focus)
        paste_prompt_background(clip_num, prompt, target, desktop, focus)
        M.verify_full_config(clip_num, 1, target, desktop, focus)
        M.refocus_composer(prompt, target)
        submit_utc, baseline_cards, account_lease_id = submit_once_background(clip_num, prompt, target, desktop, focus)
    finally:
        if target and desktop and focus:
            try:
                restore_prior_tab(prior, target, desktop, focus)
            except Exception as exc:
                print("TAB_RESTORE_WARNING", repr(exc), flush=True)
        M.safe_release(focus)
        M.safe_release(desktop)
        M.safe_release(target)
    detail = M.poll_to_playable(clip_num, 1, prompt)
    temporary = work_dir / f"vo_b{beat}_attempt1.mp4"
    M.download_current_detail(clip_num, 1, detail["media_id"], temporary)
    analysis = M.audio_analysis(temporary, spoken_line, reference["features"], work_dir)
    return {
        "attempt": 1,
        "artifact_temp": str(temporary),
        "artifact_sha256": sha256_file(temporary),
        "media_id": detail["media_id"],
        "submit_utc": submit_utc,
        "settled_utc": utc_now(),
        "settlement_elapsed_s": detail["settlement_elapsed_s"],
        "baseline_cards": baseline_cards,
        "account_submission_lease_id": account_lease_id,
        "prompt_match": True,
        "detail_video": detail["video"],
        "analysis": analysis,
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--beat", type=int, required=True, choices=range(1, 7))
    parser.add_argument("--dry-run", action="store_true")
    args = parser.parse_args()
    beat = args.beat
    rows = parse_brief()
    output = OUTPUT_DIR / f"vo_b{beat}.mp4"
    if output.exists():
        raise RuntimeError(f"refusing to overwrite {output}")
    state = read_lane_state()
    enforce_lane_gap(state)
    broker_state = json.loads((PACKET / "broker" / "live_state.json").read_text())
    if broker_state["frozen"]:
        raise RuntimeError("broker is frozen")
    prompt = prompt_for(beat, rows[beat])
    if prompt.count(NARRATOR) != 1 or rows[beat] not in prompt:
        raise RuntimeError("METHOD-1 prompt fidelity failure")
    if args.dry_run:
        print(json.dumps({"beat": beat, "brief_sha256": sha256_file(BRIEF), "output_absent": True, "prompt": prompt, "spoken_line": rows[beat], "lane_state": state, "no_retry": True, "no_direct_ledger_append": True}, sort_keys=True))
        return 0

    run_id = time.strftime("%Y%m%dT%H%M%SZ", time.gmtime())
    work_dir = Path("/tmp") / f"yui-flow-method1-b{beat}-{run_id}-{os.getpid()}"
    work_dir.mkdir(parents=True, exist_ok=False)
    reference = M.analyze_reference(work_dir)
    manifest = load_manifest(reference)
    expected_prior = list(range(1, beat))
    present_prior = [row["beat"] for row in manifest["clips"]]
    if present_prior != expected_prior:
        raise RuntimeError(f"METHOD-1 sequence drift: expected completed {expected_prior}, found {present_prior}")

    try:
        attempt = generate_one(beat, prompt, rows[beat], reference, work_dir)
    except Exception as exc:
        # No automatic retry. Unknown/unaccepted attempts hold at the current
        # maximum sustainable gap until Hwao reviews the preserved evidence.
        state["hold"] = True
        state["hold_reason"] = f"vo_b{beat} first attempt stopped: {exc}"
        state["updated_utc"] = utc_now()
        write_json_atomic(LANE_STATE, state)
        raise

    source = Path(attempt.pop("artifact_temp"))
    shutil.move(str(source), str(output))
    attempt["artifact_sha256"] = sha256_file(output)
    entry = {
        "beat": beat,
        "prompt": prompt,
        "prompt_sha256": hashlib.sha256(prompt.encode()).hexdigest(),
        "spoken_line": rows[beat],
        "spoken_line_sha256": hashlib.sha256(rows[beat].encode()).hexdigest(),
        "attempt_count": 1,
        "retry_used": False,
        "selected_attempt": 1,
        "quality_gate_pass": bool(attempt["analysis"]["quality_pass"]),
        "path": str(output),
        "sha256": sha256_file(output),
        "attempts": [attempt],
    }
    manifest["clips"].append(entry)
    manifest["updated_utc"] = utc_now()
    manifest["submit_count"] = len(manifest["clips"])
    manifest["expected_credit_cost"] = len(manifest["clips"]) * 100
    manifest["quality_failure_beats"] = [row["beat"] for row in manifest["clips"] if not row["quality_gate_pass"]]
    manifest["status"] = "awaiting_hwao_review" if beat < 6 else ("completed" if not manifest["quality_failure_beats"] else "completed_with_quality_failures")
    write_json_atomic(MANIFEST, manifest)

    submit_count = int(state.get("submit_count", 0)) + 1
    state.update({
        "submit_count": submit_count,
        "last_start_utc": attempt["submit_utc"],
        "next_gap_minutes": RAMP_MINUTES[min(submit_count - 1, len(RAMP_MINUTES) - 1)],
        "last_completed_beat": beat,
        "awaiting_hwao_review": True,
        "hold": False,
        "hold_reason": None,
        "updated_utc": utc_now(),
    })
    write_json_atomic(LANE_STATE, state)
    print("METHOD1_CLIP_COMPLETE", json.dumps({
        "beat": beat,
        "path": str(output),
        "sha256": entry["sha256"],
        "media_id": attempt["media_id"],
        "submit_utc": attempt["submit_utc"],
        "quality_gate_pass": entry["quality_gate_pass"],
        "transcript": attempt["analysis"]["best_transcript"],
        "voice_consistency": attempt["analysis"]["reference_comparison"],
        "next_gap_minutes": state["next_gap_minutes"],
        "retry_used": False,
    }, sort_keys=True), flush=True)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
