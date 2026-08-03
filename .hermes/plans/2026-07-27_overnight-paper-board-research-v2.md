# Overnight Paper-Board Research Plan v2 — 2026-07-27 (PLANNING ONLY)

> **For Hermes/Hwao:** This is a plan, not an execution order. No lane may be dispatched, no file outside a future approved output root written, until the owner issues the exact approval phrase in §1. Tonight's plan follows the conventions proven on 2026-07-26 (single-writer versioned root, immutable input baseline, receipts, hard stops).

**Goal:** convert last night's decided-but-open gaps on the AI-Scientist Paper Board into isolated, reviewable research artifacts — centred on the one blocker that gates the whole MZR lineage (the unresolved O/H calibration TENSION) — plus literature-grounding for the strongest record (`fesc002`), without touching live runs, public surfaces, DB, git, or deploys.

**Board truth (post-20260726 run, 9 records):**
- `c2v2e2e0726a` — PUBLISHED AI-draft (MZR, TNG·SDSS); TENSION carried, not resolved.
- `gated-e2e-demo` — CANONICAL MZR lineage (A-decision); `d8de519cb9c9` = precursor; `2958462772b2` = overlap cluster.
- `2ab3c92eea8a` — SFMS; C1 outline exists with explicit to-be-computed slots (honest, unfilled).
- `e2f3b038f8dd` — label/result mismatch (says SFMS/quenching, result is MZR); source-record decision still open.
- `fesc002` — strongest record (NOVEL, PDF+MINOR) but zero positive citation-entailment coverage and missing cited works (D2 PARTIAL).
- `7cb504ea7ad3` — D1 BLOCKED (needs obs comparison, error/bias analysis; not closable without new gates).
- `gated-halt-demo` — B-decision adopted; citation-clean body exists, candidate not built.

---

## 1. Mode and authorization boundary

**PLANNING ONLY.** Writing this plan authorizes nothing. Prohibited until approval, and prohibited always tonight: publishing, DB/SQL/API/wiki/trust writes, deploy/restart, git writes, cron/launchd creation, edits to `tools/lab_runner_worker.py` / `tools/nm_gates.py` / `tools/render_pipeline_board.py`, edits to any `lab-runs/*.json` or existing run dir, cockpit updates, billing/account/OAuth actions, paid-overage paths.

Approval phrase for the recommended default:

`APPROVE OVERNIGHT PAPER-BOARD PLAN V2 E1+E2+E3, HOLD E4+E5, LOCAL-ONLY, HARD STOP 06:00 KST.`

Narrower approvals may name packets. Output root (created only after approval):
`.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-paper-board-research-20260727/`

---

## 2. Prioritized lanes (packets)

### Task 0 — Immutable input baseline (always first)
Copy the 9 run JSONs → `inputs/run-records/`; SHA-256 manifest; board snapshot; quota T0. Validation: `shasum -c` all OK. **Stop:** any source drift → `INPUT_DRIFT_BLOCKER`.

### Packet E1 — O/H calibration reconciliation (P1; the board's central blocker)
**Objective:** quantify whether the C2/canonical-MZR TENSION survives calibration-scale reconciliation, using ONLY published conversion relations (Kewley & Ellison 2008 polynomial conversions; Tremonti04 ↔ PP04-O3N2 ↔ Te-anchored scales; known offset ~+0.24 dex at the massive end) applied to the already-recorded median relations (TNG N=23,722; SDSS N=120,000 — verbatim invariants from the C2 manifest; counts corrected per Tori verification 2026-07-27).
**[ON HOLD 2026-07-27: owner clarified tonight's target is the DESI DR1 aa60182-26 referee revision, not this board. Tori's further findings — portfolio scope 1 flagship + 5 frontier drafts + 9 runs; tng-validation-draft 404 review + internal MZR contradiction — are logged for a future representation-consistency-first re-prioritization, unadjudicated.]
**Precondition (verified 2026-07-27):** SDSS galSpecLine is NOT on local disk → **no fresh data run tonight**; formula-based reconciliation only. A galSpecLine-based re-derivation is named as future work, not attempted.
**Lanes:** Lana authors the reconciliation memo + recalibrated comparison table/figure; Kun independently re-derives the conversion arithmetic; Goru verifies numeric invariants verbatim vs the frozen C2 manifest; Hwao scientific disposition.
**Evidence/acceptance gates:** (i) every conversion cites the exact published equation (paper, eq. number, validity range); (ii) recalibrated offsets reported with propagated conversion scatter; (iii) verdict is one of `TENSION_RESOLVED_BY_SCALE`, `TENSION_REDUCED_RESIDUAL`, `TENSION_ROBUST`, with the arithmetic reproducible by Kun to <0.01 dex; (iv) no source-record edits; C2 V3 drafting is explicitly OUT of scope tonight.
**Files:** `packets/E1-oh-reconciliation/{OH_SCALE_MEMO.md, CONVERSION_TABLE.json, KUN_REDERIVATION.md, GORU_INVARIANT_CHECK.md, HWAO_DISPOSITION.md}`
**Done marker:** `GE_LAB_OH_RECONCILE_<T0>`. **ETA:** 1.5–2 h.
**Stop:** conversion validity range excludes the sample's mass/metallicity regime → record `OUT_OF_VALIDITY_BLOCKED`, do not extrapolate.

### Packet E2 — fesc002 literature grounding via DR (P2; runs parallel to E1)
**Objective:** close D2's gap — missing cited works + zero positive entailment coverage — with real retrieved literature, not invented bridges.
**Lanes:** **DR (Gemini Deep Research, browser, driven by Tori as DR-correspondent)** retrieves the missing cited works and passage-level evidence for each fesc002 claim; Kun rebuilds `CLAIM_CITATION_LEDGER.json` from the DR-retrieved passages and re-runs `tools/nm_gates.py:citation_entailment_gate` on an isolated candidate body; Lana checks no claim got strengthened.
**DR pacing (protocol):** max **2** DR runs, spaced ≥30 min; back off on first soft throttle; if blocked, mark `DR_THROTTLED_SKIPPED` and continue with whatever Kun can ground from already-local corpus. DR output filed to `packets/E2-fesc-grounding/dr/DR_REFERENCE.md` — **reference artifact only; DR never edits candidates.**
**Evidence/acceptance gates:** (i) each formerly-missing work resolved to an exact bibliographic record + retrieved passage, or honestly marked `SOURCE_UNRESOLVED`; (ii) entailment gate re-run with receipts; target positive coverage >0 with zero fabricated support; (iii) fesc002 source record untouched.
**Files:** `packets/E2-fesc-grounding/{dr/DR_REFERENCE.md, CLAIM_CITATION_LEDGER.json, CANDIDATE_BODY.md, CITATION_GATE_RECEIPT.json, KUN_SUMMARY.md}`
**Done marker:** `GE_LAB_FESC_GROUNDED_<T0>` (or `_PARTIAL_` preserving unresolved flags). **ETA:** 1–1.5 h wall-clock (DR latency dominates).
**Stop:** any DR account throttle/captcha → back off, one retry after ≥30 min, then skip. Never create accounts, never pay.

### Packet E3 — C1 completion: `2ab3c92eea8a` SFMS candidate (P2)
**Objective:** fill the C1 outline's to-be-computed slots ONLY from the run's existing computed Study artifacts (recorded medians/fits in the run dir); compile to an isolated AASTeX candidate.
**Lanes:** Lana fills + drafts; Kun compiles (tectonic) + reproducibility receipt; Goru slot-by-slot provenance map (each number → exact source artifact path); Hwao review.
**Evidence/acceptance gates:** (i) zero numbers from model memory — every filled slot has a provenance line; unfillable slots stay as slots with `SLOT_UNFILLED`; (ii) compile rc=0, no undefined refs; (iii) citation-entailment receipt saved; (iv) expected-value gate run before drafting (CONTRADICTS = hard stop); (v) live run record untouched.
**Files:** `packets/E3-sfms-candidate/2ab3c92eea8a/{SLOT_PROVENANCE.json, candidate/draft.tex, candidate/draft.pdf, candidate/CITATION_GATE.json, candidate/MANIFEST.json, REVIEW.md}`
**Done marker:** `GE_LAB_SFMS_CANDIDATE_<T0>` (or `_PARTIAL_`). **ETA:** 1.5–2 h.
**Stop:** >30% of slots unfillable from computed artifacts → stop drafting, deliver the provenance map + gap list instead (that is the honest deliverable).

### Packet E4 — `e2f3b038f8dd` mislabel disposition packet (P3; HOLD by default)
Propose-only: side-by-side label-vs-result evidence + a proposed corrected record as a NEW file (`PROPOSED_RECORD.json`) + Hwao memo recommending one of `RELABEL_APPROVAL_REQUESTED` / `RETIRE_APPROVAL_REQUESTED`. **No in-place edit tonight.** Done marker `GE_LAB_MISLABEL_DISPO_<T0>`. ETA 30–40 min.

### Packet E5 — D1 `7cb504ea7ad3` closure spec (P4; drop first)
Spec-only ledger of the exact new computations/gates that would unblock it (obs comparison dataset, error model, bias analysis), each with data-availability noted. No execution. Done marker `GE_LAB_D1_SPEC_<T0>`. ETA 20–30 min.

**Start order:** Task 0 → E1 + E2 in parallel → E3 (after Task 0, independent) → E4/E5 only if E1–E3 are done before the no-new-start cutoff. **Drop order:** E5 first, then E4; never abandon a started citation/grounding packet (E2).

---

## 3. Subscription-quota model allocation (subscription-backed routes ONLY)
| Lane | Model / route | Budgeted work | Cap (block new starts at) |
|---|---|---|---|
| Hwao | Fable — Claude Max direct subscription | direct, dispositions, verdict | Claude weekly 30% |
| Lana | Claude (same Max pool, direct lane) | E1 memo, E3 draft, E2 wording check | Claude weekly 30% (shared) |
| Kun | Codex via ChatGPT subscription (gpt-5.5) | E1 re-derivation, E2 gates, E3 compile | Codex weekly 30% |
| Goru | Antigravity / Gemini subscription (Gemini 3.1 Pro) | invariants, provenance maps, mechanical diffs | Gemini agent-pool weekly 20% |
| Tori | relay/receipts (openai-codex provider; Nous-managed) | receipts, DR driving, ledger | no bulk research; Nous top-up untouched |
| DR | consumer Gemini app (subscription) | E2 literature retrieval, ≤2 runs | 2 runs max; stop on throttle |

Quota snapshots (redacted meter) at T0 and every 30 min → `quota/usage_<UTC>.json`. Post-20260726 baselines: Claude 5%, Codex 1%, Gemini agent 0.22%, consumer Gemini 1%, Nous $42.60. **Never spend quota to hit a number; stop when the approved work is done.**

---

## 4. Global stop conditions
- Any cap in §3 reached; usage feed stale >10 min; any rate-limit/billing/OAuth/credential prompt (record + halt that lane).
- Input drift vs Task 0 hashes (`INPUT_DRIFT_BLOCKER`).
- DR throttle beyond one spaced retry.
- No new packet starts after **04:45 KST**; research hard stop **05:40 KST**; receipts/rollup hard stop **06:00 KST**. Never extend without a new owner instruction.
- Any prohibited-action requirement discovered mid-packet (e.g., a fix needs a DB write) → record blocker, stop the packet.

## 5. Exact morning deliverables (by 06:00 KST, 2026-07-28)
1. `MORNING_HANDOFF_20260728T0600KST.md` — one-screen outcome; per-packet DONE/PARTIAL/BLOCKED/DROPPED_BY_PRIORITY with markers; E1 tension verdict; E2 grounding coverage before→after; E3 candidate disposition; quota T0→final delta per lane; safety ledger (`DB:0 deploy:0 git:0 cockpit:0 billing:0`); `NO ACTIVE EXECUTION PHRASE`; exact next-approval options.
2. `FINAL_AUDIT.md` + `FINAL_ARTIFACT_MANIFEST.json` (Kun, x-checked Tori) — every artifact SHA-256'd; all 9 input hashes still OK; nothing outside the output root changed.
3. Packet artifacts as specified per lane above.
4. `OVERNIGHT_LEDGER.md` — timestamped (KST) start/ACK/done lines for every lane; ACK phrase: `ACK <packet> v2`.

## 6. Risks
- Conversion-formula reconciliation (E1) is scale-limited — it can bound, not fully resolve, the TENSION without a galSpecLine re-derivation (named future work; data not local).
- DR latency/throttle can zero out E2's retrieval — the partial path (local-corpus-only grounding) is pre-authorized above.
- C1 slots may be genuinely uncomputed — the honest deliverable is then the gap map, not a padded draft.
- Model-memory numeric drift remains the top integrity risk — provenance lines are mandatory for every number.

---
*Separately: `work/desi2/revision_aa60182/overnight_final/OVERNIGHT_V8_QUINTET_PLAN.md` (human-paper v8 scrutiny) is written and held un-dispatched; it is NOT part of this Paper-Board plan and would need its own approval.*
