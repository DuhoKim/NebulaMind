# BS-5 — Longo sign dictionary (fill receipt)

**Lana (science / claim-boundary seat), 2026-08-14. Fills Binding Slot BS-5 of
`PREREG_LONGO_AMPLITUDE_TEST_20260812.md`.** Documentation work only — no real-sky data, no object rows, no
images, no sky statistic. **Not published, accepted, run, committed, or pushed. Kun gates; Duho decides.**

> **Why this slot is the highest risk (register line 10–12):** a sign error inverts the result and is caught
> by no internal consistency check. This receipt fills BS-5 **by verbatim quotation from Longo's methods,
> never from memory**, and anchors the absolute estimator sign to an external synthetic injection so a coding
> sign-flip cannot silently invert the outcome.

## Source (custody)
- **Longo, M. J., "Detection of a Dipole in the Handedness of Spiral Galaxies with Redshifts z ~ 0.04,"
  Phys. Lett. B 699 (2011) 224–229**, DOI `10.1016/j.physletb.2011.04.008`; preprint **arXiv:1104.2815**.
- Full text retrieved as PDF 2026-08-14; **SHA-256 `4cd5d41f7ed8553452cbd5179f2f00b62a390e7f2a3734b7d29e1da9fe8f0c83`**
  (arXiv PDF). All quotes below are from that text with page/section locators. Abstract axis/amplitude
  cross-checked against the arXiv abstract record.

## 1. Longo's primitives — verbatim, with locators
- **Handedness symbols (Section 2 "The Analysis", paragraph 3, p. 3):**
  > *"The scanners had only 3 choices: Left, Right, or Unclear, where Left ≡ ↺ and Right ≡ ↻."*
  So **Left ≡ ↺ (counter-clockwise arrow)** and **Right ≡ ↻ (clockwise arrow)**.
- **Viewpoint — as the galaxy appears to the observer (Fig. 1 caption, p. 2):**
  > *"(b) A 'typical' spiral galaxy from the SDSS. This one is defined as having right-handed 'spin'. (c) A
  > left-handed two-armed spiral galaxy."* and *"Note that galaxies in one hemisphere would appear to us to be
  > right-handed and in the opposite hemisphere left-handed."*
  The classification is the **apparent visual winding in the sky image** (RGB images shown to scanners) — a
  line-of-sight projected quantity, no de-projection. **Our estimator operates on the same as-appears
  analysis raster, so the identification is like-for-like.**
- **Asymmetry parameter (Section 3 "Results", paragraph 1, p. 4):**
  > *"A plot of asymmetries ⟨A⟩ ≡ (R − L)/(R + L), binned in 30° sectors of right ascension and 0.01 slices in
  > z for z<0.085, is shown in Fig. 2. Positive ⟨A⟩ are shown in red and negative ones in blue."*
  So **A ≡ (R − L)/(R + L)**, R = Right = ↻ = clockwise, L = Left = ↺ = counter-clockwise.
- **Direction of the effect (Section 3, paragraph 1, p. 4):**
  > *"There is an apparent excess of left-handed spirals in the sectors for 150°< α<240° and a complementary
  > excess of right-handed in the opposite hemisphere…"*
- **Amplitude and axis (Abstract, p. 1):**
  > *"…gives a dipole asymmetry of −0.0408±0.011 with a probability of occurring by chance of 7.9 x 10⁻⁴… The
  > axis of the dipole asymmetry lies at approx. (l, b) =(52°, 68.5°)…"*

## 2. What Longo's sign means (unambiguous — no tie-break needed to read it)
`A ≡ (R − L)/(R + L)` and the reported dipole value is **negative, −0.0408**. Negative ⟹ **L > R** ⟹ an
**excess of Left-handed (↺, counter-clockwise) spirals looking toward the axis** `n̂_L = (l,b) = (52°, 68.5°)`.
This is internally corroborated: the excess-of-left sector `150°<α<240°` contains the dipole axis
(`α ≈ 217°`, the equatorial equivalent frozen in prereg §1), and Fig. 2's "Dipole axis" arrow points into that
same left-excess region. **Longo's paper is not ambiguous about its own sign.**

## 3. Mapping to our East-of-North winding convention (the fill)
Our estimand (prereg F-1): `D̂(n̂_L) = (1/N)·Σᵢ sign(χᵢ)·cos θᵢ`, `Â = 3·D̂`. The prereg leaves the **polarity of
`sign(χ)` unset** (I-2 defines `χ` up to sign); BS-5 fixes it. Per the BS-5 fill rule — *"the documented
convention is chosen so his reported amplitude is positive toward his stated axis, and the [choice] is
published"* — and so that the prereg's F-6 band `|Â_c − 0.0408|` (written around **+0.0408**) is centred
correctly, we adopt:

> **DEFINITION (frozen here):** `sign(χ) = +1` for **counter-clockwise apparent winding (↺ = Longo-Left =
> "left-handed")**; `sign(χ) = −1` for **clockwise (↻ = Longo-Right)**, evaluated on the analysis raster in sky
> coordinates with **winding measured East-of-North** (position angle increasing from North through East; on a
> North-up / East-left raster this increasing-PA sense is counter-clockwise = ↺).

Under this definition `D̂` is the **(L − R)-weighted dipole moment**, so Longo's effect reproduces as a
**positive** value toward `n̂_L`:

> **Longo's target in our convention: `Â(n̂_L) = +0.0408` (± 0.011 published), at `n̂_L = (l,b) = (52°, 68.5°)`
> ≡ (α,δ) = (217°, 32°) [equatorial equivalent frozen in prereg §1, not re-derived here].**
> A **REPRODUCED-LONGO** outcome (F-6) therefore requires `Â_c` **positive** (an excess of ↺/CCW/Left looking
> toward `n̂_L`) **AND** `|Â_c − 0.0408| ≤ 3·σ_comb`. A negative `Â_c` of similar magnitude is **not** a
> reproduction of Longo — it is the opposite sign and falls outside the band.

## 4. Published polarity note (carried openly, not silent)
Longo's **native** formula is `A ≡ (R − L)/(R + L)` with reported value **−0.0408** (excess of Left). We adopt
the **(L − R) polarity** for `+χ`, so the *same physical effect* is written **+0.0408** in our convention. This
is a deliberate, documented polarity choice to (a) satisfy the BS-5 tie-break rule and (b) match the prereg
F-6 band centred at +0.0408. **The physical content is identical and must be stated wherever the number
appears: an excess of counter-clockwise (↺, Longo-"Left") spirals looking toward (52°, 68.5°).** No reader
should be told Longo "reported +0.0408" — he reported −0.0408 in (R−L); the +0.0408 is our (L−R) re-expression.

## 5. Absolute-sign anchor (mandatory — closes the "inverts silently" risk)
Because a code-level sign flip in `χ` would invert the result undetectably, the polarity in §3 is **binding on
the estimator only through an external synthetic anchor**, checked in the prereg injection battery (PC-5,
I-4, control C1) **before any real image**:
- Inject a synthetic spiral of **known counter-clockwise (↺) apparent winding** on the production raster; the
  estimator **must** return `χ > 0` (`sign(χ)=+1`). Its pixel-mirror must return `χ < 0`.
- If the estimator returns the opposite sign, the code sign is flipped and **must be corrected on synthetic
  images before the run** (a calibration on synthetic data — no real sky touched). WCS parity (PC-3: North-up/
  East-left, determinant-logged) must be validated first, since an unnoticed parity error would itself invert
  the anchor.
This makes the BS-5 sign **operationally falsifiable**, not an assertion.

## 6. Validity check (BS-5 range: "unambiguous mapping; if ambiguous, choose so amplitude is positive toward the stated axis, and publish")
- Mapping is **unambiguous**: Longo's Left≡↺/Right≡↻, `A≡(R−L)/(R+L)`, −0.0408 toward (52°,68.5°) are all
  quoted verbatim with locators. ✔
- Convention **chosen so the reproduced amplitude is positive** (+0.0408) toward the stated axis. ✔
- Polarity choice **published** openly (§4), and anchored to a synthetic injection (§5). ✔
**BS-5 PASSES its validity range.** No value tuned; the sign is fixed by quotation and by an external anchor.

## Custody / boundary
sample rows exported: 0 · positions: 0 · images: 0 · chirality computed on real sky: 0 · sky statistics: 0 ·
bulk downloads: 0 · publication/acceptance/commit/push: 0. Sourced only from Longo 2011 (hash above) and the
prereg. Back to Kun to gate; Tori may bind the published-journal page locators alongside the arXiv locators at
freeze. — Lana, 2026-08-14.
