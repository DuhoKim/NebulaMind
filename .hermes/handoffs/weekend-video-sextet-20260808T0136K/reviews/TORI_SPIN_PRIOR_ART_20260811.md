# TORI SPIN PRIOR-ART CUSTODY — 2026-08-11

- Custody timestamp: 2026-08-11T13:14:43Z
- Scope: facts-only answers to the two prior-art questions and verification of the two proposed confirmatory axes.
- Decision boundary: this receipt does **not** decide whether a new study is worth doing. Nothing is published or accepted; Duho decides. Lana and Kun apply these facts to their gate.
- Method: full methods/results and associated primary artifacts were read. Abstract-only characterizations were not used as evidence for methods.

## Plain findings

1. **Patel & Desmond (2024) do not generate new handedness labels from galaxy imaging.** They collate and statistically reanalyse seven pre-existing handedness-label catalogues.[2] Their methods explicitly say they “accept at face value the annotation of the utilised datasets by other authors.” They do not run an image classifier or annotator.[2]
2. **Patel & Desmond do not themselves perform Lana's requested mirrored-input control.** Their compilation includes two already-published Ganalyzer products, one made from mirrored inputs (“GAN M”) and one from unmirrored inputs (“GAN NM”), but those classifications came from McAdam & Shamir.[2] Patel & Desmond compare/reanalyse those inherited labels; they do not send images or their mirrors through a classifier of their own.[2]
3. **Their anisotropy statistics are broad, free-axis searches, not confirmatory tests fixed at Longo's or Shamir's published axes.** Their Bayesian monopole/dipole/quadrupole and hemisphere models give the relevant axes full-sky priors.[2] Their frequentist method refits 50,000 shuffled mock catalogues and is limited to the monopole-plus-dipole model; the methods explicitly say it does not include a quadrupole, and they do not describe a separate frequentist hemisphere analysis.[2]
4. “The 2024 Hyper Suprime-Cam symmetry paper” is ambiguous because two close 2024 records exist:[4][8]
   - Lior Shamir, *Asymmetry in Galaxy Spin Directions: A Fully Reproducible Experiment Using HSC Data*, **Symmetry 16, 1389** (2024), DOI `10.3390/sym16101389`.[4]
   - Richard Stiskalek & Harry Desmond, *Symmetry in Hyper Suprime-Cam Galaxy Spin Directions*, **Research Notes of the AAS 8, 281** (2024), DOI `10.3847/2515-5172/ad8fb1`.[8]
5. **Stiskalek & Desmond (2024) is another label-level reanalysis.** It expressly assumes Shamir's spin labels are correct and applies Patel & Desmond's statistical model.[9] It does not classify images and has no mirrored-input classifier control.[9]
6. **Shamir (2024) does generate its own HSC labels from downloaded HSC images with deterministic Ganalyzer and reports rerunning the annotation after mirroring every image.** This is close to the image-level component, but the paper does not document mirror antisymmetry as an enforced identity, does not publish paired original/mirror outputs or a mismatch rate, and says only that mirroring “does not change the annotation.”[5] The paper does not say that the classified files were raw FITS or establish end-to-end orientation custody.[5] Its public reproduction page supplies label tables and sky-statistic source code, not the HSC image cutouts or the annotation program/configuration used in this run.[6]
7. **Neither 2024 HSC paper runs preregistered fixed-axis tests at Longo `(l,b)=(52°,68.5°)` or Shamir `(RA,Dec)=(132°,32°)`.** Shamir scans integer-valued sky coordinates and reports the maximizer; Stiskalek & Desmond fit free dipole/quadrupole directions.[5][9]
   No preregistration record is identified in either paper.[5][9]
8. Two earlier adjacent primary records matter to the narrow “has the image pipeline been built?” question:
   - Tadaki et al. (2020) built an HSC CNN, converted HSC FITS cutouts to JPEG, and paired horizontal flips with opposite S/Z training labels.[10] It was not an enforced reflection-equivariant architecture and did not perform a sky-axis anisotropy test.[10][11]
   - Jia, Zhu & Pen (2023) built CE-ResNet, an explicitly reflection-equivariant S/Z classifier.[11] It used SDSS/DESI JPEGs and Galaxy Zoo 1 training labels, not HSC raw FITS, and did not perform a dipole/quadrupole/fixed-axis anisotropy analysis.[11]
9. **The quoted axes resolve correctly to the primary papers.** Longo reports Galactic `(l,b)=(52°,68.5°)`.[12] Shamir reports equatorial `(RA,Dec)=(132°,32°)`, with the RA 1-sigma interval `107°–179°`.[13]
10. **The correction is confirmed.** ApJ 907, 123 is by Masanori Iye, Masafumi Yagi, and Hideya Fukumoto—not Hayashi.[14] The DOI is `10.3847/1538-4357/abb3bb`.[14]

## Question 1 — actual scope of Patel & Desmond (2024)

### Exact record

Richard Patel & Harry Desmond, “No evidence for anisotropy in galaxy spin directions,” *Monthly Notices of the Royal Astronomical Society* **534**(2), 1553–1563 (2024).[1][2]

- Journal DOI: https://doi.org/10.1093/mnras/stae2158 [1]
- Full arXiv record used for method custody: arXiv:2404.06617v3, https://arxiv.org/abs/2404.06617v3 [2]
- Versioned full text: https://arxiv.org/pdf/2404.06617v3 [2]
- Authors' public analysis repository: https://github.com/harrydesmond/GalaxySpinAnisotropy [3]

The arXiv record says v3 was submitted 2024-09-11 and adds the published journal reference and DOI.[2] The journal page and arXiv v3 identify the same paper, authors, and DOI.[1][2]

### What they ingest

Their methods state:

> “We collate all publicly available image data that has been used in the literature to test the isotropy of galaxy spins. Beyond the raw data, this test requires an algorithm to calculate the spin direction of each galaxy (annotation). Any difference in results for fixed data could arise either from the annotation method or the statistics with which the annotated data is tested for anisotropy. Here we accept at face value the annotation of the utilised datasets by other authors, and ask merely whether the statistics of the annotated datasets provide compelling evidence for anisotropy.”[2]

Table 1 lists seven inherited catalogues: Longo, Iye, SDSS DR7, GAN M, GAN NM, Shamir, and PS DR1.[2]

The rows are catalogues of sky positions and already-assigned spin signs.[2] Patel & Desmond describe who made each annotation—for example Longo's manual labels or Ganalyzer/SpArcFiRe labels from the other catalogue papers.[2] They do not describe running any of those images through a new annotator or classifier.[2]

The GitHub artifact matches that scope.[3] Its README says the work provides code for reproducing the anisotropy statistics; the checked repository contains statistical scripts and catalogue data, not an image-labeling model or image-classification stage.[3]

**Answer to the label-provenance branch:** Patel & Desmond reanalyse existing published labels.[2] They do not generate their own handedness classifications from imaging.[2]

### Mirrored-input control

Patel & Desmond's compilation contains an inherited mirror experiment:[2]

> “`GAN M' is almost identical to `GAN NM' except the galaxy images were mirrored before being fed into the annotation algorithm, in order to quantify the level of asymmetry in this algorithm.”[2]

Their Table 1 identifies both GAN catalogues as products of the same prior McAdam & Shamir paper, with 139,852 and 138,940 labels respectively.[2] Patel & Desmond later cross-match the inherited catalogues and analyse their disagreements.[2] That is a comparison of pre-existing output labels, not a fresh mirrored-input run through a Patel–Desmond classifier.[2]

**Answer to the mirror-control branch:** no Patel–Desmond image classifier exists in this paper, so they do not perform the requested same-pipeline original-versus-mirror classification.[2][3] Their statistical input set does contain mirrored and unmirrored Ganalyzer products created by other authors.[2]

### Axis freedom and look-elsewhere scope

Their Bayesian models are not fixed-axis confirmation tests.[2] The methods state:

> “We adopt uniform priors on $M$, $D\ge0$ and $Q\ge0$, and a uniform prior on area element for the $\vec{d}$, $\vec{q}_1$ and $\vec{q}_2$ vectors across the full sky.”[2]

The quadrupole likewise uses two free directions with priors uniform over the sphere. The alternative hemisphere model has its own free unit axis with a uniform prior on area element.[2]

Their frequentist method creates 50,000 mock catalogues with the observed galaxy positions and randomized spins, refits each mock, and obtains the null p-value from the resulting fitted-parameter distribution.[2] That methods paragraph says: “In this case we do not consider a quadrupole.” It does not describe a separate frequentist hemisphere run.[2]

The methods then state:

> “Note that both of our methods account for the ‘look-elsewhere effect’ that comes into play when testing multiple hypotheses (in this case many possible dipole directions). In the frequentist approach this is accounted for by calculating significance with respect to mock data that has the same properties as the real data and has been processed identically, while in the Bayesian approach it is accounted for by the priors, which appropriately weight the probability that an axis should point in any particular direction.”[2]

The paper therefore covers free-axis Bayesian dipole, quadrupole, and hemisphere models, plus mock-calibrated frequentist monopole/dipole fitting.[2] Kun's description is correct that Patel & Desmond use both Bayesian and frequentist methods and account for axis freedom/look-elsewhere, but it is too broad if read as saying that every dipole, quadrupole, and hemisphere model was run in both frameworks.[2] None is a preregistered test evaluated only at Longo's or Shamir's published coordinates.[2]

## Question 2 — the 2024 Hyper Suprime-Cam records

### Candidate A: the paper published in *Symmetry*

Lior Shamir, “Asymmetry in Galaxy Spin Directions: A Fully Reproducible Experiment Using HSC Data,” *Symmetry* **16**(10), 1389 (2024).[4][5]

- DOI: https://doi.org/10.3390/sym16101389 [4]
- arXiv:2410.15269v1: https://arxiv.org/abs/2410.15269v1 [5]
- Versioned full text: https://arxiv.org/pdf/2410.15269v1 [5]
- Author's reproduction page: https://people.cs.ksu.edu/~lshamir/data/asymmetry_hsc/ [6]

#### Label generation

This paper does not merely reanalyse someone else's labels.[5] Its methods say that 101,415 HSC DR3 galaxy images were downloaded and:[5]

> “After the images of all galaxies were downloaded, the galaxies were annotated by their direction of rotation. [...] Therefore, the entire process of annotating the galaxies was performed in a fully automatic manner, and without any human intervention except for inspection of the annotation. The spin directions of galaxies were annotated by the *Ganalyzer* algorithm...”[5]

It reports a final annotated dataset of 13,477 galaxies after Ganalyzer rejected about 86% of the HSC image sample as lacking an identifiable spin direction.[5]

The method is deterministic rather than learned:

> “*Ganalyzer* is a fully symmetric algorithm [...], and its simple and ‘mechanical’ nature allows to understand and control the way it works. The explainable nature of *Ganalyzer* makes it different from machine learning and deep neural network solutions.”[5]

#### What its mirror claim does and does not establish

The methods make an image-level mirror-control claim:[5]

> “The annotation was repeated also after mirroring all galaxy images to ensure that the analysis is symmetric, and that mirroring the galaxy images does not change the annotation.”[5]

This establishes that the paper reports a full mirrored-image rerun.[5] It does **not**, from the text or artifacts located here, establish all of Lana's stronger control requirements:[5][6]

- no formal identity such as `f(mirror(x)) = opposite(f(x))` is specified;[5]
- no per-object original/mirror output pairs are published on the reproduction page;[6]
- no mirror mismatch or exclusion/disagreement rate is reported;[5][6]
- the sentence “does not change the annotation” does not explain whether “annotation” means the image-relative S/Z label, an orientation-corrected physical label, or sample membership.

The public reproduction page offers catalogue/result tables and C++ programs for the statistical sky analyses.[6] It does not expose the 101,415 classified image cutouts or an executable/configuration that reproduces the HSC Ganalyzer labeling stage end to end.[6]

#### Raw FITS and orientation custody

The 2024 paper says only that HSC “images” were downloaded.[5] It does not identify their file format, FITS-to-display conversion, pixel-axis/WCS convention, cutout service, or orientation-preservation checks.[5]

The cited Ganalyzer program's own primary description states:

> “Currently, the supported file formats are TIFF, JPG, PPM, and BMP. In cases where the source images are in the FITS format, the images can be converted to lossless 8 or 16 bit TIFF format before being analyzed by Ganalyzer.”[7]

Therefore the reviewed record does not show Ganalyzer directly classifying raw FITS.[5][7]

It also does not document what conversion was used for this HSC run.[5]

Whether the 2024 run maintained end-to-end raw-FITS orientation custody does **not resolve** from the methods or public reproduction page.[5][6][7]

#### Axis test status

Shamir's method scans candidate axes rather than freezing a prior coordinate:[5]

> “In summary, all possible integer combinations of $(\alpha,\delta)$ are fitted to a cosine dependence with the directions of rotations of the galaxies.”[5]

The paper reports the coordinate that maximizes that scan.[5] It does not identify a preregistration, nor does it state a confirmatory test frozen at Longo `(52°,68.5°)` or Shamir `(132°,32°)`.[5]

### Candidate B: the paper whose title begins “Symmetry in Hyper Suprime-Cam...”

Richard Stiskalek & Harry Desmond, “Symmetry in Hyper Suprime-Cam Galaxy Spin Directions,” *Research Notes of the AAS* **8**(10), 281 (2024).[8][9]

- DOI: https://doi.org/10.3847/2515-5172/ad8fb1 [8]
- arXiv:2410.18884v3: https://arxiv.org/abs/2410.18884v3 [9]
- Versioned full text: https://arxiv.org/pdf/2410.18884v3 [9]

This short paper does not classify HSC images.[9] Its methods explicitly say:

> “We take the HSC DR3 data which matches that used by Shamir (2024). We assume that these spin assignments are correct; a direction-dependent bias in the assignment would be much more likely to introduce a spurious dipole than spuriously remove a true one.”[9]

It applies the Patel & Desmond monopole/dipole/quadrupole model to Shamir's published HSC labels.[9] It introduces no image classifier, no original-versus-mirrored inputs, and no orientation-custody pipeline.[9]

Its dipole and quadrupole axes are fitted parameters, not frozen coordinates.[9] It reports the posterior constraints from those free-axis models and has no identified preregistration.[9]

### Adjacent image-classifier prior art

#### Tadaki et al. (2020): HSC CNN, reflected training pairs, no axis test

Ken-ichi Tadaki et al., “Spin Parity of Spiral Galaxies II: A catalogue of 80k spiral galaxies using big data from the Subaru Hyper Suprime-Cam Survey and deep learning,” *MNRAS* **496**, 4276–4286 (2020).

- DOI: https://doi.org/10.1093/mnras/staa1880 [10]
- arXiv:2006.13544v1: https://arxiv.org/abs/2006.13544v1 [10]

This is a true HSC image classifier. It states:

> “We convert FITS images of galaxies to Joint Photographic Experts Group (JPEG) format by using STIFF software... In this paper, we simply use JPEG images...”[10]

For S/Z balance and reflection augmentation:

> “We add horizontally flipped images of Z-spirals and S-spirals to the S-spiral and Z-spiral classes, resulting in the same number in S-spirals and Z-spirals. Flipping spiral galaxies is also important for making an unbiased training dataset.”[10]

This couples mirrored training images to opposite labels, but the model is a standard three-class CNN; the paper does not impose or prove exact output antisymmetry under reflection. Jia et al. later describe Tadaki's classifier as “not manifestly parity-even.”[11]

Tadaki et al. report global S/Z counts and trends with magnitude, redshift, size, and axis ratio. They do not perform a celestial dipole/quadrupole/hemisphere search or a fixed test at Longo's or Shamir's axis.[10]

#### Jia, Zhu & Pen (2023): enforced reflection equivariance, but JPEG/GZ1 and no axis test

He Jia, Hong-Ming Zhu & Ue-Li Pen, “Galaxy Spin Classification. I. Z-wise versus S-wise Spirals with the Chirality Equivariant Residual Network,” *The Astrophysical Journal* **943**, 32 (2023).

- DOI: https://doi.org/10.3847/1538-4357/aca8aa [11]
- arXiv:2210.04168v2: https://arxiv.org/abs/2210.04168v2 [11]

This paper implements the closest located match to the architecture-level mirror condition:

> “The proposed Chirality Equivariant Residual Network (CE-ResNet) is manifestly equivariant under a reflection of the input image, which guarantees that there is no inherent asymmetry between the Z-wise and S-wise probability estimators.”[11]

Its architecture evaluates the same estimator on the original and vertically reflected image:

> “The network predicts the scores of Z-Spirals and Non-Spirals from the original images, and the scores of S-Spirals and Non-Spirals from the flipped images, which guarantees that it is equivariant under a parity inversion.”[11]

However, it trains from GZ1 labels and uses display cutouts:

> “We train the model with Sloan Digital Sky Survey (SDSS) images, with the training labels given by the Galaxy Zoo 1 (GZ1) project.”[11]

> “We obtain the jpeg images of these galaxies from both SDSS and DESI surveys using the Legacy Surveys Sky Viewer tool.”[11]

It does not use HSC raw FITS, and no dipole/quadrupole/hemisphere/fixed-axis anisotropy test appears in its methods or results.[11]

### Element-by-element coverage matrix

| Design element in Lana's description | Patel & Desmond 2024 | Shamir HSC 2024 | Stiskalek–Desmond HSC 2024 | Tadaki HSC 2020 | Jia CE-ResNet 2023 |
|---|---|---|---|---|---|
| Generates new S/Z labels from images | No | Yes | No | Yes | Yes |
| Machine-learned classifier | No | No; deterministic Ganalyzer | No | Yes; CNN | Yes; CE-ResNet |
| Same-pipeline mirrored inputs | No fresh run; inherits GAN M/NM labels | Claims full mirrored rerun | No | Uses flipped training augmentation | Yes, by construction |
| Reflection antisymmetry enforced in architecture | No | Not specified/proved as an enforced identity | No | No | Yes |
| Raw FITS classified directly | No | Does not resolve; Ganalyzer cannot directly ingest FITS | No | No; FITS converted to JPEG | No; SDSS/DESI JPEG |
| End-to-end image-orientation custody documented | No | Does not resolve | No | Conversion documented; full custody not framed as a control | No |
| Preregistered fixed-axis test | No | No identified preregistration; all-sky scan | No identified preregistration; free axes | No axis test | No axis test |
| Tests Longo and Shamir axes as frozen confirmations | No | No | No | No | No |

This matrix is a scope comparison only. It is not a recommendation or worth-doing verdict.

## Axis custody

### Longo axis

Michael J. Longo, “Detection of a dipole in the handedness of spiral galaxies with redshifts z ~ 0.04,” *Physics Letters B* **699**, 224–229 (2011).

- DOI: https://doi.org/10.1016/j.physletb.2011.04.008 [12]
- arXiv:1104.2815v1: https://arxiv.org/abs/1104.2815v1 [12]
- Versioned full text: https://arxiv.org/pdf/1104.2815v1 [12]

The full paper states:

> “The best fit was found at $(\alpha_A,\delta_A)=(217^\circ,32^\circ)$, or $(l,b)=(52^\circ,68.5^\circ)$ in Galactic coordinates.”[12]

**Axis result:** Lana's Longo coordinate is exact as stated, in Galactic longitude and latitude.

### Shamir axis and RA interval

Lior Shamir, “Handedness asymmetry of spiral galaxies with z<0.3 shows cosmic parity violation and a dipole axis,” *Physics Letters B* **715**, 25–29 (2012).

- DOI: https://doi.org/10.1016/j.physletb.2012.07.054 [13]
- arXiv:1207.5464v1: https://arxiv.org/abs/1207.5464v1 [13]
- Versioned full text: https://arxiv.org/pdf/1207.5464v1 [13]

The method reports:

> “The most likely dipole axis was found at $RA=132^\circ$, $DEC=32^\circ$.”[13]

For uncertainty, it states:

> “The most likely dipole axis is at $RA=132^\circ$, and the 1$\sigma$ error range for the dipole is between RA $107^\circ$ and $179^\circ$.”[13]

**Axis result:** Lana's Shamir coordinate and RA one-sigma interval are exact as stated.

## Corrected rebuttal citation

Masanori Iye, Masafumi Yagi & Hideya Fukumoto, “Spin Parity of Spiral Galaxies. III. Dipole Analysis of the Distribution of SDSS Spirals with 3D Random Walk Simulations,” *The Astrophysical Journal* **907**, 123 (2021).

- DOI: https://doi.org/10.3847/1538-4357/abb3bb [14]
- arXiv:2011.00662v1: https://arxiv.org/abs/2011.00662v1 [14]
- Versioned full text: https://arxiv.org/pdf/2011.00662v1 [14]

The primary journal record lists the authors as Masanori Iye, Masafumi Yagi, and Hideya Fukumoto.[14] No Hayashi is an author of ApJ 907, 123. Masao Hayashi is an author of the separate 2020 Tadaki et al. HSC catalogue paper, which likely explains how the names could be conflated.[10]

## Items that do not resolve from the reviewed primary record

- Shamir HSC 2024 does not say whether its downloaded HSC files were FITS, JPEG, TIFF, or another format before Ganalyzer processed them.
- It does not publish paired original/mirror classifications or define the semantics of “does not change the annotation,” so exact per-image antisymmetry cannot be audited from the posted artifacts.
- Its reproduction page does not expose the HSC cutouts or the exact annotation executable/configuration used for the 2024 run.
- Neither 2024 HSC paper identifies a preregistration record.
- None of the five method families in the coverage matrix combines all of: raw-FITS custody, enforced reflection-equivariant labeling, and preregistered fixed tests at both published axes.
- This receipt did not attempt to establish whether unpublished/private implementations exist.

## Facts-only handoff

Patel & Desmond's blocker is label-level: it covers the statistical reanalysis of other authors' handedness catalogues, including one mirrored and one non-mirrored Ganalyzer product, but not a newly built image classifier controlled from raw survey pixels through mirrored classification.

The HSC literature shows that major **components** already exist separately: own HSC labels plus a reported mirror rerun (Shamir 2024), HSC FITS-to-JPEG CNN classification with flipped-label augmentation (Tadaki et al. 2020), and an architecture with exact reflection equivariance (Jia et al. 2023). The reviewed papers do not combine those components with raw-FITS orientation custody and preregistered fixed tests at Longo's and Shamir's published axes.

That is the prior-art custody result. Whether the remaining combination is scientifically or operationally worth doing is outside Tori's authority here.

## Sources

[1] Patel & Desmond (2024), journal version, DOI `10.1093/mnras/stae2158`: https://doi.org/10.1093/mnras/stae2158

[2] Patel & Desmond, arXiv:2404.06617v3, full record/text: https://arxiv.org/abs/2404.06617v3 ; https://arxiv.org/pdf/2404.06617v3

[3] Patel & Desmond public analysis repository: https://github.com/harrydesmond/GalaxySpinAnisotropy

[4] Shamir (2024), *Symmetry* 16, 1389, DOI `10.3390/sym16101389`: https://doi.org/10.3390/sym16101389

[5] Shamir, arXiv:2410.15269v1, full record/text: https://arxiv.org/abs/2410.15269v1 ; https://arxiv.org/pdf/2410.15269v1

[6] Shamir HSC reproduction page: https://people.cs.ksu.edu/~lshamir/data/asymmetry_hsc/

[7] Shamir (2011), “Ganalyzer,” DOI `10.1088/0004-637X/736/2/141`: https://doi.org/10.1088/0004-637X/736/2/141

[8] Stiskalek & Desmond (2024), RNAAS 8, 281, DOI `10.3847/2515-5172/ad8fb1`: https://doi.org/10.3847/2515-5172/ad8fb1

[9] Stiskalek & Desmond, arXiv:2410.18884v3, full record/text: https://arxiv.org/abs/2410.18884v3 ; https://arxiv.org/pdf/2410.18884v3

[10] Tadaki et al. (2020), DOI `10.1093/mnras/staa1880`, arXiv:2006.13544v1: https://doi.org/10.1093/mnras/staa1880 ; https://arxiv.org/abs/2006.13544v1 ; https://arxiv.org/pdf/2006.13544v1

[11] Jia, Zhu & Pen (2023), DOI `10.3847/1538-4357/aca8aa`, arXiv:2210.04168v2: https://doi.org/10.3847/1538-4357/aca8aa ; https://arxiv.org/abs/2210.04168v2 ; https://arxiv.org/pdf/2210.04168v2

[12] Longo (2011), DOI `10.1016/j.physletb.2011.04.008`, arXiv:1104.2815v1: https://doi.org/10.1016/j.physletb.2011.04.008 ; https://arxiv.org/abs/1104.2815v1 ; https://arxiv.org/pdf/1104.2815v1

[13] Shamir (2012), DOI `10.1016/j.physletb.2012.07.054`, arXiv:1207.5464v1: https://doi.org/10.1016/j.physletb.2012.07.054 ; https://arxiv.org/abs/1207.5464v1 ; https://arxiv.org/pdf/1207.5464v1

[14] Iye, Yagi & Fukumoto (2021), DOI `10.3847/1538-4357/abb3bb`, arXiv:2011.00662v1: https://doi.org/10.3847/1538-4357/abb3bb ; https://arxiv.org/abs/2011.00662v1 ; https://arxiv.org/pdf/2011.00662v1
