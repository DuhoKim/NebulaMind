# G3 Surveys RF-3 — USER APPROVAL RELAY (not a crew receipt)

Run: `quartet-kun-application-20260721T114246Z` · Phase 3 follow-on · G3 Surveys unit · RF-3 activation
Relayed by: Claude Code (Lab session) on Duho's explicit instruction. This file records a user approval line
for Hwao/Tori to pick up; it is NOT a Hwao ratification and executes nothing (no source/test edit, no git/
index/worktree mutation, no runtime/DB/network/.env access). One file written (this relay).

## User approval line (verbatim, relayed)
`UNFREEZE G3 SURVEYS RF-3` — given by Duho 2026-07-22 (~13:40 KST), in response to the RF-3 rescope gate
`SURVEYS_G3_RF2_CENSUS_STOP_RF3_RESCOPE_RECEIPT.md`.

## Scope (exactly as the RF-3 gate defined it; nothing added)
- Authorizes ONLY RF-3 as defined in the census-STOP receipt §3. Not blanket G3; G3 re-latches to Held when the unit completes or stops.
- ControlBar.tsx becomes the 7th authorized path. Writable files exactly THREE: `PlotA.tsx`, the surveys smoke test, `ControlBar.tsx`. `FilterSheet.tsx` stays READ-ONLY.
- E5 fix = the LOCKED relationship (§2.3): conditional `aria-controls` on the ControlBar trigger — present ("surveys-filter-sheet") only when `filterSheetOpen` is true, `undefined` otherwise; `aria-haspopup="dialog"` and `aria-expanded` always present; FilterSheet keeps `if (!open) return null`. Mounted-hidden FilterSheet is REJECTED.
- All RF-2 work items (PlotA R6/R7 etc.) carry over unchanged.
- All stop-rules / preconditions intact: work only in the disposable worktree at the pinned base; NO commit/PR/push/merge; stop on any pin/hash/census drift.

## Pins re-verified at relay time (Claude Code, read-only, 13:40 KST)
- Primary: branch `feat/surveys-atlas-ia-p1-20260627` @ HEAD `826e733`; 20 modified / 360 untracked / 0 deleted. ✅ matches RF-3 requirement.
- Worktree `g3-surveys-rework-20260722` base @ `28e8735` (cached origin/main). ✅
- Baseline blob pins from the gate receipt still apply (PlotA `efe9d5d4…`, ControlBar `a72e9186…`, FilterSheet `e61f9e76…`) — Hwao to re-verify at activation.

## Next step (crew)
Hwao: ratify → issue `HWAO_G3_SURVEYS_RF3_ACTIVATED_20260722` (or halt on any drift). Tori: execute the three-file
fix in the worktree, re-review against the §2.3 locked E5 relationship. Nothing here bypasses Hwao's ratification.
