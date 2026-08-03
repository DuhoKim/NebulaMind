# Lana-DMW P1 sentence-plan review

Request marker: GALAXY_EVOLUTION_METHOD3_P1_REVIEW_REQUEST_20260706T150253Z
Lane report marker: GALAXY_EVOLUTION_METHOD3_P1_REVIEW_LANA_20260706T150253Z

Role/lane: Lana-DMW — science/prose reviewer (semantic accuracy, reader-facing clarity, overclaim risk).

Reviewed (read-only):
- `frontend/public/agent-reports/wiki-method-results/galaxy-evolution/debate-map-to-wiki-rebuild/p1-debate-map-sentence-plan.md`
- `frontend/public/agent-reports/wiki-method-results/galaxy-evolution/debate-map-to-wiki-rebuild/p1-debate-map-sentence-plan.json`
- `.hermes/handoffs/galaxy-evolution/method3/P1_SENTENCE_PLAN_VALIDATION_20260706T145501Z.md`

---

## Verdict: PASS_WITH_PATCHES

The sentence plan is scientifically sound, faithfully preserves all seven debate-map axis statuses, keeps overclaim risk low with a strong "not allowed" guard list, and does **not** prematurely bind citations or claim chips. It is fit to proceed to the next Method3 gate. The patches below are **non-blocking refinements** to fold in at the prose-drafting pass — none require blocking or re-issuing the plan.

---

## Reader clarity assessment

Strong overall. The S01→S12 arc is a coherent reader journey: orient → frame quenching → scoped AGN mechanism → observational evidence → mode distinction → reservoir caution → dominance debate → alternatives → redshift/sample scope → simulation scope → takeaway → open questions. A newcomer can follow it without a single-cause misread, and each sentence role has an explicit wording guard.

Clarity watch-items (addressed in patches):
- **S08 density.** One sentence role carries ~9 pathways (central structure, BH/bulge correlations, halo/satellite environment, strangulation, stripping, stellar feedback, recycling, gas retention, low SFE). The plan already flags a possible split; recommend committing to it so the reader is not hit with a list-dump. See Patch P1.
- **"Starvation" vs "strangulation" collision.** S03 uses "starvation" as an AGN-driven mechanism; S08 uses "strangulation" as an environmental channel. Both mean "cut off / consume the gas supply" and readers routinely conflate them. See Patch P2.
- **Observational-vs-model thread.** S05/S06/S10 all trade in "modes/models"; a single connective cue in prose ("observationally… ; in simulations…") would keep the reader oriented. Folded into Patch P3.

## Science / semantic overclaim risks

Overclaim risk in the plan is **low** — the "Not allowed in the next prose pass" list directly closes the main traps (universal AGN quenching, selected-sample→population rate, single-case→prevalence anchor, mode-merging, simulations-as-observations, dropping alternatives, premature binding). Debate-map status is preserved axis-by-axis:

- mechanism_ejective_feedback (widely_supported, scoped) → S03 keeps "selected systems." Preserved.
- outflow_prevalence_frequency (emerging_sample_limited) → S04 + S09 keep sample/tracer/redshift scope. Preserved.
- dominance_debate (actively_debated) → S07 keeps dominance as context-dependent. Preserved.
- maintenance_heating_prevention (model_dependent) → S05/S10 mark model-dependence. Preserved (see underclaim note, Patch P3).
- reservoir_response (actively_debated) → S06 keeps "both matter." Preserved.
- alternatives_countercases (widely_supported) → S08 keeps alternatives as real pathways. Preserved.
- simulation_model_scope (model_dependent) → S10 marks model-bounded. Preserved.

Residual semantic risks (all non-blocking):
1. **Underclaim mirror on maintenance heating (S05/S10, axes 4/7).** The "contradicted_or_model_dependent" label is correct for *galaxy-scale preventive-heating prevalence*, but if prose lets "model-dependent" blanket the concept, it risks *understating* the observational maintenance-mode grounding in massive halos/clusters (X-ray cavities, cooling-flow suppression). An overclaim guard should not silently become an underclaim. See Patch P3.
2. **Causal-vs-correlational for BH/bulge (S08).** The plan correctly uses "correlations"/"predictors"; prose must keep BH–bulge (e.g. M–σ-type) relations as correlations/predictors, not as established causal quenching channels. See Patch P5.
3. **Meta-editorial "safest synthesis" (S11).** Framing the takeaway as the "safest" synthesis reads as editorial hedging rather than a scientific conclusion. Prefer a state-of-the-field framing. See Patch P4.

## Exact patch requests (recommended; I did not and will not edit the plan)

- **P1 — Clarity, S08 split.** Split the S08 "Alternatives" role into two ordered roles: S08a *internal/mass-linked* (central structure; BH/bulge correlations as predictors; low SFE; gas retention; recycling) and S08b *environment-linked* (halo/satellite environment; strangulation; ram-pressure/tidal stripping). Keep both as real pathways per the existing guard. Update the JSON `sentence_plan` count/note accordingly.
- **P2 — Semantics, terminology disambiguation.** Add a plan note under S03/S08: distinguish AGN-driven *starvation/preventive suppression of accretion* (S03/S05) from *environmental strangulation* (S08b); do not treat the two as synonyms in prose.
- **P3 — Semantics, scope the "model-dependent" label (S05/S10; axes 4/7).** Add a guard: "'model-dependent' applies to galaxy-scale preventive-heating *prevalence*; do not word prose to deny observational maintenance-mode evidence in massive halos/clusters." Pair with a connective cue separating observational vs simulation statements across S05/S06/S10.
- **P4 — Wording, S11 takeaway.** Replace "the safest synthesis is…" with a state-of-the-field framing, e.g. "current evidence supports a context-dependent, multi-channel account of quenching," retaining the context-dependent/sample-dependent/multi-channel guards.
- **P5 — Preserve-in-prose note, S08.** Explicitly tag BH/bulge relations as correlational predictors, not causal quenching mechanisms, so the causal/correlational line is not lost when prose is written.

## Citation / claim-chip binding check (brief focus)

PASS. Every sentence defers citations via its "Later binding need"; the "Not allowed in the next prose pass" list and the P1 stop-state both prohibit binding citations, evidence IDs, product claim chips, or live wiki rows during P1. The plan holds this line cleanly. No premature binding observed.

---

## Hard-stop acknowledgement

NO ACTIVE EXECUTION PHRASE. This review is docs-only. I performed no product/wiki publish, no live wiki/page_versions update, no DB write, no SQL apply/rollback, no migration, no trust recompute, no backend/API or service restart, no production write, no git operation, no cloud/API mutation, and no cross-method or shared-parent/alias edits. I did not edit the sentence plan or any file other than this single assigned report. I wrote only:
`/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/method3/reviews/LANA_P1_SENTENCE_PLAN_REVIEW_20260706T150253Z.md`

Stopping after writing this report.
