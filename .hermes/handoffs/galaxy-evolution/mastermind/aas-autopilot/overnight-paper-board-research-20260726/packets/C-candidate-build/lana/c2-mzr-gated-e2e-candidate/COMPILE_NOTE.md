# C2 — Compile Note (root-local tectonic)

AI_DRAFT_NOT_HUMAN_GOLD

- Engine: `tectonic 0.16.9` (`/opt/homebrew/bin/tectonic`). `pdflatex` / `latexmk` are absent (expected).
- Command (run with cwd = this C2 root only): `tectonic candidate.tex --keep-logs`
- Saved return code: **rc = 0** (captured immediately after tectonic, not from a pipe tail).
- Outcome: **SUCCESS — `candidate.pdf` produced** (82,670 bytes on disk; tectonic reported 80.73 KiB). tectonic fetched the `aastex631` class and required packages from its bundle successfully.
- Warnings (non-fatal, cosmetic): only `Underfull \hbox (badness …)` at lines 28–29 and 31 — the References block, whose long bibcodes and the verbatim string `0.5 <= z <= 0.7` do not fill the justified column. These are line-justification warnings, not errors, and are inherited from the source reference strings, which were reproduced verbatim (no source text altered to suppress them). No overfull boxes, no missing-font or missing-package errors, no fatal TeX errors.
- Logs (both root-local in this folder): `compile.log` (captured stdout+stderr of the run) and `candidate.log` (full TeX engine log via `--keep-logs`).
- Isolation: every write stayed inside this C2 root. The Lab runner was NOT invoked. The source figure and source draft were not modified; the local `result.png` is a byte-identical copy of `gated-e2e-demo/result.png` (SHA-256 `ed83a8250b4a7a2ba969751f3519253f7a2e386080de239bd06e66baa9f82639`).
- Per brief: a failed fetch/compile would NOT have been a failure state (deliver `.tex` + this note); here the compile succeeded and `candidate.pdf` is included.
