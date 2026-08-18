#!/usr/bin/env python3
from pathlib import Path
import hashlib
import tempfile
import unittest

import pipeline


class FrozenInputTests(unittest.TestCase):
    def test_load_frozen_inputs_reconstructs_script_and_passed_gate(self):
        frozen = pipeline.load_frozen_inputs()
        self.assertEqual(len(frozen["panels"]), 10)
        self.assertEqual(frozen["gate_token"], "PASS_EXPLAINER_PACKET")
        self.assertEqual(
            hashlib.sha256(frozen["script_path"].read_bytes()).hexdigest(),
            "5c957bef48cdf44e5142affafc54c40af31d84651c69d2d99013ad98c881dc12",
        )
        for parsed, panel in zip(frozen["script_panels"], frozen["panels"]):
            self.assertEqual(parsed["id"], panel["id"])
            self.assertEqual(parsed["heading"], panel["assertion_heading"])
            self.assertEqual(parsed["narration"], panel["narration"])

    def test_sentence_split_preserves_exact_text_and_quoted_period_boundary(self):
        frozen = pipeline.load_frozen_inputs()
        panel = frozen["panels"][0]
        sentences = pipeline.split_sentences(panel["narration"])
        self.assertEqual(" ".join(sentences), panel["narration"])
        self.assertIn('The chain offered 2 neutron-star tests, joined by "or."', sentences)
        self.assertIn("Its heavy-star test reaches serious doubt.", sentences)


class CardRendererTests(unittest.TestCase):
    def test_rendered_cards_use_exact_closed_world_text_and_honest_mass_geometry(self):
        import render_cards

        with tempfile.TemporaryDirectory() as tmp:
            receipt = render_cards.render_all_cards(Path(tmp))
            self.assertEqual(len(receipt["cards"]), 10)
            for card in receipt["cards"]:
                self.assertEqual(card["emitted_text"], card["permitted_text"])
                self.assertTrue(Path(tmp, card["path"]).is_file())
            geometry = receipt["panel_06_geometry"]
            self.assertGreater(geometry["one_sigma_low"], geometry["threshold"])
            self.assertTrue(geometry["strict_95_4_visual_crosses_threshold"])
            self.assertFalse(geometry["strict_95_4_hard_lower_endpoint_drawn"])

    def test_all_viewer_text_flows_through_the_closed_world_audit_wrapper(self):
        import render_cards

        source = Path(render_cards.__file__).read_text(encoding="utf-8")
        self.assertEqual(source.count("draw.text("), 1)


class AudioTimelineTests(unittest.TestCase):
    def test_timeline_reconstructs_exact_narration_on_fixed_card_grid(self):
        import build_audio

        frozen = pipeline.load_frozen_inputs()
        durations = {
            panel["id"]: [0.5] * len(pipeline.split_sentences(panel["narration"]))
            for panel in frozen["panels"]
        }
        timeline = build_audio.plan_timeline(frozen["panels"], durations)
        self.assertEqual(timeline["master_duration_seconds"], 312.0)
        self.assertEqual(timeline["master_sample_count"], 312 * 48000)
        for card, panel in zip(timeline["cards"], frozen["panels"]):
            self.assertEqual(card["heading"], panel["assertion_heading"])
            self.assertEqual(card["narration"], panel["narration"])
            records = [record for record in timeline["records"] if record["card_id"] == panel["id"]]
            self.assertEqual(" ".join(record["text"] for record in records), panel["narration"])
            self.assertLessEqual(card["speech_end_sample"], card["end_sample"])

    def test_audio_first_grid_extends_an_overlong_panel_on_frame_boundaries(self):
        import build_audio

        frozen = pipeline.load_frozen_inputs()
        durations = {
            panel["id"]: [0.5] * len(pipeline.split_sentences(panel["narration"]))
            for panel in frozen["panels"]
        }
        durations["03"] = [10.0] * len(durations["03"])
        timeline = build_audio.plan_timeline(frozen["panels"], durations)
        panel_03 = timeline["cards"][2]
        self.assertGreater(panel_03["effective_seconds"], panel_03["planned_seconds"])
        self.assertEqual(panel_03["effective_seconds"] * 30, panel_03["frame_count"])
        self.assertLessEqual(timeline["master_duration_seconds"], 360.0)


class AssemblyContractTests(unittest.TestCase):
    def test_stream_validator_requires_video_audio_and_default_english_subtitle(self):
        import assemble

        probe = {
            "streams": [
                {"codec_type": "video", "codec_name": "h264", "width": 1920, "height": 1080, "r_frame_rate": "30/1", "nb_frames": "9360"},
                {"codec_type": "audio", "codec_name": "aac", "sample_rate": "48000", "channels": 1},
                {"codec_type": "subtitle", "codec_name": "mov_text", "tags": {"language": "eng"}, "disposition": {"default": 1}},
            ],
            "format": {"duration": "312.000000"},
        }
        assemble.validate_media_contract(probe)
        probe["streams"][2]["disposition"]["default"] = 0
        with self.assertRaisesRegex(RuntimeError, "default English subtitle"):
            assemble.validate_media_contract(probe)


class AsrDiffTests(unittest.TestCase):
    def test_asr_normalization_allows_numeric_form_but_never_erases_negation(self):
        import qa_final

        expected = "The hypothesis is not refuted at 2.08 ± 0.07 and 95.4%."
        spoken = "The hypothesis is not refuted at two point zero eight plus or minus zero point zero seven and ninety five point four percent."
        self.assertEqual(qa_final.normalize_words(expected), qa_final.normalize_words(spoken))
        altered = "The hypothesis is refuted at two point zero eight plus or minus zero point zero seven and ninety five point four percent."
        self.assertNotEqual(qa_final.normalize_words(expected), qa_final.normalize_words(altered))
        diff = qa_final.word_diff(expected, altered)
        self.assertTrue(any(item["tag"] in {"delete", "replace"} and "not" in item["expected"] for item in diff))

    def test_asr_normalization_handles_only_observed_phonetic_and_symbol_forms(self):
        import qa_final

        pairs = [
            ("Brown–Lee–Rho", "Brown-Li-Rho"),
            ("about 1.5 times", "about one and a half times"),
            ("PSR J0740+6620", "PSR J0740 plus 6620"),
            ("PSR J1913+1102", "PSR J1913 plus 1102"),
            ("2.08 ± 0.07", "2.08 plus minus 0.07"),
            ("Brown–Bethe", "Brown-Bethy"),
            ("Brown–Bethe", "Brown-Bethane"),
            ("Brown–Bethe", "Brown-Betha"),
            ("remeasure", "re-measure"),
            ('joined by "or."', "joined by ore."),
            ("Brown, Lee, and Rho", "Brown, Li, and Rowe"),
            ("Brown–Lee–Rho", "Brownlee Row"),
            ("at least 8 standard deviations", "at least eight standard deviations"),
            ("19.3 ± 0.7%", "19.3% plus or minus 0.7%"),
        ]
        for expected, transcript in pairs:
            with self.subTest(expected=expected, transcript=transcript):
                self.assertEqual(qa_final.normalize_words(expected), qa_final.normalize_words(transcript))


if __name__ == "__main__":
    unittest.main()
