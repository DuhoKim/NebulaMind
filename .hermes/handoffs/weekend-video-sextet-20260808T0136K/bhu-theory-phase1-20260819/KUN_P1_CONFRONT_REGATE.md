PASS_CONFRONTATION

Re-gate of KUN_P1_CONFRONT_GATE.md (HOLD_CONFRONT_SWEEP_FIGURES_MISLABELED), numbered
repairs only. Reviewer: Miru, second reviewer. Date: 2026-08-19. Findings-only; no file
other than this one written. Local files only; grep verification; one receipt spot-rerun
(python3). Scope per kickoff and per the gate's own regate convention: the three repaired
sentences plus the two caveat additions only; Checks 1-5 stand as passed and are not
re-litigated.

## Repair 1 (gate item 1, §1 sweep-orders figure): APPLIED as specified

- New phrasing grep-confirmed, line 23: "5×10⁵ (5.7 orders) at fiducial; 5.2–6.7 orders
  across the full (z_ta, C) sweep." — the gate's first sanctioned option, matching its
  independent recompute (5.22–6.73).
- Old mislabeled figure absent: grep for "5.2–6.4" / "5.2-6.4" returns nothing; the
  alternative re-scope "5.4–6.4" also absent (not the option taken; no hybrid left behind).

## Repair 2 (gate item 2, §1 sigma bracket): APPLIED as specified

- New phrasing grep-confirmed, lines 25-26: "(bracket 0.0025–0.08σ across the full
  (z_ta, C) sweep)" — the gate's second sanctioned option (single-sweep-consistent full
  sweep), matching the gate's F2 pairing.
- Old mixed-provenance bracket absent: grep for "0.005–0.08" / "0.005-0.08" returns
  nothing; no stray "0.005" or "0.048" anywhere in the document.

## Repair 3 (gate item 3, §3(b) stellar binding threshold): APPLIED as specified

- New phrasing grep-confirmed, line 66: "binding (below 1) for D ≲ 6×10³⁰ (stellar) /
  10²³ (supermassive) (R10 table)." — the recomputed crossover 6e30 (gate: 6.1e30);
  supermassive 10²³ stands, exactly as the repair permitted.
- Old threshold absent: the only "(stellar)" binding-threshold mention in the file is the
  repaired 6×10³⁰ form; no "1e30 (stellar)" remnant.

## No number changed anywhere else

Full-document read cross-checked against the gate's Check 1-3 confirmed record. Every
other number matches it exactly: §1 table (1.2/1.9/3.2 ×10⁻⁸ with brackets
[2.3,2.2]/[3.6,3.4]/[6.1,5.7] ×10⁻⁹/⁻⁸), C = 7.2 [1.4, 12.8], 16× tighter S1, 9.5×10⁻³
floor, 5×10⁵ (5.7 orders), 2.0×10¹², σ_A = 7.1×10⁻⁷, 0.027σ, 2.5×10¹⁶ ≈ 12,000
universes, 5.2×10⁻⁷ edge, 0.04× (0.037), [10⁻¹², 5×10⁻⁷], 1.4 orders, 18 → ~12,000;
§2: 5.7×10⁻⁸, 5.2 orders, 0.08σ; §3: 1.66×10⁻²⁷, 2.5×10³⁰ (ln 70), 2.5×10²², 1.2×10⁷,
z_eq = 3400, 2.2×10²³ / 2.2×10¹⁵, 27 / 18 e-folds, 10²²–10³⁰; §4 budget rows ×16,
×[0.19, 1.8], ×[0.49, 1.7]. Grep for stray old values ("6.4", "0.048", "0.005") returns
nothing.

Receipts untouched: bound_mapping_receipt.py (mtime 02:28:01) and inversion_receipt.py
(02:28:24) both predate the gate (02:53:29) and the doc revision (02:55:13).
Spot-rerun: `python3 receipts/bound_mapping_receipt.py` reproduces the gate's recorded
R9 output verbatim (fiducial A = 1.91e-8; z=1 1.221e-8 [2.3e-9, 2.2e-8]; z=10 3.226e-8
[6.1e-9, 5.7e-8]; 5.0e+05x short, 5.7 orders vs 9.5e-3; 0.027 sigma; strict/generous
0.037 vs 5.2e-7; N = 2.45e16 = 1.2e4 universes) — the revised doc's §1 numbers still
match the receipt.

## UNVERIFIED-AT-GATE caveats: BOTH PRESENT in §4 error budget

Lines 91-99, under an explicit "Gate-recorded caveats (UNVERIFIED-AT-GATE, per
KUN_P1_CONFRONT_GATE.md Check 6 — carried here openly, not held on)" header:
- U1 (lines 93-96): Kerr Ω_H formula carries no fetched primary-source pin; exercised in
  R10, independently recomputed at the gate, dimensionally correct; "pin before any
  external use." Matches gate Check 6 U1.
- U2 (lines 97-99): "ECSK torsion-bounce inflation is generically quoted at tens of
  e-folds" is an unpinned literature characterization; hedged, qualitative, not
  load-bearing; "pin or drop before any external use." Matches gate Check 6 U2.

## Verdict

All three numbered repairs applied exactly as specified, old phrasings fully removed, no
other number in the document altered, receipts untouched and the R9 spot-rerun still
matches the doc, and both UNVERIFIED-AT-GATE items are now carried openly as caveats in
the error-budget section. The hold condition of KUN_P1_CONFRONT_GATE.md is cleared.
D-C confrontation/inversion gate: PASS.

— Miru (second reviewer), 2026-08-19. Supersedes the hold in KUN_P1_CONFRONT_GATE.md;
sibling gates KUN_P1_OMEGA_GATE.md (PASS), KUN_P1_TRANSFER_GATE.md (PASS) untouched.
