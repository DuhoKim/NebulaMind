# URL: https://sdm-schemas.lsst.io/dp1.html

# Data Preview 1

* * *

## [Object](https://sdm-schemas.lsst.io/dp1.html\#Object)

Descriptions of static astronomical objects (or the static aspects of variable and slowly-moving objects) detected and measured on coadds.

Indexes

| Columns | Description | Reference Name |
| --- | --- | --- |
| [objectId](https://sdm-schemas.lsst.io/dp1.html#Object.objectId) | Unique index on objectId column | idx\_Object\_objectId |

CSV

Search:

| Column Name | Data Type | Unit | Description | UCD | Order | Principal |
| --- | --- | --- | --- | --- | --- | --- |
| [coord\_dec](https://sdm-schemas.lsst.io/dp1.html#Object.coord_dec) | double | deg | Fiducial ICRS Declination of centroid used for database indexing | pos.eq.dec;meta.main |  | 1 |
| [coord\_decErr](https://sdm-schemas.lsst.io/dp1.html#Object.coord_decErr) | float | deg | Error in fiducial ICRS Declination of centroid | stat.error;pos.eq.dec;meta.main |  |  |
| [coord\_ra](https://sdm-schemas.lsst.io/dp1.html#Object.coord_ra) | double | deg | Fiducial ICRS Right Ascension of centroid used for database indexing | pos.eq.ra;meta.main |  | 1 |
| [coord\_ra\_dec\_Cov](https://sdm-schemas.lsst.io/dp1.html#Object.coord_ra_dec_Cov) | float | deg\*\*2 | Covariance between fiducial ICRS Right Ascension and Declination of centroid | stat.covariance;pos.eq.ra;pos.eq.dec;meta.main |  |  |
| [coord\_raErr](https://sdm-schemas.lsst.io/dp1.html#Object.coord_raErr) | float | deg | Error in fiducial ICRS Right Ascension of centroid | stat.error;pos.eq.ra;meta.main |  |  |
| [deblend\_failed](https://sdm-schemas.lsst.io/dp1.html#Object.deblend_failed) | boolean |  | Deblender failed to deblend this source |  |  |  |
| [deblend\_incompleteData](https://sdm-schemas.lsst.io/dp1.html#Object.deblend_incompleteData) | boolean |  | One or more bands were not deblended due to an inability to model the PSF. |  |  |  |
| [deblend\_isolatedParent](https://sdm-schemas.lsst.io/dp1.html#Object.deblend_isolatedParent) | boolean |  | Deblender skipped this footprint because there was only a single peak |  |  |  |
| [deblend\_iterations](https://sdm-schemas.lsst.io/dp1.html#Object.deblend_iterations) | int |  | Number of iterations during deblending |  |  |  |
| [deblend\_logL](https://sdm-schemas.lsst.io/dp1.html#Object.deblend_logL) | float |  | Log likelihood of the entire blend in scarlet\_lite. |  |  |  |
| [deblend\_masked](https://sdm-schemas.lsst.io/dp1.html#Object.deblend_masked) | boolean |  | Deblender skipped this source because there were too many masked pixels. |  |  |  |
| [deblend\_nChild](https://sdm-schemas.lsst.io/dp1.html#Object.deblend_nChild) | int |  | Number of children this object has (defaults to 0) |  |  | 1 |
| [deblend\_nPeaks](https://sdm-schemas.lsst.io/dp1.html#Object.deblend_nPeaks) | int |  | Number of peaks this parent footprint has (even if the deblender failed or skipped this blend) |  |  |  |
| [deblend\_parentTooBig](https://sdm-schemas.lsst.io/dp1.html#Object.deblend_parentTooBig) | boolean |  | Deblender skipped this source because the parent footprint was too large. |  |  |  |
| [deblend\_peak\_center\_x](https://sdm-schemas.lsst.io/dp1.html#Object.deblend_peak_center_x) | int | pixel | x-coordinate of the peak after source detection |  |  |  |
| [deblend\_peak\_center\_y](https://sdm-schemas.lsst.io/dp1.html#Object.deblend_peak_center_y) | int | pixel | y-coordinate of the peak after source detection |  |  |  |
| [deblend\_skipped](https://sdm-schemas.lsst.io/dp1.html#Object.deblend_skipped) | boolean |  | Deblender skipped this source |  |  |  |
| [deblend\_tooManyPeaks](https://sdm-schemas.lsst.io/dp1.html#Object.deblend_tooManyPeaks) | boolean |  | Deblender skipped this source because there were too many peaks in the Footprint. |  |  |  |
| [detect\_fromBlend](https://sdm-schemas.lsst.io/dp1.html#Object.detect_fromBlend) | boolean |  | This source is deblended from a parent with more than one child. |  |  | 1 |
| [detect\_isDeblendedModelSource](https://sdm-schemas.lsst.io/dp1.html#Object.detect_isDeblendedModelSource) | boolean |  | True if source has no children and is in the inner region of a coadd patch and is in the inner region of a coadd tract and is not detected in a pseudo-filter (see config.pseudoFilterList) and is a deblended child |  |  |  |
| [detect\_isIsolated](https://sdm-schemas.lsst.io/dp1.html#Object.detect_isIsolated) | boolean |  | This source is not a part of a blend. |  |  | 1 |
| [ebv](https://sdm-schemas.lsst.io/dp1.html#Object.ebv) | float | mag | E(B-V) at coord\_ra/coord\_dec per Schlegel, Finkbeiner & Davis (1998) |  |  |  |
| [footprintArea](https://sdm-schemas.lsst.io/dp1.html#Object.footprintArea) | int | pixel | Number of pixels in the sources detection footprint. Reference band. |  |  |  |
| [g\_ap03Flux](https://sdm-schemas.lsst.io/dp1.html#Object.g_ap03Flux) | float | nJy | Flux within 3.0-pixel aperture. Forced on g-band. |  |  |  |
| [g\_ap03Flux\_flag](https://sdm-schemas.lsst.io/dp1.html#Object.g_ap03Flux_flag) | boolean |  | Flag set for any failure with the 3.0-pixel aperture flux. Forced on g-band. |  |  |  |
| [g\_ap03FluxErr](https://sdm-schemas.lsst.io/dp1.html#Object.g_ap03FluxErr) | float | nJy | Flux uncertainty within 3.0-pixel aperture. Forced on g-band. |  |  |  |
| [g\_ap06Flux](https://sdm-schemas.lsst.io/dp1.html#Object.g_ap06Flux) | float | nJy | Flux within 6.0-pixel aperture. Forced on g-band. |  |  |  |
| [g\_ap06Flux\_flag](https://sdm-schemas.lsst.io/dp1.html#Object.g_ap06Flux_flag) | boolean |  | Flag set for any failure with the 6.0-pixel aperture flux. Forced on g-band. |  |  |  |
| [g\_ap06FluxErr](https://sdm-schemas.lsst.io/dp1.html#Object.g_ap06FluxErr) | float | nJy | Flux uncertainty within 6.0-pixel aperture. Forced on g-band. |  |  |  |
| [g\_ap09Flux](https://sdm-schemas.lsst.io/dp1.html#Object.g_ap09Flux) | float | nJy | Flux within 9.0-pixel aperture. Forced on g-band. |  |  |  |
| [g\_ap09Flux\_flag](https://sdm-schemas.lsst.io/dp1.html#Object.g_ap09Flux_flag) | boolean |  | Flag set for any failure with the 9.0-pixel aperture flux. Forced on g-band. |  |  |  |
| [g\_ap09FluxErr](https://sdm-schemas.lsst.io/dp1.html#Object.g_ap09FluxErr) | float | nJy | Flux uncertainty within 9.0-pixel aperture. Forced on g-band. |  |  |  |
| [g\_ap12Flux](https://sdm-schemas.lsst.io/dp1.html#Object.g_ap12Flux) | float | nJy | Flux within 12.0-pixel aperture. Forced on g-band. |  |  |  |
| [g\_ap12Flux\_flag](https://sdm-schemas.lsst.io/dp1.html#Object.g_ap12Flux_flag) | boolean |  | Flag set for any failure with the 12.0-pixel aperture flux. Forced on g-band. |  |  |  |
| [g\_ap12FluxErr](https://sdm-schemas.lsst.io/dp1.html#Object.g_ap12FluxErr) | float | nJy | Flux uncertainty within 12.0-pixel aperture. Forced on g-band. |  |  |  |
| [g\_ap17Flux](https://sdm-schemas.lsst.io/dp1.html#Object.g_ap17Flux) | float | nJy | Flux within 17.0-pixel aperture. Forced on g-band. |  |  |  |
| [g\_ap17Flux\_flag](https://sdm-schemas.lsst.io/dp1.html#Object.g_ap17Flux_flag) | boolean |  | Flag set for any failure with the 17.0-pixel aperture flux. Forced on g-band. |  |  |  |
| [g\_ap17FluxErr](https://sdm-schemas.lsst.io/dp1.html#Object.g_ap17FluxErr) | float | nJy | Flux uncertainty within 17.0-pixel aperture. Forced on g-band. |  |  |  |
| [g\_ap25Flux](https://sdm-schemas.lsst.io/dp1.html#Object.g_ap25Flux) | float | nJy | Flux within 25.0-pixel aperture. Forced on g-band. |  |  |  |
| [g\_ap25Flux\_flag](https://sdm-schemas.lsst.io/dp1.html#Object.g_ap25Flux_flag) | boolean |  | Flag set for any failure with the 25.0-pixel aperture flux. Forced on g-band. |  |  |  |
| [g\_ap25FluxErr](https://sdm-schemas.lsst.io/dp1.html#Object.g_ap25FluxErr) | float | nJy | Flux uncertainty within 25.0-pixel aperture. Forced on g-band. |  |  |  |
| [g\_ap35Flux](https://sdm-schemas.lsst.io/dp1.html#Object.g_ap35Flux) | float | nJy | Flux within 35.0-pixel aperture. Forced on g-band. |  |  |  |
| [g\_ap35Flux\_flag](https://sdm-schemas.lsst.io/dp1.html#Object.g_ap35Flux_flag) | boolean |  | Flag set for any failure with the 35.0-pixel aperture flux. Forced on g-band. |  |  |  |
| [g\_ap35FluxErr](https://sdm-schemas.lsst.io/dp1.html#Object.g_ap35FluxErr) | float | nJy | Flux uncertainty within 35.0-pixel aperture. Forced on g-band. |  |  |  |
| [g\_ap50Flux](https://sdm-schemas.lsst.io/dp1.html#Object.g_ap50Flux) | float | nJy | Flux within 50.0-pixel aperture. Forced on g-band. |  |  |  |
| [g\_ap50Flux\_flag](https://sdm-schemas.lsst.io/dp1.html#Object.g_ap50Flux_flag) | boolean |  | Flag set for any failure with the 50.0-pixel aperture flux. Forced on g-band. |  |  |  |
| [g\_ap50FluxErr](https://sdm-schemas.lsst.io/dp1.html#Object.g_ap50FluxErr) | float | nJy | Flux uncertainty within 50.0-pixel aperture. Forced on g-band. |  |  |  |
| [g\_ap70Flux](https://sdm-schemas.lsst.io/dp1.html#Object.g_ap70Flux) | float | nJy | Flux within 70.0-pixel aperture. Forced on g-band. |  |  |  |
| [g\_ap70Flux\_flag](https://sdm-schemas.lsst.io/dp1.html#Object.g_ap70Flux_flag) | boolean |  | Flag set for any failure with the 70.0-pixel aperture flux. Forced on g-band. |  |  |  |
| [g\_ap70FluxErr](https://sdm-schemas.lsst.io/dp1.html#Object.g_ap70FluxErr) | float | nJy | Flux uncertainty within 70.0-pixel aperture. Forced on g-band. |  |  |  |
| [g\_apFlux\_flag](https://sdm-schemas.lsst.io/dp1.html#Object.g_apFlux_flag) | boolean |  | Duplicate of g\_ap12Flux\_flag. |  |  |  |
| [g\_apFlux\_flag\_apertureTruncated](https://sdm-schemas.lsst.io/dp1.html#Object.g_apFlux_flag_apertureTruncated) | boolean |  | Duplicate of g\_ap12Flux\_flag\_apertureTruncated. |  |  |  |
| [g\_apFlux\_flag\_sincCoeffsTruncated](https://sdm-schemas.lsst.io/dp1.html#Object.g_apFlux_flag_sincCoeffsTruncated) | boolean |  | Duplicate of g\_ap12Flux\_flag\_sincCoeffsTruncated. Measured on g-band. |  |  |  |
| [g\_bdChi2](https://sdm-schemas.lsst.io/dp1.html#Object.g_bdChi2) | float |  | -ln(likelihood) (chi^2) in CModel fit. Measured on g-band. |  |  |  |
| [g\_bdE1](https://sdm-schemas.lsst.io/dp1.html#Object.g_bdE1) | float | pixel\*\*2 | Flux-weighted average of exponential and de Vaucouleurs ellipticities. Measured on g-band. |  |  |  |
| [g\_bdE2](https://sdm-schemas.lsst.io/dp1.html#Object.g_bdE2) | float | pixel\*\*2 | Flux-weighted average of exponential and de Vaucouleurs ellipticities. Measured on g-band. |  |  |  |
| [g\_bdFluxB](https://sdm-schemas.lsst.io/dp1.html#Object.g_bdFluxB) | float | nJy | Flux from the de Vaucouleurs fit. Measured on g-band. |  |  |  |
| [g\_bdFluxBErr](https://sdm-schemas.lsst.io/dp1.html#Object.g_bdFluxBErr) | float | nJy | Flux uncertainty from the de Vaucouleurs fit. Measured on g-band. |  |  |  |
| [g\_bdFluxD](https://sdm-schemas.lsst.io/dp1.html#Object.g_bdFluxD) | float | nJy | Flux from the exponential fit. Measured on g-band. |  |  |  |
| [g\_bdFluxDErr](https://sdm-schemas.lsst.io/dp1.html#Object.g_bdFluxDErr) | float | nJy | Flux uncertainty from the exponential fit. Measured on g-band. |  |  |  |
| [g\_bdReB](https://sdm-schemas.lsst.io/dp1.html#Object.g_bdReB) | float | pixel\*\*2 | Half-light ellipse of the de Vaucouleurs fit. Measured on g-band. |  |  |  |
| [g\_bdReD](https://sdm-schemas.lsst.io/dp1.html#Object.g_bdReD) | float | pixel\*\*2 | Half-light ellipse of the exponential fit. Measured on g-band. |  |  |  |
| [g\_blendedness](https://sdm-schemas.lsst.io/dp1.html#Object.g_blendedness) | float |  | Measure of how much the flux is affected by neighbors, (1 - child\_flux/parent\_flux). Operates on the absolute value of the pixels to try to obtain a de-noised value. See section 4.9.11 of Bosch et al. 2018, PASJ, 70, S5 for details. Measured on g-band. |  |  |  |
| [g\_blendedness\_flag](https://sdm-schemas.lsst.io/dp1.html#Object.g_blendedness_flag) | boolean |  | Flag set for any failure in the blendedness algorithm. Measured on g-band. |  |  |  |
| [g\_calib\_astrometry\_used](https://sdm-schemas.lsst.io/dp1.html#Object.g_calib_astrometry_used) | boolean |  | Propagated from sources. Measured on g-band. |  |  |  |
| [g\_calib\_photometry\_reserved](https://sdm-schemas.lsst.io/dp1.html#Object.g_calib_photometry_reserved) | boolean |  | Propagated from sources. Measured on g-band. |  |  |  |
| [g\_calib\_photometry\_used](https://sdm-schemas.lsst.io/dp1.html#Object.g_calib_photometry_used) | boolean |  | Propagated from sources. Measured on g-band. |  |  |  |
| [g\_calib\_psf\_candidate](https://sdm-schemas.lsst.io/dp1.html#Object.g_calib_psf_candidate) | boolean |  | Propagated from sources. Measured on g-band. |  |  |  |
| [g\_calib\_psf\_reserved](https://sdm-schemas.lsst.io/dp1.html#Object.g_calib_psf_reserved) | boolean |  | Propagated from sources. Measured on g-band. |  |  |  |
| [g\_calib\_psf\_used](https://sdm-schemas.lsst.io/dp1.html#Object.g_calib_psf_used) | boolean |  | Propagated from sources. Measured on g-band. |  |  |  |
| [g\_calibFlux](https://sdm-schemas.lsst.io/dp1.html#Object.g_calibFlux) | float | nJy | Duplicate of g\_ap12Flux. |  |  |  |
| [g\_calibFlux\_flag](https://sdm-schemas.lsst.io/dp1.html#Object.g_calibFlux_flag) | boolean |  | Duplicate of g\_ap12Flux\_flag. |  |  |  |
| [g\_calibFlux\_flag\_apertureTruncated](https://sdm-schemas.lsst.io/dp1.html#Object.g_calibFlux_flag_apertureTruncated) | boolean |  | Duplicate of g\_ap12Flux\_flag\_apertureTruncated. |  |  |  |
| [g\_calibFlux\_flag\_sincCoeffsTruncated](https://sdm-schemas.lsst.io/dp1.html#Object.g_calibFlux_flag_sincCoeffsTruncated) | boolean |  | Duplicate of g\_ap12Flux\_flag\_sincCoeffsTruncated. Measured on g-band. |  |  |  |
| [g\_calibFluxErr](https://sdm-schemas.lsst.io/dp1.html#Object.g_calibFluxErr) | float | nJy | Duplicate of g\_ap12FluxErr. |  |  |  |
| [g\_centroid\_flag](https://sdm-schemas.lsst.io/dp1.html#Object.g_centroid_flag) | boolean |  | Flag set for any failure in the centroid algorithm. Measured on g-band. |  |  |  |
| [g\_centroid\_x](https://sdm-schemas.lsst.io/dp1.html#Object.g_centroid_x) | double | pixel | Centroid from the SDSS centroid algorithm. Measured on g-band. |  |  |  |
| [g\_centroid\_xErr](https://sdm-schemas.lsst.io/dp1.html#Object.g_centroid_xErr) | float | pixel | 1-sigma uncertainty on x position. Measured on g-band. |  |  |  |
| [g\_centroid\_y](https://sdm-schemas.lsst.io/dp1.html#Object.g_centroid_y) | double | pixel | Centroid from the SDSS centroid algorithm. Measured on g-band. |  |  |  |
| [g\_centroid\_yErr](https://sdm-schemas.lsst.io/dp1.html#Object.g_centroid_yErr) | float | pixel | 1-sigma uncertainty on y position. Measured on g-band. |  |  |  |
| [g\_cModel\_flag](https://sdm-schemas.lsst.io/dp1.html#Object.g_cModel_flag) | boolean |  | Flag set if the final CModel fit (or any previous fit) failed. Forced on g-band. |  |  |  |
| [g\_cModel\_flag\_apCorr](https://sdm-schemas.lsst.io/dp1.html#Object.g_cModel_flag_apCorr) | boolean |  | Flag set if unable to aperture-correct the CModel flux. Forced on g-band. |  |  |  |
| [g\_cModelFlux](https://sdm-schemas.lsst.io/dp1.html#Object.g_cModelFlux) | float | nJy | Flux from the final CModel fit. Forced on g-band. |  |  |  |
| [g\_cModelFlux\_inner](https://sdm-schemas.lsst.io/dp1.html#Object.g_cModelFlux_inner) | float | nJy | Flux within the fit region, with no extrapolation. Forced on g-band. |  |  |  |
| [g\_cModelFluxErr](https://sdm-schemas.lsst.io/dp1.html#Object.g_cModelFluxErr) | float | nJy | Flux uncertainty from the final CModel fit. Forced on g-band. |  |  |  |
| [g\_cModelMag](https://sdm-schemas.lsst.io/dp1.html#Object.g_cModelMag) | float | mag | AB magnitude of cModelFlux. Forced on g-band. |  |  | 1 |
| [g\_cModelMagErr](https://sdm-schemas.lsst.io/dp1.html#Object.g_cModelMagErr) | float | mag | Uncertainty in magnitudes on cModelFlux. Forced on g-band. |  |  | 1 |
| [g\_deblend\_blendedness](https://sdm-schemas.lsst.io/dp1.html#Object.g_deblend_blendedness) | float |  | Blendedness in the deconvolved scarlet space. |  |  |  |
| [g\_deblend\_dataCoverage](https://sdm-schemas.lsst.io/dp1.html#Object.g_deblend_dataCoverage) | float |  | Fraction of data that contained good data, ie. 1 - number of no data pixels/total number of pixels in the g-band. |  |  |  |
| [g\_deblend\_fluxOverlap](https://sdm-schemas.lsst.io/dp1.html#Object.g_deblend_fluxOverlap) | float |  | The total flux from neighboring objects that overlaps with this sources footprint in the deconvolved space. |  |  |  |
| [g\_deblend\_fluxOverlapFraction](https://sdm-schemas.lsst.io/dp1.html#Object.g_deblend_fluxOverlapFraction) | float |  | Fraction of flux from neighbors / source flux in the deconvolved footprint. |  |  |  |
| [g\_deblend\_zeroFlux](https://sdm-schemas.lsst.io/dp1.html#Object.g_deblend_zeroFlux) | boolean |  | True when there was no flux attributed to this object after flux redistribution in the deblender. |  |  |  |
| [g\_dec](https://sdm-schemas.lsst.io/dp1.html#Object.g_dec) | double | deg | Position in declination, measured on g-band. | pos.eq.dec |  |  |
| [g\_decErr](https://sdm-schemas.lsst.io/dp1.html#Object.g_decErr) | float | deg | Error in declination, measured on g-band. | stat.error;pos.eq.dec |  |  |
| [g\_epoch](https://sdm-schemas.lsst.io/dp1.html#Object.g_epoch) | double | d | Mean epoch of the object in the g-band coadd in MJD TAI |  |  |  |
| [g\_extendedness](https://sdm-schemas.lsst.io/dp1.html#Object.g_extendedness) | float |  | Flux-ratio measure of whether an object is point-like (0) or extended (1). Measured on g-band. |  |  |  |
| [g\_extendedness\_flag](https://sdm-schemas.lsst.io/dp1.html#Object.g_extendedness_flag) | boolean |  | Flag set for any failure in the flux-ratio extendedness. Measured on g-band. |  |  |  |
| [g\_free\_cModelFlux](https://sdm-schemas.lsst.io/dp1.html#Object.g_free_cModelFlux) | float | nJy | Flux from the final CModel fit. Measured on g-band. |  |  |  |
| [g\_free\_cModelFlux\_flag](https://sdm-schemas.lsst.io/dp1.html#Object.g_free_cModelFlux_flag) | boolean |  | Flag set if the final CModel fit (or any previous fit) failed. Measured on g-band. |  |  |  |
| [g\_free\_cModelFlux\_inner](https://sdm-schemas.lsst.io/dp1.html#Object.g_free_cModelFlux_inner) | float | nJy | Flux within the fit region, with no extrapolation. Measured on g-band. |  |  |  |
| [g\_free\_cModelFluxErr](https://sdm-schemas.lsst.io/dp1.html#Object.g_free_cModelFluxErr) | float | nJy | Flux uncertainty from the final CModel fit. Measured on g-band. |  |  |  |
| [g\_free\_psfFlux](https://sdm-schemas.lsst.io/dp1.html#Object.g_free_psfFlux) | float | nJy | Flux derived from using the PSF model as a weight function. Measured on g-band. |  |  |  |
| [g\_free\_psfFlux\_flag](https://sdm-schemas.lsst.io/dp1.html#Object.g_free_psfFlux_flag) | boolean |  | Flag set if the unforced PSF flux failed in this band for any reason. Measured on g-band. |  |  |  |
| [g\_free\_psfFluxErr](https://sdm-schemas.lsst.io/dp1.html#Object.g_free_psfFluxErr) | float | nJy | Flux uncertainty derived from using the PSF model as a weight function. Measured on g-band. |  |  |  |
| [g\_gaap0p7Flux](https://sdm-schemas.lsst.io/dp1.html#Object.g_gaap0p7Flux) | float | nJy | GAaP Flux with 0.7 arcsec aperture after reconvolving the image to a Gaussian PSF larger than the original by a factor of 1.15. Forced on g-band. |  |  |  |
| [g\_gaap0p7Flux\_flag\_bigPsf](https://sdm-schemas.lsst.io/dp1.html#Object.g_gaap0p7Flux_flag_bigPsf) | boolean |  | The Gaussianized PSF is bigger than the aperture. Forced on g-band. |  |  |  |
| [g\_gaap0p7FluxErr](https://sdm-schemas.lsst.io/dp1.html#Object.g_gaap0p7FluxErr) | float | nJy | GAaP Flux uncertainty with 0.7 arcsec aperture after multiplying the seeing by 1.15. Forced on g-band. |  |  |  |
| [g\_gaap1p0Flux](https://sdm-schemas.lsst.io/dp1.html#Object.g_gaap1p0Flux) | float | nJy | GAaP Flux with 1.0 arcsec aperture after reconvolving the image to a Gaussian PSF larger than the original by a factor of 1.15. Forced on g-band. |  |  |  |
| [g\_gaap1p0Flux\_flag\_bigPsf](https://sdm-schemas.lsst.io/dp1.html#Object.g_gaap1p0Flux_flag_bigPsf) | boolean |  | The Gaussianized PSF is bigger than the aperture. Forced on g-band. |  |  |  |
| [g\_gaap1p0FluxErr](https://sdm-schemas.lsst.io/dp1.html#Object.g_gaap1p0FluxErr) | float | nJy | GAaP Flux uncertainty with 1.0 arcsec aperture after multiplying the seeing by 1.15. Forced on g-band. |  |  |  |
| [g\_gaap1p5Flux](https://sdm-schemas.lsst.io/dp1.html#Object.g_gaap1p5Flux) | float | nJy | GAaP Flux with 1.5 arcsec aperture after reconvolving the image to a Gaussian PSF larger than the original by a factor of 1.15. Forced on g-band. |  |  |  |
| [g\_gaap1p5Flux\_flag\_bigPsf](https://sdm-schemas.lsst.io/dp1.html#Object.g_gaap1p5Flux_flag_bigPsf) | boolean |  | The Gaussianized PSF is bigger than the aperture. Forced on g-band. |  |  |  |
| [g\_gaap1p5FluxErr](https://sdm-schemas.lsst.io/dp1.html#Object.g_gaap1p5FluxErr) | float | nJy | GAaP Flux uncertainty with 1.5 arcsec aperture after multiplying the seeing by 1.15. Forced on g-band. |  |  |  |
| [g\_gaap2p5Flux](https://sdm-schemas.lsst.io/dp1.html#Object.g_gaap2p5Flux) | float | nJy | GAaP Flux with 2.5 arcsec aperture after reconvolving the image to a Gaussian PSF larger than the original by a factor of 1.15. Forced on g-band. |  |  |  |
| [g\_gaap2p5Flux\_flag\_bigPsf](https://sdm-schemas.lsst.io/dp1.html#Object.g_gaap2p5Flux_flag_bigPsf) | boolean |  | The Gaussianized PSF is bigger than the aperture. Forced on g-band. |  |  |  |
| [g\_gaap2p5FluxErr](https://sdm-schemas.lsst.io/dp1.html#Object.g_gaap2p5FluxErr) | float | nJy | GAaP Flux uncertainty with 2.5 arcsec aperture after multiplying the seeing by 1.15. Forced on g-band. |  |  |  |
| [g\_gaap3p0Flux](https://sdm-schemas.lsst.io/dp1.html#Object.g_gaap3p0Flux) | float | nJy | GAaP Flux with 3.0 arcsec aperture after reconvolving the image to a Gaussian PSF larger than the original by a factor of 1.15. Forced on g-band. |  |  |  |
| [g\_gaap3p0Flux\_flag\_bigPsf](https://sdm-schemas.lsst.io/dp1.html#Object.g_gaap3p0Flux_flag_bigPsf) | boolean |  | The Gaussianized PSF is bigger than the aperture. Forced on g-band. |  |  |  |
| [g\_gaap3p0FluxErr](https://sdm-schemas.lsst.io/dp1.html#Object.g_gaap3p0FluxErr) | float | nJy | GAaP Flux uncertainty with 3.0 arcsec aperture after multiplying the seeing by 1.15. Forced on g-band. |  |  |  |
| [g\_gaapFlux\_flag](https://sdm-schemas.lsst.io/dp1.html#Object.g_gaapFlux_flag) | boolean |  | Flag set for any failure in the GAaP photometry. Forced on g-band. |  |  |  |
| [g\_gaapFlux\_flag\_edge](https://sdm-schemas.lsst.io/dp1.html#Object.g_gaapFlux_flag_edge) | boolean |  | Source is too close to the edge. Forced on g-band. |  |  |  |
| [g\_gaapFlux\_flag\_gaussianization](https://sdm-schemas.lsst.io/dp1.html#Object.g_gaapFlux_flag_gaussianization) | boolean |  | PSF Gaussianization failed when trying to scale by this factor. Forced on g-band. |  |  |  |
| [g\_gaapOptimalFlux](https://sdm-schemas.lsst.io/dp1.html#Object.g_gaapOptimalFlux) | float | nJy | GAaP Flux with optimal aperture after reconvolving the image to a Gaussian PSF larger than the original by a factor of 1.15. Forced on g-band. |  |  |  |
| [g\_gaapOptimalFlux\_flag\_bigPsf](https://sdm-schemas.lsst.io/dp1.html#Object.g_gaapOptimalFlux_flag_bigPsf) | boolean |  | The Gaussianized PSF is bigger than the aperture. Forced on g-band. |  |  |  |
| [g\_gaapOptimalFluxErr](https://sdm-schemas.lsst.io/dp1.html#Object.g_gaapOptimalFluxErr) | float | nJy | GAaP Flux uncertainty with optimal aperture after multiplying the seeing by 1.15. Forced on g-band. |  |  |  |
| [g\_gaapPsfFlux](https://sdm-schemas.lsst.io/dp1.html#Object.g_gaapPsfFlux) | float | nJy | GAaP Flux with PSF aperture after reconvolving the image to a Gaussian PSF larger than the original by a factor of 1.15. Forced on g-band. |  |  |  |
| [g\_gaapPsfFluxErr](https://sdm-schemas.lsst.io/dp1.html#Object.g_gaapPsfFluxErr) | float | nJy | GAaP Flux uncertainty with PSF aperture after multiplying the seeing by 1.15. Forced on g-band. |  |  |  |
| [g\_hsm\_moments\_03](https://sdm-schemas.lsst.io/dp1.html#Object.g_hsm_moments_03) | float |  | HSM higher-order moment 03. Measured on g-band. |  |  |  |
| [g\_hsm\_moments\_04](https://sdm-schemas.lsst.io/dp1.html#Object.g_hsm_moments_04) | float |  | HSM higher-order moment 04. Measured on g-band. |  |  |  |
| [g\_hsm\_moments\_12](https://sdm-schemas.lsst.io/dp1.html#Object.g_hsm_moments_12) | float |  | HSM higher-order moment 12. Measured on g-band. |  |  |  |
| [g\_hsm\_moments\_13](https://sdm-schemas.lsst.io/dp1.html#Object.g_hsm_moments_13) | float |  | HSM higher-order moment 13. Measured on g-band. |  |  |  |
| [g\_hsm\_moments\_21](https://sdm-schemas.lsst.io/dp1.html#Object.g_hsm_moments_21) | float |  | HSM higher-order moment 21. Measured on g-band. |  |  |  |
| [g\_hsm\_moments\_22](https://sdm-schemas.lsst.io/dp1.html#Object.g_hsm_moments_22) | float |  | HSM higher-order moment 22. Measured on g-band. |  |  |  |
| [g\_hsm\_moments\_30](https://sdm-schemas.lsst.io/dp1.html#Object.g_hsm_moments_30) | float |  | HSM higher-order moment 30. Measured on g-band. |  |  |  |
| [g\_hsm\_moments\_31](https://sdm-schemas.lsst.io/dp1.html#Object.g_hsm_moments_31) | float |  | HSM higher-order moment 31. Measured on g-band. |  |  |  |
| [g\_hsm\_moments\_40](https://sdm-schemas.lsst.io/dp1.html#Object.g_hsm_moments_40) | float |  | HSM higher-order moment 40. Measured on g-band. |  |  |  |
| [g\_hsm\_moments\_flag](https://sdm-schemas.lsst.io/dp1.html#Object.g_hsm_moments_flag) | boolean |  | Flag set for any failure in the HSM higher-order moments. Measured on g-band. |  |  |  |
| [g\_hsm\_momentsPsf\_03](https://sdm-schemas.lsst.io/dp1.html#Object.g_hsm_momentsPsf_03) | float |  | HSM higher-order moment 03 measured on the PSF model at the position of the object. Measured on g-band. |  |  |  |
| [g\_hsm\_momentsPsf\_04](https://sdm-schemas.lsst.io/dp1.html#Object.g_hsm_momentsPsf_04) | float |  | HSM higher-order moment 04 measured on the PSF model at the position of the object. Measured on g-band. |  |  |  |

[... middle omitted — see footer ...]

| [ySize](https://sdm-schemas.lsst.io/dp1.html#CcdVisit.ySize) | long | pixel | Number of rows in the image. |  |  |  |
| [zenithDistance](https://sdm-schemas.lsst.io/dp1.html#CcdVisit.zenithDistance) | float | deg | Zenith distance at observation mid-point. |  |  | 1 |
| [zeroPoint](https://sdm-schemas.lsst.io/dp1.html#CcdVisit.zeroPoint) | float | mag | Zero-point for the Ccd, estimated at Ccd center. |  |  |  |
| [visitId](https://sdm-schemas.lsst.io/dp1.html#CcdVisit.visitId) | long |  | Reference to the corresponding entry in the Visit table. | meta.id.parent;obs | 2 | 1 |
| [expMidptMJD](https://sdm-schemas.lsst.io/dp1.html#CcdVisit.expMidptMJD) | double | d | Midpoint time for exposure at the fiducial center of the focal plane array in MJD. TAI, accurate to 10ms. | time.epoch;obs.exposure | 5 | 1 |
| [expMidpt](https://sdm-schemas.lsst.io/dp1.html#CcdVisit.expMidpt) | timestamp |  | Midpoint time for exposure at the fiducial center of the focal plane array. TAI, accurate to 10ms. |  | 6 |  |
| [obsStartMJD](https://sdm-schemas.lsst.io/dp1.html#CcdVisit.obsStartMJD) | double | d | Start of the exposure in MJD, TAI, accurate to 10ms. | time.start;obs.exposure | 7 |  |

Showing 1 to 50 of 50 entries

* * *

## [MPCORB](https://sdm-schemas.lsst.io/dp1.html\#MPCORB)

Orbit catalog produced by the Minor Planet Center based on submissions from DP1 processing. The columns are described at https://minorplanetcenter.net//iau/info/MPOrbitFormat.html .

Indexes

| Columns | Description | Reference Name |
| --- | --- | --- |
| [mpcDesignation](https://sdm-schemas.lsst.io/dp1.html#MPCORB.mpcDesignation) | Non-unique index on the mpcDesignation column | idx\_MPCORB\_mpcDesignation |
| [ssObjectId](https://sdm-schemas.lsst.io/dp1.html#MPCORB.ssObjectId) | Unique index on the ssObjectId column | idx\_MPCORB\_ssObjectId |

CSV

Search:

| Column Name | Data Type | Unit | Description | UCD | Order | Principal |
| --- | --- | --- | --- | --- | --- | --- |
| [e](https://sdm-schemas.lsst.io/dp1.html#MPCORB.e) | double |  | MPCORB: Orbital eccentricity |  |  |  |
| [epoch](https://sdm-schemas.lsst.io/dp1.html#MPCORB.epoch) | double | d | MPCORB: Epoch (in MJD, .0 TT) |  |  |  |
| [incl](https://sdm-schemas.lsst.io/dp1.html#MPCORB.incl) | double | deg | MPCORB: Inclination to the ecliptic, J2000.0 (degrees) |  |  |  |
| [mpcDesignation](https://sdm-schemas.lsst.io/dp1.html#MPCORB.mpcDesignation) | char |  | MPCORB: Number or provisional designation (in packed form) | meta.id;src |  |  |
| [mpcH](https://sdm-schemas.lsst.io/dp1.html#MPCORB.mpcH) | float | mag | MPCORB: Absolute magnitude, H |  |  |  |
| [node](https://sdm-schemas.lsst.io/dp1.html#MPCORB.node) | double | deg | MPCORB: Longitude of the ascending node, J2000.0 (degrees) |  |  |  |
| [peri](https://sdm-schemas.lsst.io/dp1.html#MPCORB.peri) | double | deg | MPCORB: Argument of perihelion, J2000.0 (degrees) |  |  |  |
| [q](https://sdm-schemas.lsst.io/dp1.html#MPCORB.q) | double | AU | MPCORB: Perihelion distance (AU) |  |  |  |
| [ssObjectId](https://sdm-schemas.lsst.io/dp1.html#MPCORB.ssObjectId) | long |  | LSST unique identifier (if observed by LSST) | meta.id;src |  |  |
| [t\_p](https://sdm-schemas.lsst.io/dp1.html#MPCORB.t_p) | double | d | MPCORB: MJD of pericentric passage |  |  |  |

Showing 1 to 10 of 10 entries

* * *

## [SSObject](https://sdm-schemas.lsst.io/dp1.html\#SSObject)

LSST-computed per-object quantities. 1:1 relationship with MPCORB.

Indexes

| Columns | Description | Reference Name |
| --- | --- | --- |
| [ssObjectId](https://sdm-schemas.lsst.io/dp1.html#SSObject.ssObjectId) | Unique index on the ssObjectId column | idx\_SSObject\_ssObjectId |

CSV

Search:

| Column Name | Data Type | Unit | Description | UCD | Order | Principal |
| --- | --- | --- | --- | --- | --- | --- |
| [discoverySubmissionDate](https://sdm-schemas.lsst.io/dp1.html#SSObject.discoverySubmissionDate) | double | d | The date the LSST first linked and submitted the discovery observations to the MPC. May be NULL if not an LSST discovery. The date format will follow general LSST conventions (MJD TAI, at the moment). |  |  |  |
| [numObs](https://sdm-schemas.lsst.io/dp1.html#SSObject.numObs) | int |  | Number of LSST observations of this object |  |  |  |
| [ssObjectId](https://sdm-schemas.lsst.io/dp1.html#SSObject.ssObjectId) | long |  | Unique identifier. | meta.id;src |  |  |

Showing 1 to 3 of 3 entries

* * *

## [SSSource](https://sdm-schemas.lsst.io/dp1.html\#SSSource)

LSST-computed per-source quantities. 1:1 relationship with DiaSource.

Indexes

| Columns | Description | Reference Name |
| --- | --- | --- |
| [diaSourceId](https://sdm-schemas.lsst.io/dp1.html#SSSource.diaSourceId) | Unique index on the diaSourceId column; accelerates joins between DiaSource and SSSource | idx\_SSSource\_diaSourceId |
| [ssObjectId](https://sdm-schemas.lsst.io/dp1.html#SSSource.ssObjectId) | Non-unique index on the ssObjectId column; accelerates retrieval of single-epoch data for SSObjects | idx\_SSSource\_ssObjectId |

CSV

Search:

| Column Name | Data Type | Unit | Description | UCD | Order | Principal |
| --- | --- | --- | --- | --- | --- | --- |
| [diaSourceId](https://sdm-schemas.lsst.io/dp1.html#SSSource.diaSourceId) | long |  | Unique identifier of the observation | meta.id;src |  |  |
| [eclipticBeta](https://sdm-schemas.lsst.io/dp1.html#SSSource.eclipticBeta) | double | deg | Ecliptic latitude |  |  |  |
| [eclipticLambda](https://sdm-schemas.lsst.io/dp1.html#SSSource.eclipticLambda) | double | deg | Ecliptic longitude |  |  |  |
| [galacticB](https://sdm-schemas.lsst.io/dp1.html#SSSource.galacticB) | double | deg | Galactic latitute |  |  |  |
| [galacticL](https://sdm-schemas.lsst.io/dp1.html#SSSource.galacticL) | double | deg | Galactic longitude |  |  |  |
| [heliocentricDist](https://sdm-schemas.lsst.io/dp1.html#SSSource.heliocentricDist) | float | AU | Heliocentric distance |  |  |  |
| [heliocentricVX](https://sdm-schemas.lsst.io/dp1.html#SSSource.heliocentricVX) | float | AU | Cartesian heliocentric X velocity (at the emit time) |  |  |  |
| [heliocentricVY](https://sdm-schemas.lsst.io/dp1.html#SSSource.heliocentricVY) | float | AU | Cartesian heliocentric Y velocity (at the emit time) |  |  |  |
| [heliocentricVZ](https://sdm-schemas.lsst.io/dp1.html#SSSource.heliocentricVZ) | float | AU | Cartesian heliocentric Z velocity (at the emit time) |  |  |  |
| [heliocentricX](https://sdm-schemas.lsst.io/dp1.html#SSSource.heliocentricX) | float | AU | Cartesian heliocentric X coordinate (at the emit time) |  |  |  |
| [heliocentricY](https://sdm-schemas.lsst.io/dp1.html#SSSource.heliocentricY) | float | AU | Cartesian heliocentric Y coordinate (at the emit time) |  |  |  |
| [heliocentricZ](https://sdm-schemas.lsst.io/dp1.html#SSSource.heliocentricZ) | float | AU | Cartesian heliocentric Z coordinate (at the emit time) |  |  |  |
| [phaseAngle](https://sdm-schemas.lsst.io/dp1.html#SSSource.phaseAngle) | float | deg | Phase angle |  |  |  |
| [residualDec](https://sdm-schemas.lsst.io/dp1.html#SSSource.residualDec) | double | deg | Residual Dec vs. ephemeris |  |  |  |
| [residualRa](https://sdm-schemas.lsst.io/dp1.html#SSSource.residualRa) | double | deg | Residual R.A. vs. ephemeris |  |  |  |
| [ssObjectId](https://sdm-schemas.lsst.io/dp1.html#SSSource.ssObjectId) | long |  | Unique identifier of the object. | meta.id;src |  |  |
| [topocentricDist](https://sdm-schemas.lsst.io/dp1.html#SSSource.topocentricDist) | float | AU | Topocentric distace |  |  |  |
| [topocentricVX](https://sdm-schemas.lsst.io/dp1.html#SSSource.topocentricVX) | float | AU | Cartesian topocentric X velocity (at the emit time) |  |  |  |
| [topocentricVY](https://sdm-schemas.lsst.io/dp1.html#SSSource.topocentricVY) | float | AU | Cartesian topocentric Y velocity (at the emit time) |  |  |  |
| [topocentricVZ](https://sdm-schemas.lsst.io/dp1.html#SSSource.topocentricVZ) | float | AU | Cartesian topocentric Z velocity (at the emit time) |  |  |  |
| [topocentricX](https://sdm-schemas.lsst.io/dp1.html#SSSource.topocentricX) | float | AU | Cartesian topocentric X coordinate (at the emit time) |  |  |  |
| [topocentricY](https://sdm-schemas.lsst.io/dp1.html#SSSource.topocentricY) | float | AU | Cartesian topocentric Y coordinate (at the emit time) |  |  |  |
| [topocentricZ](https://sdm-schemas.lsst.io/dp1.html#SSSource.topocentricZ) | float | AU | Cartesian topocentric Z coordinate (at the emit time) |  |  |  |

Showing 1 to 23 of 23 entries

* * *

[SDM Schemas](https://github.com/lsst/sdm_schemas) is maintained by
[Rubin Observatory](https://rubinobservatory.org/).

──────── [TRUNCATED] ────────
Showing 26,121 chars (head) + 8,641 chars (tail) of 345,350 total clean characters.
Full text saved to: /Users/duhokim/.hermes/profiles/tori2/cache/web/sdm-schemas.lsst.io-3126a63e3c.md
To read the omitted middle: read_file path="/Users/duhokim/.hermes/profiles/tori2/cache/web/sdm-schemas.lsst.io-3126a63e3c.md" offset=160 limit=200  (the file is the complete page; raise/lower offset to page through it).
─────────────────────────────