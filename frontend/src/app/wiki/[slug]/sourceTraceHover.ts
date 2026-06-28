export interface SourceTraceCitationLike {
  evidence_id?: number | string | null;
  author_year_key?: string | null;
  title?: string | null;
  authors?: string[] | string | null;
  year?: number | string | null;
  doi?: string | null;
  arxiv_id?: string | null;
  url?: string | null;
  summary?: string | null;
  abstract?: string | null;
  journal_ref?: string | null;
}

export interface SourceTraceCrossLink {
  kind: "source-index" | "external-paper";
  label: string;
  href: string;
  external: boolean;
}

export interface SourceTraceHoverCardCopy {
  eyebrow: "Source trace";
  title: string;
  traceLabel: string;
  byline: string;
  locator: string;
  summary: string;
  crossLinks: SourceTraceCrossLink[];
}

function splitAuthors(authors?: string[] | string | null): string[] {
  if (!authors) return [];
  const raw = Array.isArray(authors) ? authors : [authors];
  if (raw.length === 1 && typeof raw[0] === "string") {
    const value = raw[0];
    if (value.includes(";")) return value.split(";").map((s) => s.trim()).filter(Boolean);
    if (value.includes(",")) return value.split(",").map((s) => s.trim()).filter(Boolean);
  }
  return raw.map((s) => String(s).trim()).filter(Boolean);
}

function formatAuthors(authors?: string[] | string | null): string {
  const list = splitAuthors(authors);
  if (list.length === 0) return "";
  if (list[0]?.toLowerCase().includes("collaboration")) return list[0];
  if (list.length <= 2) return list.join(", ");
  return `${list.slice(0, 2).join(", ")} et al.`;
}

function cleanText(value?: string | null): string {
  return String(value || "").replace(/\s+/g, " ").trim();
}

export function formatSourceTraceSummary(value?: string | null, maxLength = 220): string {
  const clean = cleanText(value);
  if (!clean) return "No abstract or summary has been published for this source yet.";
  const safeMax = Number.isFinite(maxLength) && maxLength > 8 ? Math.floor(maxLength) : 220;
  return clean.length > safeMax ? `${clean.slice(0, safeMax - 1)}…` : clean;
}

function formatTraceLabel(citation: SourceTraceCitationLike): string {
  const parts: string[] = [];
  const id = cleanText(citation.evidence_id == null ? "" : String(citation.evidence_id));
  if (id) parts.push(`Evidence #${id}`);
  const key = cleanText(citation.author_year_key);
  if (key) parts.push(key);
  return parts.length > 0 ? parts.join(" · ") : "Evidence trace";
}

function formatByline(citation: SourceTraceCitationLike): string {
  const parts = [formatAuthors(citation.authors)];
  const year = cleanText(citation.year == null ? "" : String(citation.year));
  if (year) parts.push(year);
  const journal = cleanText(citation.journal_ref);
  if (journal) parts.push(journal);
  const compact = parts.filter(Boolean).join(" · ");
  return compact || "Source metadata pending";
}

function formatLocator(citation: SourceTraceCitationLike): string {
  const parts: string[] = [];
  const arxiv = cleanText(citation.arxiv_id);
  if (arxiv) parts.push(`arXiv:${arxiv}`);
  const doi = cleanText(citation.doi);
  if (doi) parts.push(`DOI:${doi}`);
  if (parts.length > 0) return parts.join(" · ");
  const url = cleanText(citation.url);
  return url ? "External source link available" : "External source link unavailable";
}

function cleanPageSlug(pageSlug?: string | null): string {
  return cleanText(pageSlug).replace(/^\/+|\/+$/g, "");
}

export function buildSourceTraceCrossLinks(
  citation: SourceTraceCitationLike,
  pageSlug?: string | null,
): SourceTraceCrossLink[] {
  const links: SourceTraceCrossLink[] = [];
  const slug = cleanPageSlug(pageSlug);
  if (slug) {
    links.push({
      kind: "source-index",
      label: "Open source index",
      href: `/wiki/${encodeURIComponent(slug)}/sources`,
      external: false,
    });
  }
  const url = cleanText(citation.url);
  if (url) {
    links.push({
      kind: "external-paper",
      label: "Open paper",
      href: url,
      external: true,
    });
  }
  return links;
}

export function formatSourceTraceHoverCard(citation: SourceTraceCitationLike, pageSlug?: string | null): SourceTraceHoverCardCopy {
  return {
    eyebrow: "Source trace",
    title: cleanText(citation.title) || "Untitled source",
    traceLabel: formatTraceLabel(citation),
    byline: formatByline(citation),
    locator: formatLocator(citation),
    summary: formatSourceTraceSummary(citation.summary || citation.abstract),
    crossLinks: buildSourceTraceCrossLinks(citation, pageSlug),
  };
}
