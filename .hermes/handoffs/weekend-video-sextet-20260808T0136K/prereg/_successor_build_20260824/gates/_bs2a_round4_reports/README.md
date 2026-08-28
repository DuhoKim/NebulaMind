# BS-2a round 4 — reports

- `BS2A_CODE_GATE_CODEX.md` — CODEX, **NOT CLEAR**. One HIGH finding: malformed top-level
  `receipt`/`evidence` containers crash instead of refusing, via JSON-native input. Everything else
  verified fixed, including all 276 pairwise deletion probes and the three round-3 repairs.
- **GPT56 was still running when round 5 was dispatched at the principal's instruction.** Its
  round-4 review is therefore of superseded bytes (`e9d2ce3b…`). If `BS2A_CODE_GATE_GPT56.md`
  appears with a round-4 heading, read it against `e9d2ce3b…`, not against the current file.
  From round 5 onward report filenames carry a `_R<N>` suffix so rounds cannot overwrite each other.
- GPT56's round-3 pair battery completed after its seat died: `276 pairs tested, silent
  (undetected) pairs: NONE` — independently corroborating CODEX's own 276/276.
