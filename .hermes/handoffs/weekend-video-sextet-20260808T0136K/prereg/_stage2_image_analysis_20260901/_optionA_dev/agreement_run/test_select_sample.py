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

    def test_insufficient_population_refused(self):
        """POSITIVE-REGRESSION: an insufficient post-exclusion population refuses."""
        inputs = self.make_inputs(self.eligible[:2899], self.excluded, self.failed)
        with self.assertRaises(ValueError):
            select(*inputs, self.seed)

    def test_digest_mismatch_refused(self):
        """POSITIVE-REGRESSION: each of the three input pins is mandatory and verified."""
        for index, name in ((1, "eligible"), (3, "exclusion"), (5, "failed")):
            with self.subTest(input=name):
                inputs = list(self.inputs)
                inputs[index] = "0" * 64
                with self.assertRaisesRegex(ValueError, "^" + name + ": SHA256 mismatch:"):
                    select(*inputs, self.seed)

    def test_tuning_scored_floor_sufficient_draw_short_refused(self):
        """POSITIVE-REGRESSION: tuning meeting its scored-count floor cannot permit a short draw."""
        inputs = self.make_inputs(self.eligible[:780], self.excluded, self.failed)
        with self.assertRaisesRegex(
                ValueError,
                r"^tuning draw size shortfall: 20 "
                r"\(eligible population after exclusions 380, "
                r"remaining 380, requested 400\)$"):
            select(*inputs, self.seed)

    def test_holdout_scored_floor_sufficient_draw_short_refused(self):
        """POSITIVE-REGRESSION: holdout meeting its scored-count floor cannot permit a short draw."""
        inputs = self.make_inputs(self.eligible[:990], self.excluded, self.failed)
        with self.assertRaisesRegex(
                ValueError,
                r"^holdout draw size shortfall: 10 "
                r"\(eligible population after exclusions 590, "
                r"remaining 190, requested 200\)$"):
            select(*inputs, self.seed)

    def test_validation_scored_floor_sufficient_draw_short_refused(self):
        """POSITIVE-REGRESSION: validation meeting its scored-count floor cannot permit a short draw."""
        inputs = self.make_inputs(self.eligible[:2900], self.excluded, self.failed)
        with self.assertRaisesRegex(
                ValueError,
                r"^validation draw size shortfall: 100 "
                r"\(eligible population after exclusions 2500, "
                r"remaining 1900, requested 2000\)$"):
            select(*inputs, self.seed)

    def test_overlapping_exclusion_failed_refused(self):
        """POSITIVE-REGRESSION: exclusion and failed sets sharing an eligible ID refuse and name it."""
        inputs = self.make_inputs(self.eligible, self.excluded,
                                  [self.excluded[-1], *self.failed])
        with self.assertRaisesRegex(ValueError, r"^exclusion/failed overlap: 100199$"):
            select(*inputs, self.seed)

    def test_nonmember_excluded_id_tolerated_and_counted(self):
        """FAIL-FIRST: an excluded ID outside eligibility is tolerated and counted."""
        inputs = self.make_inputs(self.eligible, [99999, *self.excluded], self.failed)
        result = select(*inputs, self.seed)
        self.assertEqual(result["counts"]["exclusion_nonmembers"], 1)

    def test_nonmember_failed_id_tolerated_and_counted(self):
        """FAIL-FIRST: failed IDs outside eligibility are tolerated and counted as unique IDs."""
        inputs = self.make_inputs(self.eligible, self.excluded,
                                  [99998, 99997, 99998, *self.failed])
        result = select(*inputs, self.seed)
        self.assertEqual(result["counts"]["failed_nonmembers"], 2)

    def test_nonmembers_never_appear_in_any_split(self):
        """FAIL-FIRST: neither historical nonmembers nor eligible excluded IDs enter any split."""
        excluded = [99999, *self.excluded]
        failed = [99998, *self.failed]
        inputs = self.make_inputs(self.eligible, excluded, failed)
        result = select(*inputs, self.seed)
        selected = set(result["tuning"] + result["holdout"] + result["validation"])
        self.assertEqual(selected & set(excluded + failed), set())

    def test_nonmember_overlap_still_refused(self):
        """POSITIVE-REGRESSION: overlap outside eligibility still refuses and names the ID."""
        inputs = self.make_inputs(self.eligible, [99999, *self.excluded],
                                  [99999, *self.failed])
        with self.assertRaisesRegex(ValueError, r"^exclusion/failed overlap: 99999$"):
            select(*inputs, self.seed)

    def test_invalid_eligible_order_refused(self):
        """POSITIVE-REGRESSION: descending or duplicate eligible IDs still refuse."""
        for eligible in (self.eligible[::-1], [self.eligible[0], *self.eligible]):
            with self.subTest(eligible_prefix=eligible[:2]):
                inputs = self.make_inputs(eligible, self.excluded, self.failed)
                with self.assertRaisesRegex(ValueError, "ascending without duplicates"):
                    select(*inputs, self.seed)


if __name__ == "__main__":
    unittest.main()
