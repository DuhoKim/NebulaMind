"""Text test WRITTEN AGAINST THE V28 WORDING (the V27-specific test_track7_text_v27 is retained as pinned and stays a V27 test). Fail-first: FAILS against the V27 text.
Blanc 02:06 KST: the text must keep DISCLOSED LIMITS and REPAIRED CONTRADICTIONS apart, and must not present V27-1/V27-2 as limits."""
import os, re, unittest
from pathlib import Path
class V28Text(unittest.TestCase):
    def test_v28_labels_and_sentences(self):
        r = Path(os.environ["RULE_TEXT"]).read_text(encoding="utf-8")
        self.assertIn("DRAFT V28 — STAGED CANDIDATE", r); self.assertIn("3c. V28", r); self.assertNotIn("3c. V27", r)
        self.assertIn("V28 of 2026-09-07 is V27 after its complete-package review", r)
        for k in ("(V27-1)", "(V27-2)", "(V27-3)", "run_configurations_v12", "provenance_designs_v8", "validate_continuation_v8", "build_corpus_identity_v28", "beacon_record_drand_v28", "coherent_attacks_v28.py", "track8/test_track8_fail_first.py", "track8/test_track8_text_v28.py", "V28_CANDIDATE_ATTACK_INSPECTION_20260907.md", "LIMITS_VS_CONTRADICTIONS_20260907.md", "BLANC_ORDER_V27_CONTRADICTIONS_NOT_LIMITS.md"): self.assertIn(k, r, k)
        sec = r[r.index("3c. V28"):]; sec = sec[:sec.index("\n")]
        self.assertIn("DISCLOSED LIMITS", sec); self.assertIn("REPAIRED CONTRADICTIONS", sec); self.assertIn("UNREPAIRED CONTRADICTIONS: none known", sec)
        self.assertLess(sec.index("DISCLOSED LIMITS"), sec.index("REPAIRED CONTRADICTIONS"))
        lim = sec[sec.index("DISCLOSED LIMITS"):sec.index("REPAIRED CONTRADICTIONS")]; self.assertNotIn("V27-1", lim); self.assertNotIn("V27-2", lim)   # the contradictions are NOT listed among the limits
        self.assertIn("track 8 7 + track 8 text (V28-specific) 1 = 132 tests", r); self.assertIn("132 tests across the 20 suites", r); self.assertNotIn("seventeen suites", r); self.assertNotIn("124 tests across", r)
        self.assertNotIn("THIS candidate — two still pass", r); self.assertIn("the inspection of THIS candidate is `V28_CANDIDATE_ATTACK_INSPECTION_20260907.md`", r)
        self.assertIn("## 9. Questions for the seats at the V28 complete-package review", r); self.assertIn("(V28, if ordered; V16–V27's counted)", r)
        self.assertIn("plus the V28-specific test against THIS text", r); self.assertIn("agy passed all twelve", r)
        for pin in re.findall(r"`(run_configurations_v12\.py|provenance_designs_v8\.py|build_corpus_identity_v28\.py|beacon_record_drand_v28\.py|coherent_attacks_v28\.py)`,? (?:SHA-256 )?\(?`([0-9a-f]{64})`", r): self.assertEqual(len(pin[1]), 64)
if __name__ == "__main__": unittest.main()
