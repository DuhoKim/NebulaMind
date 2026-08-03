# Hwao/Fable Doctrine Report — Step 8 docs-only prose preview

Task: HWAO STEP 8 adversarial doctrine review · Status: COMPLETE — read-only except this report; no generic NLI; no model downloads; no DB/product/git; nothing mutated.
Verified directly: the full preview draft (all 16 sentences read against the ledger entries I have reviewed line-by-line across this campaign), the binding table, the B1-prime attention audit JSON (structure inspected), validation facts.

## Verdict: `PASS_WITH_PATCHES` — four patches, none blocking; the doctrine held at first contact with prose.

Before the attack, the finding that matters most: **this preview is the 2299 arc landing.** S016 renders "AGN feedback can remove or deplete star-forming fuel in selected systems, while prevalence, reservoir response, and dominance remain constrained…" — the exact prevalence-qualified, debate-aware sentence the operator's correction demanded, produced *by the pipeline* rather than by hand. Every sentence is bound, no orphans, no modality overflows, fractions are tracer-scoped and unblended (S005/S006 are exemplary — 17%-of-AGNs vs 46%-of-massive-galaxies with "not a combined prevalence" stated), the single-case guard renders correctly (S003 names GS-10578 and blocks it as a prevalence anchor), the reservoir axis I forced into Step 6 does its job (S010–S012: central-kpc scoping + retention counter), and simulations are fenced twice (S014–S015 at `in_model_only` with "cannot by themselves establish observed…").

## Attack results per brief target

- **Overclaiming / universality:** none found. The strongest declaratives are correctly confined to the debate framing itself (S007–S008) at `mixed_debated`.
- **Evidence rescue:** none — the preview renders the *corrected* 2299 story; no sentence reaches beyond its bound entries.
- **False consensus:** none — dominance is rendered as a named-position debate (S008 lists central/bulge/BH, halo/environment, satellite, strangulation/stripping, retention, SF-driven outflows).
- **Simulation-as-observation:** **one subtle leak, at citation level (Patch 2).** S002 begins "Observations show that…" but its source list includes `2012MNRAS.420.2662D` — a simulation paper (Dubois jet-heating), inherited via the mechanism entry's qualifier links. The wording is capped correctly and three observational sources genuinely carry the sentence, but a reader checking sources under "Observations show" would meet a simulation. This is exactly the leakage class the brief names, and it passed because the validator checks tiers, not source-epistemic consistency.
- **Dominance leakage:** none; S009 keeps the SF-driven counter scope-specific ("typical low-redshift galaxies… may be").
- **Reservoir overreach:** none — the axis renders with both halves of the tension.
- **Step 10 / product-gate creep:** boundary is stated and the gate is locked, but there is a **latent creep path (Patch 1)**: six sentences are written in *pipeline voice*, not reader voice — S001 "In the current ledger…", S003 "the ledger blocks…", S007 "the strongest wording the current map allows…", S012 "…would overstate the ledger", S014 "In this worked corpus…", S016 "A safe Galaxy Evolution rendering would therefore present…". For a docs-only preview this is honest and even helpful; the creep risk is a future reader treating "Step 8 PASS" as "this text is product-ready copy." It is not — and the de-voicing pass that will someday make it reader-facing can smuggle modality changes if it is treated as cosmetic.

## The four patches

1. **Voice classification + de-voicing rule.** Tag each sentence `reader_voice` or `pipeline_voice` in the bindings JSONL (six pipeline-voice sentences listed above). Add one line to the preview and the validation: *"Step 8 PASS certifies bindings and caps for THIS text; any product-facing rendering requires a de-voicing pass in which every reworded sentence is re-bound and re-validated — de-voicing is a content change, not a cosmetic one."* This closes the Step-10 creep path.
2. **Epistemic-consistency rule for source lists.** Fix S002 (drop `2012MNRAS.420.2662D` from its source list, or reword to "Observations and simulations show… can"). Add the machine-checkable validator rule: *a sentence whose text attributes support to observations may not list bibcodes whose ledger epistemic type is `simulation`* — the ledger already carries the epistemic types, so Goru can enforce this mechanically forever.
3. **"Unflagged ≠ cleared" line in the attention audit.** The B1-prime audit flags 11 of 16 sentences; the 5 unflagged sentences must not receive reduced review. Verified the audit is genuinely additive (authority `attention_additive_only`, `auto_stance_assignments: 0`, `gate_authority: false`, per-flag status `attention_only_reviewed_no_auto_stance`, no stance strings anywhere) — add the one sentence so absence-of-flag is never read as clearance.
4. **Missing "as of" date.** The Baseline's Step 6 dating requirement carries into prose; the preview text has no as-of stamp. Add "as of mid-2026" (or the map's `as_of`) to the slice preamble or S016.

## Review-question answers (this lane)

1. Every sentence within bound entries/map/contract — **yes** (spot-verified against the ledger entries; tiers match entry certainties; 0 orphans/overflows per validation). 2. Too strong/universal/falsely dominant — **no**; nearest miss is the S002 citation-level issue. 3. Fractions tracer/sample-scoped, unblended — **yes, exemplary**. 4. Reservoir/maintenance/simulation/dominance qualified — **yes** (reservoir axis renders both halves; sims double-fenced). 5. B1-prime attention-additive only — **confirmed at artifact level**, with Patch 3's one-line hardening. 6. Slice-not-full-page stated — **yes, twice**. 7. Step 8 docs-only status — **PASS_WITH_PATCHES**; apply Patches 1–4 (all small; only S002 touches the prose itself) and Step 8 docs-only can be marked complete. Product remains locked behind Steps 9–10 and the operator's exact-diff gate, unchanged.

## Safety ledger

Generic NLI runs 0 · model downloads 0 · DB 0 · SQL 0 · migrations 0 · deploy/restart 0 · product publish 0 · git 0 · exact-diff apply 0 · secrets 0 · files written 1 (this report).

HWAO_STEP8_DOCS_PREVIEW_DOCTRINE_DONE_20260703T1242Z
