import json
import tempfile
import threading
import unittest
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
from unittest.mock import patch

from completeness_gate import GateError, GZRecord
import tap_source
from tap_source import (HttpClient, OutageBudgetExhausted, TAPCandidateSource,
                        append_jsonl, canonical_manifest, make_sync_adql,
                        sha256_bytes, validate_manifest)


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
    failures_remaining = 0

    def log_message(self, *args): pass

    def do_POST(self):
        if self.path == "/sync":
            type(self).creations += 1
            self.rfile.read(int(self.headers.get("Content-Length", 0)))
            if type(self).failures_remaining:
                type(self).failures_remaining -= 1
                self.send_response(503); self.end_headers(); return
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
        FakeHandler.failures_remaining = 0
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

    def test_resumed_chunks_read_checkpoint_once_and_hash_each_raw_once(self):
        count = 50
        with tempfile.TemporaryDirectory() as td:
            root = Path(td)
            records = [GZRecord(i, i + 1, 10, 0, 10, 0) for i in range(count)]
            for i in range(count):
                raw = result_votable(tag=i)
                attempt = root / f"chunk_{i:04d}"
                attempt.mkdir(parents=True)
                (attempt / "result.vot").write_bytes(raw)
                append_jsonl(root / "checkpoint.jsonl", {
                    "chunk_id": i, "raw_result": f"chunk_{i:04d}/result.vot",
                    "raw_sha256": sha256_bytes(raw), "cap_signal": "QUERY_STATUS=OK (MAXREC=10000)",
                })

            legacy = self.source(td)
            for i, record in enumerate(records):
                legacy._entries = None
                legacy.run_chunk(i, [record])
            expected = legacy._results

            resumed = self.source(td)
            real_read = tap_source.read_checkpoint
            real_sha = tap_source.sha256_file
            calls = {"read": 0, "sha": 0}
            def counted_read(*args, **kwargs):
                calls["read"] += 1
                return real_read(*args, **kwargs)
            def counted_sha(*args, **kwargs):
                calls["sha"] += 1
                return real_sha(*args, **kwargs)
            with patch("tap_source.read_checkpoint", side_effect=counted_read), \
                    patch("tap_source.sha256_file", side_effect=counted_sha):
                for i, record in enumerate(records):
                    self.assertTrue(resumed.run_chunk(i, [record])["resumed"])

            self.assertEqual(calls, {"read": 1, "sha": count})
            self.assertEqual(resumed._results, expected)

    def test_torn_checkpoint_tail_is_discarded_and_exactly_one_chunk_reruns(self):
        with tempfile.TemporaryDirectory() as td:
            root = Path(td); source = self.source(td)
            rows = [GZRecord(i, i + 1, 10, 0, .9, .1) for i in range(2)]
            FakeHandler.tag = 0; source.run_chunk(0, [rows[0]])
            FakeHandler.tag = 1; source.run_chunk(1, [rows[1]])
            checkpoint = root / "checkpoint.jsonl"
            lines = checkpoint.read_bytes().splitlines(keepends=True)
            checkpoint.write_bytes(lines[0] + lines[1][:len(lines[1]) // 2])
            before = FakeHandler.creations
            resumed = self.source(td)
            self.assertTrue(resumed.run_chunk(0, [rows[0]])["resumed"])
            rerun = resumed.run_chunk(1, [rows[1]])
            self.assertNotIn("resumed", rerun)
            self.assertEqual(FakeHandler.creations - before, 1)
            events = [json.loads(x) for x in (root / "run.log.jsonl").read_text().splitlines()]
            self.assertEqual([x["event"] for x in events], ["checkpoint_tail_discarded"])
            self.assertEqual(len(checkpoint.read_text().splitlines()), 2)

    def test_corrupt_middle_checkpoint_line_refuses(self):
        with tempfile.TemporaryDirectory() as td:
            root = Path(td); source = self.source(td)
            rows = [GZRecord(i, i + 1, 10, 0, .9, .1) for i in range(3)]
            for i, row in enumerate(rows):
                FakeHandler.tag = i
                source.run_chunk(i, [row])
            lines = (root / "checkpoint.jsonl").read_bytes().splitlines(keepends=True)
            (root / "checkpoint.jsonl").write_bytes(lines[0] + b'{"broken":\n' + lines[2])
            with self.assertRaisesRegex(GateError, "checkpoint_corrupt"):
                self.source(td).run_chunk(0, [rows[0]])

    def test_outage_failures_then_recovery_retries_same_chunk(self):
        with tempfile.TemporaryDirectory() as td:
            FakeHandler.failures_remaining = 3; sleeps = []
            source = self.source(td, sleeps)
            result = source.run_chunk(0, [GZRecord(0, 1, 10, 0, .9, .1)])
            self.assertEqual(result["chunk_id"], 0)
            self.assertEqual(FakeHandler.creations, 4)
            self.assertEqual(sleeps, [1, 2, 4])
            self.assertEqual(len((Path(td) / "checkpoint.jsonl").read_text().splitlines()), 1)

    def test_outage_budget_exhaustion_leaves_checkpoint_unchanged(self):
        with tempfile.TemporaryDirectory() as td:
            root = Path(td); row = GZRecord(0, 1, 10, 0, .9, .1)
            self.source(td).run_chunk(0, [row])
            checkpoint = root / "checkpoint.jsonl"; before = checkpoint.read_bytes()
            FakeHandler.failures_remaining = 99
            clock = [0.0]
            def sleep(delay): clock[0] += delay
            client = HttpClient(sleep=sleep, rng=lambda: 0, max_outage_minutes=.05,
                                monotonic=lambda: clock[0], run_log=root / "run.log.jsonl")
            source = TAPCandidateSource(self.base + "/sync", "ls_dr10.tractor_s",
                ["release", "brickid", "objid", "brickname", "ra", "dec"], root,
                client=client, create_interval=0)
            with self.assertRaisesRegex(OutageBudgetExhausted, "outage_budget_exhausted"):
                source.run_chunk(1, [GZRecord(1, 2, 10, 0, .9, .1)])
            self.assertEqual(checkpoint.read_bytes(), before)

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
