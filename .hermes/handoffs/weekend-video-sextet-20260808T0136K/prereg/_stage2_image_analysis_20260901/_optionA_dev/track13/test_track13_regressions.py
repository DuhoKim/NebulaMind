"""TRACK 13 — codex's V32 constructions as REGRESSIONS, one subcase per method (Blanc 05:02 item 3). Targets the SUCCESSORS (provenance_designs_v13,
run_configurations_v17); run FIRST against byte-copies of the V32 modules (import lines renamed only). The table-derived controls (v2, with identity-file pairs,
per-check attribution and independently expected finding sets) are in test_track13_nsd_table.py. Labelled fixtures; monkeypatches labelled."""
import json, os, re, sys, tempfile, unittest, hashlib, subprocess, base64
from pathlib import Path
from unittest import mock
HERE = Path(__file__).resolve().parent; D = HERE.parent
for p in ("beacon_v2", "drand_only", "corpus_identity", "fourier_chirality", "track2", "track12"): sys.path.insert(0, str(D / p))
import provenance_designs_v13 as P
import run_configurations_v17 as rc, test_run_configurations_v17 as TF, history_v2 as H
REF = "refs/heads/main"; REPO = "DuhoKim/NebulaMind"
def canon(e): return hashlib.sha256(json.dumps(e, sort_keys=True, separators=(",", ":")).encode()).hexdigest()
def feed(events, page2=None, page1_fail=False):
    def runner(cmd):
        if cmd[-1].endswith("page=1"): return (1, "", "gh: HTTP 503") if page1_fail else (0, json.dumps(events), "")
        if page2 is not None and cmd[-1].endswith("page=2"): return page2(cmd)
        return (0, json.dumps([]), "")
    return runner
FETCH_FAIL = lambda: mock.patch.object(rc, "verify_witness", side_effect=rc.DataIntegrityFail("WITNESS-FETCH-FAILED fixture transport unavailable"))
class H13:
    def __init__(self, t): self.t = t; rows = t.rows(6); self.ids = [r[0] for r in rows]; self.hold = [str(500000 + i) for i in range(60)]
    def pev(self, commit, n, wk): return {"type": "PushEvent", "id": f"h{n}", "created_at": f"2026-09-06T09:{50 + n:02d}:00Z", "repo": {"name": REPO}, "payload": {"ref": REF, "before": TF.git(wk, "rev-parse", commit + "^"), "head": commit, "commits": [{"sha": commit}]}}
    def fresh(self):
        tmp = Path(tempfile.mkdtemp()); TP = TF.TPJ(tmp); rc.ADOPTION_FILE = Path(self.t.TP.adoption_file); wk = Path(TP.seal_journal).parent; TF.git(TP.witness_remote_url, "config", "receive.denyNonFastforwards", "true")
        of = wk / "HISTORY_OPEN_EVENT.json"; cTP = rc.Protocol(**{**TP.__dict__, "provenance_mode": "composed", "events_repo": REPO, "history_open_event_file": str(of)}); return {"tmp": tmp, "TP": TP, "wk": wk, "of": of, "evs": [], "cTP": cTP}
    def build(self, rebuild_after=False, mutate_ev=None, mutate_I=None, nonce_ok=True, **kw):
        env = self.fresh(); wk, of, evs = env["wk"], env["of"], env["evs"]
        def publish(I, ctx):
            ev = I["approval_witness"]["push_event"]; ev["repo"] = {"name": REPO}
            log = ctx["log"]; lines = [l for l in (log.read_bytes().split(b"\n")) if l]
            for n in range(len(lines)):
                log.write_bytes(b"\n".join(lines[: n + 1]) + b"\n"); TF.git(wk, "add", log.name); TF.git(wk, "commit", "-q", "-m", f"history entry {n}"); c = TF.git(wk, "rev-parse", "HEAD"); TF.git(wk, "push", "-q", "origin", "HEAD:" + REF); evs.append(self.pev(c, n, wk))
                if n == 0 and not of.exists(): of.write_text(json.dumps(evs[0])); TF.git(wk, "add", of.name)
            if rebuild_after:
                ctx["log"].unlink(); H.genesis(ctx["log"], I["approval_witness"]["record_sha256"], I["T_pulse"], I["rule_sha256"], I["beacon_round"])
                e = H.append(ctx["log"], {"stage": "builder-accept", "record_sha256": I["beacon_record_sha256"], "outcome": "ACCEPT-DRAND", "seed_hex": I["seed_hex"], "source": "drand-mainnet-default"}); I["collection_lock"] = {"first_accept": e, "log_sha256": rc.sha_file(ctx["log"]), "entries": 2}
                TF.git(wk, "add", ctx["log"].name); TF.git(wk, "commit", "-q", "-m", "rewrite"); c = TF.git(wk, "rev-parse", "HEAD"); TF.git(wk, "push", "-q", "origin", "HEAD:" + REF); evs.append(self.pev(c, len(evs), wk))
            env["genuine"] = json.loads(json.dumps(ev))
            if mutate_ev: mutate_ev(ev, evs)
            I["approval_witness"]["push_event_sha256"] = canon(ev)
            if mutate_I: mutate_I(I)
        ident = TF.identity(env["tmp"], env["cTP"], self.ids, self.hold, mutate=publish, nonce_ok=nonce_ok, **kw); env["ident"] = ident; env["ev"] = json.loads(ident.read_text())["approval_witness"]["push_event"]; env["live"] = [env["ev"]] + evs; return env

    def build_plant(self, rebuild_after=False, mutate_ev=None, mutate_I=None, nonce_ok=True, _ids5=False, _seed_bodies=False, **kw):
        """build() with two extra plants for the table controls: five tuning ids (lists) and unverifiable seed bodies (seed, rebound coherently)"""
        env = self.fresh(); wk, of, evs = env["wk"], env["of"], env["evs"]; ids = self.ids[:5] if _ids5 else self.ids
        def publish(I, ctx):
            ev = I["approval_witness"]["push_event"]; ev["repo"] = {"name": REPO}
            if _seed_bodies:
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
            if rebuild_after:
                ctx["log"].unlink(); H.genesis(ctx["log"], I["approval_witness"]["record_sha256"], I["T_pulse"], I["rule_sha256"], I["beacon_round"])
                e = H.append(ctx["log"], {"stage": "builder-accept", "record_sha256": I["beacon_record_sha256"], "outcome": "ACCEPT-DRAND", "seed_hex": I["seed_hex"], "source": "drand-mainnet-default"}); I["collection_lock"] = {"first_accept": e, "log_sha256": rc.sha_file(ctx["log"]), "entries": 2}
                TF.git(wk, "add", ctx["log"].name); TF.git(wk, "commit", "-q", "-m", "rewrite"); c = TF.git(wk, "rev-parse", "HEAD"); TF.git(wk, "push", "-q", "origin", "HEAD:" + REF); evs.append(self.pev(c, len(evs), wk))
            env["genuine"] = json.loads(json.dumps(ev)); self._wk = str(wk)
            if mutate_ev: mutate_ev(ev, evs)
            I["approval_witness"]["push_event_sha256"] = canon(ev)
            if mutate_I: mutate_I(I)
        ident = TF.identity(env["tmp"], env["cTP"], ids, self.hold, mutate=publish, nonce_ok=nonce_ok, **kw); env["ident"] = ident; env["ev"] = json.loads(ident.read_text())["approval_witness"]["push_event"]; env["live"] = [env["ev"]] + evs; return env
    def refusal(self, env, runner, ctx=None, TPo=None):
        with (ctx or mock.patch.dict(os.environ, {})):
            with self.t.assertRaises(rc.DataIntegrityFail) as cm: rc.load_identity(env["ident"], rc.Protocol(**{**(TPo or env["cTP"]).__dict__, "events_runner": runner}))
        return str(cm.exception), getattr(rc, "LAST_OUTCOME", None)
def codes(out): return {f["code"] for f in (out or {}).get("findings", [])}
def whys(out): return " | ".join(f.get("why", "") for f in (out or {}).get("findings", []))
class V32_1_Independence(unittest.TestCase):
    @classmethod
    def setUpClass(cls): cls.t = TF.T("test_composed_mode_on_the_production_call_path"); cls.t.setUp(); cls.h = H13(cls.t)
    @classmethod
    def tearDownClass(cls): cls.t.tearDown()
    def test_identity_missing_still_contributes_open_local(self):
        env = self.h.build(); env["of"].write_text(json.dumps({**env["evs"][0], "repo": {"name": "wrong/repo"}})); Path(env["ident"]).unlink()
        msg, out = self.h.refusal(env, feed(env["live"])); self.assertTrue(msg.startswith("IDENTITY-MISSING") or "OPEN-EVENT-INCONSISTENT-INPUT" in msg, msg); self.assertIn("HISTORY-CONTINUATION: OPEN-EVENT-INCONSISTENT-INPUT", codes(out), whys(out))
    def test_identity_missing_still_contributes_open_same_id(self):
        env = self.h.build(); Path(env["ident"]).unlink(); live = [env["ev"], {**env["evs"][0], "payload": {**env["evs"][0]["payload"], "before": "0" * 40}}] + env["evs"][1:]
        msg, out = self.h.refusal(env, feed(live)); self.assertIn("HISTORY-CONTINUATION: OPEN-EVENT-FORGED", codes(out), whys(out))
    def test_identity_missing_still_contributes_rewrite(self):
        env = self.h.build(rebuild_after=True); Path(env["ident"]).unlink(); msg, out = self.h.refusal(env, feed(env["live"])); self.assertTrue(any("NOT-AN-EXTENSION" in f.get("why", "") for f in out["findings"]), whys(out))
    def test_root_discovery_does_not_depend_on_identity(self):
        env = self.h.build(); Path(env["ident"]).unlink(); msg, out = self.h.refusal(env, feed(env["live"])); self.assertNotIn("no local repository root", json.dumps(out.get("blocked", {})) + json.dumps(out.get("stages", {})))
    def test_malformed_approval_commit_does_not_gate_open_same_id(self):
        env = self.h.build(mutate_I=lambda I: I["approval_witness"].update({"commit": "not-a-sha"})); live = [env["ev"], {**env["evs"][0], "payload": {**env["evs"][0]["payload"], "before": "0" * 40}}] + env["evs"][1:]
        with mock.patch.object(P, "remote_head", lambda url, ref: None): msg, out = self.h.refusal(env, feed(live))
        self.assertIn("HISTORY-CONTINUATION: OPEN-EVENT-FORGED", codes(out), whys(out))
    def test_approval_repo_list_does_not_hide_open_local(self):
        env = self.h.build(mutate_ev=lambda ev, evs: ev.update({"repo": ["DuhoKim/NebulaMind"]})); env["of"].write_text(json.dumps({**env["evs"][0], "repo": {"name": "wrong/repo"}}))
        with mock.patch.object(P, "remote_head", lambda url, ref: None): msg, out = self.h.refusal(env, feed(env["live"]))
        self.assertIn("HISTORY-CONTINUATION: OPEN-EVENT-INCONSISTENT-INPUT", codes(out), whys(out))
    def test_fetch_failure_does_not_hide_nonce_unauthenticated(self):
        env = self.h.build(nonce_ok=False); msg, out = self.h.refusal(env, feed(env["live"]), FETCH_FAIL()); self.assertIn("NONCE-UNAUTHENTICATED", codes(out), whys(out))
    def test_first_local_integrity_failure_does_not_hide_the_next(self):
        env = self.h.build(mutate_I=lambda I: I.update({"schema_version": "WRONG", "pool_sha256": "q" * 64})); msg, out = self.h.refusal(env, feed(env["live"]), FETCH_FAIL()); self.assertIn("IDENTITY-SCHEMA", codes(out)); self.assertIn("IDENTITY-POOL-DIGEST", codes(out), whys(out))
    def test_helper_import_failure_still_contributes_open_local(self):
        env = self.h.build(); env["of"].write_text(json.dumps({**env["evs"][0], "repo": {"name": "wrong/repo"}}))
        with mock.patch.object(rc, "_P", side_effect=ImportError("fixture: provenance helpers unavailable")):
            with self.assertRaises(rc.DataIntegrityFail) as cm: rc.load_identity(env["ident"], rc.Protocol(**{**env["cTP"].__dict__, "events_runner": feed(env["live"])}))
        out = rc.LAST_OUTCOME; self.assertIsNotNone(out); self.assertIn("HISTORY-CONTINUATION: OPEN-EVENT-INCONSISTENT-INPUT", codes(out), str(cm.exception))
    def test_degraded_seed_bytes_are_checked_against_the_witness_digest(self):
        """codex's construction: the working-tree approval record CHANGED and the coherently sealed witness digest set to the CHANGED bytes; only the freeze fetch fails —
        S4 must not take the committed blob (whose digest no longer matches the witness) unchecked; the source used must match the witness digest"""
        env = self.h.build(mutate_I=lambda I: None)
        wk = env["wk"]; aw = json.loads(Path(env["ident"]).read_text())["approval_witness"]; rp = wk / aw["record_path"]; changed = rp.read_bytes() + b"\n# changed\n"
        env2 = self.h.build(mutate_I=lambda I: I["approval_witness"].update({"record_sha256": hashlib.sha256(changed).hexdigest()}))
        aw2 = json.loads(Path(env2["ident"]).read_text())["approval_witness"]; (env2["wk"] / aw2["record_path"]).write_bytes(changed)
        msg, out = self.h.refusal(env2, feed(env2["live"]), FETCH_FAIL())
        self.assertNotEqual(out.get("approval_bytes_source"), "committed-blob", f"the committed blob does not match the witness digest and must not be used: {out.get('approval_bytes_source')}")
        self.assertIn(out.get("approval_bytes_source"), ("working-tree", None), out.get("approval_bytes_source"))
class V32_2_Partial(unittest.TestCase):
    @classmethod
    def setUpClass(cls): cls.t = TF.T("test_composed_mode_on_the_production_call_path"); cls.t.setUp(); cls.h = H13(cls.t)
    @classmethod
    def tearDownClass(cls): cls.t.tearDown()
    def test_absence_from_a_partial_prefix_is_not_forgery(self):
        env = self.h.build(); ev = env["ev"]; later = {"type": "PushEvent", "id": "later", "created_at": "2026-09-06T09:58:00Z", "repo": {"name": REPO}, "payload": {"ref": REF, "before": TF.git(env["wk"], "rev-parse", ev["payload"]["head"] + "^"), "head": env["evs"][-1]["payload"]["head"]}}
        filler = [{"type": "IssuesEvent", "id": f"f{i}", "created_at": "2026-09-06T09:40:00Z", "repo": {"name": REPO}, "payload": {}} for i in range(100 - 1 - len(env["evs"]))]
        page1 = [later] + env["evs"] + filler; self.assertEqual(len(page1), 100)
        msg, out = self.h.refusal(env, feed(page1, page2=lambda cmd: (1, "", "gh: HTTP 503"))); self.assertFalse(msg.startswith("EVENT-FORGED"), msg); self.assertTrue(msg.startswith("RETRY-EVENTS-UNAVAILABLE"), msg)
        rc.load_identity(env["ident"], rc.Protocol(**{**env["cTP"].__dict__, "events_runner": feed(page1, page2=lambda cmd: (0, json.dumps([ev]), ""))}))   # the completed snapshot supplies the retained event → ACCEPT (rule iii)
class V32_3_Durable(unittest.TestCase):
    @classmethod
    def setUpClass(cls): cls.t = TF.T("test_composed_mode_on_the_production_call_path"); cls.t.setUp(); cls.h = H13(cls.t)
    @classmethod
    def tearDownClass(cls): cls.t.tearDown()
    def test_remote_event_with_null_commit_does_not_erase_the_rewrite_finding(self):
        env = self.h.build(rebuild_after=True); bad = {"type": "PushEvent", "id": "bad", "created_at": "2026-09-06T09:45:00Z", "repo": {"name": REPO}, "payload": {"ref": REF, "before": "1" * 40, "head": "2" * 40, "commits": [None]}}
        msg, out = self.h.refusal(env, feed([env["ev"], bad] + env["evs"])); self.assertTrue(any("NOT-AN-EXTENSION" in f.get("why", "") for f in out["findings"]), whys(out)); self.assertFalse(msg.startswith("RETRY-"), msg)
    def test_missing_working_tree_history_does_not_erase_remote_findings(self):
        env = self.h.build(rebuild_after=True); Path(env["cTP"].collection_log).unlink(); msg, out = self.h.refusal(env, feed(env["live"])); self.assertTrue(any("NOT-AN-EXTENSION" in f.get("why", "") for f in out["findings"] if f["stage"].startswith("S5")), whys(out))
    def test_standalone_contributes_malformed_remote_evidence(self):
        env = self.h.build(); bad = {"type": "PushEvent", "id": "bad", "created_at": "2026-09-06T09:45:00Z", "repo": {"name": REPO}, "payload": "scalar"}
        ok, why, info = P.validate_continuation_v13(env["wk"], Path(env["cTP"].collection_log).name, env["cTP"].witness_remote_url, REF, env["evs"][0], feed(env["live"] + [bad]), REPO); self.assertFalse(ok); self.assertIn("MALFORMED-REMOTE-EVIDENCE", why + json.dumps(info.get("findings", [])))
class V32_5_Accounting(unittest.TestCase):
    def test_dynamic_tuning_receipt_codes_are_classified(self):
        for c in ("TUNING-RECEIPT-0-CONFIG", "TUNING-RECEIPT-3-COUNTS", "TUNING-RECEIPT-1-JOURNAL-MISMATCH", "TUNING-RECEIPT-2-DERIVED"): got = P.classify_refusal(f"{c}: x"); self.assertFalse(got[3], c); self.assertEqual(got[0], "LOCAL-TERMINAL")
    def test_history_success_wording_claims_blob_equality_not_head(self):
        src = (D / "track2" / "provenance_designs_v13.py").read_text(encoding="utf-8"); i = src.index("def history_findings_v13"); body = src[i:i + 12000]; self.assertNotIn("working tree equals the live remote head", body); self.assertIn("history blob", body)
if __name__ == "__main__": unittest.main()
