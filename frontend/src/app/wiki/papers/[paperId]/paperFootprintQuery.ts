import type { PaperProfilePayload } from "./paperProfile";

function cleanText(value?: string | number | null): string {
  return String(value ?? "").replace(/\s+/g, " ").trim();
}

function positiveInteger(value: unknown): number | null {
  const n = Number(value ?? 0);
  return Number.isInteger(n) && n > 0 ? n : null;
}

function stripPrefix(value: string, prefix: string): string {
  return value.toLowerCase().startsWith(`${prefix}:`) ? value.slice(prefix.length + 1) : "";
}

function encodedParam(name: "arxiv_id" | "evidence_id", value: string | number): string {
  return `${name}=${encodeURIComponent(String(value))}`;
}

export function buildPaperFootprintQuery(paperId: string, profile: PaperProfilePayload | null | undefined): string | null {
  const payloadArxivId = cleanText(profile?.paper?.arxiv_id).replace(/^arxiv:/i, "");
  if (payloadArxivId) return encodedParam("arxiv_id", payloadArxivId);

  const requested = cleanText(paperId);
  const requestedArxivId = stripPrefix(requested, "arxiv");
  if (requestedArxivId) return encodedParam("arxiv_id", requestedArxivId);

  const payloadEvidenceId = positiveInteger(profile?.paper?.evidence_id);
  if (payloadEvidenceId) return encodedParam("evidence_id", payloadEvidenceId);

  const requestedEvidenceId = positiveInteger(stripPrefix(requested, "evidence"));
  if (requestedEvidenceId) return encodedParam("evidence_id", requestedEvidenceId);

  if (requested && !/^(doi|url|paper):/i.test(requested)) return encodedParam("arxiv_id", requested.replace(/^arxiv:/i, ""));

  return null;
}
