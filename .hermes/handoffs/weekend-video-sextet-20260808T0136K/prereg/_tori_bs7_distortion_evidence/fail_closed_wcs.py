#!/usr/bin/env python3
"""Fail-closed WCS distortion audit for the bound DR10.1 South route."""
from __future__ import annotations

import argparse
import hashlib
import json
import math
import re
from datetime import datetime, timezone
from pathlib import Path
from typing import Mapping

EXPECTED_ROUTE_RECEIPT_SHA256 = "a573d8993b40cfbde143f9bd653cf7579dc1e73467a04fb9ed36b716efbc77e6"
EXPECTED_PRODUCT_SHA256 = "ac212f9d9003688a266273452b22385d8e13a9d613bbc4a873291ff544e1c24c"


def utc_now() -> str:
    return datetime.now(timezone.utc).isoformat(timespec="seconds").replace("+00:00", "Z")


def numeric(value: object) -> float:
    if not isinstance(value, (int, float, str)):
        raise TypeError(f"WCS numeric value has unsupported type: {type(value).__name__}")
    return float(value)


def distortion_families(header: Mapping[str, object]) -> tuple[list[str], list[str]]:
    families: set[str] = set()
    keys: list[str] = []
    for raw_key in header:
        key = str(raw_key).upper()
        family = None
        if re.match(r"^(A|B|AP|BP)_(ORDER|\d+_\d+)$", key):
            family = "SIP"
        elif re.match(r"^PV[12]_\d+$", key):
            family = "PV"
        elif key.startswith("CPDIS"):
            family = "CPDIS"
        elif key.startswith("D2IM") or key.startswith("DET2IM"):
            family = "DET2IM"
        if family is not None:
            families.add(family)
            keys.append(key)
    return sorted(families), sorted(keys)


def audit_header(header: Mapping[str, object]) -> dict:
    normalized = {str(key).upper(): value for key, value in header.items()}
    families, keys = distortion_families(normalized)
    base = {
        "branch": "FAIL_CLOSED",
        "distortion_families": families,
        "distortion_keywords": keys,
        "local_jacobian_used": False,
    }
    if families:
        return {**base, "status": "FAIL_DISTORTION", "linear_determinant": None, "linear_parity": None}
    ctype1 = str(normalized.get("CTYPE1", ""))
    ctype2 = str(normalized.get("CTYPE2", ""))
    if not ctype1.startswith("RA-") or not ctype2.startswith("DEC-"):
        return {**base, "status": "FAIL_NON_CELESTIAL", "linear_determinant": None, "linear_parity": None}

    cd_keys = ("CD1_1", "CD1_2", "CD2_1", "CD2_2")
    present_cd = [key in normalized for key in cd_keys]
    if any(present_cd):
        if not all(present_cd):
            return {**base, "status": "FAIL_INCOMPLETE_LINEAR_WCS", "linear_determinant": None, "linear_parity": None}
        a, b, c, d = (numeric(normalized[key]) for key in cd_keys)
        representation = "CD"
    else:
        pc_keys = ("PC1_1", "PC1_2", "PC2_1", "PC2_2", "CDELT1", "CDELT2")
        if not all(key in normalized for key in pc_keys):
            return {**base, "status": "FAIL_INCOMPLETE_LINEAR_WCS", "linear_determinant": None, "linear_parity": None}
        cdelt1 = numeric(normalized["CDELT1"])
        cdelt2 = numeric(normalized["CDELT2"])
        a = numeric(normalized["PC1_1"]) * cdelt1
        b = numeric(normalized["PC1_2"]) * cdelt1
        c = numeric(normalized["PC2_1"]) * cdelt2
        d = numeric(normalized["PC2_2"]) * cdelt2
        representation = "PCxCDELT"
    determinant = a * d - b * c
    if not math.isfinite(determinant) or determinant == 0.0:
        return {
            **base,
            "status": "FAIL_SINGULAR",
            "linear_determinant": determinant if math.isfinite(determinant) else None,
            "linear_parity": None,
            "linear_representation": representation,
        }
    return {
        **base,
        "status": "PASS",
        "linear_determinant": determinant,
        "linear_parity": "PRESERVING" if determinant > 0 else "REVERSING",
        "linear_representation": representation,
    }


def build_receipt(route_record: dict, route_receipt_sha256: str) -> dict:
    if route_receipt_sha256 != EXPECTED_ROUTE_RECEIPT_SHA256:
        raise RuntimeError("bound route receipt hash mismatch")
    if route_record.get("sha256") != EXPECTED_PRODUCT_SHA256:
        raise RuntimeError("bound metadata-check product hash mismatch")
    if route_record.get("chirality_computed") is not False or route_record.get("sky_statistics_computed") is not False:
        raise RuntimeError("bound route receipt violates no-signal boundary")
    ctype = route_record.get("ctype")
    cd = route_record.get("cd")
    if not isinstance(ctype, list) or len(ctype) != 2 or not isinstance(cd, list) or len(cd) != 2:
        raise RuntimeError("bound route receipt lacks complete CTYPE/CD metadata")
    header = {
        "CTYPE1": ctype[0],
        "CTYPE2": ctype[1],
        "CD1_1": cd[0][0],
        "CD1_2": cd[0][1],
        "CD2_1": cd[1][0],
        "CD2_2": cd[1][1],
    }
    for key in route_record.get("distortion_keywords", []):
        header[str(key)] = "PRESENT"
    audit = audit_header(header)
    return {
        "recorded_utc": utc_now(),
        "status": audit["status"],
        "declared_branch": "FAIL_CLOSED",
        "local_jacobian_branch_selected": False,
        "frozen_policy": "Reject SIP/PV/CPDIS/DET2IM, non-celestial, partial, singular, or indeterminate WCS before any object-level statistic; never fall back silently to a linear determinant.",
        "bound_route": "DESI Legacy DR10.1 South ls-dr10-south generated FITS cutout",
        "bound_route_receipt_sha256": route_receipt_sha256,
        "bound_metadata_product_sha256": route_record["sha256"],
        "bound_metadata_audit": audit,
        "future_products_require_per_product_audit": True,
        "route_example_not_extrapolated_to_future_headers": True,
        "new_network_requests": 0,
        "images_opened": 0,
        "object_rows": 0,
        "positions": 0,
        "chirality_or_morphology_labels": 0,
        "sky_statistics": 0,
        "primary_wcs_source": "https://www.legacysurvey.org/dr10/description/#image-stacks-south-coadd",
        "primary_wcs_source_statement": "image stacks use a simple tangent-plane (WCS TAN) projection; g,r,i,z projections are identical at 0.262 arcsec/pixel",
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("route_receipt", type=Path)
    parser.add_argument("output", type=Path)
    args = parser.parse_args()
    route_bytes = args.route_receipt.read_bytes()
    route_hash = hashlib.sha256(route_bytes).hexdigest()
    receipt = build_receipt(json.loads(route_bytes), route_hash)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(receipt, indent=2, sort_keys=True) + "\n")
    print(json.dumps(receipt, sort_keys=True))


if __name__ == "__main__":
    main()
