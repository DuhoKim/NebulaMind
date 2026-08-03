# Local frontier-delta promotion custody

Status: `EXECUTED_AND_VERIFIED`
Run: `overnight-arxiv-frontier-preview-20260731T133649Z`
Manifest SHA-256: `aaa9d4fe45da6a8f12b68325c1dd20f1c141f6f24a9929b99e50ce471dc6b0ba`
Promotion receipt SHA-256: `65a5117e54c0e46eb11189e1559ef195a922d3c88a4a77b7feff79eaa5a460fe`
Independent verification SHA-256: `bd05d04be0bc912a53395ef24598fe1d14ce9f5e3859a45b2d3f27a99718115d`

## Verified state

- Canonical delta rows: 720 before + 233 appended = 953 after.
- Labels: 953, with exact paper-ID set and matching cluster values.
- Embeddings: 953 × 2560 float32 vectors; all finite; zero zero-norm rows.
- Historical paper and embedding bytes are exact prefixes.
- Appended paper and embedding bytes exactly match staged artifacts.
- New IDs overlap neither the 120,676-row immutable base nor the prior 720-row delta.
- All 15 protected non-target files match their locked hashes.
- All 47 sealed-manifest artifacts and all 47 checksum-ledger entries match.
- Frozen ranking constants, rank arithmetic, and zero review holds independently verified.
- Git status exactly matches the input lock.
- Post-promotion suite: 13 passed.

## Active target hashes

- `new_papers.jsonl`: `7ebca5bbdc46d1e92f775bbc0608f367bd44f8dcc102bef76bb669066af2ad38`
- `new_labels.json`: `fd3f4cb056b8f7acedfcb3957f1e65e2019b175bc37c97e87f3ef7a76cfaafd0`
- `new_emb.f32`: `6cb41e46917dae2ade4d98402a92024be856e21eed029bcc64af68be1eef8909`

## Safety boundary

The approved promotion replaced exactly the three local canonical delta files. Verification made zero canonical writes. No DB/SQL, frontend/live/public/cockpit, wiki/evidence/trust, scheduler/cron/LaunchAgent, deploy/restart, external-submission, or Git write occurred. No second promotion was attempted.

Any product/frontend/live/public application remains a separate explicit approval gate.

## Rollback custody — do not execute without fresh explicit approval

The rollback snapshot and guarded rollback script are sealed by the receipt. If rollback is explicitly approved, the hash-bound command is:

`/Users/duhokim/NebulaMind/NebulaMind/backend/.venv/bin/python /Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/overnight-arxiv-frontier-preview-20260731T133649Z/promotion/rollback_local_delta.py --execute --receipt-sha 65a5117e54c0e46eb11189e1559ef195a922d3c88a4a77b7feff79eaa5a460fe`

The rollback script refuses execution unless the active targets still match this verified after-state and the snapshot still matches the exact before-state.
