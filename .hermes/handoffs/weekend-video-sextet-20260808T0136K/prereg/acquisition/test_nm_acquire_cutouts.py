#!/usr/bin/env python3
"""Offline tests for nm_acquire_cutouts.py; synthetic fixtures and mock transport only."""
from __future__ import annotations

import importlib.util
import hashlib
import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

HERE = Path(__file__).resolve().parent
MODULE_PATH = HERE / "nm_acquire_cutouts.py"


def load_module():
    if not MODULE_PATH.is_file():
        raise AssertionError("RED: nm_acquire_cutouts.py is missing")
    spec = importlib.util.spec_from_file_location("nm_acquire_cutouts", MODULE_PATH)
    if spec is None or spec.loader is None:
        raise AssertionError("RED: cannot load nm_acquire_cutouts.py")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def _fits_card(key, value=None):
    if value is None:
        text = key
    else:
        if isinstance(value, bool):
            rendered = "T" if value else "F"
        elif isinstance(value, str):
            rendered = "'" + value + "'"
        else:
            rendered = str(value)
        text = f"{key:<8}= {rendered:>20}"
    return text.ljust(80).encode("ascii")


def synthetic_fits(*, sip=False, parity_flipped=False, corrupt=False):
    scale = 0.0000727777777777778
    cards = [
        _fits_card("SIMPLE", True),
        _fits_card("BITPIX", 8),
        _fits_card("NAXIS", 3),
        _fits_card("NAXIS1", 256),
        _fits_card("NAXIS2", 256),
        _fits_card("NAXIS3", 3),
        _fits_card("WCSAXES", 2),
        _fits_card("CTYPE1", "RA---TAN-SIP" if sip else "RA---TAN"),
        _fits_card("CTYPE2", "DEC--TAN-SIP" if sip else "DEC--TAN"),
        _fits_card("CRPIX1", 128.5),
        _fits_card("CRPIX2", 128.5),
        _fits_card("CRVAL1", 12.5),
        _fits_card("CRVAL2", -3.25),
        _fits_card("CD1_1", scale if parity_flipped else -scale),
        _fits_card("CD1_2", 0.0),
        _fits_card("CD2_1", 0.0),
        _fits_card("CD2_2", scale),
    ]
    if sip:
        cards.extend([_fits_card("A_ORDER", 2), _fits_card("A_2_0", 1e-8)])
    cards.append(_fits_card("END"))
    header = b"".join(cards)
    header += b" " * ((-len(header)) % 2880)
    data = bytes(3 * 256 * 256)
    payload = header + data + bytes((-len(data)) % 2880)
    return payload[:-17] if corrupt else payload


class FrozenSelectionTests(unittest.TestCase):
    def test_frozen_cut_1_through_6_contract_is_exact(self) -> None:
        module = load_module()
        self.assertEqual(
            module.FROZEN_SELECTION_STAGES,
            (
                ("cut_1_primary_mask", "brick_primary = 1 AND maskbits = 0"),
                ("cut_2_extended_positive_flux", "type <> 'PSF' AND flux_r > 0"),
                (
                    "cut_3_photo_z",
                    "LEFT JOIN photo_z ON (ls_id, release, brickid, objid) AND 0 <= z_phot_median < 0.15",
                ),
                ("cut_4_dered_magnitude", "dered_mag_r < 17.7"),
                ("cut_5_size", "shape_r > 1.5"),
                (
                    "cut_6_inclination",
                    "POWER(shape_e1,2) + POWER(shape_e2,2) < 0.1836734693877551",
                ),
            ),
        )

    def test_synthetic_selector_applies_every_frozen_stage_in_order(self) -> None:
        module = load_module()
        self.assertTrue(
            hasattr(module, "evaluate_frozen_selection"),
            "RED: executable synthetic selector is missing",
        )
        accepted = {
            "scope": "SYNTHETIC_ONLY_BUILD",
            "brick_primary": 1,
            "maskbits": 0,
            "type": "EXP",
            "flux_r": 100.0,
            "photo_z_join_exact": True,
            "z_phot_median": 0.10,
            "dered_mag_r": 17.0,
            "shape_r": 2.0,
            "shape_e1": 0.1,
            "shape_e2": 0.1,
        }
        result = module.evaluate_frozen_selection(accepted)
        self.assertTrue(result["accepted"])
        self.assertIsNone(result["failed_stage"])
        self.assertEqual(
            list(result["stage_pass"]),
            [name for name, _ in module.FROZEN_SELECTION_STAGES],
        )

        failures = (
            ("cut_1_primary_mask", {"maskbits": 1}),
            ("cut_2_extended_positive_flux", {"type": "PSF"}),
            ("cut_3_photo_z", {"photo_z_join_exact": False}),
            ("cut_4_dered_magnitude", {"dered_mag_r": 17.7}),
            ("cut_5_size", {"shape_r": 1.5}),
            ("cut_6_inclination", {"shape_e1": 1.0}),
        )
        for expected_stage, override in failures:
            with self.subTest(stage=expected_stage):
                rejected = module.evaluate_frozen_selection({**accepted, **override})
                self.assertFalse(rejected["accepted"])
                self.assertEqual(rejected["failed_stage"], expected_stage)


class DryRunTests(unittest.TestCase):
    def test_dry_run_builds_exact_request_logs_it_and_never_calls_transport(self) -> None:
        module = load_module()
        self.assertTrue(hasattr(module, "SyntheticObject"), "RED: SyntheticObject is missing")
        self.assertTrue(hasattr(module, "run_pipeline"), "RED: run_pipeline is missing")

        class ExplodingTransport:
            calls = 0

            def fetch(self, request):
                self.calls += 1
                raise AssertionError("dry-run called transport")

        transport = ExplodingTransport()
        with tempfile.TemporaryDirectory(prefix="_tmp_nm_acquire_synth_") as tmp:
            output = Path(tmp)
            synthetic = module.SyntheticObject(
                object_key="SYNTH-OBJECT-0001",
                ra_deg=12.5,
                dec_deg=-3.25,
            )

            summary = module.run_pipeline(
                [synthetic], output, transport=transport, dry_run=True
            )

            self.assertEqual(transport.calls, 0)
            self.assertEqual(summary["dry_run_requests"], 1)
            self.assertEqual(summary["issued_requests"], 0)
            self.assertEqual(list(output.rglob("*.fits")), [])
            events = [
                json.loads(line)
                for line in (output / "request_log.jsonl").read_text().splitlines()
            ]
            self.assertEqual(len(events), 1)
            self.assertEqual(events[0]["status"], "DRY_RUN_NOT_ISSUED")
            self.assertEqual(events[0]["previous_event_sha256"], None)
            self.assertEqual(
                events[0]["request"]["url"],
                "https://www.legacysurvey.org/viewer/fits-cutout"
                "?ra=12.50000000&dec=-3.25000000&layer=ls-dr10-south"
                "&pixscale=0.262&bands=grz&size=256",
            )
            self.assertEqual(events[0]["request"]["route"]["layer"], "ls-dr10-south")
            self.assertRegex(events[0]["request_sha256"], r"^[0-9a-f]{64}$")
            self.assertRegex(events[0]["event_sha256"], r"^[0-9a-f]{64}$")


class MockResponseTests(unittest.TestCase):
    def test_valid_mock_fits_is_hash_checked_parity_checked_and_custodied(self) -> None:
        module = load_module()
        self.assertTrue(hasattr(module, "MockTransport"), "RED: MockTransport is missing")
        payload = synthetic_fits()
        transport = module.MockTransport({"SYNTH-OBJECT-0001": payload})
        with tempfile.TemporaryDirectory(prefix="_tmp_nm_acquire_synth_") as tmp:
            output = Path(tmp)
            summary = module.run_pipeline(
                [module.SyntheticObject("SYNTH-OBJECT-0001", 12.5, -3.25)],
                output,
                transport=transport,
                dry_run=False,
            )

            self.assertEqual(len(transport.calls), 1)
            self.assertEqual(summary["completed"], 1)
            self.assertEqual(summary["failed"], 0)
            cutout = output / "cutouts" / "SYNTH-OBJECT-0001.fits"
            self.assertEqual(cutout.read_bytes(), payload)
            receipt = json.loads(
                (output / "receipts" / "SYNTH-OBJECT-0001.json").read_text()
            )
            expected_hash = hashlib.sha256(payload).hexdigest()
            self.assertEqual(receipt["response_sha256"], expected_hash)
            self.assertEqual(receipt["output_sha256"], expected_hash)
            self.assertEqual(receipt["fits_shape"], [3, 256, 256])
            self.assertEqual(receipt["distortion_families_detected"], [])
            self.assertEqual(receipt["parity"]["combined_determinant_sign"], -1)
            self.assertTrue(receipt["parity"]["east_left"])
            self.assertTrue(receipt["parity"]["north_up"])
            self.assertEqual(
                receipt["parity"]["validator_sha256"],
                "7bf0201917e7722ee9545c9c11b6cc1cbdec345504e3f29fa1aeb01e58edaa55",
            )

    def test_corrupt_sip_and_parity_flipped_mock_responses_fail_closed(self) -> None:
        module = load_module()
        cases = (
            ("SYNTH-CORRUPT", synthetic_fits(corrupt=True), "FAILED_FITS_INTEGRITY", []),
            ("SYNTH-SIP", synthetic_fits(sip=True), "REJECTED_DISTORTION", ["SIP"]),
            ("SYNTH-FLIPPED", synthetic_fits(parity_flipped=True), "REJECTED_PARITY", []),
        )
        for key, payload, expected_status, expected_families in cases:
            with self.subTest(key=key), tempfile.TemporaryDirectory(
                prefix="_tmp_nm_acquire_synth_"
            ) as tmp:
                output = Path(tmp)
                summary = module.run_pipeline(
                    [module.SyntheticObject(key, 12.5, -3.25)],
                    output,
                    transport=module.MockTransport({key: payload}),
                    dry_run=False,
                )

                self.assertEqual(summary["completed"], 0)
                self.assertEqual(summary["failed"], 1)
                self.assertEqual(list((output / "cutouts").glob("*.fits")), [])
                self.assertEqual(list((output / "staging").glob("*")), [])
                receipt = json.loads((output / "receipts" / f"{key}.json").read_text())
                self.assertEqual(receipt["status"], expected_status)
                self.assertEqual(receipt["response_sha256"], hashlib.sha256(payload).hexdigest())
                self.assertEqual(
                    receipt["distortion_families_detected"], expected_families
                )
                events = [
                    json.loads(line)
                    for line in (output / "request_log.jsonl").read_text().splitlines()
                ]
                self.assertEqual(events[-1]["status"], expected_status)


class ResumeTests(unittest.TestCase):
    def test_completed_object_is_checksum_verified_and_not_refetched(self) -> None:
        module = load_module()
        key = "SYNTH-RESUME-COMPLETE"
        payload = synthetic_fits()
        with tempfile.TemporaryDirectory(prefix="_tmp_nm_acquire_synth_") as tmp:
            output = Path(tmp)
            module.run_pipeline(
                [module.SyntheticObject(key, 12.5, -3.25)],
                output,
                transport=module.MockTransport({key: payload}),
                dry_run=False,
            )
            receipt_path = output / "receipts" / f"{key}.json"
            original_receipt_hash = hashlib.sha256(receipt_path.read_bytes()).hexdigest()
            second_transport = module.MockTransport({key: payload})

            summary = module.run_pipeline(
                [module.SyntheticObject(key, 12.5, -3.25)],
                output,
                transport=second_transport,
                dry_run=False,
            )

            self.assertEqual(second_transport.calls, [])
            self.assertEqual(summary["resumed_complete"], 1)
            self.assertEqual(
                hashlib.sha256(receipt_path.read_bytes()).hexdigest(),
                original_receipt_hash,
            )
            events = [
                json.loads(line)
                for line in (output / "request_log.jsonl").read_text().splitlines()
            ]
            self.assertEqual(events[-1]["status"], "RESUME_COMPLETE_NOT_REFETCHED")

    def test_response_custodied_interrupt_resumes_without_refetch(self) -> None:
        module = load_module()
        key = "SYNTH-RESUME-STAGED"
        payload = synthetic_fits()
        with tempfile.TemporaryDirectory(prefix="_tmp_nm_acquire_synth_") as tmp:
            output = Path(tmp)
            first_transport = module.MockTransport({key: payload})
            self.assertTrue(
                hasattr(first_transport, "interrupt_after_custody_keys"),
                "RED: mock custody interruption hook is missing",
            )
            first_transport.interrupt_after_custody_keys.add(key)
            with self.assertRaises(KeyboardInterrupt):
                module.run_pipeline(
                    [module.SyntheticObject(key, 12.5, -3.25)],
                    output,
                    transport=first_transport,
                    dry_run=False,
                )
            state = json.loads((output / "state.json").read_text())
            self.assertEqual(state["objects"][key]["status"], "RESPONSE_CUSTODIED")
            second_transport = module.MockTransport({key: payload})

            summary = module.run_pipeline(
                [module.SyntheticObject(key, 12.5, -3.25)],
                output,
                transport=second_transport,
                dry_run=False,
            )

            self.assertEqual(second_transport.calls, [])
            self.assertEqual(summary["resumed_custodied"], 1)
            self.assertEqual(summary["completed"], 1)
            self.assertEqual(
                (output / "cutouts" / f"{key}.fits").read_bytes(), payload
            )
            self.assertEqual(list((output / "staging").glob("*")), [])
            statuses = [
                json.loads(line)["status"]
                for line in (output / "request_log.jsonl").read_text().splitlines()
            ]
            self.assertIn("RESUME_RESPONSE_CUSTODIED", statuses)

    def test_in_flight_interrupt_remains_explicit_and_is_not_refetched(self) -> None:
        module = load_module()
        key = "SYNTH-RESUME-UNCERTAIN"
        payload = synthetic_fits()
        with tempfile.TemporaryDirectory(prefix="_tmp_nm_acquire_synth_") as tmp:
            output = Path(tmp)
            first_transport = module.MockTransport({key: payload})
            self.assertTrue(
                hasattr(first_transport, "interrupt_before_response_keys"),
                "RED: mock pre-response interruption hook is missing",
            )
            first_transport.interrupt_before_response_keys.add(key)
            with self.assertRaises(KeyboardInterrupt):
                module.run_pipeline(
                    [module.SyntheticObject(key, 12.5, -3.25)],
                    output,
                    transport=first_transport,
                    dry_run=False,
                )
            state = json.loads((output / "state.json").read_text())
            self.assertEqual(state["objects"][key]["status"], "IN_FLIGHT_UNCERTAIN")
            second_transport = module.MockTransport({key: payload})

            summary = module.run_pipeline(
                [module.SyntheticObject(key, 12.5, -3.25)],
                output,
                transport=second_transport,
                dry_run=False,
            )

            self.assertEqual(second_transport.calls, [])
            self.assertEqual(summary["uncertain"], 1)
            self.assertFalse((output / "cutouts" / f"{key}.fits").exists())
            state = json.loads((output / "state.json").read_text())
            self.assertEqual(state["objects"][key]["status"], "IN_FLIGHT_UNCERTAIN")
            events = [
                json.loads(line)
                for line in (output / "request_log.jsonl").read_text().splitlines()
            ]
            self.assertEqual(
                events[-1]["status"], "RESUME_IN_FLIGHT_UNCERTAIN_NOT_REFETCHED"
            )

    def test_terminal_failure_is_counted_logged_and_not_refetched(self) -> None:
        module = load_module()
        key = "SYNTH-RESUME-FAILED"
        payload = synthetic_fits(corrupt=True)
        with tempfile.TemporaryDirectory(prefix="_tmp_nm_acquire_synth_") as tmp:
            output = Path(tmp)
            module.run_pipeline(
                [module.SyntheticObject(key, 12.5, -3.25)],
                output,
                transport=module.MockTransport({key: payload}),
                dry_run=False,
            )
            second_transport = module.MockTransport({key: payload})

            summary = module.run_pipeline(
                [module.SyntheticObject(key, 12.5, -3.25)],
                output,
                transport=second_transport,
                dry_run=False,
            )

            self.assertEqual(second_transport.calls, [])
            self.assertEqual(summary["failed"], 1)
            self.assertEqual(summary["skipped"], 1)
            events = [
                json.loads(line)
                for line in (output / "request_log.jsonl").read_text().splitlines()
            ]
            self.assertEqual(
                events[-1]["status"], "RESUME_TERMINAL_FAILURE_NOT_REFETCHED"
            )


class RatePolicyTests(unittest.TestCase):
    def test_mock_requests_are_serial_and_at_least_five_seconds_apart(self) -> None:
        module = load_module()
        self.assertTrue(hasattr(module, "RateLimiter"), "RED: RateLimiter is missing")

        class FakeClock:
            def __init__(self):
                self.now = 100.0
                self.sleeps = []

            def monotonic(self):
                return self.now

            def sleep(self, seconds):
                self.sleeps.append(seconds)
                self.now += seconds

        fake = FakeClock()
        limiter = module.RateLimiter(clock=fake.monotonic, sleeper=fake.sleep)
        keys = ["SYNTH-RATE-0001", "SYNTH-RATE-0002"]
        transport = module.MockTransport({key: synthetic_fits() for key in keys})
        with tempfile.TemporaryDirectory(prefix="_tmp_nm_acquire_synth_") as tmp:
            summary = module.run_pipeline(
                [
                    module.SyntheticObject(keys[0], 12.5, -3.25),
                    module.SyntheticObject(keys[1], 13.5, -2.25),
                ],
                Path(tmp),
                transport=transport,
                dry_run=False,
                rate_limiter=limiter,
            )

        self.assertEqual(len(transport.calls), 2)
        self.assertEqual(fake.sleeps, [5.0])
        self.assertEqual(limiter.request_times, [100.0, 105.0])
        self.assertEqual(summary["completed"], 2)
        self.assertEqual(summary["rate_policy"]["max_concurrent_requests"], 1)
        self.assertEqual(summary["rate_policy"]["min_interval_seconds"], 5.0)

    def test_retryable_mock_failure_uses_frozen_backoff_then_completes(self) -> None:
        module = load_module()
        self.assertTrue(
            hasattr(module, "RetryableTransportError"),
            "RED: RetryableTransportError is missing",
        )

        class FakeClock:
            def __init__(self):
                self.now = 200.0
                self.sleeps = []

            def monotonic(self):
                return self.now

            def sleep(self, seconds):
                self.sleeps.append(seconds)
                self.now += seconds

        fake = FakeClock()
        limiter = module.RateLimiter(clock=fake.monotonic, sleeper=fake.sleep)
        key = "SYNTH-BACKOFF-0001"
        transport = module.MockTransport(
            {
                key: [
                    module.RetryableTransportError("synthetic service pressure"),
                    synthetic_fits(),
                ]
            }
        )
        with tempfile.TemporaryDirectory(prefix="_tmp_nm_acquire_synth_") as tmp:
            output = Path(tmp)
            summary = module.run_pipeline(
                [module.SyntheticObject(key, 12.5, -3.25)],
                output,
                transport=transport,
                dry_run=False,
                rate_limiter=limiter,
            )
            statuses = [
                json.loads(line)["status"]
                for line in (output / "request_log.jsonl").read_text().splitlines()
            ]

        self.assertEqual(len(transport.calls), 2)
        self.assertEqual(fake.sleeps, [30.0])
        self.assertEqual(summary["transient_retries"], 1)
        self.assertEqual(summary["completed"], 1)
        self.assertIn("RETRYABLE_TRANSPORT_ERROR_BACKOFF", statuses)


class BuildOnlyBoundaryTests(unittest.TestCase):
    def test_cli_only_exposes_synthetic_dry_run(self) -> None:
        with tempfile.TemporaryDirectory(prefix="_tmp_nm_acquire_synth_") as tmp:
            output = Path(tmp) / "dry"
            result = subprocess.run(
                [
                    sys.executable,
                    str(MODULE_PATH),
                    "--dry-run",
                    "--output-dir",
                    str(output),
                ],
                text=True,
                capture_output=True,
                check=False,
            )
            self.assertEqual(result.returncode, 0, result.stderr)
            self.assertTrue(result.stdout.strip(), "RED: CLI did not emit a summary")
            summary = json.loads(result.stdout)
            self.assertEqual(summary["dry_run_requests"], 1)
            self.assertEqual(summary["issued_requests"], 0)
            self.assertEqual(list(output.rglob("*.fits")), [])

            refused = subprocess.run(
                [sys.executable, str(MODULE_PATH), "--output-dir", str(Path(tmp) / "no")],
                text=True,
                capture_output=True,
                check=False,
            )
            self.assertNotEqual(refused.returncode, 0)
            self.assertIn("BUILD_ONLY_STOP", refused.stderr)

    def test_real_identifiers_and_non_mock_transport_are_rejected_before_fetch(self) -> None:
        module = load_module()
        with self.assertRaisesRegex(ValueError, "BUILD_ONLY_STOP"):
            module.SyntheticObject("REAL-OBJECT-1", 12.5, -3.25)
        with self.assertRaisesRegex(ValueError, "BUILD_ONLY_STOP"):
            module.SyntheticObject("SYNTH-../ESCAPE", 12.5, -3.25)

        class PretendRealTransport:
            calls = 0

            def fetch(self, request):
                self.calls += 1
                raise AssertionError("non-mock transport called")

        transport = PretendRealTransport()
        with tempfile.TemporaryDirectory(prefix="_tmp_nm_acquire_synth_") as tmp:
            with self.assertRaisesRegex(RuntimeError, "BUILD_ONLY_STOP"):
                module.run_pipeline(
                    [module.SyntheticObject("SYNTH-ONLY-MOCK", 12.5, -3.25)],
                    Path(tmp),
                    transport=transport,
                    dry_run=False,
                )
        self.assertEqual(transport.calls, 0)

    def test_tampered_append_only_log_refuses_next_event(self) -> None:
        module = load_module()
        with tempfile.TemporaryDirectory(prefix="_tmp_nm_acquire_synth_") as tmp:
            output = Path(tmp)
            item = module.SyntheticObject("SYNTH-LOG-TAMPER", 12.5, -3.25)
            transport = module.MockTransport({})
            module.run_pipeline([item], output, transport=transport, dry_run=True)
            log_path = output / "request_log.jsonl"
            event = json.loads(log_path.read_text())
            event["status"] = "TAMPERED"
            log_path.write_text(json.dumps(event) + "\n")

            with self.assertRaisesRegex(RuntimeError, "log hash mismatch"):
                module.run_pipeline([item], output, transport=transport, dry_run=True)

            self.assertEqual(transport.calls, [])


if __name__ == "__main__":
    unittest.main()
