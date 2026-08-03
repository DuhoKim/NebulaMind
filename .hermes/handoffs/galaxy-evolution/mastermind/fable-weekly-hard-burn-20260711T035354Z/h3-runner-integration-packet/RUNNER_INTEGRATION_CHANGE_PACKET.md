FABLE_HARD_BURN_H3_INTEGRATION_PACKET_20260711T035354Z

# Runner/manuscript integration change-packet — rollup follow-up item 3

Burn `fable-weekly-hard-burn-20260711T035354Z`, lane H3. Written 2026-07-11 ≈04:30Z. **Proposal only — nothing here is applied.** Every referenced live file was read read-only; the running sprint (PID 45665, checked alive `Ss+` at 04:05Z) was not touched.

Live targets (read-only, hashes at read time 04:05–04:30Z):
- Runner/audit/prompt file: `<S>/run_weekend_journal_sprint.py` — 50,295 bytes, sha256 `b6795c05f3b790cc22644addcf2c42f7da33387d986f683c7193ccf94450efa2`, where `<S> = /Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_WEEKEND_48H_20260710T110009Z`
- Canon base package: `<S>/candidates/cycle_05_package/` (flagship + supplement TeX; snapshot copies hash-pinned in P1 receipt: flagship `63b3920e…`, supplement `a4e3d66c…`)
- Manifest: prior burn `p1-rp1-invariants/INVARIANT_MANIFEST.json`, sha256 `f4eb857e8cc2002208b1d89a8c517d30e044ed5f7c08a3dab976c0bd7556c717` (verified before use)

**Live status update discovered during preparation (read-only greps, 04:17–04:30Z), strengthening urgency:** the livelock is still active and has *widened* beyond the RCA's two cycles:
- `cycle_08` (results phase): flagship carries `[-1.334,-1.282]` ×4 and supplement `2.831` — the same re-derivation signature; `CYCLE_08_results_AUDIT.json` fails with `numeric_invariants_missing: ["[-1.334,-1.283]"]`.
- `cycle_09` (discussion phase, rebuilt from clean base): canon strings restored (`-1.283` ×4, `2.830`), but `CYCLE_09_discussion_AUDIT.json` fails with `numeric_invariants_missing: ["249,917", "24.0"]` — grep confirms both strings are **gone entirely** from the cycle-9 flagship. This is a third failure mode: outright deletion/rewording of canon numerals (carry-rule §5.5 class), not re-rounding.

Three distinct drift classes have now each caused a cycle failure: re-rounding (6,7,8), aggregate/referent rewrite (6), deletion (9). Sections (a) and (b) close all three.

---

## (a) Proposed extension of the runner audit `numeric_invariants` list

**Current live list** (`run_weekend_journal_sprint.py` line 109, verbatim):

```python
NUMERIC_INVARIANTS = ["8,146", "-1.309", "[-1.334,-1.283]", "249,917", "60,000", "24.0"]
```

**Check mechanism** (line 281): `"numeric_invariants_missing": [x for x in NUMERIC_INVARIANTS if x not in flagship_text]` — presence-only substring test against the **flagship text only**; any hit becomes integrity blocker `numeric invariants missing` (line 319). Two consequences the extension must respect: (1) supplement entries are dead weight unless the metrics line also tests `supplement_text`; (2) the audit is presence-level, weaker than the manifest's occurrence counts — the manifest pre-audit gate (RCA §5.6) remains the count-level check; this list is the runner-side backstop.

### (a.1) Coverage stats (mechanically derived by `tools/derive_audit_extension.py`; cross-validated 105/105 against the hash-pinned cycle-5 snapshot, 0 problems)

- Manifest entries: 105 total = 23 flagship + 82 supplement; 97 substring-mode + 8 numeric_token-mode.
- Already covered by the live 6-entry list (presence-level, flagship only): 5 manifest entries.
- Proposed NEW audit entries: 17 flagship + 75 supplement (0 exact-duplicate strings removed; 8 numeric_token entries routed to the manifest gate instead of the audit list; 15 of the new entries are presence-implied by a longer proposed entry and retained anyway).
- Proposed list sizes: NUMERIC_INVARIANTS 6 -> 23; SUPPLEMENT_NUMERIC_INVARIANTS 0 -> 75.
- Reverse check (live entry -> manifest): `8,146` -> FLG-8146; `-1.309` -> FLG-MEDIAN-OFFSET; `[-1.334,-1.283]` -> FLG-CI95; `249,917` -> FLG-PARENT; `60,000` -> FLG-60000; `24.0` -> substring of FLG-COVERAGE
- Cross-validation against cycle-5 snapshot TeX: 105/105 entries verified (substring entries: exact occurrence count; numeric_token entries: presence).
- PROBLEMS: 0 (none)

### (a.2) Proposed lists — exact entries, audit's own format (paste-ready)

Every string below is a Python literal exactly as it must appear in the script; comments carry the manifest id it implements. The 8 `numeric_token` manifest entries (short bare numerals like `0.5`, ambiguous as substrings) are deliberately **excluded** from the audit lists and routed to the manifest gate; they are enumerated at the end of the block.

```python
# --- proposed replacement for run_weekend_journal_sprint.py line 109 ---
NUMERIC_INVARIANTS = [
    '8,146',  # kept from live list
    '-1.309',  # kept from live list
    '[-1.334,-1.283]',  # kept from live list
    '249,917',  # kept from live list
    '60,000',  # kept from live list
    '24.0',  # kept from live list
    '8{,}146',  # FLG-8146-BRACED
    '95\\%',  # FLG-CI-LEVEL
    '24.0\\%',  # FLG-COVERAGE
    '0.02<z<0.12',  # FLG-ZRANGE
    '1.2--6.5',  # FLG-KPC
    '3-arcsec',  # FLG-FIBER
    'S/N$\\geq3$',  # FLG-SNCUT
    '39,553',  # FLG-SF
    '12,234',  # FLG-COMP
    '100\\%',  # FLG-COVERAGE-PCT
    '0.0045',  # FLG-SEP-LOGM
    '0.00021',  # FLG-SEP-Z
    '\\lambda5007',  # FLG-OIII
    '\\lambda6584',  # FLG-NII
    'SDSS\\_AGN\\_SFR\\_PILOT\\_20260708T122000Z',  # FLG-RUNID
    'DR17',  # FLG-DR17
    'Broad optical BPT-selected targets, S/N$\\geq3$, nearest SF control with replacement & 8,146 & -1.309 & [-1.334,-1.283] & Preferred association estimate \\\\',  # FLG-ROW-057
]

# --- proposed new constant (immediately below NUMERIC_INVARIANTS) ---
SUPPLEMENT_NUMERIC_INVARIANTS = [
    '60,000',  # SUP-60000
    '8,146',  # SUP-8146
    '249,917',  # SUP-PARENT
    '24.0\\%',  # SUP-COVERAGE
    'S/N$\\geq3$',  # SUP-SNCUT-A
    'S/N$\\geq$3',  # SUP-SNCUT-B
    '0.02<z<0.12',  # SUP-ZRANGE
    '55-arcsec',  # SUP-FCOLL
    '3-arcsec',  # SUP-FIBER
    '10th',  # SUP-NEIGHBOR-ORD
    '0.230',  # SUP-ENV-HI
    '3,456/15,000',  # SUP-ENV-HI-RATIO
    '0.181',  # SUP-ENV-LO
    '2,710/15,000',  # SUP-ENV-LO-RATIO
    '[0.041, 0.059]',  # SUP-ENV-CI
    '0.032 +/- 0.004',  # SUP-ENV-COEF
    '15,000',  # SUP-15000
    '9,298',  # SUP-MASSIVE-N
    '5,695',  # SUP-MASSIVE-LOWSSFR-N
    '0.430',  # SUP-BPT-FRAC-MASSIVE
    '0.607',  # SUP-BPT-FRAC-MASSIVE-LOWSSFR
    '4,440',  # SUP-HIEXC-N
    '0.074',  # SUP-HIEXC-FRAC
    '-11.53',  # SUP-HIEXC-SSFR
    '-10.14',  # SUP-FULL-SSFR
    '0.509',  # SUP-JET-HI
    '0.367',  # SUP-JET-LO
    '[0.112, 0.170]',  # SUP-JET-CI
    '[11.0,12.5]',  # SUP-MASSBIN-INT
    '11.0--12.5',  # SUP-MASSBIN-DASH
    '0.520',  # SUP-BPT-PEAK
    '0.136',  # SUP-TRACER-LO
    '0.418',  # SUP-TRACER-HI
    '6,729',  # SUP-GAS-N
    '0.549',  # SUP-GAS-BPT
    '40.061',  # SUP-GAS-LHA
    '0.005-0.729',  # SUP-SPAN-QUENCH
    '0.003-0.520',  # SUP-SPAN-BPT
    '60k',  # SUP-60K
    'SDSS\\_REMAINING\\_TOPIC\\_PILOTS\\_20260708T125828Z',  # SUP-RUNID-TOPICS
    'SDSS\\_AGN\\_SFR\\_PILOT\\_20260708T122000Z',  # SUP-RUNID-PILOT
    '668ad7a67290600ff5028ae587d32ef239a09bd8627a480539f37e1927d659df',  # SUP-SHA-RESULTS
    '4ea53af867cccccb2b68b81557ff84fe90ec3f13e0512ffbdc977fa7216996fd',  # SUP-SHA-PAIRS
    'DR17',  # SUP-DR17
    'Relative neighbor-count baseline & \\texttt{SDSS\\_REMAINING\\_TOPIC\\_PILOTS\\_20260708T125828Z} & \\texttt{m1\\_rp2\\_environment\\_quenching/analysis\\_results.json} & \\texttt{c0421620f67f3c227955affa3f4c1876cb85f8b31874d219f2cd2e35a7f9cec0} \\\\',  # SUP-ROW-039
    'Maintenance-heating denominator & \\texttt{SDSS\\_REMAINING\\_TOPIC\\_PILOTS\\_20260708T125828Z} & \\texttt{m1\\_rp3\\_maintenance\\_heating/analysis\\_results.json} & \\texttt{06291f82c3fbe0f7fe84f7249568882ca4fa44972bcc25a55e367ef1fdcc7e6e} \\\\',  # SUP-ROW-040
    'Resolved-kinematics follow-up denominator & \\texttt{SDSS\\_REMAINING\\_TOPIC\\_PILOTS\\_20260708T125828Z} & \\texttt{m2\\_p1\\_outflow\\_escape\\_recycling/analysis\\_results.json} & \\texttt{44b2407aa691d64fd6de22eb49a8c0a185c86bb1f3b538c7bf066e904d0a3210} \\\\',  # SUP-ROW-041
    'Radio-jet environment baseline & \\texttt{SDSS\\_REMAINING\\_TOPIC\\_PILOTS\\_20260708T125828Z} & \\texttt{m2\\_p2\\_radio\\_jet\\_environment/analysis\\_results.json} & \\texttt{4e1ff701bb5b98af4945d5adad2e543e00005e1ab3907e8fae7d15e70c93e351} \\\\',  # SUP-ROW-042
    'Stellar-mass selection diagnostic & \\texttt{SDSS\\_REMAINING\\_TOPIC\\_PILOTS\\_20260708T125828Z} & \\texttt{m2\\_p3\\_feedback\\_transition\\_mass/analysis\\_results.json} & \\texttt{204ec46dc838e5e69a34b4dc2f790cb0b5e0f7fc1cb4eaa71f830779a2c92b67} \\\\',  # SUP-ROW-043
    'Tracer-threshold census & \\texttt{SDSS\\_REMAINING\\_TOPIC\\_PILOTS\\_20260708T125828Z} & \\texttt{m3\\_p1\\_multiphase\\_census/analysis\\_results.json} & \\texttt{e711563011102657b6d5cab279c1b2ab7ed087dfc734e50932ad4edfe90d0683} \\\\',  # SUP-ROW-044
    'Low-sSFR optical denominator & \\texttt{SDSS\\_REMAINING\\_TOPIC\\_PILOTS\\_20260708T125828Z} & \\texttt{m3\\_p2\\_gas\\_depletion\\_efficiency/analysis\\_results.json} & \\texttt{42965b6f359c23b56098f5f9845561f4a4a2ba81e1e00df09fbae4acf3bcc2d9} \\\\',  # SUP-ROW-045
    'Simulation target vector & \\texttt{SDSS\\_REMAINING\\_TOPIC\\_PILOTS\\_20260708T125828Z} & \\texttt{m3\\_p3\\_simulation\\_validation/analysis\\_results.json} & \\texttt{6f289f8c68da425eb3d8005e673bf5c5c02cf917eaa2bc6feedd053535de8f52} \\\\',  # SUP-ROW-046
    'Environment & low-sSFR vs.\\ 10th-neighbor rank (60,000 total; 15,000 per quartile) & \\texttt{m1\\_rp2} \\\\',  # SUP-ROW-059
    'Maintenance heating & broad optical BPT-selected hosts in massive low-sSFR galaxies (9,298 massive; 5,695 low-sSFR) & \\texttt{m1\\_rp3} \\\\',  # SUP-ROW-060
    'Outflow kinematics & high-excitation broad optical BPT-selected subset (4,440/60,000) & \\texttt{m2\\_p1} \\\\',  # SUP-ROW-061
    'Env.\\ jets & neighbor-rank-stratified broad optical BPT-selected fraction in massive hosts & \\texttt{m2\\_p2} \\\\',  # SUP-ROW-062
    'Mass bin & low-sSFR and broad optical BPT-selected incidence by $M_\\star$ bin (15 cells with $n\\geq50$) & \\texttt{m2\\_p3} \\\\',  # SUP-ROW-063
    'Tracer census & tracer prevalence in 60k sample (0.136 to 0.418) & \\texttt{m3\\_p1} \\\\',  # SUP-ROW-064
    'Gas depletion & gas-depletion low-sSFR baseline; H$\\alpha$ proxy (6,729 galaxies) & \\texttt{m3\\_p2} \\\\',  # SUP-ROW-065
    'Simulation vector & mass-redshift target vector (15 cells with $n\\geq50$) & \\texttt{m3\\_p3} \\\\',  # SUP-ROW-066
    '8.0--9.5 & 0.02--0.05 & 6,201 & 0.006 & 0.003 & 1.532 \\\\',  # SUP-ROW-176
    '8.0--9.5 & 0.05--0.08 & 1,638 & 0.001 & 0.001 & 1.379 \\\\',  # SUP-ROW-177
    '8.0--9.5 & 0.08--0.12 & 300 & 0.007 & 0.010 & 1.045 \\\\',  # SUP-ROW-178
    '9.5--10.0 & 0.02--0.05 & 3,607 & 0.061 & 0.030 & 1.854 \\\\',  # SUP-ROW-179
    '9.5--10.0 & 0.05--0.08 & 6,059 & 0.013 & 0.008 & 1.696 \\\\',  # SUP-ROW-180
    '9.5--10.0 & 0.08--0.12 & 2,187 & 0.003 & 0.001 & 1.516 \\\\',  # SUP-ROW-181
    '10.0--10.5 & 0.02--0.05 & 2,962 & 0.256 & 0.154 & 2.264 \\\\',  # SUP-ROW-182
    '10.0--10.5 & 0.05--0.08 & 7,581 & 0.161 & 0.090 & 2.119 \\\\',  # SUP-ROW-183
    '10.0--10.5 & 0.08--0.12 & 8,593 & 0.062 & 0.040 & 1.920 \\\\',  # SUP-ROW-184
    '10.5--11.0 & 0.02--0.05 & 1,895 & 0.581 & 0.430 & 2.623 \\\\',  # SUP-ROW-185
    '10.5--11.0 & 0.05--0.08 & 5,083 & 0.451 & 0.297 & 2.580 \\\\',  # SUP-ROW-186
    '10.5--11.0 & 0.08--0.12 & 9,861 & 0.326 & 0.209 & 2.455 \\\\',  # SUP-ROW-187
    '11.0--12.5 & 0.02--0.05 & 390 & 0.856 & 0.610 & 2.830 \\\\',  # SUP-ROW-188
    '11.0--12.5 & 0.05--0.08 & 1,199 & 0.805 & 0.563 & 2.851 \\\\',  # SUP-ROW-189
    '11.0--12.5 & 0.08--0.12 & 2,444 & 0.672 & 0.485 & 2.838 \\\\',  # SUP-ROW-190
]

# --- NOT in the audit lists: numeric_token manifest entries (manifest gate only) ---
#   FLG-UNCLASS: '67'
#   SUP-ENV-PP: '3.2'
#   SUP-MASSCUT: '10.8'
#   SUP-HALF: '0.5'
#   SUP-TRACER-RATIO: '3.1'
#   SUP-GAS-DEX: '0.66'
#   SUP-CELLS: '15'
#   SUP-CELL-MIN: '50'
```

**Required mechanism change (one line, same blocker key)** — without it the supplement list is never evaluated. In `journal_metrics()` (live line 281), replace:

```python
        "numeric_invariants_missing": [x for x in NUMERIC_INVARIANTS if x not in flagship_text],
```

with:

```python
        "numeric_invariants_missing": [x for x in NUMERIC_INVARIANTS if x not in flagship_text]
        + [x for x in SUPPLEMENT_NUMERIC_INVARIANTS if x not in supplement_text],
```

`classify_integrity_blockers()` needs no change (it already fires on a non-empty list). Note for the integrator: the running process loaded these constants at start; editing the script does **not** affect PID 45665 mid-run. Apply at sprint end or as the seed config of the next sprint (see section d).

### (a.3) Mapping table — manifest entry → audit entry (all 105 entries)

Legend: "covered" = already caught presence-level by the live 6-entry list (flagship only); "NEW" = added by this proposal; `numeric_token` rows are manifest-gate-only. Cycle-5 check = exact occurrence count against the hash-pinned snapshot (token rows: presence).

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

---

## (b) Verbatim-carry rule — prose-phase prompt patch

The prose-phase prompt is assembled in the live runner file (`<S>/run_weekend_journal_sprint.py`, sha256 `b6795c05f3b790cc22644addcf2c42f7da33387d986f683c7193ccf94450efa2`) from two functions: `base_prompt()` (lines 466–486, shared by all reviewer lanes, the analyst, the integrator, and the post-fix referee) and `integrator_prompt()` (lines 669–688, the **single writer lane** — the only lane that edits the TeX, so the only place drift is created). The patch touches both: the shared contract line, and a binding writer-side block.

### (b.1) Exact current text — `base_prompt()` (live lines 466–486, quoted verbatim)

```python
def base_prompt(phase: str, candidate: Path) -> str:
    return f"""Phase: {phase}
Sprint: {SPRINT_ID}
Candidate root: {candidate}

Safety locks:
{chr(10).join('- ' + x for x in SAFETY_LOCKS)}

Real-data rules:
{chr(10).join('- ' + x for x in REAL_DATA_RULES)}

Required review behavior:
- Inspect {candidate / 'provenance/REAL_DATA_SOURCE_CUSTODY.json'} before declaring provenance absent; it inventories real source paths, hashes, and row counts without copying the source data.
- Demand concrete section-level improvements for the flagship and supplement.
- Provide real source identifiers for literature suggestions: DOI, arXiv, ADS bibcode, URL, journal volume/page, or explicit "unverified / do not integrate".
- Preserve exact numeric invariants and association-only boundaries.
- Separate integrity blockers from journal-quality blockers.
- End with exactly one verdict line: JOURNAL_LEVEL_PASS: YES or JOURNAL_LEVEL_PASS: NO.
"""
```

The operative sentence today is the single bullet `- Preserve exact numeric invariants and association-only boundaries.` — cycles 6, 7, 8, and 9 prove it does not communicate "verbatim string carry": writers read it as "keep the values right" and re-derive.

### (b.2) Exact proposed replacement — `base_prompt()`

Replace **only** the bullet `- Preserve exact numeric invariants and association-only boundaries.` with the following two bullets (rest of the function byte-identical):

```
- Numeric verbatim-carry contract: every numeral, interval, percentage, SHA-256, and run-ID string already present in the base package is an opaque string. Carry it character-for-character, including formatting ('8,146' vs '8{,}146', 'S/N$\geq3$' vs 'S/N$\geq$3', '[-1.334,-1.283]' spacing). Never re-derive, re-round, reformat, relocate the referent of, or delete such a string - even when recomputation from the custody artifacts looks arithmetically more correct. If a base numeral looks wrong, STOP and report it in your response; do not fix it inline.
- Preserve association-only boundaries.
```

(ASCII hyphen-minus throughout; the block is inside an f-string — it contains no `{`/`}` so no escaping is needed.)

### (b.3) Exact current text — `integrator_prompt()` role block (live lines 669–688, quoted verbatim)

```python
def integrator_prompt(phase: str, cycle: int, candidate: Path, reports: list[Path]) -> str:
    report_text = []
    for path in reports:
        report_text.append(f"\n\n===== {path.name} =====\n{read_text(path, 40_000)}")
    allowed = "\n".join(f"- {candidate / rel}" for rel in TEX_RELATIVES)
    return base_prompt(phase, candidate) + f"""
Role: single manuscript integrator for cycle {cycle}.

You may edit only:
{allowed}
- candidate-local analysis artifacts under {candidate / 'analysis_extensions'} when needed for provenance references.

The real-data analyst and integrator must not overlap; analyst has already finished or was skipped.
Return a concise final response through the CLI output; do not create a separate response file in the candidate.
Do not add padding merely to hit word/count targets. Refuse absent measurements instead of inventing them.

Reviewer reports:
{''.join(report_text)}
"""
```

### (b.4) Exact proposed replacement — `integrator_prompt()`

Insert the following block into the returned f-string, immediately after the line `Do not add padding merely to hit word/count targets. Refuse absent measurements instead of inventing them.` and before `Reviewer reports:` (rest of the function byte-identical; block contains no `{`/`}`):

```
Numeric verbatim-carry rule (binding; cycles 6-9 all failed audit by violating it):
1. Copy, never re-derive: every numeric string in the base TeX is copied character-for-character. Prose around numbers may change; the numeric strings may not.
2. No re-rounding, ever: do not recompute any number from artifacts, tables, or memory. A re-derived value that differs from the base string is a defect even when arithmetically correct. If a base numeral looks wrong, STOP and report; never fix inline.
3. No deletions or rewordings of numeral occurrences (e.g. '249,917', '24.0\%'): removing or paraphrasing one is a numeric change and is out of scope for a prose phase.
4. Referents are invariant: do not change what a quantitative sentence ranges over (e.g. 'across mass bins' vs 'across the displayed table').
5. New numerals only with provenance: a new number is allowed only if your final response states the custody-inventoried artifact and field it comes from, so it can be registered in the invariant manifest.
6. Self-check before finishing: verify every NUMERIC_INVARIANTS string still appears in the flagship TeX and every SUPPLEMENT_NUMERIC_INVARIANTS string in the supplement TeX, unchanged; if any check fails, restore the exact base string.
```

Rules 1–5 are RCA §5.1–§5.5 verbatim in intent; rule 6 is the writer-side mirror of the audit in section (a). The manifest-based pre-audit gate (RCA §5.6, occurrence-count level, via `INVARIANT_MANIFEST.json` + a check script) sits between writer and audit in the cycle loop — that is rollup follow-up item 3's "manifest into the pre-audit flow" and is orchestration, not prompt text; it needs a `run_cycle`-level hook and is listed in section (d) ordering.

---

## (c) Canon adjudication memo — `-1.283` vs `-1.282` and `2.830` vs `2.831`

**Question.** Cycle-5 canon (and the audit list) carry flagship CI `[-1.334,-1.283]` and supplement cell `2.830`. The custody artifacts give raw `-1.2821399375` (nearest 3-dp `-1.282`) and raw `2.83066` (nearest 3-dp `2.831`). Adopt the artifact-nearest strings, or keep canon?

**Evidence for ADOPTING `-1.282` / `2.831` (from RCA, plus live state):**
- RCA E1/E3: the raw custody values nearest-round to `-1.282` and `2.831`. RCA E2: these are the **only two** canon strings (of 105) that are not nearest-roundings of their own artifacts — every other flagship scalar (`-1.309`←`-1.308887`, `0.0045`←`0.00446`, `0.00021`←`0.000210795`) and neighboring table cells (`2.85057→2.851`, `2.83792→2.838`) are nearest-rounded. Canon's `-1.283` is producible only by floor-toward-−∞; `2.830` is a truncation. Both look like cycle-5 mis-roundings, not choices.
- RCA E4 + live cycles 8: four independent prose cycles (6, 7, 8) re-derived and emitted `-1.282` at the same four locations (cycle 8 also `2.831`) — the re-derivation pressure is deterministic and permanent. Keeping canon means every future prose phase must fight its own arithmetic; adopting nearest makes regeneration converge to canon.
- Directional conservatism: `[-1.334,-1.282]` is the *wider* interval; the current canon upper bound `-1.283` was truncated toward the interval interior, i.e. slightly anti-conservative. Adopting nearest cannot be criticized as strengthening the claim.
- Policy simplicity: one stated convention — "every printed value is the nearest-rounding (half away from zero) of its custody-artifact value at printed precision" — makes all 105 invariants mechanically re-derivable and auditable.

**Evidence for KEEPING `-1.283` / `2.830`:**
- Canon-is-canon (RCA §3.2.1): cycle 5 is the only audited clean base (`integrity_blockers: []`); it anchors every hash, snapshot, receipt, and downstream artifact (P2 comparison candidate and P4 claim candidates quote `[-1.334,-1.283]` verbatim). A canon edit ripples into all of them.
- The difference is scientifically nil (last digit of a bootstrap CI bound; one supplement color cell). Zero reader impact, non-zero operational risk: the change touches 4 flagship locations + 1 supplement cell + audit list + manifest, and a *partial* application recreates the livelock in reverse (writer carries new canon, audit demands old — or vice versa).
- The cleanest possible carry-contract precedent is "numeric strings never change, full stop"; adjudicating even a justified change weakens the rule's teaching value at the exact moment it is being installed.
- With the verbatim-carry prompt patch (b) in place, re-derivation pressure should disappear anyway — the livelock argument loses force *if* the prompt patch works.

**Recommendation: ADOPT `-1.282` / `2.831` (Option B), executed only as the atomic three-surface change below, in the same integrator window as (a)+(b).** Rationale: the keep-side's strongest point (prompt patch may suffice) leaves canon permanently mis-rounded against its own artifacts and dependent on prompt compliance by every future model; the adopt-side fixes the root inconsistency once, is conservative in direction, and the ripple risk is exactly what the atomic checklist eliminates. **Until Duho approves, canon stands:** candidates must reproduce `-1.283`/`2.830` character-for-character, and P2/P4 downstream artifacts correctly quote current canon.

**Atomic-change checklist (three surfaces change together or not at all):**

Surfaces: (S1) base-package manuscript TeX; (S2) runner audit list — `NUMERIC_INVARIANTS` line 109 (+ proposed `SUPPLEMENT_NUMERIC_INVARIANTS`); (S3) `INVARIANT_MANIFEST.json`.

0. Preconditions: written Duho approval of Option B; runner idle (sprint ended or between cycle slots — the running PID does not reload the script, so S2 lands at sprint end / next-sprint seed; do NOT edit mid-sprint expecting live effect).
1. Freeze: record sha256 of S1 (both TeX), S2 (runner script), S3 (manifest).
2. Identify the current clean base package at execution time (today `cycle_05_package`; re-verify with `grep -F -c -- '[-1.334,-1.283]' <flagship.tex>` → 4 and `grep -F -c -- ' 2.830 ' <supplement.tex>` → 1).
3. S1 flagship: replace all 4 occurrences `[-1.334,-1.283]` → `[-1.334,-1.282]` (lines 13/57/65/74: abstract, Table-1 row, `$…$` Fig.-2 caption, conclusion).
4. S1 supplement: line 188 row cell `2.830` → `2.831` (the `11.0--12.5 & 0.02--0.05 & 390 & 0.856 & 0.610 & 2.830 \\` row).
5. S2: in `NUMERIC_INVARIANTS`, `'[-1.334,-1.283]'` → `'[-1.334,-1.282]'`; in the extended lists (section a), update `FLG-ROW-057`'s row string (contains the CI) and `SUP-ROW-188`'s row string (contains `2.830`) to the new cell values.
6. S3: update entries `FLG-CI95` and `FLG-ROW-057` (flagship) and the line-188 table-row entry `SUP-ROW-188` (supplement) to the new exact strings; delete/annotate `known_rounding_anomalies`; add the convention line ("printed values are nearest-roundings, half away from zero, of custody-artifact values at printed precision"); regenerate counts with P1's `tools/build_manifest.py` if preferred.
7. Verify: `tools/derive_audit_extension.py` (this packet) against the edited files → 105/105, 0 problems; grep acceptance: old strings count 0 everywhere, new strings count 4 (flagship CI) and 1 (supplement cell); dry-run `journal_metrics()` on the base → `numeric_invariants_missing: []`.
8. Record new sha256s of S1/S2/S3 beside the step-1 values in the change receipt; downstream note: P2 comparison candidate and P4 claim candidates quote the old CI string — mark them "re-quote from canon at integration" (section d).
9. Rollback (any step fails or any check mismatches): restore S1+S2+S3 from the step-1 snapshot byte-exact, verify hashes match step-1, state PARTIAL-REVERTED in the receipt. Never leave the three surfaces disagreeing.

---

## (d) Integration sequencing

Dependency-ordered; each step is separately gated (rollup: "every item GATED, needs separate Duho approval").

1. **Decide (c) first** — it determines the CI/cell strings that (a)'s lists and (S1) manuscripts carry. A "keep canon" decision costs nothing (lists below already carry current canon); an "adopt" decision folds the checklist in (c) into step 2's window.
2. **One integrator window applies (a) + (b) [+ (c) if adopted] together** at a runner-idle boundary (sprint end / next-sprint seed — the live PID 45665 never reloads the script). (a) and (b) are the gate side and writer side of the same contract: shipping the audit extension without the prompt patch produces hard-fails on every prose phase (cycles 6–9 show base-rate ~4/4); shipping the prompt patch without the audit extension leaves supplement drift (D2/D3 class) invisible. The manifest pre-audit gate (RCA §5.6; `INVARIANT_MANIFEST.json` + count-level checker between writer and audit) belongs to this same window as orchestration work.
3. **Verification artifacts for step 2** are in this packet: paste-ready lists (a.2), one-line metrics change (a.2), exact prompt texts before/after (b), and `tools/derive_audit_extension.py` as the cross-validator (105/105 green precondition for merge).
4. **P2 prior-work comparison candidate — integrates only after the network pass (rollup follow-up item 1) upgrades its leads.** Its own GATE block requires (1) the approved network-verification pass over the `NEEDS_NETWORK_VERIFICATION` ledger entries it cites (N01, N05, … — 39 leads in `SOURCE_LEAD_LEDGER.json`), and (2) a separate integrator approval; bracketed status tags travel with the text until then. Additional dependency introduced by this packet: it quotes `[-1.334,-1.283]` verbatim from cycle-5 canon — if (c) adopts Option B, re-quote its RP-1 numerals from post-adjudication canon before insertion; after insertion, register any adopted external (prior-work) values in the manifest per RCA §5.3. Note: its target blocker (`missing explicit quantitative comparison to prior work`) is a *quality* blocker, so sequencing it late costs pass-rate but not integrity.
5. **Same gating class, listed for completeness:** literature EXT-1..EXT-4 quantitative slots in `INTRODUCTION_LITERATURE_REFERENCE.md` (sha256 verified this burn) also wait on follow-up item 1 + manifest registration; P4 wiki-side candidates are item 4, independent of this packet.
6. **After the first post-integration cycle:** confirm the audit JSON shows `numeric_invariants_missing: []` with the extended lists, and that the integrator's self-check (b.4 rule 6) appears in its lane report; then the manifest gate's occurrence-level counts become the promotion criterion, per RCA §5.6.

Sequencing summary: **(c) decision → [(a)+(b)(+c-apply)] one atomic runner-side window → item-1 network pass → P2 candidate + EXT slots (with manifest registration) → subsequent cycles under the full contract.**

---

Prepared offline by Fable lane H3; no file outside `h3-runner-integration-packet/` was created or modified; the runner tree, candidates, manuscript, audit config, and repo were read-only throughout. Custody, hashes, and poll log: `H3_RECEIPT.md`.

FABLE_HARD_BURN_H3_INTEGRATION_PACKET_20260711T035354Z
