import bs2k_stage_v2 as stage
import hashlib
import re

real = stage.X2_COMMIT
temp = real.with_name(real.name + ".temp")
content = real.read_text().replace("COMMITTEE-READ\n", "COMMITTEE-READX\n")

# Recompute the canonical digest for the modified tokens
blocks = re.findall(r"```[^\n]*\n(.*?)```", content, flags=re.DOTALL)
tokens = tuple(line.strip() for line in blocks[0].splitlines() if line.strip())
canonical = stage.x2_encoding(tokens)
new_digest = hashlib.sha256(canonical).hexdigest()

# Replace the stated digest in the markdown
content = re.sub(r"([0-9a-f]{64})", new_digest, content)
temp.write_text(content)

orig_x2 = stage.X2_COMMIT
stage.X2_COMMIT = temp
try:
    stage.x2_material()
    print("R3 BYPASS SUCCESS: Accepted tampered token + digest!")
except stage.Refusal as e:
    print(f"R3 BYPASS FAILED: Refused with {e.code}")
finally:
    stage.X2_COMMIT = orig_x2
    temp.unlink()
