# Method2/SFA P2 claim/status ledger

Marker: `GALAXY_EVOLUTION_METHOD2_P2_CLAIM_STATUS_LEDGER_20260706T142132Z`

Consumed approval phrase: `APPROVE METHOD2 P2 DOCS-ONLY CLAIM-STATUS LEDGER FROM ACCEPTED SOURCE POSITIONS`
Current safety phrase: `NO ACTIVE EXECUTION PHRASE`

## Method Baseline

Start from papers/source positions; only accepted or accepted-limited source roles may support public wiki sentences.

P2 uses only P1 accepted/accepted-limited source positions for claim binding. P1 rejected rows and non-support-eligible rows remain preserved in the no-go/gap ledger.

## Result

- Claim units: `6`
- Citation-role mappings from support-eligible source positions: `22`
- P1 accepted/accepted-limited rows not used as claim support: `2`
- P1 rejected rows preserved: `12`
- NO-GO/gap ledger rows including overclaim guards: `32`

## Claim/status rows

| claim unit | status | source positions | primary | allowed wording |
|---|---|---:|---|---|
| METHOD2-P2-CU-2942 | accepted_limited_for_docs_claim_status | 4 | 28151 | Use “can be” / “is a scoped pathway” / “appears regime-dependent”; do not say AGN feedback universally quenches galaxies. |
| METHOD2-P2-CU-2943 | accepted_for_docs_claim_status_with_scope_limits | 5 | 28141 | Use “can drive” / “has been observed in selected systems”; keep “selected” and “tracer/sample dependent”; do not present prevalence or universal gas removal. |
| METHOD2-P2-CU-2944 | accepted_limited_for_docs_claim_status_partial_support | 3 | 28069, 28088 | Use “other mechanisms and qualifiers matter” and name only the alternatives actually supported by accepted rows unless later sources support broader lists. |
| METHOD2-P2-CU-2945 | accepted_limited_for_docs_claim_status | 2 | 28066, 28075 | Use “requires caution,” “can fall back,” and “may be insufficient”; do not claim gas removal is always absent or always decisive. |
| METHOD2-P2-CU-2946 | accepted_limited_for_docs_claim_status | 3 | 28123, 28158 | Use “distinct from ejective outflows,” “model-dependent,” and “limited observational hot-gas evidence”; do not convert simulations into observed prevalence. |
| METHOD2-P2-CU-2947 | accepted_limited_for_docs_claim_status | 5 | 28095, 28111 | Use “can mechanically couple” and “context-dependent”; include uncertainty/weak-coupling caveats; do not call it a population-wide quenching channel. |

## Citation-role mappings

| claim unit | evidence | arXiv | role | epistemic type | source role |
|---|---:|---|---|---|---|
| METHOD2-P2-CU-2942 | 28074 | 2604.15438 | secondary_claim_support | observational_case | support |
| METHOD2-P2-CU-2942 | 28087 | 2009.11175v1 | secondary_claim_support | review_synthesis | support |
| METHOD2-P2-CU-2942 | 28151 | 2403.17145v1 | primary_claim_support | review_synthesis | support |
| METHOD2-P2-CU-2942 | 28155 | 2604.15438 | secondary_claim_support | simulation_model | support |
| METHOD2-P2-CU-2943 | 28091 | 2604.15438 | secondary_claim_support | review_synthesis | support |
| METHOD2-P2-CU-2943 | 28140 | 2111.01801v2 | secondary_claim_support | simulation_model | support |
| METHOD2-P2-CU-2943 | 28141 | 1706.08987v2 | primary_claim_support | observational_sample | support |
| METHOD2-P2-CU-2943 | 28144 | 2508.06707v1 | secondary_claim_support | observational_sample | support |
| METHOD2-P2-CU-2943 | 28148 | 2604.22922 | secondary_claim_support | observational_sample | support |
| METHOD2-P2-CU-2944 | 28069 | 2512.05584v2 | primary_claim_support | review_synthesis | support |
| METHOD2-P2-CU-2944 | 28073 | 2512.05584v2 | secondary_claim_support | source_position_synthesis | support |
| METHOD2-P2-CU-2944 | 28088 | 2605.03008v1 | primary_claim_support | simulation_model | limitation_or_caution |
| METHOD2-P2-CU-2945 | 28066 | 2512.05584v2 | primary_claim_support | source_position_synthesis | limitation_or_caution |
| METHOD2-P2-CU-2945 | 28075 | 0901.1880v2 | primary_claim_support | source_position_synthesis | limitation_or_caution |
| METHOD2-P2-CU-2946 | 28089 | 2508.06707v1 | secondary_claim_support | simulation_model | support |
| METHOD2-P2-CU-2946 | 28123 | 2403.17145v1 | primary_claim_support | simulation_model | support |
| METHOD2-P2-CU-2946 | 28158 | 2403.17145v1 | primary_claim_support | simulation_model | support |
| METHOD2-P2-CU-2947 | 28062 | 2508.06707v1 | qualifier_or_caution | source_position_synthesis | limitation_or_caution |
| METHOD2-P2-CU-2947 | 28095 | 2009.11175v1 | primary_claim_support | source_position_synthesis | support |
| METHOD2-P2-CU-2947 | 28108 | 2009.11175v1 | qualifier_or_caution | source_position_synthesis | limitation_or_caution |
| METHOD2-P2-CU-2947 | 28111 | 2009.11175v1 | primary_claim_support | simulation_model | support |
| METHOD2-P2-CU-2947 | 28131 | 0901.1880 | secondary_claim_support | source_position_synthesis | support |

## Preserved no-go/gap ledger

P2 does not restore rejected rows, background-only rows, positive-feedback caution rows, duplicate rows, or overclaim strings as support. See `P2_NO_GO_GAP_LEDGER_20260706T142132Z.jsonl` for row-level details.

## Next safe gate

`APPROVE METHOD2 P3 DOCS-ONLY WIKI PROSE PACKET FROM CLAIM-STATUS LEDGER`

P3, if approved later, remains docs-only and must bind every sentence to this P2 claim/status ledger and citation-role mapping. Product/wiki DB ingest remains a separate explicit gate.

## Safety ledger

- DB writes: 0
- SQL apply/rollback: 0
- Migration: 0
- Trust recompute: 0
- Live wiki/page_versions publish: 0
- Runtime deploy/restart: 0
- Commit/push/merge: 0
- Production/cloud/API mutation: 0
- Cross-method/shared-parent edit: 0
