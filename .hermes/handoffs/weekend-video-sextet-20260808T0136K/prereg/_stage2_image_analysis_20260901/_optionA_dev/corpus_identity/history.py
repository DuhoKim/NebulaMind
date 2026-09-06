"""AUTHENTICATED COLLECTION HISTORY (option A V21; V19/V20 audits M2). An append-only JSONL whose first entry is a GENESIS anchored to the
approval record's digest, its T_pulse and the rule digest, and whose every later entry carries `prev_sha256` = SHA-256 of the previous line's
exact bytes. Appends happen under an exclusive file lock after re-reading and re-validating the chain (read-check-append is atomic against
other processes using this module). A missing, truncated, reordered or edited history fails validation — it cannot be treated as a fresh
start: `genesis()` refuses to overwrite an existing file, and the driver requires the genesis to name the approval record it verified."""
from __future__ import annotations
import fcntl, hashlib, json, time
from pathlib import Path
STAGES = {"genesis", "collector-collect", "collector-verify", "collector-refusal", "collector-error", "witness-pending", "witness-closed",
          "builder-pre-parse-refusal", "builder-verdict", "builder-witness-or-adoption", "builder-error", "builder-accept", "builder-conflict"}
def utc(): return time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime())
def _line(entry: dict) -> bytes: return (json.dumps(entry, sort_keys=True, separators=(",", ":")) + "\n").encode()
def _sha(b: bytes) -> str: return hashlib.sha256(b).hexdigest()

def genesis(path: Path, approval_record_sha256: str, t_pulse: str, rule_sha256: str, round_number: int) -> dict:
    path = Path(path)
    if path.exists() and path.stat().st_size > 0: raise SystemExit("HISTORY-EXISTS: refusing to overwrite an initiated history")
    e = {"utc": utc(), "stage": "genesis", "approval_record_sha256": approval_record_sha256, "t_pulse": t_pulse, "rule_sha256": rule_sha256, "round": round_number, "prev_sha256": "0" * 64}
    with open(path, "ab") as f:
        fcntl.flock(f, fcntl.LOCK_EX); f.write(_line(e)); f.flush(); fcntl.flock(f, fcntl.LOCK_UN)
    return e

def validate(path: Path) -> list:
    """Return the entries; raise ValueError naming the first defect (missing, empty, bad JSON, unknown stage, broken chain, no genesis first)."""
    path = Path(path)
    if not path.is_file(): raise ValueError("HISTORY-MISSING")
    raw = path.read_bytes(); lines = raw.split(b"\n")
    if lines and lines[-1] == b"": lines = lines[:-1]
    if not lines: raise ValueError("HISTORY-EMPTY")
    out = []; prev = "0" * 64
    for i, l in enumerate(lines, 1):
        try: e = json.loads(l)
        except Exception: raise ValueError(f"HISTORY-BAD-JSON line {i}")
        if _line(e) != l + b"\n": raise ValueError(f"HISTORY-NON-CANONICAL line {i}")
        if e.get("stage") not in STAGES: raise ValueError(f"HISTORY-UNKNOWN-STAGE line {i}: {e.get('stage')!r}")
        if i == 1 and e["stage"] != "genesis": raise ValueError("HISTORY-NO-GENESIS")
        if i > 1 and e["stage"] == "genesis": raise ValueError(f"HISTORY-SECOND-GENESIS line {i}")
        if e.get("prev_sha256") != prev: raise ValueError(f"HISTORY-CHAIN-BROKEN line {i}")
        prev = _sha(l + b"\n"); out.append(e)
    return out

def append(path: Path, entry: dict) -> dict:
    """Validate the whole chain, then append under an exclusive lock (the lock is taken before the re-read so two appenders serialise)."""
    path = Path(path)
    with open(path, "ab") as f:
        fcntl.flock(f, fcntl.LOCK_EX)
        try:
            entries = validate(path); last = path.read_bytes().split(b"\n"); last = [x for x in last if x]
            e = {"utc": utc(), **entry, "prev_sha256": _sha(last[-1] + b"\n")}
            if e["stage"] not in STAGES: raise SystemExit(f"HISTORY-UNKNOWN-STAGE {e['stage']}")
            f.write(_line(e)); f.flush()
        finally: fcntl.flock(f, fcntl.LOCK_UN)
    return e

def first_accept(entries: list):
    """The earliest builder-accept, and the list of semantic conflicts: any later accept-bearing entry naming a different record or seed."""
    acc = [e for e in entries if e.get("stage") == "builder-accept"]
    if not acc: return None, []
    fa = acc[0]; conf = [e for e in entries if e.get("stage") in ("builder-accept", "builder-conflict", "collector-collect", "collector-verify", "builder-verdict") and str(e.get("outcome", "")).startswith("ACCEPT") and (e.get("record_sha256") != fa.get("record_sha256") or e.get("seed_hex") != fa.get("seed_hex")) and entries.index(e) > entries.index(fa)]
    return fa, conf

def append_locked(path: Path, fn):
    """ATOMIC read-check-append: under the exclusive lock, validate the chain, call fn(entries) → the entry to append (or fn raises to
    refuse); append it before releasing. Two builders racing for the first accept serialise here: the second sees the first's entry."""
    path = Path(path)
    with open(path, "ab") as f:
        fcntl.flock(f, fcntl.LOCK_EX)
        try:
            entries = validate(path); entry = fn(entries)
            if entry is None: return None
            last = [x for x in path.read_bytes().split(b"\n") if x]
            e = {"utc": utc(), **entry, "prev_sha256": _sha(last[-1] + b"\n")}
            if e["stage"] not in STAGES: raise SystemExit(f"HISTORY-UNKNOWN-STAGE {e['stage']}")
            f.write(_line(e)); f.flush(); return e
        finally: fcntl.flock(f, fcntl.LOCK_UN)
