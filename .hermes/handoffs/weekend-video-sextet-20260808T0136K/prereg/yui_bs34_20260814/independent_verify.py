#!/usr/bin/env python3
"""Independent BS-3/BS-4 JSONL reducer and custody verifier.

No import of the model runner, training code, Torch, SciPy, or secondary algorithm.
"""
from __future__ import annotations

import hashlib
import json
import math
import struct
from pathlib import Path
from typing import Iterable

ROOT = Path(
    "/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/"
    "weekend-video-sextet-20260808T0136K"
)
OUT = ROOT / "prereg/yui_bs34_20260814"
RESULTS = OUT / "results.json"
RECORDS = OUT / "identity_probe_records.jsonl"
SECONDARY_RECEIPT = ROOT / "prereg/receipt_results.json"
SECONDARY_SPIKE_RESULTS = ROOT / "spike/yui_identity/results.json"
SECONDARY_TAU = 5.916292121766702
EXPECTED_FROZEN = {
    "prereg/KUN_REGATE_BS1_BS3_20260814.md": "e5bc40fc4368d813649534dd50dd9fe686b6200c244e7ffe4a457602ba483a66",
    "prereg/PREREG_LONGO_AMPLITUDE_TEST_20260812.md": "ac43490054b159610385b8faac28dc4e3178161fadd97d66aa0418a1186b7590",
    "prereg/YUI_PRODUCTION_ESTIMATOR_RECEIPT_20260812.md": "b4e2f5b5f92fc881ec2a0a35e84515fd05057c1051bff516cad7acae3609e18a",
    "prereg/receipt_results.json": "d5d4a8bc005b031ed523e64a672237536896f37030722fd5cf71ff44a3405a04",
    "prereg/train_results.json": "c36cd33001e432c60df786da8c0ff95b8ef5ab350a458b29d71ff084178a41fd",
    "prereg/weights_frozen.pt": "83008c1cbdae511af5d30020540e1e281c62c2bd95d3cb05527fc0687bf49e6d",
    "prereg/yui_bs3_r4_r5_20260813/run_bs3_r4_r5.py": "de0f35355902f25497e240a413a087a1413d365342419b0be3fc15a7e5117914",
    "prereg/yui_inclination_retention_remeasure_20260812/results.json": "414fbc5cb6fa050390f0a6bca69e02e81795ed2a3585928be19767f4cb3a59e2",
    "prereg/yui_receipt_run.py": "eb41680c8425135662bf9d18cad1a12a4c752c137672f179e3e140f48656a028",
    "spike/YUI_IDENTITY_UNITTEST_RECEIPT_20260812.md": "fc2d99f23cb8ac720558f14bc94537faffd4d3f9f1f810f840220c9be0b60c55",
    "spike/yui_identity/results.json": "9e95861f8e02113ae97681f572b93a8dcbc27f16fa22214fb7971d3a0becab61",
    "spike/yui_identity/run_identity_test.py": "c44813b73ee3cb92895d3d29c71c64d0a9860d5650e0cec4567ee215b12182e5",
    "spike/yui_identity/w_chi.py": "89da33ec6260e75e06eadb0f171da4c52f1478b59ff5e543d363dbf56fefcd75",
}


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def float32(value: float) -> float:
    return struct.unpack("<f", struct.pack("<f", float(value)))[0]


def bits32(value: float) -> str:
    bits = struct.unpack("<I", struct.pack("<f", float32(value)))[0]
    return f"0x{bits:08x}"


def sign(value: float) -> int:
    return int(value > 0.0) - int(value < 0.0)


def bin_label(snr: float) -> str:
    if 2.0 <= snr < 5.0:
        return "2-5"
    if 5.0 <= snr < 10.0:
        return "5-10"
    if 10.0 <= snr < 20.0:
        return "10-20"
    if 20.0 <= snr < 50.0001:
        return "20-50"
    raise ValueError(f"S/N outside support: {snr}")


def reduce_records(rows: Iterable[dict], secondary_tau: float) -> dict:
    materialized = list(rows)
    manifest = hashlib.sha256()
    prefix_manifest = hashlib.sha256()
    offsets: list[int] = []
    source_indices: list[int] = []
    primary_residuals: list[float] = []
    secondary_residuals: list[float] = []
    r4_residuals: list[float] = []
    contributions: list[float] = []
    counts = {
        "r1": 0,
        "primary_R2_value_exact": 0,
        "primary_R2_bit_exact": 0,
        "secondary_R2_value_exact": 0,
        "secondary_R2_bit_exact": 0,
        "secondary_accepted": 0,
        "serialized_acceptance_matches": 0,
        "serialized_contribution_matches": 0,
        "serialized_R4_residual_matches": 0,
    }
    by_snr = {label: [0, 0] for label in ("2-5", "5-10", "10-20", "20-50")}
    for row in materialized:
        offset = int(row["probe_offset"])
        offsets.append(offset)
        source_indices.append(int(row["source_index"]))
        image_digest = bytes.fromhex(row["image_sha256_float32"])
        manifest.update(image_digest)
        if offset < 200:
            prefix_manifest.update(image_digest)
        counts["r1"] += int(bool(row["R1_mirror_involution_byte_exact"]))

        primary_x = float(row["primary_chi_x_float32"])
        primary_m = float(row["primary_chi_mirror_float32"])
        primary_value = primary_m == -primary_x
        primary_bit = row["primary_chi_mirror_bits"] == bits32(-primary_x)
        counts["primary_R2_value_exact"] += int(primary_value)
        counts["primary_R2_bit_exact"] += int(primary_bit)
        primary_residuals.append(abs(primary_m + primary_x))

        secondary_x = float(row["secondary_chi_x_float32"])
        secondary_m = float(row["secondary_chi_mirror_float32"])
        secondary_value = secondary_m == -secondary_x
        secondary_bit = row["secondary_chi_mirror_bits"] == bits32(-secondary_x)
        counts["secondary_R2_value_exact"] += int(secondary_value)
        counts["secondary_R2_bit_exact"] += int(secondary_bit)
        secondary_residuals.append(abs(secondary_m + secondary_x))

        accepted = abs(secondary_x) > secondary_tau
        counts["secondary_accepted"] += int(accepted)
        counts["serialized_acceptance_matches"] += int(
            accepted == bool(row["secondary_accepted_at_frozen_tau"])
        )
        label = bin_label(float(row["snr"]))
        by_snr[label][0] += int(accepted)
        by_snr[label][1] += 1

        contribution = (
            sign(float(row["secondary_raw_w_x_float32"]))
            + sign(float(row["secondary_raw_w_mirror_float32"]))
        ) / 2.0
        contributions.append(contribution)
        counts["serialized_contribution_matches"] += int(
            contribution == float(row["secondary_dA_raw_contribution"])
        )

        r4_residual = abs(
            float(row["secondary_R4_chi_bad_input_float32"]) + secondary_x
        )
        r4_residuals.append(r4_residual)
        counts["serialized_R4_residual_matches"] += int(
            r4_residual == float(row["secondary_R4_abs_identity_violation"])
        )

    n = len(materialized)
    contribution_counts = {
        str(value): contributions.count(value) for value in sorted(set(contributions))
    }
    return {
        "rows": n,
        "offsets": offsets,
        "source_indices": source_indices,
        "image_manifest_sha256": manifest.hexdigest(),
        "prefix_200_manifest_sha256": prefix_manifest.hexdigest(),
        **counts,
        "primary_max_identity_residual": max(primary_residuals) if primary_residuals else None,
        "secondary_max_identity_residual": max(secondary_residuals) if secondary_residuals else None,
        "secondary_dA_raw": sum(contributions) / n if n else None,
        "secondary_dA_sum": sum(contributions),
        "secondary_dA_counts": contribution_counts,
        "secondary_R4_n_exceeding_0_01": sum(value > 0.01 for value in r4_residuals),
        "secondary_R4_min": min(r4_residuals) if r4_residuals else None,
        "secondary_R4_max": max(r4_residuals) if r4_residuals else None,
        "secondary_R4_mean": sum(r4_residuals) / n if n else None,
        "secondary_by_snr": {
            label: {
                "accepted": pair[0],
                "n": pair[1],
                "retention": pair[0] / pair[1] if pair[1] else None,
                "abstention": 1.0 - pair[0] / pair[1] if pair[1] else None,
            }
            for label, pair in by_snr.items()
        },
    }


def main() -> None:
    results = json.loads(RESULTS.read_text())
    rows = [json.loads(line) for line in RECORDS.read_text().splitlines() if line]
    reduced = reduce_records(rows, SECONDARY_TAU)
    bs3 = results["BS3_primary_identity"]
    bs4 = results["BS4_secondary_identity_and_abstention"]
    r4 = bs4["R4_interpolating_mirror_canary"]
    r5 = bs4["R5_raw_flip_imbalance"]
    fresh = bs4["fresh_promised_probe_abstention"]
    historical = json.loads(SECONDARY_RECEIPT.read_text())["secondary_retention"]
    spike = json.loads(SECONDARY_SPIKE_RESULTS.read_text())["E_calibration"]
    frozen_actual = {
        rel: sha256_file(ROOT / rel) for rel in EXPECTED_FROZEN
    }
    checks = {
        "all_frozen_hashes_match": frozen_actual == EXPECTED_FROZEN,
        "records_hash_matches": sha256_file(RECORDS) == results["records"]["sha256"],
        "rows_1000": reduced["rows"] == 1000 == results["records"]["rows"],
        "offsets_exact": reduced["offsets"] == list(range(1000)),
        "source_indices_exact": reduced["source_indices"] == list(range(3_000_000, 3_001_000)),
        "manifest_matches": reduced["image_manifest_sha256"] == results["probe_set"]["image_manifest_sha256"],
        "prefix_manifest_matches_prior": (
            reduced["prefix_200_manifest_sha256"]
            == results["probe_set"]["prefix_200_manifest_sha256"]
            == "ab75d5f2ec08ad44fbcf1198d1612c23759f8d3aac29db044a181346ac43f9b2"
        ),
        "R1_all_exact": reduced["r1"] == 1000,
        "BS3_R2_value_all_exact": reduced["primary_R2_value_exact"] == 1000,
        "BS3_R2_bits_all_exact": reduced["primary_R2_bit_exact"] == 1000,
        "BS3_max_residual_zero": reduced["primary_max_identity_residual"] == 0.0,
        "BS3_result_pass": bs3["verdict"] == "PASS",
        "BS4_R2_value_all_exact": reduced["secondary_R2_value_exact"] == 1000,
        "BS4_R2_bits_all_exact": reduced["secondary_R2_bit_exact"] == 1000,
        "BS4_max_residual_zero": reduced["secondary_max_identity_residual"] == 0.0,
        "BS4_result_pass": bs4["verdict"] == "PASS",
        "serialized_acceptance_all_match": reduced["serialized_acceptance_matches"] == 1000,
        "fresh_abstention_matches": (
            reduced["secondary_accepted"] == fresh["accepted"] == 1
            and fresh["abstention"] == 0.999
            and reduced["secondary_by_snr"] == fresh["by_snr"]
        ),
        "serialized_contributions_all_match": reduced["serialized_contribution_matches"] == 1000,
        "R5_matches": (
            reduced["secondary_dA_raw"] == r5["dA_raw"] == 0.0
            and reduced["secondary_dA_sum"] == r5["sum"] == 0.0
            and reduced["secondary_dA_counts"] == r5["counts"] == {"0.0": 1000}
        ),
        "serialized_R4_residuals_all_match": reduced["serialized_R4_residual_matches"] == 1000,
        "R4_matches": (
            reduced["secondary_R4_n_exceeding_0_01"] == r4["n_exceeding_threshold"] == 939
            and reduced["secondary_R4_min"] == r4["min"]
            and reduced["secondary_R4_max"] == r4["max"]
            and reduced["secondary_R4_mean"] == r4["mean"]
        ),
        "historical_production_abstention_exact": (
            historical["tau"] == SECONDARY_TAU
            and historical["retention_central"] == 0.0013333333333333333
            and 1.0 - historical["retention_central"] == 0.9986666666666667
            and historical["n"] == 12_000
        ),
        "historical_spike_abstention_exact": spike["overall_abstention_spirals"] == 0.922,
        "all_boundaries_false": all(value is False for value in results["boundaries"].values()),
        "overall_machine_status_pass": results["status"] == "PASS_BS3_IDENTITY_AND_BS4_IDENTITY_VALIDITY",
    }
    verification = {
        "status": "PASS_INDEPENDENT_BS34_REDUCTION" if all(checks.values()) else "FAIL_INDEPENDENT_BS34_REDUCTION",
        "checks": checks,
        "reduced": reduced,
        "frozen_hashes_actual": frozen_actual,
        "results_sha256": sha256_file(RESULTS),
        "records_sha256": sha256_file(RECORDS),
    }
    destination = OUT / "independent_verification.json"
    destination.write_text(json.dumps(verification, indent=2, sort_keys=True) + "\n")
    print(json.dumps(verification, indent=2, sort_keys=True))
    if not all(checks.values()):
        raise SystemExit(1)


if __name__ == "__main__":
    main()
