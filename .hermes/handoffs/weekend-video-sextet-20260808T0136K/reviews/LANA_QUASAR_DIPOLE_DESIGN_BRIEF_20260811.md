# DESIGN BRIEF — quasar/radio number-count dipole vs the CMB-kinematic expectation

Per `HWAO_QUASAR_DIPOLE_DESIGN_BRIEF_ORDER_20260811T0845K.md` (`26b6f295…`). Drafted by Lana; I own the
claim boundary. Filed **2026-08-11 10:02 KST**. **Brief only — no run, no result.** Three seats converged
on this probe (Kun, Lana, Goru). Kun's gate is binding: **every frozen item below is a value, a named
custody artifact, or an explicit "cannot be frozen from hand" finding — never a promise to freeze later.**
If any required item cannot be reduced to a value before the run, **the brief does not proceed and
NOT_WORTH_DOING_YET is the outcome.**

## The question, made sharp (why this and not spin)
Not "is there a dipole?" but: **does the number-count dipole amplitude exceed the specific, falsifiable
CMB-kinematic prediction, on ONE frozen catalogue / mask / flux-threshold ladder / selection correction,
computed once — and does the excess survive the published ecliptic-selection systematic?** The test can
fail (spin's could not), and its dominant systematics are published products, not unmeasurable priors. This
brief adjudicates the live Secrest et al. (excess) vs Abghari et al. (ecliptic bias) dispute with the
analyst freedom removed. Its worth-doing is **conditional** on the freeze being achievable (see §9).

---

## 1. Catalogue family — [FROZEN VALUE]
**CatWISE2020 quasars with the Secrest et al. selection** (the version Tori graded DOCUMENTED, "CatWISE
Secrest v3"), as **primary**; **NVSS** radio continuum as the **independent cross-check** (Tori DOCUMENTED,
with the exact masks and generation code). **Pantheon+ and Fermi are NOT admissible** — they failed Tori's
custody gate. No other catalogue enters. *Believe and build on the published products; do not re-derive.*
The exact versioned derived FITS and their sha256 are **bound by Tori's custody receipt at freeze** — this
names the specific existing files, it is not a choice deferred.

## 2. Sky mask — [TORI-CUSTODY VALUE — hash bound at freeze]
**The exact published Secrest mask FITS** that Tori graded DOCUMENTED (Galactic-plane cut and bright-source
/ high-density masking as distributed), applied identically to CatWISE and, in its own documented form, to
NVSS. One mask, adopted from the authors, not reconstructed. Tori binds the file + hash at freeze. **No
mask variant is tried after any amplitude is seen.**
- ⚠️ [FINDING] I do not hold the mask's exact parameter values verbatim; they must come from the
  Tori-documented FITS/header, **not** reconstructed from memory. If the published mask cannot be bound as a
  single versioned file, that is a §9 not-worth-doing trigger.

## 3. Flux-threshold ladder — [PARTIAL FROZEN VALUE + FINDING]
- **[FROZEN VALUE]** Rung 1 = the Secrest 2021 cut, verbatim from ApJL 908 L51: **`9 < W1 < 16.4`**.
- **[FINDING — carry verbatim, do not reconstruct]** Rung 2 = the deeper CatWISE cut of Secrest 2022; I do
  **not** hold its exact value from the abstract, so it must be **quoted verbatim from Secrest 2022 §[X]
  before freeze**. It may not be reconstructed or chosen by us.
- **[FROZEN PROTOCOL VALUE]** The ladder is exactly these published rungs, fixed in advance; **no rung is
  added, removed, or shifted after any amplitude is computed.** Choosing thresholds after seeing amplitudes
  is the classic manufactured-result route and is prohibited. If the deeper rung cannot be quoted verbatim,
  the ladder is Rung 1 only, stated as such.

## 4. Selection-function correction + named systematics maps — [FROZEN METHOD + FINDING on free parameters]
- **[FROZEN VALUE — method]** Apply the **published Secrest ecliptic-latitude selection correction**, and as
  a **mandatory pre-registered systematic**, the **Abghari et al. (2024) ecliptic-multipole diagnostic**
  (the leakage of ecliptic scan-pattern power into the dipole). Named systematics maps to be used, all
  public products: the CatWISE ecliptic scan-pattern density map; the flux-calibration / depth-gradient
  maps; the Galactic extinction and stellar-contamination maps.
- ⚠️ **[FINDING — the pivotal freeze risk]** If the correction carries a **free parameter chosen after
  seeing data** — e.g. the number of multipoles marginalized, or a data-tuned ecliptic template amplitude —
  then it **cannot be frozen in advance**, and per Kun this converts the analysis into another analyst
  choice in a contested field, adding nothing. In that case the honest answer is **NOT_WORTH_DOING_YET**.
  The correction is admissible **only** if every parameter is fixed by the published method or quoted
  verbatim; state each parameter's frozen value or declare the freeze failed.

## 5. Kinematic-dipole subtraction convention — [FROZEN CONVENTION + TORI-VERBATIM NULL]
- **[FROZEN VALUE — convention]** The expected kinematic dipole is the **Ellis & Baldwin (1984)** relation
  `D_kin = [2 + x(1+α)]·β`, where `β = v/c` from the CMB dipole velocity **v = 369.82 km s⁻¹** (Planck 2018;
  `β ≈ 1.2336×10⁻³`); `x` (integral source-count slope) and `α` (spectral index) are **taken verbatim from
  the sample's published values at the frozen threshold** — not fit by us.
- **[TORI-CUSTODY VERBATIM]** The **NVSS Monte-Carlo null convention** for the significance is carried
  **verbatim from the primary documentation Tori located** — quoted, **not reimplemented**. Tori supplies
  the exact quoted passage + source at freeze.
- ⚠️ [FINDING] I hold the Ellis-Baldwin form and the CMB velocity as values; I do **not** hold the sample
  `x, α` values or the NVSS MC passage verbatim — both must be carried from primary sources before freeze.

## 6. Decision rule — [FROZEN VALUES]
Computed once, on the frozen inputs above:
- **DETECTION** (kinematic null rejected): the excess `(D − D_kin)` is positive and, **after** the §4
  ecliptic correction, significant at **≥ 3σ** under the §5 frozen null, **AND** consistent in sign across
  every §3 ladder rung, **AND** the CatWISE and NVSS dipole directions agree within **15°**.
- **NULL** (consistent with kinematic): after the §4 correction, `(D − D_kin)` is consistent with zero
  within the §5 null — i.e. the ecliptic-multipole diagnostic accounts for the raw excess.
- **INCONCLUSIVE**: the §4 diagnostic accounts for **> 50%** but not all of the excess; **or** the ladder
  rungs disagree on detection/null; **or** CatWISE and NVSS directions disagree by **> 15°**.
(The 3σ, 50%, and 15° values are pre-registered here as values; they are not revised after any statistic.)

## 7. Execution protocol — [FROZEN VALUE]
**Computed once, fresh, separately receipted; no parameter revision after any statistic is seen.** Receipt
schema (all pinned): catalogue FITS + sha256; mask FITS + sha256; flux rung(s); correction code + sha256 +
each systematics map + sha256; kinematic convention (`x, α, β`, formula ref) + the verbatim NVSS-MC passage;
computed `D`, `D_kin`, `σ`, ecliptic-diagnostic fraction, cross-family direction separation; and the §6
decision. **Any post-hoc parameter change voids the run** (the discipline Kun blocked A2 for).

## 8. Claim boundary — [BINDING, verbatim, carried from my scope packet]
- **A DETECTION may say:** *"the number-count dipole amplitude exceeds the CMB-kinematic prediction at
  [significance], and an exclusively-kinematic interpretation is rejected."* It **may not** say "the
  universe is anisotropic," "the cosmological principle is refuted," or attribute the excess to any specific
  cause (intrinsic anisotropy, local structure, BHU, or any model). **The test is sharp; the origin of any
  excess is degenerate — that asymmetry is the whole discipline of this brief.**
- **A NULL may say:** *"the dipole is consistent with the CMB-kinematic expectation within [sensitivity],"*
  or *"the reported excess is accounted for by the [named] ecliptic-selection systematic."* It may not say
  "the universe is isotropic" or "the dispute is settled."
- **INCONCLUSIVE** is reported plainly and is a successful outcome. This is a separate study from spin/BHU;
  BHU is a labelled personal-interest footnote or absent.

## 9. What would make this NOT worth doing — [ANSWERED PLAINLY]
- **Already settled by the published analyses?** No. Secrest et al. (excess at ~4.9–5σ) vs Abghari et al.
  (ecliptic bias reduces it) is a **live, unresolved** dispute; the significance's dependence on the
  measurable ecliptic systematic is exactly what is open.
- **Would our version only reproduce them?** It adds value **only** as a *pre-registered adjudication* with
  the analyst freedom removed. Therefore the study is worth doing **if and only if every item in §§1–5 can
  be reduced to a value before the run** — the catalogue and mask bound by Tori, the flux ladder quoted
  verbatim, the correction free of any data-tuned parameter, and the kinematic/NVSS-MC conventions quoted
  verbatim. **If the §4 correction requires a parameter chosen after seeing data, or the deeper flux rung or
  the NVSS-MC convention cannot be quoted verbatim, then we would merely be adding one more analyst choice
  to a contested field — which adds nothing, and the honest outcome is NOT_WORTH_DOING_YET.** That
  conditional is the real finding of this brief, and it is Kun's gate to enforce.

## Disposition
Brief only; no run, no data acquisition, no result asserted; nothing unblocks any lane; nothing is accepted
without Duho. The frozen values are set; the three cannot-freeze-from-hand items (§2 mask parameters, §3
deeper rung, §5 sample `x,α` + NVSS-MC passage) are flagged as **must be quoted verbatim / bound by custody
before freeze, not reconstructed**, and the §4 free-parameter question is the pivotal go/no-go. Kun gates
the frozen brief before any number; Tori binds the catalogue/mask/convention custody; Goru builds from the
data side; my claim boundary governs any output. If the freeze cannot be completed as values,
NOT_WORTH_DOING_YET. Relay submitted.