import hashlib
import math
import subprocess
import tempfile
import unittest
from pathlib import Path

from anchor_gate import blind_guard
from anchor_gate.bs4_anchor import (AbsoluteAnchorFailure, synthetic_wcs_reproject,
                                    validate_fixture_output, validate_geometry)
from anchor_gate.instrument_identity import (InstrumentIdentityFailure, make_event,
                                             validate_environment)
from seal_gate.seal_gate import _seal_predecessor, canonical_bytes, sha256_bytes


def _fixture_pin(tmp_path, ra=0.0, dec=0.0):
    path = tmp_path / "protected.csv"
    path.write_text(f"ls_id,brickid,objid,ra,dec,shape_e1,shape_e2\n99,7,8,{ra},{dec},0,0\n")
    return {path: (hashlib.sha256(path.read_bytes()).hexdigest(), 1)}


class AnchorGateTests(unittest.TestCase):
    def tmp(self):
        return Path(tempfile.mkdtemp())

    def test_instrument_sha_mismatch_refuses(self):
        tmp_path=self.tmp(); bad=tmp_path/"instrument.py"; bad.write_bytes(b"synthetic mismatch\n")
        with self.assertRaisesRegex(InstrumentIdentityFailure,"^INSTRUMENT-INTEGRITY-FAIL: instrument sha256 mismatch$"):
            make_event(journal=tmp_path/"empty.jsonl",instrument_path=bad)

    def test_environment_extra_field_refuses(self):
        record={"python_version":"3.9.6","package_versions":{"numpy":"1.26.4"},
            "os":{"system":"x","release":"x","version":"x","machine":"x"},
            "frozen_instrument_sha256":"6a9abbbd900db882b804149edd6d2b8d1780b7114b191e1a58457d7e5875c148","extra":"forbidden"}
        with self.assertRaisesRegex(InstrumentIdentityFailure,"^INSTRUMENT-INTEGRITY-FAIL: environment schema violation$"):
            validate_environment(record)

    def test_bs4_missing_battery_sign_refuses(self):
        with self.assertRaisesRegex(AbsoluteAnchorFailure,"^ABSOLUTE-ANCHOR-FAIL: fixture output contract$"):
            validate_fixture_output(subprocess.CompletedProcess([],0,"ALL FIXTURES PASS\n",""))

    def test_wrong_parity_literal_token(self):
        self.assertEqual(synthetic_wcs_reproject(source_jacobian=((-1.,0.),(0.,1.))),"WRONG-PARITY-REFUSAL")

    def test_bs4_fiducials_run_through_renderer(self):
        result = validate_geometry()
        self.assertEqual(result["jacobian_parity"], "PRESERVED")
        self.assertIn("renderer_digest", result)

    def test_blind_guard_exactly_one_arcsec_refuses(self):
        pins=_fixture_pin(self.tmp())
        receipt=blind_guard.guard([{"ra":0.,"dec":1./3600.}],protected_paths=pins)
        self.assertEqual(receipt["status"],"REFUSE")

    def test_blind_guard_one_step_inside_refuses(self):
        pins=_fixture_pin(self.tmp()); boundary=math.nextafter(1./3600.,-math.inf)
        self.assertEqual(blind_guard.guard([{"ra":0.,"dec":boundary}],protected_paths=pins)["status"],"REFUSE")

    def test_blind_guard_one_step_outside_passes(self):
        pins=_fixture_pin(self.tmp()); boundary=math.nextafter(1./3600.,math.inf)
        self.assertEqual(blind_guard.guard([{"ra":0.,"dec":boundary}],protected_paths=pins)["status"],"PASS")

    def test_blind_guard_identity_match_refuses(self):
        pins=_fixture_pin(self.tmp())
        self.assertEqual(blind_guard.guard([{"ls_id":99,"ra":180.,"dec":80.}],protected_paths=pins)["status"],"REFUSE")

    def test_seal_journal_chaining_real_format_temp_copy(self):
        tmp_path=self.tmp(); live=Path(__file__).resolve().parent.parent/"seal_journal_tierc.jsonl"
        journal=tmp_path/"seal_journal_tierc.jsonl"; journal.write_bytes(live.read_bytes())
        body={"timestamp":"2026-09-03T00:00:00Z","operation":"synthetic-test","status":"PASS",
              "predecessor_receipt_digest":_seal_predecessor(journal)}
        body["receipt_digest"]=sha256_bytes(canonical_bytes(body))
        with journal.open("ab") as stream: stream.write(canonical_bytes(body))
        self.assertEqual(_seal_predecessor(journal),body["receipt_digest"])


if __name__ == "__main__": unittest.main()
