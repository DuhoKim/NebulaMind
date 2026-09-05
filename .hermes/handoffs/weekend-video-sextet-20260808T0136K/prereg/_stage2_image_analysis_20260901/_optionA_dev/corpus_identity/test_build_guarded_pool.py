import json, math, unittest
from pathlib import Path
import numpy as np
import build_guarded_pool as m

class GuardedPoolTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.ok=m.build()
        with open(Path(__file__).with_name('guarded_pool_receipt.json')) as f: cls.receipt=json.load(f)

    def test_real_controls(self):
        self.assertTrue(self.ok)
        self.assertEqual((self.receipt['pool_count'],self.receipt['guard_dropped_count'],self.receipt['guarded_pool_count']),(12100,46,12054))

    def test_inclusive_synthetic_guard(self):
        # Same point must be dropped; a remote point must not.
        c=[(1,10.0,20.0,1),(2,30.0,40.0,-1)]
        got=m.guard_mask(c,np.array([[10.0,20.0]],dtype=np.float64))
        self.assertEqual(got.tolist(),[True,False])
        self.assertEqual(m.R_GUARD_ARCSEC,(33.536/2)*math.sqrt(2))

if __name__=='__main__': unittest.main()
