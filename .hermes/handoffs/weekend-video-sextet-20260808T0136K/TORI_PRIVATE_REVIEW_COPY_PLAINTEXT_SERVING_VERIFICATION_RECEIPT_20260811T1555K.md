# Tori verification receipt — byte-identical plain-text private review copy

Timestamp: `2026-08-11T15:55:18+0900 KST`

Marker: `TORI_PRIVATE_REVIEW_COPY_PLAINTEXT_SERVING_VERIFICATION_RECEIPT_20260811T1555K`

Scoped result: `PASS_EXACT_BYTES_AND_INLINE_DISPLAY__FAIL_BROWSER_UTF8_DECODING_BECAUSE_CHARSET_HEADER_IS_ABSENT__DUHO_MUST_NOT_RELY_ON_CURRENT_BROWSER_VIEW_YET`

## 1. Authority and action classification

The new plain-text review copy was disclosed at the moment of acting under Duho's standing order to make the gated note readable through the private cockpit.

Classification: `NO_AUTHORIZATION_BREACH_FOUND`.

The action does not confer publication, acceptance, registry, renderer, Git, frontend, YouTube, public-exposure, or scientific-execution clearance. Duho still decides.

This receipt is required because exact transfer bytes and browser-visible decoding are separate checks. The transfer bytes pass; the current browser-visible decoding does not.

## 2. Local byte identity: PASS

Gated source:

- Path: `/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/weekend-video-sextet-20260808T0136K/reviews/LANA_METHODS_NOTE_MITTAL_SINGAL_ATTRIBUTABILITY_20260811_EXTERNAL.md`
- Bytes: `11,473`
- SHA-256: `a79f748e42cf92d1831e6115b7ce55912afe4b0555fb9bc185b6d9428edc292b`

Plain-text copy:

- Path: `/Users/duhokim/HermesOps/cockpit/methods-note-mittal-singal.txt`
- Bytes: `11,473`
- SHA-256: `a79f748e42cf92d1831e6115b7ce55912afe4b0555fb9bc185b6d9428edc292b`
- Filesystem MIME inspection: `text/plain; charset=utf-8`
- `cmp` against the gated source: exit `0`.

Finding: `PASS_BYTE_IDENTICAL_LOCAL_COPY`.

There is no conversion or derived-content comparison at rest: the local `.txt` file is the exact gated artifact bytes.

## 3. Source and frozen-render custody: PASS

Two consecutive hash rounds one second apart at `2026-08-11T15:54:19+09:00` were identical.

The three Markdown artifacts remain unchanged:

1. Authoritative: `36e4efe8984c8d5f7f6f1996f2d6efb38a1be2ceade49b4622f0131917fb99aa`.
2. CLEAN: `80b1d1425a9fa28a17b27c3ae599eb5c231c31ae46ad9871ce468cf386489aa7`.
3. External source: `a79f748e42cf92d1831e6115b7ce55912afe4b0555fb9bc185b6d9428edc292b`.

The three failed HTML renders remain unchanged:

1. V1: `5a5bf634ab20984536e52bb37ce924f65e2794ae714fe67e1a1dd36f77806557`.
2. V2: `ffd3086b8b8f8ee00db7ba07bb3ac19ba1b2d0f8dc080e8944240c2fc8c1e9ce`.
3. V3: `25de23fae7473d2753bda74e47156d1164f16f35da13328fa9a65a6bd8156fca`.

Finding: `PASS_ALL_FROZEN_ARTIFACT_HASHES_UNCHANGED`.

Current state proves the files are distinct and stable. As in the earlier receipts, the no-overwrite pre-state remains the actor's contemporaneous disclosure because Tori did not possess a pre-write snapshot.

## 4. Served transfer bytes: PASS

Actual private Tailnet route:

`https://duho-macstudio.taila27502.ts.net/cockpit/methods-note-mittal-singal.txt`

Local backing route:

`http://127.0.0.1:8093/cockpit/methods-note-mittal-singal.txt`

Both routes returned:

- HTTP status: `200`.
- `Content-Type`: `text/plain`.
- `Content-Length`: `11473`.
- `Content-Disposition`: absent.
- Response-body SHA-256: `a79f748e42cf92d1831e6115b7ce55912afe4b0555fb9bc185b6d9428edc292b`.
- Response-body `cmp` against gated source: exact.

The private Tailnet response therefore transfers the exact gated bytes.

Evidence:

- Local headers SHA-256: `883e41e0aa390a78ed8bb0498d483aa06b798a0429c673eeea9d10f0efeafafc`.
- Local body SHA-256: `a79f748e42cf92d1831e6115b7ce55912afe4b0555fb9bc185b6d9428edc292b`.
- Tailnet HTTPS headers SHA-256: `3157f1ab6178e494cebb4965c6becd63c056adaf463d251063b77f07917a6cb7`.
- Tailnet HTTPS body SHA-256: `a79f748e42cf92d1831e6115b7ce55912afe4b0555fb9bc185b6d9428edc292b`.

Finding: `PASS_SERVED_BODY_BYTE_IDENTITY`.

## 5. Inline rather than download: PASS

Headless Chrome 151 opened the exact Tailnet HTTPS route.

The browser:

- created an inline `<pre>` element;
- used `word-wrap: break-word; white-space: pre-wrap;`;
- created no download link or `[download]` element;
- displayed the response in the browser viewport;
- did not trigger a file download.

The absent `Content-Disposition: attachment` header is consistent with the observed inline display.

Finding: `PASS_INLINE_NOT_DOWNLOAD`.

## 6. Browser readability: FAIL because HTTP omits UTF-8 charset

Although the local file detector identifies UTF-8, the HTTP response sends only:

`Content-Type: text/plain`

It does **not** send:

`Content-Type: text/plain; charset=utf-8`

Chrome therefore decoded the exact UTF-8 transfer bytes using a different legacy encoding. The browser view contains extensive mojibake:

- Source Unicode characters: `11,324`.
- Browser `<pre>` Unicode characters: `11,375`.
- Non-equal diff opcodes: `72`.
- Unicode replacement characters `�`: `96`.

Examples visible in Chrome:

- em dash `—` displays as `��`;
- the en dash in `Mittal–Singal` is corrupted;
- section sign `§` displays as `짠`;
- `λᵢ·sᵢ` displays as `貫巢◈톝巢�`;
- degree sign `°` displays as `째`;
- other Greek letters, subscripts, superscripts, arrows, and scientific symbols are also corrupted.

Browser evidence:

- Dumped DOM SHA-256: `ca165b69b4eb316572efc1272de22d4b23f4b2115c0bb740e564ade934357d19`.
- First-viewport screenshot SHA-256: `5ca69104b39f1c41caee54d56383ead31de964efa91996301a6eecc36f99f9a0`.

Finding: `FAIL_BROWSER_VISIBLE_UTF8_DECODING`.

This is not a content conversion defect and does not challenge byte identity. It is a serving-metadata defect at the browser decoding layer. Byte identity proves what was transferred; the `charset` parameter controls how those bytes are displayed.

## 7. Decision and minimal next action

Overall:

- Byte-identical local copy: `PASS`.
- Three Markdown hashes unchanged: `PASS`.
- Three failed-render hashes unchanged: `PASS`.
- Tailnet HTTP 200 and exact response body: `PASS`.
- Inline browser display rather than download: `PASS`.
- Browser-readable exact Unicode text: `FAIL`.

Duho **cannot yet rely on the current served browser view as the exact reading copy**, because scientific notation and punctuation are visibly corrupted despite exact transfer bytes.

The conversion line can remain abandoned. Do not change the `.txt` body. The minimal correction is response metadata only:

`Content-Type: text/plain; charset=utf-8`

with no `Content-Disposition: attachment`.

After that header-only serving correction, re-check:

1. HTTP 200.
2. Response body hash still `a79f748e…`.
3. `Content-Type` includes `charset=utf-8`.
4. No attachment disposition.
5. Browser `<pre>` text equals the gated source and scientific symbols display correctly.

## 8. Shape-green/content-red lesson is already recorded

No skill patch is needed. The current `cockpit-handoff-review` skill is version `1.4.2`, and its reference
`references/private-review-markdown-html-visible-equivalence.md`
already records the lesson explicitly:

- row and cell counts are only preliminary;
- a candidate can remain `9 × 2` while a row is truncated to two fragments;
- shape-green/content-red is still HOLD;
- compare every normalized cell string in order;
- bind canary notation and source attribution to the exact expected cell;
- whole-page token counts cannot substitute for per-cell comparison.

That matches the user's correction: a count check cannot detect truncation to the expected count.

Duho still decides. No source note, plain-text body, cockpit file, server configuration, renderer, registry, frontend, Baseline, DB, Git, deploy, publication, acceptance, or scientific artifact was mutated by Tori during this verification. Only append-only audit evidence and this receipt were written in the assigned handoff workspace.
