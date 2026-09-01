# External human labels for BS-8f

## Executive finding

**NOT USABLE.** No examined Galaxy Zoo release supplies the required combination of (i) apparent spiral handedness on a defensible sample of the 49,211 accepted DR10.1-south objects and (ii) a known-answer error calibration for the same released human decision rule. Galaxy Zoo 1 (GZ1) has clockwise/anticlockwise votes, but its SDSS-selected footprint and bright target selection do not represent this population, and its repeat/mirror material does not estimate the frozen known-truth `epsilon`. Galaxy Zoo 2 (GZ2), Galaxy Zoo DECaLS (GZD), and Galaxy Zoo DESI publish spiral presence, arm count, and **winding tightness**, not winding **direction**. The latter distinction is disqualifying.

The local frozen requirement is explicit: `raw_b` is instrument agreement with a human handedness label on probability-sampled real accepted objects, while `epsilon` is that human rule's error on blind known-sign synthetics; the same correction is then used in `a_b=(raw_b-epsilon)/(1-2epsilon)` and `A_L=beta/(2a-1)`. Repeat consistency or crowd consensus is not a substitute for correctness against known truth. The panel memorandum likewise permits an external catalogue only with defensible sampling/transport **and** error calibration.

## 1. Handedness, not morphology

| Release | What is actually released | Direction usable? |
|---|---|---|
| **GZ1** | The original task offered six mutually exclusive answers: elliptical, clockwise spiral, anticlockwise spiral, edge-on, star/don't know, and merger. Released tables contain vote fractions conventionally described as `P_CW`/`P_ACW` (along with `P_EL`, `P_EDGE`, `P_DK`, `P_MG`; exact capitalization varies by table/schema). Thus this is the one relevant Galaxy Zoo release. The official release page describes nearly 900,000 objects and its `zooVotes`/Tables 2–3 products. ([official Galaxy Zoo data release](https://data.galaxyzoo.org/); [Lintott et al. 2011](https://arxiv.org/abs/1007.3265)) | **Yes in content, no for this calibration.** All catalogue rows have fractions for the six-answer task, but that does not mean all have a resolved direction. There is no single release-wide “gets direction” fraction without choosing a vote threshold. As an empirical high-confidence scale, the published spin analysis retained about 37,000 spirals, only about **4.1% of 893,212** GZ1 targets; that is analysis-specific, not a guaranteed crossmatch yield. ([Land et al. 2008](https://academic.oup.com/mnras/article/388/4/1686/981637)) |
| **GZ2** | Its branching tree asks whether spiral structure exists, then how tightly wound the arms are (`tight`, `medium`, `loose`) and how many arms are present. “Winding” in GZ2 is pitch/tightness, not chirality. ([official GZ data page](https://data.galaxyzoo.org/index.html); [winding-score definition](https://academic.oup.com/mnras/article/487/2/1808/5482087)) | **No.** No CW/ACW or S/Z answer columns. |
| **Galaxy Zoo DECaLS** | Volunteer and model catalogues use GZ2-like tasks: `has-spiral-arms`, `spiral-winding_{tight,medium,loose}`, and `spiral-arm-count`; no direction answers. It classified about 314,000 galaxies in DECaLS DR5 within the SDSS DR8 footprint. ([Walmsley et al. 2022](https://arxiv.org/abs/2102.08414); [official release summary](https://data.galaxyzoo.org/)) | **No.** “Spiral winding” is not winding sense. |
| **Galaxy Zoo DESI** | The 8.67-million-row catalogue has model-predicted vote fractions for the same morphology questions. Its schema has tight/medium/loose winding and arm counts, not CW/ACW. The bulk catalogue is an automated prediction product, though trained on volunteer votes. ([Walmsley et al. 2023](https://academic.oup.com/mnras/article/526/3/4768/7283169); [Zenodo record and schema description](https://zenodo.org/records/8360385)) | **No.** It is neither a chirality catalogue nor, for 8.7M rows, a published human-label catalogue. |

Therefore the attractive Legacy-Survey releases fail question 1 before coverage is considered.

## 2. Coverage and crossmatch

The supplied local files were checked without reading any image: `positions_selected_cut.csv` contains **49,211** rows and spans RA 0–360 degrees and Dec **−82.776 to +34.603 degrees**; `selected_brickids_cut.txt` contains **6,104** unique bricks. This is a broad DR10.1-south traversal, not an SDSS-footprint sample.

* **GZ1:** targets came from SDSS DR6/DR7-era imaging, principally the SDSS Main Galaxy Sample (`r<17.77`) plus other observed galaxy spectra. SDSS DR6 Legacy imaging covered 8,417 deg2, far smaller and much more northern/equatorial than DR10 south. ([SDSS DR6 summary](https://classic.sdss.org/dr6/); [GZ1 release paper](https://arxiv.org/abs/1007.3265)) The overlap is consequently confined to the SDSS stripes/caps intersecting the DR10-south definition; nearly all of the deep southern cap has no GZ1 coverage. An exact count was not asserted because no catalogue-row download or image access was authorized. Even the geometric upper bound, 8,417/roughly 20,000 DR10 deg2, is only about 42%, and the actual object yield is much lower because GZ1 is bright/SDSS-target selected and only a small subset has confident direction. It cannot plausibly provide the frozen 500 probability-sampled real labels across all nine strata/three bins.
* **GZD:** DECaLS **DR5**, restricted to the intersection with the **SDSS DR8 footprint**, about 5,000 deg2; this is not full DR10 south. It has coordinates and Legacy DR5 identifiers, but no direction label. ([Walmsley et al. 2022](https://arxiv.org/abs/2102.08414))
* **GZ DESI:** based on DESI Legacy Imaging Surveys **DR8** images and extended to the full DECaLS/MzLS/BASS/DESI footprint, about **19,000 deg2**, so it is the only examined release with potentially broad geometric overlap. Its published selection is extended sources brighter than approximately `r=19`, not the study's `shape_r>1.5`, non-PSF plus frozen-quality selection. ([official Galaxy Zoo release summary](https://data.galaxyzoo.org/); [Zoobot catalogue documentation](https://zoobot.readthedocs.io/en/latest/science_data.html)) DR10 subsequently expands/reprocesses southern DECam imaging and is not object-identical to DR8. ([Legacy Surveys DR10 description](https://www.legacysurvey.org/dr10/description/)) It still supplies zero direction labels.

**Join keys.** GZ DESI's `dr8_id`/`id_str` is `{DR8 brickid}_{DR8 objid}`. The study has DR10 `ls_id`, `brickid`, and `objid`; object identifiers are release-specific, so a direct DR8-to-DR10 `brickid,objid` or `ls_id` equality join is not defensible. A coordinate crossmatch (RA/Dec, with a prospectively fixed radius and duplicate/deblend resolution) is constructible for GZ1, GZD, or GZ DESI. It would require a row-level catalogue query and validation of ambiguous/resegmented sources. Coordinates enable a match; they do not cure absent chirality, selection mismatch, or error calibration.

## 3. Parity convention: the silent killer

GZ1's UI called apparent screen-image choices “Clock” and “Anti.” The spin paper avoids confusing apparent arm winding with physical rotation: moving outward from the centre, its **clockwise classification is called Z-wise**, and anticlockwise is called S-wise. ([GZ1 tutorial](https://zoo1.galaxyzoo.org/Tutorial.aspx); [Land et al. 2008](https://academic.oup.com/mnras/article/388/4/1686/981637)) These are display-relative labels, not a catalogue-level East-of-North signed angle.

A safe anchor would have to be prospective and executable: select published GZ1 examples (including a documented mirrored pair), reconstruct the exact SDSS display orientation from WCS, transform sky coordinates into the study's East-of-North convention, verify that horizontal reflection swaps the sign exactly once, and pin a lookup stating which of `P_CW`/`P_ACW` equals study `chi>0` (CCW/Longo-Left). That fixture must reproduce the frozen statement that Longo's `(R-L)=-0.0408` is this study's `(L-R)=+0.0408`. Catalogue names alone cannot anchor that mapping. No such WCS-and-mirror fixture is published in the release or presently pinned here, so GZ1 cannot safely supply the sign. GZ2/GZD/GZ DESI cannot be anchored because no chirality label exists.

## 4. Independence

GZ1 volunteer labels predate this study, used SDSS images, and were not selected with this instrument, its 6,104-brick traversal, its quality cuts, or its machine committee. That is genuinely external as to personnel and measurement pipeline. However, the catalogue's own SDSS target selection drives the transport failure below.

GZD volunteers viewed DECaLS DR5 imagery, and GZ DESI models were trained on volunteer answers to Legacy Survey DR5/DR8 images. They predate this study and were not selected from its DR10 accepted list, but they use the same survey family and GZ DESI's 8.7M labels are machine-model outputs, not an independent human hand-check. Using those outputs inside `a` would violate the frozen “no machine result inside `a`” rule. In any event both lack direction.

## 5. Their error rate and `epsilon`

The releases provide many votes per object and hence vote fractions; GZ1 also conducted rotated/mirrored-image bias experiments. A mirror should swap apparent chirality, and the experiment found a persistent human preference/bias, motivating statistical corrections. ([Galaxy Zoo bias-study description](https://blog.galaxyzoo.org/2007/12/31/the-bias-study/); [Land et al. 2008](https://academic.oup.com/mnras/article/388/4/1686/981637)) These data can estimate consensus, dispersion, mirror equivariance, and directional response bias.

They **cannot estimate the required `epsilon=P(human rule != known true handedness)`**. Real galaxies have no independent known-answer arm-winding key; a mirrored real object supplies a known *relationship* between two presentations but not the correctness of either original call. Published comparisons to experts principally validate broad morphology, not an absolute known-truth CW/ACW rule. GZD/GZ DESI accuracy statements quantify how well a neural network predicts confident volunteer answers, not how often humans identify true chirality, and they concern questions that omit chirality. No examined release publishes blind synthetic known-sign controls passed through the same aggregate labeling rule. Thus there is no `epsilon`, `sigma_epsilon`, shared-error covariance, or per-bin lower bound for BS-8f. This alone is disqualifying.

## 6. Sampling and transport

None is a probability sample of the accepted population. The study population comes from a fixed DR10.1-south brick traversal and frozen shape/type/quality cuts. GZ1 is an SDSS bright spectroscopic/photometric target catalogue; GZD was selected from DECaLS DR5 within SDSS DR8; GZ DESI uses DR8 extended sources around `r<19`. Inclusion depends on footprint, flux, targeting, deblending/data-release processing, and whether morphology questions were reached.

A defensible transport would require, at minimum, knowing inclusion probabilities or modeling overlap/non-overlap from covariates observed identically in both catalogues, positivity in every one of the nine strata by three calibration bins, a preregistered DR8/DR10 coordinate/deblend match, frozen nonresponse/confidence handling, population/allocation weights, and sensitivity bounds for unmeasured image-quality and morphology differences. GZ1 has structural zero inclusion over much of the southern footprint, so positivity fails and weighting cannot recover the full estimand. GZ DESI has broader positivity but no human direction outcome. Consequently no valid transport to the accepted population exists from these releases.

## 7. Verdict and implications for stage two

**NOT USABLE.** Blocking reasons are cumulative:

1. Broad-overlap GZD/GZ DESI/GZ2 catalogues do not publish clockwise/anticlockwise handedness.
2. GZ1's handedness subset does not cover or probability-sample the DR10.1-south accepted population; positivity fails over large regions and its bright selection is incompatible.
3. No release provides blind known-answer controls for the same human aggregate rule, so frozen `epsilon` and its uncertainty cannot be formed.
4. GZ1's display-relative CW/ACW sign lacks the required pinned East-of-North/WCS/mirror anchor.
5. GZ DESI's broad catalogue values are machine predictions, forbidden inside `a`.

This is not “conditional” because satisfying the missing conditions would require collecting new chirality classifications and known-answer controls—precisely new human labour—not merely a catalogue crossmatch. Stage two must not write a Galaxy Zoo-derived BS-8f receipt, substitute vote agreement for `epsilon`, infer chirality from tight/loose winding, or treat model-to-volunteer accuracy as human correctness. With the panel infeasible and this external route unusable, the frozen calibration remains unavailable; absent an explicit redesign/re-freeze, Stage C cannot form a calibrated confirmatory `A_L` verdict.

SEAT: CODEX
VERSION: EXTLABELS-V1
VERDICT: NOT-USABLE
COUNT: 12
