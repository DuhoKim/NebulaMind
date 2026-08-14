#!/usr/bin/env python3
"""Independent no-model/no-NumPy BS-5 record reducer and custody verifier."""
from __future__ import annotations

import ast
import hashlib
import json
from pathlib import Path
from typing import Iterable

ROOT = Path(
    "/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/"
    "weekend-video-sextet-20260808T0136K"
)
OUT = ROOT / "prereg/yui_bs5_sign_anchor_20260814"
RESULTS = OUT / "results.json"
PRE_RESULTS = OUT / "pre_correction_results.json"
RECORDS = OUT / "pre_correction_probe_records.jsonl"
WCS_RECEIPT = OUT / "wcs_parity.json"
RUNNER = OUT / "run_bs5_sign_anchor.py"
MASTER_SEED = "LONGO-AMPLITUDE-BS5-ABSOLUTE-SIGN-V1"
PROBE_INDEX_START = 5_000_000
N_PROBES = 32
FROZEN_TAU = 4.4006456017494235
EXPECTED_FROZEN = {
    "prereg/PREREG_LONGO_AMPLITUDE_TEST_FROZEN_20260814.md": "da2c6a21d994b9af7395347bf881075f855826ff859dd0415f15042f80ed3308",
    "prereg/PREREG_LONGO_AMPLITUDE_TEST_20260812.md": "ac43490054b159610385b8faac28dc4e3178161fadd97d66aa0418a1186b7590",
    "prereg/LANA_BS5_LONGO_SIGN_20260814.md": "b7c32dcf12d9e147e5dee6a8262d925b61011615f2ee1d75d687600abb0a72ca",
    "prereg/_tmp_YUI_SIGN_ANCHOR_BRIEF.md": "f8f0633a9e2bb513534ba721e79e573afd0e8e2d0e2ef3a11f6bcfee3be45602",
    "prereg/weights_frozen.pt": "83008c1cbdae511af5d30020540e1e281c62c2bd95d3cb05527fc0687bf49e6d",
    "prereg/train_results.json": "c36cd33001e432c60df786da8c0ff95b8ef5ab350a458b29d71ff084178a41fd",
    "prereg/receipt_results.json": "d5d4a8bc005b031ed523e64a672237536896f37030722fd5cf71ff44a3405a04",
    "prereg/yui_bs3_r4_r5_20260813/run_bs3_r4_r5.py": "de0f35355902f25497e240a413a087a1413d365342419b0be3fc15a7e5117914",
    "spike/yui_identity/w_chi.py": "89da33ec6260e75e06eadb0f171da4c52f1478b59ff5e543d363dbf56fefcd75",
}


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def expected_seed(source_index: int) -> int:
    payload = f"{MASTER_SEED}||{source_index}".encode()
    return int.from_bytes(hashlib.sha256(payload).digest()[:8], "big") % (2**63)


def reduce_records(rows: Iterable[dict], *, tau: float) -> dict:
    materialized = list(rows)
    image_manifest = hashlib.sha256()
    probe_indices = []
    source_indices = []
    estimator_values = []
    counts = {
        "serialized_seed_matches": 0,
        "analytic_ccw_slope_positive": 0,
        "ccw_slope_positive": 0,
        "mirror_slope_negative": 0,
        "mirror_involution_byte_exact": 0,
        "base_sign_pair_pass": 0,
        "estimator_sign_pair_pass": 0,
        "estimator_antisymmetry_exact": 0,
        "serialized_predicates_match": 0,
        "accepted_at_tau": 0,
    }
    multipliers = []
    for row in materialized:
        probe_indices.append(int(row["probe_index"]))
        source_index = int(row["source_index"])
        source_indices.append(source_index)
        counts["serialized_seed_matches"] += int(
            int(row["seed"]) == expected_seed(source_index)
        )
        image_manifest.update(bytes.fromhex(row["image_sha256_float32"]))
        image_manifest.update(bytes.fromhex(row["mirror_sha256_float32"]))
        analytic_slope = float(row["analytic_d_pa_d_ln_r"])
        ccw_slope = float(row["measured_ccw_image_d_pa_d_ln_r"])
        mirror_slope = float(row["measured_mirror_d_pa_d_ln_r"])
        counts["analytic_ccw_slope_positive"] += int(analytic_slope > 0.0)
        counts["ccw_slope_positive"] += int(ccw_slope > 0.0)
        counts["mirror_slope_negative"] += int(mirror_slope < 0.0)
        counts["mirror_involution_byte_exact"] += int(
            bool(row["mirror_involution_byte_exact"])
        )
        base_value = float(row["base_chi_ccw_float32"])
        base_mirror = float(row["base_chi_mirror_float32"])
        counts["base_sign_pair_pass"] += int(base_value > 0.0 and base_mirror < 0.0)
        estimator_value = float(row["estimator_chi_ccw_float32"])
        estimator_mirror = float(row["estimator_chi_mirror_float32"])
        estimator_values.append(estimator_value)
        multipliers.append(int(row["estimator_sign_multiplier"]))
        pair_pass = estimator_value > 0.0 and estimator_mirror < 0.0
        accepted = abs(estimator_value) > tau
        counts["estimator_sign_pair_pass"] += int(pair_pass)
        counts["estimator_antisymmetry_exact"] += int(estimator_mirror == -estimator_value)
        counts["accepted_at_tau"] += int(accepted)
        counts["serialized_predicates_match"] += int(
            pair_pass == bool(row["estimator_sign_pair_pass"])
            and accepted == bool(row["accepted_at_frozen_tau"])
        )
    n = len(materialized)
    return {
        "rows": n,
        "probe_indices": probe_indices,
        "source_indices": source_indices,
        "image_and_mirror_manifest_sha256": image_manifest.hexdigest(),
        "estimator_sign_multipliers": multipliers,
        **counts,
        "estimator_chi_min": min(estimator_values) if estimator_values else None,
        "estimator_chi_max": max(estimator_values) if estimator_values else None,
        "estimator_chi_mean": sum(estimator_values) / n if n else None,
    }


def imported_roots(path: Path) -> set[str]:
    tree = ast.parse(path.read_text(encoding="utf-8"))
    roots = set()
    for node in ast.walk(tree):
        if isinstance(node, ast.Import):
            roots.update(alias.name.split(".")[0] for alias in node.names)
        elif isinstance(node, ast.ImportFrom) and node.module:
            roots.add(node.module.split(".")[0])
    return roots


def attempt1_disclosure_valid(history: dict, stderr: str, *, partial_size: int) -> bool:
    return bool(
        history["technical_rerun_after_serialization_failure"] is True
        and history["attempt1_failed_before_any_sign_result"] is True
        and "bool_ is not JSON serializable" in stderr
        and partial_size == 0
    )


def main() -> None:
    results = json.loads(RESULTS.read_text(encoding="utf-8"))
    pre_results = json.loads(PRE_RESULTS.read_text(encoding="utf-8"))
    rows = [json.loads(line) for line in RECORDS.read_text(encoding="utf-8").splitlines() if line]
    reduced = reduce_records(rows, tau=FROZEN_TAU)
    wcs = json.loads(WCS_RECEIPT.read_text(encoding="utf-8"))
    frozen_actual = {relative: sha256_file(ROOT / relative) for relative in EXPECTED_FROZEN}
    runner_imports = imported_roots(RUNNER)
    prohibited_imports = {
        "requests",
        "urllib",
        "httpx",
        "socket",
        "astropy",
        "astroquery",
        "pandas",
        "sqlite3",
    }
    result_counts = results["counts"]
    checks = {
        "independent_verifier_has_no_model_numeric_imports": not (
            imported_roots(Path(__file__)) & {"numpy", "torch", "scipy"}
        ),
        "runner_has_no_network_survey_catalogue_imports": not (runner_imports & prohibited_imports),
        "all_frozen_hashes_match": frozen_actual == EXPECTED_FROZEN,
        "stage_file_hash_matches": sha256_file(PRE_RESULTS) == results["stage_result_sha256"],
        "records_hash_matches": sha256_file(RECORDS) == results["records"]["sha256"],
        "wcs_hash_matches": sha256_file(WCS_RECEIPT) == results["wcs_parity_first"]["sha256"],
        "wcs_passed_first": (
            wcs["status"] == "PASS_WCS_PARITY_FIRST"
            and all(wcs["checks"].values())
            and wcs["east_direction_on_raster"] == "left"
            and wcs["north_direction_on_raster"] == "up"
            and wcs["cd_pc_cdelt_determinant"] < 0.0
            and wcs["row_order_transform_determinant"] == 1.0
            and wcs["combined_pixel_to_sky_determinant"] < 0.0
        ),
        "rows_32": reduced["rows"] == N_PROBES == results["records"]["rows"],
        "probe_indices_exact": reduced["probe_indices"] == list(range(N_PROBES)),
        "source_indices_exact": reduced["source_indices"] == list(
            range(PROBE_INDEX_START, PROBE_INDEX_START + N_PROBES)
        ),
        "all_seeds_match": reduced["serialized_seed_matches"] == N_PROBES,
        "image_manifest_matches": (
            reduced["image_and_mirror_manifest_sha256"]
            == results["probe_set"]["image_and_mirror_manifest_sha256"]
        ),
        "all_analytic_ccw": reduced["analytic_ccw_slope_positive"] == N_PROBES,
        "all_rendered_ccw": (
            reduced["ccw_slope_positive"]
            == result_counts["known_ccw_image_slope_positive"]
            == N_PROBES
        ),
        "all_mirrors_cw": (
            reduced["mirror_slope_negative"]
            == result_counts["known_cw_mirror_slope_negative"]
            == N_PROBES
        ),
        "all_mirror_involutions_exact": (
            reduced["mirror_involution_byte_exact"]
            == result_counts["mirror_involution_byte_exact"]
            == N_PROBES
        ),
        "uncorrected_base_sign_passes": (
            reduced["base_sign_pair_pass"]
            == result_counts["base_chi_ccw_positive"]
            == result_counts["base_chi_mirror_negative"]
            == N_PROBES
        ),
        "estimator_sign_passes": (
            reduced["estimator_sign_pair_pass"]
            == result_counts["estimator_chi_ccw_positive"]
            == result_counts["estimator_chi_mirror_negative"]
            == N_PROBES
        ),
        "estimator_antisymmetry_exact": (
            reduced["estimator_antisymmetry_exact"]
            == result_counts["estimator_antisymmetry_value_exact"]
            == N_PROBES
        ),
        "serialized_predicates_all_match": reduced["serialized_predicates_match"] == N_PROBES,
        "all_accepted_at_frozen_tau": (
            reduced["accepted_at_tau"]
            == result_counts["estimator_accepted_at_tau"]
            == N_PROBES
        ),
        "summary_matches": (
            reduced["estimator_chi_min"] == results["estimator_chi_summary"]["min"]
            and reduced["estimator_chi_max"] == results["estimator_chi_summary"]["max"]
            and reduced["estimator_chi_mean"] == results["estimator_chi_summary"]["mean"]
        ),
        "multiplier_is_uncorrected_plus_one": (
            results["estimator_sign_multiplier"] == 1
            and set(reduced["estimator_sign_multipliers"]) == {1}
            and results["estimator_corrected_after_precheck"] is False
        ),
        "convention_never_changed": (
            results["convention_changed"] is False
            and results["boundaries"]["convention_change"] is False
        ),
        "technical_attempt1_disclosed": (
            (OUT / "attempt1_pre_correction_stderr.log").is_file()
            and attempt1_disclosure_valid(
                results["execution_history"],
                (OUT / "attempt1_pre_correction_stderr.log").read_text(encoding="utf-8"),
                partial_size=(OUT / "attempt1_partial_probe_records.jsonl").stat().st_size,
            )
        ),
        "no_probe_selection_tuning": (
            results["execution_history"]["probe_selection_tuned_or_replaced"] is False
            and results["boundaries"]["probe_selection_tuning_or_replacement"] is False
        ),
        "all_prohibited_boundaries_false": all(
            results["boundaries"][key] is False
            for key in (
                "real_sky_data",
                "real_object_rows",
                "real_images",
                "sky_positions",
                "sky_statistic",
                "training_or_retraining",
                "weight_reexport",
                "threshold_tuning",
                "probe_selection_tuning_or_replacement",
                "convention_change",
                "acceptance_or_freeze",
                "publication",
                "commit_or_push",
            )
        ),
        "pre_and_final_status_pass": (
            pre_results["status"] == results["status"] == "PASS_BS5_SYNTHETIC_ABSOLUTE_SIGN_ANCHOR"
            and results["absolute_sign_anchor"] == "PASS"
            and results["semantic_image_validation"] == "PASS"
        ),
    }
    verification = {
        "status": "PASS_INDEPENDENT_BS5_SIGN_ANCHOR_REDUCTION" if all(checks.values()) else "FAIL_INDEPENDENT_BS5_SIGN_ANCHOR_REDUCTION",
        "checks": checks,
        "reduced": reduced,
        "frozen_hashes_actual": frozen_actual,
        "runner_import_roots": sorted(runner_imports),
        "results_sha256": sha256_file(RESULTS),
        "pre_correction_results_sha256": sha256_file(PRE_RESULTS),
        "records_sha256": sha256_file(RECORDS),
        "wcs_parity_sha256": sha256_file(WCS_RECEIPT),
    }
    destination = OUT / "independent_verification.json"
    destination.write_text(json.dumps(verification, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps(verification, indent=2, sort_keys=True))
    if not all(checks.values()):
        raise SystemExit(1)


if __name__ == "__main__":
    main()
