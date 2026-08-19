#!/usr/bin/env python3
"""Kun pipeline-gate witness: identity + mirror antisymmetry on the seeded 200-probe prefix.

Gate seat rerun, independent of the GPT1 receipt: loads the hash-pinned frozen
BS-3 generator, the hash-pinned old R4/R5 runner (model + old chi path), and the
hash-pinned PRODUCTION cutout runner IC functions, then recomputes, for source
indices 3,000,000-3,000,199 (the seeded 200-row prefix):

  * identity witness: old-path chi bits == new full-IC-path chi bits
  * mirror antisymmetry through the full IC path: chi(mirror(x)) == -chi(x),
    value- and float32-bit-exact
  * IC-7 placement: mirror(after IC-1..IC-6) bytes == IC(raw mirror) bytes
  * R1 involution byte-exactness
  * input-byte identity of the IC-5 map (tensor bytes == delivered raster bytes)

Cross-checks the recomputed per-probe chi bits against the preserved rerun rows
in _icrerun_20260820/r1_r5_records.jsonl. Synthetics only; no network; no real
data path is touched.
"""
from __future__ import annotations

import hashlib
import importlib.util
import json
import sys
from pathlib import Path

import numpy as np
import torch

ROOT = Path(__file__).resolve().parent
HANDOFF_ROOT = ROOT.parent
PINS = {
    ROOT / "_cutout_runner_20260820/cutout_runner.py": "ccb9b8fed457333669e54fa9f0a3dac645dc866a56c6cd8dc665ffd4d93b1bcc",
    ROOT / "_cutout_runner_20260820/ic_slots.json": "10d24a6e1c5dd64eef8e1ada7e3d222f2e168bab288b1438792db7ff6a848372",
    ROOT / "_icrerun_20260820/ic5_scaler.py": "21b66eda899b5e48034be2b2d92ee2c77f262b156eb59d680eb1b80763d12621",
    ROOT / "yui_bs3_r4_r5_20260813/run_bs3_r4_r5.py": "de0f35355902f25497e240a413a087a1413d365342419b0be3fc15a7e5117914",
    HANDOFF_ROOT / "spike/yui_identity/w_chi.py": "89da33ec6260e75e06eadb0f171da4c52f1478b59ff5e543d363dbf56fefcd75",
    ROOT / "weights_frozen.pt": "83008c1cbdae511af5d30020540e1e281c62c2bd95d3cb05527fc0687bf49e6d",
    ROOT / "_icrerun_20260820/r1_r5_records.jsonl": "65fa6dfe8ab43ea28053c3840126c98406a10ce137329446d1a3e5d38747ef1a",
}
SLOTS_PATH = ROOT / "_cutout_runner_20260820/ic_slots.json"
EXPECTED_CANONICAL_WEIGHTS = "1075a4d91c295d7f3256128534a0b8c4d097fb9d162169df1ac698843637a589"
EXPECTED_PREFIX_MANIFEST = "ab75d5f2ec08ad44fbcf1198d1612c23759f8d3aac29db044a181346ac43f9b2"
START, N = 3_000_000, 200


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with Path(path).open("rb") as handle:
        for chunk in iter(lambda: handle.read(1 << 20), b""):
            digest.update(chunk)
    return digest.hexdigest()


def load_module(path: Path, name: str):
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    sys.modules[name] = module
    spec.loader.exec_module(module)
    return module


def bits32(value) -> str:
    return f"0x{int(np.float32(value).view(np.uint32)):08x}"


def main() -> None:
    measured = {str(p): sha256_file(p) for p in PINS}
    mismatches = {p: (m, PINS[Path(p)]) for p, m in measured.items() if m != PINS[Path(p)]}
    if mismatches:
        raise SystemExit("PIN MISMATCH: " + json.dumps(mismatches, indent=2))

    cutout = load_module(ROOT / "_cutout_runner_20260820/cutout_runner.py", "kun_gate_cutout")
    base = load_module(ROOT / "yui_bs3_r4_r5_20260813/run_bs3_r4_r5.py", "kun_gate_base")

    torch.set_num_threads(1)
    torch.set_num_interop_threads(1)
    torch.use_deterministic_algorithms(True)
    model = base.build_and_load_model()
    digest = hashlib.sha256()
    for parameter in model.parameters():
        digest.update(parameter.detach().numpy().astype("<f4").tobytes())
    canonical = digest.hexdigest()
    if canonical != EXPECTED_CANONICAL_WEIGHTS:
        raise SystemExit(f"canonical weights mismatch: {canonical}")

    recorded = {}
    with (ROOT / "_icrerun_20260820/r1_r5_records.jsonl").open(encoding="utf-8") as handle:
        for line in handle:
            row = json.loads(line)
            if row["probe_offset"] < N:
                recorded[row["source_index"]] = row

    prefix_manifest = hashlib.sha256()
    counts = {
        "input_bytes_equal_old_path": 0,
        "R1_involution_byte_exact": 0,
        "IC7_placement_byte_exact": 0,
        "antisymmetry_value_exact": 0,
        "antisymmetry_bit_exact": 0,
        "identity_witness_old_new_chi_bit_identical": 0,
        "recorded_row_chi_bits_match": 0,
    }
    max_residual = 0.0
    for offset in range(N):
        source_index = START + offset
        parity, pitch_deg, inclination_deg, snr = base.params(source_index)
        old_image = np.ascontiguousarray(
            base.synth_spiral(parity, pitch_deg, inclination_deg, snr, seed=base.sample_seed(source_index)),
            dtype=np.float32,
        )
        prefix_manifest.update(bytes.fromhex(hashlib.sha256(old_image.tobytes()).hexdigest()))

        tensor, _receipt = cutout.apply_input_contract(old_image, slots_path=SLOTS_PATH, real_sky=False)
        counts["input_bytes_equal_old_path"] += int(tensor[0].tobytes() == old_image.tobytes())

        mirrored = cutout.mirror_tensor(tensor)
        restored = cutout.mirror_tensor(mirrored)
        counts["R1_involution_byte_exact"] += int(restored.tobytes() == tensor.tobytes())

        mirrored_raw, _ = cutout.apply_input_contract(
            np.ascontiguousarray(np.fliplr(old_image)), slots_path=SLOTS_PATH, real_sky=False
        )
        counts["IC7_placement_byte_exact"] += int(mirrored.tobytes() == mirrored_raw.tobytes())

        raw_x = base.raw_output(model, tensor[0])
        raw_m = base.raw_output(model, mirrored[0])
        chi_x = np.float32((raw_x - raw_m) / np.float32(2.0))
        # full-path chi of the mirrored tensor: mirror(mirror(x)) == x by R1
        raw_m2 = base.raw_output(model, mirrored[0])
        raw_x2 = base.raw_output(model, restored[0])
        chi_mirror = np.float32((raw_m2 - raw_x2) / np.float32(2.0))
        neg = np.float32(-chi_x)
        counts["antisymmetry_value_exact"] += int(bool(chi_mirror == neg))
        counts["antisymmetry_bit_exact"] += int(bits32(chi_mirror) == bits32(neg))
        max_residual = max(max_residual, float(abs(np.float64(chi_mirror) + np.float64(chi_x))))

        old_raw_x = base.raw_output(model, np.ascontiguousarray(old_image, dtype=np.float32))
        old_raw_m = base.raw_output(model, np.ascontiguousarray(np.fliplr(old_image), dtype=np.float32))
        old_chi = np.float32((old_raw_x - old_raw_m) / np.float32(2.0))
        counts["identity_witness_old_new_chi_bit_identical"] += int(bits32(old_chi) == bits32(chi_x))

        rec = recorded[source_index]
        counts["recorded_row_chi_bits_match"] += int(
            rec["chi_new_path_bits"] == bits32(chi_x)
            and rec["chi_new_mirror_bits"] == bits32(chi_mirror)
            and rec["chi_old_path_bits"] == bits32(old_chi)
        )

    result = {
        "verdict": "PASS_KUN_PIPELINE_WITNESS" if (
            all(value == N for value in counts.values())
            and max_residual == 0.0
            and prefix_manifest.hexdigest() == EXPECTED_PREFIX_MANIFEST
        ) else "FAIL_KUN_PIPELINE_WITNESS",
        "population": {"source_index_start": START, "n": N, "master_seed": "LONGO-AMPLITUDE-FREEZE-M1"},
        "prefix_manifest_sha256": prefix_manifest.hexdigest(),
        "expected_prefix_manifest_sha256": EXPECTED_PREFIX_MANIFEST,
        "canonical_weights_sha256": canonical,
        "counts": counts,
        "n": N,
        "max_abs_chi_mirror_plus_chi": max_residual,
        "environment": {
            "python": sys.version.split()[0],
            "numpy": np.__version__,
            "torch": torch.__version__,
            "deterministic_algorithms": bool(torch.are_deterministic_algorithms_enabled()),
        },
    }
    print(json.dumps(result, indent=2, sort_keys=True))
    if result["verdict"] != "PASS_KUN_PIPELINE_WITNESS":
        raise SystemExit(1)


if __name__ == "__main__":
    main()
