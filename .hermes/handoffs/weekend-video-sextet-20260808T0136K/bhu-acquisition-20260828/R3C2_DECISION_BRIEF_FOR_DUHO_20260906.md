# R3C2 — decision brief for Duho: three method choices, UNADOPTED until he says so (2026-09-06 21:52 KST)

**What this is.** Three choices the reproduction census cannot run without. Each is prepared, tooled, tested, and reviewed; none is
adopted. This brief is a lane preparation relayed by Blanc; it approves nothing by itself. V23 stays the signed design of record,
V25 (with the approved AUTHOR_SPECIFIED_INPUT) stays the living draft, the census stays stopped.

**What was examined, honestly.** Revisions 1, 2 and 3 of the candidate were each reviewed independently by two engines (codex, kimi),
seven identical tokens per round, every finding either repaired or stated as a limit. Revision 4 carries the round-3 repairs (all
routine, all with fail-first controls); it was NOT re-reviewed by two engines — Codex replayed its own round-3 counterexamples against
it and found them closed (receipt `.hermes/CODEX_TORI_R4_TARGETED_CLOSURE_20260906.json`). Full record:
`R3C2_CANDIDATE_REVIEW_RECONCILIATION_20260906.md`.

---

## Choice 1 — D1: a number a paper borrows from another paper in the corpus, where that other paper's own line says "we choose" (or "we fit")

**The question.** Does the borrower's number "rest on an import" or "rest on a choice"?

**Options.**
- **(B) RECOMMENDED — it rests on an import, evidenced at the borrower.** The record quotes the BORROWER's citing sentence; the value is
  machine-matched at the source's line; the source's own wording is never applied to the borrower. Both reviewers preferred this.
- (A) the same outcome, evidenced by quoting the SOURCE's line. Same classification, different evidence bytes; the staged tool would
  have to be re-staged for it.
- (Change) an inherited origin such as `IMPORTED_CHOSEN`: the census could then say "rests on a choice made elsewhere". Cost: a taxonomy
  expansion and a second pass over every import; not prepared.
- (Defer) — then such records stay BLOCKED or split, and a first run cannot file them.

**Consequence of (B) in plain words.** The census will say "this paper's number rests on an import" and will NOT say "rests on a
choice" when the choice was another paper's; the choice shows on the source paper's own record. Machine checks now bind every
printed value to its claiming paper, match numeric tokens not substrings, verify the source's bytes against the manifest, and take
the first line carrying symbol and numeral; whether a quotation really cites THAT value stays seat judgement, checked by the second
seat and by the audit for selected claims.

## Choice 2 — D7: how independent the audit seat is

**Options.**
- **(Stronger) RECOMMENDED — the auditor first enumerates all 89 texts itself with no seat ledger in sight;** its enumeration is
  census-checked and sealed; the selection is computed only after that seal and the external seed; the auditor gets identifiers with
  file and line only; its re-derivations are sealed BEFORE any seat ledger is released; only then the comparison runs. An omission in
  either direction fails the audit; a mere disagreement is counted under a 10% rule.
- (Weaker) the auditor sees the seats' lists with outcomes blanked, then re-derives. Anchoring on those lists makes discovery of a
  passage both seats missed less likely (direction only; no magnitude measured).

**Consequence and cost.** Under the stronger version `CENSUS_COMPLETE` requires a run record showing the auditor's enumeration
preceded any exposure and its re-derivations were committed before release — the tools commit bytes, the custodian's dispatch record
fixes the order. Cost: a third full reading of the corpus plus the assigned re-derivations; runtime unmeasured. What the audit's PASS
then means: bounded evidence, not proof of completeness; shared reader error and prior exposure remain possible.

## Choice 3 — batch reading: how a seat reads 89 texts it cannot hold in one session

**Options.**
- **(Ownership batches) RECOMMENDED — 12 batches partition which texts a session ENUMERATES; every session holds ALL 89 texts** so a
  borrowed number can be looked up wherever it lives (round 1 found that withholding texts breaks the import rule; repaired). Per-batch
  artefacts are sealed in order; a pure-function join with global source-based identifiers produces one candidate file, one exclusion
  file, one ledger per seat; the pinned census and full-corpus validation then run over the joined files.
- (Change) a line-balanced partition instead of manifest row order — the row-order batches range from about 3,300 to about 18,000
  non-blank lines; a balanced one is a different pure function of the same manifest, not prepared.
- (Change) require batch 1 to confirm session capacity before batch 2 is dispatched — recommended as part of the run plan.
- (Defer) — no seat completes the corpus on the evidence of the limb-B death finding; whether batching is the remedy is what batch 1
  tests.

**Consequence in plain words.** One denominator, mechanically; two independent readers, each across twelve sessions. Lost and
stated: cross-batch consistency of one reader's judgement — the report gives between-seat disagreement by batch, which does not
measure within-reader drift. Cost: 12 sessions × 2 seats (+12 for the auditor under the stronger D7).

---

## Fingerprints of what was tested
- Candidate (D1, D7 clause text): `R3C2_D1_D7_CANDIDATE_CLAUSES_20260906.md` sha256 `3b959684e2262e5fd27fca5c122880992d12553a6fc10daeac256269bda8144c`
- Batch preparation: `R3C2_BATCH_PREPARATION_UNADOPTED_20260906.md` sha256 `1f7206e40f9150fbb295928ba7baf7dcfd096e28da25e61067f1f5553dda3204`
- Staged kit pin sheet (7 files; 111 controls, 38 deletion probes, PASS): `r3c2_staged_d1d7/R3C2_STAGED_D1D7.sha256` sha256 `62eafdfa5fb94aa7cef9714b63475d3562cd416469a050483c7baf7b272070ef`
- Review reconciliation: sha256 `08f36942fa0757470173e35aed528040912fe9db03130ae8f644bdc9cb55eb85`

## What his approval would and would not authorize
**Would:** the three method choices as design decisions, in his words, recorded by the lane under §10's record form.
**Would NOT:** any of the following, each a separate step with its own gate — writing the integrated draft (V26) that carries the
choices; re-pinning the seat tool and rebuilding the packet; C0 reachability by two seats; the two-seat gate; the approval procedure
of 11:11 (bytes and digest presented in the codex conversation, Blanc recomputing); the run word; and the run plan additions the
reviews named (per-dispatch inventory and probes, fresh auditor context, custodian-only selection, release events recorded).

**The line for Duho, in plain words:** D1 — B / A / change / defer. D7 — stronger / weaker / defer. Batching — ownership batches as
prepared / line-balanced / defer. Anything not chosen stays exactly as it is.

R3C2_DECISION_BRIEF — preparation, UNADOPTED
