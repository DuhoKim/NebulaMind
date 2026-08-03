# CONTRACT_R3_DRAFT — offline r3 redesign of the C1r output contract

Packet: `gemini-dr-c1r-contract-r3-manual-triage-20260713T024458Z` · Lane: Lana (P1a, high reasoning) · Coordinator: Hwao.
Phase: P1a only. **This file is a reviewable DRAFT. It does not overwrite, edit, or supersede the sealed contract.** No classification (P2) is performed here.

**Contract of record (immutable, path-corrected per Duho 2026-07-13):** `../gemini-dr-revised-canary-20260712T045317Z/prompt/C1r.md`, expected sha256 `fffac44fbf6e9abe3afb1f8f34f3a9e3e7688991f319c4927459fb29ac00e1ef` (byte-identical to sealed `runs/c1r/prompt_submitted.md`). All "current rule" quotations below cite that sealed file by `C1r.md:<line-range>`.

**Boundaries honored:** offline; no network/source retrieval/browser/git/DB/dashboard/deploy/cron/account action; no validator implementation; no live canary. Source IDs stay quarantined (`QUARANTINED_PENDING_LOCAL_CHECK`); every scientific / source-fidelity question is deferred to the later, separately gated manual verification pass — this draft decides **contract wording and mechanical checks only**, never whether a paper actually supports a claim.

**Governance note:** the sealed C1r run remains `FAIL_CLOSED`; nothing here retro-accepts it. r3 is a *proposed future* contract. Where an r3 decision would re-type a current finding (notably D3), that is flagged and is the archetype for the P2 `CONTRACT_R3_CHANGE` lane — named here, classified later.

---

## 0. Decision summary (concrete choices; one per item)

| D | Question | r3 choice (concrete) | FAIL_CLOSED_IMPACT |
|---|---|---|---|
| D1 | S1 comparison scope | Type the comparison rule by cell role: `emergent`/`notes` result-claims + GAP + non-S2 bullets require the token; `calibration_target`/`feedback_params` register cells are exempt via a typed `CALIBRATION_TARGET_DESCRIPTION` marker. | **NO** |
| D2 | Four-qualifier fraction scope | Rule applies to **every quoted numeric fraction/incidence** (universal); tuned/model parameters are *labeled*, not exempted, via a `TRACER=MODEL_PARAMETER` fill convention. SIMBA ~10% still fails without syntax (upholds T14 Rule B). | **NO** |
| D3 | S2 Result vs Citation authority | The **dedicated Citation cell is the single authoritative citation** for the S2 row; Result cell is bound to it as one atomic record and is not independently citation-gated. Ends the schema-vs-C4 redundancy. | **YES** |
| D4 | Ledger integrity | Index-based bidirectionality; per-source uniqueness on normalized keys; non-empty short names; `abs\|html\|pdf`+DOI/ADS normalization; `article`/`article-abstract` (14↔29) surfaced as `NEAR_DUPLICATE`. | **NO** |
| D5 | GAP granularity | Exactly **one `GAP:` item per rendered paragraph/logical unit**, each self-carrying citation-or-token. Removes the merged-`<p>` loophole. | **NO** |
| D6 | Validator/fixture consequences | Design matrix only (rule → check → fixture → expected RED). No code. | n/a |

Only **D3** relaxes a gate; its preserved guard is specified in §D3 and consolidated in §8.

---

## D1 — Simulation–observation comparison definition + Section-1 scope

- **Current rule** — `C1r.md:110-113` (C6): "Do not make a simulation-observation comparison outside Section 2. If one is unavoidable in an allowed bullet or GAP line, that same logical unit must contain exactly one of the two exact tokens MATCHED_SELECTIONS or NON_COMMENSURABLE_UNMATCHED_SELECTIONS. A comparison elsewhere without one of those tokens is a C6 failure." Section 1's table (`C1r.md:29`) includes the column "Explicitly emergent (stated NOT calibrated)".
- **Observed pressure** — Section 1's purpose is to describe what each simulation was calibrated against, and the "Explicitly emergent" cell naturally states that an un-tuned output *reproduces/agrees with* an observation. Under the flat rule this trips `UNLABELED_COMPARISON` on genuine emergent-agreement cells (5 sealed S1 emergent cells + the FLAMINGO cell resolved in T14 Rule A), while calibration-target descriptions ("tuned to reproduce observed X") are *not* out-of-sample validations yet look comparison-like. The detector needs a typed distinction, not prose keyword guessing.
- **Proposed r3 wording** — Replace C6's outside-Section-2 clause with:
  > A "simulation–observation comparison" is an **agreement or tension result claim**: a statement that a simulation's *output* agrees with, matches, reproduces, or is in tension/discrepancy/offset with an observation or observable dataset. Such a claim belongs in Section 2. Outside Section 2, any allowed unit (a Section-1 `Explicitly emergent` or `Notes` cell, a Section-3 bullet, or a Section-5 GAP line) that makes an agreement/tension result claim MUST contain exactly one of `MATCHED_SELECTIONS` or `NON_COMMENSURABLE_UNMATCHED_SELECTIONS` in the same cell/line. A **calibration-target description** — a statement that a parameter or model was tuned to reproduce an observation — is NOT a comparison; Section-1 `Stated calibration targets` and `Feedback parameters tuned` cells carry the typed prefix `CALIBRATION_TARGET_DESCRIPTION:` and are exempt from the comparability token. The exemption is valid only in those two columns; an agreement/tension *result* claim placed in any cell still requires the token.
- **Rationale** — Scopes the token requirement to genuine validation comparisons by *cell type*, matching the table's own column semantics; preserves the guard exactly where over-claim risk lives (emergent/notes result claims) while ending false positives on calibration register. Consistent with T14 Rule A (named-observable objects like "cluster scaling relations" count as observational references in emergent cells).
- **Positive example** — FLAMINGO `Explicitly emergent` cell: "Calibrated runs reproduce cluster scaling relations, which were strictly excluded from calibration" → agreement result claim in an emergent cell, no token → **C6 FAIL** (correct; matches the T14-amended pin).
- **Negative example** — SIMBA `Stated calibration targets` cell: "CALIBRATION_TARGET_DESCRIPTION: tuned to reproduce the observed z=0 galaxy stellar mass function" → calibration register in col 1 → exempt → **no C6 finding**.
- **Validator implication** — Comparison scan runs per typed cell/line; roles `{emergent, notes(result-claim), gap_line, non_s2_bullet}` are token-gated; roles `{calibration_target, feedback_params}` bearing the `CALIBRATION_TARGET_DESCRIPTION:` prefix are skipped; the observational-reference phrase list is fixture-scoped and extendable only by a logged r3 note (never silently).
- **FAIL_CLOSED_IMPACT: NO** — the token requirement is retained wherever a genuine comparison exists; the exemption is confined to definitionally-non-validation calibration cells, and a mis-placed result claim cannot use the marker to escape (marker valid only in col 1/2; result verbs in col 1/2 without the marker still gate).

---

## D2 — Four-qualifier numeric rule scope (the SIMBA ~10% case)

- **Current rule** — `C1r.md:104-106` (C6): "Any quoted fraction or incidence, anywhere in the body, carries the four qualifiers in exactly this syntax within the same line/cell: `TRACER=<...>; SELECTION=<...>; DENOMINATOR=<...>; REDSHIFT=<...>` using NOT_APPLICABLE as the value of any individual qualifier that does not apply."
- **Observed pressure** — T14 Rule B deferred to r3 the question of whether this binds *every* quoted fraction or only population/statistical quantities. SIMBA's tuned coupling "~10% of available supernova energy" is a quoted fraction with a numeric value but is a *model input parameter*, not an observational population fraction; the four qualifiers (tracer/selection/denominator/redshift) are meaningful for observational fractions and largely `NOT_APPLICABLE` for a tuned constant. Separately, the repaired validator already gates on a *quoted numeric value* so bare words ("cluster gas fractions", "fraction of SN energy" with no number) do not trigger.
- **Proposed r3 wording** —
  > The four-qualifier syntax applies to **every quoted numeric fraction or incidence** (a fraction/percentage/ratio/incidence with a numeric value) anywhere in the body. Two typed fills are defined: (a) an **observational/population fraction** (a fraction or incidence of a population of objects — e.g. quenched fraction, gas fraction of passive galaxies, radio-AGN incidence) fills `TRACER/SELECTION/DENOMINATOR/REDSHIFT` with real values or `NOT_APPLICABLE` per qualifier; (b) a **model/tuned-parameter fraction** (a numeric coupling/efficiency input, e.g. "~10% of available SN energy") fills exactly `TRACER=MODEL_PARAMETER; SELECTION=NOT_APPLICABLE; DENOMINATOR=<coupled quantity>; REDSHIFT=NOT_APPLICABLE`. A quoted numeric fraction with no qualifier syntax is a C6 failure regardless of class. A fraction/incidence *word* with no quoted numeric value is not gated.
- **Rationale** — Resolves the deferred question in favor of universal coverage (fail-closed) while giving parameter fractions an honest, checkable fill instead of an exemption. Upholds T14 Rule B (no role-based exemption; SIMBA ~10% remains a genuine `MISSING_QUALIFIER` in the amended 17-finding pin) and preserves the repaired validator's numeric gate (removes the 3 word-only false positives).
- **Positive example** — "quenched fraction TRACER=color-sSFR; SELECTION=M*>10^10.5; DENOMINATOR=all centrals; REDSHIFT=0.0-0.1" → numeric fraction with full syntax → MANUAL (semantic content checked later).
- **Negative example** — SIMBA feedback-parameter cell: "couples ~10% of available SN energy" with no qualifier syntax → quoted numeric fraction, no syntax → **C6 `MISSING_QUALIFIER` FAIL** (the T14-amended finding). Contrast: "cluster gas fractions are observable-mapped" (no number) → **no finding**.
- **Validator implication** — Numeric-fraction gate (quoted value required) → require the four-qualifier regex; accept `TRACER=MODEL_PARAMETER;…` as a valid parameter fill; bare fraction/incidence words remain ungated.
- **FAIL_CLOSED_IMPACT: NO** — the rule is retained universally; parameter fractions are labeled rather than exempted, so no fraction escapes the gate.

---

## D3 — Section-2 Result-cell vs Citation-cell authority

- **Current rule** — `C1r.md:37` gives Section 2 a dedicated final "Citation" column; `C1r.md:39-40` requires it non-empty (checkable citation or `UNCITED_NOT_USABLE`); but C4 `C1r.md:86-92` states "a citation in the Simulation cell or a dedicated Citation cell does not satisfy the other claim-bearing cells." So the Result cell must repeat its own citation while a dedicated Citation column also exists.
- **Observed pressure** — The schema asks for a Citation column and then declares that column insufficient for the Result cell it serves. The model populated all 8 dedicated Citation cells but none of the 8 Result cells → 8 genuine C4 failures that are really a contract-design redundancy: one atomic validation record forced to cite itself twice.
- **Proposed r3 wording** —
  > For Section 2 only, each row is one atomic validation record. The **dedicated Citation cell (final column) is the authoritative citation** for the entire row; it must be a checkable citation or `UNCITED_NOT_USABLE` and must never be empty. The Result cell states the agreement/tension result and magnitude and is **not** independently citation-gated; it is bound to the same row's Citation cell. This supersedes, for Section 2 rows only, the C4 clause that a dedicated Citation cell "does not satisfy the other claim-bearing cells." Section 1 (independent per-cell claims) and Section 4 (independent per-cell status claims) retain the C4 same-cell citation rule unchanged.
- **Rationale** — A validation record is a single claim; repeating the identifier in Result and Citation cells is mechanical duplication a deterministic renderer should perform, not a research model. Matches the root-cause recommendation ("source IDs once per atomic validation record"). Removes an internal contract contradiction rather than an evidentiary guard.
- **Positive example** — Row "IllustrisTNG | quenched fractions | tension: over-quenched at low mass | NON_COMMENSURABLE_UNMATCHED_SELECTIONS | No | arXiv:xxxx.xxxxx" → Result uncited, Citation cell populated and non-empty → **PASS under r3** (the citation is authoritative for the row).
- **Negative example** — Same row with an **empty** Citation cell → **FAIL** (`EMPTY_CITATION_CELL`): the single authoritative channel is missing, so the record is uncited.
- **Validator implication** — Section-2 citation gate reads the dedicated Citation cell (non-empty, resolvable, quarantined); the Result cell is excluded from C4 same-cell gating; the "authoritative cell" binding is per row. Under r3 the 8 sealed S2 Result-cell findings are **re-typed, not deleted** — they become `CONTRACT_R3_CHANGE` entries absorbed by D3 (named for P2; not classified here).
- **FAIL_CLOSED_IMPACT: YES** — this removes the Result-cell same-cell citation requirement for Section 2. **Preserved guard:** every Section-2 row must still carry exactly one authoritative, non-empty, resolvable citation in its dedicated Citation cell, bound to the Result cell as one record; an empty or missing Citation cell is still a hard FAIL; the citation stays `QUARANTINED_PENDING_LOCAL_CHECK` and its actual support is a later manual `VERIFY_SOURCE_FIDELITY` decision. Net effect: no validation claim becomes uncited; the citation is relocated to one authoritative cell, not dropped.

---

## D4 — Ledger integrity (uniqueness, names, index↔source, normalization, near-duplicates)

- **Current rule** — Ledger line format `C1r.md:59`: "One line per cited item: `<short name> | <citation or UNCITED_NOT_USABLE> | QUARANTINED_PENDING_LOCAL_CHECK`." Bidirectional/unique `C1r.md:60-61` and C7 `C1r.md:115-117`: "every inline citation appears in the Links ledger; every ledger row is cited inline at least once; each ledger row is unique; each ledger row ends with `QUARANTINED_PENDING_LOCAL_CHECK`. No orphan rows, no inline-only citations, no duplicates."
- **Observed pressure** — Sealed ledger: 46 rows for 37 unique sources (9 duplicate rows), 46 blank `<short name>` fields (the chip occupied the slot), 12 orphan indices `{2,5,8,9,13,16,18,23,24,29,31,33}`, and a normalizer-invisible near-duplicate 14↔29 (`article/` vs `article-abstract/` of the same paper). The original validator's URL-set method hid duplicates and misclassified all 37 as orphaned.
- **Proposed r3 wording** —
  > The Links ledger is checked over **source indices**, not raw URL strings. (1) **Bidirectionality:** the set of source indices cited inline in Sections 1–5 (resolved citation chips ∪ inline literal IDs) MUST equal the set of ledger indices; a ledger index never cited inline is an orphan FAIL, a cited index absent from the ledger is an inline-only FAIL. (2) **Uniqueness:** exactly one ledger row per unique source after normalization; a second row for the same source is a duplicate FAIL. (3) **Non-empty short name:** the `<short name>` field MUST be a non-empty human-readable label distinct from the citation/index; blank is a FAIL. (4) **Normalization:** before uniqueness/bidirectionality, canonicalize arXiv `abs|html|pdf` variants (strip `vN`) to `/abs/<id>`, and DOI/ADS to one canonical form. (5) **Near-duplicate:** two indices whose canonical forms differ only by a landing-page variant (e.g. `article/` vs `article-abstract/`, or `/abs/` vs the same paper's publisher DOI) are FLAGGED `NEAR_DUPLICATE` for manual reconciliation — never silently merged, never auto-failed. (6) Every row still ends with `QUARANTINED_PENDING_LOCAL_CHECK`; existence and support remain manual.
- **Rationale** — Encodes exactly the sealed failure modes the set-based check missed, while keeping source verification out of scope (quarantine preserved). Near-duplicate is surfaced, not resolved, because deciding "same paper?" is a manual judgment.
- **Positive example** — "IllustrisTNG methods (Pillepich+2018) | arXiv:1703.02970 | QUARANTINED_PENDING_LOCAL_CHECK", cited once inline → unique, named, bidirectional → PASS.
- **Negative example** — two rows both normalizing to `arxiv.org/abs/2410.19905` (one `/abs`, one `/pdf`) with empty first fields → 1 `DUPLICATE_ROW` FAIL + 2 `BLANK_SHORT_NAME` FAIL; indices 14 `…/article/…` and 29 `…/article-abstract/…` → 1 `NEAR_DUPLICATE` flag (manual).
- **Validator implication** — index bidirectionality; normalized-key uniqueness; blank-short-name check on the first pipe field; normalizer extended to `pdf` + DOI/ADS; `NEAR_DUPLICATE` emitted as a distinct MANUAL finding.
- **FAIL_CLOSED_IMPACT: NO** — strictly tightens C7 (adds duplicate/blank-name/near-duplicate/normalization detection absent from the original); nothing relaxed.

---

## D5 — One GAP item per paragraph / logical unit

- **Current rule** — Section 5 `C1r.md:53-56` and C2 GAP device `C1r.md:76-78`: "GAP: lines only. Each GAP line either carries a checkable citation OR ends with the exact token `ASSERTED_ABSENCE_NOT_SYSTEMATICALLY_VERIFIED`."
- **Observed pressure** — The model rendered all four GAP lines as spans inside a single `<p>`, so per-GAP checks operated on one merged block; GAP2/GAP4's absence token could satisfy the whole block, masking whether GAP1/GAP3 were individually cited. A rendering ambiguity, not a science gap.
- **Proposed r3 wording** —
  > Each GAP item MUST be its own rendered paragraph / block-level logical unit: exactly one `GAP:` line per paragraph, each independently carrying its own checkable citation or the exact token `ASSERTED_ABSENCE_NOT_SYSTEMATICALLY_VERIFIED`. A paragraph containing more than one `GAP:` line is a structure failure; a GAP line whose own unit carries neither a citation nor the token is a failure regardless of sibling lines.
- **Rationale** — Guarantees per-GAP evaluability and closes the merged-block loophole; each absence assertion stands or falls on its own citation/token.
- **Positive example** — four separate `<p>GAP: … | citation-or-token</p>` blocks → each validated independently → PASS.
- **Negative example** — one `<p>` with "GAP: A [cite]\nGAP: B\nGAP: C [cite]\nGAP: D TOKEN" → the uncited B line is not individually satisfied → structure FAIL + per-line FAIL on B.
- **Validator implication** — capture splits GAP lines into independent `gap_line` units; C2/C4 GAP checks run per unit; a paragraph with >1 `GAP:` line raises a structure FAIL.
- **FAIL_CLOSED_IMPACT: NO** — adds a structural requirement and removes a loophole; strictly fail-closed.

---

## D6 — Validator / fixture consequences (design matrix only; no code)

| r3 rule (from D#) | Validator check | Fixture need | Expected RED |
|---|---|---|---|
| D1 typed comparison scope | per-cell comparison scan; token-gate `{emergent,notes-result,gap,non-s2 bullet}`; exempt `CALIBRATION_TARGET_DESCRIPTION:` col1/col2 | S1 emergent agreement cell (no token); S1 calibration_target cell (marker); FLAMINGO named-observable emergent cell | emergent + FLAMINGO cells → `UNLABELED_COMPARISON` FAIL; calibration_target cell → no finding |
| D2 universal fraction + MODEL_PARAMETER fill | numeric-value gate → require four-qualifier syntax; accept `TRACER=MODEL_PARAMETER;…` | SIMBA "~10%" param cell (no syntax); observational quenched-fraction cell (full syntax); "cluster gas fractions" (no number) | SIMBA cell → `MISSING_QUALIFIER` FAIL; syntax cell → MANUAL; bare-word cell → no finding |
| D3 S2 dedicated-citation authoritative | S2 citation gate on dedicated cell; Result cell excluded from C4 same-cell gate | S2 row: populated Citation + uncited Result; S2 row: empty Citation cell | first row → PASS (no Result-cell FAIL); second row → `EMPTY_CITATION_CELL` FAIL. (Re-types the 8 sealed S2 Result-cell findings → `CONTRACT_R3_CHANGE`/D3.) |
| D4 ledger integrity | index bidirectionality; normalized-key uniqueness; blank-name; `abs\|html\|pdf`+DOI/ADS norm; near-dup flag | sealed ledger (46 rows/37 sources, 9 dups, 46 blank names, 12 orphans, 14↔29) | 12 `ORPHAN_LEDGER_SOURCE` + 9 `DUPLICATE_ROW` + 46 `BLANK_SHORT_NAME` FAIL; 14↔29 `NEAR_DUPLICATE` flag |
| D5 one GAP per paragraph | per-`gap_line` split; >1 `GAP:` per paragraph → structure FAIL | merged 4-GAP `<p>` (negative); 4 separate `<p>` (positive) | merged block → structure + per-line FAIL; separate blocks → PASS |

No code is authored in this packet; the above is the design contract a later, separately-gated validator-implementation phase would test against.

---

## PROPOSED r3 CONTRACT TEXT (DRAFT — does not replace sealed `C1r.md`)

> This is the **full standalone proposed r3 contract**. It can be read and executed without consulting the sealed `C1r.md`. It is a DRAFT for review; it does **not** overwrite or supersede the sealed contract of record. `[r3-D#]` tags mark wording that realizes decisions D1–D5; all other wording reproduces the current contract so the text is complete. `<REQ_ID>` and `<COMPLETION_MARKER>` are assigned by the future run packet (a live run needs its own separate Duho gate); no run identifier or approval phrase is minted here.

### r3.0 — Role and question (standalone)

You are a literature analyst for a galaxy-evolution research journal. Report only published work; you have no access to the journal's internal results. The question, scope unchanged: for each major galaxy-formation simulation project (IllustrisTNG, EAGLE, SIMBA, FIRE/FIRE-2, ROMULUS, ASTRID, FLAMINGO, and comparable published suites such as BAHAMAS), what do the METHOD papers state was used to calibrate the feedback/subgrid model, and which later observation comparisons are genuinely out-of-sample (not calibration targets, per the papers themselves)?

### r3.1 — Output discipline (binding)

The report body is STRUCTURED ONLY. Its EXACT top-to-bottom sequence is: (a) the mandatory 4-line meta header (C1); (b) the five numbered content sections below, in order; (c) the Links ledger; (d) the final completion-marker line (C8), alone. NOTHING ELSE may appear — no abstract, introduction, summary, prose paragraph, or free narrative of any kind OUTSIDE the allowed units (meta-header lines, table cells, bullet lines, GAP lines, ledger lines, and the marker line). Every factual claim lives inside a table cell or a single bullet. Any content outside the permitted units is a contract violation.

### r3.2 — Required content sections (exactly five, in order)

**## 1. Calibration ledger** — Markdown table, one row per simulation:
`| Simulation (method-paper citation) | Stated calibration targets (faithful to source wording) | Feedback parameters tuned (as stated) | Explicitly emergent (stated NOT calibrated) | Notes |`
An empty cell is exactly `NONE_FOUND`. A source that is unclear is `AMBIGUOUS_IN_SOURCE` plus the quoted sentence. EVERY claim-bearing cell in the row (calibration-targets, feedback-parameters, explicitly-emergent, notes) carries its OWN same-cell checkable citation or `UNCITED_NOT_USABLE` — the Simulation cell's citation does not cover the other cells (C4). **[r3-D1]** A `Stated calibration targets` or `Feedback parameters tuned` cell that references an observation as a tuning target carries the typed prefix `CALIBRATION_TARGET_DESCRIPTION:` and is exempt from any comparability token; a `CALIBRATION_TARGET_DESCRIPTION:` prefix is valid only in those two columns. An agreement/tension result claim placed in the `Explicitly emergent` or `Notes` cell requires exactly one comparability token in that same cell (C6).

**## 2. Out-of-sample validation ledger** — Markdown table, one row per published out-of-sample comparison:
`| Simulation | Observable | Result (agreement or tension, with magnitude) | COMPARABILITY | Overlap with a Section-1 calibration target | Citation |`
The COMPARABILITY cell is exactly `MATCHED_SELECTIONS` or `NON_COMMENSURABLE_UNMATCHED_SELECTIONS`. **[r3-D3]** The dedicated Citation cell is the single authoritative citation for the whole row: it must be a checkable citation or `UNCITED_NOT_USABLE` and must never be empty. The Result cell states the agreement/tension result and magnitude and is bound to the same row's Citation cell as one atomic validation record; the Result cell is not independently citation-gated. (This is the only place the C4 same-cell rule is relocated rather than repeated — see C4.)

**## 3. Double-counting warnings** — Bullet list only. Each bullet is one published warning against treating a calibration target as evidence of predictive success, stated as an attributed claim with a same-bullet checkable citation or `UNCITED_NOT_USABLE`. No prose outside bullets.

**## 4. Feedback-relevant observables map** — Markdown table:
`| Simulation | Quenched fractions | Gas fractions of passive galaxies | Outflow demographics | Hot-halo/cavity properties | Radio-AGN incidence |`
Each observable cell is `CALIBRATED`, `EMERGENT`, or `NOT_REPORTED`. A `CALIBRATED` or `EMERGENT` cell carries a same-cell checkable citation (or `UNCITED_NOT_USABLE`). A missing status is written exactly as `NOT_REPORTED — NONE_FOUND`.

**## 5. Gaps** — GAP: lines only. **[r3-D5]** Exactly one `GAP:` item per rendered paragraph / block-level logical unit. Each GAP line either carries a checkable citation OR ends with the exact token `ASSERTED_ABSENCE_NOT_SYSTEMATICALLY_VERIFIED` (use this when asserting that no published test exists and the absence itself cannot be cited). No uncited, unlabeled GAP line is allowed, and a paragraph containing more than one `GAP:` line is a structure violation.

**## Links ledger** — One line per unique cited source:
`<short name> | <citation or UNCITED_NOT_USABLE> | QUARANTINED_PENDING_LOCAL_CHECK`
**[r3-D4]** Bidirectional and unique, checked over source indices (resolved citation identifiers ∪ inline literal IDs): every citation appearing inline in Sections 1–5 appears exactly once here, and every row here is cited at least once inline. The `<short name>` field must be non-empty and human-readable. Before uniqueness/bidirectionality, canonicalize arXiv `abs|html|pdf` variants (strip `vN`) to `/abs/<id>` and DOI/ADS to one canonical form. Landing-page variants of the same paper (e.g. `article` vs `article-abstract`) are flagged `NEAR_DUPLICATE` for manual reconciliation — never silently merged, never auto-failed. No duplicates, no orphan rows, no inline-only citations.

### r3.3 — Binding output contract (C1–C8)

**C1 (meta header).** The body's first lines are exactly:

    # Joint C1R answer — <REQ_ID>
    Run date (UTC): <YYYY-MM-DDTHH:MM:SSZ>
    Model: Gemini Pro (selected UI mode; backend version not exposed)
    Simulations covered: <N>

Emit the Model line verbatim as written above — do not substitute a version number or any other self-identification (a hallucinated version such as "1.5" is a defect). This 4-line meta header is the first content of the body.

**C2 (structure + empty-field device).** Exactly the five sections above in order, then the Links ledger. An empty field is exactly `NONE_FOUND` — never blank, never padded. **[r3-D5]** Every Section-5 GAP line is its own paragraph and carries a checkable citation OR the exact token `ASSERTED_ABSENCE_NOT_SYSTEMATICALLY_VERIFIED`; more than one `GAP:` line in a paragraph is a structure failure. The Section-4 missing-status token is exactly `NOT_REPORTED — NONE_FOUND`.

**C3 (uncertainty).** Every scientific quantitative value carries its source's uncertainty in the same line/cell, OR the same-line/cell label `UNCERTAINTY_NOT_QUOTED_BY_SOURCE`. Never invent error bars. EXEMPT (no token required): run timestamps, request IDs, citation identifiers/URLs (arXiv, DOI, ADS numbers), section numbers, the meta-header simulation count (the "Simulations covered: N" value), and project-name suffixes (for example FIRE-2, FIRE-1, TNG50).

**C4 (citation labeling).** Every calibration or validation statement carries, within the SAME logical unit (a single bullet, or the individual table cell that makes the claim), a checkable citation (arXiv ID, DOI, ADS bibcode, or URL) OR the same-unit label `UNCITED_NOT_USABLE`. A citation in one cell does NOT cover other cells: in a multi-cell Section-1 row, EVERY claim-bearing cell (calibration-targets, feedback-parameters, explicitly-emergent, notes) repeats its own checkable citation or `UNCITED_NOT_USABLE` — a citation in the Simulation cell or a dedicated Citation cell does not satisfy the other claim-bearing cells. Section 3 bullets and Section 4 `CALIBRATED`/`EMERGENT` cells follow the same same-unit rule. Empty citation cells are forbidden. **[r3-D3 — Section 2 exception]** For Section-2 rows only, the dedicated Citation cell is the single authoritative citation for the row and the Result cell is bound to it as one atomic validation record; the Result cell is not independently citation-gated, but the dedicated Citation cell must be non-empty and checkable.

**C5 (wording contract).** In your own voice the following settled/causal register is BANNED (case-insensitive): establish, establishes, established, establishing, proves, proven, confirms that, settles, settled question, resolves the debate, definitively, conclusively, is now known, "demonstrates that … causes". A source's own claim in that register may appear ONLY as an explicit attributed quote with a checkable citation. Before finalizing, perform an INTERNAL LITERAL SELF-AUDIT: scan your own draft for each banned term above and remove or re-attribute every own-voice occurrence. Do not output the audit.

**C6 (estimand / commensurability).** Each Section-2 ROW has its dedicated COMPARABILITY cell containing exactly one token — `MATCHED_SELECTIONS` or `NON_COMMENSURABLE_UNMATCHED_SELECTIONS` — and nothing else in that cell. **[r3-D2]** Any quoted numeric fraction or incidence (a fraction/percentage/ratio/incidence with a numeric value), anywhere in the body, carries the four qualifiers in exactly this syntax within the same line/cell: `TRACER=<...>; SELECTION=<...>; DENOMINATOR=<...>; REDSHIFT=<...>`, using `NOT_APPLICABLE` for any qualifier that does not apply. A tuned model/parameter fraction fills it exactly as `TRACER=MODEL_PARAMETER; SELECTION=NOT_APPLICABLE; DENOMINATOR=<coupled quantity>; REDSHIFT=NOT_APPLICABLE`. A fraction/incidence *word* with no quoted numeric value is not gated. **[r3-D1]** A simulation–observation comparison is an agreement/tension result claim (a simulation's output stated to agree with, match, reproduce, or be in tension/discrepancy/offset with an observation) and belongs in Section 2. Outside Section 2, any `Explicitly emergent`/`Notes` result-claim cell, Section-3 bullet, or Section-5 GAP line making such a claim must contain exactly one of `MATCHED_SELECTIONS` or `NON_COMMENSURABLE_UNMATCHED_SELECTIONS` in the same unit; Section-1 calibration-target descriptions prefixed `CALIBRATION_TARGET_DESCRIPTION:` are exempt. Label honestly; the semantic correctness of these labels is checked later by human review.

**C7 (links ledger — bidirectional, unique, quarantined).** **[r3-D4]** Checked over source indices, not raw URL strings. Every inline citation appears in the Links ledger; every ledger row is cited inline at least once; each ledger row is unique after normalization (arXiv `abs|html|pdf` with `vN` stripped, DOI/ADS canonicalized); each `<short name>` field is non-empty; landing-page variants of the same paper are flagged `NEAR_DUPLICATE` for manual reconciliation; each ledger row ends with `QUARANTINED_PENDING_LOCAL_CHECK`. No orphan rows, no inline-only citations, no duplicates.

**C8 (completion marker).** The exact string `<COMPLETION_MARKER>` appears exactly once, as the standalone final non-empty line of the body. Nothing may follow it — no "End of Report", no sign-off, no blank-line-then-text. A marker present only in a chat-UI completion element and not in the body counts as ABSENT and the run is rejected.

### r3.4 — Silent preflight (perform before emitting; DO NOT output any of it)

Verify: (1) the body sequence is exactly meta header → five sections → Links ledger → final marker line, with no content outside allowed units; (2) the Model line is exactly `Model: Gemini Pro (selected UI mode; backend version not exposed)`; (3) every empty field is `NONE_FOUND`, and every GAP line — one per paragraph (D5) — is cited or `ASSERTED_ABSENCE_NOT_SYSTEMATICALLY_VERIFIED`; (4) every scientific number has an uncertainty or `UNCERTAINTY_NOT_QUOTED_BY_SOURCE`, with the C3 exemptions (including the meta-header simulation count) respected; (5) every claim-bearing cell carries its own citation or `UNCITED_NOT_USABLE` and no citation cell is empty — except Section 2, where the dedicated Citation cell is authoritative for the row and the Result cell is not independently gated (D3); (6) the C5 literal self-audit passed; (7) every Section-2 row's COMPARABILITY cell holds exactly one token, every out-of-Section-2 emergent/notes/bullet/GAP agreement-tension comparison carries one of the two tokens in the same unit while `CALIBRATION_TARGET_DESCRIPTION:` calibration cells are exempt (D1), every Section-4 cell is `CALIBRATED`/`EMERGENT` (with a same-cell citation) or exactly `NOT_REPORTED — NONE_FOUND`, and every quoted numeric fraction uses `TRACER=<...>; SELECTION=<...>; DENOMINATOR=<...>; REDSHIFT=<...>` with the `MODEL_PARAMETER` fill where applicable (D2); (8) the Links ledger is index-bidirectional, unique after normalization, every short name non-empty, near-duplicates flagged, and every row ends `QUARANTINED_PENDING_LOCAL_CHECK` (D4); (9) the marker appears exactly once as the final non-empty line. If any check fails, fix it silently, then emit only the final report.

### r3.5 — Safety locks

- Output is advisory only. Not accepted evidence, not product-claim binding.
- Do not present generated DOI/ADS/arXiv IDs as verified; all IDs are quarantined pending local check.
- Do not propose edits to any local artifact; produce this report body only.

### r3.6 — Final reminder

The last non-empty line of your report must be exactly `<COMPLETION_MARKER>` with no text after it.

---

## 8. Consolidated fail-closed impact register

| D | Relaxes a gate? | Preserved guard / replacement |
|---|---|---|
| D1 | No | Token still required for every emergent/notes/GAP/bullet agreement-tension claim; exemption limited to col1/col2 `CALIBRATION_TARGET_DESCRIPTION` register; result claims cannot use the marker to escape. |
| D2 | No | Universal fraction rule retained; tuned parameters labeled via `TRACER=MODEL_PARAMETER`, not exempted; SIMBA ~10% still fails without syntax. |
| **D3** | **YES** | Every S2 row must carry one authoritative, non-empty, resolvable citation in the dedicated Citation cell, bound to the Result cell; empty citation cell is still a hard FAIL; citation stays quarantined; source support is later manual `VERIFY_SOURCE_FIDELITY`. No validation claim becomes uncited. |
| D4 | No | Strictly tightens C7. |
| D5 | No | Strictly tightens C2/S5; removes the merged-block loophole. |

**D3 is the sole `FAIL_CLOSED_IMPACT: YES` item** and must be surfaced verbatim to Hwao (`HWAO_R3_REVIEW.md`) and, if accepted, to Duho in the final recommendation.

---

## 9. Deterministic crosswalk (per Amendment A3 — not the manual queue)

Each r3 D-item resolves **deterministic FAIL findings** that live in the 17-finding residue (`readjudication/validator_result_v2.json` / `RESIDUE_REPORT.md`). **These deterministic findings are NOT members of the 73-entry manual queue and must NOT appear in `triage/TRIAGE_LEDGER.*`** (exactly-73 source-order custody stands; stop condition 2 unchanged). In particular, the eight Section-2 Result-cell findings that D3 re-types **remain outside the manual ledger** — the earlier note that called them "triage entries" is withdrawn.

Deterministic crosswalk (D-item ↔ the residue finding it resolves, referenced by FAIL identity, not by manual-queue index):

| D-item | Deterministic finding(s) resolved | Identity in residue |
|---|---|---|
| **D1** | the **6 `UNLABELED_COMPARISON`** findings (5 Section-1 `Explicitly emergent` cells + GAP1; FLAMINGO included per T14 Rule A) | C6 `UNLABELED_COMPARISON`, anchored cells |
| **D2** | the **1 SIMBA ~10% `MISSING_QUALIFIER`** finding (tuned accretion fraction) | C6 `MISSING_QUALIFIER`, SIMBA feedback-params cell |
| **D3** | the **8 Section-2 Result-cell `UNCITED_CELL_CLAIM`** failures (rows 15–22) | C4 `UNCITED_CELL_CLAIM`, Section-2 Result cells |
| **D4** | the **1 C7 integrity** finding (12 orphan indices + 9 duplicate rows + 46 blank short names + 14↔29 near-duplicate) | C7 integrity clause |
| **D5** | the **GAP-granularity history** (merged single-`<p>` four-GAP block → per-`gap_line` split; C2/GAP per-unit evaluation) | C2/S5 GAP structure |

Per Amendment A3/A1, the P2 requirement "cross-map for each `CONTRACT_R3_CHANGE` entry" applies only to **manual** entries actually classified into that lane — which may be none. No entry is classified in this file; P2 classification is `triage/TRIAGE_LEDGER.*`, pinned against the Goru-extracted queue and reconciled to exactly 73.

LANA_CONTRACT_R3_DRAFT_DONE_20260713T024458Z
