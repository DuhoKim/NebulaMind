import hashlib
import json
import sys
import time
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
RESULT_PATH = Path("receipts/GORU_DR_RESULT.md")
METADATA_PATH = Path("receipts/GORU_DR_RESULT_METADATA.json")
IDENTITY = json.loads(IDENTITY_PATH.read_text())
CONVERSATION_PATH = IDENTITY["conversation_path"]
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
    parsed = urlparse(matches[0].get("url", ""))
    return parsed.scheme == "https" and parsed.netloc == "gemini.google.com" and parsed.path == CONVERSATION_PATH


def snapshot(page):
    return page.evaluate("""() => {
      const v=e=>{const s=getComputedStyle(e),r=e.getBoundingClientRect();return s.display!=='none'&&s.visibility!=='hidden'&&r.width>0&&r.height>0};
      const label=e=>(e.getAttribute('aria-label')||e.getAttribute('title')||e.innerText||'').trim().replace(/\\s+/g,' ').slice(0,500);
      const dialogs=[...document.querySelectorAll('[role=dialog],dialog')].filter(v).map(label);
      const challenge=location.hostname==='accounts.google.com'||[...document.querySelectorAll('input[type=password]')].some(v)||[...document.querySelectorAll('iframe')].some(e=>/recaptcha|captcha/i.test(e.src||''))||dialogs.some(t=>/captcha|verify|verification|sign in|two-step|2-step|unusual activity|permission|challenge/i.test(t));
      const controls=[...document.querySelectorAll('button,[role=button]')].filter(v).map(label);
      const status=[...document.querySelectorAll('div,span,p')].filter(v).map(label);
      const messages=[...document.querySelectorAll('message-content')].filter(v);
      const last=messages.at(-1);
      const links=last?[...last.querySelectorAll('a[href]')].map(a=>({label:(a.innerText||a.textContent||'').trim().replace(/\\s+/g,' ').slice(0,300),href:a.href})).filter(x=>/^https?:/.test(x.href)):[];
      return {challenge,stop:controls.some(x=>x==='Stop response'||/stop researching/i.test(x)),research:status.some(x=>/researching(?: \\d+)? websites|research in progress/i.test(x)),messageCount:messages.length,resultText:last?(last.innerText||'').trim():'',links};
    }""")


def main():
    if RESULT_PATH.exists() or METADATA_PATH.exists():
        raise RuntimeError("result custody file already exists")
    if IDENTITY.get("target_id") != TARGET_ID or IDENTITY.get("conversation_id") != CONVERSATION_PATH.removeprefix("/app/") or not IDENTITY.get("conversation_title") or not IDENTITY.get("submit_utc"):
        raise RuntimeError("identity custody incomplete")
    if not target_ok():
        raise RuntimeError("exact result target failed")
    client = UDSClient(SOCK)
    lease = None
    try:
        lease = need(client.op({"op": "acquire", "holder": "tori-goru-dr-result-custody", "kind": "target", "mode": "read", "scope": SCOPE, "ttl": 180, "heartbeat_interval": 45}), "result target acquire")["lease"]
        with sync_playwright() as p:
            browser = p.chromium.connect_over_cdp(BASE)
            pages = [pg for ctx in browser.contexts for pg in ctx.pages if urlparse(pg.url).path == CONVERSATION_PATH]
            if len(pages) != 1:
                raise RuntimeError(f"exact result page count {len(pages)}")
            page = pages[0]
            if not target_ok():
                need(client.op({"op": "check", "lease_id": lease["lease_id"], "epoch": lease["epoch"], "action": "capture stable bounded DR result", "target_verified": False}), "target drift")
            first = snapshot(page)
            if first["challenge"]:
                need(client.op({"op": "freeze", "declared_by": "tori-goru-dr-result-custody", "reason": "real page-content challenge during result custody"}), "freeze")
                raise RuntimeError("page challenge: broker frozen")
            if first["stop"] or first["research"] or first["messageCount"] < 3 or len(first["resultText"]) < 800:
                raise RuntimeError("result is not deterministically complete")
            need(client.op({"op": "check", "lease_id": lease["lease_id"], "epoch": lease["epoch"], "action": "read exact stable bounded DR result", "target_verified": True}), "result read check")
            first_sha = hashlib.sha256(first["resultText"].encode()).hexdigest()
            time.sleep(10)
            if not target_ok():
                need(client.op({"op": "check", "lease_id": lease["lease_id"], "epoch": lease["epoch"], "action": "verify stable bounded DR result", "target_verified": False}), "stable target drift")
            second = snapshot(page)
            second_sha = hashlib.sha256(second["resultText"].encode()).hexdigest()
            if second["challenge"] or second["stop"] or second["research"] or first_sha != second_sha:
                raise RuntimeError("result stability verification failed")
            captured_utc = datetime.now(timezone.utc).isoformat().replace("+00:00", "Z")
            unique_links = []
            seen = set()
            for link in second["links"]:
                key = (link["label"], link["href"])
                if key not in seen:
                    seen.add(key)
                    unique_links.append(link)
            lines = [
                "# One bounded Deep Research result — Thunderbolt Bridge browser automation",
                "",
                f"Conversation ID: `{IDENTITY['conversation_id']}`",
                f"Conversation title: `{IDENTITY['conversation_title']}`",
                f"Target ID: `{TARGET_ID}`",
                f"Prompt submit UTC: `{IDENTITY['submit_utc']}`",
                f"Research start UTC: `{IDENTITY.get('research_start_utc', '')}`",
                f"Result captured UTC: `{captured_utc}`",
                f"Result text SHA-256: `{second_sha}`",
                "",
                "## Prompt",
                "",
                IDENTITY["prompt"],
                "",
                "## Deep Research result",
                "",
                second["resultText"],
                "",
                "## Captured result links",
                "",
            ]
            lines.extend([f"- {x['label'] or '(unlabeled)'} — {x['href']}" for x in unique_links] or ["- No direct anchor links were exposed inside the final `message-content`; source text remains preserved above."])
            RESULT_PATH.write_text("\n".join(lines) + "\n")
            metadata = {
                "identity": IDENTITY,
                "captured_utc": captured_utc,
                "message_count": second["messageCount"],
                "page_challenge": False,
                "research_indicator_visible": False,
                "stop_control_visible": False,
                "result_chars": len(second["resultText"]),
                "result_text_sha256": second_sha,
                "stable_recheck_seconds": 10,
                "captured_links": unique_links,
            }
            METADATA_PATH.write_text(json.dumps(metadata, indent=2, sort_keys=True) + "\n")
            print(json.dumps({"result_path": str(RESULT_PATH), "metadata_path": str(METADATA_PATH), "result_chars": len(second["resultText"]), "result_text_sha256": second_sha, "captured_links": len(unique_links)}, sort_keys=True))
    finally:
        if lease is not None:
            with suppress(Exception):
                print(json.dumps({"result_target_release": client.op({"op": "release", "lease_id": lease["lease_id"]})}, sort_keys=True))
        client.close()


if __name__ == "__main__":
    main()
