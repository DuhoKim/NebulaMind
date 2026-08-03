# YUI FLOW — M2/SFA Omni Flash Voice-Reference CANARY (one submit)

Issued by Hwao 2026-07-16. Marker: `M2_SFA_OMNI_VOICEREF_CANARY_20260716`
Lane: Yui / Flow on Studio. Scope: exactly ONE account submit, then stop and report.

**What this is:** the Method-2 (SFA, source-first adjudication) explainer will need its own narration set. PGR narration used Veo 3.1 Quality native voice at 100 credits/submit. This canary validates the cheaper, voice-locked route — **Gemini Omni Flash with a Voice Reference** — before Hwao authorizes any M2 batch. The canary PASSING authorizes nothing by itself; report and wait for the batch brief.

---

## Verbatim narration (the ONLY line; word-for-word, nothing added or dropped)

> "Method 2 is source-first adjudication. Every statement starts from the papers themselves, and claims are ranked by how strongly independent sources corroborate them."

## Reference assets

- **Voice Reference (attach in Omni Flash):** `/Users/duhokim/HermesOps/scripts/clips/narration/vo_test_01.mp4`
  sha256 `135d485f99e1966fd6739efad20748fe0a01155972b372ae31a8a4ea535e9d23` — the locked series narrator (8.0s, median F0 210.53 Hz, median spectral centroid 694.81 Hz, RMS −17.84 dBFS). Same asset the PGR audio-match analyzer used.
- **Narrator descriptor (identical to intro + PGR, keep verbatim in prompt):** "a warm, calm, professional female documentary narrator delivers a clean studio voiceover with no on-screen speaker"

## Prompt to paste (exact)

> Static minimalist deep-navy studio backdrop with a subtle faint spiral-galaxy texture in one corner, soft cyan and warm amber accent glow, plain empty background. No on-screen speaker, captions, subtitles, logos, or added text. A warm, calm, professional female documentary narrator delivers a clean studio voiceover with no on-screen speaker, saying exactly: "Method 2 is source-first adjudication. Every statement starts from the papers themselves, and claims are ranked by how strongly independent sources corroborate them." Ambient noise: subtle cosmic ambience kept low under the voice.

## Flow configuration (verify EVERY item in the settings popup before submit)

- Model: **Gemini Omni Flash** (video), with the Voice Reference above attached and visibly named in the UI
- Duration: **8s** — if Omni Flash does not offer an 8s chip, STOP and report the offered options; do not improvise
- Aspect: **16:9** · Output count: **1x** · Pacing: serial, single job
- **Displayed credits per submit: READ AND RECORD THE EXACT NUMBER.** Expected band 15–30 (capability map). Outside the band, or not visible → STOP, no submit. Credits context: 22,208 remaining, renews Aug 4.

## Exact target + broker (non-negotiable)

- Target: **window 1, tab 2** — same owned Flow project URL (project `a22b5b61-833d-4e62-857b-4a7030b93bfa`). Acquire the write-set lease via the broker; no direct RUN_LEDGER appends; `VERIFY_OK` precheck (6191 at issue time).
- Patched `probe_exact` semantics apply: genuine project-URL mismatch → emergency_freeze; matching URL with placement mismatch → non-freezing local HOLD, release own leases, report.

## One-submit quality gate

1. **Pre-submit:** exact-target verify → full config verify (model / voice-ref attached / 8s / 16:9 / 1x / exact displayed credits) → re-verify after paste (PGR pattern).
2. **Submit once.** Flow is async — poll the card to a TERMINAL state before judging (no read-immediately-Failed). Accepted-then-Failed at low % = render-backend outage signal (seen 2026-07-15, not charged): do NOT retry, report.
3. **Post-download checks (all must pass):**
   - Transcript is the verbatim line word-for-word — no added, dropped, or reworded speech
   - Voice matches `vo_test_01.mp4` within the PGR analyzer tolerances (F0 / spectral-centroid match); this is the whole point of the canary
   - No on-screen speaker, captions, subtitles, logos, or rendered text; duration ≈8s; audio levels sane (no clipping, voice clearly above ambience)
4. **Output:** create `/Users/duhokim/HermesOps/scripts/clips/method2_sfa/`; save clip as `vo_sfa_canary_01.mp4` (refuse to overwrite); write `M2_SFA_VOICEREF_CANARY_ACCEPTANCE.json` with per-check results, media_id, lease id, exact displayed credits, sha256s; update lane state.
5. **Either way — PASS or FAIL — zero further submits.** Release leases, report to Hwao with the acceptance JSON path + sha256. PASS ⇒ Hwao issues the M2 narration batch brief. FAIL ⇒ hold; no retry without Hwao.
6. **STOP + hold for Duho on any `google.com/sorry` or challenge; never interact with a challenge.**
