import unittest

import numpy as np
from astropy.wcs import WCS

from study_renderer.renderer import (
    CD,
    PINNED_GEOMETRY,
    PROHIBITED_TRANSFORMS,
    RenderTarget,
    WRONG_GEOMETRY_REFUSAL,
    WRONG_PARITY_REFUSAL,
    render_cutout,
)


def make_wcs(ra=40.0, dec=10.0, width=180, height=180, *, flipped=False, x_shift=0.0, tile_id="tile"):
    w = WCS(naxis=2)
    w.wcs.ctype = ["RA---TAN", "DEC--TAN"]
    w.wcs.cunit = ["deg", "deg"]
    w.wcs.crval = [ra, dec]
    w.wcs.crpix = [(width + 1) / 2 + x_shift, (height + 1) / 2]
    w.wcs.cd = CD.copy()
    if flipped:
        w.wcs.cd[0, 0] *= -1
    w.array_shape = (height, width)
    w.tile_id = tile_id
    w.wcs.set()
    return w


def sky_field(w, shape):
    yy, xx = np.indices(shape, dtype=np.float64)
    world = w.all_pix2world(np.column_stack((xx.ravel(), yy.ravel())), 0)
    return (3.0 * world[:, 0] + 7.0 * world[:, 1]).reshape(shape)


class StudyRendererTests(unittest.TestCase):
    def test_a_north_up_east_left_markers(self):
        w = make_wcs()
        image = np.zeros((180, 180), dtype=np.float64)
        image[108, 89] = 10.0  # North of target (+y in FITS pixel coordinates).
        image[89, 70] = 20.0  # East of target: x decreases as RA increases.
        raster = render_cutout([(image, w)], (40.0, 10.0))
        north_window = raster.array[:, 58:69]
        north_local = np.unravel_index(np.argmax(north_window), north_window.shape)
        north = (north_local[0], north_local[1] + 58)
        east_window = raster.array[58:69, :]
        east_local = np.unravel_index(np.argmax(east_window), east_window.shape)
        east = (east_local[0] + 58, east_local[1])
        self.assertGreater(north[0], 63, "north up = +y")
        self.assertLess(east[1], 64, "east left = -x")

    def test_b_wrong_parity_refusal(self):
        with self.assertRaisesRegex(ValueError, f"^{WRONG_PARITY_REFUSAL}$"):
            render_cutout([(np.ones((180, 180)), make_wcs(flipped=True))], (40.0, 10.0))

    def test_c_two_tile_boundary_has_no_seam(self):
        left_w = make_wcs(width=90, x_shift=45.0, tile_id="left")
        right_w = make_wcs(width=90, x_shift=-45.0, tile_id="right")
        left = sky_field(left_w, (180, 90))
        right = sky_field(right_w, (180, 90))
        raster = render_cutout([(left, left_w), (right, right_w)], (40.0, 10.0))
        expected = sky_field(raster.wcs, raster.array.shape)
        np.testing.assert_allclose(raster.array, expected, rtol=0.0, atol=2e-10)
        self.assertEqual(raster.metadata["tile_ids"], ("left", "right"))

    def test_d_mirrored_input_yields_mirrored_raster(self):
        w = make_wcs()
        yy, xx = np.indices((180, 180), dtype=np.float64)
        image = np.exp(-((xx - 72.0) ** 2 + (yy - 96.0) ** 2) / 80.0)
        original = render_cutout([(image, w)], (40.0, 10.0))
        mirrored = render_cutout([(image[:, ::-1], w)], (40.0, 10.0))
        np.testing.assert_allclose(mirrored.array, original.array[:, ::-1], rtol=0.0, atol=2e-12)

    def test_e_determinism_binary64_bytes(self):
        w = make_wcs()
        image = sky_field(w, (180, 180))
        one = render_cutout([(image, w)], (40.0, 10.0))
        two = render_cutout([(image, w)], (40.0, 10.0))
        self.assertEqual(one.canonical_bytes(), two.canonical_bytes(), "binary64 bytes differ")
        self.assertEqual(one.digest, two.digest, "SHA-256 digest differs")

    def test_f_wrong_geometry_refusal(self):
        w = make_wcs()
        for key, value in (("pixel_scale_arcsec", 0.3), ("raster_width_pixels", 127), ("crpix1", 64.0)):
            geometry = dict(PINNED_GEOMETRY)
            geometry[key] = value
            with self.subTest(key=key), self.assertRaisesRegex(ValueError, f"^{WRONG_GEOMETRY_REFUSAL}$"):
                render_cutout([(np.ones((180, 180)), w)], RenderTarget(40.0, 10.0, geometry))

    def test_g_exact_target_cd_matrix(self):
        raster = render_cutout([(np.ones((180, 180)), make_wcs())], (40.0, 10.0))
        np.testing.assert_array_equal(raster.wcs.wcs.cd, CD)
        self.assertEqual(raster.wcs.wcs.crpix.tolist(), [64.5, 64.5])

    def test_prohibited_transforms_are_only_declarations(self):
        self.assertEqual(len(PROHIBITED_TRANSFORMS), 10)
        for name in ("resize", "rotate", "transpose", "reflect", "wrap", "pad"):
            module = __import__("study_renderer.renderer", fromlist=["renderer"])
            self.assertFalse(hasattr(module, name), f"prohibited operation implemented: {name}")


if __name__ == "__main__":
    unittest.main()
