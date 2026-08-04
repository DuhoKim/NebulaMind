#!/usr/bin/env python3
"""Wait for the current repair sprint, then run an additional couple-hour continuation.

This is local/artifact-only. It first records system-issue receipts for the
workflow fixes, then starts the patched LaTeX repair sprint using the latest
candidate from the previous repair run as its source.
"""
from __future__ import annotations

import datetime as dt
import json
import os
import subprocess
import sys
import time
from pathlib import Path
from typing import Any, Dict, Optional

REPO = Path("/Users/duhokim/NebulaMind/NebulaMind")
AUTO = REPO / ".hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot"
REPAIR_DIR = AUTO / "latex-publishability-repair"
OVERNIGHT_ROOT = AUTO / "overnight-critical-review/OVERNIGHT_PDF_REVIEW_WORKFLOW_SWARM_20260709T163102Z"
PREVIOUS_RUN_ROOT = Path(os.environ.get(
    "NEBULAMIND_PREVIOUS_LATEX_REPAIR_RUN_ROOT",
    str(REPAIR_DIR / "LATEX_PUBLISHABILITY_REPAIR_20260709T235447Z"),
))
PREVIOUS_PID = int(os.environ.get("NEBULAMIND_PREVIOUS_LATEX_REPAIR_PID", "87526"))
WAIT_MAX_SECONDS = int(os.environ.get("NEBULAMIND_CONTINUATION_WAIT_MAX_SECONDS", str(3 * 60 * 60)))
WAIT_POLL_SECONDS = int(os.environ.get("NEBULAMIND_CONTINUATION_WAIT_POLL_SECONDS", "30"))
RUN_ID = os.environ.get("NEBULAMIND_LATEX_REPAIR_CONTINUATION_RUN_ID") or "LATEX_PUBLISHABILITY_REPAIR_CONTINUATION_" + dt.datetime.now(dt.timezone.utc).strftime("%Y%m%dT%H%M%SZ")
RUN_ROOT = REPAIR_DIR / RUN_ID
PATCHED_REPAIR_SCRIPT = REPAIR_DIR / "run_couple_hour_latex_publishability_repair.py"
OVERNIGHT_SCRIPT = AUTO / "overnight-critical-review/run_overnight_pdf_and_workflow_swarm.py"
LINT_TOOL = REPO / "tools/ge_tex_publishability_lint.py"

SAFETY_LOCKS = [
    "local/artifact-only continuation",
    "wait for the existing repair sprint before starting the next repair sprint",
    "use copied candidate package only as repair source",
    "no public PDF replacement or public/live root edits",
    "no DB/API/wiki/page_versions/trust writes",
    "no deploy/restart",
    "no git commit/push/merge/rebase/history rewrite",
    "no cron creation/update/removal",
    "no billing/cloud/OAuth/API-key/account/credential actions",
    "no external manuscript submission",
]


def utc() -> str:
    return dt.datetime.now(dt.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def write(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text)


def append(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("a") as f:
        f.write(text)


def status(**kwargs: Any) -> None:
    path = RUN_ROOT / "CONTINUATION_STATUS.json"
    data: Dict[str, Any] = {}
    if path.exists():
        try:
            data = json.loads(path.read_text())
        except Exception:
            data = {}
    data.update(kwargs)
    data["updated_utc"] = utc()
    write(path, json.dumps(data, indent=2, sort_keys=True))


def ledger(message: str) -> None:
    append(RUN_ROOT / "CONTINUATION_LEDGER.md", f"- {utc()} — {message}\n")


def pid_alive(pid: int) -> bool:
    if pid <= 0:
        return False
    try:
        os.kill(pid, 0)
        return True
    except ProcessLookupError:
        return False
    except PermissionError:
        return True


def run_command(name: str, cmd: list[str], cwd: Path = REPO, timeout: int = 120) -> Dict[str, Any]:
    started = time.time()
    try:
        proc = subprocess.run(cmd, cwd=str(cwd), text=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, timeout=timeout)
        output = proc.stdout or ""
        rc = proc.returncode
    except Exception as exc:
        output = f"[EXCEPTION] {type(exc).__name__}: {exc}\n"
        rc = 125
    receipt = {"name": name, "cmd": cmd, "cwd": str(cwd), "returncode": rc, "elapsed_s": round(time.time() - started, 2), "output": output[-20000:]}
    write(RUN_ROOT / "system-receipts" / f"{name}.json", json.dumps(receipt, indent=2, sort_keys=True))
    write(RUN_ROOT / "system-receipts" / f"{name}.log", output)
    return receipt


def latest_candidate_from_previous() -> Optional[Path]:
    status_path = PREVIOUS_RUN_ROOT / "REPAIR_STATUS.json"
    if status_path.exists():
        try:
            data = json.loads(status_path.read_text())
            raw = data.get("latest_candidate") or data.get("candidate")
            if raw and Path(raw).exists():
                return Path(raw)
        except Exception:
            pass
    candidates = sorted((PREVIOUS_RUN_ROOT / "candidates").glob("cycle_*_nine_papers"))
    if candidates:
        return candidates[-1]
    overnight_candidates = sorted((OVERNIGHT_ROOT / "candidates").glob("cycle_*_nine_papers"))
    if overnight_candidates:
        return overnight_candidates[-1]
    return None


def write_board() -> None:
    lines = [
        "# Additional couple-hour system + PDF continuation",
        "",
        f"Run ID: `{RUN_ID}`",
        f"Run root: `{RUN_ROOT}`",
        f"Previous repair root: `{PREVIOUS_RUN_ROOT}`",
        f"Previous repair PID: `{PREVIOUS_PID}`",
        "",
        "## Mission",
        "Patch and verify the workflow system issues found by the overnight swarm, then continue local candidate-copy LaTeX/PDF publishability repair for an additional couple of hours after the current sprint exits.",
        "",
        "## Safety locks",
        *[f"- {x}" for x in SAFETY_LOCKS],
    ]
    write(RUN_ROOT / "CONTINUATION_BOARD.md", "\n".join(lines) + "\n")


def verify_system_fixes(source: Optional[Path]) -> None:
    py_compile = run_command("py_compile_system_scripts", [
        sys.executable,
        "-m",
        "py_compile",
        str(OVERNIGHT_SCRIPT),
        str(PATCHED_REPAIR_SCRIPT),
        str(LINT_TOOL),
    ])
    assertions = []
    overnight_text = OVERNIGHT_SCRIPT.read_text(errors="replace") if OVERNIGHT_SCRIPT.exists() else ""
    repair_text = PATCHED_REPAIR_SCRIPT.read_text(errors="replace") if PATCHED_REPAIR_SCRIPT.exists() else ""
    assertions.append({"name": "overnight_feed_no_16000_limit", "passed": "collect_lane_texts(lane_results, 16000)" not in overnight_text})
    assertions.append({"name": "workflow_lane_no_16000_limit", "passed": "read_text(p, 16000)" not in overnight_text})
    assertions.append({"name": "overnight_latest_run_symlink_support", "passed": "update_latest_run_symlink" in overnight_text and "latest_run" in overnight_text})
    assertions.append({"name": "repair_source_override_support", "passed": "NEBULAMIND_LATEX_REPAIR_SOURCE" in repair_text})
    assertions.append({"name": "repair_final_log_analysis", "passed": "analysis_text = transcript.read_text" in repair_text})
    assertions.append({"name": "repair_precompile_linter", "passed": "run_tex_lint(candidate, cycle, \"before\")" in repair_text})
    if source and source.exists():
        lint_receipt = run_command("tex_lint_source_candidate", [sys.executable, str(LINT_TOOL), "--json", str(source)], timeout=300)
        assertions.append({"name": "tex_lint_source_candidate_ran", "passed": lint_receipt["returncode"] in (0, 1)})
    all_passed = py_compile["returncode"] == 0 and all(a["passed"] for a in assertions)
    write(RUN_ROOT / "SYSTEM_FIX_ASSERTIONS.json", json.dumps({"created_utc": utc(), "all_passed": all_passed, "assertions": assertions}, indent=2, sort_keys=True))
    ledger(f"system fix assertions all_passed={all_passed}")


def stream_repair_process(source: Path) -> int:
    child_run_id = RUN_ID + "_PDF_REPAIR"
    env = os.environ.copy()
    env.update({
        "NEBULAMIND_LATEX_REPAIR_RUN_ID": child_run_id,
        "NEBULAMIND_LATEX_REPAIR_SOURCE": str(source),
        "NEBULAMIND_LATEX_REPAIR_SECONDS": str(2 * 60 * 60),
        "NEBULAMIND_LATEX_REPAIR_MAX_CYCLES": "6",
        "NEBULAMIND_LATEX_REPAIR_LANE_TIMEOUT": str(32 * 60),
        "NEBULAMIND_LATEX_REPAIR_INTEGRATOR_TIMEOUT": str(38 * 60),
        "NEBULAMIND_LATEX_REPAIR_SLEEP_BETWEEN_CYCLES": str(2 * 60),
    })
    child_root = REPAIR_DIR / child_run_id
    status(state="starting_child_repair", child_run_id=child_run_id, child_run_root=str(child_root), source_candidate=str(source))
    ledger(f"starting child repair {child_run_id} from {source}")
    cmd = [sys.executable, str(PATCHED_REPAIR_SCRIPT)]
    log_path = RUN_ROOT / "child-repair-stdout.log"
    with log_path.open("w") as log:
        proc = subprocess.Popen(cmd, cwd=str(REPO), env=env, text=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        status(state="child_repair_running", child_pid=proc.pid, child_run_id=child_run_id, child_run_root=str(child_root), source_candidate=str(source))
        assert proc.stdout is not None
        for line in proc.stdout:
            log.write(line)
            log.flush()
            print(line, end="", flush=True)
        rc = proc.wait()
    status(state="child_repair_completed", child_exit_code=rc, child_run_id=child_run_id, child_run_root=str(child_root), source_candidate=str(source))
    ledger(f"child repair completed exit={rc}")
    return rc


def main() -> int:
    RUN_ROOT.mkdir(parents=True, exist_ok=True)
    write(RUN_ROOT / "RUNNING.pid", str(os.getpid()) + "\n")
    write_board()
    status(state="started", pid=os.getpid(), started_utc=utc(), run_root=str(RUN_ROOT), previous_pid=PREVIOUS_PID, previous_run_root=str(PREVIOUS_RUN_ROOT))
    ledger("continuation wrapper started")

    waited = 0
    while pid_alive(PREVIOUS_PID) and waited < WAIT_MAX_SECONDS:
        status(state="waiting_for_previous_repair", waited_seconds=waited, previous_pid=PREVIOUS_PID)
        if waited == 0:
            print(f"Waiting for previous repair PID {PREVIOUS_PID} before launching continuation", flush=True)
        time.sleep(WAIT_POLL_SECONDS)
        waited += WAIT_POLL_SECONDS
    if pid_alive(PREVIOUS_PID):
        ledger(f"previous repair PID {PREVIOUS_PID} still alive after wait max; not launching overlapping repair")
        status(state="blocked_previous_repair_still_running", waited_seconds=waited, previous_pid=PREVIOUS_PID)
        return 2

    source = latest_candidate_from_previous()
    status(state="previous_repair_done", waited_seconds=waited, chosen_source=str(source) if source else None)
    ledger(f"previous repair done/absent after wait={waited}s; chosen source={source}")
    verify_system_fixes(source)
    if source is None or not source.exists():
        status(state="blocked_no_source_candidate")
        ledger("blocked: no source candidate found")
        return 3

    rc = stream_repair_process(source)
    status(state="completed", exit_code=rc, finished_utc=utc())
    write(RUN_ROOT / "FINAL_CONTINUATION_HANDOFF.md", "\n".join([
        "# Additional couple-hour system + PDF continuation handoff",
        "",
        f"Run ID: `{RUN_ID}`",
        f"Finished UTC: {utc()}",
        f"Previous repair root: `{PREVIOUS_RUN_ROOT}`",
        f"Source candidate for child repair: `{source}`",
        f"Child repair exit code: {rc}",
        f"Child repair root: `{REPAIR_DIR / (RUN_ID + '_PDF_REPAIR')}`",
        "",
        "## Safety",
        *[f"- {x}" for x in SAFETY_LOCKS],
        "",
        "No public replacement, DB/wiki/API write, deploy/restart, git write, cron, credential, or submission was performed.",
    ]) + "\n")
    return rc


if __name__ == "__main__":
    raise SystemExit(main())
