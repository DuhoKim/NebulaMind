# DRAFTING BRIEF — R8. Make route (b) decidable, and stop claiming a rule the document contradicts.

Subject to revise: `SECTION6_DRAFT_AGY_R7.md`, sha256
`ecccedde495a88377497057a4334c676f651f559fc0a7b2635a78dca8a990f30`.
Read `SECTION6_REVIEW_R7_GPT56.md` and `SECTION6_REVIEW_R7_CODEX.md` first.

**The round is converging.** Blocking findings: R5 four and three, R6b two and three, R7 two and
one. CODEX credits R7's repairs as substantive — the exact-parent join, the ban on silent
inner-join loss, precedence before confidence, the ban on discretionary retry, and widening the
trigger to every removal. **Those stay.** So do the clause bodies, the twenty rows, the three
protected properties, and the reconstituted §6.2/§6.3.

CODEX states the scope explicitly: *"Without inventing the separate BS-2a schemas, make the
route-(b) prose decidable."* That is this brief. **Do not attempt BS-2a.** Findings 1, 2, 2b and 3
stay UNRESOLVED.

## Defect A — the terminal states are described, not defined

"A named deterministic terminal state" names nothing. R8 must:

1. **Name the closed set of post-unblinding states** and define precedence between them, derived
   from an **exact set-equality join against one pinned attempt-set identity**. Name the fixed join
   keys and the attempt-set digest that governs.
2. Give **one fixed consequence each** to: zero records, duplicate records, extra records, malformed
   records, absent measurement, non-finite measurement, low confidence, and accepted-finite. State
   whether more than one measurement for a parent is an unconditional refusal. **No retry.**
3. **Enumerate the locked calibration and power predicates** and state exactly which failure emits
   `INCONCLUSIVE-BY-CALIBRATION` and which emits `INCONCLUSIVE-BY-POWER`. "Calibration
   applicability", "the pinned protocol" and "any locked adequacy condition" currently have no
   pass/fail relation anywhere in R7 or V15, so a gate must supply policy after unblinding — which
   is the thing this document exists to prevent.
4. Decide the **hand-check case**: if a removal takes out an allocated committee member, does that
   force `INCONCLUSIVE-BY-CALIBRATION`, permit a frozen recalculation, or merely rerun power?
5. Name the **artifact that authenticates the exact-parent accounting**.

## Defect B — the BS-5f claim is temporally false

R7's row J says *"BS-5f may not certify a mask containing rows the verdict cannot use."* **V15 §4
defines Stage C/BS-5f to run before unblinding on the sealed BS-2f mask, and route (b) deliberately
leaves reason-(c) rows in that mask.** So BS-5f can certify it, and in the motivating case does.
Part 5's claim that this cannot happen "without triggering refusal" is also false: if the
recomputation passes, row P proceeds rather than refuses.

Write the temporal truth instead:

- BS-5f certifies **only** the locked pre-attrition BS-2f population and is **insufficient** for a
  changed final mask.
- On any post-unblinding removal, require a **separately named post-unblinding adequacy receipt**
  bound to the final-mask digest **and** the original BS-5f and BS-L digests. **Do not call it
  BS-5f** — issuing a BS-5f after unblinding contradicts its class-E pre-unblinding role.
- Amend §5's verdict guard to verify **both** receipts and the exact final-mask binding, and to
  refuse before forming any statistic if calibration applicability or the re-run Stage C fails.
- Replace the "may not certify" and "without triggering refusal" sentences with this
  supersession-and-revalidation rule.

**On the conditional-versus-unconditional choice:** both referees offer unconditional refusal after
any unusable row as an alternative. Do not take it. At 65,060 objects some unusable outputs are
near-certain, so unconditional refusal would void essentially every run and is not an honest
contract. Build the conditional revalidation properly instead — with the predicates actually
enumerated, which is what makes it honest rather than convenient. If you think that reasoning is
wrong, say so in Part 3 and argue it.

## Defect C — Part 5 understates a refusal both referees credited

GPT56 and CODEX both credited the reason-(c) refusal when the future-execution-status attack failed,
and R7 then marked it UNRESOLVED. Split the disposition, as GPT56 asks:

- the impossible future-execution-status assignment → **RESOLVED BY REFUSAL** (pipeline blocked);
- the replacement BS-2a mechanism and its channel-closure requirements → **UNRESOLVED**.

This is an accuracy repair and **not permission to execute anything**.

## Deliverable

`SECTION6_DRAFT_AGY_R8.md` here — complete, self-contained, five parts, not a diff. Part 2 must
carry the §4 and §5 conforming edits Defect B requires, since a repair in §6 that leaves §4
asserting the old behaviour is the failure this lane has already made in prose.

Do not modify the preregistration. Do not read `/Users/duhokim/NebulaMindData/`. Nothing is
authorised to fetch. No deadline.

**Renaming a finding counts as refusing it; so does emptying a clause; so does naming a state
without defining it.**
