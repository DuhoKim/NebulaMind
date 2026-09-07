# Publisher-text verification — 2026-09-07

Both target **APS version-of-record PDFs were obtained directly from APS and read**. The saved PDF bytes, not a manuscript or mirror, support the transcriptions below. Equations preserve symbols, signs, factors and numbering; LaTeX spacing and line wrapping are normalized. Printed page numbers are distinguished from PDF page indices.

**PRD identity and correction check.** Nikodem Popławski, “Nonsingular, big-bounce cosmology from spinor-torsion coupling,” *Physical Review D* **85**, **107502** (2012), DOI [10.1103/PhysRevD.85.107502](https://doi.org/10.1103/PhysRevD.85.107502). The saved five-page PDF is the published Brief Report, dated 29 May 2012, with pages 107502-1–107502-5; it is not an erratum. APS-deposited Crossref metadata labels its Harvest full-text link “vor”. The PDF hash matches the earlier memory-only receipt R09 in SOURCES_20260907.md.

**No erratum or later correction was found in the records checked; an exhaustive absence is not established.** The [APS article landing page](https://journals.aps.org/prd/abstract/10.1103/PhysRevD.85.107502), read through the web tool, displays no erratum/correction link. The [journal's volume 85, issue 10 ERRATA listing](https://journals.aps.org/prd/issues/85/10) contains 109901 (a Publisher’s Note concerning 083007) and 109902 (an erratum concerning 043524); neither concerns 107502. Exact-title/citation searches for errata and corrections found no matching notice. Crossref has an empty relation object and no update-to or updated-by field. The journal's search-results endpoint and attempted /prd/errata endpoint were inaccessible; the latter's validity as a standalone listing was not established. No complete survey of all later issue listings was obtained. Accordingly, this record does not certify that no later correction exists or that APS has never replaced the PDF.

**PRD tilde convention and requested equations — printed p. 107502-2, PDF page 2.** Immediately before Eq. (10), the publisher prints:

> The averaged second term on the right of (9) acts thus like a perfect fluid with a negative energy density:

\[
\tilde{\epsilon}=-\tilde{p}=-\alpha n^2,\qquad
\alpha=\frac{9}{16}\kappa.
\tag{10}
\]

This is the introducing sentence, not a sentence literally containing the word “tilde”. Together with (10), it assigns the tilded density and pressure to the averaged second term of (9), i.e. the added contribution, rather than the effective totals.

\[
\dot{a}^{2}+k=\frac{1}{3}\kappa(\epsilon-\alpha n^2)a^2,
\tag{11}
\]

\[
\dot{a}^{2}+2a\ddot{a}+k=-\kappa(p+\alpha n^2)a^2,
\tag{12}
\]

**Effective total pressure correction: \(+\alpha n^2\).** The quoted line is Eq. (12) itself, specifically its printed \(-\kappa(p+\alpha n^2)a^2\). The pressure entering that equation is \(p+\alpha n^2\).

Source: [APS full-text PDF](https://harvest.aps.org/v2/journals/articles/10.1103/PhysRevD.85.107502/fulltext); saved [PDF](prd_publisher_verify_20260907/prd_pdf.pdf) and visually checked [page 107502-2](prd_publisher_verify_20260907/prd_page_2.png).

**Formalism anchor.** Friedrich W. Hehl, Paul von der Heyde, G. David Kerlick and James M. Nester, “General relativity with spin and torsion: Foundations and prospects,” *Reviews of Modern Physics* **48**, **393–416** (1976), DOI [10.1103/RevModPhys.48.393](https://doi.org/10.1103/RevModPhys.48.393). The 24-page APS PDF is the published July 1976 article, not an erratum. Crossref labels the Harvest link “vor”. Its hash matches SOURCES_20260907.md receipt R10.

No correction was found on the [APS landing page](https://journals.aps.org/rmp/abstract/10.1103/RevModPhys.48.393), in the [volume 48, issue 3 listing](https://journals.aps.org/rmp/issues/48/3), or by the exact-title/citation erratum searches. That issue's sole listed erratum is the unrelated Particle Data Group item at p. 497. The landing page's See Also link is an Agnese–Calvini article, not a correction. Crossref has no recorded correction relation. Search and attempted /rmp/errata access failed; absence across all later issues remains unverified.

**Combined tensor — printed p. 400, PDF page 8.**

\[
G^{ij}(\{\})=k\tilde{\sigma}^{ij}
\qquad\text{(combined field equation)}
\tag{3.23}
\]

The introducing words are:

> with the combined energy-momentum tensor

\[
\begin{aligned}
\tilde{\sigma}^{ij}:={}&\sigma^{ij}
+k\Bigl[-4\tau^{ik}{}_{[l}\tau^{jl}{}_{k]}
-2\tau^{ikl}\tau^{j}{}_{kl}
+\tau^{kli}\tau_{kl}{}^{j}\\
&\qquad+\frac12g^{ij}
\bigl(4\tau^{k}{}_{m[l}\tau^{ml}{}_{k]}
+\tau^{mkl}\tau_{mkl}\bigr)\Bigr],
\end{aligned}
\tag{3.24}
\]

The [publisher-rendered equation excerpt](prd_publisher_verify_20260907/rmp_eq_3_23_3_24.png) preserves the original index-placement dots.

**Dirac combined tensor — printed p. 408, PDF page 16.**

\[
\tilde{\sigma}_{\alpha\beta}
=\Sigma_{(\alpha\beta)}(\{\})
-\frac12g_{\alpha\beta}k\tau^{\mu\nu\lambda}\tau_{\mu\nu\lambda}.
\tag{5.15}
\]

**Semiclassical spin-fluid combined tensor — printed p. 408, PDF page 16.**

\[
\begin{aligned}
\tilde{\sigma}^{ij}={}&(\rho+P-2ks^2)u^iu^j
+(P-ks^2)g^{ij}\\
&+2(u_mu^k-\delta_m^k)\overset{\{\}}{\nabla}_k
\bigl(\tau^{m(i}u^{j)}\bigr)\\
&+\tau^{(i}\bigl(2\delta_m^{j)}u^k-u^{j)}\delta_m^k\bigr)
\overset{\{\}}{\nabla}_ku^m.
\end{aligned}
\tag{5.18}
\]

The adjacent unnumbered definitions are \(\tau_i:=\tau_{ik}u^k\) and \(s^2:=\tau_{kl}\tau^{kl}\). The printed pressure coefficient in (5.18) is **\(P-ks^2\)**: the explicit quadratic pressure correction is **\(-ks^2\)** in this paper's notation. See [printed p. 408](prd_publisher_verify_20260907/rmp_page_16.png) and the [equation excerpt](prd_publisher_verify_20260907/rmp_eq_5_18.png).

Section V.B.7, pp. 408–409, discusses averaging randomly oriented spins and retaining quadratic spin terms. **No separately printed pair of effective energy density and effective pressure equations specifically labelled for an unpolarised fluid was found.** Equation (5.18) is quoted in full; no reduced pair is supplied here as a purported verbatim quotation. The \(\tilde E\) defined on p. 410 is \((\tilde\sigma_{ij}-g_{ij}\tilde\sigma^k{}_k/2)u^iu^j\), a distinct quantity; it is not substituted for such a pair.

Source: [APS full-text PDF](https://harvest.aps.org/v2/journals/articles/10.1103/RevModPhys.48.393/fulltext), saved [PDF](prd_publisher_verify_20260907/rmp_pdf.pdf). PDF pages 8, 16, 17 and 18 (printed 400, 408, 409 and 410) were rendered and visually inspected.

**Access evidence.** All writes for this task are under bounce/. Direct-download byte counts are response-body lengths, including saved HTTP 403 challenge bodies. These challenge bodies are not publisher article text. Successful web-tool retrieval of APS landing/issue text is recorded separately: that tool does not expose origin HTTP status or raw response-byte count, so neither is invented. The PDF quotations come from the direct APS PDF downloads.

The following ledger records every distinct URL requested by the direct-download receipt pass. Web-tool searches and retrievals are preserved in web_evidence.txt; initial exploratory searches also located APS issue pages and supplied no additional equation evidence. No mirror or arXiv text was used. Local rendering artifacts and the web-tool transcript have their own byte counts and hashes below; those are local file measurements, not HTTP measurements.

- **prd_pdf** — URL: <https://harvest.aps.org/v2/journals/articles/10.1103/PhysRevD.85.107502/fulltext>; final URL: <https://harvest.aps.org/v2/journals/articles/10.1103/PhysRevD.85.107502/fulltext>; UTC: 2026-09-07T02:21:01.982907+00:00; HTTP **200**; **281368 bytes**; Content-Type: application/pdf; local path: `/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/weekend-video-sextet-20260808T0136K/bhu-acquisition-20260828/bounce/prd_publisher_verify_20260907/prd_pdf.pdf`; SHA-256: `edbbf7279e40d044130df35ce2b10c1281669dc2b9e90c2d61a0e6d308d744da`.

- **rmp_pdf** — URL: <https://harvest.aps.org/v2/journals/articles/10.1103/RevModPhys.48.393/fulltext>; final URL: <https://harvest.aps.org/v2/journals/articles/10.1103/RevModPhys.48.393/fulltext>; UTC: 2026-09-07T02:21:01.983161+00:00; HTTP **200**; **2276931 bytes**; Content-Type: application/pdf; local path: `/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/weekend-video-sextet-20260808T0136K/bhu-acquisition-20260828/bounce/prd_publisher_verify_20260907/rmp_pdf.pdf`; SHA-256: `a5aa872c97e88f2a5e72554974166e3c51c5b078889bcf8e531afda4b958bcb9`.

- **prd_doi** — URL: <https://doi.org/10.1103/PhysRevD.85.107502>; final URL: <https://link.aps.org/doi/10.1103/PhysRevD.85.107502>; UTC: 2026-09-07T02:21:01.983303+00:00; HTTP **403**; **5514 bytes**; Content-Type: text/html; charset=UTF-8; local path: `/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/weekend-video-sextet-20260808T0136K/bhu-acquisition-20260828/bounce/prd_publisher_verify_20260907/prd_doi.html`; SHA-256: `4892d96b7b568661d629ee27982feb957d4cef635c3bbe420d7a6f4f0ed6563d`.

- **rmp_doi** — URL: <https://doi.org/10.1103/RevModPhys.48.393>; final URL: <https://link.aps.org/doi/10.1103/RevModPhys.48.393>; UTC: 2026-09-07T02:21:01.983413+00:00; HTTP **403**; **5511 bytes**; Content-Type: text/html; charset=UTF-8; local path: `/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/weekend-video-sextet-20260808T0136K/bhu-acquisition-20260828/bounce/prd_publisher_verify_20260907/rmp_doi.html`; SHA-256: `b7c9f0cd76b80dca2ea524c585caf62ada3df9f017ac72e7c011138cf14492ab`.

- **prd_landing** — URL: <https://journals.aps.org/prd/abstract/10.1103/PhysRevD.85.107502>; final URL: <https://journals.aps.org/prd/abstract/10.1103/PhysRevD.85.107502>; UTC: 2026-09-07T02:21:01.983518+00:00; HTTP **403**; **5587 bytes**; Content-Type: text/html; charset=UTF-8; local path: `/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/weekend-video-sextet-20260808T0136K/bhu-acquisition-20260828/bounce/prd_publisher_verify_20260907/prd_landing.html`; SHA-256: `58bed3a21c2521d1eda9de789c45be4675aea48f3e328bf2f597093f978f6927`.

- **rmp_landing** — URL: <https://journals.aps.org/rmp/abstract/10.1103/RevModPhys.48.393>; final URL: <https://journals.aps.org/rmp/abstract/10.1103/RevModPhys.48.393>; UTC: 2026-09-07T02:21:01.983647+00:00; HTTP **403**; **5584 bytes**; Content-Type: text/html; charset=UTF-8; local path: `/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/weekend-video-sextet-20260808T0136K/bhu-acquisition-20260828/bounce/prd_publisher_verify_20260907/rmp_landing.html`; SHA-256: `e3a01bac2142c87f8be205af8bb055e0b4c31621b438337b354e72b6ff76e1b5`.

- **prd_errata** — URL: <https://journals.aps.org/prd/errata>; final URL: <https://journals.aps.org/prd/errata>; UTC: 2026-09-07T02:21:01.983780+00:00; HTTP **403**; **5458 bytes**; Content-Type: text/html; charset=UTF-8; local path: `/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/weekend-video-sextet-20260808T0136K/bhu-acquisition-20260828/bounce/prd_publisher_verify_20260907/prd_errata.html`; SHA-256: `bfdbecc49e44adda451cf117e6fa9c5968cf9420c9837f5c103d4bd62b9828f6`.

- **rmp_errata** — URL: <https://journals.aps.org/rmp/errata>; final URL: <https://journals.aps.org/rmp/errata>; UTC: 2026-09-07T02:21:01.983893+00:00; HTTP **403**; **5458 bytes**; Content-Type: text/html; charset=UTF-8; local path: `/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/weekend-video-sextet-20260808T0136K/bhu-acquisition-20260828/bounce/prd_publisher_verify_20260907/rmp_errata.html`; SHA-256: `4f8f56a70b8f530cf887ed1b68c2a3566451dead3f84054ac9e2d8212a04d690`.

- **prd_issue** — URL: <https://journals.aps.org/prd/issues/85/10>; final URL: <https://journals.aps.org/prd/issues/85/10>; UTC: 2026-09-07T02:22:40.245992+00:00; HTTP **403**; **5476 bytes**; Content-Type: text/html; charset=UTF-8; local path: `/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/weekend-video-sextet-20260808T0136K/bhu-acquisition-20260828/bounce/prd_publisher_verify_20260907/prd_issue.html`; SHA-256: `cd30f2af5aedc1186c6b103aea281a2df3b608c9738980a7583ac8b74222a3a7`.

- **rmp_issue** — URL: <https://journals.aps.org/rmp/issues/48/3>; final URL: <https://journals.aps.org/rmp/issues/48/3>; UTC: 2026-09-07T02:22:40.246341+00:00; HTTP **403**; **5473 bytes**; Content-Type: text/html; charset=UTF-8; local path: `/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/weekend-video-sextet-20260808T0136K/bhu-acquisition-20260828/bounce/prd_publisher_verify_20260907/rmp_issue.html`; SHA-256: `9d72ed23a576224918aa44f988d98602b587116e4f70d3c29855f59a93347f51`.

- **prd_crossref** — URL: <https://api.crossref.org/works/10.1103/PhysRevD.85.107502>; final URL: <https://api.crossref.org/works/10.1103/PhysRevD.85.107502>; UTC: 2026-09-07T02:22:40.246491+00:00; HTTP **200**; **7482 bytes**; Content-Type: application/json; local path: `/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/weekend-video-sextet-20260808T0136K/bhu-acquisition-20260828/bounce/prd_publisher_verify_20260907/prd_crossref.json`; SHA-256: `4581d6224beace68f79a21e6f44b92ef01700b10b919a67bebf156dfaef20849`.

- **rmp_crossref** — URL: <https://api.crossref.org/works/10.1103/RevModPhys.48.393>; final URL: <https://api.crossref.org/works/10.1103/RevModPhys.48.393>; UTC: 2026-09-07T02:22:40.246632+00:00; HTTP **200**; **27718 bytes**; Content-Type: application/json; local path: `/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/weekend-video-sextet-20260808T0136K/bhu-acquisition-20260828/bounce/prd_publisher_verify_20260907/rmp_crossref.json`; SHA-256: `6a71f0b6c1fbef095222df7d166265857aacbcd2c71c1b18c1d8bbba717b110a`.

- **prd_corrections_search** — URL: <https://journals.aps.org/search/results?q=%22Nonsingular%2C+big-bounce+cosmology+from+spinor-torsion+coupling%22&sort=relevance>; final URL: <https://journals.aps.org/search/results?q=%22Nonsingular%2C+big-bounce+cosmology+from+spinor-torsion+coupling%22&sort=relevance>; UTC: 2026-09-07T02:22:40.246760+00:00; HTTP **403**; **5892 bytes**; Content-Type: text/html; charset=UTF-8; local path: `/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/weekend-video-sextet-20260808T0136K/bhu-acquisition-20260828/bounce/prd_publisher_verify_20260907/prd_corrections_search.html`; SHA-256: `25fb8012d4160236f06110f01ea27e229483fc84941767f7834c1b330ad780fd`.

- **rmp_corrections_search** — URL: <https://journals.aps.org/search/results?q=%22General+relativity+with+spin+and+torsion%3A+Foundations+and+prospects%22&sort=relevance>; final URL: <https://journals.aps.org/search/results?q=%22General+relativity+with+spin+and+torsion%3A+Foundations+and+prospects%22&sort=relevance>; UTC: 2026-09-07T02:22:40.246879+00:00; HTTP **403**; **5907 bytes**; Content-Type: text/html; charset=UTF-8; local path: `/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/weekend-video-sextet-20260808T0136K/bhu-acquisition-20260828/bounce/prd_publisher_verify_20260907/rmp_corrections_search.html`; SHA-256: `96d0c58f768d4c4b498069deea75415d9982588af3423d101460bebb553a6914`.


Web-tool APS landing and issue reads: URLs are the same as prd_landing, rmp_landing, prd_issue and rmp_issue above. Result: publisher-page text retrieved. Origin HTTP status: **not exposed**; origin bytes: **not exposed**. Local transcript: `bounce/prd_publisher_verify_20260907/web_evidence.txt`. Direct HTTP 403 receipts above and successful web-tool text retrievals are distinct accesses. DOI opens and standalone errata/search endpoint opens in the web tool returned errors. Exact-title/citation search results contained no matching correction notice; they are not an exhaustive journal catalogue.


- **Local artifact** — path: `/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/weekend-video-sextet-20260808T0136K/bhu-acquisition-20260828/bounce/prd_publisher_verify_20260907/access.json`; HTTP: not applicable; **8331 bytes**; SHA-256: `66704c2fbd457338744c9020014bd3a602f79869e94e775139c7d28e05a6962d`. Locally serialized access evidence.

- **Local artifact** — path: `/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/weekend-video-sextet-20260808T0136K/bhu-acquisition-20260828/bounce/prd_publisher_verify_20260907/prd_page_2.png`; HTTP: not applicable; **445009 bytes**; SHA-256: `dd165e81e13cc0b6346db5d8e544796fc4f951169d3fe1994339ebe7d0666e50`. Rendered from prd_pdf.pdf.

- **Local artifact** — path: `/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/weekend-video-sextet-20260808T0136K/bhu-acquisition-20260828/bounce/prd_publisher_verify_20260907/rmp_eq_3_23_3_24.png`; HTTP: not applicable; **58286 bytes**; SHA-256: `17303bbf3e9c971371f56e147ce6f54aad293e5c46ac5a4641da78b37210bd76`. Rendered from rmp_pdf.pdf.

- **Local artifact** — path: `/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/weekend-video-sextet-20260808T0136K/bhu-acquisition-20260828/bounce/prd_publisher_verify_20260907/rmp_eq_5_18.png`; HTTP: not applicable; **91090 bytes**; SHA-256: `8c977d4e5f10ab606adb211b97a2037d3a2e830b256381c0ffa586bbfea72eae`. Rendered from rmp_pdf.pdf.

- **Local artifact** — path: `/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/weekend-video-sextet-20260808T0136K/bhu-acquisition-20260828/bounce/prd_publisher_verify_20260907/rmp_page_16.png`; HTTP: not applicable; **731568 bytes**; SHA-256: `bd22e2921dd7d95f2b1cd9ca74ccb359386680e59129e0977811a9cbfacff2fb`. Rendered from rmp_pdf.pdf.

- **Local artifact** — path: `/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/weekend-video-sextet-20260808T0136K/bhu-acquisition-20260828/bounce/prd_publisher_verify_20260907/rmp_page_17.png`; HTTP: not applicable; **826602 bytes**; SHA-256: `78ef799eee2f3e426dfcfad1638a231069c2ad5245ee51a1c02d67469281586a`. Rendered from rmp_pdf.pdf.

- **Local artifact** — path: `/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/weekend-video-sextet-20260808T0136K/bhu-acquisition-20260828/bounce/prd_publisher_verify_20260907/rmp_page_18.png`; HTTP: not applicable; **779884 bytes**; SHA-256: `3ac19abc4d6cbb2681c10a9c930ca234e26aa35bfca229f442bbbf4056cd5cc0`. Rendered from rmp_pdf.pdf.

- **Local artifact** — path: `/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/weekend-video-sextet-20260808T0136K/bhu-acquisition-20260828/bounce/prd_publisher_verify_20260907/rmp_page_8.png`; HTTP: not applicable; **733343 bytes**; SHA-256: `723bee34bc21c2505bf6108d447c84e007a6bede78e6713fa3250ee27a1974d7`. Rendered from rmp_pdf.pdf.

- **Local artifact** — path: `/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/weekend-video-sextet-20260808T0136K/bhu-acquisition-20260828/bounce/prd_publisher_verify_20260907/web_evidence.txt`; HTTP: not applicable; **58939 bytes**; SHA-256: `0dbdba1364cbf39c83c4dbdf454a1a1636d6d1be04bae52504675dc7adc859af`. Locally serialized access evidence.

**Final source record.** “No correction found” below has the limited scope stated above.

| source | publisher text obtained? | erratum? | tilde convention quoted | effective pressure correction sign |
|---|---|---|---|---|
| Popławski, PRD 85, 107502 (2012) | Yes — APS VOR PDF, 5 pages | No correction found; exhaustive later-correction absence unverified | Yes — sentence introducing (10), p. 107502-2; tildes designate the added contribution | \(+\alpha n^2\), printed in (12) |
| Hehl et al., RMP 48, 393 (1976) | Yes — APS VOR PDF, 24 pages | No correction found; exhaustive later-correction absence unverified | Yes — combined-tensor introduction and (3.23)–(3.24), p. 400; \(\tilde\sigma^{ij}\) is combined | \(-ks^2\), pressure coefficient in (5.18); separate unpolarised density/pressure pair not found |
