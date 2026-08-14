# KUN_FINAL_GATE_20260814

Timestamp: 2026-08-14 KST

Brief: `prereg/_tmp_KUN_FINAL_GATE_BRIEF.md`

Boundary: documentation/aggregate gate only. I did not query a service, inspect rows, export positions, inspect images, compute chirality, run a sky statistic, freeze a preregistration, publish, commit, push, or accept anything for Duho.

## Verdict

**HOLD FREEZE.**

The complete binding-slot set does not pass because **BS-1 fails its licence validity range**. That failure is real and should not be softened. The public Legacy Surveys text located in the receipt grants CC BY 4.0 for **images** and gives acknowledgement language for use of **data** in papers; it does not expressly establish permission to publish a per-object derived catalogue. The BS-1 validity range says the licence must permit derived-catalogue publication. That range is not met.

The other nine slots are either PASS or PASS WITH REPAIR/NOTICE, but none rescues BS-1. A failed slot sends the preregistration back to design or permission gathering; it does not authorize a workaround.

## Slot Gates

| Slot | Gate | Reason |
|---|---|---|
| BS-1 licence | **FAIL** | Tori's scope reading is sound: CC BY is applied to "Images"; acknowledgement for data use is not a catalogue/derived-product licence grant. |
| BS-2 covariates | **PASS** | 9/10 core covariates survive by an absolute-count lower-bound coverage rule; arm contrast is dropped rather than invented. |
| BS-3 primary instrument | **PASS** | Yui supplied the missing 1,000-probe production identity witness and carried retention/R4/R5 receipts. |
| BS-4 secondary instrument | **PASS WITH REQUIRED NOTICE** | Validity range is met, but the prereg/results text must state it is a near-total-abstention cross-check, not a usable high-yield secondary. |
| BS-5 Longo sign | **PASS** | Longo's sign, symbols, and axis are quoted and mapped openly to the `+chi` convention; synthetic sign anchor required before real images. |
| BS-6 photometric cuts | **PASS** | I accept Lana's §3b reading: `type <> 'PSF'` is an automated source-type/star-galaxy exclusion, not a forbidden visual/chirality morphology label. |
| BS-7 distortion | **PASS** | One branch is declared: FAIL_CLOSED on distortion metadata; local-Jacobian branch is not selected. |
| BS-8 power | **PASS WITH DECLARED DEVIATION ACCEPTED** | The unmodified pinned harness cannot evaluate arbitrary bound `N`/`A_eff`; the direct analytical evaluation uses the same normal-approximation logic and is comfortably above 0.95. |
| BS-9 constants | **PASS** | Constants clear `sigma_ours <= 0.008` and detection-floor `<= 0.025`, including at `a = 0.85`. |
| BS-10 Shamir class | **PASS AS INFORMATIONAL** | Amplitude class is pinned from full text; K-14 still forbids Shamir decision language. Published-journal locator binding remains good cleanup, not a decision unlock. |

## Specific Attack Points

### BS-6 `type`

I accept the §3b reading. `TYPE` is a Tractor source-model classification used for point-source exclusion. It is not a human visual morphology label, not Galaxy Zoo membership, not spiral/non-spiral selection, and not a chirality label. The condition `type <> 'PSF'` is therefore admissible under BS-6 as an automated star/galaxy source-type cut.

Required wording: the assembled preregistration must call it an **automated source-type / point-source exclusion**. It must not describe it as a morphology-clean spiral selection.

I also accept the absence of a surface-brightness cut. BS-6 asked for constants for mag/size/SB ranges; the correct fill for SB is "none in the frozen design", not inventing a late SB cut.

### BS-8 Harness Deviation

Accepted, but it must remain disclosed.

The fill rule says "rerun of sha-pinned `spike/sim_power.py` at A_eff, bound N." The pinned script has hardcoded `N_list` and `A_list`, and accepts no CLI parameters. Editing it to add inputs would break the "sha-pinned unmodified" requirement. Goru's direct evaluation uses the same normal-approximation p-value logic embodied in `compute_power_curve()` and applies it to the frozen values:

- `N = 130,076`;
- conservative `a = 0.999711`;
- `A_eff = 0.04077642`;
- `alpha = 0.001`;
- reported power effectively `1.0000`.

Because the result is nowhere near the `0.95` threshold, the declared deviation is not being used to rescue a marginal pass. I gate BS-8 as PASS WITH DECLARED DEVIATION ACCEPTED. Freeze text must not say the harness was literally rerun at custom inputs; it must say the pinned harness was inspected and its analytical power logic was evaluated directly because the hardcoded script could not be parameterized without modification.

### BS-3 Zero-Case Clarity

Yui's receipt resolves the apparent contradiction. The 1,000-probe production grid had zero R2 zero cases and 1,000 nonzero R2 cases. The signed-zero probe in section 4 is the separate R3 mirror-symmetric edge case, outside the nonzero production grid.

This is no longer a result defect. For clarity, the assembled preregistration should preserve the distinction:

> R1/R2 identity: 1,000 nonzero production probes. R3 signed-zero: separate mirror-symmetric edge probe, value-equal but bit-different, and excluded by ordered `abs(chi) > tau`.

### BS-2 Coverage Bound

The absolute-count coverage rule is conservative.

For any accepted subset with `N >= 100,000`, if a product is missing for `M` eligible parents, the adversarial worst case is that as many missing parents as possible are selected into the accepted subset. The accepted coverage is therefore at least:

`1 - min(M, N) / N`.

The minimum over all valid `N >= 100,000` is bounded by:

`1 - min(M, 100000) / 100000`.

That is exactly the rule Tori used. It is not a sky-area extrapolation and does not assume density uniformity. The depth/seeing missing counts, `1,234` and `1,220`, therefore give worst-case accepted coverage of `98.766%` and `98.780%`, above the 95% rule. The two missing colour rows give `99.998%`.

### BS-4 Abstention

BS-4 passes the literal range, but the warning is load-bearing. The secondary has:

- production held-out acceptance `16/12,000`;
- retention `0.133333%`;
- abstention `99.866667%`;
- fresh 1,000-probe acceptance `1/1,000`.

The assembled preregistration must carry this warning in both the BS-4 slot and the negative-control/secondary-instrument section:

> The secondary instrument is a sparse, training-free cross-check with near-total abstention; it is not a high-yield substitute for the primary and cannot rescue primary failure or supply an independent powered estimate.

Leaving that warning only in Yui's receipt is insufficient because readers of the freeze document would otherwise over-read the word "PASS".

### BS-1 Licence Failure

Confirmed. Tori is right to fail it.

The receipt quotes the Legacy Surveys page applying CC BY 4.0 to **images**, and separately quotes acknowledgement language for use of **data** in papers. That is not the same as a licence grant covering source catalogues or derived per-object catalogues. The CC BY legal code only helps after the licensor has applied CC BY to the relevant licensed material. Here, the located primary text applies it to images, not the DR10 Tractor/sweep catalogue or a derived catalogue.

I do not have a primary-source quotation that proves derived-catalogue publication is covered. Therefore I will not infer one.

## What BS-1 Failure Forecloses

BS-1 failure forecloses:

- freezing this preregistration under the current binding-slot register;
- publishing a per-object derived catalogue from this route under the current evidence;
- representing the route as publication-ready;
- using acknowledgement language as if it were a licence grant;
- proceeding to a public result package whose plan depends on releasing derived per-object data.

BS-1 failure does **not** foreclose:

- preserving the internal design work;
- aggregate/documentation-only analysis notes;
- seeking explicit written permission or a primary catalogue/derived-product licence;
- redesigning the output so it does not require derived-catalogue publication, if that redesign is explicitly re-gated;
- private/internal feasibility calculations already performed under their own boundaries;
- Duho deciding whether the scientific question remains worth pursuing after the legal/custody blocker.

It also does not imply the science is false or the footprint/instrument gates failed. It means the route, as specified, lacks a required publication-permission limb.

## Complete Freeze Blockers

Blocking:

1. **BS-1 licence FAIL**: derived-catalogue publication permission is not established from primary sources.

Required before any future freeze candidate even if BS-1 is repaired:

2. **Assembled freeze document absent**: the current preregistration file is still the earlier draft; all ten receipts must be incorporated or referenced in a clean hash-pinned freeze candidate.
3. **BS-8 wording**: the freeze must accurately say analytical evaluation of the pinned harness logic, not literal custom-parameter rerun.
4. **BS-4 warning placement**: the near-total-abstention warning must appear in the assembled preregistration, not only in the receipt.
5. **BS-3 zero-case distinction**: R1/R2 production grid versus separate R3 signed-zero probe must remain clear.
6. **BS-6 `TYPE` wording**: call it automated source-type / point-source exclusion, not visual morphology or spiral selection.
7. **BS-10 locator cleanup**: Tori should bind the published-journal locator/checksum if this ever returns for publication-facing freeze, although BS-10 remains informational and K-14 stands.

Only item 1 is the hard slot failure. Items 2-7 are assembly/clarity requirements that prevent a sloppy freeze packet if the licence problem is later solved or the design is revised.

## Plain Answer For Duho

The slot set does not freeze. Nine slots are scientifically/custodially usable with the repairs/notices above, but **BS-1 fails** because permission to publish a derived per-object catalogue is not established. The honest next step is not a sky run; it is either a permission repair from a primary source or an explicit redesign that no longer requires derived-catalogue publication and then a fresh gate.

No freeze, publication, acceptance, commit, push, or sky run follows from this report. Duho owns acceptance.
