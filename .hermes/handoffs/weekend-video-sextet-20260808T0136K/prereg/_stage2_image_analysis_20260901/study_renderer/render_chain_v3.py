"""THE EXECUTED RENDER CHAIN under the V38 pipeline identity (Tier-C V38 draft §8.15b consumer; option A V15 §6). v3 = v2 with
protected_region_v2 (binary64 r_T, no truncation) and, in the receipt, the flagged OUTPUT coordinates and the §9B.2d band indicator
(any flag with r_T < d ≤ 64), so N_asym / p_val_excl are computed from this single pass without re-rendering (codex V37 [MAJOR]). One function, in the
binding order: validate planes → source-grid rejection and replacement including zero exposure (pixel_rejection_v2.clean_source) →
single reprojection with integer-plane carriage (renderer_v4.render_cutout) → output flags (pixel_rejection_v2.flagged_output) →
refusal test (protected_region.refuse_on_contamination: F ≤ 819, nothing flagged inside T) → amplitude normalisation (§8.15) →
128×128 float32 tensor (65,536 bytes). MEDIUM is carried and counted per raster, never used for rejection or flagging.
Returns a dict; never raises for an object-level refusal (status REFUSED + reason); raises only on caller misuse.
Written 2026-09-06 after codex's V36 FATAL 1 (the helper implemented §6 but no pinned consumer executed it end to end)."""
from __future__ import annotations
import hashlib
import numpy as np
from pathlib import Path
import sys; sys.path.insert(0, str(Path(__file__).resolve().parent.parent)); sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "miniprereg_pins"))
from study_renderer import pixel_rejection_v2 as prj
from study_renderer import renderer_v4 as rv4
import protected_region_v2 as pr

APERTURE = (slice(48, 80), slice(48, 80))      # §8.15 central 32×32
TENSOR_BYTES = 65536


def render_object(image, maskbits, nexp, wcs, ra: float, dec: float, brick_id: str, r_t: float) -> dict:
    rec = {"brick": brick_id, "r_T": float(r_t)}
    try:
        prj.validate_planes(image, maskbits, nexp)                                           # §8.12 (V37): shape + finiteness + integer planes
        cleaned, fill, n_rej, n_zero, n_med_src = prj.clean_source(image, maskbits, nexp)    # §8.9a–c incl. zero exposure
        raster = rv4.render_cutout([(cleaned, maskbits, nexp, wcs)], rv4.RenderTarget(ra=ra, dec=dec, primary_tile_id=brick_id))   # §8.9, §8.9d carriage
        C = np.asarray(raster.array, dtype=np.float64)
        if not np.isfinite(C).all():
            raise ValueError("DATA-INTEGRITY-FAIL:non-finite output")
        flagged = prj.flagged_output(np.asarray(raster.maskbits), np.asarray(raster.nexp))  # §8.9d (V37): rejecting bit OR zero exposure
        coords = [(int(i), int(j)) for i, j in zip(*np.nonzero(flagged))]
        F = len(coords); medium = prj.medium_count(np.asarray(raster.maskbits))
        rec.update({"F": F, "medium_count": medium, "replacement_value": fill, "n_rejected_source": n_rej, "n_zero_exposure_source": n_zero,
                    "n_medium_source": n_med_src, "raster_digest": raster.digest})
        rec["flagged_coords"] = coords                                                            # v3: retained for §9B.2d without re-rendering
        rec["asym_band_flag"] = any(float(r_t) < ((i - pr.CENTRE) ** 2 + (j - pr.CENTRE) ** 2) ** 0.5 <= 64.0 for i, j in coords)   # §9B.2d N_asym membership
        refusal = pr.refuse_on_contamination(coords, float(r_t))                              # §8.14a: F > 819 or any flag inside T (binary64 radius)
        if refusal:
            raise ValueError("REFUSED:" + refusal)
        peak = float(np.max(C[APERTURE]))                                                   # §8.15, binary64
        rec["peak"] = peak
        if not np.isfinite(peak) or peak <= 0:
            raise ValueError("REFUSED:DATA-INTEGRITY-FAIL:degenerate peak")                   # §8.15c
        A = np.ascontiguousarray((C / peak).astype("<f4")).reshape(1, 128, 128)
        payload = A.tobytes(order="C")
        if len(payload) != TENSOR_BYTES:
            raise ValueError("DATA-INTEGRITY-FAIL:tensor size")
        rec.update({"status": "SCORED", "tensor": payload, "tensor_sha256": hashlib.sha256(payload).hexdigest()})
    except ValueError as e:
        msg = str(e); rec.update({"status": "REFUSED", "reason": msg[len("REFUSED:"):] if msg.startswith("REFUSED:") else msg})
    return rec
