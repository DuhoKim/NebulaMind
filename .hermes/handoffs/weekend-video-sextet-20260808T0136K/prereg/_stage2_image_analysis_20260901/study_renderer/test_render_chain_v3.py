"""Integration fixture for render_chain_v3 (v2 tests + binary64 radius counterexample + band indicator) — the receipts codex's V36 report required: through the ACTUAL renderer, (a) one zero-exposure
source pixel mapping OUTSIDE T renders (F = 1, SCORED); (b) one mapping INSIDE T refuses; (c) 819 flagged output pixels outside T are
allowed and 820 refuse; (d) MEDIUM pixels are carried, counted, never flagged; (e) the same outside-T zero-exposure case REFUSES through
renderer_v3 (the V35 chain), so the fixture fails on the old behaviour. Synthetic source: 180×180, identity-scale TAN WCS aligned so
source pixel (r, c) maps to output pixel (r − 26, c − 26) exactly."""
import unittest, sys
import numpy as np
from pathlib import Path
HERE = Path(__file__).resolve().parent; sys.path.insert(0, str(HERE.parent)); sys.path.insert(0, str(HERE.parent / "miniprereg_pins"))
from study_renderer import render_chain_v3 as rc, renderer_v3 as rv3, pixel_rejection_v2 as prj
from study_renderer.test_renderer_v4 import make_wcs
import protected_region_v2 as pr
R_T = pr.r_t_validation()          # 23
OFF = 26                           # source = output + 26 on both axes for make_wcs(width=height=180) and the 128×128 output

def source(blob=True):
    w = make_wcs(); yy, xx = np.indices((180, 180), dtype=np.float64)
    image = 1.0 + (5.0 * np.exp(-((yy - 89.5) ** 2 + (xx - 89.5) ** 2) / (2 * 6.0 ** 2)) if blob else np.zeros((180, 180)))
    return image, np.zeros((180, 180), dtype=np.int32), np.ones((180, 180), dtype=np.int32), w

def outside_T_source_pixels(n):
    """n source pixels whose OUTPUT images lie outside T: output rows 0..6 (distance to centre > 60 px)."""
    pts = [(r + OFF, c + OFF) for r in range(0, 7) for c in range(0, 128)]
    assert len(pts) >= n; return pts[:n]

class T(unittest.TestCase):
    def test_mapping_is_exact_offset(self):
        image, mb, nexp, w = source(); nexp[OFF + 5, OFF + 7] = 0
        r = rc.render_object(image, mb, nexp, w, 40.0, 10.0, "tile", R_T)
        self.assertEqual(r["status"], "SCORED"); self.assertEqual(r["F"], 1)
        # the flagged output pixel is (5, 7): recompute from the renderer to prove the offset
        raster = rc.rv4.render_cutout([(image, mb, nexp, w)], rc.rv4.RenderTarget(ra=40.0, dec=10.0, primary_tile_id="tile"))
        self.assertEqual([tuple(map(int, p)) for p in zip(*np.nonzero(np.asarray(raster.nexp) == 0))], [(5, 7)])
    def test_zero_exposure_outside_T_renders__v3_chain_refuses(self):
        image, mb, nexp, w = source(); nexp[OFF + 0, OFF + 0] = 0
        r = rc.render_object(image, mb, nexp, w, 40.0, 10.0, "tile", R_T)
        self.assertEqual(r["status"], "SCORED"); self.assertEqual((r["F"], r["n_zero_exposure_source"], r["medium_count"]), (1, 1, 0))
        self.assertEqual(len(r["tensor"]), 65536); self.assertEqual(r["tensor_sha256"], __import__("hashlib").sha256(r["tensor"]).hexdigest())
        cleaned, *_ = prj.clean_source(image, mb, nexp)
        with self.assertRaises(ValueError): rv3.render_cutout([(cleaned, mb, nexp, w)], rv3.RenderTarget(ra=40.0, dec=10.0, primary_tile_id="tile"))   # V35 chain
    def test_zero_exposure_inside_T_refuses(self):
        image, mb, nexp, w = source(); nexp[OFF + 63, OFF + 63] = 0
        r = rc.render_object(image, mb, nexp, w, 40.0, 10.0, "tile", R_T)
        self.assertEqual(r["status"], "REFUSED"); self.assertIn("F", r); self.assertEqual(r["F"], 1); self.assertNotIn("tensor", r)
    def test_ceiling_819_allowed_820_refused(self):
        for n, want in ((819, "SCORED"), (820, "REFUSED")):
            image, mb, nexp, w = source()
            for (rr, cc) in outside_T_source_pixels(n): mb[rr, cc] = 1 << 1     # BRIGHT
            r = rc.render_object(image, mb, nexp, w, 40.0, 10.0, "tile", R_T)
            self.assertEqual((r["F"], r["status"]), (n, want), n)
    def test_medium_carried_counted_not_flagged(self):
        image, mb, nexp, w = source(); mb[OFF + 63, OFF + 63] = 1 << 11; mb[OFF + 2, OFF + 2] = 1 << 11
        r = rc.render_object(image, mb, nexp, w, 40.0, 10.0, "tile", R_T)
        self.assertEqual(r["status"], "SCORED"); self.assertEqual(r["F"], 0); self.assertEqual(r["medium_count"], 2); self.assertEqual(r["n_medium_source"], 2)
        self.assertEqual(image[OFF + 63, OFF + 63], image[OFF + 63, OFF + 63])  # image untouched by MEDIUM (clean_source copies)
    def test_degenerate_peak_and_bad_planes_refuse(self):
        image, mb, nexp, w = source(blob=False); image[:] = 0.0
        self.assertEqual(rc.render_object(image, mb, nexp, w, 40.0, 10.0, "tile", R_T)["status"], "REFUSED")
        image, mb, nexp, w = source(); r = rc.render_object(image, mb.astype(np.float64), nexp, w, 40.0, 10.0, "tile", R_T)
        self.assertEqual(r["status"], "REFUSED"); self.assertIn("integer", r["reason"])
        nexp2 = nexp.copy(); nexp2[0, 0] = -1; self.assertEqual(rc.render_object(image, mb, nexp2, w, 40.0, 10.0, "tile", R_T)["status"], "REFUSED")
    def test_binary64_radius_codex_counterexample(self):
        image, mb, nexp, w = source(); nexp[OFF + 40, OFF + 63] = 0                     # output (40,63): distance 23.505 from the centre
        r = rc.render_object(image, mb, nexp, w, 40.0, 10.0, "tile", pr.r_t_main(3.1309))   # prescribed r_T = 23.9 → inside T → REFUSED
        self.assertEqual(r["status"], "REFUSED"); self.assertAlmostEqual(r["r_T"], 23.9, places=6)
        r23 = rc.render_object(image, mb, nexp, w, 40.0, 10.0, "tile", 23.0); self.assertEqual(r23["status"], "SCORED")   # with r_T = 23 the same flag is outside T
    def test_band_indicator_and_coords_retained(self):
        image, mb, nexp, w = source(); nexp[OFF + 30, OFF + 63] = 0                     # distance 33.5: outside T (23), inside the 64 band
        r = rc.render_object(image, mb, nexp, w, 40.0, 10.0, "tile", 23.0)
        self.assertEqual(r["status"], "SCORED"); self.assertTrue(r["asym_band_flag"]); self.assertEqual(r["flagged_coords"], [(30, 63)])
        image, mb, nexp, w = source(); nexp[OFF + 0, OFF + 0] = 0                       # distance 89.8: outside the band
        r = rc.render_object(image, mb, nexp, w, 40.0, 10.0, "tile", 23.0); self.assertFalse(r["asym_band_flag"])
if __name__ == "__main__": unittest.main()
