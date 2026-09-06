"""APPROVAL WITNESS v4 (option A V21 draft; codex V20 items W3/W5/M1). v3 bytes preserved in approval_witness_v3.py.
v4 adds: W3 delivery by before..head ANCESTRY (a push whose payload.commits omits the approval commit still delivers it when before is a
strict ancestor of the commit and the commit an ancestor of head — checked with git, not by substring); the PENDING / CLOSED state of a missing
push event is RETURNED as data (refusal token carries it; the builder persists it in the authenticated history) — PENDING while now < T_pulse +
EVENTS_LATENCY_S (the API's stated publication latency), CLOSED afterwards; W5 the nonce round is EXACTLY {round_for(T_sign)−1,
round_for(T_sign)}, its scheduled time must be ≥ MIN_T_SIGN (the nonce postdates the amendment) and before the seed round, and the nonce
is AUTHENTICATED: every pinned relay's body for the nonce round is fetched from the chain-hash-qualified path, BLS-verified under the pinned
key with exact URL membership, ≥ 2 distinct relays must verify with randomness equal to the recorded nonce; the verified bodies are RETAINED
in the witness (nonce_bodies_b64) so the driver re-verifies them offline. Corrected docstring: the record was written no earlier than the
scheduled time of round R (≥ T_sign − 60 s), not "T_sign − 30 s".
What each check proves: W1 byte identity + committed once; W2 present ancestry of the protected ref + pinned origin; W3 the server recorded
the push before T_pulse; W4 exactly one record path for the version; W5 nonce = a BLS-verified public value that did not exist before round
R's scheduled time. Still attested, not proved: who spoke, and that the approval statement itself was made at T_sign."""
from __future__ import annotations
import base64, json, re, subprocess, hashlib
from datetime import datetime, timezone
from pathlib import Path
import sys; sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "drand_only"))
import verify_drand_v2 as vd

NONCE_RE = re.compile(r"^DRAND_AT_APPROVAL: round (\d+) randomness ([0-9a-f]{64})\s*$", re.M)
TSIGN_RE = re.compile(r"^APPROVAL_UTC: (\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}Z)\s*$", re.M)
DIGEST_RE = re.compile(r"^RULE_SHA256: ([0-9a-f]{64})\s*$", re.M)
EVENTS_LATENCY_S = 6 * 3600                               # GitHub Events API: 30 s to 6 h publication latency (stated by GitHub)
MIN_NONCE_RELAYS = 2
class ApprovalRefused(SystemExit):
    def __init__(self, msg, state=None): super().__init__(msg); self.state = state
def _refuse(tok, why, state=None): raise ApprovalRefused(f"APPROVAL-{tok}: {why}", state)
def _git(cwd, *a, check=True):
    r = subprocess.run(["git", *a], cwd=cwd, capture_output=True, text=True)
    if check and r.returncode != 0: _refuse("GIT", f"git {' '.join(a)} failed: {r.stderr.strip()[:120]}")
    return r.stdout
def _utc(s): return datetime.strptime(s, "%Y-%m-%dT%H:%M:%SZ").replace(tzinfo=timezone.utc)
def _is_ancestor(root, a, b):
    """True iff commit a is an ancestor of commit b (a == b counts), and both exist locally."""
    if not (re.fullmatch(r"[0-9a-f]{40}", str(a)) and re.fullmatch(r"[0-9a-f]{40}", str(b))): return False
    return subprocess.run(["git", "merge-base", "--is-ancestor", a, b], cwd=root, capture_output=True).returncode == 0

def github_events(repo="DuhoKim/NebulaMind", pages=3):
    """Production events source: `gh api` (authenticated CLI). Returns (events newest-first, provenance): endpoint per page, retrieval UTC, gh version."""
    out = []; prov = {"endpoints": [], "retrieved_utc": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")}
    v = subprocess.run(["gh", "--version"], capture_output=True, text=True); prov["gh_version"] = (v.stdout.splitlines() or [""])[0]
    for page in range(1, pages + 1):
        ep = f"repos/{repo}/events?per_page=100&page={page}"; prov["endpoints"].append(ep)
        r = subprocess.run(["gh", "api", ep], capture_output=True, text=True)
        if r.returncode != 0: _refuse("EVENTS-UNAVAILABLE", r.stderr.strip()[:120])
        out.extend(json.loads(r.stdout))
    return out, prov

def delivers(e, commit, branch_ref, root=None):
    """Does PushEvent e deliver `commit` to `branch_ref`? head == commit, commit in payload.commits, or (v4) before..head ancestry via git."""
    if e.get("type") != "PushEvent": return False
    p = e.get("payload") or {}
    if p.get("ref") != branch_ref: return False
    if p.get("head") == commit or any(c.get("sha") == commit for c in p.get("commits", [])): return True
    before, head = p.get("before"), p.get("head")
    return bool(root) and before != commit and _is_ancestor(root, before, commit) and _is_ancestor(root, commit, head)

def push_event_for(events, commit, branch_ref, root=None):
    """The EARLIEST qualifying PushEvent (a later repeated push must not hide an earlier one)."""
    hits = [e for e in events if delivers(e, commit, branch_ref, root)]
    return min(hits, key=lambda e: e["created_at"]) if hits else None

def verify_nonce_bodies(bodies_b64, R, rand):
    """Offline re-verification of retained nonce bodies: {exact pinned url: b64 body} → verified urls (≥ MIN_NONCE_RELAYS distinct, all with randomness == rand)."""
    ok = []
    for url, b in (bodies_b64 or {}).items():
        try:
            resp = json.loads(base64.b64decode(b))
            if isinstance(resp, dict) and vd.verify(resp, R, url)["accepted"] and str(resp.get("randomness")) == rand: ok.append(url)
        except Exception: pass
    return sorted(set(ok))

def verify(statement_path, t_sign, t_pulse, seed_round, rule_sha256, fetch, remote_ref, remote_url, min_t_sign, version_glob, events, branch_ref, do_fetch=True, provenance=None, now=None):
    now = now or datetime.now(timezone.utc)
    p = Path(statement_path).resolve(); text = p.read_text(encoding="utf-8")
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
    if not _is_ancestor(root, commit, _git(root, "rev-parse", remote_ref).strip()): _refuse("RECORD-NOT-PUSHED", f"{commit[:12]} not an ancestor of {remote_ref}")
    # W3 server-side push time (the upper bound), delivery incl. before..head ancestry, PENDING/CLOSED as data
    ev = push_event_for(events, commit, branch_ref, root)
    if ev is None:
        state = "PENDING" if now < t_pulse.replace(tzinfo=timezone.utc) + __import__("datetime").timedelta(seconds=EVENTS_LATENCY_S) else "CLOSED"
        _refuse("PUSH-EVENT-" + state, f"no PushEvent delivering {commit[:12]} to {branch_ref} in the retrieved events — {state}: " + ("within the API's publication latency; retry, nothing else changes" if state == "PENDING" else "the latency window has passed; the commitment is CLOSED; never a licence for a new approval, time, round or source"), state)
    created = datetime.fromisoformat(ev["created_at"].replace("Z", "+00:00")).astimezone(timezone.utc)
    if created >= t_pulse: _refuse("PUSHED-AFTER-T-PULSE", f"server push time {created.isoformat()} is not before T_pulse {t_pulse.isoformat()} — the commitment is CLOSED; nothing redraws", "CLOSED")
    # W4 first approval is final
    paths = {l for l in _git(root, "log", "--all", "--diff-filter=A", "--name-only", "--format=", "--", version_glob).split("\n") if l.strip()}
    if paths != {rel}: _refuse("NOT-FIRST", f"approval records for this version in history: {sorted(paths)}")
    # W5 nonce: exact round set, scheduled bound, before the seed round, BLS-authenticated from the chain-hash path, bodies retained
    R = int(nn[0][0]); rand = nn[0][1]; r_sign = vd.round_for(t_sign)
    if R not in (r_sign - 1, r_sign): _refuse("NONCE-ROUND", f"nonce round {R} is not in {{{r_sign - 1}, {r_sign}}} (the rounds current at T_sign)")
    if vd.round_time(R) < _utc(min_t_sign): _refuse("NONCE-ROUND", f"nonce round {R} was scheduled at {vd.round_time(R).isoformat()}, before MIN_T_SIGN {min_t_sign}")
    if not (R < seed_round): _refuse("NONCE-ROUND", f"nonce round {R} not before the seed round {seed_round}")
    bodies = {}
    for host in vd.RELAYS:
        url = vd.round_url(host, R)
        try: bodies[url] = base64.b64encode(fetch(url)).decode()
        except Exception: pass
    okurls = verify_nonce_bodies(bodies, R, rand)
    if len(okurls) < MIN_NONCE_RELAYS: _refuse("NONCE-UNAUTHENTICATED", f"{len(okurls)} pinned relays serve a BLS-verifying body for round {R} with randomness {rand[:12]}… (need {MIN_NONCE_RELAYS})")
    return {"witness_version": 4, "commit": commit, "record_path": rel, "record_sha256": hashlib.sha256(p.read_bytes()).hexdigest(), "remote_ref": remote_ref, "remote_url": remote_url, "push_event": ev, "push_event_sha256": hashlib.sha256(json.dumps(ev, sort_keys=True, separators=(",", ":")).encode()).hexdigest(), "events_provenance": provenance,
            "committer_utc": _git(root, "show", "-s", "--format=%cI", commit).strip(), "nonce_round": R, "nonce_randomness": rand, "nonce_bodies_b64": {u: bodies[u] for u in okurls}, "nonce_verified_urls": okurls, "t_sign": ts[0],
            "proves": "bytes committed once and pushed to the protected ref before T_pulse per the server's own timestamp; written no earlier than the scheduled time of drand round R (the round current at T_sign, BLS-verified)",
            "attested": "who spoke; that the approval statement was made at T_sign (Codex attestation + Duho's chat confirmations)"}
