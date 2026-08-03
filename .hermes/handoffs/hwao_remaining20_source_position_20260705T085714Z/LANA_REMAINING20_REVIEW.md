# LANA review — remaining-20 draft (source-position / methods)

**Verdict: ISSUES** — 2 rows need fixes before Hwao gates; the other 18 are safe. Most of the queue is well-routed (kinetic/radio routing correct, non-AGN rows not inflating AGN claims, all successors capped `accepted_limited`, no full-PDF-pin overclaim). Details below.

## Blocking issues (exact row fixes)

**28088 — reason/span mismatch, hold for supervised Gemini.**
The quoted span is *"Stellar feedback can regulate star formation in low- and intermediate-mass systems, but is generally insufficient to fully quench high-mass galaxies."* That is a **mixed / partly pro-AGN motivation** sentence. The `decision_reason` instead asserts *"low-mass high-redshift quenched galaxies are often environmental/satellite systems"* — content **not present in the span**. As written it both overclaims and risks reading a pro-AGN motivation as a non-AGN alternative.
- Replacement: `relink -> 2944 / limitation_or_caution / accepted_limited`, reason rewritten to the actual span (stellar feedback regulates low/intermediate-mass SF but is insufficient to quench high-mass systems). **If the source's true position cannot be pinned from the snippet alone, leave this row `pending` for the single supervised Gemini one-packet second opinion** — this is the row most in need of it. Do not gate it as `support` on the current reason.

**28148 — reason overclaims relative to span.**
`decision_reason` says the source *"reports strong detections of ultra-fast nuclear winds,"* but the quoted span is motivational/broad-framing (AGN feedback *"believed to be driven by powerful outflows … could be a promising mechanism … M_BH–σ"*). No detection is quoted.
- Replacement: keep `relink -> 2943 / accepted_limited`, but rewrite `decision_reason` to match the span (broad AGN-feedback framing, not a detection result) and keep `abstract_only_verified`. Tori's own `limitation_or_counter_reason` already flags the broad-framing caveat — make the reason field consistent with it, don't let "strong detections" stand.

## Caveats Hwao must preserve (not blocking)

- **28069 + 28073** are two `support` rows from the same source (2512.05584) to the same claim 2944. Role-distinction (observational baryon deficiency vs SFR-scaling) is genuine, so allow — but they must **not be counted as two independent corroborations** of 2944.
- **28131** (`route_kinetic_radio -> 2947`) rests on a *definitional* span ("often called radio mode"), not an efficacy result. Routing is correct and cap is right; treat as thin support / near-background. Secondary Gemini candidate if 28088 does not consume the packet.
- **28140** (`-> 2943`) rests on a section-preview methods sentence ("in Section 4 we present our results"), thin as direct evidence; acceptable only because it is capped and 2943 has stronger corroboration (28144).
- **28076** correctly **rejected** from 2947 despite a "radio" matched-term — supernova superbubble, not AGN jet. Preserve this; do not let a later pass re-route it.
- Verification labels are honest: every accepted row keeps `full text not DB-pinned`, `NO_GO` product gate, `accepted_limited` cap. No full-PDF-pin overclaim. Keep it that way.

## Summary
Safe to gate B4/B6/B7/B8 as drafted (with the 28148 reason fix folded in). **Hold B5's 28088** for a corrected role or the reserved Gemini second opinion before Hwao closes it. No SQL/DB/trust/prose/deploy touched by this review.

LANA_REMAINING20_REVIEW_20260705T085714Z
