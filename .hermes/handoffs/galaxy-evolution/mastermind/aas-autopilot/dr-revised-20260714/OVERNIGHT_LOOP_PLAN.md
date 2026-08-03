# OVERNIGHT DR MANUSCRIPT LOOP — plan (Duho, 2026-07-14 ~23:45 KST)

GOAL: iteratively improve the 9 aas-autopilot AASTeX drafts using Deep Research, until **10:00 KST 2026-07-15 (HARD STOP)**.
LOOP: revise 9 drafts (incorporate DR packets) -> DR reviews each -> DR re-researches the gaps -> revise again -> DR reviews again -> ... until 10:00.

## Who does the work: TORI + GORU (+ WonE). NOT Hwao.
- **Tori (lead operator):** runs the loop end to end — does the manuscript REVISION writing (integrator), directs the DR runs, sequences rounds, captures receipts. Pulls in helpers as needed.
- **Goru (agy DR driver):** runs the Deep Research REVIEW of each revised paper (referee: blocker/major/minor + safer wording, real sourced) and the RE-RESEARCH on the gaps, on the Pro via Deep Research. Serialized submits; save reference artifacts; delete own conversations (history hygiene).
- **WonE (agy):** writer/integrator ASSISTANT under Tori — help fold review feedback + new sources into the drafts.
- **Garu (agy):** overnight WATCH — track round progress, flag freezes/challenges/anomalies to Hwao, keep the ledger clean.
- **Hwao (captain, coordinate only — does NOT write or review):** enforces the freeze policy + 10:00 stop, adjudicates STOP-class, reports to Duho in the morning.

## Hard rails
- DR = REFERENCE ONLY for research + review; DR never edits a .tex. Revisions go to `dr-revised-20260714/roundN/`, NEVER overwrite the published integrated drafts, NEVER committed/published.
- PRESERVE every measured SDSS invariant EXACTLY; real-data-only; association-not-causal; DR sources added only as real \citep{} with verifiable IDs; skip not-usable/unverifiable sources.
- LEDGER discipline: during active submits ONLY the broker writes the ledger — NO concurrent direct journal appends (that caused tonight's epoch-collision freeze).
- FREEZE POLICY (overnight): BENIGN concurrency freeze (ledger collision / lease race, NOT an account challenge) -> raise to Hwao, Hwao auto-resets + continue. ACCOUNT challenge/CAPTCHA/sign-in/throttle -> STOP + hold for Duho; never push the account.
- Serialized account submits (broker lease). Capture receipts each round; log sources added/skipped.

## Round 1 (start now): Tori (+WonE) revise all 9 drafts incorporating the DR packets
- Input drafts: integration-runs/INTEGRATED_9_PAPERS_20260709T012051Z/NN_*/aastex/*_integrated.tex
- Input DR packets: dr-research-lane-9-20260714/packets/paper_NN_*_dr_packet.md
- Output: dr-revised-20260714/round1/paper_NN_r1.tex
- Then hand to Goru for DR review, then re-research, then round 2, ... until 10:00.
