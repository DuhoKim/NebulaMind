# C2 V2 — Compile Note (root-local tectonic)

AI_DRAFT_NOT_HUMAN_GOLD

- Engine: `tectonic 0.16.9` (`pdflatex`/`latexmk` absent).
- Command (cwd = this V2 root only): `tectonic candidate.tex --keep-logs`
- Saved return code: **rc = 0** (captured immediately after tectonic, not from a pipe tail).
- Outcome: **SUCCESS — `candidate.pdf` produced** (84,831 bytes; tectonic reported 82.84 KiB). aastex631 + packages fetched successfully.
- Warnings (non-fatal): three cosmetic `Underfull \hbox` (loose-line) warnings, mapped from `compile.log` to the numbered `candidate.tex`:
  - `candidate.tex:34` — "paragraph at lines 33--34" (badness 2368): the paragraph spanning source lines 33–34, i.e. the **Provenance-caveat paragraph** (line 33) up to `\section*{References}` (line 34).
  - `candidate.tex:36` — "paragraph at lines 36--36" (badness 1097 and 1515): the **References entries line** (source line 36). Two warnings.
  - These are line-justification (loose-spacing) artifacts at the exact locations above; no errors, no overfull boxes, no missing font/package. The precise cause (short/loose final-line justification) is **not further adjudicated**.
- Rendering verified via `pdftotext`: all four fixes render in the PDF text layer — F4 not-submitted tag (extracted line 9), F3 abstract scale-limited/TENSION/anchor flag (wraps across extracted lines 12–13), F3 figure-caption note (extracted lines 40–41), F1 softened Result sentence (extracted line 36); the old "provides insights into the relationship" phrase and "reproducible" are absent; the O/H-scale, TENSION, and provenance disclosures remain rendered.
- Logs (root-local): `compile.log` (captured run) and `candidate.log` (TeX engine log).
- Isolation: every write stayed inside this V2 root. The Lab runner was NOT invoked. V1, the source draft, and the source figure were not modified; the local `result.png` is a byte-identical copy of source `gated-e2e-demo/result.png` (`ed83a8250b4a7a2ba969751f3519253f7a2e386080de239bd06e66baa9f82639`).
