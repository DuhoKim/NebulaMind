#!/usr/bin/env python3
"""CLOSURE PROBE SUITE V6 — negative controls for the closure check behind its process boundary.

WHAT CHANGED SINCE V5
---------------------
CODEX refereed v5 NOT CLEAR with four blockers, and the first one was about the shape of the
fix: `close_manifest` had been reduced to one argument on the theory that a smaller signature
was a custody boundary. It is not — every pin it reads is a mutable module global, so a caller
sharing its interpreter sets a path and its digest together and nominates the artifact that
judges it. That seat demonstrated it against the count table.

So the production entry point is now `closure_receipt()`, which runs `ref/closure_worker_v9.py` in
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
import threading
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
SUBJECT = (HERE / ".." / "ref" / "successor_ref_v9.py").resolve()
FIXTURES = (HERE / ".." / "ref" / "FIXTURES_V9_20260826.out").resolve()
WORKER = (HERE / ".." / "ref" / "closure_worker_v9.py").resolve()
PREREG = HERE.resolve().parents[1]          # the directory pinned paths are relative to
DEFAULT_RUNDIR = HERE / f"_tmp_closure_probe_run_{os.getpid()}"

NOT_COVERED = [
    "A caller who can WRITE to the interpreter or to any directory on the worker's sys.path. "
    "KIMI-V6 F4 measured this wider than v6 stated it: under -I the CommandLineTools system "
    "site-packages still precedes the one pinned add-back, and astropy — which PARSES the "
    "sidecar — resolves from the same unpinned user directory as numpy. The sidecar's bytes "
    "are pinned; its parser is not. Every receipt records the full sys.path -- and so does a "
    "refusal, since the interpreter state is captured before the isolation gate -- so this is "
    "visible rather than assumed. Probes W03 and B04 assert that; this sentence does not "
    "establish it (KIMI-V8 F3: in v8 the sentence was here and the record was not).",
    "Three classes of answer-determining state the planner fingerprint cannot see, each "
    "demonstrated by KIMI-V6 F4 rather than argued: a global that resolves to a MODULE is "
    "folded as the string '<module>' (rebinding math.radians left the digest unmoved), a "
    "pure-Python helper reachable only through a class method is not recursed into (rebinding "
    "tangent_plane_offsets left the digest unmoved), and a C callable contributes its type name "
    "only. In the worker these bite only at import time, which is the residual above — but the "
    "digest's cross-process stability and its blindness have the same root cause, and v7 does "
    "not close this.",
    "Modification of a pinned artifact in place. Redirection probes point a constant at a copy.",
    "A genuine race: replacing a file between the worker's verified read and its parse. V6 reads "
    "each artifact once and parses that snapshot, so the window is closed by construction, but "
    "no probe here wins a timing race to prove it — the evidence is structural (probe F03).",
    "The download itself — byte integrity, retries, the transfer manifest.",
    "Whether the pinned selection is the authorised BS-2s output. Its digest is a code pin with "
    "no producer receipt behind it; the parent now has a pinned receipt envelope, the selection "
    "does not. CODEX-V5 F6 remains open and is not claimed as closed.",
    "Concurrency. One process, one closure at a time.",
    "KIMI-V7 F3, F4 and F5, which are NOT fixed in v8 and are listed here so that this round "
    "cannot be read as having closed them: the six S0x/U01 `varies` strings still omit the "
    "PINNED_*_REL reassignment that Ctx.redirect performs (KIMI-V6 F7, twice named); B06's "
    "verify hook returns True unconditionally and asserts nothing, though its probe body does; "
    "F05's basis claims a no-window property no static-symlink probe can evidence; the worker "
    "subprocess has no timeout, so a hung worker hangs the caller; extra keys in the worker's "
    "stdin JSON are ignored; and the manifest-type refusal exits on the WORKER-ERROR channel "
    "rather than the REFUSE channel.",
    "Mutation of the objmanifest module instance that close_manifest itself holds. "
    "_frozen_planner() re-executes that module on every call, so the digest inspects a fresh "
    "instance rather than the retained one; N05 reaches the shared adapter instead, which is "
    "the object a mid-plan mutation can actually reach.",
]


def load_subject():
    spec = importlib.util.spec_from_file_location("closure_probe_subject_v9", SUBJECT)
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


@probe("B06", "an interpreter handed to closure_receipt as an argument",
       "nothing about the artifacts; the call is attempted with a python_executable keyword",
       "REFUSE",
       "KIMI-V6 F3: that parameter existed and was forged with a three-line fake interpreter "
       "that ignored -I and the worker and printed a PASS. It is gone, so the call itself must "
       "fail rather than silently ignoring the argument",
       direct="closure_receipt (called with a keyword it must not accept)",
       verify=lambda o, r: (True, "TypeError from the signature, not a forged receipt"))
def b06(c):
    fake = c.dir / "fake_python"
    fake.write_text("#!/bin/sh\necho '{\"outcome\":\"PASS\",\"result\":{\"required_count\":1}}'\n")
    fake.chmod(0o755)
    try:
        c.mod.closure_receipt(c.required, python_executable=str(fake))
    except TypeError as exc:
        raise c.mod.ManifestClosureError(
            f"closure_receipt refuses to take an interpreter: {exc}", {"typeerror": str(exc)})
    raise AssertionError("closure_receipt accepted a python_executable argument")


@probe("B07", "a JSON object rather than an array as the worker's manifest",
       "the worker is given {\"manifest\": {name: 1, ...}} over stdin, bypassing "
       "closure_receipt's list() normalisation",
       "REFUSE",
       "KIMI-V6 F6: iterating a dict yields its keys, so this was accepted and reported 12,117 "
       "entries. It cannot under-cover, but an unvalidated type at the trust boundary is what "
       "R06 and R07 exist to refuse",
       mentions="must be a JSON array", direct="closure_worker_v9.py subprocess")
def b07(c):
    payload = json.dumps({"manifest": {name: 1 for name in c.required}})
    proc = subprocess.run([sys.executable, "-I", str(WORKER)], input=payload,
                          capture_output=True, text=True)
    out = json.loads(proc.stdout)
    if out.get("outcome") == "WORKER-ERROR":
        raise c.mod.ManifestClosureError(out["message"], out)
    return out


@probe("F05", "the count table reached through a symlink whose target is the real table",
       "PINNED_COUNTS_REL points at a symlink to the genuine file, so the bytes behind it are "
       "correct and only the path form differs",
       "REFUSE",
       "KIMI-V6 F5: the refusal is now O_NOFOLLOW on the open itself rather than an lstat "
       "before it, so there is no window between the check and the read",
       mentions="symlink", direct="load_pinned_counts")
def f05(c):
    link = c.dir / "counts_nofollow.csv"
    if link.is_symlink() or link.exists():
        link.unlink()
    link.symlink_to(PREREG / c.pins["PINNED_COUNTS_REL"])
    c.redirect("PINNED_COUNTS_REL", "counts_nofollow.csv")
    return c.mod.load_pinned_counts()


@probe("B04", "the worker started without -I",
       "the same worker invoked by an ordinary interpreter rather than an isolated one",
       "REFUSE", "an un-isolated interpreter can inherit state the boundary exists to exclude",
       # v8 (my own doing): F2 rewrote this refusal's wording and the probe still asserted the
       # word "isolated", which now appears only as a payload KEY. Third round running that a
       # version change broke a probe's expectation and the mentions guard caught it. The
       # substring is now the flag itself, which the refusal names by construction, and the real
       # assertion moved to the structured payload where wording cannot drift.
       mentions="-I", direct="closure_worker_v9.py subprocess",
       verify=lambda o, r: (r.get("isolated") is False and len(r.get("sys_path") or []) > 0,
                            f"payload records isolated=False and {len(r.get('sys_path') or [])} "
                            f"sys.path entries — the refusal carries interpreter state (KIMI-V8 F3)"))
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
       mentions="SUBJECT DIGEST MISMATCH", direct="closure_worker_v9.py subprocess")
def b05(c):
    (c.dir / WORKER.name).write_bytes(WORKER.read_bytes())
    subject = SUBJECT.read_text() + "\n# an added line changes the digest\n"
    # Derived from SUBJECT.name, not spelled out: the v6->v7 bump left this hardcoded and the
    # copied worker looked for a file the probe had not written, so it refused with "subject
    # missing" instead of a digest mismatch. The probe still refused, for the wrong reason —
    # which is exactly what the `mentions` guard exists to catch.
    (c.dir / SUBJECT.name).write_text(subject)
    proc = subprocess.run([sys.executable, "-I", str(c.dir / WORKER.name)],
                          input='{"manifest": []}', capture_output=True, text=True)
    out = json.loads(proc.stdout)
    if out.get("outcome") == "WORKER-ERROR":
        raise c.mod.ManifestClosureError(out["message"], out)
    return out


# ------------------------------------------------------------------ F2: planner state
@probe("W01", "the worker started without -I, in an environment carrying a poisoned import",
       "a fake numpy package whose module-level code writes a sentinel file is placed on "
       "PYTHONPATH and the worker is run by an ordinary interpreter; the probe requires BOTH "
       "the refusal AND that the sentinel was never written",
       "REFUSE",
       "KIMI-V7 F2: the isolation check ran after the subject import, so the untrusted "
       "environment executed first — that seat's sentinel fired and the worker then died with "
       "an uncaught traceback instead of a receipt",
       mentions="refusing before reading or importing",
       direct="closure_worker_v9.py subprocess",
       verify=lambda o, r: (r.get("sentinel_written") is False,
                            "the poisoned import never executed"))
def w01(c):
    poison = c.dir / "poison"
    (poison / "numpy").mkdir(parents=True, exist_ok=True)
    sentinel = c.dir / "poison_fired.txt"
    (poison / "numpy" / "__init__.py").write_text(
        f"open({str(sentinel)!r}, 'w').write('fired')\n")
    env = dict(os.environ, PYTHONPATH=str(poison))
    proc = subprocess.run([sys.executable, str(WORKER)], input='{"manifest": []}',
                          capture_output=True, text=True, env=env)
    try:
        out = json.loads(proc.stdout)
    except ValueError:
        out = {"outcome": "NO-JSON", "message": (proc.stderr or proc.stdout)[:300]}
    out["sentinel_written"] = sentinel.exists()
    if out.get("outcome") in ("WORKER-ERROR", "NO-JSON"):
        raise c.mod.ManifestClosureError(out.get("message", "worker refused"), out)
    return out


@probe("W02", "the subject file counted, once when only hashed and once through a full closure",
       "nothing about the artifacts; the worker is run twice under a Python audit hook that "
       "counts file events naming the subject — first with --self-check, which never imports, "
       "then on a real closure",
       "PASS",
       "KIMI-V7 F1: the worker hashed the subject's bytes and then imported the PATH, a second "
       "read with a window between. The counts must be EQUAL — a real run may not touch the "
       "file more than a run that only hashes it",
       direct="closure_worker_v9.py under sys.addaudithook",
       verify=lambda o, r: (r["self_check_events"] == r["full_run_events"],
                            f"{r['self_check_events']} events hashing, "
                            f"{r['full_run_events']} through a whole closure — equal"))
def w02(c):
    def count(argv, stdin):
        probe_src = (
            "import sys\n"
            "n=[0]\n"
            "def hook(e,a):\n"
            f"    if e in ('open','exec','compile') and a and str(a[0]).endswith({SUBJECT.name!r}):\n"
            "        n[0]+=1\n"
            "sys.addaudithook(hook)\n"
            f"sys.argv={argv!r}\n"
            "import runpy\n"
            "try:\n"
            f"    runpy.run_path({str(WORKER)!r}, run_name='__main__')\n"
            "except SystemExit:\n"
            "    pass\n"
            "print('EV', n[0], file=sys.stderr)\n")
        r = subprocess.run([sys.executable, "-I", "-c", probe_src], input=stdin,
                           capture_output=True, text=True)
        line = [l for l in r.stderr.splitlines() if l.startswith("EV ")]
        if not line:
            raise AssertionError(f"probe produced no count: {r.stderr[-200:]}")
        return int(line[-1].split()[1])
    wd = c.dir / "w02_work"
    wd.mkdir(exist_ok=True)
    self_check = count([str(WORKER), "--self-check"], "")
    full = count([str(WORKER), "--work-dir", str(wd)], '{"manifest": []}')
    return {"self_check_events": self_check, "full_run_events": full}


@probe("W03", "the interpreter state a receipt is claimed to carry",
       "nothing about the artifacts; a normal closure through the boundary, inspected for the "
       "provenance two written claims say every receipt records",
       "PASS",
       "KIMI-V8 F3: the v8 fix correctly refused before provenance existed and closure_receipt "
       "dropped it anyway, so `sys_path` appeared in zero receipts while the worker docstring "
       "and this suite's own not_covered list both said it appeared in every one. The claim is "
       "made true here rather than narrowed, and this probe is what makes it checkable",
       verify=lambda o, r: (len(((r.get("worker_provenance") or {}).get("sys_path")) or []) > 0
                            and (r.get("worker_provenance") or {}).get("isolated") is True
                            and bool((r.get("worker_provenance") or {}).get("pinned_site_dir")),
                            f"{len(((r.get('worker_provenance') or {}).get('sys_path')) or [])} "
                            f"sys.path entries, isolated=True, add-back named"))
def w03(c):
    return c.mod.closure_receipt(c.required)


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
       "a timer thread moves adapter.INTERSECTION_AREA_THRESHOLD_SOURCE_PIX2 from 1e-8 to 2e-8 "
       "100 s into the call — a valid value that changes the digest without breaking the "
       "planner — so the digest was correct when close_manifest checked it and wrong by the "
       "time the plan finished. The probe asserts the mutation actually fired",
       "REFUSE",
       "CODEX-V5 F2: N01-N04 catch mutation before the check; the plan's own duration was "
       "unguarded, and a plan over 65,060 objects takes about 77 seconds",
       mentions="PLANNER CHANGED DURING THE PLAN",
       direct="close_manifest (in-process, so the mutation can be timed)",
       verify=lambda o, r: (r.get("planner_before") != r.get("planner_after"),
                            "the refusal reports both digests and they differ"))
def n05(c):
    # The first version of this probe wrapped plan_candidate_bricks on the module object
    # returned by _frozen_planner(). That call re-executes the module, so close_manifest held a
    # DIFFERENT instance, the wrapper never ran, no mutation happened, and the probe passed
    # while testing nothing. The adapter module is the shared one — mutate that, and time it
    # with a clock rather than a call count.
    # Rebinding a helper to a stub made the planner raise mid-plan, so the call was refused by
    # the fail-closed handler and never reached the post-plan digest check — a refusal for the
    # wrong reason. A different VALID threshold changes the digest and lets the plan finish.
    adapter = c.mod._frozen_planner()._adapter()
    original = adapter.INTERSECTION_AREA_THRESHOLD_SOURCE_PIX2
    fired = {"yes": False}

    def mutate():
        adapter.INTERSECTION_AREA_THRESHOLD_SOURCE_PIX2 = original * 2.0
        fired["yes"] = True

    # 100 s, not 20: the call spends ~47 s verifying the sidecar and ~15 s parsing the count
    # table, selection and parent BEFORE require_pinned_planner() runs. A mutation at 20 s
    # landed ahead of the pre-check and was refused there, which tests N04 over again rather
    # than the plan's own duration.
    timer = threading.Timer(100.0, mutate)
    timer.start()
    try:
        result = c.mod.close_manifest(c.required, snapshot_dir=c.dir)
    except c.mod.ManifestClosureError:
        if not fired["yes"]:
            raise AssertionError("probe is vacuous: the timed mutation never fired, so the "
                                 "refusal cannot be attributed to it")
        raise
    finally:
        timer.cancel()
        adapter.INTERSECTION_AREA_THRESHOLD_SOURCE_PIX2 = original
    if not fired["yes"]:
        raise AssertionError("probe is vacuous: the timed mutation never fired")
    return result


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
       direct="closure_worker_v9.py --self-check plus one boundary call")
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


def normalise_deep(value, rundir):
    """Rewrite the run directory out of every string in a structure.

    KIMI-V6 F2: `normalise()` was applied to the message and not to the result, and F03/F04's
    refusal payloads carry the path of a per-process run directory. Three same-mode runs
    therefore produced three stable hashes over byte-identical evidence — a false mismatch on
    honest runs. Everything hashed is normalised now.
    """
    if isinstance(value, str):
        return normalise(value, rundir)
    if isinstance(value, dict):
        return {k: normalise_deep(v, rundir) for k, v in value.items()}
    if isinstance(value, list):
        return [normalise_deep(v, rundir) for v in value]
    return value


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
        # KIMI-V6 F1: the hooks were registered and never called. The suite's conformance was
        # exactly as narrow as v5's while the brief told two referee seats otherwise. The hook
        # runs on the LIVE result, not the receipt's truncated copy, and its verdict is folded
        # into conformance rather than recorded beside it.
        verify_note, verify_ran = None, False
        if p["verify"] is not None:
            verify_ran = True
            try:
                ok, verify_note = p["verify"](out["actual"], out["result"])
            except BaseException as exc:  # noqa: BLE001 — a hook that raises has failed
                ok, verify_note = False, f"verify hook raised {type(exc).__name__}: {exc}"
            conforms = bool(conforms and ok)
        rows.append({**{k: p[k] for k in ("id", "label", "varies", "expect", "basis", "direct",
                                          "dispute")},
                     "actual": out["actual"], "conforms": conforms,
                     "mentions_required": p["mentions"],
                     "verify_declared": p["verify"] is not None,
                     "verify_ran": verify_ran,
                     "verify_note": normalise(verify_note, rundir) if verify_note else None,
                     "message": normalise(out["message"], rundir)[:400],
                     "result": normalise_deep(jsonable(out["result"]), rundir),
                     "seconds": out["seconds"]})

    nonconforming = [r["id"] for r in rows if r["conforms"] is False]
    errors = [r["id"] for r in rows if r["actual"] == "ERROR"]
    stable = {
        "receipt_version": "2",
        "subject": {"path": "../ref/successor_ref_v9.py", "sha256": sha256_of(SUBJECT)},
        "suite": {"path": "closure_probe_suite_v9.py", "sha256": sha256_of(Path(__file__))},
        "fixtures": {"path": "../ref/FIXTURES_V9_20260826.out",
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
                    "unexpected_error_type": errors,
                    # Computed, not asserted: a hook that is declared and never invoked is the
                    # v6 defect, so the receipt carries both counts and their equality.
                    "verify_hooks_declared": sum(1 for r in rows if r["verify_declared"]),
                    "verify_hooks_ran": sum(1 for r in rows if r["verify_ran"]),
                    "verify_hooks_all_ran": all(r["verify_ran"] for r in rows
                                                if r["verify_declared"])},
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
