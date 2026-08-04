#!/usr/bin/env python3
from __future__ import annotations

import argparse
import hashlib
import importlib.util
import json
import os
import subprocess
import time
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

from PIL import Image

PACKET = Path(__file__).resolve().parents[1]
OUTPUT_DIR = Path("/Users/duhokim/HermesOps/scripts/clips/method1_pgr")
STATE = OUTPUT_DIR / "PGR_FLOW_LANE_STATE.json"
ROOT = "https://labs.google/fx/tools/flow/project/a22b5b61-833d-4e62-857b-4a7030b93bfa"
SUMMARY = "🍌 Nano Banana Pro crop_16_9 1x"
HELPER = Path("/tmp/axpress_exact_role")


def load_module(name: str, path: Path):
    spec = importlib.util.spec_from_file_location(name, path)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"cannot load {path}")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


B = load_module("pgr_slide_base", Path(__file__).with_name("yui_flow_method1_narration.py"))
M = B.M
H = M.H

SLIDES: dict[int, dict[str, str]] = {
    2: {
        "title": "THE PACKET",
        "caption": "one real paper · the exact evidence · a trust score",
        "visual": "A single glowing rounded packet card centered in the frame, visibly bundling three crisp icons: a blank research-paper document represented only by horizontal lines with no letters or numbers, a magnifying glass over a data chip, and a circular trust gauge. Soft light rays bind the three into one bundle.",
    },
    3: {
        "title": "THE GATE",
        "caption": "no packet, no claim",
        "visual": "A clear left-to-right checkpoint pipeline made only from simple geometric icons: a completely blank solid claim card approaches an upright evidence gate, the gate compares it with a completely blank layered packet rectangle, and a restrained green check marks the permitted path. The cards contain no internal marks at all: no lines, scribbles, signatures, letters, or numbers.",
    },
    4: {
        "title": "VISIBLE CAUTIONS",
        "caption": "verified ✓ vs. unconfirmed ⚠ / no-go",
        "visual": "A clean icon-only claim-status panel with blank rows marked by solid green checks, amber warning triangles, and one restrained no-entry symbol. Keep the hierarchy simple and unmistakable; the rows contain no labels, letters, or numbers.",
    },
    5: {
        "title": "TRUST + DEBATE",
        "caption": "every claim scored & cited · contested = live debate",
        "visual": "Two balanced elements side by side: a blank claim card with a cyan trust-score meter and icon-only citation-link chips; beside it, two opposing amber arrows around a balanced scale to signify an open scientific debate. Put no letters or numbers inside the card or chips.",
    },
}

STYLE = (
    "Clean modern flat-vector infographic slide. Deep navy (#0b1220) background with a subtle faint spiral-galaxy texture in one corner, "
    "soft cyan (#5fd0e0) and warm amber (#f0b45f) accent glow. Iconographic, minimal, crisp, high clarity, generous spacing, 16:9 widescreen."
)


def utc_now() -> str:
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def sha256_text(value: str) -> str:
    return hashlib.sha256(value.encode()).hexdigest()


def sha256_file(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as fh:
        for chunk in iter(lambda: fh.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()


def prompt_for(beat: int) -> str:
    row = SLIDES[beat]
    return (
        f"Create one polished infographic slide. {STYLE} {row['visual']} "
        f"Render exactly two text lines: the first line must read \"{row['title']}\" and the second line must read \"{row['caption']}\". "
        "The quotation marks are instructions and must not appear in the image. Make the first line large and the second line smaller but fully legible. "
        "Copy every character exactly, including punctuation and symbols. Do not paraphrase, respell, translate, omit, or add words. "
        "No other lettering, labels, numbers, logos, watermarks, or decorative pseudo-text anywhere in the image."
    )


def native_press(pid: int, role: str, label: str, attempts: int = 12) -> str:
    last = ""
    for _ in range(attempts):
        result = subprocess.run(
            [str(HELPER), str(pid), role, label],
            text=True,
            capture_output=True,
            timeout=20,
            check=False,
        )
        last = (result.stdout + result.stderr).strip()
        if "matches=1" in last:
            return last
        time.sleep(0.5)
    raise RuntimeError(f"native AXPress failed role={role} label={label!r}: {last}")


def config_state() -> dict[str, Any]:
    return H.run_js(
        r'''(() => {const vis=e=>{const s=getComputedStyle(e),r=e.getBoundingClientRect();return s.display!='none'&&s.visibility!='hidden'&&r.width>0&&r.height>0};const clean=s=>(s||'').trim().replace(/\s+/g,' ');const controls=[...document.querySelectorAll('button,[role=button],[role=tab]')].filter(vis).map(e=>({label:clean(e.innerText||e.textContent),selected:e.getAttribute('aria-selected')}));const lines=(document.body.innerText||'').split('\n').map(clean).filter(Boolean);return JSON.stringify({url:location.href,summary:controls.find(x=>x.label.includes('Nano Banana Pro')&&x.label.includes('crop_'))?.label||'',model:controls.find(x=>x.label.includes('Nano Banana Pro')&&x.label.includes('arrow_drop_down'))?.label||'',image:controls.find(x=>x.label==='image Image')||null,video:controls.find(x=>x.label==='play_circle Video')||null,aspects:controls.filter(x=>['crop_16_9 16:9','crop_landscape 4:3','crop_square 1:1','crop_portrait 3:4','crop_9_16 9:16'].includes(x.label)),outputs:controls.filter(x=>['1x','x2','x3','x4'].includes(x.label)),credit:lines.find(x=>/^Generating will use \d+ credits$/.test(x))||lines.find(x=>/^\d+ credits$/.test(x))||'',sorry:location.href.includes('google.com/sorry'),challenge:/verify you are human|unusual traffic|captcha/i.test(document.body.innerText||'')});})()'''
    )


def verify_config(beat: int, attempt: int, target: dict[str, Any], desktop: dict[str, Any], focus: dict[str, Any]) -> dict[str, Any]:
    H.probe_exact(target_lease=target)
    for lease, action, uses_desktop in (
        (target, f"verify Nano Banana Pro config slide_b{beat} attempt {attempt}", False),
        (focus, f"focus Nano Banana Pro config slide_b{beat} attempt {attempt}", False),
        (desktop, f"native AXPress Nano Banana Pro config slide_b{beat} attempt {attempt}", True),
    ):
        H.check(lease, action, uses_desktop=uses_desktop)
    pid = int(subprocess.check_output(["pgrep", "-x", "Google Chrome"], text=True).splitlines()[0])
    try:
        native_press(pid, "AXPopUpButton", SUMMARY)
    except RuntimeError:
        H.check(target, f"one bounded exact-root reload for slide_b{beat} settings AX remount")
        H.check(focus, f"focus exact Flow root during slide_b{beat} AX remount reload")
        H.check(desktop, f"reload exact Flow root for slide_b{beat} AX remount", uses_desktop=True)
        subprocess.run(["osascript", "-e", 'tell application "Google Chrome" to reload active tab of window 1'], check=True)
        last: dict[str, Any] = {}
        for _ in range(12):
            time.sleep(0.75)
            H.probe_exact(target_lease=target)
            last = H.run_js(
                r'''(() => {const vis=e=>{const s=getComputedStyle(e),r=e.getBoundingClientRect();return s.display!='none'&&s.visibility!='hidden'&&r.width>0&&r.height>0};const clean=s=>(s||'').trim().replace(/\s+/g,' ');const bs=[...document.querySelectorAll('button,[role=button]')].filter(vis);const input=[...document.querySelectorAll('[contenteditable=true]')].find(vis);return JSON.stringify({summary:bs.map(e=>clean(e.innerText||e.textContent)).find(x=>x.includes('Nano Banana Pro')&&x.includes('crop_'))||'',prompt:input?(input.innerText||input.textContent||'').trim():null,sorry:location.href.includes('google.com/sorry'),challenge:/verify you are human|unusual traffic|captcha/i.test(document.body.innerText||'')});})()'''
            )
            if last["sorry"] or last["challenge"]:
                raise RuntimeError(f"slide_b{beat} hard challenge STOP during AX remount reload: {last}")
            if last["summary"] == SUMMARY and last["prompt"] is not None:
                break
        else:
            raise RuntimeError(f"slide_b{beat} Flow root did not remount after one reload: {last}")
        native_press(pid, "AXPopUpButton", SUMMARY)
    time.sleep(0.8)
    state = config_state()
    ok = (
        state["url"] == ROOT
        and state["summary"] == SUMMARY
        and "Nano Banana Pro" in state["model"]
        and state["image"] and state["image"]["selected"] == "true"
        and state["video"] and state["video"]["selected"] == "false"
        and any(x["label"] == "crop_16_9 16:9" and x["selected"] == "true" for x in state["aspects"])
        and any(x["label"] == "1x" and x["selected"] == "true" for x in state["outputs"])
        and state["credit"] == "0 credits"
        and not state["sorry"]
        and not state["challenge"]
    )
    if not ok:
        raise RuntimeError(f"slide_b{beat} Nano Banana Pro config drift: {state}")
    native_press(pid, "AXPopUpButton", SUMMARY)
    time.sleep(0.5)
    print(f"slide_b{beat} attempt {attempt} config", json.dumps(state, sort_keys=True), flush=True)
    return state


def paste_prompt(beat: int, attempt: int, prompt: str, target: dict[str, Any], desktop: dict[str, Any], focus: dict[str, Any]) -> None:
    H.probe_exact(target_lease=target)
    holder = f"yui-flow-pgr-slide-b{beat}-attempt{attempt}"
    clipboard = M.wait_acquire(holder, "clipboard", "write", {"host_id": "studio"}, 120, 60, keepalive=(target, desktop, focus))
    try:
        H.check(target, f"paste exact slide_b{beat} attempt {attempt} prompt")
        H.check(focus, f"focus exact slide_b{beat} attempt {attempt} composer")
        H.check(desktop, f"trusted paste slide_b{beat} attempt {attempt} prompt", uses_desktop=True)
        H.check(clipboard, f"clipboard holds non-secret slide_b{beat} prompt")
        subprocess.run(
            ["osascript", "-", prompt],
            input="on run argv\nset the clipboard to item 1 of argv\nend run",
            text=True,
            check=True,
        )
        pid = int(subprocess.check_output(["pgrep", "-x", "Google Chrome"], text=True).splitlines()[0])
        current_prompt = H.run_js(
            r'''(() => {const vis=e=>{const s=getComputedStyle(e),r=e.getBoundingClientRect();return s.display!='none'&&s.visibility!='hidden'&&r.width>0&&r.height>0};const input=[...document.querySelectorAll('[contenteditable=true]')].find(vis);return JSON.stringify(input?(input.innerText||input.textContent||'').trim():null);})()'''
        )
        if not current_prompt:
            current_prompt = "What do you want to create?"
        try:
            native_press(pid, "AXTextArea", current_prompt, attempts=2)
        except RuntimeError:
            H.ax_press("AXTextArea", "true", before_attempt=lambda: H.probe_exact(target_lease=target))
        subprocess.run(
            ["osascript", "-e", 'tell application "System Events" to keystroke "a" using {command down}', "-e", "delay 0.3", "-e", 'tell application "System Events" to keystroke "v" using {command down}'],
            check=True,
        )
        time.sleep(1.5)
    finally:
        M.safe_release(clipboard)
    state = H.run_js(
        r'''(() => {const vis=e=>{const s=getComputedStyle(e),r=e.getBoundingClientRect();return s.display!='none'&&s.visibility!='hidden'&&r.width>0&&r.height>0};const clean=s=>(s||'').trim().replace(/\s+/g,' ');const input=[...document.querySelectorAll('[contenteditable=true]')].find(vis);const bs=[...document.querySelectorAll('button,[role=button]')].filter(vis);const create=bs.find(e=>clean(e.innerText||e.textContent).includes('arrow_forward')&&clean(e.innerText||e.textContent).includes('Create'));return JSON.stringify({url:location.href,prompt:input?(input.innerText||input.textContent||'').trim():null,active:document.activeElement===input,summary:bs.map(e=>clean(e.innerText||e.textContent)).find(x=>x.includes('Nano Banana Pro')&&x.includes('crop_'))||'',disabled:create?create.disabled:null,aria:create?create.getAttribute('aria-disabled'):null,sorry:location.href.includes('google.com/sorry'),challenge:/verify you are human|unusual traffic|captcha/i.test(document.body.innerText||'')});})()'''
    )
    if not (state["url"] == ROOT and state["prompt"] == prompt and state["active"] and state["summary"] == SUMMARY and state["disabled"] is not True and state["aria"] != "true" and not state["sorry"] and not state["challenge"]):
        raise RuntimeError(f"slide_b{beat} prompt readiness failed: {state}")


def prompt_card_urls(prompt: str) -> list[str]:
    return H.run_js(
        r'''(() => {const target=''' + json.dumps(prompt) + r''';const leaves=[...document.querySelectorAll('*')].filter(e=>e.children.length===0&&(e.innerText||e.textContent||'').trim()===target);return JSON.stringify([...new Set(leaves.map(e=>e.closest('a[href]')?.href).filter(Boolean))]);})()'''
    )


def all_detail_urls() -> list[str]:
    return H.run_js(
        r'''(() => JSON.stringify([...new Set([...document.querySelectorAll('a[href*="/edit/"]')].map(a=>a.href))]))()'''
    )


def submit_once(beat: int, attempt: int, prompt: str, target: dict[str, Any], desktop: dict[str, Any], focus: dict[str, Any]) -> tuple[str, str, str]:
    pid = int(subprocess.check_output(["pgrep", "-x", "Google Chrome"], text=True).splitlines()[0])
    try:
        native_press(pid, "AXTextArea", prompt, attempts=2)
    except RuntimeError:
        H.ax_press("AXTextArea", "true", before_attempt=lambda: H.probe_exact(target_lease=target))
    H.probe_exact(target_lease=target)
    pre = H.run_js(
        r'''(() => {const vis=e=>{const s=getComputedStyle(e),r=e.getBoundingClientRect();return s.display!='none'&&s.visibility!='hidden'&&r.width>0&&r.height>0};const clean=s=>(s||'').trim().replace(/\s+/g,' ');const input=[...document.querySelectorAll('[contenteditable=true]')].find(vis);const bs=[...document.querySelectorAll('button,[role=button]')].filter(vis);const create=bs.find(e=>clean(e.innerText||e.textContent).includes('arrow_forward')&&clean(e.innerText||e.textContent).includes('Create'));return JSON.stringify({url:location.href,prompt:input?(input.innerText||input.textContent||'').trim():null,active:document.activeElement===input,summary:bs.map(e=>clean(e.innerText||e.textContent)).find(x=>x.includes('Nano Banana Pro')&&x.includes('crop_'))||'',disabled:create?create.disabled:null,aria:create?create.getAttribute('aria-disabled'):null,layers:[...document.querySelectorAll('[role=dialog],[aria-modal=true],[role=alertdialog]')].filter(vis).map(e=>clean(e.innerText||e.textContent).slice(0,500)),sorry:location.href.includes('google.com/sorry'),challenge:/verify you are human|unusual traffic|captcha/i.test(document.body.innerText||'')});})()'''
    )
    baseline = set(all_detail_urls())
    if not (pre["url"] == ROOT and pre["prompt"] == prompt and pre["active"] and pre["summary"] == SUMMARY and pre["disabled"] is not True and pre["aria"] != "true" and not pre["layers"] and not pre["sorry"] and not pre["challenge"]):
        raise RuntimeError(f"slide_b{beat} final pre-submit failed: {pre}")
    for lease in (target, desktop, focus):
        H.heartbeat(lease)
    account = M.wait_acquire(
        f"yui-flow-pgr-slide-b{beat}-attempt{attempt}",
        "account-submission",
        "write",
        {"account": "google-ultra-shared"},
        120,
        60,
        keepalive=(target, desktop, focus),
    )
    submit_utc = utc_now()
    try:
        H.probe_exact(target_lease=target)
        H.check(target, f"submit exactly one Nano Banana Pro slide_b{beat} attempt {attempt}")
        H.check(focus, f"trusted Return submit slide_b{beat} attempt {attempt}")
        H.check(desktop, f"trusted Return submit slide_b{beat} Nano Banana Pro x1", uses_desktop=True)
        H.check(account, f"serialized shared-account submit slide_b{beat} Nano Banana Pro x1")
        H.key_code(36)
        time.sleep(5)
    finally:
        M.safe_release(account)
    last: dict[str, Any] = {}
    new_urls: list[str] = []
    for _ in range(20):
        H.probe_exact(target_lease=target)
        current = all_detail_urls()
        new_urls = [url for url in current if url not in baseline]
        last = H.run_js(
            r'''(() => {const vis=e=>{const s=getComputedStyle(e),r=e.getBoundingClientRect();return s.display!='none'&&s.visibility!='hidden'&&r.width>0&&r.height>0};const input=[...document.querySelectorAll('[contenteditable=true]')].find(vis);return JSON.stringify({input:input?(input.innerText||input.textContent||'').trim():null,sorry:location.href.includes('google.com/sorry'),challenge:/verify you are human|unusual traffic|captcha/i.test(document.body.innerText||'')});})()'''
        )
        if last["sorry"] or last["challenge"]:
            raise RuntimeError(f"slide_b{beat} hard challenge STOP: {last}")
        if last["input"] == "What do you want to create?" and len(new_urls) == 1:
            break
        time.sleep(1)
    else:
        raise RuntimeError(f"slide_b{beat} submit acceptance unresolved: ui={last} new_urls={new_urls}")
    print(f"slide_b{beat} acceptance", json.dumps({"account_lease_id": account["lease_id"], "detail_url": new_urls[0], "submit_utc": submit_utc}, sort_keys=True), flush=True)
    return submit_utc, account["lease_id"], new_urls[0]


def poll_card(beat: int, attempt: int, prompt: str, detail_url: str) -> dict[str, Any]:
    target = M.wait_acquire(
        f"yui-flow-pgr-slide-b{beat}-attempt{attempt}-poll",
        "target",
        "read",
        {"host_id": "studio", "bundle": "com.google.Chrome", "user_data_dir": "default-google-chrome-profile", "window_id": "1", "target_id": "flow-project-a22b5b61"},
        1800,
        600,
    )
    started = time.monotonic()
    stable = 0
    failed = 0
    last: dict[str, Any] = {}
    try:
        for poll in range(1, 91):
            H.probe_exact(target_lease=target)
            last = H.run_js(
                r'''(() => {const url=''' + json.dumps(detail_url) + r''';const target=''' + json.dumps(prompt) + r''';const a=[...document.querySelectorAll('a[href]')].find(e=>e.href===url);let node=a;const ancestors=[];for(let i=0;i<7&&node;i++,node=node.parentElement)ancestors.push(node);const imgs=ancestors.flatMap(e=>[...e.querySelectorAll('img')]).filter(i=>i.alt==='Generated image');const lines=ancestors.flatMap(e=>(e.innerText||e.textContent||'').split('\n')).map(x=>x.trim()).filter(Boolean);return JSON.stringify({found:!!a,prompt:lines.includes(target),failed:lines.includes('Failed'),queued:lines.includes('Queued'),image:imgs.map(i=>({width:i.naturalWidth,height:i.naturalHeight,complete:i.complete})).sort((x,y)=>y.width-x.width)[0]||null,sorry:location.href.includes('google.com/sorry'),challenge:/verify you are human|unusual traffic|captcha/i.test(document.body.innerText||'')});})()'''
            )
            if last["sorry"] or last["challenge"]:
                raise RuntimeError(f"slide_b{beat} hard challenge STOP while polling: {last}")
            good = bool(last["found"] and last["image"] and last["image"]["complete"] and last["image"]["width"] >= 1024 and last["image"]["height"] >= 576 and not last["failed"])
            stable = stable + 1 if good else 0
            failed = failed + 1 if last["found"] and last["failed"] else 0
            print(f"slide_b{beat} attempt {attempt} poll", json.dumps({"poll": poll, "elapsed_s": round(time.monotonic()-started, 1), "state": last}, sort_keys=True), flush=True)
            if stable >= 2:
                last["settlement_elapsed_s"] = round(time.monotonic() - started, 1)
                return last
            if failed >= 18:
                raise RuntimeError(f"slide_b{beat} terminal Failed after bounded settlement: {last}")
            time.sleep(10)
    finally:
        M.safe_release(target)
    raise RuntimeError(f"slide_b{beat} settlement timeout: {last}")


def navigate_detail(beat: int, attempt: int, detail_url: str, prompt: str) -> dict[str, Any]:
    target = desktop = focus = None
    try:
        target, desktop, focus = M.acquire_write_set(300 + beat, attempt)
        for lease, action, uses_desktop in (
            (target, f"navigate exact slide_b{beat} detail", False),
            (focus, f"focus exact slide_b{beat} detail", False),
            (desktop, f"navigate exact slide_b{beat} detail", True),
        ):
            H.check(lease, action, uses_desktop=uses_desktop)
        script = f'tell application "Google Chrome" to set URL of tab 1 of window 1 to {json.dumps(detail_url)}'
        subprocess.run(["osascript", "-e", script], check=True)
        last: dict[str, Any] = {}
        for _ in range(30):
            time.sleep(0.5)
            last = H.run_js(
                r'''(() => {const target=''' + json.dumps(prompt) + r''';const vis=e=>{const s=getComputedStyle(e),r=e.getBoundingClientRect();return s.display!='none'&&s.visibility!='hidden'&&r.width>0&&r.height>0};const clean=s=>(s||'').trim();const text=document.body.innerText||'';const img=[...document.images].filter(i=>i.alt==='Generated image'&&vis(i)).sort((a,b)=>b.naturalWidth-a.naturalWidth)[0];return JSON.stringify({url:location.href,prompt_match:text.includes(target),image:img?{width:img.naturalWidth,height:img.naturalHeight,complete:img.complete}:null,download:[...document.querySelectorAll('button,[role=button]')].filter(vis).map(e=>(e.innerText||e.textContent||'').trim().replace(/\s+/g,' ')).filter(x=>x.includes('download')&&x.includes('Download')),sorry:location.href.includes('google.com/sorry'),challenge:/verify you are human|unusual traffic|captcha/i.test(text)});})()'''
            )
            if last["sorry"] or last["challenge"]:
                raise RuntimeError(f"slide_b{beat} hard challenge STOP on detail: {last}")
            if last["url"] == detail_url and last["prompt_match"] and last["image"] and last["image"]["width"] >= 1024 and last["download"]:
                return last
        raise RuntimeError(f"slide_b{beat} detail did not become downloadable: {last}")
    finally:
        M.safe_release(focus)
        M.safe_release(desktop)
        M.safe_release(target)


def download_detail(beat: int, attempt: int, detail_url: str, destination: Path) -> dict[str, Any]:
    if destination.exists():
        raise RuntimeError(f"refusing to overwrite {destination}")
    downloads = Path.home() / "Downloads"
    before = {p: (p.stat().st_mtime_ns, p.stat().st_size) for p in downloads.iterdir() if p.is_file()}
    click_utc = time.time()
    target = desktop = focus = None
    prior: dict[str, Any] | None = None
    try:
        target, desktop, focus = M.acquire_write_set(300 + beat, attempt)
        prior = B.chrome_tab_state()
        H.probe_exact(allow_detail=True, target_lease=target)
        for lease, action, uses_desktop in (
            (target, f"download exact slide_b{beat} attempt {attempt} detail", False),
            (focus, f"focus exact slide_b{beat} attempt {attempt} Download", False),
            (desktop, f"native Download exact slide_b{beat} attempt {attempt}", True),
        ):
            H.check(lease, action, uses_desktop=uses_desktop)
        subprocess.run(["osascript", "-e", 'tell application "Google Chrome" to set active tab index of window 1 to 1'], check=True)
        time.sleep(0.5)
        active = B.chrome_tab_state()
        if active["index"] != 1 or active["url"] != detail_url:
            raise RuntimeError(f"slide_b{beat} detail target mismatch before Download: {active}")
        pid = int(subprocess.check_output(["pgrep", "-x", "Google Chrome"], text=True).splitlines()[0])
        native_press(pid, "AXPopUpButton", "download Download")
        time.sleep(0.5)
        native_press(pid, "AXMenuItem", "1K Original size")
    finally:
        if target and desktop and focus:
            try:
                B.restore_prior_tab(prior, target, desktop, focus)
            except Exception as exc:
                print("TAB_RESTORE_WARNING", repr(exc), flush=True)
        M.safe_release(focus)
        M.safe_release(desktop)
        M.safe_release(target)
    candidate: Path | None = None
    stable_signature: tuple[int, int] | None = None
    stable_count = 0
    for _ in range(120):
        time.sleep(1)
        if list(downloads.glob("*.crdownload")):
            continue
        changed = []
        for p in downloads.iterdir():
            if not p.is_file():
                continue
            sig = (p.stat().st_mtime_ns, p.stat().st_size)
            if p not in before or before[p] != sig:
                if p.stat().st_mtime >= click_utc - 2:
                    try:
                        with Image.open(p) as image:
                            if image.width >= 1024 and image.height >= 576:
                                changed.append(p)
                    except Exception:
                        pass
        if len(changed) != 1:
            continue
        p = changed[0]
        sig = (p.stat().st_mtime_ns, p.stat().st_size)
        if candidate == p and stable_signature == sig:
            stable_count += 1
        else:
            candidate, stable_signature, stable_count = p, sig, 1
        if stable_count >= 2:
            break
    if candidate is None or stable_count < 2:
        raise RuntimeError(f"slide_b{beat} unique image download not found")
    destination.parent.mkdir(parents=True, exist_ok=True)
    os.replace(candidate, destination)
    with Image.open(destination) as image:
        probe = {"format": image.format, "width": image.width, "height": image.height, "mode": image.mode, "size": destination.stat().st_size}
        image.verify()
    if probe["width"] < 1024 or probe["height"] < 576:
        raise RuntimeError(f"slide_b{beat} downloaded image too small: {probe}")
    target = M.wait_acquire(
        f"yui-flow-pgr-slide-b{beat}-attempt{attempt}-return",
        "target",
        "write",
        {"host_id": "studio", "bundle": "com.google.Chrome", "user_data_dir": "default-google-chrome-profile", "window_id": "1", "target_id": "flow-project-a22b5b61"},
        300,
        120,
    )
    try:
        H.probe_exact(allow_detail=True, target_lease=target)
        H.check(target, f"return from exact slide_b{beat} detail to project root")
        H.run_js_raw("history.back(); 'BACK'")
        for _ in range(30):
            time.sleep(0.5)
            if H.probe_exact(allow_detail=True, target_lease=target)["url"] == ROOT:
                break
        else:
            raise RuntimeError(f"slide_b{beat} could not return to root")
    finally:
        M.safe_release(target)
    probe["sha256"] = sha256_file(destination)
    return probe


def update_state(beat: int, attempt: int, receipt: dict[str, Any], status: str) -> None:
    state = json.loads(STATE.read_text())
    gate = state.setdefault("slide_gate", {})
    gate.update({
        "last_asset": f"slide_b{beat}",
        "last_attempt": attempt,
        "last_submit_utc": receipt.get("submit_utc"),
        "last_media_id": receipt.get("media_id"),
        "status": status,
    })
    state["status"] = "ACTIVE_SLIDES_NARRATION_HELD" if status == "AWAITING_TEXT_VERIFICATION" else status
    state["updated_utc"] = utc_now()
    tmp = STATE.with_suffix(".tmp")
    tmp.write_text(json.dumps(state, indent=2, sort_keys=True) + "\n")
    os.replace(tmp, STATE)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--beat", type=int, required=True, choices=range(2, 6))
    parser.add_argument("--attempt", type=int, default=1, choices=(1, 2))
    parser.add_argument("--dry-run", action="store_true")
    args = parser.parse_args()
    beat = args.beat
    attempt = args.attempt
    prompt = prompt_for(beat)
    destination = OUTPUT_DIR / f"slide_b{beat}_attempt{attempt}.jpg"
    final = OUTPUT_DIR / f"slide_b{beat}.png"
    if destination.exists() or final.exists():
        raise RuntimeError(f"refusing overlap: attempt={destination.exists()} final={final.exists()}")
    state = json.loads(STATE.read_text())
    if state.get("narration_hold", {}).get("status") != "MORNING_DECISION_REQUIRED":
        raise RuntimeError("narration morning hold missing")
    if state.get("slide_gate", {}).get("hold") is not False:
        raise RuntimeError(f"slide gate held: {state.get('slide_gate')}")
    if args.dry_run:
        print(json.dumps({"beat": beat, "attempt": attempt, "prompt": prompt, "prompt_sha256": sha256_text(prompt), "destination": str(destination), "summary": SUMMARY}, sort_keys=True))
        return 0
    target = desktop = focus = None
    prior: dict[str, Any] | None = None
    submit_utc = account_lease_id = detail_url = ""
    try:
        target, desktop, focus = M.acquire_write_set(300 + beat, attempt)
        prior = B.activate_flow(target, desktop, focus)
        H.ensure_root(target)
        verify_config(beat, attempt, target, desktop, focus)
        paste_prompt(beat, attempt, prompt, target, desktop, focus)
        config = verify_config(beat, attempt, target, desktop, focus)
        submit_utc, account_lease_id, detail_url = submit_once(beat, attempt, prompt, target, desktop, focus)
    finally:
        if target and desktop and focus:
            try:
                B.restore_prior_tab(prior, target, desktop, focus)
            except Exception as exc:
                print("TAB_RESTORE_WARNING", repr(exc), flush=True)
        M.safe_release(focus)
        M.safe_release(desktop)
        M.safe_release(target)
    settled = poll_card(beat, attempt, prompt, detail_url)
    detail = navigate_detail(beat, attempt, detail_url, prompt)
    media_id = detail_url.rsplit("/", 1)[-1]
    probe = download_detail(beat, attempt, detail_url, destination)
    receipt = {
        "task": "PGR_PILOT_SLIDE",
        "asset": f"slide_b{beat}",
        "attempt": attempt,
        "model": "Nano Banana Pro",
        "aspect_ratio": "16:9",
        "output_count": "1x",
        "displayed_credits": config["credit"],
        "title": SLIDES[beat]["title"],
        "caption": SLIDES[beat]["caption"],
        "prompt": prompt,
        "prompt_sha256": sha256_text(prompt),
        "submit_utc": submit_utc,
        "account_lease_id": account_lease_id,
        "detail_url": detail_url,
        "media_id": media_id,
        "settlement_elapsed_s": settled["settlement_elapsed_s"],
        "detail_image": detail["image"],
        "artifact": str(destination),
        "artifact_probe": probe,
        "text_verification": "PENDING_VISUAL_REVIEW",
        "challenge_observed": False,
        "status": "AWAITING_TEXT_VERIFICATION",
        "saved_utc": utc_now(),
    }
    receipt_path = OUTPUT_DIR / f"PGR_SLIDE_B{beat}_ATTEMPT{attempt}.json"
    receipt_path.write_text(json.dumps(receipt, indent=2, sort_keys=True) + "\n")
    update_state(beat, attempt, receipt, "AWAITING_TEXT_VERIFICATION")
    print("PGR_SLIDE_SAVED", json.dumps({"beat": beat, "attempt": attempt, "path": str(destination), "sha256": probe["sha256"], "media_id": media_id, "receipt": str(receipt_path)}, sort_keys=True), flush=True)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
