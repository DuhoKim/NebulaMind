"""protected_region_v2: r_T in binary64 without truncation; the V35 module (unchanged) truncates — asserted on the same inputs."""
import unittest, sys, math
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
import protected_region_v2 as P2, protected_region as P1
class T(unittest.TestCase):
    def test_codex_counterexample_shape_r_3_1309(self):
        r2 = P2.r_t_main(3.1309); r1 = P1.r_t_main(3.1309)
        self.assertAlmostEqual(r2, 23.9, places=6); self.assertEqual(r1, 23)                       # V35 truncates; V38 does not
        d = math.hypot(40 - 63.5, 63 - 63.5); self.assertLess(d, r2); self.assertGreater(d, r1)
        self.assertIsNotNone(P2.refuse_on_contamination([(40, 63)], r2)); self.assertIsNone(P1.refuse_on_contamination([(40, 63)], r1))
    def test_floor_cap_and_validation_constant(self):
        self.assertEqual(P2.r_t_main(0.0), 23.0); self.assertEqual(P2.r_t_main(100.0), 64.0); self.assertEqual(P2.r_t_validation(), 23.0)
        self.assertIsInstance(P2.r_t_main(1.0), float); self.assertEqual(P2.r_t_main(3.0), min(64.0, max(23.0, 2.0 * 3.0 / 0.262)))
    def test_refusals_unchanged(self):
        with self.assertRaises(ValueError): P2.r_t_main(None)
        with self.assertRaises(ValueError): P2.r_t_main(float("nan"))
        with self.assertRaises(ValueError): P2.r_t_main(-1.0)
        self.assertIsNotNone(P2.refuse_on_contamination([(0, 0)] * 820, 23.0)); self.assertIsNone(P2.refuse_on_contamination([(0, 0)] * 819, 23.0))
        self.assertIsNotNone(P2.refuse_on_contamination([(63, 63)], 23.0))
if __name__ == "__main__": unittest.main()
