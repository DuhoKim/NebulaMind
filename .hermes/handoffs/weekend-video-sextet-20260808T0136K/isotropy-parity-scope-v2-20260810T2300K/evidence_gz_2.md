URL: https://zenodo.org/records/4573248/files/schema.md

\# Galaxy Zoo DECaLS Schema

This schema describes the columns in the GZ DECaLS catalogues; \`gz\_decals\_auto\_posteriors\`, \`gz\_decals\_volunteers\_1\_and\_2\`, and \`gz\_decals\_volunteers\_5\`.

In all catalogues, galaxies are identified by their \`iauname\`. Galaxies are unique within a catalogue. \`gz\_decals\_auto\_posteriors\` contains all galaxies with appropriate imaging and photometry in DECaLS DR5, while \`gz\_decals\_volunteers\_1\_and\_2\`, and \`gz\_decals\_volunteers\_5\` contain subsets classified by volunteers in the respective campaigns.

The columns reporting morphology measurements are named like \`{some-question}\_{an-answer}\`. For example, for the first question, both volunteer catalogues include the following:

\| Column \| Description \|
\| \-\-\-\-\-\-\-\-\-\-\- \| \-\-\-\-\-\-\-\-\-\-\- \|
\| smooth-or-featured\_total \| Total number of volunteers who answered the "Smooth of Featured" question \|
\| smooth-or-featured\_smooth \| Count of volunteers who responded "Smooth" to the "Smooth or Featured" question \|
\| smooth-or-featured\_featured-or-disk \| Count of volunteers who responded "Featured or Disk", similarly \|
\| smooth-or-featured\_artifact \| Count of volunteers who responded "Artifact", similarly \|
\| smooth-or-featured\_smooth\_fraction \| Fraction of volunteers who responded "Smooth" to the "Smooth or Featured" question, out of all respondes (i.e. smooth count / total) \|
\| smooth-or-featured\_featured-or-disk\_fraction \| Fraction of volunteers who responded "Featured or Disk", similarly \|
\| smooth-or-featured\_artifact\_fraction \| Fraction of volunteers who responded "Artifact", similarly \|

The questions and answers are slightly different for \`gz\_decals\_volunteers\_1\_and\_2\` than \`gz\_decals\_volunteers\_5\`. See the paper for more.

The volunteer catalogues include \`{question}\_{answer}\_debiased\` columns which attempt to estimate what the vote fractions would be if the same galaxy were imaged at lower redshift. See the paper for more. Note that the debiased measurements are highly uncertain on an individual galaxy basis and therefore should be used with caution. Debiased estimates are only available for galaxies with 0.02M\_r>-23, and at least 30 votes for the first question (\`Smooth or Featured') after volunteer weighting.

The automated catalogue, \`gz\_decals\_auto\_posteriors\`, includes predictions for all galaxies and all questions even when that question may not be appropriate (e.g. number of spiral arms for a smooth elliptical). To assess relevance, we include \`{question}\_proportion\_volunteers\_asked\` columns showing the estimated fraction of volunteers that would have been asked each question (i.e. the product of the vote fractions for the preceding answers). We suggest a cut of \`{question}\_proportion\_volunteers\_asked\` > 0.5 as a starting point.

The automated catalogue does not include volunteer counts or totals (naturally).

Each catalogue includes a pair of columns to warn where galaxies may have been classified using an inappropriately large field-of-view (due to incorrect radii measurements in the NSA, on which the field-of-view is calculated). We suggest excluding galaxies (<1%) with such warnings.

\| Column \| Description \|
\| \-\-\-\-\-\-\-\-\-\-\- \| \-\-\-\-\-\-\-\-\-\-\- \|
\| wrong\_size\_statistic \| Mean distance from center of all pixels above double the 20th percentile (i.e. probable source pixels) \|
\| wrong\_size\_warning \| True if wrong\_size\_statistic > 161.0, our suggested starting cut. Approximately the mean distance of all pixels from center\|

For convenience, each catalogue includes the same set of basic astrophysical measurements copied from the NASA Sloan Atlas (NSA). Additional measurements can be added my crossmatching on \`iauname\` with the NSA. See \[here\](https://data.sdss.org/datamodel/files/ATLAS\_DATA/ATLAS\_MAJOR\_VERSION/nsa.html) for the NSA schema. If you use these columns, you should cite the NSA.

\| Column \| Description \|
\| \-\-\-\-\-\-\-\-\-\-\- \| \-\-\-\-\-\-\-\-\-\-\- \|
\| ra \| Right ascension (degrees) \|
\| dec \| Declination (degrees) \|
\| iauname \| Unique identifier listed in NSA v1.0.1 \|
\| petro\_theta \| "Azimuthally-averaged SDSS-style Petrosian radius (derived from r band" \|
\| petro\_th50 \| "Azimuthally-averaged SDSS-style 50% light radius (r-band)" \|
\| petro\_th90 \| "Azimuthally-averaged SDSS-style 50% light radius (r-band)" \|
\| elpetro\_absmag\_r \| "Absolute magnitude from elliptical Petrosian fluxes in rest-frame" in SDSS r \|
\| sersic\_nmgy\_r \| "Galactic-extinction corrected AB flux" in SDSS r \|
\| redshift \| "Heliocentric redshift" ("z" column in NSA) \|
\| mag\_r \| 22.5 - 2.5 log10(sersic\_nmgy\_r). \*Not\* the same as the NSA mag column! \|

If you have any questions or find any issues, feel free to reach out.
