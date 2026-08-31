### Extraction Rule

To derive the closed operation token set for the access-log event schema's `(row, operation)` class key, I evaluated Rows A through L to isolate actions that traverse Row B (the store mediator) to interact with one of the three sealed stores (Main Sealed Store, Committee Sealed Store, Predecessor Archive). 

1. **Filter by Mediator Traverse**: Pure workflow or compute verbs that never touch a mediated store (e.g., generating keys, cryptographic signing, in-memory computations, Stage C synthetic injections, reading unsealed release images, or passing data directly between rows via interface without a store commit) do not route through Row B and therefore generate no access-log event. These are excluded.
2. **Qualify by Store**: Because a single row can legitimately access multiple distinct stores (e.g., Row I reads from both the Committee Store and the Main Store), an unqualified `READ` operation would collapse failures from entirely different domains into the same `(I, READ)` class key. To keep the `(row, operation)` key unambiguous and prevent unrelated defects from merging into one recurrence count, every read and write primitive must be explicitly qualified by its target store.
3. **Conveyance as a Primitive**: Row G's access involves cutouts being "rendered through the sealed interface" for a human committee member. Because this conveys bytes to a human display surface rather than programmatically returning a byte buffer to a machine, it constitutes its own distinct primitive (`VIEW-MAIN-STORE`).
4. **Metadata Separation**: Row A inspects the predecessor archive "by non-content metadata operation" to verify its seal state, requiring a distinct primitive to differentiate metadata access from content access.

### Closed Operation Token Set

```text
READ-MAIN-STORE
WRITE-MAIN-STORE
READ-COMMITTEE-STORE
WRITE-COMMITTEE-STORE
READ-METADATA-ARCHIVE-STORE
VIEW-MAIN-STORE
```

SEAT: AGY
VERSION: OPSET-V1
VERDICT: DERIVED
COUNT: 6
