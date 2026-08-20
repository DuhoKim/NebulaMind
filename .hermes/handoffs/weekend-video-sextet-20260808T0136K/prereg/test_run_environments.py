#!/usr/bin/env python3
from __future__ import annotations

import subprocess
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parent


class RunEnvironmentTests(unittest.TestCase):
    def test_each_stage_uses_its_declared_interpreter(self) -> None:
        expected = {
            "run_cutout_stage.sh": ("/usr/bin/python3", "_cutout_runner_20260820/cutout_runner.py"),
            "run_inference_stage.sh": ("venv_torch/bin/python", "_inference_20260820/inference_runner.py"),
            "run_committee_stage.sh": ("venv_torch/bin/python", "_committee_20260820/committee.py"),
            "run_display_stage.sh": ("/usr/bin/python3", "display/tensor_to_png.py"),
            "run_hc1h_stage.sh": ("/usr/bin/python3", "handcheck/nm_handcheck.py"),
        }
        for name, fragments in expected.items():
            script = ROOT / name
            text = script.read_text(encoding="utf-8")
            for fragment in fragments:
                self.assertIn(fragment, text)
            completed = subprocess.run(
                [str(script), "--help"],
                cwd=ROOT,
                capture_output=True,
                text=True,
            )
            self.assertEqual(completed.returncode, 0, msg=completed.stderr)

    def test_environment_record_and_real_population_trap_are_prominent(self) -> None:
        record = (ROOT / "RUN_ENVIRONMENTS.md").read_text(encoding="utf-8")
        self.assertIn("No stage requires both torch and Pillow", record)
        self.assertIn("venv_torch", record)
        self.assertIn("/usr/bin/python3", record)
        hc1h = (ROOT / "run_hc1h_stage.sh").read_text(encoding="utf-8")
        self.assertIn("REAL_POPULATION IS A FROZEN ROLE NAME", hc1h)
        self.assertIn(".provenance.json", hc1h)


if __name__ == "__main__":
    unittest.main(verbosity=2)
