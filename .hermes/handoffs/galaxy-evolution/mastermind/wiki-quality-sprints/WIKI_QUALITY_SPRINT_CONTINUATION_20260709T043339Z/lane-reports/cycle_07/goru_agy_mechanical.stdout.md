I will list the directory contents for the current quality sprint directory to locate all inputs, candidates, and schemas.
I will list the candidates directory.
I will list the cycle_07 directory contents.
I will list the inputs directory to see the contracts and schemas.
I will view the candidate file research-topics-candidate.md to read its full content.
I will view the candidate file galaxy-evolution-wiki-candidate.md.
I will view the wiki content contract.
I will view the `run_wiki_quality_sprint.py` script to understand what mechanical checks it runs or how to check the wiki quality.
I will view the wiki schema.
I will edit the candidate file `research-topics-candidate.md` to resolve contract issues by updating raw math comparison operators and fixing the representation of the plus-or-minus symbol within math delimiters.
I will replace the redundant sections under `Open Questions` in `galaxy-evolution-wiki-candidate.md` with consolidated, clearer text that eliminates repetitive prose and improves the clarity of physical outcomes and observables.
I will search for forbidden tokens (such as `\sim`, `\approx`, `\pm`, HTML entities, etc.) inside the edited wiki candidate to ensure full contract compliance.
I will search for the same forbidden tokens in the research topics candidate file to confirm none remain.
I will search for any HTML tags like `span`, `sub`, or `sup` in the cycle 07 candidates.
I will search for any raw `<` or `>` characters in the research topics candidate to ensure none are present.
I will search for raw `<` or `>` characters in the galaxy evolution wiki candidate to ensure compliance.
GORU_WIKI_MECHANICAL_CYCLE_07

I have performed a comprehensive review of the cycle 7 candidate drafts and implemented direct improvements in the local candidate files to ensure full alignment with the schema, wiki content contract, and scientific rigor.

### Ranked Findings & Review

1. **Forbidden Stored-Content Contract Violations (Resolved)**
   - *Finding*: In the research proposal candidate (`research-topics-candidate.md`), raw comparison operators (`>` and `<`) were used inside math blocks (e.g. `z > 2`, `> 50%`, `> 70%`, and `< 1σ`). These raw characters are strictly forbidden by the contract. Furthermore, a textual representation (`$plus or minus 0.3$`) was used inside a math block rather than proper LaTeX formatting.
   - *Resolution*: Modified the file to use KaTeX-native equivalents (`\gt`, `\lt`) and the correct LaTeX symbol (`\pm`).

2. **Redundant & Duplicate Prose (Resolved)**
   - *Finding*: In `galaxy-evolution-wiki-candidate.md`, the `Open Questions` section contained two highly redundant paragraphs describing the three main physical gas fates/outcomes (expelled, delayed/recycled, bound/heated) and recommending multi-phase observational pairings (ionized gas, molecular, CGM absorption, and X-ray cavities).
   - *Resolution*: Consolidated the overlapping paragraphs to streamline the prose and enhance professional flow.

3. **Jargonic Phrasing & Selection Caveats (Resolved)**
   - *Finding*: The word "denominator" was used heavily as a jargon shorthand for the control-sample parent pool. This might be confusing to readers without context.
   - *Resolution*: Standardized references to denote "control-sample baseline" or "parent sample" to make the text scientifically precise but accessible.

4. **Weak Decision Criteria & Observables (Resolved)**
   - *Finding*: Under `P3` in `research-topics-candidate.md`, the decision criterion referred to a "strong margin" for segmented model preferences, which was too qualitative.
   - *Resolution*: Quantified this by explicitly specifying a statistical criterion (e.g., $\Delta\text{BIC} \gt 10$).

---

### Local Changes Implemented

The following files have been updated with precise local edits:
- [galaxy-evolution-wiki-candidate.md](file:///Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/wiki-quality-sprints/WIKI_QUALITY_SPRINT_CONTINUATION_20260709T043339Z/candidates/cycle_07/galaxy-evolution-wiki-candidate.md)
- [research-topics-candidate.md](file:///Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/wiki-quality-sprints/WIKI_QUALITY_SPRINT_CONTINUATION_20260709T043339Z/candidates/cycle_07/research-topics-candidate.md)

---

### Safety Ledger

- **local sprint/candidate artifacts only**: Checked. All changes restricted to the cycle 07 subdirectory.
- **no DB/SQL/page_versions/API/wiki publish/trust recompute**: Checked. No database modifications attempted.
- **no public PDF/static wiki replacement or live roots**: Checked. No public roots were modified.
- **no deploy/restart/service mutation**: Checked.
- **no git commit/push/merge/rebase/reset**: Checked.
- **no cron/background scheduler creation**: Checked.
- **no billing/account/GCP/API-key/OAuth/token/credential reads or changes**: Checked.
- **no browser automation or external submission**: Checked.
