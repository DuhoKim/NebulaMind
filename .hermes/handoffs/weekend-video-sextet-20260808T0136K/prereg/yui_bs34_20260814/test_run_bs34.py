#!/usr/bin/env python3
"""Focused contract tests for the combined BS-3/BS-4 synthetic runner."""
from __future__ import annotations

import unittest

import numpy as np

from run_bs34 import (
    N_IDENTITY_PROBES,
    PROBE_SOURCE_INDEX_START,
    identity_source_indices,
    ordered_accept,
    secondary_chi_from_raw,
    sign_pair_contribution,
)


class Bs34ContractTests(unittest.TestCase):
    def test_identity_source_indices_are_the_promised_thousand_probe_extension(self) -> None:
        indices = identity_source_indices()
        self.assertEqual(N_IDENTITY_PROBES, 1000)
        self.assertEqual(len(indices), 1000)
        self.assertEqual(indices[0], PROBE_SOURCE_INDEX_START)
        self.assertEqual(indices[-1], PROBE_SOURCE_INDEX_START + 999)
        self.assertEqual(indices, list(range(3_000_000, 3_001_000)))

    def test_acceptance_is_ordered_and_strict_at_tau(self) -> None:
        tau = 5.0
        self.assertFalse(ordered_accept(np.float32(0.0), tau))
        self.assertFalse(ordered_accept(np.float32(-0.0), tau))
        self.assertFalse(ordered_accept(np.float32(5.0), tau))
        self.assertTrue(ordered_accept(np.float32(5.000001), tau))

    def test_secondary_chi_uses_float32_raw_outputs_and_float32_subtraction(self) -> None:
        observed = secondary_chi_from_raw(10.0, 2.0)
        self.assertIsInstance(observed, np.float32)
        self.assertEqual(observed, np.float32(4.0))

    def test_raw_flip_contribution_uses_both_signs_without_tuning(self) -> None:
        self.assertEqual(sign_pair_contribution(2.0, -4.0), 0.0)
        self.assertEqual(sign_pair_contribution(2.0, 4.0), 1.0)
        self.assertEqual(sign_pair_contribution(-2.0, -4.0), -1.0)


if __name__ == "__main__":
    unittest.main()
