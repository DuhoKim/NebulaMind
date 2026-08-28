Status: `PRESERVED_POST_ENCODE_QA_HOLD`

Candidate SHA-256: `b5013cd341cab940188db82df0ae57d64f9ec08c0f786a90d6b782bb75599af1`

The renderer correction passed visual preview, but encoded QA measured -22.01 LUFS and held the integrated-loudness gate. True peak was safe at -2.31 dBTP. Root cause: scalar normalization was capped by a transient peak and could not bring programme loudness to target. The exact MP4, build/QA receipts, timeline, master audio, synthesis receipt, and tool provenance are preserved here. The correction path changes assembly to dynamic loudness normalization and requires a new full render; this attempt is never overwritten.
