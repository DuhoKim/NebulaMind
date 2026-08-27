# P6 receipt — the genuine path transfer, and it overturns P5's background term
(2026-08-26. p6_path_transfer.py, log _tmp_p6_run.txt, 5/5 checks. Answers REGATE2 findings
1–3. NOT yet blind-doubled; nothing here is claimed as confirmed.)

## What P6 adds that P5 lacked

P5 was a single screen: all emission at the junction, one opacity for the whole sky, no source
range. P6 integrates the transfer along the ray, with a separate exterior solved **for every
direction** (each has its own crossing epoch, hence its own ρ̄, N, τ and profile).

The piece P5 did not have is the **depth-to-junction redshift**, derived here from the pinned
metric: for a radial photon k_t̄ is conserved and the null condition gives ṙ̄² = AE²/B, so with
the comoving u^r̄ = √(N−1) each fluid element measures ω = E/√|B| — and a photon emitted at
depth arrives at the junction shifted by **√(|B(r̄)|/|B_junction|)**, with B integrated from
pinned (3.4). Only the ratio matters, so the normalisation is not an assumption.

## The consequence, and it is not small

**B → 0 at the horizon, so Z → 0** (measured: 1.0 at the junction → 1.2×10⁻⁵ at the horizon).
That is standard horizon behaviour — light emitted at a horizon is infinitely redshifted — and
it means:

1. **Deep emission is suppressed**: the emergent beam comes from the near-junction region.
2. **P5's transmitted-background term is WRONG.** P5 carried a background arriving through the
   exterior at strength e^(−τ). There is no such background: the sight line terminates at the
   horizon, and anything from beyond arrives redshifted by ~10⁻⁵. Nothing comes through.
3. **The crossing sky is DARK** — the emergent temperature is a few percent of the interior
   background (monopole −0.93 at the junction-value closure), not a Doppler-shifted copy of it.

## Result

| w | τ_tot | dipole c₁ | bound on x_off/r_*(cross) |
|---|---|---|---|
| 0.999 | 0.037 | 3.844 | 3.53e-4 |
| 0.500 | 0.058 | 3.666 | 3.70e-4 |
| 0.2456 | 0.132 | 3.441 | 3.95e-4 |
| 0.100 | 0.308 | 3.051 | 4.45e-4 |
| 0.030 | 0.930 | 1.503 | **9.04e-4** |
| 0.010 | 2.603 | 2.257 | 6.01e-4 |

**Bound: 3.5×10⁻⁴ to 9.0×10⁻⁴ — one part in 1107 at worst, one part in 2832 at best.**
P5's single-screen treatment gave 2.2×10⁻³ to 5.5×10⁻³, so **the proper path transfer TIGHTENS
the exclusion by a factor of 3–6**, because a dark patch is a louder signal than a shifted one.

## Two things I am flagging rather than smoothing

- **The trend is not monotone**: c₁ falls to 1.50 at w = 0.03 and rises again to 2.26 at
  w = 0.01. P5's clean saturation picture does not survive depth resolution, and I do not yet
  understand the turn. It does not threaten the bound (the worst case is the dip, and the dip
  is still one part in 1107), but "saturates at a floor" is no longer the right description and
  I am not claiming it.
- **The gate's finding 2 is therefore partly vindicated**: the 0.2461 floor WAS a property of
  the fixed-crossing-source model. What survives is the weaker, sufficient statement that the
  dipole stays large at every computed opacity — not that it approaches a limit.

## Standing limits

σ = 1/3, pre-horizon, photon channel; A4 at its LTE upper end (the energy-budget ceiling);
crossing-radius normalisation per the gate's B1 ruling; B normalised at the junction. Blind
double owed before any of this is claimed as confirmed.

---

# CORRECTION, 2026-08-27 — REGATE4 required-repair 4

Appended rather than edited above, so the record shows what was claimed and when.

## 1. The nan defect is repaired, and this receipt's number was right

REGATE4: "The w=0.03 centre tau printed `nan` while a dipole was still reported; this weakens
the script's 'across every computed opacity' presentation." Accepted, and it is the same class
of defect as p1c's: **the table above tabulates τ = 0.930 at w = 0.03, a number the delivered
script could not produce.**

Cause: the terminal event sat at `N = 1` exactly, and at the centre epoch with w = 0.03 the
integrator failed *on* that singular endpoint, so `exterior()` returned None. The dipole
survived because it averages over epochs — **24 of 25 sampled epochs integrated fine, only the
centre one failed** — so a complete-looking result sat next to a blank.

Repair: terminate at `N = 1+ε` (`EPS_HZ`), as in p1c. Convergent, one decade of Δτ per decade
of ε: 0.92960226 → **0.92958804** across ε from 1e-4 to 1e-10. Independent confirmation:
`p1c_rigorous_sweep.py`'s separate 2-state integrator gives **0.928627** at the same w, 0.1%
apart — the same level of agreement as every other row the two share.

A new check now makes this failure mode unshippable: *"every row that reports a dipole ALSO has
a finite tau (no nan hiding behind a result)"* — 6/6 rows finite. Run: exit 0, **6/6 checks**
(was 5/5).

**Scope of the repair, stated because it is not total.** The earliest epoch on the grid
(η = 0.000011, the η → 0 limit) still fails to integrate at all 5 sampled w values. That is a
grid-edge limit, not the singular-endpoint defect fixed here, and it is **not** claimed fixed.

## 2. The Result table above is STALE — do not quote it

It predates the source-temperature reconciliation of 2026-08-26 (the blind double established
T ∝ ρ̄^[w/(1+w)], not the blackbody 1/4 regardless of w). The current script prints materially
different numbers:

| w | c₁ above | c₁ now | bound above | bound now |
|---|---|---|---|---|
| 0.999 | 3.844 | 0.82978 | 3.53e-4 | 1.6360e-3 |
| 0.2456 | 3.441 | 0.50616 | 3.95e-4 | 2.6820e-3 |
| 0.03 | 1.503 | 0.16327 | 9.04e-4 | 8.3149e-3 |

**The headline "one part in 1107 at worst, 2832 at best" is withdrawn.** The current figures are
one part in 120 at worst, 904 at best — roughly a factor of 9 weaker. Any citation of the older
bound is a citation of pre-reconciliation numbers.

## 3. Withdrawn language, per REGATE4's scope audit

- **"The crossing sky is DARK", with the monopole quoted at −0.93** — withdrawn as stated. The
  monopole is a function of the added source map, not of the pinned geometry, and the current
  run gives −0.5283 at the junction-value closure. Its *magnitude* is closure-dependent.
- **"the proper path transfer TIGHTENS the exclusion by a factor of 3–6"** — withdrawn. See §2.
- **"P5's transmitted-background term is WRONG … Nothing comes through"** — this one is NOT
  withdrawn but must be quoted in its narrowed scope. REGATE4 gave Claim 1 a CONDITIONAL PASS:
  it holds for regular sources of finite local intensity and finite relative boost, plus the
  causal no-crossing statement for the horizon itself. The receipt's unrestricted phrasing "for
  a source that is not comoving" was never justified.

## 4. Standing conditionality

The script now carries a header banner: its source construction is an **added thermal closure**
the published papers do not supply, so every dipole, bound and null here is a property of that
assumed source map. REGATE4 separately withdrew null existence as a model-level claim. See
`BHU_CLOSED_ROUTES.md` and `REGATE4_DISPOSITION.md`.
