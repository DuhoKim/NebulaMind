AUDIT_HOLDS_CONSISTENCY_ONLY

# Entry 20 deep audit — claude-seat (blind; 2026-09-02 20:08 KST)

Source read: `../bhu-reading-20260823/sources/gr-qc_0611022_clean.txt` (755 lines), and nothing else. All line
numbers below refer to that file. I did not open any ENTRY20_*_RESULT file. I re-derived every equation I cite
(checks recorded inline) rather than trusting the disclosed prior findings.

## 1. The solutions — what is proved here, what is cited

**Setting.** GR + minimally coupled scalar with a *wrong-sign* kinetic term, action (3): `S = ∫√g [R − (∂φ)² − 2V(φ)]`
(l. 203–207; signature (+−−−), l. 72–73, so `−(∂φ)²` is phantom; the paper itself labels `ε = −1` "phantom" at
l. 468–470). Static spherical ansatz (1) in the quasiglobal coordinate ρ, `ds² = A dt² − dρ²/A − r²(ρ)dΩ²` (l. 68–69,
77–82), `φ = φ(ρ)`.

**Derived in this paper (checked by me):**
- Field equations (4)–(7) (l. 210–225); (7) integrates to (8) `B' ≡ (A/r²)' = 2(ρ₀ − ρ)/r⁴` (l. 230–232). I verified
  (8) from (7), and (10) from (7)+(5): with `r ≈ −aρ`, (7) gives `A = 1/a² − Ca²ρ²`, (5) gives `V = 3Ca²` — correct
  (l. 283–286).
- The asymptotic trichotomy at ρ → −∞ (l. 256–307): because (6) gives `r'' = rφ'²/2 ≥ 0` (no oscillation, l. 265–267),
  r either hits zero (a centre, no BH: l. 260–264), tends to a constant r₀ (l. 268–281, the anisotropic
  "r₀ asymptotic", metric (9)), or grows `r ~ |ρ|` (l. 282–302). In the last case C = 0 → Minkowski, C < 0 → AdS
  wormhole (no horizon possible by (8), l. 290–294), **C > 0 → de Sitter T-region = "black universe"** (l. 295–302).
- Causal structure: by (8), B has one maximum, so at most two simple zeros or one double zero — the
  Schwarzschild–de Sitter menu (l. 233–244); an asymptotically flat configuration then has exactly one simple horizon,
  hence a Schwarzschild-like Penrose diagram with r = 0 replaced by r = ∞ (l. 303–307; diagram 4b, l. 129–131,
  140–142). The theorem itself is **cited** to [26] (l. 244–245, 523–524), restated here.
- The explicit example (11)–(16): `r = √(ρ²+b²)` chosen, then B from (8), φ from (6), V from (5) — the **inverse
  problem method** (l. 308–323). I re-derived (12), (13) (`φ' = √2 b/(ρ²+b²)`), (15), the flatness condition
  `2bc = −πρ₀`, `m = ρ₀/3`, `A(0) = 1 + c`, the throat criterion `3πm ⋛ 2b` (l. 335–348), and
  `Λ₋ = V₋ = 3πρ₀/b³` (l. 562). All consistent.
- k-essence generalisation (27)–(31) (l. 496–557) and the exclusion of the perfect-fluid (24) and Chaplygin (26)
  representations (l. 566–573): derived here (short arguments, sound).

**Cited, not proved here:** the existence of "16 types of regular solutions" and the example itself are from ref. [1]
(Bronnikov & Fabris, PRL 96, 251101; l. 254–256, 308, 618–621); the Global Structure Theorem [26]; the de Sitter
attractor result (Faraoni [32], l. 365–368) — proved there for *spatially flat isotropic* cosmology and extended to
Kantowski–Sachs only as "very probably" (l. 368).

**What is *not* a theorem:** "black universes are a generic kind of solutions" (l. 375–377) rests on the potential
needing two zero-slope points (l. 355–359) plus `V₊ = 0`, `V₋ > 0` (l. 362–363, 370). The only exhibited potential is
the reconstructed (16); for the named "suitable" potentials (cos², Mexican hat, l. 360–362) no BU solution is shown.
Genericity is asserted, not measured.

**One internal slip (minor):** for the r₀ asymptotic the paper writes `V → −1/r₀²` (l. 271). With `A ≈ −ρ²/r₀²`
(l. 269, correct from (7)) eq. (5) gives `(A'r₀²)' = −2 = −2r₀²V ⇒ V = +1/r₀²` — the Nariai (dS₂ × S²) value, and
the same sign convention the paper uses when it identifies `V₋ = Λ > 0` at l. 369–372 and 562. Sign typo; it does not
touch the r → ∞ black-universe branch.

## 2. Matter — what is required, what is only cited

- **Required:** a phantom *field* (wrong-sign kinetic term, l. 204; k-essence `F_X < 0`, explicitly "the phantom
  condition", l. 529–531) with a potential having ≥ 2 zero-slope points, zero at the flat end and a positive value at
  the de Sitter end (l. 355–363, 370). No `w` enters the static solution.
- **The NEC is violated by construction, though never named:** the paper contains no occurrence of "energy condition"
  (grep). The signature is eq. (6) `r'' ≥ 0` (l. 267) — flare-out — and the paper says so in words: a black universe
  "combine[s] the properties of a wormhole (absence of a centre, a regular minimum of the area function)" (l. 580–582).
  A regular throat in a static spherically symmetric spacetime is impossible without radial-null NEC violation; here
  `T_kk ∝ −φ'²` is negative wherever `φ' ≠ 0`, and in the example `φ' = √2 b/(ρ²+b²)` never vanishes, so the violation
  is everywhere and persists through the horizon into the T region ((6) is the same equation there).
- **Observational support:** cited, not claimed. "Favoured by cosmological observations" (l. 24–25, 49) points to
  ref. [2], six 2004–05 papers (l. 622–632); "probably required for the dark energy" (l. 195–198) cites reviews
  [24, 25]. No data are used.
- **Adversarial point on the motivation:** the observational "phantom" is an effective `w < −1` fluid, and the paper's
  *own* Sec. 4.2 shows that the perfect-fluid representation (24) with `w < −1` **cannot** give a black universe
  (`X` changes sign at the horizon and `X^{(w+1)/(2w)}` "loses its meaning at X < 0", l. 566–571); the Chaplygin
  representation fails too (l. 572–573). So the specific ingredient required is a field-theoretic phantom with a
  tuned potential, not the observationally motivated fluid. The abstract's "various (but not all)" (l. 23–24) and
  "many, though not all" (l. 574) are the honest hedges.
- **Instability:** one sentence (l. 53–58): the "obvious quantum instability" is deferred to an effective-theory
  reading [6], and classical stability is asserted for a *massless* phantom [7, 8] — the BU solutions require a
  potential, so that result does not cover them. No perturbative stability analysis of any black-universe solution is
  performed (contrast type 3, where stability is at least cited, l. 184–186).

## 3. "Our Universe originated from phantom-dominated collapse in another universe"

**Status: a suggestion, not a derivation.** Abstract: "It also looks possible" (l. 25–27). Conclusion: the solutions
"lead to the idea that our Universe could appear from phantom-dominated collapse in another, 'mother' universe"
(l. 592–594); "if certainly amended by adding realistic matter ingredients [it] may even lead to viable
alternatives" (l. 609–611).

- **No collapse is modelled.** Every solution is static/eternal (Killing horizon with analytic extension,
  l. 86–91); the Penrose diagram 4b is the eternal one with de Sitter infinities on both horizontals (l. 140–142).
  "Collapse" appears only in the abstract and conclusion (l. 26, 593).
- **No matching to an FRW late universe, no parameters.** No H₀, no Ω's, no redshift of any transition, no
  matter/radiation era — the interior is pure phantom scalar + Λ.
- **Isotropisation** is asserted, not derived: "gradually isotropizing" (l. 299–300), with the regime "depend[ing]
  on the choice of V" (l. 300–302); the attractor is Faraoni's flat-isotropic result extended "very probably"
  (l. 365–368); in STT "izotropization must take place" (l. 444) is stated without argument; the conclusion invokes
  particle creation (l. 594), which is not in the action. The r₀ branch is a permanent counter-example the paper
  itself describes: "highly anisotropic … no expansion in the two angular directions" (l. 277–279), and nothing in
  the paper selects the dS branch over it except the choice of V.
- **Observables stated for an interior observer:** (a) the late-time expansion rate is `Λ_eff = V₋ > 0`, set by the
  potential value, "rather than by … the Schwarzschild mass" (l. 369–374); in the example `Λ₋ = 3πρ₀/b³ = 9πm/b³`
  (l. 562 with l. 336) — a formula in parent-universe parameters, never evaluated, never compared with our Λ;
  (b) anisotropy: a Kantowski–Sachs universe is "not excluded observationally [34] if its isotropization had happened
  … before the last scattering epoch (z ≳ 1000)" (l. 595–597) — a *consistency* condition imported from [34], with
  no magnitude or axis predicted; (c) no curvature statement for the interior observer is made.

## 4. Easson map (entry 22, Proposition 2) — report only

Read on the brief's statement of Prop. 2 (I could not read entry 22): daughters that are nondegenerate, comoving,
no-shell, **closed-FRW**, inside static asymptotically-flat finite-ADM parents; a flat/open limb requiring curvature
regularity, regular affine ends, and **ANEC**.

**Parent side — hypotheses match.** The black universe's exterior is static, asymptotically flat (`A → 1`, `r ≈ ρ`,
l. 95, 257), with finite ADM mass `m = ρ₀/3 > 0` (l. 335–336, 341); the daughter is "comoving/no-shell" in the
strongest sense — it is the analytic continuation across the Killing horizon, no thin shell, no matching surface
(l. 86–91, 303–307).

**Daughter side — two hypotheses fail, each by construction:**

(i) *Geometry.* The interior is Kantowski–Sachs (R × S², homogeneous, anisotropic; l. 99–101, 274–281, 300), not
closed FRW (S³). It is anisotropic at every finite interior time and only *tends* to de Sitter (l. 295–302). Prop. 2's
"closed-FRW daughter" premise is therefore not met, and the isotropic limit — de Sitter — is degenerate in the sense
that it can be foliated as closed, flat or open FRW, so no unique FRW class is picked out even asymptotically.

(ii) *Energy condition.* ANEC fails on every complete radial null geodesic: the phantom field makes `T_kk ∝ −φ'² ≤ 0`
pointwise (from (6), l. 218–220, 267), strictly negative wherever `φ' ≠ 0` — everywhere in the example (φ' never
vanishes, l. 316–318) — so the average is negative, not merely non-positive. This is not incidental: the paper
proves that the throat/flare-out needs `F_X < 0` ("phantom condition", l. 529–531) and describes the object as
wormhole-plus-horizon (l. 580–582). With a normal field (6) flips to `r'' ≤ 0`, r reaches zero and no black universe
exists at all (l. 258–264 read with the sign reversed). So the ANEC premise of Prop. 2 is violated by the very
mechanism that makes the solution exist.

**Verdict of the map: Prop. 2 is INAPPLICABLE to entry 20 — it neither kills nor restricts it, and it does not
"spare" it in any vindicating sense.** The precise statement: entry 20 lives entirely outside Prop. 2's hypothesis
space, on the NEC-violating side. If entry 22's proposition is read contrapositively ("a nondegenerate no-shell
daughter of a static finite-ADM parent must violate ANEC or fail regularity"), then entry 20 is a *worked instance of
the contrapositive*, not a counter-example: it buys nondegeneracy and regularity with ANEC violation everywhere, and
the paper concedes the price (l. 53–58). Two cautions for whoever writes the map: (a) since the daughter is KS not
FRW, even a hypothetical ANEC-respecting Bronnikov-type interior would fall outside Prop. 2 as stated, so the
"kills/restricts/spares" trichotomy needs a fourth box, "off-hypothesis"; (b) the obstruction that *does* bind
entry 20 is internal — the Global Structure Theorem (l. 233–253, 303–307) forbids a regular centre and allows only
one simple horizon for any potential, phantom or not — and that is a restriction on *shape*, not on existence.

## 5. Tier consequence, argued

**CONSISTENCY-ONLY holds.** Arguments against each alternative:

- *CALIBRATED-FALSIFIER:* nothing is calibrated. The one interior quantity, `Λ_eff = V₋ = 9πm/b³` (l. 369–374, 562),
  is a free potential value in parent-universe parameters; the paper never evaluates it or compares it to anything.
  No number is missing that the lane could own — the *definition* of the observable is missing.
- *QUALITATIVE-DIRECTIONAL:* the only sign-type statements are (a) `Λ_eff > 0` and (b) "we may be a Kantowski–Sachs
  universe that isotropised before z ≳ 1000". (a) is not a risky prediction: `C > 0` / `V₋ > 0` is the *selection
  criterion* that distinguishes the black-universe branch from the AdS-wormhole branch (l. 287–296, 339–342), i.e.
  it is what "black universe" means, and positive Λ was the paper's input motivation (l. 193–198), not its output;
  moreover in the STT Jordan frame the de Sitter asymptotic "is not necessarily preserved" (l. 441–443), so the sign
  is not even robust across the paper's own generalisation. (b) is written as "not excluded … if" (l. 595–597) — a
  compatibility clause borrowed from [34], with no axis, magnitude or direction of anisotropy predicted. Neither
  reaches the QUAL-DIR bar that entry 54 sets (a sign that could have come out the other way).
- *PROSPECT:* the paper proposes no test, no observable to look for, and no route to one; the cosmological reading
  is "the idea" (l. 592) and "may even lead to viable alternatives" once "amended by adding realistic matter
  ingredients" (l. 609–611).

**Tier-adjacent note for Duho (packet, not a tier change):** the `Λ_eff > 0` implication is the only item a
dissenting seat could push toward QUAL-DIR. I argue it is a class definition rather than a prediction; if the lane's
rule is that *any* sign implication counts, this entry would be the borderline case and should be ruled explicitly.
Separately, the paper's viability is hostage to the observational status of a field-theoretic phantom (its
motivation at l. 24–25, 49, 193–198 is a 2004–05 `w < −1` consensus), and its own Sec. 4.2 shows the fluid version
of that consensus does not even support the solution.

## Plain language

This paper shows, with correct algebra, that if you allow a "phantom" field — matter with negative kinetic energy,
which breaks the usual energy rules on purpose — then Einstein's equations admit black holes whose inside is not a
crushing singularity but an expanding, initially lopsided universe that settles toward a de Sitter state. That part
is solid mathematics, mostly built on the authors' earlier PRL and their own structure theorem. The step from there
to "our universe was born this way" is explicitly offered as an idea, not a result: nothing collapses in the model,
nothing is matched to our universe, no number is predicted, and the smoothing-out of the lopsidedness is assumed
rather than shown. On the Easson question, the interior is not the kind of universe Easson's proposition talks about
(it is Kantowski–Sachs, not closed FRW) and it violates the energy condition his proposition assumes — not by
accident but as the very thing that makes the solution exist — so the proposition simply does not reach it; entry 20
is best read as an example of what one has to give up to get a regular black-hole interior at all. The tier stays
CONSISTENCY-ONLY.
