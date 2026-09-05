import unittest, json, tempfile
from datetime import datetime, timezone, timedelta
from unittest import mock
import sys; from pathlib import Path; sys.path.insert(0, str(Path(__file__).resolve().parent))
import fetch_beacon as fb
import test_support as ts
ts.install_test_root()
class T(unittest.TestCase):
    def run_main(self, source):
        d=Path(tempfile.mkdtemp()); out=d/'record.json'; stmt=d/'statement.txt'; D='a'*64
        t_sign=(datetime.now(timezone.utc)-timedelta(hours=30 if source=='drand' else 2)).replace(microsecond=0).strftime('%Y-%m-%dT%H:%M:%SZ'); tp=fb.pulse_time(fb.parse_utc(t_sign)); stmt.write_text(f'signed {D} at {t_sign}')
        uri='https://beacon.nist.gov/beacon/2.0/chain/2/pulse/123'
        if source=='nist': body,pem=ts.make_nist(tp,uri); side=ts.nist_side(body,pem,tp=tp)
        else:
            rnd=fb.drand_round(tp); side=ts.drand_side(rnd)
        with mock.patch.object(fb,'fetch',side_effect=side): self.assertEqual(fb.main(['--t-sign',t_sign,'--out',str(out),'--rule-sha256',D,'--signature-statement',str(stmt)]),0)
        return json.loads(out.read_text())
    def test_main_writes_complete_nist_record(self):
        r=self.run_main('nist'); self.assertEqual(r['source'],'NIST-beacon-2.0')
        for k in ('rule','rule_sha256','signature_statement_sha256','source','uri','T_sign','T_pulse','pulse','seed_hex','fetched_utc','body_sha256','certificate_pem','certificate_pem_sha256','pulse_verification'): self.assertIn(k,r)
        self.assertTrue(r['pulse_verification']['output_is_sha512_of_message_plus_signature']); self.assertTrue(r['pulse_verification']['certificate_id_matches_sha512_of_der'])
    def test_structural_failure_is_retry_not_seed(self):    # a pulse whose output does not bind its content is rejected (RETRY), never a seed
        d=Path(tempfile.mkdtemp()); out=d/'r.json'; stmt=d/'s.txt'; D='a'*64
        t_sign=(datetime.now(timezone.utc)-timedelta(hours=2)).replace(microsecond=0).strftime('%Y-%m-%dT%H:%M:%SZ'); tp=fb.pulse_time(fb.parse_utc(t_sign)); stmt.write_text(f'signed {D} at {t_sign}')
        body,pem=ts.make_nist(tp); bad=json.loads(body); bad['pulse']['outputValue']='0'*128; side=ts.nist_side(json.dumps(bad).encode(),pem,tp=tp)
        with mock.patch.object(fb,'fetch',side_effect=side): self.assertEqual(fb.main(['--t-sign',t_sign,'--out',str(out),'--rule-sha256',D,'--signature-statement',str(stmt)]),4)
        r=json.loads(out.read_text()); self.assertNotIn('seed_hex',r); self.assertIn('not authenticated', r['primary_rejected']['reason']); self.assertFalse(r['primary_rejected']['checks']['output_is_sha512_of_message_plus_signature'])
    def test_main_writes_complete_drand_record(self):
        r=self.run_main('drand'); self.assertEqual(r['source'],'drand-mainnet-default'); self.assertEqual(r['round'],r['pulse']['round'])
        for k in ('rule','rule_sha256','signature_statement_sha256','chain_hash','fallback_condition','primary_error','relay_responses','relays_agreeing','body','body_sha256'): self.assertIn(k,r)
        self.assertGreaterEqual(len({__import__('urllib').parse.urlparse(u).netloc for u in r['relays_agreeing']}), fb.MIN_RELAY_AGREEMENT)
    def test_pulse_time_rule(self):                         # T_pulse = first whole minute >= T_sign + 600 s
        self.assertEqual(fb.pulse_time(fb.parse_utc("2026-09-06T01:00:00Z")).strftime("%H:%M:%S"), "01:10:00")
        self.assertEqual(fb.pulse_time(fb.parse_utc("2026-09-06T01:00:01Z")).strftime("%H:%M:%S"), "01:11:00")
        self.assertEqual(fb.pulse_time(fb.parse_utc("2026-09-06T01:00:59Z")).strftime("%H:%M:%S"), "01:11:00")
    def test_drand_round_rule(self):                        # round = floor((t - genesis)/period) + 1, checked against a known live pair
        t = datetime.fromtimestamp(1595431050 + 30 * 100, tz=timezone.utc); self.assertEqual(fb.drand_round(t), 101)
    def test_accept_nist_exact_timestamp_and_host(self):
        t = fb.parse_utc("2026-09-05T14:15:00Z"); good = json.dumps({"pulse": {"uri": "https://beacon.nist.gov/beacon/2.0/chain/2/pulse/1928201", "timeStamp": "2026-09-05T14:15:00.000Z", "outputValue": "D" * 128, "chainIndex": "2", "statusCode": 0}})
        self.assertTrue(fb.accept_nist(good, t)[0])
        late = good.replace("14:15:00.000Z", "14:16:00.000Z"); self.assertFalse(fb.accept_nist(late, t)[0])          # wrong minute -> rejected
        fake = good.replace("https://beacon.nist.gov/", "https://example.org/"); self.assertFalse(fb.accept_nist(fake, t)[0])
        self.assertFalse(fb.accept_nist(good.replace('"chainIndex": "2"', '"chainIndex": "1"'), t)[0]); self.assertFalse(fb.accept_nist(good.replace('"statusCode": 0', '"statusCode": 1'), t)[0]); self.assertFalse(fb.accept_nist(good.replace("D" * 128, "Z" * 128), t)[0])
    def test_accept_drand_round_must_match(self):
        self.assertTrue(fb.accept_drand(json.dumps({"round": 5, "randomness": "a" * 64}), 5)[0]); self.assertFalse(fb.accept_drand(json.dumps({"round": 6, "randomness": "a" * 64}), 5)[0])
    def test_no_seed_before_pulse_time(self):               # signature first, beacon second: running before T_pulse yields no seed (exit 3)
        import tempfile, os; out = os.path.join(tempfile.mkdtemp(), "b.json")
        st = out + ".stmt"; Path(st).write_text("V9 signed: " + "a" * 64 + " at 2099-01-01T00:00:00Z")
        self.assertEqual(fb.main(["--t-sign", "2099-01-01T00:00:00Z", "--out", out, "--rule-sha256", "a" * 64, "--signature-statement", st]), 3)
        Path(st).write_text("unrelated"); self.assertEqual(fb.main(["--t-sign", "2099-01-01T00:00:00Z", "--out", out, "--rule-sha256", "a" * 64, "--signature-statement", st]), 2)   # statement must bind digest + T_sign
    def test_fallback_not_before_24h(self):                 # agy V8: no immediate fallback; a blocked primary yields RETRY, not a second seed
        import tempfile, os; from unittest import mock
        out = os.path.join(tempfile.mkdtemp(), "b.json")
        t_sign = (datetime.now(timezone.utc) - __import__("datetime").timedelta(hours=1)).strftime("%Y-%m-%dT%H:%M:%SZ")   # T_pulse ~50 min ago
        st = out + ".stmt"; Path(st).write_text("signed " + "a" * 64 + " at " + t_sign)
        with mock.patch.object(fb, "fetch", side_effect=OSError("blocked")):
            self.assertEqual(fb.main(["--t-sign", t_sign, "--out", out, "--rule-sha256", "a" * 64, "--signature-statement", st]), 4)                                                  # RETRY, no fallback
            rec = json.loads(Path(out).read_text()); self.assertNotIn("seed_hex", rec); self.assertTrue(rec["verdict"].startswith("BEACON-RETRY"))
    def test_fallback_after_24h_only_when_primary_absent(self):
        import tempfile, os; from unittest import mock
        out = os.path.join(tempfile.mkdtemp(), "b.json")
        t_sign = (datetime.now(timezone.utc) - __import__("datetime").timedelta(hours=30)).strftime("%Y-%m-%dT%H:%M:%SZ")
        rnd = fb.drand_round(fb.pulse_time(fb.parse_utc(t_sign)))
        fake_fetch = ts.drand_side(rnd, randomness="b" * 64)                                                        # NIST 404 = absence; relays agree
        st = out + ".stmt"; Path(st).write_text("signed " + "a" * 64 + " at " + t_sign)
        with mock.patch.object(fb, "fetch", side_effect=fake_fetch):
            self.assertEqual(fb.main(["--t-sign", t_sign, "--out", out, "--rule-sha256", "a" * 64, "--signature-statement", st]), 0); rec = json.loads(Path(out).read_text()); self.assertEqual(rec["source"], "drand-mainnet-default")
    def test_after_24h_network_error_is_not_absence(self):    # codex V9: after 24 h an ordinary failure must still be RETRY, not fallback
        import tempfile, os; from unittest import mock
        out = os.path.join(tempfile.mkdtemp(), "b.json"); t_sign = (datetime.now(timezone.utc) - __import__("datetime").timedelta(hours=30)).strftime("%Y-%m-%dT%H:%M:%SZ")
        st = out + ".stmt"; Path(st).write_text("signed " + "a" * 64 + " at " + t_sign)
        with mock.patch.object(fb, "fetch", side_effect=OSError("network down")):
            self.assertEqual(fb.main(["--t-sign", t_sign, "--out", out, "--rule-sha256", "a" * 64, "--signature-statement", st]), 4)
    def test_unsigned_pulse_is_retry_not_seed(self):        # codex V11: a pulse whose RSA signature does not verify is never accepted
        d=Path(tempfile.mkdtemp()); out=d/'r.json'; stmt=d/'s.txt'; D='a'*64
        t_sign=(datetime.now(timezone.utc)-timedelta(hours=2)).replace(microsecond=0).strftime('%Y-%m-%dT%H:%M:%SZ'); tp=fb.pulse_time(fb.parse_utc(t_sign)); stmt.write_text(f'signed {D} at {t_sign}')
        body,pem=ts.make_nist(tp, sign=False); side=ts.nist_side(body,pem,tp=tp)
        with mock.patch.object(fb,'fetch',side_effect=side): self.assertEqual(fb.main(['--t-sign',t_sign,'--out',str(out),'--rule-sha256',D,'--signature-statement',str(stmt)]),4)
        r=json.loads(out.read_text()); self.assertNotIn('seed_hex',r); self.assertFalse(r['primary_rejected']['checks']['signature_pkcs1v15_sha512']); self.assertTrue(r['primary_rejected']['checks']['output_is_sha512_of_message_plus_signature'])
    def test_unverifiable_primary_after_24h_falls_back_to_agreeing_relays(self):
        d=Path(tempfile.mkdtemp()); out=d/'r.json'; stmt=d/'s.txt'; D='a'*64
        t_sign=(datetime.now(timezone.utc)-timedelta(hours=30)).replace(microsecond=0).strftime('%Y-%m-%dT%H:%M:%SZ'); tp=fb.pulse_time(fb.parse_utc(t_sign)); stmt.write_text(f'signed {D} at {t_sign}'); rnd=fb.drand_round(tp)
        body,pem=ts.make_nist(tp, sign=False); nist=ts.nist_side(body,pem,tp=tp); dr=ts.drand_side(rnd)
        def side(url,timeout=30): return nist(url) if 'nist.gov' in url else dr(url)
        with mock.patch.object(fb,'fetch',side_effect=side): self.assertEqual(fb.main(['--t-sign',t_sign,'--out',str(out),'--rule-sha256',D,'--signature-statement',str(stmt)]),0)
        r=json.loads(out.read_text()); self.assertEqual(r['source'],'drand-mainnet-default'); self.assertIn('not authenticable', r['fallback_condition'])
    def test_relay_disagreement_yields_no_seed(self):
        d=Path(tempfile.mkdtemp()); out=d/'r.json'; stmt=d/'s.txt'; D='a'*64
        t_sign=(datetime.now(timezone.utc)-timedelta(hours=30)).replace(microsecond=0).strftime('%Y-%m-%dT%H:%M:%SZ'); tp=fb.pulse_time(fb.parse_utc(t_sign)); stmt.write_text(f'signed {D} at {t_sign}'); rnd=fb.drand_round(tp)
        import urllib.error, urllib.parse, hashlib as _h
        def side(url,timeout=30):                                                                                  # EVERY relay returns a different randomness: no value has >= 2 hosts
            if 'nist.gov' in url: raise urllib.error.HTTPError(url,404,'Not Found',None,None)
            return json.dumps({'round':rnd,'randomness':_h.sha256(urllib.parse.urlparse(url).netloc.encode()).hexdigest()}).encode()
        with mock.patch.object(fb,'fetch',side_effect=side): self.assertEqual(fb.main(['--t-sign',t_sign,'--out',str(out),'--rule-sha256',D,'--signature-statement',str(stmt)]),2)
        r=json.loads(out.read_text()); self.assertNotIn('seed_hex',r); self.assertEqual(r['verdict'],'BEACON-UNAVAILABLE')
    def test_self_signed_certificate_is_not_anchored(self):   # agy V12: a certificate not chaining to the pinned root must be refused even if the pulse verifies under it
        d=Path(tempfile.mkdtemp()); out=d/'r.json'; stmt=d/'s.txt'; D='a'*64
        t_sign=(datetime.now(timezone.utc)-timedelta(hours=2)).replace(microsecond=0).strftime('%Y-%m-%dT%H:%M:%SZ'); tp=fb.pulse_time(fb.parse_utc(t_sign)); stmt.write_text(f'signed {D} at {t_sign}')
        cert=ts.test_certificate(signed_by_root=False); body,pem=ts.make_nist(tp, cert=cert); side=ts.nist_side(body,pem,tp=tp)
        with mock.patch.object(fb,'fetch',side_effect=side): self.assertEqual(fb.main(['--t-sign',t_sign,'--out',str(out),'--rule-sha256',D,'--signature-statement',str(stmt)]),4)
        r=json.loads(out.read_text()); self.assertNotIn('seed_hex',r); self.assertFalse(r['primary_rejected']['checks']['anchor']['chains_to_pinned_root']); self.assertTrue(r['primary_rejected']['checks']['signature_pkcs1v15_sha512'])
    def test_wrong_hostname_is_not_anchored(self):
        d=Path(tempfile.mkdtemp()); out=d/'r.json'; stmt=d/'s.txt'; D='a'*64
        t_sign=(datetime.now(timezone.utc)-timedelta(hours=2)).replace(microsecond=0).strftime('%Y-%m-%dT%H:%M:%SZ'); tp=fb.pulse_time(fb.parse_utc(t_sign)); stmt.write_text(f'signed {D} at {t_sign}')
        cert=ts.test_certificate(san="example.org"); body,pem=ts.make_nist(tp, cert=cert); side=ts.nist_side(body,pem,tp=tp)
        with mock.patch.object(fb,'fetch',side_effect=side): self.assertEqual(fb.main(['--t-sign',t_sign,'--out',str(out),'--rule-sha256',D,'--signature-statement',str(stmt)]),4)
        self.assertFalse(json.loads(out.read_text())['primary_rejected']['checks']['anchor']['san_matches'])
if __name__ == "__main__": unittest.main()
