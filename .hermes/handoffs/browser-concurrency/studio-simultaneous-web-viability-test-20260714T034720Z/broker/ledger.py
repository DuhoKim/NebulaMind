"""Append-only, hash-chained run ledger (broker-epoch-ordered source of truth).

Entry: {"epoch": int, "utc": str, "actor": str, "type": str, "payload": dict,
        "prev_sha256": str, "entry_sha256": str}
entry_sha256 = sha256 of the canonical JSON of the entry minus entry_sha256.
Genesis prev_sha256 = 64*"0". Epochs are strictly monotonic +1.
"""
from __future__ import annotations

import hashlib
import json
import sys
from datetime import datetime, timezone
from pathlib import Path

GENESIS_PREV = "0" * 64


def _canon(obj) -> bytes:
    return json.dumps(obj, sort_keys=True, separators=(",", ":")).encode()


def _entry_hash(entry: dict) -> str:
    core = {k: v for k, v in entry.items() if k != "entry_sha256"}
    return hashlib.sha256(_canon(core)).hexdigest()


def read_entries(path: Path):
    if not path.exists():
        return []
    return [json.loads(line) for line in path.read_text().splitlines() if line.strip()]


def append(path: Path, actor: str, etype: str, payload: dict, utc: str | None = None) -> dict:
    entries = read_entries(path)
    if entries:
        prev = entries[-1]
        epoch, prev_sha = prev["epoch"] + 1, prev["entry_sha256"]
    else:
        epoch, prev_sha = 0, GENESIS_PREV
    entry = {
        "epoch": epoch,
        "utc": utc or datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
        "actor": actor,
        "type": etype,
        "payload": payload,
        "prev_sha256": prev_sha,
    }
    entry["entry_sha256"] = _entry_hash(entry)
    with path.open("a") as f:
        f.write(json.dumps(entry, sort_keys=True) + "\n")
    return entry


def verify(path: Path) -> tuple[bool, str]:
    entries = read_entries(path)
    prev_sha = GENESIS_PREV
    for i, e in enumerate(entries):
        if e["epoch"] != i:
            return False, f"epoch break at index {i}: {e['epoch']}"
        if e["prev_sha256"] != prev_sha:
            return False, f"chain break at epoch {i}"
        if _entry_hash(e) != e["entry_sha256"]:
            return False, f"hash mismatch at epoch {i}"
        prev_sha = e["entry_sha256"]
    return True, f"OK ({len(entries)} entries)"


def main(argv):
    path = Path(argv[1])
    cmd = argv[2]
    if cmd == "append":
        actor, etype, payload = argv[3], argv[4], json.loads(argv[5])
        entry = append(path, actor, etype, payload)
        print(json.dumps({"epoch": entry["epoch"], "entry_sha256": entry["entry_sha256"]}))
    elif cmd == "verify":
        ok, msg = verify(path)
        print(("VERIFY_OK " if ok else "VERIFY_FAIL ") + msg)
        return 0 if ok else 1
    else:
        print("usage: ledger.py <path> append <actor> <type> <payload-json> | verify")
        return 2
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
