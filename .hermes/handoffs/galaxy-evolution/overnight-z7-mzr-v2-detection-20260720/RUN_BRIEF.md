# Overnight run — z>7 MZR: descriptive → validated detection (Pick #1)

Build on overnight-z7-mzr-20260720 (referee MINOR, bounded selection-robust ~0.25–0.41 dex deficit,
CI excludes 0, but STILL descriptive). Goal: close the 3 blockers that keep it from a validated detection.

## The pre-committed decision rule (LOCKED before any new number)
Upgrade the label from "selection-bounded DESCRIPTIVE" → "DETECTION of z>7 MZR evolution below the
extrapolated local relation" **only if ALL hold**:
1. the mass-controlled deficit's sign + (bootstrap 95% CI excludes 0) survives in **≥2 independent surveys**
   (not Nakajima+23 alone), computed per-survey;
2. it survives **≥2 independent calibration transfers** (KE08 T04→PP04-O3N2 AND a second Te-independent path);
3. it survives in **≥1 orthogonally-selected** subsample (lensed / deep-continuum, i.e. NOT emission-line-selected).
Otherwise it STAYS descriptive — and that is an honest, submittable result. Both outcomes admissible.

## Blockers to close
- B1 single-survey: add Curti+24 (JADES; NOT in VizieR TAP → try MAST/JADES DR / CDS / the DR packet registry)
  and Heintz+23; target N≳40 in the mass-overlap [8.0,9.5] across ≥3 surveys.
- B2 calibration-leaning: add a 2nd, Te-independent transfer; report the deficit as the INTERSECTION of transfers.
- B3 selection: add an orthogonally-selected (lensed/continuum) subsample; if the deficit holds there, the
  selection caveat collapses. (z>7 sim comparator = Pick #2, deferred.)

## Reuse from the z7 lane (../overnight-z7-mzr-20260720/)
sdss_anchor.json (SDSS T04 anchor + KE08 cubic), z7_metallicity.csv (Nakajima+23 z>7 sample),
selection_forward_model.py + selection_results.json (the MC selection model), results.json, PREREGISTRATION.md.

## Guardrails
No fabrication; if a sample can't be pulled, SAY SO and the rule holds (stays descriptive). Every number carries
a bootstrap CI. Calibration reconciled (mass-DEPENDENT). Honest label = whatever the rule outputs. Times in KST.
Crew writes outputs via Bash/python (shared-checkout Write guard active).

## Phases
A Data (independent + orthogonal samples) · B Analysis (per-survey Δ, 2nd transfer, apply rule) ·
C Draft update + referee + verdict (lift cap or keep descriptive per the rule).
