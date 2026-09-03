# Version-of-record check: entries 51 and 59

Line numbers below refer to the supplied clean-text files. The scope for entry 51 is the lane's `~10^16 kg` floor and density statement (`b11_entry51_measurement.py:39-51,56-57`; `b13_floor_routes.py:73-84,91-96,108-129,146-159`). The scope for entry 59 is the claims and quotations collected in `CANDIDATE_SD2016_RECONCILIATION_20260902.md:13-32`.

## Entry 51 — Popławski, Phys. Lett. B 690 (2010) 73; erratum PLB 727 (2013) 575

### 1. What the erratum corrects (verbatim)

The standalone erratum identifies itself as an erratum to the 2010 article (`poplawski_2013_plb727_575_update_clean.txt:12-16`) and gives these four corrections verbatim:

> The second sentence below Eq. (21) should begin with “For this conﬁguration located at the origin, Θ ik is proportional to δ(r)”.
>
> The sentence below Eq. (26) should begin with “For a point particle located at the origin”.
>
> The line above Eq. (29) should have (x1 = r , x2 = φ, x3 = z).
>
> Eq. (29) should be
> M αi j ∝ ∫ δ xα v i j δ(r − a)δ( z)r dr dφ dz. (1)

Receipt: `poplawski_2013_plb727_575_update_clean.txt:29-34`. The update appended to the supplied VoR reproduces the same four corrections (`poplawski_2010_plb690_73_vor_with_update_clean.txt:450-472`). Thus the erratum changes statements/formulae concerning the configurations and integration coordinates/measure around Eqs. (21), (26), and (29), not the later density or minimum-black-hole-mass passage (correction list: standalone erratum lines 29-34; appended update lines 467-472).

### 2. Lane-cited numbers and statements across the three records

**Cartan-density statement.** The arXiv pin says that the electron Cartan density is `~10^51 kg m^-3` and “approximately gives the order of the maximum density of ordinary matter composed of quarks and leptons” (`0910.1181_clean.txt:359`); it immediately explains that such a system cannot be compressed above the component Cartan densities (`0910.1181_clean.txt:360-361`). The VoR says the same: `ρ_Ce ~ m_e/r_Ce^3 ~ 10^51 kg m^-3` approximately gives the maximum-density order (`poplawski_2010_plb690_73_vor_with_update_clean.txt:340-344`), followed by the same compression rationale (`poplawski_2010_plb690_73_vor_with_update_clean.txt:346-354`). The erratum contains only the four corrections quoted above (`poplawski_2013_plb727_575_update_clean.txt:29-34`) and supplies no replacement density statement or number.

**Black-hole density and `~10^16 kg` floor.** The arXiv pin states: “The mass density of a black hole also cannot exceed ρ_Ce, from which its minimum mass in the ECKS theory is ~10^16 kg,” and also gives `~10^43 GeV` (`0910.1181_clean.txt:368`); its LHC consequence follows on line 369. The VoR has the same density ceiling, minimum mass `~10^16 kg`, energy `~10^43 GeV`, and LHC consequence (`poplawski_2010_plb690_73_vor_with_update_clean.txt:391-397`). Again, the erratum's exhaustive correction text is confined to the four items at `poplawski_2013_plb727_575_update_clean.txt:29-34`, so it neither changes nor withdraws these claims.

**Result.** No number or statement cited by the lane differs between the arXiv pin and VoR, and the erratum does not address any of them. The clean files differ typographically/layout-wise, but the scoped scientific wording and values match in the paired receipts above.

### 3. Verdict

`VOR_MATCH` — the VoR preserves the lane-cited `~10^51 kg m^-3` density statement and `~10^16 kg` minimum mass, while the erratum corrects only unrelated configuration/coordinate/integration details around Eqs. (21), (26), and (29).

## Entry 59 — Desai & Popławski, Phys. Lett. B 755 (2016) 183

### 1. What the publication record changes

No separate erratum or correction is among the supplied entry-59 records. For every item quoted or summarized by the reconciliation, the VoR repeats the arXiv-pin content; the paired receipts below show the publication-level check. Consequently there is no verbatim correction text to report for entry 59.

### 2. Lane-cited numbers and statements across arXiv pin and VoR

**Assumed particle-production law and free coefficient.** The arXiv text says that a rigorous treatment should derive `K` from quantum field theory, then says “we assume that” `K = β(κε̃)^2`, with `β` dimensionless (`desai_poplawski_2016_plb755_183_clean.txt:120-130`). The VoR says the same (`desai_poplawski_2016_plb755_183_vor_clean.txt:120-130`). Both later state that `β` “ultimately should be derived from quantum gravity” (arXiv `desai_poplawski_2016_plb755_183_clean.txt:436-441`; VoR `desai_poplawski_2016_plb755_183_vor_clean.txt:416-420`).

**Chosen tuning, initial scale, and e-folds.** The arXiv pin gives `β_cr = 1/929.0915` (`desai_poplawski_2016_plb755_183_clean.txt:211-218`) and chooses `β = 1/929.25`, `a_0 = 10^-27 m` (`desai_poplawski_2016_plb755_183_clean.txt:263-269`); those values imply `1-β/β_cr ≈ 1.7×10^-4`. It reports about 60 e-folds (`desai_poplawski_2016_plb755_183_clean.txt:275-286`). The VoR gives the identical critical value (`desai_poplawski_2016_plb755_183_vor_clean.txt:191-200`), choices (`desai_poplawski_2016_plb755_183_vor_clean.txt:226-233`), and about-60 result (`desai_poplawski_2016_plb755_183_vor_clean.txt:237-246`; see also figure-caption lines 256-260). Both records also describe expansion entering radiation domination without reheating (arXiv `desai_poplawski_2016_plb755_183_clean.txt:173-177`; VoR `desai_poplawski_2016_plb755_183_vor_clean.txt:227-236`).

**Reconstruction is a mathematical surrogate, and torsion perturbations are deferred.** The arXiv pin calls reconstruction “only a mathematical technique” (`desai_poplawski_2016_plb755_183_clean.txt:88-96`), says quantized torsion-field perturbations are needed and will be addressed in a future publication (`desai_poplawski_2016_plb755_183_clean.txt:283-290`), and then says the scalar potential gives the same scale-factor dynamics (`desai_poplawski_2016_plb755_183_clean.txt:296-306`). The VoR preserves all three points: mathematical-technique qualification (`desai_poplawski_2016_plb755_183_vor_clean.txt:116-122`), needed/deferred torsion perturbations, and same-dynamics reconstruction (`desai_poplawski_2016_plb755_183_vor_clean.txt:300-311`).

**Table value and `N` range.** In the arXiv pin, Table I labels its column `β/β_cr`, pairs `0.965` with three bounces, and defines the table as bounce count versus that ratio (`desai_poplawski_2016_plb755_183_clean.txt:228-238`); the VoR does likewise (`desai_poplawski_2016_plb755_183_vor_clean.txt:168-182`). Thus `0.965` is not an `n_s` entry in either record. The arXiv text says usual `N` is 50–60, the lower limit can be 18, and it evaluates 18–60 (`desai_poplawski_2016_plb755_183_clean.txt:356-368`); the VoR matches (`desai_poplawski_2016_plb755_183_vor_clean.txt:348-361`).

**Observable values and the paper's comparison to Planck 2015.** The arXiv pin gives `n_s ≈ 0.96` for `N ≈ 20–25`, `n_s ≈ 0.99` for `N = 50–60`, and calls the latter about `6σ` from its quoted Planck 2015 fit (`desai_poplawski_2016_plb755_183_clean.txt:369-380`). It gives `r_0.05 < 0.12` as the comparison limit and running of order `10^-3` (`desai_poplawski_2016_plb755_183_clean.txt:381-393`), while its sensitivity discussion puts `r` at `0.01–0.03` and `|α_s|` at order `10^-3–10^-4` (`desai_poplawski_2016_plb755_183_clean.txt:424-433`). The VoR gives the same `n_s` values and about-`6σ` characterization (`desai_poplawski_2016_plb755_183_vor_clean.txt:362-371`), the same `r_0.05 < 0.12` and order-`10^-3` running statements (`desai_poplawski_2016_plb755_183_vor_clean.txt:343-353`), and the same `r = 0.01–0.03`, `|α_s| = O(10^-3–10^-4)` sensitivity results (`desai_poplawski_2016_plb755_183_vor_clean.txt:366-374`).

The reconciliation's comparisons against **Planck 2018** and its independently recomputed sigma values are later audit calculations, not statements in either 2015/2016 source; the reconciliation explicitly labels these as its “Numbers vs data” audit (`CANDIDATE_SD2016_RECONCILIATION_20260902.md:25-29`). They therefore cannot differ between the arXiv pin and VoR. The source-level inputs to that audit are unchanged, as the paired receipts above establish.

**Result.** No lane-cited source number or statement differs between the arXiv pin and VoR. Differences visible in the clean texts are publication typography, pagination, headings (`Table I` versus `Table 1`), and extraction/layout, not scientific content in scope (table receipts above; arXiv section labels at lines 99 and 397 versus VoR numbered headings at lines 124 and 356).

### 3. Verdict

`VOR_MATCH` — every source statement and number used by the reconciliation is preserved in the VoR, including the assumed production law, parameter choices, surrogate-only qualification, deferred torsion-spectrum calculation, scanned `N` range, and observable values.
