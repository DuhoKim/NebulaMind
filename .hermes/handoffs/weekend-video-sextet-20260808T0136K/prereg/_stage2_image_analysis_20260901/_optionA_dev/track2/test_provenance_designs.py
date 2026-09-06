"""Exhibit-tests for the UNADOPTED track-2 designs. The live event feed is FIXTURE-SUPPLIED (labelled); git repositories are real and local."""
import json, unittest, tempfile, subprocess, sys
from pathlib import Path
HERE = Path(__file__).resolve().parent; sys.path.insert(0, str(HERE)); sys.path.insert(0, str(HERE.parent / "corpus_identity"))
import provenance_designs as P, history_v2 as H
def git(cwd, *a): return subprocess.run(["git", *a], cwd=cwd, capture_output=True, text=True, check=True).stdout.strip()
REPO = "DuhoKim/NebulaMind"; REF = "refs/heads/feat/paper-workflow-v2"; C = "a" * 40
def ev(**kw):
    e = {"type": "PushEvent", "id": "1", "created_at": "2026-09-07T01:05:00Z", "repo": {"name": REPO}, "actor": {"login": "x"}, "payload": {"ref": REF, "head": C, "commits": [{"sha": C}]}}; e.update(kw); return e
class T(unittest.TestCase):
    def test_a_event_authentication_against_a_fixture_feed(self):
        genuine = ev(); feed = [ev(id="9", created_at="2026-09-07T01:06:00Z"), genuine, {"type": "WatchEvent"}]     # FIXTURE-SUPPLIED live feed
        self.assertEqual(P.authenticate_event(genuine, feed, REPO, REF, C)[0], "AUTHENTIC")
        forged = ev(created_at="2000-01-01T00:00:00Z", id="invented", repo={"name": "attacker/unrelated"})           # codex's coherent forgery
        self.assertEqual(P.authenticate_event(forged, feed, REPO, REF, C)[0], "FORGED")
        forged2 = ev(created_at="2000-01-01T00:00:00Z", id="invented")                                             # names the right repo, absent from the feed
        self.assertEqual(P.authenticate_event(forged2, feed, REPO, REF, C)[0], "FORGED")
        self.assertEqual(P.authenticate_event(ev(id="9", created_at="2026-09-07T01:06:00Z"), feed, REPO, REF, C)[0], "FORGED")   # in the feed but not the earliest
        self.assertEqual(P.authenticate_event(genuine, None, REPO, REF, C)[0], "UNAVAILABLE")
        self.assertEqual(P.authenticate_event(forged2, feed, REPO, REF, C, feed_reaches_back_to="2026-01-01T00:00:00Z")[0], "EXPIRED")
    def test_b_history_continuation_through_git(self):
        tmp = Path(tempfile.mkdtemp()); work = tmp / "w"; work.mkdir(); subprocess.run(["git", "init", "-q", str(work)], check=True); git(work, "config", "user.email", "t@t"); git(work, "config", "user.name", "t")
        (work / "seed").write_text("x"); git(work, "add", "seed"); git(work, "commit", "-q", "-m", "init")
        log = work / "collection_log.jsonl"; H.genesis(log, "a" * 64, "t", "b" * 64, 1); git(work, "add", log.name); git(work, "commit", "-q", "-m", "history-open"); open_c = git(work, "rev-parse", "HEAD")
        H.append(log, {"stage": "collector-collect", "outcome": "RETRY"}); git(work, "commit", "-q", "-am", "attempt 1")
        H.append(log, {"stage": "builder-accept", "record_sha256": "c" * 64, "outcome": "ACCEPT-DRAND", "seed_hex": "d" * 64}); git(work, "commit", "-q", "-am", "accept")
        ok, why, commits = P.validate_continuation(work, log.name, open_c); self.assertTrue(ok, why); self.assertEqual(len(commits), 3)
        good = log.read_bytes()
        lines = good.split(b"\n"); log.write_bytes(b"\n".join(lines[:-2]) + b"\n")                                        # deleted suffix: internally valid, refused here
        self.assertTrue(H.validate(log)); ok, why, _ = P.validate_continuation(work, log.name, open_c); self.assertFalse(ok); self.assertIn("NOT-AN-EXTENSION", why)
        log.unlink(); H.genesis(log, "a" * 64, "t", "b" * 64, 1); H.append(log, {"stage": "builder-accept", "record_sha256": "e" * 64, "outcome": "ACCEPT-DRAND", "seed_hex": "f" * 64})   # rebuilt: fresh genesis + accept
        self.assertTrue(H.validate(log)); ok, why, _ = P.validate_continuation(work, log.name, open_c); self.assertFalse(ok)
        git(work, "commit", "-q", "-am", "rebuilt and committed")                                                      # even committed, the rebuild is not an extension of the previous blob
        ok, why, _ = P.validate_continuation(work, log.name, open_c); self.assertFalse(ok); self.assertIn("NOT-AN-EXTENSION", why)
        self.assertFalse(P.validate_continuation(work, log.name, "0" * 40)[0])                                          # wrong open commit
        log.write_bytes(good); git(work, "commit", "-q", "-am", "restored")                                              # restoring the bytes does not undo the recorded rebuild
        ok, why, _ = P.validate_continuation(work, log.name, open_c); self.assertFalse(ok)
if __name__ == "__main__": unittest.main()
