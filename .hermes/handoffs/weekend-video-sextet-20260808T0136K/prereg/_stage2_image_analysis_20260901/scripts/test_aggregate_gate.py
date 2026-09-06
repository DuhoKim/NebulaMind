"""The gate's own controls (Blanc 05:48): it must FAIL the synthetic log that fooled v1 (FAILED + a trailing 'OK'), FAIL the genuine 12-NameError RUN1, and PASS the
genuine RUN2. Written against v2; run first against the RETAINED v1 to show v1 passing the synthetic log (fail-first)."""
import subprocess, sys, unittest
from pathlib import Path
HERE = Path(__file__).resolve().parent; GATE = HERE / "aggregate_gate.py"; FX = HERE / "gate_fixtures"
def run(gate, log, suites, tests): r = subprocess.run([sys.executable, str(gate), str(log), "--suites", str(suites), "--tests", str(tests)], capture_output=True, text=True); return r.returncode, r.stdout.strip()
class Gate(unittest.TestCase):
    def test_synthetic_failing_log_is_rejected(self): rc, out = run(GATE, FX / "synthetic_failing_blanc_0548.txt", 1, 1); self.assertEqual(rc, 2, out); self.assertIn("FAILED", out)
    def test_genuine_failing_run1_is_rejected(self): rc, out = run(GATE, FX / "genuine_failing_v32_RUN1_12_nameerrors.txt", 28, 232); self.assertEqual(rc, 2, out)
    def test_genuine_passing_run2_passes(self): rc, out = run(GATE, FX / "genuine_passing_v32_RUN2.txt", 28, 232); self.assertEqual(rc, 0, out); self.assertIn("exactly one result line equal to 'OK'", out)
    def test_two_results_in_one_suite_fail(self):
        p = FX / "_two_results.txt"; p.write_text("== s  []\nRan 1 test in 0.001s\nOK\nOK\n"); rc, out = run(GATE, p, 1, 1); p.unlink(); self.assertEqual(rc, 2, out)
    def test_ok_prefix_is_not_ok(self):
        p = FX / "_ok_prefix.txt"; p.write_text("== s  []\nRan 1 test in 0.001s\nOK (skipped=1)\n"); rc, out = run(GATE, p, 1, 1); p.unlink(); self.assertEqual(rc, 2, out)
if __name__ == "__main__": unittest.main()
