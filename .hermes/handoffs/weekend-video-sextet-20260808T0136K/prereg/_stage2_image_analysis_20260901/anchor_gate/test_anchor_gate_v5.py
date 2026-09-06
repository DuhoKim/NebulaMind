import hashlib
import math
import tempfile
import unittest
from pathlib import Path

from anchor_gate import blind_guard
from anchor_gate.renderer_parity_fixture_v5 import (RendererParityFixtureFailure,
                                                    synthetic_wcs_reproject, validate_geometry)
from anchor_gate.instrument_identity_v4 import (InstrumentIdentityFailure, make_event,
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

    def test_reference_battery_is_retired_not_merely_unused(self):
        """V20 retired the reference-implementation battery. Assert the EXACT
        retirement: the harness must expose no fixture-output contract, must not
        name the retired token, and must not invoke the excluded script."""
        import inspect
        from anchor_gate import renderer_parity_fixture_v5 as rpf
        self.assertFalse(hasattr(rpf, "validate_fixture_output"))
        src = inspect.getsource(rpf)
        for retired in ("ABSOLUTE-ANCHOR-FAIL", "BATTERY-SIGN", "successor_ref", "subprocess"):
            self.assertNotIn(retired, src)

    def test_fixture_still_passes_end_to_end(self):
        """Deletion probe: retiring the battery must not leave the fixture inert."""
        from anchor_gate import renderer_parity_fixture_v5 as rpf
        result = rpf.validate_geometry()
        self.assertEqual(result["jacobian_parity"], "PRESERVED")

    def test_wrong_parity_literal_token(self):
        self.assertEqual(synthetic_wcs_reproject(source_jacobian=((-1.,0.),(0.,1.))),"WRONG-PARITY-REFUSAL")

    def test_bs4_fiducials_run_through_renderer(self):
        result = validate_geometry()
        self.assertEqual(result["jacobian_parity"], "PRESERVED")
        self.assertIn("renderer_digest", result)

    def test_bs4_zero_nexp_is_carried_negative_refuses(self):
        # V37 §8.12: zero exposure is CARRIED through the harness (renderer_v4); the v4 harness/test asserted a refusal here
        synthetic_wcs_reproject(nexp_value=0)
        with self.assertRaises(ValueError):
            synthetic_wcs_reproject(nexp_value=-1)
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


class TestEnvironmentRecordCannotBeFabricated(unittest.TestCase):
    """V20-V26: capture_environment wrote the renderer's NumPy-only runtime into the
    record TWICE, validate_environment checked neither torch nor astropy nor interpreter
    separation, and the runner digest was a constant. A referee ran the fixture and
    proved a reachable false PASS. Each test below is one of those holes, asserted shut."""

    def _good(self):
        from anchor_gate import instrument_identity_v4 as ii
        w, r = ii.verify_instrument()
        return ii.capture_environment(w, r)

    def test_positive_control_the_real_environments_validate(self):
        from anchor_gate import instrument_identity_v4 as ii
        rec = ii.validate_environment(self._good())
        self.assertIn("torch", rec["instrument_environment"]["package_versions"])
        self.assertIn("astropy", rec["renderer_environment"]["package_versions"])
        self.assertNotEqual(rec["instrument_environment"]["interpreter"],
                            rec["renderer_environment"]["interpreter"])

    def test_numpy_only_instrument_environment_is_refused(self):
        from anchor_gate import instrument_identity_v4 as ii
        rec = self._good(); rec["instrument_environment"]["package_versions"] = {"numpy": "1.26.4"}
        with self.assertRaisesRegex(ii.InstrumentIdentityFailure, "lacks torch"):
            ii.validate_environment(rec)

    def test_renderer_environment_without_astropy_is_refused(self):
        from anchor_gate import instrument_identity_v4 as ii
        rec = self._good(); rec["renderer_environment"]["package_versions"] = {"numpy": "1.26.4"}
        with self.assertRaisesRegex(ii.InstrumentIdentityFailure, "lacks astropy"):
            ii.validate_environment(rec)

    def test_a_shared_interpreter_is_refused(self):
        """The exact V20 record: the same interpreter written into both slots."""
        from anchor_gate import instrument_identity_v4 as ii
        rec = self._good(); rec["instrument_environment"]["interpreter"] = rec["renderer_environment"]["interpreter"]
        with self.assertRaisesRegex(ii.InstrumentIdentityFailure, "share an interpreter"):
            ii.validate_environment(rec)

    def test_the_runner_is_hashed_not_asserted(self):
        from anchor_gate import instrument_identity_v4 as ii
        import tempfile, pathlib
        bad = pathlib.Path(tempfile.mkdtemp()) / "inference_runner.py"; bad.write_text("# tampered\n")
        with self.assertRaisesRegex(ii.InstrumentIdentityFailure, "runner sha256 mismatch"):
            ii.verify_instrument(runner=bad)

    def test_an_absent_venv_is_a_failure_not_a_fabrication(self):
        from anchor_gate import instrument_identity_v4 as ii
        import pathlib
        with self.assertRaisesRegex(ii.InstrumentIdentityFailure, "venv_torch interpreter absent"):
            ii._instrument_runtime(pathlib.Path("/nonexistent/venv/bin/python"))

    def test_the_pinned_schema_itself_requires_torch_and_astropy(self):
        """Prose 'MUST include' is not a constraint; JSON-Schema `required` is."""
        import json
        from anchor_gate import instrument_identity_v4 as ii
        sch = json.loads(ii.SCHEMA.read_text())
        self.assertIn("torch", sch["properties"]["instrument_environment"]["properties"]["package_versions"]["required"])
        self.assertIn("astropy", sch["properties"]["renderer_environment"]["properties"]["package_versions"]["required"])


class TestStandaloneEventPath(unittest.TestCase):
    def test_make_event_with_no_supplied_environment_captures_and_validates(self):
        """V27 shipped make_event() assigning verify_instrument's TUPLE to `digest` and
        calling capture_environment(digest) with one argument: an uncaught TypeError on
        the standalone path. The fixture path was adapted; this one was not. Found by a
        referee running the pinned module as a program."""
        import tempfile, pathlib
        from anchor_gate import instrument_identity_v4 as ii
        j = pathlib.Path(tempfile.mkdtemp()) / "journal.jsonl"; j.write_bytes(b"")
        ev = ii.make_event(journal=j, environment=None)
        self.assertEqual(ev["observed_digest"], ii.PIN)
        self.assertEqual(ev["observed_runner_digest"], ii.RUNNER_PIN)
        self.assertIn("torch", ev["environment"]["instrument_environment"]["package_versions"])


if __name__ == "__main__": unittest.main()
