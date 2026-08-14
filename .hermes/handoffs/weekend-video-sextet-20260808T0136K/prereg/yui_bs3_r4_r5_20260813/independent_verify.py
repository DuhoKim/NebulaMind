#!/usr/bin/env python3
"""Independent reduction and custody verification for BS-3 R4/R5 receipts.

This verifier does not import the model runner, torch, scipy, or the training code.
It parses the landed JSONL rows and recomputes the receipt values independently.
"""
from __future__ import annotations

import hashlib
import json
from pathlib import Path
from typing import Iterable

import numpy as np

ROOT = Path(
    "/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/"
    "weekend-video-sextet-20260808T0136K"
)
OUT = ROOT / "prereg/yui_bs3_r4_r5_20260813"
RESULTS = OUT / "results.json"
RECORDS = OUT / "paired_probe_records.jsonl"
EXPECTED_FROZEN_HASHES = {
    ROOT / "spike/yui_identity/w_chi.py": "89da33ec6260e75e06eadb0f171da4c52f1478b59ff5e543d363dbf56fefcd75",
    ROOT / "prereg/weights_frozen.pt": "83008c1cbdae511af5d30020540e1e281c62c2bd95d3cb05527fc0687bf49e6d",
    ROOT / "prereg/train_results.json": "c36cd33001e432c60df786da8c0ff95b8ef5ab350a458b29d71ff084178a41fd",
    ROOT / "prereg/receipt_results.json": "d5d4a8bc005b031ed523e64a672237536896f37030722fd5cf71ff44a3405a04",
    ROOT / "prereg/yui_inclination_retention_remeasure_20260812/results.json": "414fbc5cb6fa050390f0a6bca69e02e81795ed2a3585928be19767f4cb3a59e2",
}


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def sign(value: float) -> int:
    return int(value > 0.0) - int(value < 0.0)


def reduce_records(rows: Iterable[dict]) -> dict:
    materialized = list(rows)
    contributions: list[float] = []
    residuals: list[float] = []
    manifest = hashlib.sha256()
    source_indices: list[int] = []
    offsets: list[int] = []
    contribution_serialization_matches = 0
    production_identity_exact = 0
    acceptance_matches = 0
    for row in materialized:
        source_indices.append(int(row["source_index"]))
        offsets.append(int(row["probe_offset"]))
        manifest.update(bytes.fromhex(row["image_sha256_float32"]))
        contribution = (
            sign(float(row["raw_f_x_float32"]))
            + sign(float(row["raw_f_mirror_x_float32"]))
        ) / 2.0
        contributions.append(contribution)
        contribution_serialization_matches += int(
            contribution == float(row["dA_raw_contribution"])
        )
        residual = float(row["r4_abs_identity_violation"])
        residuals.append(residual)
        production_identity_exact += int(float(row["pure_identity_residual"]) == 0.0)
        acceptance_matches += int(not bool(row["acceptance_mismatch"]))
    return {
        "rows": len(materialized),
        "source_indices": source_indices,
        "probe_offsets": offsets,
        "image_manifest_sha256": manifest.hexdigest(),
        "dA_raw": float(np.mean(contributions)) if contributions else None,
        "sum_contributions": float(np.sum(contributions)),
        "contribution_counts": {
            str(value): contributions.count(value) for value in sorted(set(contributions))
        },
        "contribution_serialization_matches": contribution_serialization_matches,
        "r4_n_exceeding_0_01": sum(value > 0.01 for value in residuals),
        "r4_min_abs_identity_violation": min(residuals) if residuals else None,
        "r4_max_abs_identity_violation": max(residuals) if residuals else None,
        "r4_mean_abs_identity_violation": (
            float(np.mean(residuals)) if residuals else None
        ),
        "production_identity_exact": production_identity_exact,
        "acceptance_matches": acceptance_matches,
    }


def main() -> None:
    results = json.loads(RESULTS.read_text())
    rows = [json.loads(line) for line in RECORDS.read_text().splitlines() if line]
    reduced = reduce_records(rows)
    r4 = results["R4_interpolating_mirror_canary"]
    r5 = results["R5_flip_imbalance"]
    probe = results["probe_set"]
    frozen_hashes_actual = {
        str(path.relative_to(ROOT)): sha256_file(path)
        for path in EXPECTED_FROZEN_HASHES
    }
    checks = {
        "all_frozen_hashes_match": all(
            frozen_hashes_actual[str(path.relative_to(ROOT))] == expected
            for path, expected in EXPECTED_FROZEN_HASHES.items()
        ),
        "records_hash_matches_results": sha256_file(RECORDS) == results["records"]["sha256"],
        "row_count_200": reduced["rows"] == 200 == results["records"]["rows"],
        "source_indices_exact": reduced["source_indices"] == list(range(3_000_000, 3_000_200)),
        "probe_offsets_exact": reduced["probe_offsets"] == list(range(200)),
        "image_manifest_matches": (
            reduced["image_manifest_sha256"] == probe["image_manifest_sha256"]
        ),
        "per_row_contributions_recomputed": (
            reduced["contribution_serialization_matches"] == 200
        ),
        "dA_raw_matches": reduced["dA_raw"] == r5["dA_raw"] == 0.015,
        "dA_sum_matches": reduced["sum_contributions"] == r5["sum_contributions"] == 3.0,
        "dA_counts_match": reduced["contribution_counts"] == r5["contribution_counts"],
        "r4_count_matches": (
            reduced["r4_n_exceeding_0_01"] == r4["n_exceeding_threshold"] == 200
        ),
        "r4_min_matches": (
            reduced["r4_min_abs_identity_violation"] == r4["min_abs_identity_violation"]
        ),
        "r4_max_matches": (
            reduced["r4_max_abs_identity_violation"] == r4["max_abs_identity_violation"]
        ),
        "r4_mean_matches": (
            reduced["r4_mean_abs_identity_violation"] == r4["mean_abs_identity_violation"]
        ),
        "r4_pass_rule_satisfied": reduced["r4_n_exceeding_0_01"] >= 1,
        "production_identity_all_exact": reduced["production_identity_exact"] == 200,
        "production_acceptance_pairs_all_match": reduced["acceptance_matches"] == 200,
        "operative_retention_exact": (
            results["operative_retention"]["accepted"] == 10_349
            and results["operative_retention"]["n"] == 12_000
            and results["operative_retention"]["retention"] == 0.8624166666666667
            and results["operative_retention"]["lower95_one_sided_wilson"]
            == 0.8571626782674123
        ),
        "no_sky_or_downstream_authority": all(
            value is False for value in results["boundaries"].values()
        ),
    }
    verification = {
        "status": (
            "PASS_INDEPENDENT_R4_R5_REDUCTION"
            if all(checks.values())
            else "FAIL_INDEPENDENT_R4_R5_REDUCTION"
        ),
        "checks": checks,
        "reduced": reduced,
        "frozen_hashes_actual": frozen_hashes_actual,
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
