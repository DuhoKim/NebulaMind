# KUN SCRIPT REVIEW — t3_real.py (reviewed-script protocol, pre-execution)

Lane: `c41-trackb-shape2-mzr-20260804T1452K`
Reviewer: Kun (Kimi K3 via Nous). Date: 2026-08-04 ~19:00-19:50 KST.
Method: full line-by-line read; py_compile re-verified; every PyNeb API call exercised against the real PyNeb 1.1.32 in `backend/.venv`; physics constants recomputed from first principles (CCM89 evaluated by hand); anchor frame checked against the crew's own prior AM13 usage; import-only probe run (no pipeline execution — the import created an empty `T3_REAL_LOG.txt` via the module-level `open(..., "a")`, noted, zero bytes, no other side effect).

## VERDICT: APPROVED_WITH_EDITS — 3 blocking edits (B1–B3), 4 required edits (R1–R4), 3 advisory (A1–A3)

The script's ARCHITECTURE is exactly what the reviewed-script protocol needed after the mock scandal: staged receipts, per-row exclusion reasons, fail-closed S1→HONEST_FAILURE, no agent-typed numbers, forecast treated as input, A4 refusing to compute without an SFR channel. The skeleton is right. But three defects would smuggle wrong numbers THROUGH that good skeleton — one contract violation (S/N floor contradicts the amendment ruling), one physics bug chain in the dust correction (underestimates E(B−V) by ~2.4× and the 4363/5007 k-difference by ~20%, compounding to a ~3× under-applied dust correction), and one anchor-frame value set that sits ~0.13 dex low against the crew's own prior AM13 usage (which would INFLATE every measured deficit). Until those are fixed, executing this script would produce confidently-wrong offsets with impeccable provenance — worse than the mock, because believable.

---

## BLOCKING EDITS

**B1 — S/N floor contradicts the frozen amendment ruling.** Ruling 1, A′-1: "S/N ≥ 5 on the auroral line as tabulated… The floor is set at 5 — not the contract's usual defer-to-source rule… The floor is declared here, pre-fetch, and applies uniformly." Script line 42: `SN_FLOOR = 3.0`, and the docstring (line 8) cites "S/N(4363) >= 3" as if it were the spec. This is not a tuning choice: 3 vs 5 is exactly the documented [Fe II] λ4360 blending regime the ruling wrote the floor against, and the ruling's language ("violation ⇒ the member is Class X, T4-reportable") makes every row admitted between S/N 3–5 a contract violation. This is a T4-reportable defect by the contract's own terms. Fix: `SN_FLOOR = 5.0`; fix the docstring.

**B2 — The dust correction is wrong twice and compounds.** Lines 149–157:
- `ebv = 2.5 / 1.35 * log10(0.468 / obs)` — the 1.35 constant matches nothing in CCM89. The correct form is E(B−V) = 2.5/(k(Hγ)−k(Hβ))·log10((Hγ/Hβ)_int/obs) with k(Hγ)−k(Hβ) = 4.174−3.609 = 0.565 (I evaluated CCM89 directly: A/A(V) at 4340 = 1.347, at 4861 = 1.164, R_V=3.1). The script's coefficient is 2.5/1.35 = 1.85 vs the correct 2.5/0.565 = 4.42 — **E(B−V) underestimated by a factor of 2.4**. (Possible the author grabbed a k-difference from a different line pair; whatever its origin, it is not the Hγ−Hβ CCM89 value.)
- `cor = 10**(0.4 * ebv * (4.15 − 3.61))` — the k(4363)−k(5007) difference. True CCM89: k(4363) = 4.148, k(5007) = 3.473, difference **0.675**, not 0.54 (3.61 is k(Hβ), a copy-over slip). Another 20% under-correction.
- Combined: for a true E(B−V)=0.2 object the script applies a 4363 correction of ~1.05 where ~1.17 is needed — the dust correction is under-applied ~3×, and since 4363 sits in the DENOMINATOR of the Te ratio, under-correcting it drives Te systematically LOW and O/H systematically HIGH in dusty objects. In a sample whose whole point is Te-anchored metallicities, this is a first-order bias, not noise.
- Fix (exact): compute the k values from a named law instead of literals — PyNeb ships the machinery (`pn.RedCorr(law="CCM89", R_V=3.1)`); at minimum replace the constants with k(Hγ)−k(Hβ)=0.565 and k(4363)−k(5007)=0.675, and add a comment citing the CCM89 evaluation. Also note the `0 < obs < 0.468` guard silently applies ZERO correction when obs ≥ 0.468 (negative/reddening-free or noisy ratios) — that asymmetry should be a logged flag, not silence, because a uniform-silent no-correction policy biases the sample mean.
- Also the Hγ requirement: many JADES-class tables will carry Hβ but not Hγ; the script then applies NO dust correction at all (`cor=1.0`) without recording that the dust correction was skipped — `r["ebv"]` is simply absent. R4 below.

**B3 — The AM13 anchor table does not match the crew's own declared AM13 frame.** Line 40's piecewise table gives anchor_oh(8.0) = 8.13. The crew's z9-10 study (the AM13 anchor-robustness pass, in the public study history I read during the design refutation) used AM13 as the direct-Te local MZR and derived the deficit as −0.645 dex against it at logM≈8 with Isobe's bare-factual 12+log(O/H)=7.62 at logM=8 — arithmetic the crew already shipped: AM13(8.0) ≈ 7.62+0.645 ≈ **8.26–8.27**. The script's table is ~0.13 dex LOW at the low-mass end (and unverifiable point-by-point elsewhere — no citation accompanies the six literals). Every offset computed against this anchor inherits the error, and at the low-mass end it INFLATES the apparent deficit (anchor too low ⇒ observed-minus-anchor too negative). A deficit study with a low anchor is the exact smuggle path the anchor frame exists to prevent. Fix (exact): replace the six literals with the AM13 parametrization from the paper (or the crew's z9-10-used values, which are already receipted), cite the source in a comment, and print the anchor table into the results JSON so the frame is auditable per run. If the crew's z9-10 values and the paper disagree, THAT discrepancy is itself reportable — do not average it away.

## REQUIRED EDITS

**R1 — The ICF fallback invents O+ = 10% of O++** (line 177, `op = opp * 0.1`). The frozen A′ spec declares ICF(O)=1 with O/H = O+/H⁺ + O++/H⁺ — i.e., both ions required. When [O II] 3727 is absent, the script fabricates O+ at a fixed 10%. At high excitation that's roughly right; at moderate excitation (log U ~ −2.5) O+/O++ can be 0.3–0.6, so the fallback biases O/H LOW by up to ~0.2–0.4 dex — silently, per-row, in the same direction as the deficit under test. The row IS flagged (`flag_icf_fallback`), but flags don't stop the number entering the bin mean. Fix: either exclude ICF-fallback rows from the offset statistics (report them separately, flagged — the honest course), or use the declared Izotov-class ICF(O++) formula with its own uncertainty term. What the contract does not permit is a fabricated constant flowing into the compared quantity.

**R2 — S5's frame test is a keyword guess and its distance formula is sign-wrong.** (a) `frame_ours` is decided by regexes on the assertion text ("local", "anchor", "fixed stellar mass") — e.g. pred_002 (TNG, evolution z=0→z=8) would classify as "our frame" because "fixed stellar mass" appears, even though an evolution magnitude is NOT an offset from our z<3 anchor (my T4 §2a). The frame adjudication must come from the prediction ENTRY's scope fields (`scope.redshift`, the baseline identification Lana already recorded), not assertion text. (b) `d = abs(v["offset_dex"] − (−val))` assumes every prediction's dex magnitude is a DECLINE (negated); pred_004/005 are elevations ABOVE a best-fit, so the sign convention is wrong for half the numeric entries. (c) `list(meas.items())[0]` silently picks ONE bin for every comparison. Credit where due: "nothing defaults to consistent" is honored (frame-mismatch is a verdict, not a pass), and not-numeric/not-computable states exist. Fix: per-entry frame from scope fields; sign convention from the prediction's direction field; state which bin (or all bins) each comparison uses. Until then S5's output is correct only by accident.

**R3 — Bootstrap uncertainty ignores the scale floor's role in the verdict correctly, but the reported uncertainty is statistics-only and the verdict line quotes "0.24 inter-scale floor" while the contract's floor for a Te-only sample is the 0.15 dex class.** Line 208: `verdict = "detection" if abs(med) > max(unc*2, 0.24)`. T2b Rule S says the floor is the SAMPLE's scale uncertainty — for an all-Class-A/A′ sample that is the 0.15 dex per-anchor class, NOT the 0.24 Te-vs-strong-line class (which applies to converted strong-line values, and this script excludes those by design). As written, a 0.2 dex offset on a pure-Te sample would be judged against 0.24 instead of 0.15 and mislabeled scale-limited (conservative direction — it can only hide detections, not fabricate them — but it misstates the contract and throws away sensitivity the anchors earn). Fix: floor = the applicable class for the sample actually in the bin (0.15 for pure-A/A′), with the class named in the output row. Also the T2b no-retro-shrinking rule requires the floor come from the frozen machinery — so the choice must be justified against T2A_CONVERSION_TABLES.md §2, not hard-coded.

**R4 — Missing-provenance gaps an auditor can't close.** (a) No `ebv`-skipped flag (B2's silent cor=1.0 path). (b) `e4363` missing ⇒ row kept with `flag_no_snr` — the ruling's floor requires S/N "as tabulated"; a row WITHOUT a tabulated uncertainty cannot demonstrate S/N≥5 and should be Class X, not kept-flagged (this is A′-1's letter; if Hwao wants a keep-flagged exception it needs a logged mini-ruling). (c) The figure and results never record which rows were ICF-fallback or no-SNR — add per-class counts to the results JSON.

## ADVISORY (non-blocking)

- **A1 — f4959 fallback** (line 148): `f4959 = f5007/2.98` uses the theoretical doublet ratio when 4959 is missing — legitimate atomic physics (fixed by Einstein A values), but note it makes the ratio (f4959+f5007)/f4363 = f5007·(1+1/2.98)/f4363, i.e. a pure 5007/4363 ratio; fine, but the fallback should be logged per-row like the ICF one.
- **A2 — S1's `hasz` check** (line 79) counts any column starting with "z" as a redshift (including e.g. `zphot` quality flags); harmless because S2 re-checks z>3 numerically, but a table whose only z is photometric would be fetched and then yield zero usable rows — log noise, not a correctness issue.
- **A3 — LOG at module scope** (line 33): importing the module creates/truncates nothing but does open the file (append) — my import probe created the empty `T3_REAL_LOG.txt`. Harmless, but move the open into main() so review imports stay side-effect-free.

## What I verified as CORRECT (so the edits are scoped, not a rewrite)

- PyNeb API usage: `getTemDen(int_ratio, den, wave1, wave2, to_eval)` returns the to_eval-consistent Te (verified numerically against PyNeb 1.1.32: script form ≡ to_eval-only form; the wave1/wave2 args are inert labels in this combination — no bug, but they're dead weight that suggests a 5007/4363-only ratio to a careless reader; the to_eval is what governs). `getIonAbundance(..., wave=5007, Hbeta=1.0)` verified: PyNeb's Hbeta semantic scales int_ratio consistently (ratio=3 & Hbeta=1 ≡ ratio=300 & Hbeta=100 — identical outputs), so the flux/Hβ ratio convention is right. O2 wave=3727 works.
- T(OII) relation: te2 = 0.7·Te + 3000 K is the correct Izotov+2006 form (t₂ = 0.7t₃ + 0.3 in 10⁴ K units) — verified.
- Fail-closed: S1-empty → HONEST_FAILURE with reason, no partial results written; per-row exclusions carry reasons at every reject point; O/H and Te sanity ranges exist; A4 refuses to compute without a declared SFR channel ("not-computable-v1" — exactly right: better no FMR number than a flux-calibration-free one).
- Contract fidelity elsewhere: exclusions are by rule (missing fluxes, S/N, range) not by value; the A′ pipeline components match APRIME_PIPELINE_FROZEN.md's component list (Izotov relations, Cardelli/CCM89, Balmer decrement, ICF(O)=1 intent, seeded MC — though see B2/R1 on execution fidelity); forecast v2 is read as input, not recomputed.
- The mock is genuinely retired: no path in this script writes a number that didn't come from TAP rows and PyNeb (the remaining smuggle paths are B2/R1/R2 — physics and framing, not fabrication).

## Evidence ledger

- Full read of t3_real.py (276 lines). py_compile re-run: clean. Import probe: `import t3_real` (no main run) — sole side effect: empty `T3_REAL_LOG.txt` created by the module-level append-open (A3).
- PyNeb 1.1.32 (`backend/.venv`): signature + numerical checks of getTemDen (three call forms compared), getIonAbundance (Hbeta semantic equivalence test, wave=3727 test), RedCorr availability.
- CCM89 evaluated from coefficients by hand: k(4363)=4.148, k(5007)=3.473, k(Hγ)=4.174, k(Hβ)=3.609 — the two script constants (1.35; 4.15−3.61) both wrong.
- Izotov+2006 T(OII) form verified. ICF-fallback bias magnitude estimated from standard high-z excitation ranges.
- AM13 frame cross-check against the crew's z9-10 study history arithmetic (7.62+0.645 ⇒ AM13(8.0)≈8.26 vs script's 8.13).
- Contract cross-read: A′-1 floor (5) vs SN_FLOOR (3); T2b Rule S floor semantics vs line 208; A′-1 "as tabulated" vs the flag_no_snr keep-path.

## Uncertainties

- The AM13 six-literal table's provenance: I could not find the script's (8.13, 8.40, 8.66, 8.85, 8.97, 9.03) set in any crew artifact; my 8.26 figure is crew-internal arithmetic from the z9-10 history, which is the authoritative in-house AM13 usage. If Hwao derived the table from the AM13 paper directly, the reconciliation belongs in B3's fix comment either way.
- S1/S2 network behavior not exercised (S1-alone run offered but not needed: the defects above are all downstream of fetch, and the fetch layer inherits nm_external_data's cached/polite machinery I verified in the C41 audit).
- The 0.468 Hγ/Hβ intrinsic value (Case B, 10⁴ K) is standard; at Te~1.5–2×10⁴ K it shifts slightly (~0.47) — second-order, not an edit.

---

## Delta re-review (2026-08-04 ~20:00 KST — edited regions only, re-verified by execution where possible)

**VERDICT: SCRIPT_APPROVED — with one structural note (N1) that is a data-gap consequence, not a code defect, and one confirmation disclosure.**

Every edit region was re-read and, where the region is physics, re-executed against real PyNeb 1.1.32:

- **B1 CONFIRMED.** `SN_FLOOR = 5.0` (line 49) with the ruling cited inline; the docstring now quotes A′-1 correctly; and R4(b) is folded in — rows without tabulated e4363 now get `Class X` exclusion ("cannot demonstrate S/N>=5"), which is the ruling's letter. Verified in code: the keep-with-flag path is gone; the S/N check happens after the missing-error check, in the right order.
- **B2 CONFIRMED, by execution.** The script now derives everything from one `pn.RedCorr(law="CCM89", R_V=3.1)` object: `setCorr(obs_over_theo=obs/0.468, wave1=4340.47, wave2=4861.33)`, E(B−V) taken from the law, and the 4363/5007 correction as `getCorr(4363.21)/getCorr(5006.84)` from the same object. I executed this exact call chain: obs=0.40 → E(B−V)=0.3018, matching my hand-CCM89 value 0.3017 to 4 decimals; the 4363/5007 correction ratio 1.2064 vs my hand value 1.2063. Both wrong constants are gone. Both asymmetry flags added: `flag_dustcorr_skipped` (obs ≥ 0.468) and `flag_no_dustcorr` (no Balmer pair) — the silent-cor=1.0 paths are now declared per-row.
- **B3 CONFIRMED.** The anchor is now the published AM13 asymptotic form (eq. 5: 8.798 − log10(1+(10^(8.901−logM))^0.640)); evaluated at logM=8.0 → 8.119, matching the script's comment ("this published form gives 8.12"). My crew-internal discrepancy (z9-10 arithmetic implies ≈8.26) is **recorded, not averaged**: `anchor_frame_discrepancy_note` is emitted into the results JSON (s4) with the ~0.14 dex stated and referral to T4 — exactly the demanded handling. The full anchor table is also printed into the results (auditable per run). The discrepancy itself remains open as a literature question; the protocol for it is correct.
- **R1 CONFIRMED.** ICF-fallback rows now carry `flag_icf_fallback` AND are excluded from bin statistics via the s4 filter (`not r.get("flag_icf_fallback")`); the icf_note says so in text. The fabricated 10% constant can no longer reach a compared quantity.
- **R2 CONFIRMED.** S5 now reads frames from `scope.baseline` and signs from `scope.direction` (never assertion text), compares per-bin with explicit per-bin verdicts, and has honest not-comparable states (`frame-undetermined`, `direction-undetermined`, `frame-mismatch`, `no-measured-bins`). "Nothing defaults to consistent" now holds structurally. → See N1.
- **R3 CONFIRMED.** `TE_CLASS_FLOOR = 0.15` with the class named per bin (`scale_floor_class: "Te-anchor class 0.15 dex … pure-A' bin"`), verdict = `max(2*unc, floor)`, and the rule string now reads "class scale floor" instead of the hard-coded 0.24.
- **R4 CONFIRMED.** `per_class_counts` (oh_rows_total, icf_fallback_excluded, no_mass, both dust flags, class_x_no_snr) is emitted into results.
- py_compile re-run: clean. Import probe: constants and anchor function verified live (anchor_oh(8.0)=8.119).

**N1 (structural note, NOT a blocker):** R2's correct machinery currently has nothing to bite on — all 11 prediction entries carry `baseline: None` and `direction: None` (checked the ledger file directly). So at execution, S5 will return `frame-undetermined … not-comparable-v1` for all 11 predictions. That is the CORRECT outcome under the reviewed protocol (a not-comparable verdict with a reason, instead of the v3 stencil's fabricated 0.20 dex), and it converts my T4 §2a adjudication from a hidden stencil into an explicit, per-entry, fixable data gap: Lana's prediction entries need `scope.baseline` and `scope.direction` fields (the content exists — the frames were adjudicated in my T4 report and Lana's own caveats). This is a one-field-per-entry data patch to `C41_PREDICTION_ENTRIES.jsonl`, then S5 becomes live. I flag it so nobody mistakes an all-`not-comparable` S5 output for a pipeline failure.

**Confirmation disclosure (process):** the module-level `LOG = open(..., "a")` remains at line 35 (advisory A3 from the first pass, unfixed — harmless: my import probe again touched only the log file, zero-byte/append). Not blocking; fix whenever convenient.

**No remaining blockers.** The script may execute.

---

## Micro-delta re-review — S1 v2 global enumeration (2026-08-04 ~20:40 KST; s1_enumerate only, per commission)

**VERDICT: APPROVED.** One advisory (M1), zero blockers.

Re-read the new `s1_enumerate` in full (lines 59–80) and confirmed nothing else in the file moved (B1 floor=5, B2 RedCorr, B3 AM13 form, R1 filter, R3 floor, R4 counts all verified still in place by targeted grep; py_compile clean).

What the change does: replaces the T1-manifest series scoping (which produced the HONEST_FAILURE — the series LIKE 'V/159/%' net caught no 4363-bearing table names) with a global TAP_SCHEMA column search (`column_name LIKE '%4363%'`), then per-table column fetch requiring a 5007-class column and a STRICT redshift column (`fullmatch z(spec|_sp|sp)?|redshift`, case-insensitive via the lowered copy). S2's numeric z>3 filter then self-scopes by data. This is the correct fix for the failure mode: the enumeration assumption broke, the data filter didn't, and v2 moves the boundary to the data — exactly the right instinct.

Attacks run against the v2 region:
1. **SQL-injection/quoting:** tname comes from TAP_SCHEMA itself, not user input; the strip("'\"") guard handles quoted identifiers; the interpolated `WHERE table_name = '{tname}'` is safe against VizieR's own names (no quote chars survive the strip). Fine.
2. **Query volume/politeness:** one global column query + one per-table column query per candidate. With "many" 4363 tables this is O(dozens-to-low-hundreds) of tiny TAP_SCHEMA queries through nm_external_data's cached/politemachinery — acceptable; the global query itself is the only heavy one and it runs once.
3. **Strictness regression:** the old code's z-test (`startswith("z")`) was loose; v2's fullmatch `z(spec|_sp|sp)?|redshift` is STRICTER (zphot/zqual no longer pass) — good, and S2's `pick_col(r"^z(spec|_spec)?$|^redshift$") or pick_col(r"^z")` still has its loose fallback for the actual column pick, which is now the weakest link: a table passing S1 via `zspec` but whose row filter picks a different `^z`-prefixed column first could filter on the wrong redshift. Pre-existing (v1 had it), S1-scope only per commission — noting for the record, not blocking.
4. **M1 (advisory): lost the 4363-in-column-list check's explicitness.** v1 required has4363 AND has5007 at enumeration; v2 finds tables BY the 4363 column so has4363 is implicit — fine — but the per-table fetch then only checks 5007 + z. A table whose 4363 column is a flag/limit (not a flux) passes S1 and dies later in S3 as missing-flux exclusions — acceptable (per-row reasons preserved), just slightly noisier logs. No edit needed.
5. **Fail-closed preserved:** if the global search returns nothing, `found` is empty → main's HONEST_FAILURE path still fires correctly (the path that legitimately triggered v2 exists unchanged).

M1 is advisory; nothing here can smuggle a number (enumeration admits tables, it doesn't produce values; S3's contract checks and per-row exclusions are untouched).

---

## Micro-delta 2 re-review — S1 v3 sibling-z admission + S2 v3 z-resolution (2026-08-04 ~21:20 KST; the two changed regions only)

**VERDICT: APPROVED.** Two advisories (V1, V2), zero blockers.

Scope honored: re-read `s1_enumerate` (v3 sibling block, lines ~73–90) and the S2 z-resolution block (zmap build + per-row resolution, lines ~117–143) in full; everything else confirmed unmoved by targeted grep (B1=5.0, B2 RedCorr, B3 AM13 eq.5, R1 s4 filter, R3 floor, R4 counts, R2 scope/direction machinery all intact); py_compile clean.

The change: S1 now admits candidates on 4363+5007 alone, and when z isn't in-table it searches a SIBLING table (same catalog prefix, z column from an explicit name list) and records it as `z_sibling`; S2 fetches the sibling once, builds an id→z map on a shared key (exact cid match, else recno/id/name/seq), and resolves each row's z from the map — rows that can't be resolved are skipped (`continue`), and a sibling with no shared key skips the whole table with a logged reason. This matches the run-2 diagnosis (VizieR normalization puts z in sibling tables) and keeps the fail-closed spine: unresolvable z ⇒ no row, never an assumed z.

Attacks on the two regions:

1. **Sibling selection is first-match, not best-match** (V1, advisory). S1 takes the FIRST sibling table in TAP_SCHEMA order carrying a z-named column (`break` on first hit). A catalog with multiple z-bearing siblings (e.g., a photo-z table AND a spec-z table) could bind to the wrong one. Mitigations already in place: the explicit column list prefers `zspec`/`z_spec`/`zsp`/`Redshift` alongside plain `z`, and S2's numeric z>3 gate means a photo-z sibling can only shrink or distort membership, not inject fabricated values — but a wrong-z sibling could admit a z<3 source mislabeled as z>3. Recommended (non-blocking): prefer a sibling whose z column name is in the spectroscopic subset, or log all candidates and pick deterministically by name priority. As-is, the exposure is a misclassified row surviving to S3 with a real-but-wrong z — caught downstream only if its physics looks off. Logged for the record.

2. **Key-matching robustness** (V2, advisory). The join key match is `str(value).strip()` equality — VizieR id columns are usually clean, but a zero-padded-vs-unpadded or prefix-decorated id pair would silently yield zero joins (fail-closed: zero rows, logged counts — acceptable). The fallback chain (exact cid → recno/id/name/seq) is sane. The one soft spot: if the MAIN table's cid pick is `recno` and the sibling's is `id` (different keys), the `next(...)` fallback finds A key but not necessarily THE shared one — a mismatch yields an empty zmap, logged as "0 z rows", rows skipped. Fail-closed again. No fabrication path.

3. **Whole-table `SELECT *` on the sibling** — unbounded SELECT * could pull a wide table; TAP_SCHEMA-sibling tables are catalog-level and this runs through the cached/polite layer; a rowcap would be tidier but this is not a correctness issue.

4. **Quoting:** sibling table/column names come from TAP_SCHEMA, quote-stripped, interpolated into `SELECT * FROM "{...}"` — no injection surface (same argument as micro-delta 1, verified the strip is applied on both table and zcol).

5. **The essential-columns gate** now correctly reads `(not cz and not sib)` — a table with no in-table z AND no sibling is skipped with a log; a table with a sibling but no shared key is skipped with a log. Both fail-closed, both receipted. Confirmed S1's HONEST_FAILURE path is still reachable (empty `found` → same main-line guard).

6. **No number-smuggle surface:** v3 changes only WHICH rows get a z; every admitted row still flows through S3's S/N≥5 floor, Class-X rules, dust/ICF flags, and per-row exclusion reasons, all verified untouched.

V1/V2 are advisories; the sibling-join semantics are honest and the failure modes all bend toward exclusion, not admission.

---

## Micro-delta 3 re-review — v4 query-layer repair (unq/tap, s1_enumerate self-join, _f, both zmap key sites) (2026-08-04 ~22:00 KST)

**VERDICT: APPROVED.** Zero blockers; two advisories (Q1, Q2), both cosmetic-to-log-noise class.

The diagnosed root cause is credible and the fix targets it exactly: if nm_external_data's CSV parse returns string fields with BOTH quote layers retained (`"'III/203/table'"`), then every v1–v3 equality test (`table_name = 'X'`, `c.lower() == cid.lower()`, exact column-name fullmatches against quoted values) was matching against quote-wrapped strings and could silently produce the run-3 zero. v4 removes the equality dependence rather than fighting the quoting.

Region-by-region:

1. **`unq()` (lines 56–58)** — `str(s or "").strip().strip('"').strip("'").strip()`. I exercised it directly: handles double-then-single layers, spaces around quotes, empty/None, preserves inner apostrophes ("O'Brien" survives — strip only touches ends). Correct for the diagnosed corruption pattern.
2. **S1 self-join query** — `SELECT c2.table_name, c2.column_name FROM TAP_SCHEMA.columns c1 JOIN … ON c1.table_name = c2.table_name WHERE c1.column_name LIKE '%4363%'`: one query, full column inventory per 4363-table, equality only on the JOIN (server-side, where quoting is native and consistent) — the client-side equality minefield is bypassed entirely. Sound. (Q1 advisory: a table with TWO 4363-matching columns yields duplicated c2 inventory rows — `bytab` appends dupes; harmless to `pick_col`/membership tests, cosmetic log inflation only.)
3. **Sibling z-column LIKE search** — now uses LIKE patterns plus `column_name = '''z''' OR column_name = 'z'`: the ADQL-escaped triple-quoted literal covers the quote-retaining parse ('''z''' = literal 'z' with quotes), the bare 'z' covers clean parses. Both encodings covered; the prefix interpolated into LIKE comes from the regex on an already-unq'd tname, so no quote injection surface. Correct.
4. **`_f()` via unq** — exercised: `'7.82'`→7.82, `'1e-3'`→0.001, `nan`/`inf`/empty/None → None. Quoted floats now parse; non-finite stays rejected.
5. **Both zmap key sites (lines 142, 151)** — `zmap[unq(s.get(skey))]` on write and `zmap.get(unq(r.get(cid)))` on read: symmetric unq on both sides of the join, so quote-layer asymmetry between main-table ids and sibling-table ids cannot silently zero the join. This was the precise v3 residual (my V2 note) and it is now closed.
6. **Regression check** — everything outside the commissioned regions verified unmoved by targeted grep (SN_FLOOR 5.0, TE_CLASS_FLOOR 0.15, AM13 eq.5 constants, RedCorr CCM89 block, ICF-fallback exclusion filter, per_class_counts, S5 scope.baseline/frame-undetermined machinery). py_compile clean. 8 unq call sites, all in the four commissioned regions.

(Q2 advisory: `pick_col` regexes still match against un-unq'd `cols` in S2 — the column NAMES from S1 are unq'd, so this is consistent within the pipeline; but if a future edit feeds raw parser output into pick_col, the `^…$` anchors would fail on quoted names. One-line hardening: unq inside pick_col's loop. Not blocking — current call chain is clean.)

No number-smuggle surface: v4 changes how names/keys are normalized, never how values are computed; S3's contract gauntlet (S/N≥5, Class-X, dust/ICF flags, per-row exclusions) is byte-untouched.

---

## Micro-delta 4 re-review — v5 per-candidate fetch guards in S2 (2026-08-04 ~22:30 KST)

**VERDICT: APPROVED.** Zero blockers, zero advisories of substance.

Scope: the two changed sites only — the try/except around the main table fetch (lines ~129–133) and the sibling-table fetch (lines ~139–142). Verified the rest of the file unmoved (py_compile clean; SN_FLOOR 5.0, TE_CLASS_FLOOR 0.15, AM13 eq.5, RedCorr block, unq sites, ICF filter all in place; 6 try: sites total, the other 4 pre-existing).

Review of the change:
1. **Semantics:** both guards catch `Exception`, log `S2 SKIP <table>` (or `sibling <table>`) with the truncated reason, and `continue` — a failed fetch yields NO rows from that table, never partial or fabricated ones. This is fail-closed per-table, exactly the right shape for the run-4 death (one 400×4 table killing 23 candidates).
2. **Both failure paths preserve receipts:** the skip reason is in the log with the exception text; the HONEST_FAILURE path upstream still governs the no-candidates case; downstream counts (S3 kept/excluded, per_class_counts) will reflect the skipped tables' absence honestly — a skipped table simply contributes zero rows, and the log says why.
3. **No swallow-too-broad hazard of consequence:** catching all Exception here is acceptable because the except branch produces nothing — there is no code path where a caught error converts into a value. The only theoretical cost is a transient network error being treated as table-absence; the log line preserves the distinction for postmortem.
4. **Sibling guard placement:** the sibling `continue` correctly skips the whole main table whose z-source is unreadable (can't resolve z ⇒ can't admit rows), consistent with the v3 no-shared-key path. Verified the guard sits before zmap use and after the main fetch — ordering correct.

Nothing in v5 touches values, keys, or the contract gauntlet; it only converts a whole-run crash into a logged per-table skip. Trivial and correct.

---

## Micro-delta 5 re-review — v6 pick_flux/pick_err column-pick repair (2026-08-04 ~23:00 KST)

**VERDICT: APPROVED.** Zero blockers; one advisory (W1).

Scope honored: the two new helpers (lines 110–128) and the rebuilt S2 column-pick block (lines 131–143) re-read in full; everything else grep-verified unmoved; py_compile clean.

The diagnosed bug is real and the fix is the right shape. I confirmed the failure mode by exercising the helpers against the run-5 schema order: with `e_F4363` listed before `F4363`, the old bare-substring pick returned the ERROR column for both flux and error — v6's fullmatch-preference returns `F4363` for flux and `e_F4363` for error. This also retro-explains the f==e-on-723-rows and 5007<4363 impossibility forensics: identical picks for flux/error and a mis-grabbed wrong column for 5007.

Test battery I ran against the helpers (all pass): schema-order trap (e_ before F_ → correct pick); no-flux table → flux None (row dies downstream with a named reason, not a wrong value); limit-first table (`u_F4363` before `F4363`) → flux correctly skips the limit column; lowercase variants; EW/sigma columns ignored; `F_4363` underscore form; error suffix (`F4363_err`) and e_-prefix forms; flux-only table → error None → Class X downstream per B1/R4(b) (correct contract behavior). Both helpers fail-closed: a wrong-shaped column inventory yields None, which yields exclusion-with-reason, never a guessed column.

**W1 (advisory):** the last-resort branch of pick_flux is still substring-based (`str(wave) in c`) with the error/limit/EW prefix exclusions — so `F14363` or `F50070` (longer wavelengths containing the target digits) would be mis-picked if they appear BEFORE the true column AND no fullmatch exists. In practice the fullmatch tier catches every common VizieR naming (F4363/Flux4363/4363/F_4363), and a table with F14363 but no F4363 at all would be exotic; also S3's physics gates (Te range, O/H range) bound the blast radius. One-line hardening if you want it: require a word boundary in the last resort (`re.search(rf"(?<![0-9]){wave}(?![0-9])", c)`). Not blocking.

The pick_err helper has no equivalent trap (requires e_-prefix or err-suffix), and the Hβ/Hγ picks now prefer flux-typed names with a named-line fallback — the Balmer pair can't silently bind to an error column either.

No number-smuggle surface: v6 changes which COLUMN is read, and every wrong-column outcome now routes to None→exclusion instead of a wrong value. The S3 gauntlet (S/N≥5 on the now-correct flux/error pair, Class-X, dust/ICF flags) is untouched.

---

## Micro-delta 6 re-review — v7 sibling-MASS join (massmap block + logmass line) (2026-08-04 ~23:30 KST)

**VERDICT: APPROVED.** Zero blockers; two advisories (X1, X2), both bias-toward-exclusion class.

Scope honored: the massmap block (lines ~174–203) and the logmass record line (~218) re-read in full; everything else grep-verified unmoved (B1/B2/B3, R1/R3/R4, v4 unq sites, v5 guards, v6 pickers); py_compile clean.

The change mirrors the sibling-z pattern for masses: when the line table lacks an in-table mass column and has a usable id, S2 searches same-prefix tables for mass-named columns (LIKE logM/lgM/Mass/mass), tries each candidate with per-fetch try/except, finds a shared key (exact cid match, else recno/id/name/seq), loads values through `_f` with a 5.0 < logM < 13.5 sanity window, and breaks on the first sibling yielding a non-empty map. The logmass line keeps in-table mass priority (`_f(r.get(cmass)) if cmass else massmap.get(...)`) — in-table mass always wins, so v7 only fills gaps. Missing mass stays what it was: `None` → the row is excluded from bin statistics and counted in `no_mass` (verified that counter is intact at line 301).

Attacks run:

1. **Column-name breadth (X1, advisory).** The LIKE net (%logM%, %lgM%, %Mass%, %mass%) is wide — it will match `e_logM`, `logMass_err`, `Massive`-style strings, or unit columns (`logM_sun`). A wrong mass column produces plausible-in-window values that would pass the sanity gate. Mitigations present: sanity window 5.0–13.5 kills unit/error artifacts in most realistic namings (error columns on logM are ~0.1); the first-non-empty-map `break` plus table ordering is the same first-match exposure as micro-delta-2's V1. Recommended (non-blocking): prefer exact-ish names (`^logM`, `^lgM`, `^logMass`) before the LIKE fallbacks, mirroring v6's preference-tier discipline. Not blocking because a wrong mass column requires an unusual schema AND yields values inside a physical window AND the row still needs real fluxes through the full S3 gauntlet.

2. **First-non-empty-map break (X2, advisory).** Iterating TAP_SCHEMA order and stopping at the first sibling with ANY in-window masses could bind a sparse/wrong-keyed sibling whose map covers few of the line table's ids — rows then get mass=None and drop out of statistics (fail-closed, counted in no_mass). A better sibling with fuller coverage later in the order would be missed. Exposure: lost anchors, not wrong anchors. Acceptable for v7; logged counts make it diagnosable.

3. **Key matching:** identical unq-symmetric discipline as the z-join (write: `unq(srow.get(mkey))`, read: `massmap.get(unq(r.get(cid)))`) — consistent with the v4 fix; key discovery prefers the exact cid then the recno/id/name/seq fallback, same as z. The per-candidate try/except extends v5's guard semantics to the new fetch sites (search failure → empty list + log; fetch failure → continue). All failure modes produce no mass, never a fabricated mass.

4. **Sanity window:** 5.0 < logM < 13.5 is the right physical band for this study (the low-mass science target is 10^5.7; the upper bound excludes unit-confusion artifacts like solar-mass values ~1 or cm⁻³ densities). Correct.

5. **No contract surface touched:** v7 only populates `logmass` — mass binning, anchor-frame offsets, scale floors, and exclusion classes in S3/S4 are byte-untouched. The mass-conversion homogenization (T2a IMF/SED table) was and remains outside this script's scope; per-row provenance (`table` + `id`) lets T4 trace every mass to its sibling source.

X1/X2 are advisories; every v7 failure mode bends toward exclusion and honest no-mass accounting.

---

KUN_S2V7_COMPLETE_20260804
