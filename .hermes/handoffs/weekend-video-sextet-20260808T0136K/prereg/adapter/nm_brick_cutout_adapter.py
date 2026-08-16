#!/usr/bin/env python3
"""Build-only guarded local-cut adapter for the Globus DR10.1 South brick route.

STOP RULE: this module is structurally incapable of transferring or fetching.
It imports no HTTP library, no socket layer, no Globus SDK, and no subprocess
machinery. There is no fetch(), no submit(), and no transport class of any
kind. The only executable behaviors are: brick-working-set planning against a
synthetic geometry table, sealed transfer-manifest construction (dry run,
never issued), and local cutting of explicitly synthetic staged brick files
with PC-3/PC-4 gates atomic to output acceptance.

Authority:
- TORI_ROUTE_BINDING_20260815.md
  c7ed11c12ad7c26db8ce784b4d4d76c86694231d4eaab42b3ddca720a265d4cb
- PREREG_LONGO_AMPLITUDE_TEST_FROZEN_20260815_V3.md (frozen, mode 444)
  b06901c8a0f3a0570af41262453670589d8dc0b20c79c7d4162853c7dfec42d7

Known stand-ins that must be replaced at the environment-lock gate before any
real execution (documented in TORI_ADAPTER_20260815.md):
- synthetic staged bricks are uncompressed primary-HDU FITS; production reads
  fpack-compressed image HDU 1 through the pinned fitsio/Imagine layer;
- the per-pixel renderer is a deterministic bilinear resampler whose
  semantics match the fixture oracle (2026-08-16 resampler gate); its
  equivalence with the hash-pinned Imagine/astrometry.net production kernel
  is bound to Yui's dependency lock and is not asserted here.
"""
from __future__ import annotations

import argparse
import hashlib
import importlib.util
import json
import math
import re
import struct
import sys
from datetime import datetime, timezone
from pathlib import Path
from typing import Callable, Iterable, Mapping, Optional

BUILD_ONLY = True
SCOPE = "SYNTHETIC_ONLY_BUILD"

ROUTE_BINDING_SHA256 = "c7ed11c12ad7c26db8ce784b4d4d76c86694231d4eaab42b3ddca720a265d4cb"
FROZEN_PREREG_SHA256 = "b06901c8a0f3a0570af41262453670589d8dc0b20c79c7d4162853c7dfec42d7"

HERE = Path(__file__).resolve().parent
PARITY_VALIDATOR_PATH = HERE.parent / "yui_bs5_sign_anchor_20260814" / "validate_wcs_parity.py"
PARITY_VALIDATOR_SHA256 = "7bf0201917e7722ee9545c9c11b6cc1cbdec345504e3f29fa1aeb01e58edaa55"
DISTORTION_VALIDATOR_PATH = HERE.parent / "_tori_bs7_distortion_evidence" / "fail_closed_wcs.py"
DISTORTION_VALIDATOR_SHA256 = "cae1b1b7ef4e25000ad5d8c906647216b1425638ac737b4ea7363ca948760569"

# Frozen output geometry, route binding section 7.2.
OUT_N = 128
SRC_N = 3600
PIX_SCALE_DEG = 0.262 / 3600.0
OUT_CRPIX = 64.5
SRC_CRPIX = 1800.5
OUT_CD = ((-PIX_SCALE_DEG, 0.0), (0.0, PIX_SCALE_DEG))
# Determinant bound to the product of the frozen CD terms. The route binding's
# human-readable literal -5.296604938271605e-09 differs from this product in
# the final digit; the executable check binds to the CD terms, and the
# discrepancy is reported in TORI_ADAPTER_20260815.md rather than adopted.
OUT_CD_DET = OUT_CD[0][0] * OUT_CD[1][1] - OUT_CD[0][1] * OUT_CD[1][0]
ROUND_TRIP_TOLERANCE_PIXELS = 1e-6

# Transfer custody constants, route binding sections 4 and 5. Recorded in the
# sealed dry-run manifest only; nothing in this module can contact them.
SOURCE_COLLECTION_UUID = "9d6d994a-6d04-11e5-ba46-22000b92c6ec"
MANIFEST_RELEASE = "dr10.1-latest-byte-bound"
MANIFEST_FORMAT_VERSION = 1
CFS_IMAGE_TEMPLATE = (
    "/global/cfs/cdirs/cosmo/data/legacysurvey/dr10/south/coadd/"
    "{aaa}/{brickname}/legacysurvey-{brickname}-image-r.fits.fz"
)
GEOMETRY_SIDECAR_CFS_PATH = (
    "/global/cfs/cdirs/cosmo/data/legacysurvey/dr10/south/survey-bricks-dr10-south.fits.gz"
)
MANIFEST_OBJECT_LIST_HASH_THRESHOLD = 1000

# Widest object-centre-to-brick-centre separation at which a source image can
# still intersect the output footprint: source half-diagonal (~667") plus
# output half-diagonal (~24"), with slack. The polygon test decides inclusion.
CANDIDATE_PREFILTER_DEG = 0.21

# Tolerance for classifying neighbour reasons from rectangular unique-area
# adjacency. Rectangular (ra, dec) bounds are a projection of the true brick
# geometry and can carry seams of order 1e-4 deg away from the tangent point
# (the 2026-08-16 corner-fixture failure class), so classification must absorb
# them. Reasons are grouping/manifest metadata only — never a selection rule.
REASON_CLASSIFICATION_TOLERANCE_DEG = 1e-3

TERMINAL_FAILURE_STATUSES = {
    "FAILED_FITS_INTEGRITY",
    "FAILED_INVALID_PIXEL_CAP",
    "FAILED_OUTPUT_ACCEPTANCE",
    "FAILED_PLAN_NO_SOURCES",
    "FAILED_SOURCE_DIGEST",
    "FAILED_SOURCE_MISSING",
    "FAILED_ZERO_COVERAGE",
    "REJECTED_AMBIGUOUS_WCS",
    "REJECTED_ALTERNATE_WCS",
    "REJECTED_DISTORTION",
    "REJECTED_DUPLICATE_KEY",
    "REJECTED_GEOMETRY_MISMATCH",
    "REJECTED_INCOMPLETE_WCS",
    "REJECTED_LINEAR_WCS",
    "REJECTED_LOOKUP_DISTORTION",
    "REJECTED_NON_CELESTIAL",
    "REJECTED_NONFINITE_WCS",
    "REJECTED_NON_TAN",
    "REJECTED_PARITY",
    "REJECTED_SINGULAR_WCS",
    "REJECTED_SWAPPED_AXES",
}


class FitsIntegrityError(RuntimeError):
    pass


class ManifestError(RuntimeError):
    pass


class WcsRejectedError(RuntimeError):
    def __init__(self, message: str, *, code: str, detail: Optional[dict] = None) -> None:
        super().__init__(message)
        self.code = code
        self.detail = dict(detail or {})


class ObjectTerminalError(RuntimeError):
    def __init__(self, message: str, *, code: str, detail: Optional[dict] = None) -> None:
        super().__init__(message)
        self.code = code
        self.detail = dict(detail or {})


# ---------------------------------------------------------------------------
# Small custody helpers (hash chain, canonical JSON, hash-pinned imports).
# ---------------------------------------------------------------------------

def _canonical_bytes(value: object) -> bytes:
    return json.dumps(value, sort_keys=True, separators=(",", ":")).encode("utf-8")


def _sha256_bytes(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def _sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        while True:
            chunk = handle.read(1 << 20)
            if not chunk:
                break
            digest.update(chunk)
    return digest.hexdigest()


def _utc_now() -> str:
    return datetime.now(timezone.utc).isoformat(timespec="seconds").replace("+00:00", "Z")


def _self_sha256() -> str:
    return _sha256_bytes(Path(__file__).resolve().read_bytes())


def _load_hash_pinned_module(path: Path, expected_sha256: str, module_name: str):
    data = path.read_bytes()
    actual = _sha256_bytes(data)
    if actual != expected_sha256:
        raise RuntimeError(
            f"hash-pinned dependency changed: {path} expected={expected_sha256} actual={actual}"
        )
    spec = importlib.util.spec_from_file_location(module_name, path)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"cannot import hash-pinned dependency: {path}")
    module = importlib.util.module_from_spec(spec)
    sys.modules[module_name] = module
    spec.loader.exec_module(module)
    return module


def _validate_existing_log(log_path: Path) -> Optional[str]:
    previous: Optional[str] = None
    if not log_path.exists():
        return previous
    for number, line in enumerate(log_path.read_text(encoding="utf-8").splitlines(), start=1):
        event = json.loads(line)
        claimed = event.pop("event_sha256", None)
        if event.get("previous_event_sha256") != previous:
            raise RuntimeError(f"log chain broken at line {number}")
        actual = _sha256_bytes(_canonical_bytes(event))
        if claimed != actual:
            raise RuntimeError(f"log hash mismatch at line {number}")
        previous = claimed
    return previous


def _append_event(log_path: Path, event: dict) -> dict:
    event = dict(event)
    event["previous_event_sha256"] = _validate_existing_log(log_path)
    event["event_sha256"] = _sha256_bytes(_canonical_bytes(event))
    with log_path.open("a", encoding="utf-8") as handle:
        handle.write(json.dumps(event, sort_keys=True, separators=(",", ":")) + "\n")
        handle.flush()
    return event


def _atomic_json(path: Path, value: object) -> None:
    temporary = path.with_suffix(path.suffix + ".tmp")
    temporary.write_text(json.dumps(value, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    temporary.replace(path)


# ---------------------------------------------------------------------------
# Synthetic inputs. Everything this adapter consumes must be marked synthetic.
# ---------------------------------------------------------------------------

class SyntheticCutTarget:
    """Explicitly synthetic cut target accepted by the build-only pipeline."""

    def __init__(self, object_key: str, ra_deg: float, dec_deg: float) -> None:
        if re.fullmatch(r"SYNTH-[A-Z0-9][A-Z0-9_-]{0,63}", object_key) is None:
            raise ValueError("BUILD_ONLY_STOP: invalid synthetic object_key")
        if not math.isfinite(ra_deg) or not 0.0 <= ra_deg < 360.0:
            raise ValueError("synthetic ra_deg must be finite and in [0, 360)")
        if not math.isfinite(dec_deg) or not -90.0 <= dec_deg <= 90.0:
            raise ValueError("synthetic dec_deg must be finite and in [-90, 90]")
        self.object_key = object_key
        self.ra_deg = float(ra_deg)
        self.dec_deg = float(dec_deg)


def brickname_for(ra_deg: float, dec_deg: float) -> str:
    hemi = "p" if dec_deg >= 0 else "m"
    return f"{int(round(ra_deg * 10)) % 3600:04d}{hemi}{int(round(abs(dec_deg) * 10)):03d}"


class SyntheticBrickGeometry:
    """Synthetic stand-in for the DR10 South survey-bricks geometry sidecar."""

    def __init__(self, rows: Iterable[Mapping[str, object]], *, scope: str) -> None:
        if scope != SCOPE:
            raise ValueError("BUILD_ONLY_STOP: geometry table must declare SYNTHETIC_ONLY_BUILD scope")
        self.rows: list[dict] = []
        seen: set[str] = set()
        for row in rows:
            record = {
                "brickname": str(row["brickname"]),
                "brickid": int(row["brickid"]),  # type: ignore[arg-type]
                "ra": float(row["ra"]),  # type: ignore[arg-type]
                "dec": float(row["dec"]),  # type: ignore[arg-type]
                "ra1": float(row["ra1"]),  # type: ignore[arg-type]
                "ra2": float(row["ra2"]),  # type: ignore[arg-type]
                "dec1": float(row["dec1"]),  # type: ignore[arg-type]
                "dec2": float(row["dec2"]),  # type: ignore[arg-type]
            }
            if record["brickname"] in seen:
                raise ValueError(f"duplicate synthetic brickname {record['brickname']}")
            seen.add(record["brickname"])
            self.rows.append(record)
        self.sidecar_sha256 = _sha256_bytes(_canonical_bytes(self.rows))

    def row(self, brickname: str) -> dict:
        for record in self.rows:
            if record["brickname"] == brickname:
                return record
        raise KeyError(brickname)


def _ra_delta_deg(ra_a: float, ra_b: float) -> float:
    delta = (ra_a - ra_b) % 360.0
    if delta > 180.0:
        delta -= 360.0
    return delta


def _unique_area_contains(row: Mapping[str, float], ra: float, dec: float) -> bool:
    if not row["dec1"] <= dec < row["dec2"]:
        return False
    span = (row["ra2"] - row["ra1"]) % 360.0
    offset = (ra - row["ra1"]) % 360.0
    return offset < span or span == 0.0


def _interval_relation(
    a1: float, a2: float, b1: float, b2: float, *, wrap: bool,
    eps: float = REASON_CLASSIFICATION_TOLERANCE_DEG,
) -> str:
    """Classify two intervals as overlap, touch, or disjoint (metadata only)."""
    if wrap:
        a2 = a1 + ((a2 - a1) % 360.0)
        original_b1 = b1
        b1 = a1 + _ra_delta_deg(b1, a1)
        b2 = b1 + ((b2 - original_b1) % 360.0)
    low = max(a1, b1)
    high = min(a2, b2)
    if high - low > eps:
        return "overlap"
    if abs(high - low) <= eps:
        return "touch"
    return "disjoint"


# ---------------------------------------------------------------------------
# FITS cards and headers (pure stdlib; header custody happens on raw cards).
# ---------------------------------------------------------------------------

def fits_card(key: str, value: object = None) -> bytes:
    if value is None:
        text = key
    else:
        if isinstance(value, bool):
            rendered = "T" if value else "F"
        elif isinstance(value, str):
            rendered = "'" + value + "'"
        elif isinstance(value, float):
            rendered = repr(value)
        else:
            rendered = str(value)
        text = f"{key:<8}= {rendered:>20}"
    if len(text) > 80:
        raise ValueError(f"FITS card too long: {key}")
    return text.ljust(80).encode("ascii")


def _fits_value(text: str):
    value = text.split("/", 1)[0].strip()
    if value.startswith("'") and value.endswith("'"):
        return value[1:-1].replace("''", "'").strip()
    if value == "T":
        return True
    if value == "F":
        return False
    try:
        if any(marker in value.upper() for marker in (".", "E", "D")):
            return float(value.upper().replace("D", "E"))
        return int(value)
    except ValueError:
        return value


def parse_fits_header(payload: bytes, *, offset: int = 0):
    """Parse one FITS header as raw cards, before any WCS object exists.

    Returns (cards, ordered value-card keys, data offset, canonical header
    SHA-256). Raises FitsIntegrityError on structural damage.
    """
    if len(payload) - offset < 2880:
        raise FitsIntegrityError("FITS header shorter than one 2880-byte block")
    cards: dict = {}
    ordered_keys: list[str] = []
    end_offset = None
    position = offset
    while position < len(payload):
        card_bytes = payload[position : position + 80]
        if len(card_bytes) != 80:
            raise FitsIntegrityError("truncated FITS card")
        try:
            card = card_bytes.decode("ascii")
        except UnicodeDecodeError as exc:
            raise FitsIntegrityError("non-ASCII FITS header") from exc
        key = card[:8].strip().upper()
        if key == "END":
            end_offset = position + 80
            break
        if card[8:10] == "= " and key:
            ordered_keys.append(key)
            cards[key] = _fits_value(card[10:])
        position += 80
    if end_offset is None:
        raise FitsIntegrityError("missing FITS END card")
    header_end = ((end_offset - offset + 2879) // 2880) * 2880 + offset
    header_sha256 = _sha256_bytes(payload[offset:header_end])
    return cards, ordered_keys, header_end, header_sha256


# ---------------------------------------------------------------------------
# PC-4: fail-closed header gate, pinned core plus reviewed successor checks.
# Runs on raw cards BEFORE any TAN transform object is constructed, for every
# source header and again for every synthesized output header.
# ---------------------------------------------------------------------------

_ALTERNATE_WCS_PATTERN = re.compile(
    r"^(?:WCSAXES|WCSNAME|C(?:TYPE|UNIT|RVAL|RPIX|DELT|ROTA)\d|(?:CD|PC)\d_\d|PV\d_\d|LONPOLE|LATPOLE)[A-Z]$"
)
_LOOKUP_DISTORTION_PATTERN = re.compile(r"^D[PQ]\d")


def fail_closed_header_gate(cards: Mapping[str, object], ordered_keys: Iterable[str], *, context: str) -> dict:
    """Reject any header that is not a clean, complete, parity-correct TAN.

    The pinned fail_closed_wcs policy is the core; the successor checks below
    extend it exactly as route binding section 9.1 requires. Raises
    WcsRejectedError; returns the gate receipt on pass.
    """
    keys = [str(key).upper() for key in ordered_keys]
    duplicates = sorted({key for key in keys if keys.count(key) > 1})
    if duplicates:
        raise WcsRejectedError(
            f"{context}: duplicated header keywords {duplicates}",
            code="REJECTED_DUPLICATE_KEY",
            detail={"keywords": duplicates},
        )
    normalized = {str(key).upper(): value for key, value in cards.items()}

    alternates = sorted(key for key in normalized if _ALTERNATE_WCS_PATTERN.match(key))
    if alternates:
        raise WcsRejectedError(
            f"{context}: alternate WCS version keywords {alternates}",
            code="REJECTED_ALTERNATE_WCS",
            detail={"keywords": alternates},
        )
    lookup_keys = sorted(key for key in normalized if _LOOKUP_DISTORTION_PATTERN.match(key))
    if lookup_keys:
        raise WcsRejectedError(
            f"{context}: record-valued lookup distortion keywords {lookup_keys}",
            code="REJECTED_LOOKUP_DISTORTION",
            detail={"keywords": lookup_keys},
        )

    ctype1 = str(normalized.get("CTYPE1", ""))
    ctype2 = str(normalized.get("CTYPE2", ""))
    if ctype1.startswith("DEC") and ctype2.startswith("RA"):
        raise WcsRejectedError(f"{context}: swapped celestial axes", code="REJECTED_SWAPPED_AXES")

    distortion = _load_hash_pinned_module(
        DISTORTION_VALIDATOR_PATH, DISTORTION_VALIDATOR_SHA256, "nm_hash_pinned_fail_closed_wcs"
    )
    audit = distortion.audit_header(normalized)
    if audit["status"] == "FAIL_DISTORTION":
        raise WcsRejectedError(
            f"{context}: distortion-bearing WCS {audit['distortion_families']}",
            code="REJECTED_DISTORTION",
            detail={
                "families": audit["distortion_families"],
                "keywords": audit["distortion_keywords"],
            },
        )
    if audit["status"] == "FAIL_NON_CELESTIAL":
        raise WcsRejectedError(f"{context}: non-celestial axes", code="REJECTED_NON_CELESTIAL")
    if audit["status"] == "FAIL_INCOMPLETE_LINEAR_WCS":
        raise WcsRejectedError(f"{context}: incomplete linear WCS", code="REJECTED_LINEAR_WCS")
    if audit["status"] == "FAIL_SINGULAR":
        raise WcsRejectedError(f"{context}: singular linear WCS", code="REJECTED_SINGULAR_WCS")
    if audit["status"] != "PASS":
        raise WcsRejectedError(f"{context}: pinned audit status {audit['status']}", code="REJECTED_LINEAR_WCS")

    if ctype1 != "RA---TAN" or ctype2 != "DEC--TAN":
        raise WcsRejectedError(
            f"{context}: CTYPE is not exactly RA---TAN/DEC--TAN", code="REJECTED_NON_TAN"
        )

    has_cd = any(key in normalized for key in ("CD1_1", "CD1_2", "CD2_1", "CD2_2"))
    has_pc = any(
        key in normalized for key in ("PC1_1", "PC1_2", "PC2_1", "PC2_2", "CDELT1", "CDELT2")
    )
    if has_cd and has_pc:
        raise WcsRejectedError(
            f"{context}: mixed CD and PC/CDELT encodings with no reviewed equivalence rule",
            code="REJECTED_AMBIGUOUS_WCS",
        )

    required = ("CRVAL1", "CRVAL2", "CRPIX1", "CRPIX2")
    numeric_keys = [key for key in normalized if re.match(r"^(CRVAL|CRPIX|CDELT)\d$|^(CD|PC)\d_\d$", key)]
    for key in required:
        if key not in normalized:
            raise WcsRejectedError(f"{context}: missing {key}", code="REJECTED_INCOMPLETE_WCS")
    for key in sorted(set(numeric_keys) | set(required)):
        try:
            value = float(normalized[key])  # type: ignore[arg-type]
        except (TypeError, ValueError):
            raise WcsRejectedError(f"{context}: non-numeric {key}", code="REJECTED_NONFINITE_WCS")
        if not math.isfinite(value):
            raise WcsRejectedError(f"{context}: nonfinite {key}", code="REJECTED_NONFINITE_WCS")

    if has_cd:
        matrix = [
            [float(normalized["CD1_1"]), float(normalized["CD1_2"])],
            [float(normalized["CD2_1"]), float(normalized["CD2_2"])],
        ]
    else:
        matrix = [
            [
                float(normalized["PC1_1"]) * float(normalized["CDELT1"]),
                float(normalized["PC1_2"]) * float(normalized["CDELT1"]),
            ],
            [
                float(normalized["PC2_1"]) * float(normalized["CDELT2"]),
                float(normalized["PC2_2"]) * float(normalized["CDELT2"]),
            ],
        ]

    parity = _load_hash_pinned_module(
        PARITY_VALIDATOR_PATH, PARITY_VALIDATOR_SHA256, "nm_hash_pinned_yui_parity"
    )
    template = parity.build_parity_receipt()
    template_checks = parity.parity_predicates(template)
    if not all(template_checks.values()):
        raise RuntimeError("pinned parity template failed its own predicates")
    row_transform = [list(row) for row in template["row_order_transform_matrix"]]
    combined = parity.multiply_2x2(matrix, row_transform)
    combined_det = parity.determinant_2x2(combined)
    tolerance = 1e-12
    east_left = matrix[0][0] < 0 and abs(matrix[0][1]) <= tolerance
    north_up = matrix[1][1] > 0 and abs(matrix[1][0]) <= tolerance
    if combined_det >= 0 or not east_left or not north_up:
        raise WcsRejectedError(
            f"{context}: WCS parity is not North-up/East-left", code="REJECTED_PARITY"
        )

    return {
        "context": context,
        "pinned_distortion_audit": audit,
        "pinned_distortion_validator_sha256": DISTORTION_VALIDATOR_SHA256,
        "pinned_parity_validator_sha256": PARITY_VALIDATOR_SHA256,
        "pinned_parity_template_checks": template_checks,
        "linear_matrix": matrix,
        "linear_determinant": parity.determinant_2x2(matrix),
        "combined_pixel_to_sky_determinant": combined_det,
        "east_left": east_left,
        "north_up": north_up,
        # The pinned parity validator is a position-free template; the
        # position-dependent PC-3 checks are performed by pc3_output_receipt.
        "parity_validator_scope": "position-free template predicates plus header-derived matrix parity",
    }


# ---------------------------------------------------------------------------
# TAN WCS math (pure stdlib, double precision).
# ---------------------------------------------------------------------------

class TanWcs:
    def __init__(self, crval1: float, crval2: float, crpix1: float, crpix2: float, cd) -> None:
        self.crval1 = float(crval1)
        self.crval2 = float(crval2)
        self.crpix1 = float(crpix1)
        self.crpix2 = float(crpix2)
        self.cd = [[float(cd[0][0]), float(cd[0][1])], [float(cd[1][0]), float(cd[1][1])]]
        det = self.cd[0][0] * self.cd[1][1] - self.cd[0][1] * self.cd[1][0]
        if not math.isfinite(det) or det == 0.0:
            raise WcsRejectedError("singular CD matrix", code="REJECTED_SINGULAR_WCS")
        self.cd_det = det
        self.inv_cd = [
            [self.cd[1][1] / det, -self.cd[0][1] / det],
            [-self.cd[1][0] / det, self.cd[0][0] / det],
        ]

    def pixel_to_sky(self, x: float, y: float):
        u = self.cd[0][0] * (x - self.crpix1) + self.cd[0][1] * (y - self.crpix2)
        v = self.cd[1][0] * (x - self.crpix1) + self.cd[1][1] * (y - self.crpix2)
        xi = math.radians(u)
        eta = math.radians(v)
        ra0 = math.radians(self.crval1)
        dec0 = math.radians(self.crval2)
        denominator = math.cos(dec0) - eta * math.sin(dec0)
        ra = ra0 + math.atan2(xi, denominator)
        dec = math.atan2(
            math.sin(dec0) + eta * math.cos(dec0), math.hypot(xi, denominator)
        )
        return math.degrees(ra) % 360.0, math.degrees(dec)

    def sky_to_pixel(self, ra_deg: float, dec_deg: float):
        xi, eta = tangent_plane_offsets(self.crval1, self.crval2, ra_deg, dec_deg)
        x = self.crpix1 + self.inv_cd[0][0] * xi + self.inv_cd[0][1] * eta
        y = self.crpix2 + self.inv_cd[1][0] * xi + self.inv_cd[1][1] * eta
        return x, y


def tangent_plane_offsets(ra0_deg: float, dec0_deg: float, ra_deg: float, dec_deg: float):
    """Gnomonic (xi, eta) offsets in degrees of (ra, dec) about (ra0, dec0)."""
    ra0 = math.radians(ra0_deg)
    dec0 = math.radians(dec0_deg)
    ra = math.radians(ra_deg)
    dec = math.radians(dec_deg)
    cos_c = math.sin(dec0) * math.sin(dec) + math.cos(dec0) * math.cos(dec) * math.cos(ra - ra0)
    if cos_c <= 1e-9:
        raise ValueError("position is not on the visible tangent hemisphere")
    xi = math.cos(dec) * math.sin(ra - ra0) / cos_c
    eta = (math.sin(dec) * math.cos(dec0) - math.cos(dec) * math.sin(dec0) * math.cos(ra - ra0)) / cos_c
    return math.degrees(xi), math.degrees(eta)


def angular_separation_deg(ra1: float, dec1: float, ra2: float, dec2: float) -> float:
    phi1 = math.radians(dec1)
    phi2 = math.radians(dec2)
    delta = math.radians(_ra_delta_deg(ra1, ra2))
    a = math.sin((phi2 - phi1) / 2.0) ** 2 + math.cos(phi1) * math.cos(phi2) * math.sin(delta / 2.0) ** 2
    return math.degrees(2.0 * math.asin(min(1.0, math.sqrt(a))))


def nine_point_boundary(n_pixels: int):
    """Pinned nine-point pixel-edge boundary: corners, edge midpoints, closed."""
    low, mid, high = 0.5, n_pixels / 2.0 + 0.5, n_pixels + 0.5
    return [
        (low, low), (mid, low), (high, low), (high, mid),
        (high, high), (mid, high), (low, high), (low, mid), (low, low),
    ]


# Positive-area threshold for source inclusion, in squared source pixels.
# Matches the fixture-oracle planning contract; a source at exact zero-area
# tangency contributes zero pixels and is excluded.
INTERSECTION_AREA_THRESHOLD_SOURCE_PIX2 = 1e-8


def _clip_polygon_halfplane(points, axis: int, bound: float, keep_greater: bool):
    """Sutherland-Hodgman clip of a polygon against one axis-aligned halfplane."""
    if not points:
        return points
    output = []
    previous = points[-1]
    previous_inside = (previous[axis] >= bound) if keep_greater else (previous[axis] <= bound)
    for current in points:
        current_inside = (current[axis] >= bound) if keep_greater else (current[axis] <= bound)
        if current_inside != previous_inside:
            denominator = current[axis] - previous[axis]
            if denominator != 0.0:
                fraction = (bound - previous[axis]) / denominator
                intersection = [
                    previous[0] + fraction * (current[0] - previous[0]),
                    previous[1] + fraction * (current[1] - previous[1]),
                ]
                intersection[axis] = bound
                output.append(tuple(intersection))
        if current_inside:
            output.append(current)
        previous = current
        previous_inside = current_inside
    return output


def output_overlap_area_in_source_pixels(output_wcs: TanWcs, source_wcs: TanWcs) -> float:
    """Clipped area (source px^2) of the output nine-point boundary inside a source image.

    The route section 6.2 nine-point rule, evaluated in the candidate source's
    pixel plane: the output boundary polygon (which subtends only ~33 arcsec
    and therefore projects near-rigidly into any nearby TAN frame at any
    declination) is clipped against the source's exact pixel-edge box, whose
    own nine-point boundary it is. Projecting in this direction is what keeps
    knife-edge decisions valid near the poles, where the reverse projection of
    a 3600-pixel source square is curvature-limited (the round-3
    dec -89.875 exact-tangency defect, 2026-08-16).
    """
    points = []
    for x, y in nine_point_boundary(OUT_N)[:-1]:
        ra, dec = output_wcs.pixel_to_sky(x, y)
        points.append(source_wcs.sky_to_pixel(ra, dec))
    for axis, bound, keep_greater in (
        (0, 0.5, True),
        (0, SRC_N + 0.5, False),
        (1, 0.5, True),
        (1, SRC_N + 0.5, False),
    ):
        points = _clip_polygon_halfplane(points, axis, bound, keep_greater)
        if len(points) < 3:
            return 0.0
    area = 0.0
    for index in range(len(points)):
        x1, y1 = points[index]
        x2, y2 = points[(index + 1) % len(points)]
        area += x1 * y2 - x2 * y1
    return abs(area) / 2.0


# ---------------------------------------------------------------------------
# Output WCS (route binding section 7.2, exact constants).
# ---------------------------------------------------------------------------

def build_output_wcs(ra_deg: float, dec_deg: float) -> TanWcs:
    return TanWcs(ra_deg, dec_deg, OUT_CRPIX, OUT_CRPIX, OUT_CD)


def output_header_bytes(item: SyntheticCutTarget) -> bytes:
    cards = [
        fits_card("SIMPLE", True),
        fits_card("BITPIX", -32),
        fits_card("NAXIS", 2),
        fits_card("NAXIS1", OUT_N),
        fits_card("NAXIS2", OUT_N),
        fits_card("CTYPE1", "RA---TAN"),
        fits_card("CTYPE2", "DEC--TAN"),
        fits_card("CRVAL1", item.ra_deg),
        fits_card("CRVAL2", item.dec_deg),
        fits_card("CRPIX1", OUT_CRPIX),
        fits_card("CRPIX2", OUT_CRPIX),
        fits_card("CD1_1", OUT_CD[0][0]),
        fits_card("CD1_2", OUT_CD[0][1]),
        fits_card("CD2_1", OUT_CD[1][0]),
        fits_card("CD2_2", OUT_CD[1][1]),
        fits_card("BUNIT", "nanomaggy"),
        fits_card("NMSCOPE", SCOPE),
        fits_card("OBJKEY", item.object_key),
        b"END".ljust(80),
    ]
    header = b"".join(cards)
    return header + b" " * ((-len(header)) % 2880)


# ---------------------------------------------------------------------------
# Planning: brick mapping and the margin rule (route binding section 6.2).
# ---------------------------------------------------------------------------

def _source_wcs_for_row(row: Mapping[str, float]) -> TanWcs:
    return TanWcs(row["ra"], row["dec"], SRC_CRPIX, SRC_CRPIX, OUT_CD)


def plan_object(item: SyntheticCutTarget, geometry: SyntheticBrickGeometry) -> dict:
    """Derive the source working set by polygon intersection alone.

    The polygon-intersection rule (route binding section 6.2) is the only
    selection rule. The catalogue/rectangular "primary" is grouping metadata:
    a rectangular unique-area containment test is a projection of the true
    brick geometry, is not seam-free away from the tangent point, and MUST NOT
    gate planning (2026-08-16 corner-fixture repair, Kun condition 1). The
    grouping primary is instead the planned brick whose centre is nearest the
    object by angular separation, with exact ties broken by lexicographic
    brickname; rectangular containment is recorded as metadata only. Planning
    is terminal only when no source image intersects the output footprint.

    Inclusion rule (2026-08-16 round-3 repair): a candidate is planned iff the
    output nine-point boundary polygon, projected into that candidate's own
    TAN pixel plane, has clipped intersection area with the source pixel box
    greater than INTERSECTION_AREA_THRESHOLD_SOURCE_PIX2. Exact zero-area
    tangency is excluded — such a source contributes zero pixels.
    """
    if type(item) is not SyntheticCutTarget:
        raise TypeError("BUILD_ONLY_STOP: only SyntheticCutTarget input is accepted")
    output_wcs = build_output_wcs(item.ra_deg, item.dec_deg)

    candidates: list[str] = []
    planned_rows: list = []
    separations: dict = {}
    overlap_areas: dict = {}
    for row in geometry.rows:
        separation = angular_separation_deg(item.ra_deg, item.dec_deg, row["ra"], row["dec"])
        if separation > CANDIDATE_PREFILTER_DEG:
            continue
        candidates.append(row["brickname"])
        separations[row["brickname"]] = separation
        area = output_overlap_area_in_source_pixels(output_wcs, _source_wcs_for_row(row))
        if area > INTERSECTION_AREA_THRESHOLD_SOURCE_PIX2:
            planned_rows.append(row)
            overlap_areas[row["brickname"]] = area
    if not planned_rows:
        raise ObjectTerminalError(
            "no source image intersects the output footprint",
            code="FAILED_PLAN_NO_SOURCES",
            detail={"candidates": sorted(candidates)},
        )

    primary = min(
        planned_rows, key=lambda row: (separations[row["brickname"]], row["brickname"])
    )
    unique_area_primaries = sorted(
        row["brickname"] for row in geometry.rows
        if _unique_area_contains(row, item.ra_deg, item.dec_deg)
    )

    planned: list = []
    reasons: dict = {}
    crosses: dict = {}
    for row in planned_rows:
        planned.append(row["brickname"])
        if row["brickname"] == primary["brickname"]:
            reasons[row["brickname"]] = "primary"
            crosses[row["brickname"]] = False
            continue
        ra_rel = _interval_relation(primary["ra1"], primary["ra2"], row["ra1"], row["ra2"], wrap=True)
        dec_rel = _interval_relation(primary["dec1"], primary["dec2"], row["dec1"], row["dec2"], wrap=False)
        if ra_rel != "overlap" and dec_rel != "overlap":
            reasons[row["brickname"]] = "corner_neighbour"
        else:
            reasons[row["brickname"]] = "edge_neighbour"
        crosses[row["brickname"]] = any(
            _unique_area_contains(row, *output_wcs.pixel_to_sky(x, y))
            for x, y in nine_point_boundary(OUT_N)[:-1]
        )
    planned.sort()
    candidates.sort()
    return {
        "object_key": item.object_key,
        "ra_deg": item.ra_deg,
        "dec_deg": item.dec_deg,
        "primary_brickname": primary["brickname"],
        "primary_rule": (
            "grouping metadata only: nearest planned brick centre by angular separation, "
            "exact ties lexicographic; never a source-selection precondition"
        ),
        "unique_area_primary_bricknames": unique_area_primaries,
        "candidate_bricknames": candidates,
        "planned_bricknames": planned,
        "planned_overlap_area_source_pix2": overlap_areas,
        "intersection_area_threshold_source_pix2": INTERSECTION_AREA_THRESHOLD_SOURCE_PIX2,
        "reasons": reasons,
        "output_crosses_unique_boundary": crosses,
        "working_set_signature": _sha256_bytes(_canonical_bytes(planned)),
    }


# ---------------------------------------------------------------------------
# Sealed dry-run transfer manifest (route binding section 5.1). Constructed
# and logged only; there is no code path that can issue it.
# ---------------------------------------------------------------------------

def staged_relpath_for(brickname: str) -> str:
    return f"coadd/{brickname[:3]}/{brickname}/legacysurvey-{brickname}-image-r.fits"


def build_transfer_manifest(
    plans: Iterable[Mapping[str, object]],
    geometry: SyntheticBrickGeometry,
    source_root: Path,
) -> dict:
    source_root = Path(source_root)
    required: dict = {}
    for plan in plans:
        for brickname in plan["planned_bricknames"]:  # type: ignore[union-attr]
            entry = required.setdefault(str(brickname), {"objects": set(), "reasons": set()})
            entry["objects"].add(str(plan["object_key"]))
            entry["reasons"].add(str(plan["reasons"][brickname]))  # type: ignore[index]
    records = []
    total_bytes = 0
    for brickname in sorted(required):
        staged = source_root / staged_relpath_for(brickname)
        if staged.is_symlink() or not staged.is_file():
            raise ManifestError(
                f"required source file missing at manifest time: {staged} (terminal, not skippable)"
            )
        stat = staged.stat()
        reasons = required[brickname]["reasons"]
        reason = "primary" if "primary" in reasons else (
            "edge_neighbour" if "edge_neighbour" in reasons else "corner_neighbour"
        )
        object_keys = sorted(required[brickname]["objects"])
        if len(object_keys) > MANIFEST_OBJECT_LIST_HASH_THRESHOLD:
            object_binding = {"required_by_object_keys_sha256": _sha256_bytes(_canonical_bytes(object_keys))}
        else:
            object_binding = {"required_by_object_keys": object_keys}
        record = {
            "release": MANIFEST_RELEASE,
            "source_collection_uuid": SOURCE_COLLECTION_UUID,
            "source_path": CFS_IMAGE_TEMPLATE.format(aaa=brickname[:3], brickname=brickname),
            "destination_relpath": staged_relpath_for(brickname),
            "brickname": brickname,
            "aaa": brickname[:3],
            "product": "image-r",
            "reason": reason,
            "source_bytes": stat.st_size,
            "source_mtime_utc": datetime.fromtimestamp(stat.st_mtime, timezone.utc)
            .isoformat(timespec="seconds")
            .replace("+00:00", "Z"),
            "source_sha256": _sha256_file(staged),
            "synthetic_stand_in": True,
        }
        record.update(object_binding)
        records.append(record)
        total_bytes += stat.st_size
    records.append(
        {
            "release": MANIFEST_RELEASE,
            "source_collection_uuid": SOURCE_COLLECTION_UUID,
            "source_path": GEOMETRY_SIDECAR_CFS_PATH,
            "destination_relpath": "survey-bricks-dr10-south.synthetic.json",
            "brickname": None,
            "aaa": None,
            "product": "geometry_sidecar",
            "reason": "geometry_sidecar",
            "source_bytes": None,
            "source_mtime_utc": None,
            "source_sha256": geometry.sidecar_sha256,
            "synthetic_stand_in": True,
        }
    )
    body = {
        "scope": SCOPE,
        "manifest_format_version": MANIFEST_FORMAT_VERSION,
        "created_utc": _utc_now(),
        "records": records,
        "file_count": len(records),
        "total_source_bytes": total_bytes,
    }
    manifest_sha256 = _sha256_bytes(_canonical_bytes({k: v for k, v in body.items() if k != "created_utc"}))
    body["manifest_sha256"] = manifest_sha256
    body["globus_task_template"] = {
        "submitted": False,
        "submission_capability_exists": False,
        "submission_forbidden_reason": "BUILD_ONLY_STOP: no transport exists in this module",
        "source_collection_uuid": SOURCE_COLLECTION_UUID,
        "destination_collection_uuid": "SYNTHETIC-LOCAL-BUILD-ONLY",
        "label": f"nm-longo-bricks-{manifest_sha256[:12]}",
        "verify_checksum": True,
        "sync_level": "checksum",
        "skip_source_errors": False,
    }
    return body


# ---------------------------------------------------------------------------
# Synthetic staged source files: custody, gate, and pixel access.
# ---------------------------------------------------------------------------

class SyntheticBrickSource:
    """One digest-verified, gate-passed synthetic staged brick image."""

    def __init__(self, path: Path, row: Mapping[str, float], expected_sha256: str) -> None:
        path = Path(path)
        if path.is_symlink() or not path.is_file():
            raise ObjectTerminalError(
                f"planned source missing or not a regular file: {path}",
                code="FAILED_SOURCE_MISSING",
            )
        actual_sha256 = _sha256_file(path)
        if actual_sha256 != expected_sha256:
            raise ObjectTerminalError(
                f"planned source digest mismatch: {path}",
                code="FAILED_SOURCE_DIGEST",
                detail={"expected": expected_sha256, "actual": actual_sha256},
            )
        with path.open("rb") as handle:
            payload_head = handle.read(2880 * 8)
        cards, ordered_keys, data_offset, header_sha256 = parse_fits_header(payload_head)
        # PC-4 pre-parse gate: raw cards are audited before a TAN object exists.
        self.gate_receipt = fail_closed_header_gate(cards, ordered_keys, context=f"source:{path.name}")
        if cards.get("SIMPLE") is not True or cards.get("BITPIX") != -32:
            raise FitsIntegrityError("source must be SIMPLE float32 FITS")
        if cards.get("NAXIS") != 2 or cards.get("NAXIS1") != SRC_N or cards.get("NAXIS2") != SRC_N:
            raise FitsIntegrityError(f"source shape must be {SRC_N}x{SRC_N}")
        data_bytes = SRC_N * SRC_N * 4
        expected_total = data_offset + ((data_bytes + 2879) // 2880) * 2880
        if path.stat().st_size != expected_total:
            raise FitsIntegrityError(
                f"source FITS length mismatch expected={expected_total} actual={path.stat().st_size}"
            )
        for key, expected in (
            ("CRVAL1", row["ra"]), ("CRVAL2", row["dec"]),
            ("CRPIX1", SRC_CRPIX), ("CRPIX2", SRC_CRPIX),
            ("CD1_1", OUT_CD[0][0]), ("CD1_2", OUT_CD[0][1]),
            ("CD2_1", OUT_CD[1][0]), ("CD2_2", OUT_CD[1][1]),
        ):
            if abs(float(cards[key]) - float(expected)) > 1e-12:
                raise WcsRejectedError(
                    f"source header {key} disagrees with geometry sidecar",
                    code="REJECTED_GEOMETRY_MISMATCH",
                )
        self.path = path
        self.sha256 = actual_sha256
        self.header_sha256 = header_sha256
        self.cards = cards
        self.data_offset = data_offset
        self.wcs = TanWcs(cards["CRVAL1"], cards["CRVAL2"], cards["CRPIX1"], cards["CRPIX2"],
                          [[cards["CD1_1"], cards["CD1_2"]], [cards["CD2_1"], cards["CD2_2"]]])
        self._handle = path.open("rb")

    def pixel(self, ix: int, iy: int) -> float:
        offset = self.data_offset + ((iy - 1) * SRC_N + (ix - 1)) * 4
        self._handle.seek(offset)
        return struct.unpack(">f", self._handle.read(4))[0]

    def close(self) -> None:
        self._handle.close()


# ---------------------------------------------------------------------------
# PC-3: per-output receipt on the staged output bytes as written.
# ---------------------------------------------------------------------------

def pc3_output_receipt(item: SyntheticCutTarget, staged_bytes: bytes, coverage: list, sets: dict) -> dict:
    cards, ordered_keys, data_offset, header_sha256 = parse_fits_header(staged_bytes)
    gate = fail_closed_header_gate(cards, ordered_keys, context=f"output:{item.object_key}")

    expected_cards = {
        "NAXIS": 2, "NAXIS1": OUT_N, "NAXIS2": OUT_N, "BITPIX": -32,
        "CTYPE1": "RA---TAN", "CTYPE2": "DEC--TAN",
        "CRVAL1": item.ra_deg, "CRVAL2": item.dec_deg,
        "CRPIX1": OUT_CRPIX, "CRPIX2": OUT_CRPIX,
        "CD1_1": OUT_CD[0][0], "CD1_2": OUT_CD[0][1],
        "CD2_1": OUT_CD[1][0], "CD2_2": OUT_CD[1][1],
    }
    for key, expected in expected_cards.items():
        actual = cards.get(key)
        if isinstance(expected, float):
            if not isinstance(actual, (int, float)) or float(actual) != expected:
                raise WcsRejectedError(
                    f"output header {key}={actual!r} is not the exact frozen constant {expected!r}",
                    code="FAILED_OUTPUT_ACCEPTANCE",
                )
        elif actual != expected:
            raise WcsRejectedError(
                f"output header {key}={actual!r} is not the exact frozen value {expected!r}",
                code="FAILED_OUTPUT_ACCEPTANCE",
            )

    wcs = TanWcs(cards["CRVAL1"], cards["CRVAL2"], cards["CRPIX1"], cards["CRPIX2"],
                 [[cards["CD1_1"], cards["CD1_2"]], [cards["CD2_1"], cards["CD2_2"]]])
    if not (math.isfinite(wcs.cd_det) and wcs.cd_det < 0.0):
        raise WcsRejectedError("output CD determinant not finite-negative", code="FAILED_OUTPUT_ACCEPTANCE")
    if wcs.cd_det != OUT_CD_DET:
        raise WcsRejectedError("output CD determinant drifted from frozen product", code="FAILED_OUTPUT_ACCEPTANCE")

    centre_x, centre_y = wcs.sky_to_pixel(item.ra_deg, item.dec_deg)
    centre_residual = max(abs(centre_x - OUT_CRPIX), abs(centre_y - OUT_CRPIX))
    if centre_residual > ROUND_TRIP_TOLERANCE_PIXELS:
        raise WcsRejectedError("CRVAL does not map to (64.5, 64.5)", code="FAILED_OUTPUT_ACCEPTANCE")

    arcsec = 1.0 / 3600.0
    ra_dx = wcs.sky_to_pixel((item.ra_deg + arcsec) % 360.0, item.dec_deg)[0] - centre_x
    dec_dy = wcs.sky_to_pixel(item.ra_deg, item.dec_deg + arcsec)[1] - centre_y
    if not (ra_dx < 0.0 and dec_dy > 0.0):
        raise WcsRejectedError("perturbation direction test failed", code="FAILED_OUTPUT_ACCEPTANCE")

    probes = [
        (64.5, 64.5), (1.0, 1.0), (1.0, 128.0), (128.0, 1.0), (128.0, 128.0),
        (0.5, 0.5), (0.5, 128.5), (128.5, 0.5), (128.5, 128.5),
    ]
    max_residual = 0.0
    for x, y in probes:
        ra, dec = wcs.pixel_to_sky(x, y)
        back_x, back_y = wcs.sky_to_pixel(ra, dec)
        max_residual = max(max_residual, abs(back_x - x), abs(back_y - y))
    if max_residual > ROUND_TRIP_TOLERANCE_PIXELS:
        raise WcsRejectedError(
            f"round-trip residual {max_residual} exceeds 1e-6 pixel", code="FAILED_OUTPUT_ACCEPTANCE"
        )

    coverage_min = min(coverage)
    zero_coverage = sum(1 for value in coverage if value == 0)
    if coverage_min < 1 or zero_coverage != 0:
        raise ObjectTerminalError(
            f"{zero_coverage} output pixels have zero coverage",
            code="FAILED_ZERO_COVERAGE",
        )
    unexplained = sorted(
        (set(sets["planned"]) - set(sets["opened"]))
        | (set(sets["contributing"]) - set(sets["opened"]))
    )
    if unexplained:
        raise ObjectTerminalError(
            f"unexplained planned/opened/contributing difference: {unexplained}",
            code="FAILED_OUTPUT_ACCEPTANCE",
        )

    data_shape_bytes = OUT_N * OUT_N * 4
    data = staged_bytes[data_offset : data_offset + data_shape_bytes]
    if len(data) != data_shape_bytes:
        raise FitsIntegrityError("staged output data truncated")
    return {
        "output_header_sha256": header_sha256,
        "output_data_sha256": _sha256_bytes(data),
        "output_file_sha256": _sha256_bytes(staged_bytes),
        "gate": gate,
        "wcs_constants_exact": True,
        "cd_determinant": wcs.cd_det,
        "cd_determinant_sign": -1,
        "centre_residual_pixels": centre_residual,
        "ra_plus_1arcsec_dx": ra_dx,
        "dec_plus_1arcsec_dy": dec_dy,
        "round_trip_max_residual_pixels": max_residual,
        "coverage_min": coverage_min,
        "coverage_zero_count": zero_coverage,
        "coverage_plane_sha256": _sha256_bytes(struct.pack(f">{len(coverage)}i", *coverage)),
        "planned_sources": sorted(sets["planned"]),
        "opened_sources": sorted(sets["opened"]),
        "contributing_sources": sorted(sets["contributing"]),
        "zero_pixel_touch_sources": sorted(sets["zero_touch"]),
        "parity_validator_note": (
            "pinned validate_wcs_parity is a position-free synthetic template; it supplies the "
            "row-order convention, 2x2 algebra, and predicate set. The position-dependent checks "
            "it cannot perform on synthesized headers (exact frozen constants, CRVAL centre "
            "mapping, perturbation directions, round-trip residuals) are performed here on the "
            "staged output bytes."
        ),
    }


# ---------------------------------------------------------------------------
# Rendering: bilinear resampler matching the fixture-oracle interpolation rule
# (2026-08-16 resampler gate). Equivalence with the hash-pinned Imagine/
# astrometry.net production kernel is bound to Yui's dependency lock, not
# asserted here.
# ---------------------------------------------------------------------------

def render_cutout(item: SyntheticCutTarget, sources: Mapping[str, SyntheticBrickSource]):
    output_wcs = build_output_wcs(item.ra_deg, item.dec_deg)
    values: list = []
    coverage: list = []
    contributed_counts = {name: 0 for name in sources}
    for iy in range(1, OUT_N + 1):
        for ix in range(1, OUT_N + 1):
            ra, dec = output_wcs.pixel_to_sky(float(ix), float(iy))
            total = 0.0
            count = 0
            nonfinite = False
            for name, source in sources.items():
                sx, sy = source.wcs.sky_to_pixel(ra, dec)
                # Contribution/support window: the output pixel CENTRE must
                # lie within the source's interior pixel-centre window [1, N]
                # (bilinear support), matching the fixture oracle. A planned
                # source whose overlap holds no output pixel centre is a
                # legitimate zero-pixel-touch source, never an error and never
                # credited as coverage.
                if 1.0 <= sx <= SRC_N and 1.0 <= sy <= SRC_N:
                    # Bilinear with the oracle's exact index rule: 0-based
                    # fx = sx - 1, x0 = floor(fx), x1 = min(x0 + 1, N - 1).
                    fx = sx - 1.0
                    fy = sy - 1.0
                    x0 = int(math.floor(fx))
                    y0 = int(math.floor(fy))
                    x1 = min(x0 + 1, SRC_N - 1)
                    y1 = min(y0 + 1, SRC_N - 1)
                    wx = fx - x0
                    wy = fy - y0
                    sample = (
                        source.pixel(x0 + 1, y0 + 1) * (1.0 - wx) * (1.0 - wy)
                        + source.pixel(x1 + 1, y0 + 1) * wx * (1.0 - wy)
                        + source.pixel(x0 + 1, y1 + 1) * (1.0 - wx) * wy
                        + source.pixel(x1 + 1, y1 + 1) * wx * wy
                    )
                    contributed_counts[name] += 1
                    count += 1
                    if math.isfinite(sample):
                        total += sample
                    else:
                        nonfinite = True
            coverage.append(count)
            if count == 0:
                values.append(float("nan"))
            elif nonfinite:
                values.append(float("nan"))
            else:
                values.append(total / count)
    return values, coverage, contributed_counts


# ---------------------------------------------------------------------------
# Guarded local-cut pipeline with resumable custody.
# ---------------------------------------------------------------------------

def _summary() -> dict:
    return {
        "scope": SCOPE,
        "planned_objects": 0,
        "completed": 0,
        "failed": 0,
        "skipped": 0,
        "resumed_complete": 0,
        "reprocessed_stale": 0,
        "zero_issuance": {
            "globus_endpoints_activated": 0,
            "globus_tasks_submitted": 0,
            "network_calls": 0,
            "real_survey_files_read": 0,
            "real_cutouts_generated": 0,
        },
    }


def _load_state(path: Path) -> dict:
    if not path.exists():
        return {"scope": SCOPE, "objects": {}}
    if path.is_symlink() or not path.is_file():
        raise RuntimeError("state.json must be a regular file")
    state = json.loads(path.read_text(encoding="utf-8"))
    if state.get("scope") != SCOPE or not isinstance(state.get("objects"), dict):
        raise RuntimeError("state.json scope/schema mismatch")
    return state


def _validate_completed(output_dir: Path, object_key: str, prior: Mapping[str, object]) -> None:
    receipt_path = output_dir / "receipts" / f"{object_key}.json"
    if receipt_path.is_symlink() or not receipt_path.is_file():
        raise RuntimeError("completed receipt missing or not regular")
    receipt = json.loads(receipt_path.read_text(encoding="utf-8"))
    if receipt != prior:
        raise RuntimeError("completed state and receipt differ")
    cutout = output_dir / str(prior["output_path"])
    if cutout.is_symlink() or not cutout.is_file():
        raise RuntimeError("completed output missing or not regular")
    if _sha256_file(cutout) != prior["output_file_sha256"]:
        raise RuntimeError("completed output checksum mismatch")


def run_local_cut(
    objects: Iterable[SyntheticCutTarget],
    geometry: SyntheticBrickGeometry,
    source_root: Path,
    output_dir: Path,
    *,
    invalid_fraction_cap: float,
    manifest_only: bool = False,
    tamper_hook: Optional[Callable[[str, bytes], bytes]] = None,
    interrupt_hook: Optional[Callable[[str, str], None]] = None,
) -> dict:
    """Plan, seal the dry-run manifest, and (unless manifest_only) cut locally.

    invalid_fraction_cap is the IC invalid-pixel-cap BINDING SLOT from the
    frozen V3 contract; it is filled on synthetics only and owned by Yui's
    input-function receipt, not by this adapter.
    """
    if not (isinstance(invalid_fraction_cap, float) and math.isfinite(invalid_fraction_cap)
            and 0.0 <= invalid_fraction_cap < 1.0):
        raise ValueError("invalid_fraction_cap must be a finite float in [0, 1)")
    if type(geometry) is not SyntheticBrickGeometry:
        raise TypeError("BUILD_ONLY_STOP: only SyntheticBrickGeometry is accepted")
    output_dir = Path(output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)
    log_path = output_dir / "cut_log.jsonl"
    summary = _summary()
    code_manifest = {
        "adapter_sha256": _self_sha256(),
        "parity_validator_sha256": PARITY_VALIDATOR_SHA256,
        "distortion_validator_sha256": DISTORTION_VALIDATOR_SHA256,
        "route_binding_sha256": ROUTE_BINDING_SHA256,
        "frozen_prereg_sha256": FROZEN_PREREG_SHA256,
    }

    items = list(objects)
    for item in items:
        if type(item) is not SyntheticCutTarget:
            raise TypeError("BUILD_ONLY_STOP: only SyntheticCutTarget input is accepted")

    plans = {}
    plan_failures = {}
    for item in items:
        try:
            plans[item.object_key] = plan_object(item, geometry)
        except ObjectTerminalError as exc:
            plan_failures[item.object_key] = exc
    summary["planned_objects"] = len(plans)

    manifest = build_transfer_manifest(list(plans.values()), geometry, source_root)
    _atomic_json(output_dir / "transfer_manifest.json", manifest)
    _append_event(
        log_path,
        {
            "recorded_utc": _utc_now(),
            "status": "DRY_RUN_MANIFEST_SEALED_NOT_SUBMITTED",
            "manifest_sha256": manifest["manifest_sha256"],
            "file_count": manifest["file_count"],
            "total_source_bytes": manifest["total_source_bytes"],
            "code_manifest": code_manifest,
        },
    )
    summary["manifest_sha256"] = manifest["manifest_sha256"]
    if manifest_only:
        summary["mode"] = "DRY_RUN_MANIFEST_ONLY"
        for object_key, exc in sorted(plan_failures.items()):
            _append_event(
                log_path,
                {
                    "recorded_utc": _utc_now(),
                    "object_key": object_key,
                    "status": exc.code,
                    "error": str(exc),
                },
            )
            summary["failed"] += 1
        return summary
    summary["mode"] = "SYNTHETIC_LOCAL_CUT"

    digests = {
        record["brickname"]: record["source_sha256"]
        for record in manifest["records"]
        if record["product"] == "image-r"
    }
    state_path = output_dir / "state.json"
    state = _load_state(state_path)
    cutout_dir = output_dir / "cutouts"
    receipt_dir = output_dir / "receipts"
    staging_dir = output_dir / "staging"
    quarantine_dir = output_dir / "quarantine"
    for directory in (cutout_dir, receipt_dir, staging_dir, quarantine_dir):
        directory.mkdir(parents=True, exist_ok=True)

    def _terminal(item: SyntheticCutTarget, exc: Exception, code: str, base_event: dict, staged: Path) -> None:
        if staged.exists():
            staged.replace(quarantine_dir / staged.name)
        receipt = {
            "schema_version": 1,
            "scope": SCOPE,
            "object_key": item.object_key,
            "status": code,
            "error_type": type(exc).__name__,
            "error": str(exc),
            "detail": getattr(exc, "detail", {}),
            "output_path": None,
            "output_file_sha256": None,
            "manifest_sha256": manifest["manifest_sha256"],
            "code_manifest": code_manifest,
        }
        _atomic_json(receipt_dir / f"{item.object_key}.json", receipt)
        state["objects"][item.object_key] = receipt
        summary["failed"] += 1
        _append_event(log_path, {**base_event, "status": code, "error_type": type(exc).__name__})
        _atomic_json(state_path, state)

    ordered = sorted(
        (item for item in items if item.object_key in plans),
        key=lambda item: (plans[item.object_key]["primary_brickname"], item.object_key),
    )
    for item in items:
        if item.object_key in plan_failures:
            exc = plan_failures[item.object_key]
            base_event = {"recorded_utc": _utc_now(), "object_key": item.object_key}
            _terminal(item, exc, exc.code, base_event, staging_dir / f"{item.object_key}.fits.part")

    for item in ordered:
        plan = plans[item.object_key]
        base_event = {
            "recorded_utc": _utc_now(),
            "object_key": item.object_key,
            "primary_brickname": plan["primary_brickname"],
            "working_set_signature": plan["working_set_signature"],
        }
        staged = staging_dir / f"{item.object_key}.fits.part"
        if interrupt_hook is not None:
            interrupt_hook(item.object_key, "before_object")

        prior = state["objects"].get(item.object_key)
        if prior is not None:
            if prior.get("status") == "COMPLETED":
                _validate_completed(output_dir, item.object_key, prior)
                _append_event(log_path, {**base_event, "status": "RESUME_COMPLETE_NOT_RECUT"})
                summary["resumed_complete"] += 1
                continue
            if prior.get("status") in TERMINAL_FAILURE_STATUSES:
                receipt_path = receipt_dir / f"{item.object_key}.json"
                if receipt_path.is_symlink() or not receipt_path.is_file():
                    raise RuntimeError("terminal failure receipt missing or not regular")
                if json.loads(receipt_path.read_text(encoding="utf-8")) != prior:
                    raise RuntimeError("terminal failure state and receipt differ")
                _append_event(
                    log_path,
                    {**base_event, "status": "RESUME_TERMINAL_NOT_RECUT", "prior_status": prior["status"]},
                )
                summary["skipped"] += 1
                continue
            staged.unlink(missing_ok=True)
            _append_event(log_path, {**base_event, "status": "RESUME_REPROCESS_STALE"})
            summary["reprocessed_stale"] += 1

        state["objects"][item.object_key] = {"status": "IN_PROGRESS", "plan": plan}
        _atomic_json(state_path, state)
        _append_event(log_path, {**base_event, "status": "OBJECT_START"})

        sources: dict = {}
        try:
            try:
                for brickname in plan["planned_bricknames"]:
                    if brickname not in digests:
                        raise ObjectTerminalError(
                            f"planned brick {brickname} absent from sealed manifest",
                            code="FAILED_SOURCE_MISSING",
                        )
                    sources[brickname] = SyntheticBrickSource(
                        source_root / staged_relpath_for(brickname),
                        geometry.row(brickname),
                        digests[brickname],
                    )
                values, coverage, contributed = render_cutout(item, sources)
                zero_coverage = sum(1 for count in coverage if count == 0)
                if zero_coverage:
                    raise ObjectTerminalError(
                        f"{zero_coverage} output pixels have zero source coverage; "
                        "a truncated cutout is rejected, never padded",
                        code="FAILED_ZERO_COVERAGE",
                    )
                invalid_fraction = sum(1 for value in values if not math.isfinite(value)) / len(values)
                if invalid_fraction > invalid_fraction_cap:
                    raise ObjectTerminalError(
                        f"invalid pixel fraction {invalid_fraction} exceeds frozen cap {invalid_fraction_cap}",
                        code="FAILED_INVALID_PIXEL_CAP",
                    )
                header = output_header_bytes(item)
                if tamper_hook is not None:
                    header = tamper_hook(item.object_key, header)
                data = struct.pack(f">{len(values)}f", *values)
                staged_bytes = header + data + b"\x00" * ((-len(data)) % 2880)
                staged.write_bytes(staged_bytes)
                sets = {
                    "planned": plan["planned_bricknames"],
                    "opened": list(sources),
                    "contributing": [name for name, count in contributed.items() if count > 0],
                    "zero_touch": [name for name, count in contributed.items() if count == 0],
                }
                pc3 = pc3_output_receipt(item, staged.read_bytes(), coverage, sets)
            except (FitsIntegrityError, WcsRejectedError, ObjectTerminalError) as exc:
                code = getattr(exc, "code", "FAILED_FITS_INTEGRITY")
                if isinstance(exc, FitsIntegrityError):
                    code = "FAILED_FITS_INTEGRITY"
                _terminal(item, exc, code, base_event, staged)
                continue

            cutout = cutout_dir / f"{item.object_key}.fits"
            staged.replace(cutout)
            receipt = {
                "schema_version": 1,
                "scope": SCOPE,
                "object_key": item.object_key,
                "status": "COMPLETED",
                "plan": plan,
                "invalid_fraction_cap_binding_slot": invalid_fraction_cap,
                "invalid_pixel_fraction": invalid_fraction,
                "sources": {
                    name: {
                        "path": str(source.path),
                        "sha256": source.sha256,
                        "header_sha256": source.header_sha256,
                        "contributed_pixels": contributed[name],
                        "gate": source.gate_receipt,
                    }
                    for name, source in sources.items()
                },
                "pc3": pc3,
                "output_path": str(cutout.relative_to(output_dir)),
                "output_file_sha256": pc3["output_file_sha256"],
                "manifest_sha256": manifest["manifest_sha256"],
                "code_manifest": code_manifest,
                "resampler_note": "deterministic bilinear resampler matching the fixture-oracle interpolation rule (support window [1,N], float64 accumulation, mean over coverage); equivalence with the hash-pinned Imagine/astrometry.net production kernel is bound to Yui's dependency lock and re-gated there",
            }
            _atomic_json(receipt_dir / f"{item.object_key}.json", receipt)
            state["objects"][item.object_key] = receipt
            summary["completed"] += 1
            _append_event(
                log_path,
                {**base_event, "status": "COMPLETED", "output_file_sha256": pc3["output_file_sha256"]},
            )
            _atomic_json(state_path, state)
            if interrupt_hook is not None:
                interrupt_hook(item.object_key, "after_accept")
        finally:
            for source in sources.values():
                source.close()
    _atomic_json(state_path, state)
    summary["log_chain_tip"] = _validate_existing_log(log_path)
    return summary


# ---------------------------------------------------------------------------
# Synthetic fixture writer (used by tests and the CLI dry run only).
# ---------------------------------------------------------------------------

def write_synthetic_brick(
    source_root: Path,
    row: Mapping[str, float],
    *,
    value: float = 1.0,
    data_big_endian: Optional[bytes] = None,
    header_only: bool = False,
    truncate_data: bool = False,
    extra_cards: Iterable = (),
    override_cards: Optional[Mapping[str, object]] = None,
) -> Path:
    cards_map = {
        "SIMPLE": True, "BITPIX": -32, "NAXIS": 2, "NAXIS1": SRC_N, "NAXIS2": SRC_N,
        "CTYPE1": "RA---TAN", "CTYPE2": "DEC--TAN",
        "CRVAL1": float(row["ra"]), "CRVAL2": float(row["dec"]),
        "CRPIX1": SRC_CRPIX, "CRPIX2": SRC_CRPIX,
        "CD1_1": OUT_CD[0][0], "CD1_2": OUT_CD[0][1],
        "CD2_1": OUT_CD[1][0], "CD2_2": OUT_CD[1][1],
        "BUNIT": "nanomaggy", "NMSCOPE": SCOPE,
    }
    for key, value_override in (override_cards or {}).items():
        if value_override is None:
            cards_map.pop(key, None)
        else:
            cards_map[key] = value_override
    cards = [fits_card(key, card_value) for key, card_value in cards_map.items()]
    for extra in extra_cards:
        cards.append(fits_card(*extra) if isinstance(extra, tuple) else extra)
    cards.append(b"END".ljust(80))
    header = b"".join(cards)
    header += b" " * ((-len(header)) % 2880)
    path = Path(source_root) / staged_relpath_for(str(row["brickname"]))
    path.parent.mkdir(parents=True, exist_ok=True)
    if header_only:
        path.write_bytes(header)
        return path
    if data_big_endian is not None:
        if len(data_big_endian) != SRC_N * SRC_N * 4:
            raise ValueError("data_big_endian must be exactly SRC_N*SRC_N big-endian float32")
        data = bytes(data_big_endian)
    else:
        data = struct.pack(">f", value) * (SRC_N * SRC_N)
    data += b"\x00" * ((-len(data)) % 2880)
    if truncate_data:
        data = data[: len(data) // 2]
    path.write_bytes(header + data)
    return path


def make_grid_geometry(centres: Iterable, *, spacing_deg: float = 0.25) -> SyntheticBrickGeometry:
    half = spacing_deg / 2.0
    rows = []
    for index, (ra, dec) in enumerate(centres):
        rows.append(
            {
                "brickname": brickname_for(ra, dec),
                "brickid": index + 1,
                "ra": ra, "dec": dec,
                "ra1": (ra - half) % 360.0, "ra2": (ra + half) % 360.0,
                "dec1": dec - half, "dec2": dec + half,
            }
        )
    return SyntheticBrickGeometry(rows, scope=SCOPE)


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Build-only synthetic dry run for the guarded brick-route local-cut adapter."
    )
    parser.add_argument("--dry-run", action="store_true")
    parser.add_argument("--output-dir", type=Path, required=True)
    args = parser.parse_args()
    if not args.dry_run:
        parser.error("BUILD_ONLY_STOP: only --dry-run is exposed; no transport exists")
    geometry = make_grid_geometry([(0.0, 0.0)])
    source_root = args.output_dir / "_tmp_synthetic_staged"
    write_synthetic_brick(source_root, geometry.rows[0])
    summary = run_local_cut(
        [SyntheticCutTarget("SYNTH-CLI-DRYRUN", 0.0, 0.0)],
        geometry,
        source_root,
        args.output_dir,
        invalid_fraction_cap=0.0,
        manifest_only=True,
    )
    print(json.dumps(summary, sort_keys=True))


if __name__ == "__main__":
    main()
