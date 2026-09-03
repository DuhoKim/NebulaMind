#!/usr/bin/env python3
"""Fast contract tests for the V137-H BS-3g parameterization."""
from decimal import Decimal

import numpy as np

import bs3g_producer as producer
import verify_bs3g_receipt as verifier
from receipt_strict import schema_entry_digest


def main():
    old = producer.ruled_values()
    assert old["gamma"] == Decimal("0.25")
    headroom = producer.ruled_values(Decimal("0.10"))
    assert headroom["delta"] == Decimal("0.004")
    assert headroom["grid"][0] == Decimal("-0.10")
    assert headroom["grid"][-1] == Decimal("0.10")
    assert headroom["grid"][headroom["j0"]] == 0

    frozen = {"a_hat": 0.88, "a_lb": 0.86,
              "a_b": np.array([0.88, 0.88, 0.88]),
              "a_lb_b": np.array([0.86, 0.86, 0.86]),
              "cov_a": np.diag([0.0004] * 3)}
    shifted = producer._shifted_calibration(frozen, Decimal("0.95"))
    independently_shifted = verifier.shifted_calibration(frozen, Decimal("0.95"))
    assert shifted["a_hat"] == 0.95 and shifted["a_lb"] == 0.9299999999999999
    for key in frozen:
        np.testing.assert_array_equal(np.asarray(shifted[key]),
                                      np.asarray(independently_shifted[key]))
    assert schema_entry_digest("BS-3g") == (
        "eb8589f5f70656b16dc8ba16e7d78677a0ab0da7b92cb54eddd22fef14e20102")
    nd, seed, _gen, ns, gamma, step, grid, j0, _nperm, a0 = verifier.rules()
    assert (nd, seed, ns, gamma, step, len(grid), j0, a0) == (
        99, 20260830, 50, Decimal("0.10"), Decimal("0.004"), 51, 25,
        Decimal("0.95"))
    print("BS-3g V137-H parameter tests: 12/12 PASS")


if __name__ == "__main__":
    main()
