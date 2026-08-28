with open('../PREREG_SUCCESSOR_DRAFT_V27_20260827.md', 'r') as f:
    text = f.read()

import re
text = re.sub(
    r'authenticated catalogue-quality evidence fields (.*?) and computes',
    r'authenticated catalogue-quality evidence fields (exact authenticated fields `flux_ivar_r`, `psfsize_r`, `nobs_r` from source digest `61214b59d7b35a1e5004a39c6381d08b354ec1f7be6af6b60b23474d02ec28a3`, joined one-to-one on keys `brickid`, `objid`, verified by the BS-2a pinned verifier, failing nonfatally as an ordinary exclusion) \1 and computes',
    text
)

with open('../PREREG_SUCCESSOR_DRAFT_V27_20260827.md', 'w') as f:
    f.write(text)
