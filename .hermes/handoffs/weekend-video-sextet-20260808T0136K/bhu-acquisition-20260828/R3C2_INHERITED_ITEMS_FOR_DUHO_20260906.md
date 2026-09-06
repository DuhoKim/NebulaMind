# Five open design questions in the signed census (V23), assembled for Duho — plain words, cost, recommendation, urgency

Written 2026-09-06 (Blanc's 13:29 KST note). None of these is in the narrow V24 amendment; all five were found by the machine referees
in the signed V23 text or its unchanged tooling. Each block says what it is, what it costs if left alone, my minimal recommendation
(my judgement, marked), and whether it must be settled BEFORE a first run or can wait until after. Nothing here is applied.

## D1 — a borrowed number whose source says "we choose"
**What it is.** When a paper uses a number it did not print but took from another paper in our corpus, the rules say: record it as
IMPORTED with the evidence "citation", quoting the source line. But if that source line itself says "we choose a = 2", the evidence
rule for citations does not fit the quote, and the tool's pair check can refuse the record. The two rules were written for different
cases and meet here.
**What it costs if left as is.** For every borrowed number whose origin paper made a choice, the seats will either file it as
BLOCKED (the arithmetic is never attempted, so the claim drops out of the reproduction count) or the two seats will classify it two
ways and it counts toward the 10% dispute stop. In a corpus where authors borrow each other's chosen constants freely, this could
remove a noticeable slice of claims from the tally for a bookkeeping reason, and the census would report fewer reproducible claims
than the papers actually allow.
**Minimal recommendation (my judgement).** One sentence: for a number routed through a pinned source, the source's own line is the
citation, whatever that line says about how the source got it; the source's own provenance is recorded on the source's record,
not on the borrower's. No class changes.
**Urgency.** Settle BEFORE the first run. It changes how records are filed during the run; fixing it afterwards means re-filing.

## D2 — no category for "an input the author set by hand"
**What it is.** The rule says every number that is not a result must be filed as excluded, with one of five reasons: equation number,
reference number, page or line number, date, or "attributed, not derived". A number like "we set the grid width to 256 cells" is
none of those. It is not a result, and it has no reason to be filed under.
**What it costs if left as is.** Each seat will improvise: some will squeeze such numbers into "attributed, not derived", some will
include them as claims (and then fail to reproduce them, since nothing derives a chosen width), and the two seats will not agree.
Every disagreement of this kind either stops the census under the denominator-dispute class or, if it slips through, pads the
"failed" count with numbers that were never claims. The denominator, the single most important number the census reports, becomes
wrong by however many such inputs the 89 texts contain, plausibly dozens.
**Minimal recommendation (my judgement).** Add one exclusion reason, "author-specified input", defined as a number the paper sets
rather than derives. This is a taxonomy change and is yours.
**Urgency.** Settle BEFORE the first run. It goes to the denominator.

## D4 — a lane-side check with no PASS/FAIL code
**What it is.** After the seats run, the lane owner checks the provider log to confirm the kimi seat never fell back to a different
model. The document names that check but gives it no result code, so nothing in the record says whether it passed.
**What it costs if left as is.** If a seat had silently run on a different model, the census would still be filed as if both
seats were the engines named in the dispatch record, and no line in the record would show it. A reader could not tell.
**Minimal recommendation (my judgement).** One code, `C7_NO_FALLBACK=PASS|FAIL|NOT_RUN`, printed by the lane owner with the log
line it rests on; FAIL voids that seat's limb. A new control code, so yours.
**Urgency.** Can wait until AFTER a first run if the lane owner records the check in the run log anyway (I will); settling it
before costs one line and removes the "can wait" caveat.

## D7 — the auditor reads the answers before "re-deriving without sight of them"
**What it is.** The third seat's job is to audit the full ledgers for completeness and then re-derive a sample "without sight of
earlier work". As written, the ledger it audits first already contains every outcome and every reproduced number. It cannot
un-see them before re-deriving.
**What it costs if left as is.** The audit's re-derivations are not independent: an auditor that has seen "REPRO_FAILED,
reproduced 16.2 vs printed 17.4" is checking, not re-deriving. A tally the audit confirms might still be wrong in exactly the way an
independent seat would have caught. The audit's PASS would then mean less than the document says it means, and the interpretation
that follows rests on it.
**Minimal recommendation (my judgement).** Split the auditor's inputs: for the completeness audit, give it the candidate list with
inclusion decisions but with outcomes and numbers blanked; for the re-derivation, give it only claim identifiers. Reveal the
sealed outcomes to it only after both are printed. This reshapes C6's inputs, so yours.
**Urgency.** Settle BEFORE the first run. The audit runs at the end, but the sealed artefacts it receives are produced during the
run, and blanking them afterwards from a sealed file would itself look like tampering.

## D8 — the label `DERIVED_ONLY` promises more than it means
**What it is.** A claim whose inputs are all derived, standard constants, or the paper's own measurements is labelled DERIVED_ONLY.
Read as ordinary English, the label says "derived and nothing else", which is not what the rule counts.
**What it costs if left as is.** Nothing in the tally; the rule is exact and the label is only a name. The cost is in the paper:
a reader who sees "DERIVED_ONLY" will believe a stronger claim than the census makes, and a referee will say so.
**Minimal recommendation (my judgement).** Rename to `DERIVED_STANDARD_OR_MEASURED_ONLY` everywhere it is a live output token
(master, lane tool, interpretation protocol), membership unchanged, with a rename notice in §10. A rename, so yours.
**Urgency.** Can wait until AFTER a first run. It changes no filed outcome; it can be applied as an amendment before the paper.

## In one line each, for the morning
- D1 borrowed-choice evidence: BEFORE the run.
- D2 author-specified inputs: BEFORE the run (it is the denominator).
- D4 no-fallback code: after is acceptable; before is one line.
- D7 auditor independence: BEFORE the run.
- D8 the label: after.
Three of five block a first run: D1, D2, D7. Each is one sentence to one class or one control's inputs, and each needs your word
because it changes a class, a taxonomy, or a control's contract. None touches the scope clause V24 repairs.
