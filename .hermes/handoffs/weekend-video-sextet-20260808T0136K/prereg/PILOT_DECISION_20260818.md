# Pilot decision — HC-1H §2b PILOT SELECTED

**Duho, 2026-08-18 20:38 KST, verbatim: "go with the pilot, 150 labels"**

Given in the Hwao session after the harvest/research status report. This closes the choice that
had been open since 2026-08-15 ("Pilot (150 labels) or full (850) — §2b of the HC-1H document;
this is his choice and nothing proceeds without it").

## What is selected — §2b exactly as written

Source: `LANA_ONE_HUMAN_ATTENUATION_20260814.md`, SHA-256 re-verified at decision time:
`b2590e4213e225f9869fe782cfe0f55d8d8979dcb470752836a5cd31a58453fd` (matches the accepted
artifact recorded in `HC1H_ACCEPTANCE_20260815.md`).

- **150 labels**: 90 real (10 per stratum), 40 blind synthetics, 20 mirrored re-presentations,
  under the identical blinding and session rules.
- **Only possible outcomes: PASS-TO-FULL-HC1H or INCONCLUSIVE.** It cannot produce the final
  `a`, cannot feed HC-6, and cannot substitute for the full 850-label design.
- **Carry-forward per Revision 3**: the 40 synthetics are excluded from the final ε̂ (protocol-
  integrity validation only; final ε̂ comes from the full design's 200 fresh synthetics); the
  90 real labels and 20 retests may carry forward only if the pilot passes with the sealed-key
  chain unbroken and the pass rule stays exactly as written.
- **"If a pilot is run, it is run first."** The checker is Duho (one-human design).

## What this decision does and does not do

- DOES: fix the hand-check sequence (pilot first), sized at 150; permits scheduling and harness
  configuration for the pilot when its inputs exist.
- DOES NOT: authorize acquisition or any transfer of real imaging. The STOP-rule crossing
  (fetching real cutouts/bricks) remains a separate, explicit authorization. No real galaxy has
  been touched as of this record; K-8 untripped.

## Sequencing to a runnable pilot

1. Checksum harvest completes (projected 2026-08-20 ~14:00 KST; 40,436/60,308 at record time).
2. Duho authorizes acquisition; route B (public HTTPS + per-brick checksums, currency proven
   2026-08-17) or Globus if `cosmo` approval lands first.
3. Gated cutout pipeline produces the pilot's real-stratum inputs.
4. Yui's HC-1H harness (gated `PASS_HC1H_HARNESS_WITH_OPERATING_BOUNDARIES`,
   `KUN_HARNESS_GATE_20260815.md`) runs the 150-label pilot, Duho labeling.

— recorded by Hwao; the decision and its verbatim wording are Duho's.
