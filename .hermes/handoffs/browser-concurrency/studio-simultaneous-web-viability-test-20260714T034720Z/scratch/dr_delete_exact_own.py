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
import ledger
from playwright.sync_api import sync_playwright

SOCK = "/tmp/nmbrk-live-20260714/b.sock"
BASE = "http://127.0.0.1:19223"
TARGET_ID = "C92443095EE9116210C178D855DF3329"
PATH = "/app/8af765be7d623416"
IDENTITY_PATH = Path("receipts/GORU_DR_RUN_IDENTITY.json")
RESULT_PATH = Path("receipts/GORU_DR_RESULT.md")
METADATA_PATH = Path("receipts/GORU_DR_RESULT_METADATA.json")
EVIDENCE_PATH = Path("receipts/GORU_DR_EXACT_OWN_DELETION.json")
LEDGER_PATH = Path("ledger/RUN_LEDGER.jsonl")
EXPECTED = {
    RESULT_PATH: "84f3ebfee6ddc51fbfdbc918911fd1977f7943c7ddd5837e69c7784a12aed755",
    METADATA_PATH: "17e137def32fb920662ed61de1d0f7f26bf88520ec3a33384cc4697082ccc13f",
    IDENTITY_PATH: "69bc9899ee044326ec97b5ef1f1bc2971557c6964e5f69dfa0dfeb3f42957fee",
}
SAVE_EPOCH = 220
SAVE_ENTRY_SHA = "3380829d0daf5f92c31086fce2870b18191841c0cdf1c7f214dea1139068c47d"
SCOPE = {"host_id": "pro", "bundle": "com.google.Chrome", "user_data_dir": "dr-live-cdp-20260714", "window_id": "pid-65195", "target_id": TARGET_ID}


def need(resp, name):
    if not resp.get("ok"):
        raise RuntimeError(f"{name}: {resp}")
    return resp


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def target_path():
    with urllib.request.urlopen(f"{BASE}/json/list", timeout=3) as response:
        targets = json.load(response)
    hits = [x for x in targets if x.get("id") == TARGET_ID and x.get("type") == "page"]
    if len(hits) != 1:
        return None
    parsed = urlparse(hits[0].get("url", ""))
    if parsed.scheme != "https" or parsed.netloc != "gemini.google.com":
        return None
    return parsed.path


def page_challenge(page):
    return page.evaluate("""() => {const v=e=>{const s=getComputedStyle(e),r=e.getBoundingClientRect();return s.display!=='none'&&s.visibility!=='hidden'&&r.width>0&&r.height>0};const d=[...document.querySelectorAll('[role=dialog],dialog')].filter(v).map(e=>(e.innerText||'').slice(0,500));return location.hostname==='accounts.google.com'||[...document.querySelectorAll('input[type=password]')].some(v)||[...document.querySelectorAll('iframe')].some(e=>/recaptcha|captcha/i.test(e.src||''))||d.some(t=>/captcha|verify|verification|sign in|two-step|2-step|unusual activity|permission|challenge/i.test(t))}""")


def preflight_custody(identity):
    if EVIDENCE_PATH.exists():
        raise RuntimeError("deletion evidence already exists")
    for path, expected in EXPECTED.items():
        if digest(path) != expected:
            raise RuntimeError(f"custody hash mismatch: {path}")
    ok, msg = ledger.verify(LEDGER_PATH)
    if not ok:
        raise RuntimeError(f"ledger verify failed: {msg}")
    entries = ledger.read_entries(LEDGER_PATH)
    if len(entries) <= SAVE_EPOCH:
        raise RuntimeError("verified result-save epoch missing")
    saved = entries[SAVE_EPOCH]
    if saved.get("entry_sha256") != SAVE_ENTRY_SHA or saved.get("type") != "dr_result_saved_verified":
        raise RuntimeError("verified result-save ledger identity mismatch")
    files = saved.get("payload", {}).get("files", {})
    if files.get(str(RESULT_PATH)) != EXPECTED[RESULT_PATH] or identity["conversation_id"] not in saved.get("payload", {}).get("note", ""):
        raise RuntimeError("verified result-save payload mismatch")
    if identity.get("conversation_id") != PATH.removeprefix("/app/") or not identity.get("conversation_title") or not identity.get("submit_utc") or not identity.get("prompt"):
        raise RuntimeError("conversation identity incomplete")


def main():
    identity = json.loads(IDENTITY_PATH.read_text())
    preflight_custody(identity)
    if target_path() != PATH:
        raise RuntimeError("exact run-owned conversation target is not current")
    client = UDSClient(SOCK); lease = None
    try:
        lease = need(client.op({"op": "acquire", "holder": "tori-goru-dr-delete-exact-own", "kind": "target", "mode": "write", "scope": SCOPE, "ttl": 180, "heartbeat_interval": 45}), "delete target acquire")["lease"]
        with sync_playwright() as p:
            browser = p.chromium.connect_over_cdp(BASE)
            pages = [pg for ctx in browser.contexts for pg in ctx.pages if urlparse(pg.url).path == PATH]
            if len(pages) != 1:
                raise RuntimeError(f"exact owned page count {len(pages)}")
            page = pages[0]
            if page_challenge(page):
                need(client.op({"op": "freeze", "declared_by": "tori-goru-dr-delete-exact-own", "reason": "real page-content challenge before exact-own conversation deletion"}), "freeze")
                raise RuntimeError("page challenge: broker frozen")
            open_sidebar = page.get_by_label("Open sidebar", exact=True)
            if open_sidebar.count() == 1 and open_sidebar.is_visible():
                need(client.op({"op": "check", "lease_id": lease["lease_id"], "epoch": lease["epoch"], "action": "open sidebar for exact run-owned conversation deletion", "target_verified": target_path() == PATH}), "open sidebar check")
                open_sidebar.click(); page.wait_for_timeout(600)
            exact_link = page.locator(f'a[href="{PATH}"]')
            if exact_link.count() != 1 or not exact_link.is_visible():
                raise RuntimeError(f"exact run-owned history row count {exact_link.count()}")
            current_title = (exact_link.inner_text() or "").strip().replace("\n", " ")
            current_title = " ".join(current_title.split())
            if not current_title or not identity["prompt"].startswith(current_title) or not current_title.startswith(identity["conversation_title"]):
                raise RuntimeError("current row title does not positively match captured run identity")
            exact_link.hover(); page.wait_for_timeout(400)
            nav_item = exact_link.locator("xpath=..")
            options = nav_item.locator("button:visible")
            if options.count() != 1 or (options.get_attribute("aria-label") or "") != f"More options for {current_title}":
                raise RuntimeError("exact row options identity mismatch")
            need(client.op({"op": "check", "lease_id": lease["lease_id"], "epoch": lease["epoch"], "action": f"open options for exact run-owned conversation {identity['conversation_id']}", "target_verified": target_path() == PATH}), "open exact options check")
            options.click(); page.wait_for_timeout(400)
            delete_item = page.get_by_role("menuitem", name="Delete", exact=True)
            if delete_item.count() != 1 or not delete_item.is_visible():
                raise RuntimeError(f"exact Delete menu item count {delete_item.count()}")
            if page_challenge(page):
                need(client.op({"op": "freeze", "declared_by": "tori-goru-dr-delete-exact-own", "reason": "real page-content challenge in exact-own delete menu"}), "freeze")
                raise RuntimeError("page challenge: broker frozen")
            need(client.op({"op": "check", "lease_id": lease["lease_id"], "epoch": lease["epoch"], "action": f"choose Delete only for exact run-owned conversation {identity['conversation_id']} after verified save epoch {SAVE_EPOCH}", "target_verified": target_path() == PATH}), "choose exact delete check")
            delete_item.click(); page.wait_for_timeout(500)
            confirmation_mode = "direct"
            dialog_text = ""
            dialogs = page.locator('[role="dialog"]:visible')
            if dialogs.count() == 1:
                dialog = dialogs.first
                dialog_text = " ".join((dialog.inner_text() or "").split())[:500]
                if "delete" not in dialog_text.lower() or not any(word in dialog_text.lower() for word in ("chat", "conversation", "activity")):
                    raise RuntimeError("unexpected deletion confirmation dialog")
                confirm = dialog.get_by_role("button", name="Delete", exact=True)
                cancel = dialog.get_by_role("button", name="Cancel", exact=True)
                if confirm.count() != 1 or cancel.count() != 1 or not confirm.is_visible():
                    raise RuntimeError("deletion confirmation controls not exact")
                if target_path() != PATH or page_challenge(page):
                    raise RuntimeError("target or challenge changed before exact delete confirmation")
                need(client.op({"op": "check", "lease_id": lease["lease_id"], "epoch": lease["epoch"], "action": f"confirm deletion only for exact run-owned conversation {identity['conversation_id']} after receipt {EXPECTED[RESULT_PATH]}", "target_verified": True}), "confirm exact delete check")
                confirm.click(); confirmation_mode = "dialog"
            page.wait_for_timeout(1500)
            post_path = target_path()
            if post_path is None or post_path == PATH:
                raise RuntimeError(f"exact conversation still current after deletion: {post_path}")
            if page.locator(f'a[href="{PATH}"]').count() != 0:
                raise RuntimeError("exact run-owned history row still exists after deletion")
            deleted_utc = datetime.now(timezone.utc).isoformat().replace("+00:00", "Z")
            evidence = {
                "conversation_id": identity["conversation_id"],
                "captured_title": identity["conversation_title"],
                "deletion_match_title": current_title,
                "submit_utc": identity["submit_utc"],
                "deleted_utc": deleted_utc,
                "target_id": TARGET_ID,
                "pre_delete_path": PATH,
                "post_delete_path": post_path,
                "confirmation_mode": confirmation_mode,
                "confirmation_dialog": dialog_text,
                "verified_result_receipt": str(RESULT_PATH),
                "verified_result_receipt_sha256": EXPECTED[RESULT_PATH],
                "verified_result_save_epoch": SAVE_EPOCH,
                "verified_result_save_entry_sha256": SAVE_ENTRY_SHA,
                "bulk_delete_used": False,
                "unrelated_conversation_touched": False,
            }
            EVIDENCE_PATH.write_text(json.dumps(evidence, indent=2, sort_keys=True) + "\n")
            print(json.dumps(evidence, sort_keys=True))
    finally:
        if lease is not None:
            with suppress(Exception): print(json.dumps({"delete_target_release": client.op({"op": "release", "lease_id": lease["lease_id"]})}, sort_keys=True))
        client.close()


if __name__ == "__main__": main()
