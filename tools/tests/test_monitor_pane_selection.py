"""A pane the operator scrolled back must never receive send-keys.

tmux copy-mode binds '/' to search-forward. Sending '/usage' or '/status' into a
copy-mode pane types a search, jumps the operator's scroll position, and never
reaches the CLI — the gauge silently stops refreshing while the pane yanks itself
up the scrollback every slash-interval.
"""
from __future__ import annotations

import sys
import types
from pathlib import Path

import pytest

TOOLS = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(TOOLS))

# The monitor imports two local-only modules at load time.
for name, attrs in (
    ('stable_cockpit_renderer', {'DEFAULT_PUBLIC_ROOTS': [], 'write_outputs': lambda *a, **k: None}),
    ('stable_cockpit_guard', {'unlock_all': lambda *a, **k: None, 'lock_all': lambda *a, **k: None}),
):
    if name not in sys.modules:
        module = types.ModuleType(name)
        module.__dict__.update(attrs)
        sys.modules[name] = module

import live_provider_usage_monitor as mon  # noqa: E402

IDLE_AGY = '\n'.join(['some output', '>', '? for shortcuts   Gemini 3.1 Pro (High)'])
IDLE_CODEX = '\n'.join(['OpenAI Codex', '› ready', 'gpt-5.5'])


def pane(pane_id, command, role='', target='sess:win.0', in_mode='0'):
    return {'pane_id': pane_id, 'target': target, 'command': command, 'role': role, 'in_mode': in_mode}


@pytest.fixture
def always_idle(monkeypatch):
    monkeypatch.setattr(mon, 'capture_pane', lambda pane_id, lines=500: IDLE_AGY + '\n' + IDLE_CODEX)
    monkeypatch.setattr(mon, 'is_idle_agy', lambda text: True)
    monkeypatch.setattr(mon, 'is_idle_codex', lambda text: True)


class TestInCopyMode:
    def test_flag_set(self):
        assert mon.in_copy_mode(pane('%1', 'agy', in_mode='1'))

    def test_flag_clear(self):
        assert not mon.in_copy_mode(pane('%1', 'agy', in_mode='0'))

    def test_missing_key_defaults_to_not_in_mode(self):
        assert not mon.in_copy_mode({'pane_id': '%1'})


class TestChoosePaneSkipsCopyMode:
    def test_copy_mode_agy_pane_is_never_chosen(self, always_idle):
        panes = [pane('%44', 'agy', role='Goru', in_mode='1')]
        assert mon.choose_pane(panes, 'agy') is None, 'would have typed a search into the operator scrollback'

    def test_copy_mode_codex_pane_is_never_chosen(self, always_idle):
        panes = [pane('%9', 'codex', role='Kun', in_mode='1')]
        assert mon.choose_pane(panes, 'codex') is None

    def test_live_pane_is_still_chosen(self, always_idle):
        panes = [pane('%66', 'agy', role='Goru-m1', in_mode='0')]
        assert mon.choose_pane(panes, 'agy')['pane_id'] == '%66'

    def test_prefers_the_live_pane_over_the_scrolled_one(self, always_idle):
        panes = [pane('%44', 'agy', role='Goru', in_mode='1'), pane('%66', 'agy', role='Goru-m1', in_mode='0')]
        assert mon.choose_pane(panes, 'agy')['pane_id'] == '%66'

    def test_all_panes_scrolled_yields_no_pane(self, always_idle):
        panes = [pane('%44', 'agy', in_mode='1'), pane('%66', 'agy', in_mode='1')]
        assert mon.choose_pane(panes, 'agy') is None


class TestTmuxPanesParsing:
    def test_in_mode_is_parsed_from_the_format_string(self, monkeypatch):
        line = '%44\tgoru-agy:[tmux].0\tagy\tGoru\t1'
        monkeypatch.setattr(mon, 'run', lambda cmd, timeout=20: types.SimpleNamespace(returncode=0, stdout=line))
        parsed = mon.tmux_panes()[0]
        assert parsed['pane_id'] == '%44'
        assert parsed['role'] == 'Goru'
        assert parsed['in_mode'] == '1'

    def test_short_line_does_not_raise(self, monkeypatch):
        monkeypatch.setattr(mon, 'run', lambda cmd, timeout=20: types.SimpleNamespace(returncode=0, stdout='%1\tsess:w.0'))
        assert mon.tmux_panes()[0]['in_mode'] == ''

    def test_format_string_requests_pane_in_mode(self, monkeypatch):
        seen = {}

        def fake_run(cmd, timeout=20):
            seen['cmd'] = cmd
            return types.SimpleNamespace(returncode=0, stdout='')

        monkeypatch.setattr(mon, 'run', fake_run)
        mon.tmux_panes()
        assert '#{pane_in_mode}' in seen['cmd'][-1]
