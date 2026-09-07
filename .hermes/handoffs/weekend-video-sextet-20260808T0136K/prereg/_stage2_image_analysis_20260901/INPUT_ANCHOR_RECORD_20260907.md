# INPUT ANCHOR RECORD — written after the anchor events, quoting their timestamps (2026-09-07 20:02:59 KST)
Binds three identities WITHOUT mutating any of them. `INPUT_FREEZE_C_20260907.json` keeps its `commit_id` and `external_timestamp` fields UNFILLED by design: filling them would change C's digest and break the binding this record exists to make.
| bound identity | value |
|---|---|
| commit containing C | `f7486ed56b00d8243a959ee3eff367853910cd9f` |
| input freeze C | `bbc08cd696150f9a077b32a644f0f39b18dc777e8627576c55b6dada8d3269f8` |
| adopted A1 | `6b9ecc79210046fa4c6611953184ece75818214bf4e962e4ac2e308243616e9f` |

## TWO ANCHOR EVENTS, WITH THEIR PROVENANCE STATED HONESTLY
1. **Public-remote push — A1 §86 route one. `2026-09-07T10:57:47Z`.** GitHub's PushEvent `created_at` for head `f7486ed5…` on `refs/heads/feat/paper-workflow-v2`, read from the Events API. **This timestamp is written by GitHub, off this machine, and cannot be edited by the lane owner or by any agent here.** It is the anchor that carries the independence property.
2. **Codex statement — A1 §86 route two. `2026-09-07T10:59:20.236Z`**, response_item 3109, message `msg_0f31e804df0f7f53016a9e9904b92087d08dbfec8f2a35285a`, task `01a07a87-…`, quoting the same three identities.
**THE PROVENANCE JUDGEMENT, which is the point of this record.** Codex disclosed candidly that its timestamp is the top-level conversation `response_item` value and that **no separate provider `create_time` is exposed** — "do not describe it as a separately verified backend timestamp". I accept that at face value and act on it: **that timestamp lives in a local session file on this machine and is therefore not, by itself, sufficient as the anchor.** Accepting it alone would reopen the exact FATAL that created this requirement — an unwitnessed local timestamp can be backdated, and the party who benefits is the party who could edit it. It is retained as corroboration, not as the anchor.
**Anchor of record: the GitHub push at `10:57:47Z`.** No fabricated backend time is claimed anywhere in this package.

## THE DESIGNATION THAT FOLLOWS
Base = **the later of the two events**, `2026-09-07T10:59:20.236Z` — deliberately conservative: the strong anchor is earlier, so measuring the wait from the later moment makes the round strictly more prospective than either event requires.
Earliest permitted round time = base + 600 s = `2026-09-07T11:09:20.236Z`.
**DESIGNATED ROUND 6444945, scheduled `2026-09-07T11:09:30Z`** (drand mainnet genesis 1595431050, period 30 s). At designation the round **did not yet exist** — 417 seconds in the future, verified against the live clock. It is **not** the excluded exhibit round 6440756.
Nothing protected was opened; no seed value existed at designation; the round's randomness is unknowable to everyone until it is produced.
