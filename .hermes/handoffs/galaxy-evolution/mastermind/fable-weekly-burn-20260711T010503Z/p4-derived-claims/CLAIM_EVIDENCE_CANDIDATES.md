FABLE_BURN_P4_CLAIM_EVIDENCE_CANDIDATES_20260711T010503Z

# Derived claim/evidence candidates from the clean cycle-5 package (RP-1 flagship + supplement)

**OFFLINE CANDIDATES — NOT PUBLISHED, NOT INTEGRATED.** Nothing in this file has been written to the DB, the API, the live wiki, or the runner's `candidates/` tree. Every numeral in claim text and evidence quotes is carried **verbatim from cycle 5** per `p1-rp1-invariants/INVARIANT_MANIFEST.json` (105 entries; character-for-character, never re-derived, never re-rounded). The **association-only wording contract** applies throughout: no "establishes"/"demonstrates"/"proves", no causal phrasing; RP-1's scope caveats (association-only, morphology-uncontrolled, fiber-centered, selection-limited, non-volume-complete) are carried wherever a claim would otherwise overread.

## Provenance (snapshots used for all line references)

| Source | Snapshot | sha256 (verified = cycle-5 originals) |
|---|---|---|
| `cycle_05_package/flagship_rp1/aastex/rp1_flagship_polished.tex` | `sources-snapshot/rp1_flagship_polished.tex` | `63b3920e158ba3be3a78ac0fcf771a979ccf43afe1a8759eda921e1f35ae9384` |
| `cycle_05_package/supplementary_denominator_atlas/aastex/supplementary_denominator_atlas.tex` | `sources-snapshot/supplementary_denominator_atlas.tex` | `a4e3d66c5d4fdffe969d5520636f89d963beece6f44246dd68aa3e98673cdc71` |
| `p1-rp1-invariants/INVARIANT_MANIFEST.json` | read in place (read-only) | `f4eb857e8cc2002208b1d89a8c517d30e044ed5f7c08a3dab976c0bd7556c717` |
| `p1-rp1-invariants/INTRODUCTION_LITERATURE_REFERENCE.md` | read in place (read-only) | `874794a1ea1202ceebace131ce31d46fd9587d6aedde9db1e600ae9cfe07713d` |

Snapshot hashes equal the cycle-5 originals, so snapshot line numbers are identical to cycle-5 line anchors. `FLG` = flagship tex, `SUP` = supplement tex.

## Conventions

- **Numeral scope.** Manifest-checked numerals are those inside `claim_text` and quoted evidence spans. File metadata (candidate ids, line anchors, timestamps, sha256 hashes, marker strings) is staging metadata, not manuscript/wiki prose, and is outside the manifest rule. Identifier digits (RP-1, DR17 as release id, unit notation like erg/s) follow the manifest's stated exclusions; `DR17` is itself manifest-covered (FLG-DR17/SUP-DR17).
- **LaTeX escapes.** Evidence quotes are byte-verbatim from the tex (e.g. `95\%`, `S/N$\geq3$`, `1.2--6.5`, `8{,}146`, `0.032 +/- 0.004`). Where `claim_text` renders these in plain text (95%, S/N≥3), the digits are identical character-for-character; only LaTeX markup is stripped. Range dashes `--` and interval strings `[-1.334,-1.283]`, `0.005-0.729` are carried exactly as in cycle 5.
- **Known rounding anomalies (manifest `known_rounding_anomalies`).** The FLG-CI95 upper bound is canonically `-1.283`; the nearest-rounded artifact variant must NOT be used (cycles 6/7 died on re-typed/re-derived numbers). No candidate below re-derives any value from artifacts.
- **Wiki shaping.** Per `wiki_schema.md` (working-tree file, observed sha256 `d1c04e1fcf1e9b412712d07407c42fccffcf12b5a2fc2eced59dba888594b5dd`): each candidate carries a proposed category (all `galaxy`), target page slug (`/wiki/...` format), target section (schema's required article structure), and ≥3 `see_also` cross-links. All DB-resident fields (ids, foreign keys, publish state) are explicit `OFFLINE_PLACEHOLDER` values — never real DB values. On integration (separately gated), the schema's attribution note applies, e.g. *[Written from an observational astronomy perspective by {model_name}]*.
- **Reference lines (schema `## References` format), shared by all candidates:**
  - [S1] NebulaMind Research Autopilot (2026). Broad Optical BPT Galaxies and Catalog Specific Star Formation in SDSS DR17: A Selection-Aware Pilot Matched-Control Study. Offline cycle-5 candidate manuscript (unpublished). DOI: OFFLINE_PLACEHOLDER
  - [S2] NebulaMind Research Autopilot (2026). Supplementary SDSS Denominator and Proxy Atlas for Galaxy-Evolution Follow-up. Offline cycle-5 candidate manuscript (unpublished). DOI: OFFLINE_PLACEHOLDER
  - Custody run families (named in cycle 5): `SDSS_AGN_SFR_PILOT_20260708T122000Z` (flagship result), `SDSS_REMAINING_TOPIC_PILOTS_20260708T125828Z` (eight atlas artifacts).

---

## P4-C01 — Flagship headline: matched-control catalog-sSFR offset (preferred estimate)

```
candidate_id: P4-C01
wiki_shape:
  page_id: OFFLINE_PLACEHOLDER
  claim_id: OFFLINE_PLACEHOLDER
  evidence_ids: OFFLINE_PLACEHOLDER
  page_version_fk: OFFLINE_PLACEHOLDER
  publish_state: OFFLINE_PLACEHOLDER
  category: galaxy
  proposed_page_slug: /wiki/active-galactic-nuclei
  proposed_section: Current Research
  see_also: [/wiki/galaxy-formation, /wiki/quasars, /wiki/stellar-evolution]
  references: [S1]
```

**claim_text:** In a selection-aware SDSS DR17 matched-control pilot (RP-1), broad optical BPT-selected galaxies are associated with a lower catalog median sSFR proxy than star-forming controls matched in stellar mass and redshift only: the preferred custody-backed comparison yields 8,146 pairs and a median Δlog sSFR (target minus matched control) of -1.309 dex, with a bootstrap 95% confidence interval of [-1.334,-1.283] dex. This is a fiber-centered, morphology-uncontrolled association inside a non-volume-complete, sequentially capped 60,000-galaxy optical cache — not a causal feedback, physical-quenching, gas-depletion, or population-abundance measurement.

**evidence:**
1. `flagship_rp1/aastex/rp1_flagship_polished.tex`, snapshot line 13 (abstract): "Broad optical BPT-selected galaxies are matched to star-forming controls in stellar mass and redshift only; the preferred custody-backed comparison yields 8,146 pairs and a median $\Delta\log {\rm sSFR}$ of -1.309 dex, with a bootstrap 95\% confidence interval of [-1.334,-1.283] dex." — manifest: FLG-8146, FLG-MEDIAN-OFFSET, FLG-CI95, FLG-CI-LEVEL.
2. `flagship_rp1/aastex/rp1_flagship_polished.tex`, snapshot line 57 (Table 1 row, carried as one string): `Broad optical BPT-selected targets, S/N$\geq3$, nearest SF control with replacement & 8,146 & -1.309 & [-1.334,-1.283] & Preferred association estimate \\` — manifest: FLG-ROW-057 (whole row), FLG-SNCUT, FLG-8146, FLG-MEDIAN-OFFSET, FLG-CI95.
3. `flagship_rp1/aastex/rp1_flagship_polished.tex`, snapshot line 74 (conclusion): "Its provenance-retained result is the preferred 8,146-pair, -1.309 dex offset with bootstrap 95\% interval [-1.334,-1.283] dex." — manifest: FLG-8146, FLG-MEDIAN-OFFSET, FLG-CI-LEVEL, FLG-CI95.

**numerals_check:** 8,146 ↔ FLG-8146 `8,146` MATCH; -1.309 ↔ FLG-MEDIAN-OFFSET `-1.309` MATCH; [-1.334,-1.283] ↔ FLG-CI95 `[-1.334,-1.283]` MATCH (audit-canonical string; rounding anomaly noted in manifest — carried verbatim, not re-derived); 95% ↔ FLG-CI-LEVEL `95\%` MATCH (digits identical, LaTeX `\%` rendered); 60,000 ↔ FLG-60000 `60,000` MATCH; DR17 ↔ FLG-DR17 `DR17` MATCH. Zero unmatched numerals.

**caveats:** Association-only; morphology-uncontrolled; fiber-centered (3-arcsec fiber); non-volume-complete sequentially capped cache; result conditional on the optical emission-line denominator; traced to `SDSS_AGN_SFR_PILOT_20260708T122000Z` custody artifacts.

**verification:** LOCAL_ONLY

---

## P4-C02 — Flagship denominator census (BPT class counts)

```
candidate_id: P4-C02
wiki_shape:
  page_id: OFFLINE_PLACEHOLDER
  claim_id: OFFLINE_PLACEHOLDER
  evidence_ids: OFFLINE_PLACEHOLDER
  page_version_fk: OFFLINE_PLACEHOLDER
  publish_state: OFFLINE_PLACEHOLDER
  category: galaxy
  proposed_page_slug: /wiki/active-galactic-nuclei
  proposed_section: Physical Properties
  see_also: [/wiki/galaxy-formation, /wiki/quasars, /wiki/interstellar-medium]
  references: [S1]
```

**claim_text:** The custody-backed analysis denominator of the RP-1 pilot contains 39,553 star-forming galaxies, 12,234 intermediate/composite galaxies, 8,146 broad optical BPT-selected targets, and 67 unclassified objects, within a fixed 60,000-galaxy SDSS DR17 optical-emission-line cache. These counts are conditional on the optical selection (strict four-line S/N cut, sequential specObjID cap) and are not population-complete.

**evidence:**
1. `flagship_rp1/aastex/rp1_flagship_polished.tex`, snapshot line 39: "The custody-backed analysis denominator contains 39,553 star-forming galaxies, 12,234 intermediate/composite galaxies, 8,146 broad optical BPT-selected targets, and 67 unclassified objects." — manifest: FLG-SF, FLG-COMP, FLG-8146, FLG-UNCLASS.
2. `flagship_rp1/aastex/rp1_flagship_polished.tex`, snapshot line 31: "The retained pilot analysis sample is a fixed 60,000-galaxy subset selected sequentially by \texttt{specObjID}." — manifest: FLG-60000.

**numerals_check:** 39,553 ↔ FLG-SF `39,553` MATCH; 12,234 ↔ FLG-COMP `12,234` MATCH; 8,146 ↔ FLG-8146 `8,146` MATCH; 67 ↔ FLG-UNCLASS `67` MATCH (numeric_token); 60,000 ↔ FLG-60000 `60,000` MATCH; DR17 ↔ FLG-DR17 MATCH. Zero unmatched numerals ("four-line" is spelled-out prose, manifest-excluded).

**caveats:** Counts are denominator-conditional, not a volume-complete census; intermediate/composite galaxies are retained in denominator counts but excluded from the star-forming control pool; the 67 unclassified objects do not enter the 8,146-pair estimate.

**verification:** LOCAL_ONLY

---

## P4-C03 — Flagship matching quality (coverage and separations)

```
candidate_id: P4-C03
wiki_shape:
  page_id: OFFLINE_PLACEHOLDER
  claim_id: OFFLINE_PLACEHOLDER
  evidence_ids: OFFLINE_PLACEHOLDER
  page_version_fk: OFFLINE_PLACEHOLDER
  publish_state: OFFLINE_PLACEHOLDER
  category: galaxy
  proposed_page_slug: /wiki/active-galactic-nuclei
  proposed_section: Current Research
  see_also: [/wiki/galaxy-formation, /wiki/quasars, /wiki/galaxy-clusters]
  references: [S1]
```

**claim_text:** RP-1's preferred matched comparison attains 100% target coverage (8,146 of 8,146 targets matched) using variance-normalized Euclidean nearest-neighbor matching in standardized (log M*, z) space with replacement and no mass–redshift caliper; the unrestricted match has median absolute separations of 0.0045 dex in log M* and 0.00021 in redshift. Matching is in stellar mass and redshift only, so the association still inherits any mismatch in structure or fiber coverage between the two populations.

**evidence:**
1. `flagship_rp1/aastex/rp1_flagship_polished.tex`, snapshot line 39: "In the preferred estimate, this yields 100\% target coverage (8,146 of 8,146 targets matched), and the unrestricted Euclidean match has median absolute separations of 0.0045 dex in $\log M_\star$ and 0.00021 in redshift, so the association still inherits any mismatch in structure or fiber coverage between the two populations." — manifest: FLG-COVERAGE-PCT, FLG-8146, FLG-SEP-LOGM, FLG-SEP-Z.

**numerals_check:** 100% ↔ FLG-COVERAGE-PCT `100\%` MATCH (digits identical, LaTeX `\%` rendered); 8,146 (×2) ↔ FLG-8146 `8,146` MATCH; 0.0045 ↔ FLG-SEP-LOGM `0.0045` MATCH; 0.00021 ↔ FLG-SEP-Z `0.00021` MATCH. Zero unmatched numerals ("two variables" spelled out, manifest-excluded).

**caveats:** No caliper is imposed (deliberate, to cover all 8,146 custody-backed targets); matching excludes morphology, aperture fraction, halo mass, gas mass, accretion-luminosity proxy, and duty-cycle phase — these are follow-up requirements.

**verification:** LOCAL_ONLY

---

## P4-C04 — Flagship selection context (parent count and cache coverage)

```
candidate_id: P4-C04
wiki_shape:
  page_id: OFFLINE_PLACEHOLDER
  claim_id: OFFLINE_PLACEHOLDER
  evidence_ids: OFFLINE_PLACEHOLDER
  page_version_fk: OFFLINE_PLACEHOLDER
  publish_state: OFFLINE_PLACEHOLDER
  category: galaxy
  proposed_page_slug: /wiki/active-galactic-nuclei
  proposed_section: Open Questions
  see_also: [/wiki/galaxy-formation, /wiki/milky-way, /wiki/quasars]
  references: [S1]
```

**claim_text:** RP-1's analysis sample is a fixed 60,000-galaxy subset of SDSS DR17 selected sequentially by specObjID. The strict public four-line S/N≥3 eligible parent count of 249,917 galaxies, and the corresponding 24.0% cache coverage, are selection-context diagnostics rather than custody-backed independent result rows. Because specObjID ordering follows SDSS targeting and plate/MJD bookkeeping, the subset is non-random and carries survey-plate and sky-coverage bias; it supports no absolute volume densities, luminosity functions, or population-normalized abundances.

**evidence:**
1. `flagship_rp1/aastex/rp1_flagship_polished.tex`, snapshot line 31: "The strict public four-line S/N$\geq3$ eligible parent count of 249,917 galaxies, and the corresponding 24.0\% cache coverage, are selection-context diagnostics rather than custody-backed independent result rows" — manifest: FLG-SNCUT, FLG-PARENT, FLG-COVERAGE.
2. `flagship_rp1/aastex/rp1_flagship_polished.tex`, snapshot line 31: "The retained pilot analysis sample is a fixed 60,000-galaxy subset selected sequentially by \texttt{specObjID}." — manifest: FLG-60000.

**numerals_check:** 60,000 ↔ FLG-60000 `60,000` MATCH; S/N≥3 ↔ FLG-SNCUT `S/N$\geq3$` MATCH (digit 3 identical, LaTeX `$\geq$` rendered as ≥); 249,917 ↔ FLG-PARENT `249,917` MATCH; 24.0% ↔ FLG-COVERAGE `24.0\%` MATCH (digits identical); DR17 ↔ FLG-DR17 MATCH. Zero unmatched numerals.

**caveats:** Parent-count cascade values are query context only, not promoted to retained results without separate query receipts; the strict four-line S/N cut biases the retained denominator against emission-weak passive systems.

**verification:** LOCAL_ONLY

---

## P4-C05 — Flagship aperture geometry (fiber-centered comparison)

```
candidate_id: P4-C05
wiki_shape:
  page_id: OFFLINE_PLACEHOLDER
  claim_id: OFFLINE_PLACEHOLDER
  evidence_ids: OFFLINE_PLACEHOLDER
  page_version_fk: OFFLINE_PLACEHOLDER
  publish_state: OFFLINE_PLACEHOLDER
  category: galaxy
  proposed_page_slug: /wiki/active-galactic-nuclei
  proposed_section: Physical Properties
  see_also: [/wiki/galaxy-formation, /wiki/interstellar-medium, /wiki/quasars]
  references: [S1]
```

**claim_text:** Over the redshift interval 0.02<z<0.12, the SDSS 3-arcsec fiber subtends roughly 1.2--6.5 kpc, so RP-1's catalog median sSFR proxy comparison is fiber-centered rather than global. Single-fiber measurements can miss extended star-forming disks; if broad optical BPT hosts are more bulge-dominated than the star-forming controls, the central fiber measurement can inflate the observed offset relative to a galaxy-wide star-formation comparison.

**evidence:**
1. `flagship_rp1/aastex/rp1_flagship_polished.tex`, snapshot line 32: "Over the redshift interval $0.02<z<0.12$, the SDSS 3-arcsec fiber subtends roughly 1.2--6.5 kpc, so the catalog median sSFR proxy comparison is fiber-centered rather than global." — manifest: FLG-ZRANGE, FLG-FIBER, FLG-KPC.
2. `flagship_rp1/aastex/rp1_flagship_polished.tex`, snapshot line 33: "If broad optical BPT hosts are more bulge-dominated than the star-forming controls, the central fiber measurement can inflate the observed offset relative to a galaxy-wide star-formation comparison." — (no numerals; context for the caveat).

**numerals_check:** 0.02<z<0.12 ↔ FLG-ZRANGE `0.02<z<0.12` MATCH; 3-arcsec ↔ FLG-FIBER `3-arcsec` MATCH; 1.2--6.5 ↔ FLG-KPC `1.2--6.5` MATCH (LaTeX range dash carried verbatim). Zero unmatched numerals.

**caveats:** Aperture-morphology degeneracy is unbroken in this cycle (structural proxies not retained in the cache); resolved IFU spectroscopy is a named follow-up requirement, not a result.

**verification:** LOCAL_ONLY

---

## P4-C06 — Supplement environment baseline (10th-neighbor quartiles)

```
candidate_id: P4-C06
wiki_shape:
  page_id: OFFLINE_PLACEHOLDER
  claim_id: OFFLINE_PLACEHOLDER
  evidence_ids: OFFLINE_PLACEHOLDER
  page_version_fk: OFFLINE_PLACEHOLDER
  publish_state: OFFLINE_PLACEHOLDER
  category: galaxy
  proposed_page_slug: /wiki/galaxy-clusters
  proposed_section: Current Research
  see_also: [/wiki/active-galactic-nuclei, /wiki/galaxy-formation, /wiki/dark-matter]
  references: [S2]
```

**claim_text:** Within the fixed 60,000-galaxy SDSS emission-line denominator, a higher internally computed 10th-neighbor index is associated with a modestly higher low-sSFR emission-line fraction: 0.230 (3,456/15,000) in the high-index quartile versus 0.181 (2,710/15,000) in the low-index quartile, with a bootstrap high-minus-low interval of [0.041, 0.059]. A linear probability model adjusted for log stellar mass and redshift gives a high-index coefficient of 0.032 +/- 0.004, corresponding to an approximate 3.2 percentage-point increase in low-sSFR incidence at fixed mass and redshift. The 10th-neighbor index is a fiber-collision-biased projected-rank proxy (SDSS 55-arcsec collision limit), not a physical environmental or halo density estimate.

**evidence:**
1. `supplementary_denominator_atlas/aastex/supplementary_denominator_atlas.tex`, snapshot line 92: "The high-index quartile has a low-sSFR emission-line fraction of 0.230 (3,456/15,000), while the low-index quartile has 0.181 (2,710/15,000). The bootstrap high-minus-low interval is [0.041, 0.059], and a linear probability model adjusted for log stellar mass and redshift gives a high-index coefficient of 0.032 +/- 0.004, corresponding to an approximate 3.2 percentage-point increase in low-sSFR incidence at fixed mass and redshift." — manifest: SUP-ENV-HI, SUP-ENV-HI-RATIO, SUP-ENV-LO, SUP-ENV-LO-RATIO, SUP-ENV-CI, SUP-ENV-COEF, SUP-ENV-PP, SUP-15000, SUP-NEIGHBOR-ORD, SUP-60000 (line 92).
2. `supplementary_denominator_atlas/aastex/supplementary_denominator_atlas.tex`, snapshot line 93: "The SDSS 55-arcsec fiber-collision limit systematically removes close spectroscopic neighbors in dense regions before any physical interpretation is attempted" — manifest: SUP-FCOLL.

**numerals_check:** 60,000 ↔ SUP-60000 `60,000` MATCH; 10th ↔ SUP-NEIGHBOR-ORD `10th` MATCH; 0.230 ↔ SUP-ENV-HI MATCH; 3,456/15,000 ↔ SUP-ENV-HI-RATIO MATCH; 0.181 ↔ SUP-ENV-LO MATCH; 2,710/15,000 ↔ SUP-ENV-LO-RATIO MATCH; [0.041, 0.059] ↔ SUP-ENV-CI MATCH; 0.032 +/- 0.004 ↔ SUP-ENV-COEF MATCH (carried with `+/-` exactly); 3.2 ↔ SUP-ENV-PP MATCH (numeric_token); 15,000 ↔ SUP-15000 MATCH; 55-arcsec ↔ SUP-FCOLL MATCH. Zero unmatched numerals.

**caveats:** Ordinal rank inside a selection-biased sample; no line-of-sight velocity window; missing observables (group catalogs, central/satellite labels, halo mass, fiber-collision correction) are required before any physical inference (atlas Table 3).

**verification:** LOCAL_ONLY

---

## P4-C07 — Supplement maintenance-heating denominator (massive subset)

```
candidate_id: P4-C07
wiki_shape:
  page_id: OFFLINE_PLACEHOLDER
  claim_id: OFFLINE_PLACEHOLDER
  evidence_ids: OFFLINE_PLACEHOLDER
  page_version_fk: OFFLINE_PLACEHOLDER
  publish_state: OFFLINE_PLACEHOLDER
  category: galaxy
  proposed_page_slug: /wiki/active-galactic-nuclei
  proposed_section: Current Research
  see_also: [/wiki/galaxy-clusters, /wiki/quasars, /wiki/galaxy-formation]
  references: [S2]
```

**claim_text:** In the atlas's massive subset (log M* ≥ 10.8), 9,298 SDSS emission-line galaxies include 5,695 low-sSFR objects by the pilot threshold; the broad optical BPT-selected fraction is 0.430 in the massive subset and 0.607 among massive low-sSFR objects. This is an optical duty-cycle denominator for future X-ray and radio maintenance-heating follow-up, not a heating-to-cooling measurement.

**evidence:**
1. `supplementary_denominator_atlas/aastex/supplementary_denominator_atlas.tex`, snapshot line 103: "The massive subset (\(\log M_\star \geq 10.8\)) contains 9,298 emission-line galaxies, of which 5,695 are low-sSFR by the pilot threshold. The broad optical BPT-selected fraction is 0.430 in the massive subset and 0.607 among massive low-sSFR objects." — manifest: SUP-MASSCUT, SUP-MASSIVE-N, SUP-MASSIVE-LOWSSFR-N, SUP-BPT-FRAC-MASSIVE, SUP-BPT-FRAC-MASSIVE-LOWSSFR.

**numerals_check:** 10.8 ↔ SUP-MASSCUT `10.8` MATCH (numeric_token); 9,298 ↔ SUP-MASSIVE-N MATCH; 5,695 ↔ SUP-MASSIVE-LOWSSFR-N MATCH; 0.430 ↔ SUP-BPT-FRAC-MASSIVE MATCH; 0.607 ↔ SUP-BPT-FRAC-MASSIVE-LOWSSFR MATCH. Zero unmatched numerals.

**caveats:** Optical broad BPT selection primarily traces the radiative-mode denominator and cannot isolate the jet-mode population without contemporaneous X-ray and radio measurements; missing observables per atlas Table 3 (X-ray cavities, cooling luminosity, radio jet powers, halo-selected parents).

**verification:** LOCAL_ONLY

---

## P4-C08 — Supplement high-excitation subset (resolved-kinematics denominator)

```
candidate_id: P4-C08
wiki_shape:
  page_id: OFFLINE_PLACEHOLDER
  claim_id: OFFLINE_PLACEHOLDER
  evidence_ids: OFFLINE_PLACEHOLDER
  page_version_fk: OFFLINE_PLACEHOLDER
  publish_state: OFFLINE_PLACEHOLDER
  category: galaxy
  proposed_page_slug: /wiki/active-galactic-nuclei
  proposed_section: Current Research
  see_also: [/wiki/quasars, /wiki/galaxy-formation, /wiki/interstellar-medium]
  references: [S2]
```

**claim_text:** High-excitation broad optical BPT-selected candidates number 4,440 of 60,000 SDSS emission-line galaxies (0.074). Their median log sSFR is -11.53, compared with -10.14 for the full denominator. SDSS does not measure escape velocity or multiphase outflow velocities here; the subset defines a denominator for resolved-kinematics follow-up, not an escape or recycling result.

**evidence:**
1. `supplementary_denominator_atlas/aastex/supplementary_denominator_atlas.tex`, snapshot line 114: "High-excitation broad optical BPT-selected candidates number 4,440 of 60,000 emission-line galaxies (0.074). Their median \(\log {\rm sSFR}\) is -11.53, compared with -10.14 for the full denominator." — manifest: SUP-HIEXC-N, SUP-60000, SUP-HIEXC-FRAC, SUP-HIEXC-SSFR, SUP-FULL-SSFR.

**numerals_check:** 4,440 ↔ SUP-HIEXC-N MATCH; 60,000 ↔ SUP-60000 MATCH; 0.074 ↔ SUP-HIEXC-FRAC MATCH; -11.53 ↔ SUP-HIEXC-SSFR MATCH; -10.14 ↔ SUP-FULL-SSFR MATCH. Zero unmatched numerals.

**caveats:** Optical excitation alone cannot determine whether gas exceeds the halo escape speed; missing observables per atlas Table 3 (resolved velocities, halo potentials, multiphase gas, CGM tracers).

**verification:** LOCAL_ONLY

---

## P4-C09 — Supplement radio-jet environment baseline (massive hosts, quartile contrast)

```
candidate_id: P4-C09
wiki_shape:
  page_id: OFFLINE_PLACEHOLDER
  claim_id: OFFLINE_PLACEHOLDER
  evidence_ids: OFFLINE_PLACEHOLDER
  page_version_fk: OFFLINE_PLACEHOLDER
  publish_state: OFFLINE_PLACEHOLDER
  category: galaxy
  proposed_page_slug: /wiki/galaxy-clusters
  proposed_section: Current Research
  see_also: [/wiki/active-galactic-nuclei, /wiki/quasars, /wiki/galaxy-formation]
  references: [S2]
```

**claim_text:** Among massive hosts in the atlas denominator, the high-index quartile has a broad optical BPT-selected fraction of 0.509, while the low-index quartile has 0.367; the bootstrap high-minus-low interval is [0.112, 0.170]. This is an optical/environment denominator for future radio-jet follow-up; it does not measure radio jet power or coupling efficiency, and the neighbor ranking carries the same fiber-collision bias as the environment baseline.

**evidence:**
1. `supplementary_denominator_atlas/aastex/supplementary_denominator_atlas.tex`, snapshot line 125: "Among massive hosts, the high-index quartile has a broad optical BPT-selected fraction of 0.509, while the low-index quartile has 0.367. The bootstrap high-minus-low interval is [0.112, 0.170]." — manifest: SUP-JET-HI, SUP-JET-LO, SUP-JET-CI.

**numerals_check:** 0.509 ↔ SUP-JET-HI MATCH; 0.367 ↔ SUP-JET-LO MATCH; [0.112, 0.170] ↔ SUP-JET-CI MATCH. Zero unmatched numerals.

**caveats:** Missing observables per atlas Table 3 (radio morphology/age, cavity energetics, hot-gas density); reuses the projected-neighbor ranking with its 55-arcsec fiber-collision bias.

**verification:** LOCAL_ONLY

---

## P4-C10 — Supplement stellar-mass selection diagnostic (incidence by mass bin)

```
candidate_id: P4-C10
wiki_shape:
  page_id: OFFLINE_PLACEHOLDER
  claim_id: OFFLINE_PLACEHOLDER
  evidence_ids: OFFLINE_PLACEHOLDER
  page_version_fk: OFFLINE_PLACEHOLDER
  publish_state: OFFLINE_PLACEHOLDER
  category: galaxy
  proposed_page_slug: /wiki/galaxy-formation
  proposed_section: Current Research
  see_also: [/wiki/active-galactic-nuclei, /wiki/stellar-evolution, /wiki/galaxy-clusters]
  references: [S2]
```

**claim_text:** In this optical-emission-line denominator, the first stellar-mass bin with low-sSFR fraction above 0.5 is log(M*/M☉) ∈ [11.0,12.5], and broad optical BPT-selected incidence peaks in the 11.0--12.5 bin at 0.520, within a selection-limited, SpecObjID-capped pilot sample. The peak is consistent with a selection-function bias (the S/N≥3 cut preferentially removes truly passive massive galaxies) and must not be read as a universal physical threshold or a physical transition mass for individual galaxies.

**evidence:**
1. `supplementary_denominator_atlas/aastex/supplementary_denominator_atlas.tex`, snapshot line 136: "The first stellar-mass bin with low-sSFR fraction above 0.5 is \(\log(M_\star/M_\odot) \in [11.0,12.5]\), and the broad optical BPT-selected incidence peaks in the 11.0--12.5 bin at 0.520 within this selection-limited, SpecObjID-capped pilot sample." — manifest: SUP-HALF, SUP-MASSBIN-INT, SUP-MASSBIN-DASH, SUP-BPT-PEAK.
2. `supplementary_denominator_atlas/aastex/supplementary_denominator_atlas.tex`, snapshot line 136: "the S/N$\geq$3 cut preferentially removes truly passive, massive galaxies, leaving a surviving emission-line subset that is concentrated in that mass bin." — manifest: SUP-SNCUT-B (spacing variant `S/N$\geq$3`).

**numerals_check:** 0.5 ↔ SUP-HALF `0.5` MATCH (numeric_token); [11.0,12.5] ↔ SUP-MASSBIN-INT MATCH; 11.0--12.5 ↔ SUP-MASSBIN-DASH MATCH (LaTeX range dash carried verbatim); 0.520 ↔ SUP-BPT-PEAK MATCH; S/N≥3 ↔ SUP-SNCUT-B `S/N$\geq$3` MATCH (digit 3 identical; this line uses the spacing variant, distinct manifest entry). Zero unmatched numerals.

**caveats:** Optical distribution diagnostic only; gas fractions and baryon deficits are needed before assigning physical meaning; missing observables per atlas Table 3.

**verification:** LOCAL_ONLY

---

## P4-C11 — Supplement tracer-threshold census (prevalence sensitivity)

```
candidate_id: P4-C11
wiki_shape:
  page_id: OFFLINE_PLACEHOLDER
  claim_id: OFFLINE_PLACEHOLDER
  evidence_ids: OFFLINE_PLACEHOLDER
  page_version_fk: OFFLINE_PLACEHOLDER
  publish_state: OFFLINE_PLACEHOLDER
  category: galaxy
  proposed_page_slug: /wiki/active-galactic-nuclei
  proposed_section: Open Questions
  see_also: [/wiki/quasars, /wiki/interstellar-medium, /wiki/galaxy-formation]
  references: [S2]
```

**claim_text:** Within the same 60,000-galaxy SDSS denominator, simple optical tracer definitions produce broad optical BPT-selected prevalence from 0.136 to 0.418 — a widest-to-narrowest prevalence ratio of 3.1 — before adding molecular, neutral, X-ray, or radio phases. This tracer sensitivity motivates a common-denominator multiphase census; it does not measure molecular or neutral outflow rates.

**evidence:**
1. `supplementary_denominator_atlas/aastex/supplementary_denominator_atlas.tex`, snapshot line 147: "Within the same 60,000-galaxy denominator, simple optical tracer definitions produce prevalence from 0.136 to 0.418. The widest-to-narrowest prevalence ratio is 3.1 before adding molecular, neutral, X-ray, or radio phases." — manifest: SUP-60000, SUP-TRACER-LO, SUP-TRACER-HI, SUP-TRACER-RATIO.

**numerals_check:** 60,000 ↔ SUP-60000 MATCH; 0.136 ↔ SUP-TRACER-LO MATCH; 0.418 ↔ SUP-TRACER-HI MATCH; 3.1 ↔ SUP-TRACER-RATIO MATCH (numeric_token). Zero unmatched numerals.

**caveats:** Missing observables per atlas Table 3 (multiphase tracers, shared denominator, aperture model); prevalence values are conditional on the optical selection.

**verification:** LOCAL_ONLY

---

## P4-C12 — Supplement gas-depletion denominator (CO/HI follow-up baseline)

```
candidate_id: P4-C12
wiki_shape:
  page_id: OFFLINE_PLACEHOLDER
  claim_id: OFFLINE_PLACEHOLDER
  evidence_ids: OFFLINE_PLACEHOLDER
  page_version_fk: OFFLINE_PLACEHOLDER
  publish_state: OFFLINE_PLACEHOLDER
  category: galaxy
  proposed_page_slug: /wiki/interstellar-medium
  proposed_section: Current Research
  see_also: [/wiki/active-galactic-nuclei, /wiki/galaxy-formation, /wiki/nebulae]
  references: [S2]
```

**claim_text:** The gas-depletion note's massive low-sSFR denominator contains 6,729 galaxies in the SDSS emission-line sample; its broad optical BPT-selected fraction is 0.549, and the median H-alpha luminosity proxy is log L_Hα = 40.061 (erg/s catalog scale), which is 0.66 dex lower than in massive star-forming emission-line galaxies. The H-alpha value is an aperture-corrected, model-dependent catalog proxy, not a direct total cold-gas-mass measurement, and this denominator is note-specific — it should not be conflated with the log M* ≥ 10.8 maintenance-heating subset.

**evidence:**
1. `supplementary_denominator_atlas/aastex/supplementary_denominator_atlas.tex`, snapshot line 158: "the massive low-sSFR denominator contains 6,729 galaxies in the SDSS emission-line sample." / "Its broad optical BPT-selected fraction is 0.549, and the median H-alpha luminosity proxy is \(\log (L_{\mathrm{H}\alpha}/\mathrm{erg\,s^{-1}}) = 40.061\)." / "The median H-alpha luminosity proxy is 0.66 dex lower than in massive star-forming emission-line galaxies." — manifest: SUP-GAS-N, SUP-GAS-BPT, SUP-GAS-LHA, SUP-GAS-DEX.
2. `supplementary_denominator_atlas/aastex/supplementary_denominator_atlas.tex`, snapshot line 158: "This denominator is note-specific and should not be conflated with the \(\log M_\star \geq 10.8\) maintenance-heating subset summarized above." — manifest: SUP-MASSCUT (line 158 occurrence).

**numerals_check:** 6,729 ↔ SUP-GAS-N MATCH; 0.549 ↔ SUP-GAS-BPT MATCH; 40.061 ↔ SUP-GAS-LHA MATCH; 0.66 ↔ SUP-GAS-DEX MATCH (numeric_token); 10.8 ↔ SUP-MASSCUT MATCH (numeric_token). Zero unmatched numerals (the `s^{-1}` exponent in the quoted LaTeX is unit notation, manifest-excluded identifier digits; claim_text uses "erg/s" to avoid a bare unit numeral).

**caveats:** No CO-to-H₂ conversion performed; MPA-JHU Kroupa-IMF catalog scale retained; residual dust attenuation and stellar-absorption systematics apply; missing observables per atlas Table 3 (CO/dust gas masses, aperture-matched SFRs, morphology, environment).

**verification:** LOCAL_ONLY

---

## P4-C13 — Supplement simulation target vector (forward-model spans)

```
candidate_id: P4-C13
wiki_shape:
  page_id: OFFLINE_PLACEHOLDER
  claim_id: OFFLINE_PLACEHOLDER
  evidence_ids: OFFLINE_PLACEHOLDER
  page_version_fk: OFFLINE_PLACEHOLDER
  publish_state: OFFLINE_PLACEHOLDER
  category: galaxy
  proposed_page_slug: /wiki/galaxy-formation
  proposed_section: Current Research
  see_also: [/wiki/active-galactic-nuclei, /wiki/dark-matter, /wiki/galaxy-clusters]
  references: [S2]
```

**claim_text:** The atlas's simulation target vector comprises 15 mass-redshift cells with n ≥ 50, recording low-sSFR fraction, broad optical BPT-selected incidence, and median u−r colour versus mass and redshift. Across mass bins, low-sSFR fractions span 0.005-0.729 and broad optical BPT-selected fractions span 0.003-0.520. This is an observed optical target vector for forward modelling, not a simulation comparison; simulations must be passed through the same optical S/N, fiber-aperture, and sequential cache-cap selection function before any comparison is valid.

**evidence:**
1. `supplementary_denominator_atlas/aastex/supplementary_denominator_atlas.tex`, snapshot line 169: "The pilot writes 15 mass-redshift cells with \(n \geq 50\) as a compact comparison vector for low-sSFR fraction, broad optical BPT-selected incidence, and median \(u-r\) colour versus mass and redshift. Across mass bins, low-sSFR fractions span 0.005-0.729, and broad optical BPT-selected fractions span 0.003-0.520." — manifest: SUP-CELLS, SUP-CELL-MIN, SUP-SPAN-QUENCH, SUP-SPAN-BPT.

**numerals_check:** 15 ↔ SUP-CELLS `15` MATCH (numeric_token); 50 ↔ SUP-CELL-MIN `50` MATCH (numeric_token); 0.005-0.729 ↔ SUP-SPAN-QUENCH MATCH (artifact-anchored m3_p3 span; cycle 6 corrupted this exact value — carried verbatim); 0.003-0.520 ↔ SUP-SPAN-BPT MATCH (artifact-anchored; same cycle-6 failure class — carried verbatim). Zero unmatched numerals.

**caveats:** Spans are anchored to the m3_p3 artifact result bullet, not re-derived from Table 4 (the table-derived spans differ — that substitution is precisely the cycle-6 integrity failure); the full 15-row target-vector table (snapshot lines 176–190) is invariant as whole rows (manifest SUP-ROW-176…SUP-ROW-190, including the line-188 truncation anomaly) and should be carried byte-identical if ever integrated.

**verification:** LOCAL_ONLY

---

## Coverage note

13 candidates: flagship headline result and its four core context claims (P4-C01…C05), then all eight supplement atlas entries (P4-C06…C13). The 15 individual target-vector table rows (SUP-ROW-176…190) are deliberately not expanded into separate candidates — P4-C13 carries the vector as a unit with its whole-row invariance rule, which is the integrity-safe form. All 105 manifest entries relevant to the claims above are referenced; manifest entries not used here (e.g. FLG-8146-BRACED figure-caption form, FLG-OIII/FLG-NII wavelength identifiers, SUP-RUNID rows, SUP-SHA-* provenance hashes, individual SUP-ROW-039…066 table rows) are provenance/structural invariants that belong to manuscript carry-checks rather than standalone wiki claims.

`FABLE_BURN_P4_CLAIM_EVIDENCE_CANDIDATES_20260711T010503Z`
