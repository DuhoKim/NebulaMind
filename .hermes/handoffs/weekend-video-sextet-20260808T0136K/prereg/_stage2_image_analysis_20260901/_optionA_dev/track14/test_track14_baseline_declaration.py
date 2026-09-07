"""V34 B-4: executed defect-only findings must match the frozen declaration exactly."""
import unittest
from collections import Counter
import test_track14_nsd_table_v18 as controls
from BASELINE_DECLARATIONS_V18 import DECLARED


class BaselineDeclaration(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.t = controls.TF.T("test_composed_mode_on_the_production_call_path")
        cls.t.setUp()
        cls.h = controls.H13(cls.t)

    @classmethod
    def tearDownClass(cls):
        cls.t.tearDown()

    def observed(self, defect):
        self.assertEqual(set(DECLARED), set(controls.DEFECTS), "declaration must cover every recipe exactly")
        msg, out = controls.run_case(self, [], defect)
        fs = out["findings"]
        recipe = controls.DEFECTS[defect]
        self.assertTrue(any(f["check"] == defect and f["code"] == recipe["code"]
                            and ("reason" not in recipe or recipe["reason"] in f["why"])
                            for f in fs), "the defect's own finding must carry its code and declared reason")
        self.assertEqual(out["blocked"], {}, "defect-only scenario must not block checks")
        winner = controls.PC.resolve([controls.PC.finding(f["class"], f["code"], f["why"], f["stage"], i, f["check"])
                                      for i, f in enumerate(fs)])
        self.assertTrue(msg.startswith(winner["code"]))
        self.assertEqual(controls.counts_by_check(fs),
                         {check: Counter(tuple(row) for row in rows) for check, rows in DECLARED[defect].items()},
                         "finding multiplicity must match the frozen declaration")
        return controls.by_check(fs)

    def test_open_local(self):
        """POSITIVE-REGRESSION: open-local matches the frozen V34 declaration."""
        self.assertEqual(self.observed('open-local'), controls.baseline('open-local'))

    def test_approval_local(self):
        """POSITIVE-REGRESSION: approval-local matches the frozen V34 declaration."""
        self.assertEqual(self.observed('approval-local'), controls.baseline('approval-local'))

    def test_approval_delivery(self):
        """POSITIVE-REGRESSION: approval-delivery matches the frozen V34 declaration."""
        self.assertEqual(self.observed('approval-delivery'), controls.baseline('approval-delivery'))

    def test_lists(self):
        """POSITIVE-REGRESSION: lists matches the frozen V34 declaration."""
        self.assertEqual(self.observed('lists'), controls.baseline('lists'))

    def test_identity_local(self):
        """POSITIVE-REGRESSION: identity-local matches the frozen V34 declaration."""
        self.assertEqual(self.observed('identity-local'), controls.baseline('identity-local'))

    def test_nonce(self):
        """POSITIVE-REGRESSION: nonce matches the frozen V34 declaration."""
        self.assertEqual(self.observed('nonce'), controls.baseline('nonce'))

    def test_adoption(self):
        """POSITIVE-REGRESSION: adoption matches the frozen V34 declaration."""
        self.assertEqual(self.observed('adoption'), controls.baseline('adoption'))

    def test_adoption_identity(self):
        """POSITIVE-REGRESSION: adoption-identity matches the frozen V34 declaration."""
        self.assertEqual(self.observed('adoption-identity'), controls.baseline('adoption-identity'))

    def test_identity_time_order(self):
        """POSITIVE-REGRESSION: identity-time-order matches the frozen V34 declaration."""
        self.assertEqual(self.observed('identity-time-order'), controls.baseline('identity-time-order'))

    def test_history_working_tree(self):
        """POSITIVE-REGRESSION: history-working-tree matches the frozen V34 declaration."""
        self.assertEqual(self.observed('history-working-tree'), controls.baseline('history-working-tree'))

    def test_conjunction(self):
        """POSITIVE-REGRESSION: conjunction matches the frozen V34 declaration."""
        self.assertEqual(self.observed('conjunction'), controls.baseline('conjunction'))

    def test_approval_live(self):
        """POSITIVE-REGRESSION: approval-live matches the frozen V34 declaration."""
        self.assertEqual(self.observed('approval-live'), controls.baseline('approval-live'))

    def test_open_same_id(self):
        """POSITIVE-REGRESSION: open-same-id matches the frozen V34 declaration."""
        self.assertEqual(self.observed('open-same-id'), controls.baseline('open-same-id'))

    def test_seed(self):
        """POSITIVE-REGRESSION: seed matches the frozen V34 declaration."""
        self.assertEqual(self.observed('seed'), controls.baseline('seed'))

    def test_history_remote(self):
        """POSITIVE-REGRESSION: history-remote matches the frozen V34 declaration."""
        self.assertEqual(self.observed('history-remote'), controls.baseline('history-remote'))

    def test_open_delivery_auth(self):
        """POSITIVE-REGRESSION: open-delivery-auth matches the frozen V34 declaration."""
        self.assertEqual(self.observed('open-delivery-auth'), controls.baseline('open-delivery-auth'))

    def test_per_entry(self):
        """POSITIVE-REGRESSION: per-entry matches the frozen V34 declaration."""
        self.assertEqual(self.observed('per-entry'), controls.baseline('per-entry'))


if __name__ == "__main__":
    unittest.main()
