#!/usr/bin/env python3
"""Synthetic-only inclination retention remeasurement for the frozen estimator.

Boundary: no sky/catalogue/survey inputs. This script reads only the frozen local
weights, the local analytic synthetic generator, and the original machine receipt.
It does not retrain, recalibrate tau, or modify any frozen input.
"""
from __future__ import annotations

import hashlib
import json
import math
import os
import platform
import sys
import time
from pathlib import Path

import numpy as np
import torch
import torch.nn as nn

ROOT = Path("/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/weekend-video-sextet-20260808T0136K")
OUT = ROOT / "prereg/yui_inclination_retention_remeasure_20260812"
GENERATOR = ROOT / "spike/yui_identity/w_chi.py"
TRAIN_SCRIPT = ROOT / "prereg/yui_train_measure.py"
WEIGHTS = ROOT / "prereg/weights_frozen.pt"
ORIGINAL_RESULTS = ROOT / "prereg/train_results.json"
MASTER_SEED = "LONGO-AMPLITUDE-FREEZE-M1"
N_HELDOUT = 12_000
I_MAX_DEG = 69.3
TAU_EXPECTED = 4.4006456017494235
Z_ONE_SIDED_95 = 1.6448536269514722
INCLINATION_EDGES_DEG = [0.0, 15.0, 30.0, 45.0, 60.0, 65.0, 69.3]
SNR_EDGES = [2.0, 5.0, 10.0, 20.0, 50.0001]
EXPECTED_HASHES = {
    str(GENERATOR.relative_to(ROOT)): "89da33ec6260e75e06eadb0f171da4c52f1478b59ff5e543d363dbf56fefcd75",
    str(TRAIN_SCRIPT.relative_to(ROOT)): "653694dd72d6f30319336e948c787bafa958a3b181bed01b237a06d4f6c31f8a",
    str(WEIGHTS.relative_to(ROOT)): "83008c1cbdae511af5d30020540e1e281c62c2bd95d3cb05527fc0687bf49e6d",
    str(ORIGINAL_RESULTS.relative_to(ROOT)): "c36cd33001e432c60df786da8c0ff95b8ef5ab350a458b29d71ff084178a41fd",
}

sys.path.insert(0, str(GENERATOR.parent))
from w_chi import N, synth_spiral  # noqa: E402


def sha256_file(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()


def sample_seed(index: int) -> int:
    payload = f"{MASTER_SEED}||{index}".encode()
    return int.from_bytes(hashlib.sha256(payload).digest()[:8], "big") % (2**63)


def base_randoms(index: int) -> tuple[int, float, float, float]:
    """Return parity, pitch, raw inclination uniform, and S/N using the original draw order."""
    rng = np.random.default_rng(sample_seed(index))
    parity = int(rng.choice([1, -1]))
    pitch_deg = float(rng.uniform(10.0, 40.0))
    inclination_uniform = float(rng.uniform(0.0, 1.0))
    snr = float(np.exp(rng.uniform(np.log(2.0), np.log(50.0))))
    return parity, pitch_deg, inclination_uniform, snr


def original_params(index: int) -> tuple[int, float, float, float]:
    parity, pitch_deg, u, snr = base_randoms(index)
    return parity, pitch_deg, 60.0 * u, snr


def remeasure_params(index: int) -> tuple[int, float, float, float]:
    parity, pitch_deg, u, snr = base_randoms(index)
    # Uniform cos(i) on the population selected by 0 <= i <= 69.3 degrees.
    # Drawing cos(i) uniformly is the orientation-random measure.
    cos_min = math.cos(math.radians(I_MAX_DEG))
    cos_i = 1.0 - u * (1.0 - cos_min)
    inclination_deg = math.degrees(math.acos(cos_i))
    return parity, pitch_deg, inclination_deg, snr


class Block(nn.Module):
    def __init__(self, channels_in: int, channels_out: int, stride: int):
        super().__init__()
        self.conv1 = nn.Conv2d(channels_in, channels_out, 3, stride, 1, bias=False)
        self.bn1 = nn.BatchNorm2d(channels_out)
        self.conv2 = nn.Conv2d(channels_out, channels_out, 3, 1, 1, bias=False)
        self.bn2 = nn.BatchNorm2d(channels_out)
        if stride == 1 and channels_in == channels_out:
            self.shortcut = nn.Sequential()
        else:
            self.shortcut = nn.Sequential(
                nn.Conv2d(channels_in, channels_out, 1, stride, bias=False),
                nn.BatchNorm2d(channels_out),
            )

    def forward(self, x: torch.Tensor) -> torch.Tensor:
        import torch.nn.functional as functional
        y = functional.relu(self.bn1(self.conv1(x)))
        y = self.bn2(self.conv2(y))
        return functional.relu(y + self.shortcut(x))


class Trunk(nn.Module):
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
                    Block(incoming, widths[stage], 1 if stage == 0 else 2),
                    Block(widths[stage], widths[stage], 1),
                ]
            )
        layers.extend([nn.AdaptiveAvgPool2d(1), nn.Flatten(), nn.Linear(256, 1)])
        self.features = nn.Sequential(*layers)

    def forward(self, x: torch.Tensor) -> torch.Tensor:
        return self.features(x).squeeze(-1)


def build_and_load_model() -> Trunk:
    # yui_train_measure.py used short attribute names; state-dict keys therefore need the
    # exact original class layout. Rebuild that layout explicitly, without importing the
    # training script (which would retrain as an import side effect).
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

    model = OriginalTrunk()
    state = torch.load(WEIGHTS, map_location="cpu", weights_only=True)
    model.load_state_dict(state, strict=True)
    model.eval()
    return model


def bits32(value: float | np.float32) -> int:
    return int(np.float32(value).view(np.uint32))


def chi_net(model: nn.Module, image: np.ndarray) -> np.float32:
    contiguous = np.ascontiguousarray(image, dtype=np.float32)
    with torch.no_grad():
        tensor = torch.from_numpy(contiguous)[None, None]
        a = model(tensor).item()
        b = model(torch.flip(tensor, dims=[3])).item()
    return np.float32((a - b) / 2.0)


def wilson_lower(successes: int, trials: int) -> float | None:
    if trials == 0:
        return None
    p = successes / trials
    z = Z_ONE_SIDED_95
    denominator = 1.0 + z * z / trials
    center = p + z * z / (2.0 * trials)
    radius = z * math.sqrt(p * (1.0 - p) / trials + z * z / (4.0 * trials * trials))
    return (center - radius) / denominator


def blank_counter() -> dict[str, int]:
    return {"n": 0, "accepted": 0, "correct_accepted": 0}


def finish_counter(counter: dict[str, int]) -> dict[str, int | float | None]:
    n = counter["n"]
    accepted = counter["accepted"]
    correct = counter["correct_accepted"]
    return {
        **counter,
        "retention": accepted / n if n else None,
        "retention_lower95_one_sided_wilson": wilson_lower(accepted, n),
        "accepted_sign_accuracy": correct / accepted if accepted else None,
        "accepted_sign_accuracy_lower95_one_sided_wilson": wilson_lower(correct, accepted),
    }


def inclination_key(inclination_deg: float) -> str:
    for low, high in zip(INCLINATION_EDGES_DEG[:-1], INCLINATION_EDGES_DEG[1:]):
        is_last = high == INCLINATION_EDGES_DEG[-1]
        if low <= inclination_deg < high or (is_last and inclination_deg <= high):
            return f"{low:.1f}-{high:.1f}"
    raise ValueError(f"inclination out of frozen range: {inclination_deg}")


def snr_key(snr: float) -> str:
    for low, high in zip(SNR_EDGES[:-1], SNR_EDGES[1:]):
        if low <= snr < high:
            return f"{low:g}-{int(high)}"
    raise ValueError(f"S/N out of frozen range: {snr}")


def evaluate_population(
    model: nn.Module,
    param_fn,
    *,
    write_records: bool,
    test_high_inclination_identity: bool,
) -> tuple[dict, str | None]:
    overall = blank_counter()
    by_inclination = {
        f"{low:.1f}-{high:.1f}": blank_counter()
        for low, high in zip(INCLINATION_EDGES_DEG[:-1], INCLINATION_EDGES_DEG[1:])
    }
    by_snr = {
        f"{low:g}-{int(high)}": blank_counter()
        for low, high in zip(SNR_EDGES[:-1], SNR_EDGES[1:])
    }
    high = blank_counter()
    high_identity = {
        "tested": 0,
        "mirror_involution_byte_exact": 0,
        "antisymmetry_value_exact": 0,
        "antisymmetry_bit_exact_nonzero": 0,
        "nonzero_chi": 0,
        "signed_zero_cases": 0,
        "max_abs_residual": 0.0,
    }
    image_manifest = hashlib.sha256()
    records_path = OUT / "records.jsonl"
    records_file = records_path.open("w", encoding="utf-8") if write_records else None
    parity_counts = {"+1": 0, "-1": 0}
    inclination_sum = 0.0
    try:
        for offset in range(N_HELDOUT):
            source_index = 2_000_000 + offset
            parity, pitch_deg, inclination_deg, snr = param_fn(source_index)
            image = synth_spiral(
                parity,
                pitch_deg,
                inclination_deg,
                snr,
                seed=sample_seed(source_index),
            ).astype(np.float32)
            image_sha = hashlib.sha256(image.tobytes()).hexdigest()
            image_manifest.update(bytes.fromhex(image_sha))
            chi = chi_net(model, image)
            accepted = bool(abs(chi) > TAU_EXPECTED)
            correct = bool(accepted and np.sign(chi) == parity)
            parity_counts[f"{parity:+d}"] += 1
            inclination_sum += inclination_deg
            for counter in (overall, by_inclination[inclination_key(inclination_deg)], by_snr[snr_key(snr)]):
                counter["n"] += 1
                counter["accepted"] += int(accepted)
                counter["correct_accepted"] += int(correct)
            if inclination_deg > 60.0:
                high["n"] += 1
                high["accepted"] += int(accepted)
                high["correct_accepted"] += int(correct)
                if test_high_inclination_identity:
                    mirrored = np.ascontiguousarray(np.fliplr(image))
                    chi_mirror = chi_net(model, mirrored)
                    neg_chi = np.float32(-chi)
                    high_identity["tested"] += 1
                    high_identity["mirror_involution_byte_exact"] += int(
                        np.fliplr(np.fliplr(image)).tobytes() == image.tobytes()
                    )
                    high_identity["antisymmetry_value_exact"] += int(chi_mirror == neg_chi)
                    residual = float(abs(np.float64(chi_mirror) + np.float64(chi)))
                    high_identity["max_abs_residual"] = max(
                        high_identity["max_abs_residual"], residual
                    )
                    if chi != np.float32(0.0):
                        high_identity["nonzero_chi"] += 1
                        high_identity["antisymmetry_bit_exact_nonzero"] += int(
                            bits32(chi_mirror) == bits32(neg_chi)
                        )
                    else:
                        high_identity["signed_zero_cases"] += 1
            if records_file is not None:
                records_file.write(
                    json.dumps(
                        {
                            "offset": offset,
                            "source_index": source_index,
                            "image_sha256_float32": image_sha,
                            "parity": parity,
                            "pitch_deg": pitch_deg,
                            "inclination_deg": inclination_deg,
                            "snr": snr,
                            "chi_float32": float(chi),
                            "chi_bits_uint32_hex": f"0x{bits32(chi):08x}",
                            "accepted": accepted,
                            "accepted_sign_correct": correct,
                        },
                        sort_keys=True,
                    )
                    + "\n"
                )
            if (offset + 1) % 1000 == 0:
                print(f"evaluated {offset + 1}/{N_HELDOUT}", flush=True)
    finally:
        if records_file is not None:
            records_file.close()
    result = {
        "overall": finish_counter(overall),
        "by_inclination_deg": {key: finish_counter(value) for key, value in by_inclination.items()},
        "high_inclination_60_to_69_3_deg": finish_counter(high),
        "by_snr": {key: finish_counter(value) for key, value in by_snr.items()},
        "parity_counts": parity_counts,
        "mean_inclination_deg": inclination_sum / N_HELDOUT,
        "image_manifest_sha256": image_manifest.hexdigest(),
        "high_inclination_identity": high_identity,
    }
    return result, sha256_file(records_path) if write_records else None


def run_edge_identity(model: nn.Module, n_edge: int = 256) -> dict:
    receipt = {
        "inclination_deg": I_MAX_DEG,
        "tested": 0,
        "mirror_involution_byte_exact": 0,
        "antisymmetry_value_exact": 0,
        "antisymmetry_bit_exact_nonzero": 0,
        "nonzero_chi": 0,
        "signed_zero_cases": 0,
        "max_abs_residual": 0.0,
        "accepted": 0,
        "correct_accepted": 0,
    }
    for offset in range(n_edge):
        index = 4_000_000 + offset
        parity, pitch_deg, _, snr = base_randoms(index)
        image = synth_spiral(
            parity,
            pitch_deg,
            I_MAX_DEG,
            snr,
            seed=sample_seed(index),
        ).astype(np.float32)
        mirrored = np.ascontiguousarray(np.fliplr(image))
        chi = chi_net(model, image)
        chi_mirror = chi_net(model, mirrored)
        neg_chi = np.float32(-chi)
        accepted = bool(abs(chi) > TAU_EXPECTED)
        receipt["tested"] += 1
        receipt["mirror_involution_byte_exact"] += int(
            np.fliplr(np.fliplr(image)).tobytes() == image.tobytes()
        )
        receipt["antisymmetry_value_exact"] += int(chi_mirror == neg_chi)
        receipt["max_abs_residual"] = max(
            receipt["max_abs_residual"],
            float(abs(np.float64(chi_mirror) + np.float64(chi))),
        )
        receipt["accepted"] += int(accepted)
        receipt["correct_accepted"] += int(accepted and np.sign(chi) == parity)
        if chi != np.float32(0.0):
            receipt["nonzero_chi"] += 1
            receipt["antisymmetry_bit_exact_nonzero"] += int(
                bits32(chi_mirror) == bits32(neg_chi)
            )
        else:
            receipt["signed_zero_cases"] += 1
    receipt["retention"] = receipt["accepted"] / n_edge
    receipt["accepted_sign_accuracy"] = (
        receipt["correct_accepted"] / receipt["accepted"] if receipt["accepted"] else None
    )
    return receipt


def main() -> None:
    started = time.time()
    OUT.mkdir(parents=True, exist_ok=True)
    actual_hashes = {
        str(path.relative_to(ROOT)): sha256_file(path)
        for path in (GENERATOR, TRAIN_SCRIPT, WEIGHTS, ORIGINAL_RESULTS)
    }
    if actual_hashes != EXPECTED_HASHES:
        raise SystemExit(
            "FROZEN INPUT HASH MISMATCH\n"
            + json.dumps({"expected": EXPECTED_HASHES, "actual": actual_hashes}, indent=2)
        )
    original = json.loads(ORIGINAL_RESULTS.read_text())
    if original["tau"] != TAU_EXPECTED:
        raise SystemExit("frozen tau mismatch")

    torch.set_num_threads(1)
    torch.set_num_interop_threads(1)
    torch.use_deterministic_algorithms(True)
    model = build_and_load_model()

    # First reproduce the original 12,000-row aggregate. This verifies that the load-only
    # reconstruction matches the frozen production estimator before measuring the new population.
    print("reproducing original uniform-in-i held-out aggregate", flush=True)
    original_reproduced, _ = evaluate_population(
        model,
        original_params,
        write_records=False,
        test_high_inclination_identity=False,
    )
    expected_accepted = round(original["retention_central"] * original["n_heldout"])
    reproduction_pass = (
        original_reproduced["overall"]["n"] == original["n_heldout"]
        and original_reproduced["overall"]["accepted"] == expected_accepted
        and original_reproduced["overall"]["correct_accepted"] == expected_accepted
    )
    if not reproduction_pass:
        raise SystemExit(
            "ORIGINAL AGGREGATE REPRODUCTION FAILED\n"
            + json.dumps(
                {
                    "expected_n": original["n_heldout"],
                    "expected_accepted": expected_accepted,
                    "reproduced": original_reproduced["overall"],
                },
                indent=2,
            )
        )

    print("measuring new uniform-in-cos(i) 0-69.3 degree population", flush=True)
    measured, records_sha = evaluate_population(
        model,
        remeasure_params,
        write_records=True,
        test_high_inclination_identity=True,
    )
    edge_identity = run_edge_identity(model)

    results = {
        "scope": "synthetic-only; no sky/catalogue/survey data",
        "measurement_status": "COMPLETED_SYNTHETIC_REMEASUREMENT_NOT_ACCEPTED",
        "frozen_estimator": {
            "weights_path": str(WEIGHTS.relative_to(ROOT)),
            "weights_sha256": actual_hashes[str(WEIGHTS.relative_to(ROOT))],
            "canonical_weights_sha256": original["weights_sha256_canonical"],
            "tau": TAU_EXPECTED,
            "tau_recalibrated": False,
            "weights_retrained_or_modified": False,
        },
        "original_sampling_audit": {
            "source_path": str(TRAIN_SCRIPT.relative_to(ROOT)),
            "source_sha256": actual_hashes[str(TRAIN_SCRIPT.relative_to(ROOT))],
            "training_and_heldout_inclination_draw": "uniform in inclination degrees on [0,60]",
            "evidence": "params(): float(r.uniform(0,60)) at yui_train_measure.py line 10",
            "null_inclination_draw": "same params(i)[2], therefore uniform in inclination degrees on [0,60]",
            "original_n_heldout": original["n_heldout"],
            "original_expected_accepted": expected_accepted,
            "original_reproduced": original_reproduced["overall"],
            "aggregate_reproduction_pass": reproduction_pass,
        },
        "remeasurement_population": {
            "n": N_HELDOUT,
            "inclination_range_deg": [0.0, I_MAX_DEG],
            "inclination_sampling": "uniform in cos(i), conditional on 0 <= i <= 69.3 degrees",
            "inclination_edges_deg_frozen_before_run": INCLINATION_EDGES_DEG,
            "same_heldout_source_indices_and_noise_seed_stream_as_original": True,
            "only_inclination_transform_changed_in_parameter draw": True,
            "generator_limit": "analytic y-coordinate squeeze; not a realism validation for edge-on arm blending",
        },
        "measurement": measured,
        "edge_69_3_degree_identity": edge_identity,
        "input_hashes": actual_hashes,
        "records": {
            "path": str((OUT / "records.jsonl").relative_to(ROOT)),
            "sha256": records_sha,
            "rows": N_HELDOUT,
        },
        "environment": {
            "python": sys.version,
            "platform": platform.platform(),
            "numpy": np.__version__,
            "torch": torch.__version__,
            "torch_num_threads": torch.get_num_threads(),
            "torch_num_interop_threads": torch.get_num_interop_threads(),
            "deterministic_algorithms": torch.are_deterministic_algorithms_enabled(),
            "pid": os.getpid(),
        },
        "elapsed_seconds": time.time() - started,
    }
    (OUT / "results.json").write_text(json.dumps(results, indent=2, sort_keys=True) + "\n")
    print(json.dumps(results, indent=2, sort_keys=True), flush=True)


if __name__ == "__main__":
    main()
