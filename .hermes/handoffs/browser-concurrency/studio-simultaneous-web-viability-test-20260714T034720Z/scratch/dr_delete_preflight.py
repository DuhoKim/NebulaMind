import json
import sys
import urllib.request
from contextlib import suppress
from urllib.parse import urlparse

sys.path.insert(0, "broker")
from transport import UDSClient
from playwright.sync_api import sync_playwright

SOCK = "/tmp/nmbrk-live-20260714/b.sock"
BASE = "http://127.0.0.1:19223"
TARGET_ID = "C92443095EE9116210C178D855DF3329"
PATH = "/app/8af765be7d623416"
SCOPE = {"host_id": "pro", "bundle": "com.google.Chrome", "user_data_dir": "dr-live-cdp-20260714", "window_id": "pid-65195", "target_id": TARGET_ID}


def need(r, name):
    if not r.get("ok"):
        raise RuntimeError(f"{name}: {r}")
    return r


def target_ok():
    with urllib.request.urlopen(f"{BASE}/json/list", timeout=3) as response:
        targets = json.load(response)
    hits = [x for x in targets if x.get("id") == TARGET_ID and x.get("type") == "page"]
    return len(hits) == 1 and urlparse(hits[0].get("url", "")).path == PATH and urlparse(hits[0].get("url", "")).netloc == "gemini.google.com"


def main():
    if not target_ok():
        raise RuntimeError("exact delete target preflight failed")
    client = UDSClient(SOCK); lease = None
    try:
        lease = need(client.op({"op": "acquire", "holder": "tori-goru-dr-delete-preflight", "kind": "target", "mode": "write", "scope": SCOPE, "ttl": 120, "heartbeat_interval": 45}), "acquire")["lease"]
        with sync_playwright() as p:
            browser = p.chromium.connect_over_cdp(BASE)
            pages = [pg for ctx in browser.contexts for pg in ctx.pages if urlparse(pg.url).path == PATH]
            if len(pages) != 1: raise RuntimeError(f"page count {len(pages)}")
            page = pages[0]
            challenge = page.evaluate("""() => {const v=e=>{const s=getComputedStyle(e),r=e.getBoundingClientRect();return s.display!=='none'&&s.visibility!=='hidden'&&r.width>0&&r.height>0};const d=[...document.querySelectorAll('[role=dialog],dialog')].filter(v).map(e=>(e.innerText||'').slice(0,500));return location.hostname==='accounts.google.com'||[...document.querySelectorAll('input[type=password]')].some(v)||[...document.querySelectorAll('iframe')].some(e=>/recaptcha|captcha/i.test(e.src||''))||d.some(t=>/captcha|verify|verification|sign in|two-step|2-step|unusual activity|permission|challenge/i.test(t))}""")
            if challenge:
                need(client.op({"op": "freeze", "declared_by": "tori-goru-dr-delete-preflight", "reason": "real page challenge before exact-own deletion"}), "freeze")
                raise RuntimeError("challenge")
            open_sidebar = page.get_by_label("Open sidebar", exact=True)
            if open_sidebar.count() == 1 and open_sidebar.is_visible():
                need(client.op({"op": "check", "lease_id": lease["lease_id"], "epoch": lease["epoch"], "action": "open Gemini sidebar for exact-own deletion preflight", "target_verified": target_ok()}), "open sidebar check")
                open_sidebar.click(); page.wait_for_timeout(700)
            rows = page.evaluate("""path => {const v=e=>{const s=getComputedStyle(e),r=e.getBoundingClientRect();return s.display!=='none'&&s.visibility!=='hidden'&&r.width>0&&r.height>0};const label=e=>(e.getAttribute('aria-label')||e.getAttribute('title')||e.innerText||'').trim().replace(/\\s+/g,' ').slice(0,220);const links=[...document.querySelectorAll('a[href]')].filter(v).filter(a=>{try{return new URL(a.href).pathname===path}catch{return false}});return links.map(a=>{let n=a,anc=[];for(let i=0;i<6&&n;i++,n=n.parentElement){anc.push({tag:n.tagName,label:label(n),cls:(n.className||'').toString().slice(0,160),buttons:[...n.querySelectorAll(':scope > button,:scope > [role=button]')].filter(v).map(label)})}return{linkLabel:label(a),href:a.href,ancestors:anc}})}""", PATH)
            exact_link = page.locator(f'a[href="{PATH}"]')
            if exact_link.count() != 1 or not exact_link.is_visible():
                raise RuntimeError(f"exact owned conversation link count {exact_link.count()}")
            need(client.op({"op": "check", "lease_id": lease["lease_id"], "epoch": lease["epoch"], "action": "hover exact run-owned Gemini conversation row for deletion preflight", "target_verified": target_ok()}), "hover exact row check")
            exact_link.hover(); page.wait_for_timeout(500)
            hovered = exact_link.evaluate("""a => {const v=e=>{const s=getComputedStyle(e),r=e.getBoundingClientRect();return s.display!=='none'&&s.visibility!=='hidden'&&r.width>0&&r.height>0};const label=e=>(e.getAttribute('aria-label')||e.getAttribute('title')||e.innerText||'').trim().replace(/\\s+/g,' ').slice(0,220);let n=a,out=[];for(let i=0;i<5&&n;i++,n=n.parentElement){out.push({tag:n.tagName,label:label(n),buttons:[...n.querySelectorAll('button,[role=button]')].filter(v).map(label)})}return out}""")
            nav_item = exact_link.locator("xpath=..")
            options = nav_item.locator("button:visible")
            if options.count() != 1 or not (options.get_attribute("aria-label") or "").startswith("More options for "):
                raise RuntimeError(f"exact-row options count {options.count()}")
            need(client.op({"op": "check", "lease_id": lease["lease_id"], "epoch": lease["epoch"], "action": "open options menu for exact run-owned Gemini conversation", "target_verified": target_ok()}), "open exact options check")
            options.click(); page.wait_for_timeout(500)
            menu_items = page.locator('[role="menuitem"]:visible').evaluate_all("els=>els.map(e=>(e.getAttribute('aria-label')||e.innerText||'').trim().replace(/\\s+/g,' '))")
            need(client.op({"op": "check", "lease_id": lease["lease_id"], "epoch": lease["epoch"], "action": "close exact-own deletion preflight menu without mutation", "target_verified": target_ok()}), "close menu check")
            page.keyboard.press("Escape")
            print(json.dumps({"exact_rows": rows, "hovered_ancestors": hovered, "menu_items": menu_items, "challenge": False, "target_id": TARGET_ID}, sort_keys=True))
    finally:
        if lease is not None:
            with suppress(Exception): print(json.dumps({"release": client.op({"op": "release", "lease_id": lease["lease_id"]})}, sort_keys=True))
        client.close()


if __name__ == "__main__": main()
