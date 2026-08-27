# CODEX referee report — proposed replacement §6, third pass

## Verdict

**NOT CLEAR.** The central access finding remains closed at the normative level: clause 1 binds every person and process, the table is the sole pre-unblinding exception surface, and clause 5 preserves conforming table-authorized acts. The R3 author also closes the prior label-receipt, ledger-producer, cutout-checkpoint, and enforceable-mediation findings. Six lifecycle defects remain. Two accepted ceremony findings are only renamed rather than specified or receipted; the acceptance recompute is given byte access to receipts that the draft itself says carry χ; BS-5f crosses the disclosure boundary without being on the sole permitted χ-derived export surface; archive checkpoint equality is undefined; and the void rule stops at BS-L while the access ban continues to unblinding.

## Numbered findings

### 1. BLOCKING — the “canonical opening authorization” still has no canonical body

**Clause / table row at issue.** Rows L and O; clause 3(b)–(d); Part 2 item 6; Part 5 GPT56 item 4. Row L creates a “canonical opening authorization,” and row O requires it and refuses replay. Unlike BS-L, however, no clause defines the bytes or fields of that authorization. Nothing binds it to the BS-L digest, the two store identities, the declared destination, a one-use ceremony identifier, or the intended phase. Part 2 names an “opening authorization verifier” but supplies no contract for what it verifies.

**Why it fails as a promise.** The second-pass finding was not that the authorization lacked a name; it was that an unspecified signed message could be `OPEN`, a reused BS-L signature, or an authorization for another lock or destination. R3 leaves all those implementations conforming. “Canonical” is an adjective here, not an executable serialization, and replay refusal cannot distinguish ceremonies without a bound one-use identifier.

**Smallest sufficient repair.** Define the opening-authorization canonical body and signature envelope with, at minimum, the BS-L digest, both store identities, declared post-unblinding destination, unique one-use ceremony identifier, phase/purpose, signer identity, and schema/version. Make row O’s pinned verifier authenticate those exact fields and make its unblinding receipt carry the authorization digest, verification result, and consumed ceremony identifier.

### 2. BLOCKING — the genuinely final access-log checkpoint is still not a named receipt

**Clause / table row at issue.** Row B; rows L, N, and O; clause 4; Part 5 CODEX item 3. R3 correctly renames the checkpoint bound into BS-L as the **pre-unblinding lock checkpoint**. It then says the chain continues through issuance, opening, and unsealing to a “genuinely final post-unblinding checkpoint.” Row B lists that checkpoint as an emission, but no slot or other authenticated artifact carries it, no producer signs or binds it, no schema is named, and Part 2 adds no later checkpoint field. The phase line’s later named receipts are BS-7f and BS-V, but neither is assigned this checkpoint.

**Why it fails as a promise.** An in-memory or loose log digest is not receipted merely because the table calls it an emission. After BS-L, a chain can omit a required issuance/opening/unsealing event and there is no named later artifact whose verification must fail. The prior chronology self-cycle is repaired, but the promised end-to-end record remains unclosable and unauthenticated.

**Smallest sufficient repair.** Put the final checkpoint in a named post-unblinding artifact—most economically the unblinding receipt or a required field in BS-V—and specify its producer, schema, authentication, and verifier. Require it to extend the checkpoint bound in BS-L and cover the BS-L issuance, opening-authorization consumption, and every unsealing event. Conform row B, row O, §7, `SLOT_SCHEMA`, and the relevant verifier to that one choice.

### 3. BLOCKING — row E’s sign-blind recompute is authorized to read receipts that §6 says contain the sign and amplitude

**Clause / table row at issue.** Scope lines 33–36; row D; row E; current §2.7(3)–(5); Part 2 item 4. The scope defines **every per-object execution receipt** as carrying χ value, sign, amplitude, and confidence. Row D writes those receipts. Row E is then authorized to read “execution receipts” while promising that it “never” reads a χ sign or amplitude. Current §2.7 requires the exclusion path to be unable to read handedness by construction, not merely to ignore a field.

**Why it fails as a promise.** A callable given the receipt bytes has access to the sign and amplitude even if its intended implementation does not inspect the decoded fields. That is not blindness by construction. Because row E computes accepted/excluded status after inference exists, access to those fields restores the exact outcome-dependent selection degree of freedom §2.7 was added to close. The table also makes the read lawful, so the universal ban does not rescue the promise.

**Smallest sufficient repair.** Split D’s output into an outcome-bearing measurement record and a separate authenticated acceptance-evidence projection whose schema contains only the fields needed for §2.7 (attempt identity, expected/actual checksum and shape, execution completion/non-finite status, and the frozen confidence quantity if that quantity is independently shown sign-blind). Authorize row E to read only that projection, not the measurement receipt bytes, and require the BS-2a gate to prove at the interface/schema level that sign, amplitude, and axis-relative position are unavailable.

### 4. BLOCKING — BS-5f is a pre-lock χ-derived export excluded by the disclosure clause’s sole exception

**Clause / table row at issue.** Disclosure lines 22–27; scope lines 39–60; row I; row J; clause 3(b). The disclosure rule says the permitted aggregate surface is the **only** pre-lock χ-derived export and names only BS-2f and BS-8f. Row I produces BS-8f from real labels and instrument outputs. Row J reads those aggregates and emits BS-5f, whose pass/fail and trial result are therefore derivatives of the real calibration aggregates; BS-L must then bind the BS-5f receipt digest outside the sealed stores. Listing BS-5f among nominally non-χ-bearing `SLOT_SCHEMA` receipts does not cure the separate disclosure rule, which says the only χ-derived export is BS-2f/BS-8f.

**Why it fails as a promise.** Literal compliance has no path: either BS-5f leaves the store so BS-L can bind it, violating the “only” export sentence, or it remains sealed and the lock ceremony cannot consume it under its non-χ-bearing receipt surface. More fundamentally, a schema rule that merely forbids per-object payloads does not make a Stage-C result independent of the real χ-derived calibration input.

**Smallest sufficient repair.** Add an explicitly bounded BS-5f Stage-C surface to the permitted χ-derived aggregate/export surface, listing its exact allowed fields and forbidding any additional calibration value, or redefine the disclosure clause so authenticated derivatives of the permitted surface are allowed only through enumerated schemas and enumerate BS-5f. Keep the exception closed and state the lawful BS-5f → BS-L receipt path directly.

### 5. BLOCKING — the archive seal-state checkpoints have no comparison or transition rule

**Clause / table row at issue.** Rows A and Q; clause 3(b)–(c); §6.2; Part 2 items 3 and 6; Part 5 GPT56 item 2. R3 now names the inspector and adds archive fields to BS-2f/BS-L, but it only says the seal state is recorded and re-receipted and that a “broken seal state” is a custody failure. It does not define the authenticated seal-state fields, which prior receipt each checkpoint must match, or what transition/equality predicate distinguishes intact from broken.

**Why it fails as a promise.** Three individually valid metadata receipts can describe three different states and still satisfy every stated schema requirement. `verify_lock()` is told to check the archive seal-state receipt, not to enforce a defined BS-2k → BS-2f → lock invariant. An operator must therefore invent the acceptance rule at execution time, and “broken” remains an unauditable judgment.

**Smallest sufficient repair.** Define the archive seal-state schema and invariant: bind archive identity, seal identifier/version, holder-roster digest, checkpoint predecessor digest, monotonic event/epoch data, and an explicit allowed-transition or exact-equality rule. Make BS-2f compare against BS-2k, make BS-L compare against BS-2f, and require `verify_lock()` to refuse any nonconforming transition.

### 6. BLOCKING — the void consequence ends at the lock although the access ban continues until unblinding

**Clause / table row at issue.** Table preamble; rows K, L, M, and R; clauses 1 and 5; phase line P6 → P7. The universal ban and closed-world default apply until **unblinding**. Clause 5, however, voids only a **pre-lock** out-of-table touch. Rows K, L, and M likewise list only pre-lock access as voiding. Row R says any pre-unblinding access voids, but key holders, Duho, and Hwao are expressly enumerated rows and therefore are not “every other” actor covered by R.

**Why it fails as a promise.** Between BS-L and the P7 unblinding event, a listed key holder, Duho, or Hwao can make a forbidden χ-bearing read without triggering any row’s stated void consequence. The read is prohibited, but the table’s auditable consequence column and clause 5 do not say the run fails. That leaves the central access covenant weaker for the most capable actors during the ceremony window.

**Smallest sufficient repair.** Replace “pre-lock” with “pre-unblinding” in clause 5 and in rows K, L, and M for unauthorized χ-bearing access, while retaining the explicit table-authorized BS-L/opening operations as non-voiding. Audit every other row’s consequence against the same P7 boundary.

## Checks that held

1. **Central access attack failed.** Clauses 1–2 and the table preamble bind every person and process; no named-holder or powerful-role carve-out reappears.
2. **Mandatory-exception attack failed at the role level.** Rows C, D, E, G–J, and P name cutout production, inference, acceptance recompute, committee view/ingestion, calibration, Stage C, and verdict recompute. A conforming within-row act does not void the run.
3. **Label-receipt attack failed.** Row H keeps the explicitly χ-bearing label-set receipt in the committee store and row I is expressly authorized to read it there.
4. **Acceptance-producer attack failed apart from finding 3’s input boundary.** Row E computes statuses from raw evidence and atomically writes the evidence ledger and realised partition; it no longer trusts operator-supplied statuses.
5. **Cutout chronology attack failed.** Row C emits a distinct post-production completion receipt, row D requires it, and BS-2f performs the later cross-check; §2.5’s producer checksum list is source-image-only.
6. **Raw-access detectability attack failed prospectively.** Clause 4 makes enforceable mediation a BS-2k gate condition and says BS-2k is unfillable when that boundary cannot be enforced.
7. **BS-L self-membership attack failed.** BS-L is class E, excludes itself from the frozen class-P manifest, follows BS-5f, and uses a detached signature over a canonical body.
8. **Freeze-binding attack failed.** The BS-L body now binds the ordered class-P receipt manifest, gate reports, and freeze signature, and `verify_lock()` is required to check the bound bytes rather than mutable filenames.
9. **Post-unblinding table-boundary attack failed.** The closed-world default is explicitly pre-unblinding and row S separately authorizes disclosure after BS-V.

## Mechanical check

I ran `python3 /Users/duhokim/NebulaMind/NebulaMind/tools/prereg_lint.py <current V15 draft> --gates <gates>`. It reported 20 §7 rows (14 class P, 6 class E) and `no inconsistencies found`. There is still no integrated candidate containing Part 1 plus Part 2’s prose, §7, schema, and code edits, so that clean result applies only to the current document and does not test R3. The linter does not check opening-authorization fields, checkpoint receipt closure, field-level information flow, χ-derived export closure, archive transition invariants, or lock-versus-unblinding void boundaries.

## Testimony

I did not inspect any image, χ value, sealed store, archive payload, key, credential, access log, or `/Users/duhokim/NebulaMindData/`. I did not establish historical outcome-blindness, predecessor archive custody, absence of prior access, or the existence/behavior of any future mediator, opening verifier, unsealing service, acceptance projection, archive checker, or integrated R3 code. I reviewed the R3 brief and draft, both R2 referee reports, the current V15 preregistration, `tools/prereg_lint.py`, and the relevant v9 `SLOT_SCHEMA`; I ran only the current-document lint and modified only this report.

**NOT CLEAR**