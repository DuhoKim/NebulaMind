"""TRACK 7 FAIL-FIRST tests — codex's V26 findings V26-1, V26-2, V26-3 (CODEX_SELRULE_V26_SEATB.md). Targets the SUCCESSORS (provenance_designs_v7,
run_configurations_v11, collector v27, builder v27); run FIRST against byte-copies of the V26 modules (import lines renamed only), classified per test.
Remotes/clones are LOCAL; the gh runner is fixture-supplied — labelled. Pinned V26 files are not edited."""
import json, os, sys, tempfile, unittest, hashlib, subprocess
from pathlib import Path
HERE = Path(__file__).resolve().parent; D = HERE.parent
for p in ("beacon_v2", "drand_only", "corpus_identity", "fourier_chirality", "track2"): sys.path.insert(0, str(D / p))
import provenance_designs_v7 as P
def git(cwd, *a, check=True):
    r = subprocess.run(["git", *a], cwd=cwd, capture_output=True, text=True)
    if check and r.returncode: raise RuntimeError(r.stderr)
    return r.stdout.strip()
REF = "refs/heads/main"; REPO = "DuhoKim/NebulaMind"
def canon(e): return hashlib.sha256(json.dumps(e, sort_keys=True, separators=(",", ":")).encode()).hexdigest()
def ev(commit, before, n, **extra):
    e = {"type": "PushEvent", "id": f"h{n}", "created_at": f"2026-09-07T01:{n:02d}:00Z", "repo": {"name": REPO}, "payload": {"ref": REF, "before": before, "head": commit, "commits": [{"sha": commit}]}}; e.update(extra); return e
class V26_1_Contradiction(unittest.TestCase):
    def test_same_event_different_before_is_forged(self):                        # codex V26-1: same id, same head, different `before` → an affirmative contradiction, terminal
        live = ev("a" * 40, "b" * 40, 5); older = ev("c" * 40, "d" * 40, 1)
        retained = json.loads(json.dumps(live)); retained["payload"]["before"] = "0" * 40
        o, why = P.authenticate_event(retained, [older, live], REPO, REF, "a" * 40, feed_reaches_back_to=older["created_at"])
        self.assertEqual(o, "FORGED", why)
        retained2 = json.loads(json.dumps(live)); retained2["payload"]["head"] = "e" * 40; retained2["payload"]["commits"] = [{"sha": "a" * 40}]   # different head, same delivered commit (via commits), same id
        o, why = P.authenticate_event(retained2, [older, live], REPO, REF, "a" * 40, feed_reaches_back_to=older["created_at"]); self.assertEqual(o, "FORGED", why)
        o, why = P.authenticate_event(live, [older], REPO, REF, "a" * 40, feed_reaches_back_to=older["created_at"]); self.assertEqual(o, "INCOMPLETE", why)   # plain absence stays a retry
class V26_2_TriStateDelivery(unittest.TestCase):
    def setUp(self):
        self.tmp = Path(tempfile.mkdtemp()); self.bare = self.tmp / "remote.git"; self.work = self.tmp / "work"
        subprocess.run(["git", "init", "-q", "--bare", str(self.bare)], check=True); subprocess.run(["git", "clone", "-q", str(self.bare), str(self.work)], check=True, capture_output=True); git(self.work, "config", "user.email", "t@t"); git(self.work, "config", "user.name", "t")
        (self.work / "s").write_text("x"); git(self.work, "add", "s"); git(self.work, "commit", "-q", "-m", "init"); git(self.work, "push", "-q", "-u", "origin", "HEAD:" + REF); self.base = git(self.work, "rev-parse", "HEAD")
        (self.work / "a").write_text("a"); git(self.work, "add", "a"); git(self.work, "commit", "-q", "-m", "approval"); self.commit = git(self.work, "rev-parse", "HEAD"); git(self.work, "push", "-q", "origin", "HEAD:" + REF)
        self.stale = self.tmp / "stale"; subprocess.run(["git", "clone", "-q", str(self.bare), str(self.stale)], check=True, capture_output=True)   # a clone taken BEFORE the descendant head exists
        (self.work / "l").write_text("l"); git(self.work, "add", "l"); git(self.work, "commit", "-q", "-m", "later"); self.head = git(self.work, "rev-parse", "HEAD"); git(self.work, "push", "-q", "origin", "HEAD:" + REF)
        self.anc = {"type": "PushEvent", "id": "anc", "created_at": "2026-09-07T01:05:00Z", "repo": {"name": REPO}, "payload": {"ref": REF, "before": self.base, "head": self.head}}   # before..head delivery, no commits list
    def test_delivery_is_tri_state(self):
        self.assertEqual(P.delivery(self.anc, self.commit, REF, self.work), "DELIVERED")
        self.assertEqual(P.delivery(self.anc, self.commit, REF, self.stale), "UNDETERMINED")                     # the descendant object is missing: cannot be established
        self.assertEqual(P.delivery(ev("f" * 40, "g" * 40, 1), self.commit, REF, self.work), "NOT-DELIVERED")
    def test_missing_objects_are_retry_not_forged(self):                        # codex V26-2
        self.assertEqual(P.authenticate_event(self.anc, [self.anc], REPO, REF, self.commit, root=self.work)[0], "AUTHENTIC")
        o, why = P.authenticate_event(self.anc, [self.anc], REPO, REF, self.commit, root=self.stale); self.assertEqual(o, "UNAVAILABLE", why); self.assertNotEqual(o, "FORGED")
        o, why = P.authenticate_event(ev("f" * 40, "g" * 40, 1), [self.anc], REPO, REF, self.commit, root=self.work); self.assertEqual(o, "INCONSISTENT-INPUT", why)   # a retained event that does not deliver the commit: a positive input mismatch, named as such
        o, why = P.authenticate_event({**self.anc, "repo": {"name": "other/repo"}}, [self.anc], REPO, REF, self.commit, root=self.work); self.assertEqual(o, "INCONSISTENT-INPUT", why)   # wrong repository in the retained event: an input mismatch, named as such (not FORGED)
class V26_3_Text(unittest.TestCase):
    def test_sweep(self):
        r = Path(os.environ["RULE_TEXT"]).read_text(encoding="utf-8"); t2 = Path(os.environ["DESIGN_TEXT"]).read_text(encoding="utf-8"); q = Path(os.environ["QUESTIONS_TEXT"]).read_text(encoding="utf-8")
        p7 = (D / "track2" / "provenance_designs_v7.py").read_text(encoding="utf-8"); d11 = (D / "fourier_chirality" / "run_configurations_v11.py").read_text(encoding="utf-8")
        self.assertNotIn("FORGED (absent from the live feed", t2); self.assertIn("INCOMPLETE", t2.split("## (b)")[0])
        self.assertNotIn("EVIDENCE-EXPIRED (retry", p7); self.assertNotIn("retry-class) and", p7)
        self.assertNotIn("OPEN-EVENT-EXPIRED", q); self.assertNotIn("EVIDENCE-UNAVAILABLE / EXPIRED for ANY", q)
        self.assertNotIn("beacon_record_drand_v22.collect", r); self.assertNotIn("(`verify_drand.py` `", r.split("(4)")[1][:600] if "(4)" in r else "")
        self.assertNotIn("v9 on provenance_designs_v6", d11); self.assertNotIn("v8 on provenance_designs_v6", d11); self.assertNotIn("codex V24 N2/N3: composed mode on provenance_designs_v6", d11)
if __name__ == "__main__": unittest.main()
