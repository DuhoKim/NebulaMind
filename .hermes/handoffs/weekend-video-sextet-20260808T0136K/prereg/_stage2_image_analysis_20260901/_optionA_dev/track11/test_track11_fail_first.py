"""TRACK 11 FAIL-FIRST tests — codex's V30 findings: V30-1 FATAL (a JSON null open-event file disables the composed history boundary), V30-2 (retries before the
local sweep, class-0 checks after the resolver), V30-3 (helpers suppress higher findings; evidence not shared across retrievals; unavailability before expiry),
V30-4 (text). Targets the SUCCESSORS (provenance_designs_v11, run_configurations_v15); run FIRST against byte-copies of the V30 modules — run 1 REPRODUCES THE
FATAL IN EXECUTED OUTPUT before any repair (the V20 rule). Labelled fixture runners; local bare repositories."""
import json, os, sys, base64, tempfile, unittest, hashlib, subprocess
from pathlib import Path
HERE = Path(__file__).resolve().parent; D = HERE.parent
for p in ("beacon_v2", "drand_only", "corpus_identity", "fourier_chirality", "track2"): sys.path.insert(0, str(D / p))
import provenance_designs_v11 as P
REF = "refs/heads/main"; REPO = "DuhoKim/NebulaMind"
def feed(events, counter=None):
    def runner(cmd):
        if counter is not None: counter.append(cmd[-1])
        return (0, json.dumps(events if cmd[-1].endswith("page=1") else []), "")
    return runner
def canon(e): return hashlib.sha256(json.dumps(e, sort_keys=True, separators=(",", ":")).encode()).hexdigest()
class V30_CompletePath(unittest.TestCase):
    def setUp(self):
        sys.path.insert(0, str(D / "fourier_chirality")); import run_configurations_v15 as rc, test_run_configurations_v15 as TF, history_v2 as H
        self.rc, self.TF, self.H = rc, TF, H; self.t = TF.T("test_composed_mode_on_the_production_call_path"); self.t.setUp()
        rows = self.t.rows(6); self.ids = [r[0] for r in rows]; self.hold = [str(500000 + i) for i in range(60)]
    def tearDown(self): self.t.tearDown()
    def pev(self, commit, n, wk): return {"type": "PushEvent", "id": f"h{n}", "created_at": f"2026-09-06T09:{50 + n:02d}:00Z", "repo": {"name": REPO}, "payload": {"ref": REF, "before": self.TF.git(wk, "rev-parse", commit + "^"), "head": commit, "commits": [{"sha": commit}]}}
    def fresh(self):
        import tempfile as tf; rc, TF = self.rc, self.TF
        tmp = Path(tf.mkdtemp()); TP = TF.TPJ(tmp); rc.ADOPTION_FILE = Path(self.t.TP.adoption_file); wk = Path(TP.seal_journal).parent; TF.git(TP.witness_remote_url, "config", "receive.denyNonFastforwards", "true")
        of = wk / "HISTORY_OPEN_EVENT.json"; evs = []; cTP = rc.Protocol(**{**TP.__dict__, "provenance_mode": "composed", "events_repo": REPO, "history_open_event_file": str(of)}); return tmp, TP, wk, of, evs, cTP
    def publish(self, I, ctx, wk, of, evs, keep=None, mutate=None, rebuild_after=False):
        TF, H, rc = self.TF, self.H, self.rc
        ev = I["approval_witness"]["push_event"]; ev["repo"] = {"name": REPO}
        def push_all():
            log = ctx["log"]; lines = [l for l in (log.read_bytes().split(b"\n")) if l]
            for n in range(len(lines)):
                log.write_bytes(b"\n".join(lines[: n + 1]) + b"\n"); TF.git(wk, "add", log.name); TF.git(wk, "commit", "-q", "-m", f"history entry {n}"); c = TF.git(wk, "rev-parse", "HEAD"); TF.git(wk, "push", "-q", "origin", "HEAD:" + REF); evs.append(self.pev(c, n, wk))
                if n == 0 and not of.exists(): of.write_text(json.dumps(evs[0])); TF.git(wk, "add", of.name)
        push_all()
        if rebuild_after:                                                                          # codex's V30 construction: publish honestly, then a fast-forward history REWRITE, then restoration of the current bytes
            ctx["log"].unlink(); H.genesis(ctx["log"], I["approval_witness"]["record_sha256"], I["T_pulse"], I["rule_sha256"], I["beacon_round"])
            e = H.append(ctx["log"], {"stage": "builder-accept", "record_sha256": I["beacon_record_sha256"], "outcome": "ACCEPT-DRAND", "seed_hex": I["seed_hex"], "source": "drand-mainnet-default"})
            I["collection_lock"] = {"first_accept": e, "log_sha256": rc.sha_file(ctx["log"]), "entries": 2}
            TF.git(wk, "add", ctx["log"].name); TF.git(wk, "commit", "-q", "-m", "rewrite"); c = TF.git(wk, "rev-parse", "HEAD"); TF.git(wk, "push", "-q", "origin", "HEAD:" + REF); evs.append(self.pev(c, len(evs), wk))
        if keep is not None: keep.append(json.loads(json.dumps(ev)))
        if mutate: mutate(ev, evs)
        I["approval_witness"]["push_event_sha256"] = canon(ev)
    def test_V30_1_null_open_event_file_never_accepts(self):
        rc, TF = self.rc, self.TF
        tmp, TP, wk, of, evs, cTP = self.fresh(); ident = TF.identity(tmp, cTP, self.ids, self.hold, mutate=lambda I, ctx: self.publish(I, ctx, wk, of, evs)); ev = json.loads(ident.read_text())["approval_witness"]["push_event"]
        rc.load_identity(ident, rc.Protocol(**{**cTP.__dict__, "events_runner": feed([ev] + evs)}))                   # genuine: loads
        of.write_text("null")                                                                                          # codex V30-1: a JSON null parses without error
        with self.assertRaises(rc.DataIntegrityFail) as cm: rc.load_identity(ident, rc.Protocol(**{**cTP.__dict__, "events_runner": feed([ev] + evs)}))
        self.assertTrue(str(cm.exception).startswith("HISTORY-OPEN-EVENT-INVALID"), str(cm.exception))
        for bad in ("[]", '"x"', "7", '{"type": "PullRequestEvent"}'):
            of.write_text(bad)
            with self.assertRaises(rc.DataIntegrityFail) as cm: rc.load_identity(ident, rc.Protocol(**{**cTP.__dict__, "events_runner": feed([ev] + evs)}))
            self.assertTrue(str(cm.exception).startswith("HISTORY-OPEN-EVENT-INVALID") or "OPEN-EVENT-INCONSISTENT-INPUT" in str(cm.exception), str(cm.exception))
        # the rewritten history that the genuine open event refuses must stay refused with a null open file
        tmp, TP, wk, of, evs, cTP = self.fresh(); ident = TF.identity(tmp, cTP, self.ids, self.hold, mutate=lambda I, ctx: self.publish(I, ctx, wk, of, evs, rebuild_after=True)); ev = json.loads(ident.read_text())["approval_witness"]["push_event"]
        with self.assertRaises(rc.DataIntegrityFail) as cm: rc.load_identity(ident, rc.Protocol(**{**cTP.__dict__, "events_runner": feed([ev] + evs)}))
        self.assertIn("NOT-AN-EXTENSION", str(cm.exception))
        of.write_text("null")
        with self.assertRaises(rc.DataIntegrityFail) as cm: rc.load_identity(ident, rc.Protocol(**{**cTP.__dict__, "events_runner": feed([ev] + evs)}))
    def test_V30_2_local_findings_beat_early_and_late_retries(self):
        rc, TF = self.rc, self.TF
        # (a) wrong approval repository + the freeze-witness fetch failing → EVENT-INCONSISTENT, not WITNESS-FETCH-FAILED
        tmp, TP, wk, of, evs, cTP = self.fresh(); ident = TF.identity(tmp, cTP, self.ids, self.hold, mutate=lambda I, ctx: self.publish(I, ctx, wk, of, evs, mutate=lambda ev, evs: ev.update({"repo": {"name": "wrong/repo"}}))); ev = json.loads(ident.read_text())["approval_witness"]["push_event"]
        dead = str(tmp / "no-such-remote.git"); TF.git(wk, "remote", "set-url", "origin", dead); TPd = rc.Protocol(**{**cTP.__dict__, "witness_remote_url": dead, "events_runner": feed([ev] + evs)})
        with self.assertRaises(rc.DataIntegrityFail) as cm: rc.load_identity(ident, TPd)
        self.assertTrue(str(cm.exception).startswith("EVENT-INCONSISTENT"), str(cm.exception))
        # (b) one tuning id missing (a class-0 list defect) + the approval feed at HTTP 503 → IDENTITY-tuning_objids-SIZE-OR-TYPE, not a retry
        tmp, TP, wk, of, evs, cTP = self.fresh(); ident = TF.identity(tmp, cTP, self.ids[:5], self.hold, mutate=lambda I, ctx: self.publish(I, ctx, wk, of, evs))
        with self.assertRaises(rc.DataIntegrityFail) as cm: rc.load_identity(ident, rc.Protocol(**{**cTP.__dict__, "events_runner": (lambda cmd: (1, "", "gh: HTTP 503: Service Unavailable"))}))
        self.assertIn("IDENTITY-tuning_objids-SIZE-OR-TYPE", str(cm.exception))
    def test_V30_3_higher_findings_are_not_suppressed_and_one_snapshot_serves_all(self):
        rc, TF = self.rc, self.TF
        # (a) a published history REWRITE with an EMPTY events feed → HISTORY-NOT-AN-EXTENSION (derived from fetched objects) beats the retry for the empty open-event retrieval
        tmp, TP, wk, of, evs, cTP = self.fresh(); ident = TF.identity(tmp, cTP, self.ids, self.hold, mutate=lambda I, ctx: self.publish(I, ctx, wk, of, evs, rebuild_after=True)); ev = json.loads(ident.read_text())["approval_witness"]["push_event"]
        with self.assertRaises(rc.DataIntegrityFail) as cm: rc.load_identity(ident, rc.Protocol(**{**cTP.__dict__, "events_runner": feed([])}))
        self.assertIn("NOT-AN-EXTENSION", str(cm.exception)); self.assertFalse(str(cm.exception).startswith("RETRY-"), str(cm.exception))
        # (b) undetermined approval delivery + a feed that no longer reaches the event (newer only) + the remote down → EVENT-EXPIRED-NO-RECEIPT-PATH outranks the retry
        tmp, TP, wk, of, evs, cTP = self.fresh(); ident = TF.identity(tmp, cTP, self.ids, self.hold, mutate=lambda I, ctx: self.publish(I, ctx, wk, of, evs, mutate=lambda ev, evs: ev["payload"].update({"before": "e" * 40, "head": evs[-1]["payload"]["head"], "commits": []})))
        newer = {"type": "PushEvent", "id": "z", "created_at": "2027-01-01T00:00:00Z", "repo": {"name": REPO}, "payload": {"ref": REF, "before": "1" * 40, "head": "2" * 40, "commits": [{"sha": "2" * 40}]}}
        real = P.remote_head
        try:
            P.remote_head = lambda url, ref: None
            with self.assertRaises(rc.DataIntegrityFail) as cm: rc.load_identity(ident, rc.Protocol(**{**cTP.__dict__, "events_runner": feed([newer])}))
        finally: P.remote_head = real
        self.assertTrue(str(cm.exception).startswith("EVENT-EXPIRED-NO-RECEIPT-PATH"), str(cm.exception))
        # (c) ONE evidence snapshot per invocation: the events runner is asked once (pages of one retrieval), not once per stage
        tmp, TP, wk, of, evs, cTP = self.fresh(); ident = TF.identity(tmp, cTP, self.ids, self.hold, mutate=lambda I, ctx: self.publish(I, ctx, wk, of, evs)); ev = json.loads(ident.read_text())["approval_witness"]["push_event"]
        calls = []; rc.load_identity(ident, rc.Protocol(**{**cTP.__dict__, "events_runner": feed([ev] + evs, counter=calls)}))
        pages1 = [c for c in calls if c.endswith("page=1")]; self.assertEqual(len(pages1), 1, f"retrievals: {calls}")
class V30_Classification(unittest.TestCase):
    def test_every_named_refusal_has_a_class_and_ordering_is_expiry_before_unavailability(self):
        inv = {"LOCAL-TERMINAL": ["ADOPTION-MISSING", "ADOPTION-MALFORMED", "WITNESS-MISSING", "WITNESS-COMMIT-MALFORMED", "WITNESS-NOT-A-GIT-REPO", "WITNESS-COMMIT-LACKS-JOURNAL", "WITNESS-COMMIT-LACKS-RECORD", "WITNESS-REMOTE-URL", "IDENTITY-MISSING", "IDENTITY-NOT-SEALED", "IDENTITY-NOT-IN-WITNESS-COMMIT", "IDENTITY-SCHEMA", "IDENTITY-FIELD-MISSING", "IDENTITY-POOL-DIGEST", "IDENTITY-EXCLUSION-DIGEST", "PROTOCOL-NO-REDERIVER", "ADOPTION-MISMATCH", "IDENTITY-RULE-DIGEST", "IDENTITY-NOT-BEACON-SEEDED", "IDENTITY-BEACON-NOT-ACCEPTED", "IDENTITY-SOURCE", "IDENTITY-WITNESS-MISSING", "IDENTITY-WITNESS-COMMIT", "APPROVAL-RECORD-MISSING", "APPROVAL-RECORD-DIGEST", "APPROVAL-RECORD-NOT-AT-COMMIT", "APPROVAL-RECORD-HISTORY", "APPROVAL-NOT-FIRST", "APPROVAL-RULE-LINE", "APPROVAL-T-SIGN-LINE", "APPROVAL-NONCE-LINE", "IDENTITY-T-SIGN", "IDENTITY-T-PULSE", "IDENTITY-ROUND", "IDENTITY-T-SIGN-PREDATES-AMENDMENT", "IDENTITY-T-PULSE-EXCLUDED", "IDENTITY-WITNESS-TIME", "IDENTITY-WITNESS-LATE", "EVENT-DIGEST", "EVENT-INCONSISTENT", "EVENT-PROVENANCE", "IDENTITY-WITNESS-NONCE", "NONCE-UNAUTHENTICATED", "ADOPTION-NOT-AT-APPROVAL-COMMIT", "ADOPTION-DIGEST", "COLLECTION-LOG-DIGEST", "COLLECTION-LOG-NOT-IN-WITNESS-COMMIT", "HISTORY-INVALID", "HISTORY-GENESIS", "HISTORY-COUNT", "COLLECTION-LOG-EMPTY", "IDENTITY-LOCK-MISMATCH", "COLLECTION-CLOSED", "COLLECTION-LOG-CONFLICT", "BEACON-RECORD-DIGEST", "BEACON-RECORD-NOT-IN-WITNESS-COMMIT", "BEACON-RECORD-UNREADABLE", "BEACON-RECORD-BINDING", "BEACON-RECORD-STATEMENT", "BEACON-RECORD-RELAYS", "HISTORY-OPEN-EVENT-MISSING", "HISTORY-OPEN-EVENT-INVALID", "IDENTITY-tuning_objids-SIZE-OR-TYPE", "IDENTITY-OVERLAP", "MALFORMED-RETAINED-INPUT"],
               "RETRY-UNAVAILABLE": ["WITNESS-FETCH-FAILED", "VERIFIER-UNAVAILABLE", "REDERIVE-RETRY", "RETRY-EVENTS-UNAVAILABLE", "RETRY-REMOTE-UNAVAILABLE", "IO-UNAVAILABLE"],
               "DERIVED-TERMINAL": ["WITNESS-NOT-PUSHED", "APPROVAL-COMMIT-NOT-PUSHED", "IDENTITY-SEED-NOT-REDERIVED", "REDERIVE-CLOSED", "HISTORY-NOT-AN-EXTENSION", "HISTORY-DELETED-AT", "HISTORY-BATCH-COMMIT", "HISTORY-PUBLICATION-BATCH", "HISTORY-PUBLICATION-ORDER", "HISTORY-NO-COMMITS", "OPEN-NOT-GENESIS-ONLY", "PENDING-PUSH", "HISTORY-DIVERGED"],
               "FORGED": ["EVENT-FORGED", "OPEN-EVENT-FORGED"], "NOT-EARLIEST": ["EVENT-NOT-EARLIEST", "OPEN-EVENT-NOT-EARLIEST"], "EXPIRED": ["EVENT-EXPIRED-NO-RECEIPT-PATH", "EVENT-EXPIRED-RECEIPT-REFUSED", "EVIDENCE-EXPIRED"], "RETRY-INCOMPLETE": ["EVIDENCE-INCOMPLETE", "RETRY-EVENTS-INCOMPLETE"]}
        for cls, codes in inv.items():
            for c in codes:
                got = P.classify_refusal(f"{c}: some detail"); self.assertEqual(got[0], cls, f"{c} → {got}"); self.assertFalse(got[3], f"{c} unclassified")
        self.assertTrue(P.classify_refusal("SOMETHING-NEW: x")[3])                                             # an unknown code is flagged, never silently placed
        self.assertEqual(P.classify_exception(json.JSONDecodeError("x", "y", 0))[0], "LOCAL-TERMINAL"); self.assertEqual(P.classify_exception(OSError("boom"))[0], "RETRY-UNAVAILABLE")
        tmp = Path(tempfile.mkdtemp()); subprocess.run(["git", "init", "-q", str(tmp)], check=True)
        und = {"type": "PushEvent", "id": "u", "created_at": "2026-01-01T00:00:00Z", "repo": {"name": REPO}, "payload": {"ref": REF, "before": "e" * 40, "head": "f" * 40}}
        newer = {"type": "PushEvent", "id": "z", "created_at": "2027-01-01T00:00:00Z", "repo": {"name": REPO}, "payload": {"ref": REF, "before": "1" * 40, "head": "2" * 40, "commits": [{"sha": "2" * 40}]}}
        o, why = P.authenticate_event(und, [newer], REPO, REF, "a" * 40, feed_reaches_back_to=newer["created_at"], root=tmp); self.assertEqual(o, "EXPIRED", why)   # V30-3: expiry before unavailability
class V30_4_Text(unittest.TestCase):
    def test_offline_wording_and_policies(self):
        r = Path(os.environ["RULE_TEXT"]).read_text(encoding="utf-8")
        sec = r[r.index("3c. V3"):]; sec = sec[:sec.index("\n")]; cur = r[:r.index(" was V")] + sec                        # the CURRENT text: the newest version paragraph and §3c (historical paragraphs are kept verbatim)
        self.assertNotIn("offline mode, which has no retry vocabulary", cur); self.assertNotIn("offline has no retry vocabulary", cur); self.assertIn("REDERIVE-RETRY", cur); self.assertIn("WITNESS-FETCH-FAILED", cur)
        for k in ("(V30-1)", "(V30-2)", "(V30-3)", "(V30-4)", "run_configurations_v15", "provenance_designs_v11", "HISTORY-OPEN-EVENT-INVALID", "No required stage can be skipped into acceptance", "one evidence snapshot", "classify_refusal", "PENDING-PUSH", "coherent_attacks_v31.py"): self.assertIn(k, r, k)
if __name__ == "__main__": unittest.main()
