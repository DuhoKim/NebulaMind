import hashlib
import json
import subprocess
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

import seal_gate
from seal_gate import (EXPECTED_BLOB_ID, ZERO_DIGEST, canonical_bytes, checksum_url,
                       run_gate, sha256_bytes)


class SealGateTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.root = Path(self.temp.name)
        self.bricks = self.root / "bricks"
        self.bricks.mkdir()
        self.names = [f"00{i}p00{i}" for i in range(5)]
        manifest = {"schema": "TIERC-MANIFEST-3", "bricks": [
            {"brick": brick, "planes": [f"legacysurvey-{brick}-{plane}.fits.fz"
                                         for plane in seal_gate.PLANES]}
            for brick in self.names]}
        (self.root / "manifest.json").write_text(json.dumps(manifest))
        self.payloads = {}
        self.rows_by_plane = {plane: [] for plane in seal_gate.PLANES}
        for brick in self.names:
            lines = []
            for plane in seal_gate.PLANES:
                data = f"synthetic-{brick}-{plane}".encode()
                digest = hashlib.sha256(data).hexdigest()
                filename = f"legacysurvey-{brick}-{plane}.fits.fz"
                (self.bricks / filename).write_bytes(data)
                lines.append(f"{digest}  {filename}\r\n")
                self.rows_by_plane[plane].append(
                    {"brick": brick, "bytes": len(data), "computed_sha256": digest,
                     "published_sha256": digest, "url": f"synthetic://{brick}/{plane}",
                     "utc": "2026-09-02T00:00:00Z", "verdict": "OK"})
            self.payloads[checksum_url(brick)] = "".join(lines).encode()
        self.rows = self.rows_by_plane["image-r"]
        self._write_journals()
        self.live = self.root / "fetch_bricks.py"
        self.pin = self.root / "fetch_bricks_pinned.py"
        self.live.write_bytes(b"same-script\n")
        self.pin.write_bytes(b"same-script\n")
        self.seal_journal = self.root / "seal.jsonl"

    def tearDown(self):
        self.temp.cleanup()

    def _write_journals(self):
        for plane, rows in self.rows_by_plane.items():
            (self.root / f"journal-{plane}.jsonl").write_text(
                "".join(json.dumps(r) + "\n" for r in rows))

    def _write_journal(self):
        self.rows_by_plane["image-r"] = self.rows
        self._write_journals()

    def failed_row(self, brick, verdict="FETCH-FAILED"):
        if verdict == "FETCH-FAILED":
            return {"brick": brick, "error": "OSError: synthetic", "url": "synthetic://" + brick,
                    "utc": "2026-09-01T23:59:59Z", "verdict": verdict}
        row = dict(next(row for row in self.rows if row["brick"] == brick), verdict=verdict)
        if verdict == "OK-NO-PUBLISHED-SHA":
            row["published_sha256"] = None
        return row

    def fetcher(self, url, timeout):
        return self.payloads[url]

    def git(self, command, capture_output=True):
        if command[1:3] == ["ls-files", "-s"]:
            return subprocess.CompletedProcess(command, 0, stdout="100644 " + EXPECTED_BLOB_ID + " 0\t" + str(self.live) + "\n", stderr="")
        if command[1:3] == ["cat-file", "-p"]:
            return subprocess.CompletedProcess(command, 0, stdout=self.live.read_bytes(), stderr=b"")
        return subprocess.CompletedProcess(command, 0, stdout=b"", stderr=b"")

    def run_fixture(self, **changes):
        journals = {plane: self.root / f"journal-{plane}.jsonl" for plane in seal_gate.PLANES}
        args = dict(manifest=self.root / "manifest.json", journals=journals,
                    bricks_dir=self.bricks, live_script=self.live, pinned_copy=self.pin,
                    seal_journal=self.seal_journal,
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
        self.assertEqual(5, receipt["counts"]["files_checked"])
        self.assertEqual({"image-r": 5, "maskbits": 5, "nexp-r": 5},
                         receipt["counts"]["receipt_count_by_plane"])

    def test_duplicate_ok_receipts_pass(self):
        self.rows.append(dict(self.rows[2]))
        self._write_journal()
        receipt = self.run_fixture()
        self.assertEqual("PASS", receipt["status"])
        self.assertTrue(receipt["data_integrity_pass"])

    def test_fetch_network_error(self):
        def unavailable(url, timeout):
            raise OSError("network unavailable")

        self.assert_refusal(
            self.run_fixture(fetcher=unavailable),
            "published_checksum_fetch_failed: OSError: network unavailable",
        )

    def test_malformed_journal_json(self):
        (self.root / "journal-image-r.jsonl").write_text("{not-json}\n")
        self.assert_refusal(self.run_fixture(), "malformed_journal")

    def test_fetch_omitted(self):
        self.assert_refusal(
            self.run_fixture(fetch=False), "published_checksum_refetch_not_requested"
        )

    def test_git_worktree_dirty(self):
        def dirty_git(command, capture_output=True):
            result = self.git(command, capture_output=capture_output)
            if command[1:3] == ["diff", "--quiet"]:
                return subprocess.CompletedProcess(command, 1, stdout=b"", stderr=b"")
            return result

        self.assert_refusal(self.run_fixture(git_runner=dirty_git), "git_worktree_dirty")

    def test_git_blob_id_mismatch(self):
        self.assert_refusal(
            self.run_fixture(expected_blob_id="a" * 40), "git_blob_id_mismatch"
        )

    def test_unexpected_exception_emits_named_refusal(self):
        with patch.object(seal_gate, "_manifest_entries", side_effect=KeyError("injected")):
            self.assert_refusal(self.run_fixture(), "KeyError: 'injected'")

    def test_seal_journal_chain_broken(self):
        self.seal_journal.write_text(
            json.dumps({"receipt_digest": "f" * 64}, sort_keys=True,
                       separators=(",", ":")) + "\n"
        )
        self.assert_refusal(self.run_fixture(), "seal_journal_chain_broken")

    def test_genesis_predecessor_when_seal_journal_absent(self):
        self.assertFalse(self.seal_journal.exists())
        receipt = self.run_fixture()
        self.assertEqual(ZERO_DIGEST, receipt["predecessor_receipt_digest"])

    def test_predecessor_from_two_record_seal_journal(self):
        records = []
        predecessor = ZERO_DIGEST
        for number in (1, 2):
            body = {"number": number, "predecessor_receipt_digest": predecessor}
            record = dict(body, receipt_digest=sha256_bytes(canonical_bytes(body)))
            records.append(record)
            predecessor = record["receipt_digest"]
        self.seal_journal.write_bytes(b"".join(canonical_bytes(r) for r in records))
        receipt = self.run_fixture()
        self.assertEqual(records[-1]["receipt_digest"],
                         receipt["predecessor_receipt_digest"])

    def test_missing_file(self):
        (self.bricks / f"legacysurvey-{self.names[2]}-nexp-r.fits.fz").unlink()
        self.assert_refusal(self.run_fixture(), "missing_brick_file:nexp-r")

    def test_disk_hash_mismatch(self):
        (self.bricks / f"legacysurvey-{self.names[2]}-image-r.fits.fz").write_bytes(b"wrong")
        self.assert_refusal(self.run_fixture(), "disk_hash_mismatch:image-r")

    def test_fresh_published_disagrees_with_receipt(self):
        self.rows[2]["published_sha256"] = "f" * 64
        self.rows[2]["computed_sha256"] = "f" * 64
        self._write_journal()
        self.assert_refusal(self.run_fixture(), "fresh_published_receipt_disagreement:image-r")

    def test_incomplete_journal(self):
        self.rows.pop()
        self._write_journal()
        self.assert_refusal(self.run_fixture(), "acquisition_set_incomplete:image-r")

    def test_fetch_failed_without_later_ok_refuses(self):
        self.rows = [row for row in self.rows if row["brick"] != self.names[1]]
        self.rows.append(self.failed_row(self.names[1]))
        self._write_journal()
        self.assert_refusal(self.run_fixture(), "non_ok_without_later_ok:image-r")

    def test_fetch_failed_then_later_ok_passes(self):
        self.rows.insert(1, self.failed_row(self.names[1]))
        self._write_journal()
        self.assertEqual("PASS", self.run_fixture()["status"])

    def test_ok_no_published_sha_without_later_ok_refuses_as_non_ok(self):
        bad = self.failed_row(self.names[1], "OK-NO-PUBLISHED-SHA")
        self.rows = [row for row in self.rows if row["brick"] != self.names[1]]
        self.rows.append(bad)
        self._write_journal()
        self.assert_refusal(self.run_fixture(), "non_ok_without_later_ok:image-r")

    def test_sha_mismatch_quarantined_then_later_ok_passes(self):
        self.rows.insert(1, self.failed_row(self.names[1], "SHA-MISMATCH-QUARANTINED"))
        self._write_journal()
        self.assertEqual("PASS", self.run_fixture()["status"])

    def test_five_key_ok_is_malformed(self):
        row = self.failed_row(self.names[1])
        row["verdict"] = "OK"
        self.rows.append(row)
        self._write_journal()
        self.assert_refusal(self.run_fixture(), "malformed_journal_schema")

    def test_ok_with_published_null_is_malformed(self):
        self.rows[1]["published_sha256"] = None
        self._write_journal()
        self.assert_refusal(self.run_fixture(), "malformed_journal_schema")

    def test_unknown_verdict_is_malformed(self):
        self.rows[1]["verdict"] = "UNKNOWN"
        self._write_journal()
        self.assert_refusal(self.run_fixture(), "malformed_journal_schema")

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
