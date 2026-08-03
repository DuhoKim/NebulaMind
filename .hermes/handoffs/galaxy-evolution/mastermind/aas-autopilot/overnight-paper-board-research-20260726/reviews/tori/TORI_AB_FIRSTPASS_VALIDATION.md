# Tori Validation — Packets A/B First Pass

Marker: `OVERNIGHT_PAPER_BOARD_TORI_AB_FIRSTPASS_VALIDATION_V1`

Status: `PASS_INPUT_INTEGRITY__A_REPAIR_REQUIRED__B_SEMANTIC_REVIEW_REQUIRED`

## Grounding and no-drift checks

- Tori independently reran the 38-file source SHA-256 check against `baseline/INPUT_SHA256.txt`: PASS.
- Current Lab source JSONs/directories changed by this run: 0.
- Existing PDFs replaced: 0.
- Public/static roots changed: 0.
- DB/wiki/API/page-version writes: 0.
- Deploy/restart/git/cron/browser/account/billing actions: 0.

## Packet A — Goru first pass

Preserved first-pass artifacts:

- `packets/A-mzr-reconciliation/goru/MZR_FIELD_MATRIX.csv` — SHA-256 `411d1f3be6a0ed9e9e6a380ffd7062c9852f8f34d8e008b22e2136f4d9ae4a0e`
- `packets/A-mzr-reconciliation/goru/MZR_FIELD_MATRIX.md` — SHA-256 `65048a8d497080b975c763959a36f4400d77475b709909f1004a51abcc8457ac`
- `packets/A-mzr-reconciliation/goru/PROVENANCE_NOTES.md` — SHA-256 `9fe16d6dd56e66b71a0d235c75bcafd7b21159e018ed1d7ec3c76dfce3bb31c3`
- `reviews/goru/GORU_PACKET_A_RECEIPT.md` — SHA-256 `b7ac33bef22443a4e0fcd464b0e7ce8e4bf0869df790719e6721a1b24aff5f7c`

The first pass is useful but does not satisfy its own completion contract:

1. The receipt does not list SHA-256 values for its produced files, although the brief requires them.
2. The receipt says no STOP conditions and no files modified but omits the out-of-scope creation of `/tmp/inspect.py`. Tori rejected execution of that helper, verified its exact 716-byte contents and SHA-256 `25128dcfdef2855f02d8b7a5bfeffe6cf029e49aa4554004e96c84ad7382417c`, then removed that exact task-created temporary file to restore the scope boundary.
3. `MZR_FIELD_MATRIX.md` records redshift as `ABSENT` for `gated-e2e-demo` even though `spec.topic` explicitly contains the verbatim phrase `the z=0 gas-phase mass-metallicity relation of galaxies: IllustrisTNG vs SDSS`. The field must distinguish a stated topic-level `z=0` from a wholly absent redshift.
4. The receipt's “No files were modified” wording must be narrowed to “immutable source files were unchanged”; new output artifacts were created.

Tori validation state for Packet A first pass: `BLOCKED_FOR_VERSIONED_REPAIR`. Preserve these v1 hashes; do not overwrite them silently.

## Packet B — Kun first pass

Preserved first-pass artifacts:

- `packets/B-citation-integrity/kun/UNSUPPORTED_CLAIM_MAP.md` — SHA-256 `54cf78b57b61d0a4ddb755f8a1d6f96ed53e25873a08268a775102af6f720498`
- `packets/B-citation-integrity/kun/UNSUPPORTED_CLAIM_MAP.csv` — SHA-256 `b1cec58ae9f30b1845988f40c563c50d36f9cb19475f1c53b67e0da55c436f2b`
- `packets/B-citation-integrity/kun/METHOD.md` — SHA-256 `fc278658bedb6e488a16dff303373310d13e7a0c879ee795892db53e2383b2e2`
- `reviews/kun/KUN_PACKET_B_RECEIPT.md` — SHA-256 `cac3a11b080ea99dd236da50cb053cfb7176300b0138f9d03fd86abde0a56206`

The CSV parses with 6 checked rows: 4 for `gated-e2e-demo`, 2 for `gated-halt-demo`, and none for `fesc002`. The candidate edits are isolated and source files remain unchanged.

However, the stored gate reasons are internally awkward at the citation-key level:

- The row keyed `Torrey2019` is marked unsupported while its own reason says the compared passage mentions Torrey's mass-metallicity work but not Qi's content.
- The row keyed `Guo2016` is marked unsupported while its own reason says the passage mentions Guo's study but not Garcia's content.

Kun accepted those booleans mechanically and removed the Torrey and Guo clauses. That is conservative, but it may discard valid anchors rather than diagnose a compound-sentence/key-assignment defect. The corrected candidates therefore require Lana's semantic/no-overclaim review and Goru's independent one-to-one mechanical cross-check before Hwao can declare Packet B clean or choose removal versus sentence-splitting/re-grounding.

Tori validation state for Packet B first pass: `PROVISIONAL_PENDING_LANA_AND_GORU_REVIEW`.

## Next Hwao gate

Hwao should issue versioned repair/review briefs for:

1. Goru Packet A v2 repair, preserving v1 hashes and correcting the receipt/redshift/scope incident.
2. Kun Packet A independent reproducibility/duplication analysis.
3. Lana Packet B semantic/no-overclaim review.
4. Goru Packet B one-to-one citation cross-check after Packet A v2 completes.

Packet C remains gated on Hwao's Packet A canonical decision. No promotion/publication packet may be prepared from first-pass A/B artifacts.
