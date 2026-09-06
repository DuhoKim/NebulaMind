"""TRACK 8 FAIL-FIRST tests — codex's V27 findings V27-1 (precedence), V27-2 (tri-state propagation), V27-3 (names) — Blanc 02:06: these are CONTRADICTIONS
between text and code, to be REPAIRED. Targets the SUCCESSORS (provenance_designs_v8, run_configurations_v12, collector v28, builder v28); run FIRST against
byte-copies of the V27 modules (import lines renamed only), classified per test. Local repositories and fixture runners — labelled. Pinned V27 files untouched."""
import json, os, sys, tempfile, unittest, hashlib, subprocess
from pathlib import Path
HERE = Path(__file__).resolve().parent; D = HERE.parent
for p in ("beacon_v2", "drand_only", "corpus_identity", "fourier_chirality", "track2"): sys.path.insert(0, str(D / p))
import provenance_designs_v8 as P
def git(cwd, *a, check=True):
    r = subprocess.run(["git", *a], cwd=cwd, capture_output=True, text=True)
    if check and r.returncode: raise RuntimeError(r.stderr)
    return r.stdout.strip()
REF = "refs/heads/main"; REPO = "DuhoKim/NebulaMind"
def ev(commit, before, n, **extra):
    e = {"type": "PushEvent", "id": f"h{n}", "created_at": f"2026-09-07T01:{n:02d}:00Z", "repo": {"name": REPO}, "payload": {"ref": REF, "before": before, "head": commit, "commits": [{"sha": commit}]}}; e.update(extra); return e
def feed(events): return lambda cmd: (0, json.dumps(events if cmd[-1].endswith("page=1") else []), "")
class Repo(unittest.TestCase):
    def setUp(self):
        self.tmp = Path(tempfile.mkdtemp()); self.bare = self.tmp / "remote.git"; self.work = self.tmp / "work"
        subprocess.run(["git", "init", "-q", "--bare", str(self.bare)], check=True); subprocess.run(["git", "clone", "-q", str(self.bare), str(self.work)], check=True, capture_output=True); git(self.work, "config", "user.email", "t@t"); git(self.work, "config", "user.name", "t")
        (self.work / "s").write_text("x"); git(self.work, "add", "s"); git(self.work, "commit", "-q", "-m", "init"); git(self.work, "push", "-q", "-u", "origin", "HEAD:" + REF); self.base = git(self.work, "rev-parse", "HEAD")
        (self.work / "a").write_text("a"); git(self.work, "add", "a"); git(self.work, "commit", "-q", "-m", "approval"); self.commit = git(self.work, "rev-parse", "HEAD"); git(self.work, "push", "-q", "origin", "HEAD:" + REF)
        self.stale = self.tmp / "stale"; subprocess.run(["git", "clone", "-q", str(self.bare), str(self.stale)], check=True, capture_output=True)
        (self.work / "l").write_text("l"); git(self.work, "add", "l"); git(self.work, "commit", "-q", "-m", "later"); self.head = git(self.work, "rev-parse", "HEAD"); git(self.work, "push", "-q", "origin", "HEAD:" + REF)
class V27_1_Precedence(Repo):
    def test_same_id_contradiction_beats_undetermined_delivery(self):          # codex V27-1(a)
        genuine = ev(self.commit, self.base, 5); live = [ev("c" * 40, "d" * 40, 1), genuine]
        retained = json.loads(json.dumps(genuine)); retained["payload"]["head"] = self.head; retained["payload"]["commits"] = []      # same id; head changed to one the stale clone lacks (ancestry undeterminable there)
        o, why = P.authenticate_event(retained, live, REPO, REF, self.commit, feed_reaches_back_to=live[0]["created_at"], root=self.stale)
        self.assertEqual(o, "FORGED", why)
    def test_same_id_differently_encoded_copy_beats_verbatim_presence(self):   # codex V27-1(b)
        genuine = ev(self.commit, self.base, 5); copy = json.loads(json.dumps(genuine)); copy["payload"]["before"] = "0" * 40
        o, why = P.authenticate_event(genuine, [genuine, copy], REPO, REF, self.commit, root=self.work); self.assertEqual(o, "FORGED", why)
    def test_local_mismatch_decided_before_retrieval(self):                    # codex V27-1(c): wrong repository + HTTP 503 must be INCONSISTENT-INPUT, not UNAVAILABLE
        wrong = ev(self.commit, self.base, 5, repo={"name": "other/repo"})
        o, why, prov = P.authenticate_event_live(wrong, REPO, lambda cmd: (1, "", "gh: HTTP 503: Service Unavailable"), REF, self.commit, root=self.work); self.assertEqual(o, "INCONSISTENT-INPUT", why)
        nondeliver = ev("f" * 40, "g" * 40, 1)
        o, why, prov = P.authenticate_event_live(nondeliver, REPO, lambda cmd: (1, "", "gh: HTTP 503: Service Unavailable"), REF, self.commit, root=self.work); self.assertEqual(o, "INCONSISTENT-INPUT", why)
        anc = {"type": "PushEvent", "id": "anc", "created_at": "2026-09-07T01:05:00Z", "repo": {"name": REPO}, "payload": {"ref": REF, "before": self.base, "head": self.head}}
        o, why, prov = P.authenticate_event_live(anc, REPO, lambda cmd: (1, "", "gh: HTTP 503: Service Unavailable"), REF, self.commit, root=self.stale); self.assertEqual(o, "UNAVAILABLE", why)   # undetermined + unavailable feed: retry
class V27_2_TriStatePropagation(Repo):
    def test_git_launch_failure_is_undetermined(self):                         # codex V27-2: a git process-launch exception must be UNDETERMINED, not raise
        anc = {"type": "PushEvent", "id": "anc", "created_at": "2026-09-07T01:05:00Z", "repo": {"name": REPO}, "payload": {"ref": REF, "before": self.base, "head": self.head}}
        self.assertEqual(P.delivery(anc, self.commit, REF, self.tmp / "not-a-repo"), "UNDETERMINED")
        import unittest.mock as um
        with um.patch.object(P.subprocess, "run", side_effect=OSError("git cannot launch")): self.assertEqual(P.delivery(anc, self.commit, REF, self.work), "UNDETERMINED")
    def test_open_event_stage_is_tri_state(self):                              # codex V27-2: the open-event stage must not turn UNDETERMINED into OPEN-EVENT-DOES-NOT-DELIVER
        import history_v2 as H
        log = self.work / "collection_log.jsonl"; H.genesis(log, "a" * 64, "t", "b" * 64, 1); oc = P.publish_entry(self.work, log.name, str(self.bare), REF, "open")
        (self.work / "m").write_text("m"); git(self.work, "add", "m"); git(self.work, "commit", "-q", "-m", "after open"); h2 = git(self.work, "rev-parse", "HEAD"); git(self.work, "push", "-q", "origin", "HEAD:" + REF)
        und = {"type": "PushEvent", "id": "open-und", "created_at": "2026-09-07T01:06:00Z", "repo": {"name": REPO}, "payload": {"ref": REF, "before": "e" * 40, "head": h2}}   # claims oc only by before..head; `before` is an object no clone holds (a force-pushed-away parent) — UNDETERMINED even after the validator's fetch
        ok, why, info = P.validate_continuation_v8(self.work, log.name, str(self.bare), REF, und, feed([und]), REPO)
        self.assertFalse(ok); self.assertNotIn("DOES-NOT-DELIVER", why); self.assertTrue(why.startswith("EVIDENCE-UNAVAILABLE"), why)
        gp = git(self.work, "rev-parse", oc + "^^"); nd = {"type": "PushEvent", "id": "open-nd", "created_at": "2026-09-07T01:06:00Z", "repo": {"name": REPO}, "payload": {"ref": REF, "before": gp, "head": gp}}   # ancestry ESTABLISHED false → positive non-delivery, terminal
        ok, why, info = P.validate_continuation_v8(self.work, log.name, str(self.bare), REF, nd, feed([nd]), REPO)
        self.assertFalse(ok); self.assertTrue(why.startswith("OPEN-EVENT-INCONSISTENT-INPUT"), why)

class V27_2_DriverPath(unittest.TestCase):
    """codex V27-2 on the COMPLETE path: driver v12's witness-commit precheck and the composed open-event stage, with the labelled fixture of test_run_configurations_v12."""
    def test_precheck_and_open_stage_tri_state_on_the_complete_path(self):
        sys.path.insert(0, str(D / "fourier_chirality")); import run_configurations_v12 as rc, test_run_configurations_v12 as TF, hashlib, tempfile as tf
        t = TF.T("test_composed_mode_on_the_production_call_path"); t.setUp()
        try:
            rows = t.rows(6); ids = [r[0] for r in rows]; hold = [str(500000 + i) for i in range(60)]
            def canon(e): return hashlib.sha256(json.dumps(e, sort_keys=True, separators=(",", ":")).encode()).hexdigest()
            def pev(commit, n, wk): return {"type": "PushEvent", "id": f"h{n}", "created_at": f"2026-09-06T09:{50 + n:02d}:00Z", "repo": {"name": "DuhoKim/NebulaMind"}, "payload": {"ref": "refs/heads/main", "before": TF.git(wk, "rev-parse", commit + "^"), "head": commit, "commits": [{"sha": commit}]}}
            def feed(events): return lambda cmd: (0, json.dumps(events if cmd[-1].endswith("page=1") else []), "")
            def fresh():
                tmp = Path(tf.mkdtemp()); TP = TF.TPJ(tmp); rc.ADOPTION_FILE = Path(t.TP.adoption_file); wk = Path(TP.seal_journal).parent; TF.git(TP.witness_remote_url, "config", "receive.denyNonFastforwards", "true")
                of = wk / "HISTORY_OPEN_EVENT.json"; evs = []; cTP = rc.Protocol(**{**TP.__dict__, "provenance_mode": "composed", "events_repo": "DuhoKim/NebulaMind", "history_open_event_file": str(of)}); return tmp, TP, wk, of, evs, cTP
            def publish(I, ctx, wk, of, evs, witness_payload=None):
                ev = I["approval_witness"]["push_event"]; ev["repo"] = {"name": "DuhoKim/NebulaMind"}
                log = ctx["log"]; lines = [l for l in log.read_bytes().split(b"\n") if l]
                for n in range(len(lines)):
                    log.write_bytes(b"\n".join(lines[: n + 1]) + b"\n"); TF.git(wk, "add", log.name); TF.git(wk, "commit", "-q", "-m", f"history entry {n}"); c = TF.git(wk, "rev-parse", "HEAD"); TF.git(wk, "push", "-q", "origin", "HEAD:refs/heads/main"); evs.append(pev(c, n, wk))
                    if n == 0: of.write_text(json.dumps(evs[0])); TF.git(wk, "add", of.name)
                if witness_payload: ev["payload"] = witness_payload(ev["payload"], evs)
                I["approval_witness"]["push_event_sha256"] = canon(ev)
            # (a) witness-commit precheck, UNDETERMINED: the approval event's `before` is an object no clone holds (a force-pushed-away parent), head a later real commit
            tmp, TP, wk, of, evs, cTP = fresh()
            ident = TF.identity(tmp, cTP, ids, hold, mutate=lambda I, ctx: publish(I, ctx, wk, of, evs, witness_payload=lambda p, evs: {**p, "before": "e" * 40, "head": evs[-1]["payload"]["head"], "commits": []}))
            ev = json.loads(ident.read_text())["approval_witness"]["push_event"]
            with self.assertRaises(rc.DataIntegrityFail) as cm: rc.load_identity(ident, TP)
            self.assertIn("IDENTITY-WITNESS-COMMIT-UNDETERMINED", str(cm.exception)); self.assertFalse(str(cm.exception).startswith("RETRY-"))          # offline: named, no retry vocabulary
            with self.assertRaises(rc.DataIntegrityFail) as cm: rc.load_identity(ident, rc.Protocol(**{**cTP.__dict__, "events_runner": feed([ev] + evs)}))
            self.assertTrue(str(cm.exception).startswith("RETRY-EVENTS-UNAVAILABLE"), str(cm.exception))                                                # composed: retry, not IDENTITY-WITNESS-COMMIT
            # (b) witness-commit precheck, POSITIVE non-delivery: before = head = the approval commit's parent (ancestry established false)
            tmp, TP, wk, of, evs, cTP = fresh()
            ident = TF.identity(tmp, cTP, ids, hold, mutate=lambda I, ctx: publish(I, ctx, wk, of, evs, witness_payload=lambda p, evs: {**p, "before": TF.git(wk, "rev-parse", p["head"] + "^"), "head": TF.git(wk, "rev-parse", p["head"] + "^"), "commits": []}))
            ev = json.loads(ident.read_text())["approval_witness"]["push_event"]
            with self.assertRaises(rc.DataIntegrityFail) as cm: rc.load_identity(ident, rc.Protocol(**{**cTP.__dict__, "events_runner": feed([ev] + evs)}))
            self.assertTrue(str(cm.exception).startswith("EVENT-INCONSISTENT: IDENTITY-WITNESS-COMMIT"), str(cm.exception))
            # (c) open-event stage, UNDETERMINED: the retained history-open event claims the open commit only by before..head with an unknown `before`
            tmp, TP, wk, of, evs, cTP = fresh()
            ident = TF.identity(tmp, cTP, ids, hold, mutate=lambda I, ctx: publish(I, ctx, wk, of, evs)); ev = json.loads(ident.read_text())["approval_witness"]["push_event"]
            und = {**evs[0], "payload": {**evs[0]["payload"], "before": "e" * 40, "head": evs[1]["payload"]["head"], "commits": []}}; of.write_text(json.dumps(und))
            with self.assertRaises(rc.DataIntegrityFail) as cm: rc.load_identity(ident, rc.Protocol(**{**cTP.__dict__, "events_runner": feed([ev, und] + evs[1:])}))
            self.assertTrue(str(cm.exception).startswith("RETRY-HISTORY-CONTINUATION: EVIDENCE-UNAVAILABLE"), str(cm.exception)); self.assertNotIn("DOES-NOT-DELIVER", str(cm.exception))
            # (d) open-event stage, POSITIVE non-delivery: before = head = the open commit's parent
            gp = TF.git(wk, "rev-parse", evs[0]["payload"]["before"] + "^"); nd = {**evs[0], "payload": {**evs[0]["payload"], "before": gp, "head": gp, "commits": []}}; of.write_text(json.dumps(nd))   # before = head = the open commit's GRANDparent (its parent is the approval commit, which the event must not deliver either)
            with self.assertRaises(rc.DataIntegrityFail) as cm: rc.load_identity(ident, rc.Protocol(**{**cTP.__dict__, "events_runner": feed([ev] + evs[1:])}))
            self.assertTrue(str(cm.exception).startswith("HISTORY-CONTINUATION: OPEN-EVENT-INCONSISTENT-INPUT"), str(cm.exception))
        finally: t.tearDown()

class V27_3_Text(unittest.TestCase):
    def test_names_and_count(self):
        r = Path(os.environ["RULE_TEXT"]).read_text(encoding="utf-8"); d12 = (D / "fourier_chirality" / "run_configurations_v12.py").read_text(encoding="utf-8"); p8 = (D / "track2" / "provenance_designs_v8.py").read_text(encoding="utf-8"); t2 = Path(os.environ["DESIGN_TEXT"]).read_text(encoding="utf-8"); insp = (D / "track1" / "coherent_attacks_v28.py").read_text(encoding="utf-8")
        self.assertNotIn("v10 (V26: composed on provenance_designs_v7)", d12); self.assertIn("v10 (V26: composed on provenance_designs_v6)", d12); self.assertNotIn("validate_continuation_v6(", d12); self.assertNotIn("track-2 v6", d12)
        self.assertNotIn("v1's pure decision, unchanged", p8); self.assertNotIn("The pure decision: (outcome, why). v3:", p8)
        self.assertIn("132 tests across the 20 suites", r); self.assertNotIn("seventeen suites", r); self.assertNotIn("124 tests across", r)   # codex: V27 said seventeen, its logs held 18; V28 executes 20 (track 8 + its text test) and says so; self.assertNotIn("THIS candidate — two still pass", r)
        self.assertNotIn("driver v10", insp); self.assertIn("V28", insp); self.assertIn("INCONSISTENT-INPUT", t2.split("## (b)")[0])
        self.assertIn("DISCLOSED LIMITS", r); self.assertIn("REPAIRED CONTRADICTIONS", r)
if __name__ == "__main__": unittest.main()
