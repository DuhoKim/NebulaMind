"""Text test WRITTEN AGAINST THE V31 WORDING (the V30-specific test_track10_text_v30 is retained as pinned and stays a V30 test). Fail-first: FAILS against the V30 text."""
import os, re, unittest
from pathlib import Path
class V31Text(unittest.TestCase):
    def test_v31_labels_and_sentences(self):
        r = Path(os.environ["RULE_TEXT"]).read_text(encoding="utf-8")
        self.assertIn("DRAFT V31 — STAGED CANDIDATE", r); self.assertIn("3c. V31", r); self.assertNotIn("3c. V30", r); self.assertIn("V31 of 2026-09-07 is V30 after its complete-package review", r)
        for k in ("(V30-1)", "(V30-2)", "(V30-3)", "(V30-4)", "FATAL", "the lane's own", "run_configurations_v15", "provenance_designs_v11", "load_identity_composed", "history_findings_v11", "classify_refusal", "classify_exception", "HISTORY-OPEN-EVENT-INVALID", "No required stage can be skipped into acceptance", "one evidence snapshot", "PENDING-PUSH", "track11/test_track11_fail_first.py", "track11/test_track11_text_v31.py", "coherent_attacks_v31.py", "V31_CANDIDATE_ATTACK_INSPECTION_20260907.md", "REQUIRED_STAGES"): self.assertIn(k, r, k)
        self.assertEqual(re.findall(r"`\\[0-9]`", r), [])
        sec = r[r.index("3c. V31"):]; sec = sec[:sec.index("\n")]; lim = sec[sec.index("DISCLOSED LIMITS"):sec.index("REPAIRED CONTRADICTIONS")]
        for k in ("V27-1", "V27-2", "V28-1", "V28-2", "V29-1", "V29-2", "V30-1", "V30-2", "V30-3"): self.assertNotIn(k, lim, k)
        self.assertIn("UNREPAIRED CONTRADICTIONS: none known", sec); self.assertIn("S0", sec); self.assertIn("S5", sec)
        self.assertIn("driver v15 23 + V15 driver 17 + history_v2 4 + witness v4 3 + builder v31 8 + V15 builder 4 + verdict v31 7", r); self.assertIn("track 11 5 + track 11 text (V31-specific) 1 = 147 tests", r); self.assertIn("147 tests across the 26 suites", r); self.assertNotIn("141 tests across", r)
        self.assertIn("the inspection of THIS candidate is `V31_CANDIDATE_ATTACK_INSPECTION_20260907.md`", r); self.assertIn("## 9. Questions for the seats at the V31 complete-package review", r); self.assertIn("(V31, if ordered; V16–V30's counted)", r)
        self.assertIn("plus the V31-specific test against THIS text", r); self.assertIn("agy passed all fifteen", r)
if __name__ == "__main__": unittest.main()
