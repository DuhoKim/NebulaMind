# Phase A — Data acquisition (Tori): independent + orthogonal z>7 O/H samples

Generated: 2026-07-20T16:07:40+0900 (KST). Real data only. No fabricated rows.
Output table: `z7_multisurvey.csv` (per-object; survey, id, z, logM, logM_err, OH, OH_err, calib, selection_type, lensed, mu, oh_limit, mass_limit).

## Summary of what was pulled

| Survey | Reachable per-object? | N(z>7) | N overlap [8.0,9.5], measured O/H | N overlap incl. limits | Calib/diagnostic | Selection |
|---|---|---|---|---|---|---|
| Nakajima+2023 (J/ApJS/269/33) | YES (reused; VizieR TAP) | 26 | 16 | 19 (+3 mass upper-limits) | direct-Te / R23 / R3 (O-based) | emission-line census |
| Heintz+2023 (arXiv:2212.02890) | YES (arXiv source Table 1) | 16 | 13 | 15 (+2 O/H lower-limits) | R3 / O32 / R2 (O-based, Nakajima22 Large-EW) | photometric-dropout; 5 lensed (cluster fields) |
| Curti+2024 (J/A+A/684/A75) | NO (per-object genuinely unreachable) | -- | -- | -- | R-hat/R3/R23 (paper) | JADES deep + CEERS |

Two independent per-object samples now exist (Nakajima+23 AND Heintz+23), plus a real
orthogonally-selected (lensed/continuum, NOT emission-line-selected) subsample of N=5 from Heintz.

## 1. Nakajima+2023 (reused)
- Catalog: VizieR TAP `J/ApJS/269/33/table1` (as pulled in overnight-z7-mzr-20260720; verified table still live this run).
- Source file reused verbatim: `../overnight-z7-mzr-20260720/z7_metallicity.csv` (26 rows, all z>7, both M* and O/H).
- Overlap [8.0,9.5]: 16 with measured O/H (excludes 3 mass upper-limits: CEERS_00689, CEERS_01025, CEERS_01163). Matches prior run results.json.
- Diagnostics: direct-Te (6), R23/R3 strong-line (rest) — all oxygen-based (no N-based). calib column preserved.
- selection_type tagged `emission_line` (JWST NIRSpec emission-line/UV census). lensed flag left blank: the census mixes lensed (GLASS=Abell2744, ERO=SMACS0723) and field (CEERS) targets without a per-object mu in the pulled table, so no clean per-object lensed cut is asserted here.

## 2. Heintz+2023 — "Dilution of chemical enrichment in galaxies 600 Myr after the Big Bang"
- Nature Astronomy 7, 1517 (2023); arXiv:2212.02890; DOI 10.1038/s41550-023-02078-7. (Brief guessed ApJ/ApJL; it is Nat. Astron. — same paper, the z=7-10 O/H sample.)
- NOT in VizieR (no CDS catalog deposited). Per-object data pulled from the arXiv e-print source (`main.tex`, Table "Physical properties of the primary sample galaxies", tab:props) — the published machine-readable per-object table. Line fluxes cross-checked against Table "Line flux measurements" (tab:lflux).
- Method: curl arXiv e-print tarball 2212.02890 -> extract main.tex -> parse Table 1. Values transcribed exactly; asymmetric (+/-) errors averaged into symmetric logM_err / OH_err.
- N=16, all z=7.10-9.50 (all z>7). O/H via strong-line R3 ([OIII]5008/Hb, Nakajima22 Large-EW, EW_Hb>200A) for 13; O32 for 2; R2 for 1 — all oxygen-based, none N-based.
- Overlap [8.0,9.5]: 15 by mass; 13 with measured O/H (2 are O/H lower-limits: Abell-z7878 >7.30, CEERS-z7789 >8.06 — flagged oh_limit=lower). One object (CEERS-z8684, logM=10.0) is above the overlap window.
- Lensed / orthogonal subsample (mu column present = cluster-lensing fields RX J2129 and Abell): RXJ-z9500 (mu=19.2), RXJ-z8149 (2.25), RXJ-z8152 (1.46), Abell-z7878 (1.33), Abell-z7885 (2.12). These 5 are lensed, photometric-dropout-selected behind clusters — i.e. selected orthogonally to an emission-line census. 4 have measured O/H inside [8.0,9.5] (Abell-z7878 is an O/H limit). tagged selection_type=lensed_cluster, lensed=1.
- CEERS field galaxies (11): mu absent, tagged selection_type=field_photometric, lensed=0.

### INDEPENDENCE CAVEAT (for the analysis lead)
Heintz+23 is an independent reduction/analysis (Bagpipes non-parametric SFH masses; independently applied Nakajima22 R3 calibration). Its 11 CEERS galaxies are drawn from the same public CEERS NIRSpec pointings as Nakajima+23's CEERS objects and MAY overlap at the object level (different ID schemes: Heintz uses CEERS-z#### by redshift; Nakajima uses CEERS_#####). A coordinate cross-match is needed before treating the CEERS subsets as fully independent. The 5 LENSED objects (RX J2129 + Abell fields) are from fields NOT in Nakajima's pulled sample and are cleanly independent AND orthogonally selected — this is the robust orthogonal subsample.

## 3. Curti+2024 (JADES) — GENUINELY UNREACHABLE at per-object level
- A&A 684, A75 (2024); arXiv:2304.08516; DOI 10.1051/0004-6361/202346698; ADS 2024A&A...684A..75C.
- (a) Vizier.find_catalogs("Curti 2024 JADES metallicity") -> returns only unrelated stellar catalogs + V/159 (JADES DR1-DR3 phot/line-flux catalog, Rieke+); NOT the Curti MZR catalog.
- (b) Direct VizieR TAP (https://tapvizier.cds.unistra.fr/TAPVizieR/tap/sync) ADQL SELECT from "J/A+A/684/A75/table1", "/tablea1", "/sample" -> HTTP 400 (table does not exist). Control query on "J/ApJS/269/33/table1" (Nakajima) returns columns -> mechanism verified working.
- (c) CDS store: https://cdsarc.cds.unistra.fr/viz-bin/cat/J/A+A/684/A75 -> "vizier catalogue not found"; FTP dir behind Anubis bot-wall. No machine-readable table deposited.
- (d) arXiv e-print 2304.08516 source (aanda.tex): contains only BINNED summary tables (Table tab:binned_values: median M*, SFR, O/H per M*-z bin; Table tab:best-fit_mzr: MZR fit params). NO per-object catalog anywhere in the source. Per-object metallicities are not published by Curti+24.
- Best available Curti+24 context (BINNED, not per-object; z in [6,10] bins, and these bins INCLUDE re-measured CEERS objects that overlap Nakajima -> not independent):
  - logM bin [6,7.75]: N=10, <z>=6.71, <logM>=7.35, 12+log(O/H)=7.64 +/-0.07 (sd 0.24)
  - logM bin [7.75,8.5]: N=15, <z>=6.54, <logM>=8.10, O/H=7.67 +/-0.06 (0.22)
  - logM bin [8.5,10]: N=11, <z>=6.93, <logM>=8.76, O/H=7.73 +/-0.08 (0.30)
  - MZR fit z in [6,10]: 12+log(O/H) = 7.65(+/-0.04) + 0.11(+/-0.05)*log(M*/1e8); median FMR offset ~ -0.64 dex.
  Use only as a consistency cross-check for the binned trend, NOT as a per-object independent survey.

## Decision-rule bearing (Phase A deliverable)
- Blocker B1 (single-survey): PARTIALLY CLOSED. Two independent per-object z>7 samples now on disk (Nakajima+23 N=26; Heintz+23 N=16). Combined overlap [8.0,9.5] with measured O/H = 16 + 13 = 29 (target was N>=40 across >=3 surveys; 3rd survey Curti+24 unreachable per-object, so we have 2 surveys, N=29 in overlap). Heintz+23 also independently reports the SAME-direction offset (median -0.50 +/- 0.05 dex vs local FMR at z=7-10).
- Blocker B3 (selection): a REAL orthogonally-selected (lensed) subsample exists — Heintz lensed N=5 (4 with measured O/H in overlap). The per-survey Delta and the orthogonal-subsample Delta are computable in Phase B.
- Honest status: we are NO LONGER single-survey. Whether the label lifts to DETECTION now depends on the Phase-B per-survey CIs and the orthogonal-subsample CI, per the locked rule. If the small-N orthogonal/Heintz CIs straddle 0, the rule keeps it DESCRIPTIVE — an admissible, honest outcome.
