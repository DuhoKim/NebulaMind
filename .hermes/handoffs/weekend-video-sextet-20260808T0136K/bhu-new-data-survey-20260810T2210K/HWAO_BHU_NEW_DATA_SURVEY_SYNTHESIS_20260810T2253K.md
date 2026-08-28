# BHU new-data survey — synthesis

Marker: `HWAO_BHU_NEW_DATA_SURVEY_SYNTHESIS_20260810T2253K`
Filed 2026-08-10 23:0x KST against `TORI_TO_HWAO_BHU_SYNTHESIS_REQUEST_20260810T2253K`.

**Authorship, stated plainly because this file carries an `HWAO_` name.** Written by the
**Claude-macbook seat** (Directors board, pane %30) on Duho's direct instruction to execute Tori's
bounded synthesis request. **Hwao did not author it.** The filename follows the one Tori suggested so
the crew finds it where expected; the authorship claim is this paragraph, not the filename. An
artifact's self-description is not evidence about the artifact
(`HWAO_RULING_SELF_DESCRIPTION_20260809T1800K.md`), so it is said here rather than implied.

Inputs read in full: the governing order `HWAO_BHU_NEW_DATA_SURVEY_ORDER_20260810T2210K.md`; Lana's
Step 1; the Hwao/Goru preliminary inventory; Kun's adversarial packet; Tori's provenance gate; and
`EVIDENCE_QUOTES.md` + `citation-ledger.json`.

---

## Verdict

**`NEW_PUBLIC_DATA_EXISTS_BUT_NO_READY_BHU_DISCRIMINATOR_UNDER_CURRENT_CONSTRAINTS`**

No primary-source contradiction was found that would displace it. The verdict is adopted from Tori's
gate and independently consistent with Lana's Step 1 and Kun's adversarial pass — three seats
reaching it from theory, from adversarial design, and from provenance respectively.

## Framing — carried, not summarised

**Black-hole-universe cosmology is Duho's standing personal research interest, not a ranked frontier
in this corpus. It is his project, not a disqualifier — but an output implying mainstream priority
would misrepresent the field, and that is the one way this survey can fail dishonestly.**

That sentence is the survey's own condition of honesty, set in the order before any seat reported,
and it holds unchanged after all four reported.

---

## The question the survey actually answered

"Is there new data?" is unanswerable until "what would count as evidence?" is settled. Run in that
order, the survey produces a two-part answer, and the parts point opposite ways:

**Yes, there is substantially new public data.** DESI DR1 — *"Public Data Release 1 (DR1) was
publicly released July 1, 2025"* — plus Galaxy Zoo DECaLS and DESI (8.7M galaxies, 29 detailed
morphology measurements), Euclid Q1, SDSS DR17/18, Rubin DP1/EDP2, Planck final, ACT DR6, SPT-3G D1.
Every one postdates Galaxy Zoo 1. The premise of Duho's question is correct.

**No, none of it supplies the observable.** Not one of these products publishes a frozen, signed,
documented **handedness** field. The gap is not scale, coverage or recency — all improved. It is that
the specific quantity a spin-parity study needs is absent from the outputs.

## The four findings that produce that answer

**1. Lana — no uniquely-BHU observable survives primary sources.** BHU's predictions are either
non-distinguishing (a closed, nonsingular universe, consistent with data and with many other models)
or qualitative and degenerate. The strongest primary statement is conditional: *"The preferred axis of
the parent black hole **may** have been inherited by the daughter universe"* (Popławski,
arXiv:1910.10819). A preferred axis with **no predicted amplitude** is not sharply falsifiable, and
its signature is shared with primordial parity violation from inflation, rotating Gödel-type and
anisotropic Bianchi cosmologies, and residual classification systematics. **A detection would not
uniquely confirm BHU; a null would not kill it.**

**2. Goru/inventory — the data era genuinely changed.** New instruments, new footprints, new
morphology pipelines, new spectroscopy. This is why the question was worth asking rather than
assuming 2008's answer.

**3. Kun — adversarial, and one qualification is binding.** Duho's data-era hypothesis was that a
classifier *we* run can be bias-controlled by construction: feed an image and its mirror, require
handedness to flip. Kun's limit on that: **"we control the classifier" is only partly true.** A
public catalogue like Galaxy Zoo DESI is *a prediction of what volunteers would say*, so a model
trained on human labels can reimport the very bias being controlled for. Owning the pipeline means
owning weights, preprocessing and mirrored-image generation — not downloading a column.

**4. Tori — provenance, applied per candidate.** The gate that decides admissibility, and the one
that would have saved the last four days.

## Mandatory corrections, carried verbatim in substance with sources

These correct plausible-sounding assumptions that would each have produced a wrong study design.

| # | Correction | Primary source |
|---|---|---|
| 1 | Galaxy Zoo DECaLS/DESI **`spiral-winding` is arm tightness** (tight/medium/loose), **not** clockwise/counterclockwise. Neither catalogue publishes handedness. | GZ DECaLS schema; GZ DESI paper |
| 2 | The released DECaLS model trained with *"randomly horizontally and vertically flipped, and randomly rotated"* inputs. Mirror evaluation therefore **audits invariance but cannot recover a chirality target absent from the output tree**. | arXiv:2102.08414 |
| 3 | **DESI DR1 is the latest verified public release**; no public DR2 product was verified. | data.desi.lbl.gov |
| 4 | The claimed 0.8–1.3M-object DESI Legacy spin catalogue is **not downloadable** — page reads *"Download data (coming soon)"*, no frozen dictionary or checksum. | people.cs.ksu.edu spin page |
| 5 | **HSC DR3 is the one public modern spin catalogue found**, but its +1/−1 sign mapping is **not stated in the data dictionary**. Independent analysis already found decisive evidence for isotropy — believe and build on it rather than rerun it. | arXiv:2410.18884 |
| 6 | PA fields in Legacy/SDSS/Euclid are documented but **parity-blind**: `phi = arctan2(e2,e1)/2`, *"east of north"*, *"counter-clockwise from the x-axis"* — an unoriented axis mod 180°, not chirality. | Legacy DR10; Tractor; Euclid Q1 cookbook |

Correction 2 is the decisive one for Duho's hypothesis. The mirror test is sound in principle; the
released model was deliberately trained to be **blind to the thing being tested**.

## The honest prior already in the literature

Not mutually consistent, which is exactly why catalogue construction and statistical method are not
implementation details:

- Iye, Yagi & Fukumoto (2021): after cleaning duplicates, *"SDSS data alone does not support the
  presence of a large-scale symmetry-breaking in the spin vector distribution."*
- Patel & Desmond (2024/25), all public binary spin catalogues: *"All analysis indicate consistency
  with isotropy to within 3σ."*
- Stiskalek & Desmond (2024), HSC DR3: *"the Bayes factor indicates decisive evidence for the
  isotropic model."*
- Planck VII (2020): *"no unambiguous detections … of anomalies corresponding to those seen in
  temperature, are claimed"* in polarization.

**These do not prove BHU false.** They show the presently public, already-annotated spin data yield no
robust anisotropy detection under the strongest recent reanalyses, and that CMB anomalies remain mild
and non-unique.

## What can be leveraged now, and what cannot

**Yes — as evidence constraints:** cite the independent HSC DR3 isotropy result rather than repeating
it; cite Planck's own anomaly/systematics assessment; treat DESI DR1 spectroscopy as a documented
support catalogue for future joins; treat documented PA catalogues as orientation-alignment data
only, never as spin chirality.

**No — ready BHU-discriminating analysis.** No named catalogue simultaneously has (1) a public frozen
signed handedness field, (2) a primary documented sign/orientation mapping, (3) an independently
audited mirror response, (4) independent instrument/footprint leverage, and (5) a quantitative BHU
prediction forecasting differently from competing explanations. Item 5 fails on theory alone, before
any data question.

**Maybe, and not authorized here:** a public-data-only robustness join asking whether already-published
spin labels retain an isotropic result when matched to documented DESI DR1 spectroscopy. Existing
labels, no new labelling. That is a data-quality/redshift robustness study, **not a unique BHU test**,
and must not proceed until exact spin-sign provenance and an object-match manifest are frozen.

## Where the constructive path actually went

The survey's honest product is not a BHU test. It is the recognition — Lana's, developed in Kun's
and Tori's packets — that the observable people *associate* with BHU is more testable now than in
2008, as **large-scale isotropy/parity: a mainstream question with a live literature dispute** (Longo
dipole; Shamir asymmetry; Land et al. isotropy after bias correction).

Hwao scoped exactly that at 22:50 as its own frontier
(`HWAO_ISOTROPY_PARITY_SCOPE_ORDER_20260810T2245K.md`), with BHU appearing only as a labelled
personal-interest footnote or not at all. This synthesis endorses that separation: it is the outcome
that keeps Duho's interest alive as research while refusing to dress it as mainstream priority.

The GZ1 failure looks like **data-era bookkeeping rather than physics** — a bias control that could
not be built from the archive's fields. That remains plausible and unproven. What this survey
establishes is that the *new* products inspected have not yet supplied the clean signed observable a
replacement test would need.

## Standing — nothing here moves

- **No result, no claim, no video, no publication.** Nothing unblocks any lane.
- `lanes/spin/SOURCE_FREEZE.json` **still forbids BHU support** in that lane's video; this survey is
  research scoping and does not touch it.
- **Public data only; no new labelling**, per Duho.
- No cockpit, public site, wiki, video, data product, Git, runtime or acceptance-state change was made
  in producing this file. It is a private synthesis artifact and nothing else.
- Written from the four seat packets and the primary quotes registered in `citation-ledger.json`;
  where wording is reported rather than primary it is flagged as such in the source packets and must
  be primary-verified before any downstream use.

---

## APPEND-ONLY CORRECTION — 2026-08-11 20:15 KST

Filed by the **Claude-macbook** seat, which wrote this synthesis, on
`TORI_BHU_CITATION_CUSTODY_VERDICT_20260811.md`
(`CITATION_CUSTODY: FAIL_AS_WRITTEN` / `NARROW_OPERATIONAL_CLOSURE: SURVIVES`).

Nothing above is edited. This section states what in it was overstated.

### What I got wrong, and why

Tori read **arXiv:1910.10819v2 in full**; Lana and Kun read it at abstract depth, and I built on their
reading without flagging that gap. The body **does** contain a Kerr scale, force laws, Λ(Ω), data
redshifts and fitted axes. Therefore:

- My section heading **"Lana — no uniquely-BHU observable survives primary sources"** is too broad and
  is withdrawn as written.
- My sentence that BHU's predictions are **"either non-distinguishing … or qualitative and
  degenerate"** is not supported in that general form.
- **"A preferred axis with no predicted amplitude"** survives only in the narrow sense below: no
  *calibrated handedness* amplitude. The paper is not devoid of numbers.

### The statement that does survive, and it is enough

For the four sky-statistics routes this campaign attempted — galaxy handedness, public-data
isotropy/parity, the quasar number-count dipole, and parity-odd 4PCF — the cited BHU sources supply
**no frozen BHU-specific finite-precision prediction**: no calibrated handedness amplitude/scale/
redshift law or lower bound, no independently predicted axis, no quasar-count-dipole prediction, no
parity-odd 4PCF prediction.

That is why the four lanes found no BHU-specific test target. It is **not** proof that every BHU
proposal is untestable, nor that no future or full-literature route exists.

Also carried from Tori: the Brown–Lee–Rho/CNS neutron-star chain **does** provide a numerical test
near 2 M☉, and the cited pulsar masses reach or cross that threshold — a **separate nuclear-astrophysics
route**, not a sky statistic, and not covered by this survey's verdict.

### What is unaffected

The survey verdict **`NEW_PUBLIC_DATA_EXISTS_BUT_NO_READY_BHU_DISCRIMINATOR_UNDER_CURRENT_CONSTRAINTS`
stands.** It is a statement about *public data provenance* — no released catalogue publishes a frozen,
signed, documented handedness field — established by Tori's own gate and untouched by this correction.
The six mandatory corrections, the literature prior, and every standing constraint are likewise
unaffected.

Goru's independent sweep (`GORU_BHU_INDEPENDENT_LITERATURE_VERDICT_20260811.md`) searched deliberately
away from the ruled-out authors and found no quantitative distinguishable signature either. That
corroborates the narrow closure from a different search space; it does not restore the broad claim,
which needs comparative citations to the alternative models rather than BHU abstracts alone.

### Standing, unchanged

No result, no claim, no video, no publication. Nothing unblocks any lane. Spin-lane freeze intact.
Public data only, no new labelling. This correction changed no gate, no acceptance state, and no file
other than this one.

### Correction addendum — two further items from the full Tori verdict

Verdict binding: `TORI_BHU_CITATION_CUSTODY_VERDICT_20260811.md`,
SHA-256 `8a1d7a8d8d71a36768a544714c1365354d07aade40077b08dda7d0d00bef8ba9`, 23,867 bytes.

**A. Lana Revision 2 is not hash-gated.** Kun's gate binds a **16,945-byte predecessor**
(`12c052…`), not the Rev2 this synthesis drew on (`209f9e…`). My opening claims the verdict is
*"independently consistent with Lana's Step 1 and Kun's adversarial pass — three seats"*. The
verdict-level convergence stands (Kun's adversarial packet reached it on its own), but readers must
not take Kun's gate as validating the Rev2 text I quoted. **No adversarial gate currently binds the
revision this synthesis used.**

**B. The load-bearing axis paper is primarily `physics.pop-ph`.** arXiv:1910.10819v2 is categorised
popular-physics. That does not make its content wrong — Tori confirms it states the inherited
preferred axis and carries a Kerr scale, force laws, `Λ = 3Ω²/c²`, and numerical post-hoc axes and
redshift ranges — but it is context this synthesis omitted while treating the paper as the
programme's primary prediction source.

**Wording fix carried:** for the neutron-star chain, use **"reaches/crosses the stated
serious-doubt/falsification threshold"**, not definitive falsification. Brown–Lee–Rho
(DOI 10.1103/PhysRevLett.101.091101) states `M ≈/≳ 2 M☉` would *"put in serious doubt or simply
falsify"* the chain including CNS; Demorest `1.97 ± 0.04` and Fonseca `2.08 ± 0.07` resolve against it.

Pathria remains `[VERIFY]`: the accessible abstract and commentary do not establish exhaustive
absence of observables in the body. Citation verifier on the Tori report: PASS, 56% coverage,
9/9 sources with evidence quotes.

### Correction addendum 2 — Tori custody report Revision 2

Binding: `TORI_BHU_CITATION_CUSTODY_VERDICT_20260811.md` SHA-256
`b3f0a41681d25debdd8f10d434aa7666dea9287679075da9afdefa7bb814fcf3`, 27,501 bytes.
**Supersedes `8a1d7a8d…`, which addendum 1 cited.** Verdict unchanged:
`FAIL_AS_WRITTEN / NARROW_OPERATIONAL_CLOSURE_ONLY`.

**C. My neutron-star sentence was too strong — withdrawn.** Addendum 1 said Demorest and Fonseca
*"resolve against it."* Per Revision 2 they do not resolve that cleanly:

- Brown–Lee–Rho's corrected sign is `M ≳ 2 M☉` (APS Publisher Note DOI 10.1103/PhysRevLett.101.119901).
- **Demorest `1.97 ± 0.04`** — 1σ interval 1.93–2.01; **does not strictly cross by central value**.
- **Fonseca `2.08 ± 0.07`** — 68.3% interval 2.01–2.15, but **95.4% lower bound 1.95**, below the threshold.

Correct statement: the cited masses **approach and, at 1σ for Fonseca, exceed** the stated threshold;
they do not establish a clean crossing at 2σ. This remains a genuine quantitative route — and it is
the only one in this line — but its status is *threshold-adjacent*, not settled.

**D. The axis paper does make qualitative directional claims.** Revision 2 finds arXiv:1910.10819v2
asserts **parallel spin alignment, unequal handedness, and bulk flow perpendicular/away**. So
"excludes no finite-precision outcome" is too categorical, and my framing inherited that. What is
genuinely absent is narrower still: **an estimator, tolerance, likelihood, amplitude threshold, scale
law, or prospective finite-precision forecast.** The paper makes claims about *direction*; it supplies
nothing to *test them to a precision*.

**E. Two further items** that do not change this synthesis's verdict but correct the record it rests
on: 1007.0587's full text proposes an inherited-direction verification route without a forecast, and
its *"sixty orders below observability"* framing lacks a defined sensitivity basis; Pathria's abstract
itself asserts oscillation, a radius condition and bounded expansion, so "forbids nothing / no
dynamics" is too strong even before the paywalled body.

Citation verifier on Revision 2: PASS, 57% coverage, 10/10 sources with evidence.
