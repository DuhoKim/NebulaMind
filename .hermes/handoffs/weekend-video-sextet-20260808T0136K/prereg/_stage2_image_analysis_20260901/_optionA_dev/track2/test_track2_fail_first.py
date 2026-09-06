"""TRACK 2 FAIL-FIRST tests (Blanc 21:02 + 21:04 KST; codex probe 21:00). Target: provenance_designs_v2 — run FIRST against a byte-copy of
provenance_designs.py (6ff0f7dc…): the history tests reproduce codex's two counterexamples and FAIL; the event-path tests FAIL because the
mechanisms do not exist; then against the repaired v2. Remotes are LOCAL BARE repositories with non-fast-forward receives denied (labelled: a
stand-in for the protected GitHub branch; `git ls-remote` against a path is the same command as against https://github.com/…, minus TLS).
Event feeds and the `gh` runner are FIXTURE-SUPPLIED (labelled)."""
import json, unittest, tempfile, subprocess, sys, hashlib
from pathlib import Path
HERE = Path(__file__).resolve().parent; sys.path.insert(0, str(HERE)); sys.path.insert(0, str(HERE.parent / "corpus_identity"))
import provenance_designs_v2 as P, history_v2 as H
def git(cwd, *a, check=True):
    r = subprocess.run(["git", *a], cwd=cwd, capture_output=True, text=True); 
    if check and r.returncode: raise RuntimeError(r.stderr)
    return r.stdout.strip()
REF = "refs/heads/main"
def scaffold():
    """bare remote (denyNonFastforwards) + client clone with an initial commit pushed; returns (bare, work)."""
    tmp = Path(tempfile.mkdtemp()); bare = tmp / "remote.git"; work = tmp / "work"
    subprocess.run(["git", "init", "-q", "--bare", str(bare)], check=True); git(bare, "config", "receive.denyNonFastforwards", "true"); git(bare, "config", "receive.denyDeletes", "true")
    subprocess.run(["git", "clone", "-q", str(bare), str(work)], check=True, capture_output=True); git(work, "config", "user.email", "t@t"); git(work, "config", "user.name", "t")
    (work / "seed").write_text("x"); git(work, "add", "seed"); git(work, "commit", "-q", "-m", "init"); git(work, "push", "-q", "-u", "origin", "HEAD:" + REF)
    return bare, work
def open_history(work, bare):
    log = work / "collection_log.jsonl"; H.genesis(log, "a" * 64, "t", "b" * 64, 1); git(work, "add", log.name); git(work, "commit", "-q", "-m", "history-open"); oc = git(work, "rev-parse", "HEAD"); git(work, "push", "-q", "origin", "HEAD:" + REF)
    H.append(log, {"stage": "collector-collect", "outcome": "RETRY"}); git(work, "commit", "-q", "-am", "attempt 1: RETRY"); git(work, "push", "-q", "origin", "HEAD:" + REF)
    return log, oc
class History(unittest.TestCase):
    def test_honest_continuation_pushed_each_entry(self):
        bare, work = scaffold(); log, oc = open_history(work, bare)
        H.append(log, {"stage": "builder-accept", "record_sha256": "c" * 64, "outcome": "ACCEPT-DRAND", "seed_hex": "d" * 64}); git(work, "commit", "-q", "-am", "accept"); git(work, "push", "-q", "origin", "HEAD:" + REF)
        ok, why, info = P.validate_continuation_v2(work, log.name, oc, str(bare), REF); self.assertTrue(ok, why); self.assertEqual(info["remote_head"], git(work, "rev-parse", "HEAD")); self.assertEqual(info["acknowledged_entries"], 3)
    def test_codex_counterexample_1_unpushed_append(self):                       # valid chain, remote unchanged: an UNCOMMITTED accept governs nothing
        bare, work = scaffold(); log, oc = open_history(work, bare)
        H.append(log, {"stage": "builder-accept", "record_sha256": "c" * 64, "outcome": "ACCEPT-DRAND", "seed_hex": "d" * 64}); self.assertTrue(H.validate(log))
        ok, why, _ = P.validate_continuation_v2(work, log.name, oc, str(bare), REF); self.assertFalse(ok, "an unpushed extension must not validate"); self.assertIn("PENDING-PUSH", why)
        git(work, "commit", "-q", "-am", "accept, committed but NOT pushed")                          # committed-but-unpushed is the same state
        ok, why, _ = P.validate_continuation_v2(work, log.name, oc, str(bare), REF); self.assertFalse(ok); self.assertIn("PENDING-PUSH", why)
    def test_codex_counterexample_2_local_reset_and_replacement(self):           # reset the client to history-open, replace RETRY by an ACCEPT; remote unchanged
        bare, work = scaffold(); log, oc = open_history(work, bare)
        git(work, "reset", "-q", "--hard", oc); H.append(log, {"stage": "builder-accept", "record_sha256": "c" * 64, "outcome": "ACCEPT-DRAND", "seed_hex": "d" * 64}); git(work, "commit", "-q", "-am", "replacement accept"); self.assertTrue(H.validate(log))
        ok, why, _ = P.validate_continuation_v2(work, log.name, oc, str(bare), REF); self.assertFalse(ok, "a local rewrite with the remote unchanged must not validate")
        r = subprocess.run(["git", "push", "-q", "origin", "HEAD:" + REF], cwd=work, capture_output=True, text=True); self.assertNotEqual(r.returncode, 0)   # the protected remote denies the non-fast-forward
        ok, why, _ = P.validate_continuation_v2(work, log.name, oc, str(bare), REF); self.assertFalse(ok)
    def test_stale_expected_head_unavailable_remote_and_unpublished_open_commit(self):
        bare, work = scaffold(); log, oc = open_history(work, bare); old = git(work, "rev-parse", "HEAD")
        H.append(log, {"stage": "collector-collect", "outcome": "RETRY"}); git(work, "commit", "-q", "-am", "attempt 2"); git(work, "push", "-q", "origin", "HEAD:" + REF)
        ok, why, _ = P.validate_continuation_v2(work, log.name, oc, str(bare), REF, expected_head=old); self.assertFalse(ok); self.assertIn("STALE", why)   # a cached/operator-supplied head is refused when the live remote differs
        ok, why, _ = P.validate_continuation_v2(work, log.name, oc, str(bare) + ".missing", REF); self.assertFalse(ok); self.assertIn("REMOTE-UNAVAILABLE", why)          # unavailable remote: RETRY, never a pass
        ok, why, _ = P.validate_continuation_v2(work, log.name, "0" * 40, str(bare), REF); self.assertFalse(ok); self.assertIn("OPEN", why)                               # an open commit the remote never acknowledged
    def test_deleted_suffix_and_rebuild_with_remote_consulted(self):
        bare, work = scaffold(); log, oc = open_history(work, bare); good = log.read_bytes()
        lines = good.split(b"\n"); log.write_bytes(b"\n".join(lines[:-2]) + b"\n"); self.assertTrue(H.validate(log))
        ok, why, _ = P.validate_continuation_v2(work, log.name, oc, str(bare), REF); self.assertFalse(ok)
        log.unlink(); H.genesis(log, "a" * 64, "t", "b" * 64, 1); git(work, "commit", "-q", "-am", "rebuilt")
        ok, why, _ = P.validate_continuation_v2(work, log.name, oc, str(bare), REF); self.assertFalse(ok)
class Events(unittest.TestCase):
    def runner_ok(self, pages):
        """FIXTURE-SUPPLIED `gh api` runner: returns pages in order, then an empty page (the API's end)."""
        def run(cmd):
            ep = cmd[-1]; page = int(ep.split("page=")[-1]); body = pages[page - 1] if page <= len(pages) else []
            return 0, json.dumps(body), ""
        return run
    def test_retrieval_and_pagination_execute(self):
        e = [{"type": "PushEvent", "id": str(i), "created_at": f"2026-09-07T01:{59 - i:02d}:00Z", "repo": {"name": "r"}, "payload": {"ref": REF, "head": "a" * 40}} for i in range(5)]
        events, prov = P.retrieve_events("r", self.runner_ok([e[:2], e[2:4], e[4:]]), per_page=2, max_pages=10)
        self.assertEqual([x["id"] for x in events], ["0", "1", "2", "3", "4"]); self.assertEqual(prov["pages_fetched"], 3); self.assertEqual(prov["oldest_created_at"], e[4]["created_at"]); self.assertEqual(len(prov["endpoints"]), 3)
        events, prov = P.retrieve_events("r", self.runner_ok([e[:2], e[2:4], e[4:]]), per_page=2, max_pages=2); self.assertEqual(len(events), 4); self.assertTrue(prov["truncated_by_max_pages"])
    def test_error_handling_each_failure_takes_its_path(self):
        def http(code, msg): return lambda cmd: (1, "", f"gh: HTTP {code}: {msg}")
        with self.assertRaises(P.EventsUnavailable) as cm: P.retrieve_events("r", http(403, "API rate limit exceeded"))
        self.assertEqual(cm.exception.kind, "RATE-LIMITED")
        with self.assertRaises(P.EventsUnavailable) as cm: P.retrieve_events("r", http(502, "Bad Gateway"))
        self.assertEqual(cm.exception.kind, "SERVER-ERROR")
        with self.assertRaises(P.EventsUnavailable) as cm: P.retrieve_events("r", http(401, "Bad credentials"))
        self.assertEqual(cm.exception.kind, "AUTH")
        with self.assertRaises(P.EventsUnavailable) as cm: P.retrieve_events("r", lambda cmd: (0, "{not json", ""))
        self.assertEqual(cm.exception.kind, "MALFORMED")
        with self.assertRaises(P.EventsUnavailable) as cm: P.retrieve_events("r", lambda cmd: (0, json.dumps({"message": "Not Found"}), ""))
        self.assertEqual(cm.exception.kind, "MALFORMED")
        def boom(cmd): raise TimeoutError("gh hung")
        with self.assertRaises(P.EventsUnavailable) as cm: P.retrieve_events("r", boom)
        self.assertEqual(cm.exception.kind, "TRANSPORT")
        self.assertEqual(P.authenticate_event_live({"type": "PushEvent"}, "r", boom, REF, "a" * 40)[0], "UNAVAILABLE")
    def test_expired_event_and_independent_receipt_path(self):
        C = "a" * 40; genuine = {"type": "PushEvent", "id": "1", "created_at": "2026-09-07T01:05:00Z", "repo": {"name": "DuhoKim/NebulaMind"}, "payload": {"ref": REF, "head": C, "commits": [{"sha": C}]}}
        newer = [{"type": "PushEvent", "id": str(9 + i), "created_at": f"2026-10-{20 + i:02d}T00:00:00Z", "repo": {"name": "DuhoKim/NebulaMind"}, "payload": {"ref": REF, "head": "b" * 40}} for i in range(3)]
        live = self.runner_ok([newer])                                                                       # the feed no longer reaches back to the approval
        self.assertEqual(P.authenticate_event_live(genuine, "DuhoKim/NebulaMind", live, REF, C)[0], "EXPIRED")
        bare, work = scaffold()                                                                               # the OPS receipt: taken inside the window, committed and pushed
        receipt = P.write_events_receipt(work / "EVENTS_RECEIPT_T.json", [genuine, newer[0]], {"endpoints": ["e1"], "retrieved_utc": "2026-09-07T02:00:00Z", "gh_version": "gh test"}, origin={"actor": "blanc-ops", "session": "OPS", "note": "independent retrieval"})
        git(work, "add", receipt.name); git(work, "commit", "-q", "-m", "events receipt"); git(work, "push", "-q", "origin", "HEAD:" + REF)
        ok, why = P.verify_events_receipt(receipt, work, str(bare), REF, genuine, expected_origin={"actor": "blanc-ops", "session": "OPS"}); self.assertTrue(ok, why)
        forged = dict(genuine); forged["created_at"] = "2000-01-01T00:00:00Z"                                # the lane forges a receipt naming a different event, digests recomputed
        P.write_events_receipt(receipt, [forged], {"endpoints": ["e1"], "retrieved_utc": "x", "gh_version": "gh test"}, origin={"actor": "blanc-ops", "session": "OPS"}); git(work, "commit", "-q", "-am", "replaced receipt")
        ok, why = P.verify_events_receipt(receipt, work, str(bare), REF, forged, expected_origin={"actor": "blanc-ops", "session": "OPS"}); self.assertFalse(ok); self.assertIn("RECEIPT-NOT-FIRST", why)   # the receipt path was rewritten after its first commit
        git(work, "push", "-q", "origin", "HEAD:" + REF)                                                      # even pushed, a second version of the receipt is refused
        ok, why = P.verify_events_receipt(receipt, work, str(bare), REF, forged, expected_origin={"actor": "blanc-ops", "session": "OPS"}); self.assertFalse(ok)
        ok, why = P.verify_events_receipt(receipt, work, str(bare), REF, genuine, expected_origin={"actor": "someone-else", "session": "OPS"}); self.assertFalse(ok)   # wrong origin
        (work / "EVENTS_RECEIPT_U.json").write_text("x"); ok, why = P.verify_events_receipt(work / "EVENTS_RECEIPT_U.json", work, str(bare), REF, genuine, expected_origin={"actor": "blanc-ops", "session": "OPS"}); self.assertFalse(ok)   # unpushed / malformed
if __name__ == "__main__": unittest.main()
