import csv
import gzip
import math
import random
import tempfile
import time
import unittest
from pathlib import Path

from completeness_gate import (
    Candidate, GateError, GZRecord, InMemoryCandidateSource, Position,
    PARENT_ARCSEC, TIER_A_ARCSEC, PositionIndex, _within_linear,
    parse_dec, parse_ra, read_gz_tables, run_gate, separation_arcsec,
)


def gz(index, objid, ra=10.0, dec=0.0, cw=0.9, acw=0.1):
    return GZRecord(index, objid, ra, dec, cw, acw)


def cand(objid, ra=10.0, dec=0.0, brickid=1):
    return Candidate(9010, brickid, objid, ra, dec, "0100p000")


def gate(records, candidates=(), a=(), parent=(), prior=()):
    return run_gate(records, a, parent, InMemoryCandidateSource(candidates), prior,
                    input_digests={"table2": "a", "table3": "b"},
                    expected_rows=len(records), expected_prior=len(prior))


class ParserTests(unittest.TestCase):
    def test_declination_sign_applies_to_whole_quantity(self):
        self.assertEqual(parse_dec("-01:30:00"), -1.5)
        self.assertEqual(parse_dec("+01:30:00"), 1.5)

    def test_ra_wrap_and_invalid_24_hours(self):
        self.assertAlmostEqual(parse_ra("23:59:59.9"), 359.99958333333336)
        with self.assertRaisesRegex(GateError, r"^DATA-INTEGRITY-FAIL: RA sexagesimal component out of range$"):
            parse_ra("24:00:00")

    def test_parser_requires_printed_dec_sign(self):
        with self.assertRaisesRegex(GateError, r"^DATA-INTEGRITY-FAIL: DEC lacks printed leading sign$"):
            parse_dec("01:00:00")

    def test_csv_duplicate_is_checked_by_gate(self):
        with tempfile.TemporaryDirectory() as td:
            p = Path(td) / "g.csv"
            with p.open("w", newline="") as f:
                w = csv.writer(f); w.writerow(["OBJID", "RA", "DEC", "P_CW", "P_ACW"])
                w.writerow([7, "00:00:00", "+00:00:00", .9, .1])
                w.writerow([7, "00:00:01", "+00:00:00", .9, .1])
            rows = read_gz_tables([p])
            with self.assertRaisesRegex(GateError, r"^DATA-INTEGRITY-FAIL: duplicate GZ1 OBJID: 7$"):
                gate(rows)

    def test_official_gzip_csv_is_parsed(self):
        with tempfile.TemporaryDirectory() as td:
            p = Path(td) / "g.csv.gz"
            with gzip.open(p, "wt", newline="") as f:
                w = csv.writer(f); w.writerow(["OBJID", "RA", "DEC", "P_CW", "P_ACW"])
                w.writerow([8, "00:00:00", "+00:00:00", .8, .1])
            self.assertEqual(read_gz_tables([p])[0].objid, 8)


class MatchTests(unittest.TestCase):
    def test_ra_wrap_great_circle(self):
        self.assertAlmostEqual(separation_arcsec(359.9999, 0, 0.0001, 0), 0.72, places=8)

    def test_equality_at_one_arcsecond_is_inclusive(self):
        rows = [gz(0, 1, ra=0, dec=0)]
        pairs, receipt = gate(rows, [cand(11, ra=0, dec=1.0 / 3600.0)])
        self.assertEqual(len(pairs), 1)
        self.assertEqual(receipt["funnel_counts"]["one_dr10"], 1)

    def test_zero_one_two_candidates(self):
        rows = [gz(0, 1, ra=10), gz(1, 2, ra=20), gz(2, 3, ra=30)]
        cs = [cand(21, ra=20), cand(31, ra=30), cand(32, ra=30, brickid=2)]
        pairs, receipt = gate(rows, cs)
        self.assertEqual([p.gz1_objid for p in pairs], [2])
        self.assertEqual((receipt["funnel_counts"]["no_dr10"],
                          receipt["funnel_counts"]["one_dr10"],
                          receipt["funnel_counts"]["multiple_dr10"]), (1, 1, 1))

    def test_gz_collision_excludes_all_owners(self):
        rows = [gz(0, 1, ra=10), gz(1, 2, ra=10.0001)]
        pairs, receipt = gate(rows, [cand(40, ra=10.00005)])
        self.assertEqual(pairs, [])
        self.assertEqual(receipt["funnel_counts"]["collision"], 2)

    def test_backend_duplicate_candidate_refused(self):
        c = cand(50)
        with self.assertRaisesRegex(GateError, r"^COMPLETENESS-FAIL: backend returned duplicate DR10 candidate for GZ1 OBJID 1$"):
            gate([gz(0, 1)], [c, c])


class PositionIndexTests(unittest.TestCase):
    @staticmethod
    def synthetic():
        rng = random.Random(20260903)
        positions = [Position(str(i), rng.random() * 360.0,
                              math.degrees(math.asin(rng.uniform(-1.0, 1.0))))
                     for i in range(20_000)]
        positions.extend((Position("wrap-west", math.nextafter(360.0, 0.0), 0.0),
                          Position("wrap-east", 0.0, 0.0),
                          Position("north", 123.0, 89.99),
                          Position("south", 321.0, -89.99)))
        records = [gz(i, i, rng.random() * 360.0,
                      math.degrees(math.asin(rng.uniform(-1.0, 1.0))))
                   for i in range(256)]
        records.extend((gz(len(records), 900001, 0.0, 0.0),
                        gz(len(records) + 1, 900002, 123.0, 89.99),
                        gz(len(records) + 2, 900003, 321.0, -89.99)))
        return positions, records

    def test_indexed_equals_linear_on_20000_positions(self):
        positions, records = self.synthetic()
        index = PositionIndex(positions)
        for radius in (TIER_A_ARCSEC, PARENT_ARCSEC):
            self.assertEqual(radius, 1.0)
            for record in records:
                self.assertEqual(index.within(record, radius),
                                 _within_linear(record, positions, radius))

    def test_exact_one_arcsec_and_adjacent_binary64_values(self):
        exact = 1.0 / 3600.0
        inside = math.nextafter(exact, 0.0)
        outside = math.nextafter(exact, math.inf)
        positions = [Position("exact", 10.0, exact),
                     Position("inside", 20.0, inside),
                     Position("outside", 30.0, outside)]
        index = PositionIndex(positions)
        records = [gz(0, 1, 10.0, 0.0), gz(1, 2, 20.0, 0.0), gz(2, 3, 30.0, 0.0)]
        self.assertEqual(separation_arcsec(10.0, 0.0, 10.0, exact), 1.0)
        self.assertLess(separation_arcsec(20.0, 0.0, 20.0, inside), 1.0)
        self.assertGreater(separation_arcsec(30.0, 0.0, 30.0, outside), 1.0)
        for radius in (TIER_A_ARCSEC, PARENT_ARCSEC):
            got = [index.within(record, radius) for record in records]
            expected = [_within_linear(record, positions, radius) for record in records]
            self.assertEqual(got, expected)
            self.assertEqual(got, [True, True, False])

    def test_timing_100k_records(self):
        positions, seed_records = self.synthetic()
        index = PositionIndex(positions)
        records = (seed_records * ((100_000 + len(seed_records) - 1) // len(seed_records)))[:100_000]
        started = time.perf_counter()
        for record in records:
            index.within(record, TIER_A_ARCSEC)
        elapsed = time.perf_counter() - started
        print(f"TIMING_100K: {elapsed:.3f} seconds")
        self.assertLess(elapsed, 120.0)


class TierAndLabelTests(unittest.TestCase):
    def test_equality_at_point_eight_is_inclusive(self):
        pairs, _ = gate([gz(0, 1, cw=.8, acw=.79)], [cand(10)])
        self.assertEqual(pairs[0].label, "CLOCKWISE")

    def test_contradictory_labels_refused_exactly(self):
        with self.assertRaisesRegex(GateError, r"^DATA-INTEGRITY-FAIL: contradictory labels for GZ1 OBJID 9$"):
            gate([gz(0, 9, cw=.8, acw=.8)], [cand(10)])

    def test_tier_priority_a_then_b_then_c(self):
        rows = [gz(0, 1, ra=10), gz(1, 2, ra=20), gz(2, 3, ra=30)]
        a = [Position("a", 10, 0)]
        parent = [Position("also-a", 10, 0), Position("b", 20, 0)]
        pairs, receipt = gate(rows, [cand(101, 10), cand(102, 20), cand(103, 30)], a, parent)
        self.assertEqual([p.gz1_objid for p in pairs], [3])
        self.assertEqual(receipt["terminal_dispositions"][1], "TIER-A-EXCLUDED")
        self.assertEqual(receipt["terminal_dispositions"][2], "TIER-B-EXCLUDED")
        self.assertNotIn(1, [p.gz1_objid for p in pairs])

    def test_canonical_pair_sort_uses_integer_keys(self):
        rows = [gz(0, 20, ra=20), gz(1, 3, ra=3), gz(2, 11, ra=11)]
        pairs, _ = gate(rows, [cand(2, 20, brickid=20), cand(3, 3, brickid=3), cand(1, 11, brickid=11)])
        self.assertEqual([p.gz1_objid for p in pairs], [3, 11, 20])


class ReceiptTests(unittest.TestCase):
    def test_required_receipt_fields_present(self):
        _, r = gate([gz(0, 1)], [cand(1)], prior=[1])
        expected = {"input_digests", "dr10_release_identity", "query_export_artifacts",
                    "software_environment", "match_radius_arcsec", "funnel_counts",
                    "rows_considered_exactly_once", "prior_unresolved_terminal",
                    "candidate_enumeration", "pair_sha256"}
        self.assertTrue(expected.issubset(r))
        self.assertEqual(r["prior_unresolved_terminal"],
                         [{"gz1_objid": 1, "disposition": "ONE-DR10-WITHIN-1ARCSEC"}])

    def test_missing_prior_unresolved_position_refused_exactly(self):
        with self.assertRaisesRegex(GateError, r"^COMPLETENESS-FAIL: prior-unresolved OBJID lacks terminal disposition: 99$"):
            gate([gz(0, 1)], prior=[99])

    def test_row_once_gap_refused_exactly(self):
        with self.assertRaisesRegex(GateError, r"^COMPLETENESS-FAIL: GZ1 input_index coverage is not exactly once$"):
            gate([gz(1, 1)])


if __name__ == "__main__":
    unittest.main(verbosity=2)
