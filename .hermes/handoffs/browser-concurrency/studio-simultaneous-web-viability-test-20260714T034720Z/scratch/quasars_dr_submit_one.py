import hashlib
import json
import sys
import urllib.request
from contextlib import suppress
from datetime import datetime, timezone
from pathlib import Path
from urllib.parse import urlparse

sys.path.insert(0, "broker")
from transport import UDSClient
from playwright.sync_api import sync_playwright

SOCK = "/tmp/nmbrk-live-20260714/b.sock"
BASE = "http://127.0.0.1:19223"
TARGET_ID = "C92443095EE9116210C178D855DF3329"
BRIEF_PATH = Path("briefs/DR_PROVEFIRST_QUASARS_PROMPT.md")
STAGE_PATH = Path("receipts/GORU_DR_PROVEFIRST_QUASARS_STAGE.json")
IDENTITY_PATH = Path("receipts/GORU_DR_PROVEFIRST_QUASARS_RUN_IDENTITY.json")
MARKER = "## DR PROMPT (submit verbatim)\n"
PROMPT = BRIEF_PATH.read_text().split(MARKER, 1)[1].rstrip("\n")
PROMPT_SHA = "6d3b61d77e50aab1dd341d5a4c52c9bd07845f64b465d6da3d5e339bc1e0f5d9"
SCOPE = {"host_id": "pro", "bundle": "com.google.Chrome", "user_data_dir": "dr-live-cdp-20260714", "window_id": "pid-65195", "target_id": TARGET_ID}


def need(resp, name):
    if not resp.get("ok"):
        raise RuntimeError(f"{name}: {resp}")
    return resp


def exact_target(initial=False):
    with urllib.request.urlopen(f"{BASE}/json/list", timeout=3) as response:
        pages = json.load(response)
    hits = [x for x in pages if x.get("id") == TARGET_ID and x.get("type") == "page"]
    if len(hits) != 1:
        return None
    parsed = urlparse(hits[0].get("url", ""))
    if parsed.scheme != "https" or parsed.netloc != "gemini.google.com":
        return None
    if initial and parsed.path != "/app":
        return None
    if not initial and not (parsed.path == "/app" or parsed.path.startswith("/app/")):
        return None
    return hits[0]


def challenge(page):
    return page.evaluate("""() => {const v=e=>{const s=getComputedStyle(e),r=e.getBoundingClientRect();return s.display!=='none'&&s.visibility!=='hidden'&&r.width>0&&r.height>0};const d=[...document.querySelectorAll('[role=dialog],dialog')].filter(v).map(e=>(e.innerText||'').slice(0,500));return location.hostname==='accounts.google.com'||[...document.querySelectorAll('input[type=password]')].some(v)||[...document.querySelectorAll('iframe')].some(e=>/recaptcha|captcha/i.test(e.src||''))||d.some(t=>/captcha|verify|verification|sign in|two-step|2-step|unusual activity|permission|challenge/i.test(t))}""")


def freeze(client, reason):
    need(client.op({"op": "freeze", "declared_by": "tori-goru-quasars-dr-submit", "reason": reason}), "freeze")
    raise RuntimeError(reason)


def staged_prompt(editor):
    lines = editor.evaluate("""el => [...el.children].map(child => {
        const value = (child.innerText || '').replace(/\\r\\n/g, '\\n');
        return value === '\\n' ? '' : value;
    })""")
    return "\n".join(lines)


def titles_for(page, path):
    return page.evaluate("""path => {const v=e=>{const s=getComputedStyle(e),r=e.getBoundingClientRect();return s.display!=='none'&&s.visibility!=='hidden'&&r.width>0&&r.height>0};const rows=[...document.querySelectorAll('a[href]')].filter(v).filter(a=>{try{return new URL(a.href).pathname===path}catch{return false}});return [...new Set(rows.map(a=>(a.getAttribute('aria-label')||a.innerText||a.textContent||'').trim().replace(/\\s+/g,' ')).filter(Boolean))]}""", path)


def main():
    if IDENTITY_PATH.exists():
        raise RuntimeError(f"identity already exists: {IDENTITY_PATH}")
    stage = json.loads(STAGE_PATH.read_text())
    if stage.get("prompt_sha256") != PROMPT_SHA or stage.get("staged_text_sha256") != PROMPT_SHA:
        raise RuntimeError("stage receipt prompt hash mismatch")
    if hashlib.sha256(PROMPT.encode()).hexdigest() != PROMPT_SHA:
        raise RuntimeError("source prompt hash mismatch")
    if exact_target(initial=True) is None:
        raise RuntimeError("exact new-chat target failed")
    client = UDSClient(SOCK); target_lease = None; submit_lease = None
    try:
        target_lease = need(client.op({"op": "acquire", "holder": "tori-goru-quasars-dr-one", "kind": "target", "mode": "write", "scope": SCOPE, "ttl": 300, "heartbeat_interval": 45}), "target acquire")["lease"]
        with sync_playwright() as p:
            browser = p.chromium.connect_over_cdp(BASE)
            pages = [pg for ctx in browser.contexts for pg in ctx.pages if pg.url == "https://gemini.google.com/app"]
            if len(pages) != 1:
                raise RuntimeError(f"new-chat page count {len(pages)}")
            page = pages[0]
            if challenge(page): freeze(client, "real page-content challenge before Quasars DR submit")
            active = page.get_by_label("Deselect Deep research", exact=True)
            if active.count() != 1 or not active.is_visible():
                raise RuntimeError("Deep research not uniquely active")
            editor = page.get_by_role("textbox", name="Enter a prompt for Gemini", exact=True)
            if editor.count() != 1 or not editor.is_visible():
                raise RuntimeError("prompt editor not unique visible")
            actual = staged_prompt(editor)
            if actual != PROMPT or hashlib.sha256(actual.encode()).hexdigest() != PROMPT_SHA:
                raise RuntimeError("staged prompt not verbatim immediately before submit")
            send = page.get_by_label("Send message", exact=True)
            if send.count() != 1 or not send.is_visible() or send.is_disabled():
                raise RuntimeError("Send message not one enabled visible control")
            submit_lease = need(client.op({"op": "acquire", "holder": "tori-goru-quasars-dr-one", "kind": "account-submission", "mode": "write", "scope": {}, "ttl": 120, "heartbeat_interval": 45}), "account-submission acquire")["lease"]
            verified = exact_target(initial=True) is not None
            if not verified:
                need(client.op({"op": "check", "lease_id": target_lease["lease_id"], "epoch": target_lease["epoch"], "action": "submit verbatim Quasars prove-first DR prompt", "target_verified": False}), "target drift")
            if challenge(page): freeze(client, "real page-content challenge immediately before Quasars DR submit")
            need(client.op({"op": "check", "lease_id": target_lease["lease_id"], "epoch": target_lease["epoch"], "action": "submit verbatim Quasars prove-first DR prompt", "target_verified": True}), "target submit check")
            need(client.op({"op": "check", "lease_id": submit_lease["lease_id"], "epoch": submit_lease["epoch"], "action": "serialized shared-account submit: one Quasars prove-first DR prompt", "target_verified": True}), "account submit check")
            submit_utc = datetime.now(timezone.utc).isoformat().replace("+00:00", "Z")
            try:
                send.click()
            finally:
                need(client.op({"op": "release", "lease_id": submit_lease["lease_id"]}), "account-submission release")
                submit_lease = None
            page.wait_for_url(lambda url: urlparse(url).netloc == "gemini.google.com" and urlparse(url).path.startswith("/app/"), timeout=30000)
            target = exact_target(initial=False)
            if target is None or target.get("url") != page.url:
                need(client.op({"op": "check", "lease_id": target_lease["lease_id"], "epoch": target_lease["epoch"], "action": "capture exact Quasars DR conversation identity", "target_verified": False}), "post-submit drift")
            if challenge(page): freeze(client, "real page-content challenge after Quasars DR submit")
            path = urlparse(page.url).path; conversation_id = path.removeprefix("/app/")
            if not conversation_id or "/" in conversation_id:
                raise RuntimeError(f"invalid conversation path {path}")
            titles = []
            for index in range(24):
                if index % 8 == 0:
                    need(client.op({"op": "heartbeat", "lease_id": target_lease["lease_id"]}), "target heartbeat")
                titles = [x for x in titles_for(page, path) if x not in {"New chat", "Google Gemini"}]
                if len(titles) == 1:
                    break
                if index == 2:
                    open_sidebar = page.get_by_label("Open sidebar", exact=True)
                    if open_sidebar.count() == 1 and open_sidebar.is_visible():
                        need(client.op({"op": "check", "lease_id": target_lease["lease_id"], "epoch": target_lease["epoch"], "action": "open sidebar to capture exact Quasars conversation title", "target_verified": exact_target(initial=False) is not None}), "open sidebar check")
                        open_sidebar.click()
                page.wait_for_timeout(2500)
            if len(titles) != 1:
                raise RuntimeError(f"exact conversation title candidate count {len(titles)}")
            identity = {
                "target_id": TARGET_ID, "conversation_id": conversation_id, "conversation_path": path,
                "conversation_title": titles[0], "conversation_title_candidates": titles,
                "submit_utc": submit_utc, "prompt": PROMPT, "prompt_sha256": PROMPT_SHA,
                "brief_sha256": stage["brief_sha256"], "stage_receipt_sha256": hashlib.sha256(STAGE_PATH.read_bytes()).hexdigest(),
                "page_challenge_after_submit": False,
            }
            IDENTITY_PATH.write_text(json.dumps(identity, indent=2, sort_keys=True) + "\n")
            print(json.dumps(identity, sort_keys=True))
    finally:
        if submit_lease is not None:
            with suppress(Exception): client.op({"op": "release", "lease_id": submit_lease["lease_id"]})
        if target_lease is not None:
            with suppress(Exception): print(json.dumps({"target_release": client.op({"op": "release", "lease_id": target_lease["lease_id"]})}, sort_keys=True))
        client.close()


if __name__ == "__main__": main()
