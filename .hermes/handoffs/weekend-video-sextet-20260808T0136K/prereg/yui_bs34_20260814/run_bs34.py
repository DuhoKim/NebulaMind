#!/usr/bin/env python3
"""Fill BS-3 identity-count custody and BS-4 secondary-instrument receipts.

Synthetic-only, load-only execution. The primary model is loaded from frozen weights;
the secondary is the frozen deterministic geometry code. No training, calibration,
tuning, survey access, object-row access, sky statistic, acceptance, or publication.
"""
from __future__ import annotations

import hashlib
import importlib.util
import json
import os
import platform
import sys
import time
from pathlib import Path

import numpy as np
import torch

ROOT = Path(
    "/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/"
    "weekend-video-sextet-20260808T0136K"
)
OUT = ROOT / "prereg/yui_bs34_20260814"
BASE_RUNNER_PATH = ROOT / "prereg/yui_bs3_r4_r5_20260813/run_bs3_r4_r5.py"
GENERATOR_PATH = ROOT / "spike/yui_identity/w_chi.py"
WEIGHTS_PATH = ROOT / "prereg/weights_frozen.pt"
TRAIN_RESULTS_PATH = ROOT / "prereg/train_results.json"
RECEIPT_RESULTS_PATH = ROOT / "prereg/receipt_results.json"
RETENTION_RESULTS_PATH = ROOT / "prereg/yui_inclination_retention_remeasure_20260812/results.json"
SECONDARY_RUNNER_PATH = ROOT / "prereg/yui_receipt_run.py"
SECONDARY_SPIKE_RUNNER_PATH = ROOT / "spike/yui_identity/run_identity_test.py"
SECONDARY_SPIKE_RESULTS_PATH = ROOT / "spike/yui_identity/results.json"
SECONDARY_SPIKE_RECEIPT_PATH = ROOT / "spike/YUI_IDENTITY_UNITTEST_RECEIPT_20260812.md"
KUN_REGATE_PATH = ROOT / "prereg/KUN_REGATE_BS1_BS3_20260814.md"
PREREG_PATH = ROOT / "prereg/PREREG_LONGO_AMPLITUDE_TEST_20260812.md"
PRIMARY_RECEIPT_PATH = ROOT / "prereg/YUI_PRODUCTION_ESTIMATOR_RECEIPT_20260812.md"

N_IDENTITY_PROBES = 1000
PROBE_SOURCE_INDEX_START = 3_000_000
PRIMARY_TAU = 4.4006456017494235
SECONDARY_TAU = 5.916292121766702
R4_THRESHOLD = 0.01
EXPECTED_PREFIX_200_MANIFEST = "ab75d5f2ec08ad44fbcf1198d1612c23759f8d3aac29db044a181346ac43f9b2"
EXPECTED_HASHES = {
    BASE_RUNNER_PATH: "de0f35355902f25497e240a413a087a1413d365342419b0be3fc15a7e5117914",
    GENERATOR_PATH: "89da33ec6260e75e06eadb0f171da4c52f1478b59ff5e543d363dbf56fefcd75",
    WEIGHTS_PATH: "83008c1cbdae511af5d30020540e1e281c62c2bd95d3cb05527fc0687bf49e6d",
    TRAIN_RESULTS_PATH: "c36cd33001e432c60df786da8c0ff95b8ef5ab350a458b29d71ff084178a41fd",
    RECEIPT_RESULTS_PATH: "d5d4a8bc005b031ed523e64a672237536896f37030722fd5cf71ff44a3405a04",
    RETENTION_RESULTS_PATH: "414fbc5cb6fa050390f0a6bca69e02e81795ed2a3585928be19767f4cb3a59e2",
    SECONDARY_RUNNER_PATH: "eb41680c8425135662bf9d18cad1a12a4c752c137672f179e3e140f48656a028",
    SECONDARY_SPIKE_RUNNER_PATH: "c44813b73ee3cb92895d3d29c71c64d0a9860d5650e0cec4567ee215b12182e5",
    SECONDARY_SPIKE_RESULTS_PATH: "9e95861f8e02113ae97681f572b93a8dcbc27f16fa22214fb7971d3a0becab61",
    SECONDARY_SPIKE_RECEIPT_PATH: "fc2d99f23cb8ac720558f14bc94537faffd4d3f9f1f810f840220c9be0b60c55",
    KUN_REGATE_PATH: "e5bc40fc4368d813649534dd50dd9fe686b6200c244e7ffe4a457602ba483a66",
    PREREG_PATH: "ac43490054b159610385b8faac28dc4e3178161fadd97d66aa0418a1186b7590",
    PRIMARY_RECEIPT_PATH: "b4e2f5b5f92fc881ec2a0a35e84515fd05057c1051bff516cad7acae3609e18a",
}
EXPECTED_CANONICAL_WEIGHTS = "1075a4d91c295d7f3256128534a0b8c4d097fb9d162169df1ac698843637a589"
EXPECTED_NULL_MANIFEST = "1963132f2f36e7aa42b08012aad02d2c541d6c0973740a5bbce6a6e7a2904bd1"
EXPECTED_MASTER_SEED = "LONGO-AMPLITUDE-FREEZE-M1"


def load_module(path: Path, name: str):
    spec = importlib.util.spec_from_file_location(name, path)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"cannot load module spec: {path}")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


base = load_module(BASE_RUNNER_PATH, "bs3_r4_r5_base")
sys.path.insert(0, str(GENERATOR_PATH.parent))
from w_chi import bits as bits64  # noqa: E402
from w_chi import chi as secondary_chi_float64  # noqa: E402
from w_chi import mirror as secondary_mirror  # noqa: E402
from w_chi import synth_disk, synth_spiral, w as secondary_w  # noqa: E402


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def identity_source_indices() -> list[int]:
    return list(range(PROBE_SOURCE_INDEX_START, PROBE_SOURCE_INDEX_START + N_IDENTITY_PROBES))


def ordered_accept(value: np.float32, tau: float) -> bool:
    return bool(abs(value) > tau)


def secondary_chi_from_raw(raw_x: float, raw_mirror_x: float) -> np.float32:
    return np.float32(
        (np.float32(raw_x) - np.float32(raw_mirror_x)) / np.float32(2.0)
    )


def sign_pair_contribution(raw_x: float, raw_mirror_x: float) -> float:
    return float((np.sign(raw_x) + np.sign(raw_mirror_x)) / 2.0)


def secondary_raw(image_float32: np.ndarray) -> np.float32:
    return np.float32(secondary_w(np.ascontiguousarray(image_float32, dtype=np.float32)))


def secondary_chi_production(image_float32: np.ndarray) -> np.float32:
    image = np.ascontiguousarray(image_float32, dtype=np.float32)
    mirrored = np.ascontiguousarray(secondary_mirror(image))
    return secondary_chi_from_raw(secondary_raw(image), secondary_raw(mirrored))


def primary_chi_production(model, image_float32: np.ndarray) -> np.float32:
    image = np.ascontiguousarray(image_float32, dtype=np.float32)
    mirrored = np.ascontiguousarray(base.pure_index_mirror(image))
    raw_x = base.raw_output(model, image)
    raw_mirror = base.raw_output(model, mirrored)
    return np.float32((raw_x - raw_mirror) / np.float32(2.0))


def direct_hashes() -> dict[str, str]:
    return {str(path.relative_to(ROOT)): sha256_file(path) for path in EXPECTED_HASHES}


def verify_frozen_inputs() -> dict:
    actual = direct_hashes()
    mismatches = {
        str(path.relative_to(ROOT)): {
            "expected": expected,
            "actual": actual[str(path.relative_to(ROOT))],
        }
        for path, expected in EXPECTED_HASHES.items()
        if actual[str(path.relative_to(ROOT))] != expected
    }
    if mismatches:
        raise SystemExit("FROZEN INPUT HASH MISMATCH\n" + json.dumps(mismatches, indent=2))

    train = json.loads(TRAIN_RESULTS_PATH.read_text())
    receipt = json.loads(RECEIPT_RESULTS_PATH.read_text())
    retention = json.loads(RETENTION_RESULTS_PATH.read_text())
    spike = json.loads(SECONDARY_SPIKE_RESULTS_PATH.read_text())
    checks = {
        "master_seed": receipt["master_seed"] == EXPECTED_MASTER_SEED,
        "primary_tau": train["tau"] == PRIMARY_TAU,
        "secondary_tau": receipt["secondary_retention"]["tau"] == SECONDARY_TAU,
        "null_manifest": (
            receipt["null_manifest"]["manifest_sha256"] == EXPECTED_NULL_MANIFEST
            and receipt["null_manifest"]["n"] == 8000
        ),
        "canonical_weights_record": train["weights_sha256_canonical"] == EXPECTED_CANONICAL_WEIGHTS,
        "primary_retention_full_support": (
            retention["measurement"]["overall"]["accepted"] == 10_349
            and retention["measurement"]["overall"]["n"] == 12_000
            and retention["measurement"]["overall"]["retention"] == 0.8624166666666667
            and retention["measurement"]["overall"]["retention_lower95_one_sided_wilson"]
            == 0.8571626782674123
        ),
        "secondary_historical_production_retention": (
            receipt["secondary_retention"]["retention_central"] == 0.0013333333333333333
            and receipt["secondary_retention"]["n"] == 12_000
        ),
        "secondary_spike_abstention": spike["E_calibration"]["overall_abstention_spirals"] == 0.922,
    }
    if not all(checks.values()):
        raise SystemExit("FROZEN VALUE MISMATCH\n" + json.dumps(checks, indent=2))
    return {"hashes": actual, "value_checks": checks}


def snr_bin(value: float) -> str:
    for low, high, label in (
        (2.0, 5.0, "2-5"),
        (5.0, 10.0, "5-10"),
        (10.0, 20.0, "10-20"),
        (20.0, 50.0001, "20-50"),
    ):
        if low <= value < high:
            return label
    raise ValueError(f"S/N outside frozen support: {value}")


def summarize_bin(counts: dict[str, list[int]]) -> dict:
    return {
        label: {
            "accepted": pair[0],
            "n": pair[1],
            "retention": pair[0] / pair[1] if pair[1] else None,
            "abstention": 1.0 - pair[0] / pair[1] if pair[1] else None,
        }
        for label, pair in counts.items()
    }


def main() -> None:
    started = time.time()
    OUT.mkdir(parents=True, exist_ok=True)
    frozen_before = verify_frozen_inputs()
    torch.set_num_threads(1)
    torch.set_num_interop_threads(1)
    torch.use_deterministic_algorithms(True)
    model = base.build_and_load_model()
    canonical_hash = base.canonical_parameter_hash(model)
    if canonical_hash != EXPECTED_CANONICAL_WEIGHTS:
        raise SystemExit(f"CANONICAL WEIGHTS HASH MISMATCH: {canonical_hash}")

    records_path = OUT / "identity_probe_records.jsonl"
    manifest_1000 = hashlib.sha256()
    manifest_prefix_200 = hashlib.sha256()
    counters = {
        "r1": 0,
        "primary_value": 0,
        "primary_bits": 0,
        "primary_nonzero": 0,
        "primary_zero": 0,
        "secondary_value": 0,
        "secondary_bits": 0,
        "secondary_nonzero": 0,
        "secondary_zero": 0,
        "secondary_accept": 0,
    }
    primary_max_residual = 0.0
    secondary_max_residual = 0.0
    secondary_contributions: list[float] = []
    secondary_canary_residuals: list[float] = []
    secondary_by_snr = {label: [0, 0] for label in ("2-5", "5-10", "10-20", "20-50")}

    with records_path.open("w", encoding="utf-8") as records:
        for offset, source_index in enumerate(identity_source_indices()):
            parity, pitch_deg, inclination_deg, snr = base.params(source_index)
            image_float64 = synth_spiral(
                parity,
                pitch_deg,
                inclination_deg,
                snr,
                seed=base.sample_seed(source_index),
            )
            image = np.ascontiguousarray(image_float64, dtype=np.float32)
            image_sha = hashlib.sha256(image.tobytes()).hexdigest()
            manifest_1000.update(bytes.fromhex(image_sha))
            if offset < 200:
                manifest_prefix_200.update(bytes.fromhex(image_sha))
            mirrored = np.ascontiguousarray(base.pure_index_mirror(image))
            r1 = base.pure_index_mirror(base.pure_index_mirror(image)).tobytes() == image.tobytes()
            counters["r1"] += int(r1)

            primary_chi_x = primary_chi_production(model, image)
            primary_chi_mirror = primary_chi_production(model, mirrored)
            primary_neg = np.float32(-primary_chi_x)
            primary_value = bool(primary_chi_mirror == primary_neg)
            primary_bit = base.bits32(primary_chi_mirror) == base.bits32(primary_neg)
            primary_residual = float(abs(np.float64(primary_chi_mirror) + np.float64(primary_chi_x)))
            primary_max_residual = max(primary_max_residual, primary_residual)
            counters["primary_value"] += int(primary_value)
            counters["primary_bits"] += int(primary_bit)
            counters["primary_zero"] += int(primary_chi_x == np.float32(0.0))
            counters["primary_nonzero"] += int(primary_chi_x != np.float32(0.0))

            secondary_raw_x = secondary_raw(image)
            secondary_raw_mirror = secondary_raw(mirrored)
            secondary_chi_x = secondary_chi_from_raw(secondary_raw_x, secondary_raw_mirror)
            secondary_chi_mirror = secondary_chi_production(mirrored)
            secondary_neg = np.float32(-secondary_chi_x)
            secondary_value = bool(secondary_chi_mirror == secondary_neg)
            secondary_bit = base.bits32(secondary_chi_mirror) == base.bits32(secondary_neg)
            secondary_residual = float(abs(np.float64(secondary_chi_mirror) + np.float64(secondary_chi_x)))
            secondary_max_residual = max(secondary_max_residual, secondary_residual)
            counters["secondary_value"] += int(secondary_value)
            counters["secondary_bits"] += int(secondary_bit)
            counters["secondary_zero"] += int(secondary_chi_x == np.float32(0.0))
            counters["secondary_nonzero"] += int(secondary_chi_x != np.float32(0.0))
            secondary_accepted = ordered_accept(secondary_chi_x, SECONDARY_TAU)
            counters["secondary_accept"] += int(secondary_accepted)
            label = snr_bin(snr)
            secondary_by_snr[label][0] += int(secondary_accepted)
            secondary_by_snr[label][1] += 1
            contribution = sign_pair_contribution(secondary_raw_x, secondary_raw_mirror)
            secondary_contributions.append(contribution)

            bad_input = base.bad_interpolating_mirror(image)
            secondary_chi_bad = secondary_chi_production(bad_input)
            canary_residual = float(
                abs(np.float64(secondary_chi_bad) + np.float64(secondary_chi_x))
            )
            secondary_canary_residuals.append(canary_residual)

            record = {
                "probe_offset": offset,
                "source_index": source_index,
                "image_sha256_float32": image_sha,
                "parity": parity,
                "pitch_deg": pitch_deg,
                "inclination_deg": inclination_deg,
                "snr": snr,
                "R1_mirror_involution_byte_exact": r1,
                "primary_chi_x_float32": float(primary_chi_x),
                "primary_chi_x_bits": base.bits32(primary_chi_x),
                "primary_chi_mirror_float32": float(primary_chi_mirror),
                "primary_chi_mirror_bits": base.bits32(primary_chi_mirror),
                "primary_R2_value_exact": primary_value,
                "primary_R2_bit_exact": primary_bit,
                "primary_identity_residual": primary_residual,
                "secondary_raw_w_x_float32": float(secondary_raw_x),
                "secondary_raw_w_mirror_float32": float(secondary_raw_mirror),
                "secondary_chi_x_float32": float(secondary_chi_x),
                "secondary_chi_x_bits": base.bits32(secondary_chi_x),
                "secondary_chi_mirror_float32": float(secondary_chi_mirror),
                "secondary_chi_mirror_bits": base.bits32(secondary_chi_mirror),
                "secondary_R2_value_exact": secondary_value,
                "secondary_R2_bit_exact": secondary_bit,
                "secondary_identity_residual": secondary_residual,
                "secondary_accepted_at_frozen_tau": secondary_accepted,
                "secondary_dA_raw_contribution": contribution,
                "secondary_R4_chi_bad_input_float32": float(secondary_chi_bad),
                "secondary_R4_abs_identity_violation": canary_residual,
                "secondary_R4_exceeds_0_01": canary_residual > R4_THRESHOLD,
            }
            records.write(json.dumps(record, sort_keys=True) + "\n")

    if manifest_prefix_200.hexdigest() != EXPECTED_PREFIX_200_MANIFEST:
        raise SystemExit(
            "PROBE PREFIX CUSTODY MISMATCH: "
            f"{manifest_prefix_200.hexdigest()} != {EXPECTED_PREFIX_200_MANIFEST}"
        )

    sym64 = synth_disk(30.0, 1e9, seed=7)
    sym32 = np.ascontiguousarray((sym64 + secondary_mirror(sym64)) / 2.0, dtype=np.float32)
    primary_sym = primary_chi_production(model, sym32)
    primary_sym_mirror = primary_chi_production(
        model, np.ascontiguousarray(base.pure_index_mirror(sym32))
    )
    secondary_sym = secondary_chi_production(sym32)
    secondary_sym_mirror = secondary_chi_production(
        np.ascontiguousarray(secondary_mirror(sym32))
    )

    receipt = json.loads(RECEIPT_RESULTS_PATH.read_text())
    spike = json.loads(SECONDARY_SPIKE_RESULTS_PATH.read_text())
    historical_secondary = receipt["secondary_retention"]
    historical_spike = spike["E_calibration"]
    contributions = secondary_contributions
    contribution_counts = {
        str(value): contributions.count(value) for value in sorted(set(contributions))
    }
    canary_count = sum(value > R4_THRESHOLD for value in secondary_canary_residuals)
    primary_valid = (
        counters["r1"] == N_IDENTITY_PROBES
        and counters["primary_bits"] == N_IDENTITY_PROBES
    )
    secondary_valid = (
        counters["r1"] == N_IDENTITY_PROBES
        and counters["secondary_bits"] == N_IDENTITY_PROBES
    )
    results = {
        "scope": "synthetic instrument probes and aggregate frozen receipts only; no sky/survey/object data",
        "status": (
            "PASS_BS3_IDENTITY_AND_BS4_IDENTITY_VALIDITY"
            if primary_valid and secondary_valid
            else "FAIL_BS3_OR_BS4_IDENTITY_VALIDITY"
        ),
        "probe_set": {
            "definition": "one-shot 1,000-probe extension of the landed production R1/R2 prefix",
            "source_index_start": PROBE_SOURCE_INDEX_START,
            "source_index_end_inclusive": PROBE_SOURCE_INDEX_START + N_IDENTITY_PROBES - 1,
            "n": N_IDENTITY_PROBES,
            "master_seed": EXPECTED_MASTER_SEED,
            "raster": [128, 128],
            "dtype": "float32",
            "image_manifest_sha256": manifest_1000.hexdigest(),
            "prefix_200_manifest_sha256": manifest_prefix_200.hexdigest(),
            "prefix_matches_prior_production_receipt": True,
        },
        "BS3_primary_identity": {
            "validity_rule": "R1 and R2 bit-exact 1000/1000 on the promised production probe set",
            "verdict": "PASS" if primary_valid else "FAIL",
            "R1_mirror_involution_byte_exact": f'{counters["r1"]}/{N_IDENTITY_PROBES}',
            "R2_antisymmetry_value_exact": f'{counters["primary_value"]}/{N_IDENTITY_PROBES}',
            "R2_antisymmetry_bit_exact": f'{counters["primary_bits"]}/{N_IDENTITY_PROBES}',
            "R2_nonzero_cases": counters["primary_nonzero"],
            "R2_zero_cases": counters["primary_zero"],
            "max_abs_chi_mirror_plus_chi": primary_max_residual,
            "R3_signed_zero": {
                "chi_sym": float(primary_sym),
                "chi_mirror_bits": base.bits32(primary_sym_mirror),
                "neg_chi_bits": base.bits32(np.float32(-primary_sym)),
                "value_equal": bool(primary_sym_mirror == -primary_sym),
                "bit_equal": base.bits32(primary_sym_mirror) == base.bits32(np.float32(-primary_sym)),
                "ordered_acceptance_false": not ordered_accept(primary_sym, PRIMARY_TAU),
            },
            "frozen_weights_file_sha256": EXPECTED_HASHES[WEIGHTS_PATH],
            "frozen_weights_canonical_sha256": canonical_hash,
            "frozen_tau": PRIMARY_TAU,
            "operative_retention": {
                "accepted": 10_349,
                "n": 12_000,
                "central": 0.8624166666666667,
                "lower95_one_sided": 0.8571626782674123,
                "support": "uniform in cos(i), 0 to 69.3 degrees admitted by b/a > 0.4",
            },
        },
        "BS4_secondary_identity_and_abstention": {
            "validity_rule": "identity bit-exact; abstention published",
            "verdict": "PASS" if secondary_valid else "FAIL",
            "R1_mirror_involution_byte_exact": f'{counters["r1"]}/{N_IDENTITY_PROBES}',
            "R2_antisymmetry_value_exact": f'{counters["secondary_value"]}/{N_IDENTITY_PROBES}',
            "R2_antisymmetry_bit_exact": f'{counters["secondary_bits"]}/{N_IDENTITY_PROBES}',
            "R2_nonzero_cases": counters["secondary_nonzero"],
            "R2_zero_cases": counters["secondary_zero"],
            "max_abs_chi_mirror_plus_chi": secondary_max_residual,
            "R3_signed_zero": {
                "chi_sym": float(secondary_sym),
                "chi_mirror_bits": base.bits32(secondary_sym_mirror),
                "neg_chi_bits": base.bits32(np.float32(-secondary_sym)),
                "value_equal": bool(secondary_sym_mirror == -secondary_sym),
                "bit_equal": base.bits32(secondary_sym_mirror) == base.bits32(np.float32(-secondary_sym)),
                "ordered_acceptance_false": not ordered_accept(secondary_sym, SECONDARY_TAU),
            },
            "R4_interpolating_mirror_canary": {
                "formula": "abs(chi_secondary_production(m_bad(x)) + chi_secondary_production(x))",
                "threshold": R4_THRESHOLD,
                "n": N_IDENTITY_PROBES,
                "n_exceeding_threshold": canary_count,
                "min": min(secondary_canary_residuals),
                "max": max(secondary_canary_residuals),
                "mean": float(np.mean(secondary_canary_residuals)),
                "verdict": "PASS" if canary_count >= 1 else "FAIL",
            },
            "R5_raw_flip_imbalance": {
                "formula": "mean((sign(w(x)) + sign(w(mirror(x)))) / 2)",
                "dA_raw": float(np.mean(contributions)),
                "sum": float(np.sum(contributions)),
                "counts": contribution_counts,
            },
            "fresh_promised_probe_abstention": {
                "tau": SECONDARY_TAU,
                "accepted": counters["secondary_accept"],
                "n": N_IDENTITY_PROBES,
                "retention": counters["secondary_accept"] / N_IDENTITY_PROBES,
                "abstention": 1.0 - counters["secondary_accept"] / N_IDENTITY_PROBES,
                "by_snr": summarize_bin(secondary_by_snr),
            },
            "historical_production_heldout_abstention": {
                "source": "prereg/receipt_results.json::secondary_retention",
                "tau": historical_secondary["tau"],
                "accepted": round(
                    historical_secondary["retention_central"] * historical_secondary["n"]
                ),
                "n": historical_secondary["n"],
                "retention": historical_secondary["retention_central"],
                "abstention": 1.0 - historical_secondary["retention_central"],
                "retention_lower95": historical_secondary["retention_lower95"],
                "by_snr": historical_secondary["by_snr"],
                "support": "uniform in inclination on 0 to 60 degrees; not a full b/a > 0.4 support estimate",
            },
            "historical_spike_abstention": {
                "source": "spike/yui_identity/results.json::E_calibration",
                "tau": historical_spike["tau"],
                "n": 1000,
                "abstention": historical_spike["overall_abstention_spirals"],
                "by_snr": historical_spike["by_snr"],
                "reproducibility_caveat": (
                    "the historical runner used process-salted Python hash(...) for spiral noise seeds; "
                    "its landed result is pinned by file hash but exact probe noise is not reconstructible "
                    "from source without the missing PYTHONHASHSEED"
                ),
            },
            "algorithm_code_sha256": EXPECTED_HASHES[GENERATOR_PATH],
            "production_receipt_runner_sha256": EXPECTED_HASHES[SECONDARY_RUNNER_PATH],
            "frozen_tau": SECONDARY_TAU,
            "null_manifest_sha256": EXPECTED_NULL_MANIFEST,
        },
        "records": {
            "path": str(records_path.relative_to(ROOT)),
            "rows": N_IDENTITY_PROBES,
            "sha256": sha256_file(records_path),
        },
        "frozen_input_verification": frozen_before,
        "environment": {
            "python": sys.version,
            "platform": platform.platform(),
            "numpy": np.__version__,
            "torch": torch.__version__,
            "torch_threads": torch.get_num_threads(),
            "torch_interop_threads": torch.get_num_interop_threads(),
            "deterministic_algorithms": torch.are_deterministic_algorithms_enabled(),
            "pid": os.getpid(),
        },
        "elapsed_seconds": time.time() - started,
        "boundaries": {
            "real_sky_data": False,
            "real_object_rows": False,
            "sky_statistic": False,
            "tuning_or_retry_to_pass": False,
            "training_or_retraining": False,
            "tau_recalibration": False,
            "acceptance_or_freeze": False,
            "publication": False,
            "commit_or_push": False,
        },
    }
    results_path = OUT / "results.json"
    results_path.write_text(json.dumps(results, indent=2, sort_keys=True) + "\n")
    frozen_after = verify_frozen_inputs()
    if frozen_after != frozen_before:
        raise SystemExit("FROZEN INPUTS CHANGED DURING RUN")
    print(json.dumps(results, indent=2, sort_keys=True), flush=True)
    if not (primary_valid and secondary_valid):
        raise SystemExit(2)


if __name__ == "__main__":
    main()
