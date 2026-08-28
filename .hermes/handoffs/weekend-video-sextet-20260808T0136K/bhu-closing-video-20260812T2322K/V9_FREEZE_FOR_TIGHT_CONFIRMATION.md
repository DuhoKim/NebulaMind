# BHU V9 — tight same-card exact-hash freeze

Status: `FROZEN_V9_AWAITING_TIGHT_THREE_SEAT_EXACT_HASH_CONFIRMATION`

Render authority: **false**. No audio, frames, render, upload, publication, or acceptance is authorised by this freeze. The user will route a tight confirmation to Lana, Goru, and Kun. Only three unconditional verdicts bound to all four exact V9 hashes may clear local rendering. Any `PASS WITH`, conditional, hold, or failure verdict marker blocks; descriptive mention of the already-applied V8 repair does not.

## Exact V9 review targets

- `NARRATION_DRAFT_V9.md`
  - SHA-256 `85f111d366c5d11d912e4f7db5586f10b491b12b1c5091d3f94d822c388190b3`
- `STORYBOARD_DRAFT_V9.json`
  - SHA-256 `c9824b95453be7e67d6066f3810648dc8d588a8c3210546ec9caa5ee74710d7a`
- `CLAIM_LINE_LEDGER_V9.md`
  - SHA-256 `aa4b459a3b4112dc40feabb5e84a0853e205db400d0adfc9d58cab248f6cc9aa`
- `DETERMINISTIC_DIAGRAM_SPEC_V9.md`
  - SHA-256 `e296e2f29a00cf714cbc9f562bb224d224e185fb8d6a5ecb03e718cf5e1cc52e`

All four hashes are mandatory in every verdict. The ledger and diagram spec are byte-identical copies of the fully reviewed V8 targets.

## One canonical content change

Lana's V8 verdict, `LANA_GATE_V8.md` SHA-256 `4240e33df939a5a0b7bd3cadf7ec54ef5efde04b6066717071e29e9e1d67fb35`, directed one repair.

Only `cards[3].narration` changed. Card 04 narration sentence 1 is now, verbatim:

> One proposal — called cosmological natural selection — says universes have children: every black hole buds off a new universe with slightly different physics.

The standalone narration receives exactly the same replacement through `make_v9_one_sentence.py`. Nothing else in the canonical storyboard changed. All headings, timing values, diagrams, printable labels, support strings, claim IDs, packet-line mappings, numbers, dates, and citations remain identical to V8.

The versioned ledger and graphics spec are byte-identical to V8 under the user's change-nothing-else order; their internal V8 H1/status text therefore remains historical scaffolding and is not rendered.

## Provenance and verification

V8 verdict receipts pinned by the V9 generator:

- Lana: `4240e33df939a5a0b7bd3cadf7ec54ef5efde04b6066717071e29e9e1d67fb35` — `PASS WITH ONE REPAIR`.
- Goru: `d3eb719e7176e9c976bba15134ecc293d42157bb0239ff16d4de2b7b6216c805` — `PASS`.
- Kun: `c58c0a70a96f0363cf47f36cff6a5bd0541391bbe3621113b9fa4dd3b1aaaa9a` — `PASS_FOR_RENDER`.

V9 receipts:

- `V9_DELTA_RECEIPT.json` — `6835ef6c48f3b2ca70482ae7b5dee67325089c287f993d99eaa975ce05a8c497`.
- `V9_BUILD_VERIFICATION.json` — `a8776a1b8ba09855d2aa3daa52a7db84ed0e55cd0e3dfb32bc9d69653fc51b6d`.
- `V9_SHORTHAND_AUDIT.json` — `2cd55bd9698ec11ccf002b3e1810ab51408bfdbe18f4bca3fa51314e46931624`.
- `make_v9_one_sentence.py` — `dd4ea8317223592849d4922cbf434c08e0ca98aa8fc3146910b870eb66246a36`.
- `verify_v9_delta.py` — `64fb75aef54e3f6c61995a612155069f2de16d01a0d47a3e784b539e3b3ae14b`.

Verification result: `PASS_V9_ONE_SENTENCE_DELTA_AWAITING_THREE_SEAT_EXACT_HASH_CONFIRMATION`.

## Initialism and shorthand sweep

Scope: title; all 11 headings; all narration; complete diagram and printable-label instructions; all on-screen support. Routing and renderer metadata were classified separately.

Lexical initialisms found:

1. `BHU` — expanded in Card 02 as `black-hole universe, or BHU for short`, in the same breath as its first viewer-facing card use.
2. `CNS` — now expanded in Card 04's first sentence as `cosmological natural selection`, in the same breath as the heading use.
3. `CW/CCW` — expanded in Card 07 as `clockwise- and counterclockwise-spinning galaxy counts`; later Cards 09 and 10 are therefore earned.

Scientific shorthand found:

- Card 04: `~`, `M☉`, and `M ≳ 2 M☉`, spoken on the same card as `about one and a half times the mass of our Sun`, `one point five solar masses`, and `approximately two solar masses or above`.
- Card 05: `±`, `68.3%`, and `95.4%`, spoken on the same card as `give or take`, `sixty-eight point three percent`, and `ninety-five point four percent`.
- Card 07: `≠`, spoken as the two counts `should be different`.

Result: zero unearned **string** defects after Lana's repair. No other lexical initialism or shorthand requiring expansion was found.

Nonviewer classifications:

- `bhu-closing-record` is routing metadata; the local renderer does not consume it, and no upload/publication is authorised.
- `G1` through `G8` are implementation IDs, not printable labels.
- `fps`, `px`, and `WPM` are render-contract metadata, not spoken or printed.

Render-time constraint: because first-card visible diagrams may otherwise precede speech, first-use labels must be staged no earlier than their same-card spoken witness. This applies to the Card 02 BHU label, Card 07 CW/CCW labels and unequal sign, Card 04 mass notation, and Card 05 uncertainty/percentage notation. The Card 04 CNS heading is accepted under Lana's explicit in-breath treatment and remains visible from frame one. Encoded frame/audio QA must prove these reveal conditions.

## Pacing note

Card 04 has 100 words after the five-word repair and retains 41 planned seconds. Static 120–135 WPM arithmetic gives 50.00–44.44 seconds. The prior local renderer derives actual card duration from TTS rather than forcing the planning field; V7 Card 04's 84 words occupied 35.54 seconds of speech. No timing value or wording beyond Lana's exact sentence was changed. The encoded gate must check Card 04 actual cadence and intelligibility.

## Exact tight confirmation required

Each of `LANA_GATE_V9.md`, `GORU_GATE_V9.md`, and `KUN_GATE_V9.md` must:

1. name all four exact V9 hashes above;
2. issue an unconditional current-byte pass;
3. state a standalone unconditional `VERDICT: PASS` or `VERDICT: PASS_FOR_RENDER`, with no `PASS WITH`, `CONDITIONAL`, `HOLD`, or `FAIL` verdict marker;
4. acknowledge that V9's sole canonical content delta is Card 04 sentence 1; and
5. acknowledge the initialism/shorthand audit and render-time reveal constraints.

`preflight_gate_v9.py` must return `PASS_V9_TIGHT_THREE_SEAT_EXACT_HASH_GATE_LOCAL_RENDER_AUTHORIZED` before any audio or frame generation. V8's conditional predecessor and `preflight_gate_v8.py` are superseded for render authority and must not be used.

If cleared, authority is limited to local rendering using no paid generation and no upload. The previous upload is user-declared private and retired; this freeze performs no publication-state mutation.
