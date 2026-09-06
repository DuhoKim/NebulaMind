#!/usr/bin/env python3
"""COHERENT-ATTACK INSPECTION of the STAGED V29 candidate (driver v13, verdict v29, provenance_designs_v9; supersedes the V28 inspection; earlier scripts retained
as pinned). Re-runs every reviewer counter-case with adjacent digests, counts and locks kept COHERENT, against DRIVER v13 with PRODUCTION's own re-deriver, and the
standalone v9 helpers — the modules this script imports are the ones it executes (codex V27-3: the V27 header named v10/v6 while executing v11/v7). Prints one row per case.
Deterministic; the output is filed as V29_CANDIDATE_ATTACK_INSPECTION_20260907.md."""
import json, sys, tempfile, hashlib, subprocess
from pathlib import Path
HERE = Path(__file__).resolve().parent; D = HERE.parent
for p in ("fourier_chirality", "corpus_identity", "beacon_v2", "drand_only", "track2"): sys.path.insert(0, str(D / p))
import run_configurations_v13 as rc, test_run_configurations_v13 as TF, history_v2 as H, provenance_designs_v9 as P, verify_drand_v2 as vd
TF.BD.EXCLUDED_ROUNDS = (6440756,)                                                   # exhibit round admissible in this inspection only (never a study seed)
def git(cwd, *a): return subprocess.run(["git", *a], cwd=cwd, capture_output=True, text=True, check=True).stdout.strip()
def attempt(name, kw, note=""):
    tmp = Path(tempfile.mkdtemp()); TP = TF.TPJ(tmp); ids = [str(500000 + i) for i in range(6)]; hold = [str(500000 + i) for i in range(6, 66)]
    try:
        ident = TF.identity(tmp, TP, ids, hold, **kw); rc.load_identity(ident, TP); res = "ACCEPTED"
    except rc.DataIntegrityFail as e: res = "REFUSED " + str(e).split(":")[0]
    except SystemExit as e: res = "REFUSED(fixture) " + str(e)[:40]
    rows.append((name, res, note)); return tmp, TP
rows = []
def M(**kv):
    def f(I, ctx):
        for k, v in kv.items():
            d = I
            for part in k.split(".")[:-1]: d = d[part]
            d[k.split(".")[-1]] = v
    return f
# 0 the successful production path
attempt("0 baseline: real evidence, real seed, PRODUCTION re-deriver", {}, "the happy path")
# 1 codex: fabricated event, coherently recomputed digest, invented provenance
def forge(I, ctx):
    ev = {"type": "PushEvent", "id": "invented", "created_at": "2000-01-01T00:00:00Z", "repo": {"name": "attacker/unrelated"}, "payload": {"ref": "refs/heads/main", "head": ctx["commit"], "commits": [{"sha": ctx["commit"]}]}}
    I["approval_witness"]["push_event"] = ev; I["approval_witness"]["push_event_sha256"] = P.canon(ev); I["approval_witness"]["events_provenance"] = {"endpoints": ["https://attacker.invalid/events"], "retrieved_utc": "not-a-time"}
attempt("1 forged event (coherent digest, invented provenance)", {"mutate": forge}, "TRACK 2(a): codex's wrong-repository forgery → INCONSISTENT-INPUT (row 9b); a same-id / same-commit contradiction → FORGED (rows 9s–9u; see below)")
# 2 codex: deleted/recreated two-entry history with consistent lock/count/digests
def rebuild(I, ctx):
    ctx["log"].unlink(); H.genesis(ctx["log"], I["approval_witness"]["record_sha256"], I["T_pulse"], I["rule_sha256"], I["beacon_round"])
    e = H.append(ctx["log"], {"stage": "builder-accept", "record_sha256": I["beacon_record_sha256"], "outcome": "ACCEPT-DRAND", "seed_hex": I["seed_hex"], "source": "drand-mainnet-default"})
    I["collection_lock"] = {"first_accept": e, "log_sha256": rc.sha_file(ctx["log"]), "entries": 2}
attempt("2 history deleted and rebuilt before the freeze (consistent lock/count/digest)", {"mutate": rebuild}, "TRACK 2(b): validate_continuation → NOT-AN-EXTENSION (see below)")
# 3 codex: second approval-record path committed and pushed
tmp3, TP3 = attempt("3a (setup) baseline in a fresh repo", {})
work = Path(TP3.seal_journal).parent; (work / "APPROVAL_RECORD_SELRULE_V22_T_second.md").write_bytes(b"RULE_SHA256: x\n"); git(work, "add", "APPROVAL_RECORD_SELRULE_V22_T_second.md"); git(work, "commit", "-q", "-m", "second"); git(work, "push", "-q", "origin", "HEAD:refs/heads/main")
ident3 = sorted(work.glob("identity_*.json"))[0]
try: rc.load_identity(ident3, TP3); rows.append(("3 second approval-record path committed and pushed", "ACCEPTED", ""))
except rc.DataIntegrityFail as e: rows.append(("3 second approval-record path committed and pushed", "REFUSED " + str(e).split(":")[0], "v6 reproduces W4"))
# 4 codex: re-encoded retained bodies with matching digests (SAME value)
def reencode(I, ctx):
    rec = json.loads(ctx["rp"].read_text()); import base64
    for u, r in rec["relays"].items():
        if "body_b64" in r: b = json.loads(base64.b64decode(r["body_b64"])); r["body_b64"] = base64.b64encode(json.dumps(b, indent=2, sort_keys=True).encode()).decode()
    ctx["rp"].write_text(json.dumps(rec)); d = rc.sha_file(ctx["rp"]); I["beacon_record_sha256"] = d
    H.append(ctx["log"], {"stage": "builder-accept", "record_sha256": d, "outcome": "ACCEPT-DRAND", "seed_hex": I["seed_hex"], "source": "drand-mainnet-default"})   # a SECOND accept naming the re-encoded record
    I["collection_lock"] = {"first_accept": [e for e in H.validate(ctx["log"]) if e["stage"] == "builder-accept"][0], "log_sha256": rc.sha_file(ctx["log"]), "entries": len(H.validate(ctx["log"]))}
attempt("4 re-encoded retained bodies (same signature) with a coherently re-pointed record", {"mutate": reencode}, "same VALUE; the earliest accept names the first record → lock mismatch is the correct refusal; with the first record it is ACCEPTED (correctly)")
# 5 codex: uppercase live signature — verdict level
import beacon_record_drand_v29 as BD
REAL = json.loads((D / "drand_only" / "round_6441924_api.drand.sh.json").read_text()); BODY = json.dumps(REAL).encode()
from datetime import timedelta
TP = vd.round_time(6441924); TS = BD.fmt(TP - timedelta(seconds=600)); RD = "b" * 64; STMT = f"x {RD} {TS}".encode()
def relays(default=None):
    def fetch(url, timeout=30):
        for host in vd.RELAYS:
            if url == vd.round_url(host, 6441924): return default if default is not None else BODY
        raise OSError("404")
    return fetch
rec = BD.collect(relays(), TS, RD, STMT, now=TP + timedelta(minutes=1)); up = dict(REAL); up["signature"] = REAL["signature"].upper()
r = BD.verdict(rec, TP + timedelta(minutes=1), fetch=relays(json.dumps(up).encode()), rule_sha256=RD, statement_bytes=STMT)
rows.append(("5 live relay serves the signature in UPPERCASE hex", r["outcome"] + (" (same seed, representation recorded ×%d)" % len(r["checks"].get("live_representation_differs", {}))), "v22: decoded-bytes equality"))
# 6 codex: negative objids / arbitrary lists (inherited limitation)
def neg(I, ctx): I["tuning_objids"] = [-(i + 1) for i in range(6)]
attempt("6 negative tuning objids, coherently sealed", {"mutate": neg}, "INHERITED (V15 driver trusts the lists); verify_split (UNADOPTED, off) would refuse — exhibited in the e2e test on real builder output")
# 7 witness-closed entry then sealed
def closed(I, ctx):
    H.append(ctx["log"], {"stage": "witness-closed", "record_sha256": I["beacon_record_sha256"], "outcome": "ACCEPT-DRAND", "refusal": "APPROVAL-PUSH-EVENT-CLOSED", "state": "CLOSED"})
    I["collection_lock"]["log_sha256"] = rc.sha_file(ctx["log"]); I["collection_lock"]["entries"] = len(H.validate(ctx["log"]))
attempt("7 witness-closed entry present, coherently sealed", {"mutate": closed}, "v6: CLOSED is terminal")
# 8 deleted suffix, coherently sealed
def suffix(I, ctx):
    lines = ctx["log"].read_bytes().split(b"\n"); ctx["log"].write_bytes(b"\n".join(lines[:2]) + b"\n")                # genesis + collector-collect only: no accept
    I["collection_lock"]["log_sha256"] = rc.sha_file(ctx["log"]); I["collection_lock"]["entries"] = 2
attempt("8 history suffix deleted (accept removed), coherently sealed", {"mutate": suffix}, "internally valid chain; TRACK 2(b) refuses; v6 refuses here only because no accept remains")
# 9 the track-2 designs on attacks 1 and 2, explicitly
genuine = {"type": "PushEvent", "id": "1", "created_at": "2026-09-07T01:05:00Z", "repo": {"name": "DuhoKim/NebulaMind"}, "payload": {"ref": "refs/heads/feat/paper-workflow-v2", "head": "a" * 40, "commits": [{"sha": "a" * 40}]}}
forged = {**genuine, "id": "invented", "created_at": "2000-01-01T00:00:00Z", "repo": {"name": "attacker/unrelated"}}
feed = [genuine]                                                                                                       # FIXTURE-SUPPLIED live feed (labelled)
rows.append(("9a track 2(a) authenticate_event(genuine, fixture feed)", P.authenticate_event(genuine, feed, "DuhoKim/NebulaMind", "refs/heads/feat/paper-workflow-v2", "a" * 40)[0], "fixture feed"))
rows.append(("9b track 2(a) authenticate_event(codex's forgery, fixture feed)", P.authenticate_event(forged, feed, "DuhoKim/NebulaMind", "refs/heads/feat/paper-workflow-v2", "a" * 40)[0], "fixture feed"))
# 9c–9h: track 2(b) v3 — the remote is a LOCAL BARE repository with non-fast-forward receives denied; the gh runner is FIXTURE-SUPPLIED (both labelled)
tb = Path(tempfile.mkdtemp()); bare = tb / "remote.git"; w = tb / "w"; subprocess.run(["git", "init", "-q", "--bare", str(bare)], check=True); git(bare, "config", "receive.denyNonFastforwards", "true")
subprocess.run(["git", "clone", "-q", str(bare), str(w)], check=True, capture_output=True); git(w, "config", "user.email", "t@t"); git(w, "config", "user.name", "t"); (w / "s").write_text("x"); git(w, "add", "s"); git(w, "commit", "-q", "-m", "i"); git(w, "push", "-q", "-u", "origin", "HEAD:refs/heads/main")
EV9 = []
def pev(commit, n, wk=None): return {"type": "PushEvent", "id": f"h{n}", "created_at": f"2026-09-07T01:{n:02d}:00Z", "repo": {"name": "DuhoKim/NebulaMind"}, "payload": {"ref": "refs/heads/main", "before": git(wk or w, "rev-parse", commit + "^"), "head": commit, "commits": [{"sha": commit}]}}
def feed9(events): return lambda cmd: (0, json.dumps(events if cmd[-1].endswith("page=1") else []), "")
log = w / "collection_log.jsonl"; H.genesis(log, "a" * 64, "t", "b" * 64, 1); oc = P.publish_entry(w, log.name, str(bare), "refs/heads/main", "history-open"); EV9.append(pev(oc, 0))
H.append(log, {"stage": "collector-collect", "outcome": "RETRY"}); c1 = P.publish_entry(w, log.name, str(bare), "refs/heads/main", "retry"); EV9.append(pev(c1, 1))
def vc(open_event=None, events=None): ok, why, _ = P.validate_continuation_v7(w, log.name, str(bare), "refs/heads/main", open_event or EV9[0], feed9(events if events is not None else EV9), "DuhoKim/NebulaMind"); return "OK" if ok else "REFUSED " + why.split(":")[0]
rows.append(("9c track 2(b) v4 validate_continuation_v7(genuine: genesis-only open commit, authentic open event, one server-timed push event per commit)", vc(), "asks the remote; authenticates the open event; per-commit push events"))
H.append(log, {"stage": "builder-accept", "record_sha256": "c" * 64, "outcome": "ACCEPT-DRAND", "seed_hex": "d" * 64}); rows.append(("9d track 2(b) v3: codex V21 counterexample 1 — ACCEPT appended, NOT pushed", vc(), ""))
git(w, "commit", "-q", "-am", "accept unpushed"); rows.append(("9e track 2(b) v3: committed but NOT acknowledged by the remote", vc(), ""))
git(w, "reset", "-q", "--hard", oc); H.append(log, {"stage": "builder-accept", "record_sha256": "c" * 64, "outcome": "ACCEPT-DRAND", "seed_hex": "d" * 64}); git(w, "commit", "-q", "-am", "replacement"); rows.append(("9f track 2(b) v3: codex V21 counterexample 2 — local reset to history-open, RETRY replaced by ACCEPT, remote unchanged", vc(), ""))
r = subprocess.run(["git", "push", "-q", "origin", "HEAD:refs/heads/main"], cwd=w, capture_output=True); rows.append(("9g track 2(b) v3: the rewrite pushed to the protected remote", ("push REJECTED (non-fast-forward); " if r.returncode else "push accepted?!; ") + vc(), ""))
rows.append(("9h track 2(b) v3: remote unreachable", "REFUSED " + P.validate_continuation_v3(w, log.name, str(bare) + ".missing", "refs/heads/main", EV9[0], feed9(EV9), "DuhoKim/NebulaMind")[1].split(":")[0], "RETRY, never a pass"))
git(w, "reset", "-q", "--hard", c1); rows.append(("9i track 2(b) v3: open event ABSENT from the live feed", vc(events=EV9[1:]), "codex V22 A: the anchor is authenticated"))
rows.append(("9j track 2(b) v3: live feed EMPTY", vc(events=[]), "codex V22 F: UNAVAILABLE, never FORGED"))
tb2 = Path(tempfile.mkdtemp()); bare2 = tb2 / "remote.git"; w2 = tb2 / "w"; subprocess.run(["git", "init", "-q", "--bare", str(bare2)], check=True); subprocess.run(["git", "clone", "-q", str(bare2), str(w2)], check=True, capture_output=True); git(w2, "config", "user.email", "t@t"); git(w2, "config", "user.name", "t"); (w2 / "s").write_text("x"); git(w2, "add", "s"); git(w2, "commit", "-q", "-m", "i"); git(w2, "push", "-q", "-u", "origin", "HEAD:refs/heads/main")
log2 = w2 / "collection_log.jsonl"; H.genesis(log2, "a" * 64, "t", "b" * 64, 1); H.append(log2, {"stage": "builder-accept", "record_sha256": "c" * 64, "outcome": "ACCEPT-DRAND", "seed_hex": "d" * 64}); git(w2, "add", log2.name); git(w2, "commit", "-q", "-m", "late first publication"); lc = git(w2, "rev-parse", "HEAD"); git(w2, "push", "-q", "origin", "HEAD:refs/heads/main")
ok, why, _ = P.validate_continuation_v7(w2, log2.name, str(bare2), "refs/heads/main", pev(lc, 0, w2), feed9([pev(lc, 0, w2)]), "DuhoKim/NebulaMind"); rows.append(("9k track 2(b) v7: codex V22 attack A — rebuilt history published as the FIRST commit, named history-open", "OK" if ok else "REFUSED " + why.split(":")[0], "v2 said True"))
# 9l: codex V23 M1 — four single-entry commits delivered by ONE late push
tb3 = Path(tempfile.mkdtemp()); bare3 = tb3 / "remote.git"; w3 = tb3 / "w"; subprocess.run(["git", "init", "-q", "--bare", str(bare3)], check=True); subprocess.run(["git", "clone", "-q", str(bare3), str(w3)], check=True, capture_output=True); git(w3, "config", "user.email", "t@t"); git(w3, "config", "user.name", "t"); (w3 / "s").write_text("x"); git(w3, "add", "s"); git(w3, "commit", "-q", "-m", "i"); git(w3, "push", "-q", "-u", "origin", "HEAD:refs/heads/main"); base3 = git(w3, "rev-parse", "HEAD")
log3 = w3 / "collection_log.jsonl"; H.genesis(log3, "a" * 64, "t", "b" * 64, 1); git(w3, "add", log3.name); git(w3, "commit", "-q", "-m", "open"); c0 = git(w3, "rev-parse", "HEAD")
for e in ({"stage": "collector-collect", "outcome": "RETRY"}, {"stage": "builder-verdict", "outcome": "ACCEPT-DRAND", "record_sha256": "c" * 64, "seed_hex": "d" * 64}, {"stage": "builder-accept", "outcome": "ACCEPT-DRAND", "record_sha256": "c" * 64, "seed_hex": "d" * 64}): H.append(log3, e); git(w3, "commit", "-q", "-am", "e")
c3 = git(w3, "rev-parse", "HEAD"); git(w3, "push", "-q", "origin", "HEAD:refs/heads/main")
late = {"type": "PushEvent", "id": "late", "created_at": "2026-09-07T01:09:00Z", "repo": {"name": "DuhoKim/NebulaMind"}, "payload": {"ref": "refs/heads/main", "before": base3, "head": c3, "commits": [{"sha": c0}, {"sha": c3}]}}
ok3, why3, _ = P.validate_continuation_v3(w3, log3.name, str(bare3), "refs/heads/main", late, feed9([late]), "DuhoKim/NebulaMind"); ok4, why4, _ = P.validate_continuation_v7(w3, log3.name, str(bare3), "refs/heads/main", late, feed9([late]), "DuhoKim/NebulaMind")
rows.append(("9l codex V23 M1: four single-entry commits delivered by ONE late push", f"v3: {'OK' if ok3 else 'REFUSED'} / v7: {'OK' if ok4 else 'REFUSED ' + why4.split(':')[0]}", "v3 said True; v6 requires one server-timed push event per commit (proven batch = terminal)"))
# 9m–9p: codex V24 N2/N3 dispositions and the producer precondition (v5)
def feeds9(*calls):
    st = {"k": -1}
    def run(cmd):
        if cmd[-1].endswith("page=1"): st["k"] = min(st["k"] + 1, len(calls) - 1)
        return 0, json.dumps(calls[st["k"]] if cmd[-1].endswith("page=1") else []), ""
    return run
git(w, "reset", "-q", "--hard", c1); H.append(log, {"stage": "builder-accept", "record_sha256": "c" * 64, "outcome": "ACCEPT-DRAND", "seed_hex": "d" * 64}); c2 = P.publish_entry(w, log.name, str(bare), "refs/heads/main", "accept"); EV9.append(pev(c2, 2))
ok, why, _ = P.validate_continuation_v7(w, log.name, str(bare), "refs/heads/main", EV9[0], feeds9(EV9, []), "DuhoKim/NebulaMind"); rows.append(("9m codex V24 N2: complete feed for approval/open, EMPTY feed on the per-entry retrieval", "REFUSED " + why.split(":")[0], "v4 said BATCH; v5 = retry"))
ok, why, _ = P.validate_continuation_v7(w, log.name, str(bare), "refs/heads/main", EV9[0], feed9([EV9[0], EV9[2]]), "DuhoKim/NebulaMind"); rows.append(("9n codex V24 N2: one middle per-commit event missing, no evidence of batching", "REFUSED " + why.split(":")[0], "v4 said BATCH; v5 = retry within the window"))
(w / "unrelated").write_text("u"); git(w, "add", "unrelated"); git(w, "commit", "-q", "-m", "unrelated local commit"); H.append(log, {"stage": "collector-collect", "outcome": "RETRY"})
try: P.publish_entry(w, log.name, str(bare), "refs/heads/main", "entry"); rows.append(("9o codex V24 N3: unrelated unpublished commit alongside a new entry", "PUBLISHED (v4 behaviour)", ""))
except SystemExit as e: rows.append(("9o codex V24 N3: unrelated unpublished commit alongside a new entry", "REFUSED " + str(e).split(":")[0], "v5 producer precondition; nothing pushed"))
# 9p–9r: codex V25 P1/P2 (v6)
git(w, "reset", "-q", "--hard", c2)
late_anc = {"type": "PushEvent", "id": "late-anc", "created_at": "2026-09-07T01:09:00Z", "repo": {"name": "DuhoKim/NebulaMind"}, "payload": {"ref": "refs/heads/main", "before": base3, "head": c3}}   # no payload.commits (GitHub's documented shape)
ok5, why5, _ = P.validate_continuation_v5(w3, log3.name, str(bare3), "refs/heads/main", late_anc, feed9([late_anc]), "DuhoKim/NebulaMind"); ok6, why6, _ = P.validate_continuation_v7(w3, log3.name, str(bare3), "refs/heads/main", late_anc, feed9([late_anc]), "DuhoKim/NebulaMind")
rows.append(("9p codex V25 P1: the same late batch, push event WITHOUT payload.commits (before..head only)", f"v5: REFUSED {why5.split(':')[0]} / v6: REFUSED {why6.split(':')[0]}", "v5 called a proven batch 'incomplete'; v6 uses the ancestry predicate → terminal"))
e_ret = EV9[1]; others = [x for x in EV9 if x is not e_ret]                      # a MIDDLE event: the feed still covers its time (an older event is present)
rows.append(("9q codex V25 P2: the retained approval event ABSENT from a non-empty feed that covers its time", "v6: " + P.authenticate_event(e_ret, others, "DuhoKim/NebulaMind", "refs/heads/main", e_ret["payload"]["head"], feed_reaches_back_to=min(x["created_at"] for x in others))[0] + " (the v5 function said FORGED — receipt run 1b)", "absence is not forgery"))
contradict = {**e_ret, "id": "different-bytes"}
rows.append(("9r codex V25 P2: a push delivering the same commit with DIFFERENT bytes", P.authenticate_event(e_ret, others + [contradict], "DuhoKim/NebulaMind", "refs/heads/main", e_ret["payload"]["head"])[0], "affirmative contradiction → FORGED"))
# 9s–9u: codex V26-1 / V26-2 (v7)
ret1 = json.loads(json.dumps(e_ret)); ret1["payload"]["before"] = "0" * 40
rows.append(("9s codex V26-1: retained event = the live event with a DIFFERENT `before` only (same id, same head)", "v7: " + P.authenticate_event(ret1, others + [e_ret], "DuhoKim/NebulaMind", "refs/heads/main", e_ret["payload"]["head"], feed_reaches_back_to=min(x["created_at"] for x in others))[0] + " (v6 said INCOMPLETE — receipt run 1b)", "same-event contradiction → terminal"))
tb4 = Path(tempfile.mkdtemp()); bare4 = tb4 / "remote.git"; w4 = tb4 / "w"; subprocess.run(["git", "init", "-q", "--bare", str(bare4)], check=True); subprocess.run(["git", "clone", "-q", str(bare4), str(w4)], check=True, capture_output=True); git(w4, "config", "user.email", "t@t"); git(w4, "config", "user.name", "t"); (w4 / "s").write_text("x"); git(w4, "add", "s"); git(w4, "commit", "-q", "-m", "i"); git(w4, "push", "-q", "-u", "origin", "HEAD:refs/heads/main"); base4 = git(w4, "rev-parse", "HEAD")
(w4 / "a").write_text("a"); git(w4, "add", "a"); git(w4, "commit", "-q", "-m", "approval"); ca = git(w4, "rev-parse", "HEAD"); git(w4, "push", "-q", "origin", "HEAD:refs/heads/main"); stale = tb4 / "stale"; subprocess.run(["git", "clone", "-q", str(bare4), str(stale)], check=True, capture_output=True)
(w4 / "l").write_text("l"); git(w4, "add", "l"); git(w4, "commit", "-q", "-m", "later"); hd = git(w4, "rev-parse", "HEAD"); git(w4, "push", "-q", "origin", "HEAD:refs/heads/main")
anc = {"type": "PushEvent", "id": "anc", "created_at": "2026-09-07T01:05:00Z", "repo": {"name": "DuhoKim/NebulaMind"}, "payload": {"ref": "refs/heads/main", "before": base4, "head": hd}}
rows.append(("9t codex V26-2: before..head delivery, full clone", "v7: " + P.authenticate_event(anc, [anc], "DuhoKim/NebulaMind", "refs/heads/main", ca, root=w4)[0], ""))
rows.append(("9u codex V26-2: the same event and feed, a clone MISSING the descendant object", "v7: " + P.authenticate_event(anc, [anc], "DuhoKim/NebulaMind", "refs/heads/main", ca, root=stale)[0] + " (v6 said FORGED — receipt run 1b)", "undeterminable delivery → retry, never forgery"))
# 10: THE THREE STATES on the PRODUCTION CALL PATH — the same identity through the same load_identity under OFFLINE (default) and COMPOSED (UNADOPTED; v7 on v3)
import hashlib
def canon(e): return hashlib.sha256(json.dumps(e, sort_keys=True, separators=(",", ":")).encode()).hexdigest()
def feed(events): return lambda cmd: (0, json.dumps(events if cmd[-1].endswith("page=1") else []), "")     # FIXTURE-SUPPLIED gh runner (labelled)
def composed_case(name, extra_mutate, forge_feed=False, late_first=False):
    tmpc = Path(tempfile.mkdtemp()); TPc = TF.TPJ(tmpc); rc.ADOPTION_FILE = Path(TPc.adoption_file); workc = Path(TPc.seal_journal).parent; git(TPc.witness_remote_url, "config", "receive.denyNonFastforwards", "true"); openf = workc / "HISTORY_OPEN_EVENT.json"; EVS = []
    comp = rc.Protocol(**{**TPc.__dict__, "provenance_mode": "composed", "events_repo": "DuhoKim/NebulaMind", "history_open_event_file": str(openf)})
    def publish(I, ctx):
        ev = I["approval_witness"]["push_event"]; ev["repo"] = {"name": "DuhoKim/NebulaMind"}; I["approval_witness"]["push_event_sha256"] = canon(ev)
        if late_first:                                                                                     # codex V22 attack A: rebuild BEFORE first publication, publish as first commit
            ctx["log"].unlink(); H.genesis(ctx["log"], I["approval_witness"]["record_sha256"], I["T_pulse"], I["rule_sha256"], I["beacon_round"])
            e = H.append(ctx["log"], {"stage": "builder-accept", "record_sha256": I["beacon_record_sha256"], "outcome": "ACCEPT-DRAND", "seed_hex": I["seed_hex"], "source": "drand-mainnet-default"}); I["collection_lock"] = {"first_accept": e, "log_sha256": rc.sha_file(ctx["log"]), "entries": 2}
            git(workc, "add", ctx["log"].name); git(workc, "commit", "-q", "-m", "late first publication"); c = git(workc, "rev-parse", "HEAD"); git(workc, "push", "-q", "origin", "HEAD:refs/heads/main"); EVS.append(pev(c, 0, workc)); openf.write_text(json.dumps(EVS[0])); git(workc, "add", openf.name); return
        log = ctx["log"]; lines = [l for l in log.read_bytes().split(b"\n") if l]
        for n in range(len(lines)):
            log.write_bytes(b"\n".join(lines[: n + 1]) + b"\n"); git(workc, "add", log.name); git(workc, "commit", "-q", "-m", f"entry {n}"); c = git(workc, "rev-parse", "HEAD"); git(workc, "push", "-q", "origin", "HEAD:refs/heads/main"); EVS.append(pev(c, n, workc))
            if n == 0: openf.write_text(json.dumps(EVS[0])); git(workc, "add", openf.name)
        if extra_mutate: extra_mutate(I, ctx)
    ident = TF.identity(tmpc, comp, [str(500000 + i) for i in range(6)], [str(500000 + i) for i in range(6, 66)], mutate=publish); ev = json.loads(ident.read_text())["approval_witness"]["push_event"]
    try: rc.load_identity(ident, TPc); off = "ACCEPTED"
    except rc.DataIntegrityFail as e: off = "REFUSED " + str(e).split(":")[0]
    live = ([{**ev, "id": "genuine-other", "created_at": "2026-09-06T00:00:00Z"}] if forge_feed else [ev]) + EVS
    try: rc.load_identity(ident, rc.Protocol(**{**comp.__dict__, "events_runner": feed(live)})); comp_r = "ACCEPTED"
    except rc.DataIntegrityFail as e: comp_r = "REFUSED " + str(e).split(":")[0] + (" (" + str(e).split(":")[1].strip()[:40] + ")" if ":" in str(e) else "")
    rows.append((name, f"offline: {off} / composed: {comp_r}", "same identity, same load_identity call; composed = UNADOPTED"))
composed_case("10a genuine identity, history published one entry per acknowledged commit, open event + approval event in the live feed", None)
def forge2(I, ctx):
    ev = {"type": "PushEvent", "id": "invented", "created_at": "2000-01-01T00:00:00Z", "repo": {"name": "DuhoKim/NebulaMind"}, "payload": {"ref": "refs/heads/main", "head": ctx["commit"], "commits": [{"sha": ctx["commit"]}]}}
    I["approval_witness"]["push_event"] = ev; I["approval_witness"]["push_event_sha256"] = canon(ev); I["approval_witness"]["events_provenance"] = {"endpoints": ["https://attacker.invalid/events"], "retrieved_utc": "not-a-time"}
composed_case("10b attack 1 again: forged approval event (coherent digest; names the pinned repo), live feed does not contain it", forge2, forge_feed=True)
def rebuild2(I, ctx):
    ctx["log"].unlink(); H.genesis(ctx["log"], I["approval_witness"]["record_sha256"], I["T_pulse"], I["rule_sha256"], I["beacon_round"])
    e = H.append(ctx["log"], {"stage": "builder-accept", "record_sha256": I["beacon_record_sha256"], "outcome": "ACCEPT-DRAND", "seed_hex": I["seed_hex"], "source": "drand-mainnet-default"})
    I["collection_lock"] = {"first_accept": e, "log_sha256": rc.sha_file(ctx["log"]), "entries": 2}
composed_case("10c attack 2 again: history rebuilt after honest publication, coherently sealed and pushed fast-forward", rebuild2)
composed_case("10d codex V22 attack A: history rebuilt BEFORE its first publication, published as the first commit and named history-open", None, late_first=True)
print("| attack | staged V29 candidate (driver v13 / verdict v29 / provenance v9) | note |"); print("|---|---|---|")
for n, r, note in rows: print(f"| {n} | {r} | {note} |")
