# Overnight Paper Board Portfolio Research Plan

> **For Hermes:** Use Hwao-led bounded lane dispatch only after the owner approves the exact packet phrase in this plan. This document is planning only; do not execute research from it automatically.

**Goal:** Scrutinize the highest-value unresolved science and integrity risks across the current portfolio-wide Paper Board, producing isolated local audit packets and a morning decision handoff without changing any live paper, Lab run, public route, database, service, or Git state.

**Architecture:** Hwao coordinates and adjudicates; Lana performs science/manuscript review; Kun independently checks reproducibility, artifact identity, and citations; Goru performs mechanical source/count/claim mapping; Tori relays, records receipts, and independently verifies the final custody chain. At most three helper lanes run concurrently, each writing only to its own packet directory under one new approved output root.

**Tech stack:** Existing local Paper Board sources, direct public Paper Board/API reads, ADS/arXiv metadata and primary-source retrieval where available, `pdftotext`/`pdfinfo`, SHA-256 manifests, existing citation-gate conventions, direct subscription-backed Claude/Codex/Antigravity lanes, and the existing redacted provider-usage monitor.

---

## 1. Verified current context

### Portfolio truth

The Paper Board is portfolio-wide, not only the Lab API:

- 13 visible drafts total: 1 flagship, 5 frontier manuscripts, and 7 real pipeline notes.
- The API contains 9 run records, but `gated-e2e-demo` and `gated-halt-demo` are hidden fixtures; 7 appear on the portfolio board.
- 10 of the 13 visible drafts have PDFs, 7 reached the board's referee stage, and 0 are human-validated.
- Source construction: `frontend/src/app/lab/DraftBoard.tsx:484-493`.
- Flagship definition: `frontend/src/app/lab/FlagshipStudies.tsx:15-27`.
- Frontier definitions: `frontend/src/app/lab/FrontierDrafts.tsx:15-69`.
- Live pipeline truth: `https://nebulamind.net/api/lab/runs`.

### Merit and maturity

The current five-member advisory panel means are:

1. TNG validation frontier: 6.90.
2. z≈9–10 unlensed metallicity flagship: 6.70.
3. TNG massive-galaxy abundance frontier: 5.90.
4. Reionization fesc landscape frontier: 5.60.
5. Withdrawn high-z scaling-relations draft: 3.80.
6. MZR systematics framework: 3.00.

Scores are advisory, not scientific validation. Source: `frontend/src/app/lab/paperScores.ts:18-61`.

### Prior overnight outcome

The 2026-07-26 run already completed A+B+C+D and published the separately approved labelled MZR draft `c2v2e2e0726a`. Remaining states from `progress/MORNING_HANDOFF_20260727.md` are:

- MZR C2: published AI draft, ungrounded, TENSION and unresolved O/H calibration retained.
- SFMS C1: outline only; uncomputed slots remain explicit.
- SMF `7cb504ea7ad3`: BLOCKED on observation comparison, uncertainty, and bias analysis.
- `fesc002`: PARTIAL; literature-grounded, but cited works are missing from the reference coverage and the citation-entailment gate checked zero claims.

### Newly verified portfolio-level defects

The highest-merit TNG validation frontier must be first because its current served representation is not internally stable:

- Served artifact: `/Users/duhokim/NebulaMind/NebulaMind-origin-main-live/frontend/public/agent-reports/research-frontiers/galaxy-evolution-tng-validation-draft.pdf`.
- Served-rich-root identity observed during planning: 4 pages, 132,831 bytes, SHA-256 `086654e747f13626d853d404557292bd0238f5536ee2173669f2674d37ad62ef`.
- A separate 3-page source copy exists with a different hash; it is not interchangeable with the served artifact.
- The configured review URL returns 404, and the rich public root has no corresponding review file; only a human-direction history JSON exists.
- The served PDF's abstract/conclusion say the MZR was placed on a matched Te-anchored scale and is consistent, while body passages still describe different abundance scales, a suggestive result, or TNG under-evolution. The strongest uncaveated claim therefore cannot be accepted until the actual rendered artifact is reconciled section by section.

### Coordinator draft correction boundary

Hwao produced `.hermes/plans/2026-07-27_overnight-paper-board-research-v2.md`. It is preserved as coordinator input but is not execution-ready because verification found:

- reversed MZR sample counts in E1; the correct invariant is TNG = 23,722 and SDSS = 120,000;
- pipeline-only scope instead of the portfolio-wide 13 visible drafts;
- omission of the highest-merit TNG validation representation/science contradiction;
- stale quota baseline values.

This verified plan supersedes that draft for any later approval decision. Hwao must acknowledge these corrections before dispatch.

---

## 2. Mode and authorization boundary

This is **PLAN ONLY**.

Writing this plan does not authorize:

- research-lane dispatch or background workers;
- cron, launchd, browser automation, or a Deep Research submission;
- modification of `frontend`, `backend`, `tools`, current Lab records, current paper PDFs, or either public root;
- DB/SQL/API/wiki/page-version/trust writes;
- deploy or restart;
- Git add/commit/push/merge or history changes;
- account, credential, OAuth, billing, payment, or provider-routing changes;
- public publication, substitution, external submission, or cockpit changes.

Recommended future approval phrase:

`APPROVE OVERNIGHT PAPER-BOARD PORTFOLIO P0+P1+P2, LOCAL-ONLY, NO BROWSER/CRON/PUBLISH, HARD STOP 06:00 KST.`

If approved, the only write root is:

`.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-paper-board-portfolio-20260727/`

Every source and served artifact remains immutable input. Failed reviews and contradictory states remain preserved rather than overwritten.

---

## 3. Task 0 — Freeze the portfolio baseline

**Objective:** Establish reproducible custody before any research lane starts.

**Files to create after approval:**

- `baseline/PORTFOLIO_BOARD_SNAPSHOT.json`
- `baseline/INPUT_MANIFEST.json`
- `baseline/INPUT_SHA256.txt`
- `baseline/PUBLIC_ARTIFACT_IDENTITY.json`
- `quota/usage_<T0>.json`
- `OVERNIGHT_LEDGER.md`
- `SAFETY_LEDGER.md`

**Steps:**

1. Record all 13 visible board items with track, title, source path/URL, stage, verdict, PDF/review URL, grounding state, and board-visible caveats.
2. Record the 9 API records separately and label the two hidden demo fixtures.
3. Pin local source and rich-public-root files by size, page count, modification time, and SHA-256.
4. Direct-fetch each prioritized public PDF/review URL with cache-busting/no-cache semantics; record HTTP status, bytes, ETag/Last-Modified where present, and SHA-256.
5. Capture current source hashes for all existing Lab JSONs and prioritized paper artifacts.
6. Capture the redacted provider gauges and record the source timestamp.
7. Record the dirty-worktree baseline as context only; do not use Git cleanliness as the write-scope proof.

**Acceptance gate:** all JSON parses, all expected input hashes are recorded, and each public artifact is linked to one unambiguous byte identity.

**Stop condition:** source drift, ambiguous artifact identity, or a public URL that resolves to a different revision than the pinned source. Mark `INPUT_OR_IDENTITY_DRIFT_BLOCKER`; do not choose a convenient copy silently.

---

## 4. Packet P0 — TNG validation representation and scientific-consistency audit

**Priority:** first and last-to-drop. It is the highest-merit frontier and currently has contradictory rendered claims.

**Objective:** Determine exactly which MZR/SFMS claims survive in the currently served four-page PDF before any new research or revision is attempted.

**Primary lane:** Lana scientific consistency review.

**Independent lanes:** Kun artifact/representation audit; Goru claim-citation and numeric-invariant map; Hwao final disposition.

**Inputs:**

- pinned served PDF and direct public bytes;
- `galaxy-evolution-tng-validation-draft_history.json`;
- `frontend/src/app/lab/FrontierDrafts.tsx` card text;
- `frontend/src/app/lab/paperScores.ts` evaluation notes;
- cited primary sources and exact publication versions;
- related MZR framework and C2 calibration packets as contextual evidence only.

**Files:**

- `packets/P0-tng-validation/ARTIFACT_IDENTITY.md`
- `packets/P0-tng-validation/REPRESENTATION_MATRIX.json`
- `packets/P0-tng-validation/SECTION_CLAIM_LEDGER.md`
- `packets/P0-tng-validation/NUMERIC_INVARIANTS.json`
- `packets/P0-tng-validation/CITATION_AND_REVIEW_LINK_AUDIT.md`
- `packets/P0-tng-validation/LANA_SCIENCE_REVIEW.md`
- `packets/P0-tng-validation/KUN_REPRODUCTION.md`
- `packets/P0-tng-validation/GORU_MECHANICAL_CHECK.md`
- `packets/P0-tng-validation/HWAO_DISPOSITION.md`

**Steps:**

1. Compare rendered pages, plain-text extraction, figures/captions, board card text, and history JSON; never grade from one lossy representation.
2. Build an abstract/method/results/discussion/conclusion matrix for every load-bearing SFMS and MZR claim.
3. Record exact estimand, sample, redshift, selection, mass aperture, abundance scale, statistic, uncertainty, and citation for every headline number.
4. Separate representation-caused extraction artifacts from actual manuscript contradictions.
5. Verify the `+0.41/+0.49 dex` SFMS gap, selection-debiasing envelope, `+0.13 dex` aperture statement, and all MZR scale claims against source evidence.
6. Audit the missing/404 referee path as an artifact-integrity defect; do not invent a review verdict from the history JSON.
7. Hwao chooses exactly one disposition:
   - `CONSISTENT_CLAIMS__ISOLATED_REVISION_PACKET_ALLOWED`
   - `MZR_STATE_CONTRADICTORY__CORRECTION_LEDGER_ONLY`
   - `SOURCE_OR_ESTIMAND_BLOCKED__NO_REVISION`
8. Do not write a corrected manuscript tonight under the default approval. Any candidate revision is a separate next-day packet.

**Acceptance gates:**

- Every strong conclusion appears consistently across all sections, or is listed as an unresolved contradiction.
- Every load-bearing citation resolves to the authoritative version and supports the attached claim.
- The rendered figures and captions are visually checked, not inferred from PDF text.
- Numeric reproduction matches pinned inputs or the claim is blocked.

**Done marker:** `P0_TNG_VALIDATION_AUDIT_DONE_<T0>`.

**Stop conditions:** source inaccessible; artifact revisions disagree; estimands cannot be made commensurable; or correcting the claim would require a fresh analysis. Preserve `BLOCKED` rather than drafting around the gap.

---

## 5. Packet P1 — High-redshift massive-galaxy abundance source/statistic audit

**Priority:** second. Advisory merit 5.90 and review-ready, but the paper carries high-risk cumulative-density and systematic-budget claims.

**Objective:** Test whether the z≈4–6 TNG/JWST consistency claim survives exact statistic, population, aperture, IMF, selection, uncertainty, and source-version reconciliation.

**Primary lane:** Kun adversarial/reproducibility audit.

**Independent lanes:** Goru mechanical source/numeric map; Lana scientific scope review; Hwao disposition.

**Inputs:**

- pinned `tng-massive-galaxy-abundance-systematics.pdf`;
- its review loop and history JSON;
- each load-bearing primary source, using published/latest values;
- TNG conventions and actual compared statistic.

**Files:**

- `packets/P1-massive-abundance/QUERY_COVERAGE.json`
- `packets/P1-massive-abundance/CUMULATIVE_DENSITY_LEDGER.csv`
- `packets/P1-massive-abundance/SYSTEMATIC_BUDGET_LEDGER.csv`
- `packets/P1-massive-abundance/SIMULATION_COMMENSURABILITY.md`
- `packets/P1-massive-abundance/SOURCE_ROLE_AUDIT.md`
- `packets/P1-massive-abundance/KUN_VERDICT.md`
- `packets/P1-massive-abundance/LANA_SCOPE_REVIEW.md`
- `packets/P1-massive-abundance/HWAO_DISPOSITION.md`

**Steps:**

1. Grade query coverage, statistic identity, population commensurability, simulation commensurability, primary-source support, source version, and claim strength separately as `PASS`, `PARTIAL`, or `FAIL`.
2. Reconcile the historical `0.28 dex` erasure threshold with the later `0.20 dex` mass-basis result; identify which artifact/version carries each number.
3. Require explicit `n(>M*)` evidence. Do not substitute Schechter parameters, UV luminosity functions, halo densities, or extreme-value ceilings.
4. Keep total, star-forming, quiescent, and UV-selected populations separate.
5. Record IMF, aperture, bound/all-star convention, redshift bin, threshold, completeness, contamination, Eddington/scatter treatment, Poisson error, and cosmic variance for every comparison row.
6. Do not add maximum shifts from unrelated samples into a consensus systematic budget; record covariance and population scope.
7. Keep the z>6 quiescent residual separate from the z≈4–6 total-population claim.
8. Hwao assigns `AUDIT_PASS`, `PARTIAL__CLAIMS_REQUIRE_NARROWING`, or `FAIL__NOT_REVISION_READY`.

**Done marker:** `P1_MASSIVE_ABUNDANCE_AUDIT_DONE_<T0>`.

**Stop conditions:** no primary cumulative-density evidence, cross-wired identifiers, superseded numerical values, or incomparable population/simulation conventions.

---

## 6. Packet P2 — Reionization/fesc lineage and citation-entailment reconciliation

**Priority:** third. This closes a known integrity gap without forcing new science.

**Objective:** Reconcile the frontier fesc landscape manuscript with pipeline run `fesc002`, close or honestly preserve its cited-work and zero-positive-entailment gaps, and decide whether the two artifacts are canonical, complementary, or duplicative.

**Primary lane:** Goru lineage and source matrix.

**Independent lanes:** Kun citation-entailment audit; Lana overclaim/status review; Hwao disposition.

**Important current truth:** `fesc002` is already labelled literature-grounded on 6 papers/5 passages. The unresolved defect is not “no literature”; it is missing cited-work coverage plus `checked=0`, which provides zero positive entailment evidence.

**Files:**

- `packets/P2-fesc/LINEAGE_MATRIX.json`
- `packets/P2-fesc/CLAIM_STATUS_LEDGER.jsonl`
- `packets/P2-fesc/BIBLIOGRAPHY_IDENTITY.csv`
- `packets/P2-fesc/PASSAGE_SUPPORT_LEDGER.csv`
- `packets/P2-fesc/CITATION_GATE_REPLAY.json`
- `packets/P2-fesc/LANA_OVERCLAIM_REVIEW.md`
- `packets/P2-fesc/KUN_CITATION_VERDICT.md`
- `packets/P2-fesc/HWAO_DISPOSITION.md`

**Steps:**

1. Pin both manuscripts/runs and list every claimed result, estimand, systematic assumption, citation, and source role.
2. Identity-verify cited-but-unlisted `Chisholm+22`, `Flury+22`, and `Simmonds+24`; retrieve exact passages through read-only ADS/arXiv/public-source paths.
3. Deduplicate by bibcode first, then DOI/title fallback; quarantine cross-wired or unresolved identities.
4. Re-run citation entailment only on an isolated copied body and saved source set; never edit `fesc002`.
5. Distinguish maintenance-criterion mapping from full reionization-history integration, and indirect proxy calibration from direct fesc measurement.
6. Build a status map before any prose: established assumptions, debated inputs, measured proxies, unknowns, and `DO_NOT_USE` claims.
7. Hwao assigns one relation: `CANONICAL_PLUS_SUPPORTING`, `COMPLEMENTARY_DISTINCT_ESTIMANDS`, `DUPLICATE_CONSOLIDATION_RECOMMENDED`, or `UNRESOLVED`.

**Acceptance gates:** every positive support decision has an exact passage; unresolved sources remain unresolved; target coverage is greater than zero without fabricated support; no claim is strengthened to force a pass.

**Done marker:** `P2_FESC_LINEAGE_AND_CITATION_DONE_<T0>` or `_PARTIAL_`.

**Stop conditions:** identity mismatch, source inaccessible, citation supports only topic proximity, or the only path requires browser/account interaction. Under the default approval there is no browser or Deep Research run.

---

## 7. Held packets — not part of the recommended default

### H1 — Flagship human-review packet

The z≈9–10 unlensed metallicity flagship is already the most mature item. More automated rewriting risks churn. A later local-only packet should prepare a one-screen human validation checklist, claim/caveat ledger, and decision form. It must not simulate human sign-off.

### H2 — C2 O/H calibration research

Do not start with a formula-only cross-calibration. TNG's solar-scaled O/Z conversion and empirical strong-line/Te diagnostics may not share an estimand. First require an accepted scale taxonomy, exact equation/validity ranges, diagnostic compatibility, and propagated scatter. Correct frozen invariants: TNG = 23,722; SDSS = 120,000. A C2 V3 or public correction is a separate gate.

### H3 — Pipeline backlog specifications

- `2ab3c92eea8a`: produce a slot-provenance/computation-readiness map; do not fill absent numbers from model memory.
- `7cb504ea7ad3`: preserve BLOCKED; specify observational comparison, uncertainty, selection, and mass-bias analyses required for a future fresh-run gate.
- `e2f3b038f8dd`: proposed relabel/retire packet only; never edit the source record in place.
- `c2v2e2e0726a`: preserve the published labelled AI draft and consumed publication phrase.

These held packets begin only under a separate owner approval or if the owner explicitly expands tonight's scope.

---

## 8. Lane schedule and review order

Default window if approved before 22:30 KST:

1. T0–T0+20 min: Task 0 baseline and quota receipt.
2. T0+20–00:30: P0, P1, and P2 primary lanes run concurrently.
3. 00:30–01:30: cross-review swap; authors do not review their own packet.
4. 01:30–03:30: source corrections, deterministic replay, and second-pass verdicts.
5. 03:30: no new science subtask starts.
6. 04:30: packet content freezes; only verification and blocker clarification remain.
7. 05:00–05:40: Kun final audit, independently reproduced by Tori.
8. 05:40–06:00: Hwao morning synthesis and final safety receipt.

Late-approval degradation:

- After 00:00 KST: run P0 + P2; produce P1 intake ledger only.
- After 02:00 KST: run P0 only plus portfolio baseline and morning handoff.
- After 03:30 KST: no research starts; prepare the baseline/blocker handoff only.
- Never extend past 06:00 KST without a new owner instruction.

Single-writer rule: each lane writes only under `packets/<packet>/<lane>/`; Hwao writes only disposition files; Tori writes only shared receipts/manifest/handoff.

---

## 9. Subscription quota allocation

Live redacted snapshot observed at 2026-07-27 21:42 KST:

- Claude/Fable/Lana: 6% five-hour used; 9% weekly used.
- Codex/Kun: 1% weekly used; five-hour reading unknown/stale and must be refreshed before dispatch.
- Antigravity/Goru: about 0.21% five-hour and 0.24% weekly used.
- Consumer Gemini app: 1% current-window and weekly used, but browser/Deep Research remains held under the recommended approval.
- Nous free plan: exhausted; purchased top-up observed at $42.58. Do not intentionally spend it for bulk research.

Allocation:

| Lane | Subscription-backed route | Work | New-start cap |
|---|---|---|---|
| Hwao | direct Claude subscription | coordination and closed dispositions | Claude weekly 25% |
| Lana | direct Claude subscription | P0/P1/P2 scientific review | shared Claude weekly 25% |
| Kun | ChatGPT/Codex subscription | P0 custody, P1 audit, P2 entailment | Codex weekly 20%; require fresh visible status |
| Goru | Antigravity subscription | mechanical matrices and source identity | Gemini agent weekly 10% |
| Tori | current OpenAI-Codex lane | relay, receipts, independent verification | no bulk source synthesis |
| Consumer DR | held | none under default approval | separate explicit browser/DR gate |

Capture redacted gauges at T0 and every 30 minutes. A globally observed Nous balance movement must be reported with unknown attribution; never claim zero spend from an aggregate balance alone.

Stop a lane on stale quota data (>10 minutes for a new start), paid/overage/rate-limit/account prompts, cap breach, or completed useful scope. Never burn quota merely to reach a percentage.

---

## 10. Global safety and scientific stop conditions

Stop the affected packet immediately on:

- input/public artifact drift;
- unsupported or cross-wired source identity;
- number, redshift, population, aperture, IMF, diagnostic, or statistic mismatch;
- expected-value `CONTRADICTS` where a packet depends on that claim;
- source-access failure that prevents line-level review;
- a requirement for fresh data, runner use, mutation, browser/account action, payment, or external submission;
- two failed independent review attempts on the same candidate claim;
- any write outside the approved output root.

Do not evidence-hunt to rescue an overbroad claim. Narrow, block, or retire it. A compiled PDF or automated ACCEPT does not equal human validation.

---

## 11. Exact morning deliverables

By 06:00 KST, create only under the approved overnight root:

1. `MORNING_HANDOFF_20260728T0600KST.md`
   - one-screen outcome;
   - verified 13-item portfolio baseline;
   - P0/P1/P2 `DONE`, `PARTIAL`, `BLOCKED`, or `DROPPED_BY_PRIORITY`;
   - strongest surviving claims and exact blockers;
   - Hwao dispositions;
   - quota T0→final deltas with source timestamps;
   - safety ledger and `NO ACTIVE EXECUTION PHRASE`;
   - next approval options, each separately scoped.
2. `FINAL_ARTIFACT_MANIFEST.json`
   - path, bytes, SHA-256, owner lane, source identities, and validation status for every output.
3. `FINAL_AUDIT.md`
   - JSON/JSONL parse checks;
   - input hash recheck;
   - PDF/public identity checks;
   - citation/source-identity results;
   - confirmation that no source/public/product/service/Git bytes changed.
4. `OVERNIGHT_LEDGER.md`
   - KST timestamps for approval, lane start, source freeze, cross-review, disposition, freeze, and final audit.
5. `SAFETY_LEDGER.md`
   - Lab/source writes: 0;
   - public/cockpit writes: 0;
   - DB/API/wiki/trust writes: 0;
   - deploy/restart: 0;
   - Git writes: 0;
   - cron/browser/DR submissions: 0;
   - billing/account/OAuth changes: 0.
6. All P0/P1/P2 files listed above, including failed or partial reviewer artifacts.

Next-day options must remain separate approval gates:

- build an isolated corrected TNG-validation candidate;
- narrow/revise the massive-abundance manuscript;
- repair or consolidate fesc artifacts;
- prepare the flagship human-review packet;
- authorize a fresh data/runner analysis;
- publish/substitute/rollback any public paper.

---

## 12. Verification commands for a later approved run

Run from the approved overnight root:

- Parse JSON: `python3 -m json.tool <file>.json >/dev/null`.
- Parse JSONL: a Python line-by-line `json.loads` check with zero failures.
- Verify inputs: `shasum -a 256 -c baseline/INPUT_SHA256.txt`.
- Verify PDFs: `pdfinfo <file>.pdf`, nonzero bytes, `%PDF` header, recorded SHA-256.
- Verify public identity: direct no-cache fetch hash equals the pinned receipt or is explicitly marked drifted.
- Verify source scope: compare the final filesystem manifest with the approved output-root allowlist.
- Verify Git context read-only: compare ordered `git status --porcelain` records against T0; do not require a clean worktree.

Expected final state: all approved packets have explicit dispositions, every input hash remains unchanged, no write exists outside the overnight root, and no active execution phrase remains.

---

## 13. Risks and tradeoffs

- P0 may conclude that the top-ranked frontier needs correction rather than more research; that is a valuable result, not a failed night.
- P1 can invalidate a neat conclusion if cumulative-density or population definitions are not commensurable.
- P2 may remain PARTIAL if passage-level evidence cannot be acquired without browser/DR access.
- Restricting default scope to three integrity-first packets means the SFMS/SMF backlog will not advance tonight.
- The mature flagship is intentionally protected from another autonomous prose cycle; human review is the correct next gate.
- Current repository dirtiness requires hash/allowlist verification rather than clean-status assumptions.

A good overnight result is a smaller set of defensible claims and explicit blockers—not more PDFs.