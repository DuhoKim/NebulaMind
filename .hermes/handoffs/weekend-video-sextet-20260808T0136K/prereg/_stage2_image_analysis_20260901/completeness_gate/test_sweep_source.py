import json
import math
import tempfile
import unittest
from pathlib import Path

from astropy.io import fits

from completeness_gate import GateError, GZRecord, separation_arcsec, sha256_file
from sweep_source import FITS_LIB, SweepCandidateSource
from tap_source import TAPCandidateSource


class SweepSourceTest(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.root = Path(self.tmp.name)
        self.sweeps = self.root / "sweeps"
        self.sweeps.mkdir()
        self.manifest = self.root / "manifest.json"
        self.receipts = self.root / "receipts.jsonl"
        self.artifacts = self.root / "artifacts"

    def tearDown(self):
        self.tmp.cleanup()

    def write_sweep(self, name, rows):
        columns = [
            fits.Column(name="RELEASE", format="K", array=[r[0] for r in rows]),
            fits.Column(name="BRICKID", format="J", array=[r[1] for r in rows]),
            fits.Column(name="OBJID", format="J", array=[r[2] for r in rows]),
            fits.Column(name="BRICKNAME", format="8A", array=[r[3] for r in rows]),
            fits.Column(name="RA", format="D", array=[r[4] for r in rows]),
            fits.Column(name="DEC", format="D", array=[r[5] for r in rows]),
            # A forbidden science column demonstrates that it is not required.
            fits.Column(name="FLUX_R", format="E", array=[99.0 for _ in rows]),
        ]
        fits.BinTableHDU.from_columns(columns).writeto(self.sweeps / name)

    def configure(self, entries, receipt_names=None):
        files = []
        for name, box in entries:
            files.append({"filename": name, "box": box,
                          "published_sha256": sha256_file(self.sweeps / name)})
        self.manifest.write_text(json.dumps({"version": 1, "files": files}) + "\n")
        selected = {x[0] for x in entries} if receipt_names is None else set(receipt_names)
        self.receipts.write_text("".join(
            json.dumps({"filename": f["filename"], "status": "OK",
                        "sha256": f["published_sha256"]}) + "\n"
            for f in files if f["filename"] in selected))

    def source(self):
        return SweepCandidateSource(self.sweeps, self.manifest,
                                    self.receipts, self.artifacts)

    def boundary_fixture(self):
        left, right = "left.fits", "right.fits"
        self.write_sweep(left, [])
        self.write_sweep(right, [(9010, 8, 12, "0050p000", 5.00005, 0.0)])
        self.configure([
            (left, {"ra_min_deg": 0, "ra_max_deg": 5,
                    "dec_min_deg": -5, "dec_max_deg": 0}),
            (right, {"ra_min_deg": 5, "ra_max_deg": 10,
                     "dec_min_deg": -5, "dec_max_deg": 0}),
        ])

    def test_boundary_margin_consults_both_boxes_and_finds_candidate_once(self):
        self.boundary_fixture()
        record = GZRecord(0, 1, 4.99995, 0.0, .9, .1)
        source = self.source()
        meta = source.run_chunk(0, [record])
        self.assertEqual([x["filename"] for x in meta["consulted_sweeps"]],
                         ["left.fits", "right.fits"])
        self.assertEqual([c.identity for c in source.candidates(record, 1.0)],
                         [(9010, 8, 12)])

    def test_equality_at_one_arcsec_is_accepted(self):
        name = "one.fits"
        dec = 1.0 / 3600.0
        while separation_arcsec(10.0, 0.0, 10.0, dec) > 1.0:
            dec = math.nextafter(dec, 0.0)
        self.assertEqual(separation_arcsec(10.0, 0.0, 10.0, dec), 1.0)
        self.write_sweep(name, [(9010, 1, 2, "0100p000", 10.0, dec)])
        self.configure([(name, {"ra_min_deg": 5, "ra_max_deg": 15,
                                "dec_min_deg": -5, "dec_max_deg": 5})])
        record = GZRecord(0, 1, 10.0, 0.0, .9, .1)
        source = self.source(); source.run_chunk(0, [record])
        self.assertEqual(len(source.candidates(record, 1.0)), 1)

    def test_missing_receipt_sweep_refuses_without_checkpoint(self):
        name = "one.fits"
        self.write_sweep(name, [])
        self.configure([(name, {"ra_min_deg": 0, "ra_max_deg": 5,
                                "dec_min_deg": -5, "dec_max_deg": 0})], [])
        with self.assertRaisesRegex(GateError, "lacks an OK receipt"):
            self.source().run_chunk(0, [GZRecord(0, 1, 1, -1, .9, .1)])
        self.assertFalse((self.artifacts / "checkpoint.jsonl").exists())

    def test_on_disk_sha_mismatch_refuses(self):
        name = "one.fits"
        self.write_sweep(name, [])
        self.configure([(name, {"ra_min_deg": 0, "ra_max_deg": 5,
                                "dec_min_deg": -5, "dec_max_deg": 0})])
        with (self.sweeps / name).open("ab") as stream:
            stream.write(b"changed")
        with self.assertRaisesRegex(GateError, "on-disk sweep sha256 mismatch"):
            self.source().run_chunk(0, [GZRecord(0, 1, 1, -1, .9, .1)])

    def test_candidate_is_attributed_to_both_positions(self):
        name = "one.fits"
        self.write_sweep(name, [(9010, 1, 2, "0100p000", 10.0, 0.0)])
        self.configure([(name, {"ra_min_deg": 5, "ra_max_deg": 15,
                                "dec_min_deg": -5, "dec_max_deg": 5})])
        records = [GZRecord(7, 10, 10.0, 0.0, .9, .1),
                   GZRecord(8, 11, 10.0001, 0.0, .9, .1)]
        source = self.source(); source.run_chunk(0, records)
        self.assertEqual([len(source.candidates(r, 1.0)) for r in records], [1, 1])

    def test_candidate_sets_match_tap_admission_on_same_catalogue(self):
        name = "one.fits"
        rows = [(9010, 1, 2, "0100p000", 10.0, 0.0),
                (9010, 1, 3, "0100p000", 10.0001, 0.0),
                (9010, 1, 4, "0100p000", 20.0, 0.0)]
        self.write_sweep(name, rows)
        self.configure([(name, {"ra_min_deg": 5, "ra_max_deg": 25,
                                "dec_min_deg": -5, "dec_max_deg": 5})])
        records = [GZRecord(0, 10, 10.0, 0.0, .9, .1),
                   GZRecord(1, 11, 10.0001, 0.0, .9, .1)]
        local = self.source(); local.run_chunk(0, records)
        tap = TAPCandidateSource("https://invalid/sync", "synthetic", [],
                                 self.root / "tap")
        tap._admit_rows([
            {"input_index": "0", "release": str(r[0]), "brickid": str(r[1]),
             "objid": str(r[2]), "brickname": r[3], "ra": str(r[4]),
             "dec": str(r[5])} for r in rows[:2]], records)
        for record in records:
            self.assertEqual({c.identity for c in local.candidates(record, 1.0)},
                             {c.identity for c in tap.candidates(record, 1.0)})

    def test_checkpoint_resume_and_provenance_bind_proof(self):
        self.boundary_fixture()
        record = GZRecord(0, 1, 4.99995, 0.0, .9, .1)
        self.source().run_chunk(0, [record])
        resumed = self.source(); meta = resumed.run_chunk(0, [record])
        self.assertTrue(meta["resumed"])
        self.assertEqual(len(resumed.provenance["query_artifacts"][0]
                             ["consulted_sweeps"]), 2)
        self.assertTrue(FITS_LIB.startswith(("astropy ", "fitsio ")))


if __name__ == "__main__":
    unittest.main(verbosity=2)
