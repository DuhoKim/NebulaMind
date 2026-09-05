"""Test-only support: build a NIST-2.0-shaped pulse that is INTERNALLY consistent the way nist_signature checks it — certificateId =
SHA-512 of a self-signed test certificate's DER, outputValue = SHA-512(serialized pulse || signature). The signature bytes are
arbitrary, so the RSA check reports False (as it does on NIST's live material tonight); the structural checks report True.
Production never imports this module."""
import json, hashlib, datetime, os
from pathlib import Path
import sys; sys.path.insert(0, str(Path(__file__).resolve().parent))
import nist_signature as ns
from cryptography import x509
from cryptography.hazmat.primitives import hashes, serialization
from cryptography.hazmat.primitives.asymmetric import rsa

from cryptography.hazmat.primitives.asymmetric import padding
_KEY = rsa.generate_private_key(public_exponent=65537, key_size=2048)          # leaf key (one per process; generation is slow)
_ROOT_KEY = rsa.generate_private_key(public_exponent=65537, key_size=2048)     # a TEST trust root, substituted for the pinned DigiCert root via install_test_root()
_ROOT_NAME = x509.Name([x509.NameAttribute(x509.NameOID.COMMON_NAME, "test-root")])
_ROOT = x509.CertificateBuilder().subject_name(_ROOT_NAME).issuer_name(_ROOT_NAME).public_key(_ROOT_KEY.public_key()).serial_number(1).not_valid_before(datetime.datetime(2020, 1, 1)).not_valid_after(datetime.datetime(2035, 1, 1)).add_extension(x509.BasicConstraints(ca=True, path_length=None), critical=True).sign(_ROOT_KEY, hashes.SHA256())
ROOT_PEM = _ROOT.public_bytes(serialization.Encoding.PEM)
def install_test_root():
    """Make nist_signature trust the TEST root (production never calls this; TRUST_ROOTS is None in production)."""
    ns.TRUST_ROOTS = [_ROOT]
def test_certificate(san="engine.beacon.nist.gov", signed_by_root=True, key=None):
    k = key or _KEY; name = x509.Name([x509.NameAttribute(x509.NameOID.COMMON_NAME, san)])
    b = x509.CertificateBuilder().subject_name(name).issuer_name(_ROOT_NAME if signed_by_root else name).public_key(k.public_key()).serial_number(7).not_valid_before(datetime.datetime(2020, 1, 1)).not_valid_after(datetime.datetime(2035, 1, 1)).add_extension(x509.SubjectAlternativeName([x509.DNSName(san)]), critical=False).add_extension(x509.AuthorityInformationAccess([x509.AccessDescription(x509.oid.AuthorityInformationAccessOID.CA_ISSUERS, x509.UniformResourceIdentifier("http://test.invalid/test-root.crt"))]), critical=False)
    c = b.sign(_ROOT_KEY if signed_by_root else k, hashes.SHA256())
    return c.public_bytes(serialization.Encoding.PEM), hashlib.sha512(c.public_bytes(serialization.Encoding.DER)).hexdigest().upper(), k

def make_nist(tp, uri="https://beacon.nist.gov/beacon/2.0/chain/2/pulse/123", cert=None, status=0, sign=True):
    """A pulse SIGNED with the test certificate's key (PKCS1v15/SHA-512 over the NISTIR serialization), so verify_pulse.all is True
    for the right reason; sign=False leaves an arbitrary signature (used to show that an unauthenticated pulse is refused)."""
    pem, cid, key = cert or test_certificate()
    p = {"uri": uri, "version": "2.0", "cipherSuite": 0, "period": 60000, "certificateId": cid, "chainIndex": 2, "pulseIndex": 123,
         "timeStamp": tp.strftime("%Y-%m-%dT%H:%M:%S.000Z"), "localRandomValue": "11" * 64,
         "external": {"sourceId": "00" * 32, "statusCode": 0, "value": "22" * 64},
         "listValues": [{"uri": uri.rsplit("/", 1)[0] + "/122", "type": "previous", "value": "33" * 64}],
         "precommitmentValue": hashlib.sha512(bytes.fromhex(NEXT_LOCAL_RANDOM)).hexdigest().upper(), "statusCode": status, "signatureValue": ""}
    msg = ns.serialize(p)
    sig = key.sign(msg, padding.PKCS1v15(), hashes.SHA512()) if sign else bytes.fromhex("AB" * 256)
    p["signatureValue"] = sig.hex().upper()
    p["outputValue"] = hashlib.sha512(msg + sig).hexdigest().upper()
    return json.dumps({"pulse": p}).encode(), pem

NEXT_LOCAL_RANDOM = "55" * 64
def make_next(tp, uri="https://beacon.nist.gov/beacon/2.0/chain/2/pulse/124"):
    """The pulse one minute later, whose localRandomValue closes the precommitment chain of make_nist's pulse."""
    p = {"uri": uri, "localRandomValue": NEXT_LOCAL_RANDOM, "timeStamp": (tp + datetime.timedelta(minutes=1)).strftime("%Y-%m-%dT%H:%M:%S.000Z")}
    return json.dumps({"pulse": p}).encode()

def nist_side(body, pem, next_body=None, tp=None):
    """fetch side_effect: certificate endpoint -> test certificate; the T_pulse+60s time URL -> the next pulse; else the pulse body."""
    def side(url, timeout=30):
        if "/certificate/" in url: return pem
        if "cacerts" in url or url.endswith(".crt"): return ROOT_PEM        # the AIA issuer fetch: our test root doubles as the issuer (leaf is root-signed)
        if tp is not None and url.endswith(str(int(tp.timestamp() * 1000) + 60000)): return next_body if next_body is not None else make_next(tp)
        return body
    return side

def drand_side_with_authenticable_nist(rnd, tp, randomness="f" * 64):
    """Fallback probe: relays agree, but NIST now serves an authenticable T_pulse pulse -> the builder must VOID the fallback."""
    body, pem = make_nist(tp); ns_side = nist_side(body, pem, tp=tp); dr = drand_side(rnd, randomness)
    def side(url, timeout=30): return ns_side(url) if "nist.gov" in url else dr(url)
    return side

def drand_side(rnd, randomness="f" * 64, disagree_hosts=()):
    """fetch side_effect for the fallback: NIST -> 404; every drand relay returns the same round/randomness (relays in disagree_hosts differ)."""
    import urllib.error, urllib.parse
    def side(url, timeout=30):
        if "nist.gov" in url: raise urllib.error.HTTPError(url, 404, "Not Found", None, None)
        host = urllib.parse.urlparse(url).netloc
        return json.dumps({"round": rnd, "randomness": ("0" * 64 if host in disagree_hosts else randomness), "signature": "aa"}).encode()
    return side
