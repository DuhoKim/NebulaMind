# R3C2 — decision brief for Duho: three method choices, UNADOPTED until he says so (2026-09-06 21:52 KST)

**What this is.** Three choices the reproduction census cannot run without. Each is prepared, tooled, tested, and reviewed; none is
adopted. This brief is a lane preparation relayed by Blanc; it approves nothing by itself. V23 stays the signed design of record,
V25 (with the approved AUTHOR_SPECIFIED_INPUT) stays the living draft, the census stays stopped.

**Review history, honestly.** Three rounds. Revisions 1 and 2 were each reviewed independently by two engines (codex, kimi) with
seven identical tokens per round: round 1 found the batch proposal UNSOUND (a session holding only its own texts cannot serve the
import rule — repaired by partitioning ownership, not access); round 2 found the mechanism sound with executable tool gaps, repaired.
Round 3 was a bounded verification of revision 3: both engines found every round-2 repair present and, between them, THREE unique
new defects (both found the unknown-claim binding gap and the seed-contract gap; codex alone found the root-seal gap). **Readiness on
revision 3 was split: codex READY_FOR_PRINCIPAL=NO, kimi YES.** Revision 4 repaired the three defects and the wording residues with
fail-first controls (111 controls, 38 deletion probes). Whether the split survives revision 4 is NOT settled: no reviewer has issued a
readiness token on revision 4. The evidence that exists is narrower — Codex replayed its own round-3 counterexamples against revision 4
in a fresh directory and found them closed (`.hermes/CODEX_TORI_R4_TARGETED_CLOSURE_20260906.json`); those were Codex's own
reproductions of the reviewer fixtures, not the reviewer issuing a new verdict, and they closed the three unique executable findings
only. Codex's NO had rested on those findings plus the vocabulary and count residues, also repaired. A fourth round, on order, would
give revision 4 a verdict of its own; it is not guaranteed to settle every issue. Full record: `R3C2_CANDIDATE_REVIEW_RECONCILIATION_20260906.md`.

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

**Exact recommended D1 clause (wording B), verbatim from the candidate:**

> **A value the claiming paper does not print but traces to a named source is classified `PRINTED` with `origin` `IMPORTED` only when
> that source is an enumerable text of `R3C2_CORPUS_MANIFEST.md` whose bytes verify against its manifest row, and the value machine-matches
> as a numeric token at the cited source line.** The record's `source_file`/`source_line` name that external value line; `origin_evidence`
> carries `ORIG_CITATION` with a non-empty verbatim quotation of the CLAIMING paper's sentence naming the source, at the claiming paper's
> own file and line (the claiming file is the file of the candidate row the record's `claim_id` names). The origin records the claiming
> paper's import regardless of how the external source obtained the value; no reason code is applied to the source's line. **Where the
> value machine-matches at more than one line of the named source, the seat files the first line carrying both the symbol and the
> numeral; `validate` fails any other line.** If the named source is not enumerable or the value does not match there, file `REPRO_BLOCKED`
> under §3. C3's pair rule: `ORIG_CITATION` is satisfied by that quotation at the claiming paper.
>
> **Machine floor, stated.** For EVERY `PRINTED` record `validate` first binds the claim to its claiming file through the candidate file;
> a record whose value line lies in another file must be `IMPORTED` with `ORIG_CITATION`, whatever reason code was submitted. For an
> import it then checks: the citing file is the claiming file; the two files differ; the source is an exact manifest row with verified
> bytes; the quotation is non-empty and present at the cited claiming line; the value is a numeric token at the cited source line; some
> line of the source carries both symbol and numeral, and the cited line is the first such line. Whether the quotation cites THAT value
> is seat judgement; the second seat and C6 may detect an error, but can share it, and C6 re-classifies inputs only for selected claims.

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

**Exact recommended D7 clause (stronger), verbatim from the candidate:**

> **C6 — audit, with a frozen sampling frame and an independent enumeration.** A third independent seat, on a different engine from both
> census seats, **first** enumerates and classifies candidate passages itself from EVERY pinned source — all 89 enumerable texts of
> `R3C2_CORPUS_MANIFEST.md`, a complete independent enumeration, never a sample of texts — under §1's rule, with no seat candidate,
> exclusion, input or outcome ledger in its dispatch inventory, and writes its own candidate and exclusion ledgers. The custodian runs
> `census` over them and, only on PASS, records their digests in a first-write stage-1 seal (`audit seal-enumeration`). **Second**, after
> receipt T and the supply of the external seed, the custodian computes the selection (`audit select`, which refuses without the stage-1
> seal) — every arithmetic-group claim plus `k = min(max(1, ceil(0.20 × N)), R)` of the remaining included claims, drawn as already
> defined — and hands the auditor claim identifiers with source file and line ONLY (`audit handout`); the auditor re-derives each
> assigned claim and re-classifies each of its inputs' `origin` from the pinned sources, and the custodian seals those re-derivations by
> digest (`audit seal-rederivation`) BEFORE any sealed ledger is released. **Only then** are the sealed (merged) candidate, exclusion and
> input ledgers opened to the comparison (`audit compare`), which recomputes the selection from the sealed candidates and seed and fails
> on any disagreement, and writes and prints `C6_AUDIT.json` with (i) one completeness row per passage key (file, line, numeral) in the
> UNION of the sealed and the auditor's enumerations — both presences, both dispositions, both exclusion kinds, and a result: `MATCH`,
> `OMISSION`, or `AUDIT_INCLUSION_DISPUTED` — and (ii) `MATCH`/`MISMATCH` per audited claim (outcome; printed and reproduced values for
> arithmetic outcomes) and per re-classified input origin. **Omissions:** a sealed INCLUDED passage absent from the auditor's enumeration;
> a passage the auditor lists (included OR excluded) that the sealed ledgers omit — each is ledger incompleteness and files
> `CENSUS_AUDIT_FAILED`. **Disputes:** a passage both sides list but dispose differently, and a sealed EXCLUDED passage absent from the
> auditor's enumeration, are `AUDIT_INCLUSION_DISPUTED`, listed with both dispositions and counted; above 10% of the sealed included
> denominator the audit files `CENSUS_AUDIT_FAILED`; at or below it the count is reported. A sealed denominator of zero with any passage
> on either side fails. `C6_AUDIT_SAMPLE=PASS` only if the artefact exists and is printed, both seals match, the recomputed selection
> matches, no row is an omission, the dispute rate is at or below 10%, and no audited claim or origin is `MISMATCH`. **What PASS means:**
> the enumerated predicates held over the sealed files; it is bounded by the custodian's dispatch and release record (the seals fix
> WHAT was committed, the dispatch record — inventoried and access-proven like the seats' — fixes WHEN, relative to release) and by
> shared reader error; prior exposure cannot be excluded — the same floor C4 states for the seats. Its enumeration reads the corpus
> under the same reading discipline as the census seats, batch for batch if the census is batched, including the same cross-batch
> source access for re-classifying imports.

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
- (Defer) — the one observed single-session attempt died at eleven texts; that motivates batching without proving no engine could
  ever complete the corpus. Whether this batching is the remedy is what batch 1 tests.

Already part of the prepared plan, not a choice: batch 1 confirms session capacity before batch 2 is dispatched.

**Consequence in plain words.** One denominator, mechanically; two independent readers, each across twelve sessions. Lost and
stated: cross-batch consistency of one reader's judgement — the report gives between-seat disagreement by batch, which does not
measure within-reader drift. Cost: 12 sessions × 2 seats (+12 for the auditor under the stronger D7).

---

## Fingerprints of what was tested (recomputed after the last edit of every file named, 2026-09-06 22:00 KST)
- Candidate (D1, D7 clause text): `R3C2_D1_D7_CANDIDATE_CLAUSES_20260906.md` sha256 `3b959684e2262e5fd27fca5c122880992d12553a6fc10daeac256269bda8144c`
- Batch preparation: `R3C2_BATCH_PREPARATION_UNADOPTED_20260906.md` sha256 `1f7206e40f9150fbb295928ba7baf7dcfd096e28da25e61067f1f5553dda3204`
- Staged kit pin sheet (7 files; 111 controls, 38 deletion probes, PASS): `r3c2_staged_d1d7/R3C2_STAGED_D1D7.sha256` sha256 `62eafdfa5fb94aa7cef9714b63475d3562cd416469a050483c7baf7b272070ef`
- Review reconciliation: sha256 `f12870245912d9dde04eee9f8ca71031335edd0b02c60d7008ac0804ef0dda66`

## What his decision covers, and what follows without asking again
**His decision:** the three method choices, in his words, recorded by the lane under §10's record form.
**Follows as routine preparation, already authorized, no further asking:** the integrated draft that carries his choices (an
UNADOPTED integrated candidate already exists as a separate file and is adjusted to whatever he chooses; the earlier pause on new
numbered versions was the coordinator's own anti-churn measure, Blanc's, not a limit of Duho's — his limits are the one holdout, the
sample sizes, the exclusions, custody, blindness and the frozen V23); re-pinning the seat tool and rebuilding the packet; C0
reachability by two seats; the two-seat gate; independent review; the run-plan
additions the reviews named (per-dispatch inventory and probes, fresh auditor context, custodian-only selection, release events
recorded). These are technical checks the lane runs, not permissions it asks for.
**Remains his, later and separately:** approval of the final version's bytes and digest by the procedure of 11:11 (presented in the
codex conversation, attested by Codex, Blanc recomputing the digest), and his approval to run, recorded as given in conversation.

**The line for Duho, in plain words:** D1 — B / A / change / defer. D7 — stronger / weaker / defer. Batching — ownership batches as
prepared / line-balanced / defer. Anything not chosen stays exactly as it is.

R3C2_DECISION_BRIEF — preparation, UNADOPTED
