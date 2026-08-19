#!/usr/bin/env python3
"""Fail-closed IC-1..IC-7 composition over the gated brick reader and cutter.

This module has no acquisition or selection-query capability. Positions and
receipt-accepted brick references are explicit inputs. The production reader
and resampler-gate-certified adapter are imported only after exact hash checks.
"""
from __future__ import annotations

import argparse
import csv
import hashlib
import importlib.util
import json
import math
import os
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Mapping, Sequence

import numpy as np

HERE = Path(__file__).resolve().parent
PREREG_ROOT = HERE.parent
PREREG_PATH = PREREG_ROOT / "PREREG_LONGO_AMPLITUDE_TEST_FROZEN_20260815_V3.md"
AMENDMENT_PATH = PREREG_ROOT / "LANA_PC1_INPUT_AMENDMENT_20260815.md"
ADAPTER_PATH = PREREG_ROOT / "adapter" / "nm_brick_cutout_adapter.py"
READPATH_PATH = PREREG_ROOT / "_production_readpath_20260819" / "production_readpath.py"

PREREG_SHA256 = "b06901c8a0f3a0570af41262453670589d8dc0b20c79c7d4162853c7dfec42d7"
AMENDMENT_SHA256 = "519ab5ba33c5e9d670b5654fb41f6941293c5d969c5515fb0284ebe8d52d70fb"
ADAPTER_SHA256 = "267b2a93d2a61f65b281aeb3b04dd874d7add058797b10f593cb3efb4066006f"
READPATH_SHA256 = "105bd0c6858f27166fecee5ff7ece42c0e993eab8e3bc15b517f9bc9b5418d56"
EXPECTED_SHAPE = (128, 128)
TENSOR_SHAPE = (1, 128, 128)


class ContractError(RuntimeError):
    def __init__(self, message: str, *, code: str, detail: dict | None = None) -> None:
        super().__init__(message)
        self.code = code
        self.detail = dict(detail or {})


@dataclass(frozen=True)
class Position:
    ra: float
    dec: float
    ls_id: str


@dataclass(frozen=True)
class BrickSpec:
    path: Path
    row: Mapping[str, float]
    sha256: str
    brickname: str


def _sha256_bytes(payload: bytes) -> str:
    return hashlib.sha256(payload).hexdigest()


def _sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with Path(path).open("rb") as handle:
        for chunk in iter(lambda: handle.read(1 << 20), b""):
            digest.update(chunk)
    return digest.hexdigest()


def _canonical_bytes(value: object) -> bytes:
    return json.dumps(value, sort_keys=True, separators=(",", ":")).encode("utf-8")


def verify_frozen_dependencies() -> dict:
    expected = {
        PREREG_PATH: PREREG_SHA256,
        AMENDMENT_PATH: AMENDMENT_SHA256,
        ADAPTER_PATH: ADAPTER_SHA256,
        READPATH_PATH: READPATH_SHA256,
    }
    measured: dict[str, dict] = {}
    for path, digest in expected.items():
        actual = _sha256_file(path)
        mode = path.stat().st_mode & 0o777
        if actual != digest:
            raise ContractError(
                f"hash-pinned dependency changed: {path}",
                code="FAILED_FROZEN_DEPENDENCY",
                detail={"path": str(path), "expected": digest, "actual": actual},
            )
        measured[path.name] = {"sha256": actual, "mode": format(mode, "03o")}
    if (PREREG_PATH.stat().st_mode & 0o777) != 0o444:
        raise ContractError(
            "frozen preregistration mode is not 444",
            code="FAILED_FROZEN_MODE",
            detail={"path": str(PREREG_PATH), "actual_mode": measured[PREREG_PATH.name]["mode"]},
        )
    return measured


def _load_module(path: Path, digest: str, module_name: str):
    actual = _sha256_file(path)
    if actual != digest:
        raise ContractError(
            f"hash-pinned module changed: {path}",
            code="FAILED_FROZEN_DEPENDENCY",
            detail={"path": str(path), "expected": digest, "actual": actual},
        )
    existing = sys.modules.get(module_name)
    if existing is not None:
        return existing
    spec = importlib.util.spec_from_file_location(module_name, path)
    if spec is None or spec.loader is None:
        raise ContractError(f"cannot import {path}", code="FAILED_PINNED_IMPORT")
    module = importlib.util.module_from_spec(spec)
    sys.modules[module_name] = module
    spec.loader.exec_module(module)
    return module


def _adapter():
    return _load_module(ADAPTER_PATH, ADAPTER_SHA256, "nm_cutout_runner_pinned_adapter")


def _readpath():
    return _load_module(READPATH_PATH, READPATH_SHA256, "nm_cutout_runner_pinned_readpath")


def load_positions(path: Path) -> list[Position]:
    path = Path(path)
    positions: list[Position] = []
    with path.open(newline="", encoding="utf-8") as handle:
        reader = csv.DictReader(handle)
        if reader.fieldnames != ["ra", "dec", "ls_id"]:
            raise ContractError(
                "positions CSV header must be exactly ra,dec,ls_id",
                code="FAILED_POSITIONS_SCHEMA",
            )
        seen: set[str] = set()
        for line_number, row in enumerate(reader, start=2):
            try:
                ra = float(row["ra"])
                dec = float(row["dec"])
                ls_id = row["ls_id"]
            except (TypeError, ValueError) as exc:
                raise ContractError(
                    f"invalid position at line {line_number}", code="FAILED_POSITIONS_VALUE"
                ) from exc
            if not math.isfinite(ra) or not 0.0 <= ra < 360.0:
                raise ContractError("RA must be finite in [0,360)", code="FAILED_POSITIONS_VALUE")
            if not math.isfinite(dec) or not -90.0 <= dec <= 90.0:
                raise ContractError("Dec must be finite in [-90,90]", code="FAILED_POSITIONS_VALUE")
            if not ls_id or ls_id in seen:
                raise ContractError("ls_id must be nonempty and unique", code="FAILED_POSITIONS_VALUE")
            seen.add(ls_id)
            positions.append(Position(ra, dec, ls_id))
    return positions


def _load_slots(path: Path, *, real_sky: bool) -> tuple[dict, bytes]:
    path = Path(path)
    raw = path.read_bytes()
    slots = json.loads(raw)
    if set(slots) != {"ic4_invalid_fraction_cap", "ic5_scaling_map"}:
        raise ContractError("IC slot schema mismatch", code="FAILED_SLOT_SCHEMA")
    if real_sky and (
        slots["ic4_invalid_fraction_cap"] is None or slots["ic5_scaling_map"] is None
    ):
        raise ContractError(
            "real-sky object refused while IC-4/IC-5 binding slots are unfilled",
            code="REFUSED_REAL_SKY_UNFILLED_SLOTS",
        )
    return slots, raw


def _load_scaler(specification: object):
    if not isinstance(specification, dict):
        raise ContractError("IC-5 scaling-map slot is unfilled", code="FAILED_IC5_UNFILLED")
    required = {"module_path", "module_sha256", "callable", "constants"}
    if set(specification) != required:
        raise ContractError("IC-5 scaling-map schema mismatch", code="FAILED_IC5_SCHEMA")
    path = Path(str(specification["module_path"]))
    digest = str(specification["module_sha256"])
    module = _load_module(path, digest, "nm_frozen_scaler_" + digest[:16])
    function = getattr(module, str(specification["callable"]), None)
    if not callable(function):
        raise ContractError("IC-5 callable missing", code="FAILED_IC5_SCHEMA")
    return function, specification["constants"]


def apply_input_contract(
    raster: np.ndarray,
    *,
    slots_path: Path,
    real_sky: bool,
) -> tuple[np.ndarray, dict]:
    slots, slot_bytes = _load_slots(slots_path, real_sky=real_sky)
    plane = np.asarray(raster)
    if plane.ndim != 2 or plane.shape != EXPECTED_SHAPE:
        raise ContractError(
            "IC-1 requires exactly one 2-D 128x128 image plane",
            code="FAILED_IC1_SINGLE_PLANE",
            detail={"shape": list(plane.shape), "ndim": plane.ndim},
        )

    invalid = ~np.isfinite(plane)
    invalid_fraction = float(np.count_nonzero(invalid) / plane.size)
    cap = slots["ic4_invalid_fraction_cap"]
    if cap is None:
        raise ContractError("IC-4 cap slot is unfilled", code="FAILED_IC4_UNFILLED")
    if isinstance(cap, bool) or not isinstance(cap, (int, float)) or not math.isfinite(float(cap)):
        raise ContractError("IC-4 cap must be finite", code="FAILED_IC4_SCHEMA")
    cap = float(cap)
    if not 0.0 <= cap < 1.0:
        raise ContractError("IC-4 cap must be in [0,1)", code="FAILED_IC4_SCHEMA")
    if invalid_fraction > cap:
        raise ContractError(
            "IC-4 invalid fraction exceeds frozen cap",
            code="FAILED_IC4_INVALID_FRACTION_CAP",
            detail={"invalid_fraction": invalid_fraction, "cap": cap},
        )

    scaler, constants = _load_scaler(slots["ic5_scaling_map"])
    # IC-2/IC-3: the delivered nanomaggies are passed to the frozen map whole;
    # no unit conversion, background estimate, subtraction, or normalization.
    scaled = np.asarray(scaler(plane, constants))
    if scaled.shape != EXPECTED_SHAPE:
        raise ContractError("IC-5 changed raster shape", code="FAILED_IC5_OUTPUT")
    newly_invalid = ~np.isfinite(scaled) & ~invalid
    if np.any(newly_invalid):
        raise ContractError("IC-5 produced invalid values from valid input", code="FAILED_IC5_OUTPUT")
    scaled = np.array(scaled, copy=True)
    # IC-4 ordering is binding: replacement occurs only after scaling.
    scaled[invalid] = 0.0
    if not np.all(np.isfinite(scaled)):
        raise ContractError("nonfinite value survived IC-4", code="FAILED_IC4_REPLACEMENT")

    # IC-6: one materialization to little-endian float32, C-order, then channel insertion.
    tensor = np.array(scaled, dtype=np.dtype("<f4"), order="C", copy=True).reshape(TENSOR_SHAPE)
    if tensor.shape != TENSOR_SHAPE or not tensor.flags.c_contiguous or tensor.dtype != np.dtype("<f4"):
        raise ContractError("IC-6 layout postcondition failed", code="FAILED_IC6_LAYOUT")
    receipt = {
        "slot_file_sha256": _sha256_bytes(slot_bytes),
        "invalid_fraction": invalid_fraction,
        "invalid_fraction_cap": cap,
        "invalid_pixel_count": int(np.count_nonzero(invalid)),
        "invalid_replacement": "0.0_after_scaling",
        "delivered_units": "nanomaggies",
        "unit_operation_before_scaling": "NONE",
        "background_operation": "NONE",
        "scaling_map_module_sha256": slots["ic5_scaling_map"]["module_sha256"],
        "dtype": "<f4",
        "order": "C",
        "shape": list(tensor.shape),
        "big_endian_ingest_conversion_owner": "ProductionBrickSource np.array(..., dtype=np.float32, order='C')",
    }
    return tensor, receipt


def mirror_tensor(tensor: np.ndarray) -> np.ndarray:
    value = np.asarray(tensor)
    if value.shape != TENSOR_SHAPE or value.dtype != np.dtype("<f4") or not value.flags.c_contiguous:
        raise ContractError("IC-7 requires an IC-6 tensor", code="FAILED_IC7_INPUT")
    mirrored = np.ascontiguousarray(np.fliplr(value[0])[np.newaxis, :, :], dtype=np.dtype("<f4"))
    return mirrored


class _CutTarget:
    def __init__(self, position: Position) -> None:
        self.object_key = position.ls_id
        self.ra_deg = position.ra
        self.dec_deg = position.dec


def _safe_name(ls_id: str) -> str:
    encoded = hashlib.sha256(ls_id.encode("utf-8")).hexdigest()[:16]
    return f"object-{encoded}"


def _atomic_bytes(path: Path, payload: bytes) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    temporary = path.with_suffix(path.suffix + ".tmp")
    temporary.write_bytes(payload)
    os.replace(temporary, path)


def _atomic_json(path: Path, value: object) -> None:
    _atomic_bytes(path, json.dumps(value, sort_keys=True, separators=(",", ":")).encode("utf-8") + b"\n")


def compose_object(
    position: Position,
    bricks: Sequence[BrickSpec],
    *,
    slots_path: Path,
    output_dir: Path,
    synthetic: bool = False,
    mirror: bool = False,
) -> dict:
    dependency_receipt = verify_frozen_dependencies()
    output_dir = Path(output_dir)
    base = _safe_name(position.ls_id)
    receipt_path = output_dir / "receipts" / f"{base}.json"
    ic_flags = {f"IC-{index}": False for index in range(1, 8)}
    receipt: dict = {
        "receipt_version": 1,
        "status": "FAIL",
        "scope": "SYNTHETIC_FIXTURE" if synthetic else "REAL_SKY",
        "ls_id": position.ls_id,
        "position": {"ra": position.ra, "dec": position.dec},
        "dependencies": dependency_receipt,
        "brick_sha_refs": [
            {"brickname": brick.brickname, "path": str(Path(brick.path).resolve()), "sha256": brick.sha256}
            for brick in bricks
        ],
        "ic_flags": ic_flags,
        "invalid_fraction": None,
        "output_tensor_sha256": None,
    }
    sources: dict[str, object] = {}
    try:
        if not bricks:
            raise ContractError("no explicit brick references supplied", code="FAILED_NO_BRICKS")
        # This refusal precedes all real brick opens and therefore all real raster reads.
        _load_slots(slots_path, real_sky=not synthetic)
        reader = _readpath()
        adapter = _adapter()
        for brick in bricks:
            if brick.brickname in sources:
                raise ContractError("duplicate brickname", code="FAILED_DUPLICATE_BRICK")
            sources[brick.brickname] = reader.ProductionBrickSource(
                Path(brick.path), brick.row, brick.sha256
            )
        values, coverage, contributed = adapter.render_cutout(_CutTarget(position), sources)
        raster = np.asarray(values).reshape(EXPECTED_SHAPE)
        ic_flags["IC-1"] = True
        tensor, ic_receipt = apply_input_contract(
            raster, slots_path=slots_path, real_sky=not synthetic
        )
        for index in range(2, 7):
            ic_flags[f"IC-{index}"] = True
        receipt["invalid_fraction"] = ic_receipt["invalid_fraction"]
        if mirror:
            tensor = mirror_tensor(tensor)
        ic_flags["IC-7"] = True
        payload = tensor.tobytes(order="C")
        tensor_path = output_dir / "tensors" / f"{base}.f32le"
        _atomic_bytes(tensor_path, payload)
        output_wcs = adapter.build_output_wcs(position.ra, position.dec)
        receipt.update({
            "status": "PASS",
            "input_contract_receipt": ic_receipt,
            "adapter_geometry_receipt": {
                "adapter_sha256": ADAPTER_SHA256,
                "output_shape": [128, 128],
                "output_crpix": [adapter.OUT_CRPIX, adapter.OUT_CRPIX],
                "output_cd": [list(row) for row in adapter.OUT_CD],
                "output_cd_determinant": output_wcs.cd_det,
                "coverage_min": min(coverage),
                "coverage_max": max(coverage),
                "coverage_zero_count": sum(value == 0 for value in coverage),
                "coverage_plane_sha256": _sha256_bytes(
                    np.asarray(coverage, dtype=">i4").tobytes(order="C")
                ),
                "contributed_pixel_counts": contributed,
                "source_wcs_gate_receipts": {
                    name: source.gate_receipt for name, source in sources.items()
                },
            },
            "mirror_applied": mirror,
            "mirror_operation": "np.fliplr(tensor[0])" if mirror else "NOT_REQUESTED",
            "tensor": {
                "path": str(tensor_path.relative_to(output_dir)),
                "shape": list(tensor.shape),
                "dtype": "<f4",
                "order": "C",
                "byte_length": len(payload),
            },
            "output_tensor_sha256": _sha256_bytes(payload),
        })
    except Exception as exc:
        receipt["failure"] = {
            "code": getattr(exc, "code", type(exc).__name__),
            "message": str(exc),
            "detail": getattr(exc, "detail", {}),
        }
        _atomic_json(receipt_path, receipt)
        raise
    finally:
        for source in sources.values():
            source.close()
    receipt["content_hash_excludes"] = ["receipt_content_sha256"]
    receipt["receipt_content_sha256"] = _sha256_bytes(_canonical_bytes(receipt))
    _atomic_json(receipt_path, receipt)
    return receipt


def load_brick_manifest(path: Path) -> dict[str, list[BrickSpec]]:
    document = json.loads(Path(path).read_text(encoding="utf-8"))
    if document.get("schema_version") != 1 or not isinstance(document.get("objects"), dict):
        raise ContractError("brick manifest schema mismatch", code="FAILED_BRICK_MANIFEST")
    result: dict[str, list[BrickSpec]] = {}
    for ls_id, entries in document["objects"].items():
        if not isinstance(entries, list):
            raise ContractError("brick manifest object value must be a list", code="FAILED_BRICK_MANIFEST")
        result[ls_id] = [
            BrickSpec(
                path=Path(entry["path"]),
                row={"ra": float(entry["row"]["ra"]), "dec": float(entry["row"]["dec"])},
                sha256=str(entry["sha256"]),
                brickname=str(entry["brickname"]),
            )
            for entry in entries
        ]
    return result


def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--positions", type=Path, required=True)
    parser.add_argument("--brick-manifest", type=Path, required=True)
    parser.add_argument("--slots", type=Path, default=HERE / "ic_slots.json")
    parser.add_argument("--output-dir", type=Path, required=True)
    parser.add_argument("--synthetic", action="store_true")
    parser.add_argument("--mirror", action="store_true")
    args = parser.parse_args(argv)
    positions = load_positions(args.positions)
    manifest = load_brick_manifest(args.brick_manifest)
    if set(manifest) != {position.ls_id for position in positions}:
        raise ContractError(
            "brick manifest keys must exactly match explicit position ls_id values",
            code="FAILED_BRICK_MANIFEST_COVERAGE",
        )
    failures = 0
    for position in positions:
        try:
            compose_object(
                position,
                manifest[position.ls_id],
                slots_path=args.slots,
                output_dir=args.output_dir,
                synthetic=args.synthetic,
                mirror=args.mirror,
            )
        except Exception:
            failures += 1
    return 1 if failures else 0


if __name__ == "__main__":
    raise SystemExit(main())
