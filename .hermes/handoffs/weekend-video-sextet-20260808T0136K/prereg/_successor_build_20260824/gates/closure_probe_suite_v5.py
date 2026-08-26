#!/usr/bin/env python3
"""CLOSURE PROBE SUITE V5 — negative controls for the repaired closure check.

WHAT CHANGED SINCE V4
---------------------
The V4 review (CLOSURE_RECEIPT_GPT56.md, CLOSURE_RECEIPT_CODEX.md) found one defect in three
places: the count table, the selection and the parent were all nominated by the caller, so the
artifact that judged the manifest was chosen by whoever presented it. `close_manifest` now takes
ONE argument — the candidate manifest — and loads everything else from a pinned path with a
pinned digest. So the V4 probes that edited those inputs cannot be written at all any more.

They are replaced by REDIRECTION probes. Each points a pinned path constant at a copy inside
this run directory and checks that the digest gate refuses it. Where a probe wants to exercise
validation BEYOND the digest gate (schema, universe membership), it must also override the
pinned digest constant — otherwise the digest refuses first and the validator is never reached.
Every probe that does this declares it in its `varies` field, because the V4 review's F5/F6
were about exactly that: probe metadata that did not enumerate everything the probe changed.

WHAT IT DOES NOT DO
-------------------
It never writes outside `_tmp_closure_probe_run_<pid>/` in this directory, and it never modifies
a pinned artifact — redirection points a constant at a copy; the originals are untouched. Probes
marked `direct` call a binding helper rather than `close_manifest`; that is stated per probe
rather than in a suite-wide claim, which is the V4 F5 correction.

COST
----
`close_manifest` verifies the 366,912-brick sidecar (~47 s), parses the 270,577-row count table
and the 65,060-row parent, and — for probes that get that far — plans all 65,060 objects through
the frozen planner (~77 s). A probe that refuses before planning costs ~50 s; one that plans
costs ~185 s. The required manifest is derived ONCE in setup and reused, so the run is about 25
minutes. `--fast-geometry` memoises the sidecar after one verification; it is not the production
path and the receipt records the mode.

USAGE
-----
    python3 closure_probe_suite_v5.py --list
    python3 closure_probe_suite_v5.py --json RECEIPT.json
    python3 closure_probe_suite_v5.py --only D01,N01
"""
from __future__ import annotations

import argparse
import csv
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
SUBJECT = (HERE / ".." / "ref" / "successor_ref_v5.py").resolve()
FIXTURES = (HERE / ".." / "ref" / "FIXTURES_V5_20260826.out").resolve()
PREREG = HERE.resolve().parents[1]          # the directory pinned paths are relative to
DEFAULT_RUNDIR = HERE / f"_tmp_closure_probe_run_{os.getpid()}"

NOT_COVERED = [
    "Modification of a pinned artifact in place. Redirection probes point a path constant at a "
    "copy; nothing here writes to the sidecar, the count table, the selection or the parent.",
    "A change to an input file between its digest read and its data read. Each loader hashes "
    "and then re-opens; the window is real and untested.",
    "The download itself — byte integrity, retries, the transfer manifest.",
    "Whether the pinned selection is the selection the preregistration authorises. The suite "
    "checks that the artifact is fixed and unaltered, not that it is the right artifact; the "
    "selection carries a code pin only, with no producer receipt behind it (the parent has one).",
    "Concurrency. One process, one closure at a time.",
]


def load_subject():
    spec = importlib.util.spec_from_file_location("closure_probe_subject_v5", SUBJECT)
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


def probe(pid, label, varies, expect, basis, mentions=None, direct=None, dispute=None):
    """Register a probe.

    direct   name of the binding helper this probe calls instead of close_manifest, or None.
             Stated per probe because V4 claimed suite-wide that every probe used the
             production entry point while two did not (GPT56 F6, CODEX F5).
    """
    def deco(fn):
        PROBES.append({"id": pid, "label": label, "varies": varies, "expect": expect,
                       "basis": basis, "mentions": mentions, "direct": direct,
                       "dispute": dispute, "fn": fn})
        return fn
    return deco


class Ctx:
    """Derives the required manifest once, and builds redirection copies on demand."""

    def __init__(self, mod, rundir):
        self.mod, self.dir = mod, rundir
        self.rel_base = f"_successor_build_20260824/gates/{rundir.name}"
        self.pins = {k: getattr(mod, k) for k in
                     ("PINNED_COUNTS_REL", "PINNED_COUNTS_SHA256", "PINNED_SELECTION_REL",
                      "PINNED_SELECTION_SHA256", "PINNED_PARENT_REL", "PINNED_PARENT_SHA256",
                      "PINNED_PARENT_RECEIPTS_REL")}
        # The required manifest is what the check itself derives; nothing supplies it.
        try:
            mod.close_manifest([])
            raise RuntimeError("an empty manifest was accepted; setup cannot continue")
        except mod.ManifestClosureError as exc:
            self.required = sorted(exc.result["missing_from_manifest"])
            self.setup_result = {k: exc.result[k] for k in
                                 ("objects", "selected_bricks", "required_count")}

    def restore(self):
        for k, v in self.pins.items():
            setattr(self.mod, k, v)

    def redirect(self, const, filename, sha_const=None, sha_value=None):
        """Point a pinned path constant at a file in the run directory."""
        setattr(self.mod, const, f"{self.rel_base}/{filename}")
        if sha_const:
            setattr(self.mod, sha_const,
                    sha_value if sha_value else sha256_of(self.dir / filename))

    # ---- copies of the pinned artifacts, altered in one stated way -----------------------
    def counts_copy(self, name, mutate):
        src = PREREG / self.pins["PINNED_COUNTS_REL"]
        rows = list(csv.reader(src.open()))
        rows = mutate(rows)
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
        rows = list(csv.reader(src.open()))
        rows = mutate(rows)
        out = self.dir / name
        with out.open("w", newline="") as f:
            csv.writer(f).writerows(rows)
        return out


# --------------------------------------------------------------------------- controls
@probe("P01", "the manifest the check itself derived, complete",
       "nothing; the control that the pinned artifacts close against each other",
       "PASS", "the closure must accept the brick set it computes from the pinned parent")
def p01(c):
    r = c.mod.close_manifest(c.required)
    return {k: r[k] for k in ("objects", "selected_bricks", "required_count", "manifest_count",
                              "plan_digest", "parent_sha256", "selection_sha256",
                              "counts_sha256")}


@probe("R01", "manifest with one required brick removed",
       "one brickname dropped from the candidate manifest; nothing else",
       "REFUSE", "the 60,308-vs-60,310 failure this check exists to prevent",
       mentions="missing 1")
def r01(c):
    return c.mod.close_manifest(c.required[1:])


@probe("R02", "manifest with 100 required bricks removed",
       "one hundred bricknames dropped from the candidate manifest; nothing else",
       "REFUSE",
       "GPT56-V5 I3: the message shows only four examples, so the structured result must carry "
       "the full set — this probe exists to check that it does",
       mentions="missing 100")
def r02(c):
    return c.mod.close_manifest(c.required[100:])


@probe("R03", "manifest carrying a brick no object requires",
       "one brickname added to the candidate manifest; nothing else",
       "REFUSE", "an over-broad manifest downloads bricks the study did not ask for",
       mentions="extra")
def r03(c):
    return c.mod.close_manifest(c.required + ["0001p000"])


@probe("R04", "manifest listing the same brickname twice",
       "one duplicate entry in the candidate manifest; nothing else",
       "REFUSE", "close_manifest's explicit duplicate-brickname refusal",
       mentions="duplicate")
def r04(c):
    return c.mod.close_manifest(c.required + [c.required[0]])


@probe("R05", "empty manifest",
       "the candidate manifest replaced by an empty list; nothing else",
       "REFUSE", "an empty manifest closes nothing", mentions="missing")
def r05(c):
    return c.mod.close_manifest([])


@probe("R06", "manifest passed as None instead of a list",
       "the candidate manifest replaced by None; nothing else",
       "REFUSE", "malformed input must leave as one closure refusal")
def r06(c):
    return c.mod.close_manifest(None)


@probe("R07", "manifest of integers rather than bricknames",
       "every entry replaced by its index as an int; nothing else",
       "REFUSE", "CODEX-V5 F7: values are str()-converted, so wrong types must not silently pass",
       mentions="missing")
def r07(c):
    return c.mod.close_manifest(list(range(len(c.required))))


# --------------------------------------------------------------------------- digest gates
@probe("D01", "count table redirected to a copy with one brick's count moved to another row",
       "PINNED_COUNTS_REL points at the copy; the pinned digest constant is NOT changed",
       "REFUSE",
       "V4 C01 repaired: this is the input that passed when the table was a call argument",
       mentions="COUNT TABLE DIGEST MISMATCH")
def d01(c):
    def mutate(rows):
        rows[1][1] = str(int(rows[1][1]) - 1)
        rows[2][1] = str(int(rows[2][1]) + 1)
        return rows
    c.counts_copy("counts_moved.csv", mutate)
    c.redirect("PINNED_COUNTS_REL", "counts_moved.csv")
    return c.mod.close_manifest(c.required)


@probe("D02", "count table redirected through a symlink to that same copy",
       "PINNED_COUNTS_REL points at a symlink whose target is D01's file; digest unchanged",
       "REFUSE", "V4 C03 repaired: path form must not change the answer",
       mentions="COUNT TABLE DIGEST MISMATCH")
def d02(c):
    c.counts_copy("counts_moved2.csv", lambda rows: rows[:1] + [[rows[1][0], "0"]] + rows[2:])
    link = c.dir / "counts_link.csv"
    if link.is_symlink() or link.exists():
        link.unlink()
    link.symlink_to(c.dir / "counts_moved2.csv")
    c.redirect("PINNED_COUNTS_REL", "counts_link.csv")
    return c.mod.close_manifest(c.required)


@probe("D03", "selection redirected to a copy with one brick removed",
       "PINNED_SELECTION_REL points at the copy; the pinned digest constant is NOT changed",
       "REFUSE", "V4 C02 repaired: a selection reduced to match a shorter parent used to pass",
       mentions="SELECTION DIGEST MISMATCH")
def d03(c):
    c.selection_copy("selection_reduced.npz", lambda b: b[:-1])
    c.redirect("PINNED_SELECTION_REL", "selection_reduced.npz")
    return c.mod.close_manifest(c.required)


@probe("D04", "parent redirected to a copy with one row's identity and coordinates replaced",
       "PINNED_PARENT_REL points at the copy; the pinned digest constant is NOT changed",
       "REFUSE", "V4 C04 repaired: per-brick counts still balance, so only a digest catches it",
       mentions="PARENT DIGEST MISMATCH")
def d04(c):
    def mutate(rows):
        rows[2][0] = "99999999999999999"
        rows[2][3], rows[2][4] = rows[1][3], rows[1][4]
        return rows
    c.parent_copy("parent_swapped.csv", mutate)
    c.redirect("PINNED_PARENT_REL", "parent_swapped.csv")
    return c.mod.close_manifest(c.required)


@probe("D05", "parent redirected to that copy, with the pinned constant updated to match it",
       "PINNED_PARENT_REL points at the copy AND PINNED_PARENT_SHA256 is set to the copy's "
       "digest, leaving the fetch receipt as the only remaining witness",
       "REFUSE",
       "the parent has two independent bindings; defeating the code pin must not be enough",
       mentions="PARENT NOT THE FETCHED ARTIFACT")
def d05(c):
    c.parent_copy("parent_swapped2.csv",
                  lambda rows: rows[:2] + [rows[2][:1] + ["999999"] + rows[2][2:]] + rows[3:])
    c.redirect("PINNED_PARENT_REL", "parent_swapped2.csv", "PINNED_PARENT_SHA256")
    return c.mod.close_manifest(c.required)


# --------------------------------------------------------------------------- validators
@probe("S01", "count table with a duplicate brickid",
       "a copy with row 2's brickid set to row 1's, AND the pinned digest set to the copy's, so "
       "the schema validator is reached rather than the digest gate",
       "REFUSE", "CODEX-V5 F7.1: duplicate keys were silently overwritten by the dict build",
       mentions="duplicate brickid", direct="load_pinned_counts")
def s01(c):
    def mutate(rows):
        rows[2][0] = rows[1][0]
        return rows
    c.counts_copy("counts_dup.csv", mutate)
    c.redirect("PINNED_COUNTS_REL", "counts_dup.csv", "PINNED_COUNTS_SHA256")
    return c.mod.load_pinned_counts()


@probe("S02", "count table with a negative count",
       "a copy with row 1's count set to -1, AND the pinned digest set to the copy's",
       "REFUSE", "CODEX-V5 F7.1: negative counts were accepted",
       mentions="negative", direct="load_pinned_counts")
def s02(c):
    def mutate(rows):
        rows[1][1] = "-1"
        return rows
    c.counts_copy("counts_neg.csv", mutate)
    c.redirect("PINNED_COUNTS_REL", "counts_neg.csv", "PINNED_COUNTS_SHA256")
    return c.mod.load_pinned_counts()


@probe("S03", "count table whose total is not the pinned release total",
       "a copy with one count reduced by 1, AND the pinned digest set to the copy's",
       "REFUSE", "the release total is the one quantity pinned independently of the file",
       mentions="totals", direct="load_pinned_counts")
def s03(c):
    def mutate(rows):
        rows[1][1] = str(int(rows[1][1]) - 1)
        return rows
    c.counts_copy("counts_total.csv", mutate)
    c.redirect("PINNED_COUNTS_REL", "counts_total.csv", "PINNED_COUNTS_SHA256")
    return c.mod.load_pinned_counts()


@probe("S04", "count table with a row removed",
       "a copy without its last row, AND the pinned digest set to the copy's",
       "REFUSE", "the row count is pinned as well as the total",
       mentions="rows", direct="load_pinned_counts")
def s04(c):
    c.counts_copy("counts_short.csv", lambda rows: rows[:-1])
    c.redirect("PINNED_COUNTS_REL", "counts_short.csv", "PINNED_COUNTS_SHA256")
    return c.mod.load_pinned_counts()


@probe("S05", "count table with a renamed column",
       "a copy whose second column header is changed, AND the pinned digest set to the copy's",
       "REFUSE", "the column names are pinned; a renamed column is a different table",
       mentions="columns", direct="load_pinned_counts")
def s05(c):
    def mutate(rows):
        rows[0][1] = "n_something_else"
        return rows
    c.counts_copy("counts_cols.csv", mutate)
    c.redirect("PINNED_COUNTS_REL", "counts_cols.csv", "PINNED_COUNTS_SHA256")
    return c.mod.load_pinned_counts()


@probe("U01", "selection containing a brickid that is not in the pinned geometry universe",
       "a copy with one brickid replaced by 999999999, AND the pinned digest set to the copy's",
       "REFUSE", "CODEX-V5 F7.2: selection membership was never checked against geometry",
       mentions="absent from the pinned geometry universe")
def u01(c):
    def mutate(b):
        b = b.copy()
        b[0] = 999_999_999
        return b
    c.selection_copy("selection_alien.npz", mutate)
    c.redirect("PINNED_SELECTION_REL", "selection_alien.npz", "PINNED_SELECTION_SHA256")
    return c.mod.close_manifest(c.required)


@probe("U02", "parent row whose declared brick disagrees with its own coordinates",
       "a copy with the FIRST row's coordinates replaced by those of a row in a different "
       "brick, while its own brickid is left alone, AND the pinned digest set to the copy's, "
       "AND the fetch receipt's output digest redirected to match — so every custody binding is "
       "satisfied and only the row's internal consistency is wrong",
       "REFUSE",
       "the check derives the image list from each row's coordinates but never verifies that "
       "the row sits in the brick it claims; counts alone cannot see this",
       dispute="A referee may hold that a parent which passes every custody binding is by "
               "definition authorised, and that internal consistency belongs to the producer. "
               "If so, say which producer check enforces it, because nothing downstream does.")
def u02(c):
    def mutate(rows):
        # The parent is grouped by brick, so borrowing from an adjacent row lands inside the
        # SAME brick and tests nothing. The first version of this probe did exactly that and
        # reported a pass that meant nothing. Take coordinates from the last row instead, and
        # assert the two rows really are in different bricks before relying on the result.
        donor = rows[-1]
        assert donor[1] != rows[1][1], "donor row is in the same brick; probe would be vacuous"
        rows[1][3], rows[1][4] = donor[3], donor[4]
        return rows
    out = c.parent_copy("parent_incoherent.csv", mutate)
    rec = json.loads((PREREG / c.pins["PINNED_PARENT_RECEIPTS_REL"]).read_text())
    rec["output_sha256"] = sha256_of(out)
    (c.dir / "receipts_incoherent.json").write_text(json.dumps(rec))
    c.redirect("PINNED_PARENT_REL", "parent_incoherent.csv", "PINNED_PARENT_SHA256")
    c.redirect("PINNED_PARENT_RECEIPTS_REL", "receipts_incoherent.json")
    return c.mod.close_manifest(c.required)


# --------------------------------------------------------------------------- planner binding
@probe("N01", "the frozen planner's live plan_object replaced in memory",
       "adapter.plan_object is rebound to a function returning ['0001p000']; no file changes, "
       "and the prefilter constant is left alone",
       "REFUSE",
       "GPT56-V5 F4, demonstrated by that seat: the digest hashes source bytes on disk, so it "
       "can still match while different code produces the answer",
       mentions="PLANNER DIGEST MISMATCH", direct="require_pinned_planner")
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
       "REFUSE", "the prefilter is inside the pinned transitive digest",
       mentions="PLANNER DIGEST MISMATCH", direct="require_pinned_planner")
def n02(c):
    adapter = c.mod._frozen_planner()._adapter()
    original = adapter.CANDIDATE_PREFILTER_DEG
    try:
        adapter.CANDIDATE_PREFILTER_DEG = original + 0.01
        return c.mod.require_pinned_planner()
    finally:
        adapter.CANDIDATE_PREFILTER_DEG = original


@probe("G01", "the planner digest and pinned artifact digests this run actually observed",
       "nothing; recorded so the receipt carries the values rather than asserting them",
       "PASS", "a control that puts the bindings in the receipt", direct="several loaders")
def g01(c):
    _, sidecar = c.mod.load_pinned_geometry()
    _, counts = c.mod.load_pinned_counts()
    _, sel = c.mod.load_pinned_selection()
    _, par = c.mod.load_pinned_parent()
    return {"planner_digest": c.mod.require_pinned_planner(), "sidecar_sha256": sidecar,
            "counts_sha256": counts, "selection_sha256": sel, "parent_sha256": par}


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
            print(f"{p['id']:<5} {p['expect']:<7} {(p['direct'] or 'close_manifest'):<22} "
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
        "subject": {"path": "../ref/successor_ref_v5.py", "sha256": sha256_of(SUBJECT)},
        "suite": {"path": "closure_probe_suite_v5.py", "sha256": sha256_of(Path(__file__))},
        "fixtures": {"path": "../ref/FIXTURES_V5_20260826.out",
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
