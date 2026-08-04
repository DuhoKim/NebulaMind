import argparse
import hashlib
import json
import re
import subprocess
import sys
import time
import traceback
import urllib.request
from contextlib import suppress
from datetime import datetime, timezone
from pathlib import Path
from urllib.parse import urlparse

sys.path.insert(0, "broker")
import ledger
from transport import UDSClient
from playwright.sync_api import sync_playwright

SOCK = "/tmp/nmbrk-live-20260714/b.sock"
BASE = "http://127.0.0.1:19223"
TARGET_ID = "C92443095EE9116210C178D855DF3329"
BATCH_ROOT = Path("/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/dr-revised-20260714/round1")
PROMPT_DIR = BATCH_ROOT / "dr-review-prompts"
PACKET_DIR = BATCH_ROOT / "dr-review-packets"
STATE_PATH = PACKET_DIR / "ROUND1_DR_REVIEW_STATE.json"
SUMMARY_PATH = PACKET_DIR / "ROUND1_DR_REVIEW_FINAL_SUMMARY.md"
HOLD_SUMMARY_PATH = PACKET_DIR / "ROUND1_DR_REVIEW_HOLD_SUMMARY.md"
LEDGER_PATH = Path("ledger/RUN_LEDGER.jsonl")
JOURNAL_PYTHON = "/Users/duhokim/NebulaMind/NebulaMind/backend/.venv/bin/python"
HWAO_TARGET = "garu-agy-viability:0.0"
SCOPE = {"host_id": "pro", "bundle": "com.google.Chrome", "user_data_dir": "dr-live-cdp-20260714", "window_id": "pid-65195", "target_id": TARGET_ID}
GLOBAL_STOP = False


class GlobalChallengeStop(RuntimeError):
    pass


class TargetDrift(RuntimeError):
    pass


class PaperFailure(RuntimeError):
    pass


def utcnow():
    return datetime.now(timezone.utc).isoformat().replace("+00:00", "Z")


def sha_bytes(data):
    return hashlib.sha256(data).hexdigest()


def sha_file(path):
    return sha_bytes(Path(path).read_bytes())


def normalized(text):
    return " ".join((text or "").split())


def assert_allowed_write(path):
    resolved = Path(path).resolve()
    root = PACKET_DIR.resolve()
    if resolved != root and root not in resolved.parents:
        raise RuntimeError(f"write outside reference packet directory denied: {resolved}")
    if resolved.suffix.lower() not in {".md", ".json"}:
        raise RuntimeError(f"non-reference artifact extension denied: {resolved}")


def atomic_write(path, content):
    path = Path(path)
    assert_allowed_write(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    tmp = path.with_name(path.name + ".tmp.json" if path.suffix == ".json" else path.name + ".tmp.md")
    assert_allowed_write(tmp)
    tmp.write_text(content)
    tmp.replace(path)


def atomic_json(path, value):
    atomic_write(path, json.dumps(value, indent=2, sort_keys=True) + "\n")


def discover_prompts():
    files = sorted(PROMPT_DIR.glob("paper_*.md"))
    if len(files) != 9:
        raise RuntimeError(f"expected 9 prompt files, found {len(files)}")
    specs = []
    for index in range(1, 10):
        hits = [path for path in files if path.name.startswith(f"paper_{index:02d}_")]
        if len(hits) != 1:
            raise RuntimeError(f"paper_{index:02d} prompt count {len(hits)}")
        prompt_path = hits[0]
        suffix = prompt_path.name.removeprefix(f"paper_{index:02d}_").removesuffix("_dr_research_prompt.md")
        if not suffix or suffix == prompt_path.name:
            raise RuntimeError(f"unexpected prompt filename {prompt_path.name}")
        packet_base = f"paper_{index:02d}_{suffix}_dr_packet"
        raw = prompt_path.read_text()
        prompt = raw.rstrip("\n")
        specs.append({
            "paper": index,
            "paper_id": f"paper_{index:02d}",
            "shortname": suffix,
            "prompt_path": str(prompt_path),
            "prompt_file_sha256": sha_file(prompt_path),
            "prompt_chars": len(prompt),
            "prompt_lines": len(prompt.splitlines()),
            "prompt_sha256": sha_bytes(prompt.encode()),
            "packet_path": str(PACKET_DIR / f"{packet_base}.md"),
            "metadata_path": str(PACKET_DIR / f"{packet_base}.metadata.json"),
            "deletion_path": str(PACKET_DIR / f"{packet_base}.deletion.json"),
            "failure_path": str(PACKET_DIR / f"{packet_base}.failure.json"),
        })
    return specs


def initial_state(specs):
    return {
        "batch_id": "DR_MANUSCRIPT_REVIEW_ROUND1_20260715",
        "created_utc": utcnow(),
        "updated_utc": utcnow(),
        "advisory_only": True,
        "reference_only": True,
        "hard_boundaries": {
            "tex_edits": False,
            "db_writes": False,
            "autopilot_lane_mutation": False,
            "auto_apply": False,
            "deploy_publish_git_cron": False,
        },
        "target_id": TARGET_ID,
        "papers": [{**spec, "status": "pending"} for spec in specs],
    }


def save_state(state):
    state["updated_utc"] = utcnow()
    atomic_json(STATE_PATH, state)


def load_or_create_state(specs):
    if not STATE_PATH.exists():
        state = initial_state(specs)
        save_state(state)
        return state
    state = json.loads(STATE_PATH.read_text())
    manifest = [(x["paper_id"], x["prompt_file_sha256"], x["prompt_sha256"]) for x in state["papers"]]
    current = [(x["paper_id"], x["prompt_file_sha256"], x["prompt_sha256"]) for x in specs]
    if manifest != current or not state.get("advisory_only") or not state.get("reference_only"):
        raise RuntimeError("existing batch state manifest/boundary mismatch")
    return state


def report_hwao(message):
    text = normalized(message)
    tmux = "/opt/homebrew/bin/tmux"
    try:
        subprocess.run([tmux, "set-buffer", "--", text], check=True, timeout=10, env={k: v for k, v in __import__("os").environ.items() if k != "TMUX"})
        subprocess.run([tmux, "paste-buffer", "-t", HWAO_TARGET], check=True, timeout=10, env={k: v for k, v in __import__("os").environ.items() if k != "TMUX"})
        subprocess.run([tmux, "send-keys", "-t", HWAO_TARGET, "Enter"], check=True, timeout=10, env={k: v for k, v in __import__("os").environ.items() if k != "TMUX"})
        return True
    except Exception as exc:
        print(json.dumps({"hwao_report_error": str(exc), "message": text[:500]}), flush=True)
        return False


def broker_need(response, name):
    if not response.get("ok"):
        raise RuntimeError(f"{name}: {response}")
    return response


def target_record():
    with urllib.request.urlopen(f"{BASE}/json/list", timeout=3) as response:
        pages = json.load(response)
    hits = [item for item in pages if item.get("id") == TARGET_ID and item.get("type") == "page"]
    if len(hits) != 1:
        return None
    parsed = urlparse(hits[0].get("url", ""))
    if parsed.scheme != "https" or parsed.netloc != "gemini.google.com":
        return None
    return {"id": TARGET_ID, "url": hits[0]["url"], "path": parsed.path, "title": hits[0].get("title")}


def target_matches(expected_path, page=None):
    record = target_record()
    if not record or record["path"] != expected_path:
        return False
    if page is not None:
        parsed = urlparse(page.url)
        if parsed.scheme != "https" or parsed.netloc != "gemini.google.com" or parsed.path != expected_path:
            return False
    return True


def exact_page(browser, expected_path):
    pages = []
    for context in browser.contexts:
        for page in context.pages:
            parsed = urlparse(page.url)
            if parsed.scheme == "https" and parsed.netloc == "gemini.google.com" and parsed.path == expected_path:
                pages.append(page)
    if len(pages) != 1:
        raise TargetDrift(f"exact page count for {expected_path}: {len(pages)}")
    return pages[0]


def _page_challenge_dom(page):
    return page.evaluate("""() => {const visible=e=>{const s=getComputedStyle(e),r=e.getBoundingClientRect();return s.display!=='none'&&s.visibility!=='hidden'&&r.width>0&&r.height>0};const dialogs=[...document.querySelectorAll('[role=dialog],dialog')].filter(visible).map(e=>(e.innerText||'').slice(0,600));return location.hostname==='accounts.google.com'||[...document.querySelectorAll('input[type=password]')].some(visible)||[...document.querySelectorAll('iframe')].some(e=>/recaptcha|captcha/i.test(e.src||''))||dialogs.some(t=>/captcha|verify|verification|sign in|two-step|2-step|unusual activity|permission|challenge/i.test(t))}""")


def page_challenge(page):
    parsed = urlparse(page.url)
    if parsed.netloc == "www.google.com" and parsed.path.startswith("/sorry"):
        return True
    return _page_challenge_dom(page)


def freeze_for_challenge(client, holder, paper_id, phase):
    with suppress(Exception):
        client.op({"op": "freeze", "declared_by": holder, "reason": f"real page-content challenge during {paper_id} {phase}"})
    raise GlobalChallengeStop(f"real page challenge during {paper_id} {phase}; broker frozen")


def check_action(client, lease, action, expected_path, page=None):
    verified = target_matches(expected_path, page)
    response = client.op({"op": "check", "lease_id": lease["lease_id"], "epoch": lease["epoch"], "action": action, "target_verified": verified})
    if not verified:
        raise TargetDrift(f"target drift before action: {action}")
    return broker_need(response, action)


def acquire_retry(client, request, max_wait, heartbeat_lease=None, expected_path=None, page=None):
    deadline = time.monotonic() + max_wait
    last_heartbeat = 0.0
    while True:
        response = client.op(request)
        if response.get("ok"):
            return response["lease"]
        error = str(response.get("error", ""))
        if "frozen" in error:
            raise GlobalChallengeStop(f"broker frozen while acquiring {request['kind']}: {error}")
        retryable = "already held" in error or "scope overlap" in error
        if not retryable or time.monotonic() >= deadline:
            raise RuntimeError(f"lease acquire failed: {request['kind']}: {response}")
        if heartbeat_lease and time.monotonic() - last_heartbeat >= 20:
            if expected_path is not None and not target_matches(expected_path, page):
                check_action(client, heartbeat_lease, f"fail closed while waiting for {request['kind']}", expected_path, page)
            broker_need(client.op({"op": "heartbeat", "lease_id": heartbeat_lease["lease_id"]}), "target heartbeat during lease wait")
            last_heartbeat = time.monotonic()
        time.sleep(5)


def acquire_target(client, holder, mode, ttl=900, max_wait=120):
    return acquire_retry(client, {"op": "acquire", "holder": holder, "kind": "target", "mode": mode, "scope": SCOPE, "ttl": ttl, "heartbeat_interval": 45}, max_wait)


def acquire_account(client, holder, target_lease, expected_path, page):
    return acquire_retry(client, {"op": "acquire", "holder": holder, "kind": "account-submission", "mode": "write", "scope": {}, "ttl": 180, "heartbeat_interval": 45}, 900, target_lease, expected_path, page)


def release_lease(client, lease):
    if lease is not None:
        with suppress(Exception):
            client.op({"op": "release", "lease_id": lease["lease_id"]})


def editor_value(editor):
    lines = editor.evaluate("""el => [...el.children].map(child => {const value=(child.innerText||'').replace(/\\r\\n/g,'\\n');return value==='\\n'?'':value})""")
    if lines:
        return "\n".join(lines)
    return (editor.evaluate("el => el.innerText || ''") or "").replace("\r\n", "\n")


def current_prompt_identity(page, prompt):
    """Prove the current conversation from its exact route and visible prompt."""
    prompt_title = normalized(prompt)
    queries = page.locator("user-query:visible")
    visible = [queries.nth(i) for i in range(queries.count()) if queries.nth(i).is_visible()]
    if len(visible) != 1:
        return None
    query_text = normalized(visible[0].inner_text())
    expected_query = normalized("You said " + prompt)
    document_title = normalized(page.title())
    suffix = " - Google Gemini"
    title_without_product = document_title[:-len(suffix)] if document_title.endswith(suffix) else document_title
    if query_text != expected_query or not title_without_product:
        return None
    return {
        "captured_title": title_without_product,
        "evidence": "exact_route_plus_visible_user_query_plus_document_title",
        "visible_user_query_normalized_sha256": sha_bytes(query_text.encode()),
        "document_title_normalized_sha256": sha_bytes(document_title.encode()),
    }


def result_text_identity(text, expected_sha256, expected_chars):
    return len(text) == expected_chars and sha_bytes(text.encode()) == expected_sha256


def needs_deletion_settlement_reload(post_path, old_path, old_link_count):
    return bool(post_path and post_path != old_path and old_link_count > 0)


def current_saved_result_identity(page, paper_state):
    """Prove the current owned chat from its verified saved terminal result."""
    snapshot = page_snapshot(page)
    messages = snapshot.get("messages", [])
    expected = paper_state.get("result", {})
    if len(messages) < 3 or snapshot.get("challenge") or snapshot.get("research") or snapshot.get("stop"):
        return None
    last = messages[-1]["text"]
    if not result_text_identity(last, expected.get("text_sha256", ""), expected.get("chars", -1)):
        return None
    return {
        "evidence": "exact_route_plus_terminal_result_matching_verified_packet",
        "message_count": len(messages),
        "result_chars": len(last),
        "result_text_sha256": sha_bytes(last.encode()),
    }


def _page_snapshot_dom(page):
    return page.evaluate("""() => {const visible=e=>{const s=getComputedStyle(e),r=e.getBoundingClientRect();return s.display!=='none'&&s.visibility!=='hidden'&&r.width>0&&r.height>0};const label=e=>(e.getAttribute('aria-label')||e.getAttribute('title')||e.innerText||e.textContent||'').trim().replace(/\s+/g,' ').slice(0,500);const dialogs=[...document.querySelectorAll('[role=dialog],dialog')].filter(visible).map(label);const challenge=location.hostname==='accounts.google.com'||[...document.querySelectorAll('input[type=password]')].some(visible)||[...document.querySelectorAll('iframe')].some(e=>/recaptcha|captcha/i.test(e.src||''))||dialogs.some(t=>/captcha|verify|verification|sign in|two-step|2-step|unusual activity|permission|challenge/i.test(t));const controls=[...document.querySelectorAll('button,[role=button]')].filter(visible).map(e=>({label:label(e),disabled:!!e.disabled}));const status=[...document.querySelectorAll('div,span,p')].filter(visible).map(label);const messages=[...document.querySelectorAll('message-content')].filter(visible).map(e=>({text:(e.innerText||'').trim(),links:e.querySelectorAll('a[href]').length}));const links=[...document.querySelectorAll('a[href]')].filter(visible).map(a=>({label:label(a),href:a.href})).filter(x=>/^https?:/.test(x.href));const last=messages.length?messages[messages.length-1].text:'';return {challenge,dialogs,controls,status,messages,links,stop:controls.some(x=>x.label==='Stop response'||/stop researching/i.test(x.label)),research:status.some(x=>/researching(?: \d+)? websites|research in progress|i'm on it.*research/i.test(x)),failure:/couldn't complete|unable to complete|research stopped|something went wrong|failed to research/i.test(last)}}""")


def page_snapshot(page):
    parsed = urlparse(page.url)
    if parsed.netloc == "www.google.com" and parsed.path.startswith("/sorry"):
        return {"challenge": True, "dialogs": [], "controls": [], "status": [], "messages": [], "links": [], "stop": False, "research": False, "failure": False}
    return _page_snapshot_dom(page)


def keep_source(link):
    try:
        parsed = urlparse(link["href"])
    except Exception:
        return False
    excluded = {"gemini.google.com", "accounts.google.com", "myactivity.google.com", "support.google.com", "policies.google.com"}
    return parsed.scheme in {"http", "https"} and parsed.netloc.lower() not in excluded and not parsed.netloc.lower().endswith(".gemini.google.com")


def output_scan(text):
    scans = {}
    for number in range(1, 5):
        scans[f"section_{number}_present"] = bool(re.search(rf"(?i)section\s*{number}\b", text))
    scans.update({
        "source_blocks": len(re.findall(r"(?im)^\s*(?:[-*]\s*)?`?Source\s+\d+\s*:", text)),
        "identifier_fields": len(re.findall(r"(?im)^\s*(?:[-*]\s*)?`?Identifier\s*:", text)),
        "role_fields": len(re.findall(r"(?im)^\s*(?:[-*]\s*)?`?Role\s*:", text)),
        "stance_rationale_fields": len(re.findall(r"(?im)^\s*(?:[-*]\s*)?`?Stance\s*/\s*Rationale\s*:", text)),
        "arxiv_like_ids": sorted(set(re.findall(r"(?i)\b(?:arXiv\s*:?\s*)?(\d{4}\.\d{4,5})(?:v\d+)?\b", text))),
        "doi_like_ids": sorted(set(re.findall(r"(?i)\b10\.\d{4,9}/[-._;()/:A-Z0-9]+", text))),
        "no_mock_receipt_present": bool(re.search(r"(?i)no[- ]mock[- ]data|no mock|no synthetic|safety ledger", text)),
    })
    return scans


def journal_entry(etype, note, files):
    ok, message = ledger.verify(LEDGER_PATH)
    if not ok:
        raise GlobalChallengeStop(f"ledger invalid before {etype}: {message}")
    args = [JOURNAL_PYTHON, "-B", "broker/journal.py", str(LEDGER_PATH), "goru", etype, note] + [str(Path(path)) for path in files]
    completed = subprocess.run(args, check=True, text=True, capture_output=True, timeout=120)
    lines = [line for line in completed.stdout.splitlines() if line.strip()]
    entry = json.loads(lines[0])
    ok, message = ledger.verify(LEDGER_PATH)
    if not ok:
        raise GlobalChallengeStop(f"ledger invalid after {etype}: {message}")
    entry["verify"] = message
    return entry


def set_paper_state(state, paper_number, **updates):
    paper = state["papers"][paper_number - 1]
    paper.update(updates)
    save_state(state)
    return paper


def stage_and_submit(spec, state, browser):
    paper_id = spec["paper_id"]
    holder = f"goru-dr-review-r1-{paper_id}-submit"
    prompt = Path(spec["prompt_path"]).read_text().rstrip("\n")
    if sha_bytes(prompt.encode()) != spec["prompt_sha256"] or sha_file(spec["prompt_path"]) != spec["prompt_file_sha256"]:
        raise PaperFailure("prompt hash drift")
    if not target_matches("/app"):
        raise TargetDrift(f"{paper_id} requires exact /app target")
    client = UDSClient(SOCK); target_lease = None; account_lease = None
    try:
        target_lease = acquire_target(client, holder, "write", ttl=1200)
        page = exact_page(browser, "/app")
        if page_challenge(page):
            freeze_for_challenge(client, holder, paper_id, "page-scoped preflight")
        active = page.get_by_label("Deselect Deep research", exact=True)
        if not (active.count() == 1 and active.is_visible()):
            tools = page.get_by_label("Upload & tools", exact=True)
            if tools.count() != 1 or not tools.is_visible():
                raise PaperFailure("Upload & tools not unique visible")
            check_action(client, target_lease, f"{paper_id} open Upload & tools", "/app", page)
            tools.click(); page.wait_for_timeout(500)
            deep = page.get_by_text("Deep research", exact=True)
            visible = [deep.nth(i) for i in range(deep.count()) if deep.nth(i).is_visible()]
            if len(visible) != 1:
                raise PaperFailure(f"Deep research visible count {len(visible)}")
            check_action(client, target_lease, f"{paper_id} select Deep research", "/app", page)
            visible[0].click(); page.wait_for_timeout(700)
        active = page.get_by_label("Deselect Deep research", exact=True)
        if active.count() != 1 or not active.is_visible():
            raise PaperFailure("Deep research mode not active")
        editor = page.get_by_role("textbox", name="Enter a prompt for Gemini", exact=True)
        if editor.count() != 1 or not editor.is_visible():
            raise PaperFailure("prompt editor not unique visible")
        check_action(client, target_lease, f"{paper_id} fill verbatim prompt", "/app", page)
        editor.fill(prompt); page.wait_for_timeout(600)
        staged = editor_value(editor)
        staged_sha = sha_bytes(staged.encode())
        if staged != prompt or staged_sha != spec["prompt_sha256"]:
            raise PaperFailure(f"staged prompt not verbatim chars={len(staged)} sha={staged_sha}")
        send = page.get_by_label("Send message", exact=True)
        if send.count() != 1 or not send.is_visible() or send.is_disabled():
            raise PaperFailure("Send message not one enabled visible control")
        set_paper_state(state, spec["paper"], status="staged", staged_utc=utcnow(), staged_text_sha256=staged_sha, page_challenge=False)
        account_lease = acquire_account(client, holder, target_lease, "/app", page)
        if page_challenge(page):
            freeze_for_challenge(client, holder, paper_id, "immediate pre-submit")
        check_action(client, target_lease, f"{paper_id} submit one verbatim Deep Research prompt", "/app", page)
        check_action(client, account_lease, f"serialized account submit {paper_id} verbatim Deep Research prompt", "/app", page)
        submit_utc = utcnow(); account_id = account_lease["lease_id"]
        send.click()
        try:
            page.wait_for_url(lambda url: urlparse(url).netloc == "gemini.google.com" and urlparse(url).path.startswith("/app/"), timeout=45000)
        finally:
            release_lease(client, account_lease); account_lease = None
        record = target_record()
        if not record or record["path"] != urlparse(page.url).path or record["path"] == "/app":
            check_action(client, target_lease, f"{paper_id} fail closed post-submit identity", "/app", page)
        path = record["path"]; conversation_id = path.removeprefix("/app/")
        if not conversation_id or "/" in conversation_id:
            raise PaperFailure(f"invalid conversation path {path}")
        if page_challenge(page):
            freeze_for_challenge(client, holder, paper_id, "post-submit identity")
        titles = []
        for attempt in range(24):
            links = page.locator(f'a[href="{path}"]')
            visible_links = [links.nth(i) for i in range(links.count()) if links.nth(i).is_visible()]
            titles = sorted(set(normalized(link.inner_text()) for link in visible_links if normalized(link.inner_text())))
            if len(titles) == 1:
                break
            if attempt == 2:
                open_sidebar = page.get_by_label("Open sidebar", exact=True)
                if open_sidebar.count() == 1 and open_sidebar.is_visible():
                    check_action(client, target_lease, f"{paper_id} open sidebar for exact identity", path, page)
                    open_sidebar.click()
            broker_need(client.op({"op": "heartbeat", "lease_id": target_lease["lease_id"]}), "identity target heartbeat")
            page.wait_for_timeout(2500)
        prompt_identity = current_prompt_identity(page, prompt)
        if len(titles) == 1:
            captured_title = titles[0]
            identity_evidence = {"evidence": "exact_route_plus_visible_history_row"}
        elif prompt_identity:
            captured_title = prompt_identity["captured_title"]
            identity_evidence = prompt_identity
        else:
            raise PaperFailure(
                f"conversation identity unavailable: exact history title candidate count {len(titles)} and visible prompt mismatch"
            )
        identity = {
            "target_id": TARGET_ID,
            "conversation_id": conversation_id,
            "conversation_path": path,
            "captured_title": captured_title,
            "identity_evidence": identity_evidence,
            "submit_utc": submit_utc,
            "submit_account_lease_id": account_id,
            "prompt_sha256": spec["prompt_sha256"],
            "prompt_file_sha256": spec["prompt_file_sha256"],
            "page_challenge_after_submit": False,
        }
        set_paper_state(state, spec["paper"], status="submitted", identity=identity)
        print(json.dumps({"paper": paper_id, "submitted": True, "conversation_id": conversation_id, "submit_utc": submit_utc}), flush=True)
        return identity
    finally:
        release_lease(client, account_lease)
        release_lease(client, target_lease)
        client.close()


def wait_for_plan(identity, spec, state, browser):
    paper_id = spec["paper_id"]; path = identity["conversation_path"]
    holder = f"goru-dr-review-r1-{paper_id}-plan"
    client = UDSClient(SOCK); lease = None
    try:
        lease = acquire_target(client, holder, "read", ttl=600)
        page = exact_page(browser, path)
        deadline = time.monotonic() + 420
        while time.monotonic() < deadline:
            if not target_matches(path, page):
                check_action(client, lease, f"{paper_id} fail closed plan poll", path, page)
            snapshot = page_snapshot(page)
            if snapshot["challenge"]:
                freeze_for_challenge(client, holder, paper_id, "research-plan wait")
            check_action(client, lease, f"read-only {paper_id} research-plan poll", path, page)
            broker_need(client.op({"op": "heartbeat", "lease_id": lease["lease_id"]}), "plan heartbeat")
            start = page.get_by_role("button", name="Start research", exact=True)
            visible_start = [start.nth(i) for i in range(start.count()) if start.nth(i).is_visible() and not start.nth(i).is_disabled()]
            if len(visible_start) == 1:
                return "start_required"
            if snapshot["research"] and snapshot["stop"]:
                set_paper_state(state, spec["paper"], status="researching", research_start_utc=utcnow(), research_start_mode="automatic")
                return "already_researching"
            if snapshot["failure"] and not snapshot["stop"]:
                raise PaperFailure("terminal failure while creating research plan")
            time.sleep(8)
        raise PaperFailure("research plan did not settle within 420 seconds")
    finally:
        release_lease(client, lease); client.close()


def start_research(identity, spec, state, browser):
    paper_id = spec["paper_id"]; path = identity["conversation_path"]
    holder = f"goru-dr-review-r1-{paper_id}-start"
    client = UDSClient(SOCK); target_lease = None; account_lease = None
    try:
        target_lease = acquire_target(client, holder, "write", ttl=1200)
        page = exact_page(browser, path)
        if page_challenge(page):
            freeze_for_challenge(client, holder, paper_id, "before Start research")
        start = page.get_by_role("button", name="Start research", exact=True)
        visible = [start.nth(i) for i in range(start.count()) if start.nth(i).is_visible() and not start.nth(i).is_disabled()]
        if len(visible) != 1:
            raise PaperFailure(f"Start research enabled visible count {len(visible)}")
        account_lease = acquire_account(client, holder, target_lease, path, page)
        if page_challenge(page):
            freeze_for_challenge(client, holder, paper_id, "immediate pre-Start research")
        check_action(client, target_lease, f"{paper_id} Start research exact conversation", path, page)
        check_action(client, account_lease, f"serialized account submit {paper_id} Start research", path, page)
        start_utc = utcnow(); account_id = account_lease["lease_id"]
        visible[0].click()
        accepted = False
        deadline = time.monotonic() + 120
        while time.monotonic() < deadline:
            snapshot = page_snapshot(page)
            if snapshot["challenge"]:
                freeze_for_challenge(client, holder, paper_id, "post-Start research")
            in_progress_text = " ".join(item["text"] for item in snapshot["messages"])
            in_progress_signal = snapshot["research"] or "While I'm researching" in in_progress_text or "Researching " in in_progress_text or "Creating visuals for the report" in in_progress_text
            if target_matches(path, page) and snapshot["stop"] and in_progress_signal:
                accepted = True; break
            time.sleep(1)
        release_lease(client, account_lease); account_lease = None
        if not accepted:
            raise PaperFailure("Start research acceptance not positively confirmed")
        set_paper_state(state, spec["paper"], status="researching", research_start_utc=start_utc, research_start_mode="confirmed_button", research_start_account_lease_id=account_id)
        print(json.dumps({"paper": paper_id, "research_started": True, "research_start_utc": start_utc}), flush=True)
    finally:
        release_lease(client, account_lease); release_lease(client, target_lease); client.close()


def poll_terminal(identity, spec, state, browser):
    paper_id = spec["paper_id"]; path = identity["conversation_path"]
    holder = f"goru-dr-review-r1-{paper_id}-monitor"
    client = UDSClient(SOCK); lease = None
    try:
        lease = acquire_target(client, holder, "read", ttl=3000)
        page = exact_page(browser, path)
        deadline = time.monotonic() + 2700
        failure_stable = 0; poll_count = 0
        while time.monotonic() < deadline:
            if not target_matches(path, page):
                check_action(client, lease, f"{paper_id} fail closed terminal poll", path, page)
            snapshot = page_snapshot(page)
            if snapshot["challenge"]:
                freeze_for_challenge(client, holder, paper_id, "terminal polling")
            check_action(client, lease, f"read-only {paper_id} terminal poll", path, page)
            broker_need(client.op({"op": "heartbeat", "lease_id": lease["lease_id"]}), "monitor heartbeat")
            lengths = [len(item["text"]) for item in snapshot["messages"]]
            print(json.dumps({"paper": paper_id, "messages": len(lengths), "lengths": lengths, "research": snapshot["research"], "stop": snapshot["stop"], "failure": snapshot["failure"]}), flush=True)
            last = snapshot["messages"][-1]["text"] if snapshot["messages"] else ""
            candidate = len(lengths) >= 3 and len(last) >= 2000 and not snapshot["stop"] and not snapshot["research"] and "I'll let you know when your research is done" not in last
            if candidate:
                digest = sha_bytes(last.encode())
                time.sleep(20)
                if not target_matches(path, page):
                    check_action(client, lease, f"{paper_id} fail closed stable-result check", path, page)
                stable = page_snapshot(page)
                stable_last = stable["messages"][-1]["text"] if stable["messages"] else ""
                stable_digest = sha_bytes(stable_last.encode())
                if not stable["challenge"] and not stable["stop"] and not stable["research"] and len(stable.get("messages", [])) >= 3 and digest == stable_digest:
                    return stable, stable_digest
            failure_stable = failure_stable + 1 if snapshot["failure"] and not snapshot["stop"] and not snapshot["research"] else 0
            if failure_stable >= 2:
                raise PaperFailure("Deep Research reached a stable terminal failure")
            poll_count += 1
            if poll_count % 8 == 0:
                set_paper_state(state, spec["paper"], status="researching", last_poll_utc=utcnow(), last_message_lengths=lengths)
            time.sleep(15)
        raise PaperFailure("Deep Research did not reach terminal stable state within 2700 seconds")
    finally:
        release_lease(client, lease); client.close()


def save_packet(snapshot, result_sha, identity, spec, state):
    result_text = snapshot["messages"][-1]["text"]
    unique_links = []; seen = set()
    for link in snapshot["links"]:
        if not keep_source(link):
            continue
        if link["href"] not in seen:
            seen.add(link["href"]); unique_links.append(link)
    scan = output_scan(result_text)
    captured_utc = utcnow()
    packet_path = Path(spec["packet_path"]); metadata_path = Path(spec["metadata_path"])
    prompt = Path(spec["prompt_path"]).read_text().rstrip("\n")
    lines = [
        f"# Deep Research reference packet — {spec['paper_id']} {spec['shortname']}", "",
        "advisory_only: true", "reference_only: true", "auto_apply_authorized: false", "",
        f"Prompt file: `{spec['prompt_path']}`", f"Prompt file SHA-256: `{spec['prompt_file_sha256']}`",
        f"Submitted prompt text SHA-256: `{spec['prompt_sha256']}`", f"Conversation ID: `{identity['conversation_id']}`",
        f"Captured conversation title: `{identity['captured_title']}`", f"Submit UTC: `{identity['submit_utc']}`",
        f"Research start UTC: `{state['papers'][spec['paper']-1].get('research_start_utc','')}`",
        f"Result captured UTC: `{captured_utc}`", f"Result text SHA-256: `{result_sha}`", "",
        "## Verbatim prompt", "", prompt, "", "## Full Deep Research sourced report", "", result_text, "",
        "## Captured source anchors", "",
    ]
    lines.extend([f"- {item['label'] or '(unlabeled)'} — {item['href']}" for item in unique_links] or ["- No external source anchors were exposed; identifiers remain preserved in the full report above."])
    lines.extend(["", "## Reference-only safety receipt", "", "- advisory_only: true", "- No `.tex` edit or auto-apply is authorized or performed by this lane.", "- No DB, API, wiki, trust, autopilot-lane, deploy, git, publish, cron, billing, account-setting, credential, secret, bulk-history, or unrelated-conversation mutation is authorized or performed. Exact-owned conversation cleanup is authorized only after verified packet save.", ""])
    atomic_write(packet_path, "\n".join(lines))
    metadata = {
        "paper_id": spec["paper_id"], "shortname": spec["shortname"],
        "advisory_only": True, "reference_only": True, "auto_apply_authorized": False,
        "downstream_mutations_authorized": False,
        "hard_boundaries": {"tex_edits": False, "db_writes": False, "autopilot_lane_mutation": False, "auto_apply": False},
        "prompt_path": spec["prompt_path"], "prompt_file_sha256": spec["prompt_file_sha256"], "prompt_sha256": spec["prompt_sha256"],
        "identity": identity, "captured_utc": captured_utc,
        "terminal_state": {"page_challenge": False, "research_visible": False, "stop_visible": False, "message_count": len(snapshot["messages"]), "stable_recheck_seconds": 20},
        "result_chars": len(result_text), "result_text_sha256": result_sha,
        "captured_source_anchors": unique_links, "source_anchor_count": len(unique_links), "output_scan": scan,
    }
    atomic_json(metadata_path, metadata)
    packet_text = packet_path.read_text(); metadata_read = json.loads(metadata_path.read_text())
    raw_start = "## Full Deep Research sourced report\n\n"; raw_end = "\n\n## Captured source anchors\n"
    if packet_text.count(raw_start) != 1 or packet_text.count(raw_end) != 1:
        raise PaperFailure("saved packet result markers invalid")
    saved_raw = packet_text.split(raw_start, 1)[1].split(raw_end, 1)[0]
    if sha_bytes(saved_raw.encode()) != result_sha or len(saved_raw) != len(result_text):
        raise PaperFailure("saved packet raw result verification failed")
    if metadata_read["result_text_sha256"] != result_sha or metadata_read["source_anchor_count"] != len(unique_links) or metadata_read["advisory_only"] is not True:
        raise PaperFailure("saved packet metadata verification failed")
    packet_sha = sha_file(packet_path); metadata_sha = sha_file(metadata_path)
    note = (f"REFERENCE-ONLY {spec['paper_id']} Deep Research packet saved/verified before deletion; advisory_only=true; "
            f"conversation_id={identity['conversation_id']}; prompt_sha256={spec['prompt_sha256']}; result_chars={len(result_text)}; "
            f"result_text_sha256={result_sha}; packet_sha256={packet_sha}; metadata_sha256={metadata_sha}; source_anchors={len(unique_links)}; "
            "no .tex/DB/autopilot-lane/auto-apply/deploy/git/publish/cron/account-setting/secret mutation; exact-owned conversation cleanup occurs only after verified save.")
    entry = journal_entry(f"dr_review_r1_{spec['paper_id']}_reference_packet_saved_verified", note, [packet_path, metadata_path, spec["prompt_path"]])
    set_paper_state(state, spec["paper"], status="saved_verified", result={"chars": len(result_text), "text_sha256": result_sha, "source_anchor_count": len(unique_links), "output_scan": scan}, packet_sha256=packet_sha, metadata_sha256=metadata_sha, save_ledger=entry)
    return metadata, entry


def delete_exact_own(identity, spec, state, browser):
    paper_id = spec["paper_id"]; path = identity["conversation_path"]
    paper_state = state["papers"][spec["paper"] - 1]
    packet_path = Path(spec["packet_path"]); metadata_path = Path(spec["metadata_path"]); deletion_path = Path(spec["deletion_path"])
    if deletion_path.exists():
        raise PaperFailure("deletion evidence already exists")
    if sha_file(packet_path) != paper_state.get("packet_sha256") or sha_file(metadata_path) != paper_state.get("metadata_sha256"):
        raise PaperFailure("packet custody hash changed before deletion")
    save_epoch = paper_state.get("save_ledger", {}).get("epoch"); save_sha = paper_state.get("save_ledger", {}).get("entry_sha256")
    ok, message = ledger.verify(LEDGER_PATH)
    entries = ledger.read_entries(LEDGER_PATH) if ok else []
    saved = next((item for item in entries if item.get("epoch") == save_epoch), None)
    if not saved or saved.get("entry_sha256") != save_sha or saved.get("type") != f"dr_review_r1_{paper_id}_reference_packet_saved_verified":
        raise PaperFailure(f"verified save ledger absent before deletion: {message}")
    if not target_matches(path):
        raise TargetDrift("exact run-owned conversation is not current before deletion")
    holder = f"goru-dr-review-r1-{paper_id}-delete"
    client = UDSClient(SOCK); lease = None
    try:
        lease = acquire_target(client, holder, "write", ttl=600)
        page = exact_page(browser, path)
        if page_challenge(page):
            freeze_for_challenge(client, holder, paper_id, "before exact-own deletion")
        prompt = Path(spec["prompt_path"]).read_text().rstrip("\n")
        prompt_identity = current_prompt_identity(page, prompt)
        result_identity = current_saved_result_identity(page, paper_state)
        if not prompt_identity and not result_identity:
            raise PaperFailure("current exact route matches neither submitted prompt nor verified terminal result")
        # A completed Deep Research report may be open in Gemini's immersive
        # side panel.  Verify the saved result while that panel is open, then
        # close only the panel so the exact current-conversation controls are
        # available for owned-history cleanup.
        close_report_panel = page.get_by_label("Close panel", exact=True)
        if result_identity and close_report_panel.count() == 1 and close_report_panel.is_visible():
            check_action(client, lease, f"{paper_id} close verified terminal report panel before exact-own deletion", path, page)
            close_report_panel.click()
            page.wait_for_timeout(700)
            if page_challenge(page) or not target_matches(path, page):
                raise TargetDrift("target/challenge changed while closing verified terminal report panel")
        open_sidebar = page.get_by_label("Open sidebar", exact=True)
        if open_sidebar.count() == 1 and open_sidebar.is_visible():
            check_action(client, lease, f"{paper_id} open sidebar for exact-own deletion", path, page)
            open_sidebar.click(); page.wait_for_timeout(700)
        link = page.locator(f'a[href="{path}"]')
        visible = [link.nth(i) for i in range(link.count()) if link.nth(i).is_visible()]
        captured_title = normalized(identity["captured_title"])
        prompt_title = normalized(prompt)
        if len(visible) == 1:
            row = visible[0]
            current_title = normalized(row.inner_text())
            if not current_title:
                raise PaperFailure("exact run-owned row title empty")
            title_relation = "exact_prompt" if current_title == prompt_title else ("captured_title" if current_title == captured_title else ("captured_prefix" if current_title.startswith(captured_title) or captured_title.startswith(current_title) else "exact_route_id_with_title_change"))
            row.hover(); page.wait_for_timeout(400)
            parent = row.locator("xpath=..")
            options = parent.locator("button:visible")
            if options.count() != 1:
                raise PaperFailure(f"exact row options count {options.count()}")
            options_label = options.get_attribute("aria-label") or ""
            prefix = "More options for "
            if not options_label.startswith(prefix) or normalized(options_label[len(prefix):]) != current_title:
                raise PaperFailure("exact row options title mismatch")
            deletion_control = "exact_history_row_options"
        elif len(visible) == 0:
            if prompt_identity:
                current_title = prompt_identity["captured_title"]
                title_relation = "exact_prompt_current_route"
            else:
                current_title = normalized(page.title())
                suffix = " - Google Gemini"
                if current_title.endswith(suffix):
                    current_title = current_title[:-len(suffix)]
                if not current_title:
                    raise PaperFailure("current exact conversation title unavailable")
                title_relation = "exact_route_and_verified_terminal_result"
            options = page.get_by_label("Open menu for conversation actions.", exact=True)
            # On a narrow CDP viewport, Gemini can keep this exact control in
            # the DOM while the expanded sidebar clips it out of view.  The
            # exact history row may be virtualized at the same time.  Close
            # only the sidebar, then re-resolve the unique current-chat menu;
            # identity remains anchored by route + verified saved result.
            if options.count() == 1 and not options.is_visible():
                close_sidebar = page.get_by_label("Close sidebar", exact=True)
                if close_sidebar.count() == 1 and close_sidebar.is_visible():
                    check_action(client, lease, f"{paper_id} close sidebar to reveal exact current conversation menu", path, page)
                    close_sidebar.click()
                    page.wait_for_timeout(700)
                    options = page.get_by_label("Open menu for conversation actions.", exact=True)
            if options.count() != 1 or not options.is_visible():
                raise PaperFailure("current exact conversation action menu unavailable")
            options_label = options.get_attribute("aria-label") or ""
            deletion_control = "current_exact_conversation_menu"
        else:
            raise PaperFailure(f"exact run-owned history row count {len(visible)}")
        check_action(client, lease, f"{paper_id} open options exact own conversation {identity['conversation_id']}", path, page)
        options.click(); page.wait_for_timeout(400)
        delete_item = page.get_by_role("menuitem", name="Delete", exact=True)
        if delete_item.count() != 1 or not delete_item.is_visible():
            raise PaperFailure(f"Delete menu item count {delete_item.count()}")
        if page_challenge(page):
            freeze_for_challenge(client, holder, paper_id, "exact-own delete menu")
        check_action(client, lease, f"{paper_id} choose Delete exact own {identity['conversation_id']} after save epoch {save_epoch}", path, page)
        delete_item.click(); page.wait_for_timeout(500)
        dialogs = page.locator('[role="dialog"]:visible'); confirmation_mode = "direct"; dialog_text = ""
        if dialogs.count() == 1:
            dialog = dialogs.first; dialog_text = normalized(dialog.inner_text())[:500]
            if "delete" not in dialog_text.lower() or not any(word in dialog_text.lower() for word in ("chat", "conversation", "activity")):
                raise PaperFailure("unexpected deletion dialog")
            confirm = dialog.get_by_role("button", name="Delete", exact=True); cancel = dialog.get_by_role("button", name="Cancel", exact=True)
            if confirm.count() != 1 or cancel.count() != 1 or not confirm.is_visible():
                raise PaperFailure("exact delete confirmation controls missing")
            if page_challenge(page) or not target_matches(path, page):
                raise TargetDrift("target/challenge changed before deletion confirmation")
            check_action(client, lease, f"{paper_id} confirm Delete exact own {identity['conversation_id']} packet {paper_state['packet_sha256']}", path, page)
            confirm.click(); confirmation_mode = "dialog"
        page.wait_for_timeout(1600)
        record = target_record(); post_path = record["path"] if record else None
        old_link_count = page.locator(f'a[href="{path}"]').count()
        if needs_deletion_settlement_reload(post_path, path, old_link_count):
            check_action(client, lease, f"{paper_id} settle exact-own deletion verification", post_path, page)
            page.reload(wait_until="domcontentloaded", timeout=30000)
            page.wait_for_timeout(1600)
            open_sidebar = page.get_by_label("Open sidebar", exact=True)
            if open_sidebar.count() == 1 and open_sidebar.is_visible():
                check_action(client, lease, f"{paper_id} open sidebar for settled deletion verification", post_path, page)
                open_sidebar.click(); page.wait_for_timeout(700)
            old_link_count = page.locator(f'a[href="{path}"]').count()
        if post_path is None or post_path == path or old_link_count != 0:
            raise PaperFailure(f"exact own conversation not absent after deletion: {post_path}")
        evidence = {
            "paper_id": paper_id, "advisory_only": True, "conversation_id": identity["conversation_id"],
            "captured_title": identity["captured_title"], "deletion_match_title": current_title, "title_relation": title_relation,
            "deletion_control": deletion_control, "prompt_identity_evidence": prompt_identity,
            "saved_result_identity_evidence": result_identity,
            "submit_utc": identity["submit_utc"], "deleted_utc": utcnow(), "target_id": TARGET_ID,
            "pre_delete_path": path, "post_delete_path": post_path, "confirmation_mode": confirmation_mode, "confirmation_dialog": dialog_text,
            "verified_packet": str(packet_path), "verified_packet_sha256": paper_state["packet_sha256"],
            "verified_metadata_sha256": paper_state["metadata_sha256"], "verified_save_epoch": save_epoch, "verified_save_entry_sha256": save_sha,
            "bulk_delete_used": False, "unrelated_conversation_touched": False,
        }
        atomic_json(deletion_path, evidence)
        evidence_sha = sha_file(deletion_path)
        note = (f"REFERENCE-ONLY {paper_id} exact-own history cleanup after verified packet save; conversation_id={identity['conversation_id']}; "
                f"submit_utc={identity['submit_utc']}; deletion_sha256={evidence_sha}; save_epoch={save_epoch}; post_path={post_path}; "
                "bulk_delete=false; unrelated_conversation_touched=false; no .tex/DB/autopilot/auto-apply mutation.")
        entry = journal_entry(f"dr_review_r1_{paper_id}_exact_own_deleted", note, [deletion_path, packet_path, metadata_path])
        set_paper_state(state, spec["paper"], status="completed", deletion_sha256=evidence_sha, delete_ledger=entry, deleted_utc=evidence["deleted_utc"])
        return evidence, entry
    finally:
        release_lease(client, lease); client.close()


def recover_new_chat(identity, spec, browser):
    record = target_record()
    if not record or record["path"] == "/app":
        return bool(record)
    own_path = identity.get("conversation_path") if identity else None
    if record["path"] != own_path:
        return False
    holder = f"goru-dr-review-r1-{spec['paper_id']}-recover"
    client = UDSClient(SOCK); lease = None
    try:
        lease = acquire_target(client, holder, "write", ttl=180)
        page = exact_page(browser, own_path)
        if page_challenge(page):
            freeze_for_challenge(client, holder, spec["paper_id"], "failure recovery")
        check_action(client, lease, f"{spec['paper_id']} navigate owned failed conversation to new chat without deletion", own_path, page)
        page.goto("https://gemini.google.com/app", wait_until="domcontentloaded", timeout=30000)
        page.wait_for_timeout(1000)
        return target_matches("/app", page)
    finally:
        release_lease(client, lease); client.close()


def write_failure(spec, state, exc, identity=None):
    failure_path = Path(spec["failure_path"])
    if failure_path.exists():
        attempt = 2
        candidate = failure_path
        while candidate.exists():
            candidate = failure_path.with_name(failure_path.name.replace(".failure.json", f".failure_{attempt}.json"))
            attempt += 1
        failure_path = candidate
    failure = {
        "paper_id": spec["paper_id"], "advisory_only": True, "failed_utc": utcnow(),
        "error_class": type(exc).__name__, "error": str(exc),
        "global_challenge_stop": isinstance(exc, GlobalChallengeStop),
        "identity": identity, "actions_not_taken": ["no .tex edit", "no DB write", "no autopilot-lane mutation", "no auto-apply"],
    }
    atomic_json(failure_path, failure)
    failure_sha = sha_file(failure_path)
    entry = None
    with suppress(Exception):
        entry = journal_entry(f"dr_review_r1_{spec['paper_id']}_failed_or_stopped", f"REFERENCE-ONLY {spec['paper_id']} failed/stopped; error={type(exc).__name__}: {str(exc)[:500]}; failure_sha256={failure_sha}; no auto-apply or protected mutation.", [failure_path, spec["prompt_path"]])
    records = list(state["papers"][spec["paper"] - 1].get("failure_records", []))
    records.append({"path": str(failure_path), "sha256": failure_sha, "ledger": entry})
    set_paper_state(state, spec["paper"], status="stopped_challenge" if isinstance(exc, GlobalChallengeStop) else "failed", failure_sha256=failure_sha, failure_ledger=entry, failure_records=records)
    report_hwao(f"DR-REVIEW-R1 {spec['paper_id']} FAILED/STOPPED reference-only: {type(exc).__name__}: {str(exc)[:500]}. failure={failure_path} sha={failure_sha}. No protected mutation. Next paper proceeds only if broker/target rails permit.")


def restore_submitted_owned_route(identity, spec, state, browser):
    """Restore one already-submitted exact-owned plan from /app without resubmitting."""
    path = identity["conversation_path"]
    if target_matches(path):
        return
    if not target_matches("/app"):
        raise TargetDrift(f"{spec['paper_id']} submitted-route restore requires current /app")
    holder = f"goru-dr-review-r1-{spec['paper_id']}-restore"
    client = UDSClient(SOCK)
    lease = None
    try:
        lease = acquire_target(client, holder, "write", ttl=300)
        page = exact_page(browser, "/app")
        check_action(client, lease, f"{spec['paper_id']} navigate to previously submitted exact-owned plan", "/app", page)
        page.goto("https://gemini.google.com" + path, wait_until="domcontentloaded", timeout=60000)
        page.wait_for_timeout(1800)
        check_action(client, lease, f"{spec['paper_id']} verify restored submitted exact-owned plan", path, page)
        if page_challenge(page):
            freeze_for_challenge(client, holder, spec["paper_id"], "submitted-route restoration")
        prompt = Path(spec["prompt_path"]).read_text().rstrip("\n")
        evidence = current_prompt_identity(page, prompt)
        if not evidence:
            raise PaperFailure("restored submitted route did not match its exact visible prompt")
        set_paper_state(
            state,
            spec["paper"],
            submitted_route_restored_utc=utcnow(),
            submitted_route_restore_evidence=evidence,
        )
    finally:
        release_lease(client, lease)
        client.close()


def run_one(spec, state, browser):
    paper_state = state["papers"][spec["paper"] - 1]
    if paper_state.get("status") == "completed":
        print(json.dumps({"paper": spec["paper_id"], "skip": "already completed"}), flush=True)
        return "completed"
    identity = paper_state.get("identity")
    try:
        if paper_state.get("status") == "failed":
            return "failed_continue" if target_matches("/app") else "blocked"
        if paper_state.get("status") == "pending":
            if Path(spec["packet_path"]).exists() or Path(spec["metadata_path"]).exists() or Path(spec["deletion_path"]).exists():
                raise PaperFailure("fresh pending paper has pre-existing output artifact")
            set_paper_state(state, spec["paper"], status="starting", started_utc=utcnow())
            identity = stage_and_submit(spec, state, browser)
            paper_state = state["papers"][spec["paper"] - 1]
        if identity is None:
            identity = state["papers"][spec["paper"] - 1].get("identity")
        if not identity:
            raise PaperFailure("missing durable conversation identity")
        current_status = state["papers"][spec["paper"] - 1].get("status")
        if current_status == "submitted":
            restore_submitted_owned_route(identity, spec, state, browser)
            plan = wait_for_plan(identity, spec, state, browser)
            if plan == "start_required":
                start_research(identity, spec, state, browser)
        current_status = state["papers"][spec["paper"] - 1].get("status")
        if current_status == "researching":
            snapshot, result_sha = poll_terminal(identity, spec, state, browser)
            save_packet(snapshot, result_sha, identity, spec, state)
        current_status = state["papers"][spec["paper"] - 1].get("status")
        if current_status == "saved_verified":
            delete_exact_own(identity, spec, state, browser)
        final = state["papers"][spec["paper"] - 1]
        if final.get("status") != "completed":
            raise PaperFailure(f"unexpected final paper state {final.get('status')}")
        report_hwao(f"DR-REVIEW-R1 {spec['paper_id']} COMPLETE reference-only. packet={spec['packet_path']} sha={final['packet_sha256']} sources={final['result']['source_anchor_count']} result_chars={final['result']['chars']}; exact-own conversation {identity['conversation_id']} deleted only after save epoch {final['save_ledger']['epoch']}; deletion sha={final['deletion_sha256']}. advisory_only=true; no .tex/DB/autopilot/auto-apply. Proceeding to next paper.")
        print(json.dumps({"paper": spec["paper_id"], "status": "completed", "packet": spec["packet_path"], "packet_sha256": final["packet_sha256"]}), flush=True)
        return "completed"
    except Exception as exc:
        write_failure(spec, state, exc, identity)
        if isinstance(exc, GlobalChallengeStop):
            return "global_stop"
        recovered = False
        with suppress(Exception):
            recovered = recover_new_chat(identity, spec, browser)
        print(json.dumps({"paper": spec["paper_id"], "status": "failed", "recovered_new_chat": recovered, "error": str(exc)}), flush=True)
        return "failed_continue" if recovered and target_matches("/app") else "blocked"


def write_summary(state, final=True):
    statuses = {}
    total_sources = 0
    for paper in state["papers"]:
        statuses[paper.get("status", "unknown")] = statuses.get(paper.get("status", "unknown"), 0) + 1
        total_sources += paper.get("result", {}).get("source_anchor_count", 0)
    lines = [
        "# Deep Research 9-paper batch summary — REFERENCE-ONLY", "",
        f"Batch ID: `{state['batch_id']}`", f"Summary UTC: `{utcnow()}`", "advisory_only: true", "reference_only: true", "",
        "## Hard boundary", "", "No `.tex`, DB, autopilot-lane, auto-apply, deploy, git, publish, cron, billing, account-setting, credential, secret, bulk-history, or unrelated-conversation mutation was authorized or performed. Exact-owned conversation cleanup occurred only after verified packet save.", "",
        "## Totals", "", f"- Status counts: `{json.dumps(statuses, sort_keys=True)}`", f"- Captured source anchors across completed packets: `{total_sources}`", "",
        "## Papers", "",
    ]
    for paper in state["papers"]:
        lines.extend([
            f"### {paper['paper_id']} — {paper['shortname']}", "",
            f"- status: `{paper.get('status')}`", f"- prompt_sha256: `{paper['prompt_sha256']}`",
            f"- packet: `{paper['packet_path']}`", f"- packet_sha256: `{paper.get('packet_sha256','')}`",
            f"- metadata_sha256: `{paper.get('metadata_sha256','')}`", f"- source_anchor_count: `{paper.get('result',{}).get('source_anchor_count',0)}`",
            f"- conversation_id: `{paper.get('identity',{}).get('conversation_id','')}`", f"- deletion_sha256: `{paper.get('deletion_sha256','')}`",
            f"- failure_sha256: `{paper.get('failure_sha256','')}`", "",
        ])
    lines.extend(["## Downstream gate", "", "These packets are advisory references only. Tori/WonE validators must verify identifiers, source roles, wording, and manuscript fit before any separately approved candidate-copy edit. Nothing is auto-applied.", ""])
    summary_path = SUMMARY_PATH if final else HOLD_SUMMARY_PATH
    atomic_write(summary_path, "\n".join(lines))
    summary_sha = sha_file(summary_path)
    prefix = "final_summary" if final else "hold_summary"
    state[prefix + "_path"] = str(summary_path)
    state[prefix + "_sha256"] = summary_sha
    state["completed_utc" if final else "held_utc"] = utcnow()
    save_state(state)
    entry_type = "dr_review_r1_reference_batch_final_summary" if final else "dr_review_r1_reference_batch_hold_summary"
    entry = journal_entry(entry_type, f"9-paper Deep Research REFERENCE-ONLY {'final' if final else 'hold'} summary; summary_sha256={summary_sha}; status_counts={json.dumps(statuses,sort_keys=True)}; source_anchors={total_sources}; no .tex/DB/autopilot/auto-apply mutation.", [summary_path])
    state[prefix + "_ledger"] = entry
    save_state(state)
    return statuses, total_sources, summary_sha, entry, summary_path


def dry_run(specs):
    ok, message = ledger.verify(LEDGER_PATH)
    record = target_record()
    state = json.loads(Path("broker/live_state.json").read_text())
    outputs = [path for spec in specs for path in (spec["packet_path"], spec["metadata_path"], spec["deletion_path"], spec["failure_path"]) if Path(path).exists()]
    result = {"status": "PASS" if ok and record and record["path"] == "/app" and not state.get("frozen") and not outputs else "FAIL", "ledger": message, "target": record, "broker_frozen": state.get("frozen"), "prompt_count": len(specs), "prompt_hashes": {spec["paper_id"]: spec["prompt_sha256"] for spec in specs}, "preexisting_outputs": outputs, "write_root": str(PACKET_DIR), "advisory_only": True}
    print(json.dumps(result, sort_keys=True))
    return 0 if result["status"] == "PASS" else 1


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--dry-run", action="store_true")
    parser.add_argument("--start", type=int, default=1)
    parser.add_argument("--end", type=int, default=9)
    args = parser.parse_args()
    specs = discover_prompts()
    if args.dry_run:
        return dry_run(specs)
    state = load_or_create_state(specs)
    report_hwao(f"DR-REVIEW-R1 batch runner ACTIVE starting paper_{args.start:02d}; reference-only packets under {PACKET_DIR}; exact target {TARGET_ID}; one run at a time; no protected mutation.")
    global_stop = False; blocked = False
    with sync_playwright() as playwright:
        browser = playwright.chromium.connect_over_cdp(BASE)
        for spec in specs:
            if spec["paper"] < args.start or spec["paper"] > args.end:
                continue
            if global_stop or blocked:
                set_paper_state(state, spec["paper"], status="not_run_global_freeze" if global_stop else "not_run_target_blocked")
                continue
            outcome = run_one(spec, state, browser)
            if outcome == "global_stop":
                global_stop = True
            elif outcome == "blocked":
                blocked = True
    final = not global_stop and not blocked
    statuses, total_sources, summary_sha, entry, summary_path = write_summary(state, final=final)
    report_hwao(f"DR-REVIEW-R1 BATCH {'FINISHED' if final else 'HELD'} reference-only. statuses={json.dumps(statuses,sort_keys=True)} total_source_anchors={total_sources}; summary={summary_path} sha={summary_sha}; ledger epoch={entry['epoch']} VERIFY_OK. No .tex/DB/autopilot/auto-apply. Any global freeze/blocked papers require explicit human disposition.")
    print(json.dumps({"batch_finished": final, "batch_held": not final, "statuses": statuses, "total_source_anchors": total_sources, "summary": str(summary_path), "summary_sha256": summary_sha, "ledger": entry}), flush=True)
    return 0 if statuses.get("completed", 0) == args.end - args.start + 1 else 2


if __name__ == "__main__":
    raise SystemExit(main())
