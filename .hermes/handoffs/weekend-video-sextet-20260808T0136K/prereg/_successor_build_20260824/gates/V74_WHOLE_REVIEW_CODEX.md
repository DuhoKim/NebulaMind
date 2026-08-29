# CODEX — V74 whole-document adversarial review

VERDICT: NOT CLEAR.

The dispatched draft matched the brief's SHA-256 before I read it. V74 repairs several literal V73 failures on the present bytes, but the new 123-field registry still does not cover the operative non-χ artifact corpus, the render-buffer repair makes post-commit rendering internally impossible, the refusal checker still admits an active undeclared code through the deliberately unsplit em-dash case, and the claimed fresh-interpreter and checker-digest bindings are false as written. These are new failures of the V74 repairs, not re-findings of the parked availability-code, object-identity, durable-pre-verdict, strata/producer, VOID-partition, BS-3g-cycle, or draw-discipline questions.

## Findings

### F1 — HIGH / REPAIR-REQUIRED — the 123-field registry omits operative runtime-created non-χ receipt fields

V74 §6.1 lines 586–589 calls the non-χ receipt list exhaustive and admits slot receipts only under authenticated schemas. Lines 663–684 and §11 lines 1414–1420 then claim that `ref/STRING_FIELD_REGISTRY.md` covers every string-bearing field and that `receipt_strict()` plus the verifiers will enforce those value domains. The generated registry does now include all 86 fields declared in frozen v9's `SLOT_SCHEMA`, but that is not the operative receipt schema.

Frozen `ref/successor_ref_v9.py:208–224` creates every canonical receipt envelope at runtime with fields `slot`, `schema`, `environment`, `body_sha256`, and `envelope_sha256`. Its nested environment record at lines 50–57 has `python`, `python_major_minor`, `numpy`, `platform`, `machine`, and `byteorder`. None of `slot`, `schema`, `body_sha256`, `envelope_sha256`, `python`, `platform`, or `machine` appears in the 123-row registry. The generator cannot find them: `ref/gen_string_field_registry.py:32–38` reads only `SLOT_SCHEMA`, while lines 120–134 recognize five phrase-specific draft patterns. The claim that the operative corpus is enumerated therefore mistakes payload-field names for the complete artifact schema.

This omission is exploitable, not cosmetic. In a fresh in-memory import of the exact pinned v9 bytes, I rebound `platform.machine` to return `objid=12345 outcome=+1` and called `receipt("BS-1", ...)` with the exact required BS-1 payload fields. The canonical receipt was accepted and returned an authenticated `environment` containing that arbitrary free-prose value. `receipt()` calls `environment_record()` directly and does not call `require_environment()`; even that guard constrains only three of the six environment keys. Thus a registry-clean slot payload can still emit arbitrary prose through an authenticated non-χ envelope.

The same narrow extractor is already incomplete on the draft's own declared non-slot schemas. §6.1 line 610 says an enumeration entry has “exactly these fields” and ends with the enumerator's signature, while the extractor's regex at lines 128–130 deliberately stops before `· the enumerator`; no signature field is registered. Line 661 also calls the projection bits “e.g.” examples, and the extractor hard-codes only the three current names at line 133. An in-memory mutation adding an explicit fourth backticked projection field, `outcome_hint_pass`, left `extract()` unchanged at 37 draft fields and would leave the generator green.

Required repair: derive the registry from canonical schema objects for the complete receipt envelope, nested environment, every successor slot schema, and every declared non-slot schema; prohibit free-form runtime environment fields or digest-reference a canonical environment body; and canary runtime-created, signature, and newly added projection fields.

### F2 — HIGH / REPAIR-REQUIRED — the V74 render-buffer repair makes render delivery impossible

The lifecycle spec defines delivery as occurring after commit (`LIFECYCLE_GUARANTEE_SPEC.md:18–19`) and explicitly has W3 “after commit, before delivery” and W4 “during delivery” (`:59–68`). A render touch therefore needs committed bytes to survive from the commit into post-commit frame delivery. The spec's actual constraint at lines 116–120 is narrower: render buffers receive no reuse; every render re-conveys under a new commit.

V74's derived construction at draft line 633 first preserves the required ordering: “DELIVERY is a separate act after the touch commit, executed from Row B's committed buffer.” But the same line then says “render buffers do not outlive their commit.” Those statements cannot both hold. At the instant the render commit completes, the latter deletes the only buffer from which the former says the subsequent delivery executes. This is not N1 over-reporting and is not the already-repaired cached re-render case; it prevents the first delivery of the committed render itself.

Concrete crash-window counterexample: a render touch commits, entering spec window W3 before any frame has been delivered. Under V74 the render buffer may not outlive that completed commit, so W4 has no bytes to display. Retaining it long enough to display violates the draft; deleting it obeys the draft but makes G5's render path non-executable.

Required repair: state that the render buffer survives only through that commit's first delivery attempt and is destroyed at delivery completion/request end; forbid reuse for any re-display. “No reuse” is the needed invariant. “Does not outlive the commit” is too strong under a post-commit delivery model.

### F3 — MEDIUM / REPAIR-REQUIRED — fragment scoping still lets one retirement word legalize another active code

V74 claims the retirement exemption is now per sentence fragment, and `tools/refusal_vocabulary_check.py:123–138` implements fragments by splitting only on `.`, `;`, and `:`. The code deliberately does not split on em dash. Within each resulting fragment, however, `RETIREMENT.search(frag)` is still global: it is not bound to the token being exempted.

Against the exact V74 checker I appended only this in memory to its otherwise-clean fixture:

`REFUSED-OLD was deleted — REFUSED-EVADE remains in force.`

`check()` returned `[]` and the process exited 0. The active undeclared `REFUSED-EVADE` shares one em-dash fragment with an unrelated retirement word and is therefore exempted. The new semicolon control at checker lines 267–268 passes precisely because semicolon is a splitter; it does not exercise the punctuation the implementation deliberately leaves unsplit.

Required repair: bind affirmative retirement syntax to each token, preferably permitting it only for a token present in the explicit `RETIRED` map. Fragment-wide retirement state is not token-scoped retirement. Add the em-dash and comma/conjunction mixed-token attacks as controls.

### F4 — MEDIUM / REPAIR-REQUIRED — “fresh interpreter” does not close the pre-import rebinding window

Draft §11 lines 1314–1323 says the replay starts a fresh process that hashes, imports, and computes “with no code running before the import,” and concludes that no rebinding window survives. A fresh ordinary Python process does not have that property. Python imports `site` before executing the verifier script unless launched with `-S`; site processing can import `sitecustomize`/`usercustomize`, and inherited `PYTHONPATH`/import hooks can affect resolution before the verifier hashes or imports v9. On this host, an ordinary `python3 -c` reported `site_preloaded True`, `isolated 0`, and `no_site 0` before user code executed.

The draft names neither `-I -S`, a sanitized environment, a pinned interpreter executable/environment, nor a hermetic import path. Hashing `successor_ref_v9.py` after startup does not authenticate code that already ran and may have modified import machinery or the modules v9 imports. This is exactly the surviving environment window the brief asks the seat to test.

Required repair: specify a hermetic launcher and pin it: isolated/no-site startup (or an equivalent audited bootstrap), sanitized environment, no inherited `PYTHONPATH`/startup hooks, pinned interpreter and dependency bytes, and imports resolved only from pinned locations. Then canary a hostile `sitecustomize`/import-hook environment and require refusal.

### F5 — LOW / REPAIR-REQUIRED — V74's quoted refusal-checker digest is stale

Draft §6.1 line 618 explicitly says `29e85d4a38d89c61…` is the SHA-256 of `tools/refusal_vocabulary_check.py`, recomputed after the last edit in this revision. The current referenced file hashes to:

`1db25971dda678a1f40f80841ecf5591c8e706d07aa53eaf7d4e2238713d5c6e`

The asserted prefix does not match. This is the exact stale-in-the-act-of-repair failure the paragraph says its ordering prevents. The checker is not pinned by that prose, and the historical explanation has become a false current-byte claim.

Required repair: recompute and replace the quoted digest only after the checker reaches final bytes, or remove the mutable hand-copied digest in favor of a generated/pinned manifest entry.

## Failed attacks / repairs that held

- Subject identity held: SHA-256 `d229952d5046e9cc3827e81e371b49ef7bcb887daae22c1cef58208f3b243835` matched before reading.
- Companion identity held: `LIFECYCLE_GUARANTEE_SPEC.md` hashes to `ca24b6dd994a70b8396f58d8370fa4389a05500b2266402b9de8e3bd44ca8fe3`, matching the draft's sole pin.
- The V74 lifecycle helper now enforces full labelled bodies, one pin, and presence of all G1–G6/N1–N3 rows; its nine-control self-test and the exact-byte run were green. F2 is an unlabelled derived contradiction, not a claim that the labelled quotations drifted.
- The missing-companion lint path is now blocking, and the integrated lint ran it. Official lint exited 0 with 16 class-P / 8 class-E rows and 97 legacy advisories, zero blocking. I did not re-report the option-D legacy citations.
- The registry generator now reads frozen v9 `SLOT_SCHEMA` by AST, finds 123 classified rows, blocks stale rows, and exits 0 on current bytes. F1 attacks the omitted runtime/non-slot schema corpus, not those 123 rows.
- Frozen v9 identity held at `6a9abbbd900db882b804149edd6d2b8d1780b7114b191e1a58457d7e5875c148`.
- The raise-site ledger read from the requested `ref/RAISE_SITE_CLASSIFICATION.md` still closes at 112 nodes and 25 CALLER / 60 INTEGRITY / 20 NUMERICAL / 3 PLANNING-INTERNAL / 1 TYPED-OUTCOME / 3 WRAPPER. I did not re-find the parked per-raise/per-call-site defect or the L963/L973/L986 question.
- The eleven intended refusal codes are present on current draft bytes; the baseline checker and its 22-control self-test return clean. F3 is the surviving adversarial mixed-token path.
- Entry↔emission bijection, continuation joins, five verifier consultation gates, and the no-second-EXPLAINED rule are stated. I found no distinct current-byte orphan beyond the unimplemented verifier already disclosed.
- BS-3g remains blocked on unset design values and missing implementation. I did not attack the parked draw discipline, `k_gamma` choice, or within-draw semantics.
- I did not re-derive the parked logged-object membership leak, availability-code semantics, integrity-mismatch collision, durable pre-verdict state, strata/producer issue, VOID/numerical partition, freeze-signature exemption, or BS-3g lifecycle cycle.

## Evidence ledger and scope

Read as content: `gates/BRIEF_V74_REVIEW.md` first; all 1,442 lines of the exact-hash V74 draft; `LIFECYCLE_GUARANTEE_SPEC.md`; `ref/STRING_FIELD_REGISTRY.md`; `ref/gen_string_field_registry.py`; the environment, `SLOT_SCHEMA`, and `receipt()` regions of `ref/successor_ref_v9.py`; `ref/RAISE_SITE_CLASSIFICATION.md`; `tools/refusal_vocabulary_check.py`; `tools/lifecycle_derivation_check.py`; `tools/prereg_lint.py`; and both V73 seat reports to distinguish repairs from re-findings.

Executed: subject/spec/tool SHA-256 checks; official lint; refusal checker and self-test; lifecycle checker through lint; registry regeneration (byte-identical, no git diff); exact v9 runtime-envelope attack; in-memory fourth-projection-field extraction attack; in-memory em-dash retirement attack; ordinary-Python startup-flag inspection; and scoped git status/diff checks. No draft, spec, reference-code, checker, or registry content was changed. The only intended content write is this report.

<!-- FINDINGS-BLOCK v1 -->
SEAT: CODEX
VERSION: V74
VERDICT: NOT CLEAR
COUNT: 5
F1 | HIGH | REPAIR-REQUIRED | §6.1 lines 586–589, 663–684; §11 lines 1414–1420 | The 123-field registry omits runtime receipt-envelope/environment and declared non-slot fields.
F2 | HIGH | REPAIR-REQUIRED | §6.1 line 633; lifecycle spec lines 18–19, 59–68 | A render buffer cannot both die with its commit and deliver only after that commit.
F3 | MEDIUM | REPAIR-REQUIRED | §6.1 lines 591–618; refusal checker lines 121–138 | An em-dash fragment lets one token's retirement exempt another active undeclared code.
F4 | MEDIUM | REPAIR-REQUIRED | §11 lines 1314–1323 | An ordinary fresh interpreter runs site/import machinery before the pinned v9 import.
F5 | LOW | REPAIR-REQUIRED | §6.1 line 618 | The claimed post-edit refusal-checker digest is stale on current bytes.
<!-- END FINDINGS-BLOCK -->