#!/usr/bin/env python3
"""BEACON SEED for the prospective development split (selection rule §3b) — Duho 2026-09-05 23:15 KST: "use the beacon split".
Rule (fixed here, before signature; the seed value is unknowable before it is published):
  T_sign = the UTC instant in Duho's signature statement of the selection rule (RFC 3339, seconds).
  T_pulse = the first whole minute >= T_sign + 600 s  (ten minutes after signature; NIST pulses are on the minute).
  PRIMARY: NIST Randomness Beacon v2, chain 2, pulse at T_pulse: https://beacon.nist.gov/beacon/2.0/pulse/time/<ms since epoch>.
           seed = outputValue (512-bit hex). Accept only if pulse.timeStamp == T_pulse exactly and pulse.uri is on beacon.nist.gov.
  FALLBACK (fixed): ONLY if, 24 h or more after T_pulse, NIST's server answers HTTP 404 for the T_pulse pulse (absence). A network,
           DNS, timeout or validation failure is NOT absence and yields BEACON-RETRY at any time; never before 24 h; never if the pulse exists: drand mainnet default chain (hash 8990e7a9aaed2ffed73dbd7092123d6f289930540d7651336225dc172e51b2ce,
           genesis 1595431050, period 30 s), round = floor((T_pulse_epoch - genesis)/period) + 1, seed = randomness (256-bit hex),
           from https://api.drand.sh/public/<round>. Same acceptance: the round number must equal the computed one.
  Before 24 h have passed a failed primary fetch yields BEACON-RETRY (exit 4): nothing else may supply a seed; run again later.
  If after 24 h the primary is absent AND the fallback also fails: BEACON-UNAVAILABLE; the draw is NOT made; the study waits for Duho.
  A third party settles a disputed fallback by asking NIST's archive for the T_pulse pulse: if it exists, the primary was binding and
  any fallback-derived split is VOID.
  Nothing else may supply a seed. Reading a public beacon is inward; nothing is published.
Inputs bound into the record: --rule-sha256 (the signed selection rule's digest) and --signature-statement (a text file holding Duho's
signature statement as relayed, containing that digest and T_sign); the record hashes both, so a third party can check that the T_sign
used to pick the pulse is the one in the retained statement.
ACCEPTANCE (what the script checks): NIST — timeStamp == T_pulse, uri on beacon.nist.gov, chainIndex == "2", statusCode == 0,
outputValue is 128 hex chars; THEN the certificate NIST serves for certificateId is fetched and nist_signature.verify_pulse runs:
certificateId == SHA-512(certificate DER) and outputValue == SHA-512(serialized pulse || signatureValue) are REQUIRED (the second
proves the pulse bytes are the ones NIST signed over), the RSA signature verification result is RECORDED (it is required to pass
whenever NIST serves a certificate whose key can verify it; on 2026-09-05 NIST served a 2048-bit TLS certificate for a 4096-bit
signature — recorded as a limit, see the rule); drand — round == computed round, randomness is 64 hex chars. WHAT IT DOES NOT DO: it does not verify the
NIST pulse signature/certificate/precommitment chain or drand's BLS proof; those are verified by a third party against the public
archives (the record retains signatureValue / signature verbatim for that purpose). Authentication is therefore by public re-fetch, not
by this program.
Output: beacon_record.json {source, uri, T_sign, T_pulse, pulse (verbatim JSON), seed_hex, fetched_utc, body_sha256, rule_sha256,
signature_statement_sha256}. A third party verifies by fetching the same uri and comparing outputValue/randomness.
"""
import sys, json, time, hashlib, argparse, urllib.request, urllib.error, urllib.parse
from pathlib import Path as _P
sys.path.insert(0, str(_P(__file__).resolve().parent))
import nist_signature
from datetime import datetime, timezone, timedelta
NIST_TIME_URL = "https://beacon.nist.gov/beacon/2.0/pulse/time/{ms}"
NIST_CERT_URL = "https://beacon.nist.gov/beacon/2.0/certificate/{cid}"
DRAND_URLS = ("https://api.drand.sh/public/{round}", "https://api2.drand.sh/public/{round}", "https://api3.drand.sh/public/{round}", "https://drand.cloudflare.com/public/{round}")   # independent relays; >= 2 distinct hosts must agree
DRAND_URL = DRAND_URLS[0]
NIST_NEXT_URL = "https://beacon.nist.gov/beacon/2.0/pulse/time/{ms}"
MIN_RELAY_AGREEMENT = 2
DRAND_GENESIS, DRAND_PERIOD, DRAND_CHAIN = 1595431050, 30, "8990e7a9aaed2ffed73dbd7092123d6f289930540d7651336225dc172e51b2ce"
DELAY_S = 600
def parse_utc(s): return datetime.strptime(s, "%Y-%m-%dT%H:%M:%SZ").replace(tzinfo=timezone.utc)
def pulse_time(t_sign):
    t = t_sign + timedelta(seconds=DELAY_S)
    if t.second or t.microsecond: t = (t + timedelta(minutes=1)).replace(second=0, microsecond=0)
    return t
def drand_round(t_pulse): return int((t_pulse.timestamp() - DRAND_GENESIS) // DRAND_PERIOD) + 1
def fetch(url, timeout=30):
    with urllib.request.urlopen(url, timeout=timeout) as r: return r.read()
HEX = __import__("re").compile(r"^[0-9A-Fa-f]+$")
def accept_nist(body, t_pulse):
    p = json.loads(body)["pulse"]; ov = str(p.get("outputValue", ""))
    ok = (p.get("timeStamp") == t_pulse.strftime("%Y-%m-%dT%H:%M:%S.000Z") and str(p.get("uri", "")).startswith("https://beacon.nist.gov/")
          and str(p.get("chainIndex")) == "2" and int(p.get("statusCode", -1)) == 0 and len(ov) == 128 and bool(HEX.match(ov)))
    return ok, p
def accept_drand(body, rnd):
    p = json.loads(body); r = str(p.get("randomness", "")); return (p.get("round") == rnd and len(r) == 64 and bool(HEX.match(r))), p
def main(argv=None):
    ap = argparse.ArgumentParser(); ap.add_argument("--t-sign", required=True, help="UTC of the signature statement, e.g. 2026-09-06T01:00:00Z"); ap.add_argument("--out", required=True)
    ap.add_argument("--rule-sha256", required=True, help="SHA-256 of the signed selection rule"); ap.add_argument("--signature-statement", required=True, help="text file: Duho's signature statement as relayed (must contain the rule digest and T_sign)")
    a = ap.parse_args(argv)
    with open(a.signature_statement, "rb") as fh:
        stmt = fh.read()
    if a.rule_sha256.encode() not in stmt or a.t_sign.encode() not in stmt: print("SIGNATURE-STATEMENT-DOES-NOT-BIND: the statement must contain the rule digest and T_sign"); return 2
    t_sign = parse_utc(a.t_sign); t_pulse = pulse_time(t_sign); now = datetime.now(timezone.utc)
    if now < t_pulse: print(f"BEACON-NOT-YET: T_pulse {t_pulse.isoformat()} is in the future"); return 3
    rec = {"T_sign": a.t_sign, "T_pulse": t_pulse.strftime("%Y-%m-%dT%H:%M:%SZ"), "fetched_utc": now.strftime("%Y-%m-%dT%H:%M:%SZ"), "rule": __doc__,
           "rule_sha256": a.rule_sha256, "signature_statement_sha256": hashlib.sha256(stmt).hexdigest()}
    absent = False; unverifiable = False
    try:
        body = fetch(NIST_TIME_URL.format(ms=int(t_pulse.timestamp() * 1000))); ok, p = accept_nist(body, t_pulse)
        if ok:
            # AUTHENTICATION (nist_signature): certificate NIST serves for certificateId; REQUIRE all of: certificateId == SHA-512(cert DER),
            # outputValue == SHA-512(serialized pulse || signature), statusCode == 0, AND the RSA signature verifies under that certificate's
            # key. A pulse whose signature does not verify is NOT accepted (BEACON-RETRY with reason) — codex, V11 gate. Also fetch the NEXT
            # pulse and check the precommitment chain: SHA-512(next.localRandomValue) == pulse.precommitmentValue (recorded; required).
            cert_pem = fetch(NIST_CERT_URL.format(cid=p["certificateId"]))
            # CERTIFICATE ANCHOR (agy, V12 gate: a certificate carried in the record must not be trusted by itself): fetch the issuer chain
            # via the leaf's AIA URL and require SAN == engine.beacon.nist.gov and a verified chain to the PINNED DigiCert Global Root G2.
            inters = []
            try:
                leaf = nist_signature.x509.load_pem_x509_certificate(cert_pem); u = nist_signature.issuer_url(leaf)
                if u:
                    ib = fetch(u)
                    try: ic = nist_signature.x509.load_der_x509_certificate(ib)
                    except Exception: ic = nist_signature.x509.load_pem_x509_certificate(ib)
                    inters.append(ic.public_bytes(nist_signature.serialization.Encoding.PEM))
            except Exception as e: rec["intermediate_error"] = repr(e)[:120]
            v = nist_signature.verify_pulse(p, cert_pem, intermediates_pem=inters, at=t_pulse)
            chain_ok = None
            try:
                nb = fetch(NIST_NEXT_URL.format(ms=int(t_pulse.timestamp() * 1000) + 60000)); nxt = json.loads(nb)["pulse"]
                chain_ok = hashlib.sha512(bytes.fromhex(nxt["localRandomValue"])).hexdigest().lower() == str(p["precommitmentValue"]).lower()
                v["precommitment_chain_to_next_pulse"] = chain_ok; v["next_pulse_uri"] = nxt.get("uri"); next_body = nb
            except Exception as e: v["precommitment_chain_to_next_pulse"] = None; v["next_pulse_error"] = repr(e)[:120]
            if v.get("all") and chain_ok:
                rec.update(source="NIST-beacon-2.0", uri=p["uri"], pulse=p, seed_hex=p["outputValue"].lower(), body=body.decode("utf-8", "replace"), body_sha256=hashlib.sha256(body).hexdigest(),
                           certificate_pem=cert_pem.decode("utf-8", "replace"), certificate_pem_sha256=hashlib.sha256(cert_pem).hexdigest(),
                           intermediate_pems=[b.decode("utf-8", "replace") for b in inters], pinned_root_sha256=nist_signature.PINNED_ROOT_SHA256, pulse_verification=v,
                           next_body=next_body.decode("utf-8", "replace"), next_body_sha256=hashlib.sha256(next_body).hexdigest())      # retained so the builder RECOMPUTES the precommitment link
            else:
                unverifiable = True; rec["primary_rejected"] = {"reason": "pulse not authenticated (signature/certificate/output/status/precommitment)", "checks": v}
        else: rec["primary_rejected"] = {"timeStamp": p.get("timeStamp"), "uri": p.get("uri")}      # served but not the T_pulse pulse: NOT absence
    except urllib.error.HTTPError as e:
        rec["primary_error"] = f"HTTP {e.code}"; absent = (e.code == 404)                            # ONLY a 404 from NIST is evidence of absence
    except Exception as e: rec["primary_error"] = repr(e)[:200]                                     # network/DNS/timeout: not evidence of absence
    if "seed_hex" not in rec:
        if now - t_pulse < timedelta(hours=24) or not (absent or unverifiable):
            rec["verdict"] = ("BEACON-RETRY: primary not retrievable or not authenticated yet; fallback is not permitted before 24 h after T_pulse" if now - t_pulse < timedelta(hours=24)
                              else "BEACON-RETRY: primary failed without a 404 from NIST and without a recorded authentication failure (network failure is neither); retry")
            with open(a.out, "w") as fh:
                json.dump(rec, fh, indent=1, sort_keys=True)
            print(rec["verdict"]); return 4
        # FALLBACK trigger (fixed): >= 24 h after T_pulse AND (NIST 404 for T_pulse OR NIST pulse present but NOT authenticable). drand mainnet
        # default chain, computed round; AUTHENTICATION: >= MIN_RELAY_AGREEMENT distinct relay hosts must return the same randomness for that
        # round (all responses retained). The BLS proof is NOT verified here — no BLS12-381 library on the lane; stated in the rule.
        rnd = drand_round(t_pulse); responses = {}; agree = {}
        for u in DRAND_URLS:
            url = u.format(round=rnd)
            try:
                b = fetch(url); ok, q = accept_drand(b, rnd)
                responses[url] = {"ok": ok, "body": b.decode("utf-8", "replace"), "body_sha256": hashlib.sha256(b).hexdigest()}
                if ok: agree.setdefault(q["randomness"].lower(), []).append(url)
            except Exception as e: responses[url] = {"ok": False, "error": repr(e)[:120]}
        best = max(agree.items(), key=lambda kv: len(kv[1]), default=(None, []))
        if best[0] and len({urllib.parse.urlparse(x).netloc for x in best[1]}) >= MIN_RELAY_AGREEMENT:
            first = json.loads(responses[best[1][0]]["body"])
            rec.update(source="drand-mainnet-default", uri=best[1][0], chain_hash=DRAND_CHAIN, round=rnd, pulse=first, seed_hex=best[0], body=responses[best[1][0]]["body"], body_sha256=responses[best[1][0]]["body_sha256"],
                       relay_responses=responses, relays_agreeing=best[1], fallback_condition=("primary absent (404)" if absent else "primary present but not authenticable") + " >= 24 h after T_pulse; VOID if NIST's archive later serves an authenticable T_pulse pulse")
        else: rec["fallback_rejected"] = {"reason": f"fewer than {MIN_RELAY_AGREEMENT} independent relays agree", "responses": responses}
    if "seed_hex" not in rec: rec["verdict"] = "BEACON-UNAVAILABLE"
    with open(a.out, "w") as fh:
        json.dump(rec, fh, indent=1, sort_keys=True)
    print(json.dumps({k: rec.get(k) for k in ("source", "T_pulse", "seed_hex", "verdict")})); return 0 if "seed_hex" in rec else 2
if __name__ == "__main__": sys.exit(main())
