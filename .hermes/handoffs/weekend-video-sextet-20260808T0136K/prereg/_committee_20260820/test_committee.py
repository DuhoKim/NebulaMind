import hashlib
import json
import tempfile
import unittest
from pathlib import Path
from unittest import mock

import numpy as np
import torch

from committee import (
    GENERATOR_SHA256,
    GEOMETRIC_THRESHOLD,
    CNN_THRESHOLD,
    ContractError,
    MEMBER_B_WEIGHTS_SHA256,
    SmallPlainCNN,
    canonical_parameter_hash,
    committee_state,
    geometric_chi,
    load_frozen_member_b,
    mirror,
    score_manifest,
    synth_sample,
)


class CommitteeContractTests(unittest.TestCase):
    def test_frozen_generator_hash_is_bound(self):
        self.assertEqual(
            GENERATOR_SHA256,
            "89da33ec6260e75e06eadb0f171da4c52f1478b59ff5e543d363dbf56fefcd75",
        )

    def test_thresholds_match_written_spec(self):
        self.assertEqual(GEOMETRIC_THRESHOLD, 0.08)
        self.assertEqual(CNN_THRESHOLD, 0.15)

    def test_mirror_is_byte_exact_involution(self):
        image, _ = synth_sample("HC1H-COMMITTEE-TEST", 7)
        self.assertEqual(mirror(mirror(image)).tobytes(), image.tobytes())

    def test_geometric_member_is_mirror_antisymmetric(self):
        for index in range(12):
            image, _ = synth_sample("HC1H-COMMITTEE-TEST", index)
            chi = geometric_chi(image)
            mirrored_chi = geometric_chi(mirror(image))
            self.assertEqual(mirrored_chi, -chi)

    def test_state_mapping_is_exhaustive(self):
        expected = {
            (1, 1): "AGREE_CONFIDENT",
            (-1, -1): "AGREE_CONFIDENT",
            (1, -1): "DISAGREE",
            (-1, 1): "DISAGREE",
        }
        for pair, state in expected.items():
            self.assertEqual(committee_state(*pair), state)
        for a in (-1, 0, 1):
            for b in (-1, 0, 1):
                if a == 0 or b == 0:
                    self.assertEqual(committee_state(a, b), "LOW_CONFIDENCE")

    def test_cnn_family_is_plain_and_output_shape_is_scalar_per_image(self):
        model = SmallPlainCNN()
        self.assertFalse(any("res" in name.lower() for name, _ in model.named_modules()))
        batch = torch.zeros((3, 1, 128, 128), dtype=torch.float32)
        self.assertEqual(tuple(model(batch).shape), (3,))

    def test_canonical_hash_is_stable_for_same_state(self):
        torch.manual_seed(11)
        first = SmallPlainCNN()
        torch.manual_seed(11)
        second = SmallPlainCNN()
        self.assertEqual(canonical_parameter_hash(first), canonical_parameter_hash(second))
        self.assertEqual(len(canonical_parameter_hash(first)), 64)

    def test_member_b_weight_hash_mismatch_refuses_before_torch_load(self):
        with tempfile.TemporaryDirectory(dir=Path(__file__).resolve().parent) as raw:
            bad = Path(raw) / "bad.pt"
            bad.write_bytes(b"not frozen weights")
            with mock.patch.object(torch, "load") as load:
                with self.assertRaises(ContractError):
                    load_frozen_member_b(bad)
            load.assert_not_called()

    def test_batch_entry_point_scores_tensor_manifest_per_object(self):
        with tempfile.TemporaryDirectory(dir=Path(__file__).resolve().parent) as raw:
            root = Path(raw)
            paths = []
            for index in range(2):
                image, _ = synth_sample("HC1H-COMMITTEE-BATCH-TEST", index)
                path = root / f"object-{index}.f32le"
                path.write_bytes(image.astype("<f4", copy=False).tobytes(order="C"))
                paths.append(path)
            manifest = root / "inputs.json"
            manifest.write_text(json.dumps([str(path) for path in paths]), encoding="utf-8")
            output = root / "committee.jsonl"

            count = score_manifest(manifest, output)

            rows = [json.loads(line) for line in output.read_text().splitlines()]
            self.assertEqual(count, 2)
            self.assertEqual([row["input_path"] for row in rows], [str(path) for path in paths])
            self.assertTrue(all(row["state"] in {"AGREE_CONFIDENT", "DISAGREE", "LOW_CONFIDENCE"} for row in rows))
            self.assertEqual(
                [row["hc1h_state"] for row in rows],
                [
                    {"AGREE_CONFIDENT": "agree-confident", "DISAGREE": "disagree", "LOW_CONFIDENCE": "low-confidence"}[row["state"]]
                    for row in rows
                ],
            )
            self.assertTrue(all(row["member_b_weights_sha256"] == MEMBER_B_WEIGHTS_SHA256 for row in rows))


if __name__ == "__main__":
    unittest.main()
