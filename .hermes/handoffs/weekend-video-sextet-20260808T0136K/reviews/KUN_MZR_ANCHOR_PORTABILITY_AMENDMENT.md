# MZR-anchor renderer portability amendment

Status: `INTEGRATOR_CLOSURE_PREPARED_FOR_KUN_CONFIRMATION`

Kun's exact-hash review passed the MZR-anchor candidate's audio, synchronization, full decode, independent introduction ASR, motion, and clean deterministic replay. The sole caveat was that the renderer bytes were not yet preserved.

The exact renderer reported by the frozen candidate's build receipt is now archived without changing the candidate:

- candidate SHA-256: `973daba3a6b8ef66409d3bbd2588fc2db2459f4fb3c5d474a731a93b8c2e1970`
- renderer SHA-256: `7d42ea801d6f72648403227728bd771844f3c35ea464bcf99e1eb5dc7d49ca53`
- archived renderer: `integrator/renderer-archive/7d42ea801d6f72648403227728bd771844f3c35ea464bcf99e1eb5dc7d49ca53/render.py`
- archive manifest: `integrator/renderer-archive/7d42ea801d6f72648403227728bd771844f3c35ea464bcf99e1eb5dc7d49ca53/ARCHIVE.json`

Verification performed:

1. The archived source hashes exactly to the renderer hash in `build_receipt.json`.
2. The archived source compiles under the recorded interpreter.
3. Python, platform, Pillow, FFmpeg/libx264, and both font hashes are recorded in the archive manifest.
4. Kun's independent review already records a clean temporary rerender that reproduced the candidate MP4 byte-for-byte using these renderer bytes on the same environment.
5. The frozen candidate tree and MP4 were not modified.

This closes the missing-byte preservation defect mechanically. Final reviewer disposition remains Kun's independent decision. All publication and reporting gates remain closed.
