# Method2 / SFA — S2 source adjudication review (Lana)

Marker: OVERNIGHT_AUTONOMOUS_GO_20260706T155128Z
Method packet marker: GALAXY_EVOLUTION_METHOD2_ULTRA_FORMAT_ROLE_SPLIT_20260707
Gate honored: S1 exists (`hwao/SOURCE_POSITION_LEDGER_PLAN_20260707.md`) before this S2 began.
Role: Lana-m2 — high-reasoning science judgment / review pressure on the P1 source-position ledger (marker 20260706T142132Z, 36 rows, 13 source groups).
Inputs read: `p1/P1_SOURCE_POSITION_LEDGER_PACKET_20260706T142132Z.md` (all 36 row adjudications), `p1/P1_SOURCE_POSITION_LEDGER_SUMMARY_20260706T142132Z.json`, first ledger row of `p1/P1_SOURCE_POSITION_LEDGER_20260706T142132Z.jsonl` (schema).

## Overall verdict: RATIFIED WITH NOTES

33 of 36 adjudications ratified as written; 1 internal-consistency erratum (28133); 2 standing caveats (28095 review-source weighting; claim-2946 model-dependence). All 12 rejections ratified. No re-adjudication required before S3/S4. Claims and prose remain fully gated — nothing here authorizes a public sentence.

## Per-group review (science pressure applied)

1. **arxiv:0901.1880** — RATIFIED. 28075 (winds less effective in low-z low-mass systems → 2945 caution) is sign-correct and properly limited; 28131 (radio-mode in massive radio galaxies → 2947) fits the kinetic claim. Rejecting 28110 as a duplicate of 28075's span prevents double-counting one caution — good hygiene.
2. **arxiv:1203.2926** — RATIFIED (both rejected). Radiation pressure on star-forming clumps is sub-galactic stellar physics; keeping it out of AGN/quenching claims avoids a category error.
3. **arxiv:1507.06366** — RATIFIED (rejected). GMC-scale radiation feedback, same category-error guard.
4. **arxiv:1706.08987** — RATIFIED, including full `accepted` status for 28141: quasar outflows evacuating star-forming gas is direct primary-observation support for 2943, and it carries a human +1. This is one of only two full acceptances — the scarcity is scientifically appropriate.
5. **arxiv:2009.11175** — RATIFIED with two notes (F2, F3 below). Routing 28095 to 2947 (jet feedback) matches the human +1; 28108 as caution and 28111 as model-bounded support are correctly hedged; 28087 is honest about being a generic complexity caveat.
6. **arxiv:2111.01801** — RATIFIED. Seyfert-jet simulation vs observation comparison as model-bounded 2943 support with subgrid caveat is exactly right.
7. **arxiv:2403.17145** — RATIFIED. Keeping 28158 (observed X-ray bubbles — the only *observed* maintenance heating in the set) while rejecting three same-paper redundant lines shows real anti-stacking discipline.
8. **arxiv:2508.06707** — RATIFIED. 28062 correctly demotes weak jet-gas kinetic coupling to a 2947 caution rather than 2943 support; 28089's "simulations need AGN feedback" is properly model-bounded for 2946.
9. **arxiv:2512.05584** — RATIFIED. DESI/Mg II stellar-feedback outflows as non-AGN alternative support for 2944 (28069, 28073) with recycling caution to 2945 (28066); 28070 rejected as same-source duplication. Sign and scope both correct.
10. **arxiv:2512.21927 (Perseus superbubble)** — RATIFIED (all 4 rejected). Milky-Way superbubble physics under an AGN-quenching page would be the clearest possible overclaim; rejection is mandatory, not optional.
11. **arxiv:2604.15438 (SWAN IV, M51)** — RATIFIED with note F4. All four rows limited; 28060's positive-feedback (compression) caution kept with NO target claim is the ledger's best sign-error guard — a positive-feedback line must never prop up a quenching sentence.
12. **arxiv:2604.22922 (UFOs >0.3c)** — RATIFIED. An ultra-fast-outflow detection is not yet star-forming-gas removal; "broad framing, limited" is the correct strength.
13. **arxiv:2605.03008** — RATIFIED. Stellar feedback insufficient to quench high-mass galaxies → limitation routing to 2944 is sign- and scope-correct.

## Findings

- **F1 — erratum, 28133 (2009.11175 → 2943):** internal inconsistency. Role is `background_only` and the stated reason is "keep it archived rather than pretending it's support," yet status is `accepted_limited` with a `MAY_SUPPORT_ONLY_QUALIFIED...` public-sentence use. Reason and role are right; the use string is wrong. Recommendation: at the claim-status stage treat 28133 as background-only with NO public-sentence use. Docs-only erratum for the next Hwao packet; do not mutate P1 files.
- **F2 — caveat, 28095 (full `accepted`):** arXiv 2009.11175 is a review/synthesis source. Support for 2947 stands (human +1), but any eventual prose must attribute it as review synthesis, not as a primary detection.
- **F3 — stacking guard, claim 2947:** three of its five accepted/limited rows (28095, 28108, 28111) come from the single paper 2009.11175. In any later prose, at most one *support* use of this paper for 2947; the 28108 caution should accompany it.
- **F4 — scoping guard, 2604.15438:** all four rows are a single-galaxy (M51) case study; prose must scope any use to M51 explicitly.
- **F5 — abstract-only cap continuity:** 28 of 36 rows are `abstract_only_verified`; their `ABSTRACT_ONLY_CAP` qualifiers must survive into the claim-status ledger unchanged — this is the method's main defense against strength inflation.
- **F6 — claim 2946 fragility:** maintenance/preventive heating rests on model-bounded rows (28089, 28123) plus exactly one observation (28158). Prose, when eventually allowed, must keep "model-dependent" framing or 2946 will overclaim.

## Overclaim / prose-drift risk assessment

LOW, conditional on F1–F6 being honored downstream. The ledger's own hedging vocabulary (limited caps, caution pairings, archival rejections) is scientifically sound; the single defect found is a bookkeeping inconsistency (F1), not a science error.

## Ultra second-opinion position

`ULTRA_NOT_NEEDED`. The one candidate (28133) is a locally resolvable bookkeeping fix, not a contested scientific judgment; no adjudication in this set is close enough to warrant burning the one supervised second-opinion slot.

## Handback to Hwao

S2 acceptance criteria met: source roles stand as accepted / accepted-limited / rejected per P1 with the F1 erratum recorded. S3 (Goru recount) and S4 (Kun rebuild) may proceed per the S1 plan. Claims/prose and same-format conversion remain gated on a later Hwao packet.

## Safety ledger

Zero DB/SQL/live wiki/page_versions/deploy/restart/git/cloud/API/GCP/billing/account/payment/credits/OAuth/browser/Ultra actions. Writes confined to the Method2 handoff root.
