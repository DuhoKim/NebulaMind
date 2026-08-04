import hashlib
import json
import sys
import urllib.request
from contextlib import suppress
from pathlib import Path
from urllib.parse import urlparse

sys.path.insert(0, "broker")
import ledger
from transport import UDSClient
from playwright.sync_api import sync_playwright

SOCK = "/tmp/nmbrk-live-20260714/b.sock"
BASE = "http://127.0.0.1:19223"
TARGET_ID = "C92443095EE9116210C178D855DF3329"
IDENTITY_PATH = Path("receipts/GORU_DR_PROVEFIRST_QUASARS_RUN_IDENTITY.json")
RESULT_PATH = Path("receipts/GORU_DR_PROVEFIRST_QUASARS_RESULT.md")
META_PATH = Path("receipts/GORU_DR_PROVEFIRST_QUASARS_RESULT_METADATA.json")
EXPECTED = {
    RESULT_PATH: "cd65f4eed3aa5615104a50877a489379233905d3a4a7121b19abcc9099210694",
    META_PATH: "92a16b27ebbe7815836c7b965db1e1be1b85a28050a7c3b563e2fc855fd7f4b9",
    IDENTITY_PATH: "e34aaeb2c8414061955b3d44d9d955bef852216a22fec46c606ce6e3c149485f",
}
SAVE_EPOCH = 582
SAVE_ENTRY = "f23e9690dbaca4e547403d56fc65d805f08236cdbd9bc47460489ee2fa5dbcec"
SCOPE = {"host_id": "pro", "bundle": "com.google.Chrome", "user_data_dir": "dr-live-cdp-20260714", "window_id": "pid-65195", "target_id": TARGET_ID}


def need(resp, name):
    if not resp.get("ok"):
        raise RuntimeError(f"{name}: {resp}")
    return resp


def target_path():
    with urllib.request.urlopen(f"{BASE}/json/list", timeout=3) as response:
        pages = json.load(response)
    hits = [x for x in pages if x.get("id") == TARGET_ID and x.get("type") == "page"]
    if len(hits) != 1:
        return None
    parsed = urlparse(hits[0].get("url", ""))
    return parsed.path if parsed.scheme == "https" and parsed.netloc == "gemini.google.com" else None


def challenge(page):
    return page.evaluate("""() => {const v=e=>{const s=getComputedStyle(e),r=e.getBoundingClientRect();return s.display!=='none'&&s.visibility!=='hidden'&&r.width>0&&r.height>0};const d=[...document.querySelectorAll('[role=dialog],dialog')].filter(v).map(e=>(e.innerText||'').slice(0,500));return location.hostname==='accounts.google.com'||[...document.querySelectorAll('input[type=password]')].some(v)||[...document.querySelectorAll('iframe')].some(e=>/recaptcha|captcha/i.test(e.src||''))||d.some(t=>/captcha|verify|verification|sign in|two-step|2-step|unusual activity|permission|challenge/i.test(t))}""")


def custody(identity):
    for path, expected in EXPECTED.items():
        if hashlib.sha256(path.read_bytes()).hexdigest() != expected:
            raise RuntimeError(f"custody hash mismatch: {path}")
    ok, msg = ledger.verify(Path("ledger/RUN_LEDGER.jsonl"))
    if not ok:
        raise RuntimeError(f"ledger invalid: {msg}")
    entries = ledger.read_entries(Path("ledger/RUN_LEDGER.jsonl"))
    saved = next((x for x in entries if x.get("epoch") == SAVE_EPOCH), None)
    if not saved or saved.get("type") != "dr_provefirst_quasars_result_saved_verified" or saved.get("entry_sha256") != SAVE_ENTRY:
        raise RuntimeError("verified result-save ledger entry absent")
    if identity.get("conversation_id") != "116a89ea5f3eae3a" or identity.get("submit_utc") != "2026-07-14T11:07:37.629377Z":
        raise RuntimeError("identity mismatch")


def main():
    identity = json.loads(IDENTITY_PATH.read_text()); path = identity["conversation_path"]
    custody(identity)
    if target_path() != path:
        raise RuntimeError("exact Quasars target failed before delete preflight")
    client = UDSClient(SOCK); lease = None
    try:
        lease = need(client.op({"op": "acquire", "holder": "tori-goru-quasars-delete-preflight", "kind": "target", "mode": "write", "scope": SCOPE, "ttl": 180, "heartbeat_interval": 45}), "target acquire")["lease"]
        with sync_playwright() as p:
            browser = p.chromium.connect_over_cdp(BASE)
            pages = [pg for ctx in browser.contexts for pg in ctx.pages if urlparse(pg.url).path == path]
            if len(pages) != 1:
                raise RuntimeError(f"exact delete preflight page count {len(pages)}")
            page = pages[0]
            if challenge(page):
                need(client.op({"op": "freeze", "declared_by": "tori-goru-quasars-delete-preflight", "reason": "real page-content challenge before Quasars exact-own deletion"}), "freeze")
                raise RuntimeError("page challenge: broker frozen")
            open_sidebar = page.get_by_label("Open sidebar", exact=True)
            if open_sidebar.count() == 1 and open_sidebar.is_visible():
                need(client.op({"op": "check", "lease_id": lease["lease_id"], "epoch": lease["epoch"], "action": "open sidebar for exact Quasars delete preflight", "target_verified": target_path() == path}), "open sidebar check")
                open_sidebar.click(); page.wait_for_timeout(700)
            link = page.locator(f'a[href="{path}"]')
            visible = [link.nth(i) for i in range(link.count()) if link.nth(i).is_visible()]
            if len(visible) != 1:
                raise RuntimeError(f"exact Quasars history row count {len(visible)}")
            row = visible[0]; current_title = (row.inner_text() or "").strip().replace("\n", " ")
            if not current_title:
                raise RuntimeError("exact Quasars row title empty")
            row.hover(); page.wait_for_timeout(500)
            parent = row.locator("xpath=..")
            buttons = [parent.locator("button").nth(i) for i in range(parent.locator("button").count()) if parent.locator("button").nth(i).is_visible()]
            if len(buttons) != 1:
                raise RuntimeError(f"exact row option button count {len(buttons)}")
            options_label = buttons[0].get_attribute("aria-label") or ""
            if not options_label.startswith("More options for "):
                raise RuntimeError(f"unexpected exact-row options label {options_label}")
            need(client.op({"op": "check", "lease_id": lease["lease_id"], "epoch": lease["epoch"], "action": "open options for exact Quasars run-owned conversation 116a89ea5f3eae3a", "target_verified": target_path() == path}), "options check")
            buttons[0].click(); page.wait_for_timeout(500)
            items = page.get_by_role("menuitem"); menu = [(items.nth(i).inner_text() or "").strip() for i in range(items.count()) if items.nth(i).is_visible()]
            if menu.count("Delete") != 1:
                raise RuntimeError(f"Delete menu item is not unique: {menu}")
            need(client.op({"op": "check", "lease_id": lease["lease_id"], "epoch": lease["epoch"], "action": "close exact Quasars delete preflight menu without mutation", "target_verified": target_path() == path}), "escape check")
            page.keyboard.press("Escape"); page.wait_for_timeout(300)
            print(json.dumps({"conversation_id": identity["conversation_id"], "captured_title": identity["conversation_title"], "current_title": current_title, "options_label": options_label, "menu_items": menu, "submit_utc": identity["submit_utc"], "save_epoch": SAVE_EPOCH, "page_challenge": False}, sort_keys=True))
    finally:
        if lease is not None:
            with suppress(Exception): print(json.dumps({"delete_preflight_target_release": client.op({"op": "release", "lease_id": lease["lease_id"]})}, sort_keys=True))
        client.close()


if __name__ == "__main__": main()
