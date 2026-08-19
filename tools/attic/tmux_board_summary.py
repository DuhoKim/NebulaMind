#!/usr/bin/env python3
"""Render a copy-safe text summary from a tmux board snapshot JSON file."""
from __future__ import annotations

import argparse
import json
import subprocess
import sys
from pathlib import Path
from typing import Any

DEFAULT_COPY_DIR = Path("/Users/duhokim/HermesOps/tmux-copies")
DEFAULT_LATEST = DEFAULT_COPY_DIR / "latest-board-summary.txt"


def load_snapshot(path: str) -> dict[str, Any]:
    if path == "-":
        return json.load(sys.stdin)
    return json.loads(Path(path).read_text())


def pane_sort_key(pane: dict[str, Any]) -> tuple[str, int, int, str]:
    return (
        str(pane.get("session_name", "")),
        int(pane.get("window_index") or 0),
        int(pane.get("pane_index") or 0),
        str(pane.get("pane_id", "")),
    )


def trim(value: Any, width: int) -> str:
    text = "" if value is None else str(value).replace("\n", " ").strip()
    if len(text) <= width:
        return text
    if width <= 1:
        return text[:width]
    return text[: width - 1] + "…"


def status_for(pane: dict[str, Any]) -> str:
    bits: list[str] = []
    if pane.get("active"):
        bits.append("active")
    if pane.get("dead"):
        bits.append("dead")
    if pane.get("in_mode"):
        bits.append("copy-mode")
    return ",".join(bits) if bits else "idle"


def role_for(pane: dict[str, Any]) -> str:
    return str(pane.get("role") or pane.get("mesh_role") or pane.get("master_role") or "-")


def render(snapshot: dict[str, Any], *, include_warnings: bool = True) -> str:
    summary = snapshot.get("summary") or {}
    lines: list[str] = []
    lines.append("NebulaMind tmux board summary")
    lines.append(f"generated_at_utc: {snapshot.get('generated_at_utc', '-')}")
    lines.append(
        "counts: "
        f"sessions={summary.get('session_count', len(snapshot.get('sessions') or []))} "
        f"windows={summary.get('window_count', len(snapshot.get('windows') or []))} "
        f"panes={summary.get('pane_count', len(snapshot.get('panes') or []))} "
        f"clients={summary.get('client_count', len(snapshot.get('clients') or []))} "
        f"control_clients={summary.get('control_mode_client_count', 0)} "
        f"dead_panes={summary.get('dead_pane_count', 0)} "
        f"empty_board_roles={summary.get('empty_board_role_count', 0)}"
    )

    options = snapshot.get("tmux_options") or {}
    if options:
        lines.append(
            "options: "
            f"mouse={options.get('mouse', '-')} "
            f"window-size={options.get('window-size', '-')} "
            f"pane-border-status={options.get('pane-border-status', '-')} "
            f"copy-command={options.get('copy-command', '-')}"
        )

    warnings = snapshot.get("warnings") or []
    if include_warnings and warnings:
        lines.append("")
        lines.append("warnings:")
        for warning in warnings:
            lines.append(f"- {warning}")

    lines.append("")
    lines.append("panes:")
    lines.append("target | role | command | title | status | path")
    lines.append("-" * 96)
    for pane in sorted(snapshot.get("panes") or [], key=pane_sort_key):
        lines.append(
            " | ".join(
                [
                    trim(pane.get("target", "-"), 28),
                    trim(role_for(pane), 18),
                    trim(pane.get("current_command", "-"), 16),
                    trim(pane.get("title", "-"), 52),
                    trim(status_for(pane), 18),
                    trim(pane.get("current_path", "-"), 80),
                ]
            )
        )

    clients = snapshot.get("clients") or []
    if clients:
        lines.append("")
        lines.append("clients:")
        lines.append("tty | session | term | size | control | readonly")
        lines.append("-" * 80)
        for client in clients:
            lines.append(
                " | ".join(
                    [
                        trim(client.get("tty") or client.get("name") or "-", 28),
                        trim(client.get("session_name", "-"), 20),
                        trim(client.get("termname", "-"), 16),
                        f"{client.get('width', 0)}x{client.get('height', 0)}",
                        "yes" if client.get("control_mode") else "no",
                        "yes" if client.get("readonly") else "no",
                    ]
                )
            )

    return "\n".join(lines).rstrip() + "\n"


def write_clipboard(text: str) -> None:
    cp = subprocess.run(["pbcopy"], input=text, text=True, capture_output=True, check=False)
    if cp.returncode != 0:
        raise RuntimeError(cp.stderr.strip() or "pbcopy failed")


def write_copy_files(text: str, output_path: Path | None) -> Path:
    path = output_path or DEFAULT_LATEST
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text)
    return path


def main() -> int:
    parser = argparse.ArgumentParser(description="Render a copy-safe text summary from tmux_board_snapshot.py JSON.")
    parser.add_argument("snapshot", help="Snapshot JSON path, or '-' for stdin.")
    parser.add_argument("--copy", action="store_true", help="Copy the rendered summary to the macOS clipboard via pbcopy.")
    parser.add_argument("--output", "-o", type=Path, help="Write rendered text to this path.")
    parser.add_argument("--no-warnings", action="store_true", help="Do not include snapshot warnings in text output.")
    args = parser.parse_args()

    snapshot = load_snapshot(args.snapshot)
    text = render(snapshot, include_warnings=not args.no_warnings)
    if args.output or args.copy:
        written = write_copy_files(text, args.output)
        if args.copy:
            write_clipboard(text)
            print(f"Copied board summary to clipboard and wrote {written}", file=sys.stderr)
    print(text, end="")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
