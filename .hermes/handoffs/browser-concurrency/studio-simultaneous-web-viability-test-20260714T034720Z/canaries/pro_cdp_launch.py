"""Launch and verify one dedicated visible CDP Chrome on the Mac Pro.

This script is streamed to the Pro over authenticated SSH. It never reads an
existing Chrome profile and intentionally leaves the dedicated browser running
for Duho's manual sign-in.
"""

import argparse
import json
import os
import shlex
import stat
import subprocess
import time
import urllib.request
from pathlib import Path
from urllib.parse import urlsplit, urlunsplit


CHROME_BIN = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
EXPECTED_PROFILE_NAME = "dr-live-cdp-20260714"
EXPECTED_PACKET = "studio-simultaneous-web-viability-test-20260714T034720Z"


def build_chrome_args(profile: str, port: int, url: str) -> list[str]:
    return [
        "open",
        "-na",
        "Google Chrome",
        "--args",
        f"--user-data-dir={profile}",
        "--remote-debugging-address=127.0.0.1",
        f"--remote-debugging-port={port}",
        "--no-first-run",
        "--no-default-browser-check",
        "--new-window",
        url,
    ]


def is_dedicated_root(ppid: int, command: str, profile: str) -> bool:
    if ppid != 1 or not command.startswith(CHROME_BIN):
        return False
    if " --type=" in command:
        return False
    try:
        args = shlex.split(command)
    except ValueError:
        return False
    return f"--user-data-dir={profile}" in args


def listener_is_loopback(lsof_text: str, port: int) -> bool:
    listener_lines = [
        line for line in lsof_text.splitlines() if f":{port}" in line and "(LISTEN)" in line
    ]
    return bool(listener_lines) and all(f"127.0.0.1:{port}" in line for line in listener_lines)


def sanitize_targets(targets: list[dict]) -> list[dict]:
    sanitized = []
    for target in targets:
        split = urlsplit(str(target.get("url", "")))
        clean_url = urlunsplit((split.scheme, split.netloc, split.path, "", ""))
        sanitized.append(
            {
                "id": str(target.get("id", "")),
                "type": str(target.get("type", "")),
                "title": str(target.get("title", "")),
                "url": clean_url,
            }
        )
    return sanitized


def root_processes() -> list[tuple[int, int, str]]:
    output = subprocess.check_output(["ps", "-axww", "-o", "pid=,ppid=,command="], text=True)
    roots = []
    for line in output.splitlines():
        fields = line.strip().split(None, 2)
        if len(fields) != 3:
            continue
        pid_text, ppid_text, command = fields
        if command.startswith(CHROME_BIN) and " --type=" not in command:
            roots.append((int(pid_text), int(ppid_text), command))
    return roots


def fetch_json(url: str) -> object:
    with urllib.request.urlopen(url, timeout=2) as response:
        return json.loads(response.read().decode("utf-8"))


def visible_window_state(pid: int) -> tuple[bool, int]:
    script = f'''
    tell application "System Events"
        set theProc to first application process whose unix id is {pid}
        set procVisible to visible of theProc
        set windowCount to count of windows of theProc
        return (procVisible as string) & "," & (windowCount as string)
    end tell
    '''
    output = subprocess.check_output(["osascript", "-e", script], text=True, stderr=subprocess.STDOUT)
    visible_text, count_text = output.strip().split(",", 1)
    return visible_text.lower() == "true", int(count_text)


def validate_fresh_profile(profile: Path) -> None:
    if profile.name != EXPECTED_PROFILE_NAME or EXPECTED_PACKET not in profile.parts:
        raise RuntimeError("profile path is outside the authorized packet target")
    if profile.exists():
        raise RuntimeError("dedicated profile path already exists; refusing non-fresh launch")


def launch_and_verify(profile: Path, port: int, url: str) -> dict:
    validate_fresh_profile(profile)
    if not 1024 <= port <= 65535:
        raise RuntimeError("remote debugging port must be an unprivileged TCP port")

    before_roots = root_processes()
    if any(is_dedicated_root(ppid, command, str(profile)) for _, ppid, command in before_roots):
        raise RuntimeError("dedicated Chrome root already exists")

    probe = subprocess.run(
        ["lsof", f"-iTCP:{port}", "-sTCP:LISTEN", "-n", "-P"],
        text=True,
        capture_output=True,
        check=False,
    )
    if probe.returncode == 0 and probe.stdout.strip():
        raise RuntimeError("remote debugging port is already in use")

    old_umask = os.umask(0o077)
    try:
        profile.mkdir(parents=True, mode=0o700)
        profile.chmod(0o700)
    finally:
        os.umask(old_umask)

    subprocess.run(build_chrome_args(str(profile), port, url), check=True)

    dedicated = []
    version = None
    targets = None
    listener_text = ""
    deadline = time.monotonic() + 25
    while time.monotonic() < deadline:
        roots = root_processes()
        dedicated = [
            item for item in roots if is_dedicated_root(item[1], item[2], str(profile))
        ]
        listener = subprocess.run(
            ["lsof", f"-iTCP:{port}", "-sTCP:LISTEN", "-n", "-P"],
            text=True,
            capture_output=True,
            check=False,
        )
        listener_text = listener.stdout
        try:
            version = fetch_json(f"http://127.0.0.1:{port}/json/version")
            targets = fetch_json(f"http://127.0.0.1:{port}/json/list")
        except Exception:
            version = None
            targets = None
        if len(dedicated) == 1 and listener_is_loopback(listener_text, port) and targets:
            break
        time.sleep(0.5)

    if len(dedicated) != 1:
        raise RuntimeError("did not find exactly one dedicated Chrome root")
    if not listener_is_loopback(listener_text, port):
        raise RuntimeError("CDP listener is absent or is not loopback-only")
    if not isinstance(version, dict) or not isinstance(targets, list):
        raise RuntimeError("CDP metadata endpoint did not become ready")

    sanitized = sanitize_targets(targets)
    sign_in_targets = [
        target
        for target in sanitized
        if target["type"] == "page" and urlsplit(target["url"]).hostname == "accounts.google.com"
    ]
    if not sign_in_targets:
        raise RuntimeError("CDP has no Google sign-in page target")

    dedicated_pid = dedicated[0][0]
    process_visible, window_count = visible_window_state(dedicated_pid)
    if not process_visible or window_count < 1:
        raise RuntimeError("dedicated Chrome does not have a verified visible GUI window")

    after_roots = root_processes()
    default_roots_after = [
        item for item in after_roots if not is_dedicated_root(item[1], item[2], str(profile))
    ]
    if len(default_roots_after) != len(before_roots):
        raise RuntimeError("default Chrome root count changed during dedicated launch")

    return {
        "status": "ready_for_duho_sign_in",
        "dedicated_pid": dedicated_pid,
        "default_root_count_before": len(before_roots),
        "default_root_count_after": len(default_roots_after),
        "listener": f"127.0.0.1:{port}",
        "profile_mode": oct(stat.S_IMODE(profile.stat().st_mode)),
        "process_visible": process_visible,
        "window_count": window_count,
        "browser": str(version.get("Browser", "")),
        "targets": sign_in_targets,
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--profile", required=True)
    parser.add_argument("--port", required=True, type=int)
    parser.add_argument("--url", default="https://accounts.google.com/")
    args = parser.parse_args()
    try:
        result = launch_and_verify(Path(args.profile), args.port, args.url)
    except Exception as exc:
        print(json.dumps({"status": "stop", "error": f"{type(exc).__name__}: {exc}"}))
        return 2
    print(json.dumps(result, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
