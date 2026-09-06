"""TRACK 14 v2 — FAIL-FIRST reproduction of seat B's V33 counter-cases, with the coordinating Codex's five fixture corrections (08:49 KST) applied.
v1 (`test_track14_fail_first.py`, sha256 86133b8078d5c431a14995076245910696aba0ec93bdb8569940b7fc3f9f8c90; run 1 log a1a7fae45e2e0e90660a5a9f64cf7608bf72279af4fa6d1de47c9de366c035b0,
7 tests / 6 failures / 1 pass) is RETAINED UNCHANGED as the historical scope. v2 changes only the fixtures, never the promises asserted:
  1a — the mutated created_at is now applied through mutate_ev, BEFORE the witness digest is rebound, so the case isolates the two independent timestamp inputs
       instead of also tripping EVENT-DIGEST (v1's run showed EVENT-DIGEST alongside IDENTITY-WITNESS-TIME).
  1b2 — v1's same-id case ALREADY PASSED on V33 and is kept, explicitly, as a POSITIVE REGRESSION (not fail-first evidence). The reviewer's actual case — an
       approval-delivery parse fault beside a COHERENT DIFFERING same-id event on the live feed — is added separately as 1b3.
  1c — split into two separately evidenced subcases (the false PENDING-PUSH, and the later adjacent relation still being checked), because v1 failed at the first
       assertion and never reached the second; the injection now targets a PINNED PUBLICATION IDENTITY (evs[1]'s head commit) rather than "the second distinct blob
       call", so it survives legitimate call-order changes.
  3 — history stays AUTHENTIC: only the APPROVAL event's authentication is expired (v1 patched authenticate_event globally, expiring the history-open event too),
       and the promised whole-call completion is actually exercised.
  and the devnull stream in the table-mutation control is closed by a context manager (v1 leaked it; the ResourceWarning was real)."""
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
class T14v2(unittest.TestCase):
    @classmethod
    def setUpClass(cls): cls.t = TF.T("test_composed_mode_on_the_production_call_path"); cls.t.setUp(); cls.h = H13(cls.t)
    @classmethod
    def tearDownClass(cls): cls.t.tearDown()
    def _witness_down(self): return mock.patch.object(rc, "verify_witness", side_effect=rc.DataIntegrityFail("WITNESS-FETCH-FAILED fixture transport unavailable"))

    def test_1a_both_unparsable_time_inputs_contribute__digest_coherent(self):
        """B-1a: T_pulse and created_at are two INDEPENDENT inputs; a malformed first must not hide the second. Digest-coherent fixture (created_at via mutate_ev, before the rebind)."""
        env = self.h.build(mutate_ev=lambda ev, evs: ev.update({"created_at": "also-not-a-time"}), mutate_I=lambda I: I.update({"T_pulse": "not-a-time"}))
        msg, out = self.h.refusal(env, feed(env["live"]), ctx=self._witness_down()); c = codes(out)
        self.assertNotIn("EVENT-DIGEST", c, f"the fixture must be digest-coherent so the two timestamp inputs are isolated: {sorted(c)}")
        self.assertIn("IDENTITY-WITNESS-TIME", c, f"the malformed created_at must be contributed: {sorted(c)} | {whys(out)}")
        self.assertIn("IDENTITY-T-PULSE", c, f"the malformed T_pulse is an INDEPENDENT input and must ALSO be contributed: {sorted(c)} | {whys(out)}")

    def test_1b_retained_input_exception_stays_local(self):
        """B-1b: an exception raised by RETAINED data must be classified at its own input boundary, not with the enclosing stage's remote/git label"""
        env = self.h.build(mutate_ev=lambda ev, evs: ev["payload"].update({"commits": [None]}))
        msg, out = self.h.refusal(env, feed(env["live"]), ctx=self._witness_down()); c = codes(out)
        self.assertIn("MALFORMED-RETAINED-INPUT", c, f"a retained-data failure must be a retained-input finding, not a remote/IO one: {sorted(c)} | {whys(out)}")
        self.assertIn("LOCAL-TERMINAL", cls_of(out, "MALFORMED-RETAINED-INPUT"), "and it must carry the local-terminal class")

    def test_1b2_POSITIVE_REGRESSION_same_id_survives_a_broken_delivery_parse(self):
        """NOT fail-first: this ALREADY PASSES on V33 (v1 run 1). Kept so the V34 repair cannot lose it."""
        env = self.h.build(mutate_ev=lambda ev, evs: ev["payload"].update({"commits": [None]}))
        live = [{**env["genuine"], "payload": {**env["genuine"]["payload"], "before": "0" * 40}}] + env["live"]
        msg, out = self.h.refusal(env, feed(live), ctx=self._witness_down())
        self.assertIn("EVENT-FORGED", codes(out), f"the obtainable same-id contradiction must still be collected: {sorted(codes(out))} | {whys(out)}")

    def test_1b3_same_id_contradiction_when_delivery_evaluation_itself_faults(self):
        """B-1b, the reviewer's actual case: the retained approval event's head/before REQUIRE delivery evaluation, that evaluation faults on commits=[None],
        and the live feed carries a COHERENT DIFFERING event of the same id — the contradiction must still be collected."""
        def mut(ev, evs):
            ev["payload"]["commits"] = [None]; ev["payload"]["before"] = "0" * 40      # delivery must be evaluated (before/head do not match by identity)
        env = self.h.build(mutate_ev=mut)
        genuine_other = json.loads(json.dumps(env["genuine"])); genuine_other["payload"]["commits"] = [{"sha": genuine_other["payload"]["head"]}]; genuine_other["created_at"] = "2026-09-06T09:41:00Z"
        msg, out = self.h.refusal(env, feed([genuine_other] + env["live"][1:]), ctx=self._witness_down())
        self.assertIn("EVENT-FORGED", codes(out), f"a coherent differing same-id event must be collected even when delivery evaluation faults: {sorted(codes(out))} | {whys(out)}")

    def _flaky_blob(self, env):
        """inject the read failure at a PINNED PUBLICATION IDENTITY — evs[1]'s head commit — not at the Nth call"""
        target = env["evs"][1]["payload"]["head"]; real = P._blob_at
        def flaky(root, commit, rel):
            if commit == target: raise OSError("fixture: this blob cannot be read")
            return real(root, commit, rel)
        return mock.patch.object(P, "_blob_at", flaky), target

    def test_1c_1_unreadable_blob_never_fakes_pending_push(self):
        """B-1c, first subcase: with _prev never installed, working_tree defaults it to empty bytes and claims PENDING-PUSH for already-published bytes"""
        env = self.h.build(rebuild_after=True); patch, target = self._flaky_blob(env)
        with patch: msg, out = self.h.refusal(env, feed(env["live"]), ctx=self._witness_down())
        self.assertNotIn("PENDING-PUSH", whys(out), f"an unreadable blob at {target[:12]} must never produce a PENDING-PUSH claim about already-published bytes: {whys(out)[:400]}")

    def test_1c_2_unreadable_blob_does_not_stop_the_later_adjacent_relation(self):
        """B-1c, second subcase (separately evidenced: v1 never reached this assertion): the later, independently readable rewrite must still be detected"""
        env = self.h.build(rebuild_after=True); patch, target = self._flaky_blob(env)
        with patch: msg, out = self.h.refusal(env, feed(env["live"]), ctx=self._witness_down())
        self.assertIn("HISTORY-NOT-AN-EXTENSION", whys(out), f"the rewrite after the unreadable blob at {target[:12]} must still be detected: {whys(out)[:400]}")

    def test_1c_3_the_unreadable_blob_is_itself_accounted_for(self):
        """B-1c, third subcase: the failed read must be a finding or a named block — never silently absorbed while S5 reports completed"""
        env = self.h.build(rebuild_after=True); patch, target = self._flaky_blob(env)
        with patch: msg, out = self.h.refusal(env, feed(env["live"]), ctx=self._witness_down())
        accounted = "history-remote" in (out or {}).get("blocked", {}) or any("cannot be read" in f.get("why", "") for f in out["findings"])
        self.assertTrue(accounted, f"the unreadable blob must be recorded: blocked={sorted((out or {}).get('blocked', {}))} | {whys(out)[:300]}")

    def test_1d_adoption_permission_error_blocks_adoption_identity_by_name(self):
        """B-1d: any failure to obtain the adopted digest must BLOCK adoption-identity by name; S0h catches only DataIntegrityFail"""
        env = self.h.build()
        with mock.patch.object(rc, "adopted_rule_sha256", side_effect=PermissionError("fixture: adoption file unreadable")):
            msg, out = self.h.refusal(env, feed(env["live"]))
        self.assertTrue("adoption-identity" in (out or {}).get("blocked", {}) or "adoption-identity" in by_check(out),
                        f"adoption-identity must be blocked by name or contribute under its own name: blocked={sorted((out or {}).get('blocked', {}))} by_check={by_check(out)}")

    def test_2_table_verification_catches_a_removed_dynamic_code(self):
        """B-2: EVENT-FORGED is selected through m[o], invisible to a regex over add(...) sites — removing it from the table must FAIL a table test"""
        import unittest as U
        saved = set(rc.INDEPENDENCE["approval-live"]["codes"])
        try:
            rc.INDEPENDENCE["approval-live"]["codes"] = saved - {"EVENT-FORGED"}
            import test_track13_table_vs_code as TV
            with open(os.devnull, "w") as devnull:                                   # closed by the context manager (v1 leaked it)
                r = U.TextTestRunner(verbosity=0, stream=devnull).run(U.defaultTestLoader.loadTestsFromModule(TV))
            self.assertFalse(r.wasSuccessful(), "removing a code the code contributes must make the table verification FAIL; it passed, so the verification does not cover dynamically selected codes")
        finally: rc.INDEPENDENCE["approval-live"]["codes"] = saved

    def test_3_a_verified_expired_receipt_completes_the_whole_call(self):
        """B-3: ONLY the approval event's authentication is expired (history stays authentic); with a receipt that verifies, the built branch must complete and the
        whole call must ACCEPT — V33 falls through to m['EXPIRED'] and raises KeyError."""
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
            out = getattr(rc, "LAST_OUTCOME", None)
        w = whys(out)
        self.assertNotIn("KeyError", w, f"a verified receipt must complete the branch, not raise: {(raised or '')[:120]} | {w[:300]}")
        self.assertNotIn("MALFORMED-REMOTE-EVIDENCE", codes(out), f"a verified receipt must not be reported as malformed remote evidence: {(raised or '')[:120]} | {w[:300]}")
        self.assertIsNone(raised, f"with every other input genuine, a verified expired-approval receipt must let the WHOLE CALL complete: {(raised or '')[:200]} | {w[:300]}")
if __name__ == "__main__": unittest.main()
