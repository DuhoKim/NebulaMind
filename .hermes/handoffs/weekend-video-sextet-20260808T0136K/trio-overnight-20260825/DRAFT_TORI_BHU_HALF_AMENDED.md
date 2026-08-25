# BHU half — Tori, AMENDED per Goru's two catches (2026-08-25 11:10 KST; replaces both
# prior drafts in full)

## Plain-language lead

The night settled this for the BHU lane: the evidence table for the new anisotropy study is
now sealed — both reviewing engines pass it, after one of them spent five rounds inventing
quote-forgeries that forced five rebuilds of the checker. And this morning, on Duho's go, the
study's final judgment started running under rules that were written down before anyone knew
the answer.

## The facts, evidence-classed, receipts named

1. MEASURED — Track A closed, both engines. First lines verbatim: "PASS_TRACK_A_AMENDED"
   (bhu-theory-phase4-anisotropy-20260823/REGATE3_TRACKA_VERDICT.md); "PASS_TRACK_A"
   (KGATE_TRACKA_VERDICT.md).
2. MEASURED — Track B freeze CLOSED, both engines. First lines verbatim:
   "PASS_TRACK_B_FREEZE" (KGATE_TRACKB_VERDICT.md, 08-24 19:04) and "PASS_TRACK_B_FREEZE"
   (REGATE5_TRACKB_VERDICT.md, file mtime 10:49:32) — GORU CATCH 1 RESOLVED: the file exists
   and reads PASS; my 10:58 "no file" check used the exact path (session log) yet the mtime
   predates it — consistent with a staged compose-then-move write landing between my check
   and 11:02; the artifact is the authority.
3. MEASURED — the verifier war: five codex HOLDs (GATE_TRACKB → REGATE4, first lines all
   HOLD) forced verifier v4→v8; v8 passes 50/50 quotes, 0 manual acceptances, 0 fallbacks,
   8 corruption self-tests failing through the corpus row path (b_verify_ledger.json 50 rows;
   b_verify_quotes.py; commits 4445e363→736007f0, 08-24 18:49→08-25 10:42).
4. MEASURED — frozen tables unchanged through all rebuilds: B2 = 11 rows, B3 = 7 rows, B1 =
   reference tier (TRACK_B_FREEZE.md).
5. GORU CATCH 2 RESOLVED, receipt-true — Track C is NO LONGER "not started": Duho's go was
   recorded 11:04 (TRACK_C_GO_RECORD.md; operative line verbatim: "Track C has his GO. The
   precondition your brief set is met — PASS_TRACK_B_FREEZE landed at 10:49 — and he
   authorizes the confrontation to run under the judgment criteria exactly as pre-registered
   in TRACK_C_BRIEF.md"). The confrontation executed 11:06; its artifact's first line
   verbatim: "# Track C verdict — the confrontation, executed as pre-registered" — a
   PRE-GATE DRAFT by its own header, and per Duho's sequencing rule its CONTENT stays out of
   this report until its gates pass.
6. MEASURED, in flux at 11:08 — Track C gate states: codex first line verbatim
   "HOLD_C2_CRITERION_DRIFT_ROW_MISCLASSIFICATION_AND_SCOPE_EXCESS" (GATE_TRACKC_VERDICT.md);
   kimi gate RUNNING, dispatched ~11:07, no verdict file at 11:08:29. Amendment cycle ahead;
   no stronger claim exists.
7. MEASURED — the DESI curvature watch is verified for its next tick (lane
   desi_curvature_watch_state.json: last_error null, seen 25); weekly, next 2026-08-31
   10:00 KST; nothing fired overnight.

## Suggested slide headlines (numbers all present above)

- "The forgery war is over: five rebuilds, eight corruptions dead, both engines pass" (50/50,
  0, 8, 5)
- "Track C launched under pre-registered rules — and its first review promptly said HOLD"
  (go 11:04; codex HOLD verbatim; kimi running at 11:08)
- "B2 eleven rows, B3 seven, unchanged through the whole war"
