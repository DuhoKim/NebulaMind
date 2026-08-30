# Gate brief — B41 v5 (CGATE's final confirmation round)

CGATE_B41V4 closed with: "Bind all four chains to actual scoped receipt text, and add the
missing flag-6 read phrase predicate. The same numerical conclusion can then be confirmed
without qualification."

v5 (`b41_census_coverage.py`, commit 2860644f0) does exactly that and nothing else:

- **Four explicit refresher chains**, each binding the entry's own refresher line in CGATE_B37,
  the actual prior artifact, its first-line token, and a content fragment proving the artifact
  engages the right source: 23 → CGATE_A10 ("Do not promote entry 23", HOLD_UNCALIBRATED_CUTOFF);
  26 → CGATE_A5 ("Gaztanaga, entry 26", AUDIT_CONFIRMED_TIER_ONLY); 44 → CGATE_B17 (the (5.1)
  DGP sentence, AUDIT_REFUTED_MISSED_EQ5_1_AND_TIER); 54 → AGATE_B15 (the Planck 1807.06209
  fragment, CONTRAST_REFUTED_NAIVE_STATISTICS).
- **Strengths printed, not implied**: the script now prints that none of the four priors carries
  its own "read in full" sentence, that the full-source testimony for 26/44 is CGATE_B37's own
  wording, and that AGATE_B15 is subject-matched only — it never names entry 54. Nothing is
  implied to exist that does not.
- **Flag 6** now also binds the notes' read phrase ("read at last").
- Docstring records AGATE_B41V4's confirmation of the defective v4 as another instance of the
  one-seat-does-the-work pattern.

**Your task:** run it, verify the four chains against the artifacts, and rule. If it survives,
this is the census closer of record: coverage 39/39; paper-tier miss rate 1 of 2; precision
1 of 3; claim-level sensitivity not measured, two labelled observations.

**Verdict file:** `CGATE_B41V5_VERDICT.md`, first line a single token
(`B41V5_CONFIRMED` / `B41V5_REFUTED_<REASON>` / `B41V5_NARROWED_<REASON>`).
