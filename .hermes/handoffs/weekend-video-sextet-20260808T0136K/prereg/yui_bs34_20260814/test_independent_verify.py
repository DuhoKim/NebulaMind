#!/usr/bin/env python3
"""Focused test for independent BS-3/BS-4 record reduction."""
from __future__ import annotations

import unittest

from independent_verify import reduce_records


class IndependentReductionTests(unittest.TestCase):
    def test_reduces_identity_abstention_and_flip_without_model_imports(self) -> None:
        row = {
            "probe_offset": 0,
            "source_index": 3_000_000,
            "image_sha256_float32": "00" * 32,
            "R1_mirror_involution_byte_exact": True,
            "primary_R2_value_exact": True,
            "primary_R2_bit_exact": True,
            "primary_chi_x_float32": 2.0,
            "primary_chi_mirror_float32": -2.0,
            "primary_chi_mirror_bits": "0xc0000000",
            "primary_identity_residual": 0.0,
            "secondary_R2_value_exact": True,
            "secondary_R2_bit_exact": True,
            "secondary_chi_mirror_float32": -6.0,
            "secondary_chi_mirror_bits": "0xc0c00000",
            "secondary_identity_residual": 0.0,
            "secondary_raw_w_x_float32": 2.0,
            "secondary_raw_w_mirror_float32": -3.0,
            "secondary_dA_raw_contribution": 0.0,
            "secondary_chi_x_float32": 6.0,
            "secondary_accepted_at_frozen_tau": True,
            "secondary_R4_chi_bad_input_float32": -5.5,
            "secondary_R4_abs_identity_violation": 0.5,
            "snr": 3.0,
        }
        reduced = reduce_records([row], secondary_tau=5.916292121766702)
        self.assertEqual(reduced["rows"], 1)
        self.assertEqual(reduced["primary_R2_bit_exact"], 1)
        self.assertEqual(reduced["secondary_R2_bit_exact"], 1)
        self.assertEqual(reduced["secondary_accepted"], 1)
        self.assertEqual(reduced["secondary_dA_raw"], 0.0)
        self.assertEqual(reduced["secondary_R4_n_exceeding_0_01"], 1)


if __name__ == "__main__":
    unittest.main()
