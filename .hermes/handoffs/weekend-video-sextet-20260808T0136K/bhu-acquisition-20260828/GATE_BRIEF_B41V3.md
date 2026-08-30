# Gate brief — B41 v3 re-gate (the census closer, after both refutations)

`b41_census_coverage.py` v1 was refuted by both seats on different grounds:

- **CGATE_B41** (ENTRY38_UNRECEIPTED): {38,57} was bound to b33's retrospective comment; entry 38
  had no full-read receipt. → Repaired by **b43** (full read, gated: CGATE_B43 confirmed the tier
  and the 39/39 reading coverage) and by per-batch verdict bindings in v2.
- **AGATE_B41** (MULTIPLE_HOLES): the live flag recompute never scanned entry 5's file (it lives
  under `reviews/`, outside the mapped pool); entry 6's adjudication predates the b28 rule; the
  1-of-2 denominator was called gerrymandered. → Repaired in **v3**: the pool boundary is now
  printed as part of the finding; entry 5's file is scanned separately and the counterfactual is
  computed live — criterion counts (0,0,0), it would NOT have flagged even in-pool, so the miss
  is a DOUBLE miss (never scanned AND vocabulary-invisible); entry 6's basis (batch-9 full read
  reclassifying it QUALITATIVE-DIRECTIONAL, pre-rule, plus B25's paper-level FP ruling) is
  disclosed in the docstring and the coverage claim's wording weakened to "receipted read +
  obstruction adjudication", not "uniform procedure". On the denominator the seats split; v3
  follows CGATE's rule (no claim-level metric without a frozen denominator) and prints AGATE's
  fact verbatim (among recorded claim-level exclusion carriers 25/37/38/51/52/53/57 the screen
  flagged only 25).

**Your task:** run `python3 b41_census_coverage.py` (from this directory), read v3's docstring
and every check, and rule whether the repairs discharge YOUR seat's refutation (and whether the
other seat's repairs introduced anything false). Specifically:

1. Is the coverage claim now honestly worded for what the flags' artifacts actually support?
2. Is the entry-5 counterfactual computed correctly and stated without spin?
3. Do the per-batch verdict bindings (token + read phrase) bind what they claim to bind?
4. Any predicate that validates a string where it claims to validate a fact?
5. Final ruling: is the census closer now sound — coverage 39/39, paper-tier miss rate 1 of 2,
   precision 1 of 3, claim-level sensitivity unmeasured-with-stated-facts?

**Verdict file:** `<A|C>GATE_B41V3_VERDICT.md`, first line a single token
(`B41V3_CONFIRMED` / `B41V3_REFUTED_<REASON>` / `B41V3_NARROWED_<REASON>`).
