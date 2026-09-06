"""TRACK 9 FAIL-FIRST tests — codex's V28 findings V28-1 (the driver's witness precheck pre-empts the repaired precedence), V28-2 (the open-event wrapper does the same),
V28-3 (names/pins/wording). COMBINED conditions on the COMPLETE paths (Blanc 02:06: contradictions, repaired). Targets the SUCCESSORS (provenance_designs_v9,
run_configurations_v13); run FIRST against byte-copies of the V28 modules (import lines renamed only). Labelled fixture runners; local bare repositories."""
import json, os, sys, tempfile, unittest, hashlib, subprocess
from pathlib import Path
HERE = Path(__file__).resolve().parent; D = HERE.parent
for p in ("beacon_v2", "drand_only", "corpus_identity", "fourier_chirality", "track2"): sys.path.insert(0, str(D / p))
import provenance_designs_v9 as P
def git(cwd, *a):
    r = subprocess.run(["git", *a], cwd=cwd, capture_output=True, text=True); assert r.returncode == 0, r.stderr; return r.stdout.strip()
REF = "refs/heads/main"; REPO = "DuhoKim/NebulaMind"
def feed(events): return lambda cmd: (0, json.dumps(events if cmd[-1].endswith("page=1") else []), "")
def canon(e): return hashlib.sha256(json.dumps(e, sort_keys=True, separators=(",", ":")).encode()).hexdigest()
class V28_1_2_CompletePaths(unittest.TestCase):
    """the COMPLETE composed path (driver v13 with the labelled fixture of test_run_configurations_v13): combined conditions codex built for V28-1 / V28-2."""
    def test_precedence_survives_the_prechecks(self):
        sys.path.insert(0, str(D / "fourier_chirality")); import run_configurations_v13 as rc, test_run_configurations_v13 as TF, tempfile as tf
        t = TF.T("test_composed_mode_on_the_production_call_path"); t.setUp()
        try:
            rows = t.rows(6); ids = [r[0] for r in rows]; hold = [str(500000 + i) for i in range(60)]
            def pev(commit, n, wk): return {"type": "PushEvent", "id": f"h{n}", "created_at": f"2026-09-06T09:{50 + n:02d}:00Z", "repo": {"name": REPO}, "payload": {"ref": REF, "before": TF.git(wk, "rev-parse", commit + "^"), "head": commit, "commits": [{"sha": commit}]}}
            def fresh():
                tmp = Path(tf.mkdtemp()); TP = TF.TPJ(tmp); rc.ADOPTION_FILE = Path(t.TP.adoption_file); wk = Path(TP.seal_journal).parent; TF.git(TP.witness_remote_url, "config", "receive.denyNonFastforwards", "true")
                of = wk / "HISTORY_OPEN_EVENT.json"; evs = []; cTP = rc.Protocol(**{**TP.__dict__, "provenance_mode": "composed", "events_repo": REPO, "history_open_event_file": str(of)}); return tmp, TP, wk, of, evs, cTP
            def publish(I, ctx, wk, of, evs, keep=None, mutate=None):
                ev = I["approval_witness"]["push_event"]; ev["repo"] = {"name": REPO}
                log = ctx["log"]; lines = [l for l in (log.read_bytes().split(b"\n")) if l]
                for n in range(len(lines)):
                    log.write_bytes(b"\n".join(lines[: n + 1]) + b"\n"); TF.git(wk, "add", log.name); TF.git(wk, "commit", "-q", "-m", f"history entry {n}"); c = TF.git(wk, "rev-parse", "HEAD"); TF.git(wk, "push", "-q", "origin", "HEAD:" + REF); evs.append(pev(c, n, wk))
                    if n == 0: of.write_text(json.dumps(evs[0])); TF.git(wk, "add", of.name)
                if keep is not None: keep.append(json.loads(json.dumps(ev)))                      # the GENUINE approval event, as GitHub would serve it
                if mutate: mutate(ev, evs)
                I["approval_witness"]["push_event_sha256"] = canon(ev)
            # ---- V28-1(a): approval delivery UNDETERMINED (unknown `before`, real later head, genuine id, no commits shortcut) + the live feed holds the GENUINE conflicting same-id event → EVENT-FORGED, not retry
            tmp, TP, wk, of, evs, cTP = fresh(); genuine = []
            ident = TF.identity(tmp, cTP, ids, hold, mutate=lambda I, ctx: publish(I, ctx, wk, of, evs, keep=genuine, mutate=lambda ev, evs: ev["payload"].update({"before": "e" * 40, "head": evs[-1]["payload"]["head"], "commits": []})))
            with self.assertRaises(rc.DataIntegrityFail) as cm: rc.load_identity(ident, rc.Protocol(**{**cTP.__dict__, "events_runner": feed(genuine + evs)}))
            self.assertTrue(str(cm.exception).startswith("EVENT-FORGED"), str(cm.exception))
            # ---- V28-1(b): the same undetermined payload + wrong repository → EVENT-INCONSISTENT with a healthy feed AND with HTTP 503 (locally decidable, no retrieval needed)
            tmp, TP, wk, of, evs, cTP = fresh()
            ident = TF.identity(tmp, cTP, ids, hold, mutate=lambda I, ctx: publish(I, ctx, wk, of, evs, mutate=lambda ev, evs: (ev["payload"].update({"before": "e" * 40, "head": evs[-1]["payload"]["head"], "commits": []}), ev.update({"repo": {"name": "wrong/repo"}}))))
            ev = json.loads(ident.read_text())["approval_witness"]["push_event"]
            for runner in (feed([ev] + evs), (lambda cmd: (1, "", "gh: HTTP 503: Service Unavailable"))):
                with self.assertRaises(rc.DataIntegrityFail) as cm: rc.load_identity(ident, rc.Protocol(**{**cTP.__dict__, "events_runner": runner}))
                self.assertTrue(str(cm.exception).startswith("EVENT-INCONSISTENT"), str(cm.exception))
            with self.assertRaises(rc.DataIntegrityFail) as cm: rc.load_identity(ident, TP)                    # offline keeps its named undetermined refusal (no repository pinning offline)
            self.assertIn("IDENTITY-WITNESS-COMMIT-UNDETERMINED", str(cm.exception))
            # ---- V28-1(c) regression guard: undetermined, the feed serves the retained event itself, nothing contradicts → RETRY-EVENTS-UNAVAILABLE (unchanged)
            tmp, TP, wk, of, evs, cTP = fresh()
            ident = TF.identity(tmp, cTP, ids, hold, mutate=lambda I, ctx: publish(I, ctx, wk, of, evs, mutate=lambda ev, evs: ev["payload"].update({"before": "e" * 40, "head": evs[-1]["payload"]["head"], "commits": []})))
            ev = json.loads(ident.read_text())["approval_witness"]["push_event"]
            with self.assertRaises(rc.DataIntegrityFail) as cm: rc.load_identity(ident, rc.Protocol(**{**cTP.__dict__, "events_runner": feed([ev] + evs)}))
            self.assertTrue(str(cm.exception).startswith("RETRY-EVENTS-UNAVAILABLE"), str(cm.exception))
            # ---- V28-2(a): the retained history-open event UNDETERMINED (unknown before, real later history commit, genuine id) + the runner serves the GENUINE open event → OPEN-EVENT-FORGED (terminal), not retry
            tmp, TP, wk, of, evs, cTP = fresh()
            ident = TF.identity(tmp, cTP, ids, hold, mutate=lambda I, ctx: publish(I, ctx, wk, of, evs)); ev = json.loads(ident.read_text())["approval_witness"]["push_event"]
            und = {**evs[0], "payload": {**evs[0]["payload"], "before": "e" * 40, "head": evs[1]["payload"]["head"], "commits": []}}; of.write_text(json.dumps(und))
            with self.assertRaises(rc.DataIntegrityFail) as cm: rc.load_identity(ident, rc.Protocol(**{**cTP.__dict__, "events_runner": feed([ev] + evs)}))
            self.assertTrue(str(cm.exception).startswith("HISTORY-CONTINUATION: OPEN-EVENT-FORGED"), str(cm.exception))
            # ---- V28-2(b): the same + wrong repository → OPEN-EVENT-INCONSISTENT-INPUT, terminal
            wr = {**und, "repo": {"name": "wrong/repo"}}; of.write_text(json.dumps(wr))
            with self.assertRaises(rc.DataIntegrityFail) as cm: rc.load_identity(ident, rc.Protocol(**{**cTP.__dict__, "events_runner": feed([ev] + evs)}))
            self.assertTrue(str(cm.exception).startswith("HISTORY-CONTINUATION: OPEN-EVENT-INCONSISTENT-INPUT"), str(cm.exception))
            # ---- V28-2(c) regression guard: undetermined open event, the feed serves the retained (undetermined) event itself, nothing contradicts → RETRY (EVIDENCE-UNAVAILABLE)
            of.write_text(json.dumps(und))
            with self.assertRaises(rc.DataIntegrityFail) as cm: rc.load_identity(ident, rc.Protocol(**{**cTP.__dict__, "events_runner": feed([ev, und] + evs[1:])}))
            self.assertTrue(str(cm.exception).startswith("RETRY-HISTORY-CONTINUATION: EVIDENCE-UNAVAILABLE"), str(cm.exception))
        finally: t.tearDown()
class V28_3_RuleIII(unittest.TestCase):
    """rule (iii) as codex states it: a later distinct qualifying push beside a retained earliest genuine event is AUTHENTIC; NOT-EARLIEST needs an EARLIER qualifying event."""
    def test_later_distinct_delivery_does_not_invalidate_the_earliest(self):
        tmp = Path(tempfile.mkdtemp()); git(tmp, "init", "-q"); git(tmp, "config", "user.email", "t@t"); git(tmp, "config", "user.name", "t")
        (tmp / "a").write_text("a"); git(tmp, "add", "a"); git(tmp, "commit", "-q", "-m", "base"); base = git(tmp, "rev-parse", "HEAD")
        (tmp / "b").write_text("b"); git(tmp, "add", "b"); git(tmp, "commit", "-q", "-m", "approval"); commit = git(tmp, "rev-parse", "HEAD")
        (tmp / "c").write_text("c"); git(tmp, "add", "c"); git(tmp, "commit", "-q", "-m", "later"); later = git(tmp, "rev-parse", "HEAD")
        genuine = {"type": "PushEvent", "id": "g1", "created_at": "2026-09-07T01:00:00Z", "repo": {"name": REPO}, "payload": {"ref": REF, "before": base, "head": commit, "commits": [{"sha": commit}]}}
        later_push = {"type": "PushEvent", "id": "g2", "created_at": "2026-09-07T01:05:00Z", "repo": {"name": REPO}, "payload": {"ref": REF, "before": base, "head": later}}   # re-delivers the commit by ancestry, later, distinct id
        o, why = P.authenticate_event(genuine, [genuine, later_push], REPO, REF, commit, root=tmp); self.assertEqual(o, "AUTHENTIC", why)
        earlier = {**later_push, "id": "g0", "created_at": "2026-09-07T00:55:00Z"}
        o, why = P.authenticate_event(genuine, [earlier, genuine], REPO, REF, commit, root=tmp); self.assertEqual(o, "NOT-EARLIEST", why)
        self.assertIn("a later event does not invalidate an authentic earliest event", P.__doc__)
class V28_3_Text(unittest.TestCase):
    def test_names_pins_and_wording(self):
        r = Path(os.environ["RULE_TEXT"]).read_text(encoding="utf-8"); q = Path(os.environ["QUESTIONS_TEXT"]).read_text(encoding="utf-8"); t2 = Path(os.environ["DESIGN_TEXT"]).read_text(encoding="utf-8")
        tf13 = (D / "fourier_chirality" / "test_run_configurations_v13.py").read_text(encoding="utf-8").split("\n")[0]; insp = (D / "track1" / "coherent_attacks_v29.py").read_text(encoding="utf-8")
        import hashlib as h
        d = lambda p: h.sha256((D / p).read_bytes()).hexdigest()
        self.assertIn("fixture `test_build_corpus_identity_v27.py` `" + d("corpus_identity/test_build_corpus_identity_v27.py"), r)          # the historical clause names the file the digest belongs to
        self.assertNotIn("`test_build_corpus_identity_v28.py` `" + d("corpus_identity/test_build_corpus_identity_v27.py"), r)
        self.assertNotIn("`test_build_corpus_identity_v29.py` `" + d("corpus_identity/test_build_corpus_identity_v27.py"), r)
        vd2 = d("drand_only/verify_drand_v2.py"); vd1 = d("drand_only/verify_drand.py")
        self.assertIn("`verify_drand_v2.py` (`" + vd2, r); self.assertNotIn("`verify_drand_v2.py` (the pinned verifier; the V20 `verify_drand.py` is historical) `" + vd1, r)
        self.assertTrue(tf13.startswith('"""Fixture for the STAGED driver v13 (V29 candidate'), tf13[:80])   # codex V28-3: the file must OPEN by naming itself; the inherited v8 header text follows, marked
        self.assertNotIn("authenticate_event → FORGED (see below)", insp); self.assertIn("INCONSISTENT-INPUT", insp.split("| 2 history deleted")[0])
        self.assertIn("same event id and different canonical bytes", q.lower()); self.assertNotIn("FORGED only when the feed carries a push delivering the same commit with different bytes;", q)
        self.assertIn("evaluated only when the retained event is absent", t2); self.assertIn("a later event does not invalidate an authentic earliest event", r)
        self.assertIn("L-INH", r); self.assertIn("default-mode implementation limit", r); self.assertIn("stateless closure enforcement", r)
        self.assertIn("(V28-1)", r); self.assertIn("(V28-2)", r); self.assertIn("(V28-3)", r); self.assertIn("run_configurations_v13", r); self.assertIn("provenance_designs_v9", r)
if __name__ == "__main__": unittest.main()
