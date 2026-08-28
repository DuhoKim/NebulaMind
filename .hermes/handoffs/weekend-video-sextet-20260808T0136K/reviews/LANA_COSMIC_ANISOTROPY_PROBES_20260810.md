# LANA — cosmic anisotropy beyond galaxy spin: per-probe science frame (scope only)

Per `HWAO_COSMIC_ANISOTROPY_OVERNIGHT_ORDER_20260810T2340K.md` (`fa5be56d…`). I go first and set the frame.
Filed **2026-08-10 23:57 KST**. **Scope only — no run, no result, no claim, no video, no publication;
public data only, no new labelling; believe existing systematics papers.** NOT_WORTH_DOING_YET and
INCONCLUSIVE are successful outcomes. This is a **separate** study from spin — it contaminates nothing;
the spin freeze, blockers, and method-only video all stand, and none of these probes is a BHU test (Step 1
governs: a dipole is degenerate across many models, so a detection would not confirm BHU and a null would
not kill it; BHU is a labelled personal-interest footnote or absent).

## The frame — the one question that decides everything
Spin died on an **unmeasurable prior**: a classifier can pass the mirror self-test and still carry a
sky-position bias that no public field lets you measure out. So the test per probe is **not** "is there an
anisotropy claim" but: **is the dominant systematic MEASURABLE from public data, or is it an unmeasurable
prior like the spin classifier's?** That distinction is the whole order. None of these five probes requires
morphology classification, so the *specific* failure mode that killed spin is absent — but that is a reason
to expect a different outcome, not to assume one.

## Verdict up front
**One probe clears the bar: the quasar / radio number-count dipole.** Its dominant systematic (ecliptic-
latitude selection, flux calibration, masking, multipole leakage) is **measurable from the public data**,
it tests a **specific falsifiable null** (the CMB-kinematic amplitude), and the live dispute is being fought
*on those measurable systematics*. The other four are weaker: parity-violation's significance rests on
mock-covariance fidelity (an unmeasurable-prior-like assumption — closest to the spin trap); SN Ia/H0
directional signals are degenerate with local bulk flow (the mundane cause); GRB anisotropy vanishes once
the known sky-exposure function is applied. **Recommend a design brief for the quasar dipole only.**

---

## Probe 1 — Quasar / radio number-count dipole  ·  **RECOMMENDED**
**Claimed, by whom, significance (verbatim primary).** Secrest, von Hausegger, Rameez, Mohayaee, Sarkar
et al., *A Test of the Cosmological Principle with Quasars*, ApJL **908**, L51 (2021), arXiv:2009.14826, on
1.36 million CatWISE2020 quasars: *"While the direction of the dipole in the quasar sky is similar to that
of the cosmic microwave background (CMB), its amplitude is over twice as large as expected, rejecting the
canonical, exclusively kinematic interpretation of the CMB dipole with a p-value of 5×10⁻⁷ (4.9σ for a
normal distribution, one-sided), the highest significance achieved to date in such studies. Our results are
in conflict with the cosmological principle."* Follow-ups report ~4.4σ (2022) and radio+IR combined ~5.1σ.
**Amplitude vs CMB-kinematic prediction: over twice the expected value.**
**How contested (live dispute).** Disputed on **measurable** grounds: Abghari et al. (2024) argue an
ecliptic-latitude selection bias in the CatWISE sample implies comparable power in other multipoles, which
if present **reduces the significance**; others flag theoretical systematics in the velocity estimate and
Bayesian reanalyses of the number-count dipole. The dispute is precisely about measurable selection power.
**Public data.** CatWISE2020 (IR quasars); NVSS / RACS / other radio continuum surveys for the radio dipole.
**Dominant systematic.** Selection/instrumental: ecliptic-latitude coverage, flux-limit/photometric
calibration, source evolution and clustering (the "kinematic vs intrinsic" split), masking.
**Measurable from public data? YES.** Ecliptic structure, multipole power, flux limits and masks are all in
the public catalogues, and the leading counter-claim (Abghari) is itself a *measured* systematic argument.
This is the decisive contrast with spin: **whichever way it resolves, it resolves from public data.**
**Degeneracy flag.** The *test* is sharp — it rejects a **specific, falsifiable null** (the CMB-kinematic
amplitude), unlike spin's unpredicted null. But the **origin** of a confirmed excess is degenerate
(genuine large-scale anisotropy vs a local supervoid/bulk-flow vs residual selection). So a detection may
reject the kinematic null **without** attributing the excess.
**Detection entitled to say:** *"the number-count dipole amplitude exceeds the CMB-kinematic prediction at
Xσ after controlling ecliptic-latitude selection, flux limits, masking and multipole leakage — the
exclusively-kinematic interpretation is rejected."* **Not** entitled to: "the universe is anisotropic," "the
cosmological principle is refuted," any single-model attribution (BHU included), or "the excess is
intrinsic" (degenerate with local structure/systematics).
**Null entitled to say:** *"the dipole is consistent with the CMB-kinematic expectation within [sensitivity],"*
or *"the reported excess is accounted for by [measured systematic, e.g. ecliptic-latitude selection]."*
Either is a **real, publishable resolution** — the strength spin never had.

## Probe 2 — Cosmological parity violation from the galaxy 4-point function  ·  weakest / closest to the spin trap
**Claimed (verbatim primary).** Philcox, *Probing Parity-Violation with the Four-Point Correlation Function
of BOSS Galaxies*, PRD **106**, 063501 (2022), arXiv:2206.04227: a **blind** test on BOSS CMASS gives *"a
detection probability of 99.6% (2.9σ). This provides significant evidence for parity-violation, either from
cosmological sources or systematics."* Hou, Slepian & Cahn (2022) report a higher significance (~7σ) with a
different covariance.
**Author's own caveat (verbatim).** *"we cannot exclude the possibility that our detection is caused by the
simulations not faithfully representing the statistical properties of the BOSS data."*
**How contested.** The significance depends **entirely on the mock covariance**; 2024 reassessments
(Krolewski et al. and related) find **no robust evidence** once the covariance and look-elsewhere issues
are handled. **The significance itself is the dispute.**
**Dominant systematic.** The covariance matrix estimated from mock catalogues — a **modelling assumption**,
only partly testable (alternative mocks, analytic covariance, jackknife) and with an irreducible "do the
mocks represent the data" component. **This is unmeasurable-prior-like — the closest of the five to the
spin classifier's fatal flaw.**
**Degeneracy flag: HIGH.** A detection is degenerate (early-universe parity violation vs systematics), and
the significance is fragile. **Detection entitled to:** at most *"a parity-odd 4PCF signal at Xσ,
conditional on the assumed covariance; consistent with early-universe parity violation OR covariance
misestimation, not distinguished."* **Null:** *"no significant parity-odd signal under [covariance];
does not exclude early-universe parity violation (amplitude unpredicted)."*

## Probe 3 — SN Ia anisotropy / directional H0  ·  degenerate with local bulk flow
**Claimed / contested (search-level; a brief must pull verbatim).** Some directional Hubble-diagram
analyses report a statistically significant dipolar H0 variation (>1.5 km s⁻¹ Mpc⁻¹ in 0.023<z<0.15);
multiple analyses find **no excess** bulk flow beyond ΛCDM once peculiar-velocity correlations are in the
covariance — inferred bulk-flow speeds (~100–400 km s⁻¹) are all ΛCDM-consistent.
**Public data.** Pantheon+ and other public SN Ia compilations.
**Dominant systematic.** Local peculiar velocities / bulk flow (the mundane, expected cause), calibration,
sky-coverage selection.
**Measurable from public data? Largely yes** (the peculiar-velocity covariance is computable) — **but the
signal is weak and degenerate with the bulk flow it must be separated from.**
**Degeneracy flag: HIGH** — directional H0 ≈ local bulk flow, which is expected in ΛCDM. **Detection
entitled to:** *"a directional H0 variation at Xσ, degenerate with local bulk flow; a cosmological
interpretation is not entitled without excluding the local flow."* **Null:** *"consistent with isotropic H0
within ΛCDM bulk-flow expectation."*

## Probe 4 — GRB angular anisotropy  ·  resolves toward isotropy once exposure is applied
**Claimed / contested (search-level).** Historical claims of large GRB structures / short-GRB anisotropy;
BATSE found the distribution isotropic within errors, and recent BATSE+Fermi GBM dipole/quadrupole analyses
show the apparent quadrupole **vanishes after the sky-exposure function is applied** — deviations are
consistent with instrumental exposure, not cosmology.
**Public data.** BATSE, Fermi GBM, Swift catalogues.
**Dominant systematic.** Non-uniform **sky-exposure / instrumental selection** — **measurable and already
corrected for** in the literature.
**Degeneracy flag / status.** The systematic is measurable, but once applied the signal is **gone** — this
is closer to a **settled-toward-isotropy** question than a live dispute with a robust claim. **Detection:**
would need to survive exposure correction, which historically it does not. **Null:** *"isotropic after
exposure correction."* Low value for a new brief.

## Probe 5 — H0 directional variation
Effectively the same measurement and degeneracy as Probe 3 (directional H0 from SN Ia peculiar velocities);
degenerate with local bulk flow, largely ΛCDM-consistent after correction. Not separately recommended.

---

## Recommendation
**One probe is worth a design brief: the quasar / radio number-count dipole (Probe 1).** It is the only one
whose dominant systematic is **measurable from public data** — the exact property spin lacked — it tests a
**specific falsifiable null** (the CMB-kinematic amplitude, ~2× exceeded at ~4.9–5σ), the dispute is a live,
high-significance one fought on those measurable systematics (Secrest et al. vs Abghari et al.), it uses
public data (CatWISE, NVSS/RACS), and it involves **no morphology classification** — the spin failure mode
is entirely absent. Crucially, **either outcome is a real, publishable resolution from public data**: a
confirmed excess (kinematic null rejected) or a demonstration that a measured selection systematic accounts
for it. That is the opposite of spin's unresolvable dead end.

**The one caveat any brief must carry:** the *test* is sharp but a confirmed excess's *origin* is degenerate
(anisotropy vs local structure vs systematics), so a detection is entitled only to "the kinematic
interpretation is rejected," never to "the cosmological principle is refuted" or any model attribution
(BHU included). The design brief's core is the **systematics reanalysis** (ecliptic-latitude selection,
flux/photometric calibration, masking, multipole leakage, and the radio/IR cross-check on independent
instruments and footprints) — believing and building on Secrest et al. and Abghari et al. rather than
re-deriving them.

**On the other four:** parity-violation (significance-fragile, mock-covariance is an unmeasurable-prior-like
assumption — closest to the spin trap), SN Ia/H0 (degenerate with local bulk flow), GRB (resolves to
isotropy once exposure is applied). I do **not** recommend a brief for any of these now; each would more
likely land at NOT_WORTH_DOING_YET.

## Scope disposition
Scope only; no run, no data, no result asserted; nothing unblocks any lane. This sets the science frame and
the per-probe claim boundaries for the other seats, who would draft the systematics design brief for the
quasar dipole if Duho proceeds. The two flagged probes are verbatim-primary; Probes 3–5 are search-level and
must be pulled verbatim before any brief uses them. This is a separate study from spin and BHU; BHU stays a
labelled personal-interest footnote or absent. Relay submitted.