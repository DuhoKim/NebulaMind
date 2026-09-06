#!/usr/bin/env python3
"""Append ONE chained freeze record to the lane's seal journal — the record shape `scripts/stage2_gate_validation.py`
writes (timestamp, operation, relative_path, observed_digest, status, predecessor_receipt_digest, receipt_digest), using the
seal gate's own `canonical_bytes`, `sha256_bytes`, `sha256_file` and `_seal_predecessor` (which verifies the last record before
linking to it). Operations allowed: the two the signed V15 names — corpus-identity-freeze, tuning-freeze. Refuses a broken
chain, an unknown operation, a missing file, and a duplicate (same operation + observed_digest already sealed).
`verify` walks the WHOLE chain: every line canonical, every receipt_digest recomputed, every predecessor equal to the previous
receipt_digest (first = 64 zeros). Standard library only. Written 2026-09-06 (gap 1 of OPTION_A_RUN_SEQUENCE); not part of the
signed rule's pinned family; its digest is filed in the run record before use.
"""
from __future__ import annotations
import json, sys, time
from pathlib import Path
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent))
from seal_gate.seal_gate import canonical_bytes, sha256_bytes, sha256_file, _seal_predecessor, ZERO_DIGEST, GateFailure  # noqa: E402

OPERATIONS = ("corpus-identity-freeze", "tuning-freeze")

def utc() -> str: return time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime())

def verify_chain(journal: Path) -> int:
    """Return the record count; raise ValueError naming the first broken line."""
    if not journal.exists() or journal.stat().st_size == 0: return 0
    prev = ZERO_DIGEST; n = 0
    for i, line in enumerate(journal.read_bytes().splitlines(keepends=True), 1):
        rec = json.loads(line)
        if line != canonical_bytes(rec): raise ValueError(f"line {i}: non-canonical")
        body = dict(rec); rd = body.pop("receipt_digest", None)
        if rd != sha256_bytes(canonical_bytes(body)): raise ValueError(f"line {i}: receipt_digest mismatch")
        if body.get("predecessor_receipt_digest") != prev: raise ValueError(f"line {i}: predecessor != previous receipt_digest")
        prev = rd; n += 1
    return n

def append(journal: Path, operation: str, sealed_file: Path, relative_path: str | None = None, status: str = "SEALED", now: str | None = None) -> dict:
    if operation not in OPERATIONS: raise ValueError(f"REFUSE-OPERATION {operation!r} not in {OPERATIONS}")
    if not sealed_file.is_file(): raise ValueError(f"REFUSE-FILE-MISSING {sealed_file}")
    verify_chain(journal)                                   # whole chain first
    pred = _seal_predecessor(journal)                       # the gate's own check of the last record
    digest = sha256_file(sealed_file)
    if journal.exists():
        for line in journal.read_bytes().splitlines():
            r = json.loads(line)
            if r.get("operation") == operation and r.get("observed_digest") == digest: raise ValueError("REFUSE-DUPLICATE already sealed")
    try: rel = relative_path or sealed_file.resolve().relative_to(journal.resolve().parent).as_posix()
    except ValueError: rel = relative_path or sealed_file.name
    event = {"timestamp": now or utc(), "operation": operation, "relative_path": rel, "observed_digest": digest, "status": status, "predecessor_receipt_digest": pred}
    event["receipt_digest"] = sha256_bytes(canonical_bytes(event))
    with journal.open("ab") as fh: fh.write(canonical_bytes(event))
    verify_chain(journal)
    return event

def main(argv=None) -> int:
    import argparse
    ap = argparse.ArgumentParser(); sub = ap.add_subparsers(dest="mode", required=True)
    a = sub.add_parser("append"); a.add_argument("--journal", required=True); a.add_argument("--operation", required=True, choices=OPERATIONS); a.add_argument("--file", required=True); a.add_argument("--relative-path", default=None)
    v = sub.add_parser("verify"); v.add_argument("--journal", required=True)
    ns = ap.parse_args(argv)
    try:
        if ns.mode == "verify":
            n = verify_chain(Path(ns.journal)); print(json.dumps({"chain": "OK", "records": n})); return 0
        ev = append(Path(ns.journal), ns.operation, Path(ns.file), ns.relative_path); print(json.dumps(ev, sort_keys=True)); return 0
    except (ValueError, GateFailure) as e:
        print(json.dumps({"refused": str(e)})); return 2

if __name__ == "__main__": sys.exit(main())
