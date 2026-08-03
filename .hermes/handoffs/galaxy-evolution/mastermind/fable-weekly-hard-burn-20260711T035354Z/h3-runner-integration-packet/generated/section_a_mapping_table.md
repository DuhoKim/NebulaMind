| manifest id | doc | kind | audit-list entry (exact string) | exp. occ. | cycle-5 check | live-list coverage | notes |
|---|---|---|---|---:|---|---|---|
| FLG-60000 | flagship | count | `60,000` | 11 | OK | covered | already covered by live list |
| FLG-8146 | flagship | count | `8,146` | 9 | OK | covered | already covered by live list |
| FLG-8146-BRACED | flagship | count | `8{,}146` | 1 | OK | NEW | — |
| FLG-MEDIAN-OFFSET | flagship | point_estimate | `-1.309` | 6 | OK | covered | already covered by live list |
| FLG-CI95 | flagship | ci_interval | `[-1.334,-1.283]` | 4 | OK | covered | already covered by live list |
| FLG-CI-LEVEL | flagship | percent | `95\%` | 5 | OK | NEW | — |
| FLG-PARENT | flagship | count | `249,917` | 1 | OK | covered | already covered by live list |
| FLG-COVERAGE | flagship | percent | `24.0\%` | 1 | OK | NEW | — |
| FLG-ZRANGE | flagship | redshift_range | `0.02<z<0.12` | 2 | OK | NEW | — |
| FLG-KPC | flagship | physical_range | `1.2--6.5` | 2 | OK | NEW | — |
| FLG-FIBER | flagship | aperture | `3-arcsec` | 4 | OK | NEW | — |
| FLG-SNCUT | flagship | threshold | `S/N$\geq3$` | 2 | OK | NEW | presence implied by FLG-ROW-057 |
| FLG-SF | flagship | count | `39,553` | 1 | OK | NEW | — |
| FLG-COMP | flagship | count | `12,234` | 1 | OK | NEW | — |
| FLG-UNCLASS | flagship | count | `67` | 2 | present (token mode) | NEW | numeric_token mode -> manifest pre-audit gate only; too short/ambiguous for a bare substring check |
| FLG-COVERAGE-PCT | flagship | percent | `100\%` | 1 | OK | NEW | — |
| FLG-SEP-LOGM | flagship | dex | `0.0045` | 1 | OK | NEW | — |
| FLG-SEP-Z | flagship | other | `0.00021` | 1 | OK | NEW | — |
| FLG-OIII | flagship | wavelength_identifier | `\lambda5007` | 1 | OK | NEW | — |
| FLG-NII | flagship | wavelength_identifier | `\lambda6584` | 1 | OK | NEW | — |
| FLG-RUNID | flagship | run_identifier | `SDSS\_AGN\_SFR\_PILOT\_20260708T122000Z` | 2 | OK | NEW | — |
| FLG-DR17 | flagship | release_identifier | `DR17` | 7 | OK | NEW | — |
| SUP-60000 | supplement | count | `60,000` | 15 | OK | NEW | presence implied by SUP-ROW-059 |
| SUP-8146 | supplement | count | `8,146` | 1 | OK | NEW | — |
| SUP-PARENT | supplement | count | `249,917` | 1 | OK | NEW | — |
| SUP-COVERAGE | supplement | percent | `24.0\%` | 2 | OK | NEW | — |
| SUP-SNCUT-A | supplement | threshold | `S/N$\geq3$` | 2 | OK | NEW | — |
| SUP-SNCUT-B | supplement | threshold | `S/N$\geq$3` | 1 | OK | NEW | — |
| SUP-ZRANGE | supplement | redshift_range | `0.02<z<0.12` | 2 | OK | NEW | — |
| SUP-FCOLL | supplement | aperture | `55-arcsec` | 4 | OK | NEW | — |
| SUP-FIBER | supplement | aperture | `3-arcsec` | 1 | OK | NEW | — |
| SUP-NEIGHBOR-ORD | supplement | method_parameter | `10th` | 8 | OK | NEW | presence implied by SUP-ROW-059 |
| SUP-ENV-HI | supplement | fraction | `0.230` | 1 | OK | NEW | — |
| SUP-ENV-HI-RATIO | supplement | fraction | `3,456/15,000` | 1 | OK | NEW | — |
| SUP-ENV-LO | supplement | fraction | `0.181` | 1 | OK | NEW | — |
| SUP-ENV-LO-RATIO | supplement | fraction | `2,710/15,000` | 1 | OK | NEW | — |
| SUP-ENV-CI | supplement | ci_interval | `[0.041, 0.059]` | 1 | OK | NEW | — |
| SUP-ENV-COEF | supplement | point_estimate | `0.032 +/- 0.004` | 1 | OK | NEW | — |
| SUP-ENV-PP | supplement | percent | `3.2` | 1 | present (token mode) | NEW | numeric_token mode -> manifest pre-audit gate only; too short/ambiguous for a bare substring check |
| SUP-15000 | supplement | count | `15,000` | 3 | OK | NEW | presence implied by SUP-ENV-HI-RATIO |
| SUP-MASSCUT | supplement | threshold | `10.8` | 2 | present (token mode) | NEW | numeric_token mode -> manifest pre-audit gate only; too short/ambiguous for a bare substring check |
| SUP-MASSIVE-N | supplement | count | `9,298` | 2 | OK | NEW | presence implied by SUP-ROW-060 |
| SUP-MASSIVE-LOWSSFR-N | supplement | count | `5,695` | 2 | OK | NEW | presence implied by SUP-ROW-060 |
| SUP-BPT-FRAC-MASSIVE | supplement | fraction | `0.430` | 2 | OK | NEW | presence implied by SUP-ROW-185 |
| SUP-BPT-FRAC-MASSIVE-LOWSSFR | supplement | fraction | `0.607` | 1 | OK | NEW | — |
| SUP-HIEXC-N | supplement | count | `4,440` | 2 | OK | NEW | presence implied by SUP-ROW-061 |
| SUP-HIEXC-FRAC | supplement | fraction | `0.074` | 1 | OK | NEW | — |
| SUP-HIEXC-SSFR | supplement | dex | `-11.53` | 1 | OK | NEW | — |
| SUP-FULL-SSFR | supplement | dex | `-10.14` | 1 | OK | NEW | — |
| SUP-JET-HI | supplement | fraction | `0.509` | 1 | OK | NEW | — |
| SUP-JET-LO | supplement | fraction | `0.367` | 1 | OK | NEW | — |
| SUP-JET-CI | supplement | ci_interval | `[0.112, 0.170]` | 1 | OK | NEW | — |
| SUP-MASSBIN-INT | supplement | range | `[11.0,12.5]` | 1 | OK | NEW | — |
| SUP-MASSBIN-DASH | supplement | range | `11.0--12.5` | 4 | OK | NEW | presence implied by SUP-ROW-188 |
| SUP-BPT-PEAK | supplement | fraction | `0.520` | 2 | OK | NEW | presence implied by SUP-SPAN-BPT |
| SUP-HALF | supplement | threshold | `0.5` | 1 | present (token mode) | NEW | numeric_token mode -> manifest pre-audit gate only; too short/ambiguous for a bare substring check |
| SUP-TRACER-LO | supplement | fraction | `0.136` | 2 | OK | NEW | presence implied by SUP-ROW-064 |
| SUP-TRACER-HI | supplement | fraction | `0.418` | 2 | OK | NEW | presence implied by SUP-ROW-064 |
| SUP-TRACER-RATIO | supplement | ratio | `3.1` | 1 | present (token mode) | NEW | numeric_token mode -> manifest pre-audit gate only; too short/ambiguous for a bare substring check |
| SUP-GAS-N | supplement | count | `6,729` | 2 | OK | NEW | presence implied by SUP-ROW-065 |
| SUP-GAS-BPT | supplement | fraction | `0.549` | 1 | OK | NEW | — |
| SUP-GAS-LHA | supplement | luminosity | `40.061` | 1 | OK | NEW | — |
| SUP-GAS-DEX | supplement | dex | `0.66` | 1 | present (token mode) | NEW | numeric_token mode -> manifest pre-audit gate only; too short/ambiguous for a bare substring check |
| SUP-SPAN-QUENCH | supplement | range | `0.005-0.729` | 1 | OK | NEW | — |
| SUP-SPAN-BPT | supplement | range | `0.003-0.520` | 1 | OK | NEW | — |
| SUP-CELLS | supplement | count | `15` | 4 | present (token mode) | NEW | numeric_token mode -> manifest pre-audit gate only; too short/ambiguous for a bare substring check |
| SUP-CELL-MIN | supplement | threshold | `50` | 5 | present (token mode) | NEW | numeric_token mode -> manifest pre-audit gate only; too short/ambiguous for a bare substring check |
| SUP-60K | supplement | count | `60k` | 1 | OK | NEW | presence implied by SUP-ROW-064 |
| SUP-RUNID-TOPICS | supplement | run_identifier | `SDSS\_REMAINING\_TOPIC\_PILOTS\_20260708T125828Z` | 9 | OK | NEW | presence implied by SUP-ROW-039 |
| SUP-RUNID-PILOT | supplement | run_identifier | `SDSS\_AGN\_SFR\_PILOT\_20260708T122000Z` | 2 | OK | NEW | — |
| SUP-SHA-RESULTS | supplement | sha256 | `668ad7a67290600ff5028ae587d32ef239a09bd8627a480539f37e1927d659df` | 1 | OK | NEW | — |
| SUP-SHA-PAIRS | supplement | sha256 | `4ea53af867cccccb2b68b81557ff84fe90ec3f13e0512ffbdc977fa7216996fd` | 1 | OK | NEW | — |
| SUP-DR17 | supplement | release_identifier | `DR17` | 4 | OK | NEW | — |
| FLG-ROW-057 | flagship | table_row | `Broad optical BPT-selected targets, S/N$\geq3$, nearest SF control with replacement & 8,146 & -1.309 & [-1.334,-1.283] & Preferred association estimate \\` | 1 | OK | NEW | — |
| SUP-ROW-039 | supplement | table_row | `Relative neighbor-count baseline & \texttt{SDSS\_REMAINING\_TOPIC\_PILOTS\_20260708T125828Z} & \texttt{m1\_rp2\_environment\_quenching/analysis\_results.json} & \texttt{c0421620f67f3c227955affa3f4c1876cb85f8b31874d219f2cd2e35a7f9cec0} \\` | 1 | OK | NEW | — |
| SUP-ROW-040 | supplement | table_row | `Maintenance-heating denominator & \texttt{SDSS\_REMAINING\_TOPIC\_PILOTS\_20260708T125828Z} & \texttt{m1\_rp3\_maintenance\_heating/analysis\_results.json} & \texttt{06291f82c3fbe0f7fe84f7249568882ca4fa44972bcc25a55e367ef1fdcc7e6e} \\` | 1 | OK | NEW | — |
| SUP-ROW-041 | supplement | table_row | `Resolved-kinematics follow-up denominator & \texttt{SDSS\_REMAINING\_TOPIC\_PILOTS\_20260708T125828Z} & \texttt{m2\_p1\_outflow\_escape\_recycling/analysis\_results.json} & \texttt{44b2407aa691d64fd6de22eb49a8c0a185c86bb1f3b538c7bf066e904d0a3210} \\` | 1 | OK | NEW | — |
| SUP-ROW-042 | supplement | table_row | `Radio-jet environment baseline & \texttt{SDSS\_REMAINING\_TOPIC\_PILOTS\_20260708T125828Z} & \texttt{m2\_p2\_radio\_jet\_environment/analysis\_results.json} & \texttt{4e1ff701bb5b98af4945d5adad2e543e00005e1ab3907e8fae7d15e70c93e351} \\` | 1 | OK | NEW | — |
| SUP-ROW-043 | supplement | table_row | `Stellar-mass selection diagnostic & \texttt{SDSS\_REMAINING\_TOPIC\_PILOTS\_20260708T125828Z} & \texttt{m2\_p3\_feedback\_transition\_mass/analysis\_results.json} & \texttt{204ec46dc838e5e69a34b4dc2f790cb0b5e0f7fc1cb4eaa71f830779a2c92b67} \\` | 1 | OK | NEW | — |
| SUP-ROW-044 | supplement | table_row | `Tracer-threshold census & \texttt{SDSS\_REMAINING\_TOPIC\_PILOTS\_20260708T125828Z} & \texttt{m3\_p1\_multiphase\_census/analysis\_results.json} & \texttt{e711563011102657b6d5cab279c1b2ab7ed087dfc734e50932ad4edfe90d0683} \\` | 1 | OK | NEW | — |
| SUP-ROW-045 | supplement | table_row | `Low-sSFR optical denominator & \texttt{SDSS\_REMAINING\_TOPIC\_PILOTS\_20260708T125828Z} & \texttt{m3\_p2\_gas\_depletion\_efficiency/analysis\_results.json} & \texttt{42965b6f359c23b56098f5f9845561f4a4a2ba81e1e00df09fbae4acf3bcc2d9} \\` | 1 | OK | NEW | — |
| SUP-ROW-046 | supplement | table_row | `Simulation target vector & \texttt{SDSS\_REMAINING\_TOPIC\_PILOTS\_20260708T125828Z} & \texttt{m3\_p3\_simulation\_validation/analysis\_results.json} & \texttt{6f289f8c68da425eb3d8005e673bf5c5c02cf917eaa2bc6feedd053535de8f52} \\` | 1 | OK | NEW | — |
| SUP-ROW-059 | supplement | table_row | `Environment & low-sSFR vs.\ 10th-neighbor rank (60,000 total; 15,000 per quartile) & \texttt{m1\_rp2} \\` | 1 | OK | NEW | — |
| SUP-ROW-060 | supplement | table_row | `Maintenance heating & broad optical BPT-selected hosts in massive low-sSFR galaxies (9,298 massive; 5,695 low-sSFR) & \texttt{m1\_rp3} \\` | 1 | OK | NEW | — |
| SUP-ROW-061 | supplement | table_row | `Outflow kinematics & high-excitation broad optical BPT-selected subset (4,440/60,000) & \texttt{m2\_p1} \\` | 1 | OK | NEW | — |
| SUP-ROW-062 | supplement | table_row | `Env.\ jets & neighbor-rank-stratified broad optical BPT-selected fraction in massive hosts & \texttt{m2\_p2} \\` | 1 | OK | NEW | — |
| SUP-ROW-063 | supplement | table_row | `Mass bin & low-sSFR and broad optical BPT-selected incidence by $M_\star$ bin (15 cells with $n\geq50$) & \texttt{m2\_p3} \\` | 1 | OK | NEW | — |
| SUP-ROW-064 | supplement | table_row | `Tracer census & tracer prevalence in 60k sample (0.136 to 0.418) & \texttt{m3\_p1} \\` | 1 | OK | NEW | — |
| SUP-ROW-065 | supplement | table_row | `Gas depletion & gas-depletion low-sSFR baseline; H$\alpha$ proxy (6,729 galaxies) & \texttt{m3\_p2} \\` | 1 | OK | NEW | — |
| SUP-ROW-066 | supplement | table_row | `Simulation vector & mass-redshift target vector (15 cells with $n\geq50$) & \texttt{m3\_p3} \\` | 1 | OK | NEW | — |
| SUP-ROW-176 | supplement | table_row | `8.0--9.5 & 0.02--0.05 & 6,201 & 0.006 & 0.003 & 1.532 \\` | 1 | OK | NEW | — |
| SUP-ROW-177 | supplement | table_row | `8.0--9.5 & 0.05--0.08 & 1,638 & 0.001 & 0.001 & 1.379 \\` | 1 | OK | NEW | — |
| SUP-ROW-178 | supplement | table_row | `8.0--9.5 & 0.08--0.12 & 300 & 0.007 & 0.010 & 1.045 \\` | 1 | OK | NEW | — |
| SUP-ROW-179 | supplement | table_row | `9.5--10.0 & 0.02--0.05 & 3,607 & 0.061 & 0.030 & 1.854 \\` | 1 | OK | NEW | — |
| SUP-ROW-180 | supplement | table_row | `9.5--10.0 & 0.05--0.08 & 6,059 & 0.013 & 0.008 & 1.696 \\` | 1 | OK | NEW | — |
| SUP-ROW-181 | supplement | table_row | `9.5--10.0 & 0.08--0.12 & 2,187 & 0.003 & 0.001 & 1.516 \\` | 1 | OK | NEW | — |
| SUP-ROW-182 | supplement | table_row | `10.0--10.5 & 0.02--0.05 & 2,962 & 0.256 & 0.154 & 2.264 \\` | 1 | OK | NEW | — |
| SUP-ROW-183 | supplement | table_row | `10.0--10.5 & 0.05--0.08 & 7,581 & 0.161 & 0.090 & 2.119 \\` | 1 | OK | NEW | — |
| SUP-ROW-184 | supplement | table_row | `10.0--10.5 & 0.08--0.12 & 8,593 & 0.062 & 0.040 & 1.920 \\` | 1 | OK | NEW | — |
| SUP-ROW-185 | supplement | table_row | `10.5--11.0 & 0.02--0.05 & 1,895 & 0.581 & 0.430 & 2.623 \\` | 1 | OK | NEW | — |
| SUP-ROW-186 | supplement | table_row | `10.5--11.0 & 0.05--0.08 & 5,083 & 0.451 & 0.297 & 2.580 \\` | 1 | OK | NEW | — |
| SUP-ROW-187 | supplement | table_row | `10.5--11.0 & 0.08--0.12 & 9,861 & 0.326 & 0.209 & 2.455 \\` | 1 | OK | NEW | — |
| SUP-ROW-188 | supplement | table_row | `11.0--12.5 & 0.02--0.05 & 390 & 0.856 & 0.610 & 2.830 \\` | 1 | OK | NEW | — |
| SUP-ROW-189 | supplement | table_row | `11.0--12.5 & 0.05--0.08 & 1,199 & 0.805 & 0.563 & 2.851 \\` | 1 | OK | NEW | — |
| SUP-ROW-190 | supplement | table_row | `11.0--12.5 & 0.08--0.12 & 2,444 & 0.672 & 0.485 & 2.838 \\` | 1 | OK | NEW | — |
