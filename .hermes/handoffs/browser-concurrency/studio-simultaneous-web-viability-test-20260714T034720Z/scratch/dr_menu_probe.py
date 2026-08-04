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
PROFILE = "dr-live-cdp-20260714"
SCOPE = {
    "host_id": "pro",
    "bundle": "com.google.Chrome",
    "user_data_dir": PROFILE,
    "window_id": "pid-65195",
    "target_id": TARGET_ID,
}


def require(resp, what):
    if not resp.get("ok"):
        raise RuntimeError(f"{what} denied: {resp}")
    return resp


def target_info():
    with urllib.request.urlopen(f"{BASE}/json/list", timeout=3) as response:
        pages = json.load(response)
    matches = [p for p in pages if p.get("type") == "page" and p.get("id") == TARGET_ID]
    if len(matches) != 1:
        return None
    p = matches[0]
    if p.get("url") != "https://gemini.google.com/app":
        return None
    return p


def challenge(page):
    return page.evaluate("""() => {
      const visible = (el) => {
        const s = getComputedStyle(el); const r = el.getBoundingClientRect();
        return s.display !== 'none' && s.visibility !== 'hidden' && r.width > 0 && r.height > 0;
      };
      const dialogs = [...document.querySelectorAll('[role=dialog],dialog')].filter(visible)
        .map(el => (el.innerText || '').replace(/\\s+/g, ' ').slice(0, 500));
      const dialogSignal = dialogs.some(t => /captcha|verify|verification|sign in|two-step|2-step|unusual activity|permission|challenge/i.test(t));
      return location.hostname === 'accounts.google.com'
        || [...document.querySelectorAll('input[type=password]')].some(visible)
        || [...document.querySelectorAll('iframe')].some(el => /recaptcha|captcha/i.test(el.src || ''))
        || dialogSignal;
    }""")


def main():
    client = UDSClient(SOCK)
    lease = None
    opened = False
    try:
        if target_info() is None:
            raise RuntimeError("exact target preflight failed")
        lease = require(client.op({
            "op": "acquire", "holder": "tori-goru-dr-menu-probe", "kind": "target",
            "mode": "write", "scope": SCOPE, "ttl": 120.0, "heartbeat_interval": 45.0,
        }), "target acquire")["lease"]
        with sync_playwright() as p:
            browser = p.chromium.connect_over_cdp(BASE)
            matches = [pg for ctx in browser.contexts for pg in ctx.pages if pg.url == "https://gemini.google.com/app"]
            if len(matches) != 1:
                raise RuntimeError(f"expected one exact Gemini page, got {len(matches)}")
            page = matches[0]
            if challenge(page):
                require(client.op({"op": "freeze", "declared_by": "tori-goru-dr-menu-probe", "reason": "real page-content challenge during DR menu probe"}), "freeze")
                raise RuntimeError("page challenge: broker frozen")
            deep = page.get_by_text("Deep Research", exact=True)
            visible_deep = [deep.nth(i) for i in range(deep.count()) if deep.nth(i).is_visible()]
            if not visible_deep:
                if target_info() is None:
                    require(client.op({"op": "check", "lease_id": lease["lease_id"], "epoch": lease["epoch"], "action": "open Upload & tools", "target_verified": False}), "target drift")
                require(client.op({"op": "check", "lease_id": lease["lease_id"], "epoch": lease["epoch"], "action": "open Upload & tools", "target_verified": True}), "open menu check")
                tool = page.get_by_label("Upload & tools", exact=True)
                if tool.count() != 1 or not tool.is_visible():
                    raise RuntimeError("Upload & tools is not one unique visible control")
                tool.click()
                opened = True
                page.wait_for_timeout(500)
                visible_deep = [deep.nth(i) for i in range(deep.count()) if deep.nth(i).is_visible()]
            labels = page.locator("button:visible,[role=menuitem]:visible,[role=option]:visible").evaluate_all("""els => els.map(el => (el.getAttribute('aria-label') || el.innerText || '').trim().replace(/\\s+/g,' ')).filter(x => /research|tools?/i.test(x)).slice(0,30)""")
            print(json.dumps({"target_id": TARGET_ID, "page_challenge": False, "deep_research_visible_exact_count": len(visible_deep), "relevant_visible_labels": labels}, sort_keys=True))
            if opened:
                if target_info() is None:
                    require(client.op({"op": "check", "lease_id": lease["lease_id"], "epoch": lease["epoch"], "action": "close Upload & tools", "target_verified": False}), "target drift")
                require(client.op({"op": "check", "lease_id": lease["lease_id"], "epoch": lease["epoch"], "action": "close Upload & tools", "target_verified": True}), "close menu check")
                page.get_by_label("Upload & tools", exact=True).click()
    finally:
        if lease is not None:
            with suppress(Exception):
                print(json.dumps({"release": client.op({"op": "release", "lease_id": lease["lease_id"]})}, sort_keys=True))
        client.close()


if __name__ == "__main__":
    main()
