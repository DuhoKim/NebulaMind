#!/usr/bin/env python3
"""EXHIBIT (option A V20, drand-only): the seed is a function of (round, pinned public key) — INCLUDING the first-collection case that refuted V19.
Archive = the real public round 6441924 (BLS-verified). (A) two FIRST collections at different wall-clock times → same record round, same verified seed;
(B) a first collection while three relays are down and one serves garbage → RETRY (no seed); a later first collection with relays up → the SAME
seed as in (A): unavailability can only delay, never redirect; (C) a relay that later serves different bytes cannot produce a different verified
value (BLS signatures for a round are deterministic) → REFUSE-LIVE-DIFFERS-BUT-VERIFIES only if it verified, else ignored; (D) verify at +1 min and +30 days: identical.
The exhibit-round exclusion is lifted here ONLY; it is never a study seed. Deterministic output; digest filed."""
import json, hashlib, sys
from datetime import timedelta
from pathlib import Path
HERE = Path(__file__).resolve().parent; sys.path.insert(0, str(HERE)); sys.path.insert(0, str(HERE.parent / "drand_only"))
import beacon_record_drand as BD, verify_drand as vd
ROUND = 6441924; REAL = json.loads((HERE.parent / "drand_only" / "round_6441924_api.drand.sh.json").read_text()); BODY = json.dumps(REAL).encode()
TP = vd.round_time(ROUND); TS = BD.fmt(TP - timedelta(seconds=600)); D = "b" * 64; STMT = f"V20 {D} {TS}".encode()
def relays(down=(), garbage=()):
    def fetch(url, timeout=30):
        for host in vd.RELAYS:
            if url == vd.round_url(host, ROUND):
                if host in down: raise OSError("down")
                return b"garbage" if host in garbage else BODY
        raise OSError("404")
    return fetch
def strip(r): return {k: r.get(k) for k in ("outcome", "seed_hex", "round", "why")}
def run():
    saved = BD.EXCLUDED_ROUNDS; BD.EXCLUDED_ROUNDS = (6440756,); out = {}
    try:
        n = relays(); r1 = BD.collect(n, TS, D, STMT, now=TP + timedelta(minutes=1)); r2 = BD.collect(n, TS, D, STMT, now=TP + timedelta(days=30))
        v1 = strip(BD.verdict(r1, TP + timedelta(minutes=1), fetch=n, rule_sha256=D, statement_bytes=STMT)); v2 = strip(BD.verdict(r2, TP + timedelta(days=30), fetch=n, rule_sha256=D, statement_bytes=STMT))
        out["A_two_first_collections_at_different_times"] = {"first": v1, "second": v2, "same_seed": v1["seed_hex"] == v2["seed_hex"] == REAL["randomness"]}
        bad = relays(down=("https://api2.drand.sh", "https://api3.drand.sh", "https://drand.cloudflare.com"), garbage=("https://api.drand.sh",)); rb = BD.collect(bad, TS, D, STMT, now=TP + timedelta(minutes=1))
        vb = strip(BD.verdict(rb, TP + timedelta(minutes=1), fetch=bad, rule_sha256=D, statement_bytes=STMT)); rl = BD.collect(n, TS, D, STMT, now=TP + timedelta(hours=6)); vl = strip(BD.verdict(rl, TP + timedelta(hours=6), fetch=n, rule_sha256=D, statement_bytes=STMT))
        out["B_bad_first_collection_then_good"] = {"first": vb, "later": vl, "first_is_retry_no_seed": vb["outcome"] == "RETRY" and vb["seed_hex"] is None, "later_seed_equals_A": vl["seed_hex"] == v1["seed_hex"]}
        alt = dict(REAL); alt["extra"] = 1; va = strip(BD.verdict(r1, TP + timedelta(minutes=2), fetch=relays() if False else (lambda url, timeout=30: json.dumps(alt).encode() if "/public/" in url else (_ for _ in ()).throw(OSError())), rule_sha256=D, statement_bytes=STMT))
        out["C_relay_serves_different_bytes_that_still_verify"] = va
        t = dict(REAL); t["signature"] = REAL["signature"][:-2] + "00"; vt = strip(BD.verdict(r1, TP + timedelta(minutes=2), fetch=relays() if False else (lambda url, timeout=30: json.dumps(t).encode() if "/public/" in url else (_ for _ in ()).throw(OSError())), rule_sha256=D, statement_bytes=STMT))
        out["C_relay_serves_tampered_bytes_live"] = vt
        out["D_verify_same_record_twice"] = strip(BD.verdict(r1, TP + timedelta(minutes=1), rule_sha256=D, statement_bytes=STMT)) == strip(BD.verdict(r1, TP + timedelta(days=365), rule_sha256=D, statement_bytes=STMT))
        out["pinned"] = {"round": ROUND, "chain_hash": vd.CHAIN_HASH, "public_key": vd.PUBLIC_KEY_HEX, "seed": REAL["randomness"]}
    finally: BD.EXCLUDED_ROUNDS = saved
    return out
if __name__ == "__main__":
    res = run(); text = json.dumps(res, indent=1, sort_keys=True) + "\n"; print(text)
    ok = res["A_two_first_collections_at_different_times"]["same_seed"] and res["B_bad_first_collection_then_good"]["first_is_retry_no_seed"] and res["B_bad_first_collection_then_good"]["later_seed_equals_A"] and res["C_relay_serves_different_bytes_that_still_verify"]["outcome"] == "REFUSE-LIVE-DIFFERS-BUT-VERIFIES" and res["C_relay_serves_tampered_bytes_live"]["outcome"] == "RETRY" and res["D_verify_same_record_twice"]
    print("EXHIBIT OK:", ok); print("EXHIBIT-DIGEST:", hashlib.sha256(text.encode()).hexdigest())
