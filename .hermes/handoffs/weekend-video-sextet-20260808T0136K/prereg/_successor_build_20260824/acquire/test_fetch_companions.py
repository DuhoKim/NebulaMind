#!/usr/bin/env python3
import hashlib
import json
import tempfile
import threading
import unittest
from functools import partial
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path

import fetch_companions as subject


class QuietHandler(SimpleHTTPRequestHandler):
    def log_message(self, _format, *_args):
        pass


class CompanionFetcherTests(unittest.TestCase):
    BRICK = "0001m010"

    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.root = Path(self.temp.name)
        self.web = self.root / "web"
        self.dest = self.root / "dest"
        self.quarantine = self.root / "quarantine"
        self.journal = self.root / "journal.jsonl"
        directory = self.web / "000" / self.BRICK
        directory.mkdir(parents=True)
        self.payloads = {
            "image-r": b"synthetic image",
            "invvar-r": b"synthetic inverse variance",
            "maskbits": b"synthetic mask bits",
            "nexp-r": b"synthetic exposure counts",
        }
        self.write_server_files(self.payloads)
        handler = partial(QuietHandler, directory=str(self.web))
        self.server = ThreadingHTTPServer(("127.0.0.1", 0), handler)
        self.thread = threading.Thread(target=self.server.serve_forever,
                                       daemon=True)
        self.thread.start()
        self.old_base = subject.BASE
        subject.BASE = f"http://127.0.0.1:{self.server.server_port}"

    def tearDown(self):
        subject.BASE = self.old_base
        self.server.shutdown()
        self.server.server_close()
        self.thread.join()
        self.temp.cleanup()

    def write_server_files(self, payloads, checksum_planes=None):
        directory = self.web / "000" / self.BRICK
        lines = []
        checksum_planes = checksum_planes or list(payloads)
        for plane, payload in payloads.items():
            name = subject.plane_filename(self.BRICK, plane)
            (directory / name).write_bytes(payload)
            if plane in checksum_planes:
                lines.append(f"{hashlib.sha256(payload).hexdigest()}  {name}\n")
        checksum = directory / (
            f"legacysurvey_dr10_south_coadd_000_{self.BRICK}.sha256sum")
        checksum.write_text("".join(lines))

    def args(self, plane="nexp-r", *, allow_invvar=False):
        manifest = self.root / "manifest.json"
        manifest.write_text(json.dumps([self.BRICK]))
        return type("Args", (), dict(
            plane=plane, allow_invvar=allow_invvar, limit=0, delay=0, timeout=2, start=0, workers=1,
            manifest=manifest, dest=self.dest, journal=self.journal,
            quarantine=self.quarantine))()

    def receipt(self):
        return json.loads(self.journal.read_text().splitlines()[-1])

    def test_checksum_line_forms_parse_identically(self):
        sha = "a" * 64
        name = subject.plane_filename(self.BRICK, "maskbits")
        self.assertEqual(subject.SHA_RE.findall(f"{sha}  {name}"),
                         [(sha, name)])
        self.assertEqual(subject.SHA_RE.findall(f"{sha} *{name}"),
                         [(sha, name)])

    def test_published_sha_accepts_text_and_binary_markers_once(self):
        sha = hashlib.sha256(self.payloads["maskbits"]).hexdigest()
        name = subject.plane_filename(self.BRICK, "maskbits")
        checksum = self.web / "000" / self.BRICK / (
            f"legacysurvey_dr10_south_coadd_000_{self.BRICK}.sha256sum")
        for marker in ("  ", " *"):
            with self.subTest(marker=marker):
                checksum.write_text(f"{sha}{marker}{name}\n")
                self.assertEqual(subject.published_sha(
                    self.BRICK, "maskbits", 2), sha)

    def test_malformed_checksum_lines_do_not_match(self):
        sha = "a" * 64
        name = subject.plane_filename(self.BRICK, "maskbits")
        self.assertEqual(subject.SHA_RE.findall(f"{sha[:-1]}  {name}"), [])
        self.assertEqual(subject.SHA_RE.findall(f"{sha}  {name} junk"), [])

    def test_published_sha_raises_when_wanted_filename_is_absent(self):
        self.write_server_files(self.payloads, checksum_planes=["image-r"])
        name = subject.plane_filename(self.BRICK, "maskbits")
        with self.assertRaisesRegex(
                RuntimeError,
                f"published checksum line count for {name}: 0"):
            subject.published_sha(self.BRICK, "maskbits", 2)

    def test_ok_receipt_shape_exact(self):
        self.assertEqual(subject.run(self.args()), 0)
        rec = self.receipt()
        self.assertEqual(set(rec), {"brick", "bytes", "computed_sha256",
                         "published_sha256", "url", "utc", "verdict"})
        self.assertEqual(rec["verdict"], "OK")
        self.assertEqual(rec["computed_sha256"], rec["published_sha256"])

    def test_mismatch_quarantines_with_seven_key_shape(self):
        bad_name = subject.plane_filename(self.BRICK, "nexp-r")
        (self.web / "000" / self.BRICK / bad_name).write_bytes(b"corrupt")
        self.assertEqual(subject.run(self.args()), 1)
        rec = self.receipt()
        self.assertEqual(rec["verdict"], "SHA-MISMATCH-QUARANTINED")
        self.assertEqual(len(rec), 7)
        self.assertTrue((self.quarantine / bad_name).exists())
        self.assertFalse((self.dest / bad_name).exists())

    def test_fetch_failure_has_exact_five_key_shape(self):
        name = subject.plane_filename(self.BRICK, "maskbits")
        (self.web / "000" / self.BRICK / name).unlink()
        self.assertEqual(subject.run(self.args("maskbits")), 1)
        rec = self.receipt()
        self.assertEqual(set(rec), {"brick", "error", "url", "utc", "verdict"})
        self.assertEqual(rec["verdict"], "FETCH-FAILED")

    def test_resume_skips_verified_file(self):
        self.dest.mkdir()
        name = subject.plane_filename(self.BRICK, "nexp-r")
        (self.dest / name).write_bytes(self.payloads["nexp-r"])
        self.assertEqual(subject.run(self.args()), 0)
        self.assertFalse(self.journal.exists())

    def test_absent_selected_plane_line_is_fetch_failed(self):
        self.write_server_files(self.payloads,
                                checksum_planes=["image-r", "maskbits"])
        self.assertEqual(subject.run(self.args()), 1)
        rec = self.receipt()
        self.assertEqual(set(rec), {"brick", "error", "url", "utc", "verdict"})
        self.assertEqual(rec["verdict"], "FETCH-FAILED")

    def test_invvar_requires_explicit_legacy_flag(self):
        with self.assertRaisesRegex(SystemExit, "explicit --allow-invvar"):
            subject.run(self.args("invvar-r"))
        self.assertEqual(subject.run(self.args("invvar-r", allow_invvar=True)), 0)


if __name__ == "__main__":
    unittest.main(verbosity=2)
