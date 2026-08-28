URL: https://data.desi.lbl.gov/doc/releases/dr1/vac/full-shape-bao-clustering/

[Skip to content](https://data.desi.lbl.gov/doc/releases/dr1/vac/full-shape-bao-clustering/#desi-dr1-full-shape-and-bao-clustering-products)

# DESI DR1 Full Shape and BAO clustering products [¶](https://data.desi.lbl.gov/doc/releases/dr1/vac/full-shape-bao-clustering/\#desi-dr1-full-shape-and-bao-clustering-products "Permanent link")

## Overview [¶](https://data.desi.lbl.gov/doc/releases/dr1/vac/full-shape-bao-clustering/\#overview "Permanent link")

This repository contains clustering measurements (power spectrum, correlation function, window matrix, covariance matrix) for the DESI DR1 Full Shape and BAO analyses.
These measurements are referenced in:

- [DESI 2024 II: Sample Definitions, Characteristics, and Two-point Clustering Statistics](https://ui.adsabs.harvard.edu/abs/2025JCAP...07..017A/abstract)
- [DESI 2024 III: Baryon Acoustic Oscillations from Galaxies and Quasars](https://ui.adsabs.harvard.edu/abs/2025JCAP...04..012A/abstract)
- [DESI 2024 V: Full-Shape Galaxy Clustering from Galaxies and Quasars](https://ui.adsabs.harvard.edu/abs/2025JCAP...09..008A/abstract)

## Data Access [¶](https://data.desi.lbl.gov/doc/releases/dr1/vac/full-shape-bao-clustering/\#data-access "Permanent link")

**Data URL:** [https://data.desi.lbl.gov/public/dr1/vac/dr1/full-shape-bao-clustering](https://data.desi.lbl.gov/public/dr1/vac/dr1/full-shape-bao-clustering)

NERSC access:

```
/global/cfs/cdirs/desi/public/dr1/vac/dr1/full-shape-bao-clustering
```

## Documentation [¶](https://data.desi.lbl.gov/doc/releases/dr1/vac/full-shape-bao-clustering/\#documentation "Permanent link")

The primary directory contains four folders:

- `data/` contains power spectrum and correlation function measurements, their window matrix and covariance matrix, and the packaged (data, window, covariance) to be used for cosmological inference, used in the Key Project Full Shape (combined with BAO) analysis.
- `data_v1.2/` contains the correlation function measurements, their window matrix and covariance matrix for the version v1.2 of the clustering catalogs, used in the Key Project BAO analysis. See Appendix B of [DESI 2024 II](https://ui.adsabs.harvard.edu/abs/2025JCAP...07..017A/abstract).
- `EZmock/` contains power spectrum, correlation function and BAO measurements for the 1000 EZ mocks.
- `AbacusSummit/` contains power spectrum, correlation function and BAO measurements for the 25 Abacus cutsky mocks.

We recommend to read the files with [lsstypes](https://github.com/adematti/lsstypes), though files can be read with any [HDF5](https://en.wikipedia.org/wiki/Hierarchical_Data_Format) reader.

Complementary to these clustering products is this [GitHub repository](https://github.com/cosmodesi/desi-kp-cosmological-likelihoods), which contains in the `dr1` folder:

- a notebook illustrating how to read the HDF5 files;
- a script to prepare the final likelihoods (including scale cuts and systematic contributions) from the raw data, window matrix and covariance matrix;
- an implementation of the Full Shape (+BAO) likelihoods.

See the `README.md` file in that directory.

### data/ Directory [¶](https://data.desi.lbl.gov/doc/releases/dr1/vac/full-shape-bao-clustering/\#data-directory "Permanent link")

For the fiducial likelihood (including data, window matrix, covariance matrix), go directly to [**data/likelihood/**](https://data.desi.lbl.gov/doc/releases/dr1/vac/full-shape-bao-clustering/#datalikelihood).

#### data/spectrum/ [¶](https://data.desi.lbl.gov/doc/releases/dr1/vac/full-shape-bao-clustering/\#dataspectrum "Permanent link")

`data/spectrum/` contains the power spectrum multipoles.
The power spectrum multipoles obtained with the FKP estimator read: `spectrum-poles_{tracer}_{region}_z{zrange[0]:.1f}-{zrange[1]:.1f}{thetacut}.h5`, with:

- tracer `tracer`: ‘BGS\_BRIGHT-21.5’, ‘LRG’, ‘ELG\_LOPnotqso’, ‘LRG+ELG\_LOPnotqso’ (for post-reconstruction correlation functions only), ‘QSO’
- region `region`: ‘NGC’, ‘SGC’, or ‘GCcomb’. Combined power spectrum measurements ‘GCcomb’ are the average of ‘NGC’ and ‘SGC’ power spectra, weighted by their normalization factor.
- redshift range `zrange`: (0.1, 0.4), (0.4, 0.6), (0.6, 0.8), (0.8, 1.1), (1.1, 1.6), (0.8, 2.1)
- θ-cut: `thetacut`: ‘’ (no θ-cut) or ‘\_thetacut0.05’. θ-cut removes all pairs with angular separation < 0.05°, to mitigate fiber assignment effects. It requires a modified window matrix (file name ending with ‘\_thetacut0.05’), which in its raw form contains large high-k theory tails. Therefore, we also provide “rotated” measurements (data, window, covariance), for which the window matrix is more compact, at the price of marginalizing over some templates, called “rotation systematics” in the following.
The file naming convention for the corresponding window matrices is: `window_spectrum-poles_{tracer}_{region}_z{zrange[0]:.1f}-{zrange[1]:.1f}{thetacut}.h5`.

The power spectrum multipoles corrected for the radial integral constraint (RIC) and angular mode removal (AMR) read `spectrum-poles-corrected_{tracer}_{region}_z{zrange[0]:.1f}-{zrange[1]:.1f}{thetacut}.h5`. The RIC is the result of the so-called ‘shuffling’ technique to assign data redshifts to the random catalogs. The AMR (called Angular Integral Constraint - AIC in [DESI 2024 II: Sample Definitions, Characteristics, and Two-point Clustering Statistics](https://ui.adsabs.harvard.edu/abs/2025JCAP...07..017A/abstract)){: target=’\_blank’} is caused by the overfitting of imaging systematic weights. Both RIC and AMR impact low k-modes; they were estimated from mocks (RIC from EZmocks, AMR from Abacus mocks) and compensated for in the power spectrum measurements. The window matrices are left unchanged.

The ‘rotated’ power spectrum multipoles read `spectrum-poles-rotated_{tracer}_{region}_z{zrange[0]:.1f}-{zrange[1]:.1f}_thetacut0.05.h5`. Rotation is designed to make the window matrix related to the power spectrum measurements more compact. This rotation is only applied to measurements with θ-cut, for which the original window matrix has large high-k theory tails. The technique is described in [Pinon _et al._ (2024)](https://ui.adsabs.harvard.edu/abs/2025JCAP...01..131P/abstract). The file format is similar to raw power spectrum measurements `spectrum-poles-rotated_{tracer}_{region}_z{zrange[0]:.1f}-{zrange[1]:.1f}_thetacut0.05.h5`. Corresponding rotated window matrices are provided as `window_spectrum-poles-rotated_{tracer}_{region}_z{zrange[0]:.1f}-{zrange[1]:.1f}_thetacut0.05.h5`, and the file format is similar to that of raw window matrices.

The ‘rotated’ and ‘corrected’ (for RIC, AMR) power spectrum multipoles read `spectrum-poles-rotated-corrected_{tracer}_{region}_z{zrange[0]:.1f}-{zrange[1]:.1f}_thetacut0.05.h5`. They represent the fiducial power spectrum measurements.

#### data/templates\_spectrum/ [¶](https://data.desi.lbl.gov/doc/releases/dr1/vac/full-shape-bao-clustering/\#datatemplates_spectrum "Permanent link")

`data/templates_spectrum/` contains power spectrum templates for systematics.
Templates for the radial integral constraint (RIC) read `template_ric_spectrum-poles_{tracer}_{region}_z{zrange[0]:.1f}-{zrange[1]:.1f}{thetacut}.h5` and `template_ric_spectrum-poles-rotated_{tracer}_{region}_z{zrange[0]:.1f}-{zrange[1]:.1f}_thetacut0.05.h5` (without and with rotation, respectively). These templates were obtained by fitting ∑n∈{−5,−3,−2}ankn to the difference of EZmock power spectra (with and without RIC).
Templates for the angular mode removal (AMR) read `template_amr_spectrum-poles_{tracer}_{region}_z{zrange[0]:.1f}-{zrange[1]:.1f}{thetacut}.h5` and `template_amr_spectrum-poles-rotated_{tracer}_{region}_z{zrange[0]:.1f}-{zrange[1]:.1f}_thetacut0.05.h5` (without and with rotation, respectively).
The corrected power spectrum multipoles `spectrum-poles-corrected_{tracer}_{region}_z{zrange[0]:.1f}-{zrange[1]:.1f}{thetacut}.h5` and `spectrum-poles-rotated-corrected_{tracer}_{region}_z{zrange[0]:.1f}-{zrange[1]:.1f}_thetacut0.05.h5` are obtained by subtracting these RIC and AMR templates from `spectrum-poles_{tracer}_{region}_z{zrange[0]:.1f}-{zrange[1]:.1f}{thetacut}.h5` and `spectrum-poles-rotated_{tracer}_{region}_z{zrange[0]:.1f}-{zrange[1]:.1f}_thetacut0.05.h5`, respectively.

Templates for photometric systematics (non-zero for ELGs and QSOs only) are `template_photo_spectrum-poles_{tracer}_{region}_z{zrange[0]:.1f}-{zrange[1]:.1f}{thetacut}.h5` and `template_photo_spectrum-poles-rotated_{tracer}_{region}_z{zrange[0]:.1f}-{zrange[1]:.1f}{thetacut}.h5` (without and with rotation, respectively). The corresponding systematic covariance matrix is computed with a 0-centered Gaussian prior of standard deviation 0.2.

#### data/rotation/ [¶](https://data.desi.lbl.gov/doc/releases/dr1/vac/full-shape-bao-clustering/\#datarotation "Permanent link")

`data/rotation/` contains the rotation matrices, `rotation_spectrum-poles_{tracer}_{region}_z{zrange[0]:.1f}-{zrange[1]:.1f}_thetacut0.05.h5`, to obtain the rotated power spectrum measurements, window matrix, and covariance matrix from the raw ones.

#### data/recsym/ [¶](https://data.desi.lbl.gov/doc/releases/dr1/vac/full-shape-bao-clustering/\#datarecsym "Permanent link")

`data/recsym/correlation/` contains post-reconstruction correlation functions. File naming convention is `counts-recsym-smu_{tracer}_{region}_z{zrange[0]:.1f}-{zrange[1]:.1f}.h5` for the pair counts (DD, DS, SD, SS, RR, with the Landy-Szalay estimator). Correlation function multipoles are named `correlation-recsym-poles_{tracer}_{region}_z{zrange[0]:.1f}-{zrange[1]:.1f}.h5`. Corresponding (binning) window matrices are named `window_correlation-recsym-poles_{tracer}_{region}_z{zrange[0]:.1f}-{zrange[1]:.1f}.h5`.

#### data/covariance/ [¶](https://data.desi.lbl.gov/doc/releases/dr1/vac/full-shape-bao-clustering/\#datacovariance "Permanent link")

`data/covariance/EZmock/ffa/` contains the covariance as estimated from the raw power spectra and post-reconstruction correlation function of EZmocks (see See [EZmock](https://data.desi.lbl.gov/doc/releases/dr1/vac/full-shape-bao-clustering/#ezmock-directory) section).
The raw power spectrum covariance reads `covariance_spectrum-poles_{tracer}_{region}_z{zrange[0]:.1f}-{zrange[1]:.1f}{thetacut}.h5`.
The joint (raw power spectrum, post-reconstruction correlation) covariance reads `covariance_spectrum-poles+correlation-recon_{tracer}_{region}_z{zrange[0]:.1f}-{zrange[1]:.1f}{thetacut}.h5`
The joint (raw power spectrum, post-reconstruction BAO) covariance reads `covariance_spectrum-poles+bao-recon_{tracer}_{region}_z{zrange[0]:.1f}-{zrange[1]:.1f}{thetacut}.h5`.

File names with **spectrum-poles-rotated** ( _e.g._`covariance_spectrum-poles-rotated+bao-recon_{tracer}_{region}_z{zrange[0]:.1f}-{zrange[1]:.1f}{thetacut}.h5`) correspond to covariance matrices for the rotated power spectrum.

`covariance/RascalC/` contains semi-analytic covariance matrices for the post-reconstruction correlation function measurements. File naming convention is `covariance_correlation-recsym-poles_{tracer}_{region}_z{zrange[0]:.1f}-{zrange[1]:.1f}.h5`.

`covariance/syst/` contains the systematic covariance matrix accounting for the systematic shifts due to galaxy-halo connexion (modeled as HOD): `covariance_hod_spectrum-poles-rotated_{tracer}_{region}_z{zrange[0]:.1f}-{zrange[1]:.1f}{thetacut}.h5`, see [Findlay _et al._ (2025)](https://ui.adsabs.harvard.edu/abs/2025JCAP...09..007F/abstract) for details.

#### data/likelihood/ [¶](https://data.desi.lbl.gov/doc/releases/dr1/vac/full-shape-bao-clustering/\#datalikelihood "Permanent link")

`data/likelihood/` contains the set of (observable, window, covariance), with systematic contributions, with the fiducial Key Project scale cuts, including the post-reconstruction BAO part. We recommend these files for cosmological inference.

The θ-cut power-spectrum-only likelihood reads `likelihood_spectrum-poles_syst-rotation-hod-photo_{tracer}_{region}_z{zrange[0]:.1f}-{zrange[1]:.1f}_thetacut0.05.h5`.
The joint power spectrum - post-reconstruction BAO likelihood reads `likelihood_spectrum-poles+bao-recon_syst-rotation-hod-photo_{tracer}_{region}_z{zrange[0]:.1f}-{zrange[1]:.1f}_thetacut0.05.h5`.
These likelihoods, which we used for the cosmological inference, include correcting factors in the covariance matrix (Table 6 of [DESI 2024 II](https://ui.adsabs.harvard.edu/abs/2025JCAP...07..017A/abstract) and Sections 5.7 and 5.8 of [DESI 2024 V](https://ui.adsabs.harvard.edu/abs/2025JCAP...09..008A/abstract)), and systematic contributions for:

- galaxy-halo connexion (`hod`)
- rotation of the window matrix (`rotation`): analytic marginalization over the parameter s of Eq. 5.4 of [Pinon _et al._ (2024)](https://ui.adsabs.harvard.edu/abs/2025JCAP...01..131P/abstract).
- residual photometric systematics (`photo`)

The last two contributions are mostly off-diagonal, and increase the size of the diagonal of the covariance, which results in “odd-looking” error bars. Therefore, we also provide likelihoods without analytic marginalization for rotation of the window matrix (`rotation`) and residual photometric systematics (`photo`). The corresponding files are named `likelihood_spectrum-poles_syst-hod_{tracer}_{region}_z{zrange[0]:.1f}-{zrange[1]:.1f}_thetacut0.05.h5` and `likelihood_spectrum-poles+bao-recon_syst-hod_{tracer}_{region}_z{zrange[0]:.1f}-{zrange[1]:.1f}_thetacut0.05.h5` for the power spectrum-only and joint power spectrum - post-reconstruction BAO likelihoods, respectively. These files however include two new theory components: ‘rotation’ and ‘photo’, to marginalize over in the inference, with prior (diagonal) **covariance** given by ‘prior\_variance’.

Post-reconstruction BAO-only likelihoods are provided as `likelihood_bao-recon_syst_{tracer}_GCcomb_z{zrange[0]:.1f}-{zrange[1]:.1f}.h5` (files with ‘stat-only’ instead of ‘syst’ contain no systematic uncertainties). The BAO Ly-α likelihood (see [DESI 2024 IV](https://ui.adsabs.harvard.edu/abs/2025JCAP...01..124A)) is also provided for completeness.

ShapeFit likelihoods (see _e.g._ [Brieden _et al._ (2021)](https://ui.adsabs.harvard.edu/abs/2021JCAP...12..054B)) obtained by fitting the joint (rotated) power spectrum and post-reconstruction BAO are named `likelihood_shapefit_spectrum-poles-rotated+bao-recon_syst-rotation-hod-photo_{tracer}_GCcomb_z{zrange[0]:.1f}-{zrange[1]:.1f}_thetacut0.05.h5`.

Likelihoods for the post-reconstruction correlation function are named `likelihood_correlation-recon-poles_{tracer}_{region}_z{zrange[0]:.1f}-{zrange[1]:.1f}.h5`.

### data\_v1.2/ Directory [¶](https://data.desi.lbl.gov/doc/releases/dr1/vac/full-shape-bao-clustering/\#data_v12-directory "Permanent link")

These files were used for the BAO cosmological inference. We provide them for completeness, though we recommend using the v1.5 (default) version of the files.

- `data/recsym/correlation/` same structure as above.
- `data/covariance/RascalC/` same structure as above.
- `data/likelihood/` same structure as above.

### EZmock/ Directory [¶](https://data.desi.lbl.gov/doc/releases/dr1/vac/full-shape-bao-clustering/\#ezmock-directory "Permanent link")

`EZmock/ffa/spectrum/` contains power spectrum measurements `spectrum-poles_{tracer}_{region}_z{zrange[0]:.1f}-{zrange[1]:.1f}{thetacut}_{imock:d}.h5` for cutsky EZmocks with fast fiber assignment (FFA). They can directly be used to compute the EZmock-based covariance matrices `data/covariance/EZmock/ffa/covariance_spectrum-poles_{tracer}_{region}_z{zrange[0]:.1f}-{zrange[1]:.1f}{thetacut}.h5`. Format is the same as for the data files. Corresponding raw window matrices are provided, `window_spectrum-poles_{tracer}_{region}_z{zrange[0]:.1f}-{zrange[1]:.1f}{thetacut}.h5`.

`EZmock/ffa/recsym/correlation/` contains post-reconstruction correlation function measurements `correlation-recsym-poles_{tracer}_{region}_z{zrange[0]:.1f}-{zrange[1]:.1f}_{imock:d}.h5`. Format is the same as for the data files.

`EZmock/ffa/recsym/bao/` contains post-reconstruction BAO measurements (obtained from the correlation function) `bao-recsym_{tracer}_{region}_z{zrange[0]:.1f}-{zrange[1]:.1f}_{imock:d}.h5`. They can directly be used to compute the EZmock-based covariance matrices `covariance/EZmock/ffa/covariance_spectrum-poles+bao-recon_{tracer}_{region}_z{zrange[0]:.1f}-{zrange[1]:.1f}{thetacut}.h5`.

Note: EZmocks corresponding to the BGS\_BRIGHT-21.5 and ELG\_LOPnotqso samples are named BGS and ELG\_LOP, respectively.

### AbacusSummit/ Directory [¶](https://data.desi.lbl.gov/doc/releases/dr1/vac/full-shape-bao-clustering/\#abacussummit-directory "Permanent link")

`AbacusSummit/complete/spectrum` contains power spectrum measurements `spectrum-poles_{tracer}_{region}_z{zrange[0]:.1f}-{zrange[1]:.1f}{thetacut}_{imock:d}.h5` for Abacus SecondGen complete cutsky mocks. Format is the same as for the data files. Corresponding raw window matrices are provided, `window_spectrum-poles_{tracer}_{region}_z{zrange[0]:.1f}-{zrange[1]:.1f}{thetacut}.h5`.

Similar files are provided for mocks with fast fiber assignment (FFA) `AbacusSummit/ffa/spectrum` and alt-MTL `AbacusSummit/altmtl/spectrum`.

`AbacusSummit/complete/recsym/correlation` contains post-reconstruction correlation function measurements `correlation-recsym-poles_{tracer}_{region}_z{zrange[0]:.1f}-{zrange[1]:.1f}_{imock:d}.h5`. Format is the same as for the data files.

Note: “complete” and “ffa” AbacusSummit mocks corresponding to the ELG\_LOPnotqso sample are named ELG\_LOP.

## Contact [¶](https://data.desi.lbl.gov/doc/releases/dr1/vac/full-shape-bao-clustering/\#contact "Permanent link")

Contact [Ashley J. Ross](mailto:ashley.jacob.ross@gmail.com) and [Arnaud de Mattia](mailto:arnaud.de-mattia@cea.fr) for questions about this catalog.
