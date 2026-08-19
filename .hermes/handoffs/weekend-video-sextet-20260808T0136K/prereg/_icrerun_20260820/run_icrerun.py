#!/usr/bin/env python3
"""Synthetic-only IC-path R1-R5 and retention rerun.

This runner imports the hash-pinned production input-contract implementation from
_cutout_runner_20260820/cutout_runner.py. It never reimplements IC-1..IC-7 and
has no acquisition, catalogue, coordinate, FITS, or network input.
"""
from __future__ import annotations

import hashlib
import importlib.util
import json
import math
import os
import platform
import sys
import time
from pathlib import Path

import numpy as np
import torch

ROOT = Path(__file__).resolve().parent.parent
OUT = ROOT / "_icrerun_20260820"
HANDOFF_ROOT = ROOT.parent
CUTOUT_PATH = ROOT / "_cutout_runner_20260820/cutout_runner.py"
SLOTS_PATH = ROOT / "_cutout_runner_20260820/ic_slots.json"
SCALER_PATH = OUT / "ic5_scaler.py"
BASE_RUNNER_PATH = ROOT / "yui_bs3_r4_r5_20260813/run_bs3_r4_r5.py"
RETENTION_RUNNER_PATH = ROOT / "yui_inclination_retention_remeasure_20260812/run_remeasure.py"
GENERATOR_PATH = HANDOFF_ROOT / "spike/yui_identity/w_chi.py"
WEIGHTS_PATH = ROOT / "weights_frozen.pt"
TRAIN_RESULTS_PATH = ROOT / "train_results.json"
RECEIPT_RESULTS_PATH = ROOT / "receipt_results.json"
OLD_IDENTITY_RESULTS_PATH = ROOT / "yui_bs34_20260814/results.json"
OLD_RETENTION_RESULTS_PATH = ROOT / "yui_inclination_retention_remeasure_20260812/results.json"
OLD_R4_R5_RESULTS_PATH = ROOT / "yui_bs3_r4_r5_20260813/results.json"
AMENDMENT_PATH = ROOT / "LANA_PC1_INPUT_AMENDMENT_20260815.md"
APPENDIX_PATH = ROOT / "YUI_PRODUCTION_ESTIMATOR_APPENDIX_20260812.md"

MASTER_SEED = "LONGO-AMPLITUDE-FREEZE-M1"
TAU = 4.4006456017494235
R4_THRESHOLD = 0.01
IDENTITY_START = 3_000_000
N_IDENTITY = 1000
N_R4_R5 = 200
RETENTION_START = 2_000_000
N_RETENTION = 12_000
EXPECTED_IDENTITY_MANIFEST = "35d679d4955d3657866bd64fe309a9a42b30ff8a61d1952d2a3795ee59231024"
EXPECTED_PREFIX_MANIFEST = "ab75d5f2ec08ad44fbcf1198d1612c23759f8d3aac29db044a181346ac43f9b2"
EXPECTED_RETENTION_MANIFEST = "bb60b69b17b24424af47667367312c1915cd0b8986336865a741fe70f80933d0"
EXPECTED_CANONICAL_WEIGHTS = "1075a4d91c295d7f3256128534a0b8c4d097fb9d162169df1ac698843637a589"
EXPECTED_HASHES = {
    AMENDMENT_PATH: "519ab5ba33c5e9d670b5654fb41f6941293c5d969c5515fb0284ebe8d52d70fb",
    APPENDIX_PATH: "331a941a807eef2f02e821086230655505b332b90ff1e47ff128d034334f9fc3",
    CUTOUT_PATH: "ccb9b8fed457333669e54fa9f0a3dac645dc866a56c6cd8dc665ffd4d93b1bcc",
    SCALER_PATH: "21b66eda899b5e48034be2b2d92ee2c77f262b156eb59d680eb1b80763d12621",
    BASE_RUNNER_PATH: "de0f35355902f25497e240a413a087a1413d365342419b0be3fc15a7e5117914",
    RETENTION_RUNNER_PATH: "15de0ea82baab8dd8115d5707f897fdfcc86e6287dc4cb8fb4affa327da66ca7",
    GENERATOR_PATH: "89da33ec6260e75e06eadb0f171da4c52f1478b59ff5e543d363dbf56fefcd75",
    WEIGHTS_PATH: "83008c1cbdae511af5d30020540e1e281c62c2bd95d3cb05527fc0687bf49e6d",
    TRAIN_RESULTS_PATH: "c36cd33001e432c60df786da8c0ff95b8ef5ab350a458b29d71ff084178a41fd",
    RECEIPT_RESULTS_PATH: "d5d4a8bc005b031ed523e64a672237536896f37030722fd5cf71ff44a3405a04",
    OLD_IDENTITY_RESULTS_PATH: "cfd11391f123e0caa054f0a3bdfab76b20eb7293c457bafd70563e90af07df33",
    OLD_RETENTION_RESULTS_PATH: "414fbc5cb6fa050390f0a6bca69e02e81795ed2a3585928be19767f4cb3a59e2",
    OLD_R4_R5_RESULTS_PATH: "bb4eef8798893a0ce8e06c09768e20d683ca771c5b7dfb396fd7747a86efea78",
}


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1 << 20), b""):
            digest.update(chunk)
    return digest.hexdigest()


def load_module(path: Path, expected: str, name: str):
    actual = sha256_file(path)
    if actual != expected:
        raise SystemExit(f"PIN MISMATCH {path}: {actual} != {expected}")
    spec = importlib.util.spec_from_file_location(name, path)
    if spec is None or spec.loader is None:
        raise SystemExit(f"cannot import pinned module {path}")
    module = importlib.util.module_from_spec(spec)
    sys.modules[name] = module
    spec.loader.exec_module(module)
    return module


cutout = load_module(CUTOUT_PATH, EXPECTED_HASHES[CUTOUT_PATH], "icrerun_production_cutout_runner")
base = load_module(BASE_RUNNER_PATH, EXPECTED_HASHES[BASE_RUNNER_PATH], "icrerun_old_bs3_runner")
retention_base = load_module(
    RETENTION_RUNNER_PATH,
    EXPECTED_HASHES[RETENTION_RUNNER_PATH],
    "icrerun_old_retention_runner",
)
generator = load_module(
    GENERATOR_PATH,
    EXPECTED_HASHES[GENERATOR_PATH],
    "icrerun_frozen_bs3_generator",
)


def bits32(value: float | np.float32) -> str:
    return f"0x{int(np.float32(value).view(np.uint32)):08x}"


def canonical_hash(model: torch.nn.Module) -> str:
    digest = hashlib.sha256()
    for parameter in model.parameters():
        digest.update(parameter.detach().numpy().astype("<f4").tobytes())
    return digest.hexdigest()


def verify_pins() -> dict[str, str]:
    actual = {str(path.relative_to(HANDOFF_ROOT)): sha256_file(path) for path in EXPECTED_HASHES}
    expected = {str(path.relative_to(HANDOFF_ROOT)): digest for path, digest in EXPECTED_HASHES.items()}
    if actual != expected:
        raise SystemExit("FROZEN INPUT HASH MISMATCH\n" + json.dumps({"expected": expected, "actual": actual}, indent=2))
    slots = json.loads(SLOTS_PATH.read_text(encoding="utf-8"))
    scaling = slots["ic5_scaling_map"]
    slot_checks = {
        "ic4_cap_zero": slots["ic4_invalid_fraction_cap"] == 0.0,
        "scaler_path": Path(scaling["module_path"]) == SCALER_PATH,
        "scaler_hash": scaling["module_sha256"] == EXPECTED_HASHES[SCALER_PATH],
        "callable": scaling["callable"] == "scale",
        "constants": scaling["constants"] == {
            "form": "tensor = float32(nanomaggy)",
            "gain": 1.0,
            "offset": 0.0,
        },
    }
    if not all(slot_checks.values()):
        raise SystemExit("IC SLOT VALUE MISMATCH\n" + json.dumps(slot_checks, indent=2))
    train = json.loads(TRAIN_RESULTS_PATH.read_text())
    receipt = json.loads(RECEIPT_RESULTS_PATH.read_text())
    if train["tau"] != TAU or receipt["master_seed"] != MASTER_SEED:
        raise SystemExit("frozen tau or master seed mismatch")
    return actual


def apply_contract(image: np.ndarray) -> tuple[np.ndarray, dict]:
    return cutout.apply_input_contract(image, slots_path=SLOTS_PATH, real_sky=False)


def raw_pair(model: torch.nn.Module, tensor: np.ndarray) -> tuple[np.float32, np.float32]:
    mirrored = cutout.mirror_tensor(tensor)
    return base.raw_output(model, tensor[0]), base.raw_output(model, mirrored[0])


def chi_from_pair(raw_x: np.float32, raw_mirror: np.float32) -> np.float32:
    return np.float32((raw_x - raw_mirror) / np.float32(2.0))


def old_chi(model: torch.nn.Module, image: np.ndarray) -> np.float32:
    raw_x = base.raw_output(model, np.ascontiguousarray(image, dtype=np.float32))
    raw_mirror = base.raw_output(model, np.ascontiguousarray(np.fliplr(image), dtype=np.float32))
    return chi_from_pair(raw_x, raw_mirror)


def write_json(path: Path, value: object) -> None:
    path.write_text(json.dumps(value, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def self_test() -> dict:
    monotone = np.linspace(-8.0, 8.0, 128 * 128, dtype=np.float32).reshape(128, 128)
    tensor, receipt = apply_contract(monotone)
    exact = tensor[0].tobytes() == monotone.tobytes()
    monotone_ok = bool(np.all(np.diff(tensor[0].ravel().astype(np.float64)) >= 0.0))
    involution = cutout.mirror_tensor(cutout.mirror_tensor(tensor)).tobytes() == tensor.tobytes()
    one_invalid = monotone.copy()
    one_invalid[0, 0] = np.nan
    invalid_failed = False
    invalid_code = None
    try:
        apply_contract(one_invalid)
    except cutout.ContractError as exc:
        invalid_failed = True
        invalid_code = exc.code
    result = {
        "synthetic_monotone_grid_exact_bytes": exact,
        "synthetic_monotone_grid_order_preserved": monotone_ok,
        "ic7_involution": involution,
        "zero_invalid_receipt_fraction": receipt["invalid_fraction"],
        "one_invalid_fraction": 1.0 / (128 * 128),
        "one_invalid_fails_closed": invalid_failed,
        "one_invalid_failure_code": invalid_code,
    }
    if not (exact and monotone_ok and involution and invalid_failed and invalid_code == "FAILED_IC4_INVALID_FRACTION_CAP"):
        raise SystemExit("IC SELF TEST FAILED\n" + json.dumps(result, indent=2))
    return result


def main() -> None:
    started = time.time()
    OUT.mkdir(parents=True, exist_ok=True)
    frozen_before = verify_pins()
    slot_sha = sha256_file(SLOTS_PATH)
    slot_validation = self_test()

    torch.set_num_threads(1)
    torch.set_num_interop_threads(1)
    torch.use_deterministic_algorithms(True)
    model = base.build_and_load_model()
    loaded_canonical_hash = canonical_hash(model)
    if loaded_canonical_hash != EXPECTED_CANONICAL_WEIGHTS:
        raise SystemExit(f"canonical weights mismatch: {loaded_canonical_hash}")

    identity_records_path = OUT / "r1_r5_records.jsonl"
    identity_manifest = hashlib.sha256()
    prefix_manifest = hashlib.sha256()
    tensor_manifest = hashlib.sha256()
    r1 = r2_value = r2_bits = old_new_chi_bits = mirror_placement_bytes = 0
    max_identity_residual = 0.0
    invalid_count_identity = 0
    r4_residuals: list[float] = []
    r5_contributions: list[float] = []
    r5_acceptance_mismatches = 0

    with identity_records_path.open("w", encoding="utf-8") as records:
        for offset in range(N_IDENTITY):
            source_index = IDENTITY_START + offset
            parity, pitch_deg, inclination_deg, snr = base.params(source_index)
            old_image = np.ascontiguousarray(
                base.synth_spiral(
                    parity,
                    pitch_deg,
                    inclination_deg,
                    snr,
                    seed=base.sample_seed(source_index),
                ),
                dtype=np.float32,
            )
            image_sha = hashlib.sha256(old_image.tobytes()).hexdigest()
            identity_manifest.update(bytes.fromhex(image_sha))
            if offset < N_R4_R5:
                prefix_manifest.update(bytes.fromhex(image_sha))
            invalid_count = int(np.count_nonzero(~np.isfinite(old_image)))
            invalid_count_identity += invalid_count
            tensor, ic_receipt = apply_contract(old_image)
            tensor_sha = hashlib.sha256(tensor.tobytes()).hexdigest()
            tensor_manifest.update(bytes.fromhex(tensor_sha))
            exact_input = tensor[0].tobytes() == old_image.tobytes()
            if not exact_input:
                raise SystemExit(f"IC-5 identity map changed probe bytes at {source_index}")
            mirrored = cutout.mirror_tensor(tensor)
            restored = cutout.mirror_tensor(mirrored)
            r1_ok = restored.tobytes() == tensor.tobytes()
            r1 += int(r1_ok)
            mirrored_raw, _ = apply_contract(np.ascontiguousarray(np.fliplr(old_image)))
            placement_ok = mirrored.tobytes() == mirrored_raw.tobytes()
            mirror_placement_bytes += int(placement_ok)

            raw_x, raw_mirror = raw_pair(model, tensor)
            chi_x = chi_from_pair(raw_x, raw_mirror)
            raw_mirror_again, raw_restored = raw_pair(model, mirrored)
            chi_mirror = chi_from_pair(raw_mirror_again, raw_restored)
            neg_chi = np.float32(-chi_x)
            value_ok = bool(chi_mirror == neg_chi)
            bits_ok = bits32(chi_mirror) == bits32(neg_chi)
            r2_value += int(value_ok)
            r2_bits += int(bits_ok)
            residual = float(abs(np.float64(chi_mirror) + np.float64(chi_x)))
            max_identity_residual = max(max_identity_residual, residual)
            old_value = old_chi(model, old_image)
            old_new_ok = bits32(old_value) == bits32(chi_x)
            old_new_chi_bits += int(old_new_ok)

            row = {
                "probe_offset": offset,
                "source_index": source_index,
                "image_sha256_float32": image_sha,
                "tensor_sha256_float32": tensor_sha,
                "invalid_pixel_count": invalid_count,
                "invalid_fraction": ic_receipt["invalid_fraction"],
                "input_bytes_equal_old_path": exact_input,
                "R1_involution_byte_exact": r1_ok,
                "IC7_mirror_placement_byte_exact": placement_ok,
                "chi_old_path_float32": float(old_value),
                "chi_old_path_bits": bits32(old_value),
                "chi_new_path_float32": float(chi_x),
                "chi_new_path_bits": bits32(chi_x),
                "chi_new_mirror_float32": float(chi_mirror),
                "chi_new_mirror_bits": bits32(chi_mirror),
                "R2_value_exact": value_ok,
                "R2_bit_exact": bits_ok,
                "old_new_chi_bit_identical": old_new_ok,
                "identity_residual": residual,
            }
            if offset < N_R4_R5:
                bad_old = base.bad_interpolating_mirror(old_image)
                bad_tensor, _ = apply_contract(bad_old)
                bad_raw_x, bad_raw_mirror = raw_pair(model, bad_tensor)
                chi_bad = chi_from_pair(bad_raw_x, bad_raw_mirror)
                r4_residual = float(abs(np.float64(chi_bad) + np.float64(chi_x)))
                r4_residuals.append(r4_residual)
                contribution = float((np.sign(raw_x) + np.sign(raw_mirror)) / 2.0)
                r5_contributions.append(contribution)
                accepted_x = bool(abs(chi_x) > TAU)
                accepted_mirror = bool(abs(chi_mirror) > TAU)
                r5_acceptance_mismatches += int(accepted_x != accepted_mirror)
                row.update({
                    "parity": parity,
                    "pitch_deg": pitch_deg,
                    "inclination_deg": inclination_deg,
                    "snr": snr,
                    "raw_f_x_float32": float(raw_x),
                    "raw_f_mirror_float32": float(raw_mirror),
                    "R4_abs_identity_violation": r4_residual,
                    "R4_exceeds_0_01": r4_residual > R4_THRESHOLD,
                    "R5_contribution": contribution,
                    "accepted_x": accepted_x,
                    "accepted_mirror": accepted_mirror,
                })
            records.write(json.dumps(row, sort_keys=True) + "\n")

    if identity_manifest.hexdigest() != EXPECTED_IDENTITY_MANIFEST:
        raise SystemExit("identity generator manifest mismatch")
    if prefix_manifest.hexdigest() != EXPECTED_PREFIX_MANIFEST:
        raise SystemExit("R4/R5 prefix generator manifest mismatch")

    sym64 = generator.synth_disk(30.0, 1e9, seed=7)
    sym_old = np.ascontiguousarray((sym64 + np.fliplr(sym64)) / 2.0, dtype=np.float32)
    sym_tensor, _ = apply_contract(sym_old)
    sym_raw_x, sym_raw_mirror = raw_pair(model, sym_tensor)
    sym_chi = chi_from_pair(sym_raw_x, sym_raw_mirror)
    sym_mirrored = cutout.mirror_tensor(sym_tensor)
    sym_m_raw_x, sym_m_raw_mirror = raw_pair(model, sym_mirrored)
    sym_chi_mirror = chi_from_pair(sym_m_raw_x, sym_m_raw_mirror)
    r3 = {
        "chi": float(sym_chi),
        "chi_bits": bits32(sym_chi),
        "chi_mirror": float(sym_chi_mirror),
        "chi_mirror_bits": bits32(sym_chi_mirror),
        "neg_chi_bits": bits32(np.float32(-sym_chi)),
        "value_equal": bool(sym_chi_mirror == -sym_chi),
        "bit_equal": bits32(sym_chi_mirror) == bits32(np.float32(-sym_chi)),
        "ordered_acceptance_false": not bool(abs(sym_chi) > TAU),
        "input_bytes_equal_old_path": sym_tensor[0].tobytes() == sym_old.tobytes(),
    }

    r4_count = sum(value > R4_THRESHOLD for value in r4_residuals)
    contribution_counts = {str(value): r5_contributions.count(value) for value in sorted(set(r5_contributions))}
    r1_r5 = {
        "probe_set": {
            "source_index_start": IDENTITY_START,
            "source_index_end_inclusive": IDENTITY_START + N_IDENTITY - 1,
            "n": N_IDENTITY,
            "master_seed": MASTER_SEED,
            "generator_manifest_sha256": identity_manifest.hexdigest(),
            "old_receipt_generator_manifest_sha256": EXPECTED_IDENTITY_MANIFEST,
            "prefix_200_manifest_sha256": prefix_manifest.hexdigest(),
        },
        "R1": {"byte_exact": r1, "n": N_IDENTITY, "old_quantity": "1000/1000"},
        "R2": {
            "value_exact": r2_value,
            "bit_exact": r2_bits,
            "n": N_IDENTITY,
            "max_abs_chi_mirror_plus_chi": max_identity_residual,
            "old_quantity": "1000/1000 bit-exact; max residual 0.0",
        },
        "R3": {**r3, "old_quantity": "+0.0 vs -0.0 bits; value-equal; ordered rejection"},
        "R4": {
            "formula": "abs(chi_production_full_path(m_bad(x)) + chi_production_full_path(x))",
            "n": N_R4_R5,
            "threshold": R4_THRESHOLD,
            "n_exceeding_threshold": r4_count,
            "min": min(r4_residuals),
            "max": max(r4_residuals),
            "mean": float(np.mean(r4_residuals)),
            "verdict": "PASS" if r4_count >= 1 else "FAIL",
            "old_quantity": {
                "n_exceeding_threshold": 200,
                "min": 0.010587692260742188,
                "max": 1.5070748329162598,
                "mean": 0.3970843741297722,
            },
        },
        "R5": {
            "formula": "mean((sign(f(x)) + sign(f(mirror_full_path(x)))) / 2)",
            "n": N_R4_R5,
            "sum": float(np.sum(r5_contributions)),
            "dA_raw": float(np.mean(r5_contributions)),
            "contribution_counts": contribution_counts,
            "acceptance_mismatches": r5_acceptance_mismatches,
            "old_quantity": {"sum": 3.0, "dA_raw": 0.015, "counts": {"0.0": 197, "1.0": 3}},
        },
        "identity_witness": {
            "old_new_chi_bit_identical": old_new_chi_bits,
            "n": N_IDENTITY,
            "verdict": "PASS" if old_new_chi_bits == N_IDENTITY else "FAIL",
        },
        "full_path_IC7": {
            "mirror_after_IC1_IC6_equals_contract_of_raw_mirror_bytes": mirror_placement_bytes,
            "n": N_IDENTITY,
            "chi_sign_flip_bit_exact": r2_bits,
        },
        "natural_invalid_pixels": {"count": invalid_count_identity, "images": N_IDENTITY},
        "records": {"path": identity_records_path.name, "sha256": sha256_file(identity_records_path), "rows": N_IDENTITY},
    }
    write_json(OUT / "R1_R5_RECEIPT.json", r1_r5)

    retention_records_path = OUT / "retention_records.jsonl"
    retention_manifest = hashlib.sha256()
    retention_tensor_manifest = hashlib.sha256()
    overall = {"n": 0, "accepted": 0, "correct_accepted": 0}
    by_inclination = {
        f"{low:.1f}-{high:.1f}": {"n": 0, "accepted": 0, "correct_accepted": 0}
        for low, high in zip(retention_base.INCLINATION_EDGES_DEG[:-1], retention_base.INCLINATION_EDGES_DEG[1:])
    }
    by_snr = {
        f"{low:g}-{int(high)}": {"n": 0, "accepted": 0, "correct_accepted": 0}
        for low, high in zip(retention_base.SNR_EDGES[:-1], retention_base.SNR_EDGES[1:])
    }
    retention_invalid_count = 0
    retention_input_bytes_exact = 0
    with retention_records_path.open("w", encoding="utf-8") as records:
        for offset in range(N_RETENTION):
            source_index = RETENTION_START + offset
            parity, pitch_deg, inclination_deg, snr = retention_base.remeasure_params(source_index)
            old_image = np.ascontiguousarray(
                base.synth_spiral(parity, pitch_deg, inclination_deg, snr, seed=base.sample_seed(source_index)),
                dtype=np.float32,
            )
            image_sha = hashlib.sha256(old_image.tobytes()).hexdigest()
            retention_manifest.update(bytes.fromhex(image_sha))
            invalid_count = int(np.count_nonzero(~np.isfinite(old_image)))
            retention_invalid_count += invalid_count
            tensor, ic_receipt = apply_contract(old_image)
            tensor_sha = hashlib.sha256(tensor.tobytes()).hexdigest()
            retention_tensor_manifest.update(bytes.fromhex(tensor_sha))
            exact = tensor[0].tobytes() == old_image.tobytes()
            retention_input_bytes_exact += int(exact)
            if not exact:
                raise SystemExit(f"IC-5 changed retention tensor bytes at {source_index}")
            raw_x, raw_mirror = raw_pair(model, tensor)
            chi = chi_from_pair(raw_x, raw_mirror)
            accepted = bool(abs(chi) > TAU)
            correct = bool(accepted and np.sign(chi) == parity)
            inclination_key = retention_base.inclination_key(inclination_deg)
            snr_key = retention_base.snr_key(snr)
            for counter in (overall, by_inclination[inclination_key], by_snr[snr_key]):
                counter["n"] += 1
                counter["accepted"] += int(accepted)
                counter["correct_accepted"] += int(correct)
            records.write(json.dumps({
                "offset": offset,
                "source_index": source_index,
                "image_sha256_float32": image_sha,
                "tensor_sha256_float32": tensor_sha,
                "invalid_pixel_count": invalid_count,
                "invalid_fraction": ic_receipt["invalid_fraction"],
                "input_bytes_equal_old_path": exact,
                "parity": parity,
                "inclination_deg": inclination_deg,
                "snr": snr,
                "chi_float32": float(chi),
                "chi_bits": bits32(chi),
                "accepted": accepted,
                "accepted_sign_correct": correct,
            }, sort_keys=True) + "\n")
            if (offset + 1) % 1000 == 0:
                print(f"retention {offset + 1}/{N_RETENTION}", flush=True)

    if retention_manifest.hexdigest() != EXPECTED_RETENTION_MANIFEST:
        raise SystemExit("retention generator manifest mismatch")

    def finish(counter: dict) -> dict:
        n = counter["n"]
        accepted = counter["accepted"]
        correct = counter["correct_accepted"]
        return {
            **counter,
            "retention": accepted / n if n else None,
            "retention_lower95_one_sided_wilson": retention_base.wilson_lower(accepted, n),
            "accepted_sign_accuracy": correct / accepted if accepted else None,
        }

    retention_receipt = {
        "population": "frozen full admitted support: uniform in cos(i), 0 <= i <= 69.3 degrees",
        "overall": finish(overall),
        "by_inclination_deg": {key: finish(value) for key, value in by_inclination.items()},
        "by_snr": {key: finish(value) for key, value in by_snr.items()},
        "generator_manifest_sha256": retention_manifest.hexdigest(),
        "old_receipt_generator_manifest_sha256": EXPECTED_RETENTION_MANIFEST,
        "tensor_manifest_sha256": retention_tensor_manifest.hexdigest(),
        "input_bytes_equal_old_path": retention_input_bytes_exact,
        "natural_invalid_pixel_count": retention_invalid_count,
        "old_path_quantity": {
            "accepted": 10349,
            "n": 12000,
            "retention": 0.8624166666666667,
            "lower95_one_sided_wilson": 0.8571626782674123,
            "accepted_sign_accuracy": 1.0,
        },
        "records": {"path": retention_records_path.name, "sha256": sha256_file(retention_records_path), "rows": N_RETENTION},
    }
    write_json(OUT / "RETENTION_RECEIPT.json", retention_receipt)

    slot_validation.update({
        "selection_basis": (
            "All 13,000 frozen-generator natural synthetic images had invalid fraction 0.0. "
            "No synthetic evidence supports tolerance above zero, so the conservative cap is 0.0; "
            "one invalid pixel (1/16384) fails closed."
        ),
        "ic4_invalid_fraction_cap": 0.0,
        "natural_synthetic_images": N_IDENTITY + N_RETENTION,
        "natural_invalid_pixel_count": invalid_count_identity + retention_invalid_count,
        "ic5_form": "tensor = float32(nanomaggy)",
        "ic5_gain": 1.0,
        "ic5_offset": 0.0,
        "ic5_validation": (
            "Fixed monotone identity affine map; exact old/new input bytes on all 13,000 natural synthetics; "
            "no per-object or data-dependent operation; preserves frozen estimator scale and tau."
        ),
        "old_new_input_bytes_exact": retention_input_bytes_exact + N_IDENTITY,
        "old_new_input_images": N_RETENTION + N_IDENTITY,
        "slots_sha256": slot_sha,
        "scaler_sha256": sha256_file(SCALER_PATH),
    })
    write_json(OUT / "IC_SLOT_VALIDATION_RECEIPT.json", slot_validation)

    frozen_after = verify_pins()
    if frozen_after != frozen_before or sha256_file(SLOTS_PATH) != slot_sha:
        raise SystemExit("frozen inputs or IC slots changed during run")

    old_r4 = r1_r5["R4"]["old_quantity"]
    pass_checks = {
        "R1": r1 == N_IDENTITY,
        "R2": r2_value == N_IDENTITY and r2_bits == N_IDENTITY and max_identity_residual == 0.0,
        "R3": r3["value_equal"] and not r3["bit_equal"] and r3["ordered_acceptance_false"],
        "R4": r4_count >= 1,
        "R4_exact_old_quantity": (
            r4_count == old_r4["n_exceeding_threshold"]
            and min(r4_residuals) == old_r4["min"]
            and max(r4_residuals) == old_r4["max"]
            and float(np.mean(r4_residuals)) == old_r4["mean"]
        ),
        "R5_exact_old_quantity": (
            float(np.sum(r5_contributions)) == 3.0
            and float(np.mean(r5_contributions)) == 0.015
            and contribution_counts == {"0.0": 197, "1.0": 3}
        ),
        "identity_witness": old_new_chi_bits == N_IDENTITY,
        "IC7_full_path": mirror_placement_bytes == N_IDENTITY and r2_bits == N_IDENTITY,
        "retention_exact_old_quantity": (
            overall["accepted"] == 10349
            and overall["n"] == 12000
            and finish(overall)["retention_lower95_one_sided_wilson"] == 0.8571626782674123
        ),
        "slots_synthetic_only_validation": (
            invalid_count_identity + retention_invalid_count == 0
            and retention_input_bytes_exact + N_IDENTITY == 13000
        ),
    }
    summary = {
        "status": "PASS_ICRERUN" if all(pass_checks.values()) else "FAIL_ICRERUN",
        "checks": pass_checks,
        "slot_values": {
            "IC-4_invalid_fraction_cap": 0.0,
            "IC-5": {"form": "tensor = float32(nanomaggy)", "gain": 1.0, "offset": 0.0},
            "slots_sha256": slot_sha,
        },
        "identity_witness": r1_r5["identity_witness"],
        "hash_pins_before_and_after": frozen_after,
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
            "synthetics_only": True,
            "real_data_touched": False,
            "network_used": False,
            "training_or_retraining": False,
            "tau_recalibration": False,
            "sky_access_authorized_by_this_receipt": False,
        },
    }
    write_json(OUT / "ICRERUN_RESULTS.json", summary)
    if not all(pass_checks.values()):
        raise SystemExit(json.dumps(summary, indent=2))
    print(json.dumps(summary, indent=2, sort_keys=True), flush=True)


if __name__ == "__main__":
    main()
