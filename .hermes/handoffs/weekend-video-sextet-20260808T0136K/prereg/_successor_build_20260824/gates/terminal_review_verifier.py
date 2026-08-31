#!/usr/bin/env python3
"""terminal_review_verifier — REQUIRED build item (the P9 machinery of
TERMINAL_SIGNATURE_RULING_20260830.md, taken in its V101 recomputation-hardened
form). At run end the principal performs ONE signing ceremony that does not sign a
digest the enumerator presents: it RECOMPUTES the terminal head from the chain bytes
and the anchor chain under THIS pinned verifier, then signs the canonical
domain-tagged TERMINAL-REVIEW body. The two forms mirror the authoritative
FORM_SCHEMAS registry (ref/gen_string_field_registry.py) and the producer SELECTS BY
THE CHAIN-DERIVED ENDING, never by claim (GPT56-V115 F1):

  terminal-review-terminated: (kind, terminal_checkpoint_digest,
      drain_start_position, recomputed_head, verifier_digest, transcript_digest)
  terminal-review-completed:  (kind, disclosure_record_digest,
      successor_export_digest, recomputed_head, verifier_digest, transcript_digest)

On the COMPLETED path the ceremony is the successor export's CLOSING VERIFIER
(CODEX-V114 F4: disclosure is the last gate, so every-later-pass was an empty
promise there): the export must exist, be UNIQUE, sit inside the disclosure pass
record's own atomic commit, and byte-match its schema regeneration against the
chain — absent, duplicate, displaced or mismatched exports refuse BEFORE the
principal signs. On the TERMINATED path the body binds the terminal checkpoint and
its drain-start position, and the checkpoint's receipt must be present in the
receipt store (the ceremony's receipt-vs-store check, per the ruling).

The record model is enumeration_verifier's (imported, not twinned — a second
digest/prefix implementation would be the divergent-copy defect); both files are
separately pinned and the ceremony script prints both digests for the principal's
own OS-tool comparison against the printed pins.

v2 after AGY TRV-V1 (DEFECTIVE, 2): the ENDING IS TERMINAL IN POSITION — after
the ending record, only members of the ending's own atomic commit may follow, so
an enumerator cannot append post-termination garbage and have the principal sign
a head that authorizes it (TRAILING-RECORDS); and a receipt has EXACTLY ONE
drain-start (Row B's ordering obligation makes the drain-start the receipt's next
chain append — a second one is malformed history, DUPLICATE-DRAIN-START, which
also closes the earliest-fake-wins selection agy noted). The ceremony script's
refusal path is repaired in its own v2: every refusal exits 2 with the refusal
line in the transcript, never an unhandled crash.

v3 after AGY TRV-V2 (DEFECTIVE, 3, all in the v2-changed regions): the ending's
commit_set must name REAL chain positions — a fictional member no longer lets a
partial commit pass (ENDING-COMMIT-MALFORMED); the chain must OPEN with an epoch
opening (CHAIN-UNMOORED — clock lawfulness stays the gates' job, but the ceremony
will not sign a rootless history); and the ceremony's late-refusal path no longer
rewrites a transcript whose digest was already printed — a digested artifact is
append-never-rewrite, so the refusal lands in a sidecar and the printed digest
stays true (repaired in the ceremony's v3)."""
import hashlib
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import enumeration_verifier as ev  # noqa: E402

HEX64 = re.compile(r"[0-9a-f]{64}\Z")

REVIEW_FORM_SCHEMAS = {
    "terminal-review-terminated": (
        "kind", "terminal_checkpoint_digest", "drain_start_position",
        "recomputed_head", "verifier_digest", "transcript_digest"),
    "terminal-review-completed": (
        "kind", "disclosure_record_digest", "successor_export_digest",
        "recomputed_head", "verifier_digest", "transcript_digest"),
}


class ReviewRefusal(ValueError):
    def __init__(self, code, msg):
        self.code = code
        super().__init__(f"{code}: {msg}")


def _r(code, msg):
    raise ReviewRefusal(code, msg)


def recompute_terminal_head(chain):
    """The ruling's core act: the head is RECOMPUTED from the chain bytes under the
    running-digest discipline with external anchors — never accepted from the
    enumerator's presentation."""
    if not chain:
        _r("EMPTY-CHAIN", "no chain, no head")
    ev.verify_prefix(chain, len(chain) - 1)
    return chain[-1]["running"]


def derive_ending(chain):
    """The ending is CHAIN-DERIVED: exactly one of a TERMINATED terminal checkpoint
    or a DISCLOSURE pass record. Both, neither, or a duplicated ending refuses."""
    terminated = [(pos, r) for pos, r in enumerate(chain)
                  if r["k"] == "terminal-checkpoint"
                  and r.get("status") == "TERMINATED"]
    disclosed = [(pos, r) for pos, r in enumerate(chain)
                 if r["k"] == "passrec" and r.get("gate") == "DISCLOSURE"]
    if terminated and disclosed:
        _r("AMBIGUOUS-ENDING",
           "both a TERMINATED checkpoint and a disclosure pass record stand")
    if len(terminated) > 1:
        _r("AMBIGUOUS-ENDING", "two TERMINATED checkpoints in one history")
    if len(disclosed) > 1:
        _r("AMBIGUOUS-ENDING", "two disclosure pass records in one history")
    if terminated:
        ending = ("TERMINATED", terminated[0][0])
    elif disclosed:
        ending = ("COMPLETED", disclosed[0][0])
    else:
        _r("NO-ENDING", "the run has not ended; there is nothing to sign")
    # THE CHAIN OPENS WITH ITS EPOCH OPENING (AGY TRV-V2 F2): a chain whose
    # first record is not an opening is unmoored — clock lawfulness belongs to
    # the five gates, but the ceremony will not sign a history with no root
    if chain[0]["k"] != "epoch-opening":
        _r("CHAIN-UNMOORED",
           "the chain does not open with an epoch opening; the principal does "
           "not sign an unmoored history")
    # THE ENDING IS TERMINAL IN POSITION (AGY TRV-V1 F1): the head the principal
    # signs covers every chain byte, so nothing may follow the ending except the
    # ending's own atomic commit — trailing garbage would be signed into
    # authorization otherwise. The commit_set itself must name REAL positions
    # (AGY TRV-V2 F1: fictional members made a partial commit pass silently)
    pos = ending[1]
    raw_commit = chain[pos].get("commit_set", ())
    for p in raw_commit:
        if type(p) is not int or p < 0 or p >= len(chain):
            _r("ENDING-COMMIT-MALFORMED",
               f"commit_set member {p!r} is not an existing chain position")
    commit = set(raw_commit)
    for p in range(pos + 1, len(chain)):
        if p not in commit:
            _r("TRAILING-RECORDS",
               f"pos {p}: a record follows the ending outside its atomic "
               "commit — the run ended, history does not continue")
    return ending


def validate_review_body(body):
    kind = body.get("kind")
    if kind not in REVIEW_FORM_SCHEMAS:
        _r("REVIEW-KIND-UNKNOWN", f"{kind!r}")
    want = REVIEW_FORM_SCHEMAS[kind]
    if tuple(sorted(body)) != tuple(sorted(want)):
        _r("REVIEW-SCHEMA-FIELD",
           f"body fields {sorted(body)} do not match the {kind} exact set "
           f"{sorted(want)}")
    return body


def build_review_body(chain, stores, verifier_digest, transcript_digest):
    """Constructs the exact per-kind body from the chain-derived ending. Every value
    is recomputed or store-checked here; nothing is accepted from a presentation."""
    for label, d in (("verifier_digest", verifier_digest),
                     ("transcript_digest", transcript_digest)):
        if type(d) is not str or not HEX64.match(d):
            _r("REVIEW-DIGEST-MALFORMED", f"{label} is not 64 lowercase hex")
    head = recompute_terminal_head(chain)
    ending, pos = derive_ending(chain)
    if ending == "TERMINATED":
        tc = chain[pos]
        receipt = tc.get("receipt_digest")
        if receipt is None:
            _r("RECEIPT-DIGEST-MISSING",
               "the TERMINATED checkpoint carries no receipt digest")
        stored = {r["receipt_digest"] for r in stores["receipt_store"]
                  if r["status"] == "TERMINATED"}
        if receipt not in stored:
            _r("RECEIPT-NOT-IN-STORE",
               "the ceremony's receipt-vs-store check fails: the checkpoint's "
               "receipt is absent from the receipt store")
        drains = [p for p, r in enumerate(chain)
                  if r["k"] == "drain-start" and r["receipt_digest"] == receipt]
        if not drains:
            _r("DRAIN-START-MISSING",
               "no drain-start on the chain binds the checkpoint's receipt")
        if len(drains) > 1:
            _r("DUPLICATE-DRAIN-START",
               f"positions {drains}: Row B's ordering obligation makes the "
               "drain-start the receipt's next chain append — a second one is "
               "malformed history (AGY TRV-V1: the earliest-fake-wins risk)")
        values = {
            "kind": "terminal-review-terminated",
            "terminal_checkpoint_digest": tc["body_digest"],
            "drain_start_position": drains[0],
            "recomputed_head": head,
            "verifier_digest": verifier_digest,
            "transcript_digest": transcript_digest,
        }
    else:
        disc = chain[pos]
        exports = [(p, r) for p, r in enumerate(chain)
                   if r["k"] == "successor-export"]
        if not exports:
            _r("EXPORT-ABSENT-AT-CEREMONY",
               "a COMPLETED run's export rides the disclosure commit; the closing "
               "verifier found none — the principal does not sign over its absence")
        if len(exports) > 1:
            _r("DUPLICATE-EXPORT",
               "a history carrying two successor-facing exports is malformed "
               "outright")
        epos, erec = exports[0]
        if epos not in set(disc.get("commit_set", ())):
            _r("EXPORT-OUTSIDE-COMMIT",
               "the export does not sit inside the disclosure pass record's own "
               "atomic commit")
        regen = ev.regenerate_export(
            "successor-export", chain, stores["sealed_enumeration"],
            stores["continuation_segment"], stores["freeze_signature_digest"],
            stores["flagged_keys"], pos)
        if ev._canon(regen) != ev._canon(erec["body"]):
            _r("EXPORT-MISMATCH",
               "the regenerated export does not byte-match the emitted body")
        values = {
            "kind": "terminal-review-completed",
            "disclosure_record_digest": disc["body_digest"],
            "successor_export_digest": erec["body_digest"],
            "recomputed_head": head,
            "verifier_digest": verifier_digest,
            "transcript_digest": transcript_digest,
        }
    body = {f: values[f] for f in REVIEW_FORM_SCHEMAS[values["kind"]]}
    return validate_review_body(body)


def signing_bytes(body):
    """The exact bytes the principal signs: the domain-tagged canonical body under
    the registry's terminal-review kind. Deterministic by construction."""
    validate_review_body(body)
    return b"NMPR1:terminal-review:" + ev._canon(body).encode()


# ------------------------------------------------------------------ fixtures
FAILS = []
TOTAL = 0


def expect(code, thunk):
    global TOTAL
    TOTAL += 1
    try:
        thunk()
    except ReviewRefusal as e:
        if e.code != code:
            FAILS.append(f"[{code}] refused with {e.code}")
        return
    except ev.Refusal as e:
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
    D64 = "d" * 64
    V64 = "e" * 64
    T64 = "f" * 64
    o1 = {"k": "epoch-opening", "epoch": 1, "reading": 0, "predecessor": "a" * 64,
          "gap_declared": False, "gap_epochs": []}
    store = [{"receipt_digest": D64, "status": "TERMINATED"}]
    stores_t = dict(receipt_store=store, sealed_enumeration=[],
                    continuation_segment=[], freeze_signature_digest="9" * 64,
                    flagged_keys=[])

    # terminated path, clean
    term_chain = ev.mkchain([
        o1,
        {"k": "drain-start", "receipt_digest": D64, "epoch": 1, "reading": 10},
        {"k": "terminal-checkpoint", "status": "TERMINATED",
         "receipt_digest": D64, "commit_set": [], "failed_members": [],
         "epoch": 1, "reading": 15},
    ])
    body = ok("terminated body builds",
              lambda: build_review_body(term_chain, stores_t, V64, T64))
    if body is not None:
        if body["kind"] != "terminal-review-terminated" or \
                body["drain_start_position"] != 1 or \
                body["terminal_checkpoint_digest"] != term_chain[2]["body_digest"] \
                or body["recomputed_head"] != term_chain[-1]["running"]:
            FAILS.append("[terminated body] wrong values")
    # determinism: same inputs, identical signing bytes
    global TOTAL
    TOTAL += 1
    b1 = build_review_body(term_chain, stores_t, V64, T64)
    b2 = build_review_body(term_chain, stores_t, V64, T64)
    if signing_bytes(b1) != signing_bytes(b2):
        FAILS.append("[determinism] same inputs, different signing bytes")
    # transcript sensitivity: a different transcript digest changes the bytes
    TOTAL += 1
    b3 = build_review_body(term_chain, stores_t, V64, "0" * 64)
    if signing_bytes(b1) == signing_bytes(b3):
        FAILS.append("[transcript binding] transcript digest did not bind")

    expect("RECEIPT-NOT-IN-STORE",
           lambda: build_review_body(term_chain, dict(stores_t, receipt_store=[]),
                                     V64, T64))
    no_drain = ev.mkchain([
        o1,
        {"k": "terminal-checkpoint", "status": "TERMINATED",
         "receipt_digest": D64, "commit_set": [], "failed_members": [],
         "epoch": 1, "reading": 15},
    ])
    expect("DRAIN-START-MISSING",
           lambda: build_review_body(no_drain, stores_t, V64, T64))
    no_receipt = ev.mkchain([
        o1,
        {"k": "terminal-checkpoint", "status": "TERMINATED",
         "commit_set": [], "failed_members": [], "epoch": 1, "reading": 15},
    ])
    expect("RECEIPT-DIGEST-MISSING",
           lambda: build_review_body(no_receipt, stores_t, V64, T64))
    expect("REVIEW-DIGEST-MALFORMED",
           lambda: build_review_body(term_chain, stores_t, "not-hex", T64))
    expect("REVIEW-DIGEST-MALFORMED",
           lambda: build_review_body(term_chain, stores_t, V64, "ABC"))

    # head recomputation catches tampering (custody, not presentation)
    tampered = ev.mkchain([o1, {"k": "drain-start", "receipt_digest": D64,
                                "epoch": 1, "reading": 10}])
    tampered[1]["running"] = "0" * 64
    expect("RUNNING-DIGEST-MISMATCH",
           lambda: recompute_terminal_head(tampered))
    expect("EMPTY-CHAIN", lambda: recompute_terminal_head([]))

    # endings
    expect("NO-ENDING", lambda: derive_ending(ev.mkchain([o1])))
    both = ev.mkchain([
        o1,
        {"k": "terminal-checkpoint", "status": "TERMINATED",
         "receipt_digest": D64, "commit_set": [], "failed_members": [],
         "epoch": 1, "reading": 10},
        {"k": "passrec", "gate": "DISCLOSURE", "predecessor": "b" * 64,
         "epoch": 1, "reading": 15},
    ])
    expect("AMBIGUOUS-ENDING", lambda: derive_ending(both))
    twotc = ev.mkchain([
        o1,
        {"k": "terminal-checkpoint", "status": "TERMINATED",
         "receipt_digest": D64, "commit_set": [], "failed_members": [],
         "epoch": 1, "reading": 10},
        {"k": "terminal-checkpoint", "status": "TERMINATED",
         "receipt_digest": D64, "commit_set": [], "failed_members": [],
         "epoch": 1, "reading": 15},
    ])
    expect("AMBIGUOUS-ENDING", lambda: derive_ending(twotc))

    # the ending is terminal in position (AGY TRV-V1 F1): trailing garbage after
    # the checkpoint, outside its commit, refuses before anything gets signed
    expect("TRAILING-RECORDS",
           lambda: build_review_body(ev.mkchain([
               o1,
               {"k": "drain-start", "receipt_digest": D64, "epoch": 1,
                "reading": 10},
               {"k": "terminal-checkpoint", "status": "TERMINATED",
                "receipt_digest": D64, "commit_set": [], "failed_members": [],
                "epoch": 1, "reading": 15},
               {"k": "bindmap-entry", "request_key": 1, "binding": "x"},
           ]), stores_t, V64, T64))
    # exactly one drain-start per receipt (Row B's ordering obligation)
    expect("DUPLICATE-DRAIN-START",
           lambda: build_review_body(ev.mkchain([
               o1,
               {"k": "drain-start", "receipt_digest": D64, "epoch": 1,
                "reading": 10},
               {"k": "drain-start", "receipt_digest": D64, "epoch": 1,
                "reading": 15},
               {"k": "terminal-checkpoint", "status": "TERMINATED",
                "receipt_digest": D64, "commit_set": [], "failed_members": [],
                "epoch": 1, "reading": 20},
           ]), stores_t, V64, T64))

    # completed path: the ceremony as the export's closing verifier
    def completed_chain(with_export=True, in_commit=True, body_override=None,
                        extra_export=False):
        if not with_export:
            commit = []
        elif extra_export:
            commit = [2, 3]
        else:
            commit = [2] if in_commit else []
        base = [o1, {"k": "passrec", "gate": "DISCLOSURE",
                     "predecessor": "b" * 64, "epoch": 1, "reading": 10,
                     "commit_set": commit}]
        pre = ev.mkchain(base)
        regen = ev.regenerate_export("successor-export", pre, [], [],
                                     "9" * 64, [], 1)
        if body_override is not None:
            regen = body_override(regen)
        recs = list(base)
        if with_export:
            recs.append({"k": "successor-export", "body": regen})
        if extra_export:
            recs.append({"k": "successor-export", "body": regen})
        return ev.mkchain(recs)

    stores_c = dict(receipt_store=[], sealed_enumeration=[],
                    continuation_segment=[], freeze_signature_digest="9" * 64,
                    flagged_keys=[])
    cc = completed_chain()
    cbody = ok("completed body builds (closing verifier green)",
               lambda: build_review_body(cc, stores_c, V64, T64))
    if cbody is not None:
        if cbody["kind"] != "terminal-review-completed" or \
                cbody["successor_export_digest"] != cc[2]["body_digest"] or \
                cbody["disclosure_record_digest"] != cc[1]["body_digest"]:
            FAILS.append("[completed body] wrong values")
    expect("EXPORT-ABSENT-AT-CEREMONY",
           lambda: build_review_body(completed_chain(with_export=False),
                                     stores_c, V64, T64))
    expect("DUPLICATE-EXPORT",
           lambda: build_review_body(completed_chain(extra_export=True),
                                     stores_c, V64, T64))
    # an export placed AFTER the ending but outside its commit is trailing
    # history under the new rule; the displaced-export code remains reachable
    # for an export BEFORE the disclosure record, probed separately
    expect("TRAILING-RECORDS",
           lambda: build_review_body(completed_chain(in_commit=False),
                                     stores_c, V64, T64))
    pre_export = ev.mkchain([
        o1,
        {"k": "successor-export",
         "body": {"kind": "successor-export"}},
        {"k": "passrec", "gate": "DISCLOSURE", "predecessor": "b" * 64,
         "epoch": 1, "reading": 10, "commit_set": []},
    ])
    expect("EXPORT-OUTSIDE-COMMIT",
           lambda: build_review_body(pre_export, stores_c, V64, T64))
    # the ending's commit_set must name real positions (AGY TRV-V2 F1)
    expect("ENDING-COMMIT-MALFORMED",
           lambda: build_review_body(ev.mkchain([
               o1,
               {"k": "drain-start", "receipt_digest": D64, "epoch": 1,
                "reading": 10},
               {"k": "terminal-checkpoint", "status": "TERMINATED",
                "receipt_digest": D64, "commit_set": [99],
                "failed_members": [], "epoch": 1, "reading": 15},
           ]), stores_t, V64, T64))
    # the chain opens with its epoch opening or the ceremony signs nothing
    # (AGY TRV-V2 F2: the unmoored single-checkpoint chain was signable)
    expect("CHAIN-UNMOORED",
           lambda: build_review_body(ev.mkchain([
               {"k": "terminal-checkpoint", "status": "TERMINATED",
                "receipt_digest": D64, "commit_set": [], "failed_members": [],
                "epoch": 1, "reading": 15},
           ]), stores_t, V64, T64))
    expect("EXPORT-MISMATCH",
           lambda: build_review_body(
               completed_chain(body_override=lambda b: dict(
                   b, flagged_keys=[["A", "read"]])), stores_c, V64, T64))

    # schema exactness on presented bodies
    expect("REVIEW-KIND-UNKNOWN",
           lambda: validate_review_body({"kind": "terminal-review", "x": 1}))
    good = dict(b1)
    del good["transcript_digest"]
    expect("REVIEW-SCHEMA-FIELD", lambda: validate_review_body(good))
    extra = dict(b1, bonus=1)
    expect("REVIEW-SCHEMA-FIELD", lambda: validate_review_body(extra))
    return FAILS, TOTAL


if __name__ == "__main__":
    fails, total = fixtures()
    for x in fails:
        print("FIXTURE FAIL:", x)
    print(f"terminal review verifier fixtures: {total - len(fails)}/{total} green")
    sys.exit(1 if fails else 0)
