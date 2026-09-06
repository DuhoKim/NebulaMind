#!/usr/bin/env python3
"""THE ONE VERDICT — EXPEDITED (option A V16 draft, 2026-09-06; Duho, via codex voice, confirmed in chat 2026-09-06 11:08 KST).
IDENTICAL to beacon_record.py (V15, pinned) except: FALLBACK_AFTER_H = 0 (the drand fallback is permitted from T_pulse itself, not
T_pulse + 24 h); MIN_T_SIGN (a T_sign earlier than this amendment's drafting is refused — signature first, seed second, visibly); and
EXCLUDED_T_PULSE (the already-public 2026-09-06T00:15:00Z pulse — NIST 1928801 / drand round 6440756 — is INELIGIBLE by name).
ORIGINAL TEXT OF THE PINNED MODULE FOLLOWS.
THE ONE VERDICT (rebuilt once, 2026-09-06). A beacon record holds INPUTS (T_sign, rule digest, the retained signature statement) and
EVIDENCE BYTES (NIST pulse/leaf/chain/next; drand relay bodies) — nothing else. `verdict(record, now, roots, fetch=None)` recomputes the
outcome from evidence and the clock; the fetcher that creates a record and the identity builder that consumes it call this SAME function.
With `fetch` given, every piece of evidence is also RE-FETCHED live and must equal the retained bytes (the builder's provenance check —
the only proof available that a record's bytes are what the public sources serve).
Outcomes: ACCEPT-NIST | ACCEPT-DRAND | RETRY (no seed yet) | UNAVAILABLE (fallback also failed) | REFUSE-<token> (record itself invalid).
Rule (V17): T_pulse = first whole minute >= T_sign + 600 s. A verdict asked before T_pulse is RETRY, first of all. NIST is binding
whenever its pulse authenticates AND (with fetch) the live re-fetch EQUALS the retained bytes; a live re-fetch that raises is RETRY —
never a seed and never evidence of NIST failure. From T_pulse itself (FALLBACK_AFTER_H = 0): drand round_for(T_pulse) is used ONLY if the
primary is not authenticable at the time of the verdict (recomputed live, not recorded) AND >= 2 pinned hosts agree retained and live. VOID: if NIST later serves an
authenticable T_pulse pulse, any fallback identity is void (a later verdict with fetch would say ACCEPT-NIST, not ACCEPT-DRAND)."""
import json, hashlib, re, base64, urllib.error
from datetime import datetime, timezone, timedelta
from pathlib import Path
import sys; sys.path.insert(0, str(Path(__file__).resolve().parent))
import nist_pulse, drand_round

DELAY_S = 600; FALLBACK_AFTER_H = 0
MIN_T_SIGN = "2026-09-06T02:20:00Z"                      # this amendment was drafted before this instant; any earlier T_sign is refused
EXCLUDED_T_PULSE = ("2026-09-06T00:15:00Z",)             # public before any V16 signature: NIST pulse 1928801, drand round 6440756
def parse_utc(s): return datetime.strptime(s, "%Y-%m-%dT%H:%M:%SZ").replace(tzinfo=timezone.utc)
def fmt(t): return t.strftime("%Y-%m-%dT%H:%M:%SZ")
def pulse_time(t_sign):
    t = t_sign + timedelta(seconds=DELAY_S)
    if t.second or t.microsecond: t = (t + timedelta(minutes=1)).replace(second=0, microsecond=0)
    return t
def b64(b): return base64.b64encode(b).decode()
def unb64(s): return base64.b64decode(s)

def collect(fetch, t_sign_str, rule_sha256, statement_bytes, now):
    """Build a record: inputs + evidence bytes. Refuses to run before T_pulse (signature first, beacon second)."""
    t_sign = parse_utc(t_sign_str); t_pulse = pulse_time(t_sign)
    if t_sign < parse_utc(MIN_T_SIGN): raise SystemExit(f"T-SIGN-PREDATES-AMENDMENT: T_sign {t_sign_str} is before the amendment was drafted ({MIN_T_SIGN})")
    if fmt(t_pulse) in EXCLUDED_T_PULSE: raise SystemExit(f"T-PULSE-EXCLUDED: {fmt(t_pulse)} was public before any V16 signature")
    if now < t_pulse: raise SystemExit(f"BEACON-NOT-YET: T_pulse {fmt(t_pulse)} is in the future")
    if rule_sha256.encode() not in statement_bytes or t_sign_str.encode() not in statement_bytes: raise SystemExit("STATEMENT-DOES-NOT-BIND: the statement must contain the rule digest and T_sign")
    rec = {"schema": "BEACON-RECORD-3", "T_sign": t_sign_str, "T_pulse": fmt(t_pulse), "rule_sha256": rule_sha256, "statement_b64": b64(statement_bytes), "collected_utc": fmt(now), "nist": {}, "drand": {}}
    try:
        ev = nist_pulse.collect(fetch, t_pulse); rec["nist"] = {"pulse_body_b64": b64(ev["pulse_body"]), "leaf_pem_b64": b64(ev["leaf_pem"]), "intermediate_pems_b64": [b64(b) for b in ev["intermediate_pems"]], "next_body_b64": b64(ev["next_body"])}
    except urllib.error.HTTPError as e: rec["nist"] = {"http_error": e.code}
    except Exception as e: rec["nist"] = {"error": repr(e)[:160]}
    if now >= t_pulse + timedelta(hours=FALLBACK_AFTER_H):
        rnd = drand_round.round_for(t_pulse); dev = drand_round.collect(fetch, rnd)
        rec["drand"] = {"round": rnd, "relays": {u: ({"body_b64": b64(r["body"])} if "body" in r else {"error": r["error"]}) for u, r in dev.items()}}
    return rec

def _nist_evidence(rec):
    n = rec.get("nist", {})
    if not all(k in n for k in ("pulse_body_b64", "leaf_pem_b64", "intermediate_pems_b64", "next_body_b64")): return None
    return {"pulse_body": unb64(n["pulse_body_b64"]), "leaf_pem": unb64(n["leaf_pem_b64"]), "intermediate_pems": [unb64(x) for x in n["intermediate_pems_b64"]], "next_body": unb64(n["next_body_b64"])}
def _drand_evidence(rec):
    d = rec.get("drand", {}); return {u: ({"body": unb64(r["body_b64"])} if "body_b64" in r else {"error": r.get("error")}) for u, r in d.get("relays", {}).items()}, d.get("round")

def verdict(rec, now, roots, fetch=None, rule_sha256=None, statement_bytes=None):
    """Recompute everything. Returns {'outcome', 'seed_hex', 'source', 'checks'}. Never trusts a stored result (none exist)."""
    out = {"checks": {}}
    def refuse(tok, why): out.update(outcome=f"REFUSE-{tok}", seed_hex=None, source=None, why=why); return out
    if rec.get("schema") != "BEACON-RECORD-3": return refuse("SCHEMA", "not a BEACON-RECORD-3")
    try: t_sign = parse_utc(rec["T_sign"]); t_pulse = pulse_time(t_sign)
    except Exception as e: return refuse("T-SIGN", repr(e)[:80])
    if rec.get("T_pulse") != fmt(t_pulse): return refuse("T-PULSE", "T_pulse does not follow from T_sign")
    if t_sign < parse_utc(MIN_T_SIGN): return refuse("T-SIGN-PREDATES-AMENDMENT", f"T_sign before {MIN_T_SIGN}")
    if fmt(t_pulse) in EXCLUDED_T_PULSE: return refuse("T-PULSE-EXCLUDED", "this pulse was public before any V16 signature")
    stmt = unb64(rec.get("statement_b64", ""))
    if rule_sha256 is not None and rec.get("rule_sha256") != rule_sha256: return refuse("RULE-DIGEST", "record names a different rule")
    if statement_bytes is not None and stmt != statement_bytes: return refuse("STATEMENT-BYTES", "record's statement differs from the retained relay")
    if rec.get("rule_sha256", "").encode() not in stmt or rec["T_sign"].encode() not in stmt: return refuse("STATEMENT-BINDING", "statement lacks the rule digest or T_sign")
    if now < t_pulse: out.update(outcome="RETRY", seed_hex=None, source=None, why="verdict asked before T_pulse; never a seed"); return out   # V17: clock FIRST (codex V16 FATAL 1b)
    ev = _nist_evidence(rec); nist_ok = False; live_ok = (fetch is None)
    if ev is not None:
        c = nist_pulse.authenticate(ev, t_pulse, roots); out["checks"]["nist"] = c
        if fetch is not None:
            try:
                live = nist_pulse.collect(fetch, t_pulse)
                same = (live["pulse_body"] == ev["pulse_body"] and live["leaf_pem"] == ev["leaf_pem"] and live["next_body"] == ev["next_body"]
                        and list(live["intermediate_pems"]) == list(ev["intermediate_pems"]))     # every retained public input, the issuer chain included (codex, V14 gate)
                out["checks"]["nist_live_equal"] = same; live_ok = same
                if not same:
                    lc = nist_pulse.authenticate(live, t_pulse, roots); out["checks"]["nist_live_authenticates"] = lc["accepted"]
                    if lc["accepted"]: return refuse("NIST-LIVE-DIFFERS", "NIST now serves an authenticable pulse different from the retained one")
                    return refuse("NIST-LIVE-DIFFERS", "retained NIST evidence differs from what NIST serves now")
            except urllib.error.HTTPError as e: out["checks"]["nist_live_http"] = e.code; live_ok = False
            except Exception as e:
                out["checks"]["nist_live_error"] = repr(e)[:120]
                out.update(outcome="RETRY", seed_hex=None, source=None, why="live re-fetch of the NIST pulse raised; the primary's status cannot be established now — never a seed"); return out   # V17 (codex V16 FATAL 1a)
        nist_ok = c["accepted"] and live_ok
    if nist_ok: out.update(outcome="ACCEPT-NIST", seed_hex=out["checks"]["nist"]["seed_hex"], source="NIST-beacon-2.0", t_pulse=fmt(t_pulse)); return out
    # primary not accepted: RETRY before the fallback time
    if now < t_pulse + timedelta(hours=FALLBACK_AFTER_H): out.update(outcome="RETRY", seed_hex=None, source=None, why="primary not authenticable/retrievable yet; fallback not permitted before T_pulse"); return out
    # V17: from T_pulse itself, primary still not authenticable NOW — with fetch, re-check live; a live authenticable primary is binding (VOID)
    if fetch is not None:
        try:
            live = nist_pulse.collect(fetch, t_pulse); lc = nist_pulse.authenticate(live, t_pulse, roots); out["checks"]["nist_live_now"] = lc["accepted"]
            if lc["accepted"]: return refuse("DRAND-VOID-PRIMARY-AUTHENTICABLE", "NIST now serves an authenticable T_pulse pulse: the primary is binding")
        except urllib.error.HTTPError as e: out["checks"]["nist_live_now_http"] = e.code          # an HTTP error IS a public answer (pulse absent/unauthenticable)
        except Exception as e:
            out["checks"]["nist_live_now_error"] = repr(e)[:120]
            out.update(outcome="RETRY", seed_hex=None, source=None, why="live NIST re-check raised; a local failure is not a public NIST failure — never a seed"); return out   # V17 (codex V16 item 1)
    dev, rnd = _drand_evidence(rec); exp = drand_round.round_for(t_pulse)
    if rnd != exp or not dev: out.update(outcome="UNAVAILABLE", seed_hex=None, source=None, why=f"no fallback evidence for round {exp}"); return out
    ag = drand_round.agreement(dev, exp); out["checks"]["drand"] = ag
    if fetch is not None:
        live = drand_round.agreement(drand_round.collect(fetch, exp), exp); out["checks"]["drand_live"] = live
        if not (live["accepted"] and live["randomness"] == ag["randomness"]): out.update(outcome="UNAVAILABLE", seed_hex=None, source=None, why="pinned relays do not currently confirm the retained randomness"); return out
    if ag["accepted"]: out.update(outcome="ACCEPT-DRAND", seed_hex=ag["randomness"], source="drand-mainnet-default", round=exp, t_pulse=fmt(t_pulse)); return out
    out.update(outcome="UNAVAILABLE", seed_hex=None, source=None, why=f"fewer than {drand_round.MIN_HOSTS} pinned hosts agree"); return out

def main(argv=None):
    import argparse, urllib.request
    def fetch(url, timeout=30):
        with urllib.request.urlopen(url, timeout=timeout) as r: return r.read()
    ap = argparse.ArgumentParser(); sub = ap.add_subparsers(dest="mode", required=True)
    c = sub.add_parser("collect"); c.add_argument("--t-sign", required=True); c.add_argument("--rule-sha256", required=True); c.add_argument("--signature-statement", required=True); c.add_argument("--out", required=True)
    v = sub.add_parser("verify"); v.add_argument("--record", required=True); v.add_argument("--rule-sha256", required=True); v.add_argument("--signature-statement", required=True); v.add_argument("--no-live", action="store_true")
    a = ap.parse_args(argv); now = datetime.now(timezone.utc); roots = nist_pulse.pinned_roots()
    if a.mode == "collect":
        stmt = Path(a.signature_statement).read_bytes(); rec = collect(fetch, a.t_sign, a.rule_sha256, stmt, now)
        Path(a.out).write_text(json.dumps(rec, indent=1, sort_keys=True)); r = verdict(rec, now, roots)
        print(json.dumps({"outcome": r["outcome"], "seed_hex": r.get("seed_hex"), "source": r.get("source")})); return 0 if r["outcome"].startswith("ACCEPT") else (4 if r["outcome"] == "RETRY" else 2)
    rec = json.loads(Path(a.record).read_text()); stmt = Path(a.signature_statement).read_bytes(); r = verdict(rec, now, roots, fetch=None if a.no_live else fetch, rule_sha256=a.rule_sha256, statement_bytes=stmt)
    print(json.dumps({"outcome": r["outcome"], "seed_hex": r.get("seed_hex"), "source": r.get("source"), "why": r.get("why")})); return 0 if r["outcome"].startswith("ACCEPT") else 2
if __name__ == "__main__": sys.exit(main())
