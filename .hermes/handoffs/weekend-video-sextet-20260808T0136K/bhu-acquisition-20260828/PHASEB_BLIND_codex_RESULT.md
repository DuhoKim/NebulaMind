# Phase-B blind independent implementation result

Actual stdout from `python3 -u phaseB_blind_codex.py`:

```text
Independent Phase-B blind cut-sky S_1/2
nside=64 lmax=191 bins=3 deg FWHM=160 arcmin
Implementation choices: harmonic evaluation of exact 3-degree bin-integrated pair sums;
  256-point Gauss-Legendre quadrature; linear interpolation from bin centers.
f_sky=0.75146484 (36936/49152)
S_1/2_obs=1217.3647 uK^4
MC n_per_row=500
seed policy: NumPy legacy RNG reset once per row; each listed seed starts that row's stream
row seed median_uK4 p05_uK4 P_le_obs
lcdm 731021 31823.4505 5403.78998 0.002000
A_2pi 731022 8185.99888 1713.01615 0.022000
A_pi 731023 19055.3324 3749.39824 0.008000
B_spliced 731024 11024.0901 2171.22205 0.016000
B_nosplice 731025 13387.8737 2536.41971 0.006000
elapsed_seconds=77.621
```
