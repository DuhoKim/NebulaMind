#!/usr/bin/env python3
"""Broker-only sequential Veo native-narration batch for vo_02 through vo_07.

The runner preserves Chrome window 1 / tab 1 as the exact Flow project,
verifies Veo 3.1 Quality + 8s + 1x + 100 credits immediately before each
submit, acquires a short shared account-submission lease for exactly one
submit, polls to a playable prompt-matched result, downloads without
overwrite, and analyzes the generated audio against the approved vo_test_01
reference. It never writes the shared RUN_LEDGER directly; all control-plane
receipts are emitted only by broker operations.
"""
from __future__ import annotations

import argparse
import difflib
import hashlib
import importlib.util
import json
import math
import os
import re
import shutil
import subprocess
import sys
import time
from pathlib import Path
from typing import Any

import numpy as np

PACKET = Path(__file__).resolve().parents[1]
BRIEF = Path("/Users/duhokim/HermesOps/scripts/clips/narration/NARRATION_BATCH_BRIEF.md")
OUTPUT_DIR = BRIEF.parent
REFERENCE = OUTPUT_DIR / "vo_test_01.mp4"
MANIFEST = PACKET / "receipts" / "YUI_FLOW_VEO_NARRATION_BATCH_02_07_MANIFEST.json"
REJECTED_DIR = PACKET / "receipts" / "YUI_FLOW_VEO_NARRATION_REJECTED"
HELPER_PATH = PACKET / "canaries" / "yui_flow_hq_batch_02_13.py"
HERMES_PYTHON = Path("/Users/duhokim/.hermes/hermes-agent/venv/bin/python")
HERMES_REPO = Path("/Users/duhokim/.hermes/hermes-agent")
PROJECT_ROOT = "https://labs.google/fx/tools/flow/project/a22b5b61-833d-4e62-857b-4a7030b93bfa"
CONFIG_SUMMARY = "Video · 8s crop_16_9 1x"
NARRATOR = "a warm, calm, professional female documentary narrator delivers a clean studio voiceover with no on-screen speaker"

_spec = importlib.util.spec_from_file_location("hq_helper", HELPER_PATH)
assert _spec and _spec.loader
H = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(H)


def utc_now() -> str:
    return time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime())


def sha256_file(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()


def parse_brief() -> dict[int, dict[str, str]]:
    text = BRIEF.read_text()
    rows: dict[int, dict[str, str]] = {}
    for clip_num in range(2, 8):
        match = re.search(rf"^vo_{clip_num:02d} : (.+)$", text, re.MULTILINE)
        if not match:
            raise RuntimeError(f"brief is missing vo_{clip_num:02d}")
        prompt = match.group(1).strip()
        if prompt.count(NARRATOR) != 1:
            raise RuntimeError(f"narrator descriptor drift in vo_{clip_num:02d}")
        spoken = re.search(r'no on-screen speaker: "([^"]+)" Subtle cosmic ambience', prompt)
        if not spoken:
            raise RuntimeError(f"could not extract spoken line for vo_{clip_num:02d}")
        rows[clip_num] = {"prompt": prompt, "spoken_line": spoken.group(1)}
    return rows


def write_manifest(data: dict[str, Any]) -> None:
    MANIFEST.parent.mkdir(parents=True, exist_ok=True)
    tmp = MANIFEST.with_suffix(".json.tmp")
    tmp.write_text(json.dumps(data, indent=2, sort_keys=True) + "\n")
    os.replace(tmp, MANIFEST)


def wait_acquire(
    holder: str,
    kind: str,
    mode: str,
    scope: dict[str, Any],
    ttl: int,
    heartbeat: int,
    *,
    timeout: int = 1800,
    keepalive: tuple[dict[str, Any], ...] = (),
) -> dict[str, Any]:
    deadline = time.monotonic() + timeout
    attempt = 0
    while True:
        attempt += 1
        try:
            return H.acquire(holder, kind, mode, scope, ttl, heartbeat)
        except RuntimeError as exc:
            message = str(exc)
            if "conflict" not in message.lower() or time.monotonic() >= deadline:
                raise
            for lease in keepalive:
                H.heartbeat(lease)
            print(
                "LEASE_WAIT",
                json.dumps({"holder": holder, "kind": kind, "attempt": attempt, "reason": message}, sort_keys=True),
                flush=True,
            )
            time.sleep(10)


def safe_release(lease: dict[str, Any] | None) -> None:
    if not lease:
        return
    try:
        H.release(lease)
    except Exception as exc:
        print("LEASE_RELEASE_WARNING", lease.get("lease_id"), repr(exc), flush=True)


def acquire_write_set(clip_num: int, attempt: int) -> tuple[dict[str, Any], dict[str, Any], dict[str, Any]]:
    holder = f"yui-flow-narration-vo{clip_num:02d}-attempt{attempt}"
    target = wait_acquire(
        holder,
        "target",
        "write",
        {
            "host_id": "studio",
            "bundle": "com.google.Chrome",
            "user_data_dir": "default-google-chrome-profile",
            "window_id": "1",
            "target_id": "flow-project-a22b5b61",
        },
        1800,
        600,
    )
    desktop = focus = None
    try:
        desktop = wait_acquire(holder, "desktop-control", "write", {"host_id": "studio"}, 1200, 600)
        focus = wait_acquire(holder, "focus", "write", {"host_id": "studio"}, 1200, 600)
        return target, desktop, focus
    except Exception:
        safe_release(focus)
        safe_release(desktop)
        safe_release(target)
        raise


def verify_full_config(
    clip_num: int,
    attempt: int,
    target: dict[str, Any],
    desktop: dict[str, Any],
    focus: dict[str, Any],
) -> dict[str, Any]:
    H.probe_exact(target_lease=target)
    label = f"narration vo_{clip_num:02d} attempt {attempt}"
    H.check(target, f"open and verify {label} full Flow config")
    H.check(focus, f"focus {label} Flow config")
    H.check(desktop, f"AXPress {label} Flow config", uses_desktop=True)
    H.ax_press(
        "AXPopUpButton",
        'n.startsWith("Video ·")',
        before_attempt=lambda: H.probe_exact(target_lease=target),
    )
    time.sleep(1.5)
    state = H.run_js(
        r'''(() => {const vis=e=>{const s=getComputedStyle(e),r=e.getBoundingClientRect();return s.display!='none'&&s.visibility!='hidden'&&r.width>0&&r.height>0};const controls=[...document.querySelectorAll('button,[role=button],[role=tab]')].filter(vis).map(e=>({label:(e.innerText||e.textContent||'').trim().replace(/\s+/g,' '),selected:e.getAttribute('aria-selected')}));const lines=(document.body.innerText||'').split('\n').map(x=>x.trim()).filter(Boolean);return JSON.stringify({model:controls.find(x=>x.label.includes('Veo 3.1 - Quality'))?.label||'',duration:controls.filter(x=>['4s','6s','8s','10s'].includes(x.label)),outputs:controls.filter(x=>['1x','x2','x3','x4'].includes(x.label)),credit:lines.find(x=>/^100 credits$/.test(x))||'',audio_controls:controls.filter(x=>/audio|sound|voice/i.test(x.label))});})()'''
    )
    ok = (
        "Veo 3.1 - Quality" in state["model"]
        and any(x["label"] == "8s" and x["selected"] == "true" for x in state["duration"])
        and any(x["label"] == "1x" and x["selected"] == "true" for x in state["outputs"])
        and state["credit"] == "100 credits"
    )
    print(f"vo_{clip_num:02d} attempt {attempt} config", json.dumps(state, sort_keys=True), flush=True)
    if not ok:
        H.key_code(53)
        raise RuntimeError(f"Flow config drift for {label}: {state}")
    H.check(target, f"dismiss verified {label} config")
    H.check(focus, f"focused Escape dismiss {label} config")
    H.check(desktop, f"Escape dismiss {label} config", uses_desktop=True)
    H.key_code(53)
    time.sleep(0.8)
    return state


def paste_prompt(
    clip_num: int,
    attempt: int,
    prompt: str,
    target: dict[str, Any],
    desktop: dict[str, Any],
    focus: dict[str, Any],
) -> None:
    H.probe_exact(target_lease=target)
    holder = f"yui-flow-narration-vo{clip_num:02d}-attempt{attempt}"
    clipboard = wait_acquire(holder, "clipboard", "write", {"host_id": "studio"}, 120, 60)
    try:
        H.check(target, f"paste verbatim narration vo_{clip_num:02d} attempt {attempt} prompt")
        H.check(focus, f"AXPress narration vo_{clip_num:02d} attempt {attempt} composer")
        H.check(desktop, f"paste narration vo_{clip_num:02d} attempt {attempt} prompt", uses_desktop=True)
        H.check(clipboard, f"clipboard holds non-secret narration vo_{clip_num:02d} prompt")
        subprocess.run(
            ["osascript", "-", prompt],
            input="on run argv\nset the clipboard to item 1 of argv\nend run",
            text=True,
            check=True,
        )
        H.ax_press("AXTextArea", "true", before_attempt=lambda: H.probe_exact(target_lease=target))
        subprocess.run(
            [
                "osascript",
                "-e",
                'tell application "System Events" to keystroke "a" using {command down}',
                "-e",
                "delay 0.3",
                "-e",
                'tell application "System Events" to keystroke "v" using {command down}',
            ],
            check=True,
        )
        time.sleep(1.5)
    finally:
        safe_release(clipboard)
    state = H.run_js(
        r'''(() => {const vis=e=>{const s=getComputedStyle(e),r=e.getBoundingClientRect();return s.display!='none'&&s.visibility!='hidden'&&r.width>0&&r.height>0};const input=[...document.querySelectorAll('[contenteditable=true]')].find(vis);const buttons=[...document.querySelectorAll('button,[role=button]')].filter(vis);const create=buttons.find(e=>(e.innerText||e.textContent||'').includes('arrow_forward')&&(e.innerText||e.textContent||'').includes('Create'));return JSON.stringify({url:location.href,prompt:(input?(input.innerText||input.textContent||'').trim():null),active:document.activeElement===input,config:buttons.map(e=>(e.innerText||e.textContent||'').trim().replace(/\s+/g,' ')).find(x=>x.includes('Video ·'))||'',videos:document.querySelectorAll('video').length,create_disabled:create?create.disabled:null});})()'''
    )
    if state["prompt"] != prompt or state["config"] != CONFIG_SUMMARY or state["create_disabled"] is not False:
        raise RuntimeError(f"prompt/config verification failed for vo_{clip_num:02d} attempt {attempt}: {state}")


def refocus_composer(prompt: str, target: dict[str, Any]) -> None:
    H.ax_press("AXTextArea", "true", before_attempt=lambda: H.probe_exact(target_lease=target))
    state = H.run_js(
        r'''(() => {const vis=e=>{const s=getComputedStyle(e),r=e.getBoundingClientRect();return s.display!='none'&&s.visibility!='hidden'&&r.width>0&&r.height>0};const input=[...document.querySelectorAll('[contenteditable=true]')].find(vis);return JSON.stringify({prompt:(input?(input.innerText||input.textContent||'').trim():null),active:document.activeElement===input});})()'''
    )
    if state["prompt"] != prompt or not state["active"]:
        raise RuntimeError(f"composer refocus failed: {state}")


def submit_once(
    clip_num: int,
    attempt: int,
    prompt: str,
    target: dict[str, Any],
    desktop: dict[str, Any],
    focus: dict[str, Any],
) -> tuple[str, int, str]:
    H.probe_exact(target_lease=target)
    state = H.run_js(
        r'''(() => {const vis=e=>{const s=getComputedStyle(e),r=e.getBoundingClientRect();return s.display!='none'&&s.visibility!='hidden'&&r.width>0&&r.height>0};const input=[...document.querySelectorAll('[contenteditable=true]')].find(vis);const buttons=[...document.querySelectorAll('button,[role=button]')].filter(vis);return JSON.stringify({url:location.href,prompt:(input?(input.innerText||input.textContent||'').trim():null),active:document.activeElement===input,config:buttons.map(e=>(e.innerText||e.textContent||'').trim().replace(/\s+/g,' ')).find(x=>x.includes('Video ·'))||'',videos:document.querySelectorAll('video').length});})()'''
    )
    valid = state["url"] == PROJECT_ROOT and state["prompt"] == prompt and state["active"] and state["config"] == CONFIG_SUMMARY
    if not valid:
        raise RuntimeError(f"final pre-submit verification failed for vo_{clip_num:02d} attempt {attempt}: {state}")
    baseline_cards = int(state["videos"])
    for lease in (target, desktop, focus):
        H.heartbeat(lease)
    account = wait_acquire(
        f"yui-flow-narration-vo{clip_num:02d}-attempt{attempt}",
        "account-submission",
        "write",
        {"account": "google-ultra-shared"},
        120,
        60,
        keepalive=(target, desktop, focus),
    )
    submit_utc = utc_now()
    account_lease_id = account["lease_id"]
    try:
        H.check(target, f"submit narration vo_{clip_num:02d} attempt {attempt} exact Flow project")
        H.check(focus, f"Return on focused narration vo_{clip_num:02d} attempt {attempt} composer")
        H.check(desktop, f"Return submit narration vo_{clip_num:02d} attempt {attempt} Veo Quality 8s x1", uses_desktop=True)
        H.check(account, f"serialized shared-account submit narration vo_{clip_num:02d} attempt {attempt} Veo Quality x1")
        H.key_code(36)
        time.sleep(5)
    finally:
        safe_release(account)
    H.probe_exact(target_lease=target)
    accepted = H.run_js(
        r'''(() => {const vis=e=>{const s=getComputedStyle(e),r=e.getBoundingClientRect();return s.display!='none'&&s.visibility!='hidden'&&r.width>0&&r.height>0};const input=[...document.querySelectorAll('[contenteditable=true]')].find(vis);const lines=(document.body.innerText||'').split('\n').map(x=>x.trim()).filter(Boolean);return JSON.stringify({input:(input?(input.innerText||input.textContent||'').trim():null),videos:document.querySelectorAll('video').length,failed:[...document.querySelectorAll('*')].filter(e=>vis(e)&&e.children.length===0&&(e.innerText||e.textContent||'').trim()==='Failed').length,prompt_visible:lines.includes(''' + json.dumps(prompt) + r''')});})()'''
    )
    print(f"vo_{clip_num:02d} attempt {attempt} accepted", json.dumps(accepted, sort_keys=True), flush=True)
    if accepted["input"] != "What do you want to create?" or not accepted["prompt_visible"]:
        raise RuntimeError(f"submit acceptance not proven for vo_{clip_num:02d} attempt {attempt}: {accepted}")
    return submit_utc, baseline_cards, account_lease_id


def acquire_read_poll(clip_num: int, attempt: int) -> dict[str, Any]:
    return wait_acquire(
        f"yui-flow-narration-vo{clip_num:02d}-attempt{attempt}-poll",
        "target",
        "read",
        {
            "host_id": "studio",
            "bundle": "com.google.Chrome",
            "user_data_dir": "default-google-chrome-profile",
            "window_id": "1",
            "target_id": "flow-project-a22b5b61",
        },
        1200,
        600,
    )


def inspect_newest_with_lease(
    lease: dict[str, Any],
    clip_num: int,
    attempt: int,
    prompt: str,
) -> dict[str, Any] | None:
    H.ensure_root(lease)
    H.probe_exact(target_lease=lease)
    H.check(lease, f"read-only inspect newest settled narration vo_{clip_num:02d} attempt {attempt} card")
    clicked = H.run_js(
        r'''(() => {const cards=[...document.querySelectorAll('video')].map(v=>v.closest('button,[role=button]')).filter((e,i,a)=>e&&a.indexOf(e)===i);if(!cards[0])return JSON.stringify({clicked:false,count:cards.length});cards[0].click();return JSON.stringify({clicked:true,count:cards.length});})()'''
    )
    if not clicked["clicked"]:
        return None
    time.sleep(2)
    detail = None
    for _ in range(15):
        H.probe_exact(target_lease=lease)
        detail = H.run_js(
            r'''(() => {const lines=(document.body.innerText||'').split('\n').map(x=>x.trim()).filter(Boolean);const v=[...document.querySelectorAll('video')][0];return JSON.stringify({url:location.href,prompts:lines.filter(x=>x.length>70&&!x.includes('Google Flow - AI Creative Studio')),video:v?{readyState:v.readyState,duration:Number.isFinite(v.duration)?v.duration:null,width:v.videoWidth,height:v.videoHeight}:null,failed:lines.includes('Failed')});})()'''
        )
        video = detail.get("video") if detail else None
        if video and video["readyState"] >= 2 and video["duration"] is not None:
            break
        time.sleep(2)
    if detail and prompt in detail.get("prompts", []):
        video = detail.get("video")
        if not detail.get("failed") and video and video["readyState"] >= 2 and 7.0 <= video["duration"] <= 10.5 and video["width"] >= 1280 and video["height"] >= 720:
            return {"media_id": detail["url"].rstrip("/").split("/")[-1], **detail}
    H.run_js_raw("history.back(); 'BACK'")
    time.sleep(2)
    H.ensure_root(lease)
    return None


def poll_to_playable(clip_num: int, attempt: int, prompt: str) -> dict[str, Any]:
    lease = acquire_read_poll(clip_num, attempt)
    start = time.monotonic()
    lease_start = start
    complete_stable = 0
    failed_stable = 0
    try:
        for poll_num in range(1, 91):
            H.probe_exact(target_lease=lease)
            state = H.run_js(
                r'''(() => {const vis=e=>{const s=getComputedStyle(e),r=e.getBoundingClientRect();return s.display!='none'&&s.visibility!='hidden'&&r.width>0&&r.height>0};const lines=(document.body.innerText||'').split('\n').map(x=>x.trim()).filter(Boolean);return JSON.stringify({url:location.href,videos:document.querySelectorAll('video').length,failed:[...document.querySelectorAll('*')].filter(e=>vis(e)&&e.children.length===0&&(e.innerText||e.textContent||'').trim()==='Failed').length,prompt_visible:lines.includes(''' + json.dumps(prompt) + r'''),status:lines.filter(x=>/Generating|Creating|Queued|Pending|Failed/.test(x)).slice(-20)});})()'''
            )
            elapsed = round(time.monotonic() - start, 1)
            print(
                f"vo_{clip_num:02d} attempt {attempt} poll",
                json.dumps({"poll": poll_num, "elapsed_s": elapsed, **state}, sort_keys=True),
                flush=True,
            )
            candidate = not state["prompt_visible"] and state["failed"] == 0
            complete_stable = complete_stable + 1 if candidate else 0
            failed_stable = failed_stable + 1 if state["prompt_visible"] and state["failed"] > 0 else 0
            if complete_stable >= 2:
                detail = inspect_newest_with_lease(lease, clip_num, attempt, prompt)
                if detail:
                    detail["settlement_elapsed_s"] = elapsed
                    return detail
                complete_stable = 0
            if failed_stable >= 18:
                raise RuntimeError(f"terminal Failed persisted for narration vo_{clip_num:02d} attempt {attempt}")
            if time.monotonic() - lease_start >= 240:
                safe_release(lease)
                lease = acquire_read_poll(clip_num, attempt)
                lease_start = time.monotonic()
            time.sleep(10)
    finally:
        safe_release(lease)
    raise RuntimeError(f"settlement timeout for narration vo_{clip_num:02d} attempt {attempt}")


def download_current_detail(clip_num: int, attempt: int, media_id: str, destination: Path) -> Path:
    if destination.exists():
        raise RuntimeError(f"refusing to overwrite temporary artifact {destination}")
    target = wait_acquire(
        f"yui-flow-narration-vo{clip_num:02d}-attempt{attempt}-save",
        "target",
        "write",
        {
            "host_id": "studio",
            "bundle": "com.google.Chrome",
            "user_data_dir": "default-google-chrome-profile",
            "window_id": "1",
            "target_id": "flow-project-a22b5b61",
        },
        900,
        300,
    )
    downloads = Path.home() / "Downloads"
    before = {p.name: (p.stat().st_mtime_ns, p.stat().st_size) for p in downloads.iterdir() if p.is_file()}
    try:
        probe = H.probe_exact(target_lease=target)
        if not probe["url"].endswith("/" + media_id):
            H.emergency_freeze(f"narration download detail target mismatch for vo_{clip_num:02d} attempt {attempt}", target)
        H.check(target, f"invoke visible Flow Download for settled narration vo_{clip_num:02d} attempt {attempt}")
        click = H.run_js(
            r'''(() => {const b=[...document.querySelectorAll('button,[role=button]')].find(e=>{const t=(e.getAttribute('aria-label')||e.getAttribute('title')||e.innerText||e.textContent||'').trim().replace(/\s+/g,' ');return t==='download Download'||t==='Download'||t.endsWith(' Download')});if(!b)return JSON.stringify({clicked:false});b.click();return JSON.stringify({clicked:true});})()'''
        )
        if not click["clicked"]:
            raise RuntimeError(f"Flow Download control not found for vo_{clip_num:02d} attempt {attempt}")
        started = time.time()
        candidates: list[Path] = []
        for _ in range(180):
            partials = [p for p in downloads.iterdir() if p.is_file() and p.suffix == ".crdownload"]
            candidates = []
            for path in downloads.iterdir():
                if not path.is_file() or path.suffix == ".crdownload":
                    continue
                stat = path.stat()
                old = before.get(path.name)
                if old is not None and old == (stat.st_mtime_ns, stat.st_size):
                    continue
                if stat.st_mtime < started - 2 or stat.st_size <= 0:
                    continue
                info = H.ffprobe(path, allow_failure=True)
                if info and 7.0 <= info["duration"] <= 10.5 and info["width"] >= 1280 and info["height"] >= 720:
                    candidates.append(path)
            if len(candidates) == 1 and not partials:
                break
            if len(candidates) > 1:
                raise RuntimeError(f"ambiguous concurrent downloads: {[p.name for p in candidates]}")
            time.sleep(1)
        if len(candidates) != 1:
            raise RuntimeError(f"no completed Flow download detected for vo_{clip_num:02d} attempt {attempt}")
        destination.parent.mkdir(parents=True, exist_ok=True)
        shutil.move(str(candidates[0]), str(destination))
        H.run_js_raw("history.back(); 'BACK'")
        time.sleep(1.5)
        H.ensure_root(target)
        return destination
    finally:
        safe_release(target)


def canonical_tokens(text: str) -> list[str]:
    value = text.lower().replace("here’s", "here is").replace("here's", "here is")
    value = re.sub(r"\ba\s*\.\s*i\s*\.?", "ai", value)
    # Speech recognizers normally render the spoken phrase "nebula mind dot
    # net" as the written domain "nebulamind.net". Canonicalize both forms to
    # the same tokens without erasing the required spoken "dot".
    value = re.sub(r"\bnebula\s+mind\s+dot\s+net\b", "nebulamind dot net", value)
    value = re.sub(r"\bnebulamind\s*\.\s*net\b", "nebulamind dot net", value)
    return re.findall(r"[a-z0-9]+", value)


def lcs_alignment(expected: list[str], observed: list[str]) -> tuple[int, list[str], list[str]]:
    rows = len(expected) + 1
    cols = len(observed) + 1
    table = [[0] * cols for _ in range(rows)]
    for i in range(1, rows):
        for j in range(1, cols):
            if expected[i - 1] == observed[j - 1]:
                table[i][j] = table[i - 1][j - 1] + 1
            else:
                table[i][j] = max(table[i - 1][j], table[i][j - 1])
    i, j = len(expected), len(observed)
    matched_expected: set[int] = set()
    matched_observed: set[int] = set()
    while i and j:
        if expected[i - 1] == observed[j - 1]:
            matched_expected.add(i - 1)
            matched_observed.add(j - 1)
            i -= 1
            j -= 1
        elif table[i - 1][j] >= table[i][j - 1]:
            i -= 1
        else:
            j -= 1
    missing = [token for index, token in enumerate(expected) if index not in matched_expected]
    extras = [token for index, token in enumerate(observed) if index not in matched_observed]
    return table[-1][-1], missing, extras


def assess_wording(expected_text: str, transcript: str) -> dict[str, Any]:
    expected = canonical_tokens(expected_text)
    observed = canonical_tokens(transcript)
    lcs, missing, extras = lcs_alignment(expected, observed)
    similarity = difflib.SequenceMatcher(None, expected, observed).ratio() if expected or observed else 1.0
    coverage = lcs / len(expected) if expected else 1.0
    passed = not missing and not extras and similarity >= 0.90
    return {
        "expected_tokens": expected,
        "observed_tokens": observed,
        "missing_tokens": missing,
        "extra_tokens": extras,
        "coverage": round(coverage, 4),
        "token_similarity": round(similarity, 4),
        "pass": passed,
    }


def decode_pcm(path: Path, filter_audio: str | None = None) -> np.ndarray:
    command = ["ffmpeg", "-v", "error", "-i", str(path), "-vn"]
    if filter_audio:
        command.extend(["-af", filter_audio])
    command.extend(["-ac", "1", "-ar", "16000", "-f", "f32le", "-"])
    result = subprocess.run(command, capture_output=True, check=True)
    return np.frombuffer(result.stdout, dtype="<f4").astype(np.float64)


def signal_features(path: Path) -> dict[str, Any]:
    audio = decode_pcm(path)
    if not len(audio):
        raise RuntimeError(f"empty audio stream: {path}")
    peak = float(np.max(np.abs(audio)))
    rms = float(np.sqrt(np.mean(audio * audio)))
    frame_len, hop = 640, 160
    frames = []
    for start in range(0, max(0, len(audio) - frame_len + 1), hop):
        frame = audio[start : start + frame_len]
        frame_rms = float(np.sqrt(np.mean(frame * frame)))
        frames.append((frame, frame_rms))
    energies = np.array([value for _, value in frames])
    threshold = max(float(np.percentile(energies, 55)) if len(energies) else 0.0, rms * 0.65, 1e-4)
    f0_values: list[float] = []
    centroids: list[float] = []
    spectra: list[np.ndarray] = []
    window = np.hanning(frame_len)
    min_lag = int(16000 / 360)
    max_lag = int(16000 / 80)
    freqs = np.fft.rfftfreq(frame_len, 1 / 16000)
    for frame, frame_rms in frames:
        if frame_rms < threshold:
            continue
        centered = (frame - np.mean(frame)) * window
        corr = np.correlate(centered, centered, mode="full")[frame_len - 1 :]
        if corr[0] > 0:
            window_corr = corr[min_lag : max_lag + 1] / corr[0]
            lag_offset = int(np.argmax(window_corr))
            strength = float(window_corr[lag_offset])
            if strength >= 0.25:
                lag = min_lag + lag_offset
                f0_values.append(16000 / lag)
        magnitude = np.abs(np.fft.rfft(centered)) + 1e-12
        mask = freqs <= 4000
        centroids.append(float(np.sum(freqs[mask] * magnitude[mask]) / np.sum(magnitude[mask])))
        # A coarse normalized log-spectral envelope for broad outlier detection.
        logmag = np.log1p(magnitude[mask])
        sample_x = np.linspace(0, len(logmag) - 1, 64)
        signature = np.interp(sample_x, np.arange(len(logmag)), logmag)
        signature = signature - np.mean(signature)
        norm = np.linalg.norm(signature)
        if norm > 0:
            spectra.append(signature / norm)
    average_signature = np.mean(spectra, axis=0) if spectra else np.zeros(64)
    signature_norm = np.linalg.norm(average_signature)
    if signature_norm > 0:
        average_signature /= signature_norm
    return {
        "duration_s": round(len(audio) / 16000, 4),
        "peak_dbfs": round(20 * math.log10(max(peak, 1e-12)), 2),
        "rms_dbfs": round(20 * math.log10(max(rms, 1e-12)), 2),
        "median_f0_hz": round(float(np.median(f0_values)), 2) if f0_values else None,
        "median_spectral_centroid_hz": round(float(np.median(centroids)), 2) if centroids else None,
        "voiced_frame_count": len(f0_values),
        "active_frame_count": len(centroids),
        "signature": [round(float(x), 8) for x in average_signature],
    }


def center_side_metrics(path: Path) -> dict[str, Any]:
    mid = decode_pcm(path, "pan=mono|c0=0.5*c0+0.5*c1")
    side = decode_pcm(path, "pan=mono|c0=0.5*c0-0.5*c1")
    mid_rms = float(np.sqrt(np.mean(mid * mid)))
    side_rms = float(np.sqrt(np.mean(side * side)))
    mid_db = 20 * math.log10(max(mid_rms, 1e-12))
    side_db = 20 * math.log10(max(side_rms, 1e-12))
    return {
        "mid_rms_dbfs": round(mid_db, 2),
        "side_rms_dbfs": round(side_db, 2),
        "mid_over_side_db": round(mid_db - side_db, 2),
    }


def transcribe_audio(path: Path) -> dict[str, Any]:
    code = (
        "import json,sys; "
        "from tools.transcription_tools import transcribe_audio; "
        "print(json.dumps(transcribe_audio(sys.argv[1]),ensure_ascii=False,sort_keys=True))"
    )
    last: dict[str, Any] | None = None
    for attempt in range(2):
        result = subprocess.run(
            [str(HERMES_PYTHON), "-c", code, str(path)],
            cwd=HERMES_REPO,
            text=True,
            capture_output=True,
            timeout=180,
        )
        if result.returncode == 0 and result.stdout.strip():
            try:
                parsed = json.loads(result.stdout.strip().splitlines()[-1])
                last = parsed if isinstance(parsed, dict) else {
                    "success": False,
                    "error": f"unexpected transcription response: {parsed!r}",
                    "transcript": "",
                }
            except json.JSONDecodeError:
                last = {"success": False, "error": result.stdout.strip(), "transcript": ""}
            if last.get("success"):
                return last
        else:
            last = {"success": False, "error": result.stderr.strip(), "transcript": ""}
        time.sleep(2)
    raise RuntimeError(f"managed transcription failed for {path}: {last}")


def audio_analysis(
    artifact: Path,
    spoken_line: str,
    reference_features: dict[str, Any],
    work_dir: Path,
) -> dict[str, Any]:
    full_audio = work_dir / f"{artifact.stem}_full.mp3"
    mid_audio = work_dir / f"{artifact.stem}_mid.mp3"
    subprocess.run(
        ["ffmpeg", "-y", "-v", "error", "-i", str(artifact), "-vn", "-ac", "1", "-ar", "16000", "-b:a", "64k", str(full_audio)],
        check=True,
    )
    subprocess.run(
        [
            "ffmpeg",
            "-y",
            "-v",
            "error",
            "-i",
            str(artifact),
            "-filter_complex",
            "[0:a]pan=mono|c0=0.5*c0+0.5*c1",
            "-ar",
            "16000",
            "-b:a",
            "64k",
            str(mid_audio),
        ],
        check=True,
    )
    full_stt = transcribe_audio(full_audio)
    mid_stt = transcribe_audio(mid_audio)
    full_wording = assess_wording(spoken_line, full_stt["transcript"])
    mid_wording = assess_wording(spoken_line, mid_stt["transcript"])
    if mid_wording["token_similarity"] > full_wording["token_similarity"]:
        best_transcript = mid_stt["transcript"]
        best_wording = mid_wording
        best_source = "mid"
    else:
        best_transcript = full_stt["transcript"]
        best_wording = full_wording
        best_source = "full"
    features = signal_features(artifact)
    ref_f0 = reference_features.get("median_f0_hz")
    cand_f0 = features.get("median_f0_hz")
    f0_ratio = cand_f0 / ref_f0 if ref_f0 and cand_f0 else None
    ref_centroid = reference_features.get("median_spectral_centroid_hz")
    cand_centroid = features.get("median_spectral_centroid_hz")
    centroid_ratio = cand_centroid / ref_centroid if ref_centroid and cand_centroid else None
    ref_sig = np.array(reference_features["signature"], dtype=float)
    cand_sig = np.array(features["signature"], dtype=float)
    timbre_similarity = float(np.dot(ref_sig, cand_sig)) if np.linalg.norm(ref_sig) and np.linalg.norm(cand_sig) else 0.0
    voice_pass = (
        f0_ratio is not None
        and 0.60 <= f0_ratio <= 1.67
        and centroid_ratio is not None
        and 0.55 <= centroid_ratio <= 1.80
        and timbre_similarity >= 0.45
    )
    center_side = center_side_metrics(artifact)
    media = H.ffprobe(artifact)
    assert media is not None
    wording_pass = bool(best_wording["pass"])
    quality_pass = wording_pass and voice_pass and media.get("audio_codec") is not None
    score = (
        (100.0 if wording_pass else 0.0)
        + 10.0 * float(best_wording["token_similarity"])
        + max(-1.0, min(1.0, timbre_similarity))
        + (1.0 if voice_pass else 0.0)
    )
    features_public = {k: v for k, v in features.items() if k != "signature"}
    return {
        "full_transcript": full_stt["transcript"],
        "mid_transcript": mid_stt["transcript"],
        "best_transcript": best_transcript,
        "best_transcript_source": best_source,
        "full_wording": full_wording,
        "mid_wording": mid_wording,
        "wording_pass": wording_pass,
        "signal": features_public,
        "center_side": center_side,
        "reference_comparison": {
            "f0_ratio": round(f0_ratio, 4) if f0_ratio is not None else None,
            "spectral_centroid_ratio": round(centroid_ratio, 4) if centroid_ratio is not None else None,
            "timbre_signature_cosine": round(timbre_similarity, 4),
            "voice_consistency_pass": voice_pass,
            "method": "broad automated acoustic-outlier gate versus vo_test_01; not human speaker verification",
        },
        "single_clean_narrator_supported": bool(wording_pass and full_stt.get("success") and mid_stt.get("success")),
        "quality_pass": quality_pass,
        "quality_score": round(score, 4),
        "media": media,
    }


def analyze_reference(work_dir: Path) -> dict[str, Any]:
    if not REFERENCE.exists():
        raise RuntimeError(f"approved reference missing: {REFERENCE}")
    features = signal_features(REFERENCE)
    public = {k: v for k, v in features.items() if k != "signature"}
    public["path"] = str(REFERENCE)
    public["sha256"] = sha256_file(REFERENCE)
    return {"features": features, "public": public}


def generate_attempt(
    clip_num: int,
    attempt: int,
    prompt: str,
    spoken_line: str,
    reference_features: dict[str, Any],
    work_dir: Path,
) -> dict[str, Any]:
    target = desktop = focus = None
    submit_utc = ""
    baseline_cards = 0
    account_lease_id = ""
    try:
        target, desktop, focus = acquire_write_set(clip_num, attempt)
        H.ensure_root(target)
        verify_full_config(clip_num, attempt, target, desktop, focus)
        paste_prompt(clip_num, attempt, prompt, target, desktop, focus)
        verify_full_config(clip_num, attempt, target, desktop, focus)
        refocus_composer(prompt, target)
        submit_utc, baseline_cards, account_lease_id = submit_once(clip_num, attempt, prompt, target, desktop, focus)
    finally:
        safe_release(focus)
        safe_release(desktop)
        safe_release(target)
    detail = poll_to_playable(clip_num, attempt, prompt)
    temporary = work_dir / f"vo_{clip_num:02d}_attempt{attempt}.mp4"
    download_current_detail(clip_num, attempt, detail["media_id"], temporary)
    analysis = audio_analysis(temporary, spoken_line, reference_features, work_dir)
    return {
        "attempt": attempt,
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


def choose_attempt(attempts: list[dict[str, Any]]) -> dict[str, Any]:
    passing = [row for row in attempts if row["analysis"]["quality_pass"]]
    pool = passing or attempts
    return max(pool, key=lambda row: row["analysis"]["quality_score"])


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--start", type=int, default=2)
    parser.add_argument("--end", type=int, default=7)
    parser.add_argument("--dry-run", action="store_true")
    args = parser.parse_args()
    if not (2 <= args.start <= args.end <= 7):
        raise SystemExit("range must satisfy 2 <= start <= end <= 7")
    rows = parse_brief()
    for clip_num in range(args.start, args.end + 1):
        target = OUTPUT_DIR / f"vo_{clip_num:02d}.mp4"
        if target.exists():
            raise RuntimeError(f"refusing to overwrite existing narration artifact: {target}")
    if args.dry_run:
        print(
            json.dumps(
                {
                    "brief": str(BRIEF),
                    "brief_sha256": sha256_file(BRIEF),
                    "range": [args.start, args.end],
                    "narrator_descriptor_exact": True,
                    "outputs_absent": True,
                    "no_direct_ledger_append": True,
                },
                sort_keys=True,
            )
        )
        return 0

    run_id = time.strftime("%Y%m%dT%H%M%SZ", time.gmtime())
    work_dir = Path("/tmp") / f"yui-flow-narration-{run_id}-{os.getpid()}"
    work_dir.mkdir(parents=True, exist_ok=False)
    reference = analyze_reference(work_dir)
    manifest: dict[str, Any] = {
        "status": "in_progress",
        "started_utc": utc_now(),
        "updated_utc": utc_now(),
        "brief": str(BRIEF),
        "brief_sha256": sha256_file(BRIEF),
        "project_id": H.PROJECT_ID,
        "model": "Veo 3.1 - Quality",
        "duration": "8s",
        "aspect_ratio": "16:9",
        "output_count": "1x",
        "displayed_cost_per_submit": 100,
        "narrator_descriptor": NARRATOR,
        "reference": reference["public"],
        "no_direct_run_ledger_appends": True,
        "clips": [],
    }
    write_manifest(manifest)

    for clip_num in range(args.start, args.end + 1):
        prompt = rows[clip_num]["prompt"]
        spoken_line = rows[clip_num]["spoken_line"]
        attempts: list[dict[str, Any]] = []
        for attempt in (1, 2):
            print(f"START vo_{clip_num:02d} attempt {attempt}", flush=True)
            row = generate_attempt(clip_num, attempt, prompt, spoken_line, reference["features"], work_dir)
            attempts.append(row)
            if row["analysis"]["quality_pass"]:
                break
            if attempt == 1:
                print(
                    "AUTHORIZED_QUALITY_RETRY",
                    json.dumps(
                        {
                            "clip": f"vo_{clip_num:02d}",
                            "wording_pass": row["analysis"]["wording_pass"],
                            "voice_consistency_pass": row["analysis"]["reference_comparison"]["voice_consistency_pass"],
                        },
                        sort_keys=True,
                    ),
                    flush=True,
                )
        selected = choose_attempt(attempts)
        output = OUTPUT_DIR / f"vo_{clip_num:02d}.mp4"
        selected_path = Path(selected["artifact_temp"])
        if output.exists():
            raise RuntimeError(f"refusing overwrite during finalization: {output}")
        shutil.move(str(selected_path), str(output))
        for rejected in attempts:
            path = Path(rejected["artifact_temp"])
            if path.exists():
                REJECTED_DIR.mkdir(parents=True, exist_ok=True)
                destination = REJECTED_DIR / f"vo_{clip_num:02d}_attempt{rejected['attempt']}_not_selected.mp4"
                if destination.exists():
                    raise RuntimeError(f"refusing overwrite rejected-attempt artifact: {destination}")
                shutil.move(str(path), str(destination))
                rejected["artifact_rejected_path"] = str(destination)
                rejected["artifact_rejected_sha256"] = sha256_file(destination)
            rejected.pop("artifact_temp", None)
        selected_attempt = selected["attempt"]
        clip_entry = {
            "clip_num": clip_num,
            "prompt": prompt,
            "prompt_sha256": hashlib.sha256(prompt.encode()).hexdigest(),
            "spoken_line": spoken_line,
            "spoken_line_sha256": hashlib.sha256(spoken_line.encode()).hexdigest(),
            "attempt_count": len(attempts),
            "retry_used": len(attempts) == 2,
            "selected_attempt": selected_attempt,
            "quality_gate_pass": selected["analysis"]["quality_pass"],
            "path": str(output),
            "sha256": sha256_file(output),
            "attempts": attempts,
        }
        manifest["clips"].append(clip_entry)
        manifest["updated_utc"] = utc_now()
        write_manifest(manifest)
        print(
            "CLIP_COMPLETE",
            json.dumps(
                {
                    "clip": f"vo_{clip_num:02d}",
                    "path": str(output),
                    "selected_attempt": selected_attempt,
                    "retry_used": len(attempts) == 2,
                    "quality_gate_pass": clip_entry["quality_gate_pass"],
                    "transcript": selected["analysis"]["best_transcript"],
                    "voice_consistency": selected["analysis"]["reference_comparison"],
                },
                sort_keys=True,
            ),
            flush=True,
        )

    failures = [row["clip_num"] for row in manifest["clips"] if not row["quality_gate_pass"]]
    manifest["status"] = "completed" if not failures else "completed_with_quality_failures"
    manifest["quality_failure_clips"] = failures
    manifest["completed_utc"] = utc_now()
    manifest["updated_utc"] = utc_now()
    manifest["submit_count"] = sum(row["attempt_count"] for row in manifest["clips"])
    manifest["expected_credit_cost"] = manifest["submit_count"] * 100
    write_manifest(manifest)
    print(json.dumps(manifest, sort_keys=True), flush=True)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
