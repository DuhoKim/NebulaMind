"""Fixture for pixel_rejection_v2: asserts the V15 §6 identity BOTH WAYS, and — on the SAME inputs — that the V35 module
(pixel_rejection.py, unchanged) behaves differently, so this fixture FAILS if pointed at the old behaviour."""
import unittest, sys
from pathlib import Path
import numpy as np
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from study_renderer import pixel_rejection_v2 as V2
from study_renderer import pixel_rejection as V1

def planes(n=8):
    img = np.arange(n * n, dtype=np.float64).reshape(n, n) + 100.0
    mb = np.zeros((n, n), dtype=np.int32); nexp = np.ones((n, n), dtype=np.int32)
    return img, mb, nexp

class T(unittest.TestCase):
    def test_set_both_ways(self):
        self.assertEqual(V2.REJECT_BITS, (1, 3, 6, 10, 13)); self.assertNotIn(11, V2.REJECT_BITS)
        self.assertEqual(V2.REJECT_MASK, (1 << 1) | (1 << 3) | (1 << 6) | (1 << 10) | (1 << 13))
        img, mb, nexp = planes()
        for bit in V2.REJECT_BITS:
            m = mb.copy(); m[2, 2] = 1 << bit; self.assertTrue(V2.rejection_mask(m, nexp)[2, 2], bit)
        for bit in V2.NOT_REJECTED:
            m = mb.copy(); m[2, 2] = 1 << bit; self.assertFalse(V2.rejection_mask(m, nexp)[2, 2], bit)
    def test_medium_is_carried_not_replaced__old_module_replaces_it(self):
        img, mb, nexp = planes(); mb[3, 3] = 1 << 11
        cleaned, fill, n_rej, n_zero, n_med = V2.clean_source(img, mb, nexp)
        self.assertEqual(n_rej, 0); self.assertEqual(n_med, 1); self.assertEqual(cleaned[3, 3], img[3, 3])
        self.assertEqual(V2.medium_count(mb), 1); self.assertFalse(V2.flagged_output(mb, nexp).any())
        old_cleaned, _, old_n = V1.clean_source(img, mb)                   # the V35 behaviour on the same input
        self.assertEqual(old_n, 1); self.assertNotEqual(old_cleaned[3, 3], img[3, 3]); self.assertIn(11, V1.REJECT_BITS)
    def test_zero_exposure_rejects_and_flags__old_module_ignores_nexp(self):
        img, mb, nexp = planes(); nexp[5, 1] = 0
        cleaned, fill, n_rej, n_zero, n_med = V2.clean_source(img, mb, nexp)
        self.assertEqual((n_rej, n_zero, n_med), (1, 1, 0)); self.assertEqual(cleaned[5, 1], fill); self.assertNotEqual(cleaned[5, 1], img[5, 1])
        self.assertTrue(V2.flagged_output(mb, nexp)[5, 1]); self.assertEqual(int(V2.flagged_output(mb, nexp).sum()), 1)
        old_cleaned, _, old_n = V1.clean_source(img, mb)                   # V1 has no nexp input: the pixel survives untouched
        self.assertEqual(old_n, 0); self.assertEqual(old_cleaned[5, 1], img[5, 1])
    def test_replacement_is_lower_median_of_accepted_and_excludes_zero_exposure(self):
        img, mb, nexp = planes(8); nexp[0, 0] = 0; img[0, 0] = 1e9          # the unexposed pixel must not enter the median
        cleaned, fill, *_ = V2.clean_source(img, mb, nexp)
        acc = np.sort(np.delete(img.ravel(), 0)); self.assertEqual(fill, acc[(acc.size - 1) // 2]); self.assertEqual(cleaned[0, 0], fill)
    def test_refusals(self):
        img, mb, nexp = planes()
        with self.assertRaises(ValueError): V2.rejection_mask(mb.astype(np.float64), nexp)
        with self.assertRaises(ValueError): V2.rejection_mask(mb, nexp.astype(np.float32))
        with self.assertRaises(ValueError): V2.rejection_mask(mb, nexp[:4])
        bad = nexp.copy(); bad[0, 0] = -1
        with self.assertRaises(ValueError): V2.zero_exposure_mask(bad)
        img4, mb4, n4 = planes(4); n4[:] = 0; n4[0, :3] = 1                # 3 accepted < 16
        with self.assertRaises(ValueError) as c: V2.clean_source(img4, mb4, n4)
        self.assertEqual(str(c.exception), V2.NO_ACCEPTED_PIXELS)
    def test_bit_and_zero_exposure_combine(self):
        img, mb, nexp = planes(); mb[1, 1] = 1 << 1; nexp[6, 6] = 0; mb[7, 7] = 1 << 11
        f = V2.flagged_output(mb, nexp); self.assertEqual(int(f.sum()), 2); self.assertTrue(f[1, 1] and f[6, 6]); self.assertFalse(f[7, 7])
if __name__ == "__main__": unittest.main()
