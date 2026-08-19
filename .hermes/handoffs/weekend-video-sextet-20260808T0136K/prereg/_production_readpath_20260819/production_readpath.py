#!/usr/bin/env python3
"""Deterministic production reader for DR10 South fpack-compressed coadds.

The adapter remains unchanged and stdlib-only. This module owns the production
boundary: digest verification, Astropy/CFITSIO decompression of image HDU 1,
PC-4 header gating through the hash-pinned adapter, and immutable float32 array
materialization for the adapter-compatible ``pixel(ix, iy)`` interface.
"""
from __future__ import annotations

import hashlib
import importlib.util
import json
import multiprocessing
import sys
import time
from concurrent.futures import ProcessPoolExecutor, as_completed
from datetime import datetime, timezone
from pathlib import Path
from typing import Mapping, Sequence

import astropy
import numpy as np
from astropy.io import fits

ASTROPY_VERSION = "6.0.1"
NUMPY_VERSION = "1.26.4"
DEFAULT_SHAPE = (3600, 3600)
ADAPTER_SHA256 = "267b2a93d2a61f65b281aeb3b04dd874d7add058797b10f593cb3efb4066006f"
HERE = Path(__file__).resolve().parent
ADAPTER_PATH = HERE.parent / "adapter" / "nm_brick_cutout_adapter.py"


class ReadPathError(RuntimeError):
    def __init__(self, message: str, *, code: str, detail: dict | None = None) -> None:
        super().__init__(message)
        self.code = code
        self.detail = dict(detail or {})


def _sha256_bytes(payload: bytes) -> str:
    return hashlib.sha256(payload).hexdigest()


def _sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1 << 20), b""):
            digest.update(chunk)
    return digest.hexdigest()


def _canonical_bytes(value: object) -> bytes:
    return json.dumps(value, sort_keys=True, separators=(",", ":")).encode("utf-8")


def _utc_now() -> str:
    return datetime.now(timezone.utc).isoformat(timespec="seconds").replace("+00:00", "Z")


def _load_adapter():
    actual = _sha256_file(ADAPTER_PATH)
    if actual != ADAPTER_SHA256:
        raise ReadPathError(
            "hash-pinned gated adapter changed",
            code="FAILED_ADAPTER_DIGEST",
            detail={"expected": ADAPTER_SHA256, "actual": actual},
        )
    module_name = "nm_production_hash_pinned_adapter"
    module = sys.modules.get(module_name)
    if module is not None:
        return module
    spec = importlib.util.spec_from_file_location(module_name, ADAPTER_PATH)
    if spec is None or spec.loader is None:
        raise ReadPathError("cannot import gated adapter", code="FAILED_ADAPTER_IMPORT")
    module = importlib.util.module_from_spec(spec)
    sys.modules[module_name] = module
    spec.loader.exec_module(module)
    return module


def _logical_header_cards(header: fits.Header) -> tuple[dict[str, object], list[str]]:
    cards: dict[str, object] = {}
    ordered_keys: list[str] = []
    for card in header.cards:
        key = card.keyword.upper()
        # Match the adapter's raw-card parser: COMMENT/HISTORY and blank cards
        # do not have value-card syntax and therefore do not enter PC-4.
        if not key or key in {"COMMENT", "HISTORY", "END"}:
            continue
        ordered_keys.append(key)
        cards[key] = card.value
    return cards, ordered_keys


class ProductionBrickSource:
    """Digest-verified HDU-1 source matching ``SyntheticBrickSource`` access.

    The first three arguments intentionally match the gated adapter source
    constructor. ``expected_shape`` exists only to permit small offline-safe
    compressed fixtures; real DR10 use keeps the 3600x3600 default.
    """

    def __init__(
        self,
        path: Path,
        row: Mapping[str, float],
        expected_sha256: str,
        *,
        expected_shape: tuple[int, int] = DEFAULT_SHAPE,
    ) -> None:
        if astropy.__version__ != ASTROPY_VERSION or np.__version__ != NUMPY_VERSION:
            raise ReadPathError(
                "production decompressor dependency version drift",
                code="FAILED_DEPENDENCY_PIN",
                detail={
                    "expected_astropy": ASTROPY_VERSION,
                    "actual_astropy": astropy.__version__,
                    "expected_numpy": NUMPY_VERSION,
                    "actual_numpy": np.__version__,
                },
            )
        path = Path(path)
        if path.is_symlink() or not path.is_file():
            raise ReadPathError(
                f"planned source missing or not a regular file: {path}",
                code="FAILED_SOURCE_MISSING",
            )
        actual_sha256 = _sha256_file(path)
        if actual_sha256 != expected_sha256:
            raise ReadPathError(
                f"planned source digest mismatch: {path}",
                code="FAILED_SOURCE_DIGEST",
                detail={"expected": expected_sha256, "actual": actual_sha256},
            )

        adapter = _load_adapter()
        try:
            with fits.open(
                path,
                mode="readonly",
                memmap=False,
                lazy_load_hdus=False,
                checksum=False,
            ) as hdul:
                if len(hdul) <= 1:
                    raise ReadPathError("image HDU 1 is missing", code="FAILED_HDU_SELECTION")
                hdu = hdul[1]
                if not isinstance(hdu, fits.CompImageHDU):
                    raise ReadPathError(
                        f"HDU 1 is {type(hdu).__name__}, not fpack CompImageHDU",
                        code="FAILED_HDU_SELECTION",
                    )
                header = hdu.header.copy()
                cards, ordered_keys = _logical_header_cards(header)
                gate_receipt = adapter.fail_closed_header_gate(
                    cards, ordered_keys, context=f"production_source:{path.name}:HDU1"
                )
                data = hdu.data
                if data is None:
                    raise ReadPathError("HDU 1 has no image data", code="FAILED_FITS_INTEGRITY")
                array = np.array(data, dtype=np.float32, order="C", copy=True)
                compression_type = str(getattr(hdu, "compression_type", "UNKNOWN"))
        except ReadPathError:
            raise
        except adapter.WcsRejectedError as exc:
            raise ReadPathError(
                str(exc), code=exc.code, detail=getattr(exc, "detail", None)
            ) from exc
        except Exception as exc:
            raise ReadPathError(
                f"Astropy failed to read fpack image HDU 1: {exc}",
                code="FAILED_FITS_INTEGRITY",
            ) from exc

        if array.shape != expected_shape:
            raise ReadPathError(
                f"HDU 1 shape mismatch expected={expected_shape} actual={array.shape}",
                code="FAILED_SOURCE_SHAPE",
            )
        if int(cards.get("NAXIS", -1)) != 2:
            raise ReadPathError("logical HDU 1 is not a 2-D image", code="FAILED_SOURCE_SHAPE")
        if (int(cards.get("NAXIS2", -1)), int(cards.get("NAXIS1", -1))) != expected_shape:
            raise ReadPathError("logical header dimensions disagree with array", code="FAILED_SOURCE_SHAPE")
        for key, expected in (("CRVAL1", row["ra"]), ("CRVAL2", row["dec"])):
            if abs(float(cards[key]) - float(expected)) > 1e-12:
                raise ReadPathError(
                    f"source header {key} disagrees with geometry sidecar",
                    code="REJECTED_GEOMETRY_MISMATCH",
                )

        array.setflags(write=False)
        logical_header_bytes = header.tostring(sep="", endcard=True, padding=True).encode("ascii")
        array_sha256 = _sha256_bytes(array.tobytes(order="C"))
        wcs = adapter.TanWcs(
            cards["CRVAL1"],
            cards["CRVAL2"],
            cards["CRPIX1"],
            cards["CRPIX2"],
            [
                [gate_receipt["linear_matrix"][0][0], gate_receipt["linear_matrix"][0][1]],
                [gate_receipt["linear_matrix"][1][0], gate_receipt["linear_matrix"][1][1]],
            ],
        )

        self.path = path
        self.sha256 = actual_sha256
        self.header_sha256 = _sha256_bytes(logical_header_bytes)
        self.cards = cards
        self.data_offset = None  # compressed HDU has no adapter-readable flat byte offset
        self.wcs = wcs
        self.gate_receipt = gate_receipt
        self.array = array
        self.header_receipt = {
            "receipt_version": 1,
            "source_path": str(path.resolve()),
            "source_file_sha256": actual_sha256,
            "adapter_sha256": ADAPTER_SHA256,
            "hdu_index": 1,
            "hdu_class": "CompImageHDU",
            "hdu_name": str(header.get("EXTNAME", "COMPRESSED_IMAGE")),
            "compression_type": compression_type,
            "decompressor": "astropy.io.fits",
            "astropy_version": astropy.__version__,
            "numpy_version": np.__version__,
            "logical_header_sha256": self.header_sha256,
            "shape": list(array.shape),
            "dtype": str(array.dtype),
            "array_byte_order": "native",
            "array_memory_order": "C",
            "array_sha256": array_sha256,
            "wcs_custody": {
                "status": "VERIFIED_NOT_ASSUMED",
                "header_source": "decompressed logical image header from physical HDU 1",
                "wcs_fields": {
                    key: cards[key]
                    for key in (
                        "CTYPE1", "CTYPE2", "CRVAL1", "CRVAL2", "CRPIX1", "CRPIX2",
                        "CD1_1", "CD1_2", "CD2_1", "CD2_2",
                    )
                },
                "linear_matrix": gate_receipt["linear_matrix"],
                "linear_determinant": gate_receipt["linear_determinant"],
                "combined_pixel_to_sky_determinant": gate_receipt[
                    "combined_pixel_to_sky_determinant"
                ],
                "east_left": gate_receipt["east_left"],
                "north_up": gate_receipt["north_up"],
                "row_order_transform": "array[iy-1, ix-1]",
                "pixel_origin": "FITS one-based pixel centres",
                "pc4_gate_passed": True,
                "pc4_gate_receipt": gate_receipt,
            },
        }

    def pixel(self, ix: int, iy: int) -> float:
        height, width = self.array.shape
        if not (1 <= ix <= width and 1 <= iy <= height):
            raise IndexError(f"FITS pixel outside image: ix={ix} iy={iy}")
        return float(self.array[iy - 1, ix - 1])

    def write_header_receipt(self, path: Path) -> Path:
        """Atomically log the verified HDU/WCS custody receipt."""
        path = Path(path)
        path.parent.mkdir(parents=True, exist_ok=True)
        temporary = path.with_suffix(path.suffix + ".tmp")
        temporary.write_text(
            json.dumps(self.header_receipt, sort_keys=True, separators=(",", ":")) + "\n",
            encoding="utf-8",
        )
        temporary.replace(path)
        return path

    def close(self) -> None:
        # The decompressed array is an owned copy; the FITS handle was closed
        # atomically before construction completed.
        return None

    def __enter__(self) -> "ProductionBrickSource":
        return self

    def __exit__(self, exc_type, exc_value, traceback) -> None:
        self.close()


def _worker_read(arguments: tuple) -> dict:
    path, row, expected_sha256, expected_shape, delay, task_token = arguments
    if delay:
        time.sleep(delay)
    with ProductionBrickSource(
        Path(path), row, expected_sha256, expected_shape=tuple(expected_shape)
    ) as source:
        # The task token is stripped into an explicitly excluded scheduling
        # observation before stable worker results are canonicalized. No PID,
        # hostname, timestamp, or completion position enters stable content.
        return {
            "_schedule_task_token": task_token,
            "array_sha256": source.header_receipt["array_sha256"],
            "logical_header_sha256": source.header_sha256,
            "source_file_sha256": source.sha256,
            "shape": list(source.array.shape),
            "dtype": str(source.array.dtype),
            "wcs_custody": source.header_receipt["wcs_custody"],
        }


def multiprocess_determinism_check(
    path: Path,
    row: Mapping[str, float],
    expected_sha256: str,
    *,
    process_count: int,
    expected_shape: tuple[int, int] = DEFAULT_SHAPE,
    completion_delays: Sequence[float] | None = None,
) -> dict:
    """Read one brick in N spawned processes and emit a stable receipt.

    Results are collected in completion order and then canonicalized, so forced
    scheduling/completion changes cannot alter ``stable_content`` or its hash.
    """
    if process_count < 1:
        raise ValueError("process_count must be positive")
    delays = tuple(completion_delays or (0.0,) * process_count)
    if len(delays) != process_count:
        raise ValueError("completion_delays must contain one delay per process")
    arguments = [
        (
            str(Path(path)), dict(row), expected_sha256, tuple(expected_shape),
            float(delays[index]), f"task-{index}",
        )
        for index in range(process_count)
    ]
    context = multiprocessing.get_context("spawn")
    completion_order_results: list[dict] = []
    observed_completion_order: list[str] = []
    with ProcessPoolExecutor(max_workers=process_count, mp_context=context) as executor:
        futures = [executor.submit(_worker_read, argument) for argument in arguments]
        for future in as_completed(futures):
            result = future.result()
            observed_completion_order.append(result.pop("_schedule_task_token"))
            completion_order_results.append(result)

    canonical_results = sorted(
        completion_order_results,
        key=lambda value: _canonical_bytes(value),
    )
    array_hashes = {result["array_sha256"] for result in canonical_results}
    header_hashes = {result["logical_header_sha256"] for result in canonical_results}
    all_arrays_identical = len(array_hashes) == 1
    if not all_arrays_identical or len(header_hashes) != 1:
        raise ReadPathError(
            "multiprocessing read results are not deterministic",
            code="FAILED_MULTIPROCESS_DETERMINISM",
        )
    stable_content = {
        "receipt_version": 1,
        "check": "N spawned processes read the same receipt-accepted HDU-1 brick",
        "process_start_method": "spawn",
        "process_count": process_count,
        "worker_result_count": len(canonical_results),
        "canonical_worker_results": canonical_results,
        "all_arrays_identical": True,
        "array_sha256": next(iter(array_hashes)),
        "logical_header_sha256": next(iter(header_hashes)),
        "scheduling_canonicalization": "collect completion order, then sort canonical JSON bytes",
        "content_hash_excludes": ["observed_completion_order", "recorded_utc"],
    }
    return {
        "stable_content": stable_content,
        "content_sha256": _sha256_bytes(_canonical_bytes(stable_content)),
        "recorded_utc": _utc_now(),
        "observed_completion_order": observed_completion_order,
        "all_arrays_identical": True,
        "array_sha256": stable_content["array_sha256"],
    }
