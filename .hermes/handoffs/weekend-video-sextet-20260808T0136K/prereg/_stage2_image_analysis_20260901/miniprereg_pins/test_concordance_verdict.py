#!/usr/bin/env python3
"""Fixture tests for concordance_verdict.py; standard library only."""

import copy
import io
import json
import math
import unittest
from contextlib import redirect_stdout
from unittest import mock

import concordance_verdict as cv


def document(n=3000, map_same=True, est_same=True):
    rows = []
    for objid in range(n):
        split = cv._split(objid)
        same = map_same if split == "map" else est_same
        rows.append({"gz1_objid": objid, "gz_label": 1,
                     "machine_sign": 1 if same else -1})
    doc = {
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
    for key in cv.DIGEST_KEYS:
        doc[key] = "a" * 64
    return doc


class VerdictFixtures(unittest.TestCase):
    def assert_verdict(self, doc, expected):
        self.assertEqual(cv.verdict(doc)["verdict"], expected)

    def test_blind_violation(self):
        doc = document()
        doc["blind_violation"] = True
        self.assert_verdict(doc, "VOID-BLIND-VIOLATION")

    def test_completeness_failure(self):
        doc = document()
        doc["completeness_pass"] = False
        self.assert_verdict(doc, "COMPLETENESS-FAIL")

    def test_data_integrity_failure(self):
        doc = document()
        doc["data_integrity_pass"] = False
        self.assert_verdict(doc, "DATA-INTEGRITY-FAIL")

    def test_instrument_integrity_failure(self):
        doc = document()
        doc["instrument_integrity_pass"] = False
        self.assert_verdict(doc, "INSTRUMENT-INTEGRITY-FAIL")

    def test_wrong_parity(self):
        doc = document()
        doc["wrong_parity"] = True
        self.assert_verdict(doc, "WRONG-PARITY-REFUSAL")

    def test_absolute_anchor_failure(self):
        doc = document()
        doc["absolute_anchor_pass"] = False
        self.assert_verdict(doc, "ABSOLUTE-ANCHOR-FAIL")

    def test_measurement_failure(self):
        doc = document()
        doc["measurement_pass"] = False
        self.assert_verdict(doc, "MEASUREMENT-FAIL")

    def test_nondeterministic_instrument(self):
        doc = document()
        doc["deterministic_pass"] = False
        self.assert_verdict(doc, "NONDETERMINISTIC-INSTRUMENT")

    def test_undetermined_sign(self):
        doc = document()
        flip = False
        for row in doc["objects"]:
            if cv._split(row["gz1_objid"]) == "map":
                row["machine_sign"] = 1 if flip else -1
                flip = not flip
        self.assert_verdict(doc, "UNDETERMINED-SIGN")

    def test_insufficient_sample(self):
        self.assert_verdict(document(20), "INSUFFICIENT-SAMPLE")

    def test_ordinary_concordant_band(self):
        block = cv.verdict(document())
        self.assertEqual(block["verdict"], "CONCORDANT")
        self.assertEqual(block["k_agree"], block["n_est"])
        self.assertEqual(block["p_agree"], 1.0)

    def test_nan_fails_closed(self):
        doc = document()
        doc["unexpected_nonfinite"] = math.nan
        self.assert_verdict(doc, "DATA-INTEGRITY-FAIL")

    def test_stdout_json_has_exact_closed_key_set(self):
        payload = json.dumps(document())
        stdout = io.StringIO()
        with mock.patch("sys.argv", ["concordance_verdict.py"]), \
             mock.patch("sys.stdin", io.StringIO(payload)), \
             redirect_stdout(stdout):
            cv.main()
        output = json.loads(stdout.getvalue())
        self.assertEqual(set(output), cv.VERDICT_KEYS)
        self.assertEqual(stdout.getvalue().count("\n"), 1)


if __name__ == "__main__":
    unittest.main()
