#!/usr/bin/env python3
"""COHERENT-ATTACK INSPECTION of the STAGED V22 candidate (Blanc 20:45: "inspect BOTH the successful production path AND the prior reviewer's coherent
attacks against the same pinned candidate"). Re-runs codex's V21 substitutions — each mutation keeps every adjacent digest/count/lock COHERENT — against
driver v6 with PRODUCTION's own re-deriver, and, for the two provenance boundaries, ALSO against the UNADOPTED track-2 designs (fixture-supplied feed,
labelled). Prints one row per attack: what v6 does (ACCEPTED = the attack passes; a named refusal = it does not) and what the track-2 design would do.
Deterministic; the output is filed as V22_CANDIDATE_ATTACK_INSPECTION_20260906.md."""
import json, sys, tempfile, hashlib, subprocess
from pathlib import Path
HERE = Path(__file__).resolve().parent; D = HERE.parent
for p in ("fourier_chirality", "corpus_identity", "beacon_v2", "drand_only", "track2"): sys.path.insert(0, str(D / p))
import run_configurations_v6 as rc, test_run_configurations_v6 as TF, history_v2 as H, provenance_designs_v2 as P, verify_drand_v2 as vd
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
attempt("1 forged event (coherent digest, invented provenance)", {"mutate": forge}, "TRACK 2(a): authenticate_event → FORGED (see below)")
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
import beacon_record_drand_v22 as BD
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
# 9c–9h: track 2(b) v2 — the remote is a LOCAL BARE repository with non-fast-forward receives denied (labelled stand-in for the protected branch)
tb = Path(tempfile.mkdtemp()); bare = tb / "remote.git"; w = tb / "w"; subprocess.run(["git", "init", "-q", "--bare", str(bare)], check=True); git(bare, "config", "receive.denyNonFastforwards", "true")
subprocess.run(["git", "clone", "-q", str(bare), str(w)], check=True, capture_output=True); git(w, "config", "user.email", "t@t"); git(w, "config", "user.name", "t"); (w / "s").write_text("x"); git(w, "add", "s"); git(w, "commit", "-q", "-m", "i"); git(w, "push", "-q", "-u", "origin", "HEAD:refs/heads/main")
log = w / "collection_log.jsonl"; H.genesis(log, "a" * 64, "t", "b" * 64, 1); git(w, "add", log.name); git(w, "commit", "-q", "-m", "history-open"); oc = git(w, "rev-parse", "HEAD"); git(w, "push", "-q", "origin", "HEAD:refs/heads/main")
H.append(log, {"stage": "collector-collect", "outcome": "RETRY"}); git(w, "commit", "-q", "-am", "retry"); git(w, "push", "-q", "origin", "HEAD:refs/heads/main")
def vc(): ok, why, _ = P.validate_continuation_v2(w, log.name, oc, str(bare), "refs/heads/main"); return "OK" if ok else "REFUSED " + why.split(":")[0]
rows.append(("9c track 2(b) v2 validate_continuation_v2(genuine, every entry pushed)", vc(), "asks the remote (ls-remote)"))
H.append(log, {"stage": "builder-accept", "record_sha256": "c" * 64, "outcome": "ACCEPT-DRAND", "seed_hex": "d" * 64}); rows.append(("9d track 2(b) v2: codex counterexample 1 — ACCEPT appended, NOT pushed", vc(), "v1 said True"))
git(w, "commit", "-q", "-am", "accept unpushed"); rows.append(("9e track 2(b) v2: committed but NOT acknowledged by the remote", vc(), ""))
git(w, "reset", "-q", "--hard", oc); H.append(log, {"stage": "builder-accept", "record_sha256": "c" * 64, "outcome": "ACCEPT-DRAND", "seed_hex": "d" * 64}); git(w, "commit", "-q", "-am", "replacement"); rows.append(("9f track 2(b) v2: codex counterexample 2 — local reset to history-open, RETRY replaced by ACCEPT, remote unchanged", vc(), "v1 said True"))
r = subprocess.run(["git", "push", "-q", "origin", "HEAD:refs/heads/main"], cwd=w, capture_output=True); rows.append(("9g track 2(b) v2: the rewrite pushed to the protected remote", ("push REJECTED (non-fast-forward); " if r.returncode else "push accepted?!; ") + vc(), ""))
rows.append(("9h track 2(b) v2: remote unreachable", "REFUSED " + P.validate_continuation_v2(w, log.name, oc, str(bare) + ".missing", "refs/heads/main")[1].split(":")[0], "RETRY, never a pass"))
print("| attack | staged V22 candidate (driver v6 / verdict v22) | note |"); print("|---|---|---|")
for n, r, note in rows: print(f"| {n} | {r} | {note} |")
