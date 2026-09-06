"""Text test WRITTEN AGAINST THE V33 WORDING (the V32-specific test_track12_text_v32 is retained as pinned and stays a V32 test). Fail-first: FAILS against the V32 text."""
import os, re, unittest
from pathlib import Path
class V33Text(unittest.TestCase):
    def test_v33_labels_and_sentences(self):
        r = Path(os.environ["RULE_TEXT"]).read_text(encoding="utf-8")
        self.assertIn("DRAFT V33 — STAGED CANDIDATE", r); self.assertIn("3c. V33", r); self.assertNotIn("3c. V32", r); self.assertIn("V33 of 2026-09-07 is V32 after its complete-package review", r)
        for k in ("(V32-1)", "(V32-2)", "(V32-3)", "(V32-4)", "(V32-5)", "seat A (agy) TIMED OUT", "DISAPPEARANCE IS NOT COMPLETION", "not a verdict", "run_configurations_v17", "provenance_designs_v13", "precedence_core", "INDEPENDENCE TABLE", "verified against the code", "test_track13_table_vs_code.py", "track13/test_track13_nsd_table.py", "track13/test_track13_regressions.py", "track13/test_track13_text_v33.py", "coherent_attacks_v33.py", "V33_CANDIDATE_ATTACK_INSPECTION_20260907.md", "DISPATCH_DEFECT_SEAT_CHILD_KEEPS_WRAPPER_ALIVE_20260907.md", "plausibility", "approval_bytes_source", "check"): self.assertIn(k, r, k)
        self.assertEqual(re.findall(r"`\\[0-9]`", r), [])
        sec = r[r.index("3c. V33"):]; sec = sec[:sec.index("\n")]; lim = sec[sec.index("DISCLOSED LIMITS"):sec.index("REPAIRED CONTRADICTIONS")]
        for k in ("V27-1", "V28-1", "V29-1", "V30-1", "V31-1", "V32-1", "V32-2", "V32-3"): self.assertNotIn(k, lim, k)
        self.assertIn("UNREPAIRED CONTRADICTIONS: none known", sec); self.assertNotIn("every derivable finding", sec); self.assertIn("| check | stage | needs | can contribute |", sec)
        self.assertIn("driver v17 23 + V15 driver 17 + history_v2 4 + witness v4 3 + builder v33 8 + V15 builder 4 + verdict v33 7", r); self.assertIn("track 13 regressions 16 + track 13 controls 116 + track 13 table-vs-code 4 + track 13 text (V33-specific) 1 = 369 tests", r); self.assertIn("369 tests across the 32 suites", r); self.assertNotIn("232 tests across", r)
        self.assertIn("the inspection of THIS candidate is `V33_CANDIDATE_ATTACK_INSPECTION_20260907.md`", r); self.assertIn("## 9. Questions for the seats at the V33 complete-package review", r); self.assertIn("(V33, if ordered; V16–V32's counted)", r)
        self.assertIn("plus the V33-specific test against THIS text", r); self.assertIn("agy passed all sixteen it completed, and its seventeenth review timed out without a final answer", r)
if __name__ == "__main__": unittest.main()
