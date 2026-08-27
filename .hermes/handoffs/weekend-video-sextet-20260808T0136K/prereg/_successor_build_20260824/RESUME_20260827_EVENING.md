# RESUME — DESI successor lane, 2026-08-27 ~19:15 KST

Written as a precaution at 100% context. **Everything below is on disk. Trust the files, not a
memory of them.** Reseed by reading paths, not by recalling decisions.

## What is settled and frozen

- **Closure mechanism: FROZEN at v9.** `gates/FREEZE_CLOSURE_V9_20260826.md` names the six
  read-only artifacts and their digests, the one-seat limitation, and nine carried-open items.
  Referee verdict `gates/CLOSURE_V9_KIMI.md` = CLEAR. Do not re-open without a decision.
- **Closure output:** 65,060 objects → 6,445 selected bricks → **12,117 required bricks**,
  `plan_digest aaeaa9f3…`, derived independently three times.
- **Power: restored, measured not accepted.** 995/1000 exact per-trial nulls,
  `real/STAGEP_EXACT_RECEIPT_20260826.json`, harness `real/stagep_exact.py`. **BS-5p cannot be
  filled** — the exact test is not in the code §0 pins.
- **Ceiling:** ≈148 GB approved as a **planning decision only**, recorded at the foot of
  `acquire/DOWNLOAD_QUEUE_PLAN_20260825.md`. **No image byte has been fetched.**

## What is in flight

- **§6 R5 draft has LANDED**: `gates/SECTION6_DRAFT_AGY_R5.md` (222 lines, sha 63782432d816).
  **Not yet refereed.** Next action: dispatch `gates/BRIEF_SECTION6_REVIEW_R5.md` to GPT56 and
  CODEX. Drafting brief that produced it: `gates/BRIEF_DRAFT_SECTION6_R5.md` — complete enough
  to run cold.
- **BS-2a: refereed, all three NOT CLEAR** (`gates/BS2A_REVIEW_{GPT56,CODEX,KIMI}.md`).
  **BS-6 — the first image byte — is blocked by all three seats.**
- Blanc runs an R5 watcher **outside this session**; the verdict reaches Duho regardless.

## The two findings that matter most today

1. **The inherited acceptance rule excludes galaxies on the quantity being measured.**
   `YUI_PRODUCTION_ESTIMATOR_APPENDIX_20260812.md` line 82 freezes "Accept object x iff
   |χ_net(x)| > τ", and |χ_net| **is** handedness amplitude. Verified by KIMI against the frozen
   record. Mirror-evenness does not fix it — `abs(chi_net)` is itself mirror-even. BS-2a stays
   REFUSED. Open question I raised and no referee has ruled on: a |χ| cut may also change the
   estimand, i.e. be an estimator defect and not only a blinding one.
2. **§6 R5 built the outcome-blindness property instead of naming it** — by changing the writer.
   `verify_cutout_integrity` (row C2) runs pre-inference, reads only cutouts, and produces the
   acceptance projection; confidence is excluded pre-lock and deferred post-unblinding. Cost
   accepted and stated in the draft: a possibly-wasted run if too few objects survive.

## Standing constraints — do not rediscover these

- Drafting runs on **agy** (`agy --dangerously-skip-permissions`) and gpt seats; **gate verdicts
  stay multi-engine and fresh-context**. The drafter never referees its own text.
- `hermes -Q -q` **does not exist** in this build despite RESOURCE_CATALOG.md saying so; use
  `hermes -z`. kimi = `--provider moonshot -m kimi-k3`.
- **Renaming a finding counts as refusing it.** Verdicts are REPAIR or REFUSE, never bare
  "Accepted".
- My watcher's REPAIR/REFUSE counts are **word frequency, not parsed verdicts** — I have misread
  them as verdicts twice. Parse Part 5 before quoting numbers.
- `tools/prereg_lint.py` checks the document against itself; run it after any text edit.
- Three §6 properties confirmed held across four passes and two authors — **do not trade away**:
  the universal access ban, the committee completing G→H→I without voiding the run, the BS-5f
  chain.

## Prereg state

V15 is current (`PREREG_SUCCESSOR_DRAFT_V15_20260827.md`). Fifteen class-P slots, **one filled**
(BS-2m). The text has been refereed four times, always NOT CLEAR. Stage P remains dual-valued and
that is Duho's decision: implement the exact test in the pinned code, or amend §0's precedence
rule. It cannot be fixed by editing prose.
