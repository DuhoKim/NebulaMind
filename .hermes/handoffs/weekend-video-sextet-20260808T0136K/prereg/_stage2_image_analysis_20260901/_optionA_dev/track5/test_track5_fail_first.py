"""TRACK 5 FAIL-FIRST tests — codex's V24 findings N1, N2, N3, N5 (CODEX_SELRULE_V24_SEATB.md). Targets the SUCCESSORS (provenance_designs_v5,
run_configurations_v9, collector v25, builder v25) and was run FIRST against byte-copies of the V24 modules (import lines renamed only).
Classification of run 1, honestly: a case that fails only because a name is absent is MISSING-INTERFACE; a case that fails because the old code
returned the wrong outcome or raised the wrong exception is BEHAVIOURAL — stated per test in the receipt, not counted by unittest category.
Remotes are LOCAL BARE repositories (non-fast-forward denied); the gh runner is fixture-supplied — both labelled. Pinned V24 files are not edited."""
import json, os, sys, tempfile, unittest, hashlib, subprocess
from pathlib import Path
HERE = Path(__file__).resolve().parent; D = HERE.parent
for p in ("beacon_v2", "drand_only", "corpus_identity", "fourier_chirality", "track2"): sys.path.insert(0, str(D / p))
import provenance_designs_v5 as P, history_v2 as H
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
def pev(commit, before, n, created=None, commits=None):
    return {"type": "PushEvent", "id": f"h{n}", "created_at": created or f"2026-09-07T01:{n:02d}:00Z", "repo": {"name": REPO}, "payload": {"ref": REF, "before": before, "head": commit, "commits": commits or [{"sha": commit}]}}
def feed(events): return lambda cmd: (0, json.dumps(events if cmd[-1].endswith("page=1") else []), "")
def feeds(*pages_per_call):
    """a runner whose successive CALL SEQUENCES return different feeds (call k → pages_per_call[k]); models a feed that changes between the approval/open retrieval and the per-entry retrieval"""
    state = {"k": -1}
    def run(cmd):
        if cmd[-1].endswith("page=1"): state["k"] = min(state["k"] + 1, len(pages_per_call) - 1)
        ev = pages_per_call[state["k"]]; return 0, json.dumps(ev if cmd[-1].endswith("page=1") else []), ""
    return run
def honest_history(bare, work, n_entries=3):
    log = work / "collection_log.jsonl"; base = git(work, "rev-parse", "HEAD"); evs = []; prev = base; entries = [None, {"stage": "collector-collect", "outcome": "RETRY"}, {"stage": "builder-accept", "outcome": "ACCEPT-DRAND", "record_sha256": "c" * 64, "seed_hex": "d" * 64}][:n_entries]
    for n, e in enumerate(entries):
        if e is None: H.genesis(log, "a" * 64, "t", "b" * 64, 1)
        else: H.append(log, e)
        c = P.publish_entry(work, log.name, str(bare), REF, f"entry {n}"); evs.append(pev(c, prev, n)); prev = c
    return log, evs
class N2_Dispositions(unittest.TestCase):
    def test_N2a_empty_second_feed_is_retry_not_batch(self):                    # codex V24 N2: complete feed for approval/open, EMPTY feed on the per-entry retrieval
        bare, work = scaffold(); log, evs = honest_history(bare, work)
        ok, why, _ = P.validate_continuation_v5(work, log.name, str(bare), REF, evs[0], feeds(evs, []), REPO)
        self.assertFalse(ok); self.assertIn("EVIDENCE-UNAVAILABLE", why); self.assertNotIn("BATCH", why)
    def test_N2b_missing_middle_event_is_incomplete_evidence_not_batch(self):    # a delayed honest event: no evidence of a multi-commit delivery → retry within the window
        bare, work = scaffold(); log, evs = honest_history(bare, work)
        ok, why, _ = P.validate_continuation_v5(work, log.name, str(bare), REF, evs[0], feed([evs[0], evs[2]]), REPO)
        self.assertFalse(ok); self.assertIn("EVIDENCE-INCOMPLETE", why); self.assertNotIn("BATCH", why)
    def test_N2c_multi_commit_delivery_is_batch(self):                          # the feed itself shows several history commits delivered by one push → proven batch, terminal
        bare, work = scaffold(); log = work / "collection_log.jsonl"; base = git(work, "rev-parse", "HEAD")
        H.genesis(log, "a" * 64, "t", "b" * 64, 1); git(work, "add", log.name); git(work, "commit", "-q", "-m", "open"); c0 = git(work, "rev-parse", "HEAD")
        H.append(log, {"stage": "collector-collect", "outcome": "RETRY"}); git(work, "commit", "-q", "-am", "e1"); c1 = git(work, "rev-parse", "HEAD"); git(work, "push", "-q", "origin", "HEAD:" + REF)
        late = pev(c1, base, 9, commits=[{"sha": c0}, {"sha": c1}])
        ok, why, _ = P.validate_continuation_v5(work, log.name, str(bare), REF, late, feed([late]), REPO)
        self.assertFalse(ok); self.assertIn("BATCH", why)
class N3_ProducerPrecondition(unittest.TestCase):
    def test_N3_unrelated_unpublished_commit_refused_before_publishing(self):    # codex V24 N3: an unrelated local commit would ride along and break before == parent
        bare, work = scaffold(); log, evs = honest_history(bare, work, 1)
        (work / "unrelated").write_text("u"); git(work, "add", "unrelated"); git(work, "commit", "-q", "-m", "unrelated local commit")
        H.append(log, {"stage": "collector-collect", "outcome": "RETRY"})
        with self.assertRaises(SystemExit) as cm: P.publish_entry(work, log.name, str(bare), REF, "entry 1")
        self.assertIn("PUBLISH-UNRELATED-COMMITS", str(cm.exception)); self.assertEqual(git(bare, "rev-parse", REF), evs[0]["payload"]["head"], "nothing was pushed")
class N1_N5_Text(unittest.TestCase):
    def test_N1_residual_is_the_covenant(self):                                 # the residual must cover unpublished work/decisions BEFORE genesis publication AND BETWEEN later publications
        for p in (Path(os.environ["RULE_TEXT"]), Path(os.environ["DESIGN_TEXT"]), D / "track2" / "provenance_designs_v5.py"):
            t = p.read_text(encoding="utf-8"); self.assertIn("between later publications", t, p.name); self.assertIn("does not authenticate when", t, p.name)
    def test_N5_labels_and_sweep(self):
        r = Path(os.environ["RULE_TEXT"]).read_text(encoding="utf-8"); q = Path(os.environ["QUESTIONS_TEXT"]).read_text(); drv = (D / "fourier_chirality" / "run_configurations_v9.py").read_text()
        self.assertIn("3c. V25", r); self.assertNotIn("3c. V22", r); self.assertIn("coherent_attacks_v25.py", r); self.assertNotIn("`coherent_attacks.py` and add", r)
        self.assertIn("build_corpus_identity_v25.py", r); self.assertIn("beacon_record_drand_v25.py collect", r)
        self.assertIn("every history commit", q); self.assertIn("EVIDENCE-INCOMPLETE", q)                              # Q1 states the full live contract and the retry disposition
        for old in ("provenance_designs_v3", "provenance_designs_v4", "v7 on provenance", "v8 on provenance"): self.assertNotIn(old, drv, old)
        self.assertTrue((Path(os.environ["RULE_TEXT"]).parent / "TRACK_RECEIPTS_CLASSIFICATION_CORRECTION_20260907.md").is_file())   # N4: the correction note beside the pinned receipts
if __name__ == "__main__": unittest.main()
