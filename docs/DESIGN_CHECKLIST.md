# Design Checklist

Use this before implementing architecture/design docs that affect user-visible output or durable product behavior.

## Display And Rendering

- Checked durable display directives? (`frontend/CITATION_POLICY.md`, `MEMORY.md`)
- Confirmed the design does not reintroduce bottom References/Bibliography sections for wiki pages.
- Confirmed citation markers render as inline evidence badges only, with no numbered `[n]` superscripts.

## Implementation Notes

- When a historical design doc conflicts with a durable directive, annotate the design doc and follow the durable directive.
- Keep backend canonical data contracts separate from frontend display policy unless the durable directive explicitly changes storage.
