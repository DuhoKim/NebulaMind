#!/usr/bin/env python3
"""Run missing BS-3 production-estimator receipts R4 and R5 on synthetics only.

This is a load-only instrument run. It fails closed on every pinned frozen input,
never imports the training script, never retrains, never recalibrates tau, and
never reads survey, catalogue, coordinate, or sky-image data.
"""
from __future__ import annotations

import hashlib
import json
import os
import platform
import sys
import time
from pathlib import Path
from typing import Iterable

import numpy as np
import torch
import torch.nn as nn
from scipy.ndimage import affine_transform

ROOT = Path(
    "/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/"
    "weekend-video-sextet-20260808T0136K"
)
OUT = ROOT / "prereg/yui_bs3_r4_r5_20260813"
GENERATOR = ROOT / "spike/yui_identity/w_chi.py"
WEIGHTS = ROOT / "prereg/weights_frozen.pt"
TRAIN_RESULTS = ROOT / "prereg/train_results.json"
RECEIPT_RESULTS = ROOT / "prereg/receipt_results.json"
RETENTION_RESULTS = ROOT / "prereg/yui_inclination_retention_remeasure_20260812/results.json"
MASTER_SEED = "LONGO-AMPLITUDE-FREEZE-M1"
TAU = 4.4006456017494235
N_PROBES = 200
PROBE_SOURCE_INDEX_START = 3_000_000
R4_THRESHOLD = 0.01
EXPECTED = {
    "generator_sha256": "89da33ec6260e75e06eadb0f171da4c52f1478b59ff5e543d363dbf56fefcd75",
    "weights_file_sha256": "83008c1cbdae511af5d30020540e1e281c62c2bd95d3cb05527fc0687bf49e6d",
    "weights_canonical_sha256": "1075a4d91c295d7f3256128534a0b8c4d097fb9d162169df1ac698843637a589",
    "train_results_sha256": "c36cd33001e432c60df786da8c0ff95b8ef5ab350a458b29d71ff084178a41fd",
    "receipt_results_sha256": "d5d4a8bc005b031ed523e64a672237536896f37030722fd5cf71ff44a3405a04",
    "retention_results_sha256": "414fbc5cb6fa050390f0a6bca69e02e81795ed2a3585928be19767f4cb3a59e2",
    "null_manifest_sha256": "1963132f2f36e7aa42b08012aad02d2c541d6c0973740a5bbce6a6e7a2904bd1",
}

sys.path.insert(0, str(GENERATOR.parent))
from w_chi import N, synth_spiral  # noqa: E402


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def sample_seed(index: int) -> int:
    payload = f"{MASTER_SEED}||{index}".encode()
    return int.from_bytes(hashlib.sha256(payload).digest()[:8], "big") % (2**63)


def params(index: int) -> tuple[int, float, float, float]:
    rng = np.random.default_rng(sample_seed(index))
    return (
        int(rng.choice([1, -1])),
        float(rng.uniform(10.0, 40.0)),
        float(rng.uniform(0.0, 60.0)),
        float(np.exp(rng.uniform(np.log(2.0), np.log(50.0)))),
    )


def pure_index_mirror(image: np.ndarray) -> np.ndarray:
    return np.fliplr(image)


def bad_interpolating_mirror(image: np.ndarray) -> np.ndarray:
    """The feasibility spike's deliberate bad mirror, reproduced verbatim.

    Reflection is displaced 0.25 pixel from the grid centreline, forcing
    bilinear resampling. This is a canary only and never enters production chi.
    """
    transformed = affine_transform(
        image,
        [[1.0, 0.0], [0.0, -1.0]],
        offset=[0.0, (image.shape[1] - 1) + 0.5],
        order=1,
        mode="nearest",
    )
    return np.ascontiguousarray(transformed, dtype=np.float32)


def flip_imbalance_contribution(raw_x: float, raw_mirror: float) -> float:
    return float((np.sign(raw_x) + np.sign(raw_mirror)) / 2.0)


def canary_passes(residuals: Iterable[float]) -> bool:
    return any(value > R4_THRESHOLD for value in residuals)


def canary_identity_residual(
    raw_x: float,
    raw_mirror_x: float,
    raw_bad_x: float,
    raw_mirror_bad_x: float,
) -> float:
    """Replay the spike canary with frozen production chi on a bad-mirrored input."""
    chi_x = np.float32(
        (np.float32(raw_x) - np.float32(raw_mirror_x)) / np.float32(2.0)
    )
    chi_bad_x = np.float32(
        (np.float32(raw_bad_x) - np.float32(raw_mirror_bad_x)) / np.float32(2.0)
    )
    return float(abs(np.float64(chi_bad_x) + np.float64(chi_x)))


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

    def forward(self, x: torch.Tensor) -> torch.Tensor:
        import torch.nn.functional as functional

        return functional.relu(
            self.b2(self.c2(functional.relu(self.b1(self.c1(x))))) + self.sh(x)
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

    def forward(self, x: torch.Tensor) -> torch.Tensor:
        return self.f(x).squeeze(-1)


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
        value = model(torch.from_numpy(contiguous)[None, None]).item()
    return np.float32(value)


def bits32(value: float | np.float32) -> str:
    return f"0x{int(np.float32(value).view(np.uint32)):08x}"


def verify_frozen_inputs() -> dict:
    actual = {
        "generator_sha256": sha256_file(GENERATOR),
        "weights_file_sha256": sha256_file(WEIGHTS),
        "train_results_sha256": sha256_file(TRAIN_RESULTS),
        "receipt_results_sha256": sha256_file(RECEIPT_RESULTS),
        "retention_results_sha256": sha256_file(RETENTION_RESULTS),
    }
    for key, value in actual.items():
        if value != EXPECTED[key]:
            raise SystemExit(f"FROZEN INPUT HASH MISMATCH: {key}: {value}")

    train_result = json.loads(TRAIN_RESULTS.read_text())
    receipt_result = json.loads(RECEIPT_RESULTS.read_text())
    retention_result = json.loads(RETENTION_RESULTS.read_text())
    checks = {
        "master_seed_matches": receipt_result["master_seed"] == MASTER_SEED,
        "tau_matches": train_result["tau"] == TAU,
        "null_manifest_matches": (
            receipt_result["null_manifest"]["manifest_sha256"]
            == EXPECTED["null_manifest_sha256"]
            and receipt_result["null_manifest"]["tag"] == "null-8000"
            and receipt_result["null_manifest"]["n"] == 8000
        ),
        "stored_canonical_hash_matches": (
            train_result["weights_sha256_canonical"]
            == EXPECTED["weights_canonical_sha256"]
        ),
        "operative_retention_matches": (
            retention_result["measurement"]["overall"]["accepted"] == 10_349
            and retention_result["measurement"]["overall"]["n"] == 12_000
            and retention_result["measurement"]["overall"]["retention"]
            == 0.8624166666666667
            and retention_result["measurement"]["overall"][
                "retention_lower95_one_sided_wilson"
            ]
            == 0.8571626782674123
        ),
    }
    if not all(checks.values()):
        raise SystemExit("FROZEN RECEIPT VALUE MISMATCH\n" + json.dumps(checks, indent=2))
    return {"hashes": actual, "value_checks": checks}


def main() -> None:
    started = time.time()
    OUT.mkdir(parents=True, exist_ok=True)
    frozen_before = verify_frozen_inputs()

    torch.set_num_threads(1)
    torch.set_num_interop_threads(1)
    torch.use_deterministic_algorithms(True)
    model = build_and_load_model()
    canonical_hash = canonical_parameter_hash(model)
    if canonical_hash != EXPECTED["weights_canonical_sha256"]:
        raise SystemExit(f"CANONICAL WEIGHTS HASH MISMATCH: {canonical_hash}")

    records_path = OUT / "paired_probe_records.jsonl"
    probe_manifest = hashlib.sha256()
    residuals: list[float] = []
    contributions: list[float] = []
    pure_r1 = 0
    pure_r2_value = 0
    pure_r2_bits_nonzero = 0
    pure_r2_nonzero = 0
    pure_r2_signed_zero = 0
    pure_max_residual = 0.0
    acceptance_mismatches = 0
    abs_chi_delta_max = 0.0

    with records_path.open("w", encoding="utf-8") as records:
        for probe_offset in range(N_PROBES):
            source_index = PROBE_SOURCE_INDEX_START + probe_offset
            parity, pitch_deg, inclination_deg, snr = params(source_index)
            image = synth_spiral(
                parity,
                pitch_deg,
                inclination_deg,
                snr,
                seed=sample_seed(source_index),
            ).astype(np.float32)
            image_sha = hashlib.sha256(image.tobytes()).hexdigest()
            probe_manifest.update(bytes.fromhex(image_sha))

            mirrored = np.ascontiguousarray(pure_index_mirror(image))
            raw_x = raw_output(model, image)
            raw_mirror = raw_output(model, mirrored)
            chi_x = np.float32((raw_x - raw_mirror) / np.float32(2.0))
            chi_mirror = np.float32((raw_mirror - raw_x) / np.float32(2.0))
            neg_chi_x = np.float32(-chi_x)
            accepted_x = bool(abs(chi_x) > TAU)
            accepted_mirror = bool(abs(chi_mirror) > TAU)
            d_a_contribution = flip_imbalance_contribution(raw_x, raw_mirror)
            contributions.append(d_a_contribution)

            pure_r1 += int(
                pure_index_mirror(pure_index_mirror(image)).tobytes()
                == image.tobytes()
            )
            pure_r2_value += int(chi_mirror == neg_chi_x)
            pure_residual = float(abs(np.float64(chi_mirror) + np.float64(chi_x)))
            pure_max_residual = max(pure_max_residual, pure_residual)
            if chi_x != np.float32(0.0):
                pure_r2_nonzero += 1
                pure_r2_bits_nonzero += int(bits32(chi_mirror) == bits32(neg_chi_x))
            else:
                pure_r2_signed_zero += 1
            acceptance_mismatches += int(accepted_x != accepted_mirror)
            abs_chi_delta = float(abs(abs(np.float64(chi_x)) - abs(np.float64(chi_mirror))))
            abs_chi_delta_max = max(abs_chi_delta_max, abs_chi_delta)

            bad_once = bad_interpolating_mirror(image)
            raw_bad_once = raw_output(model, bad_once)
            pure_mirror_bad_once = np.ascontiguousarray(pure_index_mirror(bad_once))
            raw_mirror_bad_once = raw_output(model, pure_mirror_bad_once)
            chi_production_bad_input = np.float32(
                (raw_bad_once - raw_mirror_bad_once) / np.float32(2.0)
            )
            bad_residual = canary_identity_residual(
                raw_x,
                raw_mirror,
                raw_bad_once,
                raw_mirror_bad_once,
            )
            residuals.append(bad_residual)

            record = {
                "probe_offset": probe_offset,
                "source_index": source_index,
                "image_sha256_float32": image_sha,
                "parity": parity,
                "pitch_deg": pitch_deg,
                "inclination_deg": inclination_deg,
                "snr": snr,
                "raw_f_x_float32": float(raw_x),
                "raw_f_mirror_x_float32": float(raw_mirror),
                "raw_sign_x": int(np.sign(raw_x)),
                "raw_sign_mirror_x": int(np.sign(raw_mirror)),
                "dA_raw_contribution": d_a_contribution,
                "chi_x_float32": float(chi_x),
                "chi_x_bits_uint32_hex": bits32(chi_x),
                "chi_mirror_x_float32": float(chi_mirror),
                "chi_mirror_x_bits_uint32_hex": bits32(chi_mirror),
                "pure_identity_residual": pure_residual,
                "accepted_x_at_frozen_tau": accepted_x,
                "accepted_mirror_x_at_frozen_tau": accepted_mirror,
                "acceptance_mismatch": accepted_x != accepted_mirror,
                "abs_chi_pair_delta": abs_chi_delta,
                "r4_bad_raw_f_once_float32": float(raw_bad_once),
                "r4_raw_f_pure_mirror_of_bad_once_float32": float(raw_mirror_bad_once),
                "r4_production_chi_of_bad_input_float32": float(chi_production_bad_input),
                "r4_abs_identity_violation": bad_residual,
                "r4_exceeds_0_01": bad_residual > R4_THRESHOLD,
            }
            records.write(json.dumps(record, sort_keys=True) + "\n")

    contribution_counts = {
        str(value): contributions.count(value) for value in sorted(set(contributions))
    }
    results = {
        "scope": "synthetic-only; no sky/catalogue/survey data",
        "status": "COMPLETED_R4_R5_INSTRUMENT_RECEIPTS_NOT_FREEZE_ACCEPTANCE",
        "frozen_instrument": {
            "master_seed": MASTER_SEED,
            "generator_sha256": EXPECTED["generator_sha256"],
            "weights_file_sha256": EXPECTED["weights_file_sha256"],
            "weights_canonical_sha256": canonical_hash,
            "tau": TAU,
            "null_manifest_sha256": EXPECTED["null_manifest_sha256"],
            "weights_retrained_or_modified": False,
            "tau_recalibrated_or_retuned": False,
            "training_set_regenerated": False,
        },
        "probe_set": {
            "definition": "same 200 deterministic production probes used by R1/R2",
            "source_index_start_inclusive": PROBE_SOURCE_INDEX_START,
            "source_index_end_inclusive": PROBE_SOURCE_INDEX_START + N_PROBES - 1,
            "n": N_PROBES,
            "raster": [N, N],
            "dtype": "float32",
            "image_manifest_sha256": probe_manifest.hexdigest(),
        },
        "production_path_recheck": {
            "mirror": "pure width-axis pixel-index reversal",
            "R1_mirror_involution_byte_exact": f"{pure_r1}/{N_PROBES}",
            "R2_antisymmetry_value_exact": f"{pure_r2_value}/{N_PROBES}",
            "R2_nonzero_pairs": pure_r2_nonzero,
            "R2_antisymmetry_bit_exact_nonzero": (
                f"{pure_r2_bits_nonzero}/{pure_r2_nonzero}"
            ),
            "R2_signed_zero_cases": pure_r2_signed_zero,
            "max_abs_chi_mirror_plus_chi": pure_max_residual,
            "acceptance_mismatches_at_frozen_tau": acceptance_mismatches,
            "max_abs_chi_pair_delta": abs_chi_delta_max,
        },
        "R4_interpolating_mirror_canary": {
            "canary_transform": (
                "scipy.ndimage.affine_transform reflection displaced 0.25 pixel "
                "from grid centreline; bilinear interpolation order=1; mode=nearest"
            ),
            "pass_rule": "at least one abs(chi_production(m_bad(x)) + chi_production(x)) > 0.01",
            "threshold": R4_THRESHOLD,
            "n_probes": N_PROBES,
            "n_exceeding_threshold": sum(value > R4_THRESHOLD for value in residuals),
            "min_abs_identity_violation": min(residuals),
            "max_abs_identity_violation": max(residuals),
            "mean_abs_identity_violation": float(np.mean(residuals)),
            "verdict": "PASS_CANARY_DETECTS_INTERPOLATING_MIRROR"
            if canary_passes(residuals)
            else "FAIL_CANARY_DID_NOT_DETECT_INTERPOLATING_MIRROR",
        },
        "R5_flip_imbalance": {
            "formula": "mean((sign(f(x)) + sign(f(mirror(x)))) / 2)",
            "n_probes": N_PROBES,
            "dA_raw": float(np.mean(contributions)),
            "sum_contributions": float(np.sum(contributions)),
            "contribution_counts": contribution_counts,
            "per_object_outputs_published_in": str(records_path.relative_to(ROOT)),
            "acceptance_mismatches_at_frozen_tau": acceptance_mismatches,
            "interpretation": (
                "raw-trunk flip imbalance before architectural antisymmetrization; "
                "not a sky statistic and not the antisymmetrized estimator output"
            ),
        },
        "operative_retention": {
            "population": "uniform in cos(i), 0 <= i <= 69.3 degrees admitted by b/a > 0.4",
            "accepted": 10_349,
            "n": 12_000,
            "retention": 0.8624166666666667,
            "retention_percent_rounded": 86.24,
            "lower95_one_sided_wilson": 0.8571626782674123,
            "lower95_percent_rounded": 85.72,
            "superseded_number_not_operational": (
                "96.44% / 96.15% came from synthetics uniform in inclination on 0-60 degrees"
            ),
        },
        "input_verification": frozen_before,
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
            "scipy_affine_transform_module": affine_transform.__module__,
            "torch_num_threads": torch.get_num_threads(),
            "torch_num_interop_threads": torch.get_num_interop_threads(),
            "deterministic_algorithms": torch.are_deterministic_algorithms_enabled(),
            "pid": os.getpid(),
        },
        "elapsed_seconds": time.time() - started,
        "boundaries": {
            "sky_run": False,
            "acceptance_or_freeze_decision": False,
            "publication": False,
            "commit": False,
        },
    }
    if results["R4_interpolating_mirror_canary"]["verdict"].startswith("FAIL"):
        raise SystemExit(json.dumps(results["R4_interpolating_mirror_canary"], indent=2))
    results_path = OUT / "results.json"
    results_path.write_text(json.dumps(results, indent=2, sort_keys=True) + "\n")

    frozen_after = verify_frozen_inputs()
    if frozen_after != frozen_before:
        raise SystemExit("FROZEN INPUTS CHANGED DURING RUN")
    print(json.dumps(results, indent=2, sort_keys=True), flush=True)


if __name__ == "__main__":
    main()
