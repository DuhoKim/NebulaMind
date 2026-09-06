"""Gate v3 controls (Blanc 07:33; relocation-safe per Blanc 07:49). The boundary MUST refuse a child that prints 'Ran 1 / OK' and exits 17 (codex's probe);
v2 accepting the same log is the fail-first exhibit of the defect; a genuine exit-0 child passes; a tampered full output fails; the '## DONE' marker is not a suite;
an ABSOLUTE suite dir in status.tsv is refused (relocation must be impossible to get wrong). The tamper test builds its OWN fixture through the real runner inside
its OWN temporary directory (outside gate_fixtures/), tampers only there, and PROVES the written path lies inside that directory; a control shows the guard refusing
a target outside it. Beside the 05:48 fixtures (scripts/test_aggregate_gate.py, unchanged)."""
import subprocess, sys, unittest, shutil, tempfile, os
from pathlib import Path
HERE = Path(__file__).resolve().parent; V2 = HERE / "aggregate_gate.py"; V3 = HERE / "aggregate_gate_v3.py"; RUNNER = HERE / "run_suites.sh"; FX = HERE / "gate_fixtures"
TMP_ROOT = HERE.parent / "_tmp_gate_v3_tests"      # lane-scoped scratch, NOT inside gate_fixtures/
def v3(log, status, suites=1, tests=1): r = subprocess.run([sys.executable, str(V3), str(log), "--suites", str(suites), "--tests", str(tests), "--status", str(status)], capture_output=True, text=True); return r.returncode, r.stdout
def inside(target: Path, root: Path) -> Path:
    """the ONLY way the tamper test obtains a path to write: refuses anything not strictly inside root"""
    t, r = target.resolve(), root.resolve()
    if r not in t.parents: raise PermissionError(f"refusing to write outside the test's own directory: {t} not under {r}")
    return t
def build_child(tmp: Path, code: int):
    child = tmp / "synthetic_child.py"; child.write_text(f'import sys; sys.stderr.write("Ran 1 test in 0.001s\\n\\nOK\\n"); sys.exit({code})\n')
    spec = tmp / "spec.tsv"; spec.write_text(f"cmd:{sys.executable} {child}\n"); run = tmp / "run"; log = tmp / "log.txt"
    r = subprocess.run(["zsh", str(RUNNER), str(spec), str(run), str(log)], capture_output=True, text=True); assert r.returncode == 0, r.stderr
    return log, run / "status.tsv"
class GateV3(unittest.TestCase):
    def setUp(self): TMP_ROOT.mkdir(exist_ok=True); self.tmp = Path(tempfile.mkdtemp(prefix="gate_v3_", dir=str(TMP_ROOT)))
    def tearDown(self): shutil.rmtree(self.tmp, ignore_errors=True)
    def test_exit17_with_ok_text_is_refused(self):
        rc, out = v3(FX / "exit17_ok_text/log.txt", FX / "exit17_ok_text/run/status.tsv"); self.assertEqual(rc, 2, out); self.assertIn("EXIT 17", out); self.assertIn("rc=17", out)
    def test_v2_accepts_the_same_log__the_defect_exhibited(self):
        r = subprocess.run([sys.executable, str(V2), str(FX / "exit17_ok_text/log.txt"), "--suites", "1", "--tests", "1"], capture_output=True, text=True); self.assertEqual(r.returncode, 0, r.stdout)
    def test_genuine_exit0_child_passes(self):
        rc, out = v3(FX / "exit0_ok_text/log.txt", FX / "exit0_ok_text/run/status.tsv"); self.assertEqual(rc, 0, out); self.assertIn("EXIT 0", out)
    def test_fresh_exit17_through_the_real_runner_is_refused(self):
        log, st = build_child(self.tmp, 17); rc, out = v3(log, st); self.assertEqual(rc, 2, out); self.assertIn("rc=17", out)
    def test_tampered_full_output_is_refused__writes_only_inside_own_tmp(self):
        log, st = build_child(self.tmp, 0); rc, out = v3(log, st); self.assertEqual(rc, 0, out)             # passes before tampering
        row = st.read_text().strip().split("\t"); self.assertFalse(os.path.isabs(row[5]), "status.tsv dir must be RELATIVE"); target = inside(st.parent / row[5] / "stderr.txt", self.tmp)
        self.assertTrue(target.exists()); target.write_text("Ran 1 test in 0.001s\n\nOK\n\n"); rc, out = v3(log, st); self.assertEqual(rc, 2, out); self.assertIn("do not match the digests", out)
    def test_control__guard_refuses_a_target_outside_own_tmp(self):
        live = FX / "exit0_ok_text/run/status.tsv"; d = live.parent / live.read_text().strip().split("\t")[5] / "stderr.txt"; before = d.read_bytes()
        with self.assertRaises(PermissionError): inside(d, self.tmp)
        self.assertEqual(d.read_bytes(), before)                                                            # the live fixture is byte-identical
    def test_absolute_suite_dir_is_refused(self):
        log, st = build_child(self.tmp, 0); rows = [r.split("\t") for r in st.read_text().strip().split("\n")]; rows[0][5] = str((st.parent / rows[0][5]).resolve())
        st2 = self.tmp / "status_abs.tsv"; st2.write_text("\n".join("\t".join(r) for r in rows) + "\n"); shutil.copytree(st.parent / rows[0][5].split("/")[-1], self.tmp / rows[0][5].split("/")[-1], dirs_exist_ok=True)
        rc, out = v3(log, st2); self.assertEqual(rc, 2, out); self.assertIn("ABSOLUTE suite dir", out)
    def test_done_marker_is_not_a_suite(self):
        rc, out = v3(FX / "exit0_ok_text/log.txt", FX / "exit0_ok_text/run/status.tsv", suites=2, tests=1); self.assertEqual(rc, 2, out); self.assertIn("1 suite blocks, 2 required", out)
if __name__ == "__main__": unittest.main()
