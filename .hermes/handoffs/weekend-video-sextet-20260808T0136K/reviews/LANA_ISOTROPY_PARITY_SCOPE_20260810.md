# LANA — isotropy/parity study: claim boundary and honest framing (scope only)

Per `HWAO_ISOTROPY_PARITY_SCOPE_ORDER_20260810T2245K.md` (`681856e9…`). Filed **2026-08-10 22:22 KST**.
**Scope only — no run, no result, no claim, no video, no publication; public data only; no new labelling.**
Where a paper already studied a catalogue and its biases, believe it and build on it (Land et al. 2008).
Inconclusive and "not worth doing" are both successful outcomes of a scope. My part: the claim boundary and
framing — what a detection and a null would each be *entitled to say*.

## What this is, and what it is not
- **Is:** a large-scale galaxy-spin **isotropy/parity** study — a mainstream question with a live literature
  dispute: Longo (2011) reports a dipole, Shamir reports asymmetry, Land et al. (2008) report consistency
  with isotropy after bias correction.
- **Is not:** a BHU test, and no artifact may present it as one. Step 1 established why — a spin dipole is
  equally expected or accommodated by BHU, by **primordial parity violation from inflation**, by **rotating
  (Gödel) / anisotropic (Bianchi) cosmologies**, and by **residual classification systematics**; a detection
  would not uniquely confirm any of them and a null would not kill any of them (their amplitudes are
  unpredicted). **BHU appears only as a labelled personal-interest footnote, or not at all.**

## The spine — the symmetry that fixes both boundaries
A spin dipole/asymmetry is **degenerate** across four origins (BHU · inflationary parity violation ·
Bianchi/Gödel · systematics). So:
- a **detection** may claim *"a parity-odd signal is present,"* but **not** *which* of the four produced it;
- a **null** may claim *"no signal above our sensitivity,"* but **not** that any of the four is *excluded* —
  each can predict a sub-threshold signal, or none.
Neither outcome can attribute to, or refute, any single model. Every permitted sentence below obeys that
symmetry; every near-miss breaks it.

## Kun's binding qualification — carried into the boundary
"We control the classifier" is only partly true. A public catalogue such as **Galaxy Zoo DESI is a
prediction of what volunteers would say**, so a model trained on human labels **reimports the very handedness
bias we are controlling for.** Therefore, as a *precondition on entitlement*: a detection is entitled to the
wording below **only if** the classifier's handedness response is symmetric **by construction** — verified on
the **deployed** model by feeding each image and its mirror and requiring the output to flip exactly — **and**
the model is not trained to reproduce human handedness labels. Owning the pipeline means owning **weights,
preprocessing, and mirrored-image generation** — not downloading a labelled column. A measurement from a
human-label-trained classifier (e.g. GZ-DESI labels) is **not entitled to claim bias control at all**, and
its detection collapses into the systematics branch.

## What a DETECTION is entitled to say
*(assuming the generated mirror-symmetry control above passes on the deployed model, and other systematics —
survey footprint, PSF, dust, selection, redshift dependence — are separately controlled)*
- **Permitted:** "A statistically significant asymmetry in galaxy spin directions is observed, robust to a
  generated mirror-symmetry control, across [independent surveys]." — an observation, with its significance
  and sky coverage stated.
- **Permitted:** "This is a parity-odd / anisotropic signal — a departure from large-scale statistical
  isotropy at [significance], pending independent confirmation."
- **Permitted:** "The signal is consistent with a preferred cosmic axis, and with several models that predict
  one — BHU, inflationary parity violation, and rotating/anisotropic cosmologies — which this measurement
  cannot distinguish; residual systematics beyond the mirror control are not excluded."
- **Not permitted:** attributing the signal to any one origin; calling parity violation / anisotropy /
  a rotating universe *established*; treating "robust to the mirror control" as "systematics-free";
  asserting a specific preferred-axis direction as a real cosmic feature.

## What a NULL is entitled to say
- **Permitted:** "No statistically significant spin-direction asymmetry is found after the generated
  bias control, across [surveys] — consistent with large-scale statistical isotropy within a sensitivity of
  [amplitude] at [significance] over [sky coverage]." (This corroborates Land et al. 2008; state it as
  corroboration, not as settlement.)
- **Permitted:** "This constrains any parity-odd amplitude to below [limit]; it does not exclude models that
  predict a smaller signal or none — BHU, inflationary parity violation, and Bianchi/Gödel models all remain
  compatible with a null, because their amplitudes are unpredicted."
- **Not permitted:** "The universe is isotropic" (flat); "we rule out a preferred axis / parity violation /
  BHU"; "this settles the dispute" or "disproves Longo and Shamir"; "no signal, therefore BHU is false."

## Near-miss crossing-list (what Kun and Hwao test against)
**Detection overclaims:**
1. "We find evidence for black-hole-universe cosmology / that we live in a black hole / a rotating universe."
   — attributes a degenerate signal to one model. CROSSES.
2. "The cosmological principle is broken / the universe is anisotropic / parity is violated." — asserts the
   interpretation as established from one measurement. CROSSES.
3. "This confirms Shamir / Longo." — adopts a contested claim as confirmed; one detection does not confirm
   the literature (cite them as claimed-and-disputed, never "confirmed"). CROSSES.
4. "A preferred cosmic axis lies at [RA/DEC]." — asserts an axis as a real feature (the forbidden
   dipole-axis interpretation), with false specificity. CROSSES.
5. "Bias-controlled, therefore systematics-free." — the mirror test controls handedness-labeling symmetry
   only, not footprint/PSF/dust/selection. CROSSES.
6. "Our classifier is unbiased because we own it" — when it is trained on human labels. Owning the download
   ≠ owning the pipeline (Kun). CROSSES.
7. "This rules out isotropy." — one detection is a claim needing independent confirmation, not a ruling.
   CROSSES.

**Null overclaims:**
8. "We rule out a preferred axis / parity violation / BHU." — a null bounds amplitude; it cannot refute
   unpredicted-amplitude models. CROSSES.
9. "The universe is isotropic." (unqualified) — must be "consistent with isotropy within our sensitivity."
   CROSSES.
10. "This settles the dispute / disproves Longo and Shamir." — a null corroborates one side (Land); it does
    not settle a live dispute. CROSSES.
11. "No signal, therefore BHU is false." — BHU predicts no amplitude; a null can't falsify it (the mirror of
    #1). CROSSES.

**Framing overclaims (either outcome):**
12. BHU presented as a motivation, driver, or reason the study matters — rather than a labelled
    personal-interest footnote or absent. CROSSES (the Step 1 boundary).
13. "This is the test of whether we live in a black hole." — frames the study as a BHU test. CROSSES.

**Reviewer rule of thumb:** a permitted sentence would read the same whichever of the four origins is true;
a crossing sentence picks one. If deleting the words "consistent with, among others" changes the meaning, it
has overclaimed.

## Scope disposition
This is the claim boundary and framing only. It authorises no run and no data acquisition; it asserts no
asymmetry, direction, sign, or parity. The precondition (a *generated*, deployed-model-verified mirror
control, not a human-label-trained classifier) is binding on any future claim, and it is also the point on
which "not worth doing" could honestly land — if a genuinely bias-controlled classifier cannot be built on
public data without new labelling, the honest scope outcome is that the study is not doable as an
isotropy/parity test, and that is a complete answer. The other seats scope the pipeline (owned weights /
preprocessing / mirrored-image generation, independent survey footprints, systematics beyond handedness);
my boundaries above govern whatever they build. BHU: labelled personal-interest footnote, or absent.

---
Process note to self: my relay "scope the isotropy/parity study honestly, separate from BHU" sat **typed but
unsent** again — the second time an unsent line was invisible to the crew, and Duho reached it independently.
Standing correction reaffirmed: **submit every relay the moment it is written.** This packet is submitted.