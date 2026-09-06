"""APPROVAL WITNESS v2 (option A V18 draft; codex V17 FATAL 1: "a late writer plus backdated commit PASSES"). v1 proved present ancestry,
byte identity and an operator-set committer date — no wall-clock UPPER bound on the push. v2 adds the INDEPENDENT one: GitHub's
server-side PushEvent `created_at` for the push that delivered the approval commit to the protected branch (Events API; retained verbatim
in the identity; re-queryable by any reader for 90 days, attested afterwards). Also: the nonce must be the LATEST CLOSED drand round at
T_sign (round_for(T_sign) − 1 ≤ R ≤ round_for(T_sign)), exactly ONE nonce line and exactly ONE approval-time line (strict schema), the
approval time in the record must equal T_sign, and missing the deadline (push event ≥ T_pulse) CLOSES the commitment — nothing redraws.
What each check proves: W1 byte identity + committed once; W2 present ancestry of the protected ref + pinned origin; W3 (NEW) the
server recorded the push before T_pulse — an upper bound outside the operator's control; W4 exactly one record path for the version;
W5 nonce = a public value that did not exist before round R, R being the round current at T_sign — a lower bound. Together the record
was written after T_sign − 30 s and pushed before T_pulse. Still attested, not proved: who spoke, and that the approval statement
itself was made at T_sign (Codex's attestation + Duho's confirmations)."""
from __future__ import annotations
import json, re, subprocess
from datetime import datetime, timezone
from pathlib import Path
import sys; sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "beacon_v2"))
import drand_round

NONCE_RE = re.compile(r"^DRAND_AT_APPROVAL: round (\d+) randomness ([0-9a-f]{64})\s*$", re.M)
TSIGN_RE = re.compile(r"^APPROVAL_UTC: (\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}Z)\s*$", re.M)
DIGEST_RE = re.compile(r"^RULE_SHA256: ([0-9a-f]{64})\s*$", re.M)
class ApprovalRefused(SystemExit): pass
def _refuse(tok, why): raise ApprovalRefused(f"APPROVAL-{tok}: {why}")
def _git(cwd, *a, check=True):
    r = subprocess.run(["git", *a], cwd=cwd, capture_output=True, text=True)
    if check and r.returncode != 0: _refuse("GIT", f"git {' '.join(a)} failed: {r.stderr.strip()[:120]}")
    return r.stdout
def _utc(s): return datetime.strptime(s, "%Y-%m-%dT%H:%M:%SZ").replace(tzinfo=timezone.utc)

def github_events(repo="DuhoKim/NebulaMind", pages=3):
    """Production events source: `gh api` (authenticated CLI). Returns the list of event dicts, newest first."""
    out = []
    for page in range(1, pages + 1):
        r = subprocess.run(["gh", "api", f"repos/{repo}/events?per_page=100&page={page}"], capture_output=True, text=True)
        if r.returncode != 0: _refuse("EVENTS-UNAVAILABLE", r.stderr.strip()[:120])
        out.extend(json.loads(r.stdout))
    return out

def push_event_for(events, commit, branch_ref):
    """The PushEvent whose payload delivered `commit` to `branch_ref` (head == commit, or commit among payload.commits)."""
    for e in events:
        if e.get("type") != "PushEvent": continue
        p = e.get("payload", {})
        if p.get("ref") != branch_ref: continue
        if p.get("head") == commit or any(c.get("sha") == commit for c in p.get("commits", [])): return e
    return None

def verify(statement_path, t_sign, t_pulse, seed_round, rule_sha256, fetch, remote_ref, remote_url, min_t_sign, version_glob, events, branch_ref, do_fetch=True):
    p = Path(statement_path).resolve(); text = p.read_text(encoding="utf-8")
    # strict schema
    ts = TSIGN_RE.findall(text); nn = NONCE_RE.findall(text); dg = DIGEST_RE.findall(text)
    if len(ts) != 1: _refuse("SCHEMA", f"{len(ts)} APPROVAL_UTC lines, need exactly 1")
    if len(nn) != 1: _refuse("SCHEMA", f"{len(nn)} DRAND_AT_APPROVAL lines, need exactly 1")
    if len(dg) != 1 or dg[0] != rule_sha256: _refuse("SCHEMA", "RULE_SHA256 line missing, duplicated, or not the approved digest")
    if ts[0] != t_sign.strftime("%Y-%m-%dT%H:%M:%SZ"): _refuse("T-SIGN", f"record says {ts[0]}, record T_sign is {t_sign.strftime('%Y-%m-%dT%H:%M:%SZ')}")
    if t_sign < _utc(min_t_sign): _refuse("T-SIGN", f"before MIN_T_SIGN {min_t_sign}")
    # W1 committed once, never modified, bytes equal
    root = Path(_git(p.parent, "rev-parse", "--show-toplevel").strip()); rel = p.relative_to(root).as_posix()
    adds = _git(root, "log", "--diff-filter=A", "--format=%H", "--", rel).split()
    if len(adds) != 1: _refuse("RECORD-NOT-COMMITTED", f"{len(adds)} commits add {rel}")
    commit = adds[0]
    if _git(root, "log", "--format=%H", "--", rel).split() != [commit]: _refuse("RECORD-MODIFIED", f"{rel} touched after its adding commit")
    blob = subprocess.run(["git", "cat-file", "-p", f"{commit}:{rel}"], cwd=root, capture_output=True)
    if blob.returncode != 0 or blob.stdout != p.read_bytes(): _refuse("RECORD-MODIFIED", "bytes on disk differ from the committed blob")
    # W2 pinned origin + ancestry
    remote = remote_ref.split("/")[0]
    if _git(root, "remote", "get-url", remote).strip() != remote_url: _refuse("REMOTE-URL", "origin is not the pinned URL")
    if do_fetch: _git(root, "fetch", remote)
    if subprocess.run(["git", "merge-base", "--is-ancestor", commit, remote_ref], cwd=root).returncode != 0: _refuse("RECORD-NOT-PUSHED", f"{commit[:12]} not an ancestor of {remote_ref}")
    # W3 server-side push time (the upper bound)
    ev = push_event_for(events, commit, branch_ref)
    if ev is None: _refuse("PUSH-EVENT-MISSING", f"no PushEvent delivering {commit[:12]} to {branch_ref} in the retrieved events")
    created = datetime.fromisoformat(ev["created_at"].replace("Z", "+00:00")).astimezone(timezone.utc)
    if created >= t_pulse: _refuse("PUSHED-AFTER-T-PULSE", f"server push time {created.isoformat()} is not before T_pulse {t_pulse.isoformat()} — the commitment is CLOSED; nothing redraws")
    # W4 first approval is final
    paths = {l for l in _git(root, "log", "--all", "--diff-filter=A", "--name-only", "--format=", "--", version_glob).split("\n") if l.strip()}
    if paths != {rel}: _refuse("NOT-FIRST", f"approval records for this version in history: {sorted(paths)}")
    # W5 nonce = latest closed round at T_sign, confirmed live
    R = int(nn[0][0]); rand = nn[0][1]; r_sign = drand_round.round_for(t_sign)
    if not (r_sign - 1 <= R <= r_sign): _refuse("NONCE-ROUND", f"nonce round {R} is not the round current at T_sign (expected {r_sign - 1} or {r_sign})")
    if not (R < seed_round): _refuse("NONCE-ROUND", f"nonce round {R} not before the seed round {seed_round}")
    ag = drand_round.agreement(drand_round.collect(fetch, R), R)
    if not (ag["accepted"] and ag["randomness"] == rand): _refuse("NONCE-MISMATCH", f"pinned relays do not confirm round {R} randomness {rand[:12]}…")
    return {"commit": commit, "record_path": rel, "remote_ref": remote_ref, "remote_url": remote_url, "push_event": {"id": ev.get("id"), "created_at": ev["created_at"], "ref": ev["payload"].get("ref"), "head": ev["payload"].get("head")},
            "committer_utc": _git(root, "show", "-s", "--format=%cI", commit).strip(), "nonce_round": R, "nonce_randomness": rand, "t_sign": ts[0],
            "proves": "bytes committed once and pushed to the protected ref before T_pulse per the server's own timestamp; written after drand round R (current at T_sign)",
            "attested": "who spoke; that the approval statement was made at T_sign (Codex attestation + Duho's chat confirmations)"}
