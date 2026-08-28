# HWAO ORDER v2 — isotropy/parity scope, hardened per Kun

Stamped 2026-08-10 23:20 KST. Duho: *"rewrite the scope with the inherited-prior control."*
**Supersedes `HWAO_ISOTROPY_PARITY_SCOPE_ORDER_20260810T2245K.md`** (preserved, not authority).
Hardened per `KUN_ISOTROPY_PARITY_SCOPE_ADVERSARIAL_20260810T2245K.md`
(`SCOPE_PROCEED_WITH_HARDENING_REQUIRED`).

## The correction that drives this rewrite

**Mirror anti-equivariance is necessary but NOT sufficient.** I overstated the advantage when I
put it to Duho, and Kun proved it:

> *"A model trained on human labels can learn a chirality decision rule that is perfectly
> anti-equivariant under image mirroring while still carrying a sky-position, survey-depth,
> redshift… prior."*

A classifier can flip perfectly on every mirrored pair — passing the self-test cleanly — while its
behaviour still varies with **where on the sky** the galaxy sits. That is precisely where a
spurious dipole comes from. The self-test removes the 2008 blocker; it does not remove the general
problem.

## The seven hardenings, all required

1. **State explicitly** that mirror anti-equivariance is necessary but not sufficient. No scope
   that treats it as sufficient is admissible.
2. **Inherited-prior / selection-bias control** — first class, not an appendix. It must test
   whether the classifier's **confidence and abstention**, not only its label flips, depend on
   sky-position-correlated covariates *after* the mirror pair is accounted for.
3. **Forbid `spiral-winding` from GZ DESI/DECaLS as chirality.** Those columns are a prediction of
   what volunteers would say, not an instrument-independent handedness measurement.
4. **WCS parity validation as a first-class gate**, with **Jacobian sign receipts** and **injected
   asymmetric test images**. Kun calls this a single-point catastrophic failure: get parity wrong
   and every downstream number inverts silently.
5. **Expand the null-control covariates** beyond depth/seeing/latitude/instrument/redshift to
   include Galactic extinction and stellar density separately from latitude, sky brightness and
   airmass history, PSF ellipticity and model residuals, deblending/crowding flags,
   surface-brightness completeness, angular size and inclination proxy, colour and band-dependent
   arm contrast, and profile type or bulge fraction. Require joint preservation **or** adversarial
   sky-position-predictability tests.
6. **Replication: two instrument families is a FLOOR, not sufficiency.** Preferred-axis language
   additionally requires independence of imaging, footprint, preprocessing **and** classifier.
7. **An explicit `NOT_WORTH_DOING_YET` branch** if no public chirality estimator can be frozen
   without new labelling — which Duho has ruled out.

## What this scope is, unchanged

A **large-scale galaxy-spin isotropy/parity** study — mainstream, with a live dispute between
Longo, Shamir and Land. **Not a BHU test**; BHU is a labelled personal-interest footnote or absent.
Lana's Step 1 governs: a detection would not uniquely confirm BHU and a null would not kill it.

## Seats

**Kun** — you wrote the hardenings; now attack v2 as written, especially whether your own
inherited-prior control is *itself* sufficient, or whether a classifier could pass both the mirror
self-test and the confidence/abstention test and still leak a sky-correlated prior.
**Lana** — permitted wording for a detection and for a null, plus the near-miss list.
**Goru** — per candidate: are raw FITS retrievable, are weights/preprocessing public, is released
morphology a human-label prediction or an independent measurement.
**Tori** — provenance gate per candidate before any design commitment; grade DOCUMENTED /
UNDOCUMENTED / NOT-YET-CHECKED, quoting primaries.
**Yui** — still holding; nothing to build.

## Standing

**Scope only — the admissible next product is a stricter design brief, not a run.** Kun's words.
Public data only, no new labelling. Where a paper already studied a catalogue and its biases,
believe it and build on it. `NOT_WORTH_DOING_YET` and `INCONCLUSIVE` remain successful outcomes.
