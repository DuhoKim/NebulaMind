# MINI-PREREG SIGNATURE CEREMONY PACKET — staged 2026-09-02 17:1x KST (Hwao)

**In plain words.** The Tier-C mini-preregistration reached SIGNABLE on its
seventh hostile referee round. Twenty-one findings were raised across V1–V6
and every one is closed; the V7 round raised none. Nothing has been measured,
no pixel has been opened, the P0 blind and Tier A are untouched, Tier B is held.
Signing V7 freezes the rules; it does NOT start measurement — that still waits
on the pre-pixel gates the document itself defines (§5 completeness, §7.11
integrity with the independent NERSC checksum re-fetch, §9 instrument, §10
BS-4 anchor). You CHECK, never trust: run every command yourself.

**What you are signing:** `MINI_PREREG_GZ_TIERC_DRAFT_V7_20260902.md`
(file sha256 as staged, both signature lines blank:
`a7cdc045f55e88efef75760ac63842cb294bd85dc1bc74d987e31373ef898c9b`).
Referee: `AGY_MINIPREREG_REFEREE_V7_20260902.md` — VERDICT: SIGNABLE, COUNT: 0.

## The ceremony — five steps

1. **Confirm the staged bytes and the referee verdict:**

       cd /Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/weekend-video-sextet-20260808T0136K/prereg/_stage2_image_analysis_20260901
       shasum -a 256 MINI_PREREG_GZ_TIERC_DRAFT_V7_20260902.md
       tail -3 AGY_MINIPREREG_REFEREE_V7_20260902.md

   The first must print exactly `a7cdc045f55e…898c9b`; the second must show
   `VERDICT: SIGNABLE` and `COUNT: 0`. If either differs, STOP and surface it.

2. **Fill the UTC line** (§17.1). Edit the file and replace the blank
   `SIGNATURE UTC:` line with, e.g., `SIGNATURE UTC: 2026-09-02T08:20:00Z`
   (the current `date -u +%Y-%m-%dT%H:%M:%SZ`). Touch nothing else.
   Leave `DUHO SIGNATURE:` blank for now.

3. **Compute the signing digest yourself** (§17.1–17.4: the file with the
   `DUHO SIGNATURE:` line blank, nothing else normalized):

       python3 miniprereg_sign_digest.py MINI_PREREG_GZ_TIERC_DRAFT_V7_20260902.md

   It prints one 64-hex digest — that is the number you sign. (Independent
   cross-check with the OS tool: `shasum -a 256 MINI_PREREG_GZ_TIERC_DRAFT_V7_20260902.md`
   must print the SAME value as long as the `DUHO SIGNATURE:` line is still blank.)

4. **Sign the digest with your own key tooling** (this packet holds no key
   and signs nothing). Same key as P0, new namespace:

       printf '%s' '<digest>' | ssh-keygen -Y sign -f ~/.ssh/id_ed25519 -n nmpr-miniprereg-tierc > MINI_PREREG_V7_digest.sig

   Then record `MINI_PREREG_SIGNATURE_20260902.md` beside this packet with:
   the digest, the signature block (the .sig contents), your public key, the
   date/time. Optionally paste the signature after `DUHO SIGNATURE:` in the
   draft — verification blanks that line before hashing (§17.3), so the
   digest is unaffected.

5. **Say "mini-prereg signed" through Blanc.** Hwao folds the signature file
   and the UTC-filled draft into the repository, the freeze is in force
   (§17.5), and the pre-pixel gates begin ONLY when the Tier-C acquisition
   completes (§7.11 set condition; ETA ~noon 2026-09-03 KST).

## What the signature covers and what it does not

Covers: every constant, threshold, source, order, exclusion, formula, verdict
band and custody rule in V7; the six pinned files in `miniprereg_pins/`
(hashes in §2.10–2.14, re-hashed by agy in every round); the §19 register of
178 frozen rules. Does NOT cover: run-time artifacts that do not exist yet —
the completed acquisition journal head, the freeze-time seal receipts, the
NERSC checksum binding digest, the sample manifest, and every chi-bearing byte;
those are produced under the rules this signature freezes, and their gates
verify against it (§16.7c: a boolean passed to the verdict program that
disagrees with its seal receipt voids the run).

## Chain record

| version | referee verdict | findings raised | notes |
|---|---|---|---|
| V1 | NOT-SIGNABLE | F1–F3 | missing pins, missing BS-4 mechanics |
| V2 | NOT-SIGNABLE | F4–F9 | verdict program printed one word; F9 mis-labelled by agy (instructed change) |
| V3 | NOT-SIGNABLE | F10–F13 | prereg_sha256 undefined; journal unpinned; input schema absent |
| V4 | NOT-SIGNABLE | F14 | coordinator attestation ≠ receipt |
| V5 | NOT-SIGNABLE | F15–F17 | false git chronology (Hwao's brief); computed==published never receipted |
| V6 | NOT-SIGNABLE | F18–F21 | 42 not 35 (Hwao's rounded cutoff); receipt-copied checksum; gate unbound |
| V7 | **SIGNABLE** | none | all 21 closed |

Ruling #55 scope unchanged throughout: Tier-C only; P0 blind and Tier A
untouched; Tier B held; signature before any measurement.
