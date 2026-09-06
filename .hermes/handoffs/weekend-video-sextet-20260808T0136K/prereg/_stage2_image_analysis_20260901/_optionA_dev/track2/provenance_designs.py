"""TRACK 2 (Blanc 20:45 KST) — RECOMMENDED, UNADOPTED designs for the two provenance boundaries codex's V21 review left open, as EXECUTABLE
exhibits with the trust they rely on stated. NOTHING here is wired into the production driver (run_configurations_v6 does not import it).

(a) AUTHENTIC GITHUB EVENT VALIDATION — `authenticate_event(retained_event, live_events, repo, branch_ref, commit)`:
    the retained PushEvent must appear VERBATIM (canonical SHA-256 equal) in a LIVE retrieval of the pinned repository's events, must name the
    pinned repository (`repo.name`), the protected ref and the approval commit, and must be the EARLIEST qualifying event in that retrieval.
    Live retrieval in production = `approval_witness_v4.github_events` (`gh api repos/<repo>/events`, authenticated CLI). Outcomes:
    AUTHENTIC | FORGED (absent from the live feed while the feed still covers the event's time) | UNAVAILABLE (API error) | EXPIRED (the feed no
    longer reaches back to created_at — GitHub serves ~90 days / 300 events; then only a second, independent retrieval receipt can stand in).
    TRUSTED afterwards: GitHub's server clock and feed integrity; the authenticity of the `gh` session. NOT trusted: the identity's retained bytes.
    In the exhibit the live feed is FIXTURE-SUPPLIED — labelled so; it demonstrates the decision, not a real remote service.
(b) EXTERNALLY WITNESSED HISTORY CONTINUATION — `validate_continuation(repo_root, log_relpath, open_commit)`:
    the history file's FIRST commit must be `open_commit` (the "history-open" commit, pushed to the protected branch and witnessed by its own
    server-side PushEvent like the approval record — that is the external anchor); every later commit touching the file must carry a blob that is
    a strict byte-prefix EXTENSION of the previous blob (append-only, verified through git, not through the file's own hashes); the working-tree
    bytes must extend the last committed blob. A rebuilt history (fresh genesis) is not an extension; a deleted suffix is shorter than the last
    committed blob; a reset before the first freeze is visible because the earlier commits cannot be removed from a protected branch.
    TRUSTED afterwards: branch protection (no force push, no deletion — Duho's GitHub setting) and the PushEvent for the open commit. NOT trusted:
    the file's own chain, the operator's clock. COST: every collector/builder attempt is committed and pushed as it happens (one commit per entry).
"""
from __future__ import annotations
import hashlib, json, subprocess
from pathlib import Path
def canon(e): return hashlib.sha256(json.dumps(e, sort_keys=True, separators=(",", ":")).encode()).hexdigest()

def authenticate_event(retained, live_events, repo, branch_ref, commit, feed_reaches_back_to=None):
    """(outcome, why). live_events: the events retrieved NOW from the pinned repo (production: approval_witness_v4.github_events()[0])."""
    if not isinstance(retained, dict) or retained.get("type") != "PushEvent": return "FORGED", "retained object is not a PushEvent"
    if (retained.get("repo") or {}).get("name") != repo: return "FORGED", f"retained event names repository {(retained.get('repo') or {}).get('name')!r}, not the pinned {repo!r}"
    pay = retained.get("payload") or {}
    if pay.get("ref") != branch_ref or not (pay.get("head") == commit or any(c.get("sha") == commit for c in pay.get("commits", []))): return "FORGED", "retained event does not deliver the approval commit to the protected ref"
    if live_events is None: return "UNAVAILABLE", "the live feed could not be retrieved; retry — nothing else changes"
    d = canon(retained)
    if not any(canon(e) == d for e in live_events):
        if feed_reaches_back_to is not None and str(retained.get("created_at")) < feed_reaches_back_to: return "EXPIRED", "the live feed no longer reaches the event's time; only an independent second retrieval receipt can stand in"
        return "FORGED", "the retained event is not in the live feed of the pinned repository"
    qualifying = [e for e in live_events if e.get("type") == "PushEvent" and (e.get("payload") or {}).get("ref") == branch_ref and ((e.get("payload") or {}).get("head") == commit or any(c.get("sha") == commit for c in (e.get("payload") or {}).get("commits", [])))]
    earliest = min(qualifying, key=lambda e: e["created_at"])
    if canon(earliest) != d: return "FORGED", "an earlier qualifying event exists in the live feed; the retained one is not the earliest"
    return "AUTHENTIC", "retained event present verbatim in the live feed of the pinned repository, earliest qualifying"

def _git(root, *a):
    r = subprocess.run(["git", *a], cwd=root, capture_output=True); return r.returncode, r.stdout
def validate_continuation(root, rel, open_commit):
    """(ok, why, commits). Append-only continuation of the history file through git, anchored at open_commit."""
    rc_, out = _git(root, "log", "--reverse", "--format=%H", "--", rel)
    commits = out.decode().split()
    if rc_ != 0 or not commits: return False, "HISTORY-NO-COMMITS", commits
    if commits[0] != open_commit: return False, f"HISTORY-OPEN-COMMIT-MISMATCH: first commit touching the file is {commits[0][:12]}, not the witnessed open commit {open_commit[:12]}", commits
    prev = b""
    for c in commits:
        rc_, blob = _git(root, "cat-file", "-p", f"{c}:{rel}")
        if rc_ != 0: return False, f"HISTORY-DELETED-AT {c[:12]}", commits
        if not blob.startswith(prev) or len(blob) <= len(prev) and c != commits[0]: return False, f"HISTORY-NOT-AN-EXTENSION at {c[:12]}: the committed blob does not extend the previous one (rebuilt or truncated)", commits
        prev = blob
    cur = (Path(root) / rel).read_bytes()
    if not cur.startswith(prev) or len(cur) < len(prev): return False, "HISTORY-WORKING-TREE-NOT-AN-EXTENSION: on-disk bytes do not extend the last committed blob (deleted suffix or rebuild)", commits
    return True, "append-only continuation from the witnessed open commit; working tree extends the last committed blob", commits
