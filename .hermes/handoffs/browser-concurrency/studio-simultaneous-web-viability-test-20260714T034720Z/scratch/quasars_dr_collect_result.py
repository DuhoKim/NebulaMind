import hashlib
import json
import re
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
IDENTITY_PATH = Path("receipts/GORU_DR_PROVEFIRST_QUASARS_RUN_IDENTITY.json")
RESULT_PATH = Path("receipts/GORU_DR_PROVEFIRST_QUASARS_RESULT.md")
METADATA_PATH = Path("receipts/GORU_DR_PROVEFIRST_QUASARS_RESULT_METADATA.json")
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
    hits = [x for x in pages if x.get("id") == TARGET_ID and x.get("type") == "page"]
    if len(hits) != 1:
        return False
    parsed = urlparse(hits[0].get("url", ""))
    return parsed.scheme == "https" and parsed.netloc == "gemini.google.com" and parsed.path == CONVERSATION_PATH


def snapshot(page):
    return page.evaluate("""() => {const v=e=>{const s=getComputedStyle(e),r=e.getBoundingClientRect();return s.display!=='none'&&s.visibility!=='hidden'&&r.width>0&&r.height>0};const label=e=>(e.getAttribute('aria-label')||e.getAttribute('title')||e.innerText||e.textContent||'').trim().replace(/\\s+/g,' ').slice(0,500);const dialogs=[...document.querySelectorAll('[role=dialog],dialog')].filter(v).map(label);const challenge=location.hostname==='accounts.google.com'||[...document.querySelectorAll('input[type=password]')].some(v)||[...document.querySelectorAll('iframe')].some(e=>/recaptcha|captcha/i.test(e.src||''))||dialogs.some(t=>/captcha|verify|verification|sign in|two-step|2-step|unusual activity|permission|challenge/i.test(t));const controls=[...document.querySelectorAll('button,[role=button]')].filter(v).map(label);const status=[...document.querySelectorAll('div,span,p')].filter(v).map(label);const messages=[...document.querySelectorAll('message-content')].filter(v);const last=messages.at(-1);const links=[...document.querySelectorAll('a[href]')].filter(v).map(a=>({label:label(a),href:a.href})).filter(x=>/^https?:/.test(x.href));return {challenge,stop:controls.some(x=>x==='Stop response'||/stop researching/i.test(x)),research:status.some(x=>/researching(?: \\d+)? websites|research in progress|i'm on it.*research/i.test(x)),messageCount:messages.length,resultText:last?(last.innerText||'').trim():'',links}}""")


def keep_source(link):
    try:
        parsed = urlparse(link["href"])
    except Exception:
        return False
    host = parsed.netloc.lower()
    if parsed.scheme not in {"http", "https"}:
        return False
    excluded = {"gemini.google.com", "accounts.google.com", "myactivity.google.com", "support.google.com", "policies.google.com"}
    return host not in excluded and not host.endswith(".gemini.google.com")


def structure_scan(text):
    return {
        "claim_text_fields": len(re.findall(r"(?im)^\s*[-*]?\s*\*{0,2}claim_text\*{0,2}\s*:", text)),
        "claim_type_fields": len(re.findall(r"(?im)^\s*[-*]?\s*\*{0,2}claim_type\*{0,2}\s*:", text)),
        "debate_topic_fields": len(re.findall(r"(?im)^\s*[-*]?\s*\*{0,2}debate_topic\*{0,2}\s*:", text)),
        "papers_fields": len(re.findall(r"(?im)^\s*[-*]?\s*\*{0,2}papers\*{0,2}\s*:", text)),
        "established_mentions": len(re.findall(r"(?i)\bestablished\b", text)),
        "debate_mentions": len(re.findall(r"(?i)\bdebate\b", text)),
        "bibliography_marker": bool(re.search(r"(?im)^\s*#{0,4}\s*(plain-text\s+)?bibliography\b", text)),
        "arxiv_like_ids": sorted(set(re.findall(r"(?i)\b(?:arXiv\s*:?\s*)?(\d{4}\.\d{4,5})(?:v\d+)?\b", text))),
        "doi_like_ids": sorted(set(re.findall(r"(?i)\b10\.\d{4,9}/[-._;()/:A-Z0-9]+", text))),
    }


def main():
    if RESULT_PATH.exists() or METADATA_PATH.exists():
        raise RuntimeError("Quasars result custody file already exists")
    if IDENTITY.get("target_id") != TARGET_ID or IDENTITY.get("conversation_id") != CONVERSATION_PATH.removeprefix("/app/") or not IDENTITY.get("conversation_title") or not IDENTITY.get("submit_utc") or not IDENTITY.get("research_start_confirmed"):
        raise RuntimeError("Quasars identity custody incomplete")
    if not target_ok():
        raise RuntimeError("exact Quasars result target failed")
    client = UDSClient(SOCK); lease = None
    try:
        lease = need(client.op({"op": "acquire", "holder": "tori-goru-quasars-result-custody", "kind": "target", "mode": "read", "scope": SCOPE, "ttl": 240, "heartbeat_interval": 45}), "result target acquire")["lease"]
        with sync_playwright() as p:
            browser = p.chromium.connect_over_cdp(BASE)
            pages = [pg for ctx in browser.contexts for pg in ctx.pages if urlparse(pg.url).path == CONVERSATION_PATH]
            if len(pages) != 1:
                raise RuntimeError(f"exact Quasars result page count {len(pages)}")
            page = pages[0]
            if not target_ok():
                need(client.op({"op": "check", "lease_id": lease["lease_id"], "epoch": lease["epoch"], "action": "capture stable Quasars DR result", "target_verified": False}), "target drift")
            first = snapshot(page)
            if first["challenge"]:
                need(client.op({"op": "freeze", "declared_by": "tori-goru-quasars-result-custody", "reason": "real page-content challenge during Quasars result custody"}), "freeze")
                raise RuntimeError("page challenge: broker frozen")
            if first["stop"] or first["research"] or first["messageCount"] < 3 or len(first["resultText"]) < 1500:
                raise RuntimeError("Quasars result is not deterministically complete")
            need(client.op({"op": "check", "lease_id": lease["lease_id"], "epoch": lease["epoch"], "action": "read exact stable Quasars DR result", "target_verified": True}), "result read check")
            first_sha = hashlib.sha256(first["resultText"].encode()).hexdigest()
            time.sleep(15)
            if not target_ok():
                need(client.op({"op": "check", "lease_id": lease["lease_id"], "epoch": lease["epoch"], "action": "verify stable Quasars DR result", "target_verified": False}), "stable target drift")
            second = snapshot(page); second_sha = hashlib.sha256(second["resultText"].encode()).hexdigest()
            if second["challenge"] or second["stop"] or second["research"] or second["messageCount"] < 3 or first_sha != second_sha:
                raise RuntimeError("Quasars result stability verification failed")
            captured_utc = datetime.now(timezone.utc).isoformat().replace("+00:00", "Z")
            unique_links = []; seen = set()
            for link in second["links"]:
                if not keep_source(link):
                    continue
                key = link["href"]
                if key not in seen:
                    seen.add(key); unique_links.append(link)
            scan = structure_scan(second["resultText"])
            lines = [
                "# Deep Research prove-first result — Quasars as drivers of galaxy evolution",
                "", "NebulaMind page: `quasars` (page_id 32)",
                "Debate: `Are Quasars the Primary Drivers of Galaxy Evolution?`", "",
                f"Conversation ID: `{IDENTITY['conversation_id']}`",
                f"Conversation title: `{IDENTITY['conversation_title']}`",
                f"Target ID: `{TARGET_ID}`",
                f"Prompt SHA-256: `{IDENTITY['prompt_sha256']}`",
                f"Prompt submit UTC: `{IDENTITY['submit_utc']}`",
                f"Research start UTC: `{IDENTITY.get('research_start_utc', '')}`",
                f"Result captured UTC: `{captured_utc}`",
                f"Result text SHA-256: `{second_sha}`", "",
                "## Verbatim prompt", "", IDENTITY["prompt"], "",
                "## Full Deep Research report", "", second["resultText"], "",
                "## Captured source anchors", "",
            ]
            lines.extend([f"- {item['label'] or '(unlabeled)'} — {item['href']}" for item in unique_links] or ["- No external anchors were exposed; all identifiers and bibliography text remain preserved in the full report above."])
            RESULT_PATH.write_text("\n".join(lines) + "\n")
            metadata = {
                "identity": IDENTITY, "identity_sha256": hashlib.sha256(IDENTITY_PATH.read_bytes()).hexdigest(),
                "captured_utc": captured_utc, "message_count": second["messageCount"],
                "page_challenge": False, "research_indicator_visible": False, "stop_control_visible": False,
                "result_chars": len(second["resultText"]), "result_text_sha256": second_sha,
                "stable_recheck_seconds": 15, "captured_source_anchors": unique_links,
                "structure_scan": scan,
                "advisory_only": True,
                "downstream_mutations_authorized": False,
            }
            METADATA_PATH.write_text(json.dumps(metadata, indent=2, sort_keys=True) + "\n")
            print(json.dumps({"result_path": str(RESULT_PATH), "metadata_path": str(METADATA_PATH), "result_chars": len(second["resultText"]), "result_text_sha256": second_sha, "captured_source_anchors": len(unique_links), "structure_scan": scan}, sort_keys=True))
    finally:
        if lease is not None:
            with suppress(Exception): print(json.dumps({"result_target_release": client.op({"op": "release", "lease_id": lease["lease_id"]})}, sort_keys=True))
        client.close()


if __name__ == "__main__": main()
