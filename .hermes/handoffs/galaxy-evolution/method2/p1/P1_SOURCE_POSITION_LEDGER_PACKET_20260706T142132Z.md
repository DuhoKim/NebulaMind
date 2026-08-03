# Method2/SFA P1 source-position ledger

Marker: `GALAXY_EVOLUTION_METHOD2_P1_SOURCE_POSITION_LEDGER_20260706T142132Z`

Consumed approval phrase: `APPROVE METHOD2 P1 DOCS-ONLY SOURCE-POSITION LEDGER`
Current safety phrase: `NO ACTIVE EXECUTION PHRASE`

## Method Baseline

Start from papers/source positions; only accepted or accepted-limited source roles may support public wiki sentences.

## Result

- Total source-position rows reviewed from the existing docs-only queue: `36`
- Accepted: `2`
- Accepted-limited: `22`
- Rejected: `12`
- Source groups: `13`

This P1 artifact does not create claims, prose, DB rows, page_versions, trust scores, or runtime changes. It records which existing source-position decisions may feed a later Method2 docs-only claim/status ledger.

## Accepted or accepted-limited rows

| evidence | arXiv | status | target claim | role | public sentence use | reason |
|---:|---|---|---:|---|---|---|
| 28060 | 2604.15438 | accepted_limited | None | limitation_or_caution | LIMITED_CAUTION_ONLY_NO_CURRENT_TARGET_CLAIM_SUPPORT | This line is about AGN feedback that HELPS star formation (compression), the opposite of the page's quenching claims. The human marked it a weakening, and none of the new claims cover positive feedback, so keep it archived as a caution rather than pretending i |
| 28062 | 2508.06707v1 | accepted_limited | 2947 | limitation_or_caution | MAY_SUPPORT_ONLY_QUALIFIED_OR_LIMITED_PUBLIC_SENTENCE_AFTER_LATER_GATE_ABSTRACT_ONLY_CAP | The source is about high-redshift radio galaxies and jet-gas coupling; the row emphasizes weak kinetic coupling, so it best serves 2947 as a context-dependent kinetic/radio caution rather than broad 2943 support. |
| 28066 | 2512.05584v2 | accepted_limited | 2945 | limitation_or_caution | MAY_SUPPORT_ONLY_QUALIFIED_OR_LIMITED_PUBLIC_SENTENCE_AFTER_LATER_GATE | Gas in massive-galaxy stellar-feedback outflows falling back before 100 kpc is a gas-removal/recycling caution, so it supports claim 2945 rather than an AGN-outflow success claim. |
| 28069 | 2512.05584v2 | accepted_limited | 2944 | support | MAY_SUPPORT_ONLY_QUALIFIED_OR_LIMITED_PUBLIC_SENTENCE_AFTER_LATER_GATE_ABSTRACT_ONLY_CAP | The DESI/Mg II result says stellar feedback can drive strong outflows and baryon deficiency in low-mass galaxies, a direct non-AGN alternative/qualifier for claim 2944. |
| 28073 | 2512.05584v2 | accepted_limited | 2944 | support | MAY_SUPPORT_ONLY_QUALIFIED_OR_LIMITED_PUBLIC_SENTENCE_AFTER_LATER_GATE | The row says outflow rate and mass-loading depend strongly on SFR, confirming the stellar-feedback outflow scenario; it is role-distinct mechanism support for non-AGN alternatives in 2944. |
| 28074 | 2604.15438 | accepted_limited | 2942 | support | MAY_SUPPORT_ONLY_QUALIFIED_OR_LIMITED_PUBLIC_SENTENCE_AFTER_LATER_GATE_ABSTRACT_ONLY_CAP | This line shows M51's AGN works in a specific (kinetic, low-power) way, which supports the idea that AGN feedback is not one uniform thing. It fits the scoped claim; it's also kinetic-relevant, but as one galaxy's case it's a limited support. |
| 28075 | 0901.1880v2 | accepted_limited | 2945 | limitation_or_caution | MAY_SUPPORT_ONLY_QUALIFIED_OR_LIMITED_PUBLIC_SENTENCE_AFTER_LATER_GATE_ABSTRACT_ONLY_CAP | The source says winds are less likely to remove gas in low-redshift low-mass systems, which directly supports gas-removal caution in claim 2945. |
| 28087 | 2009.11175v1 | accepted_limited | 2942 | support | MAY_SUPPORT_ONLY_QUALIFIED_OR_LIMITED_PUBLIC_SENTENCE_AFTER_LATER_GATE_ABSTRACT_ONLY_CAP | This line just says AGN feedback is complicated and works in many ways, which backs the claim that it isn't one simple universal thing. It fits the scoped claim but is a general caveat, so it's a supporting-but-limited relink. |
| 28088 | 2605.03008v1 | accepted_limited | 2944 | limitation_or_caution | MAY_SUPPORT_ONLY_QUALIFIED_OR_LIMITED_PUBLIC_SENTENCE_AFTER_LATER_GATE_ABSTRACT_ONLY_CAP | The quoted span says stellar feedback can regulate star formation in low- and intermediate-mass systems but is generally insufficient to fully quench high-mass galaxies; that is a non-AGN/stellar-feedback limitation that supports 2944 as an alternatives-and-qu |
| 28089 | 2508.06707v1 | accepted_limited | 2946 | support | MAY_SUPPORT_ONLY_QUALIFIED_OR_LIMITED_PUBLIC_SENTENCE_AFTER_LATER_GATE | The row says cosmological simulations need AGN feedback to avoid over-forming massive galaxies; that is model-bounded maintenance/preventive support for claim 2946. |
| 28091 | 2604.15438 | accepted_limited | 2943 | support | MAY_SUPPORT_ONLY_QUALIFIED_OR_LIMITED_PUBLIC_SENTENCE_AFTER_LATER_GATE_ABSTRACT_ONLY_CAP | This line says outflow-driven turbulence can stop gas from forming stars, which backs the idea that AGN outflows suppress star formation. It fits the outflow claim, though the exact mechanism (turbulence, not gas removal) and its background-review status mean  |
| 28095 | 2009.11175v1 | accepted | 2947 | support | MAY_SUPPORT_PUBLIC_WIKI_SENTENCE_AFTER_LATER_CLAIM_STATUS_AND_PROSE_GATE | This line is about AGN jets driving feedback, which is exactly the new kinetic/radio-mode claim. Route it there and relink it as support, matching the human's +1. |
| 28108 | 2009.11175v1 | accepted_limited | 2947 | limitation_or_caution | MAY_SUPPORT_ONLY_QUALIFIED_OR_LIMITED_PUBLIC_SENTENCE_AFTER_LATER_GATE_ABSTRACT_ONLY_CAP | This line says we don't yet fully understand AGN jet feedback and its outflow powers. It's about the kinetic/radio claim, but as a caution, not proof. Attach it to the kinetic claim as a caveat so the claim isn't only backed by cheerleading from the same paper |
| 28111 | 2009.11175v1 | accepted_limited | 2947 | support | MAY_SUPPORT_ONLY_QUALIFIED_OR_LIMITED_PUBLIC_SENTENCE_AFTER_LATER_GATE_ABSTRACT_ONLY_CAP | This line says simulations show AGN jets blow bubbles of gas, which supports the kinetic/radio-mode claim, but because it's a simulation result it's a model-bounded support. Route it to the kinetic claim and mark the model caveat. |
| 28123 | 2403.17145v1 | accepted_limited | 2946 | support | MAY_SUPPORT_ONLY_QUALIFIED_OR_LIMITED_PUBLIC_SENTENCE_AFTER_LATER_GATE_ABSTRACT_ONLY_CAP | This line says simulations all model AGN feedback differently, which is exactly why the maintenance/heating claim is called model-dependent. It's a good, limited support for that claim. |
| 28131 | 0901.1880 | accepted_limited | 2947 | support | MAY_SUPPORT_ONLY_QUALIFIED_OR_LIMITED_PUBLIC_SENTENCE_AFTER_LATER_GATE_ABSTRACT_ONLY_CAP | The row explicitly names AGN radio-mode feedback in massive radio galaxies, fitting the 2947 kinetic/radio-mode claim better than the generic maintenance or gas-removal claims. |
| 28133 | 2009.11175v1 | accepted_limited | 2943 | background_only | MAY_SUPPORT_ONLY_QUALIFIED_OR_LIMITED_PUBLIC_SENTENCE_AFTER_LATER_GATE_ABSTRACT_ONLY_CAP | This line is about how to measure outflow numbers, not about outflows shutting down star formation. It's related to the outflow claim in topic only, so keep it archived rather than pretending it's support. |
| 28140 | 2111.01801v2 | accepted_limited | 2943 | support | MAY_SUPPORT_ONLY_QUALIFIED_OR_LIMITED_PUBLIC_SENTENCE_AFTER_LATER_GATE_ABSTRACT_ONLY_CAP | The source simulates Seyfert jets and compares produced inflows/outflows with observations; it supports 2943 that AGN activity can drive large-scale multiphase outflows, with a simulation/subgrid caveat. |
| 28141 | 1706.08987v2 | accepted | 2943 | support | MAY_SUPPORT_PUBLIC_WIKI_SENTENCE_AFTER_LATER_CLAIM_STATUS_AND_PROSE_GATE | This paper shows AGN outflows in distant quasars pushing away the gas where stars form, which directly backs the claim that AGN outflows remove star-forming gas. Relink it to the outflow claim, matching the human's +1. |
| 28144 | 2508.06707v1 | accepted_limited | 2943 | support | MAY_SUPPORT_ONLY_QUALIFIED_OR_LIMITED_PUBLIC_SENTENCE_AFTER_LATER_GATE_ABSTRACT_ONLY_CAP | The source record and row cite multiple detections of powerful high-velocity gas outflows in lower-redshift AGN hosts, directly supporting the scoped AGN-outflow claim 2943. |
| 28148 | 2604.22922 | accepted_limited | 2943 | support | MAY_SUPPORT_ONLY_QUALIFIED_OR_LIMITED_PUBLIC_SENTENCE_AFTER_LATER_GATE_ABSTRACT_ONLY_CAP | The quoted span frames AGN feedback as being driven by powerful accretion-disk outflows and as a plausible mechanism for host-galaxy coevolution correlations; it supports 2943 only as broad, limited AGN-outflow framing, not as the detection-result paragraph. |
| 28151 | 2403.17145v1 | accepted_limited | 2942 | support | MAY_SUPPORT_ONLY_QUALIFIED_OR_LIMITED_PUBLIC_SENTENCE_AFTER_LATER_GATE_ABSTRACT_ONLY_CAP | This line argues AGN feedback matters most in medium-sized systems (groups), which supports the idea that feedback is scoped and not a one-size-fits-all quenching mechanism. Relink to the scoped claim, limited. |
| 28155 | 2604.15438 | accepted_limited | 2942 | support | MAY_SUPPORT_ONLY_QUALIFIED_OR_LIMITED_PUBLIC_SENTENCE_AFTER_LATER_GATE_ABSTRACT_ONLY_CAP | This line says galaxy-evolution models need AGN feedback to match reality, which supports the claim that AGN feedback is a real (if scoped) way galaxies quench. It's theory/background rather than a direct observation, so it's a supporting-but-limited fit. |
| 28158 | 2403.17145v1 | accepted_limited | 2946 | support | MAY_SUPPORT_ONLY_QUALIFIED_OR_LIMITED_PUBLIC_SENTENCE_AFTER_LATER_GATE_ABSTRACT_ONLY_CAP | This line describes real X-ray bubbles that AGN blow in hot gas - actual observed maintenance heating, which the maintenance claim currently lacks. Attach it to that claim as a limited support and flag it for the observed-heating gap. |

## Rejected rows

| evidence | arXiv | status | target claim | role | public sentence use | reason |
|---:|---|---|---:|---|---|---|
| 28070 | 2512.05584v2 | rejected | None | background_only | MUST_NOT_SUPPORT_PUBLIC_WIKI_SENTENCE | This is a general simulation-background sentence saying stellar-feedback gas ejection is introduced in models; it duplicates the stronger 28069/28073 same-source evidence and should not inflate 2944. |
| 28076 | 2512.21927v1 | rejected | None | background_only | MUST_NOT_SUPPORT_PUBLIC_WIKI_SENTENCE | The Perseus superbubble is a Milky-Way massive-star/supernova feedback cycle that can clear gas and trigger star formation; it is not AGN/radio-mode evidence and is too local/cloud-scale for visible successor support. |
| 28080 | 2512.21927v1 | rejected | None | background_only | MUST_NOT_SUPPORT_PUBLIC_WIKI_SENTENCE | The row describes fragmentation and formation/dispersal of star-forming regions by a local stellar superbubble; it is relevant background but not a clean Galaxy Evolution AGN/quenching successor evidence row. |
| 28082 | 1507.06366v1 | rejected | None | background_only | MUST_NOT_SUPPORT_PUBLIC_WIKI_SENTENCE | This source concerns radiation feedback from young star clusters in GMCs and whether it disrupts clouds; it is sub-galactic stellar feedback, not AGN/quenching evidence for visible successors. |
| 28083 | 2512.21927v1 | rejected | None | background_only | MUST_NOT_SUPPORT_PUBLIC_WIKI_SENTENCE | The phrase calls the source an extreme example of stellar-feedback-driven structures in disk galaxies; useful context, but not a target-specific AGN/quenching claim support. |
| 28084 | 2512.21927v1 | rejected | None | background_only | MUST_NOT_SUPPORT_PUBLIC_WIKI_SENTENCE | The row says stellar feedback disrupts molecular clouds and affects star-formation efficiency; it is generic cloud-scale background, not a scoped successor claim support. |
| 28110 | 0901.1880 | rejected | None | background_only | MUST_NOT_SUPPORT_PUBLIC_WIKI_SENTENCE | This repeats the same 0901.1880 low-redshift winds-insufficient caution already kept via 28075; leaving it archival avoids double-counting the same source/span. |
| 28114 | 1203.2926v2 | rejected | None | background_only | MUST_NOT_SUPPORT_PUBLIC_WIKI_SENTENCE | The row is about radiation pressure from young stars in clusters and starburst disks; it is star-cluster feedback background, too far from the page-57 AGN/quenching successor claims. |
| 28118 | 1203.2926v2 | rejected | None | background_only | MUST_NOT_SUPPORT_PUBLIC_WIKI_SENTENCE | The row describes a simulation code applying an outward radiation force to star-forming clumps; it is implementation detail, not evidence for a visible successor claim. |
| 28127 | 2403.17145v1 | rejected | None | background_only | MUST_NOT_SUPPORT_PUBLIC_WIKI_SENTENCE | This line describes the standard cooling-then-AGN cycle, which the maintenance claim is already covered for by two better lines from the same paper. Keep it archived to avoid overloading one claim with one source. |
| 28139 | 2403.17145v1 | rejected | None | background_only | MUST_NOT_SUPPORT_PUBLIC_WIKI_SENTENCE | This line sets up why groups are useful to study feedback, but it's general background and overlaps stronger lines already kept. Archive to avoid stacking the same paper on one claim. |
| 28143 | 2403.17145v1 | rejected | None | background_only | MUST_NOT_SUPPORT_PUBLIC_WIKI_SENTENCE | This line says AGN can blow gas out of small (group-sized) halos. That's not the 'massive galaxy' outflow claim, and its main point (feedback matters most in certain halos) is already kept from another line. Archive it. |

## Source groups

| source group | rows | accepted/limited | rejected | target claims |
|---|---|---|---|---|
| arxiv:0901.1880 | 28075, 28110, 28131 | 28075, 28131 | 28110 | 2945, 2947 |
| arxiv:1203.2926 | 28114, 28118 | none | 28114, 28118 | none |
| arxiv:1507.06366 | 28082 | none | 28082 | none |
| arxiv:1706.08987 | 28141 | 28141 | none | 2943 |
| arxiv:2009.11175 | 28087, 28095, 28108, 28111, 28133 | 28087, 28095, 28108, 28111, 28133 | none | 2942, 2943, 2947 |
| arxiv:2111.01801 | 28140 | 28140 | none | 2943 |
| arxiv:2403.17145 | 28123, 28127, 28139, 28143, 28151, 28158 | 28123, 28151, 28158 | 28127, 28139, 28143 | 2942, 2946 |
| arxiv:2508.06707 | 28062, 28089, 28144 | 28062, 28089, 28144 | none | 2943, 2946, 2947 |
| arxiv:2512.05584 | 28066, 28069, 28070, 28073 | 28066, 28069, 28073 | 28070 | 2944, 2945 |
| arxiv:2512.21927 | 28076, 28080, 28083, 28084 | none | 28076, 28080, 28083, 28084 | none |
| arxiv:2604.15438 | 28060, 28074, 28091, 28155 | 28060, 28074, 28091, 28155 | none | 2942, 2943 |
| arxiv:2604.22922 | 28148 | 28148 | none | 2943 |
| arxiv:2605.03008 | 28088 | 28088 | none | 2944 |

## Next safe gate

`APPROVE METHOD2 P2 DOCS-ONLY CLAIM-STATUS LEDGER FROM ACCEPTED SOURCE POSITIONS`

P2, if approved later, must use only accepted/accepted-limited rows from this P1 ledger, preserve rejected/no-go rows as blockers, and remain docs-only unless separately approved.

## Safety ledger

- DB writes: 0
- SQL apply/rollback files generated: 0
- Trust recompute: 0
- Live wiki/page_versions publish: 0
- Runtime deploy/restart: 0
- Git commit/push/merge: 0
- Production/cloud/API mutation: 0
- Cross-method/shared-parent edits: 0
