"""TRACK 6 FAIL-FIRST tests — codex's V25 findings P1, P2, P3, P4 (CODEX_SELRULE_V25_SEATB.md). Targets the SUCCESSORS (provenance_designs_v6,
run_configurations_v10, collector v26, builder v26); run FIRST against byte-copies of the V25 modules (import lines renamed only), classified per test.
Remotes are LOCAL BARE repositories (non-fast-forward denied); the gh runner is fixture-supplied — both labelled. Pinned V25 files are not edited."""
import json, os, sys, tempfile, unittest, hashlib, subprocess
from pathlib import Path
HERE = Path(__file__).resolve().parent; D = HERE.parent
for p in ("beacon_v2", "drand_only", "corpus_identity", "fourier_chirality", "track2"): sys.path.insert(0, str(D / p))
import provenance_designs_v6 as P, history_v2 as H
def git(cwd, *a, check=True):
    r = subprocess.run(["git", *a], cwd=cwd, capture_output=True, text=True)
    if check and r.returncode: raise RuntimeError(r.stderr)
    return r.stdout.strip()
REF = "refs/heads/main"; REPO = "DuhoKim/NebulaMind"
def scaffold():
    tmp = Path(tempfile.mkdtemp()); bare = tmp / "remote.git"; work = tmp / "work"
    subprocess.run(["git", "init", "-q", "--bare", str(bare)], check=True); git(bare, "config", "receive.denyNonFastforwards", "true")
    subprocess.run(["git", "clone", "-q", str(bare), str(work)], check=True, capture_output=True); git(work, "config", "user.email", "t@t"); git(work, "config", "user.name", "t")
    (work / "seed").write_text("x"); git(work, "add", "seed"); git(work, "commit", "-q", "-m", "init"); git(work, "push", "-q", "-u", "origin", "HEAD:" + REF)
    return bare, work
def pev(commit, before, n, created=None, commits="own"):
    e = {"type": "PushEvent", "id": f"h{n}", "created_at": created or f"2026-09-07T01:{n:02d}:00Z", "repo": {"name": REPO}, "payload": {"ref": REF, "before": before, "head": commit}}
    if commits == "own": e["payload"]["commits"] = [{"sha": commit}]
    elif commits is not None: e["payload"]["commits"] = commits
    return e
def feed(events): return lambda cmd: (0, json.dumps(events if cmd[-1].endswith("page=1") else []), "")
def honest_history(bare, work, n_entries=3):
    log = work / "collection_log.jsonl"; base = git(work, "rev-parse", "HEAD"); evs = []; prev = base; entries = [None, {"stage": "collector-collect", "outcome": "RETRY"}, {"stage": "builder-accept", "outcome": "ACCEPT-DRAND", "record_sha256": "c" * 64, "seed_hex": "d" * 64}][:n_entries]
    for n, e in enumerate(entries):
        if e is None: H.genesis(log, "a" * 64, "t", "b" * 64, 1)
        else: H.append(log, e)
        c = P.publish_entry(work, log.name, str(bare), REF, f"entry {n}"); evs.append(pev(c, prev, n)); prev = c
    return log, evs
class P1_AncestryBatch(unittest.TestCase):
    def test_P1_batch_proven_by_ancestry_without_commits_list_is_terminal(self):   # codex V25 P1: GitHub PushEvents may omit payload.commits; before..head still proves the batch
        bare, work = scaffold(); log = work / "collection_log.jsonl"; base = git(work, "rev-parse", "HEAD")
        H.genesis(log, "a" * 64, "t", "b" * 64, 1); git(work, "add", log.name); git(work, "commit", "-q", "-m", "open"); c0 = git(work, "rev-parse", "HEAD")
        H.append(log, {"stage": "collector-collect", "outcome": "RETRY"}); git(work, "commit", "-q", "-am", "e1"); c1 = git(work, "rev-parse", "HEAD")
        H.append(log, {"stage": "builder-accept", "outcome": "ACCEPT-DRAND", "record_sha256": "c" * 64, "seed_hex": "d" * 64}); git(work, "commit", "-q", "-am", "e2"); c2 = git(work, "rev-parse", "HEAD"); git(work, "push", "-q", "origin", "HEAD:" + REF)
        late = pev(c2, base, 9, commits=None)                                                                   # one push, before..head covers c0..c2, NO commits list
        ok, why, _ = P.validate_continuation_v6(work, log.name, str(bare), REF, late, feed([late]), REPO)
        self.assertFalse(ok); self.assertIn("HISTORY-PUBLICATION-BATCH", why); self.assertNotIn("INCOMPLETE", why)
class P2_AbsenceIsNotForgery(unittest.TestCase):
    def test_P2_approval_event_absent_from_a_covering_feed_is_retry_not_forged(self):   # codex V25 P2
        e = pev("a" * 40, "b" * 40, 5); other = pev("c" * 40, "d" * 40, 1)                                       # the feed covers e's time (older event present) but lacks e
        o, why = P.authenticate_event(e, [other], REPO, REF, "a" * 40, feed_reaches_back_to=other["created_at"])
        self.assertEqual(o, "INCOMPLETE", why)
        contradict = {**e, "id": "different-bytes"}                                                                # a push delivering the same commit with different bytes: affirmative contradiction
        o, why = P.authenticate_event(e, [other, contradict], REPO, REF, "a" * 40); self.assertEqual(o, "FORGED")
        o, why = P.authenticate_event(e, [other, e], REPO, REF, "a" * 40); self.assertEqual(o, "AUTHENTIC")
    def test_P2_open_event_absent_is_retry_in_the_driver_shape(self):            # the open-event stage returns a RETRY-classed disposition, uniformly
        bare, work = scaffold(); log, evs = honest_history(bare, work)
        ok, why, _ = P.validate_continuation_v6(work, log.name, str(bare), REF, evs[0], feed([evs[1], evs[2]]), REPO)
        self.assertFalse(ok); self.assertTrue(why.startswith("EVIDENCE-"), why)                                       # the open-event stage speaks the uniform EVIDENCE-* vocabulary (here EXPIRED: the feed's oldest event is later than the open event; no receipt path exists for it)
        ok, why, _ = P.validate_continuation_v6(work, log.name, str(bare), REF, evs[0], feed([]), REPO)
        self.assertFalse(ok); self.assertTrue(why.startswith("EVIDENCE-UNAVAILABLE"), why)
class P3_P4_Text(unittest.TestCase):
    def test_P3_sweep(self):
        r = Path(os.environ["RULE_TEXT"]).read_text(encoding="utf-8"); t2 = Path(os.environ["DESIGN_TEXT"]).read_text(encoding="utf-8")
        drv = (D / "fourier_chirality" / "run_configurations_v10.py").read_text(); insp = (D / "track1" / "coherent_attacks_v26.py").read_text()
        self.assertNotIn("on the V22 candidate", r); self.assertNotIn("offered with their costs", t2); self.assertNotIn("rejected push = DIVERGED, dead", t2)
        for old in ("track-2 v2", "validate_continuation_v2", "provenance_designs_v5", "v9 on provenance"): self.assertNotIn(old, drv, old)
        self.assertNotIn("driver v6", insp); self.assertNotIn("V22 inspection", insp); self.assertIn("V26", insp)
    def test_P4_covenant_in_the_questions_file(self):
        q = Path(os.environ["QUESTIONS_TEXT"]).read_text(encoding="utf-8"); self.assertIn("does not authenticate when", q); self.assertIn("between later publications", q)
if __name__ == "__main__": unittest.main()
