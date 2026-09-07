"""TRACK 13 — the table-derived controls, v3 (Blanc 05:02 item 2; codex V32-1; agy V32 FATALs): generated from run_configurations_v18.INDEPENDENCE / PREREQUISITES
with NO exemption, one method per (prerequisite, check) pair with the check independent of the prerequisite, plus two-prerequisite variants; every method is one subcase.
v4 asserts the property DIFFERENTIALLY against the frozen defect-only DECLARED snapshot; the separate declaration suite checks it against executed outcomes; then with the prerequisite failed, (1) EVERY check that does not need the
failed prerequisite contributes EXACTLY what it contributed in the baseline — the defect's own check included — the only permitted addition being the prerequisite's
failure code at the check that meets it; (2) NOTHING independent of the failed prerequisite is blocked (out["blocked"] is a subset of the table's needers); (3) every
check that needs it is BLOCKED BY NAME or contributes under its own name only unavailability / the failure code / a subset of its baseline; (4) the winner equals the
resolver over the recorded findings. No allow-list of stray codes: a check reading the same altered input under another code is part of the baseline, not an exemption.
v2 (the allow-list model, runs 1/2/1b/2b/1c/2c) is retained as _nsd_table_controls_v2_RETAINED_20260907.py.txt."""
import json, os, re, sys, tempfile, unittest, hashlib, subprocess, base64
from collections import Counter
from BASELINE_DECLARATIONS_V18 import DECLARED
from pathlib import Path
from unittest import mock
HERE = Path(__file__).resolve().parent; D = HERE.parent
for p in ("beacon_v2", "drand_only", "corpus_identity", "fourier_chirality", "track2", "track13"): sys.path.insert(0, str(D / p))
import provenance_designs_v14 as P, precedence_core as PC
import run_configurations_v18 as rc, test_run_configurations_v18 as TF, history_v2 as H
from test_track13_regressions import H13, feed, canon, REF, REPO
import test_track13_regressions as _R
_R.rc, _R.P, _R.TF = rc, P, TF   # the helpers hold their own globals; without this an "on V34" run silently exercises V33
# ---- defect recipes: ONE planted defect per check, with the code the check must contribute (independent of the implementation's output)
DEFECTS = {
    "open-local":         {"code": "HISTORY-CONTINUATION: OPEN-EVENT-INCONSISTENT-INPUT", "plant": "open-wrong-repo"},
    "approval-local":     {"code": "EVENT-INCONSISTENT",                                  "plant": "approval-wrong-repo"},
    "approval-delivery":  {"code": "EVENT-INCONSISTENT",                                  "plant": "approval-non-delivery"},
    "lists":              {"code": "IDENTITY-tuning_objids-SIZE-OR-TYPE",                 "plant": "five-ids"},
    "identity-local":     {"code": "IDENTITY-POOL-DIGEST",                                "plant": "pool-digest"},
    "nonce":              {"code": "NONCE-UNAUTHENTICATED",                               "plant": "nonce-bad"},
    "adoption":           {"code": "ADOPTION-MISMATCH",                                   "plant": "adoption-mismatch"},
    "adoption-identity":  {"code": "IDENTITY-RULE-DIGEST",                               "plant": "identity-rule-digest"},
    "identity-time-order": {"code": "IDENTITY-WITNESS-LATE",                             "plant": "late-approval"},          # v18 (B-1a): the order comparison as its own check
    "history-working-tree": {"code": "HISTORY-CONTINUATION",                             "plant": "pending-push", "reason": "PENDING-PUSH"},   # v14 (B-1c): the working-tree comparison as its own check
    "conjunction":        {"code": "IDENTITY-LOCK-MISMATCH",                              "plant": "lock"},
    "approval-live":      {"code": "EVENT-FORGED",                                        "plant": "same-id-approval"},
    "open-same-id":       {"code": "HISTORY-CONTINUATION: OPEN-EVENT-FORGED",             "plant": "same-id-open"},
    "seed":               {"code": "REDERIVE-RETRY",                                      "plant": "seed-bodies"},
    "history-remote":     {"code": "HISTORY-CONTINUATION",                                "plant": "rewrite", "reason": "NOT-AN-EXTENSION"},
    "open-delivery-auth": {"code": "HISTORY-CONTINUATION",                                "plant": "open-non-delivery", "reason": "OPEN-EVENT-INCONSISTENT-INPUT"},
    "per-entry":          {"code": "HISTORY-CONTINUATION",                                "plant": "batch", "reason": "HISTORY-PUBLICATION-BATCH"},
}
def build_with(h, plant):
    kw = {}; mutate_ev = None; mutate_I = None; rebuild = False; nonce_ok = True
    if plant == "five-ids": kw["_ids5"] = True
    if plant == "approval-wrong-repo": mutate_ev = lambda ev, evs: ev.update({"repo": {"name": "wrong/repo"}})
    if plant == "approval-non-delivery": mutate_ev = lambda ev, evs: ev["payload"].update({"before": TF.git(Path(h._wk), "rev-parse", ev["payload"]["head"] + "^"), "head": TF.git(Path(h._wk), "rev-parse", ev["payload"]["head"] + "^"), "commits": []})
    if plant == "pool-digest": mutate_I = lambda I: I.update({"pool_sha256": "q" * 64})
    if plant == "identity-rule-digest": mutate_I = lambda I: I.update({"rule_sha256": "b" * 64})   # the identity names a rule that is not the adopted one
    if plant == "late-approval": mutate_I = lambda I: I.update({"T_pulse": "2020-01-01T00:00:00Z"})           # a genuine approval pushed AFTER T_pulse — the order check's own defect
    if plant == "pending-push": pass                                                                          # planted after the build: the working tree is extended without publishing
    if plant == "adoption-mismatch": pass   # planted after the build: the adoption file rewritten to a different digest (restored per test)
    if plant == "lock": kw["lock_ok"] = False
    if plant == "nonce-bad": nonce_ok = False
    if plant == "rewrite": rebuild = True
    if plant == "seed-bodies": kw["_seed_bodies"] = True
    env = h.build_plant(rebuild_after=rebuild, mutate_ev=mutate_ev, mutate_I=mutate_I, nonce_ok=nonce_ok, **kw)
    live = env["live"]
    if plant == "open-wrong-repo": env["of"].write_text(json.dumps({**env["evs"][0], "repo": {"name": "wrong/repo"}}))
    if plant == "open-non-delivery": gp = TF.git(env["wk"], "rev-parse", env["evs"][0]["payload"]["before"] + "^"); env["of"].write_text(json.dumps({**env["evs"][0], "payload": {**env["evs"][0]["payload"], "before": gp, "head": gp, "commits": []}}))
    if plant == "same-id-approval": live = [{**env["genuine"], "payload": {**env["genuine"]["payload"], "before": "0" * 40}}] + env["evs"]
    if plant == "same-id-open": live = [env["ev"], {**env["evs"][0], "payload": {**env["evs"][0]["payload"], "before": "0" * 40}}] + env["evs"][1:]
    if plant == "batch": live = [env["ev"], env["evs"][0], {"type": "PushEvent", "id": "batch", "created_at": "2026-09-06T09:59:00Z", "repo": {"name": REPO}, "payload": {"ref": REF, "before": env["evs"][1]["payload"]["head"], "head": env["evs"][-1]["payload"]["head"]}}]
    if plant == "adoption-mismatch": env["_adoption_backup"] = Path(rc.ADOPTION_FILE).read_bytes(); Path(rc.ADOPTION_FILE).write_text("a" * 64 + "\n")
    if plant == "pending-push":
        lp = Path(env["cTP"].collection_log); lp.write_bytes(lp.read_bytes() + b'{"stage":"unpublished","note":"an entry the remote has never acknowledged"}\n')   # the COLLECTION LOG is the published history the collector compares (the seal journal is not)
    env["live"] = live; return env
def fail_prereqs(Ps, env):
    ctxs = []; runner = feed(env["live"]); live = env["live"]
    for P_ in Ps:
        if P_ == "identity-file": Path(env["ident"]).unlink()
        elif P_ == "open-file": env["of"].write_text("null")
        elif P_ == "adoption-file": env.setdefault("_adoption_backup", Path(rc.ADOPTION_FILE).read_bytes()); Path(rc.ADOPTION_FILE).unlink()
        elif P_ == "witness-fetch": ctxs.append(mock.patch.object(rc, "verify_witness", side_effect=rc.DataIntegrityFail("WITNESS-FETCH-FAILED fixture transport unavailable")))
        elif P_ == "verifier-import": ctxs.append(mock.patch.object(rc, "_drand_modules", side_effect=rc.DataIntegrityFail("VERIFIER-UNAVAILABLE: fixture — py_ecc unavailable")))
        elif P_ == "helpers-import": ctxs.append(mock.patch.object(rc, "_P", side_effect=ImportError("fixture: provenance helpers unavailable")))
        elif P_ == "events-page1": runner = feed(live, page1_fail=True)
        elif P_ == "events-later-page":
            filler = [{"type": "IssuesEvent", "id": f"f{i}", "created_at": "2026-09-06T09:40:00Z", "repo": {"name": REPO}, "payload": {}} for i in range(100 - len(live))]
            runner = feed(live + filler, page2=lambda cmd: (1, "", "gh: HTTP 503"))
        elif P_ == "remote-head": ctxs.append(mock.patch.object(P, "remote_head", lambda url, ref: None))
        elif P_ == "git-launch":
            real = subprocess.run
            def failing(args, *a, **k):
                if args and args[0] == "git": raise OSError("fixture: git cannot launch")
                return real(args, *a, **k)
            ctxs.append(mock.patch("subprocess.run", side_effect=failing))
        else: raise ValueError(P_)
    return ctxs, runner
class NSD2(unittest.TestCase):
    @classmethod
    def setUpClass(cls): cls.t = TF.T("test_composed_mode_on_the_production_call_path"); cls.t.setUp(); cls.h = H13(cls.t)
    @classmethod
    def tearDownClass(cls): cls.t.tearDown()
REPORTER = {"identity-file": "approval-local", "open-file": "open-local", "git-launch": "history-remote", "witness-fetch": "conjunction", "verifier-import": "helpers", "helpers-import": "helpers", "events-page1": "snapshot", "events-later-page": "snapshot", "remote-head": "history-remote", "adoption-file": "adoption"}
UNAVAIL = {"RETRY-EVENTS-UNAVAILABLE", "RETRY-HISTORY-CONTINUATION", "RETRY-EVENTS-INCOMPLETE", "STAGE-BLOCKED", "MALFORMED-REMOTE-EVIDENCE", "VERIFIER-UNAVAILABLE", "IO-UNAVAILABLE", "IDENTITY-SCHEMA", "HISTORY-OPEN-EVENT-MISSING", "ADOPTION-MALFORMED"}
def by_check(fs):
    b = {}
    for f in fs: b.setdefault(f["check"], set()).add((f["class"], f["code"], f["stage"]))
    return b
def run_case(self, Ps, C):
    """plant defect C, fail the prerequisites Ps, run the production call path; return (winner message, LAST_OUTCOME)"""
    self.h._wk = None; env = build_with(self.h, DEFECTS[C]["plant"]); self.h._wk = str(env["wk"]); ctxs, runner = fail_prereqs(Ps, env)
    from contextlib import ExitStack
    try:
        with ExitStack() as st:
            for c in ctxs: st.enter_context(c)
            with self.assertRaises(rc.DataIntegrityFail) as cm: rc.load_identity(env["ident"], rc.Protocol(**{**env["cTP"].__dict__, "events_runner": runner}))
    finally:
        if "_adoption_backup" in env: Path(rc.ADOPTION_FILE).write_bytes(env["_adoption_backup"])                       # the adoption file is shared by the class: restore it
    out = rc.LAST_OUTCOME; self.assertIsNotNone(out); return str(cm.exception), out
def baseline(C):
    """Frozen data only: never execute the implementation to choose expected findings."""
    return {check: {tuple(row) for row in rows} for check, rows in DECLARED[C].items()}
def counts_by_check(fs):
    b = {}
    for f in fs:
        b.setdefault(f["check"], Counter())[(f["class"], f["code"], f["stage"])] += 1
    return b
def _make(Ps, C):
    def test(self):
        base = baseline(C); msg, out = run_case(self, Ps, C); fs = out["findings"]; b = by_check(fs)
        needers = {k for k, v in rc.INDEPENDENCE.items() if any(P_ in v["needs"] for P_ in Ps)}; pcodes = {rc.PREREQUISITES[P_]["failure_code"] for P_ in Ps}
        self.assertTrue(msg.startswith(DEFECTS[C]["code"]) or DEFECTS[C]["code"] in {f["code"] for f in fs}, f"[{Ps} fail; defect {C}] the defect {DEFECTS[C]['code']} must be contributed at all (behavioural, before attribution): winner {msg[:100]!r}; codes {sorted({f['code'] for f in fs})}")
        self.assertIn(DEFECTS[C]["code"], {t[1] for t in b.get(C, set())}, f"[{Ps} fail; defect {C}] the defect must be contributed by ITS check: got {b}")
        if "reason" in DEFECTS[C]: self.assertTrue(any(DEFECTS[C]["reason"] in f["why"] for f in fs if f["check"] == C and f["code"] == DEFECTS[C]["code"]), f"reason {DEFECTS[C]['reason']}: {[f['why'][:60] for f in fs if f['check'] == C]}")
        # (1) INDEPENDENCE: every check that needs none of the failed prerequisites contributes exactly its baseline (+ the failure code, at the reporter only)
        for k in (set(b) | set(base)) - needers - {"helpers", "resolver"}:
            add_ = {(rc.PREREQUISITES[P_]["class"], rc.PREREQUISITES[P_]["failure_code"], rc.INDEPENDENCE[k]["stage"]) for P_ in Ps if REPORTER[P_] == k}
            self.assertEqual(b.get(k, set()), base.get(k, set()) | add_, f"[{Ps} fail; defect {C}] check {k} needs none of {Ps}; its contribution must equal the baseline {sorted(base.get(k, set()))} (+{sorted(add_)}), got {sorted(b.get(k, set()))}")
            expected_counts = Counter(tuple(row) for row in DECLARED[C].get(k, []))
            expected_counts |= Counter(add_)
            self.assertEqual(counts_by_check(fs).get(k, Counter()), expected_counts,
                             f"[{Ps} fail; defect {C}] check {k}: finding multiplicity must equal the declaration plus reporter failures")
        # (2) nothing independent of the failed prerequisites is blocked
        self.assertTrue(set(out["blocked"]) <= needers, f"[{Ps} fail; defect {C}] blocked checks must all need a failed prerequisite (table needers {sorted(needers)}): blocked={sorted(out['blocked'])}")
        # the prerequisite failure is contributed by the check that meets it
        for P_ in Ps:
            r = REPORTER[P_]; fc = rc.PREREQUISITES[P_]["failure_code"]
            self.assertTrue(fc in {t[1] for t in b.get(r, set())} or (r == "helpers" and any(f["code"] in ("VERIFIER-UNAVAILABLE", "HELPERS-UNAVAILABLE") for f in fs)), f"[{Ps} fail; defect {C}] the failure {fc} of {P_} must be contributed by {r}: got {b}")
        # (3) every check that needs a failed prerequisite: BLOCKED by name, or contributing under its own name only unavailability / the failure code / a subset of its baseline
        for n in needers:
            if n in out["blocked"]: continue
            self.assertIn(n, b, f"[{Ps} fail; defect {C}] check {n} needs {Ps}: it must be BLOCKED by name or contribute under its own name: blocked={sorted(out['blocked'])}, by_check={b}")
            self.assertTrue(all(t in base.get(n, set()) or t[1] in pcodes | UNAVAIL for t in b[n]), f"[{Ps} fail; defect {C}] check {n} (needs {Ps}) contributed beyond unavailability / the failure code / its baseline {sorted(base.get(n, set()))}: {sorted(b[n])}")
            retained = Counter({t: count for t, count in counts_by_check(fs)[n].items()
                                if t[1] not in pcodes | UNAVAIL})
            declared_counts = Counter(tuple(row) for row in DECLARED[C].get(n, []))
            self.assertFalse(retained - declared_counts,
                             f"[{Ps} fail; defect {C}] check {n}: baseline subset must not gain duplicate findings")
        self.assertTrue(all(f.get("why") for f in fs))
        # (4) one resolver decides
        w = PC.resolve([PC.finding(f["class"], f["code"], f["why"], f["stage"], i, f["check"]) for i, f in enumerate(fs)]); self.assertTrue(msg.startswith(w["code"]), f"{msg[:80]!r} vs {w['code']}")
    return test
PAIRS = [([P_], C) for P_ in rc.PREREQUISITES for C, spec in rc.INDEPENDENCE.items() if P_ not in spec["needs"] and C in DEFECTS and C != "snapshot"]
for Ps, C in PAIRS: setattr(NSD2, f"test_{Ps[0].replace('-', '_')}_fails__{C.replace('-', '_')}", _make(Ps, C))
DOUBLES = [(["witness-fetch", "events-page1"], "identity-local"), (["witness-fetch", "remote-head"], "open-local"), (["helpers-import", "witness-fetch"], "lists"), (["identity-file", "remote-head"], "open-local"), (["verifier-import", "events-later-page"], "adoption"), (["git-launch", "events-page1"], "identity-local")]
for Ps, C in DOUBLES: setattr(NSD2, f"test_{'_and_'.join(p.replace('-', '_') for p in Ps)}_fail__{C.replace('-', '_')}", _make(Ps, C))
if __name__ == "__main__": unittest.main()
