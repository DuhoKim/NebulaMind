# C41 Track-B Shape 2 — measurement design **v2** (execution gated by Duho 2026-08-04; Kun refutation folded)

> **Revision v2**: Kun's design refutation (`KUN_DESIGN_REFUTATION.md`, verdict
> DESIGN_SOUND_WITH_PATCHES) — all six patches applied. F1: the 10^5.7 low-mass sample is a
> LENSING-cluster sample; its magnification-inheritance chain must be declared per-galaxy and the
> unlensed/lensed split carried through every comparison. F2: differentiation from the crew's own
> z9-10 unlensed study — that work established the deficit's SIGN with Te anchors at z≈9.3–10.6
> and concluded "systematic-limited, not a detection" (−0.69±0.16 dex, Te-scale-dominated); THIS
> design adds the matched-mass re-test across the FULL z>3 range, the A4 FMR offset test the z9-10
> study never touched, and the ledger'd model-prediction confrontation; the z9-10 unlensed anchor
> set IS reused, declared as prior crew work with its published error budget. F3: the calibration
> contract extends beyond Te-vs-strong-line O/H to the **UV-vs-optical abundance channel** (N/O
> class, ~1.4 dex discrepancy scale): UV-derived and optical-derived abundances are never mixed in
> one comparison without an explicitly declared cross-channel systematic term. F4: **pre-fetch
> forecast pre-commitment** — before any science row is fetched, T2a computes and freezes the
> expected Te-anchored N per matched-mass bin and the resulting deficit-precision forecast
> (~0.1–0.2 dex regime), defining the null's information content ("at N anchors/bin, deficits
> larger than X dex are excluded at the scale floor") so a null cannot be retro-justified. F6:
> T2 re-scoped — contract SEMANTICS stay Hwao+Lana; conversion-table/metrology MACHINERY moves to
> Goru with Kun verifying; and Kun's T4 carries his self-declared guard: the A3/A4 ledger anchors
> are inputs-to-attack, not prior work to defend. F7: fallback tables are to be NAMED in T1's
> manifest (recon in progress), with the shape-1 fallback clause intact.

Lane: `c41-trackb-shape2-mzr-20260804T1452K` · Gated: Duho 2026-08-04 14:52 KST, verbatim in the
study history file. Designed by Hwao from the map's settle-lines; Kun refutes this design before
the START gate is requested.

## The question (from the map, not invented)

A3's settle-line: the z>3 auroral/Te anchor set is the deficiency (~25 galaxies in-corpus,
c41_012); feasibility is demonstrated (c41_026/013/061); the disputed deficit claims (c41_043 vs
c41_033/035/044/045) have never been re-tested on matched samples with Te anchors. A4's
settle-line: an FMR test at z>3 holding selection, tracer, and calibration fixed — the c41_040
single-methodology design exists at z<3; its z>3 execution does not.

**Measurement**: assemble the largest possible **Te-anchored z>3 gas-phase metallicity sample**
from public JWST spectroscopic catalogs; on it, (i) re-test the metal-poor-deficit sign and
magnitude on matched stellar-mass samples (A3), and (ii) run the fixed-methodology FMR offset test
at z>3 (A4). Confront both against **ledger'd enrichment-model predictions** (entered as cited
claims, never re-simulated).

## The calibration contract (the known trap, handled first)

- **Single Te-anchored scale for every number that gets compared.** Strong-line values enter ONLY
  through explicitly declared conversions (per-sample, with the conversion's own uncertainty
  propagated); undeclared-scale data are excluded by rule, not judgment.
- The ~0.24 dex Te-vs-strong-line offset class is stated in the protocol with its consequence:
  any claimed deficit smaller than the scale uncertainty of its own sample is reported as
  scale-limited, not as a detection.
- Per-catalog inheritance disclosure (Kun's shared-pipeline rule from Shape 1, imported): each
  sample declares its reduction/line-fitting/mass chain; model predictions calibrated on the same
  chains are flagged in the comparison.

## Data plan (all public, via `nm_external_data` VizieR TAP + resilient fetch)

1. Candidate source catalogs (verify exact VizieR/table availability at execution — none are
   asserted as certain): JWST NIRSpec Te-detection compilations (JADES/CEERS/GLASS/UNCOVER-class
   auroral-line samples), the in-corpus M*≈10^5.7 low-mass sample's public table, and the c41_040
   methodology's z<3 anchor set for continuity.
2. Assembly rules written and frozen BEFORE fetching (Step-1 discipline): inclusion by
   measurement class (auroral detection / Te-consistent limit), never by result.
3. Masses re-homogenized to one IMF/SED convention with declared conversions.

## Model/prediction side

Enrichment-model predictions (FIRE/IllustrisTNG/EAGLE-class published MZR/FMR evolution tracks +
analytic regulator models) enter as **ledger prediction claims with citations** — the Step-4
pattern; nothing is re-simulated; predictions calibrated on the observational chains we use are
flagged per the contract above.

## Non-circularity statement

Data assembly never touches model outputs; the deficit re-test and FMR offsets are computed before
any model track is overlaid; the comparison metric (offset + dispersion vs prediction bands) is
frozen in this design. The known residual risk — shared photometric masses between observation and
some model calibrations — is disclosed, not absorbed.

## Lanes and stages (execution, once gated)

1. **T1 Goru (mechanical)**: catalog reconnaissance + assembly-rule-frozen fetches, per-sample
   provenance manifest, sha-pinned. 2. **T2 Lana (author)**: the calibration-contract protocol
   document + conversion tables. 3. **T3 Goru**: matched-sample deficit re-test + FMR offset
   computation (deterministic scripts, seeds fixed). 4. **T4 Kun (adversarial)**: independent
   reproduction + scale-forensics (his Step-5-style pass on every printed number). 5. **T5 Tori**:
   receipts. 6. Draft only if the result survives T4 — merit panel + your read after.

## Success and failure, defined now

- Success = a scale-honest statement of the z>3 deficit sign/magnitude and FMR offset with
  Te-anchored uncertainties, compared against ledger'd predictions — WHATEVER direction it points.
- An honest null ("scale-limited at current anchor statistics") is a publishable outcome of THIS
  design (it directly answers A3's settle-line by quantifying the anchor gap).
- Failure = only: catalogs unavailable at honest completeness (falls back per plan to shape #1),
  or the calibration contract cannot be satisfied — reported, not patched.
