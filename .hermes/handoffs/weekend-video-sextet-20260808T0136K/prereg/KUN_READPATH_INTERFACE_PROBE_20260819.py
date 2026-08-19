#!/usr/bin/env python3
"""Kun gate: structural interface conformance of ProductionBrickSource vs the
gated adapter's SyntheticBrickSource contract. Findings-only; no writes."""
import inspect
import sys
from pathlib import Path

HERE = Path("/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/weekend-video-sextet-20260808T0136K/prereg")
sys.path.insert(0, str(HERE / "_production_readpath_20260819"))

import production_readpath as rp

adapter = rp._load_adapter()  # hash-pinned load; raises if adapter drifted
Syn = adapter.SyntheticBrickSource
Prod = rp.ProductionBrickSource

results = {}

# 1. Constructor: first three positional parameters must be (path, row, expected_sha256)
syn_params = list(inspect.signature(Syn.__init__).parameters)
prod_params = list(inspect.signature(Prod.__init__).parameters)
results["syn_ctor_first3"] = syn_params[1:4]
results["prod_ctor_first3"] = prod_params[1:4]
results["ctor_first3_match"] = syn_params[1:4] == prod_params[1:4] == ["path", "row", "expected_sha256"]

# 2. Required runtime fields/methods exist on the production source class
#    (checked against a real constructed instance below; here class-level callables)
results["has_pixel_callable"] = callable(getattr(Prod, "pixel", None))
results["has_close_callable"] = callable(getattr(Prod, "close", None))
prod_pixel_params = list(inspect.signature(Prod.pixel).parameters)
syn_pixel_params = list(inspect.signature(Syn.pixel).parameters)
results["pixel_params_match"] = syn_pixel_params[1:] == prod_pixel_params[1:] == ["ix", "iy"]

# 3. TanWcs identity: production reader must build the adapter's own TanWcs
results["tanwcs_same_object"] = rp._load_adapter().TanWcs is adapter.TanWcs

# 4. Live instance field check on the real accepted brick (read-only)
import json, hashlib
DATA_ROOT = Path("/Users/duhokim/NebulaMindData/dr10_south_image_r")
path = record = None
with (DATA_ROOT / "receipts.jsonl").open() as h:
    for line in h:
        cand = json.loads(line)
        if cand.get("outcome") != "ACCEPTED" or cand.get("digest_verified") is not True:
            continue
        rel = Path(cand["destination_relative_path"])
        for loc in (DATA_ROOT / rel, DATA_ROOT / "staging" / rel):
            if loc.is_file():
                digest = hashlib.sha256(loc.read_bytes()).hexdigest()
                if digest == cand["local_sha256"]:
                    path, record = loc, cand
                    break
        if path is not None:
            break
assert path is not None, "no accepted brick"
from astropy.io import fits
with fits.open(path, mode="readonly", memmap=False) as hdul:
    row = {"ra": float(hdul[1].header["CRVAL1"]), "dec": float(hdul[1].header["CRVAL2"])}
    direct = hdul[1].data  # keep for pixel spot-checks

src = Prod(path, row, record["local_sha256"])
fields = ["path", "sha256", "header_sha256", "cards", "data_offset", "wcs", "gate_receipt"]
results["instance_fields_present"] = {f: hasattr(src, f) for f in fields}
results["wcs_is_adapter_tanwcs"] = isinstance(src.wcs, adapter.TanWcs)
results["wcs_has_sky_to_pixel"] = callable(getattr(src.wcs, "sky_to_pixel", None))
results["wcs_has_pixel_to_sky"] = callable(getattr(src.wcs, "pixel_to_sky", None))

# 5. pixel() 1-based FITS semantics vs direct astropy reads (corners + centre + off-diagonal)
checks = []
for ix, iy in [(1, 1), (3600, 3600), (1, 3600), (3600, 1), (1800, 1800), (123, 456), (3599, 7)]:
    got = src.pixel(ix, iy)
    want = float(direct[iy - 1, ix - 1])
    checks.append({"ix": ix, "iy": iy, "match": got == want})
results["pixel_values_match_direct_astropy"] = checks
results["all_pixel_checks_pass"] = all(c["match"] for c in checks)

# 6. 1-based bounds enforcement (out-of-range must raise, matching adapter semantics)
for bad in [(0, 1), (1, 0), (3601, 1), (1, 3601)]:
    try:
        src.pixel(*bad)
        results.setdefault("bounds_errors", []).append((bad, "NO ERROR"))
    except IndexError:
        results.setdefault("bounds_errors", []).append((bad, "IndexError"))
results["bounds_all_raised"] = all(r[1] == "IndexError" for r in results["bounds_errors"])

# 7. close() and context-manager protocol
src.close()
results["close_ran"] = True
results["context_manager"] = hasattr(Prod, "__enter__") and hasattr(Prod, "__exit__")

ok = (results["ctor_first3_match"] and results["has_pixel_callable"] and results["has_close_callable"]
      and results["pixel_params_match"] and results["tanwcs_same_object"]
      and all(results["instance_fields_present"].values()) and results["wcs_is_adapter_tanwcs"]
      and results["wcs_has_sky_to_pixel"] and results["wcs_has_pixel_to_sky"]
      and results["all_pixel_checks_pass"] and results["bounds_all_raised"]
      and results["close_ran"] and results["context_manager"])
results["VERDICT"] = "INTERFACE_MATCH" if ok else "INTERFACE_MISMATCH"
for k, v in results.items():
    print(f"{k}: {v}")
sys.exit(0 if ok else 1)
