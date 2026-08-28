# URL: https://www.legacysurvey.org/dr10/catalogs/

[Skip to main content](https://www.legacysurvey.org/dr10/catalogs/#content)

## [south/tractor/<AAA>/tractor-<brick>.fits](https://www.legacysurvey.org/dr10/catalogs/\#toc-entry-1)

FITS binary table containing Tractor photometry. Before using these catalogs, note that there may be
[known issues](https://www.legacysurvey.org/dr10/issues) regarding their content and derivation. All flux-based quantities in the
catalogs are on the AB system (we specify that WISE fluxes are AB in the table for clarity, as
such quantities are often quoted on the Vega system).

| Name | Type | Units | Description |
| --- | --- | --- | --- |
| `release` | int16 |  | Integer denoting the camera and filter set used, which will be unique for a given processing run of the data ( [as documented here](https://www.legacysurvey.org/release)) |
| `brickid` | int32 |  | Brick ID \[1,662174\] |
| `brickname` | char\[8\] |  | Name of brick, encoding the brick sky position, eg "1126p222" near RA=112.6, Dec=+22.2 |
| `objid` | int32 |  | Catalog object number within this brick; a unique identifier hash is `release,brickid,objid`; `objid` spans \[0,N-1\] and is contiguously enumerated within each brick |
| `brick_primary` | boolean |  | `True` if the object is within the brick boundary |
| `maskbits` | int32 |  | Bitwise mask indicating that an object touches a pixel in the `coadd/*/*/*maskbits*` maps, as cataloged on the [DR10 bitmasks page](https://www.legacysurvey.org/dr10/bitmasks) |
| `fitbits` | int16 |  | Bitwise mask detailing pecularities of how an object was fit, as cataloged on the [DR10 bitmasks page](https://www.legacysurvey.org/dr10/bitmasks) |
| `type` | char\[3\] |  | Morphological model: "PSF"=stellar, "REX"="round exponential galaxy", "DEV"=deVauc, "EXP"=exponential, "SER"=Sersic, "DUP"=Gaia source fit by different model. See also [the larger description](https://www.legacysurvey.org/dr10/description/#morphological-classification). |
| `ra` | float64 | deg | Right ascension at equinox J2000 |
| `dec` | float64 | deg | Declination at equinox J2000 |
| `ra_ivar` | float32 | 1/deg² | Inverse variance of RA (no cosine term!), excluding astrometric calibration errors |
| `dec_ivar` | float32 | 1/deg² | Inverse variance of DEC, excluding astrometric calibration errors |
| `bx` | float32 | pix | X position (0-indexed) of coordinates in the brick image stack ( _i.e._ in the _e.g._ legacysurvey-<brick>-image-g.fits.fz [coadd file](https://www.legacysurvey.org/dr10/files/#image-stacks-south-coadd)) |
| `by` | float32 | pix | Y position (0-indexed) of coordinates in brick image stack |
| `dchisq` | float32\[5\] |  | Difference in χ² between successively more-complex model fits: PSF, REX, DEV, EXP, SER. The difference is versus no source. |
| `ebv` | float32 | mag | Galactic extinction E(B-V) reddening from [SFD98](https://ui.adsabs.harvard.edu/abs/1998ApJ...500..525S/abstract), used to compute the `mw_transmission_` columns |
| `mjd_min` | float64 | days | Minimum Modified Julian Date of observations used to construct the model of this object |
| `mjd_max` | float64 | days | Maximum Modified Julian Date of observations used to construct the model of this object |
| `ref_cat` | char\[2\] |  | Reference catalog source for this star: "T2" for [Tycho-2](https://heasarc.gsfc.nasa.gov/W3Browse/all/tycho2.html), "GE" for [Gaia EDR3](https://gea.esac.esa.int/archive/documentation/GEDR3/Gaia_archive/chap_datamodel/sec_dm_main_tables/ssec_dm_gaia_source.html), "L3" for the [SGA](https://www.legacysurvey.org/sga/sga2020), empty otherwise |
| `ref_id` | int64 |  | Reference catalog identifier for this star; Tyc1\*1,000,000+Tyc2\*10+Tyc3 for Tycho2; "sourceid" for [Gaia EDR3](https://gea.esac.esa.int/archive/documentation/GEDR3/Gaia_archive/chap_datamodel/sec_dm_main_tables/ssec_dm_gaia_source.html) and [SGA](https://www.legacysurvey.org/sga/sga2020) |
| `pmra` | float32 | mas/yr | Reference catalog proper motion in RA direction (μ∗α≡μαcosδμα∗≡μαcos⁡δ) in the ICRS at `ref_epoch` |
| `pmdec` | float32 | mas/yr | Reference catalog proper motion in Dec direction (μδμδ) in the ICRS at `ref_epoch` |
| `parallax` | float32 | mas | Reference catalog parallax |
| `pmra_ivar` | float32 | 1/(mas/yr)² | Reference catalog inverse-variance on `pmra` |
| `pmdec_ivar` | float32 | 1/(mas/yr)² | Reference catalog inverse-variance on `pmdec` |
| `parallax_ivar` | float32 | 1/mas² | Reference catalog inverse-variance on `parallax` |
| `ref_epoch` | float32 | yr | Reference catalog reference epoch (eg, 2015.5 for [Gaia EDR3](https://gea.esac.esa.int/archive/documentation/GEDR3/Gaia_archive/chap_datamodel/sec_dm_main_tables/ssec_dm_gaia_source.html)) |
| `gaia_phot_g_mean_mag` | float32 | mag | [Gaia EDR3](https://gea.esac.esa.int/archive/documentation/GEDR3/Gaia_archive/chap_datamodel/sec_dm_main_tables/ssec_dm_gaia_source.html) G band mag |
| `gaia_phot_g_mean_flux_over_error` | float32 |  | [Gaia EDR3](https://gea.esac.esa.int/archive/documentation/GEDR3/Gaia_archive/chap_datamodel/sec_dm_main_tables/ssec_dm_gaia_source.html) G band signal-to-noise |
| `gaia_phot_g_n_obs` | int16 |  | [Gaia EDR3](https://gea.esac.esa.int/archive/documentation/GEDR3/Gaia_archive/chap_datamodel/sec_dm_main_tables/ssec_dm_gaia_source.html) G band number of observations |
| `gaia_phot_bp_mean_mag` | float32 | mag | [Gaia EDR3](https://gea.esac.esa.int/archive/documentation/GEDR3/Gaia_archive/chap_datamodel/sec_dm_main_tables/ssec_dm_gaia_source.html) BP mag |
| `gaia_phot_bp_mean_flux_over_error` | float32 |  | [Gaia EDR3](https://gea.esac.esa.int/archive/documentation/GEDR3/Gaia_archive/chap_datamodel/sec_dm_main_tables/ssec_dm_gaia_source.html) BP signal-to-noise |
| `gaia_phot_bp_n_obs` | int16 |  | [Gaia EDR3](https://gea.esac.esa.int/archive/documentation/GEDR3/Gaia_archive/chap_datamodel/sec_dm_main_tables/ssec_dm_gaia_source.html) BP number of observations |
| `gaia_phot_rp_mean_mag` | float32 | mag | [Gaia EDR3](https://gea.esac.esa.int/archive/documentation/GEDR3/Gaia_archive/chap_datamodel/sec_dm_main_tables/ssec_dm_gaia_source.html) RP mag |
| `gaia_phot_rp_mean_flux_over_error` | float32 |  | [Gaia EDR3](https://gea.esac.esa.int/archive/documentation/GEDR3/Gaia_archive/chap_datamodel/sec_dm_main_tables/ssec_dm_gaia_source.html) RP signal-to-noise |
| `gaia_phot_rp_n_obs` | int16 |  | [Gaia EDR3](https://gea.esac.esa.int/archive/documentation/GEDR3/Gaia_archive/chap_datamodel/sec_dm_main_tables/ssec_dm_gaia_source.html) RP number of observations |
| `gaia_phot_variable_flag` | bool |  | [Gaia EDR3](https://gea.esac.esa.int/archive/documentation/GEDR3/Gaia_archive/chap_datamodel/sec_dm_main_tables/ssec_dm_gaia_source.html) photometric variable flag |
| `gaia_astrometric_excess_noise` | float32 |  | [Gaia EDR3](https://gea.esac.esa.int/archive/documentation/GEDR3/Gaia_archive/chap_datamodel/sec_dm_main_tables/ssec_dm_gaia_source.html) astrometric excess noise |
| `gaia_astrometric_excess_noise_sig` | float32 |  | [Gaia EDR3](https://gea.esac.esa.int/archive/documentation/GEDR3/Gaia_archive/chap_datamodel/sec_dm_main_tables/ssec_dm_gaia_source.html) astrometric excess noise uncertainty |
| `gaia_astrometric_n_obs_al` | int16 |  | [Gaia EDR3](https://gea.esac.esa.int/archive/documentation/GEDR3/Gaia_archive/chap_datamodel/sec_dm_main_tables/ssec_dm_gaia_source.html) number of astrometric observations along scan direction |
| `gaia_astrometric_n_good_obs_al` | int16 |  | [Gaia EDR3](https://gea.esac.esa.int/archive/documentation/GEDR3/Gaia_archive/chap_datamodel/sec_dm_main_tables/ssec_dm_gaia_source.html) number of good astrometric observations along scan direction |
| `gaia_astrometric_weight_al` | float32 |  | [Gaia EDR3](https://gea.esac.esa.int/archive/documentation/GEDR3/Gaia_archive/chap_datamodel/sec_dm_main_tables/ssec_dm_gaia_source.html) astrometric weight along scan direction |
| `gaia_duplicated_source` | bool |  | [Gaia EDR3](https://gea.esac.esa.int/archive/documentation/GEDR3/Gaia_archive/chap_datamodel/sec_dm_main_tables/ssec_dm_gaia_source.html) duplicated source flag |
| `gaia_a_g_val` | float32 | magnitudes | [Gaia EDR3](https://gea.esac.esa.int/archive/documentation/GEDR3/Gaia_archive/chap_datamodel/sec_dm_main_tables/ssec_dm_gaia_source.html) line-of-sight extinction in the G band |
| `gaia_e_bp_min_rp_val` | float32 | magnitudes | [Gaia EDR3](https://gea.esac.esa.int/archive/documentation/GEDR3/Gaia_archive/chap_datamodel/sec_dm_main_tables/ssec_dm_gaia_source.html) line-of-sight reddening E(BP-RP) |
| `gaia_phot_bp_rp_excess_factor` | float32 |  | [Gaia EDR3](https://gea.esac.esa.int/archive/documentation/GEDR3/Gaia_archive/chap_datamodel/sec_dm_main_tables/ssec_dm_gaia_source.html) BP/RP excess factor |
| `gaia_astrometric_sigma5d_max` | float32 | mas | [Gaia EDR3](https://gea.esac.esa.int/archive/documentation/GEDR3/Gaia_archive/chap_datamodel/sec_dm_main_tables/ssec_dm_gaia_source.html) longest semi-major axis of the 5-d error ellipsoid |
| `gaia_astrometric_params_solved` | uint8 |  | Which astrometric parameters were estimated for a [Gaia EDR3](https://gea.esac.esa.int/archive/documentation/GEDR3/Gaia_archive/chap_datamodel/sec_dm_main_tables/ssec_dm_gaia_source.html) source |
| `flux_g` | float32 | nanomaggy | model flux in gg |
| `flux_r` | float32 | nanomaggy | model flux in rr |
| `flux_i` | float32 | nanomaggy | model flux in ii |
| `flux_z` | float32 | nanomaggy | model flux in zz |
| `flux_w1` | float32 | nanomaggy | WISE model flux in W1W1 (AB system) |
| `flux_w2` | float32 | nanomaggy | WISE model flux in W2W2 (AB) |
| `flux_w3` | float32 | nanomaggy | WISE model flux in W3W3 (AB) |
| `flux_w4` | float32 | nanomaggy | WISE model flux in W4W4 (AB) |
| `flux_ivar_g` | float32 | 1/nanomaggy² | Inverse variance of `flux_g` |
| `flux_ivar_r` | float32 | 1/nanomaggy² | Inverse variance of `flux_r` |
| `flux_ivar_i` | float32 | 1/nanomaggy² | Inverse variance of `flux_i` |
| `flux_ivar_z` | float32 | 1/nanomaggy² | Inverse variance of `flux_z` |
| `flux_ivar_w1` | float32 | 1/nanomaggy² | Inverse variance of `flux_w1` (AB system) |
| `flux_ivar_w2` | float32 | 1/nanomaggy² | Inverse variance of `flux_w2` (AB) |
| `flux_ivar_w3` | float32 | 1/nanomaggy² | Inverse variance of `flux_w3` (AB) |
| `flux_ivar_w4` | float32 | 1/nanomaggy² | Inverse variance of `flux_w4` (AB) |
| `fiberflux_g` | float32 | nanomaggy | Predicted gg-band flux within a fiber of diameter 1.5 arcsec from this object in 1 arcsec Gaussian seeing |
| `fiberflux_r` | float32 | nanomaggy | Predicted rr-band flux within a fiber of diameter 1.5 arcsec from this object in 1 arcsec Gaussian seeing |
| `fiberflux_i` | float32 | nanomaggy | Predicted ii-band flux within a fiber of diameter 1.5 arcsec from this object in 1 arcsec Gaussian seeing |
| `fiberflux_z` | float32 | nanomaggy | Predicted zz-band flux within a fiber of diameter 1.5 arcsec from this object in 1 arcsec Gaussian seeing |
| `fibertotflux_g` | float32 | nanomaggy | Predicted gg-band flux within a fiber of diameter 1.5 arcsec from all sources at this location in 1 arcsec Gaussian seeing |
| `fibertotflux_r` | float32 | nanomaggy | Predicted rr-band flux within a fiber of diameter 1.5 arcsec from all sources at this location in 1 arcsec Gaussian seeing |
| `fibertotflux_i` | float32 | nanomaggy | Predicted ii-band flux within a fiber of diameter 1.5 arcsec from all sources at this location in 1 arcsec Gaussian seeing |
| `fibertotflux_z` | float32 | nanomaggy | Predicted zz-band flux within a fiber of diameter 1.5 arcsec from all sources at this location in 1 arcsec Gaussian seeing |
| `apflux_g` | float32\[8\] | nanomaggy | Aperture fluxes on the co-added images in apertures of radius \[0.5, 0.75, 1.0, 1.5, 2.0, 3.5, 5.0, 7.0\] arcsec in gg, masked by invvar=0invvar=0 (inverse variance of zero [\[1\]](https://www.legacysurvey.org/dr10/catalogs/#footnote-1)) |
| `apflux_r` | float32\[8\] | nanomaggy | Aperture fluxes on the co-added images in apertures of radius \[0.5, 0.75, 1.0, 1.5, 2.0, 3.5, 5.0, 7.0\] arcsec in rr, masked by invvar=0invvar=0 |
| `apflux_i` | float32\[8\] | nanomaggy | Aperture fluxes on the co-added images in apertures of radius \[0.5, 0.75, 1.0, 1.5, 2.0, 3.5, 5.0, 7.0\] arcsec in ii, masked by invvar=0invvar=0 |
| `apflux_z` | float32\[8\] | nanomaggy | Aperture fluxes on the co-added images in apertures of radius \[0.5, 0.75, 1.0, 1.5, 2.0, 3.5, 5.0, 7.0\] arcsec in zz, masked by invvar=0invvar=0 |
| `apflux_resid_g` | float32\[8\] | nanomaggy | Aperture fluxes on the co-added residual images in gg, masked by invvar=0invvar=0 |
| `apflux_resid_r` | float32\[8\] | nanomaggy | Aperture fluxes on the co-added residual images in rr, masked by invvar=0invvar=0 |
| `apflux_resid_i` | float32\[8\] | nanomaggy | Aperture fluxes on the co-added residual images in ii, masked by invvar=0invvar=0 |
| `apflux_resid_z` | float32\[8\] | nanomaggy | Aperture fluxes on the co-added residual images in zz, masked by invvar=0invvar=0 |
| `apflux_blobresid_g` | float32\[8\] | nanomaggy | Aperture fluxes on image−blobmodelimage−blobmodel residual maps in gg [\[2\]](https://www.legacysurvey.org/dr10/catalogs/#footnote-2), masked by invvar=0invvar=0 |
| `apflux_blobresid_r` | float32\[8\] | nanomaggy | Aperture fluxes on image−blobmodelimage−blobmodel residual maps in rr, masked by invvar=0invvar=0 |
| `apflux_blobresid_i` | float32\[8\] | nanomaggy | Aperture fluxes on image−blobmodelimage−blobmodel residual maps in ii, masked by invvar=0invvar=0 |
| `apflux_blobresid_z` | float32\[8\] | nanomaggy | Aperture fluxes on image−blobmodelimage−blobmodel residual maps in zz, masked by invvar=0invvar=0 |
| `apflux_ivar_g` | float32\[8\] | 1/nanomaggy² | Inverse variance of `apflux_resid_g`, masked by invvar=0invvar=0 |
| `apflux_ivar_r` | float32\[8\] | 1/nanomaggy² | Inverse variance of `apflux_resid_r`, masked by invvar=0invvar=0 |
| `apflux_ivar_i` | float32\[8\] | 1/nanomaggy² | Inverse variance of `apflux_resid_i`, masked by invvar=0invvar=0 |
| `apflux_ivar_z` | float32\[8\] | 1/nanomaggy² | Inverse variance of `apflux_resid_z`, masked by invvar=0invvar=0 |
| `apflux_masked_g` | float32\[8\] |  | Fraction of pixels masked in gg-band aperture flux measurements; 1 means fully masked (ie, fully ignored; contributing zero to the measurement) |
| `apflux_masked_r` | float32\[8\] |  | Fraction of pixels masked in rr-band aperture flux measurements; 1 means fully masked (ie, fully ignored; contributing zero to the measurement) |
| `apflux_masked_i` | float32\[8\] |  | Fraction of pixels masked in ii-band aperture flux measurements; 1 means fully masked (ie, fully ignored; contributing zero to the measurement) |
| `apflux_masked_z` | float32\[8\] |  | Fraction of pixels masked in zz-band aperture flux measurements; 1 means fully masked (ie, fully ignored; contributing zero to the measurement) |
| `apflux_w1` | float32\[5\] | nanomaggy | Aperture fluxes on the co-added images in apertures of radius \[3, 5, 7, 9, 11\] [\[3\]](https://www.legacysurvey.org/dr10/catalogs/#footnote-3) arcsec in W1W1, masked by invvar=0invvar=0 |
| `apflux_w2` | float32\[5\] | nanomaggy | Aperture fluxes on the co-added images in apertures of radius \[3, 5, 7, 9, 11\] arcsec in W2W2, masked by invvar=0invvar=0 |
| `apflux_w3` | float32\[5\] | nanomaggy | Aperture fluxes on the co-added images in apertures of radius \[3, 5, 7, 9, 11\] arcsec in W3W3, masked by invvar=0invvar=0 |
| `apflux_w4` | float32\[5\] | nanomaggy | Aperture fluxes on the co-added images in apertures of radius \[3, 5, 7, 9, 11\] arcsec in W4W4, masked by invvar=0invvar=0 |
| `apflux_resid_w1` | float32\[5\] | nanomaggy | Aperture fluxes on the co-added residual images in W1W1, masked by invvar=0invvar=0 |
| `apflux_resid_w2` | float32\[5\] | nanomaggy | Aperture fluxes on the co-added residual images in W2W2, masked by invvar=0invvar=0 |
| `apflux_resid_w3` | float32\[5\] | nanomaggy | Aperture fluxes on the co-added residual images in W3W3, masked by invvar=0invvar=0 |
| `apflux_resid_w4` | float32\[5\] | nanomaggy | Aperture fluxes on the co-added residual images in W4W4, masked by invvar=0invvar=0 |
| `apflux_ivar_w1` | float32\[5\] | 1/nanomaggy² | Inverse variance of `apflux_resid_w1`, masked by invvar=0invvar=0 |
| `apflux_ivar_w2` | float32\[5\] | 1/nanomaggy² | Inverse variance of `apflux_resid_w2`, masked by invvar=0invvar=0 |
| `apflux_ivar_w3` | float32\[5\] | 1/nanomaggy² | Inverse variance of `apflux_resid_w3`, masked by invvar=0invvar=0 |
| `apflux_ivar_w4` | float32\[5\] | 1/nanomaggy² | Inverse variance of `apflux_resid_w4`, masked by invvar=0invvar=0 |
| `mw_transmission_g` | float32 |  | Galactic transmission in gg filter in linear units \[0, 1\] |
| `mw_transmission_r` | float32 |  | Galactic transmission in rr filter in linear units \[0, 1\] |
| `mw_transmission_i` | float32 |  | Galactic transmission in ii filter in linear units \[0, 1\] |
| `mw_transmission_z` | float32 |  | Galactic transmission in zz filter in linear units \[0, 1\] |
| `mw_transmission_w1` | float32 |  | Galactic transmission in W1W1 filter in linear units \[0, 1\] |
| `mw_transmission_w2` | float32 |  | Galactic transmission in W2W2 filter in linear units \[0, 1\] |
| `mw_transmission_w3` | float32 |  | Galactic transmission in W3W3 filter in linear units \[0, 1\] |
| `mw_transmission_w4` | float32 |  | Galactic transmission in W4W4 filter in linear units \[0, 1\] |
| `nobs_g` | int16 |  | Number of images that contribute to the central pixel in gg filter for this object (not profile-weighted) |
| `nobs_r` | int16 |  | Number of images that contribute to the central pixel in rr filter for this object (not profile-weighted) |
| `nobs_i` | int16 |  | Number of images that contribute to the central pixel in ii filter for this object (not profile-weighted) |
| `nobs_z` | int16 |  | Number of images that contribute to the central pixel in zz filter for this object (not profile-weighted) |
| `nobs_w1` | int16 |  | Number of images that contribute to the central pixel in W1W1 filter for this object (not profile-weighted) |
| `nobs_w2` | int16 |  | Number of images that contribute to the central pixel in W2W2 filter for this object (not profile-weighted) |
| `nobs_w3` | int16 |  | Number of images that contribute to the central pixel in W3W3 filter for this object (not profile-weighted) |
| `nobs_w4` | int16 |  | Number of images that contribute to the central pixel in W4W4 filter for this object (not profile-weighted) |
| `rchisq_g` | float32 |  | Profile-weighted χ² of model fit normalized by the number of pixels in gg |
| `rchisq_r` | float32 |  | Profile-weighted χ² of model fit normalized by the number of pixels in rr |
| `rchisq_i` | float32 |  | Profile-weighted χ² of model fit normalized by the number of pixels in ii |
| `rchisq_z` | float32 |  | Profile-weighted χ² of model fit normalized by the number of pixels in zz |
| `rchisq_w1` | float32 |  | Profile-weighted χ² of model fit normalized by the number of pixels in W1W1 |
| `rchisq_w2` | float32 |  | Profile-weighted χ² of model fit normalized by the number of pixels in W2W2 |
| `rchisq_w3` | float32 |  | Profile-weighted χ² of model fit normalized by the number of pixels in W3W3 |
| `rchisq_w4` | float32 |  | Profile-weighted χ² of model fit normalized by the number of pixels in W4W4 |
| `fracflux_g` | float32 |  | Profile-weighted fraction of the flux from other sources divided by the total flux in gg (typically \[0,1\]) |
| `fracflux_r` | float32 |  | Profile-weighted fraction of the flux from other sources divided by the total flux in rr (typically \[0,1\]) |
| `fracflux_i` | float32 |  | Profile-weighted fraction of the flux from other sources divided by the total flux in ii (typically \[0,1\]) |
| `fracflux_z` | float32 |  | Profile-weighted fraction of the flux from other sources divided by the total flux in zz (typically \[0,1\]) |
| `fracflux_w1` | float32 |  | Profile-weighted fraction of the flux from other sources divided by the total flux in W1W1 (typically \[0,1\]) |
| `fracflux_w2` | float32 |  | Profile-weighted fraction of the flux from other sources divided by the total flux in W2W2 (typically \[0,1\]) |
| `fracflux_w3` | float32 |  | Profile-weighted fraction of the flux from other sources divided by the total flux in W3W3 (typically \[0,1\]) |
| `fracflux_w4` | float32 |  | Profile-weighted fraction of the flux from other sources divided by the total flux in W4W4 (typically \[0,1\]) |
| `fracmasked_g` | float32 |  | Profile-weighted fraction of pixels masked from all observations of this object in gg, strictly between \[0,1\] |
| `fracmasked_r` | float32 |  | Profile-weighted fraction of pixels masked from all observations of this object in rr, strictly between \[0,1\] |
| `fracmasked_i` | float32 |  | Profile-weighted fraction of pixels masked from all observations of this object in ii, strictly between \[0,1\] |
| `fracmasked_z` | float32 |  | Profile-weighted fraction of pixels masked from all observations of this object in zz, strictly between \[0,1\] |
| `fracin_g` | float32 |  | Fraction of a source's flux within the blob in gg, near unity for real sources |
| `fracin_r` | float32 |  | Fraction of a source's flux within the blob in rr, near unity for real sources |
| `fracin_i` | float32 |  | Fraction of a source's flux within the blob in ii, near unity for real sources |
| `fracin_z` | float32 |  | Fraction of a source's flux within the blob in zz, near unity for real sources |
| `ngood_g` | int16 |  | Number of good (unmasked) images that contribute in gg (this quantity is consistent with the nexp maps in the [image stacks](https://www.legacysurvey.org/dr10/files/#image-stacks-south-coadd)) |
| `ngood_r` | int16 |  | Number of good (unmasked) images that contribute in rr (this quantity is consistent with the nexp maps in the [image stacks](https://www.legacysurvey.org/dr10/files/#image-stacks-south-coadd)) |
| `ngood_i` | int16 |  | Number of good (unmasked) images that contribute in ii (this quantity is consistent with the nexp maps in the [image stacks](https://www.legacysurvey.org/dr10/files/#image-stacks-south-coadd)) |
| `ngood_z` | int16 |  | Number of good (unmasked) images that contribute in zz (this quantity is consistent with the nexp maps in the [image stacks](https://www.legacysurvey.org/dr10/files/#image-stacks-south-coadd)) |

[... middle omitted — see footer ...]

| `lc_flux_w2` | float32\[17\] | nanomaggy | `flux_w2` in each of up to seventeen unWISE coadd epochs (AB; defaults to zero for unused entries) |
| `lc_flux_ivar_w1` | float32\[17\] | 1/nanomaggy² | Inverse variance of `lc_flux_w1` (AB system; defaults to zero for unused entries) |
| `lc_flux_ivar_w2` | float32\[17\] | 1/nanomaggy² | Inverse variance of `lc_flux_w2` (AB; defaults to zero for unused entries) |
| `lc_nobs_w1` | int16\[17\] |  | `nobs_w1` in each of up to seventeen unWISE coadd epochs |
| `lc_nobs_w2` | int16\[17\] |  | `nobs_w2` in each of up to seventeen unWISE coadd epochs |
| `lc_fracflux_w1` | float32\[17\] |  | `fracflux_w1` in each of up to seventeen unWISE coadd epochs (defaults to zero for unused entries) |
| `lc_fracflux_w2` | float32\[17\] |  | `fracflux_w2` in each of up to seventeen unWISE coadd epochs (defaults to zero for unused entries) |
| `lc_rchisq_w1` | float32\[17\] |  | `rchisq_w1` in each of up to seventeen unWISE coadd epochs (defaults to zero for unused entries) |
| `lc_rchisq_w2` | float32\[17\] |  | `rchisq_w2` in each of up to seventeen unWISE coadd epochs (defaults to zero for unused entries) |
| `lc_mjd_w1` | float64\[17\] |  | `mjd_w1` in each of up to seventeen unWISE coadd epochs (defaults to zero for unused entries) |
| `lc_mjd_w2` | float64\[17\] |  | `mjd_w2` in each of up to seventeen unWISE coadd epochs (defaults to zero for unused entries) |
| `lc_epoch_index_w1` | int16\[17\] |  | Index number of unWISE epoch for W1 (defaults to -1 for unused entries) |
| `lc_epoch_index_w2` | int16\[17\] |  | Index number of unWISE epoch for W2 (defaults to -1 for unused entries) |
| `sersic` | float32 |  | Power-law index for the Sersic profile model (`type="SER"`) |
| `sersic_ivar` | float32 |  | Inverse variance of `sersic` |
| `shape_r` | float32 | arcsec | Half-light radius of galaxy model for galaxy type `type` (>0) |
| `shape_r_ivar` | float32 | 1/arcsec² | Inverse variance of `shape_r` |
| `shape_e1` | float32 |  | Ellipticity component 1 of galaxy model for galaxy type `type` |
| `shape_e1_ivar` | float32 |  | Inverse variance of `shape_e1` |
| `shape_e2` | float32 |  | Ellipticity component 2 of galaxy model for galaxy type `type` |
| `shape_e2_ivar` | float32 |  | Inverse variance of `shape_e2` |

## [Goodness-of-Fits and Morphological `type`](https://www.legacysurvey.org/dr10/catalogs/\#toc-entry-2)

The `dchisq` values represent the χ² sum of all pixels in the source's blob
for various models. This 5-element vector contains the χ² difference between
the best-fit point source (type="PSF"), round exponential galaxy model ("REX"),
de Vaucouleurs model ("DEV"), exponential model ("EXP"), and a Sersic model ("SER"), in that order. Note that the Sersic model replaces the composite ("COMP") model used in [DR8](https://www.legacysurvey.org/dr8/catalogs) (and before).
The "REX" model is a round exponential galaxy profile with a variable radius
and is meant to capture slightly-extended but low signal-to-noise objects.
The `dchisq` values are the χ² difference versus no source in this location---that is, it is the improvement from adding the given source to our model of the sky. The first element (for PSF) corresponds to a traditional notion of detection significance.
Note that the `dchisq` values are negated so that positive values indicate better fits.
We penalize models with negative flux in a band by subtracting rather than adding its χ² improvement in that band.

The `rchisq` values are interpreted as the reduced χ² pixel-weighted by the model fit,
computed as the following sum over pixels in the blob for each object:

χ2=∑\[(image−model)2×model×inversevariance\]∑\[model\]χ2=∑\[(image−model)2×model×inversevariance\]∑\[model\]

The above sum is over all images contributing to a particular filter, and can be negative-valued for sources
that have a flux measured as negative in some bands where they are not detected.

The final, additional moropholigical type is "DUP." This type is set for Gaia sources that are coincident with, and so have been fit by, an extended source.
No optical flux is assigned to `DUP` sources, but they are retained to ensure that all Gaia sources appear in the catalogs even if Tractor prefers an alternate fit.

## [Galactic Extinction Coefficients](https://www.legacysurvey.org/dr10/catalogs/\#toc-entry-3)

The Galactic extinction values are derived from the [SFD98](https://ui.adsabs.harvard.edu/abs/1998ApJ...500..525S/abstract) maps, but with updated coefficients to
convert E(B-V) to the extinction in each filter. These are reported in linear units of transmission,
with 1 representing a fully transparent region of the Milky Way and 0 representing a fully opaque region.
The value can slightly exceed unity owing to noise in the [SFD98](https://ui.adsabs.harvard.edu/abs/1998ApJ...500..525S/abstract) maps, although it is never below 0.

Eddie Schlafly has computed the extinction coefficients for the DECam filters through airmass=1.3, computed for a 7000K source spectrum as was
done in the Appendix of [Schlafly & Finkbeiner (2011)](https://ui.adsabs.harvard.edu/abs/2011ApJ...737..103S/abstract).
These coefficients are A/E(B−V)A/E(B−V) = 3.995, 3.214, 2.165, 1.592, 1.211, 1.064
for the DECam uu, gg, rr, ii, zz, YY filters,
respectively. Note that these are _slightly_ different from the coefficients in [Schlafly & Finkbeiner (2011)](https://ui.adsabs.harvard.edu/abs/2011ApJ...737..103S/abstract).
The coefficients are multiplied by the [SFD98](https://ui.adsabs.harvard.edu/abs/1998ApJ...500..525S/abstract) E(B-V) values at the coordinates
of each object to derive the gg, rr and zz`mw_transmission` values in the Legacy Surveys catalogs. The coefficients at different airmasses
only change by a small amount, with the largest effect in gg-band where the coefficient would be 3.219 at airmass=1 and 3.202 at airmass=2.

We calculate Galactic extinction for [BASS](https://www.legacysurvey.org/bass) and [MzLS](https://www.legacysurvey.org/mzls) as if they are on the DECam filter system.

The coefficients for the four WISE filters are derived from [Fitzpatrick (1999)](https://ui.adsabs.harvard.edu/abs/1999PASP..111...63F/abstract), as recommended by [Schlafly & Finkbeiner (2011)](https://ui.adsabs.harvard.edu/abs/2011ApJ...737..103S/abstract),
considered better than either the [Cardelli et al. (1989)](https://ui.adsabs.harvard.edu/abs/1989ApJ...345..245C/abstract) curves or the newer [Fitzpatrick & Massa (2009)](https://ui.adsabs.harvard.edu/abs/2009ApJ...699.1209F/abstract) NIR curve (which is not vetted beyond 2 microns).
These coefficients are A / E(B-V) = 0.184, 0.113, 0.0241, 0.00910.

## [Ellipticities](https://www.legacysurvey.org/dr10/catalogs/\#toc-entry-4)

The ellipticities for each galaxy `type` (i.e. `shape_e1`, `shape_e2`) are different from the usual
eccentricity, e≡1−(b/a)2−−−−−−−−√e≡1−(b/a)2. In gravitational lensing
studies, the ellipticity is taken to be a complex number:

ϵ=a−ba+bexp(2iϕ)=ϵ1+iϵ2ϵ=a−ba+bexp⁡(2iϕ)=ϵ1+iϵ2

Where ϕ is the position angle with a range of 180°, due to the
ellipse's symmetry. Going between r,ϵ1,ϵ2r,ϵ1,ϵ2
and r,b/a,ϕr,b/a,ϕ:

r\|ϵ\|baϕ\|ϵ\|ϵ1ϵ2=======rϵ21+ϵ22−−−−−−√1−\|ϵ\|1+\|ϵ\|12arctanϵ2ϵ11−b/a1+b/a\|ϵ\|cos(2ϕ)\|ϵ\|sin(2ϕ)r=r\|ϵ\|=ϵ12+ϵ22ba=1−\|ϵ\|1+\|ϵ\|ϕ=12arctan⁡ϵ2ϵ1\|ϵ\|=1−b/a1+b/aϵ1=\|ϵ\|cos⁡(2ϕ)ϵ2=\|ϵ\|sin⁡(2ϕ)

**Footnotes**

──────── [TRUNCATED] ────────
Showing 22,366 chars (head) + 7,363 chars (tail) of 35,608 total clean characters.
Full text saved to: /Users/duhokim/.hermes/profiles/tori2/cache/web/www.legacysurvey.org-5f61a3740a.md
To read the omitted middle: read_file path="/Users/duhokim/.hermes/profiles/tori2/cache/web/www.legacysurvey.org-5f61a3740a.md" offset=160 limit=200  (the file is the complete page; raise/lower offset to page through it).
─────────────────────────────