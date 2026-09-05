# Standing design rules for BHU preregistrations — carried from R3D (V1–V31) and R3C2 (V1–V20), written 2026-09-05

These five rules cost R3D and R3C2 about fifty versions between them. Every new prereg in this lane starts with them at V1
and cites this file. A draft that lacks any of the five is not ready to freeze. Written at Blanc's 22:33 KST note.

## Rule 1 — C0 reachability, verbatim, seat-authored, lane-verified only
Before the first design gate, two independent seats (different engines) each produce an exhibition: for every declared
outcome class, one concrete input and the clause path that files it, quoting the document verbatim; any class with no such
input is UNREACHABLE and names its blocking clause. The lane owner never authors an exhibition and never repairs one; the
lane only verifies ACCESS_SHA after exit and checks that the two seats agree. The exhibitions are committed as files. A
document is not gated until C0 is PASS on both seats. (R3D lost V10 and V12 to unreachable classes discovered late; R3C2
caught two at V10 and none after.)

## Rule 2 — falsifier asymmetry: no PASS path carries a precondition the FAIL path lacks
For every outcome class that would count as the construction "passing" (consistent, derived, fixed, robust, stable), the
document lists every way the pipeline can go wrong — anchor mismatch, timeout, script exception, control failure, seat
disagreement, missing artefact — and states the class each lands on. None may land on the PASS class. The PASS class is filed
only from a positive printed artefact for every required item; a missing artefact is a failure, never a default. This is a
design rule in §4 of each prereg, not a note. (R3C2 V11–V16: several errors defaulted into the favourable reading.)

## Rule 3 — a declared cap before the first gate
Each prereg states, before it is gated, the condition that stops versioning and forces a filed diagnosis instead of another
Vn: typically "a gate round after freeze that returns new non-escalated, non-cosmetic findings", or "a second C0 failure".
Repairs against the two seats' lists are applied together, once per version. Items reserved to the principal (class
additions, renames, tier/warrant moves) are escalated at once and never block the cap. (R3C2 stopped itself at V20 by such
a cap; without it the gate would have produced V21–V25 of the same size.)

## Rule 4 — describe versus compute: every control executes and prints
A control is one exact command (placeholders resolved and printed), its complete stdout and stderr, its exit status, and the
exact token set it must print; PASS is defined from that printed run and nothing else. A pre-written block of pinned
versions, a paraphrase of what a script checks, or a token asserted from prose is a defect (the gate is instructed to flag
it). Controls have a positive form (must PASS) and a negative form (a planted fault must produce the exact expected failure
set). Deletion probes delete the load-bearing relation, not a bystander. The control scripts are committed and pinned by
sha256 beside the prereg at freeze; a draft names them and their commands now. (R3A's harness pin was theatre until the gate
said so; R3C2's C3 and C6 passed by assertion until V18.)

## Rule 5 — abort guards, and every dependency inside the delivered read set
(a) Lane process: an apply chain (patch → build → commit → dispatch) fails-stop after every step; patch scripts write at the
end (all-or-nothing); build, commit and dispatch sit behind the guards; controls are run against named positive/negative
pairs. (R3C2 V18: a half-applied master was dispatched once.)
(b) Delivered read set: the prereg enumerates every file a seat may open — packet, brief, tools, wrapper, pin file, manifest,
pinned sources — and pins each by sha256; no operative command names a tool outside that set or at an absolute path; the
third-seat dispatcher and other lane infrastructure are stated as administrative actions not claimed executable from the
packet. (R3C2 V20 gate: an operative step named a script the seats could not reach.)

## Applies to
R3E, R3F, R3G, R3H, R3I (DRAFT 2 each cites this file) and every later prereg in this lane. R3D and R3C2 are not re-versioned
for it; their records already carry the lessons in the long form.

R3_PREREG_DESIGN_RULES_COMPLETE
