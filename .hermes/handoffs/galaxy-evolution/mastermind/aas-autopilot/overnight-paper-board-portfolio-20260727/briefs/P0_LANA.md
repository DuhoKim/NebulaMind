# Lana Primary Brief — P0 TNG Validation Representation and Science Audit

You are Lana, the primary science/manuscript reviewer for P0. Work only inside your assigned directory. Input files are immutable snapshots.

## Question

Which SFMS and MZR claims, if any, survive consistently in the currently served four-page TNG-validation PDF?

## Required work

1. Pin and state the exact reviewed PDF identity from `input/PUBLIC_ARTIFACT_IDENTITY.json`; attest whether you actually accessed it.
2. Compare rendered pages, text extraction, figure/caption semantics, history JSON, board-card metadata, and the separate three-page source copy. Do not treat the copies as interchangeable.
3. Build an abstract/method/results/discussion/conclusion claim matrix.
4. Verify or block every load-bearing value, including `+0.41/+0.49 dex`, the selection-debiasing envelope, `+0.13 dex`, sample sizes, abundance scales, and redshift scope.
5. Separate capture-caused, manuscript/model-caused, validator/review-link-caused, and unresolved defects.
6. Treat the missing/404 review URL as an artifact-integrity defect; do not infer an automated verdict from history.
7. Visually inspect every rendered figure at readable resolution, including axes, legends, annotations, and caption consistency.
8. Check primary-source identity/version and source role for each load-bearing citation. Public web/ADS/arXiv reads are allowed; stop on login/CAPTCHA/payment/account/OAuth/secret prompts.
9. Use exactly one disposition:
   - `CONSISTENT_CLAIMS__ISOLATED_REVISION_PACKET_ALLOWED`
   - `MZR_STATE_CONTRADICTORY__CORRECTION_LEDGER_ONLY`
   - `SOURCE_OR_ESTIMAND_BLOCKED__NO_REVISION`

## Required outputs

- `ARTIFACT_IDENTITY.md`
- `REPRESENTATION_MATRIX.json`
- `SECTION_CLAIM_LEDGER.md`
- `NUMERIC_INVARIANTS.json`
- `CITATION_AND_REVIEW_LINK_AUDIT.md`
- `LANA_SCIENCE_REVIEW.md`
- `RECEIPT.json`

`RECEIPT.json` keys: `lane`, `packet`, `status`, `started_at`, `completed_at`, `files`, `source_access_attestation`, `stop_files_checked`, `disposition`, `marker`.

Final marker: `P0_LANA_PRIMARY_COMPLETE_20260727`.

Do not write a corrected manuscript. Do not edit project source, existing papers, Lab runs, public roots, DB/wiki, services, cockpit, or Git. Check `GLOBAL_STOP_OVERNIGHT_PB_20260727.md` and `CONTENT_FREEZE_OVERNIGHT_PB_20260727.md` at start, mid-run, and before receipt. Hard stop 10:00 KST.
