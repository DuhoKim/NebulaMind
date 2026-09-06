#!/usr/bin/env python3
"""verify_drand_v2 (option A V21): verify_drand with EXACT pinned-URL membership — source_url is REQUIRED and must equal one of the four
chain-hash-qualified URLs for the round (None, look-alike hosts and suffixes refused; codex V20). The V20 bytes are preserved in verify_drand.py.
DRAND-ONLY PROPOSAL (2026-09-06, prepared at Blanc's 18:59 instruction; NOT adopted, NOT gated, NOT approved).
Single public randomness source: drand mainnet default chain, scheme pedersen-bls-chained. Everything below is pinned in the proposal text:
  CHAIN_HASH, the chain's PUBLIC KEY (G1, 48 bytes), GENESIS, PERIOD, the message rule, the DST.
1. PROSPECTIVELY FIXED FUTURE ROUND: T_pulse = first whole minute >= T_approval + 600 s (the pinned V15 formula); ROUND = floor((T_pulse - GENESIS)/PERIOD) + 1.
   The round's scheduled time is GENESIS + (ROUND-1)*PERIOD >= T_pulse > T_approval: it does not exist when the approval is given.
2. BOUND CHAIN IDENTITY: a response is admissible only if fetched from `/<CHAIN_HASH>/public/<round>` on a pinned relay AND it verifies under the
   pinned PUBLIC KEY — the key IS the chain; no response from an unpinned path or another chain can pass.
3. ACTUAL CRYPTOGRAPHIC VERIFICATION: BLS12-381 signature (G2, 96 bytes) verified against the pinned public key over
   message = SHA-256(previous_signature || round as 8-byte big-endian), DST BLS_SIG_BLS12381G2_XMD:SHA-256_SSWU_RO_NUL_ (py_ecc G2Basic);
   randomness must equal SHA-256(signature). The signature is DETERMINISTIC for the round (BLS threshold signature of a fixed message), so the
   seed is a function of (ROUND, PUBLIC KEY) — no relay, no operator and no collection time can change it.
4. RESIDUAL TRUST, stated in the proposal text: the chain's threshold key holders (League of Entropy) and the pinned key's authenticity;
   relay availability (RETRY, never a different value); py_ecc's correctness (a pure-Python BLS implementation, pinned by version and digest).
"""
from __future__ import annotations
import hashlib, json, sys
from datetime import datetime, timezone, timedelta
from pathlib import Path
from py_ecc.bls import G2Basic

CHAIN_HASH = "8990e7a9aaed2ffed73dbd7092123d6f289930540d7651336225dc172e51b2ce"
PUBLIC_KEY_HEX = "868f005eb8e6e4ca0a47c8a77ceaa5309a47978a7c71bc5cce96366b5d7a569937c529eeda66c7293784a9402801af31"
GENESIS = 1595431050; PERIOD = 30; SCHEME = "pedersen-bls-chained"; DELAY_S = 600
RELAYS = ("https://api.drand.sh", "https://api2.drand.sh", "https://api3.drand.sh", "https://drand.cloudflare.com")
def round_url(host, rnd): return f"{host}/{CHAIN_HASH}/public/{rnd}"

def pulse_time(t_approval: datetime) -> datetime:
    t = t_approval + timedelta(seconds=DELAY_S)
    if t.second or t.microsecond: t = (t + timedelta(minutes=1)).replace(second=0, microsecond=0)
    return t
def round_for(t: datetime) -> int: return int((t.timestamp() - GENESIS) // PERIOD) + 1
def round_time(rnd: int) -> datetime: return datetime.fromtimestamp(GENESIS + (rnd - 1) * PERIOD, tz=timezone.utc)
def prospective_round(t_approval: datetime) -> dict:
    tp = pulse_time(t_approval); r = round_for(tp)
    return {"t_approval": t_approval.strftime("%Y-%m-%dT%H:%M:%SZ"), "t_pulse": tp.strftime("%Y-%m-%dT%H:%M:%SZ"), "round": r,
            "round_scheduled_utc": round_time(r).strftime("%Y-%m-%dT%H:%M:%SZ"), "exists_at_approval": round_time(r) <= t_approval}

def message(previous_signature_hex: str, rnd: int) -> bytes:
    return hashlib.sha256(bytes.fromhex(previous_signature_hex) + rnd.to_bytes(8, "big")).digest()

def verify(resp: dict, expected_round: int, source_url: str) -> dict:
    """Recompute everything from the response bytes and the pinned key. Returns a dict of checks; 'accepted' iff all hold."""
    c = {}
    c["url_bound_to_chain_hash"] = source_url in {round_url(h, expected_round) for h in RELAYS}     # V21: EXACT membership; None or look-alike hosts or suffixes refused
    c["round_matches"] = int(resp.get("round", -1)) == expected_round
    try:
        sig = bytes.fromhex(resp["signature"]); prev = resp["previous_signature"]; rnd = int(resp["round"])
        c["signature_is_96_bytes_g2"] = len(sig) == 96
        c["randomness_is_sha256_of_signature"] = resp.get("randomness") == hashlib.sha256(sig).hexdigest()
        c["bls_verifies_under_pinned_key"] = bool(G2Basic.Verify(bytes.fromhex(PUBLIC_KEY_HEX), message(prev, rnd), sig))
    except Exception as e:
        c["error"] = repr(e)[:120]; c["bls_verifies_under_pinned_key"] = False
    c["accepted"] = all(v is True for k, v in c.items() if k != "error")
    if c["accepted"]: c["seed_hex"] = resp["randomness"]
    return c

def verify_chain_link(resp: dict, prev_resp: dict) -> bool:
    """Optional: the response's previous_signature equals the previous round's signature (chained scheme)."""
    return int(prev_resp["round"]) == int(resp["round"]) - 1 and prev_resp["signature"] == resp["previous_signature"]
