# SELF-CONTINUATION — standing orders, 2026-08-29 00:40 KST → 09:00 KST

**Authorised by Duho, relayed by Blanc.** First lane to run without a relay between rounds. The
problem being fixed: every round tonight ended with a turn and nothing dispatched the next, costing
20–40 minute dead gaps.

Lane root: `.hermes/handoffs/weekend-video-sextet-20260808T0136K/prereg/_successor_build_20260824`

## MAY DO UNSUPERVISED — mechanical continuation only

- Re-dispatch a round whose seats have **both** reported.
- Apply a repair **both seats agree on** where the fix is unambiguous.
- Re-run a battery, recompute a constant, regenerate a trace.
- Commit with a real message.

## MUST STOP AND WAIT FOR A HUMAN

- **A fork where both directions cost something.** (Tonight's example: hemisphere contrast vs
  continuous slope — each lost something real.)
- **Seats disagreeing on substance**, or one seat finding what the other cleared.
- **Anything that changes what the study CLAIMS** rather than how well it is specified — tier
  changes, acceptance rules, `|μ|max`, thresholds.
- **Filling a slot, unblocking BS-6, or anything touching the first image byte.** That gate is Duho.
- **A repair I am not confident in.** If I would have asked, ask.

When stopping for a human: write the question to `OPEN_QUESTION_<topic>.md` in the lane with the
options and what each costs, and say so plainly in the last line.

## PRIORITY: VOID reverse reachability

It is the single item gating clause 10 executability, and therefore BS-6 and the first image byte.
Everything else is specification quality. Progress so far:

- `tools/void_registry.py` — extracts §7.1, canonicalises, digests, checks completeness.
  On V34: **52 antecedents, 20 §6.1 rows, all covered, `registry_digest bd55490e…`**, self-test
  6 controls / 0 failures.
- **The BS-2v row's stated reason for UNRESOLVED does not hold.** It says "the registry cannot be
  pinned before the converter exists". But §7.1's content comes from the document's own normative
  clauses (§5, §6.1's row table, §6.3, §2.7) — the converter *handles* those IDs, it does not author
  them. The real self-reference risk is only digesting §7.1 *into* the document, avoided the same way
  §10 already avoids it: digest the rows, store the digest outside them.
- **Not yet established:** whether pinning the registry is *sufficient* to move BS-2v off UNRESOLVED.
  That is a gate question for the seats, not a claim to make alone.

## BOUNDS

- **Stop at 09:00 KST.** Check `date` on each wake; past 09:00, `CronDelete` the job and write a
  handover.
- **If a round fails twice the same way, stop and write it up** rather than trying a third time.
- **Do not spend seat quota on a question I cannot act on alone.**
- Never modify a subject while a seat is reviewing it — the POST-CHECK exists to catch exactly that,
  and doing it once already cost GPT56's round-4 findings.

## STATE — NOT HERE. Read `LANE_STATE_20260829.md`.

**This file holds the RULES. `LANE_STATE_20260829.md` holds the STATE. Do not duplicate state here
again.**

At 06:21 the table that used to sit in this section had gone stale in the dangerous direction: it
said the draft was V34 and untouched, and that two decisions awaited a human. By then V35 existed
with three fixes applied and **four** decisions were parked. The cron prompt tells the reader to open
*this* file first, so a compacted reader would have taken the stale version as current and could have
re-dispatched a round on a superseded draft, or missed half the open questions.

Two files describing one state is the same defect this lane has been finding all night in other
forms: a second copy that can silently disagree with the thing it describes. One source now.

## PRIORITY, unchanged: VOID reverse reachability

It is the single item gating clause 10 executability and therefore BS-6. `tools/void_registry.py`
extracts, canonicalises, digests and checks §7.1. The mechanism is cleared by both seats — the
BS-2v row's stated circularity is false — and the *content* is blocked on a human: three verified
gaps (`degenerate`, `digest`, `chosen`). See `OPEN_QUESTION_VOID_REGISTRY_COMPLETENESS.md`.

## Operating notes that cost time tonight

- `hermes` is NOT on PATH: use `/Users/duhokim/.hermes/hermes-agent/venv/bin/hermes`. A bare `hermes`
  dies with `command not found` and the runner log shows dispatch and done at the **same second**.
- Report filenames carry a `_R<N>` suffix so two rounds cannot overwrite one file.
- A seat can exhaust its iteration budget and write **no** report while leaving a stale earlier file
  in place. Check the mtime and the heading, not just the filename.
- Probe deletions **strictly**: a crash must not count as detection.
