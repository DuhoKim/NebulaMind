#!/usr/bin/env python3
"""NIST Randomness Beacon 2.0 — EVIDENCE and AUTHENTICATION, rebuilt once (2026-09-06, Blanc's cap). Two functions and nothing else:
  collect(fetch, t_pulse)  -> evidence: a dict of BYTES only (pulse body, leaf certificate PEM, the issuer chain reached through AIA, the
                              next pulse body). No verdicts, no booleans are stored anywhere.
  authenticate(evidence, t_pulse, roots) -> checks: computed from the bytes alone, every time, by whoever holds the evidence.
Serialization per NISTIR 8213 (length-prefixed UTF-8 strings / hex bytes; big-endian u32/u64) in the documented field order. Anchor:
SAN == engine.beacon.nist.gov, validity at t_pulse, chain leaf -> intermediates -> a trusted root with every link's RSA signature verified.
The pulse is ACCEPTED only if anchor, certificateId, output binding, statusCode 0, RSA signature (SHA-512 PKCS1v15) and the
precommitment link to the next pulse ALL hold. This module never decides fallback; see beacon_record.verdict."""
import hashlib, struct, datetime, json
from pathlib import Path
from cryptography import x509
from cryptography.x509.oid import ExtensionOID, AuthorityInformationAccessOID
from cryptography.hazmat.primitives import hashes, serialization
from cryptography.hazmat.primitives.asymmetric import padding, rsa

TIME_URL = "https://beacon.nist.gov/beacon/2.0/pulse/time/{ms}"
CERT_URL = "https://beacon.nist.gov/beacon/2.0/certificate/{cid}"
EXPECTED_SAN = "engine.beacon.nist.gov"
PINNED_ROOT_SHA256 = "cb3ccbb76031e5e0138f8dd39a23f9de47ffc35e43c1144cea27d46a5ab1cb5f"      # DigiCert Global Root G2, DER SHA-256
PINNED_ROOT_PEM = Path(__file__).resolve().parent / "pinned_root_DigiCertGlobalRootG2.pem"
MAX_CHAIN = 4

def pinned_roots():
    r = x509.load_pem_x509_certificate(PINNED_ROOT_PEM.read_bytes())
    if hashlib.sha256(r.public_bytes(serialization.Encoding.DER)).hexdigest() != PINNED_ROOT_SHA256: raise RuntimeError("pinned root file does not match PINNED_ROOT_SHA256")
    return [r]

def _s(v): b = str(v).encode("utf-8"); return struct.pack(">I", len(b)) + b
def _h(v): b = bytes.fromhex(str(v)); return struct.pack(">I", len(b)) + b
def _u32(v): return struct.pack(">I", int(v))
def _u64(v): return struct.pack(">Q", int(v))
def serialize(p):
    out = b"".join([_s(p["uri"]), _s(p["version"]), _u32(p["cipherSuite"]), _u32(p["period"]), _h(p["certificateId"]), _u64(p["chainIndex"]), _u64(p["pulseIndex"]),
                    _s(p["timeStamp"]), _h(p["localRandomValue"]), _h(p["external"]["sourceId"]), _u32(p["external"]["statusCode"]), _h(p["external"]["value"])])
    for lv in p["listValues"]: out += _h(lv["value"])
    return out + _h(p["precommitmentValue"]) + _u32(p["statusCode"])

def issuer_url(cert):
    try:
        for d in cert.extensions.get_extension_for_oid(ExtensionOID.AUTHORITY_INFORMATION_ACCESS).value:
            if d.access_method == AuthorityInformationAccessOID.CA_ISSUERS: return d.access_location.value
    except Exception: pass
    return None

def _load(b):
    try: return x509.load_pem_x509_certificate(b)
    except Exception: return x509.load_der_x509_certificate(b)

def collect(fetch, t_pulse):
    """Gather EVIDENCE BYTES for the pulse at t_pulse: body, leaf, AIA chain (until a root-subject issuer or MAX_CHAIN), next body."""
    ms = int(t_pulse.timestamp() * 1000)
    ev = {"pulse_body": fetch(TIME_URL.format(ms=ms))}
    p = json.loads(ev["pulse_body"])["pulse"]
    ev["leaf_pem"] = _load(fetch(CERT_URL.format(cid=p["certificateId"]))).public_bytes(serialization.Encoding.PEM)
    chain = []; cur = _load(ev["leaf_pem"])
    for _ in range(MAX_CHAIN):
        u = issuer_url(cur)
        if not u or cur.issuer == cur.subject: break
        nxt = _load(fetch(u)); chain.append(nxt.public_bytes(serialization.Encoding.PEM)); cur = nxt
    ev["intermediate_pems"] = chain
    ev["next_body"] = fetch(TIME_URL.format(ms=ms + 60000))
    return ev

def _signed_by(child, parent):
    try:
        pk = parent.public_key()
        if not isinstance(pk, rsa.RSAPublicKey) or child.issuer != parent.subject: return False
        pk.verify(child.signature, child.tbs_certificate_bytes, padding.PKCS1v15(), child.signature_hash_algorithm); return True
    except Exception: return False

def anchor(leaf_pem, intermediate_pems, at, roots, expected_san=EXPECTED_SAN):
    res = {}
    try:
        leaf = _load(leaf_pem); inters = [_load(b) for b in intermediate_pems]
        res["san_matches"] = expected_san in leaf.extensions.get_extension_for_oid(ExtensionOID.SUBJECT_ALTERNATIVE_NAME).value.get_values_for_type(x509.DNSName)
        res["valid_at_time"] = leaf.not_valid_before_utc <= at <= leaf.not_valid_after_utc
        cur = leaf; ok = False; length = 1
        for _ in range(MAX_CHAIN):
            if any(_signed_by(cur, r) for r in roots): ok = True; break
            nxt = next((i for i in inters if _signed_by(cur, i)), None)
            if nxt is None: break
            cur = nxt; length += 1
        res["chains_to_trusted_root"] = ok; res["chain_length"] = length
    except Exception as e: res["error"] = repr(e)[:160]
    res["anchored"] = bool(res.get("san_matches") and res.get("valid_at_time") and res.get("chains_to_trusted_root"))
    return res

def authenticate(ev, t_pulse, roots):
    """Every check recomputed from evidence bytes. Returns {checks..., 'accepted': bool, 'seed_hex' or None}."""
    c = {}
    try:
        p = json.loads(ev["pulse_body"])["pulse"]; leaf = _load(ev["leaf_pem"]); sig = bytes.fromhex(p["signatureValue"]); msg = serialize(p)
        c["timestamp_is_t_pulse"] = p.get("timeStamp") == t_pulse.strftime("%Y-%m-%dT%H:%M:%S.000Z")
        c["uri_is_nist_chain2"] = bool(__import__("re").fullmatch(r"https://beacon\.nist\.gov/beacon/2\.0/chain/2/pulse/\d+", str(p.get("uri", "")))) and str(p.get("chainIndex")) == "2"
        c["status_code_zero"] = int(p.get("statusCode", -1)) == 0
        c["certificate_id_is_sha512_of_leaf_der"] = hashlib.sha512(leaf.public_bytes(serialization.Encoding.DER)).hexdigest().lower() == str(p["certificateId"]).lower()
        c["output_is_sha512_of_message_and_signature"] = hashlib.sha512(msg + sig).hexdigest().lower() == str(p["outputValue"]).lower()
        c["anchor"] = anchor(ev["leaf_pem"], ev.get("intermediate_pems", []), t_pulse, roots)
        try: leaf.public_key().verify(sig, msg, padding.PKCS1v15(), hashes.SHA512()); c["signature_verifies_under_leaf"] = True
        except Exception: c["signature_verifies_under_leaf"] = False
        c["leaf_key_bits"] = leaf.public_key().key_size; c["signature_bytes"] = len(sig)
        nxt = json.loads(ev["next_body"])["pulse"]
        c["precommitment_links_to_next"] = hashlib.sha512(bytes.fromhex(nxt["localRandomValue"])).hexdigest().lower() == str(p["precommitmentValue"]).lower()
        c["accepted"] = all([c["timestamp_is_t_pulse"], c["uri_is_nist_chain2"], c["status_code_zero"], c["certificate_id_is_sha512_of_leaf_der"], c["output_is_sha512_of_message_and_signature"], c["anchor"]["anchored"], c["signature_verifies_under_leaf"], c["precommitment_links_to_next"]])
        c["seed_hex"] = p["outputValue"].lower() if c["accepted"] else None
    except Exception as e:
        c["error"] = repr(e)[:160]; c["accepted"] = False; c["seed_hex"] = None
    return c
