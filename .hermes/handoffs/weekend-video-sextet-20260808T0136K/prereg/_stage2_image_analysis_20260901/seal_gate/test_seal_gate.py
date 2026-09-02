import hashlib
import json
import subprocess
import tempfile
import unittest
from pathlib import Path
from unittest.mock import Mock

from seal_gate import ZERO_DIGEST, canonical_bytes, checksum_url, run_gate, sha256_bytes


class SealGateTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.root = Path(self.temp.name)
        self.bricks = self.root / "bricks"
        self.bricks.mkdir()
        self.names = [f"00{i}p00{i}" for i in range(5)]
        (self.root / "manifest.json").write_text(json.dumps(self.names))
        self.payloads = {}
        rows = []
        for brick in self.names:
            data = ("synthetic-" + brick).encode()
            digest = hashlib.sha256(data).hexdigest()
            filename = f"legacysurvey-{brick}-image-r.fits.fz"
            (self.bricks / filename).write_bytes(data)
            self.payloads[checksum_url(brick)] = f"{digest}  {filename}\r\n".encode()
            rows.append({"brick": brick, "bytes": len(data), "computed_sha256": digest,
                         "published_sha256": digest, "url": "synthetic://" + brick,
                         "utc": "2026-09-02T00:00:00Z", "verdict": "OK"})
        self.rows = rows
        self._write_journal()
        self.live = self.root / "fetch_bricks.py"
        self.pin = self.root / "fetch_bricks_pinned.py"
        self.live.write_bytes(b"same-script\n")
        self.pin.write_bytes(b"same-script\n")

    def tearDown(self):
        self.temp.cleanup()

    def _write_journal(self):
        (self.root / "journal.jsonl").write_text("".join(json.dumps(r) + "\n" for r in self.rows))

    def fetcher(self, url, timeout):
        return self.payloads[url]

    def git(self, command, capture_output=True):
        if command[1:3] == ["ls-files", "-s"]:
            return subprocess.CompletedProcess(command, 0, stdout="100644 " + "a" * 40 + " 0\t" + str(self.live) + "\n", stderr="")
        if command[1:3] == ["cat-file", "-p"]:
            return subprocess.CompletedProcess(command, 0, stdout=self.live.read_bytes(), stderr=b"")
        return subprocess.CompletedProcess(command, 0, stdout=b"", stderr=b"")

    def run_fixture(self, **changes):
        args = dict(manifest=self.root / "manifest.json", journal=self.root / "journal.jsonl",
                    bricks_dir=self.bricks, live_script=self.live, pinned_copy=self.pin,
                    expected_manifest_count=5, fetch=True, fetcher=self.fetcher,
                    process_checker=lambda: False, git_runner=self.git,
                    timestamp="2026-09-02T00:00:00Z")
        args.update(changes)
        return run_gate(**args)

    def assert_refusal(self, receipt, failure):
        self.assertEqual("REFUSE", receipt["status"])
        self.assertEqual("DATA-INTEGRITY-FAIL", receipt["verdict"])
        self.assertEqual(failure, receipt["failure"])
        self.assertFalse(receipt["data_integrity_pass"])

    def test_all_good(self):
        receipt = self.run_fixture()
        self.assertEqual("PASS", receipt["status"])
        self.assertEqual("PASS", receipt["verdict"])
        self.assertTrue(receipt["data_integrity_pass"])
        body = dict(receipt)
        digest = body.pop("receipt_digest")
        self.assertEqual(digest, sha256_bytes(canonical_bytes(body)))
        self.assertEqual(ZERO_DIGEST, receipt["predecessor_receipt_digest"])

    def test_missing_file(self):
        (self.bricks / f"legacysurvey-{self.names[2]}-image-r.fits.fz").unlink()
        self.assert_refusal(self.run_fixture(), "missing_brick_file")

    def test_disk_hash_mismatch(self):
        (self.bricks / f"legacysurvey-{self.names[2]}-image-r.fits.fz").write_bytes(b"wrong")
        self.assert_refusal(self.run_fixture(), "disk_hash_mismatch")

    def test_fresh_published_disagrees_with_receipt(self):
        self.rows[2]["published_sha256"] = "f" * 64
        self.rows[2]["computed_sha256"] = "f" * 64
        self._write_journal()
        self.assert_refusal(self.run_fixture(), "fresh_published_receipt_disagreement")

    def test_incomplete_journal(self):
        self.rows.pop()
        self._write_journal()
        self.assert_refusal(self.run_fixture(), "acquisition_set_incomplete")

    def test_non_ok_without_later_ok(self):
        bad = dict(self.rows[1], verdict="FETCH-FAILED")
        self.rows.append(bad)
        self._write_journal()
        self.assert_refusal(self.run_fixture(), "non_ok_without_later_ok")

    def test_process_running(self):
        self.assert_refusal(self.run_fixture(process_checker=lambda: True), "acquisition_process_running")

    def test_git_custody_mismatch(self):
        self.pin.write_bytes(b"different")
        self.assert_refusal(self.run_fixture(), "git_custody_digest_mismatch")

    def test_extra_file_refuses_under_section_7_8(self):
        (self.bricks / "extra.fits.fz").write_bytes(b"extra")
        self.assert_refusal(self.run_fixture(), "extra_brick_file")


if __name__ == "__main__":
    unittest.main(verbosity=2)
