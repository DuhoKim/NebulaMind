# Survey Logo/Emblem Audit — Design v1

**Author:** Kun 🔬
**Date:** 2026-06-12 16:52 KST
**Status:** Design — awaiting Papa approval before Tori dispatch
**Live grounding:** 50 survey rows from the live local PostgreSQL-backed NebulaMind DB on Mac Studio; every non-null remote logo URL was live-checked on 2026-06-12 for HTTP 200 and image content type.
**Scope:** All 50 rows of the `surveys` table. Goal: replace the decorative card emoji with each survey's official logo.

---

## 1. Summary

- **41 / 50** surveys have a verified, working logo URL from an official source (survey site or operating agency).
- **9 / 50** are `null` — no findable logo (dead site, pre-web-branding mission, or sub-field with no own identity).
- Every non-null URL was verified live (HTTP 200 + `image/*` content type) on 2026-06-12. No Wikimedia Commons sources were used.
- Quality mix: 3 survey-specific SVGs, ~28 transparent PNGs, 7 opaque JPGs, a few agency-generic fallbacks (flagged).

**Headline recommendation: do NOT hotlink these URLs.** Mirror the images into `frontend/public/survey-logos/` and serve self-hosted (see §4). Reasons:
1. **Mixed content** — `ukidss` and `vipers` are HTTP-only hosts; browsers block HTTP images on an HTTPS page.
2. **Fingerprinted asset paths** — `ngvla`, `roman`, `spherex`, `hst` (esahubble), `jwst` (esawebb) use build-hashed filenames that rotate on site redeploys.
3. **Fragile hosts** — `h-atlas` is already dead; `weave`'s URL requires a long Atlassian query string; several sites 403 generic fetchers.
4. Hotlinking 40+ third-party hosts adds latency and etiquette problems for zero benefit.

---

## 2. Logo URL table

`tier`: **S** = survey-specific logo · **O** = operator logo (identifies the facility, acceptable) · **A** = agency-generic (does not identify the survey — recommend fallback instead, see §6 Q1).
`bg`: rendering hint — `any` = transparent, works on dark card directly · `dark` = white/reversed variant, needs dark background (fine: our theme is dark) · `light` = black variant or opaque JPG, needs a light chip behind it.

| survey | logo_url | source_page | tier | bg | notes |
|---|---|---|---|---|---|
| 2MASS | https://www.ipac.caltech.edu/system/activities/logos/66/original/2mass.png | https://www.ipac.caltech.edu/project/2mass | S | any | PNG 500×300, transparent |
| 4MOST | https://www.4most.eu/static/core/img/4most-logo-300.png | https://www.4most.eu/cms/ | S | any | PNG 300×352, transparent; 4most-survey.org unreachable |
| ACT | null | https://act.princeton.edu/ | — | — | Site 403s all fetchers; Wayback shows text-only header; no logo exists |
| ALMA | https://www.almaobservatory.org/wp-content/themes/alma-v3.0/images/logos/alma-footer-logo.svg | https://www.almaobservatory.org/ | S | any | SVG, official footer logo |
| ASKAP/EMU | https://emu-survey.org/figs/EMU-logo-extra.png | https://emu-survey.org/ | S | any | PNG 780×400, transparent |
| CDF-N | null | https://cxc.harvard.edu/ | — | — | No distinct field logo; Chandra wordmark is the natural fallback (§6 Q2) |
| CDF-S | null | https://cxc.harvard.edu/ | — | — | Same as CDF-N |
| Chandra | https://cxc.harvard.edu/incl/chandra_header.png | https://cxc.harvard.edu/ | S | any | PNG 410×144 wordmark, transparent |
| CMB-S4 | https://cmb-s4.org/wp-content/uploads/sites/4/2024/01/cropped-CMBS4-Logo-Reversed-1.png | https://cmb-s4.org/ | S | dark | White reversed variant — ideal on our dark theme |
| COSMOS2020 | https://cosmos.astro.caltech.edu/assets/cosmos-logo.png | https://cosmos.astro.caltech.edu/ | S | any | PNG 388×141, transparent; mission_url in DB serves an empty stub (§6 Q3) |
| DEEP2 | null | https://deep.ps.uci.edu/ | — | — | Text-only WordPress site; deep2.lbl.gov unreachable; nothing in Wayback |
| DES | https://www.darkenergysurvey.org/wp-content/uploads/2023/11/des-logo-rev-lg.png | https://www.darkenergysurvey.org/ | S | dark | White reversed variant, PNG 822×156; non-reversed 404s |
| DESI | https://data.desi.lbl.gov/doc/img/desilogo.jpg | https://data.desi.lbl.gov/doc/ | S | light | JPG (opaque); only static logo found — desisurvey.org unreachable |
| ELT | https://elt.eso.org/public/archives/djp/elt-assets/img/eso_logo_transparent.png | https://elt.eso.org/ | A | any | Generic ESO logo — no ELT-specific emblem exists |
| eROSITA | https://erosita.mpe.mpg.de/images/eROSITA_Logo_RGB.png | https://erosita.mpe.mpg.de/ | S | any | PNG RGBA, official |
| Euclid | https://www.euclid-ec.org/wp-content/uploads/cropped-EC_logos_official_black-2.png | https://www.euclid-ec.org/ | S | light | Euclid Consortium black variant, 1732px — needs light chip on dark theme |
| Fermi-LAT | https://fermi.gsfc.nasa.gov/inc/img/nasa-logo.svg | https://fermi.gsfc.nasa.gov/ | A | any | NASA meatball only — no mission logo anywhere on fermi.gsfc.nasa.gov |
| Gaia | https://www.cosmos.esa.int/documents/29201/29222/Gaia+Archive+logo.png/167275a5-9577-4d20-b0e0-a97625a73e0b?t=1469109633000 | https://www.cosmos.esa.int/web/gaia | S | any | "Gaia Archive" logo, not a mission insignia — closest official Gaia mark (§6 Q4) |
| GALEX | https://www.galex.caltech.edu/images/galexlogo.jpg | https://www.galex.caltech.edu/ | S | light | JPG wordmark banner 525×75, opaque |
| GAMA | https://www.gama-survey.org/gallery/logos/images/GAMA_logo_blue.png | https://www.gama-survey.org/gallery/logos/ | S | any | Dedicated logos gallery; green/pink variants in same dir |
| H-ATLAS | null | http://www.h-atlas.org/ | — | — | Host dead (connect timeout); Wayback homepage had no logo either |
| HETDEX | https://hetdex.org/wp-content/themes/MDO/images/logo.svg | https://hetdex.org/ | S | any | SVG, official header logo |
| HIPASS | https://www.atnf.csiro.au/wp-content/plugins/nba-plugin-block-header/assets/images/csiro-logo.svg | https://www.atnf.csiro.au/ | A | any | Generic CSIRO logo — 1990s-era survey pages have no logo |
| HSC | https://hsc.mtk.nao.ac.jp/ssp/wp-content/uploads/2016/03/hsc_ssp.png | https://hsc.mtk.nao.ac.jp/ssp/ | S | any | PNG RGBA, official SSP header |
| HST | https://esahubble.org/assets/images/logo.9ab14af4d8f2.png | https://esahubble.org/ | O | any | ESA/Hubble outreach logo; nasa.gov/hubble has only NASA meatball; hashed filename |
| JWST | https://esawebb.org/assets/images/esa-jwst-logo.png | https://esawebb.org/ | O | any | ESA/Webb outreach logo, transparent; nasa.gov/jwst has only NASA meatball |
| KiDS | https://kids.strw.leidenuniv.nl/images/header2.png | https://kids.strw.leidenuniv.nl/ | S | any | Header wordmark banner 850×150, transparent; no standalone logo on site |
| LOFAR | https://www.lofar.eu/wp-content/uploads/2021/02/logo-w720-margin-2.png | https://www.lofar.eu/ | S | any | PNG transparent, official ILT site |
| MeerKAT | https://www.sarao.ac.za/wp-content/uploads/2020/10/sarao_logo.png | https://www.sarao.ac.za/science/meerkat/ | O | any | SARAO operator logo — no MeerKAT-specific logo on page |
| ngVLA | https://ngvla.nrao.edu/assets/ngvla_full_logo-e4f5dbcdabcc9ad37aec068a7624acfd59738508037c51d2b4e70abb79e1f629.png | https://ngvla.nrao.edu/ | S | any | PNG transparent; fingerprinted asset path |
| Pan-STARRS | https://panstarrs.ifa.hawaii.edu/images/pan-starrs_logo1.png | https://panstarrs.ifa.hawaii.edu/ | S | any | PNG transparent; white/silver variants in same dir |
| PFS | https://pfs.ipmu.jp/images/logo-pfs.png | https://pfs.ipmu.jp/ | S | any | PNG transparent, official header |
| Planck | https://www.cosmos.esa.int/documents/387566/387639/Planck_red_sm.jpg/227f9b45-ff80-40ff-b70b-d15d4445131a?t=1406903688941 | https://www.cosmos.esa.int/web/planck | S | light | Red Planck wordmark, JPG opaque |
| Roman | https://roman.ipac.caltech.edu/assets/roman_logo-220aca95c59aae902c4c6e58ce32050e354328361cdd1d0a2584063fb8e64e1e.png | https://roman.ipac.caltech.edu/ | S | any | PNG transparent; roman.gsfc.nasa.gov now redirects to science.nasa.gov; fingerprinted path |
| ROSAT | null | https://www.mpe.mpg.de/ROSAT/ | — | — | Pre-web-branding mission; MPE/HEASARC have only photo banners |
| Rubin/LSST | https://www.lsst.org/sites/default/files/Rubin-NSF-DOE%20triad%20-%20Horizontal%20-%20Use%20me%20over%20dark%20backgrounds%20-%20RGB.png | https://www.lsst.org/ | S | dark | Official "use over dark backgrounds" triad, 3201×477 — ideal for our theme |
| SDSS | https://www.sdss.org/wp-content/uploads/2022/09/sdss-new-logo-72dpi.png | https://www.sdss.org/ | S | any | 2022 redesign logo, transparent |
| SDSS-V | https://www.sdss.org/wp-content/uploads/2022/09/sdss-new-logo-72dpi.png | https://www.sdss.org/ | S | any | Same file — sdss.org IS the SDSS-V site; no separate "-V" variant exists (§6 Q5) |
| SKA Phase 1 | https://www.skao.int/themes/custom/ska/assets/images/logo-color.svg | https://www.skao.int/ | S | any | SVG color variant; white variant at /logo-dia.svg |
| SPHEREx | https://spherex.caltech.edu/assets/spherex_logo-9fad8e49075ac91fb1b747d217517023fd5bf3d121c5022d78a71966ff75b6ce.png | https://spherex.caltech.edu/ | S | any | PNG 1950×1950 transparent; fingerprinted path |
| SPT | null | https://pole.uchicago.edu/ | — | — | Google Site with one telescope photo; no logo on LAMBDA or Commons either |
| UKIDSS | http://www.ukidss.org/images/ukidsslogo5.jpg | http://www.ukidss.org/ | S | light | JPG 800×100 banner, opaque; **HTTP-only host** — must mirror |
| UNIONS | https://www.skysurvey.cc/wp-content/uploads/2022/04/UNIONS-Logo-TextBlack-1K.png | https://www.skysurvey.cc/ | S | light | PNG transparent but black text — needs light chip on dark theme |
| VIKING | null | https://www.eso.org/sci/observing/phase3/data_releases/viking_dr5.html | — | — | ESO data-release page has only generic ESO chrome; no VIKING logo exists |
| VIPERS | http://vipers.inaf.it/images/Banner.jpg | http://vipers.inaf.it/ | S | light | Masthead JPG containing the logo (no standalone file); **HTTP-only host** — must mirror |
| VLA | https://public.nrao.edu/wp-content/themes/nrao/img/NRAO_logo_text.png | https://public.nrao.edu/telescopes/vla/ | O | any | NRAO operator logo — no VLA-specific logo on page |
| WEAVE | https://weave-project.atlassian.net/wiki/download/attachments/115376155/WEAVE?version=4&modificationDate=1726652531777&cacheVersion=1&api=v2 | https://weave-project.atlassian.net/wiki/spaces/WEAVE/ | S | any | PNG 200×200 transparent, project wiki space icon; long query string required — must mirror |
| WISE | https://wise.ssl.berkeley.edu/images/wise_logo.jpg | https://wise.ssl.berkeley.edu/ | S | light | JPG 160×83, opaque, small — no larger static variant exists |
| XMM-Newton | https://www.esa.int/var/esa/storage/images/esa_multimedia/images/2013/06/xmm-newton_mission_logo/12863796-1-eng-GB/XMM-Newton_mission_logo.jpg | https://www.esa.int/ESA_Multimedia/Images/2013/06/XMM-Newton_mission_logo | S | light | ESA mission logo, JPG opaque |
| zCOSMOS | null | https://www.eso.org/sci/activities/garching/projects/zcosmos/ | — | — | Old ESO project page, generic chrome only |

**Tier counts:** S = 34 · O = 4 (HST, JWST, MeerKAT, VLA) · A = 3 (ELT, Fermi-LAT, HIPASS) · null = 9 (ACT, CDF-N, CDF-S, DEEP2, H-ATLAS, ROSAT, SPT, VIKING, zCOSMOS).
(O-tier is 4 entries: HST, JWST, MeerKAT, VLA. The ESA outreach logos for HST/JWST do name the mission, so they sit at the strong end of O.)

---

## 3. Risk register

| Risk | Affected | Mitigation |
|---|---|---|
| Mixed-content block (HTTP image on HTTPS page) | UKIDSS, VIPERS | Mirror (§4) — never hotlink |
| Build-fingerprinted URLs rotate | ngVLA, Roman, SPHEREx, HST, JWST | Mirror; keep `logo_source_page` for re-fetch |
| Host death / 403s | H-ATLAS (dead), ACT (403), WEAVE (Atlassian query string) | Mirror; the audit table is the provenance record |
| Black-variant logos invisible on `#0f172a` | Euclid, UNIONS (+ all opaque JPGs) | `logo_bg='light'` hint → render on light chip (§5) |
| White-reversed logos invisible on light surfaces | CMB-S4, DES, Rubin | `logo_bg='dark'`; our theme is dark so these render directly — but never place on white |
| Agency-generic logos mislabel the survey | Fermi-LAT (NASA), ELT (ESO), HIPASS (CSIRO) | Recommend demoting to fallback (§6 Q1) |

---

## 4. Schema change + mirroring

### 4.1 Schema (3 columns, one ALTER)

```sql
ALTER TABLE surveys
  ADD COLUMN logo_url         text,          -- what the frontend renders, e.g. /survey-logos/desi.png (self-hosted)
  ADD COLUMN logo_source_page text,          -- provenance: official page the logo came from (re-fetch anchor)
  ADD COLUMN logo_bg          varchar(8);    -- 'any' | 'dark' | 'light' | NULL (NULL = no logo, use fallback)
```

- `logo_url` holds the **local mirrored path**, not the remote URL. Remote URLs live in this doc + `logo_source_page`.
- No NOT NULL constraints: 9 surveys are legitimately null and the fallback is a UI concern.
- `logo_bg` drives the chip treatment in §5. Single source of truth in DB so the API needs no logic.

### 4.2 Mirroring step (Tori, one-shot script)

`backend/scripts/mirror_survey_logos.py`:
1. Embed the §2 table (slug → remote URL, bg hint) as a dict.
2. Download each remote URL → `frontend/public/survey-logos/{slug}.{ext}` (keep original format; sanitize ext from content-type, not URL — the WEAVE URL has no extension).
3. `UPDATE surveys SET logo_url='/survey-logos/{slug}.{ext}', logo_source_page=..., logo_bg=...` per row.
4. Print a verification table: slug, bytes, content-type, DB row updated.
- SVGs served as-is (they're from trusted official hosts, but ensure they're static — strip `<script>` if paranoid; the three SVGs here are plain vector data).
- Idempotent: re-running overwrites files and re-issues UPDATEs.

API: the surveys list endpoint must include the three new columns in its payload (additive, non-breaking).

---

## 5. UI card spec (Tori)

Applies to the survey card in the Surveys tab (post-overhaul `SurveyCard` from `Design_SurveysTab_Overhaul_v1.md`; if executing before that lands, same change applies to the Directory card in `SurveysView.tsx`).

### 5.1 Logo slot replaces emoji

- Replace the decorative lead emoji with a fixed logo slot: **48×48px on cards** (height-constrained `max-h-12`, `object-contain`, width free up to ~96px for wordmark-shaped logos), 20–24px height in the SurveyPeek/detail header.
- Render rules by `logo_bg`:
  - `any` / `dark` → `<img>` directly on the card panel (`#1e293b`). No chip.
  - `light` → wrap in a light chip: rounded-md, `background: #e2e8f0`, 4px padding. Opaque JPGs get the same chip so their white boxes read as intentional.
- `alt={name + " logo"}`, `loading="lazy"`, `onError` → swap to fallback (defensive: mirrored files make this rare).

### 5.2 Fallback (9 null surveys + onError)

Colored-initial tile, no new assets:
- 48×48 rounded-md tile, `background:` band color at ~20% opacity, 1px border in band color, survey initials (first 2–4 chars of `name`, e.g. "ACT", "SPT", "CDF") in band color, font-semibold.
- Band colors: reuse the Band Spectrum Strip palette from the Surveys overhaul (single source of truth — import, don't redefine).
- This intentionally looks different from a logo: it signals "no official emblem," not "image failed to load."

### 5.3 Out of scope (do-not-touch)

- Trust-level styling (just shipped), idea chips/toggle, Chart/plot components, FilterSheet.
- No backend model changes beyond the 3 columns; no changes to `emoji` column (leave data in place; UI simply stops rendering it on cards).

### 5.4 Acceptance criteria

1. Cold-load `/surveys`: ≥41 cards show a real logo image; zero broken-image icons.
2. UKIDSS and VIPERS logos load over HTTPS (proof that mirroring, not hotlinking, is in effect — check the network tab shows only same-origin `/survey-logos/*` requests).
3. Euclid and UNIONS logos are legible (light chip present); CMB-S4, DES, Rubin legible directly on the dark card.
4. The 9 null surveys (ACT, CDF-N, CDF-S, DEEP2, H-ATLAS, ROSAT, SPT, VIKING, zCOSMOS) show the band-colored initial tile — not an empty slot, not the old emoji.
5. SurveyPeek/detail header shows the same logo at reduced height.
6. Lighthouse/layout: no CLS from logo loads (fixed slot dimensions).

---

## 6. Open questions for Papa (non-blocking except Q1)

1. **Agency-generic logos (Fermi-LAT→NASA meatball, ELT→ESO, HIPASS→CSIRO):** my recommendation is to **demote these 3 to the initials fallback** — a NASA logo on the Fermi card identifies the agency, not the survey, and dilutes the system. Operator logos that effectively brand the facility (SARAO/MeerKAT, NRAO/VLA, ESA outreach Hubble/Webb marks) I'd keep. Default in the spec: demoted.
2. **CDF-N / CDF-S:** reuse the Chandra wordmark (they're Chandra fields) or initials fallback? Default: initials fallback — two identical Chandra logos next to the real Chandra card is confusing.
3. **COSMOS2020 source drift:** the DB `mission_url` (cosmos.ipac.caltech.edu) serves an empty stub; the live site is cosmos.astro.caltech.edu. Recommend a separate one-line data fix to `mission_url`.
4. **Gaia:** the only official Gaia-branded mark on the ESA site is the *Archive* logo. Acceptable, or prefer initials fallback? Default: use it.
5. **SDSS vs SDSS-V** share one logo file (sdss.org is the SDSS-V site). Acceptable duplication? Default: yes — mirror once, point both rows at the same file.

---

## 7. Execution order for Tori

1. Migration: ALTER TABLE (§4.1) + API payload addition.
2. `mirror_survey_logos.py` run on Mac Studio (local — backend + frontend share the repo here); verify 41 files land in `frontend/public/survey-logos/`.
3. UI: logo slot + chip + fallback tile (§5).
4. Acceptance pass (§5.4), screenshot to HwaO.

Estimated risk: low. Additive schema, additive API field, one UI slot swap, fully reversible (drop columns, delete dir).
