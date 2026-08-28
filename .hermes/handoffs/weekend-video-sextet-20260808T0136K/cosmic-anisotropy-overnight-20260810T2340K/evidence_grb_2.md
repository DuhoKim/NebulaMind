URL: https://fermi.gsfc.nasa.gov/ssc/data/

[Skip to main content](https://fermi.gsfc.nasa.gov/ssc/data/#main-content)

# Data & Products

The Fermi mission provides an extensive array of data products, with [no proprietary period](https://fermi.gsfc.nasa.gov/ssc/data/policy/) and minimal latency between observation and public release. Primary products are [all-sky survey data](https://fermi.gsfc.nasa.gov/ssc/data/#allsky-panel) from the LAT and [transient event data](https://fermi.gsfc.nasa.gov/ssc/data/#time-panel) (e.g, GRBs) from the GBM. Derived products include the [LAT Point Source Catalog](https://fermi.gsfc.nasa.gov/ssc/data/access/lat/fl16y/), and specialized catalogs for active galactic nuclei, pulsars, gamma-ray bursts, and high-energy sources, as well as [light curves](https://fermi.gsfc.nasa.gov/ssc/data/access/lat/psc/) and variability information for [monitored sources](https://fermi.gsfc.nasa.gov/ssc/data/access/lat/msl_lc/). You should have a [basic familiarity](https://fermi.gsfc.nasa.gov/overview.html) with Fermi before proceeding further. Tools to analyze Fermi data and documentation (e.g., how-to guides) are available under the [Data Analysis](https://fermi.gsfc.nasa.gov/ssc/data/analysis/) section. Note that the LAT and GBM data are accompanied by [caveats](https://fermi.gsfc.nasa.gov/ssc/data/analysis/caveats.html) about their use.

- #### All-Sky Survey Data







The Fermi observatory operates primarily in an all-sky scanning [survey mode](https://fermi.gsfc.nasa.gov/ssc/observations/types/allsky/) that alternates between the northern and southern hemispheres each orbit (roughly 90 minutes) to maximize observing time while maintaining exposure uniformity. The GBM sees the entire unocculted sky. The LAT field of view covers approximately 20% of the sky at any given time, and the scanning strategy provides coverage of the entire sky approximately every three hours. The LAT rarely stares at a single point in the sky for an extended period.




## Accessing LAT Data




LAT survey data consist of lists of gamma-ray photons from across the entire sky and spacecraft pointing information that can be analyzed using software like the [Fermitools](https://fermi.gsfc.nasa.gov/ssc/data/analysis). See [LAT data products](https://fermi.gsfc.nasa.gov/ssc/data/access/data_products.html#lat) for a description of the file types.




### Interactive Data Server



The [LAT Data Server](https://fermi.gsfc.nasa.gov/cgi-bin/ssc/LAT/LATDataQuery.cgi) allows you to search and retrieve LAT data based on position, time, energy, and other parameters. After you enter your query, the data server will provide a query ID and status page you can monitor. Depending on the size of your query and server load, processing may take some time. You can return later and enter your query ID into the [query results](https://fermi.gsfc.nasa.gov/cgi-bin/ssc/LAT/QueryResults.cgi) form to check the status.





The [Space Science Data Center](https://fermi.ssdc.asi.it/) (SSDC) in Italy operates their own [data server](https://tools.ssdc.asi.it/fermi.jsp), which may be more convenient for some users.




### Direct Archive Access



The Fermi [data archive](https://heasarc.gsfc.nasa.gov/FTP/fermi/) hosted by HEASARC contains compilations of survey data organized into weekly packages for [convenient download and analysis](https://github.com/fermi-lat/AnalysisThreads/blob/master/DataSelection/5.UsingLATAllSkyWeekly/LAT_weekly_allsky.ipynb). For queries encompassing the whole sky (or close to it) you should use these files. You should also use them if you are doing repeated queries for the same sources.




| LAT Data Compilations |
| --- |
| [Weekly Photon Files](http://heasarc.gsfc.nasa.gov/FTP/fermi/data/lat/weekly/photon/) | All-sky photon data broken into week-long increments. |
| [Weekly Spacecraft Files](http://heasarc.gsfc.nasa.gov/FTP/fermi/data/lat/weekly/spacecraft/) | Spacecraft pointing and history information in 30-second increments, useful for most analyses. |
| [Mission Long Spacecraft File](http://heasarc.gsfc.nasa.gov/FTP/fermi/data/lat/mission/spacecraft/) | Single file containing all 30-second spacecraft information for the entire mission |
| [Weekly 1-second Spacecraft Files](http://heasarc.gsfc.nasa.gov/FTP/fermi/data/lat/weekly/1s_spacecraft/) | Weekly spacecraft information in 1-second increments for high-precision timing analyses. |
| [Filtered Weekly Photon Files](http://heasarc.gsfc.nasa.gov/FTP/fermi/data/lat/weekly/diffuse/) | Weekly photon files with pre-computed diffuse columns. See the [README](https://heasarc.gsfc.nasa.gov/FTP/fermi/data/lat/weekly/diffuse/README) file before using. |
| [Fermi LAT Weekly Data Catalog](https://heasarc.gsfc.nasa.gov/W3Browse/fermi/fermilweek.html) | HEASARC browse interface for accessing weekly photon and 30-second spacecraft files. |
| Previous data processings | Weekly files from previous data processing versions are available: [Pass 8 (P8R2)](http://heasarc.gsfc.nasa.gov/FTP/fermi/data/lat/weekly/p8r2/),<br> [Pass 7 (V6d)](http://heasarc.gsfc.nasa.gov/FTP/fermi/data/lat/weekly/p7v6d/),<br> [Pass 7 (V6)](http://heasarc.gsfc.nasa.gov/FTP/fermi/data/lat/weekly/p7v6/),<br> [Pass 6 (V11)](http://heasarc.gsfc.nasa.gov/FTP/fermi/data/lat/weekly/p6v11/), and<br> [Pass 6 (V3)](http://heasarc.gsfc.nasa.gov/FTP/fermi/data/lat/weekly/p6v3/). |




The links above allow you to download the file through a web browser. There are other method for retreiving the files that may be preferable.


  - [Download weekly files using wget](https://fermi.gsfc.nasa.gov/ssc/help/faq.html#weekly)
  - [Download weekly files from AWS cloud](https://fermi.gsfc.nasa.gov/ssc/help/faq.html#aws)
  - [Download weekly files from the SSDC archive mirror](https://tools.ssdc.asi.it/fermi/weekly.jsp)

## Accessing GBM Daily Data

The GBM is composed of 14 non-imaging detectors placed around the Fermi spacecraft with different orientations. The primary survey data produced by GBM are gamma-ray events, which are provided in pre-binned daily chunks or (since late 2012) unbinned in hourly chunks, of the unocculted sky. See [GBM data products](https://fermi.gsfc.nasa.gov/ssc/data/access/data_products.html#gbm_daily) for a description of the file types. GBM daily data can be analyzed using software like the [Gamma-ray Data Tools](https://fermi.gsfc.nasa.gov/ssc/data/analysis/gbm/) and obtained in several ways:

  - The HEASARC's searchable [Fermi GBM Daily Data catalog](http://heasarc.gsfc.nasa.gov/W3Browse/fermi/fermigdays.html)
  - Direct download from the [GBM data archive](http://heasarc.gsfc.nasa.gov/FTP/fermi/data/gbm/daily/)
  - [Download GBM files using wget](https://fermi.gsfc.nasa.gov/ssc/help/faq.html#gbm_data)

- #### Transient and Time Domain Data






Since Fermi is continuously scanning the sky, Fermi data naturally lends itself to transient and time domain astronomy. There are several kinds of data products that are available.








| Transients |
| --- |
| [GBM Trigger Catalog](http://heasarc.gsfc.nasa.gov/W3Browse/fermi/fermigtrig.html) | Searchable catalog of all GBM triggers (e.g., GRBs, solar flares, SGRs). Data can also be directly from the [HEASARC archive](https://heasarc.gsfc.nasa.gov/FTP/fermi/data/gbm/triggers/) or [using wget](https://fermi.gsfc.nasa.gov/ssc/help/faq.html#gbm_data). |
| [GBM Burst Catalog](http://heasarc.gsfc.nasa.gov/W3Browse/fermi/fermigbrst.html) | Searchable caalog of gamma-ray bursts (GRBs) with extra information characterizing the burst compared to the Trigger Catalog. Data can also be directly from the [HEASARC archive](https://heasarc.gsfc.nasa.gov/FTP/fermi/data/gbm/bursts/) or [using wget](https://fermi.gsfc.nasa.gov/ssc/help/faq.html#gbm_data). |
| [LAT Low-Energy (LLE) Data](https://heasarc.gsfc.nasa.gov/W3Browse/fermi/fermille.html) | Provides LAT low-energy data for certain GBM GRBs (updated periodically) |
| [Fermi All-sky Variability Analysis Catalog](https://fermi.gsfc.nasa.gov/ssc/data/access/lat/FAVA/) (FAVA) | Catalog searching for flaring sources in LAT data across the sky |
| [Aperture Photometry for Flaring Sources](https://fermi.gsfc.nasa.gov/ssc/data/access/lat/10yr_catalog/ap_lcs_flares.html) | Weekly updated list of flaring sources identified by aperture photometry LAT light curve data |




| Source Monitoring |
| --- |
| [Fermi LAT Light Curve Repository](https://fermi.gsfc.nasa.gov/ssc/data/access/lat/LightCurveRepository/#) (LCR) | Database of multi-cadence flux calibrated light curves for LAT-detected sources |
| [LAT Monitored Source List Light Curves](https://fermi.gsfc.nasa.gov/ssc/data/access/lat/msl_lc/) | Daily updated flux values for bright sources and transient sources that have shown flares during the mission |
| [Aperture Photometry Light Curves](https://fermi.gsfc.nasa.gov/ssc/data/access/lat/10yr_catalog/ap_lcs.php) | Weekly updated aperture photometry light curves for sources in the 4FGL-DR2 catalog |
| [GBM Earth Occultation Light Curves](https://gammaray.nsstc.nasa.gov/gbm/science/earth_occ.html) | Light curves for bright X-ray and gamma-ray sources derived from Earth occultation measurements |




See [Time-Domain Resources](https://fermi.gsfc.nasa.gov/ssc/time-domain.html) for more related catalogs and resources.



- #### General Source Catalogs






The LAT Source Catalog is a comprehensive collection of gamma-ray sources detected by the Fermi Large Area Telescope across the entire sky. It represents one of the most important data products from the Fermi mission, cataloging thousands of gamma-ray emitting objects including pulsars, active galactic nuclei, supernova remnants, and other high-energy sources. The catalog has evolved through multiple releases as the mission has accumulated more data.




| LAT Source Catalog |
| --- |
| [LAT 16-year Source List](https://fermi.gsfc.nasa.gov/ssc/data/access/lat/fl16y/) | Early version of the upcoming 5FGL catalog of LAT sources, based on 16 years of survey data (FL16Y). |
| [LAT 14-year Source Catalog](https://fermi.gsfc.nasa.gov/ssc/data/access/lat/14yr_catalog/) | Fourth catalog data release covering 14 years of LAT observations (4FGL-DR4) |
| [LAT 12-year Source Catalog](https://fermi.gsfc.nasa.gov/ssc/data/access/lat/12yr_catalog/) | Fourth catalog data release covering 12 years of LAT observations (4FGL-DR3) |
| [LAT 10-year Source Catalog](https://fermi.gsfc.nasa.gov/ssc/data/access/lat/10yr_catalog/) | Fourth catalog data release covering 10 years of LAT observations (4FGL-DR2) |
| [LAT 8-year Source Catalog](https://fermi.gsfc.nasa.gov/ssc/data/access/lat/8yr_catalog/) | Fourth catalog of LAT-detected gamma-ray sources covering 8 years of observations (4FGL) |
| [Preliminary LAT 8-year Source List](https://fermi.gsfc.nasa.gov/ssc/data/access/lat/fl8y/) | Preliminary list of LAT sources from 8 years of survey data (FL8Y) |
| [LAT 4-year Source Catalog](https://fermi.gsfc.nasa.gov/ssc/data/access/lat/4yr_catalog/) | Third catalog of LAT-detected gamma-ray sources covering 4 years of observations (3FGL) |
| [LAT 2-year Source Catalog](https://fermi.gsfc.nasa.gov/ssc/data/access/lat/2yr_catalog/) | Second catalog of LAT-detected gamma-ray sources covering 2 years of observations (2FGL) |
| [LAT 1-year Source Catalog](https://fermi.gsfc.nasa.gov/ssc/data/access/lat/1yr_catalog/) | First catalog of LAT-detected gamma-ray sources covering 1 year of observations (1FGL) |
| [LAT 3-month Bright Source List](http://heasarc.gsfc.nasa.gov/db-perl/W3Browse/w3table.pl?tablehead=name%3Dfermilbsl&Action=More+Options) | Initial bright source list from the first 3 months of LAT observations (0FGL) |




The LAT High Energy Source Catalog is a specialized series of catalogs that focuses specifically on sources detected at the highest gamma-ray energies accessible to the Large Area Telescope. While the standard LAT source catalogs cover energies from approximately 100 MeV upward, the high energy catalogs concentrate on sources detected above 10 GeV or 50 GeV, where the LAT has superior angular resolution and reduced contamination from diffuse emission.






| LAT High Energy Source Catalog |
| --- |
| [LAT Third High Energy Source Catalog](https://fermi.gsfc.nasa.gov/ssc/data/access/lat/3FHL/) | Third catalog of LAT sources detected above 10 GeV (3FHL) |
| [LAT Second High-Energy Source Catalog](https://fermi.gsfc.nasa.gov/ssc/data/access/lat/2FHL/) | Second catalog of LAT sources detected above 50 GeV (2FHL) |
| [LAT First High-Energy Source Catalog](https://fermi.gsfc.nasa.gov/ssc/data/access/lat/1FHL/) | First catalog of LAT sources detected above 10 GeV (1FHL) |

- #### Source Specific Catalogs and Data







| Active Galactic Nuclei (AGN) |
| --- |
| [Fourth LAT AGN Catalog](https://fermi.gsfc.nasa.gov/ssc/data/access/lat/4LACDR3/) | Active galactic nuclei detected by the LAT, including data releases 4LAC, 4LAC-DR2, and 4LAC-DR3 |




| Gamma-Ray Bursts |
| --- |
| [GBM Burst Catalog](http://heasarc.gsfc.nasa.gov/W3Browse/fermi/fermigbrst.html) | Gamma-ray bursts detected by the Gamma-ray Burst Monitor. Data can also be directly from the [HEASARC archive](https://heasarc.gsfc.nasa.gov/FTP/fermi/data/gbm/bursts/) or [using wget](https://fermi.gsfc.nasa.gov/ssc/help/faq.html#gbm_data). |
| [LAT Burst Catalog](http://heasarc.gsfc.nasa.gov/W3Browse/fermi/fermilgrb.html) | Gamma-ray bursts detected by the Large Area Telescope |
| [LAT Low-Energy (LLE) Catalog](https://heasarc.gsfc.nasa.gov/W3Browse/fermi/fermille.html) | LAT low-energy events for enhanced GRB temporal and spectral analysis |
| [Trigger notices for Fermi GRBs from GCN](https://gcn.gsfc.nasa.gov/gcn/fermi_grbs.html) | Real-time alerts and trigger information distributed through the Gamma-ray Coordinates Network |
| [Untriggered GBM Short GRB Candidates](https://gcn.gsfc.nasa.gov/fermi_gbm_subthresh_archive.html) | Archive of subthreshold gamma-ray burst candidates identified in GBM data that did not trigger onboard detection |
| [Preliminary GRB HEALPix Localizations](https://zenodo.org/record/6727152) | Sky localization maps in HEALPix format for rapid follow-up observations |




| Pulsars |
| --- |
| [LAT Third Catalog of Gamma-ray Pulsars](https://fermi.gsfc.nasa.gov/ssc/data/access/lat/3rd_PSR_catalog/) | Third catalog of gamma-ray pulsars detected by the LAT (3PC) |
| [LAT Second Catalog of Gamma-ray Pulsars](https://fermi.gsfc.nasa.gov/ssc/data/access/lat/2nd_PSR_catalog/) | Second catalog of gamma-ray pulsars detected by the LAT (2PC) |
| [LAT List of Detected Gamma-Ray Pulsars](https://confluence.slac.stanford.edu/display/GLAMCOG/Public+List+of+LAT-Detected+Gamma-Ray+Pulsars) | Frequently updated list of all gamma-ray pulsars detected by the LAT |
| [LAT Pulsar Ephemerides from Publications](https://fermi.gsfc.nasa.gov/ssc/data/access/lat/ephems/) | Timing ephemerides for LAT-detected pulsars from published papers |
| [GBM Pulsar Spin Histories](http://gammaray.nsstc.nasa.gov/gbm/science/pulsars.html) | Historical spin frequency measurements for pulsars monitored by GBM |




| Solar Flares |
| --- |
| [GBM Solar Flare Catalog](https://heasarc.gsfc.nasa.gov/w3browse/all/fermigsol.html) | Catalog of GBM-detected solar flares. |
| [Fermi Solar Flare Observations](http://hesperia.gsfc.nasa.gov/fermi_solar/) | Database and analysis tools for solar flares observed by Fermi instruments |
| [The First Fermi-LAT Solar Flare Catalog](https://fermi.gsfc.nasa.gov/ssc/data/access/lat/FLSF/) | First catalog of solar flares detected by the LAT (FLSF) |




| Supernovae |
| --- |
| [1st Fermi-LAT SNR Catalog](https://fermi.gsfc.nasa.gov/ssc/data/access/lat/1st_SNR_catalog/) | First catalog of supernova remnants detected in gamma rays by the LAT |




| Terrestrial Gamma-ray Flashes (TGF) |
| --- |
| [GBM Terrestrial Gamma-ray Flashes (TGF) Catalog](https://fermi.gsfc.nasa.gov/ssc/data/access/gbm/tgf) | Catalog of terrestrial gamma-ray flashes associated with thunderstorms detected by GBM |
