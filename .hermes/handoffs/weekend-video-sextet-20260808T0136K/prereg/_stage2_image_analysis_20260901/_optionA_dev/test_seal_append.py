import json, os, shutil, tempfile, unittest, sys
from pathlib import Path
HERE = Path(__file__).resolve().parent; sys.path.insert(0, str(HERE)); sys.path.insert(0, str(HERE / "fourier_chirality"))
import seal_append as sa
REAL = HERE.parent / "seal_journal_tierc.jsonl"

class T(unittest.TestCase):
    def setUp(self):
        self.d = Path(tempfile.mkdtemp()); self.j = self.d / "seal_journal_tierc.jsonl"; shutil.copy(REAL, self.j)
        self.f = self.d / "corpus_identity.json"; self.f.write_text('{"x":1}\n')
    def tearDown(self): shutil.rmtree(self.d)
    def test_real_journal_chain_verifies(self):
        n = sa.verify_chain(self.j); self.assertEqual(n, sum(1 for _ in REAL.open()))
    def test_append_links_and_driver_sees_it(self):
        ev = sa.append(self.j, "corpus-identity-freeze", self.f)
        self.assertEqual(sa.verify_chain(self.j), 63)
        last = json.loads(self.j.read_bytes().splitlines()[-1]); self.assertEqual(last, ev)
        self.assertEqual(ev["predecessor_receipt_digest"], json.loads(self.j.read_bytes().splitlines()[-2])["receipt_digest"])
        import run_configurations as rc
        self.assertTrue(rc.journal_has(str(self.j), "corpus-identity-freeze", ev["observed_digest"]))
        self.assertFalse(rc.journal_has(str(self.j), "tuning-freeze", ev["observed_digest"]))
    def test_refuses_duplicate_unknown_missing(self):
        sa.append(self.j, "tuning-freeze", self.f)
        with self.assertRaises(ValueError) as c: sa.append(self.j, "tuning-freeze", self.f)
        self.assertIn("REFUSE-DUPLICATE", str(c.exception))
        with self.assertRaises(ValueError): sa.append(self.j, "validation-gate-9B", self.f)
        with self.assertRaises(ValueError): sa.append(self.j, "tuning-freeze", self.d / "nope")
        self.assertEqual(sa.verify_chain(self.j), 63)
    def test_tampered_chain_refused_before_and_after(self):
        lines = self.j.read_bytes().splitlines(keepends=True); r = json.loads(lines[30]); r["observed_digest"] = "0" * 64
        lines[30] = sa.canonical_bytes(r); self.j.write_bytes(b"".join(lines))
        with self.assertRaises(ValueError) as c: sa.verify_chain(self.j)
        self.assertIn("line 31", str(c.exception))
        with self.assertRaises(ValueError): sa.append(self.j, "tuning-freeze", self.f)
    def test_empty_journal_starts_at_zero_digest(self):
        e = self.d / "empty.jsonl"; ev = sa.append(e, "corpus-identity-freeze", self.f)
        self.assertEqual(ev["predecessor_receipt_digest"], "0" * 64); self.assertEqual(sa.verify_chain(e), 1)
    def test_cli_verify_and_refusal(self):
        self.assertEqual(sa.main(["verify", "--journal", str(self.j)]), 0)
        self.assertEqual(sa.main(["append", "--journal", str(self.j), "--operation", "tuning-freeze", "--file", str(self.d / "nope")]), 2)
if __name__ == "__main__": unittest.main()
