# Cycle 4 — Goru: three open TNG data flags on paper #4 (TNG massive-galaxy abundance), RESOLVED

Source: **real TNG100-1 group catalogs**, pulled via the public API (same api-key + col-4=stars
convention as `tools/lab_runner_worker.tng_field`). Standalone script `c4_goru_tng.py` (+ cached
chunks in `_tng_c4/`). Did NOT touch the worker daemon/queue or any tracked file.

**API status:** reachable but the EU data node was heavily throttling; the single-field extraction
endpoint 504'd persistently, so I fell back to per-chunk downloads. TNG groupcat subhalos are ordered
by **descending FoF-halo mass**, so the entire massive end (logM⋆>10.3) sits in the FIRST chunk of the
448. This is verified, not assumed — see convergence below — so the counts are COMPLETE and exact, not
partial. Snapshots verified against the API: **z=5 → snap 17 (z=4.996)**, **z=6 → snap 13 (z=6.011)**.
Box = 75 Mpc/h, h=0.6774 → V = (110.72 Mpc)³ = **1.357×10⁶ Mpc³**.

Convergence proof (per-chunk max logM⋆, chunks ordered by halo mass):
- z=5: chunk0 max=**11.31** (N>10.5 = 20); chunk1 max=**10.21** (0); chunk2=9.77; …; chunk13=8.17. → nothing above 10.5 past chunk0.
- z=6: chunk0 max=**10.69** (N>10.5 = 4); chunk1 max=**9.41** (0); chunk2=8.83. → nothing above 10.5 past chunk0.

===============================================================================
## THREE RESOLVED NUMBERS
===============================================================================

### E6 / M4 — TNG stellar-mass aperture + definition offset
**The paper's TNG abundance uses the 2×stellar-half-mass-radius aperture (`SubhaloMassInRadType`), NOT
total bound stellar mass (`SubhaloMassType`).** Proof: at z=5, 10^10.5,
- n(2R½ aperture) = **1.11×10⁻⁵ Mpc⁻³** (N=15) ← matches the manuscript's quoted 1.1×10⁻⁵ to 2 sig figs
- n(total bound) = 1.47×10⁻⁵ Mpc⁻³ (N=20)

**Median offset total − 2R½ = +0.13 dex** (z=5, logM⋆>10.3, N=43; 16–84% = +0.09/+0.16; +0.12 dex at z=6,
so redshift-stable). Observed SED masses are total-galaxy, so the paper currently compares a **total-mass
observation to a 2R½-aperture simulation** — a like-for-like violation of +0.13 dex that biases the
apparent excess UPWARD by 0.13 dex.

### E7 / M5 — raw in-box count (single-anchor fragility)
z=5, above 10^10.5 in V=1.357×10⁶ Mpc³:
- **N = 15** (2R½, the paper's convention) → n=1.11×10⁻⁵, **Poisson ±26% (±0.10 dex)**
- **N = 20** (total) → n=1.47×10⁻⁵, Poisson ±22% (±0.10 dex).
It is **~15–20 objects, not hundreds** — Poisson-fragile as flagged. The whole z=5 TNG anchor is 15–20
galaxies, all centrals of the box's most massive halos; the ±0.10 dex Poisson floor propagates directly
onto the 0.43-dex gap and the required shift.

### E7 / M6 — z=6 abundance (bracketing "z≈5–6")
z=6, above 10^10.5:
- **n(total) = 2.95×10⁻⁶ Mpc⁻³** (N=4, Poisson ±50%)
- n(2R½) = 7.4×10⁻⁷ Mpc⁻³ (**N=1**, ±100% — too few to quote; use the total value at z=6).

TNG evolves **a factor 5.0× (0.70 dex) between z=5 and z=6** (total). So "z≈5–6" is NOT a safe single-value
label: the correct TNG comparison depends on the observed sample's **median** redshift.
- obs median z≈5.0 → use 1.1–1.47×10⁻⁵ (headline holds).
- obs median z≈5.5 → TNG interpolates to **6.6×10⁻⁶** (total); obs/TNG = 3e-5/6.6e-6 = 4.5× = 0.66 dex →
  required shift **0.42 dex** (up from 0.28).

===============================================================================
## EXACT MANUSCRIPT TEXT TO DROP IN
===============================================================================

**M4 (fills Tori's §3.1 placeholder — add as budget term #0, or fold into the like-for-like paragraph):**
> "TNG100-1 stellar masses in this work are the within-2×stellar-half-mass-radius aperture
> (`SubhaloMassInRadType`); we verify this reproduces the quoted n(>10^10.5, z=5)=1.1×10⁻⁵ Mpc⁻³
> (15 subhalos in the (110.7 Mpc)³ box), whereas the total gravitationally-bound stellar mass
> (`SubhaloMassType`) gives 1.47×10⁻⁵ Mpc⁻³ (20 subhalos). The observed SED masses are total-galaxy;
> we therefore place TNG on the same total-mass footing, an aperture correction of **+0.13 dex**
> (median over logM⋆>10.3 at z=5; +0.12 dex at z=6). With TNG on total masses the z=5 abundance is
> 1.47×10⁻⁵ Mpc⁻³, the observed excess is 2.04× (0.31 dex, not 0.43 dex), and the shift required to
> erase it falls to **0.20 dex** at s=−1.58 — reinforcing, not weakening, the z≃5–6 consistency."

**M5 (fills the single-anchor fragility flag; footnote to Table 1 / add to §4):**
> "The z=5 TNG anchor comprises **15 subhalos** above 10^10.5 (2R½; 20 on total masses) in the
> (110.7 Mpc)³ = 1.357×10⁶ Mpc³ box — a Poisson fractional error of **±26%** (±0.10 dex). Both the
> 0.31–0.43 dex observed excess and the 0.20–0.28 dex required shift therefore carry an irreducible
> ±0.10 dex cosmic-variance/Poisson floor from the simulation side; the confrontation rests on tens,
> not hundreds, of simulated massive galaxies confronting a single observational data point."

**M6 (fills the z=6 bracket flag; replace any bare "z≈5–6" TNG value):**
> "TNG100-1 cumulative number densities above 10^10.5 evolve steeply: n(total) = 1.47×10⁻⁵ Mpc⁻³ at
> z=5 (N=20) and 2.95×10⁻⁶ Mpc⁻³ at z=6 (N=4), a factor 5.0 (0.70 dex) over Δz=1 (the 2R½ z=6 value,
> 7.4×10⁻⁷ Mpc⁻³, rests on a single object and is not used). Because of this steep evolution we compare
> at the observed sample's median redshift rather than across a '5–6' range: at z≃5 the required shift
> is 0.20 dex (total-matched), rising to ≈0.42 dex if the effective comparison redshift is z≃5.5."

===============================================================================
## DOES THIS CHANGE THE PAPER'S CONCLUSION?
===============================================================================
**Headline (z≃5–6 consistency within budget) does NOT collapse, but M6 forces a phrasing demotion.**

- **M4 STRENGTHENS it.** Fixing the aperture mismatch puts TNG at 1.47×10⁻⁵ (total), shrinking the excess
  from 0.43→0.31 dex and the required shift from **0.28→0.20 dex** — ~0.4× the 0.46–0.55 dex budget, with
  margin, still IMF-independent.
- **M5 is a caveat, not a collapse.** ±0.10 dex Poisson on the anchor; the excess and the shift both
  survive it (0.20 ± 0.10 dex required vs 0.46–0.55 committed).
- **M6 is the one with teeth.** The single z=5 anchor is only fair if the Weibel+2024 sample median is
  z≈5. Across z=5→6 TNG drops 0.70 dex, so if the obs median is ≈5.5 the required shift rises to ≈0.42 dex
  — still inside the 0.46–0.55 budget but with the margin nearly gone, moving z≃5–6 from "robust and
  IMF-independent" toward "within budget, thin margin." **Action for the writer:** pin the comparison to
  the Weibel+2024 sample's actual median z and quote the z=5 AND z=6 TNG values; do not quote a single
  "z≈5–6" number. If that median is ≲5.2, the headline stands and is strengthened by M4; if ≳5.4, soften
  "robust" to "within budget."

Net: two of three flags (M4, M5) confirm/strengthen the result; M6 does not reopen the ΛCDM verdict
(ε=0.20 hard-bound argument is untouched) but requires the z-matched framing and a margin caveat.

Verified numbers table (real TNG100-1):
| z | snap | N(>10^10.5) total | n_total | N 2R½ | n_2R½ | aperture offset |
|---|------|---|---|---|---|---|
| 5.00 | 17 | 20 | 1.47×10⁻⁵ (±22%) | 15 | 1.11×10⁻⁵ (±26%) | +0.13 dex |
| 6.01 | 13 | 4 | 2.95×10⁻⁶ (±50%) | 1 | 7.4×10⁻⁷ (±100%) | +0.12 dex |

Script: `c4_goru_tng.py`; cached catalogs `_tng_c4/gc_{17,13}_*.hdf5`. Fields: Subhalo/{SubhaloFlag,
SubhaloMassType[:,4], SubhaloMassInRadType[:,4]}, ×1e10/h, SubhaloFlag==1 galaxy cut.
