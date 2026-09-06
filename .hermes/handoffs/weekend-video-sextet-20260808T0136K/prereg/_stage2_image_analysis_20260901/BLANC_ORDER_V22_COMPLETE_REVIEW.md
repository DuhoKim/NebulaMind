# BLANC ORDER — dispatch the complete-package review; and fix what the design assumes about ME and about Duho (2026-09-06 21:14 KST)

DISPATCH the independent review of the complete unadopted package. It is
within authorized preparation. Candidate a7417eb71d5b5fbdedcc…, with BOTH
track records, the complete attack table, and the staged helpers.

FIRST, correct two things the design currently assumes. These are not
wording nits: they claim authority nobody granted.

  1. The design names an origin actor for me ({actor: blanc-ops, session:
     OPS} or similar). DUHO HAS NEVER NAMED THAT ORIGIN. Do not write
     "origin named by Duho" or anything implying he chose it. Write what
     is true: the origin is a lane proposal, UNADOPTED, and he has not
     been asked.
  2. The design assumes Duho personally confirms every receipt digest. HE
     HAS NOT AGREED TO THAT. It is a substantial standing commitment —
     recurring work, indefinitely — and proposing it is fine; presuming it
     is not. State it as a request he must accept or refuse, with what
     happens under each.

I am flagging these hardest because they concern me. A design that quietly
installs its own coordinator as a trusted party, under a name the principal
never assigned, is the kind of thing that reads as reasonable from inside
and indefensible from outside. Put both to him as questions.

FOR THE REVIEW, require:
  - the three states distinguished: the current offline candidate (still
    accepts two attacks), the standalone staged helpers, and the composed
    recommended mode — exercised on the production call path, not in
    isolation;
  - the exact remaining trusted step assessed, including that a forged
    first receipt IN MY NAME is not caught by the code. Say what an
    independent expected-receipt identity would have to be to close it;
  - the eight initial AttributeErrors reported as MISSING-INTERFACE tests,
    with run 1b and the reproduction establishing the old behaviour —
    do not present an AttributeError as if it were a behavioural failure;
  - the cost stated correctly: one push per attempt or history entry, with
    the failure states spelled out;
  - preserved and re-verified: sample sizes, exclusions, custody,
    blindness, an actual future drand round, the ONE holdout.

Nothing adopted. Bring me the verdicts and I take the package to Duho.
