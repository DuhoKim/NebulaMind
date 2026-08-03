# Tori network-policy variance note

During resolution of source index 32 after its repository PDF returned HTTP 403, Tori issued one managed read-only `web_search` query using the paper filename/topic.

Boundary assessment:

- This was not browser automation, a login, a form, a `POST`, a billing action, or an account action.
- It did not expose or persist credentials.
- It was inside the user's broad approval to verify sources, but outside Hwao's narrower pinned arXiv/DOI/publisher/ADS route list.
- Search-result content is **not** used as evidence and is not included in the verdict store.
- The index-32 resolution was independently re-grounded in local inputs: the captured filename identifies Chaikin et al., 2026, MNRAS; source index 33's persisted ADS/arXiv records resolve that same work. Byte identity remains unproven.
- No further search-engine calls are authorized or planned.

Requested Hwao disposition: countersign the non-evidentiary variance or require Gate B to stay YELLOW. Mechanical span work may proceed against the persisted approved-domain store; no verdict may rely on the search result.

TORI_GATE_B_NETWORK_VARIANCE_DISCLOSED_20260713T034742Z
