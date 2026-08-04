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
IDENTITY_PATH = Path("receipts/GORU_DR_RUN_IDENTITY.json")
SCOPE = {"host_id": "pro", "bundle": "com.google.Chrome", "user_data_dir": "dr-live-cdp-20260714", "window_id": "pid-65195", "target_id": TARGET_ID}


def need(resp, name):
    if not resp.get("ok"):
        raise RuntimeError(f"{name}: {resp}")
    return resp


def target_exact(path):
    with urllib.request.urlopen(f"{BASE}/json/list", timeout=3) as response:
        pages = json.load(response)
    matches = [x for x in pages if x.get("id") == TARGET_ID and x.get("type") == "page"]
    if len(matches) != 1:
        return None
    parsed = urlparse(matches[0].get("url", ""))
    return matches[0] if parsed.scheme == "https" and parsed.netloc == "gemini.google.com" and parsed.path == path else None


def challenge(page):
    return page.evaluate("""() => {
      const v=e=>{const s=getComputedStyle(e),r=e.getBoundingClientRect();return s.display!=='none'&&s.visibility!=='hidden'&&r.width>0&&r.height>0};
      const d=[...document.querySelectorAll('[role=dialog],dialog')].filter(v).map(e=>(e.innerText||'').slice(0,500));
      return location.hostname==='accounts.google.com'||[...document.querySelectorAll('input[type=password]')].some(v)||[...document.querySelectorAll('iframe')].some(e=>/recaptcha|captcha/i.test(e.src||''))||d.some(t=>/captcha|verify|verification|sign in|two-step|2-step|unusual activity|permission|challenge/i.test(t));
    }""")


def freeze(client, reason):
    need(client.op({"op": "freeze", "declared_by": "tori-goru-dr-one-start", "reason": reason}), "freeze")
    raise RuntimeError(reason)


def main():
    identity = json.loads(IDENTITY_PATH.read_text())
    path = identity.get("conversation_path")
    if identity.get("target_id") != TARGET_ID or path != f"/app/{identity.get('conversation_id', '')}" or not identity.get("conversation_title") or not identity.get("submit_utc"):
        raise RuntimeError("conversation identity custody incomplete")
    if "research_start_utc" in identity:
        raise RuntimeError("research start already recorded")
    client = UDSClient(SOCK)
    target_lease = None
    submit_lease = None
    try:
        if target_exact(path) is None:
            raise RuntimeError("exact conversation target failed")
        target_lease = need(client.op({"op": "acquire", "holder": "tori-goru-dr-one-start", "kind": "target", "mode": "write", "scope": SCOPE, "ttl": 180, "heartbeat_interval": 45}), "target acquire")["lease"]
        with sync_playwright() as p:
            browser = p.chromium.connect_over_cdp(BASE)
            pages = [pg for ctx in browser.contexts for pg in ctx.pages if urlparse(pg.url).path == path]
            if len(pages) != 1:
                raise RuntimeError(f"exact conversation page count {len(pages)}")
            page = pages[0]
            if challenge(page):
                freeze(client, "real page-content challenge before Start research")
            start = page.get_by_text("Start research", exact=True)
            visible = [start.nth(i) for i in range(start.count()) if start.nth(i).is_visible()]
            if len(visible) != 1 or visible[0].is_disabled():
                raise RuntimeError(f"Start research exact enabled visible count {len(visible)}")
            submit_lease = need(client.op({"op": "acquire", "holder": "tori-goru-dr-one-start", "kind": "account-submission", "mode": "write", "scope": {}, "ttl": 120, "heartbeat_interval": 45}), "account-submission acquire")["lease"]
            verified = target_exact(path) is not None
            if not verified:
                need(client.op({"op": "check", "lease_id": target_lease["lease_id"], "epoch": target_lease["epoch"], "action": "Start research for exact bounded DR conversation", "target_verified": False}), "target drift")
            if challenge(page):
                freeze(client, "real page-content challenge immediately before Start research")
            need(client.op({"op": "check", "lease_id": target_lease["lease_id"], "epoch": target_lease["epoch"], "action": "Start research for exact bounded DR conversation", "target_verified": True}), "target start check")
            need(client.op({"op": "check", "lease_id": submit_lease["lease_id"], "epoch": submit_lease["epoch"], "action": "serialized shared-account submit: Start research for one bounded DR conversation", "target_verified": True}), "account start check")
            start_utc = datetime.now(timezone.utc).isoformat().replace("+00:00", "Z")
            try:
                visible[0].click()
            finally:
                need(client.op({"op": "release", "lease_id": submit_lease["lease_id"]}), "account-submission release")
                submit_lease = None
            start.wait_for(state="hidden", timeout=30000)
            if target_exact(path) is None:
                need(client.op({"op": "check", "lease_id": target_lease["lease_id"], "epoch": target_lease["epoch"], "action": "confirm bounded DR research started", "target_verified": False}), "post-start drift")
            if challenge(page):
                freeze(client, "real page-content challenge after Start research")
            status = page.locator("button:visible,[role=button]:visible,div:visible,span:visible").evaluate_all("els=>[...new Set(els.map(e=>(e.getAttribute('aria-label')||e.innerText||'').trim().replace(/\\s+/g,' ')).filter(x=>x&&x.length<160&&/researching|stop researching|stop response|research started|searching/i.test(x)))].slice(0,30)")
            identity["research_start_utc"] = start_utc
            identity["research_start_confirmed"] = True
            identity["post_start_status_labels"] = status
            IDENTITY_PATH.write_text(json.dumps(identity, indent=2, sort_keys=True) + "\n")
            print(json.dumps({"conversation_id": identity["conversation_id"], "research_start_utc": start_utc, "status": status}, sort_keys=True))
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
