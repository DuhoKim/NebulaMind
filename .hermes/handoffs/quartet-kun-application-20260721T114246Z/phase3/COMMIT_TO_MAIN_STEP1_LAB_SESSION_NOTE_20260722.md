# Commit-to-main (step 1) — executed via reviewable PR by the Lab session

Run: quartet-kun-application-20260721T114246Z · post-unit delivery
By: Claude Code (Lab session) on Duho's explicit authorization ("Put the reworked Surveys + runner onto the main code").
Date: 2026-07-22 ~21:15 KST.

## What was done
The two reviewed/reworked salvage units (Surveys Atlas IA V2 + backend research-runner) were
applied from their preserved phase3 patches onto a fresh branch off CURRENT origin/main (4bbb116)
in the live-deploy checkout, and opened as DRAFT PR #105 for Duho's explicit merge.

- SURVEYS_G3_REVIEW_FIX_FINAL_V2.patch (53,521 B) → applied clean (no drift), frontend builds clean.
- BACKEND_RUNNER_REVIVE_UNIT.patch (41,135 B) → applied clean (router/worker/test new, main.py +2).
- Branch: feat/land-kun-reworked-units-20260722 ; 2 commits (surveys, runner). Draft PR #105.
- Merge to main = the irreversible product change; left as draft for Duho's explicit click.

## Effect on the reconciliation
Once PR #105 merges, the salvage VALUE of feat/surveys-atlas-ia-p1-20260627 is delivered to main
→ branch retirement (step 2) becomes eligible, and the runner backend serves /api/lab/runs from main
(retiring the branch-dependency Kun flagged). This note keeps the crew ledger honest — the commit-to-main
was executed by the Lab session, not the coordinator lane, to avoid a duplicate packet.

## Still held
- Branch retirement (step 2): after #105 merges.
- G4 cleanup (step 3): quarantine MOVE only per R4/R5; deletion stays a later step after review + dwell.
