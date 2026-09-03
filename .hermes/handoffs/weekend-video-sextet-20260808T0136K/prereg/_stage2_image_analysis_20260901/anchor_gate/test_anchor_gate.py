import csv
import hashlib
import json
import math
import subprocess
from pathlib import Path

import pytest

from anchor_gate import blind_guard
from anchor_gate.bs4_anchor import (AbsoluteAnchorFailure, WRONG_PARITY,
                                    synthetic_wcs_reproject, validate_fixture_output)
from anchor_gate.instrument_identity import (InstrumentIdentityFailure, make_event,
                                             validate_environment)
from seal_gate.seal_gate import _seal_predecessor, canonical_bytes, sha256_bytes


def test_instrument_sha_mismatch_refuses(tmp_path):
    bad = tmp_path / "instrument.py"
    bad.write_bytes(b"synthetic mismatch\n")
    with pytest.raises(InstrumentIdentityFailure, match="^INSTRUMENT-INTEGRITY-FAIL: instrument sha256 mismatch$"):
        make_event(journal=tmp_path / "empty.jsonl", instrument_path=bad)


def test_environment_extra_field_refuses():
    record = {"python_version": "3.9.6", "package_versions": {"numpy": "1.26.4"},
              "os": {"system": "x", "release": "x", "version": "x", "machine": "x"},
              "frozen_instrument_sha256": "6a9abbbd900db882b804149edd6d2b8d1780b7114b191e1a58457d7e5875c148",
              "extra": "forbidden"}
    with pytest.raises(InstrumentIdentityFailure, match="^INSTRUMENT-INTEGRITY-FAIL: environment schema violation$"):
        validate_environment(record)


def test_bs4_missing_battery_sign_refuses():
    proc = subprocess.CompletedProcess([], 0, "ALL FIXTURES PASS\n", "")
    with pytest.raises(AbsoluteAnchorFailure, match="^ABSOLUTE-ANCHOR-FAIL: fixture output contract$"):
        validate_fixture_output(proc)


def test_wrong_parity_literal_token():
    assert synthetic_wcs_reproject(source_jacobian=((-1.0, 0.0), (0.0, 1.0))) == "WRONG-PARITY-REFUSAL"


def _fixture_pin(tmp_path, ra=0.0, dec=0.0):
    path = tmp_path / "protected.csv"
    path.write_text(f"ls_id,brickid,objid,ra,dec,shape_e1,shape_e2\n99,7,8,{ra},{dec},0,0\n")
    digest = hashlib.sha256(path.read_bytes()).hexdigest()
    return {path: (digest, 1)}


def test_blind_guard_exactly_one_arcsec_refuses(tmp_path):
    pins = _fixture_pin(tmp_path)
    receipt = blind_guard.guard([{"ra": 0.0, "dec": 1.0/3600.0}], protected_paths=pins)
    assert receipt["status"] == "REFUSE"
    assert receipt["reason"] == "VOID-BLIND-VIOLATION"


def test_blind_guard_one_arcsec_plus_one_binary64_step_passes(tmp_path):
    pins = _fixture_pin(tmp_path)
    boundary = 1.0 / 3600.0
    receipt = blind_guard.guard([{"ra": 0.0, "dec": math.nextafter(boundary, math.inf)}], protected_paths=pins)
    assert receipt["status"] == "PASS"
    assert receipt["reason"] is None


def test_blind_guard_identity_match_refuses_regardless_of_coordinate(tmp_path):
    pins = _fixture_pin(tmp_path)
    receipt = blind_guard.guard([{"ls_id": 99, "ra": 180.0, "dec": 80.0}], protected_paths=pins)
    assert receipt["reason"] == "VOID-BLIND-VIOLATION"


def test_seal_journal_chaining_real_format_temp_copy(tmp_path):
    live = Path(__file__).resolve().parent.parent / "seal_journal_tierc.jsonl"
    journal = tmp_path / "seal_journal_tierc.jsonl"
    journal.write_bytes(live.read_bytes())
    predecessor = _seal_predecessor(journal)
    body = {"timestamp": "2026-09-03T00:00:00Z", "operation": "synthetic-test",
            "status": "PASS", "predecessor_receipt_digest": predecessor}
    body["receipt_digest"] = sha256_bytes(canonical_bytes(body))
    with journal.open("ab") as stream:
        stream.write(canonical_bytes(body))
    assert _seal_predecessor(journal) == body["receipt_digest"]
