// Emit inline CSS verbatim. React renders a string child of <style> through its
// text-escaper, turning CSS `"`, `>` and `&` into `&quot;`/`&gt;`/`&amp;` in the
// SSR HTML — but the browser treats <style> as raw text and never decodes those,
// so the hydrated client (which holds the literal CSS) mismatches the server text
// (React #425 → #418/#423, whole root re-renders client-side → slow, deep-links
// drop). dangerouslySetInnerHTML writes the CSS raw, so server and client agree.
// Safe here: every caller passes a hardcoded CSS constant, never user input.
export function RawStyle({ css }: { css: string }) {
  return <style dangerouslySetInnerHTML={{ __html: css }} />;
}
