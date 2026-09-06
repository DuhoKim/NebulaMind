import json, unittest, tempfile, sys, hashlib
from pathlib import Path
HERE = Path(__file__).resolve().parent; sys.path.insert(0, str(HERE)); import history as H
class T(unittest.TestCase):
    def setUp(self): self.p = Path(tempfile.mkdtemp()) / "h.jsonl"
    def test_genesis_chain_validate_and_tamper(self):
        H.genesis(self.p, "a" * 64, "2026-09-07T01:11:00Z", "b" * 64, 6443748)
        with self.assertRaises(SystemExit): H.genesis(self.p, "a" * 64, "x", "b" * 64, 1)          # cannot re-initiate
        H.append(self.p, {"stage": "collector-collect", "record_sha256": "c" * 64, "outcome": "ACCEPT-DRAND", "seed_hex": "d" * 64})
        H.append(self.p, {"stage": "builder-verdict", "record_sha256": "c" * 64, "outcome": "ACCEPT-DRAND", "seed_hex": "d" * 64})
        H.append(self.p, {"stage": "builder-accept", "record_sha256": "c" * 64, "outcome": "ACCEPT-DRAND", "seed_hex": "d" * 64})
        E = H.validate(self.p); self.assertEqual([e["stage"] for e in E], ["genesis", "collector-collect", "builder-verdict", "builder-accept"]); fa, conf = H.first_accept(E); self.assertEqual(fa["stage"], "builder-accept"); self.assertEqual(conf, [])
        lines = self.p.read_bytes().split(b"\n"); lines[1] = lines[1].replace(b'"c' * 1, b'"e', 1); self.p.write_bytes(b"\n".join(lines))
        with self.assertRaises(ValueError) as c: H.validate(self.p)
        self.assertIn("HISTORY-CHAIN-BROKEN", str(c.exception))
    def test_reset_and_reorder_and_unknown_refused(self):
        with self.assertRaises(ValueError): H.validate(self.p)                                        # missing
        self.p.write_text(""); 
        with self.assertRaises(ValueError) as c: H.validate(self.p)
        self.assertIn("HISTORY-EMPTY", str(c.exception))
        self.p.unlink(); H.genesis(self.p, "a" * 64, "t", "b" * 64, 1); H.append(self.p, {"stage": "collector-collect", "outcome": "RETRY"})
        with self.assertRaises(SystemExit): H.append(self.p, {"stage": "made-up"})
        lines = self.p.read_bytes().split(b"\n"); self.p.write_bytes(b"\n".join([lines[1], lines[0], b""]))
        with self.assertRaises(ValueError): H.validate(self.p)
    def test_semantic_conflict_detected(self):
        H.genesis(self.p, "a" * 64, "t", "b" * 64, 1)
        H.append(self.p, {"stage": "builder-accept", "record_sha256": "c" * 64, "outcome": "ACCEPT-DRAND", "seed_hex": "d" * 64})
        H.append(self.p, {"stage": "builder-verdict", "record_sha256": "f" * 64, "outcome": "ACCEPT-DRAND", "seed_hex": "9" * 64})   # a later accept-bearing verdict with a different record: conflict even without the label
        fa, conf = H.first_accept(H.validate(self.p)); self.assertEqual(len(conf), 1)
class T2(unittest.TestCase):
    def test_append_locked_is_atomic_check_then_append(self):
        p = Path(tempfile.mkdtemp()) / "h.jsonl"; H.genesis(p, "a" * 64, "t", "b" * 64, 1)
        def first_accept_only(entries):
            if any(e["stage"] == "builder-accept" for e in entries): raise SystemExit("COLLECTION-LOCKED")
            return {"stage": "builder-accept", "record_sha256": "c" * 64, "outcome": "ACCEPT-DRAND", "seed_hex": "d" * 64}
        self.assertEqual(H.append_locked(p, first_accept_only)["stage"], "builder-accept")
        with self.assertRaises(SystemExit): H.append_locked(p, first_accept_only)
        self.assertEqual(len(H.validate(p)), 2)
if __name__ == "__main__": unittest.main()
