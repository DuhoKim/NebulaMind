# RCA — RP-1 numeric drift across sprint cycles 5 → 6 → 7

Marker: `FABLE_BURN_P1_RCA_20260711T010503Z` (packet `HWAO_FABLE_BURN_P1_BRIEF_20260711T010503Z`)
Author: Fable burn lane A (P1), pane %184. Written 2026-07-11 ≈02:15Z.
Evidence basis: byte-identical snapshot under `sources-snapshot/` (SHA-256 table in `P1_RECEIPT.md`); all line numbers refer to the snapshot = cycle-package files as of 01:39:35Z.

## TL;DR

The recon finding is **confirmed and sharpened**. Cycles 6 and 7 both fail the integrity audit because the flagship's bootstrap 95% CI string `[-1.334,-1.283]` comes back as `[-1.334,-1.282]` at the same four locations. But the mechanism is **not** "numbers regenerated from memory": the prose phases demonstrably **re-derive numerals from the underlying custody artifacts and re-round them**. Every re-derived numeral is arithmetically correct against the raw data — including four brand-new statistics cycle 7 added, which I reproduced exactly from the custody CSV. The audit failures occur at precisely the two places where the *cycle-5 canon string itself* is not the nearest-rounding of the raw artifact value: the CI upper bound (`-1.283` vs raw `-1.2821399375` → nearest `-1.282`) and one supplement table cell (`2.830` vs raw `2.83066` → nearest `2.831`). Re-derivation "corrects" them; the audit's frozen invariant list rejects the correction; the cycle fails. The fix for the pipeline is the **verbatim-carry rule** (§5): candidate prose must copy numeric strings character-for-character from the base package and be checked against `INVARIANT_MANIFEST.json` *before* audit; any numeric change — even an arithmetically justified one — must be an explicit, separately-approved canon change, never an inline rewrite.

## 1. Evidence base and custody chain

| item | verification |
|---|---|
| Cycle 5 is the clean base | `CYCLE_05_tables_figures_AUDIT.json`: `integrity_blockers: []`, `numeric_invariants_missing: []`, `fatal_failures: 0` |
| Snapshot integrity | 8 brief-listed files copied 01:39:35Z (before the runner's ≈01:46:31Z slot); snapshot SHA-256 = original SHA-256 for all 8 |
| Cycle-5 tex ↔ custody | custody `active_candidate_hashes` SHA-256 match my snapshot: flagship `63b3920e…`, supplement `a4e3d66c…` |
| Raw flagship artifact | `runs/SDSS_AGN_SFR_PILOT_20260708T122000Z/analysis_results.json` SHA-256 `668ad7a6…` = custody inventory value |
| Raw sim-vector artifact | `runs/SDSS_REMAINING_TOPIC_PILOTS_20260708T125828Z/m3_p3_simulation_validation/analysis_results.json` SHA-256 `6f289f8c…` = custody value |
| Matched-pairs CSV | `matched_agn_sf_pairs.csv` SHA-256 `4ea53af8…` = custody value; 8,146 data rows |
| Audit failure strings | cycle 6 and cycle 7 audits both: `numeric_invariants_missing: ["[-1.334,-1.283]"]`, `integrity_blockers: ["numeric invariants missing"]` |

Cross-checking was done mechanically: all 105 entries of `INVARIANT_MANIFEST.json` (73 scalars + 32 table rows, built from cycle 5) were counted in the cycle-6 and cycle-7 files with the same matchers (`tools/build_manifest.py`).

## 2. Drift story (a): every numeric invariant, cycle 5 vs 6 vs 7

Of the 105 manifest entries, **102 carry unchanged into cycle 6 and 103 into cycle 7** (occurrence-for-occurrence). Every changed entry is listed below — there are exactly three numeric-change groups, plus benign layout/addition effects that alter counts without altering any carried value.

### 2.1 Group D1 — flagship CI upper bound (the audit blocker) — in BOTH cycles

Cycle-5 canon `[-1.334,-1.283]`; cycles 6 and 7 both carry `[-1.334,-1.282]`. Four occurrences each, same four locations, zero surviving canon occurrences (grep-verified, matching recon exactly):

| location (flagship) | cycle 5 | cycle 6 | cycle 7 |
|---|---|---|---|
| line 13 (abstract) | `[-1.334,-1.283]` | `[-1.334,-1.282]` | `[-1.334,-1.282]` |
| line 57 (Table 1 result row) | `[-1.334,-1.283]` | `[-1.334,-1.282]` | `[-1.334,-1.282]` |
| line 65 (Fig. 2 caption) | `$[-1.334,-1.283]$` | `$[-1.334,-1.282]$` | `$[-1.334,-1.282]$` |
| line 74 (conclusion) | `[-1.334,-1.283]` | `[-1.334,-1.282]` | `[-1.334,-1.282]` |

All companion numerals in those same sentences (`8,146`, `-1.309`, `60,000`, `95\%`) are untouched in both cycles. The lower bound `-1.334` never drifts.

### 2.2 Group D2 — supplement table cell `2.830 → 2.831` — cycle 7 only (recon missed this)

Supplement line 188, simulation target-vector row `(log M* 11.0–12.5, z 0.02–0.05)`:

| cycle | row |
|---|---|
| 5 | `11.0--12.5 & 0.02--0.05 & 390 & 0.856 & 0.610 & 2.830 \\` |
| 6 | identical to cycle 5 |
| 7 | `11.0--12.5 & 0.02--0.05 & 390 & 0.856 & 0.610 & 2.831 \\` |

Only the median u−r cell changes; the other five cells and all 14 other table rows are byte-identical in all three cycles. **This drift is invisible to the current audit** — the invariant list contains only the flagship CI string — so it would have shipped had cycle 7 otherwise passed.

### 2.3 Group D3 — supplement prose span rewrite — cycle 6 only (recon missed this)

Supplement line 169 (simulation-vector note), cycle 6 replaced the artifact-anchored spans with spans recomputed from the displayed table, changing the referent *and* four numerals:

| cycle | text |
|---|---|
| 5 / 7 | "**Across mass bins**, low-sSFR fractions span **0.005-0.729**, and broad optical BPT-selected fractions span **0.003-0.520**." |
| 6 | "**Across the displayed table**, low-sSFR fractions span **0.001-0.856**, and broad optical BPT-selected fractions span **0.001-0.610**." |

The cycle-5 sentence is a near-verbatim carry of the custody artifact's own result bullet (`m3_p3 … result_bullets: "Across mass bins, quenched fractions span 0.005-0.729; optical AGN fractions span 0.003-0.520."`, ranges stored at full precision `[0.005283…, 0.729233…]`, `[0.002703…, 0.520208…]`). Cycle 6's replacement numbers are the min/max of the 15 *displayed* cells (0.001 at line 177; 0.856 and 0.610 at line 188) — arithmetically correct for the new referent, but it silently abandoned the artifact-anchored invariant. Cycle 7 (rebuilt from cycle 5) does not contain this change. Also audit-invisible today.

### 2.4 Benign count changes (no carried value altered)

- Cycle 6 supplement atlas-summary rows (lines 59–66) gain a fourth column (`… & Sec.~\ref{…}`); every numeral in the rows is preserved (full-diff verified) — the manifest's exact-row match flags them, a human confirms layout-only.
- Cycle 7 flagship has one extra `8,146` occurrence and cycle 7 supplement repeats the pilot run-ID (2→4) and pairs-CSV SHA (1→2), all inside newly added, custody-consistent material (§3.2).
- Cycle 6 removed four flagship bibitems (`ellison2021`, `harrison2017`, `strateva2001`, `mendel2014`) and two supplement bibitems (`cidfernandes2011`, `mcnamara2007` — the supplement copies; both remain cited and present in the flagship). None were `\cite`d in the affected documents (both audits: `undefined_citations: []`), so these are uncited-entry cleanups, not breakage — but they are silent deletions a carry rule should also have flagged. Cycle 7 added two supplement bibitems (`dawson2013`, `dominguezsanchez2018`) with matching new citations.

### 2.5 New numerals introduced by the prose phases

Cycle 7 flagship line 39 adds control-reuse statistics that exist nowhere in cycle 5: "**4,239** unique star-forming controls across the **8,146** matches; **2,731** controls are used once, **1,508** are reused, and the most reused control appears **26** times."

I recomputed these from the custody CSV (SHA-verified): unique controls **4,239**; used once **2,731**; reused **1,508**; max reuse **26**. **All four are exactly correct.** Cycle 7's new supplement "Flagship provenance map" table likewise carries row counts (~60,000, ~8,146) and two SHA-256 strings that match the custody receipt character-for-character.

## 3. Root cause (b): re-derivation instead of verbatim carry

### 3.1 The finding

The prose phases (cycle 6 "literature", cycle 7 "introduction") do not treat the base package's numerals as opaque strings to carry. They behave as **data-grounded regenerators**: they consult the underlying custody artifacts (result JSONs, custody receipt, matched-pairs CSV), re-derive quantities, and re-emit every numeral from the derived value using ordinary nearest-rounding.

Evidence chain:

- **E1 — the raw CI value.** `analysis_results.json` (custody SHA match) stores `matched_delta_log_sSFR_median_ci95_bootstrap = [-1.3341385500000003, -1.2821399375]`. Nearest 3-dp rounding: lower `-1.334`, upper **`-1.282`**. Both failing cycles emit exactly `[-1.334,-1.282]`.
- **E2 — cycle 5's upper bound is the anomaly.** Everything else in the flagship is nearest-rounded from the same artifact: `-1.309` (raw `-1.308887`), `0.0045` (raw `0.00446`), `0.00021` (raw `0.000210795`), all counts exact. Only `-1.283` deviates from nearest-rounding (it is the raw value rounded *toward the interval interior*, i.e. truncated inward — or simply mis-rounded; raw `-1.28214` nearest-rounds and truncates to `-1.282` either way, so `-1.283` cannot be produced by any standard per-digit rule except floor-toward-−∞).
- **E3 — the same signature in D2.** Raw `median_u_minus_r = 2.83066` for the line-188 cell; nearest = **2.831** (cycle 7's value); cycle-5's `2.830` is a truncation, and it is the *only* cell among 15×3 fraction/colour cells that is not nearest-rounded in cycle 5 (e.g. `2.85057 → 2.851`, `2.83792 → 2.838` are nearest-rounded in the very next rows). Cycle 7's rewriter "fixed" the one inconsistent cell.
- **E4 — determinism across independent cycles.** Cycle 7 was rebuilt from clean cycle 5, not from cycle 6, yet both produced the identical `-1.282` at all four locations. A memory-hallucination mechanism would not be this reproducible; re-derivation from the same artifact is.
- **E5 — new numerals are correct, not confabulated.** The four control-reuse statistics cycle 7 invented are exactly reproducible from the custody CSV (§2.5), and its new provenance-map SHAs/row counts match the custody receipt. The rewriter verifiably has the artifacts in view.
- **E6 — D3 is re-derivation of an aggregate.** Cycle 6 recomputed table-min/max spans from the 15 displayed cells instead of carrying the artifact's own "across mass bins" spans — same behavior class applied to an aggregate rather than a rounding.
- **E7 — consistency of application.** Wherever canon already equals the nearest-rounded artifact value (≈103 of 105 invariants), re-derivation reproduces canon and nothing appears to change. The observed "drift" is exactly the set-difference between {canon strings} and {nearest-rounded artifact values} — two elements — plus one referent change.

### 3.2 Root-cause statement

> **The prose phases regenerate the manuscript's numbers from the underlying data instead of carrying them verbatim from the base package.** Because the regeneration is arithmetically faithful (nearest-rounding of custody values), it silently rewrites every location where the frozen canon string differs from the recomputed value. The audit gate compares candidates against the frozen cycle-5 string `[-1.334,-1.283]`, so each such cycle fails with `numeric invariants missing`, and the restart-from-clean-base loop reproduces the identical failure — a livelock between a re-deriving writer and a string-frozen auditor.

Two aggravating factors:

1. **Latent canon inconsistency (upstream bug).** Cycle-5/audit canon contains two strings that are not the nearest-rounding of their own custody artifacts (`-1.283`, `2.830`). Whether canon should be corrected to `-1.282` / `2.831` (with the audit list and manuscript changed *together*, plus a stated rounding convention) is a policy decision for Duho/Hwao — **GATED**, listed in the receipt. Until then, canon is canon: candidates must reproduce `-1.283` and `2.830` exactly.
2. **Audit invariant list is too small.** It contains only the flagship CI string; D2 and D3 pass through it unseen. `INVARIANT_MANIFEST.json` (105 entries covering both documents, including every table row) closes this gap and is ready for integrator handoff (GATED).

### 3.3 What it is not

- Not file-lineage corruption: cycle 7's base was byte-clean cycle 5 (SHA-verified), and untouched sections are byte-identical.
- Not a typo: four synchronized occurrences per cycle, twice independently, format-preserving.
- Not fabrication: every regenerated or newly added numeral checked traces exactly to custody data.

## 4. Why this matters beyond unblocking

A regenerate-don't-carry writer turns every rounding convention, aggregate definition, and referent choice in the manuscript into a potential silent diff each cycle. Today the collision is benign (last digit of a CI bound). The same mechanism would just as happily "improve" a threshold, a sample count after re-filtering, or a span definition — and only invariants on the audit list would catch it. Numeric stability of a manuscript under prose iteration must be enforced as a *string-copy contract*, not entrusted to the writer's arithmetic being right.

## 5. The verbatim-carry rule (c) — binding for all future phase lanes

1. **Copy, never re-derive.** Every numeral (and every SHA/run-ID string) that exists in the base package is carried into the candidate **character-for-character**, including formatting (`8,146` vs `8{,}146`, `S/N$\geq3$` vs `S/N$\geq$3`, `[-1.334,-1.283]` spacing). Prose around numbers may change; the numeric strings may not.
2. **No re-rounding, ever.** Do not recompute a number from an artifact, a table, or memory — even when the recomputation is arithmetically more correct than the base string. If a base numeral looks wrong, **stop and report**; do not fix it inline (that is what failed cycles 6 and 7).
3. **New numerals require provenance and registration.** A phase may add a numeral only if (a) it traces to a custody-inventoried artifact by stated field/derivation, and (b) it is added to `INVARIANT_MANIFEST.json` in the same change. Otherwise the addition is out of scope for a prose phase.
4. **Referents are part of the invariant.** A sentence's quantitative referent ("across mass bins" vs "across the displayed table") may not be changed by a prose phase, because it changes which value is correct (D3).
5. **Deletions count too.** Removing a numeral occurrence (or a bibitem) from the base is a numeric change and needs the same explicit declaration.
6. **Pre-audit self-check.** Before a candidate is handed to the audit, the lane checks it against `INVARIANT_MANIFEST.json`: for every entry whose `file` matches, `exact_string` must appear at least `occurrences_expected` times (per `match_mode`), and no near-miss variant of a `ci_interval`/`point_estimate`/`fraction`/`table_row` entry may appear. Any mismatch → the candidate does not go to audit; fix or report.
7. **Canon changes are a separate lane.** Correcting a canon value (e.g. adjudicating `-1.283` vs `-1.282`) is a declared numeric-change task with Duho approval that updates the manuscript, the audit invariant list, and the manifest **atomically** — never a side effect of a prose rewrite.

Quick check (from a candidate package root, against the manifest):
`grep -F -c -- '[-1.334,-1.283]' flagship_rp1/aastex/rp1_flagship_polished.tex` → must print `4` (and `grep -F -c -- '[-1.334,-1.282]' …` → must print `0`); analogously for every manifest entry.

## 6. Cross-references

- `INVARIANT_MANIFEST.json` — 105 machine-checkable entries, canon anomalies flagged with full-precision artifact values.
- `INTRODUCTION_LITERATURE_REFERENCE.md` — invariant-safe reference block for future introduction/literature lanes.
- `P1_RECEIPT.md` — snapshot/artifact hashes, coordination-file checks, GATED follow-up queue.

`FABLE_BURN_P1_RCA_20260711T010503Z`
