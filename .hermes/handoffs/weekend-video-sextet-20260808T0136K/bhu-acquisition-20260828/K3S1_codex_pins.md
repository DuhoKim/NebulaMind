# K3S1 codex pin sheet

## Corpus objects and closures

- Dirac pseudovector: `s^i = (1/2) psibar gamma^i gamma^5 psi`; the associated completely antisymmetric tensor is `s_ijk = -e_ijkl s^l`. Receipt: `../bhu-reading-20260823/sources/1111.4595v2_poplawski_prd85_clean.txt`, lines 75–77 (Eq. 4; units `hbar=c=1`).
- Spin-fluid object: `s_ijk = s_ij u_k`, `s_ij u^j=0`. Receipt: `1111.4595v2_poplawski_prd85_clean.txt`, lines 118–119. Its scalar is `s^2=(1/2)s_ij s^ij>0`: `1007.0587_clean.txt`, lines 72–73 (Eq. 9), and `1410.3881_clean.txt`, lines 78–79 (Eq. 7).
- Printed Dirac closure: `<s_i s^i>=(3/4)n^2`. Receipt: `1111.4595v2_poplawski_prd85_clean.txt`, lines 109–114.
- Printed fluid closure: `s^2=(1/8)n^2` in natural units. Receipt: `1111.4595v2_poplawski_prd85_clean.txt`, lines 118–121. With units restored, `s^2=(1/8)(hbar*c*n)^2`: `1007.0587_clean.txt`, lines 90–91 (Eq. 13), and `1410.3881_clean.txt`, lines 84–85 (Eq. 8).

## Textbook constants, with executable receipts

The receipts are printed before the ensemble derivation by `K3S1_codex_spin.py`.

- Spin-1/2 Casimir: with `S_a=sigma_a/2`, `sum_a S_a^2=3 I/4`, hence every normalized state has `<S^2>=3/4`.
- Polarized limit: for `rho_+=(I+sigma_z)/2`, `<S>=(0,0,1/2)`. Thus `N` aligned particles in volume `V` give `s_z=N/(2V)=n/2` and `|s|^2=n^2/4`.
- Maximally mixed state: equal weights on the orthogonal `|+z>` and `|-z>` states give `rho_mix=(|+><+|+|-><-|)/2=I/2`; consequently `<S_a>=0`, `<S_a S_b>` has symmetric part `delta_ab/4`, and `<S^2>=3/4`.
- Uniform orientation: `rho(r)=(I+r.sigma)/2`, with sphere averages `<r_a>=0`, `<r_a r_b>=delta_ab/3`; its average is also `I/2`.

The Casimir is an operator second moment. The squared length of the bilinear mean in any pure spin-coherent state is instead `|<S>|^2=1/4`; the script prints both to prevent their conflation.
