#!/usr/bin/env python3
"""nm_playback_receipts.py — did it actually play, and where?

Hwao, 2026-08-21: "twice I told him a report should be playing on the MacBook
and twice I had no way to know." Appending to queue.json proves a report was
QUEUED; it proves nothing about sound. This collects receipts written by the
players themselves at the moment playback starts.

Design rule from that request, and it is the important one: **nothing here ever
marks an entry played on enqueue.** A missing receipt keeps meaning "nobody
heard it", so a dead listener is detectable rather than discovered from Duho.

  nm_playback_receipts.py            collect + report the last few
  nm_playback_receipts.py --seq 26   answer for one report
"""
from __future__ import annotations
import argparse, json, pathlib, subprocess

R = pathlib.Path("/Users/duhokim/HermesOps/reports/status-audio")
PLAYED = R / "played.jsonl"
MACBOOK = "duhokim@100.75.47.116"
REMOTE_RECEIPTS = "~/.nm_played.jsonl"


def collect_remote() -> tuple[int, str]:
    """Pull the MacBook's receipts. Returns (new_lines, listener_state)."""
    try:
        alive = subprocess.run(
            ["ssh", "-o", "BatchMode=yes", "-o", "ConnectTimeout=8", MACBOOK,
             "pgrep -f nm_listen_daemon >/dev/null && echo alive || echo DEAD"],
            capture_output=True, text=True, timeout=25).stdout.strip()
        out = subprocess.run(
            ["ssh", "-o", "BatchMode=yes", "-o", "ConnectTimeout=8", MACBOOK,
             f"cat {REMOTE_RECEIPTS} 2>/dev/null || true"],
            capture_output=True, text=True, timeout=25).stdout
    except Exception as exc:
        return 0, f"UNREACHABLE ({type(exc).__name__})"
    have = set()
    if PLAYED.exists():
        for line in PLAYED.open(errors="replace"):
            have.add(line.strip())
    new = [ln for ln in out.splitlines() if ln.strip() and ln.strip() not in have]
    if new:
        with PLAYED.open("a") as f:
            f.write("\n".join(new) + "\n")
    return len(new), alive or "unknown"


def load() -> list[dict]:
    rows = []
    if PLAYED.exists():
        for line in PLAYED.open(errors="replace"):
            try:
                rows.append(json.loads(line))
            except Exception:
                continue
    return rows


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--seq", type=int, help="answer for one queue seq")
    ap.add_argument("--no-collect", action="store_true")
    a = ap.parse_args()

    state = "not collected"
    if not a.no_collect:
        n, state = collect_remote()
        if n:
            print(f"collected {n} new receipt(s) from the MacBook")
    rows = load()

    if a.seq is not None:
        mine = [r for r in rows if r.get("seq") == a.seq]
        if not mine:
            print(f"seq {a.seq}: NO PLAYBACK RECEIPT — nobody is known to have heard it.")
            print(f"  MacBook listener: {state}")
            return 1
        for r in sorted(mine, key=lambda r: r.get("local_time", "")):
            print(f"seq {a.seq}: {r['event']} on {r['host']} at {r['local_time']}")
        return 0

    try:
        q = json.loads((R / "queue.json").read_text())
        entries = q.get("entries", [])[-6:]
    except Exception:
        entries = []
    print(f"MacBook listener: {state}")
    print("recent reports and what actually played:")
    for e in entries:
        mine = [r for r in rows if r.get("seq") == e["seq"]]
        if e.get("quiet"):
            verdict = "quiet — not played by design"
        elif not mine:
            verdict = "NO RECEIPT — not known to have played"
        else:
            hosts = sorted({f"{r['host']}:{r['event']}" for r in mine})
            verdict = ", ".join(hosts)
        print(f"  #{e['seq']:>3} {e.get('name','?'):6} {e.get('stamp_kst','')}  {verdict}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
