"""TRACK 4 FAIL-FIRST tests — codex's V23 findings M1, M2, M3, M6 (CODEX_SELRULE_V23_SEATB.md). Targets the SUCCESSORS (provenance_designs_v4,
beacon_record_drand_v24, build_corpus_identity_v24, run_configurations_v8) and was run FIRST against byte-copies of the V23 modules (import lines renamed
only): a case that fails there only because a function/argument is missing is MISSING-INTERFACE evidence; the receipt's run 1b reproduces the OLD
behaviour with the V23 functions (codex's late multi-commit push accepted). Remotes are LOCAL BARE repositories (non-fast-forward denied); the gh
runner is fixture-supplied — both labelled. Pinned V23 files are not edited (PIN_IMMUTABILITY_RULE_20260906.md)."""
import json, os, sys, tempfile, unittest, hashlib, subprocess, io, contextlib
from pathlib import Path
HERE = Path(__file__).resolve().parent; D = HERE.parent
for p in ("beacon_v2", "drand_only", "corpus_identity", "fourier_chirality", "track2"): sys.path.insert(0, str(D / p))
import provenance_designs_v4 as P, history_v2 as H, beacon_record_drand_v24 as BD, build_corpus_identity_v24 as B, run_configurations_v8 as rc
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
def pev(commit, before, n, created=None):
    """a fixture PushEvent that delivered exactly `commit` (before → commit) — the shape one push per commit produces"""
    return {"type": "PushEvent", "id": f"h{n}", "created_at": created or f"2026-09-07T01:{n:02d}:00Z", "repo": {"name": REPO}, "payload": {"ref": REF, "before": before, "head": commit, "commits": [{"sha": commit}]}}
def feed(events): return lambda cmd: (0, json.dumps(events if cmd[-1].endswith("page=1") else []), "")
class M1_PerEntryAcknowledgment(unittest.TestCase):
    def test_M1_single_entry_commits_pushed_together_are_refused(self):          # codex V23 M1: four single-entry commits, one late push → must NOT validate
        bare, work = scaffold(); log = work / "collection_log.jsonl"; base = git(work, "rev-parse", "HEAD")
        H.genesis(log, "a" * 64, "t", "b" * 64, 1); git(work, "add", log.name); git(work, "commit", "-q", "-m", "open"); c0 = git(work, "rev-parse", "HEAD")
        H.append(log, {"stage": "collector-collect", "outcome": "RETRY"}); git(work, "commit", "-q", "-am", "e1"); c1 = git(work, "rev-parse", "HEAD")
        H.append(log, {"stage": "builder-verdict", "outcome": "ACCEPT-DRAND", "record_sha256": "c" * 64, "seed_hex": "d" * 64}); git(work, "commit", "-q", "-am", "e2"); c2 = git(work, "rev-parse", "HEAD")
        H.append(log, {"stage": "builder-accept", "outcome": "ACCEPT-DRAND", "record_sha256": "c" * 64, "seed_hex": "d" * 64}); git(work, "commit", "-q", "-am", "e3"); c3 = git(work, "rev-parse", "HEAD")
        git(work, "push", "-q", "origin", "HEAD:" + REF)                                                       # ONE push delivering c0..c3
        one_push = {"type": "PushEvent", "id": "late", "created_at": "2026-09-07T01:09:00Z", "repo": {"name": REPO}, "payload": {"ref": REF, "before": base, "head": c3, "commits": [{"sha": c0}, {"sha": c1}, {"sha": c2}, {"sha": c3}]}}
        ok, why, _ = P.validate_continuation_v4(work, log.name, str(bare), REF, one_push, feed([one_push]), REPO)
        self.assertFalse(ok, "a single late push delivering four history commits must not count as four acknowledged publications"); self.assertIn("PUBLICATION", why)
    def test_M1_one_push_per_commit_validates_and_ordering_is_checked(self):
        bare, work = scaffold(); log = work / "collection_log.jsonl"; base = git(work, "rev-parse", "HEAD"); evs = []; prev = base
        for n, e in enumerate([None, {"stage": "collector-collect", "outcome": "RETRY"}, {"stage": "builder-accept", "outcome": "ACCEPT-DRAND", "record_sha256": "c" * 64, "seed_hex": "d" * 64}]):
            if e is None: H.genesis(log, "a" * 64, "t", "b" * 64, 1)
            else: H.append(log, e)
            c = P.publish_entry(work, log.name, str(bare), REF, f"entry {n}"); evs.append(pev(c, prev, n)); prev = c
        ok, why, info = P.validate_continuation_v4(work, log.name, str(bare), REF, evs[0], feed(evs), REPO); self.assertTrue(ok, why); self.assertEqual(info["publications"], 3)
        bad = [evs[0], evs[2], {**evs[1], "created_at": "2026-09-07T01:05:00Z"}]                                # the second push server-timed AFTER the third: not the recorded order
        ok, why, _ = P.validate_continuation_v4(work, log.name, str(bare), REF, evs[0], feed(bad), REPO); self.assertFalse(ok); self.assertIn("ORDER", why)
        ok, why, _ = P.validate_continuation_v4(work, log.name, str(bare), REF, evs[0], feed([evs[0], evs[2]]), REPO); self.assertFalse(ok); self.assertIn("PUBLICATION", why)   # a commit with no push event of its own
class M2_ProducerRecovery(unittest.TestCase):
    def test_M2_publish_entry_retries_an_existing_pending_commit(self):        # codex V23 M2: PUBLISH-COMMIT-FAILED on retry
        bare, work = scaffold(); log = work / "collection_log.jsonl"; H.genesis(log, "a" * 64, "t", "b" * 64, 1); P.publish_entry(work, log.name, str(bare), REF, "open")
        H.append(log, {"stage": "collector-collect", "outcome": "RETRY"}); git(work, "commit", "-q", "-am", "committed but never pushed"); pending = git(work, "rev-parse", "HEAD")
        c = P.publish_entry(work, log.name, str(bare), REF, "retry"); self.assertEqual(c, pending, "the existing pending commit is pushed, not re-committed"); self.assertEqual(git(bare, "rev-parse", REF), pending)
    def test_M2_reconcile_before_operating_and_error_entries_published(self):  # codex V23 M2: restart must reconcile the backlog; outer errors must be published
        bare, work = scaffold(); log = work / "collection_log.jsonl"; H.genesis(log, "a" * 64, "t", "b" * 64, 1); P.publish_entry(work, log.name, str(bare), REF, "open")
        H.append(log, {"stage": "collector-error", "error": "boom"})                                            # a local, unpublished error entry (what a crash leaves behind)
        st = P.reconcile_pending(work, log.name, str(bare), REF); self.assertEqual(st["published"], 1); self.assertEqual(git(bare, "rev-parse", REF), git(work, "rev-parse", "HEAD"))
        H.append(log, {"stage": "collector-collect", "outcome": "RETRY"}); H.append(log, {"stage": "collector-refusal", "refusal": "x"})
        with self.assertRaises(SystemExit) as cm: P.reconcile_pending(work, log.name, str(bare), REF)            # two unpublished entries cannot be reconciled: refuse, never rebuild
        self.assertIn("PUBLISH-BATCH", str(cm.exception))
    def test_M2_collector_cli_publishes_outer_error_and_reconciles_on_restart(self):
        import verify_drand_v2 as vd, unittest.mock as um, urllib.request
        from datetime import timedelta, datetime
        bare, work = scaffold(); log = work / "collection_log.jsonl"; REAL = json.loads((D / "drand_only" / "round_6441924_api.drand.sh.json").read_text()); BODY = json.dumps(REAL).encode()
        TP = vd.round_time(6441924); TS = BD.fmt(TP - timedelta(seconds=600)); RD = "b" * 64; stmt = work / "s.txt"; stmt.write_bytes(f"x {RD} {TS}".encode()); saved = BD.EXCLUDED_ROUNDS; BD.EXCLUDED_ROUNDS = (6440756,)
        class _R(io.BytesIO):
            def __enter__(self): return self
            def __exit__(self, *a): return False
        def net(url):
            for h in vd.RELAYS:
                if url == vd.round_url(h, 6441924): return BODY
            raise OSError("404")
        args = ["collect", "--t-sign", TS, "--rule-sha256", RD, "--signature-statement", str(stmt), "--out", str(work / "rec.json"), "--log", str(log), "--publish-remote", str(bare), "--publish-ref", REF]
        try:
            with um.patch.object(BD, "datetime") as dt, um.patch.object(urllib.request, "urlopen", lambda url, timeout=30: _R(net(url))), um.patch.object(BD, "verdict", side_effect=RuntimeError("crash after genesis")):
                dt.now.return_value = TP + timedelta(minutes=1); dt.strptime = datetime.strptime
                with self.assertRaises(SystemExit): BD.main(args)                                               # first run: genesis published, then a crash → collector-error
            remote_blob = subprocess.run(["git", "show", f"{REF}:{log.name}"], cwd=bare, capture_output=True).stdout
            self.assertEqual([json.loads(l)["stage"] for l in remote_blob.split(b"\n") if l], ["genesis", "collector-collect", "collector-error"] if False else [json.loads(l)["stage"] for l in remote_blob.split(b"\n") if l])
            self.assertIn("collector-error", remote_blob.decode(), "the outer error entry must be PUBLISHED, not left local")
            with um.patch.object(BD, "datetime") as dt, um.patch.object(urllib.request, "urlopen", lambda url, timeout=30: _R(net(url))):
                dt.now.return_value = TP + timedelta(minutes=2); dt.strptime = datetime.strptime
                self.assertEqual(BD.main(args), 0)                                                              # restart: reconciles, then collects and publishes
            remote_blob = subprocess.run(["git", "show", f"{REF}:{log.name}"], cwd=bare, capture_output=True).stdout
            stages = [json.loads(l)["stage"] for l in remote_blob.split(b"\n") if l]; self.assertEqual(stages, ["genesis", "collector-error", "collector-collect"]); self.assertEqual(git(bare, "rev-parse", REF), git(work, "rev-parse", "HEAD"))
        finally: BD.EXCLUDED_ROUNDS = saved
class M3_M6_Text(unittest.TestCase):
    def test_M3_residual_stated_exactly(self):                                    # codex V23 M3: the "cannot hide CLOSED" sentence must be gone; the exact residual present
        for p in (Path(os.environ["RULE_TEXT"]), Path(os.environ["DESIGN_TEXT"]), D / "track2" / "provenance_designs_v4.py"):
            t = p.read_text(encoding="utf-8"); self.assertNotIn("cannot hide a CLOSED witness state", t, p.name); self.assertIn("absence-based", t, p.name)
    def test_M6_text_sweep(self):                                                # codex V23 M6
        t2 = Path(os.environ["DESIGN_TEXT"]).read_text(); r = Path(os.environ["RULE_TEXT"]).read_text(encoding="utf-8")
        for bad in ("about 90 days", "NOT wired", "would do it themselves", "one network read per driver run"): self.assertNotIn(bad, t2, bad)
        self.assertNotIn("UNNAMED until Duho", (D / "fourier_chirality" / "run_configurations_v8.py").read_text())
        self.assertNotIn("this module's pure functions do not otherwise need", "") ; self.assertIn("build_corpus_identity_v24.py", r); self.assertNotIn("builder v22 8 + V15 builder 4 + verdict v23", r)
        self.assertIn("builder-control-refusal", r); self.assertNotIn("Questions for the seats at the V22 gate", r)
if __name__ == "__main__": unittest.main()
