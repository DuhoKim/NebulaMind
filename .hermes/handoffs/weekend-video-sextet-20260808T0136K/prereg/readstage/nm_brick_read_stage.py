#!/usr/bin/env python3
"""Pinned read/decompression stage for production-shaped .fits.fz bricks.

Architecture (Kun's round-4 read-path assessment, chosen by Duho): the
production adapter `nm_brick_cutout_adapter.py` stays stdlib-only — planning,
WCS gating, PC-3/PC-4 receipts, and bilinear cut semantics never import a
third-party package. Decoding compressed FITS moves HERE, into a separate
component that MAY use a pinned third-party decoder (astropy.io.fits).

Contract:
1. open HDU 1 of a production-shaped file (empty primary + RICE_1 compressed
   image extension) with the pinned decoder;
2. verify ZIMAGE, ZCMPTYPE == RICE_1, ZBITPIX == -32, ZNAXIS1/2 == 3600 on
   the RAW extension header cards, before any decode — a mismatch is
   terminal, never a warning;
3. verify the decompressed float32 array shape and the source WCS cards
   against the geometry sidecar row;
4. emit a canonical uncompressed raster handoff in the adapter's exact staged
   format, written by the adapter's own fixture writer — so the adapter
   cannot tell whether its bytes came from an uncompressed fixture or a
   decompressed production brick, and every prior adapter gate keeps
   standing;
5. produce a receipt chaining source file hash -> raw primary/HDU-1 header
   hashes -> decompressed array hash -> decoder environment lock -> adapter
   input bytes, with the same content_sha256 identity discipline as the
   cross-check receipt (excludes exactly ['content_sha256', 'recorded_utc'],
   exclusion list inside the hashed body).

BUILD-ONLY GUARD: the logical image header must carry the synthetic marker
card `SYNTHET = T`. A header without it is refused terminally; lifting this
guard for real DR10 bricks is a later explicit gate, not a default.

The decoder environment lock recorded here (interpreter/astropy/numpy
versions plus SHA-256 of astropy's tile-compression modules) is a partial
pin; the full dependency lock is Yui's separate deliverable and "pinned
decoder" claims defer to it.

Synthetic only. No network, no real survey data.
"""
from __future__ import annotations

import hashlib
import json
import platform
import sys
from datetime import datetime, timezone
from pathlib import Path
from typing import Mapping, Optional

import numpy as np
import astropy
from astropy.io import fits
import astropy.io.fits.hdu.compressed as astropy_compressed

HERE = Path(__file__).resolve().parent
PREREG = HERE.parent
sys.path.insert(0, str(PREREG / "adapter"))

import nm_brick_cutout_adapter as tori  # noqa: E402  (stdlib-only adapter, imported not modified)

RECEIPT_HASH_EXCLUDES = ["content_sha256", "recorded_utc"]
REQUIRED_COMPRESSION = {
    "ZIMAGE": True,
    "ZCMPTYPE": "RICE_1",
    "ZBITPIX": -32,
    "ZNAXIS": 2,
    "ZNAXIS1": tori.SRC_N,
    "ZNAXIS2": tori.SRC_N,
}


class ReadStageError(RuntimeError):
    def __init__(self, message: str, *, code: str) -> None:
        super().__init__(message)
        self.code = code


def _sha256_bytes(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def _utc_now() -> str:
    return datetime.now(timezone.utc).isoformat(timespec="seconds").replace("+00:00", "Z")


def decoder_environment_lock() -> dict:
    """Partial decoder pin; the full environment lock is Yui's deliverable."""
    compressed_dir = Path(astropy_compressed.__file__).resolve().parent
    module_hashes = {}
    for name in ("compressed.py", "_tiled_compression.py"):
        module_hashes[name] = _sha256_bytes((compressed_dir / name).read_bytes())
    extensions = sorted(compressed_dir.glob("_compression.*"))
    for extension in extensions:
        module_hashes[extension.name] = _sha256_bytes(extension.read_bytes())
    return {
        "python_version": platform.python_version(),
        "astropy_version": astropy.__version__,
        "numpy_version": np.__version__,
        "astropy_tiled_compression_module_sha256": module_hashes,
        "full_dependency_lock": (
            "Yui's dependency-lock deliverable (separate); this record is a partial pin and "
            "does not by itself establish the pinned-resampler or pinned-decoder claim"
        ),
    }


def read_production_brick(
    source_path: Path,
    geometry_row: Mapping[str, object],
    staging_root: Path,
    *,
    expected_file_sha256: Optional[str] = None,
    expected_wcs_cards: Optional[Mapping[str, object]] = None,
    write_receipt: bool = True,
) -> dict:
    """Decode one production-shaped .fits.fz brick into the adapter's staged format.

    Returns the chained read receipt. Raises ReadStageError terminally on any
    contract violation; nothing is staged on failure.
    """
    source_path = Path(source_path)
    staging_root = Path(staging_root)
    brickname = str(geometry_row["brickname"])

    if source_path.is_symlink() or not source_path.is_file():
        raise ReadStageError(
            f"source missing or not a regular file: {source_path}", code="FAILED_SOURCE_MISSING"
        )
    blob = source_path.read_bytes()
    source_sha256 = _sha256_bytes(blob)
    if expected_file_sha256 is not None and source_sha256 != expected_file_sha256:
        raise ReadStageError(
            f"source digest mismatch: {source_path.name}", code="FAILED_SOURCE_DIGEST"
        )

    # Raw pre-parse on literal cards, before the decoder touches anything.
    try:
        primary_cards, _, primary_end, primary_header_sha256 = tori.parse_fits_header(blob)
    except tori.FitsIntegrityError as exc:
        raise ReadStageError(f"unreadable primary header: {exc}", code="FAILED_FITS_INTEGRITY")
    if primary_cards.get("SIMPLE") is not True or primary_cards.get("NAXIS") != 0:
        raise ReadStageError(
            f"{source_path.name}: primary HDU is not the empty production shape",
            code="FAILED_PRIMARY_NOT_EMPTY",
        )
    try:
        extension_cards, _, _, extension_header_sha256 = tori.parse_fits_header(
            blob, offset=primary_end
        )
    except tori.FitsIntegrityError as exc:
        raise ReadStageError(f"unreadable HDU-1 header: {exc}", code="FAILED_FITS_INTEGRITY")
    if str(extension_cards.get("XTENSION", "")).strip() != "BINTABLE":
        raise ReadStageError(
            f"{source_path.name}: HDU 1 is not a compressed-image binary table",
            code="FAILED_COMPRESSION_CONTRACT",
        )
    for keyword, expected in REQUIRED_COMPRESSION.items():
        observed = extension_cards.get(keyword)
        if observed != expected:
            raise ReadStageError(
                f"{source_path.name}: {keyword}={observed!r}, contract requires {expected!r}",
                code="FAILED_COMPRESSION_CONTRACT",
            )
    for keyword in ("ZTILE1", "ZTILE2"):
        if keyword not in extension_cards:
            raise ReadStageError(
                f"{source_path.name}: missing tile card {keyword}",
                code="FAILED_COMPRESSION_CONTRACT",
            )

    # Decode HDU 1 with the pinned decoder.
    try:
        with fits.open(source_path, memmap=False) as hdus:
            if len(hdus) != 2 or hdus[0].data is not None:
                raise ReadStageError(
                    f"{source_path.name}: expected exactly empty primary plus image HDU 1",
                    code="FAILED_COMPRESSION_CONTRACT",
                )
            image = hdus[1]
            if not isinstance(image, fits.CompImageHDU) or image.compression_type != "RICE_1":
                raise ReadStageError(
                    f"{source_path.name}: HDU 1 is not a RICE_1 compressed image",
                    code="FAILED_COMPRESSION_CONTRACT",
                )
            logical_header = image.header
            data = np.ascontiguousarray(image.data, dtype=np.float32)
    except ReadStageError:
        raise
    except Exception as exc:  # decoder failure is terminal, never a warning
        raise ReadStageError(f"{source_path.name}: decode failed: {exc}", code="FAILED_DECODE")

    if data.shape != (tori.SRC_N, tori.SRC_N):
        raise ReadStageError(
            f"{source_path.name}: decompressed shape {data.shape} != ({tori.SRC_N}, {tori.SRC_N})",
            code="FAILED_SHAPE",
        )
    if logical_header.get("SYNTHET") is not True:
        raise ReadStageError(
            f"{source_path.name}: BUILD_ONLY_STOP - logical header lacks the synthetic marker; "
            "reading non-synthetic bricks requires a later explicit gate",
            code="FAILED_BUILD_ONLY_SCOPE",
        )

    # Source WCS cards against the geometry sidecar. Default expectation is
    # the production model (per-brick TAN at the brick centre, CRPIX 1800.5,
    # frozen CD). A fixture whose declared WCS legitimately differs (Yui's
    # round-1 shared-tangent bricks) must pass its declared cards explicitly;
    # the receipt records which model was verified.
    if expected_wcs_cards is not None:
        expected_wcs = dict(expected_wcs_cards)
        wcs_verification_model = "fixture-declared-cards"
    else:
        expected_wcs = {
            "CTYPE1": "RA---TAN", "CTYPE2": "DEC--TAN",
            "CRVAL1": float(geometry_row["ra"]), "CRVAL2": float(geometry_row["dec"]),
            "CRPIX1": tori.SRC_CRPIX, "CRPIX2": tori.SRC_CRPIX,
            "CD1_1": tori.OUT_CD[0][0], "CD1_2": tori.OUT_CD[0][1],
            "CD2_1": tori.OUT_CD[1][0], "CD2_2": tori.OUT_CD[1][1],
        }
        wcs_verification_model = "production-per-brick-tan"
    for keyword, expected in expected_wcs.items():
        observed = logical_header.get(keyword)
        if isinstance(expected, float):
            if not isinstance(observed, (int, float)) or abs(float(observed) - expected) > 1e-12:
                raise ReadStageError(
                    f"{source_path.name}: {keyword}={observed!r} disagrees with geometry sidecar",
                    code="FAILED_WCS_MISMATCH",
                )
        elif observed != expected:
            raise ReadStageError(
                f"{source_path.name}: {keyword}={observed!r} disagrees with geometry sidecar",
                code="FAILED_WCS_MISMATCH",
            )

    decompressed_sha256 = _sha256_bytes(data.tobytes(order="C"))

    # Canonical handoff: the adapter's OWN writer emits the staged bytes, so
    # the adapter input contract is exactly today's and provenance is
    # indistinguishable from an uncompressed fixture.
    staged_path = tori.write_synthetic_brick(
        staging_root, geometry_row,
        data_big_endian=np.ascontiguousarray(data.astype(">f4")).tobytes(),
    )
    staged_sha256 = _sha256_bytes(staged_path.read_bytes())

    receipt = {
        "scope": tori.SCOPE,
        "component": "nm_brick_read_stage",
        "brickname": brickname,
        "source_basename": source_path.name,
        "source_file_sha256": source_sha256,
        "raw_primary_header_sha256": primary_header_sha256,
        "raw_hdu1_header_sha256": extension_header_sha256,
        "raw_compression_cards": {
            keyword: extension_cards[keyword]
            for keyword in ("ZIMAGE", "ZCMPTYPE", "ZBITPIX", "ZNAXIS", "ZNAXIS1", "ZNAXIS2",
                            "ZTILE1", "ZTILE2")
        },
        "decompressed_array_sha256": decompressed_sha256,
        "wcs_verification_model": wcs_verification_model,
        "verified_wcs_cards": {key: expected_wcs[key] for key in sorted(expected_wcs)},
        "adapter_input_relpath": str(staged_path.relative_to(staging_root)),
        "adapter_input_file_sha256": staged_sha256,
        "adapter_sha256": _sha256_bytes((PREREG / "adapter" / "nm_brick_cutout_adapter.py").read_bytes()),
        "decoder_environment_lock": decoder_environment_lock(),
        "content_hash_excludes": list(RECEIPT_HASH_EXCLUDES),
    }
    hash_body = {key: value for key, value in receipt.items() if key not in RECEIPT_HASH_EXCLUDES}
    receipt["content_sha256"] = _sha256_bytes(
        json.dumps(hash_body, sort_keys=True, separators=(",", ":")).encode("utf-8")
    )
    receipt["recorded_utc"] = _utc_now()
    if write_receipt:
        receipt_dir = staging_root / "read_receipts"
        receipt_dir.mkdir(parents=True, exist_ok=True)
        (receipt_dir / f"{brickname}.json").write_text(
            json.dumps(receipt, indent=2, sort_keys=True) + "\n", encoding="utf-8"
        )
    return receipt
