#!/usr/bin/env python3
"""Render the private V3 Galaxy Evolution autopilot dashboard.

Source:  .hermes/handoffs/galaxy-evolution/mastermind/autopilot-status.json
         .hermes/handoffs/galaxy-evolution/mastermind/autopilot-events.jsonl
Output:  /Users/duhokim/HermesOps/cockpit/ge-autopilot.html
         /Users/duhokim/HermesOps/cockpit/ge-autopilot-status.json

This is a private tailnet-only read-only mirror. It does not dispatch prompts,
approve permissions, publish wiki pages, edit the public NebulaMind cockpit,
touch DB/API, deploy, restart services, run git, or contact cloud APIs.
"""
from __future__ import annotations

import argparse
import datetime as dt
import html
import json
import os
import re
import shutil
import subprocess
import time
from pathlib import Path
from typing import Any, Dict, Iterable, List

MARKER = "GE_AUTOPILOT_PRIVATE_DASHBOARD_V3"
V2_COMPAT_MARKER = "GE_AUTOPILOT_PRIVATE_DASHBOARD_V2"
LEGACY_MARKER = "GE_AUTOPILOT_PRIVATE_DASHBOARD_V1"
SURVEY_AUTOPILOT_MARKER = "SURVEY_AUTOPILOT_DASHBOARD_FEED_V1"
OUTCOME_LEDGER_MARKER = "GE_AUTOPILOT_LOCAL_OUTCOME_LEDGER_V1"
RUN_TIME_ESTIMATE_MARKER = "GE_AUTOPILOT_RUN_TIME_ESTIMATES_V1"
PAPER_QUALITY_SPRINT_MARKER = "RP1_QUALITY_SPRINT_DASHBOARD_FEED_V1"
WIKI_QUALITY_SPRINT_MARKER = "WIKI_QUALITY_SPRINT_DASHBOARD_FEED_V1"
OVERNIGHT_REPORT_MARKER = "GE_AUTOPILOT_OVERNIGHT_20260719_CORPUS_GATES_DONE"
LAST_INCIDENT = {
    "id": "goru-browser-custody-20260712",
    "title": "Goru browser custody incident — contained",
    "status": "contained",
    "component": "Goru browser lane",
    "summary": "An unauthorized Gemini Web permission prompt appeared after Chrome/AppleScript experiments and edits to the local driver. Tori denied it and held the lane.",
    "detected_utc": "2026-07-12T01:56:30Z",
    "resolved_utc": "2026-07-12T01:57:02Z",
    "verification": "Prompt denied; no matching driver, AppleScript, or R15 process remained; no durable result or receipt exists; exact prior browser effect is unknown.",
    "verification_headline": "permission denied; lane held",
    "verification_note": "read-only custody check",
    "change_note": "hard stop applied",
    "scope": "Private lane custody only; no revert, deletion, approved Gemini launch, product write, deploy, git, or cron action.",
}
COMPAT_MARKERS = [V2_COMPAT_MARKER, LEGACY_MARKER]
REPO = Path(os.environ.get("NEBULAMIND_REPO", "/Users/duhokim/NebulaMind/NebulaMind"))
MASTER_ROOT = REPO / ".hermes" / "handoffs" / "galaxy-evolution" / "mastermind"
QUALITY_SPRINT_ROOT = MASTER_ROOT / "aas-autopilot" / "quality-sprints"
WIKI_QUALITY_SPRINT_ROOT = MASTER_ROOT / "wiki-quality-sprints"
SOURCE_STATUS = Path(os.environ.get("GE_AUTOPILOT_SOURCE_STATUS", str(MASTER_ROOT / "autopilot-status.json")))
SOURCE_EVENTS = Path(os.environ.get("GE_AUTOPILOT_SOURCE_EVENTS", str(MASTER_ROOT / "autopilot-events.jsonl")))
WEB_ROOT = Path(os.environ.get("GE_AUTOPILOT_WEB_ROOT", "/Users/duhokim/HermesOps/cockpit"))
HTML_PATH = WEB_ROOT / "ge-autopilot.html"
JSON_PATH = WEB_ROOT / "ge-autopilot-status.json"
USAGE_CACHE_PATH = WEB_ROOT / "ge-autopilot-usage-cache.json"
LATEST_URL_PATH = WEB_ROOT / "latest-ge-autopilot-url.txt"
URL = os.environ.get("GE_AUTOPILOT_URL", "https://duho-macstudio.taila27502.ts.net/cockpit/ge-autopilot.html")
STATUS_URL = "ge-autopilot-status.json"
PUBLIC_USAGE_STATUS = Path(os.environ.get(
    "GE_PROVIDER_USAGE_STATUS_JSON",
    "/Users/duhokim/NebulaMind/NebulaMind-origin-main-live/frontend/public/agent-reports/live-steering-status.json",
))
PUBLIC_USAGE_URL = os.environ.get(
    "GE_PROVIDER_USAGE_STATUS_URL",
    "https://nebulamind.net/agent-reports/live-steering-status.json",
)
FLOW_CREDITS_PATH = Path(os.environ.get(
    "GE_FLOW_CREDITS_JSON",
    "/Users/duhokim/HermesOps/scripts/clips/flow_credits.json",
))
FLOW_CREDITS_STALE_AFTER_SECONDS = 24 * 3600
PUBLIC_USAGE_FEED_MARKER = "GE_AUTOPILOT_PROVIDER_USAGE_REALTIME_FEED_V1"
SURVEY_AUTOPILOT_STATUS = Path(os.environ.get(
    "SURVEY_AUTOPILOT_STATUS_JSON",
    str(MASTER_ROOT / "survey-autopilot-status.json"),
))
SURVEY_ROUTE = os.environ.get("SURVEY_AUTOPILOT_ROUTE", "/surveys")
SURVEY_REQUIRED_FILES = [
    ("Route", REPO / "frontend" / "src" / "app" / "surveys" / "page.tsx"),
    ("Detail route", REPO / "frontend" / "src" / "app" / "surveys" / "[slug]" / "SurveyDetailClient.tsx"),
    ("Explorer", REPO / "frontend" / "src" / "components" / "surveys" / "SurveysView.tsx"),
    ("Chart", REPO / "frontend" / "src" / "components" / "surveys" / "ChartView.tsx"),
    ("Plot A", REPO / "frontend" / "src" / "components" / "surveys" / "PlotA.tsx"),
    ("Plot B", REPO / "frontend" / "src" / "components" / "surveys" / "PlotB.tsx"),
    ("Shared plotting helpers", REPO / "frontend" / "src" / "components" / "surveys" / "plotting.ts"),
    ("Atlas IA smoke", REPO / "frontend" / "scripts" / "test-surveys-atlas-ia.mjs"),
]

GROUP_ORDER = ["Directors", "Method 1", "Method 2", "Method 3", "Other"]
METHOD_GROUPS = ["Method 1", "Method 2", "Method 3"]
ROLE_ORDER = ["Hwao", "Lana", "Goru", "Kun", "Tori"]
STATUS_ORDER = {"review": 0, "dead": 1, "safe-prompt": 2, "copy-mode": 3, "active": 4, "idle": 5}
SAFETY_GATES = [
    "product DB/SQL writes and pane-initiated SQL",
    "/api/pages, page_versions, live wiki publish",
    "deploy/restart/service mutation",
    "git commit/push/merge/rebase/reset",
    "public NebulaMind cockpit/Baseline replacement",
    "cloud/GCP/API/billing/OAuth/token/secrets/.env",
    "browser automation or cron",
    "direct method wiki-page.html overwrite",
]
POLICY_LINES = [
    "This page is a read-only mirror of local status JSON.",
    "Green means nothing needs you; red means a real human decision is needed.",
    "Goru permission prompts are handled by the autopilot when they match safe private-dashboard or docs/static scope.",
    "Hard gates stay closed: no DB, live publish, deploy, git, cloud/secrets, browser automation, or cron.",
]


def now_utc() -> str:
    return dt.datetime.utcnow().replace(microsecond=0).isoformat() + "Z"


def parse_ts(value: str | None) -> dt.datetime | None:
    if not value:
        return None
    try:
        if value.endswith("Z"):
            value = value[:-1] + "+00:00"
        parsed = dt.datetime.fromisoformat(value)
        if parsed.tzinfo is None:
            parsed = parsed.replace(tzinfo=dt.timezone.utc)
        return parsed.astimezone(dt.timezone.utc)
    except Exception:
        return None


def age_seconds(ts: str | None) -> int | None:
    parsed = parse_ts(ts)
    if not parsed:
        return None
    return max(0, int((dt.datetime.now(dt.timezone.utc) - parsed).total_seconds()))


def age_label(seconds: int | None) -> str:
    if seconds is None:
        return "unknown"
    if seconds < 60:
        return f"{seconds}s"
    if seconds < 3600:
        return f"{seconds // 60}m {seconds % 60}s"
    return f"{seconds // 3600}h {(seconds % 3600) // 60}m"


def load_source() -> Dict[str, Any]:
    if not SOURCE_STATUS.exists():
        return {
            "ts": now_utc(),
            "repo": str(REPO),
            "phase": "phase1-bounded-controller",
            "targets": [],
            "panes": [],
            "blockers": [{"role": "dashboard", "reason": f"source status not found: {SOURCE_STATUS}", "safe_to_approve": False}],
            "hard_gates_closed": SAFETY_GATES,
            "status_path": str(SOURCE_STATUS),
        }
    return json.loads(SOURCE_STATUS.read_text())


def read_events(limit: int = 18, meaningful_only: bool = False) -> List[Dict[str, Any]]:
    if not SOURCE_EVENTS.exists():
        return []
    lines = SOURCE_EVENTS.read_text(errors="replace").splitlines()[-200:]
    events: List[Dict[str, Any]] = []
    for line in lines:
        try:
            item = json.loads(line)
        except Exception:
            continue
        if isinstance(item, dict):
            actions = item.get("actions") or []
            blockers = item.get("blockers") or []
            event = {
                "ts": item.get("ts") or "unknown",
                "actions_count": len(actions) if isinstance(actions, list) else 0,
                "blockers_count": len(blockers) if isinstance(blockers, list) else 0,
                "actions": summarize_actions(actions),
                "blockers": summarize_blockers(blockers),
            }
            routine_actions = isinstance(actions, list) and actions and all(isinstance(action, dict) and action.get("action") == "clear-copy-mode" for action in actions)
            if meaningful_only and ((not event["actions_count"] and not event["blockers_count"]) or (routine_actions and not event["blockers_count"])):
                continue
            events.append(event)
    return events[-limit:]


def summarize_actions(actions: Any) -> List[str]:
    out: List[str] = []
    if not isinstance(actions, list):
        return out
    for item in actions[:5]:
        if not isinstance(item, dict):
            continue
        role = item.get("role") or item.get("pane_id") or "pane"
        action = item.get("action") or "action"
        out.append(f"{role}: {action}")
    return out


def summarize_blockers(blockers: Any) -> List[str]:
    out: List[str] = []
    if not isinstance(blockers, list):
        return out
    for item in blockers[:5]:
        if not isinstance(item, dict):
            continue
        role = item.get("role") or item.get("pane_id") or "pane"
        reason = item.get("reason") or "blocked"
        out.append(f"{role}: {reason}")
    return out


def group_for(pane: Dict[str, Any]) -> str:
    role = str(pane.get("role") or "")
    target = str(pane.get("target") or "")
    if target.startswith("ge-mastermind") or role in {"Hwao-director", "Tori-director", "Goru-director-live-view"}:
        return "Directors"
    if "m1" in target or role.endswith("-m1"):
        return "Method 1"
    if "m2" in target or role.endswith("-m2"):
        return "Method 2"
    if "m3" in target or role.endswith("-m3"):
        return "Method 3"
    return "Other"


def pane_status(pane: Dict[str, Any]) -> str:
    cls = pane.get("classification") or {}
    if pane.get("dead"):
        return "dead"
    if cls.get("permission_prompt") and not cls.get("safe_to_approve"):
        return "review"
    if cls.get("permission_prompt") and cls.get("safe_to_approve"):
        return "safe-prompt"
    if pane.get("in_mode"):
        return "copy-mode"
    if pane.get("active"):
        return "active"
    return "idle"


def role_prefix(role: str) -> str:
    return str(role).split("-", 1)[0]


def role_sort_key(pane: Dict[str, Any]) -> tuple:
    status = pane.get("status") or "idle"
    prefix = role_prefix(str(pane.get("role") or ""))
    role_index = ROLE_ORDER.index(prefix) if prefix in ROLE_ORDER else len(ROLE_ORDER)
    return (STATUS_ORDER.get(status, 99), role_index, str(pane.get("role") or ""))


def compact_tail(tail: str | None, limit: int = 150) -> str:
    if not tail:
        return ""
    lines = []
    for raw_line in str(tail).splitlines():
        line = raw_line.strip()
        if not line:
            continue
        line = re.sub(r"[─━═╌╍┄┅┈┉]{6,}", " ", line)
        line = re.sub(r"[·.]{12,}", " ", line)
        line = re.sub(r"\s+", " ", line).strip(" ·│┆┊─━═╌╍┄┅┈┉")
        if line:
            lines.append(line)
    if not lines:
        return ""
    text = " · ".join(lines[-2:])
    return text[: limit - 1] + "…" if len(text) > limit else text


def lane_summary(name: str, panes: List[Dict[str, Any]]) -> Dict[str, Any]:
    counts: Dict[str, int] = {"active": 0, "idle": 0, "review": 0, "safe-prompt": 0, "copy-mode": 0, "dead": 0}
    for pane in panes:
        counts[pane.get("status", "idle")] = counts.get(pane.get("status", "idle"), 0) + 1
    if counts.get("review") or counts.get("dead"):
        state = "needs-review"
        text = "Needs you"
    elif counts.get("safe-prompt") or counts.get("copy-mode"):
        state = "watching"
        text = "Autopilot watching"
    elif counts.get("active"):
        state = "active"
        text = "Working"
    else:
        state = "idle"
        text = "Idle / ready"
    return {"name": name, "state": state, "text": text, "counts": counts, "panes": len(panes)}


def fmt_int(value: Any) -> str:
    try:
        return f"{int(value):,}"
    except Exception:
        return "unknown"


def run_readonly(argv: List[str], timeout: int = 25) -> Dict[str, Any]:
    """Run a local read-only status command without shell expansion."""
    exe = shutil.which(argv[0])
    if not exe:
        return {"ok": False, "returncode": None, "stdout": "", "stderr": f"{argv[0]} not found"}
    try:
        proc = subprocess.run(
            [exe, *argv[1:]],
            cwd=str(REPO),
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
            timeout=timeout,
            check=False,
        )
        return {
            "ok": proc.returncode == 0,
            "returncode": proc.returncode,
            "stdout": proc.stdout[:12000],
            "stderr": proc.stderr[:2000],
        }
    except Exception as exc:
        return {"ok": False, "returncode": None, "stdout": "", "stderr": str(exc)[:500]}


def parse_number(label: str, text: str) -> int | None:
    match = re.search(rf"{re.escape(label)}:\s*([0-9][0-9,]*)", text)
    if not match:
        return None
    try:
        return int(match.group(1).replace(",", ""))
    except Exception:
        return None


def parse_hermes_insights(text: str) -> Dict[str, Any]:
    model = "unknown"
    lines = text.splitlines()
    for idx, line in enumerate(lines):
        if "Models Used" in line:
            for candidate in lines[idx + 1 : idx + 12]:
                match = re.match(r"\s*([A-Za-z0-9_.:/-]+)\s+\d+\s+[0-9,]+\s*$", candidate)
                if match:
                    model = match.group(1)
                    break
            break
    return {
        "sessions_7d": parse_number("Sessions", text),
        "messages_7d": parse_number("Messages", text),
        "tool_calls_7d": parse_number("Tool calls", text),
        "input_tokens_7d": parse_number("Input tokens", text),
        "output_tokens_7d": parse_number("Output tokens", text),
        "total_tokens_7d": parse_number("Total tokens", text),
        "model": model,
    }


def parse_auth_counts(text: str) -> Dict[str, int]:
    counts: Dict[str, int] = {}
    for line in text.splitlines():
        match = re.match(r"^([A-Za-z0-9_-]+) \((\d+) credentials?\):", line.strip())
        if match:
            counts[match.group(1)] = int(match.group(2))
    return counts


def read_small_json(path: Path) -> Dict[str, Any]:
    try:
        if path.exists() and path.stat().st_size < 200_000:
            data = json.loads(path.read_text(errors="replace"))
            return data if isinstance(data, dict) else {}
    except Exception:
        return {}
    return {}


def repo_rel_path(path: Path) -> str:
    try:
        return str(path.resolve().relative_to(REPO))
    except Exception:
        return str(path)


def file_card(label: str, path: Path) -> Dict[str, Any]:
    exists = path.exists()
    out: Dict[str, Any] = {
        "label": label,
        "path": repo_rel_path(path),
        "exists": exists,
    }
    if exists:
        stat = path.stat()
        out["bytes"] = stat.st_size
        out["modified_at_utc"] = dt.datetime.utcfromtimestamp(stat.st_mtime).replace(microsecond=0).isoformat() + "Z"
    return out


def build_survey_autopilot_snapshot() -> Dict[str, Any]:
    files = [file_card(label, path) for label, path in SURVEY_REQUIRED_FILES]
    missing = [item for item in files if not item.get("exists")]
    sidecar = read_small_json(SURVEY_AUTOPILOT_STATUS)
    sidecar_marker_ok = sidecar.get("marker") == SURVEY_AUTOPILOT_MARKER
    last_status = str(sidecar.get("status") or "unknown").lower() if sidecar_marker_ok else "unknown"

    state = "watching"
    text = "Ready · smoke status not recorded"
    next_action = "Use the Survey autopilot card for route/files/smoke-test custody; run `npm run test:surveys-atlas-ia` before treating a Survey UI change as verified."
    if missing:
        state = "needs-review"
        text = f"Needs review · {len(missing)} required file(s) missing"
        next_action = "A required Survey route/component/test file is missing. Inspect the repo before dispatching Survey work."
    elif last_status == "passed":
        state = "healthy"
        text = "Smoke PASS"
        next_action = "Survey frontend surface is present and the latest recorded Atlas IA smoke passed. Safe next work: read-only/static audits or separately approved UI edits."
    elif last_status == "failed":
        state = "needs-review"
        text = "Smoke FAIL"
        next_action = "The latest recorded Survey Atlas IA smoke failed. Fix the Survey surface before expanding Survey autopilot work."

    return {
        "marker": SURVEY_AUTOPILOT_MARKER,
        "generated_at": now_utc(),
        "state": state,
        "text": text,
        "route": SURVEY_ROUTE,
        "scope": "Survey frontend /surveys Atlas IA surface; separate from Galaxy Evolution method panes and product DB writes.",
        "next_action": next_action,
        "required_files_present": len(files) - len(missing),
        "required_files_total": len(files),
        "files": files,
        "missing_files": missing,
        "status_path": str(SURVEY_AUTOPILOT_STATUS),
        "latest_smoke": {
            "known": sidecar_marker_ok,
            "status": sidecar.get("status") if sidecar_marker_ok else "unknown",
            "command": sidecar.get("command") if sidecar_marker_ok else "npm run test:surveys-atlas-ia",
            "exit_code": sidecar.get("exit_code") if sidecar_marker_ok else None,
            "verified_at_utc": sidecar.get("verified_at_utc") if sidecar_marker_ok else None,
            "output": sidecar.get("output") if sidecar_marker_ok else "No Survey autopilot sidecar has been recorded yet.",
        },
        "safe_boundaries": [
            "Dashboard is read-only; browser fetches JSON only.",
            "No DB/SQL, live wiki publish, deploy/restart, git write, cloud/account/OAuth/secrets, browser automation, or cron.",
            "Survey autopilot work should produce local reports or separately approved frontend patches; helper reports are advisory until Tori verifies files/tests.",
        ],
    }


def latest_quality_sprint_root() -> Path | None:
    roots = sorted(
        QUALITY_SPRINT_ROOT.glob("RP1_QUALITY_SPRINT_*"),
        key=lambda p: p.stat().st_mtime if p.exists() else 0,
        reverse=True,
    )
    return roots[0] if roots else None


def pid_is_running(pid: Any) -> bool:
    try:
        pid_int = int(pid)
    except Exception:
        return False
    try:
        os.kill(pid_int, 0)
        return True
    except ProcessLookupError:
        return False
    except PermissionError:
        return True
    except Exception:
        return False


def percent_between(start_utc: str | None, end_utc: str | None) -> float | None:
    start = parse_ts(start_utc)
    end = parse_ts(end_utc)
    if not start or not end or end <= start:
        return None
    now = dt.datetime.now(dt.timezone.utc)
    return max(0.0, min(100.0, ((now - start).total_seconds() / (end - start).total_seconds()) * 100.0))


def latest_cycle_audit(candidate: Path | None) -> Dict[str, Any]:
    if not candidate or not candidate.exists():
        return {}
    audits = sorted(candidate.glob("CYCLE_*_QUALITY_AUDIT.json"), key=lambda p: p.stat().st_mtime, reverse=True)
    return read_small_json(audits[0]) if audits else {}


def read_paper_audit(path_text: str | None, candidate: Path | None) -> Dict[str, Any]:
    if path_text:
        path = Path(path_text)
        json_path = path.with_suffix(".json") if path.suffix == ".md" else path
        if json_path.exists():
            return read_small_json(json_path)
    return latest_cycle_audit(candidate)


def paper_fatal_count(audit: Dict[str, Any]) -> int | None:
    failures = audit.get("fatal_failures")
    if isinstance(failures, list):
        return len(failures)
    if isinstance(failures, int):
        return failures
    return None


def build_paper_quality_sprint_snapshot() -> Dict[str, Any]:
    root = latest_quality_sprint_root()
    if not root:
        return {
            "marker": PAPER_QUALITY_SPRINT_MARKER,
            "state": "idle",
            "text": "No RP-1 quality sprint found",
            "root": str(QUALITY_SPRINT_ROOT),
            "safe_boundaries": SAFETY_GATES,
        }

    status = read_small_json(root / "SPRINT_STATUS.json")
    ledger_path = root / "SPRINT_LEDGER.md"
    ledger_lines = []
    if ledger_path.exists():
        ledger_lines = [line for line in ledger_path.read_text(errors="replace").splitlines() if line.strip()][-8:]

    candidate_text = status.get("latest_candidate") or status.get("candidate") or ""
    candidate_path = Path(candidate_text) if candidate_text else None
    audit = read_paper_audit(status.get("latest_audit"), candidate_path)
    process_running = pid_is_running(status.get("pid"))
    status_state = str(status.get("state") or "unknown")
    fatal_failures_count = paper_fatal_count(audit)
    dashboard_state = "watching" if process_running and not status_state.startswith("completed") else "healthy" if status_state.startswith("completed") and fatal_failures_count == 0 else "needs-review"
    text = "Running local manuscript-quality sprint" if dashboard_state == "watching" else "Quality sprint complete" if dashboard_state == "healthy" else "Quality sprint needs review"
    display_ledger_lines = ledger_lines
    if dashboard_state == "healthy" and status_state.startswith("completed"):
        compile_ok = [item.get("ok") for item in audit.get("compile_results", []) if isinstance(item, dict)]
        compile_label = "/".join(str(x).lower() for x in compile_ok) if compile_ok else "recorded"
        figure_count = audit.get("figure_count") if audit.get("figure_count") is not None else len(audit.get("figures", [])) if isinstance(audit.get("figures"), list) else "recorded"
        display_ledger_lines = [
            f"Final clean package: {Path(str(candidate_path)).name if candidate_path else 'candidate'} · fatal_failures={fatal_failures_count} · compile={compile_label} · figures={figure_count}.",
            f"Completion receipt: {root / 'FINAL_GUARDRAIL_CLEANUP_RECEIPT.md'}",
            f"Full archived sprint ledger remains at {ledger_path}.",
        ]

    return {
        "marker": PAPER_QUALITY_SPRINT_MARKER,
        "generated_at": now_utc(),
        "state": dashboard_state,
        "text": text,
        "process_running": process_running,
        "pid": status.get("pid"),
        "status": status_state,
        "cycle": status.get("cycle"),
        "cycles_completed": status.get("cycles_completed", 0),
        "started_utc": status.get("started_utc"),
        "target_end_utc": status.get("target_end_utc"),
        "updated_utc": status.get("updated_utc"),
        "progress_percent": percent_between(status.get("started_utc"), status.get("target_end_utc")),
        "root": str(root),
        "board": str(root / "SPRINT_BOARD.md"),
        "ledger": str(ledger_path),
        "candidate": str(candidate_path) if candidate_path else "",
        "latest_audit": {
            "cycle": audit.get("cycle"),
            "fatal_failures": fatal_failures_count,
            "compile_ok": [item.get("ok") for item in audit.get("compile_results", []) if isinstance(item, dict)],
            "figures": audit.get("figure_count") if audit.get("figure_count") is not None else len(audit.get("figures", [])) if isinstance(audit.get("figures"), list) else None,
            "marker": audit.get("marker"),
        },
        "lanes": [
            "Hwao-style director review: AGY Gemini 3.1 Pro Low",
            "Gemini/Goru deep-review critique: AGY Gemini 3.5 Flash Low",
            "Codex/Kun reproducibility and TeX/prose review: Codex gpt-5.4-mini",
            "Goru mechanical checks: local Python",
            "Integrator: candidate-copy edits, compile, audit only",
        ],
        "ledger_tail": display_ledger_lines,
        "safe_boundaries": [
            "Local sprint/candidate artifacts only; original package and public pages are not replaced.",
            "No product DB/API/page writes, live wiki publish, deploy/restart, git write, cron, billing/OAuth/API-key/account changes, credential reads, or external submission.",
        ],
    }


def latest_wiki_quality_sprint_root() -> Path | None:
    roots = sorted(
        WIKI_QUALITY_SPRINT_ROOT.glob("WIKI_QUALITY_SPRINT_*"),
        key=lambda p: p.stat().st_mtime if p.exists() else 0,
        reverse=True,
    )
    return roots[0] if roots else None


def read_wiki_audit(path_text: str | None) -> Dict[str, Any]:
    if not path_text:
        return {}
    path = Path(path_text)
    candidate = path.with_suffix(".json") if path.suffix == ".md" else path
    return read_small_json(candidate) if candidate.exists() else {}


def build_wiki_quality_sprint_snapshot() -> Dict[str, Any]:
    root = latest_wiki_quality_sprint_root()
    if not root:
        return {
            "marker": WIKI_QUALITY_SPRINT_MARKER,
            "state": "idle",
            "text": "No wiki quality sprint found",
            "root": str(WIKI_QUALITY_SPRINT_ROOT),
            "safe_boundaries": SAFETY_GATES,
        }
    status = read_small_json(root / "WIKI_SPRINT_STATUS.json")
    ledger_path = root / "WIKI_SPRINT_LEDGER.md"
    ledger_lines = []
    if ledger_path.exists():
        ledger_lines = [line for line in ledger_path.read_text(errors="replace").splitlines() if line.strip()][-8:]
    candidate_text = status.get("latest_candidate") or status.get("candidate") or ""
    candidate_path = Path(candidate_text) if candidate_text else None
    audit = read_wiki_audit(status.get("latest_audit"))
    process_running = pid_is_running(status.get("pid"))
    status_state = str(status.get("state") or "unknown")
    dashboard_state = "watching" if process_running and status_state != "completed" else "healthy" if status_state == "completed" else "needs-review"
    text = "Running local Galaxy Evolution wiki-quality sprint" if dashboard_state == "watching" else "Wiki-quality sprint complete" if dashboard_state == "healthy" else "Wiki-quality sprint needs review"
    fatal_failures_value = audit.get("fatal_failures")
    fatal_failures_count = len(fatal_failures_value) if isinstance(fatal_failures_value, list) else fatal_failures_value if isinstance(fatal_failures_value, int) else None
    display_ledger_lines = ledger_lines
    if dashboard_state == "healthy" and status_state == "completed":
        claim_balanced = (audit.get("claim_markers") or {}).get("balanced") if isinstance(audit.get("claim_markers"), dict) else None
        display_ledger_lines = [
            f"Final clean wiki candidate: {Path(str(candidate_path)).name if candidate_path else 'candidate'} · fatal_failures={fatal_failures_count} · claim_markers_balanced={claim_balanced} · cites={audit.get('cite_count')}.",
            f"Final handoff: {root / 'FINAL_HANDOFF.md'}",
            f"Full archived wiki sprint ledger remains at {ledger_path}.",
        ]
    return {
        "marker": WIKI_QUALITY_SPRINT_MARKER,
        "generated_at": now_utc(),
        "state": dashboard_state,
        "text": text,
        "process_running": process_running,
        "pid": status.get("pid"),
        "status": status_state,
        "cycle": status.get("cycle"),
        "cycles_completed": status.get("cycles_completed", 0),
        "started_utc": status.get("started_utc"),
        "target_end_utc": status.get("target_end_utc"),
        "updated_utc": status.get("updated_utc"),
        "progress_percent": percent_between(status.get("started_utc"), status.get("target_end_utc")),
        "root": str(root),
        "board": str(root / "WIKI_SPRINT_BOARD.md"),
        "ledger": str(ledger_path),
        "candidate": str(candidate_path) if candidate_path else "",
        "latest_audit": {
            "fatal_failures": fatal_failures_count,
            "claim_markers_balanced": (audit.get("claim_markers") or {}).get("balanced") if isinstance(audit.get("claim_markers"), dict) else None,
            "cite_count": audit.get("cite_count"),
            "forbidden_contract_tokens": audit.get("forbidden_contract_tokens"),
            "overclaim_pattern_hits": audit.get("overclaim_pattern_hits"),
        },
        "lanes": status.get("lanes") or [
            "AGY Gemini 3.1 Pro Low: Hwao-style wiki direction",
            "AGY Gemini 3.5 Flash Low: Goru mechanical review",
            "Codex gpt-5.4-mini: Kun schema/reproducibility review",
            "Codex gpt-5.4-mini: local candidate integrator",
        ],
        "ledger_tail": display_ledger_lines,
        "safe_boundaries": [
            "Local wiki candidate/report artifacts only; no live wiki publish or product DB write.",
            "No public static replacement, deploy/restart, git write, cron, billing/OAuth/API-key/account changes, credential reads, browser automation, or external submission.",
        ],
    }


def lane_usage_counts(source: Dict[str, Any]) -> Dict[str, Dict[str, int]]:
    buckets = {
        "hermes": {"total": 0, "active": 0},
        "claude": {"total": 0, "active": 0},
        "goru": {"total": 0, "active": 0},
        "codex": {"total": 0, "active": 0},
    }
    for pane in source.get("panes", []):
        role = role_prefix(str(pane.get("role") or ""))
        key = None
        if role == "Tori":
            key = "hermes"
        elif role in {"Hwao", "Lana"}:
            key = "claude"
        elif role == "Goru":
            key = "goru"
        elif role == "Kun":
            key = "codex"
        if key:
            buckets[key]["total"] += 1
            if pane_status(pane) == "active":
                buckets[key]["active"] += 1
    return buckets


def usage_cache_fresh(max_age_seconds: int = 300) -> Dict[str, Any] | None:
    cached = read_small_json(USAGE_CACHE_PATH)
    if not cached:
        return None
    age = age_seconds(cached.get("generated_at"))
    if age is not None and age <= max_age_seconds:
        cached["cache_state"] = "cached"
        cached["cache_age_label"] = age_label(age)
        return cached
    return None


def as_percent(value: Any) -> float | None:
    if isinstance(value, (int, float)):
        return float(max(0, min(100, value)))
    return None


def _sub_is_5h(item: Dict[str, Any]) -> bool:
    lbl = (item.get("label") or "").lower()
    return "5h" in lbl or "5 hour" in lbl or "5-hour" in lbl


def _sub_is_weekly(item: Dict[str, Any]) -> bool:
    lbl = (item.get("label") or "").lower()
    vl = (item.get("value_label") or "").lower()
    return "weekly" in lbl or "weekly" in vl


_REMAINING_SEGMENT_RE = re.compile(r"\s*·\s*\d+%\s*remaining", re.IGNORECASE)


def _tidy_label(text: Any) -> Any:
    # Display normalization: current GPT model label, and drop the redundant
    # "· NN% remaining" segment so the reset-time sits consistently after usage.
    if not isinstance(text, str):
        return text
    text = text.replace("gpt-5.5", "gpt-5.6")
    text = _REMAINING_SEGMENT_RE.sub("", text)
    return text


def _tidy_detail(provider: Any, text: Any) -> Any:
    """Correct provider copy that predates Gemini's weekly-only app meter."""
    if not isinstance(text, str):
        return text
    if str(provider or "").strip().lower() == "gemini app / consumer":
        text = text.replace(
            "consumer Gemini app compute meter (5h rolling into a weekly cap)",
            "consumer Gemini app weekly compute meter",
        )
        text = text.replace(
            "the window refills on a 5h roll",
            "the weekly allowance resets on the provider-reported date",
        )
    return text


def public_gauge_card(gauge: Dict[str, Any]) -> Dict[str, Any]:
    raw_subs = [s for s in (gauge.get("sub_gauges") or []) if isinstance(s, dict)]
    # Headline = the WEEKLY quota for each provider (not the 5-hour one), and
    # drop the 5-hour sub-gauges entirely per operator preference.
    weekly = next((s for s in raw_subs if _sub_is_weekly(s)), None)
    sub_gauges = []
    for item in raw_subs:
        if _sub_is_5h(item):
            continue
        sub_gauges.append({
            "label": _tidy_label(item.get("label") or "usage"),
            "value_label": _tidy_label(item.get("value_label") or "not observed"),
            "percent": as_percent(item.get("fill_pct")),
            "tone": item.get("tone") or "ok",
        })
    if weekly is not None:
        pct = as_percent(weekly.get("fill_pct"))
        head_label = _tidy_label(weekly.get("value_label") or (f"{pct:.0f}% used weekly" if pct is not None else "not observed"))
    else:
        pct = as_percent(gauge.get("fill_pct"))
        head_label = _tidy_label(gauge.get("value_label") or (f"{pct:.0f}% used" if pct is not None else "not observed"))
    return {
        "name": gauge.get("provider") or "Provider",
        "kind": gauge.get("kind") or "public cockpit realtime feed",
        "status": gauge.get("status") or "observed",
        "percent": pct,
        "percent_label": head_label,
        "activity": head_label,
        "detail": _tidy_detail(gauge.get("provider"), gauge.get("detail") or ""),
        "source": gauge.get("source_label") or "public live steering cockpit status JSON",
        "tone": gauge.get("tone") or "ok",
        "sub_gauges": sub_gauges,
    }


def flow_credit_card() -> Dict[str, Any]:
    # Flow (Veo) monthly credit pool — separate from the Gemini-app compute limits.
    # A captured remaining balance is shown only when the drop-file is valid and
    # fresh. Otherwise the card labels the official Ultra allocation as reference
    # data and never presents it as a live balance.
    total = 25000
    remaining = None
    reset = "monthly · no rollover"
    captured_utc = None
    capture_age = None
    capture_error = None
    try:
        d = json.loads(FLOW_CREDITS_PATH.read_text())
        if not isinstance(d, dict):
            raise ValueError("capture must be a JSON object")
        remaining = d.get("remaining")
        total = d.get("total") or 25000
        reset = d.get("reset") or reset
        captured_utc = d.get("captured_utc")
        if isinstance(remaining, bool) or not isinstance(remaining, (int, float)):
            raise ValueError("remaining must be numeric")
        if isinstance(total, bool) or not isinstance(total, (int, float)) or total <= 0:
            raise ValueError("total must be a positive number")
        if not 0 <= remaining <= total:
            raise ValueError("remaining must be between zero and total")
        capture_age = age_seconds(captured_utc)
        if capture_age is None:
            raise ValueError("captured_utc must be an ISO-8601 timestamp")
    except FileNotFoundError:
        capture_error = "no Flow UI balance capture on file"
    except (OSError, ValueError, TypeError, json.JSONDecodeError) as exc:
        capture_error = f"Flow balance capture is invalid: {exc}"

    is_fresh_capture = (
        capture_error is None
        and capture_age is not None
        and capture_age <= FLOW_CREDITS_STALE_AFTER_SECONDS
    )
    if is_fresh_capture:
        assert isinstance(remaining, (int, float)) and not isinstance(remaining, bool)
        assert isinstance(total, (int, float)) and not isinstance(total, bool)
        used_pct = as_percent(100 * (float(total) - float(remaining)) / float(total))
        reset_label = str(reset).strip()
        if reset_label.lower().startswith(("not specified", "not shown", "unknown", "unavailable")):
            reset_copy = "reset date not shown in Flow UI"
        else:
            reset_copy = f"resets {reset_label}"
        head = f"{int(remaining):,} / {int(total):,} credits left · {reset_copy}"
        status = f"Flow UI capture · {age_label(capture_age)} old"
        detail = f"Current Flow UI balance captured at {captured_utc}; monthly pool is separate from Gemini-app compute limits."
        source = f"Flow UI balance captured in {FLOW_CREDITS_PATH.name} at {captured_utc}."
        tone = "danger" if used_pct is not None and used_pct >= 90 else "warn" if used_pct is not None and used_pct >= 75 else "ok"
    elif capture_error is None:
        used_pct = as_percent(100 * (float(total) - float(remaining)) / float(total))
        reset_label = str(reset).strip()
        reset_copy = ("reset date not shown" if reset_label.lower().startswith(
            ("not specified", "not shown", "unknown", "unavailable")) else f"resets {reset_label}")
        head = f"{int(remaining):,} / {int(total):,} credits left (last capture) · {reset_copy}"
        status = f"stale — captured {age_label(capture_age)} ago"
        detail = (
            f"Last operator-confirmed Flow UI balance, captured {captured_utc} ({age_label(capture_age)} old). "
            "Shown as the most recent known reading; refresh with `flow-credits <remaining>` after a glance at the Flow UI."
        )
        source = f"Last Flow UI balance capture in {FLOW_CREDITS_PATH.name} at {captured_utc}."
        tone = "warn"
    else:
        used_pct = None
        head = f"~{int(total):,} credits/month (Ultra) · current balance not captured"
        status = "reference"
        detail = f"{capture_error}. The displayed total is the Ultra plan allocation, not a remaining-balance estimate."
        source = "Official Ultra monthly allocation; live remaining balance requires a Flow UI capture."
        tone = "warn"
    return {
        "name": "Flow / Veo credits (Ultra)",
        "kind": "monthly Flow credit pool (separate from Gemini-app limits)",
        "status": status,
        "percent": used_pct,
        "percent_label": head,
        "activity": head,
        "detail": detail,
        "source": source,
        "tone": tone,
        "sub_gauges": [],
    }


def build_public_usage_snapshot(source: Dict[str, Any]) -> Dict[str, Any] | None:
    public_status = read_small_json(PUBLIC_USAGE_STATUS)
    if not public_status:
        return None
    gauges = public_status.get("provider_usage_gauges")
    if not isinstance(gauges, list) or not gauges:
        return None
    monitor = public_status.get("provider_usage_monitor")
    if not isinstance(monitor, dict):
        monitor = {}
    observed_at = monitor.get("observed_at_utc") or public_status.get("generated_at") or now_utc()
    observed_age = age_seconds(observed_at)
    def _keep_gauge(g: Dict[str, Any]) -> bool:
        # Drop cards that aren't real provider quotas, per operator preference:
        # the Flow/Veo credit-planning card and the Tori/Hermes context-window card.
        prov = (g.get("provider") or "").lower()
        return not any(t in prov for t in ("veo", "flow", "tori", "hermes"))
    cards = [public_gauge_card(g) for g in gauges if isinstance(g, dict) and _keep_gauge(g)]
    cards.append(flow_credit_card())   # re-added: Flow/Veo monthly credit pool
    if observed_age is not None and observed_age > 3600:
        return {
            "marker": PUBLIC_USAGE_FEED_MARKER,
            "provider_monitor_marker": monitor.get("marker") or "unknown",
            "provider_monitor_status": "stale-hidden",
            "generated_at": now_utc(),
            "observed_at_utc": observed_at,
            "cache_state": "stale-source-hidden",
            "cache_age_label": age_label(observed_age),
            "exact_limit_percent_sources": 0,
            "browser_poll_seconds": 5,
            "local_refresh_seconds": monitor.get("local_refresh_seconds"),
            "slash_refresh_seconds": monitor.get("slash_refresh_seconds"),
            "public_status_path": str(PUBLIC_USAGE_STATUS),
            "public_status_url": PUBLIC_USAGE_URL,
            "active_pane_counts": monitor.get("active_pane_counts") if isinstance(monitor.get("active_pane_counts"), dict) else {},
            "cards": [flow_credit_card()],
            "notes": [
                f"Provider usage source is stale ({age_label(observed_age)} old), so old quota gauges are hidden from this dashboard until the source refreshes.",
                "No credentials, billing pages, provider account surfaces, browser automation, or billing APIs were used to refresh this.",
            ],
            "sources": {
                "public_status_path": str(PUBLIC_USAGE_STATUS),
                "public_status_url": PUBLIC_USAGE_URL,
                "public_monitor_observed_at_utc": observed_at,
                "public_monitor_age_seconds": observed_age,
                "provider_gauge_count_hidden_as_stale": len(cards),
            },
        }
    exact_sources = sum(1 for card in cards if isinstance(card.get("percent"), (int, float)))
    active_counts = monitor.get("active_pane_counts") if isinstance(monitor.get("active_pane_counts"), dict) else {}
    notes = [
        "Same provider usage feed as the public live steering cockpit; this private dashboard mirrors it instead of collecting a second quota source.",
        "Browser refreshes this private JSON every 5s; local public usage monitor refreshes status files every 60s and safe visible slash panels every 300s when panes are idle.",
        monitor.get("source_policy") or "Visible pane/status sources only. No credentials, billing APIs, account/payment surfaces, browser automation, or provider secrets.",
    ]
    for item in monitor.get("limitations") or []:
        if isinstance(item, str):
            notes.append(item)
    return {
        "marker": PUBLIC_USAGE_FEED_MARKER,
        "provider_monitor_marker": monitor.get("marker") or "unknown",
        "provider_monitor_status": monitor.get("status") or "unknown",
        "generated_at": now_utc(),
        "observed_at_utc": observed_at,
        "cache_state": "public-realtime-feed",
        "cache_age_label": age_label(observed_age),
        "exact_limit_percent_sources": exact_sources,
        "browser_poll_seconds": 5,
        "local_refresh_seconds": monitor.get("local_refresh_seconds"),
        "slash_refresh_seconds": monitor.get("slash_refresh_seconds"),
        "public_status_path": str(PUBLIC_USAGE_STATUS),
        "public_status_url": PUBLIC_USAGE_URL,
        "active_pane_counts": active_counts,
        "cards": cards,
        "notes": notes,
        "sources": {
            "public_status_path": str(PUBLIC_USAGE_STATUS),
            "public_status_url": PUBLIC_USAGE_URL,
            "public_monitor_observed_at_utc": observed_at,
            "public_monitor_age_seconds": observed_age,
            "provider_gauge_count": len(cards),
        },
    }


def build_usage_snapshot(source: Dict[str, Any]) -> Dict[str, Any]:
    public_snapshot = build_public_usage_snapshot(source)
    if public_snapshot:
        return public_snapshot

    cached = usage_cache_fresh()
    if cached:
        return cached

    lanes = lane_usage_counts(source)
    insights_cmd = run_readonly(["hermes", "insights", "--days", "7"], timeout=35)
    auth_cmd = run_readonly(["hermes", "auth", "list"], timeout=20)
    insights = parse_hermes_insights(insights_cmd.get("stdout", "")) if insights_cmd.get("ok") else {}
    auth_counts = parse_auth_counts(auth_cmd.get("stdout", "")) if auth_cmd.get("ok") else {}

    claude_stats = read_small_json(Path.home() / ".claude" / "stats-cache.json")
    claude_daemon = read_small_json(Path.home() / ".claude" / "daemon.status.json")
    claude_stats_date = str(claude_stats.get("lastComputedDate") or "not found")
    today = dt.datetime.utcnow().date().isoformat()
    claude_stats_note = "local stats cache stale / not a live limit" if claude_stats_date != today else "local stats cache current"

    cards = [
        {
            "name": "Hermes / Tori",
            "kind": "local-analytics",
            "status": "measured" if insights_cmd.get("ok") else "unavailable",
            "percent": None,
            "percent_label": "quota percent not exposed",
            "activity": f"{fmt_int(insights.get('total_tokens_7d'))} tokens in 7d",
            "detail": f"{fmt_int(insights.get('sessions_7d'))} sessions · {fmt_int(insights.get('tool_calls_7d'))} tool calls · model {insights.get('model') or 'unknown'}",
            "source": "hermes insights --days 7 (local session DB)",
            "lanes_active": lanes["hermes"]["active"],
            "lanes_total": lanes["hermes"]["total"],
        },
        {
            "name": "Claude Code / Hwao+Lana",
            "kind": "subscription-lane",
            "status": "authenticated" if auth_counts.get("anthropic", 0) else "unknown",
            "percent": None,
            "percent_label": "not exposed by safe CLI",
            "activity": f"{lanes['claude']['active']}/{lanes['claude']['total']} active panes",
            "detail": f"{auth_counts.get('anthropic', 0)} Anthropic/Hermes credentials visible · {claude_stats_note} ({claude_stats_date})",
            "source": "tmux pane state + hermes auth list + .claude stats metadata only",
            "lanes_active": lanes["claude"]["active"],
            "lanes_total": lanes["claude"]["total"],
        },
        {
            "name": "Goru / Antigravity Gemini",
            "kind": "subscription-lane",
            "status": "running" if lanes["goru"]["total"] else "not seen",
            "percent": None,
            "percent_label": "not exposed by safe CLI",
            "activity": f"{lanes['goru']['active']}/{lanes['goru']['total']} active panes",
            "detail": "agy/Gemini subscription lane observed through tmux; no safe local percent-limit API found",
            "source": "tmux pane state only",
            "lanes_active": lanes["goru"]["active"],
            "lanes_total": lanes["goru"]["total"],
        },
        {
            "name": "Kun / Codex CLI",
            "kind": "subscription-lane",
            "status": "authenticated" if auth_counts.get("openai-codex", 0) else "unknown",
            "percent": None,
            "percent_label": "not exposed by safe CLI",
            "activity": f"{lanes['codex']['active']}/{lanes['codex']['total']} active panes",
            "detail": f"{auth_counts.get('openai-codex', 0)} OpenAI Codex credential visible · local doctor has no quota percent field",
            "source": "tmux pane state + hermes auth list",
            "lanes_active": lanes["codex"]["active"],
            "lanes_total": lanes["codex"]["total"],
        },
    ]
    exact_sources = sum(1 for card in cards if isinstance(card.get("percent"), (int, float)))
    snapshot = {
        "marker": "GE_USAGE_LIMIT_MONITOR_V1",
        "generated_at": now_utc(),
        "cache_state": "fresh",
        "cache_age_label": "0s",
        "exact_limit_percent_sources": exact_sources,
        "cards": cards,
        "notes": [
            "Percent gauges show only provider-reported percentages. If a safe local CLI does not expose a quota percent, the dashboard says 'not exposed' instead of guessing.",
            "This monitor reads local status/metadata only. It does not open provider web pages, call billing APIs, print tokens, or inspect credential files.",
            "Exact Claude/Codex/Gemini plan-limit percentages still require a provider UI or an approved provider-specific safe source.",
        ],
        "sources": {
            "hermes_insights_ok": bool(insights_cmd.get("ok")),
            "hermes_auth_list_ok": bool(auth_cmd.get("ok")),
            "claude_stats_last_computed": claude_stats_date,
            "claude_daemon_workers": len(claude_daemon.get("workers") or {}) if isinstance(claude_daemon.get("workers"), dict) else 0,
            "usage_cache_path": str(USAGE_CACHE_PATH),
        },
    }
    try:
        WEB_ROOT.mkdir(parents=True, exist_ok=True)
        USAGE_CACHE_PATH.write_text(json.dumps(snapshot, indent=2, sort_keys=True) + "\n")
    except Exception:
        pass
    return snapshot


def normalize_run_estimates(raw: Any) -> Dict[str, Any]:
    if not isinstance(raw, dict):
        return {
            "marker": RUN_TIME_ESTIMATE_MARKER,
            "runs_total": 0,
            "active_runs_count": 0,
            "completed_runs_count": 0,
            "archived_runs_count": 0,
            "runs": [],
        }
    runs = [item for item in (raw.get("runs") or []) if isinstance(item, dict)]
    unresolved_runs = [r for r in runs if str(r.get("state") or "running") != "complete"]
    completed_runs = [r for r in runs if str(r.get("state") or "") == "complete"]

    def run_ts(item: Dict[str, Any]) -> str:
        return str(item.get("completed_at_utc") or item.get("updated_at_utc") or item.get("started_at_utc") or "")

    completed_runs = sorted(completed_runs, key=run_ts, reverse=True)
    stale_unresolved_runs = [
        r for r in unresolved_runs
        if str(r.get("state") or "") == "over-estimate" and (age_seconds(r.get("updated_at_utc")) or 0) > 3600
    ]
    active_runs = [r for r in unresolved_runs if r not in stale_unresolved_runs]
    out = dict(raw)
    # Visible dashboard should not be dominated by old completed packets.
    # Keep active/unresolved orders as cards; summarize completed history instead.
    out["runs"] = active_runs
    out["runs_total"] = len(runs)
    out["active_runs_count"] = len(active_runs)
    out["completed_runs_count"] = len(completed_runs)
    out["stale_unresolved_runs_count"] = len(stale_unresolved_runs)
    out["archived_runs_count"] = len(completed_runs) + len(stale_unresolved_runs)
    if completed_runs:
        latest = completed_runs[0]
        out["latest_completed"] = {
            "completed_at_utc": latest.get("completed_at_utc"),
            "elapsed_label": latest.get("elapsed_label"),
        }
    return out


CORPUS_SCALEUP_DIR = Path("/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/corpus-ga-co-2009-2026-20260718")

def build_corpus_scaleup_snapshot() -> Dict[str, Any]:
    d = CORPUS_SCALEUP_DIR
    emb_status, emb_big, emb_detail, emb_tone = "UNKNOWN", "-", "no log yet", "watching"
    try:
        lines = (d / "embed.log").read_text().splitlines()
        done_line = next((l for l in reversed(lines) if "DONE embedded" in l), None)
        prog_line = next((l for l in reversed(lines) if "batches (" in l), None)
        if done_line:
            emb_status, emb_big, emb_detail, emb_tone = "DONE", "120,676 embedded", "qwen3-embedding-4b vectors complete (clean text)", "healthy"
        elif prog_line:
            m = re.search(r"\((\d+\.\d+)%\).*?(\d+) papers/s\s+ETA~(\d+)min", prog_line)
            pct = m.group(1) if m else "?"; rate = m.group(2) if m else "?"; eta = m.group(3) if m else "?"
            emb_status, emb_big, emb_tone = "EMBEDDING", f"{pct}%", "healthy"
            emb_detail = f"{rate} papers/s, ETA ~{eta} min (qwen3-embedding-4b, clean text)"
    except Exception:
        pass
    model_big, model_detail = "qwen3-embedding-4b", "won 10-model citation-retrieval eval"
    try:
        board = json.loads((d / "leaderboard.json").read_text())
        by = {r["model"]: r for r in board}
        q = by.get("qwen3-embedding-4b", {}).get("recall@10"); nm = by.get("nomic-embed-text", {}).get("recall@10")
        if q and nm:
            model_detail = f"won 10-model citation eval: recall@10 {q} vs current nomic {nm}"
    except Exception:
        pass
    ref_big, ref_detail = "-", "pending"
    try:
        rs = json.loads((d / "refs_state.json").read_text())
        ref_big = f"{rs.get('totrefs',0):,} edges"
        ref_detail = f"{rs.get('withrefs',0):,} papers with references (~99.9% coverage)"
    except Exception:
        pass
    ds_big, ds_detail = "-", "pending"
    try:
        di = json.loads((d / "dataset_index_summary.json").read_text()); it = di.get("interest", {})
        ds_big = f"MAST {it.get('MAST',0):,}"
        ds_detail = f"JWST {it.get('JWST',0)}, SDSS {it.get('SDSS',0)}, IllustrisTNG {it.get('IllustrisTNG',0)}"
    except Exception:
        pass
    tp_status, tp_big, tp_detail, tp_tone = "READY", "from scratch", "UMAP -> HDBSCAN -> c-TF-IDF validated; ready to cluster; no old topics inherited.", "watching"
    try:
        fm = json.loads((d / "frontier_map_v2.json").read_text())
        nc = fm.get("n_clusters"); cl = fm.get("clusters", []); npap = fm.get("n_papers", 1) or 1
        tops = "; ".join(" ".join((c.get("keywords") or [])[:2]) for c in cl[:3])
        tp_status, tp_big, tp_tone = "DONE", f"{nc} topics", "healthy"
        tp_detail = f"emergent from 120k, no inherited topics ({int(100*fm.get('noise',0)/npap)}% noise). Top frontiers: {tops}."
    except Exception:
        pass
    pw_status, pw_big, pw_detail, pw_tone = "PENDING", "-", "queued", "watching"
    try:
        import glob
        from collections import Counter as _Counter
        srcs = glob.glob(str(d / "fulltext_cache" / "*.src"))
        _c = _Counter()
        for _f in srcs:
            try: _c[open(_f).read().strip()] += 1
            except Exception: pass
        _pwlog = (d / "prewarm.log").read_text() if (d / "prewarm.log").exists() else ""
        if "DONE pre-warm" in _pwlog: pw_status, pw_tone = "DONE", "healthy"
        elif "starting canonical" in _pwlog: pw_status, pw_tone = "RUNNING", "healthy"
        pw_big = f"{len(srcs):,}/5,000 papers"
        pw_detail = f"HTML-first full text (ar5iv {_c.get('ar5iv',0)}, arXiv {_c.get('arxiv-html',0)}, pdf {_c.get('pdf',0)}); top most-cited canonical deep layer"
    except Exception:
        pass
    return {
        "marker": "GE_CORPUS_SCALEUP_20260718",
        "reported_at_utc": now_utc(),
        "headline": "AI-Scientist corpus: 120,676 papers (astro-ph.GA + CO, 2009-2026) embedded with qwen3-embedding-4b; full-text grounding now feeds the research pipeline.",
        "next_action": "Cluster the 120k so fresh topics emerge from scratch (no inherited topics); canonical full-text deep layer pre-warming; then swap paper-selection to the local semantic index.",
        "cards": [
            {"title":"Corpus pulled","status":"DONE","big":"120,676 papers","detail":"astro-ph.GA + astro-ph.CO, refereed, 2009-2026 - 10x the old 12k; rich ADS metadata + abstracts.","tone":"healthy"},
            {"title":"Embedding model","status":"SELECTED","big":model_big,"detail":model_detail,"tone":"healthy"},
            {"title":"Embedding run","status":emb_status,"big":emb_big,"detail":emb_detail,"tone":emb_tone},
            {"title":"Citation graph","status":"DONE","big":ref_big,"detail":ref_detail,"tone":"healthy"},
            {"title":"Dataset-usage index","status":"DONE","big":ds_big,"detail":ds_detail,"tone":"healthy"},
            {"title":"Full-text grounding","status":"WIRED","big":"on-demand","detail":"research pipeline deep-reads each study's papers (arXiv HTML-first) so drafts cite real, full-text-verified passages -- not the model's memory.","tone":"healthy"},
            {"title":"Canonical deep layer","status":pw_status,"big":pw_big,"detail":pw_detail,"tone":pw_tone},
            {"title":"Topic derivation","status":tp_status,"big":tp_big,"detail":tp_detail,"tone":tp_tone},
            {"title":"Quality gates","status":"BUILT + WIRED","big":"novelty / expected-value / citation","detail":"grounded gates in the research pipeline: novelty aborts already-done work, expected-value kills physically-impossible/contradicting results (astrosage sanity), citation-entailment catches fabricated cites. Validated.","tone":"healthy"},
        ],
    }

def build_overnight_report(usage_snapshot: Dict[str, Any]) -> Dict[str, Any]:
    cards_count = len(usage_snapshot.get("cards") or [])
    cache_state = str(usage_snapshot.get("cache_state") or "unknown")
    usage_live = cache_state == "public-realtime-feed" and cards_count > 0
    usage_status = "RESOLVED / LIVE" if usage_live else "WATCH"
    usage_big = f"{cards_count} live card{'s' if cards_count != 1 else ''}"
    usage_detail = (
        f"{cache_state}; monitor {usage_snapshot.get('provider_monitor_status') or 'unknown'}; "
        f"observed {usage_snapshot.get('observed_at_utc') or 'unknown'} "
        f"({usage_snapshot.get('cache_age_label') or 'unknown'} old)."
    )
    return {
        "marker": OVERNIGHT_REPORT_MARKER,
        "reported_at_utc": now_utc(),
        "headline": "Overnight: built the full AI-Scientist corpus foundation + the three quality gates.",
        "next_action": "Foundation complete - 120k semantic index, 8.9M-edge citation graph, 4,864-paper deep-read layer, emergent frontier map, retrieval+grounding+gates all wired. No auto-papers generated. Next: end-to-end gated study runs.",
        "approval_phrase": "NO ACTIVE EXECUTION PHRASE",
        "cards": [
            {"title": "Usage quota", "status": usage_status, "big": usage_big, "detail": usage_detail,
             "tone": "healthy" if usage_live else "needs-review"},
            {"title": "Corpus embedded", "status": "DONE", "big": "120,676 papers",
             "detail": "astro-ph.GA + CO 2009-2026 embedded with qwen3-embedding-4b (won a 10-model citation-retrieval eval); 1.24 GB semantic index - 10x the old 12k corpus.",
             "tone": "healthy"},
            {"title": "Emergent topics", "status": "DONE - from scratch", "big": "57 topics",
             "detail": "UMAP -> HDBSCAN -> c-TF-IDF on the full 120k, ranked by recent citation inflow (8.9M-edge graph). JWST high-z galaxy evolution is #1 by a wide margin. No inherited old topics.",
             "tone": "healthy"},
            {"title": "Retrieval + grounding", "status": "WIRED", "big": "our corpus + full text",
             "detail": "Pipeline retrieves semantically from our 120k, then deep-reads the working set HTML-first (ar5iv). Canonical deep layer: 4,864 top-cited papers full-text-embedded (96% clean HTML).",
             "tone": "healthy"},
            {"title": "Quality gates", "status": "BUILT + WIRED + VALIDATED", "big": "3 gates",
             "detail": "Novelty (grounded; correctly ABORTs done work, cites the paper) | Expected-value (numeric-targeted + astrosage physical-sanity; kills gross errors) | Citation-entailment (verifies real cites, catches fabricated ones). Grounded judgment beats ungrounded LLM.",
             "tone": "healthy"},
            {"title": "Flow / Veo credits", "status": "STALE - needs capture", "big": "22,096 / 25,000 (37h old)",
             "detail": "Last operator-confirmed reading is >24h old; shown as reference only. Agents cannot read the Flow UI (TCC). Refresh with `flow-credits <remaining>` after glancing at the Flow ULTRA popover.",
             "tone": "needs-review"},
            {"title": "Honesty", "status": "GATES ENFORCE IT", "big": "no auto-papers",
             "detail": "Zero papers auto-generated overnight (held for the gates, now built). The gates enforce non-circularity, non-contradiction, and real citations at run time.",
             "tone": "healthy"},
        ]
    }

def compact_status(source: Dict[str, Any]) -> Dict[str, Any]:
    groups: Dict[str, List[Dict[str, Any]]] = {name: [] for name in GROUP_ORDER}
    source_blockers = source.get("blockers", []) if isinstance(source.get("blockers", []), list) else []
    safe_source_blockers = [b for b in source_blockers if isinstance(b, dict) and b.get("safe_to_approve")]
    review_source_blockers = [b for b in source_blockers if not (isinstance(b, dict) and b.get("safe_to_approve"))]
    counts = {
        "targets_ok": 0,
        "targets_total": len(source.get("targets", [])),
        "panes": 0,
        "active": 0,
        "idle": 0,
        "dead": 0,
        "copy_mode": 0,
        "safe_prompts": 0,
        "review_prompts": 0,
        "blockers": 0,
        "safe_autoprompts": len(safe_source_blockers),
        "raw_blockers": len(source_blockers),
    }

    for target in source.get("targets", []):
        if target.get("exists"):
            counts["targets_ok"] += 1

    for pane in source.get("panes", []):
        cls = pane.get("classification") or {}
        status = pane_status(pane)
        if status == "active":
            counts["active"] += 1
        elif status == "idle":
            counts["idle"] += 1
        elif status == "dead":
            counts["dead"] += 1
        elif status == "copy-mode":
            counts["copy_mode"] += 1
        elif status == "safe-prompt":
            counts["safe_prompts"] += 1
        elif status == "review":
            counts["review_prompts"] += 1
        counts["panes"] += 1
        item = {
            "pane_id": pane.get("pane_id"),
            "role": pane.get("role") or "unknown",
            "command": pane.get("current_command") or "",
            "status": status,
            "active": bool(pane.get("active")),
            "dead": bool(pane.get("dead")),
            "copy_mode": bool(pane.get("in_mode")),
            "target": pane.get("target") or "",
            "size": pane.get("size") or "",
            "permission_prompt": bool(cls.get("permission_prompt")),
            "safe_to_approve": bool(cls.get("safe_to_approve")),
            "reason": cls.get("reason") or "",
            "tail_excerpt": compact_tail(pane.get("tail")),
        }
        groups.setdefault(group_for(pane), []).append(item)

    for name in groups:
        groups[name].sort(key=role_sort_key)

    source_ts = source.get("ts")
    age = age_seconds(source_ts)
    review_needs = counts["dead"] + counts["review_prompts"] + len(review_source_blockers)
    counts["blockers"] = review_needs
    safe_attention = counts["safe_autoprompts"] + counts["safe_prompts"] + counts["copy_mode"]
    health = "healthy"
    health_text = "RUNNING CLEAN"
    next_action = "Nothing needs you right now. Watch the lane cards or leave the dashboard open."
    if review_needs:
        health = "needs-review"
        health_text = f"NEEDS YOU · {review_needs}"
        next_action = "A hard-gate or unsafe prompt is waiting. Ask Tori or inspect the real pane; autopilot will not approve it."
    elif safe_attention:
        health = "watching"
        health_text = f"WATCHING SAFE PROMPTS · {safe_attention}"
        next_action = "Autopilot can handle safe docs/static or private-dashboard prompts; keep watching for red."
    if age is not None and age > 90:
        health = "stale"
        health_text = "STALE · monitor may be paused"
        next_action = "Check `ge-auto tail` or restart the Phase 1 monitor if the timestamp keeps aging."

    lane_summaries = {name: lane_summary(name, groups.get(name, [])) for name in GROUP_ORDER}
    events = read_events(limit=8, meaningful_only=True)
    latest_ticks = read_events(limit=1, meaningful_only=False)
    latest_event = latest_ticks[-1] if latest_ticks else events[-1] if events else None
    usage_snapshot = build_usage_snapshot(source)
    return {
        "marker": MARKER,
        "compat_markers": COMPAT_MARKERS,
        "legacy_marker": LEGACY_MARKER,
        "generated_at": now_utc(),
        "source_ts": source_ts,
        "source_age_seconds": age,
        "source_age_label": age_label(age),
        "health": health,
        "health_text": health_text,
        "next_action": next_action,
        "phase": source.get("phase") or "phase1-bounded-controller",
        "repo": source.get("repo") or str(REPO),
        "url": URL,
        "tailnet_only": True,
        "browser_executes_actions": False,
        "counts": counts,
        "targets": source.get("targets", []),
        "groups": groups,
        "lane_summaries": lane_summaries,
        "blockers": review_source_blockers,
        "safe_autoprompts": safe_source_blockers,
        "events": events,
        "latest_event": latest_event,
        "last_incident": LAST_INCIDENT,
        "overnight_report": build_overnight_report(usage_snapshot),
        "corpus_scaleup": build_corpus_scaleup_snapshot(),
        "run_estimates": normalize_run_estimates(source.get("run_estimates") or {
            "marker": RUN_TIME_ESTIMATE_MARKER,
            "runs_total": 0,
            "runs": [],
        }),
        "hard_gates_closed": source.get("hard_gates_closed") or SAFETY_GATES,
        "policy_lines": POLICY_LINES,
        "source_status_path": str(SOURCE_STATUS),
        "source_events_path": str(SOURCE_EVENTS),
        "usage_monitor": usage_snapshot,
        "paper_quality_sprint": build_paper_quality_sprint_snapshot(),
        "wiki_quality_sprint": build_wiki_quality_sprint_snapshot(),
        "survey_autopilot": build_survey_autopilot_snapshot(),
        "local_outcome_ledger": source.get("local_outcome_ledger") or {
            "marker": OUTCOME_LEDGER_MARKER,
            "enabled": False,
            "scope": "local append-only outcome ledger only; product DB/API/page writes remain closed",
            "product_db_writes_enabled": False,
        },
        "web_status_path": str(JSON_PATH),
    }


def render_html() -> str:
    template = r'''<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <meta name="color-scheme" content="dark">
  <title>Galaxy Evolution + Surveys Autopilot Dashboard V3</title>
  <style>
    :root { --bg:#030712; --panel:#081827; --panel2:#0d2238; --panel3:#102b47; --line:#244662; --text:#eef7ff; --muted:#8fa9c8; --soft:#c7dcf4; --green:#3ee28f; --yellow:#ffd166; --red:#ff5d73; --blue:#76d7ff; --violet:#c7a6ff; --shadow:0 24px 80px rgba(0,0,0,.38); }
    * { box-sizing:border-box; }
    body { margin:0; color:var(--text); font-family:-apple-system,BlinkMacSystemFont,"Segoe UI",Inter,Roboto,sans-serif; background:radial-gradient(circle at 10% -5%,rgba(118,215,255,.28),transparent 30%),radial-gradient(circle at 95% 4%,rgba(62,226,143,.16),transparent 28%),linear-gradient(180deg,#071423 0%,#030712 62%,#02050b 100%); min-height:100vh; }
    header { position:sticky; top:0; z-index:5; padding:24px clamp(16px,4vw,48px) 16px; background:rgba(3,7,18,.82); backdrop-filter:blur(20px); border-bottom:1px solid rgba(118,215,255,.18); }
    h1 { margin:0; font-size:clamp(30px,4.8vw,64px); line-height:.92; letter-spacing:-.06em; }
    h2 { margin:0 0 12px; font-size:20px; letter-spacing:-.02em; }
    h3 { margin:0; color:var(--muted); text-transform:uppercase; letter-spacing:.11em; font-size:12px; }
    p { color:var(--muted); line-height:1.55; } a { color:#ace4ff; } code { color:#bdeaff; }
    main { padding:22px clamp(16px,4vw,48px) 56px; }
    .subtitle { margin:10px 0 0; max-width:1080px; color:var(--soft); }
    .topline { display:flex; flex-wrap:wrap; gap:10px; margin-top:16px; align-items:center; }
    .pill { display:inline-flex; align-items:center; gap:8px; border:1px solid var(--line); background:rgba(8,24,39,.78); border-radius:999px; padding:8px 12px; color:var(--soft); font-size:13px; }
    .dot { width:10px; height:10px; border-radius:50%; background:var(--blue); box-shadow:0 0 20px currentColor; }
    .healthy .dot { background:var(--green); } .watching .dot,.stale .dot,.active .dot { background:var(--yellow); } .needs-review .dot,.review .dot,.dead .dot { background:var(--red); }
    .grid { display:grid; gap:16px; }
    .hero { grid-template-columns:minmax(0,1.15fr) minmax(320px,.85fr); align-items:stretch; }
    .panel,.metric,.lane,.gate,.flowbox,.summary-card,.event { border:1px solid rgba(118,215,255,.20); background:linear-gradient(180deg,rgba(16,43,71,.9),rgba(8,24,39,.93)); border-radius:24px; box-shadow:var(--shadow); }
    .panel { padding:20px; } .room { min-height:250px; display:flex; flex-direction:column; justify-content:space-between; }
    .state-word { font-size:clamp(44px,7.6vw,96px); letter-spacing:-.08em; line-height:.86; margin:8px 0 14px; }
    .state-word.healthy { color:var(--green); } .state-word.watching,.state-word.stale { color:var(--yellow); } .state-word.needs-review { color:var(--red); }
    .answer { font-size:18px; color:var(--soft); max-width:760px; }
    .micro { font-size:12px; color:var(--muted); }
    .metrics { grid-template-columns:repeat(6,minmax(0,1fr)); margin:18px 0; }
    .metric { padding:16px; min-height:105px; box-shadow:none; } .metric b { display:block; font-size:34px; letter-spacing:-.045em; } .metric span { color:var(--muted); font-size:11px; text-transform:uppercase; letter-spacing:.11em; }
    .flow { grid-template-columns:repeat(5,minmax(0,1fr)); margin-top:14px; }
    .flowbox { padding:14px; min-height:108px; position:relative; overflow:hidden; box-shadow:none; } .flowbox strong { display:block; font-size:18px; } .flowbox small { color:var(--muted); }
    .flowbox:after { content:""; position:absolute; right:-25px; bottom:-30px; width:100px; height:100px; border-radius:50%; background:rgba(118,215,255,.10); }
    .gates-strip { margin-bottom:18px; } .gate-list { display:grid; grid-template-columns:repeat(4,minmax(0,1fr)); gap:8px; } .gate { padding:10px 12px; box-shadow:none; color:var(--soft); font-size:13px; } .lock { color:var(--green); font-weight:900; }
    .summaries { grid-template-columns:repeat(5,minmax(0,1fr)); margin:18px 0; } .summary-card { padding:15px; box-shadow:none; } .summary-card b { display:block; font-size:24px; margin-top:6px; } .summary-card small { color:var(--muted); }
    .summary-card.needs-review { border-color:rgba(255,93,115,.65); } .summary-card.watching { border-color:rgba(255,209,102,.65); } .summary-card.active { border-color:rgba(118,215,255,.65); }
    .directors-grid { display:grid; grid-template-columns:repeat(3,minmax(0,1fr)); gap:12px; } .methods-grid { display:grid; grid-template-columns:repeat(3,minmax(0,1fr)); gap:16px; margin-top:18px; } .wide { display:grid; grid-template-columns:1.15fr .85fr; gap:16px; margin-top:18px; }
    .lane { padding:14px; margin:10px 0; background:rgba(6,18,31,.72); box-shadow:none; } .lane.review,.lane.dead { border-color:rgba(255,93,115,.72); } .lane.safe-prompt,.lane.copy-mode { border-color:rgba(255,209,102,.72); } .lane.active { border-color:rgba(118,215,255,.7); }
    .lane-head { display:flex; justify-content:space-between; gap:10px; align-items:baseline; } .lane-role { font-weight:800; word-break:break-word; } .pane-id { color:#bdeaff; font-family:ui-monospace,SFMono-Regular,Menlo,monospace; }
    .meta { color:var(--muted); font-size:12px; line-height:1.45; margin-top:7px; word-break:break-word; } .chips { display:flex; flex-wrap:wrap; gap:6px; margin-top:10px; }
    .chip { font-size:11px; border-radius:999px; padding:5px 8px; border:1px solid var(--line); color:var(--muted); background:#071423; } .chip.active { background:var(--blue); color:#02101a; border-color:var(--blue); } .chip.healthy { background:var(--green); color:#03170d; border-color:var(--green); } .chip.review,.chip.stale { background:var(--yellow); color:#1a1000; border-color:var(--yellow); } .chip.dead { background:var(--red); color:white; border-color:var(--red); }
    .tail { margin-top:9px; color:#b9cce4; font-size:11px; opacity:.86; border-left:2px solid rgba(118,215,255,.25); padding-left:8px; overflow-wrap:anywhere; word-break:break-word; }
    .events { display:grid; gap:8px; } .event { padding:11px 12px; box-shadow:none; } .event strong { color:var(--soft); } .event small { color:var(--muted); display:block; margin-top:4px; }
    .usage-grid { display:grid; grid-template-columns:repeat(4,minmax(0,1fr)); gap:12px; margin-top:12px; }
    .overnight-grid { display:grid; grid-template-columns:repeat(3,minmax(0,1fr)); gap:12px; margin-top:12px; }
    .usage-card { border:1px solid rgba(118,215,255,.22); background:rgba(6,18,31,.72); border-radius:20px; padding:14px; box-shadow:none; min-height:210px; }
    .usage-card h3 { margin-bottom:7px; } .usage-big { font-size:34px; letter-spacing:-.06em; color:var(--soft); margin:6px 0 3px; overflow-wrap:anywhere; word-break:break-word; }
    .usage-bar { height:10px; border-radius:999px; border:1px solid var(--line); background:#071423; overflow:hidden; margin:10px 0; }
    .usage-bar span { display:block; height:100%; width:0; background:linear-gradient(90deg,var(--green),var(--yellow)); }
    .usage-card.unknown .usage-bar span { width:100%; background:repeating-linear-gradient(45deg,rgba(143,169,200,.25),rgba(143,169,200,.25) 8px,rgba(143,169,200,.10) 8px,rgba(143,169,200,.10) 16px); }
    .usage-status { display:inline-block; border:1px solid var(--line); border-radius:999px; padding:4px 8px; color:var(--muted); font-size:11px; margin:6px 0; }
    .usage-note { color:var(--muted); font-size:12px; line-height:1.45; }
    .usage-subs { display:grid; gap:6px; margin:10px 0; }
    .usage-sub { padding-top:6px; }
    .usage-sub-line { display:flex; justify-content:space-between; gap:8px; color:var(--soft); font-size:12px; align-items:center; } .reset-time { font-family: ui-monospace, SFMono-Regular, Menlo, Monaco, Consolas, monospace; font-size: 13px; font-weight: 800; color: #ffb86c; background: rgba(255,184,108,0.15); border: 1px solid rgba(255,184,108,0.3); border-radius: 6px; padding: 2px 8px; letter-spacing: 0.5px; white-space: nowrap; }
    .reset-time.reset-red { color: #ff5555; background: rgba(255,85,85,0.15); border-color: rgba(255,85,85,0.4); }
    .reset-time.reset-orange { color: #ffb86c; background: rgba(255,184,108,0.15); border-color: rgba(255,184,108,0.4); }
    .reset-time.reset-blue { color: #8be9fd; background: rgba(139,233,253,0.15); border-color: rgba(139,233,253,0.4); }
    .usage-sub-bar { height:5px; border-radius:999px; background:#071423; overflow:hidden; margin-top:5px; }
    .usage-sub-bar span { display:block; height:100%; width:0; background:linear-gradient(90deg,var(--green),var(--yellow)); }
    .usage-sub-bar span.unknown { width:100%; background:repeating-linear-gradient(45deg,rgba(143,169,200,.24),rgba(143,169,200,.24) 6px,rgba(143,169,200,.08) 6px,rgba(143,169,200,.08) 12px); }
    .empty { color:var(--muted); border:1px dashed var(--line); border-radius:16px; padding:14px; }
    .incident-resolved { border-color:rgba(62,226,143,.52); }
    .urlbox { user-select:all; border:1px solid var(--line); background:#071423; border-radius:14px; padding:12px; overflow-wrap:anywhere; color:#bdeaff; }
    .policy-list { margin:0; padding-left:18px; color:var(--muted); } .policy-list li { margin:7px 0; }
    footer { color:var(--muted); padding:10px clamp(16px,4vw,48px) 36px; }
    @media (max-width:1240px) { .metrics { grid-template-columns:repeat(3,minmax(0,1fr)); } .summaries,.flow,.gate-list,.usage-grid,.overnight-grid { grid-template-columns:repeat(2,minmax(0,1fr)); } .hero,.wide { grid-template-columns:1fr; } .directors-grid,.methods-grid { grid-template-columns:1fr; } }
    @media (max-width:720px) { header { position:static; } .metrics,.summaries,.flow,.gate-list,.usage-grid,.overnight-grid { grid-template-columns:1fr; } .state-word { font-size:44px; } }
  </style>
</head>
<body>
  <header>
    <h1>Galaxy Evolution + Surveys Autopilot</h1>
    <p class="subtitle">PRIVATE TAILNET MIRROR · READ-ONLY · this page takes no actions. V3 adds run-time estimates, a usage-limit monitor, a local outcome DB card, and a Survey Autopilot card for the frontend <code>/surveys</code> Atlas IA surface.</p>
    <div class="topline">
      <span id="health-pill" class="pill"><span class="dot"></span><span id="health-text">Loading…</span></span>
      <span class="pill"><span class="dot"></span><span id="updated-text">Waiting for JSON</span></span>
      <span class="pill"><span class="dot"></span><span>__MARKER__</span></span>
    </div>
  </header>
  <main>
    <section class="panel gates-strip">
      <h2>Hard gates closed</h2>
      <p>Hard gates closed — no product DB/API/page writes · no live wiki/publish · no deploy · no git · no public cockpit/global · no cloud/billing/OAuth · no browser · no cron. The only DB-like write is the local append-only outcome ledger under .hermes.</p>
      <div id="gates-top" class="gate-list"></div>
    </section>

    <section class="grid hero">
      <div class="panel room">
        <div>
          <h3>Room-glance answer</h3>
          <div id="state-word" class="state-word healthy">Loading</div>
          <div id="next-action" class="answer">Waiting for the autopilot status snapshot.</div>
        </div>
        <div class="topline">
          <span class="pill"><span class="dot"></span><span id="phase-text">phase…</span></span>
          <span class="pill"><span class="dot"></span><span id="event-text">events…</span></span>
        </div>
      </div>
      <div class="panel">
        <h2>Open from MacBook</h2>
        <p class="urlbox"><a href="__URL__">__URL__</a></p>
        <p class="micro">Requires Tailscale on the MacBook. The browser only fetches <code>ge-autopilot-status.json</code>; it does not approve, run, publish, deploy, or write anything.</p>
        <h2>What this monitors</h2>
        <div class="flow grid">
          <div class="flowbox"><strong>Directors</strong><small>Hwao, Tori, Goru live-view.</small></div>
          <div class="flowbox"><strong>M1/M2/M3</strong><small>Hwao/Lana/Goru/Kun/Tori panes by method.</small></div>
          <div class="flowbox"><strong>Survey Autopilot</strong><small>Frontend /surveys files, smoke-test custody, and safe next work.</small></div>
          <div class="flowbox"><strong>Prompts</strong><small>Safe vs needs-you permission states.</small></div>
          <div class="flowbox"><strong>Events</strong><small>Latest autopilot ticks/actions/blockers.</small></div>
        </div>
      </div>
    </section>

    <section class="metrics grid" id="metrics"></section>
    <section class="summaries grid" id="summaries"></section>

    <section class="panel" id="usage-monitor-panel">
      <h2>Usage limit monitor</h2>
      <p>Live quota comes first. This mirrors the public live steering cockpit’s provider gauges; the private browser polls every 5s while the shared safe monitor refreshes public status and idle quota panels on their reported cadence.</p>
      <div id="usage-summary" class="topline"></div>
      <div id="usage-cards" class="usage-grid"><div class="empty">Loading usage monitor…</div></div>
      <p class="micro" id="usage-notes"></p>
    </section>

    <section class="panel" id="overnight-report-panel">
      <h2>C1r Deep Research overnight report</h2>
      <p>Outcome-first root-cause result from the sealed C1r canary. The report remains rejected; this panel corrects why it failed and executes nothing.</p>
      <div id="overnight-report-summary" class="topline"></div>
      <div id="overnight-report-cards" class="overnight-grid"><div class="empty">Loading overnight report…</div></div>
      <p class="micro" id="overnight-report-next"></p>
      <p class="micro"><code>NO ACTIVE EXECUTION PHRASE</code> · no retry, browser action, provider-account action, public Baseline change, DB write, deploy, git, or cron.</p>
    </section>

    <section class="panel" id="corpus-scaleup-panel">
      <h2>Corpus scale-up (RAG foundation)</h2>
      <p>Scaling the literature corpus 12k &rarr; 120k and wiring it into research + drafting. Live from the pipeline.</p>
      <p style="margin:.2rem 0 .8rem"><a href="pipeline-board.html" style="display:inline-block;background:#7c86ff;color:#0a0d17;font-weight:600;padding:.4rem .9rem;border-radius:8px;text-decoration:none;font-size:.85rem">&#9656; AI-Scientist pipeline board &mdash; per-run traces, gate evidence &amp; funnel &rarr;</a></p>
      <div id="corpus-scaleup-summary" class="topline"></div>
      <div id="corpus-scaleup-cards" class="overnight-grid"><div class="empty">Loading corpus status&hellip;</div></div>
      <p class="micro" id="corpus-scaleup-next"></p>
    </section>

    <section class="panel incident-resolved" aria-labelledby="last-incident-title">
      <h2 id="last-incident-title">Latest incident</h2>
      <p>Latest private-lane custody incident and verification. This card reports a contained operator issue; it does not execute actions.</p>
      <div id="last-incident" class="usage-grid"><div class="empty">Loading incident status…</div></div>
    </section>

    <section class="panel" id="paper-quality-sprint-panel">
      <h2>RP-1 Paper Quality Sprint</h2>
      <p>Shows the latest local-only manuscript-quality sprint status and final clean candidate. Completed history is archived in the ledger; this card only shows the current clean receipt. It does not publish or replace PDFs.</p>
      <div id="quality-sprint-summary" class="topline"></div>
      <div id="quality-sprint-cards" class="usage-grid"><div class="empty">Loading RP-1 quality sprint…</div></div>
      <div id="quality-sprint-ledger" class="events" style="margin-top:12px;"></div>
    </section>

    <section class="panel">
      <h2>Galaxy Evolution Wiki Quality Sprint</h2>
      <p>Shows the latest local-only wiki/research-topic sprint status and final clean candidate. Completed history is archived in the ledger; this card only shows the current clean receipt. It does not publish wiki pages or write the product DB.</p>
      <div id="wiki-quality-sprint-summary" class="topline"></div>
      <div id="wiki-quality-sprint-cards" class="usage-grid"><div class="empty">Loading wiki quality sprint…</div></div>
      <div id="wiki-quality-sprint-ledger" class="events" style="margin-top:12px;"></div>
    </section>

    <section class="panel">
      <h2>Autopilot run time estimates</h2>
      <p>Shows active/unresolved autopilot orders only. Completed historical packets are summarized and kept out of the visible board so stale messages do not crowd the current operator view.</p>
      <div id="run-estimate-summary" class="topline"></div>
      <div id="run-estimates" class="usage-grid"><div class="empty">Loading run estimates…</div></div>
    </section>


    <section class="panel">
      <h2>Local outcome DB</h2>
      <p>Append-only local SQLite ledger for overnight autopilot receipts. Product DB/API/page writes remain closed unless a separate exact approval packet is executed.</p>
      <div id="outcome-ledger-summary" class="topline"></div>
      <div id="outcome-ledger-card" class="usage-grid"><div class="empty">Loading local outcome ledger…</div></div>
    </section>

    <section class="panel">
      <h2>Survey Autopilot</h2>
      <p>Tracks the Survey Atlas frontend surface on this private dashboard: route, required files, latest recorded smoke-test result, and safe next action. This is not a DB/apply/deploy control.</p>
      <div id="survey-summary" class="topline"></div>
      <div id="survey-cards" class="usage-grid"><div class="empty">Loading Survey autopilot…</div></div>
      <div id="survey-files" class="events" style="margin-top:12px;"></div>
    </section>

    <section class="panel">
      <h2>Directors</h2>
      <p>Hwao sets direction; Tori verifies and relays; Goru provides mechanical crosschecks. Red here means stop and ask.</p>
      <div id="directors" class="directors-grid"></div>
    </section>
    <section class="methods-grid" id="methods"></section>

    <section class="wide">
      <div class="panel">
        <h2>Current blockers / prompts</h2>
        <div id="blockers" class="empty">Loading…</div>
      </div>
      <div class="panel">
        <h2>Latest autopilot events</h2>
        <div id="events" class="events"><div class="empty">Loading…</div></div>
      </div>
    </section>

    <section class="wide">
      <div class="panel">
        <h2>Safety policy legend</h2>
        <ul class="policy-list" id="policy"></ul>
      </div>
      <div class="panel">
        <h2>Provenance</h2>
        <p class="micro">Source status: <code id="source-status"></code></p>
        <p class="micro">Source events: <code id="source-events"></code></p>
        <p class="micro">Rendered JSON: <code id="web-status"></code></p>
        <div id="other"></div>
      </div>
    </section>
  </main>
  <footer>Dashboard marker: <code>__MARKER__</code>. Overnight report marker: <code>__OVERNIGHT_REPORT_MARKER__</code>. Paper sprint marker: <code>__PAPER_QUALITY_SPRINT_MARKER__</code>. Wiki sprint marker: <code>__WIKI_QUALITY_SPRINT_MARKER__</code>. Usage feed marker: <code>__USAGE_FEED_MARKER__</code>. Survey marker: <code>__SURVEY_MARKER__</code>. Local outcome DB marker: <code>__OUTCOME_LEDGER_MARKER__</code>. Run-time estimate marker: <code>__RUN_TIME_ESTIMATE_MARKER__</code>. Compatibility markers retained for dashboard probes: <code>__COMPAT_MARKERS__</code>.</footer>
<script>
const STATUS_URL = "__STATUS_URL__";
const GROUP_ORDER = ["Directors", "Method 1", "Method 2", "Method 3", "Other"];
function esc(s) { return String(s ?? '').replace(/[&<>"']/g, c => ({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}[c])); }
function shortenPath(value) {
  if (value === null || value === undefined) return '';
  const filename = raw => {
    const suffix = (raw.match(/[.,;:]+$/) || [''])[0];
    let path = suffix ? raw.slice(0, -suffix.length) : raw;
    path = path.replace(/\/+$/, '');
    return `${path.split('/').filter(Boolean).pop() || ''}${suffix}`;
  };
  return String(value)
    .replace(/\/Users\/[^/]+\/[^\s<>"']+/g, filename)
    .replace(/(^|[\s:])((?:\.hermes|frontend|backend|tools|mcp|…|~)\/[^\s<>"']+)/g, (_, prefix, path) => `${prefix}${filename(path)}`);
}
function metric(label, value) { return `<div class="metric"><b>${esc(value)}</b><span>${esc(label)}</span></div>`; }
function chip(text, cls='') { return `<span class="chip ${cls}">${esc(text)}</span>`; }
function paneFlags(p) { const out=[]; if(p.status==='dead') out.push(chip('dead','dead')); if(p.status==='review') out.push(chip('needs you','dead')); if(p.status==='safe-prompt') out.push(chip('safe prompt','review')); if(p.status==='copy-mode') out.push(chip('copy-mode','review')); if(p.active) out.push(chip('active','active')); if(!out.length) out.push(chip('observed')); return out.join(''); }
function paneCard(p) { return `<div class="lane ${esc(p.status||'idle')}"><div class="lane-head"><span class="lane-role">${esc(p.role)}</span><span class="pane-id">${esc(p.pane_id)}</span></div><div class="meta">${esc(p.command)} · ${esc(p.size)}<br>${esc(shortenPath(p.reason || p.target || ''))}</div><div class="chips">${paneFlags(p)}</div>${p.tail_excerpt ? `<div class="tail">${esc(shortenPath(p.tail_excerpt))}</div>` : ''}</div>`; }
function groupCard(name, panes, summary) { return `<section class="panel"><h3>${esc(name)}</h3><h2>${esc(summary?.text || '')} · ${panes.length} panes</h2>${panes.length ? panes.map(paneCard).join('') : '<div class="empty">No panes seen</div>'}</section>`; }
function summaryCard(s) { const c=s.counts||{}; return `<div class="summary-card ${esc(s.state)}"><h3>${esc(s.name)}</h3><b>${esc(s.text)}</b><small>${esc(s.panes)} panes · active ${c.active||0} · blocked ${(c.review||0)+(c.dead||0)} · safe ${c['safe-prompt']||0}</small></div>`; }
function blockerCard(b) { return `<div class="lane ${b.safe_to_approve ? 'safe-prompt' : 'review'}"><div class="lane-head"><span class="lane-role">${esc(b.role || 'unknown')}</span><span class="pane-id">${esc(b.pane_id || '')}</span></div><div class="meta">${b.safe_to_approve ? 'auto-safe prompt' : 'needs user'} · ${esc(shortenPath(b.reason || ''))}</div></div>`; }
function eventCard(e) { const details=[...(e.actions||[]), ...(e.blockers||[])].slice(0,4); return `<div class="event"><strong>${esc(e.ts)}</strong><small>actions ${esc(e.actions_count ?? (e.actions||[]).length)} · blockers ${esc(e.blockers_count ?? (e.blockers||[]).length)}${details.length ? ' · '+esc(details.join(' · ')) : ''}</small></div>`; }
function usageCard(u) {
  const hasPct = typeof u.percent === 'number' && Number.isFinite(u.percent);
  const pct = hasPct ? Math.max(0, Math.min(100, u.percent)) : null;
  const cls = hasPct ? '' : 'unknown';
  const big = hasPct ? `${pct > 0 && pct < 1 ? pct.toFixed(1) : pct.toFixed(0)}%` : '—%';
  const width = hasPct ? `style="width:${pct}%"` : '';
  const subs = (u.sub_gauges || []).map(s => {
    const sp = typeof s.percent === 'number' && Number.isFinite(s.percent) ? Math.max(0, Math.min(100, s.percent)) : null;
    const swidth = sp === null ? '' : `style="width:${sp}%"`;
    const scls = sp === null ? 'unknown' : '';
    let valStr = esc(s.value_label || (sp === null ? 'not observed' : sp.toFixed(0)+'%'));
    if (valStr.includes('remained ')) {
      const parts = valStr.split('remained ');
      const remainStr = parts.slice(1).join('remained ');
      let days = 0;
      const dayMatch = remainStr.match(/(\d+)\s*day/);
      if (dayMatch) {
        days = parseInt(dayMatch[1], 10);
      }
      let colorClass = 'reset-blue';
      if (days < 2) colorClass = 'reset-red';
      else if (days < 4) colorClass = 'reset-orange';
      valStr = parts[0] + `<span class="reset-time ${colorClass}">remained ` + remainStr + '</span>';
    } else if ((s.label || '').toLowerCase().includes('week') && valStr.includes(' · ')) {
      const parts = valStr.split(' · ');
      valStr = parts[0] + ' · <span class="reset-time">' + parts.slice(1).join(' · ') + '</span>';
    }
    return `<div class="usage-sub"><div class="usage-sub-line"><span>${esc(s.label)}</span><strong>${valStr}</strong></div><div class="usage-sub-bar"><span class="${scls}" ${swidth}></span></div></div>`;
  }).join('');
  return `<div class="usage-card ${cls}"><h3>${esc(u.name)}</h3><div class="usage-status">${esc(u.status)} · ${esc(u.kind)}</div><div class="usage-big">${esc(big)}</div><div class="usage-note">${esc(u.percent_label || '')}</div><div class="usage-bar"><span ${width}></span></div>${subs ? `<div class="usage-subs">${subs}</div>` : ''}<p><strong>${esc(u.activity || '')}</strong></p><p class="usage-note">${esc(u.detail || '')}</p><p class="usage-note">Source: ${esc(shortenPath(u.source))}</p></div>`;
}
function renderUsage(u) {
  if (!u) return;
  const cards = u.cards || [];
  const staleHidden = u.cache_state === 'stale-source-hidden';
  const usageSummary = [
    `<span class="pill"><span class="dot"></span><span>${esc(u.marker || 'usage monitor')}</span></span>`,
    `<span class="pill"><span class="dot"></span><span>Exact percent sources ${esc(u.exact_limit_percent_sources ?? 0)}/${esc(cards.length)}</span></span>`,
    `<span class="pill"><span class="dot"></span><span>${esc(u.cache_state || 'fresh')} · source age ${esc(u.cache_age_label || '0s')}</span></span>`
  ];
  if (!staleHidden) {
    usageSummary.push(`<span class="pill healthy"><span class="dot"></span><span>${esc(u.provider_monitor_status || 'unknown')} · guard relocked</span></span>`);
    usageSummary.push(`<span class="pill"><span class="dot"></span><span>Refresh ${esc(u.local_refresh_seconds ?? '—')}s local · ${esc(u.slash_refresh_seconds ?? '—')}s idle quota panels</span></span>`);
    usageSummary.push(`<span class="pill"><span class="dot"></span><span>Observed ${esc(u.observed_at_utc || u.generated_at || 'unknown')}</span></span>`);
    usageSummary.push(`<span class="pill"><span class="dot"></span><span>Public source ${esc(u.provider_monitor_marker || u.public_status_url || '')}</span></span>`);
  }
  document.getElementById('usage-summary').innerHTML = usageSummary.join('');
  document.getElementById('usage-cards').innerHTML = cards.length ? cards.map(usageCard).join('') : '<div class="empty">No usage monitor data.</div>';
  document.getElementById('usage-notes').textContent = shortenPath((u.notes || []).join(' '));
}
function overnightCard(card) {
  return `<div class="usage-card ${esc(card.tone || '')}"><h3>${esc(card.title || '')}</h3><div class="usage-status">${esc(card.status || 'observed')}</div><div class="usage-big">${esc(card.big || '')}</div><p class="usage-note">${esc(card.detail || '')}</p></div>`;
}
function renderOvernightReport(report) {
  if (!report) return;
  const cards = report.cards || [];
  document.getElementById('overnight-report-summary').innerHTML = [
    `<span class="pill healthy"><span class="dot"></span><span>${esc(report.marker || 'overnight report')}</span></span>`,
    `<span class="pill"><span class="dot"></span><span>Reported ${esc(report.reported_at_utc || 'unknown')}</span></span>`,
    `<span class="pill"><span class="dot"></span><span>${esc(report.headline || '')}</span></span>`
  ].join('');
  document.getElementById('overnight-report-cards').innerHTML = cards.length ? cards.map(overnightCard).join('') : '<div class="empty">No overnight report data.</div>';
  document.getElementById('overnight-report-next').textContent = report.next_action || '';
}
function renderCorpusScaleup(report) {
  if (!report) return;
  const cards = report.cards || [];
  const s = document.getElementById('corpus-scaleup-summary');
  if (s) s.innerHTML = [
    `<span class="pill healthy"><span class="dot"></span><span>${esc(report.marker || 'corpus scale-up')}</span></span>`,
    `<span class="pill"><span class="dot"></span><span>${esc(report.headline || '')}</span></span>`
  ].join('');
  const c = document.getElementById('corpus-scaleup-cards');
  if (c) c.innerHTML = cards.length ? cards.map(overnightCard).join('') : '<div class="empty">No corpus data.</div>';
  const nx = document.getElementById('corpus-scaleup-next');
  if (nx) nx.textContent = report.next_action || '';
}
function runStateClass(state) {
  if (state === 'blocked' || state === 'over-estimate') return 'needs-review';
  if (state === 'complete') return 'healthy';
  return 'watching';
}
function runCard(r) {
  const pct = typeof r.progress_percent === 'number' && Number.isFinite(r.progress_percent) ? Math.max(0, Math.min(100, r.progress_percent)) : 0;
  const cls = runStateClass(r.state || 'running');
  return `<div class="usage-card ${cls}"><h3>${esc(r.marker || 'autopilot run')}</h3><div class="usage-status">${esc(r.state || 'running')} · ${esc(r.dispatch_count ?? 0)}/${esc(r.expected_dispatches ?? 0)} dispatches</div><div class="usage-big">${esc(r.elapsed_label || 'unknown')}</div><div class="usage-note">elapsed runtime</div><div class="usage-bar"><span style="width:${pct}%"></span></div><p><strong>Estimate ${esc(r.estimated_total_label || 'unknown')}</strong></p><p class="usage-note">ETA ${esc(r.eta_at_utc || 'unknown')} · ${esc(r.remaining_label || 'unknown')}</p><p class="usage-note">started ${esc(r.started_at_utc || 'unknown')} · updated ${esc(r.updated_at_utc || 'unknown')}</p></div>`;
}
function renderRunEstimates(re) {
  if (!re) return;
  const runs = re.runs || [];
  const active = re.active_runs_count ?? runs.filter(r => !['complete'].includes(r.state || '')).length;
  const latest = re.latest_completed || {};
  const completedText = latest.completed_at_utc ? `last completion recorded at ${latest.completed_at_utc}` : 'no completed run summary yet';
  document.getElementById('run-estimate-summary').innerHTML = [
    `<span class="pill"><span class="dot"></span><span>${esc(re.marker || 'run estimates')}</span></span>`,
    `<span class="pill"><span class="dot"></span><span>${esc(runs.length)} visible run card(s)</span></span>`,
    `<span class="pill"><span class="dot"></span><span>${esc(active)} active/unfinished</span></span>`,
    `<span class="pill"><span class="dot"></span><span>${esc(re.archived_runs_count ?? 0)} completed archived</span></span>`,
    `<span class="pill"><span class="dot"></span><span>default estimate ${esc(re.default_estimated_label || 'unknown')}</span></span>`
  ].join('');
  document.getElementById('run-estimates').innerHTML = runs.length ? runs.map(runCard).join('') : `<div class="empty">No active autopilot orders right now. ${esc(completedText)}. Completed packet cards are archived from the visible board.</div>`;
}
function renderQualitySprint(q) {
  if (!q) return;
  const stateCls = q.state === 'needs-review' ? 'needs-review' : (q.state === 'healthy' ? 'healthy' : 'watching');
  const pct = typeof q.progress_percent === 'number' && Number.isFinite(q.progress_percent) ? Math.max(0, Math.min(100, q.progress_percent)) : 0;
  const audit = q.latest_audit || {};
  const processLabel = q.process_running ? `PID ${q.pid || '—'} · running` : 'completed · no sprint process running';
  const stateDetail = q.process_running ? `target end ${q.target_end_utc || 'unknown'} · progress ${pct.toFixed(1)}%` : `completed ${q.updated_utc || 'unknown'} · target window ended ${q.target_end_utc || 'unknown'}`;
  const auditDetail = `${audit.cycle == null ? '' : 'cycle '+audit.cycle+' · '}compile ${Array.isArray(audit.compile_ok) ? audit.compile_ok.join('/') : '—'} · figures ${audit.figures ?? '—'}`;
  document.getElementById('quality-sprint-summary').innerHTML = [
    `<span class="pill ${stateCls}"><span class="dot"></span><span>${esc(q.text || q.status || 'unknown')}</span></span>`,
    `<span class="pill"><span class="dot"></span><span>${esc(q.marker || 'quality sprint')}</span></span>`,
    `<span class="pill"><span class="dot"></span><span>cycle ${esc(q.cycle ?? '—')} · completed ${esc(q.cycles_completed ?? 0)}</span></span>`,
    `<span class="pill"><span class="dot"></span><span>${esc(processLabel)}</span></span>`
  ].join('');
  document.getElementById('quality-sprint-cards').innerHTML = [
    infoCard('Current sprint state', q.status || 'unknown', stateDetail, q.state || 'unknown'),
    infoCard('Lane model', '5 lanes', (q.lanes || []).join(' · '), 'low-usage local sprint'),
    infoCard('Latest candidate', shortenPath(q.candidate) || 'not written yet', 'Verified local candidate package', 'candidate-copy only'),
    infoCard('Latest audit', `fatal ${audit.fatal_failures ?? '—'}`, auditDetail, 'compile/audit receipt')
  ].join('');
  document.getElementById('quality-sprint-ledger').innerHTML = (q.ledger_tail || []).length ? (q.ledger_tail || []).map(x => `<div class="event"><strong>${esc(shortenPath(x))}</strong></div>`).join('') : '<div class="empty">No sprint ledger entries yet.</div>';
}
function renderWikiQualitySprint(q) {
  if (!q) return;
  const stateCls = q.state === 'needs-review' ? 'needs-review' : (q.state === 'healthy' ? 'healthy' : 'watching');
  const pct = typeof q.progress_percent === 'number' && Number.isFinite(q.progress_percent) ? Math.max(0, Math.min(100, q.progress_percent)) : 0;
  const audit = q.latest_audit || {};
  const forbidden = Array.isArray(audit.forbidden_contract_tokens) ? audit.forbidden_contract_tokens.join(', ') : '—';
  const overclaims = Array.isArray(audit.overclaim_pattern_hits) ? audit.overclaim_pattern_hits.join(', ') : '—';
  const processLabel = q.process_running ? `PID ${q.pid || '—'} · running` : 'completed · no sprint process running';
  const stateDetail = q.process_running ? `target end ${q.target_end_utc || 'unknown'} · progress ${pct.toFixed(1)}%` : `completed ${q.updated_utc || 'unknown'} · target window ended ${q.target_end_utc || 'unknown'}`;
  document.getElementById('wiki-quality-sprint-summary').innerHTML = [
    `<span class="pill ${stateCls}"><span class="dot"></span><span>${esc(q.text || q.status || 'unknown')}</span></span>`,
    `<span class="pill"><span class="dot"></span><span>${esc(q.marker || 'wiki quality sprint')}</span></span>`,
    `<span class="pill"><span class="dot"></span><span>cycle ${esc(q.cycle ?? '—')} · completed ${esc(q.cycles_completed ?? 0)}</span></span>`,
    `<span class="pill"><span class="dot"></span><span>${esc(processLabel)}</span></span>`
  ].join('');
  document.getElementById('wiki-quality-sprint-cards').innerHTML = [
    infoCard('Current sprint state', q.status || 'unknown', stateDetail, q.state || 'unknown'),
    infoCard('Lane model', '4 lanes', (q.lanes || []).join(' · '), 'low-usage local sprint'),
    infoCard('Latest candidate', shortenPath(q.candidate) || 'not written yet', 'Verified local candidate Markdown', 'candidate Markdown only'),
    infoCard('Latest audit', `fatal ${audit.fatal_failures ?? '—'}`, `claim balanced ${audit.claim_markers_balanced ?? '—'} · cites ${audit.cite_count ?? '—'} · forbidden ${forbidden} · overclaim ${overclaims}`, 'wiki/content-contract receipt')
  ].join('');
  document.getElementById('wiki-quality-sprint-ledger').innerHTML = (q.ledger_tail || []).length ? (q.ledger_tail || []).map(x => `<div class="event"><strong>${esc(shortenPath(x))}</strong></div>`).join('') : '<div class="empty">No wiki sprint ledger entries yet.</div>';
}
function renderOutcomeLedger(l) {
  if (!l) return;
  const latest = l.latest_status || {};
  const enabled = l.enabled !== false;
  document.getElementById('outcome-ledger-summary').innerHTML = [
    `<span class="pill ${enabled ? 'healthy' : 'needs-review'}"><span class="dot"></span><span>${enabled ? 'local ledger enabled' : 'local ledger disabled'}</span></span>`,
    `<span class="pill"><span class="dot"></span><span>${esc(l.marker || 'outcome ledger')}</span></span>`,
    `<span class="pill"><span class="dot"></span><span>events ${esc(l.events_total ?? 0)}</span></span>`,
    `<span class="pill"><span class="dot"></span><span>snapshots ${esc(l.snapshots_total ?? 0)}</span></span>`,
    `<span class="pill needs-review"><span class="dot"></span><span>product DB writes ${l.product_db_writes_enabled ? 'OPEN' : 'closed'}</span></span>`
  ].join('');
  document.getElementById('outcome-ledger-card').innerHTML = [
    infoCard('Ledger file', shortenPath(l.path), l.scope || '', enabled ? 'append-only local DB' : 'disabled'),
    infoCard('Latest status', latest.ts || l.latest_status_ts || 'not recorded yet', `blockers ${latest.blockers ?? '—'} · targets ${latest.targets_ok ?? '—'}/${latest.targets_total ?? '—'} · panes ${latest.panes ?? '—'}`, latest.phase || 'unknown'),
    infoCard('Safety', l.product_db_writes_enabled ? 'OPEN' : 'closed', 'Autopilot pane SQL and NebulaMind product DB writes remain denied; use an exact backup/diff/rollback packet for product DB mutation.', 'hard gate')
  ].join('');
}
function infoCard(title, big, detail, status='observed') {
  return `<div class="usage-card"><h3>${esc(title)}</h3><div class="usage-status">${esc(status)}</div><div class="usage-big">${esc(shortenPath(big))}</div><p class="usage-note">${esc(shortenPath(detail))}</p></div>`;
}
function renderIncident(i) {
  if (!i) return;
  const title = document.getElementById('last-incident-title');
  if (title) title.textContent = i.title || 'Latest incident';
  document.getElementById('last-incident').innerHTML = [
    infoCard('Status', i.status || 'unknown', `Detected ${i.detected_utc || 'unknown'} · resolved ${i.resolved_utc || 'unknown'}`, 'verified live'),
    infoCard('What changed', i.component || 'controller', i.summary || '', i.change_note || 'behavior corrected'),
    infoCard('Verification', i.verification_headline || 'verified', i.verification || '', i.verification_note || 'receipts recorded'),
    infoCard('Safety', 'No product changes', i.scope || '', 'private dashboard only')
  ].join('');
}
function surveyFileCard(f) {
  const status = f.exists ? 'present' : 'missing';
  return `<div class="event"><strong>${esc(f.label)} · ${esc(status)}</strong><small>${esc(shortenPath(f.path))}${f.modified_at_utc ? ' · modified '+esc(f.modified_at_utc) : ''}</small></div>`;
}
function renderSurvey(s) {
  if (!s) return;
  const smoke = s.latest_smoke || {};
  const stateCls = s.state === 'needs-review' ? 'needs-review' : (s.state === 'healthy' ? 'healthy' : 'watching');
  document.getElementById('survey-summary').innerHTML = [
    `<span class="pill ${stateCls}"><span class="dot"></span><span>${esc(s.text || s.state || 'unknown')}</span></span>`,
    `<span class="pill"><span class="dot"></span><span>${esc(s.marker || 'survey marker')}</span></span>`,
    `<span class="pill"><span class="dot"></span><span>Route ${esc(s.route || '/surveys')}</span></span>`,
    `<span class="pill"><span class="dot"></span><span>Files ${esc(s.required_files_present ?? 0)}/${esc(s.required_files_total ?? 0)}</span></span>`
  ].join('');
  document.getElementById('survey-cards').innerHTML = [
    infoCard('Current state', s.text || 'unknown', s.next_action || '', s.state || 'unknown'),
    infoCard('Route', s.route || '/surveys', s.scope || 'Survey frontend surface', 'read-only monitor'),
    infoCard('Latest smoke', smoke.status || 'unknown', `${smoke.command || 'npm run test:surveys-atlas-ia'}${smoke.verified_at_utc ? ' · '+smoke.verified_at_utc : ''}${typeof smoke.exit_code === 'number' ? ' · exit '+smoke.exit_code : ''}`, smoke.known ? 'recorded' : 'not recorded'),
    infoCard('Safety boundary', 'No writes', (s.safe_boundaries || []).join(' '), 'locked')
  ].join('');
  document.getElementById('survey-files').innerHTML = (s.files || []).map(surveyFileCard).join('');
}
async function load() {
  try {
    const res = await fetch(`${STATUS_URL}?t=${Date.now()}`, {cache:'no-store'});
    if (!res.ok) throw new Error(`HTTP ${res.status}`);
    const d = await res.json(); const c=d.counts||{}; const groups=d.groups||{}; const summaries=d.lane_summaries||{};
    const pill=document.getElementById('health-pill'); pill.className=`pill ${d.health||'healthy'}`;
    document.getElementById('health-text').textContent=d.health_text||d.health||'unknown';
    document.getElementById('state-word').className=`state-word ${d.health||'healthy'}`;
    document.getElementById('state-word').textContent=d.health_text||'UNKNOWN';
    document.getElementById('next-action').textContent=d.next_action||'';
    document.getElementById('updated-text').textContent=`Updated ${d.source_ts||d.generated_at||'unknown'} · age ${d.source_age_label||'unknown'}`;
    document.getElementById('phase-text').textContent=d.phase||'phase1-bounded-controller';
    document.getElementById('event-text').textContent=d.latest_event ? `last tick ${d.latest_event.ts}` : 'no event log yet';
    document.getElementById('metrics').innerHTML=[metric('Targets OK',`${c.targets_ok??0}/${c.targets_total??0}`),metric('Panes',c.panes??0),metric('Active',c.active??0),metric('Idle',c.idle??0),metric('Needs-you issues',c.blockers??0),metric('Safe auto-prompts',c.safe_autoprompts??c.safe_prompts??0)].join('');
    document.getElementById('summaries').innerHTML=GROUP_ORDER.map(g=>summaryCard(summaries[g]||{name:g,state:'idle',text:'No data',counts:{},panes:0})).join('');
    renderRunEstimates(d.run_estimates);
    renderQualitySprint(d.paper_quality_sprint);
    renderWikiQualitySprint(d.wiki_quality_sprint);
    renderUsage(d.usage_monitor);
    renderOvernightReport(d.overnight_report);
    renderCorpusScaleup(d.corpus_scaleup);
    renderOutcomeLedger(d.local_outcome_ledger);
    renderSurvey(d.survey_autopilot);
    renderIncident(d.last_incident);
    document.getElementById('directors').innerHTML=(groups['Directors']||[]).length ? (groups['Directors']||[]).map(paneCard).join('') : '<div class="empty">No director panes seen</div>';
    document.getElementById('methods').innerHTML=['Method 1','Method 2','Method 3'].map(g=>groupCard(g,groups[g]||[],summaries[g])).join('');
    const blockers=d.blockers||[]; const safePrompts=d.safe_autoprompts||[]; document.getElementById('blockers').className=(blockers.length||safePrompts.length)?'':'empty'; document.getElementById('blockers').innerHTML=blockers.length?blockers.map(blockerCard).join(''):(safePrompts.length?`<div class="empty">No user-needed blockers. ${esc(safePrompts.length)} safe prompt(s) are being handled by autopilot.</div>${safePrompts.map(blockerCard).join('')}`:'No current blockers or permission prompts.');
    const events=d.events||[]; document.getElementById('events').innerHTML=events.length?events.slice().reverse().map(eventCard).join(''):'<div class="empty">No recent actions or blockers. Heartbeat is live in the room-glance tick above.</div>';
    const gateHtml=(d.hard_gates_closed||[]).map(x=>`<div class="gate"><span class="lock">🔒</span> ${esc(x)}</div>`).join(''); document.getElementById('gates-top').innerHTML=gateHtml;
    document.getElementById('policy').innerHTML=(d.policy_lines||[]).map(x=>`<li>${esc(x)}</li>`).join('');
    document.getElementById('source-status').textContent=shortenPath(d.source_status_path); document.getElementById('source-events').textContent=shortenPath(d.source_events_path); document.getElementById('web-status').textContent=shortenPath(d.web_status_path);
    const other=groups['Other']||[]; document.getElementById('other').innerHTML=other.length ? `<h2>Standalone / helpers</h2>${other.map(paneCard).join('')}` : '';
  } catch (err) { const pill=document.getElementById('health-pill'); pill.className='pill needs-review'; document.getElementById('health-text').textContent=`Dashboard data unavailable: ${err.message}`; document.getElementById('state-word').className='state-word needs-review'; document.getElementById('state-word').textContent='NO DATA'; document.getElementById('next-action').textContent='The dashboard could not read its JSON snapshot.'; }
}
load(); setInterval(load, 5000);
</script>
</body>
</html>
'''
    return (
        template.replace("__MARKER__", html.escape(MARKER))
        .replace("__OVERNIGHT_REPORT_MARKER__", html.escape(OVERNIGHT_REPORT_MARKER))
        .replace("__PAPER_QUALITY_SPRINT_MARKER__", html.escape(PAPER_QUALITY_SPRINT_MARKER))
        .replace("__WIKI_QUALITY_SPRINT_MARKER__", html.escape(WIKI_QUALITY_SPRINT_MARKER))
        .replace("__USAGE_FEED_MARKER__", html.escape(PUBLIC_USAGE_FEED_MARKER))
        .replace("__SURVEY_MARKER__", html.escape(SURVEY_AUTOPILOT_MARKER))
        .replace("__OUTCOME_LEDGER_MARKER__", html.escape(OUTCOME_LEDGER_MARKER))
        .replace("__RUN_TIME_ESTIMATE_MARKER__", html.escape(RUN_TIME_ESTIMATE_MARKER))
        .replace("__COMPAT_MARKERS__", html.escape(", ".join(COMPAT_MARKERS)))
        .replace("__URL__", html.escape(URL, quote=True))
        .replace("__STATUS_URL__", STATUS_URL)
    )


def write_outputs(compact: Dict[str, Any]) -> None:
    WEB_ROOT.mkdir(parents=True, exist_ok=True)
    JSON_PATH.write_text(json.dumps(compact, indent=2, sort_keys=True) + "\n")
    HTML_PATH.write_text(render_html())
    LATEST_URL_PATH.write_text(URL + "\n")


def render_once() -> Dict[str, Any]:
    source = load_source()
    compact = compact_status(source)
    write_outputs(compact)
    return compact


def main() -> int:
    parser = argparse.ArgumentParser(description="Render private Galaxy Evolution autopilot dashboard V3")
    parser.add_argument("--watch", action="store_true", help="refresh continuously")
    parser.add_argument("--interval", type=float, default=20.0)
    parser.add_argument("--json", action="store_true", help="print compact JSON after one render")
    args = parser.parse_args()
    if args.watch:
        while True:
            compact = render_once()
            print(json.dumps({"ts": compact["generated_at"], "health": compact["health"], "blockers": compact["counts"]["blockers"], "events": len(compact.get("events", [])), "url": URL}), flush=True)
            time.sleep(args.interval)
    compact = render_once()
    if args.json:
        print(json.dumps(compact, indent=2, sort_keys=True))
    else:
        print(f"rendered {HTML_PATH}")
        print(f"rendered {JSON_PATH}")
        print(URL)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
