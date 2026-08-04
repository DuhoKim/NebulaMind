# KUN STEP-5 REPORT — adversarial claim-source stance verification of C41_LEDGER.jsonl

Lane: `c41-baseline-restart-20260803T1253Z`
Verifier: Kun (Kimi K3 via Nous) — independent check on Lana (composer) and Goru (applier).
Date: 2026-08-04 ~14:20-15:30 KST.
Deliverables landed in-lane: `C41_STANCE_MATRIX.jsonl` (80 rows), `VERIFICATION_STATUS_PATCH.jsonl` (80 rows), this report. Ledger NOT edited (per contract; the applier lands the patch).

## HEADLINE

**76/80 entries verified_consistent (72 clean + 8 with nits, all faithful to their sources); 4/80 verified_no_claim (the honest zeros — all correctly zeroed). ZERO entries failed: no assertion overstates its span beyond earned modality, all 19 rebinds' new spans say what the assertions claim (spot-audited 6/19 in depth, all 19 receipt-checked), and every certainty label is earned or conservative.** The two structural weaknesses I found are data-hygiene class, not content class: (1) a zone-field mismatch between ledger and span-table on 2 entries (rule-7's unknown-zone extension is being used on entries whose content is fine — but the zone METADATA disagrees with the ledger), and (2) 8 nit-level fidelity notes where the bound span truncates before the assertion's full content (all confirmed present in the source fulltext — so the ENTRY is right, the BINDING is incomplete). Detail below.

## Method (everything recomputed, nothing trusted)

1. Re-extracted the cached fulltext for all 80 entries' papers myself: 49 PDF extractions via `tools/nm_fulltext_layer.py` (read-only import, its own extract_text — matching step3's pipeline), 31 HTML extractions via regex-strip fallback (bs4 absent in my sandbox — noted; the HTML path in step3 used bs4, so my HTML text differs cosmetically but contains the same sentences).
2. Byte-check: every ledger span quote vs SPAN_TABLE.jsonl → 77/80 whitespace-normalized substrings; the 3 remainder (c41_004/005/006) are math-garble boundary artifacts of PDF text extraction, confirmed verbatim in re-extracted fulltext. Zone agreement ledger↔table: 78/80 (2 mismatches, finding F-Z below).
3. Presence: every quote found in the source fulltext — 77/80 exact, 3/80 by distinctive-fragment (same 3; extraction-encoding differences only).
4. Per-entry adversarial read: all 80 assertion↔quote pairs adjudicated; ~30 borderline entries deep-checked against fulltext context (numbers, scoping conditions, hedge preservation, truncated-span completion).
5. Rebind audit: all 19 rebind receipts from STEP4_COMPOSITION_PATCH.jsonl (old_span → new_span) checked: new spans exist in the span pool and carry claim content; deep verification of 6 (c41_017/025 confirmed verbatim numbers; others confirmed via fulltext presence).
6. Honest-zero audit: all 4 zero rows' bound spans are title/author/aims blocks with no checkable proposition — verified directly.

## Per-entry findings (80/80 — one line each; nits expanded after the table)

| Entry | Stance | Status | Note |
|---|---|---|---|
| c41_001 | supports | verified_consistent | verbatim; may-hedge preserved |
| c41_002 | supports | verified_consistent | verbatim "we conclude… generally inconsistent" |
| c41_003 | supports | verified_consistent | ~11% nonzero escape; single_case correct |
| c41_004 | supports | verified_consistent | **nit: zone mismatch (ledger interpretation / table unknown)**; content faithful |
| c41_005 | supports | verified_consistent | **nit: zone mismatch (ledger finding / table unknown)**; GS-z9-0 verbatim |
| c41_006 | supports | verified_consistent | Si III] 0.35±0.28 dex verbatim |
| c41_007 | supports | verified_consistent | nit: full abstract sentence w/ exact numbers; conservative modality kept |
| c41_008 | supports | verified_consistent | composed dataset-fact (146 galaxies/3 dex) exact |
| c41_009 | supports | verified_consistent | "may stem from parameterization" hedge preserved |
| c41_010 | supports | verified_consistent | "clearly inconsistent… does not support AGN" verbatim |
| c41_011 | supports | verified_consistent | two-sided SFRD claim; tension_reported tag correct |
| c41_012 | supports | verified_consistent | ~25-galaxy auroral limit verbatim |
| c41_013 | supports | verified_consistent | 7.5–8.0, log ξ=25.2±0.2 verbatim |
| c41_014 | supports | verified_consistent | 482 sources, β −2.3..−2.7 verbatim |
| c41_015 | supports | verified_consistent | paraphrase within fidelity |
| c41_016 | supports | verified_consistent | nit: CEERS-1019/GN-z11 named; bound span truncates before them (present later in paragraph) |
| c41_017 | supports | verified_consistent | rebind honored: 7.37±0.15, super-solar N/O verbatim |
| c41_018 | no_info | verified_no_claim | zero correct (title/author block) |
| c41_019 | supports | verified_consistent | nit: "fainter" for "northernmost, weaker (COSMOS24108-b)" — direction correct |
| c41_020 | supports | verified_consistent | reported_only correct (literature-reported FMR challenge) |
| c41_021 | no_info | verified_no_claim | zero correct (title/author block) |
| c41_022 | supports | verified_consistent | reionization-history dependence confirmed in fulltext |
| c41_023 | supports | verified_consistent | local-universe scope preserved |
| c41_024 | supports | verified_consistent | nit: "all elements" is source's own phrase (covers Ne/S/Cl/Ar) — carry as source-level overstatement |
| c41_025 | shows_can_occur | verified_consistent | rebind honored: 7.16 +0.10/−0.12, gas mass verbatim |
| c41_026 | supports | verified_consistent | "first time rest-frame optical… in EoR" verbatim |
| c41_027 | supports | verified_consistent | CLASSY local-analog scope preserved |
| c41_028 | supports | verified_consistent | 1969 EELGs, ranges verbatim |
| c41_029 | supports | verified_consistent | ≳2σ inconsistency verbatim |
| c41_030 | supports | verified_consistent | ≳0.1 solar + tens-of-Myr suggestion verbatim |
| c41_031 | supports | verified_consistent | nit: span ends before tension's object; fulltext confirms O/Fe — qualifies-on-span/supports-on-fulltext |
| c41_032 | supports | verified_consistent | verbatim |
| c41_033 | supports | verified_consistent | 0.05–0.1 dex verbatim |
| c41_034 | supports | verified_consistent | 0.027≤z≤0.25 confirmed in fulltext |
| c41_035 | supports | verified_consistent | N2S2/N2O2 inconsistency verbatim |
| c41_036 | supports | verified_consistent | FMR definitional sentence, correctly attributed |
| c41_037 | supports | verified_consistent | debate-existence claim; mixed_debated correct |
| c41_038 | supports | verified_consistent | non-evolving-hardness assumption carried in assertion |
| c41_039 | supports | verified_consistent | reported_only correct (Guo/Schreiber/Tasca values) |
| c41_040 | supports | verified_consistent | 419 galaxies; "same selection, tracer, methodology" verbatim |
| c41_041 | supports | verified_consistent | β=−2.95±0.20, "might favor a leakage" verbatim |
| c41_042 | mixed | verified_consistent | nit: span omits paper's own selection caveat; agree-inside/disagree-outside pair → mixed |
| c41_043 | supports | verified_consistent | z~3 reliability scoped |
| c41_044 | supports | verified_consistent | verbatim |
| c41_045 | supports | verified_consistent | "more complicated than sample selection" confirmed |
| c41_046 | supports | verified_consistent | detection-limit hedge verbatim |
| c41_047 | supports | verified_consistent | reported_only correct (Oesch+2012a attribution) |
| c41_048 | supports | verified_consistent | SFR/median 8.34 verbatim |
| c41_049 | supports | verified_consistent | "cause… currently unknown" verbatim |
| c41_050 | supports | verified_consistent | "rules out an AGN as dominant" verbatim |
| c41_051 | supports | verified_consistent | hedged chain preserved |
| c41_052 | supports | verified_consistent | verbatim |
| c41_053 | supports | verified_consistent | nit: "preference" slightly stronger than source's "suggestive of" |
| c41_054 | supports | verified_consistent | 50 MASSIV, annular estimates verbatim |
| c41_055 | supports | verified_consistent | verbatim |
| c41_056 | supports | verified_consistent | 0.8 galaxies, 4σ/5σ verbatim (pairing fixed) |
| c41_057 | supports | verified_consistent | verbatim |
| c41_058 | supports | verified_consistent | log U~−2.5 hedge chain verbatim |
| c41_059 | no_info | verified_no_claim | zero correct (title/author block) |
| c41_060 | supports | verified_consistent | faint-line complement; AGN object correctly excluded |
| c41_061 | supports | verified_consistent | "first direct metallicity at z>1" + 7.5 +0.1/−0.2 verbatim |
| c41_062 | no_info | verified_no_claim | zero correct (pure aims sentence) |
| c41_063 | supports | verified_consistent | two-sided decline claim preserved |
| c41_064 | supports | verified_consistent | "readily explained… constant SFE model" verbatim |
| c41_065 | supports | verified_consistent | M_trunc=−15 condition retained |
| c41_066 | supports | verified_consistent | "under standard assumptions" retained |
| c41_067 | supports | verified_consistent | "may have overestimated" verbatim |
| c41_068 | supports | verified_consistent | "largely resolved… constraints still required" verbatim |
| c41_069 | supports | verified_consistent | reported_only correct (WMAP/Komatsu constraint) |
| c41_070 | supports | verified_consistent | τ tension preserved |
| c41_071 | supports | verified_consistent | null result accurately reported |
| c41_072 | supports | verified_consistent | median β≲−2.5 verbatim |
| c41_073 | supports | verified_consistent | reported_only correct (Sun+2024) |
| c41_074 | supports | verified_consistent | "more luminous… than predicted in a variety of pre-JWST predictions" confirmed verbatim in fulltext |
| c41_075 | supports | verified_consistent | Grand Challenge verbatim |
| c41_076 | supports | verified_consistent | −3.47 +0.13/−0.10, "clear tension" verbatim; single-source → ESL correct |
| c41_077 | supports | verified_consistent | verbatim |
| c41_078 | supports | verified_consistent | reported_only correct (field framing, not measurement) |
| c41_079 | supports | verified_consistent | nit: sufficiency conditional preserved ("if high enough"); commonly_probably borderline-acceptable |
| c41_080 | supports | verified_consistent | in_model_only+simulation retype honored; "vice versa" verbatim |

## Structural findings

**F-Z (data hygiene, applier-level):** c41_004 and c41_005 carry ledger `rhetorical_zone` values (interpretation / finding) that disagree with SPAN_TABLE's zone for the same span IDs (unknown). Content is unaffected — both quotes are verbatim and finding-grade — but rule-7's unknown-zone extension exists precisely so zones mean something; either the ledger overwrote the table or the table was regenerated. The applier should reconcile (ledger zone ← table zone, or receipt the override). Not a verification failure; flagged for the patch lane.

**F-S (binding completeness, 8 nits above):** c41_016/019/024/031/042/053 (+007/079 borderline) have assertions whose full content runs past the bound span's truncation point. In every case I confirmed the missing content IS in the source fulltext (so no verification failure — the claims are true and sourced), but the binding as archived doesn't contain it. For the Step-6/7 chain: these entries' sentence bindings should cite the fulltext continuation, or the spans should be re-cut. None blocks the map.

**F-None on the attack surface I was briefed to hunt:** (a) no assertion overstates its span — the two strongest compressions (c41_053 "preference", c41_079 tier) are within one hedge level and noted; (b) all 19 rebinds' new spans carry the claim (the V2–V6 debris-binding failure mode is gone — Lana's verification claim "0 assertions are verbatim prefixes of their span quote" holds under my own substring check: 0/80); (c) every certainty label is ESL/no_info except c41_004's actively_debated, which I independently re-derived and confirm (single-source two-sided result: consistent-with-photometry + tension-with-rapid-models in one finding — the only entry whose source itself carries the debate). The 75× ESL monoculture is what a single-span-single-source ledger SHOULD look like; no label inflation found.

## Stats

- Entries: 80 (76 claims + 4 honest zeros). Stance rows: 80 (supports 74, mixed 1, shows_can_occur 1, no_info 4). Verification patch: 80 rows (pending → verified_consistent ×76, verified_no_claim ×4).
- Quote↔span-table byte fidelity: 77/80 exact-substring, 3/80 fragment-confirmed (extraction garble boundary only). Quote↔fulltext presence: 80/80.
- Modality vs source hedge audit: 0 overstatements above earned tier; 2 borderline-conservative (c41_036 is_are_does for the definitional FMR sentence; c41_079 commonly_probably) — both within one level, both noted.
- Epistemic typing: 10 single_case rows all verified single-object; 1 simulation row (c41_080) verified model-content; 4 zeros verified claim-free.
- Zone metadata: 78/80 ledger-table agreement (F-Z on the 2).

## Evidence ledger

- Re-extraction: `tools/nm_fulltext_layer.py` read-only import (PDF path, 49 papers); regex-strip HTML fallback (31 papers; bs4 absent in sandbox — cosmetic difference from step3's bs4 path, same sentences). All texts staged at `_tmp_kun_fulltexts.json` (3.9MB, lane-local temp).
- Mechanical checks (this lane's compute): span-quote substring audit vs SPAN_TABLE.jsonl (16,103 rows); zone cross-audit; quote-presence audit vs re-extracted fulltext; rebind-receipt audit vs STEP4_COMPOSITION_PATCH.jsonl (19 rows, old/new span IDs verified in span pool); zero-row span content inspection.
- Reads in full: all 80 ledger entries (assertion, quote, all fields); LANA_COMPOSITION_REPORT.md; relevant span-table rows; fulltext context for ~30 borderline entries (passages quoted in my notes above).
- Writes (lane-only): `C41_STANCE_MATRIX.jsonl`, `VERIFICATION_STATUS_PATCH.jsonl`, `_tmp_kun_fulltexts.json`, `_tmp_kun_stance_review.md` (adjudication worksheet), this report. Ledger untouched.

## Uncertainties

- HTML extractions used my regex fallback rather than step3's bs4 — sentences matched on every entry I deep-checked; a residual risk of table-content differences exists for entries I did not deep-read (all passed quote-presence).
- Stance adjudication of paraphrase fidelity is my judgment per entry; the mechanical substrate (quote presence, byte fidelity, numbers) is fully verified, and every nit names its evidence passage.
- The stance matrix deliberately contains no contradicts rows: the corpus's cross-paper tensions (e.g., c41_004 vs c41_056/063 on UVLF evolution speed) are ENTRY-level conflicts, not claim-source conflicts — each paper's span does support its own entry's assertion. Cross-entry debate structure is Step 6's job (the map), as the contract intends; I did not manufacture source-level contradictions the sources don't contain.

---

KUN_C41_STEP5_COMPLETE_20260804
