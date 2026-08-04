"""Shell-safe remote Python execution (XM-1 pass1 STOP repair).

Defect: `ssh host python3 -c "<script>"` — OpenSSH joins the remote argv into
ONE string that the remote login shell (zsh) re-parses, mangling the script.

Fix: run `ssh <opts> host python3 -` and feed the script on STDIN. The remote
shell only ever sees the fixed, metacharacter-free tokens `python3 -`; the
script body travels as stdin data and is never reparsed by a shell. Any path is
embedded into the script as a Python string LITERAL via json.dumps (JSON string
== valid Python string literal), so paths with spaces/quotes/`;`/`$()`/`*`
cannot inject or break parsing. Local-testable with channel_argv=[].
"""
from __future__ import annotations

import json
import subprocess


def run_python_stdin(channel_argv, script: str, timeout: float = 20.0):
    """channel_argv is the transport prefix (e.g. [ssh, -o..., user@host]) or []
    for a local run. Appends `python3 -` and feeds `script` on stdin.
    Returns (returncode, stdout, stderr)."""
    argv = [*channel_argv, "python3", "-"]
    p = subprocess.run(argv, input=script, capture_output=True, text=True, timeout=timeout)
    return p.returncode, p.stdout, p.stderr


def preflight_empty_dir_script(remote_dir: str) -> str:
    """exit 0 if dir absent or empty; exit 2 if it exists and is nonempty."""
    return ("import os, sys\n"
            f"d = {json.dumps(remote_dir)}\n"
            "sys.exit(2 if os.path.isdir(d) and os.listdir(d) else 0)\n")


def sha256_script(remote_path: str) -> str:
    """print the sha256 hex of a remote file."""
    return ("import hashlib\n"
            f"p = {json.dumps(remote_path)}\n"
            "print(hashlib.sha256(open(p, 'rb').read()).hexdigest())\n")
