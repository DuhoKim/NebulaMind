"""Controls for the fail-first kit (Blanc 08:51). Each fixture is written to a temp file OUTSIDE the fixtures directory and asserts one outcome."""
import subprocess, sys, tempfile, unittest, os
from pathlib import Path
HERE = Path(__file__).resolve().parent; KIT = HERE / "failfirst_kit.py"; TMP = HERE.parent / "_tmp_failfirst_kit_tests"
def run(mod, log=None):
    cmd = [sys.executable, str(KIT), str(mod)] + (["--against", str(log)] if log else [])
    r = subprocess.run(cmd, capture_output=True, text=True); return r.returncode, r.stdout
GOOD = '''
import unittest
class T(unittest.TestCase):
    def test_one(self):
        """FAIL-FIRST: a single outcome assertion"""
        self.assertTrue(False)
    def test_two(self):
        """POSITIVE-REGRESSION: already holds"""
        self.assertTrue(True)
'''
BUNDLED = GOOD.replace('        self.assertTrue(False)\n', '        self.assertTrue(False)\n        self.assertIn("a", "abc")\n')
UNLABELLED = GOOD.replace('"""FAIL-FIRST: a single outcome assertion"""', '"""just a test"""')
LOG_OK = "test_one (m.T) ... FAIL\ntest_two (m.T) ... ok\n"
LOG_FF_PASSED = "test_one (m.T) ... ok\ntest_two (m.T) ... ok\n"
LOG_PR_FAILED = "test_one (m.T) ... FAIL\ntest_two (m.T) ... FAIL\n"
class Kit(unittest.TestCase):
    def setUp(self): TMP.mkdir(exist_ok=True); self.d = Path(tempfile.mkdtemp(dir=str(TMP)))
    def w(self, name, text): p = self.d / name; p.write_text(text); return p
    def test_conforming_module_with_matching_log_passes(self):
        rc, out = run(self.w("m.py", GOOD), self.w("log.txt", LOG_OK)); self.assertEqual(rc, 0, out)
    def test_bundled_assertions_are_refused(self):
        rc, out = run(self.w("m.py", BUNDLED)); self.assertIn("2 outcome assertions", out); self.assertEqual(rc, 2, out)
    def test_unlabelled_method_is_refused(self):
        rc, out = run(self.w("m.py", UNLABELLED)); self.assertIn("declares neither", out); self.assertEqual(rc, 2, out)
    def test_failfirst_that_passed_against_the_predecessor_is_refused(self):
        rc, out = run(self.w("m.py", GOOD), self.w("log.txt", LOG_FF_PASSED)); self.assertIn("PASSED against the predecessor", out); self.assertEqual(rc, 2, out)
    def test_positive_regression_that_failed_is_refused(self):
        rc, out = run(self.w("m.py", GOOD), self.w("log.txt", LOG_PR_FAILED)); self.assertIn("not an already-holding behaviour", out); self.assertEqual(rc, 2, out)
    def test_method_absent_from_the_log_is_refused(self):
        rc, out = run(self.w("m.py", GOOD), self.w("log.txt", "test_one (m.T) ... FAIL\n")); self.assertIn("absent from the predecessor log", out); self.assertEqual(rc, 2, out)
if __name__ == "__main__": unittest.main()
