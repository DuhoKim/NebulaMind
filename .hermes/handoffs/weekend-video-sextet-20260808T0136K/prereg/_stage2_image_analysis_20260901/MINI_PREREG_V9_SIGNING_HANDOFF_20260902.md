# MINI-PREREG V9 — SIGNING HAND-OFF TO BLANC (Hwao, 2026-09-02 17:4x KST)

**Status.** V9 is SIGNABLE (agy, AGY_MINIPREREG_REFEREE_V9_20260902.md: MINIMALITY
PASS, F22 CLOSED, no new findings). Nine hostile rounds; 22 findings raised across
V1–V8, all closed. Ruling "a" stands: Duho signs this as a Tier-C validation study
only; nothing feeds the flagship, the parent run, or â.

**File.** `MINI_PREREG_GZ_TIERC_DRAFT_V9_20260902.md` in
`.hermes/handoffs/weekend-video-sextet-20260808T0136K/prereg/_stage2_image_analysis_20260901/`
(committed on `feat/paper-workflow-v2`, 42d94c3bb).

**Preview digest** (both signature-block lines still blank):
`4c0b2b34fab077bed3db7f857238ff3b9eb2b27df1f30c3bc67ab2c39b4885bc`.
Per §17.1 the UTC line is filled BEFORE hashing, so the value Duho states will
differ from the preview. Recompute after filling it, either way:

    python3 miniprereg_sign_digest.py MINI_PREREG_GZ_TIERC_DRAFT_V9_20260902.md
    shasum -a 256 MINI_PREREG_GZ_TIERC_DRAFT_V9_20260902.md   # identical while DUHO SIGNATURE: is blank

**The one-paragraph diff for Duho (V7 → V9; V7 was the SIGNABLE text he heard).**
Nothing about the study changed: not the sample, the tiers, the geometry, the
statistics, the claims boundary, the blind protection, or any pinned file. Only the
way he signs changed, by his own ruling "b": instead of an ssh-key ceremony, he
fills the UTC line, then states in the Blanc chat channel the 64-hex digest of the
file (computed with the `DUHO SIGNATURE:` line blank) plus that UTC time; Blanc
relays it verbatim as a RELAY FROM DUHO; Hwao records digest, time, relay text and
relay timestamp in the freeze record. A stated digest that does not match the
recomputed one freezes nothing, and any disagreement among statement, relay and
record voids the signature. One limit is now written into the text at the
referee's insistence: the repository holds no cryptographic proof of the chat
statement, so a later reader verifying from the repository alone is trusting the
freeze record's copy of the relay — accepted under ruling "b".

**Ceremony (three steps, all Duho's).**
1. Fill `SIGNATURE UTC:` in the V9 file with the current `date -u +%Y-%m-%dT%H:%M:%SZ`; touch nothing else.
2. Recompute the digest (either command above).
3. In the Blanc chat channel, state that digest and that UTC time in one sentence
   ("mini-prereg signed: <digest> at <UTC>"). Blanc relays verbatim; Hwao records.

**After the relay (Hwao).** Freeze record `MINI_PREREG_FREEZE_RECORD_20260902.md`
(digest, UTC, relay text, relay timestamp, recomputed digest match); the UTC-filled
V9 committed; measurement still waits on §7.11 acquisition completion (~noon
2026-09-03 KST) and every pre-pixel gate.
