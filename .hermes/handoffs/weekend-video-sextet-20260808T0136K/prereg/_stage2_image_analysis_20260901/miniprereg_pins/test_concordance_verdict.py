#!/usr/bin/env python3
"""Fixture tests for concordance_verdict.py; standard library only."""

import copy
import math
import unittest

import concordance_verdict as cv


def document(n=3000, map_same=True, est_same=True):
    rows = []
    for objid in range(n):
        split = cv._split(objid)
        same = map_same if split == "map" else est_same
        rows.append({"gz1_objid": objid, "gz_label": 1,
                     "machine_sign": 1 if same else -1})
    return {
        "blind_violation": False,
        "completeness_pass": True,
        "data_integrity_pass": True,
        "instrument_integrity_pass": True,
        "wrong_parity": False,
        "absolute_anchor_pass": True,
        "measurement_pass": True,
        "deterministic_pass": True,
        "objects": rows,
    }


class VerdictFixtures(unittest.TestCase):
    def test_undetermined_sign(self):
        doc = document()
        flip = False
        for row in doc["objects"]:
            if cv._split(row["gz1_objid"]) == "map":
                row["machine_sign"] = 1 if flip else -1
                flip = not flip
        self.assertEqual(cv.verdict(doc), "UNDETERMINED-SIGN")

    def test_insufficient_sample(self):
        self.assertEqual(cv.verdict(document(20)), "INSUFFICIENT-SAMPLE")

    def test_ordinary_concordant_band(self):
        self.assertEqual(cv.verdict(document()), "CONCORDANT")

    def test_nan_fails_closed(self):
        doc = document()
        doc["unexpected_nonfinite"] = math.nan
        self.assertEqual(cv.verdict(doc), "DATA-INTEGRITY-FAIL")


if __name__ == "__main__":
    unittest.main()
