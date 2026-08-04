# LANA BRIEF — draft the anchor-gap paper (Duho: "okay draft the anchor-gap paper")

Lane: `c41-trackb-shape2-mzr-20260804T1452K`. You are Lana, author. Every number in the draft
comes from the lane's artifacts — nothing invented, nothing remembered.

## Sources (read-only)
- `T3_REAL_RESULTS.json` (post Kun-C1/C2: bins 2/1/0, below_bin_floor 2, per-class counts,
  forecast_vs_actual block with the §6 null statement, anchor-frame table + discrepancy note).
- `T3_REAL_SAMPLE.jsonl` — the 5 anchors (IDs, z, Te, O/H, masses, flags) AND the exclusion
  census (S/N floor kills incl. the 4.8 near-miss; no-Hβ; Te-nan; the 748→5 cascade).
- `T3_REAL_FIGURE.png` + `t3_real.py` (the reviewed script IS the method), `T3_REAL_LOG.txt`.
- Contract stack: `T2B_CONTRACT_SEMANTICS.md`, `T2B_AMENDMENT_RULING.md` (Class A′),
  `APRIME_PIPELINE_FROZEN.md`, forecasts v1/v2.
- `KUN_SCRIPT_REVIEW.md` (initial + 6 micro-deltas) + `KUN_T4_REAL_FORENSICS.md` (verdict
  SOUND_WITH_CORRECTIONS; all 5 anchors reproduced to the digit) — the verification chain is a
  reportable strength of the method.
- Motivation: the C41 debate map axis A3 (`../c41-baseline-restart-20260803T1253Z/
  C41_STATUS_DEBATE_MAP_V1.md`) — the calibration-validity dispute and its settle-line.
- Differentiation (the F2 pattern, mandatory): the crew's z9-10 unlensed study — what it
  established and how THIS census differs (survey-wide public-archive scope; contract-grade
  uniform floor; the FMR half untouched there and not-computable here — say both honestly).

## The paper
Short archival-methods census, AASTeX: title in the spirit of "The public-archive direct-Te
anchor gap at z>3: a contract-grade census". Abstract states the number (5), the forecast gap
(~25 expected conservatively; order of magnitude), and the consequence (no deficit verdict
possible at contract-grade public statistics; A3's resolution currently rests on data not
publicly quotable at uniform rigor). Methods: the frozen-contract + reviewed-script protocol
(enumeration → exclusion cascade → PyNeb A′ → joins), stated plainly. Results: the 5-anchor
table with full provenance; the exclusion taxonomy table; bins + below-floor accounting; the
near-miss. Discussion: what would close the gap (publish flux TABLES with errors + linked
masses; the specific S/N-4.8 class), scope limits (VizieR-only enumeration; team archives
excluded BY scope not oversight; the anchor-frame discrepancy note verbatim), and the A3
consequence. Uncertainties section mandatory. Modality law: this is a census and a null —
never let a sentence claim more.

## Deliverables (lane dir)
`ANCHOR_GAP_PAPER.tex` (compilable structure) · `make_paper_figure.py` + figure refresh if
needed · `PAPER_CHANGELOG.md` (source → section map) · `LANA_PAPER_REPORT.md` ending with
marker `LANA_ANCHORGAP_PAPER_COMPLETE_20260804`. Lane-only writes; no network.
