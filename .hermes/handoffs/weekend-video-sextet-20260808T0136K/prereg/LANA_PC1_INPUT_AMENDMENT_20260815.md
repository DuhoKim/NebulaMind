# PC-1 INPUT-CONTRACT AMENDMENT — 128×128, SINGLE BAND r, FLOAT32
## Line-by-line amendment to the pixel input contract of the Longo-amplitude test

**Lana (science / claim-boundary seat), 2026-08-15. Status: AMENDMENT DRAFT — Duho approved the
amendment direction (128×128, one band, float32); Kun's strategy gate is
PASS_WITH_REPAIRS_FOR_STRATEGY_ONLY, HOLD EXECUTION (`KUN_STRATEGY_GATE_20260815.md`). Nothing is
frozen, published, accepted, committed, or pushed by writing this. Nothing was fetched.
`PREREG_LONGO_AMPLITUDE_TEST_FROZEN_20260815.md` (SHA-256
`62dad44dd92acf2781d2c8cf25161f7f344e3fe6f7fec35b7e04308bd1539c12`, mode 444, merged) is not
modified; producing the v3 prereg candidate is a separate later step. Kun gates; Duho owns
acceptance.**

**K-8 timing statement, explicit:** no real-sky statistic exists anywhere in this program — no
chirality label, no sky estimand, no unblinding. This amendment is made at the only safe time,
before the run. Altering the input contract *after* any real-sky statistic would fall under K-8
and void the run.

---

## 1. The defect being repaired

`TORI_SURVEY_ROUTE_BINDING_20260812.md` freezes the cutout request at `size=256`, `bands=grz`
(three 256×256 planes). `YUI_PRODUCTION_ESTIMATOR_APPENDIX_20260812.md` §3 freezes the instrument
as **ResNet-18, single input channel, 128×128**. The route fetches 12× more pixel data than the
instrument consumes (3 × 256² = 196,608 delivered pixels vs 1 × 128² = 16,384 consumed), and the
mapping from delivered planes to the consumed tensor was never frozen anywhere — an undefined,
untested reduction step sitting exactly where the custody chain must be tightest. Kun ruled PC-1
(the route side) is the document that is wrong, **unless** the science seat determines that g+r+z
information is required, in which case the estimator appendix is what must be refrozen instead.

## 2. The science decision: one band suffices, and the band is r

This decision is mine as science seat. I did not take the one-band answer because it is cheap;
here is the reasoning, in order of how much weight it carries.

**(a) Chirality is parity-odd; pixelwise color is parity-even.** The mirror operation is a pure
index reversal: it flips geometry and preserves every pixel's per-band values, hence every color.
The winding-direction signal therefore lives entirely in the *spatial* arrangement of flux, never
in color itself. Color can only help the instrument *see the arms better* (segmentation
contrast) — a sensitivity effect, not an information channel for the sign. Formally: any benefit
of adding bands moves the attenuation `a`, and `a` is measured (HC-1H) and gated (HC-6, floors
HC-5). The reflection-equivariance identity χ(mirror(x)) = −χ(x) holds for any input map, so band
choice **cannot manufacture asymmetry**; the design is safe under a suboptimal band, and the cost
of a wrong choice is honestly priced as power, not silently as bias.

**(b) The one channel the identity does NOT cover is where band choice actually matters.**
Monopole × sensitivity-gradient coupling — position-correlated variation in instrument
sensitivity — is the known uncovered channel. Band choice modulates it directly:
- **Galactic extinction** varies across the footprint, and the per-band coefficients are pinned
  from the survey's primary documentation: **A/E(B−V) = 3.214 (g), 2.165 (r), 1.211 (z)** —
  Legacy Surveys DR10 catalog documentation (legacysurvey.org/dr10/catalogs, "Galactic Extinction
  Coefficients": *"These coefficients are A/E(B-V) = 3.995, 3.214, 2.165, 1.592, 1.211, 1.064
  for the DECam u, g, r, i, z, Y filters, respectively"*, computed per the Appendix methodology
  of Schlafly & Finkbeiner 2011). The g > r > z ordering is therefore not an assertion but
  arithmetic: 3.214 > 2.165 > 1.211, with g's coefficient 1.48× r's and 2.65× z's. A g-band
  instrument would have its S/N — and therefore its sensitivity — correlated with Galactic
  latitude more strongly than r or z.
- **Sky brightness and its temporal variation** are strongest in z (airglow/moon), imprinting
  observing-condition structure on depth.
- **Arm/interarm contrast is stronger in bluer bands**, from the primary measurement: Yu, Ho,
  Barth & Li 2018, *The Carnegie-Irvine Galaxy Survey. VI. Quantifying Spiral Structure* (ApJ,
  DOI 10.3847/1538-4357/aacb25; arXiv:1806.06591), abstract: *"it [the arm strength] is stronger
  in bluer bands than redder bands"* (measured across BVRI). The trend is monotonic blue→red and
  g, r, z are ordered blue→red, so the g > r > z contrast ordering follows. The abstract does
  not quantify the size of the trend, so the earlier unquantified "magnitude" clause is
  **deleted rather than filled** — the argument uses only the ordering, which is sourced.
r is the band that keeps most of the arm contrast while sitting at neither extreme of the
position-correlated systematics: substantially lower extinction sensitivity than g,
substantially lower sky-variation sensitivity than z. For a **dipole** estimator, minimizing
sky-correlated sensitivity structure at modest contrast cost is the right trade — CB battery
covariates (extinction, depth, seeing) remain the frozen diagnostic for whatever residue is left.

**(c) The study's selected parent guarantees r flux — by our frozen cuts, with the selection
limit as separate support, not by its imagery.** The GZ DECaLS (GZD-5) sample is selected from
the NASA-Sloan Atlas v1.0.0 with an r-band-limited selection tendency: Walmsley et al. 2022
(arXiv:2102.08414) §2.2 — *"NSA primarily includes galaxies with m_r = 17.77 or brighter"*,
z ≤ 0.15, Petrosian radius ≥ 3″. For the study's selected parent, r is directly constrained by
the frozen `flux_r > 0` and `dered_mag_r < 17.7` cuts. Walmsley et al. 2022 separately supports
that the GZ DECaLS NSA parent is primarily r-limited (`m_r = 17.77`), while noting exceptions;
the r-band guarantee here therefore rests on our frozen study cuts, not on a claim that every
GZ DECaLS source is r-limited. **Correction,
carried openly:** my earlier draft described the GZ DECaLS *classification imagery* as
r-dominated; that was wrong — the volunteer images are grz Lupton composites (Walmsley et al.
2022 §2.3). The withdrawn imagery claim is replaced by the frozen-cuts argument above (with the
selection limit as separate support), which is what the band decision actually needs.

**(d) The frozen instrument is already single-channel.** This is deliberately my *last* argument,
not my first: it would be circular to let the built instrument dictate the science requirement.
Given (a)–(c) establish that one band is scientifically sufficient and r is the right one,
conformity with the frozen estimator means the smaller amendment is also the correct one.

**The refreeze trigger, stated so the cheap-answer suspicion has a standing test:** if the R1–R5
rerun on the new input path, the optional HC-1H pilot, or HC-1H itself shows sensitivity below
the HC-5 floors, the outcome is INCONCLUSIVE-BY-POWER — the run does not start — and the
*evidenced* path is then to refreeze the estimator appendix as a three-channel 128×128 instrument
(full retrain on synthetics, new identity witness, new R1–R5), still pre-run, still before any
sky statistic. Under-sensitivity fails loudly; it cannot be papered over.

## 3. The amendment, line by line

*(Targets: PC-1 in the frozen prereg (§6, carrying the 08-12 text by reference) and the input
contract now to be carried by a successor route binding. The 08-12 draft, the 08-14 frozen file,
and the 08-15 frozen file are untouched; Tori's 08-12 route binding receipt is not edited — it is
superseded in its input-contract lines by a successor receipt that Tori issues to match this
contract.)*

**A1 — PC-1 (08-12 frozen text, carried into §6).** Current:
> "**PC-1** Single survey, single cutout route, exact versions (BS-1); checksums and query logs at
> the Mittal–Singal custody standard."
Replacement:
> "**PC-1 (amended 2026-08-15)** Single survey, single cutout route, exact versions (BS-1);
> checksums and query logs at the Mittal–Singal custody standard. The pixel input contract is
> frozen by `LANA_PC1_INPUT_AMENDMENT_20260815.md` §3 A2–A3 (incorporated as frozen text):
> single band r, 128×128, float32, with the delivered raster consumed whole — no reduction,
> resampling, or plane selection step may exist between delivery and tensor."

**A2 — route request parameters (supersedes the corresponding lines of
`TORI_SURVEY_ROUTE_BINDING_20260812.md`; successor receipt required).** Current (route binding,
verbatim):
> "- `bands=grz`: exactly g, r, and z, in that order; i and WISE are not measurement channels;
> - `size=256`: a square 256×256 analysis raster per optical band;"
Replacement:
> "- `bands=r`: exactly and only r; g, z, i and WISE are not measurement channels;
> - `size=128`: a single square 128×128 analysis raster, matching the frozen estimator input
>   exactly — delivered pixels = consumed pixels, no reduction step exists;"
All other route-binding lines carry unchanged: `layer=ls-dr10-south`, `pixscale=0.262`, FITS
only, no post-delivery rotate/reproject/interpolate/resize/WCS transform, delivered FITS planes
in FITS-native row order are the final analysis raster, mirror as byte-exact pixel-index
reversal on that raster only.

**A3 — the input contract (new frozen block; every constant frozen on synthetics only, none
tunable against real images).**
> "**IC-1 Band and plane:** band r only. The delivered product must contain exactly one 2-D image
> plane of shape 128×128; the consumed plane is that plane. If the delivery contains any other
> shape, extra plane, or extra image HDU, the object FAILS CLOSED (logged, excluded by the frozen
> abstention rule — never silently reduced). The exact HDU index of the image plane in the
> service's single-band FITS response is a BINDING SLOT filled by Tori's successor route binding
> from service documentation/a schema probe on a non-science test position, before sky access.
> **IC-2 Units:** pixel values are consumed in the delivered survey units (nanomaggies), with no
> unit conversion before the frozen scaling map.
> **IC-3 Background:** no background estimation or subtraction beyond what the survey pipeline
> already applied to the delivered product. The synthetic training set must include a matching
> background model; that equivalence is part of the R1–R5 rerun, not an assumption.
> **IC-4 Invalid pixels:** NaN/Inf pixels are replaced by 0.0 *after* the scaling map, and the
> invalid fraction is logged per object; an object with invalid fraction above the frozen cap
> (BINDING SLOT, set on synthetics by Yui with the R1–R5 rerun) FAILS CLOSED to abstention.
> **IC-5 Scaling map:** the nanomaggy-to-tensor map is a fixed monotone function with all
> constants frozen (BINDING SLOT: the exact function and constants are pinned by Yui at the
> R1–R5 rerun, chosen and validated on synthetics only, and hash-pinned in the rerun receipt
> before sky access). No per-object, per-stratum, or data-dependent normalization of any kind —
> no percentile stretches, no per-image standardization — because any data-dependent map breaks
> the bit-exact mirror argument (IC-7) and can carry sky structure into sensitivity.
> **IC-6 Number format and layout:** float32, little-endian, C-order (row-major), a single
> channel tensor of shape (1, 128, 128); FITS big-endian source values are converted once at
> ingest.
> **IC-7 Mirror point:** mirror is the pure index reversal on the width axis of the consumed
> raster (np.fliplr semantics), exactly as the estimator appendix HARD RULE freezes it. 128 is
> even, so the flip axis lies between pixel columns 63 and 64 and the operation is an exact
> permutation — no interpolation, no resampling, bit-exact equivariance preserved. The mirror is
> applied in tensor space after IC-1…IC-6, and nowhere else in the χ path."

## 4. Consequences stated, not implied

1. **R1–R5 rerun is a prerequisite to sky access (Kun condition 3).** The synthetic identity,
   retention, and calibration receipts were produced on the old input path. Changing the input
   function invalidates them as evidence about the new instrument-as-consumed: Yui must rerun
   R1–R5 through the **exact** new input function (IC-1…IC-7, byte-identical code path to
   production), fill the IC-4/IC-5 slots on synthetics only, and issue a hash-pinned rerun
   receipt. No sky access before that receipt exists and Kun has gated it.
2. **PC-3 parity and PC-4 fail-closed are conditional carries.** They carry unchanged *only
   while cutting stays on the service*. If cutting ever moves local (e.g., Globus bulk bricks +
   local cutouts), WCS custody transfers onto our code and PC-3/PC-4 must be re-verified against
   the local path — re-verified, not assumed.
3. **The acquisition channel remains unresolved.** The survey discourages bulk automated cutout
   use and points large jobs to Globus; an operator query is pending Duho's decision. **This
   amendment fixes the input contract, not the delivery route.** Approval of this amendment must
   not be read as approval of any delivery mechanism; the route decision arrives separately and
   PC-1's custody standard applies to whichever channel is chosen.
4. **BS-9 note:** the frozen constants table is input-path independent (it is arithmetic on N
   and a), but the *realized* a under the r-band path is measured by HC-1H as designed — nothing
   in this amendment touches the HC-1H protocol.

## 5. Carried unchanged

BS-1 remains **FAILED as written** — nothing here cures or revisits the licence limb. F-10 and
the aggregate-only output boundary, BS-11 and the cumulative-release policy, HC-1H (all floors,
HC-7 triggers), the STOP rule, K-1…K-14, and the canonical boundary sentence carry byte-for-byte:
> **"A null here does not establish that the sky is isotropic; it rejects only Longo's published amplitude at Longo's published axis if the preregistered rejection rule is met."**

## 6. Verification hygiene

**Revision 2 (2026-08-15, per Kun's PASS_PC1_AMENDMENT_FOR_V3_DRAFTING blocker):** no [VERIFY]
markers remain. Each was filled from a primary source with a locator, or the sentence it
supported was deleted: **(1)** extinction coefficients filled from Legacy Surveys DR10
documentation (values quoted verbatim in §2b; Schlafly & Finkbeiner 2011 methodology);
**(2)** arm-contrast ordering filled from Yu, Ho, Barth & Li 2018 (DOI
10.3847/1538-4357/aacb25), abstract quoted; the unquantified magnitude clause was **deleted
rather than filled** — the source's abstract does not quantify it and the argument needs only
the ordering; **(3)** the GZ DECaLS band claim was **corrected, not merely filled**: the
replaced wording *"whose selection and classification imagery is r-dominated"* was wrong about
the imagery (grz Lupton composites, Walmsley et al. 2022 §2.3) and the r-band guarantee now rests
on the study's frozen `flux_r > 0` and `dered_mag_r < 17.7` cuts, with the sourced NSA selection
limit (primarily m_r = 17.77, exceptions noted; §2.2) as separate support. The band decision
stands unchanged on the repaired sources: the parity argument (§2a) never depended on any of
them, and the r choice survives on pinned extinction arithmetic, sourced contrast ordering, and
the frozen study cuts. Nothing in this amendment was tuned against real images; every open constant is a named
BINDING SLOT with a synthetics-only fill rule and a named owner.

**Revision 3 (2026-08-15, per Kun's HOLD_V3_FREEZE_FOR_GZ_DECALS_RATIONALE_REPAIR,
`KUN_V3_FREEZE_GATE_20260815.md`):** the §2(c) sentence "Every parent therefore has secure
r-band flux by construction…" over-claimed — Walmsley et al. 2022 says NSA **primarily**
includes galaxies brighter than m_r = 17.77 and explicitly notes fainter exceptions, so the
source supports an r-limited tendency, not an every-parent guarantee. Replaced with Kun's exact
repair wording: the r-band guarantee rests on the study's frozen `flux_r > 0` and
`dered_mag_r < 17.7` cuts — both re-verified against the frozen documents before resting on them
(`LANA_BS6_PHOTOMETRIC_CUTS_20260814.md` §1–2, cross-checked identical to the frozen Cut-6
definition in its §4; executed in Tori's frozen Cut-chain receipts
`TORI_PARENT_ROW_COUNT_20260812.md` and `TORI_CUT6_INCLINATION_COUNT_20260812.md`) — with
Walmsley as separate supporting tendency. The §2(c) lead sentence, the correction record, and
item (3) above were aligned so no summary states the rationale more strongly than the repair.
The unsourced g-band S/N comparison clause that shared the blocking sentence was dropped rather
than re-sourced — §2(b) already carries g's disadvantages on pinned and sourced grounds. The
band decision is unchanged.

**Nothing in this amendment authorises a fetch, a run, or a release. Kun gates; Duho owns
acceptance.**

— Lana, 2026-08-15.
