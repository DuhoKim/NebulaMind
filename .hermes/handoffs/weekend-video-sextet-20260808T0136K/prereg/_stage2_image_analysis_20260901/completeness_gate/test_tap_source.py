import json
import tempfile
import threading
import unittest
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path

from completeness_gate import GateError, GZRecord
from tap_source import (HttpClient, TAPCandidateSource, canonical_manifest,
                        make_sync_adql, validate_manifest)


def result_votable(status="OK", include_status=True, tag=0):
    info = f'<INFO name="QUERY_STATUS" value="{status}">done</INFO>' if include_status else ""
    return f'''<?xml version="1.0"?>
<VOTABLE xmlns="http://www.ivoa.net/xml/VOTable/v1.3"><RESOURCE type="results">
{info}<TABLE><FIELD name="input_index" datatype="long"/><FIELD name="release" datatype="long"/>
<FIELD name="brickid" datatype="long"/><FIELD name="objid" datatype="long"/>
<FIELD name="brickname" datatype="char" arraysize="*"/><FIELD name="ra" datatype="double"/>
<FIELD name="dec" datatype="double"/><DATA><TABLEDATA>
<TR><TD>{tag}</TD><TD>9010</TD><TD>1</TD><TD>22</TD><TD>0100p000</TD><TD>10</TD><TD>0</TD></TR>
</TABLEDATA></DATA></TABLE></RESOURCE></VOTABLE>'''.encode()


class FakeHandler(BaseHTTPRequestHandler):
    status = "OK"
    include_status = True
    tag = 0
    rate_limit_once = False
    rate_limit_hits = 0
    creations = 0

    def log_message(self, *args): pass

    def do_POST(self):
        if self.path == "/sync":
            type(self).creations += 1
            self.rfile.read(int(self.headers.get("Content-Length", 0)))
            self.send_response(200)
            self.send_header("Content-Type", "application/x-votable+xml")
            self.end_headers()
            self.wfile.write(result_votable(type(self).status, type(self).include_status,
                                            type(self).tag))
            return
        self.send_error(404)

    def do_GET(self):
        cls = type(self)
        if self.path == "/retry" and cls.rate_limit_once and cls.rate_limit_hits == 0:
            cls.rate_limit_hits += 1
            self.send_response(429); self.send_header("Retry-After", "0"); self.end_headers(); return
        if self.path == "/retry":
            self.send_response(200); self.end_headers(); self.wfile.write(b"ok"); return
        self.send_error(404)


class FakeServerTest(unittest.TestCase):
    def setUp(self):
        FakeHandler.status = "OK"; FakeHandler.include_status = True; FakeHandler.tag = 0
        FakeHandler.rate_limit_once = False; FakeHandler.rate_limit_hits = 0; FakeHandler.creations = 0
        self.server = ThreadingHTTPServer(("127.0.0.1", 0), FakeHandler)
        self.thread = threading.Thread(target=self.server.serve_forever, daemon=True); self.thread.start()
        self.base = f"http://127.0.0.1:{self.server.server_port}"

    def tearDown(self):
        self.server.shutdown(); self.server.server_close(); self.thread.join()

    def source(self, path, sleeps=None):
        client = HttpClient(sleep=(sleeps.append if sleeps is not None else lambda _: None), rng=lambda: 0)
        return TAPCandidateSource(self.base + "/sync", "ls_dr10.tractor_s",
            ["release", "brickid", "objid", "brickname", "ra", "dec"], Path(path),
            client=client, create_interval=0)

    def test_clean_checkpoint_and_http_capture(self):
        with tempfile.TemporaryDirectory() as td:
            source = self.source(td)
            result = source.run_chunk(0, [GZRecord(0, 1, 10, 0, .9, .1)])
            self.assertEqual(result["cap_signal"], "QUERY_STATUS=OK (MAXREC=10000)")
            self.assertEqual(len(list((Path(td) / "http").glob("*.json"))), 1)
            self.assertTrue((Path(td) / "checkpoint.jsonl").exists())

    def test_overflow_refuses_without_checkpoint(self):
        FakeHandler.status = "OVERFLOW"
        with tempfile.TemporaryDirectory() as td:
            with self.assertRaisesRegex(GateError, "overflow/truncation"):
                self.source(td).run_chunk(0, [GZRecord(0, 1, 10, 0, .9, .1)])
            self.assertFalse((Path(td) / "checkpoint.jsonl").exists())

    def test_missing_cap_signal_refuses(self):
        FakeHandler.include_status = False
        with tempfile.TemporaryDirectory() as td:
            with self.assertRaisesRegex(GateError, "lacks QUERY_STATUS cap signal"):
                self.source(td).run_chunk(0, [GZRecord(0, 1, 10, 0, .9, .1)])

    def test_provenance_expands_overlapping_cones_exactly(self):
        with tempfile.TemporaryDirectory() as td:
            source = self.source(td)
            records = [GZRecord(7, 1, 10, 0, .9, .1), GZRecord(8, 2, 10, 0, .9, .1)]
            FakeHandler.tag = 7
            source.run_chunk(0, records)
            self.assertEqual(len(source.candidates(records[0], 1.0)), 1)
            self.assertEqual(len(source.candidates(records[1], 1.0)), 1)

    def test_429_honors_retry_after_and_retries(self):
        FakeHandler.rate_limit_once = True; sleeps = []
        raw, _, _, status = HttpClient(sleep=sleeps.append, rng=lambda: 0).request(self.base + "/retry")
        self.assertEqual((raw, status, FakeHandler.rate_limit_hits), (b"ok", 200, 1))
        self.assertEqual(sleeps, [0.0])

    def test_resume_verifies_hash_restores_rows_and_does_not_recreate(self):
        with tempfile.TemporaryDirectory() as td:
            row = GZRecord(0, 1, 10, 0, .9, .1)
            self.source(td).run_chunk(0, [row])
            resumed = self.source(td); result = resumed.run_chunk(0, [row])
            self.assertTrue(result["resumed"]); self.assertEqual(len(resumed.candidates(row, 1.0)), 1)
            self.assertEqual(FakeHandler.creations, 1)
            entry = json.loads((Path(td) / "checkpoint.jsonl").read_text().strip())
            (Path(td) / entry["raw_result"]).write_bytes(b"corrupt")
            with self.assertRaisesRegex(GateError, "resume hash mismatch"):
                self.source(td).run_chunk(0, [row])

    def test_query_is_all_candidate_q3c_case_and_no_upload(self):
        q = make_sync_adql([GZRecord(4, 1, 10, -2, .9, .1)], "ls_dr10.tractor_s", False)
        self.assertIn("CASE WHEN q3c_radial_query", q)
        self.assertIn("='true'", q); self.assertNotIn("TAP_UPLOAD", q); self.assertNotIn("TOP ", q)


class ManifestTest(unittest.TestCase):
    def test_exact_893212_partition_has_no_gap_or_overlap(self):
        manifest = canonical_manifest()
        self.assertEqual(len(manifest["chunks"]), 8933)
        self.assertEqual(manifest["chunks"][0], {"chunk_id": 0, "start": 0, "stop": 100, "rows": 100})
        self.assertEqual(manifest["chunks"][-1], {"chunk_id": 8932, "start": 893200, "stop": 893212, "rows": 12})

    def test_noncanonical_input_index_set_refuses(self):
        manifest = canonical_manifest(3, 2); manifest["chunks"][1]["start"] = 1; manifest["chunks"][1]["rows"] = 2
        with self.assertRaisesRegex(GateError, "input_index set is not exactly 0..N-1"):
            validate_manifest(manifest, 3)


if __name__ == "__main__": unittest.main(verbosity=2)
