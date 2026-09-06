"""Text test WRITTEN AGAINST THE V30 WORDING (the V29-specific test_track9_text_v29 is retained as pinned and stays a V29 test). Fail-first: FAILS against the V29 text."""
import os, re, unittest
from pathlib import Path
class V30Text(unittest.TestCase):
    def test_v30_labels_and_sentences(self):
        r = Path(os.environ["RULE_TEXT"]).read_text(encoding="utf-8")
        self.assertIn("DRAFT V30 — STAGED CANDIDATE", r); self.assertIn("3c. V30", r); self.assertNotIn("3c. V29", r); self.assertIn("V30 of 2026-09-07 is V29 after its complete-package review", r)
        for k in ("(V29-1)", "(V29-2)", "(V29-3)", "(V29-4)", "run_configurations_v14", "provenance_designs_v10", "composed_resolver", "PRECEDENCE ORDER, STATED ONCE", "0 LOCAL-TERMINAL", "7 ACCEPT", "V30_PRECEDENCE_EXHIBIT_20260907.md", "BLANC_ORDER_PRECEDENCE_IS_ONE_PATTERN.md", "track10/test_track10_fail_first.py", "track10/test_track10_text_v30.py", "track10/exhibit_precedence_pairs.py", "coherent_attacks_v30.py", "V30_CANDIDATE_ATTACK_INSPECTION_20260907.md", "Before any retry is returned from load_identity", "feed iteration order is not an unstated tie-break"): self.assertIn(k, r, k)
        self.assertEqual(re.findall(r"`\\[0-9]`", r), [])
        sec = r[r.index("3c. V30"):]; sec = sec[:sec.index("\n")]; lim = sec[sec.index("DISCLOSED LIMITS"):sec.index("REPAIRED CONTRADICTIONS")]
        for k in ("V27-1", "V27-2", "V28-1", "V28-2", "V29-1", "V29-2"): self.assertNotIn(k, lim, k)
        self.assertIn("UNREPAIRED CONTRADICTIONS: none known", sec)
        self.assertIn("driver v14 23 + V15 driver 17 + history_v2 4 + witness v4 3 + builder v30 8 + V15 builder 4 + verdict v30 7", r); self.assertIn("track 10 4 + track 10 text (V30-specific) 1 = 141 tests", r); self.assertIn("141 tests across the 24 suites", r); self.assertNotIn("136 tests across", r)
        self.assertIn("the inspection of THIS candidate is `V30_CANDIDATE_ATTACK_INSPECTION_20260907.md`", r); self.assertIn("## 9. Questions for the seats at the V30 complete-package review", r); self.assertIn("(V30, if ordered; V16–V29's counted)", r)
        self.assertIn("plus the V30-specific test against THIS text", r); self.assertIn("agy passed all fourteen", r)
if __name__ == "__main__": unittest.main()
