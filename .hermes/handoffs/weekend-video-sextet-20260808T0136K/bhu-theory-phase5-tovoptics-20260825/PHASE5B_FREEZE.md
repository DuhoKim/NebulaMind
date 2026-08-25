# Phase 5b freeze record

- **Frozen 2026-08-25 19:39:56 KST** on Duho's verbatim order, relayed by Blanc:
  **"give phase 5b the go"**.
- Brief: PHASE5B_PLASMA_BRIEF.md sha256
  51c3452aa359f1c9e297c7bfaf16a41a30b8ccb1ff2ee24da16a6b9ed8f76ef0 (mtime 19:29:42 KST).
- **This go is PROSPECTIVE: it precedes P1.** Stated plainly for contrast with the 18:16 relay
  earlier today, which was a redundant second delivery of an already-given decision and which
  I briefly and wrongly recorded as a retroactive authorization (PHASE5_FREEZE.md Addenda 2
  and 3). Here the order came first and the work follows it.
- **What is authorized: the assumption-RANGE METHOD, not any plasma model.** A1–A5 are carried
  as ranges, no single choice is adopted, every deliverable is reported across the ranges, and
  if nothing survives all of them, that is the finding.
- **Scope of the K4 boundary, as put to Duho:** it covers n_e and composition only. P1's
  timelike-r̄ geometry is a DERIVATION I OWE — my error, not an assumption boundary — and is
  not covered by the authorization; it must simply be done correctly.
- Ping rule in force: only before a stage that can END the phase or needs a choice only Duho
  can make. Routine stage passes do not need him.
- The kimi S0–S2 gate is a separate thread (died on HTTP 429, re-dispatched as
  tori:bhu5-gate-k2); it cannot restore the withdrawn exclusion and does not block 5b.

## Pin restored (2026-08-25, on Blanc's cockpit check)

**The finding was real.** The freeze record above pins PHASE5B_PLASMA_BRIEF.md at sha256
51c3452a…, and for a period the file on disk hashed ae2dcc63… instead. Timeline from mtimes:
brief 19:29:42 → freeze written 19:40:43 pinning 51c3452a → **brief modified 19:42:31**. Duho's
go at 19:39:56 was given against the 51c3452a bytes, and Blanc quoted that hash in the relay.

**What changed:** Addendum A (the A6 bulk-equation-of-state assumption) was appended directly
to the brief file. The edit was a PURE APPEND — the diff adds lines and modifies none — so the
frozen text itself was never altered. But appending to the brief at all violates the convention
this lane set in PHASE5_FREEZE.md: *"Amendments require a dated addendum; the brief file does
not change."*

**Disposition — option (a), the substantive route.** A6 is a genuine sixth assumption, not a
typo, so it does not get folded into a re-pin. The brief is restored from git to the exact
51c3452a bytes (verified: the restored file hashes 51c3452a…), and Addendum A now lives in
**PHASE5B_ADDENDUM_A.md** with its original text and original 19:42:31 timing recorded there,
including the fact that it was written in the wrong place. The go stands unchanged on bytes
that exist again.

**Why this matters beyond bookkeeping:** a pin that points at vanished bytes is exactly the
state a pin exists to expose, and I created it while writing an addendum whose whole purpose
was to keep an assumption honest. The check that caught it was Blanc's, not mine.
