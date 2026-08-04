"""Shared local sandbox-Chrome lifecycle helpers (start_new_session pgids,
stale-port cleanup, exact-pgid TERM->KILL teardown, page-target discovery).
No broad pgrep/pkill anywhere; only spawned pgids are ever signalled.
"""
from __future__ import annotations

import json
import os
import signal
import subprocess
import time
import urllib.request
from pathlib import Path

CHROME = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
FLAGS = ["--headless=new", "--remote-debugging-port=0", "--no-first-run",
         "--no-default-browser-check", "--disable-sync", "--disable-extensions",
         "--disable-background-networking", "about:blank"]
PORT_DEADLINE_S = 20.0


def launch(profile: Path, log: Path):
    profile.mkdir(parents=True, exist_ok=True)
    stale = profile / "DevToolsActivePort"
    if stale.exists():
        stale.unlink()
    return subprocess.Popen([CHROME, f"--user-data-dir={profile}", *FLAGS],
                            stdout=log.open("w"), stderr=subprocess.STDOUT,
                            start_new_session=True)


def wait_port(profile: Path, deadline: float) -> int:
    f = profile / "DevToolsActivePort"
    while time.monotonic() < deadline:
        if f.exists() and f.stat().st_size > 0:
            return int(f.read_text().splitlines()[0].strip())
        time.sleep(0.1)
    raise TimeoutError(f"DevToolsActivePort not written for {profile}")


def page_target_id(port: int, host: str = "127.0.0.1") -> str:
    with urllib.request.urlopen(f"http://{host}:{port}/json/list", timeout=5) as r:
        for t in json.loads(r.read()):
            if t.get("type") == "page":
                return t["id"]
    raise RuntimeError(f"no page target on {host}:{port}")


def terminate(proc) -> str:
    if proc is None:
        return "never-started"
    if proc.poll() is not None:
        return f"already-exited({proc.returncode})"
    try:
        os.killpg(proc.pid, signal.SIGTERM); proc.wait(timeout=8); return "term-clean"
    except (subprocess.TimeoutExpired, ProcessLookupError):
        try:
            os.killpg(proc.pid, signal.SIGKILL); proc.wait(timeout=5); return "kill-forced"
        except ProcessLookupError:
            return "gone"
