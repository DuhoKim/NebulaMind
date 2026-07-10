"""Gating logic for the unattended Chrome scrape.

The Chrome/AppleScript half can't run headless in CI, so these cover the part
that decides whether an extractor result is trustworthy enough to store — the
safety-critical logic. An unattended read with no human to confirm it must
abstain rather than store a guess, and abstaining must never clobber an existing
reading.
"""
from __future__ import annotations

import json
import sys
from datetime import datetime, timedelta, timezone
from pathlib import Path

import pytest

TOOLS = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(TOOLS))

import gemini_app_usage as gau  # noqa: E402
import gemini_app_usage_autofetch as af  # noqa: E402

NOW = datetime(2026, 7, 10, 15, 0, 0, tzinfo=timezone.utc)


def extract(**overrides):
    base = {
        'used_pct': 1,
        'source_signal': 'progressbar',
        'reset_label': 'Resets at 2:59 AM',
        'tier_guess': 'AI Ultra',
        'on_usage_page': True,
        'href': 'https://gemini.google.com/usage',
    }
    base.update(overrides)
    return base


class TestBuildReading:
    def test_absolute_reset_is_parsed(self):
        r = af.build_reading(extract(), NOW)
        assert r['reset_at_utc'] is not None
        assert r['capture_method'] == 'chrome-auto'
        assert r['tier'] == 'AI Ultra'

    def test_blank_tier_becomes_none(self):
        assert af.build_reading(extract(tier_guess=''), NOW)['tier'] is None

    def test_missing_reset_label_leaves_reset_null(self):
        r = af.build_reading(extract(reset_label=''), NOW)
        assert r['reset_at_utc'] is None


class TestGating:
    def test_progressbar_signal_is_stored(self, tmp_path):
        dest = tmp_path / 'r.json'
        rep = af.process_extraction(extract(source_signal='progressbar'), NOW, dest)
        assert rep['stored'] is True
        assert gau.load_reading(dest)['capture_method'] == 'chrome-auto'

    def test_scoped_text_signal_is_stored(self, tmp_path):
        rep = af.process_extraction(extract(source_signal='scoped-text'), NOW, tmp_path / 'r.json')
        assert rep['stored'] is True

    def test_any_text_signal_abstains(self, tmp_path):
        rep = af.process_extraction(extract(source_signal='any-text'), NOW, tmp_path / 'r.json')
        assert rep['stored'] is False
        assert not (tmp_path / 'r.json').exists()

    def test_none_signal_abstains(self, tmp_path):
        rep = af.process_extraction(extract(source_signal='none', used_pct=None), NOW, tmp_path / 'r.json')
        assert rep['stored'] is False

    def test_off_usage_page_abstains(self, tmp_path):
        rep = af.process_extraction(extract(on_usage_page=False), NOW, tmp_path / 'r.json')
        assert rep['stored'] is False
        assert 'usage page' in rep['reason']

    def test_out_of_range_percent_abstains(self, tmp_path):
        rep = af.process_extraction(extract(used_pct=150), NOW, tmp_path / 'r.json')
        assert rep['stored'] is False

    def test_abstain_never_clobbers_an_existing_reading(self, tmp_path):
        dest = tmp_path / 'r.json'
        good = {
            'schema': gau.SCHEMA, 'used_pct': 42.0, 'reset_label': None, 'reset_at_utc': None,
            'tier': 'AI Ultra', 'source_url': 'https://gemini.google.com/usage',
            'captured_at_utc': gau.format_utc(NOW - timedelta(minutes=5)),
            'capture_method': 'bookmarklet-confirmed',
        }
        gau.write_reading(good, dest)
        rep = af.process_extraction(extract(source_signal='any-text'), NOW, dest)
        assert rep['stored'] is False
        # the human-confirmed reading survives untouched
        after = gau.load_reading(dest)
        assert after['used_pct'] == 42.0
        assert after['capture_method'] == 'bookmarklet-confirmed'

    def test_tier_carries_forward_from_a_prior_reading(self, tmp_path):
        dest = tmp_path / 'r.json'
        prior = {
            'schema': gau.SCHEMA, 'used_pct': 5.0, 'reset_label': None, 'reset_at_utc': None,
            'tier': 'AI Ultra', 'source_url': 'https://gemini.google.com/usage',
            'captured_at_utc': gau.format_utc(NOW - timedelta(minutes=30)),
            'capture_method': 'manual',
        }
        gau.write_reading(prior, dest)
        # a scrape with no tier should inherit the operator-set one
        af.process_extraction(extract(tier_guess=''), NOW, dest)
        after = gau.load_reading(dest)
        assert after['tier'] == 'AI Ultra'
        assert after['capture_method'] == 'chrome-auto'  # provenance still honest

    def test_scraped_tier_wins_over_a_prior_one(self, tmp_path):
        dest = tmp_path / 'r.json'
        prior = {
            'schema': gau.SCHEMA, 'used_pct': 5.0, 'reset_label': None, 'reset_at_utc': None,
            'tier': 'AI Pro', 'source_url': 'https://gemini.google.com/usage',
            'captured_at_utc': gau.format_utc(NOW - timedelta(minutes=30)), 'capture_method': 'manual',
        }
        gau.write_reading(prior, dest)
        af.process_extraction(extract(tier_guess='AI Ultra'), NOW, dest)
        assert gau.load_reading(dest)['tier'] == 'AI Ultra'

    def test_no_prior_and_no_scraped_tier_stays_none(self, tmp_path):
        rep = af.process_extraction(extract(tier_guess=''), NOW, tmp_path / 'r.json')
        assert rep['reading']['tier'] is None

    def test_dry_run_reports_but_stores_nothing(self, tmp_path):
        dest = tmp_path / 'r.json'
        rep = af.process_extraction(extract(), NOW, dest, dry_run=True)
        assert rep['stored'] is False
        assert rep['reading'] is not None
        assert not dest.exists()


class TestGaugeProvenance:
    def test_chrome_auto_reads_as_unattended_not_operator_confirmed(self):
        r = gau.validate(af.build_reading(extract(), NOW))
        gauge = gau.build_gauge(r, NOW, 'obs')
        assert 'Unattended Chrome scrape' in gauge['status']
        assert 'Operator-confirmed' not in gauge['status']

    def test_manual_still_reads_as_operator_confirmed(self):
        manual = {
            'schema': gau.SCHEMA, 'used_pct': 1.0, 'reset_label': None, 'reset_at_utc': None,
            'tier': None, 'source_url': 'https://gemini.google.com/usage',
            'captured_at_utc': gau.format_utc(NOW), 'capture_method': 'manual',
        }
        gauge = gau.build_gauge(gau.validate(manual), NOW, 'obs')
        assert 'Operator-confirmed capture' in gauge['status']


class TestFriendlyErrors:
    def test_automation_denied_maps_to_grant_instruction(self):
        msg = af.friendly_osascript_error('39:55: execution error: ... (-1743)')
        assert 'Privacy & Security -> Automation' in msg

    def test_localized_js_bridge_off_matched_via_support_url(self):
        # A non-English Chrome returns a localized message with code (12), no English
        # 'JavaScript' word — but always links this support slug. Match on that anchor
        # so the instruction is shown regardless of the OS/Chrome locale.
        localized = (
            '596:628: execution error: <localized text> '
            'https://support.google.com/chrome/?p=applescript (12)'
        )
        msg = af.friendly_osascript_error(localized)
        assert 'Allow JavaScript from Apple Events' in msg
        assert 'support.google' not in msg  # raw dump replaced with the instruction

    def test_english_js_bridge_off_is_recognised(self):
        msg = af.friendly_osascript_error('execution error: JavaScript through AppleScript is turned off. (-2700)')
        assert 'Allow JavaScript from Apple Events' in msg

    def test_unknown_error_is_passed_through(self):
        msg = af.friendly_osascript_error('some other failure')
        assert msg == 'osascript failed: some other failure'


class TestExtractorContract:
    """The Python side assumes these keys; pin the shape the JS must return."""

    def test_required_keys_consumed(self):
        r = af.build_reading(extract(), NOW)
        assert set(r) == {
            'schema', 'used_pct', 'reset_label', 'reset_at_utc',
            'tier', 'source_url', 'captured_at_utc', 'capture_method',
        }
