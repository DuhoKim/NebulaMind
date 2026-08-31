# RQ-C derivation brief — the Gaztañaga causal-horizon cutoff (BHU Lane 2, task 3)

**From:** Tori · **To:** codex + agy (independent, blind-double) · **2026-08-31** (overnight build)
**Boundary:** derive the number + a falsification verdict. **Do NOT re-tier entries 25/26/54** — the
tier move is Duho's. Published-base-layer, receipts discipline, lane-dir only. **Burn:** you (codex
0% / agy 2.5%) carry the load; do the heavy work yourselves.

## The one-sentence task

Gaztañaga's BHU predicts a **cut-off in the primordial power spectrum at the causal-horizon scale R**
(the finite FLRW-cloud size, tied to the black-hole radius r_S = 2GM), and ties the CMB **low-ℓ
deficit / large-angle anomalies** to it. **Decide whether that cutoff scale can be fixed FROM FIRST
PRINCIPLES — independently of the low-ℓ CMB deficit it is invoked to explain — and if so, whether the
predicted cutoff is consistent with, or refuted by, the Planck large-scale power spectrum.**

## What Gaztañaga claims (verbatim anchors — verify + extend from the sources)

- **The cutoff (Part II, `sym14101984_clean.txt:1010`):** *"Because R is always finite, we expect a
  cut-off in the spectrum of perturbations. This is at odds with the simplest prediction of
  Inflation. Recent anomalies … over very large super-horizon scales agree better with the BHU
  predictions than with Inflation."*
- **The horizon→angle→anomaly tie (Part I, `sym14091849_clean.txt:3116–3126`):** *"We can observe
  transverse perturbations in the CMB that are larger than R. At the time of CMB last scattering, R
  corresponds to an angle [θ] deg. Such super-horizon scales could be related to the so-called CMB
  anomalies."* (Extract the actual θ and the R↔r_S relation.)
- **The quantitative parent paper (cited in Part I refs):** **Fosalba & Gaztañaga 2021, "Explaining
  cosmological anisotropy: Evidence for causal horizons from CMB data," MNRAS 504, 5840** (arXiv
  free — acquire if you need the quantitative cutoff/ℓ_cut; pin it if you pull it). This is where the
  causal-horizon-from-CMB number lives.

## The crux (this decides falsifier vs. not — memo overclaim-pattern 1)

**Is the cutoff scale R (equivalently k_cut, or ℓ_cut at last scattering) PREDICTED or FITTED?**
- **PREDICTED** = R is fixed a priori from BHU parameters (r_S = 2GM, i.e. the present horizon /
  H_0 / the matter density) WITHOUT reference to the observed low-ℓ deficit → the cutoff multipole
  ℓ_cut is a genuine number the CMB must show. Then RQ-C yields a **candidate CMB calibrated
  falsifier**: Planck's large-scale C_ℓ either shows suppression at ℓ_cut or refutes it.
- **FITTED** = R (or ℓ_cut) is chosen/tuned to match the observed quadrupole/low-ℓ deficit → it
  "explains but does not predict" → **not a falsifier**; the claim reclassifies to a directional
  consistency statement.
- Decide this from the sources: does Gaztañaga *derive* R from r_S/H_0 independently, or *read it off*
  the anomaly? Quote the step that fixes R.

## Deliverable (`RQ_C_<seat>_RESULT.md`)

1. **R and ℓ_cut, derived.** From the sources, give R (in Mpc), the relation R ↔ r_S = 2GM ↔ present
   horizon/H_0, and the corresponding **ℓ_cut** (multipole at last scattering, R↔angle↔ℓ). Show the
   step that fixes R and state whether it uses the low-ℓ data or not.
2. **Compare to Planck's large-scale spectrum.** Use **published Planck low-ℓ values** (the observed
   quadrupole C_2 and the well-known low-ℓ / large-angle deficit, e.g. Planck 2018 results I/VI) —
   NOT a full likelihood re-run. Does the observed suppression sit at the predicted ℓ_cut? Quantify
   the agreement/tension (roughly — order-of-ℓ is enough for the verdict).
3. **VERDICT (first line, one token):**
   - `CMB_FALSIFIER_CANDIDATE` — ℓ_cut is fixed a priori AND Planck's large-scale spectrum tests it
     (consistent or in tension — say which). A number + a threshold.
   - `FITTED_NOT_PREDICTED` — R/ℓ_cut is tuned to the anomaly it explains → not a falsifier.
   - `UNDETERMINED_NEEDS_<resource>` — you cannot fix R independently from the pinned sources without
     a specific gated resource (name it: a paper, a Planck likelihood product, a code). Then STOP and
     say exactly what is needed — do NOT fabricate a cutoff.
4. **Ownership-of-proof + receipts:** every number greppable in a pinned source; if you pull
   Fosalba-Gaztañaga from arXiv, pin it. State every assumption (which horizon definition for R,
   last-scattering geometry for ℓ_cut).

## If the data-engineering is genuinely gated

Per Duho: if fixing R independently, or the Planck comparison, needs a **genuinely gated resource**
(a paywalled dataset, a likelihood product you cannot obtain, a non-free code), do NOT grind — write
the blocker into your result as `UNDETERMINED_NEEDS_<resource>` with exactly what is missing. Tori
lifts it to OPEN_QUESTIONS and the tick catches it. The *crux* (predicted vs fitted) is mostly
analytic and should be answerable from the Gaztañaga papers + Fosalba-Gaztañaga alone.

**Blind-double:** codex and agy derive independently; do not read each other's result. Tori
reconciles: agreement on PREDICTED-vs-FITTED is the load-bearing thing; a split there is a
seats-disagree item for Duho.
