import hashlib
import unittest
from pathlib import Path

import numpy as np
import torch

from committee import (
    GENERATOR_SHA256,
    GEOMETRIC_THRESHOLD,
    CNN_THRESHOLD,
    SmallPlainCNN,
    canonical_parameter_hash,
    committee_state,
    geometric_chi,
    mirror,
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


if __name__ == "__main__":
    unittest.main()
