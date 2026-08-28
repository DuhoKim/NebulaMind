#!/usr/bin/env python3
"""A7 -- entry 22 (Easson 2026, PRD 114, 044077). GATED 2026-08-29.

    CGATE_A7_VERDICT.md   A7_CONFIRMED_TIER_ONLY
                          REACHES_E25: NO  | AUXILIARY: TIDY_STORY | PUBLISHED: YES
    AGATE_A7_VERDICT.md   A7_CONFIRMED_BOTH
                          REACHES_E25: YES | AUXILIARY: TIDY_STORY | PUBLISHED: NO

THE SEATS SPLIT ON TWO TOKENS. Recorded, and adjudicated on evidence I checked myself -- not
by vote. Both agree the tier gap is REAL and both demote my auxiliary claim to TIDY_STORY.

ONE OF MY TWO CLAIMS SURVIVED.

SUSTAINED -- the tier is a category error. CGATE: "Calling that CONSISTENCY-ONLY does not merely
coarsen its evidential strength; it misstates the kind of work the result does ... That is a real
representational gap." Entry 22 proves things cannot hold; CONSISTENCY-ONLY is defined as showing
compatibility and stating no prediction that could fail. Both halves are wrong.

REFUTED -- that Theorem 1 reaches entry 25. And it was refuted by three sentences in entry 25
that I never read, because I stopped at the one that supported me ("no defects or discontinuities
in the junction"). All three are now verified in the source by hand:

    "A null junction has degeneracies that require more elaborate consideration."
    chi_* "is not always constant"                       [i.e. NON-COMOVING]
    "the BHU (or the FLRW*) metric is not static and has a past singularity."

Easson's Theorem 1 requires a NONDEGENERATE COMOVING Darmois boundary. Entry 25's load-bearing
junction is the event horizon, which its own author calls degenerate and non-comoving. CGATE:
"'There are no surface terms' is a no-shell claim, but it cannot cure the nondegenerate/comoving
mismatch." And the flat/open branch forbids being BOTH null-complete AND ANEC-consistent -- but
entry 25 concedes a past singularity, so it never claims completeness. It is CONSISTENT with the
obstruction, not forbidden by it.

This is the same error shape as the A6 gate: I lifted a supporting phrase and did not read the
qualifications around it. Second time in two gates.

WITHDRAWN -- the auxiliary correspondence (old check 5), demoted to TIDY_STORY. Easson's extra
bulk component is an escape for the CLOSED branch; entry 25 is FLAT. Gaztanaga names no bulk
component and no redshift law. CGATE: "The two sentences can be narratively aligned, but they do
not establish identity of a technical ingredient." That is my SECOND cross-paper claim demoted in
a row (A5 PATTERN, A7 AUXILIARY). It is now a habit of mine, not two slips, and is recorded here
as one.

THE USEFUL NEGATIVE RESULT: entry 22 and entry 25 do NOT conflict. Anyone who reads both will try
this join; it fails on the junction hypothesis, and the reason is written in entry 25 itself.
"""
import re, sys, hashlib

E22 = "../bhu-reading-20260823/sources/2606.25023_clean.txt"
E25 = "../bhu-reading-20260823/sources/sym14091849_clean.txt"
C3  = "../bhu-theory-phase5-tovoptics-20260825/BHU_CLOSED_ROUTES.md"
A = " ".join(open(E22).read().split())
G = " ".join(open(E25).read().split())
R = " ".join(open(C3).read().split())
checks = []
def chk(name, pred, detail=""):
    if not isinstance(pred, bool): raise TypeError("chk needs a computed predicate")
    checks.append((name, pred, detail)); print(("PASS " if pred else "FAIL ") + name + ("  -- " + detail if detail else ""))

print("=" * 96); print("A7 [GATED] -- entry 22: tier gap SUSTAINED, cross-entry reach REFUTED"); print("=" * 96)

# ---- 1. the tier gap: test BOTH halves of the CONSISTENCY-ONLY definition ------------------
forbids = len(re.findall(r"cannot be both|cannot be|does not yield|obstruct|must give up", A))
predicts = len(re.findall(r"we predict|would be observed|detectable by|constrain(?:s|ed) by (?:current|future) (?:data|observations)", A))
print(f"\n1. THE TIER GAP  [SUSTAINED by the gate]")
print(f"   impossibility statements in entry 22 ......... {forbids}")
print(f"   observational-prediction statements .......... {predicts}")
chk("entry 22 states what CANNOT hold and makes no observational prediction -- so BOTH halves of "
    "the CONSISTENCY-ONLY definition are false of it",
    forbids >= 5 and predicts == 0,
    "the earlier version merely counted three theorem labels, which tested neither half")

# ---- 2. Proposition 1 vs what phase 5 paid for three times ---------------------------------
ks   = "the trapped interior is not an exact FRW cosmology in its natural slicing" in A
ours = "rbar is timelike" in R or "r̄ is timelike" in R
print(f"\n2. PROPOSITION 1 IS THE THEOREM FORM OF OUR OWN PHASE-5 FINDING")
print(f"   Easson states the trapped interior is Kantowski-Sachs, not FRW ..... {ks}")
print(f"   our C3 register records rbar timelike inside the horizon ........... {ours}")
chk("the published theorem and this lane's independently-derived result are both on record",
    ks and ours,
    "cross-checked against BHU_CLOSED_ROUTES.md, not asserted -- the old check searched one file")

# ---- 3. THE REFUTATION: entry 25's own text fails Theorem 1's junction hypotheses ----------
degenerate  = "A null junction has degeneracies that require more elaborate consideration" in G
noncomoving = "is not always constant" in G
noshell     = "we find no defects or discontinuities in the junction" in G
needs_nondeg = "nondegenerate comoving spherical Darmois boundary" in A
print(f"\n3. DOES THEOREM 1 REACH ENTRY 25?  ->  NO  [my claim B, refuted]")
print(f"   Theorem 1 requires a NONDEGENERATE COMOVING Darmois boundary ....... {needs_nondeg}")
print(f"   entry 25 calls its own null junction DEGENERATE .................... {degenerate}")
print(f"   entry 25's chi_* is NOT always constant (non-comoving) ............. {noncomoving}")
print(f"   entry 25 does claim no-shell -- but that cures neither of the above . {noshell}")
chk("entry 25's load-bearing junction is degenerate and non-comoving BY ITS OWN TEXT, so it "
    "falls outside Theorem 1's hypotheses",
    needs_nondeg and degenerate and noncomoving,
    "I had cited only the no-shell sentence and stopped reading; these three were on the same pages")

# ---- 4. and entry 25 never claims what the flat branch forbids -----------------------------
past_sing = "has a past singularity" in G
flat_branch = "cannot be both null geodesically complete and ANEC-consistent" in A
print(f"\n4. THE FLAT BRANCH FORBIDS COMPLETE + ANEC-CONSISTENT. DOES ENTRY 25 CLAIM THAT?")
print(f"   flat/open obstruction present in entry 22 .......................... {flat_branch}")
print(f"   entry 25: 'the BHU (or the FLRW*) metric ... has a past singularity' {past_sing}")
chk("entry 25 concedes a past singularity, so it never claims completeness -- CONSISTENT with "
    "the obstruction, not forbidden by it",
    flat_branch and past_sing,
    "my earlier version attributed an ANEC-respecting complete bounce to entry 26 in a script "
    "that never opened entry 26; CGATE caught that the hypothesis was untested")

# ---- 5. the auxiliary correspondence, demoted -- test its SPECIFICITY and watch it fail ----
easson_closed = "additional smooth bulk component" in A
easson_law    = "redshifts no faster than" in A
gaz_names_it  = ("smooth bulk component" in G) or ("redshifts no faster" in G) or ("vacuum-energy component" in G)
print(f"\n5. THE AUXILIARY CORRESPONDENCE  [WITHDRAWN -- gate says TIDY_STORY]")
print(f"   Easson names a bulk component with a redshift law ......... {easson_closed and easson_law}")
print(f"   entry 25 names that same ingredient anywhere .............. {gaz_names_it}")
print(f"   Easson's escape is for the CLOSED branch; entry 25 is FLAT. Different branch.")
chk("the two texts do NOT name the same technical ingredient -- the correspondence fails "
    "specificity and is withdrawn",
    (easson_closed and easson_law) and not gaz_names_it,
    "second cross-paper claim of mine demoted in two gates; the predicate now tests the "
    "specificity my prose assumed")

print("""
6. PUBLICATION RECEIPT -- an open item in the bibliography is now closed

   Our record carried: "VERIFIED with a stated caveat: ... the deposit is still anonymized and
   carries no volume/article number yet", pending a spot-check by Miru -- a RETIRED seat, so it
   was never going to happen.

   CGATE resolved it from APS: Damien A. Easson, "Obstructions to minimal regular black hole
   cosmologies", Physical Review D 114, 044077, published 24 August 2026, DOI 10.1103/qs86-npwk;
   received 25 June 2026, accepted 31 July 2026.

   That discharges the caveat AND corrects a date: our record lists "published online 2026-07-31",
   which is the ACCEPTANCE date. Publication was 24 August 2026.

   Still testimony, not a receipt in this corpus: a seat's APS lookup, not a pinned document.
   Recorded with that label.

7. WHAT THIS GATE ACTUALLY ESTABLISHED

   - Entry 22's tier is a category error. The record cannot express theoretical obstruction.
     Whether to add a fifth class is in OPEN_QUESTIONS_FOR_DUHO.md and is not mine to take.
   - Entry 22 does NOT constrain entry 25. Useful negative: anyone reading both will attempt this
     join, and it fails on the junction hypothesis, for reasons written in entry 25 itself.
   - Entry 22 IS published, in PRD 114, 044077.
   - Sixth entry, sixth tier unchanged.
""")
n_ok = sum(1 for _, o, _ in checks if o)
print(f"SELF-CHECKS: {n_ok}/{len(checks)} passed")
print("""
8. THE TWO SPLITS, AND WHY I SIDE WITH CGATE ON BOTH

  REACHES_E25.  AGATE says YES, arguing entry 25's junction is the TIMELIKE comoving boundary of
  its Section 2.2.1, which is nondegenerate. That describes a real junction in the paper -- but
  not the load-bearing one. The indefinite expansion Easson's theorem would obstruct comes from
  the HORIZON mechanism, Lambda = 3/r_S^2 with R -> r_S, and that junction is the one entry 25
  itself calls degenerate and non-comoving. I verified all three sentences by hand in the source
  (check 3). CGATE: "'There are no surface terms' is a no-shell claim, but it cannot cure the
  nondegenerate/comoving mismatch."

  Independently of the junction: entry 25 concedes a past singularity, so it never claims the
  null completeness the flat branch forbids (check 4). AGATE's attack-3 rebuttal attributes an
  ANEC-respecting complete bounce to ENTRY 26 -- but neither my script nor AGATE ever opened
  entry 26. AGATE inherited that claim from my brief and reasoned from it. CGATE caught it.

  PUBLISHED.  AGATE says entry 22 is an unrefereed preprint and our metadata is wrong. But our
  OWN bibliography records DOI 10.1103/qs86-npwk as Crossref-VERIFIED: "an APS Physical Review D
  journal-article of this exact title". That check was made independently and earlier, and it
  agrees with CGATE, not AGATE. CGATE adds PRD 114, 044077, published 24 August 2026, and
  resolves the date our record got wrong -- 2026-07-31 was ACCEPTANCE, not publication.
  Two independent confirmations against one dissent. Treated as PUBLISHED; the volume/article
  number remains a seat's lookup and is labelled testimony, not a receipt in this corpus.

  Both seats flagged that my check names outclaimed their predicates -- the FIFTH consecutive
  gate to do so. All five are rewritten above.
""")
print("STATUS: GATED. Tier gap SUSTAINED by both seats. Cross-entry reach REFUTED (split, "
      "adjudicated).")
sys.exit(0 if n_ok == len(checks) else 1)
