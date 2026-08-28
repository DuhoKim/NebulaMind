#!/usr/bin/env python3
import json
import unittest
from pathlib import Path

import pipeline


class FrozenInputs(unittest.TestCase):
    def test_gate_assets_and_narration_mirror(self):
        frozen = pipeline.load_frozen_inputs()
        self.assertTrue(frozen["gate_token"].startswith("PASS_P2V3_PACKET"))
        self.assertEqual(len(frozen["panels"]), 16)
        self.assertEqual(len(frozen["asset_pins"]), 5)
        self.assertEqual(frozen["equations"], pipeline.EXPECTED_EQUATIONS)
        for parsed, panel in zip(frozen["script_panels"], frozen["panels"]):
            self.assertEqual(parsed["heading"], panel["assertion_heading"])
            self.assertEqual(parsed["narration"], panel["narration"])
            self.assertEqual(pipeline.text_sha256(panel["narration"]), panel["narration_sha256"])


class VisualContract(unittest.TestCase):
    def test_states_stills_equations_and_plot_walkthroughs(self):
        receipt = json.loads((pipeline.BUILD / "visual-receipt.json").read_text(encoding="utf-8"))
        self.assertEqual(receipt["status"], "PASS_NEW_V3_DESIGN_SYSTEM_STATES_RENDERED")
        self.assertEqual(receipt["equations_projected_exactly"], pipeline.EXPECTED_EQUATIONS)
        self.assertFalse(receipt["other_equations_projected"])
        self.assertEqual(len(receipt["panels"]), 16)
        self.assertEqual(receipt["generated_image_usage"]["panel"], "01")
        walkers = [(p["id"], s["name"]) for p in receipt["panels"] for s in p["states"] if s["cursor_points"]]
        self.assertEqual(walkers, [("07","plot"),("08","plot"),("14","figure1"),("14","figure2")])
        for panel in receipt["panels"]:
            still = pipeline.BUILD / panel["representative_still"]
            self.assertTrue(still.is_file())
            self.assertEqual(pipeline.sha256(still), panel["representative_still_sha256"])
            for state in panel["states"]:
                path = pipeline.BUILD / state["path"]
                self.assertEqual(pipeline.sha256(path), state["sha256"])
                self.assertEqual(state["emitted_text"][0], panel["heading"])


class AudioContract(unittest.TestCase):
    def test_exact_text_measured_pace_and_breathing_gaps(self):
        timeline = json.loads((pipeline.BUILD / "audio/timeline.json").read_text(encoding="utf-8"))
        self.assertTrue(timeline["all_tts_inputs_byte_identical_to_storyboard_narration"])
        self.assertFalse(timeline["voice_was_sped_up"])
        self.assertGreaterEqual(timeline["measured_narration_wpm"], 124.5)
        self.assertLessEqual(timeline["measured_narration_wpm"], 135.5)
        self.assertGreaterEqual(timeline["master_duration_seconds"], 600)
        self.assertLessEqual(timeline["master_duration_seconds"], 720)
        self.assertTrue(all(card["panel_turn_silence_seconds"] >= 1.75 for card in timeline["cards"]))
        self.assertEqual(len(timeline["panel_wavs"]), 16)
        for item in timeline["panel_wavs"]:
            self.assertTrue(item["concatenated_fragments_byte_identical_to_storyboard"])
            wav = pipeline.BUILD / item["audio"]
            self.assertEqual(pipeline.sha256(wav), item["audio_sha256"])


class AsrNormalization(unittest.TestCase):
    def test_contract_number_forms(self):
        import qa_final
        pairs = [
            ("10,000 to 100,000 times", "ten thousand to one hundred thousand times"),
            ("about 730 times", "about seven hundred and thirty times"),
            ("6.6 times 10 to the power 26", "six point six times ten to the 26th power"),
            ("spin-0.7", "spin zero point seven"),
            ("2 trillion", "two trillion"),
            ("10 megaelectronvolts", "ten mega electron volts"),
        ]
        for expected, transcript in pairs:
            with self.subTest(expected=expected):
                self.assertEqual(qa_final.normalize_words(expected), qa_final.normalize_words(transcript))


if __name__ == "__main__":
    unittest.main()
