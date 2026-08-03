# DATA AUDIT — z>7 mass–metallicity relation (Tori, P1)
Time: see LEDGER. Real data on disk only; no fabrication.

## What we HAVE (real, on disk)
| Asset | Path | Content | Calibration | Usable? |
|---|---|---|---|---|
| SDSS anchor | research-frontiers-20260716/sdss_mzr.csv | N=203,599 star-forming (bptclass==1 pre-filtered); cols lgm_tot_p50, oh_p50, sfr_tot_p50 | **Tremonti04** (MPA-JHU) | YES — anchor computed (sdss_anchor.json) |
| Prior SDSS fit | research-frontiers-20260716/mzr_results.json | Z0=9.218, logM0=9.997, gamma=0.524, oh@logM9=8.58, @logM10.5=9.053, scatter 0.139 | T04 | YES (reproduced) |
| TNG100-1 sim MZR | research-frontiers-20260716/topic3/tng_results.json | mzr_median_grid at z=0,4,5,6; OH=8.69+log10(Zgas/0.0127) SFR-weighted | sim (solar-scaled) | z<=6 only |
| Published high-z fits | wiki-expansion-20260715/area1_mass_metallicity_DR_PACKET.md | Curti+24 (2024A&A...684A..75C): 12+log(O/H)=(7.72±0.02)+(0.17±0.03)log(M/1e8), 3<z<10; median FMR offset ~0.5 dex above z~6. Nakajima+23 (2023ApJS..269...33N) JWST z=4-10 census. Sanders dlog(O/H)/dz=-0.11±0.02 (z=0-3.3) | Te/strong-line matched | Literature relations only |
| Nakajima anchor point | overnight-research-20260718/RESULTS.json entry i=17 (fig s17_jwst_mzr.png) | single derived point: 12+log(O/H)@logM=9 ~ 7.97 (Nakajima+23, N=144, z~4-10) | strong-line | point only, extra:{} empty |
| Calibration reference | DR_PACKET.md | Kewley&Ellison 2008 (2008ApJ...681.1183K) — inter-calibration conversions; calibration families span up to ~0.7 dex | — | conversion recipe |

## What is MISSING — THE CRITICAL GAP
1. **No individual-galaxy z>7 O/H table on disk.** chworowsky.csv (topic5) is a MASS-ONLY catalog
   (logMs, zphot, zspec — NO oxygen/metallicity column); zphot maxes at 7.64, only 7 objects at z>7.
   It CANNOT provide z>7 O/H. The only z>7 metallicity we have is embedded in published FITS
   (Curti+24) and a single derived summary point (Nakajima+23 @logM9). No per-galaxy points ->
   **we cannot bootstrap a real z>7 sample; the small-N bootstrap must run on the literature bin/fit
   uncertainties, not on individual galaxies we do not possess.**
   -> KEY GAP for human/DR-assisted pull: a compiled z>7 (M*, 12+log(O/H), calibration, sigma) table
      from Nakajima+23 (Te subset + strong-line, z>7 slice), Curti+24 JADES per-object, Heintz+23.
2. **SDSS has no emission-line fluxes on disk** (only the summary oh_p50). Direct O3N2 recompute for
   SDSS is impossible here -> calibration reconciliation must go via a PUBLISHED T04->PP04-O3N2
   conversion (Kewley&Ellison 2008), not a re-derivation.
3. **TNG stops at z=6** on disk (no z=7,8 snapshots extracted). A true z>7 sim overlay needs
   re-extraction of TNG100/TNG50 high-z snapshots; z=6 is the closest available proxy.

## Bottom line
The SDSS anchor and the calibration machinery are fully in hand. The evolution claim rests entirely
on a z>7 O/H sample we do NOT yet have as data — only as published relations. P2 can proceed by
confronting the SDSS anchor against the Curti+24 / Nakajima+23 PUBLISHED relations on a matched scale
(honest, literature-anchored), but a per-object z>7 table is the make-or-break pull for a stronger result.
