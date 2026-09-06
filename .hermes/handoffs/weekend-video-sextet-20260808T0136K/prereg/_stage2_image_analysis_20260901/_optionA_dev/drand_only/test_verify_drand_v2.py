"""drand-only verifier fixture (run under _optionA_dev/_venv_bls: python -m unittest test_verify_drand). Uses the retained public round files."""
import json, unittest, sys
from datetime import datetime, timezone
from pathlib import Path
HERE = Path(__file__).resolve().parent; sys.path.insert(0, str(HERE)); import verify_drand_v2 as vd
A = json.loads((HERE / "round_6441924_api.drand.sh.json").read_text())
class T(unittest.TestCase):
    def test_prospective_round_does_not_exist_at_approval_and_uses_pinned_formula(self):
        for t in (datetime(2026, 9, 7, 1, 0, 7, tzinfo=timezone.utc), datetime(2026, 9, 7, 1, 0, 0, tzinfo=timezone.utc), datetime(2026, 9, 7, 23, 59, 59, tzinfo=timezone.utc)):
            p = vd.prospective_round(t); self.assertFalse(p["exists_at_approval"]); self.assertGreaterEqual(vd.round_time(p["round"]), vd.pulse_time(t)); self.assertLess(vd.round_time(p["round"]) - vd.pulse_time(t), __import__("datetime").timedelta(seconds=vd.PERIOD))
        self.assertEqual(vd.pulse_time(datetime(2026, 9, 6, 1, 0, 1, tzinfo=timezone.utc)).strftime("%H:%M:%S"), "01:11:00")   # the V15 formula, unchanged
    def test_public_round_verifies_under_pinned_key(self):
        c = vd.verify(A, 6441924, vd.round_url("https://api.drand.sh", 6441924)); self.assertTrue(c["accepted"]); self.assertEqual(c["seed_hex"], A["randomness"])
    def test_tampered_wrong_round_unbound_path_and_wrong_key_refuse(self):
        U = vd.round_url("https://api.drand.sh", 6441924); t = dict(A); t["signature"] = A["signature"][:-2] + "00"; self.assertFalse(vd.verify(t, 6441924, U)["accepted"])
        self.assertFalse(vd.verify(A, 6441925, vd.round_url("https://api.drand.sh", 6441925))["accepted"])
        self.assertFalse(vd.verify(A, 6441924, "https://api.drand.sh/public/6441924")["accepted"])            # unqualified path: chain not bound
        self.assertFalse(vd.verify(A, 6441924, None)["accepted"])                                                   # V21: source_url required
        self.assertFalse(vd.verify(A, 6441924, "https://api.drand.sh.attacker.invalid/" + vd.CHAIN_HASH + "/public/6441924")["accepted"])   # look-alike host
        self.assertFalse(vd.verify(A, 6441924, vd.round_url("https://api.drand.sh", 6441924) + "/x")["accepted"])   # suffix
        self.assertFalse(vd.verify(A, 6441924, "https://attacker.invalid/" + vd.CHAIN_HASH + "/public/6441924")["accepted"])
        saved = vd.PUBLIC_KEY_HEX; vd.PUBLIC_KEY_HEX = "9" + saved[1:]
        try: self.assertFalse(vd.verify(A, 6441924, U)["bls_verifies_under_pinned_key"])
        finally: vd.PUBLIC_KEY_HEX = saved
        r = dict(A); r["randomness"] = "0" * 64; self.assertFalse(vd.verify(r, 6441924, U)["accepted"])
    def test_deterministic(self):
        U = vd.round_url("https://api.drand.sh", 6441924); self.assertEqual(vd.verify(A, 6441924, U), vd.verify(A, 6441924, U))
if __name__ == "__main__": unittest.main()
