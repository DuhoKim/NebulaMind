# BLIND-DOUBLE REBUILD — phase (b), from the pre-registration only

You are the independent second implementation required by PHASE_B_PREREG_20260902.md section 6.
**Rebuild from the pre-registration, not from the first implementation.**

ALLOWED INPUTS (only these):
- `PHASE_B_PREREG_20260902.md` (including its two dated amendments — read them, they bind you)
- `phaseB_model_cls.npz` (the five gated model C_l rows, lmax=191, zero-padded above native)
- `planck_data/COM_Mask_CMB-common-Mask-Int_2048_R3.00.fits`
- `planck_data/COM_CMB_IQU-smica_2048_R3.00_full.fits`

BARRED (do not open): `phaseB_pipeline.py`, `phaseB_c2.py`, `phaseB_production.py`,
`phaseB_observed.npz`, `phaseB_production.npz`, any `_tmp_*` log. Your value is independence.

BUILD, per the prereg + amendments (your own implementation choices where the prereg is silent —
document each):
1. Mask: ud_grade 2048→64, binary at >0.9. Report f_sky.
2. Data: SMICA I_STOKES, K→μK, ud_grade to Nside 64, smooth FWHM 160′, monopole+dipole removed by
   least squares on unmasked pixels (Amendment 2).
3. Estimator: uniform-weight pixel-pair Ĉ(θ) in 3° bins (Amendment 1), for masked data and masked
   simulations identically; S_1/2 = ∫_{-1}^{1/2} Ĉ² d cosθ via Gauss–Legendre nodes with linear
   interpolation from bin centers. Implement the pair sums ANY correct way you choose.
4. Observed value: report your S_1/2^obs. (The literature range is ~1,000–1,300; if you land far
   outside, say so plainly — do not tune toward it.)
5. MC: for each of the five rows: synthesize at Nside 64 with the same 160′ beam (no pixel window),
   apply mask, remove mono/dipole identically, estimator, S_1/2. Use n = 500 skies per row (reduced
   from 2,000 purely for your time budget — state your n), seeds of YOUR choosing, recorded.
6. Report per row: median, 5th percentile, and P(S_1/2 <= S_1/2^obs | row). Percentiles only, no
   verdict language (prereg section 5).

DELIVERABLES: `phaseB_blind_codex.py` (runnable) and `PHASEB_BLIND_codex_RESULT.md` with the
script's ACTUAL pasted output. If the MC cannot finish in your time budget, reduce n (floor 200)
and state it — a finished smaller run beats a dead larger one.
