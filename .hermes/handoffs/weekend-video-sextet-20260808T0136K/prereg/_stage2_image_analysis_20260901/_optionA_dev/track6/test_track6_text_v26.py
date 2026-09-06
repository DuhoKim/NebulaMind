"""NEW text test WRITTEN AGAINST THE V26 WORDING (Blanc's order 01:05 KST): the V25-era track-5 text test asserts V25's own labels and cannot establish
anything about V26. This file asserts the V26 labels and the V26-facing sentences. Fail-first: it FAILS against the V25 text (labels differ) and
passes against the V26 text. Lives in the lane only; the active V26 review sandbox is not touched (immutability rule)."""
import os, unittest
from pathlib import Path
class V26Text(unittest.TestCase):
    def test_v26_labels_and_sentences(self):
        r = Path(os.environ["RULE_TEXT"]).read_text(encoding="utf-8")
        self.assertIn("DRAFT V26 — STAGED CANDIDATE", r); self.assertIn("3c. V26", r); self.assertNotIn("3c. V25", r); self.assertNotIn("3c. V22", r)
        for name in ("coherent_attacks_v26.py", "build_corpus_identity_v26.py", "beacon_record_drand_v26.py collect", "run_configurations_v10.py", "provenance_designs_v6.py", "test_track6_fail_first.py"): self.assertIn(name, r, name)
        self.assertIn("Re-run `coherent_attacks_v26.py`", r); self.assertNotIn("Re-run `coherent_attacks_v25.py`", r)
        self.assertIn("between later publications", r); self.assertIn("does not authenticate when", r); self.assertIn("ABSENCE IS NEVER FORGERY", r); self.assertIn("EVIDENCE-INCOMPLETE", r)
        self.assertNotIn("on the V22 candidate", r); self.assertIn("118 tests", r)
if __name__ == "__main__": unittest.main()
