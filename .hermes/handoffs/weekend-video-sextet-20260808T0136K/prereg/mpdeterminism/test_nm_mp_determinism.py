#!/usr/bin/env python3
"""Standing test for the multiprocessing scheduling-determinism harness."""
from __future__ import annotations

import hashlib
import json
import subprocess
import sys
import unittest
from pathlib import Path

HERE = Path(__file__).resolve().parent
PREREG = HERE.parent
HARNESS = HERE / "nm_mp_determinism_harness.py"
RECEIPT = HERE / "MP_DETERMINISM_RECEIPT.json"
PINNED_ADAPTER_SHA256 = "267b2a93d2a61f65b281aeb3b04dd874d7add058797b10f593cb3efb4066006f"


class MpDeterminismTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        result = subprocess.run(
            [sys.executable, str(HARNESS)], capture_output=True, text=True
        )
        if result.returncode != 0:
            raise AssertionError(f"harness failed:\n{result.stderr[-3000:]}")
        cls.stdout = json.loads(result.stdout)
        cls.receipt = json.loads(RECEIPT.read_text(encoding="utf-8"))

    def test_all_configurations_byte_identical(self) -> None:
        self.assertEqual(self.receipt["status"], "PASS")
        self.assertEqual(self.receipt["mismatches"], [])
        self.assertEqual(self.receipt["worker_counts_exercised"], [1, 2, 4, 8])
        self.assertEqual(self.receipt["input_order_seeds_exercised"], [101, 202, 303])
        names = [config["name"] for config in self.receipt["configurations"]]
        self.assertIn("w4-completion-reversed", names)
        self.assertEqual(len(names), 7)
        for config in self.receipt["configurations"]:
            self.assertTrue(config["all_objects_byte_identical_to_reference"], config["name"])
        self.assertEqual(len(self.receipt["reference"]), 16)

    def test_adapter_pin_unmoved(self) -> None:
        observed = hashlib.sha256(
            (PREREG / "adapter" / "nm_brick_cutout_adapter.py").read_bytes()
        ).hexdigest()
        self.assertEqual(observed, PINNED_ADAPTER_SHA256)
        self.assertEqual(self.receipt["adapter_sha256_observed"], PINNED_ADAPTER_SHA256)

    def test_nondeterminism_audit_complete(self) -> None:
        sources = {entry["source"]: entry["verdict"] for entry in self.receipt["nondeterminism_audit"]}
        self.assertEqual(
            set(sources),
            {
                "float accumulation order",
                "dict/set iteration order",
                "filesystem enumeration order",
                "per-process receipt fields (pid/hostname/worker index/timestamps/temp paths)",
                "tie-breaks",
            },
        )
        self.assertNotIn("FAIL", "".join(sources.values()))

    def test_receipt_identity_discipline(self) -> None:
        self.assertEqual(
            self.receipt["content_hash_excludes"], ["content_sha256", "recorded_utc"]
        )
        recomputed = hashlib.sha256(
            json.dumps(
                {
                    key: value
                    for key, value in self.receipt.items()
                    if key not in ("content_sha256", "recorded_utc")
                },
                sort_keys=True, separators=(",", ":"),
            ).encode("utf-8")
        ).hexdigest()
        self.assertEqual(recomputed, self.receipt["content_sha256"])
        normalization = self.receipt["comparison_contract"]["receipt_normalization"]
        self.assertEqual(normalization["dropped_fields"], ["manifest_sha256"])

    def test_limits_stated(self) -> None:
        limits = self.receipt["limits"]
        self.assertIn("one machine", limits)
        self.assertIn("270,577", limits)
        self.assertIn("cross-platform", limits)


if __name__ == "__main__":
    unittest.main()
