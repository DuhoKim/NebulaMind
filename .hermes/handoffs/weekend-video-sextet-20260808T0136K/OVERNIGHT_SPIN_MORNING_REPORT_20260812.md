# Overnight spin-parity run — morning report (07:42 KST, 2026-08-12)

Dispatched 00:10–00:15; the chain converged by 00:55, before the first tick fired. All four seats
idle at 07:42, no stalls, nothing restarted, nothing new since 01:23. Tick 2 was cancelled as
redundant rather than left to fire into a finished chain.

---

## (a) Is there a design brief, and did Kun pass it?

**Yes, and yes — as a design only.**

`reviews/LANA_SPIN_DESIGN_BRIEF_20260812.md`, 20,778 bytes.
`reviews/KUN_SPIN_DESIGN_BRIEF_GATE_20260812.md`, 9,385 bytes:

> `PASS AS A DESIGN BRIEF; NOT A PREREGISTRATION FREEZE; NO EMPIRICAL SKY RUN YET.`
> *"The design is buildable in principle. It is not yet frozen."*

His three-tier gate holds: label-table reanalysis `NOT_WORTH_DOING_YET`; image-level,
custody-audited, mirror-controlled, preregistered fixed-axis test `WORTH_SCOPING`; immediate
empirical run `BLOCKED`.

Acceptance/rejection regions are pre-declared at both published axes — Longo `(l,b)=(52°,68.5°)`,
Shamir `(RA,Dec)=(132°,32°)` — with `REPRODUCED` / `REJECTED-AT-CLASS` / `INCONCLUSIVE` /
`INCONCLUSIVE-BY-POWER` branches. Kun: *"That is the right shape. It forces ambiguity to
INCONCLUSIVE rather than letting a weak result be narrated into support."* Kill switches are
*"real switches, not decorative caveats."*

The design rests on Lana's antisymmetry identity: for `χ(x) := (w(x) − w(mirror(x)))/2`,
`χ(mirror(x)) = −χ(x)` **for any weights and any w, regardless of training data** — so the sorter
cannot manufacture a net asymmetry, acceptance thresholds cannot chirality-filter, and biased
training costs sensitivity, never validity. That is precisely what the GZ1 lane lacked.

---

## (b) Which survey passes BOTH requirements?

**Goru: none. Kun: that standard is wrong. Tori: one passes a narrower gate, on evidence.**

Goru's survey returns `Custody Status: FAILS` for **every** candidate — HSC, DESI Legacy, SDSS,
Pan-STARRS, KiDS, DES, Euclid, Rubin — on the grounds that no survey publishes its own
mirrored-image control runs or native parity-check documentation.

Kun ruled that over-strict, and this is the night's decisive judgment:

> *"The design does not require the survey to publish mirrored-image control runs. We run the
> mirrored control. That is the point of the architecture."*

His correct standard: public calibrated pixel data with intact per-image WCS **sufficient for us to
compute pixel-to-sky parity ourselves**; failure is *"only rendered images with no WCS or
unverifiable orientation."* Given calibrated pixels plus WCS, the determinant of the pixel-to-sky
transform establishes parity directly.

Tori then tested rather than cited, and **graded her own result downward** after reading a
prerequisite she had initially been unable to locate:

| source | access | delivery | grade |
|---|---|---|---|
| **DESI Legacy DR10** `fits-cutout` | anonymous | **real FITS, float32, TAN WCS, 5,760 B, hash recorded** | passes the **exact FITS/WCS delivery gate for that request** |
| HSC-SSP PDR3 | account + term acceptance | FITS documented | exact delivery **UNDOCUMENTED**; WCS unverifiable without credentials |
| SDSS SkyServer `ImgCutout` | anonymous | `getjpeg` | **UNSUITABLE — RENDERED DISPLAY**, no FITS header |
| SDSS SAS corrected frame | anonymous | full corrected-frame FITS | documented image source; exact delivery untested |
| Pan-STARRS1 DR2 | anonymous | FITS cutouts | documented, **UNTESTED**; obsolete PC WCS, RADESYS + polar caveats, ≤10 threads |

**The honest limit, in her words:** *"This passes the exact-delivery FITS/header gate for that
request, but it is a generated TAN cutout and not an untouched detector frame."* And:
*"One valid FITS header is an access/header receipt, not by itself an end-to-end parity custody
proof."* Verifier: 22/22 sources quote-backed, 61% coverage.

**So: no survey clears end-to-end parity custody today. One — Legacy DR10 — clears the delivery
gate on demonstrated evidence, which is the prerequisite for attempting the rest.**

---

## (c) What is blocked, and on what

1. **Any empirical sky run — BLOCKED by Kun** until a separate preregistration artifact freezes
   every open value. Not a caveat; his stated gate.
2. **Preregistration freeze — blocked on two things Kun names:** the §7 power estimate (the numeric
   thresholds are still "the proposal"), and exact executable definitions for the covariate battery —
   maps, binning, regression or matching model, leakage threshold, and what counts as "ambiguous."
3. **End-to-end parity custody — unestablished for every survey**, including Legacy DR10. Kun's
   stated next step is a **non-sky-statistic feasibility/custody spike**: lossless rendering, WCS
   parity logging, synthetic chiral injections, original/mirror paired classification through the
   exact measurement path. None of that touches a sky statistic.
4. **HSC** cannot be graded without credentials; Tori specifies exactly what a future authorised test
   must inspect (`CTYPE*`, `CRPIX*`, `CRVAL*`, CD/PC, `RADESYS`, dimensions, HDUs, resampling).

---

## (d) What needs a decision from Duho

1. **Authorise the feasibility/custody spike, or not.** It is the only sanctioned next step. It runs
   on Legacy DR10, computes no sky statistic, and answers whether end-to-end parity is provable.
2. **Whether to pursue HSC access.** It needs an account and term acceptance — an outward action
   nobody here will take without an explicit instruction from you.
3. **Whether Pan-STARRS should be live-tested** the way Legacy was. It is documented but untested,
   and one cutout would settle it.
4. Note for the record: **a positive result would not identify BHU.** That line is closed (Kun's
   `PASS_FINAL_CLOSING_RECORD_ON_REVISION_5`). This study, if run, is about the Longo/Shamir
   dispute in its own right.

Nothing published, accepted, acquired, or run. Four seats idle and clean.
