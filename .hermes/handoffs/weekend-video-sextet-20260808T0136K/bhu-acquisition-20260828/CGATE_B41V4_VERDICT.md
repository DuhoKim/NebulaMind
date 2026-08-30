B41V4_REFUTED_B37_REFRESHER_BINDINGS

# B41V4 adversarial verdict

V4 correctly repairs B29, B43, and the presentation of the substantive metrics, but it does not implement the promised repair for B37's four refreshed entries. Its receipt engine reports `14/14` because it checks that two files exist and that all nine entry numbers occur somewhere in the later B37 verdict; it does not bind the prior full-source receipts for entries 23 and 54 at all, and it does not inspect receipt content in the files supplied for entries 26 and 44. The underlying record can still support the already-confirmed 39/39 result, but this script again does not prove the receipt provenance claimed by its green check.

I read the complete V4 docstring and all predicates, ran the committed file unchanged (`14/14`, exit 0), confirmed commit `b9ee9d3b8`, and inspected every artifact implicated by the four demanded repairs.

## 1. Repairs that are now sound

### B29 sample

The eleven-paper sample is now genuinely bound. V4:

- recomputes the committed sample;
- requires CGATE_B29's scoped declaration, “I re-read all eleven sampled papers from their pinned full texts”;
- checks CGATE_B29's first-line token; and
- requires a verdict-table row for every sampled entry.

This discharges the V3 free-rider defect. Table-row presence does not prove reading as an external event, but together with the scoped signed declaration it honestly binds the record.

### B43 entry 38

The B43 row is repaired. It checks the script's source identity/length statement, CGATE_B43's “in full and sequentially” declaration and exact token, and AGATE_B43's “full sequential read” declaration and exact token. It no longer substitutes B43's self-describing Python file for the landed gate verdicts.

### Flag 25 and metric presentation

The entry-25 predicate now reaches the actual CGATE_B25 ruling sentences and both gate tokens rather than tokens alone. The two claim-level lists are printed as distinct observations and neither is promoted to a sensitivity denominator. The record-level/script-level distinction is also explicit.

## 2. B37's four refreshed entries remain unbound

CGATE_B37 distinguishes five fresh full reads from four refreshers. Its refresher declaration says:

- entry 23: decisive current sections, “supplemented by the earlier series audits”;
- entry 26: decisive current sections plus full-source A5;
- entry 44: full-source B17;
- entry 54: decisive current sections plus “the full-source B15 curvature adjudication.”

V4's B37 requirements are instead:

```python
("CGATE_A5_VERDICT.md", ""),
("CGATE_B17_VERDICT.md", "")
```

Empty fragments are excluded from the substring test by `if frag`; those requirements therefore establish only `os.path.exists(...)`. Any contents—including an unrelated or empty file—would pass.

More decisively:

- no earlier receipt artifact of any kind is required for **entry 23**;
- no B15 artifact is required for **entry 54**;
- only `CGATE_A5_VERDICT.md`'s existence is checked for **entry 26**;
- only `CGATE_B17_VERDICT.md`'s existence is checked for **entry 44**.

There is no `CGATE_B15_VERDICT.md` in this directory; `AGATE_B15_VERDICT.md` exists, but V4 never opens it. A plausible earlier entry-23 artifact, `CGATE_A10_VERDICT.md`, also exists, but V4 never opens that either. Whether those are ultimately the correct receipts must be decided by their actual scope; mere availability is not a binding.

The per-entry identity loop does not cure this. It checks only that `entry 23`, `entry 26`, `entry 44`, and `entry 54` occur somewhere in `CGATE_B37_VERDICT.md`. They occur in the refresher list and later rulings. That establishes which papers B37 discusses, not that the earlier full-source artifacts exist or say they were read. Thus the engine joins:

1. all nine identities in the later verdict;
2. a generic five-paper full-read declaration in that verdict;
3. generic refresher prose; and
4. existence of two named files;

and calls the result a per-entry receipt for nine. The four refresher chains remain string-level assertions rather than artifact-bound receipts.

This is exactly the V3 defect the brief says V4 repaired. A correct implementation needs four explicit chains, each containing the entry identity, the B37 refresher sentence, the actual prior artifact, its gate token where applicable, and a scoped full-source/read declaration in that prior artifact. If no full-source artifact exists for entry 23 or 54, the script must not imply one.

## 3. Remaining label/predicate mismatch for flag 6

The flag-6 check is improved but still does not test all the facts named in its label. It requires:

- the batch-9 heading; and
- the entry-6 headline phrase `reclassed QUALITATIVE-DIRECTIONAL`.

Its label says the section “carries the read AND the reclassification headline.” The read declaration is supported by the reading-notes record, but the predicate does not search for it. This is a smaller defect because the same document's opening states that the pinned texts were read in full and entry 6's section says the paper was “read at last,” yet the requested per-fact repair should bind one of those phrases rather than merely claim it in the check name.

## 4. Other predicates and substantive numbers

The remaining limitations are disclosed rather than hidden:

- the not-located check binds the wrap-up's historical list, not present nonlocation;
- the flag recomputation is explicitly scoped to the mapped `bhu-reading/*_clean.txt` pool and uses equality;
- entry 5's separate scan correctly reproduces `(0,0,0)` and fairly establishes both operational failure modes;
- current paper-tier ground truth is parsed from the adjudicated bibliography labels, not independently re-derived truth;
- phrase bindings certify a record, not a human reading act.

The arithmetic remains correct conditional on the adopted corpus and current labels:

- accumulated record-level coverage after B43: **39/39**;
- paper-tier miss rate: **1 of 2** (`22` hit, `5` missed);
- observed paper-tier precision over mapped corpus flags: **1 of 3**;
- claim-level sensitivity: **not measured**, with the two non-denominator observations separately labelled.

## Final ruling

The substantive census outcome is unchanged, but B41V4 is **not confirmable as the requested receipt-provenance closer**. Its load-bearing `RECEIPTS, per-entry` predicate is green while two B37 refresher artifacts are entirely absent and two more are checked only for file existence. Bind all four chains to actual scoped receipt text, and add the missing flag-6 read phrase predicate. The same numerical conclusion can then be confirmed without qualification.
