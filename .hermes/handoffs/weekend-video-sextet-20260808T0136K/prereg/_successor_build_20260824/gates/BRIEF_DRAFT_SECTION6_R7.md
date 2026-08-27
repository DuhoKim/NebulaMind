# DRAFTING BRIEF — R7. One finding only. Do not touch anything else.

`SECTION6_DRAFT_AGY_R6B.md` (sha256 `f9743e836ff791906c94726991a7db43f04ef1a82baaaf4b9e0bea60c2c3d566`)
was refereed NOT CLEAR by GPT56 and CODEX. Read `SECTION6_REVIEW_R6B_GPT56.md` and
`SECTION6_REVIEW_R6B_CODEX.md` before drafting.

**This brief covers finding 2 and nothing else.** Findings 1 and 3 are real and blocking, but both
referees place their repairs in a replacement **BS-2a design artifact** — byte-exact schemas,
canonical serialization, a named independent verifier, an attestation chain, fixture oracles. That
is a separate deliverable and not §6 prose. Do not attempt it here. Do not invent schemas.

## What held — do not disturb it

CODEX ran a mechanical R6→R6b diff and confirms only the requested clause restoration, the typo fix
and the added Part 5 item. All three protected properties held with substantive clause bodies:
universal ban (clause 1), committee G→H→I with restored clause 5, and the BS-5f → BS-L → unblinding
chain (clause 3, rows J/N/O/P). The literal checksum attack failed — no cutout digest appears on the
projection. The future-execution-status attack failed — C2 no longer claims to report row D's
completion. **Keep all of it.**

## The finding

Refusing reason (c) was honest, but the downstream contract was never written. An object whose
instrument output is **absent or non-finite** stays `ACCEPTED` in BS-2f, because row E excludes only
on C2's cutout predicates. It then enters row F's calibration bins and the hand-check allocation.
Row I must read "the corresponding instrument outputs" to form BS-8f and has no rule for an
allocated object whose output is missing. And row J runs Stage C on the whole BS-2f mask.

GPT56's consequence, which is the reason this is blocking rather than untidy:

> A mask containing rows that cannot enter the scientific statistic inflates the sample and can PASS
> a power test for a population that will never be analysed.

**That is the shape of the failure that got the predecessor declined** — a power gate recorded as
passed against a population other than the one analysed. It has arrived by a different route.

Row P does not catch it. It reads the χ vector *joined* to the accepted mask: an absent measurement
cannot enter that join, and has no confidence value to compare. A non-finite measurement is not
mapped to the confidence exclusion. And the mandatory recomputation fires only "if this exclusion" —
the confidence cut — removes an object. Part 2 names a destination for non-finite outputs and gives
no handling rule.

## Take route (b). Route (a) is not yours to take.

Both referees offer two routes. **Route (a)** rebuilds the sealed pre-lock execution supervisor R6b
declined — that would reverse a refusal the principal authorised, so it is out of scope for this
pass. **Route (b)** keeps the refusal and writes the missing contract:

1. Define a **pinned post-unblinding exact-parent join** against the independently fixed attempt
   set. **Forbid silent inner-join loss** — an object present in the mask and absent from the join
   must be a named state, never a row that quietly disappears.
2. Give absent and non-finite measurements **explicit deterministic terminal states**, with stated
   precedence relative to the confidence exclusion. Forbid discretionary retry.
3. Require **any** such removal — not only a confidence removal — to rebuild the final mask digest
   and re-evaluate calibration applicability and Stage-C power, and to refuse the verdict if a
   locked adequacy condition no longer holds.
4. Solve the **pre-unblinding BS-8f problem**. Row I may face an allocated object with no usable
   output. Either define the allocation and calibration protocol over a provably usable sealed
   subset without exporting per-object outcomes, or **fail the run before BS-8f**. Say which.
5. State the rule that **BS-5f may not certify a mask containing rows the verdict cannot use.**

If part of this cannot be done without a pre-lock execution fact — and it may not be — **say so
explicitly and name what it costs**, rather than writing a rule that cannot be evaluated. A stated
impossibility is a result. The principal has already accepted one such cost this round.

## Disposition change CODEX asks for

Part 5 currently records finding 3 ("never invokes the classifier") as REPAIR. CODEX asks that it be
**unresolved**, not repaired, until a BS-2a candidate defines the schemas, verifier identities,
attestation chain, mediator transition and fixture oracles. Make that change. A future-work list is
not a repair receipt. Do the same for finding 1.

## Deliverable

Write `SECTION6_DRAFT_AGY_R7.md` here — complete and self-contained, all five parts, not a diff.
Carry §6.2 and §6.3 forward as **real text reconstituted from R5**, not as parenthetical
placeholders; that assembly gap was disclosed to the referees once and should not survive again.

Do not modify the preregistration. Do not read `/Users/duhokim/NebulaMindData/`. Nothing is
authorised to fetch. No deadline.

**Renaming a finding counts as refusing it, and so does emptying a clause.** REFUSE remains a
legitimate verdict when argued.
