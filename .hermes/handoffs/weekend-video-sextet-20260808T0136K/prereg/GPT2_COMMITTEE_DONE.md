GPT2_COMMITTEE_COMPLETE member_A_accuracy=0.9708460969684166 member_B_accuracy=0.9826444622792937 states=AGREE_CONFIDENT:9016,DISAGREE:424,LOW_CONFIDENCE:560

# HC-1H machine committee completion — 2026-08-20

Synthetic-only build complete. No real data was read, generated, requested, or evaluated; no network was used. The committee is restricted to HC-1H stratification/allocation/diagnostics and is never inside `a`.

- Frozen-law gate: preregistration SHA-256 `b06901c8a0f3a0570af41262453670589d8dc0b20c79c7d4162853c7dfec42d7`, mode `0444`; Lana HC-1H SHA-256 `b2590e4213e225f9869fe782cfe0f55d8d8979dcb470752836a5cd31a58453fd`.
- Member A: deterministic training-free symmetrized annular winding tracer; accepted 9,467/10,000; accepted-sign accuracy 9,191/9,467 = 0.9708460969684166; antisymmetry and mirrored decision 10,000/10,000; QUALIFIED.
- Member B: independently trained plain sequential small CNN, a different family from CE-ResNet; trained only on 20,000 frozen-generator synthetics with fresh seed `20260820`; accepted 9,968/10,000; accepted-sign accuracy 9,795/9,968 = 0.9826444622792937; antisymmetry and mirrored decision 10,000/10,000; QUALIFIED.
- Frozen member-B weights: SHA-256 `6e4a6efaf9e9db55e8ca23f1ffa7e61ef437c62bc959c9630b90db0d18aeff0a`; canonical float32 parameter SHA-256 `a61e5f726107b716570a9573aa49cbaa0152a55a889c25caf5216f587d542f5d`; mode `0444`.
- Exact states: `AGREE_CONFIDENT` = both nonzero and same sign; `DISAGREE` = both nonzero and opposite signs; `LOW_CONFIDENCE` = at least one abstains. Distribution on 10,000 fresh synthetics: 9,016 / 424 / 560 (0.9016 / 0.0424 / 0.0560).
- Verification: 7/7 unit tests pass; SymPy antisymmetry residual is exactly zero; post-freeze overwrite attempt refused with unchanged weight hash; final verification reports all checks PASS.

Artifacts: `_committee_20260820/COMMITTEE_SPEC_20260820.md`, `_committee_20260820/MEMBER_B_TRAINING_RECEIPT_20260820.md`, `_committee_20260820/COMMITTEE_VALIDATION_20260820.md`, and machine receipts under `_committee_20260820/receipts/`.
