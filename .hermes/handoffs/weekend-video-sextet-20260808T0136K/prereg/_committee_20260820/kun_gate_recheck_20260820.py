#!/usr/bin/env python3
"""Kun one-shot gate: HC-1H committee build re-verification, fresh seeds, findings only."""
from __future__ import annotations

import hashlib
import json
import sys
from collections import Counter
from pathlib import Path

import numpy as np
import torch

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))

from committee import (
    CNN_THRESHOLD,
    GENERATOR_PATH,
    GENERATOR_SHA256,
    GEOMETRIC_THRESHOLD,
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

WEIGHTS = HERE / "member_b_weights_frozen.pt"
TRAIN_RECEIPT = json.loads((HERE / "receipts" / "MEMBER_B_TRAINING_RECEIPT_20260820.json").read_text())

GATE_ANTISYM_DOMAIN = "KUN-GATE-ANTISYM-20260820-FRESH"
GATE_VALIDATE_DOMAIN = "KUN-GATE-VALIDATE-20260820-FRESH"
ANTISYM_N = 300
GATE_N = 2000

out = {}

# --- check 4: weights serialized + hashed ---------------------------------
file_hash = sha256_file(WEIGHTS)
mode = oct(WEIGHTS.stat().st_mode & 0o777)
model = SmallPlainCNN()
state = torch.load(WEIGHTS, map_location="cpu", weights_only=True)
model.load_state_dict(state)
model.eval()
torch.set_num_threads(1)
canon = canonical_parameter_hash(model)
out["weights"] = {
    "file_sha256": file_hash,
    "file_sha256_matches_receipt": file_hash == TRAIN_RECEIPT["weights_file_sha256"],
    "file_sha256_matches_claimed": file_hash == "6e4a6efaf9e9db55e8ca23f1ffa7e61ef437c62bc959c9630b90db0d18aeff0a",
    "canonical_sha256": canon,
    "canonical_matches_receipt": canon == TRAIN_RECEIPT["weights_canonical_float32_sha256"],
    "mode": mode,
    "mode_is_0444": mode == "0o444",
    "freeze_policy_in_receipt": "freeze_policy" in TRAIN_RECEIPT,
    "fresh_seed_recorded": TRAIN_RECEIPT.get("fresh_seed"),
    "training_domain": TRAIN_RECEIPT.get("training_domain"),
    "no_human_labels_boundary": TRAIN_RECEIPT.get("boundary"),
}

# --- generator pin vs BS-3 --------------------------------------------------
out["generator"] = {
    "path": str(GENERATOR_PATH),
    "current_sha256": sha256_file(GENERATOR_PATH),
    "matches_pinned_bs3_hash": bool(sha256_file(GENERATOR_PATH) == GENERATOR_SHA256
    == "89da33ec6260e75e06eadb0f171da4c52f1478b59ff5e543d363dbf56fefcd75"),
}

# --- check 2: antisymmetry on fresh seeded sample ---------------------------
a_exact = b_exact = a_decision = b_decision = 0
for index in range(ANTISYM_N):
    image, _ = synth_sample(GATE_ANTISYM_DOMAIN, index)
    a_chi = geometric_chi(image)
    a_chi_m = geometric_chi(mirror(image))
    a_exact += int(a_chi_m == -a_chi)
    s_a = accepted_sign(a_chi, GEOMETRIC_THRESHOLD)
    s_am = accepted_sign(a_chi_m, GEOMETRIC_THRESHOLD)
    a_decision += int((s_a == 0 and s_am == 0) or (s_am == -s_a))
    t = torch.from_numpy(image)[None, None]
    with torch.no_grad():
        b_chi = float(cnn_chi_batch(model, t).item())
        b_chi_m = float(cnn_chi_batch(model, torch.flip(t, dims=[3]).contiguous()).item())
    b_exact += int(b_chi_m == -b_chi)
    s_b = accepted_sign(b_chi, CNN_THRESHOLD)
    s_bm = accepted_sign(b_chi_m, CNN_THRESHOLD)
    b_decision += int((s_b == 0 and s_bm == 0) or (s_bm == -s_b))
out["antisymmetry_fresh"] = {
    "domain": GATE_ANTISYM_DOMAIN,
    "n": ANTISYM_N,
    "member_a_exact_sign_flip": f"{a_exact}/{ANTISYM_N}",
    "member_a_decision_flip": f"{a_decision}/{ANTISYM_N}",
    "member_b_exact_sign_flip": f"{b_exact}/{ANTISYM_N}",
    "member_b_decision_flip": f"{b_decision}/{ANTISYM_N}",
}

# --- check 3: fresh seeded 2,000-sample validation ---------------------------
state_counts = Counter()
a_acc = a_cor = b_acc = b_cor = 0
batch = 100
for start in range(0, GATE_N, batch):
    indices = np.arange(start, min(start + batch, GATE_N))
    images, labels = [], []
    for raw in indices:
        image, parity = synth_sample(GATE_VALIDATE_DOMAIN, int(raw))
        images.append(image)
        labels.append(parity)
    array = torch.from_numpy(np.stack(images)[:, None])
    labels_t = torch.tensor(labels, dtype=torch.float32)
    with torch.no_grad():
        b_scores = cnn_chi_batch(model, array).cpu().numpy()
    for offset in range(len(indices)):
        image = images[offset]
        truth = int(labels[offset])
        a_score = geometric_chi(image)
        b_score = float(b_scores[offset])
        s_a = accepted_sign(a_score, GEOMETRIC_THRESHOLD)
        s_b = accepted_sign(b_score, CNN_THRESHOLD)
        a_acc += int(s_a != 0)
        a_cor += int(s_a != 0 and s_a == truth)
        b_acc += int(s_b != 0)
        b_cor += int(s_b != 0 and s_b == truth)
        state_counts[committee_state(s_a, s_b)] += 1

a_accuracy = a_cor / a_acc if a_acc else None
b_accuracy = b_cor / b_acc if b_acc else None
fractions = {k: state_counts[k] / GATE_N for k in ("AGREE_CONFIDENT", "DISAGREE", "LOW_CONFIDENCE")}
claimed = {"AGREE_CONFIDENT": 0.9016, "DISAGREE": 0.0424, "LOW_CONFIDENCE": 0.056}
# 2-sigma binomial tolerances at n=2000
tol = {k: 2.0 * np.sqrt(v * (1 - v) / GATE_N) for k, v in claimed.items()}
out["fresh_validation_2000"] = {
    "domain": GATE_VALIDATE_DOMAIN,
    "n": GATE_N,
    "member_a": {
        "accepted": a_acc, "correct": a_cor, "accuracy": a_accuracy,
        "claimed": 0.970846,
        "within_2sigma_of_claim": bool(a_accuracy is not None
        and abs(a_accuracy - 0.970846) <= 2.0 * np.sqrt(0.970846 * (1 - 0.970846) / max(a_acc, 1))),
    },
    "member_b": {
        "accepted": b_acc, "correct": b_cor, "accuracy": b_accuracy,
        "claimed": 0.982644,
        "within_2sigma_of_claim": bool(b_accuracy is not None
        and abs(b_accuracy - 0.982644) <= 2.0 * np.sqrt(0.982644 * (1 - 0.982644) / max(b_acc, 1))),
    },
    "state_counts": dict(sorted(state_counts.items())),
    "state_fractions": fractions,
    "claimed_fractions": claimed,
    "state_within_2sigma": {k: bool(abs(fractions[k] - claimed[k]) <= tol[k]) for k in claimed},
    "parity_balance": int(sum(1 for i in range(GATE_N) if i % 2 == 0)),
}

print(json.dumps(out, indent=2, sort_keys=True))
