# K2 and Gasperini/K3 support-bounded record audit

Tori, 2026-09-04 01:22 KST

Scope: sentence-level support in `K2_RESULT_20260903.md`, `K2_CHECK_SHEET_20260903.md`, `K2_ROUTE2_RECONCILIATION_20260903.md`, `K3S1_RESULT_20260903.md`, `K3S1_CHECK_SHEET_20260903.md`, `GASPERINI_K3_RESULT_20260904.md`, `GASPERINI_K3_CHECK_SHEET_20260904.md`, synthesis §§12–13, and affected warrant-table rows 4, 5, 9, 10, 11, 22, 39, 52, 53, 56, 59. The corresponding warrant source records and the superseded K3 topic packet were checked where the table depended on them.

Verdict before the fresh-seat gate: SUPPORT_SOUND_WITH_REPAIRS.

## Findings and repairs

### 1. K2 route-2 executable provenance — material

Finding: `K2_ROUTE2_RECONCILIATION_20260903.md` named `K2_route2_agy.py` as the companion to the independent agy derivation, but that file is a six-line stub which emits no output and says the physics was done manually. It cannot support an executable-receipt claim. The agy Markdown report itself contains the manual equations and classes, so this is a provenance/receipt defect, not evidence that its stated classes differ.

Repair:

- preserved `K2_route2_agy.py` unchanged, SHA-256 `293fb11a146dd84497918c7aef00fceafeaf30bea3f88cd106f137c0f99535d9`;
- added `K2_route2_tori_repair.py`, a distinct SymPy check of the Misner–Sharp mass-continuity identity, both branches of the B3 comoving condition, the equator identity, the null-shell stress, and the DEC deletion probe;
- added `test_K2_route2_agy.py`; the required-receipt test was observed failing against the missing implementation, then passing after the repair;
- preserved the executed output in `K2_route2_tori_repair.out`, lines 1–16, ending `ALL_ROUTE2_CHECKS=PASS`;
- narrowed the check sheet, reconciliation and synthesis so none calls the original agy stub executable.

The repaired B3 receipt explicitly handles the equator degeneracy: away from χ=π/2, `dM/dτ = 3M₀ sin²χ cosχ χ̇`; at χ=π/2, constancy gives `d²M/dτ² = −3M₀χ̇²`; both force a fixed-mass no-shell boundary to be comoving (`K2_route2_tori_repair.out` L4–5).

### 2. K2 check-sheet receipt precision — bounded

Finding: one source range was the non-exact placeholder `L695–70x`; Pathria's `r_b=1` receipt omitted a range; the angular-gauge conversion and null-shell stress statement needed their exact spans. The recollapse sentence incorrectly presented `C_k²<1` as its reason, although recollapse comes from the closed-dust dynamics/Proposition 2 rather than that angular factor alone.

Repair: replaced those pins with entry-4 L43–66, L516–525, L603–642, L695–700, L1063–1072 and L1093–1119; entry-5 L137–179; and entry-22 L289–297. Recollapse now cites entry-1 L394–417 and entry-22 L740–748. Step receipts now point to the executed Tori route-2 output.

### 3. Entry-10 source-line drift — material

Finding: `WARRANT_10_codex.md` and warrant-table row 10 pointed the Kerlick/Hehl–Datta source, the 3/4 average, the FLRW import, equilibrium closure and cusp reversal to line ranges that do not contain those claims.

Repair: the receipts now point to the actual source spans in `1111.4595v2_poplawski_prd85_clean.txt`: Dirac-torsion result L72–108; 3/4 average L109–114; spin-fluid 1/8 closure L119–123; closed FLRW import L134–138; equilibrium closure L152–160; η jump L241–262; and explicit −v to +v reversal L287–294. The warrant token remains `W_MIXED`.

### 4. Downstream K3 inheritance object conflation — material

Finding: `K3S1_RESULT_20260903.md` grouped rows 39, 52, 53 and 59 as users of the spin-fluid 1/8 prescription. Row 53 instead uses the Dirac coefficient `α=9κ(ℏc)²/16`, corresponding to the audited 3/4 prescription. The table also omitted the load-bearing n² receipt from rows 53 and 59.

Repair: result and synthesis now distinguish rows 39/52/59 (spin-fluid 1/8) from row 53 (Dirac 3/4). Warrant records/table now cite entry-53 source L84–94 and entry-59 source L76–88. Every affected study annotation points back to `K3S1_RESULT_20260903.md` §4. No inheritance annotation was removed.

### 5. Gasperini factor attribution — bounded

Finding: the Gasperini result/check sheet said the paper takes a local spin-density magnitude `|S|=ℏn/2`. Gasperini prints the final 1/8 equality, but does not separately state that local rule. The algebraic factorization was valid; the attribution was too strong.

Repair: the records now say that factoring the printed equality leaves the unstated constitutive step `⟨S²⟩=ℏ²⟨n²⟩/4`; constituent spin ℏ/2 makes the factor suggestive but does not determine the sum/average/square ordering. The class remains `CONVENTION CONFIRMED` 2/2.

### 6. Clerical receipts — minor

Finding: the K3 check-sheet timestamp was `19:3x KST`; synthesis gave the K2 ruling as 17:17 although the filed warrant annotations and lane state use 17:18.

Repair: set the check-sheet time to the filed result time 19:32 KST and the K2 ruling receipt to 17:18 KST. Also clarified the Euclidean spatial Casimir notation to avoid confusing it with the signed four-vector contraction.

## Failed attacks / claims retained

- K2's route-1 controls and final classes still reproduce under the preserved codex/Claude scripts; the codex script's B3 `J_UNDETERMINED` is the pre-adjudication seat output, while the Claude equation plus third-seat ruling supplies the filed `J_SMOOTH_EXPANDING` existence class.
- The K2 theorem remains explicitly limited to dust, spherical symmetry, the same Λ, the named mass prescription for the null case, and unclassified trajectory-dependent non-comoving shells.
- Gasperini's source identity, source/PDF hashes, line receipts, same-object reduction, citation boundary, negative search and 2/2 class remain supported.
- K3's n/V calculation, polarized deletion control, factor-six same-object conflict for entry 10, and no-exchange limit reproduce under all three preserved scripts/reports.
- The downstream bounce sign claim remains conditional on the torsion term; only the n² coefficient/scale is called conventional.

## State boundary

No tier, warrant token, standing, stamp, histogram count, study state or successor authorization changed. K3 step 2, K4, K5 and K6 remain NOT ORDERED. Paper HOLD; nothing outward. Nurgaliev & Ponomariev remains unread and non-blocking after `NURGALIEV_PONOMARIEV_OPEN_ROUTE_RETRY_20260904.md`.

Fresh-seat review through `nm_referee_dispatch.sh` is required before this audit closes.

RECORD_SUPPORT_AUDIT_READY_FOR_GATE
