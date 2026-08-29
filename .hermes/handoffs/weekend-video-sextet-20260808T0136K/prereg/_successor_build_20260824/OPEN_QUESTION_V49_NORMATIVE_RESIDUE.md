**STATUS: CLOSED — all three items ruled.** Row L (qualify, V52), unreachable guards (third status, V52), and the access-log refusal vocabulary (**option A, eight codes, no catch-all — ruled 19:52, applied V56**).

# OPEN QUESTION — three V49 findings I did not repair, and one of them is 25 drafts old

**Raised 2026-08-29 15:5x KST by Hwao. V50 repaired the six findings that were corrections to my own
text. These three are not mine: each changes a normative rule.**

## 1. Row L's signing path still voids itself — and CODEX has now found this twice (CODEX-V49 F1, HIGH)

**This is a recurrence of `CODEX-V24 F1`, raised at V24 and still present at V49.**

Row L requires three signed objects: the freeze signature, the BS-L detached signature over the
canonical lock-body digest, and the canonical opening authorization. **Row L's void condition is
unqualified — "signing anything but the canonical lock digest" — so performing the two signatures the
same row requires voids the run.** `VOID-6.1L-WRONG-SIGNATURE` is registered at phase P7 while the
BS-L signature occurs at P6 and the freeze signature at P0, so the phases do not rescue it either.

**The document is honest about it:** the preamble lists *"§6.1 Row L's signing path voids itself
(CODEX-V24-1)"* among carried-open items. **But carried-open is not the same as freezable**, and a
seat raising the same HIGH finding 25 drafts apart is the signal worth acting on. Repairing it means
qualifying a VOID condition — normative, and squarely a hard stop.

## 2. The access log's refusal reasons defeat the closed non-χ allowlist (GPT56-V49 F1, HIGH)

§6.1 declares the non-χ-bearing receipt and log classes a **closed list defined by schema**, and
includes the BS-2k access log on the strength of its event schema — *"identities and flags, never
payload bytes."* But the schema's **refusal-reason field is unconstrained**, and a refusal reason is
written per object. A sufficiently descriptive refusal reason can carry per-object information about a
χ-bearing object while sitting inside a class the document asserts is not χ-bearing.

Repair means constraining the refusal vocabulary to a closed set — which changes what the log may
record, and therefore what the study promises about custody. **Not mine.**

## 3. The caller/run boundary misclassifies unreachable defensive guards (GPT56-V49 F5)

V49's boundary is binary: a raise is a caller error if it tests an argument as supplied, otherwise it
is a run outcome needing a named terminus. **A guard that cannot fire at all is neither**, and the
test as written files it under "caller error" by default. `allocate_handcheck` is the live example —
five of its eight feasibility guards were not reached in 60,000 executions, and the function decides
feasibility before allocating, which is exactly the design that makes later guards unreachable.

I have already revised this rule twice in two drafts (residual-ordering at V44, VOID precedence at
V50). **A third revision by me, on a rule about how to classify things, is how the rule stops meaning
anything.** The choice — treat an unreachable guard as a caller error, as dead code to be removed, or
as a third recorded status — is a decision about the classification scheme, not an application of it.

## Being repaired separately, because they are factual rather than normative

- **GPT56-V49 F6** — §2.1's *"nothing else changes with the branch"* contradicts Branch A voiding
  every Branch-B pin. The V11 commit says Branch A *"is a new preregistration in everything but
  name"*, so the record settles which side is wrong; this is recoverable, like the §2.7 phase was.
- **GPT56-V49 F7** — a cited predecessor memo no longer matches its pinned SHA, and only an uncited
  historical git object does. A citation-accuracy repair once I establish the correct reference.

## Status

- **V50** (`e3d0d65cca545040`) carries the six repairs and is **not dispatched** — dispatching now
  would re-find all three above. Checkers: 16/8 prose-matched, trace 49 transitions 0 problems,
  `void_registry` 6/0, lint exits 0.
- **BS-6 and the first image byte remain blocked.**
