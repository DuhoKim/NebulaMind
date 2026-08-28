# OPEN QUESTION — the VOID registry is not complete. Amending it needs a human.

**Raised 2026-08-29 01:20 KST by Hwao under self-continuation. Two hard stops apply at once:
the seats disagreed on substance, and the remedy changes normative content.**

## What is settled — both seats agree

**The circularity claim in the BS-2v row is false.** Both seats independently rejected it:

- GPT56: *"The claimed circularity does not survive attack: §7.1 can be frozen before the converter,
  and hashing only the canonical §7.1 rows while storing that digest in the BS-2v row creates no
  fixed point."*
- CODEX: *"§7.1's normative row content is supplied by the preregistration, not by the future
  converter, and its current canonical rows may be pinned before converter implementation."*

**And pinning is necessary, not sufficient.** CODEX: the converter, receipt schema, verifier/gate
behaviour and fixtures still have to be delivered and gated. **Nothing here unblocks BS-6.**

So the *mechanism* is cleared. The blocker moves to registry content.

## Where they disagree — and it is exactly the check I flagged as uncomputable

I told both seats that coverage is only verified against §6.1's row table, and that whether §5/§6.3/
§2.7 **prose** requires an antecedent §7.1 omits needs reading, not parsing.

- **CODEX: "I found no VOID antecedent required by the prose of §5, §6.3, or §2.7 that is absent."**
- **GPT56: found three, and named them.**

## I verified GPT56's three against the document text. All three hold.

| # | prose | registry | gap |
|---|---|---|---|
| 1 | §5 line 493: "permutation/statistic/protocol non-finite/**degenerate** failures" | `VOID-5-NONFINITE` only | **degenerate ≠ non-finite.** A finite-but-degenerate statistic (zero variance, a collapsed permutation set) is voided by the prose and has no ID. |
| 2 | §5 line 493: "protocol/**digest** deviation" | `VOID-5-PROTOCOL-DEVIATION` | The ID names protocol only. Digest deviation is either a second antecedent or an undeclared alias. **Ambiguity in a registry about to be pinned is itself the defect.** |
| 3 | §2.7 line 388: "A threshold **chosen or moved** after inference exists voids the run" | `VOID-2.7-THRESHOLD-MOVED`, phase `Post-first-real-χ` | The ID covers *moved*, not *chosen*. And the prose's trigger is "after inference exists", which is **not obviously the same instant** as `Post-first-real-χ`. |

**A negative claim ("I found no gaps") is weaker evidence than three specific positives, and the
positives check out.** This is not a tie; CODEX missed them. But the remedy is still not mine.

## Why I am stopping rather than fixing it

Adding or renaming a VOID antecedent, or changing a phase, **changes what the preregistration
normatively enumerates as voiding the run.** That is a claim, not a specification-quality
improvement. Under the standing orders that is a human decision, and the seats' disagreement is a
second, independent stop.

**There is also a real cost to getting it wrong in either direction**, which is why it is worth a
human minute rather than my guess:

- **Under-enumerate** → the registry gets pinned incomplete, and clause 10 becomes "executable"
  against a set that silently omits a void condition the prose requires. That is worse than leaving
  it unpinned, because it *looks* closed.
- **Over-enumerate** → an antecedent the prose does not require becomes normative, and every future
  converter and gate must handle a condition the study never meant to void on.

## The options, and what each costs

**A. Amend §7.1 to close all three, then re-gate.** Add `VOID-5-DEGENERATE`; either add
`VOID-5-DIGEST-DEVIATION` or declare the alias explicitly in the row; split or rename
`VOID-2.7-THRESHOLD-MOVED` to cover *chosen*, and reconcile its phase with "after inference exists".
*Cost:* four normative edits, and the phase reconciliation in particular is a judgement about when
the study considers inference to exist.

**B. Amend only the two unambiguous ones (1 and 2), and refer the §2.7 phase question separately.**
*Cost:* less at once, but leaves a known gap open and a second round needed.

**C. Ask CODEX to re-examine specifically the three GPT56 named.** *Cost:* one round, and it settles
whether CODEX disagrees or merely missed them — but I have already verified them against the text,
so this mostly buys confirmation.

**D. Pin nothing yet; record that the mechanism is cleared and the content is not.** *Cost:* the
VOID blocker stays shut, but the record is honest and no incomplete set is frozen.

**My recommendation, not my decision: A.** All three gaps are verified in the document's own words,
and the registry's whole value is that it is complete. But the §2.7 phase reconciliation is the part
I would not want to write unsupervised — "after inference exists" versus `Post-first-real-χ` is a
question about when the study's own clock starts.

## State

- `tools/void_registry.py` — mechanism sound; both seats verified the digest placement creates no
  fixed point. 52 antecedents, 20 §6.1 rows, all covered, `registry_digest bd55490e…`.
- Reports: `gates/VOID_GATE_GPT56.md` (NOT CLEAR), `gates/VOID_GATE_CODEX.md` (CLEAR).
- **BS-6 and the first image byte remain blocked either way.**
