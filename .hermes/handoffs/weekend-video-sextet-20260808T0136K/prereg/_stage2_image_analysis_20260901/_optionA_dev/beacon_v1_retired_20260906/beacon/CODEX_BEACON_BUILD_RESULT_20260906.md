PASS — 41 tests: fourier/driver 27, corpus identity 4, beacon 10; zero ResourceWarnings.

Refusal tokens emitted by the builder:

- BEACON-RECORD-INVALID-JSON
- BEACON-RECORD-MISSING-FIELDS
- BEACON-SOURCE-INVALID
- BEACON-VALIDATION-ARGS-MISSING
- BODY-DIGEST-INVALID
- DRAND-CHAIN-MISMATCH
- DRAND-FALLBACK-MISSING
- DRAND-FETCHED-TOO-EARLY
- DRAND-ROUND-MISMATCH
- DRAND-SEED-MISMATCH
- FETCHED-UTC-INVALID
- NIST-CHAIN-MISMATCH
- NIST-SEED-MISMATCH
- NIST-STATUS-NONZERO
- NIST-TIMESTAMP-MISMATCH
- NIST-URI-INVALID
- PULSE-INVALID
- RULE-DIGEST-INVALID
- RULE-DIGEST-MISMATCH
- SEED-WITHOUT-BEACON-RECORD
- STATEMENT-DIGEST-MISMATCH
- STATEMENT-DOES-NOT-BIND
- T-PULSE-MISMATCH
- T-SIGN-INVALID

Changed-file SHA-256 values:

- beacon/fetch_beacon.py: 278e9be23055646de61516a23fa223735b489d5e83b6008d424e058cdba5f503
- beacon/test_fetch_beacon.py: a70f5381b94c547015ab7f2978d49ce7c96c7618a5789665bfd779268db1c4da
- corpus_identity/build_corpus_identity.py: f142a00a10c1e8441015bdc174c8faf86c519015d135222563764e3e9e368ec0
- corpus_identity/test_build_corpus_identity.py: 9d79787c6d4928f434e03a25032d02a264e0166f411517ee6dbc0241c3ab280a
- fourier_chirality/run_configurations.py: b8656ce4dc023f511f97fe2b1b26bfa265136b3ee9bcaa2918cb1b0038f18765
- fourier_chirality/test_run_configurations.py: 0bfa33b7cf2d011dab7bf772536f17eac46bacfab552a75f11926c1b5e8c77a8

Fetcher defect found beyond the specified unclosed-file spots: none. The specified file handles were changed to context-managed opens without changing beacon selection behavior.

Could not do: embed RESULT.md's own SHA-256 inside RESULT.md. That is a self-referential digest and cannot be made byte-honest. All other changed files are listed above. The response-body digest is syntax-checked but cannot be recomputed because the fetcher record does not retain the response bytes; the builder comment records that third-party re-fetch is required, as specified.
