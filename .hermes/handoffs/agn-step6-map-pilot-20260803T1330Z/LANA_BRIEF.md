# LANA BRIEF — AGN Step-6 pilot: status/debate map v1 from the validated ledger

Lane: `agn-step6-map-pilot-20260803T1330Z` (write ONLY here; temps `_tmp_*` here).
Gate: Duho 2026-08-03 ~22:15 KST — "start both" (AGN Step-6 pilot approved as proposed).
You are Lana — the no-overclaim / semantic-review lane. Purpose: exercise the Baseline Step-6
machinery on the small validated AGN corpus BEFORE the C41 track reaches the same stage at 10×
volume, and ship the AGN status/debate map the board has listed as "next" since 2026-07-03.

## Inputs (read-only)

All under `docs/claim_ledger_contract_v1_agn_20260703T0830Z/`:
- `artifacts/claim_status_ledger.jsonl` — 16 validated entries (the ONLY source of claim content).
- `artifacts/claim_source_stance_matrix.jsonl` — stance-verified claim↔source stances.
- `artifacts/ledger_enums.json` + `.md` — the status/stance vocabulary. Use ONLY these enums.
- `artifacts/status_debate_map_seed.json` — an existing Step-6 SEED. Your map builds FROM it;
  where you depart from the seed, say so and why.
- `artifacts/wording_contract_check.json` + `CLAIM_LEDGER_CONTRACT_V1.md` — the wording rules.
- Roadmap Step-6 definition: `.hermes/plans/2026-07-01_205807-paper-prose-distillation-roadmap.md`
  (§ "Step 6 — Compute the research-status/debate map").

## Deliverables (in the lane dir)

1. `AGN_STATUS_DEBATE_MAP_V1.md` — the map: named debate axes; for each axis: the sides, the
   ledger entries on each side (by entry ID — every axis statement must bind to entry IDs; no
   content beyond the ledger), best evidence per side with source-strength, measurement dispersion
   where the ledger carries numbers, current status in contract enums, and "what would settle it".
   Prose modality may NEVER exceed ledger certainty — that is your lane's law.
2. `CONDENSATION_REPORT.md` — 16 entries + seed → K axes: the merge rule stated as a rule (not
   vibes), which entries merged where, which stand alone, K as an output.
3. `LANA_REPORT.md` — process notes, any ledger ambiguities found (report, don't fix), runtime.
   End with marker: `LANA_AGN_STEP6_COMPLETE_20260803`.

## Hard constraints

Read-only outside the lane dir. No network, no DB, no git, no DR. Do not touch the C41 lane dirs
or the overnight lab-runs dirs — and do not read `lab-runs/overnight-fesc-sweep-*` (information
hygiene: this map must not know what studies are being computed elsewhere). If an input is missing
or malformed, STOP and write the blocker into your report. Kun will adversarially red-team your
map afterward; write for a reviewer who wants to catch you overclaiming.
