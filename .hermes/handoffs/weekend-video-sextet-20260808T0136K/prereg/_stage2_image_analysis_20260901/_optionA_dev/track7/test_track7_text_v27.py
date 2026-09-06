"""Text test WRITTEN AGAINST THE V27 WORDING (the V26-specific test_track6_text_v26 is retained as pinned and stays a V26 test). Fail-first: FAILS against the V26 text."""
import os, unittest
from pathlib import Path
class V27Text(unittest.TestCase):
    def test_v27_labels_and_sentences(self):
        r = Path(os.environ["RULE_TEXT"]).read_text(encoding="utf-8")
        self.assertIn("DRAFT V27 — STAGED CANDIDATE", r); self.assertIn("3c. V27", r); self.assertNotIn("3c. V26", r)
        for name in ("coherent_attacks_v27.py", "build_corpus_identity_v27.py", "beacon_record_drand_v27.py collect", "run_configurations_v11.py", "provenance_designs_v7.py", "test_track7_fail_first.py", "test_track7_text_v27.py"): self.assertIn(name, r, name)
        self.assertIn("Re-run `coherent_attacks_v27.py`", r); self.assertNotIn("beacon_record_drand_v22.collect", r)
        self.assertIn("INCONSISTENT-INPUT", r); self.assertIn("UNDETERMINED", r); self.assertIn("same event id", r)
        self.assertIn("between later publications", r); self.assertIn("ABSENCE IS NEVER FORGERY", r); self.assertNotIn("on the V22 candidate", r)
if __name__ == "__main__": unittest.main()
