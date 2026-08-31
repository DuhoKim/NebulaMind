# BS-2k CONSTANTS + ROSTERS COMMITMENT — RULED 2026-08-31

**The principal's words, verbatim (relayed via Blanc/OPS, typed across two lines):**

> constants and rosters approved as proposed

**What this rules.** Per the packet's own signature block, that phrase takes the
WHOLE packet — `BS2K_CONSTANTS_AND_ROSTERS_PROPOSAL_20260831.md`, sha256
`f9c643455502c21df34861065d2b535a0f4254af9e7f5c9cdf01de79e8fc1977` — which this
commitment binds by digest: the reasons, derivations, margins, named channel
widths and honest notes live THERE at those exact bytes; this file carries the
committed values. Scope exactly as presented, nothing wider: these enter the
BS-2k provisioning materials and are frozen at P0. The Sep-5 BS-1 rule and the
P0 signature itself remain separate and untouched. Recorded as human direction
#18 in the spin-parity history.

## The committed constants (decimal nanoseconds on the monotonic clock unless unitless)

```
C1   g                      = 1000000            # 1 ms reading quantum
C2   commit_bound           = 1000000000         # 1 s
C3   budget                 = 5000000000         # 5 s head processing
C4   Q                      = 16                 # queue bound (unitless)
C5   detection              = 2000000000         # 2 s
C6   D                      = 120000000000       # 120 s decide-within deadline
C7   enforcement_lag        = 30000000000        # 30 s
C8   GATE_PASS_BUDGET       = 10000000000        # 10 s, quantized to g
C9   PASS_RETRY_MAX         = 3                  # unitless
C10  R_max                  = 2                  # renders/object/member
C11  A_max                  = 3                  # closed abort pairs
X1   conveyance_retry_limit = 3                  # per-position attempts
M    M_max                  = 3                  # ALREADY COMMITTED previously
```

**Frozen-inequality check, restated at the committed values:** D > commit_bound
(120 s > 1 s) ✓; D ≥ Q·(budget + commit_bound) + commit_bound (120 s ≥ 97 s) ✓;
enforcement_lag ≥ detection + Q·commit_bound (30 s ≥ 18 s) ✓; R_max ≥ 2 ✓;
GATE_PASS_BUDGET ≡ 0 (mod g) ✓; every clock value ≡ 0 (mod g) ✓. Derived faces
the spec requires be NAMED: touches timely by D − commit_bound = 119 s; refusals
by D + enforcement_lag = 150 s; W0 worst case 5 × PASS_RETRY_MAX ×
(GATE_PASS_BUDGET + 2g) ≈ 150 s per full gate sequence; channel widths
log₂(⌈D/g⌉+1) ≈ 16.9 bits/decision, log₂(⌈budget/g⌉+1) ≈ 12.3 bits/refusal.

## The rosters (both RULED as Option A)

- **Reviewer roster — one entry:** `(Duho Kim, <pubkey supplied at provisioning>)`.
  Committed within the P0-frozen BS-2k provisioning materials under the frozen
  schema `(kind, roster_entries)`, count-prefixed, identity-sorted; machine keys
  excluded by rule; any later change is a re-freeze, never an edit.
- **Custody/escrow holder roster — one entry:** Duho Kim, sole holder. The
  holder-roster digest in the seal-state schema binds this single identity; all
  sealed key material in the escrow; access only through the pinned mediator.
  **The honest note, on the record as ruled:** single-holder custody protects
  against process and machine compromise — the operative threat model — and not
  against the holder himself; the principal already holds P0, so splitting keys
  against himself would add ceremony, not security.

## X2 — the closed operation set: discipline, not a hand list

At provisioning, the class-key operation-token set is EXTRACTED from the §6.1 row
table's own operation column by the pinned extraction tooling, digested, and
committed; a hand-written duplicate list would be the divergent-registry defect.
The principal signed the DISCIPLINE; the extracted membership takes its digest at
provisioning and any mismatch refuses.

## Blind-commit status

None of these values is χ-derived or outcome-coupled; all were proposed and ruled
before any run data exists. Nothing here can move a verdict — only the patience
of the machinery. v9 stays frozen at `6a9abbbd…` throughout; nothing in this
commitment touches it, the Sep-5 rule, or P0.
