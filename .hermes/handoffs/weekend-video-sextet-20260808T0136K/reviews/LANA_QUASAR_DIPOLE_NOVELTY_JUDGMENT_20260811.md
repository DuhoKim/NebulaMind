# LANA — the novelty question, answered before any v3

Per Duho: *"have lana answer the novelty question first."* Two seats raised it independently (Kun on v2: the
brief *"claims the control rather than freezing it"*; Tori's exact-artifact gate §F: FAIL_CLOSED,
NOT_WORTH_DOING_YET). Filed **2026-08-11 10:34 KST**. **No v3, no design, no run. Public data only. This
answers only the novelty question:** what does OUR quasar-dipole analysis *add* that the published work does
not already provide — not what it would confirm.

## Answer up front
**We would only reproduce published work more carefully. That is NOT_WORTH_DOING_YET.** The one framing with
genuine novelty (a cross-catalogue single-convention test) is exactly the one we cannot freeze on public data
under our own custody constraints. I am not manufacturing novelty to keep the line alive; per Duho, where a
paper has already studied a catalogue and its biases, we believe them and build on it — and here, they have.

---

## (1) What the published work has already established, and where the live dispute actually sits
**Established, from primary sources:**
- **The amplitude has been measured against the fixed CMB-kinematic (Ellis–Baldwin) null in both catalogues.**
  CatWISE: Secrest et al. 2021 — ~2× excess, same direction as CMB, 4.9σ; ~4.4σ (2022). Quaia: Mittal et al.
  2024 (Bayesian) — *"consistent with the CMB dipole, both in… amplitude and direction"* after excising
  selection-contaminated regions; Singal 2024 (same Quaia sample) — *"3–4 times as large as the CMB dipole."*
- **The selection-function residuals have been explicitly studied**, not ignored: Abghari et al. 2024 model
  ecliptic-scan-pattern leakage into the CatWISE dipole; Mittal et al. excise and model Quaia's Galactic-plane
  selection contamination. Tori's §F confirms a published Quaia analysis already compares against a fixed
  CMB-kinematic model **while studying selection-function residuals across multiple Galactic masks.**
- **The direction is not in dispute** in any analysis — only the amplitude, i.e. only how much of the raw
  signal is selection artifact.

**Where the dispute actually sits (Kun is right):** it is about **measurable selection power** (how much of
each catalogue's amplitude is scan-pattern / depth / masking artifact) and **catalogue dependence** (CatWISE
excess vs Quaia-Mittal consistency vs Quaia-Singal excess). **The gap is real** — the field genuinely does
not agree on how much amplitude survives selection correction.

**Is it ours to close?** To close it you must either (a) adjudicate *which* selection treatment is correct on
a single catalogue — but Mittal and Singal already occupy that space, and we can only add one more treatment,
which we moreover cannot pre-freeze (§2 of v2); or (b) run the clean cross-catalogue test in (2). Neither is
available to us on the admitted terms. **The gap is real but not ours to close now.**

## (2) The specific frozen control we could add — judged, candidate by candidate
Tori named three candidates. Judged as a scientist, not a tidier:

- **A — artifact/quality-flag sensitivity (Quaia lacks row-level warning bits, so use an external artifact
  map).** *Not novel in kind.* Testing the dipole's stability against scan-pattern / depth structure is
  exactly what Mittal's selection-residual study and Abghari's ecliptic-leakage diagnostic already do, by
  other instruments. An external-map version is **tidier, not a control the field lacks.** Duho's rule —
  believe the catalogue-bias papers and build on them — forecloses "redo the residual study more carefully"
  as a contribution.
- **B — coordinate-frame-explicit reanalysis (frame undocumented in header; notebook equatorial, briefs
  assume Galactic).** *Not novel — it is pipeline hygiene on OUR reproduction, not a gap in the science.*
  This is the same lesson as my own spin-provenance finding: **"unstated in the header" ≠ "unknown to the
  authors."** Mittal and Singal used the catalogue in its correct frame; a frame-explicit rerun only protects
  *us* from a sign/orientation bug. Getting it right is a precondition for not being wrong, not a new control.
- **C — cross-catalogue consistency test binding Quaia AND CatWISE under ONE frozen convention.** *This is the
  only candidate with a genuine novel core.* The published landscape measures CatWISE (Secrest, Abghari) and
  Quaia (Mittal, Singal) **separately, each with its own mask semantics, coordinate frame, kinematic-null
  construction, and x/α** — so the CatWISE-vs-Quaia amplitude difference is **confounded**: you cannot tell
  whether it is **catalogue-dependent** (real, instrument/selection) or **convention-dependent** (an artifact
  of each group's analysis choices). A single frozen downstream convention across both catalogues would
  **disentangle catalogue-dependence from convention-dependence** — and that the published record genuinely
  lacks.
  **But it is not freezable, for two reasons the crew has already established:**
  (i) **CatWISE is only DOCUMENTED_CONDITIONAL_RECONSTRUCTION (Tori).** We cannot bind it to a single custody
  value, so it cannot enter "one frozen convention" as a value — the test fails custody on the CatWISE side.
  (ii) **The selection-correction step — the actual crux of the dispute — is irreducibly catalogue-specific.**
  You cannot apply Quaia's selection function to CatWISE or vice-versa; each catalogue's selection model is
  intrinsic to it. So "one frozen convention" can only cover the *downstream* steps (mask semantics beyond
  selection, frame, Ellis–Baldwin construction, significance rule) and **leaves the disputed step untouched.**
  The novel core disentangles everything *except* the one thing in dispute.

## (3) The plain answer
**On public data, under our custody and no-new-labelling constraints, we would only reproduce published work
more carefully.** A (tidier residual study) and B (frame hygiene) are not new controls; Duho's believe-and-
build rule forecloses them. C has a real novel core but cannot be frozen — CatWISE fails custody, and the
disputed selection step cannot be unified across catalogues. **So the honest outcome is NOT_WORTH_DOING_YET,
FAIL_CLOSED — concordant with Tori's §F and with Kun's "not gateable as drafted."** This is the fourth time
in two days we have taken this answer; it has cost nothing and saved four bad studies. The probe as a *whole*
is not dead science (Kun) — but *our* marginal contribution, on these terms, is not novel, and that is the
question I was asked.

**The single, precise condition that would flip it** (so the record is reversible, not a vague punt): a
**custody-grade CatWISE derived product** bound as a value **plus** a defensible way to place both catalogues
under one convention **without** unifying the irreducibly catalogue-specific selection step. Absent both,
NOT_WORTH_DOING_YET stands. That is Tori's custody call and Goru's data call to make, not mine to assume.

## (4) If it were novel — the boundary (unchanged, for the record)
It is not, so this does not license a run. Stated only so nothing drifts: my claim boundary is unchanged —
a detection may say *"the number-count dipole amplitude exceeds the CMB-kinematic prediction at
[significance], and an exclusively-kinematic interpretation is rejected,"* never that the universe is
anisotropic or why; a null may say *"consistent with the CMB-kinematic expectation within [sensitivity]."*

## Disposition
Novelty question answered: **NOT_WORTH_DOING_YET** — we would reproduce published work more carefully; the one
genuinely novel framing (cross-catalogue single-convention disentangling) is un-freezable on our terms. No
v3, no design, no run. Nothing unblocks any lane; nothing accepted without Duho. Relay submitted.
