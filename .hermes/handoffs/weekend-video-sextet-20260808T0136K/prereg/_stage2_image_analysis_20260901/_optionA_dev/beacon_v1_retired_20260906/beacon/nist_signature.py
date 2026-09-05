#!/usr/bin/env python3
"""NIST Randomness Beacon v2.0 pulse verification — the cryptographic checks a third party would run, done locally.
Per NISTIR 8213 (Beacon format 2.0): (i) outputValue == SHA-512 over the serialized signed message with the signature appended
(and, in some implementations, SHA-512 of the signature alone) — this module tests the documented form and reports which held;
(ii) signatureValue is an RSA signature (cipherSuite 0: SHA-512, RSASSA-PKCS1-v1_5) over the serialized pulse fields, verified
with the RSA public key in the X.509 certificate NIST serves at /beacon/2.0/certificate/<certificateId>, whose SHA-512 must equal
certificateId. Serialization: strings are UTF-8 with a 4-byte big-endian length prefix; hex fields are their bytes with a 4-byte
length prefix; cipherSuite/period/statusCodes are 4-byte big-endian integers; chainIndex/pulseIndex are 8-byte big-endian.
Field order: uri, version, cipherSuite, period, certificateId, chainIndex, pulseIndex, timeStamp, localRandomValue,
external.sourceId, external.statusCode, external.value, each listValues[i].value, precommitmentValue, statusCode.
Requires the `cryptography` package (present: 47.0.0 on this lane). Nothing here touches the network; the caller supplies bytes."""
import hashlib, struct, datetime
from pathlib import Path
from cryptography import x509
from cryptography.x509.oid import ExtensionOID, AuthorityInformationAccessOID
from cryptography.hazmat.primitives import hashes, serialization
from cryptography.hazmat.primitives.asymmetric import padding, rsa

PINNED_ROOT_SHA256 = "cb3ccbb76031e5e0138f8dd39a23f9de47ffc35e43c1144cea27d46a5ab1cb5f"      # DigiCert Global Root G2 (DER SHA-256), the root NIST's beacon certificate chains to on 2026-09-05
PINNED_ROOT_PEM = Path(__file__).resolve().parent / "pinned_root_DigiCertGlobalRootG2.pem"
EXPECTED_SAN = "engine.beacon.nist.gov"
TRUST_ROOTS = None                     # tests may substitute a test root by patching this; production never sets it (None -> the pinned file)

def _roots():
    if TRUST_ROOTS is not None: return TRUST_ROOTS
    pem = PINNED_ROOT_PEM.read_bytes(); r = x509.load_pem_x509_certificate(pem)
    if hashlib.sha256(r.public_bytes(serialization.Encoding.DER)).hexdigest() != PINNED_ROOT_SHA256: raise RuntimeError("pinned root file does not match PINNED_ROOT_SHA256")
    return [r]

def _signed_by(child, parent):
    try:
        pk = parent.public_key()
        if isinstance(pk, rsa.RSAPublicKey): pk.verify(child.signature, child.tbs_certificate_bytes, padding.PKCS1v15(), child.signature_hash_algorithm)
        else: return False
        return child.issuer == parent.subject
    except Exception: return False

def issuer_url(cert):
    try:
        for d in cert.extensions.get_extension_for_oid(ExtensionOID.AUTHORITY_INFORMATION_ACCESS).value:
            if d.access_method == AuthorityInformationAccessOID.CA_ISSUERS: return d.access_location.value
    except Exception: pass
    return None

def verify_certificate_anchor(leaf_pem: bytes, intermediates_pem: list, at: datetime.datetime, expected_san=EXPECTED_SAN):
    """SAN == expected; validity covers `at`; leaf -> (intermediates) -> a pinned trust root, each link's RSA signature verified. Returns dict."""
    res = {}
    try:
        leaf = x509.load_pem_x509_certificate(leaf_pem)
        sans = leaf.extensions.get_extension_for_oid(ExtensionOID.SUBJECT_ALTERNATIVE_NAME).value.get_values_for_type(x509.DNSName)
        res["san_matches"] = expected_san in sans
        nb, na = leaf.not_valid_before_utc, leaf.not_valid_after_utc; res["valid_at_time"] = nb <= at <= na
        inters = [x509.load_pem_x509_certificate(b) for b in intermediates_pem]; roots = _roots()
        chain = [leaf]; cur = leaf; ok = False
        for _ in range(4):
            if any(_signed_by(cur, r) for r in roots): ok = True; break
            nxt = next((i for i in inters if _signed_by(cur, i)), None)
            if nxt is None: break
            chain.append(nxt); cur = nxt
        res["chains_to_pinned_root"] = ok; res["chain_length"] = len(chain)
        res["root_sha256"] = PINNED_ROOT_SHA256 if TRUST_ROOTS is None else hashlib.sha256(roots[0].public_bytes(serialization.Encoding.DER)).hexdigest()
    except Exception as e: res["error"] = repr(e)[:160]
    res["anchored"] = bool(res.get("san_matches") and res.get("valid_at_time") and res.get("chains_to_pinned_root"))
    return res

def _s(v): b = str(v).encode("utf-8"); return struct.pack(">I", len(b)) + b
def _h(v): b = bytes.fromhex(str(v)); return struct.pack(">I", len(b)) + b
def _u32(v): return struct.pack(">I", int(v))
def _u64(v): return struct.pack(">Q", int(v))

def serialize(p):
    out = b"".join([_s(p["uri"]), _s(p["version"]), _u32(p["cipherSuite"]), _u32(p["period"]), _h(p["certificateId"]), _u64(p["chainIndex"]), _u64(p["pulseIndex"]),
                    _s(p["timeStamp"]), _h(p["localRandomValue"]), _h(p["external"]["sourceId"]), _u32(p["external"]["statusCode"]), _h(p["external"]["value"])])
    for lv in p["listValues"]: out += _h(lv["value"])
    out += _h(p["precommitmentValue"]) + _u32(p["statusCode"])
    return out

def verify_pulse(p, cert_pem: bytes, intermediates_pem=None, at=None):
    """Returns a dict of named checks, each True/False, plus 'all' — never raises on a bad pulse. When intermediates/at are given the
    certificate ANCHOR (SAN + chain to the pinned root + validity) is checked and required for 'all'."""
    res = {}
    try:
        cert = x509.load_pem_x509_certificate(cert_pem); pub = cert.public_key()
        res["certificate_id_matches_sha512_of_der"] = hashlib.sha512(cert.public_bytes(serialization.Encoding.DER)).hexdigest().lower() == str(p["certificateId"]).lower()
        res["key_is_rsa"] = isinstance(pub, rsa.RSAPublicKey)
        msg = serialize(p); sig = bytes.fromhex(p["signatureValue"])
        try: pub.verify(sig, msg, padding.PKCS1v15(), hashes.SHA512()); res["signature_pkcs1v15_sha512"] = True
        except Exception: res["signature_pkcs1v15_sha512"] = False
        res["output_is_sha512_of_message_plus_signature"] = hashlib.sha512(msg + sig).hexdigest().lower() == str(p["outputValue"]).lower()
        res["output_is_sha512_of_signature"] = hashlib.sha512(sig).hexdigest().lower() == str(p["outputValue"]).lower()
        res["status_code_zero"] = int(p["statusCode"]) == 0
    except Exception as e:
        res["error"] = repr(e)[:160]
    if intermediates_pem is not None and at is not None:
        res["anchor"] = verify_certificate_anchor(cert_pem, intermediates_pem, at); anchored = res["anchor"]["anchored"]
    else: anchored = True                                                    # anchor not requested (offline sample checks); 'all' then excludes it
    res["all"] = bool(anchored and res.get("certificate_id_matches_sha512_of_der") and res.get("key_is_rsa") and res.get("signature_pkcs1v15_sha512") and (res.get("output_is_sha512_of_message_plus_signature") or res.get("output_is_sha512_of_signature")) and res.get("status_code_zero"))
    return res

if __name__ == "__main__":
    import json, sys
    p = json.load(open(sys.argv[1]))["pulse"]; print(json.dumps(verify_pulse(p, open(sys.argv[2], "rb").read()), indent=1))
