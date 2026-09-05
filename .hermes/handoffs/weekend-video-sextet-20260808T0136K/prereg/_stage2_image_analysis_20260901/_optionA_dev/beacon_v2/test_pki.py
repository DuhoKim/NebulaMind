"""Test-only three-tier PKI (leaf -> intermediate -> test root) and mocked-network helpers for beacon_v2. Production never imports this.
The production shape of NIST's chain is leaf -> DigiCert intermediate -> DigiCert Global Root G2; tests exercise the same shape."""
import json, hashlib, datetime, urllib.error, urllib.parse
from pathlib import Path
import sys; sys.path.insert(0, str(Path(__file__).resolve().parent))
import nist_pulse as npulse, drand_round
from cryptography import x509
from cryptography.hazmat.primitives import hashes, serialization
from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.x509.oid import NameOID, AuthorityInformationAccessOID

def _name(cn): return x509.Name([x509.NameAttribute(NameOID.COMMON_NAME, cn)])
def _cert(subject, issuer, pubkey, signer_key, ca=False, san=None, aia=None, serial=1):
    b = x509.CertificateBuilder().subject_name(_name(subject)).issuer_name(_name(issuer)).public_key(pubkey).serial_number(serial).not_valid_before(datetime.datetime(2020, 1, 1)).not_valid_after(datetime.datetime(2035, 1, 1))
    b = b.add_extension(x509.BasicConstraints(ca=ca, path_length=None), critical=True)
    if san: b = b.add_extension(x509.SubjectAlternativeName([x509.DNSName(san)]), critical=False)
    if aia: b = b.add_extension(x509.AuthorityInformationAccess([x509.AccessDescription(AuthorityInformationAccessOID.CA_ISSUERS, x509.UniformResourceIdentifier(aia))]), critical=False)
    return b.sign(signer_key, hashes.SHA256())
ROOT_KEY = rsa.generate_private_key(65537, 2048); INTER_KEY = rsa.generate_private_key(65537, 2048); LEAF_KEY = rsa.generate_private_key(65537, 2048)
ROOT = _cert("test-root", "test-root", ROOT_KEY.public_key(), ROOT_KEY, ca=True)
INTER = _cert("test-intermediate", "test-root", INTER_KEY.public_key(), ROOT_KEY, ca=True, aia="http://test.invalid/root.crt", serial=2)
INTER_URL = "http://test.invalid/intermediate.crt"
def leaf(san="engine.beacon.nist.gov", key=None, signed_by="intermediate"):
    k = key or LEAF_KEY
    if signed_by == "intermediate": return _cert(san, "test-intermediate", k.public_key(), INTER_KEY, san=san, aia=INTER_URL, serial=3), k
    if signed_by == "root": return _cert(san, "test-root", k.public_key(), ROOT_KEY, san=san, aia="http://test.invalid/root.crt", serial=4), k
    return _cert(san, san, k.public_key(), k, san=san, aia=None, serial=5), k                       # self-signed
def pem(c): return c.public_bytes(serialization.Encoding.PEM)
def roots(): return [ROOT]
NEXT_LOCAL = "55" * 64
def pulse_body(t_pulse, leaf_cert, key, sign=True, status=0, uri="https://beacon.nist.gov/beacon/2.0/chain/2/pulse/123"):
    p = {"uri": uri, "version": "2.0", "cipherSuite": 0, "period": 60000, "certificateId": hashlib.sha512(leaf_cert.public_bytes(serialization.Encoding.DER)).hexdigest().upper(), "chainIndex": 2, "pulseIndex": 123,
         "timeStamp": t_pulse.strftime("%Y-%m-%dT%H:%M:%S.000Z"), "localRandomValue": "11" * 64, "external": {"sourceId": "00" * 32, "statusCode": 0, "value": "22" * 64},
         "listValues": [{"uri": uri.rsplit("/", 1)[0] + "/122", "type": "previous", "value": "33" * 64}], "precommitmentValue": hashlib.sha512(bytes.fromhex(NEXT_LOCAL)).hexdigest().upper(), "statusCode": status, "signatureValue": ""}
    msg = npulse.serialize(p); sig = key.sign(msg, padding.PKCS1v15(), hashes.SHA512()) if sign else b"\xab" * 256
    p["signatureValue"] = sig.hex().upper(); p["outputValue"] = hashlib.sha512(msg + sig).hexdigest().upper()
    return json.dumps({"pulse": p}).encode()
def next_body(t_pulse): return json.dumps({"pulse": {"uri": "https://beacon.nist.gov/beacon/2.0/chain/2/pulse/124", "localRandomValue": NEXT_LOCAL, "timeStamp": (t_pulse + datetime.timedelta(minutes=1)).strftime("%Y-%m-%dT%H:%M:%S.000Z")}}).encode()
def network(t_pulse, leaf_cert=None, key=None, sign=True, nist_404=False, drand=None, drand_disagree=False, status=0):
    """A fetch side-effect: NIST endpoints (pulse by time, certificate, AIA, next pulse) and the four drand relays for `drand` = (round, randomness)."""
    lc, k = (leaf_cert, key) if leaf_cert is not None else leaf()
    body = pulse_body(t_pulse, lc, k, sign=sign, status=status); ms = int(t_pulse.timestamp() * 1000)
    def side(url, timeout=30):
        if "nist.gov" in url:
            if nist_404: raise urllib.error.HTTPError(url, 404, "Not Found", None, None)
            if url.endswith(str(ms + 60000)): return next_body(t_pulse)
            if "/certificate/" in url: return pem(lc)
            return body
        if url == INTER_URL: return pem(INTER)
        if url.endswith("root.crt"): return pem(ROOT)
        if drand is not None:
            rnd, rand = drand; host = urllib.parse.urlparse(url).netloc
            v = hashlib.sha256(host.encode()).hexdigest() if drand_disagree else rand
            return json.dumps({"round": rnd, "randomness": v, "signature": "aa"}).encode()
        raise OSError("no such endpoint in the test network: " + url)
    return side
