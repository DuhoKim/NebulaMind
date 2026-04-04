"use client";

import { useEffect, useState } from "react";
import { useParams } from "next/navigation";
import ReactMarkdown from "react-markdown";
import Link from "next/link";

interface WikiPage {
  id: number;
  title: string;
  slug: string;
  content: string;
}

interface EditProposal {
  id: number;
  content: string;
  summary: string;
  status: string;
}

function extractHeadings(content: string) {
  const headings: { level: number; text: string; id: string }[] = [];
  const lines = content.split("\n");
  for (const line of lines) {
    const match = line.match(/^(#{1,3})\s+(.+)/);
    if (match) {
      const text = match[2].replace(/\*\*/g, "");
      headings.push({
        level: match[1].length,
        text,
        id: text.toLowerCase().replace(/[^a-z0-9]+/g, "-"),
      });
    }
  }
  return headings;
}

function extractKeyFacts(content: string): string[] {
  const facts: string[] = [];
  const lines = content.split("\n");
  for (const line of lines) {
    if (line.match(/^\*\*.*\*\*/) || line.match(/^- \*\*/)) {
      facts.push(line.replace(/^\*\*|\*\*$/g, "").replace(/^- /, "").trim());
      if (facts.length >= 4) break;
    }
  }
  return facts;
}

export default function WikiPageView() {
  const params = useParams();
  const slug = params?.slug as string;
  const [page, setPage] = useState<WikiPage | null>(null);
  const [edits, setEdits] = useState<EditProposal[]>([]);
  const [loading, setLoading] = useState(true);
  const [viewMode, setViewMode] = useState<"A" | "B">("B");
  const [voted, setVoted] = useState(false);

  useEffect(() => {
    if (!slug) return;
    Promise.all([
      fetch(`/api/pages/${slug}`).then((r) => r.ok ? r.json() : null),
      fetch(`/api/edits?status=pending`).then((r) => r.ok ? r.json() : []).catch(() => []),
    ]).then(([p, e]) => {
      setPage(p);
      setEdits(p ? e.filter((ed: EditProposal) => true) : []);
      setLoading(false);
    });
  }, [slug]);

  const handleVote = async (version: "A" | "B") => {
    try {
      await fetch("/api/feedback", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({
          name: `Wiki Vote: ${version}`,
          message: `Preferred wiki view: Version ${version} for page "${page?.title}"`,
          is_ai: false,
        }),
      });
      setVoted(true);
    } catch {}
  };

  if (loading) return <p className="text-gray-400">Loading...</p>;
  if (!page) return <p className="text-gray-500">Page not found.</p>;

  const headings = extractHeadings(page.content);
  const keyFacts = extractKeyFacts(page.content);

  return (
    <article className="max-w-4xl mx-auto">
      {/* View mode toggle */}
      <div className="flex items-center gap-2 mb-6 text-sm">
        <span className="text-gray-500">View:</span>
        <button
          onClick={() => setViewMode("A")}
          className={`px-3 py-1 rounded-full transition ${viewMode === "A" ? "bg-indigo-600 text-white" : "bg-gray-100 text-gray-600 hover:bg-gray-200"}`}
        >
          A: Clean
        </button>
        <button
          onClick={() => setViewMode("B")}
          className={`px-3 py-1 rounded-full transition ${viewMode === "B" ? "bg-indigo-600 text-white" : "bg-gray-100 text-gray-600 hover:bg-gray-200"}`}
        >
          B: Rich
        </button>
        {!voted && (
          <span className="ml-4 flex items-center gap-2">
            <span className="text-gray-400">Which do you prefer?</span>
            <button onClick={() => handleVote("A")} className="text-xs px-2 py-1 bg-blue-100 text-blue-700 rounded hover:bg-blue-200">Vote A</button>
            <button onClick={() => handleVote("B")} className="text-xs px-2 py-1 bg-purple-100 text-purple-700 rounded hover:bg-purple-200">Vote B</button>
          </span>
        )}
        {voted && <span className="ml-4 text-green-600 text-xs">✅ Thanks for voting!</span>}
      </div>

      <header className="mb-8">
        <h1 className="text-3xl font-bold mb-2">{page.title}</h1>
        <p className="text-sm text-gray-400">slug: {page.slug}</p>
      </header>

      {viewMode === "B" && headings.length > 2 && (
        <nav className="mb-8 p-4 bg-gray-50 border border-gray-200 rounded-xl">
          <h3 className="text-sm font-semibold text-gray-500 mb-2">Contents</h3>
          <ul className="space-y-1">
            {headings.map((h, i) => (
              <li key={i} style={{ paddingLeft: `${(h.level - 1) * 12}px` }}>
                <a href={`#${h.id}`} className="text-sm text-indigo-600 hover:text-indigo-800 no-underline">
                  {h.text}
                </a>
              </li>
            ))}
          </ul>
        </nav>
      )}

      {viewMode === "B" && keyFacts.length > 0 && (
        <div className="mb-8 p-4 bg-indigo-50 border border-indigo-200 rounded-xl">
          <h3 className="text-sm font-semibold text-indigo-700 mb-2">🔑 Key Facts</h3>
          <ul className="space-y-1">
            {keyFacts.map((fact, i) => (
              <li key={i} className="text-sm text-indigo-900">{fact}</li>
            ))}
          </ul>
        </div>
      )}

      <div className="prose prose-gray max-w-none leading-relaxed">
        <ReactMarkdown
          components={{
            h1: ({ children }) => {
              const text = String(children);
              const id = text.toLowerCase().replace(/[^a-z0-9]+/g, "-");
              return <h1 id={id} className="text-2xl font-bold mt-8 mb-4">{children}</h1>;
            },
            h2: ({ children }) => {
              const text = String(children);
              const id = text.toLowerCase().replace(/[^a-z0-9]+/g, "-");
              return <h2 id={id} className="text-xl font-semibold mt-6 mb-3 border-b pb-2">{children}</h2>;
            },
            h3: ({ children }) => {
              const text = String(children);
              const id = text.toLowerCase().replace(/[^a-z0-9]+/g, "-");
              return <h3 id={id} className="text-lg font-medium mt-4 mb-2">{children}</h3>;
            },
            p: ({ children }) => <p className="mb-4 leading-relaxed">{children}</p>,
            ul: ({ children }) => <ul className="list-disc pl-6 mb-4 space-y-1">{children}</ul>,
            ol: ({ children }) => <ol className="list-decimal pl-6 mb-4 space-y-1">{children}</ol>,
            strong: ({ children }) => <strong className="font-semibold text-gray-900">{children}</strong>,
            blockquote: ({ children }) => (
              <blockquote className="border-l-4 border-indigo-300 pl-4 italic text-gray-600 my-4">{children}</blockquote>
            ),
            code: ({ children }) => (
              <code className="bg-gray-100 px-1.5 py-0.5 rounded text-sm font-mono">{children}</code>
            ),
          }}
        >
          {page.content}
        </ReactMarkdown>
      </div>

      {edits.length > 0 && (
        <section className="mt-12 border-t pt-8">
          <h2 className="text-xl font-semibold mb-4">Pending Edits ({edits.length})</h2>
          <div className="space-y-3">
            {edits.map((edit) => (
              <div key={edit.id} className="p-4 bg-amber-50 border border-amber-200 rounded-lg">
                <div className="flex items-center gap-2 mb-2">
                  <span className="text-xs font-medium bg-amber-100 text-amber-700 px-2 py-0.5 rounded">Pending</span>
                  <span className="text-sm text-gray-500">#{edit.id}</span>
                </div>
                <p className="text-sm text-gray-700">{edit.content.slice(0, 200)}{edit.content.length > 200 ? "..." : ""}</p>
              </div>
            ))}
          </div>
        </section>
      )}

      <div className="mt-8 text-center">
        <Link href="/explore/graph" className="text-indigo-600 text-sm hover:text-indigo-800">
          🕸️ See how this connects to other topics →
        </Link>
      </div>
    </article>
  );
}
