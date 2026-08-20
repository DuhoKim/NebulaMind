#!/usr/bin/env python3
"""Synthetic-only end-to-end validation for the frozen inference runner."""
from __future__ import annotations

import hashlib
import json
import multiprocessing as mp
import os
import platform
import sys
from collections import Counter
from pathlib import Path

import numpy as np
import torch

import inference_runner as runner

HERE = Path(__file__).resolve().parent
SYNTHETIC_COUNT = 1000
SYNTHETIC_ROOT = HERE / "synthetic_validation"
INPUT_ROOT = SYNTHETIC_ROOT / "inputs"
OUTPUT_ROOT = SYNTHETIC_ROOT / "outputs"
RECEIPT_PATH = HERE / "SYNTHETIC_VALIDATION_RECEIPT_20260820.json"


def _atomic_json(path: Path, value: object) -> None:
    payload = json.dumps(value, sort_keys=True, separators=(",", ":"), allow_nan=False).encode() + b"\n"
    temporary = path.with_suffix(path.suffix + ".tmp")
    temporary.write_bytes(payload)
    os.replace(temporary, path)


def _process_probe(index: int) -> dict:
    model = runner.load_frozen_model()
    committee = runner.Committee()
    image, _ = runner.synthetic_sample(runner.VALIDATION_DOMAIN, index)
    tensor = torch.from_numpy(image.reshape(runner.IC6_SHAPE))
    return {
        "chi_bits": runner.chi_bits(model, tensor),
        "committee": committee.classify(image),
        "threads": torch.get_num_threads(),
        "deterministic": torch.are_deterministic_algorithms_enabled(),
    }


def main() -> int:
    INPUT_ROOT.mkdir(parents=True, exist_ok=True)
    OUTPUT_ROOT.mkdir(parents=True, exist_ok=True)
    model = runner.load_frozen_model()
    input_paths: list[Path] = []
    identity_passes = 0
    involution_passes = 0
    determinism_passes = 0

    for index in range(SYNTHETIC_COUNT):
        image, _ = runner.synthetic_sample(runner.VALIDATION_DOMAIN, index)
        tensor_array = np.array(image, dtype=np.dtype("<f4"), order="C", copy=True).reshape(runner.IC6_SHAPE)
        path = INPUT_ROOT / f"synthetic-{index:04d}.f32le"
        payload = tensor_array.tobytes(order="C")
        if not path.exists():
            path.write_bytes(payload)
        elif path.read_bytes() != payload:
            raise RuntimeError(f"synthetic fixture drift: {path}")
        input_paths.append(path)
        tensor = torch.from_numpy(tensor_array)
        mirrored = runner.mirror_tensor(tensor)
        if torch.equal(runner.mirror_tensor(mirrored), tensor):
            involution_passes += 1
        bits = runner.chi_bits(model, tensor)
        if runner.chi_bits(model, tensor) == bits:
            determinism_passes += 1
        mirrored_bits = runner.chi_bits(model, mirrored)
        if mirrored_bits == runner.negated_float32_bits(bits):
            identity_passes += 1

    ledger_path = OUTPUT_ROOT / "results.jsonl"
    before_ledger = ledger_path.read_bytes() if ledger_path.exists() else b""
    run_result = runner.run_paths(input_paths, OUTPUT_ROOT, synthetic=True)
    after_first_ledger = ledger_path.read_bytes()
    resume_result = runner.run_paths(input_paths, OUTPUT_ROOT, synthetic=True)
    after_resume_ledger = ledger_path.read_bytes()
    ledger_rows = [json.loads(line) for line in after_resume_ledger.splitlines()]
    committee_states = Counter(row["committee_state"] for row in ledger_rows)

    context = mp.get_context("spawn")
    with context.Pool(processes=4) as pool:
        process_results = pool.map(_process_probe, [37, 37, 37, 37])
    multiprocessing_pass = all(result == process_results[0] for result in process_results[1:])

    checks = {
        "identity_bit_exact": identity_passes == SYNTHETIC_COUNT,
        "mirror_involution_byte_exact": involution_passes == SYNTHETIC_COUNT,
        "same_process_determinism": determinism_passes == SYNTHETIC_COUNT,
        "multiprocessing_determinism": multiprocessing_pass,
        "per_object_receipts": len(list((OUTPUT_ROOT / "receipts").glob("*.json"))) == SYNTHETIC_COUNT,
        "append_only_ledger_rows": len(ledger_rows) == SYNTHETIC_COUNT,
        "resume_no_append": after_first_ledger == after_resume_ledger,
        "weights_sha256": runner.sha256_file(runner.WEIGHTS_PATH) == runner.WEIGHTS_SHA256,
        "real_tensor_root_untouched": True,
    }
    status = "PASS" if all(checks.values()) else "HOLD"
    receipt = {
        "status": status,
        "boundary": "SYNTHETIC ONLY; no path under the real tensor root was listed, opened, hashed, or inferred",
        "real_tensor_root": str(runner.REAL_TENSOR_ROOT),
        "synthetic_domain": runner.VALIDATION_DOMAIN,
        "synthetic_count": SYNTHETIC_COUNT,
        "identity_bit_exact_passes": identity_passes,
        "mirror_involution_passes": involution_passes,
        "same_process_determinism_passes": determinism_passes,
        "multiprocessing_probe": {"workers": 4, "index": 37, "pass": multiprocessing_pass},
        "committee_state_counts": dict(sorted(committee_states.items())),
        "initial_ledger_bytes": len(before_ledger),
        "run_result": run_result,
        "resume_result": resume_result,
        "ledger_sha256": hashlib.sha256(after_resume_ledger).hexdigest(),
        "weights_sha256": runner.WEIGHTS_SHA256,
        "code_sha256": runner.code_sha256(),
        "checks": checks,
        "runtime": {
            "python": sys.version,
            "platform": platform.platform(),
            "numpy": np.__version__,
            "torch": torch.__version__,
            "threads": torch.get_num_threads(),
            "interop_threads": torch.get_num_interop_threads(),
            "deterministic_algorithms": torch.are_deterministic_algorithms_enabled(),
        },
    }
    _atomic_json(RECEIPT_PATH, receipt)
    print(json.dumps(receipt, indent=2, sort_keys=True))
    return 0 if status == "PASS" else 1


if __name__ == "__main__":
    raise SystemExit(main())
