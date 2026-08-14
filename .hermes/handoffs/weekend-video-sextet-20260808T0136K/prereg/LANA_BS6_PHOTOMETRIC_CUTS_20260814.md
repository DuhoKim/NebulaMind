# BS-6 — Photometric cut constants (fill receipt)

**Lana + Tori slot; Lana drafting, 2026-08-14. Fills Binding Slot BS-6 of
`PREREG_LONGO_AMPLITUDE_TEST_20260812.md`.** Documentation work only — no real-sky data, no object rows, no
label distributions consulted. **Not published, accepted, run, committed, or pushed. Kun gates; Duho decides.**

Bound survey (BS-1, Tori custody): **DESI Legacy Imaging Surveys DR10.1 South** (`ls_dr10.tractor_s` sweeps +
`ls_dr10.photo_z`), per `TORI_SURVEY_ROUTE_BINDING_20260812.md` (SHA-256 `3f41b6d9…`) and
`TORI_BS1_CLOSURE_PACKET.md`.

## 1. The photometric cut constants (mag / size / SB)
Each constant is expressed in a named DR10 catalog column whose definition/units are quoted from the Legacy
Surveys DR10 catalog documentation (`legacysurvey.org/dr10/catalogs/`, retrieved 2026-08-14):

| Kind | Cut | Column (verbatim doc definition · units) |
|---|---|---|
| **Magnitude** | **`dered_mag_r < 17.7`** | `FLUX_R` = *"model flux in r"*, units **nanomaggy**; `MW_TRANSMISSION_R` = *"Galactic transmission in r filter in linear units [0,1]"*. Dereddened magnitude = `22.5 − 2.5·log₁₀(FLUX_R / MW_TRANSMISSION_R)` (Legacy Surveys nanomaggy zeropoint 22.5). |
| **Size** | **`shape_r > 1.5`** (arcsec) | `SHAPE_R` = *"Half-light radius of galaxy model for galaxy type `type` (>0)"*, units **arcsec**. |
| **Surface brightness** | **none** (see §3 flag) | — no SB column enters the frozen definition. |

**Survey-documentation rationale (not label-derived):** the size cut `shape_r > 1.5″` keeps sources
well-resolved against DECam imaging (0.262″/pix; typical seeing ≈ 1.0–1.3″), and the bright cut
`dered_mag_r < 17.7` sits far above DR10 depth (r ≈ 23–24), i.e. the high-completeness / reliable-shape regime
described in the survey documentation. **The specific threshold values (17.7, 1.5″) are fixed science choices
frozen in the Cut chain — they are NOT read off any label distribution (not our classifier's behaviour, not
any morphology catalogue's completeness).** This is the distinction BS-6's fill rule requires.

## 2. Supporting (non-photometric) cuts in the same frozen chain — for completeness, cited to docs
These are not "mag/size/SB" constants but are part of the frozen parent definition; each is a documented DR10
column, none a chirality/morphology label:
- `brick_primary = 1` — *"True if the object is within the brick boundary"* (unique-deblend selection).
- `maskbits = 0` — *"Bitwise mask indicating that an object touches a pixel in the coadd …maskbits maps"* (=0 ⟹ untouched).
- `type <> 'PSF'` — `TYPE` = *"Morphological model: 'PSF'=stellar, 'REX'=round exponential galaxy, 'DEV'=deVauc, 'EXP'=exponential, 'SER'=Sersic, 'DUP'=Gaia source…"*; **automated Tractor pipeline source-model classification (star/galaxy separation), not a visual/human morphology label** — see §3 disclosure.
- `flux_r > 0` — positive r-band model flux.
- photo-z join + `0 ≤ z_phot_median < 0.15` — `Z_PHOT_MEDIAN` from `ls_dr10.photo_z`.
- inclination `POWER(shape_e1,2)+POWER(shape_e2,2) < 0.1836734693877551` (⟺ `b/a > 0.4`, **frozen in prereg
  I-5**, not a BS-6 free constant) — `SHAPE_E1/E2` = *"Ellipticity component 1/2 of galaxy model"*.

## 3. Two disclosures carried openly (not silently harmonised)
- **(a) No surface-brightness cut exists** in the frozen definition. BS-6's "SB range" is therefore **empty by
  design** — a documented absence, not an omission. If the gate wants an SB cut, that is a **design change**,
  not something BS-6 may invent; I do not add one.
- **(b) `type <> 'PSF'` is a judgment call I surface rather than bury.** It is the survey's **automated
  source-type** used for star/galaxy separation (point-source vs extended), documented as a Tractor model
  classification — **not** a chirality label and **not** a human/visual or Galaxy-Zoo morphology flag (which
  I-5 forbids). I read it as **permitted**, but I flag it explicitly for Kun/Tori: it is a morphological
  *source-type* column, so its admissibility is a gate decision, disclosed, not assumed.

## 4. Cross-check against the frozen Cut-6 definition (832,393 dered parent) — no disagreement
Frozen chain from `TORI_BS1_CLOSURE_PACKET.md` §2 (full-keyspace certificate SHA-256 `9d629607…`; dered Cut-6
= **832,393**) and `TORI_CUT6_INCLINATION_COUNT_20260812.md` (SHA-256 `ed6b6e5e…`):

| BS-6 constant | Frozen chain value | Agree? |
|---|---|---|
| `dered_mag_r < 17.7` | Cut 4 dered: `dered_mag_r < 17.7` | ✔ identical |
| `shape_r > 1.5` | Cut 5: `shape_r > 1.5` | ✔ identical |
| SB cut | (absent) | ✔ identical (none in either) |

**No disagreement to flag.** The BS-6 photometric constants are byte-for-byte the Cut-4 / Cut-5 predicates that
produced the frozen 832,393 dered parent count; nothing is harmonised or restated with a changed value.

## 5. Validity check (BS-6 range: "cuts cite survey docs; no cut references any chirality or morphology label")
- Every cut column is cited to DR10 survey documentation with verbatim definitions. ✔
- No threshold is derived from a label distribution (classifier or morphology-catalogue behaviour). ✔
- **No cut references any chirality label.** ✔
- **No cut references a human/visual morphology label.** ✔ — with the **disclosed** judgment that
  `type <> 'PSF'` is an automated source-type (star/galaxy separation), not such a label (§3b).
**BS-6 PASSES its validity range as written**, contingent on Kun accepting the §3b reading of `type` and the
§3a documented absence of an SB cut. Both are surfaced for the gate; **nothing is tuned to force the pass**, and
if Kun rules `type` inadmissible or an SB cut required, BS-6 returns to design (an honest, useful outcome).

## Custody / boundary
sample rows exported: 0 · positions: 0 · images: 0 · label distributions consulted: 0 · sky statistics: 0 ·
bulk downloads: 0 · publication/acceptance/commit/push: 0. Sources: Legacy Surveys DR10 catalog docs
(retrieved 2026-08-14); Tori's frozen Cut-chain receipts (hashes above). Tori co-owns; she binds the exact doc
version/URL snapshot at freeze. Back to Kun to gate. — Lana, 2026-08-14.
