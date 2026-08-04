#!/usr/bin/env python3
"""Generate one PGR pilot native-voice clip per invocation, with no retries."""
from __future__ import annotations

import argparse
import hashlib
import importlib.util
import json
import os
import re
import shutil
import time
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

PACKET = Path(__file__).resolve().parents[1]
BASE = PACKET / "canaries" / "yui_flow_method1_narration.py"
_spec = importlib.util.spec_from_file_location("method1_base", BASE)
assert _spec and _spec.loader
B = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(B)
M = B.M

OUTPUT_DIR = Path("/Users/duhokim/HermesOps/scripts/clips/method1_pgr")
BRIEF = OUTPUT_DIR / "PGR_PILOT_BRIEF.md"
MANIFEST = OUTPUT_DIR / "PGR_PILOT_MANIFEST.json"
LANE_STATE = OUTPUT_DIR / "PGR_FLOW_LANE_STATE.json"
NARRATOR = "a warm, calm, professional female documentary narrator delivers a clean studio voiceover with no on-screen speaker"
MIN_GENTLE_GAP_SECONDS = 60

VISUALS = {
    1: "A restrained cinematic view of a luminous knowledge network forming from evidence packets over a deep-space background",
    2: "A clean visual metaphor of one glowing evidence packet securely bundling a paper, evidence, and a trust gauge",
    3: "A calm visual pipeline in which evidence packets pass through a rigorous checkpoint before joining a knowledge network",
    4: "A measured visual distinction between verified paths and clearly cautioned unresolved paths in a scientific knowledge map",
    5: "A balanced scientific knowledge scene with evidence links, a trust gauge, and two carefully balanced interpretations",
    6: "A calm final cosmic knowledge network built from connected papers, evidence packets, and visible trust signals",
}


def utc_now() -> str:
    return time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime())


def sha256_file(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()


def atomic_json(path: Path, data: dict[str, Any]) -> None:
    tmp = path.with_suffix(path.suffix + ".tmp")
    tmp.write_text(json.dumps(data, indent=2, sort_keys=True) + "\n")
    os.replace(tmp, path)


def parse_lines() -> dict[int, str]:
    text = BRIEF.read_text()
    rows: dict[int, str] = {}
    for match in re.finditer(r'^- \*\*vo_b([1-6]):\*\* "(.+)"$', text, re.MULTILINE):
        rows[int(match.group(1))] = match.group(2)
    if set(rows) != set(range(1, 7)):
        raise RuntimeError(f"PGR narration beat set drift: {sorted(rows)}")
    return rows


def prompt_for(beat: int, line: str) -> str:
    return (
        f"{VISUALS[beat]}; {NARRATOR}: \"{line}\" "
        "Subtle cosmic ambience kept low under the voice. No on-screen speaker, captions, subtitles, logos, or added text."
    )


def lane_state() -> dict[str, Any]:
    if not LANE_STATE.exists():
        return {
            "task": "PGR_PILOT",
            "status": "active",
            "hold": False,
            "accepted_submits": 0,
            "submit_attempts": 0,
            "last_accepted_submit_utc": None,
            "minimum_gentle_gap_seconds": MIN_GENTLE_GAP_SECONDS,
        }
    return json.loads(LANE_STATE.read_text())


def enforce_gap(state: dict[str, Any]) -> None:
    if state.get("hold"):
        raise RuntimeError(f"PGR Flow lane held: {state.get('hold_reason')}")
    last = state.get("last_accepted_submit_utc")
    if not last:
        return
    then = datetime.strptime(last, "%Y-%m-%dT%H:%M:%SZ").replace(tzinfo=timezone.utc)
    elapsed = (datetime.now(timezone.utc) - then).total_seconds()
    if elapsed < MIN_GENTLE_GAP_SECONDS:
        raise RuntimeError(f"PGR gentle submit gap not open: wait {MIN_GENTLE_GAP_SECONDS - elapsed:.1f}s")


def load_manifest(reference: dict[str, Any]) -> dict[str, Any]:
    if MANIFEST.exists():
        data = json.loads(MANIFEST.read_text())
        if data.get("brief_sha256") != sha256_file(BRIEF):
            raise RuntimeError("PGR brief hash drift against manifest")
        return data
    return {
        "task": "PGR_PILOT",
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
        "displayed_cost_per_voice_submit": 100,
        "narrator_descriptor": NARRATOR,
        "reference": reference["public"],
        "no_direct_run_ledger_appends": True,
        "voice_clips": [],
        "slides": [],
    }


def submit_once_return(
    beat: int,
    prompt: str,
    target: dict[str, Any],
    desktop: dict[str, Any],
    focus: dict[str, Any],
) -> tuple[str, int, str]:
    M.H.probe_exact(target_lease=target)
    state = M.H.run_js(
        r'''(() => {const vis=e=>{const s=getComputedStyle(e),r=e.getBoundingClientRect();return s.display!='none'&&s.visibility!='hidden'&&r.width>0&&r.height>0};const clean=s=>(s||'').trim().replace(/\s+/g,' ');const input=[...document.querySelectorAll('[contenteditable=true]')].find(vis);const buttons=[...document.querySelectorAll('button,[role=button]')].filter(vis);const create=buttons.find(e=>clean(e.innerText||e.textContent).includes('arrow_forward')&&clean(e.innerText||e.textContent).includes('Create'));const visibleLayers=[...document.querySelectorAll('[role=dialog],[aria-modal=true],[role=alertdialog]')].filter(vis);return JSON.stringify({url:location.href,prompt:(input?(input.innerText||input.textContent||'').trim():null),active:document.activeElement===input,config:buttons.map(e=>clean(e.innerText||e.textContent)).find(x=>x.includes('Video ·'))||'',videos:document.querySelectorAll('video').length,create_disabled:create?create.disabled:null,create_aria_disabled:create?create.getAttribute('aria-disabled'):null,layers:visibleLayers.map(e=>clean(e.innerText||e.textContent).slice(0,500)),sorry:location.href.includes('google.com/sorry'),challenge:/verify you are human|unusual traffic|captcha/i.test(document.body.innerText||'')});})()'''
    )
    valid = (
        state["url"] == M.H.PROJECT_ROOT
        and state["prompt"] == prompt
        and state["active"]
        and state["config"] == "Video · 8s crop_16_9 1x"
        and state["create_disabled"] is not True
        and state["create_aria_disabled"] != "true"
        and not state["layers"]
        and not state["sorry"]
        and not state["challenge"]
    )
    if not valid:
        raise RuntimeError(f"PGR vo_b{beat} final pre-submit verification failed: {state}")
    baseline_cards = int(state["videos"])
    for lease in (target, desktop, focus):
        M.H.heartbeat(lease)
    account = M.wait_acquire(
        f"yui-flow-pgr-vo-b{beat}",
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
        M.H.check(target, f"submit exactly one PGR vo_b{beat} on exact Flow project")
        M.H.check(focus, f"trusted Return submit PGR vo_b{beat}")
        M.H.check(desktop, f"trusted Return submit PGR vo_b{beat} Veo Quality x1", uses_desktop=True)
        M.H.check(account, f"serialized shared-account submit PGR vo_b{beat} Veo Quality x1")
        M.H.key_code(36)
        time.sleep(5)
    finally:
        M.safe_release(account)
    M.H.probe_exact(target_lease=target)
    accepted = M.H.run_js(
        r'''(() => {const vis=e=>{const s=getComputedStyle(e),r=e.getBoundingClientRect();return s.display!='none'&&s.visibility!='hidden'&&r.width>0&&r.height>0};const input=[...document.querySelectorAll('[contenteditable=true]')].find(vis);const lines=(document.body.innerText||'').split('\n').map(x=>x.trim()).filter(Boolean);return JSON.stringify({input:(input?(input.innerText||input.textContent||'').trim():null),videos:document.querySelectorAll('video').length,failed:[...document.querySelectorAll('*')].filter(e=>vis(e)&&e.children.length===0&&(e.innerText||e.textContent||'').trim()==='Failed').length,prompt_visible:lines.includes(''' + json.dumps(prompt) + r'''),sorry:location.href.includes('google.com/sorry'),challenge:/verify you are human|unusual traffic|captcha/i.test(document.body.innerText||'')});})()'''
    )
    print(f"PGR vo_b{beat} acceptance", json.dumps(accepted, sort_keys=True), flush=True)
    if accepted["sorry"] or accepted["challenge"]:
        raise RuntimeError(f"PGR vo_b{beat} hard challenge STOP: {accepted}")
    if accepted["input"] != "What do you want to create?" or not accepted["prompt_visible"]:
        raise RuntimeError(f"PGR vo_b{beat} first submit unaccepted: {accepted}")
    return submit_utc, baseline_cards, account["lease_id"]


def verify_full_config_with_dom_fallback(
    clip_num: int,
    attempt: int,
    target: dict[str, Any],
    desktop: dict[str, Any],
    focus: dict[str, Any],
) -> dict[str, Any]:
    """Verify the non-account Video settings popup with one DOM fallback."""
    try:
        return M.verify_full_config(clip_num, attempt, target, desktop, focus)
    except RuntimeError as exc:
        if "AXPress failed for role=AXPopUpButton" not in str(exc):
            raise
        M.H.probe_exact(target_lease=target)
        M.H.check(
            target,
            f"exact-tab DOM fallback for PGR vo_b{clip_num - 200} Video settings popup after bounded AX readiness failure",
        )
        opened = M.H.run_js(
            r'''(() => {const vis=e=>{const s=getComputedStyle(e),r=e.getBoundingClientRect();return s.display!='none'&&s.visibility!='hidden'&&r.width>0&&r.height>0};const clean=s=>(s||'').trim().replace(/\s+/g,' ');const b=[...document.querySelectorAll('button,[role=button]')].filter(vis).find(e=>clean(e.innerText||e.textContent).startsWith('Video ·'));if(!b)return JSON.stringify({clicked:false,label:null});const label=clean(b.innerText||b.textContent);b.click();return JSON.stringify({clicked:true,label});})()'''
        )
        if not opened.get("clicked"):
            raise RuntimeError(
                "DOM fallback could not find the Video settings popup (model tier, duration, aspect ratio, output count, credits)"
            ) from exc
        time.sleep(0.8)
        state = M.H.run_js(
            r'''(() => {const vis=e=>{const s=getComputedStyle(e),r=e.getBoundingClientRect();return s.display!='none'&&s.visibility!='hidden'&&r.width>0&&r.height>0};const clean=s=>(s||'').trim().replace(/\s+/g,' ');const controls=[...document.querySelectorAll('button,[role=button],[role=tab]')].filter(vis).map(e=>({label:clean(e.innerText||e.textContent),selected:e.getAttribute('aria-selected')}));const lines=(document.body.innerText||'').split('\n').map(clean).filter(Boolean);return JSON.stringify({model:controls.find(x=>x.label.includes('Veo 3.1 - Quality'))?.label||'',duration:controls.filter(x=>['4s','6s','8s','10s'].includes(x.label)),outputs:controls.filter(x=>['1x','x2','x3','x4'].includes(x.label)),aspects:controls.filter(x=>['16:9','9:16'].includes(x.label)),credit:lines.find(x=>/^100 credits$/.test(x))||'',audio_controls:controls.filter(x=>/audio|sound|voice/i.test(x.label)),fallback:'exact-tab-dom',popup_label:''' + json.dumps(opened.get("label")) + r'''});})()'''
        )
        ok = (
            "Veo 3.1 - Quality" in state["model"]
            and any(x["label"] == "8s" and x["selected"] == "true" for x in state["duration"])
            and any(x["label"] == "1x" and x["selected"] == "true" for x in state["outputs"])
            and any(x["label"] == "16:9" and x["selected"] == "true" for x in state["aspects"])
            and state["credit"] == "100 credits"
        )
        if not ok:
            raise RuntimeError(f"DOM fallback found the Video settings popup but config drifted: {state}") from exc
        closed = M.H.run_js(
            r'''(() => {const vis=e=>{const s=getComputedStyle(e),r=e.getBoundingClientRect();return s.display!='none'&&s.visibility!='hidden'&&r.width>0&&r.height>0};const clean=s=>(s||'').trim().replace(/\s+/g,' ');const b=[...document.querySelectorAll('button,[role=button]')].filter(vis).find(e=>clean(e.innerText||e.textContent).startsWith('Video ·'));if(!b)return JSON.stringify({clicked:false});b.click();return JSON.stringify({clicked:true});})()'''
        )
        if not closed.get("clicked"):
            raise RuntimeError("DOM fallback verified but could not close the Video settings popup") from exc
        time.sleep(0.5)
        print("PGR_CONFIG_DOM_FALLBACK", json.dumps(state, sort_keys=True), flush=True)
        return state


def generate_one(beat: int, prompt: str, line: str, reference: dict[str, Any], work_dir: Path) -> dict[str, Any]:
    clip_num = 200 + beat
    target = desktop = focus = None
    prior: dict[str, Any] | None = None
    submit_utc = ""
    baseline_cards = 0
    account_lease_id = ""
    try:
        target, desktop, focus = M.acquire_write_set(clip_num, 1)
        prior = B.activate_flow(target, desktop, focus)
        M.H.ensure_root(target)
        verify_full_config_with_dom_fallback(clip_num, 1, target, desktop, focus)
        M.paste_prompt(clip_num, 1, prompt, target, desktop, focus)
        verify_full_config_with_dom_fallback(clip_num, 1, target, desktop, focus)
        M.refocus_composer(prompt, target)
        submit_utc, baseline_cards, account_lease_id = submit_once_return(beat, prompt, target, desktop, focus)
    finally:
        if target and desktop and focus:
            try:
                B.restore_prior_tab(prior, target, desktop, focus)
            except Exception as exc:
                print("TAB_RESTORE_WARNING", repr(exc), flush=True)
        M.safe_release(focus)
        M.safe_release(desktop)
        M.safe_release(target)
    detail = M.poll_to_playable(clip_num, 1, prompt)
    temporary = work_dir / f"vo_b{beat}_attempt1.mp4"
    M.download_current_detail(clip_num, 1, detail["media_id"], temporary)
    analysis = M.audio_analysis(temporary, line, reference["features"], work_dir)
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
    lines = parse_lines()
    output = OUTPUT_DIR / f"vo_b{beat}.mp4"
    if output.exists():
        raise RuntimeError(f"refusing to overwrite {output}")
    state = lane_state()
    enforce_gap(state)
    broker = json.loads((PACKET / "broker" / "live_state.json").read_text())
    if broker["frozen"]:
        raise RuntimeError("broker frozen before PGR narration")
    prompt = prompt_for(beat, lines[beat])
    if prompt.count(NARRATOR) != 1 or lines[beat] not in prompt:
        raise RuntimeError("PGR prompt fidelity failure")
    if args.dry_run:
        print(json.dumps({"beat": beat, "brief_sha256": sha256_file(BRIEF), "line": lines[beat], "prompt": prompt, "output_absent": True, "lane": state, "no_retry": True, "no_direct_ledger_append": True}, sort_keys=True))
        return 0

    run_id = time.strftime("%Y%m%dT%H%M%SZ", time.gmtime())
    work_dir = Path("/tmp") / f"yui-flow-pgr-vo-b{beat}-{run_id}-{os.getpid()}"
    work_dir.mkdir(parents=True, exist_ok=False)
    reference = M.analyze_reference(work_dir)
    manifest = load_manifest(reference)
    completed = [row["beat"] for row in manifest["voice_clips"]]
    if completed != list(range(1, beat)):
        raise RuntimeError(f"PGR voice sequence drift: completed={completed}, requested={beat}")

    state["submit_attempts"] = int(state.get("submit_attempts", 0)) + 1
    state["updated_utc"] = utc_now()
    atomic_json(LANE_STATE, state)
    try:
        attempt = generate_one(beat, prompt, lines[beat], reference, work_dir)
    except Exception as exc:
        state["hold"] = True
        state["status"] = "HOLD_FIRST_UNACCEPTED_OR_TECHNICAL_STOP"
        state["hold_reason"] = f"vo_b{beat}: {type(exc).__name__}: {exc}"
        state["no_retry"] = True
        state["updated_utc"] = utc_now()
        atomic_json(LANE_STATE, state)
        raise

    temp = Path(attempt.pop("artifact_temp"))
    shutil.move(str(temp), str(output))
    attempt["artifact_sha256"] = sha256_file(output)
    entry = {
        "beat": beat,
        "prompt": prompt,
        "prompt_sha256": hashlib.sha256(prompt.encode()).hexdigest(),
        "spoken_line": lines[beat],
        "spoken_line_sha256": hashlib.sha256(lines[beat].encode()).hexdigest(),
        "attempt_count": 1,
        "retry_used": False,
        "quality_gate_pass": bool(attempt["analysis"]["quality_pass"]),
        "path": str(output),
        "sha256": sha256_file(output),
        "attempts": [attempt],
    }
    manifest["voice_clips"].append(entry)
    manifest["updated_utc"] = utc_now()
    manifest["expected_voice_credit_cost"] = len(manifest["voice_clips"]) * 100
    manifest["quality_failure_voice_beats"] = [row["beat"] for row in manifest["voice_clips"] if not row["quality_gate_pass"]]
    manifest["status"] = "voice_in_progress" if beat < 6 else "voice_complete"
    atomic_json(MANIFEST, manifest)
    if not entry["quality_gate_pass"]:
        state.update({
            "accepted_submits": int(state.get("accepted_submits", 0)) + 1,
            "last_accepted_submit_utc": attempt["submit_utc"],
            "last_generated_voice_beat": beat,
            "hold": True,
            "hold_reason": f"vo_b{beat} generated and saved for custody, but failed the script-fidelity/audio quality gate; no generation retry authorized",
            "status": "HOLD_VOICE_SCRIPT_FIDELITY_FAILURE",
            "updated_utc": utc_now(),
        })
        atomic_json(LANE_STATE, state)
        print("PGR_VOICE_QUALITY_HOLD", json.dumps({
            "beat": beat,
            "path": str(output),
            "sha256": entry["sha256"],
            "media_id": attempt["media_id"],
            "submit_utc": attempt["submit_utc"],
            "quality_gate_pass": False,
            "transcript": attempt["analysis"]["best_transcript"],
            "retry_used": False,
        }, sort_keys=True), flush=True)
        return 0
    state.update({
        "accepted_submits": int(state.get("accepted_submits", 0)) + 1,
        "last_accepted_submit_utc": attempt["submit_utc"],
        "last_completed_voice_beat": beat,
        "hold": False,
        "hold_reason": None,
        "status": "active",
        "updated_utc": utc_now(),
    })
    atomic_json(LANE_STATE, state)
    print("PGR_VOICE_COMPLETE", json.dumps({
        "beat": beat,
        "path": str(output),
        "sha256": entry["sha256"],
        "media_id": attempt["media_id"],
        "submit_utc": attempt["submit_utc"],
        "quality_gate_pass": entry["quality_gate_pass"],
        "transcript": attempt["analysis"]["best_transcript"],
        "voice_consistency": attempt["analysis"]["reference_comparison"],
        "retry_used": False,
    }, sort_keys=True), flush=True)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
