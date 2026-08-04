import json
import sys
import urllib.request
from contextlib import suppress

sys.path.insert(0, "broker")
from transport import UDSClient
from playwright.sync_api import sync_playwright

SOCK = "/tmp/nmbrk-live-20260714/b.sock"
BASE = "http://127.0.0.1:19223"
TARGET_ID = "C92443095EE9116210C178D855DF3329"
PROMPT = "Using official Apple and Google Chrome documentation, explain in no more than eight bullets how a direct Thunderbolt Bridge between two Macs can support isolated browser automation. Include two limitations and source links."
SCOPE = {"host_id": "pro", "bundle": "com.google.Chrome", "user_data_dir": "dr-live-cdp-20260714", "window_id": "pid-65195", "target_id": TARGET_ID}


def need(resp, name):
    if not resp.get("ok"):
        raise RuntimeError(f"{name}: {resp}")
    return resp


def target_ok():
    with urllib.request.urlopen(f"{BASE}/json/list", timeout=3) as response:
        pages = json.load(response)
    return sum(1 for x in pages if x.get("id") == TARGET_ID and x.get("type") == "page" and x.get("url") == "https://gemini.google.com/app") == 1


def challenge(page):
    return page.evaluate("""() => {
      const v=e=>{const s=getComputedStyle(e),r=e.getBoundingClientRect();return s.display!=='none'&&s.visibility!=='hidden'&&r.width>0&&r.height>0};
      const d=[...document.querySelectorAll('[role=dialog],dialog')].filter(v).map(e=>(e.innerText||'').slice(0,500));
      return location.hostname==='accounts.google.com'||[...document.querySelectorAll('input[type=password]')].some(v)||[...document.querySelectorAll('iframe')].some(e=>/recaptcha|captcha/i.test(e.src||''))||d.some(t=>/captcha|verify|verification|sign in|two-step|2-step|unusual activity|permission|challenge/i.test(t));
    }""")


def main():
    client = UDSClient(SOCK)
    lease = None
    try:
        if not target_ok():
            raise RuntimeError("exact initial target failed")
        lease = need(client.op({"op": "acquire", "holder": "tori-goru-dr-stage", "kind": "target", "mode": "write", "scope": SCOPE, "ttl": 180, "heartbeat_interval": 45}), "acquire")["lease"]
        with sync_playwright() as p:
            browser = p.chromium.connect_over_cdp(BASE)
            pages = [pg for ctx in browser.contexts for pg in ctx.pages if pg.url == "https://gemini.google.com/app"]
            if len(pages) != 1:
                raise RuntimeError(f"Gemini page count {len(pages)}")
            page = pages[0]
            if challenge(page):
                need(client.op({"op": "freeze", "declared_by": "tori-goru-dr-stage", "reason": "page challenge during DR stage"}), "freeze")
                raise RuntimeError("page challenge")
            need(client.op({"op": "check", "lease_id": lease["lease_id"], "epoch": lease["epoch"], "action": "open Upload & tools", "target_verified": target_ok()}), "check menu")
            tool = page.get_by_label("Upload & tools", exact=True)
            if tool.count() != 1 or not tool.is_visible():
                raise RuntimeError("tools control not unique visible")
            tool.click()
            page.wait_for_timeout(500)
            deep = page.get_by_text("Deep research", exact=True)
            visible = [deep.nth(i) for i in range(deep.count()) if deep.nth(i).is_visible()]
            if len(visible) != 1:
                raise RuntimeError(f"Deep research exact visible count {len(visible)}")
            need(client.op({"op": "check", "lease_id": lease["lease_id"], "epoch": lease["epoch"], "action": "select exact Deep research tool", "target_verified": target_ok()}), "check deep research")
            visible[0].click()
            page.wait_for_timeout(700)
            mode_labels = page.locator("button:visible,[role=button]:visible").evaluate_all("els=>els.map(e=>(e.getAttribute('aria-label')||e.innerText||'').trim().replace(/\\s+/g,' ')).filter(x=>/deep research/i.test(x)).slice(0,20)")
            if not mode_labels:
                raise RuntimeError("Deep research mode not visibly confirmed")
            editor = page.get_by_role("textbox", name="Enter a prompt for Gemini", exact=True)
            if editor.count() != 1 or not editor.is_visible():
                raise RuntimeError("prompt editor not unique visible")
            need(client.op({"op": "check", "lease_id": lease["lease_id"], "epoch": lease["epoch"], "action": "fill bounded DR prompt", "target_verified": target_ok()}), "check fill")
            editor.fill(PROMPT)
            page.wait_for_timeout(400)
            controls = page.locator("button:visible,[role=button]:visible").evaluate_all("els=>els.map(e=>({label:(e.getAttribute('aria-label')||e.getAttribute('title')||e.innerText||'').trim().replace(/\\s+/g,' '),disabled:!!e.disabled})).filter(x=>/send|submit|research|start|create/i.test(x.label)).slice(0,30)")
            print(json.dumps({"staged": True, "target_id": TARGET_ID, "page_challenge": False, "mode_labels": mode_labels, "submit_candidates": controls}, sort_keys=True))
    finally:
        if lease is not None:
            with suppress(Exception):
                print(json.dumps({"release": client.op({"op": "release", "lease_id": lease["lease_id"]})}, sort_keys=True))
        client.close()


if __name__ == "__main__":
    main()
