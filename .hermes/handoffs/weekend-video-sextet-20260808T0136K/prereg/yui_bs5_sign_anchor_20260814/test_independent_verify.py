#!/usr/bin/env python3
"""Focused tests for the independent BS-5 machine-receipt reducer."""
from __future__ import annotations

import hashlib
import unittest

from independent_verify import MASTER_SEED, attempt1_disclosure_valid, reduce_records


class IndependentBs5ReductionTests(unittest.TestCase):
    def test_accepts_the_exact_preserved_numpy_bool_serialization_trace(self) -> None:
        history = {
            "technical_rerun_after_serialization_failure": True,
            "attempt1_failed_before_any_sign_result": True,
        }
        stderr = "TypeError: Object of type bool_ is not JSON serializable\n"
        self.assertTrue(attempt1_disclosure_valid(history, stderr, partial_size=0))

    def test_reduces_sign_winding_mirror_acceptance_and_manifest_without_model(self) -> None:
        source_index = 5_000_000
        seed = (
            int.from_bytes(
                hashlib.sha256(f"{MASTER_SEED}||{source_index}".encode()).digest()[:8],
                "big",
            )
            % (2**63)
        )
        row = {
            "probe_index": 0,
            "source_index": source_index,
            "seed": seed,
            "image_sha256_float32": "11" * 32,
            "mirror_sha256_float32": "22" * 32,
            "analytic_d_pa_d_ln_r": 2.0,
            "measured_ccw_image_d_pa_d_ln_r": 1.9,
            "measured_mirror_d_pa_d_ln_r": -1.9,
            "mirror_involution_byte_exact": True,
            "base_chi_ccw_float32": 6.0,
            "base_chi_mirror_float32": -6.0,
            "estimator_sign_multiplier": 1,
            "estimator_chi_ccw_float32": 6.0,
            "estimator_chi_mirror_float32": -6.0,
            "estimator_sign_pair_pass": True,
            "accepted_at_frozen_tau": True,
        }
        reduced = reduce_records([row], tau=4.4)
        self.assertEqual(reduced["rows"], 1)
        self.assertEqual(reduced["source_indices"], [source_index])
        self.assertEqual(reduced["serialized_seed_matches"], 1)
        self.assertEqual(reduced["ccw_slope_positive"], 1)
        self.assertEqual(reduced["mirror_slope_negative"], 1)
        self.assertEqual(reduced["estimator_sign_pair_pass"], 1)
        self.assertEqual(reduced["estimator_antisymmetry_exact"], 1)
        self.assertEqual(reduced["serialized_predicates_match"], 1)
        self.assertEqual(reduced["accepted_at_tau"], 1)
        expected_manifest = hashlib.sha256(bytes.fromhex("11" * 32) + bytes.fromhex("22" * 32)).hexdigest()
        self.assertEqual(reduced["image_and_mirror_manifest_sha256"], expected_manifest)


if __name__ == "__main__":
    unittest.main()
