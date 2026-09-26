"""Account captures must outlive renderer ticks without becoming new readings."""
import json
import sys
from datetime import datetime, timezone, timedelta
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
import live_provider_usage_monitor as monitor


def test_capture_maps_weekly_window_and_keeps_observation_time(tmp_path):
    stamp = datetime(2026, 9, 9, 23, 9, tzinfo=timezone.utc)
    path = tmp_path / 'capture.json'
    path.write_text(json.dumps({
        'schema': 'NM_CODEX_APP_USAGE_V1', 'observed_at_utc': stamp.isoformat(),
        'rateLimitsByLimitId': {'codex': {
            'primary': {'usedPercent': 0, 'windowDurationMins': 10080, 'resetsAt': 1789600032},
            'secondary': None,
        }},
    }))
    first = monitor.codex_app_gauge(path, stamp)
    later = monitor.codex_app_gauge(path, stamp + timedelta(minutes=30))
    assert first['fill_pct'] == 0
    assert '100% remaining' in first['value_label']
    assert '2026-09-17 08:07 KST' in first['value_label']
    assert first['source_label'] == later['source_label']
    assert len(first['sub_gauges']) == 1  # null secondary is not a zero-usage bucket
    stale = monitor.codex_app_gauge(path, stamp + timedelta(hours=2))
    assert stale['fill_pct'] is None
    assert stale['sub_gauges'][0]['fill_pct'] is None
    assert 'expired' in stale['status']


def test_missing_usage_is_unknown_and_future_capture_is_rejected(tmp_path):
    stamp = datetime(2026, 9, 9, 23, 9, tzinfo=timezone.utc)
    path = tmp_path / 'capture.json'
    path.write_text(json.dumps({
        'schema': 'NM_CODEX_APP_USAGE_V1', 'observed_at_utc': stamp.isoformat(),
        'rateLimitsByLimitId': {'codex': {'primary': None, 'secondary': None}},
    }))
    assert monitor.codex_app_gauge(path, stamp)['fill_pct'] is None
    assert monitor.codex_app_gauge(path, stamp - timedelta(hours=1)) is None
