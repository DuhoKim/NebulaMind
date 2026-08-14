#!/usr/bin/env python3
"""Focused tests for independent R4/R5 raw-record reduction."""
from __future__ import annotations

import unittest

from independent_verify import reduce_records


class IndependentReductionTests(unittest.TestCase):
    def test_reduces_flip_imbalance_and_canary(self) -> None:
        rows = [
            {
                "probe_offset": 0,
                "source_index": 3_000_000,
                "image_sha256_float32": "00" * 32,
                "raw_f_x_float32": 2.0,
                "raw_f_mirror_x_float32": -3.0,
                "dA_raw_contribution": 0.0,
                "r4_abs_identity_violation": 0.02,
                "pure_identity_residual": 0.0,
                "acceptance_mismatch": False,
            },
            {
                "probe_offset": 1,
                "source_index": 3_000_001,
                "image_sha256_float32": "11" * 32,
                "raw_f_x_float32": 2.0,
                "raw_f_mirror_x_float32": 3.0,
                "dA_raw_contribution": 1.0,
                "r4_abs_identity_violation": 0.005,
                "pure_identity_residual": 0.0,
                "acceptance_mismatch": False,
            },
        ]
        reduced = reduce_records(rows)
        self.assertEqual(reduced["rows"], 2)
        self.assertEqual(reduced["dA_raw"], 0.5)
        self.assertEqual(reduced["r4_n_exceeding_0_01"], 1)
        self.assertEqual(reduced["source_indices"], [3_000_000, 3_000_001])


if __name__ == "__main__":
    unittest.main()
