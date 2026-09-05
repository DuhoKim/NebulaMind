import sys, unittest, hashlib
from pathlib import Path
import numpy as np
HERE = Path(__file__).resolve().parent; sys.path.insert(0, str(HERE))
import fourier_chirality as fc
from w_chi_vendored import synth_spiral, synth_disk        # vendored copy of spike/yui_identity/w_chi.py — self-contained fixture

class T(unittest.TestCase):
    def test_antisymmetry_exact_negation_on_finite_unequal(self):
        for i in range(20):
            x = synth_spiral(1 if i % 2 else -1, 15 + i, 10 + 2 * i, 5.0, seed=i)
            a, b = fc.chi(x), fc.chi(fc.mirror(x)); self.assertNotEqual(float(a), 0.0)
            self.assertEqual(a.view(np.uint32), (-b).view(np.uint32))
    def test_determinism_bytes(self):
        x = synth_spiral(1, 20, 30, 3.0, seed=7)
        self.assertEqual(hashlib.sha256(np.float32(fc.chi(x)).tobytes()).hexdigest(), hashlib.sha256(np.float32(fc.chi(x.copy())).tobytes()).hexdigest())
    def test_sign_on_ideal_spirals_both_parities(self):
        s_plus = [fc.sign(synth_spiral(+1, p, inc, 50.0, seed=100 + p)) for p in range(10, 40, 3) for inc in (0, 30, 50)]
        s_minus = [fc.sign(synth_spiral(-1, p, inc, 50.0, seed=200 + p)) for p in range(10, 40, 3) for inc in (0, 30, 50)]
        self.assertTrue(len(set(s_plus)) == 1 and len(set(s_minus)) == 1 and s_plus[0] == -s_minus[0])
    def test_null_disk_is_small(self):
        vals = [abs(float(fc.chi(synth_disk(20, 8.0, seed=i)))) for i in range(50)]
        sig = [abs(float(fc.chi(synth_spiral(1, 20, 20, 8.0, seed=i)))) for i in range(50)]
        self.assertLess(np.median(vals), 0.5 * np.median(sig))
    def test_tie_is_zero_not_a_score(self):
        x = np.zeros((128, 128)); x[60:68, 60:68] = 1.0
        self.assertEqual(float(fc.chi(x)), 0.0); self.assertEqual(fc.sign(x), 0)
    def test_mirror_is_exact_involution(self):
        x = np.random.default_rng(0).standard_normal((128, 128)); self.assertTrue(np.array_equal(fc.mirror(fc.mirror(x)), x))
    def test_w_bounded(self):
        x = np.random.default_rng(3).standard_normal((128, 128)) * 1e6; self.assertLessEqual(abs(fc.w(x)), 1.0)
    def test_grid_is_96_distinct_in_lexicographic_order(self):
        cfgs = fc.enumerate_configs(); self.assertEqual(len(cfgs), 96)
        ids = [fc.config_id(c) for c in cfgs]; self.assertEqual(len(set(ids)), 96)
        keys = list(fc.CONFIG_GRID)
        for a, b in zip(cfgs, cfgs[1:]):
            self.assertLess([fc.CONFIG_GRID[k].index(a[k]) for k in keys], [fc.CONFIG_GRID[k].index(b[k]) for k in keys])
    def test_every_config_instantiates_and_is_antisymmetric(self):
        x = synth_spiral(1, 25, 40, 6.0, seed=11)
        for cfg in fc.enumerate_configs():
            e = fc.Estimator(cfg); a, b = e.chi(x), e.chi(fc.mirror(x))
            if float(a) == 0.0: self.assertEqual(float(b), 0.0)                     # a tie must be a tie in BOTH orders (both +0.0)
            else: self.assertEqual(a.view(np.uint32), (-b).view(np.uint32))          # otherwise exact negation
    def test_out_of_grid_config_refused(self):
        bad = dict(fc.DEFAULT_CFG); bad["R_MIN"] = 5
        with self.assertRaises(ValueError): fc.Estimator(bad)

if __name__ == "__main__":
    unittest.main()
