# Lana — V12 full gate: the redesign works; two one-line contract repairs before render

**Lana (science / claim-boundary seat), 2026-08-13.** Full review. Verdict bound to exactly:

- `NARRATION_DRAFT_V12.md` — `178ffe4ada125668c8ff84bc156adee7820954591f9781adb7101aac562d80da`
- `STORYBOARD_DRAFT_V12.json` — `9d55257fe62c7a82d2fe32f424e896ce079393219c08aed6663b6c90c3539399`
- `V12_VISUAL_TEXT_CONTRACT.json` — `c91662e15de095161e84d128683dd69150c8a73b4cbb6f303dda8f79c943999c`
- `V12_SOURCE_FREEZE_RECEIPT.json` — `08898232927ec926b74030fc61113e813b716b9557ab5136d429366ee3c19cf3`

Verified myself, not inherited: all 11 narration payloads word-for-word identical to gated V11 (so
every script certification carries); sync 11/11; planned_seconds exactly my ruling table (402 s);
zero crew terms (and the contract now *forbids* them by rule, including "fable"); the
`deleted_v11_viewer_text` arrays are audit fields, not live text — Hwao's first-pass confusion has
no basis in the artifact; legacy heading/diagram/support fields are gone entirely.

---

## VERDICT: **PASS WITH TWO REPAIRS** — both one-line contract entries, no design or byte-of-script
change. The redesign itself is the best version of this artifact to date.

## 1. The blur test, applied honestly, card by card

Standard: narration off, all text hidden — does the picture deliver `blur_test_expected_claim`?

| Card | Result | Note |
|---|---|---|
| 01 | **PASS** | Fog road closes, gate intact — "closed, not demolished" is *drawn*. The personal-interest boundary is inherently verbal and lives in the badge: **ruling — the safety badge is a designed exception to the blur standard**; it is a safety channel, not a comprehension crutch. |
| 02 | **PASS** | Five unlike icons, arrows ending apart: count and divergence visible without a word. |
| 03 | **PASS — the strongest card in the video.** | The three-beat dartboard (a dart that can miss; no board = nothing to miss; two orbs, one board = can't tell who threw) delivers the spine's both conditions purely by watching. Zero text, and it needs none. |
| 04 | **PASS as scoped** | Sun-icon units are pictograms, so the 1.5-lid vs two-sun-zone *magnitude relation* survives blurring. The consequence's wording is quote-carried — correctly, since a quotation is the one thing a picture must not paraphrase. |
| 05 | **PASS as scoped** | Bars vs the two-sun mark; the widening band's open fade delivers "stricter look → unresolved" visually. The 68.3/95.4 labels are chart data by classification — right call. |
| 06 | **PASS as scoped** | Two roads, a traveller who stops: refusal-to-choose is drawn. The readings' words are quotations on the signpost arms. |
| 07 | **PASS, with a ruling** | Unequal spinning stacks carry "differ"; the gap's "?" carries "no number given." **Ruling — "?" is iconographic, not lexical**: it functions as a pictogram of absence and survives the blur standard's intent. Same ruling covers card 08's four "?" slots. |
| 08 | **PASS** | Order (photos, then bubble) and four empty props read without the year tag. |
| 09 | **PASS** | One footprint, three unlabeled animals, a splitting pointer — underdetermination understood by looking, and the unlabeled silhouettes honour the no-named-rivals boundary better than any labelled diagram we ever had. |
| 10 | **PASS** | The callback locks (blank ruler, footprint) work because the viewer just learned both — the metaphor kit paying rent. |
| 11 | **PASS** | Keys fit, the token doesn't; the final hold is the requirement. |

**11/11 as scoped, with the two rulings recorded above.** Where a blur claim is scoped to what a
picture *can* carry (04, 06), the scoping is honest — quotations are correctly exempted rather than
smuggled into imagery.

## 2. The 54 deletions — safeguard audit (risk 3)

Every deleted string that did epistemic work is accounted for: the claims themselves live in the
**unchanged narration** (word-identical to gated V11) and the subtitle stream now required by the
contract; "NOT ADJUDICATED HERE" became the *stop at the fork* (drawn); "NO AMPLITUDE SHOWN" became
the "?" gap (drawn); the card-05 framing line was double work by Duho's own definition (spoken);
and the "NO 95.4% LOWER-BOUND VALUE…" guard was a guard **for us**, correctly moved off-screen —
but its enforcement half-slipped, which is Repair A. The closed-world contract is the structural
answer to this risk class: no deleted string can silently return, no new string can silently
appear. That invention should persist to every future video.

## 3. The generation boundary (risk 1) and picture-borne claims (risk 2)

The G/D split matches my §5 table exactly where it matters most: **card 04's entire mass gauge and
card 05's entire chart are deterministic**, with generation confined to the star prop and
non-observational atmosphere; the contract carries `generated_text_allowed: false` and
`generated_quantitative_pixels_allowed: false`. No generated asset class risks reading as an
observation as specified (all stylized; card 08's "survey-photo icons" are timeline glyphs, not
data-like frames). Picture-borne claim audit (the ungreppable risk): each `picture` field was read
against the ledger — the fog road *closes but stands* (not "declared false"); the stacks are
unequal *without ratio*; the animals are *unlabeled*; the keys encode the two reopen conditions and
nothing more. **No picture asserts anything the narration does not.**

## 4. The two repairs

- **REPAIR A — restore the enumerated no-terminus prohibition as a contract rule.** V8's diagram
  spec carried the hard list verbatim ("no 95.4% endpoint, arrow, tick, bracket, marker, whisker,
  shaded boundary, axis-aligned glyph, or position-bearing terminus at any scaled mass value; the
  gradient must have no visible lower edge"). V12's file set supersedes that spec, and the rule
  survives only as prose inside card 05's `picture` text plus the general quantitative-pixels flag.
  Three fabrication catches earned that enumeration; it must not decay into paraphrase. One entry in
  `render_contract` (or a `hard_constraints` field on card 05), wording carried verbatim from V8.
- **REPAIR B — pre-authorize the conditional ILLUSTRATION tag inside the closed world.** The
  addendum makes the tag *mandatory* wherever a generated asset could read as "this is what we
  saw." The closed-world text contract — rightly — forbids every unlisted string, which currently
  makes compliance impossible without amendment at QA time. Add one conditionally-permitted role:
  `{"role": "illustration_tag", "text": "ILLUSTRATION", "permitted_when": "QA judges a generated
  asset at risk of being read as an observation"}`. If no asset ever triggers it, it never appears;
  if one does, the safety path exists without breaking the contract.

Neither repair changes a card, a picture, a word of narration, or a timing.

## 5. Pacing confirmed

402 s as ruled; narration fits at the 142 design point inside (planned − dwell) on every card by
construction of the table, with the band (135–150) now in the render contract and the encoded-audio
WPM audit still required; every dwell second maps to a named visual event; **the verdict arrives at
≈ 29 s** — inside the spine with more margin than any prior version.

## 6. Rebind rule

A V13 applying Repairs A and B (two JSON entries, no other bytes) gets a same-day delta check
against fresh hashes; that closes my list for this redesign. No audio, no render, no upload; all
three seats gate; Duho decides on the finished artifact.

— Lana, 2026-08-13.
