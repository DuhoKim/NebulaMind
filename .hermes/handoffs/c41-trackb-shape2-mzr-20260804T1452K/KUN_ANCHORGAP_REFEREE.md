# KUN REFEREE REPORT — journal-referee pass on ANCHOR_GAP_PAPER.tex

Lane: `c41-trackb-shape2-mzr-20260804T1452K`
Referee: Kun (Kimi K3 via Nous), fresh session; continuity via predecessor reports on disk.
Date: 2026-08-04 21:26 KST (stamped via `date`).
Manuscript: `ANCHOR_GAP_PAPER.tex` (34,207 B, 556 lines, AASTeX 6.3.1 twocolumn; never compiled
in-lane — disclosed in the .tex header and `LANA_PAPER_REPORT.md` note 2).
Ground truth: `T3_REAL_RESULTS.json` (sha f9b671aa…, re-verified live this session against
`T5_RECEIPTS.md`), `T3_REAL_SAMPLE.jsonl` (95 rows, sha cfecf77e… re-verified),
`T3_REAL_LOG.txt` (sha 45ffb83f… re-verified), the contract stack (`T2B_CONTRACT_SEMANTICS.md`,
`T2B_AMENDMENT_RULING.md`, `APRIME_PIPELINE_FROZEN.md`, `T2A_FORECAST_FROZEN.json`,
`T2A_FORECAST_FROZEN_V2.json` — all five shas re-verified against the T5 table),
`t3_real.py` (sha a3a75298… re-verified), predecessor reports (`KUN_SCRIPT_REVIEW.md`,
`KUN_T4_REAL_FORENSICS.md`, `KUN_DESIGN_REFUTATION.md`), plus `PAPER_CHANGELOG.md`,
`make_paper_figure.py`, and the cross-lane debate map
`../c41-baseline-restart-20260803T1253Z/C41_STATUS_DEBATE_MAP_V1.md`.
Method: independent recount of the full 95-row sample (every exclusion class recomputed from
raw fields, all 64 S/N-floor reasons re-derived from archived f4363/e4363 and the reason
strings checked against 1-dp renderings), key-for-key JSON comparisons, log census of runs
and fetches, verbatim-quote checks, and claim-by-claim trace of every number in the .tex.
All ten T5-receipted shas re-computed and confirmed this session.

## VERDICT: MINOR

Every number in the manuscript traces to a receipted lane artifact; the census modality is
never exceeded; the null is the receipted §6 instantiation with the supersession disclosed;
scope limits are prominent. Four minor errata/omissions (F-R1…F-R4 below) — none touches a
number, a verdict, the null, or a contract rule in substance; all are fixable in a few lines.
No MAJOR/REJECT trigger fired.

---

## 1. Mandate items, one by one

**1.1 Every number traces to the artifacts — PASS (independently recomputed, not trusted).**

- The five anchors (Table 1): z, S/N, E(B−V), Te, O/H, logM match `T3_REAL_SAMPLE.jsonl`
  row-for-row (ERO_04590 8.496/5.11/0.181/24847.1/7.109/7.60; ERO_05144 6.378/5.14/0.000/
  15456.7/7.922/8.55; ERO_10612 7.660/7.89/0.046/19391.9/7.685/7.78; GLASS_150029 4.584/6.65/
  nodata-flagged/16551.5/7.792/9.12; GLASS_160133 4.015/9.57/0.012/14307.4/8.032/8.11).
  Ranges in Abstract/§4.1/§7 (z 4.015–8.496; O/H 7.109–8.032; Te 14,307–24,847 K; logM
  7.60–9.12) are the exact min/max over those rows. GLASS_150029's `\nodata` + flagged
  zero-reddening note (obs Hγ/Hβ = 0.471 ≥ 0.468) matches the row's `flag_dustcorr_skipped`.
- Census backbone: 79 tables (log run-7 S1 line), 23 candidates (log "S1 done: 23
  candidates"), 12 unreachable (exactly 12 `S2 SKIP … HTTPError … after 4 tries` lines in run
  7), 11 tables in 8 catalogs fetched (enumerated from the run-7 fetch lines: A+A/666/A115,
  ApJ/844/171, ApJ/847/38, ApJS/256/44, ApJS/265/21, ApJS/267/16, ApJS/269/33, V/159×4
  tables), 95 z>3 rows (log "S2 done: 95"; sample recount: 95, all z>3, min z = 3.189),
  per-table split 10/9/32/6/38 (recount matches the paper's per-table numbers exactly;
  JADES = 85/95). Large low-z surveys (legacdr3 3166 rows; ApJS/265/21 920,077 rows)
  contributed zero z>3 rows — confirmed against the sample.
- Exclusion taxonomy (Table 2): my independent recount of the sample file gives exactly
  5 anchors / 64 S/N-floor (14 zero-flux, all JADES prism; 5 near-miss at S/N 4.7619–4.8431,
  i.e. printed band 4.76–4.84, all within 5% of the floor) / 12 no-Hβ (all twelve pass
  S/N ≥ 5 — the paper's "kills above the S/N floor" is exactly right) / 6 missing-flux /
  8 Te-failures. 5+64+12+6+8 = 95 closes. All 64 S/N reasons recompute from f4363/e4363 to
  the printed digit with zero mismatches; no anchor sits below the floor; all 12 no-Hβ rows
  genuinely lack fhb; all 6 missing-flux rows genuinely lack f4363 or f5007. The Te-failure
  physicality example (f4363 > f5007) is real: gngrat id 949, 4.373 > 3.214. Flag counts
  (20 no-Balmer-pair, 1 dust-skip, 0 Class-X-no-SNR, 0 ICF-fallback, 0 no-mass) match both
  the sample and `per_class_counts`.
- Bins and below-floor accounting: 2/1/0 in bins, ERO_04590 (7.60) and ERO_10612 (7.78)
  below the frozen 8.0 edge, 3+2=5 closure — matches `bins`, `below_bin_floor: 2`,
  `below_bin_floor_note`, and T5 check 1.
- Forecasts: v1 10/12/3 = 25, 0.25 dex precision, 0.30 dex threshold, sha 61d48d22…
  (re-computed live: matches the paper's quoted sha and v2's `v1_sha256` pin); v2 35/42/10 =
  87, 0.12/0.15 dex, revision cause verbatim. The results-JSON forecast block is key-for-key
  identical to the frozen files.
- Review-chain numbers (§3.1): APPROVED_WITH_EDITS with B1–B3 (S/N floor 3-vs-5 contract
  contradiction; dust-constant chain under-applying the correction ~3×; anchor table ~0.13
  dex low at the low-mass end), R1–R4 (ICF-fallback exclusion, prediction-frame discipline,
  0.15 dex class floor, provenance counts), A1–A3, six micro-deltas in the exact order the
  paper lists (global enumeration; sibling-z; quote-layer; fetch guards; column-pick repair;
  sibling-mass join), seven runs (3 honest empty-enumeration failures, 1 incomplete, the
  748-row zero-O/H completion with the schema-order defect — log line "S2 done: 748" and
  micro-delta-5 review confirm — and 2 clean completions, the last adding only the mass
  join; run-6→7 delta verified in forensics §2). All confirmed against `KUN_SCRIPT_REVIEW.md`,
  `T3_REAL_LOG.txt`, and T5 check 4.
- z9–10 differentiation numbers (§5.2): −0.69±0.03 statistical, N=5 unlensed anchors at
  z≈9.3–9.9 extended to 10.6 with GN-z11, ±0.16 dex total systematic dominated by the 0.15
  dex Te-scale class, bootstrap 95% CI [−0.82,−0.55], "systematic-limited, NOT a detection" —
  all carried in `KUN_DESIGN_REFUTATION.md` F1/F2 and the design v2 block. The §1 ledger
  claims (A3 = largest axis, 22 entries; c41_043 vs c41_033/035/044/045/049; c41_012 ~25
  galaxies; 0.05–0.1 dex; 0.35±0.28 dex) all trace to the debate map, and the settle-line
  quotation ("Concrete, falsifiable, and the measurement exists — statistics are the gap.")
  is verbatim from `C41_STATUS_DEBATE_MAP_V1.md` line 224–227.
- Pipeline description (§3.3) matches the reviewed script and freeze doc: PyNeb
  (λ4959+λ5007)/λ4363 at n_e=100; Izotov-2006 T(O⁺)=0.7T_e+3000 K; ICF(O)=1 with measured
  O⁺ (all five anchors have f3727 — verified); CCM89 R_V=3.1 on Hγ/Hβ with Case B 0.468;
  MC spec (seed 42, 1000 draws) named with the §6.4 disclosure that v1 outputs tabulate
  central values only.

**1.2 Census modality never exceeded — PASS.** I scanned every "deficit"/"evolution"
occurrence: all are negations, rule statements, or quotations of the licensed null. No
sentence claims a metallicity deficit, evolution, or their absence. Fig. 1a's caption
explicitly de-licenses the visual offsets; §4.3 records the per-object offsets as
provenance-only; §5.3's "order of magnitude thinner" is an anchor-count statement, not a
metallicity claim.

**1.3 z9–10 differentiation and shared absence — PASS (with one nit, F-R2).** §5.2
differentiates scope (targeted vs survey-wide), states the non-overlap (no z≳9 candidate
survived the public joins — verified: the z≈9.43 objects die at no-Hβ, the higher-z rows at
missing flux), and the shared absence is honest: FMR untouched there, `not-computable-v1`
here, "the fixed-methodology FMR offset test at z>3 remains unexecuted by anyone, including
us." Matches `KUN_DESIGN_REFUTATION.md` F2 and the results JSON `A4_FMR` block.

**1.4 Exclusion taxonomy and below-bin-floor accounting — PASS (with one nit, F-R1).**
Taxonomy verified in 1.1; C1 accounting correctly represented with the closure stated.

**1.5 Null instantiates §6 with supersession disclosed — PASS.** The §4.3 quotation is
word-for-word `null_statement_T2b_s6` from the receipted results file. §2.3 discloses the
v1→v2 supersession, its cause (Ruling 3), both shas' lineage, and F-T4-1 (verified verbatim
in `KUN_T4_FORENSICS.md`: v2's 0.12 dex precision is arithmetically impossible under the
common-mode 0.15 dex class). Ruling-3 condition 4 (cite v2, disclose v1 supersession) is
satisfied at paper level — both forecasts named in the statement, full cause disclosed in
§2.3 — and Correction 2's own "(or v1)" license explicitly permitted the conservative-v1
framing the paper uses. §6's semantic requirements hold: frozen forecast quoted, realized
statistics labelled, no "we saw nothing", no zero-measurement phrasing. The paper is also
transparent that with zero populated bins no 0.30-dex exclusion bound is computable, and
none is quoted.

**1.6 Scope limits (VizieR-only) prominent — PASS.** Abstract names the "global VizieR TAP
enumeration"; §5.2 opens with "The enumeration is VizieR-only … excluded by scope, not
oversight"; §6 items 1–2 carry the conservative-direction argument (true public yield ≥ 5);
single-epoch (2026-08-04) and λ4363-only channel scope (λ1666/λ5755 not enumerated) are
both stated. AM13 anchor-frame discrepancy carried verbatim and unresolved (§5.2, §6.3).

## 2. Findings (required for acceptance; all minor)

**F-R1 (MINOR, Table 2).** The S/N-floor row's "Dominant source" reads "JADES
prism/grating", but no grating row sits in that class: the 64 decompose as 28 gnprism + 31
gsprism + 5 compilation (my recount; gngrat/gsgrat contribute zero S/N-floor rows — their
exclusions are all no-Hβ/missing-flux/Te-fail). Fix the label to e.g. "JADES prism +
compilation". The other rows' source labels check out ("JADES prism" for the 14 zero-flux —
8 gnprism + 6 gsprism; "mixed" for near-miss — 2 compilation + 2 gnprism + 1 gsprism;
grating/prism labels for no-Hβ and Te-fail — correct).

**F-R2 (MINOR, §5.2).** "the z≥9.7 candidates lack the nebular flux" — one of the four
missing-flux z>9 rows is gsprism id 230 at z = 9.686 (< 9.7). The substance (those
candidates die at missing flux) is correct; the threshold is mis-stated for one row. Use
"z≳9.69" or "z>9.6". Related observation (no fix required): "the z=9.43 pair" counts two
objects (ids 2115, 2427) but three rows die at no-Hβ above z=9, since 2115 appears in both
gsgrat and gsprism; one clarifying parenthetical ("two objects, three rows") would
forestall a recounting referee.

**F-R3 (MINOR, §4.2 attribution).** The text says "the forensic audit recomputed all 64
exclusions from the archived fluxes and confirmed every stated reason." The written audit
(`KUN_T4_REAL_FORENSICS.md` §2) says "S/N-floor exclusions (58 rows)" and its own histogram
does not close (58+12+6+8+5 = 89 ≠ 95) — a prose-count slip in my predecessor's report that
`PAPER_CHANGELOG.md` already disclosed and repaired by direct recount (64 is correct; I
independently recomputed all 64 this session, zero mismatches). The paper's number is right;
the in-text attribution should credit the direct recount (as Table 2's own comment correctly
does: "Counts recomputed directly from the archived per-row sample file"), not ascribe "all
64" to an audit document that says 58. One-clause fix; no number changes.

**F-R4 (MINOR, §6 disclosure gap).** `APRIME_PIPELINE_FROZEN.md` specifies the dust input as
"Balmer decrement used if Hα/Hβ available, otherwise source-published A_V"; the executed and
reviewed pipeline used the Hγ/Hβ decrement exclusively (B2's approved fix:
`RedCorr.setCorr(obs/0.468, wave1=4340.47, wave2=4861.33)`), which at z > 4 is the only
physically available Balmer pair — the freeze doc's primary branch was vacuous and its
fallback never fired. The paper disclosed the analogous PyNeb 1.1.18-vs-1.1.32 seam (§6.5)
but not this one. Same class — documentation seam, not a numeric defect (all five anchors
derived and reproduced under Hγ/Hβ consistently; A′-2(c)'s generic "Balmer-decrement
reddening input identified per sample" covers the executed choice). Add one sentence to §6.5.

## 3. Observations (no fix required)

- "roughly an order of magnitude" (25→5, factor 5) is the receipted null's verbatim wording
  and is quoted as such; §5.3's "order of magnitude thinner than catalog row counts"
  (95→5, factor 19) stands on its own. Correct handling of a frozen phrasing.
- Figure not visually inspected (image-analysis backend timed out twice this session);
  `make_paper_figure.py` verified by read: it reads only the two receipted artifacts,
  asserts the 5-anchor count and the frozen AM13 form string before drawing, and draws
  exactly what the caption claims (shaded logM<8 region, bin edges, dotted 3-anchor line,
  +2-below-floor note, v1/v2/actual bars from the JSON). `.tex` compilation remains
  unverified by design (lane no-network rule; disclosed).
- The PyNeb version seam (§6.5), missing per-object MC uncertainties (§6.4), and missing
  per-object μ metadata for the five ERO/GLASS anchors (§6.6) are all disclosed by the
  paper itself — the last one correctly invokes the crew's own z9–10 lens-contamination
  precedent as the standing repair requirement before any populated-bin use.

## 4. What this pass establishes

Every quantitative claim in the manuscript — the five anchors to the printed digit, the
90-row exclusion taxonomy, the census backbone (79/23/12/11-in-8/95), the forecasts, the
review chain, the ledger motivation, the z9–10 differentiation — traces to sha-pinned,
receipted artifacts, and the critical ones were re-derived independently this session from
the raw per-row file. The null is the licensed §6 form with the supersession disclosed; the
modality discipline holds everywhere; the scope limits are prominent and honest. Four minor
errata (one table label, one redshift threshold, one attribution clause, one disclosure
sentence) stand between this draft and clean acceptance. None is structural.

Verdict: **MINOR** — accept after the F-R1…F-R4 edits.

## Evidence ledger

- Recomputed from `T3_REAL_SAMPLE.jsonl` (sha cfecf77e…, re-verified): all exclusion-class
  counts; all 64 S/N reasons from raw f4363/e4363 (zero mismatches); near-miss band
  membership and bounds; zero-flux membership; no-Hβ S/N-pass check; missing-flux
  verification; z>9 dispositions; flag counts; bin assignment; per-table split.
- Re-verified shas (10/10 match `T5_RECEIPTS.md`): results, sample, log, script, both
  reviews, both forecasts, pipeline freeze, contract, ruling.
- Verbatim checks: null statement = `null_statement_T2b_s6`; AM13 discrepancy note =
  `anchor_frame_discrepancy_note`; settle-line quote = debate map ll. 224–227; lensing
  clause quote = contract §5 / ruling 2; F-T4-1 = `KUN_T4_FORENSICS.md` line 59.
- Log census: 7 STARTs, 3 HONEST_FAILUREs, run-5 "748", run-7 23-candidate list, 12 SKIPs,
  11 fetch successes, "180 masses" from tabled1, "S2 done: 95", "S3 done: 5".
- Cross-lane read: `C41_STATUS_DEBATE_MAP_V1.md` axis A3 (22 entries; c41_012/043/033/035/
  044/045/049; dispersion figures; settle-line).
- Writes: this report only.

## Uncertainties

- Figure render and LaTeX compilation unverified (backend timeout; lane no-network rule) —
  both disclosed by the paper team; neither affects any number.
- I did not re-run PyNeb this session; the to-the-digit reproduction stands on my
  predecessor's T4-real forensics, whose anchor table I confirmed matches the sample file
  exactly, and whose method (PyNeb 1.1.32, frozen A′ chain) is internally documented.
- The two unreachable-table retries (run 5 vs run 7 show ApJ/847/38 flipping from SKIP to
  fetched) confirm the paper's "unreachable at run time, not absent" framing; a future retry
  pass can only add anchors, as §5.1(4)/§6.1 state.

KUN_ANCHORGAP_REFEREE_COMPLETE_20260804
