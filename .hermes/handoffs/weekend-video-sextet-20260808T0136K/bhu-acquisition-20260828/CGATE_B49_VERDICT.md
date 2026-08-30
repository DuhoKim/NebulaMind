ERRATUM_RING_CONCLUSION_HOLDS

# CGATE B49 verdict

I read the complete one-page 2013 erratum and the relevant version-of-record passage from equation (21) through the ring conclusion following equations (29)–(32). I rendered the VoR pages containing equations (21)–(29) and the erratum itself and treated those pages—not the text companions—as authoritative.

The erratum repairs the presentation and cylindrical integration measure. It does not weaken the point-particle, system-of-points, or symmetric Dirac–Kerr–Newman ring exclusions. It also does not touch the later Cartan-density, minimum-black-hole-mass, energy, or LHC discussion.

## 1. Corrected equation (29) preserves the ring result

The original VoR prints the cylindrical coordinate assignment incorrectly as

`(x1 = r, x2 = z, x3 = phi)`

and writes equation (29) without the cylindrical Jacobian. The erratum corrects these to

`(x1 = r, x2 = phi, x3 = z)`

and

`M^{alpha ij} proportional to integral delta x^alpha v^{ij} delta(r-a) delta(z) r dr dphi dz`.

Those corrections make the subsequent component identifications coherent and leave their zeros intact. For the ring of radius `a > 0`:

- `delta x^1 = r-a`, so

  `M^{1ij} proportional to integral (r-a) v^{ij} delta(r-a) delta(z) r dr dphi dz = 0`;

- `delta x^3 = z`, so

  `M^{3ij} proportional to integral z v^{ij} delta(r-a) delta(z) r dr dphi dz = 0`.

The new factor `r` is evaluated on the support as `r=a`. It rescales a potentially nonzero surviving moment but cannot undo either distributional zero. The corrected coordinate order is important: it makes index 3 the axial `z` coordinate, matching the already printed `delta x^3=z` and the later axial-spin discussion.

Therefore equation (30), `M^{1ij}=M^{3ij}=0`, still follows. Equation (17) then gives the two relations printed in (31). Setting `j=0` and using the total antisymmetry in (21) still yields `N^{i01}=N^{i03}=0` in (32). The paper then identifies `N^{123}` as the only potentially nonzero spatial spin-density component and the axial spin component `N_3`, dual to `N^{012}`, as zero. That contradicts the nonzero axial spin required by the symmetric Dirac–Kerr–Newman ring construction under consideration.

Thus the scoped conclusion recorded after B34 survives: under the paper's ECKS/Dirac/Papapetrou assumptions and the additional symmetry assumptions used to identify the string with the Kerr–Newman ring, that singular ring is excluded. The erratum does not broaden this into an exclusion of every possible string or two-dimensional support.

## 2. Point particle and system of points

The first two erratum corrections clarify that the delta-supported configurations are located at the origin:

- the second sentence below (21) begins, “For this configuration located at the origin…”; and
- the sentence below (26) begins, “For a point particle located at the origin…”.

For the single-pole configuration, this makes the moment calculation explicit: multiplying the origin-supported delta distribution by the displacement from the origin makes the first moment in (22) vanish, producing (23). The chain through (24)–(27) is unchanged: total antisymmetry and the Papapetrou relation force the spin density to vanish, which for a nonzero Dirac field contradicts the Dirac spin density.

The correction does not weaken the system-of-points paragraph. That paragraph separately says each point has symmetric energy–momentum, so equation (9) gives the relevant antisymmetric moment zero; equations (17) and (21) then still yield (27), contradicting a nonzero Dirac field. “Located at the origin” is the coordinate origin used for the local multipole expansion, not a new physical restriction that only a particle at one privileged global point is excluded. Each pole can be centered in its own local moment expansion.

No equation in this point/system chain is deleted or given a weaker hypothesis by the erratum.

## 3. Mass-floor and LHC material are untouched

The erratum lists exactly four corrections, all confined to the equation-(21)–(29) Papapetrou discussion. It contains no Cartan density, Cartan radius, `10^51 kg m^-3`, `10^16 kg`, `10^43 GeV`, LHC energy, or 39-orders statement.

Those estimates occur later in the original paper, after the ring discussion, and the erratum supplies no replacement for them. B49 is therefore correct that the erratum does not resolve or alter the separate reproducibility/arithmetic dispute over the mass floor. It only shows that the published correction is irrelevant to that dispute.

## 4. Record fidelity

The entry-51 erratum note accurately enumerates the four changes, prints the corrected coordinate order and integral, confines the erratum to the Papapetrou section, and states that the mass-floor/LHC material is untouched. Its statement that the correction is not a retraction is factually fair.

The phrase “the author's conclusion stands in the corrected text” should be understood carefully: the one-page erratum does not reprint the conclusion or explicitly announce a fresh proof. Rather, applying its corrected equation to the VoR derivation reproduces the same vanishing components, as shown above. The conclusion stands by calculation, not merely because the document is titled an erratum rather than a retraction.

The existing scoped record is appropriately narrower than the abstract: it limits the ring exclusion to the additional symmetry assumptions used for that construction and notes that the string-to-ring step begins as a symmetry expectation. Nothing in the erratum warrants changing that scope or the paper-level `CALIBRATED-FALSIFIER / LIVE` convention already decided in Q6.

## 5. Predicate audit

Running `b49_plb690_vor_compare.py` unchanged returns `11/11`, but it does not test the substantive question dispatched to this gate.

1. **VoR pin:** checks only PDF magic and a broad byte-size interval because the download hash is said to drift. It does not verify seven pages, page readability, DOI metadata, or content stability. The identity check adds title/journal/author strings from the companion, not from the PDF bytes.
2. **Cartan-density equality:** despite its label, it checks only the generic token `10` in both texts, `kg m` somewhere in the VoR, and `Cartan density` in both. It never binds exponent 51 to the density or verifies units in the preprint.
3. **Minimum-mass equality:** checks a loose rendering of `10^16 kg` plus “39 orders,” but does not check `10^43 GeV` at all despite announcing it in the label. It also does not bind each number to the same sentence in both artifacts.
4. **LHC equality:** the shared phrase is useful but does not verify the `10^4 GeV` LHC value.
5. **Reproducibility caveat:** two phrase fragments establish that the paper calls the density an approximate order estimate. They do not assess or reproduce its arithmetic.
6. **VoR record predicate:** it has an operator-precedence defect. The expression is effectively `(all earlier requirements) OR ("unreproduced floor" in b51)`. Because that final phrase exists, the check can pass even if the VoR pin, word-for-word comparison, or other record requirements disappear.
7. **Erratum pin:** genuinely checks PDF magic, a hash prefix, and broad identity strings. It does not verify that the PDF is one page or visually readable.
8. **Erratum scope:** checks that `(21)`, `(26)`, and `Eq. (29)` appear, but not the exact four corrections. Its positive test for generic `10` does not establish anything about the absent `10^16` value; the `10` can come from the original DOI/year. Absence of `Cartan` and `black-hole masses` is helpful but does not exhaust all mass-floor/LHC phrases.
9. **Erratum record:** checks only three prose fragments. It does not verify the corrected coordinate ordering, the factor `r`, the delta support, the four-item count, or the ring derivation.
10. **Tier:** merely parses the current label and does not adjudicate whether the erratum affects either claim shape.

Most importantly, there is no predicate that evaluates the corrected distributional integral, requires `M^{1ij}=M^{3ij}=0`, traces equations (30)–(32), or tests the point/system-of-points conclusions. `11/11` therefore verifies selected custody and record strings, not the conclusion this B49 gate was asked to decide.

## Disposition

Confirm the erratum note and retain the existing scoped obstruction content. The corrected equation (29) preserves the vanishing axial component and the symmetric Dirac–Kerr–Newman ring exclusion. The point-particle and system-of-points exclusions are not weakened, and the mass-floor/LHC material is untouched.
