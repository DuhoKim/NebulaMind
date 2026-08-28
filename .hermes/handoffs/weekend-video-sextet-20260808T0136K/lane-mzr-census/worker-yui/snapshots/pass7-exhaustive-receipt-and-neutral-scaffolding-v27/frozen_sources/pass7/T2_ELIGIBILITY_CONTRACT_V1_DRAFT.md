# T2 ELIGIBILITY CONTRACT v1.8 — **FROZEN** 2026-08-06

Status: **FROZEN — sha256-pinned and chmod 444.** Frozen on Duho's instruction after
`KUN_T2_REGATE7.md` returned **T2 EVIDENCE RE-GATE 7: PASS** on this exact text (49-span
full-denotation diff clean, definition sentence true, all fifteen controls verified against the
pinned manifest).

The header is updated as the freeze act itself and nothing else in the text is touched: the gate
passed on these bytes, and editing a passed contract before freezing it is the drift this lane
exists to prevent. Lana's recommendations (`LANA_MZR_SCIENCE_RULING.md`) are therefore the
amendment agenda under §2b, NOT silent edits — see `FREEZE_RECORD_T2.md`.

Lane: `mzr-archive-census-20260805T1857K`. Stage: T2, the eligibility layer that rules E1–E4 on
T1's 157 candidates. **Status: DRAFT.** It is not in force and no T2 ruling logic may be written
until it is gated and frozen (§5).

## 1. Inheritance

Inherits `MZR_CENSUS_CONTRACT_V1.md` (frozen, sha `84e1d9b6ed147dd0…`, chmod 444) unchanged.
**That contract is not edited, amended, or re-hashed by this document.** T2 rules from the
evidence recorded in `T1_MZR_MANIFEST.json` — the `ucd` and verbatim `description` of each
identified column — and fetches nothing new (census contract §5/F8).

Inputs pinned at freeze: `T1_MZR_MANIFEST.json` (157 candidates, 178 pre-filter, 21 dropped,
status `DONE`, 0 channels failed) and `T1_FINDINGS.md`.

## 2. Why this contract exists: no control covers axis-passing semantic contamination

The census contract's §6 [E3] froze R1–R7 with controls C1–C3. All passed: 7/7 members returned,
0/3 controls appeared. The census **did** freeze a precision control — its own §6.3 labels C1 that. But C1 —
`J/ApJ/765/140/spectra`, "present, but no redshift axis across all 58 columns" — tests a
**missing axis**, and is excluded by the three-axis intersection itself. Nothing in the frozen set tests the failure that
T1 actually exhibits: a table that **satisfies all three axes on symbol matching and is
semantically wrong**. Recall controls and precision controls are different instruments; the lane
froze the first and must now freeze the second, **before** T2's ruling logic exists.

## 3. Precision decoys — T2 MUST EXCLUDE all twelve (D1–D3 here; D4–D12 in §3b) [P-D]

Chosen to span three *distinct mechanisms*, not three instances of one. Each is in T1's manifest
and each is disqualified by evidence T1 already recorded.

| id | table | mechanism | recorded evidence that disqualifies it |
|---|---|---|---|
| **D1** | `J/A+A/453/769/grid` | **composition-Z**: a stellar-evolution model grid, no observations at all | `X` = `phys.abund.X`, *"[…] X initial X composition (H)"*; `M`/`logM` = `phys.mass`, *"Initial mass"*; `Z` = `src.redshift;phys.composition`, *"[…] Z initial composition"* |
| **D2** | `I/349/starhorse` | **coordinate-Z**: a Galactic stellar catalogue whose "redshift" is a spatial coordinate | `met16/50/84` = `phys.abund.Fe`, *"StarHorse metallicity […]"*; `mass16/50/84` = *"StarHorse stellar mass […]"*; `ZGal` = `src.redshift;pos.galactocentric;pos.cartesian`, *"[…] Galactocentric Cartesian Z co-ordinate […]"* |
| **D3** | `J/MNRAS/514/1071/primary` | **gravitational-z**: a real redshift that is not cosmological, on individual stars | `[Fe/H]1/2` = `phys.abund.Fe;arith.ratio`; `M1/M2` = `phys.mass;meta.modelled;arith`, *"Estimated mass of the … comoving star […]"*; `vGR1/vGR2` = `src.redshift;pos.heliocentric;arith`, *"Gravitational redshift velocity of the first comoving star defined as G*M1/R1 […]"* — quoted in full because the elided tail DEFINED the quantity |

**[S6] What "exclude" means here, stated because the inherited vocabulary makes it
load-bearing.** Census §2 defines EXCLUDED as an E1 failure *only*, and routes F1/F2 strata to
CENSUS-ONLY under a named rule. D1–D3 pass E1 *as symbol-matched*, so a T2 applying the inherited
vocabulary literally would route all three to CENSUS-ONLY — and a grader reading this section
could call that a failure. It is not. **"Exclude" in §3 and §6 means any disposition other than
ELIGIBLE.** The expected named rule per decoy: **D1** → F2 census-only (model grid; it also
fails E1 semantically, and the double-routing is expected, not an error); **D2** and **D3** →
F1 species/phase (stellar, not galaxy gas-phase). 
### 3b. Extended decoys [E1] — the classes D1–D3 left uncovered. Also MUST EXCLUDE.

The evidence gate established that D1–D3, though genuinely distinct, all fail on the **redshift**
axis, and that a three-keyword rule passes the original six. These close the named holes. Every
cell below was read from the candidate's **complete** column list, not a truncated view — the
failure mode that produced the P3 error in §4.

| id | table | mechanism, and why it is harder than D1–D3 | recorded evidence |
|---|---|---|---|
| **D4** | `J/A+A/703/A228/table1` | **composition-Z with a BARE UCD.** D1 is catchable on its `;phys.composition` qualifier; this one carries no qualifier at all, so any rule keyed to the qualifier misses it. | `Y` = `phys.abund.Y`, *"Helium content"*; `Mass` = `phys.mass`, *"Mass"*; `Z` = **`src.redshift`** (bare), *"Metal content"* |
| **D5** | `J/A+A/679/A131/dataset` | **simulation snapshot.** Every axis looks correct — real metallicity, real stellar mass — and the only tell is one word in the redshift description. | `ZGal` = `phys.abund.Z`, *"Metallicity (Z/Zsun)"*; `Mstellar` = `phys.mass`, *"Stellar mass"*; `z` = `src.redshift`, *"Redshift **snapshot**"* |
| **D6** | `J/ApJ/802/103/table2` | **model of real galaxies.** Worse than D5: the mass column is literally a galaxy stellar mass, so object-class reasoning does not save you — only the word "Model" does. | `logZ` = `phys.abund.Z`, *"[…] Log Metallicity log_10_(Z/Z_{sun}_)"*; `M*` = `phys.mass`, *"[…] GRB host galaxy stellar mass"*; `z` = `src.redshift`, *"[…] **Model** redshift"* |
| **D7** | `J/ApJS/274/36/mdwarfs` | **stellar catalogue with an unmarked redshift.** Unlike D3 the redshift description says only "Redshift" — nothing in the redshift cell betrays it. The tell is the object class, carried in the OTHER axes. | `Fe/H` = `phys.abund.Z`, *"[…] LAMOST DR9 metallicity […]"*; `Mstar` = `phys.mass`, *"[…] Mass from TESS Input Catalog v8.0"*; `z` = `src.redshift`, *"Redshift […]"* |
| **D8** | `J/AJ/107/2240/table6` | **coordinate-Z, second signature.** D2's UCD is `;pos.galactocentric;pos.cartesian`; this is a different tagging of the same mistake, so a rule enumerating D2's exact qualifier set misses it. | `[m/H]` = `phys.abund`, *"[…] Spectroscopic metallicity"*; `M` = `phys.mass`, *"[…] Primary mass"*; `Zm` = **`pos.distance;src.redshift;pos.galactic`**, *"[…] **Maximun** Z distance perpendicular to Galactic disk"* (sic — recorded spelling) |
| **D9** | `J/ApJS/280/57/table6` | **the ABUNDANCE axis fails.** The first decoy that does. Its "abundance" columns are emission-line measurements matched on the `OH` substring in `OHb` (H-beta outflow), and its mass is a black-hole mass. Its redshift is genuinely cosmological — so a redshift-only rule keeps it. | `EWOHb` = `spect.line.eqWidth`, *"[…] Equivalent width of the outflow component of H{beta} […]"*; `logBH` = `phys.mass`, *"[…] The adopted fiducial virial BH mass […]"*; `z` = `src.redshift`, *"[…] Cosmological redshift […]"* |
| **D10** | `J/ApJ/805/3/clusters` | **right quantities, wrong object.** The hardest of all: gas-phase metallicity, mass and redshift are each genuine — of a galaxy **cluster**, not a galaxy. No axis is individually wrong. | `Zin`/`Zmid` = `phys.abund.Z`, *"[…] Bulk core cluster metallicity […]"* / *"[…] Gas-mass-weighted metallicity […]"*; `M500` = `phys.mass`, *"[…] Total gravitational mass within R500"*; `z` = `src.redshift`, *"[…] Cluster redshift"* |

| **D11** | `J/ApJS/275/17/cos-db` | **galaxy-side species/phase — STELLAR metallicity.** [R2] The stratum the whole decoy set was missing: nothing about the object or the axes is wrong. It is a real galaxy with a real stellar mass and a real redshift; only the metallicity is the wrong *phase* for a gas-phase census. Defeats every object-class rule above, and every axis-wise rule keyed to UCD or quantity — though not an abundance-description keyword, nor a `src.redshift.phot` clause. | `logZ` = `phys.abund.Z`, *"[…] Best estimate for **Stellar** metallicity […]"*; `logM` = `phys.mass`, *"[…] Best estimate for Galaxy stellar mass […]"*; `zphot` = `src.redshift.phot`, *"[…] Photometric redshift used for fitting […]"* |
| **D12** | `J/ApJ/898/62/table1` | **galaxy-side species/phase, second signature.** [R2] Stellar-population metallicity under a different vocabulary again (luminosity- and mass-weighted), with an SDSS **spectroscopic** redshift — so a rule keyed to photometric-z or to the word "Stellar" alone misses it. | `[Z/H]L`/`[Z/H]M` = `phys.abund.Z`, *"[…] Luminosity-weighted metallicity"* / *"[…] Mass-weighted metallicity"*; `logM*` = `phys.mass`, *"[…] log10 stellar mass from Kauffmann+ […]"*; `z` = `src.redshift`, *"[…] SDSS spectroscopic redshift"* |

Ellipses mark elided material in the recorded descriptions [E2, R3, S4, S7], including leading range/percentile
prefixes, the VizieR `? ` availability marker, and trailing column-name echoes such as `(G1)`.
**[S6] The convention, met by sweep — completed at the fourth attempt.** All 49 quoted spans in
§3, §3b and §4 were diffed mechanically (48 through re-gate-5; 49 after S7-b split the
`…fmol` quote into its ratio and fraction readings) against their verbatim manifest records. The S5 round
swept 28 and missed 12; those twelve are now marked. Boilerplate elisions — **including** leading
range/percentile prefixes, the VizieR `? ` marker, and trailing column-name echoes — are marked
wherever they occur. **Three** elisions were **substantive** rather than boilerplate and are
quoted **in full** instead of marked, because a mark would hide meaning: D3's `vGR1` (the tail
named which star and gave the formula), P1's `A(O)` (the tail named the instrument and the
scale), and D6's `logZ` (the tail carried the units). Where the manifest stores
LaTeX-style markup literally, the cell reproduces it as recorded: D9 now reads `H{beta}`, which
is what the record holds; the earlier `H-beta` was a silent normalisation.
Text inside the quotes is otherwise **verbatim, typographical errors included** — D8's recorded
description reads "Maximun", and it is reproduced as recorded.

**Why this set is not merely longer.** D4 defeats qualifier-keyed rules, D8 defeats
qualifier-enumeration, D7 defeats redshift-description-keyed rules, D9 defeats redshift-only
rules entirely, and D10 defeats every axis-wise UCD/quantity rule because no single axis is wrong.

**What the re-gates established about this set, recorded honestly.** A seven-keyword denylist
still passed all thirteen controls of v1.2 — the set is strictly stronger than v1.1's but does
NOT by itself force generality. D11/D12 close the largest remaining stratum, and the cheap rule
still marks the **knowingly-undecoyed contaminated** classes ELIGIBLE — the fixed-parameter
catalogues and the `phys.abund`-family line-ratio/gradient tables. [S1: v1.3 recorded this
backwards, as the rule marking genuine gas-phase tables eligible; that would be *correct*
behaviour. The defect is contamination surviving, not clean tables surviving.] The rule is also
not a bare keyword denylist: it is nine keywords **plus three one-line clauses** (a UCD-substring
test, a no-`phys.abund` test, and a mass-range test) — a bare denylist leaves D7, D8 and D9 alive.
**The actual controls on generality are §5.5's
per-clause fire-counts and §5.6's full disposition table, not the control set.** Knowingly left
undecoyed: the fixed-parameter class, and the `phys.abund`-family line-ratio/gradient signature.

A T2 that gives any of D1–D12 the ELIGIBLE
disposition has failed, whatever it does with the rest; which non-ELIGIBLE disposition it
assigns is a separate question it must state and justify.

## 4. Precision anchors — T2 MUST NOT EXCLUDE these [P-A]

A decoy set alone is passable by excluding everything. These are genuine gas-phase extragalactic
tables that *look* like the decoys, and they carry the traps that make §3 non-trivial.

| id | table | why it is genuine | the trap it sets |
|---|---|---|---|
| **P1** | `J/A+A/712/A19/table1` | `A(O)` = `phys.abund`, *"Oxygen abundance derived by the direct Te-method from the Xshooter spectrum (12+log(O/H))"* — quoted in full, the tail is substantive; `logM*` = *"The stellar mass […]"*; `z` = `src.redshift`, *"Redshift […]"* | none — the clean control. If T2 drops P1 it is broken outright. |
| **P2** | `J/A+A/604/A53/sample` | `MPA-JHU`, `N2M13`, `N2PP04` = `phys.abund`, *"[…] Gas-phase metallicity …calibration […]"*; `logM*` = *"Stellar mass estimated from optical SDSS observations […]"*; `zopt` = *"Optical spectroscopic redshift […]"* | **the abundance columns are named after surveys and calibrations, not quantities.** Any rule keyed to column NAMES drops P2. Also `logMHI` carries UCD `meta.bib` — a wrong tag on a real column, which T2 must tolerate rather than treat as corruption. **[E3] Its `zopt` also carries `src.redshift;pos.heliocentric` — the same qualifier collision as P3's `zstar` and decoy D3's `vGR1` — so P2 independently traps a qualifier-keyed rule.** |
| **P3** | `J/A+A/699/A366/tablec1` | `BeamGasMet`/`GlobGasMet` = `phys.abund.Z`, *"[…] gas-phase metallicity derived via the O3N2 method […]"*; `zstar` = `src.redshift;pos.heliocentric`, *"Stellar redshift of the galaxy […]"* | **`zstar` shares its `pos.heliocentric` UCD qualifier with decoy D3's `vGR1`, and its NAME contains "star".** A rule that excludes on the qualifier or on the substring kills a real galaxy catalogue. |

**[E3] Correction to the previous draft, recorded rather than quietly replaced.** v1.1 stated
that P3's `phys.mass` columns "are molecular gas masses and a stellar-mass-to-gas-mass ratio".
That was wrong on both counts, and it was wrong because the table was inspected through a
two-column truncation. The complete list carries **`BeamMstar`** (*"Beam stellar mass […]"*) and
**`GlobMstar`** (*"Global stellar mass […]"*), both `phys.mass` — a genuine stellar-mass axis exists.
The ratio columns run the other way, and the `…fmol` glob denotes **eight** columns reading two
ways [S7-b]: the six survey-prefixed ones (ACA/APEX/CARMA × Beam/Global) record
*"[…] molecular gas mass to stellar mass ratio […]"*, while the consolidated-sample pair
(`FinalBeamfmol`, `FinalGlobfmol`) records *"[…] molecular gas mass fraction from the
consolidated sample […]"*. Either way the ratio is molecular-gas-to-stellar, not the inverse.
So P3's mass axis is **not** the open question v1.1 presented, and T2 must not be invited to
deliberate over a gap the evidence does not show.

**P3's redshift-axis expectation is a CONTROL DEFINITION, not a T2 ruling.** [S5] T2 may not
exclude P3 *on the grounds that `zstar` is a stellar quantity* — its redshift axis is a genuine
galaxy redshift. [R1: the v1.1 mass-axis paragraph that stood here is deleted rather than left
beside its own correction; P3's mass axis carries genuine stellar-mass columns and is not the
open question that paragraph described.]

## 5. Anti-circularity [P-C] — the rule this contract exists to enforce

I found D1–D3 by reading T1's output, and I am also the author of T2's ruling logic. That is a
circularity, and these three rules bound it:

1. **T2's exclusion rule is written on recorded evidence only** — `ucd` qualifiers and verbatim
   `description` semantics. **A rule that names any table_id, or that special-cases a decoy or
   anchor by identifier, is an automatic gate FAIL.**
2. **This contract freezes BEFORE T2's ruling logic is written.** Ordering is the control: rules
   tuned to a known answer are what the freeze exists to prevent.
3. **D1–D3 and P1–P3 are not the eligibility criteria.** They are a *test* of the criteria. T2's
   rule must be stated in general terms and must survive **the fifteen**; a rule that passes
   exactly those fifteen and is silent about **the other 142** has not been stated generally
   enough.
4. **[S2a] The adjudicator of §5.3 is frozen now, and is not the rule-author.** "Not stated
   generally enough" is a judgement, and the author may not grade their own generality. **Kun**
   holds it; if Kun authored any part of the ruling logic, **Miru** holds it instead.
5. **[S2b] Per-clause fire-counts are mandatory.** §5.1 bans naming an identifier but not
   *semantic* special-casing — a clause whose trigger fires on exactly the fifteen and nothing else
   is special-casing in general clothing. T2 must report, for every clause of its rule, how many
   of the 157 it fires on. **A clause firing only on control members is flagged as presumptive
   special-casing** and must be justified or rewritten.
6. **[S2c] The complete disposition table is a PASS precondition.** T2 must publish all 157
   candidates with their disposition and the quoted evidence behind each. Without it, a rule that
   mistreats the other 142 need never surface. This is what mechanizes §5.3.

*Recorded for the record:* a held-out control set would NOT be a stronger bound here — the author
has read the whole manifest, so any holdout is already known. Ordering (§5.2) plus independent
adjudication (§5.4) plus fire-counts (§5.5) is the available bound.

## 6. Honest outcomes, defined now

- **PASS**: all **twelve** decoys (D1–D12) given a non-ELIGIBLE disposition, all three anchors retained (P3 on
  its redshift axis), the rule stated generally per §5.3, and **the complete 157-candidate
  disposition table published per §5.6**.
- **FAIL**: any of D1–D12 ELIGIBLE, or **any anchor excluded** — with exclusion on the trap the
  anchor sets as the emphasized case, but not the only one. [S4a: P1 sets no trap, so excluding
  P1 for any reason was previously neither PASS nor FAIL.]
- **[S4a] CONTRACT FINDING — control unruleable**: if the recorded evidence proves insufficient
  to rule a *control* candidate, that is **not** a T2 failure. It is a finding that this contract
  mis-specified the control, and it triggers a re-gate of the contract rather than a silent
  T2 fail.
- **HONEST_FAILURE**: the recorded evidence is insufficient to rule on a candidate. This is a
  **valid terminal state**, and **[S4c] the unruled count must publish its named dominant cause**
  (mirroring census §8(b)), so a degenerate run that leaves most candidates unruled cannot PASS
  on the strength of the fifteen alone and must be reported as a count, never resolved by fetching more or by
  guessing from the table name. A candidate that cannot be ruled is recorded as unruled.
- **[S3a] The gas-phase-evidence count is 62 of 157, and it is now pinned to a re-runnable
  derivation**: `t1e_gasphase_count.py` → `T1E_GASPHASE_COUNT.json`, which records the pattern,
  the field it was applied to, the manifest sha256 it was computed over, and all 62 matched
  table_ids. It was previously an unpinned number derived at a shell and recorded nowhere —
  the same failure shape as the spin lane's unverified literature claim, and freeze-blocking for
  the same reason. These 62 are **not** a pre-approved set and receive no special standing; the
  count exists so a large post-T2 shortfall is visible rather than silent, and per [S4b] it is
  explicitly **not a target** — a T2 that ends far below it has not thereby failed.

## 7. Carried in from T1

- Kun advisory A1: `recall_misses_are_instrument_failure` is type-unstable (string under
  degradation, list otherwise). T2 must branch on type or restructure it here.
- Kun advisory S8: "case-complete" overstates the three-case name variants; mixed-case forms
  (`LogOH`, `ZPhot`) are unreachable by that channel. Recorded as a known instrument limit —
  **not** repaired here, since the frozen channel maps were calibrated on the same basis.
- 24 clipped descriptions are itemized in `descriptions_clipped`; T2 must consult that list
  before quoting any description as evidence. **[S3b] This contract's own quotes meet that
  standard**: all **fifteen** control tables (D1–D12, P1–P3) were checked against
  `descriptions_clipped` and **none of them appears in it at all** — the **24** clipped
  descriptions span 13
  other tables. The §3/§4 evidence cells are otherwise manifest-derived and their faithfulness
  is the evidence pass's object, not this one's.
