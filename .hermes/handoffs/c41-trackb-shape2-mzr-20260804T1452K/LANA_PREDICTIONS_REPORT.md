# LANA — Shape-2 Prediction-Class Ledger Entries (C41 Track B)

- **Author role:** Lana
- **Composed:** 2026-08-04T15:50 KST (stamped via `date`)
- **Deliverable:** `C41_PREDICTION_ENTRIES.jsonl` — 11 prediction-class entries, study lane only (NOT merged into `C41_LEDGER.jsonl`; merge is a later gated act)
- **Sources:** `c41-baseline-restart-20260803T1253Z/SPAN_TABLE.jsonl` (16,103 spans, 180 papers, sealed corpus) + model-mentioning ledger entries as pointers
- **Enums:** validated against `ledger_enums_v1_1.json` — modality / epistemic_type / certainty_level / source_access / verification_status / stance / rhetorical_zone / links.type all conform. Zero validation errors.

## Why these entries exist

`MEASUREMENT_DESIGN_V1.md` (Model/prediction side) requires enrichment-model predictions to enter as
**ledger'd prediction claims with citations** — never re-simulated. The C41 ledger (80 entries) had
**zero** prediction-class entries. These 11 fill that gap.

## The 11 entries

| ID | Prediction | Numeric? | Source modality |
|----|-----------|----------|-----------------|
| c41_pred_001 | FMR is redshift-invariant (Mannucci 2010 / Lilly 2013 regulator) — null-evolution prediction the Shape-2 offsets test | zero-band | analytic model, cited in obs full text |
| c41_pred_002 | IllustrisTNG: metallicity at fixed M* declines with z; z=8 is ~0.5 dex below z=0 (Torrey 2019) | 0.5 dex | sim prediction cited in obs full text |
| c41_pred_003 | IllustrisTNG mechanism: metal retention efficiency rises with z; rising gas fraction drives MZR evolution | no | sim prediction cited in obs full text |
| c41_pred_004 | FIRE-2 MZR normalization at 4<z<10 is ~0.14 dex above Sarkar+2025 best fit | 0.14 dex | sim prediction cited in obs full text |
| c41_pred_005 | FirstLight MZR normalization at 4<z<10 is ~0.36 dex above Sarkar+2025 best fit | 0.36 dex | sim prediction cited in obs full text |
| c41_pred_006 | FIRE bursty feedback predicts a z-trend contradicted by observed slope 0.067±0.013 dex/unit-z (which matches TNG smooth feedback) | via slope | sim prediction cited in obs full text |
| c41_pred_007 | COLIBRE variable-IMF sim: z=5 MZR elevated — factor ~2 metal mass fraction at M*=1e9 vs fiducial | ×2 | **simulation full text, direct** |
| c41_pred_008 | COLIBRE: z=5 MZR cannot discriminate IMF (scatter ≈ offset at M*≲1e10); low-z MZR is the strongest constraint | band | **simulation full text, direct** |
| c41_pred_009 | Astraeus evolving-IMF (Cueto 2024): ×1.6 elevation at M*~1e9 at z=6; minimal MZR evolution at z>6 | ×1.6 | sim prediction cited in sim full text (secondhand) |
| c41_pred_010 | Astraeus X: top-heavy-IMF z>10 galaxies have the LOWEST gas-phase metallicities (accretion dilution beats yield boost) | no | **simulation full text, direct** |
| c41_pred_011 | Gas-regulator models: MZR flattens at log(M*)≥10 as Z→yield; no turnover probed yet at z>3 | no | analytic model, cited in obs full text |

All entries: `entry_class: "prediction"`, tag `prediction_class`, `modality: in_model_only`,
`model_dependence: high`, `verification_status: pending`, bound to exact SPAN_TABLE span IDs with
verbatim quotes, `as_of: 2026-08-04`.

## Notable model-space structure captured

- **Sign disagreement worth confronting:** COLIBRE (pred_007) and Cueto/Astraeus (pred_009) predict a
  top-heavy IMF *elevates* the MZR (yield-dominated); Astraeus X (pred_010) predicts top-heavy-IMF
  galaxies sit *lowest* in metallicity (dilution-dominated). Linked as `qualifies` — a real
  disagreement the Shape-2 confrontation can exploit.
- **The null model is ledger'd:** pred_001 (FMR invariance) is the prediction the A4 FMR-offset track
  actually tests; pred_011 is the regulator shape prediction for the high-mass window.
- **TNG vs FIRE discriminant:** pred_002/003 vs pred_006 are linked `contradicts` — the observed
  decline slope is the discriminating statistic.

## Honest scarcity — per-paper, where spans carry NO numeric z>3 MZR/FMR prediction

Checked every sim/enrichment-model paper the brief pointed at:

- **2025MNRAS.537..629D (Dome+ — the burstiness multi-physics sim paper):** NO MZR/FMR prediction in
  its 95 spans. Its metallicity content is mock-SED methodology plus a ~1 dex stellar-metallicity
  mismatch against one observed quiescent galaxy (JADES-GS-z7-01-QU). Burstiness predictions are about
  SFMS scatter/mini-quenching, not metallicity scaling relations. **Not ledger'd — nothing invented.**
- **2025MNRAS.544..513M (thesan-zoom "Burst, quench, repeat"):** metallicity appears only as an
  SFR-tracer systematic. No MZR/FMR prediction. Not ledger'd.
- **2026MNRAS.545f2240B (SPICE UVLF-variability sim):** metallicity enters only via hypernova fraction
  and dust scaling. No MZR/FMR prediction. Not ledger'd.
- **2026JCAP...01..008C (semi-analytic UVLF+clustering; pointer c41_080):** UVLF/reionization only;
  no metallicity prediction in spans. Not ledger'd.
- **2023ApJ...951L...1P (THESAN SFRD; pointer c41_022):** SFRD prediction, outside MZR/FMR scope.
- **2020MNRAS.499.1652T (pointer c41_031, top-heavy-IMF O/Fe):** O/Fe plateau physics at z~2 —
  below the z>3 scope. Not ledger'd.
- **AURORA (2026ApJ..1003L..41K) six-simulation comparison:** predictions are at z~2 — below scope.
  Not ledger'd (noted here because its spans are rich; wrong epoch).
- **EAGLE:** spans carry NO numeric EAGLE band, and Sarkar+2025 is internally inconsistent about it
  (abstract: slope consistent with TNG *and* EAGLE; §7: more consistent with TNG *than* FIRE-2 and
  EAGLE). Recorded as a flag inside pred_006's verification_note instead of a fabricated entry.

## Caveats for the gate reviewer

1. All bound spans are `zone: unknown` except where noted — v1.1 rule-7 extension concerns
   *observational* entries; these are prediction-class (theory/simulation), but Kun should still rule
   on whether unknown-zone spans binding prediction entries need per-span adjudication.
2. pred_004/005/006 magnitudes are expressed **relative to the Sarkar et al. (2025) best fit** — the
   spans carry the offsets that way. Calibration-chain caveat of the Shape-2 contract applies (sim
   predictions calibrated on the same observational chains must be flagged in the comparison).
3. pred_009 is a **secondhand citation** (Cueto et al. 2024 numbers reported inside Durrant et al.
   2026, which is in-corpus; Cueto et al. itself is not). Flagged for primary-source confirmation.
4. pred_005's FirstLight source paper is not named inside the bound span — citation resolution needed
   before merge.
5. Entry IDs use the `c41_pred_###` namespace to avoid collision with `c41_001`–`c41_080`.

Lane-only writes: `C41_PREDICTION_ENTRIES.jsonl`, this report, and `_tmp_lana_pred_*` intermediates
all live in `c41-trackb-shape2-mzr-20260804T1452K/`. Main ledger untouched.

LANA_SHAPE2_PREDICTIONS_COMPLETE_20260804

---

## PATCH — scope.baseline + scope.direction (2026-08-04T16:44 KST)

Per Kun's T4 §2a adjudications (`KUN_T4_FORENSICS.md`) and this report's caveats #2–4, each of
the 11 entries' `scope` object gained two fields, in place, via `_tmp_lana_scope_patch.py`
(roundtrip-guarded: every line was verified to reserialize byte-identically before edit, so no
other field changed):

- **`scope.baseline`** — the reference frame the prediction's magnitude is measured against:
  - pred_001: local SDSS z~0 FMR surface (Mannucci 2010 anchor) — self-test frame vs the A4 offset track.
  - pred_002: **internal z=0→z=8 evolution** (TNG's own z=0 normalization); lane-frame comparison
    needs the z<3 anchor's own evolution declared (Kun §2a).
  - pred_003: internal TNG redshift trend (mechanism-level, no observational frame).
  - pred_004/005: **Sarkar et al. (2025) best-fit normalization** — a frame distinct from the lane's
    z<3 Te-anchor; bridge required (Kun §2a "frame-blocked"; caveat #2; pred_005 also caveat #4).
  - pred_006: observed combined-sample slope 0.067±0.013 dex/unit-z (literature-level frame, Kun §2a).
  - pred_007/008/009: **model-internal** variant-vs-fiducial offsets (COLIBRE fiducial; COLIBRE
    inter-sim offset vs z=5 scatter with the z=0 MZR as falsifying frame; Astraeus Salpeter variant) —
    not observationally testable without a fiducial-model normalization (Kun §2a; pred_009 caveat #3).
  - pred_010: internal metallicity rank across the Astraeus z>10 model population.
  - pred_011: the MZR's own lower-mass slope as Z→yield (internal shape; unprobed at z>3).
- **`scope.direction`** — per each assertion's own wording: null/invariant (001), decline (002),
  increase (003), elevation (004/005/007/009), bursty deviation from smooth decline (006),
  degenerate-at-z=5/sharpening-toward-low-z (008), depression/lowest (010), flattening/turnover (011).

No other field was modified. Lane-only write; main ledger untouched.

LANA_SCOPE_FIELDS_COMPLETE_20260804
