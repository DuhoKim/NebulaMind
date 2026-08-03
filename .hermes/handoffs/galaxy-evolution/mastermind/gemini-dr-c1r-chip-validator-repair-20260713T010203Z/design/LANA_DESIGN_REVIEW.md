# LANA_DESIGN_REVIEW — C1r chip-aware capture + validator (v2)

Packet: `gemini-dr-c1r-chip-validator-repair-20260713T010203Z`
Role: design reviewer (high reasoning), no implementation. This document is the buildable spec Tori implements against Goru's RED tests, under Kun's custody gate. It enforces the **immutable** contract `../gemini-dr-revised-canary-20260712T045317Z/prompt/C1r.md` (C1–C8) literally and fail-closed. It does **not** amend the contract (that is R4/contract-r3, out of packet scope); genuine contract awkwardness is enforced as written and annotated for the manual queue.

Inputs read (read-only, sealed/immutable): `HWAO_IMPLEMENTATION_DIRECTION.md`, `ROLE_TABLE.md`, `prompt/C1r.md`, sealed `validator/structured_capture.js`, `validator/validator.py`, `validator/contract_spec.json`, `dr-c1r-root-cause-20260712T163156Z/TORI_ROOT_CAUSE_CORRECTED.md`, `HWAO_ROOT_CAUSE.md`. Line refs below are to those sealed files.

Scope locks affirmed: local/offline; packet-only writes; sealed inputs byte-immutable; no browser/network/live-Gemini/DB/wiki/product/deploy/restart/git/cron/dashboard/public-cockpit action. No approval phrase minted here.

---

## 0. Design invariants (apply to every clause below)

1. **Representation before judgement.** Every clause reads the v2 capture's typed fields (`role`, `chips`, `resolved_citations`, `cited`, `claim_bearing`), never re-parses raw HTML or re-derives cell meaning from keywords/word-counts.
2. **Same-logical-unit scoping is absolute** (C1r.md:86-92). A citation/chip counts for a claim only if it lives in the **same** cell / bullet / GAP line as the claim. Row-level link aggregation is banned (this was the v1 leak: `structured_capture.js:105` `links: cells.flatMap(...)`).
3. **Fail closed, never silent.** Any unresolved chip, index→URL conflict, or count mismatch versus `EXPECTED_DOM_FACTS.json` produces an explicit flag/finding or a STOP — never an empty field silently treated as "clean."
4. **One defect → one finding.** A malformed unit is charged to exactly one clause (e.g. `NONE_FOUND.` is a sentinel-format defect, not additionally an uncited-claim defect). No double counting.
5. **No weakened assertions.** If observed behavior deviates from the pins in §8, STOP per HWAO_IMPLEMENTATION_DIRECTION §7 and adjudicate; do not edit the pin or loosen a test.
6. **Mechanical ≠ scientific.** Deterministic PASS/FAIL covers structure/representation/syntax only. Semantic comparability, uncertainty correctness, citation quality, and source fidelity are `MANUAL_REVIEW_REQUIRED` only (§7).

---

## 1. Capture schema v2 — per-logical-unit native citation extraction + fail-closed index→URL map

File: `capture/structured_capture_v2.js` (starts as a byte-copy of the sealed `structured_capture.js`; original never edited). Output schema string: **`NM_GEMINI_RENDERED_DOM_V2`**.

### 1.1 Native chip extraction (fixes RC-1)

Gemini inline citations are text-empty, href-less chips: `<source-footnote><sup class="superscript" data-turn-source-index="N">`. Add a chip serializer alongside the existing anchor serializer (keep `linksFor` for literal `<a href>`; do **not** remove it — the ledger's 46 anchors still matter):

```
function chipsFor(element):
  return Array.from(element.querySelectorAll('sup[data-turn-source-index]'))
    .map(sup => parseInt(sup.getAttribute('data-turn-source-index'), 10))
    .filter(Number.isInteger)          // preserve DOM order; do NOT sort, do NOT dedupe here
```

Chip extraction is applied **per cell** (inside the `th,td` map) and **per non-table unit** (heading/bullet/paragraph/gap_line), so attribution is exactly per logical unit — never rolled up to the row.

### 1.2 Block schema (`BlockV2`)

```
{
  id: string,                 // "table_row_14", "bullet_25", "gap_line_2", "heading_3"
  type: "heading"|"table_header"|"table_row"|"bullet"|"paragraph"|"gap_line",
  section: string|null,       // exact SECTION_NAMES value, carried forward (unchanged from v1)
  text: string,               // cleanText(innerText); tab-joined for rows (unchanged)
  source_lines: [int],        // from makeLineLocator (see 1.5)
  links: [{url:string}],      // literal <a href> only, THIS unit only
  chips: [int],               // data-turn-source-index on THIS unit (non-table units)
  resolved_citations: [{index:int, url:string}],  // chips resolved via chip_urls (unit-level)
  unresolved_chips: [int],    // chips with no chip_urls entry -> fail-closed marker
  gap_index: int|null,        // 1-based ordinal within the S5 GAP paragraph; null otherwise
  cells: [CellV2]             // present iff type in {table_row, table_header}
}
```

### 1.3 Cell schema (`CellV2`) — typed, not guessed

```
{
  col: int,                   // 0-based column position within the row
  role: string,               // from spec section_columns map (see 3.1); e.g. "result","emergent","citation"
  text: string,               // cleanText(cell.innerText)
  links: [{url:string}],      // literal <a href> in THIS cell only
  chips: [int],               // data-turn-source-index in THIS cell only
  resolved_citations: [{index:int, url:string}],
  unresolved_chips: [int],
  claim_bearing: bool,        // from schema role + text (see 3.2) — NO keyword/word-count logic
  cited: bool                 // same-cell citation present? (see 2.2)
}
```

### 1.4 Top-level capture object + fail-closed chip→URL map (fixes RC-4 evidence, satisfies T2)

```
{
  schema: "NM_GEMINI_RENDERED_DOM_V2",
  innertext: string,
  blocks: [BlockV2],
  chip_urls: { "<index>": "<url>" },        // deterministic index -> canonical URL
  chip_index_occurrences: { "<index>": int },// ledger occurrence count per index (for C7 duplicates)
  chip_map_status: "OK" | "FAIL_CLOSED",
  chip_map_conflicts: [{index:int, urls:[string]}],   // non-empty <=> FAIL_CLOSED
  capture_flags: [string]                   // e.g. "UNRESOLVED_CHIP:table_row_18:cell2"
}
```

**Map construction (Links-ledger region only):** iterate blocks with `section == "Links ledger"`. Each ledger line pairs one chip index `N` with exactly one anchor URL (the row's `<a href>`). For each pair set `chip_urls[N]=norm(url)` (norm = §6.3) and increment `chip_index_occurrences[N]`.

**Fail-closed rule (T2):** if index `N` is seen with two **different** normalized URLs, append `{index:N, urls:[...]}` to `chip_map_conflicts` and set `chip_map_status="FAIL_CLOSED"`. The capture returns the object with the flag set — it never guesses a winner and never drops the index silently.
- On the **real** sealed HTML: expected `chip_map_status="OK"`, 46 (index→URL) pairs, 37 unique indices 1–37, `chip_map_conflicts == []`. A conflict here is HWAO §7 STOP #2 — do not proceed.
- On the **deliberately corrupted** fixture (same index → two URLs): expected `chip_map_status="FAIL_CLOSED"` with the conflict listed. That is the T2 positive assertion.

**Per-unit resolution:** for every cell/unit, resolve each chip `N`: if `N` in `chip_urls` → push `{index:N, url}` to `resolved_citations`; else push `N` to `unresolved_chips` and append a `capture_flags` entry. An unresolved chip **never** counts as a citation and **never** collapses to a silent empty cell (T3).

### 1.5 Locator, dedup, GAP split (feeds T4/T5/T6) — see §5 for GAP, §1.6 for dedup.

### 1.6 li+p dedup (fixes the §3-bullet double capture; T4)

Gemini renders each S3 bullet as `<li>` with a nested `<p>` twin. v1's `SEMANTIC_SELECTOR = 'h1..h6,p,li,table'` captures both. Rule: when a `<p>` is a descendant of an `<li>` (`element.closest('li')` is non-null and the `li` is itself captured), **skip the `<p>`** (mirror the existing `closest('table')` skip at `structured_capture.js:73`). Result: exactly 3 S3 `bullet` units, zero paragraph twins.

**Stop conditions (capture):** `chip_map_status=="FAIL_CLOSED"` on real HTML ⇒ STOP; any region chip total ≠ `EXPECTED_DOM_FACTS.json` (108 total; S1 40 / S2 8 / S3 3 / S4 9 / S5 2 / ledger 46; anchors 46 all in ledger, 0 inside any `<td>`) ⇒ STOP (custody/representation mismatch).

---

## 2. Literal same-cell citation semantics (C1r.md:86-92)

### 2.1 Coverage rule (the crux)

C1r.md:86-92: "a citation in the Simulation cell or a dedicated Citation cell does not satisfy the other claim-bearing cells." Therefore:

- **`role == "simulation"`** (S1 col0, S2 col0, S4 col0): citation/chip here is **coverage-excluded** — it never marks any other cell `cited`.
- **`role == "citation"`** (S2 col5, the dedicated Citation column): coverage-excluded for the Result cell. It may itself be recorded as a resolved citation unit (T3), but it does **not** set `result.cited=true`.
- A claim cell is `cited` **only** from citations/chips physically inside **that same cell**.

The v1 defect that this kills: `structured_capture.js:105` flattened all row anchors into `block.links`, and even a per-cell reading would have been defeated because the dedicated Citation cell would "cover" the Result cell. v2 forbids both by construction (no row-level aggregation; coverage-excluded roles).

### 2.2 `cited` determination (per claim-bearing unit)

`cited == true` iff, **within the same unit**, any of:
1. `resolved_citations` non-empty (a same-cell chip resolved to a URL) — the pre-declared representation rule ("a link attached to the same logical DOM cell counts as a checkable same-cell citation"), or
2. a literal checkable citation string in `text` — arXiv ID / DOI / ADS bibcode / URL. Regex set:
   - arXiv: `\barXiv:\d{4}\.\d{4,5}(v\d+)?\b` or `\b\d{4}\.\d{4,5}(v\d+)?\b` inside an arxiv URL, DOI: `\b10\.\d{4,9}/[-._;()/:A-Za-z0-9]+\b`, ADS bibcode: `\b\d{4}[A-Za-z][A-Za-z0-9.&]{14,}\b`, URL: `https?://[^\s\]]+`.

`UNCITED_NOT_USABLE` present in the unit ⇒ **not** `cited`, but **contract-compliant** (the honest-uncited device) ⇒ routed to MANUAL (`UNCITED_DECLARED_NOT_USABLE`), never FAIL.

Outcome table (per claim-bearing unit, C4):
| condition | status | code |
|---|---|---|
| `cited` (chip-resolved or literal) | MANUAL_REVIEW_REQUIRED | `CITED_CELL_CLAIM_REVIEW` |
| `UNCITED_NOT_USABLE` present | MANUAL_REVIEW_REQUIRED | `UNCITED_DECLARED_NOT_USABLE` |
| not cited, no token, has `unresolved_chips` | FAIL | `UNRESOLVED_CITATION` (fail-closed) |
| not cited, no token, no chips | FAIL | `UNCITED_CELL_CLAIM` (cells) / `UNCITED_CLAIM` (bullets/gap) |

On sealed data this yields: all 32 S1 claim cells → MANUAL (chip-resolved); all 3 S3 bullets → MANUAL; all 9 S4 CALIBRATED/EMERGENT → MANUAL; 8 S2 Result cells → **FAIL `UNCITED_CELL_CLAIM`** (rows 15–22; chip-free, no literal cite, no token). The 8 S2 dedicated Citation cells resolve as citation units but do **not** rescue the Result cells.

---

## 3. Typed claim-bearing cells for C4 (no keyword/word-count guards) — fixes RC-2/validator lottery

### 3.1 Section-column role map (lives in `validator/contract_spec_v2.json`, data-driven)

```
"section_columns": {
  "1. Calibration ledger":                 ["simulation","calibration_target","feedback_params","emergent","notes"],
  "2. Out-of-sample validation ledger":    ["simulation","observable","result","comparability","overlap","citation"],
  "4. Feedback-relevant observables map":  ["simulation","quenched_fractions","gas_fractions","outflow_demographics","hot_halo_cavity","radio_agn_incidence"]
}
```
Capture assigns `cell.role = section_columns[section][col]` (S3 units → role `bullet`; S5 units → role `gap_line`). If a row's cell count ≠ the mapped length ⇒ fail-closed capture flag + STOP (structural drift; do not silently mis-role).

### 3.2 `claim_bearing` predicate (schema + sentinel state only)

```
claim_bearing(role, text, section):
  S1: role in {calibration_target, feedback_params, emergent, notes} AND not is_empty_sentinel(text)
  S2: role == result                                  # dedicated citation col is NOT claim-bearing-for-coverage
  S4: role in {quenched_fractions,gas_fractions,outflow_demographics,hot_halo_cavity,radio_agn_incidence}
        AND status_of(text) in {CALIBRATED, EMERGENT}  # NOT_REPORTED—NONE_FOUND is not claim-bearing
  bullet:   True
  gap_line: True   (citation-or-token rule, see §5)
  else: False
```
`is_empty_sentinel(text)` = text is the empty device (starts with `NONE_FOUND`). Malformed sentinel (`NONE_FOUND.`) is handled once by §5.1 and is **exempt** from C4 (invariant 4 — no double count). `status_of` reads the leading token of an S4 cell.

Explicitly banned in C4: `len(text.split()) > 3` gating (v1:141), `re.search(calibrated|validation|tuned|...)` cell gating (v1:139), and skipping `bullet` blocks (v1:121). These are the exact causes of the 6 false-negatived S2 Result cells (rows 15–20) and the un-scanned bullets/S4 cells; the typed predicate removes all of them.

---

## 4. Per-cell C6 comparison detection + numeric fraction/incidence gate — fixes RC-2(b)/RC-3(a)

### 4.1 Comparability token on the S2 dedicated cell (unchanged intent, typed anchor)

For each `table_row` in section 2: read `cells[col where role=="comparability"]` (col 3). Must equal exactly one of `{MATCHED_SELECTIONS, NON_COMMENSURABLE_UNMATCHED_SELECTIONS}` (nothing else in the cell). Else FAIL `MISSING_COMPARABILITY` anchored `[block_id, 3]`; if valid ⇒ MANUAL `COMPARISON_LABEL_REVIEW` (semantic correctness is human-checked, §7).

### 4.2 Comparison-outside-Section-2 (per-cell, typed; fixes the 5 S1 + GAP1 anchoring)

Scan runs **per claim cell / per gap_line**, never on tab-joined row text. It applies to roles in `comparison_token_roles = {emergent, gap_line, external_bullet}` and is **exempt** for `comparison_exempt_roles = {calibration_target, feedback_params}` and for all of section 2 (that is the designated comparison section).

A unit is a **comparison claim** iff its own text matches all three:
- a simulation/suite reference: `simulation_pattern` (spec; the v1 pattern is fine),
- an observation reference: `\b(observed|observations?|observational|survey|empirical|data)\b`,
- a **result-level agreement/tension verb**: `\b(agrees?|agreement|matches?|reproduces?|consistent|tension|discrepan\w+|offset|over-?predicts?|under-?predicts?)\b`.

If comparison claim AND no `MATCHED_SELECTIONS`/`NON_COMMENSURABLE_UNMATCHED_SELECTIONS` in the **same** unit ⇒ FAIL `UNLABELED_COMPARISON` anchored to the cell (e.g. `[block_id, 3]` for S1 emergent). If the token is present ⇒ MANUAL `COMPARISON_LABEL_REVIEW`.

Register distinction (the "calibration-target in cell 1 alone does not require the token" rule): the exemption is **by role**, not by prose. An S1 `calibration_target` (col1) cell that says "tuned to reproduce the observed X" is calibration description ⇒ exempt. An S1 `emergent` (col3) cell that asserts the simulation agrees with an observation ⇒ subject to the token. This deterministically yields findings on rows 6/7/10/11/12 emergent cells and none on rows 5/8/9 (which carry no agreement claim), matching the pin.

### 4.3 Numeric fraction/incidence gate (fixes the 3 false positives; T8)

The four-qualifier rule fires **only when a quoted numeric fraction/incidence value is present in the same unit** — not on the bare word. Gate:

```
has_numeric_fraction(text):
  # a numeric value in fraction/percentage/incidence context, same unit
  return bool(re.search(r'\b\d+(\.\d+)?\s?%', text))                       # 23%, 23 %
      or bool(re.search(r'\b\d+\s?(per ?cent|percent)\b', text, re.I))     # 23 per cent
      or bool(re.search(r'\b\d+\s?/\s?\d+\b', text))                       # 1/5
      or bool(re.search(r'\b(fraction|incidence)\b[^.]{0,40}?\b\d+(\.\d+)?\b', text, re.I))
      or bool(re.search(r'\b\d+(\.\d+)?\b[^.]{0,40}?\b(fraction|incidence)\b', text, re.I))
```

Only if `has_numeric_fraction(text)` do we require the exact syntax
`TRACER=<...>; SELECTION=<...>; DENOMINATOR=<...>; REDSHIFT=<...>` (v1 regex at validator.py:207-211 is correct; keep it). Present ⇒ MANUAL `SEMANTIC_QUALIFIER`; absent ⇒ FAIL `MISSING_QUALIFIER`.

This removes: row 6 "fraction of available Type II Supernovae energy" (no numeric), rows 21/22 "cluster gas fractions" (observable name, no numeric) ⇒ **no finding**. It keeps genuine quoted fractions (the 6 four-qualifier uses in the sealed body ⇒ MANUAL).

---

## 5. Exact sentinels + GAP unit splitting

### 5.1 Exact sentinels (T11)

Tokens (in `contract_spec_v2.json.sentinels`): empty_field `NONE_FOUND`; S4 not-reported composite `NOT_REPORTED — NONE_FOUND` (em dash U+2014); GAP absence `ASSERTED_ABSENCE_NOT_SYSTEMATICALLY_VERIFIED`.

- Any cell whose stripped text **starts with** `NONE_FOUND` but is **not exactly** `NONE_FOUND` (e.g. `NONE_FOUND.`) ⇒ FAIL `SENTINEL_FORMAT_DEFECT` (clause C2), anchored `[block_id, col]`. Exactly `NONE_FOUND` ⇒ pass, and the cell is treated as the allowed empty device (not claim-bearing). This catches the FIRE feedback-parameter `NONE_FOUND.` as exactly one finding.
- S4 non-status cell: if `text.startswith("NOT_REPORTED")` and `"NONE_FOUND" not in text` ⇒ FAIL `MISSING_NONE_FOUND` (keep v1 intent, exact composite).
- `NONE_FOUND` (exact) ⇒ never a C4 finding (invariant 4).

### 5.2 GAP unit splitting (fixes the merged `<p>`; T5)

The four S5 GAP lines render as spans inside a single `<p data-path-to-node="11">`. Split into independent `gap_line` units:
- Within the S5 paragraph, split `innerText` into lines; each line beginning `GAP:` starts a new `gap_line` unit with `gap_index` = 1..4 in document order.
- Attribute chips by DOM/source order: a chip belongs to the `gap_line` whose text-range (from its `GAP:` start to the next `GAP:` start) contains the chip's position. Per Goru's offsets: GAP1→chip 30, GAP2→token, GAP3→chip 36, GAP4→token.
- Each `gap_line` is then evaluated independently: citation-or-token (§ C2/C4). GAP1/GAP3 satisfied by resolved chip; GAP2/GAP4 satisfied by the absence token. All four pass the GAP citation rule (T9). GAP1 additionally trips §4.2 `UNLABELED_COMPARISON` (predictive-failure comparison, no token); GAP2/GAP4 do not (T10).

C2 GAP check (v1:66-69) runs **per gap_line**, not per merged block, so GAP2/GAP4's token can no longer satisfy GAP1/GAP3.

### 5.3 Order/empty decoupling (T7) — kill BAD_STRUCTURE double-count

`c2_order_ok` (section presence + heading order) must be computed **independently** of empty-cell / GAP / sentinel findings. Remove the v1 coupling at validator.py:57,64,69 (`c2_order_ok = False` on empty/sentinel/GAP). Emit:
- `STRUCTURE_ORDER_BAD` (FAIL) **only** when a section is missing or headings are out of order, with concrete evidence (the offending heading text/ids) — never the literal `set()` string (v1:72).
- Empty-cell (`EMPTY_TABLE_CELL`), sentinel, and GAP findings are their own clause-C2 findings and do **not** flip structure.
- A cell is "empty" for `EMPTY_TABLE_CELL` iff `text==""` AND `chips==[]` AND `links==[]` AND not an S4 status cell placeholder. The 8 S2 Citation cells have chips ⇒ **not empty** ⇒ zero `EMPTY_TABLE_CELL` on sealed data (removes 8 capture false positives). Perfect order + empty cells ⇒ `STRUCTURE_OK`.

---

## 6. C7 — bidirectionality, duplicates, blank names, normalization, near-duplicates (T12)

C7 operates over **resolved chip indices ∪ inline literal URLs**, not a URL set (fixes v1:247-272 which set-flattened and ignored chips).

### 6.1 Bidirectionality (indices)
- `body_indices` = { every chip index appearing (resolved) in any Section 1–5 unit } ∪ { indices whose ledger URL appears as an inline literal URL in body }.
- `ledger_indices` = keys of `chip_urls` (1–37).
- **Orphan ledger sources** = `ledger_indices - body_indices` ⇒ FAIL `C7_ORPHAN_LEDGER_SOURCE`, evidence = sorted list. Pin: `{2,5,8,9,13,16,18,23,24,29,31,33}` (12).
- **Inline-only** = `body_indices - ledger_indices` ⇒ FAIL `C7_INLINE_ONLY` (pin: empty on sealed data).

### 6.2 Duplicate rows + blank short names
- Ledger row line format (C1r.md:59): `<short name> | <citation or UNCITED_NOT_USABLE> | QUARANTINED_PENDING_LOCAL_CHECK`.
- **Duplicate rows**: any normalized ledger URL with `chip_index_occurrences > 1` (46 rows / 37 unique) ⇒ FAIL `C7_DUPLICATE_ROW`, evidence = the 9 duplicated URLs. Pin: 9 duplicate rows.
- **Blank short name**: a ledger row whose first pipe-field (before the first ` | `) is empty (the chip occupies the slot; innerText begins `" | https://…"`) ⇒ FAIL `C7_BLANK_SHORT_NAME`. Pin: 46 blank names.

### 6.3 Normalization + near-duplicate flag
```
def norm(u):
  u = u.strip().strip(".,;:)'\"")
  u = re.sub(r'(arxiv\.org)/(?:abs|html|pdf)/(\d+\.\d+)(?:v\d+)?', r'\1/abs/\2', u)   # add pdf (v1 missed it)
  return u
```
- `abs|html|pdf` variants of the same arXiv id unify to `/abs/<id>` (strip `vN`).
- **Near-duplicate** (`article` vs `article-abstract`): a normalizer-invisible variant. Detect from `near_duplicate_path_pairs=[["article","article-abstract"]]`: two ledger indices whose URLs are identical except one path segment is `article/` and the other `article-abstract/` (or the same DOI landing vs abstract page) ⇒ FLAG `C7_NEAR_DUPLICATE` (indices 14↔29 on sealed data). This is a **flag** (distinct finding), not merged into `norm`, not counted as an exact duplicate — it is surfaced for review so nothing is silently collapsed.

C7 clause verdict: FAIL if any of the above findings exist. The one C7 clause failure "covers" the 12 orphans + 9 duplicate rows + 46 blank names + the 14↔29 near-dup flag (each enumerated in evidence). Overall it is the single genuine C7 clause failure the corrected root-cause requires.

---

## 7. Manual-review boundary + expected T14 residue

### 7.1 Manual-only families (T13; never auto PASS/FAIL)
- **Semantic comparability** — whether `MATCHED_SELECTIONS`/`NON_COMMENSURABLE...` labels are semantically correct (all 8 S2 rows say `MATCHED_SELECTIONS`; FLAMINGO kSZ-stacking doubtful) ⇒ MANUAL.
- **Uncertainty (C3)** — a present `±`/`UNCERTAINTY_NOT_QUOTED_BY_SOURCE` token ⇒ MANUAL `UNCERTAINTY_CHECK` (human checks correctness); only a **bare quantity with no token and no exemption** is FAIL `BARE_QUANTITY`. C3 evaluated per value/cell (not per merged row) so one token cannot cover a different cell.
- **Citation quality** — resolved chips pointing at aggregators (chip 27 → OpenAIRE) or a shared/likely-miscited source (chip 30 shared by FLAMINGO+BAHAMAS) ⇒ MANUAL.
- **Source fidelity** — do the papers actually support the claim ⇒ MANUAL.

The `readjudication/RESIDUE_REPORT.md` must state the result is **mechanical only and does not certify science or source fidelity**, must carry no retro-acceptance language, and must record C1r as remaining FAIL_CLOSED (governance unchanged: HWAO_ROOT_CAUSE R0).

### 7.2 Pinned deterministic T14 residue (from immutable sealed C1r capture)

Deterministic FAIL set (must reproduce exactly; any deviation ⇒ STOP, §8):
| clause | count | code | anchor |
|---|---:|---|---|
| C4 | 8 | `UNCITED_CELL_CLAIM` | S2 Result cells, rows 15–22 (cell col 2) |
| C6 | 6 | `UNLABELED_COMPARISON` | 5 × S1 emergent cells (rows 6/7/10/11/12, col 3) + GAP1 |
| C7 | 1 (clause) | `C7_ORPHAN_LEDGER_SOURCE` (+`C7_DUPLICATE_ROW`,`C7_BLANK_SHORT_NAME`,`C7_NEAR_DUPLICATE` evidence) | ledger: 12 orphans + 9 dup rows + 46 blank names + 14↔29 |
| C2 | 1 | `SENTINEL_FORMAT_DEFECT` | FIRE feedback-params cell `NONE_FOUND.` |

= **15 genuine mechanical findings + 1 sentinel defect.** PASS: C1, C5, C8 (and C2 `STRUCTURE_OK`). MANUAL: comparability labels, uncertainty tokens, cited-claim reviews, citation quality.

Required **absences** (regression guards — their presence ⇒ STOP, do not weaken):
- the 41 capture-caused findings (8 `EMPTY_TABLE_CELL` + 31 S1 `UNCITED_CELL_CLAIM` + 2 paragraph `UNCITED_CLAIM`);
- the 3 `MISSING_QUALIFIER` false positives;
- `BAD_STRUCTURE`.

---

## 8. Stop conditions Tori implements verbatim (no guessing)

1. Sealed-input sha256 ≠ RUN_RECEIPT custody at any phase (T0) ⇒ STOP.
2. `chip_map_status=="FAIL_CLOSED"` on the **real** sealed HTML, or any chip→URL inconsistency there ⇒ STOP (the corrupted **fixture** failing closed is the expected T2 pass, not a stop).
3. Any region chip total or anchor placement ≠ `EXPECTED_DOM_FACTS.json` ⇒ STOP.
4. Any row whose cell count ≠ its `section_columns` length ⇒ fail-closed flag + STOP (mis-role risk).
5. Any `unresolved_chips` on a claim-bearing unit ⇒ finding `UNRESOLVED_CITATION` (fail-closed), never silent.
6. T14 residue deviates from §7.2 pin (extra, missing, or re-anchored finding) ⇒ STOP and adjudicate; never edit the pin, never loosen a RED assertion.
7. GREEN unreachable without weakening an assertion, or any write would land outside the packet root ⇒ STOP (HWAO §7.5/§7.6).
8. No git/deploy/restart/network/browser/live-Gemini action on success or failure (HWAO §7.4/§7.8).

---

## 9. Internal-consistency verdict (basis for LANA_SIGNOFF)

I traced T0→T15 against the C1–C8 contract, the sealed capture/validator behavior, the corrected root-cause adjudication, and the §7.2 pins:

- Capture (T1–T6) produces exactly the typed fields the validator clauses (T7–T13) consume; no clause re-parses HTML or re-guesses meaning. ✔
- Same-cell scoping (§2) + coverage-excluded roles (§3) deterministically produce the 8 S2 Result-cell C4 FAILs and route all chip-bearing S1/S3/S4 claim cells to MANUAL — matching T9 and the residue. ✔
- Per-cell C6 (§4.2) with role-based exemption yields exactly 5 S1 + GAP1, not rows 5/8/9, not S2 rows (already token-checked) — matching T10. The numeric gate (§4.3) removes exactly the 3 false positives — matching T8. ✔
- Sentinel (§5.1) charges `NONE_FOUND.` once and exempts it from C4; GAP split (§5.2) makes GAP1/GAP3 citation-satisfied and GAP1 comparison-unlabeled without GAP2/GAP4 leakage — matching T5/T11. ✔
- Order/empty decoupling (§5.3) removes `BAD_STRUCTURE` and the 8 `EMPTY_TABLE_CELL` (chips ⇒ non-empty) — matching T7 and the required absences. ✔
- C7 (§6) over indices with pdf normalization + near-dup flag reproduces the 12/9/46/(14↔29) evidence — matching T12. ✔
- Manual boundary (§7.1) never auto-resolves the four semantic families — matching T13; residue (§7.2) sums to 15 + sentinel with the pinned absences — matching T14; pure/sorted outputs give byte-identical reruns — matching T15. ✔
- No clause both passes and fails the same unit; a unit may legitimately be C4-MANUAL and C6-FAIL (different clauses) — not a contradiction. ✔

No internal contradiction found. The proposed T0–T15 contract is internally consistent. Known **contract-design** tensions (S2 provides a Citation column then rules it insufficient; C6 collides with calibration-target register) are enforced literally here and annotated for the manual queue / future contract-r3 pass (R4) — they are not defects in this test contract and do not block sign-off.

LANA_C1R_REPAIR_DESIGN_DONE_20260713T010203Z
