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
PROMPT = "Using official Apple and Google Chrome documentation, explain in no more than eight bullets how a direct Thunderbolt Bridge between two Macs can support isolated browser automation. Include two limitations and source links."
IDENTITY_PATH = Path("receipts/GORU_DR_RUN_IDENTITY.json")
SCOPE = {"host_id": "pro", "bundle": "com.google.Chrome", "user_data_dir": "dr-live-cdp-20260714", "window_id": "pid-65195", "target_id": TARGET_ID}


def need(resp, name):
    if not resp.get("ok"):
        raise RuntimeError(f"{name}: {resp}")
    return resp


def exact_target(require_initial=False):
    with urllib.request.urlopen(f"{BASE}/json/list", timeout=3) as response:
        pages = json.load(response)
    matches = [x for x in pages if x.get("type") == "page" and x.get("id") == TARGET_ID]
    if len(matches) != 1:
        return None
    parsed = urlparse(matches[0].get("url", ""))
    if parsed.scheme != "https" or parsed.netloc != "gemini.google.com":
        return None
    if require_initial and parsed.path != "/app":
        return None
    if not require_initial and not (parsed.path == "/app" or parsed.path.startswith("/app/")):
        return None
    return matches[0]


def page_challenge(page):
    return page.evaluate("""() => {
      const v=e=>{const s=getComputedStyle(e),r=e.getBoundingClientRect();return s.display!=='none'&&s.visibility!=='hidden'&&r.width>0&&r.height>0};
      const d=[...document.querySelectorAll('[role=dialog],dialog')].filter(v).map(e=>(e.innerText||'').slice(0,500));
      return location.hostname==='accounts.google.com'||[...document.querySelectorAll('input[type=password]')].some(v)||[...document.querySelectorAll('iframe')].some(e=>/recaptcha|captcha/i.test(e.src||''))||d.some(t=>/captcha|verify|verification|sign in|two-step|2-step|unusual activity|permission|challenge/i.test(t));
    }""")


def freeze(client, reason):
    need(client.op({"op": "freeze", "declared_by": "tori-goru-dr-one-submit", "reason": reason}), "freeze")
    raise RuntimeError(reason)


def conversation_title(page, path):
    return page.evaluate("""path => {
      const v=e=>{const s=getComputedStyle(e),r=e.getBoundingClientRect();return s.display!=='none'&&s.visibility!=='hidden'&&r.width>0&&r.height>0};
      const rows=[...document.querySelectorAll('a[href]')].filter(v).filter(a=>{try{return new URL(a.href).pathname===path}catch{return false}});
      const vals=rows.map(a=>(a.getAttribute('aria-label')||a.innerText||a.textContent||'').trim().replace(/\\s+/g,' ')).filter(Boolean);
      return [...new Set(vals)];
    }""", path)


def main():
    if IDENTITY_PATH.exists():
        raise RuntimeError(f"identity file already exists: {IDENTITY_PATH}")
    client = UDSClient(SOCK)
    target_lease = None
    submit_lease = None
    submit_utc = None
    try:
        if exact_target(require_initial=True) is None:
            raise RuntimeError("exact initial target preflight failed")
        target_lease = need(client.op({"op": "acquire", "holder": "tori-goru-dr-one-run", "kind": "target", "mode": "write", "scope": SCOPE, "ttl": 300, "heartbeat_interval": 45}), "target acquire")["lease"]
        with sync_playwright() as p:
            browser = p.chromium.connect_over_cdp(BASE)
            pages = [pg for ctx in browser.contexts for pg in ctx.pages if pg.url == "https://gemini.google.com/app"]
            if len(pages) != 1:
                raise RuntimeError(f"exact initial page count {len(pages)}")
            page = pages[0]
            if page_challenge(page):
                freeze(client, "real page-content challenge before bounded DR submit")
            active_mode = page.get_by_label("Deselect Deep research", exact=True)
            if active_mode.count() != 1 or not active_mode.is_visible():
                raise RuntimeError("Deep research mode is not uniquely active")
            editor = page.get_by_role("textbox", name="Enter a prompt for Gemini", exact=True)
            if editor.count() != 1 or not editor.is_visible() or (editor.text_content() or "").strip() != PROMPT:
                raise RuntimeError("staged prompt mismatch")
            send = page.get_by_label("Send message", exact=True)
            if send.count() != 1 or not send.is_visible() or send.is_disabled():
                raise RuntimeError("Send message is not one enabled visible control")
            submit_lease = need(client.op({"op": "acquire", "holder": "tori-goru-dr-one-run", "kind": "account-submission", "mode": "write", "scope": {}, "ttl": 120, "heartbeat_interval": 45}), "account-submission acquire")["lease"]
            if exact_target(require_initial=True) is None:
                need(client.op({"op": "check", "lease_id": target_lease["lease_id"], "epoch": target_lease["epoch"], "action": "submit one bounded Deep Research prompt", "target_verified": False}), "target drift")
            if page_challenge(page):
                freeze(client, "real page-content challenge immediately before bounded DR submit")
            need(client.op({"op": "check", "lease_id": target_lease["lease_id"], "epoch": target_lease["epoch"], "action": "submit one bounded Deep Research prompt", "target_verified": True}), "target submit check")
            need(client.op({"op": "check", "lease_id": submit_lease["lease_id"], "epoch": submit_lease["epoch"], "action": "serialized shared-account submit: one bounded Deep Research prompt", "target_verified": True}), "account submit check")
            submit_utc = datetime.now(timezone.utc).isoformat().replace("+00:00", "Z")
            try:
                send.click()
            finally:
                need(client.op({"op": "release", "lease_id": submit_lease["lease_id"]}), "account-submission release")
                submit_lease = None
            page.wait_for_url(lambda url: urlparse(url).netloc == "gemini.google.com" and urlparse(url).path.startswith("/app/"), timeout=30000)
            target = exact_target(require_initial=False)
            if target is None or target.get("url") != page.url:
                need(client.op({"op": "check", "lease_id": target_lease["lease_id"], "epoch": target_lease["epoch"], "action": "capture exact DR conversation identity", "target_verified": False}), "post-submit target drift")
            if page_challenge(page):
                freeze(client, "real page-content challenge after bounded DR submit")
            path = urlparse(page.url).path
            conversation_id = path.removeprefix("/app/")
            if not conversation_id or "/" in conversation_id:
                raise RuntimeError(f"invalid conversation path {path}")
            titles = []
            for index in range(24):
                if index % 8 == 0:
                    need(client.op({"op": "heartbeat", "lease_id": target_lease["lease_id"]}), "target heartbeat")
                titles = conversation_title(page, path)
                titles = [x for x in titles if x not in {"New chat", "Google Gemini"}]
                if len(titles) == 1:
                    break
                page.wait_for_timeout(2500)
            identity = {
                "target_id": TARGET_ID,
                "conversation_id": conversation_id,
                "conversation_path": path,
                "conversation_title": titles[0] if len(titles) == 1 else None,
                "conversation_title_candidates": titles,
                "submit_utc": submit_utc,
                "prompt": PROMPT,
                "page_challenge_after_submit": False,
            }
            IDENTITY_PATH.write_text(json.dumps(identity, indent=2, sort_keys=True) + "\n")
            print(json.dumps(identity, sort_keys=True))
    finally:
        if submit_lease is not None:
            with suppress(Exception):
                client.op({"op": "release", "lease_id": submit_lease["lease_id"]})
        if target_lease is not None:
            with suppress(Exception):
                print(json.dumps({"target_release": client.op({"op": "release", "lease_id": target_lease["lease_id"]})}, sort_keys=True))
        client.close()


if __name__ == "__main__":
    main()
