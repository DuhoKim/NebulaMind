# Lana — B2 source-position + adjudication proposal (four rows)

Coordinator: Hwao/Fable · Relay: Tori/Hermes · Lane: Lana (semantic/source-grounded), read-only proposal.
Written: 2026-07-05, repo `/Users/duhokim/NebulaMind/NebulaMind`.
**Docs-only. No queue edits, no SQL/DB/apply/rollback, no prose/wiki publish, no runtime/deploy, no git. Two output files only. No SQL until all 36 rows are decided.**

Companion machine-readable file: `lana_b2_proposal.jsonl` (four objects, one per row, same marker, ready for Tori to apply only after the Hwao gate).

## Method

I reused the batch-1 paper context (arXiv 2009.11175 = "AGN-driven outflows in young radio galaxies"; arXiv 2604.15438 = SWAN M51 IV) and read each B2 snippet in the queue's pre-edit snapshot. **All four rows have zero dependency counts** (human_votes 0, comments 0, element_links 0), so none is parked for dependency handling and none needs a new claim. Source access was **abstract-level** for all four (the specific spans are body sentences I did not full-text pin), so — per the binding rules — every visible-successor relink is capped at `accepted_limited`, never full `accepted`, and I applied zone honesty (background/discussion spans labelled and capped).

## Per-row reasoning

- **28087 → 2942 · support · accepted_limited · relink.** Span: "the AGN feedback effect is likely to be complex, involving a range of physical mechanisms on different spatial scales." A background complexity caveat — it directly reinforces 2942's "real but scoped, not universal" framing. Capped limited: a general caveat, not a measurement, abstract-only. Confidence medium.

- **28108 → 2947 · limitation_or_caution · accepted_limited · route_kinetic_radio.** Span: jets acting on the cooler ISM are "not yet fully understood," with "considerable uncertainties about the masses and kinetic powers of the resulting jet-induced outflows." Kinetic/radio-mode topic (2947), but an **uncertainty/open-question** statement — so its honest role is *caution*, not support. See stacking judgment below. Confidence medium.

- **28133 → (candidate 2943) · background_only · accepted_limited · leave_archival.** Span: "This has important implications for estimates of key outflow parameters such as the mass outflow rates, kinetic powers, and AGN feedback efficiencies." This is about **measuring** outflow parameters, not about outflows suppressing star formation, so it does **not** support 2943's ejective-removal claim. Relinking it as support would be topic-matching (the exact anti-pattern the campaign guards against). I propose `leave_archival` rather than a false support relink. Confidence medium.

- **28074 → 2942 · support · accepted_limited · relink (2947 noted as full-text alternative).** Span: "Unlike multiple indicators of kinetic feedback, the AGN is not in a radiative efficient mode of feedback, based on Chandra and NuSTAR observations that point to a Compton thick accretion with a low Eddington ratio." A source-specific classification: M51's AGN operates in a kinetic (not radiative) mode. It supports 2942's scoped/heterogeneous framing (one object's specific mode); it is also kinetic-relevant (2947). Kept accepted_limited: single-object mode classification, abstract-only. I flag 2947 as an alternative kinetic link a full-text pass could justify. Confidence medium.

## The 28108 stacking judgment

If 28108 routes to 2947, it would be the **third row from the same paper (2009.11175)** on 2947, alongside batch-1's 28095 and 28111, on top of 2947's live kinetic evidence 26681–26685. Three same-paper spans on one claim risks over-weighting a single source.

**Judgment:** 28108 adds a **genuinely distinct role** — a *caution* about the uncertain masses/kinetic powers of jet-induced outflows — whereas 28095 and 28111 are *supports*. Routed as `limitation_or_caution` (not support) and capped `accepted_limited`, it **improves the evidence balance** on 2947 (which otherwise carries only supports) rather than piling on more support-weight. That is the honest outcome, so I route it as a limited caution rather than parking it. Its `duplicate_check_against_successor_evidence_ids` records `[26681–26685, 28095, 28111]` and its dedup status is `resolved_same_paper_role_distinct_capped_limited`. **If the operator prefers strict same-paper de-duplication, the safe fallback is `leave_archival`** — flagged so Hwao/Tori can downgrade at the gate.

## Source access level per row

- 28087, 28108, 28133 — arXiv 2009.11175, `abstract_only_verified` (batch-1 abstract context; body spans not full-text pinned).
- 28074 — arXiv 2604.15438 (SWAN M51 IV), `abstract_only_verified`.
All four capped at `accepted_limited`; none reaches full `accepted` (no full-text span pinning). A later full-text pass could upgrade 28074 (M51 kinetic-mode) and re-home 28108/28074 to 2947 if warranted.

## Parked / blocker rows

**None parked for dependencies** (all four have zero votes/comments/element-links) and **none requires a new claim**. `28133` is proposed `leave_archival` (a decision, not a block) because it is a methods/implications sentence rather than support for 2943. `28108` carries a documented stacking judgment with a `leave_archival` fallback for the operator.

## Confirmation

No queue edit, no SQL/DB connection, no apply/rollback file, no prose/wiki publish, no runtime/deploy, no git. Two files written: this report + `lana_b2_proposal.jsonl` (4 rows, all carrying the marker).

LANA_B2_SOURCE_POSITION_PROPOSAL_20260705T041354Z
