# URL: https://zoobot.readthedocs.io/en/latest/science_data.html

ContentsMenuExpandLight modeDark modeAuto light/dark mode

[Back to top](https://zoobot.readthedocs.io/en/latest/science_data.html#)

Toggle Light / Dark / Auto color theme

Toggle table of contents sidebar

# Science Data [\#](https://zoobot.readthedocs.io/en/latest/science_data.html\#science-data "Permalink to this heading")

The goal of Zoobot is to do science. Here are some science-ready datasets created with Zoobot.

## Precalulated Representations [\#](https://zoobot.readthedocs.io/en/latest/science_data.html\#precalulated-representations "Permalink to this heading")

Warning

New for Zoobot v2! We’re really excited to see what you build. Reach out for help.

Zoobot v2 now includes precalculated representations for galaxies in the Galaxy Zoo DESI data release.
Download [here](https://www.dropbox.com/scl/fi/ml33hzv4ak1lwffm0fucn/representations_pca_40_with_coords.parquet?rlkey=xu3dwfjc5ando7lkbgk89slpb&dl=0) (2.5GB)

You could use these to power a similarity search, anomaly recommendation system, the vision part of a multi-modal model,
or really anything else that needs a short vector summarizing the morphology in a galaxy image.

| id\_str | ra | dec | feat\_pca\_0 | feat\_pca\_1 | … |
| --- | --- | --- | --- | --- | --- |
| 303240\_2499 | 4.021870 | 3.512972 | 0.257407 | -7.414328 | … |

`id_str` is the unique identifier for the galaxy in the DESI Legacy Surveys DR8 release and can be crossmatched with the GZ DESI catalog (below) `dr8_id` key.
It is formed with `{brickid}_{objid}` where brickid is the unique identifier for the brick in the Legacy Surveys and objid is the unique identifier for the object in the brick.
`RA` and `Dec` are in degrees.
The PCA features are the first 40 principal components representation (which is otherwse impractically large to work with).

## Galaxy Zoo Morphology [\#](https://zoobot.readthedocs.io/en/latest/science_data.html\#galaxy-zoo-morphology "Permalink to this heading")

Zoobot was used to create a detailed morphology catalog for every (extended, brighter than r=19) galaxy in the DESI Legacy Surveys (8.7M galaxies).
The catalog and schema are available from [Zenodo](https://zenodo.org/records/8360385).
For new users, we suggest starting with the `gz_desi_deep_learning_catalog_friendly.parquet` catalog file.

We previously used Zoobot to create a similar catalog for [DECaLS DR5](https://zenodo.org/records/4573248).
This has now been superceded by the GZ DESI catalog above (which includes the same galaxies, and many more).

We aim to provide both representations and an updated morphology catalog for DESI-LS DR10, but we need to redownload all the images first 😐.

Future catalogs will include morphology measurements for HSC, JWST, and Euclid galaxies (likely in that order).

Versions**[latest](https://zoobot.readthedocs.io/en/latest/science_data.html)**On Read the Docs[Project Home](https://app.readthedocs.org/projects/zoobot/?utm_source=zoobot&utm_content=flyout)[Builds](https://app.readthedocs.org/projects/zoobot/builds/?utm_source=zoobot&utm_content=flyout)Search

* * *

[Addons documentation](https://docs.readthedocs.io/page/addons.html?utm_source=zoobot&utm_content=flyout) ― Hosted by
[Read the Docs](https://about.readthedocs.com/?utm_source=zoobot&utm_content=flyout)