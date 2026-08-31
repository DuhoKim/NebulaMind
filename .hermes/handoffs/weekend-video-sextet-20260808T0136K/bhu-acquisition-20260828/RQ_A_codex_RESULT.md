STRADDLES_OPTIMISTIC_ONLY_NO_CALIBRATED_FALSIFIER

# RQ-A codex result — entry 21 QNM amplitude versus LISA

## Result in one paragraph

Roupas supplies a frequency and damping rate, but no merger-to-interior-mode coupling. Under an explicitly assumed energy fraction `ε_rd`, the fundamental mode is visible to four-year LISA only for an optimistic excitation and a very nearby event. At `D=1 Gpc`, even putting an extreme 3% of the remnant rest energy into this single distinctive mode gives four-year characteristic strains of `2.35e-22`, `7.44e-22`, and `2.35e-21` for `10^4`, `10^5`, and `10^6 M_sun`; the corresponding Robson–Cornish–Liu sky-averaged noise strains are `1.21e-21`, `9.02e-21`, and `4.60e-19`. The SNRs are only `0.195`, `0.0825`, and `0.00511`. At an illustrative low excitation `ε_rd=10^-6`, they are another factor `sqrt(0.03/10^-6)=173.2` smaller. An optimistic SNR-8 horizon exists—about 24.4, 10.3, and 0.64 Mpc respectively—but there is no source-derived positive lower bound on `ε_rd`; it may be arbitrarily small. Thus the result **straddles only by assuming optimistic excitation and exceptional proximity**. It does not turn “detectable” into a calibrated population falsifier. No tier change is made or proposed here.

## 1. Source quantities and a frequency-unit defect

The pinned Roupas text gives, for the axial `n=0, l=2` mode at `10 M_sun`,

`(2GM/c^3) ω_R = 0.0062`,  
`(2GM/c^3) ω_I = -1.5323e-17`.

It also states that the dimensionless mass dependence is very small, so I scale these values with `1/M` for the requested masses. This is the closest reproducible extraction available from the greppable source; Fig. 5 does not supply machine-readable per-mass values.

There is a `2π` inconsistency in the paper that matters for a strict detector comparison. Its perturbation is `exp(-iωt)`, so `ω` is angular frequency. The dimensionless value above gives `ω_R=62.94 s^-1` at `10 M_sun`, yet the prose calls this `63 Hz`. The physical cyclic frequency is `f=ω_R/(2π)=10.02 Hz`. I therefore report both the paper's frequency label and the dimensionally correct cyclic frequency, and use the latter in the strain/noise calculation:

| Remnant mass | paper-labeled “Hz” (`ω_R`) | physical `f=ω_R/2π` | `τ=1/|ω_I|` |
|---:|---:|---:|---:|
| `10^4 M_sun` | `6.2936e-2` | `1.0017e-2 Hz` | `2.037e8 yr` |
| `10^5 M_sun` | `6.2936e-3` | `1.0017e-3 Hz` | `2.037e9 yr` |
| `10^6 M_sun` | `6.2936e-4` | `1.0017e-4 Hz` | `2.037e10 yr` |

The long damping times follow directly from Table 1's tiny imaginary part. They are not a detail: all are vastly longer than a LISA mission.

## 2. Excitation/energy formalism

The requested Leaver-residue calculation cannot be completed from Roupas's paper. Appendix C provides the homogeneous axial master equation and potential,

`d^2φ/dr_*^2 + (ω^2/c^2 - V)φ = 0`,

but not a merger source term, initial perturbation, normalized QNM eigenfunctions, Green-function residue, or binary-merger matching. A Leaver/Berti–Cardoso excitation coefficient by itself is source-independent only after a normalization convention; the actual amplitude also needs the source overlap. Roupas correctly says this calculation remains to be done. I do not fabricate it.

I therefore use the alternative explicitly allowed in the brief: a conditional single-mode energy fraction

`E_rd = ε_rd M c^2`.

For a circularly polarized, exponentially damped wave at luminosity distance `D`, define

`h_+ = A exp(-t/τ) cos(ω_R t)`,  
`h_x = A exp(-t/τ) sin(ω_R t)`.

Using the GR wave flux

`F = c^3/(16πG) [dot(h_+)^2 + dot(h_x)^2]`

and an isotropic-equivalent emission normalization, integration over time and area gives

`E_rd = c^3 D^2 A^2 τ(ω_R^2 + τ^-2)/(8G)`

and hence

`A = [8G ε_rd M c^2 / {c^3 D^2 τ(ω_R^2 + τ^-2)}]^(1/2)`.

This `A` is an intrinsic root-sum-polarization amplitude under the stated circular/isotropic-equivalent convention. Angular emission, inclination, and detector response can change individual events by order-unity geometry factors; I do not hide those inside `ε_rd`.

### Excitation assumptions

- Illustrative conservative excitation: `ε_rd = 10^-6`.
- Deliberately optimistic ceiling: `ε_rd = 0.03`, placing 3% of the entire remnant rest energy in this one late, distinctive interior mode.
- Fiducial distance: `D = 1 Gpc`.
- Observation: `T_obs = 4 yr`, starting when the mode is accessible after the exterior light-ring signal damps.

These are conditional brackets, not a model-derived two-sided confidence interval. In particular, the strict conservative lower bound is **zero** because the uncomputed merger overlap may vanish or be arbitrarily suppressed. The 3% case is intentionally generous; it is not a result of the cosmological-BH model.

Because `τ >> T_obs`, LISA cannot accumulate the energy emitted over the full damping lifetime. The applicable finite-mission characteristic strain is

`h_c,T = A sqrt(f T_obs)`,

not `A sqrt(f τ)`. Substituting `τ` would silently grant LISA between `2e8` and `2e10` years of coherent observation and would produce a spurious detectability claim.

## 3. Public LISA sensitivity calculation

I used the four-year Robson, Cornish & Liu (2019) analytic sky-averaged sensitivity with `L=2.5e9 m`, `f_* = c/(2πL)`,

`S_inst(f) = 10/(3L^2) [P_OMS + 4P_acc/(2πf)^4] [1 + 0.6(f/f_*)^2]`,

`P_OMS = (1.5e-11 m)^2 [1 + (2e-3 Hz/f)^4]`,

`P_acc = (3e-15 m s^-2)^2 [1 + (0.4e-3 Hz/f)^2][1 + (f/8e-3 Hz)^4]`,

plus its four-year Galactic-confusion fit

`S_conf = 9e-45 f^(-7/3) exp[-f^0.138 - 221 f sin(0.102 f)] {1+tanh[521(0.00113-f)]}`.

The plotted/comparison noise strain is `h_n=sqrt[f(S_inst+S_conf)]`. With the consistent definitions here, the approximate coherent SNR is `ρ=h_c,T/h_n`.

## 4. Numerical amplitude and sensitivity table

All amplitudes below are at `D=1 Gpc`; they scale as `sqrt(ε_rd)/D`. Frequencies are the physically converted cyclic frequencies.

| `M` | `f` | `h_n` LISA | `A`, `ε=10^-6` | `h_c,4yr`, `ε=10^-6` | SNR | `A`, `ε=0.03` | `h_c,4yr`, `ε=0.03` | SNR |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `10^4 M_sun` | `1.0017e-2 Hz` | `1.205e-21` | `1.209e-27` | `1.359e-24` | `1.127e-3` | `2.093e-25` | `2.354e-22` | `0.1953` |
| `10^5 M_sun` | `1.0017e-3 Hz` | `9.023e-21` | `1.209e-26` | `4.297e-24` | `4.763e-4` | `2.093e-24` | `7.443e-22` | `0.08249` |
| `10^6 M_sun` | `1.0017e-4 Hz` | `4.603e-19` | `1.209e-25` | `1.359e-23` | `2.953e-5` | `2.093e-23` | `2.354e-21` | `0.005114` |

### Distance horizons

Linear distance scaling gives:

| `M` | SNR-1 horizon, `ε=10^-6` | SNR-8 horizon, `ε=10^-6` | SNR-1 horizon, `ε=0.03` | SNR-8 horizon, `ε=0.03` |
|---:|---:|---:|---:|---:|
| `10^4 M_sun` | `1.13 Mpc` | `0.141 Mpc` | `195 Mpc` | `24.4 Mpc` |
| `10^5 M_sun` | `0.476 Mpc` | `0.0595 Mpc` | `82.5 Mpc` | `10.3 Mpc` |
| `10^6 M_sun` | `0.0295 Mpc` | `0.00369 Mpc` | `5.11 Mpc` | `0.639 Mpc` |

These are amplitude horizons under the stated waveform, Euclidean distance, optimal circular polarization, sky-averaged noise, four-year coherent observation, and exactly known phase/frequency. A real search trials factor, imperfect coherence, source orientation, foreground subtraction, and an SNR threshold above 8 would reduce them.

## 5. Falsification verdict

This is the brief's **straddles** case, with the dividing assumptions named:

- At cosmological distances (`1 Gpc`) the mode is below LISA even under the 3% ceiling.
- It crosses design sensitivity only if the distinctive interior fundamental receives an optimistic fraction of merger energy and the merger occurs within roughly tens of Mpc for `10^4–10^5 M_sun`, or sub-Mpc for `10^6 M_sun`.
- At `ε_rd=10^-6`, even the requested masses require Local-Group or closer distances; the SNR-8 horizons are at most 141 kpc.
- Most importantly, Roupas's strict model supplies neither `ε_rd` nor an event population/rate. The excitation can approach zero, so frequency placement alone cannot provide a guaranteed amplitude or a LISA non-detection criterion.

Accordingly, RQ-A does **not** presently yield a candidate calibrated falsifier. A non-detection by LISA would refute only a separately specified population model with a lower-bounded excitation, event rate/distance distribution, search efficiency, and detection threshold; none is in entry 21. The paper's “detectable” language remains a conditional prospect, not a falsifiable number. This report does not change any tier.

## Reproducibility and remaining blocker

Constants used: `G=6.67430e-11 SI`, `c=299792458 m/s`, `M_sun=1.98847e30 kg`, `1 pc=3.085677581491367e16 m`, `1 yr=365.25 d`. Values were evaluated directly from the equations printed above.

Closing the strict-model amplitude requires a numerical inhomogeneous perturbation calculation: normalize the QNM solutions of Appendix C, construct the Green function and its residues, specify a binary-merger stress-energy/initial-data source, project that source onto the trapped `n=0,l=2` mode, and propagate the resulting waveform through the long-lived cavity. Until that source-overlap calculation exists, no nonzero model-owned conservative amplitude can be reported.
