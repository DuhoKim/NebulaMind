# KUN PREREGISTRATION DRAFT GATE

Timestamp: 2026-08-12 KST

Targets:

- `prereg/PREREG_LONGO_AMPLITUDE_TEST_20260812.md`
- `prereg/YUI_PRODUCTION_ESTIMATOR_APPENDIX_20260812.md`

Late-arrived evidence inspected:

- `prereg/GORU_ACCEPTED_YIELD_RECEIPT_20260812.md`

## Verdict

PASS AS A PREREGISTRATION DRAFT STRUCTURE; HOLD FREEZE.

This could become a freezeable preregistration after the binding slots are filled and reassembled. It is not freezeable now, and no empirical sky run is authorized.

The parent draft is mostly doing the right thing: it separates frozen rules from binding slots, carries the Longo-only claim boundary, blocks Shamir decision language, and gives exact decision regions. The slot register is the right mechanism. The issue is not that it has only one visible "BINDING SLOT" marker; it has a full §B register with ten slots. That is acceptable.

But two things prevent freeze:

1. BS-1/BS-2 survey-route, covariate-product, and accepted-yield receipts are not in closed form.
2. Appendix A is a good estimator specification draft, but it is not yet a filled production-estimator receipt: no materialized training-set manifest, no final weights hashes, no numeric τ, no measured retention, and no production mirror/unit-test receipts.

## 1. Numeric Values: Frozen Or Slots?

PASS IN STRUCTURE.

The parent preregistration mostly handles numeric values correctly:

- fixed statistical constants are frozen: `N_perm=100,000`, `p<0.001`, `p>0.05`, `N_hc=500`, `a_floor=0.85`, `N_accepted>=100,000`, `Nside=16` free-axis grid, `Nside=128/32` covariate maps, leakage thresholds, AUC thresholds, and power requirement `>=0.95`;
- values depending on the bound survey or final instrument are slots: survey route, covariate products, primary/secondary instruments, Longo sign dictionary, photometric cuts, distortion branch, power rerun, evaluated constants, Shamir amplitude class.

I do not see a major value silently frozen ahead of its evidence. The register is explicit enough that the freeze gate can check each slot.

One required cleanup before freeze: the generator-code hash in Yui's appendix is abbreviated as `89da33ec6260e75e...`. The actual hash I measured is:

`89da33ec6260e75e06eadb0f171da4c52f1478b59ff5e543d363dbf56fefcd75`

Freeze artifacts need full hashes, never ellipses.

## 2. Claim Boundary

PASS.

The boundary survives in the parent preregistration:

- title is explicitly `LONGO-AMPLITUDE TEST`;
- canonical sentence says a null does not establish sky isotropy and rejects only Longo's amplitude at Longo's axis if the preregistered rejection rule is met;
- headline says it does not test `A ~= 0.02`, Shamir, BHU, or whether the sky is isotropic;
- Shamir is secondary interval-only, with no decision language;
- outcome handling repeats that any positive is not BHU.

I also verified the repaired canonical sentence now appears in the V2 design brief at §0 and §6, and in this prereg. The earlier V2 "verbatim" custody error has been recorded openly in the prereg. This is clean.

## 3. Yui Estimator Appendix

PASS AS SPECIFICATION DRAFT; NOT CLOSED AS BS-3.

The appendix addresses the right five surfaces:

- synthetic training generator;
- architecture;
- weights-freeze policy;
- acceptance threshold procedure;
- mirror and signed-zero receipts.

It also handles the expensive abstention assumption honestly. It does **not** freeze the friendly `~50%` retention. It says production abstention is currently unknown and requires measured retention on a held-out frozen synthetic set, using the lower 95% bound for sample-size arithmetic. That is the right rule.

Still missing before BS-3 can close:

1. full generator-code hash, not truncated;
2. master seed `M`;
3. materialized training-set manifest and manifest hash;
4. exact training implementation details or an explicit statement that only the final weights hash, not the training recipe, is the reproducibility object;
5. final weights file hash and canonical flat-parameter hash;
6. numeric τ and null-set manifest hash;
7. measured retention at τ, with lower 95% bound;
8. production identity test receipts on the final raster/dtype;
9. signed-zero test receipt;
10. interpolating-mirror canary receipt;
11. per-object paired probe outputs / flip-imbalance receipt.

The training implementation point matters. The appendix freezes architecture and final weights policy, but not optimizer, loss, epochs, batch size, learning rate, stopping rule, framework version, or deterministic settings in enough detail to reproduce training. That is acceptable only if the final frozen weights are declared to be the estimator identity. If reproducible training is claimed, those details must be added.

## 4. Incoming Survey/Yield Receipts

BS-1 is still open.

I inspected the newly present `prereg/GORU_ACCEPTED_YIELD_RECEIPT_20260812.md`. It is honest, but it does **not** close accepted yield. It marks every cut survival count `[UNKNOWN — requires catalog query]` and then estimates plausibility by multiplying external priors. That is not an accepted-yield receipt under the prereg's own rule.

To close BS-1, the incoming receipt must contain:

- exact DR10/DR10.1 product paths or records;
- exact frozen parent cuts;
- actual queried surviving counts after each cut, not only plausible extrapolation;
- actual footprint variance around Longo's axis, meeting `var(cos theta) >= 0.15`;
- actual parent count multiplied by measured BS-3 lower-bound retention, yielding `N_accepted >= 100,000`;
- licence statement permitting derived-catalogue publication;
- query/code receipt with hash and rerunnable command or script.

If the receipt still says `[UNKNOWN]`, BS-1 remains open.

BS-2 is also open until Tori binds exact covariate products, coverage, photo-z status, and deblend flags.

## 5. Could This Be Frozen Once Receipts Land?

Yes, with the repairs above.

This does not need another conceptual design pass. It needs assembly of the binding-slot receipts, plus a small drafting repair to remove abbreviated hashes and clarify the estimator reproducibility object.

Freeze gate should require:

- BS-1 through BS-10 filled inside validity ranges;
- no `[VERIFY]`, `[UNKNOWN]`, ellipsized hash, or "drafting in parallel" language left in the assembled prereg;
- Appendix A replaced or supplemented by a filled estimator receipt with hashes, τ, retention, and tests;
- Tori survey/covariate custody receipt present;
- Goru accepted-yield receipt based on actual counts present;
- evaluated constants table computed from the bound `N` and measured `a`;
- final assembled prereg sha-pinned and returned for gate.

## Plain Verdict For Duho

Status:

> HOLD FREEZE; PASS DRAFT STRUCTURE.

Authorized:

> Continue filling the binding slots and assembling the freeze candidate.

Not authorized:

- no sky run;
- no real galaxy handedness computation;
- no result;
- no publication;
- no accepted status.

The draft is close enough that, if Tori and Goru land actual binding receipts and Yui fills Appendix A with real hashes/τ/retention/test outputs, it can return as a freeze candidate. The Goru receipt currently present does not close yield because it still depends on unknown counts and multiplied assumptions.
