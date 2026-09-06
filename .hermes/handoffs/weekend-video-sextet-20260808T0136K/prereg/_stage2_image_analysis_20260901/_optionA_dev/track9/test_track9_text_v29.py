"""Text test WRITTEN AGAINST THE V29 WORDING (the V28-specific test_track8_text_v28 is retained as pinned and stays a V28 test). Fail-first: FAILS against the V28 text."""
import os, unittest
from pathlib import Path
class V29Text(unittest.TestCase):
    def test_v29_labels_and_sentences(self):
        r = Path(os.environ["RULE_TEXT"]).read_text(encoding="utf-8")
        self.assertIn("DRAFT V29 — STAGED CANDIDATE", r); self.assertIn("3c. V29", r); self.assertNotIn("3c. V28", r); self.assertIn("V29 of 2026-09-07 is V28 after its complete-package review", r)
        for k in ("(V28-1)", "(V28-2)", "(V28-3)", "run_configurations_v13", "provenance_designs_v9", "validate_continuation_v9", "build_corpus_identity_v29", "beacon_record_drand_v29", "coherent_attacks_v29.py", "track9/test_track9_fail_first.py", "track9/test_track9_text_v29.py", "V29_CANDIDATE_ATTACK_INSPECTION_20260907.md", "unresolved delivery does not bypass live authentication", "a later event does not invalidate an authentic earliest event"): self.assertIn(k, r, k)
        sec = r[r.index("3c. V29"):]; sec = sec[:sec.index("\n")]
        lim = sec[sec.index("DISCLOSED LIMITS"):sec.index("REPAIRED CONTRADICTIONS")]
        for k in ("V27-1", "V27-2", "V28-1", "V28-2"): self.assertNotIn(k, lim, k)
        self.assertIn("default-mode implementation limit", lim); self.assertIn("stateless closure enforcement", lim); self.assertIn("UNREPAIRED CONTRADICTIONS: none known", sec)
        self.assertIn("track 9 3 + track 9 text (V29-specific) 1 = 136 tests", r); self.assertIn("136 tests across the 22 suites", r); self.assertNotIn("132 tests across", r)
        self.assertIn("the inspection of THIS candidate is `V29_CANDIDATE_ATTACK_INSPECTION_20260907.md`", r); self.assertIn("## 9. Questions for the seats at the V29 complete-package review", r); self.assertIn("(V29, if ordered; V16–V28's counted)", r)
        self.assertIn("plus the V29-specific test against THIS text", r); self.assertIn("agy passed all thirteen", r)
if __name__ == "__main__": unittest.main()
