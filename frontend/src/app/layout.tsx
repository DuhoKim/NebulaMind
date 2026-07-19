import type { Metadata } from "next";
import { headers } from "next/headers";
import "./globals.css";
import NavBar from "./components/NavBar";
import VisitTracker from "./VisitTracker";
import Footer from "./components/Footer";

export const metadata: Metadata = {
  title: "NebulaMind — an AI scientist automating astronomical research",
  description:
    "NebulaMind is an AI scientist that automates astronomical research on public data — mapping open frontiers and writing peer-review-style papers, focused on galaxy evolution. Explore 34+ topics from black holes to dark energy.",
  metadataBase: new URL("https://nebulamind.net"),
  openGraph: {
    title: "NebulaMind — an AI scientist automating astronomical research",
    description:
      "NebulaMind is an AI scientist that automates astronomical research on public data — mapping open frontiers and writing peer-review-style papers, focused on galaxy evolution.",
    url: "https://nebulamind.net",
    siteName: "NebulaMind",
    type: "website",
    locale: "en_US",
    images: [
      {
        url: "https://nebulamind.net/og-image.png",
        width: 1200,
        height: 630,
        alt: "NebulaMind — Collaborative astronomy knowledge platform",
      },
    ],
  },
  twitter: {
    card: "summary_large_image",
    title: "NebulaMind — an AI scientist automating astronomical research",
    description:
      "NebulaMind is an AI scientist that automates astronomical research on public data — mapping open frontiers and writing peer-review-style papers, focused on galaxy evolution.",
    images: ["https://nebulamind.net/og-image.png"],
  },
  icons: {
    icon: [
      { url: "/logo.png", sizes: "512x512", type: "image/png" },
      { url: "/logo.svg", type: "image/svg+xml" },
    ],
    apple: "/logo.png",
  },
  robots: {
    index: true,
    follow: true,
    googleBot: {
      index: true,
      follow: true,
      "max-video-preview": -1,
      "max-image-preview": "large",
      "max-snippet": -1,
    },
  },
  alternates: {
    canonical: "https://nebulamind.net",
  },
};

const jsonLd = {
  "@context": "https://schema.org",
  "@type": "WebSite",
  name: "NebulaMind",
  alternateName: "AstroBotPedia",
  url: "https://nebulamind.net",
  description:
    "NebulaMind is an AI scientist that automates astronomical research on public data — mapping open frontiers and writing peer-review-style papers, focused on galaxy evolution.",
  potentialAction: {
    "@type": "SearchAction",
    target: "https://nebulamind.net/explore?q={search_term_string}",
    "query-input": "required name=search_term_string",
  },
};

export default async function RootLayout({
  children,
}: {
  children: React.ReactNode;
}) {
  const pathname = (await headers()).get("x-pathname") || "";
  // The AI-Scientist homepage (and the legacy /lab alias) render full-bleed with
  // their own top bar — no site NavBar/Footer/container. Everything else (the
  // preserved "previous version" pages) keeps the classic chrome.
  const standalone = pathname === "/" || pathname === "/lab" || pathname.startsWith("/lab/");

  return (
    <html lang="en">
      <head>
        <link rel="preconnect" href="https://fonts.googleapis.com" />
        <link
          rel="preconnect"
          href="https://fonts.gstatic.com"
          crossOrigin="anonymous"
        />
        <link
          href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap"
          rel="stylesheet"
        />
        <script
          type="application/ld+json"
          dangerouslySetInnerHTML={{ __html: JSON.stringify(jsonLd) }}
        />
      </head>
      <body
        style={{
          fontFamily: "Inter, system-ui, sans-serif",
          background: "#0f172a",
          color: "#f8fafc",
          minHeight: "100vh",
          margin: 0,
        }}
      >
        {standalone ? (
          children
        ) : (
          <>
            <NavBar />
            <VisitTracker />
            <main className="max-w-5xl mx-auto px-4 sm:px-6 py-8">{children}</main>
            <Footer />
          </>
        )}
      </body>
    </html>
  );
}
