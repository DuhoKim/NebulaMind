# Member B training and weights-freeze receipt — 2026-08-20

Synthetic-only training completed on the frozen BS-3 generator. No real image, real statistic, human chirality label, primary weight, or network source entered training.

- Fresh seed: `20260820`
- Training images: `20000` (exactly balanced parity)
- Epochs: `4`; final training sign accuracy: `0.980250`
- Weight file SHA-256: `6e4a6efaf9e9db55e8ca23f1ffa7e61ef437c62bc959c9630b90db0d18aeff0a`
- Canonical parameter SHA-256: `a61e5f726107b716570a9573aa49cbaa0152a55a889c25caf5216f587d542f5d`
- Frozen mode: `0o444`
- Machine receipt: `receipts/MEMBER_B_TRAINING_RECEIPT_20260820.json`

Freeze policy: the serialized file is read-only and must never be retrained, recalibrated, fine-tuned, pruned, re-exported, replaced, or overwritten. Any change requires a new candidate and a new recorded freeze.
