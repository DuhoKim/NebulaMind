URL: https://data.desi.lbl.gov/doc/releases/dr1/vac/bao-cosmo-params/

[Skip to content](https://data.desi.lbl.gov/doc/releases/dr1/vac/bao-cosmo-params/#desi-dr1-bao-cosmology-results)

# DESI DR1 BAO cosmology results [¶](https://data.desi.lbl.gov/doc/releases/dr1/vac/bao-cosmo-params/\#desi-dr1-bao-cosmology-results "Permanent link")

## Overview [¶](https://data.desi.lbl.gov/doc/releases/dr1/vac/bao-cosmo-params/\#overview "Permanent link")

This repository contains cosmology chains and posterior maximization results for the DESI DR1 BAO cosmology results referenced in the paper [DESI 2024 VI: cosmological constraints from the measurements of baryon acoustic oscillations](https://ui.adsabs.harvard.edu/abs/2025JCAP...02..021A/abstract), JCAP 2025, 02.

## Data Access [¶](https://data.desi.lbl.gov/doc/releases/dr1/vac/bao-cosmo-params/\#data-access "Permanent link")

**Data URL:** [https://data.desi.lbl.gov/public/dr1/vac/dr1/bao-cosmo-params](https://data.desi.lbl.gov/public/dr1/vac/dr1/bao-cosmo-params)

NERSC access:

```
/global/cfs/cdirs/desi/public/dr1/vac/dr1/bao-cosmo-params
```

## Documentation [¶](https://data.desi.lbl.gov/doc/releases/dr1/vac/bao-cosmo-params/\#documentation "Permanent link")

The primary directory contains two folders: `cobaya/` contains MCMC chains and posterior samples obtained using the [`cobaya`](https://cobaya.readthedocs.io/en/latest/) sampling code, and `iminuit/` contains posterior maximization results determined using the [`iminuit`](https://scikit-hep.org/iminuit/) optimization code. Within each of these directories, results for different cosmological model scenarios and combinations of datasets are arranged in subfolders named according to the `[model]/[dataset]` convention, where `[model]` and `[dataset]` can take different values as explained below. The DESI DR1 BAO likelihoods used to produce these results are publicly available at [https://github.com/CobayaSampler/bao\_data](https://github.com/CobayaSampler/bao_data) (in the files named `desi_2024_*`).

### Models [¶](https://data.desi.lbl.gov/doc/releases/dr1/vac/bao-cosmo-params/\#models "Permanent link")

Model naming follows the _Planck_ convention: the base ΛCDM cosmological model is denoted by the root `base` in the folder name, with additional free parameters – when present – indicated by suffixes attached to this root. The naming convention relating suffixes to models is as follows:

- `_w`: A dark energy equation of state parameter w that is freely varied but restricted to be constant in time
- `_w_wa`: A variable dark energy equation of state with two free parameters, w0 and wa
- `_mnu`: Free sum of neutrino masses, ∑mν, with only a non-negativity constraint, ∑mν>0
- `_mnu059`: Free sum of neutrino masses, ∑mν, with the additional prior that ∑mν>0.059 eV
- `_mnu100`: Free sum of neutrino masses, ∑mν, with the additional prior that ∑mν>0.1 eV
( **Note**: in all the above cases the neutrinos are treated as 3 degenerate mass eigenstates)
- `_nnu`: Free effective number of relativistic degrees of freedom, Neff
- `_omegak`: Free curvature parameter, ΩK

Suffixes can also be chained together to represent models with more than one free parameter, _e.g._ the folder `base_omegak_w_wa/` contains results for the model where base ΛCDM is extended by allowing free curvature and a time-varying dark energy equation of state.

### Datasets [¶](https://data.desi.lbl.gov/doc/releases/dr1/vac/bao-cosmo-params/\#datasets "Permanent link")

Different datasets or likelihoods are indicated by strings present in the folder names, according to the dictionary below. For combinations of several datasets, the folder names are formed by chaining together building blocks representing different individual datasets, separated by `_`.

#### BAO likelihoods [¶](https://data.desi.lbl.gov/doc/releases/dr1/vac/bao-cosmo-params/\#bao-likelihoods "Permanent link")

- `desi-bao-[X]`: DESI DR1 BAO data from [DESI 2024 III: baryon acoustic oscillations from galaxies and quasars](https://ui.adsabs.harvard.edu/abs/2025JCAP...04..012A/abstract) and [DESI 2024 IV: Baryon Acoustic Oscillations from the Lyman alpha forest](https://ui.adsabs.harvard.edu/abs/2025JCAP...01..124A/abstract); the `[X]` placeholder specifies the subset of DESI data used and can take the following values:
  - `bgs`: BAO measured in Bright Galaxy Sample, at effective redshift zeff=0.295
  - `lrgz0`: BAO from the first Luminous Red Galaxy (LRG) redshift bin, at zeff=0.510
  - `lrgz1`: BAO from the second LRG redshift bin, at zeff=0.706
  - `lrg`: the combination of the above two redshift bins (`lrgz0` and `lrgz1`)
  - `lrgpluselg`: BAO from the combined LRG and Emission Line Galaxy (ELG) sample at zeff=0.930
  - `elg`: BAO from higher redshift ELGs, at zeff=1.317
  - `qso`: BAO from the quasar sample (QSO), at zeff=1.491
  - `lya`: BAO from the Lyman-α forest (and cross-correlation with quasars) at zeff=2.330
  - `all`: the combination of DESI BAO data in all the above redshift bins
- `desi-sdss-best`: A combination of BAO results from DESI DR1 and the earlier SDSS surveys, consisting of the `lrg-z1`, `lrgpluselg`, `elg` and `qso` data above from DESI DR1, a combination of DESI DR1 and SDSS Lyman-α forest BAO results at zeff=2.330, and only SDSS results in the remaining redshift bins.

#### Cosmic microwave background (CMB) likelihoods [¶](https://data.desi.lbl.gov/doc/releases/dr1/vac/bao-cosmo-params/\#cosmic-microwave-background-cmb-likelihoods "Permanent link")

- `planck2018-lowl-TT-clik`: CMB low-ℓ (ℓ≤30) TT `Commander` likelihood from _Planck_ PR3
- `planck2018-lowl-EE-clik`: CMB low-ℓ EE `simall` likelihood from _Planck_ PR3
- `planck2018-highl-plik-TTTEEE`: _Planck_ PR3 `plik` likelihood for TT, TE and EE at ℓ>30
- `planck-NPIPE-highl-CamSpec-TTTEEE`: alternative `CamSpec` CMB likelihood for ℓ>30 TT, TE and EE from _Planck_ PR4
- `planck2020-hillipop-TTTEEE`: alternative `hillipop` CMB likelihood for ℓ>30 TT, TE and EE from _Planck_ PR4
- `planck2020-lollipop-lowlE`: alternative `lollipop` CMB likelihood for ℓ≤30 TE and EE from _Planck_ PR4
- `planck-act-dr6-lensing`: CMB lensing data from the combination of _Planck_ PR4 NPIPE and ACT DR6 (as provided by the ACT team) – these runs (which were quoted in the [DESI 2024 VI](https://ui.adsabs.harvard.edu/abs/2025JCAP...02..021A/abstract) paper, were performed using v1.1 of this likelihood, which was subsequently updated to fix a bug)
- `planck-act-dr6-lensing-v1.2`: CMB lensing data from the combination of _Planck_ PR4 NPIPE and ACT DR6 using the later v1.2 of this likelihood code with the bug fix
- `planck2018-thetastar-fixed-marg-nnu`: A minimal CMB-derived prior on the acoustic angular scale θ∗, with width chosen to marginalise over Neff
- `planck2018-thetastar-fixed-nnu`: A minimal CMB-derived prior on the acoustic angular scale θ∗, with narrower width to represent fixed Neff
- `planck2018-rdrag-fixed-nnu`: An alternative CMB-derived prior on the sound horizon scale at the drag epoch, rdrag, obtained from the `base`ΛCDM CMB chains

The CMB lensing likelihood was either incorporated in the posterior sampling at runtime, in which case the string in the folder name appears as above, or added in post-processing via importance sampling, in which case an additional `add_` prefix is added so the string appears as, _e.g._, `add_planck-act-dr6-lensing`.

The default combination of CMB likelihoods used in the [DESI 2024 VI](https://ui.adsabs.harvard.edu/abs/2025JCAP...02..021A/abstract) paper, and denoted as “CMB” therein, is `planck2018-lowl-TT-clik_planck2018-lowl-EE-clik_planck2018-highl-plik-TTTEEE_add_planck-act-dr6-lensing`.

#### Type Ia supernova likelihoods [¶](https://data.desi.lbl.gov/doc/releases/dr1/vac/bao-cosmo-params/\#type-ia-supernova-likelihoods "Permanent link")

- `pantheonplus`: SNIa data from the Pantheon+ dataset
- `union3`: SNIa data from the Union3 dataset
- `desy5sn`: SNIa data from the Dark Energy Survey 5-year SN dataset

#### Additional external priors [¶](https://data.desi.lbl.gov/doc/releases/dr1/vac/bao-cosmo-params/\#additional-external-priors "Permanent link")

- `schoneberg2024-bbn`: A BBN prior on the baryon density Ωbh2
- `schoneberg2024-bbn-fixed-nnu`: A more restrictive version of the above BBN prior derived by fixing Neff rather than marginalising over it

These individual likelihoods and priors can be combined together in too many ways to exhaustively list here. Combinations can be identified by chaining together the appropriate roots using `_` separators.

### Data Model [¶](https://data.desi.lbl.gov/doc/releases/dr1/vac/bao-cosmo-params/\#data-model "Permanent link")

The individual `cobaya/[model]/[dataset]/` directories contain `cobaya` output files as described in full [here](https://cobaya.readthedocs.io/en/latest/output.html) (see also [here](https://cobaya.readthedocs.io/en/latest/sampler_mcmc.html) for additional information). The output files in the folders are:

- `[prefix].[number].txt`: ASCII formatted tables providing posterior samples, where `[number]` indicates the chain number from 1 to 4; `[prefix]` is `chain` for standard runs or `chain.post.importance` when any likelihoods have been added by importance sampling in post-processing
- `[prefix].input.yaml` or `[prefix].updated.yaml`: YAML file recording the input settings provided for the MCMC run; the filename contains `updated` when the any component uses default settings not explicitly provided in the input, which are then recorded in this file. `[prefix]` takes the value `chain` for standard runs or `chain.post.lensing` when CMB lensing is added by importance sampling in post-processing
- `chain.covmat`: ASCII-formatted covariance matrix for sampled cosmological parameters, which can be used as a proposal pdf for new runs using the same settings (not present for post-processed runs)
- `chain.checkpoint`: text file with summary information about the convergence of the MCMC run (not present for post-processed runs)

Chain data can easily be read and manipulated using the [`GetDist`](https://getdist.readthedocs.io/en/latest/) package, but can also be accessed by other commonly used chain-processing software.

The individual `iminuit/[model]/[dataset]/` directories contain output files described in full [here](https://cobaya.readthedocs.io/en/latest/sampler_minimize.html). The relevant files are:

- `bestfit.minimum.txt`: ASCII-formatted file providing the parameter values and goodness-of-fit criteria at the maximum of the posterior (MAP)
- `bestfit.minimum`: identical information to the file above, but recorded in [`GetDist`](https://getdist.readthedocs.io/en/latest/)-compatible formatting
- `bestfit.bestfit.txt`: as for `bestfit.minimum.txt`, but recording the maximum likelihood position instead of the MAP (not present in all cases)
- `bestfit.bestfit`: identical to `bestfit.bestfit.txt` but in `GetDist`-compatible formatting (not present in all cases)

## Contact [¶](https://data.desi.lbl.gov/doc/releases/dr1/vac/bao-cosmo-params/\#contact "Permanent link")

Contact [Seshadri Nadathur](mailto:seshadri.nadathur@port.ac.uk) for questions about this catalog.
