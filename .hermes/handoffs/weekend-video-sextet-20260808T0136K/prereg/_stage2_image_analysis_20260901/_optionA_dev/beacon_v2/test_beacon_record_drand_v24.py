"""drand-only beacon fixture (run under _optionA_dev/_venv_bls). The 'archive' is the REAL retained public round 6441924 (BLS-verifying under the
pinned key) served by mock relays at the chain-hash path; T_sign is chosen so that round_for(T_pulse) == 6441924 (the exclusion of that round is
lifted ONLY inside this fixture, so the real signature exercises real verification). Asserts: ACCEPT-DRAND with the round's randomness; identical at
two clock times and with/without live re-fetch; one relay garbage → still ACCEPT (quorum); one relay only → RETRY; tampered body → RETRY (fails BLS);
wrong chain path → not counted; clock-first; statement binding; exclusions and MIN_T_SIGN; every REFUSE token exercised; CLI logs every attempt."""
import json, hashlib, unittest, sys, re, tempfile
from datetime import datetime, timezone, timedelta
from pathlib import Path
HERE = Path(__file__).resolve().parent; sys.path.insert(0, str(HERE)); sys.path.insert(0, str(HERE.parent / "drand_only"))
import beacon_record_drand_v24 as BD, verify_drand_v2 as vd
ROUND = 6441924; REAL = json.loads((HERE.parent / "drand_only" / "round_6441924_api.drand.sh.json").read_text()); BODY = json.dumps(REAL).encode()
TP = vd.round_time(ROUND); T_SIGN = TP - timedelta(seconds=600); TS = BD.fmt(T_SIGN); D = "b" * 64; STMT = f"V20 {D} {TS}".encode(); SOON = TP + timedelta(minutes=1)
assert vd.round_for(vd.pulse_time(T_SIGN)) == ROUND
EX = set()
def relays(bodies_by_host=None, default=BODY):
    def fetch(url, timeout=30):
        for host in vd.RELAYS:
            if url == vd.round_url(host, ROUND):
                b = (bodies_by_host or {}).get(host, default)
                if b is None: raise OSError("down")
                return b
        raise OSError("404 " + url)
    return fetch
def V(rec, now, fetch=None):
    r = BD.verdict(rec, now, fetch=fetch, rule_sha256=D, statement_bytes=STMT); EX.add(r["outcome"]); return r
class T(unittest.TestCase):
    def setUp(self): self._ex = BD.EXCLUDED_ROUNDS; BD.EXCLUDED_ROUNDS = (6440756,)      # lift the exhibit-round exclusion for the fixture only
    def tearDown(self): BD.EXCLUDED_ROUNDS = self._ex
    def test_real_round_verifies_and_is_identical_at_two_times(self):
        n = relays(); rec = BD.collect(n, TS, D, STMT, now=SOON); self.assertEqual(rec["schema"], "BEACON-RECORD-4"); self.assertEqual(rec["round"], ROUND)
        r1 = V(rec, SOON, fetch=n); r2 = V(rec, SOON + timedelta(days=30), fetch=n); r3 = V(rec, SOON)
        for r in (r1, r2, r3): self.assertEqual(r["outcome"], "ACCEPT-DRAND"); self.assertEqual(r["seed_hex"], REAL["randomness"]); self.assertEqual(len(r["verified_relays"]), 4)
        self.assertEqual({k: r1[k] for k in ("outcome", "seed_hex", "round")}, {k: r2[k] for k in ("outcome", "seed_hex", "round")})
    def test_quorum_and_transport_faults(self):
        n = relays({"https://api3.drand.sh": b"garbage", "https://drand.cloudflare.com": None}); rec = BD.collect(n, TS, D, STMT, now=SOON)
        self.assertEqual(V(rec, SOON, fetch=n)["outcome"], "ACCEPT-DRAND")                                   # 2 good relays suffice
        n1 = relays({"https://api2.drand.sh": None, "https://api3.drand.sh": None, "https://drand.cloudflare.com": None}); rec1 = BD.collect(n1, TS, D, STMT, now=SOON)
        self.assertEqual(V(rec1, SOON, fetch=n1)["outcome"], "RETRY")                                         # one relay only
        t = dict(REAL); t["signature"] = REAL["signature"][:-2] + "00"; nt = relays(default=json.dumps(t).encode()); rect = BD.collect(nt, TS, D, STMT, now=SOON)
        self.assertEqual(V(rect, SOON, fetch=nt)["outcome"], "RETRY")                                          # all relays serve a tampered body: nothing verifies
        n = relays(); rec = BD.collect(n, TS, D, STMT, now=SOON); down = relays({h: None for h in ("https://api.drand.sh", "https://api2.drand.sh", "https://api3.drand.sh")})
        self.assertEqual(V(rec, SOON, fetch=down)["outcome"], "RETRY")                                         # live quorum lost → RETRY, never a different value
    def test_clock_first_and_bindings(self):
        n = relays(); rec = BD.collect(n, TS, D, STMT, now=SOON)
        self.assertEqual(V(rec, TP - timedelta(seconds=1), fetch=n)["outcome"], "RETRY")
        with self.assertRaises(SystemExit) as cm: BD.collect(n, TS, D, STMT, now=TP - timedelta(seconds=1))
        self.assertIn("BEACON-NOT-YET", str(cm.exception))
        with self.assertRaises(SystemExit): BD.collect(n, TS, D, b"unbound", now=SOON)
        for k, v, tok in (("schema", "X", "REFUSE-SCHEMA"), ("T_sign", "garbage", "REFUSE-T-SIGN"), ("T_pulse", "2026-01-01T00:00:00Z", "REFUSE-T-PULSE"), ("rule_sha256", "d" * 64, "REFUSE-RULE-DIGEST")):
            b = dict(rec); b[k] = v; self.assertEqual(V(b, SOON)["outcome"], tok, k)
        self.assertEqual(BD.verdict(rec, SOON, rule_sha256=D, statement_bytes=b"other")["outcome"], "REFUSE-STATEMENT-BYTES"); EX.add("REFUSE-STATEMENT-BYTES")
        b = dict(rec); b["statement_b64"] = BD.b64(b"unbound"); self.assertEqual(BD.verdict(b, SOON)["outcome"], "REFUSE-STATEMENT-BINDING"); EX.add("REFUSE-STATEMENT-BINDING")
        old = BD.MIN_T_SIGN; BD.MIN_T_SIGN = "2099-01-01T00:00:00Z"
        try: self.assertEqual(V(rec, SOON)["outcome"], "REFUSE-T-SIGN-PREDATES-AMENDMENT")
        finally: BD.MIN_T_SIGN = old
        BD.EXCLUDED_ROUNDS = (ROUND,); self.assertEqual(V(rec, SOON)["outcome"], "REFUSE-T-PULSE-EXCLUDED")
        with self.assertRaises(SystemExit) as cm: BD.collect(n, TS, D, STMT, now=SOON)
        self.assertIn("T-PULSE-EXCLUDED", str(cm.exception))
    def test_same_signature_reencoded_is_the_same_value_and_conflicting_valid_signatures_refuse(self):   # V21 (codex V20 X): seed-uniqueness, not byte-uniqueness
        n = relays(); rec = BD.collect(n, TS, D, STMT, now=SOON)
        alt = dict(REAL); alt["extra"] = 1                                                                            # same valid signature, different bytes
        r = V(rec, SOON, fetch=relays(default=json.dumps(alt).encode())); self.assertEqual(r["outcome"], "ACCEPT-DRAND"); self.assertEqual(len(r["checks"]["live_representation_differs"]), 4)
        import unittest.mock as um
        with um.patch.object(vd, "verify", lambda resp, rnd, url: {"accepted": True, "seed_hex": REAL["randomness"] if resp.get("signature") == REAL["signature"] else "1" * 64}):
            forged = dict(REAL); forged["signature"] = "ab" * 48; self.assertEqual(V(rec, SOON, fetch=relays(default=json.dumps(forged).encode()))["outcome"], "REFUSE-CONFLICTING-VALID-SIGNATURES")   # a verifier that accepted two signatures for one round (cannot happen under one key; simulated)
        self.assertEqual(V(rec, SOON, fetch=relays(default=b"[1,2]"))["outcome"], "RETRY")                          # live JSON that is not an object: not counted, never an escape
        self.assertEqual(V(rec, SOON, fetch=relays(default=b"{\"round\": \"x\"}"))["outcome"], "RETRY")
    def test_unpinned_urls_and_lookalike_hosts_are_not_counted(self):                                            # V21 (codex V20 U): exact URL membership
        n = relays(); rec = BD.collect(n, TS, D, STMT, now=SOON); body = rec["relays"][vd.round_url("https://api.drand.sh", ROUND)]
        rec["relays"] = {"https://api.drand.sh.attacker.invalid/" + vd.CHAIN_HASH + "/public/" + str(ROUND): body, vd.round_url("https://api.drand.sh", ROUND) + "/x": body, vd.round_url("https://api2.drand.sh", ROUND): body}
        r = V(rec, SOON); self.assertEqual(r["outcome"], "RETRY"); self.assertEqual(sum(1 for c in r["checks"]["retained"].values() if c["accepted"]), 1)
    def test_cli_logs_every_attempt(self):
        d = Path(tempfile.mkdtemp()); stmt = d / "s.txt"; stmt.write_bytes(STMT); logp = d / "log.jsonl"; rec = BD.collect(relays(), TS, D, STMT, now=SOON); p = d / "rec.json"; p.write_text(json.dumps(rec))
        import unittest.mock as um
        with um.patch.object(BD, "datetime") as dt:
            dt.now.return_value = SOON; dt.strptime = datetime.strptime
            rc = BD.main(["verify", "--record", str(p), "--rule-sha256", D, "--signature-statement", str(stmt), "--no-live", "--log", str(logp)])
            with self.assertRaises(SystemExit): BD.main(["verify", "--record", str(d / "missing.json"), "--rule-sha256", D, "--signature-statement", str(stmt), "--no-live", "--log", str(logp)])
        import history as H; L = H.validate(logp); self.assertEqual(rc, 0); self.assertEqual([e["stage"] for e in L], ["genesis", "collector-verify", "collector-error"]); self.assertEqual(L[1]["outcome"], "ACCEPT-DRAND")
        self.assertEqual(L[0]["approval_record_sha256"], hashlib.sha256(STMT).hexdigest()); self.assertEqual(L[0]["round"], ROUND)
        other = d / "other.txt"; other.write_bytes(b"different statement " + D.encode() + b" " + TS.encode())
        with um.patch.object(BD, "datetime") as dt:
            dt.now.return_value = SOON; dt.strptime = datetime.strptime
            with self.assertRaises(SystemExit) as cm: BD.main(["verify", "--record", str(p), "--rule-sha256", D, "--signature-statement", str(other), "--no-live", "--log", str(logp)])
        self.assertIn("HISTORY-GENESIS-MISMATCH", str(cm.exception)); self.assertEqual(len(H.validate(logp)), 3)              # a history for another approval cannot be reused
        with self.assertRaises(SystemExit): BD.main(["verify", "--record", str(d / "missing.json"), "--rule-sha256", D, "--signature-statement", str(stmt), "--no-live", "--log", str(d / "fresh.jsonl")])
        self.assertTrue((d / "fresh.jsonl.pregenesis.jsonl").is_file())                                                          # a failure before genesis is disclosed outside the chain
    def test_zzz_every_token_exercised(self):
        src = (HERE / "beacon_record_drand_v24.py").read_text(); toks = {"REFUSE-" + t for t in re.findall(r'refuse\("([A-Z0-9-]+)"', src)} | {"ACCEPT-DRAND", "RETRY"}
        self.assertFalse(toks - EX, toks - EX)
if __name__ == "__main__": unittest.main()
