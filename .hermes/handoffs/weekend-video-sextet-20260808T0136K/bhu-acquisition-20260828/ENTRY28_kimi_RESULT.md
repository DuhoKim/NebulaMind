AUDIT_HOLDS_CONSISTENCY_ONLY

Entry 28 — Sahu & Van Raamsdonk (2025), "Holographic black hole cosmologies," arXiv 2411.14673.
Blind independent read by kimi seat, 2026-09-02, of pinned source ../bhu-reading-20260823/sources/2411.14673_clean.txt
(619 lines in file; brief said 620 — off by one, content complete through references). No other ENTRY28_*_RESULT or
codex-named file was opened. All line receipts below refer to the pinned source.

1. The construction — what is derived vs quoted.

Derived in the paper (3D gravity, Λ<0, section 3):
- Scale factor a(t) = cos(t/ℓ_AdS). Stated line 42 ("In the solutions, the scale factor is always a(t)=cos(t/ℓ_AdS)")
  and derived from the metric ansatz eq (3), line 72: ds² = −dt² + cos²(t/ℓ) dΣ², which follows because in 3D
  gravity with Λ<0 "the spacetime geometry is locally AdS3 in the absence of matter" and the Z2 time-reversal
  symmetry fixes the t-dependence (line 71). This is derived, not quoted.
- Volume per black hole V/ℓ² = 2p(π/2 − π/q). Eq (5), lines 86–89, derived in-paper from the Gauss–Bonnet /
  angle-deficit formula for hyperbolic polygons: "the area of an n-sided polygon in hyperbolic space is equal to
  ℓ²_AdS times the amount by which the sum of the interior angles is less than (n−2)π" (line 89). Derived.
- Critical spacing. Intro gives D_crit ≈ 1.3 ℓ_AdS (line 35); the detailed section 4.4 gives the sharper numbers:
  in the infinite-lattice limit the cosmological saddle dominates for horizon length R > R∞^crit ≈ 7.06 ℓ
  (line 350), i.e. horizon radius r_crit = R_crit/(2π) ≈ 1.12 ℓ_AdS and critical separation d_crit ≈ 1.2 ℓ_AdS
  (line 351). These are derived by a numerical action comparison (Handlebodies.m, lines 207, 222, 233) between
  Schottky-construction saddles, cross-checked against Maxfield–Ross–Way's phase diagram (line 238: "we find
  parameter values for this transition in agreement with those in that figure"). Note the intro/body rounding
  discrepancy (1.3 vs 1.2 ℓ_AdS) — cosmetic, not substantive.
- The dominance condition, exactly: with saddles 1 (cosmological), 2, 3 the three symmetry-preserving candidates,
  the cosmological saddle dominates iff eq (9), lines 147–149, is negative:
  S^(1)_{n,n} − S^(2)_{n,n} = n²[(S^(1)_{1,1} − S^(2)_{1,1}) + (S^(2)_{1,1} − (1/n)S^(2)_{1,n})] < 0.
  The ensemble over which dominance is assessed is NOT a statistical ensemble of universes; it is the gravitational
  path integral for a fixed boundary geometry (the genus-(mn+1) "two tori joined by an m×n lattice of tubes"
  surface, lines 122, 125), restricted to the "three saddles that preserve the lattice symmetry and are the most
  plausible candidates for the least action saddle at each β" (line 46). Plainly: the cosmology dominates the
  wavefunction when its black holes are sufficiently large and close together (abstract, line 10).

Quoted from MMV / Maldacena–Maoz (not re-derived here):
- The heavy-particle dust picture and the ensemble-of-operator-insertions idea (line 18: "a specific simple model
  of cosmology where the matter is an approximately uniform distribution of heavy particles ... MMV"; line 20).
- The O(c) mutual-information / large-entropy requirement for wormhole dominance: "We briefly review an argument
  from MMV" (line 22).
- The no-back-reaction result and the mass density ρ_M = M/A = 1/(8πGℓ²_AdS) feeding the 3D Friedmann equation
  eq (36): "described in more detail in MMV ... Thus, there are no 'back-reaction' effects due to the
  inhomogeneity MMV" (lines 360–363).
- The Euclidean-wormhole-to-cosmology analytic continuation template: Maldacena–Maoz 2004 (lines 14, 49).

2. Dimension and sign — any carry-over to 4D or Λ>0?

Everything quantitative is three-dimensional gravity with negative Λ (line 70: "a two-dimensional holographic CFT
and a three-dimensional bulk geometry"; line 71: "Einstein equations with negative cosmological constant").
Carry-over claims are explicitly hedged and qualitative only:
- "Negative Λ gravitational effective field theories associated with holographic CFTs have interesting and
  potentially realistic cosmological solutions with zero, positive, or negative spatial curvature" (line 13) —
  "potentially realistic" modifies Λ<0 EFT cosmologies generally; it is not a claim about our Λ>0 universe.
- "While our explicit calculations have been in three-dimensional gravity, we expect that the general picture
  should be qualitatively the same in higher-dimensions" (line 356) — expectation, argued only by analogy to the
  thermofield double / Hawking–Page case, with higher-D constructions left to numerics.
There is NO claim or argument anywhere in the paper for Λ>0. The "realistic cosmology" on offer is a Λ<0,
dust-filled (black-hole-lattice), time-reflection-symmetric big-bang/big-crunch universe that recollapses —
a(t)=cos(t/ℓ_AdS) has a bang at t=−πℓ/2 and a crunch at t=+πℓ/2. The paper says nothing about matching an
accelerating universe; the only gesture toward our universe is the subdominant-saddle remark: "It may be
worthwhile to keep in mind that our own universe might be a rare part of some, e.g. for anthropic reasons"
(line 38), and the discussion that small-black-hole cosmologies "as in our own universe ... will only arise from
the contributions of a subdominant saddle and thus will be a rare part of the wavefunction in our construction"
(line 355). No acceleration mechanism is proposed.

3. Observables.

None that an observation in our universe could contradict. Every number is an AdS-scale quantity inside the 3D
construction: r_crit ≈ 1.12 ℓ_AdS (line 351), d_crit ≈ 1.2 ℓ_AdS (line 351), R > 22.341 ℓ for the single-black-hole
toroidal case (lines 239, 344), action at the transition −1.2133 c with c = 3ℓ_AdS/2G (line 237), V/ℓ² formula
(eq 5). There is no predicted curvature sign for our universe (all three spatial-curvature cases are constructed,
lines 94–107), no recollapse time applicable to us, no entropy bound on our universe, no CMB statement. The paper
itself flags the mismatch direction: in its dominant regime "the black hole size is always at least of order the
cosmological scale" (line 35) and the spacetimes are "quite inhomogeneous at the scale of the lattice" (line 354),
whereas our universe has black holes far smaller than the cosmological scale (line 355) — so our universe sits in
the regime the construction explicitly assigns to subdominant saddles.

4. The BHU relation.

This is NOT "our universe inside a black hole" in the corpus sense (an interior cosmology behind the horizon of a
parent black hole). It is the inverse aggregation: a cosmology built OUT OF many black holes' interiors as a
holographic state of many CFTs. The paper's own words: "the cosmology is the interior geometry of a multi-boundary
Lorentzian wormhole" (line 31); "from the interior perspective, we have a connected geometry with n black holes
... we can think of it as a big-bang / big-crunch cosmology where the matter is n black holes" (lines 66–68); the
dual is "an entangled state of a collection of CFTs associated with the second asymptotic regions of the black
holes" (line 29; also line 10). The black holes are the matter content of the cosmology, each with a second
asymptotic region that purifies the cosmological state; no parent universe, no parent horizon containing the
cosmology. The bibliography branch label "holographic interior cosmology" is accurate and should be retained; the
relevant sense of "interior" is "interior of the multi-boundary wormhole," not "interior of one parent BH."

5. Tier consequence, argued.

AUDIT_HOLDS_CONSISTENCY_ONLY. The disclosed prior findings re-derive cleanly: this is a microscopic construction,
not an obstruction, and its one quantitative result is a dominance condition on its own saddle within its own
path-integral ensemble (axis settled — confirmed independently above, item 1). For tier: the paper derives real,
checkable mathematics (exact 3D solutions, eqs 3–5; numerical action comparison, eqs 9, 25, 35), but (a) all of it
lives in 3D Λ<0 gravity with only an explicitly qualitative higher-D expectation (line 356); (b) no Λ>0 statement
is made at all; (c) no quantity in the paper is one an observation of our universe could confirm or contradict —
by the construction's own dominance condition, our-universe-like parameters lie in the subdominant branch
(lines 35, 354–355). CONSISTENCY-ONLY is the correct tier: the work is consistent with, and structurally adjacent
to, BHU-flavored ideas, but it constrains nothing about our universe and our universe constrains nothing about it.
It is not QUALITITATIVE-DIRECTIONAL (no direction claimed for our cosmos), not PROSPECT (no observable proposed,
even in principle, for our universe), not CALIBRATED-FALSIFIER (no threshold observable). Nothing here is a
missing threshold the lane could own; the gap is a missing dimension/sign bridge the authors themselves decline
to build. No tier change; no packet needed.

Plain-language paragraph.

Sahu and Van Raamsdonk build an explicit toy universe: take three-dimensional gravity with a negative cosmological
constant, fill it with a regular lattice of black holes, and you get an exact big-bang/big-crunch cosmology whose
scale factor is just a cosine of time. Holographically, this universe is dual to a particular entangled state of
many ordinary quantum field theories, one for each black hole's second asymptotic region, and the paper's real
technical work is showing numerically when this "cosmology" saddle beats its rivals in the gravitational path
integral: when the black holes are big and packed close together, each roughly the size of the whole observable
space. That is exactly the opposite of our universe, where black holes are specks compared to the cosmos — the
authors say so themselves and file our-universe-like cases under "rare, subdominant" contributions. Everything is
in 3D with negative Λ; the only reach toward 4D is a sentence saying the picture should be "qualitatively the
same," and nothing is said about positive Λ or acceleration at all. So the paper neither supports nor threatens
"our universe inside a black hole": it is a many-black-holes-make-a-cosmology construction, mathematically solid
inside its sandbox, with zero contact with anything we could measure. CONSISTENCY-ONLY stands.
