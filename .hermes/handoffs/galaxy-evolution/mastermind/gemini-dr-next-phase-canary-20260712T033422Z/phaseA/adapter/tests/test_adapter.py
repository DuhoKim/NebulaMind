import json
from pathlib import Path

import pytest
from bs4 import BeautifulSoup

from real_dom_adapter import SELECTORS, build_capture_js, build_js_probe, classify_signal


MASTER_ROOT = Path(__file__).resolve().parents[4]
FIXTURE_ROOT = MASTER_ROOT / "goru-deep-research-capture-dev-20260712T030531Z" / "dev" / "fixtures"

def test_build_js_probe():
    probe = build_js_probe()
    assert isinstance(probe, str)
    assert probe.lstrip().startswith("(")
    assert not probe.lstrip().startswith("return")
    assert "recaptcha" in probe
    assert "document.body.innerText" not in probe
    assert "[role='dialog']" in probe
    assert "JSON.stringify" in probe


@pytest.mark.parametrize(
    ("fixture", "selector_key"),
    [
        ("fx_running.html", "running_stop"),
        ("fx_verification_wall.html", "verification"),
        ("fx_billing_upsell.html", "billing_candidates"),
        ("fx_login_wall.html", "login"),
    ],
)
def test_named_fixtures_match_structural_selectors(fixture, selector_key):
    soup = BeautifulSoup((FIXTURE_ROOT / fixture).read_text(), "html.parser")
    assert soup.select_one(SELECTORS[selector_key]) is not None

def test_classify_login():
    signal = {"url": "https://accounts.google.com/login", "title": "Sign in", "counts": {}}
    assert classify_signal(signal) == "LOGIN_WALL"


def test_classify_challenge_url_as_verification_before_login():
    signal = {"url": "https://accounts.google.com/signin/challenge/pwd", "counts": {}}
    assert classify_signal(signal) == "VERIFICATION_WALL"


def test_classify_verification():
    signal = {"url": "https://gemini.google.com/app", "title": "Gemini", "counts": {"verification_iframe": 1}}
    assert classify_signal(signal) == "VERIFICATION_WALL"

    # Prose containing 'verification' should not trigger wall if iframe is 0
    signal_prose = {"url": "https://gemini.google.com/app", "title": "Gemini", "counts": {"verification_iframe": 0}, "has_prose_verification": True}
    assert classify_signal(signal_prose) != "VERIFICATION_WALL"

def test_classify_billing():
    signal = {"url": "https://gemini.google.com/app", "title": "Gemini", "counts": {"billing_upgrade": 1}}
    assert classify_signal(signal) == "BILLING_WALL"

def test_classify_running():
    signal = {"url": "https://gemini.google.com/app/123", "title": "Gemini", "counts": {"running_stop": 1}}
    assert classify_signal(signal) == "RUNNING"

def test_classify_plan_ready():
    signal = {"url": "https://gemini.google.com/app", "title": "Gemini", "counts": {"plan": 1, "start_control": 1, "running_stop": 0}}
    assert classify_signal(signal) == "PLAN_READY"

def test_classify_complete():
    signal = {"url": "https://gemini.google.com/app/123", "title": "Gemini", "counts": {"complete": 1, "answer_body": 1, "links": 1, "running_stop": 0}}
    assert classify_signal(signal) == "COMPLETE"

def test_classify_pro_dr_active():
    signal = {"url": "https://gemini.google.com/app", "title": "Gemini", "counts": {"composer": 1, "pro_mode": 1, "deep_research_active": 1, "plan": 0, "running_stop": 0}}
    assert classify_signal(signal) == "DR_ACTIVE"

def test_classify_unknown():
    signal = {"url": "https://gemini.google.com/app", "title": "Gemini", "counts": {}}
    assert classify_signal(signal) == "UNKNOWN"


def test_exact_target_mismatch_fails_closed():
    signal = {
        "url": "https://gemini.google.com/app/wrong",
        "counts": {"running_stop": 1},
    }
    assert classify_signal(signal, expected_url="https://gemini.google.com/app/expected") == "TARGET_MISMATCH"


def test_capture_script_is_separate_and_guarded():
    expected = "https://gemini.google.com/app/exact-target"
    marker = "C1_DONE_MARKER"
    script = build_capture_js(expected, marker)
    assert script.lstrip().startswith("(")
    assert expected in script
    assert marker in script
    assert "TARGET_MISMATCH" in script
    assert "NOT_COMPLETE" in script
    assert "#extended-response-markdown-content" in script
    assert "innerText" in script
    assert "Array.from" in script
    assert ".href" in script


def test_capture_script_json_escapes_target_and_marker():
    expected = 'https://gemini.google.com/app/exact"target'
    marker = 'MARKER"WITH\\ESCAPES'
    script = build_capture_js(expected, marker)
    assert json.dumps(expected) in script
    assert json.dumps(marker) in script
