# TRACK 2 EVENT-RECEIPT PATH — the delegated witness workflow (recommended default) and the ONE step that is Duho's — 2026-09-06 21:18 KST

Written after Blanc's 21:14 order and its 21:16 correction. Two things the earlier design text assumed were never granted: it said the receipt origin was "named by Duho" (it was the lane's label) and it presumed Duho confirms every receipt digest (a recurring chore he has asked not to be given). Both are removed from the design text, the module docstring and the candidate rule text. What replaces them:

## The origin label — proposed by the lane, unadopted
The receipt's `origin` field is `{"actor": "ops-witness", "session": "OPS"}`. This label is the LANE'S PROPOSAL for the OPS session's receipts; it is not a user decision and no user decision about it has occurred. It is routine metadata; it becomes operative only if the composed mode is adopted.

## The delegated evidence and witness workflow (recommended default — no routine human step)
1. WHO takes the receipt: the OPS session (Blanc), a different agent/process from the lane, using the same authenticated `gh` CLI, INSIDE GitHub's events window (days after the approval, at the latest at the corpus-identity freeze).
2. WHAT binds it: `write_events_receipt` writes the events page(s) verbatim, their provenance (endpoints, retrieval UTC, gh version), the origin label and the events digest; the OPS session commits it ONCE and pushes it to the protected branch; the OPS session ALSO keeps its own copy outside the lane (its own directory) and states the receipt's digest in its own pane record — a second copy the lane cannot rewrite.
3. WHAT the driver checks (composed mode, EXPIRED path): receipt added by exactly one commit and never touched; that commit an ancestor of the LIVE remote head (ls-remote); digest recomputed; origin equals the expected label; the retained event in it verbatim.
4. WHAT an independent party can check afterwards WITHOUT Duho: everything in 3, from the repository alone; plus that the OPS session's retained copy has the same digest (from OPS's directory and pane record); plus, while GitHub still serves the window, that the receipt's events are a subset of the live feed.
5. WHAT REMAINS TRUSTED, exactly (this is the step Blanc's order is about): with ONE GitHub account, a receipt FORGED by the lane as the FIRST receipt, carrying the OPS label, is NOT caught by the driver — GitHub cannot tell the lane's push from OPS's. It IS caught by step 4 (the OPS copy would be absent or differ), which is a check by a person or agent outside the lane, not by the code. So the residual trusted step is: "the OPS session's retained copy and pane record exist and were made by the OPS session". Delegation moves the work to OPS; it does not make the code verify OPS's identity.

## What would close that step by code — and why it is the ONE decision that is Duho's
An expected-receipt identity the driver can check is one of: (i) a SECOND GITHUB IDENTITY for the receipt-taker (e.g. the existing custodian account `nmcustody`, or a fine-grained token bound to it) — the driver reads the receipt commit's PushEvent from the live feed and requires `actor.login` = the pinned witness login ≠ the lane's login; or (ii) a SIGNATURE over the receipt with a key the lane cannot read (the custodian-key upgrade codex named at V7). Creating or assigning that identity/key is not delegable to the agents: only Duho holds the accounts. That is the ONE human decision on this path.

## The questions (only what genuinely needs him)
- **Q1 — Should an expired-receipt path exist at all?** Option C (recommended by the lane): NO — the driver refuses any identity whose approval event has left GitHub's feed, and tune/holdout must complete inside the window (~90 days / 300 events); no receipt, no witness identity, no residual trusted step. Option A: YES, with the delegated OPS workflow above and the residual step stated. Option B: YES, closed by code with a second GitHub identity (i) or a custodian key (ii) that Duho provides once.
- **Q2 — nothing.** No per-receipt confirmation is requested. If Q1 = B, Duho provides the identity/key ONCE; everything after is delegated and checkable without him.

Nothing is adopted; the package goes to review with these stated as they are.
