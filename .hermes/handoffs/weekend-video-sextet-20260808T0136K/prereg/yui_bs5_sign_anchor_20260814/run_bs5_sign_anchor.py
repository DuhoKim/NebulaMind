#!/usr/bin/env python3
"""Run the BS-5 absolute-sign anchor on fixed synthetic CCW spirals only.

The WCS parity receipt must already pass before this runner can load the frozen
model or generate a spiral. The frozen Longo convention is never mutable here:
CCW apparent winding in sky coordinates means chi > 0.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import math
import platform
import sys
from pathlib import Path

import numpy as np
import torch
import torch.nn as nn

ROOT = Path(
    "/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/"
    "weekend-video-sextet-20260808T0136K"
)
OUT = ROOT / "prereg/yui_bs5_sign_anchor_20260814"
PREREG = ROOT / "prereg/PREREG_LONGO_AMPLITUDE_TEST_FROZEN_20260814.md"
DRAFT = ROOT / "prereg/PREREG_LONGO_AMPLITUDE_TEST_20260812.md"
SIGN_DICTIONARY = ROOT / "prereg/LANA_BS5_LONGO_SIGN_20260814.md"
AUTHORITY_BRIEF = ROOT / "prereg/_tmp_YUI_SIGN_ANCHOR_BRIEF.md"
WEIGHTS = ROOT / "prereg/weights_frozen.pt"
TRAIN_RESULTS = ROOT / "prereg/train_results.json"
RECEIPT_RESULTS = ROOT / "prereg/receipt_results.json"
BASE_RUNNER = ROOT / "prereg/yui_bs3_r4_r5_20260813/run_bs3_r4_r5.py"
FROZEN_GENERATOR = ROOT / "spike/yui_identity/w_chi.py"
WCS_RECEIPT = OUT / "wcs_parity.json"
WCS_VALIDATOR = OUT / "validate_wcs_parity.py"

EXPECTED_HASHES = {
    PREREG: "da2c6a21d994b9af7395347bf881075f855826ff859dd0415f15042f80ed3308",
    DRAFT: "ac43490054b159610385b8faac28dc4e3178161fadd97d66aa0418a1186b7590",
    SIGN_DICTIONARY: "b7c32dcf12d9e147e5dee6a8262d925b61011615f2ee1d75d687600abb0a72ca",
    AUTHORITY_BRIEF: "f8f0633a9e2bb513534ba721e79e573afd0e8e2d0e2ef3a11f6bcfee3be45602",
    WEIGHTS: "83008c1cbdae511af5d30020540e1e281c62c2bd95d3cb05527fc0687bf49e6d",
    TRAIN_RESULTS: "c36cd33001e432c60df786da8c0ff95b8ef5ab350a458b29d71ff084178a41fd",
    RECEIPT_RESULTS: "d5d4a8bc005b031ed523e64a672237536896f37030722fd5cf71ff44a3405a04",
    BASE_RUNNER: "de0f35355902f25497e240a413a087a1413d365342419b0be3fc15a7e5117914",
    FROZEN_GENERATOR: "89da33ec6260e75e06eadb0f171da4c52f1478b59ff5e543d363dbf56fefcd75",
}
EXPECTED_CANONICAL_WEIGHTS = "1075a4d91c295d7f3256128534a0b8c4d097fb9d162169df1ac698843637a589"
EXPECTED_NULL_MANIFEST = "1963132f2f36e7aa42b08012aad02d2c541d6c0973740a5bbce6a6e7a2904bd1"
FROZEN_TAU = 4.4006456017494235
MASTER_SEED = "LONGO-AMPLITUDE-BS5-ABSOLUTE-SIGN-V1"
PROBE_INDEX_START = 5_000_000
N_PROBES = 32
RASTER_SIZE = 128
GENERATOR_PIXEL_PHASE = 0.7
ESTIMATOR_SIGN_MULTIPLIER = 1
FROZEN_SIGN_CONVENTION = "CCW apparent winding East-of-North => chi > 0"

_yy, _xx = np.mgrid[0:RASTER_SIZE, 0:RASTER_SIZE]
_center = (RASTER_SIZE - 1) / 2.0
_dx = _xx - _center
_north = _yy - _center


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def seed_for_source(source_index: int) -> int:
    payload = f"{MASTER_SEED}||{source_index}".encode()
    return int.from_bytes(hashlib.sha256(payload).digest()[:8], "big") % (2**63)


def _fraction(two_bytes: bytes) -> float:
    return int.from_bytes(two_bytes, "big") / 65535.0


def probe_definitions() -> list[dict]:
    probes = []
    for probe_index in range(N_PROBES):
        source_index = PROBE_INDEX_START + probe_index
        digest = hashlib.sha256(f"{MASTER_SEED}||PARAMS||{source_index}".encode()).digest()
        probes.append(
            {
                "probe_index": probe_index,
                "source_index": source_index,
                "seed": seed_for_source(source_index),
                "pitch_deg": 12.0 + 26.0 * _fraction(digest[0:2]),
                "inclination_deg": 55.0 * _fraction(digest[2:4]),
                "snr": 35.0 + 15.0 * _fraction(digest[4:6]),
                "arms": 2,
                "arm_amplitude": 0.9,
                "pixel_phase": GENERATOR_PIXEL_PHASE,
                "apparent_winding": "CCW",
            }
        )
    return probes


def pure_index_mirror(image: np.ndarray) -> np.ndarray:
    return np.fliplr(image)


def synthetic_ccw_spiral(
    *, seed: int, pitch_deg: float, inclination_deg: float, snr: float
) -> np.ndarray:
    """Render a known CCW spiral directly on the North-up/East-left raster.

    East = -column displacement and North = +logical row displacement. Sky PA
    is atan2(East, North), increasing North through East. The ridge obeys
    PA(r) = cot(pitch)*ln(r/8) + pixel_phase - pi/2, so dPA/dln(r)>0.
    This is algebraically the frozen parity=+1 generator expressed in sky axes.
    """
    q = math.cos(math.radians(inclination_deg))
    west = _dx
    north_deprojected = _north / q
    east = -west
    radius = np.hypot(east, north_deprojected)
    pa_east_of_north = np.arctan2(east, north_deprojected)
    radius_safe = np.maximum(radius, 0.5)
    disk = np.exp(-radius_safe / 18.0)
    winding_rate = 1.0 / math.tan(math.radians(pitch_deg))
    sky_phase = GENERATOR_PIXEL_PHASE - math.pi / 2.0
    spiral = 1.0 + 0.9 * np.cos(
        2.0 * (pa_east_of_north - winding_rate * np.log(radius_safe / 8.0) - sky_phase)
    )
    image = disk * spiral
    image[radius > 60.0] = 0.0
    image = image / image.max()
    if math.isfinite(snr):
        rng = np.random.default_rng(seed)
        image = image + rng.standard_normal((RASTER_SIZE, RASTER_SIZE)) * (1.0 / snr)
    return np.ascontiguousarray(image, dtype=np.float32)


def measure_sky_winding_slope(image: np.ndarray, *, inclination_deg: float) -> float:
    """Measure two-arm ridge PA slope in sky axes from rendered pixels."""
    q = math.cos(math.radians(inclination_deg))
    east = -_dx
    north_deprojected = _north / q
    radius = np.hypot(east, north_deprojected)
    pa = np.arctan2(east, north_deprojected)
    radial_edges = np.linspace(8.0, 52.0, 23)
    phases = []
    log_radii = []
    image64 = np.asarray(image, dtype=np.float64)
    for lower, upper in zip(radial_edges[:-1], radial_edges[1:]):
        selected = (radius >= lower) & (radius < upper)
        values = image64[selected]
        centred = values - values.mean()
        coefficient = np.sum(centred * np.exp(-2j * pa[selected]))
        phases.append(float(np.angle(coefficient)))
        log_radii.append(math.log((lower + upper) / 2.0))
    ridge_pa = -np.unwrap(np.asarray(phases, dtype=np.float64)) / 2.0
    x = np.asarray(log_radii, dtype=np.float64)
    x = x - x.mean()
    return float(np.dot(x, ridge_pa - ridge_pa.mean()) / np.dot(x, x))


def apply_estimator_sign(value: np.float32, multiplier: int = ESTIMATOR_SIGN_MULTIPLIER) -> np.float32:
    if multiplier not in (-1, 1):
        raise ValueError("estimator sign multiplier must be +1 or -1")
    return np.float32(np.float32(multiplier) * np.float32(value))


def sign_pair_fields(
    estimator_value: np.float32, estimator_mirror: np.float32, *, tau: float
) -> dict[str, bool]:
    """Return JSON-native predicates for a serialized estimator sign pair."""
    return {
        "estimator_sign_pair_pass": bool(
            estimator_value > np.float32(0.0)
            and estimator_mirror < np.float32(0.0)
        ),
        "accepted_at_frozen_tau": bool(abs(estimator_value) > tau),
    }


def execution_history() -> dict:
    return {
        "technical_rerun_after_serialization_failure": True,
        "attempt1_failed_before_any_sign_result": True,
        "attempt1_error": "numpy.bool_ was not JSON serializable",
        "attempt1_stdout": "prereg/yui_bs5_sign_anchor_20260814/attempt1_pre_correction_stdout.log",
        "attempt1_stderr": "prereg/yui_bs5_sign_anchor_20260814/attempt1_pre_correction_stderr.log",
        "attempt1_partial_records": "prereg/yui_bs5_sign_anchor_20260814/attempt1_partial_probe_records.jsonl",
        "probe_selection_tuned_or_replaced": False,
    }


class OriginalBlock(nn.Module):
    def __init__(self, channels_in: int, channels_out: int, stride: int):
        super().__init__()
        self.c1 = nn.Conv2d(channels_in, channels_out, 3, stride, 1, bias=False)
        self.b1 = nn.BatchNorm2d(channels_out)
        self.c2 = nn.Conv2d(channels_out, channels_out, 3, 1, 1, bias=False)
        self.b2 = nn.BatchNorm2d(channels_out)
        self.sh = (
            nn.Sequential()
            if stride == 1 and channels_in == channels_out
            else nn.Sequential(
                nn.Conv2d(channels_in, channels_out, 1, stride, bias=False),
                nn.BatchNorm2d(channels_out),
            )
        )

    def forward(self, value: torch.Tensor) -> torch.Tensor:
        import torch.nn.functional as functional

        return functional.relu(
            self.b2(self.c2(functional.relu(self.b1(self.c1(value))))) + self.sh(value)
        )


class OriginalTrunk(nn.Module):
    def __init__(self):
        super().__init__()
        layers: list[nn.Module] = [
            nn.Conv2d(1, 32, 3, 1, 1, bias=False),
            nn.BatchNorm2d(32),
            nn.ReLU(),
        ]
        widths = [32, 64, 128, 256]
        for stage in range(4):
            incoming = widths[max(stage - 1, 0)] if stage else 32
            layers.extend(
                [
                    OriginalBlock(incoming, widths[stage], 1 if stage == 0 else 2),
                    OriginalBlock(widths[stage], widths[stage], 1),
                ]
            )
        self.f = nn.Sequential(
            *layers,
            nn.AdaptiveAvgPool2d(1),
            nn.Flatten(),
            nn.Linear(256, 1),
        )

    def forward(self, value: torch.Tensor) -> torch.Tensor:
        return self.f(value).squeeze(-1)


def build_and_load_model() -> OriginalTrunk:
    model = OriginalTrunk()
    state = torch.load(WEIGHTS, map_location="cpu", weights_only=True)
    model.load_state_dict(state, strict=True)
    model.eval()
    return model


def canonical_parameter_hash(model: nn.Module) -> str:
    digest = hashlib.sha256()
    for parameter in model.parameters():
        digest.update(parameter.detach().numpy().astype("<f4").tobytes())
    return digest.hexdigest()


def raw_output(model: nn.Module, image: np.ndarray) -> np.float32:
    contiguous = np.ascontiguousarray(image, dtype=np.float32)
    with torch.no_grad():
        return np.float32(model(torch.from_numpy(contiguous)[None, None]).item())


def base_chi(model: nn.Module, image: np.ndarray) -> np.float32:
    original = np.ascontiguousarray(image, dtype=np.float32)
    mirrored = np.ascontiguousarray(pure_index_mirror(original))
    return np.float32(
        (raw_output(model, original) - raw_output(model, mirrored)) / np.float32(2.0)
    )


def production_chi(model: nn.Module, image: np.ndarray) -> np.float32:
    return apply_estimator_sign(base_chi(model, image))


def verify_parity_first() -> dict:
    if not WCS_RECEIPT.is_file():
        raise SystemExit("WCS PARITY RECEIPT MISSING; model load and spiral generation prohibited")
    receipt = json.loads(WCS_RECEIPT.read_text(encoding="utf-8"))
    checks = receipt.get("checks", {})
    if receipt.get("status") != "PASS_WCS_PARITY_FIRST" or not checks or not all(checks.values()):
        raise SystemExit("WCS PARITY RECEIPT FAILED; model load and spiral generation prohibited")
    if not (
        receipt["east_direction_on_raster"] == "left"
        and receipt["north_direction_on_raster"] == "up"
        and receipt["combined_pixel_to_sky_determinant"] < 0.0
    ):
        raise SystemExit("WCS PARITY SEMANTICS MISMATCH")
    return {
        "path": str(WCS_RECEIPT.relative_to(ROOT)),
        "sha256": sha256_file(WCS_RECEIPT),
        "status": receipt["status"],
        "cd_pc_cdelt_determinant": receipt["cd_pc_cdelt_determinant"],
        "row_order_transform_determinant": receipt["row_order_transform_determinant"],
        "combined_pixel_to_sky_determinant": receipt["combined_pixel_to_sky_determinant"],
        "east_direction_on_raster": receipt["east_direction_on_raster"],
        "north_direction_on_raster": receipt["north_direction_on_raster"],
    }


def verify_frozen_inputs() -> dict:
    actual = {str(path.relative_to(ROOT)): sha256_file(path) for path in EXPECTED_HASHES}
    mismatches = {
        str(path.relative_to(ROOT)): {"expected": expected, "actual": actual[str(path.relative_to(ROOT))]}
        for path, expected in EXPECTED_HASHES.items()
        if actual[str(path.relative_to(ROOT))] != expected
    }
    if mismatches:
        raise SystemExit("FROZEN INPUT HASH MISMATCH\n" + json.dumps(mismatches, indent=2))
    train = json.loads(TRAIN_RESULTS.read_text(encoding="utf-8"))
    receipt = json.loads(RECEIPT_RESULTS.read_text(encoding="utf-8"))
    value_checks = {
        "tau": train["tau"] == FROZEN_TAU,
        "canonical_weights_record": train["weights_sha256_canonical"] == EXPECTED_CANONICAL_WEIGHTS,
        "master_seed_record": receipt["master_seed"] == "LONGO-AMPLITUDE-FREEZE-M1",
        "null_manifest": (
            receipt["null_manifest"]["manifest_sha256"] == EXPECTED_NULL_MANIFEST
            and receipt["null_manifest"]["n"] == 8000
        ),
    }
    if not all(value_checks.values()):
        raise SystemExit("FROZEN VALUE MISMATCH\n" + json.dumps(value_checks, indent=2))
    return {"hashes": actual, "value_checks": value_checks}


def run(stage: str) -> dict:
    parity = verify_parity_first()
    frozen_before = verify_frozen_inputs()
    torch.set_num_threads(1)
    torch.set_num_interop_threads(1)
    torch.use_deterministic_algorithms(True)
    model = build_and_load_model()
    canonical_hash = canonical_parameter_hash(model)
    if canonical_hash != EXPECTED_CANONICAL_WEIGHTS:
        raise SystemExit(f"CANONICAL WEIGHTS HASH MISMATCH: {canonical_hash}")

    records_path = OUT / f"{stage.replace('-', '_')}_probe_records.jsonl"
    image_manifest = hashlib.sha256()
    counts = {
        "known_ccw_image_slope_positive": 0,
        "known_cw_mirror_slope_negative": 0,
        "mirror_involution_byte_exact": 0,
        "base_chi_ccw_positive": 0,
        "base_chi_mirror_negative": 0,
        "estimator_chi_ccw_positive": 0,
        "estimator_chi_mirror_negative": 0,
        "estimator_antisymmetry_value_exact": 0,
        "estimator_accepted_at_tau": 0,
    }
    estimator_values = []
    with records_path.open("w", encoding="utf-8") as records:
        for probe in probe_definitions():
            image = synthetic_ccw_spiral(
                seed=probe["seed"],
                pitch_deg=probe["pitch_deg"],
                inclination_deg=probe["inclination_deg"],
                snr=probe["snr"],
            )
            mirrored = np.ascontiguousarray(pure_index_mirror(image))
            image_sha = hashlib.sha256(image.tobytes()).hexdigest()
            mirrored_sha = hashlib.sha256(mirrored.tobytes()).hexdigest()
            image_manifest.update(bytes.fromhex(image_sha))
            image_manifest.update(bytes.fromhex(mirrored_sha))
            slope = measure_sky_winding_slope(image, inclination_deg=probe["inclination_deg"])
            mirrored_slope = measure_sky_winding_slope(
                mirrored, inclination_deg=probe["inclination_deg"]
            )
            involution = pure_index_mirror(mirrored).tobytes() == image.tobytes()
            base_value = base_chi(model, image)
            base_mirror = base_chi(model, mirrored)
            estimator_value = apply_estimator_sign(base_value)
            estimator_mirror = apply_estimator_sign(base_mirror)
            serialized_sign_fields = sign_pair_fields(
                estimator_value, estimator_mirror, tau=FROZEN_TAU
            )
            estimator_values.append(float(estimator_value))
            counts["known_ccw_image_slope_positive"] += int(slope > 0.0)
            counts["known_cw_mirror_slope_negative"] += int(mirrored_slope < 0.0)
            counts["mirror_involution_byte_exact"] += int(involution)
            counts["base_chi_ccw_positive"] += int(base_value > 0.0)
            counts["base_chi_mirror_negative"] += int(base_mirror < 0.0)
            counts["estimator_chi_ccw_positive"] += int(estimator_value > 0.0)
            counts["estimator_chi_mirror_negative"] += int(estimator_mirror < 0.0)
            counts["estimator_antisymmetry_value_exact"] += int(
                estimator_mirror == np.float32(-estimator_value)
            )
            counts["estimator_accepted_at_tau"] += int(abs(estimator_value) > FROZEN_TAU)
            row = {
                **probe,
                "wcs_status": parity["status"],
                "analytic_d_pa_d_ln_r": 1.0 / math.tan(math.radians(probe["pitch_deg"])),
                "measured_ccw_image_d_pa_d_ln_r": slope,
                "measured_mirror_d_pa_d_ln_r": mirrored_slope,
                "image_sha256_float32": image_sha,
                "mirror_sha256_float32": mirrored_sha,
                "mirror_involution_byte_exact": involution,
                "base_chi_ccw_float32": float(base_value),
                "base_chi_mirror_float32": float(base_mirror),
                "estimator_sign_multiplier": ESTIMATOR_SIGN_MULTIPLIER,
                "estimator_chi_ccw_float32": float(estimator_value),
                "estimator_chi_mirror_float32": float(estimator_mirror),
                **serialized_sign_fields,
            }
            records.write(json.dumps(row, sort_keys=True) + "\n")

    semantic_images_valid = (
        counts["known_ccw_image_slope_positive"] == N_PROBES
        and counts["known_cw_mirror_slope_negative"] == N_PROBES
        and counts["mirror_involution_byte_exact"] == N_PROBES
    )
    sign_anchor_valid = (
        counts["estimator_chi_ccw_positive"] == N_PROBES
        and counts["estimator_chi_mirror_negative"] == N_PROBES
        and counts["estimator_antisymmetry_value_exact"] == N_PROBES
    )
    result = {
        "scope": "synthetic 128x128 float32 images only; no survey image, real object, row, position, or sky statistic",
        "status": "PASS_BS5_SYNTHETIC_ABSOLUTE_SIGN_ANCHOR" if semantic_images_valid and sign_anchor_valid else "FAIL_BS5_SYNTHETIC_ABSOLUTE_SIGN_ANCHOR",
        "stage": stage,
        "execution_history": execution_history(),
        "frozen_sign_convention": FROZEN_SIGN_CONVENTION,
        "convention_changed": False,
        "estimator_sign_multiplier": ESTIMATOR_SIGN_MULTIPLIER,
        "estimator_corrected_after_precheck": stage == "post-correction",
        "wcs_parity_first": parity,
        "probe_set": {
            "master_seed": MASTER_SEED,
            "source_index_start": PROBE_INDEX_START,
            "source_index_end_inclusive": PROBE_INDEX_START + N_PROBES - 1,
            "seeds": [probe["seed"] for probe in probe_definitions()],
            "n": N_PROBES,
            "raster": [RASTER_SIZE, RASTER_SIZE],
            "dtype": "float32",
            "apparent_winding": "CCW East-of-North on North-up/East-left raster",
            "mirror": "pure width-axis pixel-index reversal",
            "image_and_mirror_manifest_sha256": image_manifest.hexdigest(),
            "parameter_policy": "fixed hash-derived pitch/inclination/SNR inside frozen synthetic support; no retry or replacement",
        },
        "counts": counts,
        "semantic_image_validation": "PASS" if semantic_images_valid else "FAIL",
        "absolute_sign_anchor": "PASS" if sign_anchor_valid else "FAIL",
        "estimator_chi_summary": {
            "min": min(estimator_values),
            "max": max(estimator_values),
            "mean": float(np.mean(estimator_values)),
        },
        "frozen_estimator": {
            "weights_file_sha256": EXPECTED_HASHES[WEIGHTS],
            "canonical_parameter_sha256_after_strict_load": canonical_hash,
            "tau": FROZEN_TAU,
            "null_manifest_sha256": EXPECTED_NULL_MANIFEST,
            "retrained": False,
            "reexported": False,
            "finetuned": False,
            "tau_recalibrated": False,
        },
        "frozen_input_verification_before": frozen_before,
        "records": {
            "path": str(records_path.relative_to(ROOT)),
            "rows": N_PROBES,
            "sha256": sha256_file(records_path),
        },
        "environment": {
            "python": sys.version,
            "platform": platform.platform(),
            "numpy": np.__version__,
            "torch": torch.__version__,
            "torch_threads": torch.get_num_threads(),
            "torch_interop_threads": torch.get_num_interop_threads(),
            "deterministic_algorithms": torch.are_deterministic_algorithms_enabled(),
            "device": "cpu",
        },
        "boundaries": {
            "real_sky_data": False,
            "real_object_rows": False,
            "real_images": False,
            "sky_positions": False,
            "sky_statistic": False,
            "training_or_retraining": False,
            "weight_reexport": False,
            "threshold_tuning": False,
            "technical_execution_rerun_after_pre_result_serialization_error": True,
            "probe_selection_tuning_or_replacement": False,
            "convention_change": False,
            "acceptance_or_freeze": False,
            "publication": False,
            "commit_or_push": False,
        },
    }
    stage_path = OUT / f"{stage.replace('-', '_')}_results.json"
    stage_path.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    result["stage_result_sha256"] = sha256_file(stage_path)
    if stage == "post-correction":
        pre_path = OUT / "pre_correction_results.json"
        if not pre_path.is_file():
            raise SystemExit("POST-CORRECTION RUN REQUIRES PRESERVED PRE-CORRECTION RESULT")
        pre = json.loads(pre_path.read_text(encoding="utf-8"))
        result["pre_correction_preserved"] = {
            "path": str(pre_path.relative_to(ROOT)),
            "sha256": sha256_file(pre_path),
            "status": pre["status"],
            "estimator_sign_multiplier": pre["estimator_sign_multiplier"],
            "counts": pre["counts"],
        }
    final_path = OUT / "results.json"
    final_path.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    frozen_after = verify_frozen_inputs()
    if frozen_after != frozen_before:
        raise SystemExit("FROZEN INPUTS CHANGED DURING RUN")
    print(json.dumps(result, indent=2, sort_keys=True), flush=True)
    if not (semantic_images_valid and sign_anchor_valid):
        raise SystemExit(2)
    return result


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--stage", choices=("pre-correction", "post-correction"), default="pre-correction")
    args = parser.parse_args()
    run(args.stage)


if __name__ == "__main__":
    main()
