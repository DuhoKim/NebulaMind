#!/usr/bin/env python3
from __future__ import annotations

import importlib.util
from pathlib import Path

ROOT = Path(__file__).resolve().parent
TARGET = ROOT / "fail_closed_wcs.py"
spec = importlib.util.spec_from_file_location("fail_closed_wcs", TARGET)
if spec is None or spec.loader is None:
    raise RuntimeError("cannot load fail-closed WCS module")
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)

base = {
    "CTYPE1": "RA---TAN",
    "CTYPE2": "DEC--TAN",
    "CD1_1": -7.27777777777778e-05,
    "CD1_2": 0.0,
    "CD2_1": 0.0,
    "CD2_2": 7.27777777777778e-05,
}
passed = module.audit_header(base)
assert passed["status"] == "PASS"
assert passed["branch"] == "FAIL_CLOSED"
assert passed["linear_parity"] == "REVERSING"
assert passed["distortion_keywords"] == []

for key, value, family in [
    ("A_ORDER", 2, "SIP"),
    ("PV1_0", 1.0, "PV"),
    ("CPDIS1", "LOOKUP", "CPDIS"),
    ("D2IMDIS1", "LOOKUP", "DET2IM"),
    ("DET2IM1", "LOOKUP", "DET2IM"),
]:
    result = module.audit_header({**base, key: value})
    assert result["status"] == "FAIL_DISTORTION"
    assert result["distortion_families"] == [family]

assert module.audit_header({**base, "CD1_1": 0.0})["status"] == "FAIL_SINGULAR"
assert module.audit_header({k: v for k, v in base.items() if k != "CD2_2"})["status"] == "FAIL_INCOMPLETE_LINEAR_WCS"
assert module.audit_header({**base, "CTYPE1": "LINEAR"})["status"] == "FAIL_NON_CELESTIAL"

pc = {
    "CTYPE1": "RA---TAN",
    "CTYPE2": "DEC--TAN",
    "PC1_1": 1.0,
    "PC1_2": 0.0,
    "PC2_1": 0.0,
    "PC2_2": 1.0,
    "CDELT1": -7.27777777777778e-05,
    "CDELT2": 7.27777777777778e-05,
}
assert module.audit_header(pc)["status"] == "PASS"

route_record = {
    "bytes": 5760,
    "cd": [[-7.27777777777778e-05, 0.0], [0.0, 7.27777777777778e-05]],
    "chirality_computed": False,
    "ctype": ["RA---TAN", "DEC--TAN"],
    "distortion_keywords": [],
    "network_requests_to_data_products": 1,
    "purpose": "prior metadata-only verification",
    "request_url": "https://www.legacysurvey.org/viewer/fits-cutout?layer=ls-dr10-south",
    "sha256": "ac212f9d9003688a266273452b22385d8e13a9d613bbc4a873291ff544e1c24c",
    "shape": [16, 16],
    "sky_statistics_computed": False,
}
receipt = module.build_receipt(route_record, "a573d8993b40cfbde143f9bd653cf7579dc1e73467a04fb9ed36b716efbc77e6")
assert receipt["status"] == "PASS"
assert receipt["declared_branch"] == "FAIL_CLOSED"
assert receipt["new_network_requests"] == 0
assert receipt["images_opened"] == 0
assert receipt["future_products_require_per_product_audit"] is True
assert receipt["local_jacobian_branch_selected"] is False
print("bs7_fail_closed_contract=PASS synthetic_cases=10 new_images=0 new_requests=0")
