AUDIT_HOLDS_CONSISTENCY_ONLY

## 1. The construction

The paper combines two layers.

The parent regular-black-hole geometry is the previously obtained de Sitter–Schwarzschild solution, not newly derived here. The assumed stress tensor obeys \(T^r{}_r=T^t{}_t\), hence \(p_r=-\rho\) (lines 162–172), and generates the Kerr–Schild metric
\[
ds^2=\left(1-\frac{R_g(r)}r\right)dt^2-\frac{dr^2}{1-R_g(r)/r}-r^2d\Omega^2,
\qquad R_g(r)=2GM(r),
\]
with \(M(r)=4\pi\int_0^r\rho(x)x^2dx\) (lines 197–228). The required asymptotics make the center de Sitter and infinity Schwarzschild; the text gives \(R_g\sim r^3/r_0^2\), \(r_0^2=3c^2/(8\pi G\rho_0)\), and cites the earlier exact profile \(\rho=\rho_0\exp[-r^3/(r_0^2r_g)]\) (lines 232–254). It explicitly attributes the general solution to Ref. 14, Dymnikova 1992 (lines 162–165; reference identification at lines 1258–1260). For \(M>M_{\rm crit}\), this imported geometry has event and Cauchy horizons and a regular de Sitter core (lines 277–281); its repeated regular-core regions are the proposed nucleation sites (lines 560–567, 584–592).

The daughter-universe calculation is a minisuperspace Wheeler–DeWitt/WKB model. Starting from the conformal-time Friedmann equation (6), the paper writes
\[
\frac{\hbar^2}{2m_{\rm Pl}}\frac{d^2\psi}{da^2}-U(a)\psi=0,
\qquad
U(a)=\frac{m_{\rm Pl}c^2}{2l_{\rm Pl}^2}\left(ka^2-\frac{a^4}{r_0^2}\right)
\]
(lines 802–855). With vacuum, strings/quintessence \(p=-\rho/3\), and radiation, the assumed density is
\[
\rho=\rho_0\left(1+B_s\frac{r_0^2}{a^2}+B_\gamma\frac{r_0^4}{a^4}\right)
\]
(lines 898–922), and the Schrödinger form has
\[
U(a)=\frac{m_{\rm Pl}c^2}{2l_{\rm Pl}^2}\left[(k-B_s)a^2-\frac{a^4}{r_0^2}\right],
\qquad E=\frac{B_\gamma}{2}\left(\frac{r_0}{l_{\rm Pl}}\right)^2E_{\rm Pl}
\]
(lines 923–952). The WKB quantization condition and levels are
\[
2\int_0^{a_1}\sqrt{2m_{\rm Pl}(E_n-U)}\,da=\pi\hbar(n+1/2),
\qquad E_n\simeq E_{\rm Pl}\sqrt{k-B_s}(n+1/2)
\]
(lines 1034–1048). The barrier action is the integral in
\[
D=\exp\left[-\frac{2}{\hbar}\left|\int_{a_1}^{a_2}\sqrt{2m_{\rm Pl}[E-U(a)]}\,da\right|\right],
\]
which the paper identifies with the Euclidean-action WKB result (lines 1050–1072). Its evaluated expression is
\[
D_2=\exp\left\{-\frac23\left(\frac{r_0}{l_{\rm Pl}}\right)^2(k-B_s)^{3/2}+(2n+1)+I\right\},
\quad I<10^{-2}(2n+1),
\]
with the level constraint in (17) (lines 1073–1116). The PDF-to-text layout makes the final placement of \((2n+1)+I\) typographically awkward, but the receipt above reproduces the paper's displayed content rather than repairing it silently.

The free/selected inputs are: discrete daughter curvature \(k=0,\pm1\) (lines 809–825); core vacuum scale \(\rho_0\), equivalently \(r_0\) or \(\Lambda_{\rm core}\), supplied by the parent solution (lines 232–252); string/quintessence coefficient \(B_s\); radiation coefficient \(B_\gamma\), equivalently the nonzero level \(E_n\); and the quantum number \(n\) (lines 910–952, 1034–1048). The illustrative closed-from-nothing estimate additionally selects a GUT scale (lines 877–892).

## 2. Derived versus premised; favored curvature

The existence of a regular black hole with a de Sitter interior is a premise imported from the earlier solution: this paper says the relevant distributed-profile solution “has been studied” and “was found” in Ref. 14 (lines 162–180), then uses its core regions as seeds (lines 593–603). It does not derive collapse into that object, core formation, or the value of \(\Lambda_{\rm core}\).

Conditional on that parent, the minisuperspace matter ansatz, and WKB treatment, universe birth is derived in the limited sense that a barrier and a nonzero penetration factor \(D\) are calculated: equations (13)–(16), lines 923–958 and 1034–1097. This is a conditional semiclassical consistency result, not a derivation that such a fluctuation occurs in nature.

The “flat birth” finding is confirmed, but it is a comparative plausibility judgment driven by required string content, not a curvature prediction. Choosing \(k-B_s\simeq3\times10^{-6}\), the paper obtains \(B_s\simeq-(1+3\times10^{-6})\) for open birth but only \(B_s\simeq-3\times10^{-6}\) for flat birth; it therefore says the flat case is favored because its string content is very small (lines 1118–1130). It then states: “The most plausible case is the birth of a flat (Ω = 1) universe” because a very small admixture suffices (lines 1142–1145), repeated at lines 1175–1177. Equation (13) shows exactly why: curvature and the string term enter only through \(k-B_s\) (lines 930–952).

## 3. Claim-level exclusion for flat/open births

It is derived within the adopted density ansatz, rather than merely asserted. From equation (13), a positive barrier away from \(a=0\) requires the quadratic coefficient to be positive:
\[
k-B_s>0 \quad\Longleftrightarrow\quad B_s<k.
\]
The paper explicitly explains that a negative \(B_s\) mimics positive curvature and supplies the barrier for \(k=0,-1\) (lines 954–958). Thus:

- flat \(k=0\): \(B_s<0\);
- open \(k=-1\): \(B_s<-1\).

At the paper's illustrative \(k-B_s\simeq3\times10^{-6}\), these sharpen to \(B_s\simeq-3\times10^{-6}\) and \(B_s\simeq-(1+3\times10^{-6})\), respectively (lines 1118–1129). Without this sufficiently negative term there is no barrier of the modeled form, so the claimed WKB tunnelling channel is unavailable. This exclusion is model-conditional: it does not prove that every possible mechanism for flat/open birth requires negative-deficit strings.

## 4. Observation-facing content for our universe

There is no identification of our universe as a daughter, no predicted measured \(\Lambda\), curvature sign, relic abundance, or independent observational threshold. The only explicit identification is possibility language: the result makes it possible to “speculate (at least not exclude)” that our Universe lies inside a regular black hole (lines 1178–1181).

The numerical observational content runs in the opposite direction from a prediction. The known anisotropy \(\Delta T/T\le10^{-5}\) “as in our Universe” is imported to restrict \(k-B_s\) to a range around \(10^{-6}\), after which the author chooses \(3\times10^{-6}\) as an example (lines 1118–1122). That choice yields the sample \(B_s\) values (lines 1123–1130) and the estimate \(D_3=\exp[-(2/3)10^7]\) for all \(k\) (lines 1131–1143). No likelihood, data fit, observable mapping unique to the black-hole-parent hypothesis, or failure threshold is supplied. The statement that infinitely many core regions make birth probability “not negligible” (lines 1146–1147, 1178–1179) also lacks a normalized measure over trials.

## 5. Easson map (report only)

Entry 22's Proposition 2 is inapplicable to the construction actually analyzed here. This paper assumes a regular, static, spherically symmetric parent geometry with de Sitter-core regions, then treats a daughter as a nonperturbative quantum fluctuation whose scale factor tunnels through a Wheeler–DeWitt potential barrier (lines 593–619, 802–808, 1050–1072). It does not construct a classical comoving, no-shell FRW daughter by identifying a portion of the parent stress tensor and geometry across a classical interface. Indeed, the daughter matter coefficients \(B_s\) and \(B_\gamma\) are separately posited for the nucleating fluctuation (lines 898–958). Therefore a proposition restricting minimal classical regular-BH-to-FRW mappings does not directly restrict this quantum minisuperspace channel. This is not a claim that tunnelling evades every consistency condition; only that the proposition's classical matching hypotheses are absent here.

## 6. Tier consequence

**CONSISTENCY-ONLY holds.** The paper establishes an internally calculable conditional channel: given a de Sitter regular core, a chosen minisuperspace state, and matter coefficients producing \(k-B_s>0\), WKB tunnelling has nonzero probability. It also gives the qualitative conditional direction that flat birth needs much less negative-string content than open birth. But the de Sitter parent and its scale are premised; the fluctuation content is free; the observed anisotropy is used as an input rather than predicted; and the link to our universe is expressly speculation/not-exclusion. The numeric tunnelling estimate is not an observable calibrated against our universe.

On A(a), this is an **absence of an observation-facing discriminator**: the lane could in principle own a missing threshold only after the model supplies a definite observable and number, but here both the model-to-observable identification and an independently predicted number are missing. Consequently it cannot be promoted to QUALITATIVE-DIRECTIONAL, PROSPECT, or CALIBRATED-FALSIFIER on the evidence in this paper.

In plain language: the paper shows that a baby universe can be made quantum-mechanically possible inside an already-assumed regular black hole, provided the starting fluctuation contains the right ingredients. Its equations favor the flat option because that option needs only a tiny negative string-like contribution, whereas an open universe needs a much larger one. It does not show that our universe actually came from a black hole, and its observational number is borrowed from our universe to tune the model rather than forecast by it. The entry therefore remains a consistency argument, not an observational test.
