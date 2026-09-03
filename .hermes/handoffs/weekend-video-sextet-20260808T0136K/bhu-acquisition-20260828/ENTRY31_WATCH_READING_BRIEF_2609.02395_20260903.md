# Entry-31 watch — reading brief for DUHO (the human reader; ruling "22a, me", 2026-09-03 14:33 KST)

**Candidate:** arXiv:2609.02395 (submitted 2026-09-02) — Astronomy & Astrophysics manuscript no. main                                                                                 ©ESO 2026 September 3, 2026
**Pinned text:** `bhu-reading-20260823/sources/2609.02395_clean.txt` (pdftotext -layout, 736 lines) sha256 `61c9f95b21beaa8a3c650f55ec2ad83b46438df810081c33814f1ef5b7a0f6ca`
**Pinned PDF:** `bhu-reading-20260823/sources/2609.02395.pdf` sha256 `d9a4a6977770df2ad71cdc13d9cf3dd136c620cea55c7b5cf1bf9ad355c87936`
**Why it surfaced:** the Tuesday watch query (run by hand 09-03 13:47 KST) matches neutron-star mass terms; the watch never
interprets. This brief stages the read; **nothing is stamped** — your verdict arrives as a Blanc relay.

## What you are testing (entry 31, Smolin 2004 §4)
A neutron star with a **secure central mass ≥ 2.5 M☉** (resolved identity: pulsar timing or light-curve mass, not a
gravitational-wave secondary of unresolved nature) is the paper's own "certain refutation". Current best secure
maximum in the ledger: PSR J0740+6620, 2.08 ± 0.07 M☉ (Fonseca 2021), 6.0σ below the bar.

## The criteria, verbatim from `NS_MASS_WATCH_PREREG_20260902.md` §2
## 2. Fire / re-gate / clear criteria — declared now
Let a candidate measurement have mass M ± σ (1σ, symmetric approximation; asymmetric errors use the
lower error), from a source with a **resolved neutron-star identity** (radio/optical pulsar timing or
light-curve mass; NOT a gravitational-wave secondary of unresolved nature).
- **FIRE_CANDIDATE:** (M − 2.5)/σ ≥ 3, in a **peer-reviewed** publication (preprints raise a
  RE_GATE, never a FIRE_CANDIDATE — the lane's published-papers-only rule). A FIRE_CANDIDATE is a
  two-seat gate + packet to Duho; the standing changes only on his stamp.
- **RE_GATE:** (M − 2.5)/σ ≥ 2 in any source, OR any peer-reviewed M > 2.5 central value at ≥ 1σ, OR a
  GW secondary with a resolved NS identity at M > 2.5 — a human reads and a two-seat gate decides
  whether the ledger changes.
- **HINT (log only):** a new measurement with posterior P(M > 2.5) ≥ 5% that does not meet RE_GATE.
- **CLEAR (no action, logged):** anything else, including tighter errors on known stars below the bar.
- **Battery rule (existing, §4): a secure central mass ≥ 2.5 M☉ added to the ledger FAILS the
  battery.** The bands above are for reading hits; the ledger is edited only after a two-seat gate.

## Machine pre-read (Tori, not a verdict)
- Abstract: an optical-pulsation SEARCH (SiFAP2 @ TNG) of rotation-powered redback / black-widow millisecond pulsars,
  epoch folding on published radio/γ-ray orbital solutions. Not a mass-measurement paper.
- Solar-mass mentions in the pinned text (first 10): 
  - L81: periods Porb ∼ hours) with low-mass (≲ 1M⊙ ) companion                           When the accretion phase is over, the bulk of their emission
  - L94: systems hosting a donor star of M ∼ 0.2 − 0.4 M⊙ , while
  - L95: black widows (BWs) host companions with M < 0.1 M⊙ .                                        58515.19481           6.3
- Expected reading: **CLEAR** (no new neutron-star mass; no P(M > 2.5) posterior). If any companion/pulsar mass with
  an error bar appears, apply the §2 bands above to that number.

## What to send back (one line, via Blanc)
`31-watch 2609.02395: CLEAR` or `HINT` or `RE_GATE` or `FIRE_CANDIDATE`, with the line number of the mass you used if any.
State-file effect: none until your line arrives; the ledger changes only after the two-seat gate (prereg §4).
