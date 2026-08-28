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

## Adjudicated 02:35 — three gaps, not five

`void_registry.py`'s compound heuristic reports **five** candidates. Two are false positives and a
human should not be handed the larger number. §5 reads
`permutation/statistic/protocol non-finite/degenerate failures`: **the first compound is the
subjects, the second is the conditions.** `VOID-5-NONFINITE` names the condition generically across
all three subjects, so `permutation` and `statistic` are covered. Only `degenerate` is an unnamed
condition.

**The three real gaps are exactly the three GPT56 named** — `degenerate`, `digest`, `chosen` — which
is also a point in GPT56's favour over CODEX's "I found none". The heuristic's docstring and its
output now say it cannot distinguish a subject from a condition.

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

## Audit 03:20 — what `void_registry.py` proves is weaker than its name claimed

Prompted by a carry-over from Tori's lane: both her seats found a check whose NAME asserted more
than its PREDICATE evaluated. Mine had the same defect.

`V05`/`V06` were named "a §6.1 row … has no antecedent in the registry". The predicate matches the
`VOID-6.1<ROW>-` **prefix convention**. It proves a row is *named* by some antecedent; it does not
prove that antecedent semantically covers the row's forbidden column. An antecedent could name row S
and describe something else, and the check would still report row S covered.

**The check is unchanged — only its name was wrong, and the name was the overclaiming part.** It now
reads "no antecedent ID names it", and the tool says "NAME-complete" rather than "complete". This
does not change the three verified gaps below, but it does mean **"20 of 20 rows covered" is a
weaker statement than it looked**, and whoever decides the options below should read it as
name-coverage only.

## State

- `tools/void_registry.py` — mechanism sound; both seats verified the digest placement creates no
  fixed point. 52 antecedents, 20 §6.1 rows, all covered, `registry_digest bd55490e…`.
- Reports: `gates/VOID_GATE_GPT56.md` (NOT CLEAR), `gates/VOID_GATE_CODEX.md` (CLEAR).
- **BS-6 and the first image byte remain blocked either way.**

---

## VERIFIED CURRENT AGAINST V36 — 2026-08-29 07:25 KST

This question was written against V34. The draft has since moved to V36 (CLEAR from both seats).
Re-checked so that a decision taken from this file is a decision about the **current** document.

- `void_registry.py` returns **identical output on V34, V35 and V36**: 52 antecedents, 20 §6.1 rows,
  `registry_digest bd55490ea4290895996bbb12c1e4c81f8a7076c7220a3f2df68971b52c2a50bb`. §7.1 did not
  move between the drafts.
- **§5 line 493 is byte- and position-identical in V34 and V36.** It reads: *"**VOID:** triggered by
  forbidden acts, protocol/digest deviation, or permutation/statistic/protocol non-finite/degenerate
  failures. **This category is not yet executable.**"* Gap 1 (`degenerate`) and gap 2 (`digest`) are
  quoted exactly above.
- **§2.7 line 388 is byte- and position-identical**, still: *"A threshold chosen or moved after
  inference exists voids the run."* Gap 3 (`chosen`) is quoted exactly.

**All three gaps hold on the current draft. Nothing in this file is stale.**
