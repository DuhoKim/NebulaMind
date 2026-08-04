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
MARKER = "## DR PROMPT (submit verbatim)\n"
BRIEF_TEXT = BRIEF_PATH.read_text()
if BRIEF_TEXT.count(MARKER) != 1:
    raise RuntimeError("verbatim prompt marker count is not one")
PROMPT = BRIEF_TEXT.split(MARKER, 1)[1].rstrip("\n")
EXPECTED_PROMPT_SHA = "6d3b61d77e50aab1dd341d5a4c52c9bd07845f64b465d6da3d5e339bc1e0f5d9"
EXPECTED_BRIEF_SHA = "8d0986ced501d14871bfa067cc0712adf2e3c00cea657a2542e093d213b0d03b"
SCOPE = {"host_id": "pro", "bundle": "com.google.Chrome", "user_data_dir": "dr-live-cdp-20260714", "window_id": "pid-65195", "target_id": TARGET_ID}


def need(resp, name):
    if not resp.get("ok"):
        raise RuntimeError(f"{name}: {resp}")
    return resp


def target_ok():
    with urllib.request.urlopen(f"{BASE}/json/list", timeout=3) as response:
        pages = json.load(response)
    hits = [x for x in pages if x.get("id") == TARGET_ID and x.get("type") == "page"]
    if len(hits) != 1:
        return False
    parsed = urlparse(hits[0].get("url", ""))
    return parsed.scheme == "https" and parsed.netloc == "gemini.google.com" and parsed.path == "/app"


def challenge(page):
    return page.evaluate("""() => {const v=e=>{const s=getComputedStyle(e),r=e.getBoundingClientRect();return s.display!=='none'&&s.visibility!=='hidden'&&r.width>0&&r.height>0};const d=[...document.querySelectorAll('[role=dialog],dialog')].filter(v).map(e=>(e.innerText||'').slice(0,500));return location.hostname==='accounts.google.com'||[...document.querySelectorAll('input[type=password]')].some(v)||[...document.querySelectorAll('iframe')].some(e=>/recaptcha|captcha/i.test(e.src||''))||d.some(t=>/captcha|verify|verification|sign in|two-step|2-step|unusual activity|permission|challenge/i.test(t))}""")


def main():
    if STAGE_PATH.exists():
        raise RuntimeError("Quasars stage receipt already exists")
    if hashlib.sha256(BRIEF_PATH.read_bytes()).hexdigest() != EXPECTED_BRIEF_SHA:
        raise RuntimeError("brief hash mismatch")
    if hashlib.sha256(PROMPT.encode()).hexdigest() != EXPECTED_PROMPT_SHA:
        raise RuntimeError("verbatim prompt hash mismatch")
    if not target_ok():
        raise RuntimeError("exact new-chat target failed")
    client = UDSClient(SOCK); lease = None
    try:
        lease = need(client.op({"op": "acquire", "holder": "tori-goru-quasars-dr-stage", "kind": "target", "mode": "write", "scope": SCOPE, "ttl": 180, "heartbeat_interval": 45}), "stage target acquire")["lease"]
        with sync_playwright() as p:
            browser = p.chromium.connect_over_cdp(BASE)
            pages = [pg for ctx in browser.contexts for pg in ctx.pages if urlparse(pg.url).path == "/app"]
            if len(pages) != 1:
                raise RuntimeError(f"new-chat page count {len(pages)}")
            page = pages[0]
            if challenge(page):
                need(client.op({"op": "freeze", "declared_by": "tori-goru-quasars-dr-stage", "reason": "real page-content challenge before Quasars DR staging"}), "freeze")
                raise RuntimeError("page challenge: broker frozen")
            active = page.get_by_label("Deselect Deep research", exact=True)
            if not (active.count() == 1 and active.is_visible()):
                tool = page.get_by_label("Upload & tools", exact=True)
                if tool.count() != 1 or not tool.is_visible():
                    raise RuntimeError("Upload & tools is not unique visible")
                need(client.op({"op": "check", "lease_id": lease["lease_id"], "epoch": lease["epoch"], "action": "open Upload & tools for Quasars prove-first DR", "target_verified": target_ok()}), "open tools check")
                tool.click(); page.wait_for_timeout(500)
                deep = page.get_by_text("Deep research", exact=True)
                visible = [deep.nth(i) for i in range(deep.count()) if deep.nth(i).is_visible()]
                if len(visible) != 1:
                    raise RuntimeError(f"Deep research exact visible count {len(visible)}")
                need(client.op({"op": "check", "lease_id": lease["lease_id"], "epoch": lease["epoch"], "action": "select exact Deep research for Quasars prove-first", "target_verified": target_ok()}), "select Deep research check")
                visible[0].click(); page.wait_for_timeout(700)
            active = page.get_by_label("Deselect Deep research", exact=True)
            if active.count() != 1 or not active.is_visible():
                raise RuntimeError("Deep research mode not uniquely active")
            editor = page.get_by_role("textbox", name="Enter a prompt for Gemini", exact=True)
            if editor.count() != 1 or not editor.is_visible():
                raise RuntimeError("prompt editor not unique visible")
            need(client.op({"op": "check", "lease_id": lease["lease_id"], "epoch": lease["epoch"], "action": "fill verbatim Quasars prove-first DR prompt", "target_verified": target_ok()}), "fill prompt check")
            editor.fill(PROMPT)
            page.wait_for_timeout(500)
            lines = editor.evaluate("""el => [...el.children].map(child => {
                const value = (child.innerText || '').replace(/\\r\\n/g, '\\n');
                return value === '\\n' ? '' : value;
            })""")
            actual = "\n".join(lines)
            actual_sha = hashlib.sha256(actual.encode()).hexdigest()
            if actual != PROMPT or actual_sha != EXPECTED_PROMPT_SHA:
                raise RuntimeError(f"staged prompt is not verbatim: chars={len(actual)} sha={actual_sha}")
            send = page.get_by_label("Send message", exact=True)
            if send.count() != 1 or not send.is_visible() or send.is_disabled():
                raise RuntimeError("Send message not one enabled visible control")
            stage = {
                "brief": str(BRIEF_PATH), "brief_sha256": EXPECTED_BRIEF_SHA,
                "prompt_chars": len(PROMPT), "prompt_lines": len(PROMPT.splitlines()),
                "prompt_sha256": EXPECTED_PROMPT_SHA, "staged_text_sha256": actual_sha,
                "target_id": TARGET_ID, "page_path": "/app", "page_challenge": False,
                "deep_research_active": True, "send_message_unique_enabled": True,
                "staged_utc": datetime.now(timezone.utc).isoformat().replace("+00:00", "Z"),
            }
            STAGE_PATH.write_text(json.dumps(stage, indent=2, sort_keys=True) + "\n")
            print(json.dumps(stage, sort_keys=True))
    finally:
        if lease is not None:
            with suppress(Exception): print(json.dumps({"stage_target_release": client.op({"op": "release", "lease_id": lease["lease_id"]})}, sort_keys=True))
        client.close()


if __name__ == "__main__": main()
