#!/usr/bin/env python3
"""STRING-FIELD REGISTRY — enumerated from the schema blocks, because the universal sentence died.

V72 asserted: every string field in every non-chi artifact is closed-vocab or bounded - "no third
kind". The corpus already contained counterexamples (CODEX-V72 F2: slot-receipt schemas constrain
names, not value domains; GPT56-V72 F3: explanation_ref itself was unbounded). A universal sentence
written in one sitting is the anywhere/never defect; the fix is the VOID-registry fix - ENUMERATE.

This generator extracts every field token from the draft's declared schema blocks, so it cannot
silently omit a field the way a keyword filter omitted Row F. Classification is human and lives in
CONSTRAINTS below; a field the extractor finds with no row is FORBIDDEN-BY-DEFAULT and this exits
nonzero, which blocks the battery rather than shipping an omission. (And the first version of
this extractor proved the point against itself: its token pattern [a-z_]+ silently dropped every
field containing a digit - all seven sha256 fields - which is Row F's keyword omission, committed
by the tool built to prevent it. The stale-row report is what caught it.)
"""
import re
import sys
from pathlib import Path

B = Path(__file__).resolve().parent.parent
V9 = Path(__file__).resolve().parent / "successor_ref_v9.py"
DRAFTS = sorted(B.glob("PREREG_SUCCESSOR_DRAFT_V*.md"),
                key=lambda p: int(re.search(r"_V(\d+)_", p.name).group(1)))
# CODEX-V84 F3: newest-by-default made older drafts unregeneratable once a successor existed;
# an explicit path argument selects the draft, newest is only the default.
DRAFT = Path(sys.argv[1]) if len(sys.argv) > 1 else DRAFTS[-1]

# v9's operative SLOT_SCHEMA (CODEX-V73 F1, GPT56-V73 F2: the registry claimed every non-chi
# artifact and enumerated only the draft-declared schemas, omitting all fields of the EXISTING slot
# receipts - the exact universal-sentence defect the registry replaced, one enumeration down).
# Extraction is mechanical over the frozen file; classification is human, below, keyed "SLOT.field".
import ast
def v9_slot_fields():
    tree = ast.parse(V9.read_text())
    for node in ast.walk(tree):
        if isinstance(node, ast.Assign) and getattr(node.targets[0], "id", "") == "SLOT_SCHEMA":
            d = ast.literal_eval(node.value)
            return {f"{slot}.{f}" for slot, fs in d.items() for f in fs}
    raise SystemExit("SLOT_SCHEMA not found in v9 - the extractor is broken, refuse to emit")

V9_CONSTRAINTS = {}
def _c(slots_fields, constraint, note="", source="v9 SLOT_SCHEMA"):
    # source defaults to the slot schema; declared sets that do NOT come from v9 MUST say
    # where they come from - the arrival rows shipped labelled "v9 SLOT_SCHEMA" although
    # frozen v9 has no arrival schema (CODEX-V88 F1): a wrong source is a wrong authority.
    for sf in slots_fields.split():
        V9_CONSTRAINTS[sf] = (constraint, source, note)
# digests and hashes
_c("BS-2m.parent_digest BS-2m.planner_digest BS-2m.plan_digest BS-2f.mask_digest BS-5f.mask_digest "
   "BS-7f.mask_digest BS-V.mask_digest BS-7f.perm_payload_digest BS-1.config_digest BS-4.anchor_digest "
   "BS-3.weights_sha256 BS-7p.ref_code_sha256 BS-7p.fixtures_sha256 BS-9.input_function_sha256 "
   "BS-6.manifest_sha256", "digest-ref")
# numeric / array payloads (bounded by dtype+shape contracts in v9's field encoders)
_c("BS-2c.universe_brickid BS-2c.brickid BS-2c.n_eligible BS-2c.c_bytes BS-2c.grouped_sum "
   "BS-2c.ungrouped_total BS-2o.order_brickid BS-2o.N BS-2o.Var BS-2o.L_raw BS-5p.l_min_plan "
   "BS-5p.l_plan BS-5p.successes BS-5p.n_trials BS-2s.selected_brickid BS-2s.L_ret BS-2s.L_raw "
   "BS-2s.N_ret BS-2s.N_eq BS-2s.repass_successes BS-2m.required_count BS-2m.manifest_count "
   "BS-2f.brickid BS-2f.objid BS-2f.c BS-2f.bin BS-2f.boundaries BS-8f.a_hat BS-8f.sigma_a "
   "BS-8f.a_lb BS-8f.a_b BS-8f.sigma_ab BS-8f.a_lb_b BS-8f.cov_a BS-8f.epsilon BS-5f.successes "
   "BS-5f.n_trials BS-7f.beta_obs BS-7f.p BS-7f.n_perm BS-V.A_L BS-V.p BS-V.sigma_comb "
   "BS-V.evaluated_floor BS-7p.n_perm BS-8p.budget BS-6.byte_ceiling BS-3.tau",
   "bounded-encoding")
# closed token sets
_c("BS-2f.accept_flag BS-5f.passed BS-V.verdict BS-V.path BS-1.branch BS-1.photoz_available "
   "BS-4.sign_convention BS-4.verdict", "closed-vocab")
# STRUCTURED payloads - the rows CODEX/GPT56 called out; constrained by named sub-schemas, and any
# without one is the finding standing until its verifier lands
_c("BS-1.resolution_date", "bounded-encoding", "ISO date")
_c("BS-1b.photoz_product BS-1b.columns BS-1b.join_keys", "closed-vocab", "declared column/key sets")
_c("BS-1b.provenance", "digest-ref",
   "digest of canonical.provenance_record - WHOSE ENCODING IS PENDING; this field is unfillable "
   "until that schema is written, which the pending row states")
_c("BS-3.antisymmetry_receipt BS-9.hdu_schema BS-9.tensor_layout BS-9.r1_r5_receipt "
   "BS-8p.allocation BS-8p.bin_algorithm", "digest-ref", "canonical sub-document, digest-referenced")
_c("BS-8p.hc_rules_quotation", "digest-ref", "the HC-1H quotation-at-freeze, by digest")
# Declared CANONICAL BODIES the extraction missed (CODEX-V76 F1): each is a canonical field-order
# encoding with its own verifier, digest-referenced wherever it appears.
_c("canonical.freeze_signature_body canonical.lock_body canonical.opening_authorization "
   "canonical.entry_body canonical.explanation_body",
   "digest-ref", "field-order encoding WRITTEN in this draft; detached signatures bind these digests")
# The canonical-body LEAVES (GPT56-V79 F4, CODEX-V79 F4: string leaves were hiding behind
# digest-ref containers, the CODEX-V78 F2 defect one level up). Opening authorization = Clause 6's
# eight fields; freeze body = its five declared components. Lock and entry bodies' leaves are
# already enumerated elsewhere in this registry (entry.* rows; the lock body's components are the
# BS-L clause's, digest+identity fields).
_c("openauth.bsl_digest openauth.ceremony_id openauth.signer_identity", "digest-ref",
   "ceremony_id one-use, signer bound to the BS-2k public key")
_c("openauth.store_identity_main openauth.store_identity_committee openauth.destination "
   "openauth.phase", "closed-vocab", "store roster / declared destinations / the literal P7")
_c("openauth.schema_version", "closed-vocab",
   "the literal schema/version Clause 6 binds - V80 substituted timestamp for this field TWICE, in "
   "the withdrawal that claimed to fix the first substitution (GPT56-V80 F1, CODEX-V80 F3)")
_c("freezebody.code_digest freezebody.parent_sha256 freezebody.draft_sha256", "digest-ref")
_c("freezebody.selection_bricks freezebody.class_counts", "bounded-encoding",
   "decimal ints; class counts as the counts tool emits them")
# CODEX-V82 F5: lock-body leaves and opening-authorization value domains. The lock body's leaves
# are the digests clause 3(a) binds - enumerated THERE, each a digest-ref; the registry carries the
# container plus this pointer rather than inventing a second enumeration (the provenance-record
# lesson). Openauth's closed sets (store identities, destinations) are BS-2k design artifacts -
# closed by construction where the roster and destination list are declared.
# GPT56/CODEX-V83 F6: the V82 pointer said clause 3(a), which contains NO enumeration - the
# unverified-pointer defect inside the row written as that lesson. The lock body lives in 3(b),
# read this time, and its leaves are enumerated AND cross-checked against the clause text below.
_c("lockbody.roster_digest lockbody.accepted_mask_digest lockbody.calibration_record_digest "
   "lockbody.stagec_receipt_digest lockbody.decision_input_digests lockbody.classp_receipt_manifest "
   "lockbody.gate_reports lockbody.freeze_signature lockbody.lock_checkpoint "
   "lockbody.chain_segment lockbody.archive_seal_state lockbody.environment_record "
   "lockbody.signer_identity",
   "digest-ref", "clause 3(b)'s canonical order; cross-checked against the clause text at generation")
_c("canonical.provenance_record", "SCHEMA-PENDING",
   "V77 force-added this as digest-ref with no written encoding (GPT56-V77 F3, CODEX-V77 F1) - the "
   "SCHEMA-PENDING defect wearing a canonical name; pending until its encoding is written")
_c("BS-9.runner_prohibition", "closed-vocab", "declared clause set")
_c("BS-7p.environment", "digest-ref",
   "canonical sub-schema below - V77 called this closed-vocab after defining it as a sub-schema, "
   "a false label one revision old (CODEX-V77 F2)")
_c("bs7p_env.interpreter_path", "bounded-encoding",
   "absolute POSIX path, printable ASCII <= 256 bytes, no traversal segments")
_c("bs7p_env.interpreter_sha256 bs7p_env.dependency_roots bs7p_env.dynamic_load_manifest",
   "digest-ref", "roots and linker-resolution manifest as ordered (path, digest) pairs")
# CODEX-V78 F2: the CONTAINERS were digest-refs while their per-entry path strings had no bound and
# no registry presence - unbounded leaves hiding behind a bounded wrapper. The entry fields:
_c("roots_entry.path dlm_entry.path", "bounded-encoding",
   "absolute POSIX path, printable ASCII <= 256 bytes, no traversal segments - same bound as the "
   "interpreter path; the containers enumerate exactly these entries")
_c("roots_entry.digest dlm_entry.digest", "digest-ref")
# GPT56-V78 F2: explanation parameter NAMES and arity were free strings - the string rule's own
# surface, one level down. Each cause declares its exact parameters; nothing else is admissible.
# GPT56-V82 F2: "bounded-encoding" with no ranges was the V76 environment-leaf defect on the
# parameter surface. The ranges:
_c("param.duration_ms", "bounded-encoding", "decimal int [0, 2^31)")
_c("param.attempt_count", "bounded-encoding", "decimal int [0, 10^4]")
_c("param.signal_number", "bounded-encoding", "decimal int [1, 64]")
_c("param.lease_id_digest", "digest-ref", "64 lowercase hex")
_c("param.store_errno", "bounded-encoding", "decimal int [0, 2^15)")
# per-cause arity unchanged: VERIFIER-TIMEOUT(duration_ms) - WORKER-CRASH(signal_number) -
# DEADLOCK(duration_ms, attempt_count) - LEASE-LOST(lease_id_digest) - STORE-UNAVAILABLE(store_errno)
_c("BS-6.producer_checksum_list", "digest-ref")
# The runtime receipt ENVELOPE and ENVIRONMENT (CODEX-V74 F1: v9's receipt() wraps every slot body
# in envelope fields, and environment_record() emits its own - all string-bearing, none previously
# enumerated), extracted below from the envelope constructor rather than hand-listed.
# The ARRIVAL event class - source: the draft's exhaustive non-chi list item (ii-b), where the
# schema now lives (CODEX-V88 F1: these rows shipped sourced to v9 SLOT_SCHEMA, which never
# contained an arrival - the registry cannot widen the draft's list, only mirror it).
# (SWEEP: GPT56/CODEX-V87 F2 - the ruled second event class escaped the
# exhaustive registry). request_key = the arrival event's own CHAIN POSITION: bounded decimal,
# unique by chain construction, restart-safe because there is one chain - no new randomness.
_c("arrival.kind", "closed-vocab", "the literal ARRIVAL",
   source="draft 6.1 item (ii-b) - ARRIVAL event schema")
_c("arrival.timestamp", "bounded-encoding", "ISO-8601 UTC, 24 bytes",
   source="draft 6.1 item (ii-b) - ARRIVAL event schema")
_c("arrival.row arrival.operation", "closed-vocab", "the event schema's own closed sets",
   source="draft 6.1 item (ii-b) - ARRIVAL event schema")
_c("arrival.object_identity", "bounded-encoding", "brickid/objid keys",
   source="draft 6.1 item (ii-b) - ARRIVAL event schema")
_c("arrival.request_key", "bounded-encoding",
   "the arrival's own chain position, decimal - unique by construction, restart-safe; the "
   "enumeration verifier checks the join BIDIRECTIONALLY: every arrival at most one terminal "
   "naming it, every terminal exactly one prior arrival",
   source="draft 6.1 item (ii-b) - ARRIVAL event schema")
_c("arrival.running_chain_digest", "digest-ref",
   source="draft 6.1 item (ii-b) - ARRIVAL event schema")
_c("arrival.boot_epoch arrival.monotonic_reading", "bounded-encoding",
   "the authenticated clock pair: boot_epoch = the BS-2k restart counter, decimal integer in "
   "[0, 10^6]; monotonic_reading = decimal integer nanoseconds in [0, 2^63-1] (GPT56-V90 F3: "
   "bounds stated); overdue is computed from these bytes under spec-3b's chain-order "
   "monotonicity invariants, never from a clock read at verification",
   source="draft 6.1 item (ii-b) - ARRIVAL event schema")
_c("haltrec.kind", "closed-vocab", "the literal TERMINATED-BY-LABEL-EXHAUSTION",
   source="spec 5 - exhaustion halt receipt (CODEX-V94 F4)")
_c("haltrec.chain_head", "bounded-encoding",
   "position + running digest at halt; identities are SEALED committee-side, not here "
   "(GPT56-V94 F7)", source="spec 5 - exhaustion halt receipt")
_c("bindmap.request_key bindmap.decision_chain_position", "bounded-encoding",
   "chain positions, bounded decimal - the join is (request_key <-> decision position)",
   source="draft 6.1 item (iv-c) - binding-to-key map")
_c("bindmap.decision_event_digest", "digest-ref", "",
   source="draft 6.1 item (iv-c) - binding-to-key map")
_c("bindmap.decision_boot_epoch bindmap.decision_monotonic_reading", "bounded-encoding",
   "the decision's clock pair, same bounds as the arrival's - the decide-within-D evidence; "
   "WIDENED at V93 (CODEX-V92 F1), FILED with the coordinator",
   source="draft 6.1 item (iv-c) - binding-to-key map")
_c("bindmap.signature", "bounded-encoding",
   "detached deterministic signature over the canonical entry body, 64 bytes - Row B's "
   "provisioned keypair, signer roster-bound, no envelope leaves (CODEX-V91 F3: sig-envelope "
   "was off-enum and invited undeclared leaves)",
   source="draft 6.1 item (iv-c) - binding-to-key map")
_c("ckclock.predecessor_epoch", "bounded-encoding",
   "the previous opening's epoch, decimal [0, 10^6]; NONE for the anchored first epoch "
   "(GPT56-V93 F1)", source="draft 6.1 item (ii-c) + spec 3b - opening record")
_c("ckclock.gap_declaration", "bounded-encoding",
   "ascending declared-skipped epochs, each decimal [0, 10^6]; emptiness proven by chain "
   "continuity, not trusted (GPT56-V93 F2)",
   source="draft 6.1 item (ii-c) + spec 3b - opening record")
_c("ckclock.boot_epoch ckclock.monotonic_reading", "bounded-encoding",
   "the checkpoint CLOCK RECORD of its own production - same bounds as the arrival pair "
   "(epoch [0, 10^6], reading ns [0, 2^63-1], GPT56-V90 F3) - the other side of the spec-3b "
   "comparison rule",
   source="draft 6.1 item (ii-c) + spec 3b - checkpoint clock record")
_c("envelope.slot", "closed-vocab", "SLOT_SCHEMA keys")
_c("envelope.schema", "closed-vocab", "the literal successor_ref_v3/1")
# The environment's SIX LEAF FIELDS, extracted from environment_record() itself rather than
# collapsed into one container row (GPT56-V75 F1, CODEX-V75 F2: "platform" is arbitrary interpreter
# text, and one falsely-closed row hid six open ones). The honest constraints differ per leaf:
# three are PINNED by require_environment (deviation refuses - a genuinely closed vocabulary of one
# value each); three are RECORDED-UNPINNED - carried in the envelope, checked by nothing, and
# therefore bounded only by their encodings. Saying which is which is the repair.
_c("envelope.environment", "digest-ref",
   "the container: canonical JSON of the six leaves below, digested into the envelope")
_c("environment.python_major_minor environment.numpy environment.byteorder",
   "closed-vocab", "pinned by require_environment - one frozen value each, deviation refuses")
# GPT56-V76 F1 / CODEX-V76 F2: "bounded-encoding" with no declared bound was a contradiction
# inside one row. The bound now EXISTS and is enforced at the successor layer: the envelope
# verifier refuses any of these three exceeding 64 bytes or leaving printable ASCII. Unpinned in
# VALUE (any interpreter string within the bound passes), bounded in ENCODING (the constraint
# column's actual claim) - both halves now true.
_c("environment.python environment.platform environment.machine",
   "bounded-encoding", "printable ASCII <= 64 bytes, refused by the envelope verifier "
   "(successor layer); value unpinned - any conforming interpreter string passes")
_c("envelope.body_sha256 envelope.envelope_sha256", "digest-ref")
# The enumerator SIGNATURE itself (GPT56-V74 F1: a valid signature still has degrees of freedom -
# an ECDSA nonce is a covert channel wearing a validity proof). Constraint: the BS-2k keypair spec
# MUST mandate a DETERMINISTIC scheme (Ed25519/RFC-6979), making the bytes a function of key+body
# with no channel left.
_c("entry.signature", "bounded-encoding", "deterministic scheme mandated at BS-2k - no nonce channel")
# The ACTUAL signature fields (GPT56-V81 F5: the registry inventoried canonical BODIES and omitted
# the detached signatures over them). Deterministic scheme, fixed 64-byte encoding.
_c("sig.freeze sig.bsl_lock sig.opening sig.explanation sig.checkpoint",
   "bounded-encoding", "detached deterministic signature over the named canonical body, 64 bytes")
# The nine declared NON-SLOT artifact classes - HONEST STUBS, not pseudo-fields (GPT56-V75 F2,
# CODEX-V75 F1: a class name in a field column was classification theatre). Three classes are
# ALREADY inventoried field-by-field in this registry: the access-log chain (the event.* rows), the
# enumeration surface (entry.* + cause), and the acceptance-evidence projection (its three predicate
# bits). The remaining six have NO per-class field schema yet - each is SCHEMA-PENDING, its fields
# unenumerable until the slot that defines it is filled, and its row says so instead of wearing a
# constraint it does not have. A SCHEMA-PENDING class cannot carry data: its producer is blocked by
# the same unfilled slot.
_c("nonslot.access_log_chain", "closed-vocab", "inventoried: the event.* rows above AND the arrival.* rows - the chain carries both event classes (CODEX-V88 F1)")
_c("nonslot.enumeration_surface", "closed-vocab", "inventoried: entry.* rows + explanation cause")
_c("nonslot.acceptance_evidence_projection", "closed-vocab", "inventoried: three predicate bits")
_c("nonslot.cutout_completion_receipt nonslot.stage_completion_artifact nonslot.label_set_receipt "
   "nonslot.unblinding_receipt nonslot.adequacy_receipt nonslot.archive_seal_state_receipt "
   "nonslot.lock_checkpoint_receipt",
   "SCHEMA-PENDING", "fields unenumerable until the defining slot fills; producer blocked by the "
   "same slot - a stub saying so, not a constraint it does not have")

# (field, constraint, declared-where, note). Constraints: closed-vocab | bounded-encoding | digest-ref
CONSTRAINTS = {
    # BS-3g slot receipt (§11)
    "mask_sha256": ("digest-ref", "§11 BS-3g", "must equal BS-2f's pinned mask_digest"),
    "calibration_sha256": ("digest-ref", "§11 BS-3g", ""),
    "perturbation_manifest_sha256": ("digest-ref", "§11 BS-3g", ""),
    "kernel_sha256": ("digest-ref", "§11 BS-3g", ""),
    "estimator_sha256": ("digest-ref", "§11 BS-3g", ""),
    "verifier_sha256": ("digest-ref", "§11 BS-3g", ""),
    "counterfactual_path_sha256": ("digest-ref", "§11 BS-3g", "compiled from verified buffer"),
    "replay_harness_sha256": ("digest-ref", "§11 BS-3g", "the harness carrying every replay obligation (CODEX-V81 F1)"),
    "mapping_id": ("closed-vocab", "§11 BS-3g", "sole member MAPPING-NOT-PREREGISTERED until ruled"),
    "gamma_hat": ("bounded-encoding", "§11 BS-3g", "finite IEEE-754 double, decimal"),
    "sigma_gamma": ("bounded-encoding", "§11 BS-3g", "finite IEEE-754 double, decimal"),
    "gamma_bound": ("bounded-encoding", "§11 BS-3g", "RULED a-priori (2026-08-30): equals the ratified frozen endpoint; k-gamma moot; the old recomputed-formula note encoded the superseded shape (SWEEP: GPT56/CODEX-V87 F6)"),
    "invariance_outcome": ("closed-vocab", "§11 BS-3g", "HELD | FAILED"),
    "n_perturbations": ("bounded-encoding", "§11 BS-3g", "decimal int [1,10^6]"),
    "n_draws": ("bounded-encoding", "§11 BS-3g", "decimal int; RULED = 99 (2026-08-30 sitting)"),
    "draw_generator_id": ("closed-vocab", "§11 BS-3g", "one member, committed blind: numpy-1.26.4-PCG64-default_rng"),
    "draw_master_seed": ("bounded-encoding", "§11 BS-3g", "decimal int; COMMITTED blind = 20260830"),
    "draw_verdict_digest": ("digest-ref", "§11 BS-3g", "row-major serialization stated"),
    "baseline_verdict": ("closed-vocab", "§11 BS-3g", "a PRODUCTION verdict token - REPRODUCED-LONGO / REJECTED-AT-LONGO-AMPLITUDE / INCONCLUSIVE - or PER-DRAW; V84 wrongly closed it to the invariance tokens (GPT56-V84 F4, CODEX-V84 F5): cells carry run verdicts"),
    "delta_gamma_max": ("bounded-encoding", "§11 BS-3g", "canonical decimal string per the "
        "one §11 grammar (no exponent, no trailing zeros, canonical zero 0) - DERIVED = "
        "2*Gamma/n_steps under AMENDMENT 2 (GPT56-V91 F4: this row said finite positive "
        "double after the grid went exact-decimal)"),
    # access-log event (§6.1 (ii))
    "timestamp": ("bounded-encoding", "§6.1 event schema", "ISO-8601 UTC YYYY-MM-DDThh:mm:ss.sssZ, exactly 24 bytes (GPT56-V77 F4: labelled bounded with no bound)"),
    "actor": ("closed-vocab", "§6.1 event schema", "row identifiers"),
    "table row": ("closed-vocab", "§6.1 event schema", ""),
    "operation": ("closed-vocab", "§6.1 event schema", "BS-2k closed operation set, STORE-QUALIFIED: (row, operation) determines the store (GPT56-V81 F4, CODEX-V81 F5 - Row I touches multiple stores, so unqualified operations made the presence-audit join non-derivable)"),
    "object identity": ("bounded-encoding", "§6.1 event schema", "brickid/objid keys"),
    "success/refusal": ("closed-vocab", "§6.1 event schema", ""),
    "refusal reason": ("closed-vocab", "§6.1 event schema", "the eleven codes"),
    "running chain digest": ("digest-ref", "§6.1 event schema", ""),
    # enumeration entry (§6.1)
    "chain_position": ("bounded-encoding", "§6.1 entry", "index into the chain"),
    "event_digest": ("digest-ref", "§6.1 entry", ""),
    "class_key": ("closed-vocab", "§6.1 entry", "(row, operation), both closed"),
    "disposition": ("closed-vocab", "§6.1 entry", "NAMED-AS-DEFECT | EXPLAINED"),
    "rederivation_digest": ("digest-ref", "§6.1 entry", "revision must contain the class_key"),
    "explanation_ref": ("digest-ref", "§6.1 entry", "sha256 of the canonical explanation body"),
    # explanation artifact (§6.1)
    "cause": ("closed-vocab", "§6.1 explanation", "five-member set"),
    # acceptance-evidence projection (§6.1 (v))
    "parent_attempt_present": ("closed-vocab", "§6.1 projection", "predicate bit"),
    "byte_integrity_pass": ("closed-vocab", "§6.1 projection", "predicate bit"),
    "canonical_shape_pass": ("closed-vocab", "§6.1 projection", "predicate bit"),
}

def extract(text):
    fields = set()
    m = re.search(r"exactly these \w+ fields[^:]*:\*\*\n(.+?)\.\n  \*\*", text, re.S)
    if m:
        fields |= set(re.findall(r"`([a-z0-9_]+)`", m.group(1)))
    m = re.search(r"access log under its BS-2k event schema \(([^)]+)\)", text)
    if m:
        fields |= {f.strip() for f in re.sub(r"—.*", "", m.group(1)).split(",")}
    m = re.search(r"ENUMERATION ENTRY\*\* is an authenticated record with exactly these fields: (.+?)· the enumerator", text, re.S)
    if m:
        fields |= set(re.findall(r"`([a-z0-9_]+)`", m.group(0)))
    if re.search(r"`cause` token from the declared set", text):
        fields.add("cause")
    fields |= set(re.findall(r"`(parent_attempt_present|byte_integrity_pass|canonical_shape_pass)`", text))
    # a draft-side token that is already a canonical.* row is the same surface mentioned in
    # prose, not a new field - the entry-block span widened over the one-encoding paragraph
    # at V79 and harvested 'provenance_record' from a sentence about its pending schema
    return {f for f in fields if f and not f.isdigit()
            and f"canonical.{f}" not in V9_CONSTRAINTS}

def envelope_fields():
    """The receipt envelope's own field names, extracted from v9's receipt() constructor."""
    src = V9.read_text()
    import re as _re
    body = _re.search(r"envelope = \((.+?field\(\"body\").+?\)\n", src, _re.S).group(1)
    names = set(_re.findall(r'field\("([a-z_]+)"', body))
    names |= {"body_sha256", "envelope_sha256"}
    return {f"envelope.{n}" for n in names if n != "body"}

BS7P_ENV = {f"bs7p_env.{n}" for n in (
    "interpreter_path", "interpreter_sha256", "dependency_roots", "dynamic_load_manifest")}
ENTRIES = {"roots_entry.path", "roots_entry.digest", "dlm_entry.path", "dlm_entry.digest"}
SIGS = {f"sig.{n}" for n in ("freeze", "bsl_lock", "opening", "explanation", "checkpoint")}
ARRIVAL = {f"arrival.{n}" for n in ("kind", "timestamp", "boot_epoch", "monotonic_reading",
    "row", "operation", "object_identity", "request_key", "running_chain_digest")}
# the checkpoint clock record (spec 3b authenticated clock basis - GPT56-V89 F1, CODEX-V89 F2)
CKCLOCK = {"ckclock.boot_epoch", "ckclock.monotonic_reading",
           "ckclock.predecessor_epoch", "ckclock.gap_declaration"}
# the binding-to-key map, declared at draft (iv-c) (CODEX-V90 F2: the pre-opening verifier
# consumes it; an unlisted artifact is chi-bearing by default)
HALTREC = {"haltrec.kind", "haltrec.chain_head"}   # the exhaustion halt receipt's non-chi
# face (CODEX-V94 F4); identities live SEALED in the committee store (GPT56-V94 F7)
BINDMAP = {"bindmap.request_key", "bindmap.decision_chain_position",
           "bindmap.decision_event_digest", "bindmap.decision_boot_epoch",
           "bindmap.decision_monotonic_reading", "bindmap.signature"}
OPENAUTH = {f"openauth.{n}" for n in ("bsl_digest", "store_identity_main", "store_identity_committee",
    "destination", "ceremony_id", "phase", "signer_identity", "schema_version")}
FREEZE = {f"freezebody.{n}" for n in ("code_digest", "parent_sha256", "selection_bricks",
    "class_counts", "draft_sha256")}
PARAMS = {f"param.{n}" for n in (
    "duration_ms", "attempt_count", "signal_number", "lease_id_digest", "store_errno")}
LOCKBODY = {f"lockbody.{n}" for n in ("roster_digest", "accepted_mask_digest",
    "calibration_record_digest", "stagec_receipt_digest", "decision_input_digests",
    "classp_receipt_manifest", "gate_reports", "freeze_signature", "lock_checkpoint",
    "chain_segment", "archive_seal_state", "environment_record", "signer_identity")}

def crosscheck_declared(text):
    """F7 (both seats): declared sets could silently omit. The three richest are now CHECKED
    declarations - the generator extracts the clause text's own noun phrases and fails if a
    declared set misses one or carries a stranger.
    OPENAUTH vs Clause 6; LOCKBODY vs clause 3(b); FREEZE vs the freeze-body sentence;
    and since V92, ARRIVAL vs the (ii-b) tuple and BINDMAP vs the (iv-c) tuple - the
    hand-declared sets that CODEX-V91 F4 showed could drift silently from the draft."""
    import re as _re
    problems = []
    # (ii-b): extract the arrival tuple from the draft bytes and compare field-for-field
    # SCOPED (GPT56-V92 F5, CODEX-V92 F6): the unscoped search matched Row B's duplicate
    # tuple, so deleting item (ii-b) stayed green. The extraction now anchors on the (ii-b)
    # label itself, and separately requires the Row B duplicate to EXIST and MATCH - two
    # sites, one schema, both checked.
    # decoy-tight (CODEX-V93 F5): the (ii-b) segment must contain EXACTLY ONE tuple, and the
    # label itself must be unique - a decoy tuple planted inside the window, or a second
    # (ii-b) label, fails loudly instead of shadowing the normative schema.
    ITEM = "\n(ii-b) **the ARRIVAL event"   # the item-DEFINITION form; bare "(ii-b)"
    # cross-references are legion and legitimate (first run of this check counted 5)
    if text.count(ITEM) != 1:
        problems.append(f"(ii-b) item-definition count {text.count(ITEM)} != 1 - decoy or deletion")
    seg = text[text.find(ITEM):text.find(ITEM) + 700] if ITEM in text else ""
    seg_tuples = _re.findall(r"kind=ARRIVAL, ([^)]+)\)", seg)
    all_tuples = _re.findall(r"kind=ARRIVAL, ([^)]+)\)", text)
    m = len(seg_tuples) == 1
    if not m:
        problems.append(f"(ii-b) segment holds {len(seg_tuples)} arrival tuple(s), not 1 - "
                        "gone, reworded past the extractor, or decoyed (CODEX-V93 F5)")
    elif len(all_tuples) < 2 or any(x != all_tuples[0] for x in all_tuples):
        problems.append(f"arrival tuple sites disagree or Row B duplicate missing: "
                        f"{len(all_tuples)} site(s)")
    if m:
        norm = {"timestamp": "timestamp", "boot_epoch": "boot_epoch",
                "monotonic_reading": "monotonic_reading", "row": "row",
                "operation": "operation", "object identity": "object_identity",
                "request_key": "request_key",
                "running chain digest": "running_chain_digest"}
        got = {"arrival.kind"}
        for part in seg_tuples[0].split(","):
            part = part.strip()
            if part in norm:
                got.add("arrival." + norm[part])
            else:
                problems.append(f"(ii-b) tuple carries a field this extractor cannot map: {part!r}")
        if got != ARRIVAL:
            problems.append(f"ARRIVAL declaration drifted from (ii-b): declared-only "
                            f"{sorted(ARRIVAL - got)}, draft-only {sorted(got - ARRIVAL)}")
    # (iv-c): the bindmap tuple
    m = _re.search(r"closed schema `\(request_key, decision chain_position, decision "
                   r"event_digest, decision boot_epoch, decision monotonic_reading, "
                   r"signature\)`", text)
    if not m:
        problems.append("(iv-c) bindmap tuple not found in the draft or its shape changed - "
                        "re-derive the BINDMAP declaration against the draft bytes")

    c6 = _re.search(r"Opening authorization\.\*\* The canonical opening-authorization body[^.]*binds exactly: ([^.]+)\.", text)
    if c6:
        want = {"bsl_digest": "BS-L digest", "store_identity_main": "store identities",
                "store_identity_committee": "store identities", "destination": "destination",
                "ceremony_id": "ceremony identifier", "phase": "phase P7",
                "signer_identity": "signer identity", "schema_version": "schema/version"}
        low = c6.group(1).lower()
        for f, phrase in want.items():
            if phrase.split()[0].lower() not in low:
                problems.append(f"openauth.{f}: '{phrase}' not found in Clause 6")
    else:
        problems.append("Clause 6 sentence not found for openauth cross-check")
    c3b = _re.search(r"canonical body names exactly, in canonical order: (.{100,900}?)signer identity\.", text, _re.S)
    if c3b:
        low = c3b.group(0).lower()
        for probe in ("roster digest", "accepted-mask digest", "calibration-record digest",
                      "stage-c receipt digest", "decision-input digests", "class-p slot receipt",
                      "gate reports", "freeze signature", "lock checkpoint", "chain segment",
                      "archive seal-state", "environment record", "signer identity"):
            if probe not in low:
                problems.append(f"lockbody: '{probe}' not found in clause 3(b)")
    else:
        problems.append("clause 3(b) sentence not found for lockbody cross-check")
    # freeze-body crosscheck (GPT56-V84 F3: the freeze body had no check, so a deletion was silent)
    fb = _re.search(r"canonical freeze-signature body\*\* is the concatenation, in this order, of: ([^\n]+)", text)
    if fb:
        low = fb.group(1).lower()
        for probe in ("code digest", "pinned_parent_sha256", "pinned_selection_bricks",
                      "class counts", "own sha"):
            if probe not in low.replace("`", ""):
                problems.append(f"freezebody: {probe!r} not found in the freeze-body sentence")
    else:
        problems.append("freeze-body sentence not found for crosscheck")
    # stranger detection for Clause 6 (CODEX-V84 F4: ADDED normative fields were invisible - the
    # check only probed declared members; every comma-segment must now map to a known member)
    if c6:
        known = ("bs-l digest", "store identities", "destination", "ceremony identifier",
                 "phase p7", "signer identity", "schema/version", "schema")
        for seg in c6.group(1).split(","):
            s = seg.strip().lower()
            s = s[4:] if s.startswith("and ") else s
            s = s.strip("* ")
            if s and not any(k.split()[0] in s or k.split()[-1] in s for k in known):
                problems.append(f"openauth STRANGER segment in Clause 6: {s[:50]!r}")
    return problems
CANONICAL = {f"canonical.{n}" for n in (
    "freeze_signature_body", "lock_body", "opening_authorization", "entry_body",
    "explanation_body", "provenance_record")}
NONSLOT = {f"nonslot.{n}" for n in (
    "access_log_chain", "enumeration_surface", "acceptance_evidence_projection",
    "cutout_completion_receipt", "stage_completion_artifact", "label_set_receipt",
    "unblinding_receipt", "adequacy_receipt", "archive_seal_state_receipt",
    "lock_checkpoint_receipt")}

def environment_leaves():
    """environment_record()'s own keys, from its dict literal - six leaves, not one container."""
    import re as _re
    src = V9.read_text()
    body = _re.search(r"def environment_record.+?return \{(.+?)\}\n", src, _re.S).group(1)
    return {f"environment.{k}" for k in _re.findall(r'"([a-z_]+)":', body)}

def main():
    text = DRAFT.read_text()
    xp = crosscheck_declared(text)
    if xp:
        for x in xp:
            print("CROSS-CHECK FAIL:", x)
        return 1
    found = extract(text)
    v9f = v9_slot_fields() | envelope_fields() | NONSLOT | CANONICAL | BS7P_ENV | ENTRIES | ARRIVAL | CKCLOCK | BINDMAP | HALTREC | OPENAUTH | FREEZE | SIGS | LOCKBODY | PARAMS | environment_leaves() | {"entry.signature"}
    rows, missing = [], []
    for sf in sorted(v9f):
        if sf in V9_CONSTRAINTS:
            c, w, note = V9_CONSTRAINTS[sf]
            rows.append(f"| `{sf}` | {c} | {w} | {note.replace(chr(124), chr(183))} |")
        else:
            missing.append(sf)
            rows.append(f"| `{sf}` | **FORBIDDEN-BY-DEFAULT — no registry row** | v9 | classify or remove |")
    stale_v9 = sorted(set(V9_CONSTRAINTS) - v9f)
    for f in sorted(found):
        if f in CONSTRAINTS:
            c, w, note = CONSTRAINTS[f]
            rows.append(f"| `{f}` | {c} | {w} | {note.replace(chr(124), chr(183))} |")
        else:
            missing.append(f)
            rows.append(f"| `{f}` | **FORBIDDEN-BY-DEFAULT — no registry row** | ? | classify or remove |")
    stale = sorted(set(CONSTRAINTS) - found) + stale_v9
    out = ["# STRING-FIELD REGISTRY — every string-bearing field in every non-χ artifact\n",
           f"**Generated from `{DRAFT.name}`'s schema blocks by `ref/gen_string_field_registry.py`; "
           "TWO provenances, said plainly (CODEX-V81 F8: the header claimed generated-from-schemas while "
           "several sets are hand-declared): draft schema blocks, v9's SLOT_SCHEMA, the envelope "
           "constructor and environment_record are EXTRACTED mechanically; the openauth, freeze, "
           "canonical, non-slot, signature and parameter sets are DECLARED here as classification "
           "law, versioned with this generator. Extraction cannot silently omit; declaration is "
           "auditable in one screen.** A field with no row is **forbidden by default** and the generator exits "
           "nonzero. Constraints: `closed-vocab` (a declared member set) · `bounded-encoding` "
           "(digest/decimal-in-range) · `digest-ref` (sha256 of a canonical body).\n",
           "**The honest limit:** bounded numerics still carry bits; the registry bounds capacity "
           "and cannot zero it. What it removes is free prose.\n",
           "| field | constraint | declared | note |", "|---|---|---|---|"] + rows
    if stale:
        out.append(f"\n**Classified but not found in the draft (stale rows, check the extractor):** "
                   f"{', '.join(f'`{s}`' for s in stale)}")
    (B / "ref/STRING_FIELD_REGISTRY.md").write_text("\n".join(out) + "\n")
    n_pending = sum(1 for r in rows if "SCHEMA-PENDING" in r)
    (B / "ref/_registry_counts.txt").write_text(
        f"total={len(found) + len(v9f)} nonslot={len(NONSLOT)} pending={n_pending}\n")
    print(f"fields found {len(found) + len(v9f)}  classified "
          f"{len(found) + len(v9f) - len(missing)}  FORBIDDEN-BY-DEFAULT {len(missing)}  "
          f"stale {len(stale)}")
    if missing:
        print("UNCLASSIFIED:", missing)
    if stale:
        # CODEX-V73 F4: stale rows are extractor/schema drift - the very signal that caught the
        # digit-blind bug - and exiting zero on them made a format omission nonblocking.
        print("STALE (blocking):", stale)
    return 1 if (missing or stale) else 0

if __name__ == "__main__":
    sys.exit(main())
