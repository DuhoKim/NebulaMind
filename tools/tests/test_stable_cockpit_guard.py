from __future__ import annotations

import importlib.util
from pathlib import Path
import sys
from types import SimpleNamespace


MODULE_PATH = Path(__file__).resolve().parents[1] / "stable_cockpit_guard.py"


def load_guard_module():
    spec = importlib.util.spec_from_file_location("stable_cockpit_guard_under_test", MODULE_PATH)
    assert spec is not None and spec.loader is not None
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


def test_process_scan_ignores_private_autopilot_controller_log(monkeypatch):
    guard = load_guard_module()
    output = "\n".join(
        [
            "duhokim 37134 zsh -c python3 /repo/tools/galaxy_evolution_autopilot.py watch --interval 20 2>&1 | tee -a /Users/duhokim/HermesOps/cockpit/ge-autopilot-controller.log",
            "duhokim 37137 tee -a /Users/duhokim/HermesOps/cockpit/ge-autopilot-controller.log",
        ]
    )
    monkeypatch.setattr(
        guard.subprocess,
        "run",
        lambda *args, **kwargs: SimpleNamespace(stdout=output, stderr="", returncode=0),
    )

    assert guard.process_scan() == ""


def test_process_scan_keeps_actual_stable_cockpit_writer(monkeypatch):
    guard = load_guard_module()
    writer = "duhokim 41234 python3 /tmp/watch_live-steering-cockpit.py"
    monkeypatch.setattr(
        guard.subprocess,
        "run",
        lambda *args, **kwargs: SimpleNamespace(stdout=writer, stderr="", returncode=0),
    )

    assert guard.process_scan() == writer


def test_process_scan_ignores_ge_mastermind_method_workspace_roots(monkeypatch):
    guard = load_guard_module()
    coordinator = (
        "duhokim 4284 /opt/homebrew/bin/tmux new-session -d -s ge-mastermind "
        "NEBULAMIND_MASTER_ROOT=/repo/.hermes/handoffs/galaxy-evolution/mastermind "
        "NEBULAMIND_METHOD1_PUBLIC_ROOT=/repo/frontend/public/agent-reports/"
        "wiki-method-results/galaxy-evolution/method-one exec claude"
    )
    monkeypatch.setattr(
        guard.subprocess,
        "run",
        lambda *args, **kwargs: SimpleNamespace(stdout=coordinator, stderr="", returncode=0),
    )

    assert guard.process_scan() == ""


def test_process_scan_keeps_ge_mastermind_that_targets_stable_route(monkeypatch):
    guard = load_guard_module()
    writer = (
        "duhokim 4284 /opt/homebrew/bin/tmux new-session -d -s ge-mastermind "
        "NEBULAMIND_MASTER_ROOT=/repo/.hermes/handoffs/galaxy-evolution/mastermind "
        "OUTPUT=/repo/frontend/public/agent-reports/live-steering-cockpit.html exec /usr/local/bin/claude"
    )
    monkeypatch.setattr(
        guard.subprocess,
        "run",
        lambda *args, **kwargs: SimpleNamespace(stdout=writer, stderr="", returncode=0),
    )

    assert guard.process_scan() == writer
