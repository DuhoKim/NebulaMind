#!/usr/bin/env python3
"""Stdlib-only structural verifier for the accepted HC-1H synthetic build."""
from __future__ import annotations

import ast
import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent
PREREG = ROOT.parent
SOURCE = ROOT / "nm_handcheck.py"
TESTS = ROOT / "test_nm_handcheck.py"
RECEIPT = ROOT / "hc1h_synthetic_selftest_receipt.json"


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def function(tree: ast.Module, name: str) -> ast.FunctionDef:
    for node in tree.body:
        if isinstance(node, ast.FunctionDef) and node.name == name:
            return node
    raise AssertionError(f"missing function {name}")


def source_segment(text: str, node: ast.AST) -> str:
    value = ast.get_source_segment(text, node)
    assert value is not None
    return value


def main() -> int:
    checks: list[str] = []

    def check(condition: bool, name: str) -> None:
        assert condition, name
        checks.append(name)

    source_text = SOURCE.read_text(encoding="utf-8")
    tests_text = TESTS.read_text(encoding="utf-8")
    tree = ast.parse(source_text)
    receipt = json.loads(RECEIPT.read_text(encoding="utf-8"))

    check('SCHEMA_VERSION = "nm-handcheck-v2-hc1h"' in source_text, "schema-v2-hc1h")
    check('HC1H_ROLE = "H"' in source_text, "one-human-role")
    check("HC1H_STATES = (\"agree-confident\", \"disagree\", \"low-confidence\")" in source_text, "committee-state-vocabulary")
    check('"_tmp_YUI_HARNESS_HC1H_BRIEF.md"' in source_text, "brief-authority")
    check('"LANA_ONE_HUMAN_ATTENUATION_20260814.md"' in source_text, "lana-authority")
    check('"HC1H_ACCEPTANCE_20260815.md"' in source_text, "acceptance-authority")
    check('"KUN_HC1H_CLOSE_20260814.md"' in source_text, "kun-close-authority")
    check(sha256(PREREG / "LANA_ONE_HUMAN_ATTENUATION_20260814.md") == "b2590e4213e225f9869fe782cfe0f55d8d8979dcb470752836a5cd31a58453fd", "accepted-authority-hash")
    check("PINNED_AUTHORITY_SHA256" in source_text and "result != PINNED_AUTHORITY_SHA256" in source_text, "active-harness-hard-pins-authority-map")

    prepare = source_segment(source_text, function(tree, "prepare_hc1h_experiment"))
    check("allocate_neyman" in prepare, "neyman-used")
    check("real_total: int = 500" in prepare, "full-real-500")
    check("synthetic_total: int = 200" in prepare, "full-injections-200")
    check("repeat_total: int = 150" in prepare, "full-repeats-150")
    check("real_floor: int = 30" in prepare, "full-floor-30")
    check('(90, 40, 20, 10)' in prepare, "pilot-90-40-20-floor10")
    check('"checker_H"' in prepare, "one-checker-package")
    check('"checker_A"' not in prepare and '"checker_B"' not in prepare and '"checker_J"' not in prepare, "no-abj-in-hc1h-prepare")
    check('mirrored = not bool(parent["mirrored"])' in prepare, "repeat-opposite-parity")
    check("hc1h-stream-order" in prepare, "keyed-interleaving")
    check("replacement_reserve_per_group" in prepare, "hc7-reserve")
    check("_hc1h_strata_from_cutpoints" in prepare and "chi_tertile_cutpoints_from_real_population" in prepare, "common-real-chi-cutpoints-applied-to-injections")
    check("row[\"item_id\"] not in repeated_parent_ids" in prepare, "repeat-reserves-use-distinct-unrepeated-parents")
    check("pilot_private_root" in prepare and "excluded_synthetic_ids" in prepare, "pilot-to-full-fresh-injection-exclusion")
    check('choices=("no-pilot-run", "exclude-completed-pilot")' in source_text, "cli-requires-explicit-pilot-policy")

    allocation = source_segment(source_text, function(tree, "allocate_neyman"))
    check("sqrt" in allocation and "largest" in allocation, "neyman-square-root-and-integer-close")
    check("N_s*sqrt(a_s*(1-a_s))" in allocation, "neyman-formula-documented")
    check("A floor is a lower-bound constraint" in allocation, "neyman-floor-is-not-base-tranche")

    checker_class = next(node for node in tree.body if isinstance(node, ast.ClassDef) and node.name == "CheckerApplication")
    checker_source = source_segment(source_text, checker_class)
    handler_source = source_segment(source_text, function(tree, "make_checker_http_handler"))
    check("unseal_key" not in checker_source, "checker-cannot-unseal")
    check("unseal_key" not in handler_source, "http-cannot-unseal")
    check("checker_H_control.json" in source_text and "session_mac_key_hex" in checker_source, "private-checker-control-separated-from-package")
    check("hmac.new(mac_key" in source_text and "hmac.compare_digest" in source_text, "session-events-use-private-hmac")
    check("ITEM_FLAGGED_HC7" in checker_source, "hc7-specific-event")
    check("SYSTEMATIC_EXPOSURE_HC7" in checker_source, "hc7-systematic-event")
    check("BREAK_ACKNOWLEDGED" in checker_source and "HC1H_SESSION_PRESENTATION_LIMIT = 50" in source_text, "fifty-presentation-break-enforced")
    check("ERGONOMICS_RECORDED" in checker_source, "pilot-ergonomics-event")
    check("Flag suspected synthetic/repeat exposure" in source_text, "hc7-ui-copy")
    check("stale presentation" in checker_source and "debounce" in checker_source, "stale-and-debounce")
    check("fcntl.flock" in checker_source, "interprocess-append-lock")

    stats = source_segment(source_text, function(tree, "hc1h_statistics"))
    verdict = source_segment(source_text, function(tree, "hc1h_verdict"))
    check("(raw - epsilon) / denominator" in stats, "noise-correction")
    check("shared_epsilon_component" in stats, "shared-epsilon-covariance")
    check("additional_covariance" in stats and "separately approved non-negative additional covariance term" in source_text, "unspecified-additional-covariance-fails-closed-for-authorized-run")
    check("repeat_nonflips" in stats and "2.0 * math.sqrt" in stats, "repeat-2sigma")
    check('Decimal("1.645")' in verdict, "one-sided-95-lower-bound")
    check("HC1H_POWER_GATE" in verdict and 'HC1H_POWER_GATE = Decimal("0.7905")' in source_text, "power-threshold")
    check("HC1H_POWER_BOUND_N" in verdict and "HC1H_POWER_BOUND_N = 130_076" in source_text, "power-bound-n")
    check('Decimal("0.85")' in verdict, "quality-floor")
    check('Decimal("0.70")' in verdict, "stratum-floor")
    check('Decimal("0.05")' in verdict, "epsilon-ceiling")

    reduce = source_segment(source_text, function(tree, "reduce_hc1h_experiment"))
    complete_index = reduce.index("application.completed")
    unseal_index = reduce.index("unseal_key")
    check(complete_index < unseal_index, "complete-before-unseal")
    check("HARD_INCONCLUSIVE_HC7_IDENTITY_EXPOSURE" in reduce and '"sealed_key_opened": False' in reduce, "systematic-exposure-published-without-unseal")
    check('assignment["category"] == "real"' in reduce, "real-only-raw-a")
    check('assignment["category"] == "synthetic"' in reduce, "synthetic-error-path")
    check('assignment["category"] != "repeat"' in reduce, "repeat-diagnostic-path")
    check('"by_session_block"' in reduce and '"enters_primary_repeat_gate": False' in reduce, "repeat-drift-reported-by-session-block")
    check("machine_committee_diagnostic" in reduce and '"enters_attenuation": False' in reduce, "machine-committee-published-diagnostic-only")
    check("F10_K_LT_50" in source_text and "_hc1h_public_projection" in reduce, "f10-public-masking")
    check("_hc1h_public_projection" in reduce and "WITHHELD_F10_MASKED_STRATA" in source_text and 'pop("all_corrected_strata_ge_0_70", None)' in source_text, "f10-withholds-masked-gate-and-final-decision")
    check('"pilot_synthetics_count_toward_full": False' in reduce, "pilot-injections-excluded")
    check('"pilot_real_and_retest_values_used_for_pass": False' in reduce and "no a or repeat statistic is produced" in reduce, "pilot-does-not-produce-a-or-condition-on-retests")

    check("test_hc1h_neyman_allocation_honours_floor_30_and_closes_to_500_real" in tests_text, "allocation-contract-test")
    check("test_neyman_recomputes_after_capacity_caps_before_fixing_low_quota" in tests_text, "allocation-cap-before-floor-regression")
    check("test_hc7_specific_exposure_flag" in tests_text, "hc7-contract-test")
    check("test_hc7_systematic_exposure_is_hard_inconclusive_before_key_open" in tests_text, "hc7-systematic-contract-test")
    check("test_hc7_replacement_reserve_exhaustion_records_hard_inconclusive" in tests_text and "REPLACEMENT_RESERVE_EXHAUSTED_HC7" in checker_source, "hc7-reserve-exhaustion-hard-inconclusive")
    check("test_hc1h_pilot_is_150_labels" in tests_text, "pilot-contract-test")
    check("test_hc1h_noise_correction_and_shared_epsilon_covariance" in tests_text, "covariance-contract-test")
    check("test_hc1h_exact_lower_bound_quality_floor_is_never_rounded_up" in tests_text, "unrounded-contract-test")

    check(receipt["status"] == "PASS_HC1H_SYNTHETIC_SELFTEST", "selftest-pass")
    check(receipt["synthetic_only"] is True, "selftest-synthetic-only")
    check(receipt["full"]["labels"] == 850, "selftest-full-850")
    check(receipt["full"]["counts"] == {"real": 500, "synthetic": 200, "repeat": 150}, "selftest-full-breakdown")
    check(receipt["full"]["allocation_total"] == 500 and receipt["full"]["allocation_floor_min"] >= 30, "selftest-allocation")
    check(receipt["full"]["repeat_later"] == 150 and receipt["full"]["repeat_parity_complement"] == 150, "selftest-repeat-order-parity")
    check(receipt["full"]["specific_hc7_flags_replaced"] == 1, "selftest-hc7-replacement")
    check(receipt["full"]["breaks_acknowledged"] == 17, "selftest-full-breaks")
    check(
        receipt["full"]["private_fixture_verdict"] == "PASS_HC1H_ATTENUATION"
        and receipt["full"]["public_f10_verdict"] == "WITHHELD_F10_MASKED_STRATA",
        "selftest-private-pass-public-f10-withheld",
    )
    check(receipt["pilot"]["labels"] == 150 and receipt["pilot"]["outcome"] == "PASS-TO-FULL-HC1H", "selftest-pilot")
    check(receipt["pilot"]["synthetics_count_toward_full"] is False, "selftest-pilot-exclusion")
    check(receipt["pilot"]["breaks_acknowledged"] == 2, "selftest-pilot-breaks")
    check(receipt["pilot"]["fresh_full_exclusion_verified"] is True, "selftest-fresh-full-injections")
    check(receipt["artifacts"]["harness_sha256"] == sha256(SOURCE), "receipt-harness-hash")
    check(receipt["artifacts"]["tests_sha256"] == sha256(TESTS), "receipt-tests-hash")

    output = {
        "status": "PASS_INDEPENDENT_HC1H_VERIFICATION",
        "checks_passed": len(checks),
        "checks": checks,
        "harness_sha256": sha256(SOURCE),
        "tests_sha256": sha256(TESTS),
        "selftest_receipt_sha256": sha256(RECEIPT),
    }
    path = ROOT / "hc1h_independent_verification.json"
    path.write_text(json.dumps(output, sort_keys=True, separators=(",", ":")) + "\n", encoding="utf-8")
    print(f"PASS_INDEPENDENT_HC1H_VERIFICATION {len(checks)} / {len(checks)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
