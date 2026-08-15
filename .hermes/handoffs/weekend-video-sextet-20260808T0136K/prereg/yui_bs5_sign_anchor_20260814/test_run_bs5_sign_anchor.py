#!/usr/bin/env python3
"""Contract tests for the BS-5 synthetic absolute-sign anchor runner."""
from __future__ import annotations

import hashlib
import json
import math
import unittest

import numpy as np

from run_bs5_sign_anchor import (
    ESTIMATOR_SIGN_MULTIPLIER,
    MASTER_SEED,
    N_PROBES,
    PROBE_INDEX_START,
    apply_estimator_sign,
    execution_history,
    measure_sky_winding_slope,
    probe_definitions,
    pure_index_mirror,
    sign_pair_fields,
    synthetic_ccw_spiral,
)


class Bs5SignAnchorContractTests(unittest.TestCase):
    def test_probe_schedule_is_fixed_independent_and_in_frozen_support(self) -> None:
        probes = probe_definitions()
        self.assertEqual(N_PROBES, 32)
        self.assertEqual(len(probes), 32)
        self.assertEqual([probe["probe_index"] for probe in probes], list(range(32)))
        self.assertEqual(
            [probe["source_index"] for probe in probes],
            list(range(PROBE_INDEX_START, PROBE_INDEX_START + 32)),
        )
        expected_seeds = [
            int.from_bytes(
                hashlib.sha256(f"{MASTER_SEED}||{index}".encode()).digest()[:8], "big"
            )
            % (2**63)
            for index in range(PROBE_INDEX_START, PROBE_INDEX_START + 32)
        ]
        self.assertEqual([probe["seed"] for probe in probes], expected_seeds)
        self.assertEqual(len(set(expected_seeds)), 32)
        self.assertTrue(all(10.0 <= probe["pitch_deg"] <= 40.0 for probe in probes))
        self.assertTrue(all(0.0 <= probe["inclination_deg"] <= 60.0 for probe in probes))
        self.assertTrue(all(2.0 <= probe["snr"] <= 50.0 for probe in probes))

    def test_rendered_spiral_is_ccw_in_sky_coordinates_and_mirror_is_clockwise(self) -> None:
        image = synthetic_ccw_spiral(
            seed=17,
            pitch_deg=24.0,
            inclination_deg=31.0,
            snr=math.inf,
        )
        slope = measure_sky_winding_slope(image, inclination_deg=31.0)
        mirrored = np.ascontiguousarray(pure_index_mirror(image))
        mirrored_slope = measure_sky_winding_slope(mirrored, inclination_deg=31.0)
        self.assertGreater(slope, 0.0)
        self.assertLess(mirrored_slope, 0.0)
        self.assertEqual(image.shape, (128, 128))
        self.assertEqual(image.dtype, np.float32)
        self.assertTrue(image.flags.c_contiguous)

    def test_production_mirror_is_byte_exact_involution(self) -> None:
        image = synthetic_ccw_spiral(
            seed=19,
            pitch_deg=20.0,
            inclination_deg=15.0,
            snr=50.0,
        )
        restored = pure_index_mirror(pure_index_mirror(image))
        self.assertEqual(restored.tobytes(), image.tobytes())

    def test_estimator_sign_layer_changes_estimator_not_convention(self) -> None:
        self.assertIn(ESTIMATOR_SIGN_MULTIPLIER, (-1, 1))
        self.assertEqual(apply_estimator_sign(np.float32(3.0), 1), np.float32(3.0))
        self.assertEqual(apply_estimator_sign(np.float32(3.0), -1), np.float32(-3.0))
        self.assertEqual(apply_estimator_sign(np.float32(-2.0), -1), np.float32(2.0))

    def test_sign_pair_fields_are_json_serializable_python_scalars(self) -> None:
        fields = sign_pair_fields(np.float32(3.0), np.float32(-3.0), tau=2.0)
        self.assertIs(type(fields["estimator_sign_pair_pass"]), bool)
        self.assertIs(type(fields["accepted_at_frozen_tau"]), bool)
        self.assertTrue(fields["estimator_sign_pair_pass"])
        self.assertTrue(fields["accepted_at_frozen_tau"])
        json.dumps(fields)

    def test_failed_serialization_attempt_is_disclosed_as_pre_result_rerun(self) -> None:
        history = execution_history()
        self.assertTrue(history["technical_rerun_after_serialization_failure"])
        self.assertTrue(history["attempt1_failed_before_any_sign_result"])
        self.assertFalse(history["probe_selection_tuned_or_replaced"])
        self.assertEqual(history["attempt1_error"], "numpy.bool_ was not JSON serializable")


if __name__ == "__main__":
    unittest.main()
