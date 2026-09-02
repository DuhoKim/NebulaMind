# SEAT BRIEF — Program (C), the flux route

Read `PROGRAM_C_FLUX_PREREG_20260902.md` in this directory, then the source passages it cites
(`../bhu-reading-20260823/sources/2003.11544_clean.txt` lines 130–160, 186–300). Use nothing else.
Derive, from first principles and showing every step:
1. The linearised flux functional δΦ[δ] for a spherically symmetric 4-window M_§ about the observer
   (state your gauge; show that the fluid term is 4πG(δρ+3δp) at linear order).
2. Reading F1: what does δΦ[δ] = 0 constrain? Decompose the perturbation field around the observer
   in spherical harmonics and state exactly which (ℓ, m) enter δΦ. Then state the consequence for
   the CMB C_ℓ (ℓ ≥ 1) and for S₁/₂, with the symmetry argument written out (rotational invariance
   of a spherically symmetric functional vs the transformation of a_ℓm).
3. Reading F2: (W ⋆ δ)(x) = 0 for all x. Take the Fourier transform. What does it imply for δ̃(k)?
   For a compactly supported spherically symmetric W, what is the zero set of W̃(k) (name the
   theorem that makes it isolated)? What continuous power spectra P(k) are compatible?
4. Classify each reading as FLUX_ALPHA / FLUX_BETA / FLUX_GAMMA / FLUX_DELTA per the prereg §3.
   If BETA, you must exhibit the C_ℓ modification explicitly.
5. Sanity check (mandatory): for a spherical top-hat window of radius R, write W̃(k) in closed form
   and give its first two positive zeros numerically.
Output: first line TWO tokens, `F1=<class> F2=<class>`; then the derivation; then one plain-language
paragraph. Change no files except your own output file.
