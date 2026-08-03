# Tori P2 specification review — input-hash correction required

The 73-entry classification, lane arithmetic, verbatim fields, zero-lane handling, and deterministic crosswalk are otherwise consistent.

One custody defect remains:

- `triage/TRIAGE_LEDGER.json.goru_input` names `triage/GORU_MANUAL_QUEUE_TABLE.json`, but `goru_input_sha256` contains the upstream validator-result hash `ad4d035b…3d52` rather than the named Goru JSON file's sha256 `ae5aac74ff85f6ba66652dd4e4f023dc435740e4b19713753ac94f380d95ad06`.
- `triage/TRIAGE_LEDGER.md:4` repeats the same incorrect association.

Required correction: replace the Goru-input hash in both ledger files with `ae5aac74ff85f6ba66652dd4e4f023dc435740e4b19713753ac94f380d95ad06`. Preserve the validator-result hash separately only if it is clearly labeled as the upstream validator-result hash. Do not alter entries, lane assignments, reasons, arithmetic, zero-lane statements, or markers.

TORI_P2_INPUT_HASH_CORRECTION_REQUIRED_20260713T024458Z
