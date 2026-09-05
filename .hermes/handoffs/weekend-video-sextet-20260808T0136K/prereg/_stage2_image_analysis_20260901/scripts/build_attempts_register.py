#!/usr/bin/env python3
"""ATTEMPTS REGISTER — generated from lane bytes, never by hand (Blanc 2026-09-05 21:02 KST). Three sections:
INSTRUMENTS VALIDATED, PRE-COMMITMENT DRAFTS REFUSED, CONTROLS RUN. Every row names its source file; every digest is
recomputed from the file on disk (never copied from prose); a row whose source cannot be read prints UNSOURCED.
Usage: build_attempts_register.py  -> writes ATTEMPTS_REGISTER_20260905.md beside the lane's other records."""
import json, re, hashlib, subprocess, sys, time, os
from pathlib import Path
LANE = Path(__file__).resolve().parent.parent; os.chdir(LANE); PREREG = LANE.parent
def sha(p):
    p = Path(p)
    if not p.is_file(): return None
    h = hashlib.sha256()
    with open(p, "rb") as fh:
        for c in iter(lambda: fh.read(1 << 20), b""): h.update(c)
    return h.hexdigest()
def short(d): return "UNSOURCED" if d is None else d[:16] + "…"
def jload(p):
    try: return json.loads(Path(p).read_text())
    except Exception: return None
def line2(p):
    try: return Path(p).read_text().split("\n")[1].strip()
    except Exception: return "UNSOURCED"
def access_ok(report, target):
    try: first = Path(report).read_text().split("\n")[0]
    except Exception: return "UNSOURCED"
    m = re.match(r"ACCESS_SHA=([0-9a-f]{64})", first); t = sha(target)
    return "UNSOURCED" if not m or t is None else ("verifies" if m.group(1) == t else "DOES NOT VERIFY")
def first_fatal(report):
    """Return (verbatim heading line, its 1-based line number, first non-empty following line as a MARKED excerpt)."""
    try: lines = Path(report).read_text().split("\n")
    except Exception: return "UNSOURCED"
    for i, ln in enumerate(lines):
        # a numbered heading with [FATAL] on the same line, OR a numbered heading whose next non-empty line starts with [FATAL] (codex style)
        nxt_lines = [x.strip() for x in lines[i+1:i+3] if x.strip()]
        if re.match(r"\s*\d+\.", ln) and "[FATAL]" not in ln and nxt_lines and nxt_lines[0].startswith("[FATAL]"):
            return f"verbatim line {i+1}: `{ln.strip().replace('|','/')}` · next line (verbatim): `{nxt_lines[0][:160].replace('|','/')}`"
        if "[FATAL]" in ln and re.match(r"\s*\d+\.", ln):
            head = ln.strip().replace("|", "/")
            rest = [x.strip() for x in lines[i+1:i+8] if x.strip()]
            nxt = rest[0] if rest else ""
            if nxt.endswith(":") and len(rest) > 1: nxt = nxt + " " + rest[1]
            return f"verbatim line {i+1}: `{head}` · excerpt (not verbatim, first following line, truncated): {nxt[:160].replace('|', '/')}…"
    return "no [FATAL] item in report"
out = []; W = out.append
W(f"# ATTEMPTS REGISTER — generated {time.strftime('%Y-%m-%d %H:%M KST')} by scripts/build_attempts_register.py from lane bytes")
W("Rules: every row carries its source file; every digest is recomputed from disk at generation time; unreadable sources print UNSOURCED. This file is derived, not maintained — regenerate, do not edit.\n")

# ---------------- INSTRUMENTS VALIDATED ----------------
W("## 1. INSTRUMENTS VALIDATED\n")
W("| # | instrument | frozen | gate faced | outcome | deciding numbers (m, k/m, bar) | source files (digests recomputed) |"); W("|---|---|---|---|---|---|---|")
R = jload("VALIDATION_GATE_RECEIPT_9B13_20260905.json")
w_sha = sha(PREREG / "weights_frozen.pt"); r_sha = sha(PREREG / "_inference_20260820/inference_runner.py")
if R:
    c, s = R["counts"], R["statistic"]
    frozen = "weights pinned in V13 (signed 2026-09-04) as flagship K8 artefact; K8_CROSSING_AUTHORIZATION_20260820.md (" + short(sha(PREREG / "K8_CROSSING_AUTHORIZATION_20260820.md")) + ")"
    W(f"| 1 | CE-ResNet chirality scorer: weights `{short(w_sha)}` (receipt says {short(R['instrument'].get('weights_sha256'))}), runner `{short(r_sha)}`; trained 10.6 min on 20,000 synthetic spirals (source: ../train_results.json {short(sha(PREREG/'train_results.json'))}) | {frozen} | V35 §9B (signed §17.2 digest {short(R.get('signed_digest_17_2'))}), run once {R['start_utc']}–{R['end_utc']} | **{R['gate_program_verdict']}** (validation_gate_pass = {R['validation_gate_pass']}); §9B.11 UNFIT | m = {c['scored_m']} (floor {s['floor_m']}; r = {c['refused_r']}); k = {c['k']}, k/m = {s['p_raw']:.6f}; bar: Wilson lower > {s['threshold']} (not computed — floor failed first; informational upper {s['wilson_upper']:.4f}); §9.7 {R['exact_rerun_9_7']['token']} ({R['exact_rerun_9_7']['nondeterministic']} of {R['exact_rerun_9_7']['objects']}) | VALIDATION_GATE_RECEIPT_9B13_20260905.json (file {short(sha('VALIDATION_GATE_RECEIPT_9B13_20260905.json'))}; its canonical receipt_sha256 field, sealed as journal record 62: {short(R.get('receipt_sha256'))} — the two differ by construction because the field is inserted after hashing); STAGE2_9B_FORMAL_RESULT_20260905.md {short(sha('STAGE2_9B_FORMAL_RESULT_20260905.md'))}; per-object {short(sha('VALIDATION_PER_OBJECT_9B13_20260905.jsonl'))} |")
else:
    W("| 1 | CE-ResNet | UNSOURCED | UNSOURCED | UNSOURCED | UNSOURCED | VALIDATION_GATE_RECEIPT_9B13_20260905.json missing |")
fam = sha("_optionA_dev/fourier_chirality/fourier_chirality.py")
W(f"| — | (candidate, NOT validated) 2DFFT-class Fourier family `{short(fam)}`, 96 configurations, driver `{short(sha('_optionA_dev/fourier_chirality/run_configurations.py'))}` | not frozen (development code; selection rule unsigned) | none — no development corpus exists, no tuning, no holdout, no §9B | no attempt | — | OPTION_A_INSTRUMENT_SELECTION_RULE_DRAFT_V5_20260905.md {short(sha('OPTION_A_INSTRUMENT_SELECTION_RULE_DRAFT_V5_20260905.md'))} |")
W(f"\nInstruments validated: **1**. Attempts under §9B: **1**. Candidates pinned in a signed rule: **0**.\n")

# ---------------- PRE-COMMITMENT DRAFTS ----------------
import glob as _glob
versions = sorted(int(re.search(r"_V(\d+)_", f).group(1)) for f in _glob.glob("OPTION_A_INSTRUMENT_SELECTION_RULE_DRAFT_V*_2026*.md"))
W(f"## 2. PRE-COMMITMENT DRAFTS REFUSED (selection rule V1–V{max(versions)})\n")
W("| draft | digest (recomputed) | seat A (agy) | seat B (codex) | access proofs | the fatal that killed it — first [FATAL] heading of a NOT-SIGNABLE report, VERBATIM with line number; the excerpt after it is a marked non-verbatim paraphrase | superseded by / record |"); W("|---|---|---|---|---|---|---|")
def rep(seat, v):
    c = _glob.glob(f"{seat}_SELRULE_V{v}_SEAT?.md"); return c[0] if c else None
def change_record(v):
    c = _glob.glob(f"MINI_PREREG_SELRULE_V{v}_TO_V{v+1}_CHANGE_RECORD_2026*.md"); return c[0] if c else None
n_refused = 0; n_gated = 0
for v in versions:
    f = (_glob.glob(f"OPTION_A_INSTRUMENT_SELECTION_RULE_DRAFT_V{v}_2026*.md") or [f"OPTION_A_INSTRUMENT_SELECTION_RULE_DRAFT_V{v}_MISSING.md"])[0]; d = sha(f); a, b = rep("AGY", v), rep("CODEX", v); cr = change_record(v)
    if a is None and b is None:
        note = ("GATE PENDING — no seat report filed yet" if v == max(versions) else "superseded before any gate") + (": SpArcFiRe (proposed primary) needs MATLAB Compiler Runtime R2017a — source OPTION_A_CANDIDATE_INSTRUMENT_SURVEY_20260905.md" if v == 1 else "")
        W(f"| V{v} | {short(d)} | {'pending' if v == max(versions) else 'not gated'} | {'pending' if v == max(versions) else 'not gated'} | — | {note} | {('V'+str(v+1)+'; '+cr+' '+short(sha(cr))) if cr else ('—' if v == max(versions) else 'V'+str(v+1))} |"); continue
    n_gated += 1; va, vb = (line2(a) if a else "no report"), (line2(b) if b else "no report")
    fatal_src = b if (b and "NOT-SIGNABLE" in vb) else (a if (a and "NOT-SIGNABLE" in va) else None)
    fat = first_fatal(fatal_src) if fatal_src else "no seat returned NOT-SIGNABLE"
    if "NOT-SIGNABLE" in va or "NOT-SIGNABLE" in vb: n_refused += 1
    stop = sorted(_glob.glob(f"V{v}_GATE_OUTCOME_*2026*.md"))
    sup = (f"V{v+1}; {cr} {short(sha(cr))}" if cr else "none yet") + (f"; {stop[0]} {short(sha(stop[0]))}" if stop else "")
    W(f"| V{v} | {short(d)} | {va.replace('VERDICT: ','')} ({a}) | {vb.replace('VERDICT: ','')} ({b}) | A {access_ok(a, f) if a else '—'}; B {access_ok(b, f) if b else '—'} | {fat} | {sup} |")
splits = [f"V{v}" for v in versions if rep("AGY", v) and rep("CODEX", v) and (("NOT-SIGNABLE" in line2(rep("AGY", v))) != ("NOT-SIGNABLE" in line2(rep("CODEX", v))))]
W(f"\nDrafts written: **{len(versions)}**. Gated: **{n_gated}**. Refused (at least one seat NOT-SIGNABLE): **{n_refused}**. Signed: **0**. Split rounds: {', '.join(splits) or 'none'}.\n")

# ---------------- CONTROLS RUN ----------------
W("## 3. CONTROLS RUN\n")
W("| control | what was exhibited | by whom | outcome | source (digest recomputed) |"); W("|---|---|---|---|---|")
S1 = jload("STAGE1_RENDERER_PARITY_FIXTURE_RECEIPT_20260905.json")
if S1: W(f"| §10 renderer parity + configuration fixture (stage 1) | renderer preserves parity/orientation on a synthetic input; render_config == §8 constants; establishes_absolute_sign = {S1.get('establishes_absolute_sign')} | lane-run, journalled (record 61, predecessor {short(S1.get('predecessor_receipt_digest'))}) | {S1.get('verdict') or S1.get('status')} | STAGE1_RENDERER_PARITY_FIXTURE_RECEIPT_20260905.json {short(sha('STAGE1_RENDERER_PARITY_FIXTURE_RECEIPT_20260905.json'))} |")
else: W("| §10 renderer parity fixture | UNSOURCED | | | STAGE1 receipt missing |")
def run_tests(cwd, mods):
    try:
        p = subprocess.run([sys.executable, "-m", "unittest"] + mods, cwd=cwd, capture_output=True, text=True, timeout=600); m = re.search(r"Ran (\d+) tests", p.stderr)
        return f"{m.group(1) if m else '?'} tests, {'OK' if p.returncode == 0 else 'FAILED'}"
    except Exception as e: return f"UNSOURCED ({e!r})"
W(f"| §9B.7a validation_gate fixture — reachable FAIL (floor; strength) and PASS (k=1441 vs 1440) | pinned program `{short(sha('miniprereg_pins/validation_gate.py'))}` exhibits both outcomes by running them | lane-pinned; re-run now | {run_tests('miniprereg_pins', ['test_validation_gate'])} | miniprereg_pins/test_validation_gate.py {short(sha('miniprereg_pins/test_validation_gate.py'))} |")
c27 = Path("CODEX_V27_SEATB_20260905.md"); hit = "0.6795" in c27.read_text() if c27.is_file() else False
W(f"| §9B reachability, seat-authored (V27 gate): k = 1,400 → p = 0.6795 → FAIL constructed independently | a seat built its own §9B failure before the gate ran | seat B (codex), V27 | {'exhibited' if hit else 'UNSOURCED (string not found)'} | CODEX_V27_SEATB_20260905.md {short(sha(c27))} |")
W(f"| §9B reachability, both directions, every round V31–V35 (brief questions 'can §9B PASS and FAIL') | both seats constructed PASS and FAIL each round | seats A+B | recorded in each round's report | AGY_V35_SEATA_20260905.md {short(sha('AGY_V35_SEATA_20260905.md'))}; CODEX_V35_SEATB_20260905.md {short(sha('CODEX_V35_SEATB_20260905.md'))} (access proofs vs archived as-delivered: A {access_ok('AGY_V35_SEATA_20260905.md','_scratch/signing/V35_AS_DELIVERED_59e89f97_20260905.md')}, B {access_ok('CODEX_V35_SEATB_20260905.md','_scratch/signing/V35_AS_DELIVERED_59e89f97_20260905.md')}) |")
if R: W(f"| refusal breakdown of attempt 1 | 205 refusals by cause: {json.dumps(R['counts']['refusal_breakdown'])} | COUNTS: read by this script from the sealed receipt JSON (machine). NARRATIVE: STAGE2_REFUSAL_BREAKDOWN_20260905.md is Hwao's prose (lane owner, not a referee seat) | all 205 are pre-instrument refusals (receipt causes) | VALIDATION_GATE_RECEIPT_9B13_20260905.json (counts); STAGE2_REFUSAL_BREAKDOWN_20260905.md {short(sha('STAGE2_REFUSAL_BREAKDOWN_20260905.md'))} (narrative) |")
dec = "_optionA_dev/refusal_bit_decomposition_20260905.jsonl"; cov = "_optionA_dev/coverage_refusal_geometry_20260905.jsonl"
def has_label(p):
    try: return any(('"g"' in l or '"match"' in l) for l in open(p))
    except Exception: return None
W(f"| mask-bit decomposition of the 159 pixel-decided refusals (no labels) | which bits drive refusals (MEDIUM 93/103); alternative-rule recoveries → m = 1,877 / 1,801 / 1,908 | lane-produced; recomputed exactly by seat A and seat B at the V2 gate (item 6 of each) | label field present: {has_label(dec)} / {has_label(cov)} (must be False) | {dec} {short(sha(dec))}; {cov} {short(sha(cov))}; AGY_SELRULE_V2_SEATA.md, CODEX_SELRULE_V2_SEATB.md |")
W(f"| §9.7 exact rerun of attempt 1 (binary32 bit pattern) | {R['exact_rerun_9_7'] if R else 'UNSOURCED'} | lane-run (two inference runs) | {R['exact_rerun_9_7']['token'] if R else 'UNSOURCED'} | validation_inference_run1/2_20260905/results.jsonl {short(sha('validation_inference_run1_20260905/results.jsonl'))} / {short(sha('validation_inference_run2_20260905/results.jsonl'))} |")
W(f"| candidate estimator fixture (development code) | antisymmetry finite/unequal; tie = 0 not a score; determinism; 96 distinct ordered configurations; out-of-grid + extra-key refusal | lane-run now; also run by seat A (V4: 10 OK) and seat B (V5: 19 OK incl. driver fixture) | {run_tests('_optionA_dev/fourier_chirality', ['test_fourier_chirality'])} | _optionA_dev/fourier_chirality/test_fourier_chirality.py {short(sha('_optionA_dev/fourier_chirality/test_fourier_chirality.py'))} |")
W(f"| candidate driver fixture (development code) | env-lock refusal; manifest shape refusals; no floor flag; unscored = miss; floor both sides; tie-break levels; holdout one-config, floor-CLOSED, overlap refusal, inconsistent-substitution refusal; PASS reachable | lane-run now; seat B ran it (V5) | {run_tests('_optionA_dev/fourier_chirality', ['test_run_configurations'])} — NOT exhibited: coherent winner substitution and manifest identity (OPTION_A_SELRULE_V5_ERRATA_20260905.md items 3–4); deterministic `CLOSED: holdout strength` (CODEX_SELRULE_V5_SEATB.md item 5, not in the errata) | _optionA_dev/fourier_chirality/test_run_configurations.py {short(sha('_optionA_dev/fourier_chirality/test_run_configurations.py'))}; OPTION_A_SELRULE_V5_ERRATA_20260905.md |")
W(f"| synthetics smoke test (three estimators, six degradation conditions) | construction check only — NOT fitness evidence (CE-ResNet: 100% synthetic / 54.7% real) | lane-run | table in file | OPTION_A_SYNTHETICS_SMOKE_20260905.md {short(sha('OPTION_A_SYNTHETICS_SMOKE_20260905.md'))}; _optionA_dev/fourier_chirality/synthetics_smoke_results_20260905.json {short(sha('_optionA_dev/fourier_chirality/synthetics_smoke_results_20260905.json'))} |")
W(f"| seat-report access proofs (10) | each ACCESS_SHA recomputed against lane bytes | lane-verified | see index | SEAT_REPORT_ACCESS_PROOF_INDEX_20260905.md {short(sha('SEAT_REPORT_ACCESS_PROOF_INDEX_20260905.md'))} |")
W("\n## 4. Counts a methods section must carry (derived above)")
W(f"- Instruments validated under a signed preregistration: 1 (CE-ResNet) — FAILED. Candidates developed but not validated: 1 family, 0 attempts.")
W(f"- Pre-commitment drafts for a replacement: {len(versions)} written, {n_gated} gated by two blind seats on different engines, {n_refused} refused, 0 signed; the third-failure rule engaged twice (V4 by Blanc's count, V10 by Hwao's); pending the principal's ruling.")
W(f"- Frozen-sample access, as far as the journals show: no render or inference event for any frozen-sample object exists in the render journal ({sum(1 for l in open('validation_render_journal_20260905.jsonl') if 'frozen' in l) if Path('validation_render_journal_20260905.jsonl').is_file() else 'UNSOURCED'} rows) or the 62-record seal journal; at generation time, in the lane, the only tensor files outside the validation directory number {len([p for p in Path('.').rglob('*.ic6') if 'validation_tensors_20260905' not in str(p)])} (the synthetic smoke tensor under _scratch/synth_smoke, if present). This is what the records show; it is not a proof that no person viewed a frozen pixel by a route the journals do not see — that limit is stated in CUSTODIAN_QUESTION_FOR_DUHO_20260905.md.")
Path("ATTEMPTS_REGISTER_20260905.md").write_text("\n".join(out) + "\n"); print("\n".join(out))
