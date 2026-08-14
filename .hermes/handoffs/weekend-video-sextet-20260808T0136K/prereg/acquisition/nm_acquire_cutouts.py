#!/usr/bin/env python3
"""Build-only Legacy Surveys cutout acquisition pipeline.

STOP RULE: this module contains no real HTTP transport. It may construct requests,
run dry-run planning, and process bytes supplied by an injected mock transport.
"""
from __future__ import annotations

import argparse
import hashlib
import importlib.util
import json
import math
import re
import sys
import time
from datetime import datetime, timezone
from pathlib import Path
from typing import Callable, Iterable, Mapping, cast

FROZEN_SELECTION_STAGES = (
    ("cut_1_primary_mask", "brick_primary = 1 AND maskbits = 0"),
    ("cut_2_extended_positive_flux", "type <> 'PSF' AND flux_r > 0"),
    (
        "cut_3_photo_z",
        "LEFT JOIN photo_z ON (ls_id, release, brickid, objid) AND 0 <= z_phot_median < 0.15",
    ),
    ("cut_4_dered_magnitude", "dered_mag_r < 17.7"),
    ("cut_5_size", "shape_r > 1.5"),
    (
        "cut_6_inclination",
        "POWER(shape_e1,2) + POWER(shape_e2,2) < 0.1836734693877551",
    ),
)

BUILD_ONLY = True
ENDPOINT = "https://www.legacysurvey.org/viewer/fits-cutout"
ROUTE = {
    "layer": "ls-dr10-south",
    "pixscale": "0.262",
    "bands": "grz",
    "size": "256",
    "format": "fits",
}
HERE = Path(__file__).resolve().parent
PARITY_VALIDATOR_PATH = HERE.parent / "yui_bs5_sign_anchor_20260814" / "validate_wcs_parity.py"
PARITY_VALIDATOR_SHA256 = "7bf0201917e7722ee9545c9c11b6cc1cbdec345504e3f29fa1aeb01e58edaa55"
DISTORTION_VALIDATOR_PATH = HERE.parent / "_tori_bs7_distortion_evidence" / "fail_closed_wcs.py"
DISTORTION_VALIDATOR_SHA256 = "cae1b1b7ef4e25000ad5d8c906647216b1425638ac737b4ea7363ca948760569"
TERMINAL_FAILURE_STATUSES = {
    "FAILED_FITS_INTEGRITY",
    "FAILED_TRANSPORT_RETRY_EXHAUSTED",
    "REJECTED_DISTORTION",
    "REJECTED_LINEAR_WCS",
    "REJECTED_NON_CELESTIAL",
    "REJECTED_PARITY",
    "REJECTED_SINGULAR_WCS",
    "REJECTED_WCS",
}
MIN_REQUEST_INTERVAL_SECONDS = 5.0
MAX_CONCURRENT_REQUESTS = 1
BACKOFF_SECONDS = (30.0, 60.0, 120.0)


def _finite_record_number(record: Mapping[str, object], key: str) -> float:
    value = record.get(key)
    if isinstance(value, bool) or not isinstance(value, (int, float)):
        raise ValueError(f"synthetic selection field {key} must be numeric")
    number = float(value)
    if not math.isfinite(number):
        raise ValueError(f"synthetic selection field {key} must be finite")
    return number


def evaluate_frozen_selection(record: Mapping[str, object]) -> dict:
    """Evaluate the frozen Cut 1–6 chain on one explicitly synthetic fixture."""

    if record.get("scope") != "SYNTHETIC_ONLY_BUILD":
        raise ValueError("BUILD_ONLY_STOP: selection evaluator accepts synthetic fixtures only")
    brick_primary = record.get("brick_primary")
    maskbits = record.get("maskbits")
    if isinstance(brick_primary, bool) or not isinstance(brick_primary, int):
        raise ValueError("synthetic brick_primary must be an integer")
    if isinstance(maskbits, bool) or not isinstance(maskbits, int):
        raise ValueError("synthetic maskbits must be an integer")
    source_type = record.get("type")
    if not isinstance(source_type, str) or not source_type:
        raise ValueError("synthetic type must be a nonempty string")
    if not isinstance(record.get("photo_z_join_exact"), bool):
        raise ValueError("synthetic photo_z_join_exact must be boolean")

    flux_r = _finite_record_number(record, "flux_r")
    z_phot_median = _finite_record_number(record, "z_phot_median")
    dered_mag_r = _finite_record_number(record, "dered_mag_r")
    shape_r = _finite_record_number(record, "shape_r")
    shape_e1 = _finite_record_number(record, "shape_e1")
    shape_e2 = _finite_record_number(record, "shape_e2")
    stage_pass = {
        "cut_1_primary_mask": brick_primary == 1 and maskbits == 0,
        "cut_2_extended_positive_flux": source_type != "PSF" and flux_r > 0.0,
        "cut_3_photo_z": record["photo_z_join_exact"] is True
        and 0.0 <= z_phot_median < 0.15,
        "cut_4_dered_magnitude": dered_mag_r < 17.7,
        "cut_5_size": shape_r > 1.5,
        "cut_6_inclination": shape_e1**2 + shape_e2**2 < 0.1836734693877551,
    }
    failed_stage = next((name for name, passed in stage_pass.items() if not passed), None)
    return {
        "scope": "SYNTHETIC_ONLY_BUILD",
        "accepted": failed_stage is None,
        "failed_stage": failed_stage,
        "stage_pass": stage_pass,
    }


class SyntheticObject:
    """Explicitly synthetic acquisition input accepted by the build-only harness."""

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


class RetryableTransportError(RuntimeError):
    """Explicit synthetic service-pressure signal eligible for bounded retry."""


class MockTransport:
    """In-memory transport; the only transport allowed by this build-only artifact."""

    def __init__(self, responses: Mapping[str, object]) -> None:
        if not all(key.startswith("SYNTH-") for key in responses):
            raise ValueError("BUILD_ONLY_STOP: mock response keys must start with SYNTH-")
        self._responses: dict[str, list[object]] = {}
        for key, value in responses.items():
            outcomes = list(value) if isinstance(value, list) else [value]
            if not outcomes or not all(
                isinstance(outcome, (bytes, BaseException)) for outcome in outcomes
            ):
                raise TypeError("mock outcomes must be bytes or exceptions")
            self._responses[key] = outcomes
        self.calls: list[dict] = []
        self.interrupt_before_response_keys: set[str] = set()
        self.interrupt_after_custody_keys: set[str] = set()

    def fetch(self, request: dict) -> bytes:
        self.calls.append(dict(request))
        key = request["object_key"]
        if key in self.interrupt_before_response_keys:
            self.interrupt_before_response_keys.remove(key)
            raise KeyboardInterrupt("synthetic interrupt before response custody")
        if key not in self._responses:
            raise KeyError(f"no synthetic response for {key}")
        if not self._responses[key]:
            raise KeyError(f"synthetic response queue exhausted for {key}")
        outcome = self._responses[key].pop(0)
        if isinstance(outcome, BaseException):
            raise outcome
        if not isinstance(outcome, bytes):
            raise TypeError("mock outcome is not bytes")
        return outcome

    def after_custody(self, request: dict) -> None:
        key = request["object_key"]
        if key in self.interrupt_after_custody_keys:
            self.interrupt_after_custody_keys.remove(key)
            raise KeyboardInterrupt("synthetic interrupt after response custody")


class RateLimiter:
    """Serial request-start limiter with injectable time for offline verification."""

    def __init__(
        self,
        *,
        min_interval_seconds: float = MIN_REQUEST_INTERVAL_SECONDS,
        clock: Callable[[], float] = time.monotonic,
        sleeper: Callable[[float], None] = time.sleep,
    ) -> None:
        if not math.isfinite(min_interval_seconds) or min_interval_seconds < 0:
            raise ValueError("min_interval_seconds must be finite and nonnegative")
        self.min_interval_seconds = float(min_interval_seconds)
        self._clock = clock
        self._sleeper = sleeper
        self._last_request_time: float | None = None
        self.request_times: list[float] = []

    def before_request(self) -> float:
        now = float(self._clock())
        if self._last_request_time is not None:
            remaining = self.min_interval_seconds - (now - self._last_request_time)
            if remaining > 0:
                self._sleeper(remaining)
                now = float(self._clock())
        if self._last_request_time is not None:
            separation = now - self._last_request_time
            if separation + 1e-9 < self.min_interval_seconds:
                raise RuntimeError("rate limiter sleeper did not advance the clock")
        self._last_request_time = now
        self.request_times.append(now)
        return now

    def backoff(self, seconds: float) -> None:
        if not math.isfinite(seconds) or seconds < 0:
            raise ValueError("backoff seconds must be finite and nonnegative")
        self._sleeper(float(seconds))


class FitsIntegrityError(RuntimeError):
    pass


class WcsRejectedError(RuntimeError):
    def __init__(
        self,
        message: str,
        *,
        code: str = "REJECTED_WCS",
        families: list[str] | None = None,
        keywords: list[str] | None = None,
    ) -> None:
        super().__init__(message)
        self.code = code
        self.families = list(families or [])
        self.keywords = list(keywords or [])


def _canonical_bytes(value: object) -> bytes:
    return json.dumps(value, sort_keys=True, separators=(",", ":")).encode("utf-8")


def _sha256_bytes(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


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


def _utc_now() -> str:
    return datetime.now(timezone.utc).isoformat(timespec="seconds").replace("+00:00", "Z")


def build_request(item: SyntheticObject) -> dict:
    if type(item) is not SyntheticObject:
        raise TypeError("BUILD_ONLY_STOP: only SyntheticObject input is accepted")
    url = (
        f"{ENDPOINT}?ra={item.ra_deg:.8f}&dec={item.dec_deg:.8f}"
        f"&layer={ROUTE['layer']}&pixscale={ROUTE['pixscale']}"
        f"&bands={ROUTE['bands']}&size={ROUTE['size']}"
    )
    request = {
        "schema_version": 1,
        "scope": "SYNTHETIC_ONLY_BUILD",
        "object_key": item.object_key,
        "ra_deg": f"{item.ra_deg:.8f}",
        "dec_deg": f"{item.dec_deg:.8f}",
        "url": url,
        "route": dict(ROUTE),
    }
    return request


def _validate_existing_log(log_path: Path) -> str | None:
    previous = None
    if not log_path.exists():
        return previous
    for number, line in enumerate(log_path.read_text(encoding="utf-8").splitlines(), start=1):
        event = json.loads(line)
        claimed = event.pop("event_sha256", None)
        if event.get("previous_event_sha256") != previous:
            raise RuntimeError(f"request log chain broken at line {number}")
        actual = _sha256_bytes(_canonical_bytes(event))
        if claimed != actual:
            raise RuntimeError(f"request log hash mismatch at line {number}")
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


def parse_fits_primary(payload: bytes) -> tuple[dict, list[int]]:
    if not payload or len(payload) % 2880 != 0:
        raise FitsIntegrityError("FITS byte length is empty or not a multiple of 2880")
    if not payload.startswith(b"SIMPLE  ="):
        raise FitsIntegrityError("missing primary SIMPLE card")
    header: dict = {}
    end_offset = None
    for offset in range(0, len(payload), 80):
        card_bytes = payload[offset : offset + 80]
        if len(card_bytes) != 80:
            raise FitsIntegrityError("truncated FITS card")
        try:
            card = card_bytes.decode("ascii")
        except UnicodeDecodeError as exc:
            raise FitsIntegrityError("non-ASCII FITS header") from exc
        key = card[:8].strip().upper()
        if key == "END":
            end_offset = offset + 80
            break
        if card[8:10] == "= " and key:
            header[key] = _fits_value(card[10:])
    if end_offset is None:
        raise FitsIntegrityError("missing FITS END card")
    header_bytes = ((end_offset + 2879) // 2880) * 2880
    if header.get("SIMPLE") is not True:
        raise FitsIntegrityError("SIMPLE must be true")
    bitpix = header.get("BITPIX")
    if bitpix not in {8, 16, 32, 64, -32, -64}:
        raise FitsIntegrityError("unsupported BITPIX")
    if header.get("NAXIS") != 3:
        raise FitsIntegrityError("expected one three-plane primary cube")
    raw_shape = [header.get("NAXIS3"), header.get("NAXIS2"), header.get("NAXIS1")]
    if not all(isinstance(value, int) and not isinstance(value, bool) for value in raw_shape):
        raise FitsIntegrityError("FITS dimensions must be integers")
    shape = cast(list[int], raw_shape)
    if shape != [3, 256, 256]:
        raise FitsIntegrityError(f"expected FITS shape [3, 256, 256], got {shape}")
    data_bytes = math.prod(shape) * (abs(bitpix) // 8)
    expected_total = header_bytes + ((data_bytes + 2879) // 2880) * 2880
    if len(payload) != expected_total:
        raise FitsIntegrityError(
            f"FITS length mismatch expected={expected_total} actual={len(payload)}"
        )
    return header, shape


def _linear_wcs_matrix(header: dict) -> list[list[float]]:
    cd_keys = ("CD1_1", "CD1_2", "CD2_1", "CD2_2")
    pc_keys = ("PC1_1", "PC1_2", "PC2_1", "PC2_2", "CDELT1", "CDELT2")
    has_cd = [key in header for key in cd_keys]
    has_pc = [key in header for key in pc_keys]
    if any(has_cd) and not all(has_cd):
        raise WcsRejectedError("partial CD matrix", code="REJECTED_LINEAR_WCS")
    if any(has_pc) and not all(has_pc):
        raise WcsRejectedError(
            "partial PC/CDELT representation", code="REJECTED_LINEAR_WCS"
        )
    if all(has_cd) and any(has_pc):
        raise WcsRejectedError(
            "ambiguous CD and PC/CDELT representations", code="REJECTED_LINEAR_WCS"
        )
    if all(has_cd):
        return [
            [float(header["CD1_1"]), float(header["CD1_2"])],
            [float(header["CD2_1"]), float(header["CD2_2"])],
        ]
    if all(has_pc):
        return [
            [float(header["PC1_1"]) * float(header["CDELT1"]),
             float(header["PC1_2"]) * float(header["CDELT1"])],
            [float(header["PC2_1"]) * float(header["CDELT2"]),
             float(header["PC2_2"]) * float(header["CDELT2"])],
        ]
    raise WcsRejectedError(
        "missing complete CD or PC/CDELT linear WCS", code="REJECTED_LINEAR_WCS"
    )


def validate_wcs(header: dict) -> tuple[dict, list[str], list[str]]:
    if not str(header.get("CTYPE1", "")).startswith("RA---"):
        raise WcsRejectedError("CTYPE1 is not celestial RA", code="REJECTED_NON_CELESTIAL")
    if not str(header.get("CTYPE2", "")).startswith("DEC--"):
        raise WcsRejectedError("CTYPE2 is not celestial DEC", code="REJECTED_NON_CELESTIAL")
    distortion = _load_hash_pinned_module(
        DISTORTION_VALIDATOR_PATH,
        DISTORTION_VALIDATOR_SHA256,
        "nm_hash_pinned_fail_closed_wcs",
    )
    families, distortion_keywords = distortion.distortion_families(header)
    families = list(families)
    distortion_keywords = list(distortion_keywords)
    if families:
        raise WcsRejectedError(
            "distortion-bearing WCS rejected",
            code="REJECTED_DISTORTION",
            families=families,
            keywords=distortion_keywords,
        )
    matrix = _linear_wcs_matrix(header)
    parity = _load_hash_pinned_module(
        PARITY_VALIDATOR_PATH,
        PARITY_VALIDATOR_SHA256,
        "nm_hash_pinned_yui_parity",
    )
    determinant = parity.determinant_2x2(matrix)
    if not math.isfinite(determinant) or determinant == 0.0:
        raise WcsRejectedError(
            "singular or non-finite WCS determinant", code="REJECTED_SINGULAR_WCS"
        )
    yui_template = parity.build_parity_receipt()
    row_transform = [list(row) for row in yui_template["row_order_transform_matrix"]]
    combined = parity.multiply_2x2(matrix, row_transform)
    combined_determinant = parity.determinant_2x2(combined)
    combined_sign = 1 if combined_determinant > 0 else -1
    tolerance = 1e-12
    east_left = matrix[0][0] < 0 and abs(matrix[0][1]) <= tolerance
    north_up = matrix[1][1] > 0 and abs(matrix[1][0]) <= tolerance
    if combined_sign != -1 or not east_left or not north_up:
        raise WcsRejectedError(
            "WCS parity is not North-up/East-left", code="REJECTED_PARITY"
        )
    return (
        {
            "validator_path": str(PARITY_VALIDATOR_PATH),
            "validator_sha256": PARITY_VALIDATOR_SHA256,
            "logical_pixel_axes": yui_template["logical_pixel_axes"],
            "sky_tangent_axes": yui_template["sky_tangent_axes"],
            "binding_pc3_quote": yui_template["binding_pc3_quote"],
            "row_transform": row_transform,
            "linear_matrix": matrix,
            "linear_determinant": determinant,
            "combined_matrix": combined,
            "combined_determinant": combined_determinant,
            "combined_determinant_sign": combined_sign,
            "east_left": east_left,
            "north_up": north_up,
        },
        families,
        distortion_keywords,
    )


def _summary() -> dict:
    return {
        "scope": "SYNTHETIC_ONLY_BUILD",
        "dry_run_requests": 0,
        "issued_requests": 0,
        "completed": 0,
        "failed": 0,
        "skipped": 0,
        "uncertain": 0,
        "resumed_complete": 0,
        "resumed_custodied": 0,
        "transient_retries": 0,
    }


def _load_state(path: Path) -> dict:
    if not path.exists():
        return {"scope": "SYNTHETIC_ONLY_BUILD", "objects": {}}
    if path.is_symlink() or not path.is_file():
        raise RuntimeError("state.json must be a regular file")
    try:
        state = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, UnicodeError, json.JSONDecodeError) as exc:
        raise RuntimeError("state.json is not valid UTF-8 JSON") from exc
    if state.get("scope") != "SYNTHETIC_ONLY_BUILD" or not isinstance(
        state.get("objects"), dict
    ):
        raise RuntimeError("state.json scope/schema mismatch")
    return state


def _validate_completed(
    output_dir: Path, item: SyntheticObject, request_sha256: str, prior: dict
) -> dict:
    receipt_path = output_dir / "receipts" / f"{item.object_key}.json"
    if receipt_path.is_symlink() or not receipt_path.is_file():
        raise RuntimeError("completed receipt missing or not regular")
    receipt = json.loads(receipt_path.read_text(encoding="utf-8"))
    if receipt != prior:
        raise RuntimeError("completed state and receipt differ")
    if receipt.get("status") != "COMPLETED":
        raise RuntimeError("completed receipt status drift")
    if receipt.get("request_sha256") != request_sha256:
        raise RuntimeError("completed request hash drift")
    expected_rel = f"cutouts/{item.object_key}.fits"
    if receipt.get("output_path") != expected_rel:
        raise RuntimeError("completed output path drift")
    cutout = output_dir / expected_rel
    if cutout.is_symlink() or not cutout.is_file():
        raise RuntimeError("completed output missing or not regular")
    actual = _sha256_bytes(cutout.read_bytes())
    if actual != receipt.get("output_sha256") or actual != receipt.get("response_sha256"):
        raise RuntimeError("completed output checksum mismatch")
    return receipt


def run_pipeline(
    objects: Iterable[SyntheticObject],
    output_dir: Path,
    *,
    transport: object,
    dry_run: bool,
    rate_limiter: RateLimiter | None = None,
) -> dict:
    output_dir = Path(output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)
    log_path = output_dir / "request_log.jsonl"
    summary = _summary()
    if not dry_run and type(transport) is not MockTransport:
        raise RuntimeError("BUILD_ONLY_STOP: only exact MockTransport is allowed")
    mock_transport = cast(MockTransport, transport)
    limiter = rate_limiter or RateLimiter()
    summary["rate_policy"] = {
        "max_concurrent_requests": MAX_CONCURRENT_REQUESTS,
        "min_interval_seconds": limiter.min_interval_seconds,
        "backoff_seconds": list(BACKOFF_SECONDS),
    }
    state_path = output_dir / "state.json"
    state = (
        {"scope": "SYNTHETIC_ONLY_BUILD", "objects": {}}
        if dry_run
        else _load_state(state_path)
    )
    state["summary"] = summary
    for item in objects:
        request = build_request(item)
        request_sha256 = _sha256_bytes(_canonical_bytes(request))
        base_event = {
            "recorded_utc": _utc_now(),
            "object_key": item.object_key,
            "request": request,
            "request_sha256": request_sha256,
        }
        if dry_run:
            _append_event(
                log_path,
                {**base_event, "status": "DRY_RUN_NOT_ISSUED", "response_sha256": None},
            )
            state["objects"][item.object_key] = {"status": "DRY_RUN_NOT_ISSUED"}
            summary["dry_run_requests"] += 1
            continue

        resumed_payload: bytes | None = None
        prior = state["objects"].get(item.object_key)
        if prior is not None:
            if not isinstance(prior, dict):
                raise RuntimeError("object state must be a JSON object")
            if prior.get("request_sha256") != request_sha256:
                raise RuntimeError("resume request hash drift")
            if prior.get("status") == "IN_FLIGHT_UNCERTAIN":
                _append_event(
                    log_path,
                    {
                        **base_event,
                        "status": "RESUME_IN_FLIGHT_UNCERTAIN_NOT_REFETCHED",
                        "response_sha256": None,
                    },
                )
                summary["uncertain"] += 1
                _atomic_json(state_path, state)
                continue
            if prior.get("status") in TERMINAL_FAILURE_STATUSES:
                receipt_path = output_dir / "receipts" / f"{item.object_key}.json"
                if receipt_path.is_symlink() or not receipt_path.is_file():
                    raise RuntimeError("terminal failure receipt missing or not regular")
                failure_receipt = json.loads(receipt_path.read_text(encoding="utf-8"))
                if failure_receipt != prior:
                    raise RuntimeError("terminal failure state and receipt differ")
                if failure_receipt.get("output_path") is not None:
                    raise RuntimeError("terminal failure unexpectedly has output")
                _append_event(
                    log_path,
                    {
                        **base_event,
                        "status": "RESUME_TERMINAL_FAILURE_NOT_REFETCHED",
                        "prior_status": prior["status"],
                        "response_sha256": prior.get("response_sha256"),
                    },
                )
                summary["failed"] += 1
                summary["skipped"] += 1
                _atomic_json(state_path, state)
                continue
            if prior.get("status") == "COMPLETED":
                receipt = _validate_completed(output_dir, item, request_sha256, prior)
                _append_event(
                    log_path,
                    {
                        **base_event,
                        "status": "RESUME_COMPLETE_NOT_REFETCHED",
                        "response_sha256": receipt["response_sha256"],
                        "output_sha256": receipt["output_sha256"],
                    },
                )
                summary["resumed_complete"] += 1
                _atomic_json(state_path, state)
                continue
            if prior.get("status") == "RESPONSE_CUSTODIED":
                expected_rel = f"staging/{item.object_key}.response.part"
                if prior.get("staged_path") != expected_rel:
                    raise RuntimeError("custodied staged path drift")
                staged_prior = output_dir / expected_rel
                if staged_prior.is_symlink() or not staged_prior.is_file():
                    raise RuntimeError("custodied staged response missing or not regular")
                resumed_payload = staged_prior.read_bytes()
                if _sha256_bytes(resumed_payload) != prior.get("response_sha256"):
                    raise RuntimeError("custodied staged response checksum mismatch")
                _append_event(
                    log_path,
                    {
                        **base_event,
                        "status": "RESUME_RESPONSE_CUSTODIED",
                        "response_sha256": prior["response_sha256"],
                    },
                )
                summary["resumed_custodied"] += 1

        cutout_dir = output_dir / "cutouts"
        receipt_dir = output_dir / "receipts"
        staging_dir = output_dir / "staging"
        for directory in (cutout_dir, receipt_dir, staging_dir):
            directory.mkdir(parents=True, exist_ok=True)
        staged = staging_dir / f"{item.object_key}.response.part"
        if resumed_payload is None:
            attempt = 1
            transport_failed = False
            payload: bytes | None = None
            while True:
                request_start = limiter.before_request()
                state["objects"][item.object_key] = {
                    "status": "IN_FLIGHT_UNCERTAIN",
                    "request_sha256": request_sha256,
                    "attempt": attempt,
                }
                _atomic_json(output_dir / "state.json", state)
                _append_event(
                    log_path,
                    {
                        **base_event,
                        "status": "REQUEST_ISSUING",
                        "response_sha256": None,
                        "attempt": attempt,
                        "rate_limit_monotonic": request_start,
                    },
                )
                summary["issued_requests"] += 1
                try:
                    payload = mock_transport.fetch(request)
                except RetryableTransportError as exc:
                    if attempt > len(BACKOFF_SECONDS):
                        status = "FAILED_TRANSPORT_RETRY_EXHAUSTED"
                        failure_receipt = {
                            "schema_version": 1,
                            "scope": "SYNTHETIC_ONLY_BUILD",
                            "object_key": item.object_key,
                            "status": status,
                            "request_sha256": request_sha256,
                            "response_sha256": None,
                            "output_sha256": None,
                            "output_path": None,
                            "fits_shape": None,
                            "error_type": type(exc).__name__,
                            "error": str(exc),
                            "attempts": attempt,
                            "distortion_families_detected": [],
                            "distortion_keywords_detected": [],
                        }
                        _atomic_json(
                            receipt_dir / f"{item.object_key}.json", failure_receipt
                        )
                        state["objects"][item.object_key] = failure_receipt
                        summary["failed"] += 1
                        _append_event(
                            log_path,
                            {
                                **base_event,
                                "status": status,
                                "response_sha256": None,
                                "attempt": attempt,
                                "error_type": type(exc).__name__,
                            },
                        )
                        _atomic_json(output_dir / "state.json", state)
                        transport_failed = True
                        break
                    backoff = BACKOFF_SECONDS[attempt - 1]
                    state["objects"][item.object_key] = {
                        "status": "RETRY_WAIT_SAFE",
                        "request_sha256": request_sha256,
                        "attempt": attempt,
                        "backoff_seconds": backoff,
                    }
                    _atomic_json(output_dir / "state.json", state)
                    _append_event(
                        log_path,
                        {
                            **base_event,
                            "status": "RETRYABLE_TRANSPORT_ERROR_BACKOFF",
                            "response_sha256": None,
                            "attempt": attempt,
                            "backoff_seconds": backoff,
                            "error_type": type(exc).__name__,
                        },
                    )
                    summary["transient_retries"] += 1
                    limiter.backoff(backoff)
                    attempt += 1
                    continue
                break
            if transport_failed:
                continue
            if not isinstance(payload, bytes):
                raise TypeError("mock transport response must be bytes")
            response_sha256 = _sha256_bytes(payload)
            staged.write_bytes(payload)
            state["objects"][item.object_key] = {
                "status": "RESPONSE_CUSTODIED",
                "request_sha256": request_sha256,
                "response_sha256": response_sha256,
                "staged_path": str(staged.relative_to(output_dir)),
            }
            _atomic_json(output_dir / "state.json", state)
            _append_event(
                log_path,
                {
                    **base_event,
                    "status": "RESPONSE_CUSTODIED",
                    "response_sha256": response_sha256,
                },
            )
            mock_transport.after_custody(request)
        else:
            payload = resumed_payload
            response_sha256 = _sha256_bytes(payload)
        try:
            header, shape = parse_fits_primary(payload)
            parity_receipt, families, distortion_keywords = validate_wcs(header)
        except (FitsIntegrityError, WcsRejectedError) as exc:
            status = (
                "FAILED_FITS_INTEGRITY"
                if isinstance(exc, FitsIntegrityError)
                else exc.code
            )
            families = [] if isinstance(exc, FitsIntegrityError) else exc.families
            distortion_keywords = [] if isinstance(exc, FitsIntegrityError) else exc.keywords
            staged.unlink(missing_ok=True)
            failure_receipt = {
                "schema_version": 1,
                "scope": "SYNTHETIC_ONLY_BUILD",
                "object_key": item.object_key,
                "status": status,
                "request_sha256": request_sha256,
                "response_sha256": response_sha256,
                "output_sha256": None,
                "output_path": None,
                "fits_shape": None,
                "error_type": type(exc).__name__,
                "error": str(exc),
                "distortion_validator_path": str(DISTORTION_VALIDATOR_PATH),
                "distortion_validator_sha256": DISTORTION_VALIDATOR_SHA256,
                "distortion_families_detected": families,
                "distortion_keywords_detected": distortion_keywords,
            }
            _atomic_json(receipt_dir / f"{item.object_key}.json", failure_receipt)
            state["objects"][item.object_key] = failure_receipt
            summary["failed"] += 1
            _append_event(
                log_path,
                {
                    **base_event,
                    "status": status,
                    "response_sha256": response_sha256,
                    "error_type": type(exc).__name__,
                },
            )
            _atomic_json(output_dir / "state.json", state)
            continue
        cutout = cutout_dir / f"{item.object_key}.fits"
        staged.replace(cutout)
        output_sha256 = _sha256_bytes(cutout.read_bytes())
        if output_sha256 != response_sha256:
            raise RuntimeError("stored output checksum differs from response checksum")
        receipt = {
            "schema_version": 1,
            "scope": "SYNTHETIC_ONLY_BUILD",
            "object_key": item.object_key,
            "status": "COMPLETED",
            "request_sha256": request_sha256,
            "response_sha256": response_sha256,
            "output_sha256": output_sha256,
            "output_path": str(cutout.relative_to(output_dir)),
            "fits_shape": shape,
            "parity": parity_receipt,
            "distortion_validator_path": str(DISTORTION_VALIDATOR_PATH),
            "distortion_validator_sha256": DISTORTION_VALIDATOR_SHA256,
            "distortion_families_detected": families,
            "distortion_keywords_detected": distortion_keywords,
        }
        _atomic_json(receipt_dir / f"{item.object_key}.json", receipt)
        state["objects"][item.object_key] = receipt
        summary["completed"] += 1
        _append_event(
            log_path,
            {**base_event, "status": "COMPLETED", "response_sha256": response_sha256,
             "output_sha256": output_sha256},
        )
        _atomic_json(output_dir / "state.json", state)
    _atomic_json(output_dir / "state.json", state if not dry_run else summary)
    return summary


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Build-only synthetic dry-run for the cutout acquisition pipeline."
    )
    parser.add_argument("--dry-run", action="store_true")
    parser.add_argument("--output-dir", type=Path, required=True)
    args = parser.parse_args()
    if not args.dry_run:
        parser.error("BUILD_ONLY_STOP: only --dry-run is exposed; no real transport exists")
    summary = run_pipeline(
        [SyntheticObject("SYNTH-CLI-DRYRUN", 12.5, -3.25)],
        args.output_dir,
        transport=MockTransport({}),
        dry_run=True,
    )
    print(json.dumps(summary, sort_keys=True))


if __name__ == "__main__":
    main()
