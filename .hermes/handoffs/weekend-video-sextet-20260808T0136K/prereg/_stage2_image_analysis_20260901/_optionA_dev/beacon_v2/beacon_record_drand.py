#!/usr/bin/env python3
"""THE ONE VERDICT — DRAND-ONLY (option A V20 draft, 2026-09-06; source decision by Duho via codex voice ~19:02 KST, "해").
THE PROPERTY, now trivially true: the seed for the fixed round R = round_for(T_pulse) is the chain's threshold BLS signature over a fixed
message, unique for R, unpredictable before R's scheduled time, and verifiable by anyone under the pinned public key. It is a function of
(R, public key) alone. Relays only TRANSPORT it: any relay's bytes either verify (then they are THE value) or fail. Collection time changes
nothing; unavailability is RETRY, never a different value. NIST is not consulted; there is no source choice and no fallback.
Record (BEACON-RECORD-4): inputs (T_sign, T_pulse, round, rule digest, statement bytes) + EVIDENCE BYTES (each pinned relay's raw body from
the chain-hash-qualified path) — no stored verdict. verdict() recomputes from bytes: clock first; MIN_T_SIGN and EXCLUDED_T_PULSE as in V19;
>= 2 pinned relays' bodies present, each BLS-verifying under the pinned key for the expected round with randomness = SHA-256(signature) and all
agreeing; with fetch given, a live re-fetch of each relay must equal the retained body (or be unavailable — then that relay is not counted
live; live quorum >= 2 required). Outcomes: ACCEPT-DRAND | RETRY | REFUSE-<token>. Every attempt is appended to --log by the CLI."""
import json, hashlib, base64, sys
from datetime import datetime, timezone, timedelta
from pathlib import Path
HERE = Path(__file__).resolve().parent; sys.path.insert(0, str(HERE)); sys.path.insert(0, str(HERE.parent / "drand_only"))
import verify_drand as vd

DELAY_S = 600
MIN_T_SIGN = "2026-09-06T02:20:00Z"                      # V16–V19 floor, kept: any earlier T_sign refused
EXCLUDED_T_PULSE = ("2026-09-06T00:15:00Z",)             # the public 00:15Z pulse/round, refused by name
EXCLUDED_ROUNDS = (6440756, 6441924)                      # 00:15Z's round and the exhibit's historical round: never a study seed
MIN_HOSTS = 2
def parse_utc(s): return datetime.strptime(s, "%Y-%m-%dT%H:%M:%SZ").replace(tzinfo=timezone.utc)
def fmt(t): return t.strftime("%Y-%m-%dT%H:%M:%SZ")
def pulse_time(t_sign): return vd.pulse_time(t_sign)
def b64(b): return base64.b64encode(b).decode()
def unb64(s): return base64.b64decode(s)

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

def _verify_bodies(bodies, rnd):
    """bodies: {url: bytes}. Returns (accepted_urls, randomness or None, per-url checks)."""
    checks = {}; ok = {}
    for url, body in bodies.items():
        try: resp = json.loads(body)
        except Exception as e: checks[url] = {"error": "not JSON: " + repr(e)[:60], "accepted": False}; continue
        c = vd.verify(resp, rnd, url); checks[url] = c
        if c["accepted"]: ok[url] = c["seed_hex"]
    values = set(ok.values())
    return ok, (values.pop() if len(values) == 1 else None), checks

def verdict(rec, now, fetch=None, rule_sha256=None, statement_bytes=None):
    out = {"checks": {}}
    def refuse(tok, why): out.update(outcome=f"REFUSE-{tok}", seed_hex=None, source=None, why=why); return out
    if rec.get("schema") != "BEACON-RECORD-4" or rec.get("chain_hash") != vd.CHAIN_HASH or rec.get("public_key") != vd.PUBLIC_KEY_HEX: return refuse("SCHEMA", "not a BEACON-RECORD-4 for the pinned chain")
    try: t_sign = parse_utc(rec["T_sign"]); t_pulse = pulse_time(t_sign)
    except Exception as e: return refuse("T-SIGN", repr(e)[:80])
    if rec.get("T_pulse") != fmt(t_pulse) or rec.get("round") != vd.round_for(t_pulse): return refuse("T-PULSE", "T_pulse/round do not follow from T_sign")
    if t_sign < parse_utc(MIN_T_SIGN): return refuse("T-SIGN-PREDATES-AMENDMENT", f"before {MIN_T_SIGN}")
    if fmt(t_pulse) in EXCLUDED_T_PULSE or rec["round"] in EXCLUDED_ROUNDS: return refuse("T-PULSE-EXCLUDED", "public before any approval, or the exhibit's round")
    stmt = unb64(rec.get("statement_b64", ""))
    if rule_sha256 is not None and rec.get("rule_sha256") != rule_sha256: return refuse("RULE-DIGEST", "record names a different rule")
    if statement_bytes is not None and stmt != statement_bytes: return refuse("STATEMENT-BYTES", "statement differs from the retained approval record")
    if rec.get("rule_sha256", "").encode() not in stmt or rec["T_sign"].encode() not in stmt: return refuse("STATEMENT-BINDING", "statement lacks the rule digest or T_sign")
    if now < t_pulse: out.update(outcome="RETRY", seed_hex=None, source=None, why="verdict asked before T_pulse; never a seed"); return out
    rnd = rec["round"]
    retained = {u: unb64(r["body_b64"]) for u, r in rec.get("relays", {}).items() if "body_b64" in r}
    ok, seed, checks = _verify_bodies(retained, rnd); out["checks"]["retained"] = checks
    if len(ok) < MIN_HOSTS or seed is None: out.update(outcome="RETRY", seed_hex=None, source=None, why=f"fewer than {MIN_HOSTS} pinned relays verify for round {rnd} (or verified values disagree — impossible for a valid BLS signature); retry later"); return out
    if fetch is not None:
        live = _relay_bodies(fetch, rnd); live_ok = {}
        for u in ok:
            b = live.get(u, {}).get("body")
            if b is not None:
                if b != retained[u]:
                    c = vd.verify(json.loads(b), rnd, u) if b[:1] == b"{" else {"accepted": False}
                    if c.get("accepted"): return refuse("LIVE-DIFFERS-BUT-VERIFIES", "a relay now serves different bytes that ALSO verify — impossible for a deterministic BLS signature; investigate")
                    continue                                   # a relay now serving garbage is not counted live
                live_ok[u] = True
        out["checks"]["live_equal"] = sorted(live_ok)
        if len(live_ok) < MIN_HOSTS: out.update(outcome="RETRY", seed_hex=None, source=None, why="fewer than 2 pinned relays confirm the retained bytes live; retry later — the value cannot change"); return out
    out.update(outcome="ACCEPT-DRAND", seed_hex=seed, source="drand-mainnet-default", round=rnd, t_pulse=fmt(t_pulse), verified_relays=sorted(ok)); return out

def main(argv=None):
    import argparse, urllib.request
    def fetch(url, timeout=30):
        with urllib.request.urlopen(url, timeout=timeout) as r: return r.read()
    ap = argparse.ArgumentParser(); sub = ap.add_subparsers(dest="mode", required=True)
    c = sub.add_parser("collect"); c.add_argument("--t-sign", required=True); c.add_argument("--rule-sha256", required=True); c.add_argument("--signature-statement", required=True); c.add_argument("--out", required=True); c.add_argument("--log", required=True)
    v = sub.add_parser("verify"); v.add_argument("--record", required=True); v.add_argument("--rule-sha256", required=True); v.add_argument("--signature-statement", required=True); v.add_argument("--no-live", action="store_true"); v.add_argument("--log", required=True)
    a = ap.parse_args(argv); now = datetime.now(timezone.utc)
    def log(stage, rec_bytes, r):                       # MANDATORY (V20): every attempt, in order
        with open(a.log, "a") as fh: fh.write(json.dumps({"utc": fmt(now), "stage": stage, "record_sha256": hashlib.sha256(rec_bytes).hexdigest(), "outcome": r["outcome"], "source": r.get("source"), "seed_hex": r.get("seed_hex"), "why": r.get("why")}, sort_keys=True) + "\n")
    try:
        if a.mode == "collect":
            stmt = Path(a.signature_statement).read_bytes(); rec = collect(fetch, a.t_sign, a.rule_sha256, stmt, now)
            Path(a.out).write_text(json.dumps(rec, indent=1, sort_keys=True)); r = verdict(rec, now); log("collector-collect", Path(a.out).read_bytes(), r)
            print(json.dumps({"outcome": r["outcome"], "seed_hex": r.get("seed_hex"), "round": r.get("round")})); return 0 if r["outcome"].startswith("ACCEPT") else (4 if r["outcome"] == "RETRY" else 2)
        rec = json.loads(Path(a.record).read_text()); stmt = Path(a.signature_statement).read_bytes(); r = verdict(rec, now, fetch=None if a.no_live else fetch, rule_sha256=a.rule_sha256, statement_bytes=stmt); log("collector-verify", Path(a.record).read_bytes(), r)
        print(json.dumps({"outcome": r["outcome"], "seed_hex": r.get("seed_hex"), "round": r.get("round"), "why": r.get("why")})); return 0 if r["outcome"].startswith("ACCEPT") else 2
    except SystemExit as e:
        with open(a.log, "a") as fh: fh.write(json.dumps({"utc": fmt(now), "stage": "collector-refusal", "refusal": str(e)}, sort_keys=True) + "\n")
        raise
    except Exception as e:                              # V20: pre-parse and I/O failures reach the log too (V19 audit M2), then refuse
        with open(a.log, "a") as fh: fh.write(json.dumps({"utc": fmt(now), "stage": "collector-error", "error": repr(e)[:160]}, sort_keys=True) + "\n")
        raise SystemExit(f"COLLECTOR-ERROR: {repr(e)[:120]}")
if __name__ == "__main__": sys.exit(main())
