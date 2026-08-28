with open('../PREREG_SUCCESSOR_DRAFT_V27_20260827.md', 'r') as f:
    text = f.read()

text = text.replace(
    '# PREREGISTRATION DRAFT V26',
    '# PREREGISTRATION DRAFT V27'
)
text = text.replace(
    '> **V26 is a repair of V25.** It repairs `PREREG_SUCCESSOR_DRAFT_V25_20260827.md`, sha256\n> `50f2e53256cc79707f2a4dfbf737740e6101742deb39365498737c904aa0f59b`',
    '> **V27 is a repair of V26.** It repairs `PREREG_SUCCESSOR_DRAFT_V26_20260827.md`, sha256\n> `2eec8da41ee69374fcc9c3fca2de150b29c04ca7b921848e908fa97a20bffd52`'
)

with open('../PREREG_SUCCESSOR_DRAFT_V27_20260827.md', 'w') as f:
    f.write(text)
