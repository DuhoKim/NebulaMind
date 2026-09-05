#!/usr/bin/env python3
"""drand (League of Entropy) mainnet default chain — EVIDENCE and AGREEMENT, rebuilt once. collect(fetch, rnd) gathers the raw body from
each PINNED relay (or the error); agreement(evidence, rnd) recomputes, from the bytes, which pinned HOSTS returned the computed round with
the same 64-hex randomness. INDEPENDENCE LIMIT (a finding, not a claim): distinct pinned hostnames are the only independence available
from bytes; the BLS proof is NOT verified here (no BLS12-381 library on the lane) — a third party verifies it against the chain."""
import json, re, urllib.parse
CHAIN_HASH = "8990e7a9aaed2ffed73dbd7092123d6f289930540d7651336225dc172e51b2ce"; GENESIS = 1595431050; PERIOD = 30
RELAYS = ("https://api.drand.sh/public/{round}", "https://api2.drand.sh/public/{round}", "https://api3.drand.sh/public/{round}", "https://drand.cloudflare.com/public/{round}")
MIN_HOSTS = 2
def round_for(t): return int((t.timestamp() - GENESIS) // PERIOD) + 1
def collect(fetch, rnd):
    ev = {}
    for u in RELAYS:
        url = u.format(round=rnd)
        try: ev[url] = {"body": fetch(url)}
        except Exception as e: ev[url] = {"error": repr(e)[:120]}
    return ev
def agreement(ev, rnd):
    """From bytes: {randomness: sorted list of pinned hosts that returned it for rnd}; keys not in RELAYS are ignored (never counted)."""
    pinned = {u.format(round=rnd) for u in RELAYS}; by_value = {}
    for url, r in ev.items():
        if url not in pinned or "body" not in r: continue
        try: q = json.loads(r["body"])
        except Exception: continue
        v = str(q.get("randomness", ""))
        if q.get("round") == rnd and re.fullmatch(r"[0-9a-fA-F]{64}", v): by_value.setdefault(v.lower(), set()).add(urllib.parse.urlparse(url).netloc)
    best = max(by_value.items(), key=lambda kv: len(kv[1]), default=(None, set()))
    return {"randomness": best[0], "hosts": sorted(best[1]), "n_hosts": len(best[1]), "accepted": best[0] is not None and len(best[1]) >= MIN_HOSTS, "values_seen": {k: sorted(v) for k, v in by_value.items()}}
