#!/usr/bin/env python3
"""Independent stdlib-only static/receipt verifier for the hand-check harness."""
from __future__ import annotations

import ast
import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent
SOURCE = ROOT / "nm_handcheck.py"
TESTS = ROOT / "test_nm_handcheck.py"
SELFTEST = ROOT / "run_synthetic_selftest.py"
RECEIPT = ROOT / "synthetic_selftest_receipt.json"
OUTPUT = ROOT / "independent_verification.json"


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def names_in(node: ast.AST) -> set[str]:
    result = set()
    for child in ast.walk(node):
        if isinstance(child, ast.Name):
            result.add(child.id)
        elif isinstance(child, ast.Attribute):
            result.add(child.attr)
        elif isinstance(child, ast.Constant) and isinstance(child.value, str):
            result.add(child.value)
    return result


def function(tree: ast.Module, name: str) -> ast.FunctionDef:
    for node in tree.body:
        if isinstance(node, ast.FunctionDef) and node.name == name:
            return node
    raise AssertionError(f"missing function: {name}")


def class_node(tree: ast.Module, name: str) -> ast.ClassDef:
    for node in tree.body:
        if isinstance(node, ast.ClassDef) and node.name == name:
            return node
    raise AssertionError(f"missing class: {name}")


def main() -> int:
    source_text = SOURCE.read_text(encoding="utf-8")
    test_text = TESTS.read_text(encoding="utf-8")
    selftest_text = SELFTEST.read_text(encoding="utf-8")
    tree = ast.parse(source_text)
    test_tree = ast.parse(test_text)
    selftest_tree = ast.parse(selftest_text)
    receipt = json.loads(RECEIPT.read_bytes())

    checker_class_names = names_in(class_node(tree, "CheckerApplication"))
    handler_names = names_in(function(tree, "make_checker_http_handler"))
    reduction_names = names_in(function(tree, "reduce_experiment"))
    parser_node = function(tree, "build_argument_parser")
    cli_subcommands = {
        call.args[0].value
        for call in ast.walk(parser_node)
        if isinstance(call, ast.Call)
        and isinstance(call.func, ast.Attribute)
        and call.func.attr == "add_parser"
        and call.args
        and isinstance(call.args[0], ast.Constant)
        and isinstance(call.args[0].value, str)
    }
    handler_routes = {value for value in handler_names if value.startswith("/")}
    imports = {
        alias.name.split(".")[0]
        for parsed_tree in (tree, selftest_tree)
        for node in ast.walk(parsed_tree)
        if isinstance(node, ast.Import)
        for alias in node.names
    }
    imports.update(
        node.module.split(".")[0]
        for parsed_tree in (tree, selftest_tree)
        for node in ast.walk(parsed_tree)
        if isinstance(node, ast.ImportFrom) and node.module
    )
    test_names = {
        node.name
        for node in ast.walk(test_tree)
        if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef)) and node.name.startswith("test_")
    }
    forbidden_checker_symbols = {
        "unseal_key",
        "passphrase",
        "root_secret_hex",
        "instrument_sign",
        "mirrored",
        "stratum",
        "abs_chi",
        "angular_size",
        "object_id",
    }
    forbidden_network_clients = {"requests", "aiohttp", "httpx", "urllib3", "socket"}
    checks = {
        "receipt_status_pass": receipt["status"] == "PASS_FULL_500_SYNTHETIC_HANDCHECK_SELFTEST",
        "receipt_all_checks_pass": receipt["checks_passed"] == receipt["checks_total"] and all(receipt["checks"].values()),
        "receipt_sample_500": receipt["sample_size"] == 500,
        "receipt_nine_strata": len(receipt["stratum_populations"]) == 9,
        "receipt_floor_40": min(receipt["stratum_allocation"].values()) >= 40,
        "receipt_allocation_closes": sum(receipt["stratum_allocation"].values()) == 500,
        "receipt_parity_replay_500": receipt["parity_replay_pixel_exact"] == 500,
        "receipt_has_both_parities": receipt["mirrored"] > 0 and receipt["unmirrored"] > 0,
        "receipt_synthetic_only": "900 generated synthetic images only" in receipt["data_boundary"],
        "receipt_no_real_data": receipt["checks"]["no_real_data_touched"],
        "receipt_checker_order_isolated": receipt["checks"]["checker_orders_independent"] and receipt["checks"]["checker_b_unchanged_while_a_checked"],
        "receipt_wrong_passphrase_rejected": receipt["checks"]["wrong_passphrase_rejected"],
        "receipt_disagreement_only": receipt["checks"]["disagreement_only_adjudication"] and receipt["checks"]["all_disagreements_adjudicated"],
        "receipt_public_aggregate_only": receipt["checks"]["public_exactly_nine_aggregate_rows"] and receipt["checks"]["public_has_only_two_files"],
        "receipt_public_no_truth_fields": receipt["checks"]["public_has_no_item_or_source_id_fields"] and receipt["checks"]["public_has_no_parity_field"] and receipt["checks"]["public_has_no_root_secret"],
        "receipt_harness_hash_current": receipt["harness_source_sha256"] == sha256(SOURCE),
        "receipt_test_hash_current": receipt["test_source_sha256"] == sha256(TESTS),
        "source_parses": isinstance(tree, ast.Module),
        "tests_parse": isinstance(test_tree, ast.Module),
        "selftest_parses": isinstance(selftest_tree, ast.Module),
        "checker_class_has_no_unseal_or_truth_symbols": not (checker_class_names & forbidden_checker_symbols),
        "http_handler_has_no_unseal_or_truth_symbols": not (handler_names & forbidden_checker_symbols),
        "reducer_contains_unseal_and_truth_symbols": {"unseal_key", "instrument_sign", "mirrored", "stratum"} <= reduction_names,
        "crypto_uses_aesgcm_and_scrypt": "AESGCM" in source_text and "Scrypt" in source_text,
        "http_routes_are_exact_allowlist": handler_routes == {"/", "/api/state", "/asset", "/api/answer"},
        "http_has_no_static_directory_route": "SimpleHTTPRequestHandler" not in source_text,
        "cli_subcommands_are_exact_allowlist": cli_subcommands == {"prepare", "check", "adjudicate", "reduce"},
        "no_remote_network_clients": not (imports & forbidden_network_clients),
        "exact_0849_test_present": "0.849" in test_text and "INCONCLUSIVE-BY-POWER" in test_text,
        "zero_disagreement_test_present": any("zero_disagreements" in name for name in test_names),
        "concurrent_append_test_present": any("two_resumed_processes" in name for name in test_names),
        "commitment_tamper_test_present": any("commitment_tampering" in name for name in test_names),
        "minimum_contract_test_count": len(test_names) >= 10,
    }
    failed = sorted(name for name, value in checks.items() if not value)
    result = {
        "schema_version": "nm-handcheck-independent-v1",
        "status": "PASS_INDEPENDENT_BLINDED_HANDCHECK_VERIFICATION" if not failed else "FAIL_INDEPENDENT_BLINDED_HANDCHECK_VERIFICATION",
        "method": "stdlib-only AST, byte-hash, and machine-receipt reduction; production module not imported",
        "checks": checks,
        "checks_passed": sum(checks.values()),
        "checks_total": len(checks),
        "failed_checks": failed,
        "source_sha256": sha256(SOURCE),
        "tests_sha256": sha256(TESTS),
        "selftest_source_sha256": sha256(SELFTEST),
        "selftest_receipt_sha256": sha256(RECEIPT),
        "production_module_imported": False,
        "model_or_estimator_imported": False,
        "real_data_accessed": False,
    }
    OUTPUT.write_bytes(json.dumps(result, sort_keys=True, separators=(",", ":")).encode() + b"\n")
    print(result["status"], result["checks_passed"], "/", result["checks_total"])
    return 0 if not failed else 1


if __name__ == "__main__":
    raise SystemExit(main())
