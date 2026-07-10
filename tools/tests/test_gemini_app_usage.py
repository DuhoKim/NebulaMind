from __future__ import annotations

import json
import sys
from datetime import datetime, timedelta, timezone
from pathlib import Path

import pytest

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

import gemini_app_usage as gau  # noqa: E402
import gemini_app_usage_ingest as ingest  # noqa: E402

NOW = datetime(2026, 7, 10, 12, 0, 0, tzinfo=timezone.utc)


def reading(**overrides):
    payload = {
        'schema': gau.SCHEMA,
        'used_pct': 30.0,
        'reset_label': 'in 3 hr 20 min',
        'reset_at_utc': None,
        'tier': 'AI Pro',
        'source_url': 'https://gemini.google.com/usage',
        'captured_at_utc': gau.format_utc(NOW),
        'capture_method': 'bookmarklet-confirmed',
    }
    payload.update(overrides)
    return payload


class TestValidate:
    def test_roundtrips_a_good_reading(self):
        assert gau.validate(reading())['used_pct'] == 30.0

    @pytest.mark.parametrize(
        'bad',
        [
            {'schema': 'SOMETHING_ELSE'},
            {'used_pct': 101.0},
            {'used_pct': -1.0},
            {'used_pct': 'high'},
            {'used_pct': True},  # bool is an int subclass; must not slip through
            {'used_pct': None},
            {'captured_at_utc': ''},
            {'captured_at_utc': 'yesterday'},
            {'capture_method': 'headless-scrape'},
            {'reset_at_utc': 'soon'},
        ],
    )
    def test_rejects_untrustworthy_readings(self, bad):
        with pytest.raises(gau.ReadingError):
            gau.validate(reading(**bad))

    def test_rejects_non_object(self):
        with pytest.raises(gau.ReadingError):
            gau.validate([1, 2, 3])

    def test_naive_timestamp_is_treated_as_utc(self):
        assert gau.validate(reading(captured_at_utc='2026-07-10T12:00:00'))['captured_at_utc'] == '2026-07-10T12:00:00Z'


class TestDropFile:
    def test_write_then_load_roundtrip(self, tmp_path):
        dest = tmp_path / 'nested' / 'gemini_app_usage.json'
        gau.write_reading(reading(used_pct=42.0), dest)
        assert gau.load_reading(dest)['used_pct'] == 42.0
        assert not dest.with_name(dest.name + '.tmp').exists()

    def test_bad_payload_never_reaches_disk(self, tmp_path):
        dest = tmp_path / 'gemini_app_usage.json'
        with pytest.raises(gau.ReadingError):
            gau.write_reading(reading(used_pct=999), dest)
        assert not dest.exists()

    def test_missing_file_is_none_not_an_error(self, tmp_path):
        assert gau.load_reading(tmp_path / 'absent.json') is None

    def test_corrupt_file_raises_rather_than_guessing(self, tmp_path):
        dest = tmp_path / 'gemini_app_usage.json'
        dest.write_text(json.dumps({'schema': 'NOPE'}))
        with pytest.raises(gau.ReadingError):
            gau.load_reading(dest)


class TestStaleness:
    def test_fresh_reading_is_not_stale(self):
        assert not gau.is_stale(reading(captured_at_utc=gau.format_utc(NOW - timedelta(hours=5))), NOW)

    def test_reading_past_the_window_is_stale(self):
        assert gau.is_stale(reading(captured_at_utc=gau.format_utc(NOW - timedelta(hours=6, minutes=1))), NOW)


class TestGauge:
    def test_fresh_reading_shows_the_number(self):
        g = gau.build_gauge(gau.validate(reading(used_pct=30.0)), NOW, 'obs')
        assert g['fill_pct'] == 30.0
        assert g['tone'] == 'ok'
        assert '30% used' in g['value_label']

    def test_high_usage_is_danger(self):
        g = gau.build_gauge(gau.validate(reading(used_pct=85.0)), NOW, 'obs')
        assert g['tone'] == 'danger'

    def test_stale_reading_withholds_the_number(self):
        old = gau.validate(reading(used_pct=30.0, captured_at_utc=gau.format_utc(NOW - timedelta(hours=9))))
        g = gau.build_gauge(old, NOW, 'obs')
        assert g['fill_pct'] is None, 'a stale percentage must never render as a live fill'
        assert g['value_label'] == 'stale capture'
        assert '9.0h ago' in g['detail']

    def test_absent_reading_invents_nothing(self):
        g = gau.build_gauge(None, NOW, 'obs')
        assert g['fill_pct'] is None
        assert g['value_label'] == 'no capture yet'
        assert g['burn_advice']['lane'] == 'unknown'

    def test_gauge_states_the_pools_are_independent(self):
        g = gau.build_gauge(gau.validate(reading()), NOW, 'obs')
        assert 'different quota pool' in g['detail']
        assert g['burn_advice']['pools_are_independent'] is True


class TestBurnAdvice:
    def test_plenty_of_headroom_says_burn(self):
        assert gau.burn_advice(gau.validate(reading(used_pct=10.0)), NOW)['lane'] == 'burn'

    def test_middling_headroom_says_measured(self):
        assert gau.burn_advice(gau.validate(reading(used_pct=55.0)), NOW)['lane'] == 'measured'

    def test_low_headroom_says_reserve(self):
        advice = gau.burn_advice(gau.validate(reading(used_pct=90.0)), NOW)
        assert advice['lane'] == 'reserve'
        assert advice['headroom_pct'] == 10.0

    def test_low_headroom_but_imminent_reset_says_wait(self):
        soon = gau.format_utc(NOW + timedelta(minutes=20))
        advice = gau.burn_advice(gau.validate(reading(used_pct=90.0, reset_at_utc=soon)), NOW)
        assert advice['lane'] == 'wait'
        assert advice['minutes_to_reset'] == 20

    def test_stale_and_missing_both_yield_unknown(self):
        old = gau.validate(reading(captured_at_utc=gau.format_utc(NOW - timedelta(hours=8))))
        assert gau.burn_advice(old, NOW)['lane'] == 'unknown'
        assert gau.burn_advice(None, NOW)['lane'] == 'unknown'
        assert gau.burn_advice(None, NOW)['headroom_pct'] is None


class TestResetParsing:
    @pytest.mark.parametrize(
        'label,expected_minutes',
        [
            ('in 3 hr 20 min', 200),
            ('Resets in 2 hours', 120),
            ('resets in 45 min', 45),
            ('in 1h 5m', 65),
        ],
    )
    def test_parses_relative_resets(self, label, expected_minutes):
        got = ingest.parse_relative_reset(label, NOW)
        assert got == gau.format_utc(NOW + timedelta(minutes=expected_minutes))

    @pytest.mark.parametrize('label', ['', 'resets tomorrow', 'in 0 min', 'no reset info'])
    def test_unparseable_reset_is_none_not_zero(self, label):
        assert ingest.parse_relative_reset(label, NOW) is None


class TestAbsoluteResetParsing:
    """The live page says 'Resets at 2:59 AM' — a local clock time, not an offset."""

    @pytest.mark.parametrize(
        'label,want_hour,want_minute',
        [
            ('Resets at 2:59 AM', 2, 59),
            ('Resets at 12:00 AM', 0, 0),
            ('Resets at 12:30 PM', 12, 30),
            ('resets at 11:05 p.m.', 23, 5),
            ('Resets at 1:07 PM', 13, 7),
        ],
    )
    def test_absolute_reset_lands_on_that_local_clock_time(self, label, want_hour, want_minute):
        got = ingest.parse_absolute_reset(label, NOW)
        assert got is not None
        local = gau.parse_utc(got).astimezone()
        assert (local.hour, local.minute) == (want_hour, want_minute)

    def test_reset_is_always_in_the_future(self):
        for label in ['Resets at 2:59 AM', 'Resets at 11:59 PM', 'Resets at 12:00 AM']:
            reset = gau.parse_utc(ingest.parse_absolute_reset(label, NOW))
            assert reset > NOW
            assert (reset - NOW) <= timedelta(days=1)

    def test_a_time_already_past_today_means_tomorrow(self):
        local_now = NOW.astimezone()
        one_minute_ago = local_now - timedelta(minutes=1)
        label = one_minute_ago.strftime('Resets at %I:%M %p')
        reset = gau.parse_utc(ingest.parse_absolute_reset(label, NOW))
        assert reset > NOW
        assert (reset - NOW) > timedelta(hours=23)

    @pytest.mark.parametrize('label', ['Resets at 13:59 AM', 'Resets at 2:99 PM', 'Resets soon', ''])
    def test_nonsense_absolute_reset_is_none(self, label):
        assert ingest.parse_absolute_reset(label, NOW) is None


class TestParseResetAcceptsEitherWording:
    def test_prefers_relative_when_present(self):
        assert ingest.parse_reset('in 2 hours', NOW) == gau.format_utc(NOW + timedelta(hours=2))

    def test_falls_back_to_absolute(self):
        got = ingest.parse_reset('Resets at 2:59 AM', NOW)
        assert got is not None and gau.parse_utc(got).astimezone().hour == 2

    def test_neither_wording_yields_none(self):
        assert ingest.parse_reset('resets eventually', NOW) is None
        assert ingest.parse_reset('', NOW) is None

    def test_absolute_reset_enables_the_wait_lane(self):
        """The whole point: without reset_at_utc, burn_advice can never return 'wait'."""
        local_now = NOW.astimezone()
        soon = (local_now + timedelta(minutes=20)).strftime('Resets at %I:%M %p')
        reset_at = ingest.parse_reset(soon, NOW)
        assert reset_at is not None
        r = gau.validate(reading(used_pct=92.0, reset_label=soon, reset_at_utc=reset_at))
        assert gau.burn_advice(r, NOW)['lane'] == 'wait'
