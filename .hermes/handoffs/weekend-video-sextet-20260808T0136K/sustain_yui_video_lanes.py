#!/usr/bin/env python3
"""Bounded local-only sustainer for the weekend Yui video lanes.

It only inspects and seeds the six dedicated tmux sessions and writes receipts
inside this handoff root. It never approves permissions, invokes Git, publishes,
or touches public/shared video assets.
"""

from __future__ import annotations

import json
import os
import subprocess
import time
from datetime import datetime, timezone, timedelta
from pathlib import Path

ROOT = Path("/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/weekend-video-sextet-20260808T0136K")
TMUX = Path("/opt/homebrew/bin/tmux")
KST = timezone(timedelta(hours=9))
DEADLINE = datetime(2026, 8, 10, 7, 0, 0, tzinfo=KST)
INTERVAL_SECONDS = 120
MIN_RESEED_SECONDS = 600
STOP_FILE = ROOT / "STOP"
STATUS_PATH = ROOT / "sustainer-status.json"
LEDGER_PATH = ROOT / "SUSTAINER_LEDGER.jsonl"

LANES = {
    "brightend": "yui-video-brightend",
    "mzr-anchor": "yui-video-mzr-anchor",
    "fesc": "yui-video-fesc",
    "mzr-census": "yui-video-mzr-census",
    "spin": "yui-video-spin",
    # "integration" REMOVED 2026-08-08 02:07 KST. That session is directed by Hwao under
    # integrator/DELEGATION.md, per Duho's continuity handoff ("delegate exactly one isolated-copy
    # writer seat to yui-video-integration"). Leaving it here meant TWO writers pasting different
    # briefs and different output dirs into one composer every ~10 min — which derails whatever the
    # seat is mid-way through. The sustainer keeps the five PAPER lanes alive; the integrator seat
    # has exactly one director.
}

OUTPUT_DIRS = {
    "brightend": "lane-c41-uvlf/worker-yui",
    "mzr-anchor": "lane-c41-mzr/worker-yui",
    "fesc": "lane-fesc-zsweep/worker-yui",
    "mzr-census": "lane-mzr-census/worker-yui",
    "spin": "lane-spin-parity/worker-yui",
    "integration": "integrator",
}


def now() -> datetime:
    return datetime.now(KST)


def run_tmux(*args: str) -> subprocess.CompletedProcess[str]:
    env = os.environ.copy()
    env.pop("TMUX", None)
    return subprocess.run(
        [str(TMUX), *args],
        text=True,
        capture_output=True,
        timeout=20,
        env=env,
        check=False,
    )


def atomic_json(path: Path, value: dict) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    tmp = path.with_suffix(path.suffix + ".tmp")
    tmp.write_text(json.dumps(value, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    os.replace(tmp, path)


def append_event(value: dict) -> None:
    with LEDGER_PATH.open("a", encoding="utf-8") as fh:
        fh.write(json.dumps(value, sort_keys=True) + "\n")


def inspect_lane(lane: str, session: str) -> dict:
    output_dir = ROOT / OUTPUT_DIRS[lane]
    info = {
        "lane": lane,
        "session": session,
        "exists": False,
        "dead": None,
        "idle": False,
        "permission_prompt": False,
        "output_dir": str(output_dir),
        "paused": (output_dir / "PAUSE").exists(),
        "lane_status": None,
    }

    has = run_tmux("has-session", "-t", session)
    if has.returncode != 0:
        return info
    info["exists"] = True

    meta = run_tmux(
        "display-message", "-p", "-t", session,
        "#{pane_dead}|#{pane_current_command}|#{pane_title}",
    )
    if meta.returncode == 0:
        fields = meta.stdout.strip().split("|", 2)
        info["dead"] = fields[0] == "1"
        if len(fields) >= 2:
            info["command"] = fields[1]
        if len(fields) == 3:
            info["title"] = fields[2]

    cap = run_tmux("capture-pane", "-J", "-p", "-S", "-180", "-t", session)
    text = cap.stdout if cap.returncode == 0 else ""
    info["permission_prompt"] = (
        "Do you want to proceed?" in text
        or "Requesting permission for:" in text
        or "denied by user" in text[-2000:]
    )
    # A fresh input prompt after the most recent active-turn marker is idle.
    last_idle = max(
        text.rfind("yui ❯"),
        text.rfind("Welcome to Hermes Agent! Type your message"),
        text.rfind("\n❯"),  # Claude/Fable integration seat after Hwao delegation
    )
    last_active = max(
        text.rfind("msg=interrupt"),
        text.rfind("Initializing agent..."),
        text.rfind("Booping…"),
        text.rfind("Running…"),
        text.rfind("Orchestrating…"),
    )
    title = str(info.get("title", ""))
    title_is_spinner = bool(title and 0x2800 <= ord(title[0]) <= 0x28FF)
    if info.get("command") == "claude.exe":
        # Claude Code keeps its composer visible while thinking. Its tmux title,
        # unlike the composer glyph, reliably carries a Braille spinner while active.
        info["idle"] = bool(not title_is_spinner and not info["permission_prompt"] and not info["dead"])
    else:
        info["idle"] = bool(last_idle > last_active and not info["permission_prompt"] and not info["dead"])

    status_file = output_dir / "STATUS.json"
    if status_file.exists():
        try:
            info["lane_status"] = json.loads(status_file.read_text(encoding="utf-8"))
        except (OSError, json.JSONDecodeError) as exc:
            info["lane_status_error"] = type(exc).__name__
    return info


def blocked_status(value: object) -> bool:
    if not isinstance(value, dict):
        return False
    tokens = " ".join(str(value.get(k, "")) for k in ("phase", "state", "status", "verdict")).lower()
    if "blocked" not in tokens and "awaiting_hwao" not in tokens and "awaiting human" not in tokens:
        return False
    return not bool(value.get("recoverable_without_human", False))


def seed(lane: str, session: str, pass_number: int) -> bool:
    output_dir = ROOT / OUTPUT_DIRS[lane]
    if lane == "integration":
        task = (
            "Re-read integrator/DELEGATION.md, the current HWAO_WEEKEND_ORDER.md, integrator/requests/, and every "
            "lane-*/worker-yui/INTEGRATOR_REQUEST*, STATUS, and receipt now on disk. "
            "Continue integration pass {n}: reconcile only source-compatible findings, run fresh encoded-frame and machine QA on the latest isolated canary, "
            "make one evidence-backed correction when warranted, preserve failed candidates, update STATUS/INTEGRATION_LEDGER/receipt, and remain inside the integration directory."
        )
    else:
        task = (
            "Re-read the current HWAO_WEEKEND_ORDER.md if present and your BRIEF, STATUS, source freeze, latest candidate, frames, and receipt. "
            "Continue isolated deepening pass {n}: perform a fresh encoded-frame scientific-presentation audit, make the next evidence-backed visual/storyboard correction if safe, "
            "or deepen the exact blocker packet without inventing science. Preserve failed candidates; update STATUS and LANE_RECEIPT; stay only in your lane directory."
        )
    message = (
        task.format(n=pass_number)
        + f" Read COORDINATION_UPDATE.md and write only to {output_dir}. "
        + "Do not publish, touch shared/public assets, invoke TTS, use Git writes, or ask routine questions."
    )
    setbuf = run_tmux("set-buffer", "--", message)
    if setbuf.returncode != 0:
        return False
    pasted = run_tmux("paste-buffer", "-t", session)
    if pasted.returncode != 0:
        return False
    submitted = run_tmux("send-keys", "-t", session, "Enter")
    return submitted.returncode == 0


def main() -> int:
    ROOT.mkdir(parents=True, exist_ok=True)
    state = {
        lane: {"pass": 1, "last_seed_epoch": time.time(), "last_seed_kst": now().isoformat()}
        for lane in LANES
    }
    # Preserve reseed counters/timestamps across a supervised sustainer upgrade.
    if STATUS_PATH.exists():
        try:
            previous = json.loads(STATUS_PATH.read_text(encoding="utf-8")).get("lane_seed_state", {})
            for lane in LANES:
                old = previous.get(lane)
                if isinstance(old, dict) and {"pass", "last_seed_epoch", "last_seed_kst"} <= old.keys():
                    state[lane] = {
                        "pass": int(old["pass"]),
                        "last_seed_epoch": float(old["last_seed_epoch"]),
                        "last_seed_kst": str(old["last_seed_kst"]),
                    }
        except (OSError, ValueError, TypeError, json.JSONDecodeError):
            pass
    append_event({
        "event": "sustainer_started",
        "ts": now().isoformat(),
        "deadline": DEADLINE.isoformat(),
        "sessions": LANES,
        "output_dirs": OUTPUT_DIRS,
        "safety": "tmux_seed_and_handoff_receipts_only",
    })

    while now() < DEADLINE and not STOP_FILE.exists():
        observed = []
        events = []
        epoch = time.time()
        for lane, session in LANES.items():
            item = inspect_lane(lane, session)
            observed.append(item)
            if (
                item["exists"]
                and item["idle"]
                and not item["paused"]
                and not blocked_status(item.get("lane_status"))
                and epoch - state[lane]["last_seed_epoch"] >= MIN_RESEED_SECONDS
            ):
                next_pass = state[lane]["pass"] + 1
                ok = seed(lane, session, next_pass)
                event = {
                    "event": "lane_reseeded" if ok else "lane_reseed_failed",
                    "lane": lane,
                    "session": session,
                    "pass": next_pass,
                    "ts": now().isoformat(),
                }
                events.append(event)
                append_event(event)
                if ok:
                    state[lane] = {
                        "pass": next_pass,
                        "last_seed_epoch": epoch,
                        "last_seed_kst": event["ts"],
                    }

        snapshot = {
            "marker": "YUI_VIDEO_WEEKEND_SUSTAINER_V1",
            "state": "running",
            "ts": now().isoformat(),
            "deadline": DEADLINE.isoformat(),
            "stop_file": str(STOP_FILE),
            "interval_seconds": INTERVAL_SECONDS,
            "min_reseed_seconds": MIN_RESEED_SECONDS,
            "lane_seed_state": state,
            "lanes": observed,
            "events_this_tick": events,
            "hard_gates_closed": [
                "public/shared video replacement",
                "upload/publish/unlist/delete",
                "paperVideos.ts and cockpit",
                "DB/SQL and deploy/restart",
                "Git writes",
                "browser/billing/provider/config/secrets",
                "cron",
            ],
        }
        atomic_json(STATUS_PATH, snapshot)
        time.sleep(INTERVAL_SECONDS)

    final_state = "stopped_by_marker" if STOP_FILE.exists() else "window_ended"
    final = {
        "marker": "YUI_VIDEO_WEEKEND_SUSTAINER_V1",
        "state": final_state,
        "ts": now().isoformat(),
        "deadline": DEADLINE.isoformat(),
        "lane_seed_state": state,
    }
    atomic_json(STATUS_PATH, final)
    append_event({"event": final_state, "ts": final["ts"], "deadline": DEADLINE.isoformat()})
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
