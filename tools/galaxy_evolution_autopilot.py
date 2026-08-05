#!/usr/bin/env python3
"""Bounded Phase-1 autopilot for the NebulaMind Galaxy Evolution method board.

This is deliberately a controller, not a broad agent:
- It drives existing tmux panes by role metadata.
- It writes status/state JSON under the Galaxy Evolution mastermind handoff root.
- It mirrors events/status into an append-only local outcome SQLite ledger under
  the handoff root so overnight runs have a checkable durable receipt.
- It can dispatch a saved order to Hwao/director panes.
- It can auto-approve only narrowly classified docs/static prompts.
- It never edits science/content itself, publishes live wiki pages, commits git, deploys,
  touches product DB/API/cockpit/cloud/secrets, or escalates outside the allowlisted roots.
"""
from __future__ import print_function

import argparse
import datetime as _dt
import hashlib
import html
import json
import os
import re
import shlex
import sqlite3
import subprocess
import sys
import time
from pathlib import Path

REPO = Path(os.environ.get("NEBULAMIND_REPO", "/Users/duhokim/NebulaMind/NebulaMind")).resolve()
LIVE_REPO = Path(os.environ.get("NEBULAMIND_LIVE_REPO", "/Users/duhokim/NebulaMind/NebulaMind-origin-main-live")).resolve()
TMUX = os.environ.get("TMUX_BIN", "/opt/homebrew/bin/tmux")
LOCAL_BIN = Path(os.environ.get("HOME", "/Users/duhokim")) / ".local" / "bin"
SCRIPT_PATH = Path(__file__).resolve()

GE_ROOT = REPO / "frontend" / "public" / "agent-reports" / "wiki-method-results" / "galaxy-evolution"
LIVE_GE_ROOT = LIVE_REPO / "frontend" / "public" / "agent-reports" / "wiki-method-results" / "galaxy-evolution"
HANDOFF_ROOT = REPO / ".hermes" / "handoffs" / "galaxy-evolution"
MASTER_ROOT = HANDOFF_ROOT / "mastermind"
STATUS_PATH = MASTER_ROOT / "autopilot-status.json"
STATE_PATH = MASTER_ROOT / "autopilot-state.json"
LOG_PATH = MASTER_ROOT / "autopilot-events.jsonl"
OUTCOME_DB_PATH = Path(os.environ.get("NEBULAMIND_GE_AUTOPILOT_OUTCOME_DB", str(MASTER_ROOT / "autopilot-outcomes.sqlite3")))
OUTCOME_DB_MARKER = "GE_AUTOPILOT_LOCAL_OUTCOME_LEDGER_V1"
RUN_TIME_ESTIMATE_MARKER = "GE_AUTOPILOT_RUN_TIME_ESTIMATES_V1"
IDLE_CONTINUATION_MARKER = "GE_AUTOPILOT_IDLE_CONTINUATION_V1"
try:
    DEFAULT_ESTIMATED_RUN_SECONDS = int(os.environ.get("NEBULAMIND_GE_AUTOPILOT_ESTIMATED_RUN_SECONDS", str(8 * 60 * 60)))
except ValueError:
    DEFAULT_ESTIMATED_RUN_SECONDS = 8 * 60 * 60
try:
    DEFAULT_IDLE_NUDGE_SECONDS = int(os.environ.get("NEBULAMIND_GE_AUTOPILOT_IDLE_NUDGE_SECONDS", "900"))
except ValueError:
    DEFAULT_IDLE_NUDGE_SECONDS = 900
AUTOPILOT_SESSION = os.environ.get("NEBULAMIND_GE_AUTOPILOT_SESSION", "ge-autopilot")
WEB_COCKPIT_ROOT = Path(os.environ.get("NEBULAMIND_GE_AUTOPILOT_WEB_ROOT", "/Users/duhokim/HermesOps/cockpit"))
WEB_STATUS_PATH = WEB_COCKPIT_ROOT / "ge-autopilot-status.json"
WEB_DASHBOARD_PATH = WEB_COCKPIT_ROOT / "ge-autopilot.html"
WEB_LATEST_URL_PATH = WEB_COCKPIT_ROOT / "latest-ge-autopilot-url.txt"
WEB_URL = os.environ.get("NEBULAMIND_GE_AUTOPILOT_WEB_URL", "https://duho-macstudio.taila27502.ts.net/cockpit/ge-autopilot.html")
PRIVATE_DASHBOARD_FILES = {WEB_DASHBOARD_PATH.resolve(), WEB_STATUS_PATH.resolve(), WEB_LATEST_URL_PATH.resolve()}

# LANES — remapped 2026-08-05 (Duho: "kill the mesh sessions and remap the dashboard").
# The three paper-to-wiki method lanes (Method1/PGR mesh-ge-m1-packet, Method2/SFA
# mesh-ge-m2-source, Method3/DMW mesh-ge-m3-debate) were retired with their tmux sessions;
# the wiki era is over and the current NebulaMind is an AI scientist for galaxy evolution.
# Everything the crew runs now lives in the ge-mastermind directors window and the reviewer
# sessions, so there are no separate per-lane sessions to watch. Kept as an empty list rather
# than deleted so the board/dispatch/prompt call sites keep their shape; add an entry here if
# a future lane gets its own session again.
METHODS: list[dict] = []

DIRECTOR = {
    "session": "ge-mastermind",
    "window": "Directors",
    "hwao_role": "Goru-director-live",
    "tori_role": "Tori-director",
}

FORBIDDEN_PATTERNS = [
    r"\b(page_versions|/api/pages|api/pages)\b",
    r"\b(psql|sqlite3|mysql|supabase|prisma\s+migrate|alembic|sqlx)\b",
    r"\b(INSERT|UPDATE|DELETE|DROP|ALTER|TRUNCATE)\b",
    r"\b(git\s+(commit|push|merge|rebase|reset|checkout|switch|branch\s+-D))\b",
    r"\b(npm\s+run\s+(deploy|start)|pnpm\s+(deploy|start)|vercel|flyctl|systemctl|launchctl|pm2|docker\s+compose\s+up)\b",
    r"\b(restart|deploy|migration|migrate|publish\s+live|live\s+publish|production)\b",
    r"\b(cockpit|stable-cockpit|baseline-cockpit|RICH_BASELINE_STABLE_COCKPIT_V1)\b",
    r"\b(gcloud|aws|az\s+|billing|OAuth|oauth|token|secret|\.env|credentials)\b",
    r"\b(cron|crontab|browser|osascript|open\s+https?://)\b",
    r"\brm\s+-rf\b",
    r"\bchmod\s+[-+]?R\b",
]

READ_ONLY_COMMAND_PATTERNS = [
    r"(?:\b(date|grep|rg|find|ls|wc|sed\s+-n|awk|cat|head|tail)\b|(?:^|\s)(?:/usr/bin/)?python3?\s+(- <<|'|\"|-c|-)|\btmux\s+(capture-pane|list-panes|display-message|list-sessions)\b)",
]

PERMISSION_HINT_PATTERNS = [
    r"Bash command",
    r"Do you want to proceed",
    r"permission",
    r"Allow( this)? command",
    r"\bApprove\b",
    r"Run this command",
    r"Create\(",
    r"Write\(",
    r"Edit\(",
    r"Bash\(",
]

SELECTED_ALWAYS_ALLOW_RE = re.compile(
    r"(?im)^[\s>❯➜●*\-]*\s*(?:\d+[.)]\s*)?.*(always|don't ask|dont ask|for this session|allow all)"
)


def utc_now():
    return _dt.datetime.utcnow().replace(microsecond=0).isoformat() + "Z"


def rel(path):
    try:
        return str(Path(path).resolve().relative_to(REPO))
    except Exception:
        return str(path)


def parse_utc(ts):
    if not ts:
        return None
    try:
        return _dt.datetime.strptime(str(ts).replace("Z", ""), "%Y-%m-%dT%H:%M:%S")
    except Exception:
        return None


def seconds_since(start, end=None):
    if not start:
        return None
    if end is None:
        end = _dt.datetime.utcnow().replace(microsecond=0)
    return max(0, int((end - start).total_seconds()))


def duration_label(seconds):
    if seconds is None:
        return "unknown"
    seconds = max(0, int(seconds))
    if seconds < 60:
        return "<1m"
    minutes = seconds // 60
    if minutes < 60:
        return "{}m".format(minutes)
    hours = minutes // 60
    mins = minutes % 60
    if hours < 24:
        return "{}h {}m".format(hours, mins) if mins else "{}h".format(hours)
    days = hours // 24
    hrs = hours % 24
    return "{}d {}h".format(days, hrs) if hrs else "{}d".format(days)


def iso_utc(dt_obj):
    if not dt_obj:
        return None
    return dt_obj.replace(microsecond=0).isoformat() + "Z"


def run_cmd(argv, input_text=None, check=False, timeout=20):
    proc = subprocess.run(
        argv,
        input=input_text,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        timeout=timeout,
    )
    if check and proc.returncode != 0:
        raise RuntimeError("command failed: {}\nstdout={}\nstderr={}".format(argv, proc.stdout, proc.stderr))
    return proc


def tmux(args, input_text=None, check=False, timeout=20):
    return run_cmd([TMUX] + list(args), input_text=input_text, check=check, timeout=timeout)


def tmux_target(session, window):
    return "{}:{}".format(session, window)


def target_exists(target):
    return tmux(["has-session", "-t", target], timeout=5).returncode == 0


def list_panes(target):
    fmt = "#{pane_id}\t#{@mesh_role}\t#{@master_role}\t#{pane_title}\t#{pane_current_command}\t#{pane_active}\t#{pane_in_mode}\t#{pane_dead}\t#{pane_width}x#{pane_height}"
    proc = tmux(["list-panes", "-t", target, "-F", fmt], timeout=10)
    panes = []
    if proc.returncode != 0:
        return panes
    for line in proc.stdout.splitlines():
        parts = line.split("\t")
        while len(parts) < 9:
            parts.append("")
        pane_id, mesh_role, master_role, title, current, active, in_mode, dead, size = parts[:9]
        role = mesh_role or master_role or title or "unknown"
        panes.append(
            {
                "pane_id": pane_id,
                "role": role,
                "mesh_role": mesh_role,
                "master_role": master_role,
                "title": title,
                "current_command": current,
                "active": active == "1",
                "in_mode": in_mode == "1",
                "dead": dead == "1",
                "size": size,
                "target": target,
            }
        )
    return panes


def all_board_targets():
    targets = [tmux_target(DIRECTOR["session"], DIRECTOR["window"])]
    for method in METHODS:
        targets.append(tmux_target(method["session"], method["window"]))
    return targets


def collect_panes(include_tail=False, tail_lines=80):
    panes = []
    for target in all_board_targets():
        for pane in list_panes(target):
            if include_tail:
                pane["tail"] = capture_tail(pane["pane_id"], tail_lines=tail_lines)
                if (
                    pane["role"].startswith("Tori")
                    or pane.get("current_command") == "tmux"
                    or "live-view" in pane.get("role", "").lower()
                ):
                    pane["classification"] = {
                        "permission_prompt": False,
                        "safe_to_approve": False,
                        "reason": "Tori/Hermes or nested live-view pane ignored for tmux permission approval",
                    }
                else:
                    pane["classification"] = classify_tail(pane["tail"])
            panes.append(pane)
    return panes


def capture_tail(pane_id, tail_lines=80):
    start = "-{}".format(max(20, int(tail_lines)))
    proc = tmux(["capture-pane", "-J", "-pt", pane_id, "-S", start], timeout=10)
    if proc.returncode != 0:
        return ""
    lines = proc.stdout.splitlines()
    return "\n".join(lines[-tail_lines:])


def find_pane_by_role(role):
    for target in all_board_targets():
        for pane in list_panes(target):
            if pane["role"] == role or pane["title"] == role:
                return pane
    return None


def read_state():
    if not STATE_PATH.exists():
        return {"orders": {}, "created_at": utc_now()}
    try:
        return json.loads(STATE_PATH.read_text())
    except Exception:
        return {"orders": {}, "created_at": utc_now(), "state_read_error": True}


def build_run_estimates(state, status_ts, blockers):
    """Build one dashboard row per dispatched autopilot order/run.

    This is an estimate, not a scheduler guarantee. A run starts at the first
    recorded dispatch for its order and is expected to fit inside the configured
    overnight window unless a future order records its own estimate.
    """
    now_dt = parse_utc(status_ts) or _dt.datetime.utcnow().replace(microsecond=0)
    expected_dispatches = 1 + len(METHODS)
    runs = []
    for marker, raw in sorted((state.get("orders") or {}).items()):
        order = raw if isinstance(raw, dict) else {}
        raw_dispatches = order.get("dispatches")
        dispatches = raw_dispatches if isinstance(raw_dispatches, dict) else {}
        ts_values = []
        for candidate in [order.get("created_at"), order.get("updated_at"), order.get("completed_at")]:
            parsed = parse_utc(candidate)
            if parsed:
                ts_values.append(parsed)
        for dispatch in dispatches.values():
            if isinstance(dispatch, dict):
                parsed = parse_utc(dispatch.get("ts"))
                if parsed:
                    ts_values.append(parsed)
        started_at_dt = min(ts_values) if ts_values else now_dt
        updated_at_dt = max(ts_values) if ts_values else now_dt
        completed_at_dt = parse_utc(order.get("completed_at"))
        end_dt = completed_at_dt or now_dt
        elapsed_seconds = seconds_since(started_at_dt, end_dt)
        estimated_total = int(order.get("estimated_total_seconds") or DEFAULT_ESTIMATED_RUN_SECONDS)
        if estimated_total <= 0:
            estimated_total = DEFAULT_ESTIMATED_RUN_SECONDS
        eta_dt = started_at_dt + _dt.timedelta(seconds=estimated_total)
        remaining_seconds = int((eta_dt - now_dt).total_seconds()) if not completed_at_dt else 0
        progress_percent = min(100, round((float(elapsed_seconds or 0) / float(estimated_total)) * 100, 1)) if estimated_total else None
        if completed_at_dt:
            state_label = "complete"
        elif len(dispatches) < expected_dispatches:
            state_label = "partial-dispatch"
        elif blockers:
            state_label = "blocked"
        elif remaining_seconds < 0:
            state_label = "over-estimate"
        else:
            state_label = "running"
        runs.append(
            {
                "marker": marker,
                "digest": order.get("digest"),
                "state": state_label,
                "started_at_utc": iso_utc(started_at_dt),
                "updated_at_utc": iso_utc(updated_at_dt),
                "completed_at_utc": iso_utc(completed_at_dt),
                "dispatch_count": len(dispatches),
                "expected_dispatches": expected_dispatches,
                "elapsed_seconds": elapsed_seconds,
                "elapsed_label": duration_label(elapsed_seconds),
                "estimated_total_seconds": estimated_total,
                "estimated_total_label": duration_label(estimated_total),
                "eta_at_utc": iso_utc(eta_dt),
                "remaining_seconds": remaining_seconds,
                "remaining_label": ("over by " + duration_label(abs(remaining_seconds))) if remaining_seconds < 0 else duration_label(remaining_seconds),
                "progress_percent": progress_percent,
                "estimate_basis": "configured default NEBULAMIND_GE_AUTOPILOT_ESTIMATED_RUN_SECONDS; override per order with estimated_total_seconds",
            }
        )
    runs.sort(key=lambda r: r.get("started_at_utc") or "", reverse=True)
    return {
        "marker": RUN_TIME_ESTIMATE_MARKER,
        "generated_at": status_ts or utc_now(),
        "default_estimated_seconds": DEFAULT_ESTIMATED_RUN_SECONDS,
        "default_estimated_label": duration_label(DEFAULT_ESTIMATED_RUN_SECONDS),
        "runs_total": len(runs),
        "runs": runs,
    }


def write_json(path, data):
    path.parent.mkdir(parents=True, exist_ok=True)
    tmp = path.with_suffix(path.suffix + ".tmp")
    tmp.write_text(json.dumps(data, indent=2, sort_keys=True) + "\n")
    tmp.replace(path)


def outcome_db_enabled():
    return os.environ.get("NEBULAMIND_GE_AUTOPILOT_OUTCOME_DB_ENABLED", "1").lower() not in ("0", "false", "no", "off")


def outcome_payload_digest(payload):
    return hashlib.sha256(json.dumps(payload, sort_keys=True, separators=(",", ":")).encode("utf-8", "replace")).hexdigest()


def outcome_connect():
    OUTCOME_DB_PATH.parent.mkdir(parents=True, exist_ok=True)
    conn = sqlite3.connect(str(OUTCOME_DB_PATH), timeout=5)
    conn.execute("PRAGMA journal_mode=WAL")
    conn.execute("PRAGMA synchronous=NORMAL")
    conn.execute(
        """
        CREATE TABLE IF NOT EXISTS autopilot_events (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            ts TEXT NOT NULL,
            event_type TEXT NOT NULL,
            payload_json TEXT NOT NULL,
            payload_sha256 TEXT NOT NULL,
            created_at TEXT NOT NULL DEFAULT (strftime('%Y-%m-%dT%H:%M:%SZ','now'))
        )
        """
    )
    conn.execute(
        """
        CREATE TABLE IF NOT EXISTS status_snapshots (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            ts TEXT NOT NULL,
            phase TEXT NOT NULL,
            targets_ok INTEGER NOT NULL,
            targets_total INTEGER NOT NULL,
            panes INTEGER NOT NULL,
            blockers INTEGER NOT NULL,
            review_blockers INTEGER NOT NULL,
            safe_blockers INTEGER NOT NULL,
            payload_json TEXT NOT NULL,
            payload_sha256 TEXT NOT NULL,
            created_at TEXT NOT NULL DEFAULT (strftime('%Y-%m-%dT%H:%M:%SZ','now'))
        )
        """
    )
    conn.execute("CREATE INDEX IF NOT EXISTS idx_autopilot_events_ts ON autopilot_events(ts)")
    conn.execute("CREATE INDEX IF NOT EXISTS idx_status_snapshots_ts ON status_snapshots(ts)")
    conn.execute("CREATE INDEX IF NOT EXISTS idx_status_snapshots_blockers ON status_snapshots(blockers)")
    return conn


def summarize_status_for_outcome(status):
    targets = status.get("targets", [])
    blockers = status.get("blockers", [])
    targets_total = len(targets)
    targets_ok = sum(1 for t in targets if t.get("exists"))
    review_blockers = sum(1 for b in blockers if not b.get("safe_to_approve"))
    safe_blockers = sum(1 for b in blockers if b.get("safe_to_approve"))
    return {
        "marker": OUTCOME_DB_MARKER,
        "ts": status.get("ts") or utc_now(),
        "phase": status.get("phase") or "unknown",
        "targets_ok": targets_ok,
        "targets_total": targets_total,
        "panes": len(status.get("panes", [])),
        "blockers": len(blockers),
        "review_blockers": review_blockers,
        "safe_blockers": safe_blockers,
        "hard_gates_closed": status.get("hard_gates_closed") or [],
        "product_db_writes_enabled": False,
        "scope": "local append-only outcome ledger only; product DB/API/page writes remain closed",
    }


def record_outcome_event(event):
    if not outcome_db_enabled():
        return
    try:
        payload = dict(event)
        payload.setdefault("marker", OUTCOME_DB_MARKER)
        payload.setdefault("product_db_writes_enabled", False)
        payload.setdefault("scope", "local append-only outcome ledger only; product DB/API/page writes remain closed")
        payload_json = json.dumps(payload, sort_keys=True)
        digest = outcome_payload_digest(payload)
        event_type = str(payload.get("event") or payload.get("action") or "event")[:120]
        with outcome_connect() as conn:
            conn.execute(
                "INSERT INTO autopilot_events(ts, event_type, payload_json, payload_sha256) VALUES (?, ?, ?, ?)",
                (payload.get("ts") or utc_now(), event_type, payload_json, digest),
            )
    except Exception as exc:
        error_path = MASTER_ROOT / "autopilot-outcome-ledger-error.json"
        try:
            write_json(error_path, {"ts": utc_now(), "error": str(exc), "path": str(OUTCOME_DB_PATH)})
        except Exception:
            pass


def record_status_snapshot(status):
    if not outcome_db_enabled():
        return
    try:
        payload = summarize_status_for_outcome(status)
        payload_json = json.dumps(payload, sort_keys=True)
        digest = outcome_payload_digest(payload)
        with outcome_connect() as conn:
            conn.execute(
                """
                INSERT INTO status_snapshots(
                    ts, phase, targets_ok, targets_total, panes, blockers,
                    review_blockers, safe_blockers, payload_json, payload_sha256
                ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
                """,
                (
                    payload["ts"], payload["phase"], payload["targets_ok"], payload["targets_total"],
                    payload["panes"], payload["blockers"], payload["review_blockers"],
                    payload["safe_blockers"], payload_json, digest,
                ),
            )
    except Exception as exc:
        error_path = MASTER_ROOT / "autopilot-outcome-ledger-error.json"
        try:
            write_json(error_path, {"ts": utc_now(), "error": str(exc), "path": str(OUTCOME_DB_PATH)})
        except Exception:
            pass


def outcome_ledger_summary():
    summary = {
        "marker": OUTCOME_DB_MARKER,
        "path": str(OUTCOME_DB_PATH),
        "enabled": outcome_db_enabled(),
        "scope": "local append-only outcome ledger only; product DB/API/page writes remain closed",
        "product_db_writes_enabled": False,
    }
    if not outcome_db_enabled():
        return summary
    try:
        with outcome_connect() as conn:
            cur = conn.cursor()
            cur.execute("SELECT COUNT(*), COALESCE(MAX(ts), '') FROM autopilot_events")
            events_total, latest_event_ts = cur.fetchone()
            cur.execute("SELECT COUNT(*), COALESCE(MAX(ts), '') FROM status_snapshots")
            snapshots_total, latest_status_ts = cur.fetchone()
            cur.execute(
                """
                SELECT ts, phase, targets_ok, targets_total, panes, blockers, review_blockers, safe_blockers
                FROM status_snapshots ORDER BY id DESC LIMIT 1
                """
            )
            row = cur.fetchone()
        summary.update({
            "events_total": events_total,
            "snapshots_total": snapshots_total,
            "latest_event_ts": latest_event_ts,
            "latest_status_ts": latest_status_ts,
        })
        if row:
            summary["latest_status"] = {
                "ts": row[0],
                "phase": row[1],
                "targets_ok": row[2],
                "targets_total": row[3],
                "panes": row[4],
                "blockers": row[5],
                "review_blockers": row[6],
                "safe_blockers": row[7],
            }
    except Exception as exc:
        summary["error"] = str(exc)
    return summary


def append_event(event):
    MASTER_ROOT.mkdir(parents=True, exist_ok=True)
    event = dict(event)
    event.setdefault("ts", utc_now())
    with LOG_PATH.open("a") as fh:
        fh.write(json.dumps(event, sort_keys=True) + "\n")
    record_outcome_event(event)


def order_marker(order_path):
    p = Path(order_path).resolve()
    text = p.read_text(errors="replace")
    patterns = [
        r"Marker:\s*`?([A-Z0-9_:-]+)`?",
        r"Order marker:\s*`?([A-Z0-9_:-]+)`?",
        r"^#\s+(.+)$",
    ]
    for pat in patterns:
        m = re.search(pat, text, re.MULTILINE)
        if m:
            raw = m.group(1).strip()
            raw = re.sub(r"[^A-Za-z0-9_.:-]+", "_", raw)[:96]
            if raw:
                return raw
    digest = hashlib.sha256(text.encode("utf-8", "replace")).hexdigest()[:12]
    return "ORDER_{}_{}".format(p.stem, digest)


def order_digest(order_path):
    data = Path(order_path).read_bytes()
    return hashlib.sha256(data).hexdigest()


def is_path_within(path, root):
    try:
        Path(path).resolve().relative_to(Path(root).resolve())
        return True
    except Exception:
        return False


def normalize_candidate_path(token):
    token = token.strip().strip("`'\"),;]")
    if not token:
        return None
    if token.startswith("/Users/duhokim/HermesOps/cockpit"):
        return Path(token)
    if token.startswith("/Users/duhokim/NebulaMind/NebulaMind"):
        return Path(token)
    if token.startswith(".hermes/") or token.startswith("frontend/public/") or token.startswith("tools/"):
        return REPO / token
    return None


def extract_paths(text):
    raw = set()
    for m in re.finditer(r"/Users/duhokim/HermesOps/cockpit/[^\s`'\")\]]+", text):
        raw.add(m.group(0))
    for m in re.finditer(r"/Users/duhokim/NebulaMind/NebulaMind[^\s`'\")\]]+", text):
        raw.add(m.group(0))
    for m in re.finditer(r"(?:\.hermes|frontend/public|tools)/[^\s`'\")\]]+", text):
        raw.add(m.group(0))
    paths = []
    for item in sorted(raw):
        # Collapsed TUI paths often contain ellipses (".h...file.md"). They are
        # not reliable enough for approval decisions; ignore them instead of
        # treating them as real outside-root paths.
        if "..." in item or "…" in item:
            continue
        if item.endswith("-"):
            continue
        p = normalize_candidate_path(item)
        if p is not None:
            paths.append(str(p))
    return paths


def path_allowed(path):
    p = Path(path)
    s = str(p)
    try:
        if p.resolve() in PRIVATE_DASHBOARD_FILES:
            return True
    except Exception:
        pass
    if is_path_within(p, HANDOFF_ROOT):
        return True
    if str(HANDOFF_ROOT).startswith(s):
        # TUI line-wrapping can truncate `.hermes/handoffs/...` path tokens.
        # Treat prefixes of the known handoff root as read-only path fragments.
        return True
    if is_path_within(p, LIVE_GE_ROOT) or str(LIVE_GE_ROOT).startswith(s):
        # Live-root inspection is permitted for this repair packet, but classify_tail
        # separately requires read-only command shape before auto-approval.
        return True
    if str(GE_ROOT).startswith(s):
        # TUI line-wrapping can truncate `galaxy-evolution` to `galaxy-e`.
        # Treat prefixes of the known static root as read-only path fragments.
        return True
    if is_path_within(p, GE_ROOT):
        # Phase 1 is docs/static only. Allow additive method workspaces,
        # same-format rebuild previews, and read-only directory inspections, but
        # do not allow live wiki-page overwrite.
        if p.name == "wiki-page.html":
            return False
        if p.suffix == "":
            return True
        if "same-format-rebuild" in p.parts:
            return True
        if p.suffix.lower() in (".md", ".html", ".json", ".csv") and "agent-reports" in p.parts:
            return True
        return False
    # The controller may inspect its own script and repo-local docs, but should not
    # auto-approve arbitrary tool rewrites from panes.
    if s == str(SCRIPT_PATH):
        return True
    return False


def is_private_dashboard_context(text):
    """True only for the private tailnet ge-autopilot dashboard surface.

    General cockpit/baseline/stable cockpit operations stay forbidden. This
    exception exists so Goru can run read-only local/tailnet probes against the
    private Phase-1 dashboard without requiring the user to navigate agy's TUI.
    """
    if not re.search(r"ge-autopilot(?:-status)?\.(?:html|json)|latest-ge-autopilot-url\.txt", text, flags=re.IGNORECASE):
        return False
    if re.search(r"stable-cockpit|baseline-cockpit|RICH_BASELINE_STABLE_COCKPIT_V1", text, flags=re.IGNORECASE):
        return False
    return bool(
        re.search(r"127\.0\.0\.1:8093/cockpit/ge-autopilot|duho-macstudio\.taila27502\.ts\.net/cockpit/ge-autopilot|/Users/duhokim/HermesOps/cockpit/ge-autopilot", text, flags=re.IGNORECASE)
    )


def contains_forbidden(text):
    for pat in FORBIDDEN_PATTERNS:
        if "cockpit" in pat and is_private_dashboard_context(text):
            continue
        if re.search(pat, text, flags=re.IGNORECASE):
            return pat
    return None


def is_forbidden_string_scan_context(text, forbidden_pattern):
    """Allow read-only safety scans that mention forbidden words as strings."""
    if not forbidden_pattern:
        return False
    if "page_versions" not in forbidden_pattern and "api/pages" not in forbidden_pattern:
        return False
    scanish = is_read_only_commandish(text) or bool(
        re.search(r"\b(print|open\(|read_text|re\.findall|FORBID|forbidden|safety|scan|audit)\b", text, flags=re.IGNORECASE)
    )
    if not scanish:
        return False
    unsafe_verbs = [
        r"requests\s*\.\s*(post|put|patch|delete)",
        r"(?<![\"'])\bfetch\s*\(",
        r"curl\b.*\b-X\s*(POST|PUT|PATCH|DELETE)",
        r"\b(sqlite3|psql|mysql|supabase|prisma\s+migrate|alembic)\b",
    ]
    if any(re.search(pat, text, flags=re.IGNORECASE | re.DOTALL) for pat in unsafe_verbs):
        return False
    return bool(re.search(r"\b(grep|rg|find|re\.findall|FORBID|forbidden|safety|scan|audit|assert|print|echo)\b", text, flags=re.IGNORECASE))


def looks_like_permission_prompt(text):
    return any(re.search(pat, text, flags=re.IGNORECASE) for pat in PERMISSION_HINT_PATTERNS)


def active_permission_context(text):
    """Return the recent slice that looks like an active approval prompt.

    Pane tails contain completed tool logs. A historical "Bash command" or a
    safety paragraph mentioning live publish must not be treated as a current
    blocker. We only classify prompts when the bottom of the TUI still looks
    like it is waiting for approval or recovery input.
    """
    lines = text.splitlines()
    recent = "\n".join(lines[-80:])
    bottom = "\n".join(lines[-14:])
    explicit = [
        r"Do you want to proceed",
        r"Allow( this)? command",
        r"Run this command",
        r"What should Antigravity CLI do instead",
        r"Interrupted · What should",
    ]
    if any(re.search(pat, bottom, flags=re.IGNORECASE) for pat in explicit):
        return current_approval_command_context(recent)
    if re.search(r"accept edits on|new task\?|esc to interrupt|for shortcuts", bottom, flags=re.IGNORECASE):
        return ""
    # Match a real standalone wait state, not completion prose such as
    # "I am awaiting any further dispatches" in a finished assistant answer.
    waiting = re.search(r"\bWaiting\b(?:\.{0,3}|…)?", bottom, flags=re.IGNORECASE)
    toolish = re.search(r"Bash command|Bash\(|Create\(|Write\(|Edit\(", recent, flags=re.IGNORECASE)
    if waiting and toolish:
        return current_approval_command_context(recent)
    return ""


def current_approval_command_context(text):
    """Limit prompt classification to the active command/prompt block.

    Claude/agy pane tails often keep the previous user prompt above the approval
    menu. Those prompts intentionally restate hard gates such as /api/pages,
    browser, cron, and page_versions; scanning them makes a safe read-only Bash
    prompt look unsafe. The approval decision should inspect the command block
    currently under "Do you want to proceed?" and not stale surrounding prose.
    """
    markers = ["\n Bash command", "\n  Bash command", "\n\tBash command"]
    start = -1
    for marker in markers:
        idx = text.rfind(marker)
        if idx > start:
            start = idx
    if start >= 0:
        return text[start:]
    return text


def selected_always_allow(text):
    # If a TUI cursor appears to be on an always-allow/session-wide option, do not
    # blindly hit Enter. Human/Tori can move it to one-time approval first.
    for line in text.splitlines()[-30:]:
        if SELECTED_ALWAYS_ALLOW_RE.search(line):
            if any(marker in line for marker in (">", "❯", "➜", "●", "*")):
                return True
    return False


def is_read_only_commandish(text):
    return any(re.search(pat, text, flags=re.IGNORECASE) for pat in READ_ONLY_COMMAND_PATTERNS)


def is_live_root_path(path):
    p = Path(path)
    s = str(p)
    return is_path_within(p, LIVE_GE_ROOT) or str(LIVE_GE_ROOT).startswith(s)


def looks_like_live_root_write(text):
    write_patterns = [
        r"\b(cp|mv|rsync|ditto|install|touch|mkdir|tee)\b",
        r">\s*/Users/duhokim/NebulaMind/NebulaMind-origin-main-live",
        r"\b(write_text|write_bytes|open\s*\([^\n]*(?:'|\")\s*[wa+])",
        r"\b(apply_patch)\b",
    ]
    return any(re.search(pat, text, flags=re.IGNORECASE | re.DOTALL) for pat in write_patterns)


def classify_tail(text):
    tail = text[-6000:]
    context = active_permission_context(tail)
    permission = bool(context) and looks_like_permission_prompt(context)
    paths = extract_paths(context)
    forbidden = contains_forbidden(context)
    path_results = [{"path": p, "allowed": path_allowed(p)} for p in paths]
    disallowed_paths = [p for p in path_results if not p["allowed"]]
    live_root_paths = [p for p in path_results if is_live_root_path(p["path"])]
    selected_broad = selected_always_allow(context)
    read_onlyish = is_read_only_commandish(context)
    safe = False
    reason = "no permission prompt detected"
    if permission:
        if forbidden and is_forbidden_string_scan_context(context, forbidden):
            safe = True
            reason = "read-only safety scan mentioning forbidden strings literally"
        elif forbidden:
            reason = "forbidden pattern: {}".format(forbidden)
        elif selected_broad:
            reason = "cursor appears to be on broad/always-allow option"
        elif live_root_paths and (not read_onlyish or looks_like_live_root_write(context)):
            reason = "live-root path requires read-only inspection; write/copy prompts need explicit user approval"
        elif disallowed_paths:
            reason = "path outside bounded docs/static allowlist: {}".format(
                ", ".join(p["path"] for p in disallowed_paths[:3]))
        elif is_private_dashboard_context(context):
            safe = True
            reason = "private ge-autopilot dashboard read-only/local-tailnet check"
        elif paths:
            safe = True
            reason = "all referenced paths are inside bounded docs/static allowlist"
        elif read_onlyish:
            safe = True
            reason = "read-only local command pattern and no disallowed paths"
        else:
            reason = "permission prompt shape not classifiable as safe"
    return {
        "permission_prompt": permission,
        "safe_to_approve": safe,
        "reason": reason,
        "referenced_paths": path_results,
        "forbidden_pattern": forbidden,
        "selected_broad_allow": selected_broad,
        "read_onlyish": read_onlyish,
    }


def paste_prompt(pane_id, prompt):
    # Keep this operation explicit and reversible: clear composer, paste, submit.
    tmux(["send-keys", "-t", pane_id, "C-u"], timeout=5)
    tmux(["load-buffer", "-"], input_text=prompt, check=True, timeout=10)
    tmux(["paste-buffer", "-t", pane_id], check=True, timeout=10)
    tmux(["send-keys", "-t", pane_id, "Enter"], check=True, timeout=5)


def approve_safe_prompts(panes, dry_run=False):
    actions = []
    for pane in panes:
        pane_id = pane["pane_id"]
        # Copy/view modes may be an operator reading pane history. Never
        # dismiss that mode or send approval keystrokes into it automatically.
        if pane.get("in_mode"):
            continue
        classification = pane.get("classification") or classify_tail(pane.get("tail", ""))
        if classification.get("permission_prompt") and classification.get("safe_to_approve"):
            if not dry_run:
                tmux(["send-keys", "-t", pane_id, "Enter"], timeout=5)
            action = {
                "pane_id": pane_id,
                "role": pane["role"],
                "action": "approve-safe-permission",
                "dry_run": dry_run,
                "reason": classification.get("reason"),
            }
            actions.append(action)
            append_event(action)
    return actions


def method_prompt(method, order_path, marker):
    return """GE AUTOPILOT PHASE 1 DISPATCH — {marker} — {method_id}

Read this order now and act as the autonomous Method Hwao controller for {method_name}:
{order_path}

Scope and permissions:
- BOUNDED DOCS/STATIC ONLY.
- You may coordinate your method-local Lana/Goru/Kun/Tori panes by tmux prompts.
- Ruthless useful-work rule: keep Goru/Antigravity busy by default with bounded read-only mechanical audits, counts, inventories, status-schema checks, marker checks, and stale-blocker analysis whenever the method has safe local work available. Do not leave Goru idle just because a high-level verdict is pending; give Goru a small verifiable report packet while Lana/Hwao reason.
- Gemini-web / Deep Research quality sidecar: if this is a research-topic (RT) quality task and outside literature/status-map review would materially improve the page, write a request packet under {master}/gemini-web-deep-research/requests/ using the protocol at {master}/gemini-web-deep-research/RT_GEMINI_WEB_DEEP_RESEARCH_PROTOCOL.md, then wait for a Tori/Hwao-verified output under the matching outputs/integrations dirs. Do not open Gemini-web, run browser automation, create API/GCP/billing/OAuth routes, or treat web output as proof. Consume only verified integration packets as advisory source-discovery/status-map input.
- You may write method-local briefs, receipts, ledgers, verdicts, and static preview artifacts only under:
  - {handoff}
  - {public}/same-format-rebuild/ or another explicitly order-named docs/static subdir under this method root
- You may run read-only local checks over the repo and these artifacts.
- You must chain dependencies: author/content first, preview/build second, Goru checks after artifacts exist, Tori receipt after fresh checks, Hwao verdict last.
- Do not burn tokens for filler: every Goru packet must produce a useful local artifact with exact paths, counts, PASS/WARN/FAIL, and the order marker.
- If a dependency is missing, wait/poll; do not produce stale blocker reports unless the order asks for a blocker.
- If you see a permission prompt, only approve one-time docs/static/read-only work in the allowed roots; otherwise stop and write a blocker.

Hard stop gates still closed unless the user separately approves them:
Product DB/SQL and pane-initiated SQL, /api/pages, page_versions/live wiki publish, deploy/restart, git commit/push/merge, cockpit/global/shared-parent changes, cloud/GCP/API/billing/OAuth/token/secrets, browser automation, cron, Method3 P3 binding. The controller's append-only local outcome ledger under .hermes is the only DB exception.

Write a method-local progress/status file under {handoff}/autopilot/ when you dispatch lanes and again when complete. Include the marker {marker}. Stop after the method verdict or a hard-stop blocker.
""".format(
        marker=marker,
        method_id=method["id"],
        method_name=method["name"],
        order_path=str(Path(order_path).resolve()),
        handoff=str(method["handoff"]),
        public=str(method["public"]),
        master=str(MASTER_ROOT),
    )


def gemini_app_route_line():
    """Live Gemini app-lane routing advisory for Hwao. Never breaks a dispatch:
    any failure degrades to an honest 'unknown' rather than raising."""
    try:
        from datetime import datetime, timezone
        from gemini_app_usage import load_reading, route_line
        return route_line(load_reading(), datetime.now(timezone.utc))
    except Exception:
        return "GEMINI APP LANE: unknown — usage tool unavailable; do not assume app-lane headroom."


def director_prompt(order_path, marker):
    method_lines = []
    for method in METHODS:
        method_lines.append("- {id}: {handoff} / {public}".format(id=method["id"], handoff=method["handoff"], public=method["public"]))
    return """GE AUTOPILOT PHASE 1 DIRECTOR DISPATCH — {marker}

Read this order and supervise the method teams autonomously inside the bounded docs/static no-apply scope:
{order_path}

Method roots:
{method_lines}

Your role:
- Hwao-director supervises; do not become a solo content author unless the order explicitly assigns that.
- Let method-local Hwao controllers dispatch their own Lana/Goru/Kun/Tori lanes.
- Ruthless useful-work rule: while hard gates stay closed, keep Gemini/Goru lanes doing useful bounded local work instead of idling. Prefer Goru for mechanical counts, file maps, marker checks, stale-blocker audits, dashboard/status schema checks, and safety-surface scans; require each Goru run to write one verifiable report artifact. Do not fake or manually edit usage gauges.
- Gemini app-lane advisory (operator-confirmed capture of gemini.google.com/usage; a different pool from the Antigravity/Goru quota — spending one does not draw down the other): {gemini_app_route} When this reads 'burn', prefer routing wide/cheap/long-context bulk to the Gemini app lane; when 'reserve'/'wait'/'unknown', do not lean on it. Advisory and only as fresh as the last capture — never fabricate or edit the number to change the lane.
- Gemini-web / Deep Research sidecar is available for RT quality only via the supervised protocol at {master}/gemini-web-deep-research/RT_GEMINI_WEB_DEEP_RESEARCH_PROTOCOL.md. If a method needs deeper literature/status-map review, have it write a request packet; Tori/Hwao may run one supervised web packet and return a verified integration artifact. Method panes must not browser-automate or configure API/GCP/billing/OAuth, and Gemini-web output remains advisory until source-verified.
- Watch for stale blockers, missing dependencies, and unsafe gates.
- Write director progress under {master}/autopilot/ and a final roll-up only after method verdicts/receipts land.
- If a pane is stuck on a safe docs/static/read-only permission prompt, allow the autopilot/Tori controller to resolve it; do not duplicate keystrokes.

Hard stop gates remain closed: product DB/SQL and pane-initiated SQL, /api/pages, page_versions/live wiki publish, deploy/restart, git, cockpit/global/shared-parent, cloud/GCP/API/billing/OAuth/token/secrets, browser automation, cron, Method3 P3 binding. The controller's append-only local outcome ledger under .hermes is the only DB exception.

Stop after final roll-up or hard-stop blocker. Marker: {marker}.
""".format(
        marker=marker,
        order_path=str(Path(order_path).resolve()),
        method_lines="\n".join(method_lines),
        master=str(MASTER_ROOT),
        gemini_app_route=gemini_app_route_line(),
    )


def dispatch_order(order_path, force=False, dry_run=False):
    order_path = Path(order_path).resolve()
    marker = order_marker(order_path)
    digest = order_digest(order_path)
    state = read_state()
    state.setdefault("orders", {})
    order_state = state["orders"].setdefault(marker, {"digest": digest, "dispatches": {}, "created_at": utc_now()})
    order_state["digest"] = digest
    dispatches = order_state.setdefault("dispatches", {})
    actions = []

    director_pane = find_pane_by_role(DIRECTOR["hwao_role"])
    if director_pane:
        key = "director:{}".format(DIRECTOR["hwao_role"])
        if force or key not in dispatches:
            prompt = director_prompt(order_path, marker)
            if not dry_run:
                paste_prompt(director_pane["pane_id"], prompt)
            dispatches[key] = {"ts": utc_now(), "pane_id": director_pane["pane_id"], "dry_run": dry_run}
            actions.append({"action": "dispatch", "role": DIRECTOR["hwao_role"], "pane_id": director_pane["pane_id"], "dry_run": dry_run})
    else:
        actions.append({"action": "missing-pane", "role": DIRECTOR["hwao_role"]})

    for method in METHODS:
        pane = find_pane_by_role(method["hwao_role"])
        if not pane:
            actions.append({"action": "missing-pane", "role": method["hwao_role"], "method": method["id"]})
            continue
        key = "{}:{}".format(method["id"], method["hwao_role"])
        if force or key not in dispatches:
            prompt = method_prompt(method, order_path, marker)
            if not dry_run:
                paste_prompt(pane["pane_id"], prompt)
            dispatches[key] = {"ts": utc_now(), "pane_id": pane["pane_id"], "dry_run": dry_run}
            actions.append({"action": "dispatch", "role": method["hwao_role"], "method": method["id"], "pane_id": pane["pane_id"], "dry_run": dry_run})

    order_state["updated_at"] = utc_now()
    if not dry_run:
        write_json(STATE_PATH, state)
        append_event({"event": "dispatch-order", "marker": marker, "actions": actions})
    return marker, actions


def expected_final_rollup_path(marker, order_path=None):
    if order_path:
        try:
            text = Path(order_path).read_text(errors="replace")
            matches = re.findall(r"/Users/duhokim/NebulaMind/NebulaMind/\.hermes/handoffs/galaxy-evolution/mastermind/autopilot/[^\s`'\")]+\.md", text)
            final_matches = [m for m in matches if "FINAL" in Path(m).name]
            if final_matches:
                return Path(final_matches[-1])
        except Exception:
            pass
    return MASTER_ROOT / "autopilot" / "{}_FINAL_WIKI_PAGES_ROLLUP.md".format(marker)


def continuation_worker_role(role):
    role = role or ""
    if role.startswith("Tori"):
        return False
    if "live-view" in role.lower():
        return False
    return role.startswith("Hwao") or role.startswith("Lana") or role.startswith("Goru") or role.startswith("Kun")


def pane_by_role_from_status(status, role):
    for pane in status.get("panes", []):
        if pane.get("role") == role:
            return pane
    return None


def order_is_complete(marker, order_path=None):
    rollup = expected_final_rollup_path(marker, order_path=order_path)
    if not rollup.exists():
        return False
    try:
        text = rollup.read_text(errors="replace")
    except Exception:
        return False
    lower = text.lower()
    terminal_status = any(item in lower for item in ("status: complete", "status: ready_for_user_approval", "status: hard_blocked", "ratified"))
    return marker.lower() in lower and terminal_status and "wiki" in lower


def continuation_prompt(order_path, marker, rollup_path, method=None):
    if method:
        lane = "Method {id} / {name}".format(id=method["id"].replace("method", ""), name=method["name"])
        roots = "handoff root: {handoff}\nstatic page root: {public}".format(handoff=method["handoff"], public=method["public"])
        focus = "Continue this method lane to a complete static wiki-page artifact, then make Goru verify exact files/counts/markers and report back to Hwao-director."
    else:
        lane = "Hwao director"
        roots = "method roots are listed in the order packet"
        focus = "Coordinate Method1/2/3 until the static wiki pages are complete and verified, not merely until one packet finishes."
    return """GE AUTOPILOT IDLE CONTINUATION — {marker}

The user corrected the autopilot: do not park after one assigned packet. Keep going until the complete static wiki pages are done, verified, and rolled up.

Order packet:
{order_path}

Lane:
{lane}
{roots}

Immediate instruction:
- {focus}
- If your pane is idle, resume now: inspect current artifacts, identify the next missing implementation/verification step, and dispatch Lana/Goru/Kun/Tori lanes as needed.
- Keep Gemini/Goru doing bounded mechanical work whenever useful: file maps, section counts, marker checks, link/static safety checks, same-format checks, stale-blocker checks, and final verification receipts.
- For RT quality gaps that require outside literature/status-map review, request the Gemini-web Deep Research sidecar via {master}/gemini-web-deep-research/RT_GEMINI_WEB_DEEP_RESEARCH_PROTOCOL.md; do not open browsers or API/cloud routes from autopilot panes, and consume only Tori/Hwao-verified integration artifacts.
- Stop only for a hard-gate blocker or after the final artifact exists at the exact path below.

Required final artifact path:
{rollup_path}

Hard gates still closed: product DB/SQL, /api/pages, page_versions/live wiki publish, deploy/restart, git, public Baseline cockpit/global mutation, cloud/GCP/API/billing/OAuth/token/secrets, browser automation, cron. Static docs/page artifacts and .hermes handoff receipts are allowed.

Marker: {marker}
Continuation marker: {continuation_marker}
""".format(
        marker=marker,
        order_path=str(Path(order_path).resolve()),
        lane=lane,
        roots=roots,
        focus=focus,
        rollup_path=str(rollup_path),
        continuation_marker=IDLE_CONTINUATION_MARKER,
        master=str(MASTER_ROOT),
    )


def maybe_idle_continue_order(order_path, status, cooldown_seconds=DEFAULT_IDLE_NUDGE_SECONDS):
    marker = order_marker(order_path)
    state = read_state()
    orders = state.setdefault("orders", {})
    order_state = orders.setdefault(marker, {"digest": order_digest(order_path), "dispatches": {}, "created_at": utc_now()})
    order_state["order_path"] = str(Path(order_path).resolve())
    rollup_path = expected_final_rollup_path(marker, order_path=order_path)
    order_state["expected_final_rollup_path"] = str(rollup_path)
    if order_is_complete(marker, order_path=order_path):
        if not order_state.get("completed_at"):
            order_state["completed_at"] = utc_now()
            write_json(STATE_PATH, state)
            append_event({"event": "order-complete", "marker": marker, "rollup_path": str(rollup_path)})
        return []
    if status.get("blockers"):
        return []
    active_workers = [p for p in status.get("panes", []) if continuation_worker_role(p.get("role")) and p.get("active")]
    if active_workers:
        return []
    last_nudge = parse_utc(order_state.get("last_idle_nudge_at"))
    elapsed_since_nudge = seconds_since(last_nudge) if last_nudge else None
    if elapsed_since_nudge is not None and elapsed_since_nudge < int(cooldown_seconds):
        return []
    actions = []
    rollup_path.parent.mkdir(parents=True, exist_ok=True)
    director = pane_by_role_from_status(status, DIRECTOR["hwao_role"])
    if director and not director.get("dead") and not director.get("active"):
        paste_prompt(director["pane_id"], continuation_prompt(order_path, marker, rollup_path))
        actions.append({"action": "idle-continuation-nudge", "role": DIRECTOR["hwao_role"], "pane_id": director["pane_id"]})
    for method in METHODS:
        pane = pane_by_role_from_status(status, method["hwao_role"])
        if pane and not pane.get("dead") and not pane.get("active"):
            paste_prompt(pane["pane_id"], continuation_prompt(order_path, marker, rollup_path, method=method))
            actions.append({"action": "idle-continuation-nudge", "role": method["hwao_role"], "method": method["id"], "pane_id": pane["pane_id"]})
    if actions:
        order_state["last_idle_nudge_at"] = utc_now()
        order_state["idle_nudge_count"] = int(order_state.get("idle_nudge_count") or 0) + 1
        write_json(STATE_PATH, state)
        append_event({"event": "idle-continuation", "marker": marker, "actions": actions, "rollup_path": str(rollup_path)})
    return actions


def board_status(include_tail=False, write=True, tail_lines=80):
    targets = []
    for target in all_board_targets():
        targets.append({"target": target, "exists": target_exists(target)})
    panes = collect_panes(include_tail=include_tail, tail_lines=tail_lines)
    blockers = []
    for pane in panes:
        cls = pane.get("classification")
        if cls and cls.get("permission_prompt"):
            blockers.append(
                {
                    "pane_id": pane["pane_id"],
                    "role": pane["role"],
                    "safe_to_approve": cls.get("safe_to_approve"),
                    "reason": cls.get("reason"),
                }
            )
    status_ts = utc_now()
    state = read_state()
    status = {
        "ts": status_ts,
        "repo": str(REPO),
        "targets": targets,
        "panes": panes,
        "blockers": blockers,
        "status_path": str(STATUS_PATH),
        "state_path": str(STATE_PATH),
        "run_estimates": build_run_estimates(state, status_ts, blockers),
        "local_outcome_ledger": outcome_ledger_summary(),
        "phase": "phase1-bounded-controller",
        "hard_gates_closed": [
            "product DB/SQL and pane-initiated SQL",
            "/api/pages/page_versions/live wiki publish",
            "deploy/restart",
            "git commit/push/merge",
            "cockpit/global/shared-parent",
            "cloud/GCP/API/billing/OAuth/token/secrets",
            "browser automation",
            "cron",
        ],
    }
    if write:
        record_status_snapshot(status)
        status["local_outcome_ledger"] = outcome_ledger_summary()
        write_json(STATUS_PATH, status)
    return status


def ensure_board():
    actions = []
    launchers = [
        [str(LOCAL_BIN / "galaxy-evolution-mastermind"), "--repair-only"],
        [str(LOCAL_BIN / "quintet-method-mesh"), "--repair-only", "1"],
        [str(LOCAL_BIN / "quintet-method-mesh"), "--repair-only", "2"],
        [str(LOCAL_BIN / "quintet-method-mesh"), "--repair-only", "3"],
    ]
    for cmd in launchers:
        if not Path(cmd[0]).exists():
            actions.append({"cmd": cmd, "ok": False, "error": "launcher missing"})
            continue
        proc = run_cmd(cmd, timeout=60)
        actions.append({"cmd": cmd, "ok": proc.returncode == 0, "stdout": proc.stdout[-1200:], "stderr": proc.stderr[-1200:]})
    append_event({"event": "ensure-board", "actions": actions})
    return actions


def doctor(args):
    checks = []
    checks.append({"name": "repo", "path": str(REPO), "ok": REPO.exists()})
    checks.append({"name": "tmux", "path": TMUX, "ok": Path(TMUX).exists()})
    for name in ("galaxy-evolution-mastermind", "quintet-method-mesh", "quintet-method"):
        p = LOCAL_BIN / name
        checks.append({"name": name, "path": str(p), "ok": p.exists() and os.access(str(p), os.X_OK)})
    for target in all_board_targets():
        checks.append({"name": "tmux-target", "target": target, "ok": target_exists(target)})
    checks.append({"name": "master-root", "path": str(MASTER_ROOT), "ok": MASTER_ROOT.exists()})
    if args.json:
        print(json.dumps({"checks": checks, "ok": all(c["ok"] for c in checks)}, indent=2, sort_keys=True))
    else:
        print("Galaxy Evolution autopilot doctor")
        for c in checks:
            label = c.get("target") or c.get("path") or ""
            print("{} {:28s} {}".format("OK " if c["ok"] else "MISS", c["name"], label))
        print("overall: {}".format("OK" if all(c["ok"] for c in checks) else "ISSUES"))
    return 0 if all(c["ok"] for c in checks) else 1


def print_status(status, as_json=False):
    if as_json:
        print(json.dumps(status, indent=2, sort_keys=True))
        return
    print("Galaxy Evolution autopilot status @ {}".format(status["ts"]))
    for t in status["targets"]:
        print("{} {}".format("OK " if t["exists"] else "MISS", t["target"]))
    print("panes: {}".format(len(status["panes"])))
    for pane in status["panes"]:
        flags = []
        if pane.get("active"):
            flags.append("active")
        if pane.get("in_mode"):
            flags.append("copy-mode")
        if pane.get("dead"):
            flags.append("dead")
        cls = pane.get("classification") or {}
        if cls.get("permission_prompt"):
            flags.append("perm:{}".format("safe" if cls.get("safe_to_approve") else "review"))
        print("- {pane_id:>4} {role:<18} {cmd:<12} {flags}".format(pane_id=pane["pane_id"], role=pane["role"][:18], cmd=pane["current_command"][:12], flags=",".join(flags)))
    if status["blockers"]:
        print("blockers/prompts:")
        for b in status["blockers"]:
            print("- {pane_id} {role}: safe={safe} {reason}".format(pane_id=b["pane_id"], role=b["role"], safe=b["safe_to_approve"], reason=b["reason"]))
    print("status file: {}".format(status["status_path"]))


def cmd_status(args):
    status = board_status(include_tail=args.tail, write=not args.no_write, tail_lines=args.tail_lines)
    if args.auto_approve_safe:
        actions = approve_safe_prompts(status["panes"], dry_run=args.dry_run)
        status["actions"] = actions
        if not args.no_write:
            write_json(STATUS_PATH, status)
    print_status(status, as_json=args.json)
    return 0


def cmd_dispatch(args):
    if args.ensure:
        ensure_board()
    marker, actions = dispatch_order(args.order, force=args.force, dry_run=args.dry_run)
    print(json.dumps({"marker": marker, "actions": actions, "dry_run": args.dry_run}, indent=2, sort_keys=True))
    return 0


def cmd_run(args):
    if args.ensure:
        ensure_board()
    marker, actions = dispatch_order(args.order, force=args.force, dry_run=args.dry_run)
    status = board_status(include_tail=True, write=not args.dry_run, tail_lines=args.tail_lines)
    approve_actions = []
    if args.auto_approve_safe:
        approve_actions = approve_safe_prompts(status["panes"], dry_run=args.dry_run)
    result = {"marker": marker, "dispatch_actions": actions, "approve_actions": approve_actions, "status_path": str(STATUS_PATH), "dry_run": args.dry_run}
    print(json.dumps(result, indent=2, sort_keys=True))
    return 0


def cmd_watch(args):
    if args.order:
        dispatch_order(args.order, force=args.force_dispatch, dry_run=False)
    limit = args.iterations
    count = 0
    while True:
        status = board_status(include_tail=True, write=True, tail_lines=args.tail_lines)
        actions = []
        if args.auto_approve_safe:
            actions = approve_safe_prompts(status["panes"], dry_run=False)
        continuation_actions = []
        if args.order and args.idle_continuation:
            continuation_actions = maybe_idle_continue_order(args.order, status, cooldown_seconds=args.idle_nudge_seconds)
        append_event({"event": "watch-tick", "blockers": status["blockers"], "actions": actions, "continuation_actions": continuation_actions})
        if args.print_ticks:
            print(json.dumps({"ts": utc_now(), "blockers": status["blockers"], "actions": actions, "continuation_actions": continuation_actions}, sort_keys=True), flush=True)
        count += 1
        if limit and count >= limit:
            break
        time.sleep(args.interval)
    return 0


def cmd_start(args):
    if tmux(["has-session", "-t", AUTOPILOT_SESSION], timeout=5).returncode == 0 and not args.force:
        print("autopilot session already exists: {}".format(AUTOPILOT_SESSION), file=sys.stderr)
        return 2
    if args.force:
        tmux(["kill-session", "-t", AUTOPILOT_SESSION], timeout=5)
    cmd = [sys.executable, str(SCRIPT_PATH), "watch", "--auto-approve-safe", "--print-ticks", "--interval", str(args.interval)]
    if args.idle_continuation:
        cmd.append("--idle-continuation")
        cmd.extend(["--idle-nudge-seconds", str(args.idle_nudge_seconds)])
    if args.order:
        cmd.extend(["--order", str(Path(args.order).resolve())])
    if args.ensure:
        ensure_board()
    shell_cmd = " ".join(shlex.quote(x) for x in cmd)
    proc = tmux(["new-session", "-d", "-s", AUTOPILOT_SESSION, "-c", str(REPO), shell_cmd], timeout=10)
    if proc.returncode != 0:
        print(proc.stderr, file=sys.stderr)
        return proc.returncode
    append_event({"event": "start", "session": AUTOPILOT_SESSION, "cmd": cmd})
    print("started {}: {}".format(AUTOPILOT_SESSION, shell_cmd))
    return 0


def cmd_stop(args):
    proc = tmux(["kill-session", "-t", AUTOPILOT_SESSION], timeout=10)
    if proc.returncode == 0:
        append_event({"event": "stop", "session": AUTOPILOT_SESSION})
        print("stopped {}".format(AUTOPILOT_SESSION))
        return 0
    print("autopilot session not running: {}".format(AUTOPILOT_SESSION))
    return 0


def cmd_tail(args):
    if tmux(["has-session", "-t", AUTOPILOT_SESSION], timeout=5).returncode == 0:
        proc = tmux(["capture-pane", "-J", "-pt", AUTOPILOT_SESSION + ":0", "-S", "-{}".format(args.lines)], timeout=10)
        print(proc.stdout)
        return proc.returncode
    if LOG_PATH.exists():
        lines = LOG_PATH.read_text().splitlines()
        print("\n".join(lines[-args.lines:]))
        return 0
    print("no autopilot tmux session or log found")
    return 1


def cmd_classify(args):
    if args.file:
        text = Path(args.file).read_text(errors="replace")
    else:
        text = sys.stdin.read()
    print(json.dumps(classify_tail(text), indent=2, sort_keys=True))
    return 0


def cmd_ledger_summary(args):
    summary = outcome_ledger_summary()
    if args.json:
        print(json.dumps(summary, indent=2, sort_keys=True))
        return 0
    print("Galaxy Evolution autopilot local outcome ledger")
    print("marker: {}".format(summary.get("marker")))
    print("path: {}".format(summary.get("path")))
    print("scope: {}".format(summary.get("scope")))
    print("product DB writes enabled: {}".format(summary.get("product_db_writes_enabled")))
    print("events: {}".format(summary.get("events_total", 0)))
    print("status snapshots: {}".format(summary.get("snapshots_total", 0)))
    latest = summary.get("latest_status") or {}
    if latest:
        print("latest status: {ts} blockers={blockers} targets={targets_ok}/{targets_total} panes={panes}".format(**latest))
    if summary.get("error"):
        print("error: {}".format(summary["error"]))
        return 1
    return 0


def cmd_self_test(args):
    safe_text = "Bash command\npython3 /Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/check.py\n⎿  Waiting…"
    safe = classify_tail(safe_text)
    assert safe["permission_prompt"] and safe["safe_to_approve"], safe
    unsafe_text = "Bash command\npython3 -c 'import requests; requests.post(\"/api/pages\")'\n⎿  Waiting…"
    unsafe = classify_tail(unsafe_text)
    assert unsafe["permission_prompt"] and not unsafe["safe_to_approve"], unsafe
    db_text = "Bash command\nsqlite3 /tmp/prod.db 'UPDATE claims SET status=\"accepted\"'\n⎿  Waiting…"
    db = classify_tail(db_text)
    assert db["permission_prompt"] and not db["safe_to_approve"], db
    outside_text = "Create(/Users/duhokim/NebulaMind/NebulaMind/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/source-first-paper-adjudication/wiki-page.html)\n⎿  Waiting…"
    outside = classify_tail(outside_text)
    assert outside["permission_prompt"] and not outside["safe_to_approve"], outside
    sample_runs = build_run_estimates(
        {
            "orders": {
                "SELF_TEST_ORDER": {
                    "created_at": "2026-07-07T00:00:00Z",
                    "dispatches": {"director:Hwao-director": {"ts": "2026-07-07T00:00:00Z", "pane_id": "%1"}},
                }
            }
        },
        "2026-07-07T01:00:00Z",
        [],
    )
    assert sample_runs["marker"] == RUN_TIME_ESTIMATE_MARKER, sample_runs
    assert sample_runs["runs"][0]["elapsed_seconds"] == 3600, sample_runs
    assert sample_runs["runs"][0]["state"] == "partial-dispatch", sample_runs
    m = order_marker_from_text_for_test("Marker: `AUTONOMOUS_SAME_FORMAT_REPAIR_ORDER_20260707T074231Z`\n")
    assert m == "AUTONOMOUS_SAME_FORMAT_REPAIR_ORDER_20260707T074231Z", m
    print("self-test: PASS")
    return 0


def order_marker_from_text_for_test(text):
    tmp = MASTER_ROOT / ".autopilot-self-test-order.md"
    tmp.parent.mkdir(parents=True, exist_ok=True)
    old = None
    if tmp.exists():
        old = tmp.read_text()
    tmp.write_text(text)
    try:
        return order_marker(tmp)
    finally:
        if old is None:
            try:
                tmp.unlink()
            except OSError:
                pass
        else:
            tmp.write_text(old)


def build_parser():
    parser = argparse.ArgumentParser(description="Bounded Phase-1 controller for Galaxy Evolution method board")
    sub = parser.add_subparsers(dest="cmd", required=True)

    p = sub.add_parser("doctor", help="Check launchers, tmux, sessions, roots")
    p.add_argument("--json", action="store_true")
    p.set_defaults(func=doctor)

    p = sub.add_parser("status", help="Write/print board status")
    p.add_argument("--json", action="store_true")
    p.add_argument("--tail", action="store_true", help="Capture pane tails and classify prompts")
    p.add_argument("--tail-lines", type=int, default=80)
    p.add_argument("--no-write", action="store_true")
    p.add_argument("--auto-approve-safe", action="store_true", help="Approve narrowly classified safe docs/static prompts")
    p.add_argument("--dry-run", action="store_true")
    p.set_defaults(func=cmd_status)

    p = sub.add_parser("dispatch", help="Dispatch an order once to director + method Hwao controllers")
    p.add_argument("order")
    p.add_argument("--ensure", action="store_true", help="Repair/create board panes before dispatch")
    p.add_argument("--force", action="store_true", help="Redispatch even if this order was already sent")
    p.add_argument("--dry-run", action="store_true")
    p.set_defaults(func=cmd_dispatch)

    p = sub.add_parser("run", help="Ensure/dispatch once, write status, optionally approve safe prompts")
    p.add_argument("order")
    p.add_argument("--ensure", action="store_true")
    p.add_argument("--force", action="store_true")
    p.add_argument("--auto-approve-safe", action="store_true")
    p.add_argument("--tail-lines", type=int, default=80)
    p.add_argument("--dry-run", action="store_true")
    p.set_defaults(func=cmd_run)

    p = sub.add_parser("watch", help="Foreground watch loop for status + safe permission prompts")
    p.add_argument("--order")
    p.add_argument("--force-dispatch", action="store_true")
    p.add_argument("--auto-approve-safe", action="store_true")
    p.add_argument("--idle-continuation", action="store_true", help="When an active order is unfinished and worker panes go idle, nudge Hwao lanes to continue")
    p.add_argument("--idle-nudge-seconds", type=int, default=DEFAULT_IDLE_NUDGE_SECONDS)
    p.add_argument("--interval", type=float, default=20.0)
    p.add_argument("--iterations", type=int, default=0, help="0 = forever")
    p.add_argument("--tail-lines", type=int, default=100)
    p.add_argument("--print-ticks", action="store_true")
    p.set_defaults(func=cmd_watch)

    p = sub.add_parser("start", help="Start background tmux autopilot watcher")
    p.add_argument("--order")
    p.add_argument("--ensure", action="store_true")
    p.add_argument("--interval", type=float, default=20.0)
    p.add_argument("--idle-continuation", action="store_true", help="Keep nudging idle Hwao lanes for the active order until its final roll-up exists")
    p.add_argument("--idle-nudge-seconds", type=int, default=DEFAULT_IDLE_NUDGE_SECONDS)
    p.add_argument("--force", action="store_true")
    p.set_defaults(func=cmd_start)

    p = sub.add_parser("stop", help="Stop background tmux autopilot watcher")
    p.set_defaults(func=cmd_stop)

    p = sub.add_parser("tail", help="Show background autopilot pane/log tail")
    p.add_argument("--lines", type=int, default=80)
    p.set_defaults(func=cmd_tail)

    p = sub.add_parser("classify", help="Classify a permission prompt from stdin or file")
    p.add_argument("--file")
    p.set_defaults(func=cmd_classify)

    p = sub.add_parser("ledger-summary", help="Show the local append-only outcome DB summary")
    p.add_argument("--json", action="store_true")
    p.set_defaults(func=cmd_ledger_summary)

    p = sub.add_parser("self-test", help="Run local classifier/state smoke tests")
    p.set_defaults(func=cmd_self_test)

    return parser


def main(argv=None):
    parser = build_parser()
    args = parser.parse_args(argv)
    return args.func(args)


if __name__ == "__main__":
    sys.exit(main())
