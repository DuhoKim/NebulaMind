"""Fixture for the pinned driver (selection rule E3(i)): exercises the SAME code as production through an explicitly labelled
small test protocol (never reachable from the command line). Each test names the clause it exhibits."""
import sys, json, csv, unittest, tempfile, hashlib, shutil
from unittest import mock
from pathlib import Path
import numpy as np
HERE = Path(__file__).resolve().parent; sys.path.insert(0, str(HERE))
import run_configurations as rc, fourier_chirality as fc
from w_chi_vendored import synth_spiral

import subprocess
def git(cwd, *a): return subprocess.run(["git", *a], cwd=cwd, capture_output=True, text=True, check=True).stdout.strip()
def TPJ(tmp, n_tune=6, floor_tune=5, n_hold=60, floor_hold=57, label="TEST-PROTOCOL", n_fresh=7):
    """A test protocol with its OWN git repo + bare remote, so the witness path is exercised for real: the journal lives in a
    clone whose origin is a bare repo; seal() commits AND pushes (a pushed witness) unless push=False."""
    bare = tmp / "remote.git"; work = tmp / "work"; subprocess.run(["git", "init", "-q", "--bare", str(bare)], check=True)
    subprocess.run(["git", "clone", "-q", str(bare), str(work)], check=True, capture_output=True); git(work, "config", "user.email", "t@t"); git(work, "config", "user.name", "t")
    (work / "seal.jsonl").write_text(""); git(work, "add", "seal.jsonl"); git(work, "commit", "-q", "-m", "init"); git(work, "push", "-q", "-u", "origin", "HEAD:refs/heads/main")
    return rc.Protocol(n_tune=n_tune, floor_tune=floor_tune, n_hold=n_hold, floor_hold=floor_hold, n_fresh=n_fresh, label=label, seal_journal=str(work / "seal.jsonl"), witness_remote_ref="origin/main", witness_fetch=True, witness_remote_url=str(bare),
                       pool_sha256="p" * 64, exclusion_sha256="x" * 64, require_beacon=True, rule_sha256="r" * 64)
def seal(tp, operation, digest, push=True, witness=True, files=()):
    jp = Path(tp.seal_journal); work = jp.parent
    with open(jp, "a") as fh: fh.write(json.dumps({"operation": operation, "observed_digest": digest, "timestamp": "test"}) + "\n")
    git(work, "add", jp.name, *[str(Path(f).resolve().relative_to(work.resolve())) for f in files]); git(work, "commit", "-q", "-m", operation); commit = git(work, "rev-parse", "HEAD")
    if push: git(work, "push", "-q", "origin", "HEAD:refs/heads/main")
    if witness: jp.with_name(jp.name + f".witness.{operation}.json").write_text(json.dumps({"commit": commit}))
def identity(tmp, tp, tune_ids, hold_ids, sealed=True):
    """PRODUCTION-SHAPED identity (CORPUS-IDENTITY-2, integer objids, all fields the builder emits), sized to the test protocol; written INSIDE
    the test repo so the seal commit carries it (the driver requires the identity bytes to be the blob at the witnessed commit)."""
    fresh = list(range(900000, 900000 + tp.n_fresh)); work = Path(tp.seal_journal).parent
    p = work / f"identity_{tmp.name}.json"; p.write_text(json.dumps({"schema_version": "CORPUS-IDENTITY-2", "tuning_objids": [int(x) for x in tune_ids],
        "holdout_objids": [int(x) for x in hold_ids], "fresh_validation_objids": fresh, "pool_sha256": "p" * 64,
        "ordering_rule": "test", "seed_hex": "0" * 64, "split_mode": "beacon-seeded (test)", "renderability_inputs": {}, "detail": {},
        "exclude_file_sha256": "x" * 64, "beacon_record_sha256": "b" * 64, "rule_sha256": tp.rule_sha256}))
    if sealed: seal(tp, "corpus-identity-freeze", rc.sha_file(p), files=[p])
    return p
def mk_tensor(d, oid, arr):
    b = np.asarray(arr, dtype="<f4").reshape(1, 128, 128).tobytes(); (d / f"{oid}.ic6").write_bytes(b); return hashlib.sha256(b).hexdigest()
def mk_manifest(path, rows):
    with open(path, "w", newline="") as fh:
        w = csv.writer(fh); w.writerow(["objid", "g", "tensor_sha256"]); [w.writerow(r) for r in rows]
def spiral(g, i): return synth_spiral(g, 20 + (i % 5) * 3, 10 + (i % 4) * 10, 20.0, seed=900 + i)
def symmetric():
    x = np.zeros((128, 128)); x[56:72, 56:72] = 1.0; return x            # mirror-symmetric -> tie -> UNSCORED

class T(unittest.TestCase):
    def setUp(self):
        self.tmp = Path(tempfile.mkdtemp()); self.tens = self.tmp / "t"; self.tens.mkdir(); self.TP = TPJ(self.tmp)
    def tune_ok(self, rows, tag="o"):
        m = self.tmp / f"m_{tag}.csv"; mk_manifest(m, rows); ident = identity(self.tmp, self.TP, [r[0] for r in rows], [str(500000 + i) for i in range(60)])
        out = Path(self.TP.seal_journal).parent / tag; s = rc.tune(m, self.tens, out, ident, self.TP); return s, ident
    def seal_tuning(self, s, tag="o"):
        out = Path(self.TP.seal_journal).parent / tag; seal(self.TP, "tuning-freeze", s["run_root_sha256"], files=[out / "tuning_receipts.jsonl", out / "tuning_journal.jsonl", out / "selection_summary.json"])
    def hold_rows(self, start=100, ties=0, labels=None):
        rows = []
        for i in range(60):
            g = 1 if i % 2 else -1
            if labels is not None: g = labels[i]
            arr = symmetric() if i < ties else spiral(g, start + i); oid = str(500000 + i); rows.append((oid, g, mk_tensor(self.tens, oid, arr)))
        return rows
    def tearDown(self): shutil.rmtree(self.tmp)
    def rows(self, n, start=0, ties=0):
        rows = []
        for i in range(n):
            g = 1 if i % 2 else -1; arr = symmetric() if i < ties else spiral(g, start + i); oid = str(start + i)       # integer-form objids, as production
            rows.append((oid, g, mk_tensor(self.tens, oid, arr)))
        return rows
    def test_environment_enforced(self):                                   # E3(i): lock hash + live equality; stop on inequality
        rc.enforce_environment()
        with self.assertRaises(rc.DataIntegrityFail): rc.enforce_environment(expect_sha="0" * 64)
        bad = self.tmp / "lock.json"; lk = json.loads((HERE / "env_lock.json").read_text()); lk["numpy"] = "0.0.0"; bad.write_text(json.dumps(lk))
        with self.assertRaises(rc.DataIntegrityFail): rc.enforce_environment(lock_path=bad, expect_sha=rc.sha_file(bad))
    def test_manifest_size_duplicate_missing_sha_refused(self):            # §7 closed invocation: exact n, unique, present, hash-equal
        m = self.tmp / "m.csv"
        mk_manifest(m, self.rows(5));                        self.assertRaises(rc.DataIntegrityFail, rc.load_manifest, m, self.tens, 6)
        r = self.rows(6); mk_manifest(m, r[:5] + [r[0]]);    self.assertRaises(rc.DataIntegrityFail, rc.load_manifest, m, self.tens, 6)
        r = self.rows(6); r[3] = ("ghost", 1, r[3][2]); mk_manifest(m, r); self.assertRaises(rc.DataIntegrityFail, rc.load_manifest, m, self.tens, 6)
        r = self.rows(6); r[2] = (r[2][0], r[2][1], "0" * 64); mk_manifest(m, r); self.assertRaises(rc.DataIntegrityFail, rc.load_manifest, m, self.tens, 6)
        r = self.rows(6); mk_manifest(m, r); objs, mf = rc.load_manifest(m, self.tens, 6); self.assertEqual(mf["n"], 6)
        self.assertRaises(rc.DataIntegrityFail, rc.load_manifest, m, self.tens, 6, [x[0] for x in r][::-1])       # same objects, wrong order -> identity mismatch
    def test_no_floor_override_on_cli(self):                                # §7: absolute floors, no command-line override
        import argparse
        with self.assertRaises(SystemExit): rc.main(["tune", "--manifest", "x", "--tensors", "y", "--out", "o", "--identity", "i", "--floor-frac", "0"])
        with self.assertRaises(SystemExit): rc.main(["tune", "--manifest", "x", "--tensors", "y", "--out", "o"])       # --identity is required
    def test_unscored_counts_as_miss_and_floor_both_sides(self):            # agy V4: objective over fixed n; floor eligibility both sides
        s, _ = self.tune_ok(self.rows(6, ties=1), "o1")
        recs = [json.loads(l) for l in (Path(self.TP.seal_journal).parent / "o1" / "tuning_receipts.jsonl").read_text().splitlines()]
        self.assertTrue(all(r["unscored"] >= 1 for r in recs)); self.assertTrue(all(r["objective_p_val_over_n"] <= 5 / 6 for r in recs))
        self.assertTrue(all(r["eligible"] for r in recs))                    # m = 5 >= floor 5
        s2, _ = self.tune_ok(self.rows(6, start=50, ties=2), "o2")
        self.assertEqual(s2["n_eligible"], 0); self.assertIsNone(s2["winner"])   # m = 4 < 5: nothing eligible, no winner
    def test_tiebreak_levels(self):                                          # §7 tie-break: objective, then fewer unscored, then earlier index
        recs = [{"objective_p_val_over_n": .8, "unscored": 2, "config_index": 5}, {"objective_p_val_over_n": .8, "unscored": 1, "config_index": 9}, {"objective_p_val_over_n": .8, "unscored": 1, "config_index": 7}, {"objective_p_val_over_n": .7, "unscored": 0, "config_index": 0}]
        w = sorted(recs, key=lambda r: (-r["objective_p_val_over_n"], r["unscored"], r["config_index"]))[0]; self.assertEqual(w["config_index"], 7)
    def test_identity_must_be_sealed_and_match(self):                       # E3/E5: identity sealed in the journal; manifests carry exactly its objids
        rows = self.rows(6); m = self.tmp / "m.csv"; mk_manifest(m, rows)
        unsealed = identity(self.tmp, self.TP, [r[0] for r in rows], [str(500000 + i) for i in range(60)], sealed=False)
        with self.assertRaises(rc.DataIntegrityFail): rc.tune(m, self.tens, self.tmp / "u", unsealed, self.TP)
        other = self.rows(6, start=900); wrong = identity(self.tmp, self.TP, [r[0] for r in other], [str(500000 + i) for i in range(60)])
        with self.assertRaises(rc.DataIntegrityFail): rc.tune(m, self.tens, self.tmp / "w", wrong, self.TP)          # valid-looking 6 objects, not the prescribed ones
    def test_holdout_reconstructs_winner_and_refuses_coherent_substitution(self):   # codex V5: summary fields are untrusted
        s, ident = self.tune_ok(self.rows(6));         h = self.tmp / "h.csv"; mk_manifest(h, self.hold_rows())
        with self.assertRaises(rc.DataIntegrityFail): rc.holdout(Path(self.TP.seal_journal).parent / "o" / "selection_summary.json", h, self.tens, self.tmp / "ns", ident, self.TP)   # tuning not sealed yet
        self.seal_tuning(s)
        hs = rc.holdout(Path(self.TP.seal_journal).parent / "o" / "selection_summary.json", h, self.tens, self.tmp / "ho", ident, self.TP)
        ids = {json.loads(l)["config_id"] for l in (self.tmp / "ho" / "holdout_journal.jsonl").read_text().splitlines()}; self.assertEqual(ids, {s["winner_config_id"]})
        self.assertIn(hs["verdict"], ("PASS", "CLOSED: holdout strength"))
        sm = json.loads((Path(self.TP.seal_journal).parent / "o" / "selection_summary.json").read_text()); other = fc.enumerate_configs()[0 if sm["winner"]["config_index"] != 0 else 1]
        sm["winner"]["config"] = other; sm["winner"]["config_index"] = fc.enumerate_configs().index(other); sm["winner"]["config_id"] = fc.config_id(other); sm["winner_config_id"] = fc.config_id(other)
        (Path(self.TP.seal_journal).parent / "o" / "selection_summary.json").write_text(json.dumps(sm))                                  # COHERENT substitution: every winner field consistent
        with self.assertRaises(rc.DataIntegrityFail) as cm0: rc.holdout(Path(self.TP.seal_journal).parent / "o" / "selection_summary.json", h, self.tens, self.tmp / "ho2a", ident, self.TP)
        self.assertIn("NOT-IN-WITNESS-COMMIT", str(cm0.exception))                                              # first line of defence: the edited file is not the witnessed blob
        self.seal_tuning(sm)                                                                                    # operator re-seals and pushes the substituted summary...
        with self.assertRaises(rc.DataIntegrityFail) as cm: rc.holdout(Path(self.TP.seal_journal).parent / "o" / "selection_summary.json", h, self.tens, self.tmp / "ho2", ident, self.TP)
        self.assertIn("WINNER-SUBSTITUTED", str(cm.exception))                                                  # ...and reconstruction from the receipts still refuses it
    def test_holdout_refuses_receipts_fabricated_against_the_journal(self):    # agy V7 / codex V6: coherent receipt replacement + new seal must fail
        s, ident = self.tune_ok(self.rows(6)); tdir = Path(self.TP.seal_journal).parent / "o"; R = tdir / "tuning_receipts.jsonl"
        recs = [json.loads(l) for l in R.read_text().splitlines()]; loser = next(r for r in recs if r["config_id"] != s["winner_config_id"])
        loser["k"] = loser["m_scored"]; loser["k_eff"] = loser["m_scored"]; loser["objective_p_val_over_n"] = loser["m_scored"] / 6   # forge a perfect loser
        R.write_text("".join(json.dumps(r, sort_keys=True) + "\n" for r in recs))
        sm = json.loads((tdir / "selection_summary.json").read_text()); sm["receipts_sha256"] = rc.sha_file(R); sm["run_root_parts"]["tuning_receipts.jsonl"] = sm["receipts_sha256"]
        sm["run_root_sha256"] = rc.hashlib.sha256("\n".join(f"{k}:{v}" for k, v in sorted(sm["run_root_parts"].items())).encode()).hexdigest()
        sm["winner"] = loser; sm["winner_config_id"] = loser["config_id"]; (tdir / "selection_summary.json").write_text(json.dumps(sm))
        self.seal_tuning(sm)                                                                                    # operator re-seals and pushes the forged receipts + summary
        h = self.tmp / "h.csv"; mk_manifest(h, self.hold_rows())
        with self.assertRaises(rc.DataIntegrityFail) as cm: rc.holdout(tdir / "selection_summary.json", h, self.tens, self.tmp / "forged", ident, self.TP)
        self.assertIn("JOURNAL-MISMATCH", str(cm.exception))
    def test_holdout_floor_overlap_and_identity(self):                             # floor before Wilson; overlap refused; holdout manifest must match identity
        s, ident = self.tune_ok(self.rows(6)); self.seal_tuning(s)
        h = self.tmp / "h.csv"; mk_manifest(h, self.hold_rows(start=200, ties=4))
        hs = rc.holdout(Path(self.TP.seal_journal).parent / "o" / "selection_summary.json", h, self.tens, self.tmp / "hf", ident, self.TP)
        self.assertEqual(hs["verdict"], "CLOSED: holdout floor"); self.assertIsNone(hs["wilson_lower"])           # m = 56 < 57
        r = self.hold_rows(start=300); r[0] = ("0", r[0][1], r[0][2]); mk_manifest(h, r)
        with self.assertRaises(rc.DataIntegrityFail): rc.holdout(Path(self.TP.seal_journal).parent / "o" / "selection_summary.json", h, self.tens, self.tmp / "hx", ident, self.TP)   # identity mismatch (o0000 not in holdout list)
    def test_holdout_strength_closed_deterministic(self):                          # CLOSED: holdout strength is reachable and exhibited
        s, ident = self.tune_ok(self.rows(6)); self.seal_tuning(s)
        rng = np.random.default_rng(77); labels = [int(x) for x in rng.choice([1, -1], size=60)]
        rows = []                                                                                                # images of one parity, labels random -> agreement ~ 0.5
        for i in range(60): rows.append((str(500000 + i), labels[i], mk_tensor(self.tens, str(500000 + i), spiral(1, 700 + i))))
        h = self.tmp / "h.csv"; mk_manifest(h, rows)
        hs = rc.holdout(Path(self.TP.seal_journal).parent / "o" / "selection_summary.json", h, self.tens, self.tmp / "hs", ident, self.TP)
        self.assertEqual(hs["verdict"], "CLOSED: holdout strength"); self.assertGreaterEqual(hs["m_scored"], 57); self.assertLessEqual(hs["wilson_lower"], 0.70)
    def test_holdout_pass_reachable(self):                                         # PASS is reachable
        s, ident = self.tune_ok(self.rows(6)); self.seal_tuning(s)
        rows = []
        for i in range(60):
            g = 1 if i % 2 else -1; rows.append((str(500000 + i), g, mk_tensor(self.tens, str(500000 + i), synth_spiral(g, 25, 0, 50.0, seed=5000 + i))))
        h = self.tmp / "h.csv"; mk_manifest(h, rows)
        hs = rc.holdout(Path(self.TP.seal_journal).parent / "o" / "selection_summary.json", h, self.tens, self.tmp / "hp", ident, self.TP)
        self.assertEqual(hs["verdict"], "PASS"); self.assertGreater(hs["wilson_lower"], 0.70)
    def test_real_builder_output_loads_through_load_identity(self):        # END-TO-END: beacon_v2 record -> pinned builder -> driver, all on the same mocked network
        import importlib.util
        from datetime import datetime, timezone, timedelta
        spec = importlib.util.spec_from_file_location("bci", HERE.parents[1] / "_optionA_dev" / "corpus_identity" / "build_corpus_identity.py"); bci = importlib.util.module_from_spec(spec); spec.loader.exec_module(bci)
        sys.path.insert(0, str(HERE.parents[1] / "_optionA_dev" / "beacon_v2")); import beacon_record as br, test_pki as pki
        out = self.tmp / "ident_e2e"; out.mkdir(); D = "a" * 64; t_sign = datetime(2026, 9, 6, 0, 0, tzinfo=timezone.utc); tp = br.pulse_time(t_sign); now = tp + timedelta(hours=1)
        stmt = out / "statement.txt"; stmt.write_bytes(f"signed {D} at {br.fmt(t_sign)}".encode()); net = pki.network(tp)
        rec = out / "beacon_record.json"; rec.write_text(json.dumps(br.collect(net, br.fmt(t_sign), D, stmt.read_bytes(), now=now)))
        bci.nist_pulse.pinned_roots = lambda: pki.roots()                                                            # test root in place of the pinned DigiCert root
        excl = HERE.parents[1] / "_optionA_dev" / "corpus_identity" / "dryrun_identities_to_exclude_20260905.txt"
        ok = bci.build(out_dir=out, beacon_record_path=rec, exclude_path=excl, rule_sha256=D, signature_statement=stmt, fetch=net, now=now); self.assertTrue(ok)
        e2e = self.tmp / "e2e_repo"; e2e.mkdir(); prod_like = TPJ(e2e, n_tune=400, floor_tune=380, n_hold=200, floor_hold=190, label="E2E-TEST", n_fresh=2000)
        prod_like = rc.Protocol(**{**prod_like.__dict__, "pool_sha256": rc.PRODUCTION.pool_sha256, "exclusion_sha256": rc.PRODUCTION.exclusion_sha256, "rule_sha256": D})
        work = Path(prod_like.seal_journal).parent; ident_in_repo = work / "corpus_identity.json"; ident_in_repo.write_bytes((out / "corpus_identity.json").read_bytes())
        with self.assertRaises(rc.DataIntegrityFail): rc.load_identity(ident_in_repo, prod_like)                     # unsealed -> refused
        seal(prod_like, "corpus-identity-freeze", rc.sha_file(ident_in_repo), files=[ident_in_repo])
        I, d = rc.load_identity(ident_in_repo, prod_like)
        self.assertEqual((len(I["tuning_objids"]), len(I["holdout_objids"]), len(I["fresh_validation_objids"])), (400, 200, 2000)); self.assertEqual(I["beacon_outcome"], "ACCEPT-NIST")
        self.assertTrue(all(isinstance(x, int) for x in I["tuning_objids"])); self.assertEqual(I["beacon_record_sha256"], rc.sha_file(rec)); self.assertTrue(I["split_mode"].startswith("beacon-seeded"))
        bad = json.loads(ident_in_repo.read_text()); bad["split_mode"] = "TEST-SEED (not for production)"; p2 = work / "test_seed_identity.json"; p2.write_text(json.dumps(bad)); seal(prod_like, "corpus-identity-freeze", rc.sha_file(p2), files=[p2])
        with self.assertRaises(rc.DataIntegrityFail): rc.load_identity(p2, prod_like)                                        # a test-seed identity is refused in production mode
    def test_witness_requires_pushed_commit_containing_record(self):            # both V6 seats: the journal alone is not a witness
        rows = self.rows(6); m = self.tmp / "m.csv"; mk_manifest(m, rows)
        ident = identity(self.tmp, self.TP, [r[0] for r in rows], [str(500000 + i) for i in range(60)], sealed=False); d = rc.sha_file(ident)
        seal(self.TP, "corpus-identity-freeze", d, push=False, files=[ident])                                  # committed locally, NOT pushed
        with self.assertRaises(rc.DataIntegrityFail) as cm: rc.tune(m, self.tens, self.tmp / "np", ident, self.TP)
        self.assertIn("WITNESS-NOT-PUSHED", str(cm.exception))
        git(Path(self.TP.seal_journal).parent, "push", "-q", "origin", "HEAD:refs/heads/main")                 # now pushed -> accepted
        s = rc.tune(m, self.tens, Path(self.TP.seal_journal).parent / "p", ident, self.TP); self.assertEqual(s["identity_witness"]["remote_ref"], "origin/main")
        wf = Path(self.TP.seal_journal + ".witness.corpus-identity-freeze.json"); wf.write_text(json.dumps({"commit": "0" * 40}))
        with self.assertRaises(rc.DataIntegrityFail): rc.tune(m, self.tens, self.tmp / "bad", ident, self.TP)   # a commit that does not exist / lacks the record
        wf.unlink()
        with self.assertRaises(rc.DataIntegrityFail): rc.tune(m, self.tens, self.tmp / "nw", ident, self.TP)    # no witness file at all
    def test_witness_refuses_redirected_remote(self):                            # agy V8: origin pointed at a fake bare repo must be refused
        rows = self.rows(6); m = self.tmp / "m.csv"; mk_manifest(m, rows); ident = identity(self.tmp, self.TP, [r[0] for r in rows], [str(500000 + i) for i in range(60)])
        work = Path(self.TP.seal_journal).parent; fake = self.tmp / "fake.git"; subprocess.run(["git", "init", "-q", "--bare", str(fake)], check=True)
        git(work, "remote", "set-url", "origin", str(fake)); git(work, "push", "-q", "origin", "HEAD:refs/heads/main")
        with self.assertRaises(rc.DataIntegrityFail) as cm: rc.tune(m, self.tens, self.tmp / "redir", ident, self.TP)
        self.assertIn("WITNESS-REMOTE-URL", str(cm.exception))
    def test_environment_records_fft_and_threads(self):                            # E2 scope: fft binary + thread env in the observed environment
        e = rc.observed_env(); self.assertIn("numpy_fft_sha256", e); self.assertTrue(all(v == "1" for v in e["thread_env"].values()))
    def test_production_constants(self):                                     # §7 numbers are literals in the driver
        self.assertEqual((rc.PRODUCTION.n_tune, rc.PRODUCTION.floor_tune, rc.PRODUCTION.n_hold, rc.PRODUCTION.floor_hold), (400, 380, 200, 190))
        self.assertEqual(rc.THRESHOLD, 0.70); self.assertEqual(rc.Z, 1.959963984540054)
    def test_estimator_rejects_extra_keys(self):
        bad = dict(fc.DEFAULT_CFG); bad["EXTRA"] = 1
        with self.assertRaises(ValueError): fc.Estimator(bad)

if __name__ == "__main__":
    unittest.main()
