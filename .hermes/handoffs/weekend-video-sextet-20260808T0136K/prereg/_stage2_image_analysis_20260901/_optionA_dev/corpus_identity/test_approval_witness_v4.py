"""approval_witness_v4: real git clone + bare origin; nonce = the REAL public round 6441904 (pinned bodies from two relays; chain-hash path), seed round 6441924."""
import json, unittest, tempfile, subprocess, sys, base64
from datetime import datetime, timezone, timedelta
from pathlib import Path
HERE = Path(__file__).resolve().parent; sys.path.insert(0, str(HERE)); sys.path.insert(0, str(HERE.parent / "drand_only"))
import approval_witness_v4 as AW, verify_drand_v2 as vd
SEED_ROUND = 6441924; NR = 6441904; DO = HERE.parent / "drand_only"
NB = {"https://api.drand.sh": (DO / "round_6441904_api.drand.sh.json").read_bytes(), "https://api2.drand.sh": (DO / "round_6441904_api2.drand.sh.json").read_bytes()}
NONCE = json.loads(NB["https://api.drand.sh"])["randomness"]; TP = vd.round_time(SEED_ROUND); T_SIGN = TP - timedelta(seconds=600); D = "b" * 64; MIN = "2026-09-01T00:00:00Z"
assert vd.round_for(T_SIGN) == NR
def git(cwd, *a): return subprocess.run(["git", *a], cwd=cwd, capture_output=True, text=True, check=True).stdout.strip()
def net(bad=False):
    def fetch(url, timeout=30):
        for h, b in NB.items():
            if url == vd.round_url(h, NR): return (json.dumps({**json.loads(b), "signature": "00"}).encode() if bad else b)
        raise OSError("404 " + url)
    return fetch
class T(unittest.TestCase):
    def setUp(self):
        self.tmp = Path(tempfile.mkdtemp()); bare = self.tmp / "remote.git"; self.work = self.tmp / "work"; self.bare = str(bare)
        subprocess.run(["git", "init", "-q", "--bare", str(bare)], check=True); subprocess.run(["git", "clone", "-q", str(bare), str(self.work)], check=True, capture_output=True)
        git(self.work, "config", "user.email", "t@t"); git(self.work, "config", "user.name", "t"); (self.work / "seed").write_text("x"); git(self.work, "add", "seed"); git(self.work, "commit", "-q", "-m", "init"); self.base = git(self.work, "rev-parse", "HEAD"); git(self.work, "push", "-q", "-u", "origin", "HEAD:refs/heads/main")
        self.stmt = self.work / "APPROVAL_RECORD_SELRULE_V21_TEST.md"; self.stmt.write_bytes(f"RULE_SHA256: {D}\nAPPROVAL_UTC: {T_SIGN.strftime('%Y-%m-%dT%H:%M:%SZ')}\nDRAND_AT_APPROVAL: round {NR} randomness {NONCE}\n".encode())
        git(self.work, "add", self.stmt.name); git(self.work, "commit", "-q", "-m", "approval"); self.commit = git(self.work, "rev-parse", "HEAD")
        (self.work / "later").write_text("y"); git(self.work, "add", "later"); git(self.work, "commit", "-q", "-m", "later"); self.head = git(self.work, "rev-parse", "HEAD"); git(self.work, "push", "-q", "origin", "HEAD:refs/heads/main")
        self.when = (TP - timedelta(minutes=3)).strftime("%Y-%m-%dT%H:%M:%SZ")
    def ev(self, **kw):
        e = {"type": "PushEvent", "id": "1", "created_at": self.when, "payload": {"ref": "refs/heads/main", "head": self.commit, "commits": [{"sha": self.commit}]}}; e["payload"].update(kw); return e
    def run_v(self, events, fetch=None, now=None, **kw):
        return AW.verify(self.stmt, T_SIGN, TP, SEED_ROUND, D, fetch or net(), "origin/main", self.bare, MIN, "APPROVAL_RECORD_SELRULE_V21*", events, "refs/heads/main", provenance={"e": 1}, now=now or TP + timedelta(minutes=1), **kw)
    def test_ok_retains_verified_nonce_bodies_and_redelivery_by_ancestry(self):
        w = self.run_v([self.ev()]); self.assertEqual(w["nonce_round"], NR); self.assertEqual(sorted(w["nonce_bodies_b64"]), sorted(vd.round_url(h, NR) for h in NB)); self.assertEqual(w["record_sha256"], __import__("hashlib").sha256(self.stmt.read_bytes()).hexdigest())
        self.assertEqual(AW.verify_nonce_bodies(w["nonce_bodies_b64"], NR, NONCE), w["nonce_verified_urls"]); self.assertEqual(AW.verify_nonce_bodies(w["nonce_bodies_b64"], NR, "0" * 64), [])
        anc = self.ev(head=self.head, commits=[{"sha": self.head}], before=self.base)                         # payload omits the approval commit; before..head covers it
        self.assertEqual(self.run_v([anc])["commit"], self.commit)
        notanc = self.ev(head=self.head, commits=[{"sha": self.head}], before=self.commit)                     # before == commit: NOT delivered by this push
        with self.assertRaises(AW.ApprovalRefused) as cm: self.run_v([notanc])
        self.assertIn("PUSH-EVENT-PENDING", str(cm.exception)); self.assertEqual(cm.exception.state, "PENDING")
    def test_pending_then_closed_and_after_t_pulse(self):
        with self.assertRaises(AW.ApprovalRefused) as cm: self.run_v([], now=TP + timedelta(hours=5))
        self.assertEqual(cm.exception.state, "PENDING")
        with self.assertRaises(AW.ApprovalRefused) as cm: self.run_v([], now=TP + timedelta(hours=7))
        self.assertEqual(cm.exception.state, "CLOSED"); self.assertIn("PUSH-EVENT-CLOSED", str(cm.exception))
        self.when = TP.strftime("%Y-%m-%dT%H:%M:%SZ")
        with self.assertRaises(AW.ApprovalRefused) as cm: self.run_v([self.ev()])
        self.assertIn("PUSHED-AFTER-T-PULSE", str(cm.exception)); self.assertEqual(cm.exception.state, "CLOSED")
    def test_nonce_round_set_bound_and_authentication(self):
        for R in (NR - 2, NR + 1, SEED_ROUND):
            self.stmt.write_bytes(self.stmt.read_bytes().replace(f"round {NR}".encode(), f"round {R}".encode())); git(self.work, "commit", "-q", "-am", "x"); git(self.work, "push", "-q", "origin", "HEAD:refs/heads/main")
            with self.assertRaises(AW.ApprovalRefused) as cm: self.run_v([self.ev()])
            self.assertIn("RECORD-MODIFIED", str(cm.exception))                                                  # W1 fires first: a rewritten record is refused before the nonce is read
            git(self.work, "reset", "-q", "--hard", self.head); git(self.work, "push", "-q", "-f", "origin", "HEAD:refs/heads/main")
        with self.assertRaises(AW.ApprovalRefused) as cm: self.run_v([self.ev()], fetch=net(bad=True))            # relays serve a non-verifying nonce body
        self.assertIn("NONCE-UNAUTHENTICATED", str(cm.exception))
        s2 = self.work / "APPROVAL_RECORD_SELRULE_V21B_TEST.md"; s2.write_bytes(self.stmt.read_bytes().replace(f"round {NR}".encode(), f"round {NR - 1}".encode()))   # a second version's record naming the predecessor round
        git(self.work, "add", s2.name); git(self.work, "commit", "-q", "-m", "approval B"); cB = git(self.work, "rev-parse", "HEAD"); git(self.work, "push", "-q", "origin", "HEAD:refs/heads/main")
        evB = {"type": "PushEvent", "id": "2", "created_at": self.when, "payload": {"ref": "refs/heads/main", "head": cB, "commits": [{"sha": cB}]}}
        with self.assertRaises(AW.ApprovalRefused) as cm: AW.verify(s2, T_SIGN, TP, SEED_ROUND, D, net(), "origin/main", self.bare, (T_SIGN - timedelta(seconds=10)).strftime("%Y-%m-%dT%H:%M:%SZ"), "APPROVAL_RECORD_SELRULE_V21B*", [evB], "refs/heads/main", now=TP)
        self.assertIn("NONCE-ROUND", str(cm.exception)); self.assertIn("before MIN_T_SIGN", str(cm.exception))    # round NR-1 was scheduled 30 s before T_sign: with MIN_T_SIGN 10 s before T_sign the nonce predates the amendment
        self.assertEqual(AW.push_event_for([self.ev(), {**self.ev(), "created_at": "2020-01-01T00:00:00Z"}], self.commit, "refs/heads/main"), {**self.ev(), "created_at": "2020-01-01T00:00:00Z"})
if __name__ == "__main__": unittest.main()
