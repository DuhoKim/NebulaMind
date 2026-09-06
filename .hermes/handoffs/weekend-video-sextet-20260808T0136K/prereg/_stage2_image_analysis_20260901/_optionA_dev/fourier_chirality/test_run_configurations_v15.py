"""Fixture for the STAGED driver v15 (V31 candidate; NOT GATED, NOT ADOPTED): composed mode on provenance_designs_v11 — the fixture text below is inherited unchanged from the v8 fixture (V24) onward; only the import lines changed at each successor. It was — Fixture for the STAGED driver v8 (V24 candidate; NOT GATED, NOT ADOPTED): composed mode on provenance_designs_v4 — one fixture PushEvent per published history commit (before = parent). Earlier fixture text follows.
Fixture for the STAGED driver v6 (V22 candidate; NOT GATED, NOT ADOPTED). v6 fixture: ONE approval commit per repository (W4 is enforced by the driver now; the v5 fixture's per-call approval records masked it — codex V21 C2); render-journal entries carry a refusal cause and a render-end. v5 fixture text follows.
Fixture for the pinned driver v5 (selection rule E3(i)): exercises the SAME code as production through an explicitly labelled small test
protocol built FROM PRODUCTION's own field values (paths, sizes and pinned digests overridden ONLY — the re-deriver is PRODUCTION's function;
no callback substitution; codex V20 FATAL). The identity fixture carries REAL evidence: a committed approval record + adoption file at one
approval commit, a real BEACON-RECORD-4 for the public round 6441924 (BLS-verified; the exhibit-round exclusion lifted inside the fixture only),
a real BLS-verified nonce (round 6441904, pinned bodies), an authenticated history (genesis → collector → builder-accept), a PushEvent with its
canonical digest and provenance. Each test names the clause it exhibits. Requires py_ecc (lane venv site-packages on PYTHONPATH)."""
import sys, json, csv, unittest, tempfile, hashlib, shutil
from unittest import mock
from pathlib import Path
import numpy as np
HERE = Path(__file__).resolve().parent; sys.path.insert(0, str(HERE))
import run_configurations_v15 as rc, fourier_chirality as fc
from w_chi_vendored import synth_spiral

import subprocess
def git(cwd, *a): return subprocess.run(["git", *a], cwd=cwd, capture_output=True, text=True, check=True).stdout.strip()
import base64
from datetime import timedelta, datetime, timezone
sys.path.insert(0, str(HERE.parent / "beacon_v2")); sys.path.insert(0, str(HERE.parent / "drand_only")); sys.path.insert(0, str(HERE.parent / "corpus_identity"))
import beacon_record_drand_v31 as BD, verify_drand_v2 as vd, history_v2 as H
ROUND = 6441924; NR = 6441904; DO = HERE.parent / "drand_only"; REAL = json.loads((DO / "round_6441924_api.drand.sh.json").read_text()); BODY = json.dumps(REAL).encode()
NB = {h: (DO / f"round_6441904_{h.split('//')[1]}.json").read_bytes() for h in ("https://api.drand.sh", "https://api2.drand.sh")}; NONCE = json.loads(NB["https://api.drand.sh"])["randomness"]
TP = vd.round_time(ROUND); T_SIGN = TP - timedelta(seconds=600); TS = BD.fmt(T_SIGN); TPS = BD.fmt(TP); SEED = REAL["randomness"]; D = "c" * 64
assert vd.round_for(T_SIGN) == NR
def net(url, timeout=30):
    for h, b in NB.items():
        if url == vd.round_url(h, NR): return b
    for host in vd.RELAYS:
        if url == vd.round_url(host, ROUND): return BODY
    raise OSError("404 " + url)
def TPJ(tmp, n_tune=6, floor_tune=5, n_hold=60, floor_hold=57, label="TEST-PROTOCOL", n_fresh=7):
    """A test protocol = PRODUCTION's own values with paths/sizes/pinned digests overridden; its OWN git repo + bare remote, so the witness path
    is exercised for real: the journal lives in a clone whose origin is a bare repo; seal() commits AND pushes unless push=False."""
    bare = tmp / "remote.git"; work = tmp / "work"; subprocess.run(["git", "init", "-q", "--bare", str(bare)], check=True)
    subprocess.run(["git", "clone", "-q", str(bare), str(work)], check=True, capture_output=True); git(work, "config", "user.email", "t@t"); git(work, "config", "user.name", "t")
    (work / "seal.jsonl").write_text(""); git(work, "add", "seal.jsonl"); git(work, "commit", "-q", "-m", "init"); git(work, "push", "-q", "-u", "origin", "HEAD:refs/heads/main")
    rc.ADOPTION_FILE = work / "ADOPTED_RULE_SHA256.txt"; rc.ADOPTION_FILE.write_text(D + "\n")
    return rc.Protocol(**{**rc.PRODUCTION.__dict__, "n_tune": n_tune, "floor_tune": floor_tune, "n_hold": n_hold, "floor_hold": floor_hold, "n_fresh": n_fresh, "label": label, "seal_journal": str(work / "seal.jsonl"), "collection_log": str(work / "collection_log.jsonl"), "witness_branch_ref": "refs/heads/main", "adoption_file": str(work / "ADOPTED_RULE_SHA256.txt"), "beacon_record_path": str(work / "beacon_record.json"), "witness_remote_ref": "origin/main", "witness_fetch": True, "witness_remote_url": str(bare),
                          "pool_sha256": "p" * 64, "exclusion_sha256": "x" * 64, "require_beacon": True, "rule_sha256": D, "render_journal": str(tmp / "render_journal_{group}.jsonl"), "holdout_marker": str(tmp / "HOLDOUT_INVOKED.marker")})
def seal(tp, operation, digest, push=True, witness=True, files=()):
    jp = Path(tp.seal_journal); work = jp.parent
    with open(jp, "a") as fh: fh.write(json.dumps({"operation": operation, "observed_digest": digest, "timestamp": "test"}) + "\n")
    git(work, "add", jp.name, *[str(Path(f).resolve().relative_to(work.resolve())) for f in files]); git(work, "commit", "-q", "-m", operation); commit = git(work, "rev-parse", "HEAD")
    if push: git(work, "push", "-q", "origin", "HEAD:refs/heads/main")
    if witness: jp.with_name(jp.name + f".witness.{operation}.json").write_text(json.dumps({"commit": commit}))
_APPROVAL = {}
def approval_commit(work, tp, adoption_ok=True):
    """ONE approval commit per repository: the approval record + the adoption file, committed together and pushed; cached per repo (v6)."""
    key = str(work)
    if key in _APPROVAL: return _APPROVAL[key]
    stmt = work / "APPROVAL_RECORD_SELRULE_V22_T.md"; stmt_bytes = f"RULE_SHA256: {D}\nAPPROVAL_UTC: {TS}\nDRAND_AT_APPROVAL: round {NR} randomness {NONCE}\n".encode(); stmt.write_bytes(stmt_bytes)
    ap = Path(tp.adoption_file); ap.write_text(tp.rule_sha256 + ("\n" if adoption_ok else "\n\n")); base = git(work, "rev-parse", "HEAD")
    git(work, "add", ap.name, stmt.name); git(work, "commit", "-q", "-m", "approval"); commit = git(work, "rev-parse", "HEAD"); git(work, "push", "-q", "origin", "HEAD:refs/heads/main")
    _APPROVAL[key] = (commit, stmt, stmt_bytes, base); return _APPROVAL[key]
def identity(tmp, tp, tune_ids, hold_ids, sealed=True, outcome="ACCEPT-DRAND", push_at=None, t_pulse=None, lock_ok=True, log_ok=True, witness=True, source="drand-mainnet-default", seed_ok=True, adoption_ok=True, conflict=False, mutate=None, seal_files=None, nonce_ok=True, ancestry=False):
    """PRODUCTION-SHAPED identity + REAL V22 evidence (see the module docstring). Knobs fabricate ONE defect each; `mutate(I, ctx)` edits the identity
    dict before sealing; `seal_files` overrides what the freeze commit carries. The exhibit-round exclusion is lifted for the fixture only. adoption_ok=False
    needs a FRESH repository (the approval commit is created once per repo)."""
    fresh = list(range(900000, 900000 + tp.n_fresh)); work = Path(tp.seal_journal).parent; push_at = push_at or BD.fmt(TP - timedelta(minutes=3)); t_pulse = t_pulse or TPS
    commit, stmt, stmt_bytes, base = approval_commit(work, tp, adoption_ok); ap = Path(tp.adoption_file)
    if ancestry: (work / "later").write_text("y"); git(work, "add", "later"); git(work, "commit", "-q", "-m", "later")
    head = git(work, "rev-parse", "HEAD"); git(work, "push", "-q", "origin", "HEAD:refs/heads/main")
    saved = BD.EXCLUDED_ROUNDS; BD.EXCLUDED_ROUNDS = (6440756,)
    try: rec = BD.collect(net, TS, D, stmt_bytes, now=TP + timedelta(minutes=1))
    finally: BD.EXCLUDED_ROUNDS = saved
    rp = Path(tp.beacon_record_path); rp.write_text(json.dumps(rec, indent=1, sort_keys=True)); recsha = rc.sha_file(rp); seed = SEED if seed_ok else "f" * 64
    log = Path(tp.collection_log); log.unlink(missing_ok=True); H.genesis(log, hashlib.sha256(stmt_bytes).hexdigest(), TPS, D, ROUND)
    H.append(log, {"stage": "collector-collect", "record_sha256": recsha, "outcome": outcome, "seed_hex": seed, "source": source})
    H.append(log, {"stage": "builder-verdict", "record_sha256": recsha, "outcome": outcome, "seed_hex": seed, "source": source})
    H.append(log, {"stage": "builder-accept", "record_sha256": recsha if lock_ok else "c" * 64, "outcome": outcome, "seed_hex": seed, "source": source})
    if conflict: H.append(log, {"stage": "builder-conflict", "record_sha256": "d" * 64, "outcome": "ACCEPT-DRAND", "seed_hex": "1" * 64})
    entries = H.validate(log); fa = [e for e in entries if e["stage"] == "builder-accept"][0]; log_sha = rc.sha_file(log)
    pay = {"ref": "refs/heads/main", "head": commit, "commits": [{"sha": commit}]} if not ancestry else {"ref": "refs/heads/main", "before": base, "head": head, "commits": [{"sha": head}]}
    ev = {"type": "PushEvent", "id": "1", "created_at": push_at, "payload": pay}
    nb = {vd.round_url(h, NR): base64.b64encode(b if nonce_ok else json.dumps({**json.loads(b), "signature": "00"}).encode()).decode() for h, b in NB.items()}
    I = {"schema_version": "CORPUS-IDENTITY-2", "tuning_objids": [int(x) for x in tune_ids], "holdout_objids": [int(x) for x in hold_ids], "fresh_validation_objids": fresh, "pool_sha256": "p" * 64,
         "ordering_rule": "test", "seed_hex": seed, "split_mode": "beacon-seeded (test)", "renderability_inputs": {}, "detail": {}, "exclude_file_sha256": "x" * 64, "beacon_record_sha256": recsha, "rule_sha256": tp.rule_sha256,
         "beacon_outcome": outcome, "beacon_source": source, "beacon_t_pulse": t_pulse, "beacon_round": ROUND, "T_sign": TS, "T_pulse": t_pulse, "adoption_sha256": rc.sha_file(ap), "collection_lock": {"first_accept": fa, "log_sha256": log_sha if log_ok else "0" * 64, "entries": len(entries)}}
    if witness: I["approval_witness"] = {"witness_version": 4, "commit": commit, "record_path": stmt.name, "record_sha256": hashlib.sha256(stmt_bytes).hexdigest(), "push_event": ev, "push_event_sha256": hashlib.sha256(json.dumps(ev, sort_keys=True, separators=(",", ":")).encode()).hexdigest(), "events_provenance": {"endpoints": ["e"], "retrieved_utc": "x"}, "nonce_round": NR, "nonce_randomness": NONCE, "nonce_bodies_b64": nb}
    if mutate: mutate(I, {"work": work, "commit": commit, "stmt": stmt, "rp": rp, "log": log})
    p = work / f"identity_{tmp.name}.json"; p.write_text(json.dumps(I))
    if sealed: seal(tp, "corpus-identity-freeze", rc.sha_file(p), files=[p, log, rp] if seal_files is None else seal_files(p, log, rp))
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
        self._ex = BD.EXCLUDED_ROUNDS; BD.EXCLUDED_ROUNDS = (6440756,)                       # the exhibit round is admissible ONLY inside this fixture (never a study seed)
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
    def tearDown(self): shutil.rmtree(self.tmp); BD.EXCLUDED_ROUNDS = self._ex
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
    def test_real_builder_output_loads_through_load_identity(self):        # END-TO-END (V21): real public round (BLS-verified) -> collector CLI (genesis) -> V21 builder -> driver v5 with PRODUCTION's re-deriver
        import subprocess, importlib
        from datetime import datetime, timezone, timedelta
        sys.path.insert(0, str(HERE.parents[1] / "_optionA_dev" / "beacon_v2")); sys.path.insert(0, str(HERE.parents[1] / "_optionA_dev" / "corpus_identity")); sys.path.insert(0, str(HERE.parents[1] / "_optionA_dev" / "drand_only"))
        try: import py_ecc  # noqa
        except ImportError: self.skipTest("py_ecc not importable in this interpreter (run under _optionA_dev/_venv_bls)")
        import build_corpus_identity_v31 as B20
        tp = TP; t_sign = T_SIGN; ts = TS; now = tp + timedelta(minutes=1); D = "a" * 64
        try:
            e2e = self.tmp / "e2e_repo"; e2e.mkdir(); prod_like = TPJ(e2e, n_tune=400, floor_tune=380, n_hold=200, floor_hold=190, label="E2E-TEST", n_fresh=2000)
            work = Path(prod_like.seal_journal).parent; bare = prod_like.witness_remote_url; r_sign = NR; nonce = NONCE
            stmt = work / "APPROVAL_RECORD_SELRULE_V22_E2E.md"; stmt.write_bytes(f"RULE_SHA256: {D}\nAPPROVAL_UTC: {ts}\nDRAND_AT_APPROVAL: round {r_sign} randomness {nonce}\n".encode())
            B20.ADOPTION_FILE = work / "ADOPTED_RULE_SHA256.txt"; B20.ADOPTION_FILE.write_text(D + "\n"); rc.ADOPTION_FILE = B20.ADOPTION_FILE
            git(work, "add", stmt.name, "ADOPTED_RULE_SHA256.txt"); git(work, "commit", "-q", "-m", "approval"); commit = git(work, "rev-parse", "HEAD"); git(work, "push", "-q", "origin", "HEAD:refs/heads/main")
            B20.WITNESS_REMOTE_REF = "origin/main"; B20.WITNESS_REMOTE_URL = bare; B20.APPROVAL_GLOB = "APPROVAL_RECORD_SELRULE_V22*"; B20.WITNESS_FETCH = True; B20.BRANCH_REF = "refs/heads/main"; B20.COLLECTION_LOG = Path(prod_like.collection_log)
            B20.EVENTS = lambda: ([{"type": "PushEvent", "id": "1", "created_at": (tp - timedelta(minutes=3)).strftime("%Y-%m-%dT%H:%M:%SZ"), "payload": {"ref": "refs/heads/main", "head": commit, "commits": [{"sha": commit}]}}], {"endpoints": ["e"], "retrieved_utc": "x", "gh_version": "gh test"})
            rec = Path(prod_like.beacon_record_path)
            import urllib.request, io
            class _R(io.BytesIO):
                def __enter__(self): return self
                def __exit__(self, *a): return False
            with mock.patch.object(BD, "datetime") as dt, mock.patch.object(urllib.request, "urlopen", lambda url, timeout=30: _R(net(url))):       # the collector CLI: genesis + collect, chained
                dt.now.return_value = now; dt.strptime = datetime.strptime
                self.assertEqual(BD.main(["collect", "--t-sign", ts, "--rule-sha256", D, "--signature-statement", str(stmt), "--out", str(rec), "--log", prod_like.collection_log]), 0)
            out = work / "ident_e2e"; out.mkdir(); excl = HERE.parents[1] / "_optionA_dev" / "corpus_identity" / "dryrun_identities_to_exclude_20260905.txt"
            ok = B20.build(out_dir=out, beacon_record_path=rec, exclude_path=excl, rule_sha256=D, signature_statement=stmt, fetch=net, now=now); self.assertTrue(ok)
            prod_like = rc.Protocol(**{**prod_like.__dict__, "pool_sha256": rc.PRODUCTION.pool_sha256, "exclusion_sha256": rc.PRODUCTION.exclusion_sha256, "rule_sha256": D})   # the re-deriver stays PRODUCTION's
            self.assertIs(prod_like.rederive_seed, rc.production_rederive_seed)
            ident = out / "corpus_identity.json"; I = json.loads(ident.read_text()); self.assertEqual(I["beacon_outcome"], "ACCEPT-DRAND"); self.assertEqual(I["seed_hex"], REAL["randomness"]); self.assertEqual(I["beacon_round"], ROUND)
            seal(prod_like, "corpus-identity-freeze", rc.sha_file(ident), files=[ident, Path(prod_like.collection_log), rec])
            Iw, d = rc.load_identity(ident, prod_like); self.assertEqual(len(Iw["tuning_objids"]), 400); self.assertEqual(Iw["approval_witness"]["witness_version"], 4)
            split_on = rc.Protocol(**{**prod_like.__dict__, "verify_split": True})                     # UNADOPTED staged check: the real builder output reproduces from the catalogue
            rc.load_identity(ident, split_on)
            Ibad = json.loads(ident.read_text()); Ibad["tuning_objids"][0], Ibad["tuning_objids"][1] = Ibad["tuning_objids"][1], Ibad["tuning_objids"][0]; bad = out / "corpus_identity_swapped.json"; bad.write_text(json.dumps(Ibad, sort_keys=True, separators=(",", ":")) + "\n")
            seal(prod_like, "corpus-identity-freeze", rc.sha_file(bad), files=[bad])
            rc.load_identity(bad, prod_like)                                                          # the DEFAULT driver accepts a swapped (coherently sealed) list — the inherited limitation, stated
            with self.assertRaises(rc.DataIntegrityFail) as cm: rc.load_identity(bad, split_on)
            self.assertIn("SPLIT-NOT-REPRODUCED", str(cm.exception))
        finally: pass
    def test_witness_requires_pushed_commit_containing_record(self):            # both V6 seats: the journal alone is not a witness
        rows = self.rows(6); m = self.tmp / "m.csv"; mk_manifest(m, rows)
        ident = identity(self.tmp, self.TP, [r[0] for r in rows], [str(500000 + i) for i in range(60)], sealed=False); d = rc.sha_file(ident)
        seal(self.TP, "corpus-identity-freeze", d, push=False, files=[ident, Path(self.TP.collection_log), Path(self.TP.beacon_record_path)])   # committed locally, NOT pushed
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

    def test_adoption_binding_fails_closed(self):                              # v2/v3: no adoption file → no identity load; wrong digest → refused
        rows = self.rows(6); m = self.tmp / "m.csv"; mk_manifest(m, rows); ident = identity(self.tmp, self.TP, [r[0] for r in rows], [str(500000 + i) for i in range(60)])
        rc.ADOPTION_FILE.unlink()
        with self.assertRaises(rc.DataIntegrityFail) as cm: rc.tune(m, self.tens, self.tmp / "noadopt", ident, self.TP)
        self.assertIn("ADOPTION-MISSING", str(cm.exception))
        rc.ADOPTION_FILE.write_text("a" * 64 + "\n")
        with self.assertRaises(rc.DataIntegrityFail) as cm: rc.tune(m, self.tens, self.tmp / "wrongadopt", ident, self.TP)
        self.assertIn("ADOPTION-MISMATCH", str(cm.exception)); rc.ADOPTION_FILE.write_text("c" * 64 + "\n")
    def test_sentinel_tensor_is_counted_and_unscored(self):                     # v2/v3: a render-refused object stays in n, is UNSCORED, and is counted
        rows = self.rows(6); oid = rows[0][0]; (Path(self.tens) / f"{oid}.ic6").write_bytes(rc.SENTINEL_TENSOR); rows[0] = (oid, rows[0][1], rc.SENTINEL_SHA256)
        m = self.tmp / "ms.csv"; mk_manifest(m, rows); ident = identity(self.tmp, self.TP, [r[0] for r in rows], [str(500000 + i) for i in range(60)])
        with self.assertRaises(rc.DataIntegrityFail) as cm: rc.tune(m, self.tens, self.tmp / "sent0", ident, self.TP)                  # v5: a sentinel without a render journal is refused
        self.assertIn("SENTINEL-WITHOUT-RENDER-JOURNAL", str(cm.exception))
        RJ = Path(self.TP.render_journal.format(group="tuning")); RJ.write_text(json.dumps({"objid": oid, "status": "REFUSED", "sentinel": True, "tensor_sha256": rc.SENTINEL_SHA256, "reason": "zero exposure"}) + "\n" + json.dumps({"event": "render-end", "refused_sentinel": 1}) + "\n")
        rc.tune(m, self.tens, self.tmp / "sent", ident, self.TP)
        recs = [json.loads(l) for l in (self.tmp / "sent" / "tuning_receipts.jsonl").read_text().splitlines()]
        self.assertTrue(all(r["sentinel_count"] == 1 for r in recs)); self.assertTrue(all(r["unscored"] >= 1 and r["n"] == 6 for r in recs))
        J = [json.loads(l) for l in (self.tmp / "sent" / "tuning_journal.jsonl").read_text().splitlines()]; self.assertTrue(all(j["status"] == "UNSCORED" for j in J if j["objid"] == oid))
        RJ.write_text(json.dumps({"objid": rows[1][0], "status": "REFUSED", "sentinel": True, "tensor_sha256": rc.SENTINEL_SHA256, "reason": "x"}) + "\n" + json.dumps({"event": "render-end", "refused_sentinel": 1}) + "\n")   # journal refuses a DIFFERENT object: mismatch both ways
        with self.assertRaises(rc.DataIntegrityFail) as cm: rc.tune(m, self.tens, self.tmp / "sent2", ident, self.TP)
        self.assertIn("SENTINEL-JOURNAL-MISMATCH", str(cm.exception))
        RJ.write_text(json.dumps({"objid": oid, "status": "REFUSED", "sentinel": True, "tensor_sha256": rc.SENTINEL_SHA256, "reason": "x"}) + "\n" + json.dumps({"event": "render-end", "refused_sentinel": 2}) + "\n")
        with self.assertRaises(rc.DataIntegrityFail) as cm: rc.tune(m, self.tens, self.tmp / "sent3", ident, self.TP)
        self.assertIn("RENDER-JOURNAL-COUNT", str(cm.exception))
    def test_v4_semantic_conjunction(self):                                    # V19 audit M1/M2: the driver verifies evidence, not fields
        rows = self.rows(6); m = self.tmp / "m.csv"; mk_manifest(m, rows); ids = [r[0] for r in rows]; hold = [str(500000 + i) for i in range(60)]
        def M(**kv):
            def f(I, ctx):
                for k, v in kv.items():
                    d = I
                    for part in k.split(".")[:-1]: d = d[part]
                    d[k.split(".")[-1]] = v
            return f
        cases = (({"outcome": "RETRY"}, "IDENTITY-BEACON-NOT-ACCEPTED"), ({"outcome": "ACCEPT-INVENTED"}, "IDENTITY-BEACON-NOT-ACCEPTED"), ({"outcome": "ACCEPT-NIST"}, "IDENTITY-BEACON-NOT-ACCEPTED"),
                 ({"source": "other"}, "IDENTITY-SOURCE"), ({"witness": False}, "IDENTITY-WITNESS-MISSING"), ({"push_at": TPS}, "IDENTITY-WITNESS-LATE"), ({"push_at": "2098-01-01T00:00:00Z"}, "IDENTITY-WITNESS-LATE"),
                 ({"lock_ok": False}, "IDENTITY-LOCK-MISMATCH"), ({"log_ok": False}, "COLLECTION-LOG-DIGEST"), ({"conflict": True}, "COLLECTION-LOG-CONFLICT"), ({"adoption_ok": False, "fresh": True}, "ADOPTION-MALFORMED"), ({"seed_ok": False}, "IDENTITY-SEED-NOT-REDERIVED"),
                 ({"nonce_ok": False}, "NONCE-UNAUTHENTICATED"), ({"t_pulse": "2026-09-06T03:11:00Z"}, "IDENTITY-T-PULSE"),
                 # codex V20 M1: fabricated witness/history fragments with a REAL seed — each now refused from committed evidence
                 ({"mutate": M(**{"approval_witness.record_path": "nope.md"})}, "APPROVAL-RECORD-MISSING"), ({"mutate": M(**{"approval_witness.nonce_round": -1})}, "APPROVAL-NONCE-LINE"),
                 ({"mutate": M(**{"approval_witness.push_event_sha256": "0" * 64})}, "EVENT-DIGEST"), ({"mutate": M(**{"approval_witness.events_provenance": {}})}, "EVENT-PROVENANCE"),
                 ({"mutate": M(**{"approval_witness.push_event.payload.head": "0" * 40, "approval_witness.push_event.payload.commits": []})}, "EVENT-DIGEST"),
                 ({"mutate": M(**{"collection_lock.entries": 999})}, "HISTORY-COUNT"), ({"mutate": M(**{"beacon_round": ROUND + 1})}, "IDENTITY-ROUND"), ({"mutate": M(**{"T_sign": "2026-09-06T01:00:00Z"})}, "APPROVAL-T-SIGN-LINE"),
                 ({"seal_files": (lambda p, log, rp: [p, log]), "fresh": True}, "BEACON-RECORD-NOT-IN-WITNESS-COMMIT"),      # in a FRESH repo (no earlier freeze commit already carries the record bytes)
                 ({"mutate": (lambda I, ctx: (ctx["log"].write_text("".join(json.dumps({"stage": "builder-accept", "record_sha256": I["beacon_record_sha256"], "outcome": "ACCEPT-DRAND", "seed_hex": I["seed_hex"], "utc": "x", "prev_sha256": "0" * 64}) + "\n" for _ in range(999))), I["collection_lock"].__setitem__("log_sha256", rc.sha_file(ctx["log"])), I["collection_lock"].__setitem__("entries", 999)))}, "HISTORY-INVALID"),
                 ({"mutate": (lambda I, ctx: (ctx["rp"].write_text(json.dumps({**json.loads(ctx["rp"].read_text()), "relays": {"https://api.drand.sh.attacker.invalid/x": next(iter(json.loads(ctx["rp"].read_text())["relays"].values())), vd.round_url("https://api2.drand.sh", ROUND): next(iter(json.loads(ctx["rp"].read_text())["relays"].values()))}})), I.__setitem__("beacon_record_sha256", rc.sha_file(ctx["rp"])), I["collection_lock"]["first_accept"].__setitem__("record_sha256", rc.sha_file(ctx["rp"]))))}, "IDENTITY-LOCK-MISMATCH"))
        for kw, tok in cases:
            kw = dict(kw); tmp, TP = (self.tmp, self.TP)
            if kw.pop("fresh", False): tmp = Path(tempfile.mkdtemp()); TP = TPJ(tmp); rc.ADOPTION_FILE = Path(self.TP.adoption_file)
            ident = identity(tmp, TP, ids, hold, **kw)
            with self.assertRaises(rc.DataIntegrityFail) as cm: rc.tune(m, self.tens, tmp / ("v4" + tok), ident, TP)
            self.assertIn(tok, str(cm.exception), kw)
        ident = identity(self.tmp, self.TP, ids, hold)                            # a complete identity tunes — through PRODUCTION's re-deriver
        self.assertIs(self.TP.rederive_seed, rc.production_rederive_seed); self.assertIs(rc.PRODUCTION.rederive_seed, rc.production_rederive_seed)
        s = rc.tune(m, self.tens, self.tmp / "v4ok", ident, self.TP); self.assertEqual(s["mode"], "tune")
        ident = identity(self.tmp, self.TP, ids, hold, ancestry=True)             # delivery by before..head ancestry (payload.commits omits the approval commit)
        s = rc.tune(m, self.tens, self.tmp / "v5anc", ident, self.TP); self.assertEqual(s["mode"], "tune")
        with self.assertRaises(rc.DataIntegrityFail) as cm: rc.load_identity(ident, rc.Protocol(**{**self.TP.__dict__, "rederive_seed": None}))   # the V20 production value, refused as before
        self.assertIn("PROTOCOL-NO-REDERIVER", str(cm.exception))
        Path(self.TP.collection_log).write_text("")                                # emptied after the seal → refused (digest), never "first attempt"
        with self.assertRaises(rc.DataIntegrityFail) as cm: rc.tune(m, self.tens, self.tmp / "v4empty", ident, self.TP)
        self.assertIn("COLLECTION-LOG", str(cm.exception))
    def test_holdout_once_prepared_not_adopted(self):                          # INHERITED — PREPARED, NOT ADOPTED: default False (unchanged behaviour); True refuses a second invocation
        self.assertFalse(rc.PRODUCTION.holdout_once)
        rows = self.rows(6)
        s, ident = self.tune_ok(rows, tag="ho"); hm = self.tmp / "hm.csv"; hr = self.hold_rows(); mk_manifest(hm, hr); self.seal_tuning(s, tag="ho"); T = Path(self.TP.seal_journal).parent / "ho" / "selection_summary.json"
        once = rc.Protocol(**{**self.TP.__dict__, "holdout_once": True})
        rc.holdout(T, hm, self.tens, self.tmp / "h1", ident, once)
        with self.assertRaises(rc.DataIntegrityFail) as cm: rc.holdout(T, hm, self.tens, self.tmp / "h2", ident, once)
        self.assertIn("HOLDOUT-ALREADY-INVOKED", str(cm.exception))
        rc.holdout(T, hm, self.tens, self.tmp / "h3", ident, self.TP)          # default protocol: repeatable (the inherited V15 behaviour, unchanged)
    def test_cli_entry_point_runs_under_PRODUCTION(self):                     # the real entry point, PRODUCTION protocol: refuses on the first missing evidence, never PROTOCOL-NO-REDERIVER
        import io, contextlib
        buf = io.StringIO()
        with contextlib.redirect_stdout(buf): code = rc.main(["tune", "--manifest", "x", "--tensors", "x", "--out", str(self.tmp / "cli"), "--identity", str(self.tmp / "absent.json")])
        self.assertEqual(code, 2); self.assertIn("IDENTITY-MISSING", buf.getvalue()); self.assertNotIn("NO-REDERIVER", buf.getvalue())
    def test_composed_mode_on_the_production_call_path(self):                  # UNADOPTED composed mode: track-2 v2 helpers inside load_identity (Blanc 21:14: not in isolation)
        rows = self.rows(6); ids = [r[0] for r in rows]; hold = [str(500000 + i) for i in range(60)]
        work = Path(self.TP.seal_journal).parent; git(self.TP.witness_remote_url, "config", "receive.denyNonFastforwards", "true"); open_file = work / "HISTORY_OPEN_EVENT.json"; EVS = []
        composed_TP = rc.Protocol(**{**self.TP.__dict__, "provenance_mode": "composed", "events_repo": "DuhoKim/NebulaMind", "history_open_event_file": str(open_file)})
        def canon(e): return hashlib.sha256(json.dumps(e, sort_keys=True, separators=(",", ":")).encode()).hexdigest()
        def pev(commit, n, wk=None):                                               # a fixture PushEvent (labelled) for ONE published history commit: before = its parent (one push per commit)
            return {"type": "PushEvent", "id": f"h{n}", "created_at": f"2026-09-06T09:{50 + n:02d}:00Z", "repo": {"name": "DuhoKim/NebulaMind"}, "payload": {"ref": "refs/heads/main", "before": git(wk or work, "rev-parse", commit + "^"), "head": commit, "commits": [{"sha": commit}]}}
        def publish(I, ctx, wk=None, of=None, evs=None):
            """the fixture's event gets the pinned repo name; the history is PUBLISHED as design (b) v3 requires: the genesis ALONE = history-open commit (its PushEvent retained), then ONE commit per entry, each pushed."""
            wk = wk or work; of = of or open_file; evs = EVS if evs is None else evs
            ev = I["approval_witness"]["push_event"]; ev["repo"] = {"name": "DuhoKim/NebulaMind"}; I["approval_witness"]["push_event_sha256"] = canon(ev)
            log = ctx["log"]; lines = [l for l in log.read_bytes().split(b"\n") if l]
            for n in range(len(lines)):
                log.write_bytes(b"\n".join(lines[: n + 1]) + b"\n"); git(wk, "add", log.name); git(wk, "commit", "-q", "-m", f"history entry {n}"); c = git(wk, "rev-parse", "HEAD"); git(wk, "push", "-q", "origin", "HEAD:refs/heads/main"); evs.append(pev(c, n, wk))
                if n == 0: of.write_text(json.dumps(evs[0])); git(wk, "add", of.name)
        def feed(events):                                                         # FIXTURE-SUPPLIED `gh api` runner (labelled): one page, then the end
            return lambda cmd: (0, json.dumps(events if cmd[-1].endswith("page=1") else []), "")
        ident = identity(self.tmp, composed_TP, ids, hold, mutate=publish); ev = json.loads(ident.read_text())["approval_witness"]["push_event"]
        rc.load_identity(ident, self.TP)                                                                  # (1) the OFFLINE candidate loads it
        Iw, d = rc.load_identity(ident, rc.Protocol(**{**composed_TP.__dict__, "events_runner": feed([ev] + EVS)})); self.assertEqual(Iw["_composed"]["event"], "AUTHENTIC")   # COMPOSED: genuine event + open event in the live feed, one entry per commit → loads
        with self.assertRaises(rc.DataIntegrityFail) as cm: rc.load_identity(ident, rc.Protocol(**{**composed_TP.__dict__, "events_runner": feed([{**ev, "id": "other", "created_at": "2026-09-06T00:00:00Z"}] + EVS)}))   # (2) the retained approval event is not in the live feed
        self.assertIn("EVENT-FORGED", str(cm.exception))
        with self.assertRaises(rc.DataIntegrityFail) as cm: rc.load_identity(ident, rc.Protocol(**{**composed_TP.__dict__, "events_runner": (lambda cmd: (1, "", "gh: HTTP 502: Bad Gateway"))}))   # (3) live feed unavailable → RETRY
        self.assertIn("RETRY-EVENTS-UNAVAILABLE", str(cm.exception))
        far = {"type": "PushEvent", "id": "z", "created_at": "2027-01-01T00:00:00Z", "repo": {"name": "DuhoKim/NebulaMind"}, "payload": {"ref": "refs/heads/main", "before": "1" * 40, "head": "2" * 40, "commits": [{"sha": "2" * 40}]}}   # a later, UNRELATED push: the feed no longer reaches the approval event and nothing contradicts it → EXPIRED (v11: a later push delivering the SAME commit would be a contradiction → FORGED)
        with self.assertRaises(rc.DataIntegrityFail) as cm: rc.load_identity(ident, rc.Protocol(**{**composed_TP.__dict__, "events_runner": feed([far])}))   # expired, no receipt path configured (Q1 Option C)
        self.assertIn("EVENT-EXPIRED-NO-RECEIPT-PATH", str(cm.exception))
        with self.assertRaises(rc.DataIntegrityFail) as cm: rc.load_identity(ident, rc.Protocol(**{**composed_TP.__dict__, "events_runner": feed([ev] + EVS[1:])}))   # the open event absent from the live feed
        self.assertIn("history-open event", str(cm.exception))                                                                       # v10: EVIDENCE-EXPIRED (history-open event) — the feed no longer reaches it; no receipt path
        # (4) codex's attack 2: history rebuilt before the freeze, coherently sealed AND pushed as a fast-forward
        tmp2 = Path(tempfile.mkdtemp()); TP2 = TPJ(tmp2); rc.ADOPTION_FILE = Path(self.TP.adoption_file); work2 = Path(TP2.seal_journal).parent; git(TP2.witness_remote_url, "config", "receive.denyNonFastforwards", "true")   # a FRESH repository, so the only history commits are this identity's
        open2 = work2 / "HISTORY_OPEN_EVENT.json"; EVS2 = []; composed2 = rc.Protocol(**{**TP2.__dict__, "provenance_mode": "composed", "events_repo": "DuhoKim/NebulaMind", "history_open_event_file": str(open2)})
        def rebuild2(I, ctx):                                                      # codex V21 attack 2: publish honestly, then rebuild and publish the rebuild (fast-forward)
            publish(I, ctx, wk=work2, of=open2, evs=EVS2); ctx["log"].unlink(); H.genesis(ctx["log"], I["approval_witness"]["record_sha256"], I["T_pulse"], I["rule_sha256"], I["beacon_round"])
            e = H.append(ctx["log"], {"stage": "builder-accept", "record_sha256": I["beacon_record_sha256"], "outcome": "ACCEPT-DRAND", "seed_hex": I["seed_hex"], "source": "drand-mainnet-default"})
            I["collection_lock"] = {"first_accept": e, "log_sha256": rc.sha_file(ctx["log"]), "entries": 2}
        ident2 = identity(tmp2, composed2, ids, hold, mutate=rebuild2); ev2 = json.loads(ident2.read_text())["approval_witness"]["push_event"]
        rc.load_identity(ident2, TP2)                                                                     # OFFLINE accepts the rebuild (disclosed boundary)
        with self.assertRaises(rc.DataIntegrityFail) as cm: rc.load_identity(ident2, rc.Protocol(**{**composed2.__dict__, "events_runner": feed([ev2] + EVS2)}))
        self.assertIn("HISTORY-CONTINUATION", str(cm.exception)); self.assertIn("NOT-AN-EXTENSION", str(cm.exception))   # COMPOSED: the remote's own history shows the rebuild
        # codex V22 attack A: a history rebuilt BEFORE its first publication, published as the first commit and named as history-open — refused (not genesis-only)
        tmp3 = Path(tempfile.mkdtemp()); TP3 = TPJ(tmp3); rc.ADOPTION_FILE = Path(self.TP.adoption_file); work3 = Path(TP3.seal_journal).parent; git(TP3.witness_remote_url, "config", "receive.denyNonFastforwards", "true")
        open3 = work3 / "HISTORY_OPEN_EVENT.json"; composed3 = rc.Protocol(**{**TP3.__dict__, "provenance_mode": "composed", "events_repo": "DuhoKim/NebulaMind", "history_open_event_file": str(open3)}); EVS3 = []
        def late_first(I, ctx):
            ev = I["approval_witness"]["push_event"]; ev["repo"] = {"name": "DuhoKim/NebulaMind"}; I["approval_witness"]["push_event_sha256"] = canon(ev)
            ctx["log"].unlink(); H.genesis(ctx["log"], I["approval_witness"]["record_sha256"], I["T_pulse"], I["rule_sha256"], I["beacon_round"])
            e = H.append(ctx["log"], {"stage": "builder-accept", "record_sha256": I["beacon_record_sha256"], "outcome": "ACCEPT-DRAND", "seed_hex": I["seed_hex"], "source": "drand-mainnet-default"})
            I["collection_lock"] = {"first_accept": e, "log_sha256": rc.sha_file(ctx["log"]), "entries": 2}
            git(work3, "add", ctx["log"].name); git(work3, "commit", "-q", "-m", "late first publication"); c = git(work3, "rev-parse", "HEAD"); git(work3, "push", "-q", "origin", "HEAD:refs/heads/main"); EVS3.append(pev(c, 0, work3)); open3.write_text(json.dumps(EVS3[0])); git(work3, "add", open3.name)
        ident3 = identity(tmp3, composed3, ids, hold, mutate=late_first); ev3 = json.loads(ident3.read_text())["approval_witness"]["push_event"]
        rc.load_identity(ident3, TP3)                                                                     # OFFLINE accepts it (disclosed boundary)
        with self.assertRaises(rc.DataIntegrityFail) as cm: rc.load_identity(ident3, rc.Protocol(**{**composed3.__dict__, "events_runner": feed([ev3] + EVS3)}))
        self.assertIn("OPEN-NOT-GENESIS-ONLY", str(cm.exception))
        self.assertEqual(rc.PRODUCTION.provenance_mode, "offline")                # the default is the offline candidate; composed is UNADOPTED
if __name__ == "__main__":
    unittest.main()
