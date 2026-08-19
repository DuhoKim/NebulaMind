import hashlib
import importlib.util
import json
import tempfile
import unittest
from unittest import mock
from datetime import datetime
from pathlib import Path

MODULE_PATH = Path(__file__).parents[1] / "nm_image_transfer.py"
spec = importlib.util.spec_from_file_location("nm_image_transfer", MODULE_PATH)
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)


class FakeClock:
    def __init__(self):
        self.value = 0.0
        self.sleeps = []

    def monotonic(self):
        return self.value

    def sleep(self, seconds):
        self.sleeps.append(seconds)
        self.value += seconds


class ImageTransferTests(unittest.TestCase):
    def make_record(self, brick, payload):
        filename = f"legacysurvey-{brick}-image-r.fits.fz"
        return {
            "release": module.RELEASE,
            "brickname": brick,
            "aaa": brick[:3],
            "product": "image-r",
            "coverage_class": "required",
            "source_url": module.image_url(brick, filename),
            "destination_relative_path": f"coadd/{brick[:3]}/{brick}/{filename}",
            "survey_sha256": hashlib.sha256(payload).hexdigest(),
            "checksum_source": {"url": "fixture://checksum", "bytes": 1, "sha256": "0" * 64},
            "reason": "working-set intersecting source",
            "working_set_sha256": "1" * 64,
            "private_object_ids_or_hash": {"working_set_sha256": "1" * 64},
            "manifest_format_version": module.MANIFEST_FORMAT_VERSION,
            "manifest_created_utc": "2026-08-19T00:00:00Z",
        }

    def test_manifest_is_derived_from_exact_harvest_listing(self):
        with tempfile.TemporaryDirectory() as td:
            root = Path(td)
            checksum_root = root / "checksums"
            (checksum_root / "123").mkdir(parents=True)
            brick = "1234m567"
            filename = f"legacysurvey-{brick}-image-r.fits.fz"
            digest = "a" * 64
            checksum_bytes = f"{digest}  {filename}\n".encode()
            (checksum_root / "123" / f"{brick}.sha256sum").write_bytes(checksum_bytes)
            harvest_receipts = root / "receipts.jsonl"
            harvest_receipts.write_text(json.dumps({
                "brickname": brick,
                "outcome": "OK_CONFIRMED",
                "image_r_listed": True,
                "url": "https://portal.nersc.gov/checksum",
                "bytes_received": len(checksum_bytes),
                "sha256_of_checksum_file": hashlib.sha256(checksum_bytes).hexdigest(),
            }) + "\n")
            working_set = root / "working.csv"
            working_set.write_text("brickname,brickid,coverage_class_exact_indicator\n1234m567,1,required\n")

            records = module.build_manifest_records(
                working_set, checksum_root, harvest_receipts, expected_count=1
            )

            self.assertEqual(len(records), 1)
            self.assertEqual(records[0]["survey_sha256"], digest)
            self.assertEqual(
                records[0]["source_url"],
                "https://portal.nersc.gov/cfs/cosmo/data/legacysurvey/dr10/south/coadd/123/1234m567/legacysurvey-1234m567-image-r.fits.fz",
            )
            self.assertNotIn("*", records[0]["source_url"])

    def test_corrupt_digest_is_quarantined_and_blocks_campaign(self):
        with tempfile.TemporaryDirectory() as td:
            root = Path(td)
            expected = b"expected"
            record = self.make_record("1234m567", expected)
            transport = module.MockTransport({record["source_url"]: b"corrupt"})
            runner = module.TransferRunner(
                root,
                transport,
                approved_byte_ceiling=10_000,
                enforce_window=False,
                sleeper=lambda _: None,
            )

            with self.assertRaises(module.CampaignBlocked):
                runner.run([record])

            self.assertTrue((root / "BLOCK_EVENT.json").exists())
            event = json.loads((root / "BLOCK_EVENT.json").read_text())
            self.assertEqual(event["reason"], "SHA256_MISMATCH")
            quarantined = list((root / "quarantine").iterdir())
            self.assertEqual(len(quarantined), 1)
            self.assertEqual(quarantined[0].read_bytes(), b"corrupt")
            self.assertFalse((root / "staging" / record["destination_relative_path"]).exists())

    def test_receipted_file_is_reverified_and_never_refetched(self):
        with tempfile.TemporaryDirectory() as td:
            root = Path(td)
            payload = b"fits fixture"
            record = self.make_record("1234m567", payload)
            first_transport = module.MockTransport({record["source_url"]: payload})
            module.TransferRunner(
                root,
                first_transport,
                approved_byte_ceiling=10_000,
                enforce_window=False,
                sleeper=lambda _: None,
            ).run([record])
            self.assertEqual(len(first_transport.calls), 1)

            second_transport = module.MockTransport({})
            result = module.TransferRunner(
                root,
                second_transport,
                approved_byte_ceiling=10_000,
                enforce_window=False,
                sleeper=lambda _: None,
            ).run([record])

            self.assertEqual(second_transport.calls, [])
            self.assertEqual(result["accepted"], 1)
            receipt_lines = (root / "receipts.jsonl").read_text().splitlines()
            self.assertEqual(len(receipt_lines), 1)

    def test_accepted_file_tamper_blocks_resume_without_fetch(self):
        with tempfile.TemporaryDirectory() as td:
            root = Path(td)
            payload = b"fits fixture"
            record = self.make_record("1234m567", payload)
            module.TransferRunner(
                root,
                module.MockTransport({record["source_url"]: payload}),
                approved_byte_ceiling=10_000,
                enforce_window=False,
                sleeper=lambda _: None,
            ).run([record])
            accepted = root / "staging" / record["destination_relative_path"]
            accepted.write_bytes(b"tampered")
            transport = module.MockTransport({record["source_url"]: payload})

            with self.assertRaises(module.CampaignBlocked):
                module.TransferRunner(
                    root,
                    transport,
                    approved_byte_ceiling=10_000,
                    enforce_window=False,
                    sleeper=lambda _: None,
                ).run([record])

            self.assertEqual(transport.calls, [])
            event = json.loads((root / "BLOCK_EVENT.json").read_text())
            self.assertEqual(event["reason"], "RECEIPTED_FILE_DIGEST_MISMATCH")

    def test_stop_on_first_403_without_retry(self):
        with tempfile.TemporaryDirectory() as td:
            root = Path(td)
            record = self.make_record("1234m567", b"expected")
            transport = module.MockTransport({
                record["source_url"]: module.TransportResult(
                    status=403,
                    headers={"content-length": "7"},
                    bytes_received=7,
                    curl_returncode=0,
                )
            })
            runner = module.TransferRunner(
                root,
                transport,
                approved_byte_ceiling=10_000,
                enforce_window=False,
                sleeper=lambda _: None,
            )

            with self.assertRaises(module.CampaignBlocked):
                runner.run([record])

            self.assertEqual(len(transport.calls), 1)
            self.assertEqual(json.loads((root / "BLOCK_EVENT.json").read_text())["reason"], "HTTP_403")

    def test_rate_limiter_enforces_two_second_request_start_floor(self):
        clock = FakeClock()
        limiter = module.RateLimiter(clock=clock.monotonic, sleeper=clock.sleep)
        limiter.before_request()
        clock.value += 0.5
        limiter.before_request()
        self.assertEqual(clock.sleeps, [1.5])
        self.assertEqual(limiter.request_times, [0.0, 2.0])

    def test_window_rule_matches_frozen_pacific_hours(self):
        pacific = module.PACIFIC
        self.assertTrue(module.in_window(datetime(2026, 8, 19, 21, tzinfo=pacific)))
        self.assertTrue(module.in_window(datetime(2026, 8, 20, 7, 59, tzinfo=pacific)))
        self.assertFalse(module.in_window(datetime(2026, 8, 20, 8, 0, tzinfo=pacific)))
        self.assertTrue(module.in_window(datetime(2026, 8, 22, 12, tzinfo=pacific)))
        self.assertEqual(
            module.seconds_until_window_close(datetime(2026, 8, 23, 12, tzinfo=pacific)),
            20 * 60 * 60,
        )

    def test_curl_transport_command_is_full_get_and_bandwidth_limited(self):
        transport = module.CurlTransport()
        command = transport.command_for(
            "https://portal.nersc.gov/cfs/cosmo/data/legacysurvey/dr10/south/coadd/123/1234m567/legacysurvey-1234m567-image-r.fits.fz",
            Path("out.part"),
            Path("headers.txt"),
            Path("metadata.json"),
        )
        joined = " ".join(command)
        self.assertEqual(command[1], "--disable")
        self.assertIn("--limit-rate 25000000", joined)
        self.assertIn("--max-filesize", command)
        self.assertNotIn("--range", command)
        self.assertNotIn("-r", command)
        self.assertNotIn("--remote-name-all", command)
        self.assertNotIn("--head", command)
        self.assertNotIn("-I", command)

    def test_disk_preflight_fails_closed(self):
        result = module.disk_preflight(Path(tempfile.gettempdir()), required_bytes=10**30)
        self.assertFalse(result["pass"])
        self.assertLess(result["available_bytes"], result["required_bytes"])

    def test_run_refuses_before_manifest_read_without_exact_execution_ack(self):
        with self.assertRaisesRegex(ValueError, "execution acknowledgement missing"):
            module.main([
                "run",
                "--manifest", "/does/not/exist",
                "--manifest-sha256", "0" * 64,
                "--approval-file", "/does/not/exist",
                "--approval-sha256", "0" * 64,
                "--destination", "/does/not/exist",
                "--approved-byte-ceiling", "1",
                "--execute-gated-transfer", "NOT_AUTHORIZED",
            ])

    def test_extra_destination_file_blocks_before_fetch(self):
        with tempfile.TemporaryDirectory() as td:
            root = Path(td)
            record = self.make_record("1234m567", b"expected")
            (root / "staging").mkdir()
            (root / "staging" / "extra.txt").write_text("extra")
            transport = module.MockTransport({record["source_url"]: b"expected"})

            with self.assertRaises(module.CampaignBlocked):
                module.TransferRunner(
                    root,
                    transport,
                    approved_byte_ceiling=10_000,
                    enforce_window=False,
                    sleeper=lambda _: None,
                ).run([record])

            self.assertEqual(transport.calls, [])
            event = json.loads((root / "BLOCK_EVENT.json").read_text())
            self.assertEqual(event["reason"], "EXTRA_DESTINATION_FILE")

    def test_transient_attempt_is_durably_receipted_and_counted(self):
        with tempfile.TemporaryDirectory() as td:
            root = Path(td)
            payload = b"fits"
            record = self.make_record("1234m567", payload)
            clock = FakeClock()
            transport = module.MockTransport({record["source_url"]: [
                module.TransportResult(0, {}, 3, 28, "timeout"),
                payload,
            ]})
            result = module.TransferRunner(
                root,
                transport,
                approved_byte_ceiling=100,
                enforce_window=False,
                sleeper=clock.sleep,
                clock=clock.monotonic,
                wall_clock=clock.monotonic,
            ).run([record])

            receipts = [json.loads(line) for line in (root / "receipts.jsonl").read_text().splitlines()]
            self.assertEqual([item["outcome"] for item in receipts], [
                "TRANSIENT_RETRY_SCHEDULED", "ACCEPTED",
            ])
            self.assertEqual(result["cumulative_received_bytes"], 7)
            self.assertEqual(receipts[-1]["cumulative_received_bytes"], 7)

    def test_remaining_byte_ceiling_is_enforced_inside_transport(self):
        with tempfile.TemporaryDirectory() as td:
            root = Path(td)
            record = self.make_record("1234m567", b"ten bytes!")
            transport = module.MockTransport({record["source_url"]: b"ten bytes!"})
            with self.assertRaises(module.CampaignBlocked):
                module.TransferRunner(
                    root,
                    transport,
                    approved_byte_ceiling=4,
                    enforce_window=False,
                    sleeper=lambda _: None,
                ).run([record])
            self.assertEqual(
                json.loads((root / "BLOCK_EVENT.json").read_text())["reason"],
                "FILE_EXCEEDS_REMAINING_CEILING",
            )
            terminal = json.loads((root / "receipts.jsonl").read_text().splitlines()[-1])
            self.assertLessEqual(terminal["cumulative_received_bytes"], 4)

    def test_campaign_lock_blocks_a_second_runner_before_fetch(self):
        with tempfile.TemporaryDirectory() as td:
            root = Path(td)
            record = self.make_record("1234m567", b"fits")
            transport = module.MockTransport({record["source_url"]: b"fits"})
            with module.campaign_lock(root / "campaign.lock"):
                with self.assertRaises(module.CampaignBlocked):
                    module.TransferRunner(
                        root,
                        transport,
                        approved_byte_ceiling=100,
                        enforce_window=False,
                        sleeper=lambda _: None,
                    ).run([record])
            self.assertEqual(transport.calls, [])

    def test_changed_manifest_cannot_reuse_receipts(self):
        with tempfile.TemporaryDirectory() as td:
            root = Path(td)
            payload = b"fits"
            record = self.make_record("1234m567", payload)
            module.TransferRunner(
                root,
                module.MockTransport({record["source_url"]: payload}),
                approved_byte_ceiling=100,
                enforce_window=False,
                sleeper=lambda _: None,
            ).run([record])
            changed = dict(record)
            changed["reason"] = "changed provenance"
            transport = module.MockTransport({changed["source_url"]: payload})
            with self.assertRaisesRegex(module.CampaignBlocked, "campaign binding changed"):
                module.TransferRunner(
                    root,
                    transport,
                    approved_byte_ceiling=100,
                    enforce_window=False,
                    sleeper=lambda _: None,
                ).run([changed])
            self.assertEqual(transport.calls, [])

    def test_nontransient_404_is_not_retried(self):
        with tempfile.TemporaryDirectory() as td:
            root = Path(td)
            record = self.make_record("1234m567", b"fits")
            transport = module.MockTransport({record["source_url"]: module.TransportResult(
                404, {"content-length": "3"}, 3, 0,
            )})
            with self.assertRaises(module.CampaignBlocked):
                module.TransferRunner(
                    root,
                    transport,
                    approved_byte_ceiling=100,
                    enforce_window=False,
                    sleeper=lambda _: None,
                ).run([record])
            self.assertEqual(len(transport.calls), 1)

    def test_leaf_certificate_fingerprint_is_computed_from_pem_der(self):
        der = b"synthetic leaf certificate DER fixture"
        pem_body = __import__("base64").b64encode(der).decode()
        certs = (
            "Subject:CN=portal.nersc.gov\nIssuer:CN=fixture CA\n"
            f"Cert:-----BEGIN CERTIFICATE-----\n{pem_body}\n-----END CERTIFICATE-----\n"
        )
        self.assertEqual(
            module._leaf_certificate_fingerprint(certs),
            hashlib.sha256(der).hexdigest(),
        )

    def test_per_request_disk_failure_writes_block_event_before_fetch(self):
        with tempfile.TemporaryDirectory() as td:
            root = Path(td)
            record = self.make_record("1234m567", b"fits")
            transport = module.MockTransport({record["source_url"]: b"fits"})
            failed = {
                "pass": False,
                "available_bytes": 1,
                "required_bytes": 100,
                "probed_existing_parent": str(root),
            }
            with mock.patch.object(module, "disk_preflight", return_value=failed):
                with self.assertRaises(module.CampaignBlocked):
                    module.TransferRunner(
                        root,
                        transport,
                        approved_byte_ceiling=100,
                        enforce_window=False,
                        sleeper=lambda _: None,
                    ).run([record])
            self.assertEqual(transport.calls, [])
            self.assertEqual(
                json.loads((root / "BLOCK_EVENT.json").read_text())["reason"],
                "DISK_SPACE_PREFLIGHT_FAILED",
            )


if __name__ == "__main__":
    unittest.main()
