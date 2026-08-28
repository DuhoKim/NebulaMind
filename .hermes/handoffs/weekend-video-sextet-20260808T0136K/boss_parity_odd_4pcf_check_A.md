# Check A — Public BOSS parity-odd 4PCF numerical products and code

Checked 2026-08-11T09:25:06Z. This is a custody/product audit, not a scientific re-analysis. I inspected primary-paper availability statements, the live GitHub/GitLab API trees, live host headers, the Zenodo record/API/concept-version endpoint, and (by HTTP range requests only) ZIP/NPZ central directories and small headers/README members. I did **not** download the large numerical archives.

## Bottom line

1. **Yes: the Philcox BOSS CMASS parity-odd 4PCF measurement vectors are public.** The two observed NGC/SGC raw ENCORE text files, disconnected terms, and analytic covariance pickle files are in [`oliverphilcox/Parity-Odd-4PCF`](https://github.com/oliverphilcox/Parity-Odd-4PCF/tree/main/data). The 2,048-mock computed 4PCF ensembles are also public, but are **live Dropbox `.npz` files linked by the README**, not files in the GitHub tree.
2. **The Hou–Slepian BOSS paper itself does not point to a public download of its measured CADENZA 4PCF vectors/covariance outputs.** Its data statement points to the SDSS input BOSS and MultiDark-Patchy products. The live SDSS directory is a listing of galaxy/random catalogue tarballs, not measured `zeta_4pcf` or covariance products. Its CADENZA measurement code was only “available … upon reasonable request”; a later Slepian-led primary paper explicitly calls CADENZA “a proprietary GPU code.”
3. **Yes: a later independent/reproduction release is archival and very complete.** Krolewski et al. deposit both 10-bin and 18-bin raw BOSS and mock 4PCF outputs, analytic covariance files, χ² products, and analysis code at [Zenodo record 12537418](https://zenodo.org/records/12537418), DOI [`10.5281/zenodo.12537418`](https://doi.org/10.5281/zenodo.12537418), under **CC-BY-4.0**. The one deposited ZIP is exactly **10,622,877,459 bytes**, SHA-256 `e061d66b2120d4d070712920b716b0e44f02fb5fd9a18143ed73429ba7d71388`. The concept DOI is `10.5281/zenodo.12537417`; the versions API reports **one** version.
4. **Mocks are not limited to galaxy catalogues.** Philcox’s Dropbox and Krolewski’s Zenodo both contain *computed 4PCFs per mock*. The separately shipped covariance artifacts in both analysis releases are analytic Gaussian covariances; the sample/mock covariances are formed from the computed mock ensembles in the notebooks/scripts. I found no separately named empirical/mock covariance product in either complete release listing.
5. **Ordering/binning are recoverable and in key cases explicit.** ENCORE text headers state the row/column convention, bin count/range, and the `-i*zeta` odd-mode convention. The Philcox notebooks specify the odd/angular and radial cuts, `ravel()` ordering, and eigenvector compression. Krolewski’s paper specifies the 10/18-bin analysis dimensions and the release contains the same self-describing ENCORE headers.

---

## 1. Philcox 2022: actual public BOSS vectors and computed mock products

### Primary-paper statement

Primary source: O. H. E. Philcox, *Probing parity violation with the four-point correlation function of BOSS galaxies*, [arXiv:2206.04227 PDF](https://arxiv.org/pdf/2206.04227), journal page [Phys. Rev. D 106, 063501](https://journals.aps.org/prd/abstract/10.1103/PhysRevD.106.063501).

Verbatim paper text:

> “The data used to produce all plots are publicly available at [68]. This includes the measurements of the 4PCF in observational data and Patchy mocks, as well as the relevant covariance matrices.”

The cited URL is [`https://github.com/oliverphilcox/Parity-Odd-4PCF`](https://github.com/oliverphilcox/Parity-Odd-4PCF). The paper also states:

> “The ENCORE code (version 1.0) used to compute NPCFs is publicly available at github.com/oliverphilcox/encore.”

### What is actually in the GitHub tree (not merely README metadata)

Live repository: [`oliverphilcox/Parity-Odd-4PCF`](https://github.com/oliverphilcox/Parity-Odd-4PCF). Full live tree API: [`/git/trees/main?recursive=1`](https://api.github.com/repos/oliverphilcox/Parity-Odd-4PCF/git/trees/main?recursive=1). At inspection the tree was untruncated and resolved to SHA `04606edd621c7e34dd34895fef546c1980b4f275`.

Observed-data and covariance files in `data/` include:

| Actual GitHub path | GitHub blob size |
|---|---:|
| [`data/boss_cmassN.zeta_4pcf.txt`](https://raw.githubusercontent.com/oliverphilcox/Parity-Odd-4PCF/main/data/boss_cmassN.zeta_4pcf.txt) | 208,573 B |
| [`data/boss_cmassS.zeta_4pcf.txt`](https://raw.githubusercontent.com/oliverphilcox/Parity-Odd-4PCF/main/data/boss_cmassS.zeta_4pcf.txt) | 208,663 B |
| `data/boss_cmassN.zeta_discon_4pcf.txt` | 130,330 B |
| `data/boss_cmassS.zeta_discon_4pcf.txt` | 130,603 B |
| `data/gaussian_cov_patchy_ngc.cov` | 47,874,880 B |
| `data/gaussian_cov_patchy_sgc.cov` | 47,175,444 B |

There are also 2PCF/3PCF inputs and parity-odd theory templates. Thus this is a real numerical vector release, not only plot images or catalogues.

### Self-described format, binning, and ordering

The first six lines of each observed 4PCF file say verbatim:

> `## Order: 5`  
> `## Bins: 10`  
> `## Minimum Radius = 2.00e+01`  
> `## Maximum Radius = 1.60e+02`  
> `## Format: Row 1 = radial bin 1, Row 2 = radial bin 2, Row 3 = radial bin 3, Rows 4+ = zeta_l1l2l3^abc. For odd parity multiplets, we give the value of -i*zeta_l1l2l3^abc.`  
> `## Columns 1-3 specify the (l1, l2, l3) multipole triplet`

Each file has 111 multiplet rows and all 120 strictly ordered radial-bin triples from 10 bins. The analysis notebook [`BOSS Odd-Parity 4PCF (CS template).ipynb`](https://github.com/oliverphilcox/Parity-Odd-4PCF/blob/main/BOSS%20Odd-Parity%204PCF%20(CS%20template).ipynb) selects:

```python
radial_filt = ((radii[1]-radii[0])>1.9*Delta_r)&((radii[2]-radii[1])>1.9*Delta_r)
ang_filt = ((ells[0]+ells[1]+ells[2])%2==1)&(ells[0]<=ell_max)&(ells[1]<=ell_max)&(ells[2]<=ell_max)
filt_flat_fourpcf_bossN = fourpcf_bossN[ang_filt][:,radial_filt].ravel()
```

With `ell_max=4`, this gives 23 odd multiplets × 56 radial triples = **1,288 components**. Direct inspection of the released small `ells`/`bins` arrays shows multiplet-major flattening with the radial combination varying fastest; the radial triple list itself is lexicographic with the third bin varying fastest. The first selected triples are `(0,2,4), (0,2,5), …`; the first selected multiplets are `(1,1,1), (1,2,2), (1,3,3), …`.

Compression is **specified in the notebook, not shipped as a standalone compressed vector**. Verbatim notebook markdown:

> “Data are projected onto the eigenvectors of the *model* inverse covariance matrix.”

It defines `v = U^T zeta`, orders eigenvectors by inverse variance, and tests `N_eigs = [10,50,100,250]`. The raw BOSS files remain uncompressed.

### Computed mock products: live Dropbox files, not just mock catalogues

The repository README links these exact live files:

* [`all_patchy2048_fourpcf.npz`](https://www.dropbox.com/s/594iol702s7gk86/all_patchy2048_fourpcf.npz?dl=1) — live final response length **707,798,836 B**, ETag `1644076553294492d`.
* [`all_nseries-patchy2048_fourpcf.npz`](https://www.dropbox.com/s/r5ezfez15ou93ws/all_nseries-patchy2048_fourpcf.npz?dl=1) — **353,903,968 B**, ETag `1644076582804875d`.

The live GitHub tree does **not** contain either `.npz`; it contains only the README links. Range-only inspection of the actual NPZ central directories and NumPy headers found:

`all_patchy2048_fourpcf.npz` (stored/uncompressed ZIP members):

* `fourpcfN.npy`, `fourpcfS.npy`: `float64`, shape `(2048,111,120)` each;
* `fourpcfNdisc.npy`, `fourpcfSdisc.npy`: shape `(2048,69,120)` each;
* `ells.npy`: `(3,111)`; `radii.npy`, `bins.npy`: `(3,120)`.

`all_nseries-patchy2048_fourpcf.npz` contains `fourpcf.npy` `(2048,111,120)`, `fourpcfdisc.npy` `(2048,69,120)`, plus the same ordering arrays. These are **computed 4PCF ensembles**, not galaxy catalogues. The sample covariance used in the analysis is generated in the notebook with `np.cov(filt_flat_fourpcf*.T)`; the separately shipped `.cov` files are analytic Gaussian models loaded as pickled multiplet-block dictionaries.

### License/version custody

* [`oliverphilcox/Parity-Odd-4PCF`](https://github.com/oliverphilcox/Parity-Odd-4PCF): GitHub license API returns 404, no `LICENSE`/`COPYING` path in the full tree, and no releases or tags. **No explicit data/code license located.** The Dropbox products have no separate license statement exposed by their pages.
* [`oliverphilcox/encore`](https://github.com/oliverphilcox/encore): current master has an [MIT LICENSE](https://raw.githubusercontent.com/oliverphilcox/encore/master/LICENSE). There is a [GitHub `v1.0` release](https://github.com/oliverphilcox/encore/releases/tag/v1.0), published 2024-10-18 and pointing to commit `aa7a5b4d0f049e78a4e07aaba1d2f2a4376936c7` (commit date 2023-04-17). **Caution:** the full `v1.0` tag tree itself contains no LICENSE file; the MIT file is present on current master and should not be silently back-applied to the old snapshot without confirmation.

---

## 2. Hou et al. 2023 / Slepian group: input catalogues public; measured CADENZA vectors not located as a paper release

Primary source: J. Hou et al., *Measurement of parity-odd modes in the large-scale 4-point correlation function of SDSS BOSS DR12 CMASS and LOWZ galaxies*, [arXiv:2206.03625 PDF](https://arxiv.org/pdf/2206.03625), journal page [MNRAS 522, 5701](https://academic.oup.com/mnras/article/522/4/5701/7169316).

### Exact paper availability text

> “CODE AVAILABILITY  
> The GPU-accelerated code CADENZA used to compute the NPCFs is available from the corresponding author upon reasonable request.”

> “DATA AVAILABILITY  
> The datasets underlying this article are publicly available in the SDSS repository at https://data.sdss.org/sas/dr12/boss/lss/ [67]. This includes the BOSS data and MultiDark-Patchy mocks used to measure the 4PCF and covariance matrices.”

This wording makes the cited material’s role clear: BOSS data and mocks **used to measure** the 4PCF/covariance, not a statement that the derived vectors are deposited there.

### What the live SDSS primary listings actually contain

* [DR12 BOSS LSS index](https://data.sdss.org/sas/dr12/boss/lss/) lists observational galaxy/random FITS products such as `galaxy_DR12v5_CMASS_North.fits.gz` (138,873,951 B) and `galaxy_DR12v5_CMASS_South.fits.gz` (51,580,500 B), plus mock subdirectories.
* [DR12 MultiDark-Patchy index](https://data.sdss.org/sas/dr12/boss/lss/dr12_multidark_patchy_mocks/) currently lists ten tarballs only: galaxy-catalogue archives `Patchy-Mocks-DR12NGC-COMPSAM_V6C.tar.gz` (44,113,316,646 B) and `...SGC...` (16,714,664,947 B), plus random-catalogue x10/x20/x50/x100 tarballs.

No derived `zeta_4pcf`, `.cov`, `.npz`, or similar numerical measurement product appears in either live directory listing. This establishes that the paper-cited SDSS release is **catalogue-level**, not computed-4PCF-level. I did not locate a separate downloadable numerical supplement on the journal page or an author Zenodo/GitHub release tied to this original paper; this is a cautious absence finding, not proof that no author can provide private files.

### CADENZA status

The original paper offers CADENZA only on request, so it was not an unconditional public code release. A later Slepian-led primary paper, [arXiv:2508.09133v1](https://arxiv.org/html/2508.09133v1), states verbatim:

> “We use a proprietary GPU code, cadenza, to measure the 4PCF, based on the CPU code encore…”

GitHub repository search API queries for `CADENZA 4PCF` and `CADENZA Slepian` returned `total_count: 0`; that search result alone is not conclusive, but it is consistent with the explicit “proprietary” statement. The Slepian group page likewise describes CADENZA as ENCORE’s “GPU-based successor” without linking a source repository.

---

## 3. Krolewski et al. 2024: archival 10/18-bin BOSS + computed mocks + analytic covariance

Primary paper: A. Krolewski et al., *No evidence for parity violation in BOSS*, [arXiv:2407.03397v1 HTML](https://arxiv.org/html/2407.03397v1), [JCAP 08 (2024) 044](https://iopscience.iop.org/article/10.1088/1475-7516/2024/08/044).

Verbatim paper statement:

> “All data and code needed to reproduce the results in the paper is available at https://zenodo.org/doi/10.5281/zenodo.12537417.”

### Record-level metadata versus actual archive

* Version record: [`https://zenodo.org/records/12537418`](https://zenodo.org/records/12537418); DOI [`10.5281/zenodo.12537418`](https://doi.org/10.5281/zenodo.12537418).
* Concept DOI: [`10.5281/zenodo.12537417`](https://doi.org/10.5281/zenodo.12537417).
* [Record API](https://zenodo.org/api/records/12537418): created/published 2024-06-25; record-level license `cc-by-4.0`; one file `Parity-Odd-4PCF-regions.zip`, **10,622,877,459 B**, SHA-256 `e061d66b2120d4d070712920b716b0e44f02fb5fd9a18143ed73429ba7d71388`.
* [Versions API](https://zenodo.org/api/records/12537418/versions): `hits.total = 1`.
* [Actual archive preview](https://zenodo.org/records/12537418/preview/Parity-Odd-4PCF-regions.zip?include_deleted=0). Range-reading the ZIP central directory found 873 entries. This is an actual file listing, not just record metadata.

The deposited top-level README says verbatim:

> “We provide the 4PCF outputs, covariance matrices and code to reproduce all analysis in ‘No evidence for parity violation in BOSS.’”

> “Parity-odd four point functions for the data and mocks are in ‘out’.”

Representative actual archive entries and uncompressed ZIP-member sizes:

| Archive member | Size |
|---|---:|
| `cov/18bins-160Mpc-cmass-ngc-bessel_improved.jld2.cov` | 4,288,129,689 B |
| `cov/18bins-160Mpc-cmass-sgc-bessel_improved.jld2.cov` | 4,288,129,689 B |
| `out/18_bins/patchy_mocks_DR12CMASS.tar.bz2` | 444,559,361 B |
| `out/18_bins/patchy_mocks.tar.bz2` | 265,717,392 B |
| `out/10_bins/patchy_mocks.tar.bz2` | 149,492,365 B |
| `out/18_bins/boss_cmass_CMASS.tar.bz2` | 24,820,015 B |
| `out/18_bins/boss_cmass.tar.bz2` | 886,514 B |
| `out/10_bins/boss_cmass.tar.bz2` | 3,835,694 B |
| `out/18_bins/chi2_files/*.txt` and `out/10_bins/chi2_files/*.txt` | present |

The 18-bin README labels the computed mock products verbatim, including:

> `patchy_mocks = CMASSLOWZTOT NGC mocks (first 500 mocks)`  
> `patchy_mocks_DR12CMASS = CMASS NGC mocks (all 2048 mocks)`  
> `patchy_mocks_reg1_SGC = CMASSLOWZTOT SGC mocks (all 2048 mocks)`

The 10-bin README states:

> `boss_cmass=CMASSLOWZTOT data`  
> `patchy_mocks=CMASSLOWZTOT mocks (first 500 mocks)`

Thus the archive contains **computed mock 4PCFs**, not just the SDSS mock galaxy catalogues. The two large `.cov` files are the analytic covariance outputs described by the paper/repository (`read_cov.py` is supplied). No separately named sample/mock covariance artifact appears in the complete 873-entry tree; the mocks themselves are the released basis for empirical distributions/covariance.

### Binning, dimensions, ordering, and compression

Krolewski’s paper defines:

* “10-bin” case: 10 linearly spaced radial bins in `[20,160] h^-1 Mpc`, `(l_max, Delta)=(4,1)`, `N_dof=1288`;
* “18-bin” case: 18 linearly spaced radial bins in `[20,160] h^-1 Mpc`, `(l_max, Delta)=(4,0)`, `N_dof=18768`.

Small range-extracted members from the actual tarballs show self-describing ENCORE headers identical in structure to Philcox’s release. An actual regional 18-bin BOSS member begins:

> `## Order: 5`  
> `## Bins: 18`  
> `## Minimum Radius = 2.00e+01`  
> `## Maximum Radius = 1.60e+02`  
> `## Format: Row 1 = radial bin 1, Row 2 = radial bin 2, Row 3 = radial bin 3, Rows 4+ = zeta_l1l2l3^abc. For odd parity multiplets, we give the value of -i*zeta_l1l2l3^abc.`

The release therefore preserves the raw coefficient ordering in file headers rather than only a flattened undocumented vector. The paper uses the scalar `chi^2 = E^a (C_ana^-1)_ab E^b` as data compression; the release supplies raw 4PCFs, covariances, scripts, and χ² text products, not a single canonical compressed vector.

### GitHub is code-only; Zenodo is the numerical custody copy

Live author repo: [`akrolewski/Parity-Odd-4PCF-regions`](https://github.com/akrolewski/Parity-Odd-4PCF-regions), full [tree API](https://api.github.com/repos/akrolewski/Parity-Odd-4PCF-regions/git/trees/main?recursive=1). At inspection its 88-entry tree was untruncated, head SHA `b3f5c3a87390843415d38ee14584b83957eb2bab`; the same SHA is recorded in the deposited `.git` logs. The GitHub tree contains scripts, `data/`, and bundled ENCORE sources, but **no `out/` or `cov/` directories and no numerical 4PCF/covariance files**. It has no releases/tags and GitHub’s license endpoint returns 404. Therefore:

* do not treat the GitHub README’s product description as an actual numerical file listing;
* use Zenodo for the released numerical products and record-level CC-BY-4.0 license;
* use GitHub for the live analysis code only (with no separate repository license located).

---

## 4. Public code inventory and license status

| Code | Function/status | Primary evidence | License located? |
|---|---|---|---|
| [`oliverphilcox/encore`](https://github.com/oliverphilcox/encore) | Public CPU C++ isotropic NPCF estimator used for Philcox; `v1.0` release exists. | [paper](https://arxiv.org/pdf/2206.04227), [release](https://github.com/oliverphilcox/encore/releases/tag/v1.0) | Current master MIT; tagged v1.0 tree has no LICENSE file. |
| CADENZA | Slepian-group GPU measurement code; not a public source release. | Hou: “available … upon reasonable request”; [later primary paper](https://arxiv.org/html/2508.09133v1): “a proprietary GPU code.” | Proprietary statement; no public repo located. |
| [`oliverphilcox/Parity-Odd-4PCF`](https://github.com/oliverphilcox/Parity-Odd-4PCF) | Public analysis notebooks/templates plus BOSS vectors and analytic covariance files; mock NPZs linked externally. | Full [tree API](https://api.github.com/repos/oliverphilcox/Parity-Odd-4PCF/git/trees/main?recursive=1) | No license file/API license. |
| [`akrolewski/Parity-Odd-4PCF-regions`](https://github.com/akrolewski/Parity-Odd-4PCF-regions) | Public live analysis/estimator snapshot; numerical products are in Zenodo, not GitHub. | Full [tree API](https://api.github.com/repos/akrolewski/Parity-Odd-4PCF-regions/git/trees/main?recursive=1) | No GitHub license; Zenodo deposit record is CC-BY-4.0. |
| [`Socob/Analytic4PC`](https://gitlab.com/Socob/Analytic4PC) | Public Julia analytic parity-odd 4PCF covariance driver. README: “Julia code to calculate the ‘analytic 4-point covariance’ … used in arXiv:2206.03625, arXiv:2206.04227.” It writes `cov.jld2`, supplies `matrix_indices`, and converts to `.cov`. | [GitLab project/API](https://gitlab.com/api/v4/projects/Socob%2FAnalytic4PC) | Public visibility; no license field/file found, no releases/tags. |
| [`Moctobers/npcf_cov`](https://github.com/Moctobers/npcf_cov) | Public Python analytic connected-4PCF covariance implementation, not a 4PCF measurement code. The original Hou paper says the then-public implementation calculated parity-even covariance elements only. | [repo](https://github.com/Moctobers/npcf_cov), [tree API](https://api.github.com/repos/Moctobers/npcf_cov/git/trees/main?recursive=1) | No license file/API license; two-file tree. |

## Cautious absence statement

After checking both 2022/2023 primary papers and their journal pages, the Philcox GitHub/release links, the Hou/Slepian availability statements and author code locations, the SDSS SAS directories, Krolewski’s paper, Zenodo record/concept versions/archive preview, and the Krolewski GitHub tree:

* **Found:** public Philcox measured vectors; public computed Philcox mock 4PCFs; public Krolewski 10/18-bin measured and computed-mock outputs; public analytic covariances and analysis code.
* **Not located as a public product:** the original Hou/CADENZA measured numerical BOSS vector/covariance release, or CADENZA source.
* **Do not conflate:** SDSS catalogue archives with computed 4PCFs; GitHub README claims with actual GitHub file trees; analytic covariance artifacts with empirical mock covariances; arXiv/article reuse licenses with code/data licenses.
