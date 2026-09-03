import gzip
import json
import re
import tempfile
import threading
import time
import unittest
from contextlib import redirect_stderr
from io import StringIO
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
from unittest.mock import patch

from completeness_gate import GateError
from run_full import execute, load_prior, main
from tap_source import HttpClient, OutageBudgetExhausted


class RunnerHandler(BaseHTTPRequestHandler):
    requests = 0
    tags = []
    delays = {}
    retry_once = set()
    lock = threading.Lock()
    def log_message(self, *args): pass
    def do_POST(self):
        body = self.rfile.read(int(self.headers["Content-Length"])).decode()
        from urllib.parse import parse_qs
        query = parse_qs(body)["QUERY"][0]
        tag = int(re.search(r"THEN (\d+)", query).group(1))
        ras = [float(x) for x in re.findall(r"q3c_radial_query\(t.ra,t.dec,([0-9.]+),", query)]
        ra = ras[0]
        with type(self).lock:
            type(self).requests += 1
            type(self).tags.append(tag)
            retry = tag in type(self).retry_once
            type(self).retry_once.discard(tag)
        if retry:
            self.send_response(429); self.send_header("Retry-After", "0"); self.end_headers()
            return
        time.sleep(type(self).delays.get(tag, 0))
        raw = f'''<VOTABLE xmlns="http://www.ivoa.net/xml/VOTable/v1.3"><RESOURCE>
<INFO name="QUERY_STATUS" value="OK">done</INFO><TABLE>
<FIELD name="input_index"/><FIELD name="release"/><FIELD name="brickid"/><FIELD name="objid"/>
<FIELD name="brickname"/><FIELD name="ra"/><FIELD name="dec"/><DATA><TABLEDATA>
<TR><TD>{tag}</TD><TD>9010</TD><TD>{tag+1}</TD><TD>{tag+100}</TD><TD>x</TD><TD>{ra}</TD><TD>0</TD></TR>
</TABLEDATA></DATA></TABLE></RESOURCE></VOTABLE>'''.encode()
        self.send_response(200); self.end_headers(); self.wfile.write(raw)


class RunFullE2E(unittest.TestCase):
    def setUp(self):
        RunnerHandler.requests = 0
        RunnerHandler.tags = []
        RunnerHandler.delays = {}
        RunnerHandler.retry_once = set()
        self.server = ThreadingHTTPServer(("127.0.0.1", 0), RunnerHandler)
        self.thread = threading.Thread(target=self.server.serve_forever, daemon=True); self.thread.start()
        self.sync = f"http://127.0.0.1:{self.server.server_port}/sync"
    def tearDown(self):
        self.server.shutdown(); self.server.server_close(); self.thread.join()

    def fixture(self, root: Path, prior_count=13725):
        t2, t3 = root/"t2.csv.gz", root/"t3.csv.gz"
        header = "OBJID,RA,DEC,P_CW,P_ACW\n"
        with gzip.open(t2,"wt") as f:
            f.write(header + "".join(f"{i+1},00:40:{i:02d},+00:00:00,.9,.1\n" for i in range(10)))
        with gzip.open(t3,"wt") as f: f.write(header)
        prior=root/"prior.json"; prior.write_text(json.dumps({"objids":[i+1 for i in range(prior_count)],"provenance":{"source":"synthetic"}}))
        probe=root/"probe.json"; probe.write_text(json.dumps({"advertised_sync_endpoint":self.sync,"relation":"ls_dr10.tractor_s","columns":[{"column_name":x} for x in ["release","brickid","objid","brickname","ra","dec"]]}))
        a=root/"a.csv"; p=root/"p.csv"; a.write_text("ra,dec\n"); p.write_text("ra,dec\n")
        return dict(table2=t2,table3=t3,tier_a=a,parent=p,prior=prior,artifacts=root/"art",probe_receipt=probe,total_rows=10,chunk_size=2,expected_prior=prior_count)

    @staticmethod
    def fast_client(artifacts):
        return HttpClient(sleep=lambda _: None, rng=lambda: 0,
                          capture_dir=artifacts/"http", run_log=artifacts/"run.log.jsonl")

    @patch("run_full.run_pinned_files", return_value=([], {"funnel_counts":{},"prior_unresolved_terminal":[]}))
    def test_two_workers_resume_after_both_uncheckpointed_killed_attempts(self, _):
        with tempfile.TemporaryDirectory() as td:
            kw=self.fixture(Path(td)); first=execute(**kw,max_chunks=2,workers=2,
                                                     client=self.fast_client(kw["artifacts"]))
            self.assertEqual(first["chunks_run"],2)
            for cid in (2, 3):
                orphan=kw["artifacts"]/f"chunk_{cid:04d}_killed"
                orphan.mkdir(); (orphan/"result.vot").write_bytes(b"partial")
            result=execute(**kw,resume=True,workers=2,
                           client=self.fast_client(kw["artifacts"]))
            self.assertEqual(result["status"],"PASS"); self.assertEqual(RunnerHandler.requests,5)
            entries=[json.loads(x) for x in (kw["artifacts"]/"checkpoint.jsonl").read_text().splitlines()]
            self.assertEqual(sorted(e["chunk_id"] for e in entries),list(range(5)))

    @patch("run_full.run_pinned_files", return_value=([], {"funnel_counts":{},"prior_unresolved_terminal":[]}))
    def test_two_workers_admit_interleaved_exactly_once(self, _):
        with tempfile.TemporaryDirectory() as td:
            kw=self.fixture(Path(td)); RunnerHandler.delays={0:.25}
            result=execute(**kw,workers=2,client=self.fast_client(kw["artifacts"]))
            self.assertEqual(result["status"],"PASS")
            ids=[json.loads(x)["chunk_id"] for x in (kw["artifacts"]/"checkpoint.jsonl").read_text().splitlines()]
            self.assertEqual(sorted(ids),list(range(5)))
            self.assertNotEqual(ids,list(range(5)))
            self.assertEqual(sorted(RunnerHandler.tags),[0,2,4,6,8])

    @patch("run_full.run_pinned_files", return_value=([], {"funnel_counts":{},"prior_unresolved_terminal":[]}))
    def test_retryable_response_drops_to_one_worker(self, _):
        with tempfile.TemporaryDirectory() as td:
            kw=self.fixture(Path(td)); RunnerHandler.retry_once={0}
            execute(**kw,workers=2,client=self.fast_client(kw["artifacts"]))
            events=[json.loads(x) for x in (kw["artifacts"]/"run.log.jsonl").read_text().splitlines()]
            drops=[x for x in events if x.get("event")=="workers_downgraded"]
            self.assertEqual(len(drops),1); self.assertEqual(drops[0]["to_workers"],1)
            self.assertEqual(sorted(set(RunnerHandler.tags)),[0,2,4,6,8])
            self.assertEqual(RunnerHandler.requests,6)

    def test_worker_count_does_not_enter_analytical_receipt(self):
        with tempfile.TemporaryDirectory() as td:
            kw=self.fixture(Path(td)); observed=[]
            def pinned(*args):
                source=args[-1]
                observed.append(json.dumps(source.provenance, sort_keys=True))
                return [], {"funnel_counts":{},"prior_unresolved_terminal":[]}
            with patch("run_full.run_pinned_files", side_effect=pinned), \
                 patch("run_full.utc_stamp", return_value="20000101T000000Z"):
                first=execute(**kw,workers=2,client=self.fast_client(kw["artifacts"]))
                first_bytes=Path(first["receipt"]).read_bytes()
                second=execute(**kw,dry_finalise=True,resume=True,workers=1)
                second_bytes=Path(second["receipt"]).read_bytes()
            self.assertEqual(observed[0],observed[1])
            self.assertEqual(first_bytes,second_bytes)
            receipt=json.loads(sorted(kw["artifacts"].glob("completeness_receipt_*.json"))[-1].read_text())
            self.assertNotIn("workers",json.dumps(receipt,sort_keys=True))

    def test_dry_finalise_gap_refuses_without_receipt(self):
        with tempfile.TemporaryDirectory() as td:
            kw=self.fixture(Path(td)); execute(**kw,max_chunks=1)
            with self.assertRaisesRegex(GateError,"dry-finalise gap"):
                execute(**kw,dry_finalise=True,resume=True)
            self.assertEqual(list(kw["artifacts"].glob("completeness_receipt_*.json")),[])

    def test_prior_count_refusal(self):
        with tempfile.TemporaryDirectory() as td:
            prior=Path(td)/"prior.json"; prior.write_text(json.dumps({"objids":[1]}))
            with self.assertRaisesRegex(GateError,"expected 13725.*got 1"):
                load_prior(prior)

    @patch("run_full.execute", side_effect=OutageBudgetExhausted("outage_budget_exhausted"))
    def test_cli_outage_budget_exhaustion_exits_75_with_status(self, _):
        stderr = StringIO()
        with redirect_stderr(stderr):
            rc = main(["--max-outage-minutes", "1"])
        self.assertEqual(rc, 75)
        self.assertEqual(json.loads(stderr.getvalue()), {"status": "outage_budget_exhausted"})

    def test_one_dr10_row_is_attributed_to_both_positions(self):
        # The full runner uses TAPCandidateSource's client expansion; exercise it
        # through one synthetic chunk containing two coincident inputs.
        with tempfile.TemporaryDirectory() as td:
            kw=self.fixture(Path(td));
            # First two generated positions are 15 arcsec apart; replace them by coincidence.
            with gzip.open(kw["table2"],"rt") as f: lines=f.readlines()
            lines[2]=lines[2].replace("00:40:01","00:40:00")
            with gzip.open(kw["table2"],"wt") as f:f.writelines(lines)
            execute(**kw,max_chunks=1)
            entry=json.loads((kw["artifacts"]/"checkpoint.jsonl").read_text())
            self.assertEqual(entry["client_row_count"],2)


if __name__ == "__main__": unittest.main(verbosity=2)
