# GORU: Legacy Surveys Data Contact Route

**Status:** Published Contact Fact-Find (No emails sent, no tickets created)

## 1. The Published Contact Route (Best First)
The Legacy Survey officially designates two main channels for general questions under their explicit **"First Points of Contact"** section at [legacysurvey.org/contact](https://www.legacysurvey.org/contact/):

1. **Discussion Forum (Google Group):** [https://groups.google.com/forum/#!forum/decam-legacy-survey](https://groups.google.com/forum/#!forum/decam-legacy-survey)
   - *Why it's ranked first:* It is literally the first bullet point on the contact page. Like many astronomical surveys, they prefer public forum posts so that the broader community benefits from the answer.
2. **Help Desk (Direct Email):** `help@legacysurvey.org`
   - *Why it's ranked second:* It is the second bullet point under "First Points of Contact". It serves as the official email for those who do not want to use the public forum.

## 2. Named Individuals
The contact page lists several dozen named individuals under "PIs and Leads" and "Other Experts", but sending a cold email to them for a general data question violates the "First Points of Contact" triage structure. 

If your question is extremely specifically about the NOIRLab Astro Data Lab infrastructure (e.g. querying their database tables) rather than NERSC data files, the named expert is:
- **Stephanie Juneau**, "Astro Data Lab Contact" (address on the survey contact page; redacted here — see note at end). 
However, for Astro Data Lab infrastructure, NOIRLab prefers you use their general help desk: `datalab@noirlab.edu`.

## 3. Bulk Data Access Permission
There is **no separate permission form, acceptable-use application, or bulk access request queue.** 
- The data is fully public domain ("publicly available and does not require special permission to access for research purposes").
- The published protocol for bulk access is simply "use Globus" or download the raw FITS brick files, rather than requesting permission to spam the cutout service. If your question is "may I scrape 832,000 cutouts via the web service?", the documented answer is effectively "no, download the bricks," and asking via email is unlikely to yield an exception.

## 4. Response Expectations
There are no published turnaround SLAs (Service Level Agreements) for `help@legacysurvey.org` or the Google Group. The forum is actively monitored by the community and the core developers (like Dustin Lang), but response times vary based on availability.

## Recommendation
If you still intend to send the query:
- Do not email the PIs or named experts directly.
- **Option A:** Post to the `decam-legacy-survey` Google Group (most likely to get a thorough, documented answer from a developer like Dustin Lang).
- **Option B:** Send the draft to `help@legacysurvey.org` if you need to keep the inquiry private.


---

**Redaction note (Hwao, 2026-08-15, not Goru's edit).** One named individual's work email address was removed from §2 before this file was committed. This repository is public, and republishing a person's address into an indexed, scrapeable location is a different act from it appearing on the survey's own contact page. The name and role are retained — they are public, professional, and load-bearing for the finding. Role addresses (`help@legacysurvey.org`, `datalab@noirlab.edu`) are kept: they are published precisely to be used. Goru's conclusion is unchanged, and it was to use the forum or the help desk rather than any individual.
