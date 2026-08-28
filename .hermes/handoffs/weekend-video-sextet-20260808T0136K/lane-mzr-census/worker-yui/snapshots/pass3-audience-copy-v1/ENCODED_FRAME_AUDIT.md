# Deepening pass 3 — fresh encoded-frame scientific-presentation audit

Audit timestamp: 2026-08-08T02:53:55+09:00

Exact read-only candidate: `/Users/duhokim/HermesOps/cockpit/videos/mzr-archive-census-narrated-20260808T0155.mp4`

Candidate SHA-256: `0bdfd12dcc87098e1034196bc973df4ace79044cadc4261f3f827b65d7cd162d`

Fresh verification: 13,989,937 bytes; 128.4 s; H.264 1920×1080 at 30 fps plus AAC mono 24 kHz. The candidate hash and mtime are unchanged. Thirty-two new encoded frames were extracted every four seconds. Contact-sheet SHA-256: `a54f9c5d7fc1cd3e7b0f186bdec4d6c5f44147b154bdc9ae7487f0bc797826df`.

All findings below are from encoded pixels. No audio, renderer intent, or unpublished state is inferred.

## Reconfirmed blockers

- 016–024 s: a metallicity-versus-redshift scatter remains titled `The spread this work is about`; the body says this census exists to measure the spread. T1 is an archive metadata enumeration and reports no metallicity/MZR measurement.
- 032–040 s: retrieval channels and exact per-axis counts remain prose rather than evidence graphics.
- 044–052 s: `157` dominates; `178`, `21`, and their conservation are body copy. The 19-redshift/2-abundance split and modifier examples are absent. `source: T1_FINDINGS.md` is audience-visible.
- 056–068 s: 157-versus-62 proportional geometry and giant `62` still call the term-regex result `explicit gas-phase evidence`. The frame does not show 62 as a side diagnostic, does not send all 157 directly to T2, and exposes internal file/run labels.
- 072–084 s: the retrieval instrument check remains prose; `7/7`, `0/3`, and `PRECISION NOT CERTIFIED` are absent.
- 088–096 s: the frozen contract remains prose; application-not-completed and no-eligible-table-count are not visible gate states. `source: FREEZE_RECORD_T2.md` is audience-visible.
- 104–116 s: the closing discussion still compresses symbol/meaning collisions and target-domain mismatches into `symbol Z, not the concept`.
- Section holds and long prose cards remain dominant over evidence-bearing graphics.

## New pass-3 representation findings

### 1. Opening unit and physical-presence overstatement

At 004–012 s the audience copy reads:

> A pre-registered census of catalogues carrying gas-phase metallicity, stellar mass and redshift together.

The frozen unit is a **single table**, and T1 establishes metadata-reachable columns, not that catalogues physically carry three adjudicated measurements. The opening also omits the persistent single-table/crossmatch boundary. This wording lets archive metadata reach masquerade as physical data presence before the later caveats appear.

### 2. The 157 card repeats the same semantic overstatement

At 044–052 s the body reads:

> candidate tables carry all three axes, drawn from 178 before the modifier filter, with 21 dropped and each drop recorded.

`Carry all three axes` is looser than the evidence. The defensible wording is `single tables with metadata-reachable columns on all three axes` or `recorded three-axis metadata candidates`. The frame still does not render the 178−21=157 conservation or 19/2 bins.

### 3. The T2 card omits the operative current state

At 088–096 s the title says `The rules are now frozen` and the body says the contract was frozen before any table was judged. It does not display that application to all 157 is not completed or that there is no eligible-table count. Contract provenance is not a substitute for an application/result gate.

### 4. Final closure replaces scientific status with generic provenance

At 124 s the final audience copy is:

> Contract frozen before measurement. Every number read from a recorded artifact.

The close does not state reportable-now versus pending, no eligible-table count, no metallicity/MZR measurement, single-table scope, or the exact next gate. `Every number read from a recorded artifact` asserts provenance, not scientific authorization, and leaves the earlier scatter/`carrying` implications unrepaired at the final takeaway.

No storyboard production commands were observed verbatim in these encoded frames. The audience-copy problem is instead that exact safe copy is underspecified and internal verification filenames are rendered as citations.

## Pass-3 verdict

`FAIL_FOR_SCIENTIFIC_REPRESENTATION_GRAPHICS_GRAMMAR_TAXONOMY_AND_CLOSURE_BOUNDARY`

The candidate remains preserved and read-only. This verdict does not authorize replacement, rendering, TTS, upload, or publication.

## Safe next correction

Keep the passing v7 static visual unchanged. Version the storyboard proposal so every beat has explicit `on_screen_copy`, and mark `visual_action` plus `verification_sources` as non-audience build/receipt fields. The pass-3 copy must:

1. open with `single-table metadata census` and `metadata-reachable columns`, not catalogues `carrying` measurements;
2. label 178 and 157 as table-level metadata reach/candidates;
3. keep the 178−21=157 and 19/2 accounting visual;
4. show the qualified T2 application/no-count state;
5. close with explicit `REPORTABLE NOW` versus `PENDING`, including no eligible-table count and no metallicity/MZR measurement;
6. forbid internal paths, filenames, and production directions from audience copy.

This is a storyboard audience-copy firewall and implementation clarification, not a new scientific result or encoded candidate.
