# P0 Claim-State Exact Diff

Selected branch: `RETRACT_UNSUPPORTED_MATCHED_SCALE_CLAIM__PRESERVE_UNMATCHED_SUGGESTIVE_STATE`

## Manuscript claim changes

| Surface | Current state | Proposed state | Reason |
|---|---|---|---|
| Abstract sample identity | `~3×10^4` TNG galaxies | “a selected TNG100-1 population” | The adjacent 23,722 invariant may use a different selection. Remove the unsupported count rather than invent equivalence. |
| Abstract MZR | PP04 recompute of 2.0×10^5 SDSS galaxies; −0.40 vs −0.27; factor 1.5; not significant; consistent | Current inputs are unmatched; face-value −0.50 vs −0.23/−0.25/−0.25; about factor two; suggestive; single-scale re-derivation required | No PP04 method, result, figure series, code, or derivation exists. |
| Observational provenance | Nakajima+2023 blended with Lisiecki+2025 supplement | Nakajima+2023 retained; exact inherited medians labeled provisional because the supplement is unverified | Lisiecki A&A 708 A235 resolves to an unrelated 2026 quiescent-galaxy paper. |
| Selection method | Unreferenced “Kennicutt” Hα→SFR conversion | `\citet{kennicutt98}` with identity-complete bibliography row | Kennicutt 1998 ARA&A 36, 189 supplies SFR calibrations. |
| MZR Results | Physical factor-two under-evolution and inferred metal-removal/dilution mechanism | Face-value unmatched-scale factor two; no physical discrepancy, consistency, or mechanism inference | Calibration mismatch is comparable to the apparent shortfall. |
| Figure 2 caption | Factor-two statement without explicit unmatched-scale modifier | Explicit current-unmatched-scale, face-value factor-two statement with calibration caveat | Prevent the caption from outrunning the corrected prose. Figure pixels already carry the calibration caveat. |
| Discussion lead | “real” factor-two chemical shortfall | face-value, suggestive factor-two MZR shortfall on unmatched scales | Align with the existing dominant-caveat paragraph. |
| Conclusion | all oxygen abundances matched; MZR consistent at factor 1.5 | SFMS is the reproducible discrepancy; MZR is suggestive and unresolved until single-scale re-derivation | Removes the controlling abstract/conclusion contradiction. |

## Claims explicitly preserved

- TNG z≈0 SFMS residual: −0.30 dex.
- TNG z≈0 MZR residual: +0.12 dex.
- TNG internal SFMS growth: +1.30/+1.45/+1.61 dex.
- SFMS over-evolution gaps: +0.41/+0.49 dex at z≈4.7/5.4.
- Selection-debiased sample-matched envelope: +0.46/+0.83 dex; up to ~+1.1 dex; sign robust across nine configurations.
- TNG aperture-to-total mass offset: +0.13 dex at z=5 and +0.12 dex at z=6; ~0.08 dex raw-plane effect.
- Body MZR arithmetic on unmatched scales: −0.23/−0.25/−0.25 versus provisional face-value −0.50; ratio about two.
- `human_validated = 0`; descriptive, automated, non-peer-reviewed status.

## Claims removed or demoted

- Removed: performed PP04 O3N2 recomputation from 2.0×10^5 SDSS galaxies.
- Removed: matched-scale observed deficit −0.40 dex.
- Removed: matched-scale TNG internal evolution −0.27 dex.
- Removed: factor-1.5 residual and “not significant/consistent” verdict.
- Removed: `~3×10^4` sample count.
- Removed: specific metal-removal/retention/pristine-dilution mechanism inference.
- Demoted: exact +0.89/+0.96 and −0.50 observed medians to provisional manuscript inputs with unresolved supplemental provenance.

## Representation reconciliation

- `FrontierDrafts.tsx`: P0 summary already states only the supported SFMS result. It remains unchanged; the dead `review` field is removed.
- `paperScores.ts`: DR/Kun chemistry-resolution claims are replaced; Tori’s overbroad “spurious chemical failure” wording is narrowed to the naive 3–4× comparison; Goru’s stale “uncorrected aperture” statement is replaced with the actual unresolved provenance/reproducibility caveats.
- History JSON: intentionally unchanged. It remains evidence of intended-but-not-landed work, not a current verdict.
- Public audit report: intentionally unchanged as a historical audit of the pre-correction served identity.
