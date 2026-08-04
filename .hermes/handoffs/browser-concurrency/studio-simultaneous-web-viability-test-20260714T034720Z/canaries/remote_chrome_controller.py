"""Task-scoped remote sandbox-Chrome controller (copied to the Mac Pro).

Tori verified `setsid` is missing on the Pro, so lifecycle stays in Python:
launch Chrome with subprocess start_new_session=True (own process group),
report {ready,port,pid}, hold until stdin EOF or a STOP line, then killpg the
exact group in finally (TERM->KILL). No setsid / ps / pkill / shell pipelines.

Usage (run over SSH): python3 remote_chrome_controller.py <profile> <log>
Speaks one JSON line on ready and one on stop, over stdout.
"""
from __future__ import annotations

import json
import os
import signal
import subprocess
import sys
import time
from pathlib import Path

CHROME = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
FLAGS = ["--headless=new", "--remote-debugging-port=0", "--no-first-run",
         "--no-default-browser-check", "--disable-sync", "--disable-extensions",
         "--disable-background-networking", "about:blank"]


def main(argv):
    profile = Path(argv[1]); log = Path(argv[2])
    profile.mkdir(parents=True, exist_ok=True)
    stale = profile / "DevToolsActivePort"
    if stale.exists():
        stale.unlink()
    if not Path(CHROME).exists():
        print(json.dumps({"ready": False, "error": "chrome missing on remote"})); return 2
    proc = subprocess.Popen([CHROME, f"--user-data-dir={profile}", *FLAGS],
                            stdout=log.open("w"), stderr=subprocess.STDOUT,
                            start_new_session=True)
    try:
        f = profile / "DevToolsActivePort"
        deadline = time.monotonic() + 20
        port = None
        while time.monotonic() < deadline:
            if f.exists() and f.stat().st_size > 0:
                port = int(f.read_text().splitlines()[0].strip()); break
            time.sleep(0.1)
        if port is None:
            raise TimeoutError("no DevToolsActivePort on remote")
        print(json.dumps({"ready": True, "port": port, "pid": proc.pid})); sys.stdout.flush()
        for line in sys.stdin:            # hold open; controller closes stdin (EOF) or sends STOP
            if line.strip() == "STOP":
                break
    finally:
        try:
            os.killpg(proc.pid, signal.SIGTERM); proc.wait(timeout=8); status = "term-clean"
        except Exception:
            try:
                os.killpg(proc.pid, signal.SIGKILL); proc.wait(timeout=5); status = "kill-forced"
            except Exception:
                status = "gone"
        print(json.dumps({"stopped": True, "teardown": status})); sys.stdout.flush()
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
