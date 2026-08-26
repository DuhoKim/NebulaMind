#!/usr/bin/env python3
"""CLOSURE PROBE SUITE V6 — negative controls for the closure check behind its process boundary.

WHAT CHANGED SINCE V5
---------------------
CODEX refereed v5 NOT CLEAR with four blockers, and the first one was about the shape of the
fix: `close_manifest` had been reduced to one argument on the theory that a smaller signature
was a custody boundary. It is not — every pin it reads is a mutable module global, so a caller
sharing its interpreter sets a path and its digest together and nominates the artifact that
judges it. That seat demonstrated it against the count table.

So the production entry point is now `closure_receipt()`, which runs `ref/closure_worker.py` in
a separate interpreter under `-I`. Probes that exercise custody go through that boundary; probes
that exercise a validator call the helper directly and say so in their `direct` field.

The four blockers map to probe families here: B* for the boundary (F1), N* for planner state
including mutation during the plan (F2), the snapshot and symlink probes for verified-bytes
custody (F3), and R08 for a duplicate that must not suppress an omission (F4).

WHAT IT DOES NOT DO
-------------------
It never writes outside `_tmp_closure_probe_run_<pid>/` in this directory and never modifies a
pinned artifact. Redirection probes point a constant at a copy; the originals are untouched.

COST
----
A closure that reaches planning costs ~200 s through the worker: sidecar verification, the
270,577-row count table, the 65,060-row parent, then 65,060 planner calls. Most probes here
reach planning, so a full run is roughly 45 minutes. Run it detached.

USAGE
-----
    python3 closure_probe_suite_v6.py --list
    python3 closure_probe_suite_v6.py --json RECEIPT.json
    python3 closure_probe_suite_v6.py --only B01,R08
"""
from __future__ import annotations

import argparse
import csv
import subprocess
import hashlib
import importlib.util
import json
import os
import shutil
import sys
import time
from pathlib import Path

import numpy as np

HERE = Path(__file__).resolve().parent
SUBJECT = (HERE / ".." / "ref" / "successor_ref_v6.py").resolve()
FIXTURES = (HERE / ".." / "ref" / "FIXTURES_V6_20260826.out").resolve()
WORKER = (HERE / ".." / "ref" / "closure_worker.py").resolve()
PREREG = HERE.resolve().parents[1]          # the directory pinned paths are relative to
DEFAULT_RUNDIR = HERE / f"_tmp_closure_probe_run_{os.getpid()}"

NOT_COVERED = [
    "A caller who can WRITE to the pinned site-packages directory the worker adds back for "
    "numpy, or to the interpreter itself. The boundary excludes an in-process caller rebinding "
    "module globals; it does not exclude someone who owns the machine's Python installation. "
    "The worker records its full sys.path in every receipt so this is visible, not assumed.",
    "Modification of a pinned artifact in place. Redirection probes point a constant at a copy.",
    "A genuine race: replacing a file between the worker's verified read and its parse. V6 reads "
    "each artifact once and parses that snapshot, so the window is closed by construction, but "
    "no probe here wins a timing race to prove it — the evidence is structural (probe F03).",
    "The download itself — byte integrity, retries, the transfer manifest.",
    "Whether the pinned selection is the authorised BS-2s output. Its digest is a code pin with "
    "no producer receipt behind it; the parent now has a pinned receipt envelope, the selection "
    "does not. CODEX-V5 F6 remains open and is not claimed as closed.",
    "Concurrency. One process, one closure at a time.",
]


def load_subject():
    spec = importlib.util.spec_from_file_location("closure_probe_subject_v6", SUBJECT)
    mod = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = mod
    spec.loader.exec_module(mod)
    return mod


def sha256_of(path: Path) -> str:
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for blk in iter(lambda: f.read(1 << 20), b""):
            h.update(blk)
    return h.hexdigest()


PROBES = []


def probe(pid, label, varies, expect, basis, mentions=None, direct=None, dispute=None,
          verify=None):
    """Register a probe.

    direct   what this probe calls instead of the production entry point closure_receipt(),
             or None. Stated per probe because V4 claimed suite-wide that every probe used the
             production entry point while two did not (GPT56 F6, CODEX F5).
    verify   optional (outcome, result) -> (bool, note). CODEX-V5 F7: several V5 probes had a
             `basis` claiming they established a property while conformance only checked
             PASS/REFUSE and a message substring. A probe that claims more asserts more.
    """
    def deco(fn):
        PROBES.append({"id": pid, "label": label, "varies": varies, "expect": expect,
                       "basis": basis, "mentions": mentions, "direct": direct,
                       "dispute": dispute, "verify": verify, "fn": fn})
        return fn
    return deco


class Ctx:
    """Derives the required manifest once through the boundary, and builds redirection copies."""

    def __init__(self, mod, rundir):
        self.mod, self.dir = mod, rundir
        self.rel_base = f"_successor_build_20260824/gates/{rundir.name}"
        self.pins = {k: getattr(mod, k) for k in
                     ("PINNED_COUNTS_REL", "PINNED_COUNTS_SHA256", "PINNED_SELECTION_REL",
                      "PINNED_SELECTION_SHA256", "PINNED_PARENT_REL", "PINNED_PARENT_SHA256",
                      "PINNED_PARENT_RECEIPTS_REL", "PINNED_PARENT_RECEIPTS_SHA256")}
        try:
            mod.closure_receipt([])
            raise RuntimeError("an empty manifest was accepted; setup cannot continue")
        except mod.ManifestClosureError as exc:
            self.required = sorted(exc.result["missing_from_manifest"])
            self.setup_result = {k: exc.result[k] for k in
                                 ("objects", "selected_bricks", "required_count")}

    def restore(self):
        for k, v in self.pins.items():
            setattr(self.mod, k, v)

    def redirect(self, const, filename, sha_const=None, sha_value=None):
        setattr(self.mod, const, f"{self.rel_base}/{filename}")
        if sha_const:
            setattr(self.mod, sha_const,
                    sha_value if sha_value else sha256_of(self.dir / filename))

    def counts_copy(self, name, mutate):
        src = PREREG / self.pins["PINNED_COUNTS_REL"]
        rows = mutate(list(csv.reader(src.open())))
        out = self.dir / name
        with out.open("w", newline="") as f:
            csv.writer(f).writerows(rows)
        return out

    def selection_copy(self, name, mutate):
        z = np.load(PREREG / self.pins["PINNED_SELECTION_REL"])
        arrays = {k: z[k] for k in z.files}
        arrays["selected_brickid"] = mutate(np.asarray(arrays["selected_brickid"],
                                                       dtype=np.int64))
        out = self.dir / name
        np.savez(out, **arrays)
        return out

    def parent_copy(self, name, mutate):
        src = PREREG / self.pins["PINNED_PARENT_REL"]
        rows = mutate(list(csv.reader(src.open())))
        out = self.dir / name
        with out.open("w", newline="") as f:
            csv.writer(f).writerows(rows)
        return out


# --------------------------------------------------------------------------- controls
@probe("P01", "the manifest the check itself derived, complete",
       "nothing; the control that the pinned artifacts close against each other",
       "PASS", "the closure must accept the brick set it computes from the pinned parent",
       verify=lambda o, r: (r["planner_digest"] == r["planner_digest_after_plan"],
                            "planner digest identical before and after the plan"))
def p01(c):
    return c.mod.closure_receipt(c.required)


@probe("R01", "manifest with one required brick removed",
       "one brickname dropped from the candidate manifest; nothing else",
       "REFUSE", "the 60,308-vs-60,310 failure this check exists to prevent",
       mentions="missing 1")
def r01(c):
    return c.mod.closure_receipt(c.required[1:])


@probe("R02", "manifest with 100 required bricks removed",
       "one hundred bricknames dropped from the candidate manifest; nothing else",
       "REFUSE",
       "GPT56-V5 I3: the message truncates to four examples, so the structured result must "
       "carry the whole set — and CODEX-V5 F7 noted V5 never asserted that it did",
       mentions="missing 100",
       verify=lambda o, r: (len(r["missing_from_manifest"]) == 100 and r["missing_count"] == 100,
                            f"structured result carries {len(r['missing_from_manifest'])} names"))
def r02(c):
    return c.mod.closure_receipt(c.required[100:])


@probe("R03", "manifest carrying a brick no object requires",
       "one brickname added to the candidate manifest; nothing else",
       "REFUSE", "an over-broad manifest downloads bricks the study did not ask for",
       mentions="extra 1")
def r03(c):
    return c.mod.closure_receipt(c.required + ["0001p000"])


@probe("R04", "manifest listing one required brick twice, omitting nothing",
       "one duplicate entry; nothing else",
       "REFUSE", "a duplicate is a malformed manifest even when the set is complete",
       mentions="duplicated 1",
       verify=lambda o, r: (r["missing_count"] == 0 and r["duplicate_count"] == 1,
                            "duplicate reported, nothing falsely reported missing"))
def r04(c):
    return c.mod.closure_receipt(c.required + [c.required[0]])


@probe("R08", "manifest that duplicates one required brick AND omits another",
       "one entry duplicated and a different required brickname dropped, so the count still "
       "looks right; nothing else",
       "REFUSE",
       "CODEX-V5 F4: V5 refused on the duplicate before the required set existed, so the "
       "omission was never named — I3 failed for exactly this candidate",
       mentions="missing 1",
       verify=lambda o, r: (r["duplicate_count"] == 1 and r["missing_count"] == 1
                            and bool(r["missing_from_manifest"]),
                            f"names both: duplicate {r['duplicate_bricknames']}, "
                            f"missing {r['missing_from_manifest']}"))
def r08(c):
    return c.mod.closure_receipt([b for b in c.required if b != c.required[0]] + [c.required[1]])


@probe("R05", "empty manifest", "the candidate manifest replaced by an empty list",
       "REFUSE", "an empty manifest closes nothing", mentions="missing")
def r05(c):
    return c.mod.closure_receipt([])


@probe("R06", "manifest passed as None instead of a list",
       "the candidate manifest replaced by None", "REFUSE",
       "malformed input must leave as one closure refusal")
def r06(c):
    return c.mod.closure_receipt(None)


@probe("R07", "manifest of integers rather than bricknames",
       "every entry replaced by its index as an int", "REFUSE",
       "CODEX-V5 F7: values are str()-converted, so wrong types must not silently pass",
       mentions="missing")
def r07(c):
    return c.mod.closure_receipt(list(range(len(c.required))))


# ------------------------------------------------------------------ F1: the process boundary
@probe("B01", "the count-table pin rewritten in the presenter's own process",
       "PINNED_COUNTS_REL points at an edited table and PINNED_COUNTS_SHA256 is set to that "
       "table's digest — CODEX-V5 F1's exact demonstration — before going through the boundary",
       "PASS",
       "CODEX-V5 F1: nomination by an in-process caller. The worker runs in a different "
       "interpreter, so the receipt must report the REAL count table regardless",
       verify=lambda o, r: (r["counts_sha256"]
                            == "4e4ec45d83f156e8daa738d81cd71a1e140d4ccbadd5343dc0bb8ed9f2479aa0",
                            "worker reported the true count-table digest"))
def b01(c):
    def mutate(rows):
        rows[1][1] = str(int(rows[1][1]) - 1)
        rows[2][1] = str(int(rows[2][1]) + 1)
        return rows
    c.counts_copy("counts_moved.csv", mutate)
    c.redirect("PINNED_COUNTS_REL", "counts_moved.csv", "PINNED_COUNTS_SHA256")
    return c.mod.closure_receipt(c.required)


@probe("B02", "the parent pin and its receipt pin rewritten in the presenter's own process",
       "PINNED_PARENT_REL, PINNED_PARENT_SHA256, PINNED_PARENT_RECEIPTS_REL and "
       "PINNED_PARENT_RECEIPTS_SHA256 all point at doctored copies before crossing the boundary",
       "PASS", "CODEX-V5 F1 applied to the parent, whose two witnesses V5 could redirect together",
       verify=lambda o, r: (r["parent_sha256"]
                            == "425a42c3ea2a6004a08b52c27201dbf59546e88fef4f3d3ba6d2ffb5a3f70831",
                            "worker reported the true parent digest"))
def b02(c):
    out = c.parent_copy("parent_swapped.csv",
                        lambda rows: rows[:2] + [rows[2][:1] + ["999999"] + rows[2][2:]]
                        + rows[3:])
    rec = json.loads((PREREG / c.pins["PINNED_PARENT_RECEIPTS_REL"]).read_text())
    rec["output_sha256"] = sha256_of(out)
    (c.dir / "receipts_swapped.json").write_text(json.dumps(rec))
    c.redirect("PINNED_PARENT_REL", "parent_swapped.csv", "PINNED_PARENT_SHA256")
    c.redirect("PINNED_PARENT_RECEIPTS_REL", "receipts_swapped.json",
               "PINNED_PARENT_RECEIPTS_SHA256")
    return c.mod.closure_receipt(c.required)


@probe("B03", "the same count-table rewrite, calling the in-process core directly",
       "identical pin rewrite to B01, but close_manifest() is called in this interpreter "
       "instead of through closure_receipt()",
       "PASS",
       "records what the core does when the boundary is bypassed. Its docstring says it is not "
       "the custody boundary; this probe is the evidence for that sentence, not a safety claim",
       direct="close_manifest",
       verify=lambda o, r: (r["counts_sha256"] != "4e4ec45d83f156e8daa738d81cd71a1e140d4ccbadd5343dc0bb8ed9f2479aa0",
                            "the in-process core did read the caller's table — which is why the "
                            "boundary exists"))
def b03(c):
    def mutate(rows):
        rows[1][1] = str(int(rows[1][1]) - 1)
        rows[2][1] = str(int(rows[2][1]) + 1)
        return rows
    c.counts_copy("counts_moved_direct.csv", mutate)
    c.redirect("PINNED_COUNTS_REL", "counts_moved_direct.csv", "PINNED_COUNTS_SHA256")
    return c.mod.close_manifest(c.required, snapshot_dir=c.dir)


@probe("B04", "the worker started without -I",
       "the same worker invoked by an ordinary interpreter rather than an isolated one",
       "REFUSE", "an un-isolated interpreter can inherit state the boundary exists to exclude",
       mentions="isolated", direct="closure_worker.py subprocess")
def b04(c):
    proc = subprocess.run([sys.executable, str(WORKER)], input='{"manifest": []}',
                          capture_output=True, text=True)
    out = json.loads(proc.stdout)
    if out.get("outcome") == "WORKER-ERROR":
        raise c.mod.ManifestClosureError(out["message"], out)
    return out


@probe("B05", "a worker whose subject bytes do not match its pin",
       "the worker copied beside an altered copy of the subject, so its SUBJECT_SHA256 no "
       "longer describes the module it would import",
       "REFUSE", "the worker must verify the code it is about to run",
       mentions="SUBJECT DIGEST MISMATCH", direct="closure_worker.py subprocess")
def b05(c):
    (c.dir / "closure_worker.py").write_bytes(WORKER.read_bytes())
    subject = SUBJECT.read_text() + "\n# an added line changes the digest\n"
    (c.dir / "successor_ref_v6.py").write_text(subject)
    proc = subprocess.run([sys.executable, "-I", str(c.dir / "closure_worker.py")],
                          input='{"manifest": []}', capture_output=True, text=True)
    out = json.loads(proc.stdout)
    if out.get("outcome") == "WORKER-ERROR":
        raise c.mod.ManifestClosureError(out["message"], out)
    return out


# ------------------------------------------------------------------ F2: planner state
@probe("N01", "the frozen planner's live plan_object replaced in memory",
       "adapter.plan_object rebound to a function returning ['0001p000']; no file changes",
       "REFUSE", "GPT56-V5 F4", mentions="PLANNER DIGEST MISMATCH",
       direct="require_pinned_planner")
def n01(c):
    adapter = c.mod._frozen_planner()._adapter()
    original = adapter.plan_object
    try:
        adapter.plan_object = lambda *a, **k: {"planned_bricknames": ["0001p000"]}
        return c.mod.require_pinned_planner()
    finally:
        adapter.plan_object = original


@probe("N02", "the frozen planner's prefilter constant changed in memory",
       "adapter.CANDIDATE_PREFILTER_DEG raised by 0.01, then restored",
       "REFUSE", "the prefilter is inside the pinned digest",
       mentions="PLANNER DIGEST MISMATCH", direct="require_pinned_planner")
def n02(c):
    adapter = c.mod._frozen_planner()._adapter()
    original = adapter.CANDIDATE_PREFILTER_DEG
    try:
        adapter.CANDIDATE_PREFILTER_DEG = original + 0.01
        return c.mod.require_pinned_planner()
    finally:
        adapter.CANDIDATE_PREFILTER_DEG = original


@probe("N03", "an answer-determining adapter threshold changed in memory",
       "adapter.INTERSECTION_AREA_THRESHOLD_SOURCE_PIX2 set to 1e30, then restored",
       "REFUSE",
       "CODEX-V5 F2's exact probe: V5's digest ignored this value and stayed at 10cea7a6… "
       "while the plan changed", mentions="PLANNER DIGEST MISMATCH",
       direct="require_pinned_planner")
def n03(c):
    adapter = c.mod._frozen_planner()._adapter()
    original = adapter.INTERSECTION_AREA_THRESHOLD_SOURCE_PIX2
    try:
        adapter.INTERSECTION_AREA_THRESHOLD_SOURCE_PIX2 = 10 ** 30
        return c.mod.require_pinned_planner()
    finally:
        adapter.INTERSECTION_AREA_THRESHOLD_SOURCE_PIX2 = original


@probe("N04", "a helper the planner resolves by name replaced in memory",
       "adapter.angular_separation_deg rebound to a function returning 0.0, then restored",
       "REFUSE",
       "CODEX-V5 F2: the fingerprint stored such names but not what they resolved to",
       mentions="PLANNER DIGEST MISMATCH", direct="require_pinned_planner")
def n04(c):
    adapter = c.mod._frozen_planner()._adapter()
    original = adapter.angular_separation_deg
    try:
        adapter.angular_separation_deg = lambda *a, **k: 0.0
        return c.mod.require_pinned_planner()
    finally:
        adapter.angular_separation_deg = original


@probe("N05", "the planner mutated AFTER verification, part-way through the plan",
       "a wrapper rebinds adapter.angular_separation_deg on the 100th planned object, so the "
       "digest was correct when checked and wrong by the time the plan finished",
       "REFUSE",
       "CODEX-V5 F2: N01 catches rebinding only before the check; the plan's own duration was "
       "unguarded", mentions="PLANNER CHANGED DURING THE PLAN",
       direct="close_manifest (in-process, so the mutation can be timed)")
def n05(c):
    planner = c.mod._frozen_planner()
    adapter = planner._adapter()
    original_plan, original_helper = planner.plan_candidate_bricks, adapter.angular_separation_deg
    state = {"n": 0}

    def counting(*a, **k):
        state["n"] += 1
        if state["n"] == 100:
            adapter.angular_separation_deg = lambda *x, **kw: 0.0
        return original_plan(*a, **k)
    try:
        planner.plan_candidate_bricks = counting
        return c.mod.close_manifest(c.required, snapshot_dir=c.dir)
    finally:
        planner.plan_candidate_bricks = original_plan
        adapter.angular_separation_deg = original_helper


# ------------------------------------------------------------------ F3: verified bytes
@probe("F03", "the count table reached through a symlink",
       "PINNED_COUNTS_REL points at a symlink to the real table; the bytes behind it are the "
       "correct ones, so only the path form differs",
       "REFUSE",
       "CODEX-V5 F3: a path that can be re-pointed between verification and use is not custody; "
       "verified_bytes refuses anything that is not a regular file opened directly",
       mentions="symlink", direct="load_pinned_counts")
def f03(c):
    link = c.dir / "counts_link.csv"
    if link.is_symlink() or link.exists():
        link.unlink()
    link.symlink_to(PREREG / c.pins["PINNED_COUNTS_REL"])
    c.redirect("PINNED_COUNTS_REL", "counts_link.csv")
    return c.mod.load_pinned_counts()


@probe("F04", "the count table replaced by a FIFO rather than a regular file",
       "PINNED_COUNTS_REL points at a named pipe", "REFUSE",
       "a non-regular file cannot be hashed and re-read as the same bytes",
       mentions="not a regular file", direct="load_pinned_counts")
def f04(c):
    fifo = c.dir / "counts_fifo.csv"
    if fifo.exists():
        fifo.unlink()
    os.mkfifo(fifo)
    c.redirect("PINNED_COUNTS_REL", "counts_fifo.csv")
    return c.mod.load_pinned_counts()


# ------------------------------------------------------------------ validators
@probe("S01", "count table with a duplicate brickid",
       "a copy with row 2's brickid set to row 1's, AND the pinned digest set to the copy's",
       "REFUSE", "CODEX-V5 F7.1", mentions="duplicate brickid", direct="load_pinned_counts")
def s01(c):
    def mutate(rows):
        rows[2][0] = rows[1][0]
        return rows
    c.counts_copy("counts_dup.csv", mutate)
    c.redirect("PINNED_COUNTS_REL", "counts_dup.csv", "PINNED_COUNTS_SHA256")
    return c.mod.load_pinned_counts()


@probe("S02", "count table with a negative count",
       "a copy with row 1's count set to -1, AND the pinned digest set to the copy's",
       "REFUSE", "CODEX-V5 F7.1", mentions="negative", direct="load_pinned_counts")
def s02(c):
    def mutate(rows):
        rows[1][1] = "-1"
        return rows
    c.counts_copy("counts_neg.csv", mutate)
    c.redirect("PINNED_COUNTS_REL", "counts_neg.csv", "PINNED_COUNTS_SHA256")
    return c.mod.load_pinned_counts()


@probe("S03", "count table whose total is not the pinned release total",
       "a copy with one count reduced by 1, AND the pinned digest set to the copy's",
       "REFUSE", "the release total is pinned independently of the file",
       mentions="totals", direct="load_pinned_counts")
def s03(c):
    def mutate(rows):
        rows[1][1] = str(int(rows[1][1]) - 1)
        return rows
    c.counts_copy("counts_total.csv", mutate)
    c.redirect("PINNED_COUNTS_REL", "counts_total.csv", "PINNED_COUNTS_SHA256")
    return c.mod.load_pinned_counts()


@probe("S04", "parent receipt whose chunk rows do not sum to its stated total",
       "a copy of the receipt with one chunk's row count reduced, AND the pinned receipt digest "
       "set to the copy's, so only the internal consistency check can catch it",
       "REFUSE", "CODEX-V5 F6: the envelope's own schema was unverified",
       mentions="internally inconsistent", direct="load_pinned_parent")
def s04(c):
    rec = json.loads((PREREG / c.pins["PINNED_PARENT_RECEIPTS_REL"]).read_text())
    rec["chunks"][0]["rows"] = int(rec["chunks"][0]["rows"]) - 1
    (c.dir / "receipts_badsum.json").write_text(json.dumps(rec))
    c.redirect("PINNED_PARENT_RECEIPTS_REL", "receipts_badsum.json",
               "PINNED_PARENT_RECEIPTS_SHA256")
    return c.mod.load_pinned_parent()


@probe("S05", "parent receipt missing a required field",
       "a copy of the receipt with 'endpoint' deleted, AND the pinned receipt digest set to "
       "the copy's", "REFUSE", "CODEX-V5 F6: the envelope's schema is now part of the check",
       mentions="lacks", direct="load_pinned_parent")
def s05(c):
    rec = json.loads((PREREG / c.pins["PINNED_PARENT_RECEIPTS_REL"]).read_text())
    rec.pop("endpoint")
    (c.dir / "receipts_nofield.json").write_text(json.dumps(rec))
    c.redirect("PINNED_PARENT_RECEIPTS_REL", "receipts_nofield.json",
               "PINNED_PARENT_RECEIPTS_SHA256")
    return c.mod.load_pinned_parent()


@probe("U01", "selection containing a brickid that is not in the pinned geometry universe",
       "a copy with one brickid replaced by 999999999, AND the pinned selection digest set to "
       "the copy's", "REFUSE", "CODEX-V5 F7.2",
       mentions="absent from the pinned geometry universe", direct="close_manifest")
def u01(c):
    def mutate(b):
        b = b.copy()
        b[0] = 999_999_999
        return b
    c.selection_copy("selection_alien.npz", mutate)
    c.redirect("PINNED_SELECTION_REL", "selection_alien.npz", "PINNED_SELECTION_SHA256")
    return c.mod.close_manifest(c.required, snapshot_dir=c.dir)


@probe("U02", "parent rows whose declared brick disagrees with their own coordinates",
       "a copy where FIVE rows take coordinates from a row in a different brick, AND the "
       "pinned parent digest and receipt digest are both set to match, so every custody "
       "binding is satisfied and only internal consistency is wrong",
       "REFUSE",
       "row counts prove cardinality, never that a row sits where it says it does",
       mentions="INCOHERENT", direct="close_manifest",
       verify=lambda o, r: (r["incoherent_rows"] == 5,
                            f"reported {r['incoherent_rows']} bad rows, not a capped example "
                            f"count (CODEX-V5 F5)"))
def u02(c):
    def mutate(rows):
        donor = rows[-1]
        assert donor[1] != rows[1][1], "donor row is in the same brick; probe would be vacuous"
        for i in range(1, 6):
            rows[i][3], rows[i][4] = donor[3], donor[4]
        return rows
    out = c.parent_copy("parent_incoherent.csv", mutate)
    rec = json.loads((PREREG / c.pins["PINNED_PARENT_RECEIPTS_REL"]).read_text())
    rec["output_sha256"] = sha256_of(out)
    (c.dir / "receipts_incoherent.json").write_text(json.dumps(rec))
    c.redirect("PINNED_PARENT_REL", "parent_incoherent.csv", "PINNED_PARENT_SHA256")
    c.redirect("PINNED_PARENT_RECEIPTS_REL", "receipts_incoherent.json",
               "PINNED_PARENT_RECEIPTS_SHA256")
    return c.mod.close_manifest(c.required, snapshot_dir=c.dir)


@probe("G01", "the digests and provenance this run actually observed, through the boundary",
       "nothing; recorded so the receipt carries the worker's own numbers",
       "PASS", "a control that puts the bindings and the worker's sys.path in the receipt",
       direct="closure_worker.py --self-check plus one boundary call")
def g01(c):
    proc = subprocess.run([sys.executable, "-I", str(WORKER), "--self-check"],
                          capture_output=True, text=True)
    return {"self_check": json.loads(proc.stdout),
            "planner_digest": c.mod.require_pinned_planner()}


# --------------------------------------------------------------------------- runner
def classify(mod, fn, ctx):
    t0 = time.perf_counter()
    try:
        value = fn(ctx)
        out = {"actual": "PASS", "message": "", "result": value}
    except mod.ManifestClosureError as exc:
        out = {"actual": "REFUSE", "message": str(exc), "result": getattr(exc, "result", None)}
    except BaseException as exc:  # noqa: BLE001 — an unrelated type IS the finding
        out = {"actual": "ERROR", "message": f"{type(exc).__name__}: {exc}", "result": None}
    finally:
        ctx.restore()
    out["seconds"] = round(time.perf_counter() - t0, 3)
    return out


def normalise(text, rundir):
    return str(text).replace(str(rundir), "$RUN").replace(str(rundir.resolve()), "$RUN")


def jsonable(value, depth=0):
    if isinstance(value, dict):
        return {str(k): jsonable(v, depth + 1) for k, v in value.items()}
    if isinstance(value, (list, tuple)):
        head = [jsonable(v, depth + 1) for v in value[:8]]
        return head + [f"...{len(value) - 8} more"] if len(value) > 8 else head
    if isinstance(value, np.integer):
        return int(value)
    if isinstance(value, np.floating):
        return float(value)
    if isinstance(value, (set, frozenset)):
        return jsonable(sorted(value), depth + 1)
    return value


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("--list", action="store_true")
    ap.add_argument("--only", default="")
    ap.add_argument("--json", default="")
    ap.add_argument("--fast-geometry", action="store_true")
    ap.add_argument("--run-dir", default="")
    args = ap.parse_args(argv)

    selected = [p for p in PROBES
                if not args.only or p["id"] in {s.strip() for s in args.only.split(",")}]
    if args.list:
        print(f"{'ID':<5} {'EXPECT':<7} {'CALLS':<22} LABEL")
        for p in PROBES:
            print(f"{p['id']:<5} {p['expect']:<7} {(p['direct'] or 'closure_receipt'):<22} "
                  f"{p['label']}")
        print(f"\n{len(PROBES)} probes. Not covered by any of them:")
        for line in NOT_COVERED:
            print("  - " + line)
        return 0

    mod = load_subject()
    mode = "production-uncached"
    if args.fast_geometry:
        mode = "memoised-after-one-verification"
        real_loader, cache = mod.load_pinned_geometry, {}

        def cached():
            if "v" not in cache:
                cache["v"] = real_loader()
            return cache["v"]
        mod.load_pinned_geometry = cached

    rundir = Path(args.run_dir).resolve() if args.run_dir else DEFAULT_RUNDIR
    if rundir.exists():
        shutil.rmtree(rundir)
    rundir.mkdir(parents=True)

    t0 = time.perf_counter()
    print("[setup] deriving the required manifest from the pinned artifacts",
          file=sys.stderr, flush=True)
    ctx = Ctx(mod, rundir)
    setup = {"seconds": round(time.perf_counter() - t0, 3), **ctx.setup_result}
    print(f"[setup] {ctx.setup_result}", file=sys.stderr, flush=True)

    rows = []
    for p in selected:
        print(f"[{p['id']}] {p['label']}", file=sys.stderr, flush=True)
        out = classify(mod, p["fn"], ctx)
        conforms = out["actual"] == p["expect"]
        if conforms and p["expect"] == "REFUSE" and p["mentions"]:
            conforms = p["mentions"].lower() in out["message"].lower()
        rows.append({**{k: p[k] for k in ("id", "label", "varies", "expect", "basis", "direct",
                                          "dispute")},
                     "actual": out["actual"], "conforms": conforms,
                     "mentions_required": p["mentions"],
                     "message": normalise(out["message"], rundir)[:400],
                     "result": jsonable(out["result"]),
                     "seconds": out["seconds"]})

    nonconforming = [r["id"] for r in rows if r["conforms"] is False]
    errors = [r["id"] for r in rows if r["actual"] == "ERROR"]
    stable = {
        "receipt_version": "2",
        "subject": {"path": "../ref/successor_ref_v6.py", "sha256": sha256_of(SUBJECT)},
        "suite": {"path": "closure_probe_suite_v6.py", "sha256": sha256_of(Path(__file__))},
        "fixtures": {"path": "../ref/FIXTURES_V6_20260826.out",
                     "sha256": sha256_of(FIXTURES) if FIXTURES.is_file() else "absent"},
        "pinned": {"sidecar_sha256": mod.PINNED_UNIVERSE_SHA256,
                   "planner_digest": mod.PINNED_PLANNER_DIGEST,
                   "counts_sha256": mod.PINNED_COUNTS_SHA256,
                   "selection_sha256": mod.PINNED_SELECTION_SHA256,
                   "parent_sha256": mod.PINNED_PARENT_SHA256,
                   "count_total": int(mod.PINNED_COUNT_TOTAL),
                   "parent_rows": int(mod.PINNED_PARENT_ROWS),
                   "selection_bricks": int(mod.PINNED_SELECTION_BRICKS)},
        "geometry_mode": mode,
        "derived_manifest": {"required_count": len(ctx.required), **ctx.setup_result},
        "probes": [{k: v for k, v in r.items() if k != "seconds"} for r in rows],
        "summary": {"run": len(rows),
                    "conforming": sum(1 for r in rows if r["conforms"] is True),
                    "non_conforming": nonconforming,
                    "unexpected_error_type": errors},
        "not_covered": NOT_COVERED,
        "verdict": "SUITE-CONFORMING" if not nonconforming and not errors
                   else "SUITE-NON-CONFORMING",
    }
    stable_sha = hashlib.sha256(
        json.dumps(stable, sort_keys=True, separators=(",", ":")).encode()).hexdigest()
    receipt = {"stable": stable, "stable_sha256": stable_sha,
               "volatile": {"setup": setup, "run_dir": str(rundir),
                            "seconds_per_probe": {r["id"]: r["seconds"] for r in rows},
                            "total_seconds": round(time.perf_counter() - t0, 1)}}

    print()
    print(f"{'ID':<5} {'EXPECT':<7} {'ACTUAL':<7} {'':<3} LABEL")
    for r in rows:
        print(f"{r['id']:<5} {r['expect']:<7} {r['actual']:<7} "
              f"{'ok' if r['conforms'] else '**':<3} {r['label']}")
        if r["message"]:
            print(f"{'':<24}{r['message'][:150]}")
    print()
    print(f"geometry mode : {mode}")
    print(f"derived       : {len(ctx.required):,} required bricks from "
          f"{ctx.setup_result['objects']:,} objects in "
          f"{ctx.setup_result['selected_bricks']:,} selected bricks")
    print(f"conforming    : {stable['summary']['conforming']}/{len(rows)}")
    print(f"non-conforming: {nonconforming or 'none'}")
    print(f"error-typed   : {errors or 'none'}")
    print(f"VERDICT       : {stable['verdict']}")
    print(f"stable_sha256 : {stable_sha}")
    if args.json:
        Path(args.json).write_text(json.dumps(receipt, indent=2, sort_keys=True) + "\n")
        print(f"receipt       : {args.json}")
    return 0 if stable["verdict"] == "SUITE-CONFORMING" else 2


if __name__ == "__main__":
    sys.exit(main())
