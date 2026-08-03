# Paper Board Held-Repair Portfolio Implementation Plan

> **For Hermes:** Execute only after the user opens the specific packet gate. Use fresh no-self-review lanes, preserve every failed/partial finding, and stop before apply/publish/restart/Git unless separately approved.

**Goal:** Convert the completed P0/P1/P2 audit into three evidence-complete repair packets, then apply only the packet the user explicitly authorizes.

**Architecture:** Treat the served PDFs, Lab run, board metadata, and final adjudications as separate representations of the same claims. Each packet begins with immutable source mapping, produces a proposed exact-diff bundle plus validation receipt, and requires an independent scientific/custody review before any source or public artifact changes. No direct binary PDF editing and no repair-by-copying from stale backups.

**Current priority:** P0 first, P1 second, P2 third. P0 is the highest-severity public contradiction and has a finite seven-item correction ledger. P1 has the strongest evidence gap and needs source acquisition plus figure/table regeneration. P2 requires provenance/lineage work before wording changes can be trusted.

**Tech stack / artifacts:** Next.js 14 / TypeScript board metadata, canonical manuscript-generation sources once discovered, PDF render/extraction tools (`pdfinfo`, `pdftotext`, `pdftoppm`), JSON/CSV validation, direct HTTP plus browser representation checks.

---

## Safety and approval boundaries

- Planning and read-only source mapping are allowed.
- Packet-root writes may contain manifests, proposed diffs, render previews, and receipts only.
- Do not edit a manuscript source, PDF, board card, Lab record, review file, public source, database/wiki, service, or Git state without its separate gate.
- Do not accept a stale backup as canonical. Start from the richest current served identity and trace backward to its generator.
- Do not claim a repair is complete unless the canonical source, generated artifact, metadata, and served representation agree.
- Human validation remains 0 unless a qualified human explicitly reviews the science.
- Every packet must have one primary and two no-self-review cross-reviews; a mechanical PASS is advisory, never controlling.
- Keep `NO ACTIVE EXECUTION PHRASE` in status/public handoffs unless an execution gate is explicitly open.

## Immutable inputs

Execution root:

`.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-paper-board-portfolio-20260727/`

Controlling adjudications:

- `lanes/hwao/final-rollup/P0_HWAO_DISPOSITION.md`
- `lanes/hwao/final-rollup/P1_HWAO_DISPOSITION.md`
- `lanes/hwao/final-rollup/P2_HWAO_DISPOSITION.md`
- `lanes/hwao/final-rollup/HWAO_PORTFOLIO_ROLLUP.md`
- `independent/VALIDATION_T2_FINAL.json`
- `PUBLICATION_RECEIPT.json`

Live board metadata that may require a later exact-diff packet:

- `/Users/duhokim/NebulaMind/NebulaMind-origin-main-live/frontend/src/app/lab/FrontierDrafts.tsx:15-68`
- `/Users/duhokim/NebulaMind/NebulaMind-origin-main-live/frontend/src/app/lab/paperScores.ts:26-59`

Current served identities:

- P0: `/agent-reports/research-frontiers/galaxy-evolution-tng-validation-draft.pdf`
- P1: `/agent-reports/research-frontiers/tng-massive-galaxy-abundance-systematics.pdf`
- P2 frontier: `/agent-reports/research-frontiers/reionization-fesc-budget-landscape.pdf`
- P2 pipeline: `/api/lab/runs/fesc002/artifact/draft.pdf`

Do not mutate the generated public files directly. Locate and verify their canonical generators first.

---

### Task 1: Build the canonical source map

**Objective:** Prove which editable source generated each current served artifact before proposing a repair.

**Files:**

- Create after packet-preparation approval: `.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-paper-board-portfolio-20260727/repairs/SOURCE_MAP.json`
- Create: `repairs/SOURCE_MAP_RECEIPT.json`
- Read only: live board metadata, current public PDFs/history/review files, Lab-run source for `fesc002`, and candidate manuscript-generation directories.

**Steps:**

1. Re-fetch the four served PDFs and record URL, status, bytes, SHA-256, page count, title, and render identity.
2. Re-hash the matching files in the rich live frontend public root.
3. Search candidate manuscript/generator trees by unique title phrases and numerical anchors, not filenames alone.
4. For every candidate generator, regenerate into an isolated temporary directory and require byte identity or an explained deterministic difference against the served artifact.
5. Record `CANONICAL`, `STALE_BACKUP`, `GENERATED_ONLY_SOURCE_NOT_FOUND`, or `AMBIGUOUS` per representation.
6. Stop a packet at `SOURCE_NOT_PROVEN` if no generator is established. Do not edit the PDF or promote a backup.

**Acceptance:** Every proposed source edit names an exact canonical file and line/section. Unproven sources remain blocked.

---

### Task 2: Prepare P0 correction packet — highest priority

**Objective:** Resolve the public manuscript's matched-metallicity contradiction without weakening the surviving SFMS result.

**Files likely to change after a separate apply gate:**

- Canonical P0 manuscript/generator discovered by Task 1.
- `/Users/duhokim/NebulaMind/NebulaMind-origin-main-live/frontend/src/app/lab/FrontierDrafts.tsx:60-67`
- `/Users/duhokim/NebulaMind/NebulaMind-origin-main-live/frontend/src/app/lab/paperScores.ts:54-59`
- P0 review-route metadata/file only after its intended review artifact is identified.

**Packet files to create:**

- `repairs/P0/CLAIM_DIFF.md`
- `repairs/P0/CITATION_IDENTITY_PATCH.csv`
- `repairs/P0/NUMERIC_RECONCILIATION.json`
- `repairs/P0/BOARD_COPY_DIFF.md`
- `repairs/P0/RENDER_ACCEPTANCE.md`
- `repairs/P0/RECEIPT.json`

**Required repair content:**

1. Preserve the +0.41/+0.49 dex SFMS over-evolution chain and all stated provenance caveats.
2. Choose one evidence-honest MZR state:
   - supply a real single-scale derivation with reproducible data/code, or
   - retract the unsupported matched-Te claims and use the adjudicated maximum statement: unmatched-scale TNG under-evolution by about 2×, suggestive pending single-scale re-derivation.
3. Reconcile or remove −0.40, −0.27, factor 1.5, 2.0×10⁵, and “consistent once scales are matched.”
4. Replace/remove the cross-wired Lisiecki citation; add PP04/Kennicutt entries only if their dependent method is actually present.
5. Reconcile the manuscript's `~3×10⁴` TNG count against the frozen 23,722 invariant.
6. Regenerate Figure 2 from the chosen MZR state; never edit its annotation independently from the plotted data.
7. Repair the 404 review route only if a real review artifact exists; otherwise remove the broken link/metadata rather than fabricate a referee record.
8. Patch board and merit-score prose so neither still asserts a matched-scale chemical success absent from the corrected paper.

**Validation:**

- Forbidden unsupported strings absent from abstract, body, conclusion, figure text layer, card copy, and merit notes.
- All numeric anchors reproduce from one ledger.
- PDF render has no clipping/overlap and matches extracted text.
- Fresh Lana science review, Kun adversarial review, and Goru numeric/citation map converge before apply.

**Gate to open packet preparation only:**

`APPROVE P0 CORRECTION PACKET PREPARATION ONLY; NO SOURCE APPLY, PUBLICATION, RESTART, OR GIT.`

---

### Task 3: Prepare P1 evidence and representation packet

**Objective:** Narrow the paper to its defensible z=5 conditional claim and remove visible figure/table inconsistencies.

**Files likely to change after a separate apply gate:**

- Canonical P1 manuscript/generator discovered by Task 1.
- `/Users/duhokim/NebulaMind/NebulaMind-origin-main-live/frontend/src/app/lab/FrontierDrafts.tsx:38-46`
- `/Users/duhokim/NebulaMind/NebulaMind-origin-main-live/frontend/src/app/lab/paperScores.ts:40-45`

**Packet files to create:**

- `repairs/P1/PRIMARY_SOURCE_DENSITY_LEDGER.csv`
- `repairs/P1/CLAIM_DIFF.md`
- `repairs/P1/FIGURE_1_SPEC.json`
- `repairs/P1/TABLE_1_LAYOUT_ACCEPTANCE.md`
- `repairs/P1/SIMULATION_COUNT_REPRODUCTION.md`
- `repairs/P1/RECEIPT.json`

**Required repair content:**

1. Pin at least one direct primary-source cumulative-density row with threshold, selection, completeness, Eddington/scatter treatment, Poisson, and cosmic variance; otherwise keep the headline support at FAIL.
2. Use the adjudicated maximum claim verbatim in the packet: at exactly z=5, claimed observational anchor plus reported TNG counts imply a 0.20–0.28 dex footing-dependent shift; suggestive, not proof of no robust TNG tension; z≈5.5 marginal.
3. Make Figure 1 arrow, caption, body, and board copy agree on the 0.20–0.28 dex bracket and exact redshift footing.
4. Regenerate Table 1 so every grounding citation is visible within page bounds.
5. Separate populations and correlated SED terms; do not present the 1.30 dex linear sum as a probabilistic budget.
6. Reproduce N=15/N=20/N=4 from a pinned TNG selection or keep them explicitly manuscript-reported/unverified.
7. Update board and merit-score prose to remove “robust and IMF-independent consistency” until the direct cumulative evidence and counts pass.

**Validation:** direct-source rows >0 or explicit FAIL; regenerated render diff; covariance-aware budget check; no clipping; independent arithmetic reproduction.

**Gate to open packet preparation only:**

`APPROVE P1 EVIDENCE-AND-REPRESENTATION PACKET PREPARATION ONLY; NO SOURCE APPLY, PUBLICATION, RESTART, OR GIT.`

---

### Task 4: Prepare P2 provenance, citation, and lineage packet

**Objective:** Repair the pipeline's public-data/provenance and citation state while keeping lineage unresolved unless direct derivation evidence is produced.

**Files likely to change after separate Lab/source gates:**

- Canonical `fesc002` run specification and renderer discovered by Task 1; never edit the generated PDF or Lab record directly.
- Canonical frontier manuscript/generator only if its residual Simmonds passage attribution requires change.
- `/Users/duhokim/NebulaMind/NebulaMind-origin-main-live/frontend/src/app/lab/FrontierDrafts.tsx:16-24` only if public summary/review state changes.
- `/Users/duhokim/NebulaMind/NebulaMind-origin-main-live/frontend/src/app/lab/paperScores.ts:26-31` only after provenance-safe wording is settled.

**Packet files to create:**

- `repairs/P2/BIBLIOGRAPHY_IDENTITY_PATCH.csv`
- `repairs/P2/CITATION_DENOMINATOR_REPLAY.json`
- `repairs/P2/PROVENANCE_DIFF.md`
- `repairs/P2/SIMMONDS_DISAMBIGUATION.md`
- `repairs/P2/LINEAGE_DERIVATION_RECEIPT.json`
- `repairs/P2/RECEIPT.json`

**Required repair content:**

1. Replace Chisholm with `2022MNRAS.517.5104C` and use Flury `2022ApJ...930..126F` for the printed LzLCS II diagnostic role.
2. Resolve the pipeline's bare Simmonds shorthand to a bibcode/DOI and supported passage, or keep it quarantined.
3. Make citation-gate output denominator-aware: `0 checked` must report `NOT_EVALUATED`, never PASS.
4. Enumerate actual claim↔passage pairs; do not convert “5 passages” metadata into evidence.
5. Remove the `public data (jwst)` abstract claim unless actual survey-catalog use is proven. Preserve `DO_NOT_USE` for JWST/SDSS/TNG catalog-use claims under the current provenance.
6. Re-run novelty against the true literature-anchored estimand; the current “using JWST data” premise is invalid.
7. Keep lineage `UNRESOLVED` unless `LINEAGE_DERIVATION_RECEIPT.json` identifies exact source run, commit/build chain, transformation steps, and output hashes. Similar methods/numbers are insufficient.
8. Preserve MAJOR → ACCEPT as an advisory automated-review trajectory, not “ACCEPT in 1 cycle.”

**Validation:** nonzero citation denominator or explicit NOT_EVALUATED; reference-list/inline/lit_refs set reconciliation; provenance sentence diff; derivation receipt schema; independent Kun/Lana/Tori review.

**Gate to open packet preparation only:**

`APPROVE P2 PROVENANCE-CITATION-LINEAGE PACKET PREPARATION ONLY; NO LAB/SOURCE APPLY, PUBLICATION, RESTART, OR GIT.`

---

### Task 5: Cross-packet integration and apply gates

**Objective:** Prevent a repair in one representation from leaving contradictions elsewhere.

**Steps:**

1. Build a matrix for manuscript text, figures/tables, bibliography, review/history record, board card, merit-score notes, Lab provenance, and public report.
2. Require every changed claim to have one canonical value/status across applicable representations.
3. Re-run the frozen-invariant checks: board count, P0 TNG=23,722 / SDSS=120,000, `human_validated=0`, source identity, and no stale public route.
4. Render every changed PDF at 300 dpi and inspect the exact changed pages.
5. Obtain fresh no-self-review receipts after any edit; previous reviews do not clear changed content.
6. Present one exact apply packet per paper. Applying P0, P1, and P2 together is prohibited unless the user explicitly combines the gates.
7. Keep publication, service restart, and Git landing as three later, separate approvals.

**Apply gate template:**

`APPROVE APPLY <P0|P1|P2> EXACT-DIFF PACKET <receipt-hash>; VERIFY SOURCE + RENDER + BOARD STATE; NO OTHER PACKET, PUBLICATION, RESTART, OR GIT.`

**Publication gate template:**

`APPROVE PUBLISH VERIFIED <P0|P1|P2> ARTIFACT ONLY; VERIFY APP HEALTH + CLEAN URL; NO OTHER DEPLOYMENT.`

---

## Stop conditions

Stop and report rather than improvise if:

- canonical generator is not proven;
- a source requires login/CAPTCHA/payment/OAuth/secrets;
- direct evidence does not support the requested claim;
- a changed figure cannot be regenerated from the same ledger as its text;
- a review/result is missing, stale, or self-reviewed;
- a paper, board card, Lab record, public route, or runtime action would cross an unopened gate;
- source, served bytes, or rendered representation drift after preflight.

Final planning marker: `PAPER_BOARD_HELD_REPAIR_PORTFOLIO_PLAN_READY_20260728`

NO ACTIVE EXECUTION PHRASE
