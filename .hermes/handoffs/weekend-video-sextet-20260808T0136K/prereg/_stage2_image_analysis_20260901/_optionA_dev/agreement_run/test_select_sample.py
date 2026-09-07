"""Synthetic-only regression checks for the trimmed selection function."""

import hashlib
from pathlib import Path
import tempfile
import unittest

from select_sample import select


class SelectSampleTests(unittest.TestCase):
    def setUp(self):
        self.directory = tempfile.TemporaryDirectory()
        self.addCleanup(self.directory.cleanup)
        self.root = Path(self.directory.name)
        self.seed = "a1" * 32
        self.eligible = list(range(100000, 103000))
        self.excluded = self.eligible[:200]
        self.failed = self.eligible[200:400]
        self.inputs = self.make_inputs(self.eligible, self.excluded, self.failed)

    def make_inputs(self, eligible, excluded, failed):
        args = []
        for name, ids in (("eligible", eligible), ("excluded", excluded), ("failed", failed)):
            raw = "".join(f"{objid}\n" for objid in ids).encode("ascii")
            path = self.root / (name + ".txt")
            path.write_bytes(raw)
            args.extend((path, hashlib.sha256(raw).hexdigest()))
        return args

    def test_determinism(self):
        """POSITIVE-REGRESSION: identical pinned inputs and seed reproduce the entire result."""
        self.assertEqual(select(*self.inputs, self.seed), select(*self.inputs, self.seed))

    def test_different_seed_changes_tuning(self):
        """POSITIVE-REGRESSION: changing the seed changes tuning membership."""
        first = select(*self.inputs, self.seed)
        second = select(*self.inputs, "b2" * 32)
        self.assertNotEqual(set(first["tuning"]), set(second["tuning"]))

    def test_three_way_disjointness(self):
        """POSITIVE-REGRESSION: every pair of selected splits has empty intersection."""
        result = select(*self.inputs, self.seed)
        tuning, holdout, validation = (set(result[name]) for name in
                                       ("tuning", "holdout", "validation"))
        self.assertEqual((tuning & holdout, tuning & validation, holdout & validation),
                         (set(), set(), set()))

    def test_exclusion_and_failed_applied(self):
        """POSITIVE-REGRESSION: the complete surviving population excludes both burnt sets."""
        result = select(*self.inputs, self.seed)
        selected = set(result["tuning"] + result["holdout"] + result["validation"])
        self.assertEqual(selected, set(self.eligible) - set(self.excluded) - set(self.failed))

    def test_exact_sizes(self):
        """POSITIVE-REGRESSION: the default draw fills all three target sizes."""
        result = select(*self.inputs, self.seed)
        self.assertEqual(tuple(len(result[name]) for name in
                               ("tuning", "holdout", "validation")), (400, 200, 2000))

    def test_floor_shortfall_refused(self):
        """POSITIVE-REGRESSION: validation one below its floor refuses with the exact deficit."""
        inputs = self.make_inputs(self.eligible[:2899], self.excluded, self.failed)
        with self.assertRaisesRegex(ValueError,
                                    r"^validation floor shortfall: 1 \(available 1899, floor 1900\)$"):
            select(*inputs, self.seed)

    def test_digest_mismatch_refused(self):
        """POSITIVE-REGRESSION: each of the three input pins is mandatory and verified."""
        for index, name in ((1, "eligible"), (3, "exclusion"), (5, "failed")):
            with self.subTest(input=name):
                inputs = list(self.inputs)
                inputs[index] = "0" * 64
                with self.assertRaisesRegex(ValueError, "^" + name + ": SHA256 mismatch:"):
                    select(*inputs, self.seed)


if __name__ == "__main__":
    unittest.main()
