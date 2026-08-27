import re
with open("SECTION6_DRAFT_AGY_R13.md", "r") as f:
    content = f.read()

old_p2_4 = r"Second, calibration accuracy: failure of the per-bin accuracy lower bound \(`a_LB_b < 0\.85`\) emits `INCONCLUSIVE-BY-CALIBRATION`\."
new_p2_4 = "Second, Row P binds the already-verified pre-unblinding calibration PASS (`a_LB_b >= 0.85`), relying on the locked BS-5f and BS-L verification rather than re-evaluating the threshold."

content = re.sub(old_p2_4, new_p2_4, content)

with open("SECTION6_DRAFT_AGY_R13.md", "w") as f:
    f.write(content)
