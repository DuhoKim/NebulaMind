# TERMINAL SIGNATURE RULING — 2026-08-30 20:22 KST

**The principal's words, verbatim (direct message to Hwao's session, immediately after the γ
ratification):**

> terminal signature approved, I'll do the ceremony at run end

**What this rules.** The FILED (V100), AMENDED (V101) recommendation is TAKEN, in its amended
(recomputation-hardened) form — that is the form that was on the table, and "approved" binds
to it:

- At run end the principal performs ONE signing ceremony. The ceremony does not sign a digest
  the enumerator presents; it **RECOMPUTES the terminal head** from the chain bytes and the
  anchor chain under the pinned `gates/terminal_review_verifier.py`, acquired at its printed
  digest and sha-checked by the principal himself with an OS tool **on his own environment**.
- The script has him CHECK, not read: recomputed head vs an independent chain copy, receipt
  digest vs the receipt store, verifier digest vs the printed pin — then sign the canonical
  domain-tagged TERMINAL-REVIEW body
  `(kind, terminal_checkpoint_digest, drain_start_position, recomputed_head, verifier_digest,
  transcript_digest)`.
- **The P7→P9 suffix therefore has its closing human waypoint.** The spec/draft sentence
  "until ruled, the suffix boundary stands as machine testimony with NO closing waypoint, said
  in exactly those words" retires at the next build; what replaces it is scoped honesty:
  between the opening authorization (P7) and the terminal signature (P9) the suffix is machine
  testimony **bracketed by human signatures on both sides**, and a forged interval must agree
  with the waypoint on each side — the same argument the three earlier waypoints already make.

**What this does NOT do.** It does not build anything: `gates/terminal_review_verifier.py`
and the ceremony script remain REQUIRED-DOES-NOT-EXIST build items with their digests printed
when built. It does not touch the ruled event vocabulary, the freeze, v9 (`6a9abbbd…`,
untouched), BS-6, or the first image byte. The Clause-6 extension (P6→P7 via the issuance
pass-record digest) stays FILED-not-taken — this ruling absorbs the stronger item only, as
the V100 filing said.

**Fold plan (V112, same build as the γ ratification fold):** the spec's trust-boundary
paragraph (§3b clock-basis block) — "Adding the act is his to rule: FILED, recommended,
awaiting. Until ruled, …" → RULED with this record quoted; the draft's mirror sites and the
waypoint enumeration (three human waypoints → FOUR: P0 freeze · P6 BS-L · P7 opening auth ·
P9 terminal review); DECISIONS_FOR_DUHO.md updated (done in this commit); superseded
phrases quoted dead per the sweep discipline.

**Recorded also in the track's human-direction history** (direction #10 in
`spin-parity_history.json`).
