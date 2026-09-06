"""V19 builder: expedited verdict (V19 predicate) + approval_witness_v3 (mock events feed + provenance) + COLLECTION HISTORY (every attempt
logged; first ACCEPT binding; conflict logged) + ADOPTION verified as a blob at the approval commit. Real git clone with a bare origin;
three-tier test PKI; no network."""
import json, unittest, tempfile, sys, subprocess, os, urllib.error
from datetime import datetime, timezone, timedelta
from pathlib import Path
HERE = Path(__file__).resolve().parent; sys.path.insert(0, str(HERE)); sys.path.insert(0, str(HERE.parent / "beacon_v2"))
import beacon_record_expedited as X, drand_round, test_pki as pki
import build_corpus_identity_v19 as B19
T_SIGN = datetime(2026, 9, 6, 3, 0, 7, tzinfo=timezone.utc); TP = X.pulse_time(T_SIGN); D = "b" * 64; RND = drand_round.round_for(TP); R_SIGN = drand_round.round_for(T_SIGN); NONCE = "e" * 64; SOON = TP + timedelta(minutes=1)
def git(cwd, *a): return subprocess.run(["git", *a], cwd=cwd, capture_output=True, text=True, check=True).stdout.strip()
def net(base=None):
    base = base or pki.network(TP, sign=False, drand=(RND, "c" * 64))
    def fetch(url, timeout=30):
        if url.endswith(f"/public/{R_SIGN}"): return json.dumps({"round": R_SIGN, "randomness": NONCE, "signature": "00"}).encode()
        return base(url, timeout)
    return fetch
class T(unittest.TestCase):
    def setUp(self):
        self.tmp = Path(tempfile.mkdtemp()); bare = self.tmp / "remote.git"; self.work = self.tmp / "work"
        subprocess.run(["git", "init", "-q", "--bare", str(bare)], check=True); subprocess.run(["git", "clone", "-q", str(bare), str(self.work)], check=True, capture_output=True)
        git(self.work, "config", "user.email", "t@t"); git(self.work, "config", "user.name", "t"); (self.work / "seed").write_text("x"); git(self.work, "add", "seed"); git(self.work, "commit", "-q", "-m", "init"); git(self.work, "push", "-q", "-u", "origin", "HEAD:refs/heads/main")
        self.stmt = self.work / "APPROVAL_RECORD_SELRULE_V19_TEST.md"; self.stmt_bytes = f"RULE_SHA256: {D}\nAPPROVAL_UTC: {X.fmt(T_SIGN)}\nDRAND_AT_APPROVAL: round {R_SIGN} randomness {NONCE}\n".encode()
        B19.ADOPTION_FILE = self.work / "ADOPTED_RULE_SHA256.txt"; B19.ADOPTION_FILE.write_text(D + "\n")           # committed WITH the approval record
        self.stmt.write_bytes(self.stmt_bytes); git(self.work, "add", self.stmt.name, "ADOPTED_RULE_SHA256.txt"); git(self.work, "commit", "-q", "-m", "approval"); self.commit = git(self.work, "rev-parse", "HEAD"); git(self.work, "push", "-q", "origin", "HEAD:refs/heads/main")
        B19.WITNESS_REMOTE_REF = "origin/main"; B19.WITNESS_REMOTE_URL = str(bare); B19.APPROVAL_GLOB = "APPROVAL_RECORD_SELRULE_V19*"; B19.WITNESS_FETCH = True; B19.BRANCH_REF = "refs/heads/main"; B19.nist_pulse.pinned_roots = pki.roots
        self.when = TP - timedelta(minutes=3); B19.EVENTS = lambda: ([{"type": "PushEvent", "id": "1", "created_at": self.when.strftime("%Y-%m-%dT%H:%M:%SZ"), "repo": {"name": "t"}, "actor": {"login": "t"}, "payload": {"ref": "refs/heads/main", "head": self.commit, "commits": [{"sha": self.commit}]}}], {"endpoints": ["e"], "retrieved_utc": "x", "gh_version": "gh test"})
        B19.COLLECTION_LOG = self.tmp / "collection_log.jsonl"
        self.n = net(); rec = X.collect(self.n, X.fmt(T_SIGN), D, self.stmt_bytes, now=SOON); self.rec = self.tmp / "rec.json"; self.rec.write_text(json.dumps(rec))
    def log(self): return [json.loads(l) for l in B19.COLLECTION_LOG.read_text().splitlines()] if B19.COLLECTION_LOG.is_file() else []
    def test_accepted_witnessed_locked_history(self):
        B, raw, r = B19._validate_beacon_record(self.rec, D, self.stmt, fetch=self.n, now=SOON)
        self.assertEqual(r["outcome"], "ACCEPT-DRAND"); self.assertEqual(r["approval_witness"]["push_event"]["repo"]["name"], "t"); self.assertEqual(r["approval_witness"]["events_provenance"]["gh_version"], "gh test")
        L = self.log(); self.assertEqual([e["stage"] for e in L], ["builder-verdict", "builder-accept"]); self.assertEqual(r["collection_lock"]["first_accept"]["stage"], "builder-accept")
        B19._validate_beacon_record(self.rec, D, self.stmt, fetch=self.n, now=SOON)                 # replay: verdict logged again, still ONE accept
        L = self.log(); self.assertEqual([e["stage"] for e in L], ["builder-verdict", "builder-accept", "builder-verdict"])
    def test_every_attempt_is_logged_including_retry_and_refusals(self):
        def http500(url, timeout=30):
            if "beacon.nist" in url: raise urllib.error.HTTPError(url, 500, "boom", None, None)
            return self.n(url, timeout)
        with self.assertRaises(SystemExit) as cm: B19._validate_beacon_record(self.rec, D, self.stmt, fetch=http500, now=SOON)
        self.assertIn("BEACON-NOT-ACCEPTED", str(cm.exception)); self.assertEqual(self.log()[-1]["outcome"], "RETRY")
        self.when = TP + timedelta(seconds=30)
        with self.assertRaises(SystemExit) as cm: B19._validate_beacon_record(self.rec, D, self.stmt, fetch=self.n, now=SOON)
        self.assertIn("APPROVAL-PUSHED-AFTER-T-PULSE", str(cm.exception)); self.assertEqual(self.log()[-1]["stage"], "builder-witness-or-adoption"); self.assertIn("PUSHED-AFTER", self.log()[-1]["refusal"])
        self.assertEqual([e["stage"] for e in self.log()], ["builder-verdict", "builder-verdict", "builder-witness-or-adoption"])   # RETRY attempt, then ACCEPT verdict + witness refusal: every attempt present
    def test_conflicting_later_accept_is_logged_and_locked(self):
        B19._validate_beacon_record(self.rec, D, self.stmt, fetch=self.n, now=SOON)
        n2 = net(pki.network(TP, drand=(RND, "c" * 64)))                                          # NIST now authenticable → a fresh record would ACCEPT-NIST
        rec2 = X.collect(n2, X.fmt(T_SIGN), D, self.stmt_bytes, now=SOON); p2 = self.tmp / "rec2.json"; p2.write_text(json.dumps(rec2))
        with self.assertRaises(SystemExit) as cm: B19._validate_beacon_record(p2, D, self.stmt, fetch=n2, now=SOON)
        self.assertIn("COLLECTION-LOCKED", str(cm.exception)); self.assertEqual(self.log()[-1]["stage"], "builder-conflict")
    def test_adoption_must_be_a_blob_at_the_approval_commit(self):
        B19.ADOPTION_FILE.write_text(D + "\n\n")
        with self.assertRaises(SystemExit) as cm: B19._validate_beacon_record(self.rec, D, self.stmt, fetch=self.n, now=SOON)
        self.assertIn("ADOPTION-MALFORMED", str(cm.exception))
        B19.ADOPTION_FILE.write_text(D + "\n"); other = self.tmp / "ADOPTED_RULE_SHA256.txt"; other.write_text(D + "\n"); B19.ADOPTION_FILE = other      # outside the worktree
        with self.assertRaises(SystemExit) as cm: B19._validate_beacon_record(self.rec, D, self.stmt, fetch=self.n, now=SOON)
        self.assertIn("ADOPTION-NOT-IN-REPO", str(cm.exception))
        B19.ADOPTION_FILE = self.work / "ADOPTED_RULE_SHA256.txt"; B19.ADOPTION_FILE.write_text(D + "\n")
        # an adoption file that is committed LATER than the approval commit is not a blob at that commit → refused
        git(self.work, "rm", "-q", "--cached", "ADOPTED_RULE_SHA256.txt"); git(self.work, "commit", "-q", "--amend", "-m", "approval without adoption"); c2 = git(self.work, "rev-parse", "HEAD")
        git(self.work, "add", "ADOPTED_RULE_SHA256.txt"); git(self.work, "commit", "-q", "-m", "adoption later"); git(self.work, "push", "-q", "-f", "origin", "HEAD:refs/heads/main"); self.commit = c2
        with self.assertRaises(SystemExit) as cm: B19._validate_beacon_record(self.rec, D, self.stmt, fetch=self.n, now=SOON)
        self.assertIn("ADOPTION-NOT-AT-APPROVAL-COMMIT", str(cm.exception))
    def test_identity_carries_lock_t_pulse_and_adoption(self):
        B, raw, r = B19._validate_beacon_record(self.rec, D, self.stmt, fetch=self.n, now=SOON)
        self.assertEqual(r["t_pulse"], X.fmt(TP)); self.assertEqual(r["collection_lock"]["first_accept"]["record_sha256"], __import__("hashlib").sha256(raw).hexdigest())
if __name__ == "__main__": unittest.main()
