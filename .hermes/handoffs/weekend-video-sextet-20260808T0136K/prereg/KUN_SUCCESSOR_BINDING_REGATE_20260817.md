PASS_SUCCESSOR_ROUTE_BINDING

# Kun successor binding re-gate — route B public HTTPS

Date: 2026-08-17 KST
Scope: document review only; no network, no HEAD, no checksum harvest, no download, no endpoint, no commit, no push.

## 1. HOLD_IMAGE_METADATA_SCOPE

The ceiling design closes the prior hold. The v1 problem was that approval still required an exact pre-approval byte total even though route B had no authorized way to obtain image `Content-Length` / `Last-Modified` before approval without either moving image bytes or adding a full image-metadata pass. The v2 successor no longer pretends those fields are sealed-manifest fields. It states that per-file size and `Last-Modified` are recorded at retrieval time, while pre-retrieval approval binds:

- the sealed URL manifest hash;
- the exact required file count;
- the approved byte ceiling and its 1,024-URL sampling receipt;
- the pacing plan.

That is a meaningful approval, not a hollowed-out one. Duho is approving the exact input set and a maximum authorized retrieval scale, not a courtesy census. The digest remains the custody binding; the ceiling is an operational authorization bound.

## 2. Enforceability

Section 5.1.1.3 is structural enough for this route-binding gate. It requires that cumulative received bytes crossing the approved ceiling is a terminal custody event: stop, receipt, and human decision by Duho, parallel to the block-handling rule in §5.4.6. Section 5.2 also makes the downloader receipt record cumulative received bytes against the ceiling and the terminal event on crossing it. This is not merely advisory language.

Implementation gate note: the downloader should enforce this as early as the HTTP response permits, using retrieval-time `Content-Length` to avoid knowingly starting a file that would cross the ceiling. The route binding already makes crossing terminal; the build gate can prove the exact mechanics.

## 3. The +25% ceiling

The +25% margin is not evidence and should not be cited as one. It is a frozen authorization margin over a 1,024-request stratified sample estimate. That is acceptable here because the byte ceiling is not the source-byte binding and is not used to identify DR10.1 bytes; it is a campaign-scale guard. Actual bytes between the sample estimate and the ceiling are authorized and receipted normally. Actual bytes above the ceiling are terminal and require Duho's human decision before any resumption.

The margin is partly policy, not a statistically derived confidence interval. That is not a hold because the successor states the loss plainly: the a-priori figure is an estimate, not a census. The binding value is the exact file set plus digest list; the ceiling only bounds transfer scale.

## 4. What Is Lost

The exact pre-approval byte total is lost under route B unless one spends another large request campaign to collect uncorroborated server headers. That loss does not matter to the sealed-manifest guarantee. The frozen design's approved byte total was useful as a scale disclosure, but not as source-byte evidence. V2 improves the operational side by making the approved scale haltable and receipted.

## 5. Prohibition Scope

The size-sample operation stays within the re-scoped prohibition. It is limited to exactly 1,024 manifest-listed image URLs, `HEAD` only, no body bytes, paced under §5.4 tier-2, and receipted. The document explicitly says this is not a license for range requests, which remain forbidden. Recursive retrieval, wildcard expansion, mirroring/crawling, public cutout-service calls, and unmanifested URLs also remain forbidden.

## 6. Reconfirmations

- Predecessor `TORI_ROUTE_BINDING_20260815.md` is byte-unmoved: SHA-256 `c7ed11c12ad7c26db8ce784b4d4d76c86694231d4eaab42b3ddca720a265d4cb`, mode `444`.
- Successor under review matches the pinned v2 hash: `1371b11094a2765228a7deb1bbe1367117c9452dbea4513519bf99b7ce23fe8b`.
- Prior HOLD transcription matches: `KUN_SUCCESSOR_BINDING_GATE_20260817.md` SHA-256 `edbe88a52c9755bfebfd709a07c5ef0d2d9c47ec7d04be863d711a84e918f43f`.
- Sections 6-10 remain unamended in force; the status note is informational and delivery-channel-independent.
- R1 and R2 are incorporated in §11 step 4b; R4 is satisfied by gating/freezing this successor before manifest work; R3 is closed by `CHECKSUM_FRESHNESS_RESOLVED_20260817.md` with standing re-verification at manifest time.
- `Last-Modified` remains labelled weaker evidence; digest carries the binding.
- Pacing asymmetry is correctly specified: later survey/NERSC guidance may tighten without re-gate, never loosen without re-gate.
- The document plainly declares itself a draft proposal, not binding or executable until Kun gates it and Duho accepts and freezes it.

## Boundary

Network calls: 0. HEAD requests: 0. Checksum files fetched: 0. Image bytes fetched: 0. Endpoints activated: 0. Manifests built: 0. Retrieval authorized by this report alone: 0. Commit/push/publication: 0.
