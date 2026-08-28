# Classification-aware provider headline — separately selectable hunk

- Marker: `TORI_PROVIDER_HEADLINE_CLASSIFICATION_AWARE_SELECTABLE_HUNK_20260810T2004K`
- State: `PREPARED_ONLY_NOT_APPLIED`
- Apply authority: **NOT GRANTED**
- Active execution phrase: `NO ACTIVE EXECUTION PHRASE`
- User-acceptance label: **not asserted**

## Selectable patch

Patch:

`/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/weekend-video-sextet-20260808T0136K/TORI_PROVIDER_HEADLINE_CLASSIFICATION_AWARE_SELECTABLE_HUNK_20260810T2004K.patch`

SHA-256:

`e8c6364174fb32c80d3f9f337e40e83270349e269764d7cce52169f027875828`

Size: `3687` bytes.

Preflight:

`git apply --check`: PASS against renderer source SHA-256 `a3855b4dd9ced190dbe8f5af3733b0fb229c222679c046322680d4994c571d28`.

The patch includes both the source hunk and a new focused test. It has not been applied.

## Bound rules already active

The wallet apply bound one-hour card-local freshness rules for:

- Claude / Fable / Lana
- Gemini app / consumer
- Moonshot / Kun (Kimi K3)
- Antigravity / Gemini
- Codex, including its seat-label variant

Each normalized card now carries:

- `freshness_classification`
- `source_observed_at_utc`
- `source_age_seconds`
- `freshness_max_age_seconds`

These fields use the card's own first source timestamp, not the public wrapper timestamp.

## Exact proposed headline behavior

The hunk adds one classification-aware helper and calls it only after card-local freshness has been computed:

1. Preserve an existing explicit `big` value. Moonshot therefore remains `$33.30`.
2. If card-local freshness is `STALE HISTORICAL OBSERVATION`, emit `Stale`.
3. If freshness is `UNAVAILABLE / UNKNOWN`, emit `Unknown`.
4. Only for `FRESH LIVE METER` with a measured provider percent, emit the percent headline.
5. Otherwise leave the headline empty rather than inventing a value.

Expected affected output:

- fresh Claude: measured percentage headline;
- fresh Gemini app: measured percentage headline;
- stale Antigravity: `Stale`;
- stale Codex: `Stale`;
- unknown Codex source timestamp: `Unknown`;
- Moonshot: existing live `$33.30` retained.

## Why this is separate

The five original empty fields had one shared source-path defect, but a blanket `big = percent` fallback would promote old Antigravity/Codex observations under a fresh wrapper. This hunk depends on the independently bound freshness metadata and is therefore separately selectable from wallet canonicalisation.

## Proposed future RED/GREEN gate

Before any apply:

- run the hunk's new focused test as RED against the current renderer;
- require failures only for the missing helper behavior;
- apply exactly this patch;
- rerun wallet, Decision 2, headline, and adjacent provider tests;
- verify current private output shows fresh percent headlines and stale/unknown text without changing Moonshot dollars;
- restart the private renderer only under a new explicit apply decision.

No source or test from this hunk was applied during wallet execution. No provider/browser/public/Git/deploy/cron/config/secret action or user-acceptance assertion is contained in this packet.
