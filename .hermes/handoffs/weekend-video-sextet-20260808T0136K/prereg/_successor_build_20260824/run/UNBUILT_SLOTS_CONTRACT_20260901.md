# UNBUILT CLASS-P SLOTS — BUILD CONTRACT (Hwao's judgment; codex builds)

**Order (Duho, direct, 2026-09-01):** "build the unbuilt slots on codex
meanwhile." Produce receipt candidates for the Class-P slots that have no
candidate, from the FROZEN bytes, so the freeze-prerequisite stack is ready when
the Sep-5 BS-1 question resolves.

## Standing rules (every slot obeys)
- Candidates ONLY → `run/classp_candidates/<slot>.json`, through the FROZEN
  `v9.receipt()` (successor layer only for BS-3g, which is not in scope here).
- Every field is a real on-disk sha, a frozen-text value with its clause quoted,
  or a fresh v9-machinery run's digest+verdict. NEVER synthesize; if a field's
  value or design genuinely needs Duho, STOP-AND-BLOCKED for that slot with the
  exact missing thing named.
- NO imagery, NO image transport, NO χ measurement, NO live-store writes. v9
  read-only. Write each candidate AS it completes; write the report LAST so
  partial progress survives a session cut.
- Order the work light→heavy so the quick wins bank first.

## The slots, in build order

### 1. BS-2v — VOID conversion receipt (LIGHT: the tool exists)
`gates/bs2v_void_converter.py` is BUILT (build phase). Run it to produce the
canonical authenticated receipt over §7.1's closed antecedent registry, then
emit the BS-2v candidate through the frozen v9.receipt() with its schema fields
(read the frozen BS-2v row + v9 SLOT_SCHEMA if BS-2v is in it; if BS-2v is NOT
in v9's SLOT_SCHEMA, the receipt is the converter's own authenticated schema —
say which, quote the frozen "canonical authenticated receipt schema" clause).
Provenance per field.

### 2. BS-1b — Branch-B photo-z binding (LIGHT: branch is ruled)
Branch B (DR10.1) is RULED (BS1_EARLY_RESOLUTION_RULING). v9's
`BRANCH_CONFIG["B_DR10_1"]` carries the frozen paths (photoz_product
ls_dr10.photo_z, sweep_dir, bricks_product, band r, hdu 1). v9 SLOT_SCHEMA BS-1b
= (photoz_product, columns, join_keys, provenance). Fill from the frozen branch
config + the acquire/ join keys (ls_id/brickid/objid) + provenance (the query
ADQL + receipts). If the photo-z PRODUCT columns cannot be named without the
actual DR10.1 photo-z file on disk, STOP-AND-BLOCKED naming what's missing.

### 3. BS-8p — hand-check plan + allocation (MEDIUM)
v9 SLOT_SCHEMA BS-8p = (bin_algorithm, allocation, hc_rules_quotation, budget).
The allocation math is v9's `allocate_handcheck` at the frozen constants (3×9,
floors 10/30, budget HC_REAL_LABELS=500); hc_rules_quotation is V3-pred's HC-1H
rules carried by quotation (quote the frozen passage); bin_algorithm is the
frozen bin construction. Produce the plan candidate WITHOUT touching imagery or
real χ — the allocation runs on the cell-count STRUCTURE, and a real allocation
needs the realized stratum cells which come post-BS-6; if the real cell counts
don't exist pre-image, the candidate is the PLAN + algorithm + rules + budget
with the allocation as the frozen METHOD (say so), or STOP-AND-BLOCKED if the
frozen schema demands realized counts. Read the frozen BS-8p row to decide.

### 4. BS-2a — acceptance design (HEAVY: the frozen thresholds → code + receipt)
The frozen row: "acceptance design: the absolute, frozen thresholds
(flux_ivar_r > 8.40..., ...), gated as text AND code before any image byte."
The thresholds are frozen (acquire/quality_cut_receipt.json carries
flux_ivar_r_gt 8.4000532, psfsize_r_lt 1.5699703, nobs_r_ge; cross-check against
the frozen §-text's stated thresholds — quote them). Build the acceptance
CODE (a pure predicate over the frozen thresholds, fixtured: a row at/above/below
each threshold), and emit the BS-2a receipt through its frozen schema (read the
frozen BS-2a row; it may be a design receipt with the thresholds + code digest).
If BS-2a's frozen schema demands anything not derivable from the frozen
thresholds + the acquire receipts, STOP-AND-BLOCKED.

### 5. BS-9 — input-path rebinding + R1–R5 (HEAVY: branch-specific)
Frozen row: "branch-specific single-band HDU/plane schema, production input
function (code + hash + tensor layout), full R1–R5 rerun through it, gated
replacement runner." v9 SLOT_SCHEMA BS-9 = (hdu_schema, input_function_sha256,
tensor_layout, r1_r5_receipt, runner_prohibition). Branch B: single-band r, hdu
1 (from BRANCH_CONFIG). Build the production input function (the code that reads
a single-band HDU/plane into the instrument's tensor layout — WITHOUT any real
image; operate on the SCHEMA and a synthetic/fixture array of the declared
shape), run R1–R5 (v9 carries the R1–R5 machinery — run it fresh, receipt
digest+verdict), and emit BS-9 through its schema. If R1–R5 or the input
function genuinely need a real image plane to run, STOP-AND-BLOCKED naming it
(the point is the rebinding SCHEMA + function identity, not reading pixels).

## Report
`run/CODEX_UNBUILT_BUILD_20260901.md`: per-slot PRODUCED / STOP-AND-BLOCKED with
provenance or the exact missing thing; total candidates produced. End:
SEAT: CODEX
VERSION: UNBUILT-V1
VERDICT: <N>-PRODUCED-<M>-BLOCKED
COUNT: <candidates produced>
