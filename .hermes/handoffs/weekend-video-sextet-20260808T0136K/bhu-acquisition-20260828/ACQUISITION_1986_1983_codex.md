# Open-route acquisition report: 1986 / 1983 pair

Run date: 2026-09-03. Network retrieval was performed with `curl` only. HTTP status below is the final status after redirects. No login, purchase, paywall bypass, CAPTCHA solving, or account creation was attempted.

## M. Gasperini, “Spin-dominated inflation in the Einstein-Cartan theory,” Phys. Rev. Lett. 56, 2873 (1986)

STATUS=NOT_FOUND

No free copy of the target paper was obtained. Consequently no target PDF/text file was written, no target hashes were generated, and no closure line can be quoted from an acquired primary text.

URLs tried, in route order:

1. ADS
   - `https://ui.adsabs.harvard.edu/abs/1986PhRvL..56.2873G/abstract` — HTTP 405 (ADS AWS-WAF challenge page).
   - `https://ui.adsabs.harvard.edu/link_gateway/1986PhRvL..56.2873G/ESOURCE` — HTTP 403 after redirect to `https://link.aps.org/doi/10.1103/PhysRevLett.56.2873` (Cloudflare challenge; exact requirement shown: “Enable JavaScript and cookies to continue”).
2. INSPIRE
   - `https://inspirehep.net/api/literature?q=doi%3A10.1103%2FPhysRevLett.56.2873&size=10` — HTTP 200. Record 234371 has no `documents`, `arxiv_eprints`, `report_numbers`, or `urls` field.
3. KEK preprint scan server
   - `https://duckduckgo.com/html/?q=site%3Alib-extopc.kek.jp%2Fpreprints+%22Spin-dominated+inflation%22` — HTTP 200 (bot/anomaly page; no result exposed).
   - `https://www.google.com/search?q=site%3Alib-extopc.kek.jp%2Fpreprints+%22Spin-dominated+inflation%22` — HTTP 200 (no KEK target URL exposed).
   - `https://www.bing.com/search?format=rss&q=site%3Alib-extopc.kek.jp%2Fpreprints+%22Spin-dominated+inflation%22` — HTTP 200 (no relevant KEK result).
   - `https://lib-extopc.kek.jp/preprints/` — HTTP 200 (server root only; INSPIRE supplies no report number from which to construct a scan URL).
4. Author institutional page
   - `https://duckduckgo.com/html/?q=M.+Gasperini+%22Spin-dominated+inflation%22+pdf` — HTTP 202 (bot/anomaly page; no result exposed).
   - `https://www.google.com/search?q=M.+Gasperini+%22Spin-dominated+inflation%22+PDF` — HTTP 200 (no target PDF exposed).
   - `https://www.bing.com/search?format=rss&q=M.+Gasperini+%22Spin-dominated+inflation%22+PDF` — HTTP 200 (no relevant result).
   - `https://www.ba.infn.it/~gasperin/` — HTTP 200 after redirect to `https://home.ba.infn.it/~gasperin/`; the page has later papers but not the target.
   - `https://www.ba.infn.it/~gasperin/publications.html` — HTTP 404 after redirect to `https://home.ba.infn.it/~gasperin/publications.html`.
   - `https://home.ba.infn.it/~gasperin/academic.html` — HTTP 200.
   - `https://home.ba.infn.it/~gasperin/Pubblicazioni_Maurizio_Gasperini.pdf` — HTTP 200; this is only a publication-list PDF. It lists the target as item 63 but does not provide its full text.

Publisher endpoint and displayed access condition:

- `https://journals.aps.org/prl/abstract/10.1103/PhysRevLett.56.2873` — HTTP 403; Cloudflare challenge, exact requirement shown: “Enable JavaScript and cookies to continue.”
- `https://journals.aps.org/prl/pdf/10.1103/PhysRevLett.56.2873` — HTTP 403; same exact requirement.
- No price or publisher registration requirement was displayed in the returned pages, so PAYWALLED cannot be pinned from this `curl`-only run.

## I. S. Nurgaliev and W. N. Ponomariev, “The earliest evolutionary stages of the universe and space-time torsion,” Phys. Lett. B 130, 378 (1983)

STATUS=NOT_FOUND

No free copy of the target paper was obtained. Consequently no target PDF/text file was written, no target hashes were generated, and no closure line can be quoted from an acquired primary text.

URLs tried, in route order:

1. ADS
   - `https://ui.adsabs.harvard.edu/abs/1983PhLB..130..378N/abstract` — HTTP 405 (ADS AWS-WAF challenge page).
   - `https://ui.adsabs.harvard.edu/link_gateway/1983PhLB..130..378N/ESOURCE` — HTTP 200 after redirect to `https://linkinghub.elsevier.com/retrieve/pii/0370269383915265`; it exposes a redirect toward the ScienceDirect article page, not a free scan/PDF.
2. INSPIRE
   - `https://inspirehep.net/api/literature?q=doi%3A10.1016%2F0370-2693%2883%2991526-5&size=10` — HTTP 200. Record 197011 has no `documents`, `arxiv_eprints`, `report_numbers`, or `urls` field.
   - `https://inspirehep.net/api/authors/2498700` — HTTP 200; the Nurgalev author record has no positions, institutional URLs, or email address.
   - `https://inspirehep.net/api/authors/2498702` — HTTP 200; the Ponomarev author record has no positions, institutional URLs, or email address.
3. KEK preprint scan server
   - `https://duckduckgo.com/html/?q=site%3Alib-extopc.kek.jp%2Fpreprints+%22earliest+evolutionary+stages%22` — HTTP 202 (bot/anomaly page; no result exposed).
   - `https://www.google.com/search?q=site%3Alib-extopc.kek.jp%2Fpreprints+%22earliest+evolutionary+stages%22` — HTTP 200 (no KEK target URL exposed).
   - `https://www.bing.com/search?format=rss&q=site%3Alib-extopc.kek.jp%2Fpreprints+%22earliest+evolutionary+stages%22` — HTTP 200 (no relevant KEK result).
   - `https://lib-extopc.kek.jp/preprints/` — HTTP 200 (server root only; INSPIRE supplies no report number from which to construct a scan URL).
4. Author institutional page
   - `https://duckduckgo.com/html/?q=I.+S.+Nurgaliev+W.+N.+Ponomariev+%22space-time+torsion%22+pdf` — HTTP 202 (bot/anomaly page; no result exposed).
   - `https://www.google.com/search?q=Nurgaliev+Ponomariev+%22space-time+torsion%22+PDF` — HTTP 200 (no institutional page or target PDF exposed).
   - `https://www.bing.com/search?format=rss&q=Nurgaliev+Ponomariev+%22space-time+torsion%22+PDF` — HTTP 200 (no relevant result).
   - No author institutional URL was exposed by those searches or by either INSPIRE author record.

Publisher endpoint and displayed access condition:

- `https://www.sciencedirect.com/science/article/pii/0370269383915265` — HTTP 403. The returned page displayed “Remote access,” linked to `https://www.sciencedirect.com/user/institution/login?targetURL=%2F`; this is the exact registration/access requirement shown. It displayed no exact article price.
- `https://www.sciencedirect.com/science/article/pii/0370269383915265/pdfft` — HTTP 403 with the same “Remote access” institutional-login link and no exact price.
- Because the response did not expose the article or an explicit per-article purchase offer, this run records NOT_FOUND rather than asserting PAYWALLED.
