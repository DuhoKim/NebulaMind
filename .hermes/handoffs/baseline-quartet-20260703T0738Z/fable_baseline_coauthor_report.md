# Fable Baseline Co-author Report

Task: THE_BASELINE_QUARTET_PRIMITIVE_WRITE_20260703T0738Z · Lane: Fable (outside doctrine co-author) · Status: COMPLETE — proposed text only; I did not edit the canonical plan or board; Hermes integrates. Docs-only, zero mutations, only this report written.

Below is my proposed section for The Baseline, written to be pasted as-is. It states the doctrine in plain English, gives the pipeline as numbered steps anyone can follow, names the rejections, and names the next required artifact.

---

## PROPOSED TEXT FOR "THE BASELINE" — begins here

# The Baseline: how NebulaMind turns papers into prose

## The rule

**NebulaMind turns papers into a ledger before it turns them into prose.**

A ledger entry is one assertion with its scope, its method, its certainty, and its receipts — exact quoted spans from identified papers. Status and debate are computed from the ledger. Prose is a rendering of the ledger. Claims, evidence rows, and trust scores are derived afterwards and must reconcile back to it.

Three consequences, stated bluntly:

1. **Sentences are not the unit of truth.** A sentence with no ledger entry behind it is decoration, and decoration does not ship.
2. **Prose may never sound more certain than the ledger.** If the ledger says "observed in 46% of one z~2 sample," the prose may say *can* and *in a substantial subset* — it may not say *does* and *generally*.
3. **Updates flow one way: papers → ledger → prose.** When a sentence and the ledger disagree, the sentence changes. Searching for papers to rescue a sentence is forbidden by name.

The pipeline in one line: **papers → claim/status ledger → research-status/debate map → prose → derived claims/evidence/trust.**

## The pipeline, step by step

Follow these steps in order for every section of every page. Do not skip a step; do not start a step before the previous one passes.

**Step 0 — Corpus protocol (before touching any paper).**
Write down, in one file: the question the section answers; the coverage cells you must fill (mechanism, prevalence, dominance/attribution, alternatives/countercases, method limitations); the search queries per cell; and the inclusion/exclusion rules. Then record flow counts as you go: how many papers found → screened → eligible → included, with a one-line reason for every exclusion.
*Pass condition:* every coverage cell has papers, including the countercase cell. A pile of recent papers is not a corpus; a corpus is what the protocol says survived it.

**Step 1 — Read and extract with receipts.**
For each included paper: get full text where possible (label abstract-only rows as such, permanently); pull candidate spans (exact quotes with paper ID + location); tag each span with its rhetorical zone (background / related-work / method / finding / interpretation) and its evidence type (review / observational sample / single case / simulation / theory).
*Pass condition:* every span has paper + location + zone + type. An introduction saying "AGN feedback is thought to quench galaxies" is background, not a finding — the zone tag is what stops us quoting it as one.

**Step 2 — Assemble the ledger.**
Convert spans into atomic entries. Each entry has: the assertion (one claim, no compounds); modality (established / likely / may / contested / no-info); scope (population, sample size, redshift, mass, environment, simulation context); epistemic type and method; its evidence spans; stance links to other entries (supports / qualifies / contradicts); certainty dimensions (directness, consistency, precision, model-dependence, sample size); and generalization links ("expels gas (universal)" and "expels gas in ~46% of massive z~2 galaxies" are two linked entries, never one blurred sentence).
*Pass condition:* no entry without a span; no compound assertions; duplicates merged; scope fields filled or explicitly unknown.

**Step 3 — Compute status and debate.**
From the ledger, not from memory: for each axis of the section, derive the status — established / emerging-sample-limited / actively debated / contradicted-or-model-dependent — and write the debate map with named positions and the papers holding them. "Consensus" requires multiple independent groups AND zero unresolved contradicting entries AND an answer to "who would disagree, and are they in the corpus?"
*Pass condition:* every status is traceable to entries; "actively debated" is a publishable result, not a failure.

**Step 4 — Apply the wording contract.**
Certainty determines the strongest language a sentence may use:

| Ledger certainty | Allowed wording |
|---|---|
| High, multi-source, consistent | "is / are / does" |
| Moderate, mostly consistent | "probably / appears to" |
| Mechanism shown, or small-N | "can / may / in this sample" |
| Single case | "shows this can occur" — never "is common" |
| Mixed / contested | "evidence is mixed / actively debated" |
| Simulation-only | "in simulations, …" — never stated as observed frequency |

*Pass condition:* zero sentences above their certainty ceiling.

**Step 5 — Render the prose.**
Only now. Every sentence binds to one or more ledger entries by ID. Debates are written into the topical text with named positions, not hidden in scores or shunted to a ghetto section. Each paragraph tells the reader: what the field thinks, how strongly, based on what, and where it is contested — dated ("as of 2026").
*Pass condition:* no orphan sentences (a sentence with no entry ID fails the packet).

**Step 6 — Adversarial audit, then the gates.**
An independent pass hunts: orphan sentences; over-scoped wording; missing countercases; simulations stated as observations; prevalence language without a fraction/sample behind it; quote-mined background spans. Only after this passes does the work go to the operator as a docs-only preview, and only after operator approval does a separate exact-diff packet (with backup, rollback, pinned postconditions, and its own execution phrase) touch the database. Derived claims, evidence attachments, and trust recomputes ride that packet and must reconcile to the ledger.

## What we reject, by name

- **Claim rescue** — hunting for evidence to save a sentence already written. The 2299 episode is the canonical example: the honest fix was editing the sentence, not three packets of searching.
- **Topic-match evidence attachment** — a paper being *about* the subject is not support; only a rationale span is. (This is how the corpus accumulated thousands of decorative evidence rows.)
- **Free abstractive summarization as grounding** — model prose that sounds right while dropping scope, certainty, or contradiction. Allowed only as drafting assistance over a finished ledger.
- **Consensus percentages** — "82% of papers agree" computed over a biased retrieval set manufactures false consensus. Named positions with named papers instead.
- **Trust scalars as reader-facing truth** — scores are internal diagnostics; readers get status labels and debate prose.
- **Recency/feed dumps as corpora** — a pile of this month's papers is a feed, not a field.
- **Single-pass "read everything and write"** — no audit trail, no receipts; brainstorming only.
- **Metric chasing** — no task may have "raise the score / widen the margin" as its objective; scores move as a consequence of honest content or not at all.

## Tripwires anyone may pull

Any Quartet member or the operator halts work by naming one of these, no justification needed beyond the name: *rescue search* · *orphan sentence* · *scope inflation* · *feed-dump corpus* · *false consensus* · *quote-mined zone* · *simulation-as-observation* · *score chasing*. A pulled tripwire is a finding to record, never an argument to lose.

## The next required artifact

**Claim Ledger Contract v1, with the AGN worked example.** One schema file (the entry fields above, plus the wording-contract table as machine-checkable rules) and one JSONL populated from the 26 already full-text-checked AGN papers — including, as the demonstration case, the claim-2299 trio: a mechanism entry (*AGN feedback can expel and heat gas — observed and simulated*), a prevalence entry (*outflow signatures in a substantial subset, e.g. ~46% of massive z~2 galaxies*), and a debate entry (*dominance relative to stellar feedback, environment, and recycling: actively debated*), linked by generalization/specialization.

No Galaxy Evolution prose is planned, drafted, or published until that contract exists and passes review. The ledger is the baseline; everything else renders from it.

## PROPOSED TEXT ENDS — Hermes integrates into the canonical plan and board mirror

---

Integration notes for Hermes (not part of the proposed text): the section is consistent with the integration report's G0–G6 (my Steps 0–6 map onto them one-to-one) and with the eight AGN worked-example seed entries it lists; the wording-contract table is lifted to match its G4 examples so the plan and the survey never diverge; the tripwire vocabulary matches the failure modes already named across the doctrine lineage, so cockpit alarms can reuse the same words.

FABLE_BASELINE_COAUTHOR_DONE_20260703T0738Z
