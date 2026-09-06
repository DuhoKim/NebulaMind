#!/usr/bin/env python3
"""EXHIBIT (option A V19): the source decision is a function of archived public bytes for T_pulse plus the pinned root — the SAME verdict
and the SAME seed at two different wall-clock times, from the same archived inputs. Two exhibits: (A) a synthetic record through the
three-tier test PKI with an archive-serving mock network (NIST served-unauthenticable, drand quorum) evaluated at T_pulse + 1 min and at
T_pulse + 30 days, with and without live re-fetch; (B) the REAL filed RETRY record of 2026-09-06T00:15:00Z (archived NIST bytes, no drand
evidence) evaluated at two times with the pinned production root and NO network — RETRY both times, identical. Deterministic output;
its digest is filed in the change record and reproduces on re-run."""
import json, hashlib, sys
from datetime import datetime, timezone, timedelta
from pathlib import Path
HERE = Path(__file__).resolve().parent; sys.path.insert(0, str(HERE))
import beacon_record_expedited as X, nist_pulse, drand_round, test_pki as pki

def strip(r): return {k: r.get(k) for k in ("outcome", "seed_hex", "source", "round", "t_pulse")}
def run():
    out = []
    T_SIGN = datetime(2026, 9, 6, 3, 0, 7, tzinfo=timezone.utc); TP = X.pulse_time(T_SIGN); D = "b" * 64; STMT = f"V19 {D} {X.fmt(T_SIGN)}".encode(); RND = drand_round.round_for(TP)
    n = pki.network(TP, sign=False, drand=(RND, "c" * 64))            # the archive: NIST serves an unauthenticable T_pulse pulse; four relays agree
    rec = X.collect(n, X.fmt(T_SIGN), D, STMT, now=TP + timedelta(minutes=1))
    times = [TP + timedelta(minutes=1), TP + timedelta(days=30)]
    for label, fetch in (("with live re-fetch from the archive", n), ("from retained bytes only", None)):
        vs = [strip(X.verdict(rec, t, pki.roots(), fetch=fetch, rule_sha256=D, statement_bytes=STMT)) for t in times]
        out.append({"exhibit": "A-synthetic", "mode": label, "times": [X.fmt(t) for t in times], "verdicts": vs, "identical": vs[0] == vs[1]})
    real = HERE.parent / "beacon_record_T_pulse_20260906T0015Z_collected_20260906T015625Z.json"
    if real.is_file():
        R = json.loads(real.read_text()); roots = nist_pulse.pinned_roots()
        t1 = X.parse_utc("2026-09-06T02:00:00Z"); t2 = X.parse_utc("2026-10-06T02:00:00Z")
        vs = [strip(X.verdict(R, t, roots, fetch=None)) for t in (t1, t2)]
        out.append({"exhibit": "B-real-filed-RETRY-record", "record_sha256": hashlib.sha256(real.read_bytes()).hexdigest(), "times": [X.fmt(t1), X.fmt(t2)], "verdicts": vs, "identical": vs[0] == vs[1],
                    "note": "MIN_T_SIGN refuses this record's T_sign under V19; the verdict shown is that refusal — identical at both times, as the property requires; it is NOT a seed"})
    return out
if __name__ == "__main__":
    res = run(); text = json.dumps(res, indent=1, sort_keys=True) + "\n"
    print(text); print("ALL IDENTICAL:", all(r["identical"] for r in res)); print("EXHIBIT-DIGEST:", hashlib.sha256(text.encode()).hexdigest())
