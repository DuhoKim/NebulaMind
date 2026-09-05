import numpy as np
from test_fryer2 import m_remnant_delay, m_remnant_rapid

for m in [19.0, 19.5, 20.0, 21.0, 22.0]:
    print(f"M={m}  Delay Z=0.01: {m_remnant_delay(m, 0.01):.3f}  Rapid Z=0.01: {m_remnant_rapid(m, 0.01):.3f}")

