# C41 Baseline restart — Step 0: the frozen question

Lane: `c41-baseline-restart-20260803T1253Z`
Gate: Duho, 2026-08-03 21:53 KST — "APPROVE C41 STEP 0 — freeze the question"
Status: **FROZEN — 2026-08-03 ~22:05 KST, by Duho via "APPROVE C41 STEP 1"** (question presented
in-session; no edits requested; Step-1 approval on the drafted question constitutes the freeze).
This file is immutable; rewording requires a new Step-0 gate. sha256 at freeze: recorded in
`STEP0_FREEZE_RECEIPT.md` beside this file.

## The question

> **What do we currently know, what is actively disputed, and what remains unknown about how the
> earliest galaxies (z ≳ 6) formed their stars, enriched their gas, and ionized their
> surroundings — and where do simulation/model predictions and JWST observations genuinely
> disagree?**

Three axes, fixed:

1. **Formation efficiency** — star-formation efficiency at cosmic dawn: feedback-free/highly
   efficient episodes, bursty SF, variable IMF, non-thermal regulation; the bright-end UV
   luminosity function as the observable battleground.
2. **Chemical enrichment** — gas-phase metallicities and abundance patterns at z ≳ 6 (down to the
   lowest-mass systems JWST reaches), what enrichment histories they permit, and calibration-scale
   comparability.
3. **Ionizing output** — ionizing photon production and escape (ξ_ion, f_esc), which sources drive
   reionization ("the few" vs "the many"), and the NIRSpec-era budget.

## Scope rules

- **In**: peer-reviewed and arXiv literature assigned to C41 (cluster 41, "JWST high-redshift
  galaxy evolution and emission"), selected by the Step-1 executable protocol; simulation/model
  predictions about the three axes wherever published (model papers may sit outside C41 — they
  enter as ledger'd prediction sources, not corpus members).
- **Boundary case, rule-decided**: Little Red Dots and high-z AGN — IN only insofar as they bear
  on the three axes (e.g., contaminating the bright-end LF or the ionizing budget); their intrinsic
  nature (AGN vs stellar) is NOT a fourth axis. Step 1 encodes this as a filter rule, not a
  per-paper judgment.
- **Out**: z ~ 0 relations except as explicitly-labeled calibration anchors; galaxy-evolution
  topics outside the three axes (quenching at cosmic noon, environment, mergers-as-topic);
  instrument papers except where completeness/selection limits bear on a ledger'd claim.

## Interpretation contract

"Know / dispute / not know" map onto the claim-ledger contract v1 status enums; a claim counts as
**disputed** only when stance-verified sources conflict (Step 5), never on lexicon hits alone.
The deliverable answering this question is the Step-6 status/debate map with its condensation
report. Prose modality may never exceed ledger certainty.

## Freeze block

- Drafted by: Hwao, 2026-08-03 ~21:58 KST
- Frozen by Duho: 2026-08-03 ~22:05 KST via "APPROVE C41 STEP 1" (no edits requested)
- sha256 at freeze: see `STEP0_FREEZE_RECEIPT.md` (computed over this final file)
