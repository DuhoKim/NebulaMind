"""APPROVAL WITNESS (option A V17 draft; codex V16 C5 NOT MET: "the code checks a caller-supplied timestamp ... it does not verify when
approval was actually recorded or whether it was the first approval"). The approval record (the `statement_bytes` the beacon collector
binds to) must be a WITNESSED file: (W1) added to git by exactly one commit and never modified since (blob at that commit == bytes on
disk); (W2) that commit is an ancestor of the protected remote ref after a fetch, and `origin` is the pinned URL; (W3) the commit's
committer time is before T_pulse — committer times are operator-set, so this proves ORDER relative to the protected tip, not wall-clock
truth (stated); (W4) FIRST APPROVAL IS FINAL: exactly one approval-record path for the version exists anywhere in history;
(W5) FRESHNESS NONCE: the record quotes `DRAND_AT_APPROVAL: round R randomness <64 hex>` — a public value that did not exist before
round R's time — with round R's time ≥ MIN_T_SIGN, R < the seed round, and ≥ 2 pinned relays confirming it live. Together: the record was
written after round R (nonce) and pushed before T_pulse's round could exist (witness) — approval first, seed second, checkable by a
reader from public sources plus the protected branch. Refuses with APPROVAL-<token>. Standard library + drand_round."""
from __future__ import annotations
import re, subprocess
from datetime import datetime, timezone
from pathlib import Path
import sys; sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "beacon_v2"))
import drand_round

NONCE_RE = re.compile(r"^DRAND_AT_APPROVAL: round (\d+) randomness ([0-9a-f]{64})\s*$", re.M)
class ApprovalRefused(SystemExit): pass
def _refuse(tok, why): raise ApprovalRefused(f"APPROVAL-{tok}: {why}")
def _git(cwd, *a, check=True):
    r = subprocess.run(["git", *a], cwd=cwd, capture_output=True, text=True)
    if check and r.returncode != 0: _refuse("GIT", f"git {' '.join(a)} failed: {r.stderr.strip()[:120]}")
    return r.stdout

def verify(statement_path, t_pulse, seed_round, fetch, remote_ref, remote_url, min_t_sign, version_glob, do_fetch=True):
    p = Path(statement_path).resolve()
    root = Path(_git(p.parent, "rev-parse", "--show-toplevel").strip()); rel = p.relative_to(root).as_posix()
    adds = _git(root, "log", "--diff-filter=A", "--format=%H", "--", rel).split()
    if len(adds) != 1: _refuse("RECORD-NOT-COMMITTED", f"{len(adds)} commits add {rel}")
    commit = adds[0]
    hist = _git(root, "log", "--format=%H", "--", rel).split()
    if hist != [commit]: _refuse("RECORD-MODIFIED", f"{rel} touched by {len(hist)} commits")
    blob = subprocess.run(["git", "cat-file", "-p", f"{commit}:{rel}"], cwd=root, capture_output=True)
    if blob.returncode != 0 or blob.stdout != p.read_bytes(): _refuse("RECORD-MODIFIED", "bytes on disk differ from the committed blob")
    remote = remote_ref.split("/")[0]
    url = _git(root, "remote", "get-url", remote).strip()
    if url != remote_url: _refuse("REMOTE-URL", f"{url[:80]} != pinned")
    if do_fetch: _git(root, "fetch", remote)
    anc = subprocess.run(["git", "merge-base", "--is-ancestor", commit, remote_ref], cwd=root)
    if anc.returncode != 0: _refuse("RECORD-NOT-PUSHED", f"{commit[:12]} is not an ancestor of {remote_ref}")
    ct = datetime.fromisoformat(_git(root, "show", "-s", "--format=%cI", commit).strip().replace("Z", "+00:00")).astimezone(timezone.utc)   # git prints Z for UTC; Python 3.9 wants +00:00
    if ct >= t_pulse: _refuse("AFTER-T-PULSE", f"committer time {ct.isoformat()} is not before T_pulse {t_pulse.isoformat()} (committer time is operator-set; ordering only)")
    paths = {l for l in _git(root, "log", "--all", "--diff-filter=A", "--name-only", "--format=", "--", version_glob).split("\n") if l.strip()}
    if paths != {rel}: _refuse("NOT-FIRST", f"approval records for this version in history: {sorted(paths)}")
    m = NONCE_RE.search(p.read_text(encoding="utf-8"))
    if not m: _refuse("NONCE-MISSING", "no 'DRAND_AT_APPROVAL: round R randomness <hex>' line")
    R = int(m.group(1)); rand = m.group(2)
    r_time = datetime.fromtimestamp(drand_round.GENESIS + (R - 1) * drand_round.PERIOD, tz=timezone.utc)
    if not (R < seed_round): _refuse("NONCE-ROUND", f"nonce round {R} is not before the seed round {seed_round}")
    if r_time < datetime.strptime(min_t_sign, "%Y-%m-%dT%H:%M:%SZ").replace(tzinfo=timezone.utc): _refuse("NONCE-ROUND", f"nonce round {R} ({r_time.isoformat()}) predates MIN_T_SIGN {min_t_sign}")
    ag = drand_round.agreement(drand_round.collect(fetch, R), R)
    if not (ag["accepted"] and ag["randomness"] == rand): _refuse("NONCE-MISMATCH", f"pinned relays do not confirm round {R} randomness {rand[:12]}…")
    return {"commit": commit, "committer_utc": ct.strftime("%Y-%m-%dT%H:%M:%SZ"), "remote_ref": remote_ref, "remote_url": remote_url, "record_path": rel,
            "nonce_round": R, "nonce_round_utc": r_time.strftime("%Y-%m-%dT%H:%M:%SZ"), "nonce_randomness": rand, "nonce_relays_agreeing": ag.get("hosts", ag.get("count"))}
