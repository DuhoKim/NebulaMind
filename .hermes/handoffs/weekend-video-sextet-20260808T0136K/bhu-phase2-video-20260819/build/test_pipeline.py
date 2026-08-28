#!/usr/bin/env python3
from pathlib import Path
import tempfile
import unittest

import pipeline


class FrozenInputTests(unittest.TestCase):
    def test_packet_and_exact_narration_contract(self):
        frozen = pipeline.load_frozen_inputs()
        self.assertEqual(frozen["gate_token"], "PASS_P2V_PACKET")
        self.assertEqual(len(frozen["panels"]), 10)
        self.assertEqual(frozen["equations"], pipeline.EXPECTED_EQUATIONS)
        for parsed, panel in zip(frozen["script_panels"], frozen["panels"]):
            self.assertEqual(parsed["heading"], panel["assertion_heading"])
            self.assertEqual(parsed["narration"], panel["narration"])
            self.assertEqual(pipeline.text_sha256(panel["narration"]), panel["narration_sha256"])


class CardTests(unittest.TestCase):
    def test_closed_world_text_and_required_geometry(self):
        import render_cards
        with tempfile.TemporaryDirectory() as tmp:
            receipt = render_cards.render_all_cards(Path(tmp))
            self.assertEqual(receipt["equations_projected_exactly"], pipeline.EXPECTED_EQUATIONS)
            self.assertFalse(receipt["other_equations_projected"])
            for card in receipt["cards"]:
                self.assertEqual(card["emitted_text"], card["permitted_text"])
            geometry = receipt["quantitative_geometry"]
            self.assertEqual(geometry["panel_03"]["linear_ladder_rungs"], 730)
            self.assertEqual(geometry["panel_03"]["planck_caveat_markers"], 2)
            self.assertEqual(geometry["panel_04"]["linear_intervals"], 6)
            self.assertEqual(geometry["panel_07"]["order_steps"], 27)
            self.assertEqual(geometry["panel_09"]["bbn_order_steps"], 45)
            self.assertFalse(geometry["panel_09"]["unlabeled_log_compression"])

    def test_all_text_uses_audited_wrapper(self):
        import render_cards
        source = Path(render_cards.__file__).read_text(encoding="utf-8")
        self.assertEqual(source.count("self.draw.text("), 1)


class TimelineTests(unittest.TestCase):
    def test_fixed_grid_and_opening_deadline(self):
        import build_audio
        frozen = pipeline.load_frozen_inputs()
        timeline = build_audio.plan_timeline(frozen["panels"], {panel["id"]: 1.0 for panel in frozen["panels"]})
        self.assertEqual(timeline["master_duration_seconds"], 325.0)
        self.assertLessEqual(timeline["cards"][0]["end_seconds"], 35.0)
        self.assertTrue(240 <= timeline["master_duration_seconds"] <= 360)


class AsrTests(unittest.TestCase):
    def test_numeric_and_spelling_normalization(self):
        import qa_final  # type: ignore[import-not-found]
        pairs = [
            ("10,000 to 100,000 times", "ten thousand to one hundred thousand times"),
            ("about 730", "about seven hundred and thirty"),
            ("6.6 times 10 to the power 26", "six point six times ten to the power of twenty six"),
            ("2 trillion", "two trillion"),
            ("NebulaMind programme", "Nebula Mind program"),
            ("NebulaMind programme", "nebula-mind program"),
            ("Popławski", "Poplawski"),
            ("fermions' intrinsic spin", "Fermion's intrinsic spin"),
            ("nucleosynthesis", "nuclear synthesis"),
        ]
        for expected, transcript in pairs:
            with self.subTest(expected=expected):
                self.assertEqual(qa_final.normalize_words(expected), qa_final.normalize_words(transcript))

    def test_contract_judgment_never_calls_a_number_cosmetic(self):
        import qa_final  # type: ignore[import-not-found]
        expected = "The value is 45 orders below the bound."
        diff = qa_final.alignment(expected, "The value is 44 orders below the bound.")
        judged = qa_final.judge_mismatches("09", expected, diff)
        self.assertEqual(judged[0]["judgment"], "contract-bearing")

    def test_observed_paper_chain_name_phonetic_is_cosmetic_not_erased(self):
        import qa_final  # type: ignore[import-not-found]
        expected = pipeline.load_frozen_inputs()["panels"][9]["narration"]
        transcript = expected.replace("1 published Popławski", "one published Popovsky")
        diff = qa_final.alignment(expected, transcript)
        judged = qa_final.judge_mismatches("10", expected, diff)
        self.assertEqual(judged[0]["judgment"], "cosmetic")


if __name__ == "__main__":
    unittest.main()
