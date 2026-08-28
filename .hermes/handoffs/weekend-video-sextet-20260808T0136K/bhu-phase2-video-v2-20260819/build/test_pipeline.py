#!/usr/bin/env python3
from pathlib import Path
import tempfile
import unittest

import pipeline


class FrozenInputTests(unittest.TestCase):
    def test_packet_assets_and_exact_narration_contract(self):
        frozen = pipeline.load_frozen_inputs()
        self.assertEqual(frozen["gate_token"], "PASS_P2V2_PACKET")
        self.assertEqual(len(frozen["panels"]), 12)
        self.assertEqual(len(frozen["asset_pins"]), 4)
        self.assertEqual(frozen["equations"], pipeline.EXPECTED_EQUATIONS)
        self.assertIn(pipeline.PANEL_09_FIXED_LABEL, pipeline.render_viewer_text(frozen["panels"][8]))
        for parsed, panel in zip(frozen["script_panels"], frozen["panels"]):
            self.assertEqual(parsed["heading"], panel["assertion_heading"])
            self.assertEqual(parsed["narration"], panel["narration"])
            self.assertEqual(pipeline.text_sha256(panel["narration"]), panel["narration_sha256"])


class CardTests(unittest.TestCase):
    def test_closed_world_text_figures_and_required_geometry(self):
        import render_cards
        with tempfile.TemporaryDirectory() as tmp:
            receipt = render_cards.render_all_cards(Path(tmp))
            self.assertEqual(receipt["equations_projected_exactly"], pipeline.EXPECTED_EQUATIONS)
            self.assertFalse(receipt["other_equations_projected"])
            self.assertEqual(receipt["no_plots_panels"], ["02", "06", "08"])
            self.assertTrue(receipt["paper_assets_verified_before_embedding"])
            for panel in receipt["panels"]:
                for text in panel["permitted_text"]:
                    self.assertGreaterEqual(panel["emission_counts"].get(text, 0), 1)
                for state in panel["states"]:
                    self.assertEqual(state["emitted_text"][0], panel["heading"])
            geometry = receipt["quantitative_geometry"]
            self.assertEqual(geometry["panel_05"]["audit"]["linear_ladder_rungs"], 730)
            self.assertTrue(geometry["panel_05"]["plot"]["planck_marker_outside_paper_pixels"])
            self.assertEqual(geometry["panel_09"]["ceiling"]["treatment_band_edges"], 2)
            self.assertEqual(geometry["panel_11"]["main"]["signal_range_band_edges"], 2)

    def test_all_text_uses_audited_wrapper(self):
        import render_cards
        source = Path(render_cards.__file__).read_text(encoding="utf-8")
        self.assertEqual(source.count("self.draw.text("), 1)


class TimelineTests(unittest.TestCase):
    def test_fixed_grid_and_opening_deadline(self):
        import build_audio
        frozen = pipeline.load_frozen_inputs()
        timeline = build_audio.plan_timeline(frozen["panels"], {panel["id"]: 1.0 for panel in frozen["panels"]})
        self.assertEqual(timeline["master_duration_seconds"], 473.0)
        self.assertLessEqual(timeline["cards"][0]["end_seconds"], 35.0)
        self.assertTrue(390 <= timeline["master_duration_seconds"] <= 480)


class AsrTests(unittest.TestCase):
    def test_numeric_and_token_normalization(self):
        import qa_final
        pairs = [
            ("10,000 to 100,000 times", "ten thousand to one hundred thousand times"),
            ("about 730", "about seven hundred and thirty"),
            ("6.6 times 10 to the power 26", "six point six times ten to the power of twenty six"),
            ("2 trillion", "two trillion"),
            ("NebulaMind", "Nebula Mind"),
            ("big-bang nucleosynthesis", "big bang nucleosynthesis"),
            ("10 megaelectronvolts", "ten mega electron volts"),
            ("The 2012 paper", "The twenty twelve paper"),
        ]
        for expected, transcript in pairs:
            with self.subTest(expected=expected):
                self.assertEqual(qa_final.normalize_words(expected), qa_final.normalize_words(transcript))

    def test_number_and_protected_phrase_are_never_cosmetic(self):
        import qa_final
        expected = pipeline.load_frozen_inputs()["panels"][8]["narration"]
        number_diff = qa_final.alignment(expected, expected.replace("6.6", "6.5"))
        self.assertEqual(qa_final.judge_mismatches("09", expected, number_diff)[0]["judgment"], "contract-bearing")
        phrase_diff = qa_final.alignment(expected, expected.replace("there is even less to see", "there is less to see"))
        self.assertEqual(qa_final.judge_mismatches("09", expected, phrase_diff)[0]["judgment"], "contract-bearing")


if __name__ == "__main__":
    unittest.main()
