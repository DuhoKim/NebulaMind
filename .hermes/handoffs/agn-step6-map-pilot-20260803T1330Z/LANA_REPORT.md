# LANA REPORT — AGN Step-6 pilot (status/debate map v1)

Lane: `agn-step6-map-pilot-20260803T1330Z` · Lana (no-overclaim/semantic lane)
Run window: 2026-08-03T13:05Z → 2026-08-03T13:09Z (≈4 min; 22:05–22:09 KST). Times stamped with `date`, not estimated.

## Process notes

1. Read the brief, then read ALL inputs before writing anything: `claim_status_ledger.jsonl`
   (16 entries, read in two pages), `claim_source_stance_matrix.jsonl` (45 rows),
   `ledger_enums.json`, `status_debate_map_seed.json`, `wording_contract_check.json` (16 template
   sentences, all `passes: true`), and roadmap § Step 6 (lines 400–428 of
   `2026-07-01_205807-paper-prose-distillation-roadmap.md`).
2. Cross-checked stance-matrix row counts against ledger `evidence_spans` per entry:
   3+3+2+2+2+3+3+2+3+2+3+3+4+3+3+4 = 45 = matrix rows. Consistent; every matrix (entry, span_id,
   stance) pair matches its ledger span.
3. Built the map FROM the seed: reproduced its 4 axes via a deterministic rule set (R1–R6 in
   `CONDENSATION_REPORT.md`), then let the same rules place the three entries the seed omits
   (005, 006, 008). Result K=5. All departures from the seed are declared in the map §7 with reasons.
4. Modality law enforcement: every axis statement in the map was written at or below the bound
   entries' ledger `modality` ("can/may" for `may_or_can`; "shows … can occur" for the single case;
   "in simulations / under model assumptions" for `in_model_only`; bare "is/are" only for the three
   `is_are_does` entries). Status labels use only `certainty_level` enum values — including replacing
   the seed's off-enum `widely_supported_scoped` (declared departure #3).
5. Step-6 pass conditions checked: every status traces to entry IDs (map §6 table); every axis has
   named positions with entry IDs; countercase quota answered in-corpus for each `widely_supported`
   status (008 for the ejective mechanism; mutual bounding for 007/009/010 inside the debated Axis C).
   `actively_debated` is reported as a valid result, per the Step-6 stop-condition.
6. Constraints honored: wrote only in the lane dir; no network, DB, git, or DR; did not touch C41
   lanes; did not read `lab-runs/overnight-fesc-sweep-*`. Required Step-6 artifact names
   (`status_debate_map.json` / `STATUS_DEBATE_MAP.md` under RUN_DIR) were superseded by the brief's
   explicit deliverable filenames for this pilot; the brief wins.

## Ledger ambiguities found (reported, not fixed)

1. **"Validated" vs. `pending`.** The brief calls the ledger "16 validated entries," but every entry
   and every stance-matrix row carries `verification_status: "pending"` (`validated` exists as a
   separate enum value and is used nowhere). The map states this on its last line. If Step-6 output
   is meant to build only on validated rows, this corpus does not yet satisfy that precondition.
2. **Off-enum status in the seed.** `status_debate_map_seed.json` axis A uses
   `"widely_supported_scoped"`, which is not in `ledger_enums.json` `certainty_level`. Handled in the
   map as declared departure #3; the enum file and seed should be reconciled upstream.
3. **Symmetric link-direction inconsistency.** The parent–child pairs are encoded inconsistently:
   002↔002a/002b use the consistent convention "source <type> target" (002 `generalizes` 002a; 002a
   `specializes` 002). But 001↔2299_001 both claim `generalizes` toward each other, and
   002↔2299_002 both claim `specializes` toward each other. At least one direction in each pair must
   be wrong under any single convention. R2 sidesteps this (it merges on either direction), but any
   future tooling that walks link direction will misbehave on these two pairs.
4. **Dual pull on clc_agn_003.** It `specializes` clc_agn2299_001 (mechanism) while its risk flag
   and `qualifies` link make it prevalence's guard row. The seed places it under prevalence without
   stating why; I codified the resolution as an explicit rule (R3, risk-flag override) so the choice
   is reproducible rather than tacit.
5. **Qualifier-only evidence base for clc_agn_005.** All three of its spans carry stance `qualifies`
   (no `supports` span anywhere in the entry). This is self-consistent — the assertion is itself a
   qualifier claim — but it means the ledger contains an entry whose `certainty_level`
   (`actively_debated`) rests on zero `supports` stances; worth a convention note upstream.
6. **Fraction field asymmetry.** `scope.fraction` exists for 002/002a/002b/2299_002 but the
   numeric content of other entries (e.g. 3–100 M⊙/yr in 001; factor ~2 in 006; 30–70% in 010) lives
   only inside quotes/scope prose. Dispersion reporting in the map therefore had to pull numbers from
   quoted spans for non-prevalence axes; a structured `numbers` field would make Step-6 dispersion
   mechanical at C41 volume.
7. **Minor:** the ledger's 2024MNRAS.528.4976D title string contains a mangled redshift ("z   2");
   harmless here, but string-matching tools at 10× volume may care.

## Deliverables

- `AGN_STATUS_DEBATE_MAP_V1.md` — 5 axes, 16/16 entries bound by ID, statuses enum-only, seed
  departures declared.
- `CONDENSATION_REPORT.md` — rule set R1–R6, per-entry assignment trace, K=5 as an output.
- `LANA_REPORT.md` — this file.

LANA_AGN_STEP6_COMPLETE_20260803
