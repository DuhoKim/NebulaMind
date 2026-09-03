# V137-H — SIGNABLE, signing handoff for Blanc → Duho (2026-09-03 22:15 KST)

**File:** `PREREG_SUCCESSOR_DRAFT_V137_20260903.md` (successor build directory), round 2.
**Plain sha256, both signature lines blank (SIGNATURE UTC and DUHO SIGNATURE, lines 1619–1620):**

```
700fd0d29d7f06b9e938b7e48bac729080cc9661bf00f08bbd24a2ad467fd190
```

**Referee:** agy `V137H-REFEREE-V2` — VERDICT SIGNABLE, COUNT 0, ACCESS PROVEN on that same digest. Round 1 was NOT-SIGNABLE with one FATAL finding (the BS-3g rows had to state the machine facts); it is CLOSED. Trace 136 transitions, 0 problems. P0 manifest 30/30 OK. Diff against the round-1 file is the two BS-3g lines only (hunks 941c941, 1252c1252); V135/V136 amendment records and the P0-signed draw mechanics are untouched.

**What Duho is signing:** an amendment that adopts his ruling "as their recs" (a₀ = 0.95, Γ = 0.10, direction #69) and records, without softening, that the resulting sweep FAILED the invariance test on one decision-changing cell (draw 94 at γ = −0.10, REPRODUCED-LONGO against the INCONCLUSIVE baseline), deterministic across two runs (receipt `19ffcbab…`), 0 of 5,049 cells inconclusive, min `a_lb_b` 0.8639832635983262, `sigma_gamma` 0.04790176316993866. BS-3g stays DESIGN/UNFILLED and BS-6 stays blocked. Signing does **not** decide what follows: that choice is put to him separately in `BS3G_DESIGN_PACKET_20260903.md` (options A–D; blind committee poll CODEX/AGY/KIMI unanimous A, high confidence).

Signature convention per §17: Duho states the digest in chat; Blanc relays; Hwao fills SIGNATURE UTC and records the freeze.
