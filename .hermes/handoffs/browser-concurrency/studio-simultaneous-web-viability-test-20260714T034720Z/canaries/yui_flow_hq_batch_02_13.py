#!/usr/bin/env python3
"""Broker-gated sequential Google Flow HQ regeneration for clips 02-13.

This script intentionally targets one exact Chrome window/tab/project, uses semantic
macOS AX for trusted React input, serializes every submit through the shared-account
broker, treats early Failed cards as provisional, polls to a playable prompt-matched
media detail, and refuses to overwrite any target artifact.
"""

from __future__ import annotations

import argparse
import hashlib
import importlib.util
import json
import os
import shutil
import subprocess
import sys
import time
from pathlib import Path
from typing import Any, Callable

PACKET = Path(__file__).resolve().parents[1]
PROJECT_ID = "a22b5b61-833d-4e62-857b-4a7030b93bfa"
PROJECT_ROOT = f"https://labs.google/fx/tools/flow/project/{PROJECT_ID}"
WINDOW_INDEX = 1
TAB_INDEX = 1
BROKER_SOCKET = "/tmp/nmbrk-live-20260714/b.sock"
PROMPTS_PATH = Path("/Users/duhokim/HermesOps/scripts/clips/prompts.txt")
OUTPUT_DIR = PROMPTS_PATH.parent
MANIFEST_PATH = PACKET / "receipts" / "YUI_FLOW_HQ_BATCH_02_13_MANIFEST.json"
PROBE_PATH = PACKET / "canaries" / "_tmp_yui_flow_page_probe.py"
JOURNAL = PACKET / "broker" / "journal.py"
LEDGER = PACKET / "ledger" / "RUN_LEDGER.jsonl"

sys.path.insert(0, str(PACKET))
from broker.transport import UDSClient  # noqa: E402

_spec = importlib.util.spec_from_file_location("flow_probe", PROBE_PATH)
assert _spec and _spec.loader
_probe_module = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_probe_module)

APPLESCRIPT = """on run argv
set jsCode to item 1 of argv
tell application \"Google Chrome\"
return execute tab 1 of window 1 javascript jsCode
end tell
end run"""

PROMPTS = [line.strip() for line in PROMPTS_PATH.read_text().splitlines() if line.strip()]
if len(PROMPTS) != 13:
    raise RuntimeError(f"expected 13 prompts, found {len(PROMPTS)}")


def utc_now() -> str:
    return time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime())


def sha256_file(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()


def run_js_raw(js: str) -> str:
    result = subprocess.run(
        ["osascript", "-", js],
        input=APPLESCRIPT,
        text=True,
        capture_output=True,
        check=True,
    )
    return result.stdout.strip()


def run_js(js: str) -> Any:
    raw = run_js_raw(js)
    return json.loads(raw)


def broker_op(payload: dict[str, Any]) -> dict[str, Any]:
    client = UDSClient(BROKER_SOCKET)
    try:
        return client.op(payload)
    finally:
        client.close()


def acquire(holder: str, kind: str, mode: str, scope: dict[str, Any], ttl: int, heartbeat: int) -> dict[str, Any]:
    result = broker_op(
        {
            "op": "acquire",
            "holder": holder,
            "kind": kind,
            "mode": mode,
            "scope": scope,
            "ttl": ttl,
            "heartbeat_interval": heartbeat,
        }
    )
    if not result.get("ok"):
        raise RuntimeError(f"lease denied: {result}")
    return result["lease"]


def release(lease: dict[str, Any] | None) -> None:
    if not lease:
        return
    result = broker_op({"op": "release", "lease_id": lease["lease_id"]})
    if not result.get("ok"):
        raise RuntimeError(f"lease release failed: {lease['lease_id']} {result}")


def heartbeat(lease: dict[str, Any]) -> None:
    result = broker_op({"op": "heartbeat", "lease_id": lease["lease_id"]})
    if not result.get("ok"):
        raise RuntimeError(f"heartbeat failed: {lease['lease_id']} {result}")


def check(lease: dict[str, Any], action: str, uses_desktop: bool = False, target_verified: bool = True) -> None:
    result = broker_op(
        {
            "op": "check",
            "lease_id": lease["lease_id"],
            "epoch": lease["epoch"],
            "action": action,
            "uses_desktop": uses_desktop,
            "target_verified": target_verified,
        }
    )
    if not result.get("ok"):
        raise RuntimeError(f"broker check denied: {result}")


def emergency_freeze(reason: str, target_lease: dict[str, Any] | None = None) -> None:
    if target_lease:
        try:
            check(target_lease, f"target verification failed: {reason}", target_verified=False)
        except Exception:
            pass
    print("EMERGENCY_FREEZE", reason, flush=True)
    print(broker_op({"op": "freeze", "declared_by": "yui", "reason": reason}), flush=True)
    raise RuntimeError(reason)


def probe_exact(*, allow_detail: bool = True, target_lease: dict[str, Any] | None = None) -> dict[str, Any]:
    probe = _probe_module.probe_live_flow_page()
    if probe["challenge"]:
        reason = "Real Flow-page challenge: " + ",".join(probe["signals"])
        print("PAGE_CHALLENGE", json.dumps(probe, sort_keys=True), flush=True)
        print(broker_op({"op": "freeze", "declared_by": "yui", "reason": reason}), flush=True)
        raise RuntimeError(reason)
    url = probe["url"]
    url_valid = url == PROJECT_ROOT or (allow_detail and url.startswith(PROJECT_ROOT + "/edit/"))
    if not url_valid:
        emergency_freeze(f"Flow target drift: expected {PROJECT_ROOT}, observed {url}", target_lease)
    placement_valid = probe["window_index"] == WINDOW_INDEX and probe["tab_index"] == TAB_INDEX
    if not placement_valid:
        raise RuntimeError(
            "Flow target placement mismatch without URL drift: "
            f"expected window/tab {WINDOW_INDEX}/{TAB_INDEX}, "
            f"observed {probe['window_index']}/{probe['tab_index']}; URL matched {url}"
        )
    return probe


def ensure_root(target_lease: dict[str, Any] | None = None) -> None:
    probe = probe_exact(allow_detail=True, target_lease=target_lease)
    if probe["url"] == PROJECT_ROOT:
        return
    if target_lease:
        check(target_lease, "read-only return from media detail to exact Flow project root")
    run_js_raw("history.back(); 'BACK'")
    for _ in range(20):
        time.sleep(0.5)
        if probe_exact(allow_detail=True, target_lease=target_lease)["url"] == PROJECT_ROOT:
            return
    emergency_freeze("Could not return to exact Flow project root", target_lease)


def ax_press(
    role: str,
    name_predicate_js: str,
    *,
    attempts: int = 12,
    interval: float = 0.5,
    before_attempt: Callable[[], Any] | None = None,
) -> None:
    js = f'''const p=Application("System Events").processes.byName("Google Chrome");
const w=p.windows[0];let pressed=false,matched="";
function walk(e,d){{if(pressed||d>28)return;try{{const n=String(e.name()||"");if(e.role()==={json.dumps(role)}&&({name_predicate_js})){{matched=n;const a=e.actions().find(x=>x.name()==="AXPress");if(a){{a.perform();pressed=true;return}}}}}}catch(_){{}};try{{for(const c of e.uiElements())walk(c,d+1)}}catch(_){{}}}}
walk(w,0);JSON.stringify({{pressed,matched}})'''
    for attempt in range(attempts):
        if before_attempt:
            before_attempt()
        result = subprocess.run(
            ["osascript", "-l", "JavaScript", "-e", js],
            text=True,
            capture_output=True,
            check=True,
        )
        data = json.loads(result.stdout)
        if data.get("pressed"):
            return
        if attempt + 1 < attempts:
            time.sleep(interval)
    raise RuntimeError(f"AXPress failed for role={role} after {attempts} readiness attempts")


def key_code(code: int) -> None:
    subprocess.run(
        ["osascript", "-e", f'tell application "System Events" to key code {code}'],
        check=True,
    )


def verify_full_config(target: dict[str, Any], desktop: dict[str, Any], focus: dict[str, Any], clip_num: int) -> None:
    probe_exact(target_lease=target)
    check(target, f"open and verify HQ clip_{clip_num:02d} full Flow config")
    check(focus, f"focus HQ clip_{clip_num:02d} Flow config")
    check(desktop, f"AXPress HQ clip_{clip_num:02d} Flow config", uses_desktop=True)
    ax_press(
        "AXPopUpButton",
        'n.startsWith("Video ·")',
        before_attempt=lambda: probe_exact(target_lease=target),
    )
    time.sleep(1.5)
    state = run_js(
        r'''(() => {const vis=e=>{const s=getComputedStyle(e),r=e.getBoundingClientRect();return s.display!='none'&&s.visibility!='hidden'&&r.width>0&&r.height>0};const controls=[...document.querySelectorAll('button,[role=button],[role=tab]')].filter(vis).map(e=>({label:(e.innerText||e.textContent||'').trim().replace(/\s+/g,' '),selected:e.getAttribute('aria-selected')}));const lines=(document.body.innerText||'').split('\n').map(x=>x.trim()).filter(Boolean);return JSON.stringify({model:controls.find(x=>x.label.includes('Veo 3.1 - Quality'))?.label||'',duration:controls.filter(x=>['4s','6s','8s','10s'].includes(x.label)),outputs:controls.filter(x=>['1x','x2','x3','x4'].includes(x.label)),credit:lines.find(x=>/^100 credits$/.test(x))||''});})()'''
    )
    ok = (
        "Veo 3.1 - Quality" in state["model"]
        and any(x["label"] == "8s" and x["selected"] == "true" for x in state["duration"])
        and any(x["label"] == "1x" and x["selected"] == "true" for x in state["outputs"])
        and state["credit"] == "100 credits"
    )
    print(f"clip_{clip_num:02d} config", json.dumps(state, sort_keys=True), flush=True)
    if not ok:
        key_code(53)
        raise RuntimeError(f"HQ config drift for clip_{clip_num:02d}: {state}")
    check(target, f"dismiss verified HQ clip_{clip_num:02d} config")
    check(focus, f"focused Escape dismiss HQ clip_{clip_num:02d} config")
    check(desktop, f"Escape dismiss HQ clip_{clip_num:02d} config", uses_desktop=True)
    key_code(53)
    time.sleep(0.8)


def acquire_write_set(clip_num: int) -> tuple[dict[str, Any], dict[str, Any], dict[str, Any]]:
    holder = f"yui-flow-hq-clip{clip_num:02d}"
    target = acquire(
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
    try:
        desktop = acquire(holder, "desktop-control", "write", {"host_id": "studio"}, 1200, 600)
        focus = acquire(holder, "focus", "write", {"host_id": "studio"}, 1200, 600)
    except Exception:
        release(target)
        raise
    return target, desktop, focus


def paste_prompt(clip_num: int, prompt: str, target: dict[str, Any], desktop: dict[str, Any], focus: dict[str, Any]) -> None:
    probe_exact(target_lease=target)
    clipboard = acquire(
        f"yui-flow-hq-clip{clip_num:02d}",
        "clipboard",
        "write",
        {"host_id": "studio"},
        120,
        60,
    )
    try:
        check(target, f"paste HQ clip_{clip_num:02d} prompt exact a22b5b61")
        check(focus, f"AXPress HQ clip_{clip_num:02d} composer")
        check(desktop, f"paste HQ clip_{clip_num:02d} prompt", uses_desktop=True)
        check(clipboard, f"clipboard holds non-secret prompts.txt line {clip_num}")
        subprocess.run(
            ["osascript", "-", prompt],
            input="on run argv\nset the clipboard to item 1 of argv\nend run",
            text=True,
            check=True,
        )
        ax_press("AXTextArea", "true")
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
        release(clipboard)
    state = run_js(
        r'''(() => {const vis=e=>{const s=getComputedStyle(e),r=e.getBoundingClientRect();return s.display!='none'&&s.visibility!='hidden'&&r.width>0&&r.height>0};const input=[...document.querySelectorAll('[contenteditable=true]')].find(vis);const buttons=[...document.querySelectorAll('button,[role=button]')].filter(vis);return JSON.stringify({prompt:(input?(input.innerText||input.textContent||'').trim():null),active:document.activeElement===input,config:buttons.map(e=>(e.innerText||e.textContent||'').trim().replace(/\s+/g,' ')).find(x=>x.includes('Video ·'))||'',videos:document.querySelectorAll('video').length});})()'''
    )
    if state["prompt"] != prompt or state["config"] != "Video · 8s crop_16_9 1x":
        raise RuntimeError(f"prompt/config verification failed for clip_{clip_num:02d}: {state}")


def refocus_composer(prompt: str) -> None:
    ax_press("AXTextArea", "true")
    state = run_js(
        r'''(() => {const vis=e=>{const s=getComputedStyle(e),r=e.getBoundingClientRect();return s.display!='none'&&s.visibility!='hidden'&&r.width>0&&r.height>0};const input=[...document.querySelectorAll('[contenteditable=true]')].find(vis);return JSON.stringify({prompt:(input?(input.innerText||input.textContent||'').trim():null),active:document.activeElement===input});})()'''
    )
    if state["prompt"] != prompt or not state["active"]:
        raise RuntimeError(f"composer refocus failed: {state}")


def pre_submit_baseline(state: dict[str, Any], prompt: str) -> int:
    valid = (
        state["url"] == PROJECT_ROOT
        and state["prompt"] == prompt
        and state["active"]
        and state["config"] == "Video · 8s crop_16_9 1x"
    )
    if not valid:
        raise RuntimeError(f"pre-submit state verification failed: {state}")
    return int(state["videos"])


def submit_once(
    clip_num: int,
    prompt: str,
    target: dict[str, Any],
    desktop: dict[str, Any],
    focus: dict[str, Any],
) -> tuple[str, int]:
    probe_exact(target_lease=target)
    state = run_js(
        r'''(() => {const vis=e=>{const s=getComputedStyle(e),r=e.getBoundingClientRect();return s.display!='none'&&s.visibility!='hidden'&&r.width>0&&r.height>0};const input=[...document.querySelectorAll('[contenteditable=true]')].find(vis);const buttons=[...document.querySelectorAll('button,[role=button]')].filter(vis);return JSON.stringify({url:location.href,prompt:(input?(input.innerText||input.textContent||'').trim():null),active:document.activeElement===input,config:buttons.map(e=>(e.innerText||e.textContent||'').trim().replace(/\s+/g,' ')).find(x=>x.includes('Video ·'))||'',videos:document.querySelectorAll('video').length});})()'''
    )
    try:
        baseline_cards = pre_submit_baseline(state, prompt)
    except RuntimeError as exc:
        raise RuntimeError(f"pre-submit verification failed for clip_{clip_num:02d}: {state}") from exc
    heartbeat(target)
    heartbeat(desktop)
    heartbeat(focus)
    account = acquire(
        f"yui-flow-hq-clip{clip_num:02d}",
        "account-submission",
        "write",
        {"account": "google-ultra-shared"},
        120,
        60,
    )
    submit_utc = utc_now()
    try:
        check(target, f"submit HQ clip_{clip_num:02d} exact Flow project a22b5b61")
        check(focus, f"Return on focused HQ clip_{clip_num:02d} composer")
        check(desktop, f"Return submit HQ clip_{clip_num:02d} Veo Quality 8s x1", uses_desktop=True)
        check(account, f"serialized shared-account submit HQ clip_{clip_num:02d} Veo Quality x1")
        key_code(36)
        time.sleep(5)
    finally:
        release(account)
    probe_exact(target_lease=target)
    accepted = run_js(
        r'''(() => {const vis=e=>{const s=getComputedStyle(e),r=e.getBoundingClientRect();return s.display!='none'&&s.visibility!='hidden'&&r.width>0&&r.height>0};const input=[...document.querySelectorAll('[contenteditable=true]')].find(vis);const lines=(document.body.innerText||'').split('\n').map(x=>x.trim()).filter(Boolean);return JSON.stringify({input:(input?(input.innerText||input.textContent||'').trim():null),videos:document.querySelectorAll('video').length,failed:[...document.querySelectorAll('*')].filter(e=>vis(e)&&e.children.length===0&&(e.innerText||e.textContent||'').trim()==='Failed').length,prompt_visible:lines.includes(''' + json.dumps(prompt) + r''')});})()'''
    )
    print(f"clip_{clip_num:02d} accepted", json.dumps(accepted, sort_keys=True), flush=True)
    if accepted["input"] != "What do you want to create?" or not accepted["prompt_visible"]:
        raise RuntimeError(f"submit acceptance not proven for clip_{clip_num:02d}: {accepted}")
    return submit_utc, baseline_cards


def acquire_read_poll(clip_num: int) -> dict[str, Any]:
    return acquire(
        f"yui-flow-hq-clip{clip_num:02d}-poll",
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


def poll_settlement(clip_num: int, prompt: str, baseline_cards: int) -> dict[str, Any]:
    lease = acquire_read_poll(clip_num)
    start = time.monotonic()
    lease_start = start
    stable = 0
    try:
        for attempt in range(1, 91):
            probe_exact(target_lease=lease)
            state = run_js(
                r'''(() => {const vis=e=>{const s=getComputedStyle(e),r=e.getBoundingClientRect();return s.display!='none'&&s.visibility!='hidden'&&r.width>0&&r.height>0};const lines=(document.body.innerText||'').split('\n').map(x=>x.trim()).filter(Boolean);return JSON.stringify({url:location.href,videos:document.querySelectorAll('video').length,failed:[...document.querySelectorAll('*')].filter(e=>vis(e)&&e.children.length===0&&(e.innerText||e.textContent||'').trim()==='Failed').length,prompt_visible:lines.includes(''' + json.dumps(prompt) + r'''),status:lines.filter(x=>/Generating|Creating|Queued|Pending|Failed/.test(x)).slice(-20)});})()'''
            )
            elapsed = round(time.monotonic() - start, 1)
            print(
                f"clip_{clip_num:02d} poll",
                json.dumps({"attempt": attempt, "elapsed_s": elapsed, **state}, sort_keys=True),
                flush=True,
            )
            complete_candidate = state["videos"] >= baseline_cards + 1 and state["failed"] == 0 and not state["prompt_visible"]
            stable = stable + 1 if complete_candidate else 0
            if stable >= 2:
                return {"elapsed_s": elapsed, "root_video_count": state["videos"]}
            if time.monotonic() - lease_start >= 240:
                release(lease)
                lease = acquire_read_poll(clip_num)
                lease_start = time.monotonic()
            time.sleep(10)
    finally:
        release(lease)
    raise RuntimeError(f"settlement timeout for clip_{clip_num:02d}")


def inspect_newest_detail(clip_num: int, prompt: str, root_count: int) -> dict[str, Any]:
    lease = acquire_read_poll(clip_num)
    matched: dict[str, Any] | None = None
    try:
        ensure_root(lease)
        for idx in range(root_count):
            probe_exact(target_lease=lease)
            check(lease, f"read-only inspect settled HQ clip_{clip_num:02d} candidate card {idx + 1}")
            clicked = run_js(
                f'''(() => {{const cards=[...document.querySelectorAll('video')].map(v=>v.closest('button,[role=button]')).filter((e,i,a)=>e&&a.indexOf(e)===i);if(!cards[{idx}])return JSON.stringify({{clicked:false,count:cards.length}});cards[{idx}].click();return JSON.stringify({{clicked:true,count:cards.length}});}})()'''
            )
            if not clicked["clicked"]:
                raise RuntimeError(f"could not open result card {idx + 1}: {clicked}")
            time.sleep(2)
            probe_exact(target_lease=lease)
            detail: dict[str, Any] | None = None
            for _ in range(15):
                detail = run_js(
                    r'''(() => {const lines=(document.body.innerText||'').split('\n').map(x=>x.trim()).filter(Boolean);const v=[...document.querySelectorAll('video')][0];return JSON.stringify({url:location.href,prompts:lines.filter(x=>x.length>70&&!x.includes('Google Flow - AI Creative Studio')),video:v?{readyState:v.readyState,duration:Number.isFinite(v.duration)?v.duration:null,width:v.videoWidth,height:v.videoHeight}:null,failed:lines.includes('Failed')});})()'''
                )
                video_detail = detail.get("video") if detail else None
                if video_detail and video_detail["readyState"] >= 2 and video_detail["duration"] is not None:
                    break
                time.sleep(2)
            if detail and prompt in detail["prompts"]:
                media_id = detail["url"].rstrip("/").split("/")[-1]
                matched = {"media_id": media_id, **detail}
                break
            run_js_raw("history.back(); 'BACK'")
            time.sleep(2)
            ensure_root(lease)
        if not matched:
            raise RuntimeError(f"no settled result matched prompt for clip_{clip_num:02d}")
        video = matched["video"]
        if matched["failed"] or not video or video["readyState"] < 2 or not (7.0 <= video["duration"] <= 10.5) or video["width"] < 1280 or video["height"] < 720:
            raise RuntimeError(f"non-playable or wrong-spec result for clip_{clip_num:02d}: {matched}")
        return matched
    finally:
        release(lease)


def download_current_detail(clip_num: int, media_id: str) -> Path:
    out = OUTPUT_DIR / f"clip_{clip_num:02d}_hq.mp4"
    if out.exists():
        raise RuntimeError(f"refusing to overwrite {out}")
    target = acquire(
        f"yui-flow-hq-clip{clip_num:02d}-save",
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
        probe = probe_exact(target_lease=target)
        if not probe["url"].endswith("/" + media_id):
            emergency_freeze(f"download detail target mismatch for clip_{clip_num:02d}", target)
        check(target, f"invoke visible Flow Download for settled HQ clip_{clip_num:02d}")
        click = run_js(
            r'''(() => {const b=[...document.querySelectorAll('button,[role=button]')].find(e=>{const t=(e.getAttribute('aria-label')||e.getAttribute('title')||e.innerText||e.textContent||'').trim().replace(/\s+/g,' ');return t==='download Download'||t==='Download'||t.endsWith(' Download')});if(!b)return JSON.stringify({clicked:false});b.click();return JSON.stringify({clicked:true});})()'''
        )
        if not click["clicked"]:
            raise RuntimeError(f"Flow Download control not found for clip_{clip_num:02d}")
        started = time.time()
        candidates: list[Path] = []
        for _ in range(180):
            partials = [p for p in downloads.iterdir() if p.is_file() and p.suffix == ".crdownload"]
            candidates = []
            for p in downloads.iterdir():
                if not p.is_file() or p.suffix == ".crdownload":
                    continue
                stat = p.stat()
                old = before.get(p.name)
                if old is not None and old == (stat.st_mtime_ns, stat.st_size):
                    continue
                if stat.st_mtime < started - 2 or stat.st_size <= 0:
                    continue
                info = ffprobe(p, allow_failure=True)
                if info and 7.0 <= info["duration"] <= 10.5 and info["width"] >= 1280 and info["height"] >= 720:
                    candidates.append(p)
            if len(candidates) == 1 and not partials:
                break
            if len(candidates) > 1:
                raise RuntimeError(f"ambiguous concurrent downloads for clip_{clip_num:02d}: {[p.name for p in candidates]}")
            time.sleep(1)
        if len(candidates) != 1:
            raise RuntimeError(f"no completed Flow download detected for clip_{clip_num:02d}")
        shutil.move(str(candidates[0]), str(out))
        run_js_raw("history.back(); 'BACK'")
        time.sleep(1.5)
        return out
    finally:
        release(target)


def ffprobe(path: Path, allow_failure: bool = False) -> dict[str, Any] | None:
    result = subprocess.run(
        [
            "ffprobe",
            "-v",
            "error",
            "-show_entries",
            "format=duration,size:stream=codec_type,codec_name,width,height,r_frame_rate",
            "-of",
            "json",
            str(path),
        ],
        text=True,
        capture_output=True,
    )
    if result.returncode != 0:
        if allow_failure:
            return None
        raise RuntimeError(f"ffprobe failed for {path}: {result.stderr}")
    data = json.loads(result.stdout)
    video = next((s for s in data.get("streams", []) if s.get("codec_type") == "video"), {})
    audio = next((s for s in data.get("streams", []) if s.get("codec_type") == "audio"), {})
    return {
        "duration": float(data["format"]["duration"]),
        "size": int(data["format"]["size"]),
        "video_codec": video.get("codec_name"),
        "audio_codec": audio.get("codec_name"),
        "width": int(video.get("width", 0)),
        "height": int(video.get("height", 0)),
        "fps": video.get("r_frame_rate"),
    }


def write_manifest(manifest: dict[str, Any]) -> None:
    MANIFEST_PATH.parent.mkdir(parents=True, exist_ok=True)
    tmp = MANIFEST_PATH.with_suffix(".json.tmp")
    tmp.write_text(json.dumps(manifest, indent=2, sort_keys=True) + "\n")
    os.replace(tmp, MANIFEST_PATH)


def journal_clip(entry: dict[str, Any]) -> None:
    note = (
        f"HQ clip_{entry['clip_num']:02d} settled and saved. Veo 3.1 Quality, x1, 8s. "
        f"media={entry['media_id']} artifact={Path(entry['path']).name} "
        f"duration={entry['media']['duration']:.3f}s size={entry['media']['size']} "
        f"sha256={entry['sha256']}. No retry; prompt exact; page challenge false."
    )
    subprocess.run(
        [
            "python3",
            str(JOURNAL),
            str(LEDGER),
            "yui",
            "flow_hq_clip_saved",
            note,
            str(MANIFEST_PATH),
            entry["path"],
        ],
        cwd=PACKET,
        check=True,
    )
    subprocess.run(["python3", str(PACKET / "broker" / "ledger.py"), str(LEDGER), "verify"], cwd=PACKET, check=True)


def process_clip(clip_num: int, manifest: dict[str, Any]) -> dict[str, Any]:
    prompt = PROMPTS[clip_num - 1]
    out = OUTPUT_DIR / f"clip_{clip_num:02d}_hq.mp4"
    if out.exists():
        raise RuntimeError(f"refusing to overwrite existing HQ artifact: {out}")
    target = desktop = focus = None
    submit_utc = ""
    try:
        target, desktop, focus = acquire_write_set(clip_num)
        ensure_root(target)
        verify_full_config(target, desktop, focus, clip_num)
        paste_prompt(clip_num, prompt, target, desktop, focus)
        verify_full_config(target, desktop, focus, clip_num)
        refocus_composer(prompt)
        submit_utc, baseline_cards = submit_once(clip_num, prompt, target, desktop, focus)
    finally:
        release(focus)
        release(desktop)
        release(target)
    settled = poll_settlement(clip_num, prompt, baseline_cards)
    detail = inspect_newest_detail(clip_num, prompt, settled["root_video_count"])
    artifact = download_current_detail(clip_num, detail["media_id"])
    media = ffprobe(artifact)
    assert media is not None
    if not (7.0 <= media["duration"] <= 10.5 and media["width"] >= 1280 and media["height"] >= 720):
        raise RuntimeError(f"saved media verification failed for clip_{clip_num:02d}: {media}")
    entry = {
        "clip_num": clip_num,
        "prompt": prompt,
        "prompt_sha256": hashlib.sha256(prompt.encode()).hexdigest(),
        "submit_utc": submit_utc,
        "settled_utc": utc_now(),
        "settlement_elapsed_s": settled["elapsed_s"],
        "media_id": detail["media_id"],
        "path": str(artifact),
        "sha256": sha256_file(artifact),
        "media": media,
        "model": "Veo 3.1 - Quality",
        "output_count": "1x",
        "duration_setting": "8s",
        "aspect_ratio": "16:9",
        "displayed_cost_credits": 100,
        "status": "settled_playable_saved",
    }
    manifest["clips"].append(entry)
    manifest["updated_utc"] = utc_now()
    write_manifest(manifest)
    journal_clip(entry)
    print("CLIP_COMPLETE", json.dumps(entry, sort_keys=True), flush=True)
    return entry


def journal_stop(manifest: dict[str, Any], error: str) -> None:
    manifest["status"] = "stopped"
    manifest["error"] = error
    manifest["updated_utc"] = utc_now()
    write_manifest(manifest)
    subprocess.run(
        [
            "python3",
            str(JOURNAL),
            str(LEDGER),
            "yui",
            "flow_hq_batch_STOP",
            f"HQ batch stopped fail-closed after {len(manifest['clips'])} saved batch clips: {error}. No automatic job retry.",
            str(MANIFEST_PATH),
        ],
        cwd=PACKET,
        check=False,
    )
    subprocess.run(["python3", str(PACKET / "broker" / "ledger.py"), str(LEDGER), "verify"], cwd=PACKET, check=False)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--start", type=int, default=2)
    parser.add_argument("--end", type=int, default=13)
    parser.add_argument("--dry-run", action="store_true")
    args = parser.parse_args()
    if not (2 <= args.start <= args.end <= 13):
        parser.error("range must be within clips 02-13")
    missing = [i for i in range(args.start, args.end + 1) if (OUTPUT_DIR / f"clip_{i:02d}_hq.mp4").exists()]
    if missing:
        raise RuntimeError(f"refusing to overwrite existing HQ clips: {missing}")
    probe = probe_exact(allow_detail=True)
    state = json.loads((PACKET / "broker" / "live_state.json").read_text())
    if state["frozen"]:
        raise RuntimeError("broker is frozen")
    print(
        json.dumps(
            {
                "dry_run": args.dry_run,
                "range": [args.start, args.end],
                "project": PROJECT_ID,
                "current_url": probe["url"],
                "challenge": probe["challenge"],
                "prompts_sha256": sha256_file(PROMPTS_PATH),
                "targets_absent": not missing,
            },
            sort_keys=True,
        )
    )
    if args.dry_run:
        return 0
    now = utc_now()
    prior_manifest: dict[str, Any] = {}
    preserved_clips: list[dict[str, Any]] = []
    if MANIFEST_PATH.exists():
        prior_manifest = json.loads(MANIFEST_PATH.read_text())
        for entry in prior_manifest.get("clips", []):
            clip_num = int(entry["clip_num"])
            if clip_num >= args.start:
                continue
            artifact = Path(entry["path"])
            if not artifact.exists() or sha256_file(artifact) != entry["sha256"]:
                raise RuntimeError(f"cannot preserve unverified prior clip_{clip_num:02d} manifest entry")
            preserved_clips.append(entry)
    manifest: dict[str, Any] = {
        "status": "running",
        "started_utc": prior_manifest.get("started_utc", now),
        "updated_utc": now,
        "project_id": PROJECT_ID,
        "prompts_path": str(PROMPTS_PATH),
        "prompts_sha256": sha256_file(PROMPTS_PATH),
        "model": "Veo 3.1 - Quality",
        "output_count": "1x",
        "duration_setting": "8s",
        "aspect_ratio": "16:9",
        "displayed_cost_per_clip": 100,
        "clips": sorted(preserved_clips, key=lambda entry: int(entry["clip_num"])),
        "range_runs": prior_manifest.get("range_runs", [])
        + [{"start": args.start, "end": args.end, "started_utc": now}],
    }
    write_manifest(manifest)
    try:
        for clip_num in range(args.start, args.end + 1):
            process_clip(clip_num, manifest)
    except Exception as exc:
        journal_stop(manifest, repr(exc))
        raise
    completed_numbers = sorted(int(entry["clip_num"]) for entry in manifest["clips"])
    full_batch_complete = completed_numbers == list(range(2, 14))
    manifest["status"] = "completed" if full_batch_complete else "range_completed"
    manifest["completed_utc"] = utc_now()
    manifest["updated_utc"] = utc_now()
    write_manifest(manifest)
    subprocess.run(
        [
            "python3",
            str(JOURNAL),
            str(LEDGER),
            "yui",
            "flow_hq_batch_02_13_complete" if full_batch_complete else "flow_hq_range_complete",
            (
                "HQ clips 02-13 completed sequentially under serialized account leases; each settled playable and saved without overwriting originals."
                if full_batch_complete
                else f"HQ range {args.start:02d}-{args.end:02d} completed; full 02-13 batch remains in progress."
            ),
            str(MANIFEST_PATH),
        ],
        cwd=PACKET,
        check=True,
    )
    subprocess.run(["python3", str(PACKET / "broker" / "ledger.py"), str(LEDGER), "verify"], cwd=PACKET, check=True)
    print("BATCH_COMPLETE", json.dumps(manifest, sort_keys=True), flush=True)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
