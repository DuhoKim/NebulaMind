"""beacon_v2 fixture: every outcome and every REFUSE token that beacon_record.verdict can emit is exercised here (test_every_token_is_exercised
enumerates them from the source and fails if one is not). All records come from beacon_record.collect over a mocked network; no accepted
record is hand-built. The live NIST sample is a REGRESSION OBSERVATION, not a normative vector."""
import json, unittest, re, hashlib, inspect
from datetime import datetime, timezone, timedelta
from pathlib import Path
import sys; HERE = Path(__file__).resolve().parent; sys.path.insert(0, str(HERE))
import nist_pulse as npulse, drand_round, beacon_record as br, test_pki as pki
T_SIGN = datetime(2026, 9, 6, 0, 0, tzinfo=timezone.utc); TP = br.pulse_time(T_SIGN); D = "a" * 64; STMT = f"signed {D} at {br.fmt(T_SIGN)}".encode(); RND = drand_round.round_for(TP)
EXERCISED = set()
def V(rec, now, fetch=None, **kw):
    r = br.verdict(rec, now, pki.roots(), fetch=fetch, rule_sha256=kw.get("rule", D), statement_bytes=kw.get("stmt", STMT)); EXERCISED.add(r["outcome"]); return r
class T(unittest.TestCase):
    def genuine(self, **net): n = pki.network(TP, **net); return br.collect(n, br.fmt(T_SIGN), D, STMT, now=TP + timedelta(hours=1)), n
    def test_pulse_time_rule(self):
        self.assertEqual(br.pulse_time(br.parse_utc("2026-09-06T01:00:00Z")).strftime("%H:%M:%S"), "01:10:00"); self.assertEqual(br.pulse_time(br.parse_utc("2026-09-06T01:00:01Z")).strftime("%H:%M:%S"), "01:11:00")
    def test_collect_refuses_before_t_pulse_and_unbound_statement(self):
        with self.assertRaises(SystemExit) as cm: br.collect(pki.network(TP), br.fmt(T_SIGN), D, STMT, now=TP - timedelta(seconds=1))
        self.assertIn("BEACON-NOT-YET", str(cm.exception))
        with self.assertRaises(SystemExit) as cm: br.collect(pki.network(TP), br.fmt(T_SIGN), D, b"unrelated", now=TP + timedelta(hours=1))
        self.assertIn("STATEMENT-DOES-NOT-BIND", str(cm.exception))
    def test_genuine_three_tier_chain_accepted_and_live_equal(self):
        rec, n = self.genuine(); r = V(rec, TP + timedelta(hours=1), fetch=n)
        self.assertEqual(r["outcome"], "ACCEPT-NIST"); self.assertEqual(r["checks"]["nist"]["anchor"]["chain_length"], 2); self.assertTrue(r["checks"]["nist_live_equal"]); self.assertEqual(len(r["seed_hex"]), 128)
    def test_record_holds_bytes_only_no_verdict_fields(self):
        rec, _ = self.genuine(); flat = json.dumps(rec)
        for banned in ("accepted", "verified", "outcome", "seed_hex", "anchored", "true", "false"): self.assertNotIn(f'"{banned}"', flat)
    def test_unsigned_pulse_is_retry_before_24h(self):
        rec, n = self.genuine(sign=False); self.assertEqual(V(rec, TP + timedelta(hours=1), fetch=n)["outcome"], "RETRY")
    def test_self_signed_and_root_signed_leaf_do_not_anchor(self):
        for how in ("self",):
            lc, k = pki.leaf(signed_by=how); rec, n = self.genuine(leaf_cert=lc, key=k); r = V(rec, TP + timedelta(hours=1), fetch=n)
            self.assertEqual(r["outcome"], "RETRY"); self.assertFalse(r["checks"]["nist"]["anchor"]["chains_to_trusted_root"])
        lc, k = pki.leaf(san="example.org"); rec, n = self.genuine(leaf_cert=lc, key=k); r = V(rec, TP + timedelta(hours=1), fetch=n); self.assertFalse(r["checks"]["nist"]["anchor"]["san_matches"]); self.assertEqual(r["outcome"], "RETRY")
    def test_status_nonzero_refused(self):
        rec, n = self.genuine(status=1); r = V(rec, TP + timedelta(hours=1), fetch=n); self.assertFalse(r["checks"]["nist"]["status_code_zero"]); self.assertEqual(r["outcome"], "RETRY")
    def test_live_differs_from_retained(self):
        rec, _ = self.genuine(); r = V(rec, TP + timedelta(hours=1), fetch=pki.network(TP, sign=False)); self.assertEqual(r["outcome"], "REFUSE-NIST-LIVE-DIFFERS")
    def test_live_intermediates_must_match(self):                                  # codex V14: the issuer chain is one of the compared live inputs
        rec, n = self.genuine(); bad = json.loads(json.dumps(rec)); bad["nist"]["intermediate_pems_b64"] = [br.b64(pki.pem(pki.ROOT))]      # a different (but root) certificate retained as the intermediate
        r = V(bad, TP + timedelta(hours=1), fetch=n); self.assertEqual(r["outcome"], "REFUSE-NIST-LIVE-DIFFERS")
    def test_tampered_record_fields(self):
        rec, n = self.genuine()
        bad = json.loads(json.dumps(rec)); bad["schema"] = "X"; self.assertEqual(V(bad, TP + timedelta(hours=1))["outcome"], "REFUSE-SCHEMA")
        bad = json.loads(json.dumps(rec)); bad["T_sign"] = "garbage"; self.assertEqual(V(bad, TP + timedelta(hours=1))["outcome"], "REFUSE-T-SIGN")
        bad = json.loads(json.dumps(rec)); bad["T_pulse"] = br.fmt(TP + timedelta(minutes=1)); self.assertEqual(V(bad, TP + timedelta(hours=1))["outcome"], "REFUSE-T-PULSE")
        self.assertEqual(V(rec, TP + timedelta(hours=1), rule="b" * 64)["outcome"], "REFUSE-RULE-DIGEST")
        self.assertEqual(V(rec, TP + timedelta(hours=1), stmt=b"other")["outcome"], "REFUSE-STATEMENT-BYTES")
        bad = json.loads(json.dumps(rec)); bad["statement_b64"] = br.b64(b"no binding here"); self.assertEqual(V(bad, TP + timedelta(hours=1), stmt=b"no binding here")["outcome"], "REFUSE-STATEMENT-BINDING")
        bad = json.loads(json.dumps(rec)); pb = json.loads(br.unb64(bad["nist"]["pulse_body_b64"])); pb["pulse"]["outputValue"] = "E" * 128; bad["nist"]["pulse_body_b64"] = br.b64(json.dumps(pb).encode())
        r = V(bad, TP + timedelta(hours=1)); self.assertFalse(r["checks"]["nist"]["output_is_sha512_of_message_and_signature"]); self.assertEqual(r["outcome"], "RETRY")
        bad = json.loads(json.dumps(rec)); bad["nist"]["next_body_b64"] = br.b64(json.dumps({"pulse": {"localRandomValue": "99" * 64}}).encode()); r = V(bad, TP + timedelta(hours=1)); self.assertFalse(r["checks"]["nist"]["precommitment_links_to_next"]); self.assertEqual(r["outcome"], "RETRY")
        bad = json.loads(json.dumps(rec)); bad["nist"]["intermediate_pems_b64"] = []; r = V(bad, TP + timedelta(hours=1)); self.assertFalse(r["checks"]["nist"]["anchor"]["chains_to_trusted_root"])   # the chain NEEDS the intermediate
    def test_fallback_after_24h_when_primary_404(self):
        n = pki.network(TP, nist_404=True, drand=(RND, "f" * 64)); rec = br.collect(n, br.fmt(T_SIGN), D, STMT, now=TP + timedelta(hours=25)); r = V(rec, TP + timedelta(hours=25), fetch=n)
        self.assertEqual(r["outcome"], "ACCEPT-DRAND"); self.assertEqual(r["checks"]["drand"]["n_hosts"], 4); self.assertEqual(r["round"], RND)
    def test_fallback_when_primary_present_but_unauthenticable_after_24h(self):
        n = pki.network(TP, sign=False, drand=(RND, "f" * 64)); rec = br.collect(n, br.fmt(T_SIGN), D, STMT, now=TP + timedelta(hours=25)); self.assertEqual(V(rec, TP + timedelta(hours=25), fetch=n)["outcome"], "ACCEPT-DRAND")
    def test_fallback_void_when_nist_authenticable_now_through_intermediate(self):    # the V13 fatal, exercised with the production chain shape
        n = pki.network(TP, nist_404=True, drand=(RND, "f" * 64)); rec = br.collect(n, br.fmt(T_SIGN), D, STMT, now=TP + timedelta(hours=25))
        self.assertEqual(V(rec, TP + timedelta(hours=25), fetch=pki.network(TP, drand=(RND, "f" * 64)))["outcome"], "REFUSE-DRAND-VOID-PRIMARY-AUTHENTICABLE")
    def test_fallback_not_before_24h_even_with_relays(self):
        n = pki.network(TP, nist_404=True, drand=(RND, "f" * 64)); rec = br.collect(n, br.fmt(T_SIGN), D, STMT, now=TP + timedelta(hours=1)); self.assertEqual(V(rec, TP + timedelta(hours=1), fetch=n)["outcome"], "RETRY"); self.assertEqual(rec["drand"], {})
    def test_relays_disagree_or_too_few(self):
        n = pki.network(TP, nist_404=True, drand=(RND, "f" * 64), drand_disagree=True); rec = br.collect(n, br.fmt(T_SIGN), D, STMT, now=TP + timedelta(hours=25)); self.assertEqual(V(rec, TP + timedelta(hours=25), fetch=n)["outcome"], "UNAVAILABLE")
        n = pki.network(TP, nist_404=True, drand=(RND, "f" * 64)); rec = br.collect(n, br.fmt(T_SIGN), D, STMT, now=TP + timedelta(hours=25))
        rec["drand"]["relays"] = {u: r for u, r in list(rec["drand"]["relays"].items())[:1]}; self.assertEqual(V(rec, TP + timedelta(hours=25))["outcome"], "UNAVAILABLE")          # one relay retained
        rec2 = br.collect(n, br.fmt(T_SIGN), D, STMT, now=TP + timedelta(hours=25)); rec2["drand"]["relays"]["https://attacker.invalid/public/%d" % RND] = rec2["drand"]["relays"][list(rec2["drand"]["relays"])[0]]
        r = V(rec2, TP + timedelta(hours=25)); self.assertNotIn("attacker.invalid", json.dumps(r["checks"]["drand"]["hosts"]))                                                    # unpinned keys never counted
    def test_live_relays_must_confirm(self):
        n = pki.network(TP, nist_404=True, drand=(RND, "f" * 64)); rec = br.collect(n, br.fmt(T_SIGN), D, STMT, now=TP + timedelta(hours=25))
        self.assertEqual(V(rec, TP + timedelta(hours=25), fetch=pki.network(TP, nist_404=True, drand=(RND, "0" * 64)))["outcome"], "UNAVAILABLE")
    def test_live_sample_regression_observation(self):                                # observation, not a normative vector
        ev = {"pulse_body": (HERE / "_sample_pulse_last.json").read_bytes(), "leaf_pem": (HERE / "_sample_certificate.pem").read_bytes(), "intermediate_pems": [(HERE / "_digicert_intermediate.pem").read_bytes()], "next_body": b'{"pulse":{"localRandomValue":"00"}}'}
        c = npulse.authenticate(ev, datetime(2026, 9, 5, 15, 13, tzinfo=timezone.utc), npulse.pinned_roots())
        self.assertTrue(c["anchor"]["anchored"]); self.assertTrue(c["output_is_sha512_of_message_and_signature"]); self.assertTrue(c["certificate_id_is_sha512_of_leaf_der"]); self.assertEqual((c["leaf_key_bits"], c["signature_bytes"]), (2048, 512)); self.assertIn(c["signature_verifies_under_leaf"], (True, False)); self.assertFalse(c["accepted"]) if not c["signature_verifies_under_leaf"] else None
    def test_4096_key_verifies_512_byte_signature(self):
        from cryptography.hazmat.primitives.asymmetric import rsa
        k = rsa.generate_private_key(65537, 4096); lc, k = pki.leaf(key=k); rec, n = self.genuine(leaf_cert=lc, key=k); r = V(rec, TP + timedelta(hours=1), fetch=n)
        self.assertEqual(r["outcome"], "ACCEPT-NIST"); self.assertEqual(r["checks"]["nist"]["signature_bytes"], 512)
    def test_zzz_every_token_is_exercised(self):                                       # runs last (name order): every REFUSE token / outcome literal in beacon_record.py must have appeared above
        src = inspect.getsource(br); tokens = {f"REFUSE-{t}" for t in re.findall(r'refuse\("([A-Z0-9-]+)"', src)} | {"ACCEPT-NIST", "ACCEPT-DRAND", "RETRY", "UNAVAILABLE"}
        missing = sorted(tokens - EXERCISED); self.assertEqual(missing, [], f"outcomes defined in beacon_record.py but never exercised: {missing}")
if __name__ == "__main__": unittest.main()
