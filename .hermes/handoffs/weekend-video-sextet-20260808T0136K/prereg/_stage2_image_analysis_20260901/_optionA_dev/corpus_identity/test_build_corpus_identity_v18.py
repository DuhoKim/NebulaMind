"""V18 builder: expedited verdict (V18 policy) + approval_witness_v2 (mock events feed) + collection-log lock + adoption binding.
Real git clone with a bare origin; three-tier test PKI; no network."""
import json, unittest, tempfile, sys, subprocess, os
from datetime import datetime, timezone, timedelta
from pathlib import Path
HERE = Path(__file__).resolve().parent; sys.path.insert(0, str(HERE)); sys.path.insert(0, str(HERE.parent / "beacon_v2"))
import beacon_record_expedited as X, drand_round, test_pki as pki
import build_corpus_identity_v18 as B18
T_SIGN = datetime(2026, 9, 6, 3, 0, 7, tzinfo=timezone.utc); TP = X.pulse_time(T_SIGN); D = "b" * 64; RND = drand_round.round_for(TP); R_SIGN = drand_round.round_for(T_SIGN); NONCE = "e" * 64; SOON = TP + timedelta(minutes=1)
def git(cwd, *a): return subprocess.run(["git", *a], cwd=cwd, capture_output=True, text=True, check=True).stdout.strip()
def net():
    base = pki.network(TP, sign=False, drand=(RND, "c" * 64))
    def fetch(url, timeout=30):
        if url.endswith(f"/public/{R_SIGN}"): return json.dumps({"round": R_SIGN, "randomness": NONCE, "signature": "00"}).encode()
        return base(url, timeout)
    return fetch
class T(unittest.TestCase):
    def setUp(self):
        self.tmp = Path(tempfile.mkdtemp()); bare = self.tmp / "remote.git"; self.work = self.tmp / "work"
        subprocess.run(["git", "init", "-q", "--bare", str(bare)], check=True); subprocess.run(["git", "clone", "-q", str(bare), str(self.work)], check=True, capture_output=True)
        git(self.work, "config", "user.email", "t@t"); git(self.work, "config", "user.name", "t"); (self.work / "seed").write_text("x"); git(self.work, "add", "seed"); git(self.work, "commit", "-q", "-m", "init"); git(self.work, "push", "-q", "-u", "origin", "HEAD:refs/heads/main")
        self.stmt = self.work / "APPROVAL_RECORD_SELRULE_V18_TEST.md"; self.stmt_bytes = f"RULE_SHA256: {D}\nAPPROVAL_UTC: {X.fmt(T_SIGN)}\nDRAND_AT_APPROVAL: round {R_SIGN} randomness {NONCE}\n".encode()
        self.stmt.write_bytes(self.stmt_bytes); git(self.work, "add", self.stmt.name); git(self.work, "commit", "-q", "-m", "approval"); self.commit = git(self.work, "rev-parse", "HEAD"); git(self.work, "push", "-q", "origin", "HEAD:refs/heads/main")
        B18.WITNESS_REMOTE_REF = "origin/main"; B18.WITNESS_REMOTE_URL = str(bare); B18.APPROVAL_GLOB = "APPROVAL_RECORD_SELRULE_V18*"; B18.WITNESS_FETCH = True; B18.BRANCH_REF = "refs/heads/main"; B18.nist_pulse.pinned_roots = pki.roots
        self.when = TP - timedelta(minutes=3); B18.EVENTS = lambda: [{"type": "PushEvent", "id": "1", "created_at": self.when.strftime("%Y-%m-%dT%H:%M:%SZ"), "payload": {"ref": "refs/heads/main", "head": self.commit, "commits": [{"sha": self.commit}]}}]
        B18.ADOPTION_FILE = self.tmp / "ADOPTED_RULE_SHA256.txt"; B18.ADOPTION_FILE.write_text(D + "\n"); B18.COLLECTION_LOG = self.tmp / "collection_log.jsonl"
        self.n = net(); rec = X.collect(self.n, X.fmt(T_SIGN), D, self.stmt_bytes, now=SOON); self.rec = self.tmp / "rec.json"; self.rec.write_text(json.dumps(rec))
    def test_accepted_witnessed_locked(self):
        B, raw, r = B18._validate_beacon_record(self.rec, D, self.stmt, fetch=self.n, now=SOON)
        self.assertEqual(r["outcome"], "ACCEPT-DRAND"); self.assertEqual(r["approval_witness"]["push_event"]["head"], self.commit); self.assertEqual(r["collection_lock"]["first_accept"]["outcome"], "ACCEPT-DRAND")
        self.assertEqual(len(B18.COLLECTION_LOG.read_text().splitlines()), 1)
        B, raw, r2 = B18._validate_beacon_record(self.rec, D, self.stmt, fetch=self.n, now=SOON)     # same record again: idempotent, still one line
        self.assertEqual(len(B18.COLLECTION_LOG.read_text().splitlines()), 1)
    def test_late_push_closes_commitment(self):
        self.when = TP + timedelta(seconds=30)
        with self.assertRaises(SystemExit) as cm: B18._validate_beacon_record(self.rec, D, self.stmt, fetch=self.n, now=SOON)
        self.assertIn("APPROVAL-PUSHED-AFTER-T-PULSE", str(cm.exception))
    def test_second_different_accept_is_locked_out(self):
        B18._validate_beacon_record(self.rec, D, self.stmt, fetch=self.n, now=SOON)                 # first ACCEPT (drand) locked
        n2 = pki.network(TP, drand=(RND, "c" * 64))                                                    # NIST now authenticable: a fresh record would ACCEPT-NIST
        def f2(url, timeout=30):
            if url.endswith(f"/public/{R_SIGN}"): return json.dumps({"round": R_SIGN, "randomness": NONCE, "signature": "00"}).encode()
            return n2(url, timeout)
        rec2 = X.collect(f2, X.fmt(T_SIGN), D, self.stmt_bytes, now=SOON); p2 = self.tmp / "rec2.json"; p2.write_text(json.dumps(rec2))
        with self.assertRaises(SystemExit) as cm: B18._validate_beacon_record(p2, D, self.stmt, fetch=f2, now=SOON)
        self.assertIn("COLLECTION-LOCKED", str(cm.exception))
    def test_adoption_binding(self):
        B18.ADOPTION_FILE.unlink()
        with self.assertRaises(SystemExit) as cm: B18._validate_beacon_record(self.rec, D, self.stmt, fetch=self.n, now=SOON)
        self.assertIn("ADOPTION-MISSING", str(cm.exception))
        B18.ADOPTION_FILE.write_text("d" * 64 + "\n")
        with self.assertRaises(SystemExit) as cm: B18._validate_beacon_record(self.rec, D, self.stmt, fetch=self.n, now=SOON)
        self.assertIn("ADOPTION-MISMATCH", str(cm.exception))
    def test_diff_from_v15_builder_is_the_boundary_only(self):
        import difflib
        a = (HERE / "build_corpus_identity.py").read_text().splitlines(); b = (HERE / "build_corpus_identity_v18.py").read_text().splitlines()
        ch = [l for l in difflib.unified_diff(a, b, n=0, lineterm="") if l[:1] in "+-" and l[:3] not in ("+++", "---")]
        removed = [l[1:] for l in ch if l[0] == "-"]
        self.assertTrue(all(("beacon_record" in l) or ("Build the ordered" in l) or ("return B, raw, r" in l) or ("'beacon_outcome'" in l) or ("t_pulse=beacon_record" in l) or ("approval_witness" in l) for l in removed), removed)
if __name__ == "__main__": unittest.main()
