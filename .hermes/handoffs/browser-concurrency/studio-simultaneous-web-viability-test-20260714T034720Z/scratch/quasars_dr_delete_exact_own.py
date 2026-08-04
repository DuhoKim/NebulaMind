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
PATH = "/app/116a89ea5f3eae3a"
IDENTITY_PATH = Path("receipts/GORU_DR_PROVEFIRST_QUASARS_RUN_IDENTITY.json")
RESULT_PATH = Path("receipts/GORU_DR_PROVEFIRST_QUASARS_RESULT.md")
METADATA_PATH = Path("receipts/GORU_DR_PROVEFIRST_QUASARS_RESULT_METADATA.json")
EVIDENCE_PATH = Path("receipts/GORU_DR_PROVEFIRST_QUASARS_EXACT_OWN_DELETION.json")
LEDGER_PATH = Path("ledger/RUN_LEDGER.jsonl")
EXPECTED = {
    RESULT_PATH: "cd65f4eed3aa5615104a50877a489379233905d3a4a7121b19abcc9099210694",
    METADATA_PATH: "92a16b27ebbe7815836c7b965db1e1be1b85a28050a7c3b563e2fc855fd7f4b9",
    IDENTITY_PATH: "e34aaeb2c8414061955b3d44d9d955bef852216a22fec46c606ce6e3c149485f",
}
SAVE_EPOCH = 582
SAVE_ENTRY_SHA = "f23e9690dbaca4e547403d56fc65d805f08236cdbd9bc47460489ee2fa5dbcec"
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
    return parsed.path if parsed.scheme == "https" and parsed.netloc == "gemini.google.com" else None


def page_challenge(page):
    return page.evaluate("""() => {const v=e=>{const s=getComputedStyle(e),r=e.getBoundingClientRect();return s.display!=='none'&&s.visibility!=='hidden'&&r.width>0&&r.height>0};const d=[...document.querySelectorAll('[role=dialog],dialog')].filter(v).map(e=>(e.innerText||'').slice(0,500));return location.hostname==='accounts.google.com'||[...document.querySelectorAll('input[type=password]')].some(v)||[...document.querySelectorAll('iframe')].some(e=>/recaptcha|captcha/i.test(e.src||''))||d.some(t=>/captcha|verify|verification|sign in|two-step|2-step|unusual activity|permission|challenge/i.test(t))}""")


def preflight_custody(identity):
    if EVIDENCE_PATH.exists():
        raise RuntimeError("Quasars deletion evidence already exists")
    for path, expected in EXPECTED.items():
        if digest(path) != expected:
            raise RuntimeError(f"custody hash mismatch: {path}")
    ok, msg = ledger.verify(LEDGER_PATH)
    if not ok:
        raise RuntimeError(f"ledger verify failed: {msg}")
    entries = ledger.read_entries(LEDGER_PATH)
    saved = next((entry for entry in entries if entry.get("epoch") == SAVE_EPOCH), None)
    if not saved or saved.get("entry_sha256") != SAVE_ENTRY_SHA or saved.get("type") != "dr_provefirst_quasars_result_saved_verified":
        raise RuntimeError("verified Quasars result-save ledger identity mismatch")
    files = saved.get("payload", {}).get("files", {})
    if files.get(str(RESULT_PATH)) != EXPECTED[RESULT_PATH] or identity["conversation_id"] not in saved.get("payload", {}).get("note", ""):
        raise RuntimeError("verified Quasars result-save payload mismatch")
    if identity.get("conversation_id") != PATH.removeprefix("/app/") or not identity.get("conversation_title") or not identity.get("submit_utc") or not identity.get("prompt"):
        raise RuntimeError("Quasars conversation identity incomplete")


def main():
    identity = json.loads(IDENTITY_PATH.read_text()); preflight_custody(identity)
    if target_path() != PATH:
        raise RuntimeError("exact Quasars run-owned conversation is not current")
    client = UDSClient(SOCK); lease = None
    try:
        lease = need(client.op({"op": "acquire", "holder": "tori-goru-quasars-delete-exact-own", "kind": "target", "mode": "write", "scope": SCOPE, "ttl": 180, "heartbeat_interval": 45}), "delete target acquire")["lease"]
        with sync_playwright() as p:
            browser = p.chromium.connect_over_cdp(BASE)
            pages = [pg for ctx in browser.contexts for pg in ctx.pages if urlparse(pg.url).path == PATH]
            if len(pages) != 1:
                raise RuntimeError(f"exact Quasars owned page count {len(pages)}")
            page = pages[0]
            if page_challenge(page):
                need(client.op({"op": "freeze", "declared_by": "tori-goru-quasars-delete-exact-own", "reason": "real page-content challenge before Quasars exact-own deletion"}), "freeze")
                raise RuntimeError("page challenge: broker frozen")
            open_sidebar = page.get_by_label("Open sidebar", exact=True)
            if open_sidebar.count() == 1 and open_sidebar.is_visible():
                need(client.op({"op": "check", "lease_id": lease["lease_id"], "epoch": lease["epoch"], "action": "open sidebar for exact Quasars run-owned deletion", "target_verified": target_path() == PATH}), "open sidebar check")
                open_sidebar.click(); page.wait_for_timeout(600)
            exact_link = page.locator(f'a[href="{PATH}"]')
            if exact_link.count() != 1 or not exact_link.is_visible():
                raise RuntimeError(f"exact Quasars history row count {exact_link.count()}")
            current_title = " ".join((exact_link.inner_text() or "").split())
            prompt_title = " ".join(identity["prompt"].split())
            if not current_title or current_title != prompt_title or not current_title.startswith(identity["conversation_title"]):
                raise RuntimeError("current Quasars row title does not positively match ID and captured prompt/title")
            exact_link.hover(); page.wait_for_timeout(400)
            nav_item = exact_link.locator("xpath=.."); options = nav_item.locator("button:visible")
            if options.count() != 1:
                raise RuntimeError(f"exact Quasars row options count {options.count()}")
            options_label = options.get_attribute("aria-label") or ""
            prefix = "More options for "
            if not options_label.startswith(prefix) or " ".join(options_label[len(prefix):].split()) != current_title:
                raise RuntimeError("exact Quasars row options identity mismatch")
            need(client.op({"op": "check", "lease_id": lease["lease_id"], "epoch": lease["epoch"], "action": "open options for exact Quasars run-owned conversation 116a89ea5f3eae3a", "target_verified": target_path() == PATH}), "open exact options check")
            options.click(); page.wait_for_timeout(400)
            delete_item = page.get_by_role("menuitem", name="Delete", exact=True)
            if delete_item.count() != 1 or not delete_item.is_visible():
                raise RuntimeError(f"exact Quasars Delete item count {delete_item.count()}")
            if page_challenge(page):
                need(client.op({"op": "freeze", "declared_by": "tori-goru-quasars-delete-exact-own", "reason": "real page-content challenge in Quasars delete menu"}), "freeze")
                raise RuntimeError("page challenge: broker frozen")
            need(client.op({"op": "check", "lease_id": lease["lease_id"], "epoch": lease["epoch"], "action": f"choose Delete only for exact Quasars run-owned conversation {identity['conversation_id']} after verified save epoch {SAVE_EPOCH}", "target_verified": target_path() == PATH}), "choose exact delete check")
            delete_item.click(); page.wait_for_timeout(500)
            confirmation_mode = "direct"; dialog_text = ""
            dialogs = page.locator('[role="dialog"]:visible')
            if dialogs.count() == 1:
                dialog = dialogs.first; dialog_text = " ".join((dialog.inner_text() or "").split())[:500]
                if "delete" not in dialog_text.lower() or not any(word in dialog_text.lower() for word in ("chat", "conversation", "activity")):
                    raise RuntimeError("unexpected Quasars deletion confirmation dialog")
                confirm = dialog.get_by_role("button", name="Delete", exact=True); cancel = dialog.get_by_role("button", name="Cancel", exact=True)
                if confirm.count() != 1 or cancel.count() != 1 or not confirm.is_visible():
                    raise RuntimeError("Quasars deletion confirmation controls not exact")
                if target_path() != PATH or page_challenge(page):
                    raise RuntimeError("target or challenge changed before Quasars deletion confirmation")
                need(client.op({"op": "check", "lease_id": lease["lease_id"], "epoch": lease["epoch"], "action": f"confirm deletion only for exact Quasars run-owned conversation {identity['conversation_id']} after receipt {EXPECTED[RESULT_PATH]}", "target_verified": True}), "confirm exact delete check")
                confirm.click(); confirmation_mode = "dialog"
            page.wait_for_timeout(1500)
            post_path = target_path()
            if post_path is None or post_path == PATH:
                raise RuntimeError(f"exact Quasars conversation still current after deletion: {post_path}")
            if page.locator(f'a[href="{PATH}"]').count() != 0:
                raise RuntimeError("exact Quasars history row still exists after deletion")
            evidence = {
                "conversation_id": identity["conversation_id"], "captured_title": identity["conversation_title"],
                "deletion_match_title": current_title, "prompt_sha256": identity["prompt_sha256"],
                "submit_utc": identity["submit_utc"], "deleted_utc": datetime.now(timezone.utc).isoformat().replace("+00:00", "Z"),
                "target_id": TARGET_ID, "pre_delete_path": PATH, "post_delete_path": post_path,
                "confirmation_mode": confirmation_mode, "confirmation_dialog": dialog_text,
                "verified_result_receipt": str(RESULT_PATH), "verified_result_receipt_sha256": EXPECTED[RESULT_PATH],
                "verified_result_metadata_sha256": EXPECTED[METADATA_PATH], "verified_result_save_epoch": SAVE_EPOCH,
                "verified_result_save_entry_sha256": SAVE_ENTRY_SHA,
                "bulk_delete_used": False, "unrelated_conversation_touched": False,
            }
            EVIDENCE_PATH.write_text(json.dumps(evidence, indent=2, sort_keys=True) + "\n")
            print(json.dumps(evidence, sort_keys=True))
    finally:
        if lease is not None:
            with suppress(Exception): print(json.dumps({"delete_target_release": client.op({"op": "release", "lease_id": lease["lease_id"]})}, sort_keys=True))
        client.close()


if __name__ == "__main__": main()
