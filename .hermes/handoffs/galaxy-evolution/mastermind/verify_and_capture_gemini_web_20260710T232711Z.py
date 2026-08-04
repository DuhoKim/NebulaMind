#!/usr/bin/env python3
import hashlib
import json
import subprocess
import time
from datetime import datetime, timezone
from pathlib import Path

MASTER = Path(__file__).resolve().parent
REQUEST_ID = "JOURNAL_CYCLE7_GEMINI_WEB_20260710T232711Z"
CONVERSATION_PREFIX = "https://gemini.google.com/app/e967f0de5039067e"
JS_PATH = Path("/tmp/gemini_web_capture_state.js")
OUTPUT_DIR = MASTER / "gemini-web-deep-research/outputs" / REQUEST_ID
OUTPUT = OUTPUT_DIR / "GEMINI_WEB_OUTPUT.md"
LINKS = OUTPUT_DIR / "GEMINI_WEB_OUTPUT.links.json"
META = OUTPUT_DIR / "GEMINI_WEB_OUTPUT.meta.json"
STATUS = OUTPUT_DIR / "CAPTURE_STATUS.json"
MARKER = "GEMINI_WEB_RT_DEEP_RESEARCH_OUTPUT_DONE"
DEADLINE = time.time() + 7200


def now() -> str:
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def write_json(path: Path, payload: dict) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def capture_state() -> dict:
    script = f'''set jsCode to (read (POSIX file "{JS_PATH}") as «class utf8»)
tell application "Google Chrome"
  repeat with w in windows
    repeat with t in tabs of w
      if (URL of t) starts with "{CONVERSATION_PREFIX}" then return execute t javascript jsCode
    end repeat
  end repeat
  return "NO_CONVERSATION_TAB"
end tell'''
    cp = subprocess.run(["osascript", "-e", script], text=True, capture_output=True, timeout=30)
    if cp.returncode != 0:
        raise RuntimeError(cp.stderr.strip() or f"osascript exit {cp.returncode}")
    raw = cp.stdout.strip()
    if raw == "NO_CONVERSATION_TAB":
        raise RuntimeError(raw)
    return json.loads(raw)


OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
write_json(STATUS, {"state": "research_running", "request_id": REQUEST_ID, "started_utc": now()})
last_state = {}
while time.time() < DEADLINE:
    try:
        last_state = capture_state()
        responses = last_state.get("responses") or []
        last = responses[-1].strip() if responses else ""
        report = (last_state.get("reportText") or "").strip()
        links = last_state.get("reportLinks") or []
        progress_only = last.startswith("I'm on it. I'll let you know when your research is done")
        write_json(
            STATUS,
            {
                "state": "research_running" if last_state.get("generating") or progress_only else "response_observed",
                "request_id": REQUEST_ID,
                "checked_utc": now(),
                "generating": bool(last_state.get("generating")),
                "response_count": len(responses),
                "last_response_chars": len(last),
                "report_chars": len(report),
                "report_links": len(links),
                "marker_present_in_report": MARKER in report,
            },
        )
        if not last_state.get("generating") and len(report) >= 1000:
            text = report + ("\n" if not report.endswith("\n") else "")
            OUTPUT.write_text(text, encoding="utf-8")
            write_json(LINKS, {"request_id": REQUEST_ID, "links": links})
            digest = hashlib.sha256(text.encode("utf-8")).hexdigest()
            meta = {
                "request_id": REQUEST_ID,
                "captured_utc": now(),
                "capture_method": "supervised-chrome-applescript-dom-deep-research-report",
                "conversation_url": last_state.get("url"),
                "bytes": len(text.encode("utf-8")),
                "sha256": digest,
                "required_marker": MARKER,
                "marker_present": MARKER in text,
                "response_count": len(responses),
                "report_chars": len(report),
                "report_links": len(links),
                "link_ledger": LINKS.name,
                "advisory_only": True,
                "source_verification_complete": False,
                "safety_ledger": {
                    "credentials_read": False,
                    "billing_or_account_opened": False,
                    "api_or_gcp_opened": False,
                    "live_runner_touched": False,
                    "product_or_public_write": False,
                },
            }
            write_json(META, meta)
            write_json(STATUS, {"state": "captured_unverified", "request_id": REQUEST_ID, "completed_utc": now(), "marker_present": MARKER in text, "bytes": meta["bytes"], "sha256": digest})
            print(json.dumps(meta, sort_keys=True), flush=True)
            raise SystemExit(0 if meta["marker_present"] else 4)
    except Exception as exc:
        write_json(STATUS, {"state": "capture_retry", "request_id": REQUEST_ID, "checked_utc": now(), "error": f"{type(exc).__name__}: {exc}"})
    time.sleep(30)

write_json(STATUS, {"state": "timeout", "request_id": REQUEST_ID, "completed_utc": now(), "last_state": last_state})
raise SystemExit(3)
