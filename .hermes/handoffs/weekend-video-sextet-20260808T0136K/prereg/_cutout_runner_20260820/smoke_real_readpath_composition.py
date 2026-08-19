#!/usr/bin/env python3
"""Read-only real-brick composition smoke; all raster outputs are deleted."""
from __future__ import annotations

import json
import tempfile
from pathlib import Path

import numpy as np

import cutout_runner as runner

HERE = Path(__file__).resolve().parent
READPATH_DIR = HERE.parent / "_production_readpath_20260819"


class SmokeTarget:
    def __init__(self, ra: float, dec: float) -> None:
        self.object_key = "NON-SCIENCE-SMOKE-BRICK-CENTRE"
        self.ra_deg = ra
        self.dec_deg = dec


def main() -> int:
    dependencies = runner.verify_frozen_dependencies()
    verification = json.loads((READPATH_DIR / "real_verification_receipt.json").read_text())
    header = json.loads((READPATH_DIR / "real_header_receipt.json").read_text())
    if verification.get("status") != "PASS":
        raise RuntimeError("gated real-brick verification receipt is not PASS")
    if verification.get("receipt_outcome") != "ACCEPTED" or not verification.get(
        "receipt_digest_verified"
    ):
        raise RuntimeError("real brick is not receipt-accepted and digest-verified")
    source_path = Path(verification["source_path"])
    source_sha = verification["source_file_sha256"]
    wcs_fields = header["wcs_custody"]["wcs_fields"]
    row = {"ra": float(wcs_fields["CRVAL1"]), "dec": float(wcs_fields["CRVAL2"])}
    readpath = runner._readpath()
    adapter = runner._adapter()
    deleted = False
    temp_path: Path | None = None
    source = readpath.ProductionBrickSource(source_path, row, source_sha)
    try:
        values, coverage, contributed = adapter.render_cutout(
            SmokeTarget(row["ra"], row["dec"]), {verification["brickname"]: source}
        )
        raster = np.asarray(values)
        if raster.shape != (128 * 128,) or min(coverage) < 1 or not np.all(np.isfinite(raster)):
            raise RuntimeError("NON-SCIENCE smoke raster failed composition postconditions")
        with tempfile.TemporaryDirectory(prefix="NON_SCIENCE_SMOKE_", dir=HERE) as temporary:
            temp_path = Path(temporary) / "NON_SCIENCE_SMOKE_RASTER_DELETE_ME.f32"
            temp_path.write_bytes(np.asarray(raster, dtype="<f4").tobytes(order="C"))
            if not temp_path.is_file():
                raise RuntimeError("smoke raster was not staged")
        deleted = temp_path is not None and not temp_path.exists()
        receipt = {
            "status": "PASS_NON_SCIENCE_SMOKE",
            "classification": "NON-SCIENCE",
            "science_output_produced": False,
            "purpose": "read-path plus certified-adapter composition smoke only",
            "source_brickname": verification["brickname"],
            "source_file_sha256": source_sha,
            "receipt_outcome": verification["receipt_outcome"],
            "receipt_digest_verified": verification["receipt_digest_verified"],
            "adapter_sha256": runner.ADAPTER_SHA256,
            "readpath_sha256": runner.READPATH_SHA256,
            "dependencies": dependencies,
            "raster_shape_observed": [128, 128],
            "coverage_zero_count": sum(value == 0 for value in coverage),
            "contributed_pixel_counts": contributed,
            "temporary_smoke_output_deleted_same_run": deleted,
            "temporary_smoke_output_exists_after_run": False if temp_path is None else temp_path.exists(),
            "ic4_ic5_not_executed": True,
            "real_sky_runner_status": "REFUSED_WHILE_IC_SLOTS_NULL",
        }
        if not deleted:
            raise RuntimeError("temporary NON-SCIENCE smoke output was not deleted")
        (HERE / "NON_SCIENCE_SMOKE_RECEIPT.json").write_text(
            json.dumps(receipt, indent=2, sort_keys=True) + "\n", encoding="utf-8"
        )
        print(json.dumps(receipt, sort_keys=True))
        return 0
    finally:
        source.close()
        if temp_path is not None and temp_path.exists():
            temp_path.unlink()


if __name__ == "__main__":
    raise SystemExit(main())
