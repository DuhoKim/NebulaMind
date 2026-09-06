"""TRACK 3 FAIL-FIRST tests — codex's V22 findings A–F (CODEX_SELRULE_V22_SEATB.md), run FIRST against byte-copies of the V22 modules
(provenance_designs_v3 = v2, run_configurations_v7 = v6, build_corpus_identity_v23 = v22, beacon_record_drand_v23 = v22), then against the
repaired successors. Behavioural cases reproduce codex's executed attacks; a case that fails only because an interface is missing is marked
MISSING-INTERFACE in its name. Remotes are LOCAL BARE repositories (non-fast-forward denied), the gh runner is fixture-supplied — labelled."""
import json, os, sys, tempfile, unittest, hashlib, subprocess, io, contextlib
from pathlib import Path
HERE = Path(__file__).resolve().parent; D = HERE.parent
for p in ("beacon_v2", "drand_only", "corpus_identity", "fourier_chirality", "track2"): sys.path.insert(0, str(D / p))
import provenance_designs_v3 as P, history_v2 as H, run_configurations_v7 as rc, build_corpus_identity_v23 as B, beacon_record_drand_v23 as BD, approval_witness_v4 as AW
import test_run_configurations_v7 as TF
def git(cwd, *a, check=True):
    r = subprocess.run(["git", *a], cwd=cwd, capture_output=True, text=True)
    if check and r.returncode: raise RuntimeError(r.stderr)
    return r.stdout.strip()
REF = "refs/heads/main"; REPO = "DuhoKim/NebulaMind"
def canon(e): return hashlib.sha256(json.dumps(e, sort_keys=True, separators=(",", ":")).encode()).hexdigest()
def feed(events): return lambda cmd: (0, json.dumps(events if cmd[-1].endswith("page=1") else []), "")
def scaffold():
    tmp = Path(tempfile.mkdtemp()); bare = tmp / "remote.git"; work = tmp / "work"
    subprocess.run(["git", "init", "-q", "--bare", str(bare)], check=True); git(bare, "config", "receive.denyNonFastforwards", "true")
    subprocess.run(["git", "clone", "-q", str(bare), str(work)], check=True, capture_output=True); git(work, "config", "user.email", "t@t"); git(work, "config", "user.name", "t")
    (work / "seed").write_text("x"); git(work, "add", "seed"); git(work, "commit", "-q", "-m", "init"); git(work, "push", "-q", "-u", "origin", "HEAD:" + REF)
    return bare, work
def ev_for(commit, created="2026-09-07T01:05:00Z", **pay):
    p = {"ref": REF, "head": commit, "commits": [{"sha": commit}]}; p.update(pay)
    return {"type": "PushEvent", "id": commit[:8], "created_at": created, "repo": {"name": REPO}, "payload": p}
class A_HistoryOpenAnchor(unittest.TestCase):
    def test_A_late_first_publication_of_a_rebuilt_history_is_refused(self):     # codex V22 A: publish a rebuilt 2-entry history as the FIRST commit and name it history-open
        bare, work = scaffold(); log = work / "collection_log.jsonl"
        H.genesis(log, "a" * 64, "t", "b" * 64, 1); H.append(log, {"stage": "builder-accept", "record_sha256": "c" * 64, "outcome": "ACCEPT-DRAND", "seed_hex": "d" * 64})
        git(work, "add", log.name); git(work, "commit", "-q", "-m", "late first publication"); oc = git(work, "rev-parse", "HEAD"); git(work, "push", "-q", "origin", "HEAD:" + REF)
        ok, why, _ = P.validate_continuation_v3(work, log.name, str(bare), REF, open_event=ev_for(oc), runner=feed([ev_for(oc)]), repo=REPO)
        self.assertFalse(ok, "a first history commit whose blob is not genesis-only must be refused"); self.assertIn("OPEN-NOT-GENESIS-ONLY", why)
    def test_A_open_commit_event_must_be_authentic_and_open_blob_genesis_only(self):
        bare, work = scaffold(); log = work / "collection_log.jsonl"; H.genesis(log, "a" * 64, "t", "b" * 64, 1)
        git(work, "add", log.name); git(work, "commit", "-q", "-m", "history-open"); oc = git(work, "rev-parse", "HEAD"); git(work, "push", "-q", "origin", "HEAD:" + REF)
        H.append(log, {"stage": "collector-collect", "outcome": "RETRY"}); git(work, "commit", "-q", "-am", "attempt 1"); c1 = git(work, "rev-parse", "HEAD"); git(work, "push", "-q", "origin", "HEAD:" + REF)
        H.append(log, {"stage": "builder-accept", "record_sha256": "c" * 64, "outcome": "ACCEPT-DRAND", "seed_hex": "d" * 64}); git(work, "commit", "-q", "-am", "accept"); c2 = git(work, "rev-parse", "HEAD"); git(work, "push", "-q", "origin", "HEAD:" + REF)
        live = [ev_for(oc), ev_for(c1, "2026-09-07T01:06:00Z"), ev_for(c2, "2026-09-07T01:07:00Z")]
        ok, why, info = P.validate_continuation_v3(work, log.name, str(bare), REF, open_event=ev_for(oc), runner=feed(live), repo=REPO); self.assertTrue(ok, why); self.assertEqual(info["entries_per_commit"], [1, 1, 1])
        forged_open = ev_for(oc, "2000-01-01T00:00:00Z"); forged_open["id"] = "invented"                   # an open event not in the live feed
        ok, why, _ = P.validate_continuation_v3(work, log.name, str(bare), REF, open_event=forged_open, runner=feed(live), repo=REPO); self.assertFalse(ok); self.assertIn("OPEN-EVENT", why)
        ok, why, _ = P.validate_continuation_v3(work, log.name, str(bare), REF, open_event=ev_for("0" * 40), runner=feed(live), repo=REPO); self.assertFalse(ok)   # names a commit that is not the first history commit
class B_ProducerBoundary(unittest.TestCase):
    def test_B_publish_entry_acknowledges_before_returning_and_refuses_batches(self):   # codex V22 B: one acknowledged publication per entry
        bare, work = scaffold(); log = work / "collection_log.jsonl"; H.genesis(log, "a" * 64, "t", "b" * 64, 1)
        oc = P.publish_entry(work, log.name, str(bare), REF, "history-open"); self.assertEqual(git(bare, "rev-parse", REF), oc)
        H.append(log, {"stage": "collector-collect", "outcome": "RETRY"}); c1 = P.publish_entry(work, log.name, str(bare), REF, "attempt 1"); self.assertEqual(git(bare, "rev-parse", REF), c1)
        H.append(log, {"stage": "collector-collect", "outcome": "RETRY"}); H.append(log, {"stage": "builder-accept", "record_sha256": "c" * 64, "outcome": "ACCEPT-DRAND", "seed_hex": "d" * 64})
        with self.assertRaises(SystemExit) as cm: P.publish_entry(work, log.name, str(bare), REF, "two at once")            # two unpublished entries: refused, nothing pushed
        self.assertIn("PUBLISH-BATCH", str(cm.exception)); self.assertEqual(git(bare, "rev-parse", REF), c1)
        with self.assertRaises(SystemExit) as cm: P.publish_entry(work, log.name, str(bare) + ".missing", REF, "x")            # remote down: PENDING-PUSH, refuse to proceed
        self.assertIn("PENDING-PUSH", str(cm.exception))
    def test_B_validator_requires_one_entry_per_acknowledged_commit(self):
        bare, work = scaffold(); log = work / "collection_log.jsonl"; H.genesis(log, "a" * 64, "t", "b" * 64, 1)
        git(work, "add", log.name); git(work, "commit", "-q", "-m", "history-open"); oc = git(work, "rev-parse", "HEAD"); git(work, "push", "-q", "origin", "HEAD:" + REF)
        H.append(log, {"stage": "collector-collect", "outcome": "RETRY"}); H.append(log, {"stage": "builder-accept", "record_sha256": "c" * 64, "outcome": "ACCEPT-DRAND", "seed_hex": "d" * 64})
        git(work, "commit", "-q", "-am", "two entries in one commit"); c1 = git(work, "rev-parse", "HEAD"); git(work, "push", "-q", "origin", "HEAD:" + REF)
        ok, why, _ = P.validate_continuation_v3(work, log.name, str(bare), REF, open_event=ev_for(oc), runner=feed([ev_for(oc), ev_for(c1, "2026-09-07T01:06:00Z")]), repo=REPO)
        self.assertFalse(ok, "a batch commit of two entries must not satisfy per-entry acknowledgment"); self.assertIn("BATCH", why)
    def test_B_collector_cli_publishes_each_entry_when_asked(self):              # the collector's own producer boundary (--publish-remote/--publish-ref)
        import verify_drand_v2 as vd
        from datetime import timedelta
        bare, work = scaffold(); log = work / "collection_log.jsonl"; REAL = json.loads((D / "drand_only" / "round_6441924_api.drand.sh.json").read_text()); BODY = json.dumps(REAL).encode()
        TP = vd.round_time(6441924); TS = BD.fmt(TP - timedelta(seconds=600)); RD = "b" * 64; stmt = work / "s.txt"; stmt.write_bytes(f"x {RD} {TS}".encode()); saved = BD.EXCLUDED_ROUNDS; BD.EXCLUDED_ROUNDS = (6440756,)
        import urllib.request, unittest.mock as um
        class _R(io.BytesIO):
            def __enter__(self): return self
            def __exit__(self, *a): return False
        def net(url):
            for h in vd.RELAYS:
                if url == vd.round_url(h, 6441924): return BODY
            raise OSError("404")
        try:
            with um.patch.object(BD, "datetime") as dt, um.patch.object(urllib.request, "urlopen", lambda url, timeout=30: _R(net(url))):
                from datetime import datetime; dt.now.return_value = TP + timedelta(minutes=1); dt.strptime = datetime.strptime
                rcode = BD.main(["collect", "--t-sign", TS, "--rule-sha256", RD, "--signature-statement", str(stmt), "--out", str(work / "rec.json"), "--log", str(log), "--publish-remote", str(bare), "--publish-ref", REF])
        finally: BD.EXCLUDED_ROUNDS = saved
        self.assertEqual(rcode, 0); commits = git(work, "log", "--reverse", "--format=%H", "--", log.name).split(); self.assertEqual(len(commits), 2, "genesis and the collect entry each published")   # one commit per entry, acknowledged
        self.assertEqual(git(bare, "rev-parse", REF), commits[-1])
class C_OnePredicate(unittest.TestCase):
    def test_C_ancestry_delivered_push_is_authentic_in_composed_mode(self):      # codex V22 C: the composed predicate must equal W3 (before..head)
        bare, work = scaffold(); base = git(work, "rev-parse", "HEAD"); (work / "a").write_text("a"); git(work, "add", "a"); git(work, "commit", "-q", "-m", "approval"); commit = git(work, "rev-parse", "HEAD")
        (work / "l").write_text("l"); git(work, "add", "l"); git(work, "commit", "-q", "-m", "later"); head = git(work, "rev-parse", "HEAD"); git(work, "push", "-q", "origin", "HEAD:" + REF)
        anc = ev_for(head, before=base, commits=[{"sha": head}])                                                # the approval commit is inside before..head only
        self.assertTrue(AW.delivers(anc, commit, REF, work))
        self.assertEqual(P.authenticate_event(anc, [anc], REPO, REF, commit, root=work)[0], "AUTHENTIC")
class D_ControlFailureLogged(unittest.TestCase):
    def test_D_control_failure_appends_a_named_entry(self):                     # codex V22 D: CONTROL FAILURE returned False past the wrapper
        import test_build_corpus_identity_v22 as TB, unittest.mock as um, csv
        t = TB.T("test_accepted_witnessed_locked_history"); t.setUp()
        try:
            B.COLLECTION_LOG = TB.B19.COLLECTION_LOG; B.ADOPTION_FILE = TB.B19.ADOPTION_FILE; B.WITNESS_REMOTE_REF = TB.B19.WITNESS_REMOTE_REF; B.WITNESS_REMOTE_URL = TB.B19.WITNESS_REMOTE_URL; B.APPROVAL_GLOB = TB.B19.APPROVAL_GLOB; B.BRANCH_REF = TB.B19.BRANCH_REF; B.EVENTS = TB.B19.EVENTS; B.WITNESS_FETCH = True
            excl = D / "corpus_identity" / "dryrun_identities_to_exclude_20260905.txt"; bad = t.tmp / "bad_control.csv"; bad.write_text("GZ1_OBJID,G\n1,1\n")
            real_open = open
            def fake_open(p, *a, **k):
                return real_open(bad, *a, **k) if str(p).endswith("VALIDATION_SELECTION_V29_20260905.csv") else real_open(p, *a, **k)
            saved = BD.EXCLUDED_ROUNDS; BD.EXCLUDED_ROUNDS = (6440756,)                                     # the exhibit round is admissible only inside this fixture
            with um.patch("builtins.open", fake_open), contextlib.redirect_stdout(io.StringIO()):
                res = B.build(out_dir=t.tmp / "out", beacon_record_path=t.rec, exclude_path=excl, rule_sha256=TB.D, signature_statement=t.stmt, fetch=t.n, now=TB.SOON)
            self.assertFalse(res); self.assertEqual(H.validate(B.COLLECTION_LOG)[-1]["stage"], "builder-control-refusal")
        finally: BD.EXCLUDED_ROUNDS = saved; t.tearDown()
class E_RenderEndLast(unittest.TestCase):
    def test_E_render_end_must_be_the_last_relevant_record(self):                # codex V22 E
        rows = [{"objid": "1", "g": 1, "tensor_sha256": rc.SENTINEL_SHA256}]; rj = Path(tempfile.mkdtemp()) / "rj.jsonl"
        rj.write_text(json.dumps({"event": "render-end", "refused_sentinel": 1}) + "\n" + json.dumps({"objid": "1", "status": "REFUSED", "sentinel": True, "tensor_sha256": rc.SENTINEL_SHA256, "reason": "x"}) + "\n")
        with self.assertRaises(rc.DataIntegrityFail) as cm: rc.reconcile_sentinels(rows, rj)
        self.assertIn("RENDER-JOURNAL", str(cm.exception))
class F_FeedSemantics(unittest.TestCase):
    def test_F_empty_feed_is_not_forged_and_every_failure_kind_is_exercised(self):   # codex V22 F: an empty feed cannot convict; 404/418/429 paths
        e = ev_for("a" * 40)
        self.assertEqual(P.authenticate_event_live(e, REPO, feed([]), REF, "a" * 40)[0], "UNAVAILABLE")          # empty feed: no evidence either way → RETRY, never FORGED
        def http(code, msg): return lambda cmd: (1, "", f"gh: HTTP {code}: {msg}")
        for code, msg, kind in ((404, "Not Found", "NOT-FOUND"), (418, "teapot", "HTTP"), (429, "too many", "RATE-LIMITED")):
            with self.assertRaises(P.EventsUnavailable) as cm: P.retrieve_events(REPO, http(code, msg))
            self.assertEqual(cm.exception.kind, kind)
    def test_F_questions_text_states_30_days_and_option_B_not_implemented(self):
        q = Path(os.environ["QUESTIONS_TEXT"]).read_text(); self.assertNotIn("90 days", q); self.assertIn("30 days", q); self.assertIn("NOT IMPLEMENTED", q)
if __name__ == "__main__": unittest.main()
