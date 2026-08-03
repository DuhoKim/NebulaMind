# External scientific-review reconciliation

Use this after Deep Research or another external reviewer returns a manuscript critique. The external report is advisory input, not the final scientific verdict.

## Verification pass

1. Re-derive every quoted model equation from the primary methods paper, including numerator/denominator direction and floors/caps.
2. Check the sign of every statistical correction. Intrinsic `M*|Mh` scatter, observational stellar-mass error, contamination, and selection incompleteness are distinct effects and need not move inferred host mass or efficiency in the same direction.
3. Distinguish a software toolkit from the physical model or fitting function it implements; changing software is not a scientific alternative to changing the HMF calibration.
4. Recalculate every headline ratio and label its statistic consistently. Do not compare an observed tail percentile with a simulated median or fixed-rank value and call the result a typical or median gap.
5. Separate valid cross-sectional fixed-rank comparisons from unsupported progenitor tracking. Merger-tree rank evolution matters only when the manuscript claims evolutionary lineage.
6. Reject categorical claims such as “mathematically impossible,” “absent,” or “ruled out” unless the implementation has a hard prohibition or a direct counterfactual proves it.
7. Inspect source roles and identities. A long source list does not prove that the cited source supports the attached assertion.

## Deep Research query-coverage and citation-role audit

When auditing a captured Deep Research report against a queued scientific question, grade four layers separately rather than issuing one impressionistic verdict:

1. **Query coverage:** decompose the queued question into explicit cells (for example, aperture threshold, calibration-by-calibration response, and resolved-versus-integrated offset). Mark each cell `PASS`, `PARTIAL`, or `FAIL`. A report that discusses ingredients in separate sections has not answered an interaction question unless it gives the cross-comparison.
2. **Estimand definition:** reject words such as “offset,” “global,” “resolved,” or “integrated” without the statistic and weighting convention. Require the x-axis, abundance diagnostic, aperture, mass/redshift range, sample, sign, dex value, and whether the comparison is flux-, area-, mass-, spaxel-, or H II-region-weighted. Relations with different independent variables are not directly offset-comparable until a mapping is defined.
3. **Numerical provenance:** trace each load-bearing number to its exact inline citation, not merely to another source somewhere in the index. Separate mean systematic shift, intrinsic scatter, object-level range, and threshold. Recompute simple transforms such as dex-to-factor independently, but do not let correct arithmetic rescue a mis-cited input value.
4. **Source identity and role:** first check that every internal anchor resolves, then independently verify title/authors/year/DOI or arXiv identity and whether that paper supports the attached claim. Mechanical anchor success is only a syntax pass. Flag aggregator/request pages, duplicate manuscript/final routes, locally scoped papers cited for high-redshift claims, and real-but-topic-mismatched papers.

For aperture/metallicity audits, keep these claim classes distinct:

- absolute zero-point differences among calibrations;
- aperture covering-fraction bias within a fixed calibration;
- DIG/line-mixing bias, whose sign and magnitude depend on the diagnostic;
- nuclear-versus-global metallicity differences;
- resolved-relation versus integrated-relation comparisons.

Do not combine them into one generic “systematic uncertainty.” A correction ledger should give the report line, current claim, exact primary result, disposition, and replacement scope. Preserve counterevidence already present in the source index: an uncited contradictory primary paper prevents categorical language such as “conclusively,” “entirely,” or “fundamental.”

Recommended delivery format:

- overall `PASS` or `FAIL — not science-drafting ready`;
- component verdicts with artifact line references;
- numerical claims distinguished as supported, mis-cited, or over-scoped;
- separate verdicts for source-index mechanics and scientific identity/role;
- claims requiring correction before drafting;
- an explicit no-edit statement when the audit is read-only.

## Source-access and artifact-identity gate

Before treating an external review as evidence about what a manuscript actually says:

1. Pin the reviewed artifact by a directly observed identity: canonical URL or path, retrieval time, byte length, `Last-Modified`/ETag when available, and SHA-256. For a repeatedly replaced PDF at one URL, use a cache-busting query or explicit no-cache request and hash the returned bytes.
2. Extract the complete artifact independently. If a generic web extractor returns language from an earlier revision, do not conclude that the public file is stale until a direct byte fetch and hash confirm it; intermediary caches can lag behind the origin.
3. Require a source-access attestation from the reviewer. A terminal answer that says the target was inaccessible, or that it reasoned only from prompt-supplied concerns, is **prompt-conditioned advisory output**, not a line-level review of the artifact.
4. Quarantine every reviewer claim about exact sections, figures, wording, or correction status when source access was not demonstrated. The reviewer may still suggest useful claim classes, but it cannot establish whether a correction landed.
5. Do not infer successful target access from a long answer, citation count, source anchors, or confident prose. Reconcile quoted text and section locations against the independently extracted artifact.
6. Preserve one-prompt/one-Start and pacing constraints. Do not automatically resubmit merely because the reviewer could not fetch the source; complete the direct reconciliation locally, or wait for an explicitly authorized later run with the full text supplied through an approved channel.

### Approval-safe text fallback and artifact-freshness gate

When PDF/network/browser access is denied but the user authorizes a local plain-text or TeX source:

1. Use only the authorized source and ordinary read/search tools. Do not bypass the approval boundary with `fitz`, shell downloads, alternate URLs, browser automation, or an external review submission unless separately authorized.
2. State the representation boundary. A text export containing `[FIGURE]` placeholders cannot verify labels embedded inside figure assets. Report those labels as **unverifiable from this artifact**, not passed or failed.
3. Before certifying a later revision, verify that the supplied artifact actually changed. If the read tool reports identical content, a hash is unchanged, or a duplicate-read guard says the region has not changed, treat the review artifact as stale/unrefreshed even if the changelog says edits landed.
4. Do not evade a duplicate-read or approval guard by changing offsets, switching to shell commands, or querying the same content through another tool. Report the stale-artifact blocker and ask for the authorized text export to be regenerated or supplied under a uniquely named, version-stamped path; verify that copy's header and targeted changes before resuming.
5. If an unblock explicitly authorizes local reads only, do not infer authorization for browser/account writes or Deep Research submission. Complete the source-grounded local audit and label the external run as gated.
6. In long revision loops, carry forward already verified sections and re-check targeted changed passages plus one final global sweep. This prevents repeated full reads while still catching stale wording in the abstract, introduction, figures, discussion, or conclusion.

## Figure-rendering and representation gate

Text extraction is not sufficient to verify that a revised figure landed correctly. Plot titles and captions may be updated while old semantics survive inside axes, legends, colorbars, annotations, shaded regions, or reference-line labels.

1. Inspect every regenerated figure visually at readable resolution, not only through extracted PDF text.
2. Audit the complete semantic surface: title, both axes, colorbar, legend, inline annotations, reference lines/regions, and caption.
3. Enforce global terminology. If a caption calls a quantity a conditional proxy but the axis still says “required efficiency,” “physical efficiency,” “ceiling,” “plausible maximum,” or similar, grade the correction `Partly landed`.
4. Treat visual labels as scientific claims. A label such as `epsilon_req`, “forbidden,” or “typical peak” can reintroduce an overclaim even when the surrounding prose is caveated.
5. When an embedded PDF viewer does not expose the rendered page, render the already pinned PDF bytes to temporary page images, inspect those images, and remove the temporary artifacts after review. Verify the bytes against the pinned SHA-256 before rendering so the visual audit cannot drift to another revision.
6. Keep visual legibility separate from scientific validity: report tiny labels, clipped annotations, or ambiguous color encodings independently from claim-level errors.

## Revision-consistency pass

A changelog records intended edits, not proof that they landed consistently. For every revision cycle:

- Build a correction ledger from the actual pinned artifact, not from the changelog or reviewer self-report.
- Sweep the abstract, final introduction paragraph, methods, results, every figure and caption, discussion, conclusion, and bibliography for residual old language.
- Treat a new caveat followed by an unchanged strong conclusion as an unresolved contradiction. The strongest uncaveated claim controls the verdict.
- Check terminology globally: a statistical proxy cannot be called conditional in one section and a physical measurement, requirement, ceiling, or achieved efficiency elsewhere.
- Verify every new in-text citation has an identity-complete bibliography entry and that author initials/identifiers agree.
- Report `Landed accurately`, `Partly landed`, or `Not landed` with exact artifact evidence. Separate safe prose/caption repairs from analyses that are legitimately deferred.

## Post-pass analysis-upgrade gate

A manuscript pass applies only to the pinned artifact and analysis scope that was reviewed. Adding a new measurement after a pass—especially a native simulation diagnostic—reopens the affected methods, results, abstract, discussion, conclusion, figures, and deferred-work ledger.

For a native central-galaxy efficiency or baryon-conversion upgrade:

1. Remove every stale statement that the native analysis is deferred, unavailable, or beyond the draft. Search the introduction, proxy section, figure captions, limitations, and conclusion—not just the deferred-work list.
2. Define the native estimand separately from any analytic fixed-rank proxy. Prefer an integrated stellar-to-halo baryon-conversion fraction such as `Mstar(<aperture)/(fb M200c)`; do not conflate it with instantaneous `SFR/(fb Mdot_h)` efficiency.
3. Make the calculation reproducible: central-selection field/criterion, group join, halo-mass field and mass definition, unit and `h` conversion, stellar aperture, binning, summary statistic, counts per bin, and uncertainty/percentile representation.
4. Restrict redshift claims to common support. If the highest-redshift snapshot truncates below the massive-halo regime, say the native result shows no evident rise only over the overlapping halo-mass range; it does not confirm the unsampled high-mass trend.
5. Treat proxy and native values as different estimands. If the proxy is numerically higher, say it returns higher values than the native central ratio and therefore should not be interpreted as a physical measurement; do not call the difference an unbiased overestimate without matched-object/statistic evidence.
6. Report peaks and flatness descriptively unless bin counts, uncertainties, and a trend test support stronger language. A figure alone is not enough when its statistic and support are undocumented.
7. Promote the new native result into the abstract only with the same support and volume caveats used in the results. Keep corrected observed-GSMF and simulation-convergence requirements explicit when they remain outstanding.

## Delivery rule

Preserve the raw review as custody when required, but deliver a separately verified synthesis. Explicitly flag and correct consequential reviewer errors rather than silently forwarding them. If source access failed, state that qualification prominently and exclude ungrounded line-level claims from the final verdict. For high-redshift galaxy work, pair this reference with `high-redshift-abundance-matching-audit.md`, `simulation-subgrid-physics-audit.md`, and `theory-representation-audit.md`.
