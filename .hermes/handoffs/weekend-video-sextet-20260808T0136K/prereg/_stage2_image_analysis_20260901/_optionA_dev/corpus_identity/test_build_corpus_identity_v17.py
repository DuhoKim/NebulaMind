"""V17 builder: expedited verdict (V17 fixes) + APPROVAL WITNESS. A real git clone with a bare 'origin' stands in for the protected
branch (the driver fixture's pattern). The approval record carries a drand freshness nonce for an earlier round; the mock network
serves both that round and the seed round through the three-tier test PKI."""
import json, unittest, tempfile, sys, subprocess, os
from datetime import datetime, timezone, timedelta
from pathlib import Path
HERE = Path(__file__).resolve().parent; sys.path.insert(0, str(HERE)); sys.path.insert(0, str(HERE.parent / "beacon_v2"))
import beacon_record_expedited as X, drand_round, test_pki as pki
import build_corpus_identity_v17 as B17, approval_witness as AW
T_SIGN = datetime(2026, 9, 6, 3, 0, 7, tzinfo=timezone.utc); TP = X.pulse_time(T_SIGN); D = "b" * 64; RND = drand_round.round_for(TP); SOON = TP + timedelta(minutes=1)
NONCE_R = drand_round.round_for(T_SIGN) - 1; NONCE = "e" * 64          # a round that closed just before approval
def git(cwd, *a, env=None): return subprocess.run(["git", *a], cwd=cwd, capture_output=True, text=True, check=True, env={**os.environ, **(env or {})}).stdout.strip()
def two_round_network(**kw):
    base = pki.network(TP, sign=False, drand=(RND, "c" * 64), **kw)
    def fetch(url, timeout=30):
        if url.endswith(f"/public/{NONCE_R}"): return json.dumps({"round": NONCE_R, "randomness": NONCE, "signature": "00"}).encode()
        return base(url, timeout)
    return fetch
class T(unittest.TestCase):
    def setUp(self):
        self.tmp = Path(tempfile.mkdtemp()); bare = self.tmp / "remote.git"; self.work = self.tmp / "work"
        subprocess.run(["git", "init", "-q", "--bare", str(bare)], check=True); subprocess.run(["git", "clone", "-q", str(bare), str(self.work)], check=True, capture_output=True)
        git(self.work, "config", "user.email", "t@t"); git(self.work, "config", "user.name", "t"); (self.work / "seed").write_text("x"); git(self.work, "add", "seed"); git(self.work, "commit", "-q", "-m", "init"); git(self.work, "push", "-q", "-u", "origin", "HEAD:refs/heads/main")
        B17.WITNESS_REMOTE_REF = "origin/main"; B17.WITNESS_REMOTE_URL = str(bare); B17.APPROVAL_GLOB = "APPROVAL_RECORD_SELRULE_V17*"; B17.WITNESS_FETCH = True; B17.nist_pulse.pinned_roots = pki.roots
        self.stmt = self.work / "APPROVAL_RECORD_SELRULE_V17_TEST.md"; self.stmt_bytes = f"V17 approved: {D} at {X.fmt(T_SIGN)}\nDRAND_AT_APPROVAL: round {NONCE_R} randomness {NONCE}\n".encode()
        self.n = two_round_network(); self.env_before = {"GIT_COMMITTER_DATE": (TP - timedelta(minutes=5)).isoformat()}
    def commit_stmt(self, push=True, env=None):
        self.stmt.write_bytes(self.stmt_bytes); git(self.work, "add", self.stmt.name); git(self.work, "commit", "-q", "-m", "approval", env=env or self.env_before)
        if push: git(self.work, "push", "-q", "origin", "HEAD:refs/heads/main")
    def record(self):
        rec = X.collect(self.n, X.fmt(T_SIGN), D, self.stmt_bytes, now=SOON); p = self.tmp / "rec.json"; p.write_text(json.dumps(rec)); return p
    def test_witnessed_approval_accepted_and_carried(self):
        self.commit_stmt(); B, raw, r = B17._validate_beacon_record(self.record(), D, self.stmt, fetch=self.n, now=SOON)
        self.assertEqual(r["outcome"], "ACCEPT-DRAND"); w = r["approval_witness"]; self.assertEqual(w["nonce_round"], NONCE_R); self.assertEqual(w["record_path"], self.stmt.name); self.assertTrue(w["committer_utc"] < X.fmt(TP))
    def test_unpushed_refused(self):
        self.commit_stmt(push=False)
        with self.assertRaises(SystemExit) as cm: B17._validate_beacon_record(self.record(), D, self.stmt, fetch=self.n, now=SOON)
        self.assertIn("APPROVAL-RECORD-NOT-PUSHED", str(cm.exception))
    def test_modified_after_commit_refused(self):
        self.commit_stmt(); rec = self.record(); self.stmt.write_bytes(self.stmt_bytes + b"\n")
        with self.assertRaises(SystemExit) as cm: B17._validate_beacon_record(rec, D, self.stmt, fetch=self.n, now=SOON)
        self.assertTrue("APPROVAL-RECORD-MODIFIED" in str(cm.exception) or "STATEMENT-BYTES" in str(cm.exception))
    def test_second_approval_record_refused(self):
        self.commit_stmt(); other = self.work / "APPROVAL_RECORD_SELRULE_V17_SECOND.md"; other.write_text("again"); git(self.work, "add", other.name); git(self.work, "commit", "-q", "-m", "again", env=self.env_before); git(self.work, "push", "-q", "origin", "HEAD:refs/heads/main")
        with self.assertRaises(SystemExit) as cm: B17._validate_beacon_record(self.record(), D, self.stmt, fetch=self.n, now=SOON)
        self.assertIn("APPROVAL-NOT-FIRST", str(cm.exception))
    def test_committed_after_t_pulse_refused(self):
        self.commit_stmt(env={"GIT_COMMITTER_DATE": (TP + timedelta(minutes=5)).isoformat()})
        with self.assertRaises(SystemExit) as cm: B17._validate_beacon_record(self.record(), D, self.stmt, fetch=self.n, now=SOON)
        self.assertIn("APPROVAL-AFTER-T-PULSE", str(cm.exception))
    def test_nonce_missing_wrong_round_or_mismatch_refused(self):
        self.stmt_bytes = f"V17 approved: {D} at {X.fmt(T_SIGN)}\n".encode(); self.commit_stmt()
        with self.assertRaises(SystemExit) as cm: B17._validate_beacon_record(self.record(), D, self.stmt, fetch=self.n, now=SOON)
        self.assertIn("APPROVAL-NONCE-MISSING", str(cm.exception))
        git(self.work, "reset", "-q", "--hard", "HEAD~1"); git(self.work, "push", "-q", "-f", "origin", "HEAD:refs/heads/main")   # test repo only
        self.stmt_bytes = f"V17 approved: {D} at {X.fmt(T_SIGN)}\nDRAND_AT_APPROVAL: round {RND} randomness {NONCE}\n".encode(); self.commit_stmt()
        with self.assertRaises(SystemExit) as cm: B17._validate_beacon_record(self.record(), D, self.stmt, fetch=self.n, now=SOON)
        self.assertIn("APPROVAL-NONCE-ROUND", str(cm.exception))
        git(self.work, "reset", "-q", "--hard", "HEAD~1"); git(self.work, "push", "-q", "-f", "origin", "HEAD:refs/heads/main")
        self.stmt_bytes = f"V17 approved: {D} at {X.fmt(T_SIGN)}\nDRAND_AT_APPROVAL: round {NONCE_R} randomness {'f' * 64}\n".encode(); self.commit_stmt()
        with self.assertRaises(SystemExit) as cm: B17._validate_beacon_record(self.record(), D, self.stmt, fetch=self.n, now=SOON)
        self.assertIn("APPROVAL-NONCE-MISMATCH", str(cm.exception))
    def test_redirected_remote_refused(self):
        self.commit_stmt(); fake = self.tmp / "fake.git"; subprocess.run(["git", "init", "-q", "--bare", str(fake)], check=True); git(self.work, "remote", "set-url", "origin", str(fake)); git(self.work, "push", "-q", "origin", "HEAD:refs/heads/main")
        with self.assertRaises(SystemExit) as cm: B17._validate_beacon_record(self.record(), D, self.stmt, fetch=self.n, now=SOON)
        self.assertIn("APPROVAL-REMOTE-URL", str(cm.exception))
if __name__ == "__main__": unittest.main()
