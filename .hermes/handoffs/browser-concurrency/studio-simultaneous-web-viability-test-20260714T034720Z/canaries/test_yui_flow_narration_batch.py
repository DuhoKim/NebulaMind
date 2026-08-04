import importlib.util
import unittest
from pathlib import Path

SCRIPT = Path(__file__).with_name("yui_flow_narration_batch_02_07.py")
SPEC = importlib.util.spec_from_file_location("narration_batch", SCRIPT)
assert SPEC and SPEC.loader
M = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(M)


class NarrationBatchTests(unittest.TestCase):
    def test_brief_has_exact_six_prompts_and_stable_descriptor(self):
        rows = M.parse_brief()
        self.assertEqual(list(rows), [2, 3, 4, 5, 6, 7])
        for row in rows.values():
            self.assertEqual(row["prompt"].count(M.NARRATOR), 1)
            self.assertTrue(row["spoken_line"])

    def test_wording_exact_passes(self):
        expected = "Agents debate and verify every claim."
        result = M.assess_wording(expected, expected)
        self.assertTrue(result["pass"])
        self.assertEqual(result["missing_tokens"], [])

    def test_ai_and_contraction_normalization_passes(self):
        expected = "Here's how. A.I. agents continuously read the latest research papers and real survey data."
        observed = "Here is how AI agents continuously read the latest research papers and real survey data."
        result = M.assess_wording(expected, observed)
        self.assertTrue(result["pass"])
        self.assertEqual(result["missing_tokens"], [])

    def test_dropped_word_fails(self):
        expected = "Every claim backed by real cited sources, never invented references."
        observed = "Every claim backed by cited sources, never invented references."
        result = M.assess_wording(expected, observed)
        self.assertFalse(result["pass"])
        self.assertEqual(result["missing_tokens"], ["real"])

    def test_extra_spoken_word_fails(self):
        expected = "The result is a living encyclopedia, evidence-linked and self-correcting."
        observed = "The result is a living encyclopedia, tethered, evidence-linked and self-correcting."
        result = M.assess_wording(expected, observed)
        self.assertFalse(result["pass"])
        self.assertEqual(result["extra_tokens"], ["tethered"])

    def test_spoken_domain_and_written_domain_are_equivalent(self):
        expected = "Explore it at nebula mind dot net."
        observed = "Explore it at NebulaMind.net."
        result = M.assess_wording(expected, observed)
        self.assertTrue(result["pass"])
        self.assertEqual(result["missing_tokens"], [])
        self.assertEqual(result["extra_tokens"], [])

    def test_choose_attempt_prefers_quality_pass(self):
        attempts = [
            {"attempt": 1, "analysis": {"quality_pass": False, "quality_score": 200.0}},
            {"attempt": 2, "analysis": {"quality_pass": True, "quality_score": 100.0}},
        ]
        self.assertEqual(M.choose_attempt(attempts)["attempt"], 2)

    def test_reference_signal_features_are_well_formed(self):
        features = M.signal_features(M.REFERENCE)
        self.assertGreater(features["duration_s"], 7.0)
        self.assertIsNotNone(features["median_f0_hz"])
        self.assertEqual(len(features["signature"]), 64)

    def test_runner_has_no_direct_ledger_writer(self):
        source = SCRIPT.read_text()
        self.assertNotIn("journal.py", source)
        self.assertNotIn("broker/journal", source)
        self.assertNotIn("RUN_LEDGER.jsonl", source)


if __name__ == "__main__":
    unittest.main()
