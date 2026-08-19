#!/usr/bin/env python3
"""Offline verification against one receipt-accepted local DR10 South brick."""
from __future__ import annotations

import hashlib
import json
from pathlib import Path

from production_readpath import ProductionBrickSource, multiprocess_determinism_check

DATA_ROOT = Path("/Users/duhokim/NebulaMindData/dr10_south_image_r")
HERE = Path(__file__).resolve().parent


def file_sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1 << 20), b""):
            digest.update(chunk)
    return digest.hexdigest()


def main() -> int:
    # Read the header first without assuming geometry. Production callers pass
    # the real sidecar row; this verifier then reopens using the exact values.
    path = None
    record = None
    with (DATA_ROOT / "receipts.jsonl").open(encoding="utf-8") as handle:
        for line in handle:
            candidate = json.loads(line)
            if candidate.get("outcome") != "ACCEPTED" or candidate.get("digest_verified") is not True:
                continue
            relative = Path(candidate["destination_relative_path"])
            for location in (DATA_ROOT / relative, DATA_ROOT / "staging" / relative):
                if location.is_file() and file_sha256(location) == candidate["local_sha256"]:
                    path, record = location, candidate
                    break
            if path is not None:
                break
    if path is None or record is None:
        raise RuntimeError("no receipt-accepted local DR10 South brick found")

    # Astropy-only header discovery for the verifier; the reader itself then
    # performs the hash-pinned PC-4 gate before exposing any array.
    from astropy.io import fits
    with fits.open(path, mode="readonly", memmap=False) as hdul:
        row = {"ra": float(hdul[1].header["CRVAL1"]), "dec": float(hdul[1].header["CRVAL2"])}

    first = ProductionBrickSource(path, row, record["local_sha256"])
    second = ProductionBrickSource(path, row, record["local_sha256"])
    try:
        sequential_identical = first.array.tobytes() == second.array.tobytes()
        header_identical = first.header_receipt == second.header_receipt
        first.write_header_receipt(HERE / "real_header_receipt.json")
        array_sha256 = first.header_receipt["array_sha256"]
    finally:
        first.close()
        second.close()

    mp_a = multiprocess_determinism_check(
        path, row, record["local_sha256"], process_count=4,
        completion_delays=(0.6, 0.0, 0.4, 0.2),
    )
    mp_b = multiprocess_determinism_check(
        path, row, record["local_sha256"], process_count=4,
        completion_delays=(0.0, 0.6, 0.2, 0.4),
    )
    result = {
        "status": "PASS" if (
            sequential_identical and header_identical
            and mp_a["content_sha256"] == mp_b["content_sha256"]
            and mp_a["observed_completion_order"] != mp_b["observed_completion_order"]
            and mp_a["array_sha256"] == array_sha256
        ) else "FAIL",
        "brickname": record["brickname"],
        "source_path": str(path),
        "source_location_note": (
            "accepted file remains in transfer-owned staging/coadd"
            if "/staging/coadd/" in str(path)
            else "accepted file is in requested coadd root"
        ),
        "source_file_sha256": record["local_sha256"],
        "receipt_outcome": record["outcome"],
        "receipt_digest_verified": record["digest_verified"],
        "sequential_reads_byte_identical": sequential_identical,
        "sequential_header_receipts_identical": header_identical,
        "array_sha256": array_sha256,
        "multiprocessing_process_count": 4,
        "multiprocessing_forced_completion_orders": 2,
        "multiprocessing_content_sha256": mp_a["content_sha256"],
        "multiprocessing_schedule_stable": mp_a["content_sha256"] == mp_b["content_sha256"],
        "observed_completion_orders_differ": (
            mp_a["observed_completion_order"] != mp_b["observed_completion_order"]
        ),
        "multiprocessing_receipt": mp_a,
    }
    (HERE / "real_verification_receipt.json").write_text(
        json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8"
    )
    print(json.dumps({key: value for key, value in result.items() if key != "multiprocessing_receipt"}, indent=2, sort_keys=True))
    return 0 if result["status"] == "PASS" else 1


if __name__ == "__main__":
    raise SystemExit(main())
