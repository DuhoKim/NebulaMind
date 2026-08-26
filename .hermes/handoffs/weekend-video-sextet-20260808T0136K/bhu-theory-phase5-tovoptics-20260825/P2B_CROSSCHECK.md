# P2b blind double — DIVERGED, diagnosed, and NOT confirmed
(2026-08-26. First double briefed under METHOD_FINDING_BLIND_DOUBLES.md: normalisation, source
function and binding multipole were left as "choose and justify", not supplied.)

## The method choices agreed — independently, which is the point

gpt1 chose, without being told: (a) sky-mean-normalised temperature contrast, because a shift
common to every direction "is not a dipole and can be absorbed into the unknown source
monopole"; (b) a bounded source, refusing an arbitrarily hot one because it "would make the
requested bound mathematically unclosed"; (c) the dipole as the binding multipole, quantified —
at the strict bound the quadrupole is 1.04e-7 against a dipole of 1.36e-3, and it declined to
substitute a quadrupole limit that was never supplied.

Those are my three choices, reached independently rather than inherited. **That is what this
brief format was changed to produce**, and it worked.

## The numbers DIVERGED by 2.67×, and both causes are found

| | Tori | gpt1 |
|---|---|---|
| dipole coefficient | 0.85652 | 2.28714 |
| bound on the offset | 1.585e-3 – 1.787e-3 | 5.936e-4 – 6.896e-4 |

**Cause 1 (factor 1.392) — a different offset normaliser, and theirs is arguably better.**
I divide x_off by r_*(η_obs) = 2.000, the shock radius *now*. gpt1 divides by r_*(η_crossing) =
1.4366, the radius where our light cone actually meets the shock. The shock radius "now" lies
outside our past light cone and is not observable; the crossing radius is. This is a definition
difference, not an error on either side, but I think gpt1's is the more physical denominator.

**Cause 2 (residual factor 1.92) — an extra propagation redshift, and I believe it is a
double-count.** Their transfer (compute_blind_p2b.py:54) is
`(eta_c/eta_obs) * gamma * (1 + beta*c)`; mine has no `eta_c/eta_obs`. Their raw central value
0.42632 = 0.28169 × 1.51359 reproduces exactly, so the factor is identified beyond doubt.

My argument for omitting it: in the radiation era a ∝ η, so a comoving thermal bath has
T(η) ∝ 1/η, while propagation from η_c to η_obs redshifts by a(η_c)/a(η_obs) = η_c/η_obs.
The two cancel exactly — which is the standard reason the observed CMB temperature does not
depend on emission epoch. Applying the propagation factor without the bath's compensating
temperature evolution counts the redshift once too often.

**But that argument is mine and unrefereed.** It is precisely the kind of claim this lane sends
to a gate rather than settles by assertion.

## Disposition

**P2b's bound is NOT CONFIRMED.** No downstream text may quote 1.585e-3–1.787e-3 as
double-checked; it is single-implementation until this is resolved. The question — whether the
crossing transfer carries a net propagation factor, and which radius normalises the offset —
goes to the Phase 5b re-gate as an explicit item, with both implementations named and the
diagnosis above supplied so the engines adjudicate rather than re-derive from scratch.

**What is unaffected:** P1/P1b (optical depth, separately doubled and confirmed), S1's law, and
the qualitative conclusion, which survives either normalisation — the bound is between one part
in ~560 and one part in ~1700, and a fine-tuning is required in every version.
