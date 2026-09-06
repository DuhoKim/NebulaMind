"""TRACK 12 FAIL-FIRST tests — Blanc 05:02: ONE property (NSD — "No Stage Decides": no stage may decide or abort; every stage contributes; one resolver decides),
made checkable by run_configurations_v16.INDEPENDENCE / PREREQUISITES; the CONTROLS are DERIVED FROM THAT TABLE — for each prerequisite P that can fail and each
check C that does not need P, one test method: plant a C-defect, make P fail, assert the WHOLE outcome (winner; the full finding set with each code and a reason;
the checks that needed P recorded as BLOCKED). Codex's V31 constructions follow as REGRESSION cases, one subcase per method. Every method is its own subcase so the
fail-first run shows each one separately. Labelled fixture runners; local bare repositories; monkeypatches labelled."""
import json, os, re, sys, tempfile, unittest, hashlib, subprocess, base64
from pathlib import Path
from unittest import mock
HERE = Path(__file__).resolve().parent; D = HERE.parent
for p in ("beacon_v2", "drand_only", "corpus_identity", "fourier_chirality", "track2"): sys.path.insert(0, str(D / p))
import provenance_designs_v12 as P
import run_configurations_v16 as rc, test_run_configurations_v16 as TF, history_v2 as H
REF = "refs/heads/main"; REPO = "DuhoKim/NebulaMind"
def canon(e): return hashlib.sha256(json.dumps(e, sort_keys=True, separators=(",", ":")).encode()).hexdigest()
def feed(events, counter=None, page2=None, page1_fail=False):
    def runner(cmd):
        if counter is not None: counter.append(cmd[-1])
        if cmd[-1].endswith("page=1"): return (1, "", "gh: HTTP 503: Service Unavailable") if page1_fail else (0, json.dumps(events), "")
        if page2 is not None and cmd[-1].endswith("page=2"): return page2(cmd)
        return (0, json.dumps([]), "")
    return runner
# ---------------------------------------------------------------- the fixture harness (shared; every test builds its own identity)
class Harness:
    def __init__(self, t): self.t = t; rows = t.rows(6); self.ids = [r[0] for r in rows]; self.hold = [str(500000 + i) for i in range(60)]
    def pev(self, commit, n, wk): return {"type": "PushEvent", "id": f"h{n}", "created_at": f"2026-09-06T09:{50 + n:02d}:00Z", "repo": {"name": REPO}, "payload": {"ref": REF, "before": TF.git(wk, "rev-parse", commit + "^"), "head": commit, "commits": [{"sha": commit}]}}
    def fresh(self):
        tmp = Path(tempfile.mkdtemp()); TP = TF.TPJ(tmp); rc.ADOPTION_FILE = Path(self.t.TP.adoption_file); wk = Path(TP.seal_journal).parent; TF.git(TP.witness_remote_url, "config", "receive.denyNonFastforwards", "true")
        of = wk / "HISTORY_OPEN_EVENT.json"; evs = []; cTP = rc.Protocol(**{**TP.__dict__, "provenance_mode": "composed", "events_repo": REPO, "history_open_event_file": str(of)}); return {"tmp": tmp, "TP": TP, "wk": wk, "of": of, "evs": evs, "cTP": cTP}
    def build(self, defect=None, **kw):
        """one identity with ONE planted defect (a check's name from INDEPENDENCE, or None); returns (ident, ev, env)"""
        env = self.fresh(); wk, of, evs = env["wk"], env["of"], env["evs"]; ids = self.ids[:5] if defect == "lists" else self.ids
        def publish(I, ctx):
            ev = I["approval_witness"]["push_event"]; ev["repo"] = {"name": REPO}
            if defect == "seed":                                                                       # unverifiable retained seed bodies, everything rebound coherently
                rp = Path(env["TP"].beacon_record_path); rec = json.loads(rp.read_text())
                for u, r in rec["relays"].items():
                    if isinstance(r, dict) and "body_b64" in r: b = json.loads(base64.b64decode(r["body_b64"])); b["signature"] = "00"; r["body_b64"] = base64.b64encode(json.dumps(b).encode()).decode()
                rp.write_text(json.dumps(rec, indent=1, sort_keys=True)); I["beacon_record_sha256"] = rc.sha_file(rp)
                ctx["log"].unlink(); H.genesis(ctx["log"], I["approval_witness"]["record_sha256"], I["T_pulse"], I["rule_sha256"], I["beacon_round"])
                e = H.append(ctx["log"], {"stage": "builder-accept", "record_sha256": I["beacon_record_sha256"], "outcome": "ACCEPT-DRAND", "seed_hex": I["seed_hex"], "source": "drand-mainnet-default"}); I["collection_lock"] = {"first_accept": e, "log_sha256": rc.sha_file(ctx["log"]), "entries": 2}
            log = ctx["log"]; lines = [l for l in (log.read_bytes().split(b"\n")) if l]
            for n in range(len(lines)):
                log.write_bytes(b"\n".join(lines[: n + 1]) + b"\n"); TF.git(wk, "add", log.name); TF.git(wk, "commit", "-q", "-m", f"history entry {n}"); c = TF.git(wk, "rev-parse", "HEAD"); TF.git(wk, "push", "-q", "origin", "HEAD:" + REF); evs.append(self.pev(c, n, wk))
                if n == 0 and not of.exists(): of.write_text(json.dumps(evs[0])); TF.git(wk, "add", of.name)
            if defect == "history-remote":                                                             # a published fast-forward REWRITE then restoration (codex's construction)
                ctx["log"].unlink(); H.genesis(ctx["log"], I["approval_witness"]["record_sha256"], I["T_pulse"], I["rule_sha256"], I["beacon_round"])
                e = H.append(ctx["log"], {"stage": "builder-accept", "record_sha256": I["beacon_record_sha256"], "outcome": "ACCEPT-DRAND", "seed_hex": I["seed_hex"], "source": "drand-mainnet-default"}); I["collection_lock"] = {"first_accept": e, "log_sha256": rc.sha_file(ctx["log"]), "entries": 2}
                TF.git(wk, "add", ctx["log"].name); TF.git(wk, "commit", "-q", "-m", "rewrite"); c = TF.git(wk, "rev-parse", "HEAD"); TF.git(wk, "push", "-q", "origin", "HEAD:" + REF); evs.append(self.pev(c, len(evs), wk))
            env["genuine"] = json.loads(json.dumps(ev))
            if defect == "approval-local": ev.update({"repo": {"name": "wrong/repo"}})
            if defect == "approval-delivery": gp = TF.git(wk, "rev-parse", ev["payload"]["head"] + "^"); ev["payload"].update({"before": gp, "head": gp, "commits": []})   # positive non-delivery
            I["approval_witness"]["push_event_sha256"] = canon(ev)
            if defect == "identity-local": I["schema_version"] = "WRONG"
        ident = TF.identity(env["tmp"], env["cTP"], ids, self.hold, mutate=publish, **({"lock_ok": False} if defect == "conjunction" else {}))
        ev = json.loads(ident.read_text())["approval_witness"]["push_event"]; env["ev"] = ev
        if defect == "open-local": of.write_text(json.dumps({**evs[0], "repo": {"name": "wrong/repo"}}))
        if defect == "open-delivery-auth": gp = TF.git(wk, "rev-parse", evs[0]["payload"]["before"] + "^"); of.write_text(json.dumps({**evs[0], "payload": {**evs[0]["payload"], "before": gp, "head": gp, "commits": []}}))
        live = [ev] + evs
        if defect == "approval-live": live = [{**env["genuine"], "payload": {**env["genuine"]["payload"], "before": "0" * 40}}] + evs                      # a conflicting same-id copy in the feed
        if defect == "open-same-id": live = [ev, {**evs[0], "payload": {**evs[0]["payload"], "before": "0" * 40}}] + evs[1:]
        if defect == "per-entry": live = [ev, evs[0], {"type": "PushEvent", "id": "batch", "created_at": "2026-09-06T09:59:00Z", "repo": {"name": REPO}, "payload": {"ref": REF, "before": evs[1]["payload"]["head"], "head": evs[-1]["payload"]["head"]}}]
        env["live"] = live; return ident, env
EXPECTED_DEFECT_CODE = {"approval-local": "EVENT-INCONSISTENT", "approval-delivery": "EVENT-INCONSISTENT", "open-local": "HISTORY-CONTINUATION: OPEN-EVENT-INCONSISTENT-INPUT", "identity-local": "IDENTITY-SCHEMA", "lists": "IDENTITY-tuning_objids-SIZE-OR-TYPE", "conjunction": "IDENTITY-LOCK-MISMATCH", "approval-live": "EVENT-FORGED", "open-same-id": "HISTORY-CONTINUATION: OPEN-EVENT-FORGED", "seed": "REDERIVE-RETRY", "history-remote": "HISTORY-CONTINUATION", "open-delivery-auth": "HISTORY-CONTINUATION", "per-entry": "HISTORY-CONTINUATION"}
EXPECTED_DEFECT_REASON = {"history-remote": "NOT-AN-EXTENSION", "open-delivery-auth": "OPEN-EVENT-INCONSISTENT-INPUT", "per-entry": "HISTORY-PUBLICATION-BATCH"}
def fail_prereq(P_, env):
    """make prerequisite P fail — labelled: monkeypatches where codex used them; returns a context manager and the runner to use"""
    live = env["live"]
    if P_ == "open-file": env["of"].write_text("null"); return mock.patch.dict(os.environ, {}), feed(live)
    if P_ == "witness-fetch": return mock.patch.object(rc, "verify_witness", side_effect=rc.DataIntegrityFail("WITNESS-FETCH-FAILED fixture transport unavailable")), feed(live)
    if P_ == "verifier-import": return mock.patch.object(rc, "_drand_modules", side_effect=rc.DataIntegrityFail("VERIFIER-UNAVAILABLE: fixture — py_ecc unavailable")), feed(live)
    if P_ == "events-page1": return mock.patch.dict(os.environ, {}), feed(live, page1_fail=True)
    if P_ == "events-later-page":
        filler = [{"type": "IssuesEvent", "id": f"f{i}", "created_at": "2026-09-06T09:40:00Z", "repo": {"name": REPO}, "payload": {}} for i in range(100 - len(live))]
        return mock.patch.dict(os.environ, {}), feed(live + filler, page2=lambda cmd: (1, "", "gh: HTTP 503: Service Unavailable"))
    if P_ == "remote-head": return mock.patch.object(P, "remote_head", lambda url, ref: None), feed(live)
    if P_ == "git-launch":
        real = subprocess.run
        def failing(args, *a, **k):
            if args and args[0] == "git": raise OSError("fixture: git cannot launch")
            return real(args, *a, **k)
        return mock.patch("subprocess.run", side_effect=failing), feed(live)
    raise ValueError(P_)
class NSD_FromTheTable(unittest.TestCase):
    """generated: for each prerequisite P and each check C with P ∉ needs(C): plant C's defect, fail P, assert the WHOLE outcome"""
    @classmethod
    def setUpClass(cls): cls.t = TF.T("test_composed_mode_on_the_production_call_path"); cls.t.setUp(); cls.h = Harness(cls.t)
    @classmethod
    def tearDownClass(cls): cls.t.tearDown()
def _make(P_, C):
    def test(self):
        ident, env = self.h.build(defect=C); ctx, runner = fail_prereq(P_, env)
        with ctx:
            with self.assertRaises(rc.DataIntegrityFail) as cm: rc.load_identity(ident, rc.Protocol(**{**env["cTP"].__dict__, "events_runner": runner}))
        msg = str(cm.exception); out = getattr(rc, "LAST_OUTCOME", None)
        codes = {f["code"] for f in (out or {}).get("findings", [])}
        want = EXPECTED_DEFECT_CODE[C]; self.assertTrue(msg.startswith(want) or want in codes, f"[{P_} fails; defect {C}] expected {want} contributed; got winner {msg[:120]!r}; findings {sorted(codes)}")
        self.assertIsNotNone(out, "whole outcome not recorded (LAST_OUTCOME)"); fs = out["findings"]
        self.assertTrue(all(f.get("why") for f in fs), "every finding carries a reason")
        self.assertIn(rc.PREREQUISITES[P_]["failure_code"], codes | {msg.split(":")[0]}, f"the prerequisite failure itself is a finding: {sorted(codes)}")
        if C in EXPECTED_DEFECT_REASON: self.assertTrue(any(EXPECTED_DEFECT_REASON[C] in f.get("why", "") for f in fs if f["code"] == want), f"reason {EXPECTED_DEFECT_REASON[C]} recorded: {[f['why'][:60] for f in fs]}")
        blocked = {k for k, v in out["stages"].items() if v.get("state") == "blocked"} | set(out.get("blocked", {}).keys()); pf = rc.PREREQUISITES[P_]["failure_code"]
        for other, spec in rc.INDEPENDENCE.items():
            if P_ not in spec["needs"] or other == C: continue
            reporter = any(f["code"] == pf and f["stage"] == spec["stage"] for f in fs)                                                   # the check that itself REPORTS the prerequisite failure is not "blocked" by it
            contributed_any = any(f["stage"] == spec["stage"] for f in fs)                                                           # the stage CONTRIBUTED (unavailability, or its own refusal reached before it needed P) — a contribution, not a skip
            self.assertTrue(other in blocked or spec["stage"] in blocked or reporter or contributed_any, f"check {other} needs {P_}: it must be recorded BLOCKED or contribute unavailability, never be skipped silently: blocked={sorted(blocked)}, findings={[(f['stage'], f['code']) for f in fs]}")
        winner = P.resolve([P.finding(f["class"], f["code"], f["why"], f["stage"], i) for i, f in enumerate(fs)]); self.assertTrue(msg.startswith(winner["code"]), f"the winner is the resolver's: {msg[:80]!r} vs {winner['code']}")
    return test
for P_ in rc.PREREQUISITES:
    if P_ == "identity-file": continue
    for C, spec in rc.INDEPENDENCE.items():
        if P_ in spec["needs"]: continue
        setattr(NSD_FromTheTable, f"test_{P_.replace('-', '_')}_fails__{C.replace('-', '_')}_still_contributed", _make(P_, C))
# ---------------------------------------------------------------- codex's V31 constructions as REGRESSIONS, one subcase per method
class Regressions(unittest.TestCase):
    @classmethod
    def setUpClass(cls): cls.t = TF.T("test_composed_mode_on_the_production_call_path"); cls.t.setUp(); cls.h = Harness(cls.t)
    @classmethod
    def tearDownClass(cls): cls.t.tearDown()
    def refusal(self, ident, env, runner, ctx=None):
        with (ctx or mock.patch.dict(os.environ, {})):
            with self.assertRaises(rc.DataIntegrityFail) as cm: rc.load_identity(ident, rc.Protocol(**{**env["cTP"].__dict__, "events_runner": runner}))
        return str(cm.exception)
    def test_V31_1a_fetch_failure_plus_same_id_contradiction(self):
        ident, env = self.h.build(defect="approval-live"); calls = []
        msg = self.refusal(ident, env, feed(env["live"], counter=calls), mock.patch.object(rc, "verify_witness", side_effect=rc.DataIntegrityFail("WITNESS-FETCH-FAILED fixture transport unavailable")))
        self.assertTrue(msg.startswith("EVENT-FORGED"), msg); self.assertGreaterEqual(len(calls), 1)
    def test_V31_1b_fetch_failure_plus_wrong_schema(self):
        ident, env = self.h.build(defect="identity-local"); msg = self.refusal(ident, env, feed(env["live"]), mock.patch.object(rc, "verify_witness", side_effect=rc.DataIntegrityFail("WITNESS-FETCH-FAILED fixture transport unavailable"))); self.assertTrue(msg.startswith("IDENTITY-SCHEMA"), msg)
    def test_V31_1c_fetch_failure_plus_rewrite(self):
        ident, env = self.h.build(defect="history-remote"); msg = self.refusal(ident, env, feed(env["live"]), mock.patch.object(rc, "verify_witness", side_effect=rc.DataIntegrityFail("WITNESS-FETCH-FAILED fixture transport unavailable"))); self.assertIn("NOT-AN-EXTENSION", msg)
    def test_V31_1d_git_launch_failure_plus_wrong_repository(self):
        ident, env = self.h.build(defect="approval-local"); ctx, runner = fail_prereq("git-launch", env); msg = self.refusal(ident, env, runner, ctx); self.assertTrue(msg.startswith("EVENT-INCONSISTENT"), msg)
    def test_V31_1e_helper_import_unavailable_is_named(self):
        ident, env = self.h.build(); msg = self.refusal(ident, env, feed(env["live"]), mock.patch.object(rc, "_P", side_effect=ImportError("fixture: provenance helpers unavailable"))); self.assertTrue(msg.startswith("VERIFIER-UNAVAILABLE"), msg)
    def test_V31_2a_later_page_503_keeps_the_contradiction(self):
        ident, env = self.h.build(defect="approval-live"); ctx, runner = fail_prereq("events-later-page", env); msg = self.refusal(ident, env, runner, ctx); self.assertTrue(msg.startswith("EVENT-FORGED"), msg)
    def test_V31_2b_later_page_malformed_keeps_the_contradiction(self):
        ident, env = self.h.build(defect="approval-live"); filler = [{"type": "IssuesEvent", "id": f"f{i}", "created_at": "2026-09-06T09:40:00Z", "repo": {"name": REPO}, "payload": {}} for i in range(100 - len(env["live"]))]
        msg = self.refusal(ident, env, feed(env["live"] + filler, page2=lambda cmd: (0, "not json", ""))); self.assertTrue(msg.startswith("EVENT-FORGED"), msg)
    def test_V31_2c_partial_without_contradiction_never_accepts(self):
        ident, env = self.h.build(); ctx, runner = fail_prereq("events-later-page", env); msg = self.refusal(ident, env, runner, ctx); self.assertTrue(msg.startswith("RETRY-EVENTS-UNAVAILABLE"), msg)
    def test_V31_3a_per_entry_loop_reaches_the_proven_batch(self):
        ident, env = self.h.build(defect="per-entry"); msg = self.refusal(ident, env, feed(env["live"])); self.assertIn("HISTORY-PUBLICATION-BATCH", msg); self.assertFalse(msg.startswith("RETRY-"), msg)
    def test_V31_3b_same_commit_arm_before_availability(self):
        tmp = Path(tempfile.mkdtemp()); g = lambda *a: subprocess.run(["git", *a], cwd=tmp, capture_output=True, text=True, check=True).stdout.strip()
        g("init", "-q"); g("config", "user.email", "t@t"); g("config", "user.name", "t"); (tmp / "a").write_text("a"); g("add", "a"); g("commit", "-q", "-m", "base"); base = g("rev-parse", "HEAD"); (tmp / "b").write_text("b"); g("add", "b"); g("commit", "-q", "-m", "approval"); commit = g("rev-parse", "HEAD"); (tmp / "c").write_text("c"); g("add", "c"); g("commit", "-q", "-m", "later"); later = g("rev-parse", "HEAD")
        retained = {"type": "PushEvent", "id": "mine", "created_at": "2026-09-07T01:00:00Z", "repo": {"name": REPO}, "payload": {"ref": REF, "before": "e" * 40, "head": later}}
        genuine = {"type": "PushEvent", "id": "g1", "created_at": "2026-09-07T01:00:00Z", "repo": {"name": REPO}, "payload": {"ref": REF, "before": base, "head": commit, "commits": [{"sha": commit}]}}
        o, why = P.authenticate_event(retained, [genuine], REPO, REF, commit, root=tmp); self.assertEqual(o, "FORGED", why)
    def test_V31_3c_standalone_path_sweeps_the_open_event_locally(self):
        tmp = Path(tempfile.mkdtemp()); subprocess.run(["git", "init", "-q", str(tmp)], check=True)
        wrong = {"type": "PushEvent", "id": "o", "created_at": "2026-09-07T01:00:00Z", "repo": {"name": "wrong/repo"}, "payload": {"ref": REF, "before": "1" * 40, "head": "2" * 40}}
        with mock.patch.object(P, "remote_head", lambda url, ref: None): ok, why, info = P.validate_continuation_v12(tmp, "x.jsonl", str(tmp), REF, wrong, feed([wrong]), REPO)
        self.assertFalse(ok); self.assertIn("OPEN-EVENT-INCONSISTENT-INPUT", why)
    def test_V31_4a_split_codes_classified_and_unknown_family_member_flagged(self):
        for c in ("SPLIT-INPUTS", "SPLIT-NOT-REPRODUCED"): got = P.classify_refusal(f"{c}: x"); self.assertEqual(got[0], "LOCAL-TERMINAL"); self.assertFalse(got[3], c)
        self.assertTrue(P.classify_refusal("EVENT-NEW-UNKNOWN: x")[3])
    def test_V31_4b_every_code_raised_by_the_sources_is_classified_unflagged(self):
        """exercises the OLD classification behaviour (classify_refusal exists in v11): every refusal code the driver and the helpers actually raise must be placed WITHOUT the unclassified flag — on the old bytes SPLIT-* and others are flagged, so this fails genuinely"""
        drv = (D / "fourier_chirality" / "run_configurations_v16.py").read_text(encoding="utf-8"); prov = (D / "track2" / "provenance_designs_v12.py").read_text(encoding="utf-8")
        codes = set(re.findall(r'DataIntegrityFail\(f?"([A-Z][A-Za-z0-9_-]*?[A-Z0-9])[ :"{]', drv)) | set(re.findall(r'"((?:RECEIPT|PUBLISH|HISTORY|OPEN-EVENT|OPEN-NOT|EVIDENCE|PENDING|RETRY|STALE|MALFORMED|IO|STAGE)-[A-Z0-9-]+):', prov))
        flagged = sorted(c for c in codes if not c.endswith("-") and P.classify_refusal(f"{c}: x")[3]); self.assertEqual(flagged, [], f"raised by the sources but flagged as unclassified: {flagged}")
    def test_V31_4c_malformed_remote_event_is_remote_evidence(self):
        ident, env = self.h.build(); bad = {"type": "PushEvent", "id": "bad", "created_at": "2026-09-06T09:45:00Z", "repo": {"name": REPO}, "payload": "scalar"}
        msg = self.refusal(ident, env, feed([env["ev"], bad] + env["evs"])); self.assertIn("MALFORMED-REMOTE-EVIDENCE", msg); self.assertNotIn("MALFORMED-RETAINED-INPUT", msg)
    def test_V31_4d_receipt_exception_follows_the_receipt_policy(self):
        ident, env = self.h.build(); wk = env["wk"]; far = {"type": "PushEvent", "id": "z", "created_at": "2027-01-01T00:00:00Z", "repo": {"name": REPO}, "payload": {"ref": REF, "before": "1" * 40, "head": "2" * 40, "commits": [{"sha": "2" * 40}]}}
        rp = wk / "RECEIPT.json"; P.write_events_receipt(rp, env["live"], {"endpoints": ["x"], "retrieved_utc": "2026-09-06T10:00:00Z"}, {"actor": "ops-witness", "session": "OPS"}); r = json.loads(rp.read_text()); r["origin"] = ["ops-witness"]; rp.write_text(json.dumps(r)); TF.git(wk, "add", rp.name); TF.git(wk, "commit", "-q", "-m", "receipt"); TF.git(wk, "push", "-q", "origin", "HEAD:" + REF)
        with self.assertRaises(rc.DataIntegrityFail) as cm: rc.load_identity(ident, rc.Protocol(**{**env["cTP"].__dict__, "events_receipt": str(rp), "expected_receipt_origin": {"actor": "ops-witness", "session": "OPS"}, "events_runner": feed([far])}))
        self.assertTrue(str(cm.exception).startswith("EVENT-EXPIRED-RECEIPT-REFUSED"), str(cm.exception))
    def test_V31_5a_blocked_stage_state_recorded(self):
        """NEW-INTERFACE test (LAST_OUTCOME does not exist before v16): no fail-first standing — Blanc 05:09 item 2"""
        ident, env = self.h.build(); env["of"].write_text("null"); self.refusal(ident, env, feed(env["live"])); out = rc.LAST_OUTCOME
        self.assertIn("open-delivery-auth", out["blocked"], out["blocked"]); self.assertIn("open", out["blocked"]["open-delivery-auth"].lower()); self.assertIn("open-same-id", out["blocked"])   # the CHECKS that need the open event are recorded blocked with the reason; S5's remote checks still ran (its stage state is completed), nothing was skipped silently
        self.assertEqual(out["stages"]["S5-history"]["state"], "completed"); self.assertTrue(all(v["state"] in ("completed", "refused", "blocked") for v in out["stages"].values()), out["stages"])
    def test_V31_5b_findings_carry_reasons(self):
        """NEW-INTERFACE test (LAST_OUTCOME): no fail-first standing"""
        ident, env = self.h.build(defect="approval-local"); self.refusal(ident, env, feed(env["live"])); fs = rc.LAST_OUTCOME["findings"]; self.assertTrue(fs and all(f.get("why") for f in fs), fs)
class V31_Text(unittest.TestCase):
    def test_claims_match_the_code(self):
        r = Path(os.environ["RULE_TEXT"]).read_text(encoding="utf-8"); sec = r[r.index("3c. V3"):]; sec = sec[:sec.index("\n")]
        for k in ("(V31-1)", "(V31-2)", "(V31-3)", "(V31-4)", "(V31-5)", "NSD", "No Stage Decides", "run_configurations_v16", "provenance_designs_v12", "CLASS_ALLOWLIST", "MALFORMED-REMOTE-EVIDENCE", "INDEPENDENCE", "PREREQUISITES", "blocked", "partial", "coherent_attacks_v32.py"): self.assertIn(k, r, k)
        self.assertNotIn("every derivable finding", sec); self.assertNotIn("nothing downstream is skipped", sec); self.assertIn("INDEPENDENCE TABLE", sec)
if __name__ == "__main__": unittest.main()
