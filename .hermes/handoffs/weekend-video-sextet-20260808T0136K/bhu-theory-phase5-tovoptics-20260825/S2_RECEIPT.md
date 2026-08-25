# S2 receipt — the crossing sky is 100,000 times too lopsided
(2026-08-25 18:45 KST, Tori. s2_transfer.py, run log _tmp_s2_run.txt, 4/4 limiting cases.
Blind double: platoon/gpt1_blind_s2/, dispatched before my numbers existed.)

## Blind double: agreement to 12 significant digits

| quantity (t_obs = t_crit) | Tori | gpt1 |
|---|---|---|
| ΔT/T, centred observer | 0.513396 | 0.513395725020 |
| f = 0.001: min / max | 0.512100 / 0.514693 | 0.512100173824 / 0.514692689502 |
| f = 0.01: min / max | 0.500503 / 0.526430 | 0.500503067346 / 0.526429576680 |
| max |ΔT/T| over cases | 0.650855 | 0.650854770294 |
| crossing region at this epoch | whole sky | whole sky (angular radius 180°) |

gpt1's crossing-equation residual is 6.7e-16 and it added a small-β limit check. **S2 stands.**
It also flagged, correctly, that "relative speed" is sign-convention-dependent: which fluid
carries the outward velocity flips the leading order-β sign. Magnitudes and the span are
convention-independent; the sign of the mean shift is not, and nothing below depends on it.

## The result

**Anisotropy span = 2.593 × (x_off / r_*)**, linear for small offsets (verified: the
coefficient is 2.5924 at f = 1e-4 and 2.5925 at f = 1e-3).

| x_off / r_* | span of ΔT/T | versus the observed CMB anisotropy (1e-5) |
|---|---|---|
| 0.001 | 0.0026 | 260× too large |
| 0.01 | 0.026 | 2,600× |
| 0.05 | 0.130 | 13,000× |
| 0.1 | 0.261 | 26,000× |

**Exclusion: x_off / r_* < 3.86 × 10⁻⁶** — the observer must sit within about **4 parts per
million** of the exact centre, or the sky is visibly lopsided at the tens-of-percent level.

## What this does to Phase 4's gated result — the converse it lacked

Phase 4 could only say the hiding condition was SUFFICIENT: staying inside the boundary hides
it, but crossing it was not shown to reveal anything. S2 supplies the missing half. If the
boundary lies inside our last-scattering sphere in any direction, the kinematic imprint is not
subtle — it is a tens-of-percent, axisymmetric temperature gradient. The observed sky permits
that only for an observer centred to ~4 ppm of the boundary radius, which is a fine-tuning of
one part in 260,000, not a natural configuration. **Necessity now holds up to that
fine-tuning**, and the honest statement of the branch's status changes accordingly — pending
gates, and pending S3's formal confrontation with the frozen bounds.

## Stated limits

- **The monopole is not an observable.** All directions share a ≈ +0.51 shift; that rescales
  the mean temperature, which the model does not independently predict, so it is absorbed.
  Every number above is the ANISOTROPY (the span), never the monopole.
- **Kinematic only.** The computation assumes both sides share one radiation bath, so no
  absolute TOV temperature is needed. The cap's absolute brightness would require T_TOV, which
  the pinned metric does not fix — that is **K4** and is NOT computed here.
- At t_obs = t_crit the shock is at z ≈ 2.55, so the "cap" is the entire sky; this is Phase 4's
  EXCLUDED-regime geometry, and both implementations found it independently. The narrow
  marginal band where a true bounded cap exists is a separate configuration, not computed here.
- σ = 1/3, pre-horizon, "rough qualitative models" — the standing caveats travel.
