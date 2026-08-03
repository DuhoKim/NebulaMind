# Lana — B3 source-position + adjudication proposal (six rows, one paper)

Coordinator: Hwao/Fable · Relay: Tori/Hermes · Lane: Lana (semantic/source-grounded), read-only proposal.
Written: 2026-07-05, repo `/Users/duhokim/NebulaMind/NebulaMind`.
**Docs-only. No queue edits, no SQL/DB, no apply/rollback, no trust recompute, no prose/wiki publish, no runtime/deploy, no git, no public-cockpit edit. Two output files only. No SQL until all 36 rows decided.**

Companion machine-readable file: `lana_b3_proposal.jsonl` (six objects, one per row, same marker).

## Method / source access

I re-confirmed dependency counts from the pre-edit snapshot: **all six rows are zero on human_votes / comments / element_links** — none is parked for dependencies and none requires a new claim. I read arXiv **2403.17145** at abstract level and confirmed via WebFetch that it is a **review article — "Galaxy groups as the ultimate probe of AGN feedback"** whose own core work is **observational** (the X-GAP XMM program on 49 groups). Per the zone-caution rule, review sentences are secondary synthesis, not primary measurement, so **all six spans are `abstract_only_verified` and every relink is capped `accepted_limited`** (no full `accepted` without full-text span pinning + a later Hwao gate).

## Per-row reasoning

- **28123 → 2946 · support · relink (KEEP, model-dependence side).** "the choice of the feedback scheme in state-of-the-art hydrodynamical simulations vastly differs from one simulation to the other." Background, but it is direct evidence for 2946's **model-dependence** framing (simulation feedback schemes differ). One of the two kept 2946 spans.
- **28158 → 2946 · support · relink · `gap_card: observational_maintenance_heating` (KEEP, observational side).** "Bubbles of outflowing material… producing pairs of cavities in the hot gas distribution (Bîrzan et al., 2008)." This is the only B3 span that is **observational maintenance-heating** (X-ray cavities), the category the standing gap card tracks. Capped `accepted_limited` because it is a **review-citation of Bîrzan 2008**, not the paper's own X-GAP measurement — so 2946 stays model-bounded until a full-text/own-observation span is pinned and gated.
- **28151 → 2942 · support · relink (KEEP, regime-scope, role-distinct).** "galaxy groups occupy a transitional regime… total feedback energy is comparable to the gravitational binding energy of the gas." This is the review's **own thesis** (not background): feedback impact is halo-mass-regime dependent. Supports 2942's "real but scoped, not universal" framing; capped limited (review-level).
- **28127 → archival · `leave_archival` (redundant_same_paper).** Cooling-AGN duty-cycle loop — background maintenance description already covered on 2946 by 28123 + 28158.
- **28139 → archival · `leave_archival` (redundant_same_paper).** "groups retain a hot IGrM… SMBH outflows produce discernible effects" — general motivational background, redundant with the two kept 2946 spans.
- **28143 → archival · `leave_archival` (redundant_same_paper + scope mismatch).** "for low-mass systems… AGN feedback is sufficient to unbind gas particles and eject them from the halo." Its regime point overlaps 28151, and its **low-mass-halo scope does not match 2943's 'selected massive or AGN-host galaxies'** — so it is not a clean 2943 support; archived rather than topic-matched.

## Same-paper stacking summary (R1)

Six rows from one review paper, with 2946 in every option set. To avoid six same-paper supports piling onto 2946, I kept **only role-distinct spans and spread them across three claims**:

- **2946 — exactly two, role-distinct:** 28123 (model-dependence) + 28158 (observational/gap-card). Together they represent the two sides of 2946's own tension (model-dependent now, observational evidence emerging), not two copies of the same point.
- **2942 — one:** 28151 (regime-sensitivity thesis).
- **Archived redundant (3):** 28127, 28139, 28143.

No claim receives more than two spans from this paper, and the two on 2946 are genuinely distinct in role (following the B2 28108 precedent).

## Observational-heating gap-card summary (R2)

- **28158 is flagged `gap_card_relevant: observational_maintenance_heating`** — X-ray cavities/bubbles are observational maintenance-heating, the category 2946's evidence set currently lacks.
- Kept **capped `accepted_limited`**, not upgraded to full accepted, because the span cites Bîrzan et al. 2008 (secondary synthesis) rather than the review paper's own X-GAP measurement.
- **Backlog note (on 28158):** the paper's own X-GAP program (49 groups, XMM) may provide primary observational maintenance-heating measurements; a full-text pass could pin a paper-own observational span that, if Hwao later gates it, could durably move 2946 off model-bounded. Recorded, not acted on.

## Parked / blocker rows

**None.** All six rows have zero dependencies and none requires a new claim. The three archival decisions are adjudications (redundant/scope-mismatch), not blockers.

## No-write ledger

- Queue edits: 0 · SQL/DB queries or connections: 0 · SQL/apply/rollback files: 0 · trust recompute: 0 · prose/wiki publish: 0 · runtime deploy/restart: 0 · git: 0 · public-cockpit edits: 0
- Source access: public arXiv abstract (2403.17145) via read-only WebFetch. Files written by Lana: 2 (this report + `lana_b3_proposal.jsonl`, 6 rows, all carrying the marker).

LANA_B3_SOURCE_POSITION_PROPOSAL_20260705T044944Z
