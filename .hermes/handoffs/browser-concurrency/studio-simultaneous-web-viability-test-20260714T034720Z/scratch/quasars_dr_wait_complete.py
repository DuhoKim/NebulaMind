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
IDENTITY = json.loads(Path("receipts/GORU_DR_PROVEFIRST_QUASARS_RUN_IDENTITY.json").read_text())
PATH = IDENTITY["conversation_path"]
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
    return parsed.scheme == "https" and parsed.netloc == "gemini.google.com" and parsed.path == PATH


def snapshot(page):
    return page.evaluate("""() => {const v=e=>{const s=getComputedStyle(e),r=e.getBoundingClientRect();return s.display!=='none'&&s.visibility!=='hidden'&&r.width>0&&r.height>0};const label=e=>(e.getAttribute('aria-label')||e.getAttribute('title')||e.innerText||'').trim().replace(/\\s+/g,' ').slice(0,220);const dialogs=[...document.querySelectorAll('[role=dialog],dialog')].filter(v).map(label);const challenge=location.hostname==='accounts.google.com'||[...document.querySelectorAll('input[type=password]')].some(v)||[...document.querySelectorAll('iframe')].some(e=>/recaptcha|captcha/i.test(e.src||''))||dialogs.some(t=>/captcha|verify|verification|sign in|two-step|2-step|unusual activity|permission|challenge/i.test(t));const controls=[...document.querySelectorAll('button,[role=button]')].filter(v).map(label);const messages=[...document.querySelectorAll('message-content')].filter(v).map(e=>({text:(e.innerText||'').trim(),links:e.querySelectorAll('a[href]').length}));const researchVisible=[...document.querySelectorAll('div,span,p')].filter(v).map(label).some(x=>/researching(?: \\d+)? websites|research in progress|i'm on it.*research/i.test(x));return {challenge,stopVisible:controls.some(x=>x==='Stop response'||/stop researching/i.test(x)),researchVisible,messages}}""")


def main():
    if IDENTITY.get("target_id") != TARGET_ID or IDENTITY.get("conversation_id") != PATH.removeprefix("/app/") or not IDENTITY.get("research_start_confirmed"):
        raise RuntimeError("Quasars identity/start custody failed")
    if not target_ok():
        raise RuntimeError("exact Quasars target unavailable before monitor")
    client = UDSClient(SOCK); lease = None
    try:
        lease = need(client.op({"op": "acquire", "holder": "tori-goru-quasars-dr-monitor", "kind": "target", "mode": "read", "scope": SCOPE, "ttl": 2700, "heartbeat_interval": 45}), "monitor target acquire")["lease"]
        with sync_playwright() as p:
            browser = p.chromium.connect_over_cdp(BASE)
            pages = [pg for ctx in browser.contexts for pg in ctx.pages if urlparse(pg.url).path == PATH]
            if len(pages) != 1:
                raise RuntimeError(f"exact Quasars monitor page count {len(pages)}")
            page = pages[0]; deadline = time.monotonic() + 2700
            while time.monotonic() < deadline:
                if not target_ok():
                    need(client.op({"op": "check", "lease_id": lease["lease_id"], "epoch": lease["epoch"], "action": "poll exact Quasars DR conversation", "target_verified": False}), "target drift")
                state = snapshot(page)
                if state["challenge"]:
                    need(client.op({"op": "freeze", "declared_by": "tori-goru-quasars-dr-monitor", "reason": "real page-content challenge during Quasars DR run"}), "freeze")
                    raise RuntimeError("page challenge: broker frozen")
                need(client.op({"op": "check", "lease_id": lease["lease_id"], "epoch": lease["epoch"], "action": "read-only poll exact Quasars DR conversation", "target_verified": True}), "monitor check")
                need(client.op({"op": "heartbeat", "lease_id": lease["lease_id"]}), "monitor heartbeat")
                lengths = [len(x["text"]) for x in state["messages"]]
                print(json.dumps({"messages": len(lengths), "lengths": lengths, "stop": state["stopVisible"], "research": state["researchVisible"]}, sort_keys=True), flush=True)
                last_text = state["messages"][-1]["text"] if state["messages"] else ""
                candidate = len(lengths) >= 3 and lengths[-1] >= 1500 and not state["stopVisible"] and not state["researchVisible"] and "I'll let you know when your research is done" not in last_text
                if candidate:
                    digest = hashlib.sha256(last_text.encode()).hexdigest()
                    time.sleep(20)
                    if not target_ok():
                        need(client.op({"op": "check", "lease_id": lease["lease_id"], "epoch": lease["epoch"], "action": "confirm stable Quasars DR result", "target_verified": False}), "stable target drift")
                    stable = snapshot(page)
                    stable_text = stable["messages"][-1]["text"] if stable["messages"] else ""
                    stable_digest = hashlib.sha256(stable_text.encode()).hexdigest()
                    if not stable["challenge"] and not stable["stopVisible"] and not stable["researchVisible"] and len(stable.get("messages", [])) >= 3 and digest == stable_digest:
                        print(json.dumps({"candidate_complete": True, "conversation_id": IDENTITY["conversation_id"], "result_chars": len(stable_text), "result_sha256": stable_digest}, sort_keys=True), flush=True)
                        return
                time.sleep(20)
            raise RuntimeError("Quasars DR monitor timed out after 2700 seconds")
    finally:
        if lease is not None:
            with suppress(Exception): print(json.dumps({"monitor_release": client.op({"op": "release", "lease_id": lease["lease_id"]})}, sort_keys=True), flush=True)
        client.close()


if __name__ == "__main__": main()
