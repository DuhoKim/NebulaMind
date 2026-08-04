import importlib.util
import json
import sys
import unittest
from pathlib import Path
from unittest.mock import patch


SCRIPT = Path(__file__).with_name("yui_flow_hq_batch_02_13.py")
PACKET = SCRIPT.parents[1]
sys.path.insert(0, str(PACKET))
SPEC = importlib.util.spec_from_file_location("yui_flow_hq_batch", SCRIPT)
assert SPEC and SPEC.loader
MODULE = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(MODULE)


class ProbeExactDriftTests(unittest.TestCase):
    def test_matching_url_never_emergency_freezes_on_tab_placement_mismatch(self) -> None:
        probe = {
            "challenge": False,
            "signals": [],
            "url": MODULE.PROJECT_ROOT,
            "window_index": MODULE.WINDOW_INDEX,
            "tab_index": MODULE.TAB_INDEX + 1,
        }

        with (
            patch.object(MODULE._probe_module, "probe_live_flow_page", return_value=probe),
            patch.object(MODULE, "emergency_freeze") as emergency_freeze,
        ):
            with self.assertRaisesRegex(RuntimeError, "placement mismatch"):
                MODULE.probe_exact()

        emergency_freeze.assert_not_called()

    def test_genuine_url_mismatch_still_emergency_freezes(self) -> None:
        observed_url = "https://labs.google/fx/tools/flow/project/not-the-owned-project"
        probe = {
            "challenge": False,
            "signals": [],
            "url": observed_url,
            "window_index": MODULE.WINDOW_INDEX,
            "tab_index": MODULE.TAB_INDEX,
        }

        with (
            patch.object(MODULE._probe_module, "probe_live_flow_page", return_value=probe),
            patch.object(MODULE, "emergency_freeze", side_effect=RuntimeError("drift")) as emergency_freeze,
        ):
            with self.assertRaisesRegex(RuntimeError, "drift"):
                MODULE.probe_exact()

        emergency_freeze.assert_called_once_with(
            f"Flow target drift: expected {MODULE.PROJECT_ROOT}, observed {observed_url}",
            None,
        )


class AxPressReadinessTests(unittest.TestCase):
    def test_ax_press_retries_until_transiently_missing_control_appears(self) -> None:
        outcomes = iter([False, False, True])
        calls = []

        def fake_run(*args, **kwargs):
            calls.append((args, kwargs))
            pressed = next(outcomes)
            return type(
                "Completed",
                (),
                {"stdout": json.dumps({"pressed": pressed, "matched": "Video · 8s crop_16_9 1x" if pressed else ""})},
            )()

        with patch.object(MODULE.subprocess, "run", side_effect=fake_run), patch.object(MODULE.time, "sleep") as sleep:
            MODULE.ax_press(
                "AXPopUpButton",
                'n.startsWith("Video ·")',
                attempts=3,
                interval=0.25,
            )

        self.assertEqual(len(calls), 3)
        self.assertEqual(sleep.call_count, 2)


class PreSubmitSnapshotTests(unittest.TestCase):
    def test_pre_submit_baseline_uses_final_verified_card_snapshot(self) -> None:
        prompt = "clip prompt"
        state = {
            "url": MODULE.PROJECT_ROOT,
            "prompt": prompt,
            "active": True,
            "config": "Video · 8s crop_16_9 1x",
            "videos": 9,
        }

        baseline = MODULE.pre_submit_baseline(state, prompt)

        self.assertEqual(baseline, 9)


if __name__ == "__main__":
    unittest.main()
