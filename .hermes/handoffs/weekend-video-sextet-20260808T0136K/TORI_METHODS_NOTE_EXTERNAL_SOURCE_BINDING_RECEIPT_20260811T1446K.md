# Tori custody receipt — external Mittal–Singal methods-note source binding

Timestamp: `2026-08-11T14:46:20+0900 KST`

Marker: `TORI_METHODS_NOTE_EXTERNAL_SOURCE_BINDING_RECEIPT_20260811T1446K`

Scoped result: `PASS_SOURCE_BINDING_WITH_SIZE_UNIT_CORRECTION__PASSED_NOTE_UNCHANGED`

## Scope and authority boundary

This receipt binds sources for the exact external-edition bytes already passed by Kun. It does not re-gate, edit, replace, publish, upload, accept, or otherwise mutate any note.

Kun gate:

- Path: `/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/weekend-video-sextet-20260808T0136K/reviews/KUN_METHODS_NOTE_MITTAL_SINGAL_EXTERNAL_GATE_20260811T1432K.md`
- SHA-256: `3fdff0d48af5e0a1a008818bfca332c0c8f4f2c9419dbd5558530a4861afae45`
- Bytes: `3,673`
- Verdict in the gated bytes: `PASS_EXTERNAL_METHODS_NOTE_NO_OVERCLAIM`
- Gated external target SHA-256: `a79f748e42cf92d1831e6115b7ce55912afe4b0555fb9bc185b6d9428edc292b`

No gated note was edited.

## 1. Exact three-artifact binding

### Authoritative internal note / provenance record

- Path: `/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/weekend-video-sextet-20260808T0136K/reviews/LANA_METHODS_NOTE_MITTAL_SINGAL_ATTRIBUTABILITY_20260811.md`
- SHA-256: `36e4efe8984c8d5f7f6f1996f2d6efb38a1be2ceade49b4622f0131917fb99aa`
- UTF-8 bytes: `17,494`
- Unicode characters: `17,292`
- Lines: `187`
- Role: authoritative internal Rev 3 note and append-only Rev 2/Rev 3 provenance record.

The supplied hash prefix and `17,494`-byte count both match.

### Clean derivative

- Path: `/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/weekend-video-sextet-20260808T0136K/reviews/LANA_METHODS_NOTE_MITTAL_SINGAL_ATTRIBUTABILITY_20260811_CLEAN.md`
- SHA-256: `80b1d1425a9fa28a17b27c3ae599eb5c231c31ae46ad9871ce468cf386489aa7`
- UTF-8 bytes: `12,439`
- Unicode characters: `12,283`
- Lines: `131`
- Role: deletion-only derivative of the authoritative internal note.

**Size-unit correction:** the supplied `12,283` value is the Unicode character count, not the byte count. The exact hash is correct; the actual UTF-8 byte count is `12,439`. This metadata correction does not change either note or Kun's hash gate.

### External edition

- Path: `/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/weekend-video-sextet-20260808T0136K/reviews/LANA_METHODS_NOTE_MITTAL_SINGAL_ATTRIBUTABILITY_20260811_EXTERNAL.md`
- SHA-256: `a79f748e42cf92d1831e6115b7ce55912afe4b0555fb9bc185b6d9428edc292b`
- UTF-8 bytes: `11,473`
- Unicode characters: `11,324`
- Lines: `120`
- Role: seat-name-free external edition passed by Kun.

**Size-unit correction:** the supplied `11,324` value is the Unicode character count, not the byte count. The exact hash is correct and equals Kun's gated target hash; the actual UTF-8 byte count is `11,473`. This metadata correction does not change the external edition or its pass.

## 2. Independent deletion-only verification

The authoritative internal note and CLEAN derivative were compared independently at both line and character level.

Result: `PASS_PURE_DELETION`.

- Equal line spans: `2`.
- Deleted line spans: `2`.
- Inserted line spans: `0`.
- Replaced line spans: `0`.
- Source lines retained byte-for-byte in CLEAN: `131`.
- Source lines deleted: `56`.
- Target lines introduced: `0`.
- Character-level operations: equal/delete only; `0` insert and `0` replace operations.

Exact source deletion spans:

1. Authoritative source lines `7–51` inclusive: `45` lines, SHA-256 of deleted UTF-8 span `2ae76a887321e3a58f89ad24a1ef014a626276f9535ee9b53c095f326c79be22`. This removes the leading blank, Rev 2/Rev 3 changelog blockquotes, and separator.
2. Authoritative source lines `177–187` inclusive: `11` lines, SHA-256 of deleted UTF-8 span `7bcced3927f54fdd305069252b7829f818683e98162d8d7a5bd9139c14cf0402`. This removes the leading blank plus the Disposition section.

Every surviving CLEAN line is an exact line from the authoritative note in the same order. No surviving sentence was rewritten. The deletion-only statement applies to authoritative → CLEAN; it is not asserted for the separately edited seat-name-free external edition.

## 3. Binding the external edition's product-check claim

External-edition claim being bound:

> “For this note, the v0.1.0 catalogues and selection maps were downloaded and checked against the published MD5 checksums and byte counts; they match.”

Finding: `CONFIRMED_AS_ACTUALLY_PERFORMED_BY_TORI_IN_THIS_NOTE_CUSTODY_WORKFLOW`.

Initial download/check date: `2026-08-11`.

Prior Tori custody receipt:

- Path: `/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/weekend-video-sextet-20260808T0136K/TORI_TO_HWAO_MITTAL_SINGAL_CUSTODY_ASSESSMENT_RECEIPT_20260811T1125K.md`
- Receipt timestamp: `2026-08-11T11:25:21+0900 KST`
- SHA-256: `f9ced629aa5a9ac6eb903f7d4d3f1614b1b42e5bfa97614a137a04c7eeaad5df`

Exact binary receipt referenced by that custody receipt:

- Path: `/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/weekend-video-sextet-20260808T0136K/mittal-singal-recoverability-20260811T1110K/TORI_QUAIA_V0P1_EXACT_PRODUCT_CUSTODY_RECEIPT_20260811T1122K.json`
- SHA-256: `f98942c288ca1ac8ceb65b93407375be97c1198d53a0b80da7eba4db7ab97bd6`

Published dataset identity:

- Quaia version: `0.1.0`
- Zenodo record: `8060755`
- DOI: `10.5281/zenodo.8060755`
- DOI URL: `https://doi.org/10.5281/zenodo.8060755`

The four downloaded files were freshly re-hashed at `2026-08-11T14:45:21+09:00`. Every current local byte count, MD5, and SHA-256 matched the prior binary receipt; every byte count and MD5 also matched the saved and live Zenodo record.

| Exact downloaded artifact | Absolute local path | Published bytes | Published MD5 | Current SHA-256 | Fresh match |
|---|---|---:|---|---|---|
| `quaia_G20.0.fits` | `/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/weekend-video-sextet-20260808T0136K/mittal-singal-recoverability-20260811T1110K/exact-products/quaia-v0.1.0/quaia_G20.0.fits` | `99,786,240` | `42cec6519d139ac5fdcf4f891a68b5d4` | `87b03f9dc9bd5105c9df85574a890a269a7d404392b3907d15c790082bbf2ef1` | `true` |
| `quaia_G20.5.fits` | `/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/weekend-video-sextet-20260808T0136K/mittal-singal-recoverability-20260811T1110K/exact-products/quaia-v0.1.0/quaia_G20.5.fits` | `171,020,160` | `8b816b719e8c8ccd1c0a648b53557ddd` | `918fbac2aa6303ff627ad356a1663c3401f8326240fbd75c22b29c38ea915a6d` | `true` |
| `selection_function_NSIDE64_G20.0.fits` | `/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/weekend-video-sextet-20260808T0136K/mittal-singal-recoverability-20260811T1110K/exact-products/quaia-v0.1.0/selection_function_NSIDE64_G20.0.fits` | `400,320` | `e62df7437156763ee59210976a808e45` | `f51b40b4ec42bec91f0e8972515247ea6cb06c0c77b6d9af4b97beddb71aa887` | `true` |
| `selection_function_NSIDE64_G20.5.fits` | `/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/weekend-video-sextet-20260808T0136K/mittal-singal-recoverability-20260811T1110K/exact-products/quaia-v0.1.0/selection_function_NSIDE64_G20.5.fits` | `400,320` | `d327cafb2011ac4a4ceafb57e7b553f3` | `24e24bab959806c95ec8330993e4a6a33af053ad8615f7950341a2ea57814cd4` | `true` |

Nothing attributed to this download-and-check claim was left unperformed: both named catalogues and both named selection maps were downloaded and checked. Scope boundary: the released Quaia random catalogues were not downloaded in that check, and the external edition does not claim that they were.

This verification establishes the public `0.1.0` product identities and supports Singal's explicit binding. It does not upgrade Mittal's unstated input bytes to byte-verified identity.

## 4. Non-authoritative Hwao trace audit

Excluded artifact:

- Path: `/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/weekend-video-sextet-20260808T0136K/HWAO_LOOSENED_BAR_MITTAL_SINGAL_ASSESSMENT_20260811T1110K.md`
- SHA-256: `1bdf7d66fc3168d2db7a54632a411024b564f4acd0328c6dbb43c86b89a0c25d`
- Status: `NON-AUTHORITATIVE`.

External-edition mechanical scan:

- `Hwao`: `0` occurrences.
- `1bdf7d66`: `0` occurrences.
- Exact excluded-artifact filename: `0` occurrences.
- `spherical harmonic` / `spherical-harmonic`: `0` occurrences.
- `multipole leakage`: `0` occurrences.
- `f_sky`: `0` occurrences.
- “magnitude cuts are unstated”: `0` occurrences.
- Exact normalized sentence overlap of at least 60 characters between the external edition and excluded Hwao artifact: `0` sentences.

Semantic cross-check also finds the external edition uses the corrected, contrary facts:

- Quaia `v0.1.0`, not Hwao's `v1` label.
- Singal's magnitude cuts are stated, not unstated.
- Singal's `30°/35°/40°` latitude cuts are stated, not only `30°`.
- Mittal is described as Bayesian model comparison over masked selection-treated pixel counts, not a spherical-harmonic estimator.
- The finding is non-attributability from the published record, not Hwao's “fully adjudicable” claim.

Finding: `PASS_NO_FACTUAL_CLAIM_TRACE_TO_NON_AUTHORITATIVE_HWAO_ASSESSMENT`.

The authoritative internal note retains Hwao only as an explicit correction/exclusion in its changelog, corrections section, and provenance boundary. CLEAN likewise retains the exclusion. The external edition removes the seat and the excluded artifact entirely; its provenance table points to published papers or the note's stated checks.

## 5. Goru-attribution audit

- External edition: `0` occurrences of `Goru`.
- CLEAN derivative: `0` occurrences of `Goru`.
- Authoritative internal note: the lexical occurrences of `Goru` are confined to the Rev 3 changelog and Disposition audit trail that records removal of the unsupported attribution. No active factual claim or active provenance-table row attributes evidence to Goru.
- No distinct Goru facts packet exists in the lane.

Finding: `PASS_NO_SURVIVING_GORU_FACT_ATTRIBUTION`.

The external edition is also mechanically seat-name-free: whole-word occurrence counts for `Lana`, `Tori`, `Kun`, `Hwao`, `Goru`, `Duho`, and `seat` are all zero.

## 6. Corrected-amplitude binding

External edition, exact current statement:

- `0.0048` for Quaia low.
- `0.0043` for Quaia high.

Tori custody receipt, spectral-index-correction bullet:

- “expected amplitudes become `0.0048` and `0.0043`”.

The values and order match exactly. The external edition labels the original `0.0080/0.0068` pair superseded and draws no numerical attribution or exclusion inference from either pair.

Finding: `PASS_CORRECTED_EXPECTED_AMPLITUDES_MATCH_TORI_RECEIPT`.

## Final binding result

The external edition's download/check statement now has an exact, separately hashed receipt chain behind it. The authoritative → CLEAN deletion-only claim passes independently. The external edition remains the exact Kun-passed hash and contains no surviving Hwao factual dependency, Goru fact attribution, or stale corrected-amplitude pair.

The two supplied CLEAN/external size values were character counts mislabeled as bytes; exact byte counts are corrected in this receipt without touching either gated note.

Nothing was published, uploaded, accepted, rendered, registered, committed, pushed, or sent to YouTube. No cockpit, registry, Git, renderer, or scientific execution action occurred. Duho decides after reading.
