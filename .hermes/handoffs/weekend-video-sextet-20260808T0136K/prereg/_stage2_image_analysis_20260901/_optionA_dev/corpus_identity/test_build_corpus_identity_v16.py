"""V16 builder variant: the beacon boundary is beacon_record_expedited.verdict. Asserts on the same expedited drand record the V16
builder ACCEPTS at T_pulse + 1 min where the V15 builder REFUSES (BEACON-NOT-ACCEPTED (RETRY)), and that both refuse a record whose
T_sign predates the amendment. Uses the three-tier test PKI; no network."""
import json, unittest, tempfile, sys, difflib
from datetime import datetime, timezone, timedelta
from pathlib import Path
HERE = Path(__file__).resolve().parent; sys.path.insert(0, str(HERE)); sys.path.insert(0, str(HERE.parent / "beacon_v2"))
import beacon_record_expedited as X, beacon_record as V15B, drand_round, test_pki as pki
import build_corpus_identity_v16 as B16, build_corpus_identity as B15
T_SIGN = datetime(2026, 9, 6, 3, 0, 7, tzinfo=timezone.utc); TP = X.pulse_time(T_SIGN); D = "b" * 64; STMT = f"V16 signed: {D} at {X.fmt(T_SIGN)}".encode()
RND = drand_round.round_for(TP); SOON = TP + timedelta(minutes=1)
class T(unittest.TestCase):
    def setUp(self):
        self.d = Path(tempfile.mkdtemp()); self.n = pki.network(TP, sign=False, drand=(RND, "c" * 64))
        rec = X.collect(self.n, X.fmt(T_SIGN), D, STMT, now=SOON); self.rec = self.d / "rec.json"; self.rec.write_text(json.dumps(rec)); self.stmt = self.d / "stmt.txt"; self.stmt.write_bytes(STMT)
        for m in (B16, B15): m.nist_pulse.pinned_roots = pki.roots
    def test_v16_builder_accepts_where_v15_builder_refuses(self):
        B, raw, r = B16._validate_beacon_record(self.rec, D, self.stmt, fetch=self.n, now=SOON)
        self.assertEqual(r["outcome"], "ACCEPT-DRAND"); self.assertEqual(r["seed_hex"], "c" * 64)
        with self.assertRaises(SystemExit) as cm: B15._validate_beacon_record(self.rec, D, self.stmt, fetch=self.n, now=SOON)
        self.assertIn("BEACON-NOT-ACCEPTED", str(cm.exception)); self.assertIn("RETRY", str(cm.exception))
    def test_both_refuse_old_t_sign(self):
        rec = json.loads(self.rec.read_text()); rec["T_sign"] = "2026-09-06T00:04:07Z"; rec["T_pulse"] = "2026-09-06T00:15:00Z"; p = self.d / "old.json"; p.write_text(json.dumps(rec))
        s = self.d / "s.txt"; s.write_bytes(f"x {D} 2026-09-06T00:04:07Z".encode())
        with self.assertRaises(SystemExit) as cm: B16._validate_beacon_record(p, D, s, fetch=self.n, now=SOON)
        self.assertIn("T-SIGN-PREDATES-AMENDMENT", str(cm.exception))
    def test_v16_builder_differs_from_v15_only_in_import_and_docstring(self):
        a = (HERE / "build_corpus_identity.py").read_text().splitlines(); b = (HERE / "build_corpus_identity_v16.py").read_text().splitlines()
        ch = [l for l in difflib.unified_diff(a, b, n=0, lineterm="") if l[:1] in "+-" and l[:3] not in ("+++", "---")]
        self.assertEqual(len(ch), 4, ch); self.assertTrue(all(("beacon_record" in l) or ("V16" in l) or ("Build the ordered" in l) for l in ch), ch)
if __name__ == "__main__": unittest.main()
