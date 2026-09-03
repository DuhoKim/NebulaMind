# V137-H AMENDMENT RECORD — SIGNED 2026-09-03

**Signed.** Duho, in the chat channel under the §17 convention, relayed verbatim by Blanc at 2026-09-03 22:20 KST:

> "V137 signed: 700fd0d2…d190 at 2026-09-03T13:20:00Z"

**Digest signed:** `700fd0d29d7f06b9e938b7e48bac729080cc9661bf00f08bbd24a2ad467fd190` — the sha256 of `PREREG_SUCCESSOR_DRAFT_V137_20260903.md` with `SIGNATURE UTC:` and `DUHO SIGNATURE:` blank. Verified by Blanc at relay time against the file on disk, and identical to the ACCESS_SHA proven by the referee. Prefix and suffix in Duho's sentence match.

**Signature lines now filled** (this changes the file's digest, as with V135 and V136):
```
SIGNATURE UTC: 2026-09-03T13:20:00Z
DUHO SIGNATURE: 700fd0d2…d190 at 2026-09-03T13:20:00Z (chat signature via Blanc relay; V136 preamble mechanism carried into V137-H)
```
Digest of the signed-and-filled file: `bf46e62a1c9c98935ebe66788bd2847ac94bbe9d33d3056aafbb49158e2544ff` — recomputed and recorded in the commit that carries this record.

**Predecessor:** V136 (amendment-signed 2026-09-03T05:15:00Z, digest `6b3ff130…`). P0's ssh-signed V134 manifest is untouched and remains the freeze at `d1be4a3b…`; manifest verified 30/30 OK at referee time.

**Referee:** agy `V137H-REFEREE-V2` — SIGNABLE, COUNT 0, ACCESS PROVEN on `700fd0d2…`. Round 1 was NOT-SIGNABLE with one FATAL finding (the BS-3g rows had to state the machine facts); CLOSED in round 2. Trace: 136 computed transitions, 0 problems.

**What is signed.** The amendment adopts Duho's ruling "as their recs" (direction #69, 2026-09-03 19:37 KST): BS-3g DESIGN accuracy a₀ = 0.95 and Γ = 0.10, deriving Δγ = 0.004. It records, without softening, that the resulting sweep FAILED the invariance test: draw 94 at γ = −0.10 is REPRODUCED-LONGO against the INCONCLUSIVE baseline, a decision-changing cell; deterministic across two runs (receipt `19ffcbab…`); 0 of 5,049 cells INCONCLUSIVE-BY-CALIBRATION; min `a_lb_b` 0.8639832635983262; `sigma_gamma` 0.04790176316993866.

**What is NOT decided.** No criterion, range, statistic or production rule changes. BS-3g remains DESIGN, UNFILLED; BS-6 remains blocked. The design consequence (packet options A/B/C/D, and E = poll first) is with Duho and is not acted on. The blind committee poll already run (CODEX, AGY, KIMI — unanimous A, high confidence) is advice, not a decision.

Paper HOLD stands. Validation-only discipline unchanged; nothing here feeds the flagship.
