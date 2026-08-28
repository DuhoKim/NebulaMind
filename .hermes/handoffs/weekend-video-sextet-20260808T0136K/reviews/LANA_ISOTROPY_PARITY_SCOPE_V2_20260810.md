# LANA — isotropy/parity study, SCOPE v2 (hardened per Kun): claim boundary + permitted wording

Per `HWAO_ISOTROPY_PARITY_SCOPE_ORDER_V2_20260810T2300K.md` (`99a1519a…`). **Supersedes the v1 scope
(`…2245K`), which is preserved but is not authority — work from v2 only.** Filed **2026-08-10 23:22 KST**.
**Scope only — the admissible next product is a stricter design brief, not a run.** Public data only, no new
labelling; believe existing catalogue-bias papers (Land et al. 2008). NOT_WORTH_DOING_YET and INCONCLUSIVE
are successful outcomes. My part: the permitted wording for a detection and a null, and the near-miss list.

## The correction that drives v2 — and it is mine to own
I told Duho the mirror control gave us a decisive advantage over 2008. **That overstated it, and Kun
proved it: mirror anti-equivariance is necessary but not sufficient.** A model trained on human labels can
learn a chirality rule that flips perfectly on every mirrored pair — passing the self-test cleanly — while
still carrying a **sky-position, survey-depth, and redshift prior.** Its behaviour varies with *where on the
sky* a galaxy sits, and that is exactly where a spurious dipole comes from. The self-test removes the 2008
blocker; it does not remove the general problem. Every entitlement below is now gated on more than the
mirror test.

## The spine — degeneracy symmetry (unchanged), now under a sufficiency ladder
Both a detection and a null remain **degenerate** across BHU · inflationary parity violation · Bianchi/Gödel
· systematics, so neither attributes to nor refutes any one (Step 1 governs). **New in v2:** passing the
mirror self-test is only the first rung. A detection earns claim-strength by climbing a ladder of controls;
without them it earns nothing, no matter how clean the mirror test looks.

**Preconditions that gate any sky claim (the seven hardenings):**
1. Mirror anti-equivariance is **necessary but not sufficient** — state this explicitly on any artifact.
2. **Inherited-prior / selection-bias control** — test whether the classifier's **confidence and abstention**
   (not only its label flips) depend on sky-position-correlated covariates after the mirror pair is
   accounted for.
3. **No volunteer-prediction chirality.** GZ DESI/DECaLS spiral-winding columns predict what volunteers would
   say, not handedness, and **may not be used as a chirality measurement.**
4. **WCS parity validation** as a first-class gate — Jacobian-sign receipts and injected asymmetric test
   images. A single-point catastrophic failure: get parity wrong and every downstream sign inverts silently.
5. **Full null-control covariate battery** — Galactic extinction and stellar density (separately from
   latitude), sky brightness, airmass history, PSF ellipticity and model residuals, deblending/crowding
   flags, surface-brightness completeness, angular size and inclination proxy, colour/band-dependent arm
   contrast, profile type / bulge fraction — with joint preservation or adversarial sky-position-
   predictability tests.
6. **Two instrument families is a floor, not sufficiency.** Preferred-axis language additionally requires
   independence of **imaging, footprint, preprocessing, and classifier.**
7. **NOT_WORTH_DOING_YET** if no public chirality estimator can be frozen meeting 2–6 without new labelling.

## What a DETECTION is entitled to say — as a ladder (controls passed → wording earned)
- **Mirror self-test only:** entitled to say only *"the classifier is anti-equivariant under mirroring."*
  **Not** entitled to any claim about the sky — an inherited sky-position prior could produce the entire
  signal.
- **+ inherited-prior/selection controls (2,5) pass, single instrument:** *"a spin-direction asymmetry robust
  to the mirror control and to the tested sky-position-correlated covariates, in [survey], at [significance]
  — not yet shown independent of imaging, footprint, preprocessing, or classifier."* **No** preferred-axis
  language.
- **+ WCS parity validated (4):** required before **any** directional or sign statement at all; without it,
  the sign may be silently inverted and no directional claim is admissible.
- **+ independence across ≥2 instrument families and across imaging/footprint/preprocessing/classifier (6):**
  the strongest admissible wording — *"Across [independent instruments and pipelines], an owned chirality
  estimator (not derived from volunteer-prediction catalogues; verified anti-equivariant on the deployed
  model; WCS-parity-validated; with confidence and abstention shown independent of the covariate battery)
  yields a statistically significant galaxy-spin-direction asymmetry at [significance] over [coverage]. This
  is a parity-odd signal consistent with a preferred cosmic axis and with several models that predict one —
  BHU, inflationary parity violation, and rotating/anisotropic cosmologies — which this measurement cannot
  distinguish; residual untested systematics are not excluded, and independent confirmation is required."*
- **Ceiling, regardless of controls:** the degeneracy caveat is mandatory — no detection, however clean,
  may attribute the signal to any single origin or call parity violation / anisotropy / a rotating universe
  *established*.

## What a NULL is entitled to say
- **Permitted:** *"With a chirality estimator meeting the preconditions (owned, non-inherited,
  mirror-verified, WCS-parity-validated, covariate-controlled), no statistically significant spin-direction
  asymmetry is found across [surveys] — consistent with large-scale statistical isotropy within a
  sensitivity of [amplitude] at [significance] over [coverage], corroborating Land et al. 2008. This bounds
  any parity-odd amplitude below [limit]; it excludes none of BHU, inflationary parity violation, or
  Bianchi/Gödel models, whose amplitudes are unpredicted."*
- **Mandatory conditionals:** the bound is **conditional on the WCS-parity validation** (an undetected
  parity error could cancel a real signal) and **on the covariate controls** (an uncontrolled prior can
  fake or mask a null). A null from an uncontrolled estimator is not informative and may claim nothing.
- **Not permitted:** *"the universe is isotropic"* (unqualified); *"rules out a preferred axis / parity /
  BHU"*; *"settles the dispute / disproves Longo and Shamir."*

## NOT_WORTH_DOING_YET — a live, successful outcome
Because volunteer-prediction winding is forbidden (3) and new labelling is ruled out, there may be **no
admissible public chirality estimator to freeze** — one that is (a) not derived from volunteer labels, (b)
verifiable anti-equivariant on the deployed model, (c) WCS-parity-validated, and (d) shown free of
sky-position-correlated confidence/abstention priors. **If none can be frozen without new labelling, the
honest scope outcome is NOT_WORTH_DOING_YET** — the study is not doable now as an isotropy/parity test.
That is a complete and successful answer, not a failure, and given the hardenings it is a genuinely likely
one. This is the point on which the whole study may honestly stop.

## Near-miss crossing-list (what Kun and Hwao test against)
**Detection overclaims:**
1. *"The classifier flips on mirrors, so the asymmetry is real / cosmic."* — the v2 core error: mirror
   anti-equivariance is necessary, not sufficient; an inherited sky-position prior survives it. CROSSES.
2. *"We control the classifier because we own the weights"* — while it carries a sky-position/depth/redshift
   prior. Owning weights ≠ owning the prior. CROSSES.
3. Using GZ DESI/DECaLS winding as a handedness measurement. — measures volunteer predictions, not
   chirality. CROSSES (forbidden outright).
4. Any directional / sign / axis claim without WCS parity validation. — silent-inversion risk. CROSSES.
5. *"Evidence for black-hole-universe cosmology / a rotating universe / that we live in a black hole."* —
   attributes a degenerate signal to one model. CROSSES.
6. *"Parity is violated / the universe is anisotropic / the cosmological principle is broken."* — asserts
   an interpretation as established. CROSSES.
7. *"This confirms Shamir / Longo."* — adopts a contested claim as confirmed. CROSSES.
8. *"A preferred axis lies at [RA/DEC]"* from one instrument/pipeline. — preferred-axis language needs
   independence of imaging/footprint/preprocessing/classifier (6). CROSSES.
9. *"Mirror-controlled, therefore systematics-free."* — the mirror test controls handedness symmetry only,
   not the covariate battery. CROSSES.
10. *"Reproduced across two surveys, therefore confirmed."* — two families is a floor; a shared
    preprocessing/classifier can carry a common prior. CROSSES.

**Null overclaims:**
11. *"We rule out a preferred axis / parity / BHU."* — a null bounds amplitude; it cannot refute
    unpredicted-amplitude models. CROSSES.
12. *"The universe is isotropic."* (unqualified) — must be *"consistent with isotropy within our
    sensitivity."* CROSSES.
13. *"This settles the dispute / disproves Longo and Shamir."* — a null corroborates one side; it does not
    settle a live dispute. CROSSES.
14. *"No signal, therefore BHU is false."* — BHU predicts no amplitude (mirror of #5). CROSSES.
15. A null stated without its **conditionals** (WCS-parity validation, covariate controls). — an
    uncontrolled null is not informative. CROSSES.

**Framing (either outcome):**
16. BHU presented as a motivation, driver, or reason the study matters, rather than a labelled
    personal-interest footnote or absent. CROSSES (Step 1).

**Reviewer rule of thumb (v2):** *"passes the mirror self-test"* is never, by itself, a licence to claim
anything about the sky. A permitted sentence names its preconditions and its degeneracy; a crossing
sentence claims the sky from a control that removes only one artifact.

## Scope disposition
This authorises no run and no data acquisition; it asserts no asymmetry, direction, sign, or parity. The
admissible next product is a stricter **design brief** (owned/non-inherited chirality estimator; the
inherited-prior and covariate controls; WCS-parity gate; instrument/pipeline independence) — Kun's, Goru's,
Yui's to draft; my boundaries above govern whatever they build. If that brief cannot freeze an admissible
public estimator without new labelling, NOT_WORTH_DOING_YET is the honest end. BHU: labelled
personal-interest footnote, or absent. My relay is submitted, not left in the pane.