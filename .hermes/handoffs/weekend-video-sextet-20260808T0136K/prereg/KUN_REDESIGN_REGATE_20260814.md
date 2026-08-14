# KUN_REDESIGN_REGATE_20260814

Timestamp: 2026-08-14 KST

Brief: `prereg/_tmp_KUN_REDESIGN_REGATE_BRIEF.md`

Inputs inspected:

- `prereg/LANA_OUTPUT_REDESIGN_20260814.md`
- `prereg/TORI_OUTPUT_LICENCE_CLEARANCE_20260814.md`
- `prereg/_tmp_TORI_INDEPENDENT_LICENCE_BOUNDARY_20260814.md`
- `prereg/KUN_FINAL_GATE_20260814.md`

Boundary: documentation/design gate only. I did not inspect sky rows, export positions, request images, compute chirality, run a sky statistic, freeze a preregistration, publish, commit, push, or accept anything for Duho. K-8 is **not** tripped because no real-sky statistic exists and the output boundary is being changed before any run.

## Verdict

**PASS AS A REDESIGN DIRECTION; HOLD FREEZE UNTIL THE AMENDMENT IS REWRITTEN AND RE-GATED.**

The redesign can remove the derived-catalogue publication dependency, but it does **not** make old BS-1 true. Old BS-1 failed because it required permission for derived-catalogue publication. Duho chose a different output, so the correct repair is to rewrite BS-1's output/licence validity range before freeze.

Safe summary:

> The no-derived-catalogue path is viable if the preregistration is amended so BS-1 binds the aggregate-only output package, with Tori's package-wide non-reconstructability rule as the controlling release rule.

Unsafe summary:

> BS-1 now passes unchanged.

That would hide the fact that the slot text itself presumed an output we are no longer publishing.

## 1. Does The Redesign Clear BS-1, Or Does BS-1 Need Rewriting?

**BS-1 needs rewriting.**

The original BS-1 validity phrase was:

> `licence permits derived-catalogue publication`

That is not satisfied and should remain failed as written. The redesign works by removing the derived-catalogue publication from the public artifact set. That is a design amendment, not a retrospective licence cure.

I accept Lana's A4 direction in substance, but it must be rewritten under Tori's stricter package-wide rule. A safe BS-1 replacement is:

> `licence/terms permit the frozen aggregate-only output package: no per-object derived catalogue, no object identifiers, no coordinates, no source rows, no per-object derived quantities, no request-only private catalogue, and no public artifact family that cumulatively reconstructs membership or functions as a catalogue substitute; Legacy acknowledgement/citation obligations are carried in full; any Legacy image pixels, if ever used, follow the separate image-credit route.`

This amended BS-1 must return in an assembled preregistration candidate. The present redesign report is not itself the freeze text.

## 2. Binding Aggregation Rule

**Tori's six package-wide conditions bind. Lana's numeric rules are additional guardrails.**

Precedence:

1. Tori's package-wide rule is mandatory and controlling.
2. Lana's `k >= 50`, frozen-cell, no-key, `<= 5,000 cells`, and "ours not theirs" rules apply only after Tori's package-wide rule passes.
3. If the two conflict, Tori's rule wins.

Binding release rule:

1. **Rowless:** no object key, row, coordinate, URL, source field, per-object derived quantity, reversible row hash, or per-object label/score.
2. **Fixed and finite:** schema and cells frozen before real-sky statistics; no post-result boundaries, dynamic query interface, or unlimited slicing.
3. **Study-result only:** cells contain this study's estimands, instrument summaries, uncertainties, or controls, not re-tabulated survey attributes.
4. **Non-reconstructable cumulatively:** no combination, overlap, differencing, version sequence, auxiliary file, or later release can recover membership or object-level attributes.
5. **Non-substitutive cumulatively:** the complete package cannot function as the source catalogue, a derived catalogue, or a catalogue-scale lookup/re-analysis product.
6. **Separate image compliance:** any source image pixels must follow their actual image-layer licence and credit route; image compliance cannot cure a catalogue-like table.

Lana's numeric rules remain useful:

- ordinary aggregate cell `k >= 50`, masked when sub-threshold;
- no ordinary table/map above `5,000` cells;
- cells frozen and object-independent;
- no per-object keys or coordinates;
- no aggregated re-tabulations of survey attributes.

But the numbers are not legal safe harbors. A package can satisfy every per-table numeric limit and still be reconstructable by overlap/differencing. That is the exact failure Tori's rules 4-5 block.

## 3. Tori's Spot-Check Correction

**Tori is right. Lana's what-is-lost table must be corrected.**

Running the released classifier on twenty newly selected public cutouts is not a spot-check of NebulaMind's hidden labels. It tests code behavior on those objects. Without a public expected per-object result, the reader cannot compare "our label for object X" against "their label for object X."

Corrected row:

| Check the catalogue enabled | Lost? | Substitute |
|---|---|---|
| Spot-checking NebulaMind's individual hidden labels against images | **Yes, except through rebuild** | A reader may run the public classifier on arbitrary cutouts to test code behavior. Exact verification of NebulaMind's private label for a given object requires rebuilding the canonical slice or full file and matching the published commitment hash. |

This is not cosmetic. The what-is-lost table is a claim to readers about what the redesign preserves. Saying object-level spot-checking is "not lost" would overstate reproducibility.

## 4. Reproducibility Path

**Conditionally honest and likely sufficient for a referee, if the claims are narrowed.**

The combination is viable:

- public code, weights, seeds, environment, WCS/parity tests, and query/cut definitions;
- exact public product/version declarations;
- aggregate outputs and maps under the package-wide release rule;
- commitment hashes for the private canonical per-object result file and 67 slices;
- deterministic rebuild instructions from public products;
- release manifest/linter that blocks row-like or reconstructable artifacts.

But the paper must say what this does and does not prove.

Safe wording:

> Commitment hashes cryptographically bind the private result file and allow byte-equality checking after an independent rebuild.

Unsafe wording:

> Commitment hashes prove the hidden rows are scientifically correct, or are strictly stronger than table inspection.

Hashes prove equality to committed bytes, not correctness. Correctness still rests on preregistration, source products, code, tests, aggregate receipts, and independent rebuild. A referee can evaluate the study without a public derived catalogue, but cannot cheaply inspect NebulaMind's exact object-level labels unless they rebuild the relevant slice.

The data-availability statement must be explicit:

> No per-object NebulaMind derived catalogue is public or available on request. Reproducibility is by rebuilding from cited public products, frozen code, aggregate outputs, and commitment hashes.

## 5. Does The Redesign Weaken The Test?

**No, not if the Tori rule and corrections are incorporated.**

I attacked the decision path for dependencies on withheld object rows:

- F-6 decision category uses aggregate `M`, `D(n_L)`, `A`, `A_c`, intervals, p-values, constants, and frozen thresholds.
- Negative controls publish aggregate count-swap, sign-negation, split, map, and jackknife summaries.
- Covariate battery publishes aggregate leakage/AUC/LR/Holm/coupling-bound outputs.
- Hand-check attenuation uses per-stratum confusion aggregates and intervals; individual hand-check rows are not required for the decision, although object-level auditability is lost.
- Commitment hashes preserve post-run integrity checks without distributing rows.

The test's falsifiability and decision regions do not require public per-object labels. What is weakened is **reuse**, not the preregistered decision. The real loss is object-level/sub-degree reuse by third parties who do not rebuild.

One caution: the public package must not include overlapping aggregate families that permit inverse reconstruction. For example, many differently binned maps, per-brick tables, or user-selectable slices could turn an "aggregate" release back into a derived catalogue. That would reopen BS-1.

## 6. Still Blocking Freeze

Hard blocker from this re-gate:

1. **Exact preregistration amendment absent.** The redesign direction is acceptable, but the freeze candidate must incorporate the amended BS-1/F-10 text with Tori's package-wide rule, corrected what-is-lost table, corrected hash language, and data-availability statement.

Earlier final-gate items restated:

2. **BS-1 old licence text still fails until rewritten.** Do not mark old `licence permits derived-catalogue publication` as pass.
3. **Release manifest/linter absent.** Tori's package-wide rule needs a machine-enforced release check over the complete package, not per-file hand judgment only.
4. **Assembled freeze document absent.** The current preregistration remains an earlier draft; the redesigned output boundary must be integrated into a clean exact freeze candidate.
5. **BS-8 wording.** The freeze must say analytical evaluation of the pinned harness logic, not a literal custom-parameter rerun.
6. **BS-4 warning placement.** The near-total-abstention secondary warning must appear in the assembled preregistration.
7. **BS-3 zero-case distinction.** Keep the R1/R2 1,000 nonzero production grid separate from the R3 signed-zero edge probe.
8. **BS-6 `TYPE` wording.** Call it automated source-type / point-source exclusion, not visual morphology or spiral selection.
9. **BS-10 locator cleanup.** Bind the published-journal locator/checksum if this becomes publication-facing; K-14 still stands regardless.

None of these authorizes a sky run. They are freeze-assembly and output-boundary blockers.

## Plain Answer For Duho

The redesign path is viable, but only by changing the preregistration's output rule. We are no longer trying to prove that derived-catalogue publication is licensed. We are redesigning the public package so there is no derived catalogue to license.

Tori's package-wide non-reconstructability/non-substitutability rule must bind. Lana's per-table numeric limits are useful guardrails, not the line. The public record must admit that object-level label spot-checking and object-level reuse are lost unless a reader rebuilds the private result file and matches the commitment.

No freeze, publication, acceptance, commit, push, or sky run follows from this re-gate. Duho owns acceptance.
