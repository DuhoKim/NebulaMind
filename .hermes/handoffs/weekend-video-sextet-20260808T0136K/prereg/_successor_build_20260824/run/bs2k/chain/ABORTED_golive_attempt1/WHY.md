# GO-LIVE ATTEMPT 1 — VOID BY DEFECT (2026-09-01 00:58:22 KST)

Post-live verification (Hwao's judgment pass, minutes after emission, before
any verifier consumed the chain) found the opening's monotonic_reading recorded
in MILLISECONDS (monotonic_ms) where the frozen spec's field is a decimal
NANOSECOND count quantized to g (≡ 0 mod 1,000,000 ns). The Row-A signature
itself verified Good (nmpr-rowa, enumerator key) — the defect is the unit, not
the custody. Artifacts preserved here exactly as emitted, never overwritten;
attempt 2 follows the repaired unit through the same stage → verify → go-live
ladder.
