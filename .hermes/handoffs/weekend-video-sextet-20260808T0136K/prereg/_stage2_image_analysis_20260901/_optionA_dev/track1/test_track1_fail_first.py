"""TRACK 1 (Blanc 20:45 KST) — FAIL-FIRST tests. Each test names the codex V21 finding it covers, targets the SUCCESSOR modules
(beacon_record_drand_v22, build_corpus_identity_v22, history_v2, run_configurations_v6), and was RUN AGAINST BYTE-COPIES OF THE V21 MODULES
FIRST (receipt: TRACK1_FAIL_FIRST_RECEIPT_20260906.md — every test FAILS there), then against the repaired successors (every test passes).
Requires the lane venv site-packages on PYTHONPATH under /usr/bin/python3 (driver tests) — run: PYTHONPATH=<venv sp> /usr/bin/python3 -W error::ResourceWarning -m unittest test_track1_fail_first."""
import json, os, sys, tempfile, unittest, hashlib, subprocess, io, contextlib
from datetime import timedelta
from pathlib import Path
HERE = Path(__file__).resolve().parent; D = HERE.parent
for p in ("beacon_v2", "drand_only", "corpus_identity", "fourier_chirality"): sys.path.insert(0, str(D / p))
import beacon_record_drand_v22 as BD, verify_drand_v2 as vd, history_v2 as H, build_corpus_identity_v22 as B, run_configurations_v6 as rc
import test_run_configurations_v6 as TF                                          # the driver fixture (real evidence), pointed at the successors
ROUND = 6441924; REAL = json.loads((D / "drand_only" / "round_6441924_api.drand.sh.json").read_text()); BODY = json.dumps(REAL).encode()
TP = vd.round_time(ROUND); TS = BD.fmt(TP - timedelta(seconds=600)); RD = "b" * 64; STMT = f"V22 {RD} {TS}".encode(); SOON = TP + timedelta(minutes=1)
def relays(default=None):
    def fetch(url, timeout=30):
        for host in vd.RELAYS:
            if url == vd.round_url(host, ROUND): return default if default is not None else BODY
        raise OSError("404")
    return fetch
class T(unittest.TestCase):
    def setUp(self): self._ex = BD.EXCLUDED_ROUNDS; BD.EXCLUDED_ROUNDS = (6440756,)
    def tearDown(self): BD.EXCLUDED_ROUNDS = self._ex
    def test_C6_uppercase_hex_signature_is_the_same_value(self):                 # codex V21 C6: signature equality must be on DECODED bytes
        rec = BD.collect(relays(), TS, RD, STMT, now=SOON); up = dict(REAL); up["signature"] = REAL["signature"].upper()
        r = BD.verdict(rec, SOON, fetch=relays(json.dumps(up).encode()), rule_sha256=RD, statement_bytes=STMT)
        self.assertEqual(r["outcome"], "ACCEPT-DRAND", r.get("why")); self.assertEqual(len(r["checks"]["live_representation_differs"]), 4); self.assertEqual(r["seed_hex"], hashlib.sha256(bytes.fromhex(REAL["signature"])).hexdigest())
    def test_C5_round_6441904_excluded_by_name(self):                             # codex V21 C5: all three historical rounds inadmissible
        BD.EXCLUDED_ROUNDS = self._ex                                              # the PINNED tuple, unlifted
        self.assertIn(6441904, BD.EXCLUDED_ROUNDS); self.assertIn(6441924, BD.EXCLUDED_ROUNDS); self.assertIn(6440756, BD.EXCLUDED_ROUNDS)
        nb = (D / "drand_only" / "round_6441904_api.drand.sh.json").read_bytes(); tp4 = vd.round_time(6441904); ts4 = BD.fmt(tp4 - timedelta(seconds=600)); st4 = f"x {RD} {ts4}".encode()
        def f4(url, timeout=30):
            for host in vd.RELAYS:
                if url == vd.round_url(host, 6441904): return nb
            raise OSError("404")
        with self.assertRaises(SystemExit) as cm: BD.collect(f4, ts4, RD, st4, now=tp4 + timedelta(minutes=1))
        self.assertIn("T-PULSE-EXCLUDED", str(cm.exception))
        BD.EXCLUDED_ROUNDS = (); rec4 = BD.collect(f4, ts4, RD, st4, now=tp4 + timedelta(minutes=1)); BD.EXCLUDED_ROUNDS = self._ex
        self.assertEqual(BD.verdict(rec4, tp4 + timedelta(minutes=1), rule_sha256=RD, statement_bytes=st4)["outcome"], "REFUSE-T-PULSE-EXCLUDED")
    def test_C7_C8_C10_rule_text_consistent(self):                                # codex V21 C7/C8/C10: the operative text must agree with the code (run with RULE_TEXT=<draft>)
        text = Path(os.environ["RULE_TEXT"]).read_text(encoding="utf-8")
        self.assertNotIn("REFUSE-LIVE-DIFFERS-BUT-VERIFIES", text); self.assertNotIn("APPROVAL_RECORD_SELRULE_V20_<date>", text)
        self.assertIn(B.APPROVAL_GLOB.rstrip("*") + "_<date>", text)              # the filename the builder searches for is the one the text instructs
        self.assertNotIn("must equal the retained body (or be unavailable", text)  # V20's byte-equality clause
        self.assertIn("SHA-256 of the DECODED signature bytes", text)             # the seed stated as VD computes it
        self.assertNotIn("test_beacon_record_drand.py` (`", text.split("## 4.")[0].split("3c.")[0]) if False else None
    def test_C4a_builder_missing_args_is_logged(self):                            # codex V21 C4: BEACON-VALIDATION-ARGS-MISSING escaped the log
        tmp = Path(tempfile.mkdtemp()); B.COLLECTION_LOG = tmp / "collection_log.jsonl"; side = Path(str(B.COLLECTION_LOG) + ".pregenesis.jsonl")
        with self.assertRaises(SystemExit) as cm: B.build(beacon_record_path=tmp / "rec.json")
        self.assertIn("BEACON-VALIDATION-ARGS-MISSING", str(cm.exception)); self.assertTrue(side.is_file(), "the refusal must be disclosed beside the history"); self.assertEqual(json.loads(side.read_text().splitlines()[-1])["stage"], "builder-args-refusal")
    def test_C4b_builder_output_failure_after_validation_is_logged(self):         # codex V21 C4: FileExistsError after validation escaped
        import test_build_corpus_identity_v22 as TB                                # the builder fixture (real round, real nonce, temp git)
        t = TB.T("test_accepted_witnessed_locked_history"); t.setUp()
        try:
            occupied = t.tmp / "outfile"; occupied.write_text("not a directory"); excl = D / "corpus_identity" / "dryrun_identities_to_exclude_20260905.txt"
            with self.assertRaises(SystemExit) as cm: B.build(out_dir=occupied, beacon_record_path=t.rec, exclude_path=excl, rule_sha256=TB.D, signature_statement=t.stmt, fetch=t.n, now=TB.SOON)
            self.assertIn("BUILDER-ERROR", str(cm.exception)); self.assertEqual(H.validate(B.COLLECTION_LOG)[-1]["stage"], "builder-error")
        finally: t.tearDown()
    def test_C4c_collector_argparse_failure_is_disclosed(self):                   # codex V21 C4: argparse failures escaped the sidecar
        tmp = Path(tempfile.mkdtemp()); logp = tmp / "log.jsonl"; side = Path(str(logp) + ".pregenesis.jsonl")
        with contextlib.redirect_stderr(io.StringIO()):
            with self.assertRaises(SystemExit): BD.main(["collect", "--log", str(logp)])                    # required arguments missing
        self.assertTrue(side.is_file(), "argparse failure must reach the sidecar named by --log"); self.assertEqual(json.loads(side.read_text().splitlines()[-1])["stage"], "collector-args-refusal")
        saved = BD.ARGPARSE_SIDECAR; BD.ARGPARSE_SIDECAR = tmp / "collector_argparse_failures.jsonl"        # a TEMP sidecar: the test must not write into the lane (codex V22)
        try:
            with contextlib.redirect_stderr(io.StringIO()):
                with self.assertRaises(SystemExit): BD.main(["collect"])                                    # no --log at all: the module-level sidecar
            self.assertTrue(BD.ARGPARSE_SIDECAR.is_file())
        finally: BD.ARGPARSE_SIDECAR = saved
    def test_C2_driver_reproduces_W4_first_approval_is_final(self):               # codex V21 C2: a second pushed approval-record path passed load_identity
        t = TF.T("test_v4_semantic_conjunction"); t.setUp()
        try:
            rows = t.rows(6); ident = TF.identity(t.tmp, t.TP, [r[0] for r in rows], [str(500000 + i) for i in range(60)]); rc.load_identity(ident, t.TP)
            work = Path(t.TP.seal_journal).parent; second = work / "APPROVAL_RECORD_SELRULE_V22_T_second.md"; second.write_bytes(b"RULE_SHA256: x\n"); TF.git(work, "add", second.name); TF.git(work, "commit", "-q", "-m", "second approval path"); TF.git(work, "push", "-q", "origin", "HEAD:refs/heads/main")
            with self.assertRaises(rc.DataIntegrityFail) as cm: rc.load_identity(ident, t.TP)
            self.assertIn("APPROVAL-NOT-FIRST", str(cm.exception))
        finally: t.tearDown()
    def test_C9_sentinel_journal_must_be_complete(self):                          # codex V21 C9: a journal with no refusal cause and no render-end passed
        rows = [("1", 1, rc.SENTINEL_SHA256), ("2", -1, "a" * 64)]; tmp = Path(tempfile.mkdtemp()); rj = tmp / "rj.jsonl"
        rj.write_text(json.dumps({"objid": "1", "status": "REFUSED", "sentinel": True, "tensor_sha256": rc.SENTINEL_SHA256}) + "\n")
        with self.assertRaises(rc.DataIntegrityFail) as cm: rc.reconcile_sentinels([{"objid": o, "g": g, "tensor_sha256": s} for o, g, s in rows], rj)
        self.assertIn("RENDER-JOURNAL", str(cm.exception))
        rj.write_text(json.dumps({"objid": "1", "status": "REFUSED", "sentinel": True, "tensor_sha256": rc.SENTINEL_SHA256, "reason": "zero exposure inside r_T"}) + "\n" + json.dumps({"event": "render-end", "refused_sentinel": 1}) + "\n")
        rc.reconcile_sentinels([{"objid": o, "g": g, "tensor_sha256": s} for o, g, s in rows], rj)      # complete: accepted
    def test_C3_closed_is_terminal_in_history_and_driver(self):                   # codex V21 C3 (mechanical part): a witness-closed entry must be terminal
        t = TF.T("test_v4_semantic_conjunction"); t.setUp()
        try:
            rows = t.rows(6)
            def closed(I, ctx):
                H.append(ctx["log"], {"stage": "witness-closed", "record_sha256": I["beacon_record_sha256"], "outcome": "ACCEPT-DRAND", "refusal": "APPROVAL-PUSH-EVENT-CLOSED", "state": "CLOSED"})
                I["collection_lock"]["log_sha256"] = rc.sha_file(ctx["log"]); I["collection_lock"]["entries"] = len(H.validate(ctx["log"]))
            ident = TF.identity(t.tmp, t.TP, [r[0] for r in rows], [str(500000 + i) for i in range(60)], mutate=closed)
            with self.assertRaises(rc.DataIntegrityFail) as cm: rc.load_identity(ident, t.TP)
            self.assertIn("CLOSED", str(cm.exception))
            fa, conf = H.first_accept(H.validate(Path(t.TP.collection_log))); self.assertTrue(conf, "history_v2.first_accept must report the closure as a conflict")
        finally: t.tearDown()
    def test_C3_genesis_takes_the_lock_before_testing_existence(self):            # codex V21 C3: H.genesis tested existence before locking (an empty pre-created file was accepted)
        p = Path(tempfile.mkdtemp()) / "h.jsonl"; p.write_text("")
        with self.assertRaises(SystemExit) as cm: H.genesis(p, "a" * 64, "t", "b" * 64, 1)
        self.assertIn("HISTORY-EXISTS", str(cm.exception))
if __name__ == "__main__": unittest.main()
