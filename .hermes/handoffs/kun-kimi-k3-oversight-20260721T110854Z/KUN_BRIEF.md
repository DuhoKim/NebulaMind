# KUN BRIEF — Kimi K3 general NebulaMind oversight

Task ID: `kun-kimi-k3-oversight-20260721T110854Z`
Coordinator: Hwao/Fable
Executor/reviewer: Kun on Hermes via Nous Portal route `moonshotai/kimi-k3`
Relay/receipt verifier: Tori/Hermes
User direction: launch Kun on Hermes Kimi K3, oversee NebulaMind generally, and submit a report; replace the two left-side WonE/Garu panes while preserving any other Kun lane.

## Objective

Perform an independent, evidence-based, read-only oversight pass over the current NebulaMind project. Submit one concise but substantive report that tells Hwao and the user what the project currently is, what is healthy, what is at risk, and what should happen next.

## Allowed read scope

- `/Users/duhokim/NebulaMind/NebulaMind`
- `/Users/duhokim/NebulaMind/NebulaMind-origin-main-live` for read-only comparison of the currently served/product frontend
- Repo-local `.hermes/board/`, `.hermes/handoffs/`, plans, tests, manifests, and project context
- Read-only git inspection and non-mutating verification commands

Start by reading `/Users/duhokim/NebulaMind/NebulaMind/.hermes.md` and obey its Hwao-led roles and safety gates.

## Sole write target

Write only:

`/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/kun-kimi-k3-oversight-20260721T110854Z/KUN_NEBULAMIND_OVERSIGHT_REPORT.md`

Do not edit any other file.

## Hard exclusions

- No DB/API writes, migrations, SQL apply, or production mutation
- No deploy, restart, process kill, publication, browser action, cloud action, cron, billing, or secrets access
- No git add/commit/push/merge/reset/checkout/branch creation
- No code, configuration, cockpit, frontend, backend, science-data, or prose edits
- Do not inspect `.env`, credentials, keychains, tokens, or unrelated out-of-scope paths
- Do not launch subagents or ask another pane to do work
- Do not claim something is live or passing without direct evidence

## Required inspection

1. Establish current branch, recent commits, dirty-state counts, and major top-level subsystems without trying to clean the worktree.
2. Map the product/research architecture at a useful level: core axiom → claim/status ledger → research/debate map → prose/wiki → derived evidence/trust; note how backend, frontend, tools, tests, and handoffs support it.
3. Inspect representative current files and active handoffs rather than summarizing filenames alone.
4. Assess:
   - product and research coherence;
   - evidence/provenance and trust boundaries;
   - implementation/test/build health from available receipts or safe focused checks;
   - dirty-worktree and parallel-work risks;
   - public/live versus source-of-truth divergence risks;
   - current safety gates and any apparent gate violations;
   - the highest-value next actions.
5. Distinguish verified facts, reasonable inference, and unknowns.

## Report contract

The report must contain:

1. Executive verdict: `HEALTHY`, `HEALTHY_WITH_RISKS`, `AT_RISK`, or `BLOCKED`
2. What NebulaMind currently is
3. What is working well
4. Top risks/blockers, ordered by severity
5. Architecture and source-of-truth map
6. Evidence/trust assessment
7. Engineering/reproducibility assessment
8. Operational/safety-gate assessment
9. Prioritized next actions: exact owner/lane, action, expected evidence, and gate
10. Evidence ledger: paths and commands actually inspected
11. Uncertainties and what Kun deliberately did not inspect
12. Model/route note: requested `Nous Portal / moonshotai/kimi-k3`; do not make billing-bucket claims beyond that route

Put this standalone marker near the top and again as the final line:

`KUN_KIMI_K3_NEBULAMIND_OVERSIGHT_COMPLETE_20260721T110854Z`

After writing, read the report back, verify the marker appears twice, report its byte count, and finish in the pane with the standalone line:

`KUN_KIMI_K3_OVERSIGHT_SUBMITTED_20260721T110854Z`

If blocked, write the same report path with exact blocker evidence and finish with:

`KUN_KIMI_K3_OVERSIGHT_BLOCKED_20260721T110854Z`
