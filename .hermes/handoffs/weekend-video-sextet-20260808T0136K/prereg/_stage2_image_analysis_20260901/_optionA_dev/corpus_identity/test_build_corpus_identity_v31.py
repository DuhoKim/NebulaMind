"""V21 builder: authenticated history (genesis by the collector; chained; atomic first accept), witness v4 with a REAL BLS-verified nonce (round 6441904, pinned bodies), every path logged. V20 was: DRAND-ONLY verdict on the real retained round 6441924 (BLS-verified under the pinned key; the exhibit-round exclusion lifted only here) + approval_witness_v3 + COLLECTION HISTORY (every attempt
logged; first ACCEPT binding; conflict logged) + ADOPTION verified as a blob at the approval commit. Real git clone with a bare origin;
three-tier test PKI; no network."""
import json, unittest, tempfile, sys, subprocess, os, urllib.error
from datetime import datetime, timezone, timedelta
from pathlib import Path
HERE = Path(__file__).resolve().parent; sys.path.insert(0, str(HERE)); sys.path.insert(0, str(HERE.parent / "beacon_v2"))
sys.path.insert(0, str(HERE.parent / "drand_only"))
import beacon_record_drand_v31 as X, verify_drand_v2 as vd, history_v2 as H
import build_corpus_identity_v31 as B19
ROUND = 6441924; REAL = json.loads((HERE.parent / "drand_only" / "round_6441924_api.drand.sh.json").read_text()); BODY = json.dumps(REAL).encode()
TP = vd.round_time(ROUND); T_SIGN = TP - timedelta(seconds=600); D = "b" * 64; RND = ROUND; R_SIGN = vd.round_for(T_SIGN); SOON = TP + timedelta(minutes=1)
NB = {h: (HERE.parent / "drand_only" / f"round_6441904_{h.split('//')[1]}.json").read_bytes() for h in ("https://api.drand.sh", "https://api2.drand.sh")}; NONCE = json.loads(NB["https://api.drand.sh"])["randomness"]; assert R_SIGN == 6441904
def git(cwd, *a): return subprocess.run(["git", *a], cwd=cwd, capture_output=True, text=True, check=True).stdout.strip()
def net(base=None):
    def fetch(url, timeout=30):
        for h, b in NB.items():
            if url == vd.round_url(h, R_SIGN): return b
        for host in vd.RELAYS:
            if url == vd.round_url(host, ROUND): return BODY
        raise OSError("404 " + url)
    return fetch
class T(unittest.TestCase):
    def setUp(self):
        self.tmp = Path(tempfile.mkdtemp()); bare = self.tmp / "remote.git"; self.work = self.tmp / "work"
        subprocess.run(["git", "init", "-q", "--bare", str(bare)], check=True); subprocess.run(["git", "clone", "-q", str(bare), str(self.work)], check=True, capture_output=True)
        git(self.work, "config", "user.email", "t@t"); git(self.work, "config", "user.name", "t"); (self.work / "seed").write_text("x"); git(self.work, "add", "seed"); git(self.work, "commit", "-q", "-m", "init"); git(self.work, "push", "-q", "-u", "origin", "HEAD:refs/heads/main")
        self.stmt = self.work / "APPROVAL_RECORD_SELRULE_V22_TEST.md"; self.stmt_bytes = f"RULE_SHA256: {D}\nAPPROVAL_UTC: {X.fmt(T_SIGN)}\nDRAND_AT_APPROVAL: round {R_SIGN} randomness {NONCE}\n".encode()
        B19.ADOPTION_FILE = self.work / "ADOPTED_RULE_SHA256.txt"; B19.ADOPTION_FILE.write_text(D + "\n")           # committed WITH the approval record
        self.stmt.write_bytes(self.stmt_bytes); git(self.work, "add", self.stmt.name, "ADOPTED_RULE_SHA256.txt"); git(self.work, "commit", "-q", "-m", "approval"); self.commit = git(self.work, "rev-parse", "HEAD"); git(self.work, "push", "-q", "origin", "HEAD:refs/heads/main")
        B19.WITNESS_REMOTE_REF = "origin/main"; B19.WITNESS_REMOTE_URL = str(bare); B19.APPROVAL_GLOB = "APPROVAL_RECORD_SELRULE_V22*"; B19.WITNESS_FETCH = True; B19.BRANCH_REF = "refs/heads/main"; self._ex = X.EXCLUDED_ROUNDS; X.EXCLUDED_ROUNDS = (6440756,)
        self.when = TP - timedelta(minutes=3); B19.EVENTS = lambda: ([{"type": "PushEvent", "id": "1", "created_at": self.when.strftime("%Y-%m-%dT%H:%M:%SZ"), "repo": {"name": "t"}, "actor": {"login": "t"}, "payload": {"ref": "refs/heads/main", "head": self.commit, "commits": [{"sha": self.commit}]}}], {"endpoints": ["e"], "retrieved_utc": "x", "gh_version": "gh test"})
        B19.COLLECTION_LOG = self.tmp / "collection_log.jsonl"; self.n = net(); self.rec = self.tmp / "rec.json"
        import unittest.mock as um
        import urllib.request, io
        class _R(io.BytesIO):
            def __enter__(self): return self
            def __exit__(self, *a): return False
        with um.patch.object(X, "datetime") as dt, um.patch.object(urllib.request, "urlopen", lambda url, timeout=30: _R(self.n(url))):   # the COLLECTOR initiates the history (genesis) and logs its collect
            dt.now.return_value = SOON; dt.strptime = datetime.strptime
            self.assertEqual(X.main(["collect", "--t-sign", X.fmt(T_SIGN), "--rule-sha256", D, "--signature-statement", str(self.stmt), "--out", str(self.rec), "--log", str(B19.COLLECTION_LOG)]), 0)
    def tearDown(self): X.EXCLUDED_ROUNDS = self._ex
    def log(self): return H.validate(B19.COLLECTION_LOG)[1:] if B19.COLLECTION_LOG.is_file() else []       # entries after the genesis (chain validated every read)
    def test_accepted_witnessed_locked_history(self):
        B, raw, r = B19._validate_beacon_record(self.rec, D, self.stmt, fetch=self.n, now=SOON)
        self.assertEqual(r["outcome"], "ACCEPT-DRAND"); self.assertEqual(r["approval_witness"]["push_event"]["repo"]["name"], "t"); self.assertEqual(r["approval_witness"]["events_provenance"]["gh_version"], "gh test")
        L = self.log(); self.assertEqual([e["stage"] for e in L], ["collector-collect", "builder-verdict", "builder-accept"]); self.assertEqual(r["collection_lock"]["first_accept"]["stage"], "builder-accept"); self.assertEqual(r["collection_lock"]["entries"], 4)
        self.assertEqual(r["approval_witness"]["witness_version"], 4); self.assertEqual(len(r["approval_witness"]["nonce_bodies_b64"]), 2)
        B19._validate_beacon_record(self.rec, D, self.stmt, fetch=self.n, now=SOON)                 # replay: verdict logged again, still ONE accept
        L = self.log(); self.assertEqual([e["stage"] for e in L], ["collector-collect", "builder-verdict", "builder-accept", "builder-verdict"])
    def test_every_attempt_is_logged_including_retry_and_refusals(self):
        def http500(url, timeout=30):
            if "drand" in url and "/public/" + str(ROUND) in url: raise urllib.error.HTTPError(url, 500, "boom", None, None)
            return self.n(url, timeout)
        with self.assertRaises(SystemExit) as cm: B19._validate_beacon_record(self.rec, D, self.stmt, fetch=http500, now=SOON)
        self.assertIn("BEACON-NOT-ACCEPTED", str(cm.exception)); self.assertEqual(self.log()[-1]["outcome"], "RETRY")
        self.when = TP + timedelta(seconds=30)
        with self.assertRaises(SystemExit) as cm: B19._validate_beacon_record(self.rec, D, self.stmt, fetch=self.n, now=SOON)
        self.assertIn("APPROVAL-PUSHED-AFTER-T-PULSE", str(cm.exception)); self.assertEqual(self.log()[-1]["stage"], "witness-closed"); self.assertIn("PUSHED-AFTER", self.log()[-1]["refusal"])
        B19.EVENTS = lambda: ([], {"endpoints": ["e"], "retrieved_utc": "x", "gh_version": "gh test"})                       # no event yet: PENDING persisted; CLOSED persisted after the latency window
        with self.assertRaises(SystemExit) as cm: B19._validate_beacon_record(self.rec, D, self.stmt, fetch=self.n, now=SOON)
        self.assertEqual(self.log()[-1]["stage"], "witness-pending")
        with self.assertRaises(SystemExit) as cm: B19._validate_beacon_record(self.rec, D, self.stmt, fetch=self.n, now=TP + timedelta(hours=7))
        self.assertEqual(self.log()[-1]["stage"], "witness-closed")
        self.assertEqual([e["stage"] for e in self.log()], ["collector-collect", "builder-verdict", "builder-verdict", "witness-closed", "builder-verdict", "witness-pending", "builder-verdict", "witness-closed"])   # every attempt present, chained
        lines = B19.COLLECTION_LOG.read_bytes().split(b"\n"); del lines[2]; B19.COLLECTION_LOG.write_bytes(b"\n".join(lines))            # a deleted entry breaks the chain: refused, disclosed beside the log
        with self.assertRaises(SystemExit) as cm: B19._validate_beacon_record(self.rec, D, self.stmt, fetch=self.n, now=SOON)
        self.assertIn("HISTORY-INVALID", str(cm.exception)); self.assertTrue(Path(str(B19.COLLECTION_LOG) + ".pregenesis.jsonl").is_file())
    def test_conflicting_later_accept_is_logged_and_locked(self):
        B19._validate_beacon_record(self.rec, D, self.stmt, fetch=self.n, now=SOON)
        n2 = net(); rec2 = X.collect(n2, X.fmt(T_SIGN), D, self.stmt_bytes, now=SOON + timedelta(hours=1)); p2 = self.tmp / "rec2.json"; p2.write_text(json.dumps(rec2))   # a second collection: same seed, different record bytes
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
        self.assertEqual(r["t_pulse"], X.fmt(TP)); self.assertEqual(r["collection_lock"]["first_accept"]["record_sha256"], __import__("hashlib").sha256(raw).hexdigest()); self.assertEqual(r["seed_hex"], REAL["randomness"])
    def test_pre_parse_failure_is_logged(self):
        with self.assertRaises(SystemExit) as cm: B19._validate_beacon_record(self.tmp / "nope.json", D, self.stmt, fetch=self.n, now=SOON)
        self.assertIn("BEACON-RECORD-INVALID", str(cm.exception)); self.assertEqual(self.log()[-1]["stage"], "builder-pre-parse-refusal")
    def test_any_other_exception_is_logged_as_builder_error(self):
        import unittest.mock as um
        with um.patch.object(B19.beacon_record, "verdict", side_effect=RuntimeError("boom")):
            with self.assertRaises(SystemExit) as cm: B19._validate_beacon_record(self.rec, D, self.stmt, fetch=self.n, now=SOON)
        self.assertIn("BUILDER-ERROR", str(cm.exception)); self.assertEqual(self.log()[-1]["stage"], "builder-error")
    def test_history_for_another_approval_is_refused(self):
        other = self.work / "APPROVAL_RECORD_SELRULE_V22_OTHER.md"; other.write_bytes(self.stmt_bytes + b"\n")
        with self.assertRaises(SystemExit) as cm: B19._validate_beacon_record(self.rec, D, other, fetch=self.n, now=SOON)
        self.assertIn("HISTORY-GENESIS-MISMATCH", str(cm.exception))
if __name__ == "__main__": unittest.main()
