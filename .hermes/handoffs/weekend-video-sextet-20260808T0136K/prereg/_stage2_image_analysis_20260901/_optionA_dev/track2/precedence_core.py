"""precedence_core — DEPENDENCY-FREE core of the composed loader (v13 / driver v17; codex V32-1: an unavailable helper module must not decide): the precedence order,
the finding record, the ONE resolver, the classification ALLOWLIST (with DECLARED dynamic families), exception classification by provenance, the local retained-event
checks, canonicalisation, same-id contradictions and the tri-state delivery predicate. Imports only the standard library, so the driver can run every LOCAL check even
when provenance_designs (history_v2, py_ecc via the verifier stack) cannot be imported; those helpers are then BLOCKED and VERIFIER-UNAVAILABLE is contributed.
provenance_designs_v13 re-exports these names so its callers are unchanged."""
import hashlib, json, re, subprocess
PRECEDENCE = ("LOCAL-TERMINAL", "FORGED", "NOT-EARLIEST", "EXPIRED", "DERIVED-TERMINAL", "RETRY-UNAVAILABLE", "RETRY-INCOMPLETE", "ACCEPT")
def finding(cls, code, why, stage, seq, check=None, unclassified=False):
    """One contribution: class (from PRECEDENCE), composed refusal NAME, reason, the stage and the CHECK (a key of the driver's INDEPENDENCE table) that derived it,
    its position in the fixed sequence, and whether its code was outside the allowlist."""
    assert cls in PRECEDENCE, cls; return {"class": cls, "rank": PRECEDENCE.index(cls), "code": code, "why": why, "stage": stage, "check": check, "seq": seq, "unclassified": unclassified}
def resolve(findings):
    """THE ONE RESOLVER: the finding of the highest class wins; within a class the fixed sequence (seq) decides; list or retrieval order plays no part."""
    return min(findings, key=lambda f: (f["rank"], f["seq"]))
def canon(e): return hashlib.sha256(json.dumps(e, sort_keys=True, separators=(",", ":")).encode()).hexdigest()
def same_id_contradictions(retained, live_events):
    d = canon(retained); return [e for e in (live_events or []) if isinstance(e, dict) and e.get("type") == "PushEvent" and e.get("id") == retained.get("id") and canon(e) != d]
def local_precheck_event(e, repo, branch_ref):
    """(outcome, why): the LOCALLY decidable shape of a retained event — a PushEvent object, an object `repo` naming the pinned repository, an object `payload` naming
    the protected ref. Every field is guarded, so a list where an object belongs is a named mismatch, not an exception (codex V32-1: a `repo` list)."""
    if not isinstance(e, dict) or e.get("type") != "PushEvent": return "INCONSISTENT-INPUT", "retained object is not a PushEvent"
    if not isinstance(e.get("repo"), dict): return "INCONSISTENT-INPUT", f"retained event's repo field is not an object ({type(e.get('repo')).__name__})"
    if e["repo"].get("name") != repo: return "INCONSISTENT-INPUT", f"retained event names repository {e['repo'].get('name')!r}, not the pinned {repo!r}"
    if not isinstance(e.get("payload"), dict): return "INCONSISTENT-INPUT", f"retained event's payload is not an object ({type(e.get('payload')).__name__})"
    if e["payload"].get("ref") != branch_ref: return "INCONSISTENT-INPUT", f"retained event names ref {e['payload'].get('ref')!r}, not the protected {branch_ref!r}"
    return None, None
def delivery(e, commit, branch_ref, root=None):
    """TRI-STATE delivery check (v7, codex V26-2; v8: an OSError launching git is UNDETERMINED, codex V27-2): 'DELIVERED' (head == commit, commit in payload.commits, or before..head ancestry ESTABLISHED via git),
    'NOT-DELIVERED' (the event positively does not deliver the commit: wrong type/ref, or ancestry established false), 'UNDETERMINED' (an ancestry claim that
    cannot be decided: no repository root given, a git object missing locally, or a failed git command). Same evidence as approval_witness_v4.delivers,
    but 'cannot establish' is no longer collapsed into 'false'."""
    if not isinstance(e, dict) or e.get("type") != "PushEvent": return "NOT-DELIVERED"
    p = e.get("payload") or {}
    if p.get("ref") != branch_ref: return "NOT-DELIVERED"
    if p.get("head") == commit or any(c.get("sha") == commit for c in p.get("commits", [])): return "DELIVERED"
    before, head = p.get("before"), p.get("head")
    if not (re.fullmatch(r"[0-9a-f]{40}", str(before)) and re.fullmatch(r"[0-9a-f]{40}", str(head)) and re.fullmatch(r"[0-9a-f]{40}", str(commit))): return "NOT-DELIVERED"
    if before == commit: return "NOT-DELIVERED"
    if not root: return "UNDETERMINED"
    try:                                                                                                # v8 (codex V27-2): a git process-launch exception is evidence that could not be established
        for obj in (before, head, commit):
            if subprocess.run(["git", "cat-file", "-e", obj + "^{commit}"], cwd=root, capture_output=True).returncode != 0: return "UNDETERMINED"
        r1 = subprocess.run(["git", "merge-base", "--is-ancestor", before, commit], cwd=root, capture_output=True); r2 = subprocess.run(["git", "merge-base", "--is-ancestor", commit, head], cwd=root, capture_output=True)
    except (OSError, subprocess.SubprocessError): return "UNDETERMINED"
    if r1.returncode not in (0, 1) or r2.returncode not in (0, 1): return "UNDETERMINED"
    return "DELIVERED" if (r1.returncode == 0 and r2.returncode == 0) else "NOT-DELIVERED"
def delivers(e, commit, branch_ref, root=None):
    """Boolean view of `delivery` for callers that only ask 'is it delivered?' (batch classification): UNDETERMINED counts as False here; the callers that
    must distinguish it (authenticate_event) use `delivery` directly."""
    return delivery(e, commit, branch_ref, root) == "DELIVERED"
LOCAL = "LOCAL-TERMINAL"; DERIVED = "DERIVED-TERMINAL"; RETRY = "RETRY-UNAVAILABLE"
CLASS_ALLOWLIST = {
    # --- driver: local integrity of retained input (class 0)
    **{c: LOCAL for c in ("ADOPTION-MISSING", "ADOPTION-MALFORMED", "ADOPTION-MISMATCH", "ADOPTION-NOT-AT-APPROVAL-COMMIT", "ADOPTION-DIGEST", "WITNESS-MISSING", "WITNESS-COMMIT-MALFORMED", "WITNESS-NOT-A-GIT-REPO", "WITNESS-COMMIT-LACKS-JOURNAL", "WITNESS-COMMIT-LACKS-RECORD", "WITNESS-REMOTE-URL",
        "IDENTITY-MISSING", "IDENTITY-NOT-SEALED", "IDENTITY-NOT-IN-WITNESS-COMMIT", "IDENTITY-SCHEMA", "IDENTITY-FIELD-MISSING", "IDENTITY-POOL-DIGEST", "IDENTITY-EXCLUSION-DIGEST", "PROTOCOL-NO-REDERIVER", "IDENTITY-RULE-DIGEST", "IDENTITY-NOT-BEACON-SEEDED", "IDENTITY-BEACON-NOT-ACCEPTED", "IDENTITY-SOURCE",
        "IDENTITY-WITNESS-MISSING", "IDENTITY-WITNESS-COMMIT", "APPROVAL-RECORD-MISSING", "APPROVAL-RECORD-DIGEST", "APPROVAL-RECORD-NOT-AT-COMMIT", "APPROVAL-RECORD-HISTORY", "APPROVAL-NOT-FIRST", "APPROVAL-RULE-LINE", "APPROVAL-T-SIGN-LINE", "APPROVAL-NONCE-LINE", "IDENTITY-T-SIGN", "IDENTITY-T-PULSE", "IDENTITY-ROUND",
        "IDENTITY-T-SIGN-PREDATES-AMENDMENT", "IDENTITY-T-PULSE-EXCLUDED", "IDENTITY-WITNESS-TIME", "IDENTITY-WITNESS-LATE", "EVENT-DIGEST", "EVENT-INCONSISTENT", "EVENT-PROVENANCE", "IDENTITY-WITNESS-NONCE", "NONCE-UNAUTHENTICATED", "COLLECTION-LOG-DIGEST", "COLLECTION-LOG-NOT-IN-WITNESS-COMMIT", "HISTORY-INVALID",
        "HISTORY-GENESIS", "HISTORY-COUNT", "COLLECTION-LOG-EMPTY", "IDENTITY-LOCK-MISMATCH", "COLLECTION-CLOSED", "COLLECTION-LOG-CONFLICT", "BEACON-RECORD-DIGEST", "BEACON-RECORD-NOT-IN-WITNESS-COMMIT", "BEACON-RECORD-UNREADABLE", "BEACON-RECORD-BINDING", "BEACON-RECORD-STATEMENT", "BEACON-RECORD-RELAYS",
        "HISTORY-OPEN-EVENT-MISSING", "HISTORY-OPEN-EVENT-INVALID", "IDENTITY-tuning_objids-SIZE-OR-TYPE", "IDENTITY-holdout_objids-SIZE-OR-TYPE", "IDENTITY-fresh_validation_objids-SIZE-OR-TYPE", "IDENTITY-OVERLAP", "SPLIT-INPUTS", "SPLIT-NOT-REPRODUCED", "MALFORMED-RETAINED-INPUT", "STAGE-NOT-RUN", "OPEN-EVENT-INCONSISTENT-INPUT",
        # driver refusals OUTSIDE load_identity (tuning / holdout / manifests / environment): class 0 by cause, listed so the table is total over the driver's raises
        "ENV-MISMATCH", "ENV-LOCK-HASH-MISMATCH", "ESTIMATOR-CHANGED-SINCE-TUNING", "HOLDOUT-OVERLAPS-TUNING", "HOLDOUT-ALREADY-INVOKED", "IDENTITY-DIFFERS-FROM-TUNING", "LABEL-NOT-PM1", "MANIFEST-COLUMNS", "MANIFEST-DUPLICATE-OBJID", "MANIFEST-IDENTITY-MISMATCH", "MANIFEST-MISSING", "MANIFEST-SIZE", "NO-TUNING-WINNER",
        "RENDER-JOURNAL-COUNT", "RENDER-JOURNAL-INCOMPLETE", "RENDER-JOURNAL-MALFORMED", "RENDER-JOURNAL-NOT-ENDED", "RENDER-JOURNAL-REFUSAL-SHAPE", "RUN-ROOT-MISMATCH", "RUN-ROOT-PARTS-DIFFER", "SENTINEL-JOURNAL-MISMATCH", "SENTINEL-WITHOUT-RENDER-JOURNAL", "TENSOR-DIR-MISSING", "TENSOR-MISSING", "TENSOR-SHA-MISMATCH", "TENSOR-SIZE",
        "TUNING-FILE-NOT-IN-WITNESS-COMMIT", "TUNING-JOURNAL-DUPLICATE", "TUNING-NOT-SEALED", "TUNING-RECEIPT-HASHES", "TUNING-RECEIPT-MODE", "TUNING-RECEIPT-MISSING", "TUNING-RECEIPT-CONFIG", "TUNING-RECEIPTS-COUNT", "WINNER-SUBSTITUTED",
        # helpers: producer / receipt refusals that name a local input defect
        "PUBLISH-BATCH", "PUBLISH-UNRELATED-COMMITS", "PUBLISH-COMMIT-FAILED", "RECEIPT-MALFORMED", "RECEIPT-DIGEST", "RECEIPT-ORIGIN", "RECEIPT-EVENT-ABSENT", "RECEIPT-MODIFIED", "RECEIPT-NOT-FIRST", "RECEIPT-NOT-PUBLISHED", "HISTORY-OPEN-COMMIT-MISMATCH", "HISTORY-OPEN-NOT-PUBLISHED", "OPEN-EVENT-DOES-NOT-DELIVER")},
    # --- affirmative contradictions in obtained live evidence (class 1), ordering (class 2), loss (class 3)
    "EVENT-FORGED": "FORGED", "OPEN-EVENT-FORGED": "FORGED", "EVENT-NOT-EARLIEST": "NOT-EARLIEST", "OPEN-EVENT-NOT-EARLIEST": "NOT-EARLIEST", "EVENT-EXPIRED-NO-RECEIPT-PATH": "EXPIRED", "EVENT-EXPIRED-RECEIPT-REFUSED": "EXPIRED", "EVIDENCE-EXPIRED": "EXPIRED",
    # --- derived from obtained remote / retained evidence by verification (class 4) — policies named in §3c
    **{c: DERIVED for c in ("IDENTITY-SEED-NOT-REDERIVED", "REDERIVE-REFUSE", "REDERIVE-CLOSED", "REDERIVE-REFUSE-ROUND", "WITNESS-NOT-PUSHED", "APPROVAL-COMMIT-NOT-PUSHED", "HISTORY-NOT-AN-EXTENSION", "HISTORY-DELETED-AT", "HISTORY-BATCH-COMMIT", "HISTORY-PUBLICATION-BATCH", "HISTORY-PUBLICATION-ORDER", "HISTORY-NO-COMMITS", "OPEN-NOT-GENESIS-ONLY", "PENDING-PUSH", "HISTORY-DIVERGED", "STALE-EXPECTED-HEAD", "HISTORY-CONTINUATION")},
    # --- evidence or environment not obtainable now (class 5) / absent, nothing contradicts (class 6)
    **{c: RETRY for c in ("REDERIVE-RETRY", "WITNESS-FETCH-FAILED", "VERIFIER-UNAVAILABLE", "IO-UNAVAILABLE", "IDENTITY-WITNESS-COMMIT-UNDETERMINED", "RETRY-EVENTS-UNAVAILABLE", "RETRY-REMOTE-UNAVAILABLE", "EVIDENCE-UNAVAILABLE", "MALFORMED-REMOTE-EVIDENCE", "RETRY-HISTORY-CONTINUATION", "STAGE-BLOCKED")},
    "EVIDENCE-INCOMPLETE": "RETRY-INCOMPLETE", "RETRY-EVENTS-INCOMPLETE": "RETRY-INCOMPLETE",
}
# 'HISTORY-CONTINUATION' / 'RETRY-HISTORY-CONTINUATION' are COMPOSED names whose reason carries the specific token; the driver classifies those findings from the token via classify_history.

DYNAMIC_FAMILIES = (re.compile(r"^TUNING-RECEIPT-\d+-(CONFIG|COUNTS|JOURNAL-MISMATCH|DERIVED)$"),)   # the driver's dynamically formatted refusal names, DECLARED (codex V32-5), class 0
def classify_refusal(message):
    """(class, code, why, unclassified): ONLY allowlisted codes and declared dynamic families are placed; every other code is placed LOCAL-TERMINAL and FLAGGED."""
    msg = str(message); code = re.split(r"[:\s]", msg, 1)[0]; why = msg[len(code):].lstrip(": ").strip() or msg
    if code in CLASS_ALLOWLIST:
        cls = CLASS_ALLOWLIST[code]
        if code in ("HISTORY-CONTINUATION", "RETRY-HISTORY-CONTINUATION"): cls = classify_history(why)[0]
        return cls, code, why, False
    if any(p.match(code) for p in DYNAMIC_FAMILIES): return "LOCAL-TERMINAL", code, why, False
    return "LOCAL-TERMINAL", code, why, True
def classify_history(why):
    if why.startswith("EVIDENCE-UNAVAILABLE"): return "RETRY-UNAVAILABLE", "RETRY-HISTORY-CONTINUATION"
    if why.startswith("EVIDENCE-INCOMPLETE"): return "RETRY-INCOMPLETE", "RETRY-HISTORY-CONTINUATION"
    if why.startswith("RETRY-REMOTE-UNAVAILABLE"): return "RETRY-UNAVAILABLE", "HISTORY-CONTINUATION"
    if why.startswith("EVIDENCE-EXPIRED"): return "EXPIRED", "HISTORY-CONTINUATION"
    if why.startswith("OPEN-EVENT-FORGED"): return "FORGED", "HISTORY-CONTINUATION"
    if why.startswith("OPEN-EVENT-INCONSISTENT-INPUT"): return "LOCAL-TERMINAL", "HISTORY-CONTINUATION"
    if why.startswith("OPEN-EVENT-NOT-EARLIEST"): return "NOT-EARLIEST", "HISTORY-CONTINUATION"
    return "DERIVED-TERMINAL", "HISTORY-CONTINUATION"
SOURCES = ("retained", "remote", "local-file", "git", "verifier", "receipt")
def classify_exception(exc, source="retained"):
    """(class, code, why, unclassified) BY PROVENANCE of the input the failing operation consumed (codex V32-3): retained input → MALFORMED-RETAINED-INPUT (class 0);
    remote evidence → MALFORMED-REMOTE-EVIDENCE (class 5); a local file / git / the verifier → IO-UNAVAILABLE / VERIFIER-UNAVAILABLE (class 5); a receipt → RECEIPT-MALFORMED
    (the receipt policy, class 3, applied by the driver); a DataIntegrityFail → classify_refusal; anything else flagged."""
    if type(exc).__name__ == "DataIntegrityFail": return classify_refusal(str(exc))
    if source == "verifier" or isinstance(exc, ImportError): return "RETRY-UNAVAILABLE", "VERIFIER-UNAVAILABLE", f"{type(exc).__name__}: {exc}"[:300], False
    if source == "receipt": return "EXPIRED", "EVENT-EXPIRED-RECEIPT-REFUSED", f"RECEIPT-MALFORMED: {type(exc).__name__}: {exc}"[:300], False
    if isinstance(exc, (OSError, subprocess.SubprocessError)) or source in ("local-file", "git"): return "RETRY-UNAVAILABLE", "IO-UNAVAILABLE", f"{type(exc).__name__}: {exc}"[:300], False
    if isinstance(exc, (json.JSONDecodeError, ValueError, KeyError, TypeError, IndexError, AttributeError, UnicodeError)):
        if source == "remote": return "RETRY-UNAVAILABLE", "MALFORMED-REMOTE-EVIDENCE", f"{type(exc).__name__}: {exc}"[:300], False
        return "LOCAL-TERMINAL", "MALFORMED-RETAINED-INPUT", f"{type(exc).__name__}: {exc}"[:300], False
    return "LOCAL-TERMINAL", f"UNEXPECTED-{type(exc).__name__}", str(exc)[:300], True
