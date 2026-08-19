#!/usr/bin/env python3
"""Train/freeze member B and validate both HC-1H members on synthetics only."""
from __future__ import annotations

import hashlib
import json
import os
import platform
import sys
import time
from collections import Counter
from pathlib import Path

import numpy as np
import sympy
import torch
import torch.nn.functional as F

from committee import (
    CNN_THRESHOLD,
    GENERATOR_PATH,
    GENERATOR_SHA256,
    GEOMETRIC_THRESHOLD,
    TRAIN_DOMAIN,
    TRAIN_SEED,
    VALIDATION_DOMAIN,
    SmallPlainCNN,
    accepted_sign,
    canonical_parameter_hash,
    cnn_chi_batch,
    committee_state,
    geometric_chi,
    mirror,
    sha256_file,
    synth_sample,
)

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent
RECEIPTS = HERE / "receipts"
WEIGHTS = HERE / "member_b_weights_frozen.pt"
TRAIN_JSON = RECEIPTS / "MEMBER_B_TRAINING_RECEIPT_20260820.json"
TRAIN_MD = HERE / "MEMBER_B_TRAINING_RECEIPT_20260820.md"
VALIDATION_JSON = RECEIPTS / "COMMITTEE_VALIDATION_10000_20260820.json"
VALIDATION_MD = HERE / "COMMITTEE_VALIDATION_20260820.md"
STATE_JSON = HERE / "COMMITTEE_STATE_DEFINITION_20260820.json"
SYMPY_JSON = RECEIPTS / "SYMPY_ANTISYMMETRY_RECEIPT_20260820.json"
TRAIN_COUNT = 20_000
VALIDATION_COUNT = 10_000
BATCH_SIZE = 100
EPOCHS = 4

EXPECTED_INPUTS = {
    ROOT / "PREREG_LONGO_AMPLITUDE_TEST_FROZEN_20260815_V3.md": (
        "b06901c8a0f3a0570af41262453670589d8dc0b20c79c7d4162853c7dfec42d7",
        0o444,
    ),
    ROOT / "LANA_ONE_HUMAN_ATTENUATION_20260814.md": (
        "b2590e4213e225f9869fe782cfe0f55d8d8979dcb470752836a5cd31a58453fd",
        None,
    ),
    GENERATOR_PATH: (GENERATOR_SHA256, None),
}


def atomic_json(path: Path, payload: dict) -> None:
    temporary = path.with_suffix(path.suffix + ".tmp")
    temporary.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    os.replace(temporary, path)


def verify_inputs() -> dict:
    result = {}
    for path, (expected_hash, expected_mode) in EXPECTED_INPUTS.items():
        actual_hash = sha256_file(path)
        actual_mode = path.stat().st_mode & 0o777
        if actual_hash != expected_hash:
            raise SystemExit(f"INPUT HASH MISMATCH: {path}")
        if expected_mode is not None and actual_mode != expected_mode:
            raise SystemExit(f"INPUT MODE MISMATCH: {path} {oct(actual_mode)}")
        result[str(path.relative_to(ROOT.parent))] = {
            "sha256": actual_hash,
            "mode": oct(actual_mode),
        }
    return result


def materialize_batch(domain: str, indices: np.ndarray) -> tuple[torch.Tensor, torch.Tensor, list[str]]:
    images = []
    labels = []
    hashes = []
    for raw_index in indices:
        image, parity = synth_sample(domain, int(raw_index))
        images.append(image)
        labels.append(parity)
        hashes.append(hashlib.sha256(image.tobytes()).hexdigest())
    array = np.stack(images)[:, None]
    return torch.from_numpy(array), torch.tensor(labels, dtype=torch.float32), hashes


def train_and_freeze(inputs: dict) -> tuple[SmallPlainCNN, dict]:
    if WEIGHTS.exists():
        raise SystemExit(f"refusing to overwrite frozen weights: {WEIGHTS}")
    torch.manual_seed(TRAIN_SEED)
    torch.set_num_threads(1)
    try:
        torch.set_num_interop_threads(1)
    except RuntimeError:
        pass
    torch.use_deterministic_algorithms(True)
    model = SmallPlainCNN().cpu()
    optimizer = torch.optim.Adam(model.parameters(), lr=0.001)
    manifest = hashlib.sha256()
    epoch_receipts = []
    started = time.time()
    for epoch in range(EPOCHS):
        permutation = np.random.default_rng(TRAIN_SEED + epoch).permutation(TRAIN_COUNT)
        loss_sum = 0.0
        correct = 0
        seen = 0
        for start in range(0, TRAIN_COUNT, BATCH_SIZE):
            indices = permutation[start : start + BATCH_SIZE]
            images, labels, hashes = materialize_batch(TRAIN_DOMAIN, indices)
            if epoch == 0:
                ordered = sorted(zip(indices.tolist(), hashes))
                for _, image_hash in ordered:
                    manifest.update(bytes.fromhex(image_hash))
            chi = cnn_chi_batch(model, images)
            loss = F.softplus(-labels * chi).mean()
            optimizer.zero_grad()
            loss.backward()
            optimizer.step()
            loss_sum += float(loss.item()) * len(indices)
            correct += int(((chi.detach() > 0).to(labels.dtype) * 2 - 1 == labels).sum().item())
            seen += len(indices)
        epoch_receipts.append(
            {
                "epoch": epoch + 1,
                "mean_loss": loss_sum / seen,
                "training_sign_accuracy": correct / seen,
                "permutation_seed": TRAIN_SEED + epoch,
            }
        )
    model.eval()
    canonical_hash = canonical_parameter_hash(model)
    torch.save(model.state_dict(), WEIGHTS)
    weights_hash = sha256_file(WEIGHTS)
    os.chmod(WEIGHTS, 0o444)
    receipt = {
        "boundary": "synthetic-only; no real data; no human chirality labels; no network",
        "architecture_family": "plain sequential LeNet-style small CNN; no residual blocks",
        "training_domain": TRAIN_DOMAIN,
        "training_count": TRAIN_COUNT,
        "balanced_parity": True,
        "fresh_seed": TRAIN_SEED,
        "epochs": EPOCHS,
        "batch_size": BATCH_SIZE,
        "optimizer": {"name": "Adam", "learning_rate": 0.001},
        "loss": "softplus(-parity * chi_B), chi_B=(g(x)-g(mirror(x)))/2",
        "epoch_receipts": epoch_receipts,
        "training_manifest_sha256": manifest.hexdigest(),
        "weights_path": str(WEIGHTS.relative_to(ROOT)),
        "weights_file_sha256": weights_hash,
        "weights_canonical_float32_sha256": canonical_hash,
        "weights_mode_after_freeze": oct(WEIGHTS.stat().st_mode & 0o777),
        "freeze_policy": (
            "Serialized once and chmod 0444. Never retrain, recalibrate, fine-tune, prune, "
            "re-export, replace, or overwrite; any change requires a new candidate and freeze."
        ),
        "threshold": CNN_THRESHOLD,
        "input_bindings": inputs,
        "runtime": {
            "python": sys.version,
            "torch": torch.__version__,
            "numpy": np.__version__,
            "platform": platform.platform(),
            "device": "cpu",
            "threads": torch.get_num_threads(),
            "deterministic_algorithms": torch.are_deterministic_algorithms_enabled(),
            "elapsed_seconds": time.time() - started,
        },
    }
    atomic_json(TRAIN_JSON, receipt)
    TRAIN_MD.write_text(
        "# Member B training and weights-freeze receipt — 2026-08-20\n\n"
        "Synthetic-only training completed on the frozen BS-3 generator. No real image, real "
        "statistic, human chirality label, primary weight, or network source entered training.\n\n"
        f"- Fresh seed: `{TRAIN_SEED}`\n"
        f"- Training images: `{TRAIN_COUNT}` (exactly balanced parity)\n"
        f"- Epochs: `{EPOCHS}`; final training sign accuracy: "
        f"`{epoch_receipts[-1]['training_sign_accuracy']:.6f}`\n"
        f"- Weight file SHA-256: `{weights_hash}`\n"
        f"- Canonical parameter SHA-256: `{canonical_hash}`\n"
        f"- Frozen mode: `{oct(WEIGHTS.stat().st_mode & 0o777)}`\n"
        f"- Machine receipt: `{TRAIN_JSON.relative_to(HERE)}`\n\n"
        "Freeze policy: the serialized file is read-only and must never be retrained, "
        "recalibrated, fine-tuned, pruned, re-exported, replaced, or overwritten. Any change "
        "requires a new candidate and a new recorded freeze.\n",
        encoding="utf-8",
    )
    return model, receipt


def summarize_member(accepted: int, correct: int, antisymmetry: int, mirror_decision: int) -> dict:
    return {
        "accepted": accepted,
        "abstained": VALIDATION_COUNT - accepted,
        "coverage": accepted / VALIDATION_COUNT,
        "correct_accepted": correct,
        "accepted_sign_accuracy": correct / accepted if accepted else None,
        "overall_correct_fraction_abstention_not_correct": correct / VALIDATION_COUNT,
        "antisymmetry_value_pass": antisymmetry,
        "antisymmetry_value_fail": VALIDATION_COUNT - antisymmetry,
        "mirror_decision_pass": mirror_decision,
        "mirror_decision_fail": VALIDATION_COUNT - mirror_decision,
        "qualification": (
            "QUALIFIED"
            if antisymmetry == VALIDATION_COUNT and mirror_decision == VALIDATION_COUNT
            else "DISQUALIFIED"
        ),
    }


def validate(model: SmallPlainCNN, inputs: dict, training_receipt: dict) -> dict:
    state_counts = Counter()
    a_accepted = a_correct = a_anti = a_decision = 0
    b_accepted = b_correct = b_anti = b_decision = 0
    manifest = hashlib.sha256()
    started = time.time()
    for start in range(0, VALIDATION_COUNT, BATCH_SIZE):
        indices = np.arange(start, min(start + BATCH_SIZE, VALIDATION_COUNT))
        images, labels, hashes = materialize_batch(VALIDATION_DOMAIN, indices)
        for image_hash in hashes:
            manifest.update(bytes.fromhex(image_hash))
        with torch.no_grad():
            b_scores = cnn_chi_batch(model, images).cpu().numpy()
            mirrored_images = torch.flip(images, dims=[3]).contiguous()
            b_mirror_scores = cnn_chi_batch(model, mirrored_images).cpu().numpy()
        for offset, index in enumerate(indices):
            image = images[offset, 0].numpy()
            truth = int(labels[offset].item())
            a_score = geometric_chi(image)
            a_mirror_score = geometric_chi(mirror(image))
            b_score = float(b_scores[offset])
            b_mirror_score = float(b_mirror_scores[offset])
            a_sign = accepted_sign(a_score, GEOMETRIC_THRESHOLD)
            a_mirror_sign = accepted_sign(a_mirror_score, GEOMETRIC_THRESHOLD)
            b_sign = accepted_sign(b_score, CNN_THRESHOLD)
            b_mirror_sign = accepted_sign(b_mirror_score, CNN_THRESHOLD)
            a_accepted += int(a_sign != 0)
            a_correct += int(a_sign != 0 and a_sign == truth)
            b_accepted += int(b_sign != 0)
            b_correct += int(b_sign != 0 and b_sign == truth)
            a_anti += int(a_mirror_score == -a_score)
            b_anti += int(b_mirror_score == -b_score)
            a_decision += int(
                (a_sign == 0 and a_mirror_sign == 0)
                or (a_sign != 0 and a_mirror_sign == -a_sign)
            )
            b_decision += int(
                (b_sign == 0 and b_mirror_sign == 0)
                or (b_sign != 0 and b_mirror_sign == -b_sign)
            )
            state_counts[committee_state(a_sign, b_sign)] += 1
    member_a = summarize_member(a_accepted, a_correct, a_anti, a_decision)
    member_b = summarize_member(b_accepted, b_correct, b_anti, b_decision)
    result = {
        "boundary": "10,000 fresh frozen-generator synthetics only; no real data; no network",
        "validation_domain": VALIDATION_DOMAIN,
        "validation_count": VALIDATION_COUNT,
        "exactly_balanced_parity": True,
        "validation_manifest_sha256": manifest.hexdigest(),
        "fresh_from_training": VALIDATION_DOMAIN != TRAIN_DOMAIN,
        "member_a": {
            "architecture": "deterministic training-free symmetrized annular winding tracer",
            "threshold": GEOMETRIC_THRESHOLD,
            **member_a,
        },
        "member_b": {
            "architecture": "independently trained plain sequential small CNN",
            "threshold": CNN_THRESHOLD,
            "weights_file_sha256": training_receipt["weights_file_sha256"],
            "weights_canonical_float32_sha256": training_receipt[
                "weights_canonical_float32_sha256"
            ],
            **member_b,
        },
        "committee_state_mapping": {
            "AGREE_CONFIDENT": "both nonzero and same sign",
            "DISAGREE": "both nonzero and opposite signs",
            "LOW_CONFIDENCE": "at least one member abstains",
        },
        "committee_state_counts": dict(sorted(state_counts.items())),
        "committee_state_fractions": {
            key: state_counts[key] / VALIDATION_COUNT
            for key in ("AGREE_CONFIDENT", "DISAGREE", "LOW_CONFIDENCE")
        },
        "committee_complete": (
            member_a["qualification"] == "QUALIFIED"
            and member_b["qualification"] == "QUALIFIED"
        ),
        "input_bindings": inputs,
        "elapsed_seconds": time.time() - started,
    }
    atomic_json(VALIDATION_JSON, result)
    fractions = result["committee_state_fractions"]
    VALIDATION_MD.write_text(
        "# HC-1H committee synthetic validation — 2026-08-20\n\n"
        "Validation used 10,000 fresh, exactly parity-balanced frozen BS-3 synthetics and no "
        "real data. Accuracy is reported among accepted signs; coverage and the overall correct "
        "fraction (abstentions not correct) are also explicit.\n\n"
        f"- Member A: accuracy `{member_a['accepted_sign_accuracy']:.6f}`, coverage "
        f"`{member_a['coverage']:.6f}`, antisymmetry `{a_anti}/10000`, "
        f"status `{member_a['qualification']}`.\n"
        f"- Member B: accuracy `{member_b['accepted_sign_accuracy']:.6f}`, coverage "
        f"`{member_b['coverage']:.6f}`, antisymmetry `{b_anti}/10000`, "
        f"status `{member_b['qualification']}`.\n"
        f"- States: AGREE_CONFIDENT `{state_counts['AGREE_CONFIDENT']}` "
        f"(`{fractions['AGREE_CONFIDENT']:.6f}`), DISAGREE `{state_counts['DISAGREE']}` "
        f"(`{fractions['DISAGREE']:.6f}`), LOW_CONFIDENCE `{state_counts['LOW_CONFIDENCE']}` "
        f"(`{fractions['LOW_CONFIDENCE']:.6f}`).\n"
        f"- Machine receipt: `{VALIDATION_JSON.relative_to(HERE)}`\n",
        encoding="utf-8",
    )
    return result


def write_state_and_sympy_receipts() -> None:
    atomic_json(
        STATE_JSON,
        {
            "states": {
                "AGREE_CONFIDENT": "A and B are both nonzero and A == B",
                "DISAGREE": "A and B are both nonzero and A == -B",
                "LOW_CONFIDENCE": "A == 0 or B == 0",
            },
            "member_values": [-1, 0, 1],
            "exhaustive": True,
            "mutually_exclusive": True,
            "prohibited_use": "stratifier/allocator/diagnostic only; never inside a",
        },
    )
    q_x, q_mx = sympy.symbols("q_x q_mx")
    chi_x = (q_x - q_mx) / 2
    chi_mx = chi_x.xreplace({q_x: q_mx, q_mx: q_x})
    residual = sympy.simplify(chi_mx + chi_x)
    atomic_json(
        SYMPY_JSON,
        {
            "sympy_version": sympy.__version__,
            "chi_x": str(chi_x),
            "chi_mirror_x": str(chi_mx),
            "simplify_chi_mirror_plus_chi": str(residual),
            "pass": residual == 0,
            "assumption": "mirror is an involution, so mirroring swaps q(x) and q(mirror(x))",
        },
    )


def main() -> None:
    RECEIPTS.mkdir(parents=True, exist_ok=True)
    inputs = verify_inputs()
    write_state_and_sympy_receipts()
    model, training_receipt = train_and_freeze(inputs)
    result = validate(model, inputs, training_receipt)
    print(json.dumps(result, indent=2, sort_keys=True))
    if not result["committee_complete"]:
        raise SystemExit(2)


if __name__ == "__main__":
    main()
