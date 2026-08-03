# G3 Surveys RF-2 preflight STOP — mirror pin drift — re-pin adjudication — Hwao decision receipt

Run: `quartet-kun-application-20260721T114246Z` · Phase 3 follow-on, G3 Surveys unit, RF-2 preflight
Authority chain: `SURVEYS_G3_REREVIEW_FAIL_RF2_RESCOPE_GATE_RECEIPT.md` (RF-2 definition) → user line `UNFREEZE G3 SURVEYS RF-2 PLOTA 20260722` → `HWAO_G3_SURVEYS_RF2_ACTIVATED_20260722` → executor §5.2 preflight STOP → this receipt
Author: Hwao/Fable — packet issuer and final ratifier per `.hermes.md`
Issued: 2026-07-22T13:26 KST (2026-07-22T04:26 UTC)
Record type: **STOP adjudication + pin update. This document executes nothing.** One file written (this receipt); no source/test edit, no git/index/worktree mutation, no runtime/cockpit/DB/network action, no `.env*` content access, no evidence overwrite.

---

## Decision

1. **The STOP was correct.** The mirror-pin sentinel fired on a true pin mismatch before the census or any edit. The executor's conduct — freeze first, read-only provenance, no self-granted continuation — is exactly right.
2. **The drift is adjudicated EXTERNAL, DELIBERATE, CLEAN, and BENIGN, with the mechanism now fully explained** (§2). It is the same Lab-PDF content already adjudicated benign at MC-1, now merged upstream as PR #102 and pulled by the external mirror operator.
3. **Dual re-pin ACCEPTED:** live mirror = `main @ ed20708788146a043721353a8cd8f49d1237b088`, clean; shared cached `origin/main` = `ed207087` (superseding the parent packet's `28e87357` sentinel value by external action). Feature-branch divergence context re-pins to **6 ahead / 67 behind** (dirty state 20/360/0 unchanged). **The RF-2 worktree base remains the immutable `28e873570f1c479fffd18a5106e5afa91d46e3e9` — deliberately pinned; nobody "corrects" the base to ed207087.** Base advance stays a separate future approval; the V2 re-review judges against `28e87357`.
4. **RF-2 resumption is AUTHORIZED at §5.2 step 4 (defect-class census) without a new user line** (grounds §3). One-shot, under the updated pins and all other unchanged preconditions (§4).
5. **No blanket waiver:** any FURTHER movement of the mirror or the shared `origin/main` ref against these pins → STOP again; each re-pin is individually adjudicated.

## 1. Preflight result reconciled (executor relay + Hwao re-verification, 13:23–13:25 KST, read-only)

PASS on every closed-world pin, re-verified live by Hwao:

| Pin | Observed | Match |
|---|---|---|
| Worktree base | detached `28e87357` | ✅ |
| Modified set | exactly the five `␣M` paths; cached diff empty | ✅ |
| Live diff | 39,513 bytes; SHA-256 `b39215c3…7bd75a` | ✅ |
| PlotA baseline | clean; index blob `efe9d5d4bb43407e8429a40acf41987e640d5e0d` | ✅ |
| Primary | `826e733`; 20 modified / 360 untracked / 0 deleted; 4/4 dirty-intent reverse-apply OK | ✅ |
| V1 evidence | `SURVEYS_G3_REVIEW_FIX_FINAL.patch` = 39,513 B / `b392…` exact | ✅ |
| V2 | absent | ✅ |

STOP item only: mirror at `ed207087` on `main` (clean), not the pinned `1a8da92e` on the chore branch. Verified: mirror HEAD `ed207087`, branch `main`, dirty lines 0, last commit `2026-07-22T13:20:57+09:00 chore(lab): refresh flagship study PDF with integrated error-budget table (#102)`.

## 2. Mechanism — fully explained, one external action

- **Topology (new, decisive):** the live mirror is a **linked worktree of the primary repository** — `git -C <mirror> rev-parse --git-common-dir` → `/Users/duhokim/NebulaMind/NebulaMind/.git`, and the primary's `git worktree list` shows `NebulaMind-origin-main-live ed20708 [main]`. Mirror and primary share one object database and one set of remote-tracking refs.
- **Reflog provenance (verbatim heads):** `checkout: moving from chore/lab-refresh-paper-pdfs-20260722 to main` (at `28e8735`) → `pull --ff-only origin main: Fast-forward` (to `ed20708`) → `checkout: moving from main to main`.
- **Therefore one operator action in the mirror worktree explains BOTH observed movements:** the pull's fetch phase updated the shared `origin/main` ref (why the primary's cached `origin/main` now reads `ed207087` although no lane ever fetches), and its ff-only merge advanced the mirror's checked-out `main`. Our lanes' no-network discipline is intact — the fetch ran in the externally-operated mirror worktree context, not in any lane.
- **Advance size:** `28e87357..ed207087` = **exactly 1 commit** — the squash-merged PR #102, byte-for-subject the same Lab-PDF chore adjudicated benign in `SURVEYS_G3_RF1_MIRROR_DRIFT_STOP_DECISION_RECEIPT.md`. Zero overlap with the six authorized Surveys paths (Lab PDF asset).
- **Untouched by the pull, verified:** the detached RF-2 worktree (commit objects are immutable; HEAD, dirty files, hash all exact), the primary's checked-out feature branch and dirty tree, and all phase3 evidence.
- Timeline: the pull landed at 13:20:57 KST, between RF-2 activation and the executor's preflight — precisely the window the sentinel exists to catch.

## 3. Why resumption needs no new user line

- The user's RF-2 activation line is fresh and none of the approved RF-2 work (census, R8, R6, R7, R9) has begun; nothing the user approved has changed shape.
- The drift is orthogonal to RF-2's closed world: base commit immutable, worktree contents verified byte-identical, acceptance criteria and re-review target unchanged (patch vs `28e87357`).
- The content class was already adjudicated benign once (MC-1); this is its upstream merge — a second sighting of the same known-benign object, now with complete mechanical provenance.
- The MC-1 precedent governs: adjudicate the sentinel, verify the closed world, re-pin, resume the user-approved remainder. Demanding a fresh user line for a benign environmental re-pin is approval fatigue without a safety gain; what the user actually gated (source edits in PlotA + smoke) proceeds exactly as they approved it.

## 4. Preconditions at census start (binding on the executor)

1. Mirror exactly `main @ ed207087`, clean; shared cached `origin/main` exactly `ed207087`. Further movement of either → STOP.
2. All §5.2 closed-world pins re-verified and unchanged: five `␣M`, cached empty, `b392…`/39,513, PlotA blob `efe9d5d4…`, primary `826e733` + 20/360/0 + 4/4 reverse-apply, V1 exact, V2 absent.
3. Census proceeds read-only per §5.2.4 (PlotA, SurveyCard, SurveyPeek, BandSpectrumStrip, FilterSheet — flattening roles over interactive descendants; conditionally-unmounted `aria-controls` targets). Any hit beyond PlotA → STOP before any edit. Census results go in the RF-2 execution receipt.
4. Then §5.3 order unchanged: R8 excision → R6 RED→fix→GREEN → R7 RED→fix→GREEN → R9 pin with fixture self-test; §5.4 completion battery; V2 patch + receipt; third independent review.
5. The RF-2 execution receipt must record the re-pinned divergence context (6 ahead / 67 behind vs `ed207087`; dirty 20/360/0) and cite this receipt as the pin source. Historical `6/66` and `origin/main=28e87357` sentinel values are superseded, not "drifted" — do not re-fire on them.

## 5. Gate ledger after this receipt

G1 Completed · G2 Completed · **G3 Surveys unit: RF-2 active (user line + `HWAO_G3_SURVEYS_RF2_ACTIVATED_20260722`), preflight STOP adjudicated, mirror/origin-main re-pinned to `ed207087`, resumption authorized at the defect census** · G3 all other units Held · G4a/G4b/G4c Held separately · G5 Closed · G6 Held · G7 Closed — no cockpit/status write accompanies this receipt.

## 6. Safety ledger for this adjudication pass

Source/test edits 0 · git/index/worktree writes 0 · fetch/pull/network by lanes 0 (the pull was external; §2) · stage/commit/PR/push/merge 0 · stash/reset 0 · file moves/deletes 0 · evidence overwrites 0 · DB/SQL 0 · runtime/deploy/cockpit/publication 0 · `.env*` content access 0 · **files written 1 (this receipt)**.

Methods: read-only git in mirror/primary/worktree (`rev-parse` incl. `--git-common-dir`, `worktree list`, `status --porcelain=v1`, `log -1`, `reflog`, `rev-list --count`, `diff --cached --name-only`, `diff HEAD` piped to `wc -c`/`shasum` only, `rev-parse :path`, `apply --reverse --check` ×4); `shasum -a 256` on the V1 patch; `ls` metadata; `date`. No state changed anywhere.

---

`HWAO_G3_SURVEYS_RF2_MIRROR_REPIN_AUTHORIZED_20260722`
