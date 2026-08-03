# Goru G1 Survey-Tab Provenance Report

**Marker:** `GORU_G1_SURVEY_TAB_PROVENANCE_DONE_20260707T144039Z`

## Findings
1. **Occurrences in HTML/JSON:** 0 exact occurrences of the words "Survey", "Surveys", "survey", "surveys", "Atlas", or "atlas" were found in `/Users/duhokim/HermesOps/cockpit/ge-autopilot.html` and `/Users/duhokim/HermesOps/cockpit/ge-autopilot-status.json`.
2. **Dashboard Groups/Tabs:** According to the source file `/Users/duhokim/NebulaMind/NebulaMind/tools/render_ge_autopilot_dashboard_v2.py`, the explicitly defined dashboard groups are `["Directors", "Method 1", "Method 2", "Method 3", "Other"]`.
3. **Survey Tab Implementation:** The private GE autopilot dashboard currently has **no Survey tab implementation whatsoever**.
4. **Likely Cause:** Based exclusively on the source code structure, the GE dashboard is strictly scoped to `Directors` + `Method 1/2/3` + `Other`. There is no logic, group definition, or template rendering for a Surveys section.

## Safety Ledger
- Read-only mechanical check performed via grep and source inspection.
- No database mutations, network access, live publications, or credential reads.
- Written strictly to the requested artifact path.

TORI_GORU_DISPATCH_DONE_20260707T144055Z
