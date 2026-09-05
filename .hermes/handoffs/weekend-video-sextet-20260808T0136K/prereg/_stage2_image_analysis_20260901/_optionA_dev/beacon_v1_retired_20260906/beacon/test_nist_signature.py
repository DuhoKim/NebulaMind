"""Offline fixture for nist_signature.py against a REAL pulse and the certificate NIST served for its certificateId (both fetched
2026-09-05 15:13Z and retained here). Asserts the REQUIRED behaviour of the checks; it does NOT assert the observed NIST-side
condition (the served certificate is a 2048-bit TLS certificate while the signature is 4096-bit) — that is recorded in the change
record as a limit, and the signature check's result is reported, not pinned."""
import json, unittest, hashlib
from pathlib import Path
import sys; sys.path.insert(0, str(Path(__file__).resolve().parent))
import nist_signature as ns
HERE = Path(__file__).resolve().parent
class T(unittest.TestCase):
    def setUp(self):
        self.p = json.loads((HERE / "_sample_pulse_last.json").read_text())["pulse"]; self.cert = (HERE / "_sample_certificate.pem").read_bytes()
    def test_serialization_is_nists(self):                                   # outputValue == SHA-512(message || signature) proves the field order/encoding
        r = ns.verify_pulse(self.p, self.cert); self.assertTrue(r["output_is_sha512_of_message_plus_signature"])
    def test_certificate_id_binds_served_certificate(self):
        r = ns.verify_pulse(self.p, self.cert); self.assertTrue(r["certificate_id_matches_sha512_of_der"]); self.assertTrue(r["key_is_rsa"])
    def test_tampered_pulse_breaks_output_check(self):                       # a changed field (statusCode) must break the output binding
        q = dict(self.p); q["statusCode"] = 1; r = ns.verify_pulse(q, self.cert); self.assertFalse(r["output_is_sha512_of_message_plus_signature"]); self.assertFalse(r["all"])
    def test_tampered_output_detected(self):
        q = dict(self.p); q["outputValue"] = "0" * 128; r = ns.verify_pulse(q, self.cert); self.assertFalse(r["output_is_sha512_of_message_plus_signature"])
    def test_wrong_certificate_detected(self):
        from cryptography.hazmat.primitives.asymmetric import rsa
        from cryptography.hazmat.primitives import serialization, hashes
        from cryptography import x509; import datetime
        k = rsa.generate_private_key(public_exponent=65537, key_size=2048); name = x509.Name([x509.NameAttribute(x509.NameOID.COMMON_NAME, "fake")])
        c = x509.CertificateBuilder().subject_name(name).issuer_name(name).public_key(k.public_key()).serial_number(1).not_valid_before(datetime.datetime(2020,1,1)).not_valid_after(datetime.datetime(2030,1,1)).sign(k, hashes.SHA256())
        r = ns.verify_pulse(self.p, c.public_bytes(serialization.Encoding.PEM)); self.assertFalse(r["certificate_id_matches_sha512_of_der"]); self.assertFalse(r["all"])
    def test_reports_signature_result_without_raising(self):                 # the signature check is REPORTED (True/False), never an exception
        r = ns.verify_pulse(self.p, self.cert); self.assertIn(r["signature_pkcs1v15_sha512"], (True, False)); self.assertNotIn("error", r)
    def test_4096_bit_key_verifies_a_512_byte_signature(self):   # agy V12: the code is not size-bound; a 512-byte signature verifies when the key matches
        import sys as _s; _s.path.insert(0, str(HERE)); import test_support as ts
        from cryptography.hazmat.primitives.asymmetric import rsa
        k = rsa.generate_private_key(public_exponent=65537, key_size=4096); cert = ts.test_certificate(key=k)
        from datetime import datetime, timezone; tp = datetime(2026, 9, 6, 1, 10, tzinfo=timezone.utc)
        body, pem = ts.make_nist(tp, cert=cert); p = json.loads(body)["pulse"]; self.assertEqual(len(bytes.fromhex(p["signatureValue"])), 512)
        r = ns.verify_pulse(p, pem); self.assertTrue(r["signature_pkcs1v15_sha512"]); self.assertTrue(r["output_is_sha512_of_message_plus_signature"])
    def test_live_certificate_anchors_to_digicert_root(self):     # the certificate NIST served DOES chain to the pinned root and names the beacon host — the failure is the key/signature mismatch, not the anchor
        from datetime import datetime, timezone
        inter = (HERE / "_digicert_intermediate.pem").read_bytes(); saved = ns.TRUST_ROOTS; ns.TRUST_ROOTS = None      # the PINNED DigiCert root, not a test root another module may have installed in this process
        try: a = ns.verify_certificate_anchor(self.cert, [inter], datetime(2026, 9, 5, 15, 13, tzinfo=timezone.utc))
        finally: ns.TRUST_ROOTS = saved
        self.assertTrue(a["anchored"]); self.assertEqual(a["root_sha256"], ns.PINNED_ROOT_SHA256)
if __name__ == "__main__": unittest.main()
