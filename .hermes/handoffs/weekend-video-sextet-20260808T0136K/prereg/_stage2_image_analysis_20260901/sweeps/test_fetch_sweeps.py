import hashlib
import json
import tempfile
import threading
import unittest
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
from types import SimpleNamespace

import fetch_sweeps as fs


GOOD = b"a small fake sweep payload"


class FakeHandler(BaseHTTPRequestHandler):
    routes = {}
    counts = {}

    def do_GET(self):
        type(self).counts[self.path] = type(self).counts.get(self.path, 0) + 1
        action = type(self).routes[self.path](type(self).counts[self.path])
        status, body, declared = action
        self.send_response(status)
        self.send_header("Content-Length", str(len(body) if declared is None else declared))
        self.end_headers()
        if body:
            self.wfile.write(body)
        self.close_connection = True

    def log_message(self, *args):
        pass


class FetchSweepsTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.root = Path(self.temp.name)
        FakeHandler.routes = {}
        FakeHandler.counts = {}
        self.server = ThreadingHTTPServer(("127.0.0.1", 0), FakeHandler)
        self.thread = threading.Thread(target=self.server.serve_forever, daemon=True)
        self.thread.start()
        self.base = f"http://127.0.0.1:{self.server.server_port}"

    def tearDown(self):
        self.server.shutdown()
        self.server.server_close()
        self.thread.join()
        self.temp.cleanup()

    def args(self, workers=8):
        dest = self.root / "data"
        quarantine = self.root / "quarantine"
        dest.mkdir()
        quarantine.mkdir()
        return SimpleNamespace(dest=dest, quarantine=quarantine,
                               journal=self.root / "receipts.jsonl", workers=workers,
                               timeout=2, delay=0)

    def entry(self, name="sweep-test.fits"):
        return {"filename": name, "url": self.base + "/file", "bytes": len(GOOD)}

    def receipts(self, args):
        return [json.loads(x) for x in args.journal.read_text().splitlines()]

    def fetcher(self, args, entry, logs=None):
        sha = hashlib.sha256(GOOD).hexdigest()
        return fs.Fetcher(args, {entry["filename"]: sha}, [entry],
                          log=(logs.append if logs is not None else lambda x: None),
                          sleeper=lambda seconds: None, rng=lambda: 0)

    def test_ok_receipt_exact_shape(self):
        FakeHandler.routes["/file"] = lambda n: (200, GOOD, None)
        args, entry = self.args(), self.entry()
        self.assertEqual(self.fetcher(args, entry).run(), 0)
        rec = self.receipts(args)[0]
        self.assertEqual(set(rec), {"brick", "bytes", "computed_sha256",
                         "published_sha256", "url", "utc", "verdict"})
        self.assertEqual(rec["verdict"], "OK")
        self.assertEqual(rec["brick"], entry["filename"])

    def test_truncated_receipt_then_success(self):
        FakeHandler.routes["/file"] = lambda n: ((200, GOOD[:4], len(GOOD))
                                                        if n == 1 else (200, GOOD, None))
        args, entry = self.args(), self.entry()
        self.assertEqual(self.fetcher(args, entry).run(), 0)
        recs = self.receipts(args)
        self.assertEqual([r["verdict"] for r in recs], ["FETCH-FAILED", "OK"])
        self.assertEqual(set(recs[0]), {"brick", "error", "url", "utc", "verdict"})

    def test_429_backoff_and_global_worker_halving(self):
        FakeHandler.routes["/file"] = lambda n: ((429, b"", None)
                                                        if n <= 3 else (200, GOOD, None))
        args, entry, logs = self.args(), self.entry(), []
        fetcher = self.fetcher(args, entry, logs)
        self.assertEqual(fetcher.run(), 0)
        self.assertEqual(fetcher.throttle.limit, 4)
        self.assertTrue(any("halved to 4" in line for line in logs))
        self.assertEqual([r["verdict"] for r in self.receipts(args)],
                         ["FETCH-FAILED"] * 3 + ["OK"])

    def test_sha_mismatch_quarantined_exact_shape(self):
        bad = b"wrong bytes"
        FakeHandler.routes["/file"] = lambda n: (200, bad, None)
        args, entry = self.args(), self.entry()
        self.assertEqual(self.fetcher(args, entry).run(), 1)
        rec = self.receipts(args)[0]
        self.assertEqual(rec["verdict"], "SHA-MISMATCH-QUARANTINED")
        self.assertEqual(set(rec), {"brick", "bytes", "computed_sha256",
                         "published_sha256", "url", "utc", "verdict"})
        self.assertTrue((args.quarantine / entry["filename"]).exists())
        self.assertFalse((args.dest / entry["filename"]).exists())

    def test_resume_skips_present_verified_file(self):
        FakeHandler.routes["/file"] = lambda n: (500, b"", None)
        args, entry = self.args(), self.entry()
        (args.dest / entry["filename"]).write_bytes(GOOD)
        fetcher = self.fetcher(args, entry)
        self.assertEqual(fetcher.run(), 0)
        self.assertEqual(fetcher.skipped, 1)
        self.assertEqual(FakeHandler.counts.get("/file", 0), 0)
        self.assertFalse(args.journal.exists())


if __name__ == "__main__":
    unittest.main(verbosity=2)
