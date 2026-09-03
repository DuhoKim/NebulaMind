import unittest
import numpy as np
from astropy.wcs import WCS

from study_renderer.renderer import (CD, DATA_INTEGRITY_FAIL, PINNED_GEOMETRY,
    PROHIBITED_TRANSFORMS, RenderTarget, WRONG_GEOMETRY_REFUSAL,
    WRONG_PARITY_REFUSAL, render_cutout)


def make_wcs(ra=40.0, dec=10.0, width=180, height=180, *, flipped=False,
             x_shift=0.0, tile_id="tile", scale=1.0):
    w = WCS(naxis=2)
    w.wcs.ctype = ["RA---TAN", "DEC--TAN"]
    w.wcs.cunit = ["deg", "deg"]
    w.wcs.crval = [ra, dec]
    w.wcs.crpix = [(width+1)/2+x_shift, (height+1)/2]
    w.wcs.cd = CD.copy() * scale
    if flipped: w.wcs.cd[0, 0] *= -1
    w.array_shape = (height, width); w.tile_id = tile_id; w.wcs.set()
    return w


def sky_field(w, shape):
    yy, xx = np.indices(shape, dtype=np.float64)
    world = w.all_pix2world(np.column_stack((xx.ravel(), yy.ravel())), 0)
    # Wrap-safe locally smooth field.
    return (3*np.unwrap(np.deg2rad(world[:,0])) + 7*np.deg2rad(world[:,1])).reshape(shape)


def tile(image, w):
    return image, np.zeros(image.shape), np.ones(image.shape,dtype=np.int16), w


class EdgeFlipWCS(WCS):
    def all_pix2world(self, pix, origin, *args, **kwargs):
        p = np.asarray(pix, dtype=float).copy()
        # Identity at the centre, x reflection at the far right edge.
        p[:, 0] = np.where(p[:, 0] > 170, 340-p[:, 0], p[:, 0])
        return super().all_pix2world(p, origin, *args, **kwargs)


class StudyRendererTests(unittest.TestCase):
    def assert_data_fail(self, sources, target=(40.,10.)):
        with self.assertRaisesRegex(ValueError, f"^{DATA_INTEGRITY_FAIL}$"):
            render_cutout(sources, target)

    def test_north_up_east_left(self):
        w=make_wcs(); image=np.zeros((180,180)); image[108,89]=10; image[89,70]=20
        r=render_cutout([tile(image,w)], (40.,10.))
        self.assertGreater(np.unravel_index(np.argmax(r.array[:,58:69]),r.array[:,58:69].shape)[0],63)
        self.assertLess(np.unravel_index(np.argmax(r.array[58:69]),r.array[58:69].shape)[1],64)

    def test_wrong_parity_refusal(self):
        with self.assertRaisesRegex(ValueError, f"^{WRONG_PARITY_REFUSAL}$"):
            render_cutout([tile(np.ones((180,180)),make_wcs(flipped=True))],(40.,10.))

    def test_edge_of_raster_parity_flip_refuses(self):
        base=make_wcs(); w=EdgeFlipWCS(base.to_header()); w.array_shape=(180,180)
        with self.assertRaisesRegex(ValueError, f"^{WRONG_PARITY_REFUSAL}$"):
            render_cutout([tile(np.ones((180,180)),w)],(40.,10.))

    def test_two_tile_boundary_and_three_planes(self):
        lw=make_wcs(width=90,x_shift=45,tile_id="left"); rw=make_wcs(width=90,x_shift=-45,tile_id="right")
        left,right=sky_field(lw,(180,90)),sky_field(rw,(180,90))
        r=render_cutout([tile(left,lw),tile(right,rw)],(40.,10.))
        np.testing.assert_allclose(r.array,sky_field(r.wcs,r.array.shape),atol=2e-10,rtol=0)
        np.testing.assert_array_equal(r.maskbits,np.zeros((128,128)))
        np.testing.assert_array_equal(r.nexp,np.ones((128,128)))

    def test_determinism(self):
        w=make_wcs(); s=[tile(sky_field(w,(180,180)),w)]
        a,b=render_cutout(s,(40.,10.)),render_cutout(s,(40.,10.))
        self.assertEqual(a.canonical_bytes(),b.canonical_bytes()); self.assertEqual(a.digest,b.digest)

    def test_wrong_geometry(self):
        g=dict(PINNED_GEOMETRY); g["crpix1"]=64.0
        with self.assertRaisesRegex(ValueError,f"^{WRONG_GEOMETRY_REFUSAL}$"):
            render_cutout([tile(np.ones((180,180)),make_wcs())],RenderTarget(40,10,g))

    def test_ra_wrap_zero_360(self):
        for ra in (0.0001,359.9999):
            w=make_wcs(ra=ra); r=render_cutout([tile(np.ones((180,180)),w)],(ra,10))
            self.assertTrue(np.all(r.array==1))

    def test_dec_near_poles(self):
        for dec in (-89.9,89.9):
            w=make_wcs(dec=dec); r=render_cutout([tile(np.ones((180,180)),w)],(40,dec))
            self.assertTrue(np.all(r.array==1))

    def test_empty_tile_list(self): self.assert_data_fail([])

    def test_nan_in_each_plane(self):
        for index in range(3):
            planes=[np.ones((180,180)) for _ in range(3)]; planes[index][0,0]=np.nan
            self.assert_data_fail([(*planes,make_wcs())])

    def test_inconsistent_pixel_scales(self):
        self.assert_data_fail([tile(np.ones((180,180)),make_wcs()),tile(np.ones((180,180)),make_wcs(scale=1.01))])

    def test_missing_maskbits_or_nexp(self):
        w=make_wcs(); image=np.ones((180,180))
        self.assert_data_fail([(image,w)])
        self.assert_data_fail([(image,np.zeros_like(image),w)])

    def test_zero_nexp_pixel_refuses(self):
        w=make_wcs(); image=np.ones((180,180)); nexp=np.ones((180,180),dtype=np.int16)
        nexp[90,90]=0
        self.assert_data_fail([(image,np.zeros_like(image),nexp,w)])

    def test_noninteger_nexp_refuses(self):
        w=make_wcs(); image=np.ones((180,180))
        self.assert_data_fail([(image,np.zeros_like(image),np.ones_like(image),w)])

    def test_exact_geometry_and_prohibitions(self):
        r=render_cutout([tile(np.ones((180,180)),make_wcs())],(40,10))
        np.testing.assert_array_equal(r.wcs.wcs.cd,CD); self.assertEqual(r.wcs.wcs.crpix.tolist(),[64.5,64.5])
        self.assertEqual(len(PROHIBITED_TRANSFORMS),10)


if __name__ == "__main__": unittest.main()
