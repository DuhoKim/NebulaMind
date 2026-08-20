#!/usr/bin/env python3
"""Independent stdlib-only mechanical verifier for the GPT1 rehearsal."""
from __future__ import annotations

import hashlib
import json
import os
import stat
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parent
SUMMARY = json.loads((ROOT / "rehearsal_summary.json").read_text())
N = 20000
FORBIDDEN_PACKAGE_KEYS = {
    "root_secret_hex", "object_id", "image_path", "instrument_sign", "abs_chi",
    "committee_state", "category", "parent_item_id", "synthetic_id", "truth_sign",
    "stratum", "mirrored", "sealed_key",
}
checks: list[str] = []


def check(condition: bool, name: str) -> None:
    if not condition:
        raise AssertionError(name)
    checks.append(name)


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1 << 20), b""):
            digest.update(chunk)
    return digest.hexdigest()


def rows(path: Path) -> list[dict]:
    return [json.loads(line) for line in path.read_text().splitlines() if line.strip()]


def keys_recursive(value):
    if isinstance(value, dict):
        for key, child in value.items():
            yield key
            yield from keys_recursive(child)
    elif isinstance(value, list):
        for child in value:
            yield from keys_recursive(child)


truth = rows(ROOT / "synthetic_truth.jsonl")
inference = rows(ROOT / "inference" / "results.jsonl")
committee = rows(ROOT / "committee_results.jsonl")
real_population = rows(ROOT / "hc1h_real_population.jsonl")
synthetic_pool = rows(ROOT / "hc1h_synthetic_pool.jsonl")
check(len(truth) == len(inference) == len(committee) == len(real_population) == len(synthetic_pool) == N, "all-campaign-row-counts-20000")
check(len({row["object_id"] for row in truth}) == N, "truth-identities-unique")
check(len({row["generator_index"] for row in truth}) == N, "generator-indices-unique")
check(sorted(row["generator_index"] for row in truth) == list(range(N)), "natural-first-20000-draws-no-preselection")

truth_by_id = {row["object_id"]: row for row in truth}
inference_by_id = {row["object_id"].rsplit("-", 1)[0]: row for row in inference}
committee_by_id = {row["object_id"]: row for row in committee}
check(set(truth_by_id) == set(inference_by_id) == set(committee_by_id), "ledger-identity-sets-match")

correct = 0
states = Counter()
for object_id, truth_row in truth_by_id.items():
    tensor = Path(truth_row["tensor_path"])
    image = Path(truth_row["png_path"])
    check(ROOT in tensor.resolve().parents and ROOT in image.resolve().parents, f"paths-contained-{object_id}")
    check(not tensor.is_symlink() and not image.is_symlink(), f"paths-not-symlinks-{object_id}")
    check(tensor.stat().st_size == 65536, f"tensor-size-{object_id}")
    check(sha256(tensor) == truth_row["tensor_sha256"], f"tensor-hash-{object_id}")
    chi = float(inference_by_id[object_id]["chi_value"])
    chi_sign = 1 if chi > 0 else -1 if chi < 0 else 0
    correct += int(chi_sign == int(truth_row["truth_sign"]))
    state_name = committee_by_id[object_id]["committee_state"]
    states[state_name] += 1
    check(state_name == inference_by_id[object_id]["committee_state"], f"committee-crosscheck-{object_id}")
check(correct == SUMMARY["chi"]["direct_correct"], "chi-accuracy-count-recomputed")
check(states == Counter(SUMMARY["committee_distribution"]), "committee-distribution-recomputed")

check(sum(row["population"] for row in SUMMARY["strata"]) == N, "strata-population-closes-20000")
check(sum(row["allocation"] for row in SUMMARY["strata"]) == 500, "allocation-closes-500")
check(len(SUMMARY["strata"]) == 9, "exactly-nine-strata")
check(all(row["population"] >= 30 and row["allocation"] >= 30 for row in SUMMARY["strata"]), "all-strata-floor-30")
check(SUMMARY["real_projection"]["allocator_floor_30_passes"] is True, "projected-real-run-floor-pass")
check(SUMMARY["real_projection"]["minimum_projected_population"] >= 30, "projected-minimum-population-at-least-30")

package_path = ROOT / "hc1h_checking" / "checker_H" / "package.json"
package = json.loads(package_path.read_text())
check(len(package["items"]) == 850, "blinded-package-850-items")
check(not (set(keys_recursive(package)) & FORBIDDEN_PACKAGE_KEYS), "checker-package-has-no-private-keys")
for item in package["items"]:
    asset = package_path.parent / item["asset"]
    check(asset.is_file() and not asset.is_symlink(), f"checker-asset-regular-{item['sequence']}")
    check(sha256(asset) == item["asset_sha256"], f"checker-asset-hash-{item['sequence']}")
check(not (package_path.parent / "answers.jsonl").exists(), "no-answer-ledger-before-first-event")
check(SUMMARY["hc1h"]["session_completed"] == 0, "zero-labels-submitted")

sealed = ROOT / "hc1h_private" / "sealed_key.nmhc"
passphrase = ROOT / "hc1h.passphrase"
commitment = ROOT / "hc1h_checking" / "commitment.json"
check(sealed.is_file() and sealed.stat().st_size > 0, "sealed-key-envelope-present")
check(sha256(sealed) == SUMMARY["hc1h"]["sealed_key_sha256"], "sealed-key-envelope-hash")
check(stat.S_IMODE(passphrase.stat().st_mode) == 0o600, "passphrase-mode-600")
check(sha256(commitment) == SUMMARY["hc1h"]["commitment_sha256"], "commitment-hash")
check((ROOT / "attempt1_sparse_strata_hold").is_dir(), "sparse-strata-failed-attempt-preserved")
check((ROOT / "attempt2_hold").is_dir(), "hc7-reserve-failed-attempt-preserved")
check((ROOT.parent / "GPT1_REHEARSAL_DONE.md").read_text().splitlines()[0].startswith("GPT1_REHEARSAL_COMPLETE"), "lane-done-marker-complete")

receipt_paths = [Path(row["tensor_path"]) for row in truth] + [Path(row["image_path"]) for row in real_population] + [Path(row["image_path"]) for row in synthetic_pool]
check(all(ROOT in path.resolve().parents for path in receipt_paths), "all-operational-input-paths-contained-in-rehearsal")
check(all("NebulaMindData" not in str(path) for path in receipt_paths), "no-real-data-operational-path")

receipt = {
    "status": "PASS_INDEPENDENT_REHEARSAL_VERIFICATION",
    "checks": len(checks),
    "objects": N,
    "tensors_verified": N,
    "checker_assets_verified": 850,
    "chi_correct": correct,
    "committee_distribution": dict(states),
    "allocation_total": 500,
    "minimum_population": min(row["population"] for row in SUMMARY["strata"]),
    "minimum_allocation": min(row["allocation"] for row in SUMMARY["strata"]),
    "labels_submitted": 0,
    "sealed_key_sha256": sha256(sealed),
    "real_data_operational_paths": 0,
}
(ROOT / "independent_verification.json").write_text(json.dumps(receipt, sort_keys=True, indent=2) + "\n")
SUMMARY["independent_verification"] = {
    "status": receipt["status"],
    "checks": len(checks),
    "receipt": str(ROOT / "independent_verification.json"),
}
(ROOT / "rehearsal_summary.json").write_text(json.dumps(SUMMARY, sort_keys=True, indent=2) + "\n")
import importlib.util
spec = importlib.util.spec_from_file_location("gpt1_rehearsal_report_renderer", ROOT / "run_rehearsal.py")
if spec is None or spec.loader is None:
    raise RuntimeError("cannot load rehearsal report renderer")
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)
(ROOT / "REHEARSAL_REPORT_20260820.md").write_text(module.render_report(SUMMARY))
print(json.dumps(receipt, sort_keys=True))
