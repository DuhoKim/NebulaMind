# R3C2 — D1 and D7 clause CANDIDATES (UNADOPTED; Blanc's orders 19:49 / 19:51 / 20:01 KST; revision 2 after two independent reviews, 2026-09-06 20:38 KST)

**Status.** Nothing here is adopted, in V25, gated for approval, installed or run. V23 (`55b466fa…`) is the signed design of record; the
V25 living draft (`ab6352d3…`) carries only the approved D2. This file holds the exact texts that would be dropped into the operative
draft if Duho accepts them, each marked TORI'S RECOMMENDATION, UNADOPTED. The batch-reading choice is kept in its own file
(`R3C2_BATCH_PREPARATION_UNADOPTED_20260906.md`): an execution question, ruled on separately.

**Review record.** Revision 1 (digest `cb78eef0…`) was reviewed independently by codex (`R3C2_CANDIDATE_REVIEW_codex_20260906.md`, access
proven by the wrapper) and kimi-k3 (`R3C2_CANDIDATE_REVIEW_kimi_20260906.md`, access line verified by hand). Both returned the same seven
tokens: CANDIDATE_D1=SOUND_WITH_REPAIRS, CANDIDATE_D7=SOUND_WITH_REPAIRS, BATCH_PREP=UNSOUND, TOOLING_MATCHES_CLAUSE=NO,
COUNTEREXAMPLE_HANDLED=YES, IMPORTED_RULE_BREAKS_PARTITION=YES, STAGED_TESTS=PASS. Their findings are reconciled BY TOPIC in
`R3C2_CANDIDATE_REVIEW_RECONCILIATION_20260906.md`; every accepted repair is in this revision and in the staged kit. This revision has
NOT yet been reviewed; a second round is dispatched on it and its verdicts will be filed beside the first.

---

## D1 — a borrowed number whose named source's own line states a choice — TORI'S RECOMMENDATION, UNADOPTED

**Two wordings of one rule.** Both assign `origin` `IMPORTED` at the borrower whatever the source's line says about how the source
obtained the value ("we choose", "we fit", "we measure", "we adopt from X"). They assign the same classification (status, origin,
value); their EVIDENCE RECORDS differ (which file and line `origin_evidence` names). The staged tool implements the SECOND wording
only; accepting the first would require re-staging the validate rule (both reviews).

**Wording A (Tori's, first draft):** the named source's own line is the citation — `ORIG_CITATION` quotes that line, with its file and line.

**Wording B (the V25 review's; RECOMMENDED — both reviewers concur, because it never applies the source's verb to the borrower and puts
the operative evidence at the borrower):** exact clause, replacing the last sentence of §2's IMPORTED rule and adding to C3's pair rule:

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
> **Machine floor, stated.** `validate` checks: the citing file is the claiming file bound through the candidate file; the two files differ;
> the source is an exact manifest row with verified bytes; the quotation is non-empty and present at the cited claiming line; the value
> is a numeric token at the cited source line and that line is the first carrying symbol and numeral. That the quoting sentence is a
> genuine citation of THAT value — not a sentence naming the source for something else — is seat judgement, caught by the second seat
> and by C6's re-classification, never by the machine.

**What accepting it changes about what the census can conclude.** A borrower's claim whose input was chosen or fitted by another paper
in the corpus is ATTEMPTED with that input (an arithmetic-group outcome follows only if the rest of the recipe and the numbers hold;
`REPRO_FAILED` remains possible) and its `rests_on` reflects `USES_IMPORTED` unless a more severe root is present. At the borrower the
census says "rests on an import", not "rests on a choice"; the choice is recorded on the source paper's own records when that paper is
censused; the census does not promise to follow provenance across papers. What the census can no longer say is "this paper's number
rests on a choice" when the choice was made by a different paper — unless Duho takes the "change" route: an inherited origin
(`IMPORTED_CHOSEN` / `IMPORTED_FITTED` / …), a taxonomy expansion and a second pass over every import.

**Line for Duho:** accept B / accept A (re-stage the tool first) / change (inherited provenance) / defer. Blocks a first run: without one
of them such records are BLOCKED or split.

---

## D7 — the C6 auditor's independence — comparison, then TORI'S RECOMMENDATION, UNADOPTED

**Comparison, as ordered.** My first clause gave the auditor the seats' ledgers with outcomes, values and origins blanked, then claim
identifiers. The V25 codex review's version has the auditor enumerate from the sources FIRST, with no ledger in sight, and see the
sealed ledgers only after its own enumeration and re-derivations are committed. **The review's version is the STRONGER, and it is the
one put to Duho:** the weaker version exposes the seats' inclusion decisions before the completeness audit, which makes discovery of a
passage both seats missed LESS LIKELY (an anchored auditor audits "what they missed that I notice" rather than enumerating afresh);
direction only — no magnitude has been measured. The stronger version withholds those decisions until independent work is committed.

**Exact clause (STRONGER, recommended), replacing C6's opening up to the sampling formula (formula and seed definitions unchanged):**

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

**Weaker alternative (my earlier clause), kept for the record:** the auditor receives the seats' ledgers with outcomes, values and
origins blanked for the completeness audit, then claim identifiers for re-derivation, and sees the sealed outcomes only after both
are printed.

**Repair history on this clause.** Revision 1's PASS predicate excluded only a sealed candidate missing from the auditor's enumeration
(Codex's probe, relayed by Blanc 20:01): repaired to both directions. The two reviews of revision 1 then found the comparison
narrower than the words (excluded-only passages vanished; zero denominator passed; auditor census not enforced; selection trusted, not
recomputed; re-derivations unsealed; "both sealed ledgers" when the object is the merged file): all repaired above and in the kit,
each with a control that asserts its exact failure and a deletion probe. Kimi's reading of the excluded-only cases is adopted (a passage
the seats never enumerated is incompleteness whatever the auditor's disposition; a sealed exclusion the auditor never listed is a
dispute) because it is the stricter one that still lets a mere disagreement follow a stop rule instead of vanishing.

**What accepting the stronger version changes about what the census can conclude.** `CENSUS_COMPLETE` and `CENSUS_PARTIAL` then rest on
an audit whose enumeration was produced without sight of the seats' lists and whose re-derivations were sealed before the seats'
numbers were released. The audit's PASS then rests on an independent enumeration and blind re-derivation rather than on an anchored
review of the seats' lists; it is bounded evidence, not proof of corpus completeness. Cost: a third full enumeration plus the assigned
re-derivations and the comparison; runtime is unmeasured; an auditor `census` PASS is enforced as a precondition of the stage-1 seal.

**Line for Duho:** accept the stronger / accept the weaker / change / defer. Blocks a first run: the sealed artefacts the auditor
receives are produced during the run.

---

## Errata the candidate would also carry (routine wording, no rule changed) — UNADOPTED

- **§1's excluded-kinds sentence still names five kinds** (kimi V25 F1). Exact replacement:
  > "Excluded, by definition and not by taste: numerals that are equation numbers, reference numbers, page or line numbers, dates,
  > values the paper attributes to another work without deriving, or numerals the paper sets as inputs to its own calculation rather
  > than asserts as results of its own (`AUTHOR_SPECIFIED_INPUT`, §3)."
- **The header's status line** would state exactly which of D1 / D7 / batching Duho accepted and in which words, per §10's record form.
- **C6's "sample" wording**: wherever C6 says the auditor samples, the SAMPLE is of claims and the ENUMERATION is of every text.

## Staged tooling and tests for these clauses — STAGED, NOT INSTALLED

Directory `r3c2_staged_d1d7/`; every file is pinned in `r3c2_staged_d1d7/R3C2_STAGED_D1D7.sha256` and this document prints no per-file
hash of its own (kimi F10: the stale-copy family). The pinned seat tool, packet, brief and pin sheet are untouched.

- **D1 in code** (`validate <ledger> <sources_dir> <candidates.json>`): implements Wording B only — see the machine floor above.
  Controls: positive ("we choose" source line, borrower's citing sentence); negatives, each asserting exactly its failure: no candidate
  file; citing sentence quoted from a third text; verbatim at the wrong sentence; empty quotation; value a substring of another numeral
  ("2" in "b = 20"); a second matching line filed instead of the first; source not a manifest row; source bytes tampered; no manifest;
  record naming its own file. Deletion probes for each of the eight load-bearing checks.
- **D7 in code** (`audit seal-enumeration | select | handout | seal-rederivation | compare`): as the clause states. Controls: the
  stage-ordered positive; first-write refusals; select before any seal refused; bad seed; census-failing auditor enumeration not sealed;
  enumeration changed after its seal; re-derivations changed after their seal; selection emptied with the digest retained (recomputation
  fails it); the four completeness asymmetries (the Codex/Blanc both-seats-omit case from two seat ledgers, its reverse, an auditor-excluded
  passage the seats never listed, a sealed exclusion the auditor never listed); disputes at 10% (PASS, counted) and 15% (FAIL); zero
  denominator; outcome, origin and missing re-derivation mismatches; disputed rows carry both dispositions; the handout carries ids,
  file and line only. Emitted completeness results: `C6_COUNTEREXAMPLE_EXHIBIT.txt`.
- **Batch tooling** is described in `R3C2_BATCH_PREPARATION_UNADOPTED_20260906.md`.
- **Test run** (`/usr/bin/python3 -E r3c2_staged_tests.py`, 2026-09-06 20:38 KST): `controls=84 passed=84 failed=0`, `STAGED_TESTS=PASS`; 29 deletion
  probes, each showing the matching negative turns to PASS when its check is neutralised.

**What installing would take** (not done): a version carrying Duho's ruling → the seat tool re-pinned in the packet's pin sheet and the
master's §2/C3/C6 text → packet rebuild → C0 by two seats → two-seat gate → the 11:11 approval procedure.

## Not in this file
D2 (adopted "for now", already in the V25 draft); D4 and D8 (can wait); the batch-reading choice (own file); the cosmetics from the V25
reviews (recorded in `R3C2_V25_GATE_RECONCILIATION_20260906.md`).

R3C2_D1_D7_CANDIDATE_CLAUSES — UNADOPTED — revision 2
