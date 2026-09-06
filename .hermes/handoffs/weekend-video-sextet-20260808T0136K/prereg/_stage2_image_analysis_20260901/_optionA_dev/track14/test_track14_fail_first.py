"""TRACK 14 — FAIL-FIRST reproduction of seat B's V33 counter-cases, BEFORE any repair (the V20 rule: reproduce in executed output first).
One subcase per method. Written against the V33 modules (run_configurations_v17 / provenance_designs_v13); each method asserts the behaviour the
CANDIDATE TEXT PROMISES, so against V33 it must FAIL — that failure IS the evidence. The same file is then run against the V34 successors, where it
must pass without any promise being weakened. Seat B's four executed NSD cases are 1a–1d; the table-mutation control is 2; the receipt success path is 3."""
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
class T14(unittest.TestCase):
    @classmethod
    def setUpClass(cls): cls.t = TF.T("test_composed_mode_on_the_production_call_path"); cls.t.setUp(); cls.h = H13(cls.t)
    @classmethod
    def tearDownClass(cls): cls.t.tearDown()
    def _witness_down(self): return mock.patch.object(rc, "verify_witness", side_effect=rc.DataIntegrityFail("WITNESS-FETCH-FAILED fixture transport unavailable"))

    def test_1a_both_unparsable_time_inputs_contribute(self):
        """B-1a: T_pulse and created_at are two INDEPENDENT inputs; a malformed first must not hide the second (text: 'the first failure never hides the next')"""
        def mut(I): I["T_pulse"] = "not-a-time"; I["approval_witness"]["push_event"]["created_at"] = "also-not-a-time"
        env = self.h.build(mutate_I=mut)
        msg, out = self.h.refusal(env, feed(env["live"]), ctx=self._witness_down()); c = codes(out)
        self.assertIn("IDENTITY-T-PULSE", c, f"the malformed T_pulse must be contributed: {sorted(c)} | {whys(out)}")
        self.assertIn("IDENTITY-WITNESS-TIME", c, f"the malformed created_at is an independent input and must ALSO be contributed: {sorted(c)} | {whys(out)}")

    def test_1b_retained_input_exception_stays_local(self):
        """B-1b: an exception raised by RETAINED data must be classified at its own input boundary, not with the enclosing stage's remote/git label"""
        def mut(ev, evs): ev["payload"]["commits"] = [None]
        env = self.h.build(mutate_ev=mut)
        msg, out = self.h.refusal(env, feed(env["live"]), ctx=self._witness_down()); c = codes(out)
        self.assertTrue({"MALFORMED-RETAINED-INPUT"} & c, f"a retained-data failure must be a LOCAL-TERMINAL retained-input finding, not a remote/IO one: {sorted(c)} | {whys(out)}")
        self.assertIn("LOCAL-TERMINAL", cls_of(out, "MALFORMED-RETAINED-INPUT"), "and it must carry the local-terminal class")

    def test_1b2_same_id_contradiction_survives_a_broken_delivery_parse(self):
        """B-1b: delivery parsing must not abort the INDEPENDENT same-id check on the live feed"""
        def mut(ev, evs): ev["payload"]["commits"] = [None]
        env = self.h.build(mutate_ev=mut); live = [{**env["genuine"], "payload": {**env["genuine"]["payload"], "before": "0" * 40}}] + env["live"]
        msg, out = self.h.refusal(env, feed(live), ctx=self._witness_down())
        self.assertIn("EVENT-FORGED", codes(out), f"the obtainable same-id contradiction must still be collected: {sorted(codes(out))} | {whys(out)}")

    def test_1c_one_unreadable_blob_neither_stops_the_loop_nor_fakes_pending_push(self):
        """B-1c: an OSError on ONE committed blob must not abort every later adjacent relation, and must never let the working-tree comparison default _prev to empty (708 published bytes reported PENDING-PUSH)"""
        env = self.h.build(rebuild_after=True); real = P._blob_at; target = {}
        def flaky(root, commit, rel):
            if not target: target["c"] = commit                      # the SECOND blob read of the history walk
            elif commit == target.get("second"): raise OSError("fixture: this blob cannot be read")
            if "second" not in target and commit != target["c"]: target["second"] = commit; raise OSError("fixture: this blob cannot be read")
            return real(root, commit, rel)
        with mock.patch.object(P, "_blob_at", flaky):
            msg, out = self.h.refusal(env, feed(env["live"]), ctx=self._witness_down())
        c = codes(out); w = whys(out)
        self.assertNotIn("PENDING-PUSH", w, f"an unreadable blob must never produce a PENDING-PUSH claim about already-published bytes: {w}")
        self.assertIn("HISTORY-NOT-AN-EXTENSION", w, f"the later, independently readable rewrite must still be detected: {sorted(c)} | {w}")
        self.assertTrue("history-remote" in (out or {}).get("blocked", {}) or any("cannot be read" in f.get("why", "") for f in out["findings"]), f"the unreadable blob must be recorded as a finding or a named block: {out.get('blocked')}")

    def test_1d_adoption_permission_error_blocks_adoption_identity_by_name(self):
        """B-1d: any failure to obtain the adopted digest must BLOCK adoption-identity by name (text: blocked checks are named); S0h catches only DataIntegrityFail"""
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
            r = U.TextTestRunner(verbosity=0, stream=open(os.devnull, "w")).run(U.defaultTestLoader.loadTestsFromModule(TV))
            self.assertFalse(r.wasSuccessful(), "removing a code the code contributes must make the table verification FAIL; it passed, so the verification does not cover dynamically selected codes")
        finally: rc.INDEPENDENCE["approval-live"]["codes"] = saved

    def test_3_a_verified_expired_receipt_completes_the_approval_branch(self):
        """B-3: with a receipt that VERIFIES, the built branch must not refuse — S3a falls through to m['EXPIRED'] and raises KeyError"""
        env = self.h.build(); rp = Path(env["tmp"]) / "receipt.json"; rp.write_text(json.dumps({"fixture": "boundary stub"}))
        TPo = rc.Protocol(**{**env["cTP"].__dict__, "events_receipt": str(rp), "expected_receipt_origin": {"actor": "ops-witness", "session": "OPS"}})
        with mock.patch.object(P, "authenticate_event", lambda *a, **k: ("EXPIRED", "fixture: outside the retained window")), \
             mock.patch.object(P, "verify_events_receipt", lambda *a, **k: (True, "fixture: receipt verifies")):
            try:
                rc.load_identity(env["ident"], rc.Protocol(**{**TPo.__dict__, "events_runner": feed(env["live"])})); out = getattr(rc, "LAST_OUTCOME", None); msg = ""
            except rc.DataIntegrityFail as e: out = getattr(rc, "LAST_OUTCOME", None); msg = str(e)
        w = whys(out)
        self.assertNotIn("KeyError", w, f"a verified receipt must complete the branch, not raise: {msg[:120]} | {w[:300]}")
        self.assertNotIn("MALFORMED-REMOTE-EVIDENCE", codes(out), f"a verified receipt must not be reported as malformed remote evidence: {msg[:120]} | {w[:300]}")
if __name__ == "__main__": unittest.main()
