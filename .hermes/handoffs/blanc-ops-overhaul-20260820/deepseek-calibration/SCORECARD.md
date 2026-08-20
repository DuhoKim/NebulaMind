# DeepSeek calibration scorecard (Blanc, 2026-08-20 ~15:2x KST)

Protocol: known-truth artifact (KUN committee gate report, PASS, 51 lines) run
clean AND with one seeded defect (AGREE_CONFIDENT 1,812 -> 1,712: breaks the
stated 0.9060 proportion AND the sum to n=2,000). Fresh Nous-route one-shots.

| model | seeded defect | clean passes | false problems | hallucination |
|---|---|---|---|---|
| deepseek/deepseek-r1 (PRIMARY) | **CAUGHT** — recomputed 1712/1900, flagged the exact quote with correct math. Partial diagnosis: adopted 1,900 as denominator instead of flagging the contradiction with stated n=2,000; two collateral proportion flags follow from that (arithmetic itself correct) | **CONFIRMED with real work** — recomputed the sum, derived binomial sigmas per 2sigma claim | 0 | 0 |
| deepseek/deepseek-chat (secondary) | **MISSED + hallucinated a confirmation** — re-quoted stated proportions as "within 2sigma" without dividing; never checked the sum | confirmed (no invented problems) | 0 | 1 (vouched for the seeded line) |

Verdict: R1 admitted as a verification lens; deepseek-chat REJECTED for gate
duty (a seat that vouches for numbers it did not recompute is worse than
absent). Sweep result: no newer R-series id in the local model catalog; a
deepseek-v4-flash/v4-pro family IS listed (v4-pro-0813 newest) — untried,
worth a probe. Runs preserved in this directory.
