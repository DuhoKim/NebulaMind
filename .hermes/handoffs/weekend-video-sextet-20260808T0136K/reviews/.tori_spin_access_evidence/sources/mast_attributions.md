SOURCE URL: https://archive.stsci.edu/publishing/data-attributions
TITLE: DATA ATTRIBUTIONS | MAST
ACCESSED: 2026-08-12 KST

# DATA ATTRIBUTIONS

## Attribution Requirements

It is expected that the results of observations from active missions, and from Archival Research programs using data hosted by MAST, will be published in the scientific literature. All refereed publications based on data from these programs should include the following types of attributions:

- Acknowledge the observing facility or mission where the data were obtained
  - List the observing programs
  - Cite the specific datasets using a DOI
- Acknowledge the funding source, explicitly saying "US investigators are funded for this work via grant/proposal <#>"
- Specify the facilities used

(See also, the [Astronomy Acknowledgement Generator](http://astrofrog.github.io/acknowledgment-generator/).)

## Data Source

The source of the data should be acknowledged in all publications, with one or more of the acknowledgements given on the [Mission Acknowledgements](https://archive.stsci.edu/publishing/mission-acknowledgements "Mission Acknowledgementss") page, as appropriate.

### Identify the Data Collection

Authors should also include a digital object identifier (DOI) in all papers that use MAST data. MAST provides a [service to generate a DOI](https://archive.stsci.edu/doi/search/) if needed; it should point to the specific data analyzed in the paper. We suggest that authors cite the DOI near the end of a section entitled, e.g., "Data" or "Observations." For example, the AASTeX markup for a citation to the HLSP collection called _HTTP_ would be:

#### **DOI citation using the AASTeX \\dataset macro**

```
The data described here may be obtained from the MAST archive at
\dataset[doi:10.17909/T9RP4V]{https://dx.doi.org/10.17909/T9RP4V}.
```

When publishing in journals that do not provide the `\dataset` macro, a simple `\url` macro will do:

#### DOI citation using the \\url macro

```
The data described here may be obtained from
\url{https://dx.doi.org/10.17909/T9RP4V}.
```

## Funding

If the research described in the publication was supported by a grant from STScI, the following acknowledgment must be included:

_Support for US investigators in program <**programID>** was provided by NASA through a grant from the Space Telescope Science Institute, which is operated by the Association of Universities for Research in Astronomy, Inc., under NASA contract NAS 5–26555._

where **_<_** _**programID>**_ is the observing program number assigned by the mission.

## Facility Keywords

Include the appropriate [facility keywords](https://journals.aas.org/facility-keywords/) when preparing manuscripts for an AAS journal. The following is an example for a paper where _HST_/WFC3 data were used in conjunction with a MAST high-level science product (HLSP) collection, and data from the Pan-STARRS survey:

```
\facilities{HST (WFC3), MAST (HLSP, Pan-STARRS)}
```

[back to top](https://archive.stsci.edu/publishing/data-attributions#body)

reCAPTCHA

Recaptcha requires verification.

protected by **reCAPTCHA**
