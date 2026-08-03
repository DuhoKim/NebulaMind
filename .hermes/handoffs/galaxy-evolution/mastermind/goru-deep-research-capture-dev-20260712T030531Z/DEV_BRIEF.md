# DEV BRIEF — Goru Deep Research capture tool (LOCAL-ONLY development, HELD pre-canary)
Lane: `goru-deep-research-capture-dev-20260712T030531Z` · Author: Hwao (coordinator only)
Commissioned: Duho direction 2026-07-12 ("Tori to help Goru develop a way to use Deep Research")

## 0. State & standing locks (binding, unchanged)
- **Goru LOCAL-ONLY:** no Chrome/browser, System Events/AppleScript, cookies/`__Secure-1PSID`,
  profiles, login, CAPTCHA/verification, Gemini Web, or network to Google — in any code Goru runs.
- **Joint canary REMAIN_NOT_ARMED; Google verification hard stop standing.** No live
  click/submit/Start-research/account action is authorized by this brief.
- **Incident quarantine:** `tools/gemini_deep_research_driver.py` and `tools/R15_prompt.txt`
  (untracked, from the denied `goru-agy-pilot-resume` attempt) are advisory-only and **must NOT be
  imported, executed, copied, or used as a base** here.
- **Tori holds live execution.** Only a *fresh supervised canary gate* (§6) can ever run the live
  path — not this brief. This brief authorizes LOCAL development, fixtures, tests, and receipt
  design ONLY.

## 1. Objective
Develop — entirely against local fixtures — a Deep Research **capture/extraction** utility (working
name `wait_and_extract`) that, in a FUTURE supervised canary, would: after the **human** starts a
Deep Research run in the human's own browser, detect completion in that **exact** conversation,
extract the answer body, verify the completion marker, and write an immutable capture receipt. Under
this brief it never touches a browser — it is proven correct on saved DOM/HTML fixtures.

## 2. Roles (no solo lanes; ACK before work)
- **Goru:** writes local-only code + fixtures + tests + receipt design under this lane; runs ONLY
  fixture/dry-run tests; never invokes browser/System Events/AppleScript/network. `GORU_ACK` row.
- **Tori:** independent verifier — code-reviews for any reachable browser/network call, re-runs
  tests, re-hashes receipts, countersigns; sole future live executor and hard-stop authority.
  `TORI_ACK` row.
- **Duho:** the only human who would click in a future gated canary; decision authority.
- **Hwao:** coordinator/author; executes nothing.
The Goru pane's current "click Start research" prompt and any live `wait_and_extract.py` run are
**paused**; move that in-progress file under `dev/` and treat it as a draft to be reviewed, not run.

## 3. Scope — what to build (all under this lane; NOT in product or the live `tools/` path)
1. `dev/wait_and_extract.py` — pure functions + a `--dry-run` CLI:
   - **Input:** a saved conversation DOM/HTML fixture + target conversation id + expected marker.
   - **Output:** `verdict.json` = `{state, target_id (echo of requested), marker_count,
     marker_is_final_nonblank_line, extracted_body_path|null, planned_actions[]}` — **declarative
     only; performs no action.**
   - Any live browser/wait/poll glue lives behind ONE clearly named boundary function that is
     **never called by a tested path** and refuses unless a future canary explicitly enables it;
     Tori reviews that boundary line-by-line.
2. `dev/fixtures/` — seed from the prior pilot taxonomy (idle, dr-active, plan-ready, running,
   ack-no-control, complete-ok, marker-missing, marker-dup, verification-wall, billing, login,
   stale) + `targets.json` + a hand-authored `EXPECTED_VERDICTS.json`. **Fix the known oracle bug:**
   the dup-marker fixture's `marker_is_final_nonblank_line` MUST match the fixture (that
   contradiction caused the prior spurious T4 FAIL). Re-pin fixtures + oracle by sha256.
3. `dev/tests/` — TDD, fixture-driven, **zero network**, deterministic: state classification,
   exact-target custody, fail-closed walls, capture integrity, bounds.
4. Capture-receipt design — `CAPTURE_RECEIPT` schema: `wc -c` + sha256 of every captured file;
   immutable-after-write; `body.md` marker check; no receipt on un-hashed text.
5. `WAVE_LEDGER.md` (this lane) — append-only; ACKs, test rows, receipt hashes.

## 4. Acceptance criteria (ALL must hold; Tori-countersigned)
- **A1 — no live surface in tested paths:** zero reachable browser/System Events/AppleScript/Chrome/
  cookie/profile/network call in any path the tests exercise (Tori code-review + grep attestation +
  a no-network test run).
- **A2 — classification correct:** dry-run CLI matches a CORRECTED `EXPECTED_VERDICTS` on all
  fixtures; the dup-marker final-line contradiction is fixed and re-pinned by sha256.
- **A3 — exact-target custody:** `target_id` echoes the requested conversation id for every fixture;
  never a default/first tab.
- **A4 — fail-closed:** verification/CAPTCHA/billing/login fixtures ⇒ `planned_actions == ["HARD_STOP"]`
  and nothing else; `UNKNOWN` state ⇒ `HARD_STOP`.
- **A5 — capture integrity:** marker present **exactly once AND as the final non-blank line** ⇒
  CAPTURED, else VOID; same fixture rerun ⇒ identical body sha256 (determinism); different fixtures
  ⇒ pairwise-distinct sha256 (anti-identical-hash regression from the 93-file macro).
- **A6 — receipt:** valid `CAPTURE_RECEIPT` with byte counts + sha256; captured files immutable.
- **A7 — TDD gate:** test module green (report N/N), `py_compile` (and any inline JS syntax) pass;
  results + receipts hashed into the lane ledger.
- **A8 — no secrets / quarantine respected:** no tokens/cookies/`__Secure-1PSID`/credentials
  anywhere; live glue quarantined behind an un-invoked boundary; the incident driver/prompt not
  imported.
- **A9 — deliverable is LAUNCH-READY but NOT-ARMED:** a written `HOLD` marker in this lane and an
  explicit statement that live use requires the §6 gate — which this brief does NOT grant.

## 5. Hard bounds / non-goals
No browser execution; no click/submit/Start-research; no account/login/CAPTCHA/network-to-Google; no
product/DB/deploy/git/cron writes; no promotion into the live `tools/` path; no import/execution of
the quarantined driver/prompt. All writes stay under this lane (temp `_tmp_*`). If any step appears
to need a live action, **STOP and report — do not widen scope** (this is the exact line the prior
incident crossed).

## 6. Gate to live (reference only — NOT authorized by this brief)
A future, separate Hwao packet under a fresh supervised canary: Duho manually clears the Google
verification; a trusted fresh evidence set is captured; the **human** (Duho) performs the single
Start-research click; Goru's tested capture code then runs **read-only** against that exact
conversation; C1-scope only; fail-closed markers. Until all of that exists: **HELD**.

## 7. What Hwao did / did not do
Did: authored this brief + lane scaffolding (`dev/`, `dev/fixtures/`, `dev/tests/`, `tori/`) and a
HOLD marker. Did NOT: write any tool code, run anything, touch a browser/Google surface, import the
quarantined artifacts, or write to product/DB/deploy/git/cron. Development starts when Goru+Tori ACK.
