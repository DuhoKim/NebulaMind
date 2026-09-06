"""TRACK 2 v2 — RECOMMENDED, UNADOPTED designs for the two provenance boundaries, REPAIRED after codex's probe of 21:00 KST (the v1 history
validator walked LOCAL HEAD and trusted the supplied open commit; it never asked the remote — a protection ASSUMED, not CHECKED) and BUILT out
after Blanc's 21:04 correction (retrieval, pagination, error handling and the expired-event receipt were prose in v1). v1 bytes preserved in
provenance_designs.py. NOTHING here is wired into the production driver.

(a) EVENTS — `retrieve_events(repo, runner)` executes the read-only retrieval through a RUNNER (production: `gh api` via subprocess; the tests
    inject a fixture runner, labelled) with PAGINATION (pages until a short/empty page or max_pages) and ERROR HANDLING that names its path:
    EventsUnavailable(kind ∈ RATE-LIMITED | SERVER-ERROR | AUTH | NOT-FOUND | HTTP | MALFORMED | TRANSPORT). `authenticate_event_live` = retrieve,
    then `authenticate_event` (v1's pure decision, unchanged): AUTHENTIC | FORGED | UNAVAILABLE | EXPIRED (the retained event is older than the
    oldest event the feed still serves). EXPIRED path: `write_events_receipt` (taken INSIDE the window by an independent party — the OPS session —
    naming its origin) and `verify_events_receipt`: the receipt file must be added ONCE by one commit and never touched (like the approval record),
    that commit must be an ancestor of the LIVE remote head (ls-remote, not local refs), its events digest recomputes, its origin equals the
    EXPECTED ORIGIN — the label {actor: ops-witness, session: OPS}, PROPOSED BY THE LANE for the OPS session's receipts, unadopted, not a user
    decision (QUESTIONS_FOR_DUHO_TRACK2_ORIGIN_AND_RECEIPTS_20260906.md) — and the retained event is in it verbatim. RESIDUAL TRUST, stated:
    with a single GitHub account the receipt's pusher cannot be distinguished by GitHub from the lane; a lane that REPLACES a receipt is caught
    (RECEIPT-NOT-FIRST); a lane that FORGES the first receipt in the named party's name is NOT caught by this code — it is caught only by OPS's own retained
    copy (outside the code); closing it BY CODE needs an expected-receipt identity the driver can check (a second GitHub identity's PushEvent actor,
    or a key the lane cannot read) — the ONE step only Duho can provide; no per-receipt human confirmation is proposed. Stated, not hidden.
(b) HISTORY — `validate_continuation_v2(root, rel, open_commit, remote_url, ref)`: (1) the CURRENT remote head is obtained INDEPENDENTLY with
    `git ls-remote <pinned url> <ref>` (production: https://github.com/DuhoKim/NebulaMind.git over TLS; the tests use a local bare repository
    with non-fast-forward receives denied, labelled); an operator-supplied `expected_head` that differs from the live head is refused as STALE;
    an unreachable remote is RETRY-REMOTE-UNAVAILABLE, never a pass; (2) the ref is fetched into a private witness ref so its objects are local;
    (3) `open_commit` must be an ancestor of the REMOTE head (HISTORY-OPEN-NOT-PUBLISHED otherwise); (4) the file's commit chain is walked on the
    REMOTE ref's history — first commit = open_commit, every later blob a strict prefix-extension of the previous one (append-only through git
    objects); (5) PUSH-ACKNOWLEDGEMENT BOUNDARY: the acknowledged history is the blob at the remote head; the working tree must EQUAL it — any
    local-only bytes (an uncommitted extension, or a commit the remote never acknowledged) are PENDING-PUSH and nothing in them governs
    acceptance until the push is acknowledged; local commits not on the remote are reported. States: OK | PENDING-PUSH | STALE-EXPECTED-HEAD |
    RETRY-REMOTE-UNAVAILABLE | HISTORY-OPEN-NOT-PUBLISHED | HISTORY-NOT-AN-EXTENSION | HISTORY-DIVERGED.
    COST (corrected — Blanc's summary to Duho said "one push per freeze"): ONE PUSH PER COLLECTOR/BUILDER ATTEMPT, i.e. per history entry; a
    failed push leaves the entry PENDING-PUSH — the builder must retry the push, never rebuild; the driver refuses while PENDING-PUSH stands.
    TRUSTED afterwards: the remote's answer to ls-remote (TLS to github.com for the pinned URL) and server-side branch protection (no force
    push, no deletion); the PushEvent witnessing the open commit (design (a)). NOT trusted: local refs, local HEAD, the file's own chain, the
    operator's clock."""
from __future__ import annotations
import hashlib, json, re, subprocess, time
from pathlib import Path
def canon(e): return hashlib.sha256(json.dumps(e, sort_keys=True, separators=(",", ":")).encode()).hexdigest()
def utc(): return time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime())

# ------------------------------------------------------------------ (a) events
class EventsUnavailable(Exception):
    def __init__(self, kind, why): super().__init__(f"{kind}: {why}"); self.kind = kind; self.why = why
def gh_runner(cmd, timeout=60):
    """PRODUCTION runner: `gh api …` via subprocess. Returns (returncode, stdout, stderr)."""
    r = subprocess.run(cmd, capture_output=True, text=True, timeout=timeout); return r.returncode, r.stdout, r.stderr
def retrieve_events(repo, runner=gh_runner, per_page=100, max_pages=3):
    """Read-only retrieval with pagination. Returns (events newest-first, provenance). Every failure mode raises EventsUnavailable(kind)."""
    out = []; prov = {"repo": repo, "endpoints": [], "retrieved_utc": utc(), "per_page": per_page, "pages_fetched": 0, "truncated_by_max_pages": False, "oldest_created_at": None}
    for page in range(1, max_pages + 1):
        ep = f"repos/{repo}/events?per_page={per_page}&page={page}"; prov["endpoints"].append(ep)
        try: rc, so, se = runner(["gh", "api", ep])
        except Exception as e: raise EventsUnavailable("TRANSPORT", repr(e)[:120])
        if rc != 0:
            m = re.search(r"HTTP (\d{3})", se or ""); code = int(m.group(1)) if m else None
            kind = "RATE-LIMITED" if (code == 403 and "rate limit" in (se or "").lower()) or code == 429 else "AUTH" if code == 401 else "NOT-FOUND" if code == 404 else "SERVER-ERROR" if code and code >= 500 else "HTTP"
            raise EventsUnavailable(kind, (se or "").strip()[:160])
        try: body = json.loads(so)
        except Exception as e: raise EventsUnavailable("MALFORMED", "response is not JSON: " + repr(e)[:80])
        if not isinstance(body, list) or not all(isinstance(x, dict) for x in body): raise EventsUnavailable("MALFORMED", "response is not a list of events")
        prov["pages_fetched"] += 1; out.extend(body)
        if len(body) < per_page: break
    else: prov["truncated_by_max_pages"] = True
    times = [str(e.get("created_at")) for e in out if e.get("created_at")]; prov["oldest_created_at"] = min(times) if times else None
    return out, prov
def authenticate_event(retained, live_events, repo, branch_ref, commit, feed_reaches_back_to=None):
    """v1's pure decision, unchanged: (outcome, why)."""
    if not isinstance(retained, dict) or retained.get("type") != "PushEvent": return "FORGED", "retained object is not a PushEvent"
    if (retained.get("repo") or {}).get("name") != repo: return "FORGED", f"retained event names repository {(retained.get('repo') or {}).get('name')!r}, not the pinned {repo!r}"
    pay = retained.get("payload") or {}
    if pay.get("ref") != branch_ref or not (pay.get("head") == commit or any(c.get("sha") == commit for c in pay.get("commits", []))): return "FORGED", "retained event does not deliver the approval commit to the protected ref"
    if live_events is None: return "UNAVAILABLE", "the live feed could not be retrieved; retry — nothing else changes"
    d = canon(retained)
    if not any(canon(e) == d for e in live_events):
        if feed_reaches_back_to is not None and str(retained.get("created_at")) < feed_reaches_back_to: return "EXPIRED", "the live feed no longer reaches the event's time; only an independent receipt taken inside the window can stand in"
        return "FORGED", "the retained event is not in the live feed of the pinned repository"
    qualifying = [e for e in live_events if e.get("type") == "PushEvent" and (e.get("payload") or {}).get("ref") == branch_ref and ((e.get("payload") or {}).get("head") == commit or any(c.get("sha") == commit for c in (e.get("payload") or {}).get("commits", [])))]
    earliest = min(qualifying, key=lambda e: e["created_at"])
    if canon(earliest) != d: return "FORGED", "an earlier qualifying event exists in the live feed; the retained one is not the earliest"
    return "AUTHENTIC", "retained event present verbatim in the live feed of the pinned repository, earliest qualifying"
def authenticate_event_live(retained, repo, runner, branch_ref, commit, per_page=100, max_pages=3):
    """Retrieve NOW, then decide. (outcome, why, provenance)."""
    try: live, prov = retrieve_events(repo, runner, per_page=per_page, max_pages=max_pages)
    except EventsUnavailable as e: return "UNAVAILABLE", f"{e.kind}: {e.why}", None
    o, why = authenticate_event(retained, live, repo, branch_ref, commit, feed_reaches_back_to=prov.get("oldest_created_at")); return o, why, prov
def write_events_receipt(path, events, provenance, origin):
    """The independent receipt (taken by the OPS session inside the window): events verbatim + provenance + origin + digest. Returns the path."""
    body = {"schema": "EVENTS-RECEIPT-1", "origin": origin, "provenance": provenance, "events": events, "events_sha256": hashlib.sha256(json.dumps(events, sort_keys=True, separators=(",", ":")).encode()).hexdigest(), "written_utc": utc()}
    Path(path).write_text(json.dumps(body, sort_keys=True, indent=1) + "\n"); return Path(path)
def _git(root, *a):
    r = subprocess.run(["git", *a], cwd=root, capture_output=True); return r.returncode, r.stdout
def remote_head(remote_url, ref):
    """The CURRENT head of `ref` at `remote_url`, obtained NOW with ls-remote (independent of every local ref). None if unreachable."""
    try: r = subprocess.run(["git", "ls-remote", "--exit-code", remote_url, ref], capture_output=True, text=True, timeout=60)
    except Exception: return None
    if r.returncode != 0: return None
    for l in r.stdout.splitlines():
        sha, name = (l.split("\t") + [""])[:2]
        if name == ref and re.fullmatch(r"[0-9a-f]{40}", sha): return sha
    return None
def _fetch_witness(root, remote_url, ref, head):
    rc, _ = _git(root, "fetch", "-q", remote_url, f"+{ref}:refs/witness/{ref.replace('refs/', '')}")
    return rc == 0 and subprocess.run(["git", "cat-file", "-e", head + "^{commit}"], cwd=root, capture_output=True).returncode == 0
def verify_events_receipt(receipt_path, root, remote_url, ref, retained_event, expected_origin):
    """(ok, why). The receipt must be added once by one commit and never touched; that commit an ancestor of the LIVE remote head; digest recomputes;
    origin equals the expected origin; the retained event is in it verbatim."""
    p = Path(receipt_path)
    try: rec = json.loads(p.read_text())
    except Exception as e: return False, f"RECEIPT-MALFORMED: {e!r}"[:160]
    if not isinstance(rec, dict) or rec.get("schema") != "EVENTS-RECEIPT-1" or not isinstance(rec.get("events"), list): return False, "RECEIPT-MALFORMED: not an EVENTS-RECEIPT-1"
    if hashlib.sha256(json.dumps(rec["events"], sort_keys=True, separators=(",", ":")).encode()).hexdigest() != rec.get("events_sha256"): return False, "RECEIPT-DIGEST: events digest does not recompute"
    origin = rec.get("origin") or {}
    if any(origin.get(k) != v for k, v in (expected_origin or {}).items()): return False, f"RECEIPT-ORIGIN: receipt origin {origin!r} is not the expected {expected_origin!r}"
    if not any(canon(e) == canon(retained_event) for e in rec["events"]): return False, "RECEIPT-EVENT-ABSENT: the retained event is not in the receipt verbatim"
    head = remote_head(remote_url, ref)
    if head is None: return False, "RETRY-REMOTE-UNAVAILABLE: the remote could not be asked for its head"
    if not _fetch_witness(root, remote_url, ref, head): return False, "RETRY-REMOTE-UNAVAILABLE: could not fetch the remote ref"
    rc, top = _git(root, "rev-parse", "--show-toplevel"); rel = p.resolve().relative_to(Path(top.decode().strip()).resolve()).as_posix()
    rc, adds = _git(root, "log", "--all", "--diff-filter=A", "--format=%H", "--", rel); adds = adds.decode().split()
    rc, touches = _git(root, "log", "--all", "--format=%H", "--", rel); touches = touches.decode().split()
    if len(adds) != 1 or touches != adds: return False, f"RECEIPT-NOT-FIRST: the receipt path was added or touched by {len(touches)} commits; the first receipt is final"
    c = adds[0]
    if subprocess.run(["git", "merge-base", "--is-ancestor", c, head], cwd=root, capture_output=True).returncode != 0: return False, f"RECEIPT-NOT-PUBLISHED: commit {c[:12]} is not an ancestor of the live remote head"
    rc, blob = _git(root, "cat-file", "-p", f"{c}:{rel}")
    if rc != 0 or blob != p.read_bytes(): return False, "RECEIPT-MODIFIED: on-disk bytes differ from the committed blob"
    return True, f"receipt added once by {c[:12]} (published at the live remote head {head[:12]}), origin {origin.get('actor')!r}, event present verbatim"

# ------------------------------------------------------------------ (b) history
def validate_continuation_v2(root, rel, open_commit, remote_url, ref, expected_head=None):
    """(ok, why, info). See the module docstring. The remote is ASKED (ls-remote); local refs and local HEAD are never trusted."""
    info = {"remote_url": remote_url, "ref": ref, "asked_utc": utc()}
    head = remote_head(remote_url, ref); info["remote_head"] = head
    if head is None: return False, "RETRY-REMOTE-UNAVAILABLE: the remote did not answer ls-remote; nothing governs until it does", info
    if expected_head is not None and expected_head != head: return False, f"STALE-EXPECTED-HEAD: supplied {expected_head[:12]} but the live remote head is {head[:12]}", info
    if not _fetch_witness(root, remote_url, ref, head): return False, "RETRY-REMOTE-UNAVAILABLE: could not fetch the remote ref's objects", info
    if not re.fullmatch(r"[0-9a-f]{40}", str(open_commit)) or subprocess.run(["git", "merge-base", "--is-ancestor", open_commit, head], cwd=root, capture_output=True).returncode != 0:
        return False, f"HISTORY-OPEN-NOT-PUBLISHED: open commit {str(open_commit)[:12]} is not an ancestor of the live remote head", info
    rc, out = _git(root, "log", "--reverse", "--format=%H", head, "--", rel); commits = out.decode().split(); info["remote_commits"] = commits
    if rc != 0 or not commits: return False, "HISTORY-NO-COMMITS on the remote ref", info
    if commits[0] != open_commit: return False, f"HISTORY-OPEN-COMMIT-MISMATCH: first remote commit touching the file is {commits[0][:12]}, not the open commit", info
    prev = b""
    for c in commits:
        rc, blob = _git(root, "cat-file", "-p", f"{c}:{rel}")
        if rc != 0: return False, f"HISTORY-DELETED-AT {c[:12]} on the remote ref", info
        if not blob.startswith(prev) or (len(blob) <= len(prev) and c != commits[0]): return False, f"HISTORY-NOT-AN-EXTENSION at {c[:12]}: the remote's committed blob does not extend the previous one", info
        prev = blob
    info["acknowledged_entries"] = sum(1 for l in prev.split(b"\n") if l)
    rc, local_head = _git(root, "rev-parse", "HEAD"); local_head = local_head.decode().strip()
    rc, unpub = _git(root, "rev-list", f"{head}..{local_head}"); info["local_commits_not_acknowledged"] = unpub.decode().split()
    cur = (Path(root) / rel).read_bytes()
    if cur != prev:
        if cur.startswith(prev): return False, f"PENDING-PUSH: the working tree extends the acknowledged history by {len(cur) - len(prev)} bytes that the remote has not acknowledged ({len(info['local_commits_not_acknowledged'])} local commits unpublished); push and retry — nothing in them governs", info
        return False, "HISTORY-DIVERGED: the working tree does not extend the history acknowledged by the remote (local reset/rebuild); refuse", info
    if info["local_commits_not_acknowledged"]: return False, "HISTORY-DIVERGED: local commits exist that the remote never acknowledged although the file bytes match; refuse until local state equals the published ref", info
    return True, f"append-only continuation from the published open commit; working tree equals the history acknowledged by the live remote head {head[:12]}", info
