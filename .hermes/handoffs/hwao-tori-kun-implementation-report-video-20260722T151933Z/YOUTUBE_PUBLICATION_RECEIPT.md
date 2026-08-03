# YouTube public publication receipt — Hwao + Tori + Kun implementation report

Marker: `HWAO_TORI_KUN_IMPLEMENTATION_REPORT_YOUTUBE_PUBLICATION_VERIFIED_V1`
Verified: `2026-07-22T16:15:11Z`
Status: **PUBLIC · processed · manual captions serving**

## Public video

- URL: https://youtu.be/jn1Bn3_CxfY
- Video ID: `jn1Bn3_CxfY`
- Title: `NebulaMind Implementation Report — Hwao, Tori & Kun`
- Channel: `NebulaMind` (`UCUHBNGk8ozEnisQRuchoS4Q`)
- Privacy: `public`
- Upload status: `processed`
- Processing status: `succeeded`
- Embeddable: `true`
- Made for kids: `false`
- Self-declared made for kids: `false`
- Local duration: `100.000` seconds
- YouTube duration: `PT1M41S` (one-second server rounding from the exact 100-second MP4)
- Source bytes: `5,152,713`
- Source SHA-256: `6c7a6480e10e3a57d074784447f1ca9520dba38599e107f66a7510ec558a3716`

## Manual caption gate

- Language: English
- Name: `English (manual implementation report V2)`
- Track kind: `standard`
- Status: `serving`
- Caption SHA-256: `cedabda88ed7fda469624b51aaa7b979c92d29c7fb94c31b7021c9e684c38e2a`

## Metadata correction

Before publication, the description's stale unlisted-review wording was removed. The public description now explains that:

- public publication was a separate gate at the video's evidence freeze;
- the current user instruction is the later explicit approval of this video-publication gate;
- website embedding, product publication, code landing, deployment, database changes, and other gated work remain unauthorized.

Public metadata SHA-256: `7c1f3d7259fe62ffe0a0d4f2c515154780f389b40041e66f50cc2c8f177d63b6`

## Propagation and verification

One exact-ID snippet/status mutation was issued at `2026-07-22T16:12:45Z`.

- The first immediate owner read still returned `unlisted`, demonstrating expected replica lag.
- Starting at `16:12:51Z`, six consecutive owner reads over 30 seconds returned `public` with exact metadata, processed media, and embeddability intact.
- The authenticated final read still returned `public`, `processed`, `succeeded`, embeddable, and not made for kids.
- Exactly one matching manual English caption track remained `serving`.
- Unauthenticated oEmbed resolved the intended title and `NebulaMind` author.
- A cache-busted signed-out player returned `playability: OK`, exact video ID/title, `isUnlisted: false`, no Unlisted badge, and duration `100` seconds.
- The channel's public RSS feed listed `jn1Bn3_CxfY` first with the exact title, updated public description, and publication timestamp.

A general-purpose text extractor briefly returned the stale unlisted replica after the owner API had settled. No repeat mutation was sent. Cache-busted browser/player metadata and the public RSS listing subsequently confirmed signed-out public convergence.

## Custody artifacts

- Public metadata: `/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/hwao-tori-kun-implementation-report-video-20260722T151933Z/youtube_public_metadata.json`
- Publication preflight: `/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/hwao-tori-kun-implementation-report-video-20260722T151933Z/youtube_publication_preflight.json`
- Publication checkpoint: `/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/hwao-tori-kun-implementation-report-video-20260722T151933Z/youtube_publication_checkpoint.json`
- Machine publication receipt: `/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/hwao-tori-kun-implementation-report-video-20260722T151933Z/youtube_publication_receipt.json`
- Idempotent publisher: `/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/hwao-tori-kun-implementation-report-video-20260722T151933Z/publish_youtube_public.py`

Hashes:

- Publisher: `1d960a1b913a1e0becb66d51e97059f24a0075f331fc87ad346e571622351f50`
- Publication preflight: `e36375953ae62baf3aca1f072dc6b817c520e27219cbcb983ef019e8705e8164`
- Publication checkpoint: `acbd1376be1e1b4d94a541b4c4910fbb22df825de1fc2771213c89d3d4367a44`
- Machine publication receipt: `e97e40f659c76084ce88c3642919104a405c9a2bba0a02f4ee9e6c8e71eed8c3`

## Explicit non-actions

- No older YouTube video was changed, unlisted, or deleted.
- No website, delivery manifest, embed, cockpit, or frontend source was changed.
- No Git commit, push, merge, or history action occurred.
- No build, restart, deploy, database, SQL, or runtime action occurred.
