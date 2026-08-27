import re

with open("SECTION6_DRAFT_AGY_R13.md", "r") as f:
    content = f.read()

old_status = r"Status: DRAFT FOR REFEREE\. Written under `BRIEF_DRAFT_SECTION6_R12\.md`\. Normatively, the protocol-deviation VOID branch was reseated in Row J where it executes before BS-5f issuance, and the complete Stage-C FAIL partition \(including the self-verification fail-closed return at lines 1275-1276\) was correctly defined in Row J\. Row P inherits the verified PASS\. BS-2a findings remain UNRESOLVED\. The principal holds the design question regarding the fail-closed rule on removal\."
new_status = "Status: DRAFT FOR REFEREE. Written under `BRIEF_DRAFT_SECTION6_R13.md`. Normatively, the calibration accuracy check was reseated in Row J before Stage-C execution to emit a pre-unblinding halt on failure, with the PASS bound through BS-5f and BS-L into Row P. The complete Stage-C FAIL partition (including the self-verification fail-closed return and count-return partition at lines 1275–1277) is correctly defined in Row J, which also enforces the no-deviation rule as a new pre-run verification. BS-2a findings remain UNRESOLVED. The principal holds the design question regarding the fail-closed rule on removal."

content = re.sub(old_status, new_status, content)

with open("SECTION6_DRAFT_AGY_R13.md", "w") as f:
    f.write(content)
