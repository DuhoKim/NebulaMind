"""V15 section 6: fixed, label-blind MEDIUM perturbation disclosure.

Public API: produce_tuning_disclosure(objects, /) -> JSON-compatible dict.
objects is an exact tuple of exact dicts with ONLY the keys in _FIELDS.
Inputs are already-authorized TUNING source planes and numeric WCS geometry.
There is no loader, pathname, inventory, callback, label, winner, configuration,
preprocessing selector, output destination, or live-run CLI in this API.

Both arms use render_chain_v3, pixel_rejection_v2 and the existing Fourier
Estimator.chi. All 96 existing configurations are disclosed in their existing
order, never selected or ranked here. See MEDIUM_DISCLOSURE_METHOD_20260907.md.
"""
from __future__ import annotations

import os

# As in run_path.py, establish the fixed thread settings before NumPy import.
for _name in ("OMP_NUM_THREADS", "OPENBLAS_NUM_THREADS", "MKL_NUM_THREADS",
              "VECLIB_MAXIMUM_THREADS", "NUMEXPR_NUM_THREADS"):
    os.environ[_name] = "1"

import numpy as np
from astropy.wcs import WCS
from study_renderer import render_chain_v3 as _chain
from study_renderer import pixel_rejection_v2 as _pixels
from _optionA_dev.fourier_chirality import fourier_chirality as _family

__all__ = ["produce_tuning_disclosure", "DisclosureRefused"]

_FIELDS = frozenset(("objid", "stage", "image", "maskbits", "nexp",
                     "wcs", "ra", "dec", "brick"))
# Only numeric celestial TAN geometry, not a FITS header or an extensible WCS
# object (either could carry catalogue metadata, extra attributes or callbacks).
_WCS_FIELDS = frozenset(("crpix", "crval", "cd"))
_METHOD = "V15-6-MEDIUM-SOURCE-LOWER-MEDIAN-1"


class DisclosureRefused(ValueError):
    """The closed label-free input contract was not met."""


def _require(ok, reason):
    if not ok:
        raise DisclosureRefused(reason)


def _numeric_tuple(value, length):
    return (type(value) is tuple and len(value) == length and
            all(type(x) in (float, int) and np.isfinite(x) for x in value))


def _validate(objects):
    # Reject extensible/lazy containers BEFORE iteration or value access.
    _require(type(objects) is tuple, "EXACT-TUPLE-REQUIRED")
    seen = set()
    for obj in objects:
        _require(type(obj) is dict, "EXACT-OBJECT-DICT-REQUIRED")
        _require(all(type(k) is str for k in obj) and set(obj) == _FIELDS,
                 "EXACT-LABEL-FREE-FIELDS-REQUIRED")
        _require(type(obj["stage"]) is str and obj["stage"] == "tuning",
                 "TUNING-ONLY")
        oid = obj["objid"]
        _require(type(oid) is int and oid >= 0 and oid not in seen,
                 "UNIQUE-INTEGER-OBJID-REQUIRED")
        seen.add(oid)
        _require(type(obj["brick"]) is str and bool(obj["brick"]) and
                 all(c in "0123456789pm" for c in obj["brick"]),
                 "BRICK-ID-REQUIRED")
        _require(_numeric_tuple((obj["ra"], obj["dec"]), 2) and
                 0 <= obj["ra"] < 360 and -90 <= obj["dec"] <= 90,
                 "TARGET-COORDINATES")
        for key in ("image", "maskbits", "nexp"):
            a = obj[key]
            # No memmap, ndarray subclass, object/structured dtype or __array__
            # hook can bring an external reader or label-bearing object inside.
            _require(type(a) is np.ndarray and a.ndim == 2 and a.size > 0 and
                     a.dtype.kind in ("fiu" if key == "image" else "iu"),
                     "PLAIN-NUMERIC-PLANES-REQUIRED")
        try:
            _pixels.validate_planes(obj["image"], obj["maskbits"], obj["nexp"])
        except ValueError as exc:
            raise DisclosureRefused(str(exc)) from exc
        # renderer_v4 returns int32 integer planes: prevent high-bit truncation.
        _require(all(a.size == 0 or int(a.max()) <= np.iinfo(np.int32).max
                     for a in (obj["maskbits"], obj["nexp"])), "INTEGER-PLANE-RANGE")
        geo = obj["wcs"]
        _require(type(geo) is dict and all(type(k) is str for k in geo) and
                 set(geo) == _WCS_FIELDS, "NUMERIC-TAN-WCS-ONLY")
        _require(_numeric_tuple(geo["crpix"], 2) and
                 _numeric_tuple(geo["crval"], 2) and
                 type(geo["cd"]) is tuple and len(geo["cd"]) == 2 and
                 all(_numeric_tuple(row, 2) for row in geo["cd"]),
                 "NUMERIC-TAN-WCS-ONLY")
        _require(0 <= geo["crval"][0] < 360 and -90 <= geo["crval"][1] <= 90,
                 "SOURCE-COORDINATES")


def _source_wcs(obj):
    # Astropy constructs the transform; renderer_v4 owns all reprojection.
    # Callers must extract only a lossless, distortion-free RA/DEC TAN WCS.
    geo = obj["wcs"]
    wcs = WCS(naxis=2)
    wcs.wcs.ctype = ["RA---TAN", "DEC--TAN"]
    wcs.wcs.cunit = ["deg", "deg"]
    wcs.wcs.crpix = geo["crpix"]
    wcs.wcs.crval = geo["crval"]
    wcs.wcs.cd = np.array(geo["cd"], dtype=np.float64)
    wcs.array_shape = obj["image"].shape
    wcs.wcs.set()
    return wcs


def _render(obj, image, wcs):
    return _chain.render_object(
        image, obj["maskbits"], obj["nexp"], wcs,
        obj["ra"], obj["dec"], obj["brick"], _chain.pr.r_t_validation())


def _score(estimator, render):
    rec = {"status": "UNSCORED", "chi": None, "chi_bits": None,
           "repeat_bits": None, "sign": None}
    if render["status"] != "SCORED":
        return {**rec, "reason": render["reason"]}
    arr = np.frombuffer(render["tensor"], dtype="<f4").reshape(128, 128)
    try:
        chi = estimator.chi(arr)
        repeat = estimator.chi(arr.copy())
    except Exception as exc:
        return {**rec, "reason": "SCORE-ERROR:" + type(exc).__name__}
    bits = int(chi.view(np.uint32))
    repeat_bits = int(repeat.view(np.uint32))
    rec.update(chi=float(chi) if np.isfinite(chi) else None,
               chi_bits=bits, repeat_bits=repeat_bits)
    if bits != repeat_bits:
        return {**rec, "reason": "NON-REPEAT"}
    if chi == 0 or not np.isfinite(chi):
        return {**rec, "reason": "TIE-OR-NONFINITE"}
    return {**rec, "status": "SCORED", "sign": 1 if chi > 0 else -1}


def produce_tuning_disclosure(objects, /):
    """Compute both fixed arms and every configuration's flips/eligible objects.

    No input can choose preprocessing, a subset of configurations or a scorer.
    This computational function does not establish adoption, temporal authority
    or actual draw membership: its label-free inputs must arrive at tuning time.
    """
    _validate(objects)  # Validate the ENTIRE batch before the first render.
    configurations = _family.enumerate_configs()
    _require(len(configurations) == 96, "EXISTING-GRID-MUST-HAVE-96-CONFIGURATIONS")
    estimators = [_family.Estimator(cfg) for cfg in configurations]
    summaries = [
        {"config_index": i, "config_id": est.config_id, "config": dict(est.cfg),
         "eligible_objects": 0, "flips": 0, "unscored_pairs": 0}
        for i, est in enumerate(estimators)
    ]
    rows = []
    for obj in objects:
        medium = _pixels.medium_mask(obj["maskbits"])
        row = {"objid": obj["objid"], "n_medium_source": int(medium.sum()),
               "medium_count": 0, "status": "NO-MEDIUM", "pairs": []}
        if not medium.any():
            rows.append(row)
            continue
        wcs = _source_wcs(obj)
        kept = _render(obj, obj["image"], wcs)
        row["kept_render"] = {k: v for k, v in kept.items() if k != "tensor"}
        row["medium_count"] = kept.get("medium_count")
        if row["medium_count"] is None:
            row["status"] = "ELIGIBILITY-UNRESOLVED"
            rows.append(row)
            continue
        if row["medium_count"] == 0:
            rows.append(row)
            continue
        row["status"] = "MEDIUM"
        # Replacement arm accepts neither ordinarily rejected nor MEDIUM source
        # pixels when forming the global lower median. No output-grid edit.
        try:
            reject = _pixels.rejection_mask(obj["maskbits"], obj["nexp"])
            fill = _pixels.replacement_value(obj["image"], reject | medium)
            perturbed = np.array(obj["image"], dtype=np.float64, copy=True)
            perturbed[medium] = fill
            replaced = _render(obj, perturbed, wcs)
            row["perturbation_lower_median"] = fill
        except ValueError as exc:
            replaced = {"status": "REFUSED", "reason": str(exc)}
            row["perturbation_lower_median"] = None
        row["replaced_render"] = {k: v for k, v in replaced.items() if k != "tensor"}
        # Original integer planes go to BOTH renders. Bit 11 never becomes a
        # rejection flag; protected-region/ceiling rules remain exactly fixed.
        for i, est in enumerate(estimators):
            kept_score, replaced_score = _score(est, kept), _score(est, replaced)
            eligible = kept_score["status"] == replaced_score["status"] == "SCORED"
            flipped = (kept_score["sign"] != replaced_score["sign"]) if eligible else None
            row["pairs"].append({
                "config_index": i, "config_id": est.config_id,
                "kept": kept_score, "replaced": replaced_score,
                "sign_flipped": flipped, "eligible": eligible})
            summaries[i]["eligible_objects"] += int(eligible)
            summaries[i]["flips"] += int(flipped is True)
            summaries[i]["unscored_pairs"] += int(not eligible)
        rows.append(row)
    unresolved = sum(row["status"] == "ELIGIBILITY-UNRESOLVED" for row in rows)
    medium_objects = sum(row["status"] == "MEDIUM" for row in rows)
    for summary in summaries:
        n = summary["eligible_objects"]
        summary["sign_flip_rate"] = summary["flips"] / n if n else None
        summary["rate_status"] = ("NO-ELIGIBLE-OBJECTS" if not n else
                                  "INCOMPLETE" if unresolved or summary["unscored_pairs"]
                                  else "COMPLETE")
    return {
        "schema": "A1-MEDIUM-PERTURBATION-1", "method": _METHOD, "stage": "tuning",
        "authorizes_execution": False,
        "configuration_policy": "ALL-96-IN-EXISTING-ORDER-NO-SELECTION",
        "rate_definition": "flips / eligible_objects, separately for every configuration",
        "n_objects": len(rows), "medium_objects": medium_objects,
        "no_medium_objects": sum(row["status"] == "NO-MEDIUM" for row in rows),
        "eligibility_unresolved_objects": unresolved,
        "objects": rows, "configurations": summaries,
    }
