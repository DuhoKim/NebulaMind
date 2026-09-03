"""Draft, in-memory-only renderer for the Tier-C handedness study.

This module deliberately has no filesystem or FITS I/O.  It accepts already
materialized arrays and astropy WCS objects, constructs one virtual stitched
source mosaic, and evaluates exactly one bilinear interpolation into the
frozen output WCS.
"""

from __future__ import annotations

from dataclasses import dataclass
import hashlib
from typing import Any, Mapping, Sequence

import numpy as np

try:
    import astropy
    from astropy.wcs import WCS
except ImportError as exc:  # pragma: no cover - required dependency gate
    raise RuntimeError("ASTROPY-ABSENT") from exc


WRONG_PARITY_REFUSAL = "WRONG-PARITY-REFUSAL"
WRONG_GEOMETRY_REFUSAL = "WRONG-GEOMETRY-REFUSAL"
DATA_INTEGRITY_FAIL = "DATA-INTEGRITY-FAIL"

WIDTH = 128
HEIGHT = 128
PIXEL_SCALE_ARCSEC = 0.262
CRPIX = (64.5, 64.5)
CD = np.array(
    [[-0.262 / 3600.0, 0.0], [0.0, 0.262 / 3600.0]], dtype=np.float64
)
INTERPOLATION = "bilinear"
NEIGHBOUR_POLICY = "stitch-neighbours-first"
ORIENTATION = "north-up/east-left"
PARITY_POLICY = "parity-preserve"

PINNED_GEOMETRY = {
        "raster_width_pixels": WIDTH,
        "raster_height_pixels": HEIGHT,
        "pixel_scale_arcsec": PIXEL_SCALE_ARCSEC,
        "crpix1": CRPIX[0],
        "crpix2": CRPIX[1],
        "interpolation": INTERPOLATION,
        "neighbour_policy": NEIGHBOUR_POLICY,
        "orientation": ORIENTATION,
        "parity_policy": PARITY_POLICY,
        "parity_refusal_token": WRONG_PARITY_REFUSAL,
    }

PROHIBITED_TRANSFORMS = (
    "resizing",
    "further interpolation",
    "rotation",
    "transpose",
    "PSF homogenization",
    "padding",
    "wrapping",
    "reflection",
    "intensity-conditioned source choice",
    "chirality-conditioned processing",
)


@dataclass(frozen=True)
class RenderTarget:
    """Target coordinate plus an inspectable request for the frozen geometry."""

    ra: float
    dec: float
    geometry: Mapping[str, Any] | None = None


@dataclass(frozen=True)
class Raster:
    array: np.ndarray
    wcs: WCS
    digest: str
    metadata: Mapping[str, Any]

    def canonical_bytes(self) -> bytes:
        return self.array.astype("<f8", copy=False).tobytes(order="C")


def _target_parts(target: tuple[float, float] | RenderTarget) -> tuple[float, float, dict[str, Any]]:
    if isinstance(target, RenderTarget):
        requested = dict(PINNED_GEOMETRY if target.geometry is None else target.geometry)
        ra, dec = target.ra, target.dec
    else:
        if not isinstance(target, (tuple, list)) or len(target) != 2:
            raise ValueError(WRONG_GEOMETRY_REFUSAL)
        ra, dec = target
        requested = dict(PINNED_GEOMETRY)
    if requested != dict(PINNED_GEOMETRY):
        raise ValueError(WRONG_GEOMETRY_REFUSAL)
    ra, dec = np.float64(ra), np.float64(dec)
    if not np.isfinite(ra) or not np.isfinite(dec):
        raise ValueError(DATA_INTEGRITY_FAIL)
    return float(ra), float(dec), requested


def _output_wcs(ra: float, dec: float) -> WCS:
    wcs = WCS(naxis=2)
    wcs.wcs.ctype = ["RA---TAN", "DEC--TAN"]
    wcs.wcs.cunit = ["deg", "deg"]
    wcs.wcs.crval = np.array([ra, dec], dtype=np.float64)
    wcs.wcs.crpix = np.array(CRPIX, dtype=np.float64)
    wcs.wcs.cd = CD.copy()
    wcs.array_shape = (HEIGHT, WIDTH)
    wcs.wcs.set()
    return wcs


def _tile_id(wcs: WCS, index: int) -> str:
    for key in ("tile_id", "name", "brick", "brickid"):
        value = getattr(wcs, key, None)
        if value is not None:
            return str(value)
    return f"tile-{index}"


def _jacobian(source_wcs: WCS, output_wcs: WCS, sx: float, sy: float) -> np.ndarray:
    """Finite-difference effective source-pixel to output-pixel Jacobian."""
    points = np.array([[sx, sy], [sx + 1.0, sy], [sx, sy + 1.0]], dtype=np.float64)
    world = source_wcs.all_pix2world(points, 0)
    out = output_wcs.all_world2pix(world, 0)
    if not np.all(np.isfinite(out)):
        raise ValueError(DATA_INTEGRITY_FAIL)
    return np.column_stack((out[1] - out[0], out[2] - out[0]))


def _assert_parity(sources: Sequence[tuple[np.ndarray, WCS]], output_wcs: WCS) -> int:
    signs: list[int] = []
    for image, source_wcs in sources:
        h, w = image.shape
        determinant = float(np.linalg.det(_jacobian(source_wcs, output_wcs, (w - 1) / 2, (h - 1) / 2)))
        if not np.isfinite(determinant) or determinant == 0.0:
            raise ValueError(DATA_INTEGRITY_FAIL)
        signs.append(1 if determinant > 0.0 else -1)
    if not signs or any(sign != 1 for sign in signs):
        raise ValueError(WRONG_PARITY_REFUSAL)
    return 1


def _sample_stitched(
    sources: Sequence[tuple[np.ndarray, WCS]], world: np.ndarray
) -> np.ndarray:
    """Bilinearly sample the union of tiles, permitting corners across seams."""
    n = world.shape[0]
    result = np.empty(n, dtype=np.float64)
    result.fill(np.nan)

    # Source choice depends only on geometric coverage and caller order, never intensity.
    coords = [wcs.all_world2pix(world, 0) for _, wcs in sources]
    for point_index in range(n):
        chosen = None
        for tile_index, ((image, _), xy) in enumerate(zip(sources, coords)):
            x, y = xy[point_index]
            if -0.5 <= x <= image.shape[1] - 0.5 and -0.5 <= y <= image.shape[0] - 0.5:
                chosen = (tile_index, float(x), float(y))
                break
        if chosen is None:
            raise ValueError(DATA_INTEGRITY_FAIL)

        base_index, x, y = chosen
        x0, y0 = int(np.floor(x)), int(np.floor(y))
        dx, dy = np.float64(x - x0), np.float64(y - y0)
        values: list[np.float64] = []
        for yy, xx in ((y0, x0), (y0, x0 + 1), (y0 + 1, x0), (y0 + 1, x0 + 1)):
            value = None
            image = sources[base_index][0]
            if 0 <= yy < image.shape[0] and 0 <= xx < image.shape[1]:
                value = image[yy, xx]
            else:
                sky = sources[base_index][1].all_pix2world([[xx, yy]], 0)
                for other_image, other_wcs in sources:
                    ox, oy = other_wcs.all_world2pix(sky, 0)[0]
                    oix, oiy = int(np.rint(ox)), int(np.rint(oy))
                    if (abs(ox - oix) <= 1e-6 and abs(oy - oiy) <= 1e-6 and
                            0 <= oiy < other_image.shape[0] and 0 <= oix < other_image.shape[1]):
                        value = other_image[oiy, oix]
                        break
            if value is None or not np.isfinite(value):
                raise ValueError(DATA_INTEGRITY_FAIL)
            values.append(np.float64(value))
        v00, v10, v01, v11 = values
        result[point_index] = (
            (1.0 - dx) * (1.0 - dy) * v00
            + dx * (1.0 - dy) * v10
            + (1.0 - dx) * dy * v01
            + dx * dy * v11
        )
    return result


def render_cutout(
    sources: Sequence[tuple[np.ndarray, WCS]], target: tuple[float, float] | RenderTarget
) -> Raster:
    """Render supplied in-memory tiles at ``target`` under frozen geometry."""
    ra, dec, requested = _target_parts(target)
    if not sources:
        raise ValueError(DATA_INTEGRITY_FAIL)
    normalized: list[tuple[np.ndarray, WCS]] = []
    for image, wcs in sources:
        array = np.asarray(image)
        if array.ndim != 2 or not isinstance(wcs, WCS):
            raise ValueError(DATA_INTEGRITY_FAIL)
        normalized.append((array, wcs))

    output_wcs = _output_wcs(ra, dec)
    jacobian_sign = _assert_parity(normalized, output_wcs)
    yy, xx = np.indices((HEIGHT, WIDTH), dtype=np.float64)
    pixels = np.column_stack((xx.ravel(order="C"), yy.ravel(order="C")))
    world = output_wcs.all_pix2world(pixels, 0)
    output = _sample_stitched(normalized, world).reshape((HEIGHT, WIDTH)).astype(np.float64)
    output.setflags(write=False)
    canonical = output.astype("<f8", copy=False).tobytes(order="C")
    digest = hashlib.sha256(canonical).hexdigest()
    metadata = {
            **requested,
            "cd_matrix_deg_per_pixel": tuple(tuple(float(v) for v in row) for row in CD),
            "crval": (ra, dec),
            "projection": "TAN",
            "tile_ids": tuple(_tile_id(wcs, i) for i, (_, wcs) in enumerate(normalized)),
            "source_to_output_jacobian_sign": jacobian_sign,
            "digest": digest,
            "canonical_dtype": "<f8",
            "canonical_order": "C",
            "astropy_version": astropy.__version__,
            "prohibited_transforms": PROHIBITED_TRANSFORMS,
        }
    return Raster(array=output, wcs=output_wcs, digest=digest, metadata=metadata)


__all__ = [
    "Raster", "RenderTarget", "render_cutout", "PINNED_GEOMETRY",
    "PROHIBITED_TRANSFORMS", "WRONG_PARITY_REFUSAL", "WRONG_GEOMETRY_REFUSAL",
]
