# R3C2 — D1 and D7 clause CANDIDATES (UNADOPTED; Blanc's order 19:49 KST; written 2026-09-06)

**Status.** Nothing here is adopted, in V25, gated for approval, or run. V23 is the signed design of record; the V25 living draft
(`ab6352d3…`) carries only the approved D2. These are the exact texts that would be dropped into the operative draft if Duho accepts
them, each marked TORI'S RECOMMENDATION, UNADOPTED. The batch-reading choice is kept out of this file on purpose (see
`R3C2_V25_PROPOSED_SUCCESSOR_20260906.md`, item 4): it is an execution question, not a clause.

---

## D1 — a borrowed number whose named source's own line states a choice — TORI'S RECOMMENDATION, UNADOPTED

**Exact clause, replacing the last sentence of §2's IMPORTED rule and adding one line to C3's pair rule:**

> **For an input the paper does not print but traces to a named source that is itself an enumerable text of the manifest, the named
> source's own line is the citation:** the record carries `status` `PRINTED` (from that source), `origin` `IMPORTED`, `origin_evidence`
> `ORIG_CITATION` quoting the cited line verbatim with its file and line, **whatever that line says about how the source obtained the
> value** — "we choose", "we fit", "we measure" and "we adopt from [x]" are all citations at the borrower. The source paper's own
> provenance for that value is recorded on the source paper's own records when that paper is censused, never on the borrower's
> record, and the two are joined only by the lane's `compute` through `derived_from`/`root_origins`, never by the seat.
> C3's pair rule: `ORIG_CITATION` is satisfied by a verbatim quotation of the cited line at the cited source; the reason-code
> precedence is not applied to the source's line at the borrower.

**What accepting it changes about what the census can conclude.** A borrower's claim whose input was chosen or fitted by another
paper in the corpus files as reproducible from its stated inputs (arithmetic-group outcome) with `rests_on = USES_IMPORTED`. At the
borrower the census says "rests on an import", not "rests on a choice"; the choice is visible one hop away on the source's record,
and the lane's `compute` can follow `derived_from` across papers where the seats recorded it. What the census can no longer say is
"this paper's number rests on a choice" when the choice was made by a different paper — unless he takes the "change" route: an
inherited origin (`IMPORTED_CHOSEN` / `IMPORTED_FITTED` / …), which is a taxonomy expansion and a second pass over every import.

**Second wording for the same rule, from the V25 codex review, put beside mine because it is at least as clean:** the import is
evidenced at the BORROWER'S own citing sentence ("we take a from Smith (2020)"), quoted verbatim as `ORIG_CITATION`, while `source_file`
and `source_line` point at the external value line where the number machine-matches; the origin records the claiming paper's import
regardless of how the source obtained the value. Under it the "we choose" conflict never arises, because the quotation is a genuine
citation and the source's line is only the match target. My clause reaches the same filings by declaring the source's line the
citation; the review's reaches them by quoting the borrower's sentence. **Recommendation between the two, my judgement:** the review's
wording — it needs no rule about what the source's line says.

**Line for Duho:** accept (review's wording) / accept (Tori's wording) / change (inherited provenance) / defer. Blocks a first run:
without one of them such records are BLOCKED or split.

---

## D7 — the C6 auditor's independence — comparison first, then TORI'S RECOMMENDATION, UNADOPTED

**Comparison, as ordered.** My V25-proposal clause gave the auditor, first, the seats' candidate and exclusion ledgers with outcomes,
values and origins BLANKED (ids, files, lines, numerals, dispositions kept) for the completeness audit, then claim identifiers for
re-derivation. The V25 codex review (its "D2", our D7) recommends **source-only independent enumeration before any ledger exposure**:
the auditor first enumerates and classifies candidate passages itself from every pinned source, with no access to either seat's
candidate, exclusion, input or outcome ledgers; the audit assignment (every arithmetic-group claim plus the seeded sample) reaches it
only after receipt T and the seed; the sealed ledgers are opened to it only after its own enumeration and re-derivations are printed.

**Verdict of the comparison: the review's version is STRONGER, and it is the one put to Duho.** Under my clause the auditor sees the
seats' inclusion decisions before auditing completeness, so "completeness" becomes "did they miss anything I notice given their
list", anchored to their choices; under the review's, completeness is a comparison of two independent enumerations, and a passage
both seats missed can be found. My clause is kept below only as the weaker alternative.

**Exact clause (STRONGER, recommended), replacing C6's opening sentence up to the sampling formula (formula and seed definitions
unchanged):**

> **C6 — audit, with a frozen sampling frame and an independent enumeration.** A third independent seat, on a different engine
> from both census seats, **first** enumerates and classifies candidate passages itself from every pinned source under §1's rule,
> with no access to either seat's candidate, exclusion, input or outcome ledgers, and writes its own candidate and exclusion
> ledgers (`census` PASS required). **Second**, after receipt T and the supply of the external seed, the custodian computes the
> audit selection — every arithmetic-group claim plus `k = min(max(1, ceil(0.20 × N)), R)` of the remaining included claims, drawn as
> already defined — and hands the auditor claim identifiers with their source file and line only; the auditor re-derives each
> assigned claim and re-classifies each of its inputs' `origin` from the pinned sources, and prints the results. **Only then** are
> the sealed ledgers opened to it; it writes `C6_AUDIT.json` with (i) the completeness comparison — every candidate in the sealed
> ledgers matched to its own enumeration or listed as unmatched, and every passage in its own enumeration absent from the sealed
> ledgers listed — and (ii) `MATCH`/`MISMATCH` per audited claim and per re-classified origin. `C6_AUDIT_SAMPLE=PASS` only if the
> artefact exists and is printed, no audited claim is `MISMATCH`, and the completeness comparison lists no sealed candidate absent
> from the auditor's enumeration whose inclusion §1 requires. Its enumeration reads the corpus under the same reading discipline
> as the census seats (if the census is batched, so is the audit, batch for batch).

**Weaker alternative (my earlier clause), kept for the record:** the auditor receives the seats' ledgers with outcomes, values and
origins blanked for the completeness audit, then claim identifiers for re-derivation, and sees the sealed outcomes only after both
are printed.

**What accepting the stronger version changes about what the census can conclude.** `CENSUS_COMPLETE` and `CENSUS_PARTIAL` then
rest on an audit that is a genuine independent replication in both senses: the auditor's enumeration can find passages both seats
missed (which the weaker version cannot), and its re-derivations were made without sight of the seats' numbers. The audit's PASS
becomes the strongest statement in the design. Cost: a third full reading of the corpus (batched like the rest), so the audit's
time roughly equals one census seat's; and an auditor `census` PASS becomes a precondition of `C6_AUDIT_SAMPLE=PASS`.

**Line for Duho:** accept the stronger / accept the weaker / change / defer. Blocks a first run: the sealed artefacts the auditor
receives are produced during the run.

---

## Not in this file
D2 (adopted "for now", already in the V25 draft); D4 and D8 (can wait); the batch-reading choice (execution; proposal item 4); the
cosmetics from the V25 reviews (recorded in `R3C2_V25_GATE_RECONCILIATION_20260906.md`).

R3C2_D1_D7_CANDIDATE_CLAUSES — UNADOPTED
