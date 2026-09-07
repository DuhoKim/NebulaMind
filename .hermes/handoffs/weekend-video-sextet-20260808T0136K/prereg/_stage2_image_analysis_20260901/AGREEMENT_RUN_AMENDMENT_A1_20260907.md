# Agreement run — narrow amendment A1, 2026-09-07

**UNADOPTED PROPOSAL, awaiting one independent review by a seat that did not author it.** Authoring only; no execution authority, draw, split or unseen-data access. Proposes amendments to V15 (`fdd9eedd9938c2ba7df312cdc9b82a06612772ccc087e9365b33fd7d9d9a97d1`); its history remains intact.

**Purpose.** One machine–human GZ1 chirality agreement number on unseen images, with a Wilson interval against 0.70. V15 allows global sign reversal: this does not establish agreement with a preassigned clockwise sign.

## Input manifest — full SHA-256 or explicit unresolved placeholder

`UNFIXED_*` names denote missing values, never usable defaults; resolve before commit C. Runtime artifacts must each receive their own filename and digest; unresolved artifact inventories below require expansion, not an aggregate substitute.

| File / file placeholder | SHA-256 / digest placeholder |
|---|---|
| `UNFIXED_ELIGIBLE_IDS_PATH` | `UNFIXED_ELIGIBLE_IDS_SHA256` |
| `_optionA_dev/corpus_identity/dryrun_identities_to_exclude_20260905.txt` | `77b29eafe18e02d4dee621a6e748e8f698381c6e23098e7db2db190aee270c95` |
| `UNFIXED_FAILED_IDS_PATH` | `UNFIXED_FAILED_IDS_SHA256` |
| `VALIDATION_SELECTION_V29_20260905.csv` (failed-ID provenance) | `UNFIXED_FAILED_SET_SHA256` (source only: `5643555c…`) |
| `guarded_pool.csv` (population/provenance) | `2cc94a29562270fcb5043f4ce942e303696f359b5fb0c59fdee48578ebb34155` |
| `UNFIXED_DR9_NORTH_SURVEY_BRICKS_PATH` (provenance) | `2edd5c295fdad26852c6f224a3ff023cff43dd0e03a53acd35b767e726ee72fb` |
| `validation_bricks/_bricks_without_r_coverage.txt` (provenance) | `ba2eb9d16d0d1d47eef2e0d52497b56d44ac979ebe67dd54b33f57c117d7a2fe` |
| `AGREEMENT_RUN_AMENDMENT_A1_20260907.md` (final procedure) | `UNFIXED_FINAL_PROCEDURE_SHA256` (external manifest) |
| `UNFIXED_SELECTION_CODE_PATH` | `UNFIXED_SELECTION_CODE_SHA256` |
| `UNFIXED_RENDERING_PIPELINE_ARTIFACT_PATHS` | `UNFIXED_RENDERING_PIPELINE_ARTIFACT_SHA256S` |
| `UNFIXED_ESTIMATOR_FAMILY_AND_96_SEARCH_PATHS` | `UNFIXED_ESTIMATOR_FAMILY_AND_96_SEARCH_SHA256S` |
| `UNFIXED_ENVIRONMENT_PATHS` | `UNFIXED_ENVIRONMENT_SHA256S` |
| `UNFIXED_SCORING_AND_GATE_PATHS` | `UNFIXED_SCORING_AND_GATE_SHA256S` (validation source only: `65e241ca…`) |
| `UNFIXED_DRAND_CONTRACT_PATH` (chain, hosts/authentication, round clock) | `UNFIXED_DRAND_CONTRACT_SHA256` |

**Eligibility as input.** Per `AGREEMENT_RUN_INPUT_CONTRACT_20260907.md`, selection consumes three pinned one-ID-per-line files. Eligible IDs are ascending and unique; failed IDs are the CSV’s GZ1_OBJID column, sorted ascending and deduplicated, with derivation recorded before C; the dry-run exclusion file retains its pin. Every selection input is passed with its expected digest, recomputed on read; absence, malformation or mismatch refuses, with no default or optional digest. Exclude the 2,000 failed identities and all 2,644 dry-run identities, including 44 skips; verify membership, uniqueness and exclusion disjointness. The guarded 12,054 leave exactly 7,410 before renderability; record the eligible count catalogue-only before C.

File provenance remains V15 §9B.2b: a brick must exist under the binary64 half-open test in the pinned DR9-north survey-bricks table and be absent from the pinned no-r registry, which lists bricks without published r-band images. Neither pixels nor checksum-catalogue membership determines eligibility. The file represents exactly that renderable subset of the 7,410. **The selection/run path does not reimplement the brick test or registry lookup.**

**Selection.** Order post-exclusion identities by unsigned big-endian `SHA256(lowercase seed hex || "||" || ASCII decimal GZ1_OBJID) mod 2^32`, ties by numeric ID; walk ranks, skipping IDs absent from the eligible file. Take 400 tuning, 200 holdout, 2,000 fresh validation; never replace raster/score failures. Retain ordered IDs, bricks, skipped ranks, seed and input/code digests before development fetch or label access. Six checks remain: determinism, disjointness, exclusions, exact sizes, refusal of reuse across draws, and missing-eligibility refusal; digest/malformation refusal also applies.

**Prospective seed.** After the separate amendment decision, fix every manifest entry and procedure; the lane owner commits the manifest and retains commit ID and UTC C. Name the first default-mainnet drand round at least **C + 600 seconds (ten minutes)**: `r = 1 + ceil((C + 600 - G)/P)`, `T = G + (r - 1)P`, with V15's `G = 1595431050`, `P = 30`. Record r, T and commit ID with contemporaneous UTC before T; missed deadline means recorded abort, never substitution. This margin permits recording, not proof of clock honesty; no 24-hour NIST fallback wait remains. Exposed round 6440756 cannot be used.

Retain raw responses: only the named round, identical 64-hex randomness from at least two of api.drand.sh, api2.drand.sh, api3.drand.sh, drand.cloudflare.com, confirmed by live re-fetch; lowercase as seed. This inherited hostname-agreement proposal supplies neither BLS verification nor operator-independence proof; question 4 must be resolved before C. Unavailability means waiting for that round or recorded abandonment, never another source/round.

**Separation, scoring and failure.** Retain the disposition note's KEEP obligations except explicit replacements here: E1–E8 scientific restrictions, §6 pipeline, environment mismatch stop, input/tensor/label checks, custody and access restrictions. Retain the fixed 96-configuration search, complete records, objective `max(k,m-k)/400`, floor 380 and tie-break. Freeze winner code/configuration/preprocessing/environment/results by digest before holdout access. Opening means first participant/process/service access to a holdout pixel, tensor, label or per-object outcome; catalogue IDs alone are not opening. Record before access; partial access/crash consumes the sole opening. Only that winner: m ≥ 190 and Wilson lower bound for `max(k,m-k)/200` > 0.70, z = 1.959963984540054. No retuning/reopening. After PASS, retain the unchanged freeze and custodian fetch-after-freeze restrictions; validate once, 2,000 drawn, floor 1,900, strict lower bound > 0.70; exact denominator/gate remains question 3. Sizes, floors and bar are unchanged.

Keep attempt 1, both step-1 collections, fixtures, corrections and chronology. Register every draw/abort/re-draw with UTC, reason, digests, seed/round, access stage and outcome; registration grants no extra attempt. Exactly one further validation attempt, no secondary or hidden restart. Seed/deadline/input mismatch, reuse/overlap/exclusion breach, premature access, changed freeze or repeated holdout invalidates and stops. No eligible winner or holdout/validation floor/bar failure closes option A. Ties, missing/non-finite/error/non-repeat scores stay unscored; report failures and unscored counts.

## WHAT THE READER LOSES

Departures proposed below; every deferral is out of scope for this run, not deleted or disproved.

- **Eligibility input:** correctness rests on the producing procedure rather than re-proof at selection, which matters if production is wrong; the file and digest must be fixed BEFORE the seed round is named.
- **Failed-ID input:** membership rests on recorded CSV extraction rather than rechecking the CSV during selection, which matters if extraction is wrong; the derived file, its digest and the CSV digest must be fixed BEFORE the seed round is named.
- **Drand only:** NIST certificate/signature/link authentication, primary priority and the 24-hour fallback path disappear, which matters if drand's retained authentication or availability is inadequate.
- **Commit-relative clock:** signature-relative timing becomes a recorded input-commit clock, which matters if that timestamp or prospective designation is unreliable.
- **Legacy builders/driver:** exclusive executable/CLI pins, winner reconstruction, RUN ROOT reconciliation and refusal-token/exit enforcement disappear, which matters if replacement code misimplements retained rules.
- **Legacy schemas/beacon tools:** CORPUS-IDENTITY-2/BEACON-RECORD-3 enforcement and NIST collector/verdict/PKI/probe machinery disappear, which matters if ordinary records omit required bindings or misauthenticate a seed.
- **Witness/provenance stack:** PushEvent/history/per-entry publication, chained seals, blob/origin/ancestry checks, server protection/chat witnesses, Option-A′/B receipts and optional countersigning cease gating, which matters if records or chronology are disputed or dishonest.
- **Composed provenance:** combined evidence-path checking is deferred, which matters if inconsistencies between paths conceal an error.
- **NSD/precedence/input-boundary apparatus:** adversarial evidence-loader refusal coverage is deferred, which matters if hostile evidence reaches this fixed-input run.
- **Broad test gates:** 132 differential controls, table verification, fail-first kit, prescribed fixture/generator/suite commands and beacon negative/behaviour probes cease gating, which matters if defects escape the focused selection checks.
- **`verify_split`:** helper-based split verification is deferred, which matters if retained-list recomputation misses a split error.
- **`holdout_once`:** flag enforcement is deferred, which matters if access records fail to expose a second opening.
- **Seal-append/step 2:** chained append and seal/witness orchestration are deferred while identity-before-access remains, which matters if ordinary digest records can be altered or backdated.
- **Review/release machinery:** repeated two-seat package gates, historical review questions and the V15 release cap are replaced by one independent amendment review, which matters if that seat misses a defect or imported precedence obligations conflict.
- **Two-candidate alternative:** the hypothetical familywise alternative is dropped, which matters if the remaining candidate fails; no substitute becomes available.

## OPEN QUESTIONS FOR THE REVIEW

Unanswered; resolve before fixing the procedure/input manifest.

1. What is the numerical renderable population within the 7,410 post-exclusion identities?
2. What is the full failed-set SHA-256 behind `5643555c…`, and what is the full validation-gate pin behind `65e241ca…`?
3. What exact denominator and calculation does V15's incorporated validation p_val use?
4. Does the recorded later drand-only direction require the exhibited chain-bound BLS verifier rather than V15's two-host agreement?
5. Which exact immutable rendering/gate artifacts belong in the new manifest?
6. How must a render-refused identity be represented to the scoring implementation?
7. What obligations are imported by V15 §10's unreproduced V2 signing/precedence clause?
8. How should the conflicting seal-helper status statements be reconciled by the history owner?
