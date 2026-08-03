# Cycle 2 — Goru (numeric crux for paper #4: TNG massive-galaxy abundance)

Target defect (Kun/Goru cycle-1): the "consistency" null is **cheap** — bought by an asserted "~1 dex" budget and a 0.28 dex shift, neither itemized nor benchmarked. Below: (M1) a real budget ledger, (M3) a ΛCDM-ceiling benchmark, and the falsification thresholds. All numbers are writer-ready.

Manuscript anchors (from the PDF): z≃5–6 observed n(>10^10.5)=3×10⁻⁵ Mpc⁻³ (Weibel+2024) vs TNG100-1 1.1×10⁻⁵ at z=5 → 2.7× (0.43 dex); slope s=dlog n/dlog M⋆≈−1.58 → shift **Δ=0.28 dex** erases it. z≃7–9 ≈13.6× (1.13 dex) → **Δ=0.44 dex** (photometric).

---

## M1 — Itemized stellar-mass systematic budget (replaces "~1 dex")

Each entry is an **independent physical axis** driving downward revision of M⋆ for z≈4–6 massive JWST galaxies. Decomposition, NOT the code-to-code spread plus its own drivers (avoids the double-count in "SED codes disagree ~1 dex," which already *contains* IMF/SPS/SFH).

| # | Source of M⋆ systematic | central (dex) | plausible range | citation (grounded) |
|---|--------------------------|:---:|:---:|---|
| 1 | IMF choice (Chabrier → top-heavy at high-z) | 0.30 | 0.1–1.0 | Lapi+2024 (2024Univ...10..141L); Steinhardt+2023 |
| 2 | SFH prior / outshining (parametric vs nonparametric) | 0.30 | 0.2–0.5 | Harvey+2025 EPOCHS IV (2025ApJ...978...89H) |
| 3 | SPS model + nebular continuum (BC03 vs BPASS, neb. treatment) | 0.20 | 0.1–0.3 | Choe+2026 (2026A&A...707A..29C); Cochrane+2025 (2025ApJ...978L..42C) |
| 4 | Dust–age–metallicity degeneracy | 0.15 | 0.1–0.25 | Choe+2026 |
| 5 | AGN / "Little Red Dot" host contamination (population-averaged) | 0.20 | 0.1–1.0* | Zhuang+2026 (2026ApJ...999...31Z); Kocevski+2025 (2025ApJ...986..126K) |
| 6 | Eddington bias (steep MF × mass-error convolution) | 0.15 | 0.1–0.25 | Adams+2023; Grazian+2015 (steep-MF deconvolution) |

*Per-object LRD contamination can reach orders of magnitude, but only a fraction of the massive sample are LRDs → population budget ~0.2 dex.

**Totals**
- **Quadrature (realistic, independent):** √(0.30²+0.30²+0.20²+0.15²+0.20²+0.15²) = **0.55 dex**
- **Linear (fully-correlated worst case):** 0.30+0.30+0.20+0.15+0.20+0.15 = **1.30 dex**  ← this is the "~1 dex" the paper cites; it is the *worst-case*, not the realistic budget.
- **IMF-excluded quadrature** (drop the contested top-heavy-IMF term #1): √(0.30²+0.20²+0.15²+0.20²+0.15²) = **0.46 dex**

**Does the itemized budget reach the required shift?**
- z≃5–6 needs **0.28 dex**: covered by the realistic quadrature (0.55 dex, ~0.5× budget) AND even by the IMF-excluded budget (0.46 dex). → **robust; does not depend on a top-heavy IMF.**
- z≃7–9 needs **0.44 dex**: ≈ the IMF-excluded budget (0.46 dex) and 0.8× the full quadrature (0.55 dex). → **marginal** — within budget only if the IMF term or photometric-mass downward revision is invoked; not robust.
- Spectroscopic quiescent z>6 (~2 dex, needs ≥1.4 dex): exceeds even the 1.30 dex linear worst case. → **genuinely outside budget; correctly flagged unresolved.**

---

## M3 — ΛCDM ceiling benchmark (ε = M⋆/(f_b·M_halo))

Abundance-matched (1:1, giving the **maximum** ε — most conservative test) via a self-contained Sheth-Tormen HMF + EH98 no-wiggle transfer function (`c2_goru_epsilon.py`, run captured). Planck: Ω_m=0.3089, Ω_b=0.0486, h=0.6774, σ8=0.816, **f_b=0.157**. HMF sanity: n(>10¹²,z=5)=3.0×10⁻⁵ Mpc⁻³ ✓ self-consistent with the match.

- Abundance match z=5, n=3×10⁻⁵ Mpc⁻³ → **M_halo = 1.0×10¹² M⊙ (log=12.00)**; f_b·M_halo = 1.58×10¹¹ M⊙ (max baryon budget).
- **ε_unshifted** (M⋆=10^10.50) = **0.200**  ← lands *exactly* on the fiducial ΛCDM SFE ε≈0.2 the paper cites, well under the Boylan-Kolchin (2023) hard bound ε≤1.
- **ε_shifted** (M⋆=10^10.22, after −0.28 dex) = **0.105**.

**Key finding:** the observed z≈5 abundance is ΛCDM-consistent (ε=0.20) with **NO shift at all**. The 0.28 dex shift is only needed to match *TNG's specific SMF*, not to be physically possible in ΛCDM. The paper under-uses its strongest number.

---

## Falsification thresholds (two distinct — writer must not conflate)

1. **Abundance-vs-TNG (Kun M2, from Table 1):** the z≃5–6 null reverts to a *tension* if the true mass-systematic budget is **< 0.28 dex**; z≃7–9 reverts if budget **< 0.44 dex**. Itemized budget (0.46–0.55 dex) clears the first with margin, the second only barely.
2. **ΛCDM physical-impossibility (Goru M3, the hard bound):** ε breaches 1 only if the true M⋆ are **+0.70 dex HIGHER** than the reported 10^10.5 (i.e. M_halo abundance-match fails). The reported abundance is nowhere near physically impossible — it would take a +0.70 dex *upward* mass error, opposite in sign and 2.5× larger than any plausible budget, to break ΛCDM.

---

## VERDICT — the null SURVIVES; it does not collapse to a tension (for z≃5–6)

Itemization + benchmarking **strengthen** #4 rather than sink it. The z≈5–6 headline null is real and now falsifiable: the required 0.28 dex shift is only ~half the realistic quadrature budget (0.55 dex) and is covered even without invoking a top-heavy IMF (0.46 dex), while the ΛCDM stress-test is passed outright — the *unshifted* abundance implies ε=0.20, exactly the fiducial ΛCDM efficiency, and reaching the ε=1 ceiling would require masses 0.70 dex *higher*, not lower. The honest corrections are two demotions, not a collapse: (i) the "~1 dex" figure is the linear worst case — quote the **realistic 0.55 dex quadrature** (or 0.46 dex IMF-excluded) as the committed budget; (ii) the z≈7–9 point (needs 0.44 dex ≈ the IMF-excluded budget) is **within budget but not robust** and must be labelled marginal/photometric, not lumped with the secure z≈5–6 result. The spectroscopic quiescent ~2 dex excess stays correctly outside budget.

**Numbers to drop into the manuscript:**
- Committed budget: **0.55 dex (realistic quadrature)**; 0.46 dex without the contested IMF term; 1.30 dex linear worst case.
- z≃5–6 requires 0.28 dex = **0.51× the quadrature budget** → consistent (IMF-independent).
- z≃7–9 requires 0.44 dex = **0.80× the quadrature budget** → within budget but marginal/photometric.
- ε(z=5): unshifted **0.20**, shifted **0.105**; M_halo=1.0×10¹² M⊙; f_b=0.157.
- Falsification: revives as tension if budget <0.28 dex (z5–6) / <0.44 dex (z7–9); ΛCDM broken only if M⋆ are **+0.70 dex** higher (ε>1).

Script: `c2_goru_epsilon.py` (RUNDIR). Method assumptions: Sheth-Tormen f(σ) with EH98 no-wiggle T(k); 1:1 abundance match (upper bound on ε); n_obs treated as comoving no-h Mpc⁻³ per Weibel+2024. A Tinker-2008 HMF would shift M_halo by ≲0.05 dex (ε by ≲0.03) — immaterial to the verdict.
