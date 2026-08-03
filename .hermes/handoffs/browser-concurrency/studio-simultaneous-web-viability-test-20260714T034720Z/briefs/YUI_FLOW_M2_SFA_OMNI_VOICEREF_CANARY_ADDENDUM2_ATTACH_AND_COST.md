# ADDENDUM 2 — M2/SFA Omni voice-ref canary: manual attach gate + amended cost rule

Issued by Hwao 2026-07-16. Amends brief (sha256 `315b3657…da5a2e`) and Addendum 1 (sha256 `f21be79c…2222f`). Marker unchanged: `M2_SFA_OMNI_VOICEREF_CANARY_20260716`. Duho has ordered the first submit — no further approval gate from Hwao after the checks below pass.

## Facts this addendum responds to

- Declared preconfig contradicted live DOM (composer was still Nano Banana Pro, no voice ref) — the page has now shown both a client-side error and a composer state reset during upload attempts. Verify-before-submit stays mandatory precisely because of this.
- Yui's one bounded switch to Video / Omni Flash / 8s / 16:9 / 1x succeeded under Duho's order; UI showed **12 credits**.
- vo_test_01 could not be attached: the native file picker needs foreground, and CUA is unavailable on this host (capture 0x0, list_apps empty). Yui correctly did not take foreground. Zero submissions, no lease, no challenge.

## Amended cost gate

The 15–30 band came from the capability-map memory and is evidently stale for this config. The protective bound is the ceiling, not the floor. New rule:

- Submit is allowed only if the model label reads exactly **Gemini Omni Flash** AND the displayed credits per submit is **≤ 30** (this is what prevents an accidental Veo Quality 100-credit submit).
- **12 is the expected reading.** Record the exact displayed number in the acceptance JSON whatever it is.

## Duho's manual sequence (in window 1, tab 2; do the attach LAST, then hands off)

1. Composer → **Video → Gemini Omni Flash** (if it reset again).
2. **8s / 16:9 / 1x**.
3. **Attach the voice reference via the native file picker:** `/Users/duhokim/HermesOps/scripts/clips/narration/vo_test_01.mp4` — confirm a chip/name for `vo_test_01` is visible in the composer.
4. Confirm the credits number is visible (expect 12). Leave the composer open; do not navigate or switch tabs. Say "attach done".

## Yui's resume (immediately after "attach done")

1. Broker account-submission lease.
2. **Fast read-only verify (mandatory, no clicks through menus):** model label exactly Gemini Omni Flash · `vo_test_01` chip visible · 8s · 16:9 · 1x · exact displayed credits recorded and ≤30. A submit without the vo_test_01 chip visible is a wasted canary — the voice reference IS the thing under test. If the read fails structurally: second hold receipt + screenshot fallback (Addendum 1), no probing.
3. Paste the exact brief prompt → re-verify (config unchanged, chip still present) → **submit once**.
4. Poll to terminal state; accepted-then-Failed = outage signal, no retry. Post-download checks, acceptance JSON, receipts, lease release — all per the original brief. Zero further submits either way.
