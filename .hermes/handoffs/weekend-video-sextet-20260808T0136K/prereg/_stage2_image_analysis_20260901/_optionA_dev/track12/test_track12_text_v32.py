"""Text test WRITTEN AGAINST THE V32 WORDING (the V31-specific test_track11_text_v31 is retained as pinned and stays a V31 test). Fail-first: FAILS against the V31 text."""
import os, re, unittest
from pathlib import Path
class V32Text(unittest.TestCase):
    def test_v32_labels_and_sentences(self):
        r = Path(os.environ["RULE_TEXT"]).read_text(encoding="utf-8")
        self.assertIn("DRAFT V32 — STAGED CANDIDATE", r); self.assertIn("3c. V32", r); self.assertNotIn("3c. V31", r); self.assertIn("V32 of 2026-09-07 is V31 after its complete-package review", r)
        for k in ("NSD", "No Stage Decides", "NO STAGE MAY DECIDE OR ABORT; EVERY STAGE CONTRIBUTES; ONE RESOLVER DECIDES", "INDEPENDENCE TABLE", "(V31-1)", "(V31-2)", "(V31-3)", "(V31-4)", "(V31-5)", "run_configurations_v16", "provenance_designs_v12", "load_identity_composed", "history_findings_v12", "CLASS_ALLOWLIST", "MALFORMED-REMOTE-EVIDENCE", "LAST_OUTCOME", "track12/test_track12_fail_first.py", "track12/test_track12_text_v32.py", "coherent_attacks_v32.py", "V32_CANDIDATE_ATTACK_INSPECTION_20260907.md", "BLANC_ORDER_TRACK12_NSD"): self.assertIn(k, r, k)
        self.assertEqual(re.findall(r"`\\[0-9]`", r), [])
        sec = r[r.index("3c. V32"):]; sec = sec[:sec.index("\n")]; lim = sec[sec.index("DISCLOSED LIMITS"):sec.index("REPAIRED CONTRADICTIONS")]
        for k in ("V27-1", "V28-1", "V29-1", "V30-1", "V31-1", "V31-2", "V31-3", "V31-4"): self.assertNotIn(k, lim, k)
        self.assertIn("UNREPAIRED CONTRADICTIONS: none known", sec); self.assertNotIn("every derivable finding", sec); self.assertNotIn("nothing downstream is skipped", sec)
        self.assertIn("| check | stage | needs | can contribute |", sec)                                                       # the independence table is IN the text
        self.assertIn("driver v16 23 + V15 driver 17 + history_v2 4 + witness v4 3 + builder v32 8 + V15 builder 4 + verdict v32 7", r); self.assertIn("track 12 84 + track 12 text (V32-specific) 1 = 232 tests", r); self.assertIn("232 tests across the 28 suites", r); self.assertNotIn("147 tests across", r)
        self.assertIn("the inspection of THIS candidate is `V32_CANDIDATE_ATTACK_INSPECTION_20260907.md`", r); self.assertIn("## 9. Questions for the seats at the V32 complete-package review", r); self.assertIn("(V32, if ordered; V16–V31's counted)", r)
        self.assertIn("plus the V32-specific test against THIS text", r); self.assertIn("agy passed all sixteen", r)
if __name__ == "__main__": unittest.main()
