import hashlib
import json
import sys
import time
import urllib.request
from contextlib import suppress
from pathlib import Path
from urllib.parse import urlparse

sys.path.insert(0, "broker")
from transport import UDSClient
from playwright.sync_api import sync_playwright

SOCK = "/tmp/nmbrk-live-20260714/b.sock"
BASE = "http://127.0.0.1:19223"
TARGET_ID = "C92443095EE9116210C178D855DF3329"
IDENTITY = json.loads(Path("receipts/GORU_DR_RUN_IDENTITY.json").read_text())
PATH = IDENTITY["conversation_path"]
SCOPE = {"host_id": "pro", "bundle": "com.google.Chrome", "user_data_dir": "dr-live-cdp-20260714", "window_id": "pid-65195", "target_id": TARGET_ID}


def need(resp, name):
    if not resp.get("ok"):
        raise RuntimeError(f"{name}: {resp}")
    return resp


def target_ok():
    with urllib.request.urlopen(f"{BASE}/json/list", timeout=3) as response:
        pages = json.load(response)
    matches = [x for x in pages if x.get("id") == TARGET_ID and x.get("type") == "page"]
    if len(matches) != 1:
        return False
    u = urlparse(matches[0].get("url", ""))
    return u.scheme == "https" and u.netloc == "gemini.google.com" and u.path == PATH


def snapshot(page):
    return page.evaluate("""() => {
      const v=e=>{const s=getComputedStyle(e),r=e.getBoundingClientRect();return s.display!=='none'&&s.visibility!=='hidden'&&r.width>0&&r.height>0};
      const label=e=>(e.getAttribute('aria-label')||e.getAttribute('title')||e.innerText||'').trim().replace(/\\s+/g,' ').slice(0,220);
      const dialogs=[...document.querySelectorAll('[role=dialog],dialog')].filter(v).map(label);
      const challenge=location.hostname==='accounts.google.com'||[...document.querySelectorAll('input[type=password]')].some(v)||[...document.querySelectorAll('iframe')].some(e=>/recaptcha|captcha/i.test(e.src||''))||dialogs.some(t=>/captcha|verify|verification|sign in|two-step|2-step|unusual activity|permission|challenge/i.test(t));
      const controls=[...document.querySelectorAll('button,[role=button]')].filter(v).map(label);
      const messages=[...document.querySelectorAll('message-content')].filter(v).map(e=>({text:(e.innerText||'').trim(),links:e.querySelectorAll('a[href]').length}));
      const researchVisible=[...document.querySelectorAll('div,span,p')].filter(v).map(label).some(x=>/researching(?: \\d+)? websites|research in progress/i.test(x));
      return {challenge,stopVisible:controls.some(x=>x==='Stop response'||/stop researching/i.test(x)),researchVisible,messages};
    }""")


def main():
    if not target_ok():
        raise RuntimeError("exact conversation target unavailable before monitor")
    client = UDSClient(SOCK)
    lease = None
    try:
        lease = need(client.op({"op": "acquire", "holder": "tori-goru-dr-one-monitor", "kind": "target", "mode": "read", "scope": SCOPE, "ttl": 2400, "heartbeat_interval": 45}), "monitor target acquire")["lease"]
        with sync_playwright() as p:
            browser = p.chromium.connect_over_cdp(BASE)
            pages = [pg for ctx in browser.contexts for pg in ctx.pages if urlparse(pg.url).path == PATH]
            if len(pages) != 1:
                raise RuntimeError(f"exact monitor page count {len(pages)}")
            page = pages[0]
            deadline = time.monotonic() + 2400
            while time.monotonic() < deadline:
                verified = target_ok()
                if not verified:
                    need(client.op({"op": "check", "lease_id": lease["lease_id"], "epoch": lease["epoch"], "action": "poll exact bounded DR conversation", "target_verified": False}), "target drift")
                state = snapshot(page)
                if state["challenge"]:
                    need(client.op({"op": "freeze", "declared_by": "tori-goru-dr-one-monitor", "reason": "real page-content challenge during bounded DR run"}), "freeze")
                    raise RuntimeError("page challenge: broker frozen")
                need(client.op({"op": "check", "lease_id": lease["lease_id"], "epoch": lease["epoch"], "action": "read-only poll exact bounded DR conversation", "target_verified": True}), "monitor check")
                need(client.op({"op": "heartbeat", "lease_id": lease["lease_id"]}), "monitor heartbeat")
                lengths = [len(x["text"]) for x in state["messages"]]
                print(json.dumps({"messages": len(lengths), "lengths": lengths, "stop": state["stopVisible"], "research": state["researchVisible"]}, sort_keys=True), flush=True)
                candidate = bool(lengths) and lengths[-1] >= 800 and not state["stopVisible"] and not state["researchVisible"]
                if candidate:
                    digest = hashlib.sha256(state["messages"][-1]["text"].encode()).hexdigest()
                    time.sleep(15)
                    if not target_ok():
                        need(client.op({"op": "check", "lease_id": lease["lease_id"], "epoch": lease["epoch"], "action": "confirm stable bounded DR result", "target_verified": False}), "stable target drift")
                    stable = snapshot(page)
                    stable_digest = hashlib.sha256(stable["messages"][-1]["text"].encode()).hexdigest() if stable["messages"] else ""
                    if not stable["challenge"] and not stable["stopVisible"] and not stable["researchVisible"] and digest == stable_digest:
                        print(json.dumps({"candidate_complete": True, "conversation_id": IDENTITY["conversation_id"], "result_chars": len(stable["messages"][-1]["text"]), "result_sha256_preview": stable_digest}, sort_keys=True), flush=True)
                        return
                time.sleep(20)
            raise RuntimeError("bounded DR monitor timed out after 2400 seconds")
    finally:
        if lease is not None:
            with suppress(Exception):
                print(json.dumps({"monitor_release": client.op({"op": "release", "lease_id": lease["lease_id"]})}, sort_keys=True), flush=True)
        client.close()


if __name__ == "__main__":
    main()
