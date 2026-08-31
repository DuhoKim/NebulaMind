#!/usr/bin/env python3
"""enumeration_verifier — REQUIRED build item (CODEX-V68 F5). Consulted at FIVE GATES
(BS-L issuance, the lock opening, BS-7f, BS-V, disclosure), each pass over the chain as
it then stands. It RECOMPUTES, never accepts a producer's summary: the catch-all event
sets (REFUSED-UNCLASSIFIED and, by the 2026-08-30 ruling, REFUSED-INTEGRITY-MISMATCH),
the entry↔emission BIJECTION both directions (GPT56-V72 F4), class_key = (table row,
operation) recomputed from the event with the operation drawn from the CLOSED operation
set (CODEX-V70 F6), the ≤1-EXPLAINED-per-key rule, the NAMES-CLASS template with
member-definition containment (CODEX-V78 F4, CODEX-V79 F5), the arrival↔terminal join
with request_digest RECOMPUTED under NMPR1:identity-envelope (GPT56-V112 F2), the
store↔log pass (GPT56-V106 F3, absolute since V107 F2), the successor-export closing
verifier on the terminated path (CODEX-V114 F4), the pass-record chain rule
(GPT56/CODEX-V96 F1), prefix verification at a declared boundary with admission held
across the pass (CODEX-V110 F2, CODEX-V111 F2), and the clock pass over §3b's three
invariants (GPT56/CODEX-V91 F1).

RECORD MODEL (normative for this tool, the decoder lesson applied: the stated model
defines, fixtures corroborate). The chain is an ordered list of records; position IS
the list index. Every record is a plain dict with field "k" (the event kind) and the
kind's fields; canonical body digest = sha256 over NMPR1:<k>: + canonical JSON of the
record's non-digest fields; running digest = sha256(prev_running_hex + body_digest_hex)
with the genesis previous value "0"*64. Event kinds consumed here: arrival, termrec
(decision: TOUCH or REFUSAL, catch-all classes REFUSED-UNCLASSIFIED /
REFUSED-INTEGRITY-MISMATCH), epoch-opening, terminal-checkpoint, drain-start,
receipt-note, verification-boundary, verification-close, verification-read, passrec,
bindmap-entry, successor-export, external-anchor, frame-residue, haltrec. Clock-BEARING
kinds (the §3b monotonicity scan): epoch-opening, arrival, verification-boundary,
verification-close, terminal-checkpoint, drain-start, receipt-note, passrec — termrec is
NOT clock-bearing (the scoping fixture: a decision lands between clock records freely;
its own map_reading obeys decide-within-D and read-then-stall instead). The
identity-envelope preimage is the draft's: sha256 over NMPR1:identity-envelope: +
canonical JSON of (origin_row, frame_sequence, operation, object_identity), and
origin_row is REQUIRED EQUAL to the arrival's own row. Constants arrive ONLY through
ProvisionedConstants, every field required non-None (the V115 lesson: a None-armed
call must be impossible, so absence refuses at construction, not at use).

REFUSAL SEMANTICS, stated (AGY ENV-V1 F6): every pass refuses at the FIRST failed
check in its documented order — this is a GATE, where one refusal blocks, not a
linter enumerating defects. A composite-defect input therefore reports the earliest
code its defects reach (quantization before regression in the clock pass; row-alias
before digest recomputation in the join), and the fixtures assert that order.

v2 after AGY ENV-V1 (DEFECTIVE, 6): the reset fixture rebuilt so the derived count
does real work (2 closes + pass record + 2 closes accepts ONLY because the record
resets; 4 unreset closes would exhaust the cap); the NAMED-second-occurrence positive
control added; the MISSED 'immediately preceding' obligation implemented — a
checkpoint's in-commit refusal events must form a contiguous block ending at the
checkpoint's own position (COMMIT-EVENTS-NOT-ADJACENT) — with both fixtures; the
in-hold cross-epoch arrival branch kept as defense-in-depth WITH the fixture that
reaches it (a clock-malformed chain boundary_pass alone must still refuse); hold
verification-reads now bind to THE PASS'S OWN boundary via boundary_position (a
stuffed foreign read no longer launders arbitrary joined records past the hold);
FORM_SCHEMAS mirrored to the authoritative registry (prelock carries
terminal_enumeration_digest)."""
import hashlib
import json
import sys

GATES = ("BS-L", "LOCK-OPENING", "BS-7F", "BS-V", "DISCLOSURE")
CATCHALL_CLASSES = ("REFUSED-UNCLASSIFIED", "REFUSED-INTEGRITY-MISMATCH")
CLOCK_BEARING = ("epoch-opening", "arrival", "verification-boundary",
                 "verification-close", "terminal-checkpoint", "drain-start",
                 "receipt-note", "passrec")
FRAME_RESIDUES = ("partial-header", "truncated-body", "malformed-length",
                  "crash-during-decode", "crash-mid-arrival-append")
CLOSE_CLASSES = ("ABORTED", "EXPIRED", "ABORTED-BY-RESTART")

# per-kind exact ordered field sets — the producer and this verifier both SELECT BY
# KIND (GPT56-V115 F1: a flat union schema conforms to nothing). These tuples MIRROR
# ref/gen_string_field_registry.py's FORM_SCHEMAS, the authoritative registry the
# draft's form echo checks — a divergent twin here would be the relabelling defect
FORM_SCHEMAS = {
    "successor-export": ("kind", "sealed_enumeration_digest",
                         "continuation_segment_digest", "terminal_head",
                         "freeze_signature_digest", "flagged_keys"),
    "successor-export-prelock": ("kind", "terminal_enumeration_digest",
                                 "terminal_head", "freeze_signature_digest",
                                 "flagged_keys"),
}


class Refusal(ValueError):
    def __init__(self, code, msg):
        self.code = code
        super().__init__(f"{code}: {msg}")


def _r(code, msg):
    raise Refusal(code, msg)


class ProvisionedConstants:
    """Every constant REQUIRED and non-None at construction; there is no default and
    no None-armed path (GPT56-V115 F2's lesson moved to the front door)."""
    FIELDS = ("first_epoch_anchor", "gate_pass_budget", "pass_retry_max",
              "decide_within_d", "quantum_g", "operation_set",
              "bs2f_receipt_digest")

    def __init__(self, **kw):
        for f in self.FIELDS:
            if f not in kw:
                _r("CONSTANT-MISSING", f"required constant {f} not provided")
            if kw[f] is None:
                _r("CONSTANT-NONE", f"constant {f} is None; a None-armed verifier "
                                    "is the V115 defect")
        extra = set(kw) - set(self.FIELDS)
        if extra:
            _r("CONSTANT-UNKNOWN", f"unknown constants {sorted(extra)}")
        for f in self.FIELDS:
            setattr(self, f, kw[f])
        self.operation_set = frozenset(self.operation_set)
        if not self.operation_set:
            _r("CONSTANT-EMPTY", "operation_set is empty; the closed set must close "
                                 "around something")


# ------------------------------------------------------------------ digests
def _canon(obj):
    return json.dumps(obj, sort_keys=True, separators=(",", ":"), ensure_ascii=False)


def body_digest(rec):
    body = {k: v for k, v in rec.items() if k not in ("body_digest", "running")}
    return hashlib.sha256(
        b"NMPR1:" + rec["k"].encode() + b":" + _canon(body).encode()).hexdigest()


def request_digest(origin_row, frame_sequence, operation, object_identity):
    return hashlib.sha256(
        b"NMPR1:identity-envelope:" + _canon(
            [origin_row, frame_sequence, operation, object_identity]).encode()
    ).hexdigest()


def mkchain(records):
    """Fixture-side builder: stamps body_digest and running digests; the verifier
    recomputes both independently in verify_prefix."""
    prev = "0" * 64
    out = []
    for rec in records:
        rec = dict(rec)
        rec["body_digest"] = body_digest(rec)
        rec["running"] = hashlib.sha256(
            (prev + rec["body_digest"]).encode()).hexdigest()
        prev = rec["running"]
        out.append(rec)
    return out


def verify_prefix(chain, upto):
    """Running-digest discipline over chain[:upto+1], external anchors checked at
    their positions — a truncated or rewritten prefix is caught at its first anchor
    (GPT56-V94 F1, CODEX-V94 F1)."""
    prev = "0" * 64
    for pos, rec in enumerate(chain[:upto + 1]):
        bd = body_digest(rec)
        if rec.get("body_digest") != bd:
            _r("BODY-DIGEST-MISMATCH", f"pos {pos}")
        # the anchor pins the running digest BEFORE itself — custody up to the
        # anchor point; pinning its own running would be circular by construction
        if rec["k"] == "external-anchor" and rec["anchored_running"] != prev:
            _r("ANCHOR-MISMATCH", f"pos {pos}: chain does not reach its anchor")
        want = hashlib.sha256((prev + bd).encode()).hexdigest()
        if rec.get("running") != want:
            _r("RUNNING-DIGEST-MISMATCH", f"pos {pos}")
        prev = rec["running"]


# ------------------------------------------------------------------ clock pass
def clock_pass(chain, constants, upto=None):
    """Spec §3b's three invariants over the clock-bearing records of the chain as it
    then stands, plus the decision-side rules (decide-within-D, FIFO, read-then-stall,
    quantization, declared gaps with the emptiness proof)."""
    upto = len(chain) - 1 if upto is None else upto
    g = constants.quantum_g
    cur_epoch = None
    cur_reading = None
    opened = set()
    latest_opening_epoch = None
    all_epochs_on_events = set()
    declared_gaps = set()
    decisions_seen = []
    for pos, rec in enumerate(chain[:upto + 1]):
        if "epoch" in rec:
            all_epochs_on_events.add(rec["epoch"])
        if rec["k"] == "epoch-opening":
            for f in ("epoch", "reading", "predecessor", "gap_declared",
                      "gap_epochs"):
                if f not in rec:
                    _r("OPENING-SCHEMA", f"pos {pos}: opening missing {f}")
            if rec["epoch"] in opened:
                _r("EPOCH-REUSE", f"pos {pos}: epoch {rec['epoch']} opened twice")
            if cur_epoch is None:
                if rec["predecessor"] != constants.first_epoch_anchor:
                    _r("FIRST-EPOCH-UNANCHORED",
                       f"pos {pos}: predecessor is not the provisioning constant")
                if rec["gap_declared"] or rec["gap_epochs"]:
                    _r("OPENING-SCHEMA", f"pos {pos}: first epoch declares a gap")
            else:
                if rec["epoch"] <= cur_epoch:
                    _r("EPOCH-ROLLBACK",
                       f"pos {pos}: epoch {rec['epoch']} after {cur_epoch}")
                skipped = set(range(cur_epoch + 1, rec["epoch"]))
                if skipped and not rec["gap_declared"]:
                    _r("EPOCH-GAP-UNDECLARED",
                       f"pos {pos}: epochs {sorted(skipped)} skipped silently")
                if rec["gap_declared"] and set(rec["gap_epochs"]) != skipped:
                    _r("EPOCH-GAP-MISDECLARED",
                       f"pos {pos}: declared {rec['gap_epochs']}, "
                       f"actual {sorted(skipped)}")
                declared_gaps |= skipped
                prior_opening = next(r for r in reversed(chain[:pos])
                                     if r["k"] == "epoch-opening")
                if rec["predecessor"] != prior_opening["body_digest"]:
                    _r("OPENING-PREDECESSOR-MISMATCH", f"pos {pos}")
            opened.add(rec["epoch"])
            cur_epoch = rec["epoch"]
            latest_opening_epoch = rec["epoch"]
            cur_reading = rec["reading"]
            if rec["reading"] % g != 0:
                _r("UNQUANTIZED-READING", f"pos {pos}")
            continue
        if rec["k"] in CLOCK_BEARING:
            if cur_epoch is None:
                _r("EPOCH-NOT-OPENED",
                   f"pos {pos}: first clock-bearing record of an epoch must be its "
                   "opening")
            if rec["epoch"] != cur_epoch:
                if rec["epoch"] < cur_epoch:
                    _r("EPOCH-ROLLBACK", f"pos {pos}")
                _r("EPOCH-NOT-OPENED",
                   f"pos {pos}: epoch {rec['epoch']} has no opening record yet")
            if rec["reading"] % g != 0:
                _r("UNQUANTIZED-READING", f"pos {pos}")
            if rec["reading"] < cur_reading:
                _r("READING-REGRESSION",
                   f"pos {pos}: {rec['reading']} < {cur_reading}")
            cur_reading = rec["reading"]
        # NOTE: "every arrival's epoch equal to the latest opening's" is enforced by
        # the clock-bearing epoch checks above (EPOCH-NOT-OPENED / EPOCH-ROLLBACK):
        # cur_epoch always equals the latest opening's epoch, so a separate arrival
        # branch would be unreachable control — deliberately not written
        if rec["k"] == "termrec":
            if rec["reading"] % g != 0 or rec["map_reading"] % g != 0:
                _r("UNQUANTIZED-READING", f"pos {pos}")
            decisions_seen.append((pos, rec))
            arr = chain[rec["request_key"]] if 0 <= rec["request_key"] < len(chain) \
                else None
            if arr is not None and arr["k"] == "arrival":
                if (rec["epoch"] == arr["epoch"]
                        and rec.get("refusal_class") not in CATCHALL_CLASSES
                        and rec["map_reading"] > arr["reading"]
                        + constants.decide_within_d):
                    _r("DECIDE-WITHIN-D",
                       f"pos {pos}: map-entry reading exceeds arrival + D and the "
                       "decision is not the catch-all taking it at its turn")
                stall_floor = max((r["reading"] for r in chain[:pos]
                                   if r["k"] in CLOCK_BEARING
                                   and r["epoch"] == rec["epoch"]), default=None)
                if stall_floor is not None and rec["map_reading"] < stall_floor:
                    _r("READ-THEN-STALL",
                       f"pos {pos}: map-entry reading {rec['map_reading']} below a "
                       f"prior clock-bearing record's {stall_floor}")
    gap_hits = declared_gaps & all_epochs_on_events
    if gap_hits:
        _r("GAP-EPOCH-NOT-EMPTY",
           f"declared-gap epochs {sorted(gap_hits)} appear on chain events; the "
           "emptiness proof fails")
    # FIFO: decisions must land in their arrivals' chain order
    decided_arrivals = [rec["request_key"] for _, rec in decisions_seen]
    if decided_arrivals != sorted(decided_arrivals):
        _r("DECISION-ORDER",
           "out-of-order decision against FIFO is malformed history")


# ------------------------------------------------------------------ boundary pass
def boundary_pass(chain, gate, constants):
    """Prefix verification at a declared boundary with ADMISSION HELD ACROSS THE PASS
    at every gate. The gate action stands at the chain head (the pass appends its own
    record only on acceptance); it belongs to the last open boundary of this gate.
    The alternation law boundary → pass-record-or-close → boundary holds per gate;
    the retry count is DERIVED (closes since the gate's last pass record); the hold
    is released by inequality only, and a released interval is contaminated: its
    late gate action refuses."""
    if gate not in GATES:
        _r("UNKNOWN-GATE", gate)
    open_boundary = None
    closes_since_pass = 0
    for pos, rec in enumerate(chain):
        if rec["k"] == "verification-boundary":
            if rec["gate"] != gate:
                continue
            if open_boundary is not None:
                _r("BOUNDARY-OVER-OPEN",
                   f"pos {pos}: second boundary while {open_boundary} is open")
            open_boundary = pos
        elif rec["k"] == "verification-close":
            if rec["gate"] != gate:
                # gate-equality law: a close must aim at a boundary OF ITS OWN gate;
                # aiming any close at another gate's boundary is malformed
                tgt = chain[rec["boundary_position"]] \
                    if 0 <= rec["boundary_position"] < len(chain) else None
                if tgt is not None and tgt["k"] == "verification-boundary" \
                        and tgt["gate"] == gate:
                    _r("CLOSE-GATE-MISMATCH",
                       f"pos {pos}: a {rec['gate']} close aimed at a {gate} "
                       "boundary")
                continue
            if rec["close_class"] not in CLOSE_CLASSES:
                _r("CLOSE-CLASS-UNKNOWN", f"pos {pos}: {rec['close_class']}")
            if open_boundary is None or rec["boundary_position"] != open_boundary:
                _r("CLOSE-WITHOUT-BOUNDARY", f"pos {pos}")
            tgt = chain[rec["boundary_position"]]
            if tgt["gate"] != rec["gate"]:
                _r("CLOSE-GATE-MISMATCH",
                   f"pos {pos}: close gate {rec['gate']} vs boundary gate "
                   f"{tgt['gate']}")
            open_boundary = None
            closes_since_pass += 1
        elif rec["k"] == "passrec" and rec["gate"] == gate:
            if open_boundary is None:
                _r("PASSREC-WITHOUT-BOUNDARY", f"pos {pos}")
            open_boundary = None
            closes_since_pass = 0
    if open_boundary is None:
        _r("NO-OPEN-BOUNDARY", f"gate {gate} has no open boundary for its action")
    if closes_since_pass >= constants.pass_retry_max:
        _r("PASS-RETRY-EXHAUSTED",
           f"{closes_since_pass} consecutive closes at {gate} reach "
           f"PASS_RETRY_MAX={constants.pass_retry_max}")
    b = chain[open_boundary]
    verify_prefix(chain, open_boundary)
    cur = [r for r in chain if r["k"] in CLOCK_BEARING]
    if cur and cur[-1]["epoch"] != b["epoch"]:
        _r("BOUNDARY-EPOCH-CHANGED",
           "an epoch change aborts open passes; this boundary was never closed "
           "ABORTED-BY-RESTART")
    read_positions = set()
    for pos in range(open_boundary + 1, len(chain)):
        rec = chain[pos]
        if rec["k"] == "verification-read":
            # THE PASS'S OWN reads only: a read must name this pass's boundary, or
            # a foreign writer could stuff reads and launder arbitrary "joined"
            # records past the hold (AGY ENV-V1 F5)
            if rec.get("boundary_position") != open_boundary:
                _r("FOREIGN-RECORD-IN-HOLD",
                   f"pos {pos}: a verification-read not bound to this pass's "
                   "boundary")
            read_positions.add(pos)
            continue
        if rec.get("joined_read") in read_positions:
            continue  # the pass's own records, excluded through their typed joins
        if rec["k"] in ("drain-start", "terminal-checkpoint", "receipt-note"):
            _r("PASS-ABORTED-BY-TERMINATION",
               f"pos {pos}: termination's indivisible unit landed mid-pass; the "
               "pass must re-boundary after it, its gate action refuses")
        if rec["k"] == "arrival":
            if rec["epoch"] != b["epoch"]:
                # defense-in-depth, NOT dead code (AGY ENV-V1 F4): reachable when
                # the chain is clock-malformed (a later record regressing to the
                # boundary's epoch slips the cur[-1] pre-check) and boundary_pass
                # runs standalone — the fixture constructs exactly that chain
                _r("BOUNDARY-EPOCH-CHANGED",
                   f"pos {pos}: cross-epoch arrival inside a hold")
            if rec["reading"] > b["reading"] + constants.gate_pass_budget:
                _r("RELEASED-INTERVAL",
                   f"pos {pos}: the hold released by inequality; the interval is "
                   "contaminated and this late gate action refuses")
            _r("MALFORMED-HOLD-ARRIVAL",
               f"pos {pos}: an ordinary arrival at or inside the budget is "
               "malformed history inside a hold")
        _r("FOREIGN-RECORD-IN-HOLD", f"pos {pos}: {rec['k']}")
    return open_boundary


# ------------------------------------------------------------------ join pass
def join_pass(chain, gate, constants):
    """The arrival↔terminal join, recomputed from the chain: request_digest is
    RECOMPUTED under NMPR1:identity-envelope with origin_row required equal to the
    arrival's own row (GPT56-V112 F2); per-row frame sequences strictly increase; a
    request_key IS its arrival's chain position; terminals bind one arrival each with
    matching identity; overdue is computed from authenticated bytes only; frame
    residues are NOT arrivals and carry no obligation (§1c)."""
    arrivals = {}
    seen_digests = {}
    seen_bindings = {}
    row_seq = {}
    for pos, rec in enumerate(chain):
        if rec["k"] == "frame-residue":
            if rec["residue"] not in FRAME_RESIDUES:
                _r("RESIDUE-UNKNOWN", f"pos {pos}: {rec['residue']}")
            continue  # no arrival, no lifecycle obligation
        if rec["k"] != "arrival":
            continue
        if rec["origin_row"] != rec["row"]:
            _r("ROW-ALIAS",
               f"pos {pos}: envelope origin_row {rec['origin_row']} differs from "
               f"the arrival's own row {rec['row']}")
        want = request_digest(rec["origin_row"], rec["frame_sequence"],
                              rec["operation"], rec["object_identity"])
        if rec["request_digest"] != want:
            _r("DIGEST-NOT-RECOMPUTED",
               f"pos {pos}: stored request_digest does not recompute from the "
               "canonical identity tuple")
        if rec["request_digest"] in seen_digests:
            _r("REPLAYED-FRAME",
               f"pos {pos}: request_digest already arrived at "
               f"{seen_digests[rec['request_digest']]}")
        seen_digests[rec["request_digest"]] = pos
        last = row_seq.get(rec["row"])
        if last is not None and rec["frame_sequence"] <= last:
            _r("SEQUENCE-REGRESSION",
               f"pos {pos}: row {rec['row']} sequence {rec['frame_sequence']} "
               f"after {last}")
        row_seq[rec["row"]] = rec["frame_sequence"]
        if rec["binding"] in seen_bindings:
            _r("BINDING-REUSED",
               f"pos {pos}: binding already used at {seen_bindings[rec['binding']]}")
        seen_bindings[rec["binding"]] = pos
        arrivals[pos] = rec
    terminals = {}
    cut_pos = None
    for pos, rec in enumerate(chain):
        if rec["k"] == "signed-cut":
            cut_pos = pos
        if rec["k"] != "termrec":
            continue
        key = rec["request_key"]
        if key not in arrivals:
            _r("TERMINAL-DANGLING",
               f"pos {pos}: request_key {key} names no on-chain arrival — the key "
               "is the arrival's chain position by definition")
        arr = arrivals[key]
        if rec["binding"] != arr["binding"]:
            _r("KEY-BINDING-MISMATCH",
               f"pos {pos}: terminal binding does not name its arrival's binding")
        if key in terminals:
            _r("TWO-TERMINALS-ONE-KEY", f"pos {pos}: second terminal for {key}")
        if (rec["row"], rec["operation"], rec["object_identity"]) != \
                (arr["row"], arr["operation"], arr["object_identity"]):
            _r("IDENTITY-SWAP",
               f"pos {pos}: terminal (row, operation, object identity) differ from "
               "its arrival's — the swap the key alone cannot see")
        terminals[key] = pos
        if cut_pos is not None and pos > cut_pos:
            entries = [r for r in chain
                       if r["k"] == "bindmap-entry" and r["request_key"] == key]
            if not entries:
                _r("CONTINUATION-ENTRY-MISSING",
                   f"pos {pos}: a post-signed-cut decision without its continuation "
                   "map entry")
    # one-decision-event: failed_members is a PROJECTION cross-checked both ways,
    # and the refusal events ride the commit IMMEDIATELY PRECEDING the checkpoint
    # record — a contiguous block ending at the checkpoint's own position (the
    # obligation AGY ENV-V1 F3 found unimplemented)
    for pos, rec in enumerate(chain):
        if rec["k"] != "terminal-checkpoint":
            continue
        commit = set(rec["commit_set"])
        ref_positions = sorted(p for p in commit
                               if p < pos and chain[p]["k"] == "termrec"
                               and chain[p]["outcome"] == "REFUSAL")
        if ref_positions and \
                ref_positions != list(range(pos - len(ref_positions), pos)):
            _r("COMMIT-EVENTS-NOT-ADJACENT",
               f"checkpoint {pos}: in-commit refusal events at {ref_positions} do "
               "not form the contiguous block immediately preceding the "
               "checkpoint record")
        in_commit_refusals = {chain[p]["request_key"] for p in ref_positions}
        listed = set(rec["failed_members"])
        for m in listed - in_commit_refusals:
            _r("LISTED-WITHOUT-EVENT",
               f"checkpoint {pos}: listed member {m} has no refusal event inside "
               "the checkpoint commit")
        for m in in_commit_refusals - listed:
            _r("EVENT-UNLISTED",
               f"checkpoint {pos}: in-commit refusal for {m} is not listed")
    # existence: overdue computed from authenticated bytes only
    clock = [r for r in chain if r["k"] in CLOCK_BEARING]
    now = clock[-1] if clock else None
    for key, arr in arrivals.items():
        if key in terminals:
            continue
        if now is not None and arr["epoch"] < now["epoch"]:
            _r("OVERDUE-ORPHAN",
               f"arrival {key}: earlier epoch than the consulted record — overdue "
               "by definition at the first later-epoch pass")
        if now is not None and arr["epoch"] == now["epoch"] and \
                now["reading"] - arr["reading"] > constants.decide_within_d:
            _r("OVERDUE-ORPHAN",
               f"arrival {key}: past its deadline with no terminal — the deadline "
               "machinery failed, a custody failure")
        if gate == "DISCLOSURE":
            _r("PENDING-AT-DISCLOSURE",
               f"arrival {key}: the run does not end over an open request")
    # the seam: issuance-commit bindings live as continuation entries, never in the
    # sealed segment (CODEX-V90 F3 / GPT56-V90 F5)
    return sorted(arrivals), {k: v for k, v in terminals.items()}


def seam_pass(chain, sealed_bindings):
    for pos, rec in enumerate(chain):
        if rec["k"] == "bindmap-entry" and rec.get("issuance") and \
                rec["binding"] in sealed_bindings:
            _r("SEAM-VIOLATION",
               f"pos {pos}: an issuance-commit binding claimed in the sealed "
               "segment")


# ------------------------------------------------------------------ catch-all pass
def _class_key_str(row, operation):
    return f"({row},{operation})"


def catchall_pass(chain, gate, constants, sealed_enumeration, continuation_segment,
                  explanations, revisions, review_records):
    """Recomputes the catch-all event sets from the chain and holds the entry↔emission
    relation to a BIJECTION checked in both directions (GPT56-V72 F4). class_key is
    recomputed from the event, never trusted stored (GPT56-V67/CODEX-V67 F4); the
    naming template is a parse, not a hope (CODEX-V78 F4, CODEX-V79 F5)."""
    emissions = {pos: rec for pos, rec in enumerate(chain)
                 if rec["k"] == "termrec"
                 and rec.get("refusal_class") in CATCHALL_CLASSES}
    entries = list(sealed_enumeration) + list(continuation_segment)
    by_emission = {}
    for e in entries:
        pos = e["emission_pos"]
        if pos in by_emission:
            _r("DUPLICATE-ENTRY", f"two entries name emission {pos}")
        if pos not in emissions:
            _r("ORPHAN-ENTRY",
               f"entry names position {pos}, which is not a catch-all emission — "
               "the bijection is checked in both directions")
        by_emission[pos] = e
    for pos in emissions:
        if pos not in by_emission:
            _r("UNENUMERATED-EMISSION",
               f"catch-all emission at {pos} has no enumeration entry")
    explained_keys = set()
    key_order = {}
    for pos in sorted(emissions):
        rec, e = emissions[pos], by_emission[pos]
        if rec["operation"] not in constants.operation_set:
            _r("OPERATION-NOT-CLOSED",
               f"pos {pos}: operation {rec['operation']!r} outside the closed set")
        key = (rec["row"], rec["operation"])
        if tuple(e["class_key"]) != key:
            _r("CLASS-KEY-MISMATCH",
               f"pos {pos}: stored key {e['class_key']} vs recomputed {key}")
        key_order.setdefault(key, []).append(pos)
        if rec["refusal_class"] == "REFUSED-INTEGRITY-MISMATCH":
            if e["disposition"] != "LOGGED-AND-CONTINUED":
                _r("MISMATCH-DISPOSITION",
                   f"pos {pos}: mismatch entries take the ruling's review "
                   "disposition, not the catch-all's NAMED/EXPLAINED pair")
            if gate == "DISCLOSURE" and \
                    e.get("review_ref") not in review_records:
                _r("MISMATCH-UNREVIEWED-AT-FREEZE",
                   f"pos {pos}: an unexplained mismatch blocks the "
                   "successor-facing freeze")
            continue
        if e["disposition"] == "EXPLAINED":
            if key in explained_keys or len(key_order[key]) > 1:
                _r("SECOND-EXPLAINED",
                   f"pos {pos}: class {key} recurs — the second occurrence demands "
                   "NAMED-AS-DEFECT and the re-derivation naming requires")
            explained_keys.add(key)
            if e.get("explanation_ref") not in explanations:
                _r("DANGLING-EXPLANATION",
                   f"pos {pos}: explanation_ref does not resolve to a signed "
                   "artifact in the lock-checkpoint materials")
        elif e["disposition"] == "NAMED-AS-DEFECT":
            digest = e.get("revision_digest")
            if digest not in revisions:
                _r("REVISION-ABSENT",
                   f"pos {pos}: no vocabulary revision exists at the entry's digest")
            if digest == e.get("prior_revision_digest"):
                _r("REVISION-UNCHANGED",
                   f"pos {pos}: a re-derivation that changed nothing named nothing")
            text = revisions[digest]
            ks = _class_key_str(*key)
            tokens = {}
            for line in text.splitlines():
                if line.startswith("TOKEN: ") and " := " in line:
                    tok, defn = line[len("TOKEN: "):].split(" := ", 1)
                    tokens[tok.strip()] = defn
            named = None
            for line in text.splitlines():
                if line.startswith(f"NAMES-CLASS: {ks} AS "):
                    named = line[len(f"NAMES-CLASS: {ks} AS "):].strip()
            if named is None:
                _r("NAMING-TEMPLATE-ABSENT",
                   f"pos {pos}: the revision carries no NAMES-CLASS line for {ks}")
            if named not in tokens:
                _r("TOKEN-NOT-MEMBER",
                   f"pos {pos}: {named!r} is not a member of the revised set")
            if ks not in tokens[named]:
                _r("NAMING-VACUOUS",
                   f"pos {pos}: the named token's own definition does not contain "
                   "the class_key — a template naming an unrelated member proves "
                   "nothing (CODEX-V79 F5)")
        else:
            _r("DISPOSITION-UNKNOWN", f"pos {pos}: {e['disposition']!r}")


# ------------------------------------------------------------------ store↔log pass
def store_log_pass(chain, receipt_store):
    """ABSOLUTE (GPT56/CODEX-V107 F2): every TERMINATED receipt in the store has its
    log record — drain-start binding it or a receipt-note — with no age excuse; a
    receipt-note whose store receipt is missing is the note-first inversion."""
    logged = set()
    for rec in chain:
        if rec["k"] in ("drain-start", "receipt-note"):
            logged.add(rec["receipt_digest"])
    stored = {r["receipt_digest"] for r in receipt_store
              if r["status"] == "TERMINATED"}
    for d in stored - logged:
        _r("ORPHAN-RECEIPT",
           f"TERMINATED receipt {d[:16]} has no log record — a Row-B violation, "
           "never a wait state")
    for rec in chain:
        if rec["k"] == "receipt-note" and rec["receipt_digest"] not in stored:
            _r("NOTE-FIRST-INVERSION",
               f"receipt-note for {rec['receipt_digest'][:16]} names no store "
               "receipt")


# ------------------------------------------------------------------ pass records
def passrec_rule(chain, constants):
    """The chain rule: each gate pass record is predecessor-bound; the first record's
    predecessor is BS-2f's receipt digest; no duplicate gate token; no fork; a
    refusing pass emits nothing — refusals block, they do not anchor."""
    recs = [(pos, r) for pos, r in enumerate(chain) if r["k"] == "passrec"]
    seen_gates = set()
    seen_preds = set()
    prev_digest = constants.bs2f_receipt_digest
    for i, (pos, r) in enumerate(recs):
        if r.get("refusing"):
            _r("REFUSING-PASS-RECORD",
               f"pos {pos}: a refusing pass emitted a record")
        if r["gate"] in seen_gates:
            _r("DUPLICATE-GATE-PASS", f"pos {pos}: second record for {r['gate']}")
        seen_gates.add(r["gate"])
        if r["predecessor"] in seen_preds:
            _r("PASSREC-FORK",
               f"pos {pos}: two records share one predecessor")
        seen_preds.add(r["predecessor"])
        if r["predecessor"] != prev_digest:
            _r("FIRST-PREDECESSOR" if i == 0 else "PREDECESSOR-BROKEN",
               f"pos {pos}: predecessor does not bind "
               + ("BS-2f's receipt digest" if i == 0 else "the prior record")
               + f" (want {prev_digest[:16]})")
        prev_digest = r["body_digest"]


# ------------------------------------------------------------------ export pass
def continuation_segment_digest(continuation_segment):
    """DEFINED preimage (CODEX-V109 F3): domain-tagged, count-prefixed concatenation
    of continuation-entry canonical bodies sorted by chain_position."""
    bodies = sorted(continuation_segment, key=lambda e: e["emission_pos"])
    buf = b"NMPR1:continuation-segment:" + str(len(bodies)).encode() + b":"
    for e in bodies:
        buf += _canon(e).encode()
    return hashlib.sha256(buf).hexdigest()


def regenerate_export(kind, chain, sealed_enumeration, continuation_segment,
                      freeze_signature_digest, flagged_keys, terminal_pos):
    if kind not in FORM_SCHEMAS:
        _r("EXPORT-KIND-UNKNOWN", kind)
    enum_digest = hashlib.sha256(
        _canon(sorted(sealed_enumeration,
                      key=lambda e: e["emission_pos"])).encode()).hexdigest()
    values = {
        "kind": kind,
        "sealed_enumeration_digest": enum_digest,
        # the prelock form joins the TERMINAL enumeration; its producer passes that
        # set as the enumeration argument — same derivation, its own field name
        "terminal_enumeration_digest": enum_digest,
        "continuation_segment_digest":
            continuation_segment_digest(continuation_segment),
        "terminal_head": chain[terminal_pos]["running"],
        "freeze_signature_digest": freeze_signature_digest,
        "flagged_keys": sorted(map(list, flagged_keys)),
    }
    # the producer derives the body FIELD-FOR-FIELD from the per-kind form schema,
    # selecting BY KIND (GPT56-V115 F1) — never the flat union
    return {f: values[f] for f in FORM_SCHEMAS[kind]}


def export_pass(chain, gate, stores):
    """The closing verifier on the terminated path (CODEX-V114 F4): after a
    TERMINATED receipt every later gate pass verifies-and-consumes — the export must
    already sit beside the terminal checkpoint, its body regenerated from the schema
    and compared byte-for-byte. Exactly one export exists per run; a history with two
    successor-facing exports is malformed outright (GPT56-V113 F5)."""
    exports = [(pos, r) for pos, r in enumerate(chain)
               if r["k"] == "successor-export"]
    if len(exports) > 1:
        _r("DUPLICATE-EXPORT",
           "a history carrying two successor-facing exports is malformed outright")
    terminated = [(pos, r) for pos, r in enumerate(chain)
                  if r["k"] == "terminal-checkpoint"
                  and r.get("status") == "TERMINATED"]
    if not terminated:
        return
    tpos, trec = terminated[0]
    if not exports:
        _r("EXPORT-ABSENT",
           "a TERMINATED run's export is emitted inside the terminal checkpoint's "
           "own atomic commit; a later gate found none")
    epos, erec = exports[0]
    if epos not in set(trec["commit_set"]):
        _r("EXPORT-OUTSIDE-COMMIT",
           "the export does not sit inside the terminal checkpoint's atomic commit")
    body = erec["body"]
    kind = body.get("kind")
    if kind not in FORM_SCHEMAS:
        _r("EXPORT-KIND-UNKNOWN", f"{kind!r}")
    if kind != "successor-export":
        _r("EXPORT-KIND-MISMATCH",
           "a TERMINATED run's export carries the sealed successor-export form — "
           "the producer selects by the chain-derived kind, never by claim")
    want_fields = FORM_SCHEMAS[kind]
    if tuple(sorted(body)) != tuple(sorted(want_fields)):
        _r("EXPORT-SCHEMA-FIELD",
           f"export body fields {sorted(body)} do not match its kind's exact set "
           f"{sorted(want_fields)}")
    regen = regenerate_export(kind, chain, stores["sealed_enumeration"],
                              stores["continuation_segment"],
                              stores["freeze_signature_digest"],
                              stores["flagged_keys"], tpos)
    if _canon(regen) != _canon(body):
        _r("EXPORT-MISMATCH",
           "the regenerated body does not byte-match the emitted export")


# ------------------------------------------------------------------ composition
def verify_pass(chain, gate, constants, stores):
    """One gate pass over the chain as it then stands. Composes every obligation; on
    full acceptance returns the pass-record body this pass emits (predecessor-bound,
    its gate token); on any refusal raises without emitting — refusals block, they
    do not anchor."""
    if type(constants) is not ProvisionedConstants:
        _r("CONSTANTS-TYPE", "constants must be a ProvisionedConstants, exactly")
    for pos, rec in enumerate(chain):
        if rec["k"] == "haltrec":
            _r("POST-HALT-PASS",
               f"pos {pos}: a halt receipt stands; the exhaustion machinery admits "
               "no further gate pass")
    boundary = boundary_pass(chain, gate, constants)
    clock_pass(chain, constants)
    join_pass(chain, gate, constants)
    seam_pass(chain, stores.get("sealed_bindings", set()))
    catchall_pass(chain, gate, constants, stores["sealed_enumeration"],
                  stores["continuation_segment"], stores["explanations"],
                  stores["revisions"], stores["review_records"])
    store_log_pass(chain, stores["receipt_store"])
    passrec_rule(chain, constants)
    export_pass(chain, gate, stores)
    prior = [r for r in chain if r["k"] == "passrec"]
    predecessor = prior[-1]["body_digest"] if prior \
        else constants.bs2f_receipt_digest
    return {"k": "passrec", "gate": gate, "predecessor": predecessor,
            "boundary_position": boundary}


# ------------------------------------------------------------------ fixtures
ANCH = "a" * 64
BS2F = "b" * 64
FAILS = []
TOTAL = 0


def _consts(**over):
    kw = dict(first_epoch_anchor=ANCH, gate_pass_budget=100, pass_retry_max=3,
              decide_within_d=50, quantum_g=5, operation_set=("read", "write"),
              bs2f_receipt_digest=BS2F)
    kw.update(over)
    return ProvisionedConstants(**kw)


def _opening(epoch=1, reading=0, predecessor=ANCH, gap=None):
    return {"k": "epoch-opening", "epoch": epoch, "reading": reading,
            "predecessor": predecessor, "gap_declared": gap is not None,
            "gap_epochs": gap or []}


def _arr(row, seq, op="read", obj="o1", epoch=1, reading=10, binding=None,
         origin=None, digest=None):
    o = row if origin is None else origin
    return {"k": "arrival", "row": row, "origin_row": o, "frame_sequence": seq,
            "operation": op, "object_identity": obj,
            "request_digest": digest or request_digest(o, seq, op, obj),
            "binding": binding or f"b-{row}-{seq}", "epoch": epoch,
            "reading": reading}


def _term(key, row, op="read", obj="o1", outcome="TOUCH", epoch=1, reading=20,
          map_reading=None, refusal_class=None, binding=None):
    d = {"k": "termrec", "request_key": key, "row": row, "operation": op,
         "object_identity": obj, "outcome": outcome, "epoch": epoch,
         "reading": reading,
         "map_reading": reading if map_reading is None else map_reading,
         "binding": binding or f"b-{row}-1"}
    if refusal_class:
        d["refusal_class"] = refusal_class
    return d


def _bnd(gate, epoch=1, reading=20):
    return {"k": "verification-boundary", "gate": gate, "epoch": epoch,
            "reading": reading}


def _cls(gate, bpos, cc="ABORTED", epoch=1, reading=25):
    return {"k": "verification-close", "gate": gate, "boundary_position": bpos,
            "close_class": cc, "epoch": epoch, "reading": reading}


def _prec(gate, predecessor, epoch=1, reading=30, refusing=False):
    d = {"k": "passrec", "gate": gate, "predecessor": predecessor,
         "epoch": epoch, "reading": reading}
    if refusing:
        d["refusing"] = True
    return d


def _stores(**over):
    d = dict(sealed_enumeration=[], continuation_segment=[], explanations={},
             revisions={}, review_records={}, receipt_store=[],
             freeze_signature_digest="f" * 64, flagged_keys=[],
             sealed_bindings=set())
    d.update(over)
    return d


def expect(code, thunk):
    global TOTAL
    TOTAL += 1
    try:
        thunk()
    except Refusal as e:
        if e.code != code:
            FAILS.append(f"[{code}] refused with {e.code}")
        return
    except Exception as e:
        FAILS.append(f"[{code}] non-refusal {type(e).__name__}: {e}")
        return
    FAILS.append(f"[{code}] accepted")


def ok(label, thunk):
    global TOTAL
    TOTAL += 1
    try:
        return thunk()
    except Exception as e:
        FAILS.append(f"[{label}] refused: {e}")


def fixtures():
    C = _consts()
    o1 = _opening()
    bo1 = body_digest(o1)

    # ---- constants: absence refuses at the front door (the V115 lesson)
    expect("CONSTANT-MISSING", lambda: ProvisionedConstants(first_epoch_anchor=ANCH))
    expect("CONSTANT-NONE", lambda: _consts(quantum_g=None))
    expect("CONSTANT-EMPTY", lambda: _consts(operation_set=()))
    expect("CONSTANT-UNKNOWN", lambda: _consts(bonus=1))

    # ---- prefix / anchors
    clean = mkchain([o1, _arr("A", 1)])
    ok("clean prefix", lambda: verify_prefix(clean, 1))
    tam = mkchain([o1, _arr("A", 1)])
    tam[1]["running"] = "0" * 64
    expect("RUNNING-DIGEST-MISMATCH", lambda: verify_prefix(tam, 1))
    tam2 = mkchain([o1, _arr("A", 1)])
    tam2[1]["reading"] = 15  # rewrite without re-digesting
    expect("BODY-DIGEST-MISMATCH", lambda: verify_prefix(tam2, 1))
    anch = mkchain([o1, {"k": "external-anchor", "anchored_running": "c" * 64}])
    expect("ANCHOR-MISMATCH", lambda: verify_prefix(anch, 1))
    a_ok = mkchain([o1, {"k": "external-anchor",
                         "anchored_running": mkchain([o1])[0]["running"]}])
    ok("chain reaching its external anchor", lambda: verify_prefix(a_ok, 1))

    # ---- boundary / hold discipline
    expect("UNKNOWN-GATE",
           lambda: boundary_pass(mkchain([_bnd("BS-L")]), "BS-X", C))
    expect("BOUNDARY-OVER-OPEN",
           lambda: boundary_pass(
               mkchain([_bnd("BS-L"), _bnd("BS-L", reading=25)]), "BS-L", C))
    expect("NO-OPEN-BOUNDARY",
           lambda: boundary_pass(mkchain([o1]), "BS-L", C))
    expect("RELEASED-INTERVAL",
           lambda: boundary_pass(
               mkchain([_bnd("BS-L"), _arr("A", 1, reading=125)]), "BS-L", C))
    expect("MALFORMED-HOLD-ARRIVAL",
           lambda: boundary_pass(
               mkchain([_bnd("BS-L"), _arr("A", 1, reading=120)]), "BS-L", C))
    ch_ex = mkchain([_bnd("BS-L", reading=20), _cls("BS-L", 0, "ABORTED", reading=25),
                     _bnd("BS-L", reading=30), _cls("BS-L", 2, "EXPIRED", reading=35),
                     _bnd("BS-L", reading=40),
                     _cls("BS-L", 4, "ABORTED-BY-RESTART", reading=45),
                     _bnd("BS-L", reading=50)])
    expect("PASS-RETRY-EXHAUSTED", lambda: boundary_pass(ch_ex, "BS-L", C))
    # the reset control does REAL work (AGY ENV-V1 F1): two closes precede the pass
    # record and two follow — 4 unreset closes would exceed the cap of 3, so this
    # chain is accepted ONLY because the pass record resets the derived count
    ch_rst = mkchain([_bnd("BS-L", reading=20), _cls("BS-L", 0, "ABORTED", reading=25),
                      _bnd("BS-L", reading=30), _cls("BS-L", 2, "EXPIRED", reading=35),
                      _bnd("BS-L", reading=40), _prec("BS-L", BS2F, reading=45),
                      _bnd("BS-L", reading=50), _cls("BS-L", 6, "ABORTED", reading=55),
                      _bnd("BS-L", reading=60),
                      _cls("BS-L", 8, "ABORTED-BY-RESTART", reading=65),
                      _bnd("BS-L", reading=70)])
    assert ok("pass record resets the derived count (4 closes total, 2 since reset)",
              lambda: boundary_pass(ch_rst, "BS-L", C)) == 10
    # and one more close past the reset reaches the cap again — the count is the
    # POST-RESET closes, not zero forever
    ch_rst2 = mkchain(ch_rst[:10] + [
        _bnd("BS-L", reading=70), _cls("BS-L", 10, "EXPIRED", reading=75),
        _bnd("BS-L", reading=80)])
    expect("PASS-RETRY-EXHAUSTED", lambda: boundary_pass(ch_rst2, "BS-L", C))
    expect("CLOSE-GATE-MISMATCH",
           lambda: boundary_pass(
               mkchain([_bnd("BS-L"), _cls("BS-7F", 0, "ABORTED", reading=25)]),
               "BS-L", C))
    expect("CLOSE-GATE-MISMATCH",
           lambda: boundary_pass(
               mkchain([_bnd("BS-L"),
                        _cls("BS-7F", 0, "ABORTED-BY-RESTART", reading=25)]),
               "BS-L", C))
    expect("CLOSE-WITHOUT-BOUNDARY",
           lambda: boundary_pass(
               mkchain([_cls("BS-L", 0, "ABORTED", reading=25),
                        _bnd("BS-L", reading=30)]), "BS-L", C))
    expect("CLOSE-CLASS-UNKNOWN",
           lambda: boundary_pass(
               mkchain([_bnd("BS-L"), _cls("BS-L", 0, "WAVED", reading=25),
                        _bnd("BS-L", reading=30)]), "BS-L", C))
    expect("PASSREC-WITHOUT-BOUNDARY",
           lambda: boundary_pass(mkchain([_prec("BS-L", BS2F, reading=10),
                                          _bnd("BS-L", reading=20)]), "BS-L", C))
    expect("PASS-ABORTED-BY-TERMINATION",
           lambda: boundary_pass(
               mkchain([_bnd("BS-L"), {"k": "drain-start",
                                       "receipt_digest": "d" * 64,
                                       "epoch": 1, "reading": 25}]), "BS-L", C))
    expect("PASS-ABORTED-BY-TERMINATION",
           lambda: boundary_pass(
               mkchain([_bnd("BS-L"), {"k": "receipt-note",
                                       "receipt_digest": "d" * 64,
                                       "epoch": 1, "reading": 25}]), "BS-L", C))
    ch_reads = mkchain([_bnd("BS-L"),
                        {"k": "verification-read", "target": 0,
                         "boundary_position": 0},
                        {"k": "termrec", "joined_read": 1, "request_key": 0,
                         "row": "A", "operation": "read", "object_identity": "o1",
                         "outcome": "TOUCH", "epoch": 1, "reading": 25,
                         "map_reading": 25, "binding": "b-A-1"}])
    assert ok("pass-own reads excluded via typed joins",
              lambda: boundary_pass(ch_reads, "BS-L", C)) == 0
    # a stuffed read NOT bound to this pass's boundary is foreign — it must not
    # open a laundering channel for joined records (AGY ENV-V1 F5)
    expect("FOREIGN-RECORD-IN-HOLD",
           lambda: boundary_pass(
               mkchain([_bnd("BS-L"),
                        {"k": "verification-read", "target": 0,
                         "boundary_position": 99}]), "BS-L", C))
    expect("BOUNDARY-EPOCH-CHANGED",
           lambda: boundary_pass(
               mkchain([_bnd("BS-L"), _opening(2, 0, bo1)]), "BS-L", C))
    # the in-hold cross-epoch arrival branch is REACHABLE (AGY ENV-V1 F4): a
    # clock-malformed chain whose LAST clock-bearing record regresses to the
    # boundary's epoch slips the pre-loop check; standalone boundary_pass must
    # still refuse at the arrival itself
    expect("BOUNDARY-EPOCH-CHANGED",
           lambda: boundary_pass(
               mkchain([_bnd("BS-L"), _arr("A", 1, epoch=2, reading=25),
                        {"k": "drain-start", "receipt_digest": "d" * 64,
                         "epoch": 1, "reading": 30}]), "BS-L", C))
    expect("FOREIGN-RECORD-IN-HOLD",
           lambda: boundary_pass(
               mkchain([_bnd("BS-L"), {"k": "signed-cut"}]), "BS-L", C))

    # ---- clock pass
    expect("EPOCH-ROLLBACK",
           lambda: clock_pass(mkchain([o1, _opening(2, 5, bo1),
                                       _arr("A", 1, epoch=1, reading=10)]), C))
    expect("EPOCH-REUSE",
           lambda: clock_pass(
               mkchain([o1, _opening(2, 5, bo1),
                        _opening(2, 10, body_digest(_opening(2, 5, bo1)))]), C))
    expect("EPOCH-NOT-OPENED",
           lambda: clock_pass(mkchain([o1, _arr("A", 1, epoch=2)]), C))
    expect("EPOCH-NOT-OPENED", lambda: clock_pass(mkchain([_arr("A", 1)]), C))
    expect("READING-REGRESSION",
           lambda: clock_pass(mkchain([o1, _arr("A", 1, reading=10),
                                       _bnd("BS-L", reading=5)]), C))
    expect("OPENING-PREDECESSOR-MISMATCH",
           lambda: clock_pass(mkchain([o1, _opening(2, 5, "d" * 64)]), C))
    expect("EPOCH-GAP-UNDECLARED",
           lambda: clock_pass(mkchain([o1, _opening(3, 5, bo1)]), C))
    expect("EPOCH-GAP-MISDECLARED",
           lambda: clock_pass(mkchain([o1, _opening(3, 5, bo1, gap=[2, 4])]), C))
    ok("declared crash-consumed gap",
       lambda: clock_pass(mkchain([o1, _opening(4, 5, bo1, gap=[2, 3])]), C))
    expect("FIRST-EPOCH-UNANCHORED",
           lambda: clock_pass(mkchain([_opening(1, 0, "e" * 64)]), C))
    expect("OPENING-SCHEMA",
           lambda: clock_pass(mkchain([_opening(1, 0, ANCH, gap=[0])]), C))
    expect("OPENING-SCHEMA",
           lambda: clock_pass(mkchain([{"k": "epoch-opening", "epoch": 1,
                                        "reading": 0, "predecessor": ANCH,
                                        "gap_declared": False}]), C))
    ok("decision between clock-bearing records (scoping)",
       lambda: clock_pass(mkchain([o1, _arr("A", 1, reading=10),
                                   _term(1, "A", reading=15, map_reading=15),
                                   _bnd("BS-L", reading=20)]), C))
    expect("DECISION-ORDER",
           lambda: clock_pass(mkchain([o1, _arr("A", 1, reading=10),
                                       _arr("B", 1, reading=15),
                                       _term(2, "B", reading=20, map_reading=20,
                                             binding="b-B-1"),
                                       _term(1, "A", reading=25, map_reading=25)]),
                              C))
    expect("DECIDE-WITHIN-D",
           lambda: clock_pass(mkchain([o1, _arr("A", 1, reading=10),
                                       _term(1, "A", reading=65,
                                             map_reading=65)]), C))
    ok("head-budget overrun takes the catch-all at its turn (cascade)",
       lambda: clock_pass(mkchain([o1, _arr("A", 1, reading=10),
                                   _bnd("BS-L", reading=70),
                                   _term(1, "A", outcome="REFUSAL",
                                         refusal_class="REFUSED-UNCLASSIFIED",
                                         reading=70, map_reading=70)]), C))
    expect("READ-THEN-STALL",
           lambda: clock_pass(mkchain([o1, _arr("A", 1, reading=10),
                                       _bnd("BS-L", reading=20),
                                       _term(1, "A", reading=20,
                                             map_reading=15)]), C))
    expect("UNQUANTIZED-READING",
           lambda: clock_pass(mkchain([o1, _arr("A", 1, reading=12)]), C))
    # composite-defect ordering is DOCUMENTED first-refusal semantics (AGY ENV-V1
    # F6): an unquantized regression reports quantization; alias + bad digest
    # reports the alias — the gate blocks either way, and the order is asserted
    expect("UNQUANTIZED-READING",
           lambda: clock_pass(mkchain([o1, _arr("A", 1, reading=15),
                                       _bnd("BS-L", reading=12)]), C))
    expect("ROW-ALIAS",
           lambda: join_pass(mkchain([o1, _arr("A", 1, origin="B",
                                               digest="1" * 64)]), "BS-L", C))
    expect("GAP-EPOCH-NOT-EMPTY",
           lambda: clock_pass(mkchain([o1, _opening(4, 5, bo1, gap=[2, 3]),
                                       {"k": "termrec", "request_key": 0,
                                        "row": "A", "operation": "read",
                                        "object_identity": "o1",
                                        "outcome": "TOUCH", "epoch": 2,
                                        "reading": 10, "map_reading": 10,
                                        "binding": "x"}]), C))

    # ---- join pass
    J = lambda ch, gate="BS-L": join_pass(ch, gate, C)
    expect("REPLAYED-FRAME",
           lambda: J(mkchain([o1, _arr("A", 1),
                              _arr("A", 1, reading=15, binding="b2")])))
    ok("retry at a strictly higher sequence",
       lambda: J(mkchain([o1, _arr("A", 1), _arr("A", 2, reading=15)])))
    expect("SEQUENCE-REGRESSION",
           lambda: J(mkchain([o1, _arr("A", 2, binding="x1"),
                              _arr("A", 1, reading=15, binding="x2")])))
    ok("equal sequences on different rows",
       lambda: J(mkchain([o1, _arr("A", 1), _arr("B", 1, reading=15)])))
    expect("DIGEST-NOT-RECOMPUTED",
           lambda: J(mkchain([o1, _arr("A", 1, digest="1" * 64)])))
    expect("ROW-ALIAS", lambda: J(mkchain([o1, _arr("A", 1, origin="B")])))
    expect("TERMINAL-DANGLING",
           lambda: J(mkchain([o1, _arr("A", 1), _term(7, "A")])))
    expect("TERMINAL-DANGLING",
           lambda: J(mkchain([o1, _arr("A", 1), _term(0, "A")])))
    expect("KEY-BINDING-MISMATCH",
           lambda: J(mkchain([o1, _arr("A", 1), _term(1, "A", binding="wrong")])))
    expect("TWO-TERMINALS-ONE-KEY",
           lambda: J(mkchain([o1, _arr("A", 1), _term(1, "A"),
                              _term(1, "A", reading=25)])))
    expect("BINDING-REUSED",
           lambda: J(mkchain([o1, _arr("A", 1),
                              _arr("A", 2, reading=15, binding="b-A-1")])))
    expect("IDENTITY-SWAP",
           lambda: J(mkchain([o1, _arr("A", 1), _term(1, "A", op="write")])))
    expect("OVERDUE-ORPHAN",
           lambda: J(mkchain([o1, _arr("A", 1, reading=10),
                              _bnd("BS-L", reading=70)])))
    for g in ("BS-L", "LOCK-OPENING", "BS-7F", "BS-V"):
        ok(f"within-deadline PENDING admissible at {g}",
           lambda g=g: J(mkchain([o1, _arr("A", 1, reading=10),
                                  _bnd(g, reading=20)]), g))
    expect("PENDING-AT-DISCLOSURE",
           lambda: J(mkchain([o1, _arr("A", 1, reading=10),
                              _bnd("DISCLOSURE", reading=20)]), "DISCLOSURE"))
    expect("OVERDUE-ORPHAN",
           lambda: J(mkchain([o1, _arr("A", 1, reading=10),
                              _opening(2, 5, bo1)])))
    ok("post-signed-cut decision with its continuation entry",
       lambda: J(mkchain([o1, _arr("A", 1), {"k": "signed-cut"},
                          _term(1, "A"),
                          {"k": "bindmap-entry", "request_key": 1,
                           "binding": "b-A-1"}])))
    expect("CONTINUATION-ENTRY-MISSING",
           lambda: J(mkchain([o1, _arr("A", 1), {"k": "signed-cut"},
                              _term(1, "A")])))
    ok("frame residues carry no obligation",
       lambda: J(mkchain([o1] + [{"k": "frame-residue", "residue": r}
                                 for r in FRAME_RESIDUES])))
    expect("RESIDUE-UNKNOWN",
           lambda: J(mkchain([o1, {"k": "frame-residue", "residue": "alien"}])))
    tc = lambda cs, fm: {"k": "terminal-checkpoint", "status": "RUNNING",
                         "commit_set": cs, "failed_members": fm, "epoch": 1,
                         "reading": 25}
    ok("listed member with its in-commit refusal event",
       lambda: J(mkchain([o1, _arr("A", 1),
                          _term(1, "A", outcome="REFUSAL"), tc([2], [1])])))
    expect("LISTED-WITHOUT-EVENT",
           lambda: J(mkchain([o1, _arr("A", 1),
                              _term(1, "A", outcome="REFUSAL"), tc([], [1])])))
    expect("EVENT-UNLISTED",
           lambda: J(mkchain([o1, _arr("A", 1),
                              _term(1, "A", outcome="REFUSAL"), tc([2], [])])))
    # the refusal events ride the commit IMMEDIATELY PRECEDING the checkpoint —
    # an in-commit refusal separated from the checkpoint by another record is
    # refused (AGY ENV-V1 F3: the obligation the first build missed)
    expect("COMMIT-EVENTS-NOT-ADJACENT",
           lambda: J(mkchain([o1, _arr("A", 1),
                              _term(1, "A", outcome="REFUSAL"),
                              {"k": "bindmap-entry", "request_key": 1,
                               "binding": "b-A-1"},
                              tc([2], [1])])))
    ok("adjacent two-member refusal block",
       lambda: J(mkchain([o1, _arr("A", 1), _arr("B", 1, reading=15),
                          _term(1, "A", outcome="REFUSAL"),
                          _term(2, "B", outcome="REFUSAL", reading=25,
                                map_reading=25, binding="b-B-1"),
                          {"k": "terminal-checkpoint", "status": "RUNNING",
                           "commit_set": [3, 4], "failed_members": [1, 2],
                           "epoch": 1, "reading": 30}])))
    ok("issuance bindings live as continuation entries",
       lambda: seam_pass(mkchain([{"k": "bindmap-entry", "request_key": 1,
                                   "binding": "x", "issuance": True}]), set()))
    expect("SEAM-VIOLATION",
           lambda: seam_pass(mkchain([{"k": "bindmap-entry", "request_key": 1,
                                       "binding": "x", "issuance": True}]),
                             {"x"}))

    # ---- catch-all pass
    def CA(entries, gate="BS-7F", chain=None, explanations=None, revisions=None,
           reviews=None):
        ch = chain if chain is not None else mkchain(
            [o1, _arr("A", 1),
             _term(1, "A", outcome="REFUSAL",
                   refusal_class="REFUSED-UNCLASSIFIED")])
        return catchall_pass(ch, gate, C, entries, [], explanations or {},
                             revisions or {}, reviews or {})
    E = lambda pos=2, key=("A", "read"), disp="EXPLAINED", **kw: dict(
        {"emission_pos": pos, "class_key": list(key), "disposition": disp}, **kw)
    expect("UNENUMERATED-EMISSION", lambda: CA([]))
    expect("ORPHAN-ENTRY", lambda: CA([E(), E(pos=0)]))
    expect("DUPLICATE-ENTRY", lambda: CA([E(), E()]))
    expect("CLASS-KEY-MISMATCH", lambda: CA([E(key=("A", "write"))]))
    ok("clean EXPLAINED with resolving reference",
       lambda: CA([E(explanation_ref="x1")], explanations={"x1": b"art"}))
    expect("DANGLING-EXPLANATION", lambda: CA([E(explanation_ref="nope")]))
    ch2 = mkchain([o1, _arr("A", 1),
                   _term(1, "A", outcome="REFUSAL",
                         refusal_class="REFUSED-UNCLASSIFIED"),
                   _arr("A", 2, reading=25),
                   _term(3, "A", outcome="REFUSAL", reading=30, map_reading=30,
                         refusal_class="REFUSED-UNCLASSIFIED",
                         binding="b-A-2")])
    expect("SECOND-EXPLAINED",
           lambda: CA([E(explanation_ref="x1"),
                       E(pos=4, explanation_ref="x1")], chain=ch2,
                      explanations={"x1": b"art"}))
    # the accepted recurrence path (AGY ENV-V1 F2's missing positive control): the
    # second occurrence takes NAMED-AS-DEFECT with a proper re-derivation and the
    # pass ACCEPTS — proving SECOND-EXPLAINED refuses the disposition, not recurrence
    ok("second occurrence NAMED-AS-DEFECT admissible",
       lambda: CA([E(explanation_ref="x1"),
                   E(pos=4, disp="NAMED-AS-DEFECT", revision_digest="r2",
                     prior_revision_digest="r1")], chain=ch2,
                  explanations={"x1": b"art"},
                  revisions={"r2": "TOKEN: t1 := the (A,read) overrun family\n"
                                   "NAMES-CLASS: (A,read) AS t1"}))
    expect("REVISION-ABSENT",
           lambda: CA([E(disp="NAMED-AS-DEFECT", revision_digest="r9")]))
    expect("REVISION-UNCHANGED",
           lambda: CA([E(disp="NAMED-AS-DEFECT", revision_digest="r1",
                         prior_revision_digest="r1")],
                      revisions={"r1": "TOKEN: t1 := x"}))
    expect("NAMING-TEMPLATE-ABSENT",
           lambda: CA([E(disp="NAMED-AS-DEFECT", revision_digest="r1",
                         prior_revision_digest="r0")],
                      revisions={"r1": "TOKEN: t1 := x"}))
    expect("TOKEN-NOT-MEMBER",
           lambda: CA([E(disp="NAMED-AS-DEFECT", revision_digest="r1",
                         prior_revision_digest="r0")],
                      revisions={"r1": "NAMES-CLASS: (A,read) AS ghost"}))
    expect("NAMING-VACUOUS",
           lambda: CA([E(disp="NAMED-AS-DEFECT", revision_digest="r1",
                         prior_revision_digest="r0")],
                      revisions={"r1": "TOKEN: t1 := generic words\n"
                                       "NAMES-CLASS: (A,read) AS t1"}))
    ok("naming template parsed: key inside the named token's definition",
       lambda: CA([E(disp="NAMED-AS-DEFECT", revision_digest="r2",
                     prior_revision_digest="r1")],
                  revisions={"r2": "TOKEN: t1 := the (A,read) overrun family\n"
                                   "NAMES-CLASS: (A,read) AS t1"}))
    expect("DISPOSITION-UNKNOWN", lambda: CA([E(disp="WAVED")]))
    chd = mkchain([o1, _arr("A", 1, op="delete"),
                   _term(1, "A", op="delete", outcome="REFUSAL",
                         refusal_class="REFUSED-UNCLASSIFIED")])
    expect("OPERATION-NOT-CLOSED",
           lambda: CA([E(key=("A", "delete"))], chain=chd))
    chm = mkchain([o1, _arr("A", 1),
                   _term(1, "A", outcome="REFUSAL",
                         refusal_class="REFUSED-INTEGRITY-MISMATCH")])
    ok("mismatch logged-and-continued admissible pre-freeze",
       lambda: CA([E(disp="LOGGED-AND-CONTINUED", review_ref="rv1")], chain=chm))
    expect("MISMATCH-UNREVIEWED-AT-FREEZE",
           lambda: CA([E(disp="LOGGED-AND-CONTINUED", review_ref="rv1")],
                      gate="DISCLOSURE", chain=chm))
    ok("reviewed mismatch admissible at the freeze",
       lambda: CA([E(disp="LOGGED-AND-CONTINUED", review_ref="rv1")],
                  gate="DISCLOSURE", chain=chm, reviews={"rv1": b"review"}))
    expect("MISMATCH-DISPOSITION",
           lambda: CA([E(disp="EXPLAINED", explanation_ref="x1")], chain=chm,
                      explanations={"x1": b"art"}))

    # ---- store↔log pass
    D64 = "d" * 64
    expect("ORPHAN-RECEIPT",
           lambda: store_log_pass(mkchain([o1]),
                                  [{"receipt_digest": D64,
                                    "status": "TERMINATED"}]))
    ok("receipt with its drain-start record",
       lambda: store_log_pass(
           mkchain([o1, {"k": "drain-start", "receipt_digest": D64,
                         "epoch": 1, "reading": 10}]),
           [{"receipt_digest": D64, "status": "TERMINATED"}]))
    ok("receipt with its receipt-note record",
       lambda: store_log_pass(
           mkchain([o1, {"k": "receipt-note", "receipt_digest": D64,
                         "epoch": 1, "reading": 10}]),
           [{"receipt_digest": D64, "status": "TERMINATED"}]))
    expect("NOTE-FIRST-INVERSION",
           lambda: store_log_pass(
               mkchain([o1, {"k": "receipt-note", "receipt_digest": "e" * 64,
                             "epoch": 1, "reading": 10}]), []))

    # ---- pass records
    p1 = _prec("BS-L", BS2F, reading=10)
    expect("DUPLICATE-GATE-PASS",
           lambda: passrec_rule(mkchain([p1, _prec("BS-L", body_digest(p1),
                                                   reading=15)]), C))
    expect("PASSREC-FORK",
           lambda: passrec_rule(mkchain([p1, _prec("LOCK-OPENING", BS2F,
                                                   reading=15)]), C))
    expect("FIRST-PREDECESSOR",
           lambda: passrec_rule(mkchain([_prec("BS-L", "9" * 64,
                                               reading=10)]), C))
    expect("PREDECESSOR-BROKEN",
           lambda: passrec_rule(mkchain([p1, _prec("LOCK-OPENING", "8" * 64,
                                                   reading=15)]), C))
    expect("REFUSING-PASS-RECORD",
           lambda: passrec_rule(mkchain([_prec("BS-L", BS2F, reading=10,
                                               refusing=True)]), C))
    ok("predecessor-bound pass-record sequence",
       lambda: passrec_rule(mkchain([p1, _prec("LOCK-OPENING", body_digest(p1),
                                               reading=15)]), C))

    # ---- successor export
    TC = {"k": "terminal-checkpoint", "status": "TERMINATED",
          "commit_set": [2], "failed_members": [], "epoch": 1, "reading": 10}
    base = mkchain([o1, TC])
    S = _stores()
    regen = regenerate_export("successor-export", base, [], [], "f" * 64, [], 1)
    full = mkchain([o1, TC, {"k": "successor-export", "body": regen}])
    ok("terminated-path export verify-and-consume",
       lambda: export_pass(full, "BS-V", S))
    expect("EXPORT-ABSENT", lambda: export_pass(base, "BS-V", S))
    bad = dict(regen, flagged_keys=[["A", "read"]])
    expect("EXPORT-MISMATCH",
           lambda: export_pass(mkchain([o1, TC, {"k": "successor-export",
                                                 "body": bad}]), "BS-V", S))
    expect("DUPLICATE-EXPORT",
           lambda: export_pass(
               mkchain([o1, dict(TC, commit_set=[2, 3]),
                        {"k": "successor-export", "body": regen},
                        {"k": "successor-export", "body": regen}]), "BS-V", S))
    short = {f: regen[f] for f in regen if f != "freeze_signature_digest"}
    short["kind"] = "successor-export"
    expect("EXPORT-SCHEMA-FIELD",
           lambda: export_pass(mkchain([o1, TC, {"k": "successor-export",
                                                 "body": short}]), "BS-V", S))
    pl = regenerate_export("successor-export-prelock", base, [], [], "f" * 64,
                           [], 1)
    expect("EXPORT-KIND-MISMATCH",
           lambda: export_pass(mkchain([o1, TC, {"k": "successor-export",
                                                 "body": pl}]), "BS-V", S))
    expect("EXPORT-OUTSIDE-COMMIT",
           lambda: export_pass(
               mkchain([o1, dict(TC, commit_set=[9]),
                        {"k": "successor-export", "body": regen}]), "BS-V", S))

    # ---- composition end-to-end
    e2e = mkchain([o1, _arr("A", 1, reading=10), _term(1, "A"),
                   _bnd("BS-L", reading=20)])
    body = ok("clean BS-L pass emits its predecessor-bound record",
              lambda: verify_pass(e2e, "BS-L", C, _stores()))
    if body is not None and (body["gate"] != "BS-L" or body["predecessor"] != BS2F
                             or body["boundary_position"] != 3):
        FAILS.append("[e2e] pass-record body malformed")
    expect("POST-HALT-PASS",
           lambda: verify_pass(mkchain([{"k": "haltrec"}, _bnd("BS-L")]),
                               "BS-L", C, _stores()))
    expect("CONSTANTS-TYPE",
           lambda: verify_pass(e2e, "BS-L", {"gate_pass_budget": 100},
                               _stores()))
    return FAILS, TOTAL


if __name__ == "__main__":
    fails, total = fixtures()
    for x in fails:
        print("FIXTURE FAIL:", x)
    print(f"enumeration verifier fixtures: {total - len(fails)}/{total} green")
    sys.exit(1 if fails else 0)
