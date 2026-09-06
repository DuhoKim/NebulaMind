"""Fixture for beacon_record_expedited (option A V16 draft). Same three-tier test PKI and mocked network as test_beacon_v2; every
accepted record is produced by collect. Asserts (1) the module differs from the pinned beacon_record.py ONLY in the disclosed lines;
(2) on identical inputs the pinned module says RETRY where the expedited one says ACCEPT-DRAND (fails on the old behaviour);
(3) NIST stays binding and VOIDs drand when authenticable; (4) the old T_sign and the public 00:15Z pulse are refused by name;
(5) every REFUSE token the expedited source can emit is exercised."""
import json, unittest, re, difflib, inspect
from datetime import datetime, timezone, timedelta
from pathlib import Path
import sys; HERE = Path(__file__).resolve().parent; sys.path.insert(0, str(HERE))
import drand_round, beacon_record as V15, beacon_record_expedited as X, test_pki as pki
T_SIGN = datetime(2026, 9, 6, 3, 0, 7, tzinfo=timezone.utc); TP = X.pulse_time(T_SIGN); D = "b" * 64
STMT = f"V16 signed: {D} at {X.fmt(T_SIGN)}".encode(); RND = drand_round.round_for(TP); SOON = TP + timedelta(minutes=1)
EXERCISED = set()
def V(mod, rec, now, fetch=None):
    r = mod.verdict(rec, now, pki.roots(), fetch=fetch, rule_sha256=D, statement_bytes=STMT)
    if mod is X: EXERCISED.add(r["outcome"])
    return r
class T(unittest.TestCase):
    REMOVED_FROM_PINNED = ['"""THE ONE VERDICT (rebuilt once, 2026-09-06). A beacon record holds INPUTS (T_sign, rule digest, the retained signature statement) and', 'Rule: T_pulse = first whole minute >= T_sign + 600 s. NIST is binding whenever its pulse authenticates. Before T_pulse + 24 h: an', 'unauthenticated or unretrievable primary is RETRY. From T_pulse + 24 h: drand round_for(T_pulse) is used ONLY if the primary is still not', 'authenticable at the time of the verdict (recomputed, not recorded) AND >= 2 pinned hosts agree. VOID: if NIST later serves an', 'DELAY_S = 600; FALLBACK_AFTER_H = 24', '    ev = _nist_evidence(rec); nist_ok = False', '                out["checks"]["nist_live_equal"] = same', '            except urllib.error.HTTPError as e: out["checks"]["nist_live_http"] = e.code', '            except Exception as e: out["checks"]["nist_live_error"] = repr(e)[:120]', '        nist_ok = c["accepted"]', '    if now < t_pulse + timedelta(hours=FALLBACK_AFTER_H): out.update(outcome="RETRY", seed_hex=None, source=None, why="primary not authenticable/retrievable yet; fallback not permitted before T_pulse + 24 h"); return out', '    # at/after 24 h: primary still not authenticable NOW — if fetch is given, re-check live (a live authenticable primary is binding -> RETRY... i.e. ACCEPT-NIST path above would have fired if evidence were live-equal; so re-collect and authenticate)', '        except urllib.error.HTTPError as e: out["checks"]["nist_live_now_http"] = e.code', '        except Exception as e: out["checks"]["nist_live_now_error"] = repr(e)[:120]']
    def test_differs_from_pinned_only_in_disclosed_lines(self):
        """The disclosed diff, frozen: exactly these lines of the pinned module are removed, and every added line belongs to one of the
        disclosed changes (fallback constant, order-visibility refusals, clock-first RETRY, live-equality requirement, docstring)."""
        a = (HERE / "beacon_record.py").read_text().splitlines(); b = (HERE / "beacon_record_expedited.py").read_text().splitlines()
        ch = [l for l in difflib.unified_diff(a, b, n=0, lineterm="") if l[:1] in "+-" and l[:3] not in ("+++", "---")]
        self.assertEqual([l[1:] for l in ch if l[0] == "-"], self.REMOVED_FROM_PINNED)
        allowed = ("FALLBACK_AFTER_H", "MIN_T_SIGN", "EXCLUDED_T_PULSE", "T-SIGN-PREDATES-AMENDMENT", "T-PULSE-EXCLUDED", "THE ONE VERDICT", "IDENTICAL to beacon_record.py", "ORIGINAL TEXT OF THE PINNED", "Rule (V17)", "RETRY", "live_ok", "nist_live", "never a seed", "V17", "NIST is binding", "authenticable at the time of the verdict", "from T_pulse itself", "ev = _nist_evidence(rec)", "T_pulse + 24 h); MIN_T_SIGN", "EXCLUDED_T_PULSE (the", "except Exception as e:", "except urllib.error.HTTPError as e:", "out[\"checks\"]")
        for l in ch:
            if l[0] == "+": self.assertTrue(any(k in l for k in allowed), l)
        self.assertTrue(20 <= len(ch) <= 50, len(ch))
    def test_pulse_time_formula_unchanged(self):
        self.assertEqual(X.pulse_time(T_SIGN), V15.pulse_time(T_SIGN)); self.assertEqual(X.fmt(TP), "2026-09-06T03:11:00Z"); self.assertEqual(X.DELAY_S, 600)
    def test_same_inputs__pinned_RETRY__expedited_ACCEPT_DRAND(self):
        n = pki.network(TP, sign=False, drand=(RND, "c" * 64))            # NIST served but not verifying (the observed limit); relays agree
        rec = X.collect(n, X.fmt(T_SIGN), D, STMT, now=SOON)
        self.assertEqual(rec["drand"]["round"], RND); self.assertEqual(len(rec["drand"]["relays"]), 4)
        r = V(X, rec, SOON, fetch=n); self.assertEqual(r["outcome"], "ACCEPT-DRAND"); self.assertEqual(r["seed_hex"], "c" * 64); self.assertEqual(r["round"], RND)
        self.assertEqual(V(V15, rec, SOON, fetch=n)["outcome"], "RETRY")  # the V15 rule on the very same record and clock
        old = V15.collect(n, V15.fmt(T_SIGN), D, STMT, now=SOON); self.assertEqual(old["drand"], {})  # V15 would not even collect drand yet
    def test_nist_authenticable_is_binding_and_voids_drand(self):
        n = pki.network(TP, drand=(RND, "c" * 64)); rec = X.collect(n, X.fmt(T_SIGN), D, STMT, now=SOON)
        self.assertEqual(V(X, rec, SOON, fetch=n)["outcome"], "ACCEPT-NIST")
        n2 = pki.network(TP, nist_404=True, drand=(RND, "c" * 64)); rec2 = X.collect(n2, X.fmt(T_SIGN), D, STMT, now=SOON)   # NIST absent at collection
        self.assertEqual(V(X, rec2, SOON, fetch=pki.network(TP, drand=(RND, "c" * 64)))["outcome"], "REFUSE-DRAND-VOID-PRIMARY-AUTHENTICABLE")  # authenticable at build time → binding
        n3 = pki.network(TP, sign=False, drand=(RND, "c" * 64)); rec3 = X.collect(n3, X.fmt(T_SIGN), D, STMT, now=SOON)          # NIST retained unsigned, live signed
        self.assertEqual(V(X, rec3, SOON, fetch=pki.network(TP, drand=(RND, "c" * 64)))["outcome"], "REFUSE-NIST-LIVE-DIFFERS")
    def test_unavailable_when_relays_disagree_or_too_few(self):
        n = pki.network(TP, sign=False, drand=(RND, "c" * 64), drand_disagree=True); rec = X.collect(n, X.fmt(T_SIGN), D, STMT, now=SOON)
        self.assertEqual(V(X, rec, SOON)["outcome"], "UNAVAILABLE")
        n = pki.network(TP, sign=False, drand=(RND, "c" * 64)); rec = X.collect(n, X.fmt(T_SIGN), D, STMT, now=SOON)
        rec["drand"]["relays"] = dict(list(rec["drand"]["relays"].items())[:1]); self.assertEqual(V(X, rec, SOON)["outcome"], "UNAVAILABLE")
    def test_retry_only_before_t_pulse_clock(self):
        n = pki.network(TP, sign=False, drand=(RND, "c" * 64)); rec = X.collect(n, X.fmt(T_SIGN), D, STMT, now=SOON)
        self.assertEqual(V(X, rec, TP - timedelta(seconds=1))["outcome"], "RETRY")   # a verdict asked before T_pulse (clock skew) is RETRY, never a seed
    def test_old_t_sign_and_public_pulse_refused_by_name(self):
        n = pki.network(TP, sign=False, drand=(RND, "c" * 64))
        with self.assertRaises(SystemExit) as cm: X.collect(n, "2026-09-06T00:04:07Z", D, f"x {D} 2026-09-06T00:04:07Z".encode(), now=SOON)
        self.assertIn("T-SIGN-PREDATES-AMENDMENT", str(cm.exception))
        self.assertIn("2026-09-06T00:15:00Z", X.EXCLUDED_T_PULSE); self.assertEqual(drand_round.round_for(X.parse_utc("2026-09-06T00:15:00Z")), 6440756)
        rec = X.collect(n, X.fmt(T_SIGN), D, STMT, now=SOON)
        bad = dict(rec); bad["T_sign"] = "2026-09-06T00:04:07Z"; bad["T_pulse"] = "2026-09-06T00:15:00Z"
        self.assertEqual(X.verdict(bad, SOON, pki.roots())["outcome"], "REFUSE-T-SIGN-PREDATES-AMENDMENT")
        old_X_min = X.MIN_T_SIGN
        try:
            X.MIN_T_SIGN = "2026-09-05T00:00:00Z"                                     # isolate the exclusion check
            self.assertEqual(X.verdict(bad, SOON, pki.roots())["outcome"], "REFUSE-T-PULSE-EXCLUDED"); EXERCISED.add("REFUSE-T-PULSE-EXCLUDED")
        finally: X.MIN_T_SIGN = old_X_min
        EXERCISED.add("REFUSE-T-SIGN-PREDATES-AMENDMENT")
    def test_codex_counterexamples__live_fetch_raises_is_RETRY_not_ACCEPT(self):
        n = pki.network(TP, drand=(RND, "c" * 64)); rec = X.collect(n, X.fmt(T_SIGN), D, STMT, now=SOON)   # retained NIST AUTHENTICATES
        def boom(url, timeout=30): raise OSError("network down")
        r = V(X, rec, SOON, fetch=boom); self.assertEqual(r["outcome"], "RETRY"); self.assertIn("nist_live_error", r["checks"])
        self.assertEqual(V15.verdict(rec, SOON, pki.roots(), fetch=boom, rule_sha256=D, statement_bytes=STMT)["outcome"], "ACCEPT-NIST")   # the V15/V16 defect, on record
        n2 = pki.network(TP, sign=False, drand=(RND, "c" * 64)); rec2 = X.collect(n2, X.fmt(T_SIGN), D, STMT, now=SOON)                     # retained NIST does NOT authenticate
        self.assertEqual(V(X, rec2, SOON, fetch=boom)["outcome"], "RETRY")                                                                    # a local failure is not a public NIST failure → no fallback
    def test_codex_counterexample__before_t_pulse_is_RETRY_even_if_nist_authenticates(self):
        n = pki.network(TP, drand=(RND, "c" * 64)); rec = X.collect(n, X.fmt(T_SIGN), D, STMT, now=SOON)
        self.assertEqual(V(X, rec, TP - timedelta(seconds=1), fetch=n)["outcome"], "RETRY")
        self.assertEqual(V15.verdict(rec, TP - timedelta(seconds=1), pki.roots(), fetch=n, rule_sha256=D, statement_bytes=STMT)["outcome"], "ACCEPT-NIST")   # the V15/V16 defect
    def test_accept_nist_requires_live_equality_when_fetch_given(self):
        n = pki.network(TP, drand=(RND, "c" * 64)); rec = X.collect(n, X.fmt(T_SIGN), D, STMT, now=SOON)
        r = V(X, rec, SOON, fetch=n); self.assertEqual(r["outcome"], "ACCEPT-NIST"); self.assertTrue(r["checks"]["nist_live_equal"])
        self.assertEqual(V(X, rec, SOON)["outcome"], "ACCEPT-NIST")   # without fetch: retained authentication only (the builder ALWAYS passes fetch)
    def test_collector_exclusion_exception_exercised(self):
        old = X.MIN_T_SIGN
        try:
            X.MIN_T_SIGN = "2026-09-05T00:00:00Z"; ts = "2026-09-06T00:04:07Z"; tp = X.pulse_time(X.parse_utc(ts))
            with self.assertRaises(SystemExit) as cm: X.collect(pki.network(tp, sign=False, drand=(drand_round.round_for(tp), "c" * 64)), ts, D, f"x {D} {ts}".encode(), now=tp + timedelta(minutes=1))
            self.assertIn("T-PULSE-EXCLUDED", str(cm.exception))
        finally: X.MIN_T_SIGN = old
    def test_record_holds_bytes_only(self):
        n = pki.network(TP, sign=False, drand=(RND, "c" * 64)); rec = X.collect(n, X.fmt(T_SIGN), D, STMT, now=SOON); flat = json.dumps(rec)
        for banned in ("accepted", "verified", "outcome", "seed_hex", "anchored", "true", "false"): self.assertNotIn(f'"{banned}"', flat)
    def test_other_refuse_tokens(self):
        n = pki.network(TP, sign=False, drand=(RND, "c" * 64)); rec = X.collect(n, X.fmt(T_SIGN), D, STMT, now=SOON)
        b = dict(rec); b["schema"] = "X"; self.assertEqual(V(X, b, SOON)["outcome"], "REFUSE-SCHEMA")
        b = dict(rec); b["T_sign"] = "garbage"; self.assertEqual(V(X, b, SOON)["outcome"], "REFUSE-T-SIGN")
        b = dict(rec); b["T_pulse"] = "2026-09-06T03:12:00Z"; self.assertEqual(V(X, b, SOON)["outcome"], "REFUSE-T-PULSE")
        b = dict(rec); b["rule_sha256"] = "d" * 64; self.assertEqual(V(X, b, SOON)["outcome"], "REFUSE-RULE-DIGEST")
        self.assertEqual(X.verdict(rec, SOON, pki.roots(), rule_sha256=D, statement_bytes=b"other")["outcome"], "REFUSE-STATEMENT-BYTES"); EXERCISED.add("REFUSE-STATEMENT-BYTES")
        b = dict(rec); b["statement_b64"] = X.b64(b"unbound"); self.assertEqual(X.verdict(b, SOON, pki.roots())["outcome"], "REFUSE-STATEMENT-BINDING"); EXERCISED.add("REFUSE-STATEMENT-BINDING")
        n_diff = pki.network(TP, sign=False, drand=(RND, "c" * 64), tamper_output=True) if "tamper_output" in inspect.signature(pki.network).parameters else None
        if n_diff is not None: self.assertEqual(V(X, rec, SOON, fetch=n_diff)["outcome"], "REFUSE-NIST-LIVE-DIFFERS")
    def test_zzz_every_token_is_exercised(self):
        src = (HERE / "beacon_record_expedited.py").read_text(); toks = {"REFUSE-" + t for t in re.findall(r'refuse\("([A-Z0-9-]+)"', src)} | {"ACCEPT-NIST", "ACCEPT-DRAND", "RETRY", "UNAVAILABLE"}
        missing = toks - EXERCISED
        self.assertFalse(missing, missing)
if __name__ == "__main__": unittest.main()
