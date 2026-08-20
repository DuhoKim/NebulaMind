PASS_COMMITTEE_BUILD

# Kun gate — HC-1H machine committee build (`_committee_20260820/`), 2026-08-20

One-shot kimi gate seat. Method: local files, grep, python3 recomputes under `../venv_torch` (torch 2.8.0 / numpy 1.26.4 / sympy 1.14.0, matching the build receipt runtime). Code read, not just notes. No network. Findings only.

## 1. Spec ordering and frozen member constraints — PASS

- `COMMITTEE_SPEC_20260820.md` mtime 01:23:57 precedes every build artifact: `committee.py` 01:24:51, `train_and_validate.py` 01:26:31, `member_b_weights_frozen.pt` + training receipt 01:29:29, validation 01:29:56, state definition 01:38:39. Both member choices carry explicit recorded rationales in the spec ("This construction was chosen because…", "This member was chosen because…") before any artifact existed.
- Different family from the primary CE-ResNet (frozen I-1, prereg §3): Member A is a training-free deterministic annular winding tracer — no learned parameters, no label source, not a network at all. Member B is a plain sequential LeNet-style CNN (8/16/24 conv blocks, no skip connections, no batch norm, no shared trunk); `test_committee.py` asserts no residual module names. Both architecturally disjoint from CE-ResNet.
- Member A training-free deterministic: confirmed in code — fixed annuli, fixed centre, deterministic median/mode arithmetic, no random seed anywhere in its path.
- Member B trained exclusively on the frozen BS-3 generator: `train_and_validate.py` hard-fails on input hash mismatch before training; the only label is the generator's own synthetic parity. Generator hash verified by me directly: `spike/yui_identity/w_chi.py` SHA-256 `89da33ec6260e75e06eadb0f171da4c52f1478b59ff5e543d363dbf56fefcd75`, identical to BS-3's pins in `GORU_BS3_INVENTORY.md`, `YUI_BS3_IDENTITY_1000_20260814.md`, and `KUN_REGATE_BS1_BS3_20260814.md`. Fresh seed `20260820` recorded in spec §Member B and in the machine receipt; epoch permutation seeds 20260820–20260823 match the receipt. Grep confirms no human chirality label, Galaxy Zoo, or morphology flag anywhere in committee code.

## 2. Antisymmetry rerun, fresh seeded sample — PASS

My own fresh domain `KUN-GATE-ANTISYM-20260820-FRESH`, 300 seeded synthetics, member B loaded from the frozen weights:

- Member A: exact value flip `chi(mirror(x)) == -chi(x)` 300/300; mirrored acceptance decision flips (or both abstain) 300/300.
- Member B: exact value flip 300/300; decision flip 300/300.
- Build receipt's 10,000/10,000 for both members is consistent with this. The exactness is structural (mirror is a byte-exact involution; IEEE subtraction negation is exact), also confirmed symbolically by the SymPy receipt (`pass: true`).

## 3. Fresh seeded 2,000-sample validation rerun — PASS

Domain `KUN-GATE-VALIDATE-20260820-FRESH` (disjoint from both build domains), indices 0–1,999, exactly parity-balanced:

- Member A: accepted 1,902, accuracy 0.9737 — claimed 0.970846, within 2-sigma sampling tolerance.
- Member B: accepted 1,993, accuracy 0.9824 — claimed 0.982644, within 2-sigma.
- States: AGREE_CONFIDENT 1,712 (0.9060), DISAGREE 83 (0.0415), LOW_CONFIDENCE 105 (0.0525) — claimed proportions 0.9016/0.0424/0.0560; all three within 2-sigma at n=2,000.

Claimed accuracies 0.9708/0.9826 and the 9016/424/560 distribution are consistent with my independent rerun.

## 4. Member B weights serialization, hashes, freeze policy — PASS

- File SHA-256 `6e4a6efaf9e9db55e8ca23f1ffa7e61ef437c62bc959c9630b90db0d18aeff0a` and canonical lexicographic float32 SHA-256 `a61e5f726107b716570a9573aa49cbaa0152a55a889c25caf5216f587d542f5d` both recomputed and identical to the training receipt.
- Mode is `0444`; freeze policy (never retrain/recalibrate/fine-tune/prune/re-export/replace; any change = new candidate + new freeze) is stated in spec §Member B and in the receipt, matching BS-3 discipline.
- Post-freeze overwrite refusal is evidenced: `freeze_refusal_summary.log` records exit 1 with identical before/after hashes; the duplicate-invocation containment receipt documents that the concurrent duplicate died at serialization without touching the frozen file.

## 5. Committee-state mapping — PASS

Exactly three states, deterministic pure function of the two member signs: AGREE_CONFIDENT (both nonzero, equal), DISAGREE (both nonzero, opposite), LOW_CONFIDENCE (either abstains). Exhaustive and mutually exclusive over the 3×3 member-value space; documented in spec §"Exact three-state mapping" and `COMMITTEE_STATE_DEFINITION_20260820.json`; unit tests 7/7 pass, including the exhaustive mapping test and threshold pinning (0.08 / 0.15).

## 6. Never-inside-a restriction — PASS

- Stated in spec §Authority verbatim: neither member, either sign, their agreement, nor committee state may enter the attenuation estimate `a`, act as a human reference, select only disagreements, rescue primary failure, or touch the real-sky estimand. Matches the frozen prereg [A1] ("stratifier/allocator/diagnostic only and never inside `a`", hash-pinned `b06901c8…`, mode 0444 verified) and `LANA_ONE_HUMAN_ATTENUATION_20260814.md` §2.
- Code audit: `committee.py` exposes only chi scores, accepted signs (±1/0), the state string, and hashes; `train_and_validate.py` writes only training/validation/state receipts. No code path computes or emits `a`, stratum weights, per-stratum corrections, epsilon, or anything a-adjacent; no real-data or network reference exists in the committee source (the sole "attenuation" hit is the read-only hash binding of the LANA document).

## Integrity note

Current files hash identically to `receipts/FINAL_VERIFICATION_20260820.json` pins (spec, committee.py, train_and_validate.py, test_committee.py, state definition — all five match).

My recompute script: `_committee_20260820/kun_gate_recheck_20260820.py` (gate artifact, does not touch frozen inputs).
