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

## STATE — refreshed 02:45 KST

| thread | state |
|---|---|
| **BS-2a code gate** | **CLOSED.** Round 6 CLEAR ×2, scoped "CLEAR for FREEZING the quality-predicate component; not a fill authorization". Pinned in V34's §7 row with its recorded limit. |
| **Prereg draft** | V34 (`1c45d32d…`). Both seats cleared the V33 *document*. Untouched since, deliberately. |
| **VOID / clause 10** | **Mechanism CLEARED, content BLOCKED.** Both seats agree the BS-2v circularity claim is false and that pinning is necessary-not-sufficient. They split on completeness; three real gaps verified (`degenerate`, `digest`, `chosen`). **Awaiting a human.** |
| **Gain control** | v5 findings repaired; **v6 dispatched 02:42** (scoped). T-completeness parked. |

## TWO DECISIONS AWAIT A HUMAN — nothing else is blocked on them

1. **`OPEN_QUESTION_VOID_REGISTRY_COMPLETENESS.md`** — amend §7.1 or not. Four options with costs.
   Three verified gaps, not the five my heuristic reports (it cannot tell a subject from a
   condition). Under-enumerating pins a registry that *looks* closed; over-enumerating makes a
   condition normative the study never meant to void on.
2. **`OPEN_QUESTION_T_COMPLETENESS.md`** — the p-gated fork. (a) hold observed `p` fixed, cheap but
   asserts the systematic does not move `p`, which GPT56's counterexample undermines; (b) freeze a
   joint counterfactual path, correct and expensive, and its sign-vector mapping is itself a
   modelling assumption; (c) withdraw the rule and state the systematic as an unbounded limitation.
   **I would drift to (a) because it is cheap, which is the reason not to let me take it.**

**Neither blocks BS-6, which stays blocked regardless.**

## Operating notes that cost time tonight

- `hermes` is NOT on PATH: use `/Users/duhokim/.hermes/hermes-agent/venv/bin/hermes`. A bare `hermes`
  dies with `command not found` and the runner log shows dispatch and done at the **same second**.
- Report filenames carry a `_R<N>` suffix so two rounds cannot overwrite one file.
- A seat can exhaust its iteration budget and write **no** report while leaving a stale earlier file
  in place. Check the mtime and the heading, not just the filename.
- Probe deletions **strictly**: a crash must not count as detection.
