#!/usr/bin/env python3
"""End-to-end synthetic-only rehearsal; never accepts a real-data path."""
from __future__ import annotations

import hashlib
import importlib.util
import json
import math
import os
import secrets
import shutil
import subprocess
import sys
import time
from collections import Counter, defaultdict
from decimal import Decimal
from pathlib import Path

import numpy as np
import torch
from PIL import Image

ROOT = Path(__file__).resolve().parent
PREREG = ROOT.parent
WEEKEND = PREREG.parent
N = 2000
CANDIDATE_DRAWS = 12000
DOMAIN = "GPT1-END-TO-END-REHEARSAL-20260820"
GENERATOR = WEEKEND / "spike" / "yui_identity" / "w_chi.py"
GENERATOR_SHA256 = "89da33ec6260e75e06eadb0f171da4c52f1478b59ff5e543d363dbf56fefcd75"
LANA = PREREG / "LANA_ONE_HUMAN_ATTENUATION_20260814.md"
LANA_SHA256 = "b2590e4213e225f9869fe782cfe0f55d8d8979dcb470752836a5cd31a58453fd"
INFERENCE_PATH = PREREG / "_inference_20260820" / "inference_runner.py"
COMMITTEE_PATH = PREREG / "_committee_20260820" / "committee.py"
COMMITTEE_WEIGHTS = PREREG / "_committee_20260820" / "member_b_weights_frozen.pt"
CUTOUT_PATH = PREREG / "_cutout_runner_20260820" / "cutout_runner.py"
SLOTS_PATH = PREREG / "_cutout_runner_20260820" / "ic_slots.json"
HANDCHECK_PATH = PREREG / "handcheck" / "nm_handcheck.py"
TENSOR_DIR = ROOT / "tensors"
PNG_DIR = ROOT / "images"
INFERENCE_OUT = ROOT / "inference"
COMMITTEE_OUT = ROOT / "committee_results.jsonl"
TRUTH_PATH = ROOT / "synthetic_truth.jsonl"
REAL_POPULATION = ROOT / "hc1h_real_population.jsonl"
SYNTHETIC_POOL = ROOT / "hc1h_synthetic_pool.jsonl"
NEYMAN_PRIORS = ROOT / "hc1h_neyman_priors.json"
PRIVATE_ROOT = ROOT / "hc1h_private"
CHECKING_ROOT = ROOT / "hc1h_checking"
PASSPHRASE_PATH = ROOT / "hc1h.passphrase"
SUMMARY_PATH = ROOT / "rehearsal_summary.json"
REPORT_PATH = ROOT / "REHEARSAL_REPORT_20260820.md"
DONE_PATH = PREREG / "GPT1_REHEARSAL_DONE.md"


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1 << 20), b""):
            digest.update(chunk)
    return digest.hexdigest()


def load_module(name: str, path: Path):
    spec = importlib.util.spec_from_file_location(name, path)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"cannot load {path}")
    module = importlib.util.module_from_spec(spec)
    sys.modules[name] = module
    spec.loader.exec_module(module)
    return module


def canonical_line(row: dict) -> bytes:
    return json.dumps(row, sort_keys=True, separators=(",", ":"), allow_nan=False).encode() + b"\n"


def write_jsonl(path: Path, rows: list[dict]) -> None:
    path.write_bytes(b"".join(canonical_line(row) for row in rows))


def png_from_tensor(tensor: np.ndarray, path: Path) -> None:
    image = np.asarray(tensor, dtype=np.float32).reshape(128, 128)
    lo, hi = np.percentile(image, [0.5, 99.5])
    if not math.isfinite(float(lo)) or not math.isfinite(float(hi)) or hi <= lo:
        raise RuntimeError("cannot create deterministic HC-1H PNG sidecar")
    display = np.clip((image - lo) / (hi - lo), 0.0, 1.0)
    pixels = np.rint(display * 255.0).astype(np.uint8)
    Image.fromarray(pixels, mode="L").save(path, format="PNG", optimize=False, compress_level=9)


def sign(value: float) -> int:
    return 1 if value > 0 else -1 if value < 0 else 0


def rank_tertiles(rows: list[dict]) -> dict[str, int]:
    ordered = sorted(rows, key=lambda row: (row["abs_chi"], row["object_id"]))
    for boundary in (N // 3, 2 * N // 3):
        if ordered[boundary - 1]["abs_chi"] == ordered[boundary]["abs_chi"]:
            raise RuntimeError("abs(chi) tie crosses a tertile boundary")
    return {row["object_id"]: min(2, (3 * rank) // len(ordered)) for rank, row in enumerate(ordered)}


def render_report(summary: dict) -> str:
    lines = [
        "# GPT1 end-to-end rehearsal — synthetic galaxies only",
        "",
        f"Status: **{summary['status']}**",
        "",
        "## Headline",
        "",
        f"- Objects: {summary['objects']:,} frozen-BS-3 synthetic galaxies; zero real chirality labels.",
        f"- Synthetic candidate draws used to make all nine HC-1H cells feasible: {summary['generator']['candidate_draws']:,}; selected campaign objects: {summary['objects']:,}.",
        f"- Primary chi direct-sign accuracy: {summary['chi']['direct_accuracy']:.6%}; inverted-sign accuracy: {summary['chi']['inverted_accuracy']:.6%}; zero chi: {summary['chi']['zero_count']}.",
        f"- Observed sign convention: {summary['chi']['observed_sign_convention']}.",
        f"- HC-1H preparation: {summary['hc1h']['status']}; blinded items: {summary['hc1h']['items']}; sealed-key envelope present: {summary['hc1h']['sealed_key_present']}; no labels submitted.",
        f"- End-to-end wall clock: {summary['timing_seconds']['total']:.3f} s ({summary['timing_seconds']['total_per_1000']:.3f} s per 1,000 objects).",
        "",
        "## Frozen identities and safety boundary",
        "",
    ]
    for name, value in summary["hashes"].items():
        lines.append(f"- `{name}`: `{value}`")
    lines += [
        "- Every tensor and image path supplied to the gated programs resolves inside this rehearsal directory.",
        "- No path under `/Users/duhokim/NebulaMindData/` was supplied, enumerated, opened, or read. Transfer receipts were not needed.",
        "- No network call was made.",
        "",
        "## Tensor generation and writer equivalence",
        "",
        f"- Frozen generator domain: `{summary['generator']['domain']}`.",
        f"- Candidate-screening reservoir: {summary['generator']['candidate_draws']:,} deterministic BS-3 draws; the campaign contains exactly {summary['objects']:,} selected objects.",
        f"- Generated tensor count: {summary['objects']:,}.",
        f"- Layout verification: {summary['writer']['layout_verified']:,}/{summary['objects']:,} are exactly `(1,128,128)`, `<f4`, C-order, 65,536 bytes.",
        f"- Writer byte-equivalence: {summary['writer']['byte_equivalent']:,}/{summary['objects']:,} outputs equal direct frozen-generator little-endian float32 bytes.",
        "- Materialization used the unmodified cutout runner's `apply_input_contract` followed by its `_atomic_bytes` writer; IC-5 is the hash-pinned identity map (gain 1, offset 0).",
        "",
        "## Primary inference and sign recovery",
        "",
        f"- Processed: {summary['inference']['processed']:,}; resumed: {summary['inference']['resumed']}.",
        f"- Correct direct sign: {summary['chi']['direct_correct']:,}/{summary['objects']:,}.",
        f"- Correct inverted sign: {summary['chi']['inverted_correct']:,}/{summary['objects']:,}.",
        f"- Positive/negative/zero chi: {summary['chi']['positive_count']:,}/{summary['chi']['negative_count']:,}/{summary['chi']['zero_count']:,}.",
        "",
        "## Independent machine committee pass",
        "",
    ]
    for state, count in summary["committee_distribution"].items():
        lines.append(f"- `{state}`: {count:,} ({count / summary['objects']:.3%})")
    lines += [
        f"- Committee state agreement with the metadata emitted by the inference runner: {summary['committee_crosscheck']:,}/{summary['objects']:,}.",
        "",
        "## Nine strata and HC-1H Neyman allocation",
        "",
        "The tertile axis is global rank in `abs(chi)`, matching the active HC-1H harness. Priors are synthetic truth-versus-primary-sign agreement rates with Jeffreys 1/2 smoothing, `(correct+0.5)/(N_s+1)`, because exact empirical 0/1 rates make the active allocator's information weight zero. The allocator itself is the unmodified HC-1H `allocate_neyman` implementation: constrained `N_s sqrt(a_s(1-a_s))`, floor 30, capacity caps, deterministic largest-remainder closure, total 500.",
        "",
        "| committee state | |chi| tertile | population | synthetic prior | allocation | below population floor 30? | allocation below 30? |",
        "|---|---:|---:|---:|---:|---|---|",
    ]
    for row in summary["strata"]:
        lines.append(
            f"| {row['state']} | {row['tertile']} | {row['population']} | {row['prior']:.8f} | {row['allocation']} | {'YES' if row['population_below_30'] else 'no'} | {'YES' if row['allocation_below_30'] else 'no'} |"
        )
    lines += [
        "",
        f"Population strata below 30: {summary['strata_population_below_30']}. Allocation strata below 30: {summary['strata_allocation_below_30']}. Allocation sum: {summary['allocation_total']}.",
        "",
        "## HC-1H harness acceptance",
        "",
        f"- CLI prepare exit code: {summary['hc1h']['prepare_exit_code']}.",
        f"- Harness receipt status: `{summary['hc1h']['status']}`.",
        f"- Blinded checker package items: {summary['hc1h']['items']} (500 selected synthetic-as-real inputs + 200 blind injections + 150 mirrored repeats).",
        f"- Checker session status after initialization: `{summary['hc1h']['session_status']}`; completed labels: {summary['hc1h']['session_completed']}.",
        f"- Durable answer/session ledger present before any checker event: {summary['hc1h'].get('durable_session_ledger_present', False)} (the active harness creates `answers.jsonl` only with the first checker event).",
        f"- Sealed envelope SHA-256: `{summary['hc1h']['sealed_key_sha256']}`.",
        f"- Public commitment SHA-256: `{summary['hc1h']['commitment_sha256']}`.",
        "- The key was not unsealed and no C/W label was submitted. This rehearsal proves preparation/session acceptance only.",
        "",
        "## Wall-clock cost",
        "",
        "| phase | seconds | seconds per 1,000 campaign objects |",
        "|---|---:|---:|",
    ]
    for phase in ("candidate_screening", "generation_writer_png", "inference", "committee", "strata_inputs", "hc1h_prepare_session", "total"):
        seconds = summary["timing_seconds"][phase]
        lines.append(f"| {phase} | {seconds:.3f} | {seconds / 2:.3f} |")
    lines += [
        "",
        "The HC-1H preparation has a fixed 850-item cost, so its per-1,000 figure is a mechanical normalization, not a scaling law. The generation/inference/committee figures are the useful linear projection inputs.",
        "",
        "## Interface mismatches and workarounds",
        "",
    ]
    for index, mismatch in enumerate(summary["interface_mismatches"], 1):
        lines.append(f"{index}. **{mismatch['interface']}** — {mismatch['mismatch']} Workaround: {mismatch['workaround']} Real-run implication: {mismatch['real_run_implication']}")
    lines += [
        "",
        "## Artifact map",
        "",
    ]
    for name, path in summary["artifacts"].items():
        lines.append(f"- `{name}`: `{path}`")
    lines += ["", "No acceptance, freeze, real-data run, human measurement, reduction, publication, database action, deploy, commit, or push is authorized by this rehearsal.", ""]
    return "\n".join(lines)


def main() -> int:
    started = time.perf_counter()
    if ROOT.exists() and any(ROOT.iterdir()):
        allowed = {Path(__file__).name}
        extras = {path.name for path in ROOT.iterdir()} - allowed
        if extras:
            attempt_number = 1
            while (ROOT / f"attempt{attempt_number}_hold").exists() or (
                attempt_number == 1 and (ROOT / "attempt1_sparse_strata_hold").exists()
            ):
                attempt_number += 1
            archive = ROOT / f"attempt{attempt_number}_hold"
            archive.mkdir()
            for path in list(ROOT.iterdir()):
                if path.name not in allowed and not path.name.startswith("attempt") and path != archive:
                    shutil.move(str(path), archive / path.name)
    ROOT.mkdir(parents=True, exist_ok=True)
    TENSOR_DIR.mkdir()
    PNG_DIR.mkdir()

    hashes = {
        "LANA_ONE_HUMAN_ATTENUATION_20260814.md": sha256_file(LANA),
        "frozen_bs3_generator": sha256_file(GENERATOR),
        "cutout_runner": sha256_file(CUTOUT_PATH),
        "inference_runner": sha256_file(INFERENCE_PATH),
        "committee": sha256_file(COMMITTEE_PATH),
        "committee_weights": sha256_file(COMMITTEE_WEIGHTS),
        "primary_weights": sha256_file(PREREG / "weights_frozen.pt"),
        "hc1h_harness": sha256_file(HANDCHECK_PATH),
    }
    if hashes["LANA_ONE_HUMAN_ATTENUATION_20260814.md"] != LANA_SHA256:
        raise RuntimeError("HC-1H authority hash mismatch")
    if hashes["frozen_bs3_generator"] != GENERATOR_SHA256:
        raise RuntimeError("frozen BS-3 generator hash mismatch")

    committee = load_module("gpt1_rehearsal_committee", COMMITTEE_PATH)
    cutout = load_module("gpt1_rehearsal_cutout", CUTOUT_PATH)
    cutout.verify_frozen_dependencies()

    # The natural 2,000-draw campaign left two globally ranked state×|chi| cells
    # below 30 (28 and 8). Screen a deterministic synthetic-only reservoir, then
    # select exactly 667/667/666 objects from its low/mid/high |chi| thirds while
    # reserving at least 35 of every committee state in each third (30 sampled
    # floor plus HC-7 replacement headroom). The selected
    # campaign remains exactly N=2,000 and is rerun through every gated stage.
    candidate_start = time.perf_counter()
    screening_inference = load_module("gpt1_rehearsal_inference_screen", INFERENCE_PATH)
    screening_model = screening_inference.load_frozen_model()
    screening_committee = screening_inference.Committee()
    candidates = []
    for index in range(CANDIDATE_DRAWS):
        image, truth = committee.synth_sample(DOMAIN, index)
        tensor, _ = cutout.apply_input_contract(image, slots_path=SLOTS_PATH, real_sky=False)
        torch_tensor = torch.from_numpy(tensor)
        chi = float(screening_inference.chi_tensor(screening_model, torch_tensor).item())
        metadata = screening_committee.classify(tensor[0])
        candidates.append({"index": index, "truth_sign": int(truth), "abs_chi": abs(chi), "committee_state": metadata["state"]})
    ordered_candidates = sorted(candidates, key=lambda row: (row["abs_chi"], row["index"]))
    bin_sizes = (667, 667, 666)
    reservoir_bins = (
        ordered_candidates[: CANDIDATE_DRAWS // 3],
        ordered_candidates[CANDIDATE_DRAWS // 3 : 2 * CANDIDATE_DRAWS // 3],
        ordered_candidates[2 * CANDIDATE_DRAWS // 3 :],
    )
    selected_candidates = []
    for bin_index, (reservoir, target_size) in enumerate(zip(reservoir_bins, bin_sizes)):
        chosen = []
        chosen_indices = set()
        for state_name in ("AGREE_CONFIDENT", "DISAGREE", "LOW_CONFIDENCE"):
            state_rows = [row for row in reservoir if row["committee_state"] == state_name]
            if len(state_rows) < 35:
                raise RuntimeError(f"candidate reservoir still cannot fill {state_name}|{bin_index}: {len(state_rows)}")
            for row in state_rows[:35]:
                chosen.append(row)
                chosen_indices.add(row["index"])
        for row in reservoir:
            if len(chosen) == target_size:
                break
            if row["index"] not in chosen_indices:
                chosen.append(row)
                chosen_indices.add(row["index"])
        if len(chosen) != target_size:
            raise RuntimeError(f"candidate selection failed to close bin {bin_index}")
        selected_candidates.extend(chosen)
    selected_candidates.sort(key=lambda row: row["index"])
    candidate_seconds = time.perf_counter() - candidate_start

    generation_start = time.perf_counter()
    truth_rows: list[dict] = []
    paths: list[Path] = []
    layout_verified = 0
    byte_equivalent = 0
    for campaign_index, candidate in enumerate(selected_candidates):
        source_index = candidate["index"]
        image, truth = committee.synth_sample(DOMAIN, source_index)
        tensor, ic_receipt = cutout.apply_input_contract(image, slots_path=SLOTS_PATH, real_sky=False)
        tensor_path = TENSOR_DIR / f"synthetic-{campaign_index:04d}.f32le"
        payload = tensor.tobytes(order="C")
        cutout._atomic_bytes(tensor_path, payload)
        png_path = PNG_DIR / f"synthetic-{campaign_index:04d}.png"
        png_from_tensor(tensor, png_path)
        expected = np.array(image, dtype=np.dtype("<f4"), order="C", copy=True).reshape(1, 128, 128).tobytes(order="C")
        layout_verified += int(
            tensor.shape == (1, 128, 128)
            and tensor.dtype == np.dtype("<f4")
            and tensor.flags.c_contiguous
            and tensor_path.stat().st_size == 65536
        )
        byte_equivalent += int(payload == expected and tensor_path.read_bytes() == expected)
        truth_rows.append({
            "object_id": f"synthetic-{campaign_index:04d}",
            "generator_index": source_index,
            "truth_sign": int(truth),
            "tensor_path": str(tensor_path),
            "png_path": str(png_path),
            "tensor_sha256": hashlib.sha256(payload).hexdigest(),
            "ic_receipt": ic_receipt,
        })
        paths.append(tensor_path)
    write_jsonl(TRUTH_PATH, truth_rows)
    generation_seconds = time.perf_counter() - generation_start
    if layout_verified != N or byte_equivalent != N:
        raise RuntimeError("writer/layout equivalence failed")

    inference = load_module("gpt1_rehearsal_inference", INFERENCE_PATH)
    inference_start = time.perf_counter()
    inference_result = inference.run_paths(paths, INFERENCE_OUT, synthetic=True)
    inference_seconds = time.perf_counter() - inference_start
    inference_rows = [json.loads(line) for line in (INFERENCE_OUT / "results.jsonl").read_text().splitlines()]
    if len(inference_rows) != N:
        raise RuntimeError("inference row count mismatch")
    by_stem = {row["object_id"].split("-")[0] + "-" + row["object_id"].split("-")[1]: row for row in inference_rows}
    # Object IDs are synthetic-0000-<hash>; strip the final hash robustly.
    by_stem = {row["object_id"].rsplit("-", 1)[0]: row for row in inference_rows}

    committee_start = time.perf_counter()
    member_b = committee.SmallPlainCNN().to(device="cpu", dtype=torch.float32)
    state = torch.load(COMMITTEE_WEIGHTS, map_location="cpu", weights_only=True)
    member_b.load_state_dict(state, strict=True)
    member_b.eval()
    committee_rows: list[dict] = []
    committee_crosscheck = 0
    for truth_row in truth_rows:
        image = np.fromfile(truth_row["tensor_path"], dtype=np.dtype("<f4")).reshape(128, 128)
        score_a = committee.geometric_chi(image)
        sign_a = committee.accepted_sign(score_a, committee.GEOMETRIC_THRESHOLD)
        score_b = committee.cnn_chi(member_b, image)
        sign_b = committee.accepted_sign(score_b, committee.CNN_THRESHOLD)
        state_name = committee.committee_state(sign_a, sign_b)
        inference_row = by_stem[truth_row["object_id"]]
        committee_crosscheck += int(state_name == inference_row["committee_state"])
        committee_rows.append({
            "object_id": truth_row["object_id"],
            "member_a_score": score_a,
            "member_a_sign": sign_a,
            "member_b_score": score_b,
            "member_b_sign": sign_b,
            "committee_state": state_name,
        })
    write_jsonl(COMMITTEE_OUT, committee_rows)
    committee_seconds = time.perf_counter() - committee_start
    if committee_crosscheck != N:
        raise RuntimeError("separate committee pass differs from inference metadata")

    strata_start = time.perf_counter()
    state_map = {
        "AGREE_CONFIDENT": "agree-confident",
        "DISAGREE": "disagree",
        "LOW_CONFIDENCE": "low-confidence",
    }
    analysis_rows = []
    for truth_row, committee_row in zip(truth_rows, committee_rows):
        inference_row = by_stem[truth_row["object_id"]]
        chi = float(inference_row["chi_value"])
        analysis_rows.append({
            "object_id": truth_row["object_id"],
            "truth_sign": truth_row["truth_sign"],
            "chi": chi,
            "chi_sign": sign(chi),
            "abs_chi": abs(chi),
            "committee_state": state_map[committee_row["committee_state"]],
            "png_path": truth_row["png_path"],
        })
    tertiles = rank_tertiles(analysis_rows)
    strata_rows: dict[str, list[dict]] = defaultdict(list)
    for row in analysis_rows:
        row["tertile"] = tertiles[row["object_id"]]
        strata_rows[f"{row['committee_state']}|{row['tertile']}"] .append(row)
    expected_strata = [f"{state}|{tertile}" for state in ("agree-confident", "disagree", "low-confidence") for tertile in range(3)]
    populations = {key: len(strata_rows[key]) for key in expected_strata}
    if any(value < 30 for value in populations.values()):
        raise RuntimeError(f"one or more nine-stratum populations cannot satisfy floor 30: {populations}")
    priors = {}
    for key in expected_strata:
        rows = strata_rows[key]
        correct = sum(row["chi_sign"] == row["truth_sign"] for row in rows)
        priors[key] = (Decimal(correct) + Decimal("0.5")) / (Decimal(len(rows)) + Decimal(1))
    handcheck = load_module("gpt1_rehearsal_handcheck", HANDCHECK_PATH)
    allocation = handcheck.allocate_neyman(populations, priors, total=500, floor=30)
    NEYMAN_PRIORS.write_text(json.dumps({key: str(priors[key]) for key in expected_strata}, sort_keys=True, indent=2) + "\n")
    real_rows = [{
        "data_class": "synthetic",
        "object_id": row["object_id"],
        "image_path": row["png_path"],
        "instrument_sign": row["chi_sign"],
        "abs_chi": row["abs_chi"],
        "committee_state": row["committee_state"],
    } for row in analysis_rows]
    if any(row["instrument_sign"] == 0 for row in real_rows):
        raise RuntimeError("HC-1H input contract rejects zero instrument signs")
    injection_rows = [{
        "data_class": "synthetic",
        "synthetic_id": "injection-" + row["object_id"],
        "image_path": row["png_path"],
        "truth_sign": row["truth_sign"],
        "abs_chi": row["abs_chi"],
        "committee_state": row["committee_state"],
    } for row in analysis_rows]
    write_jsonl(REAL_POPULATION, real_rows)
    write_jsonl(SYNTHETIC_POOL, injection_rows)
    strata_seconds = time.perf_counter() - strata_start

    harness_start = time.perf_counter()
    PASSPHRASE_PATH.write_bytes(secrets.token_bytes(32))
    os.chmod(PASSPHRASE_PATH, 0o600)
    command = [
        sys.executable, str(HANDCHECK_PATH), "prepare",
        "--mode", "full",
        "--real-population", str(REAL_POPULATION),
        "--synthetic-pool", str(SYNTHETIC_POOL),
        "--neyman-priors", str(NEYMAN_PRIORS),
        "--private-root", str(PRIVATE_ROOT),
        "--checking-root", str(CHECKING_ROOT),
        "--passphrase-file", str(PASSPHRASE_PATH),
        "--checker-id", "GPT1-REHEARSAL-NO-HUMAN-LABELS",
        "--pilot-policy", "no-pilot-run",
        "--replacement-reserve-per-group", "1",
    ]
    prepared = subprocess.run(command, text=True, capture_output=True, check=False)
    (ROOT / "hc1h_prepare.stdout.log").write_text(prepared.stdout)
    (ROOT / "hc1h_prepare.stderr.log").write_text(prepared.stderr)
    (ROOT / "hc1h_prepare.command.json").write_text(json.dumps(command, indent=2) + "\n")
    if prepared.returncode != 0:
        raise RuntimeError(f"HC-1H prepare failed: {prepared.stderr.strip()}")
    prepare_receipt = json.loads(prepared.stdout)
    application = handcheck.CheckerApplication(
        CHECKING_ROOT / "checker_H",
        control_path=PRIVATE_ROOT / "checker_H_control.json",
        debounce_seconds=0.0,
    )
    public_state = application.public_state()
    package = handcheck.load_checker_package(CHECKING_ROOT / "checker_H")
    if application.completed != 0:
        raise RuntimeError("HC-1H rehearsal unexpectedly contains labels")
    harness_seconds = time.perf_counter() - harness_start

    direct_correct = sum(row["chi_sign"] == row["truth_sign"] for row in analysis_rows)
    inverted_correct = sum(row["chi_sign"] == -row["truth_sign"] for row in analysis_rows)
    zero_count = sum(row["chi_sign"] == 0 for row in analysis_rows)
    if direct_correct >= inverted_correct:
        convention = "chi > 0 corresponds to BS-3 truth_sign +1 (direct convention)"
    else:
        convention = "chi > 0 corresponds to BS-3 truth_sign -1 (inverted convention)"
    committee_distribution = Counter(row["committee_state"] for row in committee_rows)
    total_seconds = time.perf_counter() - started
    sealed_path = PRIVATE_ROOT / "sealed_key.nmhc"
    commitment_path = CHECKING_ROOT / "precheck_commitment.json"
    if not commitment_path.exists():
        candidates = sorted(CHECKING_ROOT.glob("*commitment*.json"))
        if not candidates:
            candidates = sorted(PRIVATE_ROOT.glob("*commitment*.json"))
        if not candidates:
            raise RuntimeError("HC-1H public commitment artifact not found")
        commitment_path = candidates[0]

    summary = {
        "status": "PASS_COMPLETE_CHAIN_SYNTHETIC_ONLY",
        "objects": N,
        "hashes": hashes,
        "generator": {"domain": DOMAIN, "candidate_draws": CANDIDATE_DRAWS},
        "writer": {"layout_verified": layout_verified, "byte_equivalent": byte_equivalent},
        "inference": inference_result,
        "chi": {
            "direct_correct": direct_correct,
            "inverted_correct": inverted_correct,
            "direct_accuracy": direct_correct / N,
            "inverted_accuracy": inverted_correct / N,
            "positive_count": sum(row["chi_sign"] > 0 for row in analysis_rows),
            "negative_count": sum(row["chi_sign"] < 0 for row in analysis_rows),
            "zero_count": zero_count,
            "observed_sign_convention": convention,
        },
        "committee_distribution": {key: committee_distribution.get(key, 0) for key in ("AGREE_CONFIDENT", "DISAGREE", "LOW_CONFIDENCE")},
        "committee_crosscheck": committee_crosscheck,
        "strata": [{
            "state": key.rsplit("|", 1)[0],
            "tertile": int(key.rsplit("|", 1)[1]),
            "population": populations[key],
            "prior": float(priors[key]),
            "allocation": allocation[key],
            "population_below_30": populations[key] < 30,
            "allocation_below_30": allocation[key] < 30,
        } for key in expected_strata],
        "strata_population_below_30": sum(value < 30 for value in populations.values()),
        "strata_allocation_below_30": sum(value < 30 for value in allocation.values()),
        "allocation_total": sum(allocation.values()),
        "hc1h": {
            "prepare_exit_code": prepared.returncode,
            "status": prepare_receipt.get("status", "PREPARED"),
            "items": len(package["items"]),
            "session_status": public_state["status"],
            "session_completed": application.completed,
            "durable_session_ledger_present": (CHECKING_ROOT / "checker_H" / "answers.jsonl").exists(),
            "sealed_key_present": sealed_path.is_file(),
            "sealed_key_sha256": sha256_file(sealed_path),
            "commitment_sha256": sha256_file(commitment_path),
        },
        "timing_seconds": {
            "candidate_screening": candidate_seconds,
            "generation_writer_png": generation_seconds,
            "inference": inference_seconds,
            "committee": committee_seconds,
            "strata_inputs": strata_seconds,
            "hc1h_prepare_session": harness_seconds,
            "total": total_seconds,
            "total_per_1000": total_seconds / 2,
        },
        "interface_mismatches": [
            {
                "interface": "HC-1H session persistence before first label",
                "mismatch": "Constructing CheckerApplication returns an ACTIVE blinded state but does not persist answers.jsonl/SESSION_STARTED until the first checker event.",
                "workaround": "Verified the ACTIVE zero-completed state, package, control binding, commitment, and sealed envelope without manufacturing a C/W answer; reported the absence of a durable session ledger explicitly.",
                "real_run_implication": "If pre-label durable session creation is required for operational custody, add a dedicated start-session event/entry point before the real run.",
            },
            {
                "interface": "Natural BS-3 population versus HC-1H floor",
                "mismatch": "The first unselected N=2,000 draw produced populations 28, 8, and 11 in three cells, so the frozen floor of 30 made full preparation impossible.",
                "workaround": "Preserved that failed attempt, screened 12,000 deterministic BS-3 candidates synthetically, and selected an exactly 2,000-object campaign with 667/667/666 objects across global |chi| thirds and at least 35 of every committee state per third (floor 30 plus HC-7 reserve headroom); then reran the selected campaign through inference and committee.",
                "real_run_implication": "The real accepted population cannot be engineered this way; if any real cell has N_s<30, HC-1H is infeasible and must hold or receive a preregistered sparse-cell rule before any labels.",
            },
            {
                "interface": "Python environment split",
                "mismatch": "The frozen torch venv lacked Pillow, cryptography, and astropy, while the system Python had those packages but lacked torch.",
                "workaround": "Ran the torch venv interpreter with the existing user-site package directory on PYTHONPATH; no install and no network.",
                "real_run_implication": "The production command needs one hash-locked environment containing every gated program's dependencies.",
            },
            {
                "interface": "Inference CLI input transport",
                "mismatch": "The runner accepts every tensor as a separate --inputs argument and has no manifest/stdin mode; 2,000 absolute paths risk the macOS argument-length ceiling and the real campaign would certainly exceed it.",
                "workaround": "Called the unmodified gated run_paths API with the complete ordered Path list.",
                "real_run_implication": "Add a hash-bound manifest input mode before the real campaign without changing inference semantics.",
            },
            {
                "interface": "Committee program entry point",
                "mismatch": "committee.py has no campaign CLI and does not itself load its frozen member-B weights.",
                "workaround": "Loaded its hash-pinned SmallPlainCNN weights and called its unmodified scoring/state functions in a separate post-inference pass, then cross-checked every state against inference metadata.",
                "real_run_implication": "Provide a gated batch entry point or formally designate inference receipts as the committee campaign product.",
            },
            {
                "interface": "HC-1H image versus tensor contract",
                "mismatch": "Inference consumes raw 65,536-byte float32 tensors, but HC-1H requires Pillow-readable image_path assets and cannot ingest those tensors.",
                "workaround": "Created deterministic 128x128 grayscale PNG sidecars from each exact tensor using fixed percentile display scaling; tensor inference bytes remained untouched.",
                "real_run_implication": "Freeze the real tensor-to-checker rendering map and bind each PNG to its source tensor hash before the real hand-check.",
            },
            {
                "interface": "Neyman priors at perfect/near-perfect synthetic recovery",
                "mismatch": "The HC-1H allocator refuses when every empirical prior is exactly 0 or 1 because all information weights become zero; finite synthetic strata can hit that boundary.",
                "workaround": "Used an explicit Jeffreys-smoothed synthetic estimate (correct+0.5)/(N_s+1), then passed it to the unmodified constrained allocator.",
                "real_run_implication": "Freeze the prior estimator/smoothing rule before production rather than selecting it after seeing synthetic outcomes.",
            },
            {
                "interface": "Committee state vocabulary",
                "mismatch": "The committee emits uppercase underscore states, while HC-1H accepts lowercase hyphenated states only.",
                "workaround": "Applied the explicit bijection AGREE_CONFIDENT→agree-confident, DISAGREE→disagree, LOW_CONFIDENCE→low-confidence.",
                "real_run_implication": "Freeze one canonical vocabulary or a hash-pinned adapter.",
            },
            {
                "interface": "HC-1H campaign role naming",
                "mismatch": "The harness calls its 500-row input real_population even when data_class is synthetic, and separately requires another synthetic_pool for injections.",
                "workaround": "Used the 2,000-object synthetic campaign as a synthetic-class accepted population and a separately identified view of the same generated assets as an injection pool; no claim of independent science samples is made.",
                "real_run_implication": "Production must supply genuinely separate accepted real population and blind-injection pool, with identity-disjointness policy made explicit.",
            },
        ],
        "artifacts": {
            "summary": str(SUMMARY_PATH),
            "truth_manifest": str(TRUTH_PATH),
            "inference_ledger": str(INFERENCE_OUT / "results.jsonl"),
            "committee_ledger": str(COMMITTEE_OUT),
            "real_population_input": str(REAL_POPULATION),
            "synthetic_pool_input": str(SYNTHETIC_POOL),
            "neyman_priors": str(NEYMAN_PRIORS),
            "hc1h_prepare_stdout": str(ROOT / "hc1h_prepare.stdout.log"),
            "hc1h_checker_package": str(CHECKING_ROOT / "checker_H" / "package.json"),
            "hc1h_sealed_key": str(sealed_path),
            "report": str(REPORT_PATH),
        },
    }
    SUMMARY_PATH.write_text(json.dumps(summary, sort_keys=True, indent=2) + "\n")
    REPORT_PATH.write_text(render_report(summary))
    headline = (
        f"GPT1_REHEARSAL_COMPLETE N={N} chi_accuracy={summary['chi']['direct_accuracy']:.6%} "
        f"committee={dict(summary['committee_distribution'])} allocation_floor_min={min(allocation.values())} "
        f"hc1h_items={len(package['items'])} labels_submitted=0 total_s={total_seconds:.3f}\n"
    )
    DONE_PATH.write_text(headline + f"Report: {REPORT_PATH}\n")
    print(json.dumps({"status": summary["status"], "report": str(REPORT_PATH), "done": str(DONE_PATH), "headline": headline.strip()}, sort_keys=True))
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except Exception as exc:
        ROOT.mkdir(parents=True, exist_ok=True)
        hold = f"GPT1_REHEARSAL_HOLD: {type(exc).__name__}: {exc}\n"
        (ROOT / "REHEARSAL_HOLD_20260820.txt").write_text(hold)
        DONE_PATH.write_text(hold)
        raise
