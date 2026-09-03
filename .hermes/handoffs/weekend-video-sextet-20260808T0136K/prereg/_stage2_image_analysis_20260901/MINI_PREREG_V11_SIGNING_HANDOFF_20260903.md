# MINI-PREREG V11 — SIGNING HAND-OFF TO BLANC (Hwao, 2026-09-03 15:5x KST)

**Status.** V11 (amendment to the signed V10 under §17.6) is SIGNABLE: agy round 1 SIGNABLE-AFTER-REPAIRS
(one operational finding), round 2 through nm_referee_dispatch.sh with ACCESS PROVEN: SIGNABLE, F1 CLOSED,
minimality PASS, 0 new findings. V10's signed bytes untouched. Ruling "b" (direction #62) implemented; ruling
"a" (validation only, nothing feeds the flagship) stands.

**File.** `MINI_PREREG_GZ_TIERC_DRAFT_V11_20260902.md` (commit af0e9b0d7 on feat/paper-workflow-v2).
**Preview digest** (both signature lines blank): `a4b5f557eff5de1db72dc574a8be1787c1873f23163f2dae6186067b6576ac99`.
V11 keeps V10's §17.1 mechanism: Duho fills the UTC line FIRST, so the digest he states differs from the
preview. Blanc stages a UTC-filled copy and computes it (helper or shasum agree while DUHO SIGNATURE is blank):

    python3 miniprereg_sign_digest.py <utc-filled copy>

**One paragraph for Duho.** Nothing about the study's science changed. V11 does what you ruled: the
"was this pixel observed" check uses the survey's exposure-count map instead of the inverse-variance map,
the same fail-closed guarantee at 1/36th the bytes; the manifest lists three planes per brick (image,
maskbits, exposure count); the seal gate checks all three. One more sentence was added at the referee's
insistence: the partial inverse-variance files already on disk are disclosed as known extras, identified
by their receipts, never read, and any other stray file still refuses the seal. Everything else is
byte-identical to what you signed this morning.

**Ceremony:** one sentence in the Blanc chat: "mini-prereg V11 signed: <digest> at <UTC>". Blanc relays;
Hwao verifies, fills the signature line, writes MINI_PREREG_V11_FREEZE_RECORD_20260903.md, commits.
**Then (your 15:20 order, step 2):** stop the inverse-variance download (partial stays, receipted), fetch
nexp-r + maskbits for 17,947 bricks (4 workers, ~2 h), re-run the seal gate over three planes (~5 h).
