import pytest
import os
import json
import hashlib
from pathlib import Path
from unittest.mock import patch, mock_open

# We assume wait_and_extract.py will expose:
# - parse_dom_fixture(html_path, target_id, expected_marker) -> verdict dict
# - live_capture_boundary() -> raises Exception
# - write_capture_receipt(body_path) -> dict with sha256 and size

import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import wait_and_extract

FIXTURE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '../fixtures'))
VERDICTS_FILE = os.path.join(FIXTURE_DIR, 'EXPECTED_VERDICTS.json')

with open(VERDICTS_FILE, 'r') as f:
    ORACLE = json.load(f)

FIXTURES = ORACLE['fixtures']
MARKER = ORACLE['marker_string']

def test_12_classifications():
    for fx_name, expected in FIXTURES.items():
        fx_path = os.path.join(FIXTURE_DIR, fx_name)
        verdict = wait_and_extract.parse_dom_fixture(fx_path, "target_123", MARKER)
        
        assert verdict['state'] == expected['state'], f"Mismatch in state for {fx_name}"
        
        for req_action in expected.get('required_actions', []):
            assert req_action in verdict['planned_actions'], f"Missing {req_action} for {fx_name}"
            
        for plan in verdict['planned_actions']:
            assert plan in expected['allowed_actions'], f"Disallowed {plan} for {fx_name}"
            
        if 'capture' in expected:
            cap_expected = expected['capture']
            assert verdict['marker_count'] == cap_expected['marker_count']
            assert verdict['marker_is_final_nonblank_line'] == cap_expected['marker_is_final_nonblank_line']
            assert verdict['verdict_class'] == cap_expected['verdict_class']

def test_exact_requested_target_echo():
    for fx_name in FIXTURES:
        verdict = wait_and_extract.parse_dom_fixture(os.path.join(FIXTURE_DIR, fx_name), "conv_abc", MARKER)
        assert verdict['target_id'] == "conv_abc"
        assert 'extracted_body_path' in verdict

def test_unknown_hard_stop():
    # Provide a garbage HTML to force UNKNOWN state
    garbage_path = os.path.join(FIXTURE_DIR, "fx_garbage.html")
    with open(garbage_path, 'w') as f:
        f.write("<html><body>Nothing recognizable</body></html>")
    
    verdict = wait_and_extract.parse_dom_fixture(garbage_path, "conv_unknown", MARKER)
    assert verdict['state'] == "UNKNOWN"
    assert verdict['planned_actions'] == ["HARD_STOP"]
    
    os.remove(garbage_path)

def test_marker_exactly_once_final_captured():
    # From oracle, fx_complete_ok should be CAPTURED
    verdict = wait_and_extract.parse_dom_fixture(os.path.join(FIXTURE_DIR, "fx_complete_ok.html"), "conv_1", MARKER)
    assert verdict['verdict_class'] == "CAPTURED_OK"
    assert verdict['marker_count'] == 1
    assert verdict['marker_is_final_nonblank_line'] is True

def test_deterministic_distinct_bodies():
    v1 = wait_and_extract.parse_dom_fixture(os.path.join(FIXTURE_DIR, "fx_complete_ok.html"), "conv_1", MARKER)
    v2 = wait_and_extract.parse_dom_fixture(os.path.join(FIXTURE_DIR, "fx_complete_ok.html"), "conv_1", MARKER)
    
    v3 = wait_and_extract.parse_dom_fixture(os.path.join(FIXTURE_DIR, "fx_complete_marker_missing.html"), "conv_1", MARKER)
    
    assert v1['extracted_body_sha256'] == v2['extracted_body_sha256']
    assert v1['extracted_body_sha256'] != v3['extracted_body_sha256']

def test_immutable_receipt():
    # Mock writing a file and securing it
    tmp_path = "/tmp/test_body_receipt.md"
    with open(tmp_path, "w") as f:
        f.write("Test body")
    
    receipt = wait_and_extract.write_capture_receipt(tmp_path)
    assert 'sha256' in receipt
    assert 'bytes' in receipt
    
    # Check if file is read-only
    stat = os.stat(tmp_path)
    assert not (stat.st_mode & 0o222), "File should be immutable (read-only)"
    os.remove(tmp_path)

def test_refusing_overwrite():
    tmp_path = "/tmp/test_body_overwrite.md"
    with open(tmp_path, "w") as f:
        f.write("Old body")
        
    # Should raise error if target file exists
    with pytest.raises(Exception, match="exists|overwrite"):
        wait_and_extract.save_body("New body", tmp_path)
        
    os.remove(tmp_path)

def test_live_capture_boundary_raises_held():
    with pytest.raises(Exception, match="HELD"):
        wait_and_extract.live_capture_boundary()


def test_dry_run_writes_immutable_capture_bundle(tmp_path):
    out = tmp_path / "capture"
    rc = wait_and_extract.main([
        "--dry-run",
        "--fixture", os.path.join(FIXTURE_DIR, "fx_complete_ok.html"),
        "--target", "conv-dry-run",
        "--marker", MARKER,
        "--out", str(out),
    ])

    assert rc == 0
    verdict_path = out / "verdict.json"
    body_path = out / "body.md"
    receipt_path = out / "CAPTURE_RECEIPT.json"
    verdict = json.loads(verdict_path.read_text())
    receipt = json.loads(receipt_path.read_text())

    assert verdict["target_id"] == "conv-dry-run"
    assert verdict["extracted_body_path"] == "body.md"
    assert verdict["verdict_class"] == "CAPTURED_OK"
    assert set(receipt["files"]) == {"body.md", "verdict.json"}
    for name in receipt["files"]:
        payload = (out / name).read_bytes()
        assert receipt["files"][name]["bytes"] == len(payload)
        assert receipt["files"][name]["sha256"] == hashlib.sha256(payload).hexdigest()
    for path in (body_path, verdict_path, receipt_path):
        assert not (path.stat().st_mode & 0o222)


def test_dry_run_refuses_to_overwrite_capture_bundle(tmp_path):
    out = tmp_path / "capture"
    argv = [
        "--dry-run",
        "--fixture", os.path.join(FIXTURE_DIR, "fx_complete_ok.html"),
        "--target", "conv-no-overwrite",
        "--marker", MARKER,
        "--out", str(out),
    ]
    wait_and_extract.main(argv)
    before = {path.name: path.read_bytes() for path in out.iterdir()}

    with pytest.raises(FileExistsError):
        wait_and_extract.main(argv)

    assert {path.name: path.read_bytes() for path in out.iterdir()} == before


def test_dry_run_writes_verdict_for_non_capture_state(tmp_path):
    out = tmp_path / "idle-verdict"
    rc = wait_and_extract.main([
        "--dry-run",
        "--fixture", os.path.join(FIXTURE_DIR, "fx_composer_idle.html"),
        "--target", "conv-idle",
        "--marker", MARKER,
        "--out", str(out),
    ])

    assert rc == 0
    verdict_path = out / "verdict.json"
    verdict = json.loads(verdict_path.read_text())
    assert verdict["state"] == "COMPOSER_IDLE"
    assert verdict["target_id"] == "conv-idle"
    assert verdict["extracted_body_path"] is None
    assert sorted(path.name for path in out.iterdir()) == ["verdict.json"]
    assert not (verdict_path.stat().st_mode & 0o222)
