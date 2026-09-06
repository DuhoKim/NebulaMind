#!/usr/bin/env python3
"""THE ONE VERDICT — DRAND-ONLY, V24 STAGED CANDIDATE (codex V23 M2: outer refusal/error entries are PUBLISHED too; before any operation the collector RECONCILES a pending entry with the remote — provenance_designs_v4.reconcile_pending — and stops on PUBLISH-BATCH/PENDING-PUSH). V23 was — V23 STAGED CANDIDATE (codex V22 B: the collector PUBLISHES each history entry — the genesis as the history-open commit, then every attempt — and requires the remote's acknowledgment before it proceeds, when --publish-remote/--publish-ref are given; production composed mode gives them). V22 was — V22 STAGED CANDIDATE (track 1 of Blanc's 20:45 order; NOT GATED, NOT ADOPTED). V22 = V21 + (codex V21 C6) signature
equality on DECODED bytes, never on hex text; (C5) ALL THREE historical rounds excluded by name — 6440756, 6441904, 6441924; (C4) argparse failures
disclosed (sidecar named by --log, else the module sidecar ARGPARSE_SIDECAR); the seed is lowercase hex SHA-256 of the decoded signature bytes
(verify_drand_v2 computes it so). V21 bytes preserved in beacon_record_drand_v21.py. V21 was: (option A V21 draft, 2026-09-06; source decision by Duho via codex voice ~19:02 KST, "해"). V20 bytes preserved in beacon_record_drand.py.
THE PROPERTY, stated exactly (codex V20 item X): the SEED for the fixed round R = round_for(T_pulse) is unique — it is SHA-256 of the chain's
threshold BLS signature over a fixed message, a function of (R, public key) alone, unpredictable before R's scheduled time and verifiable by
anyone under the pinned key. The BYTES a relay serves are NOT unique: different HTTP encodings (key order, whitespace, extra fields) can carry
the same signature. So: a live body whose signature equals the retained one is the SAME value however encoded (counted live-confirmed,
the representation difference recorded); a live body with a DIFFERENT signature that also verifies under the pinned key for R would
contradict signature uniqueness under one key — REFUSE-CONFLICTING-VALID-SIGNATURES (investigate the key, not the relay); a live body that
does not verify is transport noise (not counted live). Relays only TRANSPORT; collection time changes nothing; unavailability is RETRY.
Record (BEACON-RECORD-4): inputs (T_sign, T_pulse, round, rule digest, statement bytes) + EVIDENCE BYTES (each pinned relay's raw body from
the chain-hash-qualified path, keyed by the EXACT pinned URL) — no stored verdict. verdict() recomputes from bytes: schema/chain, T_pulse/round
from T_sign, MIN_T_SIGN, EXCLUDED_T_PULSE/EXCLUDED_ROUNDS, rule/statement bindings, clock first, >= 2 DISTINCT pinned URLs whose bodies
BLS-verify for R with randomness = SHA-256(signature) and agree; with fetch given, live quorum >= 2 as above. Outcomes: ACCEPT-DRAND | RETRY |
REFUSE-<token>. LOGGING (codex V20 M2): the CLI writes to the AUTHENTICATED HISTORY (corpus_identity/history.py): the first collect creates
the GENESIS anchored to SHA-256(approval record bytes), T_pulse, rule digest and round; every later attempt is a hash-chained entry; a failure
before the genesis inputs exist is written to <log>.pregenesis.jsonl (disclosed, outside the chain)."""
import json, hashlib, base64, sys
from datetime import datetime, timezone, timedelta
from pathlib import Path
HERE = Path(__file__).resolve().parent; sys.path.insert(0, str(HERE)); sys.path.insert(0, str(HERE.parent / "drand_only")); sys.path.insert(0, str(HERE.parent / "corpus_identity"))
import verify_drand_v2 as vd
import history_v2 as H

DELAY_S = 600
MIN_T_SIGN = "2026-09-06T02:20:00Z"                      # V16–V20 floor, kept: any earlier T_sign refused
EXCLUDED_T_PULSE = ("2026-09-06T00:15:00Z",)             # the public 00:15Z pulse/round, refused by name
EXCLUDED_ROUNDS = (6440756, 6441904, 6441924)             # 00:15Z's round, the nonce-fixture round, the exhibit round: never a study seed (V22, codex V21 C5)
ARGPARSE_SIDECAR = HERE / "collector_argparse_failures.jsonl"   # V22: argument failures with no --log are disclosed here
MIN_HOSTS = 2
def parse_utc(s): return datetime.strptime(s, "%Y-%m-%dT%H:%M:%SZ").replace(tzinfo=timezone.utc)
def fmt(t): return t.strftime("%Y-%m-%dT%H:%M:%SZ")
def pulse_time(t_sign): return vd.pulse_time(t_sign)
def b64(b): return base64.b64encode(b).decode()
def unb64(s): return base64.b64decode(s)
def pinned_urls(rnd): return {vd.round_url(h, rnd) for h in vd.RELAYS}

def _relay_bodies(fetch, rnd):
    out = {}
    for host in vd.RELAYS:
        url = vd.round_url(host, rnd)
        try: out[url] = {"body": fetch(url)}
        except Exception as e: out[url] = {"error": repr(e)[:120]}
    return out

def collect(fetch, t_sign_str, rule_sha256, statement_bytes, now):
    t_sign = parse_utc(t_sign_str); t_pulse = pulse_time(t_sign); rnd = vd.round_for(t_pulse)
    if t_sign < parse_utc(MIN_T_SIGN): raise SystemExit(f"T-SIGN-PREDATES-AMENDMENT: {t_sign_str} < {MIN_T_SIGN}")
    if fmt(t_pulse) in EXCLUDED_T_PULSE or rnd in EXCLUDED_ROUNDS: raise SystemExit(f"T-PULSE-EXCLUDED: {fmt(t_pulse)} / round {rnd} was public before any approval or is the exhibit's round")
    if now < t_pulse: raise SystemExit(f"BEACON-NOT-YET: T_pulse {fmt(t_pulse)} is in the future")
    if rule_sha256.encode() not in statement_bytes or t_sign_str.encode() not in statement_bytes: raise SystemExit("STATEMENT-DOES-NOT-BIND")
    rel = _relay_bodies(fetch, rnd)
    return {"schema": "BEACON-RECORD-4", "source": "drand-mainnet-default", "chain_hash": vd.CHAIN_HASH, "public_key": vd.PUBLIC_KEY_HEX, "T_sign": t_sign_str, "T_pulse": fmt(t_pulse), "round": rnd,
            "rule_sha256": rule_sha256, "statement_b64": b64(statement_bytes), "collected_utc": fmt(now),
            "relays": {u: ({"body_b64": b64(r["body"])} if "body" in r else {"error": r["error"]}) for u, r in rel.items()}}

def _parse_verify(body, rnd, url):
    """(checks, DECODED signature bytes or None). Any failure — not JSON, not a dict, verifier exception — is a non-verifying body, never an escape.
    V22: the signature is returned as bytes (bytes.fromhex), so equality below is canonical — upper/lower-case hex of one signature is one value."""
    try:
        resp = json.loads(body)
        if not isinstance(resp, dict): return {"error": "not a JSON object", "accepted": False}, None
        c = vd.verify(resp, rnd, url); return c, (bytes.fromhex(str(resp.get("signature"))) if c["accepted"] else None)
    except Exception as e: return {"error": "unverifiable body: " + repr(e)[:60], "accepted": False}, None

def _verify_bodies(bodies, rnd):
    """bodies: {url: bytes}. Only EXACT pinned URLs are considered (V21: distinct pinned relays counted by URL). Returns (accepted {url: seed}, seed or None, checks, {url: signature})."""
    checks = {}; ok = {}; sigs = {}; P = pinned_urls(rnd)
    for url, body in bodies.items():
        if url not in P: checks[url] = {"error": "not a pinned chain-hash-qualified URL", "accepted": False}; continue
        c, sig = _parse_verify(body, rnd, url); checks[url] = c
        if c["accepted"]: ok[url] = c["seed_hex"]; sigs[url] = sig
    values = set(ok.values())
    return ok, (values.pop() if len(values) == 1 else None), checks, sigs

def verdict(rec, now, fetch=None, rule_sha256=None, statement_bytes=None):
    out = {"checks": {}}
    def refuse(tok, why): out.update(outcome=f"REFUSE-{tok}", seed_hex=None, source=None, why=why); return out
    if not isinstance(rec, dict) or rec.get("schema") != "BEACON-RECORD-4" or rec.get("chain_hash") != vd.CHAIN_HASH or rec.get("public_key") != vd.PUBLIC_KEY_HEX: return refuse("SCHEMA", "not a BEACON-RECORD-4 for the pinned chain")
    try: t_sign = parse_utc(rec["T_sign"]); t_pulse = pulse_time(t_sign)
    except Exception as e: return refuse("T-SIGN", repr(e)[:80])
    if rec.get("T_pulse") != fmt(t_pulse) or rec.get("round") != vd.round_for(t_pulse): return refuse("T-PULSE", "T_pulse/round do not follow from T_sign")
    if t_sign < parse_utc(MIN_T_SIGN): return refuse("T-SIGN-PREDATES-AMENDMENT", f"before {MIN_T_SIGN}")
    if fmt(t_pulse) in EXCLUDED_T_PULSE or rec["round"] in EXCLUDED_ROUNDS: return refuse("T-PULSE-EXCLUDED", "public before any approval, or the exhibit's round")
    try: stmt = unb64(rec.get("statement_b64", ""))
    except Exception: return refuse("STATEMENT-BYTES", "statement_b64 does not decode")
    if rule_sha256 is not None and rec.get("rule_sha256") != rule_sha256: return refuse("RULE-DIGEST", "record names a different rule")
    if statement_bytes is not None and stmt != statement_bytes: return refuse("STATEMENT-BYTES", "statement differs from the retained approval record")
    if str(rec.get("rule_sha256", "")).encode() not in stmt or rec["T_sign"].encode() not in stmt: return refuse("STATEMENT-BINDING", "statement lacks the rule digest or T_sign")
    if now < t_pulse: out.update(outcome="RETRY", seed_hex=None, source=None, why="verdict asked before T_pulse; never a seed"); return out
    rnd = rec["round"]
    try: retained = {u: unb64(r["body_b64"]) for u, r in (rec.get("relays") or {}).items() if isinstance(r, dict) and "body_b64" in r}
    except Exception: return refuse("SCHEMA", "relay bodies do not decode")
    ok, seed, checks, sigs = _verify_bodies(retained, rnd); out["checks"]["retained"] = checks
    if len(ok) < MIN_HOSTS or seed is None: out.update(outcome="RETRY", seed_hex=None, source=None, why=f"fewer than {MIN_HOSTS} distinct pinned relays verify for round {rnd} (or verified values disagree); retry later"); return out
    sig = next(iter(sigs.values()))
    if fetch is not None:
        live = _relay_bodies(fetch, rnd); live_ok = {}; rep = {}
        for u in ok:
            b = live.get(u, {}).get("body")
            if b is None: continue                                        # unavailable live: not counted
            if b == retained[u]: live_ok[u] = True; continue
            c, lsig = _parse_verify(b, rnd, u)                             # different bytes: what VALUE do they carry?
            if not c.get("accepted"): continue                             # transport noise: not counted live
            if lsig == sig: live_ok[u] = True; rep[u] = "same signature bytes, different encoding"; continue
            return refuse("CONFLICTING-VALID-SIGNATURES", f"relay {u} serves DIFFERENT signature BYTES for round {rnd} that also verify under the pinned key — contradicts uniqueness under one key; investigate the key")
        out["checks"]["live_confirmed"] = sorted(live_ok); out["checks"]["live_representation_differs"] = rep
        if len(live_ok) < MIN_HOSTS: out.update(outcome="RETRY", seed_hex=None, source=None, why="fewer than 2 pinned relays confirm the retained VALUE live; retry later — the value cannot change"); return out
    out.update(outcome="ACCEPT-DRAND", seed_hex=seed, source="drand-mainnet-default", round=rnd, t_pulse=fmt(t_pulse), verified_relays=sorted(ok), signature=sig.hex()); return out

def main(argv=None):
    import argparse, urllib.request
    def fetch(url, timeout=30):
        with urllib.request.urlopen(url, timeout=timeout) as r: return r.read()
    ap = argparse.ArgumentParser(); sub = ap.add_subparsers(dest="mode", required=True)
    c = sub.add_parser("collect"); c.add_argument("--t-sign", required=True); c.add_argument("--rule-sha256", required=True); c.add_argument("--signature-statement", required=True); c.add_argument("--out", required=True); c.add_argument("--log", required=True); c.add_argument("--publish-remote", default=None); c.add_argument("--publish-ref", default=None)
    v = sub.add_parser("verify"); v.add_argument("--record", required=True); v.add_argument("--rule-sha256", required=True); v.add_argument("--signature-statement", required=True); v.add_argument("--no-live", action="store_true"); v.add_argument("--log", required=True); v.add_argument("--publish-remote", default=None); v.add_argument("--publish-ref", default=None)
    now = datetime.now(timezone.utc); av = list(sys.argv[1:] if argv is None else argv)
    logp = Path(av[av.index("--log") + 1]) if "--log" in av and av.index("--log") + 1 < len(av) else None      # V22: known before parsing, so a parse failure is disclosed
    def side(entry):                                     # pre-genesis failures: outside the chain, disclosed by name (or in the module sidecar when no --log was given)
        with open((str(logp) + ".pregenesis.jsonl") if logp else ARGPARSE_SIDECAR, "a") as fh: fh.write(json.dumps({"utc": fmt(now), **entry}, sort_keys=True) + "\n")
    try: a = ap.parse_args(av)
    except SystemExit as e:                              # V22 (codex V21 C4): argparse failures reach the sidecar
        side({"stage": "collector-args-refusal", "argv": av, "exit": str(e)}); raise
    logp = Path(a.log)
    def _pub():
        sys.path.insert(0, str(HERE.parent / "track2")); import provenance_designs_v4 as P, subprocess as sp
        root = sp.run(["git", "rev-parse", "--show-toplevel"], cwd=logp.parent, capture_output=True, text=True).stdout.strip()
        return P, root, logp.resolve().relative_to(Path(root).resolve()).as_posix()
    def publish(message):                            # v23 producer boundary (v24: also pushes an already-committed pending entry)
        if not (a.publish_remote and a.publish_ref): return
        P, root, rel = _pub(); P.publish_entry(root, rel, a.publish_remote, a.publish_ref, message)
    def reconcile():                                 # v24 (codex V23 M2): BEFORE any operation, a pending entry is published or the run refuses
        if not (a.publish_remote and a.publish_ref): return
        P, root, rel = _pub(); P.reconcile_pending(root, rel, a.publish_remote, a.publish_ref)
    def log(stage, rec_bytes, r):                       # MANDATORY: every attempt, hash-chained, in order, PUBLISHED when configured
        H.append(logp, {"stage": stage, "record_sha256": hashlib.sha256(rec_bytes).hexdigest(), "outcome": r["outcome"], "source": r.get("source"), "seed_hex": r.get("seed_hex"), "why": r.get("why")}); publish("history: " + stage)
    def ensure_genesis(stmt, t_sign_str):
        t_pulse = pulse_time(parse_utc(t_sign_str)); rnd = vd.round_for(t_pulse); d = hashlib.sha256(stmt).hexdigest()
        if not logp.is_file() or logp.stat().st_size == 0: H.genesis(logp, d, fmt(t_pulse), a.rule_sha256, rnd); publish("history-open"); return
        g = H.validate(logp)[0]
        if (g["approval_record_sha256"], g["t_pulse"], g["rule_sha256"], g["round"]) != (d, fmt(t_pulse), a.rule_sha256, rnd): raise SystemExit("HISTORY-GENESIS-MISMATCH: this history was initiated for a different approval record / T_pulse / rule / round")
    try:
        reconcile()
        stmt = Path(a.signature_statement).read_bytes()
        if a.mode == "collect":
            ensure_genesis(stmt, a.t_sign)
            try: rec = collect(fetch, a.t_sign, a.rule_sha256, stmt, now)
            except SystemExit as e: H.append(logp, {"stage": "collector-refusal", "refusal": str(e)}); publish("history: collector-refusal"); raise
            Path(a.out).write_text(json.dumps(rec, indent=1, sort_keys=True)); r = verdict(rec, now); log("collector-collect", Path(a.out).read_bytes(), r)
            print(json.dumps({"outcome": r["outcome"], "seed_hex": r.get("seed_hex"), "round": r.get("round")})); return 0 if r["outcome"].startswith("ACCEPT") else (4 if r["outcome"] == "RETRY" else 2)
        raw = Path(a.record).read_bytes(); rec = json.loads(raw); ensure_genesis(stmt, str(rec.get("T_sign")))
        r = verdict(rec, now, fetch=None if a.no_live else fetch, rule_sha256=a.rule_sha256, statement_bytes=stmt); log("collector-verify", raw, r)
        print(json.dumps({"outcome": r["outcome"], "seed_hex": r.get("seed_hex"), "round": r.get("round"), "why": r.get("why")})); return 0 if r["outcome"].startswith("ACCEPT") else 2
    except SystemExit as e:
        if logp.is_file() and logp.stat().st_size > 0 and not str(e).startswith(("HISTORY-", "PENDING-PUSH", "PUBLISH-BATCH")):
            try: H.append(logp, {"stage": "collector-refusal", "refusal": str(e)}); publish("history: collector-refusal")   # v24: published too
            except Exception as e2: side({"stage": "collector-refusal", "refusal": str(e), "history_error": repr(e2)[:120]})
        else: side({"stage": "collector-refusal", "refusal": str(e)})
        raise
    except BaseException as e:                          # EVERY other path: I/O, parse, interrupt — logged, then refused
        entry = {"stage": "collector-error", "error": repr(e)[:160]}
        if logp.is_file() and logp.stat().st_size > 0:
            try: H.append(logp, entry); publish("history: collector-error")                          # v24: the outer error is PUBLISHED too
            except Exception as e2: side({**entry, "history_error": repr(e2)[:120]})
        else: side(entry)
        raise SystemExit(f"COLLECTOR-ERROR: {repr(e)[:120]}")
if __name__ == "__main__": sys.exit(main())
