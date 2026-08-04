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
IDENTITY_PATH = Path("receipts/GORU_DR_PROVEFIRST_QUASARS_RUN_IDENTITY.json")
PROMPT_SHA = "6d3b61d77e50aab1dd341d5a4c52c9bd07845f64b465d6da3d5e339bc1e0f5d9"
SCOPE = {"host_id": "pro", "bundle": "com.google.Chrome", "user_data_dir": "dr-live-cdp-20260714", "window_id": "pid-65195", "target_id": TARGET_ID}


def need(resp, name):
    if not resp.get("ok"):
        raise RuntimeError(f"{name}: {resp}")
    return resp


def target_exact(path):
    with urllib.request.urlopen(f"{BASE}/json/list", timeout=3) as response:
        pages = json.load(response)
    hits = [x for x in pages if x.get("id") == TARGET_ID and x.get("type") == "page"]
    if len(hits) != 1:
        return None
    parsed = urlparse(hits[0].get("url", ""))
    return hits[0] if parsed.scheme == "https" and parsed.netloc == "gemini.google.com" and parsed.path == path else None


def challenge(page):
    return page.evaluate("""() => {const v=e=>{const s=getComputedStyle(e),r=e.getBoundingClientRect();return s.display!=='none'&&s.visibility!=='hidden'&&r.width>0&&r.height>0};const d=[...document.querySelectorAll('[role=dialog],dialog')].filter(v).map(e=>(e.innerText||'').slice(0,500));return location.hostname==='accounts.google.com'||[...document.querySelectorAll('input[type=password]')].some(v)||[...document.querySelectorAll('iframe')].some(e=>/recaptcha|captcha/i.test(e.src||''))||d.some(t=>/captcha|verify|verification|sign in|two-step|2-step|unusual activity|permission|challenge/i.test(t))}""")


def freeze(client, reason):
    need(client.op({"op": "freeze", "declared_by": "tori-goru-quasars-dr-start", "reason": reason}), "freeze")
    raise RuntimeError(reason)


def status_labels(page):
    return page.locator("button:visible,[role=button]:visible,div:visible,span:visible").evaluate_all("els=>[...new Set(els.map(e=>(e.getAttribute('aria-label')||e.innerText||'').trim().replace(/\\s+/g,' ')).filter(x=>x&&x.length<180&&/researching|stop researching|stop response|research started|searching|sites|sources/i.test(x)))].slice(0,40)")


def main():
    identity = json.loads(IDENTITY_PATH.read_text())
    path = identity.get("conversation_path")
    if identity.get("target_id") != TARGET_ID or identity.get("prompt_sha256") != PROMPT_SHA or path != f"/app/{identity.get('conversation_id', '')}" or not identity.get("conversation_title") or not identity.get("submit_utc"):
        raise RuntimeError("Quasars conversation identity custody incomplete")
    if "research_start_utc" in identity:
        raise RuntimeError("Quasars research start already recorded")
    if target_exact(path) is None:
        raise RuntimeError("exact Quasars conversation target failed")
    client = UDSClient(SOCK); target_lease = None; submit_lease = None
    try:
        target_lease = need(client.op({"op": "acquire", "holder": "tori-goru-quasars-dr-start", "kind": "target", "mode": "write", "scope": SCOPE, "ttl": 180, "heartbeat_interval": 45}), "target acquire")["lease"]
        with sync_playwright() as p:
            browser = p.chromium.connect_over_cdp(BASE)
            pages = [pg for ctx in browser.contexts for pg in ctx.pages if urlparse(pg.url).path == path]
            if len(pages) != 1:
                raise RuntimeError(f"exact Quasars page count {len(pages)}")
            page = pages[0]
            if challenge(page): freeze(client, "real page-content challenge before Quasars Start research")
            start = page.get_by_text("Start research", exact=True)
            visible = [start.nth(i) for i in range(start.count()) if start.nth(i).is_visible()]
            if len(visible) != 1 or visible[0].is_disabled():
                raise RuntimeError(f"Start research exact enabled visible count {len(visible)}")
            submit_lease = need(client.op({"op": "acquire", "holder": "tori-goru-quasars-dr-start", "kind": "account-submission", "mode": "write", "scope": {}, "ttl": 120, "heartbeat_interval": 45}), "account-submission acquire")["lease"]
            if target_exact(path) is None:
                need(client.op({"op": "check", "lease_id": target_lease["lease_id"], "epoch": target_lease["epoch"], "action": "Start research for exact Quasars prove-first conversation", "target_verified": False}), "target drift")
            if challenge(page): freeze(client, "real page-content challenge immediately before Quasars Start research")
            need(client.op({"op": "check", "lease_id": target_lease["lease_id"], "epoch": target_lease["epoch"], "action": "Start research for exact Quasars prove-first conversation", "target_verified": True}), "target start check")
            need(client.op({"op": "check", "lease_id": submit_lease["lease_id"], "epoch": submit_lease["epoch"], "action": "serialized shared-account submit: Start research for one Quasars prove-first conversation", "target_verified": True}), "account start check")
            start_utc = datetime.now(timezone.utc).isoformat().replace("+00:00", "Z")
            target_lease_id = target_lease["lease_id"]; account_lease_id = submit_lease["lease_id"]
            try:
                visible[0].click()
            finally:
                need(client.op({"op": "release", "lease_id": submit_lease["lease_id"]}), "account-submission release")
                submit_lease = None
            start.wait_for(state="hidden", timeout=30000)
            if target_exact(path) is None:
                need(client.op({"op": "check", "lease_id": target_lease["lease_id"], "epoch": target_lease["epoch"], "action": "confirm exact Quasars research started", "target_verified": False}), "post-start drift")
            if challenge(page): freeze(client, "real page-content challenge after Quasars Start research")
            labels = []
            for _ in range(12):
                labels = status_labels(page)
                if any("research" in value.lower() or "stop response" in value.lower() for value in labels):
                    break
                page.wait_for_timeout(1000)
            if not any("research" in value.lower() or "stop response" in value.lower() for value in labels):
                raise RuntimeError(f"research start not positively confirmed: {labels}")
            identity.update({
                "research_start_utc": start_utc, "research_start_confirmed": True,
                "research_start_target_lease_id": target_lease_id,
                "research_start_account_lease_id": account_lease_id,
                "post_start_status_labels": labels,
            })
            IDENTITY_PATH.write_text(json.dumps(identity, indent=2, sort_keys=True) + "\n")
            print(json.dumps({"conversation_id": identity["conversation_id"], "research_start_utc": start_utc, "status": labels}, sort_keys=True))
    finally:
        if submit_lease is not None:
            with suppress(Exception): client.op({"op": "release", "lease_id": submit_lease["lease_id"]})
        if target_lease is not None:
            with suppress(Exception): print(json.dumps({"target_release": client.op({"op": "release", "lease_id": target_lease["lease_id"]})}, sort_keys=True))
        client.close()


if __name__ == "__main__": main()
