"""Pure in-memory renderer for the Tier-C handedness study."""
from __future__ import annotations

from dataclasses import dataclass
import hashlib
import json
from pathlib import Path
from typing import Any, Mapping, Sequence

import numpy as np

try:
    import astropy
    from astropy.wcs import WCS
except ImportError as exc:  # pragma: no cover
    raise RuntimeError("ASTROPY-ABSENT") from exc

WRONG_PARITY_REFUSAL = "WRONG-PARITY-REFUSAL"
WRONG_GEOMETRY_REFUSAL = "WRONG-GEOMETRY-REFUSAL"
CONFIG_GEOMETRY_MISMATCH = "PINNED-CONFIG-MISMATCH"
DATA_INTEGRITY_FAIL = "DATA-INTEGRITY-FAIL"

# The Section 8 prose constants.  No geometry is constructed until the pinned
# JSON has been loaded and compared field-for-field below.
_SECTION8_GEOMETRY = {
    "raster_width_pixels": 128, "raster_height_pixels": 128,
    "pixel_scale_arcsec": 0.262, "crpix1": 64.5, "crpix2": 64.5,
    "interpolation": "bilinear", "neighbour_policy": "stitch-neighbours-first",
    "orientation": "north-up/east-left", "parity_policy": "parity-preserve",
    "parity_refusal_token": WRONG_PARITY_REFUSAL,
}
_CONFIG = Path(__file__).resolve().parent.parent / "miniprereg_pins" / "render_config.json"
try:
    _loaded_geometry = json.loads(_CONFIG.read_text(encoding="utf-8"))
except (OSError, UnicodeError, json.JSONDecodeError) as exc:
    raise RuntimeError(CONFIG_GEOMETRY_MISMATCH) from exc
if _loaded_geometry != _SECTION8_GEOMETRY:
    raise RuntimeError(CONFIG_GEOMETRY_MISMATCH)
PINNED_GEOMETRY = dict(_loaded_geometry)

WIDTH = PINNED_GEOMETRY["raster_width_pixels"]
HEIGHT = PINNED_GEOMETRY["raster_height_pixels"]
PIXEL_SCALE_ARCSEC = PINNED_GEOMETRY["pixel_scale_arcsec"]
CRPIX = (PINNED_GEOMETRY["crpix1"], PINNED_GEOMETRY["crpix2"])
CD = np.array([[-PIXEL_SCALE_ARCSEC / 3600.0, 0.0],
               [0.0, PIXEL_SCALE_ARCSEC / 3600.0]], dtype=np.float64)

PROHIBITED_TRANSFORMS = ("resizing", "further interpolation", "rotation", "transpose",
    "PSF homogenization", "padding", "wrapping", "reflection",
    "intensity-conditioned source choice", "chirality-conditioned processing")


@dataclass(frozen=True)
class RenderTarget:
    ra: float
    dec: float
    geometry: Mapping[str, Any] | None = None


@dataclass(frozen=True)
class Raster:
    array: np.ndarray
    maskbits: np.ndarray
    nexp: np.ndarray
    wcs: WCS
    digest: str
    metadata: Mapping[str, Any]

    def canonical_bytes(self) -> bytes:
        return self.array.astype("<f8", copy=False).tobytes(order="C")


def _target_parts(target):
    if isinstance(target, RenderTarget):
        requested = dict(PINNED_GEOMETRY if target.geometry is None else target.geometry)
        ra, dec = target.ra, target.dec
    else:
        if not isinstance(target, (tuple, list)) or len(target) != 2:
            raise ValueError(WRONG_GEOMETRY_REFUSAL)
        ra, dec = target
        requested = dict(PINNED_GEOMETRY)
    if requested != PINNED_GEOMETRY:
        raise ValueError(WRONG_GEOMETRY_REFUSAL)
    ra, dec = np.float64(ra), np.float64(dec)
    if not np.isfinite(ra) or not np.isfinite(dec) or not 0 <= ra < 360 or not -90 <= dec <= 90:
        raise ValueError(DATA_INTEGRITY_FAIL)
    return float(ra), float(dec), requested


def _output_wcs(ra, dec):
    w = WCS(naxis=2)
    w.wcs.ctype = ["RA---TAN", "DEC--TAN"]
    w.wcs.cunit = ["deg", "deg"]
    w.wcs.crval = [ra, dec]
    w.wcs.crpix = CRPIX
    w.wcs.cd = CD.copy()
    w.array_shape = (HEIGHT, WIDTH)
    w.wcs.set()
    return w


def _tile_id(wcs, index):
    for key in ("tile_id", "name", "brick", "brickid"):
        value = getattr(wcs, key, None)
        if value is not None:
            return str(value)
    return f"tile-{index}"


def _jacobian(source_wcs, output_wcs, sx, sy):
    points = np.array([[sx, sy], [sx + 1.0, sy], [sx, sy + 1.0]])
    out = output_wcs.all_world2pix(source_wcs.all_pix2world(points, 0), 0)
    if not np.all(np.isfinite(out)):
        raise ValueError(DATA_INTEGRITY_FAIL)
    return np.column_stack((out[1] - out[0], out[2] - out[0]))


def _assert_parity(sources, output_wcs):
    for image, _, _, source_wcs in sources:
        h, w = image.shape
        points = ((w-1)/2, (h-1)/2), (0, 0), (w-1, 0), (0, h-1), (w-1, h-1), \
                 ((w-1)/2, 0), ((w-1)/2, h-1), (0, (h-1)/2), (w-1, (h-1)/2)
        signs = []
        for sx, sy in points:
            determinant = float(np.linalg.det(_jacobian(source_wcs, output_wcs, sx, sy)))
            if not np.isfinite(determinant) or determinant == 0:
                raise ValueError(DATA_INTEGRITY_FAIL)
            signs.append(1 if determinant > 0 else -1)
        if any(sign != signs[0] for sign in signs) or signs[0] != 1:
            raise ValueError(WRONG_PARITY_REFUSAL)
    return 1


def _assert_pixel_scales(sources):
    reference = None
    for _, _, _, wcs in sources:
        matrix = np.asarray(wcs.pixel_scale_matrix, dtype=np.float64)
        scales = np.linalg.norm(matrix, axis=0)
        if scales.shape != (2,) or not np.all(np.isfinite(scales)) or np.any(scales <= 0):
            raise ValueError(DATA_INTEGRITY_FAIL)
        if reference is None:
            reference = scales
        elif not np.allclose(scales, reference, rtol=1e-10, atol=0.0):
            raise ValueError(DATA_INTEGRITY_FAIL)


def _sample_stitched(sources, world, plane_index):
    result = np.full(world.shape[0], np.nan, dtype=np.float64)
    coords = [wcs.all_world2pix(world, 0) for *_, wcs in sources]
    for point_index in range(world.shape[0]):
        chosen = None
        for tile_index, (source, xy) in enumerate(zip(sources, coords)):
            plane = source[plane_index]
            x, y = xy[point_index]
            if -0.5 <= x <= plane.shape[1]-0.5 and -0.5 <= y <= plane.shape[0]-0.5:
                chosen = tile_index, float(x), float(y)
                break
        if chosen is None:
            raise ValueError(DATA_INTEGRITY_FAIL)
        base, x, y = chosen
        x0, y0 = int(np.floor(x)), int(np.floor(y))
        dx, dy = x-x0, y-y0
        values = []
        for yy, xx in ((y0,x0),(y0,x0+1),(y0+1,x0),(y0+1,x0+1)):
            value = None
            plane, wcs = sources[base][plane_index], sources[base][3]
            if 0 <= yy < plane.shape[0] and 0 <= xx < plane.shape[1]:
                value = plane[yy, xx]
            else:
                sky = wcs.all_pix2world([[xx, yy]], 0)
                for source in sources:
                    other, other_wcs = source[plane_index], source[3]
                    ox, oy = other_wcs.all_world2pix(sky, 0)[0]
                    oix, oiy = int(np.rint(ox)), int(np.rint(oy))
                    if abs(ox-oix) <= 1e-6 and abs(oy-oiy) <= 1e-6 and 0 <= oiy < other.shape[0] and 0 <= oix < other.shape[1]:
                        value = other[oiy, oix]
                        break
            if value is None or not np.isfinite(value):
                raise ValueError(DATA_INTEGRITY_FAIL)
            if plane_index == 2 and value <= 0:
                raise ValueError(DATA_INTEGRITY_FAIL)
            values.append(np.float64(value))
        v00, v10, v01, v11 = values
        result[point_index] = ((1-dx)*(1-dy)*v00 + dx*(1-dy)*v10 + (1-dx)*dy*v01 + dx*dy*v11)
    return result


def render_cutout(sources: Sequence[tuple[np.ndarray, np.ndarray, np.ndarray, WCS]], target) -> Raster:
    """Render ``(image, maskbits, nexp, WCS)`` tiles."""
    ra, dec, requested = _target_parts(target)
    if not sources:
        raise ValueError(DATA_INTEGRITY_FAIL)
    normalized = []
    for source in sources:
        if not isinstance(source, (tuple, list)) or len(source) != 4:
            raise ValueError(DATA_INTEGRITY_FAIL)
        image, maskbits, nexp, wcs = source
        planes = tuple(np.asarray(p) for p in (image, maskbits, nexp))
        if not isinstance(wcs, WCS) or any(p.ndim != 2 for p in planes) or len({p.shape for p in planes}) != 1:
            raise ValueError(DATA_INTEGRITY_FAIL)
        if not np.issubdtype(planes[2].dtype, np.integer):
            raise ValueError(DATA_INTEGRITY_FAIL)
        if any(not np.all(np.isfinite(p)) for p in planes):
            raise ValueError(DATA_INTEGRITY_FAIL)
        normalized.append((*planes, wcs))
    _assert_pixel_scales(normalized)
    output_wcs = _output_wcs(ra, dec)
    sign = _assert_parity(normalized, output_wcs)
    yy, xx = np.indices((HEIGHT, WIDTH), dtype=np.float64)
    world = output_wcs.all_pix2world(np.column_stack((xx.ravel(), yy.ravel())), 0)
    outputs = [_sample_stitched(normalized, world, i).reshape(HEIGHT, WIDTH) for i in range(3)]
    if np.any(outputs[2] <= 0):
        raise ValueError(DATA_INTEGRITY_FAIL)
    for output in outputs:
        output.setflags(write=False)
    canonical = outputs[0].astype("<f8", copy=False).tobytes(order="C")
    digest = hashlib.sha256(canonical).hexdigest()
    metadata = {**requested, "cd_matrix_deg_per_pixel": tuple(map(tuple, CD)), "crval": (ra, dec),
        "projection": "TAN", "tile_ids": tuple(_tile_id(s[3], i) for i,s in enumerate(normalized)),
        "source_to_output_jacobian_sign": sign, "digest": digest, "canonical_dtype": "<f8",
        "canonical_order": "C", "astropy_version": astropy.__version__,
        "prohibited_transforms": PROHIBITED_TRANSFORMS}
    return Raster(outputs[0], outputs[1], outputs[2], output_wcs, digest, metadata)


__all__ = ["Raster", "RenderTarget", "render_cutout", "PINNED_GEOMETRY", "PROHIBITED_TRANSFORMS",
    "WRONG_PARITY_REFUSAL", "WRONG_GEOMETRY_REFUSAL", "CONFIG_GEOMETRY_MISMATCH", "DATA_INTEGRITY_FAIL"]
