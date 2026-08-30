Q7_IMPL_REFUTED_THRESHOLD_CONFLATION

# Question-7 implementation verdict

The selected disposition—entries 52 and 53 remain `CONSISTENCY-ONLY`, with their theorems preserved claim-level—is not changed by this implementation audit. But the ruling's stated factual premise is false. It conflates two different thresholds: the small threshold required for a dynamical closed-universe solution to exist, and the vastly larger late-time threshold required to remove the recollapse turning point so dark energy can eventually dominate. The papers' “another cycle” language concerns only the second. It does not narrow or contradict the first no-solution theorem.

I read both pinned papers through their complete argument and closing sections:

- entry 52: Unger and Popławski, *Big Bounce and Closed Universe from Spin and Torsion*, `1808.08327_clean.txt`;
- entry 53: Cubero and Popławski, *Analysis of big bounce in Einstein–Cartan cosmology*, `1906.11824_clean.txt`.

## 1. What the closings actually say

The alternatives in attack 1 are not mutually exclusive: both papers close as constructive cosmological scenarios **and** highlight the closed-universe existence exclusion.

Entry 52 has no separately titled “Conclusions” section. Its final substantive paragraphs, after the cosmological-constant analysis, say all of the following:

1. formation of “our Universe” occurs when `C` begins to satisfy inequality (33);
2. inflation must raise `C` to threshold (51) for observed late acceleration;
3. if “this threshold” is not reached, the already-formed closed universe contracts to another bounce and begins another cycle; and
4. the last bounce before reaching that threshold can be regarded as the Big Bang.

Grammatically and mathematically, “this threshold” in item 3 refers to (51), named in the immediately preceding sentence—not to (33). The closing therefore contains both the existence entry condition and the later cyclic scenario.

Entry 53 has an explicit **Conclusions** section. It prominently restates the exclusion:

> a closed universe may exist only when some function of the scale factor and temperature is higher than a particular threshold.

It then writes that condition explicitly as equation (31), derived from equation (18) and inequality (24), and says formation occurs when `C` begins to satisfy (24). Only afterward does it discuss a second, unspecified threshold large enough for dark-energy acceleration; failure to reach **that** threshold leads to repeated temperature/double-scale-factor bounces.

Thus `CGATE_B37_VERDICT.md` was correct that the existence exclusion is highlighted in both abstracts and in entry 53's conclusion. Entry 52's untitled closing also explicitly names inequality (33), although its final rhetorical emphasis is the black-hole/cyclic-universe construction. Q7's statement that “the conclusions ... decide it the other way” is an overreading: the closings support construction-level framing but do not demote or contradict the existence theorem.

The quotation in the Q7 closure is also mishandled. It splices entry 52's two thresholds into one and then says “entry 53 closes the same way.” Entry 53 closes analogously at a qualitative level, but it does not derive or number entry 52's late-time inequality (51); its conclusion merely cites earlier work for that later threshold.

## 2. What each inequality bounds

### Entry 52: inequalities (22)/(23)/(33) and equation (24)

For the ultrarelativistic spin fluid, entry 52 defines

`x = T/T_cr`, `y = a/a_cr`, and, from adiabatic evolution, `xy = C`.

For `k=1`, its Friedmann equation becomes

`dot(y)^2 + 1 = 3 C^4/y^2 - 2 C^6/y^4`.

Turning points obey `dot(y)=0`, hence

`y^4 - 3 C^4 y^2 + 2 C^6 = 0`.

The two roots are real only if

`9 C^8 - 8 C^6 >= 0`,

which, since `C>0`, gives

`C >= sqrt(8/9)`.

This is equation (22), equivalently equation (23), `aT >= sqrt(8/9) a_cr T_cr`. At equality the two turning points coalesce and the solution is stationary. For a genuinely expanding/contracting closed universe the paper therefore uses the strict condition

`C > sqrt(8/9)` — inequality (33).

Equation (24) is not itself a separate inequality. It is the explicit pair of turning radii `y_±(C)` for `C>sqrt(8/9)`. Its square root encodes the same discriminant condition.

**What (33) bounds:** the existence of a nonstationary homogeneous, isotropic, ultrarelativistic **closed (`k=1`) EC Friedmann trajectory** with the paper's spin-fluid equation and constant adiabatic `C=xy`. Below it, the turning-point roots are not real and the paper supplies no allowed closed dynamical solution; at equality the universe is stationary; above it the solution oscillates between a bounce and a crunch. Flat and open cases have solutions for every `C>0`.

It does not say “below (33), an existing closed universe cycles.” Cycling is the above-(33) solution's ordinary behavior before a later condition removes recollapse.

### Entry 53: inequality (24)

Entry 53 uses the Dirac-field effective pressure, so its thermodynamic relation differs. It derives

`y(x) = (C/x) exp(x^2/2)`,

and therefore

`C = x y exp(-x^2/2)`.

For `k=1`, a turning point must satisfy

`(3x^2 - 2x^4) exp(x^2) = 1/C^2`.

The left side has maximum `e` at `x=1`. Two turning points exist only when the horizontal line `1/C^2` lies below that maximum:

`C > e^(-1/2)` — inequality (24).

At equality there is one stationary turning point at `x=1`. Below it there are no turning points, and the paper expressly says “the universe would not exist.” In the conclusion, equation (31) expresses the same condition in physical variables:

`x y exp(-x^2/2) > e^(-1/2)`.

**What (24) bounds:** the existence of a nonstationary homogeneous, isotropic, closed EC solution in entry 53's Dirac-field thermodynamic model. It is not a bound merely on whether dark energy begins or whether an already-existing universe avoids another cycle.

### Entry 52: inequality (51)

Entry 52 next adds a positive cosmological constant. After the radiation-to-matter transition it approximates the late Friedmann equation by

`dot(y)^2 + 1 = B/y + lambda y^2`,

with `B = 3 C^3 x_eq^3`.

Late turning points solve

`y^3 - y/lambda + B/lambda = 0`.

The paper states that this cubic has no positive real turning point when

`B > 2/(3 sqrt(3 lambda))`.

Substituting `B=3C^3 x_eq^3` yields inequality (51):

`C > [2/(9 sqrt(3 lambda))]^(1/3) / x_eq = 1.9×10^48`.

**What (51) bounds:** absence of a late-time positive turning point in the matter-dominated closed-universe approximation. If it is satisfied, the closed universe does not recollapse, expands without bound, and the cosmological-constant term can dominate, producing the late acceleration. If (33) is satisfied but (51) is not, a closed universe exists but reaches a maximum size, contracts, bounces, and can begin another cycle; particle production may change `C` between cycles.

Accordingly, the logically correct regimes for entry 52 are:

| `C` regime | result in the paper |
|---|---|
| `0 < C < sqrt(8/9)` | no nonstationary closed-universe solution under the stated early-universe equations |
| `C = sqrt(8/9)` | stationary closed solution |
| `sqrt(8/9) < C <= 1.9×10^48` | dynamical closed solution exists and recollapses/cycles in the stated scenario |
| `C > 1.9×10^48` | no late positive turning point; expansion to infinity and eventual dark-energy domination |

The numerical upper boundary belongs to the paper's specified late-time approximations and adopted `lambda`, `T_eq`, and particle content; it is not a universal EC constant.

### Reconciliation with the abstracts

There is no contradiction. “A closed universe exists only when `C` exceeds a threshold” refers to (33) in entry 52 and (24) in entry 53. “Otherwise it undergoes another cycle” refers to failure to reach the later dark-energy/no-recollapse threshold—equation (51) in entry 52 and a qualitatively cited counterpart in entry 53—after the existence condition has already been met.

`CGATE_B37`'s sentence “below a derived threshold, no dynamical closed-universe solution exists” is correct when “a derived threshold” means (33)/(24). It would be too strong only if applied to values below (51), which B37 did not do.

## 3. Does entry 37 control?

Entry 37 is a relevant paper-level convention but not a factual twin.

Its theorem first constructs a family of exact FRW/TOV shock solutions and then partitions that existing family by a physical property: the shock is everywhere subluminal iff `sigma<=1/3`. For `sigma>1/3`, the mathematical shock solution still exists; it fails the desired subluminality conjunction. The theorem characterizes the physical domain of an already-constructed family.

Entries 52/53 instead derive whether a nonstationary **closed solution exists at all** for their respective `C`. Their existence threshold is:

- stated in each title-program/abstract introduction;
- a central correction to prior work that had effectively set `k=0`;
- given a dedicated turning-point analysis;
- restated in entry 53's formal conclusion and in entry 52's formation scenario.

That is a principled difference and makes the analogy weaker than Q7 admits. It does not force a tier change here because Duho's Q7 disposition is already fixed, and the operative-contribution test can still choose the overall bounce/cyclic-universe construction. But the implementation should say this is a **new application** of the paper-level convention despite a stronger, formation-level exclusion—not assert that entry 37 straightforwardly decides the case.

The statement that “both reviewers refused promotion” for entry 37 is accurate at B30. It does not establish that both reviewers would or did endorse applying the same result to an existence threshold of this different centrality.

## 4. Stale and broken implementation state

The headline counts remain arithmetically unchanged because Q7 retained both tiers: 32 `CONSISTENCY-ONLY`, one `THEORETICAL-OBSTRUCTION`, and 51 BHU papers overall under the current record.

Question 7 is correctly marked closed, and entries 52/53 point to it. The implementation nevertheless leaves several factual defects:

1. Both bibliography entries say below “the threshold” the universe cycles, without distinguishing (33)/(24) from (51). This is false as written.
2. Both carry “One refinement pending the implementation gate,” which this gate resolves and which should be removed.
3. Entry 53 is made to quote entry 52's equation (33) and closing almost as if it were its own. Its actual threshold is (24)/(31), and its dark-energy threshold is not derived there.
4. The Q7 closure says the conclusions “decide it the other way,” although entry 53's conclusion explicitly foregrounds the existence theorem.
5. The original-question details still contain the stale Q6 claim that question 3 established “when a paper carries a calibrated falsifier, that tier leads,” already refuted by `CGATE_Q6_VERDICT.md`. That history can remain, but it must be marked as superseded rather than silently presented as a valid premise.

## Required implementation correction

Keep the selected tiers, but replace the conflated prose with a two-threshold account:

> **Claim-level existence theorem:** In entry 52's adiabatic spin-fluid model a dynamical closed universe requires `C=xy>sqrt(8/9)` (equality stationary); in entry 53's Dirac-field thermodynamics it requires `C=xy exp(-x^2/2)>e^-1/2` (equality stationary). Below those bounds the respective papers have no dynamical closed solution; flat/open solutions remain unrestricted. **Separate late-time condition:** entry 52's Eq. (51), `C>1.9×10^48` under its matter-era and cosmological-constant inputs, eliminates the late recollapse turning point. A closed solution above the existence threshold but below Eq. (51) can cycle. Entry 53 cites an analogous later threshold but does not derive Eq. (51).

Then state the Q7 paper-level ruling separately: despite those central claim-level existence exclusions, the adopted operative-contribution judgment retains the papers as constructive EC bounce/cyclic-universe analyses.

As written, the implementation's load-bearing refinement reverses the referent of “this threshold” and materially weakens the theorem. It must be corrected.
