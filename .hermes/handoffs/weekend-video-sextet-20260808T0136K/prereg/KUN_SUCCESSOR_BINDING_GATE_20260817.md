HOLD_IMAGE_METADATA_SCOPE

# KUN SUCCESSOR ROUTE BINDING GATE -- 2026-08-17

**Transcribed from the kun-r2 pane, which did not write a report file.** The brief asked for a
verdict line but did not require a gate report; the fresh lane carried none of the old lane's habit
of writing one. Recorded here so the verdict is not one `tmux kill-session` from being lost.
Brief: `_tmp_kun_successor_binding_gate_brief_20260817.md` (`ef15235391d2eefa`).
Subject: `TORI_ROUTE_BINDING_SUCCESSOR_20260817.md` (`5469197372796bd0`).

## Verdict

HOLD_IMAGE_METADATA_SCOPE
§11 step 4 re-scope is directionally the right custody change: “transfer nothing” cannot survive route B literally, and “no image bytes; paced checksum/metadata retrieval permitted” is the minimum change needed to
fetch and pin survey-published digests before approval.
But the successor is not yet executable as written. It requires pre-approval Content-Length, Last-Modified, and byte total, yet §11.4 only authorizes checksum-file harvest, while §5 re-scopes permission to explicit
full-file GETs. The document does not clearly authorize or receipt the image-URL metadata operation needed to obtain image Content-Length / Last-Modified without moving image bytes, and §5.1’s phrase “source byte size
(from the retrieval-time Content-Length of the checksum harvest phase)” does not work for image files. That must be amended before pass.
Other rulings:
- Predecessor verified byte-unmoved: TORI_ROUTE_BINDING_20260815.md matches c7ed11c12ad7c26d... and is mode 444.
- Sealed-manifest guarantee survives for digests: checksum files are treated as custody inputs and pinned by URL, bytes, digest, and receipt before image bytes move.
- The ~75-hour checksum harvest is a custody event. It is adequately covered if the downloader receipt applies to checksum/metadata harvest as well as image retrieval; the successor mostly says this, but the metadata
gap above needs explicit closure.
- §§6-10 are not substantively amended; they are carried by reference, with only an informational status note.
- Prohibitions are re-scoped, not deleted: recursive retrieval, wildcards, mirroring/crawling, range requests, cutout-service calls, and unmanifested URLs remain forbidden.
- Last-Modified may be retained as weak corroborating evidence because the successor explicitly says digest carries the binding alone. It should not be dropped if it remains labelled this way.
- Pacing asymmetry is correct: later survey/NERSC guidance may tighten without re-gate, never loosen without re-gate.
- R1, R2, R4 are carried; R3 is cited as closed with standing re-verification at manifest time.
- The document plainly states it is a draft proposal, not binding or executable until Kun gates it and Duho accepts/freezes it.
No network, download, checksum harvest, endpoint activation, commit, push, or publication was performed.
─ Worked for 1m 26s ────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────
