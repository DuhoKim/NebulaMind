# Nurgaliev & Ponomariev 1983 — legitimate open-route retry

Run time: 2026-09-04 01:04 KST

STATUS=NOT_FOUND_CLOSED_ACCESS

Target identity: I. S. Nurgaliev and W. N. Ponomariev, “The earliest evolutionary stages of the universe and space-time torsion,” *Physics Letters B* 130 (1983) 378–379, DOI `10.1016/0370-2693(83)91526-5`, PII `0370269383915265`, ADS bibcode `1983PhLB..130..378N`, INSPIRE record `197011`.

No login, institutional proxy, credential, purchase, CAPTCHA bypass, cookie replay, generic proxy, or paywall/archive bypass was used. No target PDF or extracted text was created.

## Publisher and DOI routes

- Crossref DOI record: `https://api.crossref.org/works/10.1016%2F0370-2693(83)91526-5`
  - Confirms the composite identity and exposes two Elsevier version-of-record text-mining URLs.
- Crossref-linked Elsevier XML: `https://api.elsevier.com/content/article/PII:0370269383915265?httpAccept=text/xml`
  - HTTP 200, XML, 1,814 bytes; title and metadata only. There is no full-text `<body>` or `<originalText>` payload.
- DOI-shaped Elsevier XML: `https://api.elsevier.com/content/article/doi/10.1016%2F0370-2693%2883%2991526-5?httpAccept=text/xml`
  - Same HTTP 200 metadata-only XML, byte-identical to the PII response.
- Crossref-linked Elsevier plain text: `https://api.elsevier.com/content/article/PII:0370269383915265?httpAccept=text/plain`
  - HTTP 400, XML error body, 159 bytes.
- Explicit full-view request: `https://api.elsevier.com/content/article/PII:0370269383915265?view=FULL&httpAccept=text/xml`
  - HTTP 401, XML error body, 133 bytes. No credential was supplied or sought.
- PDF media request: `https://api.elsevier.com/content/article/PII:0370269383915265?httpAccept=application/pdf`
  - HTTP 406, XML error body, 162 bytes; not a PDF.
- Publisher article page: `https://www.sciencedirect.com/science/article/pii/0370269383915265`
  - Identifies the exact two-page article and offers organizational access or “Purchase PDF”; it exposes no anonymous open full text.
- Search-indexed publisher PDF URL: `https://www.sciencedirect.com/science/article/pii/0370269383915265/pdf?md5=430f9bd127fac4c387c69e30406778d1&pid=1-s2.0-0370269383915265-main.pdf`
  - HTTP 403, HTML, 832,805 bytes; not PDF magic.
- Publisher `pdfft` route: `https://www.sciencedirect.com/science/article/pii/0370269383915265/pdfft?isDTMRedir=true&download=true`
  - HTTP 403, HTML, 832,805 bytes; not PDF magic.

The APS-style Crossref route therefore does not reproduce the Gasperini result: Crossref does expose a publisher endpoint, but its anonymous response stops at metadata.

## Repository and scan routes

- OpenAlex: `https://api.openalex.org/works/https://doi.org/10.1016/0370-2693(83)91526-5`
  - Record `W2062476953`: `is_oa=false`, `oa_status=closed`, `oa_url=null`, `any_repository_has_fulltext=false`, `has_fulltext=false`, no PDF URL.
- INSPIRE API: `https://inspirehep.net/api/literature/197011`
  - Confirms DOI, authors, journal, pages, ADS bibcode and SPIRES identifier. It supplies no `documents`, arXiv eprint, report number, or full-text URL.
- INSPIRE public record: `https://inspirehep.net/literature/197011`
  - Metadata and outbound DOI/ADS links only; no document link.
- ADS direct scan route: `https://articles.adsabs.harvard.edu/pdf/1983PhLB..130..378N`
  - The dedicated retry ended HTTP 504 after 60 seconds with a 183-byte HTML gateway-timeout body, not a PDF. A second extractor independently timed out.
- ADS legacy article query: `https://articles.adsabs.harvard.edu/cgi-bin/nph-iarticle_query?1983PhLB..130..378N&defaultprint=YES&filetype=.pdf`
  - HTTP 404 HTML, not a PDF.
- ADS publisher gateway: `https://ui.adsabs.harvard.edu/link_gateway/1983PhLB..130..378N/PUB_PDF`
  - HTTP 404 HTML, not a PDF. The ADS abstract surface separately presents a human-verification gate; it was not bypassed.
- OpenAIRE: `https://api.openaire.eu/search/publications?doi=10.1016%2F0370-2693%2883%2991526-5&format=json`
  - Exact metadata record but no usable full-text location or PDF URL.
- KEK's listed public preprint catalogue: `https://www.i-repository.net/il/meta_pub/engG0000128Lib`
  - Currently resolves to an InfoLib login page. INSPIRE supplies no report number from which to identify a KEK preprint/scan. No login was attempted.
- CERN/KEK/ADS/INSPIRE exact-title and identifier searches exposed no independent open scan.

## Author and institutional routes

- Public author profile: `https://independent.academia.edu/IldusNurgaliev`
  - Lists the exact target title and abstract metadata, but unlike adjacent uploaded papers it exposes no target paper page or “Download free PDF” link.
- Public author profile: `https://www.researchgate.net/profile/Ildus-Nurgaliev`
  - Targeted exact-title searches and the public profile exposed no matching downloadable target copy; no request-full-text, login, or contact action was taken.
- Targeted searches of Moscow State University/institutional pages exposed no target PDF or author-hosted copy.

## Receipts and boundary

Machine-readable anonymous-route probe: `_tmp_nurgaliev_open_route_probe_20260904.json`, SHA-256 `f092d842c399c7b711083e502245dcbe1e0117fcbb6c12d1e38f833c439a9c59`.

ADS timeout body: `_tmp_nurgaliev_ads_scan.bin`, SHA-256 `13381468e39367834728e60bef4b0f65fe5a4e483a2833e12af5f56f5bd891e6`; headers: `_tmp_nurgaliev_ads_scan.headers`, SHA-256 `caac59247c083a69704b678e344a2f995910004f854cad6a4abdc8013cc40980`.

This source remains unread and non-blocking. A citation marker in Gasperini 1986 is not evidence that Nurgaliev & Ponomariev derive the `1/8` coefficient. Do not buy. This acquisition result changes no K3 verdict, tier, warrant token, standing, stamp, or study state.

NURGALIEV_OPEN_ROUTE_RETRY_COMPLETE
