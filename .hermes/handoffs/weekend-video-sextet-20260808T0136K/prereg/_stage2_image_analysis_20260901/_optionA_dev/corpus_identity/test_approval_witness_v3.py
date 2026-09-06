"""approval_witness_v3 over a real git clone with a bare origin and a MOCK events feed (the server-side push timestamp)."""
import json, unittest, tempfile, sys, subprocess, os
from datetime import datetime, timezone, timedelta
from pathlib import Path
HERE = Path(__file__).resolve().parent; sys.path.insert(0, str(HERE)); sys.path.insert(0, str(HERE.parent / "beacon_v2"))
import beacon_record_expedited as X, drand_round, test_pki as pki, approval_witness_v3 as AW
T_SIGN = datetime(2026, 9, 6, 3, 0, 7, tzinfo=timezone.utc); TP = X.pulse_time(T_SIGN); D = "b" * 64; RND = drand_round.round_for(TP)
R_SIGN = drand_round.round_for(T_SIGN); NONCE = "e" * 64
def git(cwd, *a, env=None): return subprocess.run(["git", *a], cwd=cwd, capture_output=True, text=True, check=True, env={**os.environ, **(env or {})}).stdout.strip()
def net(nonce_round=R_SIGN):
    base = pki.network(TP, sign=False, drand=(RND, "c" * 64))
    def fetch(url, timeout=30):
        if url.endswith(f"/public/{nonce_round}"): return json.dumps({"round": nonce_round, "randomness": NONCE, "signature": "00"}).encode()
        return base(url, timeout)
    return fetch
class T(unittest.TestCase):
    def setUp(self):
        self.tmp = Path(tempfile.mkdtemp()); self.bare = self.tmp / "remote.git"; self.work = self.tmp / "work"
        subprocess.run(["git", "init", "-q", "--bare", str(self.bare)], check=True); subprocess.run(["git", "clone", "-q", str(self.bare), str(self.work)], check=True, capture_output=True)
        git(self.work, "config", "user.email", "t@t"); git(self.work, "config", "user.name", "t"); (self.work / "seed").write_text("x"); git(self.work, "add", "seed"); git(self.work, "commit", "-q", "-m", "init"); git(self.work, "push", "-q", "-u", "origin", "HEAD:refs/heads/main")
        self.stmt = self.work / "APPROVAL_RECORD_SELRULE_V19_TEST.md"
        self.body = f"RULE_SHA256: {D}\nAPPROVAL_UTC: {X.fmt(T_SIGN)}\nDRAND_AT_APPROVAL: round {R_SIGN} randomness {NONCE}\n"
    def commit(self, push=True):
        self.stmt.write_text(self.body); git(self.work, "add", self.stmt.name); git(self.work, "commit", "-q", "-m", "approval"); c = git(self.work, "rev-parse", "HEAD")
        if push: git(self.work, "push", "-q", "origin", "HEAD:refs/heads/main")
        return c
    def events(self, commit, when):
        return [{"type": "PushEvent", "id": "1", "created_at": when.strftime("%Y-%m-%dT%H:%M:%SZ"), "payload": {"ref": "refs/heads/main", "head": commit, "commits": [{"sha": commit}]}}]
    def verify(self, commit, when=None, fetch=None, body_override=None):
        return AW.verify(self.stmt, T_SIGN, TP, RND, D, fetch or net(), "origin/main", str(self.bare), X.MIN_T_SIGN, "APPROVAL_RECORD_SELRULE_V19*", self.events(commit, when or (TP - timedelta(minutes=3))), "refs/heads/main")
    def test_accepted_and_what_it_proves(self):
        c = self.commit(); w = self.verify(c)
        self.assertEqual(w["commit"], c); self.assertEqual(w["nonce_round"], R_SIGN); self.assertIn("before T_pulse", w["proves"]); self.assertIn("who spoke", w["attested"])
    def test_late_writer_with_backdated_commit_refused_by_server_time(self):
        c = self.commit()   # committer date irrelevant now: the SERVER time decides
        with self.assertRaises(SystemExit) as cm: self.verify(c, when=TP + timedelta(seconds=1))
        self.assertIn("APPROVAL-PUSHED-AFTER-T-PULSE", str(cm.exception)); self.assertIn("CLOSED", str(cm.exception))
    def test_no_push_event_refused(self):
        c = self.commit()
        with self.assertRaises(SystemExit) as cm: AW.verify(self.stmt, T_SIGN, TP, RND, D, net(), "origin/main", str(self.bare), X.MIN_T_SIGN, "APPROVAL_RECORD_SELRULE_V19*", [], "refs/heads/main")
        self.assertIn("APPROVAL-PUSH-EVENT-MISSING", str(cm.exception))
    def test_old_nonce_round_refused(self):
        self.body = f"RULE_SHA256: {D}\nAPPROVAL_UTC: {X.fmt(T_SIGN)}\nDRAND_AT_APPROVAL: round {R_SIGN - 5} randomness {NONCE}\n"; c = self.commit()
        with self.assertRaises(SystemExit) as cm: self.verify(c, fetch=net(R_SIGN - 5))
        self.assertIn("APPROVAL-NONCE-ROUND", str(cm.exception))
    def test_schema_exactly_one_of_each(self):
        self.body = self.body + f"DRAND_AT_APPROVAL: round {R_SIGN} randomness {NONCE}\n"; c = self.commit()
        with self.assertRaises(SystemExit) as cm: self.verify(c)
        self.assertIn("APPROVAL-SCHEMA", str(cm.exception))
    def test_wrong_t_sign_or_digest_refused(self):
        self.body = f"RULE_SHA256: {'d' * 64}\nAPPROVAL_UTC: {X.fmt(T_SIGN)}\nDRAND_AT_APPROVAL: round {R_SIGN} randomness {NONCE}\n"; c = self.commit()
        with self.assertRaises(SystemExit) as cm: self.verify(c)
        self.assertIn("APPROVAL-SCHEMA", str(cm.exception))
    def test_unpushed_modified_second_record_refused(self):
        c = self.commit(push=False)
        with self.assertRaises(SystemExit) as cm: self.verify(c)
        self.assertIn("APPROVAL-RECORD-NOT-PUSHED", str(cm.exception))
        git(self.work, "push", "-q", "origin", "HEAD:refs/heads/main"); self.stmt.write_text(self.body + "\n")
        with self.assertRaises(SystemExit) as cm: self.verify(c)
        self.assertIn("APPROVAL-RECORD-MODIFIED", str(cm.exception)); self.stmt.write_text(self.body)
        other = self.work / "APPROVAL_RECORD_SELRULE_V19_SECOND.md"; other.write_text("again"); git(self.work, "add", other.name); git(self.work, "commit", "-q", "-m", "again"); git(self.work, "push", "-q", "origin", "HEAD:refs/heads/main")
        with self.assertRaises(SystemExit) as cm: self.verify(c)
        self.assertIn("APPROVAL-NOT-FIRST", str(cm.exception))
    def test_push_event_matcher_uses_head_or_commit_list(self):
        c = self.commit(); ev = self.events(c, TP - timedelta(minutes=1)); ev[0]["payload"]["head"] = "0" * 40
        self.assertIsNotNone(AW.push_event_for(ev, c, "refs/heads/main")); self.assertIsNone(AW.push_event_for(ev, c, "refs/heads/other"))
    def test_v3_retains_entire_event_and_picks_earliest(self):
        c = self.commit(); early = self.events(c, TP - timedelta(minutes=5))[0]; late = self.events(c, TP + timedelta(minutes=5))[0]; late["id"] = "2"
        w = AW.verify(self.stmt, T_SIGN, TP, RND, D, net(), "origin/main", str(self.bare), X.MIN_T_SIGN, "APPROVAL_RECORD_SELRULE_V19*", [late, early], "refs/heads/main", provenance={"endpoints": ["e"], "retrieved_utc": "x", "gh_version": "gh test"})
        self.assertEqual(w["push_event"], early); self.assertEqual(w["push_event"]["payload"]["commits"][0]["sha"], c); self.assertIn("push_event_sha256", w); self.assertEqual(w["events_provenance"]["gh_version"], "gh test")
if __name__ == "__main__": unittest.main()
