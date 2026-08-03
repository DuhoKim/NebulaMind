# Overnight AI-Scientist Paper Board Research Execution Plan

> **For Hermes:** Use Hwao-led bounded lane dispatch to implement this plan task-by-task. This document is a plan, not an execution order. Do not dispatch any lane or mutate any paper/run until the owner approves an exact packet set and hard-stop window.

**Goal:** Use tonight’s subscription-backed model headroom to resolve the highest-value integrity and completeness gaps on the current AI-Scientist paper board, producing isolated local research/candidate artifacts and a morning decision packet without changing current runs or public surfaces.

**Architecture:** Hwao/Fable directs and makes scientific disposition decisions. Lana performs manuscript/scientific review, Goru performs mechanical comparisons and source maps, Kun performs reproducibility/citation checks, and Tori relays and verifies receipts. All work is single-writer and versioned under one new local-only overnight root; the live Lab run records, runner, pipeline board, public PDFs, and product data remain read-only.

**Tech stack:** Existing Python 3 tooling, `tools/nm_gates.py`, `tools/lab_runner_worker.py` conventions, local Ollama/corpus services already used by the Lab runner, AASTeX 6.3.1, `/opt/homebrew/bin/tectonic`, SHA-256 manifests, existing redacted provider-usage feed.

---

## 1. Mode and authorization boundary

This is **PLAN ONLY**.

Writing this plan does not authorize:

- lane dispatch or overnight execution;
- a new cron, launchd job, recurring scheduler, or service;
- edits to `tools/lab_runner_worker.py`, `tools/nm_gates.py`, or `tools/render_pipeline_board.py`;
- edits to any current `.hermes/handoffs/galaxy-evolution/lab-runs/*.json` record or its existing run directory;
- replacing existing candidate/PDF artifacts;
- updating the private dashboard or public Baseline cockpit;
- DB/SQL/API/wiki/page-version/trust writes;
- deploy, restart, git, browser, account, credential, OAuth, billing, payment, or external-submission actions.

The exact approval phrase for the recommended default is:

`APPROVE OVERNIGHT PAPER-BOARD PLAN A+B+C, HOLD D, LOCAL-ONLY, HARD STOP 06:00 KST.`

Any narrower approval may name only the desired packets.

## 2. Scope and current board truth

This plan targets the **current live AI-Scientist Lab pipeline board**:

`https://duho-macstudio.taila27502.ts.net/cockpit/pipeline-board.html`

It does not reopen the older `overnight-9-papers-20260708` swarm. That older board is a read-only precedent for lane separation and safety, not tonight’s target.

Verified current state:

- 8 runs total;
- 5 reached PDF;
- 3 stopped after Study with computed results but no draft/review/citation/PDF stages;
- 2 PDFs have citation-entailment flags;
- 4 records carry `MINOR` review verdicts;
- one PDF has referee text but no normalized `review_verdict`;
- four records overlap the mass-metallicity/chemical-evolution topic, creating duplication risk.

| Run | Project | Current gap |
|---|---|---|
| `2ab3c92eea8a` | TNG100 star-forming main sequence | Computed Study only; no draft |
| `d8de519cb9c9` | TNG100 + SDSS mass-metallicity relation | Computed Study only; no draft; overlaps other MZR runs |
| `e2f3b038f8dd` | Labeled main-sequence/quenching, but result is an SDSS MZR | Study only plus label/result mismatch |
| `gated-e2e-demo` | z=0 TNG100-vs-SDSS gas-phase MZR | PDF + MINOR; 2/4 citations unsupported |
| `gated-halt-demo` | z=0 SDSS star-forming main sequence | PDF + MINOR; 1/2 citations unsupported; expected-value `INSUFFICIENT` |
| `fesc002` | Reionization photon budget | Strongest record: NOVEL, clean citations, PDF + MINOR |
| `2958462772b2` | SDSS cosmic chemical evolution/MZR | PDF + MINOR; overlaps other MZR runs |
| `7cb504ea7ad3` | TNG100 stellar-mass assembly | PDF and referee text, but no normalized verdict |

Read-only source roots:

- Run records: `.hermes/handoffs/galaxy-evolution/lab-runs/*.json`
- Per-run source artifacts: `.hermes/handoffs/galaxy-evolution/lab-runs/<run-id>/`
- Board renderer: `tools/render_pipeline_board.py`
- Lab runner: `tools/lab_runner_worker.py`
- Quality gates: `tools/nm_gates.py`

Proposed new isolated output root, created only after execution approval:

`.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-paper-board-research-20260726/`

All overnight writes must remain below that root.

## 3. Provider allocation and quota policy

Quota snapshot observed from the existing redacted live monitor at approximately `2026-07-26T13:05Z`:

- Claude/Fable/Lana: 3% weekly used;
- Codex/Kun: 0% weekly used;
- Gemini/Goru agent pool: 0.04% weekly used;
- Gemini consumer app: 1% weekly used;
- Hermes/Nous: free plan exhausted, $42.62 paid top-up available.

Use subscription-backed routes only:

- Hwao/Fable and Lana: direct Claude Code subscription lane, not third-party Claude OAuth/PAYG routing;
- Kun: Codex via ChatGPT subscription;
- Goru: Antigravity/Gemini subscription lane;
- Tori: relay, receipt, and local verification only; do not use the paid Nous top-up for bulk research;
- do not use Flow/Veo, YouTube, browser usage pages, or any paid overage path.

Every approved execution must record the redacted meter at T0 and every 30 minutes in:

`overnight-paper-board-research-20260726/quota/usage_<UTC>.json`

Block new starts if any of the following occurs:

- Claude or Codex weekly usage reaches 30%;
- Gemini agent-pool weekly usage reaches 20%;
- the usage feed is more than 10 minutes old or hides exact gauges as stale;
- a lane presents a rate-limit, paid-overage, billing, account, OAuth, or credential prompt;
- useful approved work is complete.

Never spend quota merely to hit a usage percentage.

## 4. Proposed overnight window

Default window if approved promptly:

- T0: `2026-07-26 22:20 KST` (`2026-07-26T13:20Z`) or the actual approval time, whichever is later;
- first director checkpoint: `00:30 KST` (`15:30Z`);
- second director checkpoint: `03:00 KST` (`18:00Z`);
- no new packet starts after `04:45 KST` (`19:45Z`);
- research hard stop: `05:40 KST` (`20:40Z`);
- receipt and morning-rollup hard stop: `06:00 KST` (`21:00Z`).

Late-approval degradation:

- approval after 23:00 KST: drop Packet D and produce only one Packet C candidate;
- approval after 01:00 KST: run Packets A and B, then one readiness memo only;
- approval after 03:00 KST: run Packet B only and write the morning handoff;
- never extend beyond 06:00 KST without a new owner instruction.

Maximum concurrency: three active worker lanes plus Hwao directing. An author may not be its own scientific or reproducibility reviewer.

## 5. Task 0 — Freeze an immutable input baseline

**Objective:** Make the overnight work reproducible and prove that current run records remain unchanged.

**Files to create after approval:**

- `overnight-paper-board-research-20260726/BOARD_SNAPSHOT.json`
- `overnight-paper-board-research-20260726/INPUT_SHA256.txt`
- `overnight-paper-board-research-20260726/OVERNIGHT_LEDGER.md`
- `overnight-paper-board-research-20260726/quota/usage_<T0>.json`

**Steps:**

1. Hwao confirms the approved packet subset and writes it at the top of `OVERNIGHT_LEDGER.md`.
2. Tori/Goru copy only the eight top-level run JSONs into `inputs/run-records/`; do not copy credentials, caches, or unrelated histories.
3. Kun records SHA-256 for each source run JSON and every copied input artifact.
4. Goru writes a machine-readable board snapshot with run ID, topic, method, result summary, reached stages, gates, verdict, and PDF presence.
5. Tori records the redacted usage snapshot and confirms that the runner and board renderer were observed but not touched.

**Validation:**

```bash
python3 -m json.tool overnight-paper-board-research-20260726/BOARD_SNAPSHOT.json >/dev/null
shasum -a 256 -c overnight-paper-board-research-20260726/INPUT_SHA256.txt
```

Expected: JSON parses; every input hash reports `OK`.

**Stop condition:** Any source file changes between initial hash and packet start. Record `INPUT_DRIFT_BLOCKER` and stop; do not choose a newer version silently.

## 6. Packet A — Reconcile duplicate and mislabeled MZR runs

**Hwao priority mapping:** P3; run first because it gates Packet C.

**Objective:** Select one canonical MZR research path and document the other records as complementary, superseded, or mislabeled without editing their source records.

**Primary lane:** Goru mechanical comparison.

**Independent review:** Kun provenance/reproducibility; Hwao scientific disposition.

**Inputs:**

- `e2f3b038f8dd.json`
- `d8de519cb9c9.json`
- `2958462772b2.json`
- `gated-e2e-demo.json`
- each run’s existing result summary, figure/data artifacts, logs, provenance, gates, and review material.

**Files to create:**

- `packets/A-mzr-reconciliation/MZR_RUN_MATRIX.json`
- `packets/A-mzr-reconciliation/MZR_INVARIANT_MANIFEST.json`
- `packets/A-mzr-reconciliation/HWAO_MZR_DISPOSITION.md`
- `packets/A-mzr-reconciliation/KUN_PROVENANCE_CHECK.md`

**Steps:**

1. Compare topic label, method, data sources, sample sizes, calibration, quantitative result, selection, provenance, gates, review, and citation status for all four runs.
2. Explicitly document the `e2f3b038f8dd` mismatch: topic says main-sequence/quenching while the computed result is an MZR.
3. Identify numeric statements that must remain verbatim if any candidate is drafted.
4. Rank the records by provenance completeness, scientific distinctness, cross-survey value, gate quality, and citation cleanliness.
5. Hwao assigns exactly one disposition to each record: `CANONICAL`, `COMPLEMENTARY`, `SUPERSEDED`, `MISLABELED_BLOCKED`, or `UNRESOLVED`.
6. Do not rename, delete, rewrite, or mark any source run record.

**Done marker:** `GE_LAB_MZR_RECONCILE_<T0>` appears in `HWAO_MZR_DISPOSITION.md`, with one canonical MZR record and a specific disposition for all four records.

**Partial marker:** `GE_LAB_MZR_RECONCILE_PARTIAL_<T0>` if provenance cannot distinguish a canonical path. Packet C must then skip `d8de519cb9c9`.

**ETA:** 30–45 minutes.

**Stop condition:** Missing or contradictory provenance. Escalate to Hwao; do not infer from filenames or prose summaries.

## 7. Packet B — Repair citation integrity in isolated candidates

**Hwao priority mapping:** P2; highest-integrity, lowest-risk packet. Run in parallel with Packet A.

**Objective:** Produce isolated citation-clean candidate bodies for the two flagged papers by omitting or narrowing unsupported statements; never attach a merely topical source.

**Primary lane:** Kun citation/provenance review.

**Independent review:** Goru counts and exact-diff check; Lana overclaim/wording review.

**Inputs:**

- `gated-e2e-demo.json` and its current body/literature set;
- `gated-halt-demo.json` and its current body/literature set;
- the existing `gates.citation_entailment.unsupported` and `spot_audit` records.

**Files to create:**

- `packets/B-citation-integrity/gated-e2e-demo/CLAIM_CITATION_LEDGER.json`
- `packets/B-citation-integrity/gated-e2e-demo/CANDIDATE_BODY.md`
- `packets/B-citation-integrity/gated-e2e-demo/CITATION_GATE_RECEIPT.json`
- `packets/B-citation-integrity/gated-halt-demo/CLAIM_CITATION_LEDGER.json`
- `packets/B-citation-integrity/gated-halt-demo/CANDIDATE_BODY.md`
- `packets/B-citation-integrity/gated-halt-demo/CITATION_GATE_RECEIPT.json`
- `packets/B-citation-integrity/KUN_CITATION_REPAIR_SUMMARY.md`

**Steps for each paper:**

1. Extract every cited sentence, key, retrieved passage, support decision, and unsupported reason into the claim/citation ledger.
2. For each unsupported citation, choose only one of: remove the citation, narrow/remove the unsupported clause, or mark `SOURCE_ADDITION_REQUIRED` and stop that sentence.
3. Do not add a new paper or factual claim in this packet.
4. Preserve the exact measured result and every numeric invariant from the input manifest.
5. Run `tools/nm_gates.py:citation_entailment_gate` against the isolated candidate body and the copied existing literature set; save the full receipt.
6. Lana confirms that the repair did not strengthen causal or population-level language.
7. Goru verifies that source records and existing PDFs remain unchanged.

**Done marker:** `GE_LAB_CITATION_REPAIR_<T0>` with `n_unsupported == 0` for both isolated candidate bodies.

**Partial marker:** `GE_LAB_CITATION_REPAIR_PARTIAL_<T0>` if either paper still needs a genuinely new source. Preserve the flag rather than forcing a pass.

**ETA:** 30–45 minutes per paper; 1–1.5 hours total.

**Stop condition:** The only repair would require inventing a bridge claim, changing a measured result, or introducing a new source. Record the blocker for a later research packet.

## 8. Packet C — Advance clean Study outputs to isolated paper candidates

**Hwao priority mapping:** P1; begin after Packet A disposition.

**Objective:** Turn existing computed results into isolated, reviewable AASTeX candidates without advancing or changing the live Lab run records.

**Candidate set:**

- always eligible: `2ab3c92eea8a` (TNG100 star-forming main sequence);
- conditionally eligible: `d8de519cb9c9` only if Packet A names it `CANONICAL` or scientifically `COMPLEMENTARY` rather than duplicate;
- never eligible tonight: `e2f3b038f8dd` until its topic/result mismatch is resolved by a separate source-record decision.

**Author lane:** Lana.

**Independent checks:** Kun compile/reproducibility; Goru numeric-invariant and artifact map; Hwao final scientific review.

**Files to create for each eligible run:**

- `packets/C-study-to-candidate/<run-id>/DRAFT_READINESS.md`
- `packets/C-study-to-candidate/<run-id>/EXPECTED_VALUE_GATE.json`
- `packets/C-study-to-candidate/<run-id>/candidate/draft.tex`
- `packets/C-study-to-candidate/<run-id>/candidate/draft.pdf`
- `packets/C-study-to-candidate/<run-id>/candidate/REVIEW.md`
- `packets/C-study-to-candidate/<run-id>/candidate/CITATION_GATE.json`
- `packets/C-study-to-candidate/<run-id>/candidate/MANIFEST.json`

**Steps:**

1. Copy only the exact computed result, source provenance, existing figure/data artifacts, and immutable numeric statements into the isolated packet.
2. Run the expected-value gate before drafting. A `CONTRADICTS` verdict is a hard stop. `INSUFFICIENT` may proceed only with explicit Hwao caveat language and no expected-value claim.
3. Lana drafts four bounded sections: motivation, data/method, exact result, and caveats. No new measurement or number may be generated from model memory.
4. Include no citation unless its retrieved passage directly entails its sentence.
5. Hwao/Lana review for estimand clarity, calibration scope, selection limitations, and noncausal wording.
6. Kun compiles the isolated AASTeX candidate using the existing compiler convention:

```bash
cd <isolated-candidate-dir>
/opt/homebrew/bin/tectonic -X compile draft.tex
```

7. Kun records compile exit, PDF size, SHA-256, undefined references/citations, and warnings.
8. Goru checks every numeric invariant against `MZR_INVARIANT_MANIFEST.json` or the non-MZR run’s exact input summary.
9. Run the citation-entailment gate on the final isolated body and save the receipt.
10. Hwao assigns `READY_FOR_SEPARATE_INTEGRATION_REVIEW`, `PARTIAL`, or `REJECTED`; no source-run promotion occurs tonight.

**Done marker:** `GE_LAB_STOPPED_STUDY_CANDIDATE_<T0>` with PDF compiled, expected-value not contradictory, citation gate clean, referee verdict at least `MINOR`, and all numeric invariants preserved.

**Partial marker:** Candidate compiles but has `MAJOR`, unresolved citation, `INSUFFICIENT` framing issue, or audit mismatch. Preserve the failed review and stop revisions after two attempts.

**ETA:** 1.5–2 hours per eligible candidate.

**Hard stop:** T0+5 hours or `04:45 KST`, whichever is earlier; also stop immediately on contradictory expected value, missing provenance, numeric drift, or repeated review failure.

## 9. Packet D — Optional small-gap closure; drop first

**Hwao priority mapping:** P4. Do not start until Packets A and B are done and at least one Packet C candidate has a disposition.

### D1. Stellar-mass-assembly verdict recovery

**Objective:** Explain why `7cb504ea7ad3` has referee text but no normalized `review_verdict`.

**Outputs:**

- `packets/D-optional/7cb504ea7ad3/VERDICT_RECOVERY.md`
- `packets/D-optional/7cb504ea7ad3/REVIEW_PARSE_RECEIPT.json`

Goru extracts the referee language mechanically. Hwao assigns a disposition only if the text clearly supports one of the existing rubric values. Do not infer `ACCEPT` or `MINOR` merely because a PDF exists; the current report says substantial improvement is required.

### D2. Reionization run acceptance-readiness review

**Objective:** Test whether `fesc002` can address its proxy-calibration/data-source limitations without weakening caveats or inventing new evidence.

**Outputs:**

- `packets/D-optional/fesc002/ACCEPT_READINESS.md`
- `packets/D-optional/fesc002/EVIDENCE_GAP_LEDGER.json`

A retained `MINOR` verdict is an acceptable result. Do not iterate merely to force `ACCEPT`.

**Done marker:** `GE_LAB_OPTIONAL_CLOSE_<T0>` with an honest disposition for both records.

**ETA:** 20–30 minutes each.

**Drop rule:** Packet D is dropped first on any schedule or quota pressure.

## 10. Priority, staggering, and drop order

Start order:

1. Task 0 input baseline and quota T0.
2. Packet A begins immediately.
3. Packet B begins in parallel after Task 0.
4. Packet C begins only after Packet A decides whether `d8de519cb9c9` is distinct enough to draft.
5. Packet D begins only if A+B and at least one C candidate finish before the no-new-start cutoff.

Priority/drop logic:

- never drop Packet B once started; citation honesty is the last-to-drop integrity work;
- Packet A is cheap and unblocks Packet C;
- if time is short, run Packet B + Packet A and omit manuscript drafting;
- if Packet C can produce only one candidate, choose `2ab3c92eea8a` because it is not part of the MZR duplication cluster;
- drop Packet D first;
- no new projects tonight.

## 11. Receipt, audit, and morning handoff

**Final audit owner:** Kun, independently checked by Tori.

**Files to create:**

- `FINAL_ARTIFACT_MANIFEST.json`
- `FINAL_AUDIT.md`
- `MORNING_HANDOFF_20260727T0600KST.md`
- final quota checkpoint under `quota/`.

**Required audit checks:**

1. Every JSON output parses.
2. Every candidate PDF exists, is nonzero, begins with `%PDF`, and has a SHA-256 in the manifest.
3. Every TeX candidate has a compile receipt and no undefined citations/references.
4. Citation gate receipts retain unsupported claims rather than hiding them.
5. Numeric invariants exactly match the input manifest.
6. All original run JSONs still match `INPUT_SHA256.txt`.
7. No file outside the approved overnight output root changed because of the execution.
8. No public/private dashboard, runner, service, DB, wiki, git, account, or billing action occurred.

**Morning handoff contents:**

- one-screen outcome summary;
- board before/after comparison expressed as candidate readiness only, not source-run promotion;
- Packet A canonical MZR decision;
- Packet B citation-clean/partial status by paper;
- Packet C candidate disposition and exact artifacts;
- Packet D status or explicit `DROPPED_BY_PRIORITY`;
- failures and preserved rejected reviews;
- quota T0/final delta by subscription lane;
- exact next approval options: integrate one candidate, rerun a specific research gap, or leave all candidates local;
- safety ledger and `NO ACTIVE EXECUTION PHRASE`.

## 12. Risks and tradeoffs

- **Board status can overstate completion:** `status: done` does not mean draft/review/PDF stages occurred. Use reached-stage evidence, not the status string.
- **Citation gate is advisory in the current runner:** tonight’s candidate acceptance criterion is stricter—citation-clean is required.
- **MZR duplication can waste the night:** Packet A must precede any MZR drafting.
- **Topic/result mismatch is a provenance issue:** do not repair `e2f3b038f8dd` by changing its label in place.
- **A compiled PDF is not a publishable paper:** compile success, MINOR review, citation cleanliness, and provenance are separate receipts.
- **Model-generated prose can drift numeric invariants:** every number must come from the input manifest; verbatim comparison is mandatory.
- **Current repo is already dirty:** do not use a clean git status as proof. Use the pre/post source hashes and approved output-root allowlist.
- **Provider quota is abundant, not a target:** stop when high-value work is complete.

## 13. Open decision

Recommended default approval is Packets A+B+C, with D held.

Nothing in this plan authorizes execution. After an explicit approval, Hwao must repeat the approved packet set, effective T0, and hard stop before any lane receives work.
