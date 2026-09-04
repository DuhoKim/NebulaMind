ACCESS_SHA=037f72b7ac0cd7051c201b9835da38eeb713e906851d799cc24e13b9cbc80d04
CLASS=CONVENTION_CONFIRMED

Sources read:
`gasperini_1986_prl56_2873_vor_clean.txt` (Full text, 261 lines)

Decisive receipts:
- Lines 95-97: "...the Weyssenhoff convective condition S &u&=0, however, continues to hold also in this variational formalism. 6"
- Lines 117-119: "For an unpolarized spinning field, in particular, the averaging procedure gives, if we put (S p) =0 and a2= —,' (S iiS @) in Eq. (5)," [Translates to: <S_{\mu\nu}> = 0 and \sigma^2 = 1/2 <S_{\mu\nu}S^{\mu\nu}>].
- Lines 133-135: "...matter can be described as a liquid of unpolarized fermions with spin t/2 [1/2], and we assume, as in Ref. 8, the equation of state..."
- Lines 139-143: "We have then a- [\sigma^2] = —,' ( S ) =f( n ) /8, where n is the particle number density, and the averaging procedure gives8" [Translates to: \sigma^2 = 1/2 <S^2> = (\hbar n)^2 / 8, referencing Nurgaliev and Ponomariev (Ref 8)].

Derivation audit:
Gasperini does not derive the 1/8 coefficient in this paper. He defines the microscopic premise (a liquid of unpolarized spin-1/2 fermions) and the mean-spin condition (<S_{\mu\nu}> = 0). He then simply states "We have then \sigma^2 = ... = (\hbar n)^2 / 8" and directly attributes the resulting density scaling to "the averaging procedure gives [Ref 8]". The 1/8 factor is therefore asserted/borrowed as a given property of the unpolarized fermion fluid, with no supporting combinatorial, statistical, or trace calculation shown in this text. 

Same-object audit:
Gasperini explicitly enforces the Weyssenhoff convective condition S^{\mu\nu}u_\nu = 0 (Line 96). In the comoving rest frame where u^\mu = (0,0,0,1) (Line 103), the time-components of the spin tensor vanish, meaning the 4-tensor contraction reduces identically to the spatial contraction: S_{\mu\nu}S^{\mu\nu} = S_{ij}S^{ij}. Gasperini's \sigma^2 is defined as half this contraction (1/2 <S_{\mu\nu}S^{\mu\nu}>). This makes it precisely the same physical object as K3's s^2 = 1/2 s_{ij} s^{ij} (the squared magnitude of the spatial spin pseudovector), confirming sameness beyond mere notation.

Full-text negative search:
Searched the text for the terms: "particle-sum", "cross-term", "two-point", "density-matrix", "exchange", "correlation", "normalization", and "combinatorial". 
Result: 0 hits for all terms. There is no explicit particle-level or quantum statistical calculation in the paper that could fix the 1/8 coefficient.

Limits:
The macroscopic covariant definitions (the Weyssenhoff limit and \sigma^2 trace) fix the tensor structure and kinematic dependency of the spin fluid. However, the explicit 1/8 factor and the exact scaling with particle number density (\hbar n)^2 are strictly imported/asserted, rather than derived, leaving the microscopic justification of that numerical normalization entirely to the cited literature.

GASPERINI_K3_SECOND_SEAT_COMPLETE
