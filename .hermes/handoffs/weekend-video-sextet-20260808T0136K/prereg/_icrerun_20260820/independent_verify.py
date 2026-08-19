#!/usr/bin/env python3
"""Independent stdlib-only reduction of the IC rerun receipts.

This verifier deliberately imports neither the rerun/model runner, Torch, NumPy,
SciPy, the generator, nor the production input function.
"""
from __future__ import annotations

import ast
import hashlib
import json
import math
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
OUT = ROOT / "_icrerun_20260820"
SLOTS = ROOT / "_cutout_runner_20260820/ic_slots.json"
SCALER = OUT / "ic5_scaler.py"
RUNNER = OUT / "run_icrerun.py"
R1_R5 = OUT / "R1_R5_RECEIPT.json"
RETENTION = OUT / "RETENTION_RECEIPT.json"
SLOT_VALIDATION = OUT / "IC_SLOT_VALIDATION_RECEIPT.json"
SUMMARY = OUT / "ICRERUN_RESULTS.json"
IDENTITY_ROWS = OUT / "r1_r5_records.jsonl"
RETENTION_ROWS = OUT / "retention_records.jsonl"
EXPECTED = {
    "amendment": (ROOT / "LANA_PC1_INPUT_AMENDMENT_20260815.md", "519ab5ba33c5e9d670b5654fb41f6941293c5d969c5515fb0284ebe8d52d70fb"),
    "cutout_runner": (ROOT / "_cutout_runner_20260820/cutout_runner.py", "ccb9b8fed457333669e54fa9f0a3dac645dc866a56c6cd8dc665ffd4d93b1bcc"),
    "generator": (ROOT.parent / "spike/yui_identity/w_chi.py", "89da33ec6260e75e06eadb0f171da4c52f1478b59ff5e543d363dbf56fefcd75"),
    "weights": (ROOT / "weights_frozen.pt", "83008c1cbdae511af5d30020540e1e281c62c2bd95d3cb05527fc0687bf49e6d"),
    "scaler": (SCALER, "21b66eda899b5e48034be2b2d92ee2c77f262b156eb59d680eb1b80763d12621"),
}
EXPECTED_SLOT_SHA = "10d24a6e1c5dd64eef8e1ada7e3d222f2e168bab288b1438792db7ff6a848372"
EXPECTED_IDENTITY_MANIFEST = "35d679d4955d3657866bd64fe309a9a42b30ff8a61d1952d2a3795ee59231024"
EXPECTED_PREFIX_MANIFEST = "ab75d5f2ec08ad44fbcf1198d1612c23759f8d3aac29db044a181346ac43f9b2"
EXPECTED_RETENTION_MANIFEST = "bb60b69b17b24424af47667367312c1915cd0b8986336865a741fe70f80933d0"
Z = 1.6448536269514722


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1 << 20), b""):
            digest.update(chunk)
    return digest.hexdigest()


def read_json(path: Path):
    return json.loads(path.read_text(encoding="utf-8"))


def read_jsonl(path: Path):
    with path.open(encoding="utf-8") as handle:
        for line in handle:
            yield json.loads(line)


def manifest(rows: list[dict], field: str) -> str:
    digest = hashlib.sha256()
    for row in rows:
        digest.update(bytes.fromhex(row[field]))
    return digest.hexdigest()


def wilson(successes: int, trials: int) -> float:
    proportion = successes / trials
    denominator = 1.0 + Z * Z / trials
    center = proportion + Z * Z / (2.0 * trials)
    radius = Z * math.sqrt(proportion * (1.0 - proportion) / trials + Z * Z / (4.0 * trials * trials))
    return (center - radius) / denominator


def imported_roots(path: Path) -> set[str]:
    tree = ast.parse(path.read_text(encoding="utf-8"))
    roots: set[str] = set()
    for node in ast.walk(tree):
        if isinstance(node, ast.Import):
            roots.update(alias.name.split(".")[0] for alias in node.names)
        elif isinstance(node, ast.ImportFrom) and node.module:
            roots.add(node.module.split(".")[0])
    return roots


def main() -> None:
    r = read_json(R1_R5)
    retention = read_json(RETENTION)
    slot_validation = read_json(SLOT_VALIDATION)
    summary = read_json(SUMMARY)
    identity_rows = list(read_jsonl(IDENTITY_ROWS))
    retention_rows = list(read_jsonl(RETENTION_ROWS))
    slots = read_json(SLOTS)

    identity_sequence = [row["source_index"] for row in identity_rows]
    retention_sequence = [row["source_index"] for row in retention_rows]
    r4_values = [row["R4_abs_identity_violation"] for row in identity_rows[:200]]
    contributions = [row["R5_contribution"] for row in identity_rows[:200]]
    contribution_counts = {str(value): contributions.count(value) for value in sorted(set(contributions))}
    retention_accepted = sum(bool(row["accepted"]) for row in retention_rows)
    retention_correct = sum(bool(row["accepted_sign_correct"]) for row in retention_rows)
    all_hashes = {name: sha256(path) for name, (path, _) in EXPECTED.items()}
    expected_hashes = {name: expected for name, (_, expected) in EXPECTED.items()}
    forbidden = {"socket", "requests", "urllib", "httpx", "astropy"}
    runner_imports = imported_roots(RUNNER)

    checks = {
        "frozen_hashes": all_hashes == expected_hashes,
        "slots_hash": sha256(SLOTS) == EXPECTED_SLOT_SHA == slot_validation["slots_sha256"],
        "slot_values": (
            slots["ic4_invalid_fraction_cap"] == 0.0
            and slots["ic5_scaling_map"]["constants"] == {
                "form": "tensor = float32(nanomaggy)", "gain": 1.0, "offset": 0.0
            }
            and slots["ic5_scaling_map"]["module_sha256"] == EXPECTED["scaler"][1]
        ),
        "identity_rows": len(identity_rows) == 1000,
        "identity_source_sequence": identity_sequence == list(range(3_000_000, 3_001_000)),
        "identity_manifest": manifest(identity_rows, "image_sha256_float32") == EXPECTED_IDENTITY_MANIFEST,
        "prefix_manifest": manifest(identity_rows[:200], "image_sha256_float32") == EXPECTED_PREFIX_MANIFEST,
        "R1": sum(bool(row["R1_involution_byte_exact"]) for row in identity_rows) == 1000,
        "R2_value": sum(bool(row["R2_value_exact"]) for row in identity_rows) == 1000,
        "R2_bits": sum(bool(row["R2_bit_exact"]) for row in identity_rows) == 1000,
        "identity_witness": sum(bool(row["old_new_chi_bit_identical"]) for row in identity_rows) == 1000,
        "IC7_placement": sum(bool(row["IC7_mirror_placement_byte_exact"]) for row in identity_rows) == 1000,
        "all_identity_input_bytes": all(bool(row["input_bytes_equal_old_path"]) for row in identity_rows),
        "all_identity_invalid_zero": sum(row["invalid_pixel_count"] for row in identity_rows) == 0,
        "R3": (
            r["R3"]["value_equal"]
            and not r["R3"]["bit_equal"]
            and r["R3"]["ordered_acceptance_false"]
            and r["R3"]["chi_mirror_bits"] == "0x00000000"
            and r["R3"]["neg_chi_bits"] == "0x80000000"
        ),
        "R4_count": sum(value > 0.01 for value in r4_values) == 200 == r["R4"]["n_exceeding_threshold"],
        "R4_min": min(r4_values) == 0.010587692260742188 == r["R4"]["min"],
        "R4_max": max(r4_values) == 1.5070748329162598 == r["R4"]["max"],
        "R4_mean": math.isclose(math.fsum(r4_values) / 200, r["R4"]["mean"], rel_tol=0.0, abs_tol=1e-15),
        "R5": (
            math.fsum(contributions) == 3.0
            and math.fsum(contributions) / 200 == 0.015
            and contribution_counts == {"0.0": 197, "1.0": 3}
            and r["R5"]["acceptance_mismatches"] == 0
        ),
        "retention_rows": len(retention_rows) == 12000,
        "retention_source_sequence": retention_sequence == list(range(2_000_000, 2_012_000)),
        "retention_manifest": manifest(retention_rows, "image_sha256_float32") == EXPECTED_RETENTION_MANIFEST,
        "retention_input_bytes": all(bool(row["input_bytes_equal_old_path"]) for row in retention_rows),
        "retention_invalid_zero": sum(row["invalid_pixel_count"] for row in retention_rows) == 0,
        "retention_count": retention_accepted == 10349 and retention["overall"]["accepted"] == 10349,
        "retention_accuracy": retention_correct == 10349,
        "retention_wilson": wilson(10349, 12000) == 0.8571626782674123 == retention["overall"]["retention_lower95_one_sided_wilson"],
        "summary_pass": summary["status"] == "PASS_ICRERUN" and all(summary["checks"].values()),
        "stdlib_only_verifier": imported_roots(Path(__file__)) <= {"__future__", "ast", "hashlib", "json", "math", "pathlib"},
        "runner_has_no_network_or_fits_import": not bool(runner_imports & forbidden),
        "synthetics_only_boundary": summary["boundaries"] == {
            "network_used": False,
            "real_data_touched": False,
            "sky_access_authorized_by_this_receipt": False,
            "synthetics_only": True,
            "tau_recalibration": False,
            "training_or_retraining": False,
        },
    }
    result = {
        "verdict": "PASS_INDEPENDENT_ICRERUN_REDUCTION" if all(checks.values()) else "FAIL_INDEPENDENT_ICRERUN_REDUCTION",
        "checks": checks,
        "reductions": {
            "R1": f"{sum(bool(row['R1_involution_byte_exact']) for row in identity_rows)}/1000",
            "R2_bits": f"{sum(bool(row['R2_bit_exact']) for row in identity_rows)}/1000",
            "identity_witness": f"{sum(bool(row['old_new_chi_bit_identical']) for row in identity_rows)}/1000",
            "R4_exceeding": sum(value > 0.01 for value in r4_values),
            "R4_min": min(r4_values),
            "R4_max": max(r4_values),
            "R4_mean_fsum": math.fsum(r4_values) / 200,
            "R5_sum": math.fsum(contributions),
            "R5_dA_raw": math.fsum(contributions) / 200,
            "retention": {"accepted": retention_accepted, "n": 12000, "lower95": wilson(retention_accepted, 12000)},
        },
        "artifact_hashes": {
            "ic_slots.json": sha256(SLOTS),
            "ic5_scaler.py": sha256(SCALER),
            "run_icrerun.py": sha256(RUNNER),
            "R1_R5_RECEIPT.json": sha256(R1_R5),
            "RETENTION_RECEIPT.json": sha256(RETENTION),
            "IC_SLOT_VALIDATION_RECEIPT.json": sha256(SLOT_VALIDATION),
            "ICRERUN_RESULTS.json": sha256(SUMMARY),
            "r1_r5_records.jsonl": sha256(IDENTITY_ROWS),
            "retention_records.jsonl": sha256(RETENTION_ROWS),
        },
        "verifier_imports": sorted(imported_roots(Path(__file__))),
        "runner_imports": sorted(runner_imports),
    }
    output = OUT / "INDEPENDENT_VERIFICATION.json"
    output.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps(result, indent=2, sort_keys=True))
    if not all(checks.values()):
        raise SystemExit(1)


if __name__ == "__main__":
    main()
