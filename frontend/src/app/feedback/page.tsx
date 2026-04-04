"use client";

import { useEffect, useState } from "react";

interface FeedbackItem {
  id: number;
  name: string | null;
  message: string;
  is_ai: boolean;
  country: string | null;
  country_code: string | null;
  created_at: string;
}

export default function FeedbackPage() {
  const [name, setName] = useState("");
  const [message, setMessage] = useState("");
  const [submitting, setSubmitting] = useState(false);
  const [submitted, setSubmitted] = useState(false);
  const [error, setError] = useState("");
  const [feedbackList, setFeedbackList] = useState<FeedbackItem[]>([]);
  const [loading, setLoading] = useState(true);

  const fetchFeedback = async () => {
    try {
      const res = await fetch("/api/feedback");
      if (res.ok) setFeedbackList(await res.json());
    } catch {} finally { setLoading(false); }
  };

  useEffect(() => { fetchFeedback(); }, []);

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();
    if (!message.trim()) return;
    setSubmitting(true); setError("");
    try {
      const res = await fetch("/api/feedback", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({
          name: name.trim() || null,
          message: message.trim(),
          source: "web",
        }),
      });
      if (!res.ok) throw new Error("Failed");
      setSubmitted(true); setName(""); setMessage("");
      await fetchFeedback();
    } catch { setError("Submission failed. Please try again.");
    } finally { setSubmitting(false); }
  };

  const flagEmoji = (code: string | null) => {
    if (!code || code === "LO") return "";
    return code.toUpperCase().replace(/./g, (c) =>
      String.fromCodePoint(127397 + c.charCodeAt(0))
    );
  };

  return (
    <main className="max-w-2xl mx-auto px-4 py-10">
      <h1 className="text-3xl font-bold mb-2">Feedback</h1>
      <p className="text-gray-500 mb-8">Share your thoughts on NebulaMind. No login required.</p>

      <form onSubmit={handleSubmit} className="bg-gray-50 rounded-xl p-6 mb-10 space-y-4 border border-gray-200">
        <div>
          <label className="block text-sm font-medium text-gray-700 mb-1">Name <span className="text-gray-400">(optional)</span></label>
          <input type="text" value={name} onChange={(e) => setName(e.target.value)} placeholder="Anonymous"
            maxLength={100} className="w-full border border-gray-300 rounded-lg px-3 py-2 text-sm focus:outline-none focus:ring-2 focus:ring-indigo-500" />
        </div>
        <div>
          <label className="block text-sm font-medium text-gray-700 mb-1">Message <span className="text-red-400">*</span></label>
          <textarea value={message} onChange={(e) => setMessage(e.target.value)} rows={4} maxLength={2000} required
            placeholder="Tell us what you think..."
            className="w-full border border-gray-300 rounded-lg px-3 py-2 text-sm focus:outline-none focus:ring-2 focus:ring-indigo-500 resize-none" />
          <p className="text-xs text-gray-400 mt-1 text-right">{message.length}/2000</p>
        </div>

        {error && <p className="text-red-500 text-sm">{error}</p>}
        {submitted && <p className="text-green-600 text-sm font-medium">✅ Thank you for your feedback!</p>}

        <button type="submit" disabled={submitting || !message.trim()}
          className="bg-indigo-600 text-white px-5 py-2 rounded-lg text-sm font-medium hover:bg-indigo-700 disabled:opacity-50 disabled:cursor-not-allowed transition">
          {submitting ? "Submitting..." : "Submit Feedback"}
        </button>
      </form>

      <h2 className="text-xl font-semibold mb-4">Feedback ({feedbackList.length})</h2>
      {loading ? (
        <p className="text-gray-400">Loading...</p>
      ) : feedbackList.length === 0 ? (
        <p className="text-gray-400">No feedback yet. Be the first!</p>
      ) : (
        <ul className="space-y-4">
          {feedbackList.map((fb) => (
            <li key={fb.id}
              className={`border rounded-xl p-4 ${fb.is_ai ? "bg-purple-50 border-purple-200" : "bg-blue-50 border-blue-200"}`}>
              <div className="flex items-center justify-between mb-2">
                <div className="flex items-center gap-2 flex-wrap">
                  <span className={`text-xs font-semibold px-2 py-0.5 rounded-full ${fb.is_ai ? "bg-purple-200 text-purple-800" : "bg-blue-200 text-blue-800"}`}>
                    {fb.is_ai ? "🤖 AI" : "👤 Human"}
                  </span>
                  <span className="font-medium text-sm">{fb.name || "Anonymous"}</span>
                  {fb.country && fb.country !== "Local" && (
                    <span className="text-xs text-gray-500">{flagEmoji(fb.country_code)} {fb.country}</span>
                  )}
                </div>
                <span className="text-xs text-gray-400">{new Date(fb.created_at).toLocaleDateString("en-US")}</span>
              </div>
              <p className="text-sm text-gray-700 whitespace-pre-wrap">{fb.message}</p>
            </li>
          ))}
        </ul>
      )}
    </main>
  );
}
