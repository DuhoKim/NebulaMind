ARITH_NARROWED_NONEXHAUSTIVE_APPROXIMATION

# Adversarial verdict

## 1. Independent numerical reconstruction

I recomputed the quantities independently using

\(G=6.67430\times10^{-11}\,\mathrm{m^3\,kg^{-1}\,s^{-2}}\),
\(c=2.99792458\times10^8\,\mathrm{m\,s^{-1}}\),
\(\hbar=1.054571817\times10^{-34}\,\mathrm{J\,s}\), and
\(m_e=9.1093837015\times10^{-31}\,\mathrm{kg}\).

All of B13's displayed arithmetic reproduces:

- Solving equation (33) as an equality gives
  \[
  r_{Ce}=\left(\frac{G\hbar^2}{c^4m_e}\right)^{1/3}
  =4.655097118\times10^{-28}\,\mathrm m.
  \]
- Then
  \[
  \rho_{Ce}=\frac{m_e}{r_{Ce}^3}
  =9.030312044\times10^{51}\,\mathrm{kg\,m^{-3}},
  \]
  which is 9.0303 times the printed rounded \(10^{51}\) value.
- Schwarzschild mean density, \(3c^6/(32\pi G^3M^2)\):
  - at \(10^{51}\,\mathrm{kg\,m^{-3}}\), \(M=2.699381239\times10^{14}\,\mathrm{kg}\), with target ratio 37.0455;
  - at the equation-(33) density, \(M=8.982823083\times10^{13}\,\mathrm{kg}\), with target ratio 111.3236.
- With geometry dropped, \(\rho=M/r_s^3=c^6/(8G^3M^2)\):
  - at the quoted density, \(M=5.524697833\times10^{14}\,\mathrm{kg}\), with target ratio 18.1005 (1.2577 decades);
  - at the equation-(33) density, \(M=1.838472555\times10^{14}\,\mathrm{kg}\), with target ratio 54.3930.
- Setting \(r_s=r_{Ce}\) gives
  \[
  M=\frac{r_{Ce}c^2}{2G}=0.313425576\,\mathrm{kg},
  \]
  a target ratio of \(3.19055\times10^{16}\).
- Under the Schwarzschild mean-density convention, a \(10^{16}\,\mathrm{kg}\) floor requires
  \[
  \rho=7.286659073\times10^{47}\,\mathrm{kg\,m^{-3}}.
  \]
  The printed density is 1372.371 times higher, or 3.1375 decades; the equation-(33) density is 12392.939 times higher, or 4.0932 decades.
- The equation-(33)/mean-density candidate is \(8.982823083\times10^{16}\,\mathrm g\), which is below \(10^{17}\,\mathrm g\) by a factor 1.11324, or only 0.0467 decade.

Thus claims 1, 3, and 4 are arithmetically correct. Claim 2's five row values, nearest-row selection, factor 18, and 1.26-decade statement are also correct. The script ran 5/5 with exit 0.

## 2. Reading equation (33)

The algebra is correct. The source says the metric energy-momentum and spin-density terms are “on the order” of the displayed expressions, says the size is “on the order” of the Cartan radius, and uses \(\sim\) in equation (33). Rearranging that relation produces B13's expression for \(r_C\). In the electron application, \(m\) is indeed the electron mass: the preceding derivation uses the mass \(m\) of the spinor particle, and the next sentence explicitly specializes to an electron.

However, B13 is not entitled to call the resulting density “exact” in a physical or source-faithful sense. Treating \(\sim\) as equality is legitimate for constructing one normalized candidate and checking direction under that normalization. It does not recover omitted numerical coefficients in the energy-momentum term, spin term, wave-function normalization, effective particle volume, or balance condition. Cubing the radius makes even modest hidden radius coefficients important for density. The value \(9.0303\times10^{51}\) is exact only relative to B13's imposed unit coefficient and selected constants.

The fact that \(4.655\times10^{-28}\,\mathrm m\) is within a factor 2.15 of \(10^{-27}\,\mathrm m\) supports order-of-magnitude consistency. It does not license “full precision.”

## 3. The five routes are not exhaustive

The script tries four variants of a Schwarzschild-radius density and one horizon-equals-Cartan-radius condition. That is a useful sensitivity table, not “EVERY route from a density to a minimum black-hole mass.” Its own prose concedes possible proper-density and non-Schwarzschild routes.

At least these source-admitted choices are omitted:

- A rotating/charged Kerr-Newman geometry. The paper discusses Kerr-Newman objects extensively; its horizon/volume scale is not generally the Schwarzschild \(2GM/c^2\).
- A density defined for the collapsing fermionic matter in its local rest frame rather than average ADM mass divided by Euclidean volume inside an exterior-coordinate horizon.
- A full nonsingular ECKS interior or toroidal/shell configuration. The paper explicitly says the full coupled field equations would have to be solved for the proposed structure.
- Unknown order-unity—or larger—coefficients suppressed in equation (33) and in the passage from component density to a system-wide maximum density.

The simple extremal Kerr replacement alone does not recover \(10^{16}\,\mathrm{kg}\): using \(r_+=GM/c^2\) multiplies the Schwarzschild mean-density mass by \(2^{3/2}\), giving about \(7.64\times10^{14}\,\mathrm{kg}\) from the quoted density and \(2.54\times10^{14}\,\mathrm{kg}\) from B13's normalized density. I found no explicit route in the pinned paper that reaches \(10^{16}\,\mathrm{kg}\). But because local proper density and a nonsingular ECKS interior are not specified, I also cannot prove that no admitted route or suppressed coefficient can reach it. B13's finite enumeration cannot bear that universal conclusion.

## 4. Consequence for the PBH window

Conditional on all three choices—unit coefficient in equation (33), Schwarzschild mean density, and the fixed Carr et al. lower endpoint—the arithmetic is correct: \(8.9828\times10^{16}\,\mathrm g<10^{17}\,\mathrm g\), so the intersection of the proposed forbidden interval with that review window is empty.

The PBH-window endpoint does not mathematically “move” when the Cartan-density normalization changes; it is an independent observational summary. But it is itself approximate and caveated, while the candidate floor is only 11.3% (0.0467 decade) below it. Therefore claim 5 is a valid conditional scenario, not a robust removal of the route. An omitted coefficient of only 1.24 in the density-to-mass relation, or about 1.07 in the effective radius, reverses the ordering. The appropriate conclusion is that this normalization supplies a third candidate under which no in-window band exists—not that it establishes the route's nonexistence.

## 5. Predicate audit

Several check names/details claim more than their predicates establish:

- Check 1 tests only that the computed radius lies within half a decade of \(10^{-27}\,\mathrm m\) and that the source contains that text. It does not establish internal consistency at full precision or justify using an order relation at full precision.
- Check 2 tests only the five hard-coded rows. It cannot establish “NO route built from the paper's own quantities” or that the gap is not caused by a route omitted from the list.
- Check 3 correctly tests the direction of the two selected mean-density computations. Its detail overreaches by saying rounding as an explanation is “ruled out”: only replacement of the rounded density by the unit-coefficient equation-(33) normalization is ruled out as a cure.
- Check 4 tests only whether one selected density ratio exceeds three decades. It does not test what the hedging language “conventionally covers,” and that interpretive claim is outside arithmetic.
- Check 5 correctly tests the numerical ordering for the selected normalization and fixed endpoint. Its name calls the density “exact” and says the candidate “removes” the band without encoding the approximation and endpoint caveats.

## Bottom line

The numerical table is correct and usefully shows that the unit-coefficient equation-(33) normalization worsens the discrepancy under the selected Schwarzschild conventions. The result must be narrowed because equation (33) is not an exact definition, the route list is demonstrably nonexhaustive, and the claimed disappearance of the PBH band rests on an ordering separated by only 0.0467 decade. I could not verify any derivation of Poplawski's printed \(10^{16}\,\mathrm{kg}\) from the pinned paper, nor could I verify that the five tested routes exhaust what its conjectural density statement permits. This verdict does not rule on error versus estimate.
