"""TRACK 14 v3 — seat B's V33 counter-cases, conforming to the FAIL-FIRST KIT (scripts/failfirst_kit.py; Blanc 08:51 KST): ONE outcome assertion per method, and
every method labelled in its docstring's first line as FAIL-FIRST (it must be observed FAILING against the predecessor V33 bytes) or POSITIVE-REGRESSION (observed
passing there, kept so the repair cannot lose it). The kit refused v2 on both rules — that refusal is the evidence the rules needed to be mechanical.
Predecessors retained unchanged: v1 `test_track14_fail_first.py` (86133b80…; log a1a7fae4… 7/6F/1P) and v2 `test_track14_fail_first_v2.py` (4cc88841…; log 84f4f388… 10/7F/3P).
v2's five fixture corrections (coordinating Codex 08:49) are carried over: digest-coherent 1a, pinned publication identity for 1c, authentic history in 3, the devnull
context manager, and 1b2 labelled a positive regression. HONEST SCOPE: 1b3 (the reviewer's coherent differing same-id case) PASSED on V33 too, so it is labelled a
POSITIVE-REGRESSION — seat B's hidden same-id finding is NOT independently reproduced here, and no reproduction credit is claimed for it."""
import base64, json, os, sys, unittest
from pathlib import Path
from unittest import mock
HERE = Path(__file__).resolve().parent; D = HERE.parent
for p in ("beacon_v2", "drand_only", "corpus_identity", "fourier_chirality", "track2", "track13", "track14"): sys.path.insert(0, str(D / p))
import provenance_designs_v13 as P, precedence_core as PC
import run_configurations_v17 as rc, test_run_configurations_v17 as TF, history_v2 as H
from test_track13_regressions import H13, feed, codes, whys, canon, REF, REPO
def by_check(out):
    b = {}
    for f in (out or {}).get("findings", []): b.setdefault(f["check"], set()).add(f["code"])
    return b
def cls_of(out, code): return {f["class"] for f in (out or {}).get("findings", []) if f["code"] == code}
class T14v3(unittest.TestCase):
    @classmethod
    def setUpClass(cls): cls.t = TF.T("test_composed_mode_on_the_production_call_path"); cls.t.setUp(); cls.h = H13(cls.t)
    @classmethod
    def tearDownClass(cls): cls.t.tearDown()
    def precondition(self, cond, msg):
        """fixture validation, NOT an outcome claim (the kit does not count it): a false precondition means the fixture is wrong, not the code"""
        if not cond: raise AssertionError("FIXTURE PRECONDITION FAILED: " + msg)
    def _witness_down(self): return mock.patch.object(rc, "verify_witness", side_effect=rc.DataIntegrityFail("WITNESS-FETCH-FAILED fixture transport unavailable"))
    # ---- scenarios (helpers: assertions here are not outcome claims)
    def s_times(self):
        env = self.h.build(mutate_ev=lambda ev, evs: ev.update({"created_at": "also-not-a-time"}), mutate_I=lambda I: I.update({"T_pulse": "not-a-time"}))
        msg, out = self.h.refusal(env, feed(env["live"]), ctx=self._witness_down())
        self.precondition("EVENT-DIGEST" not in codes(out), f"the fixture must stay digest-coherent so the two timestamp inputs are isolated: {sorted(codes(out))}")
        return out
    def s_delivery_fault(self, same_id=False, coherent_other=False):
        env = self.h.build(mutate_ev=(lambda ev, evs: ev["payload"].update({"commits": [None], "before": "0" * 40})) if coherent_other else (lambda ev, evs: ev["payload"].update({"commits": [None]})))
        live = env["live"]
        if same_id: live = [{**env["genuine"], "payload": {**env["genuine"]["payload"], "before": "0" * 40}}] + env["live"]
        if coherent_other:
            other = json.loads(json.dumps(env["genuine"])); other["payload"]["commits"] = [{"sha": other["payload"]["head"]}]; other["created_at"] = "2026-09-06T09:41:00Z"; live = [other] + env["live"][1:]
        msg, out = self.h.refusal(env, feed(live), ctx=self._witness_down()); return out
    def s_unreadable_blob(self):
        env = self.h.build(rebuild_after=True); target = env["evs"][1]["payload"]["head"]; real = P._blob_at            # PINNED publication identity, not the Nth call
        def flaky(root, commit, rel):
            if commit == target: raise OSError("fixture: this blob cannot be read")
            return real(root, commit, rel)
        with mock.patch.object(P, "_blob_at", flaky): msg, out = self.h.refusal(env, feed(env["live"]), ctx=self._witness_down())
        self.precondition(target in " ".join(e["payload"]["head"] for e in env["evs"]), "the injection must target a published commit")
        return out
    def s_adoption_unreadable(self):
        env = self.h.build()
        with mock.patch.object(rc, "adopted_rule_sha256", side_effect=PermissionError("fixture: adoption file unreadable")): msg, out = self.h.refusal(env, feed(env["live"]))
        return out
    def s_verified_receipt(self):
        """ONLY the approval event is expired; the history stays authentic and every other input is genuine"""
        env = self.h.build(); rp = Path(env["tmp"]) / "receipt.json"; rp.write_text(json.dumps({"fixture": "boundary stub"}))
        approval_id = env["ev"].get("id"); real_auth = P.authenticate_event
        def only_approval_expired(retained, *a, **k):
            if isinstance(retained, dict) and retained.get("id") == approval_id: return "EXPIRED", "fixture: outside the retained window"
            return real_auth(retained, *a, **k)
        TPo = rc.Protocol(**{**env["cTP"].__dict__, "events_receipt": str(rp), "expected_receipt_origin": {"actor": "ops-witness", "session": "OPS"}, "events_runner": feed(env["live"])})
        with mock.patch.object(P, "authenticate_event", only_approval_expired), mock.patch.object(P, "verify_events_receipt", lambda *a, **k: (True, "fixture: receipt verifies")):
            raised = None
            try: rc.load_identity(env["ident"], TPo)
            except rc.DataIntegrityFail as e: raised = str(e)
        return raised, getattr(rc, "LAST_OUTCOME", None)
    # ---- one outcome assertion per method
    def test_1a_created_at_input_contributes(self):
        """POSITIVE-REGRESSION: the malformed created_at is contributed on V33 and must stay contributed"""
        self.assertIn("IDENTITY-WITNESS-TIME", codes(self.s_times()))
    def test_1a_t_pulse_input_also_contributes(self):
        """FAIL-FIRST: T_pulse is an INDEPENDENT input; V33's _time_checks raises on the first parse failure and never parses it"""
        self.assertIn("IDENTITY-T-PULSE", codes(self.s_times()))
    def test_1b_retained_input_failure_is_named_as_retained(self):
        """FAIL-FIRST: a retained-data exception must be a retained-input finding, not MALFORMED-REMOTE-EVIDENCE"""
        self.assertIn("MALFORMED-RETAINED-INPUT", codes(self.s_delivery_fault()))
    def test_1b_retained_input_failure_is_local_terminal(self):
        """FAIL-FIRST: and it must carry the local-terminal class, not a remote retry class"""
        self.assertIn("LOCAL-TERMINAL", cls_of(self.s_delivery_fault(), "MALFORMED-RETAINED-INPUT"))
    def test_1b2_same_id_survives_a_broken_delivery_parse(self):
        """POSITIVE-REGRESSION: already holds on V33; kept so the repair cannot lose it"""
        self.assertIn("EVENT-FORGED", codes(self.s_delivery_fault(same_id=True)))
    def test_1b3_same_id_survives_when_delivery_evaluation_faults(self):
        """POSITIVE-REGRESSION: the reviewer's coherent-differing-event shape ALSO passes on V33 — it is not a reproduction of the hidden finding and claims no credit as one"""
        self.assertIn("EVENT-FORGED", codes(self.s_delivery_fault(coherent_other=True)))
    def test_1c_unreadable_blob_never_fakes_pending_push(self):
        """FAIL-FIRST: _prev is never installed, so working_tree defaults it to empty and claims PENDING-PUSH for 708 already-published bytes"""
        self.assertNotIn("PENDING-PUSH", whys(self.s_unreadable_blob()))
    def test_1c_unreadable_blob_does_not_stop_the_later_relation(self):
        """FAIL-FIRST: the later, independently readable rewrite must still be detected (v1 never reached this assertion — it was bundled)"""
        self.assertIn("HISTORY-NOT-AN-EXTENSION", whys(self.s_unreadable_blob()))
    def test_1c_unreadable_blob_is_itself_accounted_for(self):
        """POSITIVE-REGRESSION: the failed read is already recorded as a finding on V33; it must stay recorded"""
        self.assertTrue(any("cannot be read" in f.get("why", "") for f in self.s_unreadable_blob()["findings"]))
    def test_1d_adoption_identity_is_blocked_by_name(self):
        """FAIL-FIRST: S0h catches only DataIntegrityFail, so a PermissionError leaves adoption-identity neither evaluated, blocked nor represented"""
        out = self.s_adoption_unreadable(); self.assertTrue("adoption-identity" in (out or {}).get("blocked", {}) or "adoption-identity" in by_check(out))
    def test_2_table_verification_catches_a_removed_dynamic_code(self):
        """FAIL-FIRST: EVENT-FORGED is selected through m[o] and is invisible to a regex over add(...) sites, so removing it from the table changes nothing"""
        import unittest as U
        saved = set(rc.INDEPENDENCE["approval-live"]["codes"])
        try:
            rc.INDEPENDENCE["approval-live"]["codes"] = saved - {"EVENT-FORGED"}
            import test_track13_table_vs_code as TV
            with open(os.devnull, "w") as devnull: r = U.TextTestRunner(verbosity=0, stream=devnull).run(U.defaultTestLoader.loadTestsFromModule(TV))
            self.assertFalse(r.wasSuccessful())
        finally: rc.INDEPENDENCE["approval-live"]["codes"] = saved
    def test_3_verified_receipt_does_not_raise(self):
        """FAIL-FIRST: S3a falls through to m['EXPIRED'] and raises KeyError on a receipt that verifies"""
        raised, out = self.s_verified_receipt(); self.assertNotIn("KeyError", whys(out) + (raised or ""))
    def test_3_verified_receipt_is_not_called_malformed_remote_evidence(self):
        """FAIL-FIRST: the KeyError is then filed as MALFORMED-REMOTE-EVIDENCE — a verified receipt reported as malformed remote evidence"""
        raised, out = self.s_verified_receipt(); self.assertNotIn("MALFORMED-REMOTE-EVIDENCE", codes(out))
    def test_3_verified_receipt_lets_the_whole_call_complete(self):
        """FAIL-FIRST: with every other input genuine, the advertised Option-A' substitution must let the whole call complete"""
        raised, out = self.s_verified_receipt(); self.assertIsNone(raised, (raised or "")[:200])
if __name__ == "__main__": unittest.main()
