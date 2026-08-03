# Lana — C2 V2 Repair — RECEIPT

- Dispatch marker: `OVERNIGHT_PAPER_BOARD_PACKET_C2_LANA_V2_BRIEF_V1`
- Parent approval: `OVERNIGHT_PAPER_BOARD_EXECUTION_APPROVED_20260726T133216Z`
- Implements: `HWAO_C2_REDTEAM_ADJUDICATION_V1` (apply F1–F4; preserve V1). Public status stays `AWAITING_EXPLICIT_PUBLISH_APPROVAL` — NOT a publication step.
- Lane: direct Claude Max subscription only — no API-key, no PAYG, no third-party route, no Nous purchased-balance.
- V2 is a NEW versioned candidate; V1 is frozen and preserved (not replaced). All science artifacts headed `AI_DRAFT_NOT_HUMAN_GOLD`. Isolated; **no publication**.

## Completion state: `DONE`  (V2 built + compiled; V1/source untouched)

## V1 + source untouched (post-build re-verification)
| file | SHA-256 | status |
|---|---|---|
| V1 `c2-mzr-gated-e2e-candidate/candidate.tex` | `c615b2f39502bf4e15f54e8fba3818ca480c9fd162360044c804893a11bc00d9` | FROZEN — unchanged |
| V1 `…/candidate.pdf` | `eed8992dbcfd2a23abc5e459dddbd2660a9add3607e9f34035df9115ac26b98e` | FROZEN — unchanged |
| V1 `…/result.png` | `ed83a8250b4a7a2ba969751f3519253f7a2e386080de239bd06e66baa9f82639` | FROZEN — unchanged |
| source `gated-e2e-demo/draft.tex` | `f1aeadd8ea43f2fd1e22e9686d23066fdf95e3d5c95937a42d8ddd076bc95a8a` | source — unchanged (vs INPUT_SHA256) |
| source `gated-e2e-demo.json` | `46ddd75d5f0e5814e814333336d8e6d1b011382c46509012af2aea8cc20af5e2` | source — unchanged |
| source `gated-e2e-demo/result.png` | `ed83a8250b4a7a2ba969751f3519253f7a2e386080de239bd06e66baa9f82639` | source — unchanged |

## V2 deliverables (new versioned root; SHA-256)
| file | SHA-256 |
|---|---|
| `…/c2-mzr-gated-e2e-candidate-v2/candidate.tex` | `bb77d38d294792f44b05a2011774c6bbb3dbcf0dfc24adf3cb0c5bd5d52e7ee6` |
| `…/c2-mzr-gated-e2e-candidate-v2/result.png` | `ed83a8250b4a7a2ba969751f3519253f7a2e386080de239bd06e66baa9f82639` |
| `…/c2-mzr-gated-e2e-candidate-v2/candidate.pdf` | `ac59ac609bab9c1fdbd74bab27920bdf6de70eac9721a066bdc74dc71384d08d` |
| `…/c2-mzr-gated-e2e-candidate-v2/COMPILE_NOTE.md` | `07456dc5685594211724ef187cd59619d003434f13bfa1a30629d28761f49f9e` |
| `…/c2-mzr-gated-e2e-candidate-v2/V1_TO_V2_DIFF.md` | `7950cbf0c2c79afbb3ef5a6f88f0228a9d895fd01406700193cab3fb4de002da` |
| `…/c2-mzr-gated-e2e-candidate-v2/compile.log` | `85fec63c45f0ac87def0ca04addd6f2927c644d948212ddbe70e2522ad164fec` |
| `…/c2-mzr-gated-e2e-candidate-v2/candidate.log` | `a977d53d5a6ed705ae1066e1d1cfd1adfc1f559d02bcb131df118ab49c7d28e6` |

## Figure byte-identity
V2 `result.png` SHA-256 = `ed83a825…` = source `gated-e2e-demo/result.png` (byte-identical). Source figure read and copied, never modified. Only the LaTeX `\caption{}` text changed (F3); the figure image is untouched.

## F1–F4 fixes applied (rendered; before → after)
1. **F1 (§Result):** "This comparison provides insights into the relationship between galaxy mass and gas-phase metallicity in these two distinct datasets." → "We present the two median relations (TNG100 and SDSS); their direct comparison is bounded by the unresolved O/H-scale systematic (see Caveats) and is not interpreted as physical here." (old phrase absent from V2 PDF)
2. **F2 (§Abstract):** "a bounded, reproducible, descriptive study" → "a bounded, descriptive study" ("reproducible" absent from V2 PDF).
3. **F3 (§Abstract + figure caption):** Abstract gains "This is a scale-limited, TENSION-flagged anchor comparison on un-reconciled O/H scales — see Caveats."; caption "Mass-metallicity relation" → "Mass-metallicity relation. Median relations on un-reconciled O/H scales; the TNG--SDSS comparison is scale-limited (see Caveats)." (caption text only; figure image unchanged).
4. **F4 (§Abstract, first line):** added "AI-assembled draft — not submitted, not peer-reviewed (AI\_DRAFT\_NOT\_HUMAN\_GOLD)."

Full before/after with effects in `V1_TO_V2_DIFF.md`. A V1→V2 `diff -u` shows only these four fixes plus the non-rendered header-comment update. Rendering confirmed via `pdftotext`: F4 (extracted l.9), F3-abstract (l.12–13, wrapped), F3-caption (l.40–41), F1 (l.36) all present.

## Retention confirmed (unchanged / not weakened)
- Source numbers verbatim: TNG100 `23,722`, SDSS `120,000`, `z=0`, SF-weighted gas metallicity → O/H (solar-scaled). No number invented; no O/H offset.
- All 5 references verbatim: Qi2025, Torrey2019, Garcia2023, Guo2016, **LaraLopez2013** (reference block textually identical to source/V1).
- Introduction citation **split** (four single-citation sentences) — unchanged.
- Three caveats retained: **O/H-scale** (bounded "…confounded … cannot be interpreted as physical until a common calibration is established"), **TENSION** (carried, not upgraded), **Provenance** (forced-demo lineage). Original source Caveats paragraph intact. None weakened.
- `AI_DRAFT_NOT_HUMAN_GOLD` header comment + rendered provenance disclosure retained (reinforced by the new F4 visible tag).

## Compile
- `tectonic 0.16.9`, cwd = V2 root, `tectonic candidate.tex --keep-logs`. **Saved rc = 0.** `candidate.pdf` produced (84,831 bytes).
- Warnings: three cosmetic `Underfull \hbox` (loose-line) warnings, mapped from `compile.log` to numbered `candidate.tex` — `candidate.tex:34` (paragraph at source lines 33–34: the Provenance-caveat paragraph up to `\section*{References}`) and `candidate.tex:36` (References entries line, ×2). Line-justification artifacts only; no errors/overfull/missing-package. Precise cause not further adjudicated. Detail in `COMPILE_NOTE.md`.

## STOP conditions
None triggered. No number/claim invented; no edit/overwrite of V1, source, or any current Lab artifact; no source drift vs `INPUT_SHA256.txt`; the compile wrote only inside the V2 root; the Lab runner was not invoked; no payment/overage/top-up/Nous/PAYG prompt; no public or source mutation.

## Constraint attestation
No V1/source/current-Lab edit; no existing PDF replaced; no write outside the V2 root (`c2-mzr-gated-e2e-candidate-v2/`) and this receipt (`reviews/lana/`); no memory/config write; no public/static-root, DB/SQL/API/wiki/page-version write; no deploy/restart; no git/cron/browser/account/billing/cloud action; no Nous purchased-balance or third-party PAYG routing; no publication.

OVERNIGHT_PAPER_BOARD_PACKET_C2_LANA_V2_COMPLETE_V1
