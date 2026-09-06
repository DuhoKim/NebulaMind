"""TRACK 10 FAIL-FIRST tests — codex's V29 findings: V29-1 (seed re-derivation retry precedes approval precedence), V29-2 (remote-head / approval-feed retries precede
the local check of the retained open event), V29-4 (equal-time edge of rule iii), V29-3 (text). Combined conditions on the COMPLETE composed path, as codex built
them. Targets the SUCCESSORS (provenance_designs_v10, run_configurations_v14); run FIRST against byte-copies of the V29 modules. Labelled fixture runners; local bare repositories."""
import json, os, sys, base64, tempfile, unittest, hashlib, subprocess
from pathlib import Path
HERE = Path(__file__).resolve().parent; D = HERE.parent
for p in ("beacon_v2", "drand_only", "corpus_identity", "fourier_chirality", "track2"): sys.path.insert(0, str(D / p))
import provenance_designs_v10 as P
def git(cwd, *a):
    r = subprocess.run(["git", *a], cwd=cwd, capture_output=True, text=True); assert r.returncode == 0, r.stderr; return r.stdout.strip()
REF = "refs/heads/main"; REPO = "DuhoKim/NebulaMind"
def feed(events): return lambda cmd: (0, json.dumps(events if cmd[-1].endswith("page=1") else []), "")
def canon(e): return hashlib.sha256(json.dumps(e, sort_keys=True, separators=(",", ":")).encode()).hexdigest()
class V29_1_2_CompletePaths(unittest.TestCase):
    def test_no_stage_retries_before_the_local_sweep_and_same_id_authentication(self):
        sys.path.insert(0, str(D / "fourier_chirality")); import run_configurations_v14 as rc, test_run_configurations_v14 as TF, history_v2 as H, tempfile as tf
        t = TF.T("test_composed_mode_on_the_production_call_path"); t.setUp()
        try:
            rows = t.rows(6); ids = [r[0] for r in rows]; hold = [str(500000 + i) for i in range(60)]
            def pev(commit, n, wk): return {"type": "PushEvent", "id": f"h{n}", "created_at": f"2026-09-06T09:{50 + n:02d}:00Z", "repo": {"name": REPO}, "payload": {"ref": REF, "before": TF.git(wk, "rev-parse", commit + "^"), "head": commit, "commits": [{"sha": commit}]}}
            def fresh():
                tmp = Path(tf.mkdtemp()); TP = TF.TPJ(tmp); rc.ADOPTION_FILE = Path(t.TP.adoption_file); wk = Path(TP.seal_journal).parent; TF.git(TP.witness_remote_url, "config", "receive.denyNonFastforwards", "true")
                of = wk / "HISTORY_OPEN_EVENT.json"; evs = []; cTP = rc.Protocol(**{**TP.__dict__, "provenance_mode": "composed", "events_repo": REPO, "history_open_event_file": str(of)}); return tmp, TP, wk, of, evs, cTP
            def publish(I, ctx, wk, of, evs, keep=None, mutate=None, unverifiable_seed_bodies=False, TP=None):
                if unverifiable_seed_bodies:                                                   # codex V29-1: the retained seed-signature bodies do not BLS-verify; everything that binds the record is recomputed coherently
                    rp = Path(TP.beacon_record_path); rec = json.loads(rp.read_text())
                    for u, r in rec["relays"].items():
                        if isinstance(r, dict) and "body_b64" in r: body = json.loads(base64.b64decode(r["body_b64"])); body["signature"] = "00"; r["body_b64"] = base64.b64encode(json.dumps(body).encode()).decode()
                    rp.write_text(json.dumps(rec, indent=1, sort_keys=True)); I["beacon_record_sha256"] = rc.sha_file(rp)
                    ctx["log"].unlink(); H.genesis(ctx["log"], I["approval_witness"]["record_sha256"], I["T_pulse"], I["rule_sha256"], I["beacon_round"])
                    e = H.append(ctx["log"], {"stage": "builder-accept", "record_sha256": I["beacon_record_sha256"], "outcome": "ACCEPT-DRAND", "seed_hex": I["seed_hex"], "source": "drand-mainnet-default"})
                    I["collection_lock"] = {"first_accept": e, "log_sha256": rc.sha_file(ctx["log"]), "entries": 2}
                ev = I["approval_witness"]["push_event"]; ev["repo"] = {"name": REPO}
                log = ctx["log"]; lines = [l for l in (log.read_bytes().split(b"\n")) if l]
                for n in range(len(lines)):
                    log.write_bytes(b"\n".join(lines[: n + 1]) + b"\n"); TF.git(wk, "add", log.name); TF.git(wk, "commit", "-q", "-m", f"history entry {n}"); c = TF.git(wk, "rev-parse", "HEAD"); TF.git(wk, "push", "-q", "origin", "HEAD:" + REF); evs.append(pev(c, n, wk))
                    if n == 0: of.write_text(json.dumps(evs[0])); TF.git(wk, "add", of.name)
                if keep is not None: keep.append(json.loads(json.dumps(ev)))
                if mutate: mutate(ev, evs)
                I["approval_witness"]["push_event_sha256"] = canon(ev)
            und = lambda ev, evs: ev["payload"].update({"before": "e" * 40, "head": evs[-1]["payload"]["head"], "commits": []})
            und_wrong = lambda ev, evs: (und(ev, evs), ev.update({"repo": {"name": "wrong/repo"}}))
            # ---- V29-1: unverifiable seed bodies (the re-deriver would say RETRY) + approval undetermined + wrong repository → EVENT-INCONSISTENT, not REDERIVE-RETRY
            tmp, TP, wk, of, evs, cTP = fresh()
            ident = TF.identity(tmp, cTP, ids, hold, mutate=lambda I, ctx: publish(I, ctx, wk, of, evs, mutate=und_wrong, unverifiable_seed_bodies=True, TP=TP)); ev = json.loads(ident.read_text())["approval_witness"]["push_event"]
            with self.assertRaises(rc.DataIntegrityFail) as cm: rc.load_identity(ident, rc.Protocol(**{**cTP.__dict__, "events_runner": feed([ev] + evs)}))
            self.assertTrue(str(cm.exception).startswith("EVENT-INCONSISTENT"), str(cm.exception))
            # ---- V29-1: unverifiable seed bodies + approval undetermined + the GENUINE conflicting same-id event in the feed → EVENT-FORGED
            tmp, TP, wk, of, evs, cTP = fresh(); genuine = []
            ident = TF.identity(tmp, cTP, ids, hold, mutate=lambda I, ctx: publish(I, ctx, wk, of, evs, keep=genuine, mutate=und, unverifiable_seed_bodies=True, TP=TP))
            with self.assertRaises(rc.DataIntegrityFail) as cm: rc.load_identity(ident, rc.Protocol(**{**cTP.__dict__, "events_runner": feed(genuine + evs)}))
            self.assertTrue(str(cm.exception).startswith("EVENT-FORGED"), str(cm.exception))
            # ---- V29-1 control: unverifiable seed bodies + otherwise genuine approval → REDERIVE-RETRY is the legitimate retry once nothing higher is established
            tmp, TP, wk, of, evs, cTP = fresh()
            ident = TF.identity(tmp, cTP, ids, hold, mutate=lambda I, ctx: publish(I, ctx, wk, of, evs, unverifiable_seed_bodies=True, TP=TP)); ev = json.loads(ident.read_text())["approval_witness"]["push_event"]
            with self.assertRaises(rc.DataIntegrityFail) as cm: rc.load_identity(ident, rc.Protocol(**{**cTP.__dict__, "events_runner": feed([ev] + evs)}))
            self.assertTrue(str(cm.exception).startswith("REDERIVE-RETRY"), str(cm.exception))
            # ---- V29-2: a retained open event naming wrong/repo (undetermined delivery) with (i) ls-remote failing, (ii) the approval-stage feed answering HTTP 503 → OPEN-EVENT-INCONSISTENT-INPUT both times, never a retry
            tmp, TP, wk, of, evs, cTP = fresh()
            ident = TF.identity(tmp, cTP, ids, hold, mutate=lambda I, ctx: publish(I, ctx, wk, of, evs)); ev = json.loads(ident.read_text())["approval_witness"]["push_event"]
            wr = {**evs[0], "repo": {"name": "wrong/repo"}, "payload": {**evs[0]["payload"], "before": "e" * 40, "head": evs[1]["payload"]["head"], "commits": []}}; of.write_text(json.dumps(wr))
            real_remote_head = P.remote_head
            try:
                P.remote_head = lambda url, ref: None                                                  # only ls-remote fails; the freeze fetch and the approval feed succeed
                with self.assertRaises(rc.DataIntegrityFail) as cm: rc.load_identity(ident, rc.Protocol(**{**cTP.__dict__, "events_runner": feed([ev] + evs)}))
                self.assertTrue(str(cm.exception).startswith("HISTORY-CONTINUATION: OPEN-EVENT-INCONSISTENT-INPUT"), str(cm.exception))
                # ---- V29-2: open event undetermined + the GENUINE conflicting same-id open event in the feed, ls-remote failing → OPEN-EVENT-FORGED (decided from the one retrieval already made)
                und_open = {**evs[0], "payload": {**evs[0]["payload"], "before": "e" * 40, "head": evs[1]["payload"]["head"], "commits": []}}; of.write_text(json.dumps(und_open))
                with self.assertRaises(rc.DataIntegrityFail) as cm: rc.load_identity(ident, rc.Protocol(**{**cTP.__dict__, "events_runner": feed([ev] + evs)}))
                self.assertTrue(str(cm.exception).startswith("HISTORY-CONTINUATION: OPEN-EVENT-FORGED"), str(cm.exception))
                # ---- control: genuine open event, ls-remote failing → the history stage's retry is legitimate
                of.write_text(json.dumps(evs[0]))
                with self.assertRaises(rc.DataIntegrityFail) as cm: rc.load_identity(ident, rc.Protocol(**{**cTP.__dict__, "events_runner": feed([ev] + evs)}))
                self.assertIn("RETRY-REMOTE-UNAVAILABLE", str(cm.exception))
            finally: P.remote_head = real_remote_head
            of.write_text(json.dumps(wr))
            with self.assertRaises(rc.DataIntegrityFail) as cm: rc.load_identity(ident, rc.Protocol(**{**cTP.__dict__, "events_runner": (lambda cmd: (1, "", "gh: HTTP 503: Service Unavailable"))}))
            self.assertTrue(str(cm.exception).startswith("HISTORY-CONTINUATION: OPEN-EVENT-INCONSISTENT-INPUT"), str(cm.exception))
        finally: t.tearDown()
class V29_4_StrictEarlier(unittest.TestCase):
    def test_equal_timestamps_are_not_earlier_in_either_feed_order(self):
        tmp = Path(tempfile.mkdtemp()); git(tmp, "init", "-q"); git(tmp, "config", "user.email", "t@t"); git(tmp, "config", "user.name", "t")
        (tmp / "a").write_text("a"); git(tmp, "add", "a"); git(tmp, "commit", "-q", "-m", "base"); base = git(tmp, "rev-parse", "HEAD")
        (tmp / "b").write_text("b"); git(tmp, "add", "b"); git(tmp, "commit", "-q", "-m", "approval"); commit = git(tmp, "rev-parse", "HEAD")
        (tmp / "c").write_text("c"); git(tmp, "add", "c"); git(tmp, "commit", "-q", "-m", "later"); later = git(tmp, "rev-parse", "HEAD")
        genuine = {"type": "PushEvent", "id": "g1", "created_at": "2026-09-07T01:00:00Z", "repo": {"name": REPO}, "payload": {"ref": REF, "before": base, "head": commit, "commits": [{"sha": commit}]}}
        other = {"type": "PushEvent", "id": "g2", "created_at": "2026-09-07T01:00:00Z", "repo": {"name": REPO}, "payload": {"ref": REF, "before": base, "head": later}}   # distinct id, EQUAL created_at
        for order in ([genuine, other], [other, genuine]):
            o, why = P.authenticate_event(genuine, order, REPO, REF, commit, root=tmp); self.assertEqual(o, "AUTHENTIC", why)
        earlier = {**other, "created_at": "2026-09-07T00:59:59Z"}
        o, why = P.authenticate_event(genuine, [genuine, earlier], REPO, REF, commit, root=tmp); self.assertEqual(o, "NOT-EARLIEST", why); self.assertIn("strictly earlier", why)
        self.assertIn("feed iteration order is not an unstated tie-break", P.__doc__)
class V29_3_Text(unittest.TestCase):
    def test_labels_and_placeholders(self):
        r = Path(os.environ["RULE_TEXT"]).read_text(encoding="utf-8")
        import re, hashlib as h
        self.assertEqual(re.findall(r"`\\[0-9]`", r), [], "literal backreference tokens where digests belong")
        d = lambda p: h.sha256((D / p).read_bytes()).hexdigest()
        for p in ("track7/test_track7_fail_first.py", "track7/test_track7_text_v27.py", "track8/test_track8_fail_first.py", "track8/test_track8_text_v28.py"): self.assertIn("`" + p + "` `" + d(p) + "`", r, p)
        self.assertIn("driver v14 23 + V15 driver 17 + history_v2 4 + witness v4 3 + builder v30 8 + V15 builder 4 + verdict v30 7", r); self.assertNotIn("driver v12 23", r)
        for k in ("(V29-1)", "(V29-2)", "(V29-3)", "(V29-4)", "run_configurations_v14", "provenance_designs_v10", "Before any retry is returned from load_identity", "feed iteration order is not an unstated tie-break", "coherent_attacks_v30.py"): self.assertIn(k, r, k)
if __name__ == "__main__": unittest.main()

class Resolver(unittest.TestCase):
    """Blanc 03:20 (BLANC_ORDER_PRECEDENCE_IS_ONE_PATTERN): the resolver's own tests — the precedence order stated once, enforced in one place, exhibited PAIRWISE:
    for every pair of classes that can co-occur, both findings are contributed in BOTH orders and the same winner results; retrieval order plays no part."""
    def test_pairwise_same_winner_regardless_of_derivation_order(self):
        cls = list(P.PRECEDENCE); self.assertEqual(cls[0], "LOCAL-TERMINAL"); self.assertEqual(cls[-1], "ACCEPT"); self.assertLess(cls.index("FORGED"), cls.index("RETRY-UNAVAILABLE")); self.assertLess(cls.index("EXPIRED"), cls.index("RETRY-INCOMPLETE")); self.assertLess(cls.index("DERIVED-TERMINAL"), cls.index("RETRY-UNAVAILABLE"))
        pairs = 0
        for i in range(len(cls) - 1):
            for j in range(i + 1, len(cls) - 1):
                a = P.finding(cls[i], f"CODE-{cls[i]}", "why-a", "stage-a", 0); b = P.finding(cls[j], f"CODE-{cls[j]}", "why-b", "stage-b", 1)
                a2 = P.finding(cls[i], f"CODE-{cls[i]}", "why-a", "stage-a", 1); b2 = P.finding(cls[j], f"CODE-{cls[j]}", "why-b", "stage-b", 0)
                self.assertEqual(P.resolve([a, b])["class"], cls[i]); self.assertEqual(P.resolve([b2, a2])["class"], cls[i]); pairs += 1
        self.assertEqual(pairs, (len(cls) - 1) * (len(cls) - 2) // 2)
        same = [P.finding("LOCAL-TERMINAL", "X", "first", "s1", 0), P.finding("LOCAL-TERMINAL", "Y", "second", "s2", 1)]
        self.assertEqual(P.resolve(same)["code"], "X"); self.assertEqual(P.resolve(list(reversed(same)))["code"], "X")   # within one class: the FIXED stage sequence (seq), not list order
        self.assertEqual(P.classify_history("EVIDENCE-UNAVAILABLE: x"), ("RETRY-UNAVAILABLE", "RETRY-HISTORY-CONTINUATION")); self.assertEqual(P.classify_history("RETRY-REMOTE-UNAVAILABLE: x"), ("RETRY-UNAVAILABLE", "HISTORY-CONTINUATION"))
        self.assertEqual(P.classify_history("OPEN-EVENT-FORGED: x")[0], "FORGED"); self.assertEqual(P.classify_history("OPEN-EVENT-INCONSISTENT-INPUT: x")[0], "LOCAL-TERMINAL"); self.assertEqual(P.classify_history("HISTORY-NOT-AN-EXTENSION at x")[0], "DERIVED-TERMINAL"); self.assertEqual(P.classify_history("EVIDENCE-EXPIRED: x")[0], "EXPIRED")
