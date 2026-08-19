#!/usr/bin/env python3
"""Emit a read-only JSON snapshot of the active tmux board.

This helper intentionally uses only read-only tmux commands. It does not attach,
detach, split, resize, send keys, source config, or mutate pane options.
"""
from __future__ import annotations

import argparse
import json
import re
import shutil
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

BOARD_SESSION_RE = re.compile(r"^(ge-|mesh-|goru-|lana-|hwao-|fable-|lcm-)")


def utc_now() -> str:
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def tmux_base(tmux_bin: str, socket_name: str | None) -> list[str]:
    cmd = [tmux_bin]
    if socket_name:
        cmd.extend(["-L", socket_name])
    return cmd


def run_tmux(tmux_bin: str, socket_name: str | None, args: list[str], timeout: int = 15) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        tmux_base(tmux_bin, socket_name) + args,
        text=True,
        capture_output=True,
        timeout=timeout,
        check=False,
    )


def split_tsv(line: str, fields: list[str]) -> dict[str, str]:
    values = line.rstrip("\n").split("\t")
    if len(values) < len(fields):
        values += [""] * (len(fields) - len(values))
    elif len(values) > len(fields):
        values = values[: len(fields) - 1] + ["\t".join(values[len(fields) - 1 :])]
    return dict(zip(fields, values))


def as_int(value: str | None, default: int = 0) -> int:
    try:
        return int(value or default)
    except ValueError:
        return default


def as_bool(value: str | None) -> bool:
    return value == "1"


def collect_table(
    tmux_bin: str,
    socket_name: str | None,
    tmux_args: list[str],
    fields: list[str],
    required: bool,
    errors: list[dict[str, Any]],
) -> list[dict[str, str]]:
    cp = run_tmux(tmux_bin, socket_name, tmux_args)
    if cp.returncode != 0:
        errors.append(
            {
                "command": tmux_base(tmux_bin, socket_name) + tmux_args,
                "returncode": cp.returncode,
                "stderr": cp.stderr.strip(),
                "stdout": cp.stdout.strip(),
                "required": required,
            }
        )
        return []
    return [split_tsv(line, fields) for line in cp.stdout.splitlines() if line.strip()]


def collect_option(tmux_bin: str, socket_name: str | None, option: str) -> str | None:
    cp = run_tmux(tmux_bin, socket_name, ["show-option", "-gqv", option])
    if cp.returncode != 0:
        return None
    return cp.stdout.strip()


def normalize_sessions(raw: list[dict[str, str]]) -> list[dict[str, Any]]:
    sessions: list[dict[str, Any]] = []
    for row in raw:
        sessions.append(
            {
                "id": row.get("session_id", ""),
                "name": row.get("session_name", ""),
                "windows": as_int(row.get("session_windows")),
                "attached_clients": as_int(row.get("session_attached")),
                "created_epoch": as_int(row.get("session_created")),
                "created": row.get("session_created_string", ""),
                "group": row.get("session_group", ""),
            }
        )
    return sessions


def normalize_windows(raw: list[dict[str, str]]) -> list[dict[str, Any]]:
    windows: list[dict[str, Any]] = []
    for row in raw:
        session = row.get("session_name", "")
        index = as_int(row.get("window_index"))
        windows.append(
            {
                "target": f"{session}:{index}",
                "session_name": session,
                "id": row.get("window_id", ""),
                "index": index,
                "name": row.get("window_name", ""),
                "active": as_bool(row.get("window_active")),
                "panes": as_int(row.get("window_panes")),
                "layout": row.get("window_layout", ""),
                "width": as_int(row.get("window_width")),
                "height": as_int(row.get("window_height")),
                "flags": row.get("window_flags", ""),
            }
        )
    return windows


def normalize_panes(raw: list[dict[str, str]]) -> list[dict[str, Any]]:
    panes: list[dict[str, Any]] = []
    for row in raw:
        session = row.get("session_name", "")
        window_index = as_int(row.get("window_index"))
        pane_index = as_int(row.get("pane_index"))
        mesh_role = row.get("mesh_role", "")
        master_role = row.get("master_role", "")
        panes.append(
            {
                "target": f"{session}:{window_index}.{pane_index}",
                "session_name": session,
                "window_index": window_index,
                "window_name": row.get("window_name", ""),
                "pane_index": pane_index,
                "pane_id": row.get("pane_id", ""),
                "active": as_bool(row.get("pane_active")),
                "dead": as_bool(row.get("pane_dead")),
                "current_command": row.get("pane_current_command", ""),
                "current_path": row.get("pane_current_path", ""),
                "title": row.get("pane_title", ""),
                "mesh_role": mesh_role,
                "master_role": master_role,
                "role": mesh_role or master_role,
                "tty": row.get("pane_tty", ""),
                "width": as_int(row.get("pane_width")),
                "height": as_int(row.get("pane_height")),
                "pid": as_int(row.get("pane_pid")),
                "in_mode": as_bool(row.get("pane_in_mode")),
            }
        )
    return panes


def normalize_clients(raw: list[dict[str, str]]) -> list[dict[str, Any]]:
    clients: list[dict[str, Any]] = []
    for row in raw:
        clients.append(
            {
                "name": row.get("client_name", ""),
                "tty": row.get("client_tty", ""),
                "session_name": row.get("client_session", ""),
                "termname": row.get("client_termname", ""),
                "width": as_int(row.get("client_width")),
                "height": as_int(row.get("client_height")),
                "control_mode": as_bool(row.get("client_control_mode")),
                "readonly": as_bool(row.get("client_readonly")),
                "created_epoch": as_int(row.get("client_created")),
                "created": row.get("client_created_string", ""),
            }
        )
    return clients


def build_warnings(panes: list[dict[str, Any]], clients: list[dict[str, Any]], options: dict[str, str | None]) -> list[str]:
    warnings: list[str] = []
    for pane in panes:
        if pane["dead"]:
            warnings.append(f"dead pane: {pane['target']} {pane['current_command']} {pane['title']}")
        if BOARD_SESSION_RE.match(pane["session_name"]) and not pane.get("role"):
            warnings.append(f"empty board pane role: {pane['target']} title={pane['title']!r} cmd={pane['current_command']!r}")

    control_clients = [client for client in clients if client.get("control_mode")]
    normal_clients = [client for client in clients if not client.get("control_mode")]
    if control_clients and normal_clients:
        warnings.append(
            f"mixed tmux clients: {len(control_clients)} control-mode and {len(normal_clients)} normal clients attached"
        )
    elif control_clients:
        warnings.append(f"control-mode clients attached: {len(control_clients)}")

    window_size = options.get("window-size")
    if window_size == "smallest" and len(clients) > 1:
        widths = [client["width"] for client in clients if client.get("width")]
        heights = [client["height"] for client in clients if client.get("height")]
        if widths and heights and (min(widths) != max(widths) or min(heights) != max(heights)):
            warnings.append(
                "window-size smallest is constraining shared sessions: "
                f"client widths {min(widths)}..{max(widths)}, heights {min(heights)}..{max(heights)}"
            )
    return warnings


def snapshot(tmux_bin: str, socket_name: str | None) -> tuple[dict[str, Any], int]:
    errors: list[dict[str, Any]] = []
    session_fields = [
        "session_id",
        "session_name",
        "session_windows",
        "session_attached",
        "session_created",
        "session_created_string",
        "session_group",
    ]
    window_fields = [
        "session_name",
        "window_id",
        "window_index",
        "window_name",
        "window_active",
        "window_panes",
        "window_layout",
        "window_width",
        "window_height",
        "window_flags",
    ]
    pane_fields = [
        "session_name",
        "window_index",
        "window_name",
        "pane_index",
        "pane_id",
        "pane_active",
        "pane_dead",
        "pane_current_command",
        "pane_current_path",
        "pane_title",
        "mesh_role",
        "master_role",
        "pane_tty",
        "pane_width",
        "pane_height",
        "pane_pid",
        "pane_in_mode",
    ]
    client_fields = [
        "client_name",
        "client_tty",
        "client_session",
        "client_termname",
        "client_width",
        "client_height",
        "client_control_mode",
        "client_readonly",
        "client_created",
        "client_created_string",
    ]

    if not shutil.which(tmux_bin):
        payload = {
            "schema_version": "nebulamind.tmux_board_snapshot.v1",
            "generated_at_utc": utc_now(),
            "tmux_bin": tmux_bin,
            "socket_name": socket_name,
            "ok": False,
            "errors": [{"error": f"tmux binary not found on PATH: {tmux_bin}"}],
            "warnings": [],
            "sessions": [],
            "windows": [],
            "panes": [],
            "clients": [],
            "tmux_options": {},
        }
        return payload, 1

    raw_sessions = collect_table(
        tmux_bin,
        socket_name,
        ["list-sessions", "-F", "\t".join(f"#{{{field}}}" for field in session_fields)],
        session_fields,
        True,
        errors,
    )
    raw_windows = collect_table(
        tmux_bin,
        socket_name,
        ["list-windows", "-a", "-F", "\t".join(f"#{{{field}}}" for field in window_fields)],
        window_fields,
        True,
        errors,
    )
    raw_panes = collect_table(
        tmux_bin,
        socket_name,
        [
            "list-panes",
            "-a",
            "-F",
            "\t".join(
                [
                    "#{session_name}",
                    "#{window_index}",
                    "#{window_name}",
                    "#{pane_index}",
                    "#{pane_id}",
                    "#{pane_active}",
                    "#{pane_dead}",
                    "#{pane_current_command}",
                    "#{pane_current_path}",
                    "#{pane_title}",
                    "#{@mesh_role}",
                    "#{@master_role}",
                    "#{pane_tty}",
                    "#{pane_width}",
                    "#{pane_height}",
                    "#{pane_pid}",
                    "#{pane_in_mode}",
                ]
            ),
        ],
        pane_fields,
        True,
        errors,
    )
    raw_clients = collect_table(
        tmux_bin,
        socket_name,
        ["list-clients", "-F", "\t".join(f"#{{{field}}}" for field in client_fields)],
        client_fields,
        False,
        errors,
    )

    options = {
        option: collect_option(tmux_bin, socket_name, option)
        for option in [
            "mouse",
            "window-size",
            "history-limit",
            "pane-border-status",
            "pane-border-format",
            "copy-command",
            "mode-keys",
            "set-clipboard",
            "focus-events",
            "status-interval",
        ]
    }

    sessions = normalize_sessions(raw_sessions)
    windows = normalize_windows(raw_windows)
    panes = normalize_panes(raw_panes)
    clients = normalize_clients(raw_clients)
    required_errors = [error for error in errors if error.get("required")]
    warnings = build_warnings(panes, clients, options)

    payload = {
        "schema_version": "nebulamind.tmux_board_snapshot.v1",
        "generated_at_utc": utc_now(),
        "tmux_bin": tmux_bin,
        "socket_name": socket_name,
        "ok": not required_errors,
        "summary": {
            "session_count": len(sessions),
            "window_count": len(windows),
            "pane_count": len(panes),
            "client_count": len(clients),
            "control_mode_client_count": sum(1 for client in clients if client.get("control_mode")),
            "dead_pane_count": sum(1 for pane in panes if pane.get("dead")),
            "empty_board_role_count": sum(
                1 for pane in panes if BOARD_SESSION_RE.match(pane["session_name"]) and not pane.get("role")
            ),
        },
        "warnings": warnings,
        "errors": errors,
        "tmux_options": options,
        "sessions": sessions,
        "windows": windows,
        "panes": panes,
        "clients": clients,
    }
    return payload, 0 if not required_errors else 1


def main() -> int:
    parser = argparse.ArgumentParser(description="Emit a read-only JSON snapshot of tmux board sessions/windows/panes.")
    parser.add_argument("--output", "-o", type=Path, help="Write JSON to this path instead of stdout.")
    parser.add_argument("--tmux-bin", default="tmux", help="tmux binary to run. Default: tmux")
    parser.add_argument("--socket", "-L", dest="socket_name", help="Optional tmux socket name, passed as tmux -L NAME.")
    parser.add_argument("--pretty", action="store_true", help="Pretty-print JSON. Default when --output is used.")
    args = parser.parse_args()

    payload, exit_code = snapshot(args.tmux_bin, args.socket_name)
    pretty = args.pretty or bool(args.output)
    text = json.dumps(payload, ensure_ascii=False, indent=2 if pretty else None, sort_keys=True)
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(text + "\n")
    else:
        print(text)
    return exit_code


if __name__ == "__main__":
    raise SystemExit(main())
